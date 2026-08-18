# Daily Research — 2026-08-11

**Archive Date:** 2026-08-11（Asia/Shanghai）

**Coverage Window:** 2026-08-09 14:53 ～ 2026-08-11 14:53（Asia/Shanghai）

**Archive Clock:** Tuesday；只生成 Daily，不生成当前周 provisional Weekly。

**Status:** Daily Complete；Books Integration Evaluated — No Change

## Executive Summary

今天没有已公开、可核验且足以立即改变核心书稿结论的模型公司 Research 或 AI Infra release。学术来源中有三项值得保留的机制证据：

1. **SwiftQK** 把 Tensor Parallel 下 layerwise QK-Norm 的通信问题，从交换完整 Q/K shard 转化为交换 RMS 所需的局部平方和；它说明 collective payload 应由数学充分统计量决定，而不是机械恢复完整 tensor。
2. **Beyond Routing** 在保持 Top-K expert identity、执行集合与总 router mass 不变的条件下，只学习已执行 expert outputs 的 aggregation 权重；它把“选择谁执行”与“多大程度相信已执行结果”分成两个可独立检验的决策。
3. **QueryProof / WarehouseReliabilityBench** 把 analytics Agent 的正确性从 SQL execution accuracy 扩展到 answer、clarify、abstain、refuse 的行为契约，并把 deterministic semantic/catalog gates 放在模型输出之后；但其 7B 与 32B 对比是系统比较，不是模型尺寸因果实验。

三项都属于新近单一 primary source，evaluation contract 仍窄，尚未形成跨来源稳定结论。今天只写入 Daily，等待 Sunday Weekly 的去重、演进重建与第二证据检查；不修改 `books/`。

## 来源覆盖

### 1. 模型与研究机构

- 检查窗口内主要模型与研究机构的官方 Research / Blog / model report 更新。
- 未发现同时满足“事件日期在窗口内、存在 primary technical evidence、与 AI System Design 长期知识树直接相关”的新增候选。
- 搜索结果中的转载、产品宣传、旧报告重新索引不进入候选表。

### 2. arXiv / 学术来源

