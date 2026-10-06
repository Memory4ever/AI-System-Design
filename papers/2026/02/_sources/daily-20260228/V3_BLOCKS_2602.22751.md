[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Know What You Know: Metacognitive Entropy Calibration for Verifiable RL Reasoning

[3] h6: Abstract.

[4] p: Large reasoning models (LRMs) have emerged as a powerful paradigm for solving complex real-world tasks. In practice, these models are predominantly trained via Reinforcement Learning with Verifiable Rewards (RLVR), yet most existing outcome-only RLVR pipelines rely almost exclusively on a binary correctness signal and largely ignore the model’s intrinsic uncertainty. We term this discrepancy the uncertainty–reward mismatch, under which high- and low-uncertainty solutions are treated equivalently, preventing the policy from “Know What You Know” and impeding the shift from optimizing for correct answers to optimizing effective reasoning paths. This limitation is especially critical in reasoning-centric tasks such as mathematics and question answering, where performance hinges on the quality of the model’s internal reasoning process rather than mere memorization of final answers. To address this, we propose EGPO, a metacognitive entropy calibration framework that explicitly integrates intrinsic uncertainty into RLVR for enhancing LRMs. EGPO estimates per-sample uncertainty using a zero-overhead entropy proxy derived from token-level likelihoods and aligns it with extrinsic correctness through an asymmetric calibration mechanism that preserves correct reasoning while selectively regulating overconfident failures, thereby enabling stable and uncertainty-aware policy optimization. Moreover, EGPO recovers informative learning signals from otherwise degenerate group-based rollouts without modifying the verifier or reward definition. Extensive experiments across multiple benchmarks demonstrate that the proposed EGPO leads to substantial and consistent improvements in reasoning performance, establishing a principled path for advancing LRMs through metacognitive entropy calibration.

[5] h6: Keywords:

[6] h2: 1. Introduction

[7] p: Large reasoning models (LRMs) have demonstrated remarkable capabilities in tackling complex tasks, ranging from mathematical problem solving ( DeepSeek-AI et al., 2025 ; Jaech et al., 2024 ; Shao et al., 2024 ) to agentic decision-making ( Wu et al., 2025 ; Chen et al., 2025 ) . Representative systems such as DeepSeek-R1 ( DeepSeek-AI et al., 2025 ) and OpenAI o1 ( Jaech et al., 2024 ) achieve remarkable performance on rigorous reasoning benchmarks, highlighting the pivotal role of explicit reasoning in modern large language models (LLMs). A key mechanism behind these advances is Reinforcement Learning with Verifiable Rewards (RLVR) ( Lightman et al., 2023 ; Shao et al., 2024 ; Chen et al., 2026 ; Liu et al., 2025a ) , a post-training paradigm that substitutes subjective preference annotations with programmatic verifiers that return a binary reward signal based on objective correctness.

[8] p: The fundamental principle of this paradigm, exemplified by Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) , is to sample multiple rollouts for a single prompt and optimize the policy using group-relative advantages derived from within-group comparisons. However, this reliance on intra-group contrast constitutes a significant bottleneck: if a sampled group consists entirely of correct or entirely incorrect responses (i.e., uniform rewards), the relative advantages vanish, resulting in ineffective zero-gradient updates. To mitigate this limitation, recent research has pursued three primary directions. The first focuses on data efficiency by prioritizing prompts that yield a mixture of correct and incorrect responses, as seen in DAPO ( Yu et al., 2025 ) . The second line of work refines advantage estimation to produce more stable update signals, exemplified by Dr.GRPO ( Liu et al., 2025b ) , DRA-GRPO ( Chen et al., 2026 ) , and GSPO ( Zheng et al., 2025 ) . The third direction enhances exploration to prevent groups from converging to uniformly correct or incorrect states, as proposed in ERPO ( Liu et al., 2025c ) .

[9] p: Despite these improvements, existing outcome-only verifiers in RLVR provide a coarse, binary correctness signal while largely neglecting the LRM’s intrinsic uncertainty, namely its internal estimate of confidence during generation. We term this discrepancy the uncertainty–reward mismatch , which prevents the policy from learning how uncertainty should meaningfully guide its reasoning behavior. To explicate this limitation, we categorize outcomes along the joint axes of correctness and uncertainty, yielding two broad classes of learning states. Success states correspond to correct solutions and comprise low-uncertainty correct, where the model is well-calibrated and truly knows the answer, and high-uncertainty correct, where the answer is correct but reached hesitantly or via fragile reasoning. Error states correspond to incorrect solutions and comprise low-uncertainty incorrect, akin to a hallucination that reflects a stable misconception, and high-uncertainty incorrect, which typically reflects exploratory attempts. Consequently, this mismatch exposes two fundamental deficiencies. First, it blurs the boundary between consolidating knowledge and preserving exploration. Because binary outcome rewards treat success states as equally desirable, while penalizing error states solutions in the same way, the model cannot reliably decide when to reinforce stable reasoning patterns versus when to sustain exploratory search. Second, it fails to extract meaningful learning signals from hard problems, particularly in entirely incorrect groups, where group-relative objectives collapse to zero gradients, forcing practitioners to either filter these hardest cases or inject additional supervision, thereby wasting valuable training signal.

[10] p: Advancing the reasoning frontier of LLMs requires an RLVR training process that explicitly accounts for the policy’s intrinsic uncertainty, which can be quantified by the dispersion of its output distribution. EDGE-GRPO ( Zhang et al., 2025 ) is an early attempt in this direction that leverages Shannon entropy ( Shannon, 1948 ) to modulate update magnitude, but it relies solely on entropy for reweighting, such that correct and incorrect trajectories may receive comparably scaled updates. This makes it difficult to both consolidate correct reasoning and preserve exploration, as overly aggressive updates on failures can inadvertently suppress exploratory attempts. Moreover, injecting external supervision (e.g., ground-truth answers) to generate corrective rollouts for entirely incorrect groups departs from outcome-only RLVR and may introduce unstable learning signals when the policy is weak, such as cases where the final answer is correct but the reasoning trajectory remains flawed. Consequently, the central challenge in incorporating uncertainty into RLVR is to establish a principled mechanism that strengthens correct reasoning while still extracting meaningful learning signals from incorrect samples without suppression of exploration.

[11] p: Inspired by metacognition ( Martinez, 2006 ) , the human capacity to monitor internal uncertainty and regulate learning accordingly, we argue that uncertainty should play a central role in RLVR optimization. Intuitively, humans strongly reinforce solutions reached with high certainty, retain uncertain successes as promising directions for further refinement, and avoid overly penalizing uncertain failures that reflect exploratory reasoning. Translating this principle to RLVR, uncertainty should serve as a modulating signal for policy updates. For success states, it reflects evidential strength and determines the degree of knowledge consolidation. For error states, it acts as a damping factor that tempers updates, enabling the model to learn from failures while preserving exploratory behavior essential for discovering improved reasoning strategies.

[12] figure: Figure 1 . Overview of EGPO: sample-level metacognitive calibration (four quadrants) and group-level rollout triage (entirely-correct / mixed (contains both correct and incorrect outcomes) / entirely-incorrect).

[13] p: To this end, we propose EGPO, a lightweight E ntropy- G uided P olicy O ptimization for RLVR that injects metacognitive calibration without changing the binary outcome reward. Instead of redesigning rewards, EGPO rescales the advantage magnitude using an intrinsic uncertainty proxy derived from the policy itself. Specifically, within each group we estimate per-sample uncertainty via sequence negative log-likelihood (NLL) ( Shannon, 1948 ) , a cheap statistic directly tied to the policy’s token log-probabilities, and normalize it into a group-level uncertainty weight so that the overall step size remains scale-preserving while credit is redistributed within the group. We further adopt an asymmetric calibration rule: correct trajectories are never down-weighted while incorrect trajectories are never up-weighted , whereas incorrect trajectories are never up-weighted, which improves stability under sparse binary rewards. Moreover, when all rollouts in a group are incorrect and GRPO yields zero advantage, EGPO applies entropy-damped negative sample reinforcement (NSR) ( Zhu et al., 2025 ) to recover a non-zero learning signal while still preserving exploratory behavior. We summarize our main contributions as follows:

[14] p: We identify a fundamental uncertainty–reward mismatch in outcome-only RLVR, where binary correctness signals are misaligned with the policy’s intrinsic uncertainty, leading to flawed credit assignment and wasted learning signals on hard problems. To address this, we frame the issue from a metacognitive perspective, arguing that effective RLVR should jointly consider correctness and uncertainty rather than optimizing answers alone.

