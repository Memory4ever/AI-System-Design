# Kimi CLI 1.39.0：Ch84 写后独立复核

范围仅为 04/25 release family 的 Books 写后 Gate；不替代全日来源覆盖、日期或语义复核。复核日期：2026-09-28。

- 官方 [1.39.0 release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0) 发布于 04/24 06:22 UTC，确在本日北京时间 04/24 09:00～04/25 09:00 窗口，且明确列出 `#2044` Skill scope-group/project override。它不能证明 PR 中每个思想在 release 日首次公开。
- 定点重开 exact tag 的 [`skill/__init__.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/skill/__init__.py)：默认 root 顺序 Project → User → Extra(config) → Extra(plugin) → Built-in，归一化同名 first-win；`skills_dirs` 显式指定时替代 Project/User 自动发现，随后仍可追加 config extra、plugin 和 built-in。并非所有运行模式都无条件 Project 优先。
- exact tag 的 [`config.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/config.py) 与 [`soul/agent.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/soul/agent.py) 支持配置进入 root resolution、discover、索引与 prompt 格式化路径；未执行测试或生产调用。
- 实际 [Ch84](../../../../../books/part-07-agent/84-agent-platform.md) 的新段位于 pre-admission chain 之后、competence-aware orchestration 之前，回答 catalog 名称如何解析为本次 Agent definition/run 使用的具体 Skill。来源/digest→prompt→run 是书稿提出的可审计设计合同，**不是声称 Kimi CLI 已实现完整 digest pin、run provenance 或安全 admission**。文中已区分解析优先级与信任/执行授权，保留恶意 Project 遮蔽、缓存/迁移成本及封闭 Skill set 共存边界；Ch59/72/83 的 registry/security/protocol owner 没有被抢占。
- 章末 Review notes 已列精确 tag、PR、有限证明和未运行测试；机制正文在 notes 之前，前后段衔接自然。`source-family` 锚点与报告一致。

**结论：**此单篇的 Books 写后 Gate PASS。仅能将 04/25 候选的 Books 状态改为“已吸收且非作者写后复核通过”；整日 Gate 仍须由日 owner 完成其他覆盖、受阻隔离及独立语义审计。此复核不证明外部历史目录无遗漏。
