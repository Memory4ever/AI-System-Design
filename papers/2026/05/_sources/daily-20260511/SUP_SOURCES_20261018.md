# 2026-05-11 Daily — 遗漏补充来源记录

## A1. 本次边界与实际停点

- 作者：`/root/may11_supp_author`；独立复核：`/root/may11_supp_reader`，另写 `SUP_REVIEW_20261018.md`。
- 2026-10-18 恢复本日，保留原小时窗口、101 条候选整行/日期/评分、原连续 §4 与有效审阅；新增仅检查北京时间 **2026-05-10 完整自然日**。本次不用旧 826 身份池反推新增范围，不迁旧候选。
- 范围：14 个每日源及 09233 线索实际触发的 CVF 单篇，不扫 Weekly、Live 或其他日期；不改 Books、LEARNING_STATE、索引，不 stage/commit/push。
- `baseline-before-supplement-20261018.md` 从实际 HEAD 完整保存，203869 bytes，逐字节复核等于运行前 README；初次添加多一个 EOF 空行已用补丁行政修正，不改原文。
- 当前结果：新增确定候选 0；五个完整题摘身份中四个 arXiv 事件在补窗外，一个 Seed 目录/首次正文资格未定；无新增评分、必要深审采用结论或 Books 改动。不是五项贡献排除，也不是全源零命中/无遗漏。

## A2. 入口、执行与实际停止范围

执行自 2026-10-18 18:32 +08:00 起（检查时间，不是材料发布时间；最终保存时间以日报字段为准）。HTTP 失败、空壳、被忽略的分页与日期查询均保原件，不把 200 当作有效历史覆盖。

首查真实响应为同目录 `SUP_<简称>_20261018.headers.raw` / `SUP_<简称>_20261018.raw.html`。额外恢复为 `.raw`；无正文返回时只有 headers/失败输出，不捏造 raw。DEEPMIND 返回 gzip 原始字节，解码后阅读；其余正文按实际可解码内容检查。Google 两次 45s 连接超时、Meta 连接重置、OpenAI 403 均未授覆盖。