[15] p: We propose EGPO, a lightweight verifier-agnostic training algorithm for RLVR that integrates metacognitive entropy calibration into group-based optimization. EGPO rescales advantage magnitudes using a token-level entropy proxy and applies an asymmetric calibration rule, while recovering learning signals from entirely incorrect groups via entropy-damped negative sample reinforcement, thereby providing a more principled and stable training strategy.

[16] p: Extensive experiments across multiple in-domain and out-of-distribution reasoning benchmarks demonstrate that EGPO consistently outperforms strong RLVR baselines, validating both its effectiveness and its robust generalization ability across models and tasks.

[17] h2: 2. Preliminaries

[18] h3: 2.1. Problem Setup

[19] h4: 2.1.1. Reinforcement Learning with Verifiable Rewards (RLVR)

[20] p: RLVR studies policy optimization where reward is provided by a programmatic verifier rather than human preference ( Lightman et al., 2023 ; Shao et al., 2024 ) . We sample a problem instance ( x , g ) ∼ 𝒟 (x,g)\sim\mathcal{D} , where x x is the prompt, g g is the ground truth and 𝒟 \mathcal{D} is the training dataset. A policy π θ ( ⋅ ∣ x ) \pi_{\theta}(\cdot\mid x) generates a response y ∼ π θ ( ⋅ ∣ x ) y\sim\pi_{\theta}(\cdot\mid x) , and a verifier V V checks correctness using only the final answer extracted from y y . Let Ans ⁡ ( y ) \mathrm{Ans}(y) denote the extracted final answer. The outcome reward is defined as

[21] table: (1) r ⁡ ( y ) = { + 1 , Ans ⁡ ( y ) = g , − 1 , otherwise . r(y)=\begin{cases}+1,&\mathrm{Ans}(y)=g,\\ -1,&\text{otherwise}.\end{cases}

[22] p: Thus, outcome-only RLVR supervises the policy only through final-answer correctness relative to g g , and does not directly score intermediate reasoning tokens.

[23] p: In verifiable math and logic tasks, we follow the standard MATH evaluation protocol ( Hendrycks et al., 2021b ; Hendrycks et al., 2021c ) by prompting the model to reason step by step and to place the final answer within \boxed . Accordingly, Ans ⁡ ( y ) \mathrm{Ans}(y) extracts the content inside the last \boxed in y y .

[24] h4: 2.1.2. Group Relative Policy Optimization (GRPO)

[25] p: Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) is a group-based policy optimization method widely used in outcome-only RLVR. For a problem instance ( x , g ) ∼ 𝒟 (x,g)\sim\mathcal{D} , we sample a group of N N responses { y i } i = 1 N \{y_{i}\}_{i=1}^{N} from an old policy π θ old ( ⋅ ∣ x ) \pi_{\theta_{\text{old}}}(\cdot\mid x) and obtain outcome rewards { r i } i = 1 N \{r_{i}\}_{i=1}^{N} via Eq. ( 1 ), forming one group 𝒢 ⁡ ( x ) = { ( x , y i , r i ) } i = 1 N \mathcal{G}(x)=\{(x,y_{i},r_{i})\}_{i=1}^{N} . GRPO constructs a group-relative advantage by normalizing outcome rewards within the group:

[26] table: (2) A i = r i − mean ⁡ ( r 1 , … , r N ) std ⁡ ( r 1 , … , r N ) . A_{i}\;=\;\frac{r_{i}-\mathrm{mean}(r_{1},\ldots,r_{N})}{\mathrm{std}(r_{1},\ldots,r_{N})}.

[27] p: Let π θ \pi_{\theta} denote the current policy. GRPO updates π θ \pi_{\theta} by maximizing a clipped ratio objective:

