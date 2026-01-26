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

Maxwell’s equations in differential form assume the field vectors are differentiable. However, at the interface between two different media, the material parameters ($\epsilon, \mu, \sigma$) often change abruptly. To handle this, we derive boundary conditions by applying the integral forms of Maxwell's equations to infinitesimal regions straddling the interface.

Let an interface separate **Medium 1** from **Medium 2**. We define the unit normal vector $\hat{\mathbf{n}}$ to point **from Medium 2 into Medium 1** $\hat{\mathbf{n}} = \hat{\mathbf{n}}_{2 \to 1}$


By applying Gauss's Law over a a small cylin ($\oint \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$) to a small "pillbox" cylinder of height $\Delta h$ and cap area $\Delta A$ that cuts across the interface. As the height $\Delta h \to 0$, the flux through the side walls vanishes. The remaining flux comes from the top (Medium 1) and bottom (Medium 2) caps:

$$
(\mathbf{D}_1 \cdot \hat{\mathbf{n}}) \Delta A - (\mathbf{D}_2 \cdot \hat{\mathbf{n}}) \Delta A = \rho_{es} \Delta A
$$

where $\rho_{es}$ is the surface charge density. This yields the jump condition for normal components.

**2. Tangential Components (Curl Equations)**
Apply Faraday's law ($\oint \mathbf{E} \cdot d\boldsymbol{\ell} = -\frac{d}{dt}\int \mathbf{B}\cdot d\mathbf{S} - \int \mathbf{M}\cdot d\mathbf{S}$) to a rectangular loop of length $\Delta \ell$ and vanishing width straddling the boundary. As the area of the loop goes to zero, the magnetic flux term ($\mathbf{B}$) vanishes (assuming $\mathbf{B}$ is finite). The circulation of $\mathbf{E}$ and the magnetic current source $\mathbf{M}$ remain:

$$
(\mathbf{E}_1 \cdot \mathbf{t}) \Delta \ell - (\mathbf{E}_2 \cdot \mathbf{t}) \Delta \ell = -(\mathbf{M}_s \cdot \mathbf{b}) \Delta \ell
$$

where $\mathbf{t}$ is the tangent vector along the loop and $\mathbf{b}$ is the binormal. In vector notation, this generalizes to the cross product with the normal vector.

### Summary of Boundary Conditions

For an interface with surface electric charge $\rho_{es}$, electric current $\mathbf{J}_s$, magnetic charge $\rho_{ms}$, and magnetic current $\mathbf{M}_s$:

| Component | Boundary Condition | Physical Implication |
| :--- | :--- | :--- |
| **Tangential E** | $\hat{\mathbf{n}} \times (\mathbf{E}_1 - \mathbf{E}_2) = -\mathbf{M}_s$ | $\mathbf{E}_{tan}$ is continuous unless magnetic current exists. |
| **Tangential H** | $\hat{\mathbf{n}} \times (\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$ | $\mathbf{H}_{tan}$ is continuous unless electric current exists. |
| **Normal D** | $\hat{\mathbf{n}} \cdot (\mathbf{D}_1 - \mathbf{D}_2) = \rho_{es}$ | $\mathbf{D}_{norm}$ jumps by the surface charge density. |
| **Normal B** | $\hat{\mathbf{n}} \cdot (\mathbf{B}_1 - \mathbf{B}_2) = \rho_{ms}$ | $\mathbf{B}_{norm}$ is continuous (unless magnetic monopoles exist). |

*Note: In most physical scenarios, magnetic sources $\mathbf{M}_s$ and $\rho_{ms}$ are zero. However, they are retained here for use in equivalence principles (e.g., aperture problems).*

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

$$
\rho_e = \rho_m = 0,\quad \mathbf{J}=\mathbf{M}=0,\quad \sigma=0.
$$

Using \(\mathbf{D}=\epsilon\mathbf{E}\), \(\mathbf{B}=\mu\mathbf{H}\):

$$
\nabla \times \mathbf{E} = -\mu\,\partial_t \mathbf{H},\qquad
\nabla \times \mathbf{H} = \epsilon\,\partial_t \mathbf{E}.
$$

Taking curl of Faraday:

$$
\nabla \times (\nabla \times \mathbf{E}) = -\mu\epsilon \frac{\partial^2\mathbf{E}}{\partial t^2}.
$$

Using the identity:

$$
\nabla\times\nabla\times\mathbf{E} = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E},
$$

