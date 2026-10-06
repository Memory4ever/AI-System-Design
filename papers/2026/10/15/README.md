# Daily Research — 2026-10-15

**规范：** V3
**窗口：** 2026-10-14 ～ 2026-10-14
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-15T09:40:12+08:00

## 1. 结论

本次只处理北京时间10月14日完整自然日；星期四不生成Weekly，两项已暂停的历史补查均未恢复。有限发现与贡献筛选形成24个唯一家族：15篇arXiv首次公告论文、9个官方工程家族；后者包含同一家族的多次合入，不是9篇新论文。必要证据与Books逐项处置已落实：18项整合、4项已有覆盖、2项仅报告；13个章节共22段新增正文均经非写入者实际写后复核。报告六部分独立验收通过，无普通可执行待办；完成指处理到合同允许的安全终态，不把已隔离来源缺段说成全覆盖。

主要研究价值不是排行榜：进度奖励可能改变策略目标；参数或函数等价不保证恢复后训练轨迹等价；事实性、攻击检测与世界模型评价都可能测到错误代理；推理和训练优化必须同时保留状态、质量及完整成本。作者报告的实验与公开代码，不等于本项目复现或生产验收。

来源检查有明确边界：arXiv宽分类条目只作有界主题导航，不变成逐项全文队列；机构组织页和commit列表也只是发现入口。动态研究目录、无首公开日期的目录及搜索截断在§5隔离，不支持“无遗漏”或全覆盖声明。

## 2. 来源覆盖

