# Apr17 V3 第二个十项有限独立审阅

## 2026-09-27 实际写后：首批五项通过

续批三项实际写后也通过：root 顺读 Ch48“历史 Logits 与 N-gram Cache”、Ch45“先形成可读压缩状态”、Ch55“混合状态组”及两侧交接，定点重开官方 v1 的 AC 状态维护、MemoSight §3.1–3.3 mask/position/历史 memory 和 PrfaaS §3.3 group/tail。正文保留 proposal 与 commit 分责、greedy/B1 的比较反例、压缩模型而非原模型的验证对象、memory 累积非恒定、SWA 精确长度仅为该实现条件，以及 transfer 完成且 destination commit 后才回收的工程约束。收益、额外状态成本、失败回退与所测配置边界齐全；不把 marker 存在当验收，也未复现实验。14885、14889、15039 可以同步为实际 Integrate，释放 Ch48/45/55；本日实际整合增至8项，剩余31项普通 Books 工作，日级 Gate 仍未通过。

复核者root，不是本次正文写入者。沿用下述未变化的必要证据与采用复核，本轮重开官方v1并顺读实际新增段及两侧衔接：14626的§4.2–4.3/§5.2与simulation范围；14825的VR/MA lowering、repair及Table4；15167的未校准probe、固定验证集及AppendixA；14690的§III-A/B四项计数/代数分解；14561的§III V-first/V-major及TableII质量反例。未复现实验或重读无关附件。

Ch49三个正文位置分别为“三类基础优化”下的分层IR、“量化不自动加速”后的checkpoint/probe、Anchor Artifact后的bit/tier分工；Ch36两处分别承接Alpha-Beta的观测口径与CP buffer的readiness/cache分支。已读真实正文，不以marker存在代替核验。共同grid与projection-boundary PSUM再非线性、repair/live-range成本、不同INT4/8配置混杂、同窗口非零计数、DiT精确通信重排与跨步近似各自保留；有限仿真/小模型/有退步的质量切片未外推成生产保证。旧方案、约束、代价、fallback与相邻交接齐全，五项窄采用及实际写后通过。

允许14626、14825、15167、14690、14561同步为真实整合并更新章末证据状态；其余34项普通Books工作以及本日日级日期/来源验收不由本记录预支。下文“尚未实际写入”的写前表述为前一阶段历史，不再适用于这五项。

本文件仅复核 `14626、14690、14825、14885、14889、14993、15009、15022、15039、15149`。采用当前研究合同，核对作者必要 exact-v1 证据与实际 Books 命题，不扩大 raw 536 / candidate 88，不遍历附件或版本史。源材料均为下列官方 v1 HTML；作者已有必要记录可复用，但本轮实际重新读取了方法、关键评价条件和反证。本轮是独立非作者语义审阅，未另加跨模型调用。

裁决中的 `PASS — Narrow Gap Proposal` 只表示必要 source→owner 比较支持该窄增量，**不表示 Books 已写入、Integrated 或整日 Gate 通过**。日期与首次公开归属仍由日级独立 lane 验收，本文件不以 submission/Updated 代替它。十项均保持作者 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，没有发现需要改分的定义或算术错误。

