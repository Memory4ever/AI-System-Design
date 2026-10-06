[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Reinforcing Real-world Service Agents: Balancing Utility and Cost in Task-Oriented Dialogue

[3] h6: Abstract

[4] p: The rapid evolution of Large Language Models (LLMs) has accelerated the transition from conversational chatbots to general agents. However, effectively balancing empathetic communication with budget-aware decision-making remains an open challenge. Since existing methods fail to capture these complex strategic trade-offs, we propose InteractCS-RL, a framework that reframes task-oriented dialogue as a multi-granularity reinforcement learning process. Specifically, we first establish a User-centric Interaction Framework to provide a high-fidelity training gym, enabling agents to dynamically explore diverse strategies with persona-driven users. Then, we introduce Cost-aware Multi-turn Policy Optimization (CMPO) with a hybrid advantage estimation strategy. By integrating generative process credits and employing a PID-Lagrangian cost controller, CMPO effectively guides the policy to explore Pareto boundary between user reward and global cost constraints. Extensive experiments on customized real business scenarios demonstrate that InteractCS-RL significantly outperform other baselines across three evaluation dimensions. Further evaluation on tool-agent-user interaction benchmarks verify InteractCS-RL robustness across diverse domains.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: With the rapid advancement of Large Language Models (LLMs), customer service systems have shifted the paradigm from simple intent classification to end-to-end generative agents. Building on this foundation, Task-Oriented Dialogue (TOD) methods have evolved, primarily focusing on helping users complete specific tasks such as booking restaurants, or reserving flights ( Yao et al., 2024 ) . Despite these advances, current methods typically involve simple information queries and form-filling conversations ( Budzianowski et al., 2018 ) , where the system only needs to follow fixed procedures to collect information, query databases, and return results ( Bocklisch et al., 2024 ) . However, real-world customer service scenarios are far more complex, filled with unexpected situations and emotional user interactions ( Jun and Lee, 2025 ) . This requires the agent to possess not only domain expertise but also refined verbal strategies and emotional regulation capabilities to alleviate user frustration. Crucially, these goals must be achieved under strict operational constraints, such as budget limits and efficiency targets, forming a multi-dimensional trade-off that existing general-purpose chatbots often struggle to balance.

[8] p: Despite their conversational fluency, current TOD approaches often focus solely on problem resolution while neglecting cost optimization, leading to two critical limitations: (1) Suboptimality of static data : Existing methods rely on Supervised Fine-Tuning (SFT) over static dialogue corpora ( Zhu et al., 2025 ; Ou et al., 2024 ; Li et al., 2025 ) . This paradigm encourages models to imitate human behaviors, including cost-inefficient decisions such as premature concessions, without assessing their long-term optimality. As a result, these models are prone to error accumulation and struggle to generalize to dynamic environments that require strategic trade-offs. (2) Lack of cost modeling mechanisms : current frameworks predominantly utilize “success rate” as a monolithic metric. They fail to penalize “false successes”, namely resolutions achieved through excessive resource expenditure, such as unnecessary compensation or protracted dialogue, thereby overlooking the economic constraints of real-world deployment.

[9] p: To address these issues, we first reframe task-oriented dialogue as a multi-granularity reinforcement learning process . Instead of fixating on a single terminal objective, we argue that an ideal service agent should possess the intrinsic capacity to reconcile three simultaneous goals: maintaining service norms at every turn, resolving problems by session end, and controlling operational costs throughout.

[10] p: Building upon this insight, we propose InteractCS-RL, a multi-granularity reinforcement learning framework for dynamic TOD.

[11] p: Departing from traditional paradigms centered on static trajectory imitation, our framework establishes a closed-loop interactive evolution cycle, empowering the customer service agent to autonomously explore optimal strategies within a simulated business environment. Specifically, we first construct the User-centric Interaction Framework , which driven by realistic user profiles with intrinsic traits and extrinsic demands modeling to provide a high-fidelity interactively online training gym. At the algorithmic level, we propose Cost-aware Multi-turn Policy Optimization (CMPO), which leverages a hybrid advantage estimation strategy to provide multi-granular guidance: (1) Session-level Outcome Utility based on final task score, such as user satisfaction; (2) Process Credit Assignment using generative reward model to ensure each-turn conversational quality; (3) Cost-aware Lagrange Penalty , which transforms global constraints into dynamic cost signals. This design enables InteractCS-RL to reduce operational costs while maintaining high resolution rates, truly learning to solve problems in a “cost-conscious” manner.

[12] p: We conduct comprehensive training and evaluation of InteractCS-RL on the representative real-world business scenarios called FoodDeliveryService . Experimental results demonstrate that our method significantly outperforms SFT, RL baselines ( Shao et al., 2024 ; Xie et al., 2025 ) and SOTA closed-source models ( OpenAI, 2025 ) across three evaluation dimensions. Furthermore, we perform cross-domain evaluation on public tool-agent-user benchmarks ( Barres et al., 2025 ) . Results show that InteractCS-RL maintains strong generalizability when handling multi-turn tool usage tasks across different domains. Finally, detailed ablation studies indicate the indispensability of both the profile-driven dynamic interaction environment and the cost-sensitive reward mechanism for enhancing agent decision-making capabilities in complex scenarios.

[13] p: Our main contributions include:

[14] p: We reframe task-oriented dialogue as a multi-granularity reinforcement learning process, transitioning from traditional static trajectory imitation to a closed-loop interactive evolution cycle.

[15] p: We design the User-centric Interaction Framework driven with diverse persona profiles bank to provide real-world service scenarios.

[16] p: We propose Cost-aware Multi-turn Policy Optimization to ensure stable policy convergence and effectively internalize operational budgets into the agent decision-making process.

[17] p: Experiments show that InteractCS-RL significantly outperforms SOTA closed-source models and other baselines in both task resolution and cost-efficiency under the FDS scenario, and further demonstrate cross-domain generalizability on τ 2 \tau^{2} -bench.

[18] h2: 2 Related Works

[19] p: Task-oriented Dialogue (TOD) systems are foundational to applications such as e-commerce, customer service, and automated sales ( Deng et al., 2024 ; Deng et al., 2025 ) . These systems must navigate complex interactions, ranging from fulfilling specific user requests to managing non-cooperative negotiations. Early research in TOD primarily leveraged sequence-to-sequence modeling and neural architectures ( Vinyals and Le, 2015 ; Wen et al., 2015 ; Shang et al., 2015 ; Li et al., 2016a ) , often employing user simulators to augment training data ( Li et al., 2016b ; Lewis et al., 2017 ; Wei et al., 2018 ) . However, the efficacy of these methods was largely constrained by the representative power of the underlying models. The advent of pre-trained and instruction-aligned LLMs has marked a paradigm shift ( Naveed et al., 2023 ; Wang et al., 2024 ; Yao et al., 2023 ) , as their sophisticated reasoning and linguistic capabilities are intrinsically well-suited for TOD. Current mainstream approaches typically focus on the construction of static datasets for supervised fine-tuning to adapt LLMs to specific scenarios ( Li et al., 2025 ; Ou et al., 2024 ; Zhu et al., 2025 ; Bernard and Balog, 2023 ) . Recent extensions have further integrated external tools ( Peiyuan et al., 2024 ) , RAG ( Xu et al., 2024 ) , and multimodal inputs ( Wang et al., 2025 ; Gong et al., 2025 ) to broaden the boundaries of these agents. Differently, InteractCS-RL operates online within a dynamic environment.

[20] p: Rewards Utility in LLM Post-training. Post-training for LLMs has evolved from simple preference alignment to the optimization of long-horizon reasoning. Early efforts focused on SFT to establish foundational capabilities ( Radford et al., 2018 ; Mann et al., 2020 ) . To improve generalization, Reinforcement Learning from Human Feedback ( Christiano et al., 2017 ; Ouyang et al., 2022 ) and its offline variants ( Rafailov et al., 2023 ; Meng et al., 2024 ) established the standard for alignment. Recently, the Reinforcement Learning from Verifiable Rewards (RLVR) paradigm has gained prominence in objective domains like mathematics and coding. Concurrently, Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) and its derivatives ( Yu et al., 2025 ; Zheng et al., 2025 ) have enhanced training stability and memory efficiency by eliminating the need for a centralized value network. However, these methods face two key challenges in complex TOD scenarios. To distribute sparse rewards, credit assignment ( Sutton, 1984 ) is employed. Some approaches leverage step-level ( Kazemnejad et al., 2024 ; Feng et al., 2025 ) or semantic-level ( Guo et al., 2025 ) sampling reuse to improve advantage estimation, but they often fail to accurately assess response quality across multiple turns. To perform optimization under operational constraints, safe alignment ( Ji et al., 2025 ) methods adopt offline optimization ( Kim et al., 2025 ; Wachi et al., 2024 ) or Lagrange multiplier ( Dai et al., 2023 ) , they typically focus on the cost ( Si et al., 2025 ) of individual responses rather than enforcing global constraints. To address these challenges in complex TOD scenarios, we introduce Process Credit Assignment and Cost-aware Lagrange Penalty, enabling more effective constraint-aware optimization in multi-turn dialogues.

