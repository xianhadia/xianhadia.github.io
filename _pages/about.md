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

I am a Ph.D. candidate in Computational Science and Engineering at <a href='https://gatech.edu/'>Georgia Tech</a>, advised by [Prof. Raphaël Pestourie](https://scholar.google.com/citations?user=Lxv3W74AAAAJ&hl=en), specializing in large-scale inverse design for nanophotonics. My research focuses on developing high-performance computational frameworks to solve complex electromagnetic inverse problems, bridging adjoint-based optimization, data-driven surrogate modeling, and scalable numerical solvers.

I build custom physics solvers utilizing finite-difference methods (FDTD, FDFD), finite element methods (FEM), and rigorous coupled-wave analysis (RCWA), alongside tools like Tidy3D, MEEP, COMSOL, and Ansys Lumerical. To make large-area nanophotonic device optimization computationally tractable, I architect high-performance computing (HPC) workflows that leverage multi-GPU parallelization, domain decomposition, and tensor-based linear algebra formulations. Beyond theoretical and algorithmic development, I bridge simulation with hardware by designing fabrication-constrained metasurfaces—for beamforming, focusing, and arbitrary wavefront engineering—and validating them via hands-on cleanroom lithography, optical metrology, and experimental bench characterization.

**Keywords:** Nanophotonics · Inverse Design · Adjoint Optimization · Computational Electromagnetics · Surrogate Models · Scientific Computing

Here is a glimpse into what I do. Much of my work involves modeling and solving partial differential equations (PDEs) under various boundary conditions and across complex geometries - most notably, Maxwell's equations, which govern electromagnetic phenomena.

My research lies at the intersection of numerical methods, physics, and scientific computing. Classical electromagnetism is one of the most thoroughly understood areas of physics, yet efficiently solving Maxwell's equations across complex geometries, material configurations, and operating conditions remains a significant computational challenge. While the underlying physics is well established, translating these equations into practical engineering design tools requires increasingly sophisticated computational methods.

One of my primary research goals is to develop efficient numerical methods and physics-based surrogate models that balance computational cost with the appropriate level of physical fidelity, enabling faster simulation, optimization, and inverse design of complex engineering systems.

<figure style="margin: 2.5rem 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/em_simulation.jpg' | relative_url }}"
    alt="Electromagnetic simulation"
    style="display: inline-block; width: min(100%, 760px); max-width: 760px; height: auto; border: 0; box-shadow: none; border-radius: 0; background: transparent;"
  />
  <figcaption style="margin-top: 0.75rem; color: var(--global-text-color-light); font-size: 0.9rem;">
    Helmholtz equation, \(\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0\), and visualization with lateral boundary conditions.
  </figcaption>
</figure>

## Metasurface inverse design hologram

A Gaussian beam illuminates a 64 × 64 array of pillars. The uniform array starts with a single bright spot in the far field. As the pillar diameters change, they delay different parts of the wavefront by different amounts. The transmitted waves interfere to form the interlocking GT.

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
    Pillar geometry on the left and a zoomed view of the simulated far field on the right. The intensity color scale is fixed across frames and clips at its upper limit.
  </figcaption>
  <div id="gt-metasurface-scrubber" style="margin: 0.75rem auto 0; max-width: 28rem;" hidden>
    <label for="gt-metasurface-iteration">Optimization iteration</label>
    <input id="gt-metasurface-iteration" type="range" min="0" max="36" value="36" style="display: block; width: 100%;" />
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
    Schematic optical layout. The focusing plane shows the simulated far-field intensity, and the distances are illustrative.
  </figcaption>
</figure>

The scalar model assigns each pillar a phase delay from an idealized, linear diameter-to-phase map. Relaxed Gerchberg–Saxton iterations alternate between the prescribed Gaussian input amplitude and the target far-field amplitude using forward and inverse FFTs. The optimizer allows some light to spill outside the displayed window so it can better match the target inside it. The model assumes unit transmission and independent pillars. [Georgia Tech logo reference](https://brand.gatech.edu/our-look/logos)

Here are some of my [projects]({{ '/projects/' | relative_url }}). The individual project pages are under construction.
