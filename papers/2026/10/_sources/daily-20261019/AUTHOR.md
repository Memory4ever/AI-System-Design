# 2026-10-19 Daily：作者原始检查与边界

作者：`daily_20261019_author`。独立复核者：root（不由作者代签）。
窗口：北京时间2026-10-18完整自然日。执行：2026-10-19 17:26～17:38 +08:00。
只处理14个每日来源；不恢复暂停的2025/2026历史补查，不写Books/LEARNING_STATE，不stage、commit、push，不创建Weekly。

## 方法与原件

已重读AGENTS、Prompt、研究合同、Report合同、来源使用说明/每日组、ROADMAP及本日路由；本日原报告不存在。
`fetch_sources.py`仅用于获取原始响应、提取可见文本，网络并发2，每请求15秒，无无限重试。`.raw.html`保存原始HTTP实体（也可能是XML/JSON/JS），`.visible.txt`为机械提取，不自动构成内容审阅。
`fetch_results.json`为首轮15入口（Google双入口）的执行结果；后续`fallback_results.json`只保存最后一批，较早批次实际结果以下述原件和本记录为准，不冒充它包含完整历史。
DeepMind首轮返回gzip而最初未解压，`deepmind.visible.txt`无效，不用于结论；修正后`deepmind_fixed`及`deepmind_blog`原件有效。arXiv月表仅意外获得的宽导航，不转换成1947项题摘/全文队列，不声称已逐项审阅。

## 有界来源结果

| 来源 | 实际入口、停止位置与观察 | 本轮边界 |
| --- | --- | --- |
| SRC-OPENAI | Research首次TLS EOF，改用官方`https://openai.com/news/rss.xml`；`openai_rss.raw.html`完整XML1299个item，逐pubDate转Asia/Shanghai，Oct18为0，最新Oct16 GMT | 完整该RSS，不能证明所有独立渠道都零发布 |
| SRC-ANTHROPIC | `anthropic`原件Publications首10从Oct16至Oct8，最新批无Oct18，停See more前 | 不扩扫旧页 |
| SRC-GOOGLE-AI | `deepmind_fixed`研究总览、`deepmind_blog`首6个October卡；Argon/safety/robotics原页Oct13、EmbeddingGemma2 Oct6、scam Oct14；antimicrobial标题已明AI for Science不追日证。`google_research_blog`最新列表从Oct16回溯；`google`出版目录仅第1页15/11622，按年份标记，不用其作日级完整列表 | Research publication目录无日级断言；Blog只实际页内范围 |
| SRC-META-AI | Research原件只有61字壳；`meta_blog`恢复官方Blog首屏Latest News与首10 Posts，最新Jul27，停Next前 | Research独立论文目录未覆盖，不能由Blog替代全Research |
| SRC-QWEN | 旧GitHub博客首5最新Sep23 2025，不作2026覆盖；迁移`qwen_current`200仅4字壳。搜索发现具体ID `7a9090115ee193ce6a7f7195271d96dd93`标2026/10/18但标题空/0words；原域精确请求15秒timeout | 必须恢复该ID实际身份/正文/日期或隔离，搜索模板日期不能纳候选 |
| SRC-DEEPSEEK | `deepseek`主页只产品导航，恢复`deepseek_updates`官方ChangeLog最新Oct17（V4.1-Flash-1017与search API），下一Sep10 | Oct17非本窗，不扩读performance数字，不把临近发布移到Oct18 |
| SRC-MOONSHOT | `moonshot`旧Platform Blog首屏到2024/2025；`kimi_latest`GitHub新建降序首10，最新Kimi-K3 Jul27，不能以pushed_at替代release。`kimi_code_whatsnew`官方What'sNew首批Desktop1.1/CLI2.2为Oct14，下一Sep23 | 未完整覆盖所有repo release/模型研究，限定这3入口；初次`kimi_github`默认升序10项无当前覆盖效力 |
| SRC-TENCENT-HUNYUAN | 静态`hunyuan`仅空壳，实际浏览器Research?page=1“全部”首11，从Sep22到Feb3；Featured最新亦Sep22 | 浏览器实读，非由空HTML推零；快照摘录见下 |
| SRC-ZAI | `zai`Research“全部/时间排序”可见首15，最新Aug26、下一Aug14，末Dec9 2025，停查看更多前 | 仅首批有界目录，不查旧页 |
| SRC-BYTEDANCE-SEED | `seed`Newest→oldest第1页标示1–20/246、Page1/13，实际18个可读日期/题名，最新Sep28→Jun3/May26；`seed_blog`Blog featured5从Aug5向前及选列publications | 不把页码20当20项已审；论文按显式排序到窗前即停，不翻13页、不把science混入候选 |
| SRC-BAIDU-ERNIE | `ernie`官方Blog首10最新May9→Nov21 2025 | 本次可见首批，无Oct18；不扩旧页 |
| SRC-XIAOMI-MIMO | `mimo`Paper8项最新Jun29；Blog首15原未标日期，后经具名route和必要iframe共14项恢复为窗前日期/月份，1项材料科学明确范围外；精确日期表见末节 | 首稿其余13未打开是普通待办，已纠正并实际恢复；不再将它们误称外部受阻 |
| SRC-MINIMAX | `minimax`Research12项从Aug13到Oct27 2025；`minimax_tech`完整3文章Oct8/Sep22/Sep19 | 不把产品NEW字样当新发布日期 |
| SRC-ARXIV | `availability`官方完整公告表：Sunday～Thursday ET公告，无Friday/Saturday；新稿、替换、撤回、crosslist均随公告。Oct18 BJT周日无正常批次，Sunday ET公告为Oct19 BJT | 只关闭常规公告批次；不排除作者独立渠道首公开。不把提交日当公开日，不追时分秒 |

