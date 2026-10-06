[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: https://github.com/exalsius/curtail-llm \reportnumber

[3] h1: Distributed LLM Pretraining During Renewable Curtailment Windows: A Feasibility Study

[4] h6: Abstract

[5] p: Training large language models (LLMs) requires substantial compute and energy. At the same time, renewable energy sources regularly produce more electricity than the grid can absorb, leading to curtailment , the deliberate reduction of clean generation that would otherwise go to waste. These periods represent an opportunity: if training is aligned with curtailment windows, LLMs can be pretrained using electricity that is both clean and cheap. This technical report presents a system that performs full-parameter LLM training across geo-distributed GPU clusters during regional curtailment windows, elastically switching between local single-site training and federated multi-site synchronization as sites become available or unavailable. Our prototype trains a 561M-parameter transformer model across three clusters using the Flower federated learning framework, with curtailment periods derived from real-world marginal carbon intensity traces. Preliminary results show that curtailment-aware scheduling preserves training quality while reducing operational emissions to 5–12% of single-site baselines.

[6] h6: keywords

[7] h2: 1 Introduction

[8] p: Large language models (LLMs) have become foundational components of modern software systems, enabling applications ranging from conversational assistants to code generation and scientific workflows. However, training state-of-the-art LLMs is resource intensive, consuming substantial GPU time and energy. At the same time, the rapid expansion of renewable generation capacity means that grids increasingly experience periods of curtailment : excess clean electricity that must be reduced because supply exceeds demand. These windows of surplus renewable energy vary in timing, duration, and location, but they represent compute time that is both low-carbon and low-cost.

[9] p: A growing body of work on carbon-aware computing has studied temporal and geographic load shifting for distributed ML workloads [ 47 , 7 , 31 ] . Yet, the practical feasibility of pretraining LLMs during curtailment windows remains unclear . Pretraining is a tightly coupled and stateful process: it requires sustained throughput to amortize fixed overheads such as compilation, data-loader warmup, and checkpoint and optimizer-state restores. Pausing, resuming, or migrating training between regions incurs nontrivial restart and communication overhead that can dominate when curtailment windows are short or sporadic. Recent work has shown that federated pretraining with infrequent synchronization can match or surpass centralized model quality for LLMs up to 7B parameters [ 39 ] , suggesting that the optimization approach itself is not a bottleneck. The open question is whether the systems overhead of elastic provisioning and communication across geo-distributed sites leaves enough useful compute time within curtailment windows. This motivates systems that can opportunistically exploit any available curtailment window and, when multiple regions are concurrently curtailed, combine their capacity to accelerate progress.

[10] p: In this technical report, we pretrain a nanochat [ 25 ] d20 (561M parameters) model on 12.8B tokens across three geographically distributed GPU clusters, where site availability is governed by curtailment windows derived from real-world marginal carbon intensity traces provided by WattTime [ 45 ] . Our goal is not to introduce a new learning algorithm, but to show that an operational system can support full-parameter training, including optimizer state and multi-site synchronization, under these constraints.

[11] p: We make the following contributions :

[12] p: we present a reactive system design for distributed LLM pretraining during curtailment windows that supports elastic participation of training sites. The system trains locally when only a single site is curtailed, performs periodic averaging of model states when multiple regions are concurrently curtailed, and pauses when no region is curtailed.

[13] p: we implement the system end-to-end using the Flower [ 6 ] FL framework and the Exalsius real-time control plane for provisioning GPU nodes across geo-distributed clusters.

[14] p: we evaluate the prototype by replaying historical grid conditions during training, and report on the resulting performance, energy usage, and operational carbon emissions.

[15] p: The prototype is publicly available on Github: 0

[16] h2: 2 Related Work

[17] h4: Carbon-aware computing.

[18] p: Research in the domain of carbon-aware optimization tries to reduce the operational emissions of computing systems through scheduling. Approaches leverage temporal shifting , executing workloads when electricity is cleaner [ 8 , 37 , 27 , 21 ] ; spatial shifting , placing workloads where electricity is cleaner [ 49 , 32 ] ; and approaches that combine both dimensions [ 40 , 22 , 26 , 47 ] . The objective is usually to minimize the carbon intensity (in gCO 2 /kWh) of consumed electricity, which—depending on methodology—can vary significantly over time and locations.

[19] h4: Exploiting curtailment windows.

[20] p: A complementary line of work focuses on utilizing renewable generation that would otherwise be curtailed. Curtailment occurs when renewable supply exceeds demand, storage, and transmission capacity, forcing clean electricity to be discarded. California curtailed 3.4 million megawatt-hours of utility-scale wind and solar output in 2024, a 29 % increase from the previous year [ 44 ] . Prior studies on exploiting curtailment windows in computing [ 43 , 18 , 42 , 49 , 47 ] show that leveraging excess renewable supply can reduce emissions while lowering operational costs.

[21] h4: Sustainable federated learning.

[22] p: Due to their high energy demand and scheduling flexibility, AI workloads are a central target for carbon-aware optimization [ 11 , 48 ] . In particular, federated learning enables training across geographically distributed resources [ 34 ] and is therefore increasingly used to exploit spatio-temporal variation in clean energy availability [ 31 , 7 , 41 , 47 ] . For example, FedZero [ 47 ] schedules training exclusively on excess renewable energy and idle compute capacity. However, the approach assumes fast provisioning of clients and minimal synchronization overhead, assumptions that do not hold for LLM pretraining at scale.

[23] h4: Distributed LLM pretraining.

[24] p: Recent results indicate that federated LLM pretraining can achieve performance comparable to centralized learning. DiLoCo [ 12 ] demonstrates competitive convergence for distributed LLM training across 8 GPU clusters, and Photon [ 39 ] reports perplexity matching or improving centralized baselines for models up to 7B parameters. The remaining challenge is therefore a systems problem: orchestrating elastic multi-site training under intermittent resource availability.

[25] h2: 3 System Design

[26] p: During pretraining, the most time and energy-intensive phase of LLM development, models are trained on large text corpora to minimize perplexity, with token budgets typically guided by scaling laws [ 23 ] . This stage produces a base model for subsequent fine-tuning. Our goal is to execute pretraining during curtailment windows when electricity is clean and cheap.

[27] figure: Figure 1 : Sites train only during curtailment windows (green), when renewable generation exceeds demand. If multiple sites are curtailed simultaneously, they train locally in parallel and periodically average model states.

[28] h3: 3.1 Problem Setting

[29] p: We consider N N geographically distributed GPU clusters, each capable of independent local training with multi-GPU data parallelism. An external signal indicates, for each site s s at time t t , whether the local grid is currently in a curtailment window. Let the curtailment indicator c s ​ ( t ) ∈ { 0 , 1 } c_{s}(t)\in\{0,1\} be 1 1 when site s s is curtailed and the active set 𝒜 ⁡ ( t ) = { s ∣ c s ​ ( t ) = 1 } \mathcal{A}(t)=\{s\mid c_{s}(t)=1\} . In practice, c s ​ ( t ) c_{s}(t) can be provided by grid operators or measured directly in case of co-located renewable generation. Otherwise, it can be derived from drops in locational marginal prices [ 3 , 33 ] , marginal grid carbon intensity metrics [ 45 ] , or time-of-use renewable energy certificates [ 10 , 13 ] .

[30] p: We face three challenges:

[31] p: curtailment is sporadic and correlated : a site may only be curtailed for short periods of time, and curtailment windows can overlap, particularly within the same balancing region. To accumulate enough compute, the system should exploit every sufficiently large window and coordinate training across sites.

[32] p: curtailment is inherently uncertain : forecasts for solar and wind carry substantial uncertainty, and curtailment additionally depends on grid congestion, demand, and operator decisions that are hard to predict. The system must therefore be fully reactive 1 1 1 designing for the reactive case also covers predictable schedules as a special instance. , and aggregation must tolerate sites joining or leaving 𝒜 ⁡ ( t ) \mathcal{A}(t) mid-round.

[33] p: provisioning is expensive : each provisioning event carries high cost (model transfer, optimizer warm-up, data-loader setup), and each synchronization round incurs significant communication overhead.

[34] h3: 3.2 Architecture and Execution Model

[35] p: A central coordinator monitors regional curtailment signals, and provisions or deprovisions training sites. After provisioning, sites receive the current model θ \theta , and perform local training on their data partition. To cope with fluctuating site availability, the system dynamically adapts its execution mode to the size of the active set 𝒜 ⁡ ( t ) \mathcal{A}(t) :

[36] p: | 𝒜 ⁡ ( t ) | = 0 |\mathcal{A}(t)|=0 : training is suspended and no compute resources are used.

[37] p: | 𝒜 ⁡ ( t ) | = 1 |\mathcal{A}(t)|=1 : the active site trains continuously without synchronization, avoiding communication and orchestration overhead.

[38] p: | 𝒜 ⁡ ( t ) | ≥ 2 |\mathcal{A}(t)|\geq 2 : all active sites train in parallel, which we refer to as federated mode . The coordinator initiates periodic synchronization rounds.

[39] p: Figure 1 illustrates a system state in federated mode. Training proceeds in timed rounds: At the start of each round, the coordinator dispatches the current global model to all active sites. Sites train locally until the round timer expires, complete their current gradient accumulation step, and return updated model parameters using work-weighted FedAvg [ 34 ] :

[40] table: θ = ∑ s ∈ 𝒜 b s ∑ k ∈ 𝒜 b k ​ θ s , \theta=\sum_{s\in\mathcal{A}}\frac{b_{s}}{\sum_{k\in\mathcal{A}}b_{k}}\,\theta_{s}, (1)

[41] p: where b s b_{s} denotes the number of batches processed by site s s during the round and θ s \theta_{s} its resulting model state. Weighting by work performed accounts for heterogeneous hardware and naturally handles sites joining or leaving during a round.

[42] p: Note, that we adopt federated learning for robustness to dynamic participation and heterogeneous throughput, rather than for privacy or data locality constraints. If data cannot be freely distributed across clients to approximate an IID distribution, the aggregation step can be replaced by more advanced methods that explicitly address data heterogeneity [ 24 , 12 , 20 , 38 ] .

[43] h3: 3.3 Curtailment-Aware Provisioning

[44] p: To prevent oscillations from short signal fluctuations, we apply time-based hysteresis when reacting to the curtailment signal c s ​ ( t ) c_{s}(t) . If c s ​ ( t ) c_{s}(t) remains continuously equal to 1 for at least τ ↑ \tau_{\uparrow} , the coordinator provisions site s s : a GPU node is allocated, the training stack is deployed, and the site connects to the server. If c s ​ ( t ) c_{s}(t) remains continuously equal to 0 for at least τ ↓ \tau_{\downarrow} , the site is deprovisioned. Before shutdown, the site completes its current gradient accumulation cycle, uploads model state and metrics, and terminates. Because provisioning incurs significant overhead, we prefer to keep a site running slightly longer rather than reprovision it, and therefore typically choose τ ↓ > τ ↑ \tau_{\downarrow}>\tau_{\uparrow} .

[45] h3: 3.4 Round Sizing and Overhead

[46] p: Related work on federated LLM pretraining typically uses large local step counts (e.g., 500 steps between global aggregation [ 12 , 39 ] ) to amortize the cost of synchronizing full model parameters. In our prototype, rounds are instead defined by wall clock time with a configurable duration Δ round \Delta_{\text{round}} , rather than by local step counts. This design reduces straggler effects in heterogeneous environments or when sites join late in a round: each site trains until the timer expires and then finishes its current gradient accumulation step before stopping.

[47] p: For reference: A single aggregation round for the 561M parameter model incurs roughly 60 s of serialization and communication overhead and about 55 s for DDP [ 29 ] process setup and teardown, totaling around 115 s of non training time per round. At Δ round = 600 \Delta_{\text{round}}=600 s, this corresponds to roughly 80 % compute utilization. During this interval, each client completes about 220 training steps, fewer than reported in prior work. However, those studies target models up to 7B parameters, where synchronization overheads are substantially higher. Longer rounds would further improve utilization but delay synchronization; identifying an optimal round duration is left for future work.

[48] h3: 3.5 Data Management

[49] p: The training corpus is pre-tokenized and split into S S fixed-size shards. The coordinator maintains a progress vector 𝐩 ∈ ℕ S \mathbf{p}\in\mathbb{N}^{S} , where p j p_{j} records the number of rows already consumed in shard j j . At the start of each round, all incomplete shards are sorted by descending progress and round-robin assigned to the active sites, so that each site receives a roughly equal partition of the remaining work. For heterogeneous setups, assignment can be weighted by expected compute capabilities.

[50] p: The coordinator sends each site its assigned shard indices together with the corresponding entries of 𝐩 \mathbf{p} , allowing the site to resume each shard from the correct position. After training, site s s returns both its updated model θ s \theta_{s} and progress values { p j ′ } \{p^{\prime}_{j}\} for its assigned shards. The coordinator applies model aggregation (Equation 1 ) and progress updates p j ← max ⁡ ( p j , p j ′ ) p_{j}\leftarrow\max(p_{j},\,p^{\prime}_{j}) atomically; if a site fails to report, neither θ \theta nor 𝐩 \mathbf{p} are affected.

[51] p: Within each multi-GPU site, row groups within the assigned shards are stride-partitioned across local DDP ranks [ 29 ] , ensuring that each token is consumed approximately once.

[52] h2: 4 Implementation

[53] p: We prototypically implemented the system using the Exalsius [ 14 ] control plane for infrastructure management and a custom Flower [ 6 ] Kubernetes operator for federated coordination.

[54] h4: Provisioning and cluster integration.

[55] p: Exalsius is a multi-site resource orchestrator for heterogeneous public cloud and on-premises environments built around Kubernetes. It provides lifecycle management for worker nodes, automated cluster deployment and operation, and integration with workload orchestration systems. Dynamic resource provisioning is abstracted into a uniform resource model that allows higher-level components to reason about available capacity without provider-specific logic. In our prototype, GPU nodes are automatically provisioned and incorporated into clusters according to § 3.3 , while node removal triggers a graceful detachment process to ensure cluster stability.

[56] h4: Federation orchestration.

[57] p: Federated training is deployed via a custom Kubernetes operator [ 15 ] for Flower. The operator reconciles a declarative Federation custom resource into a centralized coordinator and multiple distributed training sites. Elastic membership is achieved through the Exalsius node lifecycle API. Newly integrated nodes automatically become eligible training sites, while deprovisioned nodes leave the federation as part of the reconciliation loop. Secure inter-site communication is provided via integrated network encryption.

[58] h4: Runtime coordination.

[59] p: The coordinator runs as a Flower SuperLink and sites as SuperNodes , communicating via gRPC. Each round transfers the model state along with shard assignments and metrics. A custom server-side strategy implements scheduling and round control. Round completion and graceful shutdown signals are distributed via Redis pub/sub.

[60] figure: Figure 2 : Execution timeline of curtailment-aware pretraining, showing how training shifts across renewable curtailment windows in California, Texas, and South Australia.

[61] h2: 5 Experimental Evaluation

[62] p: We evaluate the prototype by pretraining a small-scale LLM across geographically distributed GPU clusters based on real curtailment traces.

[63] h4: Training workload.

[64] p: We pretrain nanochat d20, a 20-layer, 561M-parameter transformer model, following the reference implementation from the nanochat repository [ 25 ] . Training is performed on 12.8B tokens of FineWebEdu-100B [ 35 ] .

[65] h4: Infrastructure.

[66] p: We use three geographically distributed GPU clusters (sites), each equipped with four NVIDIA A100 GPUs. Although the clusters are physically distributed, the carbon-intensity traces associated with the chosen regions do not necessarily match the physical locations of the clusters in this prototype.

[67] h4: Curtailment signal.

[68] p: We use WattTime’s marginal operating emissions rate [ 45 ] as a proxy for renewable curtailment. This metric estimates the emissions of the marginal generator responding to incremental demand and drops sharply when excess renewable supply displaces fossil generation. We classify a region as curtailed when the value falls below 100 gCO 2 /kWh. Historical traces starting from January 11, 2026 at 17:00 UTC are replayed with Vessim [ 46 ] to enable controlled, repeatable evaluations.

[69] h4: Region selection.

[70] p: As curtailment events can be rare and sporadic, we initially selected four regions with comparatively frequent curtailment windows: California ISO Northern, SPP North Texas, South Australia, and Germany. This selection is optimistic but allows us to stress-test elastic behavior under realistic start and stop dynamics. During the experiment period, Germany exhibited no curtailment windows, resulting in effective training across three clusters.

[71] h3: 5.1 Execution Timeline

[72] p: The execution timeline of the curtailment-aware execution is visualized in Figure 2 . We first describe significant events, starting at January 11, 2026 at 17:00 UTC.

[73] p: 17:05 — Carbon intensity in California drops below 100 gCO 2 /kWh, triggering provisioning of the first site ( τ ↑ = 10 ​ s \tau_{\uparrow}=10s ). About five minutes later, the site connects to the coordinator, receives the initial model θ \theta and progress vector 𝐩 \mathbf{p} , and starts local training.

[74] p: 19:00 — The curtailment window in California ends. After a 10-minute hysteresis period ( τ ↓ = 10 \tau_{\downarrow}=10 min), the site receives a stop signal, returns the updated θ s \theta_{s} and { p j ′ } \{p^{\prime}_{j}\} , and is deprovisioned. Shortly after, a new curtailment window opens, the site is reprovisioned, and resumes local training.

[75] p: 21:40 — A curtailment window opens in South Australia; the corresponding site gets provisioned and connects. Training transitions to federated mode: Every Δ round = 10 \Delta_{\text{round}}=10 min, sites receive a stop signal, return θ s \theta_{s} and { p j ′ } \{p^{\prime}_{j}\} , and the coordinator aggregates and redistributes weights.

[76] p: 23:25 — The California curtailment window ends. After the hysteresis period, the site returns its progress and is deprovisioned. Training continues in South Australia.

[77] p: 3:20 — Texas enters a curtailment window, triggering federated mode. Note that short interruptions in curtailment of τ ↓ = 10 \tau_{\downarrow}=10 min do not trigger deprovisioning.

[78] p: 8:48 — Both active sites finish processing their assigned shards, and the run concludes.

[79] h3: 5.2 Training Performance

[80] p: Figure 3 compares training convergence under three scenarios: centralized single-site training, continuous two-site FL with Δ round = 10 \Delta_{\text{round}}=10 min, and our curtailment-aware execution. The centralized baseline processes the full token budget in 17.8 hours and reaches a final EMA-smoothed train perplexity of 14.8. Continuous two-site FL reduces wall-clock time to 11.1 hours but converges to a slightly higher perplexity of 15.5, reflecting the known tradeoff between parallelism and optimization noise.

[81] figure: Figure 3 : Curtailment-aware training reaches comparable perplexity as centralized training.

[82] p: Our curtailment-aware approach completes training in 14.6 hours, lying between the single- and two-site baselines in runtime. The final EMA-smoothed perplexity is 15.1, while the best perplexity observed during training is 14.6. Despite intermittent execution and transitions between single-site and federated modes, optimization remains stable and convergence closely matches continuous baselines.

[83] p: Table 1 summarizes runtime, best achieved train perplexity, and total energy consumption. Dynamic provisioning and synchronization introduce modest overhead, slightly increasing energy use compared to static deployments. Nevertheless, the results show that elastic participation and intermittent availability do not materially degrade training quality.

[84] figure: Table 1: Overhead from dynamic site provisioning slightly increases energy consumption. Scenario Runtime (hours) Best train perplexity Energy (kWh) Centralized 17.8 14.7 36.0 2-Site FL 11.1 15.2 36.1 Ours 14.6 14.6 37.7

[85] h3: 5.3 Energy and Carbon Footprint

[86] p: Total energy consumption is comparable across all scenarios, ranging from 36.0 to 37.7 kWh (Table 1 ). Our approach consumes slightly more energy due to extended wall-clock time and reprovisioning overhead during gaps in curtailment availability. Thus, emissions reductions stem from where and when energy is consumed rather than from reduced compute.

[87] p: To demonstrate curtailment utilization, Figure 5 displays the fraction of energy consumed during curtailment windows. Single-region baselines use curtailed energy only opportunistically while Germany exhibits no curtailment during the trace period. In contrast, our scheduler shifts training almost entirely into low-carbon windows, achieving 97% curtailed energy usage. The remaining 3% stem from training that extends into the hysteresis period τ ↓ \tau_{\downarrow} .

[88] p: We estimate operational emissions by multiplying site-level energy consumption with WattTime’s marginal operating emissions rate [ 45 ] . Single-region executions emit between 11.4 and 27.1 kgCO 2 , depending on regional grid conditions, whereas our curtailment-aware execution emits only 1.38 kgCO 2 . This corresponds to approximately 5–12% of the emissions of single-region baselines.

[89] figure: Figure 4 : Fraction of training energy drawn during curtailment windows. Figure 5 : Operational carbon emissions computed using marginal emissions accounting [ 45 ] .

[90] h2: 6 Discussion

[91] p: While our findings indicate that aligning training with curtailment windows is feasible and promising, this study also exposes limitations and open challenges that define an agenda for future work.

[92] h4: When curtailment-aware training is beneficial.

[93] p: Our evaluation targets regions with frequent curtailment, where overlapping windows enabled near continuous execution and in some cases even reduced runtime relative to a single site baseline. In practice, achievable throughput depends strongly on geography, seasonality, and weather conditions [ 33 ] . Future work should investigate permitting limited use of “dirty” energy to provide runtime guarantees. Beyond pretraining, curtailment-aware scheduling may benefit other energy-intensive AI workloads with flexible completion times and large compute budgets, such as reinforcement learning fine tuning and alignment, synthetic data generation, evaluation campaigns, and periodic model refreshes.

[94] h4: Systems challenges at scale.

[95] p: The effectiveness of curtailment-aware training depends on window duration relative to provisioning, synchronization, and state restoration overheads, which can dominate short windows. Scaling to larger models and more sites introduces increased overheads and additional challenges such as wide-area communication costs, data movement energy overheads, and failure recovery. Larger fleets may smooth availability but they also increase orchestration complexity and require robust progress tracking, optimizer state consistency, and fault tolerance. Future work could explore topology-aware synchronization [ 30 ] and warm standby capacity to reduce cold-start delays.

[96] h4: Carbon accounting and grid signals.

[97] p: We use marginal operating emissions rates as a proxy for curtailment, interpreting sharp drops as periods of excess clean generation. However, determining which signals should guide carbon-aware scheduling remains non-trivial. Ongoing revisions to the GHG Protocol Scope 2 Guidance [ 19 ] and recent research [ 16 , 17 , 36 ] highlight unresolved questions around temporal matching, marginal versus average emissions factors, and the conditions under which operational signals translate into verifiable emissions reductions. Identifying signals that are both operationally useful and auditable remains an important direction for future work.

[98] h4: Energy infrastructure considerations.

[99] p: At the infrastructure level, an increasing number of data centers are operated within microgrids that combine on-site or off-site generation with local battery storage [ 4 , 28 , 2 ] . Tight integration of such energy systems with cluster scheduling could buffer intermittency and further reduce reliance on grid supply [ 46 ] . Moreover, strategically siting GPU clusters near renewable generation or grid bottlenecks could increase access to curtailment windows and reduce transport distances for otherwise curtailed energy [ 9 ] . Depending on procurement contracts, such strategies could yield substantial cost savings for data center operators while also lowering grid congestion management costs for network operators, which in Germany alone amounted to €3.2 billion in 2023 [ 5 ] .

[100] h2: 7 Conclusion

[101] p: This technical report demonstrated that large language model pretraining can be aligned with renewable energy curtailment by elastically orchestrating geo-distributed GPU clusters. Our system dynamically switches between single-site execution and federated synchronization based on regional availability of low-carbon electricity, enabling full-parameter training under intermittent site participation. Experiments with real marginal carbon intensity traces show that curtailment-aware scheduling preserves convergence behavior and training stability while reducing operational emissions to 5–12% of single-region baselines.

[102] h2: Acknowledgements

[103] p: This research was made possible through the primary support of SPRIND - Federal Agency for Breakthrough Innovation, through their investment in the development of Exalsius. We also extend our gratitude to Deep Science Ventures for their financial backing and to TU Berlin for their institutional support. Finally, we thank WattTime for providing access to their API for querying marginal operating emissions rates.

[104] h2: References

[105] h2: Instructions for reporting errors

[106] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[107] p: Tip: You can select the relevant text first, to include it in your report.

[108] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[109] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
