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

The causal chain source $\longrightarrow$ field  $\longrightarrow$ observable reflects the factorization of physics into three components: excitations (sources), propagation through a medium (determined by materials and boundary conditions), and measuring quantities (observations). The notes within my classical electromagnetism section will follow this structure with the first section modeling sources.

## 1.1 Maxwell’s Equations

Electromagnetic fields are vector-valued functions of space and time. Using the Cartesian unit vectors $\hat{\mathbf{x}},\hat{\mathbf{y}},\hat{\mathbf{z}}$, a generic vector field is written as 

$$
\mathbf{V}(x,y,z,t) = V_x\,\hat{\mathbf{x}} + V_y\,\hat{\mathbf{y}} + V_z\,\hat{\mathbf{z}}.
$$

The electric and magnetic fields are denoted by $\mathbf{E}$ and $\mathbf{H}$, and the electric and magnetic flux densities by $\mathbf{D}$ and $\mathbf{B}$, respectively. In the presence of electric and magnetic charge and current densities $(\rho_e, \mathbf{J})$ and $(\rho_m, \mathbf{M})$, Maxwell's equations in differential form are

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M}
$$
$$
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J}
$$
$$
\nabla \cdot \mathbf{D} = \rho_e
\quad
\nabla \cdot \mathbf{B} = \rho_m
$$


In integral form over an oriented surface $S$ with boundary curve $\partial S$, these become


$$
\oint_{\partial S} \mathbf{E} \cdot d\boldsymbol{\ell} = - \int_{S} \left( \frac{\partial \mathbf{B}}{\partial t} + \mathbf{M} \right) \cdot d\mathbf{S}
$$
$$
\oint_{\partial S} \mathbf{H} \cdot d\boldsymbol{\ell} = \phantom{-} \int_{S} \left( \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J} \right) \cdot d\mathbf{S}
$$
$$
\int_{S} \mathbf{D} \cdot d\mathbf{S} = \int_{V} \rho_e\, dV
$$
$$ 
\int_{S} \mathbf{B} \cdot d\mathbf{S} = \int_{V} \rho_m\, dV
$$ 

where $V$ is the volume enclosed by $S$. The magnetic charge densities and currents introduced above are not known to exist physically but including them now allows for symmetry within Maxwell's equations and enables later use of duality transformations.


## 1.2 Constitutive Relations

Maxwell’s equations couple to matter through material laws:

$$
\mathbf{D} = \epsilon\,\mathbf{E}, \qquad \mathbf{B} = \mu\,\mathbf{H}, \qquad \mathbf{J} = \sigma\,\mathbf{E}.
$$

where $\epsilon$, $\mu$, and $\sigma$ are the permittivity, permeability, and conductivity of the material. In general these material parameters may be \textbf{complex-valued} with the imaginary part representing loss to the system. Additionally, we model the fields in different types of media the following way

- **Nonlinear:**  
  $$
  \mathbf{P} = \epsilon_0(\chi^{(1)}\mathbf{E} + \chi^{(2)}\mathbf{E}^2 + \cdots)
  $$
- **Anisotropic:** tensor-valued $\epsilon$ and $\mu$,
- **Bianisotropic / chiral:**  
  $$
  \mathbf{D} = \epsilon \mathbf{E} + \xi \mathbf{H}, \quad \mathbf{B} = \zeta \mathbf{E} + \mu \mathbf{H}
  $$
 - **Dispersive media** have material parameters depending on frequency (temporal dispersion), and may also depend on wavevector (spatial dispersion), leading to convolutional constitutive laws in time or space.

 We will cover materials in a later section. For now, simple linear relationships are sufficient for many classical problems and can even account for inhomogenous media if their material properties can be written as functions space $\epsilon(\mathbf{r})$, $\mu(\mathbf{r})$, and $\sigma(\mathbf{r})$.



<details>
<summary><b>Example: Field of a Point Charge</b></summary>

Consider the simplest electrostatic example: a point charge $q$ located at the origin in free space. In this case, the charge density is

$$
\rho_e(\mathbf{r}) = q\,\delta(\mathbf{r}), \quad \partial_t = 0, \quad \mathbf{J}=0.
$$

and all fields are time-independent, so that $\partial/\partial t = 0$ and $\mathbf{J} = \mathbf{0}$. Therefore, 

$$
\nabla \cdot \mathbf{D} = \rho_e, \quad \nabla \times \mathbf{E} = 0.
$$

with the relation to free space as $\mathbf{D} = \epsilon_0 \mathbf{E}$

Using Gauss’s law over a sphere of radius \(R\):

