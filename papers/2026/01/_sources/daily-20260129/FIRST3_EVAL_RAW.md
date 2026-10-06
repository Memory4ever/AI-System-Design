Revisiting Parameter Server in LLM Post-Training (https://arxiv.org/html/2601.19362v1)
citeturn28102view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19362v1","lineno":122}); Total lines: 575
L102: The classic PS architecture (cite39†Dean et al., 2012 ; cite40†Li et al., 2014 ) separates model state from model computation, where a set of server nodes is responsible for storing the model’s parameters and optimizer states. Meanwhile, a set of worker nodes pulls parameters from the servers, performs the forward and backward computations on its local data, and then pushes the resulting gradients back to the servers. The servers then aggregate these gradients and apply the updates.
L103: This design decouples the progress of individual workers and provides a natural tolerance for stragglers, which is a key advantage for the imbalanced workloads common in LLM post-training.
L104: As shown in Figure cite67†6 , ODC paradigm reframes FSDP as a modern, decentralized PS. Instead of using dedicated server nodes, we colocate the server and worker roles by evenly partitioning parameters, gradients, and optimizer states across all devices. Each device acts as a server by owning and managing a shard of the model’s parameters and optimizer state. Simultaneously, it acts as a worker by executing the forward and backward passes on its assigned data.
L105: This decentralized, co-located design mirrors the memory layout of FSDP and avoids the network bottlenecks of a centralized PS. While colocated roles has precedent in some PS systems (cite68†Jiang et al., 2020 ), our approach is novel in its direct integration with FSDP’s sharding mechanism.
L106: Ultimately, by replacing FSDP’s per-layer collectives with on-demand point-to-point communication, our method gains the imbalance tolerance of a PS while retaining the core benefits of FSDP: memory efficiency, decentralization, scalability, and simplicity.
L107: ### 3.2 Implementation
L108: ODC workers often push or pull data to servers while colocated workers concurrently perform computations, making it essential to minimize server interference. Communication primitives must also support ODC’s on-demand nature, where workers control the flow and servers cannot anticipate requests.
L109: Existing message-based libraries like MPI (cite69†Gabriel et al., 2004 ) and NCCL(cite43†NVIDIA, ) require explicit, ordered participation from both sender and receiver, making them neither transparent nor on-demand, and prone to deadlocks if not carefully scheduled.
L110: ODC instead leverages native RDMA-based interfaces: CUDA IPC (cite70†NVIDIA, ) for intra-node and NVSHMEM (cite71†NVIDIA, ) for inter-node communication. RDMA enables transparent data transfers without active server involvement, except for gradient accumulation, which is handled by a lightweight daemon.
L111: The communication kernel is built on Triton-Distributed (cite72†Zheng et al., 2025 ), a Triton (cite73†Tillet et al., 2019 ) wrapper that exposes RDMA functionalities directly in Python Triton kernels, eliminating the need for low-level CUDA C code. We put more implementation details at Appendix cite25†B , and will open-source our implementation for community usage.
L112: Integrating ODC into FSDP is straightforward: it only requires replacing collective communication calls with ODC primitives and retrieving accumulated gradients at the minibatch end.
L113: ## 4 Simplified Load Balancing with ODC
L114: Due to the variation in sequence lengths, a naive padding strategy significantly suffers from computation waste. To mitigate this, cite49†Krell et al. (2021) introduced the strategy of sequence packing, which concatenates multiple samples into a single sequence with appropriate attention masks, improving utilization and balancing workload across microbatches.
L115: This approach has been broadly adopted and extended by subsequent work (cite46†Bai et al., 2024 ; cite50†Kundu et al., 2024 ; cite51†Yao et al., 2025 ; cite52†Wang et al., 2025 ), with efficient support in modern libraries like FlashAttention (cite74†Dao et al., 2022 ; cite75†Dao, 2023 ).
L116: However, existing sequence packing methods operate at the microbatch level, which faces several fundamental limitations under FSDP. First, the size of a microbatch is bounded by device memory, limiting the number of samples per microbatch and leaving substantial variance in workload across devices.
L117: This effect is amplified in long-sequence training regimes, such as LongAlign (cite46†Bai et al., 2024 ) and RL for LLM reasoning (cite45†Guo et al., 2025 ), where extended contexts further constrain per-device capacity. Second, for a sample of sequence length $s$, activation memory typically scales as $O(s)$ while runtime scales as $O(s^{2})$ (e.g., due to attention), creating a fundamental mismatch between memory and compute. Consequently, compute alignment can be infeasible under memory constraints.
L118: For instance, if a microbatch contains a single sample at the maximum sequence length, no feasible packing of shorter samples can match its runtime.
L119: By replacing collective operations with ODC, our approach decouples the execution of microbatches across devices. This eliminates synchronization barriers inherent in FSDP and removes the implicit requirement for a uniform number of microbatches per device. This insight allows for a significant simplification of workload balancing strategy. Specifically, our strategy shifts the balancing objective from the fine-grained microbatch level to the coarser minibatch level.
L120: We first partition the global set of training samples across devices with the sole goal of balancing the total computational load. Subsequently, each device independently packs its local subset of samples into microbatches, governed only by its local memory constraints. This shift in granularity not only simplifies the packing algorithm, but also achieves superior load balancing by operating on a larger, less constrained set of samples. We leave the detailed packing algorithms in Appendix cite26†C .
L121: ## 5 Evaluations
L122: ### 5.1 Setup
L123: We evaluate ODC on two major LLM post-training tasks: SFT and RL. For SFT, we use a) LongAlign (cite46†Bai et al., 2024 ), a dataset for extending LLM context windows, and b) open-source trajectories from SWE-Smith (cite47†Yang et al., 2025 ), an agent model for software engineering tasks released by the SWE-Bench team (cite76†Jimenez et al., 2023 ).
L124: For RL, we run GRPO (cite45†Guo et al., 2025 ; cite77†Liu et al., 2025 ) implemented in verl (cite58†Sheng et al., 2025 ) on AIME prompts (cite78†Li et al., 2024 ), which includes problems from Olympiad-level math contest. Notably, we only record the model training time in RL, ignoring forward-only parts like actor rollout. The sequence length distributions of these datasets are shown in Figure cite79†7 .
L125: Figure 7: Sequence length distributions of evaluation datasets.
L126: We evaluate ODC on the DeepSeek-R1-Distill-Qwen family of models (cite80†Team, 2024 ; cite45†Guo et al., 2025 ), with varying size from 1.5B to 32B. The models are trained on up to 32 NVIDIA A100 80G GPUs, with NVSwitch for intra-node communication and RoCE RDMA (800 Gbps per node) for inter-node communication. Notably, for RL experiment we run only up to 14B model using 16 GPUs, as the inference time would be too long for a 32B model.
L127: Additionally, we validate the correctness of ODC by verifying the training convergency in Appendix cite32†F .
L128: Each method in our evaluation is a combination of communication scheme and load balancing algorithms. For communication scheme, we have a) Collective - baseline using collective all-gather and reduce-scatter; b) ODC - our approach introduced in Section cite10†3 ; For load balance algorithms, we include a) LocalSort - adapted from cite46†Bai et al. (2024) ; within each device’s minibatch, sequences are sorted by length but not packed.
L129: b) LB-Micro - a heuristic-based packing baseline designed to minimize workload imbalance across devices within the same microbatch. In RL experiments, we show that it is substantially faster than the native implementation in verl (cite58†Sheng et al., 2025 ), underscoring its effectiveness as a strong baseline. c) LB-Mini - our algorithm introduced in Section cite13†4 , which balances workload at the minibatch level.
L130: As LB-Mini can produce different number of microbatches for different devices, it applies only to ODC. Detailed implementations can be found in Appendix cite26†C . Unless otherwise specified, the maximum number of tokens in a microbatch is constrained by the maximum sequence length of a single sample in the dataset.
L131: ### 5.2 Main Results
L132: Figure 8: Samples per second on SFT datasets (LongAlign and SWE-Smith) across different model scales and minibatch sizes. ODC consistently improves throughput over Collectives in both un-packed (LocalSort) and packed (LB-Micro, LB-Mini) scenarios. Figure 9: Samples per second on RL with AIME prompts. In addition to the methods in Section cite15†5.1 , we also evaluate the default load balancing algorithm in verl, denoted as Native.
L133: LB-Micro is substantially faster than Native, underscoring its effectiveness as a strong baseline.
L134: Figure cite81†8 presents the evaluation results on SFT tasks. ODC consistently improves throughput over the collective baseline in both unpacked (LocalSort) and packed (LB-Micro, LB-Mini) settings, with the most pronounced gains observed under packing, reaching up to a 36% speedup. All methods perform similarly when the minibatch size is one, since in this case ODC synchronizes after every sample, just like collective.
L135: Figure cite82†9 shows in RL tasks ODC achieves up to 10% speedup over collective baseline, although the gains are less pronounced than in SFT. This is primarily due to: a) implementation constraints in verl, which require identical numbers of samples per device and thus limit the effectiveness of LB-Mini.
L136: While relaxing this constraint is feasible, we did not do so, as the current solution is easier to integrate; and b) a less long-tailed sequence length distribution compared to SFT datasets (Figure cite79†7 ).
L137: At small minibatch sizes, LB-Mini often outperforms LB-Micro. This reflects the benefits of its minibatch-level balancing, which permits devices to process different numbers of microbatches. As the minibatch size increases, however, LB-Micro has more flexibility to balance workloads effectively, which narrows the performance gap between the two methods. The detailed timing data as well as bubble rate is reported in Appendix cite33†G .
L138: ### 5.3 Parametric Study
L139: The effectiveness of ODC compared to collectives depends on several factors: a) Minibatch size: the number of samples per minibatch per device; b) Max length: the maximum sequence length in the dataset; to control this factor while maintaining the overall distribution, we adjust each sample by uniformly truncating or repeating tokens at a fixed ratio; c) Packing ratio: the maximum number of tokens allowed in a microbatch divided by the max sequence length (e.g., with a max sequence length of 16K and packing ratio of 2, a microbatch may contain up to 32K tokens); d) Devices: the total number of devices.
L140: To isolate the impact of each factor, we adopt a controlled methodology: starting from a fixed golden setting (Table cite83†1 ), we vary one factor at a time while holding others constant.
L141: As shown in Figure cite84†10 , the acceleration ratio peaks at moderate minibatch sizes before declining as larger batches give the baseline more flexibility; it increases with sequence length, since longer sequences amplify the quadratic compute cost and exacerbate imbalance; it decreases with packing ratio, which improves the baseline’s packing efficiency; and it grows with the number of devices, as more devices introduce greater heterogeneity.
L142: Model  | Dataset  | minibatch Size  | Devices  | Packing Ratio
L143: --- | --- | --- | --- | ---
L144: 1.5B  | LongAlign (Max 64K)  | 4  | 8  | 1
L145: Table 1: Golden setting for the parametric study. Each experiment varies at most one factor. Figure 10: Acceleration ratio of ODC compared to collective with LB-Micro in parametric study.
L146: ### 5.4 Benchmark on Communication Primitives
L147: 
L148: Figure 11: Benchmarking communication primitives against collectives. Within a node, ODC has a comparable performance with collective. But significantly slower than collective cross node.
L149: We compare the bandwidth of ODC primitives (gather and scatter-accumulate) against collectives (all-gather and reduce-scatter) in NCCL. For fairness, ODC primitives are launched synchronously: each device issues operations in the same order, with barriers inserted before and after each primitive. Results are shown in Figure cite85†11 . Within a single node (up to 8 devices), ODC achieves bandwidth comparable to collective.
L150: However, once communication spans multiple nodes, ODC lags significantly behind collective. We leave more discussion and how to mitigate this inter-node inefficiency in Section cite19†6 .
L151: ## 6 Discussion
L152: ### 6.1 Challenges on Inter-node Communication Efficiency
L153: Collective primitives are often highly optimized by exploiting hierarchical interconnects in multi-node settings. For example, an all-gather operation might first perform an inter-node broadcast followed by an intra-node broadcast to minimize costly inter-node traffic. ODC does not increase communication volume, but changes the topology: it uses point-to-point RDMA and thus forgoes these hierarchical optimizations (see Appendix cite30†D ).
L154: However, we argue that larger DP scale typically amplifies straggler effects under imbalance, increasing the benefit of ODC’s decoupled progress (see Figure cite84†10 ). Furthermore, several ways can effectively mitigate this communicate overhead.
L155: Overlapping Communication with Computation. ODC retains the standard FSDP optimization of overlapping communication with computation. This is particularly effective because communication volume per microbatch is constant with sequence length ($s$), whereas computation scales as $O(s^{2})$. For long sequences, the large computational cost effectively hides the communication latency.
L156: Consequently, despite using a non-hierarchical communication pattern, ODC shows no significant slowdown in our long-context evaluations (see Section cite16†5.2 ).
L157: Hybrid Sharding. When the tokens per microbatch is too small to hide communication costs, hybrid sharding provides an effective solution. Similar to ZeRO++ (cite86†Wang et al., 2024 ), parameters and gradients are sharded only within a node, while optimizer states remain sharded across nodes. This design eliminates cross-node parameter gather and gradient scatter-accumulate, at the cost of higher per-node memory usage, which is a manageable trade-off given that activation memory requirements are lower.
L158: As shown in Appendix cite31†E , this strategy effectively mitigates ODC’s additional overhead.
L159: ### 6.2 Future Work
L160: 
L161: ODC is an initial effort toward adapting PS to modern sharded DP. We believe this is a foundational step that opens several promising directions for future research.
L162: ODC-specific Optimizations While our current ODC implementation uses direct point-to-point communication, its communication graph can be further optimized. For instance, a device could fetch a parameter shard from a peer on the same node that has already cached it, effectively creating a hierarchical communication path similar to topology-aware collectives.
L163: Relaxing Synchronization Guarantees Our current design intentionally preserves a synchronous update at the minibatch boundary to maintain identical training semantics. However, this barrier could be relaxed. Extending ODC to support classic asynchronous SGD schemes (cite87†Recht et al., 2011 ), such as bounded-staleness updates (cite88†Chen et al., 2016 ; cite89†Ho et al., 2013 ), could further reduce idle time and improve hardware utilization, particularly in highly heterogeneous environments.
L164: This would, however, require a careful analysis of the convergence implications for LLM training.
L165: Elasticity and Fault Tolerance A significant advantage of PS-style architectures is their natural support for elasticity and fault tolerance (cite39†Dean et al., 2012 ; cite40†Li et al., 2014 ). Collective-based systems, in contrast, are notoriously brittle and difficult to resize (cite68†Jiang et al., 2020 ; cite90†Narayanan et al., 2021 ; cite91†Duan et al., 2024 ). Integrating these capabilities into ODC would improve the resilience and flexibility of large-scale, long-running LLM training jobs.
L166: ## 7 Conclusion
L167: 
L168: This paper revisits PS and adapts its principles to solve a critical bottleneck in modern sharded DP training for LLM post-training. We identified that the per-layer all-gather and reduce-scatter collectives in FSDP create fine-grained synchronization barriers, which amplify the straggler effects caused by workload imbalance.
--------------------------------------------------------------------------------
Self-Distillation Enables Continual Learning (https://arxiv.org/html/2601.19897v1)
citeturn28102view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19897v1","lineno":180}); Total lines: 562
L137: We drop $\beta$ and $C$ since linear transformations of reward do not affect the optimal policy (cite88†Sutton et al., 1998 ). While this defines a trajectory-level reward, our model has an autoregressive structure. Therefore, we decompose the reward into token-level rewards $r_{t}$ via token-level probabilities. We define the instantaneous reward as the immediate log-probability change:
L140: and indeed for all $y$, we have $\sum_{t}r_{t}(y_{t}\,|\,y_{<t},x,c)=r(y,x,c)$. Finally, we demonstrate that optimizing the policy with respect to this reward is equivalent to the reverse-KL distillation used in our method. The policy gradient under the current policy $\pi_{k}$ is:
L141: 
L142:  | $$\nabla_{\theta}J(\pi_{k})=\mathbb{E}_{y\sim\pi_{k}}\left[r(y,x,c)\nabla_{\theta}\log\pi_{k}(y|x)\right]$$  |
L143: 
L144: Substituting our derived reward from Equation cite89†5 :
L145:  | $$\nabla_{\theta}J(\pi_{k})=\mathbb{E}_{y\sim\pi_{k}}\left[\log\frac{\pi(y|x,c)}{\pi_{k}(y|x)}\nabla_{\theta}\log\pi_{k}(y|x)\right]$$  |  | (6)
L146: 
L147: We observe that this is equivalent in expectation to the gradient of the reverse KL divergence $D_{\mathrm{KL}}(\pi_{k}(\cdot|x)\|\pi(\cdot|x,c))$ in Equation cite90†2 . Thus, our method can be viewed as an on-policy RL algorithm that maximizes rewards inferred by comparing the student’s current behavior to its own “wiser,” demonstration-aware counterpart.
L148: (a) SDFT
L149: 
L150: (b) SFT
L151: 
L152: Figure 3: In a challenging continual learning experiment, where one model is trained sequentially on three different tasks, SDFT is able to learn each one while retaining performance on the others. In contrast, SFT performance on each task drops once it starts learning the next one. Performance is linearly normalized such that 0 corresponds to the base model accuracy on each one of the tasks, and 1 to the maximum accuracy obtained across both algorithms.
L153: ### 3.2 Validating the ICL Assumption
L154: 
L155: The core hypothesis of SDFT can be seen as the assumption in Equation cite91†4 , which states that a model conditioned on an expert demonstration behaves like the (unknown) optimal policy for that task $\pi_{k+1}^{*}(y|x)\approx\pi(y|x,c)$ and therefore it can be a good teacher. The quality of this approximation depends on 2 conditions:
L156: 
L157:   1. 1.
L158: 
L159: Optimality: The teacher’s expected reward must match that of the unknown optimal policy:
L160:  | $$\mathbb{E}_{y\sim\pi(y|x,c)}[r(y,x)]\approx\mathbb{E}_{y\sim\pi_{k+1}^{*}}[r(y,x)]$$  |
L161: 
L162: In other words, samples drawn from the demonstration-conditioned policy should achieve near-maximal reward on the task.
L163: 
L164:   2. 2.
L165: 
L166: Minimal Deviation: Due to the trust-region regularization in Equation cite92†3 , the optimal policy $\pi_{k+1}^{*}(y|x)$ is the one closest to the current model among all the ones that maximize reward. Thus, we require:
L167:  | $$D_{\mathrm{KL}}\left(\pi(\cdot|x,c)||\pi_{k}(\cdot|x)\right)\approx D_{\mathrm{KL}}\left(\pi_{k+1}^{*}(\cdot|x)||\pi_{k}(\cdot|x)\right)$$  |
L168: 
L169: That is, among all policies that achieve optimal reward, the teacher should be close, in the KL sense, to the $\pi_{k}$.
L170: The second requirement, remaining close to the current policy, is crucial for practical viability. If the demonstration-conditioned teacher simply mimicked the example verbatim, it would deviate substantially from the base model, losing the benefits of on-policy learning. What makes the teacher valuable is that it produces new, task-appropriate behavior while remaining anchored to the base model.
L171: Moreover, prior work shows that distributions close to the pretrained distribution suffer significantly less catastrophic forgetting and better preserve general capabilities (cite55†Shenfeld et al., 2025 ; cite56†Chen et al., 2025 ).
L172: Empirical Validation. While we cannot verify these conditions theoretically, we evaluate each empirically. We use the Qwen-2.5-7B-Instruct model (cite93†Hui et al., 2024 ) as the base policy and the ToolAlpaca dataset (cite94†Tang et al., 2023 ). In this benchmark, the model receives a tool-API specification and a user request, and must identify the correct tool call. Without demonstrations, the base model solves only 42% of examples.
L173: When provided with the appropriate demonstration $c$ for each prompt $x$, the teacher achieves a 100% success rate. To further test reward proximity, we manually inspected 50 teacher reasoning traces. In all cases, not only were the final tool calls correct, but the intermediate chain-of-thought was valid and semantically grounded. This suggests that the teacher is reconstructing a correct reasoning process rather than merely copying the expert output.
L174: These observations provide evidence for the first requirement, that the demonstration-conditioned model behaves as an optimal policy.
L175: To verify the second requirement, we measure the KL divergence to the base policy $D_{\mathrm{KL}}(\pi\|\pi_{0})$ as a proxy for the distance to the policy during training $\pi_{k}$. We compare this divergence for both the SFT model trained on demonstrations and the demonstration-conditioned teacher. As shown in Figure cite95†2 (right panel), the SFT model deviates substantially from the base model (1.26 nats), whereas the teacher remains significantly closer (0.68 nats)—nearly half the divergence.
L176: This validates that the teacher produces high-quality outputs while maintaining proximity to the base policy, precisely the balance required by the trust-region formulation.
L177: ## 4 Experiments
L178: ### 4.1 Experimental Setting
L179: 
L180: We evaluate our method in two settings that reflect common forms of post-training adaptation: Skill Learning and Knowledge Acquisition. These correspond to improving performance on a new task, and integrating novel factual information into a pretrained model.
L181: In Skill Learning, we study whether a pretrained LLM with broad capabilities can acquire a new, narrowly defined skill without degrading its existing abilities. We choose to experiment with tasks the models had not been explicitly fine-tuned on (unlike Math or Coding) to show the benefits of continual learning. Therefore, we test our method on three domains:
L182: 
L183:   * •
L184: 
L185: Science Q&A: Undergraduate-level scientific reasoning, using the Chemistry L-3 subset of SciKnowEval (cite96†Feng et al., 2024 ).
L186: 
L187:   * •
L188: Tool Use: Mapping a tool-API specification and user request to the correct tool call, using ToolAlpaca (cite94†Tang et al., 2023 ).
L189: 
L190:   * •
L191: 
L192: Medical: Clinical reasoning questions, with training data from stage 1 of the HuatuoGPT-o1 pipeline and evaluation from stage 2 (cite97†Chen et al., 2024 ).
L193: In Knowledge Acquisition, the objective is different: the model must integrate genuinely new factual content not present in its pretraining data. We construct a corpus of Wikipedia articles describing natural disasters that occurred in 2025 (after the training knowledge cutoff), totaling approximately 200K tokens. Following cite98†Mecklenburg et al. (2024) , we generate question–answer pairs about these articles, yielding an SFT dataset roughly 5× larger than the source corpus.
L194: These questions probe factual content such as “which regions were affected by the 2025 Myanmar earthquake?”.
L195: This setting tests whether the model can absorb newly injected knowledge rather than merely improving skills it already has.
L196: #### Evaluation.
L197: 
L198: For each task, we evaluate along two primary axes:
L199: 
L200:   * •
L201: 
L202: In-Distribution Accuracy: Accuracy on held-out test data for the newly introduced task. For Knowledge Acquisition, we use two variants: (1) All details correct (Strict Accuracy). (2) The answer contains correct information and no incorrect statements (Lenient Accuracy).
L203: 
L204:   * •
L205: Previous Capabilities: Performance on a suite of established benchmarks that probe general reasoning and world knowledge: HellaSwag (cite99†Zellers et al., 2019 ), TruthfulQA (cite100†Lin et al., 2021 ), MMLU (cite101†Hendrycks et al., 2020 ), IFEval (cite102†Zhou et al., 2023 ), Winogrande (cite103†Sakaguchi et al., 2021 ), and HumanEval (cite104†Chen et al., 2021 ). We report the average performance across these datasets as a measure of catastrophic forgetting.
L206: For the Knowledge Acquisition setting, we include a third metric:
L207: 
L208:   * •
L209: 
L210: Out-of-Distribution Accuracy: “Indirect” questions whose answers depend on the injected knowledge but do not directly reference it (e.g., “Which countries required international humanitarian aid in 2025?”). This measures whether the new information has been properly integrated into the model’s internal memory rather than memorized in a narrow form.
L211: Figure 4: Performance trade-offs between new task accuracy and retention of prior capabilities. Each point represents a trained model, with the top-right indicating ideal performance (high accuracy on both new and previous tasks). SDFT consistently achieves superior Pareto efficiency compared to baselines across all three skill learning tasks.
L212: #### Baselines.
L213: 
L214: In the Skill Learning setting, we compare our method to standard SFT and to DFT (cite105†Wu et al., 2025b ), which uses importance sampling to treat the offline dataset as on-policy samples. We also include the recently proposed ”Re-invocation” method (cite106†Lu & Lab, 2025 ), which performs additional on-policy distillation from the base policy on general-purpose prompts after SFT to restore prior capabilities.
L215: In the Knowledge Acquisition setting, we compare our method to CPT (Continual Pre-Training), which trains directly on the text corpus using next token prediction loss and SFT, which trains on the question-answer pairs. In addition, we also compare with pure ICL methods. Because the full corpus exceeds the model’s context window, we evaluate RAG with an oracle retriever that always provides the correct article for each question.
L216: Unless otherwise noted, all experiments were performed on the Qwen2.5-7B-Instruct model. For each baseline, we perform a hyperparameter sweep and report results for the model achieving the highest validation performance on the target task. Full datasets, hyperparameters, and training protocols are provided in Appendix cite42†B .
L217: ### 4.2 On-policy learning leads to better generalization
L218: 
L219: Prior work has shown that on policy learning achieves better in-distribution performance than SFT (cite64†Ross et al., 2011 ), as well as superior out-of-distribution generalization (cite67†Chu et al., 2025 ). We investigate whether these advantages also arise in our on-policy distillation framework. For that, we measure performance on test set on all our training tasks, as well as OOD generalization in the Knowledge Acquisition setting.
L220: #### Results.
L221: Results for Skill Learning, as shown in Figure cite107†4 , indicate that our method achieves higher new-task accuracy than SFT, which represents better in-distribution generalization. We attribute these gains to the fact that off-policy learning trains only on expert-induced trajectories; errors at test-time can push the policy into unseen states, causing compounding errors.
L222: On-policy imitation learning avoids this mismatch by training on the state distribution induced by the learned policy itself (cite64†Ross et al., 2011 ).
L223:  | Accuracy  | Accuracy  | OOD
L224:  | (strict)  | (lenient)  | Accuracy
L225: Base  | 0  | 0  | 0
L226: Oracle RAG  | 91  | 100  | 100
L227: CPT  | 9  | 37  | 7
L228: SFT  | 80  | 95  | 80
L229: SDFT (Ours)  | 89  | 100  | 98
L230: Table 1: SDFT effectively integrates new factual knowledge, thus achieving better accuracy both in- and out-of-distribution.
L231: The results for Knowledge Acquisition appear in Table cite108†1 . Since the new knowledge was not included in the base model’s training, it cannot answer any of the questions correctly. Consistent with earlier observations (cite98†Mecklenburg et al., 2024 ), continual pretraining performs poorly. SFT on questions improves performance substantially but still lags behind our SDFT. On strict accuracy, it reaches 80% while our on-policy method achieves 89% and nearly closes the gap to the oracle RAG model.
L232: The advantage becomes even clearer on out-of-distribution questions, where our method achieves close to perfect accuracy, while SFT’s performance remains low. This disparity underscores a key limitation of SFT: it teaches the model to reproduce specific answers but does not reliably incorporate the underlying facts into the model’s broader knowledge base.
L233: Finally, with on-policy RL there is a concern for superficial improvements through entropy reduction rather than acquisition of new behaviors (cite109†Yue et al., 2025 ; cite110†Wu et al., 2025a ). To ensure our gains are not merely due to distributional sharpening, we evaluate pass@$k$ for $k$ up to 128 in the Skill Learning Setting. As shown in Figure cite111†5 (right), the performance gains over both the base model and SFT persist uniformly across all $k$.
L234: This indicates that the improvements reflect genuine skill acquisition rather than entropy collapse.
L235: ### 4.3 Learning without forgetting
L236: 
L237: A central claim of SDFT is that, due to its on-policy nature, it can acquire new skills while mitigating catastrophic forgetting. To test this, we perform the following experiments:
L238: 
L239:   1. 1.
L240: 
L241: Single Task Learning. A convenient case study for continual learning is fine-tuning a model on a single task. Using the Skill Learning setting, we compare the broad capabilities of our models before and after training on each task.
L242: 
L243:   2. 2.
L244: Multi-Task Continual Learning. We investigate a more complex continual learning experiment in which a single model is trained sequentially on each task. The goal here is to measure catastrophic forgetting over longer training and to see whether the model retains the capabilities it learned at each stage of training.
L245: 
L246: .
L247: #### Results.
L248: The results for single-task training, presented in Figure cite107†4 , show that our method is the only approach to improve performance on the new task without significant degradation in prior capabilities. In contrast, standard SFT produces substantial catastrophic forgetting across all evaluated benchmarks. Augmenting SFT with the “re-invoke” procedure partially restores lost abilities but does not recover the base model’s full capabilities.
L249: DFT, which performs approximate on-policy updates, exhibits reduced forgetting relative to SFT but still results in noticeable degradation. For the breakdown of the score over prior tasks, see Table cite112†5 .
L250: We now turn to the more challenging setting of long-horizon continual learning, where a single model is trained sequentially on all three skills. Figure cite113†3 shows that SDFT enables stable accumulation of skills over time. As training progresses, the model improves on each newly introduced task while maintaining performance on previously learned ones.
L251: In contrast, SFT exhibits severe interference—performance on earlier skills rapidly degrades once training shifts to a new task, resulting in oscillatory behavior rather than cumulative learning. These results demonstrate that SDFT supports true continual learning, allowing a single model to incrementally acquire multiple skills without catastrophic forgetting.
L252: ### 4.4 Effect of model size
L253: 
L254: Figure 5: (Left) SDFT benefits from model scale. Performance gap between SDFT and SFT on the Science Q&A task increases with model size, as larger models have stronger in-context learning capabilities. (Right) SDFT improves pass@k across various k, indicating genuine skill acquisition rather than entropy collapse.
L255: Our method relies fundamentally on the model’s in-context learning ability. The teacher signal comes from the model conditioned on demonstrations, and the quality of that signal depends on how well the model can interpret and extrapolate from those examples. This suggests that larger models, whose in-context learning abilities are known to improve with scale (cite66†Brown et al., 2020 ), should yield stronger teacher policies and therefore better SDFT updates.
L256: To test this hypothesis, we conduct a scaling experiment using several sizes from the Qwen 2.5 family (cite93†Hui et al., 2024 ), evaluating each on the Science Q&A task.
L257: Figure cite111†5 (left) illustrates a clear trend. At small scales, such as the 3B variant, the model’s in-context learning is too weak to provide meaningful teacher guidance, and performance lags behind standard SFT. However, as we increase the size, the gains from our method grow consistently. The 7B model achieves a four-point improvement over SFT, and the 14B model widens the margin to seven points.