- 检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC` 的新提交，并以 arXiv metadata 的 first-public date 为事件日期，而不是列表出现日期。
- Google Scholar、OpenAlex、DBLP 用作发现与 metadata 交叉检查入口；正文与结论只依赖下列 arXiv primary sources。
- 深入阅读不超过三项：SwiftQK、Beyond Routing、QueryProof / WarehouseReliabilityBench。

### 3. AI Infra 与工程项目

- 检查 GitHub Releases、官方工程文档和项目公告。
- 未发现能够在窗口内完成 release tag、文档、代码路径和 workload contract 联合核验的高价值新增事件。
- 搜索页显示时间与 tag 时间不一致的条目不计为已验证 release。

## 候选评分

评分范围为每项 1～5 分，总分 30。

| 顺序 | 候选 | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence Level |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SwiftQK | 2026-08-10 | 5 | 5 | 4 | 5 | 5 | 4 | 28 | E2 — primary paper；无独立复现 |
| 2 | Beyond Routing / FDAA | 2026-08-09 | 5 | 4 | 4 | 4 | 5 | 4 | 26 | E2 — primary paper；单作者、窄模型与数据条件 |
| 3 | QueryProof / WarehouseReliabilityBench | 2026-08-10 | 4 | 4 | 5 | 4 | 5 | 5 | 27 | E2 — paper + public artifact links；本次未独立运行 artifact |

## Deep Analysis

### 1. SwiftQK：不要交换完整 tensor，只交换归一化真正需要的统计量

**Why**

Layerwise QK-Norm 的 RMS 因子依赖一个 query/key hidden vector 的全局平方和。Tensor Parallel 把 hidden 维分到多个 ranks 后，朴素实现会 AllGather 完整 Q/K，再做归一化；这保持语义正确，却把 `O(H)` payload 放入每层关键路径。

**Principle**

分布式算子不应默认恢复完整 tensor；先从算子数学语义推导跨 rank 的最小充分统计量。对 RMS 而言，每个 rank 的局部平方和可加，最终只需共享标量统计量。

**Mechanism**

各 rank 对本地 Q/K shard 累加平方和，通过 peer-to-peer 标量归约得到全局 RMS factor，同时把独立的 elementwise weight multiplication 与通信重叠，最后在本地 shard 上应用统一因子。论文还使用受限 persistent grid，让 resident blocks 以 stride 处理 tokens，以避免 kernel 内 peer synchronization 因过量 blocks 形成 deadlock。

**Trade-off**

- 收益依赖 normalization axis、TP layout 与通信/计算重叠空间，不代表所有 Norm 都能使用同一方案。
- persistent kernel 引入 occupancy、launch configuration、peer-ordering 与拓扑敏感性。
- 论文在 2×RTX 3090 micro-profile、4/8×A100 NVLink、OLMoE 7B、OLMo2 13B、OLMo3 32B 和 ShareGPT workload 上评估；不能把作者的 latency、TPOT 或 throughput 数字外推到其他 GPU、PCIe 拓扑、精度或 SLO。

**Connection**

ROADMAP owner 倾向第 33 章 Tensor Parallel；第 32 章只保留“由 collective semantics 推导最小 payload”的通用原则，第 45～46 章接 kernel/runtime 映射。

**Evolution**

完整 tensor materialization → 计算局部可加统计量 → 只交换标量 → 与本地 elementwise work 重叠。它不是用新 collective 否定 AllGather；当下游确实需要完整 tensor、统计量不可分解或 kernel 复杂度不值得时，AllGather 仍合理。

### 2. Beyond Routing：Top-K dispatch 与 expert commitment 不是同一个决策

**Why**

传统 sparse MoE router 的同一组 scores 同时决定 Top-K expert selection 和选中 outputs 的 aggregation weights。Top-K 排名足以完成 dispatch，却未必提供对最终 LM objective 最合适的相对 commitment。

**Principle**

应把离散资源决策与已执行结果的连续组合分开验证：dispatch 决定计算和通信路径，aggregation 决定这些结果如何影响 residual stream。

**Mechanism**

FDAA 固定 native Top-K expert IDs、执行集合和选中 router mass，只基于 token state、已计算 expert outputs、native weights、expert IDs 与 layer embedding 预测 residual commitment scores；重加权后仍保持总 selected mass。最后一层零初始化，使初始状态在数值误差范围内复现原模型。训练冻结 backbone、router 与 experts，只优化约 30 万参数的 head，目标是 next-token cross entropy 加 KL 与 residual regularization。

**Trade-off**

- 严格 fixed-dispatch protocol 很好地隔离了 aggregation 因果因素，但没有证明改变 dispatch 不会更优。
- OLMoE 实验主要使用 sequence length 96、batch 1，并在少数 target layers 上干预；DeepSeek-V2-Lite 是单 seed replication。
- WikiText-only policy 对 C4 的迁移不成立，说明 token adaptivity 不等于 domain generality。
- 新 head 增加训练、版本、checkpoint compatibility 与 inference kernel/fusion 负担。

**Connection**

第 21 章当前已把 router 写成“选择 expert 并加权组合”，但尚未把 selection、execution 与 commitment 明确拆成三个 contract。该论文能解释潜在缺口，不过仍是 Experimental，暂不写入正文。

**Evolution**

单一 router scores 同时承担 selection 与 weighting → 固定 dispatch 下审计 aggregation mismatch → 轻量 head 校准 commitment。旧设计仍具有更低复杂度、更自然的联合训练与更简单 serving path；新设计只在 mismatch 稳定、跨域成立且新增状态可管理时值得采用。

### 3. QueryProof：业务正确性是行为契约，不是 SQL 能执行

**Why**

现实 analytics 请求并不总有唯一正确 SQL。歧义、数据缺失、schema drift 和禁止操作要求系统 clarify、abstain 或 refuse；只在“存在正确 SQL”的样本上测 execution match，会把错误回答但成功执行计为成功。

**Principle**

模型适合提出候选解释与 query；可由 domain state 决定的约束，应由版本化 semantic layer、physical catalog 和 deterministic verifier 裁决。Evaluation 必须测 false success，而不只测 answer coverage。

**Mechanism**

WarehouseReliabilityBench 冻结 400 个合成任务与两个 warehouse，约一半任务没有正确 SQL，而有明确行为 contract。QueryProof 用 semantic layer 和 catalog 识别 ambiguity/answerability，静态检查 candidate，执行后再检查 filters、period、non-empty 与 impossible values，最后才允许返回答案。

**Trade-off**

- 合成 warehouse 提供可执行 ground truth 与可复现 seed，但牺牲生产外部有效性。
- 7B system 获得完整 scaffold，而 32B baseline 是 direct prompt；论文自己明确这是 system comparison，不能归因为小模型优于大模型。
- 学得的 routing/confidence 在 test 上因过度 abstain 而退化，手工 heuristic 反而更好；rules 也需要维护、覆盖测试和版本治理。
- 本次未独立运行公开 artifact；论文报告的数字只作为作者实验结论。

**Connection**

第 62 章已覆盖 executable verifier、missing/invalid/abstain state 与 judge 不能替代 truth；第 77 章已区分模型决策与 deterministic workflow state。该工作主要提供受限 domain case 和更清晰的 business-behavior contract，尚未改变两章结论。

**Evolution**

SQL exact/execution match → execution-grounded checking → semantic/catalog-aware behavior contract → selective answer/clarify/abstain/refuse。新阶段没有淘汰 execution accuracy；对明确、可回答任务它仍是必要局部指标，但不再足以代表端到端 business truth。

## Evidence Level 与事实边界

- **官方事实 / primary-source metadata：** 三项 arXiv v1 的提交日期、方法描述、实验设置和作者公开的 artifact 链接。
- **论文实验结论：** 只在各自论文披露的模型、硬件、数据、precision、length、batch、concurrency 与 baseline 范围内成立。
- **社区观点：** 本 Daily 未使用社区评论形成结论。
- **本项目推断：** “最小充分统计量”“selection/execution/commitment 三层 contract”“模型提出、规则裁决”是对多章知识树的系统抽象，不是论文声称的普适标准。
- **尚未验证：** 三项均无本次独立复现；QueryProof artifact 未运行；SwiftQK 未见跨互联/跨厂商验证；FDAA 的跨模型、跨层和长上下文一般性未知。

## 知识树位置

| 候选 | 主 Owner | 相邻章节 | 当前覆盖判断 |
| --- | --- | --- | --- |
| SwiftQK | Ch33 Tensor Parallel | Ch32 Distributed Training；Ch45 Kernel；Ch46 vLLM | 现有章节已有 TP collective 与 layout 原则；缺少 QK-Norm 受限案例，但证据尚不足以沉淀 |
| Beyond Routing | Ch21 MoE | Ch29 RL/optimization；Ch36 Megatron；Ch40 Decode | 现有章节合并描述 selection 与 weighting；潜在机制缺口，Status: Experimental |
| QueryProof | Ch62 Evaluation System | Ch63 Monitoring；Ch72 RAG；Ch77 Workflow | 核心原则已覆盖；新增的是 analytics domain case 与更严格 failure taxonomy |

## Recommended Action

| 候选 | 决策 | 原因 |
| --- | --- | --- |
| SwiftQK | Refine Ch37 / Experimental | Sunday 完成 owner/adjacent chapter 去重后，确认“由 consumer semantics 推导最小 collective payload”是现有 TP 主线的机制缺口；保留有限 hardware contract |
| Beyond Routing | W32 retroactive / Emerging / Experimental | first-public date 为 2026-08-09；提供重要机制解释，但跨域失败和窄 intervention 边界尚不足以改写 MoE 主线 |
| QueryProof | No Change — Already Covered；Weekly 保留案例 | Ch62 与 Ch77 已拥有 verifier/workflow 原则；非 matched-scaffold 比较不得进入通用结论 |

**Books Integration Decision:** 当日不修改 `books/`；Sunday W33 复核后，SwiftQK 已 `Refine — Existing Argument /
Experimental` 至 `TRAIN-TENSOR-PARALLEL`（Current Ch37，Legacy Ch33）。FDAA 保持 W32
`Emerging / Experimental`，QueryProof 保持 `No Change — Already Covered`。

当日没有立即修改核心知识库；Sunday 的跨日/章节复核确认 SwiftQK 达到 refine 门槛。

## Ignored Noise

- `Training Variable Long Sequences with Data-Centric Parallel`（arXiv:2608.07524）虽出现在当日列表，但 v1 first-public date 为 2026-07-14，属于旧内容重新索引，不作为 2026-08-11 事件。
- `Controlled Memory Interference`（arXiv:2608.07622）v1 为 2026-08-07；`An AI Scientist that Doesn't Drift`（arXiv:2608.07542）v1 为 2026-07-30，均超出窗口。
- `ElastiCo`（arXiv:2608.07971）与 `OasisKV`（arXiv:2608.08097）v1 为 2026-08-08，应按真实事件日去重，不回填到今天。
- GitHub 聚合搜索中出现但无法把 tag date、release notes、文档与代码路径共同核验的条目，不计为候选。
- 缺少 workload contract 的 benchmark 宣传、媒体转述和无 primary source 的排行榜变化被过滤。

