---
title: "Electromagnetics: Sources"
date: 2026-01-27
permalink: /posts/optics/em_01/
tags:
  - electromagnetism
  - physics
  - academic
---

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

## 1.2 Duality Transformations

Maxwell’s equations in linear, isotropic media exhibit a striking symmetry. If we exchange electrical quantities with magnetic quantities (and vice versa), the form of the equations remains invariant. This allows us to solve a problem for an electric source ($\mathbf{J}$) and immediately know the solution for the corresponding magnetic source ($\mathbf{M}$) without resolving the differential equations.

The general duality transformation is a rotation in electromagnetic space. However, two specific variations are most common: **Mathematical Duality** (unit-agnostic) and **Scaled Duality** (unit-preserving).

**1. Mathematical Duality**
This simple substitution swaps vectors directly. It is useful for verifying symmetries but ignores units (e.g., swapping Volts/m for Amps/m).

$$
\mathbf{E} \to \mathbf{H}, \quad \mathbf{H} \to -\mathbf{E}, \quad \mathbf{J} \to \mathbf{M}, \quad \mathbf{M} \to -\mathbf{J}, \quad \epsilon \leftrightarrow \mu
$$

**2. Scaled Duality (Engineering Duality)**
To preserve physical units (so that Volts map to Volts) and maintain power relations, we introduce the intrinsic impedance of the medium, $\eta = \sqrt{\mu/\epsilon}$. This scaling is critical when converting known antenna solutions (e.g., electric dipoles) to their dual counterparts (e.g., magnetic loops).

The transformation from an Electric System ($e$) to a Magnetic System ($m$) is:

$$
\mathbf{E}_m = -\eta \mathbf{H}_e \qquad \mathbf{H}_m = \frac{1}{\eta} \mathbf{E}_e
$$

$$
\mathbf{M}_m = \eta \mathbf{J}_e \qquad \rho_{mm} = \eta \rho_{ee}
$$

<details>
<summary><b>Example: From Hertzian Dipole to Small Loop</b></summary>

A **Hertzian Dipole** is a short filament of electric current $I$ of length $l$ (moment $Il$) oriented along the $z$-axis. Its known far-field radiation is:

$$
\mathbf{E}_e = j\eta k I l \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}
$$
$$
\mathbf{H}_e = j k I l \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}}
$$

We wish to find the fields of a **Small Loop Antenna** (a magnetic dipole). A small loop of area $S$ carrying current $I_{loop}$ is equivalent to a magnetic current element $K l_{eq} = j\omega\mu I_{loop} S$.

Instead of solving Maxwell's equations from scratch, we use **Scaled Duality**.

**1. Identify the Source Transformation**
The electric source magnitude is $J_e \propto Il$. The dual magnetic source is $M_m$. According to scaled duality:
$$
M_m = \eta (Il)
$$

**2. Transform the Fields**
To find the electric field of the magnetic loop ($\mathbf{E}_{loop}$), we apply the scaled transformation to the dipole's magnetic field ($\mathbf{H}_e$):

$$
\mathbf{E}_{loop} = -\eta \mathbf{H}_e
$$

Substituting the known expression for $\mathbf{H}_e$:

$$
\mathbf{E}_{loop} = -\eta \left( j k (Il) \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}} \right)
$$

**3. Substitute the Dual Source**
We must replace the old source magnitude $(Il)$ with the new source magnitude using $Il = M_m / \eta$:

$$
\mathbf{E}_{loop} = -\eta \left( j k \frac{M_m}{\eta} \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}} \right)
$$

$$
\mathbf{E}_{loop} = -j k M_m \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}}
$$

This result perfectly matches the derivation for a magnetic dipole obtained via vector potentials, achieved purely through algebraic substitution.

</details>


## 1.3 Constitutive Relations

Maxwell’s equations couple to matter through material laws

$$
\mathbf{D} = \epsilon\,\mathbf{E}, \qquad \mathbf{B} = \mu\,\mathbf{H}, \qquad \mathbf{J} = \sigma\,\mathbf{E}.
$$

where $\epsilon$, $\mu$, and $\sigma$ are the permittivity, permeability, and conductivity of the material and define how a medium responds to electormagnetic fields. Media are categorized based on how these parameters behave relative to space, time, direction, and field strength. In the most general case, material parameters possess the following characteristics:

