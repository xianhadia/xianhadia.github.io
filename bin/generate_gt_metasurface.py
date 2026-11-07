#!/usr/bin/env python3
"""Render the GT hologram GIF, poster, slider frames, and optical setup with NumPy and Pillow.

Rasterize Georgia Tech's public logo SVG at its intrinsic size, then run:

    curl -fsS https://www.gatech.edu/modules/contrib/gt_tools/images/gt-logo.svg -o /tmp/gt-logo.svg
    rsvg-convert /tmp/gt-logo.svg -o /tmp/gt-logo.png
    python bin/generate_gt_metasurface.py /tmp/gt-logo.png
"""

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageColor, ImageDraw, ImageFont


PILLARS = 64
FFT_SIZE = 3 * PILLARS
FIELD_CENTER = FFT_SIZE // 2
FIELD_HALF_WIDTH = 46
FIELD_VIEW = np.s_[
    FIELD_CENTER - FIELD_HALF_WIDTH : FIELD_CENTER + FIELD_HALF_WIDTH,
    FIELD_CENTER - FIELD_HALF_WIDTH : FIELD_CENTER + FIELD_HALF_WIDTH,
]
ITERATIONS = 160
CAPTURE = [*range(25), 27, 30, 34, 39, 45, 52, 61, 73, 87, 105, 129, ITERATIONS]
PANEL = 440
APERTURE = 416
LEFT, RIGHT, TOP = 40, 560, 134
INK = "#2b2035"
LABEL = "#817586"
SURFACE = "#f3ecf3"
PILLAR_COLORS = ["#514068", "#80507c", "#b95a84", "#dd7489", "#ef9a92"]
FIELD_COLORS = ["#1c152c", "#332046", "#642c62", "#a23d76", "#d75d85", "#f58e91", "#ffc5a2", "#fff1cf"]


def color_ramp(colors, values):
    rgb = np.array([ImageColor.getrgb(color) for color in colors])
    stops = np.linspace(0, 1, len(rgb))
    return np.stack([np.interp(values, stops, channel) for channel in rgb.T], axis=-1).astype(np.uint8)


