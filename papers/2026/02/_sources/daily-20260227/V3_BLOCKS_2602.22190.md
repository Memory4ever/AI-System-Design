[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL

[3] h6: Abstract

[4] p: Open-source native GUI agents have made rapid progress in visual grounding and low-level action execution, yet they still lag behind closed-source systems on long-horizon navigation tasks that demand both high-level reasoning and precise actions. This gap stems from two limitations in the open-source ecosystem: a shortage of high-quality, action-aligned reasoning data, and the direct adoption of generic post-training pipelines that overlook the unique challenges of GUI agents. We identify two fundamental issues in these pipelines: (i) standard supervised fine-tuning (SFT) with long chain-of-thought (CoT) reasoning often hurts grounding accuracy, and (ii) step-wise RLVR-tyle training faces partial verifiability , where multiple actions can be correct at a given state but only a single demonstrated action is used for verification. This causes reward ambiguity and makes offline step-wise metrics weak predictors of online task success during RL training. In this work, we present GUI-Libra , a systematic study and tailored training recipe that addresses these challenges. First, to mitigate the scarcity of action-aligned reasoning data, we introduce a data construction and filtering pipeline and release a curated 81K GUI reasoning dataset. Second, to reconcile reasoning with grounding, we propose action-aware supervised fine-tuning that mixes reasoning-then-action and direct-action supervision, and reweights tokens to emphasize action and grounding. Third, to stabilize RL under partial verifiability, we identify the overlooked importance of KL regularization and show, both theoretically and empirically, that a KL trust region is critical for improving offline-to-online predictability; we further introduce success-adaptive scaling to downweight unreliable negative gradients. Across diverse web and mobile benchmarks, GUI-Libra consistently improves both step-wise accuracy and end-to-end task completion, while strengthening the alignment between offline metrics and online performance. In particular, GUI-Libra-4B and GUI-Libra-8B improve their base models by +15.6% and +12.2% on AndroidWorld, +4.0% and +8.7% on Online-Mind2Web, and +12.5% and +11.3% on WebArena-Lite-v2, respectively. Our results suggest that carefully designed post-training and data curation can unlock significantly stronger task-solving capabilities without costly online data collection. We release our dataset, code, and models to facilitate further research on data-efficient post-training for reasoning-capable GUI agents.

[5] figure: Figure 1 : Overview of GUI-Libra. Using only a subset of existing open-source GUI trajectories, we tackle key limitations of prior training pipelines through action-aligned reasoning data curation, action-aware SFT, and conservative RL, yielding consistent gains on online benchmarks.

[6] h2: 1 Introduction

[7] p: Large vision–language models (VLMs) have become a central building block for graphical user interface (GUI) agents ( Qin et al., 2025b ; Xu et al., 2025c ; Gou et al., 2025 ; Wang et al., 2025a ; Bai et al., 2025a ) , enabling autonomous systems to interpret visual interfaces and output executable actions to complete complex tasks across digital platforms. Among these approaches, native GUI agents ( Qin et al., 2025b ) refer to a single end-to-end model that directly maps user instructions and observations to executable actions, without relying on external planners or separate grounding modules. Recent open-source native agents have achieved substantial progress in visual grounding and low-level action execution ( Xu et al., 2025c ; Wang et al., 2025a ; Liu et al., 2025c ; Wang et al., 2025d ) , significantly narrowing the gap with proprietary systems. Despite these advances, native GUI agents remain less effective at long-horizon decision making, where agents must reason over extended observation–action sequences and adapt their behavior reliably to achieve user-specified goals.

[8] p: Advancing native GUI agents increasingly depends on effective post-training of GUI-centric VLMs, yet current approaches face two intertwined bottlenecks. The first is the scarcity of high-quality, action-aligned reasoning data. Existing GUI navigation datasets ( Li et al., 2024 ; Zheng et al., 2024 ; Xu et al., 2025c ) often lack explicit rationales, contain only short or weakly grounded reasoning traces, or include noisy action labels, providing limited supervision for learning robust and interpretable policies. The second bottleneck is the widespread use of generic post-training recipes that do not fully account for the unique properties of GUI agents. Most existing open-source pipelines rely on either supervised fine-tuning (SFT) on brief rationales ( Wu et al., 2025b ; Xu et al., 2025c ) or reinforcement learning (RL) primarily targeting grounding accuracy ( Luo et al., 2025 ; Lu et al., 2025 ; Zhou et al., 2025b ; Yang et al., 2025b ) . In practice, these approaches expose a persistent tension between reasoning and grounding: incorporating chain-of-thought (CoT) often degrades grounding performance, leading many methods to suppress explicit reasoning rather than addressing the underlying trade-off. Meanwhile, motivated by the success of RL from verifiable rewards (RLVR) in domains such as mathematical reasoning ( Shao et al., 2024 ; Yu et al., 2025 ) , recent work ( Hong et al., 2025 ; Yang et al., 2025c ) has explored step-wise RL for GUI agents. However, these methods overlook a fundamental characteristic of GUI interaction, partial verifiability: at each step, multiple actions may correctly advance the task, yet offline supervision verifies only a single demonstrated action . As a result, alternative valid actions are ambiguously treated as failures, introducing biased gradients, destabilizing training, and weakening the connection between offline evaluation metrics and online task success.

[9] p: To address these challenges, we propose GUI-Libra, a unified post-training framework designed to strengthen decision making in native GUI agents. GUI-Libra is driven by three insights. (i) High-quality rationales and careful data filtering are essential for data-efficient learning, especially because open-source GUI trajectories are often noisy and weakly annotated. (ii) During SFT, CoT tokens can dominate the training loss and interfere with grounding; effective learning therefore requires explicitly prioritizing action and grounding tokens, which directly determine execution. (iii) Under partially verifiable rewards, RL can become unstable without conservative constraints: unlike standard RLVR settings where dropping KL regularization often helps ( Yu et al., 2025 ; Liu et al., 2025d ; Zhou et al., 2025b ; Yang et al., 2025b ) , GUI agents benefit from moderate, KL-regularized RL that mitigates reward ambiguity and distribution shift, improving robustness and offline–online alignment.

[10] p: Guided by these insights, GUI-Libra integrates action-aware supervised fine-tuning (ASFT) with conservative reinforcement learning. To alleviate the scarcity of high-quality reasoning data, we develop a scalable construction and filtering pipeline and release a curated 81K GUI reasoning dataset with improved alignment between reasoning traces and executable actions. In ASFT, GUI-Libra trains on a mixture of reasoning-then-action and direct-action supervision, and applies action-aware token reweighting to emphasize action and grounding tokens, reducing the grounding degradation caused by long CoT traces. In RL, GUI-Libra optimizes policies with GRPO ( Shao et al., 2024 ) under moderate KL regularization, and further introduces a success-adaptive negative gradient scaling strategy to reduce bias from ambiguously “negative” outcomes. Our pipeline has two practical advantages : (1) it derives all training data from existing open-source resources, showing that careful augmentation, filtering, and training method design can make modest open data competitive with closed-data systems ; and (2) it avoids costly online environment interaction, making training scalable and accessible while strengthening the connection between offline metrics and online task success.

[11] p: Extensive experiments across web and mobile benchmarks show that the GUI-Libra series (3B–8B) consistently improves offline step-wise accuracy on standard offline benchmarks and boosts online task completion on AndroidWorld ( Rawles et al., 2025 ) , WebArena-Lite-v2 ( Liu et al., 2025c ) , and Online-Mind2Web ( Xue et al., 2025 ) . Notably, GUI-Libra-4B and GUI-Libra-8B improve their base models by +15.6% and +12.2% on AndroidWorld, and +4.0% and +8.7% on Online-Mind2Web. Detailed ablations further confirm the roles of action-aware supervision and conservative regularization in mitigating grounding degradation, strengthening action prediction, and stabilizing learning under partially verifiable feedback. We also analyze the impact of data filtering and explicit reasoning, and study the trade-off between reasoning and grounding during RL training. We hope these findings and open-source resources will encourage future work on data-efficient and reliable post-training for native GUI agents.

[12] p: Our main contributions are summarized as follows:

[13] p: We present GUI-Libra , a unified post-training framework for native GUI agents that tackles two key challenges: reasoning–grounding interference in SFT, addressed by action-aware SFT that emphasizes action and grounding tokens; and weak offline-to-online predictability in RL, addressed by conservative optimization that constrains policy drift and improves offline–online alignment.

[14] p: We develop a scalable data construction and filtering pipeline and release a high-quality open-source 81K GUI reasoning dataset with improved action alignment.

[15] p: We achieve consistent gains across representative offline and online web and mobile benchmarks, showing that smaller native VLMs trained on modest open-source data can match or even outperform much larger systems.

[16] h2: 2 Related Work

[17] figure: Table 1: Comparison of existing training recipes from different perspectives. The task type column indicates the training target of the released models: denotes GUI grounding, denotes GUI navigation (both online and offline), and denotes offline step-wise action prediction. Name Task Type Reasoning SFT RL Open Weights Open Data Open Code OS-Atlas ( Wu et al., 2025b ) ✗ ✓ ✗ ✓ ✓ ✗ AGUVIS ( Xu et al., 2025c ) short ✓ ✗ ✓ ✓ ✓ UGround ( Gou et al., 2025 ) ✗ ✓ ✗ ✓ ✓ ✓ ScaleCUA ( Liu et al., 2025c ) long ✓ ✗ ✓ ✓ ✓ OpenCUA ( Wang et al., 2025d ) long ✓ ✗ ✓ ✓ ✓ UI-TARS ( Qin et al., 2025b ) short ✓ ✓ ✓ ✗ ✗ GLM-4.1-V ( Hong et al., 2025 ) long ✓ ✓ ✓ ✗ ✗ Ferret-UI Lite ( Yang et al., 2025c ) long ✓ ✓ ✗ ✗ ✗ UI-R1 ( Lu et al., 2025 ) short ✗ ✓ ✓ ✓ ✓ GUI-R1 ( Luo et al., 2025 ) short ✗ ✓ ✓ ✓ ✓ GTA1 ( Yang et al., 2025b ) ✗ ✗ ✓ ✓ ✓ ✓ GUI-Libra (Ours) long ✓ ✓ ✓ ✓ ✓

[18] h3: 2.1 Datasets for Training GUI Agents

[19] p: Recent progress in GUI agents has been propelled by a diverse ecosystem of datasets that target both visual perception and task execution. For robust visual grounding and screen parsing, datasets such as SeeClick ( Cheng et al., 2024b ) , UGround ( Gou et al., 2025 ) , GUIAct ( Chen et al., 2025c ) , ScaleCUA ( Liu et al., 2025c ) , and GUI-360 ( Mu et al., 2025 ) provide large corpora of annotated screenshots and UI element supervision ( Deka et al., 2017 ; Li et al., 2020b ; Li et al., 2020a ; Bai et al., 2021 ; Wu et al., 2023 ; Yang et al., 2025a ; Zheng et al., 2025b ; Wu et al., 2025b ; Nayak et al., 2025 ; Luo et al., 2025 ) .

[20] p: Moving beyond single-step grounding, several large-scale context-aware and trajectory-based datasets capture multi-step interactions in realistic environments, enabling models to learn how UI state evolves over time. Examples include AITW ( Rawles et al., 2023 ) , MM-Mind2Web ( Zheng et al., 2024 ; Deng et al., 2023 ) , AMEX ( Chai et al., 2025 ) , GUI Odyssey ( Lu et al., 2024 ) , and Aria-UI ( Yang et al., 2024c ) . In addition, datasets such as AndroidControl ( Li et al., 2024 ) and JEDI ( Xie et al., 2025 ) enrich interaction trajectories with low-level action descriptions, helping bridge high-level intent with executable operations and improving the learnability of fine-grained GUI manipulation policies.

[21] p: To train agents to understand not only what actions to take but also why , recent efforts introduce natural-language rationales that explicitly inject observation interpretation and planning into step-by-step decision making AITZ ( Zhang et al., 2024 ) , AgentTreck ( Xu et al., 2025a ) , OS-Genesis ( Sun et al., 2024 ) , Aguvis ( Xu et al., 2025c ) , GUI-Net-1M ( Zhang et al., 2025a ) , and WebSTAR ( He et al., 2025 ) . Despite their promise, such reasoning annotations are often short and noisy, limiting their effectiveness in reliably teaching long-horizon reasoning, error recovery, and strategy adaptation. AgentNet ( Wang et al., 2025d ) takes a step further by synthesizing more detailed reasoning traces that include reflective thoughts, enabling agents to detect mistakes and recover mid-trajectory. However, AgentNet primarily focuses on desktop environments, and high-quality reasoning-rich data for mobile and web scenarios remains scarce, leaving open challenges for training robust, general-purpose GUI agents across platforms.

[22] h3: 2.2 VLM Post-training for GUI Agents

[23] p: Recent advances in GUI agents have been largely driven by post-training VLMs to align natural-language instructions with actionable UI interactions. Many GUI grounding-oriented methods primarily rely on SFT with curated interaction or annotation data, including representative efforts such as SeeClick ( Cheng et al., 2024b ) , OS-Atlas ( Wu et al., 2025b ) , Aria-UI ( Yang et al., 2024c ) , and JEDI ( Xie et al., 2025 ) . Beyond text-based coordinate prediction, GUI-Actor ( Wu et al., 2025a ) applies an explicit attention mechanism to improve the generalization to out-of-distribution screenshots. Instead of imitation-style learning, a growing body of work explores to improve grounding accuracy and robustness via reinforcement learning, including UI-R1 ( Lu et al., 2025 ) , GUI-R1 ( Luo et al., 2025 ) , GUI-G1 ( Zhou et al., 2025b ) , GUI-G2 ( Tang et al., 2025 ) , GTA1 ( Yang et al., 2025b ) , and InfiGUI-G1 ( Liu et al., 2025b ) . Hybrid pipelines that combine SFT+RL further push performance by leveraging high-quality demonstrations for initialization and RL for policy refinement, such as Phi-Ground ( Zhang et al., 2025c ) and UI-Ins ( Chen et al., 2025b ) .

[24] p: More recently, research increasingly targets unified native GUI models that jointly learn grounding, planning, and multi-step navigation in an end-to-end manner. Several works adopt SFT-only training on mixed trajectory data to obtain strong generalist computer-use models, including CogAgent ( Hong et al., 2023 ) , Aguvis ( Xu et al., 2025c ) , ScaleCUA ( Liu et al., 2025c ) , FARA ( Awadallah et al., 2025 ) , and OpenCUA ( Wang et al., 2025d ) . To further equip agents with the ability to explore diverse strategies and improve long-horizon success via trial-and-error, other efforts incorporate RL-based post-training for better policy optimization and stability, such as DigiRL ( Bai et al., 2024b ) , AutoGLM ( Liu et al., 2024 ) , UI-TARS ( Qin et al., 2025b ; Wang et al., 2025a ) , MAI-UI ( Zhou et al., 2025a ) , UI-Venus ( Gu et al., 2025 ) , Ferret-UI-Lite ( Yang et al., 2025c ) , and WebGym ( Bai et al., 2026 ) . Despite these advances, three limitations remain. First, encouraging free-form reasoning during RL can hurt grounding accuracy ( Zhou et al., 2025b ; Yang et al., 2025b ; Tang et al., 2025 ; Lu et al., 2025 ; Chen et al., 2025b ) , as models may prioritize high-level semantic logic over precise spatial execution. Second, online RL ( Wang et al., 2025a ; Zhou et al., 2025a ; Bai et al., 2026 ) is expensive to scale, requiring costly environment interaction and robust infrastructure. Third, step-wise RLVR-style training ( Yang et al., 2025c ; Hong et al., 2025 ) in GUI settings faces partial verifiability, which makes rewards ambiguous and introduces noisy or biased learning signals.

[25] p: In this paper, we focus on systematically understanding VLM post-training for GUI agents, and contribute open-source training recipes together with a high-quality, openly released dataset, enabling reproducible development of GUI agents with enhanced reasoning capability.

[26] h2: 3 Preliminaries

[27] h5: VLM-based GUI agents.

[28] p: We formulate GUI interaction as a goal-conditioned partially observable Markov decision process (POMDP) with a natural-language instruction space ℒ \mathcal{L} , specified by ( 𝒮 , 𝒜 , 𝒪 , 𝒯 , ℛ , γ ) (\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T},\mathcal{R},\gamma) . Here, 𝒮 \mathcal{S} denotes latent environment states (e.g., application/page context and UI layout), and 𝒜 \mathcal{A} is an action space where each action consists of an operation and its arguments (e.g., click ​ ( x , y ) \texttt{click}(x,y) , type ​ ( text ) \texttt{type}(\mathrm{text}) , scroll ​ ( direction ) \texttt{scroll}(\mathrm{direction}) ). State transitions follow 𝒯 ⁡ ( s t + 1 ∣ s t , a t ) \mathcal{T}(s_{t+1}\mid s_{t},a_{t}) . At the beginning of each episode, an instruction ℓ ∈ ℒ \ell\in\mathcal{L} specifies the task goal. At each step, the agent receives a partial observation o t ∈ 𝒪 o_{t}\in\mathcal{O} derived from the underlying state s t s_{t} , typically a screenshot. Due to partial observability, the agent conditions on the interaction history h t = ( o 0 , a 0 , … , o t − 1 , a t − 1 ) h_{t}=(o_{0},a_{0},\ldots,o_{t-1},a_{t-1}) together with the current observation o t o_{t} , and follows a VLM-parameterized policy π θ ​ ( a t ∣ ℓ , h t , o t ) \pi_{\theta}(a_{t}\mid\ell,h_{t},o_{t}) . The goal-conditioned reward is r t = ℛ ⁡ ( s t , a t , ℓ ) r_{t}=\mathcal{R}(s_{t},a_{t};\ell) , which is often sparse and success-only: r t = 1 r_{t}=1 if the agent achieves the goal specified by ℓ \ell (typically at termination), and r t = 0 r_{t}=0 otherwise. The episode terminates upon success or after a maximum horizon T T . The objective is to maximize the expected return, max π θ ⁡ 𝔼 ⁡ [ ∑ t = 0 T γ t ​ r t ] \max_{\pi_{\theta}}\mathbb{E}\!\left[\sum_{t=0}^{T}\gamma^{t}r_{t}\right] . When γ = 1 \gamma=1 , this objective is equivalent to maximizing expected task success.

[29] h5: High-level vs. low-level GUI tasks.

[30] p: We categorize GUI tasks by their temporal abstraction. A low-level task can be completed with a single atomic interaction, such as “type amazon.com in the address bar” or “click the confirm button.” In contrast, a high-level task requires a multi-step interaction trajectory, such as “buy a machine learning textbook on Amazon,” which induces a sequence of low-level actions across multiple screens. We view grounding as a special case of low-level decision making, where the agent localizes the target UI element by predicting its interaction coordinates from the instruction and the current observation ( ℓ , o t ) (\ell,o_{t}) . In our paper, we mainly focus on high-level navigation tasks.

[31] h5: Post-training for GUI Models.

[32] p: Supervised fine-tuning (SFT) is a standard approach for post-training GUI models. We assume a dataset of expert trajectories D = { τ i } i = 1 N D=\{\tau_{i}\}_{i=1}^{N} , where each trajectory is τ i = { ( ℓ i , h t i , o t i , c t i , a t i ) } t = 0 T i − 1 \tau_{i}=\{(\ell^{i},h_{t}^{i},o_{t}^{i},c_{t}^{i},a_{t}^{i})\}_{t=0}^{T_{i}-1} . At step t t , the model conditions on the context x t i = ( ℓ i , h t i , o t i ) x_{t}^{i}=(\ell^{i},h_{t}^{i},o_{t}^{i}) and outputs a reasoning trace c t i c_{t}^{i} followed by an executable action a t i a_{t}^{i} . We concatenate reasoning and action into a single target sequence y t i = [ c t i ; a t i ] y_{t}^{i}=[c_{t}^{i};a_{t}^{i}] and minimize the negative log-likelihood:

[33] table: ℒ SFT ​ ( θ ) = − 𝔼 ( x t , y t ) ∼ D ​ log ⁡ π θ ​ ( y t ∣ x t ) , \mathcal{L}_{\mathrm{SFT}}(\theta)=-\mathbb{E}_{(x_{t},y_{t})\sim D}\log\pi_{\theta}(y_{t}\mid x_{t}), (1)

[34] p: where the expectation is taken over all trajectories and time steps in D D .

[35] p: Beyond SFT, prior work ( Luo et al., 2025 ; Lu et al., 2025 ; Zhou et al., 2025b ; Yang et al., 2025b ) adopts reinforcement learning from verifiable rewards (RLVR) to directly optimize step-wise action/coordinate correctness. Given step contexts x = ( ℓ , h t , o t ) ∼ D x=(\ell,h_{t},o_{t})\sim D , we sample a group of G G candidate actions { a k } k = 1 G ∼ π θ old ( ⋅ ∣ x ) \{a_{k}\}_{k=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid x) and compute rewards r k = ℛ ⁡ ( x , a k ) r_{k}=\mathcal{R}(x,a_{k}) , where ℛ \mathcal{R} is a weighted combination of rule-based matching scores on action type, value (text), and coordinates. GRPO then updates the policy using a group-relative variant of policy gradient:

