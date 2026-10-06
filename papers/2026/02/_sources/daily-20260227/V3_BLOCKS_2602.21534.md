[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning

[3] h6: Abstract

[4] p: Agentic reinforcement learning (ARL) has rapidly gained attention as a promising paradigm for training agents to solve complex, multi-step interactive tasks. Despite encouraging early results, ARL remains highly unstable, often leading to training collapse. This instability limits scalability to larger environments and longer interaction horizons, and constrains systematic exploration of algorithmic design choices. In this paper, we first propose ARLArena , a stable training recipe and systematic analysis framework that examines training stability in a controlled and reproducible setting. ARLArena first constructs a clean and standardized testbed. Then, we decompose policy gradient into four core design dimensions and assess the performance and stability of each dimension. Through this fine-grained analysis, we distill a unified perspective on ARL and propose SAMPO , a stable agentic policy optimization method designed to mitigate the dominant sources of instability in ARL. Empirically, SAMPO achieves consistently stable training and strong performance across diverse agentic tasks. Overall, this study provides a unifying policy gradient perspective for ARL and offers practical guidance for building stable and reproducible LLM-based agent training pipelines.

[5] figure: Figure 1 : Overview of ARLArena . Part 1: A standardized testbed via behavior cloning, format penalty, KL regularization, and hyperparameter search. Part 2: Policy gradient decomposition into four dimensions with representative methods mapped to each. Part 3: Key findings on training stability and collapse modes. Part 4: Insights unified into SAMPO for stable ARL training.

[6] h2: 1 Introduction

[7] p: Large language models (LLMs) have been increasingly deployed as autonomous agents for complex, multi-step interactive tasks spanning web navigation ( Zhou et al., 2024 ) , embodied environments ( Shridhar et al., 2020 ) , games ( Xi et al., 2024 ) , and deep research ( Jin et al., 2025 ; Guan et al., 2025 ) . These tasks demand planning, tool use, and long-horizon decision-making, necessitating training objectives that capture multi-turn interactions. Reinforcement learning (RL) offers a principled post-training framework for this purpose, building on its success in static reasoning tasks ( e.g. , DeepSeek-R1 ( Guo et al., 2025 ) , OpenAI o1 ( Jaech et al., 2024 ) ), and early results in the agentic setting are promising ( Jin et al., 2025 ; Cheng et al., 2025 ; Xi et al., 2024 ) .

[8] figure: Figure 2 : Training curves on ALFWorld (left) and Sokoban (right). SAMPO (ours) achieves the highest success rates on both environments with stable, monotonic improvement throughout training, while baseline methods exhibit varying degrees of instability. These results demonstrate that principled integration of sequence-level clipping, advantage design, and dynamic filtering, as combined in SAMPO, is critical for both training stability and final performance in multi-turn agentic RL.

[9] p: However, agentic RL (ARL) training remains highly unstable and prone to collapse ( Xi et al., 2025 ) . This instability arises from the interactive, multi-turn nature of agentic environments, which introduce compounding challenges such as invalid actions, sparse rewards, long-horizon credit assignment, and non-stationary agent–environment dynamics ( Wang et al., 2025b ; Xu et al., 2026 ) . Small deviations in early decisions can cascade across turns, causing distribution shifts that amplify credit-assignment noise and produce degenerate rollouts ( Xia et al., 2026 ; Xie et al., 2026 ) . Consequently, ARL outcomes are difficult to reproduce across runs and environments, and scaling to longer horizons or more complex interaction spaces remains severely limited ( Abdulhai et al., 2023 ; Xi et al., 2025 ) . These challenges underscore the need for stable and scalable training solutions for ARL.

[10] p: This paper addresses this gap by introducing ARLArena , a stable training recipe and systematic analysis framework for agentic reinforcement learning. We first construct a clean, standardized testbed through format correction, behavior cloning initialization, and KL-based regularization, establishing reliable baseline performance. We then decompose policy-gradient–based RL into four orthogonal design dimensions and evaluate the effectiveness and stability of each across diverse agentic tasks. Each dimension is examined in isolation using representative policy optimization (PO) methods; for methods that exhibit training collapse, we further diagnose the underlying failure modes and develop targeted stabilization strategies.

[11] p: This systematic analysis yields three key findings: (1) tolerant clipping induces training collapse, whereas sequence-level clipping ensures stable improvement; (2) incorporating environment-level information into advantage design improves both stability and performance; and (3) dynamic sampling combined with fine-grained advantage design further benefits ARL training. Motivated by these insights, we propose S table A gentic M ulti-turn P olicy O ptimization ( SAMPO ), a unified PO method that directly addresses the dominant sources of instability identified in our analysis. SAMPO consistently improves training stability and performance, achieving an average 25.2% improvement over the GRPO baseline. We additionally study the impact of off-policy staleness in agentic environments and conduct comparative evaluations against proprietary models, demonstrating the robustness and generality of our approach.

[12] p: In summary, our contributions are: (i) a unifying policy gradient perspective and four-dimensional categorization of PO methods for ARL; (ii) a standardized, reproducible testbed and diagnostic methodology for multi-turn ARL stability; (iii) principled, task-robust findings and remedies for common collapse modes; and (iv) SAMPO, a new PO method that achieves both reliable training and strong final performance. We hope this study provides a foundation for more reproducible and principled progress in LLM agent post-training.

[13] figure: Method Loss Objective Advantage ( A i A_{i} ) IS ( w t w_{t} ) Clipping Dynamical Sampling Adv < 0 <0 Adv > 0 >0 GRPO 1 ∑ i = 1 G T i ​ ∑ i = 1 G ∑ t = 0 T i − 1 min ⁡ ( w t ​ A i , clip ⁡ ( w t , ± ε ) ​ A i ) \displaystyle\frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}\min\!\big(w_{t}\,A_{i},\;\mathrm{clip}(w_{t},1\!\pm\!\varepsilon)A_{i}\big) r i − mean ⁡ ( r i ) std ⁡ ( r i ) \frac{\displaystyle r_{i}-\mathrm{mean}(r_{i})}{\displaystyle\mathrm{std}(r_{i})} { 1 − ε , w t < 1 − ε , w t , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon,&w_{t}<1-\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. { 1 + ε w t > 1 + ε , w t , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon&w_{t}>1+\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. × \times GRPO ST \text{GRPO}_{\texttt{ST}} 1 G ∑ i = 1 G 1 T i ∑ t = 0 T i − 1 \displaystyle\frac{1}{G}\sum_{i=1}^{G}\frac{1}{T_{i}}\sum_{t=0}^{T_{i}-1} min ⁡ ( w t ​ A i , clip ⁡ ( w t , ± ε ) ​ A i ) \min\!\big(w_{t}\,A_{i},\mathrm{clip}(w_{t},1\!\pm\!\varepsilon)A_{i}\big) r i − mean ⁡ ( r i ) std ⁡ ( r i ) \frac{\displaystyle r_{i}-\mathrm{mean}(r_{i})}{\displaystyle\mathrm{std}(r_{i})} { 1 − ε , w t < 1 − ε , w t , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon,&w_{t}<1-\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. { 1 + ε , w t > 1 + ε , w t , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon,&w_{t}>1+\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. × \times GRPO SM \text{GRPO}_{\texttt{SM}} 1 ∑ i = 1 G T i ​ ∑ i = 1 G ∑ t = 0 T i − 1 M i ​ min ⁡ ( w t ​ A i , clip ⁡ ( w t , ± ε ) ​ A i ) M i = [ A i ≥ 0 or 1 | T i | ∑ t = 0 | T i | − 1 log π θ old ​ ( y t | x , y < t ) π θ ​ ( y t | x , y < t ) ≤ δ ] \begin{aligned} \frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}M_{i}\min\!\big(w_{t}\,A_{i},\;\mathrm{clip}(w_{t},1\!\pm\!\varepsilon)A_{i}\big)\\ M_{i}=\mathbf{1}\!\left[A_{i}\geq 0\;\text{or}\;\frac{1}{|T_{i}|}\sum_{t=0}^{|T_{i}|-1}\log\frac{\pi_{\theta_{\texttt{old}}}(y_{t}|x,y_{<t})}{\pi_{\theta}(y_{t}|x,y_{<t})}\leq\delta\right]\end{aligned} r i − mean ⁡ ( r i ) std ⁡ ( r i ) \frac{\displaystyle r_{i}-\mathrm{mean}(r_{i})}{\displaystyle\mathrm{std}(r_{i})} { 1 − ε , w t < 1 − ε , w t , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon,&w_{t}<1-\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. { 1 + ε , w t > 1 + ε , w t , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon,&w_{t}>1+\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. × \times SAPO 1 ∑ i = 1 G T i ​ ∑ i = 1 G ∑ t = 0 T i − 1 f i , t ​ ( w t ) ​ A i \displaystyle\frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}f_{i,t}(w_{t})A_{i} r i − mean ⁡ ( r i ) std ⁡ ( r i ) \frac{\displaystyle r_{i}-\mathrm{mean}(r_{i})}{\displaystyle\mathrm{std}(r_{i})} σ ⁡ ( τ neg ​ ( w t − 1 ) ) ⋅ 4 τ neg \displaystyle\sigma(\tau_{\tiny\text{neg}}(w_{t}-1))\cdot\frac{4}{\tau_{\tiny\text{neg}}} σ ⁡ ( τ pos ​ ( w t − 1 ) ) ⋅ 4 τ pos \displaystyle\sigma(\tau_{\tiny\text{pos}}(w_{t}-1))\cdot\frac{4}{\tau_{\tiny\text{pos}}} × \times CISPO 1 ∑ i = 1 G T i ​ ∑ i = 1 G ∑ t = 0 T i − 1 sg ⁡ ( w t ) ​ A i ​ log ⁡ π θ \displaystyle\frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}\operatorname{sg}(w_{t})A_{i}\log\pi_{\theta} r i − mean ⁡ ( r i ) std ⁡ ( r i ) \frac{\displaystyle r_{i}-\mathrm{mean}(r_{i})}{\displaystyle\mathrm{std}(r_{i})} { 1 − ε low , w t < 1 − ε low , sg ⁡ ( w t ) , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon_{\text{low}},&w_{t}<1-\varepsilon_{\text{low}},\\ \operatorname{sg}(w_{t}),&\text{otherwise}.\end{array}\right. { 1 + ε high , w t > 1 + ε high , sg ⁡ ( w t ) , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon_{\text{high}},&w_{t}>1+\varepsilon_{\text{high}},\\ \operatorname{sg}(w_{t}),&\text{otherwise}.\end{array}\right. × \times GSPO 1 ∑ i = 1 G T i ​ ∑ i = 1 G ∑ t = 0 T i − 1 min ⁡ ( s i ​ A i , clip ⁡ ( s i , ± ε ) ​ A i ) s i = exp ⁡ ( 1 | T i | ​ ∑ t = 0 | T i | − 1 log ⁡ π θ ​ ( y t ∣ x , y < t ) π θ old ​ ( y t ∣ x , y < t ) ) \begin{aligned} \frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}\min\!\big(s_{i}\,A_{i},\;\mathrm{clip}(s_{i},1\!\pm\!\varepsilon)A_{i}\big)\\ s_{i}=\exp\!\Big(\frac{1}{|T_{i}|}\sum_{t=0}^{|T_{i}|-1}\log\frac{\pi_{\theta}(y_{t}\mid x,y_{<t})}{\pi_{\theta_{\texttt{old}}}(y_{t}\mid x,y_{<t})}\Big)\end{aligned} r i − mean ⁡ ( r i ) std ⁡ ( r i ) \frac{\displaystyle r_{i}-\mathrm{mean}(r_{i})}{\displaystyle\mathrm{std}(r_{i})} { 1 − ε , s i < 1 − ε , s i , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon,&s_{i}<1-\varepsilon,\\ s_{i},&\text{otherwise}.\end{array}\right. { 1 + ε , s i > 1 + ε , s i , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon,&s_{i}>1+\varepsilon,\\ s_{i},&\text{otherwise}.\end{array}\right. × \times GIGPO 1 ∑ i = 1 G T i ∑ i = 1 G ∑ t = 0 T i − 1 min ( w t A i , k ′ , clip ( w t , ± ε ) A i , k ′ ) \displaystyle\frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}\min\!\big(w_{t}\,A^{{}^{\prime}}_{i,k},\;\mathrm{clip}(w_{t},1\!\pm\!\varepsilon)A^{{}^{\prime}}_{i,k}\big) A i + ω ⋅ A step ​ ( y ^ i , k ) A_{i}+\omega\cdot A_{\tiny\text{step}}(\hat{y}_{i,k}) { 1 − ε , w t < 1 − ε , w t , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon,&w_{t}<1-\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. { 1 + ε , w t > 1 + ε , w t , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon,&w_{t}>1+\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. × \times EMPG 1 ∑ i = 1 G T i ∑ i = 1 G ∑ t = 0 T i − 1 min ( w t A i ′ , clip ( w t , ± ε ) A i ′ ) \displaystyle\frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}\min\!\big(w_{t}\,A^{{}^{\prime}}_{i},\;\mathrm{clip}(w_{t},1\!\pm\!\varepsilon)A^{{}^{\prime}}_{i}\big) g ⁡ ( H k ) ​ A i + ζ ​ f ​ ( H k + 1 ) \small\color[rgb]{0,0.88,0}{g\big(H_{k}\big)A_{i}+\zeta\,f\big(H_{k+1}\big)} { 1 − ε , w t < 1 − ε , w t , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon,&w_{t}<1-\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. { 1 + ε , w t > 1 + ε , w t , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon,&w_{t}>1+\varepsilon,\\ w_{t},&\text{otherwise}.\end{array}\right. × \times DAPO 1 ∑ i = 1 G T i ​ ∑ i = 1 G ∑ t = 0 T i − 1 min ⁡ ( w t ​ A i , clip ⁡ ( w t , ± ε ) ​ A i ) \displaystyle\frac{1}{\sum_{i=1}^{G}T_{i}}\sum_{i=1}^{G}\sum_{t=0}^{T_{i}-1}\min\!\big(w_{t}\,A_{i},\;\mathrm{clip}(w_{t},1\!\pm\!\varepsilon)A_{i}\big) r i − mean ⁡ ( r i ) std ⁡ ( r i ) \frac{\displaystyle r_{i}-\mathrm{mean}(r_{i})}{\displaystyle\mathrm{std}(r_{i})} { 1 − ε low , w t < 1 − ε low , w t , otherwise . \left\{\begin{array}[]{ll}1-\varepsilon_{\text{low}},&w_{t}<1-\varepsilon_{\text{low}},\\ w_{t},&\text{otherwise}.\end{array}\right. { 1 + ε high , w t > 1 + ε high , w t , otherwise . \left\{\begin{array}[]{ll}1+\varepsilon_{\text{high}},&w_{t}>1+\varepsilon_{\text{high}},\\ w_{t},&\text{otherwise}.\end{array}\right. ✓ Table 1 : A summary of policy optimization methods studied in ARLArena, decomposed along four design dimensions: loss objective formulation, advantage ( A i A_{i} ), importance sampling (IS) clipping, and dynamic sampling. Colored entries highlight distinctive design choices: purple denotes modified loss aggregation (seq-mean-token-mean), violet indicates alternative IS clipping strategies (tolerant or sequence-level), and green marks novel advantage designs. The importance sampling weight is w t = π θ ​ ( y t ∣ x , y < t ) / π θ old ​ ( y t ∣ x , y < t ) w_{t}=\pi_{\theta}(y_{t}\mid x,y_{<t})/\pi_{\theta_{\texttt{old}}}(y_{t}\mid x,y_{<t}) , and sg ⁡ ( ⋅ ) \operatorname{sg}(\cdot) denotes the stop-gradient operator.

[14] h2: 2 Problem Formulation

[15] h3: 2.1 Policy Gradient for Agentic RL

[16] p: During RL optimization for LLMs, the policy π θ \pi_{\theta} generates a response trajectory y = ( y 0 , … , y T ) y=(y_{0},\dots,y_{T}) conditioned on a prompt x x , which is subsequently used for policy updates ( Ouyang et al., 2022 ) . Following PPO-style optimization ( Schulman et al., 2017 ) , trajectories collected under a behavior policy π θ old \pi_{\theta_{\mathrm{old}}} are used to update the current policy π θ \pi_{\theta} . The corresponding policy gradient can be written as:

[17] table: ∇ θ ℒ ​ ( θ ) = 𝔼 y ∼ π θ old ​ [ ∑ t = 0 T w t ​ ( y ) ​ ∇ θ ​ log ⁡ π θ ​ ( y t ∣ x , y < t ) ​ A ​ ( x , y ) ] , {\begin{aligned} \nabla_{\theta}\mathcal{L}(\theta)=\mathbb{E}_{y\sim\pi_{\theta_{\texttt{old}}}}\Bigg[\sum_{t=0}^{T}w_{t}(y)\nabla_{\theta}\log\pi_{\theta}(y_{t}\mid x,y_{<t})\;A(x,y)\Bigg]\end{aligned},} (1)

[18] p: where the importance sampling weight is given by:

[19] table: w t ​ ( y ) = P θ ​ ( y t ∣ x , y < t ) P θ old ​ ( y t ∣ x , y < t ) = π θ ​ ( y t ∣ x , y < t ) π θ old ​ ( y t ∣ x , y < t ) . w_{t}(y)=\frac{P_{\theta}(y_{t}\mid x,y_{<t})}{P_{\theta_{\texttt{old}}}(y_{t}\mid x,y_{<t})}=\frac{\pi_{\theta}(y_{t}\mid x,y_{<t})}{\pi_{\theta_{\texttt{old}}}(y_{t}\mid x,y_{<t})}. (2)

[20] p: Here, A ⁡ ( x , y ) A(x,y) represents the advantage of the sampled sequence.

[21] h5: Agentic RL.

[22] p: An agent interacts with the environment over K K turns, forming a long-horizon decision-making process ( Wei et al., 2026 ; Luo et al., 2026 ) . At each turn, the policy conditions on the accumulated history to generate a response, from which an action is extracted and executed to transition the environment state.

[23] p: The initial user prompt is x ( 1 ) x^{(1)} . At turn k ∈ { 1 , … , K } k\in\{1,\dots,K\} , the policy generates a response y ( k ) ∼ π θ ( ⋅ ∣ x ( k ) ) y^{(k)}\sim\pi_{\theta}(\cdot\mid x^{(k)}) . Given the environment state s ( k ) s^{(k)} , actions a ( k ) a^{(k)} are extracted from y ( k ) y^{(k)} , and the environment transitions to the next state s ( k + 1 ) s^{(k+1)} according to an update function f f : s ( k + 1 ) = f ⁡ ( a ( k ) , s ( k ) ) s^{(k+1)}=f\!\left(a^{(k)},s^{(k)}\right) , where f ⁡ ( ⋅ ) f(\cdot) is the state transition function that incorporates tool calls, environment observations, or retrieved information. The user prompt for turn k + 1 k+1 , denoted x ( k + 1 ) x^{(k+1)} , is constructed from the updated state s ( k + 1 ) s^{(k+1)} . Finally, the complete multi-turn interaction trajectory is defined as τ = ( x ( 1 ) , y ( 1 ) , x ( 2 ) , y ( 2 ) , … , x ( K ) , y ( K ) ) \tau=\bigl(x^{(1)},y^{(1)},x^{(2)},y^{(2)},\dots,x^{(K)},y^{(K)}\bigr) .

[24] p: In the multi-turn agent–environment setting described above, we decompose a K K -turn trajectory into single-turn updates. This yields the following policy gradient formulation for agentic LLM interaction:

[25] table: ∇ θ ℒ ​ ( θ ) = 𝔼 τ ∼ π θ old ​ [ ∑ k = 1 K ∑ t = 0 T k w t ​ ( y ( k ) ) ⏟ IS ​ ∇ θ ​ log ​ π θ ​ ( y t ( k ) ∣ x ( k ) , y < t ( k ) ) ⏟ Log prob ​ A ⁡ ( x ( k ) , y ( k ) ) ⏟ Advantage ] . \nabla_{\theta}\mathcal{L}(\theta)=\color[rgb]{0.75,0,0.25}\mathbb{E}_{\tau\sim\pi_{\theta_{\texttt{old}}}}\color[rgb]{0,0,0}\Big[\color[rgb]{0,0,0}\sum_{k=1}^{K}\sum_{t=0}^{T_{k}}\color[rgb]{0.4336,0.1758,0.6602}\underbrace{w_{t}(y^{(k)})}_{\text{IS}}\color[rgb]{0,1,1}\underbrace{\nabla_{\theta}\log\pi_{\theta}\!\left(y^{(k)}_{t}\mid x^{(k)},y^{(k)}_{<t}\right)}_{\text{Log prob}}\color[rgb]{0,0,0}\,\color[rgb]{0,0.88,0}\underbrace{A(x^{(k)},y^{(k)})}_{\text{Advantage}}\color[rgb]{0,0,0}\Big]. (3)

[26] h3: 2.2 Policy Gradient Decomposition Dimensions

[27] p: According to Equation 3 , the policy gradient formulation for agentic LLMs can be decomposed into four key research dimensions: Loss Aggregation, Importance Sampling (IS) clipping, Trajectory Filtering and Resampling, and Advantage Design. To study each dimension in isolation, we analyze the batch-level loss objective without loss of generality. We summarize mainstream PO algorithms across the different design dimensions of the policy gradient in Table 1 .

[28] h5: Loss Aggregation.

[29] p: In practice, we approximate the loss objective using different loss aggregation schemes.

[30] table: ℒ ⁡ ( θ ) \displaystyle\mathcal{L}(\theta) = 𝔼 y ( i ) ∼ π θ old ​ [ 𝔼 t ​ [ ℓ i , t ​ ( θ ) ] ] \displaystyle=\mathbb{E}_{y^{(i)}\sim\pi_{\theta_{\mathrm{old}}}}\Big[\mathbb{E}_{t}\big[\ell_{i,t}(\theta)\big]\Big] ≜ 1 N ​ ∑ i = 1 N 1 T i ​ ∑ t = 0 T i − 1 ℓ i , t ​ ( θ ) ​ ( seq-mean-token-mean ) \displaystyle\triangleq\color[rgb]{0.75,0,0.25}\frac{1}{N}\sum_{i=1}^{N}\frac{1}{T_{i}}\sum_{t=0}^{T_{i}-1}\color[rgb]{0,0,0}\,\ell_{i,t}(\theta)\;(\text{\small seq-mean-token-mean}) (4) ≜ 1 ∑ i = 1 N T i ∑ i = 1 N ∑ t = 0 T i − 1 ℓ i , t ( θ ) ( token-mean ) , \displaystyle\triangleq\color[rgb]{0.75,0,0.25}\frac{1}{\sum_{i=1}^{N}T_{i}}\sum_{i=1}^{N}\sum_{t=0}^{T_{i}-1}\color[rgb]{0,0,0}\,\ell_{i,t}(\theta)\quad(\text{\small token-mean}), (5)

[31] p: where ℓ i , t ​ ( θ ) := min ⁡ ( w i , t ​ ( θ ) ​ A i , clip ⁡ ( w i , t ​ ( θ ) , 1 − ε , 1 + ε ) ​ A i ) \ell_{i,t}(\theta):=\min\!\big(w_{i,t}(\theta)\,A_{i},\;\mathrm{clip}\big(w_{i,t}(\theta),\,1-\varepsilon,\,1+\varepsilon\big)\,A_{i}\big) . N N denotes the total number of decomposed turns over trajectories. A i A_{i} denotes the advantage of sequence y ( i ) y^{(i)} , and w i , t ​ ( θ ) w_{i,t}(\theta) is the importance sampling ratio at token t t of sequence y ( i ) y^{(i)} . Seq-mean-token-mean weights each token by the inverse of its trajectory length, biasing optimization toward shorter trajectories and potentially introducing response-level length bias. Token-mean assigns equal weight to all unmasked tokens in the batch. Additional aggregation strategies are provided in the Appendix A.1 .

[32] h5: IS Clipping.

[33] p: Clipping methods constrain the magnitude of policy updates by limiting the change in action probabilities relative to the old policy. By constraining the deviation between the new and old policies within a bounded range, clipping mitigates performance degradation and instability caused by excessively large policy updates. The loss objective is formulated as follows:

[34] table: ℒ ⁡ ( θ ) \displaystyle\mathcal{L}(\theta) = 1 ∑ i = 1 N T i ​ ∑ i = 1 N ∑ t = 0 T i − 1 min ⁡ ( w i , t ​ ( θ ) ​ A i , clip ⁡ ( w i , t ​ ( θ ) , ± ε ) ​ A i ) . \displaystyle=\frac{1}{\sum_{i=1}^{N}T_{i}}\sum_{i=1}^{N}\sum_{t=0}^{T_{i}-1}\min\Big(w_{i,t}(\theta)\,A_{i},\;\color[rgb]{0.4336,0.1758,0.6602}{\mathrm{clip}\big(w_{i,t}(\theta),1\!\pm\!\varepsilon\big)}\color[rgb]{0,0,0}\,A_{i}\Big). (6)

[35] p: Within the GRPO ( Guo et al., 2025 ) framework, several clipping variants are considered, including CISPO ( Chen et al., 2025 ) , SAPO ( Gao et al., 2025 ) , and GSPO ( Zheng et al., 2025 ) . CISPO employs a stop-gradient mechanism to avoid hard clipping of out-of-bounds tokens while preserving their gradient information. SAPO adopts a soft-clipping strategy, in which excessively large ratios are smoothly attenuated rather than truncated. GSPO performs clipping by using the sequence-level importance ratio as the clipping criterion. Detailed formulations of these variants are provided in Table 1 and further introduced in Appendix A.2 .

[36] h5: Trajectory Filtering and Resampling.

[37] p: Dynamic sampling addresses inefficiency caused by zero-gradient trajectories in long-horizon agent training ( Yu et al., 2025b ) .

[38] table: ℒ ⁡ ( θ ) \displaystyle\mathcal{L}(\theta) = 1 ∑ i = 1 N T i ​ ∑ i = 1 N ∑ t = 0 T i − 1 min ⁡ ( w i , t ​ ( θ ) ​ A i , clip ⁡ ( w i , t ​ ( θ ) , ± ε ) ​ A i ) , \displaystyle=\frac{1}{\sum_{i=1}^{N}T_{i}}\sum_{i=1}^{N}\sum_{t=0}^{T_{i}-1}\min\Big(w_{i,t}(\theta)\,A_{i},\;\mathrm{clip}\big(w_{i,t}(\theta),1\!\pm\!\varepsilon\big)\,A_{i}\Big), (7) s.t. 0 < | { y ( i ) | is ​ _ ​ equivalent ​ ( a , y ( i ) ) } | < G . \displaystyle\text{s.t.}\quad\color[rgb]{0,1,1}0<\left|\left\{y^{(i)}\;\middle|\;\mathrm{is\_equivalent}(a,y^{(i)})\right\}\right|<G.

[39] p: Here, a a denotes the ground-truth task completion target, and equivalence is determined by whether the agent successfully completes the task. It adaptively filters out trajectories whose sampled output groups receive identical rewards (e.g., all correct or all incorrect) and resamples additional trajectories to increase the proportion of samples with informative gradient signals.

[40] h5: Advantage Design.

[41] p: Multi-turn agentic reinforcement learning introduces additional interaction steps and explicit agent–environment state transitions, which motivates specialized advantage designs. GiGPO ( Feng et al., 2025 ) defines advantages at the state level by grouping actions conditioned on the same preceding environment state and assigning them a shared relative advantage. EMPG ( Wang et al., 2025a ) augments the advantage function with an entropy-dependent term, which modulates the learning signal at each turn to better account for uncertainty across interaction steps. Detailed formulations of these variants are provided in Table 1 and further introduced in Appendix A.3 .

[42] figure: Algorithm Strategy Task Score Success Rate GRPO + Behavior Cloning +\;\text{Behavior Cloning} + + 2.56 + + 20.71 + ℛ format +\;\mathcal{R}_{\text{format}} + + 0.49 + + 7.34 + KL ​ k 3 ​ ( x ) +\;\text{KL}\;k_{3}(x) + + 0.95 + + 18.10 [dashed] GSPO ϵ : e − 2 → e − 3 \epsilon:e^{-2}\rightarrow e^{-3} + + 0.70 + + 3.36 ϵ : e − 3 → e − 4 \epsilon:e^{-3}\rightarrow e^{-4} − - 1.16 − - 9.88 [dashed] DAPO Max_try: 2 → 3 \text{Max\_try: }2\rightarrow 3 + + 0.59 + + 22.15 [dashed] SAPO Temperature: 1 → 2 \text{Temperature: }1\rightarrow 2 − - 1.20 − - 9.85 Temperature: 2 → 3 \text{Temperature: }2\rightarrow 3 − - 0.70 − - 9.20 Table 2: Incremental stabilization strategies for constructing a standardized testbed on ALFWorld, evaluated using GRPO as the base policy optimizer. Each row adds one stabilization technique or adjusts a method-specific hyperparameter. Task Score and Success Rate report the absolute improvement ( + \color[rgb]{0.7,0,0}+ ) or degradation ( − \color[rgb]{0,0.88,0}- ) relative to the preceding configuration.

[43] h2: 3 Experimental Setup

[44] h3: 3.1 Standardized Testbed

[45] p: A primary challenge is constructing a fair and effective testbed for comparing different algorithms. To address this issue, we progressively apply a sequence of stabilization strategies shown in Table 2 . Specifically, we start with behavior cloning, followed by format penalty enforcement and KL regularization when necessary, and finally PO-specific hyperparameter tuning. This process yields a standardized and stable testbed that provides a solid foundation for systematically comparing different policy optimization strategies.

[46] h5: (1) Behavior Cloning.

[47] p: We first perform behavior cloning (BC) on supervised interaction traces to initialize the policy within a reasonable behavioral manifold. Specifically, we construct a multi-turn SFT dataset by deploying the Qwen3 series model ( Yang et al., 2025 ) in the target training environments, collecting self-generated interaction trajectories, and retaining only high-scoring rollouts for supervision. This self-bootstrapped SFT stage initializes the policy within a reasonable behavioral manifold aligned with the environment dynamics.

[48] h5: (2) Format Penalty.

[49] p: We incorporate ℛ format \mathcal{R}_{\text{format}} that enforces structured outputs with explicit <think> </think> and <action> </action> tags. If the generated output violates this format ( e.g. , missing tags, malformed nesting, or extraneous content outside the tags), we apply a fixed penalty to the final reward. This explicit structural constraint provides dense shaping signals during early training and substantially reduces invalid rollouts that would otherwise corrupt policy updates.

[50] h5: (3) Auxiliary KL Loss.

[51] p: Unconstrained updates may cause the policy to drift excessively from the reference model. To regularize policy updates and preserve the pretrained knowledge embedded in the base model, we introduce a KL divergence penalty between the current policy π θ \pi_{\theta} and a reference policy π ref \pi_{\mathrm{ref}} . This constraint encourages conservative policy improvement while still allowing sufficient exploration in the action space. We adopt the commonly used Bregman divergence estimator k 3 k_{3} for KL approximation, which leverages control variates to achieve unbiasedness and low variance ( Schulman, 2017 ) . Specifically, k 3 k_{3} is defined as k 3 ​ ( x ) = δ ⁡ ( x ) − 1 − log ⁡ δ ⁡ ( x ) , k_{3}(x)=\delta(x)-1-\log\delta(x), where δ ⁡ ( x ) = p ⁡ ( x ) q ⁡ ( x ) \delta(x)=\frac{p(x)}{q(x)} denotes the likelihood ratio.

[52] h5: (4) PO-specific Hyper-parameter Grid Search.

[53] p: A natural question is how to ensure that each PO method is fairly evaluated in the multi-turn setting. Our solution is to first run each method with its default configuration, and then perform a PO-specific hyperparameter grid search. We continue tuning until the training trajectory becomes stable, measured by the variance of the success rate over the final 20% of training steps falling below a predefined threshold. As shown in Table 1 , hyperparameters related to IS clipping are particularly sensitive. The best-performing configurations and full results are reported in Appendix B .

[54] h3: 3.2 Tasks and Training Details

[55] p: We adapt ALFWorld ( Shridhar et al., 2020 ) , WebShop ( Yao et al., 2022 ) , Sokoban ( Schrader, 2018 ) , and TIR Math ( Xue et al., 2025 ) as the agentic tasks. Our entire codebase is built upon the verl RL framework ( Sheng and others, 2024 ) . We employ an agentic-loop architecture to coordinate rollouts and environment interactions, after which we segment each complete trajectory into multiple single-turn samples for policy optimization. For mathematical tasks, we use Qwen3-4B-base as the policy model, while for all other tasks we initialize from the SFT-tuned variant Qwen3-4B . For consistency validation, we additionally employed SFT-tuned Qwen3-8B , and the corresponding experimental results are provided in Appendix C . All experiments are conducted on NVIDIA H200 or B200 GPUs. Key hyperparameters and training details are reported in Appendix B .

[56] figure: Dimension Method ALFWorld WebShop Sokoban TIR Math Avg Score Success Score Success Score Success AIME AIME25 Base GRPO 3.70 62.36 75.32 57.71 5.51 83.90 49.96 30.78 46.16 (48.08) Loss Agg GRPO ST \text{GRPO}_{\texttt{ST}} 4.41 ↑ \uparrow 19.2% 72.61 ↑ \uparrow 16.4% 64.57 ↓ \downarrow 14.3% 51.29 ↓ \downarrow 11.1% 3.03 ↓ \downarrow 45.0% 68.73 ↓ \downarrow 18.1% 27.55 ↓ \downarrow 44.9% 21.63 ↓ \downarrow 29.7% 39.23 ↓ \downarrow 15.0% Importance Sampling SAPO 0.80 ↓ \downarrow 78.4% 25.16 ↓ \downarrow 59.7% 73.85 ↓ \downarrow 1.9% 52.10 ↓ \downarrow 9.7% − - 0.23 ↓ \downarrow 104% 30.25 ↓ \downarrow 63.9% 45.00 ↓ \downarrow 9.9% 30.85 ↑ \uparrow 0.2% 32.22 ↓ \downarrow 30.2% CISPO 2.16 ↓ \downarrow 41.6% 54.42 ↓ \downarrow 12.7% 67.96 ↓ \downarrow 9.8% 54.71 ↓ \downarrow 5.2% − - 0.47 ↓ \downarrow 109% 26.02 ↓ \downarrow 69.0% 36.53 ↓ \downarrow 26.9% 30.87 ↑ \uparrow 0.3% 34.03 ↓ \downarrow 26.3% GSPO 5.19 ↑ \uparrow 40.3% 78.61 ↑ \uparrow 26.1% 85.29 ↑ \uparrow 13.3% 72.48 ↑ \uparrow 25.6% 5.22 ↓ \downarrow 5.3% 82.22 ↓ \downarrow 1.7% 51.29 ↑ \uparrow 2.7% 37.95 ↑ \uparrow 23.3% 52.28 ↑ \uparrow 13.3% Advantage Design GIGPO 4.97 ↑ \uparrow 34.3% 81.09 ↑ \uparrow 30.0% 67.76 ↓ \downarrow 10.0% 56.55 ↓ \downarrow 2.0% 5.19 ↓ \downarrow 5.8% 82.67 ↓ \downarrow 1.5% – – 49.71 ↑ \uparrow 3.4% EMPG 3.32 ↓ \downarrow 10.3% 57.91 ↓ \downarrow 7.1% 79.16 ↑ \uparrow 5.1% 64.32 ↑ \uparrow 11.5% 4.48 ↓ \downarrow 18.7% 79.16 ↓ \downarrow 5.6% – – 48.06 ↓ \downarrow 0.1% Dynamic Sampling DAPO GRPO {}_{\text{GRPO}} 1.95 ↓ \downarrow 47.3% 49.58 ↓ \downarrow 20.5% 62.43 ↓ \downarrow 17.1% 46.17 ↓ \downarrow 20.0% 5.16 ↓ \downarrow 6.4% 82.40 ↓ \downarrow 1.8% 54.66 ↑ \uparrow 9.4% 38.97 ↑ \uparrow 26.6% 42.67 ↓ \downarrow 7.6% DAPO GIGPO {}_{\text{GIGPO}} 2.49 ↓ \downarrow 32.7% 60.55 ↓ \downarrow 2.9% 88.10 ↑ \uparrow 17.0% 76.82 ↑ \uparrow 33.1% 6.01 ↑ \uparrow 9.1% 86.20 ↑ \uparrow 2.7% – – 53.36 ↑ \uparrow 11.0% Ours SAMPO 7.04 ↑ \uparrow 90.3% 92.72 ↑ \uparrow 48.7% 88.37 ↑ \uparrow 17.3% 77.73 ↑ \uparrow 34.7% 6.56 ↑ \uparrow 19.1% 88.86 ↑ \uparrow 5.6% – – 60.21 ↑ \uparrow 25.2% Table 3 : Performance comparison of policy optimization methods across four agentic tasks, evaluated on the SFT version of Qwen3-4B. Methods are organized by their primary design dimension: loss aggregation, importance sampling clipping, advantage design, and dynamic sampling. Green/red subscripts denote the percentage improvement/degradation relative to the GRPO baseline. SAMPO (ours) achieves the highest average score (59.55) with consistent gains across ALFWorld (92.72% success), WebShop (74.08% success), and Sokoban (88.86% success). The evaluation metric for TIR Math is Pass@4; “–” indicates the method is not applicable. For GRPO, the value in parentheses reports the average over the first three tasks only.

[57] figure: Figure 3 : Training dynamics of six IS variants on ALFWorld: GRPO, GSPO, SAPO, CISPO, and their sequence-masked counterparts SAPO SM \text{SAPO}_{\texttt{SM}} and CISPO SM \text{CISPO}_{\texttt{SM}} . Panels show (from left to right) success rate, off-policy KL divergence between the current and behavior policies, KL loss between the current and reference policies, gradient norm, and valid-format ratio of rollout actions.

[58] h2: 4 Exploring Gradient Dimensions on ARL

[59] p: The experimental results for all policy optimization methods are reported in Table 3 . GRPO ST \text{GRPO}_{\texttt{ST}} denotes GRPO with sequence-mean-token-mean loss aggregation. DAPO GRPO \text{DAPO}_{\texttt{GRPO}} and DAPO GIGPO \text{DAPO}_{\texttt{GIGPO}} denote GRPO and GIGPO augmented with dynamic filtering, respectively.

[60] h3: 4.1 Impact of IS on ARL

[61] p: We study GSPO, CISPO, and SAPO along the importance-sampling (IS) dimension. GSPO adopts sequence-level clipping, while CISPO and SAPO employ tolerant clipping techniques. For CISPO and SAPO, we further apply sequence masking (denoted as CISPO SM \text{CISPO}_{\texttt{SM}} and SAPO SM \text{SAPO}_{\texttt{SM}} ) to improve training stability. Detailed training dynamics are reported in Figure 3 , with IS token-level and sequence-level analyses presented in Figure 4 .

[62] p: Table 3 shows that CISPO and SAPO perform substantially worse than GRPO across all tasks, achieving average scores of 34.03 and 32.22, respectively, compared to 46.16 for GRPO. In contrast, GSPO consistently outperforms all other policy optimization methods, achieving an average improvement of 13.3% compared to GRPO.

[63] p: To understand training behavior beyond final performance, we analyze training dynamics from multiple perspectives across several metrics. Different IS designs induce varying distances between the current policy and both the behavior and reference policies during training. These distance variations, in turn, influence optimization behavior (reflected by gradient norms), impact data quality (through the valid action ratio), and ultimately affect task success rates. Jointly examining these metrics enables a more comprehensive understanding of training stability and failure modes. Figure 3 reports success rate, off-policy KL divergence (between the new and old policies), KL loss (between the new and reference policies), gradient norm, and the valid-format ratio of rollout action tokens.

[64] p: As shown in Figure 3 , CISPO and SAPO with tolerant clipping exhibit rapid initial performance gains, characterized by higher success rates, larger policy updates relative to the reference model, and faster format ratio adaptation compared to GRPO and GSPO. This behavior indicates more aggressive optimization that departs quickly from the reference policy and adapts rapidly to the task. A possible explanation is that tolerant clipping may preserve gradient contributions from tokens that deviate substantially from the current policy, resulting in overly exploratory updates. However, such aggressiveness leads to training instability, with collapse occurring around step 130. This collapse is marked by exploding gradient norms and KL divergence, accompanied by a sharp drop in the valid-format ratio, ultimately resulting in a severe degradation of success rate. In contrast, GSPO demonstrates a substantially more stable training pattern, with gradual performance improvement accompanied by steady KL divergence and gradient norms. These results indicate that sequence-level clipping is effective for stabilizing training, while overly tolerant clipping thresholds may yield short-term gains at the cost of long-term stability. Furthermore, IS design substantially impacts both performance and training stability in ARL, making it an important dimension in ARL system design.

[65] h5: Rooted cause of training collapse.

[66] figure: Figure 4 : Token-level and sequence-level IS analysis of SAPO and its sequence-masked variant SAPO SM \text{SAPO}_{\texttt{SM}} . (a, b) Fraction of tokens with importance ratios outside the clipping range, decomposed into lower-bound (negative advantage) and upper-bound (positive advantage) portions. (c, d) Rollout groups partitioned by advantage sign, entropy level, and IS ratio magnitude, with KL divergence normalized for relative comparison.

[67] p: To investigate the root causes of training collapse along the IS dimension, we analyze token-level importance ratio statistics and stratify sequences by IS ratio, advantage, and entropy for SAPO and SAPO SM \text{SAPO}_{\texttt{SM}} , where SAPO SM \text{SAPO}_{\texttt{SM}} denotes a stabilized variant of SAPO introduced later. Figure 4 reports token-level and sequence-level IS ratio analysis. Subfigures (a) and (b) present the statistics of tokens whose importance sampling ratios fall outside the standard clipping range. Specifically, we report the proportion of out-of-bounds tokens and decompose it into lower- and upper-bound portions. The lower-bound portion corresponds to negative-advantage tokens with importance ratios below ϵ low \epsilon_{\text{low}} , while the upper-bound portion corresponds to positive-advantage tokens with ratios exceeding ϵ high \epsilon_{\text{high}} .

[68] p: As shown in Figure 4 , During the collapse stage, SAPO exhibits a rapidly growing number of out-of-bounds tokens, predominantly from negative-advantage sequences with small importance ratios (the lower-bound portion) In contrast, for stable training runs, the portion of out-of-bounds tokens remains fairly low, and lower- and upper-bound ratio portions remain relatively balanced. This growing pattern and imbalance during collapse suggests that negative-advantage samples with low IS ratios are the main contributors the observed training instability.

[69] p: Beyond token-level analysis, we conduct a sequence-level comparison across training steps in Subfigures (c) and (d). Rollout samples are partitioned according to three factors: the sign of the advantage, whether the importance ratio is smaller or larger than one, and whether policy entropy falls below or exceeds a predefined threshold. This yields eight groups per training step. The vertical area denotes the normalized KL divergence between the current policy and the reference policy. A larger area therefore corresponds to a greater deviation from the reference policy, indicating a stronger contribution to policy shift during training. For collapsed experiments, the proportion of KL divergence attributed to sequences with negative advantages and low importance ratios increases abruptly, whereas for stable training this KL distribution remains relatively balanced across groups. Entropy is less impactful than advantage and IS ratio. This pattern further reinforces the conclusion that negative-advantage samples with low importance ratios are a primary source of training instability.

[70] h5: Stabilization Strategies for SAPO and CISPO.

[71] p: We explore several strategies to stabilize SAPO and CISPO training, reported in Table 4 . First, we consider increasing the KL coefficient to regularize optimization, and enlarging the mini-update batch size to mitigate off-policy effects. As shown in Table 4 , increasing the KL coefficient overly constrains training and yields limited performance gains (full success-rate plots reported in Appendix C ). Similarly, increasing the mini-update batch size degrades performance. Motivated by the IS-token analysis during training collapse, we adopt sequence masking following ( Liu et al., 2025 ) to directly control negative samples that induce instability. Specifically, sequences with negative advantages and low importance ratios are masked (see Table 1 for the detailed formulation), a variant we denote as GRPO SM \text{GRPO}_{\texttt{SM}} . We apply sequence masking to SAPO and CISPO, denoted as SAPO SM \text{SAPO}_{\texttt{SM}} and CISPO SM \text{CISPO}_{\texttt{SM}} . According to Figure 4 and Table 4 , applying sequence masking improves the success rate from 54.12 to 78.88 for CISPO and from 25.16 to 76.92 for SAPO. SAPO SM \text{SAPO}_{\texttt{SM}} and CISPO SM \text{CISPO}_{\texttt{SM}} effectively stabilizes training, yielding success rates comparable to GSPO, along with steady KL divergence and gradient norms (Figures 3 , 4 ).

[72] figure: Method Metric Original KL (0.05) Off-Policy (1024) Seq-Mask CISPO Score 2.16 1.60 0.98 5.25 Success 54.42 38.46 21.59 78.88 [dashed] SAPO Score 0.80 2.40 3.82 4.88 Success 25.16 48.05 64.30 76.92 Table 4: Effect of different stabilization strategies on CISPO and SAPO in ALFWorld. We evaluate three stabilization techniques applied to the tolerant-clipping methods CISPO and SAPO: increasing the KL penalty coefficient to 0.05, enlarging the off-policy mini-update batch size to 1024, and applying sequence-level masking (Seq-Mask).

[73] h3: 4.2 Impact of Advantage Design on ARL

[74] p: We study GIGPO and EMPG along the advantage-design dimension. GIGPO incorporates both global and local advantage information from the environment, enabling fine-grained advantage estimation, while EMPG reshapes advantages by incorporating uncertainty information from the training data.

[75] p: Table 3 shows that GIGPO generally outperforms GRPO, achieving an average score of 49.71 compared to 48.08, with a particularly strong improvement of 34.4% on ALFWorld. In addition, EMPG exhibits task-dependent performance, improving the success rate on WebShop by 11.5% while degrading performance on ALFWorld by 7.1%, resulting in an average score difference of 0.1 compared to GRPO. This suggests that fine-grained advantage design incorporating richer environmental information improves performance and alleviates reward sparsity in ARL, whereas advantage reshaping based on uncertainty signals has a smaller effect.

[76] h3: 4.3 Impact of Dynamic Filtering on ARL

[77] p: Dynamic filtering is well known for delivering strong performance improvements on mathematical reasoning tasks ( Yu et al., 2025b ; Xue et al., 2025 ) . However, we find that these gains do not always transfer to agentic reinforcement learning settings. As shown in Table 3 , dynamic filtering improves performance more consistently when combined with GIGPO than with GRPO. This difference stems from how dynamic filtering interacts with format learning. In early training, many rollout groups fail entirely due to format errors, which amplifies the format penalty and produces strong implicit advantage signals for format correction. As a result, the model rapidly acquires correct formatting from early rollouts. Meanwhile, dynamic filtering removes such all-failure groups. For GRPO, whose advantage signals have limited diversity, filtering substantially reduces format-related learning signals, leading to unstable format behavior and limited gains. In contrast, GIGPO produces more diverse advantage signals, which stabilize format learning even after filtering, allowing DAPO GIGPO \text{DAPO}_{\texttt{GIGPO}} to achieve better and more stable performance. The detailed evidence supporting the above analyses is provided in Appendix G .

[78] h3: 4.4 Impact of Loss Aggregation on ARL

[79] p: As shown in Table 3 , sequence-mean-token-mean loss aggregation ( GRPO ST \text{GRPO}_{\texttt{ST}} ) degrades performance from 46.16 to 39.23 relative to token-mean aggregation (GRPO). Although GRPO ST \text{GRPO}_{\texttt{ST}} yields a 16.4% improvement on ALFWorld, it leads to a substantial decline on TIR-Math, with a 44.9% decrease on AIME. Notably, math rollouts exhibit higher variance in sequence length compared to other tasks, ranging from brief solutions to extended reasoning traces. These findings suggest that the unbalanced token weighting induced by sequence-level aggregation may negatively affect ARL training, particularly in tasks characterized by high length variability.

[80] h3: 4.5 Further Stability Considerations

[81] figure: ALFWorld Math Degree Score Success AIME AIME25 k@1 k@32 k@1 k@32 Low 3.50 60.80 26.95 87.34 24.61 50.00 Medium 3.83 58.38 24.22 75.00 17.97 48.59 High 2.33 52.71 19.53 74.99 16.41 43.85 Table 5: Effect of off-policy staleness on ALFWorld and MATH. We vary the degree of off-policy staleness (Low, Medium, High) and report task score, success rate (ALFWorld), and pass@ k k accuracy (AIME, AIME25).

[82] h5: Exploration on Off-Policy Staleness.

[83] p: Due to infrastructure and efficiency constraints, policy training is typically performed in batched rollouts, where groups of trajectories are generated and updated sequentially before proceeding to the next rollout stage. Off-policy effects arise because later updates within the same rollout stage use data from an earlier policy while the current policy has already evolved. Such off-policy mismatch is further amplified in multi-turn settings, where turn-wise decomposition increases the number of samples subject to staleness.

[84] h5: Experiment Setup and Results.

[85] p: We control off-policy degree through rollout configuration while holding the update batch size fixed. For TIR Math, rollout batch sizes of 128, 512, and 1024 correspond to low, medium, and high off-policy degrees, respectively. For ALFWorld, we vary the off-policy degree by adjusting the number of groups per rollout to 8, 16, and 32. The effects of off-policy staleness are summarized in Table 5 . TIR Math achieves higher performance under a low off-policy ratio (rollout batch size = 128), with 87.34% and 50.00% for avg@32 , compared to 74.99% and 43.85% under a high off-policy ratio. Similarly, ALFWorld attains its highest success rate of 60.80% under low off-policy settings, which decreases to 52.71% under high off-policy settings. These results suggest that policy gradient optimization for agentic tasks exhibits sensitivity to the off-policy ratio.

[86] h2: 5 SAMPO

[87] h3: 5.1 Motivation

[88] p: Can we derive a unified understanding of ARL training based on these insights? By systematically analyzing POs along orthogonal design dimensions in ARL, we identify key factors that determine training stability and optimization efficacy. At initialization, formatting errors and invalid action tokens induce severe optimization noise. We eliminate these failure modes through behavior cloning and explicit format correction, constraining learning to a valid behavioral manifold. Along the importance sampling dimension, sequence-level clipping, rather than token-wise constraints, is critical for long-horizon ARL. This mechanism addresses off-policy drift by suppressing harmful trajectories and yields substantial improvements in training stability. For advantage design, our analysis reveals that increasing advantage diversity across finer scales is essential to overcoming reward sparsity. Integrating global and local signals significantly enhances credit assignment. Finally, we show that dynamic trajectory filtering helps stabilize gradient updates by removing samples with degenerate advantages, leading to more informative and effective policy gradients.

[89] h3: 5.2 Our Method

[90] p: Guided by this unified understanding, we propose SAMPO, a new PO paradigm built on these principles. SAMPO integrates sequence-level clipping, fine-grained advantage estimation, and dynamic filtering into a unified framework, yielding a stable and scalable solution for ARL. It is formulated as:

[91] table: ℒ ⁡ ( θ ) \displaystyle\mathcal{L}(\theta) = 1 ∑ i = 1 N T i ∑ i = 1 N ∑ t = 0 T i − 1 min ( s i ( θ ) A i ′ , clip ( s i ( θ ) , ± ε ) A i ′ ) , \displaystyle=\frac{1}{\sum_{i=1}^{N}T_{i}}\sum_{i=1}^{N}\sum_{t=0}^{T_{i}-1}\min\Big(s_{i}(\theta)\,A_{i}^{{}^{\prime}},\;\mathrm{clip}\big(s_{i}(\theta),1\!\pm\!\varepsilon\big)\,A_{i}^{{}^{\prime}}\Big), (8) s.t. 0 < | { y | is ​ _ ​ equivalent ​ ( a , y ) } | < G . \displaystyle\text{s.t.}\quad 0<\left|\left\{y\;\middle|\;\mathrm{is\_equivalent}(a,y)\right\}\right|<G.

[92] p: Here, A i , k ′ = A i + ω ⋅ A step ( y ^ i , k ) A_{i,k}^{{}^{\prime}}=A_{i}+\omega\cdot A_{\tiny\text{step}}(\hat{y}_{i,k}) , s i ​ ( θ ) = exp ⁡ ( 1 | T i | ​ ∑ t = 0 | T i | − 1 log ⁡ π θ ​ ( y t ∣ x , y < t ) π θ old ​ ( y t ∣ x , y < t ) ) s_{i}(\theta)=\exp\!\Big(\frac{1}{|T_{i}|}\sum_{t=0}^{|T_{i}|-1}\log\frac{\pi_{\theta}(y_{t}\mid x,y_{<t})}{\pi_{\theta_{\texttt{old}}}(y_{t}\mid x,y_{<t})}\Big) . Across all evaluated agentic tasks, SAMPO consistently achieves the strongest overall performance shown in Table 1 . Compared to methods that modify only one dimension, SAMPO demonstrates that combining multiple design dimensions is necessary for stable and effective ARL. Notably, SAMPO delivers particularly large improvements on long-horizon interactive tasks such as ALFWorld, highlighting the importance of sequence-aware control in agentic settings. These results validate our central claim that stable agentic PO method requires satisfying multiple necessary conditions simultaneously, rather than relying on isolated algorithmic modifications.

[93] h3: 5.3 Benchmarking against Inference Paradigms

[94] p: To further contextualize the performance of SAMPO and evaluate whether a small open-source model trained with stable RL can compete with state-of-the-art inference strategies, we benchmark ARLArena against frontier closed-source models and complex multi-agent workflows. This comparison verifies a key hypothesis: principled RL training may offer greater gains in agentic tasks than heavy inference-time engineering on generic models.

[95] h5: Experiment Setup and Results.

[96] p: We evaluate GPT-5.2 ( OpenAI, 2025a ) , o3 ( OpenAI, 2025b ) , and Gemini 2.5 Pro ( Comanici et al., 2025 ) on ALFWorld and WebShop, under two paradigms: (i) Single LLM as Agent (SLA), following a standardized protocol; (ii) Multi-Agent System (MAS), with Debate and Aggressive Debate coordination strategies (details in Appendix F.5 ). Qwen3-4B-RFT post-trained with SAMPO achieves 92.72% all-task success on ALFWorld, outperforming GPT-5.2 (51.56%) and o3-based MAS (56.25%). Open-source models with SAMPO consistently exceed larger closed-source models, showing that scale and complex inference cannot replace stable, environment-aligned ARL training.

[97] h2: 6 Insights for Future Work

[98] p: Based on our systematic dissection of policy gradient design choices in ARL, we identify several promising directions that merit deeper exploration.

[99] h5: (1) Clean training recipes are foundational for complex reasoning.

[100] p: ARLArena reveals that ARL is extraordinarily sensitive to initialization and early-stage training dynamics. A carefully constructed clean setting, combining short supervised cold-start SFT, format-enforcing structural constraints, and conservative KL regularization, proves essential for unlocking stable multi-turn reasoning behaviors. Without such a controlled recipe, policy gradient signals are easily corrupted by malformed trajectories or premature collapse. This suggests that future research should treat training recipes not as auxiliary tricks, but as essential algorithmic components that define the feasible region in which sophisticated reasoning policies can emerge. Our codebase also provides detailed training recipes for reference.

[101] h5: (2) IS clipping is highly sensitive, while advantage design offers a comparatively stable gain.

[102] p: Among the policy gradient dimensions we examine, IS clipping strategies exhibit high sensitivity: minor changes in clipping thresholds or ratio parameterization can drastically affect stability. In contrast, advantage design tends to provide more stable but relatively modest improvements across tasks. These observations indicate that IS clipping strategy represents a high-risk, high-reward direction, whereas advantage design offers a more predictable but limited performance gains in ARL.

[103] h5: (3) Stable ARL unlocks long-horizon scaling opportunities.

[104] p: Once training collapse is mitigated, we observe that agentic policies can sustain performance improvements over substantially more optimization steps without degradation. This stability opens the door to scaling both interaction horizon and environment size, analogous to scaling laws in supervised pretraining. Consequently, future progress in the field will increasingly depend on scaling environment diversity, interaction data volume, and multi-task curricula.

[105] h2: 7 Conclusion

[106] p: This work systematically analyzes how policy gradient design choices impact training stability for agentic LLMs in multi-turn environments. ARLArena demonstrates that sequence-level clipping is critical for stability, while advantage design and dynamic filtering offer smaller but consistent gains, and loss aggregation has limited effect. Based on these insights, we introduce SAMPO , a unified policy optimization framework that achieves stable and effective agentic RL training. Overall, this study underscores the importance of principled policy design and reproducible evaluation for advancing ARL.

[107] h2: References

[108] p: Supplementary Materials for ARLArena

[109] h2: Appendix A More Details on Research Dimension

[110] h3: A.1 Loss Aggregation

[111] p: As discussed in Section 2.2 , the policy gradient objective for agentic LLMs is implemented through a batch-level loss aggregation over token-level surrogate losses. For a batch of N N sampled trajectories { y i } i = 1 N \{y_{i}\}_{i=1}^{N} , where trajectory i i has length T i T_{i} , we define the token-level loss as

[112] table: ℓ i , t ​ ( θ ) := min ⁡ ( w i , t ​ ( θ ) ​ A i , clip ⁡ ( w i , t ​ ( θ ) , 1 − ε , 1 + ε ) ​ A i ) , \ell_{i,t}(\theta)\;:=\;\min\!\left(w_{i,t}(\theta)A_{i},\;\mathrm{clip}\!\left(w_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)A_{i}\right), (S1)

[113] p: where w i , t ​ ( θ ) = π θ ​ ( y i , t ∣ x i , y i , < t ) / π θ old ​ ( y i , t ∣ x i , y i , < t ) w_{i,t}(\theta)=\pi_{\theta}(y_{i,t}\mid x_{i},y_{i,<t})/\pi_{\theta_{\texttt{old}}}(y_{i,t}\mid x_{i},y_{i,<t}) and A i A_{i} denotes the (sequence-level) advantage associated with trajectory y i y_{i} .

[114] p: Different loss aggregation strategies correspond to different empirical estimators of the expectation over trajectories and tokens. Below we summarize several commonly used schemes.

[115] h5: Token-mean.

[116] p: The token-mean estimator averages the loss uniformly over all unmasked tokens in the batch:

[117] table: ℒ token-mean ​ ( θ ) = 1 ∑ i = 1 N T i ​ ∑ i = 1 N ∑ t = 0 T i − 1 ℓ i , t ​ ( θ ) . \mathcal{L}_{\text{token-mean}}(\theta)\;=\;\frac{1}{\sum_{i=1}^{N}T_{i}}\sum_{i=1}^{N}\sum_{t=0}^{T_{i}-1}\ell_{i,t}(\theta). (S2)

[118] p: This scheme assigns equal weight to each token across the entire batch and is invariant to trajectory length at the sequence level. Token-mean has been adopted in several recent works (e.g., DAPO) as a means of stabilizing optimization. However, because trajectories with longer responses contribute more tokens, they implicitly receive larger total weight, which may bias optimization toward long trajectories.

[119] h5: Sequence-mean token-mean (Seq-mean-token-mean).

[120] p: This estimator first averages over tokens within each trajectory and then averages across trajectories:

[121] table: ℒ seq-mean-token-mean ​ ( θ ) = 1 N ​ ∑ i = 1 N 1 T i ​ ∑ t = 0 T i − 1 ℓ i , t ​ ( θ ) . \mathcal{L}_{\text{seq-mean-token-mean}}(\theta)\;=\;\frac{1}{N}\sum_{i=1}^{N}\frac{1}{T_{i}}\sum_{t=0}^{T_{i}-1}\ell_{i,t}(\theta). (S3)

[122] p: Under this scheme, each trajectory contributes equally regardless of its length. Equivalently, each token is weighted by 1 / T i 1/T_{i} . As a result, shorter trajectories assign larger per-token weight, while longer trajectories are relatively down-weighted. This behavior can introduce response-level length bias, rewarding short correct trajectories more strongly and penalizing long incorrect trajectories less.

[123] h5: Sequence-mean token-sum (Seq-mean-token-sum).

[124] p: An alternative aggregation removes the per-trajectory normalization over tokens:

[125] table: ℒ seq-mean-token-sum ​ ( θ ) = 1 N ​ ∑ i = 1 N ∑ t = 0 T i − 1 ℓ i , t ​ ( θ ) . \mathcal{L}_{\text{seq-mean-token-sum}}(\theta)\;=\;\frac{1}{N}\sum_{i=1}^{N}\sum_{t=0}^{T_{i}-1}\ell_{i,t}(\theta). (S4)

[126] p: This formulation corresponds to maximizing the expected cumulative surrogate objective over full trajectories. Compared to Seq-mean-token-mean, longer trajectories receive proportionally larger weight.

[127] h5: Sequence-mean token-sum with length normalization (Seq-mean-token-sum-norm).

[128] p: In practice, some implementations normalize by a fixed maximum generation length T max T_{\max} :

[129] table: ℒ seq-mean-token-sum-norm ​ ( θ ) = 1 N ​ T max ​ ∑ i = 1 N ∑ t = 0 T i − 1 ℓ i , t ​ ( θ ) . \mathcal{L}_{\text{seq-mean-token-sum-norm}}(\theta)\;=\;\frac{1}{NT_{\max}}\sum_{i=1}^{N}\sum_{t=0}^{T_{i}-1}\ell_{i,t}(\theta). (S5)

[130] p: This estimator enforces a uniform upper bound on the contribution of each trajectory and assigns equal weight to tokens across batches under a fixed-length budget.

[131] h5: Discussion.

[132] p: These aggregation schemes differ primarily in how they trade off trajectory-level fairness, token-level weighting, and variance control. Seq-mean-token-mean and token-mean are the two most commonly used estimators in practice and are the focus of our empirical analysis in Section 4.4 . The remaining variants are included here for completeness and to clarify their implicit inductive biases in agentic reinforcement learning.

[133] h3: A.2 Importance Sampling Clipping

[134] p: As discussed in Section 2.2 , importance sampling (IS) clipping plays a central role in stabilizing off-policy policy optimization. While all methods considered in this work rely on the same token-level importance ratio

[135] table: w i , t ​ ( θ ) = π θ ​ ( y i , t ∣ x i , y i , < t ) π θ old ​ ( y i , t ∣ x i , y i , < t ) , w_{i,t}(\theta)=\frac{\pi_{\theta}(y_{i,t}\mid x_{i},y_{i,<t})}{\pi_{\theta_{\texttt{old}}}(y_{i,t}\mid x_{i},y_{i,<t})}, (S6)

[136] p: they differ substantially in where and how clipping is applied. Below we summarize the clipping mechanisms of GRPO, CISPO, SAPO, and GSPO.

[137] h4: A.2.1 GRPO

[138] p: Group Relative Policy Optimization (GRPO) adopts the standard PPO-style hard clipping applied independently at each token:

[139] table: ℓ i , t GRPO ​ ( θ ) = min ⁡ ( w i , t ​ ( θ ) ​ A i , clip ⁡ ( w i , t ​ ( θ ) , 1 − ε , 1 + ε ) ​ A i ) . \ell_{i,t}^{\text{GRPO}}(\theta)=\min\!\left(w_{i,t}(\theta)A_{i},\;\mathrm{clip}\!\left(w_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)A_{i}\right). (S7)

[140] p: Clipping is performed directly on the token-level importance ratio. When w i , t w_{i,t} falls outside the clipping range, the gradient contribution of that token is truncated.

[141] h4: A.2.2 CISPO

[142] p: Clipped Importance Sampling Policy Optimization (CISPO) modifies GRPO by clipping the importance ratio itself rather than the surrogate objective. Specifically, the clipped ratio is defined as

[143] table: w ~ i , t ​ ( θ ) = { 1 + ε , w i , t ​ ( θ ) > 1 + ε , w i , t ​ ( θ ) , otherwise , \tilde{w}_{i,t}(\theta)=\begin{cases}1+\varepsilon,&w_{i,t}(\theta)>1+\varepsilon,\\ w_{i,t}(\theta),&\text{otherwise},\end{cases} (S8)

[144] p: and is treated as a stop-gradient quantity. The resulting loss takes the form

[145] table: ℓ i , t CISPO ​ ( θ ) = sg ⁡ ( w ~ i , t ​ ( θ ) ) ​ A i ​ log ⁡ π θ ​ ( y i , t ∣ x i , y i , < t ) , \ell_{i,t}^{\text{CISPO}}(\theta)=\mathrm{sg}\!\left(\tilde{w}_{i,t}(\theta)\right)\,A_{i}\,\log\pi_{\theta}(y_{i,t}\mid x_{i},y_{i,<t}), (S9)

[146] p: where sg ⁡ ( ⋅ ) \mathrm{sg}(\cdot) denotes the stop-gradient operator. By avoiding hard truncation of token updates, CISPO preserves gradient flow for clipped tokens while still bounding their influence. However, clipping remains token-local and does not explicitly enforce sequence-level coherence.

[147] h4: A.2.3 SAPO

[148] p: Soft Adaptive Policy Optimization (SAPO) replaces hard clipping with a smooth, temperature-controlled gating function. The surrogate loss is defined as

[149] table: ℓ i , t SAPO ​ ( θ ) = f i , t ​ ( w i , t ​ ( θ ) ) ​ A i , \ell_{i,t}^{\text{SAPO}}(\theta)=f_{i,t}\!\left(w_{i,t}(\theta)\right)A_{i}, (S10)

[150] p: where

[151] table: f i , t ​ ( x ) = σ ⁡ ( τ i , t ​ ( x − 1 ) ) ⋅ 4 τ i , t , τ i , t = { τ pos , A i > 0 , τ neg , A i < 0 . f_{i,t}(x)=\sigma\!\bigl(\tau_{i,t}(x-1)\bigr)\cdot\frac{4}{\tau_{i,t}},\qquad\tau_{i,t}=\begin{cases}\tau_{\text{pos}},&A_{i}>0,\\ \tau_{\text{neg}},&A_{i}<0.\end{cases} (S11)

[152] p: Here σ ⁡ ( ⋅ ) \sigma(\cdot) denotes the sigmoid function. SAPO implements a continuous trust region: near on-policy updates are preserved, while off-policy updates are smoothly attenuated rather than abruptly clipped. The asymmetric temperature design further suppresses high-variance negative-advantage updates. Despite improved smoothness, SAPO remains a token-level method and does not explicitly prevent a few extreme tokens from destabilizing a full trajectory.

[153] h4: A.2.4 GSPO

[154] p: Group Sequence Policy Optimization (GSPO) fundamentally changes the unit of clipping by operating at the sequence level. The sequence-level importance ratio is defined as

[155] table: s i ​ ( θ ) = exp ⁡ ( 1 T i ​ ∑ t = 0 T i − 1 log ⁡ w i , t ​ ( θ ) ) = ( π θ ​ ( y i ∣ x i ) π θ old ​ ( y i ∣ x i ) ) 1 / T i . s_{i}(\theta)=\exp\!\left(\frac{1}{T_{i}}\sum_{t=0}^{T_{i}-1}\log w_{i,t}(\theta)\right)=\left(\frac{\pi_{\theta}(y_{i}\mid x_{i})}{\pi_{\theta_{\texttt{old}}}(y_{i}\mid x_{i})}\right)^{\!1/T_{i}}. (S12)

[156] p: Clipping is then applied once per sequence:

[157] table: ℓ i GSPO ​ ( θ ) = min ⁡ ( s i ​ ( θ ) ​ A i , clip ⁡ ( s i ​ ( θ ) , 1 − ε , 1 + ε ) ​ A i ) . \ell_{i}^{\text{GSPO}}(\theta)=\min\!\left(s_{i}(\theta)A_{i},\;\mathrm{clip}\!\left(s_{i}(\theta),1-\varepsilon,1+\varepsilon\right)A_{i}\right). (S13)

[158] p: All tokens within a trajectory share the same clipped update. This design aligns the unit of importance sampling with the unit of reward and enforces strong sequence-level coherence. As a result, GSPO effectively suppresses high-variance token outliers and yields substantially more stable optimization in long-horizon agentic reinforcement learning.

[159] h5: Summary.

[160] p: In summary, GRPO, CISPO, and SAPO apply clipping at the token level with increasing degrees of smoothness, whereas GSPO performs clipping at the sequence level. Our empirical results in Section 4.1 demonstrate that sequence-level clipping is a key factor for stabilizing multi-turn agentic RL training.

[161] h3: A.3 Advantage Design

[162] p: This section provides detailed formulations of the advantage designs introduced in Section 2.2 , including Group-in-Group Policy Optimization (GiGPO) and Entropy-Modulated Policy Gradients (EMPG). Both methods extend standard group-based advantage estimation to better handle long-horizon agentic reinforcement learning.

[163] h5: Notation.

[164] p: We consider a batch of N N trajectories { τ i } i = 1 N \{\tau_{i}\}_{i=1}^{N} , where each trajectory τ i = { ( s i , k , a i , k , r i , k ) } k = 1 K i \tau_{i}=\{(s_{i,k},a_{i,k},r_{i,k})\}_{k=1}^{K_{i}} is generated under the behavior policy π θ old \pi_{\theta_{\texttt{old}}} . The total return of a trajectory is denoted by

[165] table: R ⁡ ( τ i ) = ∑ t = 1 T i r i , k . R(\tau_{i})=\sum_{t=1}^{T_{i}}r_{i,k}. (S14)

[166] h4: A.3.1 Group-in-Group Policy Optimization (GiGPO)

[167] p: GiGPO introduces a hierarchical advantage structure that combines trajectory-level and step-level relative advantages. The design preserves the critic-free and group-based nature of GRPO while enabling finer-grained credit assignment.

[168] h5: Episode-level relative advantage.

[169] p: GiGPO first computes a trajectory-level (episode-level) relative advantage by normalizing total returns within the rollout group:

[170] table: A i = R ⁡ ( τ i ) − mean ⁡ ( { R ⁡ ( τ j ) } j = 1 N ) F norm ​ ( { R ⁡ ( τ j ) } j = 1 N ) , A_{i}=\frac{R(\tau_{i})-\mathrm{mean}\left(\{R(\tau_{j})\}_{j=1}^{N}\right)}{F_{\mathrm{norm}}\left(\{R(\tau_{j})\}_{j=1}^{N}\right)}, (S15)

[171] p: where F norm ​ ( ⋅ ) F_{\mathrm{norm}}(\cdot) is a normalization factor. In the original formulation, F norm F_{\mathrm{norm}} may be chosen as the standard deviation or a fixed constant.

[172] h5: Step-level relative advantage via anchor state grouping.

[173] p: To assign fine-grained credit within a trajectory, GiGPO constructs step-level groups based on repeated environment states. Let 𝒰 \mathcal{U} denote the set of distinct environment states appearing in the trajectory batch. For each anchor state s ~ ∈ 𝒰 \tilde{s}\in\mathcal{U} , a step-level group is defined as

[174] table: 𝒢 S ​ ( s ~ ) = { ( a i , k , R i , k ) | s i , k = s ~ } , \mathcal{G}_{S}(\tilde{s})=\left\{\bigl(a_{i,k},R_{i,k}\bigr)\;\middle|\;s_{i,k}=\tilde{s}\right\}, (S16)

[175] p: where R i , k R_{i,k} denotes the discounted return from step k k reward:

[176] table: R i , k = ∑ m = t T i γ m − t ​ r i , m . R_{i,k}=\sum_{m=t}^{T_{i}}\gamma^{m-t}r_{i,m}. (S17)

[177] p: Within each step-level group, GiGPO computes a relative advantage for individual actions:

[178] table: A step ​ ( y ^ i , k ) = R i , k − mean ⁡ ( { R j , k ′ ∣ ( a j , k ′ , R j , k ′ ) ∈ 𝒢 S ​ ( s ~ ) } ) F norm ​ ( { R j , k ′ ∣ ( a j , k ′ , R j , k ′ ) ∈ 𝒢 S ​ ( s ~ ) } ) . A_{\text{step}}(\hat{y}_{i,k})=\frac{R_{i,k}-\mathrm{mean}\left(\{R_{j,k^{\prime}}\mid(a_{j,k^{\prime}},R_{j,k^{\prime}})\in\mathcal{G}_{S}(\tilde{s})\}\right)}{F_{\mathrm{norm}}\left(\{R_{j,k^{\prime}}\mid(a_{j,k^{\prime}},R_{j,k^{\prime}})\in\mathcal{G}_{S}(\tilde{s})\}\right)}. (S18)

[179] h5: Combined advantage.

[180] p: The final advantage used for policy optimization is a linear combination of episode-level and step-level components:

[181] table: A i , k ′ = A i + ω A step ( y i , k ) , A^{{}^{\prime}}_{i,k}=A_{i}+\omega\,A_{\text{step}}(y_{i,k}), (S19)

[182] p: where ω ≥ 0 \omega\geq 0 is a weighting coefficient controlling the contribution of step-level credit.

[183] h4: A.3.2 Entropy-Modulated Policy Gradients (EMPG)

[184] p: Entropy-Modulated Policy Gradients (EMPG) augments the advantage function by incorporating step-wise uncertainty measured via policy entropy. The method reshapes the learning signal at each decision step while preserving a trajectory-level optimization objective, making it suitable for long-horizon agentic reinforcement learning.

[185] h5: Step-level entropy.

[186] p: For a trajectory τ i \tau_{i} and its t t -th step, EMPG defines a step-level entropy H i , t H_{i,t} as the average token-level entropy over the tokens generated at that step:

[187] table: H i , t = − 1 | y i , t | ∑ j = 1 | y i , t | ∑ v ∈ 𝒱 π θ ( v ∣ y i , t , < j ) log π θ ( v ∣ y i , t , < j ) , H_{i,t}=-\frac{1}{|y_{i,t}|}\sum_{j=1}^{|y_{i,t}|}\sum_{v\in\mathcal{V}}\pi_{\theta}\!\left(v\mid y_{i,t,<j}\right)\log\pi_{\theta}\!\left(v\mid y_{i,t,<j}\right), (S20)

[188] p: where | y i , t | |y_{i,t}| is the number of tokens in step t t , y i , t , < j y_{i,t,<j} denotes the prefix before token j j within that step, and 𝒱 \mathcal{V} is the vocabulary.

[189] h5: Entropy-modulated advantage.

[190] p: Let A ⁡ ( τ i ) A(\tau_{i}) denote the trajectory-level advantage (e.g., computed via group-based normalization as described in Section 2.2 ). EMPG defines a step-wise modulated advantage as

[191] table: A mod ​ ( i , t ) = g ⁡ ( H i , t ) ​ A ​ ( τ i ) + ζ ​ f ​ ( H i , t + 1 ) , A_{\mathrm{mod}}(i,t)=g\!\left(H_{i,t}\right)\,A(\tau_{i})\;+\;\zeta\,f\!\left(H_{i,t+1}\right), (S21)

[192] p: where g ⁡ ( ⋅ ) g(\cdot) is a self-calibrating scaling function based on current-step entropy, f ⁡ ( ⋅ ) f(\cdot) is a future-clarity bonus depending on the next step, and ζ ≥ 0 \zeta\geq 0 controls the contribution of the future-clarity term.

[193] h5: Self-calibrating gradient scaling.

[194] p: The scaling function g ⁡ ( ⋅ ) g(\cdot) reweights the trajectory-level advantage according to the relative entropy of each step within a batch:

[195] table: g ⁡ ( H i , t ) = exp ⁡ ( − k ​ H ~ i , t ) 1 ∑ j T j ​ ∑ j , t ′ exp ⁡ ( − k ​ H ~ j , t ′ ) , g\!\left(H_{i,t}\right)=\frac{\exp\!\left(-k\,\tilde{H}_{i,t}\right)}{\frac{1}{\sum_{j}T_{j}}\sum_{j,t^{\prime}}\exp\!\left(-k\,\tilde{H}_{j,t^{\prime}}\right)}, (S22)

[196] p: where H ~ i , t \tilde{H}_{i,t} denotes a batch-normalized entropy value, T j T_{j} is the length of trajectory τ j \tau_{j} , and k > 0 k>0 is a temperature parameter. This normalization ensures that the average scaling factor over the batch equals one.

[197] h5: Future clarity bonus.

[198] p: To encourage transitions toward lower-uncertainty future states, EMPG introduces a future-clarity bonus defined as

[199] table: f ⁡ ( H i , t + 1 ) = exp ⁡ ( − k ′ ​ H ~ i , t + 1 ) , f\!\left(H_{i,t+1}\right)=\exp\!\left(-k^{\prime}\,\tilde{H}_{i,t+1}\right), (S23)

[200] p: where k ′ > 0 k^{\prime}>0 controls sensitivity to the entropy of the next step.

[201] h5: Final advantage normalization.

[202] p: After computing A mod ​ ( i , t ) A_{\mathrm{mod}}(i,t) for all steps in the batch, EMPG applies a final batch-level normalization (e.g., zero-mean normalization) before using the resulting advantages in policy gradient updates.

[203] h2: Appendix B Key Hyper-parameter

[204] p: The hyperparameters reported in Table S1 are determined through task-specific grid search. For each policy optimization method and environment, we sweep over the method-relevant hyperparameters while keeping the remaining training and optimization settings fixed. The final configurations correspond to the stable settings selected from the grid search.

[205] figure: Table S1: Key training hyperparameters for agentic RL experiments across four tasks (ALFWorld, WebShop, Sokoban, TIR Math). “–” indicates the method is not applicable to that task. Category ALFWorld WebShop Sokoban TIR Math Model and Environment Configuration [dashed] Base model Qwen3-4B-RFT Qwen3-4B-RFT Qwen3-4B-VL-Instruct-RFT Qwen3-4B-Base Max interaction steps 50 15 15 5 Memory context window 2 (turns) 2 (turns) 2 (turns) 8196 (tokens) Group rollout size 8 8 8 5 Max prompt length 2048 4096 1024 8196 Max response length 512 512 512 4096 Format penalty coefficient 0.1 0.1 0.1 0.1 Training Optimization [dashed] Group normalization mode mean_std_norm mean_std_norm mean_std_norm mean_std_norm Learning rate 1 × 10 − 6 1\times 10^{-6} 1 × 10 − 6 1\times 10^{-6} 1 × 10 − 6 1\times 10^{-6} 1 × 10 − 6 1\times 10^{-6} Mini-batch size 256 128 64 128 KL coefficient 0.01 0.01 0.01 0 Rollout and Inference Configuration [dashed] Rollout engine vLLM vLLM vLLM vLLM Temperature (training) 1.0 1.0 1.0 1.0 Temperature (validation) 0.6 0.6 0.7 0.6 Top- p p (validation) 0.95 0.95 0.95 0.95 Top- k k (validation) 20 20 20 20 Training and Batching [dashed] User Prompt Number 16 16 32 512 Validation batch size 128 128 128 128 Total epochs 200( ∼ \sim 24h) 200( ∼ \sim 22h) 200( ∼ \sim 12h) 30( ∼ \sim 80h) GPUs NVIDIA H200/B200 NVIDIA H200/B200 NVIDIA H200/B200 NVIDIA H200/B200 PO-specific Parameters [dashed] GRPO ε high \varepsilon_{\text{high}} 0.2 0.2 0.2 0.28 ε low \varepsilon_{\text{low}} 0.2 0.2 0.2 0.2 GIGPO ε \varepsilon 0.2 0.2 0.2 – γ \gamma 0.95 0.95 0.95 – ω \omega 1 1 1 – EMPG ε \varepsilon 0.2 0.2 0.2 – k , k ′ k,k^{\prime} 1.0 1.0 1.0 – ζ \zeta 0.05 0.05 0.05 – GSPO ε high \varepsilon_{\text{high}} 4e-3 4e-2 4e-3 4e-3 ε low \varepsilon_{\text{low}} 3e-3 3e-2 3e-3 3e-3 CISPO ε high \varepsilon_{\text{high}} 0.2 0.2 0.2 0.28 ε low \varepsilon_{\text{low}} 1 1 1 1 SAPO τ pos \tau_{\tiny\text{pos}} 1.0 1.0 1.0 1.0 τ neg \tau_{\tiny\text{neg}} 1.05 1.05 1.05 1.05 DAPO ε high \varepsilon_{\text{high}} 0.2 0.2 0.2 0.28 ε low \varepsilon_{\text{low}} 0.2 0.2 0.2 0.2 N oversample N_{\text{oversample}} 3 3 3 2

[206] h2: Appendix C Additional Experiment Result

[207] h3: C.1 Performance on 8B Model

[208] p: To further investigate the scalability of our findings, we evaluate the 8B parameter model (Qwen3-8B) on AlfWorld, which serves as a representative benchmark for complex, multi-turn agentic tasks. Given the substantial computational requirements for large-scale RL training, we focus on this environment to verify if the core design principles distilled from the 4B models remain consistent at a larger scale.

[209] p: As shown in Table S2 , the experimental results on AlfWorld demonstrate that the relative performance gains and stability trends are highly consistent with our observations in the 4B experiments Section 4 . Specifically, the critical importance of sequence-level clipping is reaffirmed: even with increased model capacity, it remains the indispensable factor for preventing training collapse. Furthermore, we observe that the benefits of advantage design and dynamic filtering persist at this larger scale, providing consistent but incremental improvements to final performance. In contrast, the choice of loss aggregation continues to exhibit limited impact, echoing our findings on 4B models. These results collectively suggest that the hierarchical impact of policy design choices—and the resulting SAMPO recipe—is robust and scale-invariant, effectively leveraging the enhanced reasoning capabilities of larger models while maintaining stable training dynamics.

[210] figure: Dimension Method ALFWorld Score Success Base GRPO 2.37 50.92 Loss Agg GRPO ST \text{GRPO}_{\texttt{ST}} 1.68 ↓ \downarrow 29.1% 49.31 ↓ \downarrow 3.2% Importance Sampling SAPO 0.08 ↓ \downarrow 96.6% 1.93 ↓ \downarrow 96.21% CISPO 0.80 ↓ \downarrow 66.2% 30.83 ↓ \downarrow 39.5% GSPO 5.05 ↑ \uparrow 113.1% 79.70 ↑ \uparrow 56.5% Advantage Design GIGPO 4.10 ↑ \uparrow 73.0% 80.03 ↑ \uparrow 57.2% EMPG 4.51 ↑ \uparrow 90.3% 71.48 ↑ \uparrow 40.4% Dynamic Sampling DAPO GRPO {}_{\texttt{GRPO}} 0.81 ↓ \downarrow 65.8% 38.11 ↓ \downarrow 25.16% DAPO GIGPO {}_{\texttt{GIGPO}} 2.49 ↑ \uparrow 5.1% 60.27 ↑ \uparrow 18.4% Ours SAMPO 8.98 ↑ \uparrow 278.9% 97.71 ↑ \uparrow 91.9% Table S2 : Performance on Qwen3-8B for ALFWorld . The overall trend on the 8B variant remains consistent, and SAMPO continues to achieve the best performance, indicating stable gains under model scaling.

[211] h3: C.2 Additional Analysis Result

[212] figure: Figure S1 : Sequence-Level IS Analysis of CISPO and CISPO SM {}_{\texttt{SM}} (CISPO with sequence masking) on ALFWorld.

[213] p: We further visualize the training dynamics of CISPO and CISPO SM \text{CISPO}_{\texttt{SM}} on the AlfWorld task using diagrams. Specifically, following the same setup as in the main text, we categorize trajectories according to three factors: the sign of the advantage, whether the entropy exceeds a predefined threshold, and whether the IS ratio is greater than zero. These criteria partition the samples into eight groups, which we use to analyze how the KL divergence evolves during training.

[214] p: Consistent with our earlier findings, we clearly observe that after CISPO collapses, trajectories with negative advantages and low IS ratios (i.e., adv < 0 \text{adv}<0 and IS < 1 \text{IS}<1 ) rapidly dominate the distribution. This imbalance correlates strongly with the surge in KL divergence and subsequent training instability.

[215] p: This observation also explains why CISPO SM \text{CISPO}_{\texttt{SM}} , which incorporates sequence-level masking, achieves substantially improved stability: by masking these harmful negative-advantage and low-ratio trajectories, the optimization process avoids pathological updates and maintains more balanced gradient signals.

[216] h3: C.3 Task Environment Details

[217] p: ALFWorld ( Shridhar et al., 2020 ) : It provides a text-based interactive setting in which LLM agents are required to complete goal-driven tasks that involve reasoning over multiple sequential decisions. The environment focuses on everyday household activities and evaluates an agent’s ability to plan and act through iterative interaction.

[218] p: WebShop ( Yao et al., 2022 ) : It is a large-scale interactive environment that places agents in realistic e-commerce scenarios, requiring them to interpret user instructions and make sequential decisions to identify and purchase suitable products.

[219] p: Sokoban ( Schrader, 2018 ) : It is a classic grid-based planning task where an agent navigates a 2D environment to push all boxes onto designated target cells. The state is represented visually, and the agent selects from discrete movement actions

[220] p: TIR Math ( Xue et al., 2025 ) : This task focuses on standard mathematical question answering, where Python is used as a tool for intermediate calculations and symbolic reasoning. The overall pipeline follows Xue et al. (2025) . The training data are adapted from SimpleRL ( Zeng et al., 2025 ) , and evaluation is conducted on the AIME and AIME25 benchmarks. Performance is measured using avg ​ @ ​ k \mathrm{avg@k} , following the evaluation protocol in Yu et al. (2025a) .

[221] h2: Appendix D Related Work

[222] p: Large language models have demonstrated strong capabilities in agent-based environments and attracted increasing attention ( Yao et al., 2022 ; Shridhar et al., 2020 ; Li et al., 2023 ) . Prior studies investigate LLMs as agents in multi-turn, action-based environments, emphasizing long-horizon memory and explicit tool use for sequential decision making and reasoning ( Yao et al., 2023 ; Schick et al., 2023 ; Wang et al., 2023 ) . Recently, driven by the success of reinforcement learning in reasoning ( Xu et al., 2025 ; OpenAI, 2025a ; Khatri et al., 2025 ) , RL has been extended to agentic settings ( Jin et al., 2025 ; Plaat et al., 2025 ; Abdulhai et al., 2023 ; Yu et al., 2025c ) . Several representative RL frameworks for LLM agents have emerged. AGILE ( Peiyuan et al., 2024 ) proposes a framework for LLM-driven conversational agents capable of planning, tool use, and expert consultation. SWEET-RL ( Zhou et al., 2025 ) studies collaborative LLM agents that interact with simulated human partners in ColBench, where agents ask clarifying questions and learn from multi-turn feedback. Agent-R1 ( Cheng et al., 2025 ) extends this paradigm to external tool-based environments and enables multi-turn reasoning with tool calls. Similarly, AgentGym-RL ( Xi et al., 2025 ) presents an RL framework for autonomous LLM agents that supports multi-turn interactions, modular architectures, and real-world scenarios. AgentRL ( Zhang et al., 2025 ) develops a multi-turn, multi-task RL system and demonstrates superior performance relative to closed-source models. VerlTool ( Jiang et al., 2025 ) focuses on tool-using LLM agents and aligns well with the VeRL codebase. Most prior work provides limited analysis of agentic RL training instability. In contrast, ARLArena offers a unified training and analysis framework for examining how policy-gradient design choices relate to stability and performance across agentic tasks.

[223] h2: Appendix E Another Roadmap of Building Agentic LLM: Multi-agent System

[224] h3: E.1 Debate

[225] p: Let 𝔸 = { 𝒜 1 , 𝒜 2 , … , 𝒜 N } \mathbb{A}=\{\mathcal{A}_{1},\mathcal{A}_{2},\dots,\mathcal{A}_{N}\} denote the set of N N agents, where N N is an odd integer to prevent tie-breaking scenarios during majority voting. Let x x denote the task prompt. In the initial round ( t = 0 t=0 ), each agent 𝒜 i \mathcal{A}_{i} independently generates a candidate solution c i ( 0 ) c_{i}^{(0)} based solely on the prompt x x :

[226] table: c i ( 0 ) = 𝒜 i ​ ( x ) , ∀ i ∈ { 1 , … , N } \displaystyle c_{i}^{(0)}=\mathcal{A}_{i}(x),\quad\forall i\in\{1,\dots,N\} (S24)

[227] p: Let 𝒞 ( t ) = { c 1 ( t ) , c 2 ( t ) , … , c N ( t ) } \mathcal{C}^{(t)}=\{c_{1}^{(t)},c_{2}^{(t)},\dots,c_{N}^{(t)}\} be the set of candidate solutions at round t t . We define a majority consensus function ℳ ⁡ ( ⋅ ) \mathcal{M}(\cdot) that returns the solution y y if it appears in more than half of the agent responses:

[228] table: y = ℳ ( 𝒞 ( t ) ) = { c ^ if ​ | { c ∈ 𝒞 ( t ) : c = c ^ } | > N 2 ∅ otherwise \displaystyle y=\mathcal{M}(\mathcal{C}^{(t)})=\begin{cases}\hat{c}&\text{if }\left|\{c\in\mathcal{C}^{(t)}:c=\hat{c}\}\right|>\frac{N}{2}\\ \emptyset&\text{otherwise}\end{cases} (S25)

[229] p: If ℳ ⁡ ( 𝒞 ( 0 ) ) ≠ ∅ \mathcal{M}(\mathcal{C}^{(0)})\neq\emptyset , the process terminates and outputs y y . Otherwise, the system enters the debate phase. The process iterates through debate rounds t = 1 , 2 , … , T m ​ a ​ x t=1,2,\dots,T_{max} . For each round, we construct the debate prompt for each agent, which includes the original prompt x x , the set of unique candidate solutions from the previous round Unique ​ ( 𝒞 ( t − 1 ) ) \text{Unique}(\mathcal{C}^{(t-1)}) , and agents’ reasoning in previous round ℛ ( t − 1 ) \mathcal{R}^{(t-1)} . Let ℛ ( t ) = { r 1 ( t ) , r 2 ( t ) , … , r N ( t ) } \mathcal{R}^{(t)}=\{r_{1}^{(t)},r_{2}^{(t)},\dots,r_{N}^{(t)}\} be the agents’ reasoning at round t t , and ℛ ( 0 ) = ∅ \mathcal{R}^{(0)}=\emptyset .

[230] table: r i ( t ) , c i ( t ) = 𝒜 i ​ ( x , Unique ​ ( 𝒞 ( t − 1 ) ) , ℛ ( t − 1 ) ) . \displaystyle r_{i}^{(t)},c_{i}^{(t)}=\mathcal{A}_{i}\left(x,\text{Unique}(\mathcal{C}^{(t-1)}),\mathcal{R}^{(t-1)}\right). (S26)

[231] p: At the end of each round t t , we check for consensus again and output the solution y y if consensus is reached. This mechanism enables agents to either rectify perceived flaws by proposing a new solution or align with a peer by voting for an existing candidate. The debate terminates when a majority consensus is achieved, ℳ ⁡ ( 𝒞 ( t ) ) ≠ ∅ \mathcal{M}(\mathcal{C}^{(t)})\neq\emptyset . If the maximum iteration limit T m ​ a ​ x T_{max} is reached without consensus, the final output y y is randomly sampled from the final set of candidates 𝒞 ( T m ​ a ​ x ) \mathcal{C}^{(T_{max})} .

[232] h3: E.2 Aggressive Debate

[233] p: We extend the Debate framework discussed above to build a decisively goal-oriented variant designed to prioritize task completion over exhaustive exploration. While the standard framework seeks consensus on an optimal solution, the aggressive variant compels agents to accept partial success by securing the best available option within a strict finite horizon.

[234] p: Formally, we modify the agent 𝒜 i \mathcal{A}_{i} by conditioning it on an additional constraint set ℐ a ​ g ​ g \mathcal{I}_{agg} . Unlike standard debate agents that aim for a perfect solution, the aggressive agent 𝒜 i ( ⋅ | ℐ a ​ g ​ g ) \mathcal{A}_{i}(\cdot|\mathcal{I}_{agg}) operates under a modified utility function characterized by several governing principles: (1) Bounded Exploration: The agent must finalize the interaction within a finite horizon. This constraint suppresses excessive exploration and ensures the agent commits to a definitive outcome rather than prolonging the information-gathering phase; (2) Temporal Efficiency: The agent is encouraged to conclude the interaction as early as possible; (3) Incentive Awareness: The agent is explicitly informed that partial rewards are available. This awareness incentivizes the agent to accept high-utility suboptimal outcomes when a perfect solution is unattainable; (4) Pragmatic Optimization: The agent prioritizes securing a result that maximizes available partial rewards rather than seeking a theoretical global optimum, thereby avoiding diminishing returns associated with perfecting the solution in complex environments.

[235] h3: E.3 Experiment Results on SLA and MAS

[236] figure: Method ALFWorld WebShop Pick Look Clean Heat Cool Pick2 All Score Success GPT-4o 61.11 33.33 36.36 50.00 45.45 63.64 50.00 13.60 12.50 GPT-5.2 70.03 66.07 35.37 62.30 52.08 37.36 51.56 26.56 26.56 Debate 67.74 64.28 33.33 60.00 52.38 65.00 56.25 22.65 34.65 Aggressive Debate – – – – – – – 28.51 61.53 Gemini-2.5-pro 84.97 61.61 63.94 22.22 62.50 75.25 66.41 – – GRPO 87.41 62.65 46.42 72.28 58.89 38.37 72.61 75.32 57.71 SAPO 34.49 32.19 24.13 24.92 16.21 9.37 25.16 73.85 52.10 CISPO 76.03 37.12 58.56 50.97 57.88 23.68 54.42 67.96 54.71 GSPO 90.36 79.31 90.71 75.45 77.95 48.95 78.61 85.29 72.48 GIGPO 94.80 83.03 86.37 81.15 75.38 59.21 81.09 67.76 56.55 EMPG 84.18 61.53 69.83 72.49 46.51 0.04 57.91 79.16 64.32 DAPO GRPO \text{DAPO}_{\texttt{GRPO}} 81.28 37.57 53.97 40.16 51.28 6.43 49.58 62.43 46.17 DAPO GIGPO \text{DAPO}_{\texttt{GIGPO}} 85.04 55.26 65.35 58.98 56.52 26.57 60.55 88.10 76.82 SAMPO 96.30 88.49 93.65 92.42 92.70 88.35 92.72 88.04 74.08 Table S3: Unified comparison across ALFWorld (six task types + overall) and WebShop (score and success rate). The upper block reports closed-source baselines and multi-agent strategies; the lower block reports policy optimization methods trained with Qwen3-4B.

[237] h2: Appendix F Failure Analysis

[238] h3: F.1 Method: Sankey Graphs for Action-Transition Flows

[239] p: We analyze agent rollouts by visualizing step-wise action transitions with Sankey graphs. Each column corresponds to a time step, node height indicates the empirical frequency of an action at that step, and edges represent transitions between consecutive steps. Compared with action histograms, Sankey graphs preserve temporal structure and thus reveal loop-like behaviors (e.g., repetitive pagination or oscillation between two actions) that dominate long-horizon failures.

[240] h3: F.2 WebShop: Action-Transition Patterns and Failure Modes

[241] h5: Overall flow (API agent).

[242] p: The API agent is a single-agent baseline powered by GPT-4o via API under the same interaction protocol, without any task-specific training. Figure S2 summarizes WebShop trajectories of the API agent, where green links correspond to successful episodes and red links correspond to failures. A large fraction of failures is characterized by repetitive next actions, suggesting exploration inefficiency where the agent keeps paginating without making progress toward constraint satisfaction.

[243] figure: Figure S2 : WebShop action-transition Sankey for the API agent. Green flows denote successful trajectories and red flows denote failures.

[244] h5: Failure-only flow with action coloring.

[245] p: Figure S3 focuses on failed trajectories and colors nodes by action type. Two dominant failure patterns are observed: (i) Pagination loops : long runs of next (and occasional search ) that rarely transition into click_product (product-detail inspection); (ii) Backtracking oscillation : frequent alternation between click_product and back , suggesting repeated revisits to previously viewed product pages and limited progress toward constraint satisfaction. Notably, our API agent is provided with a long interaction history (past actions and observations) in the prompt, so this pattern is unlikely to be explained by insufficient context alone. Instead, it may reflect limited effective memory usage: without structured tracking or summarization of verified attributes and visited items, the agent may fail to retrieve previously established evidence from a long, unstructured context and thus re-check similar products. We emphasize that this is only one plausible factor; we find instruction ambiguity or conflicting constraints may also contribute.

[246] figure: Figure S3 : WebShop failure-only action-transition Sankey for the API agent. Nodes are colored by action type (e.g., search , click_product , click_other , buy , back , next ).

[247] h3: F.3 WebShop: How RL Post-training Changes Behaviors

[248] h5: Overall flow (RL-optimized agent).

[249] p: Figure S4 shows the same visualization for our RL-optimized agent (post-trained with RL). Compared with the API baseline, the RL agent exhibits fewer next -dominated failure paths and a higher proportion of trajectories that transition into click_product and eventually attempt buy , consistent with more targeted product inspection and earlier decision making.

[250] figure: Figure S4 : WebShop action-transition Sankey for the RL-optimized agent. Green flows denote successful trajectories and red flows denote failures.

[251] h5: Remaining failure modes after RL post-training.

[252] p: Figure S5 focuses on failed RL trajectories. While next -heavy pagination loops become less prominent, two residual issues remain: (i) Backtracking-heavy browsing : repeated click_other / back transitions, suggesting inefficient navigation; (ii) Premature purchase : occasional buy attempts that do not satisfy all constraints, suggesting incomplete constraint tracking.

[253] figure: Figure S5 : WebShop failure-only action-transition Sankey for the RL-optimized agent. Nodes are colored by action type (e.g., search , click_product , click_other , buy , back , next ).

[254] h3: F.4 ALFWorld: Action-Transition Patterns

[255] p: Figure S6 visualizes ALFWorld rollouts. Navigation actions (e.g., go , look ) dominate early steps across episodes, whereas successful trajectories more often transition into object-centric interactions (e.g., examine , open/close , take , use ) and explicit state-checking ( inventory ). In contrast, failed trajectories frequently exhibit prolonged navigation with comparatively fewer object interactions, which may reflect weak progression toward concrete object-level subgoals and imperfect tracking of what has already been tried or collected over long horizons.

[256] figure: Figure S6 : ALFWorld action-transition Sankey diagrams for the API agent. Top: Success (green) vs. failure (red) trajectories. Bottom: Failure trajectories with nodes colored by action type.

[257] h3: F.5 Implications

[258] p: Our analysis suggests two actionable directions: (1) Loop-aware control (e.g., detecting repeated next or click_product ↔ \leftrightarrow back cycles and triggering a plan change); (2) Explicit constraint/state memory (e.g., introducing a lightweight memory agent that maintains a concise record of visited items and verified constraints, and feeds the acting agent with short summaries or retrieval results). Together, these mechanisms may further improve robustness beyond RL post-training.

[259] h2: Appendix G Visualization

[260] h3: G.1 Evidence of Format v.s. Dynamic Filtering

[261] p: To support the analysis in Section 4.4 , we report the format validity ratio during training for different policy optimization variants. The results illustrate that DAPO combined with GIGPO maintains more stable format behavior than DAPO+GRPO after dynamic filtering.

[262] figure: Figure S7 : Format validity ratio during training on AlfWorld and WebShop for GRPO, GIGPO, DAPO GRPO \text{DAPO}_{\texttt{GRPO}} , and DAPO GIGPO \text{DAPO}_{\texttt{GIGPO}} . Applying dynamic filtering to GRPO leads to degraded format stability, whereas DAPO GIGPO \text{DAPO}_{\texttt{GIGPO}} maintains stable format behavior across training.

[263] h2: Appendix H Case Study

[264] h3: H.1 Prompt Templates

[265] h4: H.1.1 TIR Math

[266] h4: H.1.2 WebShop

[267] h4: H.1.3 ALFWorld

[268] h4: H.1.4 Sokoban

[269] h3: H.2 Multi-turn State-Action Templates

[270] h4: H.2.1 TIR Math

[271] h4: H.2.2 WebShop

[272] h4: H.2.3 Alfworld

[273] h4: H.2.4 Sokoban

[274] h2: Instructions for reporting errors

[275] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[276] p: Tip: You can select the relevant text first, to include it in your report.

[277] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[278] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
