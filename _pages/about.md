---
layout: about
title: about
permalink: /
subtitle: PhD Candidate & Electrical Engineer

profile:
  align: right
  image: "prof_pic.jpg"
  image_circular: true # crops the image to make it circular
  more_info: >
    <p>Georgia Institute of Technology</p>
    <p>School of Computational Science and Engineering</p>
    <p>Atlanta, GA 30332</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items

latest_posts:
  enabled: true
  scrollable: false # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

I am a Ph.D. candidate in [Computational Science and Engineering at Georgia Tech](https://cse.gatech.edu/), advised by [Prof. Raphaël Pestourie](https://rpestourie.github.io/). My research lies at the intersection of **computational electromagnetics, inverse design, and photonic engineering**, with an emphasis on developing high-performance computational frameworks for solving complex electromagnetic design problems.

I develop **high-fidelity, computationally efficient electromagnetic solvers** to enable **scalable inverse design** of photonic devices under practical fabrication constraints. My work combines adjoint-based optimization, data-driven surrogate modeling, and high-performance computing to make the optimization of high-dimensional electromagnetic systems computationally tractable.

A central goal of my research is **bridging the gap between numerical simulation and physical realization**. Beyond computational methods, I have hands-on experience in photonic device fabrication, optical metrology, experimental characterization, and automation. I have taken photonic designs through the complete workflow, from numerical simulation and optimization to fabrication and experimental validation.

See my recent publications on [Google Scholar](https://scholar.google.com/citations?user=faPctLoAAAAJ&hl=en). Many are available on arXiv.

**Research Keywords:** Photonics, Computational Electromagnetics, Inverse Design, Adjoint Optimization, Scientific Computing

<div aria-hidden="true" style="height: 1.5rem;"></div>

Here's some of what I do:

Much of my work involves solving partial differential equations (PDEs) across complex geometries, materials, and boundary conditions—most notably, Maxwell's equations, which govern electromagnetic phenomena.

Although electromagnetism is well understood theoretically, accurately and efficiently solving Maxwell's equations for complex, high-dimensional photonic systems remains a significant computational challenge. This shifts modern photonic engineering from a problem of physics to **numerical methods and scientific computing**.

My research focuses on developing **efficient electromagnetic solvers and physics-based surrogate models** that balance computational cost with physical fidelity, enabling scalable simulation, optimization, and inverse design.

<figure style="margin: 2.5rem 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/em_simulation.jpg' | relative_url }}"
    alt="Full-wave finite-element simulation of an electromagnetic eigenmode"
    style="display: inline-block; width: min(100%, 760px); max-width: 760px; height: auto; border: 0; box-shadow: none; border-radius: 0; background: transparent;"
  />
  <figcaption style="margin-top: 0.75rem; color: var(--global-text-color-light); font-size: 0.9rem;">
    Full-wave finite-element simulation of an electromagnetic eigenmode, used as reference data for training and evaluating a physics-based surrogate model.
  </figcaption>
</figure>

Beyond simulating electromagnetic phenomena, a central goal of my research is to **design photonic devices with prescribed optical responses**.

Consider a metasurface composed of subwavelength nanostructures that manipulate light. Even a device just 1 mm in diameter, with individually tunable structures on a 400 nm period, can contain nearly **five million design parameters**. How do you even begin to search through this enormous design space?

**Inverse design** addresses this challenge by formulating the desired engineering function as a mathematical optimization problem. Rather than manually adjusting device geometries, we iteratively optimize their design parameters to maximize a chosen performance objective.

One particularly powerful approach is **adjoint optimization**, which enables the gradient of a scalar objective with respect to millions of design parameters to be computed using just two electromagnetic solves: one forward and one adjoint, under appropriate assumptions.

Combined with high-performance electromagnetic solvers, this makes the optimization of otherwise computationally prohibitive photonic devices tractable.

The interactive demonstration below illustrates iterative metasurface design for optical wavefront shaping.

<figure style="margin: 1.5rem 0; text-align: center;">
  <picture id="gt-metasurface-playback">
    <source
      media="(prefers-reduced-motion: reduce)"
      srcset="{{ '/assets/img/gt-metasurface-poster.png' | relative_url }}"
    />
    <img
      id="gt-metasurface-gif"
      src="{{ '/assets/img/gt-metasurface.gif' | relative_url }}"
      width="1040"
      height="638"
      alt="Left, a uniform pillar array evolves into an array of varying diameters. Right, the simulated far-field intensity evolves from a Gaussian spot into the Georgia Tech GT logo."
      style="display: block; width: 100%; height: auto; margin: 0 auto;"
    />
  </picture>
  <canvas
    id="gt-metasurface-frame"
    width="780"
    height="478"
    role="img"
    aria-label="Selected optimization frame showing the pillar array and far-field intensity"
    style="width: 100%; height: auto; vertical-align: top;"
    hidden
  ></canvas>
  <figcaption style="margin-top: 0.75rem; color: var(--global-text-color-light); font-size: 0.9rem;">
    Colors on the left show the pillar diameters. The right panel shows the resulting intensity in the focal plane.
  </figcaption>
  <div id="gt-metasurface-scrubber" style="margin: 0.75rem auto 0; max-width: 28rem;" hidden>
    <label for="gt-metasurface-iteration">Optimization iteration</label>
    <input id="gt-metasurface-iteration" type="range" min="0" max="36" value="36" style="display: block; width: 100%; accent-color: #c34c75;" />
    <output id="gt-metasurface-step" for="gt-metasurface-iteration">160 / 160</output>
  </div>
  <button
    type="button"
    id="gt-metasurface-replay"
    onclick="const gif = document.getElementById('gt-metasurface-gif'); gif.parentElement.querySelector('source')?.remove(); gif.src = gif.src.split('?')[0] + '?replay=' + Date.now();"
    style="margin-top: 0.75rem; padding: 0.4rem 0.8rem; border: 1px solid var(--global-divider-color); border-radius: 0.35rem; background: var(--global-bg-color); color: var(--global-text-color); cursor: pointer;"
  >
    Replay animation
  </button>
</figure>
<script defer src="{{ '/assets/js/gt-metasurface.js' | relative_url }}" data-frames="{{ '/assets/gt-metasurface-frames.webp' | relative_url }}"></script>

<figure style="margin: 2rem 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/gt-metasurface-setup.png' | relative_url }}"
    width="1040"
    height="540"
    loading="lazy"
    alt="Three-dimensional schematic with a labeled Gaussian laser beam on the left, a metasurface pillar array in the middle, and the GT intensity pattern on a parallel focusing plane to the right."
    style="display: block; width: 100%; height: auto; margin: 0 auto;"
  />
  <figcaption style="margin-top: 0.75rem; color: var(--global-text-color-light); font-size: 0.9rem;">
    In the intended setup, a laser provides coherent, monochromatic, linearly polarized illumination. The metasurface modulates the wavefront to form a hologram.
  </figcaption>
</figure>

The scalar model assigns each pillar a phase delay from an idealized, linear diameter-to-phase map. Relaxed Gerchberg–Saxton iterations alternate between the prescribed Gaussian input amplitude and the target far-field amplitude using forward and inverse FFTs. The optimizer allows some light to spill outside the displayed window so it can better match the target inside it. The model assumes unit transmission and independent pillars. [Georgia Tech logo reference](https://brand.gatech.edu/our-look/logos)

Here are some of my [projects]({{ '/projects/' | relative_url }}). The individual project pages are under construction.
