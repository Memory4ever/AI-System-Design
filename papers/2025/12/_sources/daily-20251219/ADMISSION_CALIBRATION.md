# 12/19 首批准入校准

作者记录，非作者Gate待root。窗口[12/18 09:00,12/19 09:00)+08，实际2026-10-02读取。

## T5Gemma2官方release拟准入

[官方原Blog](https://blog.google/innovation-and-ai/technology/developers-tools/t5gemma-2/)本机全文核心可读，JSON-LD `datePublished=2025-12-18T18:30:00+00:00`，即12/19 02:30+08落窗；`dateModified=2026-03-19T17:48:17.592801+00:00`，当前HTML非不可变2025快照。独立release事件，不把Blog时刻授arxiv first-public。

约束→新增→选择：encoder-decoder重复embedding及分别self/cross attention有参数/执行成本→T5Gemma2在Gemma3初始化/UL2适配基础上tie encoder/decoder embedding并合并decoder self/cross模块→需要核合并attention归一化/接口及表示效率边界，不能仅按参数总量替代质量/成本比较。作者拟2+2+2=6，非声望评分。原v1 [2512.14856](https://arxiv.org/abs/2512.14856v1)完整题摘实际可得，必要机制/消融继续；不等待无关来源才校准。

原Blog明确只发布pretrained checkpoints，minimal SFT无RL仅用于illustration；pre/posttraining benchmarks不同，图分数不可横比。270M-270M实际约370M total excluding vision encoder等结构事实不误当算力收益。需root核具体准入是否由实际模块变化成立；Books尚未判整项覆盖/仅报告。

## 代表负侧

- [DOE合作](https://openai.com/index/us-department-of-energy-collaboration/)标题/官方core为Genesis scientific MOU，当前ROADMAP AI-for-Science暂缓，范围关闭；不能由基础设施/Agent词重引入科学领域合作。
- [Anthropic DOE合作](https://www.anthropic.com/news/genesis-mission-partnership)同样能源/生物/科研productive领域合作、拟未来tools，范围关闭，不把愿景当执行机制。
- [Academy prompting event](https://academy.openai.com/en/public/events/prompting-with-purpose-best-practices-and-techniques-for-chatgpt-ieknhgy22u)是培训活动/既有prompt指南，非新增模型系统研究。
- T5Gemma2新语言数/排行榜本身不另立家族。已知Flash Blog12/18 00+08在本窗外；不复制18准入结论。

## 新潜力待普通阅读

GPT5.2Codex release/addendum、ProjectVend2、wellbeing评价、AgentSkills跨平台standard update具名恢复，核心/必要version/dates仍在执行。arXiv四收窄查询实达无Next：language133、system3、multimodal31、ML语义compute41，均submitted缓冲非public池；完整相关题摘及官方精确ID段补检继续。
