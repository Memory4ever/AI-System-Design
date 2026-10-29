# 2026-06-22 已有 Daily 补遗漏

## 1. 本日范围与旧层保护

- 唯一作者：`jun22_supp_author`；唯一非作者复核：`/root`，其实际检查写入 [SUP_REVIEW_20261029.md](./SUP_REVIEW_20261029.md)。不自签本轮独立复核，不写 State 或索引。
- 本次执行：2026-10-29，Asia/Shanghai；补充窗口仅 `2026-06-21 ～ 2026-06-21`，对应 UTC `2026-06-20T16:00:00Z ～ 2026-06-21T15:59:59Z`。用户授权仅补已有 Daily 遗漏，保留旧候选日期、分数、小时窗与有效证据；不扩其他日、Weekly、Live、2025 或缺失 Daily。
- 原报告 5084 bytes，SHA256 `c4b600095191bb6c3d2995976ecbdf80406daa62b94e0443b3994b9ab0d9df33`；本日限定 git status 起跑无差异。原窗 `2026-06-21T09:00:00+08:00 ～ 2026-06-22T09:00:00+08:00`；当前正式候选 0、原 §4 空。旧包 submission 口径 39 retained 已被旧 reconciliation 迁出，不能由旧 retained 标签重建本日候选；其原始材料仍保留。本轮不把旧 `created` 改名为 `registered`，也不将旧签名当本轮验收。
- 已完整重读当前 AGENTS、Research/Report 合同、Research Sources 使用说明/每日14源/arXiv主题、Research Prompt、ROADMAP；State 仅路由本日。仅复用 [06-07 来源记录](../daily-20260607/SUP_SOURCE_CHECK_20261025.md) 的合法接口形状/参数，不复用其其他日期查询结果。未读取其他日报候选池或 Weekly 反推本日。

## 2. 13 个机构每日源：实际入口与停止位置

以下均为本轮目标日复查。没有目标日事件不等于机构没有研究；完整历史目录无法恢复的部分在 §5 精确隔离。

