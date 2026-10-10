# 2026-02-14 补遗漏：core-0 非作者独立 Source 审阅

复核者：`review_20260214`（非作者）；仅本批 Source，不授 owner PRE、实际 Books POST、来源覆盖、日期或 DAY。

已对照作者 `supplement-20261008-source-ready.md` 的“core-0：交独立 reviewer_20260214 的12项”。新增提议评分保留：11534/11737/11863/11882 为2+1+2=5，其余为2+2+2=6；评分对象均是窄命题，不借宣传或Books主题关联抬分。11534复杂度、11737干预身份、11715执行验收和11882设计反证等受影响内容已定点深入。Source pass仅对本文明确限定的拟采用命题，不授被拒绝的中心子命题。

范围：精确 `2602.*v1` 的 11534、11543、11639、11683、11698、11737、11767、11824、11852、11863、11882、11715。11495/11509 已有效审阅不重复；日期隔离材料不审 Source。保留原窗口、旧候选、评分和有效 review，不扩池。当前原证来自同目录 `supplement-20261008-core-0.json` 的具名 URL/sections/text；复核者实际逐段读取下列方法、关键实验和直接反侧，不以作者摘要替代。未运行实现、实验或生产验收。

## 11534：Krause Attention

- 实际原证：§4.1–4.3，Eq5–12/Alg1；§5.1–5.4，Tables1–6及Fig7说明。
- 支持：Q/K Euclidean distance 经 RBF、局部空间/causal window、window 内 top-k、选中集合归一化后聚合V。稀疏候选复杂度依计算仅在window执行；RBF本身并未取消归一化。LLM实验是每层新增auxiliary shortcut并保留原attention、两路LoRA，50k Flan-v2；不是全量attention替换。
- 反侧：MNIST 105.60/83.58 images/s约1.26倍而非普遍2倍，CIFAR约2.39倍，绑定单H100/具体图像序列与样本数；LARM更快但BPD较差。Table6 MMLU持平，MNLI Macro-F1 55.29→53.72退步。§4.3 multi-cluster以bounded-confidence/separation条件描述，不授任意Q/K/V、残差和训练后的完整Transformer收敛保证；本缓存未含Appendix C证明，若采用理论保证须定点补读。
- 返修要求：保留“局部交互与长程路径共存”的责任，不将sink减弱的描述性曲线当普遍表示不坍缩或全指标不损；不将aux路径局部复杂度外推到整个LLM。
- Source：通过（限定局部support设计分支及任务条件质量/成本）；作者短包已隔离通用理论、kernel/LLM加速及无损宣传。

## 11543：SPES

- 实际原证：§3.2–3.3 Eq3–6、efficiency analysis；完整§4及§5限制，Tables1–4/Fig3说明。
- 支持：每节点保留完整weights，只训练shared trunk和分配专家，其他专家冻结；shared FedAvg、专家direct assignment，global weights再广播。真正节省是grad/optimizer state及上传量，不是无需全模型权重/下载。warmup对相似input projection专家做task-arithmetic mixing并线性衰减。
- 反侧：frozen专家接收token无更新、token utilization下降；merging只是局部补救。7B是4节点各8 A800/NVLink、13Gbps到大RAM参数server；2B是16 L40S、17Gbps。65%为7B每节点上传量28.6→9.8GB，不是全双向65%。throughput 3.67k vs3.79k使用不同interconnect（Ethernet vs多100Gbps RDMA），不是同网络性能因果。Table4 avg50.5→51.3但ARC-e、PIQA、OBQA反降。证明位于未缓存Appendix A，未采用其保证。
- 返修要求：仅通信/更新责任接口；不授去中心化无server、bit-exact centralized trajectory、全数据效率或全场景性能。
- Source：通过（限定完整weights驻留、局部optimizer/grad、shared/expert聚合与上传/下载分账）；无额外证据请求。

## 11639：PACE

- 实际原证：§3 Eq1–7；§4；§5.1–5.6 Tables1–4、prefix study；Limitations。
- 支持：initial policy rejection samples选最短correct（无correct则最短）；前缀冻结，512初长于前100步线性降为0；hybrid rollout empirical pass rate驱动长度penalty，cosine coefficient在pass=0为0、pass=1为1。不能把“protected”直接理解为prefix总正确。
- 反侧：1024 prefix可提前暴露答案/shortcut，MATH500质量93.1→90.3。32 A100训练、batch64/group8，评价16 independent runs/prompt、temperature.6/context32k；token减量不是paid warmstart或wall-time净收益。Table3 MATH500 LEN1390与Table1 1490冲突，不合成单一确定数字。Qwen3-32B behavior标签不是CoT真实因果证明。
- 返修要求：明写错误前缀回退、prefix/correctness来源及采样成本，pass proxy取决于当前policy/prefix而非任务固有难度；不授logic被完整保存。
- 对照作者短包返修：§4已披露32 NVIDIA A100、batch64/group8，不能写hardware未披露。采用叙事要保持先initial-policy rejection采样构建prefix，再冻结prefix+current-policy suffix形成hybrid rollout；difficulty由其pass-rate代理，非固有任务难度。
- Source：通过（限定训练prefix curriculum、hybrid pass-rate长度系数及采样/质量预算）。作者已实际修正先采prefix后hybrid rollout顺序及32 A100配置；仅局部复核修文，不重读其他有效原证。

## 11683：ThinkRouter

- 实际原证：§3.2观察及假设；§4 Eq7/Alg1；完整§5 Tables1–3及Fig3–5说明。
- 支持：temperature-scaled、过滤前max probability决定低confidence用离散sample、高confidence用top-j soft embedding；后续filtered distribution另算。confidence是route proxy，不是truth detector。四LRM/H10080G/SGLang，10题validation选择threshold后主评价排除这10题，每题3 seeds。
- 反侧：Table2 Qwen32B HumanEval ThinkRouter69.40低于Soft69.48/Random69.91；gptoss MBPP96.09低于Random96.22。部分ThinkRouter长度高于Soft；Table1 gptoss AIME24低于Random。§5.3 error calibration是3次majority vote人口，与主Pass@1平均不可合并。局部confidence轨迹相关性不证明语义noise根因；grid search和embedding处理开销不由token数代偿。
- 返修要求：保留routing/stop/threshold责任，不授较低confidence更真实、遍及模型或无latency代价。
- 对照作者短包返修：拟采用的“pre-temperature”与Alg1 `Temperature Scaling` 冲突。应为temperature-scaled distribution取max、在Top-k/Top-p/Min-p过滤重归一化之前，不能合并为未temperature处理的confidence。
- Source：通过（限定temperature-scaled/filter前confidence routing与局部结果）；作者已实际纠正gate身份，不授truth calibration/免费wall-time。

## 11698：SpiralFormer

- 实际原证：§2 Eq7–22/Alg1、§3 Tables1–2/recurrence ratio、§4 attention probes。
- 支持：同一loop core在coarse-to-fine分辨率执行，chunk down/up后causal right-shift `s=g-1`，running token state和MeSH carrier并未被删除。compact core sequence不是完整系统state线性化。等token预训练Pythia160M–1.4B/Pile250B，主指标是4096-token prefill FLOPs和quality。
- 反侧：no-overlap `s>=g`可供pipelining但Table2质量下降；过高recurrence ratio损capacity；offset影响每token触发与不均匀compute。Table1部分小模型0-shot低于baseline。§4只选跨loop变化最大的40%head、500样本作attention统计，不授因果的global→local功能证明。推理pipelining/proof附录未缓存，未采用实测latency/proof。
- 返修要求：保留shift、upsampling、carrier、post-block和quality成本，不把prefill FLOPs称端到端加速；如采用实现因果性正式证明须补Appendix C。
- Source：通过（限定coarse-to-fine core/shift/carrier交接与prefill FLOPs，不授完整因果证明或端到端latency）；作者未采用未读附录保证。

## 11737：Saliency VCD

- 实际原证：§3.1–3.2 Eq2–7；§4 Tables1–4；Limitations。
- 支持：VCD原/辅助两distribution差分并以APC保留原分布高概率tokens；DINO CLS attention作prompt-agnostic saliency。
- 中心冲突：Eq6 `M=1{δ(S−λ)>0}`、Eq7以M位置填background，故δ=-1实际替换低于quantile的区域；正文却称δ=-1删除most salient，δ=1的描述亦反向。γ=.8的阈为20%quantile，按literal δ=-1不是删除80%高saliency。不能默改符号后称已核可执行方法。
- 返修要求：保留冲突及确切修复需求（作者勘误、该v1可核mask实现/输出或统一公式）；不将Tables1–4提升归因到确定的“删除high-saliency”操作；prompt-agnostic可mask query relevant区域、双forward+DINO成本仍在。
- Source：限定审阅通过，但中心可执行mask命题未通过。作者短包已保留符号冲突；只可仅报告保存VCD一般式、原冲突及作者局部结果，不支撑正面Books mask机制。恢复须作者勘误或该v1可核干预实现统一身份。

## 11767：TSR

- 实际原证：§2.2；§3 Eq4–10/Alg1；§4全部及Tables1–2；§5 Tables3–4。
- 支持：改rollout generation而非PPO/GRPO objective，reward/proxy-guided beam/lookahead/best-of-N后再按组reward variance筛选。相同retained rollout数量不等采集成本相同，Best-of-N生成28留16，beam扩展M/B另付费；当前search-selected distribution非未选择的原on-policy人口。
- 中心冲突：§4.2/4.3 horizon K=5并称evaluation truncate5；Table2 WebShop平均turns却5.8–7.7，严格同口径下不可能。Table4 M=2/B=2报告52.3，与主实验M=4/B=2的52.3未说明预算关系。泛称防collapse的Fig4所有方法都无大spike，不构成基线发生collapse的实证。
- 返修要求：WebShop成功/turn/latency采用暂缓，需明确turn定义和真实horizon；不同query/search/step budget须绑定，不采总体“same budget更好”或turn直接换算latency。Sokoban/FrozenLake有限Tables1可独立保留，proxy scoring细节必要时补Appendix D。
- 对照作者短包返修：主文的tree search抽象不直接证明具体snapshot/fork API已核；“可分叉environment状态”只能作为搜索需要可分叉/重放模拟状态的系统前置条件推断，非实际实现已验证。
- Source：限定审阅通过（搜索/筛选责任、系统前置条件与已隔离争议）；作者已实际将可分叉/重放模拟状态标为系统推断，而非snapshot实现核验。中心公平效率、WebShop五turn人口未通过，只保留非争议局部观察，不修复论文。

## 11824：REVIS

- 实际原证：§3 Eq1–2、§4 Eq3–7/Alg1；§5 Tables2–8及§7限制。
- 支持：参考集difference vectors、对一条operational prior方向Gram-Schmidt；校准选deepest positive mean separation层、factual percentile定阈，超过阈才加固定strength vector。数学orthogonality不证明causal disentanglement/纯视觉truth/真实风险概率。
- 反侧：Qwen CHAIR-I8.13→8.23升、Table8去gate的Qwen MMVet72.57高于72.16且CHAIR近同；动态gate必要性不遍及模型。α1.8/2.0 MMVet低于regular，浅层23损害明显。naive CHAIR=0可为empty/repetition，不是hallucination-free。mean TPT .025s未披露在本核心内的完整hardware/precision/batch/CI，不授statistical indistinguishability或E2E零开销。
- 返修要求：保持方向/阈/层/生成graph的身份，解释校准人口与不支撑的truth；不采用“semantic purification”因果宣传。
- 对照作者短包返修：Eq1–3先average构raw/prior difference vectors再projection，不能暗示逐sample project再average的另一operator。与对一方向正交性/因果purification边界一起保留。
- Source：通过（限定几何operator、校准/风险gate及quality回退）；作者已实际明确average差分vectors后project，不能授因果purification。

## 11852：ProtoT

- 实际原证：§3 Eq1–2；§4；完整§5 Tables1–5。
- 支持：softmax跨固定R prototypes写/read gates；每channel past-only discounted numerator+mass denominator recurrence，cache支持sequence-wise常数state/step成本，但依R、hidden、layers仍付费。所有run R32，values降至h/2。
- 反侧：Table1固定capacity随着context扩展受瓶颈，large PPL29.5差于LLaMA25.8/Mamba26.5；短context training吞吐低于optimized LLaMA；interpretability为top activations+GPT5.1评审/少数干预，不代替任务正确性。Table4多数PMR mean为负而非普遍prototype促robustness，semantic flip敏感不等正确新答案。
- 返修要求：将channel路由/衰减责任与task验收分开，不能将固定state或可命名prototype签作无损长程记忆/grounded reasoning。
- Source：通过（限定R32 fixed-state读写/衰减与quality取舍）；作者已隔离概念命名/PMR/任务正确性，未采用通用faithfulness。

## 11863：ICL GP

