# Kimi CLI 1.39.0：有限非作者采用复核

范围仅为 2026-04-25 Daily 的同一 release family；不是十四来源、整日日期或 Books 写后 Gate。未运行测试，也未修改正式日报或 Books。

## 原始事件与必要实现

- [官方 release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0) 经 GitHub release API `releases/tags/1.39.0` 复核，`published_at=2026-04-24T06:22:19Z`，即北京时间 04/24 14:22:19，落在 `[04/24 09:00, 04/25 09:00)`。这是 release 的公开事件，不声称每个所含机制都在这时首次发明。
- [PR #2044](https://github.com/MoonshotAI/kimi-cli/pull/2044) 的官方 PR API 给出创建 `2026-04-23T17:06:02Z`、合并 `2026-04-24T05:22:34Z`；它并入该 release，不另计候选。
- 精确 tag 的 [`skill/__init__.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/skill/__init__.py) 中，默认自动发现顺序为 Project → User → Extra(config) → Extra(plugin) → Built-in；按 casefold 后的 Skill 名称首次命中获胜，随后按 scope 分组进入 prompt。**例外**：显式 `skills_dirs` CLI override 会替代 Project/User 自动发现并居最高优先级，因此不能把默认顺序写成无条件规则。
- 同 tag [`config.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/config.py) 的 `merge_all_available_skills=True`；[1.38.0 同文件](https://github.com/MoonshotAI/kimi-cli/blob/1.38.0/src/kimi_cli/config.py) 为 `False`。同 tag [`soul/agent.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/soul/agent.py) 实际调用 root resolution、Skill discovery 与 prompt formatting，说明优先级进入运行时组装路径，而不只是帮助函数或 UI 顺序。
- `skip_yolo_prompt_injection` 默认 false；相关 [PR #2028](https://github.com/MoonshotAI/kimi-cli/pull/2028) 只允许略去 yolo 系统提醒，不改变工具调用的自动批准/最终 effect 权限。Provider schema 拷贝与缺失 `type` 补全是同一 release 的另一有限兼容子命题，不是此 Skill 身份证明，也不能推任意 JSON Schema 语义等价。

## 准入、评分与实际知识 owner

独立结论：**单一 release family 准入成立；2+2+2=6 合理，按实际 Books 知识缺口深入审阅**。设计差异是同名多 scope 解析及默认合并改变选中哪份 Skill；系统影响横跨 artifact 来源、Agent definition 的 prompt 组装、run 实际加载身份与后续授权判断；这一身份/优先级合同有持续性。6 分本身不自动要求所有同分条目 Deep，本项是具体知识缺口触发。

`ROADMAP.md` 的 `AGENT-PLATFORM` → [Ch84](../../../../../books/part-07-agent/84-agent-platform.md) 为唯一正文 owner。实际 Ch84 已有 `agent_id + immutable version`、Skill registry 的 digest/publisher/权限/activation，以及 admission 不授予 runtime authority 的完整原则；但尚未把**同名多 scope 的解析规则、实际被选 Skill 的 source/digest、呈现给模型的 prompt 与 effect-time authority**串成可验收的 run identity。这是窄增量，不是“原章没有 Skill 治理”。Ch78 继续拥有 provider-facing Tool schema；Ch72 拥有供应链 enforcement，均不应复制本项 owner。

拟在 Ch84 Skill registry 与 Agent definition/run 交接处补：声明自动发现与 CLI override 模式、同名解析优先级和选中 artifact 的版本身份；prompt 列表和实际运行载入应指向同一 identity；项目优先只是该 CLI 的默认策略，**并非信任或权限优先级**，错误/恶意项目 Skill 仍可能遮蔽可信 Built-in。仍需 policy admission、effect-time 授权、回退/allowlist。当前官方源码与测试没有证明跨所有部署环境安全，也未证明运行时权限控制已因 PR #2044 自动加强。

这是 **source→actual owner 写前采用 PASS**；Books 仍未实际写入或通过写后复核，Apr25 Daily 仍进行中。正式日报中 `project/user/extra/builtin` 一语宜明确标为“默认自动发现模式”，并保留 `skills_dirs` override 与 Extra(config)/Extra(plugin) 的具体顺序。
