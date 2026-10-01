# Apr15 三项有限非作者 source → owner 复核

复核者：apr02；作者：apr01。按当前 AGENTS / Research 合同核对必要 exact-v1、真实 Ch66 正文及相邻交接；未写 Books、未复现实验，不代替日期/来源/整日日级 Gate。范围仅 11996、12035、12046，不扩展原始命中或无关附件。

## 2604.11996v1 — FRS

实际独立读[官方 v1](https://arxiv.org/html/2604.11996v1) §3.1–3.3、§4.1–4.3、§5–6及 Phi-4 关键反例。§3.3 的集合是每个 model–benchmark 内汇集每题 16 条采样后做 top-percentile，再分箱抽样 judge，并非每题选择一个答案；摘要/引言的简述不能覆盖这个实际聚合协议。Confidence 是 token 低概率尾部的均值，judge 同时看到题目、完整 response 和 gold；“faithfulness”是文本 rubric，不是内部因果真值。Phi-4 的高分区域可有正确答案与重复退化轨迹，支持过程质量和正确性不能互相代替；不证明该 estimator 或排名普遍适合部署。

已对读 Ch66 “Evidence Trail 与最终答案必须分别验收”（当前约 2811 行）、其前后 runtime identity、exploration/commitment，以及 calibration / selective-risk 分账。现文已区分过程与答案，但未明确 **同一 accepted subset、同一 selector/coverage 上同时计算过程质量和答案正确率，并保留未筛基线**。这是具体测量分母缺口，不是仅因出现新 metric。支持 2+2+2=6、缺口深入及 Ch66 窄整合提案；建议放原 Evidence Trail 段内。固定采样与 judge 身份，计入多样本/标注成本，pooled benchmark 分位数不能冒充线上逐题 selector；不追加榜单或“真实思考质量”保证。来源与 owner 提案非作者通过；实际写后仍需核验。

## 2604.12035v1 — Visual Pruning Calibration

实际独立读[官方 v1](https://arxiv.org/html/2604.12035v1) §3.1–3.3、§4.1–4.8、§5–6。固定 LLaVA-1.5-7B / CLIP 576、greedy 和 prompt，SCOPE alpha 在同路径变化，另有 FastV 两遍执行等不同路径参考；同准确率可伴随不同 ECE，强压缩与跨题库方向并非统一。置信度仅在 yes/no 或 A–D 候选内归一化；15-bin ECE、Brier、AURC测量目标不同。论文没有物理删 token 与 zeroing 的受控对照，不能补造；FastV 跨路径差异也不证明纯 saliency 因果。

对读 Ch66 “Calibration Slice 必须包含 Language × Model Scale × Estimator Contract”（约 1544–1568 行）与 runtime identity；前者没有 input retained-set / selector / implementation path 的具体测量身份。支持 2+2+2=6、缺口深入的最窄分支：视觉 token 筛选改变证据输入，**保留数量和身份、选择器配置、实施路径应与 confidence estimator 共同版本化，在同任务测质量、校准和风险覆盖**。Ch23 继续拥有裁剪机制，Ch66拥有评价身份，不迁移 owner。单模型/两题库、受限 verbalizer、校准集与重复条件限定证据；不规定 coverage 总优，也不把 ECE 改善当事实真值。提案非作者通过；未写 Books。

## 2604.12046v1 — CURE

实际独立读[官方 v1](https://arxiv.org/html/2604.12046v1) §3.1–3.4、§4.1–4.4 / Tables1–2。固定 claim 内容、改 confidence/reasoning 的 DPO 与后续 factual GRPO token mask，是有意义的目标分离；**loss 位置遮罩不隔离共享参数**，不能采用作者“不干扰校准”的保证。Table1 Biography 的 AUROC .688→.676、Brier .266→.268 是明确反例；AUROC 是区分能力，不能替代概率校准。Table2 同时改变优化器、数据与阶段预算，不单独识别顺序因果；文本 validator 不证明内部 faithfulness。

对读 Ch66 “Verbalized Confidence 必须与答案生成解耦并校准相对顺序”（约 3785–3799 行）、“Post-training…改变 Evaluation State”（约 2829 行）及 Atomic Claim / commitment 段。既有解耦与重校准原则尚未说清 **内容优化后的 confidence-preservation 必须再验，序列 mask 不等于函数冻结；筛选 claim 后重新生成的 final response 也需验新增/改写 claim**。支持 2+2+2=6、缺口深入与 Ch66 最小整合，不把全部 SFT/DPO/GRPO recipe写入Ch33。保留事实 verifier、阈值和模型身份、四长事实任务及两模型限制；失败时重新校准、外部证据或 abstain，不承诺自动阻止幻觉。提案非作者通过；实际写后需再核。

## 小批次结论

三项都显示具体主线测量/有效性增量，非泛泛 ROADMAP 映射。必要证据与真实 owner 比较通过；对论文较强宣传已收窄。可各自做最小 Books 增量，但此文件不构成写入完成、first-public 窗口独立证明或整日报 Complete。

## 三项 actual write-after 非作者复核通过

apr01实际写入后，apr02独立顺读三段、相邻交接及对应Review notes；原始证据与命题未变化，复用上述实际必要阅读，不重复遍历附件。

- **12035 / Ch66当前1565行**：Calibration Slice末尾、Atomic Claim之前。保留输入token数量/身份、selector、实施路径和verbalizer，质量与校准共同验收；没有把FastV异路径当纯saliency因果，也没有零化/删除虚构对照。固定模型/两题库/候选内概率、成本与未压缩回退边界均近正文，写后通过。
- **11996 / Ch66当前2817行**：原Evidence Trail论证内部，接Exploration。same accepted subset / selector / coverage及全体基线是实际新增命题；限定pooled model–benchmark百分位与线上逐题不同、文本rubric非内部truth。成本和单回答基线在正文保留，写后通过。
- **12046 / Ch66当前3803行**：原Verbalized Confidence论证后接重复评分。目标/loss位置分离不是函数或共享参数隔离，Biography反例、训练混杂和最终claim保持均实际存在，未照搬作者无干扰宣传。校准/verifier成本与冻结答案路径回退保留，写后通过。

三条实际机制正文及相邻衔接非作者PASS；Review notes可同步“实际写后通过（apr02）”，实验未复现状态保持。此有限PASS不代替Apr15整日来源、日期与准入Gate。

## 追加三项必要来源 → 实际 owner 独立校准

本批只处理 root 指定的 12012、12056、12119；apr02 已确认当前 AGENTS/合同，实际打开各 exact-v1 必要方法、评价及关键反证，并顺读下列真实章节与相邻交接。未写共享 Books、未复现实验，三个提案均仍须作者落笔及实际写后复核，不预称整合或全日通过。

### 2604.12012v1 TIPSv2：Ch23 窄对齐机制，6分缺口深入通过

实际读[官方 v1](https://arxiv.org/html/2604.12012v1) §3.1–3.5、§4.1–4.3 / Tables2–4。学生仍消费 masked view，改变的是 patch-level loss 同时直接监督 visible 与 masked 位置；不能写成取消 input mask。共享 vision encoder、只保留 projector 的 EMA 有外部 contrastive objective 约束这一条件，完全共享 head 的失稳反证保留，不能写成 SSL 普遍不需要 teacher。累积消融不是全因子归因，PASCAL/Normals 切片退步，不采用全面胜出。

已顺读 Ch23 阶段二/四（约53–85）及对齐多目标（约391–413）：已有“全局检索不保证像素定位”的结论，却未解释 **corruption support 与直接 target/loss support 不同；同一表示需按 global 与 patch-local 使用方式分别验收**。支持将这一窄机制嵌入多目标权重之后，而非新增配方摘要。冻结 encoder 的9任务/20数据集、WebLI116M、ViT-g/TPUv5训练及 segmentation 协议限制保留；不将空间 proxy 当物理定位真值。建议2+2+2=6、缺口深入；正文位置与证据范围非作者提案通过。

### 2604.12056v1 LoSA：canonical owner 建议 Ch45，6分缺口深入通过

实际读[官方 v1](https://arxiv.org/html/2604.12056v1) §2.1–2.2、§3、§4.1–4.5、§5.1–5.4。固定 prefix K/V 不等于 query 条件下的 attention output 不变。稳定 query 近似复用 prefix output 与 LSE，active query 各自选取后取 union，再对该共享集合计算；current block dense，首轮 dense 建状态。缓存对象是派生输出/归一化统计，不只是 KV 或索引。§4.4 将完整 B-query union 上界写成 active-count×k 缺条件；只采用 active-subset 的有效 union bound，不保留该错误链。排序、union/gather、额外状态与首轮成本都存在；短 prefix/个别任务退步、受限 attention 微基准不升级端到端生成/SLO。

实际对读 Ch14 FlashAttention/online-softmax（约267–289）和 Ch45“为什么缓存 K/V 而不是 Query”（约36–48）、双向更新/refresh frontier（约737–748）：真实缺口是 **跨 denoising 步 derived-state 的有效性、近似复用和物理读 union 合同**，不是 attention 关系定义。建议唯一 owner `INFER-KV-CACHE` / Ch45，嵌于 refresh-frontier之后；Ch14只交接合并原理，不双写机制。ROADMAP Ch13为 `MODEL-POSITION-ENCODING`，不可按误编号把本项写入 Ch13。建议2+2+2=6、缺口深入，待root最终采用owner与作者写后；不是因已经有KV主题而判Existing。

### 2604.12119v1 Semantic Fixation：Ch66 配对 EvalSpec，6分缺口深入通过

实际读[官方 v1](https://arxiv.org/html/2604.12119v1) §3–8及D.1。同一terminal board配standard/inverse规则，neutral alias与semantic-valence alias改变映射；相同视觉输入不证明每次感知均正确或只有一个内部原因。四合成games/14VLM，closed reduced与open expanded不混分母；same-rule后训练可伤opposite-rule，跨game收益依两种映射训练。late-layer steering依router/donor正确，state-level split减配对泄漏，不证明唯一机制或通用纠偏。

已对读 Ch66 decision-rule/input-estimate/actual-decision（约198）、对象/属性与关系任务（约2936）、label-inversion shortcut清洗（约3058），及Ch23 visual writer/prior reader：当前没有 **固定同一视觉状态，在规则映射、标签熟悉度与semantic valence上交叉配对，分账same/opposite-rule迁移** 的明确测量合同。支持在Ch66原规则/感知/决定分账之后窄补，而非把全部games或steering配方写入Ch23。固定图像仍可能随prompt改变感知计算，descriptive/text-only controls与独立事实witness仍需保留；中性别名不是部署保证。建议2+2+2=6、缺口深入，具体owner与必要来源提案非作者通过。

三项支持保留与窄Books提案；不支持未经写后核就标Integrate，不代替日期/来源/全日独立Gate，不增加附件队列。

### 三项真实正文写后核（root，非报告/正文作者）

apr01落实后三项，root实际顺读Ch23:400–420、Ch45:738–758、Ch66:186–207及证据区，复用上述apr02未变化的精确版本与采用边界核验，三项写后通过。12012在多目标权重之后区分corruption/loss support，保留外部contrastive/head-only EMA条件、局部退步及旧全局方案；12056承接双向refresh，区分immutable KV与query条件派生output/LSE、active union物理读取/首轮成本，拒绝缺桥界，未把微基准升成SLO；12119承接rule/input/decision分账，以同视觉状态×规则×alias作配对诊断，未声称same pixels排除全部感知误差或唯一内部因果。实际机制均在Review notes之前，唯一owner为MULTIMODAL-REPRESENTATION、INFER-KV-CACHE、PLATFORM-EVALUATION-SYSTEM，相邻交接通顺。可同步三项实际整合，不预支Apr15日级Gate；未复现实验。

### PipeLive12171精确PDF与实际Ch52写后核（root）

root实际打开官方PDFv1，核§4/Algorithm1、§5–6、§7.2–7.3的必要机制、设置及Qwen TTFT退步，再对读Ch52的stateful elasticity与相邻Ch51/53责任。旧HTML/缓存文本摘要数字不同，不作为精确v1依据。2+2+2=6，真实gap深入提案通过；随后apr01写入Ch52，root实际顺读352–378的临时current∪target容量、block-address/layerstack、dirtyslot增量patch、finalsync/commit及通信互斥三段，写后通过。正文不以scheduled/applied计数证明完整slot身份，不宣称任意故障恢复、免成本CPU权重或production SLO，保留fixed PP/drain重启/重算分支及profiling目标选择的外部责任。实际owner=INFER-DYNAMO，可同步整合；未复现实验，不替代Apr15日期/来源/日级验收。

### apr02 对追加三项的实际写后确认

apr02 在 Apr16 有限复核期间，实际顺读已写 Ch23:412–414、Ch45:749–751、Ch66:200–202及相邻交接、对应Review notes，复用本文件中自己已实际读取且未变化的12012/12056/12119必要exact-v1。三处分别保留masked-input与loss-support区别/head-only EMA条件，query派生output/LSE和union物理成本，same-pixels×规则×alias的配对身份；没有将局部收益升为全面、exact或唯一因果保证。三项真实机制正文写后均PASS，与root的独立结果一致；未写Books、未复现实验、不代替Apr15日级Gate。

## apr02：SD-Zero / ICL 机制 / REL 有限非作者提案复核

重新读取当前 AGENTS 与研究/报告合同；实际读作者 `V3_EVIDENCE_REVIEW.md` 对应记录、ROADMAP owner、下述原文必要部分和实际章节相邻论证。此次只裁决三项准入与窄增量，不重扫原始身份、版本史或无关附件，不写 Books，不预支日级 Gate。

### 2604.12002v1 SD-Zero → TRAIN-GRPO / Ch33：6分缺口深入提案通过

实际读[官方 exact-v1](https://arxiv.org/html/2604.12002v1) §2.1–2.2 / Eq1–4、§3.2–3.4、§4.1–4.2、C.1–C.2。成功修订过滤保留失败初答作为上下文；Eq2 generation target 是整串 `[初始回答, 修订提示, 修订回答]`，不能省略成仅监督正确修订。第二阶段 teacher 冻结，带完整 student response 与外部 outcome 的特权上下文形成 reverse-KL；epoch 后同步不是无限改进保证。KL 集中及关键词/长度变化不是错误因果定位或内部自知的证明。C.2 比较生成数与估算 completion tokens，不等于 prompt、backward、FLOPs、wall-clock 全匹配；C.1 的采集/过滤数量与训练 retained 数需分开。

已对读 Ch33 Outcome-routed Update / OPSD correct-only compaction（约869–887）和 Teacher Signal（约1926–1940）、Ch34离线偏好交接。前者明确错误轨迹可回 teacher correction，后者要求当前 rollout、版本及归因对照，却没有**先以可靠 outcome 条件修订训练获得 reviser，再将其条件分布监督回当前 generator**的桥。支持在 Teacher Signal 原段局部补这条条件分支，保留外部 verifier 权威、冻结/同步身份、额外 teacher forward/采集成本与离线或有 gold demonstrations 的回退；不强称普通 OPSD 必然纠错。作者有限 Qwen3-4B / Olmo3-7B 数学代码证据与不同阶段预算边界必须邻接正文。2+2+2=6，窄提案非作者 PASS，仍待真实落笔及写后核。

### 2604.12151v1 ICL mechanisms → WORLDVIEW-REPRESENTATION / Ch5：6分缺口深入提案通过

实际读[官方 exact-v1](https://arxiv.org/html/2604.12151v1) Roman III、IV.1–IV.7、V 及相关机制定义。上下文可用于识别已学 Markov 任务并取回参数，也可估计当前序列的统计；Mem 不等逐序列背诵。encoder→pool task-vector→decoder 的 patch 支持所测计算路径，不能证明完整唯一 circuit。动力学竞争与表示压缩两条边界分开；足够 task-vector/decoder 容量时同一 motif 也能泛化，不能把其固化为“记忆头”。

已顺读 Ch5 参数/activation区别、表示为后续计算服务、记忆与泛化非二分（约38–145），以及 Ch18 causal interface 的相邻交接。现有动态表示与共享特征原则未解释**上下文既可提供任务身份，也可提供待估统计量，训练更久在条件设置中能由泛化转向任务记忆，压缩容量又改变同一路径的用途**。支持在记忆/泛化原链内窄补；采用条件化机制，不把浅层有限 stationary Markov / 简化理论的相图阈值搬为 LLM 通用规律，不将局部 patch 或低 training loss 当部署泛化验收。2+1+3=6，具体 gap 提案非作者 PASS；唯一 owner 为 Ch5，不在 Ch18/22重复展开。待实际写后核。

### 2604.12176v1 REL → PLATFORM-EVALUATION-SYSTEM / Ch66：6分缺口深入提案通过

实际读[官方 exact-v1](https://arxiv.org/html/2604.12176v1) §3定义、§4生成规则、§5.1–5.4、§6。输入规模、作者生成器规定的关系 arity、operand识别难度是不同轴；同一 arity 下更大输入可能提供更多线索。回归控制只涉及已测混杂；跨任务不同 accuracy/substructure/recall 不能拼成同一因果曲线。所测模型、合成/多选协议与有限 token/one-shot干预不证明通用失败阈值、内部 capacity 下界或增加任意计算无效。

已对读 Ch66 EvalSpec（约97–108）、完整对象身份及对象/属性与关系任务分账（约2936–2940）和评估预算交接。当前有 slice 与关系任务区别，但缺少**同一生成任务族中交叉控制 entity/input量、关系规则所需联合 operand 数与 operand 识别难度，并冻结 oracle/输出格式/推理预算**的具体诊断合同。建议窄补到 EvalSpec/slice原链，不新增生物/化学知识 owner，不采用作者 RC 标签为模型内在能力量尺或唯一因果；现有简单长度切片仍适合便宜回归，交叉设计新增生成/评分与小切片统计成本。2+2+2=6，限定 measurement 分支提案非作者 PASS，待实际正文与写后核。

三项 PASS 仅指必要证据与实际 owner 缺口提案，不宣称已整合、实验已复现或 Apr15 来源/日期/分母/整体 Gate 已通过。

### apr02：三项实际写后非作者复核

已顺读实际 Ch33 Teacher Signal 新段及前后（约1932–1934）、Ch5 上下文表示新段及交接（约261–263）、Ch66 EvalSpec 新段及后续 calibration（约110–112），复用本节已核未变的 exact-v1 必要证据。12002 保留整串 generation target、外部反馈特权和 completion-token 非总计算匹配；12151 分清任务取回/序列统计及动力学竞争/容量压缩，不作唯一 circuit 或普遍阈值；12176 保留生成器属性与模型容量的区别、交叉控制与受测混杂边界。三处真实正文及相邻衔接写后 PASS（apr02），可以同步实际 Integrate；未复现实验，亦不代表整日 Gate。

## apr02：12216 / 12219 / 12247 / 12254 有限独立裁决

实际打开两篇官方 PDF-v1、另两篇官方 HTML-v1，并对读 Ch72 watermark/provenance（约794–812、2630–2638）、Ch48 proposal/target验收（约34–88）、Ch49 query-risk/Taylor执行（约1026–1032）；不采用受后发正文污染的 HTML，也未重扫原始池或复现实验。

- [12216 TimeMark PDF-v1](https://arxiv.org/pdf/2604.12216v1)：§5.1两阶段 PRF、HSM/审计信任分割与§6.3对应 Eq40/57实际核。6分安全深入、**完美识别/不可伪造保证的窄争议 PASS**：近似独立 Bernoulli 下存在非零错误，800成功/零观察假阳性不能证明任意文本与无限查询完美。保留随机payload与可信key机制线索，不否定全部有限实验；重开需一致概率/信任域范围而非全部附件。Ch72已有sensor与origin交叉验收，不加入法律可采信保证。
- [12219 PASA v1](https://arxiv.org/html/2604.12219v1)：§4.1–4.3及§5必要结果实际核。6分标准 Only PASS：校准prompt平均 velocity差分决定离线步预算、随机路由、grouped一阶统计有具体实现增量，不假称Ch49已有完整算法。有限 Wan2.1/Hunyuan、8H800配置及局部反收益，均值归一化在连续未裁剪预算的恒等式和随机重选不是有限覆盖保证；不采用“观测即严格数学证明”或全指标最优。
- [12247 SpecBound v1](https://arxiv.org/html/2604.12247v1)：§2.1–2.4/Eq5、§3必要配置实际核。6分中心范围深入、**Eq5参数解释的局部争议 PASS**：固定0<α<1、d>0，宽度无界时公式速度趋0，不支持宽度总能改善；原句同时称增加w降低round time与Eq3正斜率冲突。另一方面，未给完整拒绝修正/rollback细节只能写 **exact等价未充分核验**，不能据此断言实现必然不exact；每token算全层也单独不足以证明。工程机制/经验收益保留，重开限参数域与验收协议。
- [12254 SpanKey PDF-v1](https://arxiv.org/pdf/2604.12254v1)：§3几何、§5吸收、§6/Table6拒绝训练与§11威胁实际核。5分安全深入 Only PASS：几何out-of-span能量不推出decision拒绝，correct-key-only吸收与显式deny确有受限反证；C+1拒绝与semantic accuracy分账。已知B的forward-only探测非未知B部署威胁；作者明确不提供密码学保密/不可伪造，不将toy门控代替平台权限。

上述处置只复核必要源/真实owner/中心边界；日期、全分母和日级Gate仍独立验收。未新增共享正文。

## apr02：11838 / 11943 / 12116 / 11867 / 12426 五项 Existing 定点非作者复核

本轮实际读取 Apr15 README §4、作者必要证据记录及以下官方 exact-v1 方法/关键实验，与 ROADMAP 指定 owner 的实际机制正文和相关交接对读；2026-09-27 读取。未重扫原始池、未遍历附件、未复现实验，亦不在本批证明首次公开日期或整日 Gate。五项 **No Change — Existing Coverage 的限定采用命题通过**，不宣称现有章节已经包含五套完整算法。

- **11838 → Ch29**：[官方 v1](https://arxiv.org/html/2604.11838v1) §3、§4.2–4.4 实际核。表示相似性、attention projection 更新量和小幅 layer-swap 结果不能确定知识唯一位置；分段 LoRA 虽声明近似参数匹配，仍不能推出跨模型普遍中层最优。Ch29「Trainable Subspace 也是 Continual SFT 的评估变量」实际正文（约575–582）已要求更新深度、参数集合、optimizer/task order 与拟合/保持/回退分账，Ch30保有rank与参数化成本交接。采用的是 regime-specific 验收，不采用作者强局部化解释或通用只训中层规则；该范围 Existing PASS。
- **11943 → Ch72**：[官方 v1](https://arxiv.org/html/2604.11943v1) §5.1–5.2、§7.1/7.4–7.5 Table4、§8.3 实际核。logit 分类仍需 forward；host-function/WASM 强制经过检查与分类正确性是不同保证，规则前置及privacy boost也使对照并非仅替换读数方式。Ch72「Policy-as-Data」真实控制流（约458–477）已区分 sensor/typed decision 与 deterministic enforcement，Ch78 parse/schema→authorization→execution 保留真实principal。仅这一权限分工 Existing PASS，不假称已有完整bare-metal实现，也不采用零漏报或普遍加速。
- **12116 → Ch66**：[官方 PDF-v1](https://arxiv.org/pdf/2604.12116v1) §3.1–3.5、Table1及§5 实际核文本。行动与文字拒绝不是互补事件；D 未给充分可复算的 joint 指标定义，latest标签不是不可变权重身份。Ch66 risk-tier refusal（约461–465）、Act/Silent/Stop与Tool outcome正文（约553–573）已要求语言信号、实际effect及合法任务完成分账。此 measurement 命题 Existing PASS；不新增D公式、统计独立性或生产模型排名。证据限定三工具、100 prompts、最多两turn、temperature0的作者sandbox，未作PDF视觉版面验收。
- **11867 → Ch66**：[官方 v1](https://arxiv.org/html/2604.11867v1) §3.4、§4.1、§6.2–6.8及§10 实际核。matched judge与输出预算复核撤销headline，100条CV与193新prompt的probe表现不同；chance附近的有限线性probe不能证明表示完全没有正确性信息，原文对截断的因果叙述也不作为采用事实。Ch66实际 matched output event（约319）、格式干预审计（约405）、Self-report/Behavior/Outcome（约641）与Activation Oracle校准（约3165）共同承载接口身份、独立切片和probe权限边界；此窄反证范围 Existing PASS，不假称具备通用disposition训练算法。
- **12426 → Ch5**：[官方 v1](https://arxiv.org/html/2604.12426v1) §2、§3.1–3.3、§4 实际核。patch选择答案翻转而非正确答案；更早读出与跨token计算深度不同，full SFT的较早可读出可同时伴随长链和一般LM退步。Ch5「从可读出到机制」「信息存在、可读与被使用」实际正文（约177–218）及「可读出不等于可拆卸或可控制」（约374）已承载readout→intervention→behavior、跨context限制及诊断不拥有编辑权。该证据阶梯 Existing PASS，不采用CLUTRR有限结果为通用adaptive-depth或线上early-exit规则。

本次没有真实长期机制缺口需要新增 Books；五项判断只覆盖报告明确采用的上述窄命题。新的高强度主张、完整算法或部署收益不在此 PASS 内。Apr15 其他候选、来源/日期和整日完成状态仍由独立日级审计裁决。