- 实际原证：§3.1–3.3；§4.1–4.3；§5限制；缓存内Supplement §8/Fig8–9。
- 支持：4bit多个LLM家族在GP-sampled noisy numeric regression、维度1–4/0–49 demonstrations做MAE；把point prediction放到GP posterior likelihood作functional proxy。SFT/GRPO lowrank更新改变这些任务上的行为。
- 直接反侧：§4.1低lengthscale少demonstrations时LLM可低于所谓GP empirical lower bound，后者不是严格任何learner的界；1NN是reference而非LLM保证上界。Supplement§8同一GP point predictor的真实kernel也无法被unadjusted likelihood恢复；variance correction令某些base结果偏好更smooth。不能签LLM真实prior=rough Matérn，或证明function写在attention矩阵里。SFT/GRPO跨smooth/rough结果只局部，不授SFT必memorize/RL必generalize。
- 返修要求：correction和kernel/noise/dimensionality条件必须与结论同行，不可只复制摘要“rough prior”；kernel/LoRA式有原文疑点，不作可执行公式owner采用。
- Source：通过（限定controlled functional预测测量及variance盲区）；作者主文已读部分足够支持其窄命题，本复核者另实际读缓存Supplement§8/Fig8–9，非把作者未读附件算作作者完成，也不扩成完整推导审阅。

## 11882：World Model mixed-bit

- 实际原证：§3全部、§4 Table1/strict-run文本、§5全部。
- 支持：DINO-WM/Wall/同checkpoint，weight-only Linear symmetric per-output-channel PTQ并dequantize执行，不含activation量化、校准/重训。primary paired seeds/episodes、M4 48GB/MPS或CPU fallback，planning预算bA=(9,2,2)、bB=(12,3,3)；不授硬件INT低bitkernel吞吐。
- 反侧：mixed4比uniform4模型138.84 vs68.12MB，total precision混杂；near-size asymmetric仅部分控制。primary delta+.2/+.3 CI含0、sign p=.109；strict22 cells/66episodes于bB反转为mixed0<uniform.167。state-distance与success相关不能证causal encoder失败；layer-retention非单调。
- 返修要求：以rollout/planning success和预算比较，明确primary/strict分开与small-sample flip；不授mixed总更好、6bit通用安全阈或尺寸→latency必降。
- Source：通过（限定模块/预算耦合、尺寸混杂及strict-run方向反转）；不授精度普适阈值或硬件低bit加速。

## 11715：DICE / BiC-RL

- 实际原证：§3 CuKe；§4.1.1–4.1.2；完整§5/Table1–6/Eq3。
- 支持：先scaffold infilling、后full generation；infilling暂时固定编译/调用wrapper约束，不保证放开wrapper后的实际调用与正确性。Exec、fast1/fast2按全部任务分母区分，250 KernelBench/分层100/100/50；robust check改变实际人口。
- 反侧：Table6 DICE未检查L3 Exec34变检查16，full generation仍有deceptive；不是彻底消除。Table4 SFT→final8B L1 fast1 16→9、L2 fast2 8→0，4B L1 Exec29→27等负增益保留；Table5 CuKe不是所有fast2领先。AR最多32k/4k、fixed-length diffusion1k vs adaptive4k、默认不同配置，不能归因扩散范式必胜。CuKe描述1425/36到6303的拼接计数需按完整data provenance核，不能从数字推全独立新样本；2倍filter本身不构成抗jitter统计证明。
- 返修要求：把compiler、execution equivalence、实际调用与speedup分账；scaffold只是阶段降低shortcut空间，不替代写后runtime check，不授数据规模定律/无reward hacking。
- Source：通过（限定scaffold→full-generation训练阶段、runtime验收与fast指标分账）；作者已保留仍有deceptive与负增益，不授完全消除reward hacking。

## 本批结果

12项必要Source限定审阅已结清：10项窄正面命题通过，11737/11767其余局部观察与争议隔离通过，中心mask身份/公平效率与WebShop五turn人口不通过且隔离。作者四处事实/身份文字返修已实际定点复核，不请求新全文、不改评分、不扩大原证队列。后续Books仍须实际owner比较、PRE与非写入者POST，不能从本文件授Books整合或DAY。

## 继续授权的下一小批（2026-10-08，同日增量，非core0重审）

root授权core1六/once五及已具名core2五必要独核。恢复实际重读AGENTS、Research/Report合同、Prompt、Daily来源说明、ROADMAP与当前checkpoint；只用本日采用包和精确v1缓存，不新建长期账本，不改Books/Report/LS、不stage/commit/push、不授DAY。core1当前采用包尚未持久，已请求作者单篇准备即送；先处理已具名Zoom，不凭缓存标题创命题。

### 11858 Zooming without Zooming：Source限定通过

- 实际原证：`supplement-20261008-core-2.json`精确URL `https://arxiv.org/html/2602.11858v1`，完整§3.1/Alg1/§3.2、§4.1–4.4/Tables2–6/Fig5文本、§5.1–5.2/Tables7–8/Eq2及§6.1–6.5/Table9脚注。缓存正文实际读取，不计下载为审阅；未读Appendix8–12、未核artifact或复现。
- 支持：crop/resize对象micro-region、teacher QA/majority共识与difficulty筛选、box-overlay+spatial约束重新锚回global image、74K/DAPO/Qwen3VL4B/8B与Qwen2.5VL7B无SFT；Table6同10K的bbox-in-image对direct/no-bbox/bbox-in-question支持这一受限训练接口。Table9脚注明确global downsample抹去细节时，crop提高有效分辨率相对实际输入**增加信息**；因此不能将所有crop叫information-neutral。single-pass是无test-time工具交互的global-image路径，§6.1仍明确textual CoT，绝非整AR生成一次物理forward。
- 直接反侧/矛盾：Table6 Color83.19低于Direct83.45，§4“across all”不可采用；Table3 CountQA 74K32.40低于10K33.97，数据量非每项收益。§4把8B baseline写61.52，与Table2的62.86冲突，61.52属4B，只采用表；Table5 DiG8B MMStar72.7高于ZwZ7B63.4且规模/数据不同。Table7 ZwZ仍有15.26 global/regional gap，crop后counting54.90仍不可靠，regional只是经验参照，不是形式上界或所有crop因果证书。Eq2 attention mass coverage变化不是必要路径/faithfulness证明。
- 费用/采用边界：teacher GLM4.5V/Qwen3VL235B、crop生成/过滤与训练前置费不免费；Fig5速度来自ZoomBench平均样本时间倒数，质量来自另一Table4平均，main硬件/precision/batch/CI/SLO Not Disclosed，不授生产10×、完整降本或无SFT保证OOD。§6 spatial/multi-object未广泛训练/评价、其他工具与Agent蒸馏只是讨论，不采用其全域推广。
- 裁决：作者窄命题/2+2+2=6支持，训练privileged region到实际global可见输入的受限接口Source通过；反侧与缺像素不可补回边界已具名保留。无需新原证；请作者准备实际唯一owner差额及拟文/已有覆盖，Source不是Books准入或写权。core1/once其余普通待办，不因本项称整批完成。

### 11934 Robot-DIFT：必要原证支持，比较身份窄修后确认Source

- 实际原证：同`core-2.json`精确`https://arxiv.org/html/2602.11934v1`完整III-A/B/C、Eq1–9；IV-A/B/C/D、TablesI–IV及V。未读Appendix、未核artifact/复现。
- 支持：SD2.1冻结noisy teacher、weight-copy clean-latent student，τ uniform0–999、全decoder-block timestep-conditioned projection、归一化cosine、λ0.1→0.001半训练期退火；部署移除teacher/heads，S2-FPN us3/us6/us8粗到细及CLIP text query/visual KV/2D RoPE、view max聚合都实际原文支持。确定性仅视觉backbone，下游Diffusion Policy不因而全policy无采样。
- 必要身份返修：IV-A明确DIFT(SD2.1)对照**也经过manifold distillation成为deterministic Student**，Robot-DIFT在DROID继续robot-adapted训练。因此不得把所有DIFT称部署仍随机、把clean/noisy蒸馏首次发明或全部对照加速归本篇；通用接口可以解释，但新增差额须结合robot-adapted/multiscale具体选择。已请作者补采用包；不是要求新全文。
- 关键对照/负侧：RoboCasa24tasks/50demos/200epochs/50rollouts、encoder-swap同冻结encoder+policy，仍含DROID额外制备预算；DINOv3正文0.27与TableI0.33冲突，只采用表。OpenDrawer.60<.70、TurnOnStove.44<.58、CounterToSink.06<.08。TableIII冻结backbone/同policy仅Pressing/Insertion子集支持multiscale/anneal；无全部几何因果认证。LIBERO10各50seeds、16预测/8执行；OpenVLA8次单action匹配horizon不等同模型或全训练预算，.01s与.23s无完整硬件/precision/batch/控制SLO，不授生产23×。
- 真实机器人范围：Franka7DoF/双ZED/4tasks×20trials、31–36demos/10Kpolicy steps/16预测执行8；DINOv2 Sort.55>.50、Open.60>.55、Robot Insert.35并不可靠或安全。teacher/noise/all-block投影制备、FPN/cross-attention/policy成本不能因部署heads移除消失；nonrigid/longhorizon/video-teacher未核。
- 裁决：支持作者2+2+2=6及局部语义/接触表示接口；Source采用包需上述比较身份一句窄修后确认，其余限定正确。不授新全部蒸馏范式、通用几何真值/安全/完整实时控制。owner/PRE待实际差额，当前未授Books。

### 12205 DeepGen：Source限定通过（SCB接口/局部能力取舍，非精确RL配方）

- 实际原证：同`core-2.json`精确`https://arxiv.org/html/2602.12205v1`，完整§2/3/4/5/6，Eq1–5、Tables1–7/Fig5–6文本。原表分散于架构/训练/数据段已随段实际读，不只读§5摘要。未读Appendix7/8、未核artifact/复现。
- 支持：Qwen2.5VL3B+SD3.5Medium2B，128think位置与六个均匀low/mid/high VLM隐藏层是不同轴；channel concat→two-layer MLP→Transformer encoder connector Eq1。200K alignment冻结主模型、400K联合SFT中VLM LoRA、1500-step RL主要评价；三个reward各自组内标准化后加权/batch标准化，auxiliary SFT分支与KL代价都存在。通用GRPO不是本篇新发明，且数据10M in-house/1.1M编辑、teacher合成/标注及生成evaluation均有前置费。
- 直接反侧：Table6无SCB GenEval.86=full，无Think GenEval.87>full.86，只部分指标支持组件；不能授隐式CoT causalfaithfulness。Table2 spatial SFT.82→RL.70；Table4 RISE四维/overall13.3→10.8、UniREdit77.5→75.7均退，SFT anchor不保证全部能力保持。Table7都是1000steps，与主表1500不能拼成同checkpoint；Fig6无SFT约300steps与§3约1000退化说法不合成确定阈值。Table5 wordaccuracy.7533<GLM.9116/LongCat.8658/Qwen.8288，CLIPScore非OCR正确证书。
- 精确公式隔离：§3 stage2“unfreeze entire”与VLM LoRA并存，只采用实际LoRA限定；Eq4把velocity平方差叫KL，缺时步/协方差等分布条件不能授严格KL；Eq3为reward最大化表达而Eq5并合standard flowmatching loss，符号/实际优化身份未澄清，不采用为可执行objective或训练正确性证明。本采用包只解释SCB和观测trade-off，因此不需要为隔离公式遍历训练附件。若拟文以后采用具体objective，必须定点重开Appendix8/优化实现。
- 裁决：作者2+2+2=6与SCB受限接口Source通过，原采用包已明确上述中心式/词语矛盾隔离，无必要返修。硬件/precision/batch/CI/完整SLO main Not Disclosed，5B与排行榜不授consumer硬件或全链效率。请作者按真实唯一owner现文差额准备SCB拟文/已有覆盖，不借MR-GRPO新名称复制成熟知识；当前不授Books/DAY。

### 11934身份窄修复核

已实际重读source-ready的Robot评价段，作者加入IV-A DIFT对照亦为manifold-distilled deterministic Student，Robot新增DROID adaptation/具体multiscale且不授clean/noisy首次提出。**修后Source限定通过**；原文已足，无需重读整附件。后续owner/PRE只核此窄差额。

### 11965 MaT-LoRA：Source限定通过（共同support参数化，非无条件外推理论）

- 实际原证：`supplement-20261008-core-1.json`精确`https://arxiv.org/html/2602.11965v1`，完整§3/4/5/6/7，重点Eq4–10/13、Assumptions1–3/Theorem2及Fig2/Table1–2；未读AppendixA/B，不授完整理论证明、artifact或复现。
- 支持：固定B/A、时间core F(t)及matrix exponential/RNN/MLP三类归纳偏置，future-domain weight proposal须绑定共享support/时间/core形式。Eq4–7只在共同row/column support成立时表达独立adapter；各时rank≤r不推出union维度≤r。主文r′≤r与跨时union可能更大不能用于无条件exact/constant-rank等表达性。§4.1平移lemma仅保存已假设的weight manifold，不证明数据→最优weight diffeomorphism；作者包已隔离§4.3的越界推导与§5.2 stability保证，本篇采用接口不依赖未核Appendix证明。
- 对照/反侧：Rotating2Moons12×200/18°/noise.10/先9训练，2D坐标直投latent且省标准token/position，不认证语言未来reasoning。AIC/NewsCLS/Yelp unseen-domain分类3runs mean±std仅作者人口；core变体/rank/horizon须一起验收，标准差不授显著或普适future预测。Table2 AIC训练740±18s>Offline532±153/Inc402±77/Last241±31，test2.99>2.11/2.46/2.73，与marginal/on-par叙述不能合成全成本证书。
- 费用/边界：Eq13只固定parameter storage与core-network规模不随T，不保证完整activation/history/optimizer运行内存常数、训练/部署更快；main硬件/precision/batch/SLO Not Disclosed。support失配或非平滑shift须重新验收，可回退独立adapter/末域或增量微调，不把时间标签认证未来分布。
- 裁决：作者2+2+2=6窄Source通过，已主动保留理论条件与直接反侧；不要求为不采用的定理遍历附录。owner路由需纠正：实际ROADMAP是`TRAIN-LORA`/Ch30/`30-lora.md`，不是采用包所写`TRAIN-SFT-LORA`/Ch29；这不影响Source结论，但PRE必须比较真实owner，不授目前错误节点或写权。已通知作者准备具名拟文/现覆盖。

