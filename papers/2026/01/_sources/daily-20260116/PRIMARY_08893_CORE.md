# 2601.08893v1 necessary primary core

ExactHTML https://arxiv.org/html/2601.08893v1. Necessary selected methods/evaluation/limits; not all appendices, not later revisions. TOC-mislocation discarded before source caching.

4 
Field-Theoretic View of Generation
4.1 
From Sequences to Fields
We replace discrete token sequences with a continuous, time-evolving field
u
⁡
(
x
,
t
)
∈
ℝ
C
,
u(x,t)\in\mathbb{R}^{C},
(6)
where 
x
x
 indexes position in an abstract semantic or spatial domain and 
t
t
denotes generation time.
The channel dimension 
C
C
 represents latent semantic, syntactic, or visual
degrees of freedom.
This formulation embeds generative modeling into a function space, allowing
tools from continuum mechanics, stochastic analysis, and field theory to be
applied directly.
Under this view, text generation corresponds to a two-dimensional domain
(
x
,
t
)
(x,t)
, where 
x
x
 indexes semantic position (e.g., token order or latent
semantic coordinates) and 
t
t
 parametrizes the generative process.
Video and movie generation correspond naturally to three-dimensional domains
(
x
,
y
,
t
)
(x,y,t)
, where 
(
x
,
y
)
(x,y)
 denote spatial coordinates and 
t
t
 denotes time.
Crucially, no architectural modification is required to move between modalities;
only the dimensionality of the domain changes.
This dimensional universality mirrors physical field theories, where the same
governing equations apply across spatial dimensions.
4.2 
Generation as Dynamical Evolution
In this framework, generation is not formulated as autoregressive prediction,
x
t
+
1
∼
p
θ
​
(
x
∣
x
≤
t
)
,
x_{t+1}\sim p_{\theta}(x\mid x_{\leq t}),
(7)
but as the evolution of a field governed by a stochastic partial differential
equation (SPDE).
We posit that the generative process obeys dynamics of the form
∂
t
u
+
(
u
⋅
∇
)
u
=
−
∇
p
+
ν
Δ
u
+
f
θ
(
u
,
ξ
)
,
\partial_{t}u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f_{\theta}(u,\xi),
(8)
subject to the incompressibility constraint
∇
⋅
u
=
0
.
\nabla\cdot u=0.
(9)
Interpretation.
The Navier–Stokes structure is used here as a 
template
 for nonlinear transport,
coherence, and multiscale interaction, not as a claim that linguistic or visual processes
obey physical fluid laws. The SPDE serves as a flexible generative prior whose structure
encodes locality, conservation, and smoothness.
Here, 
(
u
⋅
∇
)
u
(u\cdot\nabla)u
 represents nonlinear self-interaction and information
transport, 
ν
​
Δ
​
u
\nu\Delta u
 is a dissipative term controlling smoothness and
stability, and 
f
θ
f_{\theta}
 is a learned forcing functional parameterized by a
neural network.
The pressure field 
p
p
 acts as a Lagrange multiplier enforcing the constraint
(
9
), analogous to incompressible fluid flow.
This formulation is inspired by the Navier–Stokes equations, which are known to
generate long-range correlations, multiscale structure, and coherent patterns
from purely local interactions.
Importantly, the role of Navier–Stokes here is not literal physical simulation,
but as a canonical example of a minimal nonlinear dynamical system capable of
rich generative behavior.
4.3 
Stochasticity and Uncertainty in Function Space
The term 
ξ
\xi
 in (
8
) denotes stochastic forcing, which we model as
noise injected into the system to represent uncertainty, variability, and
creative diversity.
Formally, this corresponds to an SPDE of the form
d
​
u
=
[
−
𝒫
⁡
(
u
⋅
∇
u
)
+
ν
​
Δ
​
u
+
f
θ
​
(
u
)
]
​
d
​
t
+
σ
​
d
​
W
t
,
\mathrm{d}u=\left[-\mathcal{P}(u\cdot\nabla u)+\nu\Delta u+f_{\theta}(u)\right]\mathrm{d}t+\sigma\,\mathrm{d}W_{t},
(10)
where 
𝒫
\mathcal{P}
 denotes the Helmholtz–Hodge projection onto the