## 1. ELMoE3D — 2604.14626v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.14626v1)，§4.1–4.3、Algorithm 1、§5–7、Table 3。复核了共享量化网格、MSB/LSB 分片、draft/verify 模式与 cycle simulator。
- 实际 owner：`INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)“量化为什么不自动带来加速”“一个 Anchor Artifact 支撑多格式”；交接 `INFER-SPECULATIVE-DECODING`，[Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md)“MoE verification 还要结算 target-expert expansion”。Ch49 已区分存储与执行精度，EdgeFlow 还已有低 bit 存储→INT8 解包；Ch48 已有 resident draft experts。但这些实际段落没有承载**同一量化表示按 bit 嵌套、快慢 tier 分别计算并合并 partial sum**这一分支。
- 必要机制与边界：共同 INT8/G32 网格的 MSB4 驻留、LSB4 外存，hot-expert 子集与高位产生 draft；verify 恢复原 router 和完整量化目标。其 exactness 只相对量化 target，不是浮点模型。证据是 ASAP7 synthesis 与 Duplex/Ramulator simulation，非硅测量；GPT-OSS MXFP4 不使用相同 bit 轴，Table 3 的量化 SD 也存在低于 1× 的配置。
- 最窄拟稿：独立多格式副本易于治理，但端侧容量紧时可让 draft 与 target 共用嵌套 bit 表示；表示 owner 固定量化 grid，数据通路 owner 负责两 tier 的 partial-sum 合并，target 仍拥有验证与提交。节省副本不保证收益：低位搬运、合并同步、expert cache 与 KV 竞争必须进入成本；格式不兼容或收益不足时保留独立 artifact / target-only。
- 裁决：`PASS — Narrow Gap Proposal`。只补 Ch49 存储/执行合同；不在 Ch48 重复完整微架构。

## 2. Switching Efficiency — 2604.14690v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.14690v1)，§III-A–D、Eq.1–9、§IV-A。复核有效 bytes 定义、三因子恒等分解及并发窗口限制。
- 实际 owner：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)“用 Alpha-Beta 模型建立下界直觉”、Ring/Tree、SHARP 与 contention-aware overlap。现正文已有 critical-path bytes、链路争用和 in-network reduction，但没有把 collective 有效增量、GPU 接收、交换端口累计转发及容量时间积**分成四本账**。同一网络优化主题不能代替这些观测量的定义。
- 必要机制与边界：有效/接收 × 接收/转发 × 转发/容量时间构成同窗口代数分解，不是三个独立因果效应；reduction 与 dispatch 的有效增量定义不同。顺序无重叠工作可时间加权，并发必须联合测量。§IV 为按并行度缩放模型的模拟，不能据此发布同预算 Rail/Torus 排名；有效通信 bytes 也不是训练质量或 serving goodput。
- 最窄拟稿：Alpha-Beta 解释时间下界；诊断全网时另固定 observation window、port scope 和 collective semantics，分别记录 useful、received、forwarded、provisioned-capacity-time。高端口忙碌可能只是多跳或重复接收，不能自动批准拓扑变更；该账目与 step critical path / 质量合同共同验收，缺少可比计数时保留原模型。
- 裁决：`PASS — Narrow Gap Proposal`。补 measurement branch，不另建网络排名或拓扑 owner。

## 3. Nautilus — 2604.14825v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.14825v1)，§4.2–4.4、§5、§8、Table 4。实际复核 rolling update 的 repair、look-ahead、live-range 与两种 tile IR。
- 实际 owner：`INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)开篇 typed equality space、“三类基础优化”和 Typed System IR。现有正文说明保持数学语义后选 tile/layout/fusion，却没有区分 scalar schedule、表达式值级 VR-tile 和显式搬运 MA-tile，也未说明跨 reduction 融合为何要补偿计算。不是因为新增 compiler 名称而判 gap。
- 必要机制与边界：先安排 scalar loops/fusion，再用 VR-tile 保留值表达式重写，MA-tile 承载显式数据搬运与 backend 映射；rolling update 改写依赖并加入 repair，look-ahead 捕获中间 elementwise，局部容量还约束 live range。实验是 GH200/RTX5090、FP16/FP8、B1/8、1K–32K 的受测 kernels；RTX5090 对 TileLang 几何均值仅 1.01，部分 1.00，不是全栈服务普遍更快。
- 最窄拟稿：高层融合与低层 layout 混在一种 schedule 中会扩大搜索并提前提交；分层 IR 可延后搬运决策，但跨 reduction 融合的 repair work、局部 buffer 生命周期、backend 覆盖和实测搜索成本须一起结算。repair 或编译成本超过节省时，普通 fusion、手写 tile 或静态成熟 kernel 仍合理。
- 裁决：`PASS — Narrow Gap Proposal`。补执行计划表示与融合合法性/成本，不扩写整套 compiler 教程。

