(() => {
  const framesUrl = document.currentScript.dataset.frames;
  const iterations = [
    ...Array.from({ length: 25 }, (_, i) => i),
    27,
    30,
    34,
    39,
    45,
    52,
    61,
    73,
    87,
    105,
    129,
    160,
  ];
  const playback = document.getElementById("gt-metasurface-playback");
  const replay = document.getElementById("gt-metasurface-replay");
  const scrubber = document.getElementById("gt-metasurface-scrubber");
  const slider = document.getElementById("gt-metasurface-iteration");
  const label = document.getElementById("gt-metasurface-step");
  const canvas = document.getElementById("gt-metasurface-frame");
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const sheet = new Image();
  let loaded;
  let scrubbing = false;
  slider.addEventListener("input", async () => {
    scrubbing = true;
    if (!loaded) {
      sheet.src = framesUrl;
      loaded = sheet.decode();
    }
    const index = slider.valueAsNumber;
    const step = iterations[index];
    const final = iterations.at(-1);
    slider.setAttribute("aria-valuetext", `Iteration ${step} of ${final}`);
    label.value = `${step} / ${final}`;

    try {
      await loaded;
    } catch {
      label.value = "Slider unavailable. Use Replay animation.";
      return;
    }
    if (!scrubbing || index !== slider.valueAsNumber) return;

    const { width, height } = canvas;
    const columns = sheet.naturalWidth / width;
    ctx.clearRect(0, 0, width, height);
    ctx.drawImage(
      sheet,
      (index % columns) * width,
      Math.floor(index / columns) * height,
      width,
      height,
      0,
      0,
      width,
      height,
    );
    playback.hidden = true;
    canvas.hidden = false;
  });

  replay.addEventListener("click", () => {
    scrubbing = false;
    canvas.hidden = true;
    playback.hidden = false;
  });
  slider.setAttribute("aria-valuetext", "Iteration 160 of 160");
  scrubber.hidden = false;
})();