混元浏览器实际快照（2026-10-19 17:27 +08）：URL`https://hunyuan.tencent.com/research?page=1`，“research all tab list / 全部”；条目日期依次Sep22、Sep22、Aug28、Aug11、Jul21、Jul6、May21、Apr30、Apr23、Feb13、Feb3。前四标题分别Hy Image3.5 preview、Batch Size Scaling、Hy4 preview、From LR to ELR。后续试开另一MiMo浏览器tab报告subagent不支持IAB visibility，因此未无限重试；MiMo改用公共脚本route与原页。

## 首批准入/排除校准

准备好的本窗拟入选：0。不是把所有原始目录行当候选后统一关闭。

1. Anthropic “Designing more efficient quantum circuits with Claude”：官方目录Oct16，窗外；明确AI for Science应用亦在暂缓范围。无需为排除去精确时刻/全文。
2. Meta “How Meta's AI Models Are Powering the First Wave of Genesis Mission Projects”：官方Blog Jul21，窗外；不能仅凭基础模型/平台词绕过科学应用暂缓。
3. OpenAI Community Oct18活动帖：最后回复/活动日期不是研究公开日期；论坛/用户观点不证明机制，既非本窗确定研究材料亦不评分。
4. DeepSeek Oct17更新：有具体模型与搜索发布，不能因为本轮Oct19发现而重归Oct18；不纳本窗、不评分、不误称已做必要Source。
5. MiMo tool-call repetition修复：正文Sep27为具体旧事件，有机制潜力但窗外，本轮只核日期停止；不继承到本窗Books池。

root已消息返回实际首批校准通过，范围为OpenAI1299 XML、Anthropic首10、完整arXiv日程、Meta Blog有限段与代表排除；不是其他尚未核源的正面覆盖或日级验收。

## 待独立核验与剩余

- Qwen具体ID和当前动态研究入口，root已实际窄浏览器恢复：同ID无标题正文，只有导航页脚及2026/10/19、undefined分钟、0词；最新进展页只有Research框架无可读条目。与搜索Oct18字段不一致，不能证明研究存在/公开日期，按来源与具体身份终态隔离。本地JS仅作公共入口定位，没有明确公开研究API路由，不执行代码或无限猜测。
- 其余目录与终态外部子范围由root独立核查，作者不代签。
- 无Books拟写、无Books窄锁；0个确定本窗候选，只有上述具体身份/覆盖保留，不等于全网0发布。

## MiMo日期差额恢复（root指出后实际执行）

首稿仅打开2篇，其余13篇未开，不能直接外部终态化。现仅取标题和日期字段，不读正文/构造新贡献。`mimo_routes.raw.html`是主页实际引用的公共4752构建文件，含精确route；`mimo_js.raw.html`显式`t.u`为`static/js/async/`。最初错误拼成`static/js/`的404是本方路径错误，已按真实映射修正，9个chunk均200，不拿404证明源失效。`mimo_chunk_results.json`保存正确chunk元数据，9个iframe明示原始目标，`mimo_iframe_results.json`全部200。原件同名前缀落盘；全部命令已exit。

| 主页Blog位置/材料 | 实际日期原字段/处置 | 原件 |
| --- | --- | --- |
| 1 Tool-call Repetition | September 27, 2026，窗外 | `mimo_tool` |
| 2 Introducing MiMo-V2.6 | September 22nd, 2026，窗外 | `mimo_iframe_9431`，官方目标`/mimo-v2-6/article.html` |
| 3 Materials R&D | 标题/简介明确新材料研发和分子设计，AI for Science暂缓；按合同无需为排除另查日期 | `mimo`主页具名题摘 |
| 4 Long-Horizon Code | June 10, 2026，窗外 | `mimo_horizon` |
| 5 UltraSpeed 1000TPS | June 8, 2026，窗外 | `mimo_1000tps` |
| 6 Inference Optimization | May 30, 2026，窗外 | `mimo_inference` |
| 7 V2.5-ASR | April 2026，整月窗外，不补造日 | `mimo_iframe_954` |
| 8 V2.5-TTS | April 2026，整月窗外，不补造日 | `mimo_iframe_3887` |
| 9 V2.5-Pro | April 27th, 2026，窗外 | `mimo_iframe_8818` |
| 10 V2.5 | April 22nd, 2026，窗外 | `mimo_iframe_1840` |
| 11 V2-Pro | March 18th, 2026，窗外 | `mimo_iframe_5718` |
| 12 V2-Omni | March 18th, 2026，窗外 | `mimo_iframe_1354` |
| 13 V2-TTS | March 18th, 2026，窗外 | `mimo_iframe_4372` |
| 14 V2-Flash | December 16, 2025，窗外 | `mimo_iframe_9389` |
| 15 HSS assessment | 2025-12-19（构建frontmatter）；December 22, 2025（正文原字段），两者不相同且均窗外，不选其中一项改写另一项 | `mimo_routes`和`mimo_hss` |

当前MiMo可执行日期差额0，14窗前/1明确暂缓，仍不宣称主页首15之外全部历史发布已审。