$$
D_r(R)\,4\pi R^2 = q \quad \Rightarrow \quad \mathbf{E} = \frac{q}{4\pi\epsilon_0 R^2}\hat{\mathbf{r}}.
$$

Alternatively, using \(\mathbf{E}=-\nabla\phi\), Poisson’s equation gives

$$
\phi(\mathbf{r}) = \frac{q}{4\pi\epsilon_0 R},
\quad
\mathbf{E} = -\nabla\phi,
$$

recovering Coulomb’s law.

</details>


This simple example highlights two complementary routes for solving Maxwell's equations: using the integral form together with symmetry arguments, or using the differential
form and solving the resulting partial differential equations (here, Poisson's equation for $\phi$).



## 1.3 Continuity and Charge Conservation

Charge conservation imposes a local constraint on admissible electromagnetic fields. In differential form, the conservation of electric (and magnetic) charge is expressed through the continuity equations

$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho_e}{\partial t}.
$$

Integrating over a fixed volume \(V\),

$$
\frac{d}{dt} \int_V \rho_e\,dV
= -\oint_{\partial V} \mathbf{J}\cdot d\mathbf{S}.
$$

Thus the charge in a region can only change via current crossing its boundary.

Charge conservation is **not independent** of Maxwell’s equations. Taking \(\nabla\cdot\) of Ampère–Maxwell and using \(\nabla\cdot\nabla\times\!\bullet=0\) plus Gauss’s law recovers the continuity equation.

