# Daily Research — 2026-10-28

**规范：** V3
**窗口：** 2026-10-27 ～ 2026-10-27
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-10-28T15:06:47+08:00

## 1. 结论

本日恢复暂停任务，尚未完成arXiv来源筛选及其必要证据/Books判断，不声明全日闭环。当前表中九家族已安全处置：八家族真实整合、一个具体已有覆盖，全部通过实际独立复核；kimi-code的四个合入事件只计一个家族。这不是最终候选分母。已改Ch18、19、25、33、75、77、78、81、83、84，保留原有内容及证据；其他arXiv拟候选的普通审阅与书稿判断仍在继续。

当前重要边界是：人工签字不自动构成独立判断证据；世界生成的演示能力不证明物理因果有效；运行时缓存、交互恢复与MCP连接重试需要区分各自状态和提交责任。arXiv类别导航中的原始数量不代表本日有同等数量的项目贡献。

## 2. 来源覆盖

机构的实际入口、停止位置与缺口见[ORG](../_sources/daily-20261028/ORG.md)，中国来源见[CHINA](../_sources/daily-20261028/CHINA.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research index首屏最新Oct26，日期早于窗口停止 | 已检查 | 不声称全网零发布 |
| SRC-ANTHROPIC | Most recent至Oct23，Oct27判断实验与drug development定点筛选 | 已检查 | 药物应用按暂缓范围排除 |
| SRC-GOOGLE-AI | DeepMind News Oct27 Genie4；Research Blog Oct27 Sleep为旧稿介绍 | 受阻 | Pubs完整Oct27日级目录无法恢复；与已核原件隔离 |
| SRC-META-AI | Research空正文；替代Publications混旧年，有限官方域查询未恢复当日目录 | 受阻 | 需可复查官方Oct27目录或具名原始发布，不授零发布 |
| SRC-QWEN | 旧站迁新站，qwen.ai动态Blog正文未恢复，有限公开脚本恢复未成功 | 受阻 | 需新站可读本窗目录或官方快照，不授零发布 |
| SRC-DEEPSEEK | 官网研究与动态首项均早于窗，停止旧页扩张 | 已检查 | 无全站无遗漏保证 |
| SRC-MOONSHOT | Platform Blog与发布页最新窗外；唯一窗内更新kimi-code定点9commit、完整核心筛选 | 已检查 | 四事件Books判断进行中，不改旧提案首次公开日期 |
| SRC-TENCENT-HUNYUAN | 中文Research空提取，root与子智能体浏览器失败，有限公开脚本恢复未成功 | 受阻 | 需中文“全部”可读列表/快照；不借英文目录授覆盖 |
| SRC-ZAI | 中文Research时间序首项Aug26，release notes同日；停止旧项扩张 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Publications最新Oct25、首屏1–20/247；首Blog SeedRealtime正文Aug05 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 中文Blog第1页首项May09，早于窗停止 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 首页Paper首Jun29、Blog首篇正文Sep27，均窗外 | 已检查 | 无 |
| SRC-MINIMAX | 中英文Blog首Oct22、Agent Tech首Oct20，均窗外 | 已检查 | 无 |
| SRC-ARXIV | `/new`已滚到Oct28，改用注册12类别pastweek明确Oct27日段；跨类导航去重后按主题分工 | 未完成 | 相关题摘语义初筛、首公开/修订归属与必要证据尚未全部处理；不将crosslist日当首公开 |

## 3. 候选与判断

此表先列已完成首批准入的机构/工程家族；arXiv尚在筛选，不假装冻结最终分母。kimi-code四事件同一家族，以下按事件给出原文新增命题和最低投入，不将分数相加。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [How AI agents shape experts’ judgment calls](https://www.anthropic.com/research/agents-judgment-calls) | 2026-10-27 | 随机Agent偏好影响可辩护分析选择，人工参与不保证判断独立；2+2+3=7 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)，HITL双人批准之后 |
| [Genie4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) | 2026-10-27 | 观察帧—目标拆解—caption控制的有限反馈接口；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，Reason-then-Render及Control flow/observed-imagined边界 |
| [kimi-code](https://github.com/MoonshotAI/kimi-code) | 2026-10-27 | 四合入事件：[4456](https://github.com/MoonshotAI/kimi-code/pull/4456)预算触发/目标与前缀投影分离6；[4428](https://github.com/MoonshotAI/kimi-code/pull/4428)pending恢复/事实重放分离6；[4283](https://github.com/MoonshotAI/kimi-code/pull/4283)弱活性证据/attempt隔离6，以上均2+2+2；[4450](https://github.com/MoonshotAI/kimi-code/pull/4450)软授权措辞反例1+2+2=5 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md)、`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)、`AGENT-MCP` [Ch83](../../../../books/part-07-agent/83-mcp.md)、`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，四实际写后均已核 |
| [LoopFold: Parallelizing Recurrent Depth in Looped Transformers](https://arxiv.org/html/2610.35556v1) | 2026-10-27 | 同前缀后续loop预测/校正换并行stage，不保证原轨迹精确；2+2+2=6 | 深入完成 | 整合：`MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md)，重复主干的状态与串行深度分支；实际写后已通过独立复核 |
| [StateLoop: Persistent State for Looped Transformers](https://arxiv.org/html/2610.35544v1) | 2026-10-27 | 独立per-token loop工作状态与直接主干路径分责；1+2+2=5 | 深入完成 | 整合：`MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md)，重复主干的状态与串行深度分支；实际写后已通过独立复核 |
| [ScaleRLT: Exact Log-Probabilities and Fast Deferred Rollouts for Reinforcement Learning on Looped Transformers](https://arxiv.org/html/2610.34427v1) | 2026-10-27 | 相同schedule/kernel/batch重放供值、dense供梯度，严格gate不等质量收益；3+2+2=7 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)，MoE Route Replay之前；实际写后已通过独立复核 |
| [LSTM-Style Looped Transformers with Shared KV Caches](https://arxiv.org/html/2610.33360v1) | 2026-10-27 | 并行训练的donor与部署递归生产cache历史不等价；2+2+2=6 | 深入完成 | 整合：`MODEL-KV-CACHE` [Ch19](../../../../books/part-02-model/19-kv-cache.md)，Depth-wise sharing后的生产历史；实际写后已独核 |
| [The Price of Scale in Proactive Memory Recall](https://arxiv.org/abs/2610.34507) | 2026-10-27 | 固定主动提醒阈值随store规模累积null max，cue-swap需同源可交换校准；2+2+3=7 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)，主动介入段后/PASK前；实际写后已独核 |
| [WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU](https://arxiv.org/html/2610.35529v1) | 2026-10-27 | 可预知访问与后台分层KV把总容量/带宽/位置horizon分开；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，WorldKV后的分层分支；实际写后已独核 |

## 4. 证据与知识整合

### [How AI agents shape experts’ judgment calls](https://www.anthropic.com/research/agents-judgment-calls)

采用官方PDF方法、Table2及相关附录的有限随机lean反例，不把自主使用/不用AI的组间差当随机因果。四项分析选择与最终政策选择须分开，后者区间跨零；单任务、单模型与领域外专家限制外推，晚注册及未独立恢复注册原件也不写成严格前瞻注册。新增书稿解释：多人批准可以核验身份与流程，却未必提供独立判断；共同受Agent framing影响时不能把人数当独立证据数。防御建议尚未经过该研究验证。完整证据和实际写入位置见ORG末节，唯一非writer已核实际保存态，未复现实验。

### [Genie4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)

采用官方核心与限制段，仅支持观察生成帧并调整生成控制的架构描述；没有训练实现、控制消融或独立物理有效性证据，运行配置Not Disclosed，不报告通用性能数字。Ch25已有语言计划与生成分工、observed/imagined差别、短时反馈与长程漂移边界；产品原生音频与演示更新不足以新增长期论点，故不改书。

### [kimi-code](https://github.com/MoonshotAI/kimi-code)

精确SHA、必要实现/test定义及反证见CHINA §5。已独核，但本次没有运行测试，不把作者测试或源码存在写成生产效果。PR先前已公开者只采用Oct27合入的实现/兼容事件，不改成论文首次公开。#4450反例来自作者有限小样，不作普遍措辞定律；#4428旧客户端404与取消reason限定、#4283重连不证明副作用幂等、#4456估算不足仍须reactive回退均保留。四章真实写入与实际独立写后通过见CHINA §7及REVIEW。

### [LoopFold: Parallelizing Recurrent Depth in Looped Transformers](https://arxiv.org/html/2610.35556v1)

精确v1 §3–5，预测后续输入后并行执行，再按新到前轮状态校正，优化预测而非顺序轨迹相等。原文分别配平训练FLOPs、延迟和目标深度，低计算预算反侧及额外KV/FLOPs保留；不外推标称加速。Ch18现有循环监督/停止不承载该执行分支，新增自然段，实际保存已成、实际独立写后已通过。原始版本/日期组合证据见[模型审阅](../_sources/daily-20261028/ARXIV_MODEL_REVIEW.md)。

### [StateLoop: Persistent State for Looped Transformers](https://arxiv.org/html/2610.35544v1)

精确v1 §3–5，保主干直连之外的门控state；同配置reset仍有收益，持续保留才是其上额外增量。可选token混合器另增缓存，不把当前token跨loop工作state当全部历史KV替代。因具体表示接口差额按5分深化到控制与限制，Ch18已真实补段，实际写后已独核；不报跨模型通用收益。

### [ScaleRLT: Exact Log-Probabilities and Fast Deferred Rollouts for Reinforcement Learning on Looped Transformers](https://arxiv.org/html/2610.34427v1)

精确v1 §2–7.4/10，实际核同schedule replay、stop-gradient式和kernel/batch改变的反证；dense梯度只在测量精度级可比，不能称完全等价。原生深读出质量/达标时间反侧、短任务ungated质量不差以及额外replay费均入采用边界。Ch33已有一般precision/route身份但缺供值/供梯度分工，新增一段、实际写后已独核；不把严格gate等同准确率改善。

### [LSTM-Style Looped Transformers with Shared KV Caches](https://arxiv.org/html/2610.33360v1)

精确v1两遍训练的cache producer与递归continuation不同，即使teacher-forced输入也不消除此差额。末段donor一致性只作局部修复，不保证任意历史等价或更好生成。Ch19补该生产路径差额、双遍费用/full-cache质量代价及实际decode变慢反侧，唯一非writer已核正文、两侧与本人注。日期组合原字段见模型日期/审阅记录，不以提交日单独归属。

### [The Price of Scale in Proactive Memory Recall](https://arxiv.org/abs/2610.34507)

精确v1 §3–7/T1/AppA–E支持store-size/null-max与ROC尾部约束，cue-swap仅对可交换cue/store的marginal保证，不是连续时间FWER；K限制可达p值。LoCoMo跨会话reference失配、同会话更保守却损hit均保留；不采用Prop6一般stochastic-dominance扩展。离线模拟、1human+2LLM、未运行artifact。Ch77原controller成本/always-off未覆盖该统计差额，已补实际段并通过写后独核。

### [WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU](https://arxiv.org/html/2610.35529v1)

精确v1必要方法、读写/检索接口与质量/限制段支持分层持久KV及pose外推预取；never-wait未命中时沿用旧集合，属于新鲜度与等待的取舍。原单机零storage stall不含反量化/写回，低带宽预取P99可劣于按需换入，长间隔质量仍损、native位置编码上限独立。Ch25已补具体分层分支并通过实际写后复核；不授实时、长期一致性或实机复现。详见[多模态实际审阅](../_sources/daily-20261028/ARXIV_MULTI.md)。

## 5. 缺口与下一步

普通待办：arXiv主题初筛与首公开/修订归并、其余候选必要审阅与Books判断；全日报告同步、校验和独立验收。不得把这些改成外部受阻后归零。

隔离外部保留项：Google Publications、Meta、Qwen新站与浑元中文“全部”目录完整性，缺少本窗可读官方目录/快照，当前不支持无遗漏、零发布或未见机制的正面采用。可接受替代为具名原始当窗发布或合法官方日目录快照，定点重开对应来源，不重跑已成材料。相关失败路径见ORG/CHINA。

本次不恢复10-27日报或2025任务。10-28验收后再按用户授权接回2026已有Daily补遗漏，保留旧候选日期/评分及有效证据。

## 6. 复核

复核者：`/root/live1028_review`。结论：未通过（全日未完），非最终验收。

已独核机构两项及kimi-code四事件准入、必要证据；Anthropic实际Ch81写后检查及Genie4具体已有覆盖通过。抽查纠正#4450/#4451“无评价”误述，前者有限反例改准入，后者无新旧效果分离维持排除；不据修复标签或提示词类别机械排除。arXiv及全日范围尚未完整验收，具体已完成层见[REVIEW](../_sources/daily-20261028/REVIEW.md)。机器校验尚未执行，不把局部通过冒为全日完成。