divergence-free subspace and 
W
t
W_{t}
 is a cylindrical Wiener process on an
appropriate Hilbert space.
This construction places generation within the well-established theory of
stochastic evolution equations, allowing uncertainty to propagate continuously
through time rather than being collapsed at each decoding step.
In contrast to autoregressive sampling, which repeatedly conditions on its own
outputs, the present framework maintains a coherent probabilistic trajectory in
function space.
4.4 
Constraint Enforcement and Projection Operators
The incompressibility constraint (
9
) plays a central
structural role.
In physical fluid dynamics, incompressibility enforces volume preservation and
prevents unphysical accumulation or depletion of mass.
In the generative setting, it enforces global consistency by preventing the
collapse or explosion of semantic mass within the field.
Mathematically, the constraint is enforced by projecting the dynamics onto the
constraint manifold:
∂
t
u
=
𝒫
[
−
(
u
⋅
∇
)
u
+
ν
Δ
u
+
f
θ
(
u
)
]
,
\partial_{t}u=\mathcal{P}\left[-(u\cdot\nabla)u+\nu\Delta u+f_{\theta}(u)\right],
(11)
where 
𝒫
\mathcal{P}
 removes gradient components corresponding to the pressure
field.
This replaces the need for explicit global coordination mechanisms, such as
attention, with a principled geometric constraint.
4.5 
Interpretation for Text and Video
In the two-dimensional text setting, the nonlinear advection term models the
transport of semantic context across positions, while dissipation suppresses
spurious oscillations corresponding to hallucinations or incoherence.
Coherent narrative structure emerges as large-scale flow patterns, while local
syntactic variations correspond to fine-scale fluctuations.
In the three-dimensional video setting, the same equations govern motion,
appearance evolution, and temporal consistency.
Temporal coherence arises naturally from the continuity of the flow, rather than
from explicit conditioning on previous frames.
This stands in contrast to transformer-based video models, which must learn
temporal consistency implicitly through massive datasets.
4.6 
Relation to Existing Generative Models
The proposed field-theoretic formulation subsumes and generalizes several
existing approaches.
Diffusion models can be recovered as linear SPDEs without advection terms,
while neural operators correspond to deterministic approximations of
∂
t
u
=
f
θ
​
(
u
)
\partial_{t}u=f_{\theta}(u)
.
However, unlike these models, the present framework integrates nonlinear
transport, stochasticity, and hard constraints into a single coherent dynamical
system.
To our knowledge, no existing language or video model formulates generation as a
constrained stochastic flow in function space inspired by Navier–Stokes
dynamics.
This shift from discrete symbolic prediction to continuous field evolution
constitutes a foundational change in how generative modeling is conceptualized.
5 
Wavelet Spectral Representation
5.1 
Motivation: Multiscale Structure and Data Efficiency
A central challenge in generative modeling is the extreme data inefficiency of
learning high-dimensional structure directly in pixel, token, or embedding
space.
Empirically, natural language, images, video, and physical fields exhibit strong
multiscale organization: global structure evolves slowly and coherently, while
fine-scale detail is localized, intermittent, and often stochastic.
Ignoring this scale separation forces models to relearn the same structure at
every resolution, dramatically increasing sample complexity.
In contrast, 