At a more abstract level, conservation laws arise from symmetries. In electromagnetism, global gauge invariance implies conservation of electric charge (Noether's theorem), whose local expression is precisely the continuity equation. The continuity equation in turn constrains the permissible electromagnetic fields and sources.

<details>
<summary><b>Example: Steady Current in a Wire</b></summary>

For a DC current \(I\):

$$
\partial_t \rho_e = 0 \quad \Rightarrow\quad \nabla\cdot\mathbf{J}=0.
$$

If \(I\) changes suddenly, transient charge buildup temporarily violates \(\nabla\cdot\mathbf{J}=0\), restoring it once steady state resumes.

</details>


## 1.4 Boundary Conditions

Maxwell’s equations in differential form assume the field vectors are differentiable. However, at the interface between two different media, the material parameters ($\epsilon, \mu, \sigma$) often change abruptly. To handle this (alongside the mathematical necessity of coupled PDEs requiriing certain conditions for a unique solution), we introduce boundary conditions

Let an interface separate **Medium 1** from **Medium 2**. We define the unit normal vector $\hat{\mathbf{n}}$ to point **from Medium 2 into Medium 1**.
$$
\hat{\mathbf{n}} = \hat{\mathbf{n}}_{2 \to 1}
$$


| Component | Boundary Condition | Physical Implication |
| :--- | :--- | :--- |
| **Tangential E** | $\hat{\mathbf{n}} \times (\mathbf{E}_1 - \mathbf{E}_2) = -\mathbf{M}_s$ | $\mathbf{E}_{tan}$ is continuous unless magnetic current exists. |
| **Tangential H** | $\hat{\mathbf{n}} \times (\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$ | $\mathbf{H}_{tan}$ is continuous unless electric current exists. |
| **Normal D** | $\hat{\mathbf{n}} \cdot (\mathbf{D}_1 - \mathbf{D}_2) = \rho_{es}$ | $\mathbf{D}_{norm}$ jumps by the surface charge density. |
| **Normal B** | $\hat{\mathbf{n}} \cdot (\mathbf{B}_1 - \mathbf{B}_2) = \rho_{ms}$ | $\mathbf{B}_{norm}$ is continuous (unless magnetic monopoles exist). |

Sources enter Maxwell's theory in two distinct ways: **explicitly** as volumetric densities ($\rho, \mathbf{J}$) driving the differential equations, or **implicitly** as surface singularities ($\rho_s, \mathbf{J}_s$) enforcing discontinuities at boundaries. 

In many practical electromagnetic problems, explicit volumetric sources are absent from the region of interest. Instead, the physics is driven by equivalent surface charges or currents defined at interfaces. A key skill in modeling is recognizing that these descriptions are often physically equivalent, differing only in mathematical convenience. More on this will be expanded on in the next chapter.

The following example applies the boundary condition approach. It solves for the radiation from a magnetic current sheet, demonstrating how a **non-zero** source ($\mathbf{M}_s$) forces a discontinuity in the tangential electric field and the **absence** of a source ($\mathbf{J}_s = 0$) preserves continuity in the tangential magnetic field.

<details>
<summary><b>Example: Field of a Magnetic Current Sheet</b></summary>

This example demonstrates how to use boundary conditions to solve for unknown fields. It also highlights a scenario where the electric field is discontinuous, but the magnetic field is continuous.

**Problem Setup**
Consider free space separated into two regions by the plane $z=0$. A **magnetic surface current** flows on this interface:
$$
\mathbf{M}_s = M_0 \hat{\mathbf{y}} \quad \text{at } z=0
$$
There is **no electric surface current** ($\mathbf{J}_s = 0$). We wish to find the electromagnetic waves radiating away from this sheet.

**1. Apply Conventions**
* Interface normal $\hat{\mathbf{n}} = \hat{\mathbf{z}}$.
* Region 1 is $z>0$; Region 2 is $z<0$.
* (note: one could easily have chosen $\hat{\mathbf{n}} = \hat{\mathbf{-z}}$ since it is also normal to the interface; however, subsequent signs would also have vto be revised to keep consistent with this normal vector choice.

**2. Formulate Field Ansatz (Guess)**
By symmetry, the sheet radiates plane waves traveling outward ($+z$ in Reg 1, $-z$ in Reg 2).
* **Region 1 ($z>0$):**
    $$\mathbf{E}_1 = E_0 \hat{\mathbf{x}} e^{-jkz} \quad \Rightarrow \quad \mathbf{H}_1 = \frac{E_0}{\eta_0} \hat{\mathbf{y}} e^{-jkz}$$
* **Region 2 ($z<0$):**
    $$\mathbf{E}_2 = -E_0 \hat{\mathbf{x}} e^{+jkz} \quad \Rightarrow \quad \mathbf{H}_2 = \frac{-E_0}{-\eta_0} \hat{\mathbf{y}} e^{+jkz} = \frac{E_0}{\eta_0} \hat{\mathbf{y}} e^{+jkz}$$
    *(Note: We guessed the sign of $E_2$ to be negative, but let's verify if this satisfies the conditions).*

**3. Enforce Boundary Conditions at $z=0$**

* **Condition A: Magnetic Tangents ($\mathbf{J}_s = 0$)**
    Since there is no electric current $\mathbf{J}_s$, the tangential $\mathbf{H}$ must be continuous:
    $$
    \hat{\mathbf{n}} \times (\mathbf{H}_1 - \mathbf{H}_2) = 0 \implies \mathbf{H}_{1, tan} = \mathbf{H}_{2, tan}
    $$
    At $z=0$:
    $$
    \frac{E_0}{\eta_0}\hat{\mathbf{y}} = \frac{E_0}{\eta_0}\hat{\mathbf{y}}
    $$
    This holds true. Our ansatz correctly assumes $\mathbf{H}$ is continuous.

* **Condition B: Electric Tangents ($\mathbf{M}_s \neq 0$)**
    Here, $\mathbf{M}_s$ causes a discontinuity:
    $$
    \hat{\mathbf{z}} \times (\mathbf{E}_1 - \mathbf{E}_2) = -\mathbf{M}_s
    $$
    Substitute the fields at $z=0$:
    $$
    \hat{\mathbf{z}} \times (E_0 \hat{\mathbf{x}} - (-E_0 \hat{\mathbf{x}})) = -M_0 \hat{\mathbf{y}}
    $$
    $$
    \hat{\mathbf{z}} \times (2E_0 \hat{\mathbf{x}}) = -M_0 \hat{\mathbf{y}}
    $$
    Using $\hat{\mathbf{z}} \times \hat{\mathbf{x}} = \hat{\mathbf{y}}$:
    $$
    2E_0 \hat{\mathbf{y}} = -M_0 \hat{\mathbf{y}}
    $$

**4. Solution**
Solving for the field amplitude:
$$
E_0 = -\frac{M_0}{2}
$$

Thus, the magnetic current sheet generates an electric field that "jumps" from $+M_0/2$ to $-M_0/2$ across the boundary, while the magnetic field passes through the boundary unchanged.

</details>

## 1.5 Derivation of the Wave Equation

Consider a source-free, homogeneous, lossless region:
$$
\rho_e = \rho_m = 0, \qquad \mathbf{J}=\mathbf{M}=0, \qquad \sigma=0.
$$
With the constitutive relations $\mathbf{D}=\epsilon\mathbf{E}$ and $\mathbf{B}=\mu\mathbf{H}$, Maxwell's curl equations become
$$
\nabla \times \mathbf{E} = -\mu\frac{\partial \mathbf{H}}{\partial t}
$$
$$
\nabla \times \mathbf{H} = \epsilon\frac{\partial \mathbf{E}}{\partial t}
$$
Taking the curl of Faraday's law:
$$
\nabla \times (\nabla \times \mathbf{E}) = -\mu\frac{\partial}{\partial t}(\nabla \times \mathbf{H}) = -\mu\epsilon \frac{\partial^2\mathbf{E}}{\partial t^2}.
$$
Using the vector identity $\nabla \times(\nabla\times \mathbf{E})=\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E}$ and the fact that in a homogeneous, source-free region $\nabla\cdot\mathbf{E}=0$, the electric field satisfies the **vector wave equation**:

$$
\nabla^2 \mathbf{E} = \mu\epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2}.
$$

A similar equation holds for $\mathbf{H}$.

In reality, an environment is often heterogeneous (composed of various materials) and contains sources. We cover this simple case first because it exposes the essential structure of electromagnetic propagation without the bookkeeping overhead of dispersion, loss, or inhomogeneity. Once the basic machinery is understood in a homogeneous medium, more realistic environments can be treated as perturbations or layered compositions using this same underlying framework.

## 1.6 General Solution of the Wave Equation

The vector wave equations derived above represent three coupled scalar partial differential equations. In Cartesian coordinates:
$$
\nabla^2 \mathbf{E} = \hat{\mathbf{x}}\nabla^2 E_x + \hat{\mathbf{y}}\nabla^2 E_y + \hat{\mathbf{z}}\nabla^2 E_z
$$
Thus, the general electromagnetic field may consist of arbitrary superpositions of solutions in the $x$, $y$, and $z$ directions. The polarization and relative amplitudes are determined by the excitation and boundary conditions.

In many geometries of interest, symmetry allows us to reduce the problem. For example, in a one-dimensional case where the fields depend only on $z$ and $t$ and are polarized along a fixed direction, we may write:
$$
\mathbf{E}(z,t) = \hat{\mathbf{x}}\,E_x(z,t), \qquad \mathbf{H}(z,t) = \hat{\mathbf{y}}\,H_y(z,t)
$$
This reduces the vector wave equation to the scalar form:
$$
\frac{\partial^2 E_x}{\partial z^2} = \frac{1}{v_p^2}\frac{\partial^2 E_x}{\partial t^2}, \qquad v_p = \frac{1}{\sqrt{\mu\epsilon}}
$$
The general solution of this one-dimensional wave equation (d'Alembert's solution) is:
$$
E_x(z,t) = K_1 f\!\left(t-\frac{z}{v_p}\right) + K_2 g\!\left(t+\frac{z}{v_p}\right)
$$
where $f$ and $g$ are arbitrary functions describing waves traveling in the $+z$ and $-z$ directions, respectively.

### Wave Parameters and Fundamental Relationships
To solve for a specific wave, we must relate the space-time properties of the wave to the material properties of the medium.

The speed of propagation is determined strictly by the medium:
$$
v_p = \frac{1}{\sqrt{\mu\epsilon}} = \frac{1}{\sqrt{\mu_0\epsilon_0 \mu_r \epsilon_r}} = \frac{c}{\sqrt{\mu_r \epsilon_r}} = \frac{c}{n}
$$
where $c \approx 3 \times 10^8$ m/s is the speed of light in vacuum and $n$ is the refractive index.

For a time-harmonic wave (oscillating at a single frequency $f$), we define:
* **Angular Frequency:** $\omega = 2\pi f$ (rad/s)
* **Wavenumber:** $k = \frac{\omega}{v_p} = \omega\sqrt{\mu\epsilon}$ (rad/m)
* **Wavelength:** $\lambda = \frac{2\pi}{k} = \frac{v_p}{f}$ (m)

These quantities are linked by the dispersion relation:
$$
v_p = \frac{\omega}{k} = f\lambda
$$

<details>
<summary><b>Example: Solving for Wave Parameters</b></summary>

Consider a 2.4 GHz WiFi signal propagating through a non-magnetic wall made of dry concrete ($\epsilon_r \approx 4.5, \mu_r = 1$).

**1. Frequency Parameters**
$$
f = 2.4 \times 10^9 \, \text{Hz}
$$
$$
\omega = 2\pi f \approx 1.51 \times 10^{10} \, \text{rad/s}
$$

**2. Phase Velocity**
The wave slows down inside the dielectric:
$$
v_p = \frac{c}{\sqrt{\epsilon_r}} = \frac{3\times 10^8}{\sqrt{4.5}} \approx \frac{3\times 10^8}{2.12} \approx 1.41 \times 10^8 \, \text{m/s}
$$

**3. Wavenumber and Wavelength**
$$
k = \frac{\omega}{v_p} = \frac{1.51 \times 10^{10}}{1.41 \times 10^8} \approx 107 \, \text{rad/m}
$$
Alternatively, the wavelength in the material is compressed relative to free space:
$$
\lambda = \frac{v_p}{f} \approx 0.059 \, \text{m} \, (5.9 \text{ cm})
$$
*(Note: In free space, $\lambda_0 \approx 12.5$ cm. The high $\epsilon_r$ shrinks the wavelength.)*

</details>

## 1.7 Special Choices of $f$ and $g$

The general solution $f(t - z/v_p)$ allows for *any* waveform shape. However, certain choices are physically and analytically privileged. Studying these canonical solutions is sufficient because, by linearity, any **more complicated waveform can be constructed as a superposition of simpler elementary waves**.

Because Maxwell’s equations in homogeneous, source-free media are linear, the set of solutions forms a linear vector space. In three dimensions, the scalar Helmholtz equation
$$
\nabla^2 \tilde{E} + k^2 \tilde{E} = 0
$$
admits sinusoidal plane waves as eigenmodes:
$$
\tilde{E}(\mathbf{r}) = E_0 e^{-j\mathbf{k}\cdot\mathbf{r}}
$$
By completeness of the Fourier basis, arbitrary fields may be represented as continuous superpositions (integrals) of these modes.

### 1.7.1 Sinusoidal Plane Waves
Choosing the function $f$ to be a cosine yields a monochromatic wave:
$$
f\!\left(t-\frac{z}{v_p}\right) = \cos(\omega t - \beta z), \qquad \beta=\frac{\omega}{v_p}
$$
Here, $\beta$ is often used interchangeably with $k$ to denote the propagation constant. Because the temporal and spatial dependencies are harmonic, these solutions are often called **time- and space-harmonic waves**. In homogeneous media, these are the **eigenfunctions of the wave operator**.

### 1.7.2  Spherical and Cylindrical Modes
While plane waves are the eigenmodes of Cartesian space, other geometries have their own natural basis functions:

* **Spherical Modes:** For a localized source radiating outward, the wave amplitude decays with distance to conserve energy.
    $$
    \tilde{E}(r) = \frac{A}{r}\,e^{-jkr}
    $$
* **Cylindrical Modes:** In waveguides or optical fibers, the Laplacian separates in cylindrical coordinates, leading to solutions involving Bessel functions:
    $$
    \tilde{E}(\rho,\phi,z) = J_m(k_\rho \rho)\,e^{jm\phi}\,e^{-j\beta z}
    $$

**Any coordinate system in which the Laplacian separates** yields canonical modal solutions. Solving an electromagnetic problem often implies expanding the fields in whichever modal basis matches the symmetry of the structure.

### 1.7.3  Non-monochromatic Fields (Wavepackets)
The choices above assume a single frequency $\omega$. General signals (pulses, data streams) are constructed via Fourier synthesis:
$$
E(z,t) = \int_{-\infty}^{\infty} \tilde{E}(\omega)\,e^{j(\omega t - \beta(\omega) z)}\,d\omega
$$
These **wavepackets** may distort as they travel if the medium is dispersive (i.e., if $v_p$ depends on $\omega$), causing different frequency components to travel at different speeds.

## 1.7.4  Phasor Representation

A sinusoidal plane wave may be written as:
$$
E(z,t) = A\cos(\omega t - \beta z + \phi) = \Re\!\left\{A e^{j(\omega t - \beta z + \phi)}\right\}
$$
Suppressing the explicit time factor $e^{j\omega t}$ yields the **phasor**:
$$
\tilde{E}(z) = A e^{-j\beta z} e^{j\phi}
$$
Phasors convert Maxwell’s equations from time-dependent differential equations into frequency-domain algebraic equations. In a homogeneous, source-free medium, this reduces to the **Vector Helmholtz Equation**:

$$
\nabla \times \nabla \times \tilde{\mathbf{E}} = k^2 \tilde{\mathbf{E}}, \qquad k=\omega\sqrt{\mu\epsilon}
$$

This is explicitly an **eigenvalue problem** of the form:
$$
\mathcal{L}[\tilde{\mathbf{E}}] = \lambda \tilde{\mathbf{E}}
$$
where $\mathcal{L} = \nabla \times \nabla \times$ is the linear operator and $\lambda = k^2$ is the eigenvalue. A field is called a **mode** if acting on it with the operator results only in a scalar multiplication—the field profile does not change shape, only its complex amplitude.