* **Complex-Valued:** To account for energy loss, we let $\epsilon = \epsilon' + i\epsilon''$. The imaginary part represents **loss** (ohmic or dipolar) within the system.
* **Inhomogeneous:** The properties are functions of position, $\epsilon(\mathbf{r})$, such as in a photonic crystal
* **Dispersive:** The properties depend on frequency, $\epsilon(\omega)$. This implies the material has "memory," and its response in the time domain is a convolution.

Furthermore, we can make these additional categorizations

| Category | Definition | Constitutive Relation |
| :--- | :--- | :--- |
| **Isotropic** | Response is independent of field orientation. | $\mathbf{D} = \epsilon \mathbf{E}$ (Scalar $\epsilon$) |
| **Anisotropic** | Response depends on direction (e.g., crystals). | $\mathbf{D} = \bar{\bar{\epsilon}} \cdot \mathbf{E}$ (Tensor $\bar{\bar{\epsilon}}$) |
| **Nonlinear** | Response depends on field magnitude. | $\mathbf{P} = \epsilon_0(\chi^{(1)}\mathbf{E} + \chi^{(2)}\mathbf{E}^2 + \dots)$ |
| **Bianisotropic** | Electric and magnetic fields are coupled. | $\mathbf{D} = \epsilon \mathbf{E} + \xi \mathbf{H}$ |


In optics and nanophotonics, it is often more convenient to describe a medium using the dimensionless **refractive index** $n$. For a linear, isotropic, and non-magnetic ($\mu = \mu_0$) medium, $n$ is defined as:

$$
n = \sqrt{\frac{\epsilon}{\epsilon_0}} = \sqrt{\epsilon_r}
$$

To account for both phase shift and attenuation (absorption), we use the **complex refractive index** $\tilde{n}$:

$$
\tilde{n} = n + i\kappa
$$

* **$n$ (Real part):** Related to the phase velocity, $v = c/n$.
* **$\kappa$ (Extinction coefficient):** Related to the absorption coefficient $\alpha$ by $\alpha = \frac{4\pi\kappa}{\lambda_0}$.


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