[36] table: ℒ GRPO ( θ ) = − 𝔼 x ∼ D , { a k } k = 1 G ∼ π θ old ( ⋅ ∣ x ) [ 1 G ∑ k = 1 G min ( ρ k A ^ k , clip ( ρ k , 1 − ϵ , 1 + ϵ ) A ^ k ) − β ⋅ KL ( π θ ( ⋅ ∣ x ) ∥ π ref ( ⋅ ∣ x ) ) ] , \mathcal{L}_{\mathrm{GRPO}}(\theta)=-\mathbb{E}_{x\sim D,\{a_{k}\}_{k=1}^{G}\sim\pi_{\theta_{\rm old}}(\cdot\mid x)}\!\left[\frac{1}{G}\sum_{k=1}^{G}\min\!\Big(\rho_{k}\hat{A}_{k},\;\mathrm{clip}(\rho_{k},1-\epsilon,1+\epsilon)\hat{A}_{k}\Big)-\beta\cdot\mathrm{KL}\!\left(\pi_{\theta}(\cdot\mid x)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid x)\right)\right], (2)

[37] p: where ρ k = π θ ​ ( a k ∣ x ) / π θ old ​ ( a k ∣ x ) \rho_{k}=\pi_{\theta}(a_{k}\mid x)/\pi_{\theta_{\mathrm{old}}}(a_{k}\mid x) and A ^ k = ( r k − μ r ) / ( σ r + δ ) \hat{A}_{k}=(r_{k}-\mu_{r})/(\sigma_{r}+\delta) is the group-normalized advantage. Here, μ r \mu_{r} and σ r \sigma_{r} are the mean and standard deviation of { r k } k = 1 G \{r_{k}\}_{k=1}^{G} , and δ \delta is a small constant for numerical stability. The coefficient β \beta controls KL regularization toward a reference policy π ref \pi_{\mathrm{ref}} . In practice, recent RLVR-style work often removes the explicit KL term (i.e., sets β = 0 \beta=0 ) ( Yu et al., 2025 ; Liu et al., 2025d ; Zhou et al., 2025b ; Yang et al., 2025b ) . While RLVR provides convenient automatic supervision, step-wise rewards can be ambiguous for high-level GUI tasks: in the same state, multiple distinct actions may be valid and still make progress, making rule-based matching an imperfect proxy for correctness. We analyze this discrepancy in Section 5.3 .

[38] h2: 4 Reasoning Data Curation for GUI Agents

[39] p: To address the scarcity of high-quality reasoning data for GUI agents, we develop an automated pipeline to construct and filter a high-quality reasoning dataset, GUI-Libra-81K .

[40] figure: Table 2 : Comparison of our GUI reasoning dataset with previous open-source datasets in web and mobile domains. Token statistics are computed using the Qwen2.5-VL-3B-Instruct tokenizer. Dataset Avg Thought Token Per Step Total Steps #Traj MM-Mind2Web ( Zheng et al., 2024 ) 0 8K 1K AndroidControl ( Li et al., 2024 ) 11 75K 14K GUIAct ( Chen et al., 2025c ) 0 17K 2.5k AMEX ( Chai et al., 2025 ) 0 35K 3K GUI-Net-1M ( Zhang et al., 2025a ) 37 4M 1M ScaleCUA ( Liu et al., 2025c ) 0 170K 19K AGUVIS ( Xu et al., 2025c ) Stage2 L2 (All sources) 56 300K 35K AGUVIS ( Xu et al., 2025c ) Stage 2 L3 (All sources) 85 300K 35K GUI-Libra-81K (Ours) 210 81K 9K

[41] figure: Figure 2 : Example data format in GUI-Libra-81K . Each sample includes the current visual observation (screenshot) and textual context (system prompt, user instruction, and interaction history/previous actions). The model output is split into (1) a CoT reasoning trace and (2) a structured executable action (JSON), specifying the action type, a brief action description, the target element (if available), and action arguments such as text values or coordinates.

[42] h3: 4.1 Data Curation and Filtering Pipeline

[43] p: As shown in Table 2 , existing open-source datasets in web and mobile domains (e.g., the AGUVIS collection ( Xu et al., 2025c ) ) typically provide only short rationales, often fewer than 100 thought tokens per step. Rather than collecting costly new data from online environments, we aim to fully leverage the large volume of existing web and mobile data by augmenting it with richer CoT reasoning and filtering out low-quality samples that would otherwise induce reasoning–action mismatch.

[44] h4: 4.1.1 Data Sources

[45] p: Although large-scale open-source datasets exist for GUI grounding ( Gou et al., 2025 ; Wu et al., 2025b ) , trajectory-based GUI navigation data remain relatively scarce due to the high cost of collecting multi-step interaction traces. Following AGUVIS ( Xu et al., 2025c ) , we therefore aggregate trajectory data from multiple public sources that cover both web and mobile domains, including GUI-Odyssey ( Lu et al., 2024 ) , AMEX ( Chai et al., 2025 ) , AndroidControl ( Li et al., 2024 ) , AitZ ( Zhang et al., 2024 ) , AitW ( Rawles et al., 2023 ) , GUIAct ( Chen et al., 2025c ) , and MM-Mind2Web ( Zheng et al., 2024 ) . Compared with the original AGUVIS collection, we additionally include the Chinese subset from GUIAct to broaden multilingual coverage and increase website diversity. Overall, these datasets span diverse applications and websites, and include tasks with varying difficulty levels. We apply an initial cleaning stage to remove incomplete trajectories, extremely short or long traces (fewer than 3 steps or more than 50 steps), and steps containing compound actions that cannot be represented in our action space. After cleaning, we obtain 19K trajectories comprising 170K steps.

[46] h4: 4.1.2 Unified Structured Format

[47] p: Figure 2 summarizes our unified data format. Each sample contains an input and an output. The input includes a system prompt that enumerates available actions, the user instruction, the interaction history (previous actions), and the current screenshot. The output contains (1) a reasoning trace enclosed by <think> … </think> and (2) a structured action enclosed by <answer> … </answer> . The structured action is represented as a JSON object with an action_type and corresponding arguments, such as value for text entry and point_2d for click coordinates. We consider 13 common action types for web and mobile control: Click , Write , Terminate , Swipe , Scroll , NavigateHome , Answer , Wait , OpenAPP , NavigateBack , KeyboardPress , LongPress , and Select . The action optionally includes an action_target , a natural-language description of the UI element to interact with. In addition, we include an action_description that succinctly states the intended operation, which is appended to the interaction history for subsequent steps and captures a brief step-level rationale. Retaining action_target further supports downstream filtering by enabling consistency checks between the described target element and the coordinates from the original datasets. Details of the action space are provided in Appendix B .

[48] h4: 4.1.3 Action-aligned Reasoning Augmentation

[49] p: Most existing GUI trajectory datasets lack detailed reasoning traces or only include short rationales. AGUVIS ( Xu et al., 2025c ) augments trajectories by prompting GPT-4o with the instruction, previous actions, and the current action, then requesting a brief “thought” and a one-sentence action description. We find two factors that limit the quality of such generated reasoning. First, the prompt is not sufficiently informative. We extend it with GUI-specific guidelines that encourage structured reasoning (observation description, reflection, and planning), enforce format constraints, and add action-related requirements. Second, reasoning quality is sensitive to the choice of generator model. We compare reasoning traces produced by GPT-4o, o4-mini, and GPT-4.1 and observe substantial differences across models (Figure 13 ). Our structured output format also facilitates reliable parsing and downstream processing. Moreover, we do not force the generator to exactly follow the dataset action; instead, we treat the annotated action as a reference and allow the model to select a different action from the available set when it has sufficient justification. The full prompt template is provided in Appendix F .

[50] p: At each step, the generator produces the reasoning trace, action_description , action_type , action_target , and value , while we reuse the coordinates from original dataset as point_2d . Because generation is conditioned on noisy original annotations, mismatches can still arise, for example, the dataset may contain incorrect coordinates, the generated action_target may not match the provided coordinates, or the model may choose a different action than the annotation. We therefore add a dedicated filtering stage to improve action–reasoning alignment and overall data quality.

[51] figure: Figure 3 : (a)(b) Data source distribution for SFT and RL. (c) Action type distribution of GUI-Libra-81K . (d) Comparison of step index distributions between our SFT and RL datasets.

[52] h4: 4.1.4 Data Filtering for SFT

[53] p: Human-collected and automatically labeled GUI trajectories are inevitably noisy ( Yang et al., 2025b ; Xu et al., 2025c ) , including incorrect action types and inaccurate coordinates. To improve data quality, we curate our SFT data using a two-step automatic filtering pipeline.

[54] p: (1) Agreement filtering via action re-prediction. We run Qwen3-VL-8B-Instruct for 10 stochastic runs on each input and measure how often the predicted action matches the annotation (e.g., exact match on action_type and coordinate proximity for Click -like actions). We discard steps with re-prediction accuracy below 0.3 0.3 , which effectively removes uncertain or low-quality samples.

[55] p: (2) Coordinate alignment via bounding-box verification. We leverage action_target to verify whether the original coordinate actually corresponds to the intended UI element, and to obtain bounding-box supervision for RL. Concretely, we prompt Qwen3-VL-32B-Instruct to predict a bounding box given the current screenshot and action_target , and keep a step only if the original point_2d falls inside the predicted box. This filtering removes coordinate errors and reduces reasoning–action mismatch, while also providing reliable bounding-box annotations, often missing from prior datasets ( Xu et al., 2025c ) , for subsequent RL training.

[56] h5: SFT Dataset Statistics.

[57] p: After filtering, we obtain 81K SFT steps originating from 9K trajectories. Figure 3 (a) shows the source distribution: most data comes from mobile datasets (e.g., AndroidControl, GUI-Odyssey, AMEX), while only 14.3% comes from the web domain. This reflects the current ecosystem where large-scale open mobile interaction data are more prevalent; scaling high-quality web trajectories remains an important direction. Figure 3 (b) shows the action distribution: Click accounts for around 60% of steps, followed by Write , Terminate , and Swipe , while LongPress and Select are rare. This imbalance makes rare actions difficult to learn from SFT alone, motivating a subsequent RL stage.

[58] h4: 4.1.5 Data Filtering for RL

[59] p: For RL, we prioritize a more balanced training set by reducing biases in both step index and domain. Specifically, we address two issues: (i) early-step bias , where many trajectories share similar initial screens and actions (e.g., mobile home screens or common web landing pages), and (ii) domain imbalance , where mobile trajectories dominate the pool. To mitigate these effects, we downsample early steps (small step indices) and further downsample mobile-domain trajectories, resulting in a 40K -step dataset for RL training. Figure 3 (c) compares the step-index distributions, while Figure 3 (a) compares the domain distributions. Overall, the RL subset is substantially more balanced than the SFT dataset.

[60] h2: 5 GUI-Libra

[61] p: In this section, we introduce GUI-Libra, a native GUI agent with enhanced reasoning capabilities. Using our curated dataset, we first conduct a systematic study of SFT with long CoT and its impact on grounding. We then analyze how step-wise RLVR-style training correlates with online performance in GUI navigation.

[62] figure: Figure 4 : (a) Grounding accuracy on ScreenSpot-v2 versus response length for base models and CoT-SFT models, showing that overly long responses correlate with degraded grounding. (b) Average grounding accuracy under different SFT strategies, where excessively long reasoning traces lead to a substantial drop.

[63] h3: 5.1 SFT with Long CoT Hurts GUI Grounding

[64] p: Prior work ( Lu et al., 2025 ; Luo et al., 2025 ) has observed that removing CoT reasoning can improve grounding performance in GUI agents. However, systematic evidence and analysis of this effect, especially under long CoT traces, remain limited, since most existing training data contain only short rationales.

[65] p: Using GUI-Libra-81K , we investigate how response length correlates with grounding performance on ScreenSpot-v2 ( Wu et al., 2025b ) . Specifically, we fine-tune Qwen2.5-VL-3/7B-Instruct base models and prompt them to generate reasoning before grounding, following our structured response format. To induce diverse response lengths, we sample outputs with a temperature of 1.0. We group responses into 30-token bins and discard bins with fewer than 20 samples for statistical reliability. As shown in Figure 4 (a), grounding accuracy exhibits a clear negative correlation with response length for both base and CoT-SFT models. Longer responses consistently lead to worse grounding performance. Moreover, CoT-based SFT substantially widens the length distribution, producing many responses longer than 250 tokens, which are associated with particularly severe performance drops.

[66] p: To pinpoint the source of this degradation, we compare three SFT variants on Qwen2.5-VL-3B-Instruct using GUI-Libra-81K : (i) SFT with CoT , which uses the full reasoning-then-action outputs; (ii) SFT without CoT , which removes reasoning and keeps only the <answer>...</answer> action; and (iii) Grounding-only , which predicts coordinates solely from the action-target description. Figure 4 (b) shows that grounding-only SFT yields a modest gain, while SFT without CoT slightly degrades performance. In contrast, SFT with long CoT traces causes a substantial drop, indicating that the primary driver of grounding degradation is excessively long reasoning sequences.

[67] h3: 5.2 Action-Aware Supervised Fine-Tuning

[68] p: Our goal is to build native GUI agents that can both reason and act within a single model. Rather than discarding reasoning traces, we seek to preserve reasoning ability while mitigating the grounding degradation caused by long CoT sequences. To this end, we propose action-aware supervised fine-tuning (ASFT), a unified training framework that combines mixed data supervision with token-level reweighting to balance reasoning, action prediction, and grounding.

[69] h5: Mixed reasoning and direct-action supervision.

[70] p: ASFT trains on a mixture of data with and without explicit reasoning traces. To construct the direct-action data, we remove the reasoning traces and keep only the structured action output between <answer> and </answer> . Training on both data variants provides two complementary supervision modes: (i) reasoning-then-action and (ii) direct action prediction. Similar data mixtures were used for GUI models such as OpenCUA ( Wang et al., 2025d ) , as well as LLM agent training ( Wang et al., 2025b ; Zhang et al., 2025b ) , but their role in mitigating grounding degradation has not been clearly demonstrated. This dual-mode supervision serves two purposes. First, it increases the amount of action-centric learning signal, strengthening action prediction that is essential for interactive agents. Second, it reduces reliance on verbose intermediate reasoning, alleviating grounding degradation induced by long CoT traces. As a result, the model can flexibly produce either concise direct actions or reasoning-then-action outputs at inference time, improving both grounding accuracy and response efficiency.

[71] h5: Action-aware reweighting.

[72] p: In addition to mixed supervision, ASFT further assigns higher weights to action and grounding tokens. Although grounding is part of the action output in our formulation, the action sequence contains both semantic components (e.g., action description, action type, and value) and spatial components (coordinates), which can be weighted differently at the token level.

[73] p: Concretely, we treat tokens inside <answer> … </answer> as the action output, and further split them into action tokens (all tokens excluding the point_2d field) and grounding tokens (tokens associated with point_2d field). Let c t c_{t} , a t a_{t} , and g t g_{t} denote the reasoning, action, and grounding tokens at step t t , respectively, and let x t = ( ℓ , h t , o t ) x_{t}=(\ell,h_{t},o_{t}) denote the conditioning context. We denote the mixed training set by D mix D_{\rm mix} , which contains both reasoning-then-action and direct-action samples; for direct-action samples we set c t c_{t} to an empty sequence. Under this unified representation, the ASFT objective is

[74] table: ℒ ASFT ​ ( θ ) = − 𝔼 ( x t , c t , a t , g t ) ∼ D mix ​ log ⁡ π θ ​ ( c t ∣ x t ) + α a ​ log ⁡ π θ ​ ( a t ∣ x t , c t ) + α g ​ log ⁡ π θ ​ ( g t ∣ x t , c t , a t ) | c t | + α a ​ | a t | + α g ​ | g t | , \mathcal{L}_{\text{ASFT}}(\theta)=-\mathbb{E}_{(x_{t},c_{t},a_{t},g_{t})\sim D_{\rm mix}}\frac{\log\pi_{\theta}(c_{t}\mid x_{t})+\alpha_{a}\log\pi_{\theta}(a_{t}\mid x_{t},c_{t})+\alpha_{g}\log\pi_{\theta}(g_{t}\mid x_{t},c_{t},a_{t})}{|c_{t}|+\alpha_{a}|a_{t}|+\alpha_{g}|g_{t}|}, (3)

[75] p: where α a \alpha_{a} and α g \alpha_{g} control the relative importance of action and grounding tokens. By adjusting these coefficients, ASFT recovers several common training strategies as special cases: (i) α a = α g = 1 \alpha_{a}=\alpha_{g}=1 reduces to standard SFT; (ii) α a = α g ≫ 1 \alpha_{a}=\alpha_{g}\!\gg\!1 emphasizes action/grounding tokens and approximates CoT-free SFT; and (iii) α g ≫ α a \alpha_{g}\!\gg\!\alpha_{a} with α g ≫ 1 \alpha_{g}\!\gg\!1 further reduces to grounding-only SFT. Overall, ASFT provides a flexible mechanism for balancing reasoning, action, and grounding during supervised fine-tuning of native GUI agents.

[76] h3: 5.3 Reinforcement Learning from Partial Verifiable Rewards

[77] p: Applying RLVR-style training to optimize step-wise action or coordinate correctness for GUI agents has been explored in prior work ( Luo et al., 2025 ; Lu et al., 2025 ; Zhou et al., 2025b ; Yang et al., 2025b ) . However, multi-step GUI navigation differs from standard RLVR settings in two key ways. (i) Errors accumulate and induce distribution shift : small step mistakes compound over time and change the distribution of states the agent visits. (ii) Rewards are partially verifiable : at each step, multiple actions can correctly advance the task, yet offline supervision typically provides and verifies only a single demonstrated action. We show that both factors are crucial for understanding when offline step-wise metrics can reliably predict online task success.

[78] h5: Setup.

[79] p: For ease of analysis, we adopt a finite-horizon MDP that is consistent with our earlier goal-conditioned POMDP formulation. Specifically, we consider a goal-conditioned MDP ℳ = ( 𝒮 , 𝒜 , P , H ) \mathcal{M}=(\mathcal{S},\mathcal{A},P,H) , where the instruction ℓ \ell is included in the state, and partial observability is handled by treating the agent’s history (or belief state) as the effective state. A policy π \pi induces a sequence of state visitation distributions { d π , t } t = 1 H \{d_{\pi,t}\}_{t=1}^{H} , where d π , t ​ ( s ) d_{\pi,t}(s) is the probability of visiting state s s at step t t . For each state s s , let 𝒜 ∗ ​ ( s ) ⊆ 𝒜 \mathcal{A}^{*}(s)\subseteq\mathcal{A} denote the set of valid actions that can correctly advance the task. Offline supervision provides only a single demonstrated action a ~ ​ ( s ) ∈ 𝒜 ∗ ​ ( s ) \tilde{a}(s)\in\mathcal{A}^{*}(s) .

[80] h6: Definition 5.1 .

[81] p: Partially Verifiable Reward For each state s s , the offline dataset provides a single demonstrated action a ~ ​ ( s ) ∈ 𝒜 ∗ ​ ( s ) \tilde{a}(s)\in\mathcal{A}^{*}(s) . The step-wise reward induced by offline verification is

[82] table: r ~ ( s , a ) ≜ 𝟏 { a = a ~ ( s ) } . \tilde{r}(s,a)\triangleq\mathbf{1}\{a=\tilde{a}(s)\}.

[83] p: We call r ~ \tilde{r} partially verifiable if

[84] table: r ~ ​ ( s , a ) = 1 ⇒ a ∈ 𝒜 ∗ ​ ( s ) but r ~ ​ ( s , a ) = 0 ⇏ a ∉ 𝒜 ∗ ​ ( s ) , \tilde{r}(s,a)=1\Rightarrow a\in\mathcal{A}^{*}(s)\quad\text{but}\quad\tilde{r}(s,a)=0\not\Rightarrow a\notin\mathcal{A}^{*}(s),

[85] p: i.e., positive feedback is reliable, while negative feedback is ambiguous because 𝒜 ∗ ​ ( s ) \mathcal{A}^{*}(s) often contains valid actions beyond a ~ ​ ( s ) \tilde{a}(s) .

[86] h5: Offline vs. online metrics.

[87] p: Offline evaluation typically measures one-step action matching on a fixed state distribution d μ d_{\mu} , the marginal induced by an expert dataset D μ D_{\mu} . We define the offline score as

[88] table: M off ( π ) ≜ 𝔼 s ∼ d μ [ π ( a ~ ( s ) ∣ s ) ] = 𝔼 ( s , a ~ ) ∼ D μ 𝔼 a ∼ π ( ⋅ ∣ s ) [ 𝟏 { a = a ~ } ] . M_{\text{off}}(\pi)\triangleq\mathbb{E}_{s\sim d_{\mu}}\big[\pi(\tilde{a}(s)\mid s)\big]=\mathbb{E}_{(s,\tilde{a})\sim D_{\mu}}\;\mathbb{E}_{a\sim\pi(\cdot\mid s)}\big[\mathbf{1}\{a=\tilde{a}\}\big]. (4)

[89] p: Online evaluation measures trajectory-level task success under closed-loop interaction. We define the probability that π \pi completes the task within horizon H H as: J ⁡ ( π ) ≜ Pr τ ∼ π , P ⁡ ( success ​ ( τ ) = 1 ) J(\pi)\triangleq\Pr_{\tau\sim\pi,P}\!\big(\text{success}(\tau)=1\big) .

[90] h5: Two quantities controlling predictability.

[91] p: We characterize when S off ​ ( π ) S_{\text{off}}(\pi) is predictive of J ⁡ ( π ) J(\pi) using two factors: (i) occupancy mismatch between the online state distribution induced by π \pi and the offline distribution d μ d_{\mu} , and (ii) step-wise ambiguity due to partial verifiability. Formally, define the occupancy mismatch coefficient

