# 2025-11-21 窄尾准入校准包

作者Dalton；2026-10-04T18:50:22+08:00。当前先交19个新增潜在问题和明确撤回负侧，非日级。此前8方向见[首批](ARXIV_FIRST_CALIBRATION.md)，未重读别日候选。这里完整题摘/决定性最小core实际可审，尚未确认首公开落窗，不评分、不采用性能数字、不请求Books写锁。

## 入口是否有界

API连续429/超时后停止同路径空追，官方advanced入口实际200恢复。初始title=LLM、Nov19→Nov20、submitted_date（最近）返回38/38，都是提交/修订发现，不是当天38篇。改original提交范围Nov19→Nov21（日期终点排除Nov21），系统query `LLM AND (inference OR GPU OR serving OR quantization)` 得19/19，Agent `agent AND (memory OR tool OR planning OR defense)` 得7/7；query完整参数和执行时刻在各HTML receipt。title多模态宽query首50/56混进一般diffusion/领域预测，停止不翻第2页；缩为VLA/title得6/6、flow matching/DiT/diffusion language得4/4。只相关机制读题摘，不把宽50或CL月表1527变全文/全题摘队列。词项Boolean如何被站点解析不宣称完美召回，实际标题有无关项即按语义收窄。

原入口：[系统](arxiv_system_advanced.html)、[Agent](arxiv_agent_advanced.html)、[宽多模态停50](arxiv_multimodal_advanced.html)、[VLA窄](arxiv_vla_narrow.html)、[生成窄](arxiv_generation_narrow.html)、[LLM最近修订定位](arxiv_title_search.html)。无关领域应用标题保留原表线索，不逐条实验关闭。

## 完整题摘及具体增量

原题摘：[系统4](WEB_SYSTEM_NEW_ABSTRACTS.json)、[Agent3/NorthPole](WEB_AGENT_NORTHPOLE.json)、[系统安全](WEB_SYSTEM_SAFETY_TAIL.json)、[VLA/生成4](WEB_VLA_GENERATION_ABSTRACTS.json)、[其余VLA4](WEB_VLA_OTHER_ABSTRACTS.json)、[生成/ES](WEB_FINAL_SCOPE_ABSTRACTS.json)。均精确v1原页，只有当前信号检查另注明；全文没有笼统称已审。