6.2 
Relation to Diffusion Models and SPDEs
The diffusion process in (
17
) is the finite-dimensional
projection of a stochastic partial differential equation defined on the
underlying function space.
In the limit of infinitesimal wavelet scales, the coefficient diffusion
corresponds to an SPDE of the form
d
​
u
=
ν
τ
​
Δ
​
u
​
d
​
τ
+
2
​
d
​
W
τ
,
\mathrm{d}u=\nu_{\tau}\Delta u\,\mathrm{d}\tau+\sqrt{2}\,\mathrm{d}W_{\tau},
(19)
where 
ν
τ
\nu_{\tau}
 is a scale-dependent diffusion coefficient.
Thus, diffusion in coefficient space can be interpreted as stochastic smoothing
of the field across scales, with fine-scale modes being progressively randomized
as 
τ
\tau
 increases.
This perspective clarifies the conceptual role of diffusion models: they define
a reversible stochastic flow on function space that connects a structured data
distribution to a tractable reference measure, typically a Gaussian.
Unlike autoregressive models, which collapse uncertainty at each step, diffusion
models maintain a coherent probabilistic trajectory throughout the generative
process.
Training and sampling pipeline.
In practice, training proceeds by estimating the score function in wavelet space,
followed by optional physics-guided correction in the reconstructed field domain.
Sampling integrates the reverse-time SDE or ODE while enforcing constraints via
projection operators. This hybrid spectral-physical pipeline distinguishes SGFMs
from both transformer and diffusion architectures.
6.3 
Conditional and Scale-Structured Score Functions
The score network 
s
θ
​
(
c
,
τ
)
s_{\theta}(c,\tau)
 is not modeled as an unconditional function
of all coefficients.
Instead, we exploit the multiscale structure of the wavelet representation by
conditioning the score on coarse-scale coefficients and physical parameters.
Formally, we write
s
θ
​
(
c
,
τ
)
=
s
θ
​
(
c
(
fine
)
,
c
(
coarse
)
,
λ
,
τ
)
,
s_{\theta}(c,\tau)=s_{\theta}\!\big(c^{(\mathrm{fine})},\,c^{(\mathrm{coarse})},\,\lambda,\,\tau\big),
(20)
where 
λ
\lambda
 denotes physical parameters such as viscosity, forcing strength,
or boundary-condition embeddings.
Coarse-scale coefficients 
c
(
coarse
)
c^{(\mathrm{coarse})}
 may be teacher-forced during
training or predicted by a separate deterministic module.
This induces a conditional diffusion process in which global structure is fixed
or weakly stochastic, while fine-scale detail is generated probabilistically.
Such conditional score modeling reflects the physical intuition that uncertainty
predominantly resides at small scales, while large-scale structure is stable and
slowly varying.
6.4 
Reverse-Time Dynamics and Sampling
Sampling from the generative model proceeds by integrating the reverse-time SDE
associated with (
17
).
Under mild regularity assumptions, the reverse process is given by
d
c
=
[
−
s
θ
(
c
,
τ
)
+
∇
c
log
p
τ
(
c
)
]
d
τ
+
2
d
W
¯
τ
,
\mathrm{d}c=\left[-\,s_{\theta}(c,\tau)+\nabla_{c}\log p_{\tau}(c)\right]\mathrm{d}\tau+\sqrt{2}\,\mathrm{d}\bar{W}_{\tau},
(21)
which in practice is approximated by
d
​
c
=
−
s
θ
​
(
c
,
τ
)
​
d
​
τ
+
2
​
d
​
W
¯
τ
,
\mathrm{d}c=-\,s_{\theta}(c,\tau)\,\mathrm{d}\tau+\sqrt{2}\,\mathrm{d}\bar{W}_{\tau},
(22)
with 
W
¯
τ
\bar{W}_{\tau}
 a reverse-time Wiener process.
Numerical integration is performed using standard discretization schemes such as
Euler–Maruyama or higher-order predictor–corrector methods.
Because the dynamics are defined in spectral space, each step has linear or
near-linear complexity in the number of active coefficients.
6.5 
Physics-Guided Score Correction
A key departure from standard diffusion models is the incorporation of
physics-guided corrections during sampling.
Let 
u
=
W
−
1
​
[
c
]
u=W^{-1}[c]
 denote the reconstructed field.