def target_mask(logo):
    # The interlocking mark occupies the upper-left 174 × 109 pixels of this lockup.
    with Image.open(logo) as image:
        width, height = image.size
        gt = image.getchannel("A").crop((0, 0, round(width * 174 / 682), round(height * 109 / 122)))
    gt = gt.resize((84, 53), Image.Resampling.LANCZOS)
    mask = Image.new("L", (FFT_SIZE, FFT_SIZE))
    mask.paste(gt, (FFT_SIZE // 2 - gt.width // 2, FFT_SIZE // 2 - gt.height // 2))
    return np.asarray(mask) / 255


def optimize(mask):
    axis = (np.arange(PILLARS) - (PILLARS - 1) / 2) / PILLARS
    beam = np.exp(-(axis[:, None] ** 2 + axis[None, :] ** 2) / 0.37**2)
    target = np.sqrt(mask)
    target *= np.linalg.norm(beam) / np.linalg.norm(target)

    pad = (FFT_SIZE - PILLARS) // 2
    phase = np.full(beam.shape, np.pi)
    rng = np.random.default_rng(199)
    for step in range(ITERATIONS + 1):
        # Each pillar applies an independent, unit-magnitude phase delay.
        aperture = np.pad(beam * np.exp(1j * phase), pad)
        field = np.fft.fftshift(np.fft.fft2(aperture, norm="ortho"))
        if step in CAPTURE:
            yield step, phase / (2 * np.pi), np.abs(field) ** 2
        if step == ITERATIONS:
            break

        # Enforce the target magnitude in the image window. Allow damped spillover
        # outside the window so the optimizer has more freedom to fill the logo.
        # Seed only the target-plane phase to break symmetry. The initial array is uniform.
        target_phase = rng.uniform(-np.pi, np.pi, field.shape) if step == 0 else np.angle(field)
        projected = 0.94 * field
        projected[FIELD_VIEW] = target[FIELD_VIEW] * np.exp(1j * target_phase[FIELD_VIEW])
        back = np.fft.ifft2(np.fft.ifftshift(projected), norm="ortho")
        phase_delta = np.angle(back[pad:-pad, pad:-pad] * np.exp(-1j * phase))
        relaxation = 0.22 if step < 20 else 0.8
        phase = (phase + relaxation * phase_delta) % (2 * np.pi)


def font(size, bold=False):
    arial = "Arial Bold.ttf" if bold else "Arial.ttf"
    dejavu = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for path in (f"/System/Library/Fonts/Supplemental/{arial}", dejavu):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


def legend(canvas, x, label, low, high, colors, *, gamma=1):
    draw = ImageDraw.Draw(canvas)
    draw.text((x, 603), label, font=font(19), fill=LABEL, anchor="lm")
    draw.text((x + 224, 603), low, font=font(18), fill=LABEL, anchor="rm")
    bar = color_ramp(colors, np.linspace(0, 1, 120) ** gamma)
    canvas.paste(Image.fromarray(np.tile(bar, (10, 1, 1))), (x + 235, 598))
    draw.text((x + 365, 603), high, font=font(18), fill=LABEL, anchor="lm")


def pillar_panel(diameter_fraction):
    pillars = Image.new("RGB", (2 * PANEL, 2 * PANEL), SURFACE)
    geometry = ImageDraw.Draw(pillars)
    pitch = 2 * APERTURE / PILLARS
    origin = PANEL - APERTURE
    colors = color_ramp(PILLAR_COLORS, diameter_fraction)
    for (row, col), fraction in np.ndenumerate(diameter_fraction):
        x = origin + (col + 0.5) * pitch
        y = origin + (row + 0.5) * pitch
        radius = pitch * (0.18 + 0.25 * fraction)
        geometry.ellipse((x - radius + 1, y - radius + 2, x + radius + 1, y + radius + 2), fill="#b3a0b4")
        geometry.ellipse((x - radius, y - radius, x + radius, y + radius), fill=tuple(colors[row, col]))
    return pillars.resize((PANEL, PANEL), Image.Resampling.LANCZOS)


def intensity_panel(intensity, field_scale):
    # Magnify the central region, keeping the same intensity scale in every frame.
    crop = intensity[FIELD_VIEW]
    sampled = Image.fromarray(crop.astype(np.float32)).resize((PANEL, PANEL), Image.Resampling.BICUBIC)
    display = np.clip(np.asarray(sampled) / field_scale, 0, 1)
    return Image.fromarray(color_ramp(FIELD_COLORS, display**0.8))


def frame(step, diameter_fraction, intensity, field_scale):
    canvas = Image.new("RGBA", (1040, 638))
    draw = ImageDraw.Draw(canvas)
    draw.text((LEFT, 26), "Metasurface inverse design hologram", font=font(37, bold=True), fill=LABEL)
    draw.rounded_rectangle((784, 24, 1000, 69), radius=22, fill="#efe5ef")
    draw.text((892, 47), f"Iteration {step:03d} / {ITERATIONS}", font=font(21), fill=INK, anchor="mm")

    draw.text((LEFT, 115), "Pillar array", font=font(26, bold=True), fill=LABEL, anchor="ls")
    draw.text((LEFT + PANEL, 115), "64 × 64", font=font(20), fill=LABEL, anchor="rs")
    draw.text((RIGHT, 115), "Far-field intensity", font=font(26, bold=True), fill=LABEL, anchor="ls")
    draw.text((RIGHT + PANEL, 115), "Focusing plane", font=font(20), fill=LABEL, anchor="rs")

    canvas.paste(pillar_panel(diameter_fraction), (LEFT, TOP))
    canvas.paste(intensity_panel(intensity, field_scale), (RIGHT, TOP))
    for x in (LEFT, RIGHT):
        draw.rectangle((x, TOP, x + PANEL - 1, TOP + PANEL - 1), outline="#bdaabb")
    draw.line((505, 354, 533, 354), fill="#9b6b8b", width=3)
    draw.line((524, 345, 533, 354, 524, 363), fill="#9b6b8b", width=3, joint="curve")

    legend(canvas, LEFT, "Diameter", "Small", "Large", PILLAR_COLORS)
    legend(canvas, RIGHT, "Relative intensity", "0", "1+", FIELD_COLORS, gamma=0.8)
    return canvas


def optical_setup(diameter_fraction, intensity, field_scale):
    """Draw parallel cross sections in an orthographic view along the optical axis."""
    size = (1040, 540)
    canvas = Image.new("RGBA", tuple(2 * value for value in size))
    draw = ImageDraw.Draw(canvas)

    def project(x, y=0, z=0):
        # x is the propagation direction. y and z span the transverse planes.
        return 2 * (90 + x + 0.82 * y), 2 * (307 - 0.085 * x + 0.33 * y - z)

    def rectangle(x, half_width):
        return [project(x, y, z) for y, z in (
            (-half_width, half_width), (half_width, half_width),
            (half_width, -half_width), (-half_width, -half_width),
        )]

    def paste_plane(texture, corners):
        top_left, top_right, _, bottom_left = np.asarray(corners)
        basis = np.column_stack((top_right - top_left, bottom_left - top_left))
        inverse = np.diag(texture.size) @ np.linalg.inv(basis)
        transform = np.column_stack((inverse, -inverse @ top_left))
        plane = texture.convert("RGBA").transform(
            canvas.size, Image.Transform.AFFINE, transform.ravel(), Image.Resampling.BICUBIC
        )
        canvas.alpha_composite(plane)

    angles = np.linspace(0, 2 * np.pi, 65)

    def cross_section(x, radius):
        return [project(x, radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]

    def envelope(start, stop, entrance, exit):
        return [project(start, 0, entrance), project(stop, 0, exit),
                project(stop, 0, -exit), project(start, 0, -entrance)]

    # Translucent nested beam envelopes suggest the Gaussian profile at the entrance.
    beam_start, surface, focus = 12, 372, 777
    for layer, fraction in enumerate(np.linspace(1.1, 0.1, 23), start=1):
        opacity = round(255 * (1 - 0.935**layer))
        draw.polygon(envelope(beam_start, surface, 12 * fraction, 96 * fraction),
                     fill=(236, 97, 130, opacity))
    for x in (95, 178, 261):
        radius = 12 + 84 * (x - beam_start) / (surface - beam_start)
        draw.line(cross_section(x, radius), fill=(195, 87, 134, 95), width=2)

    # The downstream guide marks the diffracted beam, without tracing individual rays.
    draw.polygon(envelope(surface, focus, 90, 112), fill=(160, 80, 137, 22))
    for x in (522, 621, 711):
        draw.line(cross_section(x, 80), fill=(140, 88, 138, 60), width=2)
    for x in range(surface + 24, focus, 20):
        draw.line((project(x), project(min(x + 8, focus))), fill=(127, 76, 121, 145), width=2)

    # Substrate edges and the two transverse faces.
    front = rectangle(surface, 124)
    back = rectangle(surface + 18, 124)
    draw.polygon([front[0], front[1], back[1], back[0]], fill="#decede")
    draw.polygon([front[1], front[2], back[2], back[1]], fill="#ae8cac")
    paste_plane(pillar_panel(diameter_fraction), front)
    draw.line([*front, front[0]], fill="#90768e", width=3, joint="curve")

    screen = rectangle(focus, 142)
    paste_plane(intensity_panel(intensity, field_scale), screen)
    draw.line([*screen, screen[0]], fill="#83688b", width=4, joint="curve")

    draw.line(((2 * 119, 2 * 251), (2 * 119, 2 * 287)), fill="#a98ba1", width=3)
    draw.rounded_rectangle((2 * 63, 2 * 210, 2 * 175, 2 * 251), radius=16,
                           fill="#f6e7ef", outline="#a98ba1", width=2)
    draw.text((2 * 119, 2 * 231), "Laser", font=font(42, bold=True), fill=INK, anchor="mm")

    # Use a midtone for labels that sit directly on the page background.
    draw.text((80, 56), "Optical setup", font=font(72, bold=True), fill=LABEL)
    draw.text((80, 154), "Coherent Gaussian illumination", font=font(40), fill=LABEL)
    for x, y, name, detail in (
        (462, 444, "Metasurface", "Optimized pillar array"),
        (867, 448, "Focusing plane", "Simulated GT intensity"),
    ):
        draw.line((2 * x, 2 * y, 2 * x, 920), fill="#a98ba1", width=2)
        draw.text((2 * x, 954), name, font=font(48, bold=True), fill=LABEL, anchor="mm")
        draw.text((2 * x, 1011), detail, font=font(38), fill=LABEL, anchor="mm")
    return canvas.resize(size, Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("logo", type=Path, help="Transparent PNG rasterized from the official logo SVG")
    args = parser.parse_args()

    mask = target_mask(args.logo)
    states = list(optimize(mask))
    final_intensity = states[-1][2]
    field_scale = np.quantile(final_intensity[mask > 0.9], 0.75)
    frames = [frame(step, diameter, intensity, field_scale) for step, diameter, intensity in states]
    output = Path(__file__).resolve().parents[1] / "assets" / "img" / "gt-metasurface"
    frames[-1].save(output.with_name("gt-metasurface-poster.png"), optimize=True)
    setup = optical_setup(states[-1][1], final_intensity, field_scale)
    setup.save(output.with_name("gt-metasurface-setup.png"), optimize=True)

    # Pack the same captures into a sheet that the homepage loads on first scrub.
    columns = 5
    width, height = 780, 478
    rows = (len(frames) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * width, rows * height))
    for index, image in enumerate(frames):
        tile = image.resize((width, height), Image.Resampling.LANCZOS)
        sheet.paste(tile, ((index % columns) * width, (index // columns) * height))
    sheet.save(output.parent.parent / "gt-metasurface-frames.webp", quality=88, method=4)

    # A shared palette keeps stationary colors stable across GIF frames.
    samples = Image.new("RGB", (260, 160 * len(frames)))
    for index, image in enumerate(frames):
        samples.paste(image.resize((260, 160), Image.Resampling.BOX), (0, index * 160))
    transparent = 255
    palette = samples.quantize(colors=transparent)
    indexed = []
    for image in frames:
        quantized = image.convert("RGB").quantize(palette=palette, dither=Image.Dither.NONE)
        pixels = np.array(quantized)
        pixels[np.asarray(image.getchannel("A")) < 128] = transparent
        quantized.putdata(pixels.ravel())
        indexed.append(quantized)
    durations = [1200, *([100] * (len(frames) - 2)), 1600]
    indexed[0].save(
        output.with_suffix(".gif"), save_all=True, append_images=indexed[1:],
        duration=durations, transparency=transparent, background=transparent,
        disposal=1, optimize=True,
    )
    print(f"Mask-weighted far-field power: {np.sum(final_intensity * mask) / final_intensity.sum():.1%}")


if __name__ == "__main__":
    main()