| 精确版本；Submitted原字段UTC | 原有约束 → 潜在实际增量 → 必要反侧/变化选择 |
| --- | --- |
| [2511.15898v1 Global Resolution](https://arxiv.org/abs/2511.15898v1)，Nov19 21:59:43 | 多draft OT指数变量不可解 → max-flow/polymatroid化为至多V变量凸问题 → 同一draft独立同分布、任意精度条件须核，理论optimal不等于真实推理最省时；100ms/token不是SLO收益保证。INFER-SPECULATIVE-DECODING潜力。 |
| [2511.15690v1 MoDES](https://arxiv.org/abs/2511.15690v1)，Nov19 18:48:27 | 单模态expert跳过在多模态损害效果 → layer-global modulation与两模态阈值、frontier搜索 → 需校准数据/阈值是否测试调优、保留比例与真实prefill/decode对照；不把现成组合或88%数字当机制。MODEL-MOE潜力，晚v2不反填。 |
| [2511.15503v1 DCC](https://arxiv.org/abs/2511.15503v1)，Nov19 14:58:16 | Host/PIM要求相反bank布局 → data rearrangement和compute loop partition共调、后端抽象 → 需包含搬运端到端成本、性能预测误差和GPU/模拟后端可比，不采用加速数。服务LLM kernel/编译在主线。 |
| [2511.16046v1 JEDIS-LLM](https://arxiv.org/abs/2511.16046v1)，Submitted on 20 Nov 2025（秒字段未读，不填） | 短音频训练不自然支持长流式speaker identity → chunk-wise Speaker Prompt Cache即时更新加word-level监督 → cache错误累积、登记speaker条件和offline级联不等价对照须核；不是转录应用换榜。MULTIMODAL-REPRESENTATION潜力。 |
| [2511.15950v1 NorthPole](https://arxiv.org/abs/2511.15950v1)，Nov20 00:53:44 | 离片权重/KV搬运和PP批量延迟 → 全片上状态使层间仅传embedding、片内/片间流水线与量化/容量联合约束 → context×users消耗KV片上容量，非大模型无限扩展或GPU普遍替代。最小III-A/C与C2C核心实际读，见[core](WEB_VLA_THEORY_CORE.json) L100–123、155–170；SiLQ额外训练不能省略。INFER-GPU-MEMORY路由只待具体owner选择，不由硬件名强造缺口。 |
| [2511.15757v1 RGym](https://arxiv.org/abs/2511.15757v1)，Nov19 09:12:47 | kernel APR依赖不现实oracle → call-stack/blamed-commit定位与真实本地评价 → 须核定位信息可得、过滤样本与重试/成本预算；Linux kernel不是GPU kernel，PLATFORM-EVALUATION-SYSTEM的oracle盲区潜力，不因领域/局部结果关闭。 |
| [2511.15203v1 IPI Defense SoK](https://arxiv.org/abs/2511.15203v1)，Nov19 07:47:30 | 非自适应测试可能掩盖防御失败 → 六类失败原因与针对具体框架的自适应攻击 → taxonomy本身不够；threat model、tool权限、攻击/防御预算配置必要。安全局部反证保留，不能授普遍防御无效。 |
| [2511.21726v1 SUMER](https://arxiv.org/abs/2511.21726v1)，Nov20 22:45:57 | 预定压缩丢失未预知问题所需信息 → RLVR按目标检索未压缩历史 → LoCoMo训练/测试、搜索调用和full-context预算控制必要；不能把43%宣传变一般memory定理，ID晚号与提交字段并存不补public。AGENT-MEMORY潜力。 |
| [2511.16108v1 SkyRL-Agent](https://arxiv.org/abs/2511.16108v1)，Nov20 07:05:19 | naive async batch有多轮长尾与工具导航成本 → dispatcher及AST-search训练机制 → 需调度究竟新增什么/对照预算，AST工具收益与异步速度分离，不将backend列表当贡献。TRAIN-DISTRIBUTED-TRAINING/AGENT-PLATFORM唯一owner待选。 |
| [2511.15915v1 AccelOpt](https://arxiv.org/abs/2511.15915v1)，Nov19 22:49:37 | 新accelerator手工经验稀缺 → 从slow-fast kernel对整理optimization memory → 需记忆产生/复用hook、评测kernel交叉污染、正确性与成本统一；不是泛称self-improving即准入。AGENT-MEMORY潜力，Trainium负载而非CPU软件kernel。 |
| [2511.16449v1 VLA-Pruner](https://arxiv.org/abs/2511.16449v1)，Nov20 15:16:09 | VLM语义salience剪掉动作相关信息 → semantic prefill与平滑估计action decode attention双准则 → temporal失配、action leakage、同计算预算任务成功率必要；晚月表标题不反填v1。MULTIMODAL-EMBODIED-VLA潜力。 |
| [2511.16203v1 VLA-Fool](https://arxiv.org/abs/2511.16203v1)，Nov20 10:14:32 | 单模态扰动漏掉指令/感知错配 → cross-modal攻击对OpenVLA/LIBERO行为的局部反证 → 需白/黑盒权限、扰动约束、物理/模拟界限及失败定义；不能授现实robot泛化失效。安全必要反侧保留。 |
| [2511.16233v1 FT-NCFM](https://arxiv.org/abs/2511.16233v1)，Nov20 11:04:14 | 数据价值不均且policy蒸馏绑定模型 → causal attribution与programmatic contrastive verification指导模型无关生成数据 → causal如何识别、验证访问labels和跨模型迁移控制必要；小数据比例不是自动可靠。TRAIN-DATA潜力，不取科学应用。 |
| [2511.16175v1 Mantis](https://arxiv.org/abs/2511.16175v1)，Nov20 09:30:23 | 直接预测高维视觉占backbone容量 → meta-query/DiT foresight解耦、current-state residual → 需latent action是否可辨识、language监督/数据配比与head消融；未来视觉≠事实状态。MULTIMODAL-EMBODIED-VLA潜力，不取榜值。 |
| [2511.16166v1 EvoVLA](https://arxiv.org/abs/2511.16166v1)，Nov20 09:08:33 | coarse阶段指标被shortcut → contrastive hard-negative stage reward/pose探索/选择记忆 → 核Gemini负例与阶段标签混杂、物体pose可得、三模块收益分离；组合本身不准入，局部stage hallucination反证有潜力。 |
| [2511.15605v1 SRPO](https://arxiv.org/abs/2511.15605v1)，Nov19 16:52:23 | 二值失败丢过程信号 → batch内成功轨迹与world latent作进度self-reference → 无成功样本时定义、world encoder监督/进度错误和同预算对照必要，不把extra-supervision-free当无外部模型。MULTIMODAL-EMBODIED-VLA潜力。 |
| [2511.16599v1 时间loss加权理论](https://arxiv.org/abs/2511.16599v1)，Nov20 17:55:21 | 实践time weighting常无明确理论权限 → state/time-dependent Bregman与linear generator、time分布条件 → 核正权/regularity与conditional-marginal目标等价，不推有限容量模型任意加权等效。MULTIMODAL-GENERATIVE-PARADIGMS潜力；无实验不关闭理论。 |
| [2511.16156v1 PPCL](https://arxiv.org/abs/2511.16156v1)，Nov20 08:53:07 | 每剪枝配置需重训 → interval probing与交替distill同训练覆盖深宽不同ratio → 核probe一致性、训练预算和各ratio质量/推理成本，不把参数减半当wall-time减半。MULTIMODAL-GENERATIVE-PARADIGMS潜力。 |
| [2511.16652v1 EGGROLL](https://arxiv.org/abs/2511.16652v1)，Nov20 18:56:05 | ES每worker稠密扰动/forward预算高 → 随机低秩扰动而population平均高秩更新 → O(1/r)的度量/假设须核，低秩增量成本不等于整个base模型forward变O(r(m+n))；对GRPO样本/计算预算和integer训练边界需保留。TRAIN-PRETRAINING潜力，不因backprop之外关闭。 |

JEDIS原web返回未展示history秒字段，当前只保留实际页头自然日期，不补时刻；已删除作者草稿中未核的秒值，该值不得作为原始证据。以上均潜在，不是本窗确定19家族。

## 纠错/撤回及其余有限停点

[2511.06247 Tetris当前](https://arxiv.org/abs/2511.06247) 原L8明示withdrawn，L23内部publication approval政策，history v1 Nov9 06:14:23、v2 Nov19 05:07:00 UTC withdrawn。不评分、不采用旧稿、不入Books；不是技术反证，不能说性能被证明无效，亦不由submitted授窗内撤回。和首包Mind the Motions均请root实际独立核，不读旧稿争取准入。

[FMPlug](https://arxiv.org/abs/2511.16520v1) 完整摘要涉及foundation flow先验warm-start/Gaussianity regularization，image restoration机制与scientific IP分开，非因包含科学就整篇关闭；原增量目前需最小方法澄清regularization超出组合与约束，普通待办不装外部受阻。[FreqFlow](https://arxiv.org/abs/2511.16426v1) 完整摘要为传感器交通多变量预测专用spectral linear residual建模，无foundation/LLM系统机制或改变其设计的证据，拟范围关闭不是89k参数关闭。原日期未定、不为明确范围关闭再追日期。

系统余项RAG direct-image vs summarization、genre probe、DRP已读完整摘要，需具体判断笔记后交代表性校准；COPYCHECK v1两次Cache miss，当前v2完整摘要只能恢复身份/潜力，不能反填v1，改curl一次为有限版本恢复，不同空路径停止。

当前普通：上述四项最小贡献澄清/版本恢复、有限原日期恢复、source表同步；Nano确定家族独立准入后受影响安全core/具体owner比较。校准前继续无关筛选，不展开所有未定日期实验/owner。无共享写入或Books锁。

## 最小澄清后五项增量（不改前记录）

原[含糊完整题摘](WEB_AMBIGUOUS_SYSTEM.json)、[最小方法](WEB_AMBIGUOUS_MINIMAL_CORE.json)、[FMPlug/genre追加core](WEB_AMBIGUOUS_FINAL_CORE.json)、[sharp constraint](WEB_FMPLUG_SHARP_CORE.json)、[COPYCHECK精确v1](copycheck_v1.html)均实际读。这五项潜力保留，不因local、旧组件或无全实验关闭；新增后本包24潜力，连首包8共32，不是32确定当窗候选。

- **2511.16520v1 FMPlug**，SubmittedNov20 16:35:57 UTC：simple-distortion图像生成prior的问题不是仅换领域。§3.1实际把接近观测插入可学习time，避免t0 shifted-Gaussian偏离训练薄壳；§3.2将过软negative-log regularizer改为有slack的norm-shell投影约束。明确潜在选择变化：foundation FM作为图像prior时，warm-start位置和源分布约束要共同匹配。径向shell约束本身不证明全Gaussian分布，保留scalar calibration额外4000采样预算与surjectivity未证；只取一般图像生成prior，不扩few-shot科学IP实验。MULTIMODAL-GENERATIVE-PARADIGMS潜力。
- **2511.16654v1 text-vs-image RAG**，SubmittedNov20 18:56:49 UTC：将图像先摘要成文本可能丢失检索所需视觉信息，40 QA财报局部比较给直接embedding保留视觉的负侧；可能改变原始模态索引与summary派生物取舍。金融任务动机不自动范围外。需两embedding模型、六LLM/summary/evaluator预算、40问题依赖和2-vs-3 approaches原表述差异，不能采用数字/一般所有summary劣于image。AGENT-RAG潜力。
- **2511.16540v1 genre probe**，SubmittedNov20 16:53:12 UTC：超token的genre chunks在Mistral激活可被浅probe读出，提供局部表示证据；不同两个数据/随机权重control不能被同义“classification应用”抹去。原§3 L62–91实际先生成669prompts→GPT4分段标注→人去错、mean activations与random-weight对照、80/20划分。L88声称胜random即可排除spurious/证明true representation过强：该control不排除train/test同源段落和lexical feature混杂，也未作causal干预。保留局部可解码潜力而不采用causal解释，WORLDVIEW-REPRESENTATION路由。
- **2511.15389v1 DRP**，SubmittedNov19 12:35:40 UTC：原§2.2 L83–98确实把固定handcrafted difference维度改为自主生成/定义，并同模型reflective validation后供personalized generation；这是derived user state的细粒度生成hook潜力，不仅“System2”术语或review BLEU提分。same-model validator非独立groundtruth，R1-distill/Qwen在相同参数数目不自动同训练/预算；counter-user selection/privacy和额外调用条件须核，AGENT-MEMORY潜力，未采用数字。
- **2511.15192v1 COPYCHECK**，SubmittedNov19 07:24:22 UTC：两次v1网页Cache miss后原curl200实际恢复，完整题摘精确v1已读，v2 Nov20 10:01:24只保留版本history，不当important revision。uncertainty-guided file分段/无监督聚类试图摆脱经验阈值，可能改变membership inference的标定依赖；需训练成员真值、文件split污染、聚类label指派/访问logit及假阳性，不把uncertainty或balanced accuracy推成copyright法律证明。PLATFORM-EVALUATION-SYSTEM潜力。

FreqFlow具体范围关闭请求不变。EvoVLA官方仓库现news `[2025-11-27] Paper released on arXiv`（[原恢复](WEB_DATE_RESTORE_ARXIV_02.json)和[原页/core](WEB_AMBIGUOUS_FINAL_CORE.json)）；与submittedNov20并存，不证明任何其他渠道没有更早首公开，亦不能由Nov27说明自动授Nov21窗外。日期只待同版本official first-public/完整界，有限追查不扩全部实验。
