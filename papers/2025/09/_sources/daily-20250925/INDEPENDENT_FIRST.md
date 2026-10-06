# 2025-09-25 局部非作者 FIRST

复核者：sept07_10_author；本日作者 James（sept22_25）。只校准已请求的 Robotics 家族及 Qwen3-Max/Pulse/Germany 三项代表关闭，不授日级、Evidence 或 Books 通过。

本日重新完整读取 AGENTS、Prompt、Research/Report 合同、来源使用说明 Daily/arXiv、ROADMAP 和本日 checkpoint/README/scan。窗口 09/24 09:00～09/25 09:00+08。实际读 DEEPMIND_ROBOT.txt 的完整发布核心、raw 的两个原日期字段、robot-report-cover.txt 全标题/摘要及 pp1–2 引言、Qwen 原窗口配置与完整核心；另独立打开 Pulse/Germany 两原官方主体，保存在 INDEPENDENT_FIRST_CORE.json。未用09/16日期、候选或来源声明作本日证据。

## Gemini Robotics 1.5：准入通过，2+2+2=6

原 Blog 的 article:published_time 与 JSON-LD datePublished 均为 2025-09-25T00:00:00+00:00 → 北京25日08:00，完全落窗；dateModified 不替代此公开字段。PDF Creation/Mod 只识别取得版本，不授公开时间。

最小贡献链：直接 instruction→motor 的 VLA 面对多阶段语义任务与异构机器人动作数据的约束 → 本文报告多层自然语言 thought/action 交错和 Motion Transfer，以 multi-embodiment pretraining 对已训练 ALOHA/Franka/Apollo 不做 robot-specific post-training、跨身体转移技能 → 需要核推理/动作联合监督与训练覆盖限定下的迁移设计。不是成熟 ER planner+低层 VLA 组合本身，也不借15榜总指标或机构声望准入。

Design Delta 2：有具体动作策略与迁移机制，不先授改变全部VLA设计结论；System Reach 2：涉及动作表示/训练数据到不同已训练硬件上的执行边界，不把可联想多章节计3；Durability 2：可复用的监督/迁移边界，不只是发布API事实。合计6，最低标准审阅。涉及安全约束的拟采用命题仍须按合同深入核受影响内容，不因6分免除ASIMOV/物理安全反侧。

作者下一步只沿这两个已明确潜力读必要方法、对照与限制：区分思维生成/动作交错的实际训练标签、频率/预算/语义正确性；Motion Transfer的动作空间/数据覆盖/隔离任务/对照和代价；跨已训练身体的新技能不等于任意新机器人零数据适配。可见thought不证明faithfulness/因果解释。若要用ASIMOV，核新版风险定义/tail/annotation/问答与视频协议、evaluator及安全对照；benchmark改善不证明低层碰撞安全。伙伴权限与视频demo不授生产验证。正文未读完是普通待办，不转外部终态。

Owner 路由可先定位 MULTIMODAL-EMBODIED-VLA Ch26；未比较实际章/邻接，不授整合、已有覆盖或正文提案通过，也不要求作者现在遍历62页无关内容。

## 三个代表关闭：通过

- Qwen3-Max：完整Introduction/Base/Instruct/Thinking/Develop/References已有实际原核心。沿用Qwen3 MoE/global-batch及已发表ChunkFlow；named PAI-FlashMoE pipeline/SanityCheck/EasyCheckpoint未解释本次新增执行/恢复算法，30% MFU、3x吞吐、故障时损1/5缺可比运行/基线约束。对本文披露不能建立新的模型系统机制或质量/资源边界，关闭贡献；不是因为规模大、发布或未开源。若原named方案出现具名新机制只重开相应点，不扩旧ICML全文。原配置2025-09-24T04Z落窗且无draft标志，不把这里日期继承给其他条目。
- Pulse：实际原主体§Made for you、You decide、Meant to work、Limitations核夜间memory/history/feedback异步研究、默认关闭connector、一天有效/保存为chat、curate/反馈和已完成项目仍推荐的限制。未披露新的执行、恢复、时效识别/可靠性机制；产品组合不授新系统增量。保留权限默认off与stale反馈边界，不把safety checks当有效安全保证，也不因叫主动Agent而准入。
- Germany：实际原主体为计划2026合作、Delos/Azure部署与4000GPU扩容，主权、隐私和韧性是承诺，未披露新的密钥/隔离/模型执行或风险接受机制。关闭本次技术贡献；不能把承诺当已经验证的系统约束。

上述校准允许作者立刻推进受影响必要审阅；本日其他来源/题摘/身份筛选、候选终表、Books及独立DAY均未在本FIRST验收，保持普通待办。
