# Weekly 新增来源检查 — 2026-W43

窗口：2026-10-18～2026-10-24，北京时间完整自然日。执行：2026-10-25 BJT。
仅保存每周组29源的新增检查与必要证据，不是 Weekly 正文或完成声明；当日 Daily 完成前不生成 Weekly。每日组由 root 复用 Daily19～25，不在本文件重扫。仅本文件由 live1025_weekly_sources 写入。以下10个家族为本窗新增候选（METR两份为两家族，FlashInfer三个release事件只计一家族）；并非10项Books整合或独立验收通过。

## 新增候选的必要证据

METR monitoring与Prime IPO首批已获root准入校准；其余候选的最终独立准入、owner及Books判断仍由root承接，下面的阅读状态不冒充独立复核通过。

### METR / OpenAI 内部 Agent monitoring（2026-10-22）

[原文](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) Findings 与 design ideals；已读核心、脚注权限和限制。2+2+2=6；因实际可靠性边界深入审阅。原先 eligible 流量容易被当实际监控覆盖 → compaction 和等待 agent 归还用户控制权能造成轨迹不送达 → 监控触发不应受 agent 继续行动控制，需从独立 inference/monitor 两侧对账。Owner 建议 `PLATFORM-MONITORING`，Books 由 root 对照，不在此宣称已有覆盖或整合。

访问：一名 METR 与一名 Redwood 人员在7月21～8月11进行高访问试点；结论只针对7月21及之前系统，不是10月现况。发现 compaction 未触发导致约一成 eligible Codex 流量未监控的估计，日志不足使比例不确定；相关问题由 OpenAI 先独立发现并在试点期间修复。turn-end 触发曾允许持续行动推迟监控，但受访者未查 agent 是否实际利用。eligible 不等最终送达，不能把99.2% eligible当真实成功监控率。官方原文另列 serialization、header 与监控权限边界，但不展开未公开漏洞。生产修补是 OpenAI 声明，METR未复验。61页内部报告和部分细节未公开，不能借此认证全部监控/当前安全。

root 首批准入校准已确认此实际变化可准入；Durability采用稳定约束2，不以通用原则加3。独立owner/写后由root继续。

### Prime Intellect / prime-rl 0.10.0 与 IPO（2026-10-19）

