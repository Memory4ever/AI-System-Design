Token Maturation: Autoregressive Language Generation via Continuous Token Dynamics (https://arxiv.org/html/2601.04854v1)
citeturn26862view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04854v1","lineno":40}); Total lines: 350
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:     1. cite7†Contributions. L18:   3. cite8†2 Related Work L19:     1. cite9†2.1 Autoregressive Decoding and Token Commitment L20:     2. cite10†2.2 Continuous Relaxations of Discrete Sampling L21:     3. cite11†2.3 Diffusion-Based Text Generation L22:     4. cite12†2.4 Contrastive Learning in Language Models L23:   4. cite13†3 Autoregressive token maturation L24:     1. cite14†3.1 Continuous Token Representation L25:     2. cite15†3.2 Autoregressive Vector Prediction L26:     3. cite16†3.3 Conditioning on Maturation State L27:       1. cite17†Noise-level conditioning. L28:       2. cite18†Tail-length conditioning. L29:     4. cite19†3.4 Token Maturation L30:     5. cite20†3.5 Discrete Commitment via Projection L31:     6. cite21†3.6 Training Objective L32:   5. cite22†4 Training and Generation L33:     1. cite23†4.1 Training with Simulated Maturation L34:       1. cite24†Loss weighting. L35:     2. cite25†4.2 Noise Injection and Stability L36:     3. cite26†4.3 Autoregressive Generation L37:       1. cite27†Classifier-free guidance. L38:     4. cite28†4.4 Generation Algorithm L39:     5. cite29†4.5 Computational Considerations L40:   6. cite30†5 Experiments L41:     1. cite31†5.1 Experimental Setup L42:     2. cite32†5.2 Coherent Generation without Entropy Collapse L43:     3. cite33†5.3 Tail Length Controls Diversity L44:     4. cite34†5.4 Embedding Geometry Adapts to Continuous Prediction L45:     5. cite35†5.5 Qualitative Examples L46:     6. cite36†5.6 Classifier-Free Guidance Reveals Interpretable Lookahead L47:   7. cite37†6 Discussion L48:     1. cite38†Decoupling prediction from commitment. L49:     2. cite39†Argmax does not imply greediness. L50:     3. cite40†Relation to diffusion-based language models. L51:     4. cite41†Training stability and representation collapse. L52:     5. cite42†Interpretability and internal dynamics. L53:     6. cite43†Limitations and future directions. L54:   8. cite44†7 Conclusion L55:   9. cite45†References L56:   10. cite46†A Appendix L57: cite47†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L58: 
L59: arXiv:2601.04854v1 [cs.CL] 08 Jan 2026
L60: # Token Maturation: Autoregressive Language Generation via Continuous Token Dynamics
L61: 
L62: Oshri Naparstek Affiliation: IBM Research, Haifa, Israel Correspondence to: oshri.naparstek@ibm.com
L63: ###### Abstract
L64: 
L65: Autoregressive language models are conventionally defined over discrete token sequences, committing to a specific token at every generation step. This early discretization forces uncertainty to be resolved through token-level sampling, often leading to instability, repetition, and sensitivity to decoding heuristics.
L66: In this work, we introduce a continuous autoregressive formulation of language generation in which tokens are represented as continuous vectors that mature over multiple update steps before being discretized. Rather than sampling tokens, the model evolves continuous token representations through a deterministic dynamical process, committing to a discrete token only when the representation has sufficiently converged.
L67: Discrete text is recovered via hard decoding, while uncertainty is maintained and resolved in the continuous space.
L68: We show that this maturation process alone is sufficient to produce coherent and diverse text using deterministic decoding (argmax), without reliance on token-level sampling, diffusion-style denoising, or auxiliary stabilization mechanisms. Additional perturbations, such as stochastic dynamics or history smoothing, can be incorporated naturally but are not required for the model to function.
L69: To our knowledge, this is the first autoregressive language model that generates text by evolving continuous token representations to convergence prior to discretization, enabling stable generation without token-level sampling.
L70: ###### Keywords:
L71: 
L72: autoregressive generation, continuous representations, delayed discretization, contrastive learning
L73: ## 1 Introduction
L74: 
L75: Autoregressive language models based on the Transformer architecture generate text by predicting a categorical distribution over tokens at each step (cite48†Vaswani et al., 2017 ). In modern implementations, this prediction is parameterized by a softmax over a fixed vocabulary, forcing the model to immediately commit to a discrete token via sampling or greedy selection. Once a token is selected, the decision becomes irreversible and fully conditions all subsequent generation.
L76: While effective in practice, this design enforces early discretization of uncertainty. Continuous structure present in the model’s internal representations is collapsed into a categorical choice at every step, and uncertainty must be handled indirectly through token-level sampling heuristics. This coupling between prediction and commitment limits the ways in which uncertainty can be expressed and manipulated during generation.
L77: In this work, we propose an alternative interface between prediction and commitment based on token maturation. Rather than committing to a discrete token at every generation step, we represent tokens as continuous vectors that evolve over time before discretization.
L78: Generation remains autoregressive and causal, but discretization is delayed: the model predicts trajectories in embedding space, allowing uncertainty to be represented geometrically and maintained throughout the maturation process until discrete commitment. A discrete token is committed only once the corresponding representation has sufficiently stabilized. Importantly, this final discretization step serves solely as an interface to the vocabulary and does not define the generative policy itself.
L79: Moreover, token maturation does not require a monotonic reduction in predictive entropy: discrete commitment can emerge even when entropy remains approximately constant throughout the maturation process.
L80: This formulation yields a model that is fully autoregressive yet fundamentally distinct from both standard probabilistic decoding and diffusion-based text generation. Unlike conventional autoregressive models, which discretize uncertainty at every step, token maturation maintains continuous uncertainty until commitment becomes unavoidable. Unlike diffusion models, which operate on entire sequences via global denoising, token maturation is local, causal, and incremental.
L81: As a result, uncertainty is handled within continuous dynamics rather than being collapsed prematurely into a token-level sampling decision. Figure cite49†1 contrasts immediate commitment with token maturation.
L82: A direct consequence of delayed discretization is the emergence of additional degrees of freedom during generation. Because token representations remain continuous prior to commitment, the model admits interventions that are ill-defined in standard discrete autoregressive models. These include injecting noise into historical token representations, applying temporal smoothing or exponential moving averages over past states, and perturbing intermediate trajectories without altering committed tokens.
L83: Such interventions act on the continuous dynamics rather than on the discrete sampling process and provide structured ways to explore and stabilize generation trajectories without requiring entropy collapse. While not required for correct generation, they are naturally supported by the proposed framework and provide mechanisms for controlling stability and diversity that are unavailable in purely discrete models.
L84: We study token maturation through a series of controlled experiments designed to isolate the effect of delayed discretization. We analyze the behavior of continuous token evolution under varying perturbation levels.
L85: cite50†Image: Refer to caption Figure 1: Immediate commitment vs. token maturation. (A) Standard autoregressive decoding commits to a discrete token at each step, making early decisions irreversible. (B) Token maturation maintains a continuous “liquid tail” of token representations that evolve over time; discretization is deferred to a final commitment step.
L86: #### Contributions.
L87: 
L88: The main contributions of this work are:
L89: 
L90:   * •
L91: 
L92: We introduce token maturation, a continuous-variable, autoregressive language generation framework with delayed discretization.
L93: 
L94:   * •
L95: 
L96: We show that delayed discretization enables well-defined interventions on continuous token histories, such as noise injection and temporal smoothing, which are not naturally expressible in standard discrete autoregressive models.
L97: 
L98:   * •
L99: We provide a mechanistic analysis of uncertainty resolution in continuous token space, identifying stable and collapse regimes under controlled perturbations.
L100: 
L101:   * •
L102: 
L103: We demonstrate a minimal instantiation using a GPT-2 backbone, confirming the feasibility of autoregressive language generation without softmax-based decoding.
L104: ## 2 Related Work
L105: ### 2.1 Autoregressive Decoding and Token Commitment
L106: Autoregressive language models typically generate text by predicting a categorical distribution over a fixed vocabulary at each step, followed by immediate commitment to a single token via greedy decoding or stochastic sampling (cite48†Vaswani et al., 2017 ; cite51†Radford et al., 2019 ). A large body of work has focused on improving this decision step through alternative decoding strategies, including beam search, top-$k$ sampling, and nucleus sampling (cite52†Holtzman et al., 2019 ).
L107: Despite their differences, these methods share a common assumption: uncertainty is represented discretely and resolved instantaneously at every generation step.
L108: Recent efforts such as speculative decoding aim to accelerate this process by leveraging auxiliary models, but still rely on the same immediate token commitment paradigm (cite53†Leviathan et al., 2023 ). In contrast, our work does not modify the sampling policy over discrete distributions, but instead revisits the interface between prediction and commitment by delaying discretization altogether.
L109: ### 2.2 Continuous Relaxations of Discrete Sampling
L110: Several methods have proposed continuous relaxations of discrete random variables in order to enable gradient-based optimization. Notable examples include the Gumbel-Softmax and straight-through estimators, which provide differentiable approximations to categorical sampling (cite54†Jang et al., 2016 ; cite55†Maddison et al., 2016 ). These techniques soften the decision process during training, but at inference time still require sampling or selecting a discrete token at each step.
L111: From a generative perspective, such relaxations operate at the level of individual decisions rather than modeling token evolution over time. In contrast, token maturation treats token representations as continuous trajectories whose uncertainty is resolved dynamically, with discretization deferred to a final commitment step rather than approximated during optimization.
L112: ### 2.3 Diffusion-Based Text Generation
L113: 
L114: Diffusion-based approaches to text generation can be broadly divided into two families. The first operates directly in discrete token space via iterative masking and re-masking procedures, refining entire sequences through repeated probabilistic updates (cite56†Lou et al., 2023 ; cite57†Nie et al., 2025 ). While effective for parallel generation, these models are inherently non-autoregressive and do not impose a causal left-to-right structure.
L115: A second family performs diffusion or flow-based modeling in continuous spaces, such as embeddings or latent representations, using global denoising dynamics to generate text (cite58†Hoogeboom et al., 2021 ; cite59†Li et al., 2022 ). Although these models employ continuous representations, generation typically proceeds through global refinement of complete sequences rather than local, causal token evolution.
L116: In contrast to both families, token maturation defines a fully autoregressive and causal process in which uncertainty is resolved locally over time for each token. No global denoising or iterative re-masking is performed, and discretization semantics differ fundamentally from diffusion-based formulations.
L117: ### 2.4 Contrastive Learning in Language Models
L118: 
L119: Contrastive objectives such as InfoNCE have been widely used to learn high-quality representations in language models, particularly for sentence embeddings, retrieval, and multimodal alignment (cite60†Chen et al., 2020 ; cite61†Gao et al., 2021 ). In these settings, contrastive learning serves as an auxiliary objective that improves representation quality, rather than a mechanism for generative modeling.
L120: More recently, contrastive signals have been incorporated into language model training for alignment or preference learning, but not as a replacement for likelihood-based generation. In our setting, contrastive learning plays a fundamentally different role: it is essential for stabilizing autoregressive generation in the absence of a categorical likelihood.
L121: Specifically, the contrastive objective prevents regression-to-the-mean collapse and aligns continuous predictions with the eventual discretization step, a use case that has received little attention in prior work.
L122: ## 3 Autoregressive token maturation
L123: 
L124: We introduce a continuous-variable formulation of autoregressive language modeling in which tokens are represented and generated as vectors in embedding space, and discrete commitment is deferred through a process we refer to as token maturation. This section formalizes the representation, generation dynamics, and training objective underlying the proposed framework.
L125: ### 3.1 Continuous Token Representation
L126: 
L127: Let $\mathcal{V}$ denote a discrete vocabulary of size $|\mathcal{V}|$, and let $E\in\mathbb{R}^{|\mathcal{V}|\times d}$ be a fixed embedding matrix, where each row $e_{i}\in\mathbb{R}^{d}$ corresponds to a token embedding. We assume embeddings are $\ell_{2}$-normalized and scaled to a fixed radius $R$.
L128: Rather than predicting a categorical distribution over $\mathcal{V}$, the model predicts continuous vectors $z_{t}\in\mathbb{R}^{d}$ at each position $t$. Discrete tokens are recovered only at commitment time by projecting continuous vectors onto the vocabulary embedding set.
L129: ### 3.2 Autoregressive Vector Prediction
L130: 
L131: Given a sequence of previously committed token vectors $\{z_{1},\dots,z_{t-1}\}$, the model predicts a continuous vector $\hat{z}_{t}$ via an autoregressive function
L132: 
L133:  | $$\hat{z}_{t}=f_{\theta}(z_{1},\dots,z_{t-1}),$$  |  | (1)
L134: 
L135: where $f_{\theta}$ is implemented as a causal Transformer operating directly in embedding space. Importantly, $\hat{z}_{t}$ is not immediately discretized and may evolve over time before commitment.
L136: ### 3.3 Conditioning on Maturation State
L137: 
L138: To enable the model to behave appropriately at different stages of the maturation process, we condition on two quantities: the noise level $\alpha$ at each position, and the tail length $K$.
L139: #### Noise-level conditioning.
L140: 
L141: Each position in the sequence is associated with a noise level $\alpha_{t}\in[0,1]$, indicating how corrupted or uncertain the corresponding vector is. We embed $\alpha_{t}$ using a sinusoidal positional encoding (as in diffusion models) followed by a learned MLP, and add the result to the token representation:
L142: 
L143:  | $$h_{t}\leftarrow h_{t}+\mathrm{MLP}(\mathrm{SinEmb}(\alpha_{t})).$$  |  | (2)
L144: This allows the model to distinguish between committed tokens ($\alpha\approx 1$) and uncertain tail tokens ($\alpha\approx 0$).
L145: #### Tail-length conditioning.
L146: 
L147: We further condition the model on the current tail length $K$ via feature-wise linear modulation (FiLM). A learned embedding of $K$ is projected to produce scale and shift parameters $(\gamma,\beta)$, which modulate the hidden representations:
L148: 
L149:  | $$h\leftarrow(1+\gamma)\odot h+\beta.$$  |  | (3)
L150: 
L151: This global conditioning allows the model to adjust its predictions based on how much context is committed versus uncertain.
L152: ### 3.4 Token Maturation
L153: 
L154: To decouple prediction from commitment, we maintain a maturation buffer of length $K$, referred to as the liquid tail. At any generation step, the model maintains a sequence
L155: 
L156:  | $$(z_{1},\dots,z_{t-K},\tilde{z}_{t-K+1},\dots,\tilde{z}_{t}),$$  |
L157: 
L158: where the final $K$ vectors are uncommitted and continuously updated.
L159: 
L160: At each step, predicted vectors are iteratively refined according to
L161: 
L162:  | $$\tilde{z}_{i}\leftarrow\tilde{z}_{i}+\alpha_{i}(\hat{z}_{i}-\tilde{z}_{i}),$$  |  | (4)
L163: where $\alpha_{i}\in(0,1]$ controls the maturation rate. Earlier positions in the tail are updated more aggressively, while newly introduced vectors evolve slowly, resulting in gradual stabilization over time.
L164: 
L165: This process allows uncertainty to be expressed geometrically as distance in embedding space and resolved incrementally rather than through instantaneous sampling.
L166: ### 3.5 Discrete Commitment via Projection
L167: 
L168: Once a token vector reaches the front of the maturation buffer, it is committed by projection onto the embedding matrix:
L169: 
L170:  | $$x_{t}=\arg\max_{i\in\mathcal{V}}\langle z_{t},e_{i}\rangle.$$  |  | (5)
L171: The committed vector is then replaced by its corresponding embedding $e_{x_{t}}$ and becomes part of the fixed autoregressive context. Although commitment uses an argmax operation, stochasticity arises implicitly through the continuous maturation dynamics rather than explicit sampling.
L172: ### 3.6 Training Objective
L173: 
L174: A pure regression objective on continuous vectors leads to mode averaging and collapse. To stabilize training and align continuous predictions with discrete token identity, we combine a mean-squared error objective with a contrastive loss.
L175: 
L176: Given a predicted vector $\hat{z}_{t}$ and its ground-truth embedding $e_{x_{t}}$, we minimize
L177: 
L178:  | $$\mathcal{L}_{\text{reg}}=\|\hat{z}_{t}-e_{x_{t}}\|_{2}^{2},$$  |  | (6)
L179: 
L180: alongside a contrastive InfoNCE loss
L181:  | $$\mathcal{L}_{\text{NCE}}=-\log\frac{\exp(\langle\hat{z}_{t},e_{x_{t}}\rangle/\tau)}{\sum_{j\in\mathcal{N}}\exp(\langle\hat{z}_{t},e_{j}\rangle/\tau)},$$  |  | (7)
L182: 
L183: where $\mathcal{N}$ is a set of negative samples and $\tau$ is a temperature parameter.
L184: 
L185: The final training objective is
L186: 
L187:  | $$\mathcal{L}=\mathcal{L}_{\text{reg}}+\lambda\mathcal{L}_{\text{NCE}}.$$  |  | (8)
L188: This contrastive component prevents collapse toward frequent tokens and anchors continuous predictions to discrete semantic identities without requiring a softmax likelihood.
L189: ## 4 Training and Generation
L190: 
L191: This section describes how the proposed model is trained and how autoregressive generation is performed at inference time. Although training and generation operate under different constraints, both are governed by the same underlying token maturation dynamics.
L192: ### 4.1 Training with Simulated Maturation
L193: 
L194: During training, the model is exposed to partially matured token representations to encourage robustness to uncertainty and to align training dynamics with inference-time behavior. Given a ground-truth token sequence $(x_{1},\dots,x_{T})$, we first map tokens to their embedding representations $(e_{x_{1}},\dots,e_{x_{T}})$.
L195: To simulate the presence of a liquid tail, we perturb a suffix of length $K$ by mixing the ground-truth embeddings with isotropic noise in embedding space. Earlier tokens remain fixed, while later tokens are progressively corrupted, mimicking different stages of maturation. This procedure exposes the model to inputs ranging from fully committed tokens to highly uncertain representations.
L196: The model is trained to predict the next-step continuous vector $\hat{z}_{t+1}$ given the current sequence of committed and uncommitted vectors, using the combined regression and contrastive objective described in Section cite13†3 .
L197: #### Loss weighting.
L198: 
L199: To prevent the model from overweighting highly corrupted positions where the target is inherently ambiguous, we weight the loss at each position by $(1-\alpha_{t})$, where $\alpha_{t}$ is the noise level. Positions with low noise (near commitment) contribute more to the gradient, while highly uncertain positions contribute less.
L200: ### 4.2 Noise Injection and Stability
L201: 
L202: Noise injection during training serves two complementary purposes. First, it regularizes the model by preventing over-reliance on exact embedding vectors. Second, it approximates the distribution of uncommitted token states encountered during generation.
L203: Importantly, noise is bounded and scaled such that vector norms evolve gradually over time. This ensures that uncertainty is resolved through maturation rather than abrupt stochastic jumps, and avoids the training–inference mismatch commonly encountered when noise is injected only at sampling time.
L204: ### 4.3 Autoregressive Generation
L205: 
L206: At inference time, generation proceeds autoregressively from left to right. Given an initial prompt, the corresponding token embeddings are inserted into the sequence as committed vectors. A liquid tail of length $K$ is initialized with low-norm random vectors, representing highly uncertain token states.
L207: At each generation step, the model predicts updated continuous vectors for the entire sequence. Vectors in the liquid tail are updated according to the maturation rule, while committed tokens remain fixed. Once a vector reaches the front of the liquid tail, it is discretized via projection onto the vocabulary embedding matrix and committed permanently.
L208: 
L209: This process yields a stream of discrete tokens, while internally maintaining a continuous representation that evolves over time.
L210: #### Classifier-free guidance.
L211: 
L212: At inference time, we optionally apply classifier-free guidance (CFG) to sharpen predictions toward the conditioned context. We compute two forward passes: a conditional pass using the full causal mask, and an unconditional pass using a tail-only mask that prevents tail tokens from attending to history. The final prediction is a weighted combination:
L213: 
L214:  | $$\hat{z}_{t}=\hat{z}_{t}^{\text{uncond}}+s\cdot(\hat{z}_{t}^{\text{cond}}-\hat{z}_{t}^{\text{uncond}}),$$  |  | (9)
L215: where $s\geq 1$ is the guidance scale. This encourages generated tokens to be more consistent with the committed context.
L216: ### 4.4 Generation Algorithm
L217: 
L218: Algorithm cite62†1 summarizes the proposed autoregressive generation procedure.
L219: 
L220: Algorithm 1 Autoregressive Generation with Token Maturation
L221: 
L222: 0:  Prompt embeddings $(e_{x_{1}},\dots,e_{x_{n}})$, tail length $K$, guidance scale $s$
L223: 
L224: 1:  Initialize committed sequence $\mathbf{z}_{1:n}\leftarrow(e_{x_{1}},\dots,e_{x_{n}})$
L225: 
L226: 2:  Initialize liquid tail $\tilde{\mathbf{z}}_{n+1:n+K}$ with random low-norm vectors
L227: 3:  Construct alpha profile: $\alpha_{t}=1$ for $t\leq n$, fading from $\alpha_{\max}$ to $0$ over tail
L228: 
L229: 4:  while not end-of-sequence do
L230: 
L231: 5:   $\hat{\mathbf{z}}^{\text{cond}}\leftarrow f_{\theta}(\mathbf{z},\boldsymbol{\alpha},K)$ {full causal mask}
L232: 
L233: 6:   $\hat{\mathbf{z}}^{\text{uncond}}\leftarrow f_{\theta}(\mathbf{z},\boldsymbol{\alpha},K)$ {tail-only mask}
L234: 
L235: 7:   $\hat{\mathbf{z}}\leftarrow\hat{\mathbf{z}}^{\text{uncond}}+s\cdot(\hat{\mathbf{z}}^{\text{cond}}-\hat{\mathbf{z}}^{\text{uncond}})$ {CFG}
L236: 8:   Update tail: $\tilde{z}_{i}\leftarrow\tilde{z}_{i}+\alpha_{i}(\hat{z}_{i}-\tilde{z}_{i})$ for $i$ in tail
L237: 
L238: 9:   Commit front token: $x_{n+1}\leftarrow\arg\max_{j}\langle\tilde{z}_{n+1},e_{j}\rangle$
L239: 
L240: 10:   Replace: $z_{n+1}\leftarrow e_{x_{n+1}}$, append new embryo to tail
L241: 
L242: 11:   $n\leftarrow n+1$, update $\boldsymbol{\alpha}$
L243: 
L244: 12:  end while
L245: 
L246: 13:  return Generated token sequence $(x_{1},\dots,x_{n})$
L247: ### 4.5 Computational Considerations
L248: 
L249: The proposed framework introduces minimal overhead relative to standard autoregressive generation. The primary additional cost arises from maintaining and updating the liquid tail, which scales linearly with the tail length $K$. In practice, we find small values of $K$ sufficient to capture maturation dynamics, keeping inference costs comparable to conventional decoding methods.
L250: ## 5 Experiments
L251: 
L252: We evaluate token maturation through experiments designed to validate its core claims: that coherent text can be generated without entropy collapse, that tail length controls diversity, and that learned embeddings adapt to the continuous prediction task.
L253: ### 5.1 Experimental Setup
L254: We train a 24-layer causal Transformer with hidden dimension 1024 and 16 attention heads, operating directly in embedding space. The model is trained on the FineWeb-10BT dataset (penedo2024fineweb) for 600K steps with batch size 8 and gradient accumulation over 4 steps, yielding an effective batch size of 32. Token embeddings are initialized from GPT-2 and optionally fine-tuned during training.
L255: We use the combined MSE + InfoNCE objective described in Section cite13†3 , with 256 negative samples and a logit scale of 20.
L256: Unless otherwise specified, we use a liquid tail of length $K=16$ during generation. All experiments use deterministic decoding (argmax) without temperature scaling or nucleus sampling.
L257: ### 5.2 Coherent Generation without Entropy Collapse
L258: 
L259: A central prediction of our framework is that discrete commitment can occur without a corresponding reduction in predictive entropy. To test this, we track the entropy of the model’s implicit distribution over vocabulary tokens throughout the maturation process.
L260: At each maturation step, we compute the cosine similarity between the current vector and all vocabulary embeddings, apply a softmax with temperature $\tau=1$, and measure the resulting entropy.
L261: Figure cite63†2 shows entropy trajectories for representative generation runs. Contrary to the expectation that commitment requires certainty, we observe that entropy remains approximately constant ($H\approx 3.9$ nats) throughout maturation, decreasing only marginally before the final snap. Despite this sustained uncertainty, generated text is syntactically coherent and topically consistent.
L262: This finding supports our central claim: the model converges not to a single token, but to a region in embedding space where multiple semantically appropriate tokens reside at similar distances. Commitment emerges from geometric proximity rather than probability concentration.
L263: cite64†Image: Refer to caption Figure 2: Left: Entropy throughout token maturation for four representative tokens. Despite progressing through 24 maturation steps, entropy remains constant at approximately 3.9 nats—the model never collapses to certainty before commitment. Right: Top candidate for token “Dr” at each step, showing exploration through semantically diverse alternatives despite constant entropy. This demonstrates that commitment emerges from geometric convergence, not probability concentration.
L264: ### 5.3 Tail Length Controls Diversity
L265: 
L266: The liquid tail length $K$ determines how many maturation steps each token undergoes before commitment. We hypothesize that shorter tails preserve more of the initial randomness, yielding diverse outputs, while longer tails allow convergence toward a deterministic trajectory.
L267: To test this, we generate 50 continuations from the same prompt under varying tail lengths ($K\in\{1,4,16,64\}$), using identical model weights but different random initializations for the tail.
L268: ### 5.4 Embedding Geometry Adapts to Continuous Prediction
L269: 
L270: When embeddings are fine-tuned during training, we observe systematic reorganization of the embedding space. Figure cite65†3 visualizes the drift between frozen GPT-2 embeddings and learned embeddings after 600K training steps.
L271: 
L272: Several patterns emerge:
L273: 
L274:   * •
L275: 
L276: Stable tokens: Years (1978, 1987, 1992) and common function words exhibit minimal drift, suggesting GPT-2’s geometry is already suitable for these tokens.
L277: 
L278:   * •
L279: High-drift tokens: Punctuation, Unicode symbols, and rare code fragments drift substantially, indicating that the original embeddings poorly served continuous prediction for these tokens.
L280: 
L281:   * •
L282: 
L283: Semantic reorganization: Nearest-neighbor relationships shift in interpretable ways. For instance, “Python” moves from proximity to other programming languages (Java, PHP) toward proximity to programming culture tokens (Lisp, Emacs, Unix).
L284: This reorganization occurs without explicit supervision on embedding structure, emerging purely from the continuous prediction objective.
L285: 
L286: cite66†Image: Refer to caption Figure 3: Embedding drift from frozen GPT-2 to learned embeddings. Left: distribution of drift across vocabulary. Right: tokens with highest drift are predominantly punctuation and rare symbols.
L287: ### 5.5 Qualitative Examples
L288: 
L289: Figure cite67†4 shows representative generation samples with the liquid tail visualized. blue tokens indicate pre-commitment states. We observe that tokens often remain ambiguous up to the commitment stage.
L290: cite68†Image: Refer to caption Figure 4: Generation interface showing token maturation in action. Left: Committed text (white) followed by the liquid tail (cyan) containing uncommitted tokens that will mature over subsequent steps. Bottom: Live metrics including entropy ($H=3.91$), confirming sustained uncertainty. Right: Top candidates for the next commitment, showing near-uniform scores over semantically appropriate alternatives (psychology, professor, psychiatrist, neuro).
L291: Despite high entropy, all candidates are contextually relevant—the model converges to a semantic region rather than a single token.
L292: ### 5.6 Classifier-Free Guidance Reveals Interpretable Lookahead
L293: 
L294: Classifier-free guidance (CFG) interpolates between conditional and unconditional predictions, typically used to sharpen generation toward the prompt. In our framework, CFG has an additional effect: it pulls uncommitted tail vectors toward the manifold of coherent text, making intermediate states semantically interpretable.
L295: Figure cite69†5 compares tail states with and without CFG ($s=1$ vs. $s=2$). Without guidance, tail tokens project to seemingly random vocabulary items with no coherent relationship to the context or to each other. With guidance, tail tokens form interpretable sequences that reflect forward planning: topics, syntactic continuations, and semantic themes become visible before commitment.
L296: This suggests that CFG does not merely sharpen final predictions, but actively shapes the geometry of the maturation trajectory. The liquid tail becomes a window into the model’s latent “reasoning”—a form of interpretable lookahead that is unavailable in standard autoregressive generation.
L297: cite70†Image: Refer to caption Figure 5: Effect of CFG on tail interpretability. Without CFG (top), tail tokens appear as incoherent noise. With CFG (bottom), tail tokens form semantically meaningful lookahead, revealing the model’s implicit forward planning.
L298: ## 6 Discussion
L299: #### Decoupling prediction from commitment.
L300: The central contribution of this work is not a new sampling heuristic, but a reformulation of autoregressive language generation in which prediction and commitment are explicitly separated. Standard language models collapse uncertainty into a discrete decision at each generation step via softmax-based sampling. In contrast, token maturation allows uncertainty to be expressed and resolved within a continuous embedding space before any discrete commitment is made.
L301: This decoupling enables the model to represent intermediate, partially-formed token states that evolve over time.
L302: #### Argmax does not imply greediness.
L303: A common interpretation is that argmax-based decoding is inherently greedy. Our results challenge this view. When argmax is applied after stochastic evolution in embedding space, it plays a role analogous to the Gumbel-max trick (cite54†Jang et al., 2016 ): noise injected into the dynamics propagates to the final decision, making the overall process stochastic despite a deterministic final step.
L304: The crucial difference is that noise acts on continuous trajectories rather than on discrete logits, allowing uncertainty to be shaped by geometric structure rather than by additive perturbation.
L305: #### Relation to diffusion-based language models.
L306: Recent work on diffusion-based language modeling explores both discrete masking schemes and continuous latent trajectories. While these approaches share the goal of avoiding immediate categorical decisions, they differ fundamentally from the present framework. Diffusion language models are typically non-autoregressive and operate over entire sequences or spans, whereas token maturation is inherently autoregressive.
L307: Each token evolves independently over time and is committed before the next token is generated. This preserves the causal structure and incremental generation properties of standard language models while introducing a continuous intermediate state.
L308: #### Training stability and representation collapse.
L309: An important practical observation is the role of contrastive objectives, such as InfoNCE, in preventing collapse toward degenerate embedding averages. Without such objectives, regression-based training in embedding space tends to produce overly smooth or repetitive outputs. This suggests that learning a meaningful continuous token manifold requires explicit pressure to preserve discriminative structure, even when final generation involves discretization.
L310: #### Interpretability and internal dynamics.

