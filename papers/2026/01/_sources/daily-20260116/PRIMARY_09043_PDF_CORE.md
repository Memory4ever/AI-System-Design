# 2601.09043v1 exact PDF core

Exact PDF https://arxiv.org/pdf/2601.09043v1. PDF title metadata says This Draft January15 2026; requested exact HTML says August11 2026, not usable to backfill this event. Necessary LLM interface/evaluation core from PDF only; no default revision diff.

L0@P0: Horseshoe Mixtures-of-Experts (HS-MoE)
L1@P0: Nick Polson
L2@P0: Booth School of Business
L3@P0: University of Chicago
L4@P0: Vadim Sokolov*
L5@P0: Department of Systems Engineering
L6@P0: and Operations Research
L7@P0: George Mason University
L8@P0: First Draft: December 9, 2025
L9@P0: This Draft: January 15, 2026
L10@P0: Abstract
L11@P0: Horseshoe mixtures-of-experts (HS-MoE) models provide a Bayesian framework for
L12@P0: sparse expert selection in mixture-of-experts architectures. We combine the horseshoe prior’s adaptive global-local shrinkage with input-dependent gating, yielding
L13@P0: data-adaptive sparsity in expert usage. Our primary methodological contribution is a
L14@P0: particle learning algorithm for sequential inference, in which the filter is propagated
L15@P0: forward in time while tracking only sufficient statistics. We also discuss how HS-MoE
L16@P0: relates to modern mixture-of-experts layers in large language models, which are deployed under extreme sparsity constraints (e.g., activating a small number of experts
L17@P0: per token out of a large pool).
L18@P0: Keywords: Mixture-of-Experts, Horseshoe Prior, Particle Learning, Sparse LLMs, Bayesian
L19@P0: Inference
L20@P0: *Nick Polson is at Chicago Booth: ngp@chicagobooth.edu. Vadim Sokolov is Associate Professor at
L21@P0: Volgenau School of Engineering, George Mason University, USA: vsokolov@gmu.edu.
L22@P0: 1
L23@P0-1: arXiv:2601.09043v1 [stat.ML] 14 Jan 20261 Introduction
L24@P1: Mixture-of-Experts (MoE) models provide a powerful framework for combining multiple specialized models through input-dependent gating [Jacobs et al., 1991, Jordan and

L600@P7: (i)
L601@P7: 1:n
L602@P7: }
L603@P7: N
L604@P7: i=1
L605@P7: , pˆ(y1:n)
L606@P7: 3.7 Computational Complexity
L607@P7: For Gaussian linear experts with d features, the per-observation cost is dominated by
L608@P7: evaluating K expert predictives for each particle and updating one expert and up to K − 1
L609@P7: sticks. With dense linear algebra, this is O(NKd2) per observation (due to rank-one updates and linear solves). In implementations, maintaining Cholesky factorizations for
L610@P7: the relevant precision matrices improves numerical stability and reduces constants. This
L611@P7: compares favorably to batch MCMC, which requires O(nKd2) per iteration and many
L612@P7: iterations for convergence. For streaming data, particle learning processes each observation once, achieving O(nNKd2
L613@P7: ) total complexity versus O(TnKd2) for MCMC with T
L614@P7: iterations.
L615@P7: 3.8 Data Augmentation, Conditionally Conjugate Sufficient Statistics
L616@P7: Particle learning requires that (conditional) predictive probabilities and parameter updates be available in closed form. For Gaussian experts (6) this is already true (Section 3.3).
L617@P7-8: 8For non-Gaussian expert likelihoods or robust losses, Polson and Scott [2012a] provide a
L618@P8: general variance–mean mixture representation that makes a broad class of models conditionally Gaussian given latent variables ω.
L619@P8: Concretely, for many likelihoods (or pseudo-likelihoods) with linear predictor ηi =
L620@P8: X
L621@P8: ⊤
L622@P8: i
L623@P8: θ, one can introduce ωi such that
L624@P8: p(yi| ηi) ∝
L625@P8: Z
L626@P8: expκ(yi) ηi − 1
L627@P8: 2ωiη
L628@P8: 2
L629@P8: i
L630@P8: 
L631@P8: p(ωi| yi) dωi, (32)
L632@P8: so that conditional on ωi, the dependence on θ is Gaussian (quadratic in ηi). With a
L633@P8: Gaussian prior on θ, the conditional posterior is Gaussian and can be summarized by
L634@P8: sufficient statistics (the same Λ, h structure as in Section 3.4). This is the mechanism by
L635@P8: which particle learning extends beyond purely Gaussian experts.
L636@P8: For example, the Laplace likelihood p(y | η) ∝ exp(−|y − η|/b) admits a scalemixture-of-Gaussians representation with an exponential mixing distribution on the variance; conditional on the mixing variable, (y | η, ω) is Gaussian [Polson and Scott, 2012a],
L637@P8: yielding conjugate updates for robust expert regressions within each particle.
L638@P8: 3.9 Alternative: MCMC with Data Augmentation
L639@P8: For batch inference, standard MCMC provides an alternative using data augmentation
L640@P8: [Polson and Scott, 2012a]. The inverse-gamma representation enables Gibbs sampling
L641@P8: with conjugate conditionals. However, MCMC requires processing all data each iteration,
L642@P8: making particle learning preferable for streaming or large-scale settings.
L643@P8: 3.10 P´olya–Gamma identity (logistic gating)
L644@P8: For the Bernoulli logit likelihood (used by each stick in Section 3.4), the Polya–Gamma ´
L645@P8: identity [Polson et al., 2013] gives an exact augmentation:
L646@P8: (e
L647@P8: ψ)a
L648@P8: (1 + e
L649@P8: ψ)
L650@P8: b
L651@P8: = 2
L652@P8: −b
L653@P8: e
L654@P8: κψ Z ∞
L655@P8: 0
L656@P8: e
L657@P8: −ωψ2/2 p(ω)dω, (33)
L658@P8: where ω ∼ PG(b, 0). Conditional on ω, the logit likelihood becomes quadratic in ψ,
L659@P8: hence Gaussian in the regression coefficients. Stick-breaking extends this construction
L660@P8: from binary logits to categorical gating while preserving conditional Gaussian updates
L661@P8: [Linderman et al., 2015].
L662@P8: 3.11 Integration with Transformer Architectures
L663@P8: In modern transformer architectures, MoE layers replace the feed-forward network (FFN)
L664@P8: in selected blocks. Given an input token representation X, the HS-MoE layer computes:
L665@P8: HS-MoE(X) =
L666@P8: K
L667@P8: ∑
L668@P8: k=1
L669@P8: gk(X; ϕ) FFNk(X), (34)
L670@P8-9: 9where horseshoe priors on the gating parameters ϕ induce adaptive sparsity. Each FFN
L671@P9: expert has the standard form:
L672@P9: FFNk(X) = W
L673@P9: (2)
L674@P9: k
L675@P9: σ(W
L676@P9: (1)
L677@P9: k
L678@P9: X + b
L679@P9: (1)
L680@P9: k
L681@P9: ) + b
L682@P9: (2)
L683@P9: k
L684@P9: , (35)
L685@P9: where σ(·) is a nonlinear activation (GeLU or SiLU).
L686@P9: Remark 3.1 (Comparison to Top-k Routing). Standard sparse MoE uses hard top-k selection,
L687@P9: activating exactly k experts per token regardless of input. In contrast, HS-MoE provides soft
L688@P9: sparsity where the effective number of experts is data-driven. When most λk ≈ 0, the posterior
L689@P9: concentrates on configurations with few active experts, but the model can activate more experts
L690@P9: when the data warrants it.
L691@P9: 4 Application
L692@P9: Training and deployment of MoE layers in large language models confront expert collapse (a small subset of experts dominates), routing sensitivity under distribution shift,
L693@P9: and strict compute constraints that require top-k activation per token. HS-MoE addresses
L694@P9: these issues by placing structured global-local shrinkage on router parameters, encouraging most expert logits to be effectively inactive while permitting a small subset to escape
L695@P9: shrinkage when supported by data, and by representing uncertainty over routing decisions.
L696@P9: Despite its probabilistic formulation, HS-MoE is compatible with compute-constrained
L697@P9: inference. In deployment, one uses the Bayesian router to produce expert scores and
L698@P9: then applies standard top-k selection: experts may be ranked by posterior mean logits
L699@P9: E[ηk(X) | D] (or a posterior draw), with optional uncertainty-aware ranking such as
L700@P9: E[ηk(X)] − α
L701@P9: q
L702@P9: Var(ηk(X)),
L703@P9: to avoid unstable routing early in training or under distribution shift. The resulting expert
L704@P9: selection and compute budget are identical to standard sparse MoE inference; only the
L705@P9: scoring function used to rank experts is modified.
L706@P9: Token-level particle learning is generally too expensive for large-scale pretraining, so
L707@P9: HS-MoE should be viewed as a Bayesian router that can be trained with scalable approximations. One option is variational Bayes for the router, maintaining an approximate posterior over ϕ and horseshoe scales and using minibatches of tokens with Polya–Gamma ´
L708@P9: (or a local quadratic approximation) to obtain stable, approximately Gaussian updates. A
L709@P9: second option is MAP-style training with horseshoe-like regularization on router weights,
L710@P9: optimized by SGD/Adam jointly with expert parameters, which preserves the sparse
L711@P9: routing inductive bias while matching standard training pipelines. A practical hybrid
L712@P9: is to train experts with standard optimization and periodically re-fit the router (and its
L713@P9: uncertainty) on recent activations using the sequential updates in Sections 3.4–3.5.
L714@P9: Particle learning is most viable in streaming and continual settings such as domain
L715@P9: adaptation, personalization, and interaction logs, where data arrive sequentially and the
L716@P9-10: 10router must adapt without reprocessing the full history. In these regimes, posterior predictive resampling provides a principled mechanism for online routing adaptation with
L717@P10: uncertainty quantification. Evaluation may report perplexity or downstream accuracy,
L718@P10: expert utilization and load balance, routing entropy and calibration, robustness under
L719@P10: distribution shift, and training stability (including router/expert collapse frequency).
L720@P10: 4.1 Example: Gaussian Mixture Regression
L721@P10: To illustrate the mechanics of HS-MoE in a setting where all expert updates are closed
L722@P10: form, we include a synthetic regression example with K = 10 Gaussian linear experts
L723@P10: (6) and n = 500 observations, where only s = 3 experts are active. Covariates are generated as Xi ∼ N (0, Id) with d = 5, and allocations zi are drawn from a sparse datagenerating gate so that P(zi ∈ {1, 2, 3} | Xi) dominates. Conditional on zi = k, responses
L724@P10: are sampled as yi = X
L725@P10: ⊤
L726@P10: i
L727@P10: βk + εi with εi ∼ N (0, σ
L728@P10: 2
L729@P10: k
L730@P10: ). The reproducible setup and outputs
L731@P10: shown below are generated by running python scripts/generate synth example.py,
L732@P10: which writes the LaTeX tables to generated/ and the figure to fig/.
L733@P10: In applications of particle learning (Section 3.5), posterior mean allocation frequencies are computed by averaging particle-averaged allocation probabilities across time.
L734@P10: For the synthetic generator we report the empirical allocation frequencies from the datagenerating allocations, which serve as a reference target for what a well-calibrated sparse
L735@P10: router should recover.
L736@P10: Table 1: Synthetic HS-MoE regression example (reproducible setup).
L737@P10: Quantity Value
L738@P10: Number of experts K 10
L739@P10: Active experts s 3 (experts 1–3)
L740@P10: Sample size n 500
L741@P10: Feature dimension d 5
L742@P10: Particles N 1000
L743@P10: Experts Gaussian linear, Normal–IG prior
L744@P10: Gate softmax, sparse by construction (binactive = −3.0, T = 0.70)
L745@P10: 5 Theoretical Properties
L746@P10: Mixture-of-experts models achieve universal approximation with favorable rates. For
L747@P10: functions in the Sobolev class Wr
L748@P10: p on [0, 1]
L749@P10: d
L750@P10: , MoE with K experts achieves approximation
L751@P10: error [Zeevi et al., 1998]:
L752@P10: inf
L753@P10: fMoE∈MK
L754@P10: ∥ f − fMoE∥Lp = O
L755@P10: 
L756@P10: K
L757@P10: −r/d
L758@P10: 
L759@P10: , (36)
L760@P10: where r is the smoothness parameter. This rate matches that of free-knot splines and
L761@P10: neural networks.
L762@P10-11: 111 2 3 4 5 6 7 8 9 10
L763@P11: Expert index k
L764@P11: 0.0
L765@P11: 0.1
L766@P11: 0.2
L767@P11: 0.3
L768@P11: 0.4
L769@P11: Allocation frequency
L770@P11: Figure 1: Allocation frequencies across experts in the synthetic example (generated by
L771@P11: scripts/generate synth example.py).
L772@P11: For sparse MoE activating k of K experts, recent work [Zhao et al., 2024] establishes
L773@P11: generalization error bounds depending on the Rademacher complexity Rn(H) of the expert class and the Natarajan dimension dN of the router:
L774@P11: Egen = O
L775@P11: 
L776@P11: Rn(H) + r
L777@P11: k · dN(1 + log(K/k))
L778@P11: n
L779@P11: !
L780@P11: . (37)
L781@P11: This bound explicitly shows how sparsity (k ≪ K) improves generalization. The horseshoe prior provides a soft mechanism for achieving sparsity, where the effective k is determined by the posterior rather than a hard constraint.
L782@P11: 6 Discussion
L783@P11: We have introduced Horseshoe Mixture-of-Experts (HS-MoE), a Bayesian framework combining three key elements: the horseshoe prior’s adaptive shrinkage for automatic expert
L784@P11: selection [Carvalho et al., 2010b, van der Pas et al., 2014], particle learning for efficient
L785@P11: sequential inference [Carvalho et al., 2010a], and interacting particle system theory for
L786@P11: convergence guarantees [Johannes et al., 2008]. The particle learning framework offers
L787@P11: several advantages over batch MCMC, including sequential processing of observations,
L788@P11: reduced storage requirements through sufficient statistic tracking, natural handling of
L789@P11: streaming data, and straightforward marginal likelihood computation for model selection. While stochastic gradient descent is standard for training MoE in deep learning, our
L790@P11: approach offers a probabilistic alternative that quantifies uncertainty and enables online
L791@P11: model selection, albeit at higher computational cost per sample.
L792@P11: Compared to existing routing mechanisms (Table 2), HS-MoE provides adaptive soft
L793@P11: sparsity rather than the hard top-k selection or the dense computation of Soft MoE. The
L664@P8: in selected blocks. Given an input token representation X, the HS-MoE layer computes:
L665@P8: HS-MoE(X) =
L666@P8: K
L667@P8: ∑
L668@P8: k=1
L669@P8: gk(X; ϕ) FFNk(X), (34)
L670@P8-9: 9where horseshoe priors on the gating parameters ϕ induce adaptive sparsity. Each FFN
L671@P9: expert has the standard form:
L672@P9: FFNk(X) = W
L673@P9: (2)
L674@P9: k
L675@P9: σ(W
L676@P9: (1)
L677@P9: k
L678@P9: X + b
L679@P9: (1)
L680@P9: k
L681@P9: ) + b
L682@P9: (2)
L683@P9: k
L684@P9: , (35)
L685@P9: where σ(·) is a nonlinear activation (GeLU or SiLU).
L686@P9: Remark 3.1 (Comparison to Top-k Routing). Standard sparse MoE uses hard top-k selection,
L687@P9: activating exactly k experts per token regardless of input. In contrast, HS-MoE provides soft
L688@P9: sparsity where the effective number of experts is data-driven. When most λk ≈ 0, the posterior
L689@P9: concentrates on configurations with few active experts, but the model can activate more experts
L690@P9: when the data warrants it.
L691@P9: 4 Application
L692@P9: Training and deployment of MoE layers in large language models confront expert collapse (a small subset of experts dominates), routing sensitivity under distribution shift,
L693@P9: and strict compute constraints that require top-k activation per token. HS-MoE addresses
L694@P9: these issues by placing structured global-local shrinkage on router parameters, encouraging most expert logits to be effectively inactive while permitting a small subset to escape
L695@P9: shrinkage when supported by data, and by representing uncertainty over routing decisions.
L696@P9: Despite its probabilistic formulation, HS-MoE is compatible with compute-constrained
L697@P9: inference. In deployment, one uses the Bayesian router to produce expert scores and
L698@P9: then applies standard top-k selection: experts may be ranked by posterior mean logits
L699@P9: E[ηk(X) | D] (or a posterior draw), with optional uncertainty-aware ranking such as
L700@P9: E[ηk(X)] − α
L701@P9: q
L702@P9: Var(ηk(X)),
L703@P9: to avoid unstable routing early in training or under distribution shift. The resulting expert
L704@P9: selection and compute budget are identical to standard sparse MoE inference; only the
L705@P9: scoring function used to rank experts is modified.
L706@P9: Token-level particle learning is generally too expensive for large-scale pretraining, so
L707@P9: HS-MoE should be viewed as a Bayesian router that can be trained with scalable approximations. One option is variational Bayes for the router, maintaining an approximate posterior over ϕ and horseshoe scales and using minibatches of tokens with Polya–Gamma ´
L708@P9: (or a local quadratic approximation) to obtain stable, approximately Gaussian updates. A
L709@P9: second option is MAP-style training with horseshoe-like regularization on router weights,
L710@P9: optimized by SGD/Adam jointly with expert parameters, which preserves the sparse
L711@P9: routing inductive bias while matching standard training pipelines. A practical hybrid
L712@P9: is to train experts with standard optimization and periodically re-fit the router (and its
L713@P9: uncertainty) on recent activations using the sequential updates in Sections 3.4–3.5.
L714@P9: Particle learning is most viable in streaming and continual settings such as domain
L715@P9: adaptation, personalization, and interaction logs, where data arrive sequentially and the
L716@P9-10: 10router must adapt without reprocessing the full history. In these regimes, posterior predictive resampling provides a principled mechanism for online routing adaptation with
L717@P10: uncertainty quantification. Evaluation may report perplexity or downstream accuracy,
L718@P10: expert utilization and load balance, routing entropy and calibration, robustness under
L719@P10: distribution shift, and training stability (including router/expert collapse frequency).
L720@P10: 4.1 Example: Gaussian Mixture Regression
L721@P10: To illustrate the mechanics of HS-MoE in a setting where all expert updates are closed
L722@P10: form, we include a synthetic regression example with K = 10 Gaussian linear experts
L723@P10: (6) and n = 500 observations, where only s = 3 experts are active. Covariates are generated as Xi ∼ N (0, Id) with d = 5, and allocations zi are drawn from a sparse datagenerating gate so that P(zi ∈ {1, 2, 3} | Xi) dominates. Conditional on zi = k, responses
L724@P10: are sampled as yi = X
L725@P10: ⊤
L726@P10: i
L727@P10: βk + εi with εi ∼ N (0, σ
L728@P10: 2
L729@P10: k
L730@P10: ). The reproducible setup and outputs
L731@P10: shown below are generated by running python scripts/generate synth example.py,
L732@P10: which writes the LaTeX tables to generated/ and the figure to fig/.
L733@P10: In applications of particle learning (Section 3.5), posterior mean allocation frequencies are computed by averaging particle-averaged allocation probabilities across time.
L734@P10: For the synthetic generator we report the empirical allocation frequencies from the datagenerating allocations, which serve as a reference target for what a well-calibrated sparse
L735@P10: router should recover.
L736@P10: Table 1: Synthetic HS-MoE regression example (reproducible setup).
L737@P10: Quantity Value
L738@P10: Number of experts K 10
L739@P10: Active experts s 3 (experts 1–3)
L740@P10: Sample size n 500
L741@P10: Feature dimension d 5
L742@P10: Particles N 1000
L743@P10: Experts Gaussian linear, Normal–IG prior
L744@P10: Gate softmax, sparse by construction (binactive = −3.0, T = 0.70)
L745@P10: 5 Theoretical Properties
L746@P10: Mixture-of-experts models achieve universal approximation with favorable rates. For
L747@P10: functions in the Sobolev class Wr
L748@P10: p on [0, 1]
L749@P10: d
L750@P10: , MoE with K experts achieves approximation
L751@P10: error [Zeevi et al., 1998]:
L752@P10: inf
L753@P10: fMoE∈MK
L754@P10: ∥ f − fMoE∥Lp = O
L755@P10: 
L756@P10: K
L757@P10: −r/d
L758@P10: 
L759@P10: , (36)
L760@P10: where r is the smoothness parameter. This rate matches that of free-knot splines and
L761@P10: neural networks.
L762@P10-11: 111 2 3 4 5 6 7 8 9 10
L763@P11: Expert index k
L764@P11: 0.0
L765@P11: 0.1
L766@P11: 0.2
L767@P11: 0.3
L768@P11: 0.4
L769@P11: Allocation frequency
L770@P11: Figure 1: Allocation frequencies across experts in the synthetic example (generated by
L771@P11: scripts/generate synth example.py).
L772@P11: For sparse MoE activating k of K experts, recent work [Zhao et al., 2024] establishes
L773@P11: generalization error bounds depending on the Rademacher complexity Rn(H) of the expert class and the Natarajan dimension dN of the router:
L774@P11: Egen = O
L775@P11: 
L776@P11: Rn(H) + r
L777@P11: k · dN(1 + log(K/k))
L778@P11: n
L779@P11: !
L780@P11: . (37)
L781@P11: This bound explicitly shows how sparsity (k ≪ K) improves generalization. The horseshoe prior provides a soft mechanism for achieving sparsity, where the effective k is determined by the posterior rather than a hard constraint.
L782@P11: 6 Discussion
L783@P11: We have introduced Horseshoe Mixture-of-Experts (HS-MoE), a Bayesian framework combining three key elements: the horseshoe prior’s adaptive shrinkage for automatic expert
L784@P11: selection [Carvalho et al., 2010b, van der Pas et al., 2014], particle learning for efficient
L785@P11: sequential inference [Carvalho et al., 2010a], and interacting particle system theory for
L786@P11: convergence guarantees [Johannes et al., 2008]. The particle learning framework offers
L787@P11: several advantages over batch MCMC, including sequential processing of observations,
L788@P11: reduced storage requirements through sufficient statistic tracking, natural handling of
L789@P11: streaming data, and straightforward marginal likelihood computation for model selection. While stochastic gradient descent is standard for training MoE in deep learning, our
L790@P11: approach offers a probabilistic alternative that quantifies uncertainty and enables online
L791@P11: model selection, albeit at higher computational cost per sample.
L792@P11: Compared to existing routing mechanisms (Table 2), HS-MoE provides adaptive soft
L793@P11: sparsity rather than the hard top-k selection or the dense computation of Soft MoE. The
L794@P11: number of active experts is data-driven rather than fixed, and the Bayesian framework enables principled uncertainty quantification and model selection via marginal likelihoods
L795@P11: rather than heuristics.
L796@P11-12: 12Table 2: Comparison of expert routing methods
L797@P12: Property Top-k Soft MoE HS-MoE
L798@P12: Sparsity type Hard None Soft (adaptive)
L799@P12: Experts per input Fixed k All K Data-driven
L800@P12: Uncertainty quantification No No Yes
L801@P12: Sequential inference No No Yes
L802@P12: Model selection Heuristic Heuristic Marginal likelihood
L803@P12: Several directions merit future investigation: variational approximations [Ghosh et al.,
L804@P12: 2017] for scaling to transformer-sized models, group-level horseshoe priors for structured
L805@P12: layer-wise expert selection, nonparametric priors for online adjustment of the number
L806@P12: of experts K, and connections to Kolmogorov-Arnold Networks [Polson and Sokolov,
L807@P12: 2025] for efficient function approximation. As mixture-of-experts architectures continue
L808@P12: to scale in modern LLMs, Bayesian approaches will play an increasingly important role
L809@P12: in understanding and improving these systems.
