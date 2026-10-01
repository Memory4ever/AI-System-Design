# Daily Research — 2026-04-10

**规范：** V3
**窗口：** 2026-04-09T09:00:00+08:00 ～ 2026-04-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T19:32:29+08:00

## 1. 结论

本日按当前合同重审。旧587个arXiv唯一身份只是日期过滤前的标题召回库存，不是本窗新论文数或候选分母；旧34/final27的日期与模板式准入不继承。可能改变主线判断的条目完成完整题摘语义筛选，再按真正贡献读取必要exact-v1证据；最终旧身份对账没有沿用高保留率或把全库存扩成全文队列。

本日冻结70个唯一当窗家族，均有自包含证据判断：34项实际整合且已通过实际正文的非作者核验、17项具体已有覆盖、15项受限仅报告、4项争议安全暂缓。日级独立复核通过，普通扫描、筛选、证据、Books与复核待办为0。完成表示已处理到合同允许的安全终态；§5具名日期、目录与中心争议保留项不支持正面采用或零遗漏断言。

关键认知增量包括：恢复/内容有效与跨步候选消费分责；低bit数值模拟、实际GEMM和发布artifact身份区分；动态steering工作视图与团队拓扑/权限不同；无害GUI元素仍可改变action grounding；删除有限样本影响与concept-wide目标不同。书稿采用具体条件分支，保留旧路径、代价和反证。PoST、CE谱界、DLR密度式与DualPool离散成本存在可复查中心争议，不被评分或benchmark宣传升级为知识保证。

