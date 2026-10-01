# 2026-09-29：独立复核记录（FINAL 通过）

Reviewer：`sep29_four_pre`。本人未写 Books、正式 Report 或 LEARNING_STATE。以下前半为 2026-10-01T18:46:01+08:00 起的历史 PRE/POST 过程；当时的等待状态已由文末 **2026-10-01T19:10:21+08:00 日级 FINAL** 覆盖。N20–23 实际 POST 详情在 [本 lane 记录](./V3_N20_23_PRE.md)。本人四项 theme 的 source 是作者提案，由 root 独立 PRE、Tail B 实际 POST，不自验其 source 或写入。

本次重新读取 AGENTS、研究/来源/Report 合同、Prompt、ROADMAP 与当日 checkpoint；Books 方法读取 Learning Philosophy/Writing Guide。保护原 staged/unstaged，未 stage/commit/push。范围只为 [V3_TAIL_B.md](./V3_TAIL_B.md) 的六家族，不重开 N1–19、不扩池。所有必要 exact-v1 HTML 可访问；没有伪称复现、代码运行或 External Blocked。支持和反侧足够后停止，BEHAVE 只定点补 B.4/B.5，未遍历其长附件。

## Tail B：PRE 总结

五 I 的长期差额和 owner 成立；分数采用作者已校准的 Design Delta/System Reach/Durability：DPS 7、Sparsity 6、SuffixReplay 7、BEHAVE 6、CUTLASS 5。没有把证据、访问或 Books 决定计入评分。Argus 5 的标准审阅/仅报告可接受，不删除其新评价事实。**下述具体标题/用词修正随写入执行后，五项 literal 可通过 PRE。**

| 家族 | PRE 结论 | 实际 owner 与可接受位置 |
| --- | --- | --- |
| DPS 2609.34380v1 | I，literal 支持；须明确独立标题 | Ch54 `INFER-GPU-MEMORY`，既有 `2605-28095` 末段/marker 后，离线 weight-as-stream 段前；增加 `### 双模式 Weight 与 KV 的非对称共享`。不把新两段写到 ANE 的 Review notes 内。 |
| Sparsity Crossover 2609.33889v1 | I，literal 支持 | Ch54 的“减少 Bytes”中，token/element retention 成本/fallback 段后、低比特 Compute Balance 标题前；增加 `#### 少读 Weight 与少读 KV 的交点`，正文明确只少读而非少驻留。 |
| SuffixReplay 2609.33477v1 | I，literal 支持 | Ch45 `INFER-KV-CACHE`，`2608-30386` retention-horizon 分支后、Video Ingestion cache 前；增加 `#### Group 输入锚点与旧 State Checkpoint 是不同对象`，保留前面的 exact checkpoint/WavePP 和后面的 video cache。 |
| BEHAVE 2609.34785v1 | I，literal 支持 | Ch66 `PLATFORM-EVALUATION-SYSTEM`，Reference Artifact 节中 `2609-01865` 合法多实现/原 oracle 边界末段后、Dense process score 前；增加 `#### Transaction 行为允许 Timing 差异，但 Oracle 不可自授`。 |
| CUTLASS selector 2609.35587v1 | I，须执行两处措辞收窄 | Ch49 `INFER-TENSORRT-LLM`，WaveTune 两段及 `2604-10187` marker 后、“Tensor Core 指令名必须分层”前；增加 `### 硬件行为代理可以选 Kernel，但不认证执行`。 |
| Argus 2609.35508v1 | 标准完成，仅报告/Books No Change 可接受 | Ch69 `PLATFORM-TRACE` 已有同观测对象 reference、偏离只作候选、call-chain 与干预验证；不新增 I。保留新 60-run 对照和 missing-tree 反侧，不宣称整篇所有实现已在 Books。 |

## 独立必要证据与具体差额

### DPS