[21] h2: 3 Preliminaries

[22] p: We formalize the interaction of task-oriented multi-turn dialogue as a turn-level Markov Decision Process ℳ = { 𝒮 , 𝒜 , P , R , γ } \mathcal{M}=\{\mathcal{S},\mathcal{A},P,R,\gamma\} , where 𝒮 \mathcal{S} denotes the state space, 𝒜 \mathcal{A} denotes the action space, P P represents the transition dynamics, R R is the reward function and γ \gamma is the discount factor. Specifically, the LLM serves as the agent π θ \pi_{\theta} . The initial state s 0 s_{0} is composed of the system instruction prompt x 0 x_{0} and first response of user u 0 u_{0} , such that s 0 = [ x 0 , u 0 ] s_{0}=[x_{0},u_{0}] . As the interaction progresses, the state at time t t , denoted as s t s_{t} , represents the cumulative dialogue trajectory: s t = [ x 0 , u 0 , a 0 , … , u t − 1 , a t − 1 , u t ] s_{t}=[x_{0},u_{0},a_{0},\dots,u_{t-1},a_{t-1},u_{t}] .

[23] p: The action of agent at time t t is defined as a composite output a t = [ z t , y t , d t ] a_{t}=[z_{t},y_{t},d_{t}] , where z t z_{t} denotes reasoning process ( Wei et al., 2022 ) , y t y_{t} represents the explicit response to the user, and d t d_{t} signifies its underlying decision or discrete action. The state transition probability 𝒫 ⁡ ( s t + 1 | s t , a t ) \mathcal{P}(s_{t+1}|s_{t},a_{t}) is primarily governed by user behavior; upon the execution of a t a_{t} , the environment generates the subsequent user response u t + 1 u_{t+1} . This transition 𝒫 \mathcal{P} effectively captures the inherent stochasticity of real-world multi-turn dynamics. The reward function r t ​ ( s t , a t ) r_{t}(s_{t},a_{t}) reflects the utility gained during the interaction, and the objective of agent J R J_{R} is to maximize the expected cumulative reward:

[24] table: J R ​ ( π θ ) = 𝔼 τ ∼ π θ ​ [ ∑ t γ t ​ r t ​ ( s t , a t ) ] . J_{R}(\pi_{\theta})=\mathbb{E}_{\tau\sim\pi_{\theta}}\left[\sum_{t}\gamma^{t}r_{t}(s_{t},a_{t})\right]. (1)

[25] p: To simulate resource constraints or policy boundaries inherent in task-oriented scenarios, we further introduce a cost function c t ​ ( s t , a t ) c_{t}(s_{t},a_{t}) , which quantifies the penalty incurred by the specific decision d t ∼ π θ ​ ( a t | s t ) d_{t}\sim\pi_{\theta}(a_{t}|s_{t}) . Consequently, we model the TOD task as a Constrained Markov Decision Process (CMDP) ( Altman, 2021 ) . We emphasize the aggregate cost J C ​ ( π θ ) J_{C}(\pi_{\theta}) , where the optimization objective is to maximize task utility subject to the global cost threshold δ \delta :

[26] table: max π θ J R ​ ( π θ ) , s.t. J C ​ ( π θ ) ≤ δ , \max_{\pi_{\theta}}\quad J_{R}(\pi_{\theta}),\quad\text{s.t.}\quad J_{C}(\pi_{\theta})\leq\delta, (2)

[27] p: where J C ​ ( π θ ) = 𝔼 τ ∼ π θ ​ [ ∑ t γ t ​ c t ​ ( s t , a t ) ] J_{C}(\pi_{\theta})=\mathbb{E}_{\tau\sim\pi_{\theta}}\left[\sum_{t}\gamma^{t}c_{t}(s_{t},a_{t})\right] .This formulation compels the LLM agent to not only pursue task resolution but also to learn a fine-grained calibration of action costs within its policy distribution during interaction.

[28] h2: 4 Method

[29] figure: Figure 1 : Illustration of our InteractCS-RL. (a) User-Centric Interaction Framework: Integrates persona bank modeling with dynamic user role-play to generate diverse interactive trajectories.(b) Cost-aware Multi-turn Policy Optimization: Synthesizes session-level outcomes, turn-level generative process credits, and PID-regulated global cost constraints into a hybrid advantage for stable policy optimization.