and noting \(\nabla\cdot\mathbf{E}=0\),

$$
\nabla^2 \mathbf{E} = \mu\epsilon\,\partial_t^2 \mathbf{E}.
$$

A similar expression holds for \(\mathbf{H}\).

---

## 1.7 General Solution of the Wave Equation

In 1D for fields depending on \(z,t\),

$$
\mathbf{E}(z,t)=\hat{\mathbf{x}}E_x(z,t),\quad
\mathbf{H}(z,t)=\hat{\mathbf{y}}H_y(z,t),
$$

yielding the scalar PDE

$$
\partial_z^2 E_x = \frac{1}{v_p^2}\partial_t^2 E_x,\qquad v_p = \frac{1}{\sqrt{\mu\epsilon}}.
$$

The general solution is

$$
E_x(z,t) = K_1 f\!\left(t - \frac{z}{v_p}\right) + K_2 g\!\left(t + \frac{z}{v_p}\right),
$$

representing waves traveling in \(\pm z\).

---

## 1.8 Special Choices of \(f\) and \(g\)

Maxwell’s solutions form a linear vector space. In 1D, right/left traveling waves form a useful basis. In 3D, the Helmholtz eigenbasis arises:

$$
\nabla^2 \tilde{E} + k^2 \tilde{E} = 0 \quad\Rightarrow\quad
\tilde{E}(\mathbf{r}) = E_0 e^{-j\mathbf{k}\cdot\mathbf{r}},
$$

and arbitrary fields can be expressed as

$$
\tilde{E}(\mathbf{r}) = \int \tilde{E}(\mathbf{k})\,e^{-j\mathbf{k}\cdot\mathbf{r}}\,d^3\mathbf{k}.
$$

---

###  Example: Canonical Mode Families (Interactive)

<details>
<summary><b>Click to reveal modes</b></summary>

#### Sinusoidal Plane Waves

Choosing
$$
f(t-z/v_p)=\cos(\omega t - \beta z),\quad \beta=\omega/v_p
$$

yields a monochromatic plane wave.

#### Spherical Modes

$$
\tilde{E}(r)=\frac{A}{r}e^{-jkr}
$$

#### Cylindrical Modes

$$
\tilde{E}(\rho,\phi,z)=J_m(k_\rho\rho)e^{jm\phi}e^{-j\beta z}.
$$

</details>

---

## 1.9 Non-Monochromatic Fields

Through Fourier synthesis:

$$
E(z,t)=\int \tilde{E}(\omega)e^{j(\omega t - \beta(\omega)z)}\,d\omega.
$$

Dispersion induces waveform distortion.

---

## 1.10 Phasor Representation

A real sinusoidal field:

$$
E(z,t)=A\cos(\omega t - \beta z + \phi)
= \Re\!\{ A e^{j(\omega t - \beta z + \phi)}\}.
$$

Suppressing \(e^{j\omega t}\) yields the **phasor**

$$
\tilde{E}(z)=A e^{-j\beta z}e^{j\phi}.
$$

In a homogeneous medium, frequency-domain Maxwell reduces to an eigenproblem:

$$
\nabla\times\nabla\times\tilde{\mathbf{E}} = k^2 \tilde{\mathbf{E}},\qquad k=\omega\sqrt{\mu\epsilon}.
$$

Because free space is translationally invariant, plane waves

$$
\tilde{\mathbf{E}}(\mathbf{r}) = \mathbf{E}_0 e^{-j\mathbf{k}\cdot\mathbf{r}}
$$

form a complete basis.
