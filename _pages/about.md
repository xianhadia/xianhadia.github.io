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

<figure style="margin: 1.5rem 0 2.5rem; text-align: center;">
  <img
    src="{{ '/assets/focusing_grating_demo.gif' | relative_url }}"
    alt="FDTD visualization of a grating coupler"
    style="display: inline-block; width: min(100%, 760px); max-width: 760px; height: auto; border: 0; box-shadow: none; border-radius: 0; background: transparent;"
  />
  <figcaption style="margin-top: 0.75rem; color: var(--global-text-color-light); font-size: 0.9rem;">
    Full wave validation of grating coupler design for focusing.
  </figcaption>
</figure>