[30] p: We propose InteractCS-RL to address two critical gaps in the Task-Oriented Dialogue domain: 1) the absence of dynamic interactive environments featuring non-cooperative users and decision-making costs, and 2) the lack of online optimization methods to balance and cost in complex multi-turn dialogues. As illustrated in Figure 1 , InteractCS-RL comprises two primary components: the User-Centric Interaction Framework and Cost-aware Multi-turn Policy Optimization . The former establishes a dynamic interaction environment by coupling intrinsic persona dimensions with extrinsic demands, while the latter employs a generative credit assignment mechanism and cost-aware lagrange penalty to enable the agent to balance service utility and operational costs. We detail these components and their implementation in the subsequent sections.

[31] h3: 4.1 User-Centric Interaction Framework

[32] p: To address the limitations of static datasets, we establish a dynamic, closed-loop interaction environment driven by realistic user personas and business scenario logic.

[33] h4: 4.1.1 Persona Profiles Bank

[34] p: To capture the psychological complexity of real-world users, we construct a standardized persona framework. We utilize LLMs to extract features from anonymized, high-quality business dialogue logs, distilling them into a bi-level profile:

[35] p: Intrinsic Traits ( 𝒫 i ​ n ​ t \mathcal{P}_{int} ): Leveraging behavioral research ( Cobb-Clark and Schurer, 2012 ; Thomas, 2008 ) , we model users across four stable dimensions:

[36] p: ⋄ \diamond Communication Style: Rhetorical features such as verbosity and interaction frequency.

[37] p: ⋄ \diamond Information Disclosure: The user’s initiative and completeness in providing privately key facts.

[38] p: ⋄ \diamond Problem-solving Style: Strategic preferences in conflict, ranging from active collaboration to extreme not.

[39] p: ⋄ \diamond Personal Affective Style: Psychological baseline and emotional stability of the specific user.

[40] p: Extrinsic Demands ( 𝒟 \mathcal{D} ): While intrinsic traits govern style, extrinsic demands capture the goal-oriented logic. We categorize user objectives into four distinct patterns: Rigid Pursuit , Preference-learning , Incentive-open , and Feedback-oriented .

[41] p: By deeply coupling intrinsic traits and extrinsic demands, InteractCS-RL can automatically construct massive and diverse user behavior models, providing a diverse environment for agent optimization. More details please refer to App. .

[42] h4: 4.1.2 User Simulation with Role-play

[43] p: We then employ LLMs π u ​ s ​ e ​ r \pi_{user} as the user simulator. To ensure high fidelity, the simulator is conditioned on the constructed intrinsic features 𝒫 i ​ n ​ t \mathcal{P}_{int} , extrinsic demands 𝒟 \mathcal{D} , and real-time business signals S s ​ y ​ s S_{sys} including business scenario messages. By integrating these profiles directly as a structured prompt, the model dynamically generates linguistic responses and simulates psychological state transitions based on the conversation history h t = [ u 0 , y 0 , … ​ u t − 1 , y t − 1 ] h_{t}=[u_{0},y_{0},...u_{t-1},y_{t-1}] . The generation process is formalized as:

[44] table: ( u t + 1 , m t + 1 ) = π u ​ s ​ e ​ r ( ⋅ ∣ h t , 𝒫 i ​ n ​ t , 𝒟 , S s ​ y ​ s ) , (u_{t+1},m_{t+1})=\pi_{user}(\cdot\mid h_{t},\mathcal{P}_{int},\mathcal{D},S_{sys}), (3)

[45] p: where u t u_{t} is the generated natural language response, and m t m_{t} is metadata containing a satisfaction rating 𝒮 \mathcal{S} and a dialogue termination signal e e as shown in the Fig. 1 .

[46] h4: 4.1.3 Multi-turn Dynamic Interaction

[47] p: The interactions in InteractCS-RL are modeled as a dynamic process of alternating agent decision-making and user feedback, designed to simulate the uncertainty present in real-world TOD scenarios. The agent receives the environmental state s t s_{t} and generates composite a t a_{t} . The environment then parses this output and triggers a simulator response. The input-output relationship is defined as follows:

[48] table: { User Output: ( u t , m t ) ∼ π u ​ s ​ e ​ r ( h t , 𝒫 i ​ n ​ t , 𝒟 , S s ​ y ​ s ) , Agent Output: a t = [ z t , y t , d t ] ∼ π θ ( s t ) . \begin{cases}\text{User Output: }(u_{t},m_{t})\sim\pi_{user}(h_{t},\mathcal{P}_{int},\mathcal{D},S_{sys}),\\ \text{Agent Output: }a_{t}=[z_{t},y_{t},d_{t}]\sim\pi_{\theta}(s_{t}).\ \end{cases} (4)

[49] p: When the termination signal e = 1 e=1 , the interaction terminates and the satisfaction score 𝒮 \mathcal{S} from π u ​ s ​ e ​ r \pi_{user} for task resolution is returned. This interaction framework not only provides the policy with the opportunity to explore the nondeterministic state space, but also supports the reinforcement learning process by collecting trajectory data with feedback.

[50] h3: 4.2 Cost-aware Multi-turn Policy Optimization

[51] p: Leveraging the interactive environment established in Sec. 4.1 , we formulate the task resolution process as a Constrained Markov Decision Process as illustrated in Sec. 3 . Our goal is to train a customer service agent that maximizes task utility while strictly adhering to operational cost boundaries. To optimize this objective efficiently, we first adopt Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) . Rather than relying on a learned value function, GRPO utilizes group-based rollouts to estimate the advantage. Departing from standard GRPO which relies solely on sparse outcome labels, our core contribution lies in the design of a Hybrid Advantage Estimation strategy . This mechanism unifies session-level outcomes, turn-level process guidance, and global cost constraints into a single learning signal. Formally, for the i i -th trajectory τ i \tau_{i} sampled in a group, the advantage A ^ i , t \hat{A}_{i,t} at turn t t is computed as:

[52] table: A ^ i , t = Norm ​ ( ℛ O , i ⏟ Outcome + ℛ P , i , t ⏟ Process − λ ⋅ 𝕀 ⁡ ( d i , t ) ⏟ Cost Penalty ) , \hat{A}_{i,t}=\text{Norm}\left(\underbrace{\mathcal{R}_{O,i}}_{\text{Outcome}}+\underbrace{\mathcal{R}_{P,i,t}}_{\text{Process}}-\underbrace{\lambda\cdot\mathbb{I}(d_{i,t})}_{\text{Cost Penalty}}\right), (5)