### 12005 LaCy：Source限定通过（GT/CALL委派target，不是事实真值或删除）

- 实际原证：`core-1.json`精确`https://arxiv.org/html/2602.12005v1`完整§3、§4及§5.1–5.7/§6、modified NLL、Fig2–7/正文对Fig10的直接说明、Tables1–2；未读无关Appendix A/C、未核代码/复现。
- 支持：§3单batch112documents/~44Ktokens、1.3B/50B训练的Gemini2Flash acceptability诊断同时依赖原GT意义/格式和spaCy English/custom heuristic，不是任意真值同义。§4 fact proxy×当前高loss选目标位置换CALL，未选位置在排除CALL重归一化分布上学原GT；25%facts中高loss60%=总体15%CALL是训练预算。§5部署greedy、Llama3.2-1B、CALL running quantile22%是另一人口预算；tokenizer不同可由一次返回变成多个SLM token，尤其3–4位数，不能当统一一次一个token。target修改不是删除context或经典confidence-only路由改名。
- 对照/直接反侧：334M GPT2从零/32K SentencePiece+CALL、dwiki3B/约50B16epochs/ctx1024/fullprecision/340–440Ksteps匹配原GT-gradient token数而非总forward费用。Wiki biography FactScore+6.88%仅该人口，cascade自身34.2%仍返回错误事实；无CALL的gold-containment下降是行为probe，不证权重完全无事实/知识删除。§5.4直接说明Ignorefacts/Ignore等forwardsteps时FactScore提升消失，不需为已不采用的额外收益重读Appendix Fig10。NLU均值39.9>39.6而Hella28.5<28.8，不能授全部NLU无损。
- 费用/限定：Table2 spaCy152h/Btokens/CPU core，不能与233h/A100/56h/A100硬算等价费或免费label；cascade生成/拼接/核验、reference额外制备训练均付费。§5.7目标/评估mask人口不同导致本设置loss与FactScore不单调，不推一般pretraining loss无用。§6 pilot/sometimes漏CALL、调用后如何检索未完整解决；main完整训练hw/batch、CI及服务SLO缺失，不能补造净吞吐或可靠工具行为。
- 裁决：作者2+2+2=6及训练target/委派接口窄Source通过，现采用包含具体反侧与费用，无必要返修。owner/PRE待作者真实Ch28/27比较及拟文/具体覆盖，不按CALL名转完整Agent执行owner，不授Books写权或DAY。

### 12078混合递归算子：Source限定通过（通信/数值接口，非普遍稳定与覆盖等价）

- 实际原证：`core-1.json`精确`https://arxiv.org/html/2602.12078v1`完整§3/4/5/7，Eq4–5、Fig1–3文本、Tables1–3；未读无关§6引用/额外附件，未核artifact/复现。
- 支持：保留TRM双zH/zL、Hcycles3/Lcycles4–6、Qhalt schedule，单update用Mamba2→Mamba2→Attention→MLP或MLP-t双向跨位置通信；pure causal Mamba不直接代替grid全局可见依赖。6.83M/6.86M、hidden512/dstate128/headdim64/expand2主要attention对比参数接近，非匹配全部FLOPs；MLP-t两支参数因grid另变。post-residual RMSNorm是所有实验实际配置，没有主文placement-controlled ablation，不能授实测所有pre-norm必NaN、任意递归/Jacobian收敛或“数值幅度稳定=任务解收敛”。
- 直接反侧：ARCpass1 40.50<40.75/pass2 45.88>43.88，Sudoku66.5<72.2及hybridMLP84.2<87.4；Maze80.6>60.8但checkpoint6–85%波动，MLP两支0%，不授通用稳定递归改良。ARC原MLPt29.6来自旧论文未本篇重现，资源/参数变化非受控同实验。
- 覆盖/选择身份：400puzzles/419inputs（19双输入）、dihedral/color368150/~880每input，逆变换再vote；K1000是增强池correct-anywhere非1000独立同分布解码。hybrid unique339.5>266.6/entropy5.39>4.56但top1share32.9<41.1/margin24<32.3；correct候选出现不是实际selector选中证书。hard/easy阈值15%取两模型平均correctvote，尽管作者称model-agnostic，仍依两模型定义，不是独立固有难度；246/173分层及31/23互补只原人口。
- 裁决：作者2+2+2=6、受限grid混合通信/递归验收Source通过；现包已保留任务反退、波动、vote人口与postnorm不等收敛，无必要返修。注意未来owner拟文只描述norm实际位置与应验数值，不报告本文已比较placement。§7 compute-normalized仍future work，硬件/precision/batch/训练CI/服务SLO main缺失；不能扩到AR语言泛化或内层SSM替代外loop。具名Ch17 actual差额PRE待作者，不授写权/DAY。

### 12204 CRAM/SRCD：Source限定通过（已观测retrieval的参数近似，在线免费gate隔离）

- 实际原证：`core-1.json`精确`https://arxiv.org/html/2602.12204v1`完整§2/4/6/7/8/9，Eq1–8/13–14、Tables1–2及主文§7.6直接负侧；未采用§5强最优性/necessity理论，未读其完整证明与无关附录，不授artifact/复现。
- 支持：time-gap gate的CT离散ODE-style update、有界episodic KV、rank=d/16语义MLP、三路Gumbelrouter；consolidation只取曾用episodic读取的token，以stopgradient rE训练局部参数近似。是否检索与已读结果能否由近似计算替代是不同职责。Eq6 q=exp(−||fsem−rE||²/σ²)与Eq7 router输入**仍要当前rE**；主文没有如何所有线上skip-retrieval请求无读取获得q的实现，不授免费可靠gate或本文已经解决这个循环依赖。拟采用只为已观测teacher/readout的训练接口/需验误差，不为在线无读执行保证。
- 关键对照/直接反侧：GPT2 124M/355M/OpenWebText10M linear-probe .84/.92可预测度不是因果可删除88%attention。SRCD N2048/5%queries/70%100固定patterns/Pareto gaps，.05×.30=1.5%只此生成合同的理论参照；Table1 retrieval100%不等全task无损，DynMSE1.211>Transformer.589及w/o consolidation1.198。Table2只冻结semantic/router而taskhead重新训，非完全zero-training；Activity.181<SeqBoat.386直接负侧保留。
- 成本/边界：37.8×只attention reduction/训练过程中变化，不是wallclock、全部FLOPs、环境收益或低端部署证书。q scoring/consolidation、semanticadapter/CT/router/早期coldstart与buffer范围均计费；至少50%recurrence/约3Ksteps为作者设置经验条件，novel/关系改变不授可靠自动fallback，须验真实episodic读取/原attention/静态router。§7.4γ=.43±.04与人类曲线重叠不证明共同生物因果/演化最优，主文完整hw/precision/batch/全算费/SLO缺失。
- 裁决：作者2+2+2=6受限训练近似/路由分责Source通过，中心在线q执行身份争议**隔离，不通过**免费gate/完整效率；采用包已明确该限制且不虚构解决实现，无需追加原证。owner/PRE需实际Ch14/17差额，不能借memory名称写Agent memory或用probe授普遍exact替代。不授Books写权/DAY。

### 12155 FAIL：Source限定通过（近似flow反馈路径，非exact/unbiased配方）

root追加授权本日已ready候选必要独核后处理，非跨日扩池。实际原证：`core-2.json`精确`https://arxiv.org/html/2602.12155v1`完整§2/Alg1–2/Eq1–4、§3.1–3.6/Tables1–5/Fig2文本、§4/Tables6–8及§6/7；未读无关附录、未核代码/复现。

- 支持：current-policy/expert discriminator在线更新，PD用可微反馈但实际是local-linear single-step denoising近似，PG只消费scalar discriminator并用exp(CFMold−CFMcurrent) surrogate。discriminator仍learned reward proxy，去explicit reward model不是无评价模型；group advantage不是新GRPO。Eq2分母1−(t+Δt)附近与实际t范围未给完整recipe，不采用全时域公式；§2.1 exact/unbiased DDPG等价不能继承到实际近似。Eq3/4非已核真实density ratio/exact distribution KL，不授通用flow无偏或收敛。
- 评价/费用：13K过滤GeminiPro3每prompt1expert、FLUX1dev/Qwen3VL2B、3policy+1expert hybrid、BCcoldstart/25warmup、batch128/32H20、512²/400iterations1epoch，专家/过滤/rollout/可训练discriminator/gradient与支持干预都付费。§3 CFGoff与§4同checkpoint optimalCFG是不同evaluation配置，不能混表；main完整precision/全wallclock/CI/SLO未披露。
- 直接反侧：Table1同400steps PD UniGen62.17<DPO62.83/DPG84.14<84.25/UR3.3938<3.4183，800PD接近400PG多训练费；Fig2 PG450后collapse、PD2000的proxy曲线不证明普遍manifold-preservation cause。Table3 PD+reward UniGen60.88<62.17、PG+FPO HPS11.75<FPO12.56，非彻底解决hacking或全部维度更好。Table6 PD87.32<Seedream88.27，不照录parity；Table7 baseline表61.30/文61.61冲突，只表值，Text52.87<Qwen76.14；Table8 Arts10.16<10.32/Science9.59<11.24，HPS/UR非真实全部human偏好。
- 模态/停止边界：Xomni/Wan另expert、另模型仅各自局部扩模态，不能授所有连续/离散flow适用或all SFT distribution shift解除。§6仍hyperparam/model sensitive、13K scaling开放、basepretrain缺能力不可凭alignment补齐；expert bias、approx失配、collapse/质量回退时原SFT/受控reward共存。
- 裁决：作者2+2+2=6与条件feedback可微性/flow更新路径的受限接口Source通过，包已明确近似与主要负侧，无需为不采用等价扩附件。owner/PRE待真实Ch24/33现文比较，不能以新命名自动写，未授Books/DAY。

### 12063 VLAW：root证据作者包的非作者必要Source

**Source限定通过，评分2+2+2=6保持。** 本reviewer实际读`core-2.json`精确`https://arxiv.org/html/2602.12063v1`§3、完整§4.1–4.3/Alg1/Eq1–7、完整§5.1–5.3/Table1/Fig5–9文字与drawing ablation、§6；root包仅定义拟采用范围，不代替本次原证。未读无关理论附录、未核Figure7图内百分数或artifact/复现。

§4.1真实rollout成功与失败共同进入WM diffusion目标并混合DROID；§4.2/Eq4/Alg1真实成功与RM筛过的imagined成功才有policy flow-matching权重，失败权重0。失败transition需要留给dynamics不等于BC模仿失败动作，生成成功标签不升级真实outcome。RM Qwen3VL4B以真实binary outcome微调与yes-token阈值筛选，正文明确first iteration（§5.1亦同），不能借算法省略认定每轮都再训练；WM/RM可共同误判。§4.3正则RL/closed-form/flow-matching surrogate divergence未采用exact KL、全局最优或无限迭代单调。

Table1 256段各5秒replay/wrist-view图像评价不等闭环动作，50段interaction clip为30success/20failure；expert→加online后FP11→1、TN9→19但FN2→4、TP28→26，所以不是全部误差下降或物理认证。Figure9删real-success与synthetic500→250只drawing局部，对其他任务不授唯一因果。五类任务、π0.5/CtrlWorld、每类25expertwarmstart/每轮50real/500synthetic、WM50Ksteps/policy2Kbatch256/2iterations；FilteredBC/DSRL只匹配real rollout数，不是合成、reward筛选、训练、reset全费用匹配。主文缺完整precision/hardware/control-rate/horizon/生成时延/人工reset/端到端SLO；不照抄摘要数字或由视觉连贯授安全。

actual owner comparison已开始但未发具体措辞PRE：Ch25完整`330–406`含Imagined rollout、RaWMPC失败人口、real replay/optimism目标偏置与WIMLE synthetic TD权重，以及Reflection完整`1230–1264`“失败动作也是状态转移证据”；Ch24开篇`1–46`及handoff`1798–1814`，Ch26开篇`1–42`及handoff`1309–1327`。已有失败进入dynamics与预测不能commit原则，但没有本分支WM/BC/RM三种目标训练人口和相互误判的连续分责；RaWMPC后可承载最小一段且不侵占26controller。root采用包目前只有差额描述，没有逐字拟文，已请求具体一段后再裁决措辞；不能把本Source/位置判断当写权或DAY。

### 12262 T3D：必要Source限定通过（teacher条件轨迹，不签student占用分布）

