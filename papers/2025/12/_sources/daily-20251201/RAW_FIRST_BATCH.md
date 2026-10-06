# 12/01 原始来源观察与停止点

检查时间：2026-10-02T17:28:13+08:00 起。固定窗口：[2025-11-30T09:00:00+08:00, 2025-12-01T09:00:00+08:00)。只记录实际观察；检索无命中不等于原站完整覆盖。

## 首批线索

1. 查询 `site:arxiv.org (multimodal OR "world model" OR "vision language") after:2025-11-29 before:2025-12-02` 及 `site:arxiv.org (agent OR reinforcement OR reasoning) "2025" "Nov 30"`，每查询首轮结果，未翻辅助搜索结果页。恢复 AVWM 2512.00883、HMLM 2512.00696、NavForesee 2512.01550、Real-World Robot Control 2512.01924。索引显示的是 submission 线索，不是 first-public。准入判断见 ADMISSION_FIRST_BATCH.md。未做整月检索。
2. AVWM 官方精确 v1 页面 HTML metadata：`citation_date=2025/11/30`、`citation_online_date=2025/11/30`；官方 submission history：`Sun, 30 Nov 2025 13:11:56 UTC`。字段都与提交日同值，且无时区/时刻，不能证明落窗。当前 abs 是 v4，版本串和题名已变化。
3. arXiv 题摘 API/网页工具一度失败，原站终端可访问。高级搜索参数 `terms-0-field=all; terms-0-term=large language model; date-filter_by=date_range; date-from_date=2025-11-30; date-to_date=2025-12-01; date-date_type=announced_date_first; size=50; start=0`。实际返回 `Showing 1–50 of 2,523 results`，首项 2511.23478、2511.23477，v1 submitted 28 November，originally announced November 2025。本次页面支持的日范围不等于索引真正支持日公告；停止，不把 2523 转为待审库存。
4. 定点用 ID=2512.00883 与同一 announced 日期范围检索，页面帮助明确：`announcement date supports only year and month granularity`。没有把空响应作为零候选证据。月级列表 `https://arxiv.org/list/cs.CL/2025-11?skip=0&show=25` 的 1–25/1527 仅为月身份；错误短格式 `/2511` 404；长格式可达。尝试 `/2025-11-30` 原站 HTTP400。都不提供历史单日公告身份，未翻全月分页。
5. `https://arxiv.org/list/cs.MM/2025-12` 首屏 1–50/110，定位 AVWM 月归属后停止；该目录不证明精确日期，不审无关条目。

## 14 每日源首查及有限恢复

| 来源 | 实际入口/停止位置 | 原始观察与边界 |
| --- | --- | --- |
| SRC-OPENAI | Research 首屏；news/research 首屏；限定 `site:openai.com/index (research OR model OR training) after:2025-11-29 before:2025-12-02 -site:community.openai.com` 一轮 | 当前首页为 2026，辅助查询返回 Nov20 science、旧 alignment 等窗外材料；初次宽 domain 命中社区用户帖，已经收窄，不当官方研究。历史目录尚未恢复，不能宣称无遗漏 |
| SRC-ANTHROPIC | Research 首屏；限定 research 域同一日期一轮；`research?search=2025` 恢复尝试 | 当前首屏为 2026；Dec2 How AI is transforming work 为窗外线索；参数入口不可达，历史完整性未证明 |
| SRC-GOOGLE-AI | DeepMind Research、Google pubs 首屏；Google blog/2025 第1页至 Nov12 | Google blog/2025 第一页相邻发布为 Nov21、Dec3，未见本窗 Blog；pubs 只有年字段不能证明 first-public，DeepMind 历史入口待恢复；不把 Blog 无事件扩为全部 publications 无事件 |
| SRC-META-AI | 官方 Research 空正文；窗口限定 query 首轮 | 原始入口空正文；恢复 PEER August24 2022、GRAPE Sep8 2025 等窗外材料；目录历史覆盖未证明 |
| SRC-QWEN | qwenlm.github.io 首屏；qwen.ai/blog；窗口限定 query 首轮 | 旧站首屏止于 Sep23；新站空正文，未获得窗内事件；不是完整历史零命中 |
| SRC-DEEPSEEK | deepseek.com；链接进入 V3.2 官方仓库（当前 redirect 至 V3.2-Exp） | 首页无历史日期；仓库 Update 明确 2025.11.17 indexer RoPE 非交错布局修正，为窗外纠错信号；未冒充本窗事件；news 路由转当前 API 首页 |
| SRC-MOONSHOT | platform.kimi.com/blog 完整 Overview；changelog 全页 | 最近条目为 Nov7，changelog 最新段 Nov6，未見本窗更新；停止于目录末 May29 2024，不扫描机构完整历年论文 |
| SRC-TENCENT-HUNYUAN | research 网页工具2次超时；浏览器创建超时；终端原站 HTML及部署JS | 原站终端可达，但 HTML 只有 skeleton，正在恢复 All 目录接口；不是外部终态，不把 HTTP200 当论文目录已读 |
| SRC-ZAI | zhipuai.cn/zh/research 网页超时；docs.z.ai/release-notes/new-released | release notes 相邻为 Sep30 GLM4.6 / Dec8 GLM4.6V；未见本窗 release。Research 独立目录尚待恢复；news 是企业/融资，不代替研究目录 |
| SRC-BYTEDANCE-SEED | en/research；en/public_papers 首屏1–20/242；窗口限定 query 首轮 | Research 指向 Dec2 GR-RL，晚于本窗；public_papers 停第1/13页，正在恢复历史日期段，不把首页当覆盖完成 |
| SRC-BAIDU-ERNIE | blog/zh 首屏，至Nov21条目及分页链接 | 相邻可见 Nov21 / Dec9，无本窗 Blog；待读第2/2页确认连续停止位置 |
| SRC-XIAOMI-MIMO | 首页 Paper 全部8项；Blog 首屏15项；精确日期 query 首轮空 | Paper 相邻 Oct21/Jan8，无本窗论文；Blog 不给日期且有More，仍有恢复项，不能仅据搜索空响应关闭 |
| SRC-MINIMAX | 英文Blog全部13项及中文原入口redirect minimax.cn/blog | 相邻 Oct27 M2 / Dec23 M2.1；中文亦同段且含Jan15，未见本窗Blog；没有因首页较旧记不适用 |
| SRC-ARXIV | 上述官方主题查询、月列表定位、精确ID恢复 | announced 日期仅月粒度；继续有界主题/提交窗发现与具名 first-public 恢复，不支持本窗无遗漏或公开时刻断言 |

## 仍可执行的工作

恢复 Research 动态目录、Seed 历史分页和 arXiv 主题切片；补原始公开日期，明确目录有限恢复的结果。上述待办未冒称外部受阻。首批准入校准只涵盖 ROOT_ADMISSION_REVIEW.md 明确的两项。