[53] p: where Norm denotes normalizing operation on R i , t R_{i,t} using the mean and standard deviation of all turn rewards, ℛ O , i \mathcal{R}_{O,i} represents the final user satisfaction, ℛ P , i , t \mathcal{R}_{P,i,t} denotes the turn-level process reward derived from principle adherence, and the cost term λ ⋅ 𝕀 ⁡ ( d i , t ) \lambda\cdot\mathbb{I}(d_{i,t}) applies dynamic penalties to high-cost actions (e.g, compensation). In the following sections, we detail the derivation and implementation of these three components.

[54] h4: 4.2.1 Session-level Outcome Utility

[55] p: The primary objective of a service agent is to resolve user issues effectively. We quantify this using the Outcome Reward ( ℛ O \mathcal{R}_{O} ), which serves as the anchor for policy optimization. At the conclusion of each dialogue trajectory τ i \tau_{i} , the user simulator π u ​ s ​ e ​ r \pi_{user} acts as an evaluator, assigning a normalized satisfaction score based on the resolution status and the user’s final emotional state. We directly utilize this score as the session-level reward: ℛ O , i = S i , f ​ i ​ n ​ a ​ l \mathcal{R}_{O,i}=S_{i,final} . This ensures that the agent’s optimization direction remains consistently aligned with the ultimate business goal.

[56] h4: 4.2.2 Process Credit Assignment

[57] p: Reliance on sparse terminal signals often obscures the contribution of intermediate reasoning steps ( Kazemnejad et al., 2024 ) , making it difficult for agents to learn precise behavioral norms. To bridge this gap, we introduce a turn-level Process Reward ( ℛ P \mathcal{R}_{P} ) mechanism inspired by Generative Reward Modeling (GenRM) ( Liu et al., 2025 ) .

[58] p: We first translate domain expertise—such as dialogue logic, empathy requirements, and business compliance—into a set of scalable evaluation principles P = { p 1 , p 2 , … , p M } P=\{p_{1},p_{2},\dots,p_{M}\} . We then employ an off-the-shelf LLM ( π GenPRM \pi_{\text{GenPRM}} ) as the auditor (detailed in Section ). For the t t -th turn in trajectory τ i \tau_{i} , the model evaluates the turn-level output a i , t ∼ π θ ​ ( s i , t ) a_{i,t}\sim\pi_{\theta}(s_{i,t}) against each principle p j p_{j} with inference reasoning. To ensure the reliability of given process rewards, the evaluation score S i , t , j S_{i,t,j} is constrained to a simple discrete set:

[59] table: S i , t , j = π GenPRM ​ ( a i , t ∣ s i , t , p j ) ∈ { 0 , 0.5 , 1 } , S_{i,t,j}=\pi_{\text{GenPRM}}(a_{i,t}\mid s_{i,t},p_{j})\in\{0,0.5,1\}, (6)

[60] p: where the discrete values correspond to violation, partial adherence, and full compliance. Finally, we aggregate these multi-dimensional assessments via a weighted summation to produce the turn-level process reward: ℛ P , i , t = ∑ j = 1 M w j ⋅ S i , t , j \mathcal{R}_{P,i,t}=\sum_{j=1}^{M}w_{j}\cdot S_{i,t,j} . This mechanism provides fine-grained guidance, encouraging the agent to adhere to service specifications at every step of the interaction, rather than solely optimizing for the final outcome.

[61] h4: 4.2.3 Global Cost Constraints

[62] p: Here, we address the challenge of operational costs, such as excessive compensation, which must be controlled within a predefined budget. We solve this Constrained MDP by reformulating it into an unconstrained dual problem using the Lagrange multiplier method ( Bertsekas, 2014 ; Achiam et al., 2017 ) , a technique for finding local maxima and minima of a function over a constrained set. This allows us to transform the constrained primal problem defined in Eq. 2 into its unconstrained Lagrangian dual form as follows:

[63] table: min λ ≥ 0 ⁡ max θ ⁡ ℒ ⁡ ( θ , λ ) = J R ​ ( π θ ) − λ ⁡ ( J C ​ ( π θ ) − δ ) , \min_{\lambda\geq 0}\max_{\theta}\mathcal{L}(\theta,\lambda)=J_{R}(\pi_{\theta})-\lambda(J_{C}(\pi_{\theta})-\delta), (7)

[64] p: where λ \lambda is the multiplier that dynamically penalize at the different training step.

[65] p: Standard error-based updates of λ \lambda often suffer from oscillation and overshooting. To ensure stable convergence between utility maximization and constraint satisfaction, we introduce a PID controller ( Stooke et al., 2020 ) . For the k k -th step, we first compute the error term e k = J C , k ​ ( π θ ) − δ e_{k}=J_{C,k}(\pi_{\theta})-\delta , where J C , k J_{C,k} equals to the current average cost at k k -th step, and then update the penalty coefficient λ \lambda as follows:

[66] table: λ k + 1 = clip ​ ( λ k + K P ​ e k + K I ​ ∑ e k + K D ​ Δ ​ e k , 0 , λ m ​ a ​ x ) . \lambda_{k+1}=\text{clip}\left(\lambda_{k}+K_{P}e_{k}+K_{I}\sum e_{k}+K_{D}\Delta e_{k},\ 0,\ \lambda_{max}\right). (8)

[67] p: By incorporating a proportional term to respond to instantaneous violations and an integral term to correct long-term bias, this mechanism effectively transforms global budget constraints into the stable penalty term used in Eq. 5 , compelling the model to learn cost-aware planning.

[68] p: Finally we derive the objective function below, combining with Eq. 5 and Eq. 8 to iteratively update the policy model:

[69] table: 𝒥 C ​ M ​ P ​ O ​ ( θ ) = 𝔼 ℐ ∼ Q , { τ i } i = 1 n ∼ π θ old [ 1 n ∑ i = 1 n 1 T i ∑ t = 1 T i min ( r i , t ( θ ) A ^ i , t , clip ( r i , t ( θ ) , 1 − ϵ , 1 + ϵ ) A ^ i , t ) − β 𝔻 K ​ L [ π θ ∥ π ref ] ] . \begin{aligned} \mathcal{J}_{CMPO}(\theta)=&\mathbb{E}_{\mathcal{I}\sim Q,\{\tau_{i}\}_{i=1}^{n}\sim\pi_{\theta_{\text{old}}}}\Bigg[\frac{1}{n}\sum_{i=1}^{n}\frac{1}{T_{i}}\sum_{t=1}^{T_{i}}\min\Big(r_{i,t}(\theta)\hat{A}_{i,t},\\ &\text{clip}(r_{i,t}(\theta),1-\epsilon,1+\epsilon)\hat{A}_{i,t}\Big)-\beta\mathbb{D}_{KL}[\pi_{\theta}\|\pi_{\text{ref}}]\Bigg].\end{aligned} (9)