旧全文无损保留于[原报告](../_sources/daily-20260410/V2_1_REPORT_ARCHIVE.md)，不代表当前结论。[作者checkpoint](../_sources/daily-20260410/V3_REVIEW_CHECKPOINT.md)、[题摘/证据记录](../_sources/daily-20260410/V3_SCREENING_NOTES.md)保存续跑位置。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/Research Index首屏只到近期、历史Load more未恢复；RSS定点命中[Axios供应链事故响应](https://openai.com/index/axios-developer-tool-compromise/)（2026-04-10T00:00Z），已读事故/证书撤销说明，属于成熟软件供应链处置而非新的大模型机制，前分母关闭 | 受阻 | 仅Research历史窗口目录缺口；需要可读分页或该窗官方研究快照。RSS实际当窗事件已处理，不代替Research，不宣称全源零命中 |
| SRC-ANTHROPIC | Research原始日期列，trustworthy-agents=2026-04-09T16:34:00Z落窗；已读官方核心及Ch72/78，对应model/harness/tools/environment分层和plan/action oversight为已有原则的产品实施叙述，没有新增可定位机制或独立评价边界，前分母关闭 | 已检查 | 不把官网论述冒称独立实验报告或未披露安全保证 |
| SRC-GOOGLE-AI | [Google Apr博客归档](https://research.google/blog/2026/04/)实际跨04/13→04/09 ConvApparel→04/08；[DeepMind Blog页3](https://deepmind.google/blog/page/3/)逐条April日期为30/27/23/22/15/14/02，无本窗项；[DeepMind Publications](https://deepmind.google/research/publications/)首屏04/22→03/22跨窗 | 受阻 | Google Research Publications仅年度条目未恢复本窗日期索引，需要本窗可读官方目录/历史快照；已查Blog/DeepMind不代替该缺口。ConvApparel博客独立事件仅日级日期、原论文EACL March2026，需截点前公开链和新增命题，不能倒灌首发 |
| SRC-META-AI | [Blog页1](https://ai.meta.com/blog/)和[页2](https://ai.meta.com/blog/?page=2)实际恢复，Apr08/06后Mar27停点，无Apr09/10目录项；Research空正文、Publications链接工具失败 | 受阻 | 仅Research/Publications历史本窗目录未恢复；重开需该目录可读快照或官方日期条目，不将Blog停点替代研究目录 |
| SRC-QWEN | [静态Research列表](https://qwen.ai/api/page_config?code=research.research-list)实际60条，最晚2025/12/23；[动态列表](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)实际40条，04/02T04:00+08→04/15T10:00+08跨窗无条目；两路拼接为官网Research目录 | 已检查 | 限官网公开目录，不外推未列作者稿 |
| SRC-DEEPSEEK | 官网研究June24→Feb25，新闻Apr24→Dec1跨窗 | 已检查 | 限公开目录，不外推未列作者稿 |
| SRC-MOONSHOT | Kimi Platform完整109行目录26项最新2025-11-07；MoonshotAI官方组织页恢复研究项目入口但未给历史公开日期 | 受阻 | 仅历史研究日期目录未恢复；需要该窗官方研究条目/快照。不把所有仓库commits扩成隐藏队列 |
| SRC-TENCENT-HUNYUAN | publicList page1,size100,renderType0返回9/9；04/30/04/23后02/13跨窗 | 已检查 | 限官网公开目录，不等全网无论文 |
| SRC-ZAI | Research目录04/29→04/07→04/01跨窗 | 已检查 | 无目录内缺口，不外推未列作者稿 |
| SRC-BYTEDANCE-SEED | 论文API页20/40跨Apr09→Apr08→Apr07→Mar31；blog type2页0/20跨Apr22→Apr8T16Z→Mar31。Nexus1657显示PublishDate=04/09T16Z，但ArticleID/UpdateTime为07/02且链接未版本PDF；官方2604.09258v1提交为04/10T12:17Z，不能证明截点前论文已公开 | 已检查 | 单家族Nexus日期隔离：需截点前可读正文artifact/官方历史发布链；不评分、不倒灌后出v1，也不称目录零事件 |
| SRC-BAIDU-ERNIE | Blog第1页04/15→02/06跨窗 | 已检查 | 限官网公开Blog |
| SRC-XIAOMI-MIMO | Paper八条June29→Mar13→Feb3跨窗 | 已检查 | 官网Paper目录有界检查结束；Blog补充入口未取得本窗历史时刻，不支持零更新断言。仅在可读本窗官方文章/发布链恢复后定点重开，不扩所有仓库历史 |
| SRC-MINIMAX | 英文May26→Mar18、中文Apr27→Mar18跨窗，Agent Tech llms.txt另试 | 已检查 | Agent Tech补充入口无本窗历史日期，不外推无更新 |
| SRC-ARXIV | 旧587原始唯一身份用于标题查漏，不当作当天新论文；主线潜在贡献完整题摘重判与必要exact-v1结束，旧retain最后14身份逐项对账；70工作家族及代表性排除理由有记录 | 已检查 | 官方公告slot/PID赋号、连续批界与自身早字段只共同支持明示08～09推断；7个晚字段family逐项隔离，旧09731/16469另保留窗外批次线索，不用submitted/DOI created或Updated单独定归属 |

## 3. 候选与判断

本表70个唯一当窗家族已完成贡献、日期、必要证据与日级非作者复核并冻结。公开区间为永久ID公告赋号、常规slot、连续批界与自身早字段共同支持的推断；submitted/Updated秒数不是公开动作。日期未确认的潜在贡献单项列入§5，不给零分、不伪称窗外，也不混入本表。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Valve](https://arxiv.org/pdf/2604.07874v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | channel暂停/quarantine/失效ID与框架重算形成可恢复控制点；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [AsyncTLS](https://arxiv.org/pdf/2604.07815v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 上轮coarse候选供当前fine selection，当前coarse预取下一步；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Cross-Tokenizer LLM Distillation through a Byte-Level Interface](https://arxiv.org/pdf/2604.07466v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | student训练期byte接口保留原token输出，监督与部署接口可分离但非无损迁移；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Lexical Tone is Hard to Quantize](https://arxiv.org/html/2604.07467v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | lexical tone承载词义，SSL可读不等量化保留，phone/residual接口需独立验收；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/html/2604.07666v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 有限重采样噪声下仍可学习，但同错误率的结构与checkpoint口径不同；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [PoST](https://arxiv.org/pdf/2604.07658v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 衰减谱与position stretch提出具体条件分支，但中心coherence界有可复查反例；2 + 1 + 2 = 5 | 争议 | 暂缓：Prop4.5与参数坐标需作者勘误，见§5 |
| [The Lifecycle of a Spectral Edge](https://arxiv.org/html/2604.07380v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | post-grok阶段的WD可改变线性可读性而较少改变受测行为，优化与probe验收分开；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Conservation Breaking and Spectral Compression](https://arxiv.org/pdf/2604.07405v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 连续守恒与离散二阶漂移的适用条件有价值，但中心CE曲率界已被具体GN反例否定；2 + 1 + 2 = 5 | 争议 | 暂缓：Theorem6 Eq7需勘误，不采曲率/τ保证 |
| [Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](https://arxiv.org/html/2604.07402v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 完整历史前向与局部loss/梯度窗口可分离，局部优化需补采样和表示一致性代价；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [CLEAR](https://arxiv.org/html/2604.07487v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 执行反馈训练独立context generator，executor冻结，参数owner与上下文有效性分开；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md) |
| [Label Leakage Attacks in Machine Unlearning: A Parameter and Inversion-Based Approach](https://arxiv.org/html/2604.07386v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 删除类别可识别与样本恢复目标不同，class-level ASR需比较实际多数基线；2 + 1 + 2 = 5 | 深入完成 | 仅报告：受限分类删除意图泄漏，不外推LLM隐私或统一攻击有效性 |
| [Score Shocks](https://arxiv.org/html/2604.07404v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | score误差在mode边界局部放大，平均误差与轨迹敏感性分账；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [GIRL](https://arxiv.org/html/2604.07426v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | latent grounding与自适应posterior KL形成受限分支，软惩罚非硬安全约束；2 + 2 + 2 = 6 | 标准完成 | 仅报告：有限MetaWorld实现，中心理论保证另隔离 |
| [Dual-Layer Reasoning](https://arxiv.org/pdf/2604.07518v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 投影高斯采样与claimed IS密度比不一致；2 + 2 + 2 = 6 | 争议 | 暂缓：Eq6/10与Appendix B的密度/近似说明需勘误 |
| [TrustDesc](https://arxiv.org/html/2604.07536v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 源码feature与entry参数传播不同，声明需核真实可达路径及运行任务；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [FESTS](https://arxiv.org/html/2604.07592v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 显式变量跨帧绑定同一对象，形式匹配与原始感知真值分账；2 + 1 + 2 = 5 | 标准完成 | 仅报告：人工日志/有限模板，不证明端到端感知与解释因果收益 |
| [FILCO](https://arxiv.org/pdf/2604.07523v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 预连线计算/存储原子通过逻辑视图和调度组合，配置变化不同于物理重布线；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [SAGE](https://arxiv.org/pdf/2604.07663v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | embedding保留完整momentum、column尺度有界阻尼，减少第二状态不等于减少全部状态；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [From LLM to Silicon](https://arxiv.org/html/2604.07526v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 联合架构/放置的分析PPA与实芯片测量、同workload对照不同；2 + 2 + 1 = 5 | 标准完成 | 仅报告：分析模拟设计点，不改变生产ASIC或Serving保证 |
| [Learning Is Forgetting](https://arxiv.org/html/2604.07569v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | latent熵/跨模型相关性代理不能证明信息瓶颈最优或因果泛化；2 + 1 + 2 = 5 | 标准完成 | 仅报告：有限表征压缩测量，无稳定更新/停止准则 |
| [VSAS-Bench](https://arxiv.org/html/2604.07634v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 独立墙钟与carry-forward改变streaming测量对象，consistency不能脱离更新频率；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Behavioral Dependence and Induced Bias in LLM Judges](https://arxiv.org/pdf/2604.07650v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 同群经验difficulty可诱发条件依赖，重权观察与独立性保证分账；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受限行为诊断；独立性/sign-flip中心保证另隔离 |
| [SubSearch](https://arxiv.org/pdf/2604.07415v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | outcome成功时关闭process代理、格式奖励独立，代理有效性随任务改变；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [ConsistRM](https://arxiv.org/pdf/2604.07484v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | pair历史pseudo-label改变下一轮target，时间一致不获得truth authority；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Benchmark Shadows](https://arxiv.org/html/2604.07363v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | data coverage、重复与谱代理并非同一对象，谱变化不自动证明泛化；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受限谱诊断与去重案例，不采普遍因果判断 |
| [Flux Attention](https://arxiv.org/html/2604.07394v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | prefill决定逐层full/sparse路线，decode消费其KV身份；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [SHIELD](https://arxiv.org/pdf/2604.07396v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 生命周期与bit敏感性共同决定eDRAM刷新，而非全部缓存同待遇；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [RefineRAG](https://arxiv.org/pdf/2604.07403v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 词级检索优化可保留目标错误语义，retrieval与answer成功须分账；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GameWorld](https://arxiv.org/html/2604.07429v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | action interface/暂停协议/可验证状态改变Agent评价对象；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [HY-Embodied-0.5](https://arxiv.org/html/2604.07430v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | modality专属QKV/FFN、共享表示与分阶段目标需要独立容量/质量验收；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Scalable Joint Resource Allocation](https://arxiv.org/html/2604.07472v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | model/tier/TP/PP联合可行性先于计划排序，模拟SLO非线上保证；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Reasoning Graphs](https://arxiv.org/pdf/2604.07595v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | evidence identity关联历史评价与决策，reuse需确认当前适用性；2 + 2 + 2 = 6 | 标准完成 | 仅报告：exact-v1无实验结果，不继承较晚ROZA摘要数字 |
| [Blink](https://arxiv.org/pdf/2604.07609v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | host/DPU/GPU重新分担请求入口、scheduler和KV状态；2 + 3 + 2 = 7 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [DIVERSED](https://arxiv.org/html/2604.07622v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | ensemble verifier保持混合ν而非target p，需要另立分布/质量合同；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Guardian-as-an-Advisor](https://arxiv.org/pdf/2604.07655v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | advisory risk/context不等强制gate，降低过拒也需独立安全裁决；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Conformal Social Choice](https://arxiv.org/html/2604.07667v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | marginal set coverage与singleton/adaptive-stop安全保证不同；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MIPT](https://arxiv.org/pdf/2604.07716v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | phase gate与有限memory实验不能证明通用critical capacity/常数cache保证；2 + 2 + 2 = 6 | 标准完成 | 仅报告：以实际PDF v1为准，不继承后版Fan Duality描述 |
| [TrajGuard](https://arxiv.org/html/2604.07727v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | rolling trajectory风险与累计控制状态不同，reset不能追回泄漏；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Symbiotic-MoE](https://arxiv.org/html/2604.07753v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 模态expert隔离/共享和梯度释放共同决定容量交换；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [ACIArena](https://arxiv.org/html/2604.07775v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | topology不能单独解释跨Agent攻击传播，role与interaction须联合测；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ORACLE-SWE](https://arxiv.org/html/2604.07789v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | oracle信息注入测上界，实际提取与end-to-end发布须另测；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GRASS](https://arxiv.org/html/2604.07808v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 周期选择原参数层与低秩更新不同，全层optimizer历史不因GPU驻留减少而消失；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [PolicyLong](https://arxiv.org/html/2604.07809v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 当前checkpoint熵用于选择support和拟distractor，筛选长度不等训练依赖验证；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [LogAct](https://arxiv.org/html/2604.07988v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | shared log持久意图与voter/decider/driver分责，外部effect恢复不能只靠日志；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [LegoDiffusion](https://arxiv.org/html/2604.08123v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | deferred节点启动与消费依赖分离，跨workflow组批要维护请求状态；2 + 3 + 2 = 7 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Alloc-MoE](https://arxiv.org/html/2604.08133v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | layer校准计划与token floor/global budget分配是两个控制层；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md) |
| [DMax](https://arxiv.org/html/2604.08302v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | current rollout corruption与soft token-MASK状态改变可修订生成和commit条件；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Loop, Think, & Generalize](https://arxiv.org/html/2604.07822v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 训练loop curriculum与推理halting分责，KL/entropy不能签发correctness；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-DECODER-ONLY [Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Hidden Biases in Conditioning Autoregressive Models](https://arxiv.org/html/2604.07855v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | finite validator仍需model-state/future acceptance mass可计算条件；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Bit-by-Bit](https://arxiv.org/html/2604.07888v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 渐进QAT/OCS/shared anchor仍需逐格式质量与执行验收；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Robust Length Prediction](https://arxiv.org/html/2604.07931v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 单次未来length与重复采样median监督是不同对象，尾部预算不能用MAE代替；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [ResComp](https://arxiv.org/html/2604.07955v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 固定原始FP目标与当前补偿权重目标不同，残差包含本层校准漂移；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [PEARL](https://arxiv.org/html/2604.08065v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 专家工具轨迹只作训练期表示目标，部署无预测token/工具/latentAR；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [CausalVAE World Models](https://arxiv.org/html/2604.07712v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | staged latent/transition训练与gate改变counterfactual目标，局部Jacobian不是真实因果图；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受限状态标注/目标组合未分离通用因果可靠性 |
| [DAHS / BHA](https://arxiv.org/html/2604.07747v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | teacher提示分布与逐步撤除改变suffix监督，训练step相同不等总teacher预算；2 + 2 + 2 = 6 | 标准完成 | 仅报告：能力覆盖/预算对照不足稳定采用，保留有限实现 |
| [The Art of (Mis)alignment](https://arxiv.org/html/2604.07754v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | repair顺序/方法异质性与utility回归不支持安全无损逆操作；2 + 2 + 2 = 6 | 深入完成 | 仅报告：受限模型/judge与非等tuning预算，不给普遍修复排序 |
| [Influence-Based Code Data Selection](https://arxiv.org/html/2604.07769v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | checkpoint与验证目标改变样本influence排序，选择用validation不是独立held-out；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Structured Distillation of Web Agent Capabilities](https://arxiv.org/html/2604.07776v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | teacher思考预算/版本与成功排序反转，不等teacher越强轨迹越可教；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [SEARL](https://arxiv.org/html/2604.07791v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 跨context按工具锚点组优势，名称相似不保证条件状态等价；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受限tool-memory/reward组合，不采用统一条件优势保证 |
| [Semantic-level UI Element Injection](https://arxiv.org/html/2604.07831v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 无害图标仍可误导grounding，内容安全与可执行目标identity分开；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Contextual Representation Ablation](https://arxiv.org/html/2604.07835v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 白盒推理时动态mask能绕拒答，coordinate mask不证明解耦安全子空间；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MESA](https://arxiv.org/html/2604.07914v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | EOS/长度与视觉steering纠缠，top-m KL不保持完整条件概率；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受限hallucination/recall诊断，不采用通用解耦保证 |
| [Unlearning or Untraining](https://arxiv.org/html/2604.07962v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 有限S训练影响删除与concept-wide S_full参考分布不是同一目标；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GuarantRAG](https://arxiv.org/html/2604.08046v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | document偏好与sentence方向注入不获得claim-support commit权；2 + 2 + 2 = 6 | 标准完成 | 仅报告：联合训练/解码的质量与总成本归因有限，不采用保证 |
| [OA-EM Codebook Optimization](https://arxiv.org/html/2604.08118v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | centroids更新与固定码本assignment是不同自由度，PPL/下游/执行成本分账；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [QaRL](https://arxiv.org/html/2604.07853v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | fake quant数值模拟与实际低bit训练GEMM不同，materialized权重发布需冻结数值身份；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Dual-Pool Token-Budget Routing](https://arxiv.org/html/2604.08075v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 独立池的离散fleet成本不能用去ceil连续近似签发always-help保证；2 + 2 + 2 = 6 | 争议 | 暂缓：Eq6/7的离散成本与lower-bound保证不一致，需勘误 |
| [Plan-RewardBench](https://arxiv.org/html/2604.08178v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | 轨迹偏好需保留关键违规与约束更新，长benign prefix不抵消末端失败；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Dynamic Attentional Context Scoping](https://arxiv.org/pdf/2604.07911v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | registry/focus在steering时切换工作视图，与拓扑、权限隔离不同；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [ATLAS](https://arxiv.org/pdf/2604.08044v1) | 2026-04-10T08:00:00+08:00 ～ 2026-04-10T09:00:00+08:00 | channel/row locality、MC面积、compute与thermal需要同一预算选择；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |

## 4. 证据与知识整合

### [Valve](https://arxiv.org/pdf/2604.07874v1)

Source Family：`SF-2026-ARXIV-2604-07874`；exact-v1 §4–5。长prefill无法等到operator/iteration边界时，channel暂停、quarantine、失效ID和框架重算共同完成移交；无fault不等KV内容有效，仍依赖driver/硬件路径和恢复合同。冷却/压力反馈限披露条件，摘要与正文不一致的fleet精确数字不采用。Ch56原operator-preemption之后已实际写入更细暂停与内容有效分账；root官方PDF与实际正文独立通过，见[写后复核](../_sources/daily-20260410/V3_WRITEBACK_INDEPENDENT_AUDIT.md)。未复现实验，不是生产保证。

### [AsyncTLS](https://arxiv.org/pdf/2604.07815v1)

Source Family：`SF-2026-ARXIV-2604-07815`；exact-v1 §4–5。跨步coarse/fine流水线改变候选消费时点，不恢复dense attention等价。block size64、128 blocks与作者任务/batch容量混杂限制收益；fallback/漂移检测是书稿设计建议，非已测作者控制器。Ch22 selector-reuse之后已实际加入消费/预取及近似、容量边界；root必要原文和写后对读通过，见同一[记录](../_sources/daily-20260410/V3_WRITEBACK_INDEPENDENT_AUDIT.md)。未运行实现或复现实验。

### [Cross-Tokenizer LLM Distillation through a Byte-Level Interface](https://arxiv.org/pdf/2604.07466v1)

Source Family：`SF-2026-ARXIV-2604-07466`；exact PDF v1 §3.1–3.2/4/5、Tables1–3。teacher token coverings形成byte条件概率，实际有界近似；student以token prefix+byte位置的十个并行heads预测，不是byte-AR，超过十bytes只监督前十。byte KL/CE与原token CE连接辅助接口和原head，训练后可卸载；统一坐标不保证能力无损，IFEval退化、BPE→byte整体下降与任务排序反转均保留。Ch29原跨tokenizer概率投影小节缺这一训练/部署接口分支，已在该节末落实两段与Review notes；root独立必要源/写后通过，见同一复核记录。6分因确认知识缺口深入，未复现实验。

### [Lexical Tone is Hard to Quantize](https://arxiv.org/html/2604.07467v1)

Source Family：`SF-2026-ARXIV-2604-07467`；exact HTML v1 §2–4。冻结HuBERT/data，量化前后对元音phone/tone作probe；tone可承载词义，不能默认归为可丢的声学风格。phone粗聚类→逐帧残差码本有条件改善，但mean pooling/RVQ/residual并非处处同益或等bitrate；probe读中心vectors，不是直接integer或端到端生成。Mandarin170h/400speakers、Yorùbá93h/单speaker、MFA对齐、非sandhi/非全部prosody界限保留。Ch23 semantic/acoustic分责后已实际写入tone内容保持的反例与代价，root必要原文/写后通过。5分因具体反例深入，未复现实验。

### [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/html/2604.07666v1)

Source Family：`SF-2026-ARXIV-2604-07666`；exact HTML v1 §3–5/6.3、Table1与Limitations。作者在G×T测试矩阵上分别随机翻转cell、row、column或整个group，每次重新采样，不代表固定且可被policy利用的偏差。MBPP以374训练/90验证题、每题三tests测pass-rate；Qwen3-8B/GLM4-9B的主要配置每run约64 H100 GPU-hours，response上限8192，其他部署batch、并发、precision/SLO未披露。有限噪声下能学习是受限反例，不是通用15%阈值；Table1同p不同结构有差异，best与final必须分开，正文部分叙述混用最高点时不照录。模型verifier的precision与accuracy共同变化，没有独立证明precision应普遍优先recall。Ch33原有相关误差/可利用trigger之外，已实际加入重新采样与固定偏差的对照、独立测试合同及checkpoint分账。apr03必要原文与实际正文写后对读支持这一窄结论；未复现实验，三tests通过不等于完整程序语义正确。6分因修正重要既有判断深入，AI-for-Science实验不作为本项目贡献主体。

### [PoST](https://arxiv.org/pdf/2604.07658v1)

Source Family：`SF-2026-ARXIV-2604-07658`；exact PDF v1 §2.2、§4.2–4.4、§5–6/Limitations。排序重参数化与position stretch是可核的衰减状态设计分支，但第12页Prop4.5宣称的coherence全局界不成立：取其允许的θ=1、softplus(c)=1、δ均为c，得到p=(1,2,3)，μ23=2√6/5≈0.9798大于其界μ12=2√2/3≈0.9428。§2.2的p=-log(w)、§4.4累积正gap与Algorithm1的d=-exp(p)也未充分统一，不能把理论谱直接当作实际算子的保证。stretch依赖指定谱/信息分配条件，§5.2增O(LN)操作不等零时间；GLA64K、RWKV平均退步与180/440M、4–9Btoken局部实验保留。root独立确认公式与最小反例，暂缓Books，不写minimax、无开销或任意递归模型无损保证；已读方法证据保留，不用降分删除争议。

### [The Lifecycle of a Spectral Edge](https://arxiv.org/html/2604.07380v1)

Source Family：`SF-2026-ARXIV-2604-07380`；exact HTML v1 §2–6/9/10.4、Table1–2。作者在150K两层Dyck与1.5M六层SCAN、三seed受控实验中，以W=5 attention参数更新作SVD。Table1从同一post-grok checkpoint将WD从1降至0，受测准确率变化较小而线性probe R²恢复；非线性probe仍能读出，压缩/不易线性读出不能直接写成知识删除。小ε扰动不等于移除整个投影，随机2D对照只匹配维数、未匹配范数，不能据此证明平坦方向完全无用或alignment导致grokking。Ch28 Weight Decay全局交互段后已窄幅加入任务能力与表示可读性分账、原已验证schedule共存和probe成本；root必要原文/实际正文写后独立通过。5分因具体知识缺口深入，未复现实验，不给前沿LLM通用WD schedule。

### [Conservation Breaking and Spectral Compression](https://arxiv.org/pdf/2604.07405v1)

Source Family：`SF-2026-ARXIV-2604-07405`；exact PDF v1 §2–4、第5页Theorem6 Eq7。无bias同质ReLU的相邻重缩放与连续梯度流守恒、离散步长二阶漂移恒等式只在声明假设内成立。中心CE谱上界则有直接反例：二分类p=(.9,.1)时S=diag(p)−ppᵀ=.09[[1,−1],[−1,1]]，最大特征值.18而非作者采用的max p(1−p)=.09；n=1、J=I即可违反其GN界。GN近似也不能自动升级为一般非线性参数Hessian。root独立核原式及反例，保留5分争议深入、暂缓Books；不因此否定窄同质守恒，但不能把错误中心界支撑的普遍CE曲率压缩或τ保证写入书稿。重开只需该定理勘误及与真正Hessian/评价的连接，不开展无关版本比较。

### [Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](https://arxiv.org/html/2604.07402v1)

Source Family：`SF-2026-ARXIV-2604-07402`；exact-v1 §4–6与AppD/E，PDF身份与必要机制已核。LocalOpt保留完整prefix前向，只在重叠局部窗口计算loss并对历史representation stop-gradient；不是裁掉模型条件上下文。LocalOpt单独在作者OmniTokenizer视频配置中明显退步，首窗口采样重平衡和邻表示regularizer补偿有限质量损失；两块局部loss与五块完整训练的工作量并非同一合同。作者110/343M、17帧256²、四A100、300epochs，batch96/40、lr1e-4、γ=.01、λ=.1；部署并发/precision/SLO未披露。邻状态距离不是完整Jacobian或全局Lipschitz，不能采用普遍稳定保证或含糊速度headline。Ch24 Training/Inference mismatch之后已实际加入完整前向/局部反传、采样与过平滑成本及完整训练旧路径；root必要原文/实际正文独立通过。6分因具体知识缺口深入，未复现实验。

### [CLEAR](https://arxiv.org/html/2604.07487v1)

Source Family：`SF-2026-ARXIV-2604-07487`；exact-v1 §4–5及AppA/B/D/E。对同题六条执行轨迹作对比反思，训练独立CAM生成上下文，再由冻结executor反馈进行SFT+GRPO；更新的是context generator参数，不是Agent executor或外部事实权。作者以Qwen3-32B CAM、ClaudeSonnet4/DeepSeekV3.1执行器、AppWorld TestN三次运行测TGC/SGC；实际部署precision、并发/SLO未披露。SFT/完整方法有对照但缺RL-only完整全因子，六rollout、generator和8×B200训练成本不可当等预算免费改进，oracle pass@3与平均完成率分开。新context不自动有事实或授权效力，executor/interface变更需重新验收。Ch75 assembly pipeline末已实际加入生成器训练owner及旧固定context/RAG共存边界，root原文/写后独立通过。6分因知识缺口深入，不声称可替代所有Memory或已复现。

### [Label Leakage Attacks in Machine Unlearning: A Parameter and Inversion-Based Approach](https://arxiv.org/html/2604.07386v1)

Source Family：`SF-2026-ARXIV-2604-07386`；exact-v1 §III–VI、Eq12及TableV–VIII。作者以LeNet/ResNet18、MNIST/FashionMNIST/SVHN/CIFAR10的十类分类任务识别被删除类别，白盒依赖参数/辅助head与同feature坐标，黑盒依赖完整概率向量、已知label space及梯度反演代理；不是秘密训练样本恢复或开放LLM接口。Eq12按全部十类计算forgot/retained二元accuracy，因此忘一/三类时always-retained基线为90%/70%，文中统一50%不合这一分母；单类黑盒77.75%不能证明超过多数基线，白盒98%信号也不因此被全部否定。白化共同协方差/类正交的理论前提不推出一般深网；反演忘超过四/七类时失效。root独立确认这些目标、分母和失败条件。Ch72可见通道原则不是该方法的同义完整覆盖，本项保留为受限报告而不伪称已有覆盖，不以作者ASRheadline新增通用隐私保证。5分安全深入，未复现实验。

### [Score Shocks](https://arxiv.org/html/2604.07404v1)

Source Family：`SF-2026-ARXIV-2604-07404`；exact-v1 §4、§5.4、§6.1–6.3/7.1/11.2–11.3。正smooth heat density的score/Burgers对应与binary分解的tanh恒等式成立；有限噪声非真正jump。对称两高斯mode边界中心轨迹的reverse-time增长率`(a²−σ²)/σ⁴`只在指定低噪声条件为正，τ是噪声方差的一半；局部轨迹/Grönwall界不证明全部样本或神经score网络的全局稳定性。§11调步/诊断建议没有trained模型NFE/质量或Serving验证，多峰交汇与随机情形仍有限制。Ch24原离散DDPM段之后已实际加入局部几何敏感性、固定schedule共存和诊断成本；root原文/实际正文独立通过。5分知识缺口深入，未复现实验。

### [GIRL](https://arxiv.org/html/2604.07426v1)

Source Family：`SF-2026-ARXIV-2604-07426`；exact PDF v1 §2–5/7。冻结DINOv2 ViT-B/14后用128维Ψ对齐预测与真实配对观察，预测ĉ仍非环境observation；posterior KL的δ依赖ensemble信息/损失代理，clipped β是软约束而非物理fail-closed。18项MetaWorld、十seed支持受限full/no-grounding/fixed-β差异，但VAE/DINO容量等变量不同；312→406ms约30%增加，蒸馏328ms也非免费收益。strong-duality未给足NN可行域条件，Theorem3.3的`(1−γ)^−2`与intro更强保证须分开；范数界未自动证明value test function属于指定函数类。root支持实现仅报告、中心保证争议隔离，不用争议结论支持Books，不把已有grounding主题伪称完整覆盖。

### [Dual-Layer Reasoning](https://arxiv.org/pdf/2604.07518v1)

Source Family：`SF-2026-ARXIV-2604-07518`；官方PDF v1第5页Eq6/10、§3–5/Appendix B。premise→连续visual evidence→rationale的双owner实现可核，但高斯向量归一后的球面密度须积分半径。二维σ=1、μold=(1,0)、μnew=(0,1)、z=(1,0)时，真正ratio为`I(0)/I(1)=.2233612748`，`I(a)=∫₀∞r exp(−r²/2+ar)dr`；Eq10给`e^(−1)=.3678794412`。Appendix B明确写近似logπ，争议针对Eq10等号与准确IS保证缺少surrogate误差桥，不否定全部近似训练。SigLIP attention不是ground-truth oracle，Qwen3-VL8B四图像基准、greedy pass1/部分2048长度及缺等预算限制保留。root独立核原式与反例，6分纠错深入、暂缓Books，不采用无偏/严格trust-region保证。

### [TrustDesc](https://arxiv.org/html/2604.07536v1)

Source Family：`SF-2026-ARXIV-2604-07536`；exact-v1 §4.1–4.3/§5–6。描述从entry/callsite参数传播取证，库有feature不证明对外可达；LLM debloat非静态soundness且library不展开。声明经可执行任务/logs与LLM judge修订，不能验证或运行失败的声明移除；合成任务通过不证明远端诚实或完整语义。52tools/12MCP servers、208生成任务排除部分remote/paid路径；adaptive十五轮选择率44.7–67.4%且无递增不等于零攻击，显式防御是假设。运行验证占主要成本，runtime仅共同成功任务。Ch78 ToolContract之后已实际加入entry能力/运行验证/权限分责与人工contract fallback；root必要原文/写后独立通过。6分安全/知识缺口深入，未复现实验。

### [FESTS](https://arxiv.org/html/2604.07592v1)

Source Family：`SF-2026-ARXIV-2604-07592`；exact-v1 §3–6。∃变量绑定同一object跨帧，不等于每帧分别存在任意car；formal matcher对预标注perception log生成query/match/explanation监督，不是原图感知真值。180scenes、每场126frames、七sensors、十五人工templates、27Koutputs及单Qwen2.5-3B限制覆盖；NL→SpRE自动翻译尚缺。C1无解释SFT与C2增加PPO/解释reward混合，未分离解释因果；生成label无需crowd不消除输入human label。root确认标准完成、仅报告，不升级为通用video能力，也不伪称同主题Books完整覆盖。

### [FILCO](https://arxiv.org/pdf/2604.07523v1)

Source Family：`SF-2026-ARXIV-2604-07523`；exact PDF v1 §2.1–2.5/§3/§4.1–4.4。固定MM原子和一维双缓冲FMU由逻辑视图、角色、partition和指令组合，运行时可变维度不等于物理容量或连线可任意重构。VCK190 FP32、PL150MHz/AIE1GHz/Vitis2023.1与BERT长度32–512是受限配置；SystemC与RSN解析基线不能当实芯片全部端到端测量或GPU/SLO。MILP Eq2不支撑所宣称普遍全局最优。Ch49 recurrent执行路径后已实际加入这一预布线/逻辑粒度分支，root必要源/实际正文独立通过。6分知识缺口深入，未复现实验。

### [SAGE](https://arxiv.org/pdf/2604.07663v1)

Source Family：`SF-2026-ARXIV-2604-07663`；exact PDF v1 Algorithm1/§3–4/Table2/AppA2。embedding保留`O(Vd)` momentum，额外column绝对梯度统计仅`O(d)`；instant/EMA RMS比例截断到1调节sign幅度，不保证方向正确或收敛。H200、270M/0.6B/1.3B、6.6B Pile tokens、seq512/global130K、bf16、三seed均值有限实验；0.6B全参数Lion26.58优于SAGE26.71，而Lion-Hybrid28.73并不更好。Pure两方法失败、dense UnitNorm配对与1D配置歧义不隐藏。Ch28 optimizer-state主线已实际写入第二状态与共享列尺度代价，root写后要求的Lion名称纠正已落实并再核通过。6分知识缺口深入，未复现实验或给通用Adam替代建议。

### [From LLM to Silicon](https://arxiv.org/html/2604.07526v1)

Source Family：`SF-2026-ARXIV-2604-07526`；exact HTML v1 §3.3–3.10/§4.1/4.3/4.13/4.14/5.4。联合mesh/core/partition与compute/memory/NoC分析成本可保留为受限架构探索。Llama8B FP16表9 batch3/seq2048与industry表20每用户1K并非相同合同，29809tok/s/51W是分析估算而非实芯片结果；4600单seed SAC与random/grid比较不证明稳定最优。5分标准完成、root认可仅报告，不以一个局部PPA点改变生产设计判断；部署并发/SLO未披露，未运行实现。

### [Learning Is Forgetting](https://arxiv.org/html/2604.07569v1)

Source Family：`SF-2026-ARXIV-2604-07569`；exact HTML v1 §2.2/§3 Eq2–6/§4/AppE8。角度归一、随机soft partition、层均值熵和n-gram backoff是固定C4/Tulu上下文上的代理，不是真实latent信息量。47模型六family六任务的相关性不证明因果或IB最优，DPI饱和也不直接给实际训练的可用frontier。Ch5记忆/压缩共存不等于已验证该新代理，因此不假称已有覆盖；5分标准完成、root认可仅报告。训练停止/模型选择仅提议，未披露或不适用的生产硬件/并发/SLO不补造。

### [VSAS-Bench](https://arxiv.org/html/2604.07634v1)

Source Family：`SF-2026-ARXIV-2604-07634`；exact HTML v1 §3.2.2 Algorithm1/§3.3/§4.1–4.3/Table2。独立camera与模型consumer、有界最新帧队列及carry-forward改变墙钟评价；回答更慢/更少也可能让consistency升高，不等于更正确。作者1FPS/600camera buffer/64context、H100 bf16，2/4B单卡、8B两卡、32/38B四卡，API含网络；memory policy与硬件差异不被当内部能力因果。Ch66在线流视频EvalSpec后已实际增加input/answer time、缺答策略及accuracy/update frequency/latency分账；answer completion time是书稿要求，不冒称Algorithm1完整记录。root原文/写后通过；6分知识缺口深入，PDF本次错误不伪称读过，必要HTML足够支撑采用范围，未复现实验。

### [Behavioral Dependence and Induced Bias in LLM Judges](https://arxiv.org/pdf/2604.07650v1)

Source Family：`SF-2026-ARXIV-2604-07650`；官方PDF v1 §3 Eq1–12/§3.3/§4.1–4.4。paper内部标题与索引短标题不同但必要正文身份相符。经验difficulty由同一模型群生成：两个独立Bernoulli(.5)变量在`d=.5`条件下被迫互补，残差积为−.25，因此无共享来源不自动推出该条件独立null。零均值也不足以证明有限精确sign-flip，尚需对称/渐近或交叉估计条件。两个disjoint1000 MMLU-Pro子集、18模型/三judges的重权是受限观察，不识别隐藏训练谱系。6分标准完成、root认可仅报告；中心保证被隔离而非否定所有诊断，重开需条件独立及随机化检验假设/实现说明。

### [SubSearch](https://arxiv.org/pdf/2604.07415v1)

Source Family：`SF-2026-ARXIV-2604-07415`；exact PDF v1 §3.3 Eq4–9、§4.3/4.5与AppA/D。二元EM outcome成功时，`(1-r_outcome)`关闭process代理奖励，format仍独立；失败时top-k query/document与父子/兄弟embedding相似只作过程proxy，不等证据覆盖或正确中间推理。中间reward在HotpotQA有益而NQ下降，不能默认所有错误轨迹都应获代理。四H100、prompt4096、response500、observation1200，base600/instruct200步；precision/并发/SLO未披露。正文Qwen3.2与Figure2–3的Qwen2.5标注冲突，不绑定精确模型headline。Ch33 rubric-to-token之后已实际加入outcome-gated代理、任务切片及outcome-only回退；root必要原文/写后独立通过。6分知识缺口深入，不新增trace标注不等于无需终答真值，未复现实验。

### [ConsistRM](https://arxiv.org/pdf/2604.07484v1)

Source Family：`SF-2026-ARXIV-2604-07484`；exact PDF v1 §3.2–3.4 Eq2–8、§4/5.2–5.3、AppA2–4。同一pair历轮pseudo-label均值与当前K次输出共同形成下一target，critique奖励只作用匹配target的输出；sign零点是两均值精确抵消，不是全部低confidence检测。Eq4的n项除n−1与Algorithm1除n、n=0归零不一致，不采用争议公式作为普遍保证。训练筛选使用ground-truth，不能称全流程label-free。Qwen3四配置、四epoch、batch64/K8、prompt4096/response1024、八A800，部分任务退步且length不等latency；precision/SLO未披露。Ch31 Majority Vote之后已实际接入pair-history target、漂移/版本成本、可信偏好回退并与sequence reward衔接；root原文和写后独立通过。6分知识缺口深入，未复现实验。

### [Benchmark Shadows](https://arxiv.org/html/2604.07363v1)

Source Family：`SF-2026-ARXIV-2604-07363`；exact-v1 §4–6、Tables1–3、§7。0.6B受控A–D实验分开原数据、optimizer变化、首半程十倍重复小子集和teacher规范化数据，但主要比较谱/rank代理，不直接证明这些代理导致泛化。外部模型混有训练数据/optimizer/时长，不能反向当因果消融。§6去重案例四类指标升、一类General-LLM降，谱汇总也不与任务表现同向；该反例支持诊断与outcome分账，不支持统一coverage/谱阈值。固定bf16、4096batch、约1.2T训练tokens的受限设置不包含teacher改写总成本或服务SLO。6分标准仅报告，未复现，不以正文通用化解释替代所测结果。

### [Flux Attention](https://arxiv.org/html/2604.07394v1)

Source Family：`SF-2026-ARXIV-2604-07394`；exact-v1 §3、§4.3/Table1、AppC3。prefill的prefix/suffix router冻结各层full/sparse路线，decode必须消费匹配KV；路线变更不保证旧KV有效。Ch22“Conditional Attention的route粒度”已实际覆盖这一机制以及A80080GB/BF16/batch1的prefill端到端与decode kernel-only分账。RULER部分切片低于dense，约束符号张力不作优化保证。6分标准已有覆盖；没有重复新增段落、未复现实验。

### [SHIELD](https://arxiv.org/pdf/2604.07396v1)

Source Family：`SF-2026-ARXIV-2604-07396`；exact PDF v1 §II–IV/Alg1/TableII。QO短生命周期与KV长生命周期、BF16 sign/exponent/mantissa敏感性共同形成刷新策略。3T retention/DESTINY2MB模型、H100长度2048的生命周期测量和随机mantissa故障注入是不同证据，不能并成实芯片整机节能证明；TableII的小幅质量退步保留。Ch54生命周期之后已实际加入bit与驻留时间联合分支；root必要官方PDF/正文写后PASS，6分知识缺口深入，未复现。

### [RefineRAG](https://arxiv.org/pdf/2604.07403v1)

Source Family：`SF-2026-ARXIV-2604-07403`；exact PDF v1 §3–5/Tables1/4、§6.2。MLM词替换保留目标错误语义、proxy retriever优化优先级，检索与target-answer攻击不同；低语法错误/重复率不等已测防御绕过，PPL亦有较差对照。100NQ+100MSMARCO、五污染文档、Contriever/两7B victims/A10080GB限该攻击合同，未完整披露生产长度/并发/SLO。Ch72已有provenance-bearing atomic claim及poisoning exposure/reasoning/contradiction/non-answer分账，承载这一具体安全判断；6分安全深入、已有覆盖，不外推充分防御。

### [GameWorld](https://arxiv.org/html/2604.07429v1)

Source Family：`SF-2026-ARXIV-2604-07429`；exact-v1 §2、§3.5、§4.1/4.5。可执行game-state verifier与确定性semantic action parsing不同于键鼠interface；主表在推理时暂停游戏，100action预算、单步通常200–500ms，测decision quality而非真实反应时间。34游戏/170tasks/18model-interface组合只支持该接口和环境；实时变体与主表不混算。Ch66已有trajectory outcome、action正确性/efficiency、harness与clock分账，Ch78接手typed action；6分标准已有覆盖，不把游戏分数转真实机器人能力。

### [HY-Embodied-0.5](https://arxiv.org/html/2604.07430v1)

Source Family：`SF-2026-ARXIV-2604-07430`；exact-v1 §2.2、§3.3。modality-specific QKV/FFN与latent表示、三目标到后期LLM-only的阶段变化需要分别验收，不能将发布模型的机器人结果归因为MoT单组件。Ch23“共享表示收益来自可控容量交换”已覆盖容量分责、冻结/训练状态和目标冲突；root必要原文/实际owner对读通过。6分标准已有覆盖，受限robot trials不构成单因果保证，未复現。

### [Scalable Joint Resource Allocation](https://arxiv.org/html/2604.07472v1)

Source Family：`SF-2026-ARXIV-2604-07472`；exact-v1 §3、§4.1–4.3。GH/AGH在model/tier/TP/PP/route联合可行域中构造计划；消融去掉过滤可失去feasibility。六querytype、六Llama1–70B、十GPUtier、FP16/INT8/INT4是模拟合同，analytic latency不是生产SLO测量；高波动rolling收益与低波动不优均保留。Ch56“先冻结可实现域，再排序候选计划”和“Admission也可以联合选择Model/Quantization/Placement”已有这两个具体原则。6分标准已有覆盖，不采用近最优或subsecond普遍保证。

### [Reasoning Graphs](https://arxiv.org/pdf/2604.07595v1)

Source Family：`SF-2026-ARXIV-2604-07595`；官方PDF v1 §3–5。证据item identity关联历史评价/decision_ref，已验证正确结果过滤后形成used/rejected profile注入；改变查询复用控制点，但历史正确不保证当前query适配，cold-start、identity与token成本仍在。exact-v1 §5明确无实验结果，索引后来ROZA标题/10.6pp数字不倒灌。6分标准仅报告，不把未验证方案写成稳定Books增量；没有伪称同主题完全已有覆盖。

### [Blink](https://arxiv.org/pdf/2604.07609v1)

Source Family：`SF-2026-ARXIV-2604-07609`；exact PDF v1 §4、§6.1–6.4/§7。host只做startup/provisioning，DPU ARM处理入口/tokenization/RDMA，GPU persistent scheduler持有batch/KV与device graph loop；120-launch额度窗口续接需保持状态。单H10096GB/BlueField3/FP16、ShareGPT均值1019→463、1–32req/s为受限设置；chunked prefill/prefix cache/offload禁用，同TRT engines对照有限，GPU-bound模型收益压缩，多GPU未证。Ch56 host隔离后实际加入此ownership分支，root原始PDF/正文PASS；7分深入，未复现、不继承通用SLO。

### [DIVERSED](https://arxiv.org/html/2604.07622v1)

Source Family：`SF-2026-ARXIV-2604-07622`；exact-v1 §2–4/AppC1–2。接受/残差采样保持`ν=w(x)p+(1−w(x))q`而非target p；训练weight head同时改quality与overlap，因此高acceptance不是lossless。端点文字与Eq4相反处不采用，部分任务/切片退步保留；八A10040GB、三个modelpairs、draft3/5/7、输出128/384/512、temperature0/1不含生产并发/SLO。Ch48 Lossless Verification后Relaxed Decoding Policy已有独立分布/质量shift及rollback合同。6分标准已有覆盖，未复现。

### [Guardian-as-an-Advisor](https://arxiv.org/pdf/2604.07655v1)

Source Family：`SF-2026-ARXIV-2604-07655`；exact PDF v1 §3.3–3.4/§4.2–4.4/AppE。risk label+解释注入再生成不是强制gate，label/explanation一致性judge也不是外部安全真值。低有害率下平均代价不等任意SLO；训练披露两节点各8GH200，latency图注不借此补成统一设备合同。AppE硬约束/小compliance假设不证明普通解码安全单调。Ch72“Safety Assessment与Generation可以分离，但Authority不变”已明确assessment/gateway/context/latency边界；6分安全深入、已有覆盖，不重复添加产品叙述。

### [Conformal Social Choice](https://arxiv.org/html/2604.07667v1)

Source Family：`SF-2026-ARXIV-2604-07667`；exact-v1 §3.3–3.5/§4/§5.2–5.3。三模型四轮verbal probabilities池化、每域每轮50/50ground-truth校准，再把singleton自动、多项/空集review分开。交换性只保证marginal set coverage，不自动保证singleton正确或adaptive stop-policy覆盖。MMLU-Pro八域与Bedrock模型组合、硬件/精度/SLO未披露，拦截错误比例是选择效果非推理改善。Ch66 Conformal/Risk–Coverage与Ch82 correlated consensus已有具体边界，6分标准已有覆盖。

### [MIPT](https://arxiv.org/pdf/2604.07716v1)

Source Family：`SF-2026-ARXIV-2604-07716`；以实际PDF v1 §5为准，不继承索引后来Fan Duality标题/结果。needle四类、512长度与10M Wiki训练的31M模型只支持有限phase/memory实验；PPL92对90.5、Python实现慢3–5倍等反证保留。phase gate/entropy proxy不是实测纠缠，`N*=Dξ`仍是conjecture；不得把训练activation/cache名词自动当常数decode内存证明。6分标准仅报告，未复现，不进入通用architecture保证。

### [TrajGuard](https://arxiv.org/html/2604.07727v1)

Source Family：`SF-2026-ARXIV-2604-07727`；exact-v1 §4.3 Eq6–7/§4.4/§5.1。窗口8、EWMA和连续三步越界用于在线风险检测；SAFE只reset监控累计状态，不回滚已发生的泄漏。target模型线上judge与GPT4o离线judge分开，相关误判和未检出风险不视作安全保证。Ch72动态风险段已实际加入sensor/authority、风险累计/reset与外部effect边界；root必要原文/实际正文写后PASS。6分安全深入，未复现。

### [Symbiotic-MoE](https://arxiv.org/html/2604.07753v1)

Source Family：`SF-2026-ARXIV-2604-07753`；exact-v1 §3.3/§4.3/Table2。modality专属experts与共享路径前向共用，generation warmup截断共享梯度，之后释放并scale .1/分组LR；不是直接给router标签就自然协同。understanding-only高LR同样collapse、重组loss及分阶段成本说明结构与优化混杂，不采单机制因果或零代价。Ch23模态容量交换之后已真实落两段、与隔离旧方案共存；root原文/正文PASS。6分知识缺口深入，未复現。

### [ACIArena](https://arxiv.org/html/2604.07775v1)

Source Family：`SF-2026-ARXIV-2604-07775`；exact-v1 §3–5、Appendix H1。输入、malicious agent和message poisoning跨hijack/disruption/exfiltration目标，1356testcases/28attacks/六MAS仅测其角色与交互合同；LLMjudge筛任务与变异搜索不提供完备真实攻击分布。topology不能单独归因鲁棒性，narrow defense迁移亦有限。Ch72 agent-level marginal safety/coalition/role-aware操作和authenticated provenance实际正文已有此设计判断；6分安全深入、已有覆盖，不把六拓扑排名当普遍因果。

### [ORACLE-SWE](https://arxiv.org/html/2604.07789v1)

Source Family：`SF-2026-ARXIV-2604-07789`；exact-v1 §3、§5.3。gold patch给edit location/API，reproduction tests与buggy运行给execution context；部分测试被刻意提前应用，不能当标准SWE线上未知条件。不支持selective execution的实例被排除，oracle上界与强模型实际提取分别测。Ch66“Skill必须在真实Control Path中评估”的oracle→selection→retrieval→adaptation链及“Tool成功扩展到Information Use/Outcome”已有这一原则；6分标准已有覆盖，不把提取上界当全Agent能力提升。

### [GRASS](https://arxiv.org/html/2604.07808v1)

Source Family：`SF-2026-ARXIV-2604-07808`；exact-v1 方法/周期采样、optimizer offload与对应消融。RMS gradient probe不更新参数，周期选择原参数层不同于低秩参数化；冻结层历史可陈旧，选择概率与层间耦合增加代价。全层potential optimizer保留CPU，GPU只驻本轮子集，不是总状态消失；overlap1.08x对自身no-overlap（Llama7B/batch4/length1024）而非对FFT提速。Ch30显存来源主线实际新增两段，root方法/消融/真实正文PASS。6分知识缺口深入、未复現。

### [PolicyLong](https://arxiv.org/html/2604.07809v1)

Source Family：`SF-2026-ARXIV-2604-07809`；exact-v1 §2、§3.1–3.3、§4–5/Tables3/8、AppE。当前checkpoint高熵query→检索→熵下降support，再相似检索拟distractor后shuffle；熵下降不等事实/因果依赖，相似不等已验证负例。Qwen2.5-3B四阶段各1Btokens：2K筛选不等128K训练依赖验证；RULER/HELMET为pre-SFT、LongBench为同Magpie后测，same tokens不含筛选/teacher总成本，pipeline完全overlap未采用。Ch27 checkpoint-coupled selector后真实补support/distractor分责与旧静态数据共存；root源/正文PASS。6分知识缺口深入、未复現。

### [LogAct](https://arxiv.org/html/2604.07988v1)

Source Family：`SF-2026-ARXIV-2604-07988`；exact-v1 §3–5。意图先写log、voter对intent投票、decider提交裁决、driver执行effect，三种AgentBus后端有不同durability；in-memory不持久，SQLite仅node reboot、remote store另有边界。snapshot+replay不自动使任意外部effect exactly-once，不可幂等动作必须限定执行合同。Ch81已有Durable Execution/Replay、attempt/read-certificate、effect outbox与commit/abort分权、不可回滚effect边界；root认可该具体已有覆盖。6分标准，不再同义追加Books。

### [LegoDiffusion](https://arxiv.org/html/2604.08123v1)

Source Family：`SF-2026-ARXIV-2604-08123`；exact-v1 §4.1–4.3/§5.1/§6/§7.1–8。deferred输入使节点先以已到的非deferred输入启动，在真正消费依赖时再等待；启动许可不等read许可，request identity、producer发布与可见性仍是runtime状态。model级节点允许同模型跨workflow组批/共享，但等待、传输、重算与deadline估计不能变成实际SLO承诺。12个SD3/3.5/Flux workflows、4–50steps、8–32H800真实与256GPU模拟、默认2×solo deadline、bundle/FCFS对照限作者设置；输入分辨率/精度/网络未完整披露。独立前缀很短时收益有限，approx cache/asynclora改质量不能继承pure-scheduling等价。Ch56 Progress State前实际写两段，与AR/token进度共存；root必要原文/实际正文PASS。7分深入，未复现或证明通用fault guarantee。

### [Alloc-MoE](https://arxiv.org/html/2604.08133v1)

Source Family：`SF-2026-ARXIV-2604-08133`；exact-v1 §3.2–3.3/§4–6/Tables4/7/AppA1–2。逐层相对PPL sensitivity→加性surrogate DP决定layer预算，实际token分配再从原router候选保floor并统一挑剩余配额。DP最优只针对该surrogate；Eq7候选大小/Eq9预算张力不采普遍最优，loadρ=.93–.99不证expert语义或EP通信收益。DeepSeek-V2-Lite/Qwen1.5-MoE-A2.7B/OLMoE、WikiText2/20tasks为有限合同；Qwen部分joint低于token-only。单H10080GB随机prompt batch8/input32/decode128、五warmup十次测量不包含完整精度/并发/SLO，placement/通信未联合建模。Ch21 Variable-k后实际加入calibration/runtime与两个预算控制层，root原文/正文PASS。6分知识缺口深入，未复現。

### [DMax](https://arxiv.org/html/2604.08302v1)

Source Family：`SF-2026-ARXIV-2604-08302`；exact-v1 §3.1–3.2/Eq3–10/Alg1、§4.1–4.3/Tables1–3。masked输入的当前预测再作为corruption训练clean恢复，区别uniform vocabulary噪声；decode用top1概率插值token/MASK embedding并调norm，prefix mask与两个连续top1相同/高confidence只是启发式提交，不是truth/收敛或original distribution保证。LLaDA-mini、八H200训练两epoch/batch8/block32、约.7Mmath/1Mcode，两H200TP/batch1/length2048推理限作者合同；precision/SLO未披露。无OPUT软解码失败、hard对照及小幅任务退步保留。Ch24 mutable/revision training主线实际写两段，root原文/真实正文PASS。6分知识缺口深入，未复現，不当任意模型无损加速。

### [Loop, Think, & Generalize](https://arxiv.org/html/2604.07822v1)

Source Family：`SF-2026-ARXIV-2604-07822`；exact-v1 §4/6.1–6.3/Limitations。课程须先形成可用recurrent-state更新，更多loops可能overthink；低KL也可能高entropy，联合halting只是启发式，正确token margin依赖标签不能当在线truth。合成受控任务/from-scratch、同12-hop动态与固定R8在一项任务同为19，未证明普遍动态深度收益。Ch18已写课程/termination控制与固定预算旧分支，root必要源及写后PASS。6分知识缺口深入，未复现。

### [Hidden Biases in Conditioning Autoregressive Models](https://arxiv.org/html/2604.07855v1)

Source Family：`SF-2026-ARXIV-2604-07855`；exact-v1 §2/5 Theorem2/8。succinct rational、局部多项式可计算AR模型的固定长度EOS mass可编码#SAT；有限validator并不自动使model未来接受mass易算。有限Markov×automaton仍有DP分支。该复杂性构造不是任意实际模型都困难，也不证明所有exact sampler都必须显式计算Z。Ch20已将model state/future mass条件补入finite-validator段，root源/正文PASS。6分知识缺口深入，无硬件benchmark。

### [Bit-by-Bit](https://arxiv.org/html/2604.07888v1)

Source Family：`SF-2026-ARXIV-2604-07888`；exact-v1 §3.1–3.5/§4 Tables3–4/AppA.3。weight再activation逐步降bit，block FP目标、STE/shared master派生8/4/2；OCS是已有通道拆分机制并增加activation宽度，E4M3 group32 scale增加存储。单H800作者设置不证明所有格式共享一次gate，Mistral7B 2bit及较大Qwen有退步。Ch49“一个Anchor Artifact支撑多格式，不等于一次验收覆盖所有格式”已实际要求转换规则/backend/逐格式质量、memory、latency及高精度回退，故6分标准已有覆盖，不新增重复摘要。

### [Robust Length Prediction](https://arxiv.org/html/2604.07931v1)

Source Family：`SF-2026-ARXIV-2604-07931`；exact-v1 §2.3/3.1–3.4。MAE目标对应条件median，ProD-M/D分别采用one-hot median或重复采样hist监督；test用16次生成median，并非下一请求实际长度。固定inference次数B、每题重复k改变独立prompt数量，不是同生成token/墙钟预算，math中k=1也可更好。两A10080GB、CUDA12.2/vLLM0.15.1、Qwen2.5-7B/Llama3-8B及四语料为有限合同；低于NoiseRadius的MAE不证明调度SLO。Ch56现有conditional heavy-tail、distribution calibration/quantile reservation及point fallback已承载决定对象，6分标准已有覆盖。

### [ResComp](https://arxiv.org/html/2604.07955v1)

Source Family：`SF-2026-ARXIV-2604-07955`；exact-v1 §3.3/4 Eq9–14/Alg1、§5.2–5.4 Tables3–6。冻结original FP output而非跟随compensated weights，以upstream与intralayer两残差更新；预计算不消除校准状态。GPTQ/GPTAQ消融和Llama1B–70B受限，W2A4KV4旋转组合可严重退化，原因是作者解释非因果实证；70B calibration峰值/CPUoffload内存与H20校准时间上升，非推理加速。Ch49实际两段与离线/在线Recovery交接，root必要源/写后PASS。6分知识缺口深入，未复现。

### [PEARL](https://arxiv.org/html/2604.08065v1)

Source Family：`SF-2026-ARXIV-2604-08065`；exact-v1 §3.1–3.8/4 Tables1–2/AppC。原问题与含最终答案的专家完整轨迹双前向，K=4预测token、trajectory stop-gradient、SmoothL1与NextLat辅助；部署无PRED、工具、图像编辑或latentAR。三种轨迹regime不含多种工具多次调用，部分子任务退步，不能说hidden目标是真实状态或实际规划。Qwen2.5VL3/7B、Qwen3VL4B、LoRA64/128、4H200或6H100/max4letter output只支持作者合同，concurrency/SLO未披露。Ch23对齐段实际接入训练表示目标与部署计算区别，已调整至时间/provenance标题前，root源/正文PASS。6分知识缺口深入，未复现。

### [CausalVAE World Models](https://arxiv.org/html/2604.07712v1)

Source Family：`SF-2026-ARXIV-2604-07712`；exact-v1 §3.2–3.5/§4 Tables1–3。先固定world model训练结构表示，再固定表示训练transition，用分阶段gate混合原/修正latent；训练用state labels，部署不等必须观测完整真实状态。三体、shapes、cubes、chemistry四个域配八组baseline，不能写成八数据集；state-alignment/gate消融与全方法不分离因果组件收益，局部一阶`|J−I|`也不是完整物理图。条件prior文字与后文表述张力不被采用为识别保证；不据此否定有限实现。6分标准仅报告：新接口可核，但没有稳定支持普遍counterfactual可靠性的证据，保留原pixel/latent world-model与真实反馈边界。

### [DAHS / BHA](https://arxiv.org/html/2604.07747v1)

Source Family：`SF-2026-ARXIV-2604-07747`；exact-v1 方法与AIME主表。teacher模仿student基础response风格后求解/验证，失败样本过滤；按response长度bucket采提示，再退火teacher-prefix比例，保留p=0无提示训练。ratio只对同提示suffix计算，不向teacher-prefix反传。Qwen3-1.7B/Llama3.2-1B、17K数学训练与AIME24/25/26、pass1/pass2048为有限合同；相同training steps不计teacher反复求解/校验总成本。Qwen AIME24 pass2048从base76.7到BHA70、Llama pass1亦有较弱对照，不能宣称完整恢复能力覆盖。6分标准仅报告：具体提示分布/撤除设计值得核验，但收益/预算证据尚不支持新的稳定全局训练选择；Ch33已有scaffold撤除与no-hint验收，不能仅凭主题重合将本机制伪称完整已有覆盖。

### [The Art of (Mis)alignment](https://arxiv.org/html/2604.07754v1)

Source Family：`SF-2026-ARXIV-2604-07754`；exact-v1 训练设置、misalignment/realignment主表与循环实验。四模型、六方法中SFT/PFT学习率不同（2e-4/3e-5），同五epoch不是同tuning搜索/计算预算。MisQA为13类共390条训练样本（§Data Collection、Table2、Appendix D.1），不是39K；1900测试题与三judge多数、局部human agreement只支持该评估；utility四任务平均不涵盖全部能力。ORPO并非处处更安全，DPO/LoRA/QLoRA恢复有异质性和残余错误，不能当安全更新的可逆操作。6分安全深入后仅报告：保留方法/顺序依赖与代价的受限案例，不用judge平均或跨配置排序改变长期修复保证；Ch72已有weight-repair新artifact/完整回归Gate，但不把它当相同实验的完全覆盖。

### [Influence-Based Code Data Selection](https://arxiv.org/html/2604.07769v1)

Source Family：`SF-2026-ARXIV-2604-07769`；exact-v1 influence算法、checkpoint/语料实验。CodeShell1B预训100B、20个checkpoint，每5B取点；20K候选、每十语言2K，单次update对目标coding validation loss的影响形成排序，再比较Top10K/Bottom10K继续训练。排序依赖训练阶段与具体任务，RoBERTa的20K代理转移失败；validation已经用于选择，不能再作为独立held-out。Ch27实际checkpoint-coupled loss/selector drift段和endpoint-relative influence段已说明这一具体判断及冻结mixture/重训对照。6分标准已有覆盖：机制实例可保留，不因paper新名称追加相同控制原则，未复现实验。

### [Structured Distillation of Web Agent Capabilities](https://arxiv.org/html/2604.07776v1)

Source Family：`SF-2026-ARXIV-2604-07776`；exact-v1 §5.2与harness/trajectory设置。三角色组合本身不够准入；值得保留的是减少teacher thinking预算后，所测六web环境teacher成功均更高，更新teacher版本却有四项下降，能力/预算排序反转。作者解释教师风格/可教性的两个假说未因该观测得到单组件因果证明。约3K收集/2322轨迹、9B student和BrowserGym合同；大headline含不同harness/observation，不能当同等成本蒸馏收益。Ch29“答案正确与推导模式值得学生模仿”及teacher–student独立任务验收已承载这一决定对象。5分标准已有覆盖，不把通用三角色架构当突破，也不丢弃具体反证。

### [SEARL](https://arxiv.org/html/2604.07791v1)

Source Family：`SF-2026-ARXIV-2604-07791`；exact-v1 §3.3及reward/evaluation设置。plan/retrieve/think/action、tool图创建与记忆联动；process奖励可解析plan、注册tool、可执行output，不等独立真值。按tool name/description语义相似合并anchor后跨context算step组优势，名称锚点不保证条件状态等价；episode/step标准化也需处理低/零方差。10K数学、Python/本地Wikipedia、Qwen3-32B与GT比较judge是受限合同；部分任务不胜GRPO，memory/reward联合消融不证明统一条件优势正确。6分标准仅报告：可核设计假说，但未获稳定采用依据；Ch33已有不能以语义相似伪造同组条件律的边界，不宣称该具体算法完全已有覆盖。

### [Semantic-level UI Element Injection](https://arxiv.org/html/2604.07831v1)

Source Family：`SF-2026-ARXIV-2604-07831`；exact-v1 §2–4/Appendix G。Editor→icon retrieval/overlay→Victim为黑盒screen-grounding攻击，元素内容无害也能让click偏离任务目标；L1错点与L2命中注入区域不同。885样本先由两个GUI基线过滤，每个victim再只计clean-correct，ASR不能称总体下界；查询D×3、累计best图标与random近似预算不是严格相同搜索成本。首次成功之后继续优化累计图标，不证明固定图标独立复现或persistent causality。Ch72原OCR/layout恶意语义入口未完整承载无害元素的感知误导分支，已依root授权在该段后实际写两段；6分安全/知识缺口深入，root必要原文及实际写后独立核通过；不是通用防御保证。

### [Contextual Representation Ablation](https://arxiv.org/html/2604.07835v1)

Source Family：`SF-2026-ARXIV-2604-07835`；exact-v1 RIS/CRA方法、四模型与攻击设置。已知refusal token的gradient signal选activation坐标，再按λ动态mask/失败扩大mask、rollback；Eq5是坐标删除，不证明多语义因果解耦或精确安全子空间。Llama2/Vicuna/Guanaco/Mistral7B、AdvBench/PKU/ToxicChat与DeepSeekV3/GPT4o judge局限白盒干预，不能外推普通API输入者权限。Ch72“Refusal Behavior不等危险知识消失”和white-box operator/外部effect Gate已有该具体风险判断。6分安全深入、已有覆盖，不把移除拒答路径等同新危险知识生成，未复現。

### [MESA](https://arxiv.org/html/2604.07914v1)

Source Family：`SF-2026-ARXIV-2604-07914`；exact-v1 §3–4/主表。teacher-forcing中EOS margin与短输出/Zipf频率纠缠，长度改善不等所有条件概率更忠实。冻结base训练visual token perturbations，top-m KL和排除最高五项的preservation只限制所选坐标，D_hall不是truth label；PCA hidden difference成为steering方向，不是完整分布保持证书。CHAIR/recall、POPE/AMBER/LLavaBench及maxnew512只支持该合同，未测生产SLO。6分标准仅报告：新的诊断/训练组合保留，但解耦与hallucination收益不足通用保证，不能把Ch66一般steering耦合原则当完整方法覆盖。

### [Unlearning or Untraining](https://arxiv.org/html/2604.07962v1)

Source Family：`SF-2026-ARXIV-2604-07962`；exact-v1 §4–5/7。经典随机训练A(D\S)等价关注有限S的训练影响；剩余数据可泛化回S，因此S答案被预测不单独证明删除失败。作者concept-wide目标用A(D\S_full)，S只是全概念实例的代表，S_full可得性/概念边界是额外假设；S=S_full时参照可一致。该概念分析不是通用删除算法，不采用DP等于无记忆等推论。Ch72已有参数/拒答分账，却缺这两个参考分布的明确区别，已在Unlearning开头实际补两段，6分知识缺口深入，root必要原文与实际写后复核通过；不签发概念删除保证。

### [GuarantRAG](https://arxiv.org/html/2604.08046v1)

Source Family：`SF-2026-ARXIV-2604-08046`；exact-v1 §3/评估主表。DPO偏好chosen document文本、rejected inner answer，即使后者正确也可被拒；长度惩罚和cosine query proxy不证明事实支持。refer answer由LLM按句切分后，embedding方向经γ注入hidden state；Eq6未说明不同坐标的映射，不能升级为hard claim-support commit。五QA、三Qwen8/14B、四retriever；joint训练/路由/解码与预算混合，不支持通用保证或等总成本归因。6分标准仅报告：保留可核实验分支，不能把生成标题中的guarantee写入Books，也不假称Ch76已完整覆盖其实现。

### [OA-EM Codebook Optimization](https://arxiv.org/html/2604.08118v1)

Source Family：`SF-2026-ARXIV-2604-08118`；exact-v1 §3.1–3.4/§4–6。M个K=256码本、g=8组中，固定centroids beam assignment不能自动改变表示容量；OA-EM仍顺序fit residual，以Hessian-weighted metric重分配/优化centroids（三轮/100 Adam steps）。ρ=N/(KM)只是容量proxy，不采盆地不跨越或充分条件。三模型2/3bpp、128C4×4096、五epoch、single seed；WikiText选择checkpoint不是独立测试，Qwen downstream .606→.594而PPL改善。A10080GB/8B PV单B200192GB的校准不证明LUT推理加速。Ch49量化Recovery主线已实际补两段centroid/assignment自由度与成本边界，6分知识缺口深入，root必要原文与实际写后复核通过。

### [QaRL](https://arxiv.org/html/2604.07853v1)

Source Family：`SF-2026-ARXIV-2604-07853`；exact-v1 §2.2/3.1 Figure2、§3.2与§4 Table1。learner forward实际使用低bit GEMM算log-prob，高精度master/STE backward保留，materialized量化权重发布给rollout；W4A16仅权重4bit、activation16bit，不是两者低bit。fake quant的舍入/反量化数值不等实际kernel算术，相同artifact也不承诺跨kernel/batch/设备bitwise相同。长度归一概率、ratio/log-domain clip的定义张力不用于TBPO信任域/无偏保证；作者主表局部退步和训练栈/发布成本仍在。Ch33 FP8/master段后实际增加数值模拟、实际算术与artifact发布的分支，6分知识缺口深入；root必要原文及实际写后独立通过，未运行实现或复现实验。

### [Dual-Pool Token-Budget Routing](https://arxiv.org/html/2604.08075v1)

Source Family：`SF-2026-ARXIV-2604-08075`；exact-v1 §2 Algorithm1、§3 Eq6–7、§4.1/Table1。按EMA bytes-per-token估计输入，再加max-output形成路由预算；这仍是估计，不是tokenizer精确长度证据。中心成本式Eq6对两个pool分别取ceil，Eq7却使用连续分数并宣称splitting always helps/保守下界。取λ=.5、μH=1、μS=2、α=.5，单池ceil(.5)=1，双池ceil(.125)+ceil(.25)=2，真实节省比例为−1，而Eq7=.25；直接反例只否定该无条件离散保证，不否定大规模连续近似和所有模拟结果。Llama3-70B-Instruct/BF16/TP2/A10080GB、两种100K Poisson派生trace来自Vidur校准模拟；short pool同时改context 65K→8K、Nseq16→128、batch-token8K→16K，不可将收益独立归因于context。6分中心设计反证深入、争议安全暂缓；Ch56现有预测身份/容量可行域不足授权采用该保证，本次不写Books。重开需保留ceil/利用率条件的成本式，以及分离配置变化的对照。

### [Plan-RewardBench](https://arxiv.org/html/2604.08178v1)

Source Family：`SF-2026-ARXIV-2604-08178`；exact-v1 §3.1–3.4/§4–5/Limitations。固定task、tool environment和多轮用户history形成成对完整轨迹，70%自然rollout、22%扰动、8%rule injection；LLM judge panel与meta-review生成偏好标签，不是独立执行真值。rubric区分工具无关/不可用、planning、recovery及refusal；worst unsafe episode不能被长benign前缀抵消，blind retry与未更新约束也不能用最后流畅回答掩盖。DRM独立逐轨迹打分与GRM/LLM成对AB互换是不同测量条件，宏平均及不均衡安全切片不构成部署发生率。Ch66『Deterministic-first不是拒绝Judge，而是限制它的权限』实际要求fulltrace、rubric、tool I/O、state和最终裁决分账；Ch72『Containment不能只看最终是否发生攻击』明确传播/授权/effect阶段，已承载本次设计判断。6分标准已有覆盖；此受限benchmark保留诊断价值，不追加同义正文，也不把English text-only、待公开artifact或judge preference升级为通用RM保证。

### [Dynamic Attentional Context Scoping](https://arxiv.org/pdf/2604.07911v1)

Source Family：`SF-2026-ARXIV-2604-07911`；官方PDFv1 §3.1–3.5/§6/7.4，与必要HTML段一致。orchestrator的REGISTRY只持有有界status，Focus(ai)读取该worker任务、steering历史与局部产出视图+其他worker紧凑registry；正常排队、urgent保存partial后切换并resume。它改变本次工作视图，不是新权限隔离；registry仍O(N)，F(ai)自身过预算时不能采用无条件硬界。160 scripted+40真实trial，真实Haiku4.5/N3或5/低决策密度、LLMjudge及agent-ID contamination代理，不证明普遍规模质量、zero pollution或interrupt单独收益；硬件/精度/部署并发/SLO Not Disclosed。Ch82 Supervisor/Worker瓶颈后实际两段，补齐steering工作视图与拓扑/权限的区别及stale snapshot/丢依赖/抢占成本；6分知识缺口深入，root原文及实际写后非作者核通过。没有运行作者实现或复现实验。

### [ATLAS](https://arxiv.org/pdf/2604.08044v1)

Source Family：`SF-2026-ARXIV-2604-08044`；官方PDFv1/HTML必要§3.1–3.4/§4.2–4.3/§5。SPMD算子与MPMD通信进入Ramulator2/BookSim2/HotSpot模型，operator barrier及固定inter-device带宽模型限制执行对象。channel/interleave granularity在row locality与parallelism间取舍；更多MC面积与DRAM功率又挤compute/可用频率，cloud/edge和batch改变配置排序。§3.4作者提供testchip分层性能对照与TDTR材料参数，不等探索架构热实测或全面仿真准确性；§4.3低batch MoE存在Stratum反向优势。FP16/4×4core mesh/7nm；§4.1 workload中OPT/Qwen context1K或4K、Llama/Mixtral8K或32K，§4.2 DSE图取batch64/context4K或16K子集，不是全部cloud负载或request concurrency/线上SLO；生产SLO Not Disclosed。Ch54 phase-specific knee后实际两段采用coupled-budget选择，保留通用HBM/校准/热约束回退，不采通用16channel最优或现货保证。6分知识缺口深入，root必要原文及实际写后非作者核通过；未运行实现。

## 5. 缺口与下一步

普通可执行工作为0。全部70项已有证据与最终处置，34项必要Books正文已实际写入并通过非作者写后核验，日级独立验收通过；以下仅为不能用于采用或无遗漏断言的终态保留项。

争议终态保留：PoST `2604.07658v1` 的Prop4.5反例和p坐标/实现连接未解决；`2604.07405v1` 的Theorem6 Eq7在二分类GN下已失败；DLR `2604.07518v1` 的Eq6采样、Eq10 claimed IS等号与Appendix B近似缺乏一致的density/surrogate说明。三项不进入Books、不支持正面理论保证。重开分别需要coherence界/p坐标勘误、CE谱界/真正Hessian连接，以及投影密度或明确surrogate误差/实现说明。GIRL `2604.07426v1` 的受限实现已仅报告；其中心duality/value-function条件不足另隔离，不采用普遍性能保证。只重开受影响命题，不阻塞其他普通工作。

日期逐家族隔离：TrACE08369、SkillClaw08377、SAVeR08401、KV offloading08426、MIG08451、KnowUBench08455、Metis-HDPO08545的自身v1 Updated为2026-04-10T01:01:47/01:02:14/01:04:05/01:05:33/01:06:31/01:06:40/01:10:39Z；这些晚字段既不能提供截点前上界，也不单独证明它们公开晚。尤其08426的近似KV反例、08451的共享功率/partition边界保留贡献信号。重开需要对应family在本窗截止前的官方artifact/目录可读公开链，再进行必要证据审阅；不机械迁移整批，不先评分或改Books。旧09731/16469仅保留04/14、04/21批次恢复线索，不扩本窗。Nexus09258的后建CMS/未版本PDF与截点后v1冲突，以及ConvApparel博客独立事件只有日级日期，分别需要截点前原始发布链和新增命题，不能倒灌后出论文或已处理原论文。

到期来源有界检查已结束，精确外部限制不是普通未读工作：OpenAI Research历史分页、Google Research Publications本窗索引、Meta Research/Publications、Moonshot历史研究日期目录未恢复。请求仅为各目录覆盖本窗的可读官方分页/快照或原始研究条目，不重扫全年；已检查Blog/RSS/项目组织页不替代缺口。MiMo Blog、MiniMax Agent Tech补充入口缺本窗历史日期，也不支持全源零更新；它们只在有本窗官方文章链时定点重开。这些限制不支持无遗漏断言，不生成未经核实的候选或Books结论。

DualPool08075重开条件：保留离散ceil与利用率约束的fleet成本式，以及分离context/Nseq/batch配置的对照。现有Eq7可作去ceil连续近似，不能宣称任意规模always-help/保守下界。它与前三项中心争议一样不阻塞已完成材料，但不能写正面保证。

## 6. 复核

复核者：root（日报作者apr03之外的准入、必要原文、实际Books与日级验收）；apr03独立核验root所写07666正文。
结论：通过

70行、70唯一家族与70项证据逐一对账，34项真实整合及相邻衔接均有非作者核验；有效且未变的单篇依据复用，不无差别重读附件。其余17已有覆盖、15仅报告、4争议的采用范围和§5重开条件已核对，不把安全隔离称为相关证据成立。

复核覆盖14个每日来源的实际窗口、主题与停止位置，不将587个旧原始身份变成全文队列。准入复核覆盖全部拟保留家族；否定侧除首批4正向/4负向校准、有限37项及关联理由批次、最后14旧身份对账外，root本轮实际读07392/07398/07422/07506/07551/07681/07833/08224完整题摘，并对07422的布局/条件生成与消融、07506的偏好监督/anchor和投票、07833的执行路径/模拟评价定点读必要方法。具体前分母关闭依据保存于原筛选笔记，不以主题已有、无新owner或领域较窄排除。抽检不能证明未查身份或全网无遗漏。

最终复核纠正07754的训练样本数为390（非39K），明确ATLAS不同workload/context与DSE子集，保留DualPool离散ceil反例及七个晚日期字段的逐家族隔离。`validate_research`、Markdown/本地引用和限定范围cached/unstaged `git diff --check`通过；它们只证明可判定一致性，不代替上述语义判断。未复现实验，未stage、commit或push。
