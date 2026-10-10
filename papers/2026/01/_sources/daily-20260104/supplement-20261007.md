# 2026-01-04 增量来源补查

作者：root。执行日：2026-10-07。补充窗口：2026-01-03完整北京时间自然日。用户授权只补遗漏，原09:00窗口、既有候选日期/评分/有效审阅均不搬移。本日原候选为0；原来源检查可复用，但旧完成声明不代替本轮补查。重新读取AGENTS、统一Prompt与当前适用合同；只按每日来源和实际触发入口执行。

## 实际来源范围

原始响应保存于[本次目录](supplement-20261007/)，这些是来源元数据，不是跨日判断或全文审阅。日期以原始公开字段定位；没有日期的标题不会被当作本日新论文。

| 来源 | 实际入口与停止点 | 结果及边界 |
| --- | --- | --- |
| SRC-OPENAI | Research→news/rss.xml，当前1251 item的title/link/pubDate定位Jan03与Grove Jan02/Health Jan07邻接，止元数据切片；openai.raw | 本切片无Jan03，不读全年正文，不声称所有机构发布无遗漏 |
| SRC-ANTHROPIC | Research原HTML发布日期字段，Dec19 Bloom→Jan08官方研究跨窗；anthropic.raw | 无Jan03目录行；只采用publishedOn，不用插图createdAt |
| SRC-GOOGLE-AI | 实际重开DeepMind Publications page1，Jan09→Dec03桥接止page1；Google Research Jan2026月档9篇，最早Jan12，止月档末；pubs只有年级字段，raw请求超时后用web有限入口恢复 | 两个有限dated入口已检查；Google Research论文Jan03日级目录缺口隔离，不扩大全年论文队列 |
| SRC-META-AI | Research原入口curl TLS失败；web有限页/官方日期补检无可核Jan03切片，Publications?page=3仍不可访问 | 具体日期目录受阻，空提取不证明零发布；需要该源该日dated列表或具名发布 |
| SRC-QWEN | 官方api/page_config?code=research.research-list，60项按date全量定位，最大Dec23 2025，止完整有限配置；qwen.raw | 无Jan03行，不能按数组顺序停止；当前有限目录不证明隐去历史不存在 |
| SRC-DEEPSEEK | [官网研究与动态](https://www.deepseek.com/news/)web可读有限研究索引10项，Engram Jan12→mHC Dec31跨窗，动态首屏5项；原有效official-entry记录亦保留 | 无Jan03；deepseek.raw实际是重定向后的API Docs新闻页，不作为这10项研究日期原响应。不重审窗外mHC，不要求全机构无删除证明 |
| SRC-MOONSHOT | Platform Blog26个dated条目，最新Nov07 2025；本日有效KimiCLI release原字段0.70 Dec31→0.71/0.72 Jan04，止明确相邻版本；kimi.raw及原kimi-release-date.jsonl | 无Jan03事件；两Jan04 release仍是原报告窗外线索，不重新挪日期 |
| SRC-TENCENT-HUNYUAN | 官方POST api/blog/publicList，pageNum1/pageSize100/renderType0，code0/total9/list9，最早display/published Feb03；hunyuan.raw | 完整当前有限接口已检查；publicAt/published/display分开，不把created当公开 |
| SRC-ZAI | 官方Research SSR只定位可读日期字段；最邻近Jan07后台字段及Jan13研究条目，与Dec08/09/10旧条目分开；release有效片段Jan14→Dec22；zai.raw | 未定位Jan03；CMS日期不作为论文首公开，有限目录不是全机构覆盖 |
| SRC-BYTEDANCE-SEED | 官方get_article_list_v2，type1/2026 ASC/count20/page_token0总82，最早Jan20；本轮type2同参数返回9条，最早Feb12；2025有效切片最近paper Dec15/blog Dec24，止跨窗边界；seed.raw保存type1 | 无Jan03条目；type1分页has_more不等全年读完，复用只限原始字段身份未变化的相邻片段 |
| SRC-BAIDU-ERNIE | Blog/zh/page1十条dated，Jan08→Dec23跨窗，next2/2更旧，止page1；ernie.raw | 无Jan03；不把排行榜名称当机制贡献 |
| SRC-XIAOMI-MIMO | 官网8 Papers Jan08→Oct21跨窗；官方构建索引16个英文Blog route逐项定位frontmatter或显式iframe正文日期，止完整当前路由；见下方恢复记录 | 无Jan03日期条目；无日期的Model Description核心只有通用能力介绍，无拟采用机制，不索全机构隐藏历史证明 |
| SRC-MINIMAX | English Blog有限12卡片Jan27→Dec23；本轮中文HTML恢复13 dated卡片Jan28→Dec23；Agent原页面文本唯一dated May13；minimax.raw/minimax-cn.raw/minimax-agent.raw | 三个有限入口无Jan03，中文/Agent壳访问故障解除；不合并中英文日期，不声称全机构无遗漏 |
| SRC-ARXIV | 重开Availability L170–189；四个项目窄主题older-update API尝试Jan03完整BJT日，start0/max20均total0，止首响应；过滤被改写为互斥submittedDate，零响应不支持修订阴性；cs.CL月页请求404保留访问边界 | 常规Fri/Sat ET无公告（含new/replacements等）；提交/更新字段不能证明公开，不扩Submitted池或全分类 |

## 查询口径与停止

按Jan03完整BJT日尝试的API编码为`lastUpdatedDate:[202601021600 TO 202601031559] AND submittedDate:[199001010000 TO 202601021559] AND <theme>`；四组均start0/max_results20/sortBylastUpdatedDate/ascending，实际totalResults=0、entries=[]。后续独立确认API将lastUpdatedDate改写为submittedDate，形成互斥Submitted区间；0响应无效，不授旧稿修订阴性。官方公告日程依据另行有效，不由该无效查询证明。

- model：`((cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:MoE OR all:"foundation model"))`。
- system：`((cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:kernel OR all:"model inference" OR all:"distributed training"))`。
- multimodal：`((cat:cs.CV OR cat:cs.RO OR cat:cs.LG) AND (all:"foundation model" OR all:"world model" OR all:VLA OR all:multimodal OR all:"diffusion model"))`。
- agent：`((cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:LLM OR all:"language model") AND (all:agent OR all:RAG OR all:memory OR all:reasoning OR all:planning))`。

先前一次Jan03 UTC整日而非BJT整日的探索查询返回75/1/1/5索引线索，边界不合本日，**不用于补窗覆盖或准入**，也未生成候选/审阅队列。上述正确窄查询替代它。API返回当前版本可能跨月更新，只有官方公开事件日期可决定新材料落窗；不把submitted/updated总量称本日论文数。

[官方Availability](https://info.arxiv.org/help/availability.html)明确常规公开含new、replacement、withdrawal、cross-list及journal reference，通常Sun–Thu ET20，Fri/Sat不公告。Jan03 BJT是Fri ET→Sat ET；原本日[假期有效材料](supplemental-official.txt)保存原文Jan04 ET公告安排，即Jan05 BJT。此次holiday实时请求429，但精确原文与采用命题未变化，保留有效证据。无需为没有具体线索的非标准事件或作者全部镜像创建考古请求。

Seed type2本轮确切请求为<https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2026&count=20&page_token=0&order_desc=false>；实际返回9个ArticleMeta，PublishDate最小1770825600000（Feb12 BJT），未发送locale header。其余可读日期为Feb13、Feb14、Apr01、Apr09、Apr23、Jun23、Jul07、Jul08，全部窗外；这里只保存可判定日期切片，不声称返回9项等于全年total或题摘已审。

Google月档：<https://research.google/blog/2026/01/>，实际9 dated条目Jan28至Jan12，没有分页，止末项；这不覆盖pubs中的独立论文。Meta实际Pub page3访问失败，不把Jan02同一家族条目强行当Jan03发布。

## 增量结果与Books

新增确认候选0，新增候选必要证据审阅0，Books提案/写入0。Kimi两个版本仍Jan04线索；不搬既有归属。No Change只针对可判断的本日增量，不代表全网没有研究。原Report无正式候选，其有效负侧材料保留。

## 具体保留项及独立验收

1. Google Research论文Jan03日级目录：pubs只有year。替代材料为该日主线dated官方列表或具名原始论文发布，取得后只恢复日期定位与必要审阅，不读全年论文。
2. Meta Jan03原Research/Publication dated切片：当前原入口/目标页不可读。替代为可读官方历史列表或具体原始发布，不能用空响应判零。

MiMo日期恢复（root独立读取）：[官方构建索引](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js)688092字符（UTF-8为743278字节），16个英文route。frontmatter日期为code-long-horizon Jun10、tilert Jun08、inference May30、tool-call-repetition Sep27、flash-hss Dec19 2025、flash-safety Dec18 2025；显式iframe正文为v2.5-ASR/TTS April2026、v2.5-Pro Apr27、v2.5 Apr22、material-research Sep21、v2-flash Dec16 2025、v2-omni/pro/tts Mar18。唯一无日期的[Model Description](https://mimo.xiaomi.com/htmls/mimo_v2_flash_model_description.html)正文仅通用assistant能力介绍，不具本项目机制增量；日期不影响这一拒绝判断。未见Jan03事件，不把构建时间当公开时间，也不读这些窗外文章的完整研究。MiMo原保留项解除。

均为终态保留项，不支持正面证据、Books或无遗漏断言；定点重开条件即上述材料取得。作者的扫描/筛选已收尾，普通待办只有非作者独立复核与Report写回；这里不自授通过。

本日不扫描Weekly源、不借旧Weekly扩候选、不stage/commit/push。共享Books未改；原始日期表仅供恢复身份，不把旧09:00窗口检查当此次自然日补查。

## 本轮独立复核（audit_supp_jan04，非作者）

复核时间：2026-10-07T13:57:31+08:00。独立重读AGENTS、当前研究合同/Report合同、每日来源及主题边界、统一Prompt、ROADMAP与本日停点；检查补充窗口Jan03完整BJT日，保留原09:00窗口和全部旧日期/评分/有效审阅。14源记录与入口/停点均核对，不把有限目录变成全年题摘队列。

实际分层核对：OpenAI原RSS1251项及日期邻接；Anthropic publishedOn与插图字段分离；Qwen60条date全量定位；Hunyuan code0/total9/list9及display/published/public/created分离；Seed type1当前20条/total82与原2025邻接切片。独立重放Seed type2相同请求且不加locale，HTTP200/9条/total23/next20/has_more=true，最早Feb12BJT。另抽核Moonshot平台及两条原ReleaseAPI的日期身份、ERNIE跨窗页与下一页、MiniMax中英目录和Agent原dated文本；Z.ai只核日期元数据及既有release邻接，不把CMS字段当首公开。独立重开DeepMind Publications page1（Jan09→Dec03）、Google月档9条（Jan28→Jan12）、Meta目标Pub page3不可访问及DeepSeek官方研究索引10条（Jan12→Dec31）。Google/Meta外部材料没有被空响应判为零。

arXiv独立重开[Availability](https://info.arxiv.org/help/availability.html) L170–189：常规公告包含new/replacements/withdrawals/cross-list等，Fri/Sat ET不公告；原假期精确有效片段继续复用。四组尝试查询`lastUpdatedDate:[202601021600 TO 202601031559] AND submittedDate:[199001010000 TO 202601021559] AND <theme>`按上文原式重放，start0/max20/ascending，每组HTTP200/totalResults0/entries0。API只是辅助元数据，不证明首公开；废弃UTC探索查询未重开、未入候选，也未扩Submitted池。

MiMo新恢复证据逐项独核：同一官方构建索引为688092字符（UTF-8为743278字节），16个英文Blog route；6个frontmatter日期与作者记录一致；10个显式iframe均HTTP200，9个有明确窗外日/月（v2.5-ASR/TTS April2026、v2.5-Pro Apr27、v2.5 Apr22、material-research Sep21、v2-flash Dec16 2025、v2-omni/pro/tts Mar18）。唯一无日期Model Description完整核心只有通用assistant能力描述，未披露足以改变项目机制判断的增量；日期不影响排除。MiMo具体保留项解除，而非用构建时间补造公开时间。没有深入审这些窗外正文。

发现并修正：假期引用原先指不存在的source-date-boundary.txt，已回指本日有效supplemental-official.txt；deepseek.raw实际为API Docs重定向页，已明确不支持研究10项日期；README旧OpenAI1243与Seed19/14等计数、Meta旧入口停点已由作者更新或明确原有效复用。未发现可由本日证据支持的具体误收/漏收，未改候选日期或评分。

结论：通过本轮有限补查独立复核。新增确认候选0、新增候选证据审阅0、Books提案/写入0，Books无diff，No Change成立于可判断增量。仅Google Research Jan03论文日级目录及Meta Jan03日期切片两项具体外部保留继续隔离；恢复条件见上文。未检查全机构隐藏/删除历史、所有作者镜像、全年题摘、Weekly及其他日期，不宣称Coverage/Evidence全无缺口或全网零研究。README本轮状态、来源表、§5/§6与本记录一致，原日级复核仅保留旧权限，不代替本轮。