We define a physics residual functional
ℰ
(
u
)
=
∥
𝒫
(
∂
t
u
+
(
u
⋅
∇
)
u
−
ν
Δ
u
−
f
)
∥
2
,
\mathcal{E}(u)=\big\|\mathcal{P}\big(\partial_{t}u+(u\cdot\nabla)u-\nu\Delta u-f\big)\big\|^{2},
(23)
where 
𝒫
\mathcal{P}
 denotes projection onto the

9.1 
Overview of the Composite Objective
Training the proposed Spectral Generative Flow Model requires balancing three
distinct but complementary objectives: (i) accurate learning of the generative
distribution, (ii) enforcement of physical and structural constraints, and
(iii) satisfaction of conditioning and boundary information.
We therefore define a composite loss of the form
ℒ
=
ℒ
diff
+
λ
R
​
‖
𝒫
⁡
(
R
⁡
(
u
)
)
‖
2
+
λ
B
​
ℒ
BC
,
\mathcal{L}=\mathcal{L}_{\mathrm{diff}}+\lambda_{R}\,\big\|\mathcal{P}\big(R(u)\big)\big\|^{2}+\lambda_{B}\,\mathcal{L}_{\mathrm{BC}},
(38)
where each term corresponds to a principled component of the underlying
stochastic field model.
The weighting coefficients 
λ
R
\lambda_{R}
 and 
λ
B
\lambda_{B}
 control the relative
strength of physical regularization and boundary enforcement.
This structure mirrors classical variational formulations in physics and
inverse problems, where data fidelity, constraint satisfaction, and regularity
are combined into a single objective functional.
9.2 
Diffusion Loss: Learning the Generative Distribution
The diffusion loss 
ℒ
diff
\mathcal{L}_{\mathrm{diff}}
 arises from score-based
generative modeling.
Given wavelet coefficients 
c
c
 and diffusion time 
τ
\tau
, the model is trained
to approximate the score
s
θ
(
c
,
τ
)
≈
∇
c
log
p
τ
(
c
)
,
s_{\theta}(c,\tau)\approx\nabla_{c}\log p_{\tau}(c),
(39)
where 
p
τ
p_{\tau}
 denotes the marginal distribution of the forward diffusion
process.
Using denoising score matching, the diffusion loss takes the form
ℒ
diff
=
𝔼
c
0
,
τ
,
ϵ
​
[
‖
ϵ
−
ϵ
θ
​
(
α
τ
​
c
0
+
1
−
α
τ
​
ϵ
,
τ
)
‖
2
]
,
\mathcal{L}_{\mathrm{diff}}=\mathbb{E}_{c_{0},\tau,\epsilon}\Big[\big\|\epsilon-\epsilon_{\theta}\big(\sqrt{\alpha_{\tau}}c_{0}+\sqrt{1-\alpha_{\tau}}\,\epsilon,\,\tau\big)\big\|^{2}\Big],
(40)
where 
c
0
c_{0}
 are clean coefficients, 
ϵ
∼
𝒩
⁡
(
0
,
I
)
\epsilon\sim\mathcal{N}(0,I)
, and
α
τ
\alpha_{\tau}
 is a noise schedule.
This term alone would suffice to learn an unconditional diffusion model.
However, in the absence of additional structure, such models may generate
samples that are statistically plausible yet physically inconsistent or
unstable.
The remaining terms in (
38
) correct for this deficiency.
9.3 
Physics Residual and Constraint Enforcement
Let 
u
=
W
−
1
​
[
c
]
u=W^{-1}[c]
 denote the reconstructed field in physical space.
We define the governing residual
R
(
u
)
=
∂
t
u
+
(
u
⋅
∇
)
u
−
ν
Δ
u
−
f
,
R(u)=\partial_{t}u+(u\cdot\nabla)u-\nu\Delta u-f,
(41)
where 
f
f
 denotes external forcing or learned source terms.