| 来源 | 本轮实际读取、日期邻段与停止 | 本轮处置 |
| --- | --- | --- |
| SRC-OPENAI | 首查 [Research](https://openai.com/research/)，再读 [官方 RSS](https://openai.com/news/rss.xml) 单响应 1334 项，只选目标相邻日期。`New usage analytics and updated spend controls for enterprises / Thu, 18 Jun 2026 17:00:00 GMT` 后，下一事件 `Samsung Electronics brings ChatGPT and Codex to employees / Sun, 21 Jun 2026 23:00:00 GMT` 实为 BJT Jun22；`Codex-maxxing for long-running work / Mon, 22 Jun 2026 00:00:00 GMT` 也非 Jun21。 | 目标 BJT 日未发现新事件，未把 UTC Jun21 晚间搬入补窗；只作日期导航，不审窗外正文。 |
| SRC-ANTHROPIC | 首查 [Research](https://www.anthropic.com/research)，首批不足六月；实际恢复 [`listing/research/default/2`](https://www.anthropic.com/listing/research/default/2)，HTTP200，`posts=24`、`hasNextPage=true`，从 `2026-08-12` 到 `2026-04-30`；相邻 `2026-06-26 / economic-index-june-2026-report` → `2026-06-18 / project-fetch-phase-two`，跨过 Jun21，停止第2页。 | 未见本日条目；一次 TLS EOF 后同一请求成功，失败未授零。不继续更早第3页。 |
| SRC-GOOGLE-AI | 首查 [DeepMind Research](https://deepmind.google/research/)，沿 [News 第2页](https://deepmind.google/blog/page/2/) 六月卡片回原件。A24 原 `datePublished=2026-06-22T14:30:00+00:00`，AI agents security 显示 `June 18, 2026`；其间未见 Jun21。月份卡片亦核 `computer use / Jun24`、`Nano Banana/Omni Flash / Jun30`、`UK planning / Jun16`、`multi-agent safety funding / Jun11`、`DiffusionGemma / Jun10`、`Live Translate / Jun09`、`learning / Jun09`，不把 Jun20 的 modified 字段当新公开。Research [六月 Blog](https://research.google/blog/2026/06/) 单页12项，`Jun24 / Thinking to recall` → `Jun16 / Earth AI` 已跨窗。另实际打开 [2026 + language model Publications 查询](https://research.google/pubs/?category=2026&search=language%20model)，当前11个可见结果、无下一页 href，元数据只有年份，未取得目标日日级公开归属。 | Blog 范围完成；Publications 日级缺口隔离，不把11条年级导航变成逐项队列或当天论文数。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 当前无可读研究目录正文；[Blog](https://ai.meta.com/blog/) 可读条目日期邻段 `Jun29, 2026 / Brain2Qwerty` → `Apr08, 2026 / Muse Spark`；本轮定点补检 `site:ai.meta.com "June 21, 2026"` 无新原件线索。 | 仅覆盖可见 Blog 与该查询，历史研究目录日级缺段隔离；不以空 research 响应授零。 |
| SRC-QWEN | [旧 Blog](https://qwenlm.github.io/blog/) 明示迁往 qwen.ai；本轮重查官方公开 retrieval：`https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`、`language=zh-CN`，均HTTP200、`success=true`，各40项，data仅articles、无分页字段；按 `extra.date` 核 `Qwen-Robot* / Jun16` → `Qwen-AgentWorld / Jun23`，目标日无条目。 | 没有用旧2025页面或缺参数的空响应证明Jun21；目录日期不冒充全球首公开时刻。 |
| SRC-DEEPSEEK | 首查 [主页研究入口](https://www.deepseek.com/)，再读 [官方 Change Log](https://api-docs.deepseek.com/updates/)；实际原件有 `Date: 2026-07-31 / DeepSeek-V4-Flash Update` → `Date: 2026-04-24 / DeepSeek-V4`，跨过目标日。 | 此发布时序未见Jun21新模型/机制事件；浏览工具未带尾斜杠曾显示首页，已用实际 `/updates/` 原响应恢复，不据重定向首页授零。 |
| SRC-MOONSHOT | 首查 [Kimi Blog](https://platform.kimi.com/blog)，目前最新 `2025年11月07日`；本轮 [MoonshotAI 官方组织目录](https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated) HTTP200、42仓库、无June2026新建仓库。定点补检得到 [Kimi Code What's New](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)，可读 `Jun29 / v0.20.2` → `Jun17 / v0.17.0`、`Jun16`、`Jun12 / K2.7 Code`，无Jun21条目。 | release notes有限时序可恢复；没有用仓库 updated_at 证明公开日期。完整2026研究Blog缺段隔离。 |
| SRC-TENCENT-HUNYUAN | 首查 [Research](https://hunyuan.tencent.com/research)，恢复其官方 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":100,"renderType":0}`、`accept-language:zh`；原响应 `code=0,msg=success,totalNum=11,list.length=11`，一次读完无下一页；目标邻段 `id100064 / Hy3 / displayPublishTime=1783320600 (Jul06 BJT)` → `id100041 / Hy-MT2 / 1779346800 (May21 BJT)`。 | All中文结果无本日条目；不以默认英语较短列表或空CSR壳授零，不将显示日期改称全球首发。 |
| SRC-ZAI | 首查 [官方 Research](https://www.zhipuai.cn/zh/research)，时间排序当前首屏 `Aug14 / GLM-5.3` → `Jun16 / GLM-5.2` → `May20 / ZCube`，已跨目标；停止首屏。 | 未见Jun21条目，不点更早“查看更多”。 |
| SRC-BYTEDANCE-SEED | 首查 [Research](https://seed.bytedance.com/en/research) 与 [Publications](https://seed.bytedance.com/en/public_papers) 第1页，`1–20 of247 / Page1of13`；原相邻 `Jun30 / Seed2.0 card` → `Jun19 / chemical network`，后者仅日期导航且AI for Science暂缓，不进本日池。沿页面五个实际topic href：`/en/blog_list/foundation` 为Jun23→Jun19；visual为Jul08→Apr23；audio为Jul20→Apr09；ai-infra最新Aug14,2025；frontier-research为Jul07,2026→Dec02,2025。均在各topic首屏跨过目标，停止而不扩读旧文/下一页。 | 本日无新公开条目；Research精选不是全目录，已补其五个topic和论文目录，不用页面已有宽列表制造候选配额。 |
| SRC-BAIDU-ERNIE | [官方中文技术博客](https://ernie.baidu.com/blog/zh/) 首屏最新 `2026年5月9日 / 文心5.1`，早于目标。 | 当前可见发布目录无本日条目，停止第1页，不读更早第2页。 |
| SRC-XIAOMI-MIMO | 首查 [MiMo Paper/Blog](https://mimo.xiaomi.com/)，Paper相邻Jun29/MOPD→Mar13/ARL-Tangram；官方页面JS `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js` 本轮原日期为Jun10长程Agent→Jun08 TileRT→May30推理，另一新文Sep27，不是Jun21。对无日期模型卡回 [官方 Model Release](https://mimo.mi.com/docs/en-US/updates/model)，Sep22→Jun02 ASR→Apr23，已跨窗，停止。 | 没有把无日期Blog卡/CSR壳授零，没有遗留本日模型日期请求。 |
| SRC-MINIMAX | [英文Research](https://www.minimax.io/blog)、[中文博客](https://www.minimaxi.com/blog)（实际跳至minimax.cn/blog）本轮相邻Jul31→Jun09 MaxProof→Jun01 M3。另首查清单内 [Agent Tech Blog](https://agent.minimax.io/docs/techblog)，本轮可读日期从Oct27到Sep19；依其实际链接读 [llms.txt](https://agent.minimax.io/docs/llms.txt)，research及具名文章索引没有目标日日期或历史分页。 | 两种语言主Blog有限时序无Jun21；Agent历史日级目录缺段隔离，不用错误 `/agent-tech-blog` 故障或llms.txt列表证明完整历史。 |

## 3. arXiv：本日合法日期查询与有界主题补检

本轮实际读取 [arXiv availability](https://info.arxiv.org/help/availability.html)：Sunday through Thursday公告、Friday/Saturday无常规公告，且涵盖new、replacement、withdrawal、cross listing、journal reference；最终ID/DOI在公告时才分配。BJT Jun21周日覆盖EDT Jun20 12:00～Jun21 11:59:59，前一正常批次为BJT Jun19，下一为BJT Jun22（Jun21 20:00 EDT），因此本日没有常规批次。规则只是正常公告约束，不能独自证明没有作者早稿或异常事件。

随后本轮合法本日查询 `client-id=arxiv.content`、`query=registered:[2026-06-20T16:00:00Z TO 2026-06-21T15:59:59Z]`、`page[size]=1000`，HTTP200、`total=0,totalPages=0,page=1`、data空，原响应保留于 [本日原件](./SUP_DATACITE_REGISTERED_JUN21_20261029.json)。无下一页，不用无效的 `client.client-id` query字段。两个本轮正控制分别为：仅来源筛选、page[size]=1，total3227697，首项`10.48550/arxiv.2610.35866 / registered=2026-10-27T04:58:54Z / findable`；同来源且`registered:[2026-06-18T00:00:00Z TO 2026-06-23T23:59:59Z]`、page[size]=1，total5438，首项`10.48550/arxiv.2606.23238 / registered=2026-06-23T05:13:41Z / findable`。它们仅验证来源与日期筛选生效，非本日候选/论文数量；registered不改名为实际公开时刻。

有界补检逐项执行以下七主题，各为一条search query，第一页止；没有将关键词命中直接准入：

1. `site:arxiv.org "21 Jun 2026" ("language model" OR Transformer OR MoE)`（模型结构/容量）。
2. 同日期 `(LLM OR training OR inference)`（训练/推理系统）。
3. 同日期 `(multimodal OR "world model" OR VLA)`（多模态/生成/world/action）。
4. 同日期 `(Agent OR RAG OR memory)`（Agent/检索/记忆）。
5. 同日期 `(kernel OR GPU OR compiler)`（硬件/编译/执行）。
6. 同日期 `(evaluation OR alignment OR "reinforcement learning")`（评价/后训练）。
7. 同日期 `(attention OR representation OR optimization)`（表示/学习理论）。

相关新命名线索只有四篇需核其精确题摘/日期：ASAP `2606.22541`、Text2DSL `2606.22586`、Self-Evolving Cognitive Framework `2606.22449`、A Markov Chain Approach `2606.22652`。已互斥交root只做四篇abs/notice/registered与日界校准，不重复Methods。搜索另给M* `2606.12688`、CoRA `2606.14961`、ANEForge `2606.17090`，其检索显示Jun10/Jun12非目标，只留搜索噪声标记，不借其主题重开旧日。

本轮还打开官方`/list/<category>/2026-06`的CL/LG/DC/AI/CV/AR/IR月入口，各首屏1–50仅浏览相关标题并核合法链接；例如`BitsMoE`、`ViBE`、`SPARQLe`、`DLLM-JEPA`、`TCAR-Gen`均在月初ID邻段，不是Jun21日级公告。总量或首屏不是当日论文数，没有从月目录全量建逐项关闭队列；本日无日公告批次，月表不能补造日级list。未使用`/2606`的404、catchup90天、提交日或旧created推断授零。若具体早稿、异常公告、实质修订或撤回触发目标日，定点重开该家族。

## 4. 当前判断、独立校准与Books

本日新增确定候选0。root互斥完成四篇官方完整ABS/current notice、唯一v1与同精确DOI的registered，原字段和逐项判断见 [独立复核§2](./SUP_REVIEW_20261029.md#2-互斥四题摘与精确事件日界)。四v1均为Jun21 UTC提交，按适用公告表最早Jun23 BJT08:00；`arxiv.content/findable`的registered上界依次为Jun23 UTC04:57:47（22541）、04:58:46（22586）、04:55:46（22449）、05:00:14（22652），整个联合区间均同Jun23。此为arXiv公告归属，不声称全球first-public或历史逐字内容；created未作日证。Current可见无withdrawal/纠错note，会议接受说明本身不证明窗前全文。

- `22541 / ASAP`：DP Attention与EP MoE同步屏障、不均衡→stage拆分与异步调度有具体潜力；未做Methods，摘要90%收益未采用。只作为Jun23窗外恢复线索，不评分或进入本日Books。
- `22652 / MCHF`：pairwise utility直接定义输出转移kernel及非传递项与scalar reward/博弈目标的关系有具体潜力；理论假设尚未审阅。只作为Jun23窗外恢复线索，不把收敛宣传写成已验证定理。
- `22586 / Text2DSL`：完整题摘提供grammar/API/vocabulary prompt条件、领域pairs/AST与CodeBLEU对照；未见超出成熟spec-conditioned生成的机制、有效性反证或独立执行权限边界。题摘贡献前关闭，不把新task名和局部指标当长期增量；非因小模型或单一领域自动排除。
- `22449 / Self-Evolving Cognitive Framework`：题摘组合causal model/intervention/continual refinement，并建议epistemic benchmark，未给因果state更新的新机制或可核成立条件。贡献前关闭，不因理论/机器人标签排除；Science专用部分另属暂缓范围。

两条具体贡献前排除、两条窗外潜力，不是四条均入选，也不是四条均无价值；本日确定候选、评分、Methods与Books工作均为0。没有采用命题需要全Books定位，不为制造diff改书。上述共同日期方法已有具名联合证据检验，不把一次空响应当整批终态。

## 5. 本窗外部保留项与剩余工作

- Google Publications：本轮2026+language model实际目录只有年份、无first-public日；缺Jun21日级列表/具名事件，不支持零研究、Coverage/Evidence或Books。可接受替代为带日期官方目录、具名作者原件或可读目标日快照；有材料后只恢复该片段，不扫全年。
- Meta Research：当前目录正文不可读，可见Blog/目标日查询不等完整研究档案；缺Jun21历史日级目录。替代为官方目标日列表或具名本日正文，届时只重开该来源片段。
- Moonshot：当前Blog止于2025，组织目录和Kimi Code notes不是完整2026研究历史；缺Jun21研究Blog/论文列表。替代为官方目标日公告或具名作者稿，只恢复对应条目。
- MiniMax Agent：当前techblog与llms索引未提供Jun21历史目录；缺本日文章公开日期/历史列表。替代为有日期官方文章或目标日快照，只恢复该入口。本轮主Blog中英文时序有效，不推倒其他来源。

以上外部片段均不支持正面Coverage/Evidence/Books、全网无遗漏、性能或安全保证；与尚可继续执行的本日工作分开。四条精确日界与题摘校准已完成，root实际DAY已通过（独立记录§3），作者于2026-10-29T17:49:47+08:00按该结论行政同步完成态；随后实际全稿读回与QA、交root保存后FINAL，FINAL不由作者自签。两条Jun23窗外潜力不属于本窗、不阻塞本日，真实归属日恢复时再按当日上下文处理，作者不自行接日。