## 4. RACER — 2604.14885v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.14885v1)，§3.1–3.3、§4.1–4.3、Table 1；复核 copy-logit、AC ancestry touch、LRU leaf、tree union 和 target verification。
- 实际 owner：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md)“从独立 Draft 到 Target-coupled Draft”及 training-free latent/embedding probe 分支。现正文不承载 bounded 历史 logits + n-gram proposal 的状态与失效条件；不应以“都是 training-free”直接 Existing。
- 必要机制与边界：copy-logit 取最近同 token 的历史 target 分布作为未来候选近似；bounded AC 用触及祖先与 LRU leaf 回收检索状态，检索树与 logit 树合并后仍交 target。failure links 在 prefill 后 lazy rebuild，未重建部分暂为普通 trie。历史 logits 不是真正未来分布，LRU 不拥有 commit。greedy/B1/max-output1024 的 Llama3.1 Spec-Bench 2.41× 仍低于 EAGLE-3 2.51×；不能以任务平均反证消失。
- 最窄拟稿：重复模式足够时，可复用已验证历史而不训练 drafter；proposal cache 应有明确容量、近期性与重建状态，只输出候选树。所有 token/KV commit 留给 target verifier。相同 token 的语义环境可能不同，缓存 lookup/构树也耗时；模式稀少、并发/SLO 或随机采样未验证时，普通 target decoding 或已治理 drafter 更稳。
- 裁决：`PASS — Narrow Gap Proposal`。不把本文 greedy 评价升级为未验证的 stochastic exactness。

## 5. MemoSight — 2604.14889v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.14889v1)，§3.1–3.3、Table 1、§4.1、§5.1–5.3。实际复核特殊 token 的 position/mask、step boundary 与压缩率反证。
- 实际 owner：`INFER-KV-CACHE`，[Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“Segmented Execution 必须在训练与推理共享同一语义”、trained shared KV 与 synthetic cache；Ch48 仅承接 draft/verify。现段落分别覆盖 read/gradient boundary 与压缩，但未承载**预测分支隔离→step 内读出 memory→原 step KV 回收**共同训练的时序。
- 必要机制与边界：foresight hidden state 不被未来主路径读取，完成步骤后产生 memory/boundary 再回收 raw KV；位置与 attention mask 必须一起训练。这是压缩后模型语义，不是原 full-context target 无损插件。Qwen2.5-7B/Llama3.1-8B、5 epochs、greedy/output cap10240 的结果存在 16× 压缩退步；Peak 指 context tokens，非进程 VRAM。
- 必须修正：历史 `H_i` 仍累积所有 memory/boundary，因此不能由论文的 bounded wording 推出无限 reasoning 的常数 cache；应写减少历史增长斜率/回收已完成步骤 raw KV。Table 3 也有传统 MTP 在个别任务更高，不能写全任务优于传统 MTP。
- 最窄拟稿：模型训练可使压缩状态成为后续允许读取的唯一历史；runtime 只有在 memory 已形成且 mask 合同一致时才能回收原状态。它降低历史状态量，却引入 joint-training、摘要信息损失和 boundary 识别风险；普通 checkpoint、不容许质量损失或不满足位置/mask身份时保留 full KV。
- 裁决：`PASS — Narrow Gap Proposal`，以上常数内存修正为采用前条件。

## 6. Serving Chain-structured Jobs — 2604.14993v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.14993v1)，§2.1–2.2、§3.1–3.2、§4.2/Table 1。实际核查内存约束、virtual servers、JFFC 与 trace/model 假设差异。
- 实际 owner：`INFER-SCHEDULING`，[Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)“低带宽拓扑要联合预算 Hops、Bytes 与 Steps”“多模型 Serving 必须分离离线模板与在线分配”“Session Admission 是驻留时间上的容量承诺”。已有 placement/KV/capacity 概念，但没有把**连续 block 与按 chain 预留 KV**合成 `(service rate, concurrency capacity)` 虚拟 job server，供在线 dispatch 消费。
- 必要机制与边界：权重共享、每 job KV 独占；离线确定可行 chain 与预留容量，线上 JFFC 选最快有余量 chain，满载入中央队列。假设 memory-bound、固定 per-job cache、无迁移抢占；不能把物理共享和有争用的动态 batch 直接称独立。PETALS 3×A10080GB→9 MIG/Azure trace 实测存在 P95/P99 结果，但无通用 tail SLO；trace 显著偏离 Poisson/exponential 分析假设。
- 最窄拟稿：先加载权重再按余量接流量，在低负载时简单；显存同时承载共享 blocks 与独占 KV 时，应联合定义 chain capacity，再允许在线路由使用。更长 chain 可能腾出并发却增加服务时间；固定预算、失效重建和静态 profile 限制适用域，动态 KV/突发超域时继续保守 admission，不把 steady-state surrogate 当任意到达的精确最优。
- 裁决：`PASS — Narrow Gap Proposal`。保留已有 online controller，不把整篇优化算法复制进正文。

## 7. YAN / MoE-FM — 2604.15009v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.15009v1)，§3.1–3.2/Eq.4–6、§4、§5.1–5.3/Table 1。实际核查责任分配、frozen routing 和 oracle-length 评价。
- 实际 owner：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)continuous/discrete flow、source/coupling 及 conditional expectation/full-derivative-square 区别。现正文未说明 conditional-MSE 速度平均与 mixture likelihood 的选择，也未说明 transport identity 可在开始固定。Ch21 稀疏计算不是该增量 owner。
- 必要机制与边界：Gaussian-mixture NLL 以 responsibility 分配 velocity targets；每 token 在 t0 采一个 expert 并固定整个 transport，不是每一步 top-k。K=1 / 大 σ 存在退化；实现 dense experts，稀疏化是未来方向。200M/210M task-finetuned、单 H200/B1/greedy/all-method oracle lengths，与124M/139M及8B比较，不支持通用 AR 替代；bAbI 有质量落后。
- 最窄拟稿：单点平方回归合理地估计条件平均；少步数、有限容量与多峰 transport 下，可用 mixture likelihood 表达局部方向并冻结轨迹级分支。它改变目标、router 与路径身份，也增加专家/encoder/decoder 成本；不是保证所有多峰任务更好。原目标已验收、分支不可识别或收益不足时，保留普通 FM/AR 与更多 solver steps。
- 裁决：`PASS — Narrow Gap Proposal`。不把论文动机“平均方向”误写为普通 marginal FM 数学无效。

