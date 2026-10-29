# Weekly Research — 2026-W43

**规范：** V3
**窗口：** 2026-10-18 ～ 2026-10-24
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-25T13:00:33+08:00

## 1. 结论

本周按七个完整自然日汇总：每日来源复用[10-19](../../10/19/README.md)至[10-25](../../10/25/README.md)七份已验收Daily，分别覆盖10-18至10-24；只对29个每周来源及已触发的具名原件新增研究，没有重跑七次Daily。

新增周级研究10个材料家族，必要证据及具体owner比较已由独立复核者检查：5个最小知识缺口已实际写入Books，另5项由现有具体论证承载。5处实际正文、完整前后衔接与来源注均通过非作者写后复核，完整Weekly独立验收通过，普通可执行待办为0。这里的10不是新论文总数：包括2份METR报告、1份Ai2研究报告、1个训练发布及6个工程发布家族；release交付不冒充其背景PR首次公开。

值得保留的三条联系是：监控eligible与真正送达不是同一分母；生成式记忆的接收、原记录提交和派生提取不是同一完成状态；训练或推理中间结果也不能越过实际数值/commit边界。它们是不同系统层的原理复用，不是这些项目之间存在直接演化谱系。IPO另提供ratio筛选之外的绝对概率差分支，收益仍受具体异步RL配方限制。

七份Daily现有612个候选条目已做跨日身份核对：594个互不重复的arXiv基ID与18个官方事件URL。不能把这些条目直接相加称为612项新贡献；OpenAgentCore、MiMo-Code、Qwen Code各有跨日不同事件，按项目家族归并并保留事件分数与处置，见§3。既有日级审阅/写后结果复用，不把本周汇总说成再次全文审阅。机构动态目录与两项既有中心争议仍受原报告限制。

## 2. 来源覆盖

