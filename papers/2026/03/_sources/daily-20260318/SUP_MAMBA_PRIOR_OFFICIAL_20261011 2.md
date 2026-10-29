Mamba-3 Part 1 | Goomba Lab (https://goombalab.github.io/blog/2026/mamba3-part1/)
citeturn33066view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://goombalab.github.io/blog/2026/mamba3-part1/","lineno":null}); Total lines: 138
L0: # Mamba-3 Part 1
L1: ### Contents
L2: 
L3: cite0†The Mamba-3 Model L4: 
L5: cite1†Architecture L6: 
L7: cite2†Empirical Results L8: 
L9:   * cite3†Language Modeling L10:   * cite4†Retrieval Tasks L11: 
L12: cite5†Kernels Here, There, and Everywhere L13: 
L14:   * cite6†Benchmarking Latencies L15:   * cite7†Design Choices L16: 
L17: cite8†Next Up L18: 
L19: [cite9†Paper†arxiv.org ] [cite10†Code†github.com ]
L20: 
L21: This series is cross-posted at cite11†tridao.me†tridao.me L22: 
L23:   1. Part I
L24:   2. cite12†Part II L25: Since the release of Mamba-2 in mid-2024, most architectures have switched from Mamba-1. Why? Mamba-2 made the bet that training efficiency was the largest bottleneck for state space models (SSMs), and thus simplified the underlying SSM mechanism to deliver $2-8\times$ faster training compared to its predecessor, leading to wider adoption.
L26: Since then, the LLM landscape has started to shift. While pretraining is still super important, more attention has been focused on post-training and deployment, both of which are extremely inference-heavy. The scaling of post-training methods, especially with reinforcement learning with verifiable rewards (RLVR) for coding or math, requires huge amounts of generated rollouts, and most recently, agentic workflows, such as Codex, Claude Code, or even OpenClaw, have pushed inference demand through the roof.
L27: Despite the clear, growing importance of inference, many linear architectures (including Mamba-2) were developed from a training-first perspective. To accelerate pretraining, the underlying SSM was progressively simplified (e.g., the diagonal transition was reduced to a scalar times identity). While this brought training speed, it left the inference step “too simple” and squarely memory-bound — the GPUs aren’t brr-ing but moving memory most of the time.
L28: In this new age of inference, we care a lot about pushing the boundaries of the quality-efficiency frontier: we want the better models to run faster.
L29: 
L30: A natural question arises:
L31: 
L32: > What would an SSM designed with inference in mind look like?
L33: ## The Mamba-3 Model
L34: What’s missing? The main appeal of linear models is in their name: compute scales linearly with sequence length because of a fixed-size state. Unfortunately, there is no free lunch. The same fixed state size that enables efficient computation forces the model to compress all past information into one representation, the exact opposite of a Transformer, which stores all past information through a continuously growing state (the KV cache) — a fundamental difference.
L35: So, if we can’t grow the state, how do we make that fixed state do more work?
L36: We see that earlier designs simplified the recurrence and the transition matrix to make training fast. However, the change also reduced the richness of the dynamics and left decoding memory-bound: each token update performs very little computation relative to memory movement. This provides us with three levers we can pull: (1) make the recurrence itself more expressive, (2) use a richer transition matrix, and (3) add more parallel (and almost free) work inside each update.
L37: From these insights, we improve upon Mamba-2 in three core ways that:
L38:   1. increase the expressivity of the SSM mechanism through a more general recurrence derived from our exponential-trapezoidal discretization scheme,
L39:   2. expand the state-tracking capabilities by modeling a complex-valued SSM system, and
L40:   3. improve the model’s general performance with little impact on decode latency by using multi-input, multi-output (MIMO) SSMs, which model multiple SSMs in parallel, instead of the current single-input, single-output (SISO) SSMs.
L41: Through these three changes, Mamba-3 pushes the frontier of performance while maintaining similar inference latency.
L42: 
L43: > Notably, all three of these changes are inspired by the more “classical” control theory and state space model literature.
L44: 
L45: Our work goes against the grain of many modern linear architectures, which use alternative interpretations of recurrence (such as linear attention or test-time training) that don’t easily capture these concepts.
L46: ## Architecture
L47: 
L48: What has changed in the Mamba-2 layer? Beyond the three methodological upgrades to the core SSM discussed above, we’ve revamped the architecture a bit to make it more in line with conventional modern language models.
L49: 
L50: cite13†Image: Mamba-3 Architecture Mamba-3 Architecture.
L51: 
L52: Based on the diagram, you’ll notice we’ve changed a couple of things. On a high level,
L53: Norms. We added in QKNormor "BCNorm" in SSM terminology, which empirically stabilizes the training of Mamba-3 models. The addition of this norm brings Mamba-3 in line with contemporary Transformer and Gated DeltaNet (GDN) models. With QKNorm, the RMSNorm from Mamba-2 becomes optional. However, we empirically find that it may still be worth keeping in hybrid models due to helping length extrapolation capabilities. More on this later.
L54: Goodbye Short Conv. We’ve been able to get rid of the pesky short causal convolution of Mamba-1/2 by combining (1) simple biases on B and C after BCNorm with (2) our new discretization-based recurrence. The new recurrence implicitly applies a convolution on the input to the hidden state, and we show how this is the case in Part 2 of our blog.
L55: 
L56: Can the short conv really be removed?
L57: The changes in Mamba-3 add convolution-like components inside the SSM recurrence but aren’t exactly interchangeable with the standard short conv placed outside the SSM recurrence.
L58: 
L59: The latter can still be used together with Mamba-3, but the decision not to was made empirically. We find adding the standard short conv back:
L60:   1. does not improve performance; in fact, it slightly worsens it, and
L61:   2. does not degrade retrieval capabilities on more real-world tasks (e.g., NIAH). That said, without a short convolution, training on small-scale synthetic tasks like MQAR becomes somewhat harder. Since real-world retrieval behavior remains unaffected, though, we don’t consider this a major limitation.
L62: As for why? We didn’t study the theoretical mechanisms, but in the paper, we hypothesize about how both the BC bias and the exponential-trapezoidal recurrence perform similar convolution-like mechanisms which empirically serve the same function as the external short conv.
L63: 
L64: Quick history lesson on the short conv.
L65: The short convolution is now a core component of most performant linear models today . Versions of the short conv were first used in recurrent architectures by H3 (in the form of a “shift SSM” which was inspired by the “smeared” induction heads work by Anthropic ) and RWKV-4 (through its “token shift” mechanism), before being popularized in its current form by Mamba-1.
L66: The reason it’s so commonplace is because previous works have repeatedly shown that short convolutions improve empirical performance as well as theoretically support induction-style retrieval capabilities .
L67: Finally, you’ll notice a couple of new components, namely RoPE and MIMO projections. The RoPE module expresses complex-valued SSMs via the interpretation of complex transitions as rotations, forgoing the costly reimplementation of kernels. The MIMO projections expand the B and C matrices to the appropriate representation needed for MIMO SSMs.
L68: We dig into the motivation and exact implementation of these two in greater detail in the second part of our blog (lots of goodies there 🎁), so for now, just think of them as standalone, fundamental improvements that individually contribute to improving the model’s performance and/or capabilities.
L69: 
L70: Finally, our overall architecture now adopts interleaved MLP layers following the standard convention of Transformers and other linear models.
L71: ## Empirical Results
L72: 
L73: We evaluate our final Mamba-3 model against other popular linear alternatives and the Transformer baseline.
L74: ### Language Modeling
L75: 
L76: cite14†Image: Downstream LM Evals Downstream Language Modeling Evaluations for Pretrained Models.
L77: We find that our new Mamba-3 model outperforms the prior Mamba-2 model and strong linear attention alternatives, such as GDN, on language modeling across various pretrained model scales. Mamba-3-SISO is directly comparable to prior linear models; for example, it matches Mamba-2 exactly in architecture shapes (model dimensions, state size, etc.) and has comparable training time.
L78: Our MIMO variant of Mamba-3 further boosts accuracy on our downstream tasks by more than 1 percentage point over the regular Mamba-3 at the 1B scale, with the caveat that MIMO requires longer training times but not longer decoding latencies!
L79: How can training costs go up but not inference?
L80: 
L81: While we will talk about this in detail in the second part of the blog, we give readers a sneak peek here:
L82: This dichotomy can be traced back to the respective compute versus memory-bound nature of training and inference. Current linear models have been designed to use lots of GPU tensor cores (one of the main contributions of Mamba-2) for fast training, but during decoding, each timestep requires so little compute that the hardware remains cold most of the time.
L83: Thus, if we design architectures around just increasing the amount of FLOPs needed for each time-step, inference latency stays roughly constant since we can just use some of the idle cores — not so much for training!
L84: ### Retrieval Tasks
L85: 
L86: cite15†Image: Retrieval Tasks Real-world and Synthetic Retrieval Tasks.
L87: 
L88: Linear models, with their fixed-size state, naturally underperform their Transformer counterparts on retrieval-based tasks. As expected, within pure models, the Transformer is superior on retrieval tasks, but Mamba-3 performs well within the class of sub-quadratic alternatives. Interestingly, the addition of MIMO further improves retrieval performance without increasing the state size.
L89: Given this innate deficit but overall strong modeling performance,
L90: 
L91: > we predict that linear layers will be predominantly used in conjunction with global self-attention layers in the future. $^*$
L92: 
L93: $^*$ at least for language modeling
L94: Hybrid models that combine the general memory-like nature of linear layers with the exact database-like storage of self-attention’s KV cache have been shown empirically to outperform pure models while enabling significant memory and compute savings , and we do find here that the combination of linear layers with self-attention enables better retrieval compared to a vanilla Transformer.
L95: However, we highlight that the exact way that these linear models interact with self-attention is not fully understood. For instance, we find that the use of the optional pre-output projection for Mamba-3 improves the length generalization performance on the synthetic NIAH tasks at the slight cost of in-context real-world retrieval tasks.
L96: Furthermore, even the details of the returned norm such as placement, e.g., pre-gate vs post-gate, and type, grouped vs regular, have non-negligible effects on accuracy on tasks composed of semi-structured and unstructured data, such as FDA and SWDE.
L97: ## Kernels Here, There, and Everywhere
L98: 
L99: We’re excited to see what people build with Mamba-3. To help facilitate this, we are open-sourcing our kernels, which are on par in terms of speed with the original Mamba-2 Triton kernels.
L100: ### Benchmarking Latencies
L101: 
L102: Prefill Latency
L103: 
L104: Model  | n=512  | 1024  | 2048  | 4096  | 16384
L105: --- | --- | --- | --- | --- | ---
L106: vLLM (Llama-3.2-1B)  | 0.26  | 0.52  | 1.08  | 2.08  | 12.17
L107: Gated DeltaNet  | 0.51  | 1.01  | 2.01  | 4.00  | 16.21
L108: Mamba-2  | 0.51  | 1.02  | 2.02  | 4.02  | 16.22
L109: Mamba-3 (SISO)  | 0.51  | 1.01  | 2.02  | 4.01  | 16.22
L110: Mamba-3 (MIMO $R=4$)  | 0.60  | 1.21  | 2.42  | 4.76  | 19.44
L111: 
L112: Prefill+Decode Latency
L113: Model  | n=512  | 1024  | 2048  | 4096  | 16384
L114: --- | --- | --- | --- | --- | ---
L115: vLLM (Llama-3.2-1B)  | 4.45  | 9.60  | 20.37  | 58.64  | 976.50
L116: Gated DeltaNet  | 4.56  | 9.11  | 18.22  | 36.41  | 145.87
L117: Mamba-2  | 4.66  | 9.32  | 18.62  | 37.22  | 149.02
L118: Mamba-3 (SISO)  | 4.39  | 8.78  | 17.57  | 35.11  | 140.61
L119: Mamba-3 (MIMO $R=4$)  | 4.74  | 9.48  | 18.96  | 37.85  | 151.81
L120: Prefill and prefill+decode (same token count for both prefill and decode) latencies across sequence lengths for a 1.5B model on a single H100-SXM 80GB GPU. A batch size of 128 was used for all sequence lengths, wall-clock times (in seconds) are reported over three repetitions.
L121: When comparing models at the 1.5B scale, Mamba-3 (SISO variant) achieves the fastest prefill + decode latency across all sequence lengths, outperforming Mamba-2, Gated DeltaNet, and even the Transformer with its highly optimized vLLM ecosystem. Furthermore, Mamba-3 MIMO is comparable to Mamba-2 in terms of speed but has much stronger performance.
L122: Mamba-3 SISO’s Triton-based prefill maintains nearly identical performance to Mamba-2, demonstrating that the new discretization and data-dependent RoPE embeddings do not introduce additional overhead, while Mamba-3 MIMO only incurs a moderate slowdown for prefill due to its efficient TileLang implementation. The strong decode performance for both Mamba-3 variants can be partially attributed to the CuTe DSL implementation, which was made significantly easier by the simplicity of Mamba-3 components.
L123: ### Design Choices
L124: 
L125: We spent a lot of time thinking about how to make the kernels as fast as possible without compromising on ease-of-use. We ended up using the following stack: Triton, TileLang, and CuTe DSL.
L126: The use of Triton was quite an easy choice. It’s pretty much standard for architecture development (the great cite16†flash linear attention†github.com repo is purely in PyTorch and Triton) for good reason, as it enables better performance than standard PyTorch by enabling controlled tiling and kernel fusion while being a platform-agnostic language.
L127: Triton also has some pretty nifty features, like cite17†PTX†modal.com (a GPU-oriented assembly language) injection and its Tensor Memory Accelerator support (on Hopper GPUs) for bulk, asynchronous transfers from global to shared memory.
L128: Our MIMO prefill kernels were developed with TileLang instead. The additional projections corresponding with the variant present an opportunity where we can reduce memory IO via strategic manipulation across a GPU’s memory hierarchy.
L129: Unfortunately, Triton didn’t provide the granularity of memory control we desired, so we opted for TileLang, which allows us to explicitly declare and control shared-memory tiles and create register fragments, reusing memory more efficiently while still being high-level enough for us to develop the kernels quickly.
L130: Since we’ve been hammering the importance of inference and decode, we decided to use CuTe DSL for our decode kernels. Through its Python interface, we’re able to generate low-level kernels using high-level abstractions from CUTLASS. Here, we practically have CUDA-level control, enabling us to develop highly-performant kernels tailored to the specifications of our hardware (Hopper GPUs, in this case).
L131: With fine-grained control over tensor layouts and warp specialization, we built a kernel that takes advantage of all the bells and whistles in the GPU.
L132: Importantly, these implementations across varying levels of GPU abstraction are made possible by the underlying algorithmic design of Mamba-3’s simple, lightweight additions and their clever instantiations. We discuss details such as the exact fusion structure and kernel DSL in more depth in our full release.
L133: ## Next Up
L134: 
L135: Glad you made it to the end of Part 1! There were a lot of details regarding our kernels and experimental results and ablations we didn’t have time to cover in this post, but don’t fret! Everything can be found in cite9†our paper†arxiv.org , and the kernels have been open-sourced at cite10†mamba-ssm†github.com !
L136: 
L137: Up next, the cite12†second (and final) part of the series delves into the three core improvements to Mamba-3 and their SSM foundations, and gives some directions we’re especially interested in.
--------------------------------------------------------------------------------
Mamba-3 Part 2 - Methodological Deep Dive | Goomba Lab (https://goombalab.github.io/blog/2026/mamba3-part2/)
citeturn33066view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://goombalab.github.io/blog/2026/mamba3-part2/","lineno":null}); Total lines: 223
L0: # Mamba-3 Part 2 - Methodological Deep Dive
L1: ### Contents
L2: 
L3: cite0†State Space Foundations L4: 
L5: cite1†Upgraded Discretization L6: 
L7:   * cite2†Exponential-Adjusted Discretizations L8:   * cite3†Recovering Prior Mamba Discretization L9:   * cite4†New Exponential-Trapezoidal Discretization L10:   * cite5†Parallel Representation of New Recurrence L11: 
L12: cite6†Complex-valued SSM L13: 
L14:   * cite7†Parity, what is that? L15:   * cite8†Representing with Real-valued SSMs L16:   * cite9†Efficient Implementation with RoPE Trick L17: 
L18: cite10†Multi-Input, Multi-Output L19:   * cite11†Working while Memory-Bound L20:   * cite12†The MIMO System L21:   * cite13†Intuition and Training L22:   * cite14†Instantiation L23: 
L24: cite15†The End, For Now L25: 
L26:   1. cite16†Part I L27:   2. Part II
L28: 
L29: We introduced our Mamba-3 model in cite16†Part I in which we mentioned that the three core methodological changes were inspired by the SSM perspective. Here, we’ll actually do a deep dive into what each of these three improvements entail, their motivations, and their derivations.
L30: But first, let’s refresh our memory on the underlying state space model and its background.
L31: ## State Space Foundations
L32: The state space model, at its most primitive, is a simple, continuous ordinary differential equation (ODE). The input $x(t) \in \mathbb{R}$ is mapped to output $y(t) \in \mathbb{R}$ through a hidden state $h(t) \in \mathbb{R}^N$ of size $N$, also referred to as the state size.
L33: In the past, in both deep learning and classical control theory, these systems were linear time-invariant (LTI), where the “state decay” transition $A \in \mathbb{R}^{(N\times N)}$, $B \in \mathbb{R}^{N}$, and $C \in \mathbb{R}^{N}$ terms were constant.
L34: \[\begin{aligned} h'(t) &= A h(t) + B x(t) \\ y(t) &= C^\top h(t) \end{aligned}\]
L35: 
L36: We will occasionally refer to $A$ as the state-transition, and $Bx(t)$ as the state-input.
L37: 
L38: Upon discretization with one’s favorite method, as demonstrated with the zero-order hold (ZOH) used in both Mamba-1 and Mamba-2, a familiar recurrence materializes,
L39: 
L40: \[\begin{aligned} h_{t} &= e^{\Delta_t A_t} h_{t-1}+ A_t^{-1}(e^{\Delta_t A_t} - I)\,B_t\,x_t \\ y_t &= C_t^\top h_t \end{aligned}\]
L41: where the discretized $\bar{A}$ and $\bar{B}$ are now $e^{\Delta_t A_t}$ and $A_t^{-1}(e^{\Delta_t A_t} - I)\,B_t$ respectively.
L42: 
L43: Eagle-eyed readers may ask “how does one go from a LTI system to a linear-time varying (LTV) system?” — if you did, the answer is revealed below!
L44: 
L45: Aside on prior Mamba discretizations
L46: 
L47: We’ll let you in on a little secret: prior Mamba discretizations used the canonical ZOH discretization scheme and just converted the fixed time-invariant variables A, B, and C to time-varying!
L48: No worries if this feels uneasy. We felt that too, which is why we formalized the discretization later (sorry for the clickbait, the answer is not here; you’ll have to keep on reading).
L49: 
L50: While there are no theoretical restrictions on the class of matrices $\bar{A}$ can be, computational constraints keep transition matrices structured, e.g., diagonal, scalar times identity, Householder (identity plus low-rank), etc.
L51: Great, now we’ve set up the underlying mechanism of Mamba used in both Mamba-1 and Mamba-2!
L52: 
L53: As a quick recap, Mamba-3 builds on Mamba-2 to improve the efficiency-performance trade-off of current SSMs with inference at the forefront. The three core improvements we’ve been discussing in this post are rooted in classical state space theory:
L54:   1. Instantiating a more generalized recurrence through a formal framework for discretizing the underlying ODE
L55:   2. Improving state-tracking abilities by converting to complex-valued SSM without the engineering challenges of explicit complex numbers
L56:   3. Increasing the expressivity of the SSM without increasing state size through a multi-input, multi-output (MIMO) formulation.
L57: 
L58: Let’s jump straight into it.
L59: ## Upgraded Discretization
L60: 
L61: Our end goal is to obtain a more general recurrence than that of current models from first principles. Luckily for us, the discretization of the continuous ODE provides the perfect opportunity to do so.
L62: But first, let’s lay down the foundation for our framework used in discretizing time-varying systems. Remember how we mentioned that prior Mamba discretizations adapted the canonical ZOH discretization by adding a time subscript to convert the method from LTI to LTV? Well, to be honest, we left a bit more out earlier.
L63: The cite17†actual implementation†github.com of Mamba frankensteined the canonical ZOH and Euler methods to create discretized parameters $\bar{A}_t = \exp(\Delta_t A_t), \bar{B}_t=\Delta_t B_t$.
L64: Holy heuristic! But it works empirically ¯\(ツ)/¯.
L65: 
L66: One potential explanation for why this mixture does so well despite not being theoretically grounded is that Euler is an approximation of ZOH. Taking the ZOH formula for discretized $\bar{B}_t=A_t^{-1}\left(\exp(\Delta_t A_t) - I \right) B_t$, if we use the approximation $\exp(x) \approx 1+x$, the resulting $\bar{B}_t \approx \Delta_t B_t$.
L67: This heuristic was always bugging us in the back of our minds, so in our work, we finally formalized the discretization.
L68: 
L69: > We develop a method that produces a class of formal discretizations for time-varying systems, including one called exponential-Euler that exactly corresponds to the formula used in Mamba-1/2.
L70: cite18†Image: Discretization Table Resulting final recurrent $h_t = \alpha_t h_{t-1} + \beta_t B_{t-1}x_{t-1} + \gamma_t B_tx_t$ from various discretization methods. Top half is LTI methods, and bottom is LTV methods derived from our discretization framework.
L71: ### Exponential-Adjusted Discretizations
L72: 
L73: So let’s actually figure out how to discretize our LTV system in a principled manner.
L74: 
L75: \[h'(t) = A(t)h(t) + B(t)x(t)\]
L76: The general intuition behind our framework is that a bare-bones ODE $f'(t) = Af(t)$ has a closed-form solution $f(t) = e^{tA} f(0)$. It follows that the one-step discrete update is then $x_{t+1} = e^{\Delta A}x_t$. Here, since the derivative includes $Ah(t)$, the state directly impacts the rate of change. Thus, the parameterization of A can rapidly oscillate the dynamics of the system, which forces explicit methods, like Euler, to take small $\Delta$ steps which limits the expressivity of the system.
L77: To mitigate this, we adjust the dynamics with an integrating factor of $e^{-At}$ to counteract the dominating exponential and directly analyze $e^{-At}h(t)$ instead. Let’s see how it applies to our system.
L78: 
L79: Taking our $h'(t)=A(t)h(t)+B(t)x(t)$ system, we apply an integrating factor of $e^{\int_0^t -A(s)ds}$ as $A$ is now time-varying.
L80: \[\begin{aligned} e^{\int_0^t -A(s)ds}h'(t) &= e^{\int_0^t -A(s)ds}A(t)h(t) + e^{\int_0^t -A(s)ds}B(t)x(t) \\ (e^{\int_0^t -A(s)ds}h(t))' &= e^{\int_0^t -A(s)ds}B(t)x(t) \end{aligned}\]
L81: 
L82: since $(e^{\int_0^t -A(s)ds})' = -A(t)e^{\int_0^t -A(s)ds}$.
L83: 
L84: Thus, when we want to discretize between timesteps $[\tau_{t-1}, \tau_t]$, we can just integrate both sides over that interval. For ease of notation, we denote $z(t) := e^{\int_0^t -A(s)ds}$.
L85: \[\begin{aligned} \tfrac{d}{dt}(z(t)h(t)) &= z(t)B(t)x(t) \\ \int_{\tau_{t-1}}^{\tau_t}\tfrac{d}{d\tau}(z(\tau)h(\tau))d\tau &= \int_{\tau_{t-1}}^{\tau_t}z(\tau)B(\tau)x(\tau)d\tau \\ z(\tau_{t})h(\tau_{t}) - z(\tau_{t-1})h(\tau_{t-1}) &= \int_{\tau_{t-1}}^{\tau_t}z(\tau)B(\tau)x(\tau)d\tau \\ z(\tau_{t})h(\tau_{t}) &= z(\tau_{t-1})h(\tau_{t-1}) + \int_{\tau_{t-1}}^{\tau_t}z(\tau)B(\tau)x(\tau)d\tau \\ \end{aligned}\]
L86: 
L87: Rearranging into a more familiar form and substituting back the $z(\tau)$ value:
L88: \[\begin{aligned} h(\tau_{t}) &= z(\tau_{t})^{-1}z(\tau_{t-1})h(\tau_{t-1}) + z(\tau_{t})^{-1}\int_{\tau_{t-1}}^{\tau_t}z(\tau)B(\tau)x(\tau)d\tau \\ h(\tau_t) &= \exp\left(\int_{\tau_{t-1}}^{\tau_t}A(s)ds\right)h(\tau_{t-1}) + \int_{\tau_{t-1}}^{\tau_t} \exp\left(\int_{\tau}^{\tau_t}A(s)ds\right)B(\tau)x(\tau) d\tau \end{aligned}\]
L89: Now, we’ve isolated the state-transition and the state-input through our integration factor. This means the most “difficult” part of the adjusted system can be calculated independently of the state-input integral, which is left to be approximated with many possible methods.
L90: 
L91: Under the LTV case, because $A(s)$ is continuous, we “sample” it with a right-hold assumption where $\forall s \in [\tau_{t-1},\tau_t], A(s) = A(\tau_t) = A_t$, resulting in
L92: \[h_t \approx \exp(\Delta_t A_t)h_{t-1} + \int_{\tau_{t-1}}^{\tau_t} \exp\left((\tau_t - \tau)A_t\right)B(\tau)x(\tau)d\tau\] When can the transition integral be directly calculated?
L93: 
L94: If $A$ is LTI, i.e., constant, then the state-transition integral is exactly $\exp(A \Delta_t)$, which is the discretized $\bar{A}$ term for canonical ZOH.
L95: 
L96: Under the assumption $x(\tau) = x_t$, if $B$ is also LTI, then $\bar{B}$ also recovers the canonical ZOH term, $A^{-1}\left(\exp(\Delta A) - I\right)B$.
L97: This final equation lays the foundation for recovering the prior Mamba discretization methods and is also the inspiration of our “exponential-“ style name, as the application of the integration factor can be seen as a style of exponential tilting or adjustment.
L98: ### Recovering Prior Mamba Discretization
L99: 
L100: As previously mentioned, prior Mamba discretizations differ on paper and in practice. Now, using our new discretization derivation and certain sampling assumptions, we can recover the reported LTV ZOH discretization and the implemented exponential-adjusted Euler discretization scheme, or exponential-Euler for short.
L101: 
L102: We have already recovered the $\bar{A}$ term for both, so we will focus only on the remaining state-input integral which evaluates to $\bar{B}$.
L103: ZOH: Assuming similar assumptions where $B(\tau), x(\tau)$ are constant and sampled at the right endpoint,
L104: \[\begin{aligned} (\cdot) &= B(\tau_t)x(\tau_t) \int_{\tau_{t-1}}^{\tau_t} \exp\left((\tau_t - \tau)A_t\right)d\tau\\ &= B_t\,x_t\exp(A_t\tau_t) \int_{\tau_{t-1}}^{\tau_t} \exp\left(-A_t\tau\right)d\tau \\ &= B_t\,x_t\exp(A_t\tau_t)\dfrac{1}{A_t}\left(\exp(-A_t\tau_{t-1}) - \exp(-A_t\tau_t)\right) \\ &= A_t^{-1}\left(\exp(A_t(\tau_t - \tau_{t-1})) - I\right)B_t\,x_t \\ &= A_t^{-1}\left(\exp({\Delta_tA_t})-I\right)B_t\,x_t \end{aligned}\]
L105: Exponential-Euler: Once again, we approximate the integral with Euler’s rule and hold the $B, x$ terms to the right endpoint.
L106: 
L107: \[\begin{aligned} (\cdot) &= B(\tau_t)x(\tau_t) \int_{\tau_{t-1}}^{\tau_t} \exp\left((\tau_t - \tau)A_t\right)d\tau \\ &= B_t\,x_t\exp(A_t\tau_t) \int_{\tau_{t-1}}^{\tau_t} \exp\left(-A_t\tau\right)d\tau \\ &\approx B_t\,x_t\exp(A_t\tau_t) (\tau_t - \tau_{t-1})\exp\left(-A_t\tau_t\right) \\ &= \Delta_t\,B_t\,x_t \\ \end{aligned}\]
L108: ### New Exponential-Trapezoidal Discretization
L109: 
L110: Thus, the linchpin of converting continuous-time SSMs into various tangible recurrences is approximating $\int_{\tau_{t-1}}^{\tau_t} \exp\left((\tau_t - \tau)A_t\right)B(\tau)x(\tau)d\tau$ in different ways. We’ve shown above that one can either analytically solve it (ZOH) or approximate it (Euler), but what if we don’t want to use inverses but also want something more precise than Euler’s?
--------------------------------------------------------------------------------
Verifying your browser | OpenReview (https://openreview.net/forum?id=Zu3B2TKOPV)
citeturn33066view2 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://openreview.net/forum?id=Zu3B2TKOPV","lineno":null}); Redirected to URL: https://openreview.net/challenge?redirect=/forum?id%3DZu3B2TKOPV; Total lines: 9

