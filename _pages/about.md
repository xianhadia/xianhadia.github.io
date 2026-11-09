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

**Research Keywords:** Photonics, Computational Electromagnetics, Inverse Design, Adjoint Optimization, Scientific Computing

<div aria-hidden="true" style="height: 1.5rem;"></div>

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

One of the primary motivations for developing fast, approximate, yet physically grounded solvers of Maxwell's equations is not only to simulate electromagnetic phenomena, but also to **design devices that exhibit a desired electromagnetic response**.

Consider a metasurface: an optical device composed of subwavelength structures that manipulate the amplitude, phase, or polarization of light. Despite their relatively small physical dimensions, these devices can possess extraordinarily large design spaces. For example, a circular metasurface just 1 mm in diameter, consisting of individually tunable nanostructures arranged on a 400 nm lattice, could have nearly **five million independent design parameters**.

This raises a fundamental computational question: **How can we efficiently search a design space containing millions of degrees of freedom?**

One approach is to formulate the engineering task as a mathematical optimization problem. We begin by defining an _objective function_ that quantifies how closely a device's electromagnetic response matches its intended behavior. The geometry and material properties of the device become the design variables, and the goal is to iteratively update these parameters to improve the objective.

Mathematically, this can be expressed as

$$
\min_{\boldsymbol{\theta}}\; \mathcal{L}\left(\mathbf{E}(\boldsymbol{\theta}), \boldsymbol{\theta}\right)
$$

subject to Maxwell's equations, where \\(\boldsymbol{\theta}\\) represents the device's design parameters, \\(\mathbf{E}\\) is the resulting electromagnetic field, and \\(\mathcal{L}\\) measures the discrepancy between the simulated and desired performance.

However, directly computing the sensitivity of the objective to millions of parameters through finite differences would be prohibitively expensive, potentially requiring millions of additional electromagnetic simulations per optimization iteration.

This is where **adjoint optimization** becomes particularly powerful.

Rather than perturbing each design parameter individually, the adjoint method exploits the mathematical structure of the governing equations to compute the gradient of a scalar objective with respect to _all_ design parameters using just two electromagnetic solves: one forward simulation and one adjoint simulation.

Remarkably, the number of required solves does not grow with the number of design parameters. Whether a metasurface has hundreds or millions of geometric variables, the entire gradient can be obtained from these two solves, under the appropriate assumptions.

This connection between electromagnetic physics, numerical simulation, and gradient-based optimization is what makes inverse design such an interesting problem at the intersection of **applied mathematics, physics, and scientific computing**.

The animation below illustrates this process for a metasurface hologram, where the device's geometry is iteratively optimized to produce a desired optical field distribution. Use the slider to see how the design converges at a set iteration.

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
    Pillar geometry on the left and a zoomed view of the simulated far field on the right. This phase-only demo uses Gerchberg–Saxton iterations. The intensity color scale is fixed across frames and clips at its upper limit.
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
    Schematic optical layout. The focusing plane shows the simulated far-field intensity, and the distances are illustrative.
  </figcaption>
</figure>

The scalar model assigns each pillar a phase delay from an idealized, linear diameter-to-phase map. Relaxed Gerchberg–Saxton iterations alternate between the prescribed Gaussian input amplitude and the target far-field amplitude using forward and inverse FFTs. The optimizer allows some light to spill outside the displayed window so it can better match the target inside it. The model assumes unit transmission and independent pillars. [Georgia Tech logo reference](https://brand.gatech.edu/our-look/logos)

Here are some of my [projects]({{ '/projects/' | relative_url }}). The individual project pages are under construction.