[70] figure: Table 1 : Comparison of model performance across different scenes on FoodDeliverService . Sat.: User satisfaction (Score from 1 to 5); FR: Dialogue Finish Rate(%); Comm.: Communication Quality (Score from 0 to 28); Logic: Logic Quality (Score from 0 to 12); V-Rate(%): Voucher Rate (Constrained with < 30 % <30\% ). Standard deviations are shown as superscripts. Method Scene 1 (Hard) Scene 2 (Easy) Task Score Dialogue Metric Cost Task Score Dialogue Metric Cost Sat. ↑ \uparrow FR (%) ↑ \uparrow Comm. ↑ \uparrow Logic ↑ \uparrow V-Rate ↓ \downarrow Sat. ↑ \uparrow FR (%) ↑ \uparrow Comm. ↑ \uparrow Logic ↑ \uparrow V-Rate ↓ \downarrow Large Models GPT-4.1 1.91 ±0.19 83.8 ±5.7 25.29 ±0.48 10.59 ±0.04 70.0 ±3.3 2.12 ±0.08 83.8 ±4.5 25.67 ±0.41 10.57 ±0.04 70.4 ±3.8 DeepSeek-v3.2 1.96 ±0.07 89.6 ±1.9 26.67 ±0.19 10.68 ±0.12 76.7 ±4.0 2.21 ±0.20 87.9 ±1.9 26.57 ±0.46 10.65 ±0.14 81.7 ±1.4 Qwen3-235B 1.73 ±0.07 62.5 ±3.5 23.75 ±0.27 7.82 ±0.34 91.9 ±4.4 1.93 ±0.03 60.6 ±2.7 23.80 ±0.42 7.29 ±0.39 94.2 ±1.4 LongCat-Flash 2.18 ±0.15 91.7 ±3.1 25.12 ±0.47 10.00 ±0.09 93.3 ±0.7 2.32 ±0.14 90.4 ±1.4 25.45 ±0.26 9.84 ±0.27 93.3 ±0.7 Foundation Models Qwen-2.5-7B 2.13 ±0.15 53.3 ±5.1 22.50 ±0.49 6.87 ±0.15 77.5 ±3.8 2.27 ±0.16 55.5 ±5.0 23.20 ±0.66 6.63 ±0.19 75.4 ±4.4 Qwen-2.5-14B 1.88 ±0.00 76.2 ±4.8 22.89 ±0.68 8.92 ±0.05 37.9 ±4.7 2.09 ±0.12 80.0 ±3.3 23.62 ±0.16 8.90 ±0.13 29.6 ±1.9 Static Train Qwen-2.5-7B-SFT 2.00 ±0.10 94.2 ±3.1 24.15 ±0.29 9.64 ±0.02 41.7 ±0.7 2.16 ±0.22 94.2 ±1.4 24.09 ±0.51 9.42 ±0.06 42.9 ±4.4 Qwen-2.5-14B-SFT 2.15 ±0.09 99.6 ±0.7 24.63 ±0.50 10.11 ±0.24 45.0 ±4.5 2.13 ±0.06 98.8 ±2.2 24.36 ±0.55 9.95 ±0.17 44.6 ±2.9 InteractCS-RL (Ours) Qwen-2.5-7B-RL 2.74 ±0.10 100.0 ±0.0 26.12 ±0.25 10.07 ±0.25 30.8 ±1.4 2.82 ±0.02 100.0 ±0.0 26.10 ±0.18 10.27 ±0.25 34.6 ±1.9 Qwen-2.5-14B-RL 3.05 ±0.04 100.0 ±0.0 27.43 ±0.28 11.34 ±0.21 27.5 ±2.5 3.21 ±0.07 100.0 ±0.0 27.45 ±0.29 11.34 ±0.46 28.7 ±3.8

[71] h2: 5 Experimental Setup

[72] h3: 5.1 Evaluation Objectives

[73] p: To evaluate the proposed framework, we design our experiments to answer the following three questions:

[74] p: ℋ ​ 1 \mathcal{H}1 - Can our method achieve higher dialogue quality in real-world scenarios while maintaining acceptable cost levels?

[75] p: ℋ ​ 2 \mathcal{H}2 - Is the proposed CMPO in InteractCS-RL effective?

[76] p: ℋ ​ 3 \mathcal{H}3 - Can the model trained under the proposed setting generalize to other TOD dialogue scenarios?

[77] h3: 5.2 Benchmarks and Evaluation Metrics

[78] p: Food Delivery Service (FDS). We construct a high-fidelity food delivery after-sales dispute scenario as the primary evaluation benchmark. This scenario covers core dispute types, including delivery delays, damaged food, and missing or incorrect orders. The agent’s objective is to resolve user dissatisfaction through multi-round negotiation while adhering to business compliance constraints. The primary cost incurred by the agent arises from voucher compensation actions. For the FDS scenario, we build a user profile library from pre-collected real-world business data and use it to train the SFT baseline. In addition, user profiles are clustered into five levels based on their cooperation degree, and two difficulty settings are designed by adjusting the proportion of profiles at different levels to simulate more diverse user populations. More details please refer to Appendix .

[79] p: Evaluation Metrics. Agent performance is evaluated along three dimensions. Task score includes the average user satisfaction and the completion rate of formatted dialogues. Dialogue quality measures the logical consistency and appropriateness of the agent expressions. Voucher Rate serves as the constraint indicator, capturing the frequency of issuing coupons during dialogue trajectories. All evaluations are conducted with three random tests. Additional details are provided in the Appendix A.1 .

[80] p: Additionally, we employ τ 2 \tau^{2} -bench ( Barres et al., 2025 ) to evaluate the generalizability of our InteractCS-RL across diverse TOD domains, including Retail, Telecom, and Airline. We assess the agent’s performance using Pass@1, Communicate Rate (Comm. Rate), DB Rate, and Action Reward. The detailed experimental setup and metric definitions for this benchmark are provided in Appendix A.2 .

[81] figure: Figure 2 : Results of different aspects of ablation studies.

[82] h3: 5.3 Implementation Details

[83] p: All components are implemented using the Verl distributed framework. The customer service agent is based on Qwen2.5-7/14B-Instruct, while the user role-playing model and reward generation model use Qwen2.5-32B-Instruct. The learning rate is set to 1 × 10 − 6 1\times 10^{-6} with cosine annealing, a warmup ratio of 0.1, and an annealing ratio of 0.2. The sampling group size is G = 4 G=4 , and the batch size is 128. Dialogues terminate when the user is satisfied, explicitly refuses, or reaches the maximum number of rounds T max = 15 T_{\max}=15 . Experiments are conducted on 8 NVIDIA A100 GPUs for service agent training and 2 NVIDIA H20 GPUs for other model inference. Detailed parameter settings please refer to Appendix .

[84] h3: 5.4 Baselines

