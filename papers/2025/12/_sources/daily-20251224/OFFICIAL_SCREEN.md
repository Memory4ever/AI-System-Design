# 2025-12-24 官方来源：有限发现与准入

作者：root。检查于2026-10-02约20:32～20:40北京时间。本窗 `[2025-12-23T09:00:00+08:00,2025-12-24T09:00:00+08:00)`，等价UTC `[12/23 01:00,12/24 01:00)`。此记录不授日级完成；arXiv由本日独立sidecar补齐，不继承相邻Daily的候选、评分或验收。

已独立重读AGENTS、研究合同、每日来源/arXiv主题边界、Report V3、Prompt、ROADMAP及12月停点。周级来源不扫描；HF卡和代码仅由具名官方发布触发定点恢复。

## 原始入口与停点

| 来源 | 实际读取与停止位置 | 结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)显示2026；另直接HTTP200取得[官方RSS](https://openai.com/news/rss.xml)，756710字符、1243个item，XML解析Dec22～24字段 | 本次RSS该段只有Dec22 Atlas hardening与客户故事，原`pubDate=Mon, 22 Dec 2025 00:00:00 GMT`。没有本窗RSS事件，不等于全部Research无事件；历史index切片仍未恢复。辅助泛搜索命中community用户帖，不作为官方研究证据 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)当前十项均2026；[Alignment](https://alignment.anthropic.com/)原始December六项至November，具体邻接Bloom/Oracles Dec19→mitigations16→replication12→mask8 | Alignment的December切片可复用同身份原始日期；不以它替代主Research历史分页。后者仍隔离。没有将原页月份解释为本窗新事件 |
| SRC-GOOGLE-AI | [DeepMind blog page4](https://deepmind.google/blog/page/4/)24项至November；本窗附近年度回顾Dec23、Scope2 Dec19。[Research blog2025](https://research.google/blog/2025/)第一页12项，Dec18/15/12/10/4/3到Nov12，1/9页；[publications](https://research.google/pubs/)当前年筛选仅2025计数676、year排序，`?year=2025`请求失败 | Blog邻接已读；年度回顾核心下节贡献前关闭。publications缺日级历史公开字段，不遍历676项补造每日事件，保留该部分缺口 |
| SRC-META-AI | [publications page3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3)实际2026-Feb至Jan2，随后2025-Dec26 safety games→Dec18四watermark→Dec16 SAM，混入2020等置顶 | 达本窗附近，不能称全局严格排序或全站零；未把Dec26未知时区移到本窗。此前同入口page4更早段的原始范围仅定点复用，不继承相邻报告完成 |
| SRC-QWEN | [Blog](https://qwen.ai/blog)提取空；已发现2511事件定点读[官方HF README](https://huggingface.co/Qwen/Qwen-Image-Edit-2511/raw/main/README.md)全125行，Introduction/Showcase/LoRA段 | 产品事实贡献前关闭，理由下节。动态历史目录仍缺；此前迁移组件的有限恢复停点身份未变，不重复猜测API或扩扫全部chunks |
| SRC-DEEPSEEK | [updates](https://api-docs.deepseek.com/updates/)原始2026-04-24→2025-12-01→Sep29邻接，当前早段未作为2025事件 | 已检查可见更新段；不证明全部研究目录完整 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)可見26条，Nov7/6至2024；定点CLI release0.67网页失败，既有原始changelog邻接0.69 Dec29/0.68 Dec24/0.67 Dec22仅用作路由 | 本窗没有确认新机制事件；CLI0.68原始API发布12/24 12:40Z在右端之后，属25窗口，不认领24。未用commit代first-public；没有扩大为全org提交队列 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)动态空；公开POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body `pageNum=1,pageSize=1000,renderType=0`，HTTP200/code0/totalNum9/list9 | 本次为英文条目，最早`displayPublishTime=1770090898`（2026-Feb3），不是相邻记录另一次语言环境11项。2025必要目录不可恢复，隔离；不将当前9条当2025零证明 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)HTTP200原始HTML1097209字符，历史邻接`createAt=2026-01-13T16:00Z`与GLM-TTS `2025-12-10T16:00Z`/ASR Dec9；另读[release](https://docs.z.ai/release-notes/new-released)Jan14→Dec22 GLM4.7→Dec11 | 两种目录分别检查，GLM4.7日字段不能证明12/23之后的重要新事件，也不称它此前已审。可见邻接检查不是全部渠道保证 |
| SRC-BYTEDANCE-SEED | [论文页](https://seed.bytedance.com/en/public_papers)HTTP200；公开GET `/api/get_article_list_v2?article_type={1,2}&publish_year=2025&count=20&page_token=0&order_desc=true`，header `x-tt-locale=US`，两类均HTTP200 | type1实际18/total94/next20，首两项pinned Dec15/2后Oct22至Jun26；type2实际18/total45/next20，pinned Prover Dec24、Seed1.8 Dec18、Seedance Dec16、GRRL Dec2、DA3 Nov27，之后Oct23至Jun25。已低于目标普通日期段停止；pinned/next及后续更新限制不授全局无遗漏。Prover日编码相交必要核心另读并隔离 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)第一页Jan8→Dec23排名→Dec9→Nov21，下一页2/2；另原始[百度新闻](https://cloud.baidu.com/news/news_f571211f-6b51-4cbc-b5ca-57cce8f66337)正文 | 榜单公告贡献前关闭，不采用数字作设计证据；到达低于窗口邻接停止，不扩大后续旧页或新旧模型宣传 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)Paper8项，Jan8 V2Flash→Oct21 router；Blog15项但无日期，More存在 | Paper可见邻接已读；Blog不能证明历史窗口。此前同V2Flash/组件有限恢复停点复用，仅该部分隔离，不称8/15即全站 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)12项、[中文](https://www.minimax.cn/blog)13项，Jan27/28→Dec23 M2.1→Oct27；M2.1 Blog核心/JSON-LD与Feynman实际取得的初始官方卡20380字符、Benchmarks/Evaluation Methodology Notes | Blog训练/能力主张仍关闭，固定卡新增评价协议potential见末注；午夜编码、卡commit/仓库创建不授first-public。此前Agent techblog.md仅May2026有限段不授2025完整性 |

GET/POST均为公开只读查询，没有运行模型、测试部署或修改外部服务。网络全文输出中有一次Seed payload截断，随后重新请求并逐项打印ID、PublishDate、pinned、title/slug及分页字段；采用后者实读范围，未声称截断payload全部读过。

## 官方核心的准入判断

| 原始材料 | 实际读到的增量与判断 | 日期/采用边界 |
| --- | --- | --- |
| [MiniMax M2.1 Blog](https://www.minimax.io/blog/minimax-m21) | 原核心的多语言/短思考/跨框架能力主张没有新训练机制或可比消融，在该披露范围关闭；不能把此判断扩为整个家族没有评价合同，固定卡新机制见末注 | 未采用图中分数、未检查全部图像或复现；Blog午夜编码不授first-public |
| [Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511/raw/main/README.md) | 核心披露selected popular LoRAs内置、identity/multi-person/drift改善和demo。未披露如何选择/融合、冲突控制、可比质量或额外成本；不能据此构造新merge机制、动态multi-LoRA加速或无损保证。贡献前关闭 | 当前README不认证Dec23历史字节；关闭不依赖first-public，不采用产品示例为机制证据 |
| [ERNIE LMArena排名](https://cloud.baidu.com/news/news_f571211f-6b51-4cbc-b5ca-57cce8f66337) | 排名/产品介绍没有新增评测方法、盲点反证或受控系统取舍，贡献前关闭。不是因为材料属于中文厂商，而是未提供能改变项目设计判断的具体增量 | 新闻文字2025-12-23 18:44:07无offset，关闭不需补造时区。数字不采用 |
| [Google年度回顾](https://blog.google/innovation-and-ai/products/2025-research-breakthroughs/) | 实际读模型/产品/创造力/科学/计算/责任与合作的回顾，链接既有Gemini、Gemma、Genie、SIMA、Suncatcher等发布。概括既有事件，不提供新方法、反证或重要修订；贡献前关闭，不把综述身份本身当排除理由 | 页面Dec23日文字；原链接月份说明仅去重线索，不冒称链接论文已审，不扫描其所有旧附件 |
| [Seed Prover1.5](https://seed.bytedance.com/en/blog/seed-prover-1-5-advanced-mathematical-reasoning-through-a-novel-agentic-architecture) | 本日实际读完整核心§1–3：已核lemma存储复用、递归并行分解，以及sketch的结构检查/逐lemma自然语言检查/rubric三信号。潜在增量是验证后组件的复用粒度与分解成本，不只是调用Lean；保留potential，不按数学题材关闭。自然语言检查与rubric不是形式正确性保证，Lean内部验证也不自动认证自然语言题意对齐；性能数字未采用 | 原始router JSON的ArticleMeta ID2141、`PublishDate=1766505600000`=Dec24北京00点，`UpdateTime=1789717565000`为后续修改。不能证明实际上线区间完全落窗，且相交25日。不得评分、入候选或Books。恢复精确原始发布范围后只路由真实归属日，不把两个相邻保留项算两家族 |

## MiniMax固定卡触发的评价协议补充

Feynman实际取得[初始官方卡](https://huggingface.co/MiniMaxAI/MiniMax-M2.1/raw/1aeff0e74785fbc01aa9b0e2e1ca03d40c1be9f2/README.md)，HTTP200、20380字符，完整读取Benchmarks与Evaluation Methodology Notes；root采用这一具名原源层同步，不以当前main回填历史内容。OctoCoding把SP/User/Memory/Tool/文件的跨步骤约束与single-violation-failure判分连接；VIBE验证requirement、container及runtime interaction。Terminal-bench移除timeout、系统提示覆盖与运行次数带来榜分可比限制。保留评价对象及配置边界potential，不授新训练算法、受控收益或安全保证。

固定commit只绑定内容身份；commit时刻、仓库创建与Blog日编码不能认证首次公开完全落窗。需可验证的该版本public公告或历史公开上下界，恢复前不评分、不进确定候选或Books。成熟Agent-as-Verifier一般原则不另作新贡献；重开只限该家族的具体验收对象与可比性。

## 外部边界与剩余普通工作

历史主Research/publications、Qwen/Hunyuan/MiMo Blog切片及Seed Prover精确事件日期保留，不支持正面证据、Books、无遗漏或零事件保证。接受原始2025历史分页/快照或具名事件带时区feed与正文公开界限；恢复只重开对应源/事件。不重复已穷尽接口，不扩整月/Weekly。

当前普通工作：arXiv sidecar初筛/必要局部、正式六部分与非作者复核。Prover核心已实际补齐；其日期限制仍为外部保留。尚可执行的工作不由外部隔离隐藏。