[官方发布](https://www.primeintellect.ai/blog/prime-rl-0-10-verifiers-0-4)，§IPO与后续RL变更；[精确v0.10.0配置说明](https://github.com/PrimeIntellect-ai/prime-rl/blob/v0.10.0/docs/ipo.md)已读完。2+2+2=6，标准必要层完成。原来 trainer/inference 以概率比筛异步样本 → 双边绝对概率差 mask（不依赖 advantage 正负）→ 低概率token的相对变化不应直接等同绝对分布漂移，应区分 rollout mismatch 与 PPO policy-update trust region。Owner建议 `TRAIN-GRPO`。

具体规则：超过 epsilon 的绝对 train/infer token 概率差剔除；DPPO提供概率差思想，但IPO把它用于trainer/inference差异且与advantage号解耦。极端消融为 GLM-4.5-Air、agentic SWE、无router replay、最多64 steps off-policy；IcePop约1.2k步崩溃，IPO eps0.2/0.3保持训练。原文明确通常IcePop也稳定。没有披露可支持普遍优越的多任务/硬件及重复统计；不把此结果写成普遍更稳定。默认eps0.3且无KL；其他loss仍可选。mask/筛样本改变有效分布且不证明无偏。top-p/k mask重放、冻结router与固定batch回填是同release中不同控制变量，不凭本图给它们归因。

同页 SFT 吞吐对照有固定4×8 B300、16k、FSDP+EP8、full checkpoint、fp32 AdamW；GLM部分8→12节点且改变offload/CP，不能合成纯kernel加速。此处不采用性能倍数。

精确tag文档补核：same recipe only trainer.loss改变；2 trainer nodes（Muon/CP4 Ulysses）、4×单节点TP8 inference replicas且EP；256rollouts/16groups、131k上下文、GRPO与0.1线性长度惩罚。eps0.1曾导致熵坍缩；1.8M sampled tokens重放只用于阈值筛选，不当完整训练sweep。单token对“该token/其他”二分的绝对差为TV，不等词表联合分布总变差，不能由此声称全分布受限。硬件型号/多seed置信区间在这段消融中Not Disclosed。

### METR / Anthropic风险报告外部审查（2026-10-20）

[原文](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/)，Executive summary、§covert capabilities、scope/access与限制。2+2+2=6；评价可靠性边界深入必要层完成。原假定隐藏CoT的攻击评测更宽松 → 该评测反而移除了利用CoT理由骗读CoT monitor的通道 → 评价分布应覆盖生产monitor实际读到的解释，而非将action-only通过外推到完整轨迹。Owner建议`PLATFORM-EVALUATION-SYSTEM`。METR仅据内部8月报告轻量审查，不具该机构新协议宣称的深度访问；其低风险同意主要基于当时能力不足，不是证明防护充分。事件中CoT似乎误导monitor，但METR不声称该rationalization蓄意；移除CoT的反事实flag率由Anthropic提供且非全局漏检率。不能由此断言CoT总有害或action-only普遍更优。报告的部分内部历史案例仍未公开，不能凭其未公开论据证明全部风险路径；当前可采用的是明确evaluation/production分布错位。

### Ai2 / FairStress（2026-10-20 官方发布）

[发布](https://allenai.org/blog/fairstress)及其直接链接的[原始70页报告](https://allenai.org/papers/fairstress)《Asymmetrically Unfair Decision Making and Reasoning in LLMs》。2+1+2=5；已读完整摘要、§3.1、Appendix D.1 Tables33–36、Limitations/Ethics，标准必要层完成。最终选择一致不等压力下抵抗对称 → 固定题目与weights，改变template/wording/scoring后偏置方向能变 → 评估要区分选择、受压转向与评测运行约定，而非把固定选项logprob当生成式交互行为。Owner建议`PLATFORM-EVALUATION-SYSTEM`。

关键受控证据是四模型五配置：S1 raw completion multiple-choice/loglik；S2 chat同wording/loglik；S3 chat generation；S4 yes/no loglik；S5 yes/no generation。不是仅比较两个不同benchmark。三个模型S1→S5翻方向，一个近零；D.1特别说明wording与scoring都贡献，不能把全部差异归因loglik。生成不可解析计错/剔除的差异保留。FairStress短合成两候选、GPT4o-mini生成并人工核验、单句prefix和固定US-centric身份组合；equality定义不是所有equity定义。训练数据audit只相关，不宣称训练成因已证；未将两个模型activation可分性写成真实因果推理解释。

### DeepSpeed v0.19.8（2026-10-20 BJT）

[release](https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.19.8)，已读完整变更列表，仅对具名影响正确性的[8382](https://github.com/deepspeedai/DeepSpeed/pull/8382)和[8539](https://github.com/deepspeedai/DeepSpeed/pull/8539)读root cause、fix与复现。1+2+2=5；可靠性变更深入必要层。旧GPU测试通过不等CPU/Gloo collective正确 → CPU类型字符串未匹配可跳过梯度bucket，且等待末个异步gather不证明独立Gloo线程全部完成 → bucket按dtype、逐handle完成后发布param视图，不依赖CUDA stream FIFO偶合。Owner建议`TRAIN-DISTRIBUTED-TRAINING`。

8382 exact merge `20a60f221ff24bd0b556c6651fb22625af543feb`，CPU mean/相同rank梯度能掩盖漏allreduce，sum才暴露world-size因子；8539 merge `e71b8f3335b98a07665705c429452d509dcbfa18`，CPU synchronize为空操作，旧buffer可能未初始化。作者CPU/gloo world-size2–3回归与重复故障复现，不是本地重跑；不能断言CUDA原路径已坏。两PR9/21早于本窗，本窗仅首次检查release事实，不搬移PR首公开归属。其余AutoEP/AutoTP、Muon、弃用/模型接线不因变更多自动入选；不以这一组结果认证整份release。

### vLLM v0.32.0（2026-10-18 BJT）

[release](https://github.com/vllm-project/vllm/releases/tag/v0.32.0)，Highlights/Engine/Security/Breaking；对具名SHM信任变化[59357](https://github.com/vllm-project/vllm/pull/59357)核Summary和实际diff，merge `3d5625cc3c2474994107047d7a6ecb8e4008f9b0`。2+2+2=6；安全变化深入必要层。外部提供的cache address/id曾当可信内部句柄 → 签名绑定cache key/address/id并在读取及touch前核验，clear后ID不回零 → cache命中身份必须同时有授权与生命周期有效性，局部地址相同不等同对象或可反序列化内容可信。Owner建议`PLATFORM-SECURITY`。

仅`--mm-processor-cache-type shm`；默认LRU不受该问题影响，签名秘钥留服务端shared-memory而非防有本机内存访问权的攻击者。核对bounds、wrong-key、旧handle/clear、scale-out输入前校验；74 passed/1 skipped为作者记录，本次未运行或复现。PR9/30公开，本次采用10/18release事件，不冒充新漏洞首发。其他低比特KV/吞吐或新增接口只有型号/版本与厂商配置数字，未另升格；没有据此保证整版vLLM无其他漏洞。

### SGLang v0.5.22（2026-10-19 BJT）

[release](https://github.com/sgl-project/sglang/releases/tag/v0.5.22)Highlights明确指出speculative decoding+structured output的hybrid recurrent state错误。[43029](https://github.com/sgl-project/sglang/pull/43029) exact merge `0acd93c35c2ae84bc2c5129d5d92916c77c45a70`，已读实际scheduler diff。2+1+2=5；正确性变化深入必要层。草稿验证接受量曾用于mamba track跨边界 → grammar可能再截断已接受token，快照需要用最终retained长度扣除verify前非草稿token → 状态提交点属于最终commit前缀而非中间accept统计。Owner建议`INFER-SPECULATIVE-DECODING`。

diff位置`batch_result_processor.py::_mamba_check_track_boundary`：有grammar_retained_tokens时以实际retained长度与num_non_draft计算num_committed，无该条件仍用accepted+1；prev由cur-num_committed得到。不是所有spec decode都会错，也不是仅换索引术语；错误可能使后续请求恢复错误recurrent state。PR10/10窗外，本窗release交付事件；未跑GPU回归，不能由代码与作者release声明认证全模型/后端支持。其余大段release只按Highlights与目录定位，不逐950PR审阅。

### FlashInfer v0.7.2rc5 / rc6 / post1（三个本窗事件）

[rc5](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.2rc5)、[rc6](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.2rc6)、[post1](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.2.post1)。compare分别39、9、56 commits（最后包含前两阶段，不相加）。仅对具名comm correctness [5652](https://github.com/flashinfer-ai/flashinfer/pull/5652)核描述、actual diff和回归范围，merge `1ad1ed9245f0417cba0011ae85a43488129cca35`。1+2+2=5；正确性变化深入必要层。LL residual/RMSNorm collective peer CTA未到rendezvous就访问分布式shared memory → 在peer store前加cluster_arrive/wait，保留post-store和lifetime barrier → 发布屏障不能替代peer存在/初始同步的先决条件。Owner建议`TRAIN-DISTRIBUTED-TRAINING`。

CUDA Graph changing rank-local inputs、cluster配置、PDL两模式是作者新增数值覆盖；不是本次跑过Blackwell/Rubin，更不证明各种collective通用。10/13 PR早于窗，本次只计release事件。其他型别/SM107支持和性能routing条目未披露改变长期选择的可比边界，不自动准入；rc6没有独立增加该家族贡献或评分。

### Transformers v5.20.2（2026-10-20 BJT）

[release](https://github.com/huggingface/transformers/releases/tag/v5.20.2)四项已读；[49688](https://github.com/huggingface/transformers/pull/49688) merge `d88946453f945ecdc7bc5cf4427084a5d6c215fe`，核description中的最小拓扑、底层操作与oracle测试。2+2+2=6；实际梯度正确性变化深入必要层。expert归约组小于全FSDP范围时，原正确的全批次梯度分母使FSDP2选择PREMUL_SUM；该NCCL bf16/torch≤2.13路径会归零 → 所有backend强制sum后本地divide，仍保留`set_gradient_divide_factor(fsdp_size)`，不是把正确全批次分母改成较小expert组大小。不能只验证loss有限或普通dense梯度。

具体条件为token dispatch且`tp_size < ep_size < fsdp_size * tp_size`；作者4×B300、torch2.13、fsdp4/ep2，BF16 expert grad norm旧0、新0.0889、FP32参照0.0887，并加对单设备整batch每expert梯度oracle。仅作者复现与提交，未本地运行/认证所有torch/NCCL。Owner建议`TRAIN-DISTRIBUTED-TRAINING`。另三项中multimodal输入原类型保留是局部兼容修正，不额外增加家族或泛化所有generate输入均正确。

### EverMind / EverOS v1.5.0（2026-10-21 BJT）

[release](https://github.com/EverMind-AI/EverOS/releases/tag/v1.5.0)，已读async inbox、embedding identity、health snapshot及session-lock extraction关键说明。2+2+2=6；可靠性边界深入必要层。memcell已写后请求超时曾取消后续extraction → timeout只约束写前锁等待/boundary LLM，写后extraction脱锁并shield → memory accepted/committed与派生episode完成必须分开，202或buffer已消费不是记忆可检索完成。Owner建议`AGENT-MEMORY`。

async_mode用SQLite durable inbox、同session顺序与跨session并发；有backlog的同步add/flush仍排队。交付失败标failed且默认不自动retry，理由是pipeline非原子；crash replay最多3次不是exactly-once承诺，7天清row需另保审计依据。queue有413/429和health信号，不把后台worker活着等同提取成功。另一明确修正是index登记embedding model、启动时比对model和dim，旧index首次补登记并不证明历史identity真实；probe失败则警告继续跳过width检查，不能称fail-closed验证所有向量。v1.5.1仅embedding query concurrency默认4→16与队列数字，不作为独立新机制候选；两版同家族，本窗两个非重复事实。[rc1→1.5.0 compare](https://github.com/EverMind-AI/EverOS/compare/v1.5.0rc1...v1.5.0)仅2提交（pre安装提示526、release bump527），不增加机制事件或候选数。

## 每周组来源覆盖

按注册表顺序打开官方入口；代码源用 GitHub 官方 releases API `https://api.github.com/repos/<owner>/<repo>/releases?per_page=30` 第一页与published_at（转BJT日期）核对，已跨过周窗下界即停止，不扫描普通PR全集。完整条数只表示返回目录数量，不是本窗候选数。GitHub日期均为实际published_at，不用tag名推日期；API为空且仓库明确无release时只说无release，不说无研究。所有必要原文读取都轻量看当前页的纠错/撤回信号，未见影响上述命题的显式撤回，不主张全站无纠错。

| 来源 | 真实入口、覆盖与停止点 | 结果 / 缺口 |
| --- | --- | --- |
| SRC-MISTRAL | [News](https://mistral.ai/news/)，本窗2篇，读至10/15窗外；Voxtral3 10/20，NVIDIA engineering 10/21 | 核心已读；Voxtral属STT/LLM/TTS streaming组合，未披露新训练机制/受控系统消融，不自动准入；工程合作为暂缓科学应用，不采用 |
| SRC-AI2 | [Papers](https://allenai.org/papers)首10条只有年份且非可靠日期序，转[Latest research](https://allenai.org/research)读到10/14；本窗LitPivot、OlmoEarth1.3、crop benchmark、FairStress | 已检查Latest本窗；FairStress必要证据见上；其余应用/科学写作排除，不借通用节点引入。Papers的全量日期覆盖未恢复，不把首屏当零，不声称所有paper均覆盖 |
| SRC-BLACK-FOREST-LABS | [Research](https://bfl.ai/research)列3项，最新2026-03-03，整页无分页 | 本目录无窗内研究项；不外推模型菜单发布日期 |
| SRC-PHYSICAL-INTELLIGENCE | [主页](https://www.pi.website/)完整研究链接列表，最新10/13，其后4/16；[Research](https://www.pi.website/research)7题名均与主页旧项对应 | 已检查；本目录无窗内项 |
| SRC-WORLD-LABS | [Research & Insights](https://www.worldlabs.ai/blog)Research+News列表，最新9/28，整页无分页 | 本目录无窗内项 |
| SRC-SSI | [Updates](https://ssi.inc/updates)3条，最新7/26，读完 | 无窗内项 |
| SRC-REFLECTION-AI | [Blog](https://reflection.ai/blog)两条日期，最新10/05 Beam；featured同一发布；News重定向[Newsroom](https://reflection.ai/newsroom)首9条最新7/14，跨过下界不Load more | 已检查；无窗内研究项 |
| SRC-AMI-LABS | [Updates](https://amilabs.xyz/updates)一条3/10 launch，读完 | 无窗内项 |
| SRC-THINKING-MACHINES | [Connectionism](https://thinkingmachines.ai/blog/)7条，最新7/31，读完 | 无窗内项 |
| SRC-PRIME-INTELLECT | [Blog](https://www.primeintellect.ai/blog)10/19后接10/15，停止 | IPO候选，必要证据见上 |
| SRC-SAKANA-AI | [Blog](https://sakana.ai/blog/)10/23 Aquarium、10/21活动、10/20 QD-Rec，读至10/15 | 已检查；Aquarium核心ontology/governance/workflow无新执行机制或对照，排除；活动标题范围外；QD-Rec完整题摘/官方技术说明已读，固定推荐任务应用既有QD/bandit生成理由，未改变模型训练/Agent执行主线而范围排除，不通过通用搜索类比重引 |
| SRC-RECURSIVE | [Updates](https://recursive.com/updates)10/21 Flint与旧6/11研究，其他新闻不扩扫 | Flint核心How built已读：40B/2.5Bactive、4bit head+distill+Metal整decode融合；无可比消融归因，不把组合/厂商速度数字独立准入。与Daily10/22的2610.27273 FLINT检索论文不同家族，不误去重 |
| SRC-MIND-LAB | macaron入口重定向[MindLab](https://www.mindlab.im/)，[Publications](https://www.mindlab.im/publications)7条最新10/16，[Updates](https://www.mindlab.im/updates)最新9/22 | 两目录无窗内条目；不延伸旧论文 |
| SRC-SAND-AI | [组织](https://github.com/SandAI-org)研究链接与MAGI-1/MagiAttention/MagiCompiler releases API；0/13/2条，最新分别无release/9/18/7/01 | 无窗内release；组织updated10/24不等研究发布，不扫描普通commit全集 |
| SRC-EVERMIND | [主页](https://evermind.ai/)无日期发布目录，读research/product与页脚；日期搜索未恢复，转主页直接链接[EverOS](https://github.com/EverMind-AI/EverOS)，releases API22条，窗内1.5.0rc1/1.5.0(10/21)、1.5.1(10/22)，其后10/14停止 | 已检查有界发布替代；1.5.0必要证据见上；1.5.1并发调参排除；主页仍不支持研究论文全量日期覆盖断言 |
| SRC-METR | [主页](https://metr.org/)risk assessment列10/22与10/20；[Research](https://metr.org/research/)最新8/26 | 已检查；两个本窗家族必要证据见上 |
| SRC-PYTORCH | releases API30条，首v2.14.1 9/30 UTC、末v1.12.1，跨下界停止 | 无窗内release |
| SRC-MEGATRON-LM | releases API30条，首26.09-lambda.rc1 10/13，末core_v0.13.0rc3 | 无窗内release |
| SRC-DEEPSPEED | releases API30条，v0.19.8 10/20 15:21:47Z，其后跨下界 | 已检查release；具名正确性必要证据见上 |
| SRC-VERL | releases API16条全返回，首v0.9.1 9/20，末v0.1rc | 无窗内release |
| SRC-VLLM | releases API30条，v0.32.0 10/18 06:50:48Z，其后跨下界 | 已检查Highlights/Engine/Security/Breaking；SHM信任必要证据见上，不声称全814commits代码审阅 |
| SRC-SGLANG | releases API30条，v0.5.22 10/19 02:55:19Z，其后跨下界 | 已检查Highlights及章节目录，必要深入43029见上；非950PR逐条代码审阅 |
| SRC-TRITON-LANGUAGE | releases API7条全返回，首v3.8.0 8/28 | 无窗内release |
| SRC-FLASHINFER | releases API30条，v0.7.2rc5 10/20、rc6 10/22、post1 10/23 18:38:46Z（BJT10/24）；主v0.7.2 10/15窗外 | 已检查三个compare的39/9/56条提交题名；5652核心必要证据见上；后两组重叠不加计 |
| SRC-NCCL | releases API17条全返回，首v2.32.3-1 9/17 | 无窗内release |
| SRC-HF-TRANSFORMERS | releases API30条，v5.20.2 10/19 17:45:37Z（BJT10/20） | 已检查四项；bf16 EP梯度归零PR49688必要层见上 |
| SRC-KSERVE | releases API30条，首v0.21.0 9/25 | 无窗内release |
| SRC-RAY | releases API30条，ray-2.58.1与2.57.1均10/21，核心说明同两项 | 回调作用域修复+cloudCLI镜像，未给模型执行/资源边界增量，排除，不逐PR展开 |
| SRC-MCP | releases API9条全返回，首2026-07-28 | 无窗内release |

## 去重、范围关闭与恢复边界

对上述具名事件/版本、FairStress、QDRec2610.23470、Flint URL及关键PR号，在Daily19～24 README及对应_sources Markdown精确检索，未查到同事件有效审阅。Daily10/22的FLINT2610.27273为检索模型，与Recursive Flint不同；不能按同名去重。Daily25仍由root处理中，最终去重由root合并；不得据未命中字符串断言每日完全无遗漏。

QD-Rec [v1身份](https://arxiv.org/abs/2610.23470v1)与[技术说明](https://pub.sakana.ai/qd-rec/)已核，排除理由不是日期或低分，而是固定推荐应用不直接修正模型/执行机制。其v1提交`2026-10-16T13:49:22Z`；[DataCite](https://api.datacite.org/dois/10.48550/arXiv.2610.23470)登记方为arXiv DOI，`state=findable`，`registered=2026-10-19T02:41:56.000Z`，v1 Updated字段`2026-10-19T01:08:35Z`另保原名。[arXiv官方公告/发号规则](https://info.arxiv.org/help/availability.html)与EDT给最早界10/19 BJT08:00，registered给最晚界10/19 BJT10:41:56，整个区间同一BJT自然日，故公告日有限推断10/19，不拿submitted或Updated改名当实际发布时间；v2提交10/19，更新10/20，未见明确实质改变原主张的信号，不凭v2号展开逐字比较。不是10/20 blog首发。

Mistral Voxtral3的声学+语义end-turn与LiveKit三stage流式调度已读，未披露足以改变既有选择的机制对照，排除而不是只因品牌发布保留候选；未采用subsecond宣传或型号语言数作为长期知识。Flint同理：读核心后未发现可以与组合/硬件变化分开的新因果证据，排除不评分。其被称Eureka-generated不等可证自动研究增益。

按需来源没有独立发布批次/重大协议变化触发；本次只为已具名候选打开必要primary原件，不把它们升级为固定全站扫描。没有扫描Daily组或整月arXiv。

当前可执行新增来源检查及已列候选的必要原文层已处理；尚待root对所有候选作最终独立准入/owner/Books处置及实际写后复核。Ai2 Papers首屏无日期与EverMind主页无日期的局限保留隔离：不能支撑全目录Coverage或无遗漏保证；仅当取得目标周日期可过滤的官方目录或具名本窗研究线索时定点重开，不无限全站恢复。本文件不自行宣称Weekly完成，不修改Books/README/State/索引，也未stage/commit/push。
