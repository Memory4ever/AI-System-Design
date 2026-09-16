# 2026-05-08 V3 最终 closure 修复（2026-09-15）

## 角色、范围与结论

本文件是修复作者记录，不是独立终审。修复严格限定在上一轮 fresh-context reviewer 确认的 17 个 closure false negative、`2605.05219` 的 Evidence 文本缺陷，以及与这些反例共享八类错误模式的有界同层反查；没有扩展来源、日期或 raw identity，也没有把 491 个 closure 全部升级为候选。

修复后的 canonical 账本为：

- raw unique Source Family：619；
- retained：128；
- pre-denominator closure：491；
- 守恒：`619 = 128 + 491`；
- 22 个重开项全部完成 exact-v1 深入审阅，`Review Pending = 0`；
- Books：49 项此前已经 Applied；本轮 16 项 `Integrate — Root writeback required`，另有 63 项 `No Change — Existing Coverage`；
- blocked / disputed / withdrawn：0 / 0 / 0；
- 状态仍为 `Ongoing`：需要 root 串行写回 16 项 Books，再由未参与本轮修复与写回的 reviewer 独立签署。

## 有界 closure audit

有界反查只覆盖 reviewer 指定的八类同层错误：quantization×runtime controller、RAG/Agent security 与 termination、uncertainty/intervention、RLVR/post-training credit、Transformer identity injection、latent generation/RAG、multi-Agent coordination、LLM privacy/attribution。

共复核 59 个同层 closure。除 reviewer 已点名的 17 项外，新增确认 5 个 false negative：`2605.05592`、`2605.05643`、`2605.05769`、`2605.06111`、`2605.06219`。其余 54 项在题名、完整摘要、ROADMAP owner 与相邻命题对照后仍只支持单任务方法、局部指标或当前 Books 已有边界，不足以改变长期 AI System 设计；因此保持 family-specific pre-denominator closure。检查到共享错误模式边界即停止，没有重扫全量来源。

## 22 个重开项的最终处置