## Repository Changes

- 新增 `papers/2026/08/11/README.md`。
- 完成三项 primary-source 阅读、评分、事实边界、知识树映射与 Books 决策。
- 未修改 `books/`、`ROADMAP.md` 或 `docs/DECISIONS.md`。
- 历史 Weekly forward cursor 的 W23 状态独立维护；本轮完成 SDPG 与 M3Eval 的 v1、appendices、当前
  official artifact surface 和相邻章节审计，使 W23 达到 17/29 Full Source Reviews；Continual Experience
  Internalization 等 12 个未完成 families 因 arXiv primary-paper 与相关 GitHub artifact domain 被当前访问策略
  拒绝，逐项转入 blocked backlog，使 current-review pending 清零并按用户规则把 cursor 推进到 W24；M3Eval
  因 memory/perception/position/scorer confound 且相关原则已由 Ch62/22 具体拥有，暂定
  `No Change — Already Covered / Experimental Case`；W23 discovery/Historical Evidence Gates 仍为 Open，
  Historical Books Gate 仍关闭，
  本 Daily 不把历史 blocked backlog 误计为完成阅读。
- forward cursor 随后完成 W24 queue disposition：3/34 `20+` Full Source Reviews 保留，31 个依赖
  arXiv primary paper（部分还需 GitHub artifact）的 families 因当前保存的访问策略转入
  `Unverified / Blocked Backlog`，0 current-review pending；cursor 推进到 W25，但 W24 discovery/
  Historical Evidence Gates 与 Historical Books Gate 均未关闭。
