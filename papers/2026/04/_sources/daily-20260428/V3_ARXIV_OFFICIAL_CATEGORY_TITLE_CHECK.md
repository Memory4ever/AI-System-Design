# 04/28 官方 arXiv 十二分类有界标题补检（V3，非候选分母）

本页只为 `SRC-ARXIV` 的约定主题入口补缺。北京时间固定窗是 `[2026-04-27 09:00, 2026-04-28 09:00)`。按当前 `docs/RESEARCH_SOURCES.md`，分类是标题检索/查漏入口，**不是全类摘要或全文审阅队列**。这里用 arXiv 官方 2026-04 月列表中相邻日连续 ID 的 `2604.22754–2604.24764` 段定位页；ID、OAI datestamp、v1 Updated、DOI created 任一字段单独都不证明逐篇 first-public，本页不冻结 owner 日或候选分母。官方[公告时钟说明](https://info.arxiv.org/help/availability.html)与相邻 ID/OAI 组合见本日 `V3_REVIEW_CHECKPOINT.md`。

## 实际入口和停点

每个入口为 `https://arxiv.org/list/<category>/2026-04?skip=<offset>&show=50`，读取页面显示的标题和 arXiv ID；同一 ID 跨分类去重。以下 offset 是**实际读取页**，部分分类的本类/交叉列表分段使 ID 在页面序列中重新从低到高排列，不能只扫一个连续 offset。带外页用于确认进入/离开本 ID 段，不逐篇扩成研究对象。

| 分类 | 官方月列表实际页 `skip` | 本 ID 段读到的分类记录 |
| --- | --- | ---: |
| [cs.CL](https://arxiv.org/list/cs.CL/2026-04) | 1450、1500、1550；2400、2450 | 169 |
| [cs.LG](https://arxiv.org/list/cs.LG/2026-04) | 1750、1800、1850、1900；3550、3600、3650 | 303 |
| [cs.DC](https://arxiv.org/list/cs.DC/2026-04) | 200、250、300、350 | 18 |
| [cs.AI](https://arxiv.org/list/cs.AI/2026-04) | 1100、1150、1200；4400、4450、4500、4550、4600、4650 | 368 |
| [cs.CV](https://arxiv.org/list/cs.CV/2026-04) | 2300、2350、2400、2450、2500；3150、3200 | 239 |
| [cs.RO](https://arxiv.org/list/cs.RO/2026-04) | 600、650；900、950 | 63 |
| [cs.AR](https://arxiv.org/list/cs.AR/2026-04) | 100、150、200 | 16 |
| [cs.PL](https://arxiv.org/list/cs.PL/2026-04) | 50、100 | 5 |
| [cs.OS](https://arxiv.org/list/cs.OS/2026-04) | 0（该月目录共 37 条、所读页全量） | 0 |
| [cs.PF](https://arxiv.org/list/cs.PF/2026-04) | 50；0 页作边界抽查 | 1 |
| [cs.IR](https://arxiv.org/list/cs.IR/2026-04) | 300、350、450；400 页作带外边界抽查 | 31 |
| [cs.MA](https://arxiv.org/list/cs.MA/2026-04) | 300；250 页作带外边界抽查 | 16 |

本段共 **1,229 条分类记录、按 ID 去重 845 个身份**；旧 V2.1 的 111 retained 身份在上述可见页中命中 104 个。差集不能直接叫“漏稿”：有未注册分类、交叉列表、版本/分类变化及本段日期例外；845 也不是 845 个摘要或候选。标题主题浏览聚焦模型架构/训练、推理/缓存/通信、Agent/RAG/评价、多模态生成与 VLA；传统语言学、一般控制、领域预测、无大模型关联硬件题目只保留可检索目录，不逐篇准入。月列表按分类与 ID 段定位，不提供逐篇公告秒级时刻；旧 ID 的当月 cross-list/revision 仍由 OAI/具体源例外路由，不能从本表归窗。

对旧 `retained` 111 身份与其 receipt 原始 `categories` 作反向联接，**恰有 7 个完全不属注册十二分类**：`2604.22935`（cs.CR）、`.23374`（cs.CR）、`.23455`（cs.SE）、`.23711`（cs.CR）、`.23932`（cs.NI）、`.24118`（cs.CR）、`.24579`（cs.SE）。这解释了“111 中只在十二分类页见 104”的已知差额；七项均已由旧身份库回收且有各自题摘/必要贡献队列，不能把它们当作本次标题查漏的漏读，也不能从分类不匹配推它们不值得准入。此反查只解释**这 111 个旧线索**的分类差集，不证明另 845 身份外没有高信号新稿。

## 定点反向发现与前分母边界

| 身份 | 本次官方标题/题摘与现有 owner 的最小判断 | 当前状态 |
| --- | --- | --- |
| [2604.23519v1](https://arxiv.org/html/2604.23519v1) Multi-Plane HyperX | `cs.LG` 标题补检找回旧 submittedDate 库存外的同段 ID；官方 §2–4 是多平面 HyperX 的端口/交换机规模和假定光模块单价下的拓扑成本。没有模型阶段通信流量、拥塞、并行 placement 或训练吞吐测量，不能把 65K NIC 的静态价格表写成 Ch36 的 AI workload 选型收益。 | 具名范围/贡献前关闭；保留为拓扑线索，不评分，不声称已证明首公开日。 |
| [2604.24222v1](https://arxiv.org/html/2604.24222v1) MEMCoder | **旧 ledger 标题为 `Learning from Execution: Self-Evolving Memory for Private-Library Code Generation`，官方 exact-v1 题名为 `MEMCoder: Multi-dimensional Evolving Memory for Private-Library-Oriented Code Generation`。** v1 摘要/§I 把静态 API 文档仅给定义，与任务级多 API 协同、API 参数/边界约束两类 usage guideline 区分；execution feedback 更新 memory。需定点比较 Ch81 的执行反馈 workflow 与 Ch84 的私有 API/环境契约，不能沿用旧泛化“单域局部方法”关闭或凭题名自动保留。 | **恢复为 1 条待贡献消歧线索**；未评分、未写 Books、未定公告日。 |
| [2604.24391v1](https://arxiv.org/html/2604.24391v1) FreqCache | v1 摘要/§3–4 明确 VLN 跨视角视觉 token 重用失效、频域边缘/时变与预算调整。需要与现有视觉 cache 的有效性/失效检测及动作条件相邻命题比：若只是特定 VLN 频域 sensor 的有限实现而无新的 state/control owner，则具名关闭；不能凭 1.59× 或“optimal”摘要直接采用。 | **1 条定点贡献消歧线索**；不自动把领域加速升为通用 Books 增量。 |
| [2604.24608v1](https://arxiv.org/html/2604.24608v1) RouteHead | v1 摘要/§3 是固定 LLM 的 query hidden-state→attention-head subset router，离线 pseudo-label 搜索后训练稀疏选择；它优化单一 reranker 的内部打分，不是 retriever、evidence source 或 final-answer authority 的新 owner。Ch76 已写静态 head/权重选择及 query-conditioned retriever 架构，但尚不能据此认定覆盖**同一 reranker 的逐查询 head subset 控制**，需定点核其训练/开销与现章差异。 | **1 条定点贡献消歧线索**；不能因 head-level 新颖自动保留，也不能以已有 query-conditioned 检索直接前关闭。 |

本页新增的是**3 条普通待消歧**（24222、24391、24608），不是 3 个正式候选；23519 是具名前关闭。其他月页高信号题名如 `2604.23150` 多节点 MoE、`2604.24013` CommFuse、`2604.24088` TACO、`2604.24715` HyLo 已在本日旧111/晚段独立队列，不重复计身份。下一步只对受影响线索做 exact-v1 必要段与实际 Books 对照，不把 845 个标题无差别全文化。来源表仍要分别记录其他机构与 arXiv 公告/date 例外；本文件不是 SRC-ARXIV 或全日 Gate 通过。

## 三条新线索的必要原文与实际 owner 定点判断（作者提案，待独立准入）

- **24222 / Ch81 primary，Ch84 handoff。** [官方 exact-v1](https://arxiv.org/html/2604.24222v1) §III 的 oracle 静态 API 文档在 NumbaEval 的 Qwen2.5-Coder-7B pass@1 仅 26.15→27.70；§IV 将可执行反馈形成的 task-level 跨 API 协同与 API-level 参数/边界 guideline 分库存，检索时与静态文档并用，反馈后对 guideline 做 discard/delete/add/权重更新。§VI-C 的去 task memory、去 API memory 和仅 FIFO 累积消融同条件下均退步（NdonnxEval pass@5：full 69.42、无 task 58.66、无 API 38.12、FIFO 39.09）。Ch81 现有 evaluator-driven search 与 Ch84 Skill admission 已规定可执行 outcome、版本及回滚，但未明确**静态 API 规格即使 oracle 全给仍不等于跨 API 用法和参数边界经验；两种执行导出的记忆应分别索引、更新、验收**。故作者建议贡献准入，不是“私有库新应用”自动入选；下一层须核静态 RAG 同预算、反复使用是否泄漏测试、额外 token/reflector 成本，不能从两库消融断言自动记忆普遍可靠。这里未评分、未写 Books，先核本日首次公告归属。
- **24391 / Ch26 primary，Ch14 handoff。** [官方 exact-v1](https://arxiv.org/html/2604.24391v1) §4.1–4.4 把上一视角 token 的**空间对应是否仍有效**与**当前关键边缘必须刷新**分开：频谱幅度判大场景切换、相位相关估位移并限定重叠区，block DCT 高频能量标记刷新，再按频谱熵选 reuse 预算；不是只调一个缓存阈值。§6.3 去位移模块、去 edge 模块、固定预算分别退步；单 A100/InternVLA-N1/R2R-CE 主表 full SR63.0、无缓存64.3，速度 637→401ms/step，不能称精度无损或普遍实时安全。Ch14 已写可撤销视觉选择/full-KV 回退，Ch26 已写 dense observation revision 和控制时钟，但未具体承载**跨视角 token 重映射后才准许复用**及新视野/边缘强制重算的双条件。作者建议作为受限 VLA cache 有效性分支进入候选；频域 sensor 的相关性不是物理安全真值，尚需独立准入/日期和更完整性能边界审阅，不写 Books。
- **24608 / Ch76 primary。** [官方 exact-v1](https://arxiv.org/html/2604.24608v1) §3 从单 head 质量筛 top-K、逐 query 前向/交换搜索不超过 P 个 head 得伪标签，再用冻结 LLM query hidden state 与 head embedding 训练稀疏 multi-hot router；推理只对选定 head 的 query→document attention 汇总排序。Ch76 当前 `SF-2604-17237` 有**训练后固定 head/readout/截层**，并无同一 reranker 对不同 query 动态选择 head set；这是具体部署 artifact/训练标签分支，不是一般 query-conditioned retriever。§4 BEIR Llama3.2-3B 平均 nDCG@10 49.6 vs 静态 QRhead48.6，但 BRIGHT code/math 类常低于 Corehead，且训练在 MSMARCO，不能称跨域普胜；实验 top-200/100 BM25、不同生成式 reranker 候选窗口不一，也未证明只选输出 head 就能省完整 attention 前向或线上 P99。作者建议贡献准入并核 bounded score/Books 差异；独立校准与公告日仍待完成。

以上三项是从官方标题补检**新增的作者准入提案**，不是已经过非作者审阅的 3 个冻结候选，更不是 3 项 Integrate。分类月页只负责发现身份；单篇评价均绑定官方 exact-v1。

三项的旧官方元数据 receipt 显示 v1 `Updated` 分别为 `24222: 2026-04-28T01:27:11Z`、`24391: 01:39:22Z`、`24608: 01:56:26Z`，均在本窗 09:00 北京时间截点之后；DataCite 初建时间更晚，`24222` 的当前 OAI 记录为空。它们的 ID 位于有界连续公告段，**但不能只凭这个区间把晚字段逐篇推回 08:00～09:00**。若贡献准入通过，先保留单篇 Date Hold，定点找该批官方 New/Cross 列表或更早可读 artifact 的明确证据；晚字段也不单独证明它们实际在 09:00 之后首次公开。此日期状态不改变上述作者侧机制判断。
