# Daily Research — 2026-06-13

**规范：** V3
**窗口：** 2026-06-12T09:00:00+08:00 ～ 2026-06-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-26T12:15:31+08:00
**窗口说明：** 按用户授权仅补遗漏，原小时窗、旧候选日期/评分及有效证据保留，不搬移归属。
**补充窗口：** 2026-06-12 ～ 2026-06-12

## 1. 结论

本轮候选与Books已逐项处理，root唯一独立日级验收§107已通过，补充自然日研究完成。[运行前原稿](../_sources/daily-20260613/baseline-before-supplement-20261026.md)的旧零候选/完成声明只属于原轮，不作为本轮验收依据。DataCite注册窗两页1274记录只作导航，不是1274篇当天新论文或逐篇关闭队列。

来源筛选已有限收束，root§32校准后90份完整论文AB＝53个新增候选、18个具体贡献前N、18个旧Jun12同精确v1事件、1个跨日日期保留；另1个Kimi当日版本修复家族已低分关闭，合计54个正式家族，不是54篇论文或53项已证贡献。当前31项真实整合/唯一实际POST、21项有限具体已有覆盖、1项低分关闭、1项整项中心争议隔离，候选普通待办0。筛选、必要证据和处置依据见[准入记录](../_sources/daily-20260613/SUP_ADMISSION_20261026.md)与[必要证据](../_sources/daily-20260613/SUP_NECESSARY_20261026.md)。旧日期/评分不迁移，完整日级验收§107通过不授隔离项正面证据。

值得保留的变化集中在可消费接口：训练辅助latent不等于部署时的硬信息瓶颈，检索到某片段不等于可以静默更换其representation，预留symbol可生成不等于已绑定新对象。相关整合把训练信号、运行时资产与最终consumer分开留身份，并把离线制备、额外forward、索引/路由和独立质量回归的费用放回同一条链。

另一组结果修正评价权限：真实citation不等于支持claim，可信reference仍可能被harness在错误时点比较，注意力/entropy/可读几何也不等于任务必要或唯一算法。有限NC是现有具体正文足以承载受限机制/反侧，不是整篇强中心已证；PRISMR rank、LaME信息界、ReSum完整SGPO/不退理论、PatternMatching entropy等未采用子主张仍精确隔离。A2D2实际law/holding/bridge中心争议整项暂缓，无正面Book采用。所有实测仍是作者报告，未声称复现、实现审计或生产安全。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方news RSS单XML，Jun12 UTC00 Preply/UTC10 Academy课程；邻段即停，产品案例/课程非模型系统机制 | 已检查 | 不授全网无遗漏 |
| SRC-ANTHROPIC | listing/research/default/2共24posts，Jul28至Apr23；Jun12 PublicRecord后Jun08跨目标停止；完整core/Method/Limitations公众态度调查非机制证据 | 已检查 | 不等于机构无发布 |
| SRC-GOOGLE-AI | Google Blog六月一页Jun12 skin/phones后Jun10；phone完整core是通用课程云，DeepMind FromAGItoASI完整官方AB是四路径展望，具体前N | 受阻 | Publications历史日级目录不可恢复，有限Blog/搜索不补齐 |
| SRC-META-AI | 当前Research及global_search page3有限混合结果；Publication Jun29→Jun05，混有people/blog | 受阻 | 不是完整Jun12目录，等待有日期官方列表/具名原文 |
| SRC-QWEN | 正确type=qwen_ai、en-US/zh-CN各40articles完整响应，无分页字段；June1→June16Robot→June23AgentWorld | 已检查 | 无Jun12列项，不用无参数空数组授零 |
| SRC-DEEPSEEK | 官方Updates单页Apr24→Jul31跨目标即停 | 已检查 | 无Jun12列项，不遍普通commits |
| SRC-MOONSHOT | Kimi Blog末新2025-11-07，org repos单响应42项；具名Code changelog Jun12 0.14.1/0.14.2完整core按两事件筛选，目标下邻Jun10 | 已检查 | 一家族4分关闭/仅报告，不记零发布或核验实现 |
| SRC-TENCENT-HUNYUAN | 官方POST publicList page1/size100/renderType0、accept-language:zh，中文All code0/total11/list11；May21→Jul06，无下一页 | 已检查 | 无Jun12，不以默认英语9条当全部 |
| SRC-ZAI | 官方Research时间排序首屏Jun16GLM5.2→May20ZCube，跨目标即停 | 已检查 | 无Jun12卡片 |
| SRC-BYTEDANCE-SEED | public_papers首屏1–20of247/Page1of13，Jun19→Jun11化学反应网络→Jun4跨目标 | 已检查 | 无Jun12，不遍其余12页 |
| SRC-BAIDU-ERNIE | 官方中文Blog首屏最新May9文心5.1，早于目标即停 | 已检查 | 无Jun12列项 |
| SRC-XIAOMI-MIMO | 官方ModelRelease Sep22→Jun02ASR→Apr23；实际Blog资源双语frontmatter Jun10Code→Jun08TileRT→May30 | 已检查 | 有日期入口无Jun12，不给无日期route补时间 |
| SRC-MINIMAX | 官方Blog单目录Jun09MaxProof→Jun01M3；MSA论文另由arxiv发现并与旧Jun12同v1去重 | 已检查 | Blog未列不排除技术论文 |
| SRC-ARXIV | DataCite合法client-id=arxiv.content、registered Jun11UTC16至Jun12UTC15:59:59两页1000+274即停；主题有界补检90完整AB已校准。合法CL/LG `2026-06?skip=0&show=2000`各首2000身份，仅具名线索导航带CL66/LG106次出现与原NAV比对，无新身份（root§42） | 已检查 | 编号带非日证；CL另页未扫，不作全月/全类召回；原2606形状404非访问H；12505跨日隔离见§5 |

实际入口、原字段、请求和停止位置见[来源记录](../_sources/daily-20260613/SUP_SOURCE_CHECK_20261026.md)及[首次抓取原回执](../_sources/daily-20260613/SUP_FETCH_RECEIPT_20261026.json)。只检查每日组和具名触发，没有运行Weekly/Live/其他年份。

## 3. 候选与判断