- forward cursor 继续完成 W25 queue disposition：4/31 `20+` Full Source Reviews 保留，27 个未读
  families 因同一 primary-paper/artifact domain 访问限制进入 `Unverified / Blocked Backlog`，0
  current-review pending；cursor 推进到 W26，但 W25 discovery/Historical Evidence Gates 与 Historical
  Books Gate 均未关闭。
- forward cursor 继续完成 W26 queue disposition：4/37 `20+` Full Source Reviews 保留，33 个未读
  families 因同一 primary-paper/artifact domain 访问限制进入 `Unverified / Blocked Backlog`，0
  current-review pending；cursor 推进到 W27，但 W26 discovery/Historical Evidence Gates 与 Historical
  Books Gate 均未关闭。
- forward cursor 继续完成 W27 queue disposition：31 个评分行对应 30 个 unique families，9 个 unique
  Full Source Reviews 保留，21 个未读 families 因同一 primary-paper/artifact domain 访问限制进入
  `Unverified / Blocked Backlog`，0 current-review pending；Seed2.0 duplicate relation 保持闭合，cursor
  推进到 W28，但 W27 discovery/Historical Evidence Gates 与 Historical Books Gate 均未关闭。
- forward cursor 继续完成 W28 queue disposition：7/21 Full Source Reviews 保留，14 个未读 families
  因同一 primary-paper/artifact domain 访问限制进入 `Unverified / Blocked Backlog`，0 current-review
  pending；cursor 推进到 W29，但 W28 discovery/Historical Evidence Gates 与 Historical Books Gate
  均未关闭。
- forward cursor 继续完成 W29 queue disposition：7/26 Full Source Reviews 保留，19 个未读 families
  因同一 primary-paper/artifact domain 访问限制进入 `Unverified / Blocked Backlog`，0 current-review
  pending；cursor 推进到 W30，但 W29 discovery/Historical Evidence Gates 仍 Open，Historical Books
  Gate 继续关闭；本轮未修改 Books。
- forward cursor 继续完成 W30 queue disposition：9/25 Full Source Reviews 保留，16 个未读 families
  因同一 primary-paper/artifact domain 访问限制进入 `Unverified / Blocked Backlog`，0 current-review
  pending；cursor 推进到 W31，但 W30 discovery/Historical Evidence Gates 仍 Open，Historical Books
  Gate 继续关闭；本轮未修改 Books。
- W31 Live Weekly 重新验收通过：24 个评分行的六维总分可复算，7/7 Daily、跨周去重、Books
  decision、标题与代码围栏一致，无需改写正文；forward cursor 随后进入最新已结束的 W32。
- 新增 `papers/2026/08/09/README.md`，把 Beyond Routing 按 first-public date 从本日 discovery node
  回写 W32；该 Daily 随后于 2026-08-12 完成 coverage repair。W32 现为 7/7 Daily，48 个 Daily
  score rows 去重为 44 个 unique families，18 个 Full Source Reviews 已完成；15 篇 paper 与 KServe
  mechanism review 进入 `Unverified / Blocked Backlog`，6 个 8 月 9 日 families 为 Full Source Review
  Pending，ElastiCo / OasisKV 为 unscored discovery-only gaps。Tangent 已 refine Ch62；W32 Evidence
  Gate 保持 Open，Historical Books Gate 继续关闭。
