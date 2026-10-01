# 2026-04-24 四项仅报告的有限非作者复核

复核者 root，2026-09-28。下列判断只验收指定 Source Family 的必要证据、评分与 Books 处置，不代替本日候选分母、日期或其余来源的 Gate。均使用 arXiv 精确 v1；未复现作者实验。

## 2604.21159v1 Adaptive Instruction Composition

[v1 正文](https://arxiv.org/html/2604.21159v1) §4–5 用组合 query/tactic 的特征训练 contextual bandit，在给定攻击生成与评价预算下改变探索/利用分配。旧随机组合在固定候选空间便宜、可重复；适应式选择带来额外 embedding、反馈与搜索成本。HarmBench 每行为至多 150 次尝试的累计命中不能写成单次攻击率；论文所报多样性 proxy 不证明风险空间全覆盖。对读 `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-SECURITY`，现有预算、风险分母和独立 sensor 已承载长期原则，但没有采用该 bandit 为默认评估器的证据。2+1+2=5；受限搜索操作点，仅报告；非作者必要命题复核通过。

## 2604.21829v1 Black-Box Skill Stealing

[v1 正文](https://arxiv.org/html/2604.21829v1) 的主目标是公开 `find-skills` SKILL.md，最多三次尝试后取最好输出；字面匹配、语义相似和经过过滤的接受集评价不是同一个泄漏分母。公开目标的行为复述不能独证私有后台文件被读取、所有 Agent 都泄漏，亦不能用接受集的残余分数宣称全流量安全。对读 `PLATFORM-SECURITY` 的 root secret identity、输出检测和累计尝试，已有原则不等于该 LAN 防线的实现或有效性已被 Books 接纳。2+2+2=6；受限接口风险与防线反证，仅报告；非作者必要命题复核通过。

## 2604.21725v1 AEL

[v1 正文](https://arxiv.org/html/2604.21725v1) §3–4 的快路径选择记忆策略、慢路径反思调整 prompt；默认 planner/tool 没有一起演化，测试阶段冻结 bandit、memory 与 evolution。208 episode 的金融组合实验及复杂变体退步只支持这个受限状态分工，不能推出开放环境持续改进或在线无害。对读 `AGENT-MEMORY` 与 `AGENT-WORKFLOW` 的记忆选择、执行状态和独立验证后，当前结果不足以改写其长期责任边界。2+1+2=5；仅报告而非宣称完整算法已有覆盖；非作者必要命题复核通过。

## 2604.21728v1 Ramen

[v1 正文](https://arxiv.org/html/2604.21728v1) §3–5 以每 query 重置保证缓存 support-gradient 与固定 base 参数身份一致；持续更新权重时，旧梯度不能直接继承这份正确性理由。适配当前 sample、第二次推理、检索和缓存仍需成本；490×只与朴素重复计算 support gradient 的局部路径比较，不是端到端吞吐或 SLO。证据限于 CLIP 视觉分类测试时适配；它没有跨模型资产、Serving 或 Agent Memory 形成系统边界，因此 System Reach 从 2 校正为 1，2+1+2=5。对读当前模型状态与缓存身份原则，不把该局部算法升格为通用 LLM 在线适配设计。仅报告；非作者必要命题复核通过。

这四项已有单篇处置，但整日报仍为 `进行中`，不得以这份有限复核宣称全部 91 个工作家族已独立验收。