实际原证：`core-1.json`精确`https://arxiv.org/html/2602.12262v1`完整§2/3/Eq1–10、§4.1–4.2/Assumption4.2/Eq11–20、§4.3–4.4的定义/命题/上界Eq21–24与Table1、完整§5/Table2–3、§7；必要缓存`t3d-ablation.json`完整D/Table4–7及`t3d-reference.json`完整C.2。不读未采用证明/全部附件，也不核代码或复现。

支持teacher同一次decoding order的clean/intermediate pairs替代仅clean后独立mask的状态身份，implicit discriminator以teacher/reference conditional likelihood比较、early decoded token按π加权path CE。§5.1静态low-confidence remask/block4/steps4逐token保存最终order后恢复mask，student初始化teacher、mix随机inputtokens；AppendixD称“random initialization”但主文只randomtokens，不能推整个weights随机初始化。C.2 reference每10globalsteps刷新前轮student、轮内固定，与teacher身份不同；best-performing选择标准未完整给，不授validation无泄漏。Eq7 conditional expectation在sigmoid内部，Eq23只是上界，不把普通sample loss/DDO写成exact reverseKL。

Assumption4.2 teacher/student intermediate marginal相同是条件，不由初始化+teacher数据保证更新后仍相同；不授所有student真实on-policy覆盖、deployment联合KL最优、条件TC普遍单调或新GRPO。早token监督不等真实因果credit，§4推导保证未采用，必要定义和边界足即停。Teacher生成亦可能错，MATHtrain/PrimeIntellect teacher数据与SFT BespokeStratos不是same-data对照；所有fullparam/8A10040GB、生成轨迹/reference更新/likelihood/训练另付。

Table1 1.7B TokPS4 T3D average22.27<dParallel22.60，TokPS2多code切片仍低于original；Table2恢复fullstep的1.7B四项均退（56.8/78.01/41.2/57.32<59.4/80.59/45.2/59.76），4B GSM/MBPP退，不采用“without sacrificing full diffusion”。D/Table5 DDO-alone12 collapse、69>68只MATH切片，Table6完整58.6<DDO+path60.6；main full70与ablation69不可合并。Table3 dynamic阈值.9/temp.1：HumanEval29.27<33.54即使latency降；GSMsteps83.03>71.12而TPS升、length312.48>249.52，MATH也改变length，非所有更少step/端到端same-quality加速。主文完整precision/batch/CI/SLO未披露，full decoding、clean distillation/可信SFT回退保留。

裁决：作者2+2+2=6与受限teacher trajectory训练/预算验收接口Source通过，命题/直接反侧足够，不扩附件。owner候选24/29仍须具名实际正文差额与拟文择一，不自动写Books/授DAY。

### 12160 DreamID-Omni：必要Source限定通过（reference/内容/结构绑定接口）

实际独立原证：`core-2.json`精确`https://arxiv.org/html/2602.12160v1`完整§3/Eq1–5/Tables1–4、完整§4/Tables5–6、§5；非作者包替代原证。采用同identity的视觉/音频reference序列concat、同RoPE预留segment、跨video/audio/jointcaption的sub_k anchors；source-video/driving-audio以elementwise add与reference concat分责，target audio RoPE频率Lv/La缩放。其是learned binding条件接口，不是RoPE周期性就证明不同身份正交/attention总低/串扰为0；真实reference身份/声纹匹配、数据权利与授权不由模型生成保证。

Inpair同sample参考与loss排reference区不等信息隔离或绝不copy；crosspair另clip/完整loss也未自证无需身份匹配。Ovi初始化、lr1e−5/b32/M150、10K→20K→20K与全task4:3:3；multi-condition CFG分别给两stream需要额外条件forward/采样与清洗/caption/train费用，统一weights≠singleforward/省全费。主文完整硬件/precision/生成steps/耗时/CI/SLO缺失，不扩user-study/全部data附件。

评价200=100R2AV+50RV2AV+50RA2V，ArcFace/WavLM/ViCLIP/CLAP/Whisper/SyncNet与Gemini2.5Pro SpkConf均各自proxy；.08不是所有真实说话人归属错率或faithfulness。Table2 AES.618<Wan.632/PQ6.290<6.391，Table4 SyncD8.659>Humo8.323，均值优不授全质量支配。Table5 w/oSC .26与full .08/w/oSynRoPE .12支持当前多人切片组件差额，不授数学identity分离。Table6 OnlyIR IDsim.692/timbre.504高于full.674/.493却copy/text差，OnlyCD CLAP.287>full.282；无全指标/全任务课程最优。正文RV2AV Table4误指实际Table3、dual-level Table6误指Table5，按caption分人口，不合并错表。

裁决：作者2+2+2=6窄reference绑定/condition接口Source通过，直接反侧与费用已准确隔离，必要采用证据足即停。owner23/24尚需真实唯一owner比较/具名拟文，不借Syn-RoPE名称复制理论或自动授Books/DAY；支持域失配/复制/费用退化时保留原reference/data核验与分task生成路径。

### 11340 BLPO：必要Source限定通过（caption优化中间证据，judge仍原图）

