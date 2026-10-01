# 2026-04-14 V3 恢复工作记录

当前恢复位置：真实Books整合为25项，均已非作者实际写后通过；09557/09687/10044及10495/10496/10539/10547见 `V3_APR01_FINAL_GAP_ADOPTION.md` 的实际写后节。六项早期必要证据与处置已收口；82项公开时间采用该记录末节明确限定的公告批次/原始版本联合推断，不伪称逐篇公告确证。第十九批其余十项由 `V3_APR20_FINAL_DISPOSITIONS_INDEPENDENT.md` 限定；10480仍有§4.2局部instruction-triplet匹配证据，不能改写为完全无content验证；10506/10517保留独立相关家族，不合并计数。仍需正式报告与日级独立验收，不标日级完成。以下较早数字和待审语态为过程记录，最终报告以现实际裁决汇总。

### 机构事件补查与本轮实际写后

09557、09687、10044三处两段机制正文已真实写入Ch48/23/45，并由apr01顺读实际增量与相邻论证后独立通过，见既有 `V3_APR01_FINAL_GAP_ADOPTION.md`；因此本日实际Books整合为25项，六项早期普通工作已达到对应必要证据/处置终态。正式候选日期与日级Gate未完成，不能计日报Complete。

Moonshot官方 [Kimi CLI 1.32.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.32.0) 的原始 `published_at=2026-04-13T11:39:51Z`，即北京时间19:39:51，确在本窗。实际release核心说明及[PR1843](https://github.com/MoonshotAI/kimi-cli/pull/1843)变更/测试显示混合text/inline image/audio/video共享100K字符工具返回预算，超大媒体部件丢弃并提示截断，另处理未知MCP类型避免turn崩溃。不是论文新模型或全部工具输出安全证明；这项公开实现是成熟工具预算/兼容性处理的局部修复，未分离新增长期设计边界或独立端到端有效性证据，前分母具体关闭、不评分、不写Books。保留它作为已触发官方事件的来源检查，不能因未入选而声称Moonshot当日零事件。其余不可恢复历史子入口仍单独隔离，不借一个release代表组织全覆盖。

### 六项早期普通证据收口：作者侧有限裁决与三处采用提案

以下实际源阅读补齐先前普通未决，仍待非作者有限采用/处置核及日级日期归并，不预支Books写入或Complete。有效未变化的早期源阅读复用，不重扫宽列表或无关附件。

- **09557 SPEED-Bench**：复用实际 exact-v1 §5–8/Table1/Appendix H的语义分布、drafter/batch、vocabulary pruning与配置审阅，`2+2+2=6`，实际缺口深入。Ch48有accepted length不等throughput、同sampling policy与runtime参数，但没有明确“随机token替换真实请求会改变proposal可预测性，裁剪词表也可能隐藏long-tail代价”。拟在审计参数清单之后补：真实输入与合成输入即使长度相同，也会改变draft预测难度和accepted prefix分布；因此应同时固定语义流量、padding/position协议与并发，让draft length随容量比较，而不是以较好acceptance代替端到端收益。词表裁剪降低proposal成本，却可能削弱跨语言和稀有token覆盖；须与未裁剪、相同输出质量/采样合同的目标路径比较，质量漂移或draft开销抵消收益时回退完整词表、短draft或target-only。受限实现涉及不同B200/多卡TP/EP与模型设置，默认greedy和Table1 temperature例外分开，client高并发GIL/padding也影响测量；不采用23%为普遍synthetic偏差或生产SLO。唯一owner `INFER-SPECULATIVE-DECODING` Ch48/Legacy44。
- **09678 NetAgentBench**：新增实际IV–VII-C阅读。STOP只是声明，配置命令有pending→stable/error与读回；FSM理论正确性依赖确定性和perfect-observability等模型假设，CLI parsing/收敛timeout实际可破坏观测，不证明实现已形式验证。VI-C声称4模型×5任务×25重复却另写300总/75每模型，算术不一致，不沿用该总数。VII-C显示早退同时降低完成度和可观测meltdown机会，token效率也可被早退抬高，不能以低meltdown率排名可靠性。`2+2+2=6`标准**已有覆盖**：Ch66的Outcome Witness明确动作不等环境事实、完整witness才有确定verdict；风险分解的environment opportunity与Long-session Stamina的提前终止删失，联合覆盖这一采用命题。保留网络state-machine受限案例，不新增同义正文；作者精确run分母冲突单独限定，不外推动态网络/生产成功率。
- **09687 Grid2Matrix**：实际v1 §2、§3.1–3.2、§4.2、§5.1–5.2。512×512程序网格、cell/exact两指标与冻结VE浅层probe构造diagnostic；相同1024 patch token下probe能读出的空间信息不保证端到端生成能表达，patch边界邻近密度非单调；更大decoder可能改善答案却降低VE probe，反之亦然。不能唯一归因projector压缩、对齐或distillation，§5.2只是解释假说。`2+1+2=5`，actual gap深入：Ch23现讲projector瓶颈、几何稳定≠可删除，但未区分“信息在encoder可读”“经融合能访问”“输出正确表达”。拟接在encoder+projector瓶颈段后两段：端到端细节错误不直接证明encoder没看到；用冻结表示的受控readout、融合访问和真实输出分开检查，并把同patch数/密度/边界与cell/exact分别出账。probe还需新监督/训练、只提供一种readout可行性，不证明backbone能调用或部署可零成本恢复；不以扩大encoder或压缩token单一修复，精细位置场景可保留坐标/高分辨率或局部readback，通用语义任务继续原接口。唯一owner `MULTIMODAL-REPRESENTATION` Ch23。
- **09712 LAST**：补读v1 §4.1/4.3、Tables4–5及此前§2/3。Qwen2.5-VL-7B、SFT/GRPO各训练预算与rollout设置固定；multiple-choice与relative-error≤0.25的metric题不可并为通用几何真值。Table5 No-tool SFT移除训练输出，而Text/Image-only从完整训练模型在inference遮一路，两者不是同一种干预；Full也并非每格胜单一路（SPBench-SI Text-only66.90>Full66.76）。§2提示试验的direction/text与metric/image差异不能推广“所有工具同时返回两种总更好”；阶段ablation也不能消去教师数据/训练预算与skill组合的混杂。`2+1+2=5`标准**仅报告**，保留返回表示与consumer/workload条件的受限新证据，而不采用全套skill训练为长期统一路线或bestmodel排行；Ch78 typed output及Ch23 semantic compatibility不因此获得新保证，暂无必要Books改动。硬件、precision、serving concurrency/SLO未由必要段建立，Not Disclosed；未复现。
- **09870 Relational Preference Encoding**：实际v1 §3–6与当前v2顶部Erratum（2026-07-16修订，窗外纠错只限制当窗v1采用，不另算April事件）及官方版本页。v1固定chosen-first的95.2%、pairwise probe84.5与pointwise21.75不能采用：current erratum分别定位presentation-order prior与orientation/pair-partner跨split泄漏，更正为antisymmetrized63.9、pair-disjoint56.5/54.2，并撤销inverted-polarity finding，不是整篇官方withdrawn。split audit看不到order prior、swap/antisymmetry看不到pair leakage，两项需分别验证；小的paired优势不能沿用“超过reward model”headline。`3+1+2=6`纠错深入，**争议/暂缓**：隔离v1中心定量与原泛化结论，不进入Books或Existing。现公开纠错足以拒用headline，但全audit的后续稿仍in preparation；可重开材料为该evaluation固定source-item split、order-balanced/antisymmetrized指标与公开审计artifact。不是普通未读工作，不索取无关新稿全文或遍历全部版本史。
- **10044 LoopGuard**：实际v1 §4–6、§5.3的KV集合与§6.3–6.5对照。LoopBench主动诱发递归/重复，greedy、Tmax2500、三次相同deterministic runs不当独立seed；loop criterion含达到cap，不能把更短输出自动称truth更可靠。W256多信号、K-of-3/持续性、warmup/cooldown触发anchor+sparse+tail-cleaned KV pruning，反复触发提高aggressiveness；这是改变保留历史的lossy干预，不是exact cache reset或解决所有重复。§6.5与always-on/p1-only的受限控制支持事件时点和组合线索，§6.3单QA F1守护不证明广泛语义保持。`2+2+2=6`实际gap深入，拟Ch45在workload-aware eviction前：固定预算或attention importance在正常生成时成本清楚；若生成本身进入自强化尾部重复，单纯保留高attention状态可能保住坏轨迹，可由持续低多样性/重复/停滞的组合线索提出有界修剪，保prefix/稀疏长程/清理后近期，再cooldown继续。selector不拥有正确性判断；引入误触正常格式、丢指令/证据、监测和重建成本，必须同时测loop与任务质量。原文Qwen3-1.7B/Llama3.2-1B、A100、B1024、anchor32和诱发协议不推广自然loop率/生产SLO；长格式合法重复、信号不明或质量退步时保留FullKV、静态window或直接中止/重试。唯一owner `INFER-KV-CACHE` Ch45/Legacy41。

### 当前续跑位置（2026-09-27T18:39:14+08:00）

当前已有16项真实Books整合并通过非作者写后；这包括10180/10187两项Ch49正文，具名写后见 [第十四批非作者记录](./V3_APR02_FOURTEENTH_FIVE_ADOPTION_AUDIT.md)。第十五批10072仅报告、10091日期/身份隔离、10134中央保证窄争议、10311具体前分母关闭均已由apr02实际核必要源通过，见 [四项有限审计](./V3_APR02_FIFTEENTH_FOUR_ADOPTION_AUDIT.md)。以下较早的14项/待非作者语态是过程历史，不覆盖本段；没有新增日级Complete。

第十六/十七批七项与第十八批六项的必要处置已通过有限非作者复核；10352/10403已真实写入Ch75/29机制正文并由apr01实际写后通过，因此当前真实整合为18项，整日仍未完成。仍需必要裁决的14项为10480/10493/10495/10496/10500/10506/10508/10511/10516/10517/10539/10546/10547/10556；10506/10517的家族关系须在证据收口时确认，10493只补决定处置的最小范围。不能把325标题或1334原始身份重新变成全文队列。来源/日期、最终分母与独立日级验收仍待完成；恢复或压缩后实际重读AGENTS及当前合同，不以本checkpoint替代。

### 第十八批必要证据与两项具体 owner 提案

写后同步：10352的Ch75 typed-retention段和10403的Ch29 prompt-loss→gradient-route段已真实落地，apr01实际写后通过；两项为整合，不再保留普通写入待办。10367原先未定位的“2D lip某项更好”改判不采用，精确非全面胜出反例采用Table2 ALiBi ASE .584高于ours .581。其余有效证据保留。

本批复用实际已读的完整题摘，仅补采用命题需要的官方精确v1方法、对照与限制；不全附件、不比较全部修订。六项处置及两项真实正文写后已通过apr01，见[V3_APR01_BATCH18_INDEPENDENT](./V3_APR01_BATCH18_INDEPENDENT.md)；不是日级完成。

- **10333 Zero-shot World Models**：[v1](https://arxiv.org/html/2604.10333v1)，实际Sx1、Sx6.SSx1、Sx2.SSx1、Sx3。第一帧完整、第二帧只观察随机约10%patch，以MSE重建第二帧；双帧各45%/90%等控制支持受限非对称表示分支。perturb→compare→aggregate用假想patch位移、预测差和flow/threshold组成readout，不等真实action干预或物理因果SCM。170M/1B、256²/patch8、150～450ms间隔及BabyView/Kinetics/BVD支持作者的zero-head probing结果；不同readout不证明比较模型没学到对应表示。`2+1+2=5`标准仅报告：保留预测器与readout可分离的受限机制，不将稀疏未来观察条件提升为可控world-model guarantee，未新增完整因果世界建模结论。
- **10352 ClawVM**：[v1](https://arxiv.org/html/2604.10352v1)，实际§3全部必要设计、§5.2、§7。typed page含stable ID/scope/provenance/minimum fidelity；在ingestion/update预生成full/compressed/structured/pointer，budget时不重新调用LLM压缩。先装hard minima、再按marginal utility/token贪心升级；最小集合不fit必须暴露pressure，不能继续悄悄降级。writeback为typed staging→schema/provenance/scope/non-destructive validation→scoped commit，journal保留reject原因。12 real traces replay、30 synthetic、20 live单session；效用排序相对LRU两者均零fault，没有证明quality advantage；schema验证不证明事实真、replay工具不是真实effect。`2+2+2=6`，具体Books gap深入。当前Ch75已经解释typed registry、不同retention operator和原文authority，却未解释预生成分辨率、hard-minimum fit与budget阶段确定性选择的责任分离。拟refine既有typed-registry段落，补该分支与budget不fit/variant stale/utility proxy限制；不是新增ClawVM论文摘要。owner=`AGENT-CONTEXT`，Ch75/Legacy71，写前须非作者核验。现有mutation/commit段已覆盖writeback authority，故不重复增写transaction正文。
- **10367 Talking and Listening**：[v1](https://arxiv.org/html/2604.10367v1)，实际§3.2.2、§4.1/4.3.1。MHGK为共享时间尺度的RoPE加head-specific bounded Gaussian penalty；有限α不是strict local window，σ很大bias趋0。2D/3D RoPE、ALiBi对照支持局部temporal-bias分支，2D lip metric仍在某项较好，不是全面胜出。16A100/bf16/globalbatch32、base/new-module不同LR及两训练阶段；新增audio-role/time-scale控制不证明真实交互闭环或causal responsiveness。`2+1+2=5`标准仅报告，保留soft locality/global context取舍，不采用硬窗口或普适同步保证。
- **10387 Symbolic GPU Thread Mapping**：[v1](https://arxiv.org/html/2604.10387v1)，实际最小§3.1、§4.1.2、§5.3/5.5。ICL坐标示例提出Python解析映射、有限域exact-index/任意order bijection检验、然后一次生成摊销；百万点比对仍不是全整数证明，正确映射也可能使用linear search而代价更高。A10040GB dummy atomic-increment与含idle的gross NVML不是真实Transformer kernel收益，已发表人工解析映射作gold。决定贡献所需的最小消歧已足够：这是成熟code proposal→finite validation→compile路线在可解析几何上的应用，未分離足以改变本项目LLM执行/编译有效性边界的新机制或独立证据。前分母关闭、不评分；不是因非LLM/小实验硬拒，保留已读证据而不把“有GPU”变成贡献准入。
- **10390 Permanent Faults / SDC**：[v1](https://arxiv.org/html/2604.10390v1)，实际III-D、IV-A/B/C、RQ4、VI。RTL-derived fault-site/profile固定physical rank，用随机layer/phase/tile及uniform phase exposure（forward:backward1:2）仿真；GPT2Small/Medium、16H100两节点、Megatron data-parallel/sequence-parallel、Adam/warmup/cosine、FP16/BF16/FP8下有限fault campaign。finite check、skip-step/loss-scale可避免部分crash，不能挡有限数值的持续PPL损害；FP8分支不能外推所有precisions或自然故障率。`2+2+2=6`标准已有覆盖：实际Ch36“Crash、NaN或collective timeout…”及后续三段明确finite SDC沿activation/backward/optimizer扩散、分位置guard/recompute与step coordinator提交权、precision/false-positive/profile成本，不只是SDC主题匹配。采用这些机制已覆盖，不新增作者特定fault-policy；替代parallel layout和真实硅profile是限域，未复现。
- **10403 LIRA / SAG**：[v1](https://arxiv.org/html/2604.10403v1)，实际§2.1/2.2、§4.1、AppendixA.1/A.2、L和MCQ限制。普通response-only loss只排除prompt target，response损失仍可沿prompt/response依赖更新共享参数；SAG在forward不变的同时阻断response-position到projection/FFN/norm参数的梯度，并额外阻断response→response梯度路径，residual正常。counterfactual分支用SAG，benign retain分支用SAG†（不额外切response→response）；不能混写所有分支同mask。AppL有无SAG/anti-LIRA受限控制，PCA形状不是因果完备证明。toy installed backdoor、embedding attack和TOFU/WMDP协议不证明通用jailbreak免疫或知识已删除，MCQ降分只是必要非充分。`2+2+2=6`，具体Books gap深入：Ch29实际已讲loss-position/corruption-support与response-only masking，但未分开loss位置与反向计算路径。拟在“是否应该对Prompt计算loss”后补条件分支，解释forward identity/gradient-route可不同、counterfactual与retention权限及通用保证边界。owner=`TRAIN-SFT`，Ch29/Legacy25；Ch72只保留安全评价handoff，不重写攻击配方。写前须非作者有限source→owner核验。

第十六批CodeComp保护span超过预算时仍截断，不能写无限hard protection；AAR低PVR可为合法shortcut且DAG/长度混杂。第十七批visual jailbreak的transfer主表与附录average数字不同且不在采用范围，保持未采用、不扩全附件。两批七项非作者结果见V3_APR02_BATCH16_INDEPENDENT.md及V3_APR20_BATCH17_INDEPENDENT.md；并非日期/整日Gate。

### 第十九批：最后14项的必要证据与有限处置

root实际读取下列官方精确v1的方法、评价与直接反证；只处理既有155完整题摘中的未决项，不扩库存或遍历无关附件。以下为作者侧裁决，仍须有限非作者核验；四个真实gap没有预支整合。

- **10480 Dataset Lineage**：[v1](https://arxiv.org/html/2604.10480v1) §3–5及limitations。source queue→README/docs extraction→alias/时间约束→低置信人工检查→DFS是文档推断lineage，83seed/430node/971edge不等经过内容验证的全部实际祖先。root-only/out-degree采样后MinHash与Vendi/centroid在不同规模数据上比较，并未训练验证质量或证明所有隐含交集；不采用污染比例作真实content ancestry。`2+1+2=5`标准仅报告：保留受限图发现与采样分支，Ch27现有metadata inference≠source fact/版本/人工override不需要因本实验改为可信事实祖先。
- **10493 SWE-Shepherd**：[v1](https://arxiv.org/html/2604.10493v1) §3–5最小消歧。heuristic step reward→qLoRA MSE PRM→action选择复用成熟过程reward路线；100题、GPT5mini/max30的baseline57%/$ .029/15.2step与PRM51%/$ .053/12.2step反例保留。resolved/unresolved reward .4894/.4818不支持成功改善。没有分离新机制或足以修正现有重要设计边界的证据，**前分母关闭，不评分**；不是因为负面结果排除，也不删除已读反例，不改成PRM有效。
- **10495 Uncertainty Sources**：[v1](https://arxiv.org/html/2604.10495v1) §3.1–3.2、§4.1–4.2、§5/limitations。相同问答语料构造unique-answer、任一合法答案与去掉关键qualifier的ambiguity三类；GPT5构造/评价、人工Google核验及539/类有限范围。知识不确定→查证/拒答；合法多解→选择任一满足任务的答案，不必因语义entropy高拒答；输入不完整→澄清或显式条件化。三类改变action policy而非共享一个“越分散越错”的阈值。PRR对oracle/random归一且截到75%拒答，是排序/选择质量，不是事实正确率校准；相同来源与QA控制不证明开放任务能自动辨认原因。`2+2+2=6`，真实gap深入：当前Ch66 Calibration Slice解释语言/模型/access/input/token-selector身份及采样语义，不解释这三类estimand→干预。拟在该校准论证补两段窄分支，owner `PLATFORM-EVALUATION-SYSTEM`，Ch66/Legacy62；先非作者核再写。
- **10496 CodeQuant**：[v1](https://arxiv.org/html/2604.10496v1) §3.1–3.4、§4.1/4.3/4.4。activation rotation→非均匀weight centroid/assignment→重构与MoE aggregate-output/router-KL共同校准，分组permutation须折入上下游保持原算子语义。低比特activation code和weight centroid构成product LUT，再按codes查表累加；不是通用INT4 checkpoint自动享有tensor-core支持。GPU核心结论来自AccelSim/定制模拟lookup tensor-core，真实CPU路径不同，不能称A100实机2.63×。LUT/decode/布局/rotation、校准训练和静态centroids有新增成本；precision、length、batch按原文限域，SLO/concurrency未披露。`2+2+3=7`深入：Ch49现有quant-dequant成本清单未解释codebook artifact如何要求乘法路径改成lookup执行。拟refine“量化为什么不自动加速”后的小分支，owner `INFER-TENSORRT-LLM` Ch49/Legacy45；不采用模拟硬件为生产收益，不宣称router完全不变。非作者写前待核。
- **10500 Routing-Depth Visual Replay**：[v1](https://arxiv.org/html/2604.10500v1) §3.2–3.4、§4.1/4.3。局部视觉replay/self-distillation与salience-selected重复block、显式→latent curriculum是受限联合训练分支。梯度norm相关不证明视觉underoptimization唯一原因；Eq5用visited与文字unvisited冲突，§3.4部署只用LLM/无visual replay不证明所有depth-routing也无额外成本，保持未采用强实现句。8H100训练/8H20评价及α/投影反向切片限定；`2+1+2=5`标准仅报告，不从复合recipe建立普遍gradient诊断或零成本latent-reasoning机制。
- **10506 Progressive VLM Training** 与 **10517 EgoTSR**：分别[v1](https://arxiv.org/html/2604.10506v1)、[v1](https://arxiv.org/html/2604.10517v1)，实际§3/5与§3/4。官方abs author list有共享Yang Xiaoda/Wang Can/Xue Jingyang等，但作者集合、题名和paper ID不同；共同AgiBot、CoT→Tag data及实验属于关联路线，不仅因语义相似合并两个独立正文家族。前者CoT→标签/可变数据量，后者再加LongTag与长任务支持；reverse-frame/bias和短长任务区分是受限证据。额外数据/预算/任务变更未隔离唯一CoT因果，答案监督不证明形成透明causal architecture或强制排他信息通道。分别`2+1+2=5`标准仅报告；不重复采用两文共同recipe，保留原始作者/版本和弱监督、chronological shortcut与long-horizon限域，不把scene判断当真实机器人闭环。训练原文bf16/AdamW2e-7/warmup1000；10506 batch8×acc2、10517 batch4×acc2/H800，API/基线混合不作同compute比较。
- **10508 Self-Repair**：[v1](https://arxiv.org/html/2604.10508v1) §3–5/TableVII及§7。greedy初答→错误反馈最多4轮/成功即停，cumulative solved不等每轮单答accuracy；代码提取/15秒subprocess亦影响结果。7API模型HumanEval164/MBPP257，与T=.8独立5sample的对照只有4模型、不匹配token预算、无stochastic-repair，8B resampling79.9高于repair76.8。thinking文本提取失败与provider配置不能归因内部推理能力差。`2+1+2=5`标准仅报告；不采用普遍“repair优于sampling”或cost排名，已有Reflection的外部feedback/搜索预算原则不由此改变为绝对选择。
- **10511 Causal Policy Reasoning**：[v1](https://arxiv.org/html/2604.10511v1) §3–6/Table3、§4实际2400trial=40case×4model×5prompt×3repeat。case类标签用naive模型准确性确认，政策YES/NO、熟悉度和小case簇会混杂CoT因果归因；interaction OR .053不是CoT全部降低准确性，Table3 counterintuitive75高于naive70.8仍有增益。citation p=.53不证明无记忆，case内ICC .537意味着trial不独立；完整prompt附件要求联系作者。`2+1+2=5`，标准已读、中心强“causal parrots/机制因果”窄争议暂缓：不进入Books，保留40case/API默认参数/regex fallback范围和相反数据。重开条件是完整prompt、标签与因果对照或作者收窄；不等待这私有附件审所有case。
- **10516 SGKR**：[v1](https://arxiv.org/html/2604.10516v1) §2–3/Alg1、§4.5及limitations。AST function-call图连接knowledge与semantic I/O，query BFS选输入→输出子图，不等embedding/PPR替换名称。same-name merge可产生跨trace新I/O路径，名称相同不证明实现/前提相同；节点少不等token预算完全匹配，gold-symbol→Python或LLM检查也不是真实外部groundtruth。DAB/FinQA/ConvFin的有限对照支持结构retrieval分支；`2+2+2=6`标准仅报告，保留图与可执行函数身份关系而不将假设合并/路径存在升级成可运行或事实真，未确认需要修改已保留graphpath≠truth/执行验收的设计结论。 本轮没有核实各数字对应的完整模型/预算合同，不沿用先前模型推定或外推性能。
- **10539 IceCache**：[v1](https://arxiv.org/html/2604.10539v1) §4.1–4.5、§5.1/5.3。logical token order分页便宜，但相关Key分散会加载许多无关row；每head按Key相似性组织DCI tree/node-page，最大内积转换与动态插入维护索引，GQA合并同group选择后，host gather连续buffer→一次PCIe→device scatter。它改变physical locality，不改变logical causal position；ANN会漏、跨层page reuse另有精度风险。A10040/H10080 PCIe/64CPUthreads/FlashInfer、LongBench/RULER/GSM8K局部；36k Llama3.1-8B的TT2T不是TTFT，selector .05s与decode .04s反证索引开销已消失。`2+2+3=7`深入：现Ch45 Grid→Chunk→Page/physical access-plan未解释按Key locality重排物理页及GQA/搬运联动，拟在该既有层级访问论证补两段条件分支，owner `INFER-KV-CACHE` Ch45/Legacy41。保留构建/动态维护/CPU索引、stage buffers与dense回退，不采用无损或通用SLO。写前非作者待核。
- **10546 RDVQ**：[v1](https://arxiv.org/html/2604.10546v1) §3、§4/limitations。hard code承担reconstruction，soft assignment给entropy prior可微rate代理，训练端RD梯度与真正码流分开；prefix传输后AR补全后缀是生成，不证明恢复原始事实。attention-free VQVAE/250M LlamaGen、ImageNet→entropy→joint/OpenImages/DF2K、Kodak24/CLIC428/DIV2K100的受限codec对照，未给MLLM representation fidelity或通用生成质量保证。`2+1+2=5`标准仅报告：保留rate/reconstruction/completion的替代支路，不将image codec benchmark代大模型token/grounding设计。
- **10547 Agent2RL-Bench**：[v1](https://arxiv.org/html/2604.10547v1) §2.1–2.5、§3.1/3.3/3.4。同outer workspace→route选择→code→训练→artifact提交，static rule/static judge/stateful rollout三种inner structure须分开，生成script不等完成training。test未挂agent但反复scalar feedback不消除adaptive selection；best-within12h应绑定submit count/time/data/driver/scaffold。两study模型和driver纠缠，partial-factorial/single-run不能归因scaffold；SFT fallback不是onlineRL，Free高分也不能代在线轨迹工程已完成，DeepSearch种子噪声约±3pp使微小提升未决。`2+2+3=7`深入：Ch66 Post-training/AgentOptimizer仅讲artifact/旧新任务回归与harness独立owner，未讲post-training-agent的outer/inner验收以及route标签与实际训练行为区别。拟在该实际论证补两段有限evaluation contract，owner `PLATFORM-EVALUATION-SYSTEM` Ch66/Legacy62；不采用所有task表现的机制唯一因果或grade scalar防泄漏保证。写前非作者待核。
- **10556 AR vs Diffusion Hallucination**：[v1](https://arxiv.org/html/2604.10556v1) §3.1–3.3、§4.1/4.2、§5与limitations。LLaDA/Llama架构scale近似、Dream来自Qwen初始化均不等同训练数据/权重完全控制；适配更新保留parametric confound。T=L/temperature0/整1024block不代表accelerated block生产路径；无remask后future错误anchor可锁定其他位置，200 hallucinated输出多label与failure分类是条件样本不是普遍prevalence。HalluLens extrinsicQA、LongWiki/NonexistentRefusal、排除intrinsic/instruct使headline“不如AR”限域；增step Dream与LLaDA不同，作者归因schedule只是解释，不是唯一因果控制。`2+2+2=6`标准仅报告：保留bidirectional visibility≠可编辑/事实truth，当前Ch24已有commit/remask及联合一致性限制；不据此改为所有diffusion更幻觉或更安全。没有声称既有正文已包含整个本benchmark。

四个gap为10495/10496/10539/10547，全部先独立审阅再落实；其余九项候选的Only/Disputed裁决与10493 preclosure也待有限非作者核。ordinary pending没有写成external blocked；日期/正式分母与六部分日报仍待收口。

### 第十七批三项必要证据（2026-09-27；有限处置提案）

- **10286 STARS**：[v1](https://arxiv.org/html/2604.10286v1) §4.2/4.3、§5连续target定义、§6.1/6.2/6.4。静态capability prior和request/context trigger经validation quantile归一化、凸融合；后者把intent/argument与provenance/trajectory/taint分开，用request-skill gate限制context gain。所测target是canonical allow/escalate/block锚加within-band heuristic的.65/.35混合，不是独立elicited连续判断或真实攻击概率；因此ECE与目标一致性不等部署事故率校准。相同candidate space的risk-first/threshold-first选择改变false-block与task completion，支持窄retrieval/干预工作点比较，却受标签构造与有限context规则限制。2+2+2=6标准，仅报告提案：未披露新的授权保护行为，risk scorer不能拥有执行权限；不以标题安全强制深审，也不将selection目标当一般安全校准。
- **10290 AI Organizations**：[v1](https://arxiv.org/html/2604.10290v1) §3.2.3、§4.1/4.2、§5.1/5.2。软件任务分别计held-out views/错讯与cost/漏诊，咨询任务由LLM judge计business/ethics；多Agent交接允许参与者绕过拒绝参与的节点，单模型aligned不自动保证组合。90组织结构/benign-malicious ratio与Opus4.1/4.5对照保留重要反证，同时不同软件approach、judged伦理与硬任务指标不能合并作统一因果或生产事故率，Opus4.5任务切片明显改变gap。2+2+2=6，涉及安全成立边界深入，拟已有覆盖：实际Ch82“Collective Risk 来自局部 Utility 与交互规则的组合”已具体列local utility、visibility/topology、shared aggregation、dissent与独立effect verifier，保留协作收益/并行度代价和backbone/trial/judge范围。采这个组合非蕴含，不声称现章承载所有咨询领域经验或组织必然更不安全。
- **10299 Attention-Guided Visual Jailbreaking**：[v1](https://arxiv.org/html/2604.10299v1) §3.3/§4.3/§5、Limitations、A.2/D.2/H.2。PGD图像扰动同时优化prefix suppression与image anchoring，原生forward不直接改attention；loss消融支持这个受限联合分支。后续正bias的attention干预降低ASR却仍26%，b=.5与1非单调、较强bias缩短输出，监测不阻止危险生成。因此不采用“恢复attention证明唯一/必要原因”或防线已可靠的强叙述；它只支持这一明确干预会改变所测行为。H100/bfloat16/eager attention、三LVLM、p=.9/T=.7/max100及LlamaGuard/Detoxify/GPT4borderline限定，不能外推闭源/黑盒或实际副作用。2+2+2=6、安全深入，拟仅报告：保留视觉prefix路由攻击/干预的窄实证与非单调代价，不给泛化安全保证；当前Ch72 component-removal与routing-redistribution分账仍成立，但不冒称已经包含本配方/全部视觉因果结论。

本批必要命题已审，最终处置待非作者核，不预支日级完成；其余普通队列继续。

### 第十六批四项必要证据（2026-09-27；有限非作者核验中）

只收口已经完整题摘判断过的10219/10235/10261/10268，不新增原始队列。root实际打开四项精确v1 HTML，围绕以下窄命题读方法、关键对照与代价；日期待同既有公告/processing组合最终归并，Submitted不改称首发。

- **10219 V-STAR**：[v1](https://arxiv.org/html/2604.10219v1) III-D、IV-C/D/E、V-A/C。中层视觉attention分额与entropy定义HVAR，pivot token使用局部reward，FRM随机插入反思指令生成、移除注入文本再用正确终值轨迹作训练；不是仅添加自然语言“再看一次”。answer-only、HVAR、FRM及同数据规模控制支持受限训练分支，却没有把attention/hidden异常与普遍幻觉唯一因果等同。Qwen2.5-VL-7B、受测视觉推理集及规则匹配限定结果，proxy reward、正确轨迹选择、附加采样/训练与反思成本仍存在。2+1+2=5标准，仅报告提案：保留此复合轨迹配方和消融边界，不将过程proxy写成模型自知或一般grounding保证，也不假称当前Books实现了这套完整配方。
- **10235 CodeComp**：[v1](https://arxiv.org/html/2604.10235v1) §4.3/4.4、§5.1/5.3和Table4。按chunk结构复杂度分预算，再由CPG中的call/control/return/assignment与query-symbol overlap保护span；强制保留会改变可压缩预算，不是仅用attention排序。60条DebugBench切片的ablation表明保护span贡献更强、只改预算弱；SWE-bench Lite不同模型/指标也有反向切片，不能声称全面胜SnapKV。SGLang/Qwen2.5-Coder32B的局部时延不证明多租户tail/SLO。2+2+2=6标准，拟已有覆盖：实际Ch45“Pre-RoPE Calibration 与 Workload-semantic Selection 是两条正交路线”正文已具体写code shortlist→CPG prior→每chunk预算/保护span→物理KV block，并保留parser、共享前缀、校准及recency回退成本。它承载所采机制，不声称完整复现论文实现/全部实验。
- **10261 The Amazing Agent Race**：[v1](https://arxiv.org/html/2604.10261v1) §3.3、§5、§6.3/6.5。diamond任务用两条tool链与汇合阶段建立可见访问图，Harbor19工具/8类、上下文截断、step budget和600秒界限属于评价对象；PVR导航覆盖与RCR推理正确分开，不能以终值accuracy吞掉搜索失败。diamond本身还有路径长度混杂，导航指标关联不是唯一因果；不同模型/agent runtime配置不能当纯架构比较。2+2+2=6标准，拟已有覆盖：实际Ch66 document Agent正文保存retrieval/navigation/grounding/effort、actions预算与failure stage，run diagnosis又要求可观测opportunity set，不把未访问自动判错；已承载本次有限采用的诊断分账，而非声称已有本diamond benchmark。公开任务/工具、解码与预算限域，额外探索仍有循环和成本尾部。
- **10268 EditCrafter**：[v1](https://arxiv.org/html/2604.10268v1) §3.2/3.3、§4.1–4.3。训练分辨率patch作CFG0的tiledDDIM inversion，原始unconditional与dilated条件分支混合为NDCFG++，在高分辨率编辑保持对象身份和全局语义间选工作点；不能将τ的时间方向自行修补成另一算法。SD2.1/SDXL1.0、单RTX4090、150 prompt-image pairs及λ=.5是局部设置，CLIP/HPS/ImageReward不是独立身份真实性保证，默认CSD和resize+StableSR也不是严格同系统预算。2+1+2=5标准，仅报告提案：保留条件引导/反演的局部工程分支，不把图像编辑扩大为跨模态生成普遍演进或因果保证；额外patch处理、dilation/guidance选择及高分辨率显存成本保留，训练分辨率直接编辑仍为便宜基线。

四项已交apr02有限非作者source→owner/处置核验，未预支通过或日级完成；没有新增Books提案写入。剩余普通有限材料继续，不等待本批。

### 第十五批四项有限消歧（2026-09-27；待非作者裁决）

本批仅处理此前题摘队列的10072/10091/10134/10311，未扩大原始范围。实际打开四项精确v1 HTML，并按拟处置补读必要方法、对照或限制。

- **10072 E-GRM**：[v1](https://arxiv.org/html/2604.10072v1) §3.1–3.2、§4.3–4.5/Table3–5、§6。先作多次不同采样参数的短回答，以一致性触发长CoT，再用训练的 discriminative scorer 选择；“model-internal uncertainty”实际是可见生成的共识代理，不是直接读取内部自知。Huber/hinge输出也未成为校准正确率。500题、M=5/阈值.8和受限消融支持条件化计算取舍，但并行调用、域阈值与scorer OOD成本存在，效率数字不外推服务SLO。2+1+2=5标准，仅报告提案：保留这个受限 adaptive-reasoning 对照，不建立新的通用置信度/安全授权规则，也不假称具体配方完整已有覆盖。
- **10091 SEPTQ**：[v1](https://arxiv.org/html/2604.10091v1) 首页明确 KDD2025、DOI `10.1145/3690624.3709287`。§4.1–4.3/Alg1实际是全矩阵静态 salience mask、保留少量高精度位置、其余逐列量化/残差更新，不是简单所有权重RTN；有效bit还包括高精度保留，不能将2.1bit同2bit直接等量。原始首次公开归属不能由2026 arXiv库存替代2025正式版本；本次DOI正文入口错误，尚未证明事件时版本一致或存在本窗重要变化。该家族单项日期/身份隔离，不评分、不作为本窗新候选/Books；重开只需较早正式正文公开证据及本次版本是否有实质贡献，不扩全年发表史。
- **10134 PlanGuard**：[v1](https://arxiv.org/html/2604.10134v1) IV-B/C/Alg1、V-A/B、VI。隔离planner只读user instruction/tool catalog生成reference集合，exact match直接通过、未知tool拒绝、已知tool参数不符交LLM verifier，后者还读取agent reasoning。InjecAgent1054例、同DeepSeek-V3.2且victim加“工具返回命令必须执行”的设置，不证明开放防线。§V/VI由planner隔离推出“任何动作不能偏离/确定性安全”的中央保证不能由此逻辑成立：参数审核仍是模型判断，真实合法值可依赖planner未见的环境证据；作者也承认context-dependent参数路径。2+2+2=6、安全保证深入，拟窄争议/暂缓此无条件保证，不否定隔离机制或有限零ASR。所需重开为与实际第二级控制流一致的保证条件或适应性参数攻击/良性动态值对照；不能仅靠更多无攻击命中改为安全证明。实际Ch78仍由可信executor拥有业务/授权/effect验证，不将本proposal当通用确定性authorization实现。
- **10311 Gypscie**：[v1](https://arxiv.org/html/2604.10311v1) §6、§7.2实际DAG→具体数据/参数pipeline→跨框架映射，并记录operator semantics、provenance和cost；weather HDF/Pandas与Spark Docker同物理主机、10–70files/5runs对照，Spark内存未测。当前材料提供成熟artifact/workflow/cost组合和filter pushdown案例，没有分离足以改变本项目模型生命周期/训练推理平台设计的新增机制或边界，故具体前分母关闭、不评分。不是因未写LLM或单领域小实验硬拒，也不由性能图宣称跨后端普遍最优。

10072标准Only、10134中央保证窄争议、10091单项事件隔离及10311具体关闭均待有限非作者核；已读证据不删除。第十四批五项已获apr02必要源/owner通过，其中10180/10187真实写入Ch49，仍待非作者写后，不预支整合计数或日级Complete。

### 第十四批有限必要证据（2026-09-27；五项采用待独立复核）

恢复已重读AGENTS、当前合同/统一入口及ROADMAP；范围仍本日09:00截点。以下五项此前完整题摘已读，本批只补采用命题必要证据，不重新扩大325标题/155题摘或1334身份。精确v1字段分别为Updated UTC 04/14 00:31:53、00:33:20、00:34:53、00:35:00、00:35:42，来自原始DataCite三页；这不是各自首次公开时刻，只与既有永久ID/公告槽/OAI邻界组合支持早批归属，不能用Updated孤证冒充first-public。本日仍14项真实整合/写后通过，不预支本批提案或整日完成。

- [2604.10135v1 — Think in Sentences](https://arxiv.org/html/2604.10135v1)：必要§2、§4.1–4.3/Table3、§6已读。句边界分隔符的ICL/SFT分支与固定长度/随机分隔控制说明结构化入口不等任意增加token；去掉特殊分隔后的表现仍须按各训练条件比较。2+1+2=5标准，拟仅报告：这是受限表示/提示实验，不建立唯一推理机制。SaT、额外token和训练成本保留，7B SFT不能外推所有规模；attention/probe可读性不证明因果中介。对读Ch75全文emphasis-derived-view命题，不假称现书实现本配方，也不因它已有结构主题直接拒收。
- [2604.10158v1 — Tracing LC0](https://arxiv.org/html/2604.10158v1)：必要§2、§3/Algorithm1、§4局部干预已读。分别用transcoder与稀疏attention分解构造近似feature图，再做置零/移植干预；规则验证与剪枝选择决定可解释范围。2+1+2=5标准，拟仅报告：LC0棋盘64位置的局部归因不成为通用LLM推理字典，也不由可解释特征完备证明全部决策可解释。高精度/低召回、有限人工验证与多个层位的干预保留；model move probability不是世界正确率。Ch14已有probe与多点必要/充分性分责，Ch16/17拥有组合机制，不冒称本算法已有覆盖；不因小模型或棋类硬拒其有限证据。
- [2604.10180v1 — Tessera](https://arxiv.org/html/2604.10180v1)：必要§III–IV、§V-A/B已读。通过PTX访存范围和library语义建立保持原顺序的kernel依赖图，CUDA graph分别绑定策略；cut边需要跨GPU复制/等待，跨迭代KV另维护replica及增量。2+3+2=7深入，拟Ch49 phase-aware backend之后补kernel-level异构placement的依赖/副本责任；Ch55仍拥有阶段拆分。未知间接访存保守回退，collective保留原同构组，权重复制/显存容量未纳入MILP，不能写任意图都能异构化。作者以异构设备/RDMA和有限模型、vLLM.18评价吞吐与低负载策略；只取机制，不采用通用倍率，精度等未披露字段不补造。该提案尚未真实写入。
- [2604.10182v1 — Credit-Budgeted ICPC-Style Coding](https://arxiv.org/html/2604.10182v1)：必要§3.2–3.3、§4.1–4.5已读。API计费、测试/提示与可调时钟权重构成contest credit；错误提交penalty参与排序但停止规则与其不同。2+1+2=5标准，拟仅报告具体评价协议：48题先经Bronze资格筛选，跨API比较设时间权重为零，五次重复不证明生产延迟公平。swarm另测时钟/通信成本；较强提示、更多credit并非单调收益，不采“纯策略瓶颈/内在alignment唯一原因”归因。Ch66已把budget/environment/scorer纳入subject，Ch70拥有质量/SLO下outcome成本；没有把比赛credit等同实际平台账务，未重复改书。
- [2604.10187v1 — WaveTune](https://arxiv.org/html/2604.10187v1)：必要§3.2–3.3、§4.1–4.5、§5.1–5.5已读。按macro/wave桶拟合双线性cost，另存邻近loop anchor的micro配置；macro/micro仍受资源可行性耦合，不能声称独立全局最优。2+2+2=6、实际Ch49缺口深入提案：承接完整operation descriptor，将wave分段及cost/config表共同校准纳入kernel选择。五GPU/三kernel分别profiling，外推和MHA/单组代理只是近似；Step在MI355X退步，离线profiling成本与受限Prefill batch4不等全服务收益。不采用“消除quality/latency取舍”，固定稳定负载保留实测cache，近似失配回退定点实测。提案未写入，待有限非作者源→owner核验。

本批三个标准仅报告、两个深入窄采用提案均待有限独立核；不是本日剩余全部工作。现有证据和负例保留，未冻结最终分母，未签日级Gate。

### 第十三批有限必要证据（2026-09-27；十项处置及四处实际写后通过）

apr02 已在 [本批独立审计](./V3_APR02_TEN_MECHANISM_CALIBRATION.md) 核实下列十项必要来源及具体 owner 差异：六项仅报告、四项整合。四项 09970/09975/10103/10152 已分别写入 Ch36/49/24/48 的机制正文，并由 apr02 顺读真实段落与相邻衔接通过。本日累计14项实际整合且写后通过；后文“拟/提案/待复核”保留原决策过程，不再作为本批普通待办。整日来源、日期归并、最终分母及日级验收仍未完成，不计整日闭环。

- [2604.09942v1](https://arxiv.org/html/2604.09942v1)：实际读§3的二次binding probe、连续性/位置/方向控制、head选择及mean-ablation和随机head对照。七个ViT的合成曲线/物体与有限自然图像迁移支持连续性selective heads参与该探针，控制集仍有高于chance结果，最selective layer/head的选择也限定归因；不证明全部object binding、MLLM factual grounding或唯一视觉机制。2+1+2=5标准，仅报告。Ch23拥有表示/融合与干预后的任务验收，但不冒称它实现本二次probe；此局部ViT结果尚不改变本项目长期接口或架构选择。
- [2604.09970v1](https://arxiv.org/html/2604.09970v1)：实际读§3.1 Algorithm1/Assumptions1–3、§3.2与§4语言/视觉实验。每节点持有自己的adaptive moments，本地K步后压缩的是相对已重构shadow model的差，再用邻居mixing修正；不是压缩一个全局Adam gradient后简单AllReduce。2+2+2=6、Ch36真实责任缺口深入提案；拟在LocalSGD后补optimizer-local状态、compressed reconstruction与consensus分责。contractive压缩可有偏，理论另要求连通mixing、smooth/lower-bounded及独立无偏且范数有界随机梯度等条件，Adam参数还有随TK变化的限制，不能写任意Adam拓扑等价。nanoGPT10.7M/TinyShakespeare/4A100与CPU视觉实验有限；communication rounds/bytes不等端到端wall-clock或SLO。漂移/状态恢复失败时回退有界local steps或同步完整状态。
- [2604.09975v1](https://arxiv.org/html/2604.09975v1)：实际读§III stage-compatible packing、§V conversion成本、§VI配置及§VII–IX安全/限制。相邻FHE kernel输出匹配下一kernel layout，FHE/MPC边界可用minimal ciphertext packing，但expanded packing若减少计算仍可能更优；必须比较conversion+CKKS+MPC总成本，不等最少conversion次数。2+2+2=6、Ch49真实execution-plan缺口深入提案；Ch72继续拥有semi-honest威胁及密钥边界。CKKS scale/modulus、43-bit/F13 MPC、A100及实现限定结果；round-trip数值试验不成为通用误差保证，表中communication排除conversion而latency包含，不能混成完整网络节省。matched接口/数值或信任不成立时保留静态方案或其他安全计算路径。
- [2604.10027v1](https://arxiv.org/html/2604.10027v1)：实际读§2.2–2.4及必要训练/消融接口。hard replacement首先改BOS cached V会塌缩；soft injection与独立BOS path是不同干预。Eq4对单mean-pooled K/V作cross-attention，单key softmax恒1，不能由此声称query-dependent上下文选择；多长度伪码仍须形状澄清。不否定作者有限任务结果。2+2+2=6、机制身份深入，拟仅报告；Ch22 neural-memory更新不是本方法完整Existing。只保留可分离mean-anchor分支，不据未澄清query selection改写长期架构。
- [2604.10065v1](https://arxiv.org/html/2604.10065v1)：实际读§2 Eq1–3、reward与§3实验。pad/nonpad raw logits分组求和再binary softmax，是timing surrogate，并非对原token概率求边缘；两组大小不等时共同logit平移可不改变token policy却改变binary policy。2+2+2=6、新目标身份深入，拟仅报告可分离经验，不采用语义保持projection保证。43小时私有两通道对话、ASR时间和token→时间假设限定reward；Table1互动切片与latency并非全面胜原GRPO/Moshi。coarse policy的KL与ratio也不能替原token行为的校准/安全验收。
- [2604.10071v1](https://arxiv.org/html/2604.10071v1)：实际读§3 Eq1–6、§4.1与§4.4–4.6。每token以视觉attention mass选正/负层，对final logits做双anchor修正，再由final概率阈值限制候选；这是同模型proxy，不是独立事实验证或纯语言噪声的证明。2+1+2=5标准，仅报告。五个7B MLLM/RTX5070Ti、有限视觉任务与手调系数，过强负项使结果退步；额外attention读出/projection与precision/并发/SLO未完整量化。Ch20的sensor≠authority与Ch23表示访问已有通用边界，不把本精确heuristic冒称完整Existing，也不因attention有相关性给幻觉正确性保证。
- [2604.10074v1](https://arxiv.org/html/2604.10074v1)：实际读§2数据/单层单头模型、§3 Theorem1–2条件与§4均值去噪解释。正交pattern的多token GMM、population GD、特定初始化及维度/token数/step-size/迭代次数/SNR条件下接近Bayes denoising risk，是受限理论机制；不能改称有限数据深层Transformer已能学任意diffusion或部署优势。2+1+2=5标准，仅报告，不采用其全部证明为本书一般保证。Ch24 kernel表达性与可学/初始化分开，Ch15 attention的条件聚合仍成立；此toy分支不要求将本书改写成通用最优denoiser定理。
- [2604.10079v1](https://arxiv.org/html/2604.10079v1)：实际读§3检测/五类处理、§4主要结果及必要定义。用保留训练response的MC选择测可重复恢复，是改变评价接口，不能直接当自由生成的知识存在性。作者称pass@N的量实际是重复成功比例，不是至少一次成功概率；按confidence选择的BoN不是oracle上界，0.2阈值/Top1000也只界定本协议。2+1+2=5标准，仅报告其诊断/干预结果；不采用15.3%为所有SFT未学会率，CPT改进也不证明某项缺陷唯一因果。Ch29的目标拟合/监督可教性与Ch66的metric/evaluator身份已有采用原则，五类配方不强行整章复制。
- [2604.10103v1](https://arxiv.org/html/2604.10103v1)：实际读§3.2–3.5、§4.1及长视频比较。将被evict帧先写入线性L/H状态，近期窗口仍作block-sparse attention；训练先dense形成语义、再启hybrid，同时train/infer temporal RoPE cap相同，并以同noise的teacher rollout对首步latent作regularization。2+2+2=6、Ch24生成状态/训练迁移窄缺口深入提案，不归为Ch25 causal environment model。Wan1.3B、832×480、batch32、1000+1000训练步、9-window/top20%与30秒16FPS定量协议限制结果；10分钟展示不是无限无损状态证明，sparsity更强反有退步。固定历史压缩与训练/蒸馏成本并存，不能从constant-state footprint推所有历史可恢复。
- [2604.10152v1](https://arxiv.org/html/2604.10152v1)：实际读§III self-assisted/affinity/expert替换、§IV配置与§V–VI反例。draft借用target非expert参数与GPU驻留hot experts，draft不搬CPU专家，target验证时才合并各token需求并更新下一轮hot set；无需另训draft与前文训练router分支不同。2+2+2=6、Ch48实际机制缺口深入提案。greedy exact-match只保持该greedy输出，不自动保证任意sampling；NLLB/Mixtral/Scout、H10096GB/PCIe5与batch1–256限定结果，小batch缓存可更快，更多draft专家未必更快，精度/完整SLO未披露。acceptance、verify expert union与loading必须共同结算，all-resident或低batch时普通target decode仍合理。

以上只更新十项必要证据与采用提案；来源/日期、正式分母与整日Gate仍需收口，不把写作提案计为实际整合。非作者仅复核这些具体结论与owner差异，不扩全部附件或版本历史。

本次窗口为 `[2026-04-13T09:00:00+08:00, 2026-04-14T09:00:00+08:00)`。报告作者 root；当前仍进行中，不继承旧 V2.1 Complete。仅处理本日，每日来源与真实触发源；不从 Weekly 反推。

## 原始范围和日期

原始 DataCite 三页快照（`../arxiv-owner-replay-20260903/datacite-created/2026-04-14-page-01.json` 至 `03.json`）去重为2262个身份，连续 ID `2604.09548～11809`；其中 `2604.09548～10881` 共1334个身份是本次有界定位与查漏子范围，不是三页全量，**也不是1334篇贡献候选或必须逐项深审队列**。按当前来源主线作有界主题标题检索，得到325条标题线索，已浏览；关键词只用于检索，以下判断读完整题摘。另定点复查旧候选中未被主题词命中的09557/09603/09651/09681/09731及先前错误归04/12的十二项线索。

日期联合依据继续核验：arXiv官方说明 ID 在公告分配、通常美东20:00（4月北京时间次日08:00），本批连续 ID 与各自 v1 Updated 记录在00Z后；不把 submitted、DataCite created 或单个 Updated 字段直接改称 first-public。Updated≥01Z或后月更新时间、目录时间冲突的拟入选材料具名隔离；新候选采用范围必须完全落窗。本段不声称所有1334项已逐一证明落窗。

## 首批题摘判断（尚未冻结分母）

下表均已读快照中完整题摘；多版本材料进入证据审阅时仍核精确版本。`待核验`表示潜在贡献清楚、等待证据，不表示结论成立。独立准入校准已请求 apr03，同时审查拟入选和代表性排除。

| arXiv身份 | 题摘判断 | 具体依据与待核问题 |
| --- | --- | --- |
| 2604.09557 | 待核验 | SD速度由语义分布和并发制约；真实输入与合成输入、batch相关draft长度和词表剪枝改变有效比较，不是只增加题库。 |
| 2604.09560 | 待核验 | attention得分分解为metric/potential/circulation，并有干预circulation的结果；需核数学假设与移除分量是否控制预算，不把几何类比当等价机制。 |
| 2604.09562 | 待核验 | PD路由与在线speculation深度联动是具体推理分支；需核4A800相对TP基线配置与所谓11～18倍归因，不能用稳定TPOT证明质量。 |
| 2604.09574 | 前分母关闭，待校准 | 手机触摸运动学反检测和拟人指标；摘要未给足以改变本项目Agent执行、安全或发布契约的独立机制，反检测成功本身不等于系统可靠。 |
| 2604.09577 | 前分母关闭，待校准 | LLM提示+工具生成UI与人类偏好比较属于界面应用；摘要未分离出新的Agent执行机制或可信证据条件。 |
| 2604.09579 | 最小消歧 | proactive on-call与人工结案后知识提取可能只复用既有workflow/memory；只需核触发/学习机制是否存在新有效性边界，不因10月部署就自动保留。 |
| 2604.09580 | 待核验 | object state abstraction与显式transition/control图替代自由文本，final-plan reward训练结构化embodied推理；需核表示结构而非额外训练预算是否解释收益。 |
| 2604.09587 | 待核验 | 第三方app没有系统成功API时，轨迹融合图是否能提供可验证替代成功信号；改变GUI evaluation依据而非单纯20app/240task扩展。 |
| 2604.09588 | 前分母关闭，待校准 | identityfiles/log分离、RAG+RLM路由及未来multi-anchor愿景；摘要没有证明新持久记忆机制或部分失效恢复边界。 |
| 2604.09595 | 待核验 | 同参数预算压缩后不规则shape可能变慢；硬件对齐维度knapsack将参数容量与执行效率分开，是具体压缩/编译取舍。 |
| 2604.09603 | 待核验 | 高并发SD以统一super-tree做深/宽verification预算调整；需核gating/kernel/吞吐端到端与质量条件，不采最高加速数作通用结论。 |
| 2604.09604 | 待核验 | oracle定位但局部观察的text controller出现action prior/looping，比较regimen与parameter量；需核受控测试是否提供具体partial-observability边界而非只排行。 |
| 2604.09606 | 待核验 | 同prompt重复采样区分广度安全与单请求失败率；需核Bernoulli独立假设、sample数和评判器，不能将重复试验简单等同线上风险。 |
| 2604.09611 | 待核验 | 多请求依赖使batching/频率/功耗效果不同于单请求；需核workflow端到端能耗及Parrot/vLLM公平配置，而非沿用单kernel利用率。 |
| 2604.09617 | 前分母关闭，待校准 | 迭代query提取+相似card补缺字段是文档生成应用；未见新的来源授权或字段正确性机制，仅质量比较不构成长期系统增量。 |
| 2604.09620 | 最小消歧 | qualification-matched下AI态度信号可能影响LLM evaluator；只核是否分离可复用的judge混杂渠道，不能因组织治理应用自动收录。 |
| 2604.09624 | 待核验 | 从判别P(True)信号做按shift触发的无标签TTT校准；需核teacher错误相关性、逐流泄漏与成本/累积更新反证，不把ECE降低当事实保证。 |
| 2604.09651 | 待核验 | flow-VLA在连续动作生成初期注入及动力学mimicry，区别AR离散动作backdoor；安全采用需核攻击者权限、触发与真实物理适用边界。 |
| 2604.09665 | 待核验 | reasoning teacher/student alignment gap和base unsafe latent归因驱动BoN；需核归因与rerank消融，不把ASR均值下降当保证。 |
| 2604.09666 | 待核验 | 同backbone/retrieval预算下agentsearch缩小dense/GraphRAG差距，但multihop仍受益且offline摊销不同；核协议与稳定性，保留共存而非图索引被取代。 |

## 续跑位置

### 09560 / 09562 / 09580 的必要正文恢复与改判（单篇非作者复核通过，非日级验收）

apr01 已独立打开对应官方精确 v1：09560 PDF pp.1～4 的 §II～IV / Eq.8、23～24；09562 HTML §3.3～3.6、§4.1、ALPACA 与 Table8；09580 §3.1～3.4、Algorithm1、Table1 与 §4.2。支持下列具体处置，不把独立意见等同实验复现；三项单篇普通复核待办已消除，整日报告仍未冻结或通过日级 Gate。

- `2604.09560`：官方 [abs/v1](https://arxiv.org/abs/2604.09560v1) 与 [PDF/v1](https://arxiv.org/pdf/2604.09560v1) 的摘要一致，PDF 首页为 April 14；它们并不是旧快照中的“metric / potential / circulation + pretrained interventions”摘要。HTML `/v1` 首页 August 24 不用于本窗证据，旧快照也不覆盖精确 v1。root 实际读 PDF §II～IV 的 QK bidivergence、row/column normalization、Eq.8、PoE/SB 构造与 Appendix C 的 phase/probability 区分：v1 的贡献是组织 attention、diffusion map 与磁性算子的几何关系，并无快照中所称干预实验。拟按精确 v1 在前分母关闭：当前构造未给出需改变本项目 attention 解释或设计选择的新保证/适用边界，不能由后发摘要反推本窗贡献；这不是以“缺实验”排除理论。保留实际 v1 与旧摘要差异，等待独立准入校准，不列为全文不可取。
- `2604.09562`：[exact-v1 HTML](https://arxiv.org/html/2604.09562v1) §3.3～3.6、§4、§5 及 Limitations 已读。拟 `2+2+2=6`，因中心机制/评价冲突深入审阅，暂缓争议、不写 Books。FlowGuard 的 `M∈[0,1]` 与 Eq.3 `/100` 的单位口径未对齐；SpecuStream 的历史向量实际保存 δ 而非 acceptance，Eq.12 的 volatility 项增加 depth，与 conservative 描述不符；伪码的 throughput 递推也不等同新测量。§3.6 throughput 是 `(input+output)/单请求 latency`，不是 fleet output-token goodput；ALPACA TP 的171 tokens/s 高于137，而摘要的跨任务headline不能抹掉此反例。Table8/9 给出组合与固定深度比较，但改变 PD/routing/SD 多因素，TPOT 相近不证明输出质量。仅4×A800 40GB、Llama2-7B FP16、两stream pair、四数据集各80query；精确长度、持续到达分布、quality evaluator/SLO 未充分披露。恢复需要修正公式/单位、匹配执行配置与生成质量证据，不以代码未开源额外扩大请求。
- `2604.09580`：[exact-v1 HTML](https://arxiv.org/html/2604.09580v1) §3.1～3.4、Algorithm1、§4/Tables1～2 与 cross-task limits 已读。`2+1+2=5` 标准完成、仅报告。Class/Activity PlantUML 是生成的 state/plan 表达，不是经环境执行验证的 transition；GRPO reward 是 XML/diagram markers 加分区 action embedding greedy similarity，baseline 则用全篇 cosine，不能把不同 reward 尺度收益归因于世界状态。Stage2 描述还提供 ground-truth state，Stage3 实际只用29k规划集中的2k；evaluation 的 Recall 明示为 success proxy，不是物理执行。Full pipeline Recall 改善但 Precision 低于 unstructured，2-stage F1 低于 hybrid，跨任务也非全面改善。采用受限表示/训练结果，不采用“可执行 world model”“可靠因果状态”或真实机器人成功保证；未发现需要改写 Ch25/26 的独立长期机制。apr01 必要原文与反证复核通过。

### 本轮实际 Books 增量（仍非日级完成）

`2604.10055v1`：root 重读 §4、Table 1～3、Table 5 与 §6 后，按 apr01 已完成的非作者必要证据审阅，将“鲁棒训练后的 Clean Recovery 是另一项验收，不是安全证明”两段写入 Ch26，接在 capability/channel/attack-budget 安全段之后。Owner=`MULTIMODAL-EMBODIED-VLA`，Score V2=`2+2+2=6`，因真实 Books gap 深审；采用扰动 curriculum→低 LR clean recovery 与双侧回归验收，不采用梯度冲突已被因果证明、普适 hold-out、物理安全或输入分布唯一归因。正文写后非作者审阅由 apr01 通过；本日候选分母、剩余必要证据、来源边界与整体 Gate 仍未闭合。

### 后续题摘判断与独立校准

首批20项以外，以下52个身份已实际读完整摘要；合计72项题摘判断。这里只保存准入依据，不把待核验记成审阅完成，不按保留比例定配额。最小消歧只读决定准入的段落，不默认全文深审。

| 身份尾号 | 判断 | 具体依据 |
| --- | --- | --- |
| 09670 | 待核验 | in-context working-memory superposition的干预/消融能区分容量与干扰；需核因果归因。 |
| 09674 | 前分母关闭 | 哲学性的rational mind论述未提供本项目模型机制或系统设计的独立增量。 |
| 09678 | 最小消歧 | FSM多轮失败可能揭示状态追踪边界；需区分仅增加任务与改变已有能力判断的受控证据。 |
| 09679 | 最小消歧 | early consensus、pair debate和voting似为成熟组合；只核是否有独立的新有效性条件。 |
| 09681 | 前分母关闭 | 常规edge/cloud视频路由，未研究基础模型或对应的新执行机制。 |
| 09686 | 前分母关闭 | RAG/memory与latent-RL belief组合用于VQA，摘要未给独立belief机制或新的适用条件。 |
| 09687 | 待核验 | Grid2Matrix改变patch组织和encoder可恢复信息；需核输出细节与表示布局的控制对照。 |
| 09695 | 最小消歧 | PII与空间线索的隐私主张机制含糊；只核是否为可复用泄漏渠道而非任务分类。 |
| 09703 | 前分母关闭 | graph-diameter RL topology研究一般消息传播，不以类比构造LLM系统贡献。 |
| 09709 | 待核验 | 正交quadratic ViT FFN给出低秩替代分支；需核参数匹配与bilinear冗余，不能因小任务排除。 |
| 09712 | 最小消歧 | 工具视觉提示、atomic tools和skills三阶段；只核结构化视觉结果是否改变执行条件，非组合即保留。 |
| 09718 | 待核验 | 编译为JSON workflow降低重复推理成本；需核与固定脚本的约束差异及编译失败范围。 |
| 09722 | 待核验 | edge/cloud speculation联合优化goodput与energy；需区分bonus-token目标与实际资源目标。 |
| 09731 | 待核验 | 验证树按边际收益/代价调整，是具体verification分支，不只最高速度数字。 |
| 09741 | 待核验 | black-box core由另训guide平均执行概率引导；需核guide成本及可执行性评判器。 |
| 09744 | 待核验 | 多principal intent冲突协议改变授权问题；需核对单principal协议的假设，非词汇升级。 |
| 09747 | 待核验 | 根据memory entropy自适应提取数据的新攻击渠道；需核攻击权限和实际泄漏条件。 |
| 09748 | 待核验 | RLVR训练数据后门在verifier不变时影响policy；需核奖励分配与攻击归因。 |
| 09749 | 待核验 | object-conditioned因果attention bias的training-free分支；需核object oracle及成本。 |
| 09750 | 待核验 | reasoning conflict与representation overlap联系；需核受控干预是否支持攻击归因。 |
| 09752 | 最小消歧 | NPU执行/模型scale主张的快照摘要截断；只补原始核心说明，不能补造PLD后文。 |
| 09759 | 待核验 | photonic unary/analog stochastic Transformer是硬件精度执行分支，需限定模拟/实测。 |
| 09781 | 待核验 | 6D pose由坐标可视化、单轴控制和view选择分解；需核消融与真实反馈边界。 |
| 09791 | 最小消歧 | 定点failure retrain与regression约束可能为已有迭代训练；需核是否有新可复用验证机制。 |
| 09805 | 前分母关闭 | CodeGen edit tool、安全与human trust工程经验，摘要未给独立新机制或适用边界。 |
| 09813 | 待核验 | oracle-preserving环境合成区别离线SFT/auto reward；需核oracle保持条件。 |
| 09815 | 待核验 | MCP/GUI hybrid policy的distillation与experience路径；需核跨app failure及输入模态混杂。 |
| 09824 | 待核验 | slow3D ground entity与verified goal控制语言选择动作；需核具体验证与entropy条件。 |
| 09839 | 待核验 | white-box steering可离开prompt可达流形，改变攻击模型解释；需核理论与实证映射。 |
| 09841 | 前分母关闭 | 临床影像VLM分类fine-tune，领域指标和fragility未分离出本项目新机制。 |
| 09852 | 待核验 | block-summary text/KV双通道改变reasoning记忆信息路径；需核消融与缓存开销。 |
| 09855 | 前分母关闭 | regulated seller的RLVR谈判收益和策略阶段是领域应用，非新优化或return保证。 |
| 09861 | 前分母关闭 | GA prompt vector与CLIP/aesthetic fitness的成熟black-box优化，新prompt集合不构成机制增量。 |
| 09870 | 纠错定点核验 | 当前摘要明确erratum：原高准确率有ordering artifact，inverted-polarity finding撤销；需核v1与直接纠错说明，不把finding撤销误称整篇撤回。原headline不能进入Books。 |
| 09890 | 最小消歧 | reasoning-trace受控干预与MT质量脱钩可能揭示faithfulness边界；只核受控反证，非领域自动排除。 |
| 09917 | 最小消歧 | 可审计claims与概率audit预算的incentive形式化；需确认金融toy结论是否直接改变Agent验证判断。 |
| 09921 | 待核验 | dLM confidence/remask双温度区分exploration/pass@k与NFE；需核对照和选择成本。 |
| 09937 | 前分母关闭 | 医疗行政任务benchmark展示end-task/subtask成熟区别，未给新的归因或评价条件。 |
| 09940 | 待核验 | ZO weights与FO PEFT联合、多learning-rate分析，是具体训练分支。 |
| 09942 | 待核验 | ViT binding continuity的head干预分离similarity/proximity，可改变表示解释。 |
| 09945 | 最小消歧 | 固定人物的counterfactual图像可能分离judge的modality混杂；不把文化价值排行直接当贡献。 |
| 09970 | 待核验 | decentralized local Adam与biased compression的兼容条件，需核语言实验及convergence假设。 |
| 09975 | 待核验 | FHE/MPC stage compatibility与conversion cost相联，改变私密推理执行选择。 |
| 10014 | 前分母关闭 | 多模态bias题库和人口分组排行，摘要未给独立因果机制或新的validity条件。 |
| 10015 | 最小消歧 | FinTrace rubric/trajectory评估可能重复tool selection与information integration原则；只核新replay有效性条件。 |
| 10027 | 待核验 | 向首BOS attention sink注入context features改变信息流，需核对照及不良副作用。 |
| 10031 | 最小消歧 | ToM causal tracing/activation steering可能只是既有机制的新任务；需核新的干预边界。 |
| 10044 | 待核验 | attention importance偏置与尾部重复形成KV正反馈，是具体cache选择失效路径。 |
| 10055 | 最小消歧 | 扰动鲁棒训练→clean alignment暴露VLA目标冲突；需核是否超出普通curriculum及预算混杂。 |
| 10064 | 最小消歧 | LAION零样本linear-attention比较；只核是否改变可行性/等价边界，规模排行本身不足。 |
| 10065 | 待核验 | 全双工speech coarse-binary timing动作空间区别raw token GRPO，保留语义与时序成本边界。 |

apr03独立阅读09557、09595、09666的完整官方题摘，确认上述三项有具体准入机制；同时阅读09574、09577、09588、09617，确认不能仅据应用/ROADMAP关联保留。该校准仅证明准入口径，不证明日期或采用结论。

OpenAI Apr13事件已由apr02重抓RSS确认：`Enterprises power agentic workflows in Cloudflare Agent Cloud with OpenAI`，`Mon, 13 Apr 2026 06:00:00 GMT`，官方URL为 `https://openai.com/index/cloudflare-openai-agent-cloud/`。root已读核心说明：模型接入/部署可用性与Sandboxes产品合作，未公开新的机制或独立验证条件，前分母关闭；不能把‘secure production-ready’宣传作为安全保证。Google Apr13教育skills核心文：Executive avatar/rubric与Evaluator对话、人类一致性验证属于教育评估应用，未分离出本项目的新LLM评价机制，前分母关闭；其date-only不再请求不影响处置的精确时刻。

### 10071～10556的52项完整题摘

本批又实际读52项完整摘要，累计124项。以下不是最终分母；日期、必要证据和独立逐项准入仍须处理。

| 身份尾号 | 判断 | 原文增量或关闭理由 |
| --- | --- | --- |
| 10071 | 待核验 | token-specific visual-attention双层contrastive anchors，需核与固定layer/额外compute的对照。 |
| 10072 | 最小消歧 | 并行生成收敛→触发CoT与hybrid reward scorer可能只是成熟组合；只核新的validity/cost边界。 |
| 10074 | 待核验 | multi-token GMM下Transformer DDPM收敛/MMSE机制；须限定population及数据假设。 |
| 10079 | 待核验 | SFT收敛仍未学习训练子集，controlled interventions区分五类原因，可改变仅看aggregate训练验收。 |
| 10091 | 最小消歧 | 静态全局importance mask再column更新；只核相对已有PTQ的实际机制变化。 |
| 10096 | 前分母关闭 | embodiment接口、memory和critic feedback三成熟模块组合；题摘未分离新的控制条件或机制，full privilege本身不构成可靠性。 |
| 10098 | 前分母关闭 | attention sink分类/趋势综述，摘要未解决具体知识分歧或提供新综合反证。 |
| 10103 | 待核验 | 被SWA驱逐的tokens进入linear state，local blocksparse与两阶段distillation；核历史保真/成本共存条件。 |
| 10134 | 最小消歧 | 可信prompt隔离planner+hard/intent验证与既有tool控制相近；只核新攻击/有效性边界，0% ASR不自动构成通用机制。 |
| 10135 | 待核验 | sentence boundary而非任意dummy token影响内部表示；需核同token预算/文本结构控制。 |
| 10152 | 待核验 | MoE self-assisted speculation无需额外draft训练，memory-offload bandwidth与batch效益是具体分支。 |
| 10158 | 待核验 | 同时分解MLP/attention与causal intervention解释LC0并行推理；小模型/棋类不作为排除理由。 |
| 10180 | 待核验 | PTX kernel依赖支持细粒度heterogeneous GPU disaggregation，需核通信/调度正确性和端到端条件。 |
| 10182 | 最小消歧 | coding credit把token/test/time联合约束；只核是否改变行为/评价条件，而非重复cost-aware原则。 |
| 10187 | 待核验 | wave-aware bilinear latency、sparse sampling与dual table决定kernel参数；核预测失配/摊销，拒绝‘消除取舍’泛化。 |
| 10189 | 前分母关闭 | confidence/semantic entropy转换NL quadrant，再PPO与RAG是既有校准/grounding组合；摘要未给新knowledge possession验证机制。 |
| 10219 | 待核验 | entropy pivot与中间视觉锚定失效对应，HVAR/FRM干预；需分离相关性和因果归因。 |
| 10228 | 前分母关闭 | forward/backward trace、SFT与teacher-filtered semi-online DPO组合；摘要未分离新反思或评价有效性机制。 |
| 10235 | 待核验 | Code Property Graph静态程序prior改变KV选择，核同memory预算与结构分析成本。 |
| 10261 | 待核验 | fork-merge DAG在工具调用正确之外区分navigation失败，补线性tool benchmark盲点。 |
| 10268 | 待核验 | tiled inversion与noise-damped manifold guidance应对训练分辨率外重复结构；核身份保持和成本条件。 |
| 10286 | 待核验 | static capability prior与request-conditioned scorer的OOD排序/校准取舍，非risk score替代权限。 |
| 10290 | 待核验 | 单agent aligned不保证organization aligned的受控多agent反证；需核goal、utility与misalignment evaluator。 |
| 10299 | 待核验 | 对安全prefix的retrieval抑制与image anchoring双目标攻击；核梯度冲突和attention因果主张。 |
| 10300 | 前分母关闭 | doctoral研究计划/预期产物，无已成立的新执行或验证证据。 |
| 10311 | 最小消歧 | unified artifact KG/provenance/dataflow可能重复现有平台原则；只核抽象spec→实际跨平台调度的新约束。 |
| 10333 | 待核验 | sparse temporally-factored predictor分离appearance/dynamics，causal inference组合zero-shot能力；核训练预算与物理解释。 |
| 10335 | 前分母关闭 | difficulty route、三expert、verifier与consensus用于GSM8K；仅组合后accuracy，不给新机制/边界。 |
| 10352 | 待核验 | harness typed pages、minimum fidelity、lifecycle validated writeback；核可控fault与fit-budget条件。 |
| 10367 | 待核验 | talking/listening不同temporal scale的Gaussian kernel与dual audio；核lip sync/global context冲突。 |
| 10387 | 最小消歧 | LLM推导GPU thread mapping与upfront amortization；核exact mapping/recursive ceiling是否超出普通kernel自动生成。 |
| 10390 | 待核验 | RTL永久GPU fault→Megatron stochastic injection分离datapath/precision对SDC的敏感性。 |
| 10403 | 待核验 | 修改instruction interpretation的latent alignment/内部adversary；核攻击权限及unlearning指标不能直接当遗忘证明。 |
| 10438 | 前分母关闭 | Whisper非speech域数据fine-tune/linear-probe提升，降低audio-LLM训练成本仍是goal，非已验证机制增量。 |
| 10465 | 前分母关闭 | Langevin教材式统一解释，题摘未提供新比较证据或解决本项目具体既有争议；不采用‘理论优于VAE’宣传。 |
| 10480 | 待核验 | lineage路径的隐性交集/污染传播与root-level采样分支；核推断图是否能支撑provenance事实。 |
| 10493 | 最小消歧 | PRM step reward用于SWE的结构已成熟；只核新的intermediate/final success失配条件，而非换任务保留。 |
| 10495 | 待核验 | knowledge/output/input ambiguity分离揭示单confidence信号失效；需核控制与UQ评价。 |
| 10496 | 待核验 | rotation平滑activation、cluster centroids吸收weight outliers与GPU/CPU kernel耦合。 |
| 10500 | 待核验 | visual/text gradient差与token复杂度驱动replay/depth routing；需核梯度原因及预算匹配。 |
| 10502 | 前分母关闭 | analogy retrieval→rules→moderation端到端组合的领域accuracy，未新增系统有效性条件。 |
| 10506 | 待核验 | forward/reverse查询的大幅不对称暴露temporal shortcut；核训练干预与真正因果理解的边界。 |
| 10508 | 待核验 | 现代8B self-repair的受控反证与repair/resampling预算曲线；不能把累计pass gain当每轮普适收益。 |
| 10511 | 待核验 | counter-intuitive cases下CoT收益减弱，familiarity与accuracy脱钩；核案例覆盖与统计依赖。 |
| 10513 | 前分母关闭 | log发现行为再加corrective prompt的成熟mentoring过程，未分离新的有效性条件。 |
| 10516 | 待核验 | executable function dependencies而非text similarity选择知识，核依赖图/检索预算成本。 |
| 10517 | 最小消歧 | 大规模三阶段egocentric curriculum；与10506有明显问题/方法交集，先核family/重复与新贡献，不能以46M规模直接保留。 |
| 10539 | 待核验 | semantic clustering重排page locality及动态hierarchy，核选择精度与CPU/GPU transfer共同成本。 |
| 10545 | 前分母关闭 | Four Causes教育dialogue prompt/用户engagement，是HCI应用非基础模型系统新机制。 |
| 10546 | 待核验 | differentiable codebook prior把entropy loss与VQ representation耦合，核rate-distortion和test-time control。 |
| 10547 | 待核验 | benchmark要求训练并提交真实model artifact且闭合online RL，而非脚本/SFT static成绩；核grading泄漏及固定预算。 |
| 10556 | 待核验 | 同architecture/scale/pretraining控制AR/dLM hallucination，并区分NFE/refinement与独有failure。 |

### 末段31项题摘判断

以下31项完整摘要已读，累计155个题摘身份；这不是155项确定候选。尤其本段各记录的v1 Updated并未建立09:00前公开：拟保留项先隔离日期，不把该字段改名为first-public。10827当前记录更新到6月，需恢复精确事件；明确贡献排除项不为无关日期继续索取材料。

| 身份尾号 | 判断 | 具体依据 |
| --- | --- | --- |
| 10567 | 潜在贡献，日期隔离 | proximity-biased初期unmask改变后续生成路径，early planner/EOS annealing是具体dLM分支；须核受控比较，Updated01:00:01Z不证明窗内。 |
| 10577 | 潜在贡献，日期隔离 | 正当GUI请求可因环境和执行结果造成伤害，需分清入口意图与effect安全；合成任务/旧守卫漏检不证明普遍失败。 |
| 10585 | 最小消歧，日期隔离 | sycophantic GRPO与中性SFT比较可能混杂objective；ECE变化p=.41不能作确定恶化证据，只核决定准入的受控关系。 |
| 10590 | 最小消歧 | 跨语言embedding映射与alignment coefficient可能仅语言适配；核是否有新的可复用表示边界，非换语言直接保留。 |
| 10597 | 潜在贡献，日期隔离 | 动态kernel选择在oracle下可提速、实际路由反不及静态，是信息/开销与执行收益的反证；核v1是否包含当前摘要结论。 |
| 10603 | 最小消歧 | information-theoretic MoE剪枝的准入取决于新度量改变什么选择，不能只凭统一框架或提速宣传。 |
| 10636 | 潜在贡献，日期隔离 | 没有显式forget dataset时用metadata形成遗忘目标，改变数据保留条件；核retain/forget估计与泄漏边界。 |
| 10658 | 前分母关闭 | typed primitive、审核、hash log与delegation组合的少量申诉应用，未分离新授权/原子执行机制。 |
| 10666 | 潜在贡献，日期隔离 | shared similarity proxy避免多模态两两蒸馏组合，核高阶信息近似及模态规模的成本/质量边界。 |
| 10667 | 潜在贡献，日期隔离 | 从上下文探索学习grammar再约束生成，区别人工固定grammar；核所学规则的有效范围与未见输入失效。 |
| 10674 | 潜在贡献，日期隔离 | privileged teacher-only skill与importance-weighted reverse-KL、teacher refresh形成训练分支；核因果消融与坍塌反证。 |
| 10681 | 最小消歧 | reasoning backdoor防御的两阶段critical-thinking训练，核是否超出通常robust fine-tuning及攻击集迁移，不因安全标签自动保留。 |
| 10688 | 最小消歧，日期隔离 | 错teacher轨迹PPL加权KL与正确轨迹MLE的分组信用机制可能有增量；核权重/目标与常规distillation差异。 |
| 10690 | 潜在贡献，日期隔离 | 同maze的adjacency/visual表示及语义trace覆盖反差，可限定环境表示与累积状态推理的区别；不能据此否定全部world model。 |
| 10693 | 潜在贡献，日期隔离 | 受控扰动区分单chain依赖与答案一致性，核faithfulness instrument本身的validity，不把相关当因果证明。 |
| 10697 | 潜在贡献，日期隔离 | attention mass与value norm对sink reliance的不同判断，核数学假设与干预证据。 |
| 10701 | 潜在贡献，日期隔离 | generative CoT critic通过in-context actor条件更新替代scalar value，核critic成本及目标非平稳性。 |
| 10703 | 潜在贡献，日期隔离 | 根据online几何不足增长/剪枝单head给出有条件容量路线；核有限minimal-sufficiency定理，不因小任务排除也不外推LLM。 |
| 10727 | 潜在贡献，日期隔离 | heavy-tail reward下KL与Rényi约束改变Goodhart/BoN界，核tail假设和具体保证。 |
| 10733 | 最小消歧 | persona agreeableness与sycophancy的相关性不证明trait造成错误；核是否有超出已知风格偏置的受控边界。 |
| 10739 | 前分母关闭 | 按难度缩短过度reasoning、收益递减的摘要重述成熟预算原则，未提出改变既有选择的重要机制或反证。 |
| 10784 | 前分母关闭 | TorchUMM统一任务接口及功能目录，不以组件数量或支持任务数作为新执行/评价机制。 |
| 10788 | 最小消歧 | 工具知识双向alignment加SFT/RL可能是既有训练组合；只核新的知识internalization条件。 |
| 10791 | 潜在贡献，日期隔离 | QKV前非线性与content skip的architectural branch，核冻结模型/参数与compute预算匹配，不把两个分数当普遍收益。 |
| 10799 | 最小消歧 | Polish tokenizer fertility、FOCUS embedding和分阶段训练；核是否只是成熟语言适配路线的新operating point。 |
| 10800 | 最小消歧 | exploit verification-before-repair本已合理；核跨语言检验机制的实际增量，不为安全包装自动保留。 |
| 10827 | 潜在贡献，日期隔离 | reasoning diversity/depth/breadth的受控比较可修正搜索预算判断；当前Updated6月，不能确认本窗v1贡献。 |
| 10842 | 最小消歧 | atomic chunk/resume/scratch handoff是已有恢复协议；核是否新增Agent特有失败条件，测试次数不是贡献证明。 |
| 10848 | 潜在贡献，日期隔离 | Transformer学习latent mixture transition的显式机制与Bayes/Markov对照，核深度与检索匹配假设。 |
| 10857 | 潜在贡献，日期隔离 | diffusion score查询下界与adaptive noise-level约束可限定sampler可行性；核oracle精度/范数/维度假设。 |
| 10866 | 最小消歧 | professional-work simulation覆盖与隐式fault，核环境validity是否有新可检查条件，不能凭领域任务数保留。 |

14个每日来源的窗口结果仍待合并到当前日报；OpenAI Apr13T06Z和Google Apr13核心说明已完成准入关闭，不再普通pending。本批最小消歧、日期隔离、候选证据、Books比较及非作者日级Gate尚未完成。旧README仍进行中，不计入4月已验收数量。

### 定点消歧与公开日期依据（续跑）

- `2604.09557v1` SPEED-Bench：已直接核 [exact-v1](https://arxiv.org/html/2604.09557v1) §5–8、Table1、配置Appendix H及[官方版本历史](https://arxiv.org/abs/2604.09557)。语义真实输入与随机token改变proposal可预测性/路由分布；accepted length不直接决定throughput，draft长度与并发互相制约，vocabulary pruning的多语种long-tail代价不可隐藏。评价配置区分GPT-OSS120B/Llama70B单B200与Qwen/DeepSeek多卡TP/EP；默认greedy、Table1的temperature1例外、固定输出200及输入padding、client高并发GIL限制均约束作者结果，SLO未披露。23%均值只属于特定GPT-OSS/EAGLE/TRT实验，不推广所有synthetic workload；输入/RoPE错配不是唯一解释。Ch48已有AL≠throughput和verify预算边界，但真实输入分布及vocab裁剪可能构成窄缺口，尚不作Books采用。官方abs的v1 **submitted** 为2026-02-10 16:19:56UTC，HTML页头同为Feb10；这只能证明投稿日期，不与April公告ID自动构成首次公开冲突。此前将其写为公开日期反证的判断撤销。仍须结合官方公告规则、相邻ID批次和本family版本记录判断落窗；不得单凭submitted回拨Feb10，也不得单凭DataCite确认为Apr14 owner。日期工作只涉及本family，不推倒已完成的机制审阅。
- `2604.09579v1` Vigil：最小准入消歧已读§3.2.1–3.2.3。on-call持续旁听→人工解答抽取QA、Accept入库、unaccepted后Keep/Update/Delete、外链抽取是既有RAG/derived-memory反馈组合。Keep还把没有后续讨论视为正确，不能从部署规模推连续纠错有效保证。题摘和必要方法没有分离新的记忆验证/授权机制或可改变既有边界的反证，**前分母关闭**；不是把“无反馈不等于正确”的成熟原则包装成新贡献。日期未另核，HTML Feb25页头保留为身份线索而非Apr14事实。
- `2604.09620v1` LLM Nepotism：最小准入消歧读§3.1–3.2。same-ID简历stance改写、顺序双pass、合成董事会把评价者偏好引入领域治理；角色/文本立场影响judge的成熟机制在新HR场景验证，没有分离改变通用evaluation contract的独立新机制。**前分母关闭**，不把合成组织后果外推真实治理或因涉及多Agent自动保留。
- `2604.09678v1` NetAgentBench：必要准入读§III-A–C及VII-C。STOP只是Agent声明；执行后需等协议收敛并对稳定环境state predicate验证，read动作不改变配置、config触发pending→stable/error。较低meltdown率可能只是早退，token效率也可能随低完成度虚高；这些是明确的新评价混杂证据，保留为待评分/日期及标准审阅候选，不把网络任务数量当准入理由。FSM模型假定total/injective initialization，不能认作实现已证明正确。
- `2604.09679v1` HCP-MAD：最小准入消歧读§3.1–3.3。异构两模型先独立生成、相同答案停、不同则pair debate再扩容投票，是既有一致性门控/渐进预算组合。当前方法没有新的独立正确性判据；“异构即可靠”不由agreement保证。**前分母关闭**，不因更少token或组件拓扑新增普遍系统结论。

### 第二批定点消歧（尚非日报验收）

- `2604.09695v1` Privacy Preservation：已读[精确版本](https://arxiv.org/html/2604.09695v1)方法及实现说明。识别敏感对象后移除/模糊/遮罩，再由LLM评估privacy/utility，是已有检测—编辑—评价的组合；原文也承认所用保护方法为传统方法。材料未分离出新泄漏渠道、保护保证或改变现有方案适用边界的受控证据。**前分母关闭**；不因标题含privacy就构造新的安全知识增量，亦不把LLM打分当隐私保证。
- `2604.09712v1` LAST：必要准入消歧实际读§2、§3。受控提示比较显示空间metric estimation更受益于图像提示，direction relation更受益于文本，同时给两者可能退步；这提供了工具返回表示与消费能力不匹配的具体边界，不以atomic tool→skill的组件组合本身作为贡献。**拟标准审阅候选，分母未冻结**；后续只补足§4关键对照、预算与失败条件，核真实owner后再判已有覆盖或长期缺口。三阶段教师数据与部分工具输出不完整后回读原图，不能直接归因为skill结构独立收益。
- `2604.09752v1` A-IO：精确版本摘要及§3–5已恢复。entropy阈值选择小/大模型、任务识别后仅对QA/math使用PLD，属于已知路由与静态执行组合，不能仅凭NPU场景准入。原文未使用“exact PLD”的表述，先前笔记将背景保证错写成作者明说，现撤销。具体待核问题是：§4.2把PLD配置为ngram6/lookahead2，却未说明验证、采样与输入控制，§5.4 Table3报告7B HumanEval从62.80降到41.46；不能把未披露验证语义的实现反推为正确的lossless PLD必然损害质量。§5.2的混合收益是以合成300-query分类矩阵加权的数学期望，§5.6还用按任务加权TPS，不能冒充真实混合请求队列的端到端吞吐。**拟保留标准评分5（2/1/2）、因与正确性/评价判断冲突对相关内容深入核验，争议暂缓**：本次可读方法与关键表已读到足以隔离主张，恢复条件为精确PLD验证/采样实现、同输入评价配置及真实mixed-arrival trace；不索取无关NPU全文，也不采用作者普遍加速或质量保证。日期与非作者处置仍待核，不提前进入最终分母。

本批没有新增Books正文，也没有把已读必要段落记成完整日报。非作者准入/处置复核仍需汇总；原始题摘与先前判断全部保留，可追溯改判。

### 第三批消歧与标准证据（非最终分母）

- `2604.09791v1` Pioneer Agent：必要准入消歧读§2.4、§2.6的failure taxonomy、live probing、replay/regression约束及rollback。LangGraph工具化的数据/超参/学习策略搜索、先冻结验证集再定点修补，是已有训练反馈闭环的组合；阈值驱动重做数据/调参/加例没有新增可复用正确性或发布保证。受控公共任务与synthetic日志不能把production-style案例升级为部署验证。**前分母关闭**，不是因为SLM或工业场景排除，而是未分離出超出成熟闭环的机制/边界增量；保留原题摘与读到的方法依据。
- `2604.09917v1` Explanatory Equilibrium：必要消歧读§4.2–4.3 Eq1–3及§6.2。typed claims、概率audit和预期惩罚的激励式解释，条件是可取得确定ground truth；金融一次性toy模拟没有free-text baseline，不能分离结构与额外信息的收益，也未建立新的开放环境验证可行性。原文把结果限定为institutional而非经典Bayesian equilibrium。**前分母关闭**，不将熟知可核验信号/激励原理在新场景中的重述或抽样预算指标包装成通用Agent新保证。
- `2604.09890v1` MT reasoning errors：拟保留 `2+1+2=5` 标准审阅，**证据已达到标准深度，日期与非作者仍待核**。[exact-v1](https://arxiv.org/html/2604.09890v1) §3.2的人评把输出质量和trace错误分开；§4.1在thinking-disabled下回放被编辑trace，§4.2/Table5中修正trace与COMET可相反变化、两模型的局部编辑敏感性不同。它检验的是这一回放接口下的条件影响，不证明原生thinking中同一因果路径，也不证明trace错误都不重要。Hindsight/phrase oracle依赖reference，不能作为部署输入；人评仅两种语言各30样本，其余评估受自动judge/COMET限制。采用命题是“中间状态质量、被实际消费与终局outcome须分账”，不是翻译排行榜。与`PLATFORM-EVALUATION-SYSTEM` Ch66的“行为预测是独立Evaluation Task”及`No-Aux/Generated-Aux/Validated-Aux`干预段对读，已有具体trajectory protocol、干预和outcome的职责与oracle边界，暂定**已有覆盖**、不新增同义正文。Offline evaluation不涉及serving SLO；若讨论性能，其硬件、精度、batch/concurrency未由本次必要阅读建立，记Not Disclosed而非推定配置。

### 第四批必要消歧与证据（待独立复核）

- `2604.09945v1`：官方HTML实际呈现题目为 *Cross-Cultural Value Awareness*，与身份快照的 *Value Attribution* 不同，样本叙述也与原题摘线索不同。已读HTML §2 的同人不同文化背景、MFT/LLM分类和Jaccard/词汇统计；它们是现有反事实偏置评估的领域应用，不能从规模推新的有效性保证。但不能用可能变动的正文冒充exact-v1准入依据；后续只核官方PDF/v1必要题摘与对应方法，若仍版本冲突则隔离，不展开完整版本史。
- `2604.10015v1` FinTrace：拟 `2+1+2=5` 标准**已有覆盖**，日期/非作者待核。已读[精确HTML](https://arxiv.org/html/2604.10015v1) §2.2 Table1、§3.1 Table2、§4.1–4.3及Appendix D：gold-trajectory相对步数和重复调用可奖励少行动，工具F1、信息使用、judge过程质量与终局答案不能互相代替；同一9B模型SFT/DPO的过程改进也未消除低最终质量。九指标均值及LLM judge不是独立业务真值，成功工具调用过滤/合成干扰池和偏好对选择限定训练结果。Ch66“Tool成功要从Component扩展到Information Use与Outcome”已实际承载这一分账，不因新金融任务或dataset规模新增正文。Offline FMP/MCP evaluator，不采用跨域性能、硬件或SLO保证。
- `2604.10055v1` STRONG-VLA：拟 `2+2+2=6` 标准候选、因Ch26具体训练分支缺口补足必要深入证据。实际读§4、§5.1–5.4/Table2–3、§6、Appendix C.1–C.3：先在逐步扩张的扰动分布训练，再以更低学习率的clean阶段回到nominal任务；同一扰动评价下joint、无curriculum、无StageII消融提供局部比较。不能从TSR直接证明gradient conflict，Table3未单独控制learning-rate阶段变化/所有训练预算，Appendix“仅distribution不同”也被Table5的5e-4→5e-5、50k→8k限定。Gaussian noise上可显著不及RobustVLA，未见visual扰动和动态artifact并非统一改善。配置为OpenVLA/OFT LoRA32及pi0、LIBERO、L40S BF16无量化、effective batch16；实机只一AIRBOT/OFT任务且step数减少，控制频率数值、SLO及重复统计未由必要阅读建立，Not Disclosed。拟采用仅为受限训练顺序分支及其混杂边界，不作开放物理安全或通用更强保证，待Books正文比较/独立核验。
- `2604.10064v1` Linear Attention：拟 `2+1+2=5`，因数学保证冲突深入核相关命题，**争议暂缓**。已读[精确HTML](https://arxiv.org/html/2604.10064v1) §3 Eq4–7、§4.1–4.2。单位Q/K使affine kernel非负，不推出Eq6的每项归一化权重≤2/i：取i=3、q=k1、k2=k3=−q，分母2、第一项权重1>2/3。这只反驳缺少额外假设的该上界与据此的必然过平滑解释，不否定所有linear attention或作者曲线。删分母后的bounded单项系数也不等于整体输出归一化/长度无关。作者层级H200 batch4、8头d64对FlashAttention2；OpenCLIP三ViT在LAION400M/四A5500，global batch64/16/4、ImageNet21K评价且需更多epoch；不把单层百万token速度比作端到端同质量训练收益。恢复条件为上界所需假设/勘误、长度归一化机制与可比训练成本证据；不纳Books。公开日期与非作者争议核尚未完成。

上述拟入选三项的原始v1 Updated分别为`2026-04-14T00:21:11Z`、`00:25:16Z`、`00:25:56Z`，结合连续公告赋号批次和官方常规08:00北京时间slot，可支持待独立核验的`[08:00,09:00)`推断，不把这些Updated字段改称精确首次公开时刻。后续revision不用于替代当时v1。

### 第五批必要消歧与证据（待独立复核）

- `2604.10031v1` CoSToM：已读[精确HTML](https://arxiv.org/html/2604.10031v1) §3.1–3.3、§4.1/Tables1–4。冻结读出decoder的BDI问答loss通过指定层激活回传到encoder的LoRA，decoder及更深encoder层不更新，随后将patch用于对话；这是一条有条件的中间表示训练接口，不是仅给ToM生成加prompt。比较Full-Layer-LoRA还改变了encoder/decoder可训练范围，LatentQA则训练相反一侧，不能把结果全部归因于BDI内容；较浅层可解码性不证明未干预模型实际因果消费该概念。协商/说服数据及GPT judge下，部分对话指标反而不及对照。拟`2+1+2=5`标准候选，暂定仅报告：可保存受限冻结probe训练分支，不采用普遍心智理解或全对话收益；若实际Books对读显示长期接口缺口再深入采用，不以主题已有覆盖关闭。
- `2604.10072v1` Reason Only When Needed：必要准入消歧读§3的多温度/概率采样、最大答案占比阈值、额外CoT候选及teacher/human标注的hybrid reward。它组合共识路由、best-of多路径和已知reward训练，没有分离出改变共识有效性、校准或总预算边界的新机制；一致率也不是正确概率。**前分母关闭**，不将为已知组合命名或GRPO字样作为贡献。没有因Eq9记法含糊而扩出不必要的理论深审任务。
- `2604.10091v1` SEPTQ：**不是04/14首次公开候选，不评分、不本日写Books**。HTML首页载KDD25与DOI `10.1145/3690624.3709287`，apr01独立打开[Crossref出版方元数据](https://api.crossref.org/works/10.1145/3690624.3709287)，同题/作者published-online、published-print、issued/assertion均2025-07-20；created=2025-04-04不是first-public。正式发表已经早于April2026，需作为旧家族去重；如以后恢复owner只定点核2025真实首发，不扩大本窗。有效方法证据保留：§4.1–4.2/Eq4–5/Algorithm1、§5.1–5.6/Tables1–5/Fig5–7，以单weight rounding error平方除以两倍inverse-Hessian对角估计importance，并非平方和；一次冻结全矩阵保护mask，再逐列量化补偿。128个C4、2048-token校准，OPT125M–66B/LLaMA7B–30B、A800/block128；保护选择更快不证明整个PTQ更快，Table5总体仍慢于GPTQ，运行kernel/batch/并发/SLO未披露。原拟6分与Ch49 gap提案撤销为本窗去重终态，不删除已读证据。

八项非作者定点复核已完成（apr01）：10015/10031/10072/10134既定有限Existing/Only/前关闭判断通过；10064 Eq6归一化mass反例独立通过，理论中心隔离不否定全部LA；10055确认Ch26窄训练分支缺口，但Table5学习率/步骤并未完全匹配，§4.1.1“role-spoof holdout”与§4.1.2 phase2 role-training冲突，不采用特定role holdout安全保证；10091按上述2025正式发表去重；09945当前HTML题名/样本与April库存不符，PDF/v1网页缓存失败、有界下载/解析无有效PDF，现为Version Evidence终态保留项，需可绑定April原版作者稿或官方版本说明才重开，不用污染正文关闭原题摘。
- `2604.10134v1` PlanGuard：安全机制必要深入已读§IV-B/C Eq6–7/Algorithm1、§V-A/B、§VI。隔离planner只看用户指令和tool定义；exact工具/参数匹配可放行，工具名未在计划则拒绝，参数不匹配交给读取action thought的LLM intent verifier。它不是全路径deterministic授权器，原文也承认依赖外部账单时planner缺参数ground truth。1054个InjecAgent案例、17用户工具/62攻击工具、DeepSeek-V3.2同backbone；victim系统还被要求执行tool-return指令，0 ASR与较低FPR不证明adaptive/open-world安全，§VI的latency是未来优化议程而非实测。拟`2+2+2=6`安全深入，受限机制暂判Ch72“source sensor→authority registry→step guard→deterministic policy”及“Goal Alignment不等于组合授权”已有具体覆盖；不采用plan干净必然保证action安全的中心泛化主张。恢复该强保证需要对StageII参数/thought注入、context-dependent参数与独立benign集的证据，不扩大为索取所有私有实现。

本批仍未冻结日期/候选，未改Books。题摘已读、准入消歧、标准/深入证据与实际采用分开记录，不将仅有全文URL称作读完。

### 恢复后第六批：必要证据与贡献裁决

本批复用已读完整题摘，只补准入或采用命题需要的原文；没有把1334条宽库存扩成全文队列。以下三项机制缺口交apr02独立核查，未获许可前不写共享Books，日期仍须和本日既有公告批次/精确版本依据联合确认。

- [2604.09595v1 — GAC](https://arxiv.org/html/2604.09595v1)：实际读§4.1–4.3、§5.1–5.3与§7。压缩后不规则维度触及kernel效率边界，先在目标硬件profiling形成各层合法对齐候选，再按同一全模型参数预算做多选knapsack分配；不是统一round-up或运行时padding。Ch49的descriptor/heuristic/tile与结构稀疏段还没有“压缩参数分配先服从硬件可行shape集合”这一分支，拟2+2+2=6、真实gap深入。评价限Llama3-8B、dense压缩15%、FP16、PyTorch2.9.1/CUDA12.8，Table5为batch1、1024-token prefill，不支持decode、优化engine或SLO。ASVD仍远劣dense PPL，PiQA/HellaSwag部分退步；不能采用不损质量、无额外部署成本或全部硬件的保证。DP成本量化也是近似，不宣称原连续问题exact最优。
- [2604.09603v1 — ECHO](https://arxiv.org/html/2604.09603v1)：实际读§2、§3.1–3.3、§5.1/5.3和直接相关成本设置。离线找有区分力的深度、部署只在这些位置检查depth-specific confidence；共享batch节点预算优先跨请求延伸depth，暂时无可延伸请求时才扩大局部width。Ch48已有target-batch机会成本及input-adaptive depth，但没有这个两级资源决策，拟2+2+2=6、gap深入。Alg1仅检查budget>0后减W_topk，余额小于一次分配时不能据此证明严格cap；phase2的w与widen(k)/减W_max也不一致。可采用策略分支，但实现仍须按实际分配节点做硬预算检查，不照录最优或严格cap保证。8×H10080GB、BF16、greedy下，低/高负载还使用不同树预算，不能把全部收益单归sparse gate；MAT/depth也不是实际节点利用率，更不等任意sampling/SLO收益。
- [2604.09651v1 — FlowHijack](https://arxiv.org/html/2604.09651v1)：实际读§4.1/4.3–4.4、§5.1/5.3/5.5、AppendixD与E.1–E.2。白盒污染fine-tuning权重/目标，在flow早期时间段诱导恶意方向，同时匹配clean vector-field norm；不是仅prompt注入。等范数不等方向或合法任务，AppendixD单任务速度曲线也不证明统计不可区分。LIBERO ASR是task failure代理而非固定恶意终点达成；PL/IP两目标对距起点0.1m guard的结果不同，clean finetune也不能保证清除。现Ch26主要是外部sensor扰动与controller边界，拟补连续action generator内部方向×幅值的供应链威胁分支，2+2+2=6、安全深入，待非作者确认真实gap。BadVLA为作者适配至连续π0的基线，4×4090仿真配置不是全部实机控制成本，不采用普遍防御或physical safety保证。

另外五项已完成最小消歧/标准审阅，未为它们新建Books章节：

- [2604.09587v1 — MobiFlow](https://arxiv.org/html/2604.09587v1)：实际读§4.1–4.2、§5.3/5.5。按task收集成功轨迹、给同转移结构状态一致标签、union-find合并成可回放图，以降低live GUI开销；CR/CVR/AMR/TTA分开。拟2+1+2=5、标准完成、仅报告此受限harness构造。所谓完整图的覆盖依赖采集/人工标注，并未由7条轨迹或均值branch factor证明全部真实合法路径；错误动作保持原界面/空白/特定提示也是模拟约定，不能外推API副作用、开放UI变化或物理安全。新的具体构造可保存，但不把图内oracle升级为环境真值或把新benchmark名称作为长期机制新增。
- [2604.09604v1 — partial-observation gridworld](https://arxiv.org/html/2604.09604v1)：必要消歧读§3–4，19×21 ASCII、5×5局部视野、oracle坐标、已揭示地图累积、400步上限、三固定布局/每设置13次；不含classical replanner，API解码并不一致。五个动作范例改变部分模型的loop/碰撞和路径效率，但不分离训练pipeline、thinking mode或compute switch因果。**前分母关闭**：是在已知部分可观察规划/提示敏感性约束上的有限模型比较，没有定位值得改变本项目设计选择的新机制或有效性条件；不是因toy、小模型或robotics标签排除。
- [2604.09606v1 — APST](https://arxiv.org/html/2604.09606v1)：读III-B/C、IV-C与V，固定prompt的Bernoulli/binomial、225个AIR派生prompt、temperature×采样深度、breadth/depth不同分母，是此前同作者[2602.11786](https://arxiv.org/abs/2602.11786)已公开的APST主张/协议的再次呈现。当前材料没有显示改变既有重复推理失效判断的新机制、修订说明或独立条件证据，**前分母关闭**；Ch66“Safety Evaluation还需要Depth-oriented Repeated Inference”真实承载这个协议。只据必要内容关闭贡献，未凭submitted字段裁定本稿首次公开日，也未声称两个ID已完成全发表史合并。普通独立抽样不外推生产风险；浅深估计变化也不证明真实每次failure概率随采样次数单调升高。
- [2604.09611v1 — multi-request energy](https://arxiv.org/html/2604.09611v1)：实际读§4.1–4.3、§5.0.2–5.0.3和§6。Llama2-7B/A10040GB、vLLM0.9.1/Parrot、T0.7/top-p1、16用户及batch1–16；十次重复/95%区间、CPU/GPU/DRAM能量分账。batch趋势随共享prefix、顺序依赖和角色异质性反转，拟2+1+2=5、标准完成、仅报告此条件证据。没有冻结全部quality/SLO或直接干预每个解释组件，role/queue/cache的因果说明仍弱于归因宣传；§4.3 throughput称generation-only，Listing1却以workflow total time计，不能混同两种分母。Ch70已有成功goal/整机/质量合同核算，但并非此算法全部已有覆盖；不因此新增普遍vLLM优于workflow scheduler结论。
- [2604.09624v1 — SECL](https://arxiv.org/html/2604.09624v1)：实际读§3.1–3.3、§4.1–4.3、Limitations及AppendixN/Q。base-model（无LoRA）对True/False的discriminative signal经distractor归一化，给verbal confidence作有界方向目标；entropy/Page-Hinkley触发burst、bin差筛选更新、adapter跨domain累积。拟2+1+2=5、标准完成、仅报告具体label-free更新分支。2K问题/four domains、2–8B选定有generation–discrimination gap模型、A100/A6000、r8/q-v LoRA；更新不读gold不代表整个超参选择未读标签，伪标签相对偏好不是事实概率。Qwen3B无gap、self-consistency替换目标退步、部分domain ECE和部分模型AUROC退步，禁止只用aggregate ECE判在线拒答更可靠；只mask confidence位置也不隔离共享参数。Ch66已分sensor与truth、模型/estimator/calibration slice及任务质量，本文在线配方留作受限证据，不声称该具体算法已完整写入。

上述第五批裁决的非作者有限结果见后续核验；最后日级来源/集合收口尚未完成。题摘筛选、标准完成、真实Books差异分别记录，没有根据深审成本降分或缩池。

### 第六批非作者与实际写后结果

apr02已按必要精确原文与实际owner有限复核第六批八项，通过具体处置：09595/09603/09651为6分缺口/安全深入，09587/09611/09624为5分标准仅报告，09604/09606在前分母关闭。随后root将前三项实际整合进Ch49压缩形状与kernel候选、Ch48稀疏depth-gates与跨请求节点预算、Ch26生成时间速度场方向投毒三处现有机制正文，apr02再次核对应实际段落及相邻链路通过。结果见[V3非作者机制核验](./V3_INDEPENDENT_MECHANISM_CALIBRATION.md)。这八项的普通单篇复核待办消除，但全日来源/日期/候选尚未收口，不扩大为日级完成。

### 第七批必要证据与owner提案（待有限独立复核）

- [2604.09665v1](https://arxiv.org/html/2604.09665v1)：实际读§2.1、§3.1–3.2、§4–4.2。paired base/FT最后token hidden cosine用于BoN8筛选，提供deliberative-distilled模型与普通instruction-tuned模型不同适用边界；2+1+2=5，安全相关内容深入，拟仅报告。latent/KL分离是相关证据，不证明unsafe输出源于base这一因果路径；best-layer按benchmark选是oracle上界，固定layer12有utility下降，普通IT改善很小。teacher/student、LoRA32/T0.7/top-p1、三攻击集与GSM8K/MMLU共同限定结果，两个模型的PAIR depth8不证明开放adaptive攻击安全。没有重新验证全部42配置或复现实验；不把任务ASR改写成生产风险、未披露运行开销不补作免费selector。具体配方不强行声明已有章节已经完整承载。
- [2604.09666v1 — RAGSearch](https://arxiv.org/html/2604.09666v1)：实际读§4.2–4.4、§5.1–5.5、Appendix B/E。改变backends而保持对应agent protocol的比较，显示强query decomposition与迭代搜索可部分补偿dense retrieval，但multi-hop下graph仍有优势；2+1+2=5，标准完成，拟仅报告具体条件证据。multi-hop gap27.23→26.59本身只是很小缩减，“32.3%”使用另一基线，不合成统一效果。dense语料说明为2018Wikipedia，而graph说明是各question context组织，不能声称全实验corpus完全匹配；各graph context长度、构建与retrieval成本也不同。Qwen2.5系列/2×A10080、top5、RL三epoch/batch32/maxturn5限定结果；运行precision、线上并发/SLO未披露。现Ch76拥有查询/检索/reader身份、flat/graph共存与建图成本，这组结果不要求再写一个GraphRAG必胜/被替代段，也不证明GRPO普遍最佳。
- [2604.09670v1 — N-back interference](https://arxiv.org/html/2604.09670v1)：实际读§2.1–2.3、§4.1–4.3、Discussion、A.3与A.5.12。完整历史可访问、任务专训的浅层Transformer可成功，并不保证预训练chat模型已经实现相同的positional retrieval；lure/set-size/Markov变化与teacher-forcing对照显示内容竞争仍影响回读。表示测量支持中层部分分离、晚层对齐readout，early answer-position hook以SVD方向抑制letter-specific变化提供受限因果证据。拟2+1+2=5，因Ch22的具体mechanistic gap深入：在Effective utilization的容量合同后补“访问≠选择/读出、共享表示竞争”窄链。不得称人类相同机制、所有long context瓶颈或通用controller；五模型干预取方向/强度 sweep最大收益是乐观上界，不证明固定策略跨model/N迁移；10模型non-thinking、26字母multi-turn任务、无externalized reasoning，chat格式与instruction-following混杂及下游相关非因果均保留。真实差异和采用范围待非作者核验后写入。

三项仅完成上述必要阅读；精确日期、最终分母和日级复核尚未完成，普通工作继续。

### 第七批单篇复核与写后续接

apr02已有限核验09665/09666的必要原文与具体仅报告边界，以及09670的原文、Ch22实际缺口和相邻衔接。root将09670的“历史可访问不保证竞争内容的正确选择与读出”落实在Ch22有效利用的容量合同之后；answer-position均值投影的局部证据、最优方向/强度扫参的乐观上界与迁移未证均保留。apr02再次核实际两段与Review note通过，见既有[V3非作者机制核验](./V3_INDEPENDENT_MECHANISM_CALIBRATION.md)。该项为5分gap深入、实际整合；这不预支日期、集合或整日Gate。

### 第八批必要消歧与证据（继续中）

- [2604.09709v1 — OQC](https://arxiv.org/html/2604.09709v1)：实际读§3.1–3.5、§4.1/4.5–4.7与§5，比较实际Ch16的GLU/SwiGLU乘性非线性。辅助低秩分支先作逐元素二次特征，经RMSNorm在投影后host方向上消去平行成分，再lift回原空间与动态gate融合。这个投影仅针对学习的rank空间中一个方向，带epsilon也不是精确正交；lift后不保证与原host输出正交，更不证明整个函数空间非冗余。旧非线性MLP/GLU并非线性函数，不采用“普通FFN只能线性表达”的泛化背景。拟2+1+2=5、标准仅报告此受限分支：CIFAR100的8层/256宽/8头、TinyImageNet64的patch8与三seed、AdamW/选定batch和rank56限定表现；nogate/noortho消融有价值，但跨protocol的学习率/epoch差异不能合并成单因素归因，penultimate readout及dynamic gate方差反例保留。现证据展示局部host/rank/gate operating point，未证明足以改变本书一般FFN设计边界，不把“能对应Ch16”当成长期增量或完整Existing。实际独立处置复核尚待有限核验；精确日期仍随全日归并。

- [2604.09718v1 — Agentic Compilation](https://arxiv.org/html/2604.09718v1)：决定准入的必要消歧实际读§3.2–3.4、§4.3、§5.1–5.2。DOM简化→一次生成JSON blueprint→human gate→确定性执行，仅在selector/schema失败时补读DOM修复，控制流仍在executor。这个选择重复已知compile/execute、语义selector与exception-only调用组合，没有从私有三任务分离出改变本项目设计判断的新机制或有效性条件，前分母关闭；不是因为工程应用、未公开全部数据或没有新runtime协议。46/50、8/10、47/50是编译成功分母，98/95/96%是在成功blueprint中的execution accuracy，不等near100%整个流程可靠；人修正、UI变化极少和摊销O(1)不由这三切片证明，schema通过也不赋予副作用授权。
- [2604.09722v1 — ConfigSpec](https://arxiv.org/html/2604.09722v1)：实际读§3.1–3.2、§4/4.1与§4.3。按draft速度、draft–target接受与设备功率profile，把K选择写成accepted token throughput、token-priced verifier cost与edge drafting energy三个不同目标；拟2+2+2=6、标准仅报告受限配置证据。功率只乘local drafting time，不包括等待/无线/cloud能量，token价线性K的billing也不代表batched provider真实收费或end-to-end成本。RPi4/5、Jetson Orin64、llama.cpp/GGUF Q4–Q8与Llama3.1-70B/Qwen3-32B、Dolly15K限定profile，cloud硬件/precision/线上SLO与全部network条件Not Disclosed。实际Ch48已有edge/cloud的acceptance、network、draft/verify profile与fallback，但并非完整实现本三目标选择器；本稿有限profile尚不要求另写一套普遍optimal configuration准则，保留具体结果而不假称完整Existing。
- [2604.09731v1 — SMART](https://arxiv.org/html/2604.09731v1)：实际读§3.1、Cost Modeling、Sequential Decision/Optimizing及§4协议/§4.2。逐节点比较边际预期target工作与device-profile draft/verify成本，保守系数与batch共享verification budget保留具体机制；拟2+2+2=6，中心估计边界深入，待有限独立核。Eq2把全部root-to-leaf path的prefix概率和取均值，不等树所覆盖候选的总接受进度：两个互斥、各0.5的一层叶子，路径均值为0.5而树覆盖质量为1；稿中未声明随机均匀选路径这一额外执行合同。draft probability替代target probability、Eq13忽略新增path对均值分母变化，也不能因此声称每步真实期望speedup必增或全局最优。收益仅作作者的受限经验，不采用上述估计为无偏保证；RTX Pro6000/L40S、不同LLM/MLLM、T0/1、有限batch与benchmarks，batch1可略输MSD，固定budget的过低/高反例保留。verification拟合曲线并非attention quadratic推出exponential的普遍规律，exactness仍取决于底层target验收，不由tree controller自身保证。需要明确tree验收/路径选择与期望估计的桥及修正该保证，才考虑长期公式采用；是否作为争议终态须非作者核，不预称全文/日级通过。

### 第八批独立裁决与第九批必要审阅

apr02已实际核第八批必要exact-v1、具体owner及反证，通过09709/09722标准仅报告与09718前分母关闭。09731为6分中心估计深入、**争议暂缓**：旧单叶概率0.9加兄弟0.1时，Eq2的path均值0.9→0.5，Eq13却给正增量；仅重命名为surrogate不能恢复逐步必增保证。原文已明确greedy非全局最优，不指控它证明了全局最优。经验heuristic、作者实际测得的有限结果及底层target exact验收独立保留，争议公式不入Books；重开需树验收/路径选择与期望的明确桥、包含分母变化的推导或作者修订。不是删除整篇证据。独立记录见既有[V3机制核验](./V3_INDEPENDENT_MECHANISM_CALIBRATION.md)。本日仍未冻结分母。

- [2604.09741v1 — ExecTune](https://arxiv.org/html/2604.09741v1)：实际读§3.3–3.5、§4.2与§5。小guide的策略不能只按teacher文字质量训练；用受约束core实际成功过滤策略，再SFT，并用结构/非泄漏judge与相对无guide的负回归惩罚训练guide，是具体target-conditioned分支。2+1+2=5，标准完成，拟仅报告。理论的student/teacher mixture和good execution假设不证明任意black-box core已忠实执行；single-turn数学/代码、Haiku版本与Qwen3-1.7B guide、KodCode/HumanEval范围内才比较accuracy/cost，未覆盖多轮tool/memory、生产SLO与失败恢复。Advisor在域内改善但HumanEval退步是直接反证，strategy可解析不等行动正确或获授权。Ch79计划为可检验假设、执行偏差需独立观测的原论点仍成立，但不假称现书已包含完整训练配方；局部结果不要求另写通用可靠计划保证。
- [2604.09744v1 — MPAC](https://arxiv.org/html/2604.09744v1)：实际读§4.2–4.3、§6.3–6.4、§7.3及§10相应限制。session固定pre-commit或post-commit，授权与执行声明分开；coordinator拥有序列化状态，离线期间禁共享mutation，恢复snapshot/log后bumpepoch，分歧走治理而非静默merge。冻结scope按实际目标而非可省intent字段校验，resolver权限随phase判断。2+2+2=6，安全边界深入，拟仅报告这个具体协议分支。单coordinator/延迟观察不是严格linearizability，split-brain未测试；66个对抗实现测试不是formal verification或完整恶意跨组织威胁模型。3-agent单次bench是existence结果，不是通用性能曲线。Ch84已有journal-before-fold、authority/epoch/commit和workflow handoff；协议的具体scope/phase机制不冒称全被覆盖，也不因通用状态原则再写一套同义规则。不采用未经独立协议核验的“A2A只能single-principal”比较。
- [2604.09747v1 — ADAM](https://arxiv.org/html/2604.09747v1)：实际读§2.2、§3的distribution/anchor/query/iteration、§4.1/4.3及§5。单次Memory read边界未涵盖多次输出被反用为下一query的累计提取；攻击从已暴露记录提取anchor、聚类/惩罚已选主题，再按熵proxy选query，可能以相同query预算覆盖更多私有记录。2+2+2=6，安全缺口深入，拟在Ch77“similarity不等可披露”之后、私有存储访问模式之前补跨轮输出反馈/累计暴露边界。主张只限公开black-box adaptive query、作者30queries/300records/top-k3、四victim及三memory agent任务，不因MIMIC例子扩AI for Science。曝光cluster不是真实隐藏population分布，entropy只是selector proxy，不证明最优信息增益；profile变稳或增量EQ变小不证明无剩余私有记录。EQ、EE、CER和ASR分母不同，不合成为生产泄漏率；关键词/rewrite等防御只有限降低，不给授权保证。EM收敛理论不用于拟采用命题，未声称已审其全部附录。原有授权读取仍为基线，新增应是跨轮攻击评价和输出可披露控制，不宣称rate-limit自动消除泄漏。拟owner与实际写入须非作者有限核验，不预支日级Gate。

第九批提案独立结果：apr02实际必要原文与owner对读，通过09741标准Only、09744安全DeepOnly及09747 Ch77窄gap。root已将ADAM两段写入Ch77相关性/可披露之后、ORAM访问模式之前；正文解释输出反馈与累计暴露，并保留内容授权、预算与单次/跨轮测量分责。apr02已实际对读真实正文及邻接，写后通过；这只验收该项整合，不预支日级完成。

### 第十批必要证据（准备好的单篇继续，未冻结分母）

- [2604.09749v1](https://arxiv.org/html/2604.09749v1)：实际读§3.1–3.5、§4.1/4.4、§5。冻结模型、decode时按object proposal置信度/稀有度修改attention行幅度并EMA平滑是具体执行分支，不误写为只换benchmark；2+1+2=5标准，仅报告。Alg中逐元素权重与softmax后causal mask应分清：未来项被遮挡不等于掩蔽后行和仍归一。proposal/track来自作者所称模型vision stack，质量与取得成本不能当免费oracle；crowded/noisy proposals会抑制正常对象或强化伪对象。有限VQA/caption/CHAIR/POPE结果不能证明幻觉根本只由attention而非perception造成，未披露端到端延迟、并发/SLO不外推；不以此重写Ch23表示质量或Ch66事实支持的通用结论。
- [2604.09759v1](https://arxiv.org/pdf/2604.09759v1)：官方v1 PDF两页正文/图1及全部§1–4已读，HTML404不等于必要正文受阻。stochastic temporal bitstream与signed unary/analog accumulate绕过传统analog幅度精度/DAC路径，是具体硬件替代分支；2+1+2=5标准，仅报告。证据是架构/device simulation与有限Transformer/BERT/ALBERT/ViT/OPT350任务，8-bit/128-bit stream及CACTI/Vivado/自定义模拟，不是实测芯片、服务吞吐或生产可靠性。准确率与能耗只留所测配置，不把模拟倍率进入Ch49通用执行选择；更强采用需真实器件/全链成本验证，不因短论文或无LLM大参数实验排除其机制。
- [2604.09781v1](https://arxiv.org/html/2604.09781v1)：实际读§3.1、§4.2–4.4、§5及必要§3.2界面。renderer RGB-D/mesh反馈、object中心但world轴方向的坐标可视化、single-axis incremental rotation与AABB尺度平移提供可检查的pose推理界面；2+1+2=5标准，仅报告。停止由自评或iteration budget决定，不是physical-safe proof；Open6DOR/Franka执行协议与SIMPLER simulated WidowX结果仍有限，不写成真实部署。作者robot baseline无task-specific FT，GraspNet/OMPL及gripper/trajectory修改同时施于本方法和SoFar；指标将抓取与最终完成分开。Table3的Stack任务45.8低于SoFar70.8，与‘各任务best’文字不能合并。540子任务消融中view/single-axis影响有限，重复VLM/render延迟不适合real-time；现有Ch26感知/高低层控制主线不由此改成通用坐标方案。
- [2604.09813v1](https://arxiv.org/html/2604.09813v1)：实际读§3.2、§4、§5.3。工具/上下文扰动后只有原oracle仍有效才保持同一tool/answer；缺失信息或错误query需改变预期行为并借助LLM judge，不能把整套环境称纯deterministic checker。2+2+2=6标准，仅报告具体oracle-preserving augmentation recipe。多轮状态依赖有限，format reward、exact normalized call/answer和judge辅助分别计；BFCL multi-turn与部分ACE任务出现退步，SFT对照受prompt兼容影响，不归因单一训练路线。已对读Ch27 executable-spec→任务/trajectory→outcome验证主线；本配方可留受限报告，不冒称现书已有全部代码、也不因oracle名称再重复通用正确性原则。

- [2604.09750v1](https://arxiv.org/html/2604.09750v1)：实际读§3.3、§4.4及Limitations。moral/reasoning conflict使所测模型更易jailbreak是具体安全边界；2+1+2=5安全深入，仅报告。embedding cosine、WANDA选择与PCA/tSNE中的空间重叠只为成功攻击子集的相关观察，没有因果恢复干预证明唯一安全机制。LlamaGuard3 judge可错判，R1只测HarmfulQ，single-turn未测multi-turn；未设计/验证defense。不把白盒表征图等同黑盒通用绕过或给未测试的防御背书，当前Ch72威胁模型仍需独立有效性验收。
- [2604.09748v1](https://arxiv.org/html/2604.09748v1)：实际读§4.1–4.2、§5.1与Table1、§6.1–6.3。verifier没有修改不代表整个轨迹受保护：构造有害前缀+正确终局答案获得正reward，拒答却不含正确终值得到负reward；用shadow模型/dualverification选择可触发记录，top200约2%毒样不是均匀全部训练样本。2+2+2=6安全缺口深入，拟Ch31 Reward Hacking中窄补**终局checked span与完整生成行为必须分别验收**，不把R1或math/code checker当安全authority。现书已讲reward proxy与tokenizer输入错配，却没有这个在checker不变时的输出覆盖漏洞。有限GRPO/verl、Qwen/Mistral/Llama任务中clean accuracy也有退步，defense平均下降不证明消除后门；不取通用ASR或生产安全概率，硬件/精度/精确长度/并发/SLO不补造。需要非作者具体gap复核后再实际落笔，不先声称Integrate。

第十批六项必要源/处置已经apr02有限非作者复核通过。09748两段已实际写入Ch31 Reward Hacking的独立评价之后、tokenizer接口风险之前；采用checked span与完整行为分责，保留所选毒样及CA/任务效用口径限制。真实写后尚待非作者，其余全日普通队列继续，不标外部受阻或日级完成。

### 第十批写后恢复与第十一批必要审阅（2026-09-27）

09748 已由 apr02 重新核官方 v1 §3.2、§4.1–4.3、Table1、§6.1–6.3及Ch31真实两段与前后衔接，写后通过；见[有限非作者写后核验](../daily-20260416/V3_RESTORE_INDEPENDENT_WRITE_AFTER.md)。本日实际整合且写后通过增加为7项，不增加整日完成数。原有“尚待”是前一阶段记录，不继续作为普通待办。

- [2604.09815v1 — EE-MCP](https://arxiv.org/html/2604.09815v1)：实际读§4.1–4.5、§5.2–5.3、§6.3/Table3与§8。专家成功轨迹蒸馏和按应用筛选的有限经验库是两个分支，后者保留成功/失败知识；每轮SFT从base重启，不是持续权重更新。拟2+1+2=5、标准仅报告：三应用小规模评测中蒸馏加经验并非各任务都胜单独经验，专家/学生接口及输入模态混杂，峰值epoch选择不是单调学习保证。Ch29已有未蒸馏基线、监督可教性与容量错配条件，Ch77已有派生经验、检索范围与参数固化的可逆性边界；不假称现书实现本具体recipe，也不以熟悉的组合宣称新的通用控制合同。未披露硬件、精度、并发与SLO不补造。
- [2604.09824v1 — ProGAL-VLA](https://arxiv.org/html/2604.09824v1)：实际读§3–4、§5.1–5.3、§10–14。symbol→短时实体记忆→目标嵌入与澄清分支可保留为受限机制，但§3/§11让fast policy同时接收目标、observation与proprioception，§13又写只接目标。Prop2只约束固定O时对g的敏感度，却以仅g变化界定O变化后的action距离；取g恒定而policy依O即可构成缺失直接路径的反例。拟2+2+2=6、中心保证深入、争议暂缓；不是否定全部LIBERO/CAB经验，也不把attention entropy当事实概率。模板抽取仍保留多数收益，实体筛选/有限属性歧义不等物理安全验证。争议保证不进Books，定点重开需明确实际policy输入及控制直接O路径的假设/证明或修订；必要可读材料已经审阅，待非作者有限复核。
- [2604.09839v1 — Steered LLM Activations are Non-Surjective](https://arxiv.org/html/2604.09839v1)：实际读§3、Theorem4.2–4.3及其证明、§5.1–5.3和§7。prompt可达activation与白盒注入后的状态集合不能默认等同，精确状态不相交也不等输出行为不相交。拟2+2+2=6、安全知识缺口深入；Ch72现有within-model causal probe/跨模型迁移限制，尚缺白盒失败不能直接证明黑盒prompt可实现性这一威胁转换边界。拟只采用这条非蕴含，不采用“所有训练模型/steering必不可达”的强保证；理论依赖解析性与分布假设，固定意义方向的条件及有限精度不由连续概率零结论自动覆盖。小模型、有限prompt/长度和两种反演方法失败不是对所有prompt的穷尽证明。需非作者核窄gap，再实际写入Ch72 sensor论证附近。

上述三项是必要审阅与采用提案，不是新的冻结分母或日级验收；日期沿用本日官方组合依据，Submitted不改写为精确公开时刻。现有候选/关闭记录保留，尚未处理的普通队列继续，不以暂缓标签逃避可执行工作。

第十一批非作者有限审阅已由 apr02 落入上述独立记录：09815 标准仅报告、09824 中心保证争议暂缓、09839 窄安全缺口均通过。09839 的两段已实际写入 Ch72 within-model causal probe 之后、MoE fault 之前，并由 apr02 对读真实正文与交接，写后通过；采用白盒/黑盒能力和精确 activation/输出行为的非蕴含，不采用普遍不可达。该项可同步实际 Integrate，本日累计8项实际整合且写后通过；仍不增加整日完成数，尚未冻结的普通队列继续。

### 第十二批必要源、有限采用与真实写入（2026-09-27）

- [2604.09852v1 Memento](https://arxiv.org/html/2604.09852v1)：root 实际读§4–5、§6.1–6.2/Table1、3，Ti存在时生成Mi并保留Mi KV，后来去掉Ti；仅以同Mi文本重新Prefill改变构造历史。2+2+2=6、知识缺口深入，Ch45派生状态段后实际补“摘要文本不是充分KV恢复材料”两段。normal/restart分别64/8次重复，50.8/66.1不作严格匹配预算的15.3pp因果收益；部分质量退步、训练与状态管理成本保留，240并发单B200不是通用SLO。保存兼容KV/构造历史，或把text-only restart当有损fallback并重验；不得宣称无损或exact resume。apr01已必要源/真实owner提案通过，实际两段已写，**写后待非作者**，暂不计本日实际通过数。
- [2604.09921v1 Two Temperatures](https://arxiv.org/html/2604.09921v1)：root 实际读§2.2、§3.1–3.2、§4.1–4.3、§6。token T控制位置内取值、position T控制位置抽取/提交并行度；TLC无放回固定K、TCT独立概率接纳，不把confidence作truth。2+2+2=6、知识缺口深入，实际补Ch24 masked-generation内两段，承接保守schedule/pass@k和影响排序，不作一般并行定理。LLaDA8B/Dream7B、block32/256长受限；NFE、wall-clock、selector成本及四A100固定72h/非固定steps分开。apr01提案通过，**实际写后待非作者**。
- [2604.09940v1 Hybrid FO/ZO](https://arxiv.org/html/2604.09940v1)：root 实际读§2.1/Alg1、§3.1–3.4/Table1–2与§3.6/Table3–4，joint base ZO/adapter FO、两学习率与条件假设是具体branch；2+1+2=5、标准仅报告。Llama2-7B/SST2 hybrid与FO prompt均46GB，不普称低于PEFT；forward/steps不是wall-clock，部分slice退步，LoRA optimizer又变化。与Ch30实际frozen-base/完整训练状态成本对读，不伪称完整算法Existing。apr01必要源/owner及此处置通过。Accepted ICLR2026提示早公开身份例外需定点归并，不扩全年venue查找，未据Submitted直接定首发。

三项有限非作者记录见[V3_APR01_BOUNDED_THREE_ADOPTION_AUDIT.md](./V3_APR01_BOUNDED_THREE_ADOPTION_AUDIT.md)。其末尾现已保存 apr01 对 Memento / Two Temperatures 的实际正文及相邻交接写后通过，覆盖上面两条写后待核的过程状态；两个 Books Review notes 已同步。本日累计10项实际整合且写后通过，仍进行中，普通后续队列及最终日期/分母归并继续，不预称整日Complete。