[92] table: C ( π ) ≜ max t ∈ [ H ] sup s : d μ ​ ( s ) > 0 d π , t ​ ( s ) d μ ​ ( s ) , C(\pi)\triangleq\max_{t\in[H]}\sup_{s:\,d_{\mu}(s)>0}\frac{d_{\pi,t}(s)}{d_{\mu}(s)}, (5)

[93] p: and define the off-demo validity mass of π \pi at state s s as

[94] table: η π ​ ( s ) ≜ π ⁡ ( 𝒜 ∗ ​ ( s ) ∖ { a ~ ​ ( s ) } ∣ s ) , η ¯ π ≜ 𝔼 s ∼ d μ ​ [ η π ​ ( s ) ] . \eta_{\pi}(s)\triangleq\pi\!\left(\mathcal{A}^{*}(s)\setminus\{\tilde{a}(s)\}\mid s\right),\qquad\bar{\eta}_{\pi}\triangleq\mathbb{E}_{s\sim d_{\mu}}[\eta_{\pi}(s)]. (6)

[95] p: Note that the true step-wise validity probability satisfies

[96] table: π ⁡ ( 𝒜 ∗ ​ ( s ) ∣ s ) = π ⁡ ( a ~ ​ ( s ) ∣ s ) + η π ​ ( s ) , \pi\!\left(\mathcal{A}^{*}(s)\mid s\right)=\pi\!\left(\tilde{a}(s)\mid s\right)+\eta_{\pi}(s),

[97] p: since 𝒜 ∗ ​ ( s ) \mathcal{A}^{*}(s) may contain valid actions beyond the single demonstrated action a ~ ​ ( s ) \tilde{a}(s) , which are not credited by offline matching.

[98] h6: Assumption 5.1 .

[99] p: If an episode fails under policy π \pi , then there exists at least one step t ≤ H t\leq H such that a t ∉ 𝒜 ∗ ​ ( s t ) a_{t}\notin\mathcal{A}^{*}(s_{t}) .

[100] h6: Theorem 5.2 .

[101] p: Offline-to-online bound under partial verifiabilityoff2on_main Assume Assumption 5.1 and that, for all t ∈ [ H ] t\in[H] , d π , t ​ ( s ) > 0 d_{\pi,t}(s)>0 implies d μ ​ ( s ) > 0 d_{\mu}(s)>0 (i.e., supp ⁡ ( d π , t ) ⊆ supp ⁡ ( d μ ) \mathrm{supp}(d_{\pi,t})\subseteq\mathrm{supp}(d_{\mu}) ). This condition ensures the occupancy ratio C ⁡ ( π ) C(\pi) is well-defined. Then the online success probability satisfies

[102] table: J ⁡ ( π ) ≥ 1 − H ⋅ C ⁡ ( π ) ⋅ ( 1 − M off ​ ( π ) − η ¯ π ) . J(\pi)\ \geq\ 1\;-\;H\cdot C(\pi)\cdot\Big(1-M_{\mathrm{off}}(\pi)-\bar{\eta}_{\pi}\Big). (7)

[103] p: In particular, if C ⁡ ( π ) C(\pi) is uniformly bounded over a policy class and η ¯ π \bar{\eta}_{\pi} is small or stable across policies , then M off ​ ( π ) M_{\mathrm{off}}(\pi) becomes predictive of J ⁡ ( π ) J(\pi) through the affine lower bound in Eq 7 .

[104] h5: Takeaway.

[105] p: Theorem shows that offline-to-online predictability is governed by two factors: (1) distribution shift captured by C ⁡ ( π ) C(\pi) and (2) non-identifiability under partial verifiability captured by the unobserved off-demo validity mass η ¯ π \bar{\eta}_{\pi} . Thus, offline one-step matching can be a poor proxy for online success when either the policy drifts to states outside the offline support or the probability mass over valid actions shifts from the demonstrated action to other valid alternatives, changing M off ​ ( π ) M_{\mathrm{off}}(\pi) without reflecting true step validity. A detailed proof and discussion are deferred to Appendix E .

[106] h4: 5.3.1 Why Standard RLVR is Easier to Predict?

[107] h6: Corollary 5.3 .

[108] p: Fully verifiable, single-step RLVR Suppose H = 1 H=1 and the reward is fully verifiable, i.e., 𝒜 ∗ ​ ( s ) = { a ~ ​ ( s ) } \mathcal{A}^{*}(s)=\{\tilde{a}(s)\} for all s s (hence η π ​ ( s ) ≡ 0 \eta_{\pi}(s)\equiv 0 ). More generally, for H = 1 H=1 , Eq 7 reduces to

[109] table: J ⁡ ( π ) ≥ 1 − C ⁡ ( π ) ​ ( 1 − M off ​ ( π ) ) , J(\pi)\geq 1-C(\pi)\big(1-M_{\mathrm{off}}(\pi)\big),

[110] p: indicating substantially tighter offline-to-online alignment.

[111] p: Standard RLVR is often easier to analyze and predict because it is typically single-step ( H = 1 H=1 ) and fully verifiable ( η π ≡ 0 \eta_{\pi}\equiv 0 ): one-step matching directly reflects true correctness and there is no error accumulation over time. In contrast, for multi-step GUI agents, distribution shift across steps and partial verifiability jointly weaken the link between offline matching and online success. This motivates methods that explicitly address both state-distribution shift and reward ambiguity in RL for long-horizon GUI navigation.

[112] h4: 5.3.2 KL Regularization Improves Predictability

[113] p: While many RLVR pipelines omit KL regularization for efficiency ( Yu et al., 2025 ; Liu et al., 2025d ; Zhou et al., 2025b ; Yang et al., 2025b ) , we find it is crucial in partially verifiable, multi-step GUI settings. Intuitively, a KL trust region constrains policy drift, which in turn helps control the two quantities governing offline-to-online predictability in Theorem : the occupancy mismatch C ⁡ ( π ) C(\pi) and the off-demo validity mass η ¯ π \bar{\eta}_{\pi} .

[114] h5: KL-induced bounds for occupancy mismatch and off-demo validity mass (informal).