以下为本轮实际准入且联合界限定Jun12的新增家族。同精确DOI的arxiv.content/findable/registered与唯一v1 Submitted按适用公告/发号规则联合限定最早/最晚界，created不作公开证据；这不是登记即实际公告，也不证明全球首公开。原件保留于本日DataCite两页。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Drop-by-Drop](https://arxiv.org/abs/2606.12876v1) | 2026-06-12 | 单checkpoint有序码本前缀支持多bitwidth；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49正文](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，root实际POST§23通过 |
| [TWLA](https://arxiv.org/abs/2606.13054v1) | 2026-06-12 | 近邻有限差分交互与链代理精度分配；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49正文](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，root实际POST§28通过 |
| [Mental-R1](https://arxiv.org/abs/2606.13176v1) | 2026-06-12 | 显式阶段均值的signed entropy优化压力；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33正文](../../../../books/part-04-training-system/33-grpo.md)，root实际POST§6通过 |
| [ReSET](https://arxiv.org/abs/2606.13233v1) | 2026-06-12 | step-relative调温与small-M低位执行分责；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49正文](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，root唯一实际POST§13通过 |
| [Module-wise Manifold](https://arxiv.org/abs/2606.13276v1) | 2026-06-12 | attention/MLP参数几何与尺度自由度的受限反侧；2+2+2=6 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[Ch28正文](../../../../books/part-04-training-system/28-pretraining.md)，root实际POST§21通过 |
| [Next-token Generalization Bounds](https://arxiv.org/abs/2606.13280v1) | 2026-06-12 | 独立文档与文档内context估计的统计轴分责；2+1+3=6 | 深入完成 | 整合：`WORLDVIEW-SCALING-LAW`，[Ch7正文](../../../../books/part-01-worldview/07-scaling-law.md)，root实际POST§29通过 |
| [OPD Sparse Updates](https://arxiv.org/abs/2606.13657v1) | 2026-06-12 | dense监督不等dense改写，子网与optimizer反侧；2+2+3=7 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33正文](../../../../books/part-04-training-system/33-grpo.md)，root实际POST§16通过 |
| [LoRA-alpha](https://arxiv.org/abs/2606.12883v1) | 2026-06-12 | alpha映射与学习率参数步非一般全程等价；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA`，[Ch30正文](../../../../books/part-04-training-system/30-lora.md)，root实际POST§20通过 |
| [SWITCH](https://arxiv.org/abs/2606.13106v1) | 2026-06-12 | 离散boundary/确定latent与frozen条件下text梯度覆盖分责；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33正文](../../../../books/part-04-training-system/33-grpo.md)，root实际POST§39通过 |
| [Select and Improve](https://arxiv.org/abs/2606.13125v1) | 2026-06-12 | 控制SFT策略人口/RL难度分开selection/improvement；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33正文](../../../../books/part-04-training-system/33-grpo.md)，root实际POST§39通过 |
| [Jeffrey Guidance](https://arxiv.org/abs/2606.13240v1) | 2026-06-12 | 明示marginal目标与cleanestimate近似/FID反侧；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root实际POST§36通过 |
| [DuET](https://arxiv.org/abs/2606.13303v1) | 2026-06-12 | 暂释放source conditioning再回edit的fidelity取舍；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24条件分时/源保真正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root§43独核通过 |
| [Flex4DHuman](https://arxiv.org/abs/2606.13655v1) | 2026-06-12 | relative SE3/view位置与clean-history多视角rollout接口；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root§47实际POST通过 |
| [HYDRA-X](https://arxiv.org/abs/2606.13289v1) | 2026-06-12 | image/video codec重建/semantic及latent编辑分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，root§47实际POST通过 |
| [RepWAM](https://arxiv.org/abs/2606.13674v1) | 2026-06-12 | semantic visual/action tokenizer改变joint future/action表示；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25 latent-action/adapter正文](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，root§56通过 |
| [MoVerse](https://arxiv.org/abs/2606.13376v1) | 2026-06-12 | panorama/Gaussian持久状态与causal观察renderer分工；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25 persistent-state/renderer正文](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，root§56通过 |
| [TetherCache](https://arxiv.org/abs/2606.13035v1) | 2026-06-12 | long-video relevance/diversity选择与召回污染分治；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root§47实际POST通过 |
| [AIR-VLA+](https://arxiv.org/abs/2606.12859v1) | 2026-06-12 | movement/manipulation单向cascade与gradient隔离；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，root§73实际POST通过 |
| [A2D2](https://arxiv.org/abs/2606.13565v1) | 2026-06-12 | joint insertion/unmask路径measure与reward-tilted目标；2+2+3=7 | 争议 | 暂缓：实际adaptive path-law/holding/bridge未闭，不作正面证据或Books，root§58安全终态通过 |
| [Observable Patterns Are Not Explanations](https://arxiv.org/abs/2606.12689v1) | 2026-06-12 | matchedcontrol/干预区分latent可decode与因果使用；2+2+2=6 | 标准完成 | 已有覆盖：`MODEL-DECODER-ONLY`，[Ch18必要性/readout正文](../../../../books/part-02-model/18-decoder-only.md)，root§51独核通过 |
| [WEAVER](https://arxiv.org/abs/2606.13672v1) | 2026-06-12 | future proprio+views消费状态与latent reward接口；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)模态state/QueryClosure/latent反馈三处，root§26通过 |
| [InterleaveThinker](https://arxiv.org/abs/2606.13679v1) | 2026-06-12 | 强generator正例偏置、判断vsregeneration delta信用分开；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)ICRL/ECHO/Second-order及Ch80消费边界，root§26通过 |
| [Bag of Dims](https://arxiv.org/abs/2606.12629v1) | 2026-06-12 | 标准basis sign/magnitude读写限定SAE需求；2+2+2=6 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`，[Ch5正文](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，root§63实际POST通过 |
| [CAPED](https://arxiv.org/abs/2606.12666v1) | 2026-06-12 | task条件pre-upload屏幕暴露与utility/privacy分验；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72正文](../../../../books/part-06-ai-infrastructure/72-security.md)，root§63实际POST通过 |
| [Task-specific Psychometric Evaluation](https://arxiv.org/abs/2606.12730v1) | 2026-06-12 | intention selfreport代理行为的context/persona人口边界；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root§70实际POST通过 |
| [GRIP](https://arxiv.org/abs/2606.12744v1) | 2026-06-12 | consumer反馈训练视觉retriever及跨consumer复用；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG`，[Ch76 consumer-utility正文](../../../../books/part-07-agent/76-rag.md)，root§69通过 |
| [Anchoring](https://arxiv.org/abs/2606.12818v1) | 2026-06-12 | edge/node faithfulness与跨posttrain anchor方向资格；2+2+2=6 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION`，[Ch5功能迁移正文](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，root§69通过 |
| [TimeROME](https://arxiv.org/abs/2606.12841v1) | 2026-06-12 | MDLM denoise定位时钟与每step livehook部署分责；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72正文](../../../../books/part-06-ai-infrastructure/72-security.md)，root§70实际POST通过 |
| [AGAR](https://arxiv.org/abs/2606.12898v1) | 2026-06-12 | attention定位与文字读取利用解耦后的重绘干预；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，root§73实际POST通过 |
| [X-MADAM](https://arxiv.org/abs/2606.12903v1) | 2026-06-12 | 去template反转且oracle仍好定位抽取瓶颈；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG`，[Ch76正文](../../../../books/part-07-agent/76-rag.md)，root§77实际POST通过 |
| [TabPFN Causal Analysis](https://arxiv.org/abs/2606.12917v1) | 2026-06-12 | 强head定位不等固定steering方向可跨sample；2+2+2=6 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION`，[Ch5读出/必要/恢复/迁移正文](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，root§76通过 |
| [PRISMR](https://arxiv.org/abs/2606.12942v1) | 2026-06-12 | 遗漏排序候选与instance LoRA条件化替代；2+2+3=7 | 深入完成 | 已有覆盖：`TRAIN-LORA`，[Ch30条件hypernet正文](../../../../books/part-04-training-system/30-lora.md)，rank子命题不采，root§84通过 |
| [EPM-JEPA](https://arxiv.org/abs/2606.12979v1) | 2026-06-12 | prereg null与buffer/EMA/LoRA动态拆解；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25条件状态/目标正文](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，root§84通过 |
| [Emo-LiPO](https://arxiv.org/abs/2606.13006v1) | 2026-06-12 | fixed transcript内声学强度listwise目标；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-DPO`，[Ch34冻结偏好信号/列表目标正文](../../../../books/part-04-training-system/34-dpo.md)，root§88通过 |
| [LaME](https://arxiv.org/abs/2606.13061v1) | 2026-06-12 | latent辅助contrastive/AR监督与最终consumer可见图分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，仅辅助监督/consumer接口，IB理论不采，root§81POST通过 |
| [ASR and Diarization](https://arxiv.org/abs/2606.13095v1) | 2026-06-12 | length-aware speaker loss与overlap ASR阈值分责；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[Ch23字段监督正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，root§88通过 |
| [FCGraft](https://arxiv.org/abs/2606.13097v1) | 2026-06-12 | function cache graft/stitch/patch的上下文有效性；2+2+2=6 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78正文](../../../../books/part-07-agent/78-tool-calling.md)，root§98实际POST通过 |
| [PolyFlow](https://arxiv.org/abs/2606.13400v1) | 2026-06-12 | polytope支持嵌入discrete-time flow的约束资格；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root§98实际POST通过 |
| [WISE](https://arxiv.org/abs/2606.12852v1) | 2026-06-12 | causal event记忆/机会式调度改变controller信息接口；2+2+2=6 | 深入完成 | 整合：`AGENT-PLANNING`，[Ch79正文](../../../../books/part-07-agent/79-planning.md)，root§89实际POST通过 |
| [E-commerce Agent Memory Study](https://arxiv.org/abs/2606.12924v1) | 2026-06-12 | 同buyer下memory与过程/结果judge代理反侧；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77原源/派生结构正文](../../../../books/part-07-agent/77-memory.md)，并用Ch66 TRACE判分边界，root§96通过 |
| [STG](https://arxiv.org/abs/2606.12983v1) | 2026-06-12 | RTL testbench false-pass/coverage与oracle资格；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root§100实际POST通过 |
| [AuthorityBench](https://arxiv.org/abs/2606.13104v1) | 2026-06-12 | claim真假×citation真假对照拆权威/事实混杂；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66 cue/内容与引用支持正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root§102通过 |
| [CARVE VideoRAG](https://arxiv.org/abs/2606.13141v1) | 2026-06-12 | 视频证据依赖盲区与检索/生成粒度分责；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG`，[Ch76正文](../../../../books/part-07-agent/76-rag.md)，root§103实际POST通过 |
| [BlockAttnRes Causal Analysis](https://arxiv.org/abs/2606.13168v1) | 2026-06-12 | routing平均质量不等causal必要性的matched反侧；2+2+2=6 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION`，[Ch5描述量/局部干预正文](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，root§102通过 |
| [CoDeR](https://arxiv.org/abs/2606.13204v1) | 2026-06-12 | coverage与负约束compatibility encoder分责；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG`，[Ch76正文](../../../../books/part-07-agent/76-rag.md)，root§106实际POST通过 |
| [ReSum](https://arxiv.org/abs/2606.13316v1) | 2026-06-12 | summary触发处mask/非触发处插入的匹配分支；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33 prefix干预/分支人口正文](../../../../books/part-04-training-system/33-grpo.md)，仅有限采样接口，SGPO/理论强保证隔离，root§105通过 |
| [OneRetrieval](https://arxiv.org/abs/2606.13533v1) | 2026-06-12 | 语义identifier reserved slots部署后可编辑；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG`，[Ch76正文](../../../../books/part-07-agent/76-rag.md)，root§106实际POST通过 |
| [QueryMix](https://arxiv.org/abs/2606.13537v1) | 2026-06-12 | embedding语言混合/English index的非对称条件；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-RAG`，[Ch76语言/索引/调权人口正文](../../../../books/part-07-agent/76-rag.md)，局部插值验证留报告，root§105通过 |
| [Reasoning as Pattern Matching](https://arxiv.org/abs/2606.13607v1) | 2026-06-12 | 头干预与人类irrelevant-detail错误的受限关系；2+2+2=6 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION`，[Ch5局部干预/独立行为正文](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，entropy/强全称不采，root§102通过 |
| [RA-RFT](https://arxiv.org/abs/2606.13680v1) | 2026-06-12 | expected reasoning benefit检索与analogous outcome RL；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-RAG`，[Ch76 utility/consumer适配正文](../../../../books/part-07-agent/76-rag.md)，root§105通过 |
| [PERIA](https://arxiv.org/abs/2606.12830v1) | 2026-06-12 | 同prompt文本observation近似合组的credit资格；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33正文](../../../../books/part-04-training-system/33-grpo.md)，当前v2受影响层/唯一POST§66通过，不新增家族评分 |
| [Biomedical Claim Verification Shortcuts](https://arxiv.org/abs/2606.12854v1) | 2026-06-12 | NEI空evidence可分离的输入结构混杂；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66输入负控制/人口正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，局部NEI案例留报告，root§102通过 |
| [Influcoder](https://arxiv.org/abs/2606.13668v1) | 2026-06-12 | response-LoRA-gradient影响ranking蒸馏独立可缓存encoder；2+2+2=6 | 深入完成 | 整合：`TRAIN-DATA`，[Ch27正文](../../../../books/part-04-training-system/27-data.md)，root§52实际POST通过 |
| [Kimi Code CLI 0.14.1/0.14.2](https://www.kimi.com/code/docs/en/kimi-code-cli/changelog.html) | 2026-06-12 | shutdown取消/后台停止与overlap active-agent绑定修复声明；1+2+1=4 | 已关闭 | 仅报告：具体版本事实，不改变长期Books机制，root§30通过 |

## 4. 证据与知识整合

### [Mental-R1](https://arxiv.org/abs/2606.13176v1)

实际审阅III/IV、Eq4–8/Alg1、TIII/Fig5及直接反侧：固定tags划分的阶段各求全词表token entropy均值，signed coefficient改变阶段优化压力，不是内部认知或正确性证明。Qwen3-8B、8×RTX PRO6000、BF16/ZeRO2、四generation、prompt/completion各max512、1epoch；五次是推理重复而非独立训练seed。结构/平衡reward、调参及TRL/verl实现差限制单组件归因，不采用健康诊断效果或类人认知因果。

现有TRAIN-GRPO统一entropy bonus/token-flow段未承载同completion内signed stage接口；已在2605-11491 binding后/ToolFeedback小节前补两段和独立marker，真H2 Review notes留来源/边界。root必要源/actualowner/逐字PRE§5及唯一实际POST§6通过。完整证据/原稿见[N1](../_sources/daily-20260613/SUP_NECESSARY_20261026.md)。

### [ReSET](https://arxiv.org/abs/2606.13233v1)

§3–6/B1/B4–6/D已读足当前采用命题。双换行只近似step，段初window/随后causal均值不偷用未来tokens；选择性调温改变分布而非恢复BF16，T1/T3仍有退步。每model/task calibration与附录每model五道NuminaMath/无task-tune披露未闭，不采用零调参迁移。

小M路径读真实NVFP4编码，在register反量化后用FP16 FMA，大M/Prefill另走TensorCore；四位storage不等原生FP4算术。作者单B200、W4A4/BF16KV、输入512/B1/8/长输出计时已含sampler，但不认证生产SLO或其他格式/batch。root必要源/actualCh49/PRE§10通过，按收窄命题最终2+2+2=6仍深入；三段/marker/本人注已真实保存，§12–13唯一实际POST通过。完整证据/原稿见N3。

### [OPD Sparse Updates](https://arxiv.org/abs/2606.13657v1)

root唯一必要首备§9实际核exact-v1 §3–6/A3/必要A4/A9，作者直接采用该层，不第二Methods。存盘BF16差分阈值稀疏不等逐步稀疏梯度，谱集中不等exact lowrank；先完整OPD发现mask再同source重跑不是免费发现或稀疏执行。保AdamW/SGD局部反侧，不作on-policy唯一因果。actualowner Ch33既有OPD诊断缺末态可见性/坐标支持与发现费用分责，N4原两段已保存，root§14 PRE/§16实际POST通过，未核实现/复现。

### [LoRA-alpha](https://arxiv.org/abs/2606.12883v1)

root唯一必要首备§15实际核§2–5/A/D1/H3/G4，作者直接采用。有限双线性更新中的alpha改变有效映射/Jacobian而学习率作用于factor参数步；局部一步匹配不推出完整轨迹等价。期望trace不约束最大特征值，Adam局部近似不授SGD全程结论；默认alpha仍有反退/单run与调参预算。受限新增命题最终6分但保已深入层，Ch30 SignSGD段后/optimizer几何前已保存原两段，root§17 PRE/§20实际POST通过，不采用普遍免调参recipe。

### [Module-wise Manifold](https://arxiv.org/abs/2606.13276v1)

exact-v1 §2–5/A实际读足：Stiefel固定Gram同时固定尺度，DGram仅固定非对角仍放列范数；受限GPT2-small/OpenWebText/50k/单seed1337共同超参下attention/MLP反置与全DGram失稳，但DGram无decay、谱非完整因果、小loss差与尺度反例保留。Ch28已有normalizer×optimizer负交互未承载参数可行域/module尺度自由度；root§19必要/actualowner/N5两段PRE通过，按窄授真实保存，§21唯一实际POST通过。

### [Drop-by-Drop](https://arxiv.org/abs/2606.12876v1)

exact-v1 §4–7/Alg1/I1三表必要实际读：有序前k码本按加权activation-WMSE共同监督，而非普通最高精度产物任意drop。group8/8bitindex、1024/32校准验证、所测A40/RTX6000/L40多数drop切片改善仍有Qwen0.5 k4反退、Llama8B k3逊独立AQLM；fixedX/Gaussian动机不授有限码本无损，k≥3只是经验floor。总bits含码本/scale/未量化张量，在线loading/mixedprecision仅futurework。Ch49 08118后/BARQ前两段已保存，root§22 PRE/§23实际POST通过；详N7，不认证实现/复现或SLO。

### [TWLA](https://arxiv.org/abs/2606.13054v1)

exact-v1 §3–4/B2/B7–8/C3必要实际读，仅采用A8参考下unary NLL与相邻joint-minus-unaries差分冻结为链代理、DP精确解该sum-bit预算；不授真实全网NLL/bytes/latency全局最优。RTXA6000/128×2048 WikiText2校准、Llama/Qwen，三受测模型pair较unary改善，高阶133→423min统计费用且Qwen3可退；有限Jacobian/小扰动假设不认证所有远程耦合可忽略。ternary信息位不等物理包/scale，完整pipeline吞吐不独归此分配。最终6分保已深入，Ch49 13440后/LFQ前两段保存，root§25 PRE/§28实际POST通过；详N8。

### [Next-token Generalization Bounds](https://arxiv.org/abs/2606.13280v1)

exact-v1 §2.2/3/4及B必要实际读：每篇独立context的N2F模型区分n篇训练人口与每篇T观察对共享语言规律/局部context估计的作用。末位置ERM/expectedKL、bounded logits、smooth latent函数、规则embedding、指定充分大架构与渐近域不等真实全位置SGD/长尾语料或同token预算最优切分。fixedW旧n-gram仍有适用域，未核全部C–G定理或实践exponent。Ch7 raw/unique/effective-token段后两段保存，root§27 PRE/§29实际POST通过；详N9。

### [Jeffrey Guidance](https://arxiv.org/abs/2606.13240v1)

exact-v1 §2.1/3.1–2/4.1/C/F1/F3实际读足明示marginal目标→densityratio→cleanestimate近似。support内理想joint保conditional，不等实际t>0 noisy score；非线性作用于posterior均值与先积分不交换、λ/timewindow又改目标。C24符号与正文冲突，不采用完整精确recipe。CIFAR/FFHQ Inception对齐大降FID却短window几乎不改观感、CMMD可退；不是独立感知/公平性证明。线性ratio15epoch、100step DDIM、全部候选/反传/评价费保留，F1/F3 base训练披露不拼免训练。Ch24 FMRG后两段已保存，root§33 PRE/§36实际POST通过；详N12。

### [WEAVER](https://arxiv.org/abs/2606.13672v1)

有效§3/5.1及root§11复用，仅补§4/5.2.1/A5：futureproprio+views让同输入consumer续想象，RoboMeter蒸馏latent reward/critic省逐候选decode判分；memory继承。928M/4H100十天/DROID、Franka/两cam/5Hz、五任务每50FT+20eval且先选base≥20%success，相关ρ.87限此policy/task人口。视觉隐state、变形/颗粒、teacher噪声、在线最多单chunk均保，不授安全/全费匹配。Ch25 DWMP模态state、QueryClosure及24587 latent反馈的实际完整论证已承载采用命题，具体已有覆盖，root§26通过；详N10。

### [InterleaveThinker](https://arxiv.org/abs/2606.13679v1)

有效§3.2–3.3/4.3T5/root§11复用，仅补§4.1/5。强generator正例偏斜与弱负例、filter/balance的联合效应、判断reward与regeneration后Gemini delta分开；不能把未隔离variance split或fixedplan升为local→global。Qwen3VL8B/8H800约50h，SFT2epoch/RL1epoch/N8、最多每step5refine，base generative prior仍限制概念支持，未授call-matched净收益。Ch33 ICRL/ECHO/Second-order的信用/标签人口、Ch80 CRITIC-R1及干预净收益完整论证已具体覆盖，root§26通过；详N11，未造Bookdiff。

### [SWITCH](https://arxiv.org/abs/2606.13106v1)

root§31唯一必要首备§3/4/5/Limits/A/B/I，作者直接采用未第二Methods。enter/exit categorical边界与确定hidden注入分责，frozen旧prefix/latent no_grad/KV只支持该条件下text更新，不授完整hidden过程无偏PG。8H20/Qwen3-8B/OpenR1Math、T6全体同范数随机向量/skip反侧及selected成功子集分开；Kmin非自主深度，可见token未计latentforward。Ch33 20328后原两段按root§37唯一改句已保存，§39唯一实际POST通过；详N14。

### [Select and Improve](https://arxiv.org/abs/2606.13125v1)

exact-v1 §2–4/T1/F2–6文字/C已读：受控GF11/Qwen2.5-1.5B/LoRA、3SFTseed各一RLrun区分策略分派与条件内改进。easy SFT聚合约80%相似不等hard6–9起点相同（24.5/57/47），不授多样性唯一因果；rule-based trace不证内部算法，easyRL反退不推出所有任务课程规则，未出现新技能不等RL永不能创造。1–4A10040G及全部起点/rollout费保留。Ch33 bestG后两段按root§38收窄已保存，§39唯一实际POST通过；详N13。

### [DuET](https://arxiv.org/abs/2606.13303v1)

root§34唯一必要§3/4/T2/factorial/4.4直接复用：同权重单trajectory暂撤source条件、用targetcaption再恢复edit，不是两个expert权重合并。匹配VLM预算与IEP/I2IC局部对照支持条件可见性分时，4B[35,45]FC逊baseline/保真下降及judge口径保留，全部VLM/区间搜索/采样计费。Ch24 2512.25066源冲突/分时与独立保真、06667条件交接、07219旧关系回流的完整正文已具体覆盖采用域；6分标准完成/已有覆盖，root§43通过，无Book改动，详N15。

### [Flex4DHuman](https://arxiv.org/abs/2606.13655v1)

root§35唯一必要§3/5/7复用：viewslot输入身份不等relativecamera几何，分带位置与位姿参与attention；PRoPE继承且16→36输入另变，不归因仅改RoPE。GTreference/自产overlap已有覆盖；静态rig、有限42帧、32H100/40steps/CFG3、特权skeleton与部分前景指标逊对照均保留，不授任意pose/slot不变或无限稳定。Ch24 GTA12957后/06667前一段真实保存，6分差额深入、root§44PRE/§47实际POST通过，详N16，未核pixels/code/复现。

### [HYDRA-X](https://arxiv.org/abs/2606.13289v1)

root§40唯一必要§3–6/A4/E复用：训练decompressor让压缩Sem对齐较密videoteacher，部署删D；跨图source→target只在Semstage，Gen独立，不授解耦或新创HYDRA骨架。Tubelet更快/AI2Dimage-teacher反侧、1.5B消融与7B人口分开；17帧不批准longvideo/edit，完整teacher/codec/语言训练费保留。受限命题最终6分，Ch23 16373后/Rate前两段真实保存，root§45PRE/§47实际POST通过，详N17。

### [TetherCache](https://arxiv.org/abs/2606.13035v1)

root§41唯一必要§4/5/A1/A4复用：finalcleanpass接纳的新KV向旧sink/memory moments部分对齐，既有条目不重复对齐但可重选淘汰；不是精确复用或永不改写物理内存。Pooledproxy不等attentionmass/语义覆盖，std零方差未补稳定项；自产trusted非真值，单H20/240s生成更慢和局部分项反退保留。6分差额深入，Ch24 SceneCache16003后/VACE前两段真实保存，root§46PRE/§47实际POST通过，详N18。

### [Observable Patterns Are Not Explanations](https://arxiv.org/abs/2606.12689v1)

实际§3/4/7/Limits/C2/C3采用域：无hiddenrecurrence的PaT也复现BFS-like图案，改curriculum可反转，base近零故非所有GPT2天然有frontier；logitlens也不特异于CODI。Family训练预算不同、bootstrap非独立训练复现，不采未读§5/6完整geometry/Markov主张。Ch18 10229接口/06374必要性/00449readout与patch完整正文已明确图案不唯一归因、移除替换与行为检验，6分标准完成/具体已有覆盖，root§51通过，无Book改动，详N20。

### [Influcoder](https://arxiv.org/abs/2606.13668v1)

实际§4/5/6/8/A1/A3/A4/A6读足：response-LoRA CountSketch cosine只当rankingteacher，再训独立encoder缓存sampleembedding，不是fullgradient/Hessian/删除因果。1.7B主评估与360M费用、1B毒性人口分开，部分质量逊LESS，pool/query分布外明显退化及额外querylabel/stocking/encoder调参费保留，不授通用过滤安全或跨protocol加速。6分差额深入，Ch27 17835后/16181前两段真实保存，root§48PRE/§52唯一实际POST通过，详N19。

### [RepWAM](https://arxiv.org/abs/2606.13674v1)

root§49唯一必要§3/4/5直接复用。冻结visualcodec/IDM-FDM拟latenttransition再motor适配，低维/Kz+δ不保证防漏或真实actuator；100G/300G两stage、不同H20主表/消融与少量实机不混因果。OLS好而实机差、仿真平均逊对照和全部teacher/codec/训练/控制费保留。Ch25 LatentAction05230、effect10104/factor16229/operator与ΔVLA正文已具体承载producer/consumer和动作资格，Ch26 UniT明确实际action接口；6分标准完成/具体已有覆盖，root§56通过，详N22，无Book改动。

### [MoVerse](https://arxiv.org/abs/2606.13376v1)

root§50唯一必要§2.4/3.1/3.4/3.5/4直接复用，仅StageIII消费固定panoramicGaussian布局与当前camera render，localKV/causalstudent负责画质stream；不采未读I/II构造配方。Panorama错误固化/遮挡反光/漂移、dynamicworld/反馈仍future；定性未核pixels，4090/8FPS非完整SLO，全部离线制备/renderer/codec/cache费计。Ch25 Persistent25077/VerseCrafter05138/mesh00299/E³C具体正文已承载空间载荷→observerstream，6分标准完成/已有覆盖root§56通过，详N23，无Book改动。

### [A2D2](https://arxiv.org/abs/2606.13565v1)

7分深入必要完成但中心主张争议，root§58独核后安全隔离。实际§2–4/语言5.3+12/9.7必要RN/9.8关键推导/Alg1–5：仅insert/unmask的RN与实际quality-remask/delete路径未闭；Eq124仅jump乘积→125 endpoint-interpolant四loss的holding/bridge/quality likelihood未论证，Alg2 Poisson时间步与logweight也不一致，不只Eq17目标符号。正面CTMC原则不充作新贡献强写Books。语言评估有任务格式/compile/edit reward与HumanEval infill exactmatch，非执行pass@1；更多步可退、仅两行未隔离qualityheads，NFE不等全生命周期费用。未扩science应用或未依赖附件，详N24；不正面采用exact adaptive reward-tilt、完整更新recipe或性能保证，Books暂缓。

### [Bag of Dims](https://arxiv.org/abs/2606.12629v1)

root§54唯一必要§2/3/5/A1.1/A5直接复用：有标签anchor的原坐标sign prototype可作SAE之外的读出基线，type/context符号与跨层差异不支持独立寄存器；LMhead参照非答案真值、静态权重非causalwriter、steering不稳及多特征SAE更好反侧保留，标签/全词表前向/搜索费计。受限经验命题最终6分而非普遍基础7，具体差额深入，Ch5几何分区14347后/SAE前两段真实保存，root§59PRE/§63实际POST通过，详N25。

### [CAPED](https://arxiv.org/abs/2606.12666v1)

root§55唯一必要II/III/IV/VI+A/B直接复用：可信侧解释task→选择screen曝光，共用placeholder，先外送task再遮图已先漏；相关非授权/unknownPublic/open/累积风险明确。成功子集WSLR非同人口，28任务仍残漏/connected反退，AndroidWorld77→64，不以judge稳定/临时disclosure设计认证gold或用户收益。Host/service不是物理手机、精确开销比例不闭，全部解析/OCR/VQA/redaction/loop费计。6分差额深入，Ch72 PrivWeb后/AgentPrivacy前两段真实保存，root§59PRE/§63实际POST通过，详N26。

### [PERIA](https://arxiv.org/abs/2606.12830v1)

原v1归属/6分保留。[当前精确v2](https://arxiv.org/html/2606.12830v2#S4.SS3)的Comments具名方法澄清触发仅§4.3/C3受影响层：动作后resultingobservation分组、不要求同prestate，tokenratio排toolobs/fullcontext/span广播；root§57独核通过，未全版本diff。补当前§4.1/5setup–5.2/A/B1–2/D1/E2/C2cost后，OR相对exact组的局部提升不等信用无偏；δ.9→.5使非零stepadvantage比例62.3→68.5但accuracy54.1→48.9，任务分项/无RL或无tool更好切片保留。SFT10661/RL8652、完整test与2B10%诊断不同人口、10interaction+final/规则后GPT5Mini及全部teacher/工具/rollout/训练费限定，不授安全或净SLO。Ch33 GAGPO13217后两段真实保存，root§65PRE/§66实际POST通过，详N21/N27，不新增家族或倒填v1实测。

### [GRIP](https://arxiv.org/abs/2606.12744v1)

root§61唯一必要§3–6复用：视觉近邻非固定consumer utility，逐单例反馈训contrastive视觉encoder；classification/VQA只加例后正确，不能全叫扣原基线的增量收益。跨consumer UC80.0逊同85.2及CLIP85.9，局部无独立run误差不授modelagnostic；全teacher调用/labeljudge/200epoch/重编码索引费用保留，hardware/precision未披露。Ch76 LURE19535/RRPO02091完整reader绑定/单例不等组合/迁移重验正文已覆盖，5分标准完成/具体NC、root§69通过，详N28。

### [Anchoring](https://arxiv.org/abs/2606.12818v1)

root§62唯一必要§2–6/Limits复用：100OpAQ/九选与20order行为、4rotation400circuitpairs分开；单tokencorrect−anchor logit、clipCPR不代表全输出。Base/instruct几何shared仍可在稀疏功能transfer大退，局部random只排该替代解释，不授后训练唯一因果/通用电路。全部pairedforward/IG/预算扫与功能回归计，hardware/precision未披露。Ch5 08292/04119/08348/22600完整正文已具体分开恢复、geometry与checkpoint迁移，6分标准完成/NC，root§69通过，详N29。

### [Task-specific Psychometric Evaluation](https://arxiv.org/abs/2606.12730v1)

root§60唯一必要§2–5/6.1–6.4/A复用：自报instrument经sharedsession可prime后续行为，分session只同初始设置；11模型/4任务/grid与persona人口、best|r|选择/聚合CI不是单模型人格真值。移context后部分相关衰减、部分仍保留，persona不普遍救相关但非全无用；不采trainingorigin/安全训练因果或人类意识。完整API/grid/行为回归费用保留。6分具体缺口深入，Ch66 25846后/VLA29730前两段真实保存，root§69PRE/§70实际POST通过，详N30。

### [TimeROME](https://arxiv.org/abs/2606.12841v1)

root§64唯一必要III–VII复用：MDLM denoising-time追踪只提候选，实际每step livehook与U/D/G资产非只最佳时刻介入，冻backbone不是参数删除。TopQ位置先后未闭，不抄精确recipe；26s含capture/3.87s solve与逐步/驻留费分开，0activationbackward不等0额外内存。高forget损retain/RealAuth、邻项同降/过纠错/relearn弱及观察者条件保留。6分遗忘强制深入，Ch72 08623后/25994前两段真实保存，root§69PRE/§70实际POST通过，详N31，不授可靠unlearning或安全发布。

### [AIR-VLA+](https://arxiv.org/abs/2606.12859v1)

实际§3.2–3.5/4.1–4.3/T1–3/A读足：manip意图detach供move、dense专家与输出维度拼ODE分责，只有该边断梯度，sharedbackbone仍共同更新；不从硬切片/MLPgrasp授动力学解耦或接触真值。IsaacSim12D、2A100/30k+10k/10NFE/每task20rollout非训练seed，组合分项仍反退，idle可有Safe100，全部训练/多路forward与控制回归计费。6分差额深入，Ch26 20894后/坐标H3前两段真实保存，root§71PRE/§73POST通过，详N32，未核pixels/code/实机复现。

### [AGAR](https://arxiv.org/abs/2606.12898v1)

实际§3.1–4/5.1–5.2/T1–3/5.5/6/A7/A8/A10读足：known原T与renderer boxes必需，queryattention只提patch→char映回后重render再消费，非任意OCR/新观察或attention因果。Oracle联合FT/TF与SubEM不拼mainEM/F1，近token匹配uniform/random支持有限选择效应，sweep及原正确题仍可退；2A100/BF16、visualtoken增量不含两forward/attention/renderer费用。6分差额深入，Ch23 ReadingRight25770后/Focus前两段真实保存，root§72PRE/§73POST通过，详N33，不授无损压缩或净加速。

### [X-MADAM](https://arxiv.org/abs/2606.12903v1)

root§67唯一必要§3–7复用，采用仅模板捷径与extraction候选/assembly分验：naturalized100规则全0、方法次序反转而privilegedoracle仍1，但原300与100不同人口不把差额全授改写因果。Qwen2.5-7B/T0/BF16/SDPA、54source records/lexical自动metric非真实来源审计，零unsupported可只是少答，硬件口径不补造性能。全部抽取/repair/组装与独立语义费保留，6分差额深入，Ch76 11198后/25827前两段真实保存，root§76PRE/§77POST通过，详N34。

### [TabPFN Causal Analysis](https://arxiv.org/abs/2606.12917v1)

root§68唯一必要§2–4/A/G/B1–3复用：两合成regression任务中低entropy不授head必要，cleanpatch恢复与zeroablation不同，unsigned变化可实际负恢复。单任务L0均值差steering/valα/null不推全部hooksite或ICL永无共享方向；default1000split与1024steer人口分开，全部patch/feature/head扫描/val/test费保留。Ch5 08292/04119/08348/22600/20834完整正文已具体分开读出/必要/恢复与功能迁移，6分标准完成/NC、root§76通过，详N35。

### [LaME](https://arxiv.org/abs/2606.13061v1)

实际§3.2–3.4/4.1–4.2/4.4/Limits/T4–6/A/B2–3/C读足：指定latent子集受answerdecoder/contrastive辅助监督，末embed仍可读原input，K8为单forward非八轮推理。固定维数及无通道假设的Kdlog(1+SNR)不授信息界或hardbottleneck，理论精确不采；vision解冻/文字表口径差不补recipe。双头直接训63.3逊baseline63.8、暖启full64.4，K/decoder容量非单调；1.5531M/额外标签decoder与全训练编码费计，无硬件绑定60×不采。6分独立接口差额深入，Ch23 13710后/20674前两段真实保存，root§80PRE/§81POST通过，详N36，未核实现/复现。

### [PRISMR](https://arxiv.org/abs/2606.12942v1)

root§74唯一必要§3/4/6/A/B/C复用：candidate经hypernet生实例adapter，schema parse与ranking质量分验，跨domain parse100仍可质量反退。β=(ΣBiAi)/N只是和的非零缩放，不能由每项rank≤r推和rank≤r；该错误子命题精确不采，不据它认可容量保证。A仅B零初始化，不误作双因子同时零。单B200/b1/5products与0.58Bhypernet构造/安装不授零费用或完整SLO。Ch30 05903输入条件hypernet与03314条件adapter资产、Ch76 schema/value分验完整正文已承载独立有效接口；原7分深入/具体NC，root§84通过，详N37，无Book改动。

### [EPM-JEPA](https://arxiv.org/abs/2606.12979v1)

root§75唯一必要§3–6复用：MovingMNIST单gravityshift/GTX1050TiFP32/3seed，C−B4.74%落预声明±5%null带，不是统计等效或operator普遍无益。buffer/EMA联合freeze不识别三独立机制，热截短baseline可能高估C，不能消除LoRA transient。完整目标/经验编码与训练费保留。Ch25 07083 movingtarget、2506.23468条件memory、目标梯度/参数consumer分责及Ch28 replay完整论证已覆盖有限命题；6分标准完成/NC，root§84通过，详N38。

### [Emo-LiPO](https://arxiv.org/abs/2606.13006v1)

root§78唯一必要§3–6/2.3复用：同transcript/同emotion内按接近target强度排序，并非跨prompt统一强度尺度；成熟listwise方法不当新创，Eq6线性loss未闭不抄recipe。CosyVoice300M合成筛选后人口、Whisper/MOS/emotion2vec proxy非独立感知真值，Full仍有WER/EmoSIM/UTMOS反退；不补hardware/precision或普遍显著性，合成/人审/训练与语义回归全计。Ch34 08037冻结同prompt信号/非传递回退、01436列表质量序与26491真实质量分责已覆盖；6分标准完成/NC，root§88通过，详N40。

### [ASR and Diarization](https://arxiv.org/abs/2606.13095v1)

root§79唯一必要§2–5复用：content/speaker监督粒度分责，segmentlength权重及高loss mask改变训练人口，不认证重叠错误全部因果；缩speakerbranch75%不是全部输入减75%。Qwen2.5-0.5B、多encoder/LoRA/4000h+212h、真实转写切段限定适用域；去speaker可CER更好而cpCER更差，失败剔除与不同chunk协议不拼公平质量。hardware/precision/完整耗时未披露，全部对齐/训练/编码回归费保留。Ch23 DM-ASR22467、28711字段权重与25404粒度/删除分责已覆盖；6分标准完成/NC，root§88通过，详N41。

### [WISE](https://arxiv.org/abs/2606.12852v1)

实际§3.1–3.2/4.1/4.4–4.5/T3/A2–3/A5–7读足：当前观察和derived语义memory可提示尚未完成目标的机会式抢占换序，而非必须等subgoal完成。Wiki/VLM关系不是已证因果或动作授权；异步图不提供20ms freshness，position/λ/API/GPU口径不闭不抄recipe。50episode/成功人口步数与多模块组合反侧分账，知识制备/VLM/graph/重规划全部计费。6分具体差额深入，Ch79 ValuePlanner27699后两段真实保存，root§87PRE/§89实际POST通过，详N39，未核实机/复现。

### [E-commerce Agent Memory Study](https://arxiv.org/abs/2606.12924v1)

实际§3/4/5.1/T2/5.5/T7/7读足：固定2011初始profile不冻结自适应buyer逐轮query或liveAPI结果，小0.01–.10同向差额不授architecture唯一因果/普遍memory排序；judge过程与结果偏好人口分开，600对照不能当全2011。模拟click/cart非真实购买，35%latency缺完整配置/绝对值/尾延迟不作SLO。所有buyer/摘要/API/判分/独立评价计费。Ch77原序证据/派生memory三段与Ch66 TRACE11678 freshtrajectory/rescore分责已具体承载采用域；6分标准完成/NC，root§96通过，详N42，不扩未采用修复流程。

### [FCGraft](https://arxiv.org/abs/2606.13097v1)

root§82唯一必要复用：用于函数接口生成的signature KV资产与实际implementation执行分责，跨cache位置/任意独立拼接的exactness未采用，patch suffix不改变旧KV自身历史。环境/path/权重与版本绑定，CSIM不是语义安全；构造/安装/全部工具执行及独立回归费不隐去，14B precision未披露不补。Ch78 Description完整段后、21827前两段真实保存，6分具体差额深入，root§97PRE/§98实际POST通过，详N43，不授函数组合永无错或SLO。

### [PolyFlow](https://arxiv.org/abs/2606.13400v1)

root§83唯一必要§3–6/C/D/E复用：固定已知凸支持、可行初点和定义良好rayboundary下，用γ凸组合限制离散更新；仅理想精确计算可行，不保证分布质量或真实rollout安全。零方向/退化/precision guard未闭不补recipe，Gym仍违规，HalfCheetah mismatch5.256逊Flow，batch200整批时间不当单trajectory。LP/约束/每步求交及controller回归全计。Ch24 CBF21429后/VJPfree14157前两段真实保存，6分安全差额深入，root§97PRE/§98实际POST通过，详N44。

### [STG](https://arxiv.org/abs/2606.12983v1)

实际§2.1/3.1/3.2.1–3.3/5.1–5.4/T3–7读足：可信gold不保证harness比较同逻辑时刻，旧benchmark刺激/checker同edge race需分开驱动、状态推进与observationphase。主156general与15stateFSMtoy不混，silver仍模型提出的可错实现，高coverage/PASS非全部正确。全部结果用作者手修bench，不能继承原成绩；Xeon单core与GB200/五轮LLM、SFT16H100和功率估算不授纯机制720×或metered能耗。6分具体正确性差额深入，Ch66 23443后/07001前两段真实保存，root§99PRE/§100实际POST通过，详N45，未核代码/硬件复现。

### [AuthorityBench](https://arxiv.org/abs/2606.13104v1)

root§85唯一必要§3–6/Limits复用：110282claim/220564带citationprompt/40template有限分离claim真假与citationcue；FEVER真citation为backfill不entailment。人类1500κ.83不是无检索judge准确率，full/15K/拒答人口与Table4/5 lift不闭，不采用精确headline或引用普遍有害。GPU50GB未具名/precision/API全费未披露不补，构造/真citation核对与评价全计。Ch66 15456/17417内容保持/声望cue、引用存在vs支持和11509三轴分验已具体承载有限采用域；6分标准完成/NC，root§102通过，详N47。

### [CARVE VideoRAG](https://arxiv.org/abs/2606.13141v1)

实际§3–5/6.1–6.2/T1–5/A1/D开篇+D1/D3/D4读足：每120s片段的四种representation各召回，保(chunkID,configtag)，只重排实际召回该chunk的view，再以winner同view交generator；max不授跨模态校准/全四最优。216第一视角视频、2100单证据QA/300test经query-only/非证据top10过滤不证明全域唯一支持；人审/judge600/577人口及可见label不授独立gold。8H200141GB/CUDA13/默认8B/512tokens，precision未披露，在线平均排caption/index离线费、四索引与全部评价计。Ch76 2506.22900后/04962前两段真实保存，6分具体交接差额深入，root§101PRE/§103实际POST通过，详N46，未核pixels/code/复现。

### [BlockAttnRes Causal Analysis](https://arxiv.org/abs/2606.13168v1)

root§86唯一必要§2–7/A–C复用：两0.6B/200合成prompt，wrapper不保vanilla输出、currentmass由source长度可解析；maskrenorm只保权重和，不保表示norm/信息。正确末tokenmass与全部ablation人口不同，routing描述量不等局部任务依赖，低drop不证无信息或可安全prune。全部wrapper/干预/选层与独立任务费计，hardware/precisionND，不授普遍层功能。Ch5 24846/21258描述代理与真实干预、08348/22600必要/充分/迁移及13483重归一竞争已具体覆盖；6分标准完成/NC，root§102通过，详N49。

### [Reasoning as Pattern Matching](https://arxiv.org/abs/2606.13607v1)

root§95唯一必要§3.1–3.3/§5复用：模型行为/人类相关与不同Gemma机制分开，绝对ablation logit变化选head非只破坏正确的必要性。局部词替换patch不排除其他路径或证明所有reasoning=patternmatching，人类预测不授相同脑机制；pre-softmax entropy负值/未归一域不闭，子recipe精确不采，需corrected定义/可核artifact才重开。人口49/70/142与筛前8910不拼，hardware/precision/全部探测费ND不补。Ch5 27241 negativecontrol、30233/23091独立readout/行为与08348/13483局部必要/竞争分责已覆盖有限反侧；6分标准完成/NC，root§102通过，详N50，未核复现。

### [Biomedical Claim Verification Shortcuts](https://arxiv.org/abs/2606.12854v1)

root§93唯一必要§3–5/Limits/B/C/T8复用：SciFact实际输入goldrationale，NEI243/243空而SUP/REF非空，字段可分离标签；无内容盲/填NEI控制不证每次唯一走捷径，空goldrationale非世界无证据。等1008训练不控制domain/prior/label合同，双向OOD不支持严格单向/结构唯一因果；NF4/r16与T4/A100/API预算不授44.5×全费，全部制备训练回归计。Ch66 DSGym16344和23701已具体承载输入/label可见性、数据依赖负控制与人口分账，并非已逐字写NEI全空案例；该局部验证留报告。6分标准完成/NC，root§102通过，详N48，不扩临床路线。

### [CoDeR](https://arxiv.org/abs/2606.13204v1)

root§90唯一必要§3–6/Limits/B/G/H复用：两个独立bi-encoder分别提议topicalcoverage/negationcompatibility，Seq仅池内重排、Union另供候选；fallback只撤cutoff不撤兼容分。BGElarge/128token/NevIRExcluIR各800一epoch、十run不补未披露variance/hardwareprecision；recall85.85→81.7与V@1仍13.9、20query未具名generator不授完整安全。双encoder/索引/融合及独立支持核验全计。Ch76 09185第二段后/29464前两段真实保存，6分具体分工差额深入，root§104PRE/§106实际POST通过，详N52，不采零违例/硬谓词/授权或SLO。

### [OneRetrieval](https://arxiv.org/abs/2606.13533v1)

实际完整§3/4.1–4.6/T3–8/5读足：提前训练未绑定reservedsymbol的identityrouting，上线改dictionaryword→slot及SID→item外部绑定，数小时refresh、不改模型权重。不是无需训练或每个含词query保证route，组内代表选择/beam512/一对多每SID最多5item及60reserved容量保留。BARTbase/H800训4090serve、各stage数量/epoch/precisionND、synthetic2000OOV的IHR与IAR分账；IAR.553逊BM25.761、浅位/MRR可逊OneSearch，AA7/AB11day近全部替换未显著不作等效或零费。Ch76 13273第二段后/23388前两段真实保存，6分更新接口差额深入，root§104PRE/§106实际POST通过，详N51，未核真实上线/code/复现。

### [QueryMix](https://arxiv.org/abs/2606.13537v1)

root§91唯一必要§3–6/Limits/B复用：1484长query/35pair14lang、BGE-M3/8.8Mindex，query两语向量归一插值，100k子集先保全部qrels相关不作真实full人口。五ratio同dev挑max非heldout部署selector，ENindex在其他family也可正，不授Englishuniversalanchor/预训不平衡唯一因果；R@10升可伴nDCG退。翻译/两编码/选比/检索与回归全计，hardware/precision/tailND。Ch76 21543/20199/03136/19097与30612已具体承载语言/index/consumer分轴、recall/排名及oracle选比不越权，并非已逐字写该插值case；6分标准完成/有限NC，root§105通过，详N53。

### [RA-RFT](https://arxiv.org/abs/2606.13680v1)

root§94唯一必要§3–5/A/B复用：teacher结构相似judge标签非实际答对概率/因果效用，实际coarsetype裁候选；冻结retriever top1供rollout/update同条件，离线答案特权不搬上线。Qwen1.7/4B/64H100/16rollout/32768及BF16 retriever，policyprecision/独立seed/全部制备费ND；无context训练推理硬加43.3→37.7，random/普通检索亦逊无检，适配47.4只支持有限consumer×retriever关系。式3不采完整GRPO新证明，trace/judge/索引/context/训练回归全计。Ch76 19535/02091/22722/18734完整效用身份及consumer更新已承载；6分标准完成/NC，root§105通过，详N54，不授闭卷能力已写入weights或普遍收益。

### [ReSum](https://arxiv.org/abs/2606.13316v1)

root§92唯一必要§3–5/A/B复用：只在初始T条轨迹按同预算分支，循环J−1，非新分支递归；删除summary触发phrase或随机强插后重采continuation，不真实删旧KV/保证faithful压缩。零summary0/0、两组adv对不所属组参照/空组零variance与外生分支ratio未闭，不采用完整SGPO；理论只有gain≥−L√(δ/2)，不是不退保证。8H20/4096/trainT1eval.6，32/4采样非训练seed、等B非等tokens，去AP/常规GRPO反侧与全费保留，18.6%长度非净时延。Ch33 02178 boundedthinkingintervention、26352同prefix重采/非因果credit、09598有限suffix分支已覆盖唯一有限采用域；6分标准必要完成/有限接口NC，root§105通过，详N55。强算法/理论不用于正面证据或Books，精确重开见§5，未核code/复现。

### [Kimi Code CLI 0.14.1/0.14.2](https://www.kimi.com/code/docs/en/kimi-code-cli/changelog.html)

Jun12两release完整官方核心已读。厂商称shutdown取消active turns、默认stop backgroundtasks及修复overlap请求错activeagent，另有compaction展示/terminal能力guard等维护；两事件同家族1+2+1=4关闭。只采用这些版本正确性声明，不授代码已验、所有子进程回收或无泄漏/安全保证，故仅报告、Books无改；root§30独核通过，详A10。

54家族均已有证据限定的处置；31项整合的实际新增、完整两肩及本人真H2注均获唯一非writer POST，21项NC均有actualowner完整论证复核，不以题名或主题相似代替覆盖。MSA/M*/GF-DiT等与旧Jun12同精确v1去重，不重计本日；已读原件只保有限依赖核验。GF旧节号失配已具名交Jun12 writer/唯一reader窄修，不改旧候选日期/评分或重审旧63。

## 5. 缺口与下一步

可执行普通待办无；本六节格式、本地引用、限定diff检查及root唯一独立日级验收§107均已通过。来源筛选/五个准入决定点/Kimi校准均已完成，13400/12789一次timeout均已有限恢复，不列外部H。以下是本窗终态保留项，继续隔离，不用于正面证据、Books、无遗漏断言或性能/安全保证，仅在指定原件到达时定点重开。

日期保留：[DPOP2606.12505v1](https://arxiv.org/abs/2606.12505v1)有实际优化接口潜贡献，但唯一v1最早公告界与findable/registered最晚界跨Jun11–12；不列确定候选/评分/Books。可接受直接有日期官方v1公告/列表或原始正文，取得后仅重开该身份，不用created/Submitted冒称公开。

外部覆盖保留：Google Publications/Meta的Jun12历史日级目录当前不能恢复，有限Blog/混合search不补齐它们；等待有日期官方目录或具名原文，仅定点重开，不支撑正面证据、Books、无遗漏或零发布断言。

中心争议保留：A2D2 2606.13565v1的实际adaptive pathlaw/holding/endpointbridge与qualityweight不闭，7分深入受影响域后整项隔离、不用于正面结论或Books。重开需针对实际remask/delete与离散时间步的一致law/weight及Eq124–125桥接证明，或可核精确artifact；只改Eq17符号不足，详N24/root§58。

未采用子主张保留：ReSum13316完整SGPO分组/不所属组参照、空组零variance、零summary和外生分支采样权重，及不退理论，须可核精确实现/修正证明才定点重开；当前只有有限prefix干预接口NC，不支持强算法。PRISMR12942 fixedrank子命题须修正rank等式和实际hypernet执行路径；LaME13061信息界须补通道/噪声/约束及最终consumer可见域的成立证明；Pattern13607 entropy须明确pre/postsoftmax与定义域/实现；TimeROME12841 TopQ先后、Jeffrey13240符号、Emo13006线性loss等未闭recipe也仅在有精确更正/artifact时重开。它们不新增家族或整项H、不推翻各自有效独立接口/反侧，也不随整体验收变成已证定理或可执行配方；具体证据/边界分别见§4及对应N记录。

## 6. 复核

复核者：root（独立于报告作者supp_jun13）。[唯一canonical](../_sources/daily-20260613/SUP_REVIEW_20261026.md)§1–106已分批检查真实入口/停止范围、90完整AB/同精确DOI日证、排除与具名去重，31项真实POST、21项有限具体NC、Kimi低分关闭与A2D2整项中心H；原月入口形状已§42纠正并有限补导航，无新身份。§53实际核53current官方页短信号、PERIA窄方法/必要/真实POST§66通过；§105末三NC/§106末两实际POST已完成。所有拟入选家族的必要层、实际Book写入与有限处置均已独核；§107已实际读最终六节/来源收束并通过唯一完整日级验收，当前仅行政同步该既成结果，不新增研究或验收层。

排除复核范围：90份完整AB中的18项具体贡献前N、18项旧同精确v1去重和12505跨日日期，均已在分批准入/reconciliation独核中处理；未把1274导航人口的剩余标题或CL整月另页称作已读题摘/全量排除。官方非论文入口按实际日期邻段、具名核心N与有限查询检查，外部目录限制仍隔离。

本地验证：`python3 scripts/validate_research.py --report papers/2026/06/13/README.md`通过V3；54候选表行与54证据小标题对应、本地引用无缺失；31整合在15个Book文件均有正文marker和真正H2 Review notes本人注。报告、本日_sources与这些Book路径限定`git diff --check`通过，未stage/unstage/commit/push，不更State/共享索引，未把已有staged或并发修改归为本轮产物。机器检查不替代上述真实语义层。

结论：通过

root唯一完整日级验收§107；合同允许的安全终态，不授隔离项正面证据，不宣称全网无遗漏或所有强主张成立。
