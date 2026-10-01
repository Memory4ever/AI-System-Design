# 2026-09-22 arXiv 有限恢复 checkpoint — 2026-09-27

- 作者恢复：`weekly39_discovery`。只处理来源身份、公开批次与准入建议；不是独立 Day Gate，不做 Books、不改正式日报。
- 目标窗口：`[2026-09-21T09:00:00+08:00,2026-09-22T09:00:00+08:00)`。本次查询执行于 2026-09-27；不按恢复日移动窗口。
- 已读当前 AGENTS、统一 Prompt、研究/来源/Report 合同、ROADMAP 与 09/22 checkpoint，以及正式 README 和三份旧 `_sources`。旧 733/665/68 汇总只作恢复线索，不继承全量复核结论。

## 1. 公告标签对齐：先证明，后纠偏

[官方 availability](https://info.arxiv.org/help/availability.html) Announcement Schedule 使用 US Eastern：Friday14:00～Monday14:00 的常规公告为 Monday20:00；2026-09-21 是 EDT（UTC−04）。故本窗需要 Monday21 20:00EDT＝Tuesday22 00:00UTC＝09/22 08:00+08 的批次。Sunday20 20:00EDT＝Monday21 08:00+08 在目标窗之前。提交/updated 字段不是公开时间，本文不按 submission history 自动归日。

为排除 recent 标签是 Eastern 公告日而 new 标签是 UTC 日的可能，实际对齐同一时刻两个官方入口：

- `https://arxiv.org/list/cs.CL/new`：`Showing new listings for Friday,25 September 2026`；New86、Cross40、Replacement65。这里只比较 New/Cross 的126身份，不混入Replacement。
- `https://arxiv.org/list/cs.CL/recent?skip=0&show=2000`：`Fri,25 Sep 2026 (showing126 of126 entries)` 的126身份与 /new 的New/Cross **集合完全一致**；`Thu,24 Sep2026 (showing105 of105 entries)` 与上述126身份的交集为0。排序不同不构成日期不同。
- 官方规则没有 Friday20:00 常规公告，这个 Friday25 同名批次对应 Thursday24 20:00EDT→Friday25 08:00+08。因此不能把 recent Mon21 标签解释成 Monday21 20:00EDT。目标是 recent **Tue22** 组。此结论来自ID集合对齐与官方公告clock，不来自 submitted 或 weekday直觉。

原字段中的空格在上面为阅读压缩；完整原始标题于表2保留。具名ID集合供机器复查：

### newFriday25

```text
2609.28475 2609.28479 2609.28487 2609.28565 2609.28614 2609.28653 2609.28673 2609.28703 2609.28713 2609.28727
2609.28739 2609.28747 2609.28757 2609.28758 2609.28778 2609.28784 2609.28826 2609.28845 2609.28854 2609.28877
2609.28988 2609.29001 2609.29015 2609.29043 2609.29056 2609.29075 2609.29090 2609.29102 2609.29123 2609.29131
2609.29146 2609.29183 2609.29230 2609.29233 2609.29245 2609.29251 2609.29276 2609.29278 2609.29328 2609.29333
2609.29349 2609.29362 2609.29370 2609.29371 2609.29390 2609.29397 2609.29410 2609.29418 2609.29421 2609.29428
2609.29429 2609.29444 2609.29445 2609.29448 2609.29474 2609.29479 2609.29494 2609.29496 2609.29504 2609.29507
2609.29508 2609.29509 2609.29511 2609.29528 2609.29549 2609.29559 2609.29573 2609.29578 2609.29584 2609.29601
2609.29607 2609.29618 2609.29626 2609.29633 2609.29636 2609.29657 2609.29672 2609.29680 2609.29682 2609.29684
2609.29703 2609.29709 2609.29718 2609.29733 2609.29735 2609.29769 2609.29792 2609.29798 2609.29800 2609.29802
2609.29807 2609.29828 2609.29837 2609.29845 2609.29848 2609.29855 2609.29913 2609.29928 2609.29933 2609.29952
2609.30005 2609.30009 2609.30012 2609.30030 2609.30048 2609.30063 2609.30071 2609.30074 2609.30075 2609.30087
2609.30094 2609.30100 2609.30121 2609.30130 2609.30137 2609.30147 2609.30151 2609.30160 2609.30167 2609.30184
2609.30199 2609.30226 2609.30227 2609.30238 2609.30243 2609.30250
```
### recentFriday25

```text
2609.28475 2609.28479 2609.28487 2609.28565 2609.28614 2609.28653 2609.28673 2609.28703 2609.28713 2609.28727
2609.28739 2609.28747 2609.28757 2609.28758 2609.28778 2609.28784 2609.28826 2609.28845 2609.28854 2609.28877
2609.28988 2609.29001 2609.29015 2609.29043 2609.29056 2609.29075 2609.29090 2609.29102 2609.29123 2609.29131
2609.29146 2609.29183 2609.29230 2609.29233 2609.29245 2609.29251 2609.29276 2609.29278 2609.29328 2609.29333
2609.29349 2609.29362 2609.29370 2609.29371 2609.29390 2609.29397 2609.29410 2609.29418 2609.29421 2609.29428
2609.29429 2609.29444 2609.29445 2609.29448 2609.29474 2609.29479 2609.29494 2609.29496 2609.29504 2609.29507
2609.29508 2609.29509 2609.29511 2609.29528 2609.29549 2609.29559 2609.29573 2609.29578 2609.29584 2609.29601
2609.29607 2609.29618 2609.29626 2609.29633 2609.29636 2609.29657 2609.29672 2609.29680 2609.29682 2609.29684
2609.29703 2609.29709 2609.29718 2609.29733 2609.29735 2609.29769 2609.29792 2609.29798 2609.29800 2609.29802
2609.29807 2609.29828 2609.29837 2609.29845 2609.29848 2609.29855 2609.29913 2609.29928 2609.29933 2609.29952
2609.30005 2609.30009 2609.30012 2609.30030 2609.30048 2609.30063 2609.30071 2609.30074 2609.30075 2609.30087
2609.30094 2609.30100 2609.30121 2609.30130 2609.30137 2609.30147 2609.30151 2609.30160 2609.30167 2609.30184
2609.30199 2609.30226 2609.30227 2609.30238 2609.30243 2609.30250
```
### recentThursday24

```text
2609.26823 2609.26907 2609.26913 2609.26926 2609.26929 2609.26942 2609.26945 2609.26976 2609.27009 2609.27014
2609.27032 2609.27043 2609.27059 2609.27064 2609.27067 2609.27086 2609.27110 2609.27156 2609.27158 2609.27165
2609.27173 2609.27176 2609.27195 2609.27205 2609.27220 2609.27225 2609.27233 2609.27257 2609.27262 2609.27273
2609.27279 2609.27289 2609.27297 2609.27321 2609.27353 2609.27359 2609.27372 2609.27373 2609.27374 2609.27376
2609.27378 2609.27380 2609.27382 2609.27387 2609.27395 2609.27396 2609.27408 2609.27418 2609.27470 2609.27510
2609.27532 2609.27558 2609.27581 2609.27590 2609.27603 2609.27607 2609.27650 2609.27657 2609.27669 2609.27678
2609.27690 2609.27717 2609.27749 2609.27756 2609.27758 2609.27770 2609.27773 2609.27811 2609.27814 2609.27822
2609.27824 2609.27844 2609.27900 2609.27925 2609.27939 2609.27980 2609.27981 2609.28004 2609.28007 2609.28026
2609.28029 2609.28041 2609.28048 2609.28053 2609.28060 2609.28080 2609.28090 2609.28117 2609.28150 2609.28197
2609.28212 2609.28245 2609.28250 2609.28270 2609.28272 2609.28274 2609.28290 2609.28344 2609.28352 2609.28395
2609.28416 2609.28430 2609.28442 2609.28449 2609.28471
```
## 2. 十二分类实际恢复与停止点

使用 `https://arxiv.org/list/<category>/recent?skip=0&show=2000`。十二页均HTTP200；每个category只请求page1（skip0），读取五个日标题和本窗/相邻组ID与题名，不审窗外五天正文。total均小于2000，目标Tue22及邻接Mon21组到末尾；cs.OS Mon21无entries而total7全页已读。recent提供New和Cross，不包含历史Replacement全集。

| 分类 | recent页面 total | Mon21 New/Cross身份 | Tue22 New/Cross身份 | 实际目标原字段 / 停止点 |
| --- | --- | --- | --- | --- |
| [cs.CL](https://arxiv.org/list/cs.CL/recent?skip=0&show=2000) | 659 | 87 | 233 | `Tue, 22 Sep 2026 (showing 233 of 233 entries )`；skip0、show2000，完整组到末尾 |
| [cs.LG](https://arxiv.org/list/cs.LG/recent?skip=0&show=2000) | 1230 | 149 | 426 | `Tue, 22 Sep 2026 (showing 426 of 426 entries )`；skip0、show2000，完整组到末尾 |
| [cs.DC](https://arxiv.org/list/cs.DC/recent?skip=0&show=2000) | 117 | 17 | 37 | `Tue, 22 Sep 2026 (showing 37 of 37 entries )`；skip0、show2000，完整组到末尾 |
| [cs.AI](https://arxiv.org/list/cs.AI/recent?skip=0&show=2000) | 1202 | 125 | 384 | `Tue, 22 Sep 2026 (showing 384 of 384 entries )`；skip0、show2000，完整组到末尾 |
| [cs.CV](https://arxiv.org/list/cs.CV/recent?skip=0&show=2000) | 784 | 98 | 272 | `Tue, 22 Sep 2026 (showing 272 of 272 entries )`；skip0、show2000，完整组到末尾 |
| [cs.RO](https://arxiv.org/list/cs.RO/recent?skip=0&show=2000) | 640 | 114 | 210 | `Tue, 22 Sep 2026 (showing 210 of 210 entries )`；skip0、show2000，完整组到末尾 |
| [cs.AR](https://arxiv.org/list/cs.AR/recent?skip=0&show=2000) | 64 | 6 | 19 | `Tue, 22 Sep 2026 (showing 19 of 19 entries )`；skip0、show2000，完整组到末尾 |
| [cs.PL](https://arxiv.org/list/cs.PL/recent?skip=0&show=2000) | 30 | 1 | 11 | `Tue, 22 Sep 2026 (showing 11 of 11 entries )`；skip0、show2000，完整组到末尾 |
| [cs.OS](https://arxiv.org/list/cs.OS/recent?skip=0&show=2000) | 7 | 0 | 2 | `Tue, 22 Sep 2026 (showing 2 of 2 entries )`；skip0、show2000，完整组到末尾 |
| [cs.PF](https://arxiv.org/list/cs.PF/recent?skip=0&show=2000) | 29 | 6 | 8 | `Tue, 22 Sep 2026 (showing 8 of 8 entries )`；skip0、show2000，完整组到末尾 |
| [cs.IR](https://arxiv.org/list/cs.IR/recent?skip=0&show=2000) | 117 | 8 | 39 | `Tue, 22 Sep 2026 (showing 39 of 39 entries )`；skip0、show2000，完整组到末尾 |
| [cs.MA](https://arxiv.org/list/cs.MA/recent?skip=0&show=2000) | 89 | 7 | 30 | `Tue, 22 Sep 2026 (showing 30 of 30 entries )`；skip0、show2000，完整组到末尾 |

跨十二分类去重：Mon21实际恢复 **475** 个New/Cross身份；Tue22实际恢复 **1186** 个，按同ID任一合同分类为New分类得到 **1003 New、183 Cross-only**。这些是宽列表身份，不是贡献候选数，更不是1186篇全文队列。cs.AI初次`dt/dd`配对漏提2项，已用逐`dt`重新核到384/384，补回2609.22775和2609.22760；两者不能被脚本漏提悄然当成已排除。全12类原始身份及N/C角色见附录。

尝试的月/历史入口：`/list/cs.CL/2609` 和 `/list/cs.CL/2609?skip=0&show=2000`、cs.DC同类入口返回404；`/list/cs.CL/2026-09?skip=0&show=2000` HTTP200、September2026共2207项，但月列表没有本次所需历史Replacement批次，未遍历其后旧页。`/list/cs.MA/2026-09-22` 与 `/list/cs.MA/new?date=2026-09-22` 网页工具cache miss，未获得能证明目标日期的响应；没有把query参数当已实现历史查询。恢复recent已经足以保存New/Cross身份，**历史Replacement原始批次尚未恢复**。RSS仅返回Saturday26空批次，不补造历史清单。

## 3. 旧暂列68的身份冲突与普通 pending

旧68的精确 `/abs/<id>v1`（2609.12748用v2）均HTTP200，完整Title/Abstract已读取；当前history/可见Comments作轻量修订检查，不读完整旧版diff。逐项准入建议及轻量修订检查见下表；其中待补读的原创增量问题仍标明普通pending。

67个v1身份全部在官方recent Mon21组，0个在Tue22组；它们的**arXiv v1公告事件在09/21 08:00+08、早于09/22窗起点**。这只纠正公告事件，不宣称其他渠道的首次公开时刻，也不抹除既有单篇证据或 Books。2609.12748是replacement，未出现在recent New/Cross；v2 submitted=`Fri,18 Sep2026 10:22:33 UTC`不是其公开公告时刻，归属仍待目标Replacement公告恢复。

旧家族history还显示2609.21137v2（09/21 17:20:43UTC）、2609.21562v2（09/21 16:56:03UTC）、2609.22000v2（09/21 07:09:10UTC）、2609.22041v2（09/21 18:38:14UTC）、2609.21712v2（09/22 08:09:23UTC）。这些是提交元数据：版本号/时间本身不证明重要修订或落窗；对实际重要信号只定点恢复公告及变更说明，不因v1窗外而把整个family关闭。

### 3.1 68项题摘准入建议（不是最终候选分母）

全部68项的完整Title/Abstract已读；67个v1在本窗按**日期先关闭**，下表保留其原始具体贡献建议，便于真实归属日定点接续，不把日期纠错冒充学术无贡献。建议Owner来自当前ROADMAP，只表示可能的研究位置，不是Books已有覆盖或整合决定。不评分，不复制旧65/43未完成合计作新冻结分母。

| 精确题摘身份（完整标题） | 主线准入依据 / 未决事实 | 建议Owner |
| --- | --- | --- |
| [2609.12748v2 — The Mechanics of a Swarm: A Reproducible External Reconstruction of an Unintended Agent-Coordination Episode on a Third-Party Wiki](https://arxiv.org/abs/2609.12748v2) | 重要纠错候选：request log不能升级为delivery/causal use，旧传播解释被撤回；不是整篇withdrawn。v2公告归属未恢复，不确定落本窗。 | `AGENT-PLATFORM` |
| [2609.20824v1 — Do small language models know what they don't know?](https://arxiv.org/abs/2609.20824v1) | SLM token entropy近零而语义entropy仍可识别不确定性；若成立，路由须按预算分配而非宣称省算力。 | `INFER-SCHEDULING` |
| [2609.20830v1 — Reviser: Revision-Capable Text Generation via Autoregressive Cursor Actions](https://arxiv.org/abs/2609.20830v1) | next-action AR作用于可变canvas而非最终文本顺序；值得保留状态/动作与串行编辑成本分支。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| [2609.20831v1 — Recursive Language Models Generalize Out of Domain](https://arxiv.org/abs/2609.20831v1) | 隔离子任务上下文排除CoT在IID可用、OOD失效的shortcut；值得核验泛化条件，而非按递归名称保留。 | `AGENT-CONTEXT` |
| [2609.20844v1 — Boosting Deepresearch and LongContext Ability with Self-Generated Deepresearch Rollouts Traces](https://arxiv.org/abs/2609.20844v1) | 把DR轨迹网页摘要替换全文生成LongQA，再回DR-RL；新增证据关系保留与训练阶段交接，需控总预算。 | `MODEL-LONG-CONTEXT` |
| [2609.20845v1 — Reading Less While Writing: A Closed-Form Bandwidth Dial for Streaming Multimodal Decoders](https://arxiv.org/abs/2609.20845v1) | 用闭式可见prefix日程替代固定wait-k，给定异步到达下不可读取未来输入的结构保证；延迟/输入预算可共控。 | `MULTIMODAL-REPRESENTATION` |
| [2609.20846v1 — Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models](https://arxiv.org/abs/2609.20846v1) | 对欠定任务的过长CoT引入效率reward以改善abstention；需核答题能力保持及拒答阈值，不只是短输出指标。 | `TRAIN-GRPO` |
| [2609.20874v1 — Decomposing Predictive Kubernetes Autoscaling for Large Language Model Serving Under Long Startup Delays](https://arxiv.org/abs/2609.20874v1) | 冷启动延迟下拆解预测器、lookahead、token负载与margin；消融可能改变复杂预测器是否必要的选择。 | `INFER-SCHEDULING` |
| [2609.20888v1 — Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding](https://arxiv.org/abs/2609.20888v1) | 可学query threshold、训练soft suppression与推理KV块hard prune交接；新增sparsity学习与执行边界。 | `MODEL-SELF-ATTENTION` |
| [2609.20889v1 — Proxifield: Decentralized Multi-Agent Communication through Semantic Proximity](https://arxiv.org/abs/2609.20889v1) | 按四种语义信号形成去中心稀疏通信图，测试规模及永久故障；核算路由成本后再判替代Star边界。 | `AGENT-MULTI-AGENT` |
| [2609.20942v1 — When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation](https://arxiv.org/abs/2609.20942v1) | 控制合成review占比观察rating/semantic diversity collapse；主线是递归监督反馈，不是恢复科学领域任务。 | `TRAIN-DATA` |
| [2609.20957v1 — An Approximate Queueing Model of LLM Inference Serving for SLO-Driven Autoscaling](https://arxiv.org/abs/2609.20957v1) | 三参数迭代成本加状态依赖排队模型预测TTFT/ITL并驱动SLO扩容；核Markovian/light-moderate限制。 | `INFER-SCHEDULING` |
| [2609.20971v1 — RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models](https://arxiv.org/abs/2609.20971v1) | block centroid的mean dilution漏掉相关token，以半径rescue分支补选；密度匹配比较比单独加速数更关键。 | `INFER-PREFILL` |
| [2609.20974v1 — Attention-Aware Routing: Coupling Routing and Attention in MoEs](https://arxiv.org/abs/2609.20974v1) | 冻结base只改router，attention窗口特征揭示routing→后层sink与深度相关检索/推理冲突。 | `MODEL-MOE` |
| [2609.20995v1 — Voice-Light: A Full-Duplex Cascaded Voice Agent with Causal Turn-Taking and Speculative Generation](https://arxiv.org/abs/2609.20995v1) | 反向可取消playback、私有speculative response与browser rendered-ACK绑定durable history；learned controller失败保留hybrid。 | `MULTIMODAL-REPRESENTATION` |
| [2609.21022v1 — Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs](https://arxiv.org/abs/2609.21022v1) | 将chunk最后去噪步保留为高频反馈接口，避免全模型重跑；新增低频规划与高频纠正交接。 | `MULTIMODAL-EMBODIED-VLA` |
| [2609.21032v1 — Scaling Discovery through Test-Time Communication](https://arxiv.org/abs/2609.21032v1) | 有明确progress和充足compute时通信团队可优于独立best-k；条件不足时排序反转，需匹配总预算。 | `AGENT-MULTI-AGENT` |
| [2609.21039v1 — Stiefel-AdamW: Geometry-Aware AdamW for Linear Factorization Blocks](https://arxiv.org/abs/2609.21039v1) | 约束一个factor在Stiefel流形以去除非紧gauge导致factor blow-up，保留AdamW坐标预条件；非一般优化小改名。 | `TRAIN-LORA` |
| [2609.21058v1 — How Much of a Real Workload Can LLM-Generated GPU Kernels Actually Reach?](https://arxiv.org/abs/2609.21058v1) | 真实wall-clock addressable fraction限制kernel搜索收益，并纠错绝对容差接受zero/未完整write；必须深入受影响oracle。 | `INFER-TENSORRT-LLM` |
| [2609.21079v1 — DLB: Distributed Load Balancing at Scale for Generative AI Inference](https://arxiv.org/abs/2609.21079v1) | P2P probing与在线latency model支撑异构多阶段routing；新机制与内部22月部署数字分别限定。 | `INFER-SCHEDULING` |
| [2609.21081v1 — Loopjacking: Hijacking Human-in-the-Loop Approval](https://arxiv.org/abs/2609.21081v1) | 审批A被展示后B替换执行；canonical rendering与use-time精确绑定的阳/阴性对照改变审批边界。 | `PLATFORM-SECURITY` |
| [2609.21096v1 — Detecting Hallucination in LLMs: Tracing the Topological Signatures of Impaired Context Sharing](https://arxiv.org/abs/2609.21096v1) | attention图曲率单pass区分局部/全局信息flow病态；需核topology信号相对现有特征的独立增量。 | `MODEL-SELF-ATTENTION` |
| [2609.21137v1 — A Multi-Engine Dataflow for MoE Decoding on Scratchpad-Based Tensor Accelerators](https://arxiv.org/abs/2609.21137v1) | 量化expert-private加shared low-rank分解，与scratchpad多engine DMA/计算重叠共设计；不是仅硬件换代数字。 | `INFER-TENSORRT-LLM` |
| [2609.21155v1 — Same World, Different Knowledge: When Isolated Audits Misjudge World-Model Repairs](https://arxiv.org/abs/2609.21155v1) | 隔离fault审计偏好的repair在共享信息fault中反转；固定权重干预定位信息接口依赖，不能因负面结果排除。 | `MULTIMODAL-WORLD-MODELS` |
| [2609.21172v1 — TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](https://arxiv.org/abs/2609.21172v1) | prefill hidden预测需求，decode前联合exact/low-rank/flash分配，打破reactive eviction循环；核恢复成本。 | `INFER-KV-CACHE` |
| [2609.21187v1 — When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success](https://arxiv.org/abs/2609.21187v1) | 同模型SFT的gold-history next-turn收益不转为autonomous workflow成功；有配对反例，核既有评价命题真正差异。 | `PLATFORM-EVALUATION-SYSTEM` |
| [2609.21208v1 — Information-Gain Rewards over Diversity-Pruned Tests: GT-Anchored Verifier Co-Training for Reliable Code Generation](https://arxiv.org/abs/2609.21208v1) | 测试作者和coder共训的IG reward以GT correctness锚定，并去冗余test防宽松塌缩；新增reward/evaluator联合边界。 | `TRAIN-GRPO` |
| [2609.21223v1 — SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation](https://arxiv.org/abs/2609.21223v1) | 把before/during/after实物危险从native task success分离，有event/state checks；核新增可测失败而非仅97任务。 | `MULTIMODAL-EMBODIED-VLA` |
| [2609.21246v1 — VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models](https://arxiv.org/abs/2609.21246v1) | OOD类别≠执行失败，将action-prefix/progress纳入失败预测；须核独立于OOD gate的完整rollout评价。 | `MULTIMODAL-EMBODIED-VLA` |
| [2609.21257v1 — Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval at Scale](https://arxiv.org/abs/2609.21257v1) | 实验完成不等于有效结论：evaluator深度不一致导致head归因反转；typed adapter/记录+mutation拒绝无效比较。 | `AGENT-PLATFORM` |
| [2609.21264v1 — Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study](https://arxiv.org/abs/2609.21264v1) | 每层memory roofline解释XDNA1仅stream已compute-bound、XDNA2需fusion；新增应停止fusion的条件。 | `INFER-TENSORRT-LLM` |
| [2609.21267v1 — Efficient Benchmarking in Production: A Study of an Evolving LLM Agent](https://arxiv.org/abs/2609.21267v1) | 时间切分574次历史run比较固定/IRT subset保真与部署复杂度；需核跨family与漂移再校准条件。 | `PLATFORM-EVALUATION-SYSTEM` |
| [2609.21277v1 — How Many Humans Is a Judge Panel Worth?](https://arxiv.org/abs/2609.21277v1) | 同judge panel的spectral diversity与distribution recovery给出不同人类等效数；目标不能互换，新增反例。 | `PLATFORM-EVALUATION-SYSTEM` |
| [2609.21284v1 — Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution](https://arxiv.org/abs/2609.21284v1) | root cut不是完成撤权，sink fence与provider证书cutset处理异步旧任务、alternative支持及重绑定；缺证据indeterminate。 | `PLATFORM-SECURITY` |
| [2609.21299v1 — Brain API: An Intent-Aware Control Plane for Policy-Governed Agentic Systems](https://arxiv.org/abs/2609.21299v1) | 贡献未明：decision artifact与policy filtering prototype可读，但context/ranking仍design claims；需定点辨新机制而非control-plane叙述。 | `AGENT-PLATFORM` |
| [2609.21340v1 — Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](https://arxiv.org/abs/2609.21340v1) | 对LLM辅助重识别attack校准candidate ambiguity set，在exchangeability下给覆盖；隐私proxy不升级普遍安全。 | `PLATFORM-SECURITY` |
| [2609.21346v1 — IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts](https://arxiv.org/abs/2609.21346v1) | 把participation/execution/materialization分开，用有限codebook block与全expert参数composition共存；核语言模型证据。 | `MODEL-MOE` |
| [2609.21378v1 — ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL](https://arxiv.org/abs/2609.21378v1) | tournament relative reward向pivotal steps和utility skill memory分层传播credit；需核反思标注可信度与预算。 | `TRAIN-GRPO` |
| [2609.21432v1 — GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](https://arxiv.org/abs/2609.21432v1) | KL reward optimum推导gradient weighting，不靠importance sampling并扩OPD；需核唯一解/任意采样的假设。 | `TRAIN-GRPO` |
| [2609.21450v1 — Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](https://arxiv.org/abs/2609.21450v1) | 量化误差精确分成activation-guided compensation与orthogonal residual，导出sign/rotation/scaling不同适用作用。 | `INFER-TENSORRT-LLM` |
| [2609.21461v1 — AtomEgo: Exploring Ego-Robot Integration for Embodied Foundation Model Pretraining](https://arxiv.org/abs/2609.21461v1) | ego/robot联合、渐进alignment与video-action三种方案对读；数据规模×对齐质量的条件性边界值得核验。 | `MULTIMODAL-EMBODIED-VLA` |
| [2609.21465v1 — OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue](https://arxiv.org/abs/2609.21465v1) | 贡献待定：native AV任务、合成engine/bench和联合reward有主线相关性；摘要尚未分離新机制与任务/数据扩展，定点补方法即可。 | `MULTIMODAL-REPRESENTATION` |
| [2609.21483v1 — Weave: Fine-Grained Dynamic SM Scheduling in an MoE Megakernel for Compute-Communication Overlap](https://arxiv.org/abs/2609.21483v1) | 路由完成后每层/每GPU通信量已知，persistent megakernel内动态SM空间分配和时序调度，替代fixed split。 | `INFER-TENSORRT-LLM` |
| [2609.21561v1 — On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation](https://arxiv.org/abs/2609.21561v1) | privileged teacher信号混合正确性与行为；吸引/排斥共同偏移抵消的controlled distillation可能改变OPD设计。 | `TRAIN-SFT` |
| [2609.21562v1 — GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions](https://arxiv.org/abs/2609.21562v1) | tick级行为assertions+参考实现和mutant校准，runnable/最终状态正确仍能掩盖途中违规；网络代码可见性另控。 | `PLATFORM-EVALUATION-SYSTEM` |
| [2609.21573v1 — Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](https://arxiv.org/abs/2609.21573v1) | 多个局部合理文档弱信号累积，不是单毒passage；top-k/数据库diversity改变攻击共同出现概率。 | `PLATFORM-SECURITY` |
| [2609.21594v1 — HyperParallel-FSDP: Topology-Aware Fully Sharded Training with Layout-Driven Muon on Ascend SuperPods](https://arxiv.org/abs/2609.21594v1) | sharding语义上提autograd边界，validation与production双mode共用layout；拓扑FSDP/Muon通信归属需各核正确性。 | `TRAIN-DISTRIBUTED-TRAINING` |
| [2609.21605v1 — Trading Depth for Time in Recurrent Transformers](https://arxiv.org/abs/2609.21605v1) | 相同每词block计算预算下用thought-token recurrence换物理层深，降低参数但非无代价推理；需核匹配计算口径。 | `MODEL-TRANSFORMER-LAYER` |
| [2609.21619v1 — Calibrating Teacher--Student Discrepancy for On-Policy Distillation](https://arxiv.org/abs/2609.21619v1) | 正负privileged interventions估计teacher自身偏差区间，仅学超出区间的student discrepancy；区分能力差距与teacher漂移。 | `TRAIN-SFT` |
| [2609.21662v1 — When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap](https://arxiv.org/abs/2609.21662v1) | latent空间移动相当却难转成language输出改变；定位latent-to-language接口而非笼统activation steering有效性。 | `AGENT-PLANNING` |
| [2609.21686v1 — CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](https://arxiv.org/abs/2609.21686v1) | 内部敏感依赖与外部可恢复泄漏分离，观察面/检索深度影响recoverability；语义audit发现exact matching漏项。 | `PLATFORM-SECURITY` |
| [2609.21712v1 — ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](https://arxiv.org/abs/2609.21712v1) | 混合camera几何、causal streaming distillation与place memory共设计；generator-only timing不等端到端仿真。 | `MULTIMODAL-WORLD-MODELS` |
| [2609.21748v1 — World Modeling in Transformers](https://arxiv.org/abs/2609.21748v1) | 因果干预表明模型有地图但feature superposition破坏localization；行为失败不能直接证明无world model。 | `MULTIMODAL-WORLD-MODELS` |
| [2609.21793v1 — CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation](https://arxiv.org/abs/2609.21793v1) | 同threat model/预算比较19 attack×15 defense跨stage组合，检查safety/utility与query fairness，不采普遍最佳。 | `PLATFORM-SECURITY` |
| [2609.21827v1 — RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding](https://arxiv.org/abs/2609.21827v1) | 动态树构造proxy概率与verification真实采样概率拆分，避免top-k one-hot损害随机acceptance；losslessness需核证明。 | `INFER-SPECULATIVE-DECODING` |
| [2609.21858v1 — Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](https://arxiv.org/abs/2609.21858v1) | Poisson list coupling使multi-draft不依drafter且可无偏watermark、不降acceptance；核采样/水印共同假设。 | `INFER-SPECULATIVE-DECODING` |
| [2609.21908v1 — CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution](https://arxiv.org/abs/2609.21908v1) | stage commitment以当前实物证据而非command ACK判定，冻结base并阻断依赖动作、最小局部纠正。 | `MULTIMODAL-EMBODIED-VLA` |
| [2609.21940v1 — AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](https://arxiv.org/abs/2609.21940v1) | 写入前自配置低重叠semantic views减少mixed-schema检索干扰；provenance extraction与离线consolidation需分别归因。 | `AGENT-MEMORY` |
| [2609.21942v1 — When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence](https://arxiv.org/abs/2609.21942v1) | 已知注入failure与多sensor审计显示confidence/问人选择不随可靠性和cost变化；用测得accuracy而非自述置信决策。 | `MULTIMODAL-EMBODIED-VLA` |
| [2609.21967v1 — NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool Calling Capabilities](https://arxiv.org/abs/2609.21967v1) | streaming speech并行输出agent text/tool calls加RNN-T/流式TTS；工具选择与参数/执行弱项分报，不把F1当完成。 | `MULTIMODAL-REPRESENTATION` |
| [2609.21983v1 — SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation](https://arxiv.org/abs/2609.21983v1) | 25D skeleton/TCP共同状态经embodiment约束decoder实现无joint一一对应transfer；不是只加目标robot数据。 | `MULTIMODAL-EMBODIED-VLA` |
| [2609.22000v1 — RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents](https://arxiv.org/abs/2609.22000v1) | running reference oracle+hidden行为测试测跨深度recreation；static UI与interaction/computed outputs分离，先核已有首发family去重。 | `PLATFORM-EVALUATION-SYSTEM` |
| [2609.22005v1 — Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention](https://arxiv.org/abs/2609.22005v1) | 匹配scale与controlled value干扰分离abstention/noise filtering，二者收益随scale反向变化；不按gate小改标签排除。 | `MODEL-SELF-ATTENTION` |
| [2609.22041v1 — $λ$-Controlled GRPO: Turning Flow-Matching Ratio Instability into a Budgeted Resource](https://arxiv.org/abs/2609.22041v1) | flow Gaussian transition核给每步path variance解释ratio/negative gradient失效，并预算gradient effort；需核分布假设。 | `TRAIN-GRPO` |
| [2609.22048v1 — Available Guardrails: Certifying Selective Prediction across ML Systems](https://arxiv.org/abs/2609.22048v1) | 精确binomial证书的availability与validity分离，通过partition/error预算规划coverage；tool-call证据使其进入主线。 | `PLATFORM-EVALUATION-SYSTEM` |
| [2609.22055v1 — Benchmarking World Models for Continual Learning on Compositional Tasks](https://arxiv.org/abs/2609.22055v1) | compositional curriculum分离学新task与reuse旧机制，按action/perception轴定位continual learning瓶颈，不是仅榜单扩展。 | `MULTIMODAL-WORLD-MODELS` |
| [2609.22056v1 — Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring and Abstention](https://arxiv.org/abs/2609.22056v1) | ANN结构features能否含success互信息决定confident-failure可降性；跨regime互补意味着不能用单confidencefeature普遍部署。 | `AGENT-RAG` |
| [2609.22068v1 — CodeMidas: Scaling Agentic Coding RL Environments from Code Itself](https://arxiv.org/abs/2609.22068v1) | 从现有source functionality提行为spec，原code执行锚定tests并用solution rollouts过滤RL环境；需核oracle泄漏/网络访问。 | `TRAIN-GRPO` |

### 3.2 轻量撤回、修订与身份检查

68个家族的**当前**`/abs/<id>`再次只读Comments/Submission history及摘要标记，修正首遍Comments class含`mathjax`导致提取为空的问题。最终68/68元数据可读；当前Comments未提供withdrawal/correction/erratum文字，不因此宣称历史绝无标记。摘要中的2609.12748明确撤回因果解释，需保留纠错深审；不是论文withdrawn。普通名字含Revision、Correction、retraction属于方法术语，未误判成撤回通知。

当前可见v2的提交元数据：2609.21137=`2026-09-21T17:20:43Z`；21562=`2026-09-21T16:56:03Z`；22000=`2026-09-21T07:09:10Z`；22041=`2026-09-21T18:38:14Z`；21712=`2026-09-22T08:09:23Z`；21277=`2026-09-24T14:06:04Z`。前五项当前摘要与本次exact-v1摘要相同；21277当前v2摘要已变化，含外部CC-1000和panel selection等后续分析，只记录更新信号，不把它塞回09/22或深审旧版diff。**摘要相同不证明没有重要正文修订**；但版本号本身也不能制造贡献，实际变更说明与官方replacement公告是定点补查入口。12748v2的submitted字段与已读纠错内容必须分开处理：纠错内容有证据，公告落窗仍没有。

## 4. 廉价关联检查：09/23正式候选身份，不审全文

按root追加授权，仅提取09/23 README §3的38个唯一arXiv ID；**38/38在官方recent Tue22组**，无一个需为交叉检查打开正文。它们的arXiv列表归属与该日报09/22 09:00～09/23 09:00窗有实际冲突；这不否定其机制、证据、已写Books或独立审阅，只提示日期/source-event应定点协调。没有改09/23或扩大成整周重跑。38个ID如下：

```text
2609.22115 2609.22170 2609.22215 2609.22246 2609.22359 2609.22478 2609.22816 2609.22870 2609.22894 2609.22897
2609.22910 2609.23033 2609.23269 2609.23305 2609.23310 2609.23366 2609.23432 2609.23478 2609.23536 2609.23640
2609.23731 2609.23976 2609.24048 2609.24090 2609.24093 2609.24106 2609.24194 2609.24243 2609.24322 2609.24362
2609.24380 2609.24504 2609.24788 2609.24885 2609.24895 2609.24969 2609.24976 2609.24996
```
## 5. 真实Tue22批次：有限准入线索与分层关闭样本

先用本次恢复的题名辅助主题检索：GPU/kernel、graph/FP8、pipeline/sequence parallel、KV/attention、distributed RL数据路径与agent sandbox；浏览cs.DC/AR/PL/OS/PF相关标题及其余分类相应术语线索。关键词只辅助发现；没有把所有命中自动纳入，也没把剩余1186身份逐条全文审读。实际定点读取下面15项完整exact-v1 Title/Abstract：8项有具体主线增量建议继续，7项分层范围/贡献前关闭。它们均由真实Tue22官方ID组恢复；建议候选的其他更早官方首发及跨Daily家族去重仍需后续核验，所以**不称最终冻结的8项候选分母**。

| 精确题摘身份（完整标题） | 当前作者裁决 | 具体理由 / 待核证据 | 建议Owner |
| --- | --- | --- | --- |
| [2609.22220v1 — Measuring the Checker: Mutation Analysis for GPU-Kernel Benchmark Oracles](https://arxiv.org/abs/2609.22220v1) | 建议准入；Evidence普通pending | 用mutant独立kill witness衡量GPU oracle充分性，发现tolerance漏判及fuzzing误拒正确kernel；改变RL reward/benchmark有效性条件，而非另加题目。 | `INFER-TENSORRT-LLM` |
| [2609.23536v1 — Explicit State and Resource Contracts for Low-Precision Pipeline Parallel Training under Captured Graphs](https://arxiv.org/abs/2609.23536v1) | 建议准入；Evidence普通pending | captured静态地址不能代表FP8 scaling/非LIFO backward/跨optimizer weight cache归属；四状态/资源invariants及双向stream completion是具体正确性机制。 | `TRAIN-PIPELINE-PARALLEL` |
| [2609.24456v1 — Conduit: An Experience Data Plane for Distributed Reinforcement Learning](https://arxiv.org/abs/2609.24456v1) | 建议准入；Evidence普通pending | 将experience ingestion/placement/delivery从框架控制流分离，异构CPU/GPU tier与network约束下独立调度暴露延迟；准入的是训练数据平面机制，不照录泛RL规模数字。 | `TRAIN-DISTRIBUTED-TRAINING` |
| [2609.22755v1 — NSP: Accelerating Variable-Length LLM Training via Nested Sequence Parallelism](https://arxiv.org/abs/2609.22755v1) | 建议准入；Evidence普通pending | 不同SP度不再分割成disjoint GPU groups，而在同一iteration嵌套共享GPU；memory-constrained tree routing与phase streaming改变通信/负载取舍。 | `TRAIN-DISTRIBUTED-TRAINING` |
| [2609.23816v1 — SPLASH: Co-Designing Sparse Attention with High-Bandwidth Flash for Efficient Long-Context Inference](https://arxiv.org/abs/2609.23816v1) | 建议准入；Evidence普通pending | HBF/HBM近带宽但page granularity/plane parallelism不同，KV sparse attention与存储形态共设计；需核硬件建模、write endurance及全成本，不能宣称生产HBF验证。 | `INFER-KV-CACHE` |
| [2609.24847v1 — SPECTRA: Adaptive Execution of Speculative Decoding on a Runtime-Reconfigurable Tiled Architecture](https://arxiv.org/abs/2609.24847v1) | 建议准入；Evidence普通pending | spec verify强度随长度/acceptance介于GEMV与GEMM；tile内systolic/vector与tile间kernel级重配置支撑中间执行态，限制为20-tile FPGA所测。 | `INFER-TENSORRT-LLM` |
| [2609.22870v1 — Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870v1) | 建议准入；Evidence普通pending | 完整FP8管线噪声偏置importance ratio，使negative-advantage token错误零gradient；BF16 quantile匹配clipping不是仅训练推理校正数字。 | `TRAIN-GRPO` |
| [2609.22978v1 — DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](https://arxiv.org/abs/2609.22978v1) | 建议准入；Evidence普通pending | 多backend生命周期、versioned环境层、按需3FS image loading与stateful rollout/可抢占GPU training解耦；规模不是准入理由，隔离/回收状态责任才是。 | `AGENT-PLATFORM` |
| [2609.22358v1 — The Tethys Dataset: Seven Years of Hourly Smart Water Metering and a Pipeline for Making It Usable](https://arxiv.org/abs/2609.22358v1) | 范围前关闭 | 贡献是水表累计读数的数据清洗与缺测provenance；未直接研究大模型训练数据机制。数据质量原则可作类比不能恢复领域数据集。 | — |
| [2609.24713v1 — Mitigating Front-Running Attacks through Fair and Resilient Transaction Dissemination](https://arxiv.org/abs/2609.24713v1) | 范围前关闭 | 贡献是blockchain mempool公平传播与front-running；没有大模型状态/训练通信约束，分布式安全名词不足以纳入主线。 | — |
| [2609.22814v1 — From Idle to Urgent: A Resource-Harvested HPC Workflow for High-Fidelity Seismic Estimation](https://arxiv.org/abs/2609.22814v1) | 范围前关闭 | 地震3D模拟、surrogate/inverse analysis与urgent HPC用于科学领域估计；AI for Science暂缓，本文未分離通用大模型runtime新增机制。 | — |
| [2609.22775v1 — DVA-Neurons: Design and Verification of Adaptive LIF Neurons: From Single-Neuron Dynamics to Multi-Neuron Spiking Networks](https://arxiv.org/abs/2609.22775v1) | 范围前关闭 | adaptive LIF/6-neuron RTL与spike routing/verification是局部SNN器件实现；没有foundation模型形成或训练/推理设计关系，不因参数少一概排除。 | — |
| [2609.23009v1 — A Linked List of Cases in Language Design](https://arxiv.org/abs/2609.23009v1) | 范围前关闭 | LispBM在VESC固件RAM/flash分割执行与image boot经验；是通用嵌入式语言runtime，无本项目大模型计算/编译机制。 | — |
| [2609.23766v1 — TriFleetRCA: On-Premise LLM Root Cause Analysis for Kubernetes](https://arxiv.org/abs/2609.23766v1) | 贡献前关闭 | 有控制fault注入与citation/accuracy分离，但范围是K8s RCA中BM25/de-dup/ingest guard应用；单故障范围效应和小样本guard无因果收益不新增通用Agent/RAG设计边界。 | — |
| [2609.23130v1 — From Inference Engine to Inference Control Plane: Connecting vLLM, llm-d, and the Evolution of Efficient Distributed LLM Serving](https://arxiv.org/abs/2609.23130v1) | 贡献前关闭 | 作者明确synthesis而非新benchmark；串联engine/control-plane和提出planner未用新增综合证据解决具体机制分歧，不按框架组合或术语议程入选。 | — |

样本选择与覆盖：基础设施分类的领域数据集（cs.DC Tethys）、共识/链协议（cs.DC HERMES）、暂缓科学应用（cs.DC seismic）、局部非主线器件（cs.AI/AR DVA）、通用语言runtime（cs.PL LispBM）各1项；范围内应用组合（cs.LG/DC/AI TriFleetRCA）与机制综述（cs.AI/PF control-plane）各1项。共7项，不写成全部1186的独立误漏检查。八个拟保留线索来自具体执行/正确性机制，不因是正面性能或能映射owner而保留。后续非作者准入校准须双向检查这些建议保留与有纠错/反证信号排除项；本作者checkpoint不充当最终独立Day Gate。

## 6. 有限单元完成范围与精确接续

- **本单元已做完**：12类两组New/Cross身份恢复与停点；new/recent标签/公告clock对齐；旧68完整题摘和当前轻量metadata读取、逐项贡献建议；真实Tue22的15项有界题摘裁决；09/23正式38候选纯ID集合交叉。未改正式README、Books或共享checkpoint。
- **来源仍未闭合**：目标历史Replacement原清单未从recent/month恢复；2609.12748v2公告时刻没有证据。下一步定点恢复原始mailing/公告archive或可信官方版本公开证明，不能用submitted/updated、当前new或旧257合计补造本窗完整raw批次。现有1186仅New/Cross，不继承733，也不证明无遗漏。
- **普通准入pending**：真实Tue22其余主题相关标题线索尚未完成贡献筛选；当前8项只有作者建议，尚需首发去重与非作者校准。不是1186篇全部待全文，也不因此把某个已可审的单篇阻塞。旧68中21299/21465的原创增量定点方法问题留给真实归属日；无需在本窗为窗外v1继续深审。
- **重要revisionpending**：旧family当前显示v2者只登记轻量信号，未确认每个重要性/公告归属。12748确有解释撤回；其余若出现具体方法/评价/纠错变更说明再定点处理，不为数字v2制造无限版本史队列。
- **日期协调pending**：本窗旧67个v1公告归属与正式记载冲突；09/23正式38个ID全部在Tue22组。只对受影响source-event/日期依赖定点协调，保留原机制/证据与已落实Books，不在本单元改别日日报或重跑全周。
- **Evidence/Books/最终Day Gate未做**：八个建议项尚未方法/实现/关键实验审阅，本次不评分、不采性能数字、不作Books Decision。现有日报仍有普通工作；本源/准入作者恢复不等于09/22或W39完成。


## 7. 2026-09-27 继续恢复：窗口对账与证据复用（当前接续状态）

本节覆盖第5–6节的早期“8项建议/Replacement未恢复”状态，保留早期过程记录但不再沿用其队列。当前任务是一个**来源作者的有限 reconciliation 单元**：恢复批次、复用有效单篇材料、裁决差异、准备三项具体知识队列；不是独立 Day Gate、不是09/22全日报或W39 Complete，也不把42项全部标成深入完成。

### 7.1 恢复原始批次：不是复制旧合计

在当前 official recent 集合之外，实际找到了旧09/23读取留下的十二份官方 /new 完整响应：`/private/tmp/arxiv-20260923-cs.{AI,AR,CL,CV,DC,IR,LG,MA,OS,PF,PL,RO}.html`，以及完整题摘聚合 `/private/tmp/arxiv-20260923.json`。本轮实际读原字段、各 section 边界与 ID，不以文件名中的09/23作为公告归属。十二页原字段均为 **Showing new listings for Tuesday, 22 September 2026**，各 section 均为 showing N of N；读取到每个 section 最后一项、无分页余项。旧文件获取时刻为09/23 09:06～09:08，不证明公告09/23；公告日期由第1节对齐得到09/22 08:00北京时间。

| 合同分类 | New | Cross | Replacement | 原始页面停止 |
| --- | --- | --- | --- | --- |
| cs.AI | 111 | 273 | 212 | New/Cross/Replacement各 section末，showing N of N |
| cs.AR | 15 | 4 | 8 | 同上 |
| cs.CL | 176 | 57 | 122 | 同上 |
| cs.CV | 221 | 51 | 110 | 同上 |
| cs.DC | 26 | 11 | 18 | 同上 |
| cs.IR | 20 | 19 | 16 | 同上 |
| cs.LG | 241 | 185 | 210 | 同上 |
| cs.MA | 5 | 25 | 14 | 同上 |
| cs.OS | 0 | 2 | 1 | 同上 |
| cs.PF | 1 | 7 | 8 | 同上 |
| cs.PL | 5 | 6 | 6 | 同上 |
| cs.RO | 182 | 28 | 96 | 同上 |

跨分类角色去重所得 **1746=1003 New+183 Cross-only+560 Replacement-only**；这是实际该批原始身份，不是1746全文队列。逐 ID 对比旧 [New身份索引](../../../_sources/daily-20260923/arxiv-new-identities.md) 与本轮 official recent Tue22 New：1003/1003一致、missing=0、extra=0；对比旧 [non-New身份索引](../../../_sources/daily-20260923/arxiv-non-new-identities.md) 的183 Cross-only 与本轮 recent：183/183一致、missing=0、extra=0。该 durable non-New索引还保存560 Replacement-only ID、题名、分类及原角色；不用临时文件永久存活来证明身份。JSON的1746项有完整title/abstract、section/categories字段，足以复用旧题摘审阅，不需重下载1003摘要。

范围明确：当前 recent independently恢复了New/Cross并对齐；历史Replacement则复用当时保留的官方响应与逐身份索引，不是假称09/27官方历史replacement新查询成功。第2/6节“尚未恢复”已被此发现覆盖；月入口404、date参数cache miss的限制仍如实保留。

### 7.2 准入对账：38复用 + H-Spec唯一family + 3新增

旧09/23 [最终逐项New审计](../../../_sources/daily-20260923/arxiv-new-screening-audit.md) 有1003唯一行。逐行计数为38候选、580摘要/全文后关闭、276标题范围外、76标题级关闭、21标题明确范围外、5 Date Hold、4旧owner/同family、2 Theory Scope Disputed、1 Version Fact。本轮复用的是这个有逐ID层级的后期审计，不是旧398/400摘要工时、457/546早期缺账计数，也不声称本轮重新阅读1003全文。

本次差异裁决如下；前置题摘都实际读完，有关争议再定点读必要核心说明。7.3–7.5给出新增必要证据及现有知识差异。

| 第5节8个建议 | 本次裁决 | 原因及计数 |
| --- | --- | --- |
| 2609.23536 QEffect | 复用旧38中的一项 | captured graph的隐藏数值状态/资源边界已有必要证据及Ch38正文，不能重复计数 |
| 2609.22870 Full Pipeline FP8 RL | 复用旧38中的一项 | ratio失真/BF16校准的必要证据及Ch33正文已具备，不能重复计数 |
| 2609.22220 Measuring the Checker | 旧family日期隔离，不计本日 | 作者[news](https://mingzhe.space/news/)明确09/12已发布同题材料；精确首次上线/真实owner日留旧日恢复。贡献owner应为PLATFORM-EVALUATION-SYSTEM Ch66，非Ch49 kernel执行 |
| 2609.22978 DSec | 旧family核心机制去重，不计新首发 | DeepSeek V4 2026-04-24官方公告链接2606.19348v1，§5.2.5已披露四种sandbox substrate、3FS image、密度/回收与stateful trajectory/可抢占训练协调；后系统说明是同family实施补证据，没有在本窗新改变这些边界的可定位信号 |
| 2609.24456 Conduit | 贡献前关闭 | 实际§3–7.7及必要附录与Ch36 Dataflow对照，理由见7.5；不是以普通RL/现有owner为排除理由 |
| 2609.22755 NSP | 新增候选 | disjoint SP group→同pass nested共享GPU树、rank-uniform memory/remat与phase调度，见7.3 |
| 2609.23816 SPLASH | 新增候选 | near-die query-dependent page选择及program-complete KV horizon，见7.4；唯一owner改为INFER-GPU-MEMORY Ch54 |
| 2609.24847 SPECTRA | 新增候选 | 同PE fabric双dataflow与kernel mode/sharding recipe，见7.4 |

H-Spec `2609.24197v1` 已有09/22单篇准入、必要证据及Ch48写后复核；[Harvard页面](https://systems.seas.harvard.edu/seminar/2026-09-22-weifan-jiang/) 的 `datePublished`、`article:published_time` 为 `2026-09-21T15:00:00-04:00`＝09/22 03:00北京时间，后arXiv Tue22 08:00同family同一Daily，只记一项。它在旧1003审计的“旧owner”标签相对真实09/22应恢复为本日family；不能再加一个机构H-Spec计数。

**本有限单元保留池冻结为42个唯一family：迁回38+H-Spec1+NSP/SPLASH/SPECTRA3。** 这是当前有明确落窗/准入依据的保留池；5日期隔离、2理论争议、1版本事实在池外明确隔离而非零命中，下文保留实际未决；跨来源重复与Cross/Revision事件仍须日报owner协调，42不冒称全14源最终分母。旧38的33 Integrate/5 No Change只复用有效单篇边界，三新增没有Books完成结论。

```text
2609.22115 2609.22170 2609.22215 2609.22246 2609.22359 2609.22478
2609.22755 2609.22816 2609.22870 2609.22894 2609.22897 2609.22910
2609.23033 2609.23269 2609.23305 2609.23310 2609.23366 2609.23432
2609.23478 2609.23536 2609.23640 2609.23731 2609.23816 2609.23976
2609.24048 2609.24090 2609.24093 2609.24106 2609.24194 2609.24197
2609.24243 2609.24322 2609.24362 2609.24380 2609.24504 2609.24788
2609.24847 2609.24885 2609.24895 2609.24969 2609.24976 2609.24996
```

### 7.3 新增NSP：实际必要证据与唯一Books队列

[2609.22755v1 PDF](https://arxiv.org/pdf/2609.22755v1) 本轮HTTP200、19页，以内存读取文本；HTML exact-v1 HTTP404，不将HTML失败冒充全文受阻。实际读PDF pp.2–5、7–13；拟采用机制在§3.3/§4 pp.5–9，核心评价及反证在§6 pp.10–13。当前abs的v1 submitted=2026-09-19 04:32:47UTC不是公开时刻；本窗事件依据仍为官方Tue22完整组。

固定static SP在长度分布平稳时清楚；FlexSP在每个pass把序列放到动态但互斥GPU groups。NSP允许同一forward/backward pass里的不同SP degree按对齐的二叉SP树形成laminar/nested groups，共享GPU，而不是延迟长样本或单纯扩大context。CPU planner的profile-based prologue/compute/epilogue成本、token memory budget与beam-prefix/greedy-tail heuristic选择树和放置；不声称全局最优。Executor按phase queues显式安排跨层collective、计算及依赖，防止后续collective争带宽；在较贵的高树层保存activation、较便宜低层重算，并让组内各rank使用同一node字节估计/预算作save-remat决定，避免某rank跳过其他rank仍要执行的collective。输入all-to-all重排至SP tree，输出对称restore后再计算loss，planner不拥有sample/loss语义。

§6是作者内部64 NVIDIA GPUs的Qwen3 MoE30B/235B、FSDP64、EP8、235B CPU optimizer、AdamW设置；具体GPU型号与本笔记所需mixed-precision dtype为Not Disclosed，不补填A100/H100。每batch 2M tokens、192K/384K maximum context，三种公开长度trace用于长度分布，不构成这些语料文本上的质量收敛实验。各baseline共用kernel/训练栈，static SP sweep最优配置与FlexSP复现（最多5 microbatches）；50 warmup后平均第50–100 iteration。最高1.48×static、1.16×FlexSP仅是上述配置。NSP2L及leave-one-out支持中间树层、cost-model和memory/remat的必要性：235B去memory-aware重算退化9.6%；30B去cost model退化33.5%并可低于static。没有独立重复、跨拓扑质量收敛、bitwise gradient相等或任意sparse/linear attention保证。

评分：**Design Delta2 + System Reach2 + Durability2 = 6/9**。作者标准必要机制/评价已读；拟进入Books还因真实知识缺口需深入及非作者证据复核，而不是6分直接Integrate。root已独立读完整题摘确认准入，不把该准入校准扩大成PDF Evidence Gate通过。

唯一queue为 `TRAIN-DISTRIBUTED-TRAINING` → [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) L529–550“从等Token Packing到有界Attention Workload Pool”。现有段已解释固定size DP pool、sequence×head tile redistribution、sample membership和额外all-to-all，不能重复写“长序列负载均衡”。真实差异是**同一pass的SP成员从互斥组变为嵌套共享组**，需要同时约束phase order与rank-uniform保存/重算；应接在现有workload-pool分支之后比较两者控制的不同层次，保留static/disjoint低开销分支及planning/memory代价。Data27仍owner sample identity，PP38仍owner bubble/schedule；不新建章节。尚需非作者对上述必要PDF页及拟正文的复核、实际Books写入与写后复核，均为普通待办，不是外部Blocked。

### 7.4 新增SPLASH/SPECTRA：实际必要证据与两项队列

**SPLASH 2609.23816v1**：[exact-v1 HTML](https://arxiv.org/html/2609.23816v1) HTTP200，实际读§4–5.6、§6选择/控制核心、§7、§8.1–8.5。submitted=2026-09-20 19:11:43UTC只作版本身份；官方Tue22公告给本窗。HBF尚未商业制造；serving结果来自OpenHBF plane-level simulation和Vidur/measured Blackwell decode kernels，不是HBF硬件实测。

旧HBM-only与host/storage冷KV offload在通用硬件上仍合理；本文让HBM最近window与HBF append-only历史共同支撑sparse attention。写window内token共同co-selection，centroid评分以shared-KV-head的mean query统一GQA读数，直接选physical pages而非先token再放大成pages；head offset striping及**per-plane top-k cap**减少最慢plane读rounds，但cap会改变边界候选集合、不是保持候选不变的免费负载均衡。SelectFetch发送request/KV-head/query，不发送host计算的page-ID长列表，base-die持有query-dependent评分及logical→physical/valid-bit，HBFBind/HBFAppend/SelectFetch/HBFRelease是固定host descriptor界面。

append只有program完成才能推进write horizon；decode在开始时latch该horizon，不能读取仍在program的数据。每request单writer、private across-plane superblock region，region寿命内append、结束整region回收而非任意GC relocation；evicted KV在program完成前仍由HBM保留。读优先、最后读后再安排program，context长并不能消除写干扰与request isolation责任。

评价为五模型8B–235B、128K/512K/1M、batch1–128、TP1–8、BF16 weight、10% retrieval budget/16K HBM window的模型化方案；p50 50/100ms TPOT capacity frontier不是生产SLO。§8.3 Llama3.1-8B的48needle/64K/10%预算反例：Dense0.86、Quest0.62、SPLASH0.50，mean-query/page-centroid会丢极端稀疏目标，不能只记吞吐。§8.4的16nm面积9.67mm²是设计模型；§8.5耐久性用SLC P/E、**write amplification=1.15**及均匀磨损等假设，5年还依赖KV retention（Mooncake约30分钟trace只支持受限投影），不是实际yield/endurance/fault tolerance保证。

评分：**2+2+2=6/9**。root已独立读题摘及§4/5/6/7/8.3–8.5确认准入与重要限制；本作者已读拟采用核心及反证，但没有Books Gate完成结论。唯一queue `INFER-GPU-MEMORY` → [Ch54](../../../../../books/part-05-inference-system/54-gpu-memory.md) L422–445“Persistent Near-memory：容量层不再只是Offload终点”。现有正文已有persistent page/mapping owner、commit旧地址、prefetch/endurance/write amplification/fault isolation合同。缺口仅为**query-dependent选择权下沉到base-die + program-complete append visibility + per-plane quota改变候选/质量**，应嵌入当前mapping/执行层分权后，明确模拟而非量产。Ch45只交接KV语义，不能把同机制在两章再写一次。实际整合前深入确认Fig/Table对应配置、必要反证与拟正文，写后独立复核仍pending。

**SPECTRA 2609.24847v1**：[exact-v1 HTML](https://arxiv.org/html/2609.24847v1) HTTP200，实际读§3.1.1、3.2.1–3.2.3、4.1–4.4；submitted=2026-09-21 16:25:24UTC不是公开时刻。相同8×8=64MAC PE array在kernel粒度根据outer M采用两种dataflow：M=1以八dot-product lanes与64bank weight并行、broadcast/reindex作GEMV；M>1以output-stationary systolic作GEMM。改变的是预编译控制/索引而非重新加载bitstream或任意改变物理连接。四double buffers及streaming softmax/postprocess支撑attention，但不能把“20 tiles”写成20compute tiles。

Processor采用**FPGA-profiled cost model生成的offline mapping recipe**，联合tile数、M/N/K sharding、compute mode、DMA/multicast/P2P与producer/consumer pipeline。N/M shard尽可能避免reduction，K shard在小row/output等配置付reduction代价；不是普适在线最优。Target仍owner acceptance与commit，本研究没有新的接受正确性算法或概率等价证明。

§4的XCVU19P FPGA100MHz原型为20tiles＝14accelerator+4memory+1processor+1I/O，所测Pythia70→160M、SmolLM2 135→360M、GPT2 124→774M，默认32prompt tokens、20prompts、first8 speculative rounds并有长度sweep；完整dtype本轮未复核清楚（Not Verified，普通必要字段待核），不补填FP16，也不将抽取文本未显示等同作者未披露。与同一PE array固定vector/systolic的matched比较支持双模式，收益随draft fraction与target GEMM比例改变；mixed shard相对最好fixed shard另给局部增量。最高2.09×与进一步1.25×是局部实验，不是GPU端到端通用收益。资源对照也不免费：相对systolic LUT+82%、FF+79%、BRAM+7.7%、DSP+10.4%、URAM不变。§4.4 Jetson NX/TX2 token/s来自既有文献latency不是同硬件matched实测，不能拿3.6×外推。

评分：**2+1+2=5/9**。root独立读题摘及§3/4.1/4.2资源对照；拟Books仍需深入必要证据/边界与写后复核。唯一queue `INFER-TENSORRT-LLM` → [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) L299–301现有FPGA/AIE tile-loop/memory-view段，那里已限定runtime配置不是任意布线。新差异是**同一arithmetic fabric切换vector/systolic dataflow，再联合kernel sharding/communication recipe**，不是又增加tile shape选项；应紧接该段补“shape变化→工作强度变化”的下一重压力，保留固定fabric/优化GPU路径，不在Ch48重复设计target acceptance。

### 7.5 Conduit：对具体增量裁决后关闭

[2609.24456v1 HTML](https://arxiv.org/html/2609.24456v1) 实际读§3–7.7与必要Appendix A/C/D。它直接研究experience训练数据路径并有verl/Qwen数学RL案例，故**不是普通RL范围外**。三操作确为ingestion/placement/delivery；hook只能转换已声明结构、不能悄改内容语义。Profile CPU pageable/pinned、single/sharded GPU容量与有效带宽，planner调整tier/迁移、短暂停ingest/delivery而非actor/learner；feasible granularity受on-policy同iteration/minibatch freshness与off-policy replay规则约束。

§7.1两节点共8×A10080G/2TB host与另一个MI250X1024GPU classic-RL配置不能合成“LLM千卡收益”；RLlib默认CPU路径、Gear/Reverb不是drop-in baseline。Appendix A verl/Qwen2.5-Math-7B GRPO/DAPO-Math-17k在8A100里reward只依赖已生成sequence，所以可与剩余logprob/advantage后处理重叠：该路径42→20s（52%），**LLM端到端只4%**，不能把97%/38%的其他负载收益用于它。Appendix C明确数据完整性/current-policy-iteration；§7.7 DQN MountainCar/PPO MetaWorld收敛不证明LLM训练收敛。

实际现有 [Ch36 L1382–1400](../../../../../books/part-04-training-system/36-distributed-training.md) 已把rollout service→typed trajectory→transform/filter/advantage→trainer→versioned weight publication拆开，并规定runtime只owner placement/transport、不得改变reward/sample-weight/objective，承担背压、版本错配和跨域恢复；L1401–1411再把rollout placement与policy语义分离。Conduit增加的是这条已有dataflow在tier成本/传输粒度的实现选择，必要原文没有给出令现有同步/freshness/数据语义合同失效的新边界或重要反证；LLM 4%局部operating point不足以要求长期改写。故**候选前关闭，不评分、不制造Books队列**。该理由以三操作、placement/freshness与真实端到端反例为依据，不是仅凭“已有owner/经典RL/速度小”排除。

### 7.6 旧38的逐项复用定位与缺口

本轮实际读取旧正式§4、各非空附件及当前Books对应正文，不重读38全文。README的 `../../_sources` 正确指向 **papers/2026/_sources/daily-20260923/**，不是月份级目录；不存在“38证据全部missing”，也不能机械改这些links。本轮读到28个独立证据文件及additional，共359行；其中22220、23048是旧/排除项，实际支撑旧38的是26单独文件、11 additional小节、WaveFront1项正式§4自包含必要机制/评价/边界。没有凭absence创造WaveFront附件。

下表行号为本轮定位，文件后续并行编辑可移动；身份与正文论点绑定为稳定定位。复用含现有标准/深入审阅及报告记录的独立复核，但本作者不是再次独立验收人；日期段均应用本节clock更正，不复用错误09/23公开时间。33正文marker均实际查到，并读机制段而非只grep标签；5 No Change则读实际已有合同，不以没有marker证明已有覆盖。

| exact-v1 | 正式证据与实际附件 | 当前Books位置/复用范围 |
| --- | --- | --- |
| 2609.22870v1 | [§4 L79](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22870-evidence.md) | [33章正文](../../../../../books/part-04-training-system/33-grpo.md) L1178；实际正文绑定可复用，不重做写入 |
| 2609.24322v1 | [§4 L83](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24322-evidence.md) | [76章正文](../../../../../books/part-07-agent/76-rag.md) L208；实际正文绑定可复用，不重做写入 |
| 2609.23536v1 | [§4 L88](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23536-evidence.md) | [38章正文](../../../../../books/part-04-training-system/38-pipeline-parallel.md) L123；实际正文绑定可复用，不重做写入 |
| 2609.23478v1 | [§4 L92](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23478-evidence.md) | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L855；实际正文绑定可复用，不重做写入 |
| 2609.24362v1 | [§4 L96](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24362-evidence.md) | [75章正文](../../../../../books/part-07-agent/75-context.md) L183；实际正文绑定可复用，不重做写入 |
| 2609.24048v1 | [§4 L100](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24048-evidence.md) | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L246；实际正文绑定可复用，不重做写入 |
| 2609.22478v1 | [§4 L104](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22478-evidence.md) | [66章正文](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L240；No Change：实验身份贯穿 cohort、prompt、resolved model/call、annotation、analysis；H/R/identifier 比较未改变该合同 |
| 2609.24969v1 | [§4 L108](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24969-evidence.md) | [66章正文](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L3759；实际正文绑定可复用，不重做写入 |
| 2609.23033v1 | [§4 L114](../../23/README.md)；正式 §4 自包含机制/评价/限制（无单独 evidence 附件） | [48章正文](../../../../../books/part-05-inference-system/48-speculative-decoding.md) L351；实际正文绑定可复用，不重做写入 |
| 2609.22170v1 | [§4 L120](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22170-evidence.md) | [66章正文](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L226；实际正文绑定可复用，不重做写入 |
| 2609.24093v1 | [§4 L124](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24093-evidence.md) | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L37；实际正文绑定可复用，不重做写入 |
| 2609.23305v1 | [§4 L128](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23305-evidence.md) | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L480；实际正文绑定可复用，不重做写入 |
| 2609.23432v1 | [§4 L132](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23432-evidence.md) | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L365；实际正文绑定可复用，不重做写入 |
| 2609.22115v1 | [§4 L136](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22115-evidence.md) | [29章正文](../../../../../books/part-04-training-system/29-sft.md) L551；实际正文绑定可复用，不重做写入 |
| 2609.22215v1 | [§4 L140](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22215-evidence.md) | [29章正文](../../../../../books/part-04-training-system/29-sft.md) L999；实际正文绑定可复用，不重做写入 |
| 2609.22246v1 | [§4 L144](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.22246v1` 小节 | [76章正文](../../../../../books/part-07-agent/76-rag.md) L611；No Change：生成链不能充当新的独立来源；同源转载的有限注入证据不改变来源独立性/概率校准权责 |
| 2609.22359v1 | [§4 L148](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22359-evidence.md) | [31章正文](../../../../../books/part-04-training-system/31-rlhf.md) L138；实际正文绑定可复用，不重做写入 |
| 2609.22816v1 | [§4 L152](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22816-evidence.md) | [25章正文](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) L70；实际正文绑定可复用，不重做写入 |
| 2609.22894v1 | [§4 L156](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22894-evidence.md) | [27章正文](../../../../../books/part-04-training-system/27-data.md) L1080；实际正文绑定可复用，不重做写入 |
| 2609.22897v1 | [§4 L160](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.22897v1` 小节 | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L744；实际正文绑定可复用，不重做写入 |
| 2609.22910v1 | [§4 L164](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.22910-evidence.md) | [78章正文](../../../../../books/part-07-agent/78-tool-calling.md) L200；实际正文绑定可复用，不重做写入 |
| 2609.23269v1 | [§4 L168](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.23269v1` 小节 | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L704；实际正文绑定可复用，不重做写入 |
| 2609.23310v1 | [§4 L172](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23310-evidence.md) | [82章正文](../../../../../books/part-07-agent/82-multi-agent.md) L57；实际正文绑定可复用，不重做写入 |
| 2609.23366v1 | [§4 L176](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23366-evidence.md) | [22章正文](../../../../../books/part-02-model/22-long-context.md) L268；实际正文绑定可复用，不重做写入 |
| 2609.23640v1 | [§4 L180](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23640-evidence.md) | [31章正文](../../../../../books/part-04-training-system/31-rlhf.md) L274；实际正文绑定可复用，不重做写入 |
| 2609.23731v1 | [§4 L184](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.23731-evidence.md) | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L65；实际正文绑定可复用，不重做写入 |
| 2609.23976v1 | [§4 L188](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.23976v1` 小节 | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L822；实际正文绑定可复用，不重做写入 |
| 2609.24090v1 | [§4 L192](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24090-evidence.md) | [81章正文](../../../../../books/part-07-agent/81-workflow.md) L569；No Change：完整 read certificate 对 revision journal；已知依赖缩小重算、未知依赖扩大失效 |
| 2609.24106v1 | [§4 L196](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24106-evidence.md) | [27章正文](../../../../../books/part-04-training-system/27-data.md) L51；实际正文绑定可复用，不重做写入 |
| 2609.24194v1 | [§4 L200](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.24194v1` 小节 | [66章正文](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L405；实际正文绑定可复用，不重做写入 |
| 2609.24243v1 | [§4 L204](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.24243v1` 小节 | [72章正文](../../../../../books/part-06-ai-infrastructure/72-security.md) L599；No Change：controllability、monitorability、faithfulness、outcome safety 四分；CoT sensor 无 authority |
| 2609.24380v1 | [§4 L208](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.24380v1` 小节 | [32章正文](../../../../../books/part-04-training-system/32-ppo.md) L101；实际正文绑定可复用，不重做写入 |
| 2609.24504v1 | [§4 L212](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.24504v1` 小节 | [59章正文](../../../../../books/part-06-ai-infrastructure/59-model-registry.md) L224；实际正文绑定可复用，不重做写入 |
| 2609.24788v1 | [§4 L216](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24788-evidence.md) | [24章正文](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L750；实际正文绑定可复用，不重做写入 |
| 2609.24885v1 | [§4 L220](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.24885v1` 小节 | [66章正文](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L588；实际正文绑定可复用，不重做写入 |
| 2609.24895v1 | [§4 L224](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.24895v1` 小节 | [84章正文](../../../../../books/part-07-agent/84-agent-platform.md) L395；No Change：独立 acceptor 与 anytime false commit，依赖合法证据过程而非自由文本说服 |
| 2609.24976v1 | [§4 L228](../../23/README.md)；[独立文件](../../../_sources/daily-20260923/arxiv-2609.24976-evidence.md) | [25章正文](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) L932；实际正文绑定可复用，不重做写入 |
| 2609.24996v1 | [§4 L232](../../23/README.md)；[additional](../../../_sources/daily-20260923/arxiv-additional-evidence.md) 对应 `2609.24996v1` 小节 | [26章正文](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L844；实际正文绑定可复用，不重做写入 |

必要更正只涉及来源事件：24969原正式§4称GitHub 09/23 03:10早于arXiv；按本轮clock，arXiv09/22 08:00已经早于该commit，故commit不可作为此family的更早公开证据。FP8/retrieval等§4头部的09/23推定同样不可复用。23305/22170较早附件有pending/未写最终复核标签，复用后续正式§4及真实正文，不能把早期pending改造成作者本人重新独立通过。现有具体机制与限制没有因日期更正自动失效。

### 7.7 排除口径校准与安全隔离：不把普通未读伪Blocked

本轮为检查“现有owner/无跨backend/局部实验”被当硬门槛的共享排除理由，从旧1003审计选9个具名样本，实际重读保留的完整title/abstract：22091 ProspectiveMemory、22100 AdaMem、22106 PRQuant、22302皮肤病authority评估、22712 TrustworthyAgent综述、23184 CausalWM、24456 Conduit、24815 Uranus、24847 SPECTRA。SPECTRA改判新增；Conduit补核心说明后关闭。其余具体裁决限下列原贡献，不把9个样本宣称为1003全量独立复核：

- 22091：原“write-time trigger已有覆盖”关闭已被09/30非作者actual owner纠正：15405仅尾部trace，正文未承载dated/condition open-resolved ledger离线链接与乘法rank。具体准入，oracle ledger/未建抽取层与matcher负侧必要核见[当前必要包R22091](V3_RECONCILIATION_20260930.md#r22091-prospective-term--agent-memory)，不因synthetic/小样本拒收。
- 22100：原“成熟压缩与预算组合”关闭已被09/30非作者纠正：同query-forward bank+score与fixed budget整数allocation/omit及bank先计算的成本是具体机制，Ch76一般controller/sharedencoder未覆盖。具体准入，必要方法/同预算OSCAR及成本反证见[当前必要包R22100](V3_RECONCILIATION_20260930.md#r22100-adamem--agent-rag)，不自动声称Books整合。
- 22106：offline permutation把outlier集中tail+static residual避免online gather；Ch49 L756–767已有fractional-precision physical layout/permutation传播/backend消费，以及L707–715 correction分支。排除是此增量仍落已有物理布局分支，不以“单backend不能入选”为理由。
- 22302：皮肤病选proposal/action的factor身份和weighted scores/ISIC模拟是EvalSpec action/cohort权重合同的领域实例；没有改变通用evaluation validity，不把AI+医学应用类比成主线机制。
- 22712：taxonomy/lifecycle综述缺新增综合证据解决具体知识分歧；framework名称不能代替机制贡献。
- 23184：16B/31Khours、causal CoT→video prediction与三阶段训练组合；题摘所能定位的是显式reasoning中间条件，没有隔离出改变causal identification/intervention support的重要证据，暂不升级“CoT因果正确”，保留原候选前关闭而非因没有owner排除。
- 24815：joint-conditioned causal AR diffusion、单latent step对应4RGB frames、流式多视角生成；新模型/24FPS不单独改变Ch25已解释的action-condition与causal stream边界，关闭的是组合operating point，不否定新生成范式有资格入选。

未复查范围必须可见：上述9项不替代其余574/5/1关闭记录的独立分层复核，也不证明76标题级皆足够明确。后续若独立校准发现同理由漏收，应只扩查相同受影响理由；不回到1186全文队列。

保留8个精确隔离身份及重开问题：Date Hold **2609.22125、22195、22819、24144、24812** 缺决定真实owner的公开可见时间；不是书稿采用依据。Theory Scope Disputed **2609.24797、24942**：旧“需要真实LM scale/摘要不足证所有模型”不能单独当拒绝贡献门槛；若中心定理/反例会改变expressivity或OOD解释，应定点读当前精确版本假设再决定。它们是**普通准入待核，不是外部Blocked/安全完成终态**，也不为省时从隔离池删除。Version Fact **2609.22991** 保留MPS >2^32 silent failure的backend/version/shape/dtype/evaluator边界未核问题；真实正确性信号需独立核受影响内容，不能因为已有数值gate就伪“完全处理”。此有限单元不擅自给这些项补分。

Replacement实际显式信号复用当时十二页Comments：2606.08151v4纠正memory retrieval recall；2609.16639v2 withdrawn（author agreement不足）不候选；2609.15795 title typo、2609.09646 reference非重要机制；2608.28021v2 prompt-class correction、2606.22419v3三engine bugs/v1.8.0、2601.15322 faithfulness解释更正、2602.13718控制消融/realrobot VLA、2603.16859评估protocol/results变化为具名重要revision线索。旧账本已按ID/题名检查仓库采用链，除22419只有June source audit外无定位到已采用正文断言；此处没有当前需要直接撤改的Books结论，若后续命中采用才定点纠正，不扩全年旧版diff。**revision事件本身属此恢复批次，不因sourcefamily早发月份自动回拨revision日期**。560 silent Comments不声称完整摘要已读，183 Cross-only也不因角色自动认定窗外：复用原题名/有界主题审阅，对22547、23570等旧账本线索若拟保留须核首次正文事件，不以Cross标签排除。上述未决属来源owner接续边界，不能用42候选池掩盖。

09/30定点复核纠正上述旧采用链概括：16639实际曾有Ch29采用正文，官方withdraw后已移除且root写后通过；12748实际Ch84既有段只承载visible≠consume≠causal合同、缺readlog不推传播/缺outcome不推效用，与v2撤回因果解释一致而保留，不是新增v2正面采用。v2公开日期仍Hold；旧“无采用链/没有当前撤改”不再有效，不能据此跳过必要风险negative。七条具体误判22098/22101/22109/22135/23551/22100/22091均按非作者同19样本校准局部准入，见唯一reconciliation末尾七项；1746仍discovery而非全文队列，旧理论/版本待办由其当前终态覆盖，不重扫全批。

### 7.8 本有限单元交付与精确下一步

实际完成：十二类官方字段/身份/停止点恢复；原new/current recent完整集合对齐；历史Replacement snapshot与身份复用；旧38逐项证据及33实际正文/5现有覆盖核对；8建议去重裁决、三新增必要机制/评价/反证审阅及具体owner差异；Conduit关闭；有界排除口径校准。只修改本来源笔记，不改正式Daily/Books/shared checkpoint。

交给root：迁回38证据与H-Spec单family，不重复Books；三项NSP/SPLASH/SPECTRA按唯一owner深入复核采用命题、完成实际写入及写后独立复核；日期/理论/版本隔离与Cross/Revision必要信号按具名问题继续，不称外部受阻；最终冻结全日报分母、14源Source Gate、非作者Day Gate由root独立组织。旧22窗外67不再本窗深审。**这一有限恢复/差异审阅单元结束，不等于Daily22或W39完成。**

## 附录：十二分类原始New/Cross身份

N＝该合同分类主列表New；C＝cross-list。相同ID跨分类重复只计一个材料家族；不能直接相加各行数量。

### cs.CL

#### Mon21

N（65）：

```text
2609.20824 2609.20825 2609.20826 2609.20827 2609.20828 2609.20829 2609.20830 2609.20831 2609.20832 2609.20833
2609.20834 2609.20835 2609.20836 2609.20838 2609.20839 2609.20842 2609.20843 2609.20844 2609.20845 2609.20846
2609.20847 2609.20849 2609.20850 2609.20902 2609.20945 2609.21075 2609.21094 2609.21117 2609.21145 2609.21154
2609.21179 2609.21187 2609.21227 2609.21231 2609.21247 2609.21277 2609.21349 2609.21362 2609.21378 2609.21383
2609.21387 2609.21392 2609.21401 2609.21490 2609.21554 2609.21595 2609.21636 2609.21637 2609.21655 2609.21662
2609.21663 2609.21673 2609.21722 2609.21789 2609.21827 2609.21844 2609.21857 2609.21859 2609.21967 2609.21992
2609.22000 2609.22008 2609.22038 2609.22043 2609.22081
```
C（22）：

```text
2609.20875 2609.20886 2609.20989 2609.20995 2609.21032 2609.21084 2609.21096 2609.21149 2609.21183 2609.21296
2609.21340 2609.21390 2609.21562 2609.21651 2609.21672 2609.21676 2609.21683 2609.21748 2609.21793 2609.21888
2609.22005 2609.22056
```
#### Tue22

N（176）：

```text
2609.22090 2609.22091 2609.22094 2609.22096 2609.22097 2609.22098 2609.22099 2609.22100 2609.22101 2609.22104
2609.22110 2609.22111 2609.22112 2609.22114 2609.22119 2609.22124 2609.22125 2609.22127 2609.22131 2609.22133
2609.22135 2609.22136 2609.22138 2609.22143 2609.22144 2609.22149 2609.22151 2609.22152 2609.22162 2609.22163
2609.22164 2609.22169 2609.22171 2609.22174 2609.22188 2609.22195 2609.22198 2609.22200 2609.22204 2609.22206
2609.22208 2609.22209 2609.22210 2609.22212 2609.22213 2609.22214 2609.22215 2609.22219 2609.22221 2609.22223
2609.22224 2609.22225 2609.22226 2609.22228 2609.22231 2609.22234 2609.22235 2609.22239 2609.22241 2609.22243
2609.22245 2609.22246 2609.22248 2609.22249 2609.22255 2609.22256 2609.22259 2609.22261 2609.22362 2609.22409
2609.22452 2609.22455 2609.22463 2609.22494 2609.22522 2609.22536 2609.22553 2609.22566 2609.22603 2609.22607
2609.22633 2609.22697 2609.22700 2609.22705 2609.22734 2609.22767 2609.22774 2609.22778 2609.22793 2609.22796
2609.22805 2609.22884 2609.22904 2609.22917 2609.22934 2609.22971 2609.22988 2609.23039 2609.23053 2609.23056
2609.23065 2609.23083 2609.23088 2609.23178 2609.23191 2609.23194 2609.23205 2609.23231 2609.23239 2609.23264
2609.23267 2609.23371 2609.23463 2609.23465 2609.23466 2609.23490 2609.23551 2609.23573 2609.23582 2609.23587
2609.23697 2609.23703 2609.23716 2609.23726 2609.23742 2609.23808 2609.23825 2609.23853 2609.23880 2609.23886
2609.23916 2609.23935 2609.23939 2609.23951 2609.23955 2609.23959 2609.23966 2609.24028 2609.24052 2609.24066
2609.24083 2609.24106 2609.24122 2609.24156 2609.24177 2609.24194 2609.24196 2609.24199 2609.24219 2609.24238
2609.24246 2609.24264 2609.24275 2609.24357 2609.24372 2609.24410 2609.24516 2609.24538 2609.24554 2609.24574
2609.24635 2609.24650 2609.24698 2609.24799 2609.24812 2609.24821 2609.24877 2609.24885 2609.24890 2609.24895
2609.24903 2609.24911 2609.24932 2609.24965 2609.24971 2609.24983
```
C（57）：

```text
2609.22102 2609.22107 2609.22120 2609.22145 2609.22146 2609.22157 2609.22161 2609.22170 2609.22178 2609.22196
2609.22216 2609.22218 2609.22222 2609.22227 2609.22253 2609.22257 2609.22260 2609.22375 2609.22471 2609.22478
2609.22880 2609.22939 2609.22949 2609.22951 2609.22977 2609.23043 2609.23071 2609.23193 2609.23257 2609.23367
2609.23377 2609.23416 2609.23435 2609.23449 2609.23462 2609.23567 2609.23570 2609.23585 2609.23592 2609.23646
2609.23979 2609.24057 2609.24137 2609.24303 2609.24310 2609.24432 2609.24480 2609.24613 2609.24625 2609.24657
2609.24678 2609.24855 2609.24894 2609.24967 2609.24972 2609.24974 2609.24985
```
### cs.LG

#### Mon21

N（83）：

```text
2609.20883 2609.20886 2609.20888 2609.20904 2609.20906 2609.20912 2609.20942 2609.20954 2609.20968 2609.20978
2609.20982 2609.20991 2609.20997 2609.21001 2609.21032 2609.21039 2609.21044 2609.21057 2609.21073 2609.21108
2609.21109 2609.21123 2609.21126 2609.21151 2609.21158 2609.21164 2609.21172 2609.21190 2609.21197 2609.21280
2609.21288 2609.21296 2609.21306 2609.21309 2609.21327 2609.21332 2609.21346 2609.21381 2609.21382 2609.21425
2609.21427 2609.21445 2609.21450 2609.21457 2609.21523 2609.21525 2609.21527 2609.21533 2609.21550 2609.21561
2609.21605 2609.21647 2609.21656 2609.21664 2609.21693 2609.21704 2609.21735 2609.21749 2609.21758 2609.21791
2609.21815 2609.21829 2609.21849 2609.21870 2609.21876 2609.21888 2609.21894 2609.21899 2609.21906 2609.21909
2609.21926 2609.21932 2609.21945 2609.21953 2609.21989 2609.21995 2609.22005 2609.22012 2609.22041 2609.22048
2609.22053 2609.22055 2609.22064
```
C（66）：

```text
2412.07151 2609.19122 2609.20825 2609.20826 2609.20828 2609.20831 2609.20836 2609.20843 2609.20845 2609.20846
2609.20857 2609.20868 2609.20873 2609.20897 2609.20973 2609.20999 2609.21012 2609.21017 2609.21054 2609.21085
2609.21096 2609.21138 2609.21181 2609.21212 2609.21241 2609.21243 2609.21257 2609.21264 2609.21277 2609.21281
2609.21303 2609.21320 2609.21321 2609.21363 2609.21383 2609.21422 2609.21432 2609.21447 2609.21454 2609.21482
2609.21515 2609.21541 2609.21548 2609.21567 2609.21583 2609.21590 2609.21628 2609.21651 2609.21655 2609.21694
2609.21747 2609.21759 2609.21763 2609.21788 2609.21821 2609.21827 2609.21858 2609.21863 2609.21872 2609.21880
2609.21910 2609.21941 2609.21944 2609.21960 2609.21976 2609.22056
```
#### Tue22

N（241）：

```text
2609.22106 2609.22107 2609.22108 2609.22109 2609.22113 2609.22115 2609.22117 2609.22120 2609.22121 2609.22122
2609.22123 2609.22126 2609.22129 2609.22130 2609.22145 2609.22146 2609.22153 2609.22154 2609.22155 2609.22156
2609.22157 2609.22158 2609.22160 2609.22165 2609.22166 2609.22167 2609.22170 2609.22173 2609.22175 2609.22177
2609.22178 2609.22182 2609.22183 2609.22184 2609.22185 2609.22187 2609.22191 2609.22192 2609.22194 2609.22196
2609.22197 2609.22199 2609.22205 2609.22216 2609.22217 2609.22218 2609.22220 2609.22222 2609.22229 2609.22230
2609.22232 2609.22233 2609.22237 2609.22238 2609.22240 2609.22244 2609.22247 2609.22251 2609.22252 2609.22253
2609.22254 2609.22257 2609.22258 2609.22359 2609.22360 2609.22361 2609.22415 2609.22441 2609.22471 2609.22487
2609.22508 2609.22554 2609.22583 2609.22584 2609.22585 2609.22593 2609.22614 2609.22632 2609.22643 2609.22690
2609.22701 2609.22752 2609.22782 2609.22783 2609.22785 2609.22816 2609.22819 2609.22820 2609.22833 2609.22836
2609.22850 2609.22862 2609.22866 2609.22867 2609.22870 2609.22879 2609.22886 2609.22894 2609.22919 2609.22932
2609.22943 2609.22977 2609.22984 2609.22990 2609.23008 2609.23033 2609.23055 2609.23073 2609.23084 2609.23087
2609.23092 2609.23102 2609.23117 2609.23125 2609.23127 2609.23146 2609.23183 2609.23185 2609.23215 2609.23219
2609.23242 2609.23254 2609.23257 2609.23260 2609.23265 2609.23308 2609.23314 2609.23320 2609.23325 2609.23333
2609.23366 2609.23374 2609.23381 2609.23387 2609.23435 2609.23457 2609.23460 2609.23516 2609.23521 2609.23529
2609.23535 2609.23547 2609.23549 2609.23585 2609.23590 2609.23594 2609.23659 2609.23686 2609.23687 2609.23688
2609.23761 2609.23775 2609.23780 2609.23789 2609.23812 2609.23826 2609.23836 2609.23838 2609.23843 2609.23845
2609.23875 2609.23876 2609.23883 2609.23892 2609.23900 2609.23906 2609.23907 2609.23924 2609.23934 2609.23990
2609.23995 2609.23999 2609.24003 2609.24040 2609.24042 2609.24089 2609.24103 2609.24111 2609.24117 2609.24141
2609.24144 2609.24146 2609.24150 2609.24197 2609.24202 2609.24209 2609.24233 2609.24241 2609.24249 2609.24250
2609.24259 2609.24278 2609.24289 2609.24298 2609.24303 2609.24322 2609.24328 2609.24338 2609.24358 2609.24370
2609.24380 2609.24382 2609.24386 2609.24391 2609.24394 2609.24397 2609.24401 2609.24417 2609.24422 2609.24432
2609.24440 2609.24441 2609.24444 2609.24464 2609.24467 2609.24489 2609.24504 2609.24559 2609.24579 2609.24586
2609.24591 2609.24609 2609.24629 2609.24646 2609.24651 2609.24678 2609.24679 2609.24718 2609.24741 2609.24746
2609.24754 2609.24797 2609.24823 2609.24862 2609.24882 2609.24942 2609.24947 2609.24969 2609.24972 2609.24979
2609.24985
```
C（185）：

```text
2609.22087 2609.22088 2609.22092 2609.22094 2609.22095 2609.22097 2609.22100 2609.22101 2609.22103 2609.22105
2609.22119 2609.22128 2609.22131 2609.22132 2609.22134 2609.22136 2609.22138 2609.22139 2609.22141 2609.22142
2609.22143 2609.22144 2609.22149 2609.22150 2609.22151 2609.22161 2609.22162 2609.22164 2609.22171 2609.22172
2609.22174 2609.22179 2609.22188 2609.22189 2609.22195 2609.22206 2609.22208 2609.22209 2609.22212 2609.22215
2609.22219 2609.22223 2609.22224 2609.22225 2609.22226 2609.22227 2609.22228 2609.22234 2609.22260 2609.22262
2609.22294 2609.22299 2609.22323 2609.22337 2609.22338 2609.22342 2609.22349 2609.22376 2609.22377 2609.22478
2609.22484 2609.22486 2609.22510 2609.22534 2609.22547 2609.22566 2609.22576 2609.22592 2609.22642 2609.22654
2609.22663 2609.22674 2609.22684 2609.22734 2609.22750 2609.22757 2609.22760 2609.22767 2609.22771 2609.22812
2609.22839 2609.22843 2609.22880 2609.22897 2609.22913 2609.22950 2609.22951 2609.22959 2609.22983 2609.22991
2609.23016 2609.23017 2609.23038 2609.23048 2609.23065 2609.23074 2609.23085 2609.23094 2609.23097 2609.23141
2609.23163 2609.23164 2609.23170 2609.23206 2609.23212 2609.23223 2609.23232 2609.23252 2609.23269 2609.23290
2609.23321 2609.23334 2609.23340 2609.23371 2609.23376 2609.23377 2609.23383 2609.23385 2609.23449 2609.23476
2609.23574 2609.23582 2609.23596 2609.23650 2609.23658 2609.23668 2609.23697 2609.23701 2609.23703 2609.23716
2609.23731 2609.23753 2609.23766 2609.23773 2609.23819 2609.23837 2609.23885 2609.23915 2609.23917 2609.23926
2609.23937 2609.23950 2609.23967 2609.23970 2609.23971 2609.23980 2609.23986 2609.23988 2609.24021 2609.24064
2609.24112 2609.24126 2609.24128 2609.24137 2609.24138 2609.24156 2609.24161 2609.24205 2609.24260 2609.24280
2609.24302 2609.24377 2609.24379 2609.24384 2609.24423 2609.24443 2609.24455 2609.24480 2609.24517 2609.24528
2609.24556 2609.24569 2609.24621 2609.24703 2609.24736 2609.24749 2609.24750 2609.24770 2609.24791 2609.24814
2609.24840 2609.24890 2609.24929 2609.24954 2609.24983
```
### cs.DC

#### Mon21

N（11）：

```text
2609.21058 2609.21079 2609.21110 2609.21143 2609.21162 2609.21299 2609.21366 2609.21483 2609.21594 2609.21627
2609.21848
```
C（6）：

```text
2609.20874 2609.21057 2609.21173 2609.21281 2609.21419 2609.21728
```
#### Tue22

N（26）：

```text
2609.22142 2609.22358 2609.22443 2609.22674 2609.22753 2609.22755 2609.22814 2609.22978 2609.22991 2609.23278
2609.23301 2609.23321 2609.23438 2609.23454 2609.23536 2609.23773 2609.24018 2609.24161 2609.24205 2609.24294
2609.24456 2609.24628 2609.24639 2609.24713 2609.24802 2609.24991
```
C（11）：

```text
2609.22087 2609.22601 2609.22645 2609.22897 2609.23085 2609.23766 2609.23843 2609.24270 2609.24404 2609.24436
2609.24847
```
### cs.AI

#### Mon21

N（49）：

```text
2609.20971 2609.20974 2609.20981 2609.21061 2609.21096 2609.21113 2609.21139 2609.21149 2609.21157 2609.21165
2609.21181 2609.21192 2609.21208 2609.21214 2609.21221 2609.21259 2609.21263 2609.21267 2609.21293 2609.21325
2609.21390 2609.21423 2609.21432 2609.21470 2609.21486 2609.21492 2609.21493 2609.21509 2609.21519 2609.21548
2609.21599 2609.21600 2609.21619 2609.21626 2609.21672 2609.21677 2609.21683 2609.21748 2609.21755 2609.21801
2609.21811 2609.21841 2609.21863 2609.21924 2609.21940 2609.21962 2609.21996 2609.22068 2609.22086
```
C（76）：

```text
2312.01020 2412.07151 2511.16923 2608.27259 2609.20880 2609.20886 2609.20899 2609.20904 2609.20989 2609.21032
2609.21054 2609.21058 2609.21059 2609.21075 2609.21094 2609.21117 2609.21133 2609.21151 2609.21190 2609.21212
2609.21216 2609.21227 2609.21228 2609.21229 2609.21246 2609.21257 2609.21276 2609.21284 2609.21327 2609.21334
2609.21344 2609.21349 2609.21381 2609.21386 2609.21387 2609.21391 2609.21401 2609.21437 2609.21441 2609.21461
2609.21465 2609.21484 2609.21511 2609.21521 2609.21550 2609.21561 2609.21562 2609.21570 2609.21573 2609.21609
2609.21636 2609.21637 2609.21650 2609.21659 2609.21662 2609.21666 2609.21667 2609.21686 2609.21713 2609.21722
2609.21743 2609.21751 2609.21805 2609.21815 2609.21828 2609.21829 2609.21857 2609.21870 2609.21879 2609.21888
2609.21942 2609.21967 2609.21997 2609.22008 2609.22039 2609.22067
```
#### Tue22

N（111）：

```text
2609.22161 2609.22277 2609.22353 2609.22408 2609.22410 2609.22475 2609.22478 2609.22497 2609.22512 2609.22529
2609.22537 2609.22592 2609.22599 2609.22619 2609.22620 2609.22628 2609.22682 2609.22691 2609.22694 2609.22695
2609.22696 2609.22702 2609.22712 2609.22746 2609.22760 2609.22775 2609.22790 2609.22878 2609.22910 2609.22939
2609.22951 2609.22956 2609.22959 2609.22987 2609.23023 2609.23038 2609.23043 2609.23058 2609.23064 2609.23071
2609.23074 2609.23130 2609.23142 2609.23201 2609.23293 2609.23363 2609.23378 2609.23512 2609.23640 2609.23695
2609.23735 2609.23774 2609.23790 2609.23806 2609.23860 2609.23877 2609.23917 2609.23945 2609.23953 2609.23957
2609.23971 2609.23974 2609.23986 2609.23989 2609.24002 2609.24012 2609.24016 2609.24025 2609.24036 2609.24057
2609.24090 2609.24092 2609.24101 2609.24115 2609.24130 2609.24165 2609.24174 2609.24186 2609.24198 2609.24229
2609.24243 2609.24265 2609.24277 2609.24290 2609.24324 2609.24346 2609.24352 2609.24362 2609.24453 2609.24480
2609.24517 2609.24555 2609.24620 2609.24625 2609.24662 2609.24663 2609.24677 2609.24744 2609.24755 2609.24760
2609.24784 2609.24831 2609.24838 2609.24855 2609.24876 2609.24881 2609.24883 2609.24921 2609.24927 2609.24967
2609.24974
```
C（273）：

```text
2609.22101 2609.22144 2609.22170 2609.22175 2609.22178 2609.22184 2609.22192 2609.22194 2609.22195 2609.22196
2609.22197 2609.22198 2609.22199 2609.22200 2609.22204 2609.22207 2609.22208 2609.22218 2609.22219 2609.22221
2609.22222 2609.22237 2609.22239 2609.22241 2609.22243 2609.22244 2609.22245 2609.22246 2609.22247 2609.22248
2609.22249 2609.22251 2609.22252 2609.22253 2609.22254 2609.22255 2609.22256 2609.22257 2609.22258 2609.22259
2609.22261 2609.22262 2609.22264 2609.22271 2609.22281 2609.22282 2609.22283 2609.22284 2609.22285 2609.22293
2609.22295 2609.22302 2609.22308 2609.22327 2609.22329 2609.22332 2609.22333 2609.22359 2609.22375 2609.22377
2609.22379 2609.22409 2609.22463 2609.22476 2609.22538 2609.22554 2609.22566 2609.22573 2609.22582 2609.22586
2609.22588 2609.22601 2609.22603 2609.22609 2609.22611 2609.22647 2609.22664 2609.22688 2609.22700 2609.22705
2609.22719 2609.22724 2609.22747 2609.22770 2609.22771 2609.22792 2609.22793 2609.22796 2609.22813 2609.22818
2609.22834 2609.22850 2609.22851 2609.22868 2609.22869 2609.22870 2609.22880 2609.22882 2609.22884 2609.22886
2609.22894 2609.22913 2609.22917 2609.22934 2609.22942 2609.22944 2609.22947 2609.22949 2609.22961 2609.22967
2609.22971 2609.22974 2609.22981 2609.23008 2609.23016 2609.23039 2609.23065 2609.23073 2609.23087 2609.23103
2609.23117 2609.23121 2609.23139 2609.23152 2609.23156 2609.23182 2609.23193 2609.23215 2609.23260 2609.23267
2609.23307 2609.23314 2609.23315 2609.23321 2609.23333 2609.23360 2609.23381 2609.23383 2609.23387 2609.23397
2609.23407 2609.23421 2609.23423 2609.23442 2609.23444 2609.23457 2609.23465 2609.23466 2609.23492 2609.23508
2609.23529 2609.23539 2609.23549 2609.23553 2609.23565 2609.23582 2609.23587 2609.23589 2609.23590 2609.23596
2609.23600 2609.23601 2609.23643 2609.23665 2609.23680 2609.23687 2609.23688 2609.23700 2609.23716 2609.23726
2609.23766 2609.23789 2609.23808 2609.23825 2609.23853 2609.23875 2609.23876 2609.23889 2609.23892 2609.23894
2609.23910 2609.23925 2609.23951 2609.23954 2609.23980 2609.23997 2609.23999 2609.24026 2609.24061 2609.24083
2609.24084 2609.24089 2609.24094 2609.24103 2609.24124 2609.24127 2609.24137 2609.24151 2609.24152 2609.24156
2609.24161 2609.24202 2609.24238 2609.24241 2609.24246 2609.24259 2609.24274 2609.24280 2609.24289 2609.24298
2609.24302 2609.24322 2609.24348 2609.24357 2609.24359 2609.24369 2609.24372 2609.24380 2609.24385 2609.24401
2609.24417 2609.24424 2609.24433 2609.24444 2609.24446 2609.24452 2609.24456 2609.24485 2609.24487 2609.24489
2609.24504 2609.24515 2609.24538 2609.24559 2609.24586 2609.24609 2609.24627 2609.24629 2609.24631 2609.24644
2609.24646 2609.24651 2609.24660 2609.24669 2609.24688 2609.24691 2609.24698 2609.24706 2609.24710 2609.24725
2609.24742 2609.24746 2609.24757 2609.24768 2609.24799 2609.24801 2609.24814 2609.24815 2609.24847 2609.24859
2609.24862 2609.24864 2609.24890 2609.24906 2609.24942 2609.24955 2609.24965 2609.24969 2609.24971 2609.24972
2609.24976 2609.24984 2609.25001
```
### cs.CV

#### Mon21

N（74）：

```text
2609.20869 2609.20962 2609.20975 2609.21012 2609.21018 2609.21095 2609.21176 2609.21199 2609.21207 2609.21219
2609.21225 2609.21241 2609.21242 2609.21251 2609.21268 2609.21276 2609.21304 2609.21322 2609.21323 2609.21347
2609.21351 2609.21354 2609.21363 2609.21371 2609.21379 2609.21386 2609.21400 2609.21402 2609.21407 2609.21412
2609.21424 2609.21437 2609.21449 2609.21455 2609.21462 2609.21468 2609.21474 2609.21480 2609.21498 2609.21502
2609.21516 2609.21521 2609.21522 2609.21541 2609.21543 2609.21576 2609.21593 2609.21597 2609.21624 2609.21628
2609.21629 2609.21651 2609.21675 2609.21698 2609.21709 2609.21712 2609.21743 2609.21754 2609.21763 2609.21770
2609.21780 2609.21800 2609.21804 2609.21822 2609.21866 2609.21872 2609.21879 2609.21887 2609.21903 2609.21938
2609.22040 2609.22060 2609.22069 2609.22083
```
C（24）：

```text
2310.03860 2605.15418 2609.20826 2609.20839 2609.20850 2609.20892 2609.20905 2609.21000 2609.21169 2609.21186
2609.21228 2609.21246 2609.21369 2609.21391 2609.21392 2609.21511 2609.21595 2609.21683 2609.21811 2609.21812
2609.21813 2609.21849 2609.21948 2609.22086
```
#### Tue22

N（221）：

```text
2609.22267 2609.22271 2609.22272 2609.22281 2609.22282 2609.22283 2609.22284 2609.22291 2609.22293 2609.22295
2609.22302 2609.22308 2609.22315 2609.22323 2609.22333 2609.22351 2609.22379 2609.22392 2609.22479 2609.22500
2609.22506 2609.22562 2609.22582 2609.22588 2609.22631 2609.22641 2609.22647 2609.22687 2609.22688 2609.22706
2609.22716 2609.22750 2609.22762 2609.22788 2609.22789 2609.22807 2609.22834 2609.22849 2609.22857 2609.22868
2609.22896 2609.22897 2609.22913 2609.22916 2609.22941 2609.22942 2609.22947 2609.22950 2609.22967 2609.23003
2609.23005 2609.23010 2609.23012 2609.23017 2609.23026 2609.23049 2609.23061 2609.23067 2609.23121 2609.23139
2609.23153 2609.23161 2609.23169 2609.23182 2609.23184 2609.23248 2609.23249 2609.23268 2609.23286 2609.23336
2609.23345 2609.23352 2609.23369 2609.23372 2609.23380 2609.23386 2609.23397 2609.23404 2609.23408 2609.23409
2609.23425 2609.23427 2609.23431 2609.23436 2609.23442 2609.23450 2609.23478 2609.23492 2609.23495 2609.23507
2609.23509 2609.23533 2609.23534 2609.23541 2609.23548 2609.23553 2609.23561 2609.23565 2609.23566 2609.23586
2609.23592 2609.23596 2609.23600 2609.23601 2609.23606 2609.23619 2609.23655 2609.23658 2609.23673 2609.23679
2609.23714 2609.23715 2609.23717 2609.23733 2609.23753 2609.23758 2609.23769 2609.23796 2609.23815 2609.23817
2609.23830 2609.23832 2609.23881 2609.23961 2609.23967 2609.23983 2609.24014 2609.24026 2609.24031 2609.24049
2609.24058 2609.24064 2609.24071 2609.24075 2609.24088 2609.24095 2609.24098 2609.24109 2609.24116 2609.24125
2609.24127 2609.24136 2609.24151 2609.24158 2609.24170 2609.24172 2609.24190 2609.24193 2609.24204 2609.24208
2609.24210 2609.24215 2609.24220 2609.24223 2609.24226 2609.24228 2609.24244 2609.24276 2609.24287 2609.24308
2609.24312 2609.24313 2609.24330 2609.24337 2609.24359 2609.24367 2609.24379 2609.24384 2609.24403 2609.24409
2609.24424 2609.24452 2609.24455 2609.24468 2609.24470 2609.24482 2609.24485 2609.24487 2609.24492 2609.24494
2609.24510 2609.24524 2609.24526 2609.24531 2609.24537 2609.24539 2609.24560 2609.24564 2609.24565 2609.24595
2609.24612 2609.24619 2609.24626 2609.24627 2609.24634 2609.24668 2609.24691 2609.24727 2609.24732 2609.24736
2609.24737 2609.24768 2609.24769 2609.24782 2609.24787 2609.24788 2609.24813 2609.24814 2609.24825 2609.24839
2609.24850 2609.24872 2609.24875 2609.24879 2609.24894 2609.24919 2609.24937 2609.24981 2609.24984 2609.24997
2609.25001
```
C（51）：

```text
2512.04723 2609.22106 2609.22108 2609.22126 2609.22175 2609.22187 2609.22191 2609.22234 2609.22238 2609.22258
2609.22264 2609.22277 2609.22327 2609.22332 2609.22377 2609.22385 2609.22390 2609.22397 2609.22398 2609.22635
2609.22854 2609.22894 2609.23019 2609.23267 2609.23376 2609.23417 2609.23486 2609.23555 2609.23687 2609.23797
2609.23915 2609.23919 2609.23950 2609.23971 2609.24040 2609.24057 2609.24111 2609.24152 2609.24187 2609.24198
2609.24249 2609.24253 2609.24265 2609.24304 2609.24350 2609.24370 2609.24517 2609.24576 2609.24682 2609.24819
2609.24976
```
### cs.RO

#### Mon21

N（99）：

```text
2609.20892 2609.20965 2609.20970 2609.20980 2609.20983 2609.21000 2609.21005 2609.21008 2609.21015 2609.21022
2609.21024 2609.21026 2609.21045 2609.21046 2609.21059 2609.21082 2609.21099 2609.21100 2609.21107 2609.21112
2609.21114 2609.21122 2609.21130 2609.21138 2609.21155 2609.21167 2609.21178 2609.21185 2609.21186 2609.21211
2609.21212 2609.21216 2609.21220 2609.21223 2609.21226 2609.21228 2609.21229 2609.21246 2609.21275 2609.21307
2609.21316 2609.21319 2609.21330 2609.21358 2609.21365 2609.21369 2609.21377 2609.21396 2609.21404 2609.21416
2609.21447 2609.21448 2609.21461 2609.21467 2609.21482 2609.21497 2609.21504 2609.21511 2609.21514 2609.21572
2609.21580 2609.21584 2609.21609 2609.21617 2609.21621 2609.21650 2609.21659 2609.21690 2609.21707 2609.21716
2609.21718 2609.21726 2609.21729 2609.21734 2609.21740 2609.21744 2609.21751 2609.21753 2609.21761 2609.21767
2609.21777 2609.21787 2609.21788 2609.21792 2609.21803 2609.21817 2609.21818 2609.21838 2609.21883 2609.21908
2609.21929 2609.21942 2609.21948 2609.21982 2609.21983 2609.22062 2609.22073 2609.22075 2609.22085
```
C（15）：

```text
2609.20106 2609.20982 2609.21053 2609.21109 2609.21123 2609.21219 2609.21221 2609.21400 2609.21474 2609.21502
2609.21516 2609.21754 2609.21909 2609.22040 2609.22055
```
#### Tue22

N（182）：

```text
2609.22274 2609.22276 2609.22278 2609.22285 2609.22289 2609.22299 2609.22317 2609.22319 2609.22325 2609.22332
2609.22385 2609.22404 2609.22462 2609.22483 2609.22493 2609.22521 2609.22538 2609.22587 2609.22591 2609.22594
2609.22606 2609.22608 2609.22609 2609.22611 2609.22630 2609.22668 2609.22670 2609.22677 2609.22681 2609.22684
2609.22726 2609.22730 2609.22733 2609.22786 2609.22795 2609.22798 2609.22803 2609.22809 2609.22813 2609.22829
2609.22840 2609.22852 2609.22854 2609.22858 2609.22871 2609.22885 2609.22888 2609.22895 2609.22925 2609.22926
2609.22954 2609.22963 2609.22966 2609.22973 2609.22974 2609.22983 2609.23037 2609.23048 2609.23060 2609.23100
2609.23103 2609.23113 2609.23118 2609.23131 2609.23132 2609.23133 2609.23144 2609.23252 2609.23263 2609.23269
2609.23271 2609.23275 2609.23280 2609.23305 2609.23312 2609.23392 2609.23414 2609.23418 2609.23423 2609.23432
2609.23439 2609.23445 2609.23456 2609.23483 2609.23486 2609.23487 2609.23488 2609.23491 2609.23504 2609.23554
2609.23578 2609.23580 2609.23610 2609.23614 2609.23643 2609.23650 2609.23656 2609.23666 2609.23731 2609.23745
2609.23755 2609.23784 2609.23792 2609.23800 2609.23841 2609.23856 2609.23863 2609.23885 2609.23888 2609.23896
2609.23910 2609.23928 2609.23943 2609.23944 2609.23968 2609.23976 2609.23997 2609.24033 2609.24048 2609.24054
2609.24055 2609.24059 2609.24062 2609.24068 2609.24093 2609.24099 2609.24118 2609.24124 2609.24133 2609.24140
2609.24145 2609.24155 2609.24180 2609.24187 2609.24189 2609.24195 2609.24218 2609.24253 2609.24271 2609.24274
2609.24317 2609.24350 2609.24376 2609.24385 2609.24411 2609.24413 2609.24433 2609.24497 2609.24499 2609.24507
2609.24511 2609.24525 2609.24535 2609.24547 2609.24552 2609.24563 2609.24576 2609.24621 2609.24631 2609.24632
2609.24660 2609.24682 2609.24702 2609.24708 2609.24742 2609.24745 2609.24749 2609.24761 2609.24778 2609.24815
2609.24832 2609.24840 2609.24841 2609.24846 2609.24864 2609.24868 2609.24896 2609.24906 2609.24952 2609.24976
2609.24995 2609.24996
```
C（28）：

```text
2609.22108 2609.22173 2609.22277 2609.22292 2609.22335 2609.22338 2609.22678 2609.22857 2609.22919 2609.22967
2609.23003 2609.23151 2609.23157 2609.23352 2609.23356 2609.23454 2609.23478 2609.23541 2609.23565 2609.23566
2609.23673 2609.23786 2609.23797 2609.23961 2609.24312 2609.24452 2609.24626 2609.24787
```
### cs.AR

#### Mon21

N（4）：

```text
2609.21137 2609.21264 2609.21697 2609.21774
```
C（2）：

```text
2609.19639 2609.21157
```
#### Tue22

N（15）：

```text
2609.22335 2609.22343 2609.22347 2609.22590 2609.22636 2609.22743 2609.22765 2609.23116 2609.23444 2609.23816
2609.24270 2609.24288 2609.24757 2609.24847 2609.24904
```
C（4）：

```text
2609.22775 2609.23517 2609.24497 2609.24519
```
### cs.PL

#### Mon21

N（1）：

```text
2609.21284
```
C（0）：

```text

```
#### Tue22

N（5）：

```text
2609.23009 2609.23342 2609.23759 2609.23954 2609.24436
```
C（6）：

```text
2609.22220 2609.23032 2609.23854 2609.24252 2609.24345 2609.24628
```
### cs.OS

#### Mon21

N（0）：

```text

```
C（0）：

```text

```
#### Tue22

N（0）：

```text

```
C（2）：

```text
2609.23218 2609.23700
```
### cs.PF

#### Mon21

N（3）：

```text
2609.20874 2609.20957 2609.21681
```
C（3）：

```text
2609.21281 2609.21544 2609.21849
```
#### Tue22

N（1）：

```text
2609.23085
```
C（7）：

```text
2609.22114 2609.22636 2609.22781 2609.23130 2609.23790 2609.24639 2609.24991
```
### cs.IR

#### Mon21

N（5）：

```text
2609.21257 2609.21281 2609.21308 2609.21475 2609.22056
```
C（3）：

```text
2609.21018 2609.21547 2609.21863
```
#### Tue22

N（20）：

```text
2609.22150 2609.22227 2609.22655 2609.22747 2609.22770 2609.22880 2609.23111 2609.23115 2609.23162 2609.23307
2609.23354 2609.23449 2609.23646 2609.23677 2609.23718 2609.23849 2609.24152 2609.24407 2609.24430 2609.24613
```
C（19）：

```text
2609.22100 2609.22104 2609.22171 2609.22174 2609.22248 2609.22486 2609.22529 2609.22562 2609.22706 2609.22959
2609.23053 2609.23056 2609.23121 2609.23853 2609.23877 2609.23880 2609.23971 2609.24101 2609.24620
```
### cs.MA

#### Mon21

N（4）：

```text
2609.20887 2609.20889 2609.21570 2609.21997
```
C（3）：

```text
2609.21081 2609.21192 2609.21944
```
#### Tue22

N（5）：

```text
2609.22600 2609.23310 2609.24107 2609.24474 2609.24964
```
C（25）：

```text
2609.22111 2609.22130 2609.22194 2609.22212 2609.22235 2609.22251 2609.22292 2609.22592 2609.22668 2609.22678
2609.22682 2609.22726 2609.22833 2609.22944 2609.22949 2609.22951 2609.22993 2609.23137 2609.23269 2609.23454
2609.23790 2609.23875 2609.23928 2609.24006 2609.24012
```
