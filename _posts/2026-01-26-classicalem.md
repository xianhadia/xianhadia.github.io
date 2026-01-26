---
title: "Classical EM: Sources"
date: 2026-01-26
permalink: /posts/optics/classicalem_sources/
tags:
  - electromagnetism
  - physics
  - academic
---

# 1. Sources

The causal chain $\text{source} \;\longrightarrow\; \text{field} \;\longrightarrow\; \text{observable}$ reflects the factorization of physics into three components: excitations (sources), propagation through a medium (determined by materials and boundary conditions), and the mapping of fields into measurable quantiites (observations). The notes within my classical electromagnetism section will follow this structure with the first section modeling sources.

---

## 1.1 Maxwell’s Equations

Electromagnetic fields are vector-valued functions of space and time. Using the Cartesian unit vectors \(\hat{\mathbf{x}},\hat{\mathbf{y}},\hat{\mathbf{z}}\), a generic vector field is

\[
\mathbf{V}(x,y,z,t) = V_x\,\hat{\mathbf{x}} + V_y\,\hat{\mathbf{y}} + V_z\,\hat{\mathbf{z}}.
\]

With sources \((\rho_e,\mathbf{J})\) and \((\rho_m,\mathbf{M})\), the differential Maxwell equations are

\[
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M},
\]
\[
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J},
\]
\[
\nabla \cdot \mathbf{D} = \rho_e,
\quad
\nabla \cdot \mathbf{B} = \rho_m.
\]

In integral form,

\[
\oint_{\partial S} \mathbf{E}\cdot d\boldsymbol{\ell}
= -\int_S \left( \frac{\partial \mathbf{B}}{\partial t} + \mathbf{M} \right)\cdot d\mathbf{S},
\]
\[
\oint_{\partial S} \mathbf{H}\cdot d\boldsymbol{\ell}
= \int_S \left( \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J} \right)\cdot d\mathbf{S},
\]
\[
\int_S \mathbf{D}\cdot d\mathbf{S}
= \int_V \rho_e\,dV,
\quad
\int_S \mathbf{B}\cdot d\mathbf{S}
= \int_V \rho_m\,dV.
\]

Magnetic sources have no known physical realization, but including them yields a more symmetric and duality-friendly formalism.

---

## 1.2 Constitutive Relations

Maxwell’s equations couple to matter through material laws:

\[
\mathbf{D} = \epsilon\,\mathbf{E}, \qquad \mathbf{B} = \mu\,\mathbf{H}, \qquad \mathbf{J} = \sigma\,\mathbf{E}.
\]

In general:

- \(\epsilon,\mu,\sigma\) can be **complex-valued** (lossy media),
- they may be **functions of space** \(\epsilon(\mathbf{r})\),
- they may depend on **frequency** (temporal dispersion),
- they may depend on **wavevector** (spatial dispersion).

More complex media include:

- **Nonlinear:**  
  \[
  \mathbf{P} = \epsilon_0(\chi^{(1)}\mathbf{E} + \chi^{(2)}\mathbf{E}^2 + \cdots)
  \]
- **Anisotropic:** tensor-valued \(\epsilon\) and \(\mu\),
- **Bianisotropic / chiral:**  
  \[
  \mathbf{D} = \epsilon \mathbf{E} + \xi \mathbf{H}, \quad \mathbf{B} = \zeta \mathbf{E} + \mu \mathbf{H}
  \]

More detailed material models appear later; linear isotropic media suffice for many classical systems.

---

### ▶️ Example: Field of a Point Charge (Interactive)

<details>
<summary><b>Click to reveal example</b></summary>

For a point charge \(q\) at the origin:

\[
\rho_e(\mathbf{r}) = q\,\delta(\mathbf{r}), \quad \partial_t = 0, \quad \mathbf{J}=0.
\]

Then

\[
\nabla \cdot \mathbf{D} = \rho_e, \quad \nabla \times \mathbf{E} = 0.
\]

Using Gauss’s law over a sphere of radius \(R\):

\[
D_r(R)\,4\pi R^2 = q \quad \Rightarrow \quad \mathbf{E} = \frac{q}{4\pi\epsilon_0 R^2}\hat{\mathbf{r}}.
\]

Alternatively, using \(\mathbf{E}=-\nabla\phi\), Poisson’s equation gives

\[
\phi(\mathbf{r}) = \frac{q}{4\pi\epsilon_0 R},
\quad
\mathbf{E} = -\nabla\phi,
\]

recovering Coulomb’s law.

</details>

---

## 1.3 Continuity and Charge Conservation

Local charge conservation is expressed as

\[
\nabla \cdot \mathbf{J} = -\frac{\partial \rho_e}{\partial t}.
\]

Integrating over a fixed volume \(V\),

\[
\frac{d}{dt} \int_V \rho_e\,dV
= -\oint_{\partial V} \mathbf{J}\cdot d\mathbf{S}.
\]

Thus the charge in a region can only change via current crossing its boundary.

Charge conservation is **not independent** of Maxwell’s equations:

Taking \(\nabla\cdot\) of Ampère–Maxwell and using \(\nabla\cdot\nabla\times\!\bullet=0\) plus Gauss’s law recovers the continuity equation.

---

### ▶️ Example: Steady Current in a Wire (Interactive)

<details>
<summary><b>Click to reveal example</b></summary>

For a DC current \(I\):

\[
\partial_t \rho_e = 0 \quad \Rightarrow\quad \nabla\cdot\mathbf{J}=0.
\]

If \(I\) changes suddenly, transient charge buildup temporarily violates \(\nabla\cdot\mathbf{J}=0\), restoring it once steady state resumes.

</details>

---

## 1.4 Boundary Conditions

At an interface with unit normal \(\hat{\mathbf{n}}\):