实际原证：`agent-core-0.json`精确`https://arxiv.org/html/2602.11340v1`完整§3/Eq1–11/Alg1、完整§4/Tables1–2/§4.3直接反侧、§5；另直接打开[官方exact-v1 Appendix A](https://arxiv.org/html/2602.11340v1#A1)实际必要292–297数据人口/label schema。不采全部优化prompt附件、未核代码/复现，页面生成日期不用于移动既定Daily候选。

§3最终judge `f(x,p)`始终原图，caption `g(x,q)`只供p-update；inner在当前minibatch原图/label上比较p与caption诱导p′的loss差选q，outer才更新judge prompt。它优化当前p-update utility而非caption忠实度/可逆pixels，文字参数的gradient是conceptual approx，实际GPT-o3改离散prompt、judge weights frozen；无真实可微bi-level最优。q history分数与原训练池不是独立test，生成caption不升级human label/安全authority。

必要A train/eval与test各100 AGIN/200 SeeTRUE/140 ImageReward/110 UnsafeBench的小平衡人口，不是自然先验。AGIN采1–5却default7点，ImageReward main1–5/A1–7冲突保留，不自行统一label；采样描述不能自证全test无泄漏。T1 Qwen AGIN Acc.14<TextGrad.22而F1同.17；Scout ImageReward Acc.36<APO.37、SeeTRUEF1.77同TextGrad；Maverick AGINAcc.38同TextGrad，不采用全基线全指标支配。T2在Scout局部改善fixedcaption/judgeprompt-caption，不能授内部因果faithfulness或全规模安全。Scout Unsafe T1 .83/.84与T2 .81/.82未同run，不拼单点。

三judge Qwen2.5VL32B/Scout17B16E/Maverick17B128E、GPT-o3 optimizer/temp0/max5outerround/max10errors；§4.3更大batch先升后降≈15，非越大越好。caption重生成/候选judge复评分/搜索与API版本皆费用，主文完整hw/precision/batch/总API费/±含义/CI定义不够，不以少图context授全链降本。caption漏细节/label变化/版本或预算失配时保留原图、小errorbatch/固定prompt、人类/独立annotation；非自证循环。

裁决：作者2+2+2=6与当前caption→p-update的受限中间接口Source通过，必要反侧/人口/费用准确且足，STOP不扩全部prompts。唯一owner75/66须实际比较和具名采用边界择一，不凭MLLMJudge名称准入安全或写Books，不授DAY。

### 11409 TRACER：必要Source限定通过（异常proxy与tail测量，非概率安全）

实际独立读`agent-core-0.json`精确`https://arxiv.org/html/2602.11409v1`完整III/Eq1–24/TablesI–II、完整IV/TableIII–IV/early-warning与V。Agent/User step身份、概率/stopword/数字content filter、semantic×lexical local-window repetition、tool-action/outcome和agent/user embedding gap、MAX步score及top-k tail mean+worst-step的接口支持当前稀疏异常测量，不把评分名当真实failure probability或action authority。

III-B选择I依随机token/概率，unbiased conditional entropy断言不采用；numeric entity/金额可能有用但被滤掉只是工程风险推断而非本篇实测。III-C embedding distance不是任务进度/可行性，必要重复可能被误分；III-D α/β/γ、k/w、embedding/tokenizer/actor都需身份和校准，MAX没有免heterogeneous量纲校准。III-E无logprob时rU=0改变特征合同，不继承不经验证的同保证；failure bound先假定真实hazard被min(1,cr)支配、残差η/tail K/w<1，ranking证据不验证该真实支配。subadditivity只是函数不等式，不授actor因果归责/无doublecount风险证明。不读不采用的AppendixA全部证明。

τ²三模拟域airline50/retail115/telecom114任务、最终assertion failure；gemini2.5pro/flash/gpt4.1mini、LiteLLM tools/temp0/logprob，非真人开放工具或真实环境安全。TII combined九格AUROC/AUARC优仅该人口；TIII单方flashAirline A.650<SemEnt.721、proTelecom A.647<SAUP.671、proRetail U.489<SemEnt.576，非单方均优。TIV held-out validation调参/test排名支持本人口MAX，而不唯一因果解释真实sparsehazard；split计数/重复CI未完整披露。

Early-warning只在最终失败轨迹记录首次过阈值，再除事后总长度；“based on AUROC”operating threshold未完整给，不授在线FPR/真实时间或20%必可恢复。AUARC是离线逐步reject不确定episodes的accuracy，不是干预后救回/实际安全增益。logprob/embedding/caching/window比较/tail排序费用与第三方API费另计，main完整hw/precision/batch/wallcost/SLO未给；漂移/feature不可得或阈值失效时分量诊断、typed外部outcome gate、原hard stop/unknown协调保留。

裁决：作者2+2+2=6与稀疏异常/双actor测量结构Source通过，强理论/部署恢复保证已隔离，必要机制/关键对照/直接反侧足即STOP。Ch66测量或Ch80合作尚需actual唯一owner比较/具体拟文，未授Books或DAY。

### 12271 MonarchRT：必要Source限定通过（稀疏因子dense近似，不是删边无损）

实际独读`core-1.json`精确`https://arxiv.org/html/2602.12271v1`完整§2/3/4/5/7，含§3.2 Eq1/Case1–3、§4.1/4.2表示假设与tile冲突、§4.3 HBM接口及Tables1–8。不扩全部证明/附件或代码，沿用本日准入/score，仅核作者具名dense近似与布局/训练人口采用接口。

§2既有MonarchAttention通过交替优化block-diagonal因子近似dense softmax、无需物化完整A；不能把稀疏factor当attention edges本身稀疏，亦不说此文首次发明。§3 top-p只是5个随机head/layer/firstdenoisestep所测，不能外推所有视频attention不稀疏。Eq1 separable positional D+sparse semantic S+noise是建模假设，Case1–3未穷尽mixed semantic blocks；global fullrank可与blockrank1共存，不授所有真实attention exact表达。§4.1 exact只S=0且完整f/h/w分别归一个block轴，flatten索引邻近非物理邻近；§4.2固定baseblock的分tile/parameter tying包含原族不等finite优化/固定训练质量单调。正文c1²c2²与Example c1c2冲突隔离，不转完整kernel recipe/strict证明。

§4.3降低refinement iterations需finetuning/custom forward/backward，α/c依query/KVframe入HBM、frame维度仍二次；query mini-sequence只cap峰值不是移除所有quadratic work/KV。§5.1 Setup写training-free却T1/T2明确DMD注入训练Self-Forcing/4stepWan、50step diffusion loss finetune，不签free质量；T1只有一行无独立14B表，不采全scale证书。T2 4step quality.842<dense.846/semantic.788<.800/total.832<.837，50step quality.841<.846/total.835<.839，非allfidelity无损。§5.2 T3/T4训练free是另一人口90%（非trained95%）；SVG/Radial 85%overestimate并保dense首step/block，oracletopk本身费用不可免。

T5 B200480p .95 Monarch5.97ms>FA4.53/VSA4.02，T6 .95 .95ms>FA.79；不采全GPU/density最快。T7 RTX480p81frames 4stepWan7164.56→4866.97ms与T8 SelfForcing8309.06→6094.45ms只是各自人口E2E，kernel峰值11.8×不是E2E或质量等价倍率。SelfForcing720p RTX因KV OOM没E2E，720p kernel不能补部署；16FPS另torch.compile、480p、所测SelfForcing非任意首帧/interactive/长会话SLO。训练/refinement/布局/tiling/compile/KV均付费，必要主文完整trainingdata/hw/precision/batch/重复CI未披露则Not Disclosed。

裁决：作者2+2+2=6限定dense结构近似/布局与finetune发布验收接口Source通过，中心exact/单调/完整tile实现争议隔离，必要机制与反侧足即STOP。不授无损、零训练或生产视频能力；失配/质量退步/费用不合算时dense/已验稀疏分支或更保守refinement共存。owner须actual Ch14与Ch24比较后唯一择一，现未授PRE/Books写权/DAY。

### 11513 DEL：必要Source限定通过（有界随机低比特发布与噪声适配，非同ASR即同隐私）

实际独读`agent-core-0.json`精确`https://arxiv.org/html/2602.11513v1`完整§3/4/5/6/Impact，含Def4.1、Theorem4.2/Remark4.3前提及Tables1–8。§3.2 honest-but-curious server知道机制、未知实现噪声，用户本地embedding/encoder→随机latent→cloud decoder/LLM；低维latent而非明文不是独立隐私证明。

§4.1 Eq7编码/解码器在server预训练；Def4.1以逐坐标v∈[-c,c]、u=2^n−1、p=(A+v)/(2A)抽K~Binomial(u,p)，映回[-A,A]。随机低比特发布自身参与随机化，不是先Gaussian再确定性打包。Theorem4.2实际给Gaussian tradeoff左右±γ界，而非有限参数下exact μ-GDP；Remark4.3还要求逐坐标|v_j|≤C/√d、A²−c²=uσ²与渐近项，且等方差特例为每坐标±c。一般L2≤C不推出该逐坐标条件；不把‘free’推广任意encoder输出、不认证所有sequence/request组合accountant。有限离散与continuous Gaussian的强身份未通过，已明确隔离，不为未采用理论扩全proof。

§4.2仅训练prepend soft prompt，LLM与encoder/decoder冻结，训练需对应perturbation distribution；其目的恢复部分任务效用，不是还原用户敏感真值。§5.1 public C4 encoder预训、target training data softprompt与C4 softprompt迁移分开，generation r100/NLU r20、c.05、d=b/32。§5.2/5.3在evaluation dataset binary-search使embedding-inversion ASR匹配后比较COH/PPL或Acc/AUC，**匹配ASR不是匹配DP**，BERT input inference也不覆盖adaptive/all攻击。

直接反侧：T1 LlamaWiki ASR.02 DEL COH.562<InferDPT-localLlama.742；T5 MoE16B.586<.664、Qwen72B.606<.648。T3 MRPC 4bit ASR.02 AUC.590<metricDP.598、2bit Acc.703<.711；误差条含义/运行重复未完整给，不签统计显著优势。T6 C4迁移严格ASR.02 LlamaWiki .514<InferDPT-localOPT.665；T7 μ52 prompt迁μ40 PPL35.91>目标prompt32.09。T8严格μ20 d32优于128，宽松μ60则d128优，压缩越强非普遍越好。T2标题Accuracy与正文COH身份冲突隔离，COH/PPL不作事实正确性或隐私强度。

通信仅n bits×d latent payload，不能补网络RTT/client运行内存/hardware/batch或完整SLO。encoder/decoder预训、softprompt训练与额外100tokens、随机化和连续查询均另计；输入边界/训练噪声/域迁移失败时停用该发布路径，保留更保守扰动、已验证split或经明确同意的本地执行，此回退为系统推断。裁决：作者2+2+2=6的有界随机压缩及扰动适配Source限定通过，exact隐私/免费/全攻击与accountant保证隔离。必要支持与直接反侧已足即STOP；唯一owner须具名实际正文比较与拟文，未授PRE/Books/DAY。

### 11524 ADMIRE：必要Source限定通过（按终局人口分配milestone辅助credit，非GUI-state证书）

实际独读`agent-core-0.json`精确`https://arxiv.org/html/2602.11524v1`完整§3/4/5/7/Limitations；另实际官方HTML Algorithm1 lines394–477、A.1 lines480–499、B.3/B.4.2/B.5/B.6 lines583–660，未扩全部prompt图/附件。§3 Eq6/7先由成功轨迹抽取milestones，新的成功路径再作更新；Eq8/9 SentenceBERT比较动作描述与当前pointer所指milestone，只提供有序语义匹配，不是独立GUI-state验证、最优路径或因果progress。

Eq10成功轨迹只奖励hit，Eq11失败轨迹加k/K底值及hit，是终局人口分责；Eq13在同组全部steps归一，长度人口与终局reward仍共同影响训练。**新增原件边界**：正文Eq11将k定义为trajectory achieved count，而Algorithm1按step逐次增加；不自修为已核唯一逐步credit recipe。Algorithm1 line445令p=min(p+1,K)，未显式锁已完成最后milestone，重复匹配最后项可能继续增k；line434在无成功初始化时K=0，而正文/算法未给完整空列表与division guard。不采用可直接执行的完整matcher/credit配方，作者须将这两点具名隔离于报告；无需为未采用代码保证扩查artifact。

主T1仅受测Qwen2.5VL3B/7B AndroidWorld/MobileMiniWob；T3 7B adaptive Mobile61.1<static-human63，§5.3不退火62>完整61.1，不能认证adaptive或退火必优。T4 GRPO Look63.6<process66.7、RLOO WebScore80.7<process80.8、DAPO Pick93.8<process94.9，平均不授全部任务支配。ALFWorld/WebShop另在线训Qwen1.5B/A.1.4四A800，非GUI模型zero-shot跨域。A.1 GUI八A80080GB/32AVD、4tasks×8trajectories、20steps、6500/512tokens、mini128/两epochs，GPT4o初始化/修订与processjudge以及warmup成本保留。

B.4.2的500描述pairs/δ.75准确81.3%<GPT4o85.39%，70×只是匹配该batch，不签全部训练或state correctness。B.5统计150epochs，ADMIRE187.99s/epoch>outcome166.83（+12.7%），并非免费；人评仅训练后保存milestones均分4.42/87.7%≥4，非全部在线更新真值。B.6末初始化coverage92.7%明确没有覆盖所有tasks，与无成功启动缺口一致。全部精度/batch serving/重复CI/开放GUI安全未披露不补造。失配时保留终局rule reward、固定经验证rubric与独立环境反馈，此回退为系统边界非其已核实现。

裁决：score2+2+2=6的adaptive milestone与终局非对称辅助credit Source限定通过；强可验证/精确进度/完整执行配方与全域安全已隔离。上述新增algorithm边界需进入作者包，窄命题不因此重审整个family。必要支持/成本/直接反侧足即STOP，owner需实际Ch33训练reward比较及逐字拟文，未授PRE/Books/DAY。

### 11596 MAPLE：必要Source限定通过（信号支持集与训练人口分责，非完整GRPO方差证明）

实际独读`agent-core-0.json`精确`https://arxiv.org/html/2602.11596v1`完整§3/4/5及Tables1–4；仅核作者signal-support×training-cohort命题，未读/采用AppendixE.3完整CRW或所有pseudo-code。§3独立A/V/S标注、Gemini对齐与modality-isolated生成给RMT标记；这些是任务条件下最小所需信号的构造/检查，不授客观所有模态最小充分真值。QA47893/546trainvideos与5001/68evalvideos、Caption5120训练无人工/5348eval均衡7tags，训练人口与分层评价身份明确。

§4/5.2 MUPO总给VAS，MAPO输入限制RMT并同时改tag batch；所以输入减少与分组同时变化，不能独立归因advantage normalization。§4.1先定义同prompt Grollouts归一，后称MU异质reward一并归一，身份未闭合；Var(MA)≤Var(MU)、难题必小advantage/gradient与完整稳定证明不采用。Eq2/3额外1/|B_M|与tag权重改变目标，不代签原population的无偏估计；KL-to-Beta(100,1)历史只是proxy，binary reward到连续density/smoothing未充分定义，不采exact universal difficulty/zeroKL解所有任务。成熟loss聚合、clip、filter不换名为新GRPO贡献。

§5 QwenOmni3B/G8/global256/mini32、AdamW2e−6、mixed precision+FP32head、原文4×H10080GB nodes；10240训练context与8096rollout不能合并成同配置。T1 fullrecipe58.72低于sample58.86/staticcurriculum59.05，AS56.92<MU58.77/VAS57.71<58.14，earlyfilter58.00<58.58。164.72 vs523.28s/step同时含删zero-variance/信号减少，不签等有效训练量、全epoch或生产SLO。T2 adaptive QA59.82平均较高但S61.35<MU63.82。T3完整74.00>MAPO73.88而V66.20<66.78/A81.42<83.46/S84.97<87.50，单项weight/static/dynamic各低于MAPO；不授所有tag/逐样本dominance，Caption LLMjudge不是事实真值。pass@1从5samples估计不改作pass@5。

T4 QA+把所有deficit标None，另25%exact/superset替正确答案为None，76.99只验证该合成label协议，非真实缺信号可靠abstention。§5.4.2 representation separation/tSNE与18.19→18.46fusion不认证causal grounding；具体CRW配方未采用。标注/对齐/generator/judge、模态encoder/rollout/过滤历史费用均计，CI/真实部署SLO未完整披露不补造。RMT错/shortcut/judge漂移/缺失分布失配时完整信号原训练、独立缺失切片与Unknown共存，此回退为系统推断。裁决score2+2+2=6的有条件信号/训练人口与缺失冗余验收Source通过；完整variance/gradient/abstain与生产保证隔离。必要机制/关键反侧足即STOP，Ch23或Ch33须具体唯一owner比较/拟文，未授PRE/Books/DAY。

### 11351 BAO：必要Source限定通过（turn行为罚项的作用对象与误惩边界）

root已有准入复用；实际独读`once-core.json`精确`https://arxiv.org/html/2602.11351v1`完整§3/4/5/6/Impact与Table1。§3 context固定、预算15turn、Au为提交Answer并取用户反馈/Ae为Action或Search，objective的U是用户action计数，而§5 UR为E[U/trajectorylength]。UR不是绝对用户工时/满意度，更多Ae也不是informationgain。§4 GPT4o行为SFT后，Eq2只识别连续Au并罚、Eq3只按未成功提前结束的剩余turn比例给每turn罚；命名information-seeking/overthinking不认证真实信息变化或thinking因果。必要求证、合法提前停止都可能误伤，授权与hard budget独立不变。

Eq4/5 turn credit广播到turn内token、reward-to-go对group总return归一，Eq5a左t而sum从k记号不一致，不采用完整唯一estimator或宣称新GRPO。T1直接反侧4B FunctionPassU1 .2692<无BR.3333/Score.6923<.7179，TelepathyUR.1870>无BE.1452、TurtleScore.1125<无BE.1146；1.7B FunctionScore.3590<无BR.3974、TurtlePassU1 .0563<无BE.0615/无BR.0594。Figure5仅Function三seed±std局部前沿，不授全任务Pareto最优。Pass@U文本‘up to k’与括注U=k身份含糊，不补认证全部精确事件口径。

§5.1/5.2同SFT/RL样本/epoch不代签teacher、rollout、token/FLOPs总预算相等；Function rule-based反馈只该simulator，不签现实gap为零。Telepathy训练Qwen3-8B用户→评GPT4o，Turtle训练用户与reward同Qwen→评GPT4o；§5.5长回答hacking观察与RTR只对应这些judge切换，非真实用户体验或攻击免疫。SelfBLEU/NVEmbed表面多样性不证明因果信息收益。teacher/SFT、用户模拟/judge、rollout/回报/记录全费，完整硬件/batch/服务SLO未给不补造。语言only/固定context不外推多模态或意图变化；误惩或净费退步时降低/关闭罚项与原终局reward共存，此为系统推断。

裁决score2+2+2=6的两个turn罚项与行为SFT接口Source通过，exact estimator/全部信息增益/普遍Pareto/满意度保证隔离。必要原证/对照/反侧已足STOP，不扩完整附件；唯一TRAIN-GRPO Ch33仍需实际owner差额与拟文，未授Books/DAY。

### 11564 LUVE：必要Source限定通过（latent、pixel、temporal目标与频带/噪声阶段分责）

实际独读`once-core.json`精确`https://arxiv.org/html/2602.11564v1`完整§3/4/5，§3.3单独完整复读以消除输出截断；含Eq1–5/Tables1–6及Conclusion limitation。采用低清motion latent→learned latent upsampler→高分辨率refinement接口，不以三段组合本身算新贡献。§3.3 latent L1仅约束codec latent，decoded pixel L1另管重建、frame difference L1另管相邻帧变化；Figure5仅定性支持pixel/frame目标及decoder，不签全部目标唯一因果或真实动态。直接latent映射避免中间decode/interpolate/re-encode，不取消训练时pixel监督所用codec或最终video decoder，任意resolution可查询亦非任意分辨率质量保证。

§3.4高噪声lowpass→attention LoRA与低噪声highpass→FFN LoRA为两条适配支集，base模块冻结；频率/算子/噪声区间与数据同时绑定，而非泛称多video数据/通用课程。Attention全局、FFN局部是此设计解释，不授严格语义/频带因果分离。LFE HPSv3>6.5筛选，HFE另Unsharp Masking，data与机制收益未全部独立控制。§4.1 Wan2.1 1.3B/UltraVideo，UHR训练15K再每expert3K、tswitch.417，LoRA/低bit或cascade不授免费训练。

§4采用250augmented VBench prompts；patchFID只局部，Doubao1.5Pro realism/detail/alignment是judge代理非物理真实。60videos/20participants人评仅其所测偏好。T1 2K TF98.18<Wan720p98.45/1K98.98，4K SC95.36<原95.70且overall84.03<本2K84.34；高分辨率不是全质量单调。T5 learned上采样.922s虽低于RGB40.12s却慢于latent interpolation.004s，该局部阶段非全视频费用。T6普通LoRA experts patchFID47.03差于无experts46.48，不认证加adapter必益或唯一frequency因果；full受测局部优不授域外。完整hw/precision/batch/concurrency、最终E2E/重复CI在必要主文未披露不补造，§5明确计算效率仍是挑战。

编码/latent映射/解码、pixel训练反传、过滤/增强、两expert与refinement全部计费；域/codec/频率/阶段失配、运动或净费退步时保留原latent/RGB上采样、普通LoRA或更保守低清/多步路径（系统推断）。裁决2+2+2=6限定多目标与阶段/支集接口Source通过；视觉真实/频率严格因果/全费等价或普遍加速不采用。必要机制/直接反侧足STOP，不扩附件；具体Ch23 codec或Ch24生成阶段owner需actual比较及拟文，未授PRE/Books/DAY。

### 12099 GigaBrain/RAMP：必要Source限定通过（训练条件、mask与部署分支身份）

实际独读`once-core.json`精确`https://arxiv.org/html/2602.12099v1`完整§3/4/5。采用§3.2.2 Stage2/4 stochastic condition masking与Inference的双分支，而非整个组件组合。WM训练的future VAE targets/episode success监督，与policy接收WM**预测**future tokens/value条件分开，不把未来GT frame直接喂policy的泄漏主张补进原文。Stage2 mask WM tokens p.2，Stage4 I与z都mask p.2；部署I固定1是乐观请求，不是真实advantage>阈值证书，efficient mode隐藏future tokens、standard mode读取实际生成z，两者须分别验收，不能把missing condition robustness当无损免费切换。

Eq2–4中improvement event概率与exp advantage成比例是另加假设；训练Eq3双conditional NLL不签精确RL最优/RECAP实现等价，predicted z亦不能消除全部未来不确定性。WM的future visual/value/proprio latent共同建模与4K小时训练，Stage4使用HILR+base共同更新WM与policy，human corrections及边界清洗改变数据人口，主文没充分给清洗判定/迭代receipt，不授自动纯无人闭环或无标签。旧condition-only训练/efficient current-observation分支可共存，但不可跨版本混算rollout/更新。

§4 foundation训练>10K小时含6K生成/4K真实、batch3072/100Ksteps，每task另batch256/20Ksteps，与RAMP增量分清。§4.1 RoboChallenge51.67写intermediate GigaBrain0.1，而Conclusion归0.5，不将该数字作为0.5M*采用性能。§4.2 value predictor同数据/约1M frames validation：joint state+value .25s虽低VLM .32s却慢于value-only .11s，joint MAE .0621/rank.8018是value proxy，不签future state fidelity或整action E2E。同single-task20K vsmulti60K与后文图按20K展示的预算人口需分别保留，cross-task比较非全部训练费相等；3tasks RAMP/AWR/RECAP main未披露完整HILR量/随机试次/CI与mask p.2独立消融或efficient/standard质量配对，不采所有部署分支同收益。

WM/VAE/value、MLP、denoising、policy前向、真人修正/数据清洗与迭代训练全费；A800单value帧延迟不作完整robot控制频率/安全SLO，精度/batch/concurrency/完整controller未披露不补造。预测/值校准漂移、mask条件或版本不兼容时保留已验current-observation policy与真实反馈/人工接管（工程推断，不声称原实现有完整guard）。裁决score2+2+2=6的有监督条件与部署mask接口Source限定通过；强最优/真实未来/全机器人可靠或无损免WM费不采用。必要支持/直接代价足STOP，具体Ch25/26 owner仍须actual比较与拟文，未授PRE/Books/DAY。

### 12221 UniDFlow：必要Source已完成，different-reference中心不通过、step-router仅局部通过

实际独读`once-core.json`精确`https://arxiv.org/html/2602.12221v1`完整§3/4/5/Impact，含Eq1–9/Tables1–4。作者score2+2+2=6保留，不因中心争议改分、删反证或清候选。Eq6以diffusion-step hidden state产生αt，组合已分训understanding/generation低秩增量，step-router局部接口可用；StageI/II参数隔离与StageIII router、preference/DFM、reference policy身份须分别记录，不把已有task LoRA当新增贡献。

**不同reference-condition preference中心不通过，隔离Only/Report。** Eq7/8明确写winner x_ref^w、loser x_ref^l，但§4开头明确3.5M偏好样本under identical inputs and reference images，Impact又称shared conditioning；不同变量名不证明实际条件不同。不能将本篇发布为已验不同reference DPO机制，也不能把其数据实验唯一归给这一条件差额。保留双方位置，不自改公式/数据身份。重开只需该exact版本实际pair schema/样本或实现说明明确x_ref^w与x_ref^l是否相同及采用loss，不为未采用中心扩全附件。

其他未采用的完整recipe争议：§3.2.1先定义RMSNorm含γ，Eq2再乘γ，s=b=0得到γ²而非其声称exact原norm；逐维scale加bias亦不保持一般hidden direction。Eq9 edit目标写text0而输入vis_t，未纠正为确定训练公式；DFM denoising conditional概率不能未经轨迹归一核验代签完整π密度或exact DPO。以上不进入正面Books与未核实现声明。

§4 StageI MMInstruct/StageII T2I4M/StageIII3.5M偏好，training/evaluator/硬件/精度/batch/step预算与所有对照匹配未在必要主文充分披露。T4 router/多LoRA消融支持局部联合recipe，不独立证不同ref条件或step-router普遍必须；SingleLoRA仍Eval79.92/Gen.90/Edit4.08，不能照录‘fails entirely’。DPG T2 91.19与T4 91.91冲突不合成一个点，table平均/单任务主文领先不授所有fidelity/开放安全。reference构造/judge、tokenizer/codec、双adapter/router、三个stage/反思/多步采样均全费，不从冻结base或参数少签低完整内存/速度。

裁决：必要Source完成到安全限定；仅step-wise adapter composition与条件identity责任局部通过，different-reference中心与完整norm/训练配方不通过且隔离，不授整篇全Source正面保证。Only或实际已有覆盖须由具名owner正文比较，不能自动写Ch30/34；保留独立任务adapter、固定route、已验same-condition偏好与原sampler回退（工程推断）。支持/直接冲突已足STOP，未授PRE/Books/DAY。

### 11758 HAIC：修订后必要Source限定通过

实际独读`once-core.json`精确`https://arxiv.org/html/2602.11758v1`完整III/IV/V，含Eq1–2/Tables1–6；原作者一般动态障碍/规划constraint路由不获采用，现持久包已按实际III-B窄修，复用本轮实际原证不重读全部附件。接口为proprioception history与future reference motion预测对象相对pose/velocity/acceleration，以预测R,p变换canonical point cloud，再交privilege adapter/student controller；Eq2只对点云施R,p，v/a是另传状态，不是高阶几何投影、实际occupancy或外界测量。教师privileged state与student预测输入不同，stage1 joint RL/distillation、stage2 asymmetric训练与EMA rollout/gradient network分责，不签动作因果世界模型或任意障碍恢复。

IV外部PC/Ethernet部署与后文onboard computation说法冲突隔离。单RTX4090约8h、policy50Hz/PD模拟200和真机500Hz仅各阶段身份，未给全controller尾延迟/precision/batch/SLO，不能把控制频率当免费可靠性。真机skate glide100%但completion60%、cart+box pulling40%，Table5模拟100%不搬为真机；Slope位置60.5>53.5、orientation324.7>289、速度8.77>3.68、加速度4.60>3.39及stair orientation退步保留。large box/heavy3kg案例不授未知几何通用可观测、物理平衡被理解或安全许可；完整试次数/CI必要主文未披露。

参考动作/mocap、teacher特权、渲染点云与训练/在线预测均计费；预测失配时保留真实状态反馈、已验controller/任务中止与人工边界是工程推断。作者修订后的2+2+2=6窄对象状态估计→控制consumer Source PASS；旧一般障碍/规划claim不通过。必要支持与直接反侧足STOP，owner/PRE仍须actual正文与拟文，不授Books/DAY。

### 11832 JEPA到VLA：必要Source限定通过

实际独读`core-2.json`精确`https://arxiv.org/html/2602.11832v1`完整§2/3/4/6。§3采用frozen V-JEPA2视频表示作为VLA额外action consumer输入；无大规模robot预训练的basic VLA用linear projection/early concat，robot-pretrained OpenVLA-OFT侧用受Flamingo启发的gated cross-attention，原VLA token query、JEPA KV，每8层稀疏接入，fusion LR1e-5–1e-4不同原VLA5e-4。是consumer/预训练身份与适配预算，不授新gate首次机制、所有concat必失败或所有representation可即插即用无训练。

§2 frozen representation轻head估当前状态与10步expert未来状态MSE，nuisance probe只first frame且背景/光照每trajectory恒定；低task MSE/高nuisance MSE不证明不含全部nuisance、动作干预因果或真实物理模型。§4 actual两third-person frames+语言不能外推任意多相机/proprio setting。basic Chameleon监督40epochs与OpenVLA-OFT LIBERO150K/RoboTwin约100Ksteps是不同数据/预训练人口。Table3本人复现baseline90.30→96.40，官方95.35非相同baseline；Goal本方法95.6<官方96.2/Object98.0<98.3。Table2 Noise4.1不变、Camera.1→.4仍近零；RoboTwin PlaceFan Hard0→0，hard平均17.7不授普遍可靠。真机仅Piper单pick任务、22条1/5数据，试次/CI未完整披露。Table6 bin picking80<VC1 84/reacher821<836；Table7两DINOv2行身份冲突不自行改名。

主必要范围未给early concat/gated的完整配对消融或hardware/precision/batch/端到端推理延迟，稀疏接入只设计预算，不签全latency更低；若采用具体延迟须另定点必要原证，不为本窄接口扩附件。视频encoder、投影/交叉attention、action head、robot数据与适配训练全费，失败或状态漂移保留原VLA/真实反馈与安全边界（工程推断）。2+2+2=6窄consumer与预训练身份Source PASS；表征物理真值/动作因果/全实时免费不采用。必要证据足STOP，具体owner仍须actual比较，未授PRE/Books/DAY。

### 11980 SCoT：必要Source限定通过

实际独读`core-2.json`精确`https://arxiv.org/html/2602.11980v1`完整§3/4/5/Impact，Eq1–8/Tables1–5。§3.1将phrase span按caption次序紧接离散0–1000 box token，§3.2独立MLLM planner生成同一interleaved text-coordinate条件，renderer训练接收该接口；两者可分别更换而不joint pretrain。MLLM内部提出/检查/修改box，不是独立几何constraint verifier或严格可满足证明；重复/重叠phrase span与token对齐完整异常guard未给，不补成完整parser实现。

SCoT-DenseBox用Qwen3VL235B标注，单grounding训练可损aesthetics，再AestheticSFT保留视觉质量；QwenImageEdit2509两stage各2epochs/H800/不同LR和Gemini3Pro planner均是费用/身份。Table5同renderer TextCoT→TextBBox→SCoT局部提升支持接口与结构计划联合recipe，不独证interleaving为唯一原因，也不授渲染必遵守box。Table4 Qwen2B Composition70.9<无planner77.9/Overall58.6<58.9/GenEval79.7<81.7，强planner不是免费或普遍可替换。Table1 ours整体78.3低NanoBananaPro82.9，MA79.2<Qwen83.2/TR86.2<87.4；Table2 OneIG mean52.4<Qwen53.9、Align86.2<88.2/Style39.8<41.8/Div14.5<19.7，GenEval SO98.1<99/Color87.2<88。COCO-MIG SR42.38%仍非严格成功，globalCLIP25.91<CreatiLayout26.22/MIGC26.21；T2ICoReBench Qwen30BThinking checklist为judge proxy而非独立几何真值。

必要主文无完整batch/precision/采样steps、planner token/重规划/renderer全E2E或重复CI，不能从“不改backbone架构”推零架构/全费用或生产保证。标注/两阶段训练、planner/validator代理与renderer都计费，失败时保留原text-only、经独立检查的布局或人工修订（工程推断）。2+2+2=6窄phrase-box→renderer消费协议Source PASS；strict空间因果/全planner可靠/零成本不采用。支持/直接反侧足STOP，不扩editing/全部数据可视化附件；owner须actual现段比较与拟文，未授PRE/Books/DAY。

### 11619 When Agents Disagree：必要Source限定通过

实际独读`agent-core-0.json`精确`https://arxiv.org/html/2602.11619v1`完整§3/4/5/6/Impact，Tables1–5。采用answer modal fraction、tool-action sequence diversity、path length variance/first divergence分别测量，不能以序列/答案一致取代真实outcome。§3为100hard HotpotQA distractor题、79bridge/21comparison、10paragraph含2gold/8distractor，Search词法/Retrieve/Finish的ReAct，三API模型每题10runs/temp.7；不同API provider/模型能力是身份非受控规模因果。Correctness是gold/answer case-insensitive互为substring，长混合错误回答亦可能通过；行动示例只有tool type，args/replay等价归一未充分披露，不补成完整轨迹身份。

T2一致≤2/不一致≥6相关人口各79/9、70/10、25/29，3–5中间任务不在极端比较，不签全人口概率校准。T3 Llama step2为59/86发生divergence题、非100题69%或全部model必因果；step与正确r=-.34可能任务难度混杂，不签强制截短改善。T5 comparison correctness80%高于bridge75.7，但answer consistency62.4%低76.6，直接说明稳定与可靠不可互换。T4说20题temp0对照，却temp.7的77.4/4.2与主100题完全相同，matched20题baseline未独给，+5.4pp不授受控温度因果/生产推荐；temp0仍2.2序列不授determinism。T2统计显著只Llama局部极端分组，不能替代独立校准或干预。

§5并行agreement/earlyquery干预只是建议，不是已验runtime earlystop、FPR、实际救回与执行权限；单100题/词法检索不外推web/coding/alltools。十重运行、API生成/检索/重试/selection总费与真实授权独立，必要主文未给全hardware/batch/E2E或heldout operating校准不补造。原判分2+1+2=5限定测量人口/直接反例Source PASS，novel ReAct/概率正确证书/自动控制不采用；事实未知保留独立outcome证据、Unknown或人工检查（工程推断）。必要机制/反侧足STOP，具体Ch66真实覆盖或一段差额需actual正文/拟文，未授PRE/Books/DAY。

### 11636 ScalSelect：必要Source限定通过

实际独读`agent-core-0.json`精确`https://arxiv.org/html/2602.11636v1`完整§3/4/5/6、Eq1–9/Tables1–7。§3.1第一层head均值user→visual attention累加各user token，以90%mass选择视觉token再均值第一层hidden，user query改变选择支集；conversation含assistant，但attention score只user人口。Eq2未写causal mask，不能从这一选择接口断言前置visual hidden本身已经读取后面的instruction，attention亦不是grounding/正确标注真值。§3.2全体sample表示列中心化，最小k覆盖90%总σ²，πi为Uk行平方和、deterministic top rank；主子空间leverage是此表示population的variance-support，不是下游能力、label truth或随机CUR全重建保证。稀有低方差信号漏选是工程风险而非本文已测事实。

§4 O(Ndk)需fixed d及小k，k9只该第一层LLaVA表示，T7 middle59/deep260，不能授任意population恒定rank或免费严格线性全过程。image encoder、第一层/attention提取、按token排序、Nx d存储/中心化/SVD及全局top rank均付费；主文没有实际selection walltime/峰值内存/所有训练净费。§5 LLaVA625K去40K text-only/另LRV180K、100K16%主预算，LLaVA instruction前checkpoint与Qwen3VL4/8B、8H10080GB/各1epoch；same epoch不等有效token/forward费。Rel是各benchmark按表reference归一平均，不是97.85%统一准确或全部能力保留。

T1 MME-P1400.34<Random1418.85/POPE-A83.96<84.96/MMBench及SQA低COINCIDE、POPE-P94.73<Length96.71；T2更多样本非所有指标单调，400K MME-P1425.41<300K1517.26/OCR19.8<full20.3。T3 Qwen8B MMBenchEn82.46<full84.30/POPE-P94.39<96.39；T4 LRV MME-P840.59<Random848.76。T6 NoInsCon MMBench61.72/55.44>full59.19/52.80、NoCenter SQA66.29>65.29；T7 deepOCR19.60>first19.40，联合aggregate不授所有数据/任务第一层最优或instruction-selection唯一因果。必要主文precision/batch、全部CI与E2E生产SLO未披露，不为未采用性能扩附件。

2+2+2=6窄instruction-dependent选择支集与global variance-support分责Source PASS；attention真值/全部能力保持/无训练即免费/所有N严格线性保证不采用。checkpoint/模板/causal语义与population变化时须重新提表示/谱，slice退步或费用失配时保留随机/分层子集或完整训练及独立能力验收（工程推断）。支持/直接反侧足STOP，唯一TRAIN-DATA Ch27实际覆盖与拟文仍待PRE，不授Books/DAY。

### 11729 Cross-Architecture Model Diffing：必要Source限定通过

实际独读`agent-core-0.json`精确`https://arxiv.org/html/2602.11729v1`完整§1/2/3/5/6，§3独立完整补读以消除首次输出截断；另官方exact-v1 HTML Appendix A `378–412`资源与B1.6 `526–663`窗口对齐/Algorithm1/失败人口必要定点。§2共同重建的shared prior由专属/共享dictionary分区改写，专属feature对另一模型重建梯度切断；这是结构分配与发现候选，不以decoder置零认证另一model不懂概念。§5明确representation exclusivity≠conceptual capability，不授真实风险全召回或全部政治/版权标签事实。

§3.2 toy2048concept/800M pairs/5seeds standard error，recall提升伴shared误判或无concept假阳性；“安全场景召回一定优先”只是成本偏好，不能自授。真实模型无GT，另学linear stitching后比较steering产生行为、Claude4.1Opus1–5→6−similarity；只25人工ratings核验，affine/steering强度/解释或judge误差也会使transfer失败。每类500feature且active/interpretable/clearsteering过滤后的分布不外推全部latent；FVE.817同baseline、detection87.78近87.77是重建/代理非整体模型能力无损。最大激活解释亦可能不产生稳定steering，故仅screen→validate。

§3.3 smaller1/3%与随机seed会漏细粒度/部分American feature，§5也确认发现不稳定。30curated prompts/judge/95%CI只受限注入效果，非自然输出唯一必要因果或训练来源。版权拒绝负向steering导致coherence明显退且hallucinate，正向又误拒benign，不认证准确获取内容；base-v-finetune mirror features也有失败。B1.6 decoded-text窗口贪心匹配后取末token，最后activation涵盖全window仅希望；失败返回此前prefix。1000texts的992/991成功不保证非英语/chat/special字符风险slice完整，Table5 n9 vs column n8身份亦不补成精确率证书；算法跳过非内容后边界/normalize全实现未核，不授可执行完整guard。

Appendix A披露每pair采集3H10080GB约24h、每crosscoder单H100约24h/final5runs，interpretation每experiment约500,000 Claude4.1Opus API queries，资源不计preliminary/tuning；不能称已知完整总费。对齐/cache、数据、stitching、steering/judge与外部验证全費，BF16/B2048仅官方局部配置非在线SLO。2+2+2=6限定分区重建prior与screen→validate Source PASS；exclusive概念/全风险安全/稳定全面发现不采用。失配或假阳性成本过高回标准crosscoder、行为/redteam suite与独立effect核验（工程推断）。支持/反侧足STOP，不扩其余附件；Ch66 actual owner/拟文仍待PRE，不授Books/DAY。

### 11749 AIR：必要Source限定通过（post-effect与future-precheck不同权威）

实际独读`agent-core-1.json`精确`https://arxiv.org/html/2602.11749v1`完整§3/4/5/6/Impact；§4独立补读首次截断的主Table1完整人口，后段与首次完整范围接续，不拿缺表当已读。另官方exact-v1 HTML B1/B2与C `462–501`必要对照/良性人口，未扩A全部case/代码。§3两个hook分别在工具已执行后检查、未来新plan前拦截；trigger只选择哪些NL check读取inspection/current state/observation/context，同agent解释check与执行remediation不是独立安全验证。命中后工具补救并终止原task，incident再生成future plan guard；计划意图不等实际tool args/effect，所谓eradication是未来受限防复发而非已泄漏内容、删除或不可逆物理损害被撤销。

ANTLR4 DSL/公开OpenAI Agent SDK参考只主文事实，未核实现或LangChain部署。补救本身的权限、当前真实状态、可恢复条件与新副作用需要独立验收，自动生成rule不能自获发布authority；这些是工程要求，非论文已实现全guard。规则过宽/过窄、opaque tool、同模型误判/理想化“恢复已删除文件”仍会失败。

§4手写rule按已知risk类别，RedCode25×30/Embodied10×25/browser7×30，exe定义实际已发生incident人口，拒绝/执行失败已排除；T1 bias exe30/det22/era17、defaultcase30/19/25，而正文又把低det归未生成risk，口径冲突隔离，不自改分母签全检测。T2 electrical7/7/6/6与slip19/19/17/17；T3 phishweb6/5、induced12/11/10/10等实际反侧。人工GT不补盲审/一致率/重复CI，rem为–不可逆case只future block。T4 benign27.442→39.610与64.766→90.602增加约44%/40%，6.918–11.735s check和恢复/合成49.273–94.031s等全链分开，不能取小check比例称免费SLO；§5并行小模型/短delay仅未测建议，不签delay安全或原质量保持。

T5 GPT5规则三例+risky示例生成、无手修局部det/rem不满分；B1 structured rem比self好不等匹配所有推理budget/唯一DSL因果。B2采100/100/50task三轮54→6→0等，仅同风险分布且主附件未明确逐轮heldout/repeat身份，不能签新分布零事故。C50/35safe零FP只小人口，CUA8pass/27fail并非可靠任务完成；无code良性完整回归，硬件/精度/batch/基础agent完整API版、全token费与线上FPR/SLO未披露不补造。

2+2+2=6安全接口受影响加深后的Source PASS：仅post-effect检测/补救终止/future-precheck分责，NL检查安全证明、不可逆回滚与自动rule发布/全开放保障不通过。检测/规则/恢复失配时保留hard permission/effect gate、独立inspection/人工协调和原停止（工程推断）；所有检查、恢复、生成与验证全費。支持/直接反侧足STOP，唯一Ch72或workflow的具体owner差额须actual拟文比较，不授Books/DAY。

### 11750 AmbiBench：必要Source限定通过

实际独读agent-core-1精确https://arxiv.org/html/2602.11750v1 完整§3–6；首次组合长输出§3/4中部截断不计已读，恢复后两节完整独立补读9236tokens，§5/6先前完整范围复用。§3固定atomic intent后分开去path、parameter、anchor；175 requirements/240tasks/25apps/108interactive，120/80/40难度只以要求数定义，不等通用难度。posterior转换preset pseudo-prior及value-laden排除、所有遗漏参数强制nondefault，改变真实用户意图人口；ADB初态注入只logical executability，不免在线UI/网络漂移。

§4 GPT5用户只在Incomplete/Ambiguous按固定intent补参，未定义回NoPreference；raw screenshot/action/interaction先经语义serializer再MLLM judge，是代理而非独立真实意图oracle。Outcome的v_i=存在任意e_t满足r_i，TSR要求每项都有曾经满足证据，不认证最终同一状态同时满足及持续效果。Process semantic LCS只参考顺序；IGR已补gap比例不是Shannon信息，空gap/空turn完整guard未采用。三份账不能互代或授权effect。

§5 Table2 Fairy6 RCR48.7/TSR40.4/IGR17.7与DCR73.7，UI-Tars DCR87.2/IGR12、Qwen DCR88.9/IGR2.4说明礼貌合规与补参分责；不是全优。关闭交互的miniablation只预选Fairy已成功Incomplete人口，100→0不授一般无交互必失败/开放因果保证。100trace三expert doubleblind κ.91、outcome Jaccard.92/step.84与96%补参有效只该proxy校准，不授全用户satisfaction。20Snapdragon865/Android13、最多25steps、开源RTX5090/vLLM与闭源API不同条件，T0非确定性；AutoGLM9B表vs7B正文/UI-Tars开放vsAPI身份冲突隔离，完整modelrevision/precision/全tokenAPI费/CI/SLO未披露。§6 simulator/视觉语义/动态环境/clarity边界保留，代码未核。

2+2+2=6限定controlled information stripping、requirement-first和coverage/process/dialogue分账 Source PASS；最终联合state、真实动态意图/满意度、普遍澄清因果和完整计算recipe不授。原始证据、确定性state验证、实际澄清/人工授权为失败回退工程要求。支持/反侧足STOP，不扩无关prompt/附件；actualCh66差额仍待具名PRE，不授Books/DAY。

### 11754 Cooperation Delay：必要Source限定通过

实际独读agent-core-1精确https://arxiv.org/html/2602.11754v1 完整§2–5/F3–4/T1。server在D_i后更新action并同时通知对手，timestamp来自server；agent每Δt读取current策略/reward及15s改变历史，prompt明确delay、只最大化自身reward。不是纯传输延时与真实LLM墙钟开销实验。固定双方同A1/C−1/N1、同delay，60s/Δt1s、payoff5/3/1/0、GPT5mini/Sonnet4/T1，每条件10trial只末20s，F3误差SD非CI。合作U形、利用invertedU且20s恢复仍低于0s，仅该固定设置；一句CoT把迟到报复读为耐心只是相关例子，不能授内在真实意图、单因解释或任意人格/不等delay有效。

§4.2 p titfortat与(1−p)αD_i的toy、500trial拟曲线支持可存在竞争机制，不认证LLM同一算法。α.1/.2与D15/20可能越概率1、未给clipping完整guard，故完整simulation配方隔离。FLCOA五层/搬server/调整timeslot均框架建议，未实际测补偿与全墙钟费用。硬件/精度/完整modelrevision/初始化/并发/tokenAPI账与SLO未披露；不能以simseconds签性能收益。2+1+2=5窄stale feedback误读与合作非单调反证 Source PASS；延迟越大越好/全agent自发合作/安全协调不授。timestamp/staleness与实际effect独立核验属工程边界；必要支持/反侧足STOP，不扩code，Ch82 actualowner待比较，不授Books/DAY。

### 12276 CATTS：非作者必要Source限定通过

root为本项Source作者，本reviewer实际独读agent-core-1精确https://arxiv.org/html/2602.12276v1 完整§3–5/Impact/Eq1–10/T1–4，并直接官方HTML AppendixH `689–714`必要阈值表，不以root笔记代原件。每步先固定N采样、semantic LLM聚类得p，再按H或1−margin阈值选择是否额外同gpt-oss120b arbiter；动态省selector调用，不免N生成/聚类，不授投票真值/独立错误或effect权限。低共识额外选择可能有益，高共识override关联坏结果并非随机因果；495task-runs条件组及事后平均轨迹entropy不是部署可读成功oracle。τ grid未给独立heldout选择合同，取best/跨阈值均值不签普适校准。

WebArenaLite165 programchecks/GoBrowse341 Qwen3VL30BA3B judge，cleanedHTML/ReAct8工具、3seed作者结果；费用总input+outputtokens不等总API/延时/真实动作费，硬件/precision/batch并发/SLO未披露。N10→20主文称+.2而T1实际43.2→43.0；K10→20 WA44.6→42.0，DeepConf多配置退步。T4 margin47.9/405K宣N10，H T10仅N5τ.5/N20τ.7=47.9、N10最高46.1，冲突直接核实隔离，不采56%匹配预算或2.3×统一因果成本保证；H baseline另有43.8与T1 43.0身份未自行修数。

2+2+2=6限定候选vote分歧→条件selector投入接口 Source PASS；稀少错pivot恢复不授已证不可逆，highconsensus也可同错。聚类/模型/环境/阈值漂移与误override、采样/聚类/裁决/执行全费均保留，失准回固定多数票和真实环境验证。支持/直接反侧足STOP，无需扩全部附件；actualowner可Existing须具体比较，不授Books/DAY。

### 11782 FlowMind：必要Source限定通过

实际独读agent-core-1精确https://arxiv.org/html/2602.11782v1 完整§3–5/Limitations；官方HTML必要E4 `741–775`、E5/6 `776–843`与F1/2 `845–895`直接费用/失败人口。Execute只业务工具产真实轨迹，Summary移除业务工具只构图，derived graph仍压缩提案；业务完成/graphvalid/blackbox全例测试分账。多轨迹可聚合不免额外执行与筛选费；失败、缺step与低频依赖可传播，成功trace不等图泛化/授权发布。§4.3工具可见性/阶段/prompt一起变，cognitive burden作者解释非单心理机制因果证明。

T1 141cases/694tests，GPT5 ESReAct test28.7<30，Qwen32 ESP&E24.9<25.1/GPT4.1 joint90.78<95.04，非全部指标胜；主133/200漏图与E5 57/190不同人口不合并。E4 Qwen32 ESReAct总output15,103比12,317多22.6%，全方法省token宣传不授。E6三rollout、成功trace选择及强Claude可解141子集不外推所有工作负载。F累积调用时长含retry/scheduling非墙钟，4A10080GBPCIe/局部4H100、vLLM.11/Torch2.8只该setting；AOAI与另一officialAPI身份保留，reported finalizedruns不含开发/tuning，precision/逐配置解码/CI/真实SLO缺项不补造。

2+2+2=6限定阶段工具可见性及trace→复用图权限差额 Source PASS；无损忠实/通用跨域/自动生产部署与全成本效率保证不授。独立blackbox测试、当前state/effect审批与原直接执行/人工图审回退属工程边界。支持/直接反侧足STOP，唯一Ch81 actualowner待拟文，不扩D全理论或所有prompt，未授Books/DAY。

### 11812 EGTP/PLP：必要Source限定通过

实际独读agent-core-1精确https://arxiv.org/html/2602.11812v1 完整§3–5；初次输出§3.3/§4setup中部截断后独立完整补读。官方B2 `320–338`、D3 `460–471`与E3 `505–529`必要定义/层反侧/module成本直接读；检索返回邻接C1 `342–355`同时观察到主文“严格原split”与附录所有数据3:1:1的identity不明，不授精确original-heldout/时间policy迁移保证。

prompt-total与已生成prefix-conditioned remaining两个forecast对象成立，entropy加权已有hidden及近bin软标签/expectation+CE/MSE只是监督分支；BERT10k r.451相关非EOS因果/全部LLM最优权重。Eq3温度α正文有而式无、§3.3全部generatedhidden concat却同head增长维度适配不明，完整PLP执行recipe隔离。LMSYS闭源GPT4/Claude2自身hidden可访问身份未给，不授该正面实现。softbin概率非校准EOS，remaining误差下降不证每步单调/确定终止。

Qwen3B/7B reasoning MAE139.04/133.57差于TRAIL132.20/124.19，非所有best；D3中层12MAE70.26<末层24的73.93，final非普遍最佳。1V100/10core64GB/b16/seed42/≤10epoch/K20/λ.95只是训练，D另λ.99不替主setting。B2 throughput jobs/time、padding以actual为分母，不自读tokens/s。T2 vLLM/SJF两负载未给完整arrival/generation硬件/precision/batch并发/tailSLO/fairness；平均JCT好不免starvation。E3单4090测预测module.65–.67ms/5–7MB，不含完整prefill/logits/full-vocabulary entropy/generatedstates驻留及反复online预测，不能签免费全系统开销。

2+2+2=6限定hidden可访问模型下forecast表示/估计对象 Source PASS；完整维度未披露/closedhidden与一般SJF最优保证不授。访问失败、长度漂移/净费或公平性不成立回prompt/固定预算与透明FIFO/公平调度属工程推断。必要支持/反侧足STOP，不扩代码救缺项/全部GRPO曲线；唯一Ch56 actualowner待具名比较，不授Books/DAY。

### 11877 RouterXBench / ProbeDirichlet：必要Source限定通过

实际独读agent-core-1精确https://arxiv.org/html/2602.11877v1 完整§3–6/Limitations（§7只结论路由不作新增证据）、官方A/B1 `389–423`与D2 `469–473`。label判别AUROC、部署band表现与跨域迁移三账成立；大模型补救能力不能由小模型失败排序签。准确任务xVerify9BC对gold语义判定亦非纯规则oracle；开放任务GPT5同时强model和blindjudge，label为small score≥SOTA不是绝对正确，不能说完全独立large身份。LPM/MPM/HCR积分测callrate，不是tokens/墙钟总成本；非单调Φ、空feasible与d2≤d1/PerfL≤PerfS完整guard未采。

§4 prefix各层hidden先mean再globalDirichlet权重训练sample、推理mean；β共享全input，不是逐query自适应权重/uncertainty因果或probability calibration。Llama3.1-8B/GPT5，12K三域/3.2K+.8K/不同1K10Ktest，linear4096/50epoch/lr1e−4/A单seed42只该人口。T3 Dir68.70与Mean68.04差远小于跨层vsFinal53.91，不能全归Dirichlet；T2 AlpacaLPM76.50<SelfAsk76.52/HCR13.5<14，T6 Alpaca71.85→71.63/BigMath66.49→66.18反证无interference普遍宣传。D2双边同错无路由补救，abstain/扩pool建议未实际验开放安全。

2+2+2=6限定评价分责/global训练正则和部署固定权重 Source PASS；全边云latency/privacy/安全与完整metricrecipe不授。各层hidden访问/教师标签/校准/升级重复prefill全费用，hardware/precision/batch并发/fullrevision/API价格/SLO未披露；漂移回固定已验收路由/独立verifier/Unknown属工程边界。支持/反侧足STOP，无需扩完整pseudocode，唯一Ch66 actualowner待比较，不授Books/DAY。

### 11908 Selective Abstraction：必要Source限定通过

实际独读agent-core-1精确https://arxiv.org/html/2602.11908v1 完整§3–8/T1–3；首次输出§4/5中部截断后两节完整独立补读。官方H `379–422`必要algorithm/定理条件直接读，不采用完整风险证明。原model生成→atomize→提出较不具体候选/评分→最具体过threshold→重构，失败仍abstain；weakening仅prompt要求，严格entailment/claim依赖/重构未新增claim条件未验。verbal confidence只是proxy，宽泛化不自动为真或高stakes安全。

§4 Wikipedia+gptoss120b的unsupported含refuted及查无证据，102人工claims F1.93局部校准非全truth；uniformprior/Wikidata稀疏entitycounts去重相加非joint语义信息，零集合/单实体/全零信息的全域recipe未采。§5六openmodels/同36FactScore+76LongFactobjects/defaultthinking人口有限；T2 LlamaFactScore Inline −.70直接负侧，其他prompt只singlepoint非全threshold等投入。T3平均48/59.4atoms×4.4/4.3候选，generation/评分/abstract/search/SPARQL/reconstruction验真全費，hardware/fullrevision/precision/解码batch并发/墙钟SLO未披露。

§7 30%prompts校准重复100次/六model均值600不等600独立部署样本。H pool同response相关atoms，exchangeability与distinctthreshold/no-ties条件未证实际满足；θ为首次选对的critical threshold不证明所有更高threshold后续candidate皆正确，θtest越quantile的形式risk也不等最终多claim错误率。全部α+ε高概率真实风险保证隔离，不修理论或扩附件。2+2+2=6仅分级claim输出与specificity/reliability测量差额 Source PASS。弱化失真/检索不足/失校准回redaction/显式Unknown、独立依据及重写后支持核验属工程要求；唯一Ch66 actualowner待拟文/Existing，不授Books/DAY。

### 12268 CM2：必要Source限定通过

非作者实际独读 agent-core-1 精确 https://arxiv.org/html/2602.12268v1 完整§3–7/Eq1–10/T1–4/F3，另官方Appendix.3 `345–347`实际核。细criteria与credit时间assignment是两轴；同checklist的trajectory/turn/step对照中，细assignment早期快而更早collapse，支持受限人口中的分责，不支持所有环境必如此或judge噪声已被唯一因果识别。后验label从原trajectory抽取，当前prefix judge不是工具真实state/权限核验。

Eq2以pre-step依赖已满足及unsatisfied→satisfied给事件奖励，Eq3仅step路径回填较早eligible步，不等因果critical step。Eq4的只flip一次叙述依赖Sat单调/永久latch，而prefix judge未说明该保证；Eq10空eligible分母guard亦未明。完整bounded执行recipe隔离。官方Appendix.3实际std denominator设1，24/48 group、最终trajectory G48；不能拿普通std归一化的噪声机理当本实现唯一归因。Strictness终止控制后续人口，不授原轨迹后续state反事实。

§4 Nemotron310K→280K→30K、8K冷启动与另8K复杂RL/500validation，过滤、CoT压缩和训练并变。工具exact name/args匹配回放，否则30B-A3B模拟，同model作judge；没有真实执行/rollback证明。64GPU×680h与$.1/checklist标注不是全链费用，型号/precision、完整rollout/judge/token/wallclock/SLO未披露。§5 T2原8BBase CM2 avg26.76仍低于Thinking32.00/30BA3B32.03；另5K in-domain+Thinking init的41.39不合并为同人口收益。BFCL MultiTurn36.50<Thinking37.00、ToolSandbox Interrupt70.31<76.77，非全slice优势；τ²四次均值不替其他表重复CI。10K/30turn训练与>30K/200turn评价错配保留。§6强judge/ensemble使细step可行只是未验方向。

2+2+2=6仅两粒度分责与该人口直接反侧 Source PASS；模拟judge不授执行authority或全recipe保证。必要证据足STOP，不扩全部prompt/code；唯一TRAIN-GRPO Ch33 actualowner/PRE仍待比较，不授Books/DAY。独核层现56/57，剩VAT12134。

### 12134 VAT：必要Source限定通过，exact metric身份隔离

非作者实际独读 agent-core-1 精确 https://arxiv.org/html/2602.12134v1 完整§2–6/8/Limitations/Ethical；官方C `475–490`及E Figure9图注`555`定点实读。仅采用同scene-action配对pre/post的多维ordinal judgment shift、target平均gain/非target变化/跨sample co-variation三者分账。Likert中心化、support/violate符号与56→10类聚合不等潜在trait或真实价值真值；Spearman co-movement不证明干预因果、协调计算成本/伤害。

§3 GND分母|Gain|要求非零，小gain敏感。R定义包含self-correlation，在方差有定义且diagonal=1的通常矩阵下nVAT=||R||F/√|V|至少1，而T2约.09–.15；E图注只说可视化省diagonal，未明确计算也如此或额外归一。C补80%scene bootstrap、Spearman/Kendall排序和56D/10D一致，未解该identity。exact nVAT/Gini数值跨配置比较、完整metric执行recipe均隔离，不自行修公式。High-VAT hub再报同量放大是选择条件人口，不作独立真实风险验证。

§4 synthetic12国家×11domain×scene/action/microvalue形成29,568 datapoints而非独立scene；20,566/9,002 scenario-level split为作者声明，不把条数当独立样本。27annotators评54实例只局部核，neutrality2.97/cultural3.24不认证全文化真值或无害。§5四模型2/4/8-shot及Qwen六SFT/DPO checkpoint不是等预算/KL/能力的算法因果对照。T2 GPT Stimulation gain−.11/−.18/−.14、Security shot非单调，反驳全目标每次提升；tax不是normative harm或谁更安全。§8/Limitations承认受限模型/构念、非长期交互和无acceptability threshold。

2+2+2=6配对多维诊断接口与局部反证 Source PASS，仅精确metric/真实risk强主张保留争议。生成、alignment训练、多维复评、judge与bootstrap都计费；hardware/precision/batch/完整model revision/token/wallclock/SLO/重复seed未披露。必要支持/直接反侧足STOP，不修理论/扩全图；唯一Ch66 actualowner待具体差额或Only，不授Books/DAY。此项后本日必要独核57/57安全终态（含11737/11767/12221中心隔离），不是57正面中心通过或整日完成。
