# Exact v1 primary: 2601.19402

Raw primary excerpts, grouped by original tool response; physical lines distinguish local L-number resets.

## Original response: jan29_stdnext4head

PROTEUS: SLA-Aware Routing via Lagrangian RLfor Multi-LLM Serving Systems (https://arxiv.org/html/2601.19402v1)
citeturn28434view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19402v1","lineno":null}); Total lines: 249

## Original response: jan29_stdnext4core

PROTEUS: SLA-Aware Routing via Lagrangian RLfor Multi-LLM Serving Systems (https://arxiv.org/html/2601.19402v1)
citeturn28435view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28434view1","lineno":75}); Total lines: 249
L63: Query Encoding. Routing decisions must be fast. The encoder adds latency to every query, so we prioritize efficiency. We use DeBERTa-v3-small [cite36†8 ] for query encoding. This model has 22M parameters. It matches larger models like RoBERTa-base on NLU benchmarks. RoBERTa-base has 125M parameters, but DeBERTa-v3-small runs 5$\times$ faster. The encoder projects queries to a 256-dimensional embedding $z$ via a 2-layer MLP. This embedding feeds two heads.
L64: One is the $\tau$-conditioned policy network that outputs $\mu$. The other is a performance prediction head that outputs $p_{i}(x)$ for each model. On a single A100 GPU, encoding adds less than 2ms per query.
L65: Quality Preference Output. Rather than outputting discrete model selections, the policy outputs a continuous quality preference $\mu\in[0,1]$. This design choice allows smooth interpolation across operating points. When $\mu\approx 0$, the router favors cheap models. When $\mu\approx 1$, it favors expensive, high-quality models. The policy learns to map $(\text{query},\tau)$ to appropriate $\mu$ values.
L66: We use a Beta distribution for $\mu$ because it naturally constrains the output to $[0,1]$ and supports asymmetric concentration, allowing it to strongly favor quality or cost. The distribution parameters depend on the query embedding and target $\tau$. During training, a dual variable $\lambda$ (described below) provides additional constraint feedback.
L67: Adaptive Routing Scores. Given $\mu$, model selection uses the following scoring function.
L68: 
L69:  | $$s_{i}=p_{i}(x)+\mu\cdot b_{i}-(1-\mu)^{\gamma}\cdot c_{i}$$  |  | (2)
L70: The router selects $m^{*}=\arg\max_{i}s_{i}$. Here $p_{i}(x)$ is predicted model performance from a shared linear layer that maps the query embedding to $K$ correctness probabilities via sigmoid activation. Each model gets one probability. $b_{i}$ is a learned quality boost per model. $\gamma$ controls cost sensitivity. The non-linear term $(1-\mu)^{\gamma}$ matters. Unlike linear scoring [cite25†22 ], it lets the policy learn dataset-specific cost-quality tradeoffs.
L71: We make $\gamma$ learnable within $[2,8]$ so the system automatically discovers appropriate sensitivity for each deployment.
L72: ### 2.3 Constraint Enforcement via Learned Dual Variables
L73: 
L74: The core challenge is ensuring the router actually meets accuracy targets. Simply adding $\tau$ as input does not guarantee the output respects it. We use Lagrangian dual variables [cite37†3 , cite38†24 ] to enforce constraints during training. The trick is injecting constraint feedback directly into the policy.
L75: The Feedback Loop. During training, we track batch accuracy $\bar{p}_{\text{batch}}$ and compare it against the target $\tau$. A dual variable $\lambda$ adjusts based on constraint violations.
L76: 
L77:  | $$\lambda_{t+1}=\left[\lambda_{t}+\eta_{\lambda}\cdot(\tau-\bar{p}_{\text{batch}})\right]_{+}$$  |  | (3)
L78: When accuracy falls below target ($\bar{p}<\tau$), $\lambda$ increases. This penalizes the policy for cost-seeking behavior. When accuracy exceeds target, $\lambda$ decreases. This allows more aggressive cost optimization. The $[\cdot]_{+}$ operator ensures $\lambda\geq 0$. During training, this creates a feedback loop where the policy learns to associate $\tau$ values with appropriate routing behavior.
L79: The key is that $\lambda$ is injected into the policy network during training. The policy sees $\lambda$ as input alongside the query and $\tau$. It learns to anticipate constraint pressure. When $\lambda$ is high, the policy outputs higher $\mu$ values that favor quality. When $\lambda$ is low, it outputs lower $\mu$ values that favor cost. This creates correlation between $\tau$ and $\mu$. High targets produce high $\lambda$ values during training.
L80: This teaches the policy to output high $\mu$ for high $\tau$. At inference time, $\lambda$ is fixed at 1.0 and the policy responds to $\tau$ alone. The training phase has already taught it the $\tau\rightarrow\mu$ mapping through $\lambda$-mediated feedback.
L81: Policy Training. We train using Proximal Policy Optimization (PPO) [cite39†21 ]. PPO is a stable policy gradient method that clips updates to prevent large destabilizing changes. Supervised learning is unsuitable here because routing lacks ground-truth labels. We observe per-model outcomes (model $i$ scores $p_{i}$ on query $x$) but not which model the router should pick. The optimal choice depends on the cost-accuracy tradeoff specified by $\tau$. This varies at runtime. RL handles this naturally.
L82: The policy explores routing decisions, receives reward feedback, and learns to maximize the objective without explicit supervision. The reward combines accuracy, cost, and constraint satisfaction. We define $r(x,\mu)=p_{m^{*}}(x)-\alpha c_{m^{*}}+\lambda(p_{m^{*}}(x)-\tau)$. Training samples $\tau$ uniformly from the target range each batch. This ensures the policy learns to handle the full spectrum of accuracy requirements.
L83: Training Configuration. We use batch size 32 to balance gradient stability with memory constraints on a single A100 GPU. Training runs for 10K steps, roughly 4 hours per dataset. This is sufficient for dual variable convergence as monitored on validation accuracy. The dual learning rate $\eta_{\lambda}$=0.4 is set higher than the policy learning rate of $3{\times}10^{-4}$. This follows the “faster dual” heuristic [cite40†23 ].
L84: It accelerates constraint satisfaction by letting the Lagrangian multiplier adapt more quickly than the policy.
L85: ## 3 Experiments
L86: ### 3.1 Setup
L87: 
L88: Datasets. Evaluating LLM routers requires benchmarks that provide per-query correctness labels across multiple models with realistic cost signals. Standard NLP benchmarks lack this combination. We evaluate on the two gold-standard routing benchmarks that meet these requirements.
L89: RouterBench [cite23†9 ] provides 405K inference outcomes across 11 models. These span open-source variants like Llama-2-7B/13B/70B, Mistral-7B, and Mixtral-8x7B. API models include GPT-3.5, GPT-4, and Claude-2. Tasks cover reasoning with MMLU and HellaSwag, mathematics with GSM8K and MATH, and coding with HumanEval and MBPP. Model costs range from $0.0001 to $0.01 per query.
L90: SPROUT [cite25†22 ] complements RouterBench with 45K queries across 14 models. These include frontier systems like GPT-4o, Claude-3.5-Sonnet, and o3-mini. Llama variants range from 1B to 405B parameters. It uses instruction-following queries with LLM-based evaluation. Costs span $0.0001 to $0.05 per query.
L91: Together, these benchmarks test complementary aspects. RouterBench provides scale and task diversity with established models. SPROUT tests generalization to modern model pools with extreme cost variation. Oracle accuracy is 91.4% on RouterBench. On SPROUT it reaches 98.6%. We evaluate $\tau\in[0.85,0.91]$ for RouterBench and $\tau\in[0.85,0.95]$ for SPROUT. RouterBench uses 70/15/15 train/val/test splits. SPROUT uses official splits.
L92: Baselines. We compare against static strategies, learned routers, and ablated variants. For static baselines, Always-Best routes all queries to the highest-performing model (GPT-4 for RouterBench, o3-mini for SPROUT), maximizing accuracy but ignoring cost. Always-Cheapest routes to the lowest-cost model (Llama-2-7B for RouterBench, Llama-1B for SPROUT). Random provides uniform model selection.
L93: For learned routers, KNN [cite23†9 ] uses 5-nearest-neighbors to predict mean model performance via collaborative filtering from query embeddings. MLP [cite23†9 ] uses 3-layer networks for the same task. CARROT [cite25†22 ] uses DeBERTa-v3-base (86M parameters) to predict best model with score${}_{i}=(1{-}\mu)\cdot\text{acc}_{i}-\mu\cdot\text{cost}_{i}$ where we evaluate $\mu\in\{0.1,0.5,0.9\}$ representing quality-focused, balanced, and cost-focused configurations.
L94: RouteLLM-Style [cite29†17 ] extends binary win-rate prediction to multi-model selection by training a classifier predicting P(model_{i} is best $|$ query). OmniRouter-Style [cite30†16 ] adapts batch-level Lagrangian optimization to per-query routing with dual-head accuracy prediction and constraint parameter $\alpha$. For ablations, we test PROTEUS without $\tau$-conditioning (Unconstrained), fixed $\gamma$=3.0 (Fixed-Gamma), and no critic baseline (NoCritic) to isolate each component’s contribution.

## Original response: jan29_stdnext4eval

PROTEUS: SLA-Aware Routing via Lagrangian RLfor Multi-LLM Serving Systems (https://arxiv.org/html/2601.19402v1)
citeturn28436view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28434view1","lineno":95}); Total lines: 249
L89: RouterBench [cite23†9 ] provides 405K inference outcomes across 11 models. These span open-source variants like Llama-2-7B/13B/70B, Mistral-7B, and Mixtral-8x7B. API models include GPT-3.5, GPT-4, and Claude-2. Tasks cover reasoning with MMLU and HellaSwag, mathematics with GSM8K and MATH, and coding with HumanEval and MBPP. Model costs range from $0.0001 to $0.01 per query.
L90: SPROUT [cite25†22 ] complements RouterBench with 45K queries across 14 models. These include frontier systems like GPT-4o, Claude-3.5-Sonnet, and o3-mini. Llama variants range from 1B to 405B parameters. It uses instruction-following queries with LLM-based evaluation. Costs span $0.0001 to $0.05 per query.
L91: Together, these benchmarks test complementary aspects. RouterBench provides scale and task diversity with established models. SPROUT tests generalization to modern model pools with extreme cost variation. Oracle accuracy is 91.4% on RouterBench. On SPROUT it reaches 98.6%. We evaluate $\tau\in[0.85,0.91]$ for RouterBench and $\tau\in[0.85,0.95]$ for SPROUT. RouterBench uses 70/15/15 train/val/test splits. SPROUT uses official splits.
L92: Baselines. We compare against static strategies, learned routers, and ablated variants. For static baselines, Always-Best routes all queries to the highest-performing model (GPT-4 for RouterBench, o3-mini for SPROUT), maximizing accuracy but ignoring cost. Always-Cheapest routes to the lowest-cost model (Llama-2-7B for RouterBench, Llama-1B for SPROUT). Random provides uniform model selection.
L93: For learned routers, KNN [cite23†9 ] uses 5-nearest-neighbors to predict mean model performance via collaborative filtering from query embeddings. MLP [cite23†9 ] uses 3-layer networks for the same task. CARROT [cite25†22 ] uses DeBERTa-v3-base (86M parameters) to predict best model with score${}_{i}=(1{-}\mu)\cdot\text{acc}_{i}-\mu\cdot\text{cost}_{i}$ where we evaluate $\mu\in\{0.1,0.5,0.9\}$ representing quality-focused, balanced, and cost-focused configurations.
L94: RouteLLM-Style [cite29†17 ] extends binary win-rate prediction to multi-model selection by training a classifier predicting P(model_{i} is best $|$ query). OmniRouter-Style [cite30†16 ] adapts batch-level Lagrangian optimization to per-query routing with dual-head accuracy prediction and constraint parameter $\alpha$. For ablations, we test PROTEUS without $\tau$-conditioning (Unconstrained), fixed $\gamma$=3.0 (Fixed-Gamma), and no critic baseline (NoCritic) to isolate each component’s contribution.
L95: Metrics. We evaluate using standard routing metrics [cite23†9 ] (accuracy, cost, oracle gap) alongside metrics that capture target-driven capabilities.
L96: Adaptability Metrics. $\tau$-$\mu$ Correlation measures Pearson correlation between requested target $\tau$ and policy output $\mu$. High correlation ($>$0.9) indicates the policy faithfully translates business requirements into routing behavior. SLA Compliance measures the percentage of $\tau$ levels where achieved accuracy meets or exceeds $\tau$. This is the floor guarantee.
L97: Floor compliance is measured over the test distribution; per-query guarantees would require ensemble methods or conservative $\tau$ adjustment. We also report tolerance-band compliance at $\pm$2% and $\pm$5% thresholds, measuring precision of target matching.
L98: Efficiency Metrics. We introduce RE and RPI to capture routing efficiency holistically. Standard metrics like accuracy and cost ignore router overhead. Routing Efficiency (RE) measures accuracy improvement per unit latency. We define $\text{RE}=\frac{\text{Acc}-\text{Acc}_{\text{random}}}{\text{Latency}}$ in pp/ms. An RE of 10 means each millisecond yields 10 percentage points of accuracy gain over random selection. Routing Performance Index (RPI) balances quality, cost, and latency.
L99: We define $\text{RPI}=\frac{\text{Acc}}{\text{Acc}_{\text{oracle}}}\times\left(1-\frac{\text{Cost}}{\text{Cost}_{\text{max}}}\right)\times\left(1-\frac{t_{\text{router}}}{t_{\text{LLM}}}\right)\times 100$. RPI penalizes routers that achieve high accuracy via expensive models or slow inference.
L100: Implementation. We implement PROTEUS in PyTorch with HuggingFace Transformers for the DeBERTa-v3-small encoder. The policy network is a 2-layer MLP with 256 hidden units. It maps query embeddings, $\tau$, and $\lambda$ to Beta distribution parameters via softplus activation. A $\lambda$-gating layer applies element-wise modulation for constraint-aware attention. Training uses AdamW with learning rate $3{\times}10^{-4}$, batch size 64, and 10K steps.
L101: Dual updates happen every 5 batches at $\eta_{\lambda}$=0.4. Gradient clipping uses max norm 1.0. Training completes in 4 hours per dataset on a single A100 GPU. The router operates upstream of model serving and integrates with inference frameworks like vLLM [cite41†14 ] without modification. PROTEUS handles model selection while instance-level load balancing [cite42†11 ] distributes queries across replicas.
L102: ## 4 Results
L103: ### 4.1 Runtime Adaptability: The Core Capability
L104: 
L105: Table 1: PROTEUS Runtime Adaptability. A single trained policy accepts accuracy targets $\tau$ at runtime and adapts routing accordingly. Baselines require either retraining per-target (impractical for dynamic SLAs) or parameter sweeping (which yields arbitrary accuracy, not the requested target).
L106: Adaptability Metric  | RouterBench  | SPROUT
L107: --- | --- | ---
L108: $\tau$-$\mu$ Correlation  | 0.973  | 0.981
L109: Floor Compliance (acc $\geq\tau$)  | 100%  | 100%
L110: SLA Compliance ($\pm$5% tol.)  | 100%  | 67%^{†}
L111: SLA Compliance ($\pm$2% tol.)  | 44%  | 11%^{†}
L112: Cost Range (min/max $\tau$)  | 3.7$\times$  | 9.5$\times$
L113: 
L114: 
L115: Performance by Service Tier
L116: Dataset  | Tier  | $\tau$ Range  | Accuracy (margin)  | Cost
L117: --- | --- | --- | --- | ---
L118: RouterBench  | Economy  | 0.85–0.87  | 88.8% (+2.8%)  | $0.20
L119:  | Standard  | 0.87–0.89  | 90.4% (+2.4%)  | $0.29
L120:  | Premium  | 0.89–0.91  | 91.3% (+1.3%)  | $0.50
L121: SPROUT  | Economy  | 0.85–0.88  | 92.3% (+6.3%)  | $0.30
L122:  | Standard  | 0.88–0.92  | 93.8% (+5.8%)  | $0.62
L123:  | Premium  | 0.92–0.95  | 96.0% (+4.0%)  | $1.69
L124: Note: Costs in $/1K queries. Margin = achieved $-$ $\tau$ floor. ^{†}Lower tolerance-band compliance reflects intentional overshooting (+6% margin at low $\tau$ exceeds $\pm$5% band).
L125: Figure 2: Main Results. (a) SLA Compliance: PROTEUS (bars) consistently meets or exceeds each $\tau$ target (black lines), while baselines fail. OmniRouter (blue X markers) plateaus below targets despite per-$\tau$ training; CARROT (brown dotted lines) achieves fixed accuracy regardless of $\tau$. Green portions show accuracy above target. (b) Floor Guarantee + Cost: Achieved accuracy for RouterBench (blue) and SPROUT (orange) exceeds the floor constraint (dashed diagonal) across all $\tau$ values.
L126: Cost (dotted lines, right axis) increases with $\tau$. Shaded regions show the reliability margin. (c) Dynamic Adaptation: Four $\tau$-change scenarios showing PROTEUS tracking varying targets in real-time. Both datasets follow the target $\tau$ (dashed) with minimal lag across step, drift, cyclic, and realistic patterns.
L127: Table cite43†1 quantifies PROTEUS’s runtime adaptability. This is the ability to accept accuracy targets $\tau$ at inference time and adapt routing accordingly. The upper portion reports adaptability metrics across all $\tau$ values. The lower portion shows concrete service tier configurations. Baselines fail when evaluated on SLA compliance.
L128: Baselines fail to meet accuracy targets. Figure cite44†2 (a) compares PROTEUS against OmniRouter [cite30†16 ] and CARROT [cite25†22 ] on SLA compliance. OmniRouter (blue X markers) achieves only 22% floor compliance on RouterBench and 0% on SPROUT, despite being trained with Lagrangian constraints. It cannot adapt to runtime $\tau$ changes. CARROT (brown dotted lines) produces fixed accuracy regardless of the requested target.

## Original response: jan29_stdnext4tail

PROTEUS: SLA-Aware Routing via Lagrangian RLfor Multi-LLM Serving Systems (https://arxiv.org/html/2601.19402v1)
citeturn28437view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28434view1","lineno":129}); Total lines: 249
L125: Figure 2: Main Results. (a) SLA Compliance: PROTEUS (bars) consistently meets or exceeds each $\tau$ target (black lines), while baselines fail. OmniRouter (blue X markers) plateaus below targets despite per-$\tau$ training; CARROT (brown dotted lines) achieves fixed accuracy regardless of $\tau$. Green portions show accuracy above target. (b) Floor Guarantee + Cost: Achieved accuracy for RouterBench (blue) and SPROUT (orange) exceeds the floor constraint (dashed diagonal) across all $\tau$ values.
L126: Cost (dotted lines, right axis) increases with $\tau$. Shaded regions show the reliability margin. (c) Dynamic Adaptation: Four $\tau$-change scenarios showing PROTEUS tracking varying targets in real-time. Both datasets follow the target $\tau$ (dashed) with minimal lag across step, drift, cyclic, and realistic patterns.
L127: Table cite43†1 quantifies PROTEUS’s runtime adaptability. This is the ability to accept accuracy targets $\tau$ at inference time and adapt routing accordingly. The upper portion reports adaptability metrics across all $\tau$ values. The lower portion shows concrete service tier configurations. Baselines fail when evaluated on SLA compliance.
L128: Baselines fail to meet accuracy targets. Figure cite44†2 (a) compares PROTEUS against OmniRouter [cite30†16 ] and CARROT [cite25†22 ] on SLA compliance. OmniRouter (blue X markers) achieves only 22% floor compliance on RouterBench and 0% on SPROUT, despite being trained with Lagrangian constraints. It cannot adapt to runtime $\tau$ changes. CARROT (brown dotted lines) produces fixed accuracy regardless of the requested target.
L129: Setting $\mu$=0.1/0.5/0.9 yields 74.9%/67.9%/52.9% on RouterBench, none of which match the requested $\tau$.
L130: Why not retrain or sweep parameters? Two alternatives exist. First, retrain a separate model for each target $\tau$. Second, sweep baseline parameters ($\alpha$, $\mu$) to approximate desired accuracy. Neither is satisfactory. Retraining per-$\tau$ requires maintaining $N$ models for $N$ operating points, and cannot adapt at runtime. If a customer’s SLA changes mid-session or system load spikes, there is no mechanism to respond. Parameter sweeping is equally problematic.
L131: CARROT’s [cite25†22 ] $\mu$ controls cost-quality tradeoff, not accuracy target. Setting $\mu$=0.5 yields 67.9% accuracy on RouterBench, but if an operator needs exactly 85%, no $\mu$ value guarantees it. PROTEUS solves this by conditioning on $\tau$ directly, enabling one model to serve arbitrary targets with runtime adaptation.
L132: PROTEUS learns target-aware routing. The $\tau$-$\mu$ correlation is 0.973 on RouterBench. On SPROUT it reaches 0.981 (Table cite43†1 ). These values show that PROTEUS faithfully translates accuracy targets into quality preferences. A correlation near 1.0 means that when operators request higher $\tau$, the policy reliably outputs higher $\mu$ values. These favor expensive, high-quality models. This learned translation is what allows runtime adaptability.
L133: Floor guarantee with reliability margin. On held-out test data, PROTEUS achieves floor compliance across all evaluated $\tau$ levels. This means achieved accuracy meets or exceeds $\tau$. Figure cite44†2 (b) shows PROTEUS consistently exceeds the floor with a reliability margin. For the Economy tier with $\tau\in[0.85,0.87]$, PROTEUS achieves 88.8% on RouterBench. This is 2.8% above the tier floor. On SPROUT it achieves 92.3%, which is 6.3% above. This overshoot is intentional.
L134: The learned Lagrangian multiplier $\lambda$ provides a buffer against distribution shift. The margin shrinks as $\tau$ approaches the oracle ceiling. RouterBench tops out at 91.4%. SPROUT reaches 98.6%. This shows the policy recognizes feasibility limits.
L135: Tiered service delivery. The lower portion of Table cite43†1 shows practical deployment configurations. Each dataset has different $\tau$ ranges reflecting its oracle ceiling. RouterBench tops out at 91.4%, so Premium uses $\tau\in[0.89,0.91]$. SPROUT reaches 98.6%, enabling Premium at $\tau\in[0.92,0.95]$. On RouterBench, Economy tier costs $0.20/1K queries and delivers 88.8% accuracy. Premium costs $0.50/1K and achieves 91.3%. That is a 2.5$\times$ cost increase for 2.5 percentage points of accuracy.
L136: On SPROUT, the cost-accuracy gradient is steeper. Economy costs $0.30/1K. Premium costs $1.69/1K. That is 5.6$\times$ more for a 3.7 point accuracy gain. This cost-accuracy tradeoff enables operators to offer differentiated SLAs.

## Original response: jan29_stdnext4budget

PROTEUS: SLA-Aware Routing via Lagrangian RLfor Multi-LLM Serving Systems (https://arxiv.org/html/2601.19402v1)
citeturn28438view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28434view1","lineno":137}); Total lines: 249
L132: PROTEUS learns target-aware routing. The $\tau$-$\mu$ correlation is 0.973 on RouterBench. On SPROUT it reaches 0.981 (Table cite43†1 ). These values show that PROTEUS faithfully translates accuracy targets into quality preferences. A correlation near 1.0 means that when operators request higher $\tau$, the policy reliably outputs higher $\mu$ values. These favor expensive, high-quality models. This learned translation is what allows runtime adaptability.
L133: Floor guarantee with reliability margin. On held-out test data, PROTEUS achieves floor compliance across all evaluated $\tau$ levels. This means achieved accuracy meets or exceeds $\tau$. Figure cite44†2 (b) shows PROTEUS consistently exceeds the floor with a reliability margin. For the Economy tier with $\tau\in[0.85,0.87]$, PROTEUS achieves 88.8% on RouterBench. This is 2.8% above the tier floor. On SPROUT it achieves 92.3%, which is 6.3% above. This overshoot is intentional.
L134: The learned Lagrangian multiplier $\lambda$ provides a buffer against distribution shift. The margin shrinks as $\tau$ approaches the oracle ceiling. RouterBench tops out at 91.4%. SPROUT reaches 98.6%. This shows the policy recognizes feasibility limits.
L135: Tiered service delivery. The lower portion of Table cite43†1 shows practical deployment configurations. Each dataset has different $\tau$ ranges reflecting its oracle ceiling. RouterBench tops out at 91.4%, so Premium uses $\tau\in[0.89,0.91]$. SPROUT reaches 98.6%, enabling Premium at $\tau\in[0.92,0.95]$. On RouterBench, Economy tier costs $0.20/1K queries and delivers 88.8% accuracy. Premium costs $0.50/1K and achieves 91.3%. That is a 2.5$\times$ cost increase for 2.5 percentage points of accuracy.
L136: On SPROUT, the cost-accuracy gradient is steeper. Economy costs $0.30/1K. Premium costs $1.69/1K. That is 5.6$\times$ more for a 3.7 point accuracy gain. This cost-accuracy tradeoff enables operators to offer differentiated SLAs.
L137: Dynamic adaptation. Figure cite44†2 (c) evaluates PROTEUS when $\tau$ changes mid-session. We test four scenarios. Step change tests sudden SLA upgrades from $\tau$=0.82 to 0.92. Gradual drift applies linear increase from 0.80 to 0.95. Cyclic simulates sinusoidal variation modeling time-of-day pricing. Realistic captures off-peak/peak hour patterns with smoothed transitions. Each scenario spans 1,000 queries with 5 random seeds. PROTEUS tracks all patterns with 77% floor satisfaction on RouterBench.
L138: On SPROUT it achieves 82 to 86%. RouterBench shows 1.6 to 2.3% overshoot. SPROUT shows 4.3 to 5.2% overshoot. The important point is that there is zero adaptation delay. Since $\tau$ is a direct input, the policy responds instantaneously without retraining or parameter tuning. Operators can adjust targets per-query, per-customer, or based on system load.
L139: ### 4.2 Standard Routing Performance
L140: 
L141: Beyond adaptability, we evaluate PROTEUS on standard routing metrics. Table cite45†2 presents the comparison across both datasets.
L142: 
L143: Table 2: Routing Performance Comparison. PROTEUS achieves near-oracle accuracy with significant cost reduction and highest routing efficiency. RB=RouterBench, SP=SPROUT.
L144:  | Acc. (%)  | Cost ($/1K)  | Routing Eff.  | Overall Perf.
L145:  |  |  | (RE $\uparrow$)  | (RPI $\uparrow$)
L146: Method  | RB  | SP  | RB  | SP  | RB  | SP  | RB  | SP
L147: Static Baselines
L148: ---
L149: Random  | 52.4  | 71.8  | 0.86  | 1.7  | N/A^{‡}  | N/A^{‡}  | 42.4  | 56.8
L150: Cheapest  | 30.4  | 63.5  | 0.05  | 0.06  | N/A^{‡}  | N/A^{‡}  | 32.7  | 63.8
L151: Best Fixed^{†}  | 77.9  | 90.7  | 3.3  | 5.5  | N/A^{‡}  | N/A^{‡}  | 0.0  | 25.8
L152: Learned Routers
L153: ---
L154: KNN  | 77.2  | 73.8  | 2.3  | 1.7  | 7.4  | 0.9  | 25.5  | 58.1
L155: MLP  | 76.7  | 77.1  | 2.3  | 1.7  | 7.3  | 2.3  | 25.4  | 60.7
L156: CARROT-Quality  | 74.9  | 89.9  | 1.34  | 2.24  | 6.9  | 8.0  | 41.4  | 60.9
L157: CARROT-Balanced  | 67.9  | 83.9  | 0.21  | 0.35  | 6.0  | 6.8  | 69.5  | 81.0
L158: CARROT-Cost  | 52.9  | 74.0  | 0.09  | 0.11  | 0.2  | 1.2  | 55.7  | 69.9
L159: OmniRouter  | 66.2  | 82.6  | 0.24  | 0.64  | 5.3  | 6.0  | 67.1  | 76.6
L160: Ours
L161: ---
L162: PROTEUS  | 90.1  | 94.0  | 0.33  | 0.93  | 11.1  | 9.5  | 88.5  | 83.5
L163: Oracle  | 91.4  | 98.6  | 0.39  | 0.60  | N/A^{‡}  | N/A^{‡}  | 88.2  | 92.2
L164: ^{†}Best Fixed = GPT-4 (RB), o3-mini (SP).   ^{‡}RE undefined for methods with zero routing latency; RPI uses $t_{\text{router}}/t_{\text{LLM}}=0$. RE computed with batch size 8 latency (Table cite46†3 ); all learned routers use similar-sized encoders (22–125M params) with comparable latency.
L165: Near-oracle accuracy with cost savings. PROTEUS achieves 90.1% accuracy on RouterBench. This is 1.3 percentage points below oracle. Cost savings reach 90% versus GPT-4. On SPROUT, PROTEUS achieves 94.0% accuracy with a 4.6 percentage point gap. Savings reach 83% versus o3-mini. Learned baselines like KNN and MLP achieve only 77% accuracy at 7$\times$ higher cost. They default to expensive models rather than learning query-specific routing.
L166: Highest routing efficiency. PROTEUS achieves RE of 11.1 pp/ms on RouterBench. On SPROUT it reaches 9.5 pp/ms. Each millisecond of routing computation yields more than 10 percentage points of accuracy gain over random selection. On RouterBench, PROTEUS achieves higher RPI than Oracle with 88.5 versus 88.2. This shows that learned cost-quality tradeoffs can outperform pure quality optimization. By accepting a 1.4% quality reduction, PROTEUS saves 15% cost. This yields a net efficiency gain.
L167: On SPROUT, RPI of 83.5 approaches the oracle ceiling of 92.2.
L168: Table 3: PROTEUS Router Latency. Per-query routing latency (ms) and throughput on A100 GPU across batch sizes. Latency is dominated by the DeBERTa-v3-small encoder forward pass; the policy head adds $<$0.1ms.
L169: 
L170: Batch Size  | p50  | p95  | p99  | Throughput
L171: --- | --- | --- | --- | ---
L172: 1  | 8.7  | 8.9  | 9.0  | 115 q/s
L173: 8  | 2.9  | 3.0  | 3.1  | 345 q/s
L174: 32  | 2.6  | 2.7  | 2.7  | 385 q/s
L175: 64  | 2.6  | 2.6  | 2.7  | 385 q/s
L176: 128  | 2.6  | 2.6  | 2.6  | 385 q/s
L177: Throughput computed as 1000/p50. At batch size 8+, PROTEUS achieves $<$3ms per-query latency with 300+ queries/second throughput. Single-query latency (8.7ms) remains negligible compared to LLM inference (2–7 seconds).
L178: ### 4.3 Ablation Study
L179: 
L180: Table 4: Ablation Study. Performance change when removing components from PROTEUS-Full. $\Delta$Acc: accuracy change (%). $\Delta$Margin: change in buffer above $\tau$ floor (%). $\Delta$Gap: change in distance to oracle (%, higher = worse). $\Delta$Cost: relative cost change (%). Colors: significant ($|$ $\Delta$Acc$|$ $>$0.2), negligible ($|$ $\Delta$Acc$|$ $<$0.1).
L181:  | $\Delta$Acc (%)  | $\Delta$Margin (%)  | $\Delta$Gap (%)  | $\Delta$Cost
L182: Variant  | RB  | SP  | RB  | SP  | RB  | SP  | RB  | SP

## Original response: jan29_stdnext4proteustail

PROTEUS: SLA-Aware Routing via Lagrangian RLfor Multi-LLM Serving Systems (https://arxiv.org/html/2601.19402v1)
citeturn28439view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28434view1","lineno":180}); Total lines: 249
L133: Floor guarantee with reliability margin. On held-out test data, PROTEUS achieves floor compliance across all evaluated $\tau$ levels. This means achieved accuracy meets or exceeds $\tau$. Figure cite44†2 (b) shows PROTEUS consistently exceeds the floor with a reliability margin. For the Economy tier with $\tau\in[0.85,0.87]$, PROTEUS achieves 88.8% on RouterBench. This is 2.8% above the tier floor. On SPROUT it achieves 92.3%, which is 6.3% above. This overshoot is intentional.
L134: The learned Lagrangian multiplier $\lambda$ provides a buffer against distribution shift. The margin shrinks as $\tau$ approaches the oracle ceiling. RouterBench tops out at 91.4%. SPROUT reaches 98.6%. This shows the policy recognizes feasibility limits.
L135: Tiered service delivery. The lower portion of Table cite43†1 shows practical deployment configurations. Each dataset has different $\tau$ ranges reflecting its oracle ceiling. RouterBench tops out at 91.4%, so Premium uses $\tau\in[0.89,0.91]$. SPROUT reaches 98.6%, enabling Premium at $\tau\in[0.92,0.95]$. On RouterBench, Economy tier costs $0.20/1K queries and delivers 88.8% accuracy. Premium costs $0.50/1K and achieves 91.3%. That is a 2.5$\times$ cost increase for 2.5 percentage points of accuracy.
L136: On SPROUT, the cost-accuracy gradient is steeper. Economy costs $0.30/1K. Premium costs $1.69/1K. That is 5.6$\times$ more for a 3.7 point accuracy gain. This cost-accuracy tradeoff enables operators to offer differentiated SLAs.
L137: Dynamic adaptation. Figure cite44†2 (c) evaluates PROTEUS when $\tau$ changes mid-session. We test four scenarios. Step change tests sudden SLA upgrades from $\tau$=0.82 to 0.92. Gradual drift applies linear increase from 0.80 to 0.95. Cyclic simulates sinusoidal variation modeling time-of-day pricing. Realistic captures off-peak/peak hour patterns with smoothed transitions. Each scenario spans 1,000 queries with 5 random seeds. PROTEUS tracks all patterns with 77% floor satisfaction on RouterBench.
L138: On SPROUT it achieves 82 to 86%. RouterBench shows 1.6 to 2.3% overshoot. SPROUT shows 4.3 to 5.2% overshoot. The important point is that there is zero adaptation delay. Since $\tau$ is a direct input, the policy responds instantaneously without retraining or parameter tuning. Operators can adjust targets per-query, per-customer, or based on system load.
L139: ### 4.2 Standard Routing Performance
L140: 
L141: Beyond adaptability, we evaluate PROTEUS on standard routing metrics. Table cite45†2 presents the comparison across both datasets.
L142: 
L143: Table 2: Routing Performance Comparison. PROTEUS achieves near-oracle accuracy with significant cost reduction and highest routing efficiency. RB=RouterBench, SP=SPROUT.
L144:  | Acc. (%)  | Cost ($/1K)  | Routing Eff.  | Overall Perf.
L145:  |  |  | (RE $\uparrow$)  | (RPI $\uparrow$)
L146: Method  | RB  | SP  | RB  | SP  | RB  | SP  | RB  | SP
L147: Static Baselines
L148: ---
L149: Random  | 52.4  | 71.8  | 0.86  | 1.7  | N/A^{‡}  | N/A^{‡}  | 42.4  | 56.8
L150: Cheapest  | 30.4  | 63.5  | 0.05  | 0.06  | N/A^{‡}  | N/A^{‡}  | 32.7  | 63.8
L151: Best Fixed^{†}  | 77.9  | 90.7  | 3.3  | 5.5  | N/A^{‡}  | N/A^{‡}  | 0.0  | 25.8
L152: Learned Routers
L153: ---
L154: KNN  | 77.2  | 73.8  | 2.3  | 1.7  | 7.4  | 0.9  | 25.5  | 58.1
L155: MLP  | 76.7  | 77.1  | 2.3  | 1.7  | 7.3  | 2.3  | 25.4  | 60.7
L156: CARROT-Quality  | 74.9  | 89.9  | 1.34  | 2.24  | 6.9  | 8.0  | 41.4  | 60.9
L157: CARROT-Balanced  | 67.9  | 83.9  | 0.21  | 0.35  | 6.0  | 6.8  | 69.5  | 81.0
L158: CARROT-Cost  | 52.9  | 74.0  | 0.09  | 0.11  | 0.2  | 1.2  | 55.7  | 69.9
L159: OmniRouter  | 66.2  | 82.6  | 0.24  | 0.64  | 5.3  | 6.0  | 67.1  | 76.6
L160: Ours
L161: ---
L162: PROTEUS  | 90.1  | 94.0  | 0.33  | 0.93  | 11.1  | 9.5  | 88.5  | 83.5
L163: Oracle  | 91.4  | 98.6  | 0.39  | 0.60  | N/A^{‡}  | N/A^{‡}  | 88.2  | 92.2
L164: ^{†}Best Fixed = GPT-4 (RB), o3-mini (SP).   ^{‡}RE undefined for methods with zero routing latency; RPI uses $t_{\text{router}}/t_{\text{LLM}}=0$. RE computed with batch size 8 latency (Table cite46†3 ); all learned routers use similar-sized encoders (22–125M params) with comparable latency.
L165: Near-oracle accuracy with cost savings. PROTEUS achieves 90.1% accuracy on RouterBench. This is 1.3 percentage points below oracle. Cost savings reach 90% versus GPT-4. On SPROUT, PROTEUS achieves 94.0% accuracy with a 4.6 percentage point gap. Savings reach 83% versus o3-mini. Learned baselines like KNN and MLP achieve only 77% accuracy at 7$\times$ higher cost. They default to expensive models rather than learning query-specific routing.
L166: Highest routing efficiency. PROTEUS achieves RE of 11.1 pp/ms on RouterBench. On SPROUT it reaches 9.5 pp/ms. Each millisecond of routing computation yields more than 10 percentage points of accuracy gain over random selection. On RouterBench, PROTEUS achieves higher RPI than Oracle with 88.5 versus 88.2. This shows that learned cost-quality tradeoffs can outperform pure quality optimization. By accepting a 1.4% quality reduction, PROTEUS saves 15% cost. This yields a net efficiency gain.
L167: On SPROUT, RPI of 83.5 approaches the oracle ceiling of 92.2.
L168: Table 3: PROTEUS Router Latency. Per-query routing latency (ms) and throughput on A100 GPU across batch sizes. Latency is dominated by the DeBERTa-v3-small encoder forward pass; the policy head adds $<$0.1ms.
L169: 
L170: Batch Size  | p50  | p95  | p99  | Throughput
L171: --- | --- | --- | --- | ---
L172: 1  | 8.7  | 8.9  | 9.0  | 115 q/s
L173: 8  | 2.9  | 3.0  | 3.1  | 345 q/s
L174: 32  | 2.6  | 2.7  | 2.7  | 385 q/s
L175: 64  | 2.6  | 2.6  | 2.7  | 385 q/s
L176: 128  | 2.6  | 2.6  | 2.6  | 385 q/s
L177: Throughput computed as 1000/p50. At batch size 8+, PROTEUS achieves $<$3ms per-query latency with 300+ queries/second throughput. Single-query latency (8.7ms) remains negligible compared to LLM inference (2–7 seconds).
L178: ### 4.3 Ablation Study
L179: 
L180: Table 4: Ablation Study. Performance change when removing components from PROTEUS-Full. $\Delta$Acc: accuracy change (%). $\Delta$Margin: change in buffer above $\tau$ floor (%). $\Delta$Gap: change in distance to oracle (%, higher = worse). $\Delta$Cost: relative cost change (%). Colors: significant ($|$ $\Delta$Acc$|$ $>$0.2), negligible ($|$ $\Delta$Acc$|$ $<$0.1).
L181:  | $\Delta$Acc (%)  | $\Delta$Margin (%)  | $\Delta$Gap (%)  | $\Delta$Cost
L182: Variant  | RB  | SP  | RB  | SP  | RB  | SP  | RB  | SP
L183: PROTEUS-Full  | 90.1  | 94.0  | +2.1  | +4.0  | 1.3  | 4.6  | $0.33  | $0.93
L184: $-$Constraint ($\lambda$)  | $-$0.27  | $-$0.53  | $-$0.27  | $-$0.5  | +0.27  | +0.53  | $-$8%  | $-$25%
L185: $-$Learnable $\gamma$  | $\approx$0  | $-$0.62  | $\approx$0  | $-$0.6  | $\approx$0  | +0.62  | $\approx$0  | $-$44%
L186: $-$Critic  | $-$0.04  | $-$0.03  | $-$0.04  | $-$0.03  | +0.04  | +0.03  | $-$2%  | $-$1%
L187: Takeaway: $\lambda$ is critical (drops accuracy on both datasets). Learnable $\gamma$ matters only on SPROUT (wider cost range). Critic is optional.
L188: 
L189: Table cite47†4 isolates how each architectural component contributes to PROTEUS performance. We ablate three elements. First is the Lagrangian constraint mechanism ($\lambda$). Second is the learnable cost sensitivity parameter ($\gamma$). Third is the critic network used for variance reduction in policy gradients.
L190: Constraint mechanism is essential. Removing the $\lambda$ feedback loop causes the largest accuracy drops. Accuracy falls by 0.27% on RouterBench. On SPROUT it falls by 0.53%. Without $\lambda$, the policy has no mechanism to track constraint violations during training. It learns a fixed quality-cost tradeoff rather than adapting to meet specified targets. The cost reduction of 8% to 25% confirms the policy becomes more aggressive about cost optimization when unconstrained.
L191: It sacrifices accuracy in the process. This validates our core hypothesis that learned dual variables allow reliable target satisfaction.
L192: Learnable $\gamma$ matters for heterogeneous pools. The learnable cost sensitivity $\gamma$ in Equation cite48†2 has negligible effect on RouterBench. But it causes a 0.62% accuracy drop on SPROUT. The difference stems from cost distributions. RouterBench spans 3.7$\times$ cost variation. SPROUT spans 9.5$\times$. With fixed $\gamma$=3.0, the policy cannot adapt its cost weighting to handle extreme cost ratios.
L193: The 44% cost reduction on SPROUT when removing learnable $\gamma$ indicates the policy defaults to cheaper models. It fails to learn appropriate cost-quality tradeoffs. For deployments with diverse model pools, learnable $\gamma$ is important.
L194: Critic provides marginal benefit. Removing the critic network yields negligible accuracy changes ($<$0.05%). This aligns with prior work showing critics add variance reduction in multi-step problems but provide little benefit for single-step MDPs [cite49†20 ]. Since routing is a single-step decision (query in, model out), the REINFORCE gradient estimator suffices. Practitioners can omit the critic to reduce model complexity without performance loss.
L195: ## 5 Conclusion
L196: PROTEUS shows that LLM routing can be framed as target-driven policy learning. This lets operators adapt to accuracy requirements at runtime without retraining. A single trained model covers the full accuracy spectrum. The $\tau$-conditioning achieves 0.97 to 0.98 correlation between what operators ask for and how the router behaves. On held-out test data, the learned Lagrangian multipliers reliably satisfy floor constraints across all evaluated targets.
L197: Baselines that use heuristic multipliers achieve only 0 to 22%. This reliability does not come at the cost of routing quality.
L198: Limitations. RouterBench’s model pool includes Llama-2, GPT-3.5, GPT-4, and Claude-2. These predate current frontier models. SPROUT covers narrower task distributions. The larger oracle gap on SPROUT reflects its higher oracle ceiling. SPROUT has 98.6% oracle accuracy compared to RouterBench’s 91.4%. It also has wider cost variation at 9.5$\times$ compared to 3.7$\times$. This creates more challenging cost-quality tradeoffs. Both datasets exhibit compressed accuracy ranges among mid-tier models.
L199: This makes fine-grained $\tau$ distinctions difficult. PROTEUS also trains on ground-truth correctness labels. This is the standard setting for routing research [cite23†9 , cite25†22 , cite29†17 ]. But production systems lack such labels by default. Deployment would require periodic sampling with human annotation or LLM-as-judge [cite50†13 ] evaluation to generate training signals. The reliability margin of 1.3 to 6.3% overshoot buffers against distribution shift. Sustained drift would require policy updates.
L200: Future Work. Several directions warrant investigation. Bandit feedback formulations where only the selected model’s outcome is observed would reduce annotation cost and allow continual learning without full model pool evaluation. This connects to contextual bandit research [cite51†25 ] but with the added challenge of SLA constraints. Latency-aware routing could extend the objective to jointly optimize accuracy, cost, and response time by incorporating latency as a third term in the reward function.
L201: This is relevant for interactive applications where tail latency matters as much as throughput. Hierarchical routing with cascaded decisions could improve efficiency for large pools. The router would first select a model tier, then a specific model, reducing the action space at each decision point. Multi-objective $\tau$ specifications would allow operators to set accuracy floors and cost ceilings simultaneously.
L202: This would provide finer deployment control and align with service level objectives that specify both quality and budget constraints. Extending PROTEUS to multi-turn conversations introduces temporal dependencies where routing decisions affect future context length and cost accumulation. Routing benchmarks with diverse model pools spanning [0.5, 0.99] accuracy ranges would also allow evaluation of fine-grained target control beyond what current datasets support.
L203: ## Acknowledgments
L204: 
L205: We are grateful to the open-source communities behind PyTorch, HuggingFace Transformers, and the DeBERTa model, which made this research possible. We also thank the authors of RouterBench and SPROUT for releasing their datasets and evaluation frameworks publicly, enabling reproducible research in LLM routing. The availability of these resources and the broader culture of open benchmarking in the ML systems community has been invaluable to this work.
L206: Generative AI tools were used to assist with editing and refining the manuscript text. All technical content, experimental design, implementation, and analysis were conducted by the authors, who take full responsibility for the work.
L207: ## References
L208:   * [1] P. Aggarwal, A. Madaan, A. Anand, S. P. Potharaju, S. Mishra, P. Zhou, A. Gupta, D. Rajagopal, K. Kappaganthu, Y. Yang, S. Upadhyay, M. Faruqui, and Mausam (2024) AutoMix: automatically mixing language models. In NeurIPS, Note: arXiv:2310.12963 Cited by: cite52†§1 .
L209:   * [2] S. Ahmad, H. Guan, B. D. Friedman, T. Williams, R. K. Sitaraman, and T. Woo (2024) Proteus: a high-throughput inference-serving system with accuracy scaling. In ASPLOS, Cited by: cite53†§1 .
L210:   * [3] E. Altman (1999) Constrained markov decision processes. CRC Press. Cited by: cite54†§2.3 .
L211:   * [4] AWS (2024) Multi-llm routing strategies for generative ai applications on aws. Note: cite55†https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/†aws.amazon.com Accessed: 2025-01-15 Cited by: cite56†§1 .
L212:   * [5] L. Chen, M. Zaharia, and J. Zou (2023) FrugalGPT: how to use large language models while reducing cost and improving performance. arXiv preprint arXiv:2305.05176. Cited by: cite52†§1 .
L213:   * [6] D. Crankshaw, X. Wang, G. Zhou, M. J. Franklin, J. E. Gonzalez, and I. Stoica (2017) Clipper: a low-latency online prediction serving system. In NSDI, Cited by: cite53†§1 .
L214:   * [7] D. Ding, A. Mallick, C. Wang, R. Sim, S. Mukherjee, V. Ruhle, L. V.S. Lakshmanan, and A. H. Awadallah (2024) Hybrid llm: cost-efficient and quality-aware query routing. In ICLR, Note: arXiv:2404.14618 Cited by: cite52†§1 .
L215:   * [8] P. He, J. Gao, and W. Chen (2023) DeBERTaV3: improving deberta using electra-style pre-training with gradient-disentangled embedding sharing. In International Conference on Learning Representations, Cited by: cite57†§2.2 .
L216:   * [9] Q. J. Hu, J. Bieker, X. Li, N. Jiang, B. Keigwin, G. Ranganath, K. Keutzer, and S. K. Upadhyay (2024) RouterBench: a benchmark for multi-llm routing system. arXiv preprint arXiv:2403.12031. Cited by: cite52†§1 , cite58†§3.1 , cite59†§3.1 , cite60†§3.1 , cite61†§5 .
L217:   * [10] Z. Huang, G. Ling, Y. Lin, Y. Chen, S. Zhong, H. Wu, and L. Lin (2025) RouterEval: a comprehensive benchmark for routing llms to explore model-level scaling up in llms. arXiv preprint arXiv:2503.10657. Cited by: cite52†§1 .
L218:   * [11] K. Jain, A. Parayil, A. Mallick, E. Choukse, X. Qin, J. Zhang, Í. Goiri, R. Wang, C. Bansal, V. Rühle, A. Kulkarni, S. Kofsky, and S. Rajmohan (2025) Performance aware llm load balancer for mixed workloads. In EuroMLSys, Cited by: cite62†§3.1 .
L219:   * [12] S. Jaiswal, K. Jain, Y. Simmhan, A. Parayil, A. Mallick, R. Wang, R. St. Amant, C. Bansal, V. Rühle, A. Kulkarni, S. Kofsky, and S. Rajmohan (2025) SageServe: optimizing llm serving on cloud data centers with forecast aware auto-scaling. arXiv preprint arXiv:2502.14617. Cited by: cite56†§1 .
L220:   * [13] D. Jiang, X. Ren, and B. Y. Lin (2023) LLM-blender: ensembling large language models with pairwise ranking and generative fusion. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Cited by: cite61†§5 .
L221:   * [14] W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, and I. Stoica (2023) Efficient memory management for large language model serving with pagedattention. In Proceedings of SOSP, Cited by: cite62†§3.1 .
L222:   * [15] P. Liang, R. Bommasani, T. Lee, et al. (2023) Holistic evaluation of language models. Transactions on Machine Learning Research. Cited by: cite52†§1 .
L223:   * [16] K. Mei, W. Xu, M. Guo, S. Lin, and Y. Zhang (2025) OmniRouter: budget and performance controllable multi-llm routing. arXiv preprint arXiv:2502.20576. Cited by: cite52†§1 , cite63†§2.1 , cite59†§3.1 , cite64†§4.1 .
L224:   * [17] I. Ong, A. Almahairi, V. Wu, W. Chiang, T. Wu, J. E. Gonzalez, M. W. Kadous, and I. Stoica (2024) RouteLLM: learning to route llms with preference data. arXiv preprint arXiv:2406.18665. Cited by: cite52†§1 , cite63†§2.1 , cite59†§3.1 , cite61†§5 .
L225:   * [18] OpenAI (2025) OpenAI api pricing. Note: cite65†https://openai.com/api/pricing/†openai.com Accessed: 2025-01-15 Cited by: cite56†§1 .
L226:   * [19] F. Romero, Q. Li, N. J. Yadwadkar, and C. Kozyrakis (2021) INFaaS: automated model-less inference serving. In ATC, Cited by: cite53†§1 .
L227:   * [20] J. Schulman, P. Moritz, S. Levine, M. Jordan, and P. Abbeel (2016) High-dimensional continuous control using generalized advantage estimation. In International Conference on Learning Representations, Cited by: cite66†§4.3 .
L228:   * [21] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov (2017) Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347. Cited by: cite67†§2.3 .
L229:   * [22] S. Somerstep, F. M. Polo, A. F. M. de Oliveira, P. Mangal, M. Silva, O. Bhardwaj, M. Yurochkin, and S. Maity (2025) CARROT: a cost aware rate optimal router. arXiv preprint arXiv:2502.03261. Cited by: cite52†§1 , cite63†§2.1 , cite68†§2.2 , cite69†§3.1 , cite59†§3.1 , cite64†§4.1 , cite70†§4.1 , cite61†§5 .
L230:   * [23] A. Stooke, J. Achiam, and P. Abbeel (2020) Responsive safety in reinforcement learning by pid lagrangian methods. In International Conference on Machine Learning, pp. 9133–9143. Cited by: cite71†§2.3 .
L231:   * [24] C. Tessler, D. J. Mankowitz, and S. Mannor (2019) Reward constrained policy optimization. In International Conference on Learning Representations, Cited by: cite54†§2.3 .
L232:   * [25] W. Wang, T. Yang, H. Chen, Y. Zhao, F. Dernoncourt, R. A. Rossi, and H. Eldardiry (2025) Learning to route llms from bandit feedback: one policy, many trade-offs. arXiv preprint arXiv:2510.07429. Cited by: cite72†§5 .