每日组引用七份Daily实际入口/停止点，不重新抓取；新增每周组的原始查询、发布API分页与必要证据见[新增来源记录](./_sources/WEEKLY_NEW_SOURCES.md)。下表结果仅对应已描述的入口，不证明机构全网或所有历史版本无遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 七份Daily的Research index、官方正文及日期检查，完整覆盖本周窗口 | 已检查 | 沿用各日有限公开入口边界 |
| SRC-ANTHROPIC | 七份Daily的Most recent与具名原文；已审事件不重评分 | 已检查 | 不由目录推未披露内部活动 |
| SRC-GOOGLE-AI | 复用七日DeepMind/Research博客，均有具体停止段 | 受阻 | Publications缺日级公开列表的子范围沿用隔离，不以博客代替 |
| SRC-META-AI | 复用七日Blog及可读Publications替代段 | 受阻 | Research主体/混序论文目录不能支撑完整日期覆盖 |
| SRC-QWEN | 复用七日可读原文/官方artifact，10-25核稳定版scope变更；已审PR随release重列不重评分 | 受阻 | 新Research/Blog不可读子范围保留，不用旧站证明当周零研究 |
| SRC-DEEPSEEK | 七日官方研究/动态与更新日志在各日越窗停止 | 已检查 | 不外推所有分支/普通PR |
| SRC-MOONSHOT | 七日Blog、What's New和具名GitHub发布/实现 | 受阻 | 10-19/20的完整研究目录缺段并未因后日代码入口可读而被证明覆盖 |
| SRC-TENCENT-HUNYUAN | 各日具名原件复用；10-25从实际Research脚本恢复全部11/11条，最新展示09-22，覆盖当前目录的周窗排查 | 已检查 | 早期动态页读取失败不再当现存普通待办；不认证删除稿/全部历史修改 |
| SRC-ZAI | 七日Research时间序首屏与必要artifact，越窗停止 | 已检查 | 不扫描更早旧页或所有仓库 |
| SRC-BYTEDANCE-SEED | 七日显式排序目录/本周具名VeOmni事件，原审阅复用 | 已检查 | 保留原字段日期口径，不把merge当论文首发 |
| SRC-BAIDU-ERNIE | 七日博客/Publication与具名原始入口 | 已检查 | 仅ERNIE约定切片，不外推整个Paddle生态 |
| SRC-XIAOMI-MIMO | 各日已恢复原文与MiMo-Code事件复用，10-25另有限恢复首页5篇日期 | 受阻 | 首页未保证严格日期序/隐藏More范围；不能作完整日级目录保证 |
| SRC-MINIMAX | 七日Blog/Agent Tech与具名OpenAgentCore/MiniApp事件复用 | 已检查 | updated不等发布；原件支持范围之外不作保证 |
| SRC-ARXIV | 复用七日主题检索、公告/日期依据与必要审阅；594个不同基ID，不全分类重扫 | 已检查 | 各日具名日期资格/中心争议仍隔离；不是全学科召回 |
| SRC-MISTRAL | News本窗2篇，读至10-15；Voxtral3核心、工程合作范围已判断 | 已检查 | 模块组合/科学应用不自动准入 |
| SRC-AI2 | Latest Research读至10-14，本窗4项，FairStress必要报告已读 | 受阻 | Papers首屏只有年份且非日期序，全论文日期目录隔离；Latest范围已查 |
| SRC-BLACK-FOREST-LABS | Research整页3项，最新03-03，无分页 | 已检查 | 仅该目录无当窗项 |
| SRC-PHYSICAL-INTELLIGENCE | 主页研究链接及Research7题名，最新10-13 | 已检查 | 不扩旧论文 |
| SRC-WORLD-LABS | Research/News列表完整可见页，最新09-28 | 已检查 | 仅所见公开目录 |
| SRC-SSI | Updates3条读完，最新07-26 | 已检查 | 无本窗目录项，不推私下研究 |
| SRC-REFLECTION-AI | Blog最新10-05；Newsroom首9条最新07-14，越窗停止 | 已检查 | 不点旧新闻更多页 |
| SRC-AMI-LABS | Updates一条03-10，读完 | 已检查 | 不推其他未披露活动 |
| SRC-THINKING-MACHINES | Connectionism7条读完，最新07-31 | 已检查 | 无当窗目录项 |
| SRC-PRIME-INTELLECT | Blog10-19后接10-15；IPO精确tag文档补核心 | 已检查 | 不采用混配置的吞吐归因 |
| SRC-SAKANA-AI | Blog10-23/21/20读至10-15；QD-Rec完整题摘与技术说明 | 已检查 | 推荐应用、活动及无新机制治理组合排除，不按blog日改论文归属 |
| SRC-RECURSIVE | Updates10-21 Flint与旧06-11研究，读核心 | 已检查 | 无可比因果分解，不以速度宣传准入 |
| SRC-MIND-LAB | Publications7条最新10-16、Updates最新09-22 | 已检查 | 不延伸旧论文 |
| SRC-SAND-AI | 官方研究链接；MAGI-1/MagiAttention/MagiCompiler发布API共0/13/2条，最新均窗外 | 已检查 | 组织updated不等新研究事件 |
| SRC-EVERMIND | 官方链接EverOS发布API22条，窗内1.5.0/1.5.1后10-14停止 | 受阻 | release范围已查；主页无日期研究目录子范围隔离 |
| SRC-METR | 主页risk列表10-22/20及Research最新08-26，两份原文必要层 | 已检查 | 内部报告未公开部分不用于扩展公开结论 |
| SRC-PYTORCH | 官方releases API30条，最新2.14.1为09-30，跨下界停止 | 已检查 | 不扫描普通PR |
| SRC-MEGATRON-LM | releases API30条，最新10-13，跨下界停止 | 已检查 | 仅发布入口 |
| SRC-DEEPSPEED | releases API30条，本窗0.19.8，读完整说明及2个具名正确性PR | 已检查 | 背景PR早于周窗，不冒首次公开 |
| SRC-VERL | releases API16条全部返回，最新09-20 | 已检查 | 不以无release推无commit |
| SRC-VLLM | releases API30条，本窗0.32.0，读Highlights/Engine/Security/Breaking及SHM变更 | 已检查 | 不是全814 commits代码审计 |
| SRC-SGLANG | releases API30条，本窗0.5.22，具名43029实际diff | 已检查 | 不是逐950 PR审阅 |
| SRC-TRITON-LANGUAGE | releases API7条全部返回，最新08-28 | 已检查 | kernel language，不混同推理服务器 |
| SRC-FLASHINFER | releases API30条；rc5/rc6/post1 compare39/9/56条题名，重叠不相加 | 已检查 | 仅具名5652正确性必要层，不由版本号增加候选 |
| SRC-NCCL | releases API17条全部返回，最新09-17 | 已检查 | 仅发布入口 |
| SRC-HF-TRANSFORMERS | releases API30条，本窗5.20.2四项核心及49688必要diff/oracle | 已检查 | 不把全FSDP分母误写成此次故障原因 |
| SRC-KSERVE | releases API30条，最新09-25，跨下界停止 | 已检查 | 不扫描普通PR |
| SRC-RAY | releases API30条，本窗2.58.1/2.57.1同两项说明 | 已检查 | 回调作用域与CLI镜像未带来本项目独立长期机制增量 |
| SRC-MCP | releases API9条全部返回，最新07-28 | 已检查 | 无新规范事件，不扩大到全部SDK |