In incompressible settings, the pressure term is eliminated by projection onto
the divergence-free subspace.
The physics regularization term penalizes violations of the governing dynamics:
ℒ
phys
=
‖
𝒫
⁡
(
R
⁡
(
u
)
)
‖
2
,
\mathcal{L}_{\mathrm{phys}}=\big\|\mathcal{P}\big(R(u)\big)\big\|^{2},
(42)
where 
𝒫
\mathcal{P}
 is the Helmholtz–Hodge projection operator.
For periodic domains, 
𝒫
\mathcal{P}
 admits a closed-form expression in Fourier
space,
𝒫
​
v
^
​
(
k
)
=
(
I
−
k
​
k
⊤
‖
k
‖
2
)
​
v
^
​
(
k
)
,
\widehat{\mathcal{P}v}(k)=\left(I-\frac{kk^{\top}}{\|k\|^{2}}\right)\hat{v}(k),
(43)
ensuring exact enforcement of incompressibility up to numerical precision.
This term transforms the learning problem from unconstrained density estimation
into constrained stochastic modeling on a physically admissible manifold.
From a variational perspective, it acts as a soft penalty enforcing that
generated trajectories remain close to solutions of the underlying PDE.
9.4 
Boundary and Conditioning Losses
Generative control is achieved through boundary and initial conditions, encoded
via the loss 
ℒ
BC
\mathcal{L}_{\mathrm{BC}}
.
Examples include:
•
initial conditions 
u
​
(
x
,
0
)
=
u
0
​
(
x
)
u(x,0)=u_{0}(x)
 (text prompts or initial frames),
•
spatial boundary conditions for video domains,
•
semantic or stylistic constraints imposed on subsets of coefficients.
Formally, the boundary loss may be written as
ℒ
BC
=
𝔼
(
x
,
t
)
∈
∂
Ω
​
‖
u
⁡
(
x
,
t
)
−
u
¯
​
(
x
,
t
)
‖
2
,
\mathcal{L}_{\mathrm{BC}}=\mathbb{E}_{(x,t)\in\partial\Omega}\big\|u(x,t)-\bar{u}(x,t)\big\|^{2},
(44)
where 
u
¯
\bar{u}
 denotes prescribed boundary data and 
∂
Ω
\partial\Omega
 the
boundary of the spatiotemporal domain.
This formulation parallels classical weak enforcement of boundary conditions in
finite element and spectral methods.
9.5 
Interpretation as Variational Inference with Constraints
The total loss (
38
) admits a probabilistic interpretation.
Specifically, training minimizes the Kullback–Leibler divergence between the
model distribution and a target posterior of the form
p
⁡
(
u
∣
constraints
)
∝
p
diff
​
(
u
)
​
exp
⁡
(
−
λ
R
​
ℰ
phys
​
(
u
)
−
λ
B
​
ℰ
BC
​
(
u
)
)
,
p(u\mid\text{constraints})\propto p_{\mathrm{diff}}(u)\exp\!\left(-\lambda_{R}\mathcal{E}_{\mathrm{phys}}(u)-\lambda_{B}\mathcal{E}_{\mathrm{BC}}(u)\right),
(45)
where 
p
diff
p_{\mathrm{diff}}
 is the diffusion prior and
ℰ
phys
\mathcal{E}_{\mathrm{phys}}
, 
ℰ
BC
\mathcal{E}_{\mathrm{BC}}
 are energy functionals
corresponding to physics and boundary constraints.
Thus, training performs approximate Bayesian inference under a structured prior,
rather than maximum likelihood estimation alone.
9.6 
Relation to PINNs, Neural Operators, and Diffusion Models
The proposed objective generalizes several existing paradigms.
Physics-Informed Neural Networks (PINNs) correspond to deterministic models with
ℒ
diff
=
0
\mathcal{L}_{\mathrm{diff}}=0
.
N