[85] p: Large models. We evaluate several state-of-the-art closed-source and open-source models, including GPT-4.1 ( OpenAI, 2025 ) , Deepseek-v3 ( Liu et al., 2024 ) , LongCat-Flash ( Team et al., 2025 ) , and Qwen3-235B ( Yang et al., 2025 ) . Base models. Qwen2.5-Instruct (7B and 14B) ( Yang et al., 2024 ) are evaluated with carefully designed business prompts. SFT and RL models. SFT is performed on approximately 2k high-quality samples, obtained through filtering and enhancement of pre-collected business data. For RL, we compare CMPO with PPO ( Schulman et al., 2017 ) , GRPO ( Shao et al., 2024 ) , and CAPO ( Xie et al., 2025 )

[86] h2: 6 Experiment Results

[87] h3: 6.1 Main Results

[88] p: Table 1 presents the comparative experimental results of FDS scenarios with varying difficulty levels. We observe the following advances of our InteractCS-RL to answer ℋ ​ 1 \mathcal{H}1 :

[89] p: Significantly Improved Task Effectiveness: In the Hard scenario, the 14B model trained with InteractCS-RL can improve user satisfaction to 3.05 points, surpassing closed-source models including LongCat-Flash by nearly 40%; it also achieves a 100.0% dialogue completion rate (FR), outperforming top-tier closed-source models GPT-4.1 (83.8%) and DeepSeek-v3.2 (89.6%).

[90] p: High-Quality Dialogue Process: InteractCS-RL achieves the highest scores in both logical quality (11.34) and communication quality (27.43), representing a 10% improvement over the SFT model in each area. This indicates that the round-based principle introduced by GenRM effectively constrains the agent’s cognitive coherence during long-term interactions.

[91] p: Precise Cost Awareness: Under the preset constraint of Voucher Rate, all large models exhibited severe budget overruns. Supervised fine-tuning models performed relatively better but still exceeded the threshold. Our method successfully controlled the payout ratio around the set threshold of 30%.

[92] p: Universal Improvement Across Scale and Scenarios: Through our InteractCS-RL, both scale models showed consistent performance improvements and stably adapted to scenarios of varying difficulty.

[93] p: Overall, these results underscore the superiority of InteractCS-RL in internalizing complex service norms and cost boundaries, effectively breaking the performance ceiling of static imitation to achieve a better balance between service utility and operational economy.

[94] figure: Table 2 : Performance of our InteractCS-RL in τ 2 \tau^{2} -Bench. Methods Retail Airline Telecom Pass@1 Comm. Rate DB Rate Action Reward Pass@1 Comm. Rate DB Rate Action Reward Pass@1 Qwen2.5-7B 14.4% 61.4% 16.6% 152 14.0% 76.0% 18.0% 60 8.8% Qwen2.5-7B-SFT 15.8% 65.8% 18.4% 169 18.0% 78.0% 22.0% 61 10.5% InteractCS-RL 21.1 % 67.5 % 23.7 % 233 24.0 % 82.0 % 28.0 % 65 14.9 % Qwen2.5-14B 44.7% 80.7% 45.6% 337 16.0% 88.0% 20.0% 75 17.5% Qwen2.5-14B-SFT 43.9% 81.6% 45.2% 325 20.0% 88.0% 26.0% 74 20.2% InteractCS-RL (Ours) 47.4 % 85.1 % 49.1 % 355 28.0 % 92.0 % 32.0 % 75 24.6 %

[95] h3: 6.2 Studies and Ablation on CMPO

[96] p: In this section, we conduct a comprehensive analysis to validate the effectiveness of the proposed CMPO and its sub-components. We examine the impact of different reinforcement learning baselines, the necessity of the PID-controlled constraint mechanism, and the contribution of each reward component to answer ℋ ​ 2 \mathcal{H}2 .

[97] p: Efficacy of CMPO. We first compare InteractCS-RL against established RL baselines, including token-level PPO, session-level GRPO, and turn-level CAPO. Comparing CMPO with green lines, we can observe distinct trade-offs exist across different granularities. Token-level PPO achieves strong Logical Consistency (9.84) by optimizing immediate syntax probabilities but suffers significantly in goal completion (Sat. 2.29), indicating that dense token supervision struggles to capture long-horizon task utility. Conversely, standard GRPO improves Satisfaction (2.67) but exhibits degradation in process logic (9.56) due to the sparsity of outcome-only feedback. Our method, by integrating turn-level principle rewards with cost-sensitive outcomes, achieves a Pareto optimal state. It not only secures the highest User Satisfaction (2.74) and Communication Quality (26.12) but also enforces the strictly defined cost adherence (V-Rate 30.8%). This demonstrates that CMPO successfully bridges the gap between myopic generation and sparse objective optimization.

[98] p: Impact of Cost Constraint Mechanisms. A core contribution of our work is the PID-Lagrangian mechanism for global cost control. We analyze four settings in the blue part in Fig. 2 to understand the behavior of different constraint strategies, further visualization results are provided in the Appendix :

[99] p: w/o Cost ( λ = 0 \lambda=0 ): Without any penalty, the agent naturally maximizes user satisfaction by overly distributing compensation. This results in a Voucher Rate of 38.8%, significantly violating the operational threshold ( < 30 % <30\% ), although Satisfaction is relatively high (2.60).

[100] p: w/o PID Control: When removing the PID controller and relying on a basic relative error update, the agent struggles to stabilize. The Voucher Rate oscillates and settles at 34.5%, failing to strictly satisfy the constraint.

[101] p: w/o Dynamic λ \lambda (Fixed λ \lambda ): We also test a static penalty coefficient. Results show that a fixed penalty lacks the flexibility to adapt to training dynamics. It tends to over-suppress the agent’s actions (V-Rate drops to 24.6%), which severely harms the user experience, resulting in the lowest Satisfaction (2.52) among the groups.

[102] p: Ours (CMPO): By incorporating proportional and integral terms, our method dynamically adjusts λ \lambda to correct both instantaneous errors and long-term bias. This allows the model to converge precisely near the constraint boundary (V-Rate 30.8%) while maximizing utility, ultimately yielding the highest Satisfaction (2.74).

[103] p: Ablation of Hybrid Reward Components. Finally, we investigate the contribution of different reward signals in the orange part in Fig. 2 . Removing the Outcome Utility and Cost constraints ( w/o Out.+Cost ) results in a model that excels in Logical Consistency (10.21) but fails to resolve actual user problems (Sat. 2.42) or save costs (V-Rate 41.2%), as it only optimizes for conversational norms. Conversely, removing the Generative Reward Model ( w/o GenRM ) causes a drop in Logical Consistency to 9.56, as the model loses fine-grained guidance on empathy and procedure. The full CMPO integrates all components, demonstrating that high-quality service requires the simultaneous optimization of outcome utility, process logic, and cost constraints. Our approach achieves the best satisfaction under cost-aware conditions, validating the necessity of reward formulation.

