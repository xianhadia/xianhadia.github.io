---
layout: page
title: projects
permalink: /projects/
description: Projects page under construction.
nav: true
nav_order: 2
---

Here are some of my projects. The individual project pages are currently under construction.

<div class="projects">
  {% for project in site.projects %}
    <div class="project-card" style="margin: 1.5rem 0; padding: 1.25rem; border: 1px solid var(--global-divider-color); border-radius: 0.5rem;">
      <h2 style="margin-bottom: 0.5rem;"><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
      <p style="margin-bottom: 0;">{{ project.description }}</p>
    </div>
  {% endfor %}
</div>
