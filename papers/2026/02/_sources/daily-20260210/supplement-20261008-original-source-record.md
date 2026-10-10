# 2026-02-10原来源覆盖记录

仅保留2026-10-04有效检查事实，不代表2026-10-08增量验收；当前来源判断在README唯一覆盖表维护。

以下是实际有限检查，不支持“没有遗漏”。原始查询、响应和停止范围见 [原源首查](../_sources/daily-20260210/feb10_native_0.txt)、[首查续1](../_sources/daily-20260210/feb10_native_1.txt)、[首查续2](../_sources/daily-20260210/feb10_native_2.txt)、[首查续3](../_sources/daily-20260210/feb10_native_3.txt)、[恢复1](../_sources/daily-20260210/feb10_native_recovery_0.txt)、[恢复2](../_sources/daily-20260210/feb10_native_recovery_1.txt)与[正文定点恢复](../_sources/daily-20260210/feb10_native_final_1.txt)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 RSS 实际 1245 项；定点 02/09 GenAI.mil 与广告说明原文，未扩机构其他产品 | 已检查 | RSS/现页不是历史全站快照；已读两项无新增可采用技术机制 |
| SRC-ANTHROPIC | Research 当前首 10 条及本窗日期主题搜索，到当前首屏停止 | 受阻 | 首屏为后来的 9～10 月，未恢复本窗完整历史切片 |
| SRC-GOOGLE-AI | 官方 2026/02 Blog 月入口实际 8 条，02/09 Perch 原文；Research publications 年目录首屏 | 受阻 | Blog 可见切片已检查；publication 年目录未恢复本窗完整历史；Perch 属暂停的科学应用 |
| SRC-META-AI | Research 原页空响应与本窗日期限定检索 | 受阻 | 无可核历史列表，空响应不记零发布 |
| SRC-QWEN | qwenlm 旧入口重定向动态 qwen.ai；旧内容与本窗日期主题补检 | 受阻 | 动态历史目录未恢复，搜索无命中不当完整覆盖 |
| SRC-DEEPSEEK | 官网当前模型、官方 updates 入口与定点 cache complaint issue | 受阻 | 历史发布切片未恢复；用户问题不证明根因或新的系统机制 |
| SRC-MOONSHOT | Platform Blog 当前暴露旧条目；官方 kimi-cli 100 release API 覆盖相邻发布；1.10.0 Changelog 与 PR1039/1065 受影响文件 | 已检查 | 发布事件可确认；Platform Blog 完整历史切片仍有限 |
| SRC-TENCENT-HUNYUAN | Research 动态空文本；两次实际浏览器定点访问均 timeout（约65秒、73.6秒），GitHub/日期主题有限补检停止 | 受阻 | 本窗 Research 历史目录未恢复，不再无限重试 |
| SRC-ZAI | Research 动态空文本，官方 release notes 相邻 GLM5 为02/11窗外；日期主题补检 | 受阻 | 本窗研究目录历史切片未恢复 |
| SRC-BYTEDANCE-SEED | Research/Blog 与 public_papers 当前第1/13页、total242；限定主题/日期补检后停止 | 受阻 | 首屏为后来的论文，未恢复本窗完整历史 |
| SRC-BAIDU-ERNIE | 官方 Blog 暴露首10条，相邻02/06→04/15，有限本窗主题检索 | 已检查 | 仅暴露切片，无本窗条目；不证明其余历史目录无遗漏 |
| SRC-XIAOMI-MIMO | 官方 Paper 暴露8项，相邻02/03 HySparse、01/08 Flash 与03/13后项；Blog 当前条目 | 受阻 | 有日期论文切片无本窗事件；部分 Blog 无首公开日期 |
| SRC-MINIMAX | 英文 Blog 首12条，相邻01/27→02/12；中文技术页与 Agent Tech Blog 空响应 | 受阻 | 暴露列表无本窗事件，Agent 历史目录未恢复 |
| SRC-ARXIV | foundation/language model、Transformer/MoE、训练优化、Agent/RAG、World/VLA、kernel/accelerator主题有界查询与旧宽标题查漏；实际170完整题摘，原 API 失败；官方 cs.CL 2026-02 月列表与必要日期定点 | 受阻 | 月列表证明月份/身份不证明公告日；正常150项结合官方最早公告/ID注册上界条件落窗；早期12仍隔离，单字段不证明首次公开 |
| 补检：[DataCite](https://api.datacite.org/) | 仅已有具体身份的原 dates/created/registered 字段，不新增发现队列 | 已检查 | Available v1仅月，Updated精确秒语义非first-public，Created/Registered仅存在上界 |
| 表外：[NVIDIA PersonaPlex](https://research.nvidia.com/labs/adlr/personaplex/) | 仅06053项目先公开定点，原页明确Published Jan15,2026 | 已检查 | 本论文家族已有窗外公开，不移到本窗，原日精确时区未披露 |