按需组没有独立新会议发布批次或协议变化触发；仅为上述具名候选打开相关primary原件，不升级为全站扫描。

## 3. 候选与判断

以下只列本次每周组新增10家族。有效Daily事件去重复用，不把它们重新列成待审候选或重复计分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [METR / OpenAI内部Agent监控红队](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) | 2026-10-22 | eligible与实际送达分责，触发不能由被观察Agent持续行动推迟；2+2+2=6 | 深入完成 | 整合：`PLATFORM-MONITORING`，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md)，独立观察路径后最小段，实际写后通过 |
| [Prime / prime-rl 0.10.0与IPO](https://www.primeintellect.ai/blog/prime-rl-0-10-verifiers-0-4) | 2026-10-19 | 双边绝对train/infer token概率差mask，与advantage符号和PPO更新clipping分开；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)，异步ratio noise论证后，实际写后通过 |
| [METR / Anthropic风险报告外部审查](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/) | 2026-10-20 | 隐藏CoT可能删除生产monitor的可利用通道，不天然是更保守压力测试；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，监控可见性论证，实际写后通过 |
| [Ai2 / FairStress](https://allenai.org/blog/fairstress) | 2026-10-20 | 固定题目/weights下wording与scoring可改偏置方向，选择率不等压力对称；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，压力对称、评分事件与harness脆弱性具体论证 |
| [DeepSpeed v0.19.8](https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.19.8) | 2026-10-20 | CPU/Gloo独立collective完成与dtype bucket资格的新受限验证；1+2+2=5 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，ordering/completion/visibility与实际归约域 |
| [vLLM v0.32.0 / SHM句柄认证](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) | 2026-10-18 | 签名绑定key/address/id并约束clear后的身份复用；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，cache授权与对象生命周期，实际写后通过 |
| [SGLang v0.5.22 / grammar与recurrent commit](https://github.com/sgl-project/sglang/releases/tag/v0.5.22) | 2026-10-19 | grammar截断后最终retained长度才决定recurrent snapshot frontier；2+1+2=5 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)，KV/recurrent/output共同提交边界 |
| [FlashInfer v0.7.2rc5 / rc6 / post1](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.2rc5) | 2026-10-20 | 初始peer rendezvous不能由post-store/lifetime屏障代替；1+2+2=5 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，input readiness、发布与回收分责；三个release只计一家族 |
| [Transformers v5.20.2 / EP bf16归约](https://github.com/huggingface/transformers/releases/tag/v5.20.2) | 2026-10-20 | EP拓扑下PREMUL_SUM数值故障表明loss有限不代表expert梯度正确；2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，实际域及operator/dtype数值验收 |
| [EverOS v1.5.0 / memory提交与派生完成](https://github.com/EverMind-AI/EverOS/releases/tag/v1.5.0) | 2026-10-21 | durable accepted、原cell commit与derived extraction完成三态及取消边界；2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)，transaction boundary后，实际写后通过 |

跨日归并保留而不改写原始事件：OpenAgentCore的[808/811](../../10/22/README.md)、[819](../../10/23/README.md)、[846](../../10/25/README.md)是同项目家族三次接口变化；MiMo-Code的2695/2703与Qwen Code的15104等已审PR/新scope release分别保留两日不同命题。不得因family合并丢掉某事件的必要证据或把仅报告升级整合。其余arXiv按基ID去版本、官方报告按原文身份去重；两个METR独立报告不是一个报告的转载。

## 4. 证据与知识整合

### [METR / OpenAI内部Agent监控红队](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)

公开Findings和design ideals支持的缺口是合资格轨迹未必触发送达：compaction遗漏与等Agent交还控制权，会让真实行动不进入monitor。Ch67原有独立观察路径，但没有把eligible、triggered、delivered、reviewed分开；新增一段以独立inference/monitor记录对账，并解释触发不能由被观察者拖延。证据只针对7月21日前历史系统；漏覆盖估计有日志不足的不确定性，未查明Agent实际利用，修补是厂商声明且未获该团队复验。不能由本文认证10月现况。

### [Prime / prime-rl 0.10.0与IPO](https://www.primeintellect.ai/blog/prime-rl-0-10-verifiers-0-4)

[精确tag文档](https://github.com/PrimeIntellect-ai/prime-rl/blob/v0.10.0/docs/ipo.md)给出双边绝对概率差mask，不依赖advantage符号，区别于ratio门和相邻policy update clipping。Ch33只补这一替代分支：此token/其他二分的TV不能代表完整词表TV，过滤会改变有效更新人口，也不恢复无偏性。GLM-4.5-Air/SWE、最多64步陈旧、无router replay的极端消融不证明普遍胜出；过严阈值曾熵坍缩。评分/阈值校准、废样及刷新rollout都付费，旧ratio或同步路径仍适用。没有采用同页混配的速度倍数。

### [METR / Anthropic风险报告外部审查](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/)

采用公开scope、covert-capability分析与具体协议差异，不借未公开内部案例补证。生产monitor可消费CoT时，理由可能解释或掩盖越界动作；评测隐藏CoT同时删去了这条攻击通道，因此不是天然更强压力测试。Ch66新增这一反例，要求比较真实消费通道与同轨迹删减视图。METR不认定具名理由必为蓄意欺骗，也没有全面认证防护；不由有限案例推出action-only普遍更优或全局漏检率。

### [Ai2 / FairStress](https://allenai.org/blog/fairstress)

已读[原始报告](https://allenai.org/papers/fairstress)摘要、§3.1、Appendix D.1 Tables33–36及限制。固定题目/weights的raw completion、chat、生成、loglik和yes/no五配置会改变偏置方向；wording与scoring都贡献，不能唯一归因某一项。合成两候选、固定身份/equality定义不认证真实社会公平，训练audit相关性不是成因。Ch66的matched A/B压力、valid-choice/拒答分母、选项logits与生成事件分开、固定weights下harness敏感性已具体承载这三个判断，故不重复写书。

### [DeepSpeed v0.19.8](https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.19.8)

仅深入[8382](https://github.com/deepspeedai/DeepSpeed/pull/8382)与[8539](https://github.com/deepspeedai/DeepSpeed/pull/8539)具名正确性变化：dtype字符串可漏CPU bucket，mean/相同rank梯度会掩盖缺allreduce；独立Gloo handles不继承CUDA stream FIFO，wait末个不证明全部完成。Ch36已拆ordering/completion/visibility、每项显式wait和实际归约域，足以承载设计选择。背景PR9月已公开，本次是10月release交付检查，不重定发明日；作者CPU回归不是本轮复现，不外推CUDA原路径已坏。

### [vLLM v0.32.0 / SHM句柄认证](https://github.com/vllm-project/vllm/releases/tag/v0.32.0)

[59357](https://github.com/vllm-project/vllm/pull/59357)实际diff将SHM key/address/id绑定认证，读/touch及外部输入交engine前核验，clear不重置ID。Ch72原有principal namespace不等句柄对象生命周期，新增一段解释旧slot地址不能认证当前对象。仅可选SHM路径，默认LRU不受此问题影响；服务端SHM秘钥不防本机内存权限攻击者。PR9月公开，本次release不是新漏洞首发；作者测试记录不等本轮运行，亦不认证整版安全。

### [SGLang v0.5.22 / grammar与recurrent commit](https://github.com/sgl-project/sglang/releases/tag/v0.5.22)

[43029](https://github.com/sgl-project/sglang/pull/43029)的scheduler diff以grammar最终retained长度扣除非draft token，而不是中间spec accepted数，决定Mamba快照跨界。Ch48已解释recurrent状态、KV、accepted length和streamed output必须跨同一最终frontier，这里属于具体新验证，不是独立的新状态代数。背景PR10-10，release10-19；本轮未跑GPU回归，不推广所有后端。保留具体修复而不新增一段相同原则。

### [FlashInfer v0.7.2rc5 / rc6 / post1](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.2rc5)

三个交付日分别为10-20、10-22、10-24；compare重叠不相加。[5652](https://github.com/flashinfer-ai/flashinfer/pull/5652)在peer DSM访问前补初始cluster rendezvous，后续store/lifetime barrier不能替代这个前提。Ch36已分别讲input readiness、发布完成、回收和peer访问资格，故具体实现留报告、不重复原则。网页缓存Open与官方API当前merged有差异，已核精确merge；不以缓存旧态否定现态。作者CUDA Graph变输入/PDL回归不等本轮Blackwell/Rubin复现。

### [Transformers v5.20.2 / EP bf16归约](https://github.com/huggingface/transformers/releases/tag/v5.20.2)

[49688](https://github.com/huggingface/transformers/pull/49688)针对token dispatch且tp小于ep、ep小于fsdp×tp的路径，BF16 PREMUL_SUM可使expert梯度为零，改为SUM后本地divide。**全FSDP分母保留且原本有其batch语义，不是此次应改小组分母。** 来源初稿的含混句已据actual diff修正。4×B300/torch2.13作者oracle与FP32参照只是受限验证；Ch36现有实际归约域、零梯度参与以及类型/operator数值验收已承载选择，不为每个具体bug重复新增“验证数值”的段落。

### [EverOS v1.5.0 / memory提交与派生完成](https://github.com/EverMind-AI/EverOS/releases/tag/v1.5.0)

release明确durable inbox及非原子提取：202只承诺接收，原cell提交不等派生episode可检索。写后请求超时曾取消提取，修复将写前timeout和写后派生责任分开；Ch77 transaction boundary之后补一段这个生命周期。失败默认不自动retry，有限crash replay不是exactly-once；队列、状态和恢复付费，缺少交接资格时回同步或仅承诺原文接收。embedding identity另属既有检索owner，不在Memory重复扩写；并发默认调大不另算新机制。

### 跨日关系：身份延续不是对象地址延续

早期简单恢复可以重建短任务或读回checkpoint；本周[Daily10-22/23](../../10/23/README.md)的准备复用、predispatch关闭与[10-25](../../10/25/README.md)原地native复用，分别要求不同阶段的身份/完成证据。EverOS再说明即使原文已提交，派生物仍可能未完成；vLLM则说明地址可读不代表同一当前对象。这些机制组合的收益是复用昂贵状态，新增压力是多身份、兼容域、取消与清理对账；无法取得资格时保留ownership、拒收句柄、同步提取或人工恢复，而不是把缓存命中/恢复成功统一称任务完成。

### 跨日关系：少看信息不必然更保守，改分母不等修正目标

FairStress与Daily已有评分事件边界说明，固定weights也不使不同harness测同一行为；METR的CoT反例进一步说明删去信息会改变攻击面。IPO则在训练端更换筛选距离，改善某类ratio敏感性同时改变有效样本人口。三者不是同一算法的演化链，而是measurement/selection定义进入结论的原理复用；必须保留原baseline、具体反退和受测人口，不从局部稳定或压力通过外推任务/安全真值。

### 跨日关系：快路径仍要跨真实提交边界

本周Daily中的KV、draft与训练执行结果已进入各自owner，Weekly不重写这些论文摘要。SGLang、DeepSpeed、FlashInfer和HF补充了不同层的具体故障：接受量不等最终保留、最后一个handle不等所有完成、后置屏障不等初始ready、loss有限不等expert梯度正确。已有Ch36/48可以完整承载这些判断，故五项已有覆盖不是遗漏Books，也不为制造diff重复写入。

## 5. 缺口与下一步

普通待办：无。5处新增Books实际写后及本周六部分独立验收均已通过。每日组七份Daily均已验收，无缺失日期，不顺带修复W41/W42或历史六月。

本窗终态保留项：Google日级Publications、Meta动态Research、Qwen新站、Moonshot早两日完整研究目录、MiMo首页日期覆盖，以及Ai2 Papers/EverMind无日期主页子范围。有限替代入口已处理，这些缺段不支持正面证据、Books或无遗漏断言，也不授其子范围Coverage通过。定点重开条件是取得目标周官方可按公开日限定的列表/公告，或具名本窗原文；只重开受影响子范围，不无限全站恢复。

既有Daily10-21两项中心争议及其具名日期资格保留原隔离条件，不因汇总而获得正面证据或Books许可。普通未读材料不能冒称外部受阻；新增10项没有尚待读取的必要原文，实际验收也已完成。

## 6. 复核

复核者：`live1025_weekly_review`（非Report/Books作者）；各Daily原独立复核身份与写后结果见对应§6。

结论：通过

10/10新增候选的准入、日期、必要证据与具体owner均已独立核查；5项已有覆盖有实际正文承载，5处由`live1025_weekly_sources`写入的自然段、完整前后文与true H2来源注均经非作者真实写后通过。HF分母误述已按精确diff修正。七日实际窗口、43个到期来源、612条日级记录/594个arXiv基ID、跨日项目家族的不同事件及7个子范围隔离已核对，3条关系分析不冒直接技术谱系。范围、代表性排除抽检及未检查部分见[独立复核](./_sources/REVIEW.md)。V3、27个两报告本地引用及限定空白检查通过；格式不代语义，没有重新审阅Daily的全部有效原证或运行第三方实验。

本周只新增Weekly/必要原始记录与5处Books自然段/简洁来源注；Daily10-25另有Ch84一处。未修改旧Daily、合同、ROADMAP、索引或Git暂存，未stage、commit或push。历史补查未在本次日常触发中继续。