直接核 [v1 IV-B/C、V-A/B](https://arxiv.org/html/2609.34380v1)：persistent low-precision 权重、shared residual/KV 和 pinned CPU residual backup；全部 residual 恢复后才通知 full mode，每 forward 用一个模式；KV permanent mapping 是为了 scheduler free 与 in-flight worker 的地址 race。恢复不撤销已生成 token。V 的三 MoE/H100 与 joint SLO/effective pass@1 是有限服务证据，不等精度等价；低压力未分出收益。

Ch54 的既有 `2605-28095` 已有 desired/committed bitwidth 和先释放/先加载协议，新差额是 persistent/residual 的非对称共享、KV mapping 与 batch 模式历史边界。作者 literal 保留了该分工及成本。原 Ch54 “Weights 与 KV”空标题之后夹入 Cache/ANE 段，笼统“放联合预算段”容易误落 Review notes，因此表中的新标题是必须项，不授权重排无关旧正文。

### Sparsity Crossover

直接核 [v1 §3–5/6，完整驻留定位 §3及 Appendix A](https://arxiv.org/html/2609.33889v1)：同 dtype 下恒定 projection-read 与随 context 增长的 KV-read 给 byte crossing；不同 element bytes 与 batch activation union 会移动交点，kernel cost 再移动 latency crossing。原文明确 full cache 仍 allocated/接收新 entries，selection 另 gather，不是容量削减。共同 split-K dense baseline 与远距检索反侧排除了“低效 dense 对照产生超 byte-bound 加速”和“PPL 相近即质量相同”；短输出未必摊销 scoring。

Ch54 当前 token/element retention 讲驻留及粒度，还没有同一个 decode traffic budget 下两条少读路径的交点。两段 literal 不把阈值升成固定 dispatch 或将 sparse bytes 宣称 HBM 容量，故通过；相同任务质量预算是设计建议，不伪称论文已测所有任务质量。

### SuffixReplay

直接核 [v1 §4–6、§7.1–7.3](https://arxiv.org/html/2609.33477v1)：每 linear group 的 hidden-input anchors、跳过 full-attention replay、k 的 anchor 单位；sidecar 独立 pool 但共享逻辑 lifecycle，完成页/transfer 后发布，consumer 到相应 group 才 wait。缺失/未发布/hook failure 走 full-prefill；live state 则绕过 replay。质量配对分数不授状态/token 等价，OLMo RULER 有较低项；native exact-hit 同步请求有额外开销，graphs/pool/headroom 也要计。

Ch45 的 exact checkpoint 是保存真实 state 后回放缺 suffix，`2608-30386` 是省略 state units 的 horizon 分支；新缓存对象/group-local replay/publication 确有差额。两段 literal 保留 exact continuation 与完整重算，未用近似 resume 冒充历史 rollback，故通过。

### BEHAVE

直接核 [v1 §3.1–3.2、B.4/B.5](https://arxiv.org/html/2609.34785v1)：agent 的 design 与 BehaviorIR 在开发中彼此检查，最终分别对 hidden gold；accepted input/reset histories 的 task mapping 固定后比较 output histories，timing requirements 单独检查。默认按顺序；仅 task 许可重排且有标识，或明确输出顺序无意义的 multiset 假设，才改 matching。Finite stimulus pool 的 pass 与 coverage 分开；optional exact analysis 不回改评分池，unknown/refused encoding 不获完备性保证，generation/analysis 支持面窄于 replay。

Ch66 `2609-01865` 已阻止 oracle 扩张需求，却没有 transaction timing 与双产物分别过 gold 的执行合同；作者 literal 正好补该口，未采 self-improvement 曲线的普遍因果，也未把 PPA 当芯片交付，故通过。

### CUTLASS selector：两处必须修正

直接核 [v1 §3.1–3.2、§4.1/4.3.9–10、§5.5](https://arxiv.org/html/2609.35587v1)：候选诱发的 wave/cache/occupancy/pipeline proxy 静态可计算，profiling 只用于构建特征和训练；shape/layout 内相关分析、base shape 跨 layouts 共同留出、训练 shortlist best 与 held-out in-space oracle 分开。FP8 的 execution coverage 低，fusion 有持平/退步；免部署测量不授免费训练或跨域最优。

Ch49 WaveTune 已有波粒度拟合与 anchor profile，新差额是 candidate-induced static proxy→learned ranking 的选择接口、shape-group 验证和 execution coverage。需要修正：

1. 第一段“在已验证合法 catalog 中的选择”改为“在经过静态合法性筛选的有限 catalog 中提出选择，实际可执行性仍须验收”。静态 validity filter 不是所有候选都已编译/执行成功的证书。
2. 第二段“选择 regret、合法候选 coverage 一起验收”“success-only speedup 不能掩盖无可选 kernel”分别改为“选择 regret、实际 execution coverage 一起验收”“success-only speedup 不能掩盖所选 kernel 未成功编译/执行的请求”。论文 coverage 不足不等于该请求整个合法 catalog 没有可用候选。

其余两段 literal 和 provenance/目标域测量/vendor heuristic/autotune fallback 可接受；不为上述收窄改分、删候选或降池。

### Argus：仅报告边界

直接核 [v1 §2–4](https://arxiv.org/html/2609.35508v1)：RMV 来自同 workload idle reference，PMV 测受干扰路径，经验 delta 阈值指导静态 tree，逐层 multiplexed eBPF/verifier loop。五 victim×四 perturber×三 repeats 的错误归因对照是本矩阵的新证据；微基准 probe 成本不等全服务无开销，pf_cow 因树缺 mmap_lock/slab/RCU 三次 abstain 不授健康，llama.cpp 未给完整模型服务协议。

独立读 Ch69 的 semantic-region/reference、one-class deviation 和 call-chain/replay/干预正文，确认长期原则已有承载。本篇新工程组合与小矩阵仍应在 Report 呈现，不能说“全篇已覆盖”；现有证据没有把 tree traversal 提升成一般因果证明，也不必为局部实现再开 owner。故作者的仅报告理由可接受，但若正式 Report 想给生产 false-alarm、一般零诊断开销或性能选型，则应拒绝。

## 待写后与日级审查

root 实际窄写五 I 后，本 reviewer 再核实际正文、必须修正、标题作用域、原内容保留和 marker。本记录只复用已校准的日期身份，不冒充再次全分类扫描；日级将核正式 source stop、日期依据/范围、候选分母、每项终处置/非作者记录、明确排除的分层抽检及 V3 校验，外部隔离不计正面 Coverage/Evidence。所有日级 Gate 当前仍是待审，不由本 PRE 宣布完成。

## 有限负侧分层抽检（不扩候选池）

独立抽样覆盖 arXiv 硬件、推理工具、边缘模型，以及官方合作公告、agent 插件、CLI 生命周期三个来源/理由层。直接读取 MEGATRON `2609.35254`、JET `2609.33874`、MorphAtt `2609.33207` 的完整题摘；前者只给异构 PCM/RISC-V 模块及效率，JET 为有限候选 likelihood 加既有 prefix/cache/input preparation 的局部执行组合，MorphAtt 为 spike-QKV/attention/RepConv 和 buffer 组合与综合峰值。当前题摘未给相应映射/误差质量合同或新的执行失效边界，贡献排除可接受；不是按模型/硬件标题排除，也未假装三篇全文已审。

直接核 [Lenfest 原始核心](https://openai.com/index/lenfest-ai-collaborative-expansion/) 的资助扩展、合作机制与应用例：未提供新的可复用系统机制或成对控制证据，贡献排除可接受；地方新闻不是排除理由。直接核 [Google Custom Agents 原始核心](https://antigravity.google/blog/custom-agents-in-google-plugins)：Flutter 可应用 code fixes、Firebase 可 author rules，仅 Play release auditor 声明 read-only；现有 custom-agent 的 role/context/tooling 被包装为官方插件，未授统一只读或新增强制权限保证。实际报告不能用“全部只读”解释关闭。

[MiniMax 官方 changelog](https://agent.minimax.io/docs/changelog.md) 可由直接 curl 恢复，web 阅读失败不是此原文的 External Blocked。`0.5.9 · 2026-09-29` 是 background count、请求字节上限及局部 UI 修复，可按贡献关闭；`0.5.8 · 2026-09-28` 的停止会话终止后台任务、switch/clear 保留后台任务确有生命周期语义，不能因“普通 release”排除。原文只有日级日期，仍不足把它归入从 09/28 09:00 开始的本窗；精确日期身份隔离合理，后续收到原始时刻仅重开该条。这些抽样不替代所有原始源的完整正面 Coverage。

## Tail B 五 I：actual POST 第一轮（2026-10-01T18:58:27+08:00）

已逐项直接读取 root 实际写入正文及前后旧段，不以作者提案冒充 actual。未变必要源复用本文件 PRE；没有修改 Books。

| 家族 | 实际正文与第一轮结果 |
| --- | --- |
| Sparsity Crossover | Ch54:244/246、唯一 `2609-33889` marker；两段 literal 和 `####` 作用域正确，前两级 token/element selection 成本/fallback、后低比特 Compute Balance 保留。驻留与读取、byte/latency crossing、batch/质量与 scoring amortization 边界完整。PASS。 |
| SuffixReplay | Ch45:1046/1048、唯一 `2609-33477` marker；两段 literal 和新 `####` 作用域正确，旧 exact checkpoint/WavePP/horizon、后 Video Ingestion `####` 分支保留。只重建 group-local 近似状态，publication/wait/full-prefill/live-state、质量反侧和 exact continuation fallback 清楚。PASS。 |
| CUTLASS selector | Ch49:541/543、唯一 `2609-35587` marker；已执行 PRE 两处收窄：静态有限 catalog 不认证可执行性，actual execution coverage 不冒充整个 catalog 空缺。新 `###` 接 WaveTune，下一 `##` 关闭作用域，原 WaveTune、GAC、Tensor Core 层次和 fallback 保留。PASS。 |
| DPS | Ch54:426/428、唯一 `2609-34380` marker；正文与 PRE literal 一致，新独立 `###` 已脱离 Review notes。但后两段旧 weight-as-stream 被该双模式标题吞入，待增加同级 `### 离线批量推理的跨 GPU 权重共享` 关闭作用域；不得改旧正文或因此重审未变源。Pending scope fix。 |
| BEHAVE | Ch66:1773/1775、唯一 `2609-34785` marker；正文与 PRE literal 一致，旧 ExecRetrieval/legal oracle 段保留。但后面旧 Dense process/QVal 段被新 Transaction `####` 吞入，待增加同级 `#### Dense Process Score 仍须校准未来 Return` 关闭作用域，旧段不改。Pending scope fix。 |

两处作用域问题已精确发回 root；此轮不是五项全部 POST PASS 或日级 FINAL。最终外部保留项已校准为 **七组**（不是前期口头六组）：Sonnet 日期、Google Publications 排序范围、Meta Blog 历史列表、Qwen 目录、Seed Blog、MiMo 五卡日期、MiniMax CLI 0.5.8 时间。它们均非正面 Coverage/Evidence。

### Scope fix 实际复验（2026-10-01T18:59:24+08:00）

root 已在 DPS marker 后、原离线 weight-as-stream 前实际加入 `### 离线批量推理的跨 GPU 权重共享`，并在 BEHAVE marker 后、原 Dense process/QVal 段前实际加入 `#### Dense Process Score 仍须校准未来 Return`。本人直接重读这两处实际上下文：两个旧分支正文未改，新增同级标题正确关闭新作用域；旧 committed bit-plane、离线跨 GPU、ExecRetrieval、QVal 与后续 Verification 边界均保留。DPS 与 BEHAVE 改为 **POST PASS**，本批五 I 的非写入作者 actual POST 至此全部 PASS；Argus 无 Books 写入，无虚构 POST。此结论仍不是日级 FINAL，等待正式 43 项 Report 与最后五 Theme 的独立 actual POST。

## 日级 FINAL：通过（2026-10-01T19:10:21+08:00）

本 reviewer 不是 [正式 Report](../../29/README.md) 作者，未修改该 Report、Books 或 LEARNING_STATE。此次完整读取正式 43 项版本的六部分，定点实读作者修正后的字段、来源范围和引用；将每项日期、贡献、评分、§4 支持/反侧、具体 owner/最终决定与本日未变化的独立审阅/实际 POST 链对照。**本窗研究和 Books 已达到合同的安全终态，允许作者同步状态为完成及 §6 复核结果；不是宣称所有原始来源正面 Coverage 通过或所有论文主张已被证明。**

### 实际验收范围与证据复用

| 范围 | FINAL 实际结果与边界 |
| --- | --- |
| 来源与窗口 | 14 个每日到期源均有正式行，未借此扫描 Weekly。AR Tue29 16、OS4、PF20 条 New+Cross 标题的越窗停止已补入正式正文；CL首140/DC76、CV首65/RO首45/PL18/IR首45/MA首45等是有限主题查漏，不是全分类关闭配额。机构有限入口停止与七组隔离自包含，没有把搜索零结果、空壳、无序首页或 HTTP 成功当完整召回。窗口未扩张。 |
| 家族/身份 | 实际表 43 行且 43 个唯一 primary 链接；40 arXiv + 3 官方事件。40 arXiv 采用 exact-v1，New 批次、官方公告日程和版本身份联合支持正常 09/29 08:00 北京时间；Submitted 和 feed 元数据不独自授首公开。三官方事件原 RSS 对应 08:00/03:00/03:00，均在半开窗口内。旧 Mon28 发现没有混入新分母。 |
| 贡献/分数/深度 | 43 项均有具体增量与 Design Delta/System Reach/Durability 分解，算术一致；未把 Evidence、可访问性、成本或 Books 处置加减入分。5–6 分整合项依据实际 owner 差额定点深入，三项仅报告标准完成；不为凑 I 改分或造缺口。 |
| §4 逐项证据 | 43 个唯一 primary 证据小节逐项覆盖表中家族。必要原文版本、核心方法、条件、直接反侧和最终采用/不采用理由均与保留的独立批次结果一致；未用最多三条综合分析替代逐项审阅。原 N1–19 的 root 非作者 source/owner/actual POST 未变，按合同复用，不谎称本人重新全文审阅。 |
| 40 实际 Books | N1–19 的有效非作者链复用；N20–23 与 Tail B 五 I 由本人直接 actual POST，新增21处的其余12 I 为 Tail A三项、本人四Theme与最后五Theme，由 Tail B 直接 actual POST，记录已实际读取。本人四Theme另有 root 非作者 source→owner PRE，不由本人自授 Source Gate。所有40实际 owner 链接存在；辅助逐家族定位得到21个单 marker、19对 start/end binding（含三官方），没有缺失/重复绑定。该一致性检查只是辅助，不替代已完成的实际两段、邻接与作用域审核。 |
| 三项仅报告 | SPIMOE、MTP profile、Argus 均保留新局部验证，不称整篇全文已有；具体旧 owner 原则与未构成长久新机制的原因已写。模拟/单请求/受控 interference 不授实芯服务、生产 SLO/false-alarm 或一般因果保证，不强造 Books diff。Argus 的 missing-tree abstain 不当健康证书。 |
| 七组外部终态 | Sonnet5.5 日期、Google Publications 历史切片、Meta Blog 历史列表、Qwen目录、Seed Blog、MiMo五卡日期、CLI0.5.8时间分别具身份/原始入口、缺失字段、不能采用原因、官方替代材料与定点重开范围；不进43分母、不写Books、不支撑无遗漏、安全或性能保证。七组是精确保留终态，不是 Coverage/Evidence 通过。 |

### 纠错/反证信号与分层负侧

必要安全/设计反证随 43 项实际拟采用命题审阅，未跳过 Australia/safety cases、Reset/ProbeQuant/World-Model Audit/LLaDA-Guard、ToolWait/Sparsity 的直接反侧。已读取并复用 Tail B 对 RiKFAD `2609.30342v2` 的必要方法/理论及实际 Ch28 既有命题对照：无明确重要 delta/纠错信号才关闭版本事件，不声明 v1/v2 全篇相同。Google CustomAgents 的“全体只读”共同概括已修正为 Flutter 可改代码、Firebase 可写 rules、只有 Play 示例只读，正式报告已实际落实。

其余明确排除项按来源/主题/理由作 **七个直接事件样本**：arXiv 三完整题摘（MEGATRON/JET/MorphAtt）、Lenfest 官方原始核心、Google CustomAgents 核心、MiniMax CLI0.5.9/0.5.8 精确 changelog；加上上述 RiKFAD v2 非作者必要核验的未变结果复用。样本分别覆盖硬件组合/峰值、成熟推理执行组合、边缘模型流水、合作/采用公告、既有插件包装、局部实现修复和相关生命周期信号的日期隔离。没有据标签排除相关安全 release，也没有将0.5.8误称无贡献。未检查的范围是其余明确范围外标题、全部原始分类摘要/无关附件及无信号的完整历史修订；这些未检查范围不被称全量验证或无遗漏。

### 实际问题修复与机器辅助

PRE/POST 发现的 copy-commit、per-query/head 合并、Planarian capture≠restore、non-prefix 近似/DP目标、CUTLASS静态合法≠执行coverage等窄修正已落正文；DPS/BEHAVE 的新标题吞入后续旧段已由同级标题闭合，旧正文保留。正式 Report 的审阅字段附注不符合严格枚举、§4旧19项待核残句、AR/OS/PF有限停止不够自包含与 ToolWait 引用定位四处具体问题均由作者最小修正，本人实读修后文本。

本人重跑 `python3 scripts/validate_research.py --report papers/2026/09/29/README.md` 通过；43行/43唯一小节/40I/3仅报告、评分算术及本地链接存在性辅助核无遗漏。Report/Books 相关未暂存 `git diff --check` 无输出；本人独占新附件 no-index 空白检查无诊断（exit=1只是新文件差额）。此前辅助定位脚本只接受单 `source-family`，误报旧19对 binding 缺失；实际读到合法的 semantic/source-family start/end 并修正解析后40均齐，没有因此重开或改写旧内容。root 另完成130本地链接/23owner和全未暂存差额检查；不将其或 marker 数量冒充语义验收。

**最终裁决：通过。** 不存在未处理的普通扫描、候选证据或必要 Books 工作；七组外部保留项按上述方式隔离。作者剩余的是据此同步正式状态/§6及实际完成 checkpoint，不得将裁决扩成全站正面 Coverage、全主张认证、复现实验或其他日期完成。本 reviewer 只写自己的三份独立文件，未 stage/commit/push，未动任何预先 staged/无关修改。
