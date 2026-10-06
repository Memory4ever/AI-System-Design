# Jan06 原始查询、停止与当前漏斗

检查为2026-10-02实际执行；本窗固定`[2026-01-05T01:00:00Z,2026-01-06T01:00:00Z)`。本日独立重读当前合同、Daily来源与ROADMAP；未使用旧Daily/Weekly候选、评分或摘要。以下是过程停点，不是最终候选清单。

## 原入口与停止

14源当前入口原响应在official-entry-0～4.txt；补充availability/holiday/目录在supplemental-official.txt；日期字段切片在official-date-slices.jsonl。顺序按Daily14，不扫描Weekly源。

- OpenAI research当前首屏后取官方RSS，1243个日期metadata仅定位邻接：Grove Jan2T10Z、Health Jan7T00Z，本窗无该RSS条目；不读全年正文。
- Anthropic research的174个publishedOn仅日期定位，Bloom Dec19T19:45Z→ConstitutionalClassifiers Jan8T00Z，本窗无目录条目；不扩大为整个机构零事件。
- DeepMind publications第1页30条、9页/265总metadata，可见Jan9→Dec3桥接；Google pubs 2026/2025是年目录，非first-public时序档案。
- Meta首屏无可提取正文；Qwen旧目录止2025Sep23、新qwen.ai/blog无可提取正文，官方域窄搜索0仅辅助限制，不能证明窗口零。
- DeepSeek官方news有限10个date-label，Jan12→Dec31桥接，动态viewall未恢复完整历史。
- Kimi Platform日期目录止2025Nov7；fresh GitHub release page1/per_page100最早v0.38 Oct24，本窗published_at命中0；fresh CHANGELOG Jan5/6 labels命中0。release日期不用created_at，不审无窗内变更的PR。
- Hunyuan research入口timeout；fresh official POST `/api/blog/publicList` body `{pageNum:1,pageSize:1000,renderType:0}` code0/total9/list9，逐条publicAt/publishedAt/displayPublishTime/updatedAt保留，最早published/display为2026Feb3，当前九条不恢复Jan06历史。
- ZAI Research15条date floor Dec9、viewmore；release Jan14→Dec22，未恢复完整Research历史。
- Seed US official API type1/type2 × 2026ASC/2025DESC，page_token0/count20，字段PublishDate保留；跳过pinned后仅非pinned邻接：2026paper最早Jan19、blogFeb11，2025paper最新Dec14、blogDec23，pagination各实际保留，不读全年摘要。
- ERNIE Blog第1页Jan8→Dec23；MiMo paper8条Jan8→Oct21桥接，但blog15条undated/More不能恢复历史。
- MiniMax EN12条Jan27→Dec23；CN重定向导航、AgentTech仅导航，精确限制保留。

机构补检4条官方域分组Jan5/6及模型/训练/推理/Agent术语，实际0返回见institution-search.txt。它不是所有机构或全网召回证明。

## arXiv 有界发现

原查询URL、执行时刻、total/returned与metadata在arxiv-discovery-metadata.jsonl。四主题incoming Submitted缓冲`[202512311900,202601021859]`，start0/max100、Submitted升序：model72/system3/multimodal33/agent48，156是含跨主题重叠的原始命中，不是候选数。分类仅作为主题范围；未把整个分类逐项关闭。四主题older-update为lastUpdated Jan5T01→Jan6T0059且Submitted≤Dec31T1859，start0/max20，全0；只说明该有限query结果，不能覆盖实际public revision/mirror。

官方catchup Jan05/cs.CL返回HTTP400；2026-01月目录首25缓存不可得，未据此扩大扫描全月。title backstop因此有缺口；已知当窗主题身份只定点取exact-v1完整题摘，六批69份及首批3份共72份实际题摘，不是156条全摘要、更不是默认72全文队列。原始宽标题中领域应用未逐项深审。

## 日期证据

原first-public-fields与date-fields-screened两文件保留Original Submitted、Updated、Available精度和registered。holiday原文只覆盖new submissions：Dec31ET14以后至Jan2ET14的普通首次公告延迟到Jan4ET20，即Jan5T01Z；availability规定ID首次announcement才分配、不可advance/backdate。仅在具体Submitted满足该缓冲、2601身份一致、registration/首次原源访问upper落本窗且无更早具体公开线索时，合取支持`Jan5T01Z～upper`区间；不是registered=public的时刻等号。

late009xx/02404/11580等Submitted也可能在缓冲，但upper在Jan6T03或更晚，不能硬归本窗。它们仅日期保留；不以Submitted/Updated反推公开。RIMRULE v2 Submitted Jan5T04:14:46Z但Updated Jan6T01:58Z，未核本窗public revision，不能把v1审阅充当v2。本日FlashInfer2025Oct21 official blog已有trace/apply闭环，Jan06只审论文新增测试对象与context生命周期。

## 准入与最终停点

完整题摘逐项判断具体长期增量，不按名字/技术标签；首批及后续root独立准入校准已分批完成。69份exact-v1-screening JSONL加first-core-abstracts的3代表，共72份定点完整v1题摘；156重叠metadata不等候选或默认深入队列。本日最终冻结55唯一家族，15实际整合、11具体已有覆盖、21仅报告/关闭、8中心争议终态隔离；详本日README §3/4逐项采用命题/精确原段与Books处置。没有原始命中或保留率配额。

15处真实正文为Ch12/21/49/77/69/72/27/28/66/17/24/51/78及NeoVerse→Ch24、HFed→Ch36；root必要原源→owner→actual POST通过（Ch24同章两家族不增加家族数）。11具体已有覆盖Revati/FwPKM/00641/OnlineDT/Journey/FromSight/Wild/MalOpt/Inline/RIM/Spatial，各有当前owner实际承载论点。8中心FlexSpec/RWR/CSS/CDGS/RMAAT/Geometry/TGE/Avatar原材料可读，仅受影响保证隔离，不称整篇错误或代码复现失败；精确重开请求见README §5。

原始负侧不正式评分：00081医学应用、00097类比essay、00504 MotionPhysics科学应用、00598 RGBIR域感知recipe、00352 OmniVaT classifier adapter、00142 Sphere受限syllogistic solver均已root实际题摘或必要core校准；context-reward-evidence-07中九项具体负侧保留原v1题摘/理由，其中00202/00245/00444/00553四项完整AB实际抽核关闭通过，未将九项全量称独立验证。Sphere/Omni改判基于具体贡献事实，非因无artifact、深审费时或Books主题已有。00282只是修复本日已读AB停点遗漏，日期raw原有，无新主题/窗口扫描。

负侧抽检定点重开已收束：root实际完整AB核00129，纠正仅称photonic综述不足的旧理由，实际§2.1–2.3/3.1–3.3/4及Refs1–9核后认可本次综合未披露新可采用机制或对照边界，修正的贡献前关闭通过；过程保留photonic-admission-reopen.md，不扩全部引用或改变原55家族。root实际分层样本合计11项（既有六项、九项负侧中的四项、00129必要core），未称全metadata/全附件或全互联网。原55家族必要审阅及Books待办0，root14source有限切片/停止、最终清单及六部分日级Gate通过，README完成。八机构历史入口/title backstop/public revision-mirror限制仍精确隔离，不支持正面Coverage/Evidence、Books或无遗漏保证；恢复只重开受影响source/date/family。