| arXiv | Score V2 | Owner | 最终处置 |
| --- | ---: | --- | --- |
| [2605.05561](https://arxiv.org/html/2605.05561v1) | 2+2+2=6 | `INFER-SCHEDULING` | Integrate — Root writeback required |
| [2605.05592](https://arxiv.org/html/2605.05592v1) | 3+2+3=8 | `PLATFORM-EVALUATION-SYSTEM` | Integrate — Root writeback required |
| [2605.05632](https://arxiv.org/html/2605.05632v1) | 3+2+2=7 | `PLATFORM-SECURITY` | Integrate — Root writeback required |
| [2605.05643](https://arxiv.org/html/2605.05643v1) | 2+2+2=6 | `AGENT-RAG` | Integrate — Root writeback required |
| [2605.05737](https://arxiv.org/html/2605.05737v1) | 3+3+3=9 | `AGENT-WORKFLOW` | No Change — Existing Coverage |
| [2605.05769](https://arxiv.org/html/2605.05769v1) | 3+2+2=7 | `TRAIN-LORA` | Integrate — Root writeback required |
| [2605.05777](https://arxiv.org/html/2605.05777v1) | 2+2+2=6 | `PLATFORM-EVALUATION-SYSTEM` | No Change — Existing Coverage |
| [2605.05846](https://arxiv.org/html/2605.05846v1) | 3+3+3=9 | `PLATFORM-SECURITY` | Integrate — Root writeback required |
| [2605.05953](https://arxiv.org/html/2605.05953v1) | 3+2+2=7 | `PLATFORM-EVALUATION-SYSTEM` | Integrate — Root writeback required |
| [2605.05965](https://arxiv.org/html/2605.05965v1) | 3+2+2=7 | `TRAIN-GRPO` | Integrate — Root writeback required |
| [2605.06111](https://arxiv.org/html/2605.06111v1) | 3+2+2=7 | `TRAIN-GRPO` | Integrate — Root writeback required |
| [2605.06166](https://arxiv.org/html/2605.06166v1) | 2+2+2=6 | `TRAIN-SFT` | Integrate — Root writeback required |
| [2605.06188](https://arxiv.org/html/2605.06188v1) | 3+2+3=8 | `TRAIN-GRPO` | Integrate — Root writeback required |
| [2605.06216](https://arxiv.org/html/2605.06216v1) | 3+1+3=7 | `MODEL-EMBEDDING` | Integrate — Root writeback required |
| [2605.06219](https://arxiv.org/html/2605.06219v1) | 3+2+2=7 | `PLATFORM-EVALUATION-SYSTEM` | No Change — Existing Coverage |
| [2605.06232](https://arxiv.org/html/2605.06232v1) | 3+2+3=8 | `PLATFORM-SECURITY` | No Change — Existing Coverage |
| [2605.06285](https://arxiv.org/html/2605.06285v1) | 3+2+3=8 | `AGENT-RAG` | Integrate — Root writeback required |
| [2605.06320](https://arxiv.org/html/2605.06320v1) | 3+2+2=7 | `AGENT-MULTI-AGENT` | No Change — Existing Coverage |
| [2605.06423](https://arxiv.org/html/2605.06423v1) | 3+2+2=7 | `PLATFORM-SECURITY` | No Change — Existing Coverage |
| [2605.06548](https://arxiv.org/pdf/2605.06548v1) | 3+2+3=8 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Integrate — Root writeback required |
| [2605.06596](https://arxiv.org/html/2605.06596v1) | 3+2+2=7 | `PLATFORM-SECURITY` | Integrate — Root writeback required |
| [2605.06632](https://arxiv.org/html/2605.06632v1) | 3+2+2=7 | `TRAIN-SFT` | Integrate — Root writeback required |

## exact-v1 Evidence Review

### 2605.05561 — BitCal-TTS

- **Problem / mechanism：** 4-bit quantization 会扭曲 adaptive test-time compute 使用的 uncertainty 与 trace-stability signal；bit-conditioned rescaling、post-marker confirmation horizon 与在线 proxy 共同决定 halting。
- **Evaluation：** greedy 4-bit Qwen2.5-Instruct 7B/14B，GSM8K 小型子集，token cap 512；作者同时报告 Wilson 95% CI 与样本统计功效不足。
- **Non-proof / disposition：** 不证明其他 precision、sampler、任务或生产 SLO；但它改变 precision 与 runtime controller 的身份关系，进入 `INFER-SCHEDULING` 写回队列。

### 2605.05592 — binary voting structure

- **Problem / mechanism：** 在 exchangeable repeated correctness 的 latent mixture 下，多数投票曲线可以非单调甚至反复转向；完整 odd-budget curve 对应有符号 voting signature，而不是单一 competence。
- **Evaluation：** 主要是 de Finetti 表示与 signed Hausdorff moments 的理论结果；fixed-depth labels 只揭示有限前缀。
- **Non-proof / disposition：** 不覆盖非交换采样、开放答案聚类或任意 judge；但它改变 vote budget 的 Evaluation contract，进入 `PLATFORM-EVALUATION-SYSTEM` 队列。

### 2605.05632 — RAG poisoning across architectures

- **Problem / mechanism：** 四种 RAG architecture 对单文档 poisoning 的 failure path 不同；retrieval 命中之后，adversarial framing 主要在 content-reasoning stage 生效，contradiction detection 与 resolution 也必须分开。
- **Evaluation：** 921 个 Natural Questions、clean/naive/CorruptRAG-AK，四种架构。
- **Non-proof / disposition：** MADAM-RAG 是 reimplementation，judge 对 contradiction detection precision 约 48.5%，non-answer 也很高；进入 Security 队列，不外推通用 attack rate。

### 2605.05643 — text/graph bidirectional RAG

- **Problem / mechanism：** graph-to-text voting 重排文本证据，text-to-graph orphan bridging 从 search history 重开被 pruning 的 reasoning path；deferred node 必须保存 identity/provenance。
- **Evaluation：** 多个 multi-hop benchmark；摘要只给相对效果，没有完整运行条件。
- **Non-proof / disposition：** 不证明所有 corpus、graph freshness 或生产 latency；长期增量是 bidirectional evidence state，进入 `AGENT-RAG` 队列。

### 2605.05737 — ReFlect harness

- **Problem / mechanism：** deterministic wrapper 独立拥有 error detection 与 recovery，而不是让同一模型做无约束 self-critique。
- **Evaluation：** 六类 reasoning domain、六个模型，并给出 self-critique failure 与 harness gain；小模型可能无法填充结构化 state。
- **Non-proof / disposition：** 现有 Ch81 已在“Recovery 与 Verification 必须产生不同 Artifact”及 recovery/budget/commit 主线具体承载 verifier、recovery operator 与 fallback，因此 `No Change`。

### 2605.05769 — adaptive DP federated LoRA

- **Problem / mechanism：** 各层各轮独立选择 LoRA component，以 curvature-aware score 避免统一/固定 schedule 的 aggregation floor；selection 必须继承 privacy accountant。
- **Evaluation：** GLUE、SQuAD、CIFAR-100、Tiny-ImageNet，严格 DP budget 与 non-IID partition。
- **Non-proof / disposition：** 不覆盖恶意 client 或任意 DP mechanism；逐层逐轮 component control 尚未由 Ch30 承载，进入 `TRAIN-LORA` 队列。

### 2605.05777 — black-box uncertainty proxy

- **Problem / mechanism：** model-specific lightweight proxy 用 adversarial distillation 近似黑盒输出分布，再产生 uncertainty sensor，试图替代多采样。
- **Evaluation：** 作者报告约 1% target size 的 proxy 仍可量化 uncertainty，但摘要不提供足够 slice/漂移细节。
- **Non-proof / disposition：** proxy fidelity 不等于 truth；Ch66 已具体要求 raw score 经 deployment-slice calibration、drift 与 risk–coverage Gate 才能行动，因此 `No Change`。

### 2605.05846 — termination poisoning

- **Problem / mechanism：** 不可信 context 能劫持 progress/termination judgment；LoopTrap 按行为画像选择并迭代攻击。
- **Evaluation：** 8 个 Agent、60 个任务、10 种攻击，作者报告平均 3.57×、峰值 25× step amplification。
- **Non-proof / disposition：** 不证明开放生产系统发生率或防御充分性；但揭示 termination authority 不得与被污染 reasoning 共置，进入 `PLATFORM-SECURITY` 队列。

### 2605.05953 — anomaly-gated correction

- **Problem / mechanism：** probabilistic circuit 对 residual stream 做 tractable density estimation，只在 NLL anomaly 时触发 latent-density contrastive decoding，避免逐 token 无差别 correction。
- **Evaluation：** 四个 1B–8B 模型与四类 benchmark；作者报告 detection、TruthfulQA 与 preservation/corruption 指标。
- **Non-proof / disposition：** factual-manifold 假设、层选择与 calibration 不可外推；长期增量是 sensor 与 correction authority 分离，进入 Ch66 队列。

### 2605.05965 — selective eligibility trace

- **Problem / mechanism：** 用低熵 token mask 形成 sparse eligibility trace，替代把 trajectory advantage 均匀广播给所有 token。
- **Evaluation：** Qwen3 1.7B、4B、8B，比较 pass@16 与 sample/token efficiency。
- **Non-proof / disposition：** 低熵不等于因果贡献，也未覆盖异步 rollout；但改变 RLVR credit artifact，进入 `TRAIN-GRPO` 队列。

### 2605.06111 — utility-guided multi-task RL

- **Problem / mechanism：** task utility 同时驱动 hierarchical data scheduling 与 per-task KL calibration，二者共享训练状态而非分别调参。
- **Evaluation：** 两个 LLM、四类 code task；作者报告相对 specialist 和 MTRL baseline 的增益。
- **Non-proof / disposition：** utility 定义、任务集与训练成本不能外推；耦合 controller 是 Ch33 尚缺的长期机制，进入队列。

### 2605.06166 — dual data/parameter selection

- **Problem / mechanism：** 同一 validation objective 下，从 gradient interaction matrix 的行/列聚合共同产生 data utility 与 parameter importance，避免两个 selector 重复计算与漂移。
- **Evaluation：** 3B–9B LLM、matched budget 下比较 joint-constrained trade-off。
- **Non-proof / disposition：** 只是局部一/二阶 response surrogate，不证明全局 bilevel optimum；进入 `TRAIN-SFT` 队列。

### 2605.06188 — OPSD after RLVR

- **Problem / mechanism：** correct/incorrect rollout 分离后，OPSD 对 thinking-enabled reasoning 更像压缩正确轨迹，而不是纠正错误轨迹；pipeline 应条件化为 SFT→RLVR→OPSD。
- **Evaluation：** thinking-enabled 数学推理，分别训练 correct-only 与 incorrect-only groups。
- **Non-proof / disposition：** 不覆盖短输出或所有任务；但修正 post-training pipeline 位置，进入 `TRAIN-GRPO` 队列。

### 2605.06216 — layerwise token identity reinjection

- **Problem / mechanism：** EmbeddingMemory 用 K 个 context-free bank、depth-conditioned router 与 null bank 在每层重注入 token identity，针对 rare-token under-training 与 contextual collapse。
- **Evaluation：** exact-v1 给出理论论证和多个 LM/downstream 实验。
- **Non-proof / disposition：** 不证明所有表示失效来自单次注入，也缺大规模 serving 成本；改变 embedding 结构假设，进入 `MODEL-EMBEDDING` 队列。

### 2605.06219 — joint consistency aggregation

- **Problem / mechanism：** constrained Ising-type energy 同时消费 independent evaluation fields 与 pairwise judge interactions，并把 voting/weighted aggregation 视为特例。
- **Evaluation：** math/code benchmark、不同 judge、trace budget 和 generation setting；理论解释依赖 answer-level homogeneity。
- **Non-proof / disposition：** Ch66 “Per-verifier Outcome 与 Aggregation Rule 都属于 Evaluation Identity”以及 pairwise graph/calibration 主线已具体承载 per-item evidence、interaction graph 与 aggregation revision，因此 `No Change`。

### 2605.06232 — derived personal profiling

- **Problem / mechanism：** 从显式搜索、context inference 到跨源 aggregation，公开记录也可被组合成敏感 derived profile。
- **Evaluation：** IcebergExplorer 的受控现实案例报告时间、成本与 factual accuracy。
- **Non-proof / disposition：** 不能证明任意人群、搜索面或风险发生率；Ch72 已将 contextual/derived privacy、query budget 与最小暴露作为独立保护对象，因此 `No Change`。

### 2605.06285 — LatentRAG

- **Problem / mechanism：** 一次 forward 产生 latent thought/subquery tokens，并与 dense retriever 在 latent space 对齐；parallel decoder 只提供可见解释视图。
- **Evaluation：** 七个 benchmark，作者报告与显式 Agentic RAG 可比的任务结果及约 90% latency reduction。
- **Non-proof / disposition：** 硬件、backend、batch/concurrency/SLO 未完整披露，latent trace 不自动可审计；进入 `AGENT-RAG` 队列。

### 2605.06320 — adaptive coordination graph

- **Problem / mechanism：** team 共同维护带 dependency、assignment 与 progress 的 evolving coordination graph，在 partial observability 与 communication constraints 下动态分工。
- **Evaluation：** 多类协作任务与多个 base model，比较 token、wall-clock、communication、file conflict 与 accuracy。
- **Non-proof / disposition：** Ch82 “Coordination State 必须有显式 Owner 与 Commit Transition”及 authoritative dependency DAG 已完整承载 graph owner、ready set、commit/rebase 与 adaptive participation，因此 `No Change`。

### 2605.06423 — PopQuiz membership inference

- **Problem / mechanism：** 把目标训练记录转成 quiz-style multiple-choice queries，以黑盒回答推断 membership。
- **Evaluation：** 六个模型、四个数据集，并比较 instruction/filter/DP defense；作者报告 average ROC-AUC。
- **Non-proof / disposition：** 不等于法律归因或任意数据可恢复；Ch72 已要求 membership signal 绑定 sample identity、controls、query budget、低 FPR 与 defense boundary，因此 `No Change`。

### 2605.06548 — continuous latent diffusion language model

- **Problem / mechanism：** Text VAE 负责 text↔latent，block-causal DiT transport global semantic prior，conditional decoder 实现 local text，区别于 token-level observation denoising。
- **Evaluation：** 8 个 benchmark、matched ~2B AR/LLaDA baseline、至约 2000 EFLOPs scaling。
- **Non-proof / disposition：** 不证明更大规模、生产 latency、统一多模态或 likelihood/quality 普遍关系；改变生成 factorization，进入 Ch24 队列。

### 2605.06596 — federated client attribution

- **Problem / mechanism：** 成对 secure-aggregation subset queries 估计 client update，以 watermark detector 差分评分并跨轮 Stouffer aggregation。
- **Evaluation：** 作者设置中报告 100% TPR、0% FPR、6.3% overhead，并给出每轮 mutual-information bound。
- **Non-proof / disposition：** 不覆盖恶意 server/client、任意 watermark 或法律归因；改变 privacy/attribution 账本，进入 `PLATFORM-SECURITY` 队列。

### 2605.06632 — reversible SFT behavior carrier

- **Problem / mechanism：** LCDD 在 utility budget 下联合优化 routing mask 与 weights，将 SFT behavior 压进 sparse causal carrier；SFT-Eraser 通过 carrier-channel activation matching 的 soft prompt 做反转。
- **Evaluation：** safety、fixed-response、style behavior 与多个 model family；ablation 表明 standard SFT 上同一 trigger 不成立。
- **Non-proof / disposition：** 不证明任意行为可定位或反转无副作用；改变 SFT behavior locality/control，进入 `TRAIN-SFT` 队列。

## 2605.05219 Evidence 修复

原 Evidence 的 evaluation contract 是残句，并把已经写入 Ch45 的 `Integrate — Applied` 解释成“无需新增正文”。现修复为：

- **Method：** hybrid/recurrent model 只在稀疏 prefix positions 保存 exact recurrent state；部分 prefix hit 恢复最近 checkpoint，并 replay 缺失 suffix；checkpoint placement 由 overlap-depth distribution 上的 exact dynamic program 决定。
- **Evaluation contract：** 比较 dense per-token KV-prefix caching、无 recurrent-state reuse 与不同 sparse checkpoint placement；结论只在模型可精确抽取/恢复 recurrent state、请求前缀分布和论文实现范围内成立。缓存收益必须同时绑定 checkpoint density、prefix-overlap distribution、replay cost、state size 与 backend。
- **Non-proof：** 不证明任意 hybrid/recurrent architecture 都可暴露 exact state，不覆盖 state restore 误差、分布漂移或生产并发下的通用收益。
- **Disposition：** `Integrate — Applied → INFER-KV-CACHE`。Ch45 已拥有 sparse checkpoint、nearest restore 与 suffix replay 的机制正文，因此本轮不重复写入，但保留 Applied 状态。

## Books writeback 与 Gate

16 项结构化写回要求见 [BOOKS_WRITEBACK_QUEUE_FINAL_CLOSURE_REPAIR.json](BOOKS_WRITEBACK_QUEUE_FINAL_CLOSURE_REPAIR.json)。队列为 root 串行写共享 Books 使用；修复作者没有直接修改 Books。

当前 Gate：

- Coverage：Closed with declared source limitations；
- Candidate Denominator：Author-repaired，等待独立复核；
- Evidence：128/128 complete，等待独立复核；
- Books：49 Applied + 16 root writeback required + 63 No Change；
- Completion：Ongoing；
- Final independent signoff：false。