11.7 
Limitations
Despite their conceptual and theoretical appeal, Spectral Generative Flow Models
also introduce new challenges and limitations that must be addressed.
First, the mathematical sophistication of the framework is significantly higher
than that of standard transformer models.
Training and sampling involve stochastic differential equations, projection
operators, and spectral transforms, which complicate implementation, debugging,
and optimization.
Bridging this gap will require robust software abstractions and improved
numerical tooling.
Second, while physics-inspired constraints provide strong inductive bias, they
may be overly restrictive in some linguistic or creative contexts.
Not all aspects of language or art obey conservation-like principles, and
imposing such structure indiscriminately may suppress desirable forms of
novelty or divergence.
Careful design of constraint strength and scale-dependent stochasticity will be
essential.
Third, empirical validation at scale remains an open challenge.
Although the framework promises superior data efficiency and stability, large-
scale benchmarks comparable to those used for vLLMs have not yet been explored.
Demonstrating competitive or superior performance on real-world tasks is a
necessary step toward practical adoption.
Finally, interpretability, while improved at the dynamical level, introduces
new abstractions that may be unfamiliar to practitioners.
Understanding and diagnosing failure modes in function-space dynamics requires
different intuitions than token-level debugging.
12 
Conclusion
This work proposes a foundational rethinking of generative modeling.
By abandoning discrete token-based architectures and attention mechanisms in
favor of continuous, constrained stochastic dynamics, we introduce Spectral
Generative Flow Models as a viable post-transformer alternative.
SGFMs unify text, video, and physical simulation under a single mathematical
framework, replacing explicit global interaction with 

B.8 
Hybrid SGFM Sampling Complexity
Each SGFM sampling iteration alternates between:
1.
spectral diffusion: 
O
⁡
(
N
)
O(N)
 or 
O
⁡
(
N
​
log
⁡
N
)
O(N\log N)
,
2.
SPDE correction: 
O
⁡
(
N
​
log
⁡
N
)
O(N\log N)
.
Theorem B.7
 
(Overall Sampling Complexity)
.
One full SGFM sampling step satisfies
cost
⁡
(
SGFM step
)
=
O
⁡
(
N
​
log
⁡
N
)
,
\mathrm{cost}(\text{SGFM step})=O(N\log N),
dominated by the projection and wavelet transforms.
Comparison to Transformers.
Transformer-based vLLMs require 
O
⁡
(
N
2
)
O(N^{2})
 per layer due to attention.
SGFMs reduce this to 
O
⁡
(
N
​
log
⁡
N
)
O(N\log N)
 while providing:
•
locality,
•
multiscale structure,
•
physical constraints,
•
continuous dynamics.
This constitutes a fundamental computational advantage for long-context or high-resolution
generative modeling.
  
    Experimental support, please
view the build logs
    for errors. Generated by
      
        L
A
        T
E
      
      
xml
      
    
.
  
    
Instructions for reporting errors
    
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
      support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
      methods listed below:
    
      
Click the "Report Issue" 
(
            
          
)
 button, located in the page header.
    
    
Tip:
 You can select the relevant text first, to include it in your report.
    
Our team has already identified 
the following issues
. We appreciate your time reviewing and reporting rendering errors we
      may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
      should not be a barrier to accessing research. Thank you for your continued support in championing open access for
      all.
    
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a 
list of packages that need conversion
, and welcome 
developer contributions
.
  
  
    
      
        We gratefully acknowledge support from
        our 
major funders
,
member institutions
, 
,
        and all contributors.
      
        
About
        
·
        
Help
        
·
        
Contact
        
·
        
Subscribe
        
·
        
Copyright
        
·
        
Privacy
        
·
        
Accessibility
        
·
        
Operational Status
 (opens in new tab)
      
    
    
      
Major funding support from
      
        