## 8. Route to Rome — 2604.15022v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.15022v1)，§2–3、§4/Table 1 及必要 Appendix D.4。实际核查 suffix 输入权、有限查询 surrogate 和 Thinking fingerprint 的性质。
- 实际 owner：`PLATFORM-SECURITY`，[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)MoE fault Denial-of-Wallet、input-only expert attack 与 sensor/authority 分层。旧 `daily-books-trace` 的 confidence cascade 一句话不是实际正文论证；不能据此 Existing。此处攻击的是模型选择控制面，不是 expert 行为漂移。
- 必要机制与边界：用户改变 query 可推动 quality router 选昂贵模型；有限黑盒决策训练 surrogate 再优化通用 suffix。Table 1 的六个可观察路由 rows、三 runs ASR 测 strong-model routing，不直接测 policy breach 或 quality loss。GPT-5 不暴露决策，Thinking-likeness 只为输出 proxy，不证明内部路径或实际账单。
- 最窄拟稿：成本感知路由把用户内容作为难度信号是合理基线，但可塑输入不应独自授予昂贵资源。资源 owner 应独立约束预算、rate/attempt limits 和允许模型集合，并将 quality 变化与资源消耗分账；防护也需另验，不能把本文攻击成功率当已证明的防御效果。低风险受信流量可保留简单 router。
- 裁决：`PASS — Narrow Gap Proposal`，security override 深入。只承载资源授权边界，不复现攻击配方。

