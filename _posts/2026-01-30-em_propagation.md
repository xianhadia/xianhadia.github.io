---
title: "Electromagnetics: Propagation"
date: 2026-01-30
permalink: /posts/optics/em_02/
tags:
  - electromagnetism
  - physics
  - optics
  - waves
---

Having established in Chapter 1 that sources ($\rho, \mathbf{J}$) give rise to electromagnetic fields, we now turn to the second link in the causal chain: **Propagation**. Once a field is generated, it takes on a life of its own, traveling through space governed by the properties of the medium rather than the source that created it.

This chapter explores how electromagnetic fields behave in source-free regions, moving from the general wave equation to specific solutions like plane waves, and finally to the behavior of waves at interfaces.

## 2.1 The Wave Equation

Consider a source-free, homogeneous, linear, isotropic region. The source terms vanish:
$$
\rho_e = \rho_m = 0, \qquad \mathbf{J}=\mathbf{M}=0
$$
Maxwell’s curl equations in this region are coupled first-order differential equations:
$$
\nabla \times \mathbf{E} = -\mu\frac{\partial \mathbf{H}}{\partial t} \quad (1)
$$
$$
\nabla \times \mathbf{H} = \epsilon\frac{\partial \mathbf{E}}{\partial t} \quad (2)
$$
To decouple them, we take the curl of Faraday's law (1):
$$
\nabla \times (\nabla \times \mathbf{E}) = -\mu\frac{\partial}{\partial t}(\nabla \times \mathbf{H})
$$
Substituting Ampère’s law (2) into the right-hand side:
$$
\nabla \times (\nabla \times \mathbf{E}) = -\mu\epsilon \frac{\partial^2\mathbf{E}}{\partial t^2}
$$
Using the vector identity $\nabla \times(\nabla\times \mathbf{E})=\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E}$, and noting that $\nabla \cdot \mathbf{E} = 0$ in a source-free charge-free region, we arrive at the **Vector Wave Equation**:

$$
\nabla^2 \mathbf{E} - \mu\epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0
$$

A strictly analogous equation holds for the magnetic field $\mathbf{H}$.

### 2.1.1 The Scalar Approximation
The vector wave equation represents three coupled scalar PDEs (one for each Cartesian component). In many cases, we can simplify the problem by assuming the field is linearly polarized (e.g., $\mathbf{E}$ points only in the $x$-direction) and depends only on the longitudinal coordinate $z$ and time $t$. This reduces the vector equation to the scalar form:

$$
\frac{\partial^2 E_x}{\partial z^2} - \frac{1}{v^2}\frac{\partial^2 E_x}{\partial t^2} = 0
$$

where the phase velocity is defined by the medium:
$$
v = \frac{1}{\sqrt{\mu\epsilon}} = \frac{c}{n}
$$

## 2.2 General Solutions (d'Alembert)
The general solution to the 1D scalar wave equation, known as **d'Alembert’s solution**, is a superposition of two traveling waves:

$$
E_x(z,t) = f\left(t - \frac{z}{v}\right) + g\left(t + \frac{z}{v}\right)
$$

* **$f(t - z/v)$**: Represents a wave of *arbitrary shape* traveling in the **$+z$ direction**.
* **$g(t + z/v)$**: Represents a wave of *arbitrary shape* traveling in the **$-z$ direction**.

This result is profound: in a lossless, nondispersive medium, information (the shape of the function) is translated through space without distortion.

### Special Choices of $f$ and $g$
While $f$ and $g$ can be any differentiable function, two choices are fundamental to the study of optics and electromagnetics.

**1. The Sinusoidal Wave (Time-Harmonic)**


[Image of electromagnetic wave propagation]

If we choose $f$ to be a cosine function, we get a monochromatic wave:
$$
E(z,t) = E_0 \cos(\omega(t - z/v)) = E_0 \cos(\omega t - kz)
$$
where $k = \omega/v = \omega\sqrt{\mu\epsilon}$ is the **wavenumber**. These are the eigenfunctions of the wave operator and form the basis of Frequency Domain analysis.