| ID | 实际入口与停止 | 本次判断及限制 |
| --- | --- | --- |
| SRC-OPENAI | `https://openai.com/research/`；curl403；网页读取同页只为研究概览和精选卡，另有限搜索 `site:openai.com 2026 "May 10"` | 未恢复 May10 日级研究索引，不以社区贴/首页精选授零命中；历史切片外部保留。 |
| SRC-ANTHROPIC | `https://www.anthropic.com/research` 当前首10条止Oct8；限定 May10 搜索及官方 alignment/interpretability 结果可见May8 Teaching Claude why、May7 NLAE | 未见确定May10事件，但没有完整历史分页；仅有限检查，不继承旧相邻日期为全站证明。 |
| SRC-GOOGLE-AI | DeepMind research 页面当前精选，May2026 science卡不扩读；Google pubs curl两次超时，网页恢复为年度/主题过滤入口，未有May10日级停止位 | 大模型/训练/推理/多模态有限补检，无日级覆盖断言；科学应用暂缓，不扩池。 |
| SRC-META-AI | `https://ai.meta.com/research/` 连接重置；`site:ai.meta.com/research/ "May 10" "2026"` 有限搜索无结果 | 原始历史目录未恢复；搜索空不是全源零，外部保留。 |
| SRC-QWEN | 旧站明确跳转 `https://qwen.ai/research`；当前入口200仅壳；定点读当前路由及research组件，实际依赖4467.js为404；已知 `/api/config` 仅app下载配置，不是研究列表 | 不把旧站2025列表或当前壳授May10零命中；当前历史研究列表未恢复。浏览器恢复返回子任务visibility不支持，不绕过限制。 |
| SRC-DEEPSEEK | 首页研究模型入口，无按日研究历史；限定 `site:deepseek.com "May 10" "2026"` 与Moonshot/Qwen组搜索 | 当前产品入口不证明历史完整性；未见确定本窗新事件，保日级切片限制。 |
| SRC-MOONSHOT | Kimi Platform Blog 实际列表最新为2025-11-07，止2024-05；限定Moonshot官方May10搜索无结果 | 该旧列表不能覆盖2026，不据此零命中；当前历史切片保留。 |
| SRC-TENCENT-HUNYUAN | 首查SPA壳后，实际IAB读取 `/research?page=1` 的“全部”11条：Sep22两项、Aug28、Aug11、Jul21、Jul6、May21、Apr30、Apr23、Feb13、Feb3 | 真实可见相邻May21 Hy-MT2 / Apr30 Real life is where context gets hard；本页无May10条目。仅该有限官方目录切片，不证明所有仓库/渠道无事件。 |
| SRC-ZAI | 官方 `/zh/research` 可读日期列表，首15条；相邻May20 ZCube / Apr29 Scaling Pain | 本页未见May10，未扩读窗外条目；“查看更多”旧页不作全站无遗漏证明。 |
| SRC-BYTEDANCE-SEED | 首查`/en/public_papers`显示1–20/246及第1/13页（UI槽位不作实际条数）；`?page=2`仍同第一页，明确不是翻页。读取首查列出的main JS确定API参数，再取type1论文US locale/page_token0、20；20页止Apr15（BJT），且非pinned按日期递减，已越过May10，后续token40不扩为全文队列。type2 Blog US locale/token0实际15条，has_more=false/total20；非US响应12条、total24，仅作locale控制；token20空响应不反推全体无文章 | 论文API实际18+20=38个目录元数据，唯一May10条为1667；只为该条读完整题摘与链接。Blog相邻June19/Apr23（BJT），无May10；目录PublishDate非arXiv公告或历史正文证明。下节隔离1667。 |
| SRC-BAIDU-ERNIE | `/blog/zh/` 首页10条，止2025-11-21；最新May9 ERNIE5.1正式发布，下一Apr30 | 该有限日期列表无May10，May9早于补窗，不重审/迁移旧release。未读取其性能宣传为本次结论。 |
| SRC-XIAOMI-MIMO | 首页Paper8条：June29 MOPD / March13 ARL-Tangram相邻；Blog15条无日期及More入口 | 论文列表未见May10；Blog历史日期切片仍未恢复，不从无日期推零，也不对15篇无差别全文。 |
| SRC-MINIMAX | `/blog` 当前12个带日期卡，May26 / March18相邻 | 有限研究列表未见May10，不扩展为全部中文/Agent渠道无遗漏。 |
| SRC-ARXIV | 四个分类主题查询各start0/max8，按submittedDate降序；另四个具名搜索线索完整题摘/精确历史；官方公告规则、registered-window元数据辅助控制 | 本窗May10 BJT没有常规公告batch，但不由此断言所有原始事件为0。查询与停止见A3；历史分类列表请求404，日级归档缺段保留。 |

Hunyuan UI 观测来自真实返回的可访问性页面，不来自下载壳推断；实际页内11个标题只作日期浏览，未变成正文队列。Seed `ArticleID`/`UpdateTime` 为更晚字段，均不替代首次公开日。

## A3. 有界 arXiv 发现、日期依据与查询修正