\
This simple example highlights two complementary routes for solving Maxwell's equations: using the integral form together with symmetry arguments, or using the differential
form and solving the resulting partial differential equations (here, Poisson's equation for $\phi$).


## 1.4 Continuity and Charge Conservation

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

Charge conservation is **not independent** of Maxwell’s equations. Taking $\nabla\cdot$ of Ampère–Maxwell and using $\nabla\cdot\nabla\times\!\bullet=0$ plus Gauss’s law recovers the continuity equation.

At a more abstract level, conservation laws arise from symmetries. In electromagnetism, global gauge invariance implies conservation of electric charge (Noether's theorem), whose local expression is precisely the continuity equation. The continuity equation in turn constrains the permissible electromagnetic fields and sources.

<details>
<summary><b>Example: Steady Current in a Wire</b></summary>

For a DC current \(I\):

$$
\partial_t \rho_e = 0 \quad \Rightarrow\quad \nabla\cdot\mathbf{J}=0.
$$

If \(I\) changes suddenly, transient charge buildup temporarily violates $\nabla\cdot\mathbf{J}=0$, restoring it once steady state resumes.

</details>

## 1.5 Boundary Conditions

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


The following example applies the boundary condition approach. It solves for the radiation from a magnetic current sheet, demonstrating how a **non-zero** source ($\mathbf{M}_s$) forces a discontinuity in the tangential electric field and the **absence** of a source ($\mathbf{J}_s = 0$) preserves continuity in the tangential magnetic field.

<details>
<summary><b>Example: Field of a Magnetic Current Sheet</b></summary>

Consider free space separated into two regions by the plane $z=0$. A **magnetic surface current** flows on this interface:
$$
\mathbf{M}_s = M_0 \hat{\mathbf{y}} \quad \text{at } z=0
$$
There is **no electric surface current** ($\mathbf{J}_s = 0$). We wish to find the electromagnetic waves radiating away from this sheet.

**1. Apply Conventions**
* Interface normal $\hat{\mathbf{n}} = \hat{\mathbf{z}}$.
* Region 1 is $z>0$; Region 2 is $z<0$.
* (note: one could easily have chosen $\hat{\mathbf{n}} = \hat{\mathbf{-z}}$ since it is also normal to the interface; however, subsequent signs would also have vto be revised to keep consistent with this normal vector choice.

**2. Formulate Field**
By symmetry, the sheet radiates plane waves traveling outward ($+z$ in Reg 1, $-z$ in Reg 2).
* **Region 1 ($z>0$):**
    $$\mathbf{E}_1 = E_0 \hat{\mathbf{x}} e^{-jkz} \quad \Rightarrow \quad \mathbf{H}_1 = \frac{E_0}{\eta_0} \hat{\mathbf{y}} e^{-jkz}$$
* **Region 2 ($z<0$):**
    $$\mathbf{E}_2 = -E_0 \hat{\mathbf{x}} e^{+jkz} \quad \Rightarrow \quad \mathbf{H}_2 = \frac{-E_0}{-\eta_0} \hat{\mathbf{y}} e^{+jkz} = \frac{E_0}{\eta_0} \hat{\mathbf{y}} e^{+jkz}$$
    *(Note: We guessed the sign of $E_2$ to be negative, but in case that is not true then discrepencies appear later on).*

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
</details>

## 1.6 Surface Equivalence Principle

Sources enter Maxwell's theory in two distinct ways: **explicitly** as volumetric densities ($\rho, \mathbf{J}$) driving the differential equations, or **implicitly** as surface singularities ($\rho_s, \mathbf{J}_s$) enforcing discontinuities at boundaries.

In many practical electromagnetic problems, explicit volumetric sources are absent from the region of interest. Instead, the physics is driven by equivalent surface charges or currents defined at interfaces. A key skill in modeling is recognizing that these descriptions are often physically equivalent, differing only in mathematical convenience.

Consider a bounded volume $V$ containing "electromagnetic junk" -- complex sources, nonlinear media, or intricate geometrie. Let us introduce a fictitious surface enclosing the "junk" called $S$. To examine the fields ($\mathbf{E}, \mathbf{H}$) outside the volume, we can use the Equivalence Principle.

According to the Uniqueness Theorem, the field solution in the outside region is uniquely determined if we know the tangential fields on the boundary $S$. Therefore, we can perform this:

1.  **Original Problem:** We have complex sources inside $V$ producing fields $\mathbf{E}, \mathbf{H}$ outside.
2.  **Equivalent Problem:** We conceptually remove the "junk" inside $V$ and replace it with a region of zero field ($\mathbf{E}=0, \mathbf{H}=0$).
3.  **The Fix:** To support the discontinuity between the zero field inside and the actual field outside, we must introduce **equivalent surface currents** on $S$.

Using the boundary conditions derived in Section 1.5 (where $\hat{\mathbf{n}}$ points outward from the zero-field region into the solution region), these currents are:

$$
\mathbf{J}_s = \hat{\mathbf{n}} \times (\mathbf{H} - 0) = \hat{\mathbf{n}} \times \mathbf{H}
$$

$$
\mathbf{M}_s = -\hat{\mathbf{n}} \times (\mathbf{E} - 0) = \mathbf{E} \times \hat{\mathbf{n}}
$$

These fictitious currents, radiating in free space, produce the exact same fields outside $V$ as the original complex sources.

## 1.7 Image Theory

The Equivalence Principle allows us to replace a volume with surface currents, but **Image Theory** allows us to replace a conductive boundary with virtual sources. This is particularly useful when solving for radiation near ground planes or simplifying the equivalent currents derived in the previous section.


To apply image theory, we idealize materials into two theoretical limits where fields cannot exist.

* **Perfect Electric Conductor (PEC):**
    A material with infinite conductivity ($\sigma \to \infty$).
    * Inside the PEC, charges redistribute instantly to cancel any applied electric field, so $\mathbf{E}_{int} = 0$ and $\mathbf{H}_{int} = 0$.
    * **Boundary Condition:** The tangential electric field must vanish at the surface to maintain continuity with the zero field inside.
        $$\hat{\mathbf{n}} \times \mathbf{E} = 0$$

* **Perfect Magnetic Conductor (PMC):**
    A theoretical "dual" to the PEC (does not exist in nature but is useful for symmetry and modeling high-impedance surfaces).
    * Inside the PMC, $\mathbf{E}_{int} = 0$ and $\mathbf{H}_{int} = 0$.
    * **Boundary Condition:** The tangential magnetic field must vanish at the surface.
        $$\hat{\mathbf{n}} \times \mathbf{H} = 0$$

When a source is placed near a PEC or PMC, the boundary conditions can be satisfied by removing the conductor and placing an "image source" in the region previously occupied by the conductor.

The orientation of the image source depends on whether the source vector is **parallel** (tangential) or **perpendicular** (normal) to the boundary.

**Case A: Electric Source ($\mathbf{J}$) over PEC**
* **Vertical Current ($\mathbf{J}_{\perp}$):** To support a non-zero normal field ($\mathbf{D}_n$) while keeping tangential fields zero, the image current must flow in the **same** direction. The fields add up.
* **Horizontal Current ($\mathbf{J}_{\parallel}$):** To force the tangential electric field to zero at the boundary, the image current must flow in the **opposite** direction. The fields cancel out.

**Case B: Magnetic Source ($\mathbf{M}$) over PEC**
Because magnetic currents are the mathematical dual of electric currents, the rules are reversed.
* **Vertical Magnetic Current ($\mathbf{M}_{\perp}$):** Image opposes source.
* **Horizontal Magnetic Current ($\mathbf{M}_{\parallel}$):** Image is in the **same** direction.



| Source Type | Orientation | PEC Image | PMC Image |
| :--- | :--- | :--- | :--- |
| **Electric ($\mathbf{J}$)** | Vertical ($\perp$) | Same Direction ($+$) | Opposite ($-$) |
| **Electric ($\mathbf{J}$)** | Horizontal ($\parallel$) | Opposite ($-$) | Same Direction ($+$) |
| **Magnetic ($\mathbf{M}$)** | Vertical ($\perp$) | Opposite ($-$) | Same Direction ($+$) |
| **Magnetic ($\mathbf{M}$)** | Horizontal ($\parallel$) | Same Direction ($+$) | Opposite ($-$) |

---

<details>
<summary><b>Example: Uniting Equivalence & Image Theory (Radiation from an Aperture)</b></summary>

**The Problem:**
We have an infinite PEC wall at $z=0$ (the $xy$-plane). There is a small rectangular slot (aperture) in the wall where the electric field is known to be $\mathbf{E}_{ap}$. We want to find the radiation into the half-space $z>0$. Such a setup is the standard analytical model for describing the aperture of a horn antenna.

**Step 1: Apply Surface Equivalence Principle**
We place a surface $S$ along the wall ($z=0$). We replace the region $z<0$ with zero field. To support the discontinuity, we introduce surface currents on $S$:
* **Electric Current:** $\mathbf{J}_s = \hat{\mathbf{n}} \times \mathbf{H}_{ap}$
* **Magnetic Current:** $\mathbf{M}_s = -\hat{\mathbf{n}} \times \mathbf{E}_{ap} = \mathbf{E}_{ap} \times \hat{\mathbf{z}}$

We now have these currents radiating in free space, but they are technically sitting on top of the original PEC plane geometry.

**Step 2: Apply Image Theory**
We can remove the PEC plane entirely if we replace it with the images of the currents sitting on it.
* **Consider $\mathbf{J}_s$:** This current lies *flat* on the PEC surface (tangential). According to image theory, a horizontal electric current creates a negative image that cancels it out exactly.
    $$\mathbf{J}_{total} = \mathbf{J}_s + \mathbf{J}_{image} = \mathbf{J}_s - \mathbf{J}_s = 0$$
    *Physical interpretation: The electric current is "shorted out" by the conductor.*

* **Consider $\mathbf{M}_s$:** This current also lies flat on the PEC surface. According to image theory, a horizontal magnetic current creates a positive image that reinforces it.
    $$\mathbf{M}_{total} = \mathbf{M}_s + \mathbf{M}_{image} = \mathbf{M}_s + \mathbf{M}_s = 2\mathbf{M}_s$$

**Step 3: Final Equivalent Model**
The complex problem of a slot in a conductive wall has been reduced to a single equivalent magnetic current radiating in free space:
$$
\mathbf{M}_{eq} = 2 (\mathbf{E}_{ap} \times \hat{\mathbf{z}})
$$
We can now calculate the far-field radiation simply by integrating this isolated source.
</details>