- fixed-source replay 补充核验 vLLM 两个工程来源族：incremental MoE expert offloading 以
  2026-03-16 open PR 为 first-public owner，完整 Source Review 回拨 W12；W13 的 2026-03-26 RFC
  仅保留为 architecture follow-up。`TRITON_MLA_SPARSE` 由 2026-03-24 issue 与 2026-03-29 open PR
  联合定义并写入 W13 Full Source Review。W12 当前为 49 个来源族、48/48 `20+` reviews；W13 当前
  为 26 个来源族、22/22 `20+` reviews。两项均保持 Experimental/open-PR 边界；Hugging Face 历史
  papers 页的访问阻断被显式记录，因此 W13 Discovery Gate 与全历史 Books Gate 继续关闭。
- 全历史六维评分复算发现 W24 的 FastContext 撤稿记录把 Longevity 写成超出量表的 `0`；已按
  1～5 分规则改为 1，总分由 17/30 更正为 18/30。它仍是唯一的低分 withdrawn provenance record，
  不改变 W24 的候选数量、分档、Evidence Gate 或 Books 决策。
- W14 的 HippoCamp official arXiv primary text 已重新可读；本轮完成 benchmark construction、最小支持
  文件集与 Atomic Unit schema、annotation/QC、三种 evaluation regime、metrics、judge audit、failure
  analysis 和相关 Appendix 的全文审计。W14 recorded queue 因而达到 24/24 Full Source Reviews、0
  blocked、0 pending；最终 disposition 为 `No Change — Already Covered / Experimental Evaluation Case`，
  因 Ch62/72/73/68 已具体拥有其长期原则。W14 fixed-source Discovery Gate 仍为 Open，Historical Books
  Gate 仍为 Closed，本轮未修改 Books。
- Sunday W33 回读 Ch36～38 后，SwiftQK 已写入 Current Ch37（Legacy Ch33）；新增的是 algebra-first
  sufficient-statistic communication 与 AllGather 共存边界，不保留作者 speedup headline。

## Open Questions

1. SwiftQK 的 scalar-statistic path 在 PCIe、跨节点或非 NVIDIA collective/runtime 中是否仍能覆盖同步成本？
2. FDAA 在更长 context、更多 MoE backbones、不同 Top-K 与多层同时干预时能否保持收益？
3. QueryProof 在 matched scaffold、真实 warehouse、不同 semantic-layer completeness 下的 false-success / false-refusal 边界如何变化？
4. 三项工作能否在本周形成第二 primary source、独立 artifact 结果或明确的技术演进链？
5. vLLM 两条 open-PR source families 在 merge/rebase 后，机制、测试覆盖与 workload contract 会发生哪些变化？
6. HippoCamp 的三种 evaluation regime 在 matched permissions、parallelism、tokens/calls、wall-clock 与
   repeated-run contract 下是否保持相同 failure ordering；Atomic Unit scorer 如何在不泄漏 personal media
   时开放独立审计？

## Sources

访问日期均为 2026-08-11（Asia/Shanghai）。

1. SwiftQK, arXiv:2608.09160v1, first public 2026-08-10: https://arxiv.org/abs/2608.09160
2. SwiftQK HTML full text: https://arxiv.org/html/2608.09160
3. Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts, arXiv:2608.08853v1, first public 2026-08-09: https://arxiv.org/abs/2608.08853
4. Beyond Routing HTML full text: https://arxiv.org/html/2608.08853
5. Business Truth, not SQL Accuracy: A Rule-Gated 7B Analytics Agent Outperforms a Direct-Prompted 32B Baseline, arXiv:2608.09254v1, first public 2026-08-10: https://arxiv.org/abs/2608.09254
6. Business Truth HTML full text: https://arxiv.org/html/2608.09254
7. arXiv Computer Science — Artificial Intelligence recent submissions: https://arxiv.org/list/cs.AI/recent
8. arXiv Computation and Language recent submissions: https://arxiv.org/list/cs.CL/recent
9. arXiv Machine Learning recent submissions: https://arxiv.org/list/cs.LG/recent
10. arXiv Distributed, Parallel, and Cluster Computing recent submissions: https://arxiv.org/list/cs.DC/recent
11. HippoCamp, arXiv:2604.01221v1, first public 2026-04-01: https://arxiv.org/abs/2604.01221
12. HippoCamp official project page: https://hippocamp-ai.github.io/