[28] table: (3) ℒ GRPO ​ ( θ ) = 𝔼 ⁡ [ min ⁡ ( ρ i ​ ( θ ) ​ A i , clip ⁡ ( ρ i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A i ) ] , \mathcal{L}_{\mathrm{GRPO}}(\theta)=\mathbb{E}\Big[\min\big(\rho_{i}(\theta)\,A_{i},\;\mathrm{clip}(\rho_{i}(\theta),1-\epsilon,1+\epsilon)\,A_{i}\big)\Big],

[29] p: where the expectation is over ( x , g ) ∼ 𝒟 (x,g)\sim\mathcal{D} and groups { y i } i = 1 N \{y_{i}\}_{i=1}^{N} sampled from π θ old ( ⋅ ∣ x ) \pi_{\theta_{\text{old}}}(\cdot\mid x) , ϵ \epsilon is the clipping coefficient, and

[30] table: (4) ρ i ​ ( θ ) = π θ ​ ( y i ∣ x ) π θ old ​ ( y i ∣ x ) . \rho_{i}(\theta)\;=\;\frac{\pi_{\theta}(y_{i}\mid x)}{\pi_{\theta_{\text{old}}}(y_{i}\mid x)}.

[31] h5: Advantage collapse.

[32] p: With outcome rewards r i ∈ { − 1 , + 1 } r_{i}\in\{-1,+1\} , a group can be mixed ( ∃ i , j : r i ≠ r j \exists\,i,j:\ r_{i}\neq r_{j} ), entirely-correct ( ∀ i , r i = + 1 \forall i,\ r_{i}=+1 ), or entirely-incorrect ( ∀ i , r i = − 1 \forall i,\ r_{i}=-1 ). In the latter two cases, the group provides no within-group preference structure: r i = mean ⁡ ( r 1 , … , r N ) r_{i}=\mathrm{mean}(r_{1},\ldots,r_{N}) for all i i . Then Eq. ( 2 ) is undefined due to zero standard deviation, and in practice implementations set A i ≡ 0 A_{i}\equiv 0 , resulting in a vanishing update signal (advantage collapse).

[33] h3: 2.2. Intrinsic Uncertainty and Entropy Proxy

[34] p: Intrinsic uncertainty measures the dispersion of the policy’s output distribution during generation. We quantify intrinsic uncertainty using an entropy proxy computed from token log-probabilities under the old policy. Throughout the remainder of this paper, we use the term entropy to refer to the NLL-based entropy proxy.

[35] p: For a prompt x x and a response y = ( y 1 , … , y T ) y=(y_{1},\ldots,y_{T}) with length T T , the entropy proxy under the old policy is

[36] table: (5) H ~ ( x , y ) = − 1 T ∑ t = 1 T log π θ old ( y t ∣ x , y < t ) . \tilde{H}(x,y)=-\frac{1}{T}\sum_{t=1}^{T}\log\pi_{\theta_{\text{old}}}\big(y_{t}\mid x,y_{<t}\big).

[37] p: Eq. ( 5 ) is the per-token averaged negative log-likelihood of the sampled response under π θ old \pi_{\theta_{\text{old}}} : larger H ~ ​ ( x , y ) \tilde{H}(x,y) indicates lower assigned probability and higher intrinsic uncertainty, while smaller H ~ ​ ( x , y ) \tilde{H}(x,y) indicates higher assigned probability and lower intrinsic uncertainty. This proxy introduces negligible overhead in RL training because the token log-probabilities log ⁡ π θ old ​ ( y t ∣ x , y < t ) \log\pi_{\theta_{\text{old}}}(y_{t}\mid x,y_{<t}) are already computed during rollout generation.

[38] figure: Algorithm 1 EGPO update for one group 𝒢 ⁡ ( x ) \mathcal{G}(x) . 1: Input: group 𝒢 ⁡ ( x ) = { ( x , y i , r i ) } i = 1 N \mathcal{G}(x)=\{(x,y_{i},r_{i})\}_{i=1}^{N} sampled by the old policy π θ old \pi_{\theta_{\text{old}}} ; current policy π θ \pi_{\theta} ; clip ϵ \epsilon ; weight bounds λ min , λ max \lambda_{\min},\lambda_{\max} ; ε H \varepsilon_{H} ; Renorm . 2: Output: updated policy parameters θ \theta . 3: Compute entropy for each response: H ~ i ← H ~ ​ ( x , y i ) \tilde{H}_{i}\leftarrow\tilde{H}(x,y_{i}) by Eq. ( 5 ). 4: Compute group mean entropy H ¯ ← 1 N ​ ∑ i = 1 N H ~ i \bar{H}\leftarrow\frac{1}{N}\sum_{i=1}^{N}\tilde{H}_{i} . 5: Compute raw ratio weight w ^ i ← H ¯ H ~ i + ε H \hat{w}_{i}\leftarrow\frac{\bar{H}}{\tilde{H}_{i}+\varepsilon_{H}} by Eq. ( 7 ). 6: Apply asymmetric clamp to obtain w i w_{i} by Eq. ( 8 ). 7: if Renorm = 1 =1 then 8: Renormalize weights by Eq. ( 9 ). 9: end if 10: Group-type handling: 11: if ∀ i , r i = + 1 \forall i,\ r_{i}=+1 then 12: return ⊳ \triangleright entirely-correct: skip 13: else if ∀ i , r i = − 1 \forall i,\ r_{i}=-1 then 14: Set A i ← − 1 A_{i}\leftarrow-1 for all i i ⊳ \triangleright entirely-incorrect: NSR 15: else 16: Compute GRPO advantages A i A_{i} by Eq. ( 2 ) ⊳ \triangleright mixed group 17: end if 18: Form calibrated advantages A ~ i ← w i ⋅ A i \tilde{A}_{i}\leftarrow w_{i}\cdot A_{i} by Eq. ( 11 ). 19: Update θ \theta by maximizing Eq. ( 12 ) with clip ϵ \epsilon .

[39] h2: 3. Methodology

[40] p: Building on the outcome-only RLVR setup in Sec. 2.1.1 and the intrinsic uncertainty measure in Sec. 2.2 , we now introduce our Entropy-Guided Policy Optimization framework, EGPO. Existing outcome-only RLVR pipelines typically rely on group-relative objectives such as GRPO to derive policy gradients. Under binary outcome rewards, however, these objectives exhibit two structural limitations: (i) they ignore the large variation in the policy’s intrinsic uncertainty across rollouts, and (ii) they suffer from advantage collapse on all-same groups, discarding precisely the hard prompts where the learning signal is scarce.

[41] p: EGPO addresses these limitations through a metacognitive calibration mechanism that explicitly couples outcome feedback with intrinsic uncertainty. Rather than changing the verifier or reward definition, EGPO reshapes the group-based update by: (1) computing an entropy-based weight for each response and (2) forming a calibrated advantage A ~ i = w i ​ A i \tilde{A}_{i}=w_{i}A_{i} that is both outcome-aware and uncertainty-aware. On mixed groups, A i A_{i} is the GRPO advantage in Eq. ( 2 ) and w i w_{i} is obtained via an asymmetric calibration that promotes confident correct rollouts while tempering updates on uncertain or confidently wrong ones. On entirely-incorrect groups, EGPO adopts NSR by setting A i = − 1 A_{i}=-1 and then applies the same calibrated weighting, recovering a non-vanishing and structured learning signal under advantage collapse. In this way, EGPO provides a unified treatment of mixed and all-incorrect groups within a single PPO-style objective.

[42] h3: 3.1. Entropy-Guided Policy Optimization (EGPO)

[43] p: We follow the RLVR setup in Sec. 2.1.1 . For each prompt x x , we sample a group of N N responses { y i } i = 1 N \{y_{i}\}_{i=1}^{N} from the old policy π θ old ( ⋅ ∣ x ) \pi_{\theta_{\text{old}}}(\cdot\mid x) and obtain outcome rewards r i r_{i} via Eq. ( 1 ), forming 𝒢 ⁡ ( x ) = { ( x , y i , r i ) } i = 1 N \mathcal{G}(x)=\{(x,y_{i},r_{i})\}_{i=1}^{N} . We retain the PPO-style importance ratio ρ i ​ ( θ ) \rho_{i}(\theta) and clipped objective used in GRPO (Sec. 2.1.2 ); the core innovation of EGPO lies in how the group-based advantages are constructed and calibrated by entropy within each group.

[44] h4: 3.1.1. Calibration mechanism: group-relative entropy weighting

[45] figure: Figure 2 . Asymmetric calibration in EGPO: correct responses are never down-weighted and incorrect responses are never up-weighted.

[46] p: We first assign an entropy value to each response using the NLL-based proxy in Eq. ( 5 ):

[47] table: (6) H ~ i ≜ H ~ ​ ( x , y i ) . \tilde{H}_{i}\;\triangleq\;\tilde{H}(x,y_{i}).

[48] p: This quantity captures how unlikely the realized trajectory y i y_{i} is under π θ old \pi_{\theta_{\text{old}}} and thus serves as a token-level measure of intrinsic uncertainty.

[49] p: To incorporate this uncertainty in a verifier-agnostic and calibration-robust way, EGPO operates within each group. We compute the mean entropy H ¯ = 1 N ​ ∑ i = 1 N H ~ i \bar{H}=\frac{1}{N}\sum_{i=1}^{N}\tilde{H}_{i} and define a group-relative weight

[50] table: (7) w ^ i = H ¯ H ~ i + ε H , \hat{w}_{i}\;=\;\frac{\bar{H}}{\tilde{H}_{i}+\varepsilon_{H}},

[51] p: where ε H > 0 \varepsilon_{H}>0 avoids numerical instability. This inverse-entropy ratio has two key effects: (i) it is scale-preserving at the group level, and (ii) it reallocates update magnitudes among responses for the same prompt according to their relative intrinsic uncertainty, without requiring globally calibrated entropy across prompts.

[52] h4: 3.1.2. Calibration mechanism: outcome-aware asymmetric calibration

[53] p: To implement the metacognitive principle in outcome-only RLVR, EGPO couples intrinsic uncertainty with verifier outcomes when scaling update. Intuitively, high-confidence correct responses should be reinforced more aggressively, while penalties on failures should be regulated so as not to destroy latent reasoning competence or exploration. Concretely, EGPO transforms w ^ i \hat{w}_{i} via an outcome-aware asymmetric clamp (Fig. 2 ) with bounds λ min \lambda_{\min} and λ max \lambda_{\max} :

[54] table: (8) w i = { max ⁡ ( 1.0 , clip ⁡ ( w ^ i , λ min , λ max ) ) , r i = + 1 , min ⁡ ( 1.0 , clip ⁡ ( w ^ i , λ min , λ max ) ) , r i = − 1 , w_{i}\;=\;\begin{cases}\max\!\Big(1.0,\,\mathrm{clip}(\hat{w}_{i},\lambda_{\min},\lambda_{\max})\Big),&r_{i}=+1,\\ \min\!\Big(1.0,\,\mathrm{clip}(\hat{w}_{i},\lambda_{\min},\lambda_{\max})\Big),&r_{i}=-1,\end{cases}

[55] p: which enforces that correct responses are never down-weighted ( w i ≥ 1 w_{i}\geq 1 ) while incorrect responses are never up-weighted ( w i ≤ 1 w_{i}\leq 1 ). This asymmetric calibration yields a principled bias: it amplifies updates on confident correct rollouts, while ensuring that uncertainty does not translate into disproportionately large negative gradients on failures.

[56] p: Optionally, EGPO applies within-group renormalization

[57] table: (9) w i ← w i 1 N ​ ∑ j = 1 N w j , w_{i}\leftarrow\frac{w_{i}}{\frac{1}{N}\sum_{j=1}^{N}w_{j}},

[58] p: to keep the mean weight equal to 1 1 . As shown in our ablation study (Sec. 4.3 ), this renormalization can increase the performance ceiling on some benchmarks without introducing instability.

[59] h4: 3.1.3. Base advantage, calibrated advantage, and objective

[60] p: We now specify the base advantage A i A_{i} according to the outcome pattern of 𝒢 ⁡ ( x ) \mathcal{G}(x) :

[61] table: (10) A i = { 0 , entirely-correct group , r i − mean ⁡ ( r 1 , … , r N ) std ⁡ ( r 1 , … , r N ) , mixed group , − 1 , entirely-incorrect group . A_{i}\;=\;\begin{cases}0,&\textit{entirely-correct group},\\[2.0pt] \frac{r_{i}-\mathrm{mean}(r_{1},\ldots,r_{N})}{\mathrm{std}(r_{1},\ldots,r_{N})},&\textit{mixed group},\\[6.0pt] -1,&\textit{entirely-incorrect group}.\end{cases}

[62] p: The mixed-group case recovers the GRPO advantage in Eq. ( 2 ). The entirely-correct case corresponds to skipping updates. The entirely-incorrect case instantiates NSR (Sec. 3.2 ) via a constant negative advantage.

[63] p: Given A i A_{i} and w i w_{i} , EGPO forms the calibrated advantage

[64] table: (11) A ~ i = w i ⋅ A i , \tilde{A}_{i}\;=\;w_{i}\cdot A_{i},

[65] p: and optimizes a weighted clipped-ratio objective:

[66] table: (12) ℒ E ​ G ​ P ​ O ​ ( θ ) = 𝔼 ( x , y i ) ∼ 𝒢 ​ [ min ⁡ ( ρ i ​ ( θ ) ​ A ~ i , clip ⁡ ( ρ i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A ~ i ) ] , \mathcal{L}_{EGPO}(\theta)=\mathbb{E}_{(x,y_{i})\sim\mathcal{G}}\Big[\min\big(\rho_{i}(\theta)\,\tilde{A}_{i},\;\mathrm{clip}(\rho_{i}(\theta),1-\epsilon,1+\epsilon)\,\tilde{A}_{i}\big)\Big],

[67] p: where ρ i ​ ( θ ) \rho_{i}(\theta) is defined in Eq. ( 4 ) and ϵ \epsilon is the PPO clipping coefficient. Algorithm 1 summarizes the complete EGPO update for one trajectory set.

[68] h3: 3.2. Negative Sample Reinforcement (NSR) for Entirely-Incorrect Groups

[69] p: We now detail the NSR component used within EGPO for entirely-incorrect groups. Let 𝒢 − ​ ( x ) = { ( x , y i , r i ) } i = 1 N \mathcal{G}^{-}(x)=\{(x,y_{i},r_{i})\}_{i=1}^{N} denote a group where r i = − 1 r_{i}=-1 for all i i . Every sampled response in 𝒢 − ​ ( x ) \mathcal{G}^{-}(x) carries a negative learning signal under the outcome reward, but GRPO alone would collapse these signals to zero.

[70] p: Within EGPO, we instantiate NSR by using a constant negative base advantage:

[71] table: (13) A i = − 1 , ∀ i ∈ { 1 , … , N } , A_{i}\;=\;-1,\quad\forall i\in\{1,\ldots,N\}\,,

[72] p: where − 1 -1 serves as a normalized choice of scale and ensures a consistent negative update direction across responses. This corresponds exactly to the entirely-incorrect case in Eq. ( 10 ). EGPO then applies the same entropy-guided calibration as before, forming A ~ i = w i ​ A i = − w i \tilde{A}_{i}=w_{i}A_{i}=-w_{i} and optimizing Eq. ( 12 ).

[73] h5: Effect under clipping.

[74] p: On 𝒢 − ​ ( x ) \mathcal{G}^{-}(x) , the per-response term in Eq. ( 12 ) becomes

[75] table: (14) ℓ i ​ ( θ ) \displaystyle\ell_{i}(\theta) = min ⁡ ( ρ i ​ ( θ ) ​ ( − w i ) , clip ⁡ ( ρ i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ ( − w i ) ) \displaystyle=\min\Big(\rho_{i}(\theta)\,(-w_{i}),\;\mathrm{clip}(\rho_{i}(\theta),1-\epsilon,1+\epsilon)\,(-w_{i})\Big) = − w i ​ max ⁡ ( ρ i ​ ( θ ) , clip ⁡ ( ρ i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ) . \displaystyle=-w_{i}\,\max\Big(\rho_{i}(\theta),\;\mathrm{clip}(\rho_{i}(\theta),1-\epsilon,1+\epsilon)\Big).

[76] p: Therefore, the objective exhibits the following behavior: (i) if ρ i ​ ( θ ) < 1 − ϵ \rho_{i}(\theta)<1-\epsilon , then ℓ i ​ ( θ ) = − w i ​ ( 1 − ϵ ) \ell_{i}(\theta)=-w_{i}(1-\epsilon) is constant in θ \theta and contributes zero gradient; (ii) if 1 − ϵ ≤ ρ i ​ ( θ ) ≤ 1 + ϵ 1-\epsilon\leq\rho_{i}(\theta)\leq 1+\epsilon , then ℓ i ​ ( θ ) = − w i ​ ρ i ​ ( θ ) \ell_{i}(\theta)=-w_{i}\rho_{i}(\theta) ; (iii) if ρ i ​ ( θ ) > 1 + ϵ \rho_{i}(\theta)>1+\epsilon , then ℓ i ​ ( θ ) = − w i ​ ρ i ​ ( θ ) \ell_{i}(\theta)=-w_{i}\rho_{i}(\theta) . Thus, on entirely-incorrect groups with A ~ i = − w i < 0 \tilde{A}_{i}=-w_{i}<0 , clipping is active only in the low-ratio region ρ i ​ ( θ ) < 1 − ϵ \rho_{i}(\theta)<1-\epsilon ; otherwise the objective reduces to − w i ​ ρ i ​ ( θ ) -w_{i}\rho_{i}(\theta) . Maximizing − w i ​ ρ i ​ ( θ ) -w_{i}\rho_{i}(\theta) drives ρ i ​ ( θ ) \rho_{i}(\theta) downward, which reduces the probability assigned to the sampled response under the current policy in a way that is modulated by entropy.

[77] h5: Gradient characterization.

[78] p: Consider a token step t t in response y i y_{i} . Let z v z_{v} be the logit of token v v and let π v \pi_{v} be its softmax probability under π θ ( ⋅ ∣ x , y < t ) \pi_{\theta}(\cdot\mid x,y_{<t}) . In the unclipped region, the gradient ascent direction on logits satisfies

[79] table: (15) ∂ ℓ i ​ ( θ ) ∂ z v ∝ − w i ρ i ( θ ) ( 𝟏 [ v = y t ] − π v ) . \frac{\partial\ell_{i}(\theta)}{\partial z_{v}}\;\propto\;-w_{i}\,\rho_{i}(\theta)\big(\mathbf{1}[v=y_{t}]-\pi_{v}\big).

[80] p: Eq. ( 15 ) implies that the sampled token y t y_{t} is pushed down while probability mass is redistributed to other tokens at the same step, yielding a consistent negative learning signal on entirely-incorrect groups whose strength is calibrated by entropy. The detailed derivation of Eq. ( 14 )–Eq. ( 15 ), including intermediate steps, is provided in Appendix A.1 .

[81] figure: Table 1 . The Pass@1 Accuracy (%) on 1.5B and 7B models. Abbreviate DeepSeek-R1-Distill-Qwen-* as DeepSeek-R1-* . Model MATH-500 AIME24 MMLU-STEM Minerva GSM8K 1.5B Models Qwen2.5-Math-1.5B (Base) 23.40 6.67 17.44 19.90 58.15 Qwen2.5-Math-1.5B + GRPO ( Yu et al., 2025 ) 67.20 (+43.80) 13.33 (+6.66) 20.84 (+3.40) 32.26 (+12.36) 71.65 (+13.50) Qwen2.5-Math-1.5B + DAPO ( Yu et al., 2025 ) 69.80 (+46.40) 13.33 (+6.66) 22.52 (+5.08) 33.09 (+13.19) 72.33 (+14.18) Qwen2.5-Math-1.5B + EDGE-GRPO ( Zhang et al., 2025 ) 72.00 (+48.60) 16.67 (+10.00) 23.78 (+6.34) 33.82 (+13.92) 74.68 (+16.53) Qwen2.5-Math-1.5B + EGPO (ours) 74.00 (+50.60) 13.33 (+6.66) 25.69 (+8.25) 37.13 (+17.23) 79.83 (+21.68) DeepSeek-R1-1.5B (Base) 81.25 26.67 60.26 66.91 78.47 DeepSeek-R1-1.5B + GRPO ( Yu et al., 2025 ) 84.45 (+3.20) 26.67 (+0.00) 61.84 (+1.58) 66.91 (+0.00) 80.20 (+1.73) DeepSeek-R1-1.5B + DAPO ( Yu et al., 2025 ) 84.45 (+3.20) 23.33 (-3.34) 61.53 (+1.27) 67.28 (+0.37) 79.08 (+0.61) DeepSeek-R1-1.5B + EDGE-GRPO ( Zhang et al., 2025 ) 84.25 (+3.00) 26.67 (0.00) 62.10 (+1.84) 67.65 (+0.74) 81.27 (+2.80) DeepSeek-R1-1.5B + EGPO (ours) 87.80 (+6.55) 33.33 (+6.66) 66.29 (+6.03) 70.22 (+3.31) 83.40 (+4.93) 7B Models Qwen2.5-Math-7B (Base) 13.80 3.33 24.05 29.41 80.44 Qwen2.5-Math-7B + GRPO ( Yu et al., 2025 ) 80.80 (+67.00) 26.25 (+22.92) 66.60 (+42.55) 41.18 (+11.77) 83.40 (+2.96) Qwen2.5-Math-7B + DAPO ( Yu et al., 2025 ) 80.25 (+66.45) 27.08 (+23.75) 63.72 (+39.67) 40.81 (+11.40) 86.43 (+5.99) Qwen2.5-Math-7B + EDGE-GRPO ( Zhang et al., 2025 ) 81.50 (+67.70) 30.42 (+27.09) 67.08 (+43.03) 41.18 (+11.77) 84.91 (+4.47) Qwen2.5-Math-7B + EGPO (ours) 84.60 (+70.80) 33.33 (+30.00) 70.09 (+46.04) 44.49 (+15.08) 89.84 (+9.40) DeepSeek-R1-7B (Base) 87.48 56.67 85.15 77.94 90.06 DeepSeek-R1-7B + GRPO ( Yu et al., 2025 ) 90.80 (+3.32) 54.58 (-2.09) 84.99 (-0.16) 78.67 (+0.73) 90.60 (+0.54) DeepSeek-R1-7B + DAPO ( Yu et al., 2025 ) 91.40 (+3.92) 60.00 (+3.33) 84.73 (-0.42) 80.15 (+2.21) 90.14 (+0.08) DeepSeek-R1-7B + EDGE-GRPO ( Zhang et al., 2025 ) 90.80 (+3.32) 60.00 (+3.33) 87.21 (+2.06) 80.88 (+2.94) 91.05 (+0.99) DeepSeek-R1-7B + EGPO (ours) 93.40 (+5.92) 66.67 (+10.00) 91.98 (+6.83) 83.46 (+5.52) 93.18 (+3.12)

[82] h2: 4. Experiments

[83] p: In this section, we perform comprehensive experiments to evaluate the effectiveness of EGPO. We explicitly address the following research questions:

[84] p: RQ1: To what extent does EGPO improve reasoning performance and generalization over strong RL baselines?

[85] p: RQ2: How does each component of EGPO contribute to its overall effectiveness?

[86] p: RQ3: Can visualizations provide evidence of EGPO’s effectiveness?

[87] p: RQ4: Does a more fine-grained entropy guidance further improve performance?

[88] h3: 4.1. Experimental Setup

[89] p: Models and Baselines. We evaluate EGPO on two backbone families: Qwen2.5-Math (1.5B/7B) and DeepSeek-R1-Distill-Qwen (1.5B/7B). 1 1 1 Model links: https://huggingface.co/Qwen/Qwen2.5-Math-1.5B , https://huggingface.co/Qwen/Qwen2.5-Math-7B , https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B , https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B . We compare EGPO against GRPO ( Shao et al., 2024 ) , DAPO ( Yu et al., 2025 ) , and EDGE-GRPO ( Zhang et al., 2025 ) . All methods are trained on the default binary outcome reward in Eq. ( 1 ) for a controlled comparison.

[90] p: Training Data. We train on a curated subset derived from OpenR1-math-220k ( Hugging Face, 2025 ) . The subset is constructed to cover a representative difficulty spectrum while reducing reward noise via filtering and deduplication (full description in Appendix A.2 ). To control a small number of extreme-length outliers and keep the prompt-length distribution well-behaved, we filter samples with prompt length > 1024 >1024 , yielding the final training dataset OpenR1-stable-10K . We use the default binary outcome reward in Eq. ( 1 ).

[91] p: Training Setup. We conduct training using the widely used open-source RL training verl framework ( Sheng et al., 2024 ) for all RL experiments. Unless stated otherwise, we sample N = 16 N=16 rollouts per prompt and train for 5 epochs (about 770 steps). The learning rate is set to 1 × 10 − 6 1\times 10^{-6} . For our proposed EGPO method, we implement the asymmetric weight clipping with bounds λ min = 0.8 \lambda_{\min}=0.8 and λ max = 2.0 \lambda_{\max}=2.0 . All other hyperparameters, including clipping coefficient and DAPO dynamic sampling ranges, follow the default configuration in verl .

[92] p: Benchmarks and Evaluation. We evaluate on MATH-500 ( Hendrycks et al., 2021b ) , AIME 2024 ( Art of Problem Solving Wiki, 2024a ; Art of Problem Solving Wiki, 2024b ) , Minerva ( Lewkowycz et al., 2022 ) , GSM8K ( Cobbe et al., 2021 ) , and MMLU-STEM ( Hendrycks et al., 2021a ) using the widely used open-source evaluation framework evalscope ( ModelScope Team, 2024 ) with default templates to ensure reproducibility. 2 2 2 Research shows that reasoning scores can be highly sensitive to prompt templates and evaluation/seeds/decoding hyperparameters ( Liu et al., 2025b ) . We therefore fix the evaluation harness and use the default templates throughout for fair comparison. To maximize comparability and robustness, we adopt a unified decoding configuration: we set temperature T = 0.6 T=0.6 , top- p = 0.95 p=0.95 , and top- k = 20 k=20 with random sampling enabled (do_sample=True). For each benchmark, we conduct 8 independent trials and report the mean pass@1 accuracy. The maximum generation length is set to 3,072 tokens for Qwen2.5-Math series (fitting their context constraints) and 16,384 tokens for DeepSeek-R1-Distill-Qwen to prevent truncation.

[93] figure: Table 2 . Ablations on Qwen2.5-Math-1.5B under the default binary outcome reward and w i w_{i} denotes EGPO’s group-relative weight. Variant Constraint on w i w_{i} Entirely-incorrect groups Renorm MATH-500 Minerva GSM8K Avg. Base – – – 23.4 19.90 58.15 33.82 C1 (symmetric) λ min ≤ w i ≤ λ max \lambda_{\min}\leq w_{i}\leq\lambda_{\max} NSR + w i w_{i} none 66.0 33.09 80.97 60.02 C2 (neg ≤ 1 \leq 1 only) w i ≤ 1 w_{i}\leq 1 when r i = − 1 r_{i}=-1 only NSR + w i w_{i} none 70.6 30.51 78.01 59.71 C3 (pos ≥ 1 \geq 1 only) w i ≥ 1 w_{i}\geq 1 when r i = + 1 r_{i}=+1 only NSR + w i w_{i} none 72.6 33.04 80.59 62.08 C4 (neg locked to 1) asymmetric clamp NSR with w i ≡ 1 w_{i}\equiv 1 none 72.0 34.61 79.68 62.10 C5 (clamp → \rightarrow renorm) asymmetric clamp NSR + w i w_{i} after clamp 81.05 35.29 80.29 65.54 C6 (renorm → \rightarrow clamp) asymmetric clamp NSR + w i w_{i} before clamp 72.2 34.19 80.06 62.15 EGPO asymmetric clamp NSR + w i w_{i} none 76.40 37.13 81.43 65.97

[94] figure: Figure 3 . Density comparison of the entropy on the response for Qwen2.5-Math-1.5B, comparing Base/GRPO/DAPO/EDGE-GRPO/EGPO on correct vs. incorrect rollouts.

[95] h3: 4.2. RQ1: Comparison with Baselines

[96] p: Table 1 reports the main results on four mathematics benchmarks and MMLU-STEM to evaluate both effectiveness and generalization. Across both 1.5B and 7B model scales, EGPO consistently outperforms strong RL baselines on nearly all benchmarks and achieves the best overall performance. Notably, EDGE-GRPO, as an early uncertainty-aware RLVR baseline, already surpasses most other RLVR methods in many cases, validating the importance of incorporating uncertainty into RLVR, yet EGPO still delivers consistent and clear gains over EDGE-GRPO, indicating that our metacognitive uncertainty calibration leverages uncertainty more effectively. Compared with base models such as Qwen2.5-Math and DeepSeek-R1, EGPO yields substantial improvements, particularly on Qwen2.5-Math-7B, where it boosts MATH-500 by +70.80% over Base and further exceeds the strongest RL baseline by +3.10%, while also achieving state-of-the-art results on Minerva and GSM8K. In addition, EGPO exhibits strong generalization on MMLU-STEM (e.g., +46.04% over Base), suggesting that integrating intrinsic uncertainty into RLVR not only enhances in-domain reasoning performance but also strengthens generalizable reasoning behaviors beyond training domains. Moreover, performance margins tend to be larger at 7B, implying that EGPO more effectively raises the performance ceiling when the model capacity is sufficient.

[97] p: AIME24 consists of high-difficulty competition problems, so all models exhibit relatively low absolute performance, largely due to the 4096 context length constraint that can truncate long derivations. With larger base model capacity, this limitation is partially alleviated and EGPO demonstrates clear advantages on hard problems. On Qwen2.5-Math-7B, EGPO improves AIME24 by +30.00% over Base and further exceeds the strongest RL baseline EDGE-GRPO by +2.91%. On DeepSeek-R1-7B, EGPO reaches 66.67% and surpasses the strongest RL baselines by +6.67%. These results indicate that EGPO effectively extracts informative learning signals even on the most challenging instances under outcome-only RLVR. A detailed per-backbone and per-scale analysis is provided in Appendix A.3 .

[98] h3: 4.3. RQ2: Ablation Analysis

[99] p: To evaluate the contribution of each module, we conduct ablation study on Qwen2.5-Math-1.5B under the default binary outcome reward. All variants follow the same training setup and only differ in how constraints are applied to w i w_{i} and how entirely-incorrect groups are handled (Table 2 ).

[100] h4: 4.3.1. Asymmetric constraints as a mechanism for balancing exploitation and exploration.

[101] p: EGPO enforces an outcome-aware asymmetric clamp on w i w_{i} (never down-weight correct rollouts; never up-weight incorrect rollouts), which strengthens exploitation while avoiding overly aggressive negative updates that can reduce exploration. C1 instead uses a symmetric clamp λ min ≤ w i ≤ λ max \lambda_{\min}\leq w_{i}\leq\lambda_{\max} , allowing both down-weighting correct rollouts and up-weighting incorrect rollouts, and is consistently worse than EGPO (e.g., 66.0 vs. 76.40 on MATH-500; 33.09 vs. 37.13 on Minerva). The one-sided constraints (C2/C3) remain inferior, indicating both sides of the asymmetric clamp are needed for a better exploration–exploitation balance.

[102] h4: 4.3.2. Entirely-incorrect groups: extracting learning signal while preserving exploration.

[103] p: Entirely-incorrect groups require NSR to obtain learning signals. Fixing w i ≡ 1 w_{i}\equiv 1 on such groups (C4) removes entropy-conditioned redistribution and applies uniform negative pressure regardless of entropy. EGPO applies NSR together with w i w_{i} , penalizing high-entropy failures more conservatively, which better preserves exploration and improves performance on harder prompts (e.g., Minerva: 37.13 vs. 34.61).

[104] h4: 4.3.3. Renorm: where it is applied matters.

[105] p: Applying renorm after clamp (C5) can increase the performance ceiling on some benchmarks without introducing instability (e.g., GSM8K). In contrast, applying renorm before clamp (C6) is consistently less effective, suggesting that re-centering weights prior to enforcing asymmetry weakens the intended redistribution of update magnitude. However, the gains from C5 are not consistent across benchmarks and do not improve the overall average compared with EGPO. Therefore, we use the asymmetric clamp without renorm as the default setting.

[106] h3: 4.4. RQ 3: Visualization

[107] p: Beyond pass@1, we analyze the response entropy distribution as defined in Eq. ( 5 ) and conduct a qualitative case study to further demonstrate the advantages of EGPO over the base model. As shown in Fig. 3 , EGPO achieves the most pronounced separation between correct and incorrect rollouts in terms of response entropy. In particular,EGPO produces a much lower mean entropy for correct samples ( μ = 0.080 \mu=0.080 ) and a substantially higher mean entropy for incorrect samples ( μ = 0.129 \mu=0.129 ), resulting in the largest mean gap ( Δ = 0.048 \Delta=0.048 ). In contrast, GRPO and EDGE-GRPO exhibit only modest gaps ( Δ = 0.011 \Delta=0.011 and Δ = 0.012 \Delta=0.012 ), DAPO shows a marginal gap ( Δ = 0.004 \Delta=0.004 ), and Base even displays a reversed ordering with Δ = − 0.020 \Delta=-0.020 . These results indicate that EGPO effectively aligns intrinsic uncertainty with verifier outcomes at the final answer level, making the update signal increasingly targeted under binary outcome rewards and enabling the model to realize the principle of “Know What You Know”.

[108] p: To further substantiate this finding, Fig. 4 presents a representative case comparison between Qwen-2.5-Math-1.5B and EGPO under the same setting. In this example, EGPO exhibits higher entropy yet ultimately arrives at a correct and well-supported solution, whereas the base model fails to reach the correct answer. This qualitative evidence complements our quantitative analysis and provides additional validation of the effectiveness of EGPO in guiding more reliable and effective reasoning.

[109] h3: 4.5. RQ4: Extended Evaluations

[110] figure: Figure 4 . A qualitative case on Qwen2.5-Math-1.5B comparing Base vs. EGPO, including the entropy on the response.

[111] p: Some representative reasoning models (e.g., DeepSeek-R1) explicitly separate internal reasoning from final answers using dedicated <think>…</think> tokens. The content within <think> captures the model’s intermediate reasoning process, including tentative steps, backtracking, and self-correction, whereas the text outside <think> corresponds to the finalized answer presented to the user. Accordingly, we distinguish two types of uncertainty: Thinking Entropy (TE) , computed over the reasoning trace inside <think>, and Answer Entropy (AE) , computed over the distribution of the final answer. To provide a more comprehensive analysis of our method, we systematically evaluate both uncertainty signals. Specifically, we sample 1,000 problems and generate 8 rollouts per problem using DeepSeek-R1-Distill-Qwen backbones. As shown in Table 3 , AE is consistently more predictive of incorrectness than Thinking-side entropy, with AUC improving from 0.745 0.745 to 0.778 0.778 on 1.5B and from 0.700 0.700 to 0.738 0.738 on 7B, which suggests that fine-grained entropy guidance should focus on AE to better align the entropy signal with verifier outcomes. The corresponding ROC curves are provided in Appendix A.4 (Fig. 5(a) ), and we further confirm that this result is not driven by response length in Appendix A.4 .

[112] h2: 5. Related Work

[113] p: Reasoning and verifiable training. Reasoning performance has improved via chain-of-thought (CoT) prompting, self-consistency, and search-based prompting ( Wei et al., 2022 ; Kojima et al., 2022 ; Wang et al., 2022 ; Yao et al., 2023 ; Yao et al., 2022 ) . RLVR leverages verifiable signals (e.g., exact answers, symbolic checking, or program execution) to scale post-training beyond human preference labels ( Lightman et al., 2023 ; Shao et al., 2024 ) . Recent work explores richer rubric-based or multi-signal verification ( Liu et al., 2025d ; He et al., 2025 ; Tan et al., 2025 ) and analyzes R1-Zero style training dynamics ( Liu et al., 2025a ; Chen et al., 2026 ) . In contrast, EGPO keeps the verifier unchanged and focuses on calibrating the policy update magnitude.

[114] p: RLHF, PPO-style alignment, and group-based training. RLHF and preference learning optimize policies from comparisons, typically optimized with policy-gradient and trust-region updates ( Williams, 1992 ; Konda and Tsitsiklis, 2000 ; Kakade, 2002 ; Schulman et al., 2015 ; Schulman et al., 2016 ) ( Christiano et al., 2017 ; Stiennon et al., 2020 ; Ziegler et al., 2019 ) , while DPO-style objectives avoid explicit reward modeling ( Rafailov et al., 2023 ) . For verifiable tasks, group-based objectives such as GRPO reduce variance via within-group normalization and have become a common RLVR primitive ( Shao et al., 2024 ; Yu et al., 2025 ) . Recent variants study stability and bias (e.g., DAPO/Dr.GRPO/DRA-GRPO/GSPO) ( Yu et al., 2025 ; Liu et al., 2025a ; Chen et al., 2026 ; Zheng et al., 2025 ) and advantage estimators such as key-token credit assignment ( Sun et al., 2025 ) . EGPO is complementary: it modifies neither the reward nor the verifier, but rescales update magnitudes using an intrinsic uncertainty proxy and additionally recovers learning signal from entirely-incorrect groups.

[115] p: Uncertainty, calibration, and metacognition in LLMs. Classic calibration work studies the relationship between probabilistic uncertainty and accuracy ( Guo et al., 2017 ; Niculescu-Mizil and Caruana, 2005 ; Ovadia et al., 2019 ) . Recent works use uncertainty to guide or stabilize training ( Du et al., 2025 ; Yoon et al., 2025 ; Tang et al., 2025 ) . AURORA aligns reward optimization with uncertainty-aware signals ( Tan et al., 2025 ) . EGPO differs in mechanism: it does not add uncertainty to the reward; instead, it treats uncertainty as a metacognitive scaling factor on policy gradients, aligning intrinsic uncertainty with extrinsic correctness.

[116] p: Entropy in RL and in LLM post-training. Entropy regularization is central to maximum-entropy RL ( Ziebart et al., 2008 ; Haarnoja et al., 2018 ) and appears in LLM post-training as a stabilizer ( Yu et al., 2025 ; Agarwal et al., 2025 ) . However, entropy minimization alone can encourage overconfident collapse or shortcut behavior ( Agarwal et al., 2025 ; Cui et al., 2025 ) . EDGE-GRPO ( Zhang et al., 2025 ) introduced using a group-relative entropy ratio as a practical weighting construction in GRPO-style RLVR. In this work, we treat such entropy-ratio weighting as one intrinsic metacognitive signal for uncertainty, and we directly compare against EDGE-GRPO in Sec. 4.2 . Our focus is not to change the verifier or reward, but to make the use of uncertainty signals outcome-aware and robust under binary RLVR, via asymmetric constraints and explicit learning from entirely-incorrect groups.

[117] h2: 6. Conclusion

[118] figure: Table 3 . ROC-AUC for predicting incorrectness using entropy (higher is better). Backbone TE AE DeepSeek-R1-Distill-Qwen-1.5B 0.745 0.778 DeepSeek-R1-Distill-Qwen-7B 0.700 0.738

[119] p: In this work, we introduced EGPO, a metacognitive entropy calibration framework for outcome-only RLVR that bridges the gap between intrinsic uncertainty and extrinsic correctness. By rescaling update magnitudes within group-based policy optimization, EGPO systematically aligns entropy-based uncertainty with the default binary verifier without modifying the reward definition. Specifically, we enforce an outcome-aware asymmetric calibration rule that guarantees correct rollouts are never down-weighted while preventing incorrect rollouts from being up-weighted, thereby improving the exploration–exploitation balance under sparse verifiable rewards. Furthermore, EGPO integrates entropy-damped NSR with group-relative weighting to recover informative learning signals from entirely incorrect groups under advantage collapse, while avoiding overly aggressive suppression of uncertain failures. Empirically, across multiple benchmarks, EGPO delivers consistent and substantial gains on both Qwen2.5-Math and DeepSeek-R1-Distill-Qwen backbones, validating the effectiveness of metacognitive entropy calibration for advancing reasoning language models.

[120] h2: References

[121] h2: Appendix A Supplementary Material

[122] h3: A.1. Derivation for NSR updates on entirely-incorrect groups

[123] p: We derive Eq. ( 15 ) from the EGPO objective (Eq. ( 12 )) on an entirely-incorrect group. We consider one group 𝒢 − ​ ( x ) = { ( x , y i , r i ) } i = 1 N \mathcal{G}^{-}(x)=\{(x,y_{i},r_{i})\}_{i=1}^{N} with r i = − 1 r_{i}=-1 for all i i . Under NSR, the base advantage is A i = − 1 A_{i}=-1 (Eq. ( 13 )), and the calibrated advantage becomes

[124] table: (16) A ~ i = w i ​ A i = − w i . \tilde{A}_{i}\;=\;w_{i}A_{i}\;=\;-w_{i}.

[125] h5: Clipped objective term.

[126] p: For one sampled response y i y_{i} , the per-response term in Eq. ( 12 ) is

[127] table: (17) ℓ i ​ ( θ ) = min ⁡ ( ρ i ​ ( θ ) ​ A ~ i , clip ⁡ ( ρ i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A ~ i ) . \ell_{i}(\theta)=\min\Big(\rho_{i}(\theta)\,\tilde{A}_{i},\;\mathrm{clip}(\rho_{i}(\theta),1-\epsilon,1+\epsilon)\,\tilde{A}_{i}\Big).

[128] p: Substituting A ~ i = − w i \tilde{A}_{i}=-w_{i} yields

[129] table: (18) ℓ i ​ ( θ ) \displaystyle\ell_{i}(\theta) = min ⁡ ( ρ i ​ ( θ ) ​ ( − w i ) , clip ⁡ ( ρ i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ ( − w i ) ) \displaystyle=\min\Big(\rho_{i}(\theta)\,(-w_{i}),\;\mathrm{clip}(\rho_{i}(\theta),1-\epsilon,1+\epsilon)\,(-w_{i})\Big) = − w i ​ max ⁡ ( ρ i ​ ( θ ) , clip ⁡ ( ρ i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ) . \displaystyle=-w_{i}\,\max\Big(\rho_{i}(\theta),\;\mathrm{clip}(\rho_{i}(\theta),1-\epsilon,1+\epsilon)\Big).

[130] p: where the equality follows because multiplying by a negative scalar reverses the order.

[131] h5: Effect of clipping.

[132] p: Let ρ = ρ i ​ ( θ ) \rho=\rho_{i}(\theta) . By the definition of clip ⁡ ( ⋅ ) \mathrm{clip}(\cdot) ,

[133] table: (19) clip ⁡ ( ρ , 1 − ϵ , 1 + ϵ ) = { 1 − ϵ , ρ < 1 − ϵ , ρ , 1 − ϵ ≤ ρ ≤ 1 + ϵ , 1 + ϵ , ρ > 1 + ϵ . \mathrm{clip}(\rho,1-\epsilon,1+\epsilon)=\begin{cases}1-\epsilon,&\rho<1-\epsilon,\\ \rho,&1-\epsilon\leq\rho\leq 1+\epsilon,\\ 1+\epsilon,&\rho>1+\epsilon.\end{cases}

[134] p: Plugging Eq. ( 19 ) into Eq. ( 18 ) gives three cases: (i) if ρ < 1 − ϵ \rho<1-\epsilon , then max ⁡ ( ρ , clip ⁡ ( ρ ) ) = 1 − ϵ \max(\rho,\mathrm{clip}(\rho))=1-\epsilon and ℓ i ​ ( θ ) = − w i ​ ( 1 − ϵ ) \ell_{i}(\theta)=-w_{i}(1-\epsilon) is constant in ρ \rho , thus contributing zero gradient; (ii) if 1 − ϵ ≤ ρ ≤ 1 + ϵ 1-\epsilon\leq\rho\leq 1+\epsilon , then clip ⁡ ( ρ ) = ρ \mathrm{clip}(\rho)=\rho and ℓ i ​ ( θ ) = − w i ​ ρ \ell_{i}(\theta)=-w_{i}\rho ; (iii) if ρ > 1 + ϵ \rho>1+\epsilon , then clip ⁡ ( ρ ) = 1 + ϵ < ρ \mathrm{clip}(\rho)=1+\epsilon<\rho and ℓ i ​ ( θ ) = − w i ​ ρ \ell_{i}(\theta)=-w_{i}\rho . Therefore, for negative advantages on entirely-incorrect groups, clipping is active only when ρ < 1 − ϵ \rho<1-\epsilon ; otherwise the objective reduces to

[135] table: (20) ℓ i ​ ( θ ) = − w i ​ ρ i ​ ( θ ) . \ell_{i}(\theta)\;=\;-w_{i}\,\rho_{i}(\theta).

[136] h5: Gradient direction in the unclipped region.

[137] p: We derive the gradient of Eq. ( 20 ). Since ρ i ​ ( θ ) = π θ ​ ( y i ∣ x ) / π θ old ​ ( y i ∣ x ) \rho_{i}(\theta)=\pi_{\theta}(y_{i}\mid x)/\pi_{\theta_{\text{old}}}(y_{i}\mid x) and π θ old ​ ( y i ∣ x ) \pi_{\theta_{\text{old}}}(y_{i}\mid x) is constant w.r.t. θ \theta , we have

[138] table: (21) ∂ ρ i ​ ( θ ) ∂ z v = ρ i ​ ( θ ) ​ ∂ log ⁡ π θ ​ ( y i ∣ x ) ∂ z v . \frac{\partial\rho_{i}(\theta)}{\partial z_{v}}=\rho_{i}(\theta)\,\frac{\partial\log\pi_{\theta}(y_{i}\mid x)}{\partial z_{v}}.

[139] p: Moreover,

[140] table: (22) log ⁡ π θ ​ ( y i ∣ x ) = ∑ t = 1 T i log ⁡ π θ ​ ( y t ∣ x , y < t ) . \log\pi_{\theta}(y_{i}\mid x)=\sum_{t=1}^{T_{i}}\log\pi_{\theta}(y_{t}\mid x,y_{<t}).

[141] p: At a fixed step t t , let π v \pi_{v} be the softmax probability of token v v under π θ ( ⋅ ∣ x , y < t ) \pi_{\theta}(\cdot\mid x,y_{<t}) and z v z_{v} the corresponding logit. The standard softmax derivative gives

[142] table: (23) ∂ log ⁡ π θ ​ ( y t ∣ x , y < t ) ∂ z v = 𝟏 [ v = y t ] − π v . \frac{\partial\log\pi_{\theta}(y_{t}\mid x,y_{<t})}{\partial z_{v}}=\mathbf{1}[v=y_{t}]-\pi_{v}.

[143] p: Combining Eq. ( 20 )–Eq. ( 23 ),

[144] table: (24) ∂ ℓ i ​ ( θ ) ∂ z v = − w i ∂ ρ i ​ ( θ ) ∂ z v = − w i ρ i ( θ ) ( 𝟏 [ v = y t ] − π v ) . \frac{\partial\ell_{i}(\theta)}{\partial z_{v}}=-w_{i}\,\frac{\partial\rho_{i}(\theta)}{\partial z_{v}}=-w_{i}\,\rho_{i}(\theta)\big(\mathbf{1}[v=y_{t}]-\pi_{v}\big).

[145] p: Since EGPO maximizes Eq. ( 12 ), the gradient ascent direction on logits is

[146] table: (25) ∂ ℒ E ​ G ​ P ​ O ∂ z v ∝ w i ρ i ( θ ) ( 𝟏 [ v = y t ] − π v ) , \frac{\partial\mathcal{L}_{EGPO}}{\partial z_{v}}\propto w_{i}\,\rho_{i}(\theta)\big(\mathbf{1}[v=y_{t}]-\pi_{v}\big),

[147] p: which matches Eq. ( 15 ). In particular, the sampled token y t y_{t} is pushed down while probability mass is redistributed to other tokens, yielding a consistent negative update direction on entirely-incorrect groups.

[148] h3: A.2. Dataset Construction: OpenR1-Math Stable-10k

[149] p: We load OpenR1-Math shards ( Hugging Face, 2025 ) consisting of default and extended subsets, construct candidates with heavy filtering, apply (optional) test-set decontamination and internal deduplication via MinHash-LSH, then sample a 10k pool with subset/bucket/source constraints, and finally split out a small validation set. The goal is to produce an RL compatible pool with reduced reward noise and controlled coverage. This process yields the training dataset OpenR1-Stable-10k.

[150] p: We observed that for Qwen2.5-Math (4096 context length), over 99% of generated responses stay below 2500 tokens. Therefore, even with the longest prompts, the total context length remains well, and no special length adjustment beyond the standard prompt filtering is required.

[151] figure: Table 4 . Construction recipe for the OpenR1-Stable-10k training dataset. Item Setting Pool size / Val size 10,000 / 128 Subset ratio default 0.85, extended 0.15 Bucket ratio mixed 0.60, entirely_correct 0.40 (entirely_incorrect retained for robustness) Min generations ≥ 2 \geq 2 Length filters prompt ≤ 4096 \leq 4096 ; response ≤ 4096 \leq 4096 (tokenizer-based) Answer constraints single-value GT enforced; empty GT dropped Boxed-match filter enabled in Stable mode (solution or any generation last \boxed{ } matches answer) Decontam / dedup enabled (MinHash-LSH, num_perm=128, threshold=0.8) Prompt Filter ( ≤ 1024 \leq 1024 ) Applied: drop prompts longer than 1024 tokens (8 samples removed).

[152] h3: A.3. RQ1 Detailed Analysis by Backbone and Scale

[153] p: Here provides a detailed per-backbone and per-scale comparison for RQ1.

[154] p: On Qwen2.5-Math-1.5B, EGPO achieves the best results on four out of five benchmarks. It improves MATH-500 by +50.60% over Base and further exceeds the strongest RL baseline EDGE-GRPO by +2.00%. On MMLU-STEM/Minerva/GSM8K, EGPO also ranks first, surpassing EDGE-GRPO by +1.91%, +3.31%, and +5.15%, respectively. AIME24 is an exception: under the 4096 context length constraint and the 30-problem discreteness (3.33% per solved instance), EGPO is comparable to GRPO/DAPO (13.33%) while EDGE-GRPO solves one additional problem (16.67%).

[155] p: On Qwen2.5-Math-7B, EGPO achieves the best results on all benchmarks. Compared to Base, it delivers large gains, including +70.80% on MATH-500 and +46.04% on MMLU-STEM. It also consistently surpasses the strongest RL baselines: +3.10% on MATH-500 (vs. EDGE-GRPO), +2.91% on AIME24 (vs. EDGE-GRPO), +3.01% on MMLU-STEM (vs. EDGE-GRPO), +3.31% on Minerva (vs. GRPO/EDGE-GRPO), and +3.41% on GSM8K (vs. DAPO).

[156] p: On DeepSeek-R1-1.5B, EGPO achieves the best results across all benchmarks and improves over both Base and RL baselines. It exceeds the strongest RL baselines by +3.35% on MATH-500 (vs. GRPO/DAPO), +6.66% on AIME24 (vs. GRPO/EDGE-GRPO), +4.19% on MMLU-STEM (vs. EDGE-GRPO), +2.57% on Minerva (vs. EDGE-GRPO), and +2.13% on GSM8K (vs. EDGE-GRPO).

[157] p: On DeepSeek-R1-7B, EGPO again achieves the best results across all benchmarks. Notably, some RL baselines provide limited or even negative gains over Base on AIME24 and MMLU-STEM (e.g., GRPO yields -2.09% on AIME24 and -0.16% on MMLU-STEM), whereas EGPO improves them substantially (+10.00% on AIME24 and +6.83% on MMLU-STEM over Base). Against the strongest RL baselines, EGPO further gains +2.00% on MATH-500 (vs. DAPO), +6.67% on AIME24 (vs. DAPO/EDGE-GRPO), +4.77% on MMLU-STEM (vs. EDGE-GRPO), +2.58% on Minerva (vs. EDGE-GRPO), and +2.13% on GSM8K (vs. EDGE-GRPO).

[158] h3: A.4. Additional Analysis: Uncertainty Diagnostics

[159] p: This subsection provides additional uncertainty diagnostics for long-trace reasoning models that expose explicit <think> ​…​ </think> markers, enabling a clean separation between the thinking segment and the final answer segment. Our analysis is conducted on the DeepSeek-R1-Distill-Qwen series. We focus on the NLL-based entropy proxy and evaluate (i) its ability to discriminate correct vs. incorrect rollouts, and (ii) its robustness to response-length variations.

[160] p: Entropy distributions. Figures 6 and 8 visualize kernel density estimates of entropy for correct and incorrect rollouts. Answer-side entropy exhibits a clearer separation: correct rollouts concentrate in low-entropy regions, whereas incorrect rollouts shift toward higher entropy, consistent with the AUC comparison in Table 3 .

[161] p: Not a length proxy. We plot answer length versus answer-side entropy in Fig. 7 and Fig. 9 . We observe no strong monotonic relationship between length and entropy; incorrect rollouts tend to lie above correct ones in entropy at comparable lengths, indicating that the proxy captures content-level uncertainty rather than token-count artifacts.

[162] p: ROC diagnostics. Fig. 5(b) and Fig. 5(a) report ROC curves for predicting incorrectness using entropy signals. Answer-side entropy consistently achieves higher TPR under the same FPR than thinking-side entropy.

[163] p: Supplementary plots. We further visualize: (i) entropy distributions for correct vs. incorrect samples, (ii) the relationship between thinking-side and answer-side entropy, and (iii) answer length vs. answer-side entropy.

[164] figure: (a) DeepSeek-R1-Distill-Qwen-7B (b) DeepSeek-R1-Distill-Qwen-1.5B Figure 5 . ROC diagnostics for predicting incorrect rollouts using entropy on DeepSeek-R1-Distill-Qwen backbones, comparing thinking-side vs. answer-side entropy.

[165] figure: Figure 6 . Entropy distributions for DeepSeek-R1-Distill-Qwen-1.5B (thinking-side vs. answer-side; correct vs. incorrect).

[166] figure: (a) Thinking-side entropy vs. answer-side entropy (DeepSeek-R1-Distill-Qwen-1.5B). (b) Answer length vs. answer-side entropy (DeepSeek-R1-Distill-Qwen-1.5B). Figure 7 . Supplementary scatter plots for DeepSeek-R1-Distill-Qwen-1.5B.

[167] figure: Figure 8 . Entropy distributions for DeepSeek-R1-Distill-Qwen-7B (thinking-side vs. answer-side; correct vs. incorrect).

[168] figure: (a) Thinking-side entropy vs. answer-side entropy (DeepSeek-R1-Distill-Qwen-7B). (b) Answer length vs. answer-side entropy (DeepSeek-R1-Distill-Qwen-7B). Figure 9 . Supplementary scatter plots for DeepSeek-R1-Distill-Qwen-7B.

[169] h2: Instructions for reporting errors

[170] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[171] p: Tip: You can select the relevant text first, to include it in your report.

[172] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[173] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