官方 [availability](https://info.arxiv.org/help/availability.html) 已保存 `SUP_ARXIV_RULES_20261018.raw`，实际说明新稿、replacement、withdrawal等随公告过程发布，Fri14:00～Mon14:00 Eastern接收的稿件最早Mon20:00公告。May10为周日，纽约处EDT；下列Sun May10提交的具名稿件最早是May11 20:00 EDT，即 **May12 BJT**，审核/延期只会更晚。规则不证明全球没有其他早正文。2025固定文档raw及github/raw两个请求均失败，未谎称已本次读取；本次现行官方2026节日/日程足以约束本年窗口。

DataCite实际请求：`https://api.datacite.org/dois`，query=`client.client-id:arxiv.content AND registered:[2026-05-09T16:00:00Z TO 2026-05-10T15:59:59Z]`，page[size]=100。`SUP_DATACITE_20261018.raw.json`实际total0，只作该登记窗查询结果，不证明所有arXiv公告/既有DOI修订为0。没有用created代registered或Submitted代公告；本次无拟入选arXiv项需要组合最晚界。

主题请求保存为 `SUP_THEME_MODEL/MULTIMODAL/SYSTEMS/AGENT_20261018.raw` 及headers。共同窗口查询字段为 `submittedDate:[202605080000 TO 202605102359]`，start0/max_results8/sortBy=submittedDate/descending。它是相邻接收期的有界发现，**不是本窗公开论文列表**。实际query自描述与返回published已核：

| 主题/分类 | 查询同义表达 | 实际停止 |
| --- | --- | --- |
| MODEL cs.CL/cs.LG | title language model / Transformer / MoE / optimization | 首8元数据，API总169；首09820、末09751，均May10提交。 |
| MULTIMODAL cs.CV/cs.RO | title diffusion / world model / VLA / multimodal | 首8元数据，总62；首09701、末09613，均May10提交。 |
| SYSTEMS cs.DC/cs.AR/cs.PL/cs.OS/cs.PF | GPU / language model / inference / kernel | 首8元数据，总49；首09735、末09375，均May10提交，2607.20432延迟ID也保原字段，不授May10公告。 |
| AGENT cs.AI/cs.IR/cs.MA | title agent / RAG / memory / tool calling | 首8元数据，总148；首09823、末11027，均May10提交。 |

上述仅32条元数据切片，不把总数相加成候选或逐项题摘队列，也不把当前v2/v3当作本日重要修订。May10接收事件最早公告界已在补窗后；停止首8并保检索限制，不继续分页成宽池。历史分类浏览请求`https://arxiv.org/list/cs.CL/2605?skip=0&show=25`实际404（`SUP_ARXIV_LIST`），不称已浏览日级列表。

第一次宽主题URL请求的手工转义末界错误，响应query实际为`2605102359`并返回Oct材料（`SUP_ARXIV_THEME`）。此响应明确无效、未采用、不扩池，不归因为已证服务端问题。随后用`curl -G --data-urlencode`修正，`SUP_ARXIV_THEME_ENCODED`为1044条宽主题结果的首30，仅核范围；发现入口过宽后改为上面四个分类/主题请求，不把1044/30变成关闭分母。

辅助web查询实际分三组：
1. OpenAI/Anthropic/DeepMind各`2026 "May 10"`；以及`"2026-05-10" (LLM OR language model OR diffusion OR agent)`，仅返回搜索引擎可见结果；日报、digest、论坛帖子只作线索，不作为技术/日期正面证据。
2. `site:arxiv.org "2026" "May 10" (large language OR transformer OR diffusion OR world model OR accelerator)`；Qwen旧/新域、Seed域限定日查询；得到下节四个具名arXiv线索，回官方原件。
3. Meta、Qwen/DeepSeek/Moonshot、Seed/MiMo/MiniMax与arXiv系统多模态主题的May10限定补检；无新增确定原始事件。搜索不承诺全召回，未无限改写查询。

## A4. 首批题摘准入校准与最终处置

以下五个家族的完整题摘实际已读，准入链是潜在贡献，不是证据审阅结论；独核校准见同日reader记录。四篇最早公告界足以排除此arXiv事件落补窗，不要求无意义地逐篇再取DataCite。

| 身份/实际原件 | 原约束 → 原文增量 → 若成立改变何种选择 | 本次处置 |
| --- | --- | --- |
| 2605.09321 OpenIIR；`SUP_ARXIV_09321_V1` exact-v1，current `SUP_ARXIV_09321` | 多Agent IR研究易把场景脚本和runtime混合 → shared core、typed scenario接口及可复放结构输出 → 可检验场景替换与实验控制边界，窄P；仍可能只是领域仿真组合，留真实归属日核。 | v1 Sun10May04:46:58UTC，最早May12BJT，arXiv事件窗外；不评分/深审。currentv2 May14仅版本信号，不冒重要修订；未见撤回/纠错标记。 |
| 2605.09586 DeformMaster；`SUP_ARXIV_09586_V1`、current `SUP_ARXIV_09586`，项目`SUP_DEFORM_PROJECT` | 变形物体视觉模型容易只有外观而缺交互动力学 → structured physics rollout＋neural residual、compliant hand actuator及constitutive experts → 值得核验物理先验与学习残差何时可迁移的新动作边界，P。 | v1 Sun10May14:55:54UTC，arXiv事件最早May12；项目当前有完整介绍但无可见发布日期，不证明May10早稿，不采用。currentv2 May20仅信号；无具名早稿线索不无限追全站历史。 |
| 2605.09678 Absurd World；`SUP_ARXIV_09678` v1 | 复杂度增长和现实知识记忆可能混淆推理测量 → 保逻辑结构而改变现实符号/行动/事件 → 可检验在简单推理下现实先验是否破坏逻辑不变性，P。 | v1 Sun10May17:55:38UTC，最早May12BJT；不因简单benchmark贡献C，不评分/深审。 |
| 2605.09693 Do multimodal models imagine electric sheep?；`SUP_ARXIV_09693` v1 | action预测与中间视觉状态是否共享表示未明 → action-only监督出现可解码中间状态、少量visual tokens改善所测任务 → 值得核验latent world state与显式视觉CoT的条件，P。 | v1 Sun10May18:25:52UTC，最早May12BJT；不因小任务排除，不评分/深审。 |
| Seed1667 / 2605.09233 Towards Robust Sequential Decomposition for Complex Image Editing；`SUP_SEED_PUBLICATIONS_20`、`SUP_SEED1667`、`SUP_ARXIV_09233_V1` | single-pass复杂指令解析失误，sequential又累计误差 → 统一in-context比较、复杂度可控合成分解监督及训练范式 → 重新考虑何时分解/如何限制历史误差，P。 | **首次正文日期资格未定**；Seed详情明确2026-05-10但只有ABSTRACT，Download PDF唯一指向arXiv；v1 Sun10May00:23:05UTC最早May12BJT。不是贡献关闭，不是已核May10论文，不评分/不入候选表/Books。 |

09233的定点必要旁路：打开exact-v1 HTML `SUP_09233_CORE`只核身份、页头日期含义及早稿外链；页头May10仍是提交字段，没有作者项目/代码正文链接。随后精确标题查询触发[CVF单篇](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Towards_Robust_Sequential_Decomposition_for_Complex_Image_Editing_CVPR_2026_paper.html)，原件`SUP_09233_CVF`为June2026 proceedings、无May10首次正文证据。第三方笔记May8字段不具原始发布权限，不采用；未以访问当前全文冒充历史内容已核或完整Source审阅。reader已独立实读上述日期/身份原件并接纳保留，无需再无差别附录/代码请求。

## A5. 有限终态保留与恢复条件

1. **09233/Seed1667**：需要可复查的May10作者/机构完整正文与当时公开日期，或证明更早首次正文的原件；现有目录/摘要日期与arXiv公告不能替代。获得后仅重开本身份的归属资格，再做必要证据、唯一owner/PRE/真实POST；当前不支持May10正面证据、Books或无遗漏。
2. OpenAI/Anthropic/Google/Meta/Qwen/DeepSeek/Moonshot/MiMo等明确缺历史切片；Hunyuan/ZAI/ERNIE/MiniMax/Seed也只是上表列出的目录/语言范围。取得May10官方日级归档或具体漏项后仅重开受影响槽位；不把其余有效旧101层一并重跑。
3. arXiv日级分类历史列表未恢复，有限主题检索不是官方日公告全量恢复；规则和空registered查询不排除独立原始事件。具名早正文、纠错/撤回、重要修订或官方日归档出现时定点恢复；不无限寻找不存在的周末常规batch。
4. 09321/09586/09678/09693 arXiv新稿事件确定不属May10；这里只保存窗外线索，不搬迁旧报告、不在本日执行后日审阅。09586无日期项目不作为May10早稿正面证据。

普通扫描/筛选/必要日期旁路及Books工作已处理；独立六节DAY通过，当前保存完成态已由独立reader R7 FINAL实际通过，不把这项验收称外部保留。无新增Books写入，不申请Books窄写。

## A6. 作者保存与限定检查

19:05:17 +08:00 保存稿：baseline与运行前HEAD逐字节同（203869B）；101旧候选整行/日期/评分完全同；旧§4连续110103字符完全同；216个本地引用0缺失；V3通过；本日README/source目录限定cached与unstaged diff-check通过。新SUP/raw为未跟踪文件，git diff不替代其内容审阅；无全仓clean声明。

首轮V3实际暴露来源重复表、缺冻结候选档案字段以及必查来源误用“检索受限”；已定位为报告表达错误，当前只保一张16行来源表，旧来源有效记录保在完整baseline，并把必要历史缺段写为“受阻”。未改校验器/测试，未调旧日期评分；修后实际V3已通过。Seed Blog actual15/total20与非US12/total24已经按真实数组长度更正，不把total当已读数。

独立reader R5已核本次实际来源范围与五题摘处置，后续完整六节DAY亦已实际通过。按reader要求，只在旧§4连续原块之后补当前范围说明；保存完成态已由独立reader R7 FINAL实际通过。旧101证据层复用，不把格式检查当新Source或语义验收。