[115] p: Let π ref \pi_{\mathrm{ref}} be a reference policy (e.g., the SFT initialization trained on demonstrations) and assume a per-state KL constraint KL ( π ( ⋅ ∣ s ) ∥ π ref ( ⋅ ∣ s ) ) ≤ ε \mathrm{KL}\!\left(\pi(\cdot\mid s)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq\varepsilon for all s s . Under this constraint, the state visitation distribution induced by π \pi cannot drift too far from that of π ref \pi_{\mathrm{ref}} . In particular, if the offline distribution has a positive lower bound on its support, ρ ≜ inf s : d μ ​ ( s ) > 0 d μ ( s ) > 0 \rho\triangleq\inf_{s:\,d_{\mu}(s)>0}d_{\mu}(s)\;>\;0 , and d π ref , t ≪ d μ d_{\pi_{\mathrm{ref}},t}\ll d_{\mu} for all t ∈ [ H ] t\in[H] , then the occupancy mismatch is controlled as

[116] table: C ⁡ ( π ) ≤ C ⁡ ( π ref ) + H ​ 2 ​ ε ρ . C(\pi)\;\leq\;C(\pi_{\mathrm{ref}})+\frac{H\sqrt{2\varepsilon}}{\rho}. (8)

[117] p: KL regularization also limits how much probability mass can move away from the demonstrated action. If the reference policy is demo-concentrated, i.e., π ref ​ ( a ~ ​ ( s ) ∣ s ) ≥ 1 − δ ⁡ ( s ) \pi_{\mathrm{ref}}(\tilde{a}(s)\mid s)\geq 1-\delta(s) , then the off-demo validity mass satisfies

[118] table: η ¯ π ≤ δ ¯ + ε / 2 , δ ¯ ≜ 𝔼 s ∼ d μ ​ [ δ ⁡ ( s ) ] . \bar{\eta}_{\pi}\;\leq\;\bar{\delta}+\sqrt{\varepsilon/2},\qquad\bar{\delta}\triangleq\mathbb{E}_{s\sim d_{\mu}}[\delta(s)]. (9)

[119] p: Full statements and proofs are provided in Appendix E.0.2 . The above bounds provide a principled explanation for why KL-regularized policy optimization improves predictability: a KL trust region simultaneously limits state-distribution shift and constrains how much probability mass can move away from the demonstrated action. As a result, KL-regularized RL keeps training in a regime where the offline matching score M off ​ ( π ) M_{\mathrm{off}}(\pi) remains a more stable proxy for the online success rate J ⁡ ( π ) J(\pi) .

[120] h3: 5.4 Success-adaptive Negative Gradient Scaling

[121] p: Under partial verifiability, the step-wise reward provides reliable positive feedback, while r ~ ​ ( s , a ) = 0 \tilde{r}(s,a)=0 is ambiguous: it conflates truly invalid actions with valid-but-uncredited alternatives. Consequently, treating every non-match as equally negative can produce biased and overly aggressive updates, pushing the policy to overfit the demonstrator’s particular choice. To address this issue, we propose success-adaptive negative gradient scaling (SNGS) , which conservatively downweights gradients induced by ambiguous “negative” outcomes. Importantly, negative updates in policy-gradient methods such as GRPO remain useful for stabilizing training and avoiding premature collapse ( Zhu et al., 2025 ) . Therefore, rather than suppressing all negative gradients equally, SNGS rescales them using a state-conditioned reliability signal estimated from the GRPO sampling group. Concretely, GRPO samples a group of G G candidate actions for the same state and computes group-relative advantages. Let { ( a k , r ~ k ) } k = 1 G \{(a_{k},\tilde{r}_{k})\}_{k=1}^{G} denote a GRPO group at state s s , where r ~ k = 𝟏 { a k = a ~ ( s ) } ∈ { 0 , 1 } \tilde{r}_{k}=\mathbf{1}\{a_{k}=\tilde{a}(s)\}\in\{0,1\} . We define the empirical group success rate as p ^ g ​ ( s ) ≜ 1 G ​ ∑ k = 1 G r ~ k \hat{p}_{g}(s)\;\triangleq\;\frac{1}{G}\sum_{k=1}^{G}\tilde{r}_{k} , which measures how concentrated the current policy is on the demonstrated action.

[122] p: We introduce a scaling factor λ g ​ ( s ) \lambda_{g}(s) that rescales only the negative advantages.

[123] table: λ g ​ ( s ) ≜ min ⁡ ( λ 0 + κ ​ p ^ g ​ ( s ) , 1 ) . \lambda_{g}(s)\;\triangleq\;\min\left(\lambda_{0}+\kappa\,\hat{p}_{g}(s),\;1\right). (10)

[124] p: Here λ 0 \lambda_{0} is an offset, and κ \kappa controls how λ g \lambda_{g} varies with p ^ g \hat{p}_{g} . With κ > 0 \kappa>0 , λ g \lambda_{g} increases with p ^ g \hat{p}_{g} : as the policy becomes more concentrated on a ~ ​ ( s ) \tilde{a}(s) , non-matching samples are more likely to be genuinely incorrect, so we downweight negative gradients less and gradually recover the standard GRPO update as λ g → 1 \lambda_{g}\to 1 . With κ < 0 \kappa<0 , λ g \lambda_{g} decreases with p ^ g \hat{p}_{g} , making updates more conservative for high-success groups. In our experiments, we find κ > 0 \kappa>0 works well in most settings and use it as the default.

[125] p: Let A k A_{k} denote the GRPO advantage for sample k k . SNGS modifies only the negative advantages:

[126] table: A ~ k ≜ { A k , A k ≥ 0 , λ g ​ ( s ) ​ A k , A k < 0 . \tilde{A}_{k}\;\triangleq\;\begin{cases}A_{k},&A_{k}\geq 0,\\[2.0pt] \lambda_{g}(s)\,A_{k},&A_{k}<0.\end{cases} (11)

[127] p: We then replace the advantage term in the GRPO objective (Eq. 2 ) with A ~ k \tilde{A}_{k} . As a result, SNGS preserves positive learning signals corresponding to reliably verified matches, while attenuating updates driven by potentially ambiguous negatives. This reduces over-penalization of valid alternatives and leads to more robust policy optimization under partial verification.

[128] h3: 5.5 Reward Function Implementation

[129] p: Each rollout produces a structured prediction string y y following our output structure:

[130] table: y = <think> ⋯ </think><answer> a </answer> , y=\texttt{<think>}\cdots\texttt{</think><answer>}a\texttt{</answer>},

[131] p: where the <answer> block contains a structured action a a that can be parsed into a JSON object

[132] table: a = { action_type , action_description , value , point_2d } , a=\{\texttt{action\_type},\ \texttt{action\_description},\ \texttt{value},\ \texttt{point\_2d}\},

[133] p: with point_2d ∈ ℝ 2 \texttt{point\_2d}\in\mathbb{R}^{2} (or "none" when not applicable). We implement two automated verifiers: a format verifier and an accuracy verifier . The resulting step-wise reward is a weighted sum of the two:

[134] table: r ~ ​ ( s , a ) = w fmt ​ r fmt + ( 1 − w fmt ) ​ r acc , w fmt ∈ [ 0 , 1 ] , \tilde{r}(s,a)\;=\;w_{\text{fmt}}\,r_{\text{fmt}}\;+\;(1-w_{\text{fmt}})\,r_{\text{acc}},\qquad w_{\text{fmt}}\in[0,1], (12)

[135] p: where r fmt r_{\text{fmt}} checks output validity and r acc r_{\text{acc}} scores action correctness. We set w fmt = 0.1 w_{\text{fmt}}=0.1 so that our reward mainly focus on action correctness.

[136] p: Format reward. The format reward r fmt r_{\text{fmt}} is 1 1 if the output contains valid <think> and <answer> tags and the <answer> block can be parsed into the required JSON schema; otherwise r fmt = 0 r_{\text{fmt}}=0 .

[137] p: Accuracy reward. The accuracy reward r acc r_{\text{acc}} evaluates semantic correctness of the predicted action: r acc = r act ⋅ r val ⋅ r g r_{\text{acc}}\;=\;r_{\text{act}}\cdot r_{\text{val}}\cdot r_{\text{g}} , where each component is computed as follows: (1) Action-type reward r act r_{\text{act}} checks whether action_type matches the demonstrated action type. (2) Value reward r val r_{\text{val}} compares the predicted value v v with the demonstrated value v ⋆ v^{\star} using word-level F1, and sets r val = 1 r_{\text{val}}=1 if F1 ⁡ ( v , v ⋆ ) > 0.5 \mathrm{F1}(v,v^{\star})>0.5 . (3) Grounding reward r g r_{\text{g}} evaluates point grounding by checking whether the predicted point 𝐮 \mathbf{u} falls inside the demonstrated bounding box b ⋆ b^{\star} , i.e., r g = 𝟏 { 𝐮 ∈ b ⋆ } r_{\text{g}}=\mathbf{1}\{\mathbf{u}\in b^{\star}\} .

[138] p: Together, these verifiers yield a step-wise signal: positive rewards indicate reliably correct predictions, whereas low rewards may arise from either incorrect actions or valid but uncredited alternatives. This design matches the partial-verifiability setting analyzed in Sec. 5.3 .

[139] figure: Figure 5 : Overall training framework of GUI-Libra: Stage 1 applies action-aware SFT with mixed supervision and token reweighting; Stage 2 performs KL-regularized GRPO with success-adaptive negative gradient scaling.

[140] h3: 5.6 Overall Training Framework for GUI-Libra

[141] p: Figure 5 summarizes the overall training framework of GUI-Libra. Based on our augmented and filtered datasets, GUI-Libra consists of two stages:

[142] p: In the SFT stage, we apply ASFT to equip the base model with action-aligned reasoning and mitigate grounding degradation caused by long CoT. ASFT mixes reasoning-then-action and direct-action supervision, and uses an action-aware reweighted objective that emphasizes action and grounding tokens.

[143] p: In the RL stage, we further optimize the policy with conservative GRPO under partially verifiable step-wise rewards. To stabilize learning and improve offline-to-online predictability, we adopt a conservative RL design with two components: (i) KL regularization to constrain distribution shift and the effect of ambiguous rewards, and (ii) success-adaptive negative gradient scaling to downweight unreliable negative updates caused by valid-but-uncredited alternatives.

[144] p: Overall, GUI-Libra promotes step-wise improvements that are behaviorally meaningful : gains in offline action matching are more likely to translate into better decisions along the policy’s own trajectories. In addition, by leveraging partially verifiable offline feedback, our framework enables scalable optimization on large static datasets without requiring costly online interaction during training.

[145] h2: 6 Experiments

[146] p: In this section, we evaluate GUI-Libra on a diverse set of offline and online GUI navigation benchmarks. Beyond overall results, we also study the impact of our key design choices in both the SFT and RL stages, and examine when offline step-wise metrics can reliably predict online task success for GUI agents.

[147] figure: Figure 6 : Limitations of current offline benchmarks. (a) Symbolic action history not in natural language in MM-Mind2Web, (b) Action type mismatch and (c) coordinate mismatch in AndroidControl.

[148] figure: Table 3 : Step accuracy Performance on AndroidControl-v2. High Level Low Level Model Pass@1 Pass@4 Pass@1 Pass@4 Proprietary Models with SeeAct-V Framework GPT-4o + UGround-v1-7B 57.0 66.3 78.4 85.4 GPT-4.1 + UGround-v1-7B 57.5 63.3 78.4 83.2 GPT-5-mini + UGround-v1-7B 52.8 58.8 77.1 83.2 GPT-5 + UGround-v1-7B 61.3 69.4 86.2 90.0 Open-source Native Models GUI-R1-3B 40.0 54.0 55.8 71.9 GUI-R1-7B 39.7 56.3 62.3 72.6 Aguvis-7B 37.7 43.7 48.0 48.7 UI-TARS-1.5-7B 45.2 63.1 48.5 70.9 GLM-4.1V-9B-Thinking 37.2 49.0 67.1 73.4 Qwen2.5-VL-32B 49.0 66.6 78.4 85.4 Qwen2.5-VL-72B 56.5 72.9 82.9 90.2 Qwen3-VL-32B 58.8 69.6 83.9 86.9 Qwen2.5-VL-3B (Baseline) 36.4 50.8 71.1 79.2 GUI-Libra-3B (Ours) 57.3 (+20.9) 67.1 (+16.3) 85.9 (+14.8) 90.5 (+11.3) Qwen2.5-VL-7B (Baseline) 46.5 58.5 67.8 81.7 GUI-Libra-7B (Ours) 59.3 (+12.8) 67.3 (+8.8) 85.2 (+17.4) 90.7 (+9.0) Qwen3-VL-4B (Baseline) 49.3 63.3 78.9 82.4 GUI-Libra-4B (Ours) 62.3 (+13.0) 68.6 (+5.3) 86.4 (+7.5) 93.0 (+10.6) Qwen3-VL-8B (Baseline) 54.8 66.1 77.6 83.2 GUI-Libra-8B (Ours) 64.3 (+9.5) 70.6 (+4.5) 88.9 (+11.3) 91.7 (+8.5)

[149] figure: Table 4 : Step accuracy Performance on Multimodal-Mind2Web-v2. Cross-Task Cross-Website Cross-Domain Average Model Pass@1 Pass@4 Pass@1 Pass@4 Pass@1 Pass@4 Pass@1 Pass@4 Proprietary Models with SeeAct-V Framework GPT-4o + UGround-v1-7B 35.7 38.9 33.9 37.6 39.1 42.2 36.2 39.6 GPT-4.1 + UGround-v1-7B 41.1 44.8 36.2 39.7 43.0 46.4 40.1 43.6 GPT-5-mini + UGround-v1-7B 44.2 48.0 40.4 44.2 45.8 48.1 43.5 46.7 GPT-5 + UGround-v1-7B 47.7 51.7 45.0 47.6 48.2 51.6 47.0 50.3 Open-source Native Models GUI-R1-3B 24.0 37.7 22.3 37.7 24.6 39.1 23.6 38.2 GUI-R1-7B 37.0 50.1 34.1 46.3 39.6 50.5 36.9 49.0 Aguvis-7B 37.7 48.0 31.7 41.5 36.9 45.1 35.4 44.9 UI-TARS-1.5-7B 37.2 48.0 31.3 42.9 35.6 47.2 34.7 46.0 GLM-4.1V-9B-Thinking 26.9 32.9 23.0 29.3 28.7 35.3 26.2 32.5 Qwen2.5-VL-32B 46.2 55.8 42.6 55.7 46.0 57.9 44.9 56.5 Qwen2.5-VL-72B 49.1 60.2 45.1 54.0 49.8 58.6 48.0 57.6 Qwen3-VL-32B 48.8 57.5 44.3 55.2 49.6 58.9 47.6 57.2 Qwen2.5-VL-3B (Baseline) 24.4 29.0 18.6 24.6 27.1 31.2 23.4 28.3 GUI-Libra-3B (Ours) 42.7 50.8 40.6 48.4 44.8 51.9 42.7 (+19.3) 50.3 (+22.0 Qwen2.5-VL-7B (Baseline) 31.6 45.6 30.4 42.1 35.6 48.0 32.5 45.2 GUI-Libra-7B (Ours) 46.3 52.8 45.5 52.2 47.6 55.7 46.5 (+14.0) 53.6 (+8.4) Qwen3-VL-4B (Baseline) 42.9 52.2 38.8 50.0 42.0 51.7 41.2 51.3 GUI-Libra-4B (Ours) 50.8 56.3 48.4 53.2 50.8 57.5 50.0 (+8.8) 55.6 (+4.3) Qwen3-VL-8B (Baseline) 44.7 54.1 41.0 51.0 45.6 53.4 43.8 52.8 GUI-Libra-8B (Ours) 51.2 55.3 47.9 53.6 52.4 56.7 50.5 (+6.7) 55.2 (+2.4)

[150] h3: 6.1 Experimental Setups

[151] h5: GUI-Libra Details.

[152] p: We train GUI-Libra models from Qwen2.5-VL-3B/7B-Instruct ( Bai et al., 2025b ) and Qwen3-VL-4B/8B-Instruct ( Bai et al., 2025a ) . We use GUI-Libra-81K for SFT and a downsampled 40K subset for RL. For SFT , we use a learning rate of 1 × 10 − 5 1\times 10^{-5} with an effective batch size of 256, and set ASFT weights to α a = 2 \alpha_{a}=2 and α g = 4 \alpha_{g}=4 by default. To ensure fair comparison, we train baselines on GUI-Libra-81K for two epochs, while models trained with mixed reasoning and direct-action data (double size) for one epoch. Notably, our SFT corpus is substantially smaller than those used in recent GUI models ( Yang et al., 2025c ; Liu et al., 2025c ) and we do not include any direct grounding-only data (e.g., low-level instructions paired with coordinate supervision), focusing on GUI reasoning and multi-step navigation. For RL , we use a learning rate of 1 × 10 − 6 1\times 10^{-6} , rollout batch size 256, group size 8, and KL coefficient 0.005 (7B) or 0.001 (others). While SNGS can improve performance, it is sensitive to hyperparameters; therefore, for ablations unrelated to SNGS, we use KL-regularized GRPO to isolate the effects of the other components. Additional implementation details are provided in Appendix B .

[153] h5: Evaluation Benchmarks.

[154] p: We evaluate models on both offline and online benchmarks. For offline evaluation , we follow UGround ( Gou et al., 2025 ) but substantially refine the underlying datasets to improve annotation quality and realism. As illustrated in Figure 6 , the original MM-Mind2Web ( Zheng et al., 2024 ) uses symbolic action histories that do not reflect real-world usage, while AndroidControl ( Li et al., 2024 ) contains roughly 20% errors in action types and coordinates. To address these issues, we enhance AndroidControl and MM-Mind2Web by correcting label errors and translating non-natural symbolic action histories, yielding AndroidControl-v2 and Multimodal-Mind2Web-v2 (MM-Mind2Web-v2) , respectively. We report step success rate, which requires the predicted action type, textual value, and coordinates to be correct, and include both Pass@1 and Pass@4 step accuracy. For AndroidControl-v2, following UGround ( Gou et al., 2025 ) , we evaluate on 398 filtered samples with both high-level and low-level instructions. For online evaluation , we use AndroidWorld ( Rawles et al., 2025 ) , WebArena-Lite-v2 ( Liu et al., 2025c ) , and Online-Mind2Web ( Xue et al., 2025 ) , which assess agents in realistic interactive environments. Notably, Online-Mind2Web is evaluated on live websites, introducing additional real-world variability and complexity. We follow the official protocols and report task success rate as the primary metric, with a maximum of 20 steps for AndroidWorld, 15 for WebArena-Lite-v2, and 30 for Online-Mind2Web. Additional details are provided in Appendix C .

[155] h5: Baselines.

[156] p: We compare GUI-Libra series against a diverse set of native GUI agents, including Qwen2.5-VL-3/7/32/72B ( Bai et al., 2025b ) , Qwen3-VL-4/8/32B ( Bai et al., 2025a ) , Aguvis-7B ( Xu et al., 2025c ) , UI-TARS-1.5-7B ( Qin et al., 2025b ) , GLM-4.1-V-9B-Thinking ( Hong et al., 2025 ) , and GUI-R1-3/7B ( Luo et al., 2025 ) . We also evaluate proprietary models paired with a grounding module, following UGround ( Gou et al., 2025 ) , including GPT-4o, GPT-4.1, GPT-5-mini, and GPT-5, and include reported/reproduced results from ScaleCUA ( Liu et al., 2025c ) on the two online benchmarks. Because evaluation pipelines can substantially affect reported performance and are often unreleased by previous work, we make our best effort to evaluate all models under a unified and consistent protocol for fair comparison.

[157] figure: Figure 7 : Trajectory Example of GUI-Libra-7B on AndroidWorld.

[158] h3: 6.2 Performance on Offline and Online GUI Navigation Benchmarks

[159] h4: 6.2.1 Offline Benchmarks

[160] p: Tables 3 and 4 report step-wise accuracy on AndroidControl-v2 and MM-Mind2Web-v2, comparing GUI-Libra with open-source native GUI models and proprietary systems using the SeeAct-V ( Zheng et al., 2024 ) framework. Overall, the GUI-Libra series achieves the best Pass@1 performance on both benchmarks, outperforming not only similarly sized models but also several substantially larger open-source and proprietary models. Importantly, GUI-Libra consistently improves over its corresponding base models. For example, GUI-Libra-3B improves Pass@1 over Qwen2.5-VL-3B by + 20.9 +20.9 and + 14.8 +14.8 on AndroidControl-v2 high-level and low-level tasks, respectively, and by + 19.3 +19.3 on the average Pass@1 of MM-Mind2Web-v2. We also observe a clear scaling trend for both Qwen baselines and GUI-Libra models, indicating that larger models have greater potential to achieve strong offline decision-making performance. In terms of Pass@4, large models (e.g., Qwen2.5-VL-72B and Qwen3-VL-32B) can be competitive, but they rely on substantially more parameters. In contrast, GUI-Libra is more parameter-efficient and consistently outperforms models at similar scale, and even GPT5. For instance, GUI-Libra-3B improves Pass@4 over Qwen2.5-VL-3B by + 16.3 +16.3 , and + 19.3 +19.3 on AndroidControl-v2 (high-level) and MM-Mind2Web-v2, respectively.

[161] p: We further find that gains on Qwen3-based backbones are relatively smaller than those on Qwen2.5-based ones, which we attribute to Qwen3’s heavier post-training (especially RL for reasoning) that already strengthens planning and decision-making. Nevertheless, GUI-Libra still provides meaningful improvements: GUI-Libra-4/8B outperforms Qwen3-VL-4/8B by 13.0/9.5 points on Pass@1 of AndroidControl-v2 (high-level) and by 8.8/6.7 points on MM-Mind2Web-v2, demonstrating consistent benefits even with strong pretrained backbones.

[162] figure: Table 5 : Performance on the online benchmark AndroidWorld in 20 steps. ∗ denotes numbers reported by original papers. Left: Native Models (single VLM). Right: Agent Frameworks ( ≥ \geq 2 VLM modules). (a) Native Models Model Acc. UI-TARS-1.5-7B 16.5 GLM-4.1V-9B-Thinking 18.3 Qwen2.5-VL-32B 29.6 Qwen2.5-VL-72B 32.2 Qwen3-VL-32B 34.8 Qwen2.5-VL-3B (Baseline) 3.5 GUI-Libra-3B (Ours) 25.2 Qwen2.5-VL-7B (Baseline) 7.8 GUI-Libra-7B (Ours) 29.6 Qwen3-VL-4B (Baseline) 27.0 GUI-Libra-4B (Ours) 42.6 Qwen3-VL-8B (Baseline) 30.4 GUI-Libra-8B (Ours) 42.6 (b) Agent Frameworks ( ≥ \geq 2 VLM Modules) Model Additional Module Acc. Qwen2.5-VL-3B Step-wise Summary 7.0 Qwen2.5-VL-7B Step-wise Summary 15.7 Qwen3-VL-4B Step-wise Summary 36.5 Qwen3-VL-8B Step-wise Summary 39.1 ScaleCUA-3B ∗ Step-wise Summary 23.7 ScaleCUA-7B ∗ Step-wise Summary 27.2 ScaleCUA-32B ∗ Step-wise Summary 30.6 GLM-4.1V-9B-Thinking UGround-v1-7B 20.9 GPT-4o UGround-v1-7B 42.6 GPT-4.1 UGround-v1-7B 37.4 GPT-5-mini UGround-v1-7B 40.9 GPT-5 UGround-v1-7B 48.7

[163] figure: Table 6 : Performance comparison on WebArena-Lite-v2 in 15 steps. ∗ denotes numbers reported in Liu et al. (2025c) . GitLab MAP Reddit Shopping ShoppingAdmin Average Native Models Aguvis-72B ∗ - - - - - 5.8 Qwen2.5-VL-72B ∗ - - - - - 15.6 InternVL3.5-241B-A28B ∗ - - - - - 11.7 UI-TARS-1.5-7B ∗ - - - - - 20.8 UI-TARS-72B-DPO ∗ - - - - - 23.4 ScaleCUA-3B 21.7 7.7 13.2 16.5 23.6 17.2 ScaleCUA-7B 28.3 15.4 27.6 18.8 30.7 23.9 ScaleCUA-32B 34.2 10.6 26.3 16.5 33.6 24.0 Qwen2.5-VL-3B 1.7 0.0 0.0 1.7 0.0 0.8 GUI-Libra-3B (Ours) 25.8 9.6 18.4 17.6 12.1 16.7 Qwen2.5-VL-7B 8.3 1.0 2.6 7.4 2.9 4.9 GUI-Libra-7B (Ours) 25.0 10.6 26.3 26.1 22.9 22.6 Qwen3-VL-4B 17.5 5.8 10.5 13.1 10.7 11.9 GUI-Libra-4B (Ours) 29.2 10.6 34.2 30.1 17.9 24.4 Qwen3-VL-8B 15.0 5.8 17.1 17.0 19.3 15.3 GUI-Libra-8B (Ours) 31.7 17.3 35.5 26.1 25.0 26.6 Agent Framework (GPT-4o as the Planner) GPT-4o + UI-TARS-1.5-7B ( Qin et al., 2025b ) ∗ - - - - - 22.6 GPT-4o + UGround-V1-7B ( Gou et al., 2025 ) ∗ - - - - - 23.2 GPT-4o + ScaleCUA-7B ( Liu et al., 2025c ) ∗ - - - - - 28.6

[164] h4: 6.2.2 Online Benchmarks

[165] p: Tables 5 , 6 , and 7 report task success rates on AndroidWorld, WebArena-Lite-v2, and Online-Mind2Web, respectively. However, many prior works do not release their evaluation frameworks, which hinders reproducibility and can compromise fair comparison. Even open-source studies such as ScaleCUA ( Liu et al., 2025c ) report results from agent frameworks augmented with additional modules (e.g., step-wise summaries) on AndroidWorld as native agent performance. As shown in Table 5 , step-wise summaries improve Qwen3-VL-4B and Qwen3-VL-8B by 9.5 and 8.7 points over their native counterparts, respectively. To support a fair comparison, we therefore explicitly report results for true native models and agent frameworks.

[166] p: On AndroidWorld (Table 5 ), GUI-Libra substantially strengthens native GUI models across all scales. Relative to their corresponding baselines, GUI-Libra yields large and consistent gains: GUI-Libra-3B increases the success rate from 3.5 3.5 to 25.2 25.2 (+21.7) and GUI-Libra-8B from 30.4 30.4 to 42.6 42.6 (+12.2). Notably, GUI-Libra-4B/8B ( 42.6 42.6 ) surpass several much larger native models (e.g., Qwen2.5-VL-32/72B and Qwen3-VL-32B), and also match or outperform multi-module agent frameworks that add external step-wise summary modules. For example, Qwen3-VL-8B with step-wise summary reaches 39.1 39.1 , whereas our native GUI-Libra-8B achieves 42.6 42.6 . Moreover, GUI-Libra-4B/8B reaches performance comparable to strong proprietary systems such as GPT-4o ( 42.6 42.6 ) and GPT-5-mini ( 40.9 40.9 ) equipped with UGround, despite using a simpler single-VLM architecture. We further provide qualitative examples of GUI-Libra-7B successfully completing AndroidWorld tasks in Figures 7 and Appendix G .

[167] p: On WebArena-Lite-v2 (Table 6 ), a locally deployed web benchmark (rather than live websites) , GUI-Libra shows strong generalization across diverse web tasks despite being trained on only 15K web-related samples, far fewer than the web corpora used by many existing GUI models. Even in this low-data regime, GUI-Libra delivers large gains over its base models: GUI-Libra-7B improves the average success rate from 4.9 4.9 to 22.6 22.6 , and GUI-Libra-8B increases performance from 15.3 15.3 to 26.6 26.6 . These results are competitive with strong proprietary systems such as GPT-4o equipped with UI-TARS and UGround. Moreover, GUI-Libra-8B outperforms large-scale models including ScaleCUA-32B, UI-TARS-72B, and Aguvis-72B, all trained on substantially larger web datasets.

[168] p: On Online-Mind2Web (Table 7 ), which evaluates agents on live websites with real-world variability, we evaluate GUI-Libra using two independent judge models: o4-mini and WebJudge-7B ( Xue et al., 2025 ) . GUI-Libra consistently improves over its corresponding base models across all difficulty levels. In particular, GUI-Libra-8B increases the average overall score from 19.3 19.3 (Qwen3-VL-8B) to 28.0 28.0 , achieving the best result among all evaluated native models, including those with substantially more parameters. Similarly, GUI-Libra-7B improves from 15.8 15.8 (Qwen2.5-VL-7B) to 25.5 25.5 , GUI-Libra-4B from 21.7 21.7 (Qwen3-VL-4B) to 25.7 25.7 . Even at the 3B scale, GUI-Libra-3B achieves an average overall of 21.3 21.3 , a notable leap from 4.8 4.8 for Qwen2.5-VL-3B. Notably, while the ScaleCUA family performs competitively on locally deployed benchmarks, its performance is less competitive on live websites : ScaleCUA-7B and ScaleCUA-32B reach only 23.7 23.7 and 23.5 23.5 average overall, both of which are surpassed by GUI-Libra-4/7/8B. Together, these results suggest that GUI-Libra not only closes the gap between smaller open-source models and larger agents, but also provides stronger robustness and generalization in realistic, dynamically changing web environments.

[169] p: Overall, GUI-Libra delivers consistent gains on online mobile and web benchmarks, generalizing from locally deployed environments to live websites. It matches or surpasses larger models while remaining highly data-efficient, using relatively small training data, especially for the web domain.

[170] figure: Table 7 : Performance comparison on Online-Mind2Web in 30 steps using o4-mini and WebJudge-7B as judges. Model Judge o4-mini WebJudge-7B Avg. Easy Medium Hard Overall Easy Medium Hard Overall Overall Agent Framework GPT-4o + UGround-v1-7B 38.8 14.0 6.5 18.7 45.0 27.3 19.5 30.0 24.3 GPT-4.1 + UGround-v1-7B 41.3 21.7 5.2 22.7 47.5 35.0 28.6 36.7 29.7 GPT-5 + UGround-v1-7B 40.0 24.5 14.3 26.0 45.0 31.5 24.7 33.3 29.7 Native Models Qwen2.5-VL-32B 12.5 7.7 1.3 7.3 28.8 14.7 19.5 19.7 13.5 Qwen3-VL-32B 33.8 17.5 7.8 19.3 45.0 31.5 28.6 34.3 26.8 ScaleCUA-3B 30.0 4.9 2.6 11.0 37.5 18.2 11.7 21.7 16.3 ScaleCUA-7B 33.8 14.7 3.9 17.0 47.5 27.3 18.2 30.3 23.7 ScaleCUA-32B 31.3 14.7 6.5 17.0 43.8 29.4 16.9 30.0 23.5 Qwen2.5-VL-3B 3.8 0.0 1.3 1.3 16.3 7.7 1.3 8.3 4.8 GUI-Libra-3B (Ours) 28.8 9.8 5.2 13.7 47.5 21.0 24.7 29.0 21.3 Qwen2.5-VL-7B 22.5 7.7 0.0 9.7 36.3 18.9 13.0 22.0 15.8 GUI-Libra-7B (Ours) 36.3 15.4 2.6 17.7 47.5 30.8 23.4 33.3 25.5 Qwen3-VL-4B 33.8 10.5 6.5 15.7 43.8 23.8 18.2 27.7 21.7 GUI-Libra-4B (Ours) 36.3 18.2 6.5 20.0 45.0 30.1 19.5 31.3 25.7 Qwen3-VL-8B 23.8 9.8 0.0 11.0 43.8 23.1 19.5 27.7 19.3 GUI-Libra-8B (Ours) 31.3 17.5 10.4 19.3 42.5 37.8 28.6 36.7 28.0

[171] h3: 6.3 Action-aware SFT and RL Mitigate Grounding Performance Degradation

[172] p: Figure 8 analyzes how grounding performance varies with response length for the base model (Qwen2.5-VL-3B) and SFT variants trained with different strategies. We evaluate on ScreenSpot-v2, group outputs into 30-token length bins, discard bins with fewer than 20 samples, and report the average grounding accuracy within each bin. This setup enables a fine-grained analysis of how increasingly long CoT outputs affect grounding performance. As response length increases, both the base model and standard SFT exhibit a pronounced degradation in grounding accuracy, indicating that long-form reasoning interferes with precise action execution. In contrast, action-aware SFT substantially mitigates this degradation across all response lengths . By incorporating direct-action supervision, action-aware SFT supports both reasoning and no-reasoning modes. Weighted training objectives further stabilize performance under long responses. In particular, stronger weighting strategies preserve high grounding correctness even beyond 250 tokens, significantly outperforming both the base model and standard SFT.

[173] p: Table 8 reports overall grounding accuracy and average response length across different models and inference modes. Models trained with mixed data can be flexibly prompted to inference in either reasoning or no-reasoning modes, denoted as Reason and No-Reason . Across both 3B and 7B scales, mixed-data training and action-aware weighting consistently improve average grounding accuracy in both modes . For example, at the 7B scale, mixed-data SFT improves grounding accuracy in reasoning mode from 79.0% to 81.4%, while action-aware weighting further increases it to 83.4%. Despite these improvements, ASFT alone does not fully eliminate the gap between reasoning and no-reasoning modes . For instance, ASFT-3B in reasoning mode still underperforms its no-reasoning counterpart by 4.8 points, and ASFT-7B exhibits a similar 3.4-point gap, suggesting that residual interference between reasoning and grounding remains.

[174] p: This gap is largely eliminated after our RL training. GUI-Libra models achieve comparable, and even superior, grounding accuracy in reasoning mode despite producing longer responses compared to the no-reasoning mode. In particular, GUI-Libra-7B attains higher grounding accuracy in reasoning mode than in no-reasoning mode (89.3% vs. 88.5%), and GUI-Libra-3B achieves similar accuracy (83.4% vs. 83.2%) while generating substantially more tokens (176 vs. 124 and 206 vs. 59, respectively). Notably, our RL stage does not use direct grounding supervision, unlike prior work ( Luo et al., 2025 ; Lu et al., 2025 ) ; instead, it leverages step-wise data derived from high-level and multi-step tasks. These results demonstrate that RL further reshapes the policy to better align reasoning with grounding, fully mitigating grounding degradation under long CoT outputs and complementing the benefits of action-aware SFT.

[175] figure: Figure 8 : Grounding accuracy under different response lengths. Action-aware SFT strategies, including mixing direct-action data and weighted objectives, help preserve grounding accuracy under long CoT outputs. Model Name Inference Mode Average Tokens Grounding Accuracy (%) SFT-3B Reason 223.4 73.4 SFT 3B + Mixed Data No-Reason 77.3 79.4 SFT 3B + Mixed Data Reason 200.6 73.8 ASFT 3B No-Reason 67.7 81.0 ASFT 3B Reason 200.2 76.2 GUI-Libra-3B (ASFT+RL) No-Reason 59.0 83.2 GUI-Libra-3B (ASFT+RL) Reason 206.5 83.4 SFT-7B Reason 218.2 79.0 SFT 7B + Mixed Data No-Reason 69.4 85.6 SFT 7B + Mixed Data Reason 168.1 81.4 ASFT 7B No-Reason 76.3 86.8 ASFT 7B Reason 169.6 83.4 GUI-Libra-7B (ASFT+RL) No-Reason 124.4 88.5 GUI-Libra-7B (ASFT+RL) Reason 176.1 89.3 Table 8 : Grounding accuracy and average response tokens across different models and inference modes. “Reason” and “No-Reason” indicate whether explicit reasoning mode is encouraged through prompting.

[176] figure: Figure 9 : Comparison of training and evaluation metrics with and without KL regularization: (a) training reward, (b) policy entropy during training, (c) offline evaluation performance on AndroidControl-High, and (d) online evaluation performance on AndroidWorld.

[177] h3: 6.4 On the Effectiveness of KL Regularization for RL

[178] p: As analyzed in Section 5.3.2 , KL regularization theoretically controls both distribution shift and reward ambiguity, making offline step-wise metrics more reliable predictors of online task completion. To validate this empirically, we visualize training and evaluation metrics on AndroidControl-High and AndroidWorld in Figure 9 , which represent typical offline and online settings that share the same action space. We compare RL runs with and without KL regularization, using KL coefficients of 0.0 vs. 0.005 for 7B models and 0.0 vs. 0.001 for 3B models, with identical initialization. As shown in Figure 9 (a), training reward curves largely overlap across different KL settings, indicating similar reward optimization behavior. However, evaluation behavior differs markedly: in Figure 9 (c) and (d), models trained without KL regularization exhibit noticeable performance degradation despite increasing training rewards, reflecting a form of reward hacking commonly observed in RLHF. Moreover, Figure 9 (b) shows that removing KL regularization leads to a pronounced decrease in policy entropy, indicating premature policy collapse and overfitting. In contrast, a small KL penalty stabilizes policy entropy and yields more consistent offline and online performance.

[179] p: To quantitatively examine how well offline metrics predict online performance, we plot the offline and online scores of all intermediate checkpoints from both 3B and 7B models in Figure 10 . The results reveal an approximately linear relationship, supporting our theoretical analysis in Theorem . In Figure 10 (b), we report both Pearson correlation, which measures linear dependence, and Spearman correlation, which captures rank consistency between offline and online performance. Although the overall Pearson correlation is moderate ( r = 0.76 r=0.76 ), further analysis shows substantial differences across different KL regularization settings. When separating checkpoints by KL strength, models trained with KL regularization ( KL > 0 \mathrm{KL}>0 ) exhibit significantly stronger alignment between offline and online performance. As shown in Figure 10 (b), KL-regularized models achieve Pearson and Spearman correlations of 0.89 0.89 ( p < 10 − 4 p<10^{-4} ) and 0.83 0.83 ( p = 2 × 10 − 4 p=2\times 10^{-4} ), respectively, indicating strong and statistically robust dependence. In contrast, models trained without KL regularization show weaker correlations (Pearson r = 0.63 r=0.63 , p = 0.015 p=0.015 ; Spearman r = 0.53 r=0.53 , p = 0.053 p=0.053 ), with the rank correlation failing to reach conventional significance levels. Overall, these results provide strong empirical evidence that KL regularization improves training stability and enhances the predictability of online task success from offline evaluations , complementing our theoretical analysis in Section 5.3.2 .

[180] figure: Figure 10 : (a) Correlation between offline and online performance. (b) Comparison of Pearson and Spearman correlations with and without KL regularization.

[181] h3: 6.5 Ablations

[182] p: In this section, we conduct a series of ablation studies to better understand the contribution of individual designs and parameters in our pipeline on GUI navigation tasks. Specifically, we examine the impact of our data filtering strategies, analyze the role of each component in ASFT, and study the impact of different KL coefficient during RL training.

[183] figure: Figure 11 : Ablation study of data filtering at the (a) SFT and (b) RL stages. Data filtering consistently improves both Pass@1 and Pass@4 performance across three benchmarks.

[184] h5: Ablation of Data Filtering for SFT and RL.

[185] p: In Sections 4.1.4 and 4.1.5 , we introduce data filtering pipelines for both the SFT and RL stages, where approximately half of the original dataset is retained. Specifically, for SFT, we remove low-quality and ambiguous samples, while for RL, we reduce domain imbalance and early-step bias. Figure 11 reports results using a 3B base model. Across most settings, filtering consistently improves performance, with especially large gains in Pass@4. For example, in SFT, filtering improves AndroidControl-High by + 4.5 +4.5 Pass@1 and + 6.3 +6.3 Pass@4, while in RL it yields an additional + 0.5 +0.5 Pass@1 and + 3.7 +3.7 Pass@4. These results highlight the importance of data quality in both SFT and RL: focusing on a smaller but cleaner and less biased dataset can generalize better than using a larger, noisier corpus.

[186] figure: Table 9 : Ablations study on ASFT, KL regularization, and reasoning across benchmarks with Qwen2.5-VL-3B as the base model. Model MM-Mind2Web-v2 AC-v2 (High) AC-v2 (Low) AndroidWorld Pass@1 Pass@4 Pass@1 Pass@4 Pass@1 Pass@4 Base Model 23.4 28.3 36.4 50.8 71.1 79.2 3.5 SFT 28.5 36.9 45.7 59.8 73.1 83.2 5.2 SFT+ Mixed Data 30.2 42.0 45.5 64.8 72.6 85.4 11.3 ASFT 32.0 41.3 44.5 64.6 75.4 86.9 13.0 GUI-Libra w/o ASFT (KL_reg=0.0) 40.9 45.1 50.5 54.8 78.6 81.9 17.4 GUI-Libra w/o ASFT (KL_reg=0.001) 41.9 48.0 57.0 63.6 86.2 90.0 20.9 GUI-Libra (KL_reg=0.0) 43.8 49.2 49.8 58.0 87.2 91.0 21.7 GUI-Libra (KL_reg=0.001) 42.7 50.2 55.8 65.8 89.5 91.5 25.2 GUI-Libra (KL_reg=0.01) 43.4 50.6 51.5 64.8 85.9 92.0 21.7 GUI-Libra (KL_reg=0.05) 41.4 51.1 49.8 66.1 87.9 92.2 20.0 ASFT w/o CoT 35.2 41.4 40.2 56.0 71.4 87.7 5.2 GUI-Libra (KL_reg=0.001) w/o CoT 43.4 47.1 48.7 55.8 85.2 87.7 12.2 ASFT infer w/o CoT 37.1 43.8 42.7 58.3 75.6 89.2 8.7 GUI-Libra (KL_reg=0.001) infer w/o CoT 42.5 48.7 52.0 59.3 88.2 92.2 18.3

[187] h5: Ablations on ASFT and RL for Navigation Tasks.

[188] p: In Section 6.3 , we analyzed the effects of action-aware SFT and RL on mitigating grounding degradation under long CoT outputs. Here, we further examine their impact on navigation performance. Table 9 reports results on both offline and online benchmarks using the Qwen2.5-VL-3B backbone. We observe an improving trend on most benchmarks and metrics as we progress from the base model to SFT, mixed-data SFT, and ASFT. In particular, incorporating mixed supervision and action-aware weighting improves Pass@1 on MM-Mind2Web-v2 from 23.4 to 32.0 and on AndroidControl-v2 (High) from 36.4 to 44.5, while AndroidWorld sucess rate increases from 3.5 to 13.0. These results indicate that all components of ASFT benefit not only grounding accuracy, but also offline navigation and long-horizon online decision making. Beyond ASFT, RL brings further substantial gains. With RL training and moderate KL regularization (e.g., KL = 0.001 \mathrm{KL}=0.001 ), Pass@1 and Pass@4 on MM-Mind2Web-v2 improve by 10.7 and 8.9 points over ASFT, respectively, and AndroidWorld performance increases markedly from 13.0 to 25.2, highlighting the limitations of supervised fine-tuning alone and the importance of RL for generalization in dynamic environments.

[189] h5: Ablations of KL Regularization Coefficient.

[190] p: We further observe that the KL coefficient plays an important role in balancing Pass@1 and Pass@4 performance. As shown in Table 9 , increasing the KL coefficient generally improves Pass@4 performance, while Pass@1 may drop slightly. This trend is consistent with our observation that stronger KL regularization retains higher policy entropy. Within this trade-off, moderate regularization (e.g., KL = 0.001 \mathrm{KL}=0.001 ) yields strong and stable results across benchmarks, achieving the highest Pass@1 on AndroidControl-v2 and competitive Pass@1 and Pass@4 on MM-Mind2Web-v2, while substantially improving online performance on AndroidWorld. In contrast, overly large penalties (e.g., KL = 0.05 \mathrm{KL}=0.05 ) or removing KL regularization tend to degrade overall performance, reducing the AndroidWorld success rate to near 20.0. These results further validate that moderate KL regularization effectively balances distribution shift and reward ambiguity, whereas excessively large penalties lead to overly conservative policies .

[191] h5: Ablations of Reasoning in Model Training and Inference.

[192] p: We analyze the role of reasoning in both training and inference by systematically ablating CoT usage in ASFT and GUI-Libra, as summarized in Table 9 . We first consider models trained without CoT and evaluated without CoT (denoted as ASFT w/o CoT and GUI-Libra w/o CoT ) . Compared to models trained and evaluated with CoT, performance degrades across most benchmarks, with the most pronounced drops on the online benchmark AndroidWorld: GUI-Libra’s success rate decreases from 25.2 to 12.2, and ASFT drops from 13.0 to 5.2. The declines are substantially larger than those observed on offline benchmarks, highlighting the importance of CoT for generalization in dynamic online environments.

[193] p: Next, we remove CoT only at inference time (denoted as ASFT infer w/o CoT and GUI-Libra infer w/o CoT ) , while using checkpoints trained with CoT. Since ASFT incorporates direct-action supervision, these models can be prompted to produce direct actions at inference. Under this setting, ASFT shows improved performance on several offline benchmarks, such as MM-Mind2Web-v2 and AndroidControl-v2 (Low), compared to inference with CoT, but still exhibits a notable drop on AndroidWorld (13.0 → \rightarrow 8.7). In contrast, GUI-Libra consistently degrades on both offline and online benchmarks (except AndroidControl-v2 (Low)) when CoT is removed at inference. This suggests that ASFT can benefit from direct-action inference on in-distribution tasks, whereas RL relies more strongly on the joint presence of reasoning traces and actions to leverage their coupling for decision making. Importantly, across all ablations, training with CoT consistently yields better performance than removing CoT during training, even when inference is ultimately performed without CoT. Overall, these results highlight that explicit reasoning during both training and inference is important for effective GUI agent, especially for strong online generalization.

[194] figure: Table 10 : Comparison between GUI-Libra w/ SNGS and w/o SNGS across benchmarks. Model MM-Mind2Web-v2 AC-v2 (High) AC-v2 (Low) AndroidWorld WebArena-Lite-v2 Pass@1 Pass@4 Pass@1 Pass@4 Pass@1 Pass@4 GUI-Libra-4B (w/o SNGS) 49.1 55.1 59.8 69.9 87.7 92.0 39.1 22.2 GUI-Libra-4B (w/ SNGS) 50.0 55.6 62.3 68.6 86.4 93.0 42.6 24.4

[195] h5: Ablation of SNGS.

[196] p: Table 10 examines the effect of SNGS on GUI-Libra-4B. Overall, enabling SNGS consistently improves online generalization, boosting performance on both AndroidWorld and WebArena-Lite-v2. For example, GUI-Libra-4B improves from 39.1 → \rightarrow 42.6 (+3.5) on AndroidWorld and from 22.2 → \rightarrow 24.4 (+2.2) on WebArena-Lite-v2, respectively. On offline benchmarks, SNGS yields smaller but generally positive gains on reasoning-demanding settings such as AndroidControl-v2 (High) and MM-Mind2Web-v2. These gains come with minor trade-offs on low-level metrics, i.e., AndroidControl-v2 (Low) Pass@1, suggesting that SNGS reduces overfitting to short-horizon action prediction and instead favors generalizable reasoning and more robust online behavior.

[197] figure: Table 11 : Effect of mixing grounding data into RL training on ScreenSpot-v2 (SS-v2), ScreenSpot-Pro (SS-Pro), MM-Mind2Web-v2, and AndroidControl-v2 (AC-v2). We report Pass@1 on all benchmarks. Green arrows indicate performance gains, and red arrows indicate degradations relative to the corresponding GUI-Libra models. SS-v2 SS-Pro MM-Mind2Web-v2 AC-v2 (high) AC-v2 (low) Qwen3-VL-4B 91.7 52.8 41.2 49.3 78.9 GUI-Libra-4B 92.3 54.3 49.1 59.8 87.7 GUI-Libra-4B + Mix Grounding 20k 94.6 ↑ \uparrow (+2.3) 61.4 ↑ \uparrow (+7.1) 43.9 ↓ \downarrow (-5.2) 61.3 ↑ \uparrow (+1.5) 84.9 ↓ \downarrow (-2.8) Qwen3-VL-8B 92.1 52.7 43.8 54.8 77.6 GUI-Libra-8B 90.7 54.1 50.3 65.6 88.7 GUI-Libra-8B + Mix Grounding 20k 94.8 ↑ \uparrow (+4.1) 59.9 ↑ \uparrow (+5.8) 49.5 ↓ \downarrow (-0.8) 61.7 ↓ \downarrow (-3.9) 86.4 ↓ \downarrow (-2.3)

[198] h3: 6.6 RL with Mixed Navigation and Grounding Data

[199] p: Prior work ( Yang et al., 2025b ; Luo et al., 2025 ; Lu et al., 2025 ) shows that adding direct grounding supervision (element descriptions paired with coordinates) during RL can substantially improve visual localization. To study how this supervision affects both grounding and reasoning, we take the grounding dataset from ( Yang et al., 2025b ) , downsample 20K examples, and mix it with our 40K navigation-focused RL dataset for joint training. We convert grounding samples into our unified action format by keeping only click actions, and apply the same reward computation as in our RL pipeline. Table 11 reports results on grounding benchmarks (ScreenSpot-v2 and ScreenSpot-Pro) and navigation benchmarks (MM-Mind2Web-v2 and AndroidControl-v2). We observe a clear trade-off. Mixing grounding data consistently improves grounding accuracy on ScreenSpot-v2 and ScreenSpot-Pro by 2–7 points, indicating stronger visual localization. In contrast, performance on navigation benchmarks generally declines, suggesting weaker reasoning and decision making. Overall, these results reveal competing optimization pressures: adding direct grounding supervision strengthens spatial alignment, but can reduce performance on reasoning-intensive navigation tasks .

[200] h2: 7 Conclusion

[201] p: We introduce GUI-Libra, a unified framework for training reasoning-capable native GUI agents based on our curated GUI-Libra-81K dataset. The key takeaway is that competitive long-horizon navigation can be obtained by fully leveraging existing trajectory corpora with a carefully designed post-training pipeline: action-aware SFT preserve grounding performance under long reasoning traces and conservative RL that improves decision making from partially verifiable feedback by controlling policy drift. Across diverse mobile and web benchmarks, GUI-Libra achieves strong offline and online results with favorable data and parameter efficiency, without relying on expensive online interaction during training. Beyond benchmark gains, we analyze the effects of key design choices in ASFT and RL, and show that GUI-Libra makes offline evaluation more reliable and more predictive of online task success, an important property for real-world deployment. We hope our findings and released resources will encourage further work on data-efficient and reliable learning frameworks for interactive GUI agents in real-world settings.

[202] h2: Limitations

[203] p: Our work focuses on learning from existing open-source datasets. While this setting is meaningful and our results suggest that current trajectory corpora still have substantial untapped potential, we train on a relatively limited amount of data and do not explore how to extend the framework to fully online, interactive training. As more large-scale open-source GUI interaction data become available ( He et al., 2025 ; Wang et al., 2025d ; Zhang et al., 2025a ) , scaling our pipeline to incorporate broader and more diverse trajectories is a promising direction. In addition, fully online RL can be expensive, slow, and typically requires robust infrastructure and careful system design. We leave a systematic study of extending our framework to fully online scheme as future work.

[204] h2: Acknowledgments

[205] p: The authors thank Hao Bai, Chenlu Ye, and Xiao Yu for valuable discussions, and Boyu Gou and Yiheng Xu for guidance on benchmark and model evaluation.

[206] h2: References

[207] h2: Appendix A Additional Related Works

[208] h5: Reinforcement Learning from Verifiable Rewards (RLVR)

[209] p: To optimize LLMs, learning a reward model as the training signal is a common practice in reinforcement learning from human feedback (RLHF) ( Ouyang et al., 2022 ; Wang et al., 2023 ; Yang et al., 2024b ) . However, reward models are known to suffer from reward hacking and misalignment issues ( Gao et al., 2023 ; Yang et al., 2024a ) . To address these limitations, recent work has shifted toward verifiable rewards , where supervision is derived from ground-truth verifiers, such as exact mathematical answer matching or code execution, rather than from a learned and potentially ambiguous reward model. Shao et al. (2024) introduce GRPO, which enables effective policy optimization from such verifiable signals and demonstrates the emergence of complex reasoning behaviors. Building on this framework, DAPO ( Yu et al., 2025 ) and Dr. GRPO ( Liu et al., 2025d ) propose simple yet effective techniques, such as more aggressive clipping and dynamic sampling, to stabilize training and mitigate learning bias in GRPO. More recently, GSPO ( Zheng et al., 2025a ) leverages sequence-level importance sampling to further improve training stability, particularly for mixture-of-experts models. Despite their success, we find that directly applying RLVR recipes to step-wise agent training often leads to suboptimal policies, due to distribution shift and ambiguous intermediate rewards.

[210] h5: Post-training for VLM-based Agents.

[211] p: VLMs have demonstrated strong capabilities in visual perception and multimodal reasoning ( OpenAI et al., 2024 ; Bai et al., 2025b ; Bai et al., 2025a ; Zheng et al., 2024 ) . However, deploying them as agents in visually grounded environments requires moving beyond static understanding toward robust, long-horizon decision-making. To bridge the gap, recent research adopts a two-stage SFT-then-RL paradigm ( Chen et al., 2025a ; Zhai et al., 2024 ; Zhan et al., 2025 ) . In the first stage, SFT equips VLMs with essential agentic skills, including visual grounding, structured reasoning, and action prediction through curated dataset ( Hong et al., 2024 ; Cheng et al., 2024a ; Wu et al., 2024 ; Lin et al., 2024 ; Qin et al., 2025a ; Xu et al., 2025b ) . Nevertheless, SFT is inherently limited by the coverage and diversity of demonstrations, therefore prone to compounding errors when encountering out-of-distribution states ( Chen et al., 2025a ; Liu et al., 2026 ; Deng et al., 2025 ) . RL complements SFT by enabling agents to interact directly with environments. Through exploration, agents can learn from both successes and failures, gradually developing capabilities such as error recovery, self-correction, and long-horizon planning ( Bai et al., 2024a ; Qi et al., 2025 ; Putta et al., 2024 ; Feng et al., 2025 ; Wang et al., 2025c ) . Under this two-stage paradigm, SFT first establishes a stable foundation of core skills, after which RL enhances long-horizon decision-making via environment interaction and policy optimization.

[212] h2: Appendix B Implementation Details

[213] h5: Action Space.

[214] p: We model GUI interaction with a unified action space where each step outputs a structured tuple (action_type, action_target, value, point_2d) . Here, action_type specifies the operation (e.g., Click , Write , Scroll ), action_target describes the target UI element when applicable, and value provides additional arguments such as input text, scroll/swipe direction, key name, waiting time, or app name. For actions that require spatial grounding (e.g., Click , LongPress , and optionally Swipe or Write ), point_2d records the screen coordinate [x,y] ; otherwise it is set to None . This unified schema supports both web and mobile environments, including device-level controls (e.g., NavigateBack , NavigateHome , OpenApp ) and a terminal action Terminate . See Table 12 for the full specification. Following the base model’s coordinate system, we use absolute pixel coordinates for Qwen2.5-VL-based models, and normalized coordinates in [ 0 , 1000 ] [0,1000] for Qwen3-VL-based models.

[215] figure: Table 12 : Unified action space. Each action is a tuple (action_type, action_target, value, point_2d) . action_type action_target value point_2d details Answer None answer text [-100,-100] Return the final answer to the user’s question. Click element description None [x,y] Tap/click a specific UI element and provide its coordinates. Select element description option value [-100,-100] Select an item in a list or dropdown menu. LongPress element description None [x,y] Press-and-hold on a UI element (mobile only) and provide its coordinates. Write element description or None input text [x,y] or [-100,-100] Enter text into a specific input field; if point_2d is [-100,-100] , type at the current focus. KeyboardPress None key name (e.g., enter ) [-100,-100] Press a specific key on the keyboard. Scroll None direction ( up / down / left / right ) [-100,-100] Scroll a view/container in the specified direction. Swipe element description or None direction ( up / down / left / right ) [x,y] or [-100,-100] Perform a swipe gesture on a touchscreen in the given direction; provide coordinates if applicable. Wait None seconds [-100,-100] Pause execution for a specified duration to allow UI updates. NavigateHome None None [-100,-100] Navigate to the device’s home screen. NavigateBack None None [-100,-100] Press the system “Back” button. OpenApp None app name [-100,-100] Launch an app by its name (mobile only). Terminate None end-task message [-100,-100] Signal the end of the current task with a final message.

[216] h5: SFT.

[217] p: We summarize our shared SFT and Action-aware SFT implementation parameters in Table 13 . We apply full parameter tuning on Qwen2.5-VL and Qwen3-VL base models from 3B,4B, to 7B and 8B. We use a learning rate of 1 × 10 − 5 1\times 10^{-5} and an effective batch size of 256. We train SFT and ASFT models for either two epochs on GUI-Libra-81K or 1 epoch on mixing reasoning and direct-action data (it doubles data size). For action-aware SFT, we by default use α a = 2 \alpha_{a}=2 and α g = 4 \alpha_{g}=4 for ASFT, except for GUI-Libra-4B, where α a = α g = 1 \alpha_{a}=\alpha_{g}=1 . We use 8 B200 GPUs for approximately 4 hours for Qwen3-VL-4B and 5.5 hours for Qwen3-VL-8B.

[218] figure: Category Configuration Backbone Qwen2.5-VL / Qwen3-VL Training Strategy Full-parameter fine-tuning Epochs 1 Learning Rate 1 × 10 − 5 1\times 10^{-5} Scheduler Cosine Warmup Ratio 0.01 Weight Decay 0 Per-device Batch Size 4 Gradient Accumulation Steps 8 Effective Batch Size 256 (8 GPUs) Gradient Checkpointing Enabled Table 13: SFT configuration used in our experiments.

[219] h5: RL.

[220] p: We adopt GRPO ( Shao et al., 2024 ) as our RL algorithm, implemented with the verl framework 1 1 1 https://github.com/verl-project/verl and EasyR1 2 2 2 https://github.com/hiyouga/EasyR1 . GUI-Libra is initialized from the SFT/ASFT checkpoints and further optimized via online rollouts. At each iteration, the model samples trajectories, computes step-wise rewards, and updates the policy using the GRPO objective. We train for 300 RL iterations with a learning rate of 1 × 10 − 6 1\times 10^{-6} , global batch size 128, and rollout group size n = 8 n=8 . We set the KL regularization coefficient to 0.001 by default and increase it to 0.005 for GUI-Libra-7B to improve training stability. For SNGS, we use model-specific ( λ 0 , κ ) (\lambda_{0},\kappa) : ( 0.9 , 0.5 ) (0.9,0.5) for 3B, ( 1.4 , − 0.5 ) (1.4,-0.5) for 7B, ( 0.5 , 1.5 ) (0.5,1.5) for 4B, and ( 0.5 , 2.0 ) (0.5,2.0) for 8B. Training is conducted on 8 NVIDIA B200 GPUs and takes approximately 16 hours for Qwen3-VL-4B and 20 hours for Qwen3-VL-8B.

[221] figure: Category Configuration RL Training Framework VERL Distributed Training Backend FSDP Inference Engine vLLM Backbone Qwen2.5-VL, Qwen3-VL Rollout Rollout Samples per Prompt 8 Rollout Batch Size 256 Sampling Strategy Top- p p 0.98 Temperature 1.0 Max Prompt Length 8092 Max Response Length 1500 Optimization Training Iterations 300 Learning Rate 1 × 10 − 6 1\times 10^{-6} Optimizer AdamW (bf16) Global Batch Size 128 Micro Batch (Update) 4 Micro Batch (Experience) 8 Clip Ratio ( ϵ \epsilon ) 0.2 KL Coefficient ( β \beta ) 0.001 by default, and 0.005 for GUI-Libra-7B Algorithm Advantage Estimator GRPO, GRPO w/ SNGS Reward Function r ~ ​ ( s , a ) = w fmt ​ r fmt + ( 1 − w fmt ) ​ r acc , w fmt = 0.1 \tilde{r}(s,a)\;=\;w_{\text{fmt}}\,r_{\text{fmt}}\;+\;(1-w_{\text{fmt}})\,r_{\text{acc}},w_{\text{fmt}}=0.1 Table 14: RL configuration for our experiments.

[222] h5: Evaluation.

[223] p: For inference, we use vLLM as the serving backend. We set the temperature to 0.0 and top- p p to 1.0, and allow up to 1024 completion tokens by default. The system prompt follows Appendix F . The available action list within the system prompt can be adjusted depending on the deployment environment. For example, if a mobile environment does not support the OpenAPP action, it can be removed from the action list; in this case, the model typically resorts to alternative strategies such as scrolling to access the app drawer.

[224] p: For models trained with mixed direct-action data, we optionally use an explicit instruction prompt to elicit direct action generation without intermediate reasoning. Specifically, we can append the following format instruction after user instruction:

[225] h2: Appendix C Benchmark Details

[226] p: In our experiments, we adopt a diverse of benchmarks for evaluation, mainly focus on GUI navigation benchmarks that measures step-wise success or task-level completion. We also use grounding benchmarks to evaluate the correctness of grounding after long CoT generation. Details about these benchmarks are as follows.

[227] h3: C.1 Grounding Benchmarks

[228] p: We adopt ScreenSpot-V2 ( Cheng et al., 2024b ; Wu et al., 2025b ) and ScreenSpot-Pro ( Li et al., 2025 ) to evaluate grounding accuracy. Each task provides a short instruction specifying the target element or intent, together with a screenshot from a digital interface (mobile, desktop, or web). The ground-truth target is given as a bounding box, and we measure success by whether the model’s predicted click coordinate falls inside the box. ScreenSpot-V2 corrects labeling errors in the original ScreenSpot benchmark and contains 1,269 tasks, with most screenshots below 2560 × \times 1440 resolution. In contrast, ScreenSpot-Pro includes 1,555 tasks and features substantially higher-resolution screenshots (up to 5120 × \times 2880), resulting in denser visual content and more fine-grained targets. Overall, ScreenSpot-V2 reflects common UI settings, while ScreenSpot-Pro stresses precise grounding in high-resolution, information-rich interfaces.

[229] h3: C.2 Offline GUI Navigation Benchmarks

[230] h5: Multimodal-Mind2Web-v2

[231] p: We build our benchmark on Multimodal-Mind2Web (MM-Mind2Web) ( Zheng et al., 2024 ) , the multimodal extension of Mind2Web ( Deng et al., 2023 ) , to evaluate offline web navigation on realistic user tasks. MM-Mind2Web aligns each step in a human demonstration with a webpage screenshot (and the corresponding HTML/DOM state), forming a golden multi-step trajectory conditioned on a high-level natural-language instruction ( Deng et al., 2023 ; Zheng et al., 2024 ) . The test split spans 100+ websites; all webpages along the golden trajectories are cached to support fully offline evaluation, and tasks are crowdsourced to reflect real user intents. As shown in Figure 6 , MM-Mind2Web represents action history as symbolic records that are neither natural-language descriptions nor aligned with real user interaction. To address this, we use Qwen3-VL-32B-Instruct to rewrite each action into a natural-language description and use these descriptions as the history context. The resulting dataset, Multimodal-Mind2Web-v2 (MM-Mind2Web-v2), contains three subsets, Cross-Task, Cross-Website, and Cross-Domain, with 1,328, 1,019, and 1,002 samples, respectively. We report step success rate as the primary metric, which requires both correct target grounding ( element accuracy ) and correct operation execution. Operation correctness is measured by an exact-match F1 score (F1 = 1 =1 ) over the serialized action string “ ActionType Value ”, where Value can be the typed text for Write actions or the app/website identifier for OpenApp actions.

[232] h5: AndroidControl-v2

[233] p: AndroidControl-v2 is based on AndroidControl ( Li et al., 2024 ) , an offline Android GUI navigation benchmark that pairs step-wise instructions with mobile screenshots and demonstrated actions. However, AndroidControl contains non-trivial annotation noise (about 20% errors in action types and/or coordinates), as illustrated in Figure 6 . To improve evaluation reliability, we use Qwen3-VL-32B-Instruct to filter mismatched samples by checking the consistency between each demonstrated action and its oracle low-level step instruction. We start from a sampled set of 500 examples from UGround ( Gou et al., 2025 ) and obtain a cleaned subset of 398 examples after filtering. We evaluate under both high-level and low-level instructions and report step accuracy, where a step is counted as successful only if the predicted action type, textual value (when applicable), and target coordinates are all correct. Note that prior work may use inconsistent evaluation protocols for this benchmark. For example, OS-Atlas ( Wu et al., 2025b ) and GUI-R1 ( Luo et al., 2025 ) treat grounding as a distance-to-target threshold, which can be misleading in practice because UI elements vary greatly in size (so a fixed threshold is not comparable across screens). Instead, we follow UGround’ strategy ( Gou et al., 2025 ) : we use the accessibility tree to map the predicted coordinate to its nearest UI element, and then match that element against the ground-truth target.

[234] h3: C.3 Online GUI Navigation Benchmarks

[235] h5: AndroidWorld

[236] p: We evaluate online mobile agent performance on AndroidWorld ( Rawles et al., 2025 ) , which runs interactive tasks in Android emulators and scores agents by whether they reach the correct final device states. AndroidWorld contains 116 tasks across 20 real-world apps and covers diverse multi-step workflows (e.g., search, form filling, and settings changes) under realistic UI dynamics. With the official Docker environment, we found that Task #82 ( SimpleSmsReplyMostRecent ) cannot be initialized, so we report results on the remaining 115 tasks. Evaluation uses the benchmark’s rule-based completion checker with a maximum horizon of 20 steps. To assess self-verification, we count a task as successful only when (i) the agent explicitly outputs a Terminate action and (ii) the environment state satisfies the completion rules. Our agent follows the See-Act-V framework following UGround ( Gou et al., 2025 ) , but we remove the step-wise reflection and summary module. This design choice isolates the native capability of the underlying model, rather than relying on a hand-crafted control structure. For completeness, we also report baseline results with the summary modules, and show that our native model (without such modules) can surpass agents that depend on these additional components, highlighting the potential of our recipe to reduce human-designed scaffolding.

[237] h5: WebArena-Lite-v2

[238] p: We evaluate online web agent performance on WebArena-Lite-v2 ( Liu et al., 2025c ) , a locally deployed website environments upgraded from WebArena-Lite ( Liu et al., 2025a ) consisting of 154 tasks. To setup the website environment, we follow the instruction by Maxime Gasse 3 3 3 https://github.com/gasse/webarena-setup/tree/main/webarena for a more stable Map setup 4 4 4 We found the container for Map website is brittle when following the official WebArena-Lite-v2 setup: https://github.com/OpenGVLab/ScaleCUA/tree/main/evaluation/WebArenaLiteV2 . . Building upon the official WebArena-Lite-v2 implementation, we further improve the robustness of action parsing and execution by: (i) parsing the ”response” action as ”answer” rather than treating it as illegal; (ii) appending an automated ”terminate” action after ”action” and ”response”; (iii) supporting multi-line answer strings (separated by \n ) instead of only the first line; (iv) clearing blank content before typing predicted messages. Moreover, we replace gpt-4o-2024-11-20 with gpt-5 for more accurate LLM-based fuzzy evaluation as we observed false positives when using GPT-4o. Given the high variance in results, we report the average across four runs for all experiments, with the temperature set to 0.0 and top_p to 1.0.

[239] h5: Online-Mind2Web

[240] p: We also include Online-Mind2Web benchmark ( Xue et al., 2025 ) spanning 136 live real-world websites and covering 300 web agent tasks. We set the maximum interaction steps to 30 for each task. We adopt the proposed WebJudge method backed by either o4-mini 5 5 5 https://developers.openai.com/api/docs/models/o4-mini or WebJudge-7B 6 6 6 https://huggingface.co/osunlp/WebJudge-7B models. The LLM-based judge first identifies key points of the task, then selects task-relevant key screenshots from each step. Finally, the judge is provided with task description, agent textual actions, task completion key points and selected key screenshots to make a binary outcome judgment indicating whether all key points are satisfied.

[241] h2: Appendix D Additional Results

[242] p: This section presents additional results to further clarify our approach. We include an auxiliary study on grounding as a single-step verifiable case in Appendix D.1 to contrast with multi-step navigation under partial verifiability, a controlled comparison of reasoning-augmentation models in Appendix D.2 , as well as complementary offline metrics (grounding accuracy, action-type accuracy or operation F1) in Appendix D.4 .

[243] h3: D.1 Grounding as a Single-step Verifiable Setting

[244] p: Grounding provides a near-ideal single-step verifiable setting: each example typically refers to a specific UI element, and we can directly verify correctness by checking whether the predicted coordinate falls inside the annotated bounding box. Since the agent produces only a single action, this setting matches the assumptions in Corollary 5.3 . To study this regime, we train Qwen3-VL-4B and Qwen3-VL-8B with GRPO on a 40K downsampled grounding dataset from GTA1 ( Yang et al., 2025b ) . Results are shown in Figure 12 .

[245] p: Unlike navigation, grounding does not exhibit an offline–online evaluation gap; therefore, we assess predictability using two grounding benchmarks instead: ScreenSpot-v2 and ScreenSpot-Pro. ScreenSpot-v2 is closer to our training distribution (similar image resolution), while ScreenSpot-Pro contains substantially higher-resolution screenshots, making it a useful test of distribution shift. Figures 12 (a)–(b) show that performance on both benchmarks improves steadily and then plateaus after roughly 200 RL steps, without the significant reward-hacking-style drops observed in multi-step navigation. Moreover, the two benchmarks are strongly correlated: Figure 12 (c) shows a tight relationship between ScreenSpot-v2 and ScreenSpot-Pro scores, and Figure 12 (d) reports very high Pearson and Spearman correlations. Interestingly, removing KL regularization yields even higher correlation (Pearson ≈ 0.98 \approx 0.98 ), consistent with our analysis that in single-step, verifiable tasks, RLVR-style training can remain stable and highly predictable even without KL regularization.

[246] figure: Figure 12 : RL for grounding exhibits stable improvements and strong cross-benchmark predictability. (a) ScreenSpot-V2 and (b) ScreenSpot-Pro performance over RL training. (c) Correlation between the two benchmark scores across checkpoints. (d) Pearson and Spearman correlations with and without KL regularization.

[247] figure: Figure 13 : Performance comparison of different models for reasoning generation. All models are used to augment the same 30K web samples from AGUVIS and are fine-tuned on the same 3B base model. This controlled evaluation reveals substantial performance differences among generator models.

[248] h3: D.2 Comparing Different Models for Reasoning Augmentation

[249] p: In our reasoning augmentation pipeline, we use GPT-4.1 to generate reasoning traces. This choice is motivated by preliminary experiments showing that GPT-4.1 can be prompted to produce richer, more informative rationales for VLM training. With the same prompt, GPT-4o often generates shorter reasoning, while reasoning models such as o4-mini typically provide limited visible traces and hide their true reasoning traces, resulting in similarly short rationales. In contrast, GPT-4.1 more reliably produces detailed reasoning that provide more useful thought and better aligns with the actions.

[250] p: We further quantify this effect with a controlled comparison. Using the same 30K web samples from AGUVIS, we generate reasoning traces with each model under an identical prompt and fine-tune the same Qwen2.5-VL-3B-Instruct base model on the resulting augmented data. To isolate the impact of reasoning quality, we extract action targets from the model outputs and use the same UGround-7B-v1 ( Gou et al., 2025 ) model for coordinate prediction across all settings. Figure 13 reports results on the original MM-Mind2Web Cross-Website subset: GPT-4.1 yields the best performance, outperforming GPT-4o by + 3.7 +3.7 and o4-mini by + 2.1 +2.1 . These results indicate that the choice of reasoning generator is an important factor in effective reasoning augmentation.

[251] h3: D.3 Comparing with Uniform Negative Gradient Scaling Strategy

[252] p: In our method, we use an adaptive negative gradient scaling method to enable adaptive scaling behaviors. Table 15 compares our adaptive negative gradient scaling strategy with a uniform variant that applies a constant scaling factor λ g \lambda_{g} across all states. Uniform scaling yields weaker overall performance: both λ g = 0.75 \lambda_{g}=0.75 and λ g = 0.9 \lambda_{g}=0.9 perform worse on MM-Mind2Web-v2, AC-v2 (High/Low), and AndroidWorld. These results suggest that a single global scaling factor cannot capture the heterogeneous difficulty and ambiguity across states and can lead to suboptimal optimization, whereas adaptive scaling provides the flexibility needed to stabilize training and improve decision making.

[253] figure: Table 15 : Ablations study of negative scaling strategy on 3B base model. Model MM-Mind2Web-v2 AC-v2 (High) AC-v2 (Low) AndroidWorld Pass@1 Pass@4 Pass@1 Pass@4 Pass@1 Pass@4 GUI-Libra ( λ g = 0.75 \lambda_{g}=0.75 ) 42.2 48.5 54.5 64.1 86.7 90.2 19.1 GUI-Libra ( λ g = 0.9 \lambda_{g}=0.9 ) 42.7 48.1 52.3 61.1 87.4 90.7 20.0 GUI-Libra 42.7 50.2 55.8 65.8 89.5 91.5 25.2

[254] h3: D.4 Additional Metrics on Offline Benchmarks

[255] p: In our main offline evaluations, we use step accuracy as the primary metric. To better understand where the gains come from, we also report decomposed metrics that separate grounding from action prediction. Specifically, we report (i) grounding accuracy (whether the predicted coordinate lies inside the target element) and action-type accuracy on AndroidControl-v2, and (ii) grounding accuracy and operation F1 on MM-Mind2Web-v2. Operation F1 is computed following the protocol in Appendix C.2 .

[256] h5: AndroidControl-v2.

[257] p: Tables 16 and 17 show that GUI-Libra remains strong under these more fine-grained metrics. Notably, GUI-Libra-8B achieves the best Pass@1 grounding accuracy on both high-level and low-level tasks, reaching 76.3 and 95.5 Pass@1 on the high-level and low-level settings, respectively. It also outperforms GPT-5 + UGround-7B-v1 and larger open-weight models (e.g., 32B and 72B). The overall trend for action-type accuracy is similar, but the gaps to strong baselines are smaller, suggesting that our improvements are driven primarily by better grounding rather than action-type prediction. This is expected: action types are often inferred reliably from language and prior knowledge, whereas accurate grounding, especially for high-level, goal-directed tasks, is more challenging for GUI tasks.

[258] h5: MM-Mind2Web-v2.

[259] p: Tables 18 and 19 report grounding accuracy and operation F1, respectively. For grounding, GUI-Libra-8B achieves the highest Pass@1 across all three subsets, with an average Pass@1 of 57.8, surpassing strong baselines including Qwen3-VL-32B, Qwen2.5-VL-72B, and GPT-5 with UGround. For Pass@4, Qwen2.5-VL-72B is 1.4 points higher than GUI-Libra-8B, indicating that web-domain evaluation can still benefit from additional model capacity and/or web-specific training data. We attribute this gap mainly to domain imbalance in our training set: roughly 85% of our SFT data comes from mobile, with only 15% from web. We expect that scaling high-quality web data would further improve Pass@4, consistent with our strong Pass@1/Pass@4 results on AndroidControl-v2. For operation F1, we report Best@N (the maximum over N ∈ { 1 , 4 } N\!\in\!\{1,4\} samples), since F1 is a continuous score in [ 0 , 1 ] [0,1] . While larger models achieve strong Best@4 results, GUI-Libra-7B attains the best Best@1 performance (85.1), and GUI-Libra-3B remains competitive with 32B–72B baselines.

[260] p: Overall, these additional metrics show that GUI-Libra improves not only step accuracy but also its underlying components, providing a more complete view of the sources of improvement.

[261] figure: Table 16 : Grounding Accuracy on AndroidControl-v2. High Level Low Level Model Pass@1 Pass@4 Pass@1 Pass@4 Proprietary Models with SeeAct-V Framework GPT-4o + UGround-v1-7B 58.7 67.3 83.4 88.3 GPT-4.1 + UGround-v1-7B 60.5 64.6 83.0 86.1 GPT-5-mini + UGround-v1-7B 61.9 66.8 83.9 87.9 GPT-5 + UGround-v1-7B 74.4 82.1 93.7 94.6 Open-source Native Models GUI-R1-3B 53.4 66.4 81.2 87.0 GUI-R1-7B 58.3 72.2 87.9 87.9 Aguvis-7B 67.3 78.0 85.7 87.0 UI-TARS-1.5-7B 57.9 71.3 78.5 88.8 GLM-4.1V-9B-Thinking 44.0 55.6 68.2 75.8 Qwen2.5-VL-32B 49.0 66.6 78.4 85.4 Qwen2.5-VL-72B 56.5 72.9 82.9 90.2 Qwen3-VL-32B 70.9 79.4 91.9 93.3 Qwen2.5-VL-3B (Baseline) 42.2 46.6 78.0 80.7 GUI-Libra-3B (Ours) 68.2 77.1 89.2 91.5 Qwen2.5-VL-7B (Baseline) 60.5 69.5 82.5 88.3 GUI-Libra-7B (Ours) 71.8 78.0 91.5 93.7 Qwen3-VL-4B (Baseline) 65.9 76.7 90.6 93.3 GUI-Libra-4B (Ours) 74.0 81.6 91.0 95.1 Qwen3-VL-8B (Baseline) 67.7 79.8 93.3 95.1 GUI-Libra-8B (Ours) 76.2 81.6 95.5 96.4

[262] figure: Table 17 : Type Accuracy on AndroidControl-v2. High Level Low Level Model Pass@1 Pass@4 Pass@1 Pass@4 Proprietary Models with SeeAct-V Framework GPT-4o + UGround-v1-7B 73.9 82.7 89.2 93.7 GPT-4.1 + UGround-v1-7B 72.9 78.9 89.5 93.0 GPT-5-mini + UGround-v1-7B 70.9 77.4 89.7 93.5 GPT-5 + UGround-v1-7B 74.1 78.9 88.4 91.5 Open-source Native Models GUI-R1-3B 63.1 76.4 71.1 90.2 GUI-R1-7B 61.8 76.1 76.1 89.2 Aguvis-7B 58.0 59.8 60.6 62.1 UI-TARS-1.5-7B 69.4 87.4 70.9 91.0 GLM-4.1V-9B-Thinking 65.8 74.1 89.2 92.5 Qwen2.5-VL-32B 67.3 78.1 85.7 89.7 Qwen2.5-VL-72B 72.9 86.9 89.5 96.2 Qwen3-VL-32B 73.6 81.2 90.2 92.2 Qwen2.5-VL-3B (Baseline) 53.0 77.4 80.2 90.0 GUI-Libra-3B (Ours) 70.4 78.1 89.5 93.7 Qwen2.5-VL-7B (Baseline) 62.8 77.4 78.6 91.7 GUI-Libra-7B (Ours) 72.9 78.6 88.9 91.2 Qwen3-VL-4B (Baseline) 63.6 78.4 86.4 88.7 GUI-Libra-4B (Ours) 72.6 76.1 92.5 95.0 Qwen3-VL-8B (Baseline) 68.8 77.6 82.4 86.9 GUI-Libra-8B (Ours) 74.1 78.9 93.7 95.5

[263] figure: Table 18 : Grounding accuracy (%) on Multimodal-Mind2Web-v2. Cross-Task Cross-Website Cross-Domain Average Model Pass@1 Pass@4 Pass@1 Pass@4 Pass@1 Pass@4 Pass@1 Pass@4 Proprietary Models with SeeAct-V Framework GPT-4o + UGround-v1-7B 42.0 44.0 40.6 42.9 44.9 47.2 42.5 44.7 GPT-4.1 + UGround-v1-7B 47.4 49.3 43.5 45.5 48.7 51.4 46.5 48.7 GPT-5-mini + UGround-v1-7B 52.5 53.1 50.7 51.6 53.6 54.3 52.3 53.0 GPT-5 + UGround-v1-7B 55.3 56.6 53.1 53.4 55.8 57.3 54.7 55.8 Open-source Native Models GUI-R1-3B 29.1 44.6 27.2 45.5 29.1 44.9 28.5 45.0 GUI-R1-7B 43.8 56.8 40.6 54.9 45.7 56.3 43.4 56.0 Aguvis-7B 40.5 53.5 34.9 47.4 38.8 48.8 38.1 49.9 UI-TARS-1.5-7B 46.2 59.0 42.2 57.6 46.4 60.2 45.0 58.9 GLM-4.1V-9B-Thinking 36.8 42.8 34.2 39.7 36.9 44.1 36.0 42.2 Qwen2.5-VL-32B 53.0 61.8 50.9 61.6 52.6 62.9 52.2 62.1 Qwen2.5-VL-72B 55.7 65.0 53.7 61.5 56.3 64.4 55.2 63.6 Qwen3-VL-32B 55.9 62.4 52.7 61.7 56.7 63.9 55.1 62.7 Qwen2.5-VL-3B (Baseline) 37.9 40.1 35.6 38.6 38.8 43.2 37.4 40.6 GUI-Libra-3B (Ours) 50.1 57.8 50.7 58.6 51.6 58.5 50.8 58.3 Qwen2.5-VL-7B (Baseline) 44.1 54.0 45.5 54.2 46.2 57.4 45.3 55.2 GUI-Libra-7B (Ours) 53.5 59.8 54.2 60.4 53.6 60.7 53.7 60.3 Qwen3-VL-4B (Baseline) 49.9 59.6 47.9 58.2 49.9 57.5 49.2 58.4 GUI-Libra-4B (Ours) 57.2 61.7 56.2 61.4 56.7 62.1 56.7 61.7 Qwen3-VL-8B (Baseline) 52.6 60.0 49.6 59.3 52.4 59.3 51.5 59.5 GUI-Libra-8B (Ours) 58.6 62.6 56.5 61.2 58.2 62.5 57.8 62.1

[264] figure: Table 19 : Operation F1 score on Multimodal-Mind2Web-v2. Cross-Task Cross-Website Cross-Domain Average Model Best@1 Best@4 Best@1 Best@4 Best@1 Best@4 Best@1 Best@4 Proprietary Models with SeeAct-V Framework GPT-4o + UGround-v1-7B 70.1 78.9 70.9 79.6 67.7 75.7 69.6 78.1 GPT-4.1 + UGround-v1-7B 72.7 81.6 71.1 81.0 71.1 79.4 71.6 80.7 GPT-5-mini + UGround-v1-7B 80.7 88.8 77.3 86.8 77.9 85.3 78.6 87.0 GPT-5 + UGround-v1-7B 79.7 89.2 79.6 88.9 79.1 88.2 79.5 88.8 Open-source Native Models GUI-R1-3B 79.5 87.9 75.4 85.3 79.6 89.4 78.1 87.5 GUI-R1-7B 78.9 89.6 75.2 88.5 79.8 90.7 78.0 89.6 Aguvis-7B 84.4 91.1 80.7 87.9 83.3 91.5 82.8 90.2 UI-TARS-1.5-7B 81.2 85.3 78.5 81.6 81.1 85.0 80.3 84.0 GLM-4.1V-9B-Thinking 73.6 82.0 69.2 80.0 73.7 81.6 72.2 81.2 Qwen2.5-VL-32B 84.2 92.6 81.9 92.0 82.6 93.0 82.9 92.5 Qwen2.5-VL-72B 85.2 93.5 83.3 91.5 84.3 93.0 84.3 92.7 Qwen3-VL-32B 83.9 91.6 81.3 89.9 83.7 92.2 83.0 91.2 Qwen2.5-VL-3B (Baseline) 59.3 86.5 51.6 83.0 64.7 88.3 58.5 85.9 GUI-Libra-3B (Ours) 84.6 88.0 80.8 85.2 86.4 89.2 83.9 87.5 Qwen2.5-VL-7B (Baseline) 68.1 90.9 66.7 90.4 73.3 91.6 69.4 91.0 GUI-Libra-7B (Ours) 85.2 88.1 84.3 88.2 85.9 89.4 85.1 88.6 Qwen3-VL-4B (Baseline) 81.6 88.9 78.9 88.2 79.5 89.9 80.0 89.0 GUI-Libra-4B (Ours) 85.0 88.9 83.6 88.2 82.8 88.1 83.8 88.4 Qwen3-VL-8B (Baseline) 83.2 91.2 80.0 89.0 82.7 90.2 82.0 90.1 GUI-Libra-8B (Ours) 85.5 88.1 81.8 86.9 84.4 87.0 83.9 87.3

[265] h2: Appendix E Proofs for Theoretical Analysis

[266] p: This section provides detailed proofs for the theoretical results in Sec. 5.3 .

[267] h4: E.0.1 When does offline step-wise matching predict online success?

[268] h6: Theorem E.1 .

[269] p: Offline-to-online bound under partial verifiability (Restatement of Theorem )off2on_app Assume Assumption 5.1 and that, for all t ∈ [ H ] t\in[H] , d π , t ​ ( s ) > 0 d_{\pi,t}(s)>0 implies d μ ​ ( s ) > 0 d_{\mu}(s)>0 (i.e., supp ⁡ ( d π , t ) ⊆ supp ⁡ ( d μ ) \mathrm{supp}(d_{\pi,t})\subseteq\mathrm{supp}(d_{\mu}) ). This condition ensures the occupancy ratio C ⁡ ( π ) C(\pi) is well-defined. Then the online success probability satisfies

[270] table: J ⁡ ( π ) ≥ 1 − H ⋅ C ⁡ ( π ) ⋅ ( 1 − M off ​ ( π ) − η ¯ π ) . J(\pi)\ \geq\ 1\;-\;H\cdot C(\pi)\cdot\Big(1-M_{\mathrm{off}}(\pi)-\bar{\eta}_{\pi}\Big). (13)

[271] p: In particular, if C ⁡ ( π ) C(\pi) is uniformly bounded over a policy class and η ¯ π \bar{\eta}_{\pi} is small or stable across policies , then M off ​ ( π ) M_{\mathrm{off}}(\pi) becomes predictive of J ⁡ ( π ) J(\pi) through the affine lower bound.

[272] h6: Proof E.2 .

[273] p: Let E t E_{t} denote the event that the action at step t t is invalid:

[274] table: E t ≜ { a t ∉ 𝒜 ∗ ( s t ) } . E_{t}\;\triangleq\;\{a_{t}\notin\mathcal{A}^{*}(s_{t})\}.

[275] p: By Assumption 5.1 , failure implies that at least one invalid step occurs, i.e.,

[276] table: { failure } ⊆ ⋃ t = 1 H E t . \{\text{failure}\}\subseteq\bigcup_{t=1}^{H}E_{t}.

[277] p: Therefore,

[278] table: 1 − J ⁡ ( π ) = ℙ ⁡ ( failure ) ≤ ℙ ⁡ ( ⋃ t = 1 H E t ) ≤ ∑ t = 1 H ℙ ⁡ ( E t ) , 1-J(\pi)=\mathbb{P}(\text{failure})\leq\mathbb{P}\!\left(\bigcup_{t=1}^{H}E_{t}\right)\leq\sum_{t=1}^{H}\mathbb{P}(E_{t}),

[279] p: where the last inequality is the union bound.

[280] p: Fix any t ∈ [ H ] t\in[H] . Conditioning on s t s_{t} gives

[281] table: ℙ ⁡ ( E t ) = 𝔼 s ∼ d π , t ​ [ ℙ ⁡ ( a t ∉ 𝒜 ∗ ​ ( s ) ∣ s t = s ) ] = 𝔼 s ∼ d π , t ​ [ 1 − π ⁡ ( 𝒜 ∗ ​ ( s ) ∣ s ) ] . \mathbb{P}(E_{t})=\mathbb{E}_{s\sim d_{\pi,t}}\Big[\mathbb{P}(a_{t}\notin\mathcal{A}^{*}(s)\mid s_{t}=s)\Big]=\mathbb{E}_{s\sim d_{\pi,t}}\Big[1-\pi(\mathcal{A}^{*}(s)\mid s)\Big].

[282] p: Define the nonnegative function f ⁡ ( s ) ≜ 1 − π ⁡ ( 𝒜 ∗ ​ ( s ) ∣ s ) ≥ 0 f(s)\triangleq 1-\pi(\mathcal{A}^{*}(s)\mid s)\geq 0 . By the definition of C ⁡ ( π ) C(\pi) and the support condition d π , t ≪ d μ d_{\pi,t}\ll d_{\mu} ,

[283] table: 𝔼 s ∼ d π , t ​ [ f ⁡ ( s ) ] = 𝔼 s ∼ d μ ​ [ d π , t ​ ( s ) d μ ​ ( s ) ​ f ​ ( s ) ] ≤ C ⁡ ( π ) ⋅ 𝔼 s ∼ d μ ​ [ f ⁡ ( s ) ] . \mathbb{E}_{s\sim d_{\pi,t}}[f(s)]=\mathbb{E}_{s\sim d_{\mu}}\!\left[\frac{d_{\pi,t}(s)}{d_{\mu}(s)}\,f(s)\right]\leq C(\pi)\cdot\mathbb{E}_{s\sim d_{\mu}}[f(s)].

[284] p: Next, since the offline dataset verifies only the demonstrated action a ~ ​ ( s ) ∈ 𝒜 ∗ ​ ( s ) \tilde{a}(s)\in\mathcal{A}^{*}(s) , we can decompose the true step-wise validity probability as

[285] table: π ⁡ ( 𝒜 ∗ ​ ( s ) ∣ s ) = π ⁡ ( a ~ ​ ( s ) ∣ s ) + π ⁡ ( 𝒜 ∗ ​ ( s ) ∖ { a ~ ​ ( s ) } ∣ s ) = π ⁡ ( a ~ ​ ( s ) ∣ s ) + η π ​ ( s ) . \pi(\mathcal{A}^{*}(s)\mid s)=\pi(\tilde{a}(s)\mid s)\;+\;\pi\!\left(\mathcal{A}^{*}(s)\setminus\{\tilde{a}(s)\}\mid s\right)=\pi(\tilde{a}(s)\mid s)\;+\;\eta_{\pi}(s).

[286] p: Taking expectation over s ∼ d μ s\sim d_{\mu} yields

[287] table: 𝔼 s ∼ d μ ​ [ π ⁡ ( 𝒜 ∗ ​ ( s ) ∣ s ) ] = M off ​ ( π ) + η ¯ π , \mathbb{E}_{s\sim d_{\mu}}\big[\pi(\mathcal{A}^{*}(s)\mid s)\big]=M_{\mathrm{off}}(\pi)\;+\;\bar{\eta}_{\pi},

[288] p: and hence

[289] table: 𝔼 s ∼ d μ ​ [ f ⁡ ( s ) ] = 1 − 𝔼 s ∼ d μ ​ [ π ⁡ ( 𝒜 ∗ ​ ( s ) ∣ s ) ] = 1 − M off ​ ( π ) − η ¯ π . \mathbb{E}_{s\sim d_{\mu}}[f(s)]=1-\mathbb{E}_{s\sim d_{\mu}}\big[\pi(\mathcal{A}^{*}(s)\mid s)\big]=1-M_{\mathrm{off}}(\pi)-\bar{\eta}_{\pi}.

[290] p: Combining the above bounds, for each t t we have

[291] table: ℙ ⁡ ( E t ) ≤ C ⁡ ( π ) ⋅ ( 1 − M off ​ ( π ) − η ¯ π ) . \mathbb{P}(E_{t})\leq C(\pi)\cdot\big(1-M_{\mathrm{off}}(\pi)-\bar{\eta}_{\pi}\big).

[292] p: Summing over t = 1 , … , H t=1,\dots,H and using 1 − J ⁡ ( π ) ≤ ∑ t = 1 H ℙ ⁡ ( E t ) 1-J(\pi)\leq\sum_{t=1}^{H}\mathbb{P}(E_{t}) gives

[293] table: 1 − J ⁡ ( π ) ≤ H ⋅ C ⁡ ( π ) ⋅ ( 1 − M off ​ ( π ) − η ¯ π ) , 1-J(\pi)\leq H\cdot C(\pi)\cdot\big(1-M_{\mathrm{off}}(\pi)-\bar{\eta}_{\pi}\big),

[294] p: which is equivalent to Eq 13 . This concludes the proof.

[295] h5: Discussion.

[296] p: Theorem (Theorem ) clarifies why an offline one-step matching score can be an unreliable proxy for the online success probability J ⁡ ( π ) J(\pi) in multi-step GUI navigation under partial verifiability. Offline evaluation is computed on a fixed dataset distribution d μ d_{\mu} and credits only the single demonstrated action a ~ ​ ( s ) \tilde{a}(s) . In contrast, online success depends on the policy-induced state distributions { d π , t } t = 1 H \{d_{\pi,t}\}_{t=1}^{H} and on choosing any valid action in 𝒜 ∗ ​ ( s ) \mathcal{A}^{*}(s) over a long horizon. The theorem makes this mismatch explicit through two quantities: the occupancy mismatch C ⁡ ( π ) C(\pi) and the unobserved off-demo validity mass η ¯ π \bar{\eta}_{\pi} . As a result, offline-to-online predictability can break down in several ways.

[297] p: (i) Distribution shift and error accumulation (large C ⁡ ( π ) C(\pi) ). Even if π \pi matches the demonstrator well on states drawn from d μ d_{\mu} , small errors can compound over time and shift the online trajectory distribution away from the offline support. When C ⁡ ( π ) C(\pi) is large, M off ​ ( π ) M_{\mathrm{off}}(\pi) provides limited information about the states that dominate online performance. In this regime, M off ​ ( π ) M_{\mathrm{off}}(\pi) may improve while J ⁡ ( π ) J(\pi) stagnates (or decreases) because failures are driven by states that are rarely or never seen in the offline data.

[298] p: (ii) Non-identifiability under partial verifiability (unstable η ¯ π \bar{\eta}_{\pi} ). Offline matching measures only π ​ ( a ~ ​ ( s ) ∣ s ) \pi(\tilde{a}(s)\mid s) , whereas the true one-step validity is

[299] table: π ⁡ ( 𝒜 ∗ ​ ( s ) ∣ s ) = π ⁡ ( a ~ ​ ( s ) ∣ s ) + η π ​ ( s ) , η π ​ ( s ) = π ⁡ ( 𝒜 ∗ ​ ( s ) ∖ { a ~ ​ ( s ) } ∣ s ) . \pi(\mathcal{A}^{*}(s)\mid s)=\pi(\tilde{a}(s)\mid s)+\eta_{\pi}(s),\qquad\eta_{\pi}(s)=\pi\!\left(\mathcal{A}^{*}(s)\setminus\{\tilde{a}(s)\}\mid s\right).

[300] p: Therefore, M off ​ ( π ) M_{\mathrm{off}}(\pi) does not determine true step validity unless the off-demo validity mass η π ​ ( s ) \eta_{\pi}(s) is negligible or approximately invariant across the policies being compared. Importantly, a larger η ¯ π \bar{\eta}_{\pi} does not imply better predictability: the issue is that η π \eta_{\pi} is unobserved under offline verification and can vary substantially across policies, so changes in M off ​ ( π ) M_{\mathrm{off}}(\pi) may reflect reallocation of probability mass rather than genuine improvements in correctness.

[301] h6: Example E.3 .

[302] p: Larger η π \eta_{\pi} does not mean better predictabilitypolicy_comparison Consider a single decision state s s (so C ⁡ ( π ) = 1 C(\pi)=1 ) with three actions: a demonstrated valid action a ⋆ = a ~ ​ ( s ) a^{\star}=\tilde{a}(s) , an alternative valid action a ′ a^{\prime} , and an invalid action a bad a_{\mathrm{bad}} . Thus 𝒜 ∗ ​ ( s ) = { a ⋆ , a ′ } \mathcal{A}^{*}(s)=\{a^{\star},a^{\prime}\} and choosing any action outside 𝒜 ∗ ​ ( s ) \mathcal{A}^{*}(s) causes failure. Offline matching credits only a ⋆ a^{\star} , so

[303] table: M off ​ ( π ) = π ⁡ ( a ⋆ ∣ s ) , η π ​ ( s ) = π ⁡ ( a ′ ∣ s ) , J ⁡ ( π ) = π ⁡ ( a ⋆ ∣ s ) + π ⁡ ( a ′ ∣ s ) = 1 − π ⁡ ( a bad ∣ s ) . M_{\mathrm{off}}(\pi)=\pi(a^{\star}\mid s),\qquad\eta_{\pi}(s)=\pi(a^{\prime}\mid s),\qquad J(\pi)=\pi(a^{\star}\mid s)+\pi(a^{\prime}\mid s)=1-\pi(a_{\mathrm{bad}}\mid s).

[304] p: Compare two policies:

[305] table: π 1 ( a ⋆ ∣ s ) = 0.2 , π 1 ( a ′ ∣ s ) = 0.7 , π 1 ( a bad ∣ s ) = 0.1 ⇒ M off ( π 1 ) = 0.2 , η π 1 ( s ) = 0.7 , J ( π 1 ) = 0.9 , \pi_{1}(a^{\star}\mid s)=0.2,\ \pi_{1}(a^{\prime}\mid s)=0.7,\ \pi_{1}(a_{\mathrm{bad}}\mid s)=0.1\quad\Rightarrow\quad M_{\mathrm{off}}(\pi_{1})=0.2,\ \eta_{\pi_{1}}(s)=0.7,\ J(\pi_{1})=0.9,

[306] table: π 2 ( a ⋆ ∣ s ) = 0.4 , π 2 ( a ′ ∣ s ) = 0.1 , π 2 ( a bad ∣ s ) = 0.5 ⇒ M off ( π 2 ) = 0.4 , η π 2 ( s ) = 0.1 , J ( π 2 ) = 0.5 . \pi_{2}(a^{\star}\mid s)=0.4,\ \pi_{2}(a^{\prime}\mid s)=0.1,\ \pi_{2}(a_{\mathrm{bad}}\mid s)=0.5\quad\Rightarrow\quad M_{\mathrm{off}}(\pi_{2})=0.4,\ \eta_{\pi_{2}}(s)=0.1,\ J(\pi_{2})=0.5.

[307] p: Here the offline score increases ( 0.2 → 0.4 0.2\to 0.4 ), while the off-demo validity mass changes dramatically ( 0.7 → 0.1 0.7\to 0.1 ) and the true success probability drops sharply ( 0.9 → 0.5 0.9\to 0.5 ). This happens because M off M_{\mathrm{off}} only tracks probability on the single demonstrated action a ⋆ a^{\star} ; it cannot distinguish whether probability mass is reallocated from other valid alternatives a ′ a^{\prime} (uncredited) to invalid actions a bad a_{\mathrm{bad}} .

[308] p: (iii) Offline overfitting can reduce online robustness. Example also illustrates another failure mode: maximizing an offline demo-matching score can encourage demo-specific behavior. Because M off ​ ( π ) M_{\mathrm{off}}(\pi) rewards only matching the single demonstrated action a ~ ​ ( s ) \tilde{a}(s) , a policy may increase M off ​ ( π ) M_{\mathrm{off}}(\pi) by concentrating probability mass on a ~ ​ ( s ) \tilde{a}(s) while reducing exploration of other valid alternatives. This overfitting reduces behavioral diversity and weakens recovery strategies that are essential for interactive agents. In long-horizon GUI navigation, the impact is amplified by error accumulation. A small early mistake can move the agent to states that are poorly covered by the offline data, where the policy has not learned robust correction behaviors. This increases state-distribution shift (larger C ⁡ ( π ) C(\pi) ) and can lower the overall success probability J ⁡ ( π ) J(\pi) . Consequently, it is possible for M off ​ ( π ) M_{\mathrm{off}}(\pi) to improve while J ⁡ ( π ) J(\pi) decreases.

[309] p: Taken together, these failure modes explain why offline one-step matching can be poorly predictive of online success in multi-step GUI navigation: offline evaluation measures demo-matching under d μ d_{\mu} , whereas online success depends on long-horizon validity under { d π , t } \{d_{\pi,t}\} and is confounded by unobserved (and potentially unstable) off-demo validity mass.

[310] h4: E.0.2 KL regularization improves predictability

[311] p: Many RLVR pipelines drop the KL regularization term for efficiency ( Yu et al., 2025 ; Liu et al., 2025d ; Zhou et al., 2025b ; Yang et al., 2025b ) . In our setting, however, KL regularization is important because step-wise offline matching is only partially verifiable: matches to the demonstrated action provide reliable positive signal, while non-matches are ambiguous. Below we connect KL regularization (to a reference policy) to the two quantities that govern offline-to-online predictability: the occupancy mismatch C ⁡ ( π ) C(\pi) and the off-demo validity mass η ¯ π \bar{\eta}_{\pi} .

[312] h6: Lemma E.4 .

[313] p: KL regularization controls distribution shiftkl_occupancy Let π ref \pi_{\mathrm{ref}} be a reference policy and assume a per-state KL constraint

[314] table: KL ( π ( ⋅ ∣ s ) ∥ π ref ( ⋅ ∣ s ) ) ≤ ε , ∀ s ∈ 𝒮 . \mathrm{KL}\!\left(\pi(\cdot\mid s)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq\varepsilon,\qquad\forall s\in\mathcal{S}.

[315] p: Then Pinsker’s inequality implies

[316] table: TV ( π ( ⋅ ∣ s ) , π ref ( ⋅ ∣ s ) ) ≤ ε / 2 , ∀ s ∈ 𝒮 . \mathrm{TV}\!\left(\pi(\cdot\mid s),\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq\sqrt{\varepsilon/2},\qquad\forall s\in\mathcal{S}.

[317] p: Consequently, the induced state visitation distributions satisfy

[318] table: ‖ d π , t − d π ref , t ‖ 1 ≤ t ​ 2 ​ ε , ∀ t ∈ [ H ] . \|d_{\pi,t}-d_{\pi_{\mathrm{ref}},t}\|_{1}\leq t\sqrt{2\varepsilon},\qquad\forall t\in[H].

[319] p: Moreover, if d μ ​ ( s ) ≥ ρ > 0 d_{\mu}(s)\geq\rho>0 whenever d μ ​ ( s ) > 0 d_{\mu}(s)>0 and d π ref , t ≪ d μ d_{\pi_{\mathrm{ref}},t}\ll d_{\mu} , then

[320] table: sup s : d μ ​ ( s ) > 0 d π , t ​ ( s ) d μ ​ ( s ) ≤ sup s : d μ ​ ( s ) > 0 d π ref , t ​ ( s ) d μ ​ ( s ) + ‖ d π , t − d π ref , t ‖ 1 ρ ≤ C ( π ref ) + t ​ 2 ​ ε ρ . \sup_{s:\,d_{\mu}(s)>0}\frac{d_{\pi,t}(s)}{d_{\mu}(s)}\leq\sup_{s:\,d_{\mu}(s)>0}\frac{d_{\pi_{\mathrm{ref}},t}(s)}{d_{\mu}(s)}+\frac{\|d_{\pi,t}-d_{\pi_{\mathrm{ref}},t}\|_{1}}{\rho}\leq C(\pi_{\mathrm{ref}})+\frac{t\sqrt{2\varepsilon}}{\rho}.

[321] p: In particular, KL regularization bounds how much the occupancy mismatch C ⁡ ( π ) C(\pi) can grow relative to π ref \pi_{\mathrm{ref}} .

[322] h6: Proof E.5 .

[323] p: Step 1: From KL to per-state TV. By Pinsker’s inequality, for every s s ,

[324] table: TV ( π ( ⋅ ∣ s ) , π ref ( ⋅ ∣ s ) ) ≤ 1 2 KL ( π ( ⋅ ∣ s ) ∥ π ref ( ⋅ ∣ s ) ) ≤ ε / 2 . \mathrm{TV}\!\left(\pi(\cdot\mid s),\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq\sqrt{\tfrac{1}{2}\,\mathrm{KL}\!\left(\pi(\cdot\mid s)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid s)\right)}\leq\sqrt{\varepsilon/2}.

[325] p: Equivalently, for every measurable set A ⊆ 𝒜 A\subseteq\mathcal{A} ,

[326] table: | π ( A ∣ s ) − π ref ( A ∣ s ) | ≤ TV ( π ( ⋅ ∣ s ) , π ref ( ⋅ ∣ s ) ) ≤ ε / 2 . \big|\pi(A\mid s)-\pi_{\mathrm{ref}}(A\mid s)\big|\leq\mathrm{TV}\!\left(\pi(\cdot\mid s),\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq\sqrt{\varepsilon/2}. (14)

[327] p: Step 2: One-step propagation bound. Let P π P_{\pi} denote the (time-homogeneous) state-transition operator induced by π \pi :

[328] table: ( P π ​ ν ) ​ ( s ′ ) ≜ ∑ s ∈ 𝒮 ν ⁡ ( s ) ​ ∑ a ∈ 𝒜 π ⁡ ( a ∣ s ) ​ P ​ ( s ′ ∣ s , a ) , (P_{\pi}\nu)(s^{\prime})\triangleq\sum_{s\in\mathcal{S}}\nu(s)\sum_{a\in\mathcal{A}}\pi(a\mid s)\,P(s^{\prime}\mid s,a),

[329] p: and similarly define P π ref P_{\pi_{\mathrm{ref}}} . For any distribution ν \nu over states, consider ‖ ν ​ P π − ν ​ P π ref ‖ 1 \|\nu P_{\pi}-\nu P_{\pi_{\mathrm{ref}}}\|_{1} . For each s ′ s^{\prime} , define

[330] table: P π ​ ( s ′ ∣ s ) ≜ ∑ a π ⁡ ( a ∣ s ) ​ P ​ ( s ′ ∣ s , a ) , P π ref ​ ( s ′ ∣ s ) ≜ ∑ a π ref ​ ( a ∣ s ) ​ P ​ ( s ′ ∣ s , a ) . P_{\pi}(s^{\prime}\mid s)\triangleq\sum_{a}\pi(a\mid s)P(s^{\prime}\mid s,a),\qquad P_{\pi_{\mathrm{ref}}}(s^{\prime}\mid s)\triangleq\sum_{a}\pi_{\mathrm{ref}}(a\mid s)P(s^{\prime}\mid s,a).

[331] p: Then

[332] table: ∥ ν P π − ν P π ref ∥ 1 = ‖ ∑ s ν ( s ) ( P π ( ⋅ ∣ s ) − P π ref ( ⋅ ∣ s ) ) ‖ 1 ≤ ∑ s ν ( s ) ∥ P π ( ⋅ ∣ s ) − P π ref ( ⋅ ∣ s ) ∥ 1 . \|\nu P_{\pi}-\nu P_{\pi_{\mathrm{ref}}}\|_{1}=\left\|\sum_{s}\nu(s)\big(P_{\pi}(\cdot\mid s)-P_{\pi_{\mathrm{ref}}}(\cdot\mid s)\big)\right\|_{1}\leq\sum_{s}\nu(s)\,\big\|P_{\pi}(\cdot\mid s)-P_{\pi_{\mathrm{ref}}}(\cdot\mid s)\big\|_{1}.

[333] p: Moreover, for each fixed s s ,

[334] table: ∥ P π ( ⋅ ∣ s ) − P π ref ( ⋅ ∣ s ) ∥ 1 = ‖ ∑ a ( π ( a ∣ s ) − π ref ( a ∣ s ) ) P ( ⋅ ∣ s , a ) ‖ 1 ≤ ∑ a | π ( a ∣ s ) − π ref ( a ∣ s ) | = ∥ π ( ⋅ ∣ s ) − π ref ( ⋅ ∣ s ) ∥ 1 . \big\|P_{\pi}(\cdot\mid s)-P_{\pi_{\mathrm{ref}}}(\cdot\mid s)\big\|_{1}=\left\|\sum_{a}\big(\pi(a\mid s)-\pi_{\mathrm{ref}}(a\mid s)\big)P(\cdot\mid s,a)\right\|_{1}\leq\sum_{a}\big|\pi(a\mid s)-\pi_{\mathrm{ref}}(a\mid s)\big|=\|\pi(\cdot\mid s)-\pi_{\mathrm{ref}}(\cdot\mid s)\|_{1}.

[335] p: Using ∥ ⋅ ∥ 1 = 2 TV ( ⋅ , ⋅ ) \|\cdot\|_{1}=2\,\mathrm{TV}(\cdot,\cdot) for distributions,

[336] table: ∥ P π ( ⋅ ∣ s ) − P π ref ( ⋅ ∣ s ) ∥ 1 ≤ 2 TV ( π ( ⋅ ∣ s ) , π ref ( ⋅ ∣ s ) ) ≤ 2 ε / 2 = 2 ​ ε . \big\|P_{\pi}(\cdot\mid s)-P_{\pi_{\mathrm{ref}}}(\cdot\mid s)\big\|_{1}\leq 2\,\mathrm{TV}\!\left(\pi(\cdot\mid s),\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq 2\sqrt{\varepsilon/2}=\sqrt{2\varepsilon}.

[337] p: Therefore, for any ν \nu ,

[338] table: ‖ ν ​ P π − ν ​ P π ref ‖ 1 ≤ 2 ​ ε . \|\nu P_{\pi}-\nu P_{\pi_{\mathrm{ref}}}\|_{1}\leq\sqrt{2\varepsilon}. (15)

[339] p: Step 3: Telescoping over t t steps. Let d π , t d_{\pi,t} and d π ref , t d_{\pi_{\mathrm{ref}},t} denote the state distributions at step t t under π \pi and π ref \pi_{\mathrm{ref}} , respectively. Using the recursion d π , t + 1 = d π , t ​ P π d_{\pi,t+1}=d_{\pi,t}P_{\pi} and d π ref , t + 1 = d π ref , t ​ P π ref d_{\pi_{\mathrm{ref}},t+1}=d_{\pi_{\mathrm{ref}},t}P_{\pi_{\mathrm{ref}}} , we have

[340] table: ‖ d π , t + 1 − d π ref , t + 1 ‖ 1 = ‖ d π , t ​ P π − d π ref , t ​ P π ref ‖ 1 ≤ ‖ d π , t ​ P π − d π , t ​ P π ref ‖ 1 ⏟ ≤ 2 ​ ε ​ by equation 15 + ‖ d π , t ​ P π ref − d π ref , t ​ P π ref ‖ 1 ⏟ ≤ ‖ d π , t − d π ref , t ‖ 1 . \|d_{\pi,t+1}-d_{\pi_{\mathrm{ref}},t+1}\|_{1}=\|d_{\pi,t}P_{\pi}-d_{\pi_{\mathrm{ref}},t}P_{\pi_{\mathrm{ref}}}\|_{1}\leq\underbrace{\|d_{\pi,t}P_{\pi}-d_{\pi,t}P_{\pi_{\mathrm{ref}}}\|_{1}}_{\leq\sqrt{2\varepsilon}\ \text{by equation\penalty\ \ref{eq:one_step_shift_app}}}+\underbrace{\|d_{\pi,t}P_{\pi_{\mathrm{ref}}}-d_{\pi_{\mathrm{ref}},t}P_{\pi_{\mathrm{ref}}}\|_{1}}_{\leq\|d_{\pi,t}-d_{\pi_{\mathrm{ref}},t}\|_{1}}.

[341] p: Thus,

[342] table: ‖ d π , t + 1 − d π ref , t + 1 ‖ 1 ≤ ‖ d π , t − d π ref , t ‖ 1 + 2 ​ ε . \|d_{\pi,t+1}-d_{\pi_{\mathrm{ref}},t+1}\|_{1}\leq\|d_{\pi,t}-d_{\pi_{\mathrm{ref}},t}\|_{1}+\sqrt{2\varepsilon}.

[343] p: Iterating this inequality and using ‖ d π , 0 − d π ref , 0 ‖ 1 = 0 \|d_{\pi,0}-d_{\pi_{\mathrm{ref}},0}\|_{1}=0 (same initial distribution) yields

[344] table: ‖ d π , t − d π ref , t ‖ 1 ≤ t ​ 2 ​ ε . \|d_{\pi,t}-d_{\pi_{\mathrm{ref}},t}\|_{1}\leq t\sqrt{2\varepsilon}.

[345] p: Step 4: Bounding occupancy mismatch relative to d μ d_{\mu} . Assume d π ref , t ≪ d μ d_{\pi_{\mathrm{ref}},t}\ll d_{\mu} and d μ ​ ( s ) ≥ ρ > 0 d_{\mu}(s)\geq\rho>0 whenever d μ ​ ( s ) > 0 d_{\mu}(s)>0 . For any s s with d μ ​ ( s ) > 0 d_{\mu}(s)>0 ,

[346] table: d π , t ​ ( s ) d μ ​ ( s ) = d π ref , t ​ ( s ) d μ ​ ( s ) + d π , t ​ ( s ) − d π ref , t ​ ( s ) d μ ​ ( s ) ≤ d π ref , t ​ ( s ) d μ ​ ( s ) + | d π , t ​ ( s ) − d π ref , t ​ ( s ) | ρ . \frac{d_{\pi,t}(s)}{d_{\mu}(s)}=\frac{d_{\pi_{\mathrm{ref}},t}(s)}{d_{\mu}(s)}+\frac{d_{\pi,t}(s)-d_{\pi_{\mathrm{ref}},t}(s)}{d_{\mu}(s)}\leq\frac{d_{\pi_{\mathrm{ref}},t}(s)}{d_{\mu}(s)}+\frac{|d_{\pi,t}(s)-d_{\pi_{\mathrm{ref}},t}(s)|}{\rho}.

[347] p: Taking supremum over s s with d μ ​ ( s ) > 0 d_{\mu}(s)>0 and using sup s | x s | ≤ ∑ s | x s | = ‖ x ‖ 1 \sup_{s}|x_{s}|\leq\sum_{s}|x_{s}|=\|x\|_{1} gives

[348] table: sup s : d μ ​ ( s ) > 0 d π , t ​ ( s ) d μ ​ ( s ) ≤ sup s : d μ ​ ( s ) > 0 d π ref , t ​ ( s ) d μ ​ ( s ) + ‖ d π , t − d π ref , t ‖ 1 ρ ≤ C ( π ref ) + t ​ 2 ​ ε ρ , \sup_{s:\,d_{\mu}(s)>0}\frac{d_{\pi,t}(s)}{d_{\mu}(s)}\leq\sup_{s:\,d_{\mu}(s)>0}\frac{d_{\pi_{\mathrm{ref}},t}(s)}{d_{\mu}(s)}+\frac{\|d_{\pi,t}-d_{\pi_{\mathrm{ref}},t}\|_{1}}{\rho}\leq C(\pi_{\mathrm{ref}})+\frac{t\sqrt{2\varepsilon}}{\rho},

[349] p: which completes the proof.

[350] h6: Lemma E.6 .

[351] p: KL limits off-demo validity mass under single-demo supervisionkl_shrinks_ambiguity Fix a state s s and let a ~ = a ~ ​ ( s ) \tilde{a}=\tilde{a}(s) be the demonstrated action. Assume KL ( π ( ⋅ ∣ s ) ∥ π ref ( ⋅ ∣ s ) ) ≤ ε \mathrm{KL}(\pi(\cdot\mid s)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid s))\leq\varepsilon and that the reference policy is demo-concentrated: π ref ​ ( a ~ ∣ s ) ≥ 1 − δ ⁡ ( s ) \pi_{\mathrm{ref}}(\tilde{a}\mid s)\geq 1-\delta(s) . Then

[352] table: 1 − π ⁡ ( a ~ ∣ s ) ≤ δ ⁡ ( s ) + ε / 2 , η π ​ ( s ) = π ⁡ ( 𝒜 ∗ ​ ( s ) ∖ { a ~ } ∣ s ) ≤ 1 − π ⁡ ( a ~ ∣ s ) , 1-\pi(\tilde{a}\mid s)\leq\delta(s)+\sqrt{\varepsilon/2},\qquad\eta_{\pi}(s)=\pi\!\left(\mathcal{A}^{*}(s)\setminus\{\tilde{a}\}\mid s\right)\leq 1-\pi(\tilde{a}\mid s),

[353] p: and therefore

[354] table: η π ​ ( s ) ≤ δ ⁡ ( s ) + ε / 2 , η ¯ π ≤ δ ¯ + ε / 2 , δ ¯ ≜ 𝔼 s ∼ d μ ​ [ δ ⁡ ( s ) ] . \eta_{\pi}(s)\leq\delta(s)+\sqrt{\varepsilon/2},\qquad\bar{\eta}_{\pi}\leq\bar{\delta}+\sqrt{\varepsilon/2},\quad\bar{\delta}\triangleq\mathbb{E}_{s\sim d_{\mu}}[\delta(s)].

[355] h6: Proof E.7 .

[356] p: By Pinsker’s inequality,

[357] table: TV ( π ( ⋅ ∣ s ) , π ref ( ⋅ ∣ s ) ) ≤ ε / 2 . \mathrm{TV}\!\left(\pi(\cdot\mid s),\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq\sqrt{\varepsilon/2}.

[358] p: Let E ≜ { a ≠ a ~ } E\triangleq\{a\neq\tilde{a}\} . Using the standard event bound for total variation distance,

[359] table: π ( E ∣ s ) ≤ π ref ( E ∣ s ) + TV ( π ( ⋅ ∣ s ) , π ref ( ⋅ ∣ s ) ) ≤ ( 1 − π ref ( a ~ ∣ s ) ) + ε / 2 ≤ δ ( s ) + ε / 2 . \pi(E\mid s)\leq\pi_{\mathrm{ref}}(E\mid s)+\mathrm{TV}\!\left(\pi(\cdot\mid s),\pi_{\mathrm{ref}}(\cdot\mid s)\right)\leq\big(1-\pi_{\mathrm{ref}}(\tilde{a}\mid s)\big)+\sqrt{\varepsilon/2}\leq\delta(s)+\sqrt{\varepsilon/2}.

[360] p: Since π ⁡ ( E ∣ s ) = 1 − π ⁡ ( a ~ ∣ s ) \pi(E\mid s)=1-\pi(\tilde{a}\mid s) , we obtain 1 − π ⁡ ( a ~ ∣ s ) ≤ δ ⁡ ( s ) + ε / 2 1-\pi(\tilde{a}\mid s)\leq\delta(s)+\sqrt{\varepsilon/2} .

[361] p: Next, because 𝒜 ∗ ​ ( s ) ∖ { a ~ } ⊆ E \mathcal{A}^{*}(s)\setminus\{\tilde{a}\}\subseteq E , we have

[362] table: η π ​ ( s ) = π ⁡ ( 𝒜 ∗ ​ ( s ) ∖ { a ~ } ∣ s ) ≤ π ⁡ ( E ∣ s ) ≤ δ ⁡ ( s ) + ε / 2 . \eta_{\pi}(s)=\pi\!\left(\mathcal{A}^{*}(s)\setminus\{\tilde{a}\}\mid s\right)\leq\pi(E\mid s)\leq\delta(s)+\sqrt{\varepsilon/2}.

[363] p: Taking expectation over s ∼ d μ s\sim d_{\mu} yields

[364] table: η ¯ π = 𝔼 s ∼ d μ ​ [ η π ​ ( s ) ] ≤ 𝔼 s ∼ d μ ​ [ δ ⁡ ( s ) ] + ε / 2 = δ ¯ + ε / 2 , \bar{\eta}_{\pi}=\mathbb{E}_{s\sim d_{\mu}}[\eta_{\pi}(s)]\leq\mathbb{E}_{s\sim d_{\mu}}[\delta(s)]+\sqrt{\varepsilon/2}=\bar{\delta}+\sqrt{\varepsilon/2},

[365] p: which completes the proof.

[366] h5: Takeaway.

[367] p: The offline-to-online bound shows that predictability depends on (i) distribution shift along the policy’s own trajectories (captured by C ⁡ ( π ) C(\pi) ) and (ii) the unobserved probability mass on valid-but-uncredited actions under single-demo verification (captured by η ¯ π \bar{\eta}_{\pi} ). Lemma and Lemma explain why KL regularization helps in this setting: a KL trust region simultaneously limits state-distribution drift (controlling C ⁡ ( π ) C(\pi) ) and prevents the policy from moving too much probability mass away from the demonstrated action (controlling η ¯ π \bar{\eta}_{\pi} ). As a result, conservative KL-regularized optimization keeps training in a regime where improvements in the offline matching score M off ​ ( π ) M_{\mathrm{off}}(\pi) are more likely to reflect genuine improvements in online success J ⁡ ( π ) J(\pi) .

[368] h2: Appendix F Prompt Templates

[369] h3: F.1 Prompt for Reasoning Augmentation

[370] p: We use the following prompts with GPT-4.1 to generate reasoning traces, which form our initial reasoning dataset. We draw inspiration from AGUVIS ( Xu et al., 2025c ) and further refine and adapt the prompt through iterative trial-and-error during our data generation process.

[371] h3: F.2 SFT Data Example

[372] h3: F.3 RL Data Example

[373] p: The answer and the additional information used for reward computation are shown below. The gt_point_2d coordinates are normalized to the range [ 0 , 1 ] [0,1] , while gt_bbox is further scaled by a factor of 1000 1000 .

[374] h2: Appendix G Long-Horizon Trajectory Case Studies

[375] p: Figures 14 and 15 compare GUI-Libra-7B with its base model, Qwen2.5-VL-7B-Instruct, on AndroidWorld Task 18 ( ExpenseDeleteMultiple ). The task requires deleting three specific expenses in Pro Expense: School Supplies , Religious , and Flight Tickets . As shown in Figure 14 , GUI-Libra successfully completes this long-horizon task by alternating between iterative reasoning and grounded actions. In contrast, the base model requires more steps to discover how to delete a single item and then fails to remove the second one, highlighting its difficulty in sustaining multi-step progress and demonstrating the advantage of GUI-Libra on long-horizon decision making.

[376] p: We also include a web navigation case study in Figure 17 , where GUI-Libra-4B successfully completes a long-horizon WebArena-Lite-v2 task, further illustrating strong generalization to multi-step web interactions.

[377] figure: Figure 14 : Trajectory Example of GUI-Libra-7B for Task 18 ExpenseDeleteMultiple: Delete the following expenses from pro expense: School Supplies, Religious, Flight Tickets.

[378] figure: Figure 15 : Trajectory Example of the base model Qwen2.5-VL-7B-Instruct for Task 18 ExpenseDeleteMultiple: Delete the following expenses from pro expense: School Supplies, Religious, Flight Tickets.

[379] figure: Figure 16 : Trajectory Example of GUI-Libra-4B for WebArena-Lite-v2 Task: Follow [’lahwaacz’, ’Koushik’, ’Vinta Chen’] on Gitlab.

[380] figure: Figure 17 : Trajectory Example of Qwen3-VL-4B-Instruct for WebArena-Lite-v2 Task: Follow [’lahwaacz’, ’Koushik’, ’Vinta Chen’] on Gitlab.

[381] h2: Instructions for reporting errors

[382] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[383] p: Tip: You can select the relevant text first, to include it in your report.

[384] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[385] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