实际查询、分页、停止位置和筛选依据分别保存在[全球机构](../_sources/daily-20261015/global.md)、[中国机构](../_sources/daily-20261015/china.md)、[arXiv](../_sources/daily-20261015/arxiv.md)。仅检查每日组及这些材料直接触发的必要原件，不扫描每周组。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research index](https://openai.com/research/index/)9个日期卡，最新10-07，窗前前缀停止，不Load more | 已检查 | 只支持可见日期段 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)10项，10-12两项后逐至窗前，未继续See more | 已检查 | 不授隐藏条目保证 |
| SRC-GOOGLE-AI | [DeepMind Blog](https://deepmind.google/blog/)10月5卡及Research Blog页1的10-14三篇至10-07；Publications页1至09-16；Pubs页1只有年份/venue | 受阻 | 已读博客可判断；Pubs缺当日相关公开日期切片 |
| SRC-META-AI | [Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)页1十个10-14医学/健康应用标题至10-13，窗前停；Research/Blog空提取及有限替代请求失败 | 受阻 | Publication相关段已处理，不能代替Research/Blog缺段 |
| SRC-QWEN | Research动态壳及一次浏览器失败；组织首10定位具名仓库；qwen-code本窗commit两页20＋19，第二页不足20停止，只有主题核心进入贡献筛选 | 受阻 | Research日级目录未恢复；39个commit不是39篇论文。已查载体不授全组织无研究 |
| SRC-DEEPSEEK | [News/Research](https://www.deepseek.com/news/)News5条最新09-10、Research10条最新06-24，窗前前缀停止 | 已检查 | 限当前目录段 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26项窗前；kimi-code首20条commit以两窗后→5窗内→窗前夹窗，release首3。3个主题核心排除，累计旧changelog不搬日 | 已检查 | 只支持已查入口；本窗release不把旧事件重算 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)网页、真实JS/API及根浏览器有限恢复未取回日段；UniRL本窗6个commit及release2条，必要merge原件已恢复 | 受阻 | Research“全部”本窗日期段隔离，不称零论文 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)时间排序首段最新08-26、发布说明窗前；GLM-OCR本窗1个commit及release首5 | 已检查 | 已核下载修正不等于caller/tenant鉴权 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)Newest页1/13、20/246，最新09-28；Blog日期段窗前；VeOmni本窗1个commit、release首5 | 已检查 | 不扫246篇旧论文或13页；SAC局部实现未达贡献门槛 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)页1/2的10条，最新05-09，窗前停；具名仓库本窗commit返回空数组、唯一release窗前 | 已检查 | 不扩大为全百度无论文 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)8个Paper日期均窗前；15个Blog无目录日期，首原文09-27；MiMo-Code本窗3个commit及两条旧release | 受阻 | 其余14个无日期Blog不支持完整日级覆盖，未任意搬入本窗 |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog)、中文Blog及Agent Tech Blog日期前缀均窗前；OpenAgentCore本窗15个commit核心、release首5 | 已检查 | 普通UI/诊断修复具体排除，不作模型新机制 |
| SRC-ARXIV | 官方Wed14 CL/DC日期段有界标题导航、LG/CV主题定位；模型/训练、推理/GPU、Agent、多模态/World/VLA四组主题补检及12相关分类同义查询首40标题，15个精确v1题摘和必要原证 | 已检查 | 查询截断与主题有界，不授全分类召回；385/76/862/479为目录条目数，723为查询命中总量，均非候选量 |

中国六来源窄窗共26个commit槽，6个准入事件归5家族、20项排除；Qwen另4家族。机构名、仓库推送、论文提交和正式公告不混算：本次15篇arXiv由官方Wed14公告确认公开日，页面Submitted13不改其归属。精确版本当前未见撤回标记；没有为证明无撤回而遍历版本史。

## 3. 候选与判断

以下各项公开日期均为2026-10-14；工程项是本窗main合入事件，不称PR首次提出日。评分顺序为Design Delta＋System Reach＋Durability；“已有覆盖”须对应具体正文，不由主题相似推断。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Qwen: preserve cancellation intent across session recovery #13436](https://github.com/QwenLM/qwen-code/pull/13436) | 2026-10-14 | 冷恢复必须区分用户Stop与机械中断；2+1+2=5 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md)恢复意图段 |
| [Qwen: settle journal-only parked Harness turns #14078](https://github.com/QwenLM/qwen-code/pull/14078) | 2026-10-14 | 已提交journal效果与缺失投影分责；2+2+2=6 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md#tool-observation-success-不等于-world-effect-commit)receipt后修投影、不重执行 |
| [Qwen: real-broker EventTransport fault rows #14109](https://github.com/QwenLM/qwen-code/pull/14109) | 2026-10-14 | owner交接ACK可丢wake，须逐source验重驱；2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md#long-running-与-external-events)；同家族含#14080 |
| [Qwen: reconnect disposal #13864](https://github.com/QwenLM/qwen-code/pull/13864) | 2026-10-14 | shutdown与异步transport安装竞争的局部修复；1+1+2=4 | 已关闭 | 仅报告：成熟生命周期规则的局部实现，不新增长期机制 |
| [UniRL: BAGEL layout/ratio checks #548](https://github.com/Tencent-Hunyuan/UniRL/pull/548) | 2026-10-14 | ratio近一不证明conditioning相同；同家族含#549多canvas；2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)trajectory identity中的#547反证 |
| [UniRL: preserve non-persistent buffer dtypes #596](https://github.com/Tencent-Hunyuan/UniRL/pull/596) | 2026-10-14 | 相同参数不覆盖构造派生状态dtype；1+2+2=5 | 深入完成 | 整合：`TRAIN-CHECKPOINT`，[Ch35](../../../../books/part-04-training-system/35-checkpoint.md)分片恢复后的构造态 |
| [UniRL: guarded CUDA MPS runtime #492](https://github.com/Tencent-Hunyuan/UniRL/pull/492) | 2026-10-14 | fractional记账、并发收益、数值资格分开；2+2+2=6 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER`，[Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md#gpu-sharing-的语义不同)；不采用未实现guard承诺 |
| [MiMo-Code: Stop settlement and exact resume #2618](https://github.com/XiaomiMiMo/MiMo-Code/pull/2618) | 2026-10-14 | abort、真实settle、释放运行权有序；2+1+2=5 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md#resume-的语义必须比有-checkpoint更具体) |
| [GLM-OCR: task file security #254](https://github.com/zai-org/GLM-OCR/pull/254) | 2026-10-14 | task产物allowlist阻任意读，不授caller授权；1+1+2=4 | 已关闭 | 仅报告：具体下载安全行为，不宣称多租户隔离 |
| [Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868v1) | 2026-10-14 | 同hidden world生成任务/验证/进度，终局势函数改变目标；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware](https://arxiv.org/abs/2610.18140v1) | 2026-10-14 | 按搬运/投影恢复成本选稀疏或dense路径；2+1+2=5 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Do Factuality Methods Make LLMs More Factual? Reproducibility and Fair Comparison](https://arxiv.org/abs/2610.18415v1) | 2026-10-14 | relevance、claim人口与拒答可改变事实性比较；3+2+2=7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Prompt-Injection Probes Learn the Conversation, Not Just the Injection](https://arxiv.org/abs/2610.18408v1) | 2026-10-14 | 位置/长度捷径与matched negatives揭示检测误报；3+2+2=7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving](https://arxiv.org/abs/2610.18451v1) | 2026-10-14 | 可复用execution/memory/communication结构与活跃资源解耦；2+2+2=6 | 深入完成 | 整合：`INFER-DYNAMO`，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [Revisiting Cauchy-Schwarz Norm Bounds for SDC Detection in LLM Inference](https://arxiv.org/abs/2610.18557v1) | 2026-10-14 | dense有效的低成本fault检测可能漏MoE gate；3+2+2=7 | 深入完成 | 整合：`PLATFORM-PRODUCTION`，[Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [A Distributed View from a Single GPU: RankLens for Distributed Training](https://arxiv.org/abs/2610.18009v1) | 2026-10-14 | 先录制通信再单survivor运行的有条件分析；2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Quota-Based Aging for Prediction-Guided Scheduling in LLM Serving](https://arxiv.org/abs/2610.17795v1) | 2026-10-14 | quota/debt限制aging晋升，不授有界墙钟等待；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](https://arxiv.org/abs/2610.18869v1) | 2026-10-14 | 质量处理与粒度、模型、微调阶段共同决定收益；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](https://arxiv.org/abs/2610.18826v1) | 2026-10-14 | 同action真实执行配对，运动跟随不等interaction正确；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)具体论证 |
| [Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization](https://arxiv.org/abs/2610.18085v1) | 2026-10-14 | 精确函数重参数化仍不保optimizer轨迹；3+2+2=7 | 深入完成 | 整合：`TRAIN-CHECKPOINT`，[Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning](https://arxiv.org/abs/2610.18862v1) | 2026-10-14 | 同prefix双prompt logit差缩短推理，额外forward计费；2+2+2=6 | 标准完成 | 已有覆盖：`MODEL-SAMPLING`，[Ch20](../../../../books/part-02-model/20-sampling.md)具体论证 |
| [Depth Memory（2610.18809v1）](https://arxiv.org/abs/2610.18809v1) | 2026-10-14 | RLS关联记忆压缩depth信息，不是token KV；2+2+2=6 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER`，[Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Refresh Schedule（2610.18695v1）](https://arxiv.org/abs/2610.18695v1) | 2026-10-14 | 相同刷新频率/次数不等相同optimizer比较；3+1+2=6 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [UniW(A)M（2610.18697v1）](https://arxiv.org/abs/2610.18697v1) | 2026-10-14 | 共享backbone仍保预测/动作interface与路由预算；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

## 4. 证据与知识整合

各论文采用精确v1；必要方法、关键对照、直接反证与配置边界见[arXiv证据逐项记录](../_sources/daily-20261015/arxiv.md)，实际owner差额与写入位置见[Books比较](../_sources/daily-20261015/books.md)。Source初审的11标准/4深入不直接冒作Books验收：确认差额后，对拟采用的机制、相关假设及关键反侧定点深入并独立核对，最终13项整合为深入完成、2项已有覆盖为标准完成；不重读无关附件或为了处置改分。没有进行代码复现或作者实验重跑。性能配置未披露处为Not Disclosed，不自行补齐；以下不采用摘要加速率或排行榜作通用结论。

### [Qwen: preserve cancellation intent across session recovery #13436](https://github.com/QwenLM/qwen-code/pull/13436)

本窗merge为`a46aee28e60fc80d8779a48a566ed80f90406fe9`；`b2d5f348…`是最终verification comment6161332598的作者运行pin，不能混称merge。受控daemon基线在已Cancel后仍可Continue发新请求，最终把human Stop与SIGKILL/infra interruption分开。读取并非跨所有调用方事务，真实channel-worker、生产provider及Win/Linux未证。Ch81在目标恢复权限论证后补入中断意图，保留来源未知时拒绝自动恢复的退路和身份维护成本。

### [Qwen: settle journal-only parked Harness turns #14078](https://github.com/QwenLM/qwen-code/pull/14078)

合入`006d48e9…`的公开核心和负向arms只让持有充分journal evidence的非Runtime调用修投影：已启动回答started，未提交回答never-run，不明/缺funnel仍decline。Team/Hook包装完整stack尚欠物理验收。Ch81已明确receipt先于模型、投影缺失先修而不重执行，以及not_started/failure/unknown分开；现有解释能承载该实例，无需重复增文。

### [Qwen: real-broker EventTransport fault rows #14109](https://github.com/QwenLM/qwen-code/pull/14109)

与[#14080](https://github.com/QwenLM/qwen-code/pull/14080)归同家族。RocketMQ5.5.1＋H2、替身Harness的owner handoff对照显示旧subscriber SUCCESS ACK后新owner丢该wake；unacked backlog与later notice是控制，不能泛称SQL自动恢复所有来源。Ch81增加source-specific redrive与ACK/完成分责；未采用多节点、outage或全部backstop已实现的保证。

### [Qwen: reconnect disposal #13864](https://github.com/QwenLM/qwen-code/pull/13864)

完整核心与局部fixture处理shutdown与异步transport安装/恢复竞争；十个deterministic in-memory case不是网络故障恢复证据。新增是局部资源释放修正，4分关闭、仅报告，不借成熟生命周期原则抬成跨系统新机制。

### [UniRL: BAGEL layout/ratio checks #548](https://github.com/Tencent-Hunyuan/UniRL/pull/548)

合入`0fbf3ad…`按row比KV length/RoPE/canvas；ratio警告是已有step前forward数值在update返回后报告，不是保证optimizer前阻断。错配时ratio仍近一的作者反例支持Ch33现有#547论点。另[#549](https://github.com/Tencent-Hunyuan/UniRL/pull/549)用per-group canvas生成、dense padding存储及replay trim，降低生成分辨率不自动降低轨迹存储。保留这些实现限制，不再为同一conditioning判断重复改书。

### [UniRL: preserve non-persistent buffer dtypes #596](https://github.com/Tencent-Hunyuan/UniRL/pull/596)

合入`d8a82c6…`的meta-init/restore必要代码实际区分persistent与non-persistent，按captured dtype恢复而非live低精度dtype。作者Qwen3/MoE、4096序列、BF16两backend对照支持构造态边界，完整硬件/重复人口未披露。Ch35把它融入tensor identity后的恢复推理，不以局部bit-identical报告认证任意模型或训练轨迹。

### [UniRL: guarded CUDA MPS runtime #492](https://github.com/Tencent-Hunyuan/UniRL/pull/492)

合入`0ac8bc3…`六个文件与PR描述有实质差异：实际config接受1～100 active-thread，没有描述中的dtype/scorer硬拒绝；external/排空等也不能按正文认定已实现。H20/535.247.01作者测量显示收益随实际forward batch及scorer瓶颈变化，低active半精度可能finite-but-wrong。Ch63仅采用数值parity与共享收益分别验收的局部反证，不发布默认安全配置或通用吞吐数字。

### [MiMo-Code: Stop settlement and exact resume #2618](https://github.com/XiaomiMiMo/MiMo-Code/pull/2618)

采用当前merge`002cb4c…`，不是旧网页索引body。实际settlement先abort再不可中断等待真实promise、consume后传播原interrupt；started/input boundary与确切resume target避免直接删除已完成结果。延迟文件写fixture的writes=1只是本地受控证明；没有settlement timeout，忽略abort的工具仍可无限等，远端crash效果也不原子。Ch81补入Stop/settle/释放运行权的顺序，不授exactly-once。

### [GLM-OCR: task file security #254](https://github.com/zai-org/GLM-OCR/pull/254)

合入`0288f96…`必要route/task_images/tests绑定completed task与manifest中PNG crop，并做路径、symlink及文件验证；POSIX与非POSIX保证不同。测试在无authorization/cookie下仍可读已登记crop，故UUID/manifest不是caller/tenant鉴权。4分因安全行为变化深入受影响内容后关闭；仅报告，不把具体下载修正升级成通用安全设计或跨租户证书。

### [Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868v1)

§2–3.3/B：任务输入、verifier与进度由同hidden world派生，prerequisite-gated势函数限制局部credit。`pass + λΦ(final)`刻意保留终局势，**不是policy-invariant PBRS**；单轨迹passing排序保持，不保证随机policy期望排名。Table5局部消融不等不同harness/预算的榜单公平。已融入[Ch33](../../../../books/part-04-training-system/33-grpo.md)：同hidden world进度构造及保终局势的目标变化。

### [SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware](https://arxiv.org/abs/2610.18140v1)

§3.2–3.4从GPU摘要选块，以copy、projection及span开销选择稀疏恢复或full fallback。重建是从checkpointed hidden state投影K/V，**不是重跑完整prefix**；hidden checkpoint存储/更新及位置处理细节不足，不能称全KV无损恢复。OPT6.7B、batch4、RTX3070Ti8GB笔记本的Needle对照已有质量损失；precision/output length/concurrency/SLO未披露。已融入[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：hidden checkpoint投影恢复与搬运/质量成本。

### [Do Factuality Methods Make LLMs More Factual? Reproducibility and Fair Comparison](https://arxiv.org/abs/2610.18415v1)

§3–6/Limitations的shared base/judge不等训练预算全匹配：FactGRPO只原预算1/10、其他方法有替代artifact，每方法单seed；relevance-filter后还有小幅显著正结果。可采用的反证是irrelevant但supported filler、claim/拒答分母及证据库会改变分数，不是“所有事实性RL无效”。人审只支持局部，relevance删除的正确率55%也限制过滤后的结论。已融入[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：supported与relevant分开、分母及normalizer。

### [Prompt-Injection Probes Learn the Conversation, Not Just the Injection](https://arxiv.org/abs/2610.18408v1)

§3–6/Table1–2：相同对话位置clean twin与无害同格式文本揭示position/length/format捷径；同classifier消融支持matched negatives的作用。但new-app改normal-traffic阈值后标准probe也会反超，exposure标签不等实际服从；“stopped”假设二审完美，费用是projection非运行实测。不能由AUROC或局部误报下降授生产安全。已融入[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：matched negative和正常流量阈值迁移边界。

### [FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving](https://arxiv.org/abs/2610.18451v1)

必要方法区分已初始化可复用结构与active EP资源，缩放仍受初始最大topology、通信重建、KV/权重移动及请求暂停约束。秒级transition改善不是逐请求无停顿或任意扩容SLO；局部model/hardware及负载条件见原证，不采用摘要倍率作普遍加速。已融入[Ch52](../../../../books/part-05-inference-system/52-dynamo.md)：parent域内执行结构复用、远端drain与物理页回收。

### [Revisiting Cauchy-Schwarz Norm Bounds for SDC Detection in LLM Inference](https://arxiv.org/abs/2610.18557v1)

必要fault injection对照区分dense GEMM与MoE router gate：低成本norm检测的覆盖不能从dense直接继承到routing。阈值、故障幅度、误报和输出后果须绑定同一故障合同；注入检出率不是生产SDC发生率，也不证明任意多点/对抗故障完备。已融入[Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)：dense与gate的故障检测覆盖分开。

### [A Distributed View from a Single GPU: RankLens for Distributed Training](https://arxiv.org/abs/2610.18009v1)

单survivor仍需目标执行的通信记录与依赖，在通信边界恢复结果/时序，不是零目标规模样本预测。模型/shape/数据依赖和contention变化限制复用，优化幅度还出现overprediction；局部timing error不能授所有job预测或收敛等价。已融入[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)：计时回放与recorded payload数值回放分责。

### [Quota-Based Aging for Prediction-Guided Scheduling in LLM Serving](https://arxiv.org/abs/2610.17795v1)

§II–V：history quantile给eligibility，完成短prefill admission积debt，oldest eligible long真正admit才清偿；decode、continuation和KV安全仍可延迟晋升。有限quota不证明有界墙钟等待。主结果是trace-calibrated模拟，FCFS/普通aging仍有更好的切片，预测误差会同时改变均值与两class尾部；不是live serving SLO。已融入[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)：aging资格与不可冲掉的quota/debt分开。

### [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](https://arxiv.org/abs/2610.18869v1)

§3–7在同demo/budget下比较weight/filter/condition和粒度，收益依赖VLA及微调协议。真实FR3的9.6→31.7%主要是plain simulation pretraining，quality conditioning只再提高约0.83pp且有任务反退；不能把总增益归质量标签。标签可能低估恢复动作，constant tag假说未独立因果验证，结果不授通用最佳recipe或安全。已融入[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：质量标签粒度、接入方式与微调阶段共同验收。

### [WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](https://arxiv.org/abs/2610.18826v1)

精确PDF主文及p8主表核对：同initial observation/低层action对真实rollout，分physical state、alignment、interaction与views验证，保success/failure人口。跟随手臂运动不蕴涵物体交互正确；multiview项也不是直接3D一致性证书。Judge、人审和bootstrap各有范围，不由榜单推架构因果或真实控制安全。已有覆盖于[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：已有Evaluation/分层Rollout Admission及Integrity Gate，实际同initial observation/action配对、visual完整性、reference EEF、invalid与action mismatch分账，不为新metric名重复增文。

### [Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization](https://arxiv.org/abs/2610.18085v1)

§2–5在精确正scale symmetry、共享随机性和optimizer假设下说明：同函数不等同更新轨迹，单独变换Adam moments仍不够；GELU pair不在该精确对称中。hard canonical restart与soft damping不同。主要证据是人为scale失衡的恢复，无编辑control不显示稳定改善，不能称所有LLM默认提质。已融入[Ch35](../../../../books/part-04-training-system/35-checkpoint.md)：精确对称下函数等价与optimizer轨迹等价分开。

### [DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning](https://arxiv.org/abs/2610.18862v1)

§2–6用同prefix brief/verbose两次辅助forward的logit差调大模型CoT，保原候选及EOS/think-end边界。更强steering或更大辅助模型会损accuracy；区间含零不是已证非劣。单B200、14题局部walltime不等fleet收益，少token不自动抵消双forward，事后“答案已出现”不能当在线oracle。已有覆盖于[Ch20](../../../../books/part-02-model/20-sampling.md)：已有Semantic Steering正文的同prefix双条件logit差、强度、词表身份、双forward费用和质量回退；小辅助模型是受测producer选择，不因缺案例名新增长段。

### [Depth Memory（2610.18809v1）](https://arxiv.org/abs/2610.18809v1)

§3–4通过per-token RLS关联记忆与inverse covariance压缩跨depth信息；不是token-sequence memory/KV。Unwinding和延迟rank-one融合减少traffic，但fixed depth state不等constant全部activation；保留residual的消融、额外state和缺失大规模对照都限制优势结论。已融入[Ch17](../../../../books/part-02-model/17-transformer-layer.md)：标准residual与RLS跨depth关联记忆及状态费用。

### [Refresh Schedule（2610.18695v1）](https://arxiv.org/abs/2610.18695v1)

§3–4在相同refresh次数下改变placement，FineWeb与LR有排序反转；cumulative staleness仍同时变化，不能称纯placement单因果。刻意undertrained设置、不同corpus/horizon和最高密度的反侧限制外推；59次refresh的dense实验没有证明同样反转。应采用完整schedule×LR比较边界，不给默认最优刷新频率。已融入[Ch28](../../../../books/part-04-training-system/28-pretraining.md)：完整refresh placement×LR而非仅频率。

### [UniW(A)M（2610.18697v1）](https://arxiv.org/abs/2610.18697v1)

§3–4.5的共享expert与eligible atomic expert保不同video/action条件mask；PAIR用目标chunk GT误差训练，不是zero-shot路由或成功率保证。Dense/MoE同steps不等同FLOPs；latency为chunk/16归一，PAIR的feature费用也不含全部encoding，不能直接换算控制Hz。保条件接口和完整费用，不授联合生成的精确因果或闭环安全。已融入[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：typed预测/动作接口、eligible experts与chunk路由费用；唯一owner归Ch26而非Ch25。

## 5. 缺口与下一步

普通可执行工作：无。扫描、筛选、必要证据、Books判断、全部实际正文写后复核及报告六部分独立验收已完成。

以下为本窗已隔离的外部来源终态保留项，不支持正面证据、Books采用或无遗漏断言，也不是“确认无论文”；各项定点重开条件如下：

- Google Pubs仅年份/venue，缺10-14主题论文的原始公开日期切片；取得官方本窗带日期目录或具名原件时只重开该段，不扫全年。
- Meta Research/Blog空提取及有限替代请求失败；Publication已恢复不代表这两个入口完成。需可读的本窗官方主题日期段。
- Qwen Research只动态app壳，浏览器一次失败；具名仓库已处理不填补模型研究目录。需官方dated Research片段或原始发布。
- Hunyuan Research“全部”页网页/真实API/浏览器均未取回日段；需要可读日期列表或官方同等目录，不能用JS build日期代替公开日。
- MiMo的14个余Blog目录无日期，首篇原文窗前并不证明其他项均旧；需官方dated目录或具名当窗原始发布，不能把全部旧Blog自动变新审阅队列。

arXiv实际主题查询有界且首片截断，不声称全学科召回；当前已入选15项必要正文均可读，未用可选代码不可得冒充Evidence受阻。工程PR描述与当前实现冲突已限定：#492的硬guard保证不采用，#254不授caller鉴权，#2618按当前精确merge而不是陈旧网页。两项历史cursor保持暂停，本窗未启动它们。

## 6. 复核

复核者：`/root/oct15_review`（独立于报告/Books写入者）
结论：通过

[独立复核R1–R9](../_sources/daily-20261015/review.md)覆盖全部24个准入家族的日期、具体贡献、评分及拟采用证据，全部18项实际整合、4项具体已有覆盖与2项仅报告，并验收完整六部分及保存后的完成态。另定点读7项Qwen纠错/安全排除核心，并按来源、主题和排除理由抽核Google、Moonshot、VeOmni、MiMo、OAC及arXiv共7个普通排除样本；未逐项复核其余UI槽、医学标题和未送入题摘的导航条目，不称全量排除验证。

独核已修正#13436 merge与作者验证pin混淆、MiMo评分维度、Tev把具体终局势选择泛化为所有dense reward必然改目标的措辞、Ch35缩放符号与step冲突，以及两条HTML fragment。实际正文保留旧方案、条件、费用、失败与回退，不把实验限定全部藏进末注；没有删除既有有效内容、改变Stable ID或新增知识owner。

V3结构/一致性校验、diff空白检查、19个变更Markdown的本地路径/新增围栏及Report Stable Node引用检查通过；这些不证明研究真值。工作树限定为本日报、5份本日来源/比较/复核记录与13个Books章节，原有正文无删除，index为空。未stage、commit或push，历史暂停与其他日期未改。