**2. The Gaussian Pulse (Wavepacket)**
To represent a localized burst of energy (like a laser pulse or a radar ping), we choose $f$ to be a Gaussian envelope modulating a carrier:
$$
E(z,t) = E_0 e^{-(t - z/v)^2 / \tau^2} \cos(\omega_0 t - k_0 z)
$$
Unlike infinite sinusoids, these "wavepackets" are physically realizable. In dispersive media (where $v$ depends on $\omega$), these pulses will spread out over time, a phenomenon known as Group Velocity Dispersion (GVD).

## 2.3 Phasors and the Helmholtz Equation
Handling cosine and sine terms in differential equations is algebraically tedious. We simplify the math using the **Phasor Transform**. For a time-harmonic field oscillating at angular frequency $\omega$, we write the instantaneous field as the real part of a complex vector:

$$
\mathbf{E}(\mathbf{r}, t) = \Re \{ \tilde{\mathbf{E}}(\mathbf{r}) e^{j\omega t} \}
$$

*(Note: We use the engineering convention $+j\omega t$. The physics convention often uses $-i\omega t$. The choice dictates the sign of the imaginary part of the refractive index/permittivity.)*

Substituting this into the wave equation converts time derivatives into algebraic multiplication ($\partial/\partial t \to j\omega$). The wave equation becomes the **Vector Helmholtz Equation**:

$$
\nabla^2 \tilde{\mathbf{E}} + k^2 \tilde{\mathbf{E}} = 0
$$

where $k = \omega\sqrt{\mu\epsilon}$ is the wavenumber. This is an **eigenvalue problem**:
$$
\hat{L} \tilde{\mathbf{E}} = \lambda \tilde{\mathbf{E}}
$$
where the operator $\hat{L} = -\nabla^2$ and the eigenvalue is $\lambda = k^2$. This perspective is crucial in computational electromagnetics, where we often solve for the "modes" (eigenvectors) of a structure.

## 2.4 Uniform Plane Waves (UPW)
The simplest solution to the Helmholtz equation in Cartesian coordinates is the Uniform Plane Wave.
$$
\tilde{\mathbf{E}}(z) = \mathbf{E}_0 e^{-jkz}
$$
"Uniform" means the field magnitude and phase are constant across the transverse planes ($x,y$ planes).

### 2.4.1 Orthogonality (TEM Waves)
If we assume $\mathbf{E} = E_0 \hat{\mathbf{x}}$, we can find the associated magnetic field using Faraday's Law ($\nabla \times \tilde{\mathbf{E}} = -j\omega\mu \tilde{\mathbf{H}}$):
$$
\tilde{\mathbf{H}} = -\frac{1}{j\omega\mu} \nabla \times (E_0 e^{-jkz} \hat{\mathbf{x}})
$$
$$
\tilde{\mathbf{H}} = -\frac{1}{j\omega\mu} \left( \frac{\partial E_x}{\partial z} \hat{\mathbf{y}} \right) = \frac{jk E_0}{j\omega\mu} e^{-jkz} \hat{\mathbf{y}}
$$
$$
\tilde{\mathbf{H}} = \frac{E_0}{\eta} e^{-jkz} \hat{\mathbf{y}}
$$

This reveals the **Transverse Electromagnetic (TEM)** structure of plane waves: $\mathbf{E}$, $\mathbf{H}$, and the direction of propagation $\mathbf{k}$ are mutually orthogonal.

### 2.4.2 Intrinsic Impedance
The ratio of the electric to magnetic field amplitudes is a characteristic of the medium, called the **Intrinsic Impedance** ($\eta$):
$$
\eta = \frac{|\mathbf{E}|}{|\mathbf{H}|} = \frac{\omega\mu}{k} = \sqrt{\frac{\mu}{\epsilon}}
$$
* **Vacuum:** $\eta_0 \approx 377 \, \Omega$ (or $120\pi \, \Omega$)
* **Dielectrics:** $\eta = \eta_0 / \sqrt{\epsilon_r}$ (Impedance is lower in dense media)

### 2.4.3 Power Flow (Poynting Vector)
Electromagnetic waves transport energy. The instantaneous power density flux is given by the Poynting vector $\mathbf{S} = \mathbf{E} \times \mathbf{H}$. In time-harmonic form, we care about the **Time-Average Poynting Vector**:

$$
\mathbf{S}_{avg} = \frac{1}{2} \Re \{ \tilde{\mathbf{E}} \times \tilde{\mathbf{H}}^* \}
$$