[104] h3: 6.3 Generalizability

[105] p: In this section, we evaluate the generalizability of our InteractCS-RL in τ 2 \tau^{2} -bench to answer ℋ ​ 3 \mathcal{H}3 , with the results shown in Table 2 .

[106] p: As observed, the dual-control environment poses a significant challenge; standard models struggle to coordinate reasoning and action, with the Qwen2.5-7B Instruct model achieving less than 15% Pass@1 in the Retail and Airline domains. Furthermore, direct SFT demonstrates limited generalizability. In some cases, SFT even leads to performance degradation (e.g., Qwen2.5-14B-SFT drops from 44.7% to 43.9% in Retail), suggesting that static imitation learning fails to capture the underlying problem-solving logic required for unseen domains.

[107] p: In contrast, InteractCS-RL consistently outperforms baselines across all datasets and model sizes. On average across the three domains, our method improves the average Pass@1 rate by 5.6% compared to the SFT baseline on the 14B model. Crucially, the simultaneous improvements in DB Rate and Action Reward indicate that our approach significantly enhances the model’s ability to execute precise tool calls and adhere to complex domain constraints, even without specific training data for these domains. This suggests that our cost-aware reinforcement learning framework fosters robust, transferable reasoning capabilities rather than mere pattern matching.

[108] p: Additionally, the consistent gains in Communicate Rate (e.g., +6.1% in Retail for 7B) imply that our training methodology encourages the agent to be more informative and proactive. This demonstrates that InteractCS-RL not only solves the technical aspects of the task but also elevates the conversational standard, making the agent more effective at delivering critical information to users in a service context.

[109] h3: 6.4 Case Study

[110] p: In Appendix B , we present case studies comparing InteractCS-RL with the SFT baseline to highlight its superior decision-making. In FDS scenarios ( B.1 ), our method demonstrates refined adaptability to diverse user personas—successfully balancing empathetic appeasement with strict SOP and cost adherence—whereas SFT often falls into repetitive, ineffective dialogue loops. Furthermore, cross-domain evaluations on τ 2 \tau^{2} -bench ( B.2 ) show that InteractCS-RL better understands complex user intents and executes proactive guidance, overcoming the semantic gaps and mechanical stagnation prevalent in static SFT models.

[111] h2: 7 Conclusion

[112] p: In this paper, we proposed InteractCS-RL to address the critical tension between empathetic communication and operational cost in task-oriented dialogue. To reframe TOD as a multi-granularity reinforcement learning process, InteractCS-RL integrates a User-centric Interaction Framework for high-fidelity strategy exploration with CMPO, which employs a PID-Lagrangian controller to internalize global costs with turn-level generative process credit. Extensive experiments demonstrate that InteractCS-RL significantly outperforms state-of-the-art models, achieving better results between task score under budget constraints while maintaining robust performance across diverse domains.

[113] h2: Impact Statements

[114] p: This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.

[115] h2: References

[116] h2: Appendix A Benchmarks Description

[117] h3: A.1 FoodDeliverService

[118] h4: A.1.1 Benchmark Description

[119] p: FoodDeliverService is a specialized evaluation environment simulating complex customer service negotiations within the food delivery domain. Unlike standard task-oriented dialogues where user intent is static, this benchmark models realistic, friction-heavy interactions where the agent must manage user dissatisfaction, negotiate compensation, and business Standard Operating Procedures (SOPs). The framework is formalized as a dynamic multi-turn interaction environment where the User Simulator is parameterized by a tuple 𝒰 = { 𝒫 i ​ n ​ t , 𝒟 } \mathcal{U}=\{\mathcal{P}_{int},\mathcal{D}\} , representing intrinsic behavioral traits and extrinsic demands. The agent’s objective is to resolve complaints (e.g., cold food, missing items) while balancing user satisfaction against operational costs. Detailed specifications of the environment are provided in the Appendix .

[120] h4: A.1.2 Evaluation Metrics

[121] p: To comprehensively evaluate the agent’s performance, we employ a three-tiered metric system comprising Task Scores, Dialogue Quality Metrics, and Cost Control, as detailed below:

[122] p: Task Score: This category evaluates the direct outcome of the interaction from the user’s perspective and the agent’s adherence to system constraints.

[123] p: User Satisfaction (Sat.): A score ranging from 1 to 5, derived directly from the user simulator’s feedback signal at the end of the episode. It reflects the user’s emotional state and perceived resolution quality.

[124] p: Dialogue Finish Rate (FR): A binary success metric (averaged as a percentage) that validates the agent’s strict adherence to the required output format and pre-set rules. A session is considered ”Finished” only if the agent correctly utilizes the XML-based thinking/action tags (e.g., <action>voucher</action> ) and complies with hard constraints, such as issuing a voucher at most once per session.

[125] p: Dialogue Metric: We utilize a fine-grained “LLM-as-a-Judge” pipeline to evaluate the procedural quality of the conversation. The specific evaluation prompts used for this pipeline are detailed in the Appendix .

[126] p: Communication Quality (Comm.): A cumulative score (0–28) assessing the agent’s linguistic and interpersonal performance. It aggregates scores across seven dimensions: Identity Neutrality, Dialogue Quality (novelty/focus), Language Adaptability, Content Quality, Communication Effectiveness (conciseness/sincerity), Natural Fluency, and Context Adaptability.

[127] p: Logic Quality (Logic): A cumulative score (0–12) assessing the agent’s reasoning and business logic. It evaluates three critical areas: User Profile Recognition (identifying emotions/intent), Business Rule Capability (SOP compliance, authenticity, fairness, consistency), and Out-of-Distribution (OOD) Issue Recognition.

[128] p: Cost (Operational Efficiency):

[129] p: Voucher Rate (V-Rate): This metric quantifies the operational cost by measuring the percentage of sessions where the agent issues a financial compensation (voucher). To ensure sustainable service operations, agents are penalized if the V-Rate exceeds a threshold (e.g., < 30 % <30\% ), encouraging negotiation over immediate monetary concession.

[130] h4: A.1.3 Implementation Details

[131] p: The experimental setup for FoodDeliverService enforces a strict structured output format to facilitate automated parsing and reasoning evaluation. Agents are required to output a chain-of-thought process wrapped in <think> tags, followed by the response in <response> tags, and a final executable decision in <action> tags (values: chat or voucher ).

[132] p: To ensure consistent and objective evaluation of the Dialogue Metrics, we employ a specialized evaluator model prompted with the detailed scoring taxonomies described above. This evaluator analyzes the entire dialogue history to assign the Communication and Logic scores, ensuring that agents are rewarded not just for the final outcome, but for the empathy, logic, and safety of their conversational trajectory.

