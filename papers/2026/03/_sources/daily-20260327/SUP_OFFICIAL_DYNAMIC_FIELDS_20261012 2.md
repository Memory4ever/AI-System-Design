# 03-27 本轮官方动态目录原字段

本轮实际访问2026-10-12，窗口只BJT03-26自然日。元数据不替firstpublic正文语义；不读窗外core。

## Hunyuan

POST https://api.hunyuan.tencent.com/api/blog/publicList ，JSON pageNum1/pageSize20/renderType0，Content-Type application/json，Origin https://hunyuan.tencent.com；本轮totalNum9/list9（不沿旧11）。完整ID/title/displayPublishTime读到尾；Feb3/Feb13→Apr23→Apr30后均窗外，当前researchdisplay无March。publishedAt/publicAt也非display，可变更新不当首公开互替。

| ID | title | displayPublishTime |
| --- | --- | --- |
| 100116 | When Do Larger Batches Help Scale LLM Reinforcement Learning? | 1790006400 |
| 100100 | Introducing Hy4 preview | 1787846400 |
| 100091 | From LR to ELR: A Better Heuristic for Pretraining Dynamics | 1785945600 |
| 100087 | Hyra: A simple yet effective scaffold for general discovery | 1784599200 |
| 100064 | Introducing Hy3 | 1783440000 |
| 100039 | Real life is where context gets hard | 1777532400 |
| 100061 | Hy3 preview: The First Step in Rebuilding the Hy model | 1776873600 |
| 100015 | Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping | 1770971763 |
| 100025 | Learning from context is harder than we thought | 1770090898 |

## Seed

当前页面main.40eba974.js实际路由/api/get_article_list_v2，methodGET/params包括article_type/page_token/count/order_desc/publish_year等；按源真实接口而不是猜空data。GET https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=100&order_desc=false ，LocaleUS，本轮sub_article_list14/total82/next40/has_moretrue。实际邻接到Mar26，停止仅本日相关段，不扫82库存。

本页14meta顺序：CUDAAgent/SteerableCodingDataFeb27，GeometricAha/ReferenceGuidedRLMar1，QuantumwavefunctionMar12，TensorNetworkStatesMar15，MixtureDepthAttentionMar16，MixedDimKVMar21，ProteinLigandMar23，SIMART/UniGRPOMar24，TopoMeshMar25；最后两项Mar26如下。科学题只范围层暂停，不通过Data/Eval引入。

- ID1335：Towards Generalizable Robotic Data Flywheel: High-Dimensional Factorization and Composition；PublishDate1774454400000，转换BJT2026-03-26 00:00（day-normalized原值），ExternalLinks arxiv.org/pdf/2603.25583。
- ID1336：Hessian-informed machine learning interatomic potential towards bridging theory and experiments；相同PublishDate，链接arxiv.org/pdf/2603.25373；标题明确科学暂停。

article_type2/token0/count100/publish_year2026/order_descfalse：9meta/total23/next20/has_moretrue，dated邻接Feb12–14→Apr1/9/23后。token20一次：3meta/total23/next空/has_morefalse，Jul20/31/Aug5。英文可见12与total23差11，不能以12假全历史；需要缺失语言/历史datedsegment，已有限到hasmorefalse不长loop。PaperPublishDate只是官方目录字段，不以UpdateTime或当前PDF可读证明当时版本可读。

本轮其它官源具体有限停止已并入SUP_OFFICIAL_SOURCE_STOP_20261012与正式Report§2；本文件只保动态原字段，不自授14源或整日完成。

## Flywheel25583补充自然日必要日期门

本轮再次只取原同页ID1335元字段：ArticleID1776666117326、ArticleType1/Status2、PublishDate1774454400000、ContentType0、JournalarXiv、ExternalLinks仅https://arxiv.org/pdf/2603.25583、UpdateTime1776909857000、StatusEn/Zh2。无机构正文release地址或first-public语义字段。该目录日期可支持其页面给出的Mar26日期，不能单独证明exact-v1正文在机构侧已先于arXiv公告公开；ArticleID/UpdateTime也非首次公开。原29的arXiv首公开下界27不排除另一个26先发事件，但本轮可见元字段不足以把二者等同。

新必要一次请求：Flywheel25583若以机构26先发补本日，需要官方说明该目录PublishDate对应可读原正文公开日、当日institution release/原通知或可核原链接缓存；不请求精确时分秒。当前与旧29同family只定点去重，保本日日期限制，不评分或深入Source/Books；其他已ready证据继续。科学Hessian无须为排除追日期。