\[
\hat{\mathbf{n}}\times(\mathbf{E}_1-\mathbf{E}_2) = -\mathbf{M}_s,
\]
\[
\hat{\mathbf{n}}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_{es},
\]
\[
\hat{\mathbf{n}}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s,
\]
\[
\hat{\mathbf{n}}\cdot(\mathbf{B}_1-\mathbf{B}_2) = \rho_{ms}.
\]

The sign convention always appears as *region 1 minus region 2*.

---

### ▶️ Example: Planar Interface at \(z=0\)

<details>
<summary><b>Click to reveal example</b></summary>

Let \(\hat{\mathbf{n}}=\hat{\mathbf{z}}\). Then the tangential \(E\) components satisfy

\[
E_x^{(1)} = E_x^{(2)}, \qquad
E_y^{(1)} = E_y^{(2)}.
\]

Gauss yields

\[
D_z^{(1)} - D_z^{(2)} = \rho_{es}.
\]

</details>

---

## 1.5 Explicit vs Implicit Sources

Sources in electromagnetism may be:

- **explicit**, via \(\rho_e,\mathbf{J},\rho_m,\mathbf{M}\) in the PDEs,
- **implicit**, via boundary/interface conditions.

Example equivalences:

- physical antenna current,
- equivalent surface currents on a fictitious surface,
- prescribed boundary fields.

Modeling often involves choosing the most convenient representation.

---

## 1.6 Deriving the Wave Equation

In a homogeneous, source-free, lossless medium:

\[
\rho_e = \rho_m = 0,\quad \mathbf{J}=\mathbf{M}=0,\quad \sigma=0.
\]

Using \(\mathbf{D}=\epsilon\mathbf{E}\), \(\mathbf{B}=\mu\mathbf{H}\):

\[
\nabla \times \mathbf{E} = -\mu\,\partial_t \mathbf{H},\qquad
\nabla \times \mathbf{H} = \epsilon\,\partial_t \mathbf{E}.
\]

Taking curl of Faraday:

\[
\nabla \times (\nabla \times \mathbf{E}) = -\mu\epsilon \frac{\partial^2\mathbf{E}}{\partial t^2}.
\]

Using the identity:

\[
\nabla\times\nabla\times\mathbf{E} = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E},
\]

and noting \(\nabla\cdot\mathbf{E}=0\),

\[
\nabla^2 \mathbf{E} = \mu\epsilon\,\partial_t^2 \mathbf{E}.
\]

A similar expression holds for \(\mathbf{H}\).

---

## 1.7 General Solution of the Wave Equation

In 1D for fields depending on \(z,t\),

\[
\mathbf{E}(z,t)=\hat{\mathbf{x}}E_x(z,t),\quad
\mathbf{H}(z,t)=\hat{\mathbf{y}}H_y(z,t),
\]

yielding the scalar PDE

\[
\partial_z^2 E_x = \frac{1}{v_p^2}\partial_t^2 E_x,\qquad v_p = \frac{1}{\sqrt{\mu\epsilon}}.
\]

The general solution is

\[
E_x(z,t) = K_1 f\!\left(t - \frac{z}{v_p}\right) + K_2 g\!\left(t + \frac{z}{v_p}\right),
\]

representing waves traveling in \(\pm z\).

---

## 1.8 Special Choices of \(f\) and \(g\)

Maxwell’s solutions form a linear vector space. In 1D, right/left traveling waves form a useful basis. In 3D, the Helmholtz eigenbasis arises:

\[
\nabla^2 \tilde{E} + k^2 \tilde{E} = 0 \quad\Rightarrow\quad
\tilde{E}(\mathbf{r}) = E_0 e^{-j\mathbf{k}\cdot\mathbf{r}},
\]

and arbitrary fields can be expressed as

\[
\tilde{E}(\mathbf{r}) = \int \tilde{E}(\mathbf{k})\,e^{-j\mathbf{k}\cdot\mathbf{r}}\,d^3\mathbf{k}.
\]

---

### ▶️ Example: Canonical Mode Families (Interactive)

<details>
<summary><b>Click to reveal modes</b></summary>

#### Sinusoidal Plane Waves

Choosing
\[
f(t-z/v_p)=\cos(\omega t - \beta z),\quad \beta=\omega/v_p
\]

yields a monochromatic plane wave.

#### Spherical Modes

\[
\tilde{E}(r)=\frac{A}{r}e^{-jkr}
\]

#### Cylindrical Modes

\[
\tilde{E}(\rho,\phi,z)=J_m(k_\rho\rho)e^{jm\phi}e^{-j\beta z}.
\]

</details>

---

## 1.9 Non-Monochromatic Fields

Through Fourier synthesis:

\[
E(z,t)=\int \tilde{E}(\omega)e^{j(\omega t - \beta(\omega)z)}\,d\omega.
\]

Dispersion induces waveform distortion.

---

## 1.10 Phasor Representation

A real sinusoidal field:

\[
E(z,t)=A\cos(\omega t - \beta z + \phi)
= \Re\!\{ A e^{j(\omega t - \beta z + \phi)}\}.
\]

Suppressing \(e^{j\omega t}\) yields the **phasor**

\[
\tilde{E}(z)=A e^{-j\beta z}e^{j\phi}.
\]

In a homogeneous medium, frequency-domain Maxwell reduces to an eigenproblem:

\[
\nabla\times\nabla\times\tilde{\mathbf{E}} = k^2 \tilde{\mathbf{E}},\qquad k=\omega\sqrt{\mu\epsilon}.
\]

Because free space is translationally invariant, plane waves

\[
\tilde{\mathbf{E}}(\mathbf{r}) = \mathbf{E}_0 e^{-j\mathbf{k}\cdot\mathbf{r}}
\]

form a complete basis.