[133] p: For the experimental setup, we utilize DeepSeek-V3.2 as the user simulator to ensure high-fidelity and diverse interactions, with assistant models deployed on two NVIDIA H20 GPUs. The test sample consisted of 80 users, and three random tests were conducted.

[134] h3: A.2 τ 2 \tau^{2} -Bench

[135] h4: A.2.1 Benchmark Description

[136] p: τ 2 \tau^{2} -bench is a comprehensive evaluation framework designed to assess conversational agents in a dual-control environment, formalized as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP). Distinct from traditional benchmarks where the user acts as a passive information provider, τ 2 \tau^{2} -bench simulates realistic scenarios where both the agent and the user possess agency to employ tools and modify the shared world state. The benchmark specifically targets complex service domains, including Telecom, Retail, and Airline, requiring the agent not only to reason effectively about domain constraints but also to coordinate with and guide the user through necessary actions to resolve issues.

[137] h4: A.2.2 Evaluation Metrics

[138] p: We employ a multi-dimensional metric system to evaluate the agent’s performance:

[139] p: Pass@1: This serves as the primary indicator of task success, measuring the model’s ability to fulfill user requirements. For the Airline and Retail domains, Pass@1 is strictly defined by the satisfaction of two rule-based sub-metrics:

[140] p: Communicate Rate (Comm. Rate): This metric validates whether the agent has successfully conveyed all essential information required by the user (e.g., explaining policy details or confirming flight times).

[141] p: DB Rate: This evaluates the integrity of the post-interaction database. It checks if the final state of the database (e.g., order status updated to “refunded”) strictly matches the expected ground truth derived from the user’s intent.

[142] p: Action Reward: Beyond the final outcome, this metric assesses the procedural quality of the dialogue. For each task, a sequence of expected actions is predefined (including both mandatory and optimal steps). The action reward quantifies the proportion of these expected actions successfully executed by the model, reflecting its adherence to standard operating procedures.

[143] h4: A.2.3 Implementation Details

[144] p: For the experimental setup on this benchmark, we deploy the assistant models for inference using two NVIDIA H20 GPUs. To ensure high-fidelity and diverse user interactions during the evaluation, we utilize DeepSeek-V3.2 as the user simulator.

[145] h2: Appendix B Case Study

[146] h3: B.1 Food Deliver Service Case

[147] p: Here, we show some cases in FoodDeliverService .

[148] p: First, we show some rollout cases under our InteractCS-RL.

[149] p: (1) qwen-2.5-14b + InteractCS-RL engages in a dialogue with a generally cooperative user.

[150] p: The conversation below serves as a compelling demonstration of the model’s high fidelity and robust reasoning capabilities. By accurately cross-referencing order-specific metadata—such as the merchant ‘Bart’ and the ‘Mix French Toast’—without inventing non-existent details, the model proves it is virtually free of hallucinations. The assistant maintains a polite and empathetic tone throughout, yet remains fiscally responsible by systematically investigating the root cause (isolating the issue to the pudding vs. the entire order) rather than prematurely granting compensation. Furthermore, the transparent thinking process reveals a logical progression: it evaluates the user’s complaint history (rcTag), analyzes delivery signals (IM history), and tailors the final resolution to the user’s specific demand for feedback over financial recovery, ensuring both service quality and policy adherence.

[151] p: (2) qwen-2.5-7b + InteractCS-RL engages in a dialogue with a cooperative user.

[152] p: This case provides a strong validation of the model’s sophisticated and logical approach to compensation management. Rather than reflexively offering a refund at the first sign of a complaint, the model demonstrates a rigorous validation process by requesting photo evidence and conducting a targeted investigation into the time elapsed since delivery. By confirming that the user opened the meal only 10 minutes after arrival, the model successfully isolated the responsibility to the merchant, 4 Twins , for a preparation error while effectively ruling out delivery delays. The transition to compensation is handled with high fiscal responsibility; the model only proposes a proportionate 5-unit voucher after establishing the facts and aligning with the user’s ”Compensation Flexible” persona. This ”investigate-verify-compensate” workflow illustrates that the model has internalized complex business logic, maintains a near-zero hallucination rate regarding order details, and can achieve high satisfaction (4/5) through evidence-based reasoning rather than empty concessions.

[153] p: (3) qwen-2.5-7b + InteractCS-RL engages in a dialogue with a uncooperative user.

[154] p: This interaction highlights the model’s principled adherence to operational SOPs even in the face of an uncooperative user. Despite the user’s escalating tone and refusal to provide evidence, the model remained emotionally resilient and polite, successfully avoiding the ”easy path” of granting an unauthorized refund. The model accurately referenced the merchant Koyikodan and the specific complaints regarding the Puttu and Egg Curry without hallucinating additional issues. By maintaining a firm stance on the ”photo requirement” for immediate compensation while still escalating the refund request for standard review, the model demonstrated a perfect balance between empathy and policy enforcement . This proves the model’s logic is robust enough to handle ”Full Refund” personas without succumbing to pressure, ensuring both service integrity and brand protection.

[155] p: Second, we show some rollout cases under our baselines.

[156] p: (4) qwen-2.5-14b + Static SFT engages in a dialogue with a uncooperative user.

[157] p: This baseline case serves as a stark contrast to the high-performance model, illustrating the pitfalls of repetitive, non-proactive dialogue management. While the baseline model correctly identifies the merchant Shawarma Classic and adheres to the ”no evidence, no refund” policy, it suffers from significant logical stagnation and empathy exhaustion. Unlike the high-performance model, which conducts targeted inquiries into specific food attributes—such as the dryness of Puttu or the temperature of the pudding in previous cases—the baseline model remains trapped in a vague cycle of generic apologies, failing to probe for actionable details. This lack of investigative depth makes the repeated request for photo evidence feel like a defensive stall tactic rather than a genuine attempt to troubleshoot, directly leading to a critical failure in user satisfaction (1/5). Furthermore, the baseline model fails to offer alternative value—such as the strategic voucher pivot seen in the Koyikodan case—resulting in a conversational deadlock that exhausts the user’s patience and highlights a rigid, robotic approach to conflict resolution.

[158] h3: B.2 τ 2 \tau^{2} -bench case

[159] h4: B.2.1 Good Case with Qwen-2.5-14B InteractCS-RL

[160] table: Case Study: Good case for Qwen-2.5-14B trained by InteractCS-RL. Role Content Annotation & Analysis \endfirsthead Case Study: RL-Optimized Dialogue Trajectory (Continued) Role Content Annotation & Analysis

[161] h2: Instructions for reporting errors

[162] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[163] p: Tip: You can select the relevant text first, to include it in your report.

[164] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[165] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
