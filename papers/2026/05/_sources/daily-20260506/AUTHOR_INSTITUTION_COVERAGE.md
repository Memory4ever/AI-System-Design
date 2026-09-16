# 2026-05-06 Daily 机构来源覆盖

**窗口：** 2026-05-05T09:00:00+08:00 ～ 2026-05-06T09:00:00+08:00  
**检查日期：** 2026-09-14  
**角色：** 作者侧历史恢复；本文件不替代最终独立复核。

本轮只检查 `docs/RESEARCH_SOURCES.md` 的 Daily 机构来源，不扫描 Weekly 来源。网页能直接给出历史日期时，使用窗口前后相邻条目作为停止点；动态目录未在静态响应中暴露完整历史分页时，同时检查官方入口与限定官方域名的日期检索，并把“无法证明全站穷尽”保留为限制，不把空响应写成零更新证明。

| Source ID | 实际入口与停止点 | 结果 | 边界 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | `https://openai.com/research/`；读取研究索引并做官方域名的 2026-05-05/06 日期定点检索。 | 未发现落入窗口且改变本项目判断的发布。 | 当前索引不提供可复算的历史全量分页；只能支持本轮有界检查，不能证明站内绝对无事件。 |
| `SRC-ANTHROPIC` | `https://www.anthropic.com/research`；索引可见窗口前 2026-04-30 与窗口后 2026-05-07/08，边界间无条目。 | 0 个候选。 | 只证明官方研究索引的公开条目，不覆盖未公开材料。 |
| `SRC-GOOGLE-AI` | `https://deepmind.google/research/` 与 `https://research.google/pubs/`；检查窗口日期及相邻发布。 | 未发现范围内的大模型或其系统候选。 | Google 的经济/社会与领域应用研究不因机构身份进入本项目；动态索引不支持历史全量穷尽断言。 |
| `SRC-META-AI` | `https://ai.meta.com/research/`；检查研究索引及官方域名窗口日期。 | 未发现范围内候选。 | 当前页面未暴露可复算的历史分页停止点，结论限于本次有界检查。 |
| `SRC-QWEN` | `https://qwen.ai/research` 与 `https://github.com/QwenLM`；检查研究目录、发布记录及窗口日期。 | 未发现 2026-05-05 09:00～05-06 09:00 的新研究事件。 | 旧入口重定向到新目录；不能把当前目录缺少历史条目当成全站零事件证明。 |
| `SRC-DEEPSEEK` | `https://www.deepseek.com/` 与 `https://github.com/deepseek-ai`；定点检查窗口日期的官方研究/发布。 | 未发现范围内候选。 | 排除同名非官方仓库、社区 issue 与二手“V4”材料；它们不能作为 DeepSeek 官方事实。 |
| `SRC-MOONSHOT` | `https://platform.kimi.com/blog` 与 `https://github.com/MoonshotAI`；检查窗口日期与相邻官方更新。 | 未发现范围内候选。 | Blog 静态响应不含完整历史列表；保留有界检索限制。 |
| `SRC-TENCENT-HUNYUAN` | `https://hunyuan.tencent.com/research` 的“全部”目录与 `https://github.com/Tencent-Hunyuan`；按窗口日期定点检查。 | 未发现范围内候选。 | 研究列表由动态接口加载，静态 HTML 为空不作零命中证据；本结论合并页面实际目录检查与官方域名定点检索。 |
| `SRC-ZAI` | `https://www.zhipuai.cn/zh/research`；索引相邻日期为 2026-04-30 与 2026-05-11。 | 0 个候选。 | 日期停止点来自官方研究目录；未把 GitHub 普通提交当研究发布。 |
| `SRC-BYTEDANCE-SEED` | `https://seed.bytedance.com/en/public_papers`；窗口后首批可见条目为 2026-05-14/15/16。 | 0 个候选。 | 只覆盖官方论文目录；未扫描暂缓的 AI for Science 或一般推荐/广告研究。 |
| `SRC-BAIDU-ERNIE` | `https://ernie.baidu.com/blog/zh/`；相邻条目为 2026-04-30 与 2026-05-09。 | 0 个候选。 | 仅覆盖文心/ERNIE 模型、训练、推理与平台主题。 |
| `SRC-XIAOMI-MIMO` | `https://mimo.xiaomi.com/` 与 `https://github.com/XiaomiMiMo`；检查窗口日期和官方研究/发布。 | 未发现范围内候选。 | 官网动态页没有历史全量停止点；结论限于本次有界检查。 |
| `SRC-MINIMAX` | `https://www.minimax.io/blog`、`https://www.minimaxi.com/blog`；相邻可见日期为 2026-03-18 与 2026-05-26/27。 | 0 个候选。 | 未把产品公告或演示效果当机制研究。 |

## 作者侧结论

- 13 个到期机构来源均已执行；本窗未新增机构侧候选。
- 对 6 个不提供可复算历史分页的动态目录，结论明确限定为“有界检查未发现”，而不是“证明绝对没有发布”。这些限制不支持任何正面技术结论，也不改变 arXiv 候选分母。
- arXiv 的 493 raw identity、137 candidates、356 closures 与逐项 exact-v1 审阅单独记录在活动 ledger 和 `AUTHOR_EVIDENCE_COMPLETION.md`。