For a plane wave:
$$
\mathbf{S}_{avg} = \frac{|E_0|^2}{2\eta} \hat{\mathbf{z}} \quad (\text{W/m}^2)
$$

## 2.5 Polarization

The "scalar approximation" in Section 2.1 assumed the field pointed in a fixed direction (e.g., $\hat{\mathbf{x}}$). In general, the electric field vector traces out a shape in the transverse plane as it propagates. This is **polarization**.

Consider a wave traveling in $+z$ with both $x$ and $y$ components:
$$
\tilde{\mathbf{E}} = (E_{0x} \hat{\mathbf{x}} + E_{0y} e^{j\delta} \hat{\mathbf{y}}) e^{-jkz}
$$
The phase difference $\delta$ determines the polarization state:

| Polarization | Condition | Description |
| :--- | :--- | :--- |
| **Linear** | $\delta = 0$ or $\pi$ | The tip of the vector traces a line. |
| **Circular** | $|E_{0x}| = |E_{0y}|$ and $\delta = \pm \pi/2$ | The tip traces a circle. (Right or Left Handed). |
| **Elliptical** | General Case | The tip traces an ellipse. |

## 2.6 Reflection and Refraction
When a wave encounters an interface between two different media ($\eta_1$ vs $\eta_2$), the causal chain is interrupted. To satisfy the boundary conditions (Section 1.5), the incident wave must split into a **reflected** wave and a **transmitted** (refracted) wave.

### 2.6.1 Normal Incidence
For a wave striking an interface head-on, the reflection ($\Gamma$) and transmission ($\tau$) coefficients are derived strictly from impedance mismatch:

$$
\Gamma = \frac{E_r}{E_i} = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}
$$
$$
\tau = \frac{E_t}{E_i} = \frac{2\eta_2}{\eta_2 + \eta_1}
$$

* **Matched Load ($\eta_1 = \eta_2$):** $\Gamma = 0$. No reflection (stealth technology principle).
* **Short Circuit ($\eta_2 = 0$, e.g., PEC):** $\Gamma = -1$. Total reflection with $180^\circ$ phase shift.
* **Open Circuit ($\eta_2 \to \infty$):** $\Gamma = +1$. Total reflection with $0^\circ$ phase shift.

### 2.6.2 Oblique Incidence and Snell's Law

When a wave hits at an angle $\theta_i$, we must match the **phase velocities** along the interface boundary. This phase matching condition leads to **Snell's Law**:

$$
n_1 \sin \theta_i = n_2 \sin \theta_t
$$

or equivalently, the preservation of the transverse wavenumber: $k_{1x} = k_{2x}$.

### 2.6.3 Total Internal Reflection (TIR) & Evanescent Waves
If a wave travels from a dense medium to a rare medium ($n_1 > n_2$) at a steep angle, Snell's law requires $\sin \theta_t > 1$, which is impossible for a real angle.
Mathematically, the transmitted angle becomes complex. The transmitted wavenumber $k_{zt}$ becomes purely imaginary:
$$
k_{zt} = -j\alpha
$$
The transmitted field becomes:
$$
\mathbf{E}_t \propto e^{-j k_{xt} x} e^{-\alpha z}
$$
This is an **Evanescent Wave**. It does not propagate power away from the interface; instead, it decays exponentially into the second medium. This phenomenon is the foundation of:
* **Fiber Optics:** Confining light inside the core via TIR.
* **TIR Microscopy:** Illuminating only surface details.
* **Tunneling:** If a third medium is placed within the decay length $1/\alpha$, energy can "tunnel" across the gap (frustrated TIR).

<details>
<summary><b>Example: The Critical Angle</b></summary>

Light travels from Glass ($n_1 = 1.5$) to Air ($n_2 = 1.0$).
The critical angle $\theta_c$ occurs when the transmitted angle is $90^\circ$:

$$
\sin \theta_c = \frac{n_2}{n_1} \sin(90^\circ) = \frac{1.0}{1.5}
$$
$$
\theta_c = \arcsin(0.666) \approx 41.8^\circ
$$

Any incident angle $\theta_i > 41.8^\circ$ will result in 100% reflection. The glass acts as a perfect mirror.
</details>