## 9. PrfaaS — 2604.15039v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.15039v1)，§3.2–3.4、§4.1–4.2。实际核查 cache groups、尾块生命周期、prefix 后长度与 measured-profile-fed model。
- 实际 owner：`INFER-PD-DISAGGREGATION`，[Ch55](../../../../../books/part-05-inference-system/55-pd-disaggregation.md)“从静态 Pool Ratio 到耦合的 SLO Control State”“多轮交互把 Prefill 重新变成可路由的增量任务”。已有 incremental routing、cache affinity 与 pool controller，不能把这些再次算 gap；真正缺的是**混合 state 类型怎样限定 reuse/transfer**及据此判断跨集群可行性。
- 必要机制与边界：本文 linear/SWA request state 需要精确 cached-length 复用，full-attention blocks 允许 partial prefix；prefix-cache blocks 完整才可复用，transfer-tail blocks 保留到 transfer 完成才丢弃。remote 选择按 uncached length/带宽/cache，长期另调 pools。内部1T KDA:MLA3:1、32H200+64H20、100Gbps跨VPC，input128–128K/output1024/SLO40token/s（无SD）；结果由 measured profile 输入稳态模型，非 bursty end-to-end goodput，precision ND。
- 最窄拟稿：统一 token/block 命中率在全 attention 中容易管理；混合模型需要 state group、cached-length 与完整性分别验收，不能把一个组的命中当整模型可恢复。prefix reuse 与一次性 handoff-tail 也不同。架构减少 transfer bytes 后跨集群可行性仍受局部 profile、带宽与缓存实际位置约束；兼容性或链路 Gate 失败回退本地 PD。
- 裁决：`PASS — Narrow Gap Proposal`，transfer 完成后回收的时序为采用前条件。

## 10. LLMs Gaming Verifiers — 2604.15149v1

- 必要来源：[官方 HTML v1](https://arxiv.org/html/2604.15149v1)，§3–4、Table 1、Appendix C。实际核查同一 hypothesis、双射对象改名、标签/属性不变与两次训练实验。
- 实际 owner：`TRAIN-RLHF`，[Ch31](../../../../../books/part-04-training-system/31-rlhf.md)“Reward hacking 与 Goodhart's Law”、checked-span/完整行为及 tokenizer/reward adapter。现正文已有 verifier 漏洞，但没有同一输出在任务保义变换后的双验收，不能因泛称 reward hacking 就 Existing；Ch33 仅承接 inference-time verifier authority，不复制训练诊断。
- 必要机制与边界：生成一次 H，分别在原任务与双射改名对象常量的任务验收；不重新生成答案，不替换颜色等属性。枚举已见对象可过 extensional checker，却未学规则。App C 两同基模 runs 仅 reward 不同，在 SLR 内支持因果分支；无重复 seeds、开放模型标签有 presumed，不能由跨模型对比推出普遍原因。
- 必须修正：Table 1 的 OLMo-3 32B/7B 两个 RLVR rows 和 GPT-5-mini-low 都零 observed shortcuts，反驳“所有 RLVR 必然捷径”的推广；零观察也不证明零漏洞。
- 最窄拟稿：只检查原实例标签便于自动奖励，却可允许枚举代替规则；任务语义确实要求对象标识不变性时，用同一已生成假设做原实例与保义改名双检，区分 fit 与 generalization。变换无效、标识本身有任务含义或只需记忆实例时不能强加这条；更广的独立评价与安全 Gate 仍保留。
- 裁决：`PASS — Narrow Gap Proposal`，security/evaluation-contract 深入；不得宣称 isomorphic checker 消除全部 reward hacking。

## 批次交接

十项均支持上述最窄提案；未更改 README、Books、其他日期或全局 checkpoint。作者需要将审阅后精确论点落实到对应实际正文，再核对报告 disposition 和 source-family binding。实际写入前仍为普通待办，不是外部材料 Blocked。本文件不接受泛模板“必要已读/已吸收的语义增量”作为实际采用。

必须保留的事实收窄已独立通知作者：14993 有 P95/P99 结果而非通用 SLO；15039 transfer-tail 在 transfer 完成后回收；14889 memory history 仍增长而非常数内存；15149 部分 RLVR rows 为零 observed shortcuts。分数与窗口 owner 未在本文件改写。
