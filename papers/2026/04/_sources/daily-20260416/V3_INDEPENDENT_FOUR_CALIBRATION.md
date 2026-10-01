# Apr16 首四项有限非作者 source → owner 复核

复核者 apr02；作者 apr03。依据当前 AGENTS 与三合同，复用未变化的合同阅读，并实际对读作者 `v3-reopen-notes.md` 的“首四项必要原文及实际 owner 对读”、四个 exact-v1 必要方法/评价和真实章节。范围仅 13054、13065、13068、13197；未重扫 raw、未写共享 Books、未复现实验。这是单篇准入及采用边界复核，不证明 first-public 日期、来源无遗漏或全日 Gate。

## 2604.13054v1：Ch27 的任务格式 × 内容覆盖，6分缺口深入提案通过

实际必要来源为[官方 v1](https://arxiv.org/html/2604.13054v1) §3–4及 Tables3、7、9。同图像、模型、训练 token/recipe 的 caption–VQA 替换有具体对照，但“格式不提供新知识”不能升级为格式没有能力价值：Table3 的 MMBench .7507→.7000 就是明确退步，均值接近不能遮住任务差异。Pair-caption v2 仍保留原 VQA，不能当全去 VQA 的证明；§4约50B-token分支也不能与§3约100B-token混成同一预算。知识密度来自语义元素分析代理，教师生成/过滤可能同时改变内容、分布与标签质量，不是独立测得知识总量或普遍 scaling 瓶颈。

已实际对读 `TRAIN-DATA` / Ch27 的 mixture、lineage 与 bounded data patch（约132–176），及 Ch23 对齐的交接：既有 patch 要求内容/分布/token匹配，但尚未明确 **同内容覆盖的任务格式变化与内容覆盖变化是不同干预；前者可能不增加事实，却仍改变按任务读取/使用能力**。支持2+2+2=6，缺口深入。建议在 bounded data patch 的格式/语义辨析之后嵌最窄两段：数据 owner 冻结 image/source/teacher lineage，分账 format-only 与内容扩充，训练/Evaluation 按同预算任务切片验收益和回归。不得写 caption 优于 VQA 的普遍演化律；监督格式要求明确、教师可靠性不足时保留原 VQA/静态 mixture。提案通过，尚未实际写后通过。

## 2604.13065v1：Ch66 的可执行文本步骤 × 最终声明，6分缺口深入提案通过

实际必要来源为[官方 v1](https://arxiv.org/html/2604.13065v1) §3–5与 Appendix H 的确定性 Boolean 示例。九运算符、给定 truth table 的任务可用外部 oracle 检查每个文本步骤；Claude depth7 原 cohort 的34错误和新增 seed 的31错误不能混分母。新增会话抽取既有最后计算值的31/31与GPT-4o30/31，支持文本 readout 的局部分离，不证明公开 trace 忠实反映内部计算。ETT改变提示/调用预算、额外约140token；max256截断造成假 collapse 是协议反例，不是开放推理的保证。

已实际顺读 `PLATFORM-EVALUATION-SYSTEM` / Ch66 “Evidence Trail 与最终答案必须分别验收”（约2815–2819）及其前后分账。现有合理轨迹/错误答案与 accepted-subset 合同，没有 **可执行任务里逐步 oracle、最后计算值、最终声明三者分账，以及固定同一 trace 的重新抽取对照** 这一具体诊断。支持2+2+2=6，缺口深入，建议嵌原 Evidence Trail 段、FRS selector分支之前；不另建论文摘要。外部 oracle 拥有正确性，extractor只提出 readout；冻结 trace 再抽取不同于重做题，仍有跨调用/prompt影响与额外成本。只需要终局且没有可执行过程的任务保留 final-only，不能把文本正确推广成内部自知或通用自动纠正。提案通过，尚未写后通过。

## 2604.13197v1：Ch33 的 prefix scorer × 候选 token 更新，6分缺口深入提案通过

实际必要来源为[官方 v1](https://arxiv.org/html/2604.13197v1) §2.2、§3与§4.2–4.3。序列累计 log-ratio 不能唯一识别每个 prefix 的局部价值；IPVRM以归一化 prefix score/BCE和终局 label 训练，score本身不是已校准正确率或step真值。DistRL 对 old-policy 高概率词表候选使用未归一化 value差及标准化局部信号，另保留采样分支 GAE/outcome；未采样候选没有新增实际 rollout 的终局真值。§4.3.3 的2500分支（Qwen3-0.6B）中 prefix value AUROC约.64，而TD与单条终局 label相关仅.0226，作者亦区分局部优化信号与 Monte Carlo长程return。早步/晚步权重目标不同，Table6局部退步、online RM失稳和refresh成本都限制采用。

已实际对读 `TRAIN-GRPO` / Ch33 “Sequence Reward 怎样作用到 Tokens”以及“Policy-implied Value 是 Group Baseline 与 Learned Critic 之间的条件分支”（约237–243），并读 Ch32 prefix value/MC/TD交接。现文 policy-implied value 由当前policy与固定reference构造，不单独训练critic；本项另训练implicit RM，不能偷换成同一无额外模型分支。真实差异是 **完整序列 reward 身份不足以授权 prefix 查询；单独训练的 prefix scorer 与候选词表TD能补局部更新，但不获得反事实终局或无偏长期credit权**。支持2+2+2=6，缺口深入；建议在 policy-implied value 分支后写对照性两段，保留RM/参考/old-policy生命周期、outcome verifier与GAE基线、候选计算及在线漂移成本。不得承诺全部候选更新全面胜出、零RM成本或prefix可自证真值。提案通过，尚未写后通过。

## 2604.13068v1：Ch66 实际已有覆盖，6分标准处置通过

HTML本次不可用，采用[官方 PDF v1](https://arxiv.org/pdf/2604.13068v1)，实际核§3.1–3.6、Tables2–4与§7.1–7.6。552 factual labels/三个数据集、七个117M–7B模型，fold内PCA95%/nested5fold logistic与单L40S48GB/float16限定测量。只有Pythia1.4B与Qwen2.5-7B早峰显著，GPT2XL p=.054、Pythia6.9B几乎平；模型/数据/架构与post-training同时不同，不能声称统一1B阈值或instruction tuning必要因果。Table3部分confidence基线优于probe，不应写内部探针全面胜出。

原文摘要、引言与§7.4报告 probe-direction steering 0% correction；所核方法/结果没有给出足以重建该干预的强度、具体层与干预样本分母，不补造这些字段。§7.4自己列出方向非上游与短1–2token传播受限两种解释：**失败干预既不证明无因果节点，也不证明所有其他干预无效**。因此0%仅作为设置披露不足的作者报告，不作为稳健因果结论或部署纠错性能。

实际 Ch66 “可解码 Failure Direction 不拥有自动纠错权”（约1495–1508）已明确：可预测信息≠独立因果方向，反向steering/erasure不保证修复；probe仅校准风险、abstention/外部验证，correction需独立干预与行为验收；nonlinear/local intervention仍开放但需新证据。这与本项可采用边界完全一致，不只是主题相同。支持作者2+2+2=6的标准审阅 `No Change — Existing Coverage`；不新增Books、不把未披露干预细节冒充已完整核验、不将因果宣传作为正面采用。

## 有限结论

三项6分缺口深入提案通过（Ch27、Ch66、Ch33），一项6分标准已有覆盖通过（Ch66）。正文仍须获得共享写锁、实际落实并接受非作者写后核；本文件不提前宣称 Integrate 或日报 Complete。日期/来源/其他候选由独立日级Gate继续验收。

## 13054 实际写后：非作者通过

apr03获root写锁后实际落实Ch27:178/180及Reviewnote1134。apr02顺读新增两段及相邻bounded patch、静态mixture回退，复用上述未变化的必要exact-v1；正文正确区分格式与内容覆盖两轴，保留格式无新增事实却可改变任务使用、均值接近不能掩盖MMBench/ScreenVIVOv2回归、pair-caption仍留VQA、教师/密度代理与额外成本。没有采用普遍caption优先或VQA无能力价值；位置衔接与受限命题均PASS。可同步该family实际Integrate/写后非作者通过，未复现实验、不代替日期与整日Gate。
## 13054实际正文写后核（root）

root实际顺读Ch27:170–184及原bounded patch/静态mixture交接，复用apr02上述精确来源与采用边界核验。正文分开任务格式与监督语义覆盖，未把example数或teacher语义元素当知识量真值；caption替换VQA的均值近似与MMBench/Screen退步共同保留，内容扩充分支仍保VQA，未写VQA普遍可删。新增生成/过滤/lineage成本与静态mixture回退靠近机制，实际正文在Review notes之前。6分gap深入，实际owner=TRAIN-DATA，写后通过，可同步实际整合；未复现实验，未预支Apr16日级Gate。

## apr02：第二组三项有限 source→owner 非作者复核

此次只审作者已保存的 13627、13556、13519 必要原文和相关实际 owner；不扩大原始池或附件队列，不自行写共享 Books。当前 AGENTS/合同未变，复用同轮完整阅读。

### 13627 LR 与过训练 → TRAIN-PRETRAINING / Ch28：7分缺口深入提案通过

实际读[official exact-v1](https://arxiv.org/html/2604.13627v1) §3.1–3.2、§4必要机制、§5.1–5.2 / Limitations。相同 SFT loss 下不同 LR 可产生不同 MPA / OOD outcome，不代表参数距离已匹配；五条预训练 checkpoint 的 Gaussian扰动→output KL 是 sharpness proxy。WSD cooldown 同期变化未排除因果混杂，作者明确需要修改 annealing 重训才可 claim causality。有限 toy / 1–3B主实验不能升级为统一取消预训练decay的建议。

实际对读 Ch28 LR schedule（约454–471）与分组尺度，Ch29过拟合/遗忘、matching trajectory及optimizer continuity（约578–608）。已有保守LR/retain gate未承载**base预训练cooldown/checkpoint状态与后续SFT step尺度必须联合验收；base loss更低不保证固定SFT recipe更可适配**。支持 Ch28 schedule 中窄补这一交接，保留普通decay的收敛用途、额外checkpoint/扰动评估成本、proxy非决策真值及Ch29 held-out retain验收。3+2+2=7，具体缺口提案非作者 PASS；不采用标题中无条件因果、不认为低LR对所有任务最优，待实际写后。

### 13556 YOCO++ → INFER-KV-CACHE / Ch45：6分缺口深入提案通过

实际读[official exact-v1](https://arxiv.org/html/2604.13556v1) §3.1–3.3 / Eq1–2、§4.1–4.3 / Tables1–2。bottom-half各层先组合底层与本层KV并缓存combined状态，中间层combined缓存由top-half复用；不是Decode各层读多份完整历史KV。保持YOCO初始化、lambda缩放与无key residual消融限定机制；这是从零训练的1.1B/22层架构，不是给既有checkpoint无训练替换。

已顺读 Ch45 uniform cross-layer sharing→token×depth residual（约479–516）与相邻物化/重构链。现有主要是既有模型的近似表示/selector与kernel路径，未明确**由训练架构承担复用质量，并在cache物化之前合成，避免Decode重复读取多个history source**这一替代分支。可窄补到统一跨层共享处，保留传统独立KV、trained-sharing与training-free重构共存；组合算子/Prefill额外读、架构重训及受限质量必须说明。32H800训练/100B SlimPajama、H20 96GB效率实验与不同batch的max throughput不升级为同并发SLO承诺或普遍50%加速。2+2+2=6，提案非作者 PASS，待实际写后。

### 13519 ToolSpec → INFER-SPECULATIVE-DECODING / Ch48：6分缺口深入提案通过

实际读[official exact-v1](https://arxiv.org/html/2604.13519v1) §4.1–4.3、§5/§6.1、AppendixB.2–B.3。schema FSM区分tool-name、parameter-name、free-value和ordinary-text；结构proposal亦需target并行核验，free-value可用TR/历史成功调用的hidden-key检索与suffix continuation。schema只给候选结构，不知参数业务真值，更不拥有执行权限。完整历史答案与当前tenant/policy身份失配仍需限制，不能绕过verifier。

实际对读 Ch48 lexical→semantic store（約448–468）与Agent block hint/read-only action speculation（约642–674）。现有预算hint与retrieval原则没有明确**结构状态选择schema drafter、开放值选择retrieval/general drafter，统一交target验收**的控制分责。建议窄嵌Agent workflow段，避免重复一套安全/工具执行章节；不把FSM等于grammar mask或强制tool选择。AppB.2实际2×A100-PCIE40GB、batch1、torch2.5.1/CUDA12.4/HF，fp16有局部质量差；格式adherence、公开benchmark和headline倍率不证明所有工作负载/并发/生产SLO。2+2+2=6，提案非作者 PASS，待实际正文写后核，不复现实验。

三项通过指必要证据与真实窄gap，不代替Apr16日期/来源/完整分母/日级Gate；尚未凭提案声称Integrate。

## apr02：13977 / 13064 / 13072 有限准入校准

本批只核作者列明的三项题摘/必要消歧与实际相关论点，不重扫 raw，不把主题对应当增量；当前 AGENTS、研究合同和 Report 合同已重新完整读取。

- **13977 FinePhrase：6分缺口深入、Ch27提案 PASS。** 实际核[exact-v1](https://arxiv.org/html/2604.13977v1) §2–5，特别 §4.2 generator×prompt、§4.3 Tables6–8 source/mix 分离、§5 模板与任务切片。复杂 Guided Rewrite 的较大 generator 有收益，其他配置可饱和；混合原始文本在受测格式中优于纯合成，但来源与 mix-in 质量不是同一控制轴。Ch27 当前 Synthetic→persona→recursive corpus（约294–337）已承载 judge blind spot、lineage 与代际混合，却未明确 prompt 要求×generator 能力×source/raw mix 的联合选择及格式执行率≠训练效用。因此支持在 Synthetic 导入后窄补而非摘要归档。固定1.2B/21B-token、64 H100/bf16 的有限对照不能推出通用1B最优；模板多样性只是相关、重复样本补 token 不等唯一数据匹配，额外合成成本与真实数据回退须保留。2+2+2=6、gap 深入，待正文实际写后。
- **13064 Red/Blue Skills：具体前分母关闭 PASS。** 实际核[exact-v1](https://arxiv.org/html/2604.13064v1) §2–3/Tables1–2。26,502快照与11,010随机分类的目标是平台 scan/moderation 标签，非独立核实的恶意执行；输入消融支持文档预测标签，不支持新的生效权限或攻击因果边界。Ch72 当前静态 Policy Facts 及文档/脚本组合 source-to-sink（约1791–1797）、声明与实际行为（约2541）已具体承载拟连接的设计判断。材料新增受限生态描述/已知分类工作点，没有改变该选择；故关闭不是因为安全主题、缺新章或结果有限，也不把平台标签比例采用为市场真实风险。
- **13072 LiveClawBench：具体前分母关闭 PASS。** 实际核[exact-v1](https://arxiv.org/html/2604.13072v1) §3.2–3.5/§5：30case/10domain、状态 outcome rubric、mock与配对构造；未继承后改134case摘要。§3.3只是两匿名模型轨迹示例，没有给所宣称 factor stacking 的受控定量反证；Vue pair 同时变依赖严重度与 browser 验证要求，不自行提升为干净单因子效应。Ch66 mock contract（约884–890）已要求 state-transition/side-effect/failure paths 和真实 integration 验证。这里实际新增 suite 和成熟方法组合，未显示值得改变此长期判断的具体机制/有效性边界；不以所有 benchmark 必须有实验作一般排除规则。

此为一项正向与两项否定的有限非作者校准，不代替日期/来源/整日 Gate。

## apr02：13523 ATLAAS 中央语义保证的有限复核

实际重开[官方 exact-v1](https://arxiv.org/html/2604.13523v1) §3.2 PhaseB/Table2 B5、§3.3、§4.3/Table4，并核 [MLIR arith.trunci / extsi](https://mlir.llvm.org/docs/Dialects/ArithOps/)。B5明确把 extension-after-truncation 认作 saturation/clamp；官方语义却是截高位后 sign-extension：8bit的128→−128、256→0，分别不等clamp到127；overflow标记可产生poison，也不补饱和。§4.3的PE表达式和有限DMA/13目标证明不能补出该模式一般clamp的范围条件。支持作者2+2+2=6深入、**仅B5语义提升保证争议/暂缓**，不否定全部bit-exact证明、opaque回退或有限empirical结果。重开限完整B5 pattern/输入域/比较选择与等价依据或勘误，无需展开整个仓库或所有附录。此为实际必要来源的非作者 PASS，不是新Books采用。

## apr02：13327 / 13847 实际正文写后非作者复核

已实际顺读 Ch49 persistent executor 后两段（约75/77）和 Ch36 token/平方工作代理后两段（约1322/1324），包括前后旧基线、限制与回退；必要官方 exact-v1 再核后，两处写后 **PASS**。

- **13327 Event Tensor：** [官方v1](https://arxiv.org/html/2604.13327v1) §2.1–2.4/§3.1–3.4、§4.3–4.5/Tables2–3支持 symbolic wait-count、top-k/exp_indptr 的数据依赖、static queue 与 centralized dynamic queue 分支。正文正确区别依赖表达/编译责任与 runtime 就绪推进，不把 semaphore 命名成新的内存可见性证明；共同event保守退化、dynamic dense/单token反收益和离线编译107s都没有被 warmup35s 吞掉。与现有 host ring 的差异及 graph/static/独立 kernel 共存成立。
- **13847 SparseBalance：** [官方v1](https://arxiv.org/html/2604.13847v1) §IV-A/B/C Eqs3–10、§V TablesI–IV支持 bottleneck 减 attention budget、非瓶颈增预算，CPU EMA/lookup 再分 DP/microbatch；SAB重排不是DST改变近似计算。正文准确保留 score coverage 非任务质量、空可行集缺 fallback、SAB1.21低于LBB1.23与组合优势、summarization/code/激进预算退步；没有宣称原 objective 不变或总能达到 anchor。固定budget/只重排的回退为平台采用要求，不冒称作者证明已覆盖所有故障。

可将两项同步为真实 Integrate/写后非作者通过；未复现实验、不提前验收 Apr16 日级 Gate。

### apr02：13977 FinePhrase 实际写后非作者复核

已实际顺读 Ch27 Synthetic data 导入后的两段（约296/298）、上游 generator/judge blind spot 与下游 persona supplier lineage。对照本轮已核未变的 [exact-v1](https://arxiv.org/html/2604.13977v1) §2–5，正文联合记录 prompt 要求、generator identity、source partition/raw mixture，分开格式执行率与固定 recipe 的训练效用；复杂改写中较大 generator 的反例、纯合成 NLU 退步、模板相关非因果、同 token 非同 unique-data/总生成成本均在相邻限制中。小生成器与固定 mixture 的旧路径没有被普遍否定，段落未重复成论文摘要。实际写后 **PASS（apr02）**；可同步 Integrate，未复现实验、不代替日级 Gate。

## apr02：第五必要小批四项有限非作者裁决

实际打开四项官方 exact-v1 必要位置、作者记录及相关实际 owner，不展开版本史/全部附录；以下均非日期 Gate。

- **13066 LPC：2+2+2=6，Ch75窄 gap 深入提案 PASS。** [v1](https://arxiv.org/html/2604.13066v1) §3.1–3.6、§4.2/§5.2–5.3、§7区分 non-overlap/meta dictionary 的可重建性、含字典开销的 token 节省与模型实际分析等价。模板测试 per-log exact match 和算法 batch-level Levenshtein 不是同一 estimand；未测目标 analytics，因此解压不能作为理解/分析能力的已证下界。实际 Ch75 Context Compression（约229–249）虽有 task-relative sufficiency、raw fallback/time break-even，尚未承载可逆软件 codec 与模型直接消费编码态的接口区别；Ch78确定性输出重建不是此输入问题。支持在压缩主线窄补字典/tokenizer/batch identity、软件恢复/模型重建/目标任务三项分别验收与 raw/decode fallback；不采用普遍无损理解或API成本直接等比例保证。
- **13108 FAD：2+1+2=5，标准已有覆盖 PASS。** [v1](https://arxiv.org/html/2604.13108v1) §2/§3.1–3.5实读：24导航任务、96格式生成/注错、15 artifact/process任务及7012-session观察。真实可采用命题是 descriptor 降导航成本但不能取代代码事实，staleness导致五任务各组失败、解析成功/静默损坏分开；这些由实际 Ch75 Context Map（约354–358）与 Context Identity、Ch78实际入口/声明分权（约53–57）具体承载。格式无显著差异非格式等价，AutoGen/Curated p=.515非长度因果，post读取/不读取都1.65非阅读干预；不采用开放架构治理或100K+项目未测外推，无需新增正文。
- **13097 ECM：具体前分母关闭 PASS。** [v1](https://arxiv.org/html/2604.13097v1) §6.10/§7.2–7.6/§8实际为诚实manifest假设下规则原型、24模块/500合成chain/24upgrade；不是raw后改摘要的真实ROS盲重构。Ch78 Tool Contract已具体拥有schema之外的version/resources/scopes/recovery与semantic/business验证，Ch26安全commit和embodiment也分开，本文中心为该合同组合的合成示例，未分离新的长期选择条件。Table8 accepted100/fail9与98.2%分母不一致，Behavior/Version消融无变化，不能据此证明全六维必要或98.2%postaccept成功。保留身份/原始证据，关闭不是因论文名或仅缺消融，不新增Books。
- **13088 Token Gradient Cancellation：2+2+2=6，中心普遍保证窄争议/暂缓 PASS。** [v1](https://arxiv.org/html/2604.13088v1) §3.1–3.4、§4.1–4.4、§5–6实际标题与内容匹配，不继承后改IBPO摘要。共享同context-token、centered A与同有效系数可抵消；二阶Fisher局部漂移式不单独证明高频集合reward-irrelevant。Cor3.2 Eq5把共同正c(x)吸收所有方向几何，缺跨输出gradient内积条件：以softmax-logits参数p=(.6,.3,.1)、等权等detached系数的两等回报输出更新g=.5[(e_a−p)+(e_b−p)]，log(p_a/p_b)一阶−.3η而系数差0（数值η=1e−6亦核一致）。一般组内聚合不能直接满足该式；重开限明确允许的更新算子与几何条件。Cor3.3的A=(1,1,−2)、u=(1,3,2)可使A·u=0，仅说明全u相等非必要，**不单凭该例否定作者允许退化例外或zero-measure判断**。stop-gradient改权重的有限配方/匹配rollout与数学代码结果保留，不将所有经验结果或两样本toy否定；不新写普遍熵塌陷因果保证。

### apr02：第二组三项实际写后非作者复核

补充首组写后：实际顺读 Ch33 prefix-value 新段及上下无独立critic分支/Group Size（约244–246）和 Ch66 Evidence Trail 新段及上下 selector 接口（约2825–2827）。13197 明确另训 scorer、终局 verifier 权威、未执行词表无反事实 outcome与在线成本；13065 区分步骤/最终计算值/声明及固定 trace 抽取，保留 cohort 差异、截断与非内部faithfulness。两处与前述已核 exact-v1 必要源一致，实际写后 PASS（apr02），可同步 Integrate；不是全日 Gate。

实际顺读 Ch28 LR schedule 新段及 gradient-clipping 交接（约460–462）、Ch45 跨层共享新段及 runtime residual 交接（约485–487）、Ch48 schema draft 新段及 read-only effect speculation 交接（约658–660）。依据已核未变的 exact-v1 必要原文：13627 明确 cooldown/sharpness 同期只属相关、base checkpoint×SFT 尺度联合验收而非取消 decay；13556 先混合后缓存与上层复用、从零训练而非 checkpoint drop-in、不同 batch 吞吐非同 SLO；13519 FSM 仅选择 proposal，所有结构/值仍经 target 验证且不获工具权限，有限 batch-1/精度边界仍在。三处实际正文写后 PASS（apr02），未复现实验，不预支日级 Gate。
