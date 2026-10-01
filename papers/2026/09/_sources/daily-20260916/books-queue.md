# Daily 2026-09-16 Books queue

本队列只记录已经完成 Evidence Review、且与现有具体论点相比仍有长期语义增量的材料。原有 12 项、首轮返修新增的 `2609.16193`、`2609.16754`、`2609.17483`，以及本次有限返修新增的 21 项，均已按唯一 owner 合并写入；另有 11 项由现有正文充分承载。新增 21 个 source-family marker 均为唯一命中，并已通过未参与作者筛选、有限返修或 Books 写入的 reviewer 终审。

## 有限返修新增：已写入，独立复核通过

| Source Family | Owner / 章节 | 插入锚点与长期语义增量 | 证据边界；Trade-off / failure / fallback |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2609-16053` | `AGENT-MEMORY` Ch77 | 在静态写入/更新生命周期之后补充：retrieval feedback 只能提出局部 memory mutation；reconsolidation 须经 provenance、一致性与回归验证后提交。 | 两个 long-memory benchmark 与 LLM judge；图漂移、错误合并和 poisoning 是新增失败。失败时保留 immutable raw source、append-only event 与可重建索引。 |
| `SF-2026-ARXIV-2609-16055` | `MODEL-LONG-CONTEXT` Ch22 | 在 recurrent-state ownership 后补充：内部低维 state 可控制 evidence activation 与 stopping，但它只是控制传感器，不拥有事实真值。 | 三个 text backbone 与一个 VLM family；误判会造成漏读或过早停止。回退外部 bounded schedule、显式 history 或完整上下文。 |
| `SF-2026-ARXIV-2609-16056` | `MULTIMODAL-EMBODIED-VLA` Ch26 | 在 controller hierarchy/action gate 处区分 verifier、enforcer、learner：三种 placement 分别把 precondition authority 放在推理、训练加推理或参数中。 | MiniGrid、Fetch、taxi routing 且前提由设计者提供；显式 authority/审计性与策略灵活性互换。未知前提时回退显式 verifier 与安全 envelope。 |
| `SF-2026-ARXIV-2609-16057` | `AGENT-PLATFORM` Ch84 | 在 trajectory-to-Skill compilation 主线补充：verified execution 只能成为候选输入，派生 policy 必须绑定 applicability、reliability、revision 与 fallback，不能只保存 prompt 片段。 | ComfyUI/视觉生成任务；自我练习会积累错误，跨环境可移植性未证明。回退冻结 policy snapshot、人工批准或重新规划。 |
| `SF-2026-ARXIV-2609-16161` | `INFER-GPU-MEMORY` Ch54 | 在 flash/storage hierarchy 后补充：compute-in-flash 的整数执行、写寿命与带宽约束会迫使 KV 采用静态 dictionary 加 sparse coefficient，而非照搬 HBM cache。 | 两个 7–8B model、LongBench 和 analytical device model；dictionary error、双副本与 prefill 缺口存在。回退 HBM/host offload 或完整 KV。 |
| `SF-2026-ARXIV-2609-16245` | `AGENT-PLANNING` Ch79 | 在 planning-mode controller 处补充：低维内部状态可提出探索、执行、复核模式切换，但不能拥有答案正确性或 commit authority。 | 冻结 Kimi 2.6 和有限 research trajectories；state detector 可被误用或模型特化。回退显式 workflow、预算和外部 verifier。 |
| `SF-2026-ARXIV-2609-16331` | `MULTIMODAL-EMBODIED-VLA` Ch26 | 在 skill-to-controller interface 处补充：skill schema 应先声明执行所需 geometric contract，再由 perception 实例化 geometry 并绑定 motion template。 | 单一双臂平台和预定义 skill vocabulary；contract/grounding/collision gap 未消除。回退新 demo、fine-tune 或人工规划。 |
| `SF-2026-ARXIV-2609-16382` | `MODEL-MULTI-HEAD-ATTENTION` Ch15 | 在平均 attention 与上下文计算的边界处补充：mean field 只能解释平均表征传播，deviation 才描述 context-specific routing/value computation；统计解释不等于因果证明。 | 若干 corpus/model，Llama 需单独处理；统计平均可能掩盖个例。回退真实 activation measurement 与 ablation。 |
| `SF-2026-ARXIV-2609-16391` | `AGENT-RAG` Ch76 | 在 embedding deployment identity 处补充：PTQ policy 必须绑定 family、bit width、group size、module 与 retrieval task；reconstruction error 只能做同一设置内筛选，不能直接充当 allocator。 | 五 checkpoints、四 family、三个 corpus，未测完整 MTEB/整数 Kernel；失败是 retrieval collapse。回退 INT4/FP、混合精度或带 OOD gate 的 in-domain distilled student。 |
| `SF-2026-ARXIV-2609-16409` | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 | 在 hybrid proposal/correction 处补充：image generator 可作为视觉 state transformation tool，但生成 state 必须由 verifier/selector 检查，不能把生成质量当推理正确性。 | 六项任务与特定模型；几何幻觉、选择误差和多 sample 成本显著。回退固定视觉工具或文本推理。 |
| `SF-2026-ARXIV-2609-16453` | `AGENT-RAG` Ch76 | 在 iterative retrieval stop 处补充：每轮维护 partial-answer quality 与 marginal utility；只有经过校准的 stop policy 才能结束检索。 | 多跳 QA；utility 明显比 quality 难预测，约 11% 轮次下降不是通用阈值。回退最大轮数、无进展阈值或外部 verifier。 |
| `SF-2026-ARXIV-2609-16454` | `TRAIN-SFT` Ch29 | 在 SFT distribution 处补充：population cross-entropy 约束不自动转化为有限样本 diversity；SFT 可欠分散也可过分散，须实际测量。 | synthetic language、survey/code 与有限模型；不能给开放生成自动校准。回退更代表性数据、regularization 与受控 sampling。 |
| `SF-2026-ARXIV-2609-16459` | `TRAIN-SFT` Ch29 | 在 privileged distillation 处补充：错误 prefix 会让 teacher/student 同向偏离；应比较同一 teacher 在有/无 privileged evidence 下的差异，而非直接信任 teacher completion。 | Qwen3.5 4B/9B、六 benchmark；teacher 视觉错误与额外 forward 成本存在。回退 verified target、人工筛选或 RLVR。 |
| `SF-2026-ARXIV-2609-16487` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 在 dynamic evaluation 处补充：reference 是与 Agent 访问同一 live state 的 versioned executable function，输出拆为 atomic fact 后再评 precision/recall。 | 55 cases、内部 skill、synthetic staging DB，同一 Claude family 生成与 judge；reference code 完整性仍是假设。回退 deterministic gold、人工 gold 或 quarantine。 |
| `SF-2026-ARXIV-2609-16532` | `TRAIN-DPO` Ch34 | 在 preference-pair validity 处补充：事实正确的 rejected response 不能只因风格被惩罚；训练前应验证 factual relation，必要时反转、降权或丢弃 pair。 | 两 benchmark、≤8B 模型与 LLM judge；judge noise 和大 budget 下长度退化存在。回退 CPT/SFT 或 verified preference pairs。 |
| `SF-2026-ARXIV-2609-16537` | `TRAIN-SFT` Ch29 | 在 trainable subspace 处补充：layer necessity 与 plasticity 是两个不同量，且在 Transformer 与 Mamba-style SSM 上关系可反向；层选择不可跨架构复制。 | 有限架构/任务且定义依赖 adaptation procedure。回退架构内 causal ablation、全参或 adapter baseline。 |
| `SF-2026-ARXIV-2609-16639` | `TRAIN-SFT` Ch29 | 在 continual post-training 处补充：让模型先修订自身失败，verifier 只接纳正确且接近当前 policy 的 target，形成 SFT 与 on-policy RL 之间的受控分支。 | 三个视觉任务与 Qwen2.5-VL；缺正确 rollout 或 verifier 错误会污染更新。回退 expert SFT、隔离 replay 或 RLVR。 |
| `SF-2026-ARXIV-2609-16665` | `MODEL-LONG-CONTEXT` Ch22 | 在 recurrent iteration control 处补充：更新方向与 finite-step magnitude 必须分离；方向导数为正仍可能因 curvature/overshoot 使完整 recurrent step 有害。 | 两个 looped-transformer family 与 teacher-forced utility；不证明普通 decoder/free-running。回退固定保守步长、减少循环或完整 attention。 |
| `SF-2026-ARXIV-2609-16890` | `PLATFORM-SECURITY` Ch72 | 在 unlearning acceptance 处补充：path routing、representation 与 decode 是三类不同 observer；三层都要测 recoverability，行为抑制不能冒充删除。 | TOFU/MUSE/WMDP、离线 forget set；未覆盖连续请求/长上下文。失败时回退 retrain、版本隔离和访问控制。 |
| `SF-2026-ARXIV-2609-17043` | `AGENT-RAG` Ch76 | 在 RAG failure taxonomy 处补充：检索未命中与 passage 已在但事实不可抽取是不同状态；只有前者适合 targeted re-retrieval。 | 三个 QA benchmark 与 LLM fact judge；开放域覆盖未证明。后者回退 extraction/verifier、扩大上下文或人工处理。 |
| `SF-2026-ARXIV-2609-17088` | `AGENT-MEMORY` Ch77 | 在 learned memory policy 处补充：delayed future reward 可回传到早期 store/retrieve decision，但 immutable raw log 与离线 Gate 必须保留。 | 三个 conversation dataset 与 LLM judge/有限 human preference；延迟 credit、偏好固化和 poisoning 是失败面。回退静态规则和离线验证。 |

## 有限返修新增：已有覆盖，不写回

| Source Family | Owner | 现有具体承载 |
| --- | --- | --- |
| `SF-2026-ARXIV-2609-16093` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已要求保留 artifact、tool trace 与 action-time environment state，并将终局结果拆成可验证中间状态。 |
| `SF-2026-ARXIV-2609-16251` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已要求 native artifact 的结构、约束和可执行状态检查，终局截图不拥有成功真值。 |
| `SF-2026-ARXIV-2609-16635` | `AGENT-MEMORY` Ch77 | 已覆盖 procedural asset 的 applicability、validation provenance、revision 与 fallback。 |
| `SF-2026-ARXIV-2609-16646` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已明确 confidence sensor 不是通用概率，并要求校准、abstention 与外部 evidence owner。 |
| `SF-2026-ARXIV-2609-16648` | `INFER-SPECULATIVE-DECODING` Ch48 | 已将 RL rollout 信号训练 draft policy、target verification 与 exact commit 分层；该材料未改变 exactness contract。 |
| `SF-2026-ARXIV-2609-17193` | `INFER-SCHEDULING` Ch56 | 已按 KV residency、bytes×time、异构资源与 SLO 组织 state-aware scheduling；simulation 未改变主线。 |
| `SF-2026-ARXIV-2609-17251` | `MODEL-LONG-CONTEXT` Ch22 | 已覆盖 recurrent compact state 的容量、漂移、更新与 full-context fallback。 |
| `SF-2026-ARXIV-2609-17391` | `AGENT-PLATFORM` Ch84 | 已要求 local proposal 经过 production replay/global evaluator 后才 commit，并保留 rollback。 |
| `SF-2026-ARXIV-2609-17474` | `TRAIN-SFT` Ch29 | 已覆盖 teacher/student、source/target shift 与 continual update 边界；纯理论 promise-class 结果未新增可部署机制。 |
| `SF-2026-ARXIV-2609-17515` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已要求按 task complexity、capability component 与 failure mode 做压缩/剪枝 slice，不能只报告均值。 |
| `SF-2026-ARXIV-2609-17516` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已覆盖 answer/abstain cost、coverage-risk operating curve、校准与 defer authority。 |

## 已落实，独立复核通过

### `MODEL-TOKENIZER` — 第 11 章

- Source Family：`SF-2026-ARXIV-2609-16984`，exact source `arXiv:2609.16984v1`。
- 现有论点差异：本章已有 tokenizer identity、special token 与 chat template，但尚未明确区分“保留 ID”与“可由内容编码生成的 surface string”，也未将 control-token forgery 定义为编码层 identity 破坏。
- 写回命题：内容 tokenizer 的 codomain 不得包含 trusted control IDs；chat template/协议层只能在内容编码之后、通过受信路径注入 nameless control identifiers。`allowed_special`、字符串清洗或不可打印字符不是完整保证。
- Trade-off / fallback：迁移会改变 tokenizer/model/template identity，并可能破坏旧 artifact；不能迁移时，严格模板解析、输入转义、role isolation 与旧 tokenizer 的 adversarial regression 继续成立。
- 不可外推：五个 family 的实现与 probe 不证明任意 tokenizer、任意 downstream safety 或向后兼容。

### `MODEL-LONG-CONTEXT` — 第 22 章

- Source Family：`SF-2026-ARXIV-2609-16372`，exact source `arXiv:2609.16372v1`。
- 现有论点差异：本章已有 recurrent/compact state，但缺少 diffusion LM 在离散 chunk 被清空后，以固定连续 register 作为唯一跨 chunk 状态的受限分支。
- 写回命题：bounded-state generation 可把 history owner 从增长的 token 序列改为固定维 register；register update、chunk boundary、auxiliary supervision 与 reset rule 必须共同版本化。
- Trade-off / fallback：固定 memory 换来 state drift、不可解释和训练监督；full context 在作者 1024 setting 仍更强。需要逐项引用或 register 未校准时回退显式 history/RAG。
- 不可外推：单一 scratch task family、以单 seed 为主，不证明 frontier dLLM 或开放域推理稳定。

### `MULTIMODAL-WORLD-MODELS` — 第 25 章

- Source Family：`SF-2026-ARXIV-2609-17524`，exact source `arXiv:2609.17524v1`。
- 现有论点差异：本章区分生成画面与 action-conditioned transition，但尚未把“预测哪种 modality”作为 control-relevant state selection，而非重建越完整越好的默认假设。
- 写回命题：World-Action Model 应按控制因果顺序选择/生成 point tracks、feature、depth、RGB 等状态，再条件化 action；评价分开报告 modality prediction 与 closed-loop action，不用 RGB fidelity 代理控制收益。
- Trade-off / fallback：减少 RGB 可能节省计算并缩短 action path，但丢失人类审阅与未建模视觉线索；任务需要可视证据或 state selector 失配时保留 RGB/显式 observation。
- 不可外推：证据仅覆盖作者三项双臂真实任务与披露的数据/计算范围。

### `TRAIN-DISTRIBUTED-TRAINING` — 第 36 章

- Source Family：`SF-2026-ARXIV-2609-17380`，exact source `arXiv:2609.17380v1`。
- 现有论点差异：本章已有 collective correctness 与 checkpoint identity，但没有把可审计 replay 的 identity 扩展到 kernel reduction order、样本/batch order 和 collective operation order。
- 写回命题：训练“可重现”不能只保存参数与随机种子；应冻结 operation schedule，并能从任意 step checkpoint 重放局部区间。collective auditor 的 coverage 必须与 rank/sample assignment 一起记录。
- Trade-off / fallback：固定顺序与密集 checkpoint/audit artifact 增加吞吐、存储和 portability 成本；高吞吐生产训练可保留非 deterministic 路径，但须将 statistical reproducibility 与 exact replay 分开声明。
- 不可外推：1B 规模与作者 artifact 证明可行性，不证明 frontier-scale 成本或任意异构集群都能廉价复现。

- Source Family：`SF-2026-ARXIV-2609-17483`，exact source `arXiv:2609.17483v1`。
- 现有论点差异：本章已说明 worker arrival、staleness 与数据异质性会改写 objective，但尚未明确“first/second-order similarity 与 weak interpolation 仍不足以恢复同构异步训练的时间复杂度”这一负面边界。
- 写回命题：runtime 应把 worker-speed heterogeneity 与 local objective/data heterogeneity 分账；只有验证 strong interpolation 与 local PL 等更强前提后，才能声称接近 homogeneous 的 wall-clock dependence。普通相似度或平均 gradient 接近不能替代该 Gate。
- Trade-off / fallback：更强假设换来更乐观上界，却限制 workload；前提不成立时回退保守异构 bound、matched synchronous baseline，或重新平衡/shard 数据，而不是只调度更快 worker。
- 不可外推：理论建立在披露的 convexity/smoothness/interpolation/computation model 上，下界在 small-ε 只紧到对数因子；不证明任意 LLM 优化器或集群的实际 wall-clock。

### `INFER-KV-CACHE` — 第 45 章

- Source Family：`SF-2026-ARXIV-2609-17109`，exact source `arXiv:2609.17109v1`。
- 现有论点差异：本章已有 adapter/cache identity，但需明确“跨 adapter KV 复用的语义近似”与“底层 storage 物理共享”是两个不同结论。
- 写回命题：reuse key 必须包含 base model、prefix boundary、position rule、adapter identity 与允许的 approximation policy；命中只授权跳过 prefill，不自动授权共享内存或声称数值等价。
- Trade-off / fallback：作者在 Qwen3-1.7B、HotpotQA/GSM8K 上看到小而不一致的质量损失和 warm TTFT 改善，但 storage 仍 copy、memory 下降有限；高风险 slice 或 adapter drift 时回退 per-adapter prefill。
- 不可外推：不证明其他 model/adapter/task/length 的等价性，也不证明真实多租户内存节省。

### `INFER-TENSORRT-LLM` — 第 49 章（合并两项）

1. `SF-2026-ARXIV-2609-16085`，exact source `arXiv:2609.16085v1`。
   - 差异：现有 execution-plan identity 尚未明确量化 artifact 在跨 Kernel/ISA/vendor compiler 时可能改变 scale 解释、输出与速度方向。
   - 写回：量化计划同时绑定 artifact、scale semantics、integer kernel/ISA、compiler path、target hardware 与 behavioral/latency validation；compile success、top-1 保持或相同 ONNX 文件都不足以证明 portability。静默忽略 scale 必须 fail closed。
   - 边界：七类硬件各有限设备、部分 p50/单次测量；不能推广到全部 INT8 runtime。
2. `SF-2026-ARXIV-2609-16389`，exact source `arXiv:2609.16389v1`。
   - 差异：本章已有 compiler/kernel lowering，但缺少“顺序程序拥有语义、annotation 拥有 schedule、compiler 校验二者等价”的可编程分权。
   - 写回：异步 copy、tensor-core schedule 与 synchronization 不应散落为不可审计 imperative side effect；以 sequential specification 为 fallback，并将 parallel annotation、unsafe rewrite 与 equivalence check 共同版本化。
   - 边界：H100 GEMM 和 concrete-size program；两处 TMA unsafe rewrite、无完整 CUDA formal semantics、未验证 Blackwell/非 CUDA。

### `INFER-GPU-MEMORY` — 第 54 章

- Source Family：`SF-2026-ARXIV-2609-16215`，exact source `arXiv:2609.16215v1`。
- 现有论点差异：本章已有 HBM/CPU/SSD tiering，但可进一步分开“tier capacity 是否足够”与“块放在哪里/何时预取”的二阶 placement 问题。
- 写回命题：先按 session lifetime/工作集决定容量，再依据 recency、reuse frequency、link bandwidth 与 TTFT objective 选择 placement；prefetch 只有在存在可用带宽且预测命中时才成立。
- Trade-off / fallback：更细 placement 增加 metadata、预测错误与迁移流量；capacity 主导或 workload 不稳定时，简单 recency/静态 tier 更可靠。
- 不可外推：synthetic workload、batch=1、single-GPU simulator 与作者 link model，不证明生产排序。

### `INFER-SCHEDULING` — 第 56 章（合并两项）

1. `SF-2026-ARXIV-2609-16206`，exact source `arXiv:2609.16206v1`。
   - 写回：learned router 的 feature、cost constant、SLO 与 deployment calibration identity 必须一同版本化；模拟器或另一 pool 的策略排名不能直接发布。小 pool、极端 scarcity 或 calibration drift 时回退 queue-count/spreading。
   - 边界：A40、vLLM/NIXL 与披露 workload；输出长度在所测配置主导，不是通用因果定律。
2. `SF-2026-ARXIV-2609-16491`，exact source `arXiv:2609.16491v1`。
   - 写回：agentic workload 的调度目标由单请求 TTFT/TPOT 扩展到整条 trajectory 的 JCT/makespan；PP 能否成为非支配点取决于 prefill/decode balance、prefix reuse、MTP 与 fleet accounting，不能按 chat-serving 经验静态排除。
   - 边界：两种 360B+ MoE、64×H800 与 deterministic trajectory replay；不证明任意 agent workload 或 cluster 上 PP 最优。

### `PLATFORM-MODEL-REGISTRY` — 第 59 章

- Source Family：`SF-2026-ARXIV-2609-16193`，exact source `arXiv:2609.16193v1`。
- 现有论点差异：本章已有 hash/signature、provenance 与 behavior canary，但尚未明确 behavior-preserving parameter permutation 可承载隐藏 payload；“输出几乎不变”不能证明 weight artifact 只包含模型语义。
- 写回命题：Registry admission 应把 model bytes 当成潜在 payload carrier；除签名与行为 canary 外，按 threat model 执行 weight-structure/stegomalware scan，并允许在保持功能的对称变换族中重新 materialize/derange 后再签名。neutralization 后必须重新跑 capability/safety regression。
- Trade-off / fallback：随机 permutation 可破坏已知 permutation encoding，却增加 materialization、数值漂移和兼容性风险，也不覆盖非 permutation payload；来源可信且 artifact chain 完整时仍以签名/provenance 为廉价 baseline，高风险第三方权重进入 quarantine。
- 不可外推：作者只证明披露模型与已知 stegomalware threat model 下的编码/neutralization，并观察小幅数值误差；不证明清除未知隐写或恶意 remote code。

### `PLATFORM-SECURITY` — 第 72 章

- Source Family：`SF-2026-ARXIV-2609-16754`，exact source `arXiv:2609.16754v1`。
- 现有论点差异：本章已要求 post-training safety drift 与 update identity，但尚未给出“训练 token 哪些部分承载跨域 misalignment signal”的白盒审计与因果干预路径。
- 写回命题：对高风险 fine-tuning，可先用 frozen base 与 update/adapter 估计 token-level attribution，再用 attribution-guided loss masking 或 reweighting 形成修复 proposal；独立 safety/utility Gate 才能接受更新，不能把 attribution 直接升级为删除或安全证明。
- Trade-off / fallback：更细 credit assignment 可减少盲目丢弃整个数据集，却引入白盒访问、attribution 误差、mask churn 与表达风格误伤；信号不稳定时回退数据隔离、较小 update、adapter 隔离和完整行为红队。
- 不可外推：单一 bad-medical-advice domain、每条件单 seed、1–1.5B 模型与 GPT-4o judge；23×/36× 是所测单次点估计，不证明跨领域因果规律。

### `AGENT-CONTEXT` — 第 75 章

- Source Family：`SF-2026-ARXIV-2609-16302`，exact source `arXiv:2609.16302v1`。
- 现有论点差异：本章已有 evidence/provenance，但缺少从 action obligations 出发，在 derivation graph 上求最小充分 evidence envelope 的明确机制。
- 写回命题：Context 选择应先定义 claim/action obligation，再选择覆盖 derivation closure 的最小证据子图；没有充分 envelope 时状态保持 unresolved，不用更多 token 冒充 assurance。
- Trade-off / fallback：降低 context/cost 但引入 obligation discovery、类型/schema 和 solver complexity；图不完整或 obligation 不可信时回退更宽证据集、deterministic checks 或人工审阅。
- 不可外推：少量真实 preserved artifacts + 249 synthetic；未证明自动发现义务或下游 coding quality。

### `AGENT-MULTI-AGENT` — 第 82 章

- Source Family：`SF-2026-ARXIV-2609-17464`，exact source `arXiv:2609.17464v1`。
- 现有论点差异：本章已有 coordination tax 与同预算 baseline，但缺少将 decomposition 的 root-state exposure 降低和 handoff retention/yield 损失写成同一 admission frontier。
- 写回命题：每增加一层委派，完整性隔离可能改善，任务 yield 却按 handoff retention 累乘并增加 token/latency；topology controller 应从 measured retention、coordination loss、root exposure 与 equal-budget threshold 选择分解深度。
- Trade-off / fallback：高风险 root state 可接受较低 yield 换 integrity；目标是产出率且约束弱时 flat/single-agent 仍是默认。观测 trace 和拟合模型不能当普遍因果律。
- 不可外推：600 production traces、16,082 hops 与 1,012 annotated traces 的估计依赖数据选择、定义和模型假设。

## 已有覆盖，不写回

| Source Family | Owner | 现有具体承载 |
| --- | --- | --- |
| `SF-2026-ARXIV-2609-16268` | `AGENT-TOOL-CALLING` Ch78；训练 handoff `TRAIN-GRPO` Ch33 | 已要求区分 tool availability 与 necessity、记录 no-tool baseline/call cost，并防止 reward shortcut；本材料提供受控证据但不改变论点。 |
| `SF-2026-ARXIV-2609-16313` | `PLATFORM-SECURITY` Ch72 | 已有 action-specific obligation、evidence freshness/witness、certificate-bound authority、admission/dispatch guard 与 fail-closed。 |
| `SF-2026-ARXIV-2609-16816` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已要求 reward/judge 接受 adversarial impossibility/control、independent holdout 与 certificate，而非让 rubric 自签成功。 |
| `SF-2026-ARXIV-2609-16933` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已区分 local confidence、sampling/global agreement 与 semantic/modal uncertainty，明确传感器不能混成单一置信度。 |
| `SF-2026-ARXIV-2609-17226` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已区分 world evidence、reporter reliability 与模型是否真正使用证据，并要求 asymmetric error slices。 |
| `SF-2026-ARXIV-2609-17320` | `PLATFORM-SECURITY` Ch72；`AGENT-MULTI-AGENT` Ch82 | 已覆盖恶意状态跨 memory/delegation/tool 传播，以及 detection、containment、recovery 分层。 |
| `SF-2026-ARXIV-2609-17394` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已将 model/scaffold/provenance 纳入 EvalSpec，并要求 paired evidence、置信区间和 leaderboard ranking uncertainty。 |
| `SF-2026-ARXIV-2609-17475` | `INFER-GPU-MEMORY` Ch54 | 已覆盖 KV/state 的 phase-aware residency、tier transition、容量与 latency trade-off；单设备实现未改变长期结论。 |
| `SF-2026-ARXIV-2609-17527` | `AGENT-MULTI-AGENT` Ch82；`PLATFORM-SECURITY` Ch72 | 已覆盖 principal/trust boundary、prevent/detect/investigate 分层、typed handoff、权限与 forensic receipt。 |
| `SF-2026-ARXIV-2609-16229` | `PLATFORM-SECURITY` Ch72 | 已明确 unlearning 必须区分参数擦除与 inference-time refusal/access suppression，并要求在最终部署 artifact 上验证可恢复性。 |
| `SF-2026-ARXIV-2609-16267` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已要求 EvalSpec 绑定 prediction-time 可用输入、provenance、label production 与 decision stage；不能把 record choice 固定在模型比较之外。 |
| `SF-2026-ARXIV-2609-16305` | `PLATFORM-SECURITY` Ch72 | 已以完整 trajectory、tool/environment state、side effect、utility 与 over-refusal 共同定义 Agent 安全 evidence。 |
| `SF-2026-ARXIV-2609-16461` | `AGENT-CONTEXT` Ch75 | 已要求 context compression 保留 typed protocol state、pinned constraints、raw fallback 和 paired-state regression，并按风险拒绝不安全 mutation。 |
| `SF-2026-ARXIV-2609-16730` | `PLATFORM-EVALUATION-SYSTEM` Ch66；`AGENT-MEMORY` Ch77 | 已用 canonical fact ledger、validity interval、tenure slice、write/read audit 与 full-history controls 评估长期状态，且要求机制 fidelity。 |
| `SF-2026-ARXIV-2609-16777` | `PLATFORM-EVALUATION-SYSTEM` Ch66；`PLATFORM-SECURITY` Ch72 | 已要求 evaluator 固定 state identity、报告 control slice，并把 multi-turn trajectory 与 cold-start/single-turn 攻击面分开。 |
| `SF-2026-ARXIV-2609-16986` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | 已要求证明 optimization/update 实际发生、训练评测 provenance 匹配、reward/evaluator 有效；null effect 不能包装成训练收益。 |
