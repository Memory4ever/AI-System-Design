# Jun12 B2：限定必要证据与逐篇交接

作者`supp_jun12`。root已实际校准本批20份exact-v1 AB：18准入，11324/11836贡献前N；本文件不继承旧日报评分/分母，不自签PRE/POST/DAY。18份精确DOI字段见`SUP_DATACITE_EXACT_B2_20261026.jsonl`，每项arxiv.content/findable/唯一v1 Submitted与registered联合界复算均bounded Jun11 BJT、reasons为空；不是created单字段或全球首公开证明。raw日期导航只作路由。

## 12234 — 必要首备直接采用，非第二Methods

当前真实结果：root§16 actualowner/原两段PRE→作者真实SAVE→root唯一§20实际POST通过，实际I生效/窄位释放。不第二Methods。

- 2+2+2=6。作者实际采用root canonical `SUP_REVIEW_20261026.md` §15首次必要包：exact-v1 §3–5的四组base/IT配对、60概念/10类、Mistral生成训练句、100generic prompt/每组合1000输出及temp1/top-p.6/repetition1等；不再重复Methods。SFT toxicity455对与steering356有毒/379无毒分布对、干预层位/pooling/token权限不同，不能授同预算algorithm排名或alignment单因果。
- 采用的具体反侧：外部OLMo2-13B PPL低可为重复、高可为复杂流畅表达；OLMo2-32B-IT judge可把复述prompt误记IF，人审对IF弱于概念/fluency；guardrail造成缺分不能填0。PPL-v-fluency=0、TTR=.81只在48个model×intervention均值/概念再聚合人口，不是逐样本校准，也不授TTR取代judge。注入与toxicity removal目标不同，未核代码/复现。
- **actual owner**：`PLATFORM-EVALUATION-SYSTEM` Ch66。现有“语言控制的代理也要绑定具体行为”把language-ID与relevance/harmonic-mean分开，下一style段处理源意思/风格示例/拷贝；“Metric条件化对象”主要讲语音token PPL与局部声学质量，“quality contract”只定通用代理不替质量。差额是steering非目标语言质量中的重复/复杂风格对PPL双向混杂，以及干预组合均值相关与逐条校准的区分。拟language-control/CLaS完整段marker后、下一“当任务还给出一份要模仿的风格示例…”前，不另开表示干预owner。
- **唯一拟稿，待root actualowner/逐字PRE：**

控制目标之外，输出的流畅、重复与指令遵循也要分别验收。外部语言模型给出的低perplexity可能只是重复片段容易预测，高值也可能来自流畅却较复杂的表达；因此应在同一批原输出上保留目标注入、非目标质量、重复/长度读数和独立标签，而不把一种likelihood直接改名为流畅。更换干预方法、scorer或输出人口后，这份测量资格需要重新核对。

[受限steering审计](https://arxiv.org/html/2606.12234v1)中，judge还会把复述prompt误认成指令遵循；模型×干预组合均值上的相关性，不等逐条输出已校准，词汇多样性较相关也不使它成为通用裁判。应保存原样例、缺分/guardrail、干预层位与训练人口，分别结算生成、外部评分、人工核验和选择费用。指标、标签或非目标质量失准时，保留未干预模型、原输出与独立任务/人工检查，不由更强目标概念或更低PPL签发全面质量与安全。

## 11552 — Teaching Diffusion to Speculate Left-to-Right

- [exact-v1](https://arxiv.org/html/2606.11552v1)实际必要§4、§5.1–5.6、§6.1–6.5；2+2+2=6，标准已完成。没有改评分去适配处置。核心对照：同bidirectional block denoiser的uniform loss→position decay→first argmax-gold error auxiliary CE→jointprefix product surrogate，runtime verifier未改。Gold marginal连乘不是随机p/q接受事件的无条件真实概率；argmax-gold首错也不是所有stochastic verifier的实际第一拒绝。
- §5.1训练四层DFlash、K16、Llama3-8B为主、ShareGPT4096、三epochs、bf16、8H10080G/DP；跨四target六任务。§6.1隔离单项有收益；系数调过峰会退，K32超训练16会退。§6.2换target-regenerated语料的uniform baseline本身2.376→3.914，不能将其64.7%差额归三loss；两数据训练epochs/checkpoint也不同，不拿跨表合成严格同预算因果。§6.4/6.5表明可与tree/streak-distill组合，但收益不证明所有tree verifier已获得概率正确实现。
- 仅在原作者条件报告accepted length与相应throughput；不采统一生产speedup。额外CE/累积算子无新增模型forward不等训练/target data制备/serving全部费用为零；未核代码/未复现。
- **actual Books：已有覆盖**，`INFER-SPECULATIVE-DECODING`，Ch48“这也反向约束drafter training objective”及`semantic-body-binding:SF-2026-ARXIV-2605-18810`当前正文已明确：per-token overlap不足、fixed-position瓶颈会迁移、expected-prefix surrogate按survival/continuation credit分配、只改drafter loss不改target accept/commit，并保后位概率消失、target/temp/K耦合与fullfee。紧接`2610.29013`段已要求target-regenerated CE基线与监督人口分账。11552新增的首错auxiliary和三项layering保留报告为局部训练配方，不再复制一个长期owner或为制造diff写书。root唯一review §9已实际必要/actual owner复核通过，本项NC生效，无Books写入。

## 12412 — Reroute, Don't Remove

当前真实结果：root唯一review §10必要/actualowner/PRE通过→作者按精确肩部真实SAVE两段及trueH2注并读回→root §12唯一实际POST通过，实际I生效/窄位释放。下方唯一稿保留作证据，不是待再写一份。

- [exact-v1](https://arxiv.org/html/2606.12412v1)实际读§4、§5.1–5.2/Tables1–4、A.3–A.4与B.1–B.2。2+2+2=6，actual长期gap需要深入。selected tokens经完整Attn/FFN再scatter回原位；deferred tokens保原hidden走identity bypass，下次路由恢复full候选池而非只保上次selected。不是无损重建、所有层dense运行或跨层旧KV自动可复用。
- 直接反侧：A.4表7 physical-pruning基线均keep-index，避免把重编号损伤误记为routing收益；A.3/B.1相同average-token可有不同层schedule，早路由本身已有大收益，不能将其统归readmission。Nüwa在192/128平均ratio略退，FastV64在HF版基本无恢复；PDrop/VQA也有单任务退步。Qwen3.5仅route其softmax层，linear recurrent-state解释仅假说，非已证因果。
- 效率只到理论预算class与profiler TFLOPs/KV，Table4有额外TFLOPs和PDrop64 KV49.7→51.6MB，不称完全同费或实测wallclock加速；deferred hidden、gather/scatter与KV管理仍付费。无生产batch/concurrency/SLO保证，未核代码/未复现。
- **actual owner**：`MULTIMODAL-REPRESENTATION`，Ch23“固定预算要先分配信息责任，再选择具体Token”。当前DocPrune为一次删选、下一几何分支是merge后复制回网格；均不承载“decoder层间identity bypass、fullpool重新竞争”，不是主题相似当缺口。拟位置：DocPrune段及其`2604.22281`marker后、原“压缩表示还可以只服务其中一类consumer…”恢复网格段前。
- **唯一拟稿，待root必要/PRE及窄授：**

被判低分也不必意味着永久删除。若证据的重要性会随decoder深度改变，可只让本stage选中的视觉tokens经过完整block，再scatter回原位置；未选tokens保留原hidden走identity旁路，到下一路由层重新与完整候选池竞争。它把不可逆删选换成可恢复的计算延后，不是补回已经丢失的信息，也不意味着每层都更新全部表示；原token位置、阶段版本、旁路hidden与active KV的职责必须分别保存。

[有限recoverable-routing对照](https://arxiv.org/html/2606.12412v1)将physical-pruning基线也保留原position indices，支持把重入与重编号损伤分开；更早路由本身会改变结果，单次极限删选和部分强基线/任务仍无收益或反退。同平均active-token或理论预算class不等完全同TFLOPs、总状态内存或墙钟；保留hidden、重复评分、gather/scatter与KV管理全付费。细节、位置/阶段或净预算失配时，保留较宽候选、原keep-index pruning或dense路径，以实际grounding和完整请求回归验收，不由training-free或可重入签无损与SLO。

## 12397 — Redesign MoE Routers with Manifold Power Iteration

当前真实结果：root唯一review §13必要/actualowner/原两段PRE通过→作者按精确Ch21肩部真实SAVE并读回→root §14唯一实际POST通过，实际I生效且窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12397v1)实际读§3、§4.1–4.2、§5.1–5.3、§6；2+2+2=6，actualgap深入。对关联expert weight做一次rWW^T并row-normalize到C，保原Top-k/weightedcombine接口。固定矩阵power-method与§3.3小更新近似不证明训练中移动expert的精确收敛，更不证明非线性expert功能等于top singular direction。本文伪代码的wg shape注释与乘法转置口径不一致，不据其默补完整实现。
- 直接对照：1B多optimizer/100Btokens；3B/11B FineWebEdu350B+midtrain100B。§5.2单normalize无同等quality收益、却有相近balance-loss；移除retraction可不稳。§5.1十次迭代更精确却throughput约减5%、downstream退1.39pt，不能把更贴主方向当单调正确。Table3的11B MBPP45.12→44.87，故非每任务都胜。MaxVio优于balance-loss作为独立读出，但不签dispatch容量或通信SLO。
- 所用C/scale和优化器须共同校准，本文未支持所有expert规模/functional affinity保证。每步全expert矩阵向量及训练回归计费；固定weights时可以load时precompute folded router，动态weight变化须重制。不把局部0.2%训练overhead推广总费，未核artifact/未复现。
- **actual owner**：`MODEL-MOE`，Ch21“Router的tensor shape”已解释g_e/Top-k及独立W_r、nullspace、无参数/子空间/router uncertainty，但没有从expert权重构造router行的耦合。拟位置：`g_e(x)…谁被选中、权重多少、负载怎样`通用段后/原“路由权重还可成为推理节奏…”段前，不接管training runtime/dispatch owner。
- **唯一拟稿，待root必要/PRE及窄授：**

Router行还可以显式依赖它要选择的expert权重，而不总作为独立参数学习：用关联expert矩阵的Gram作用更新路由方向，再把每行收回规定norm，继续执行原Top-k与加权输出。它加入的是router—expert参数耦合；固定矩阵的主奇异方向只是线性权重代理，不是非线性expert的完整语义、最佳token分配或训练中必然精确收敛的证明。norm/scale、expert版本与router artifact应共同验收，固定权重时可预折叠，权重变化后不能继续沿用旧结果。

[受限power-then-retract对照](https://arxiv.org/html/2606.12397v1)中，仅归一化不足同等质量收益，却能改变负载指标；更充分迭代反而降质并增费，个别任务也退步。每步expert矩阵向量、norm约束、校准与训练/负载回归都计费，局部预折叠不使动态制备免费，更不代capacity和dispatch验收。方向代理、数值稳定或净质量费用不合时，保留独立linear router、原均衡约束与dense/shared路径，不由主方向对齐或较低balance loss批准通用正确和SLO。

## 11766 — Fast Speech Foundation Model Distillation Using Interleaved Stacking

当前真实结果：root§17必要/actualowner/原两段PRE→作者真实SAVE→root唯一§20实际POST通过，实际I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.11766v1)必要§3、§4.1–4.4/Table1与中间层消融。2+1+2=5；为actual长期gap深入。第b阶段从bK层每b层取一层复制，紧插其原层之后，使相对层位不被整块末端复制搬移；不保证函数恒等或层语义因果。固定K−1个teacher锚，student受监督索引随b改变，不是每次固定绝对student层号。
- HuBERT94.68M→12层/384宽/FF1536/8head/26.87M，LibriSpeech960h、75epoch、AdamW、batch64、lr5e−4，SUPERB四类任务。EQL/PROP-1及Full/Full-L2L对照：InterleavePROP ASR9.99仍略差Full-L2L9.92；SF F1/不同schedule也非单调。GradStack加hidden监督可退，不能由更多对齐或cosine热图宣告普遍兼容。训练表只给相对训练速度，完整硬件/计时分解Not Disclosed，不转为推理加速或净全链费用。
- **actual owner**：`TRAIN-SFT` Ch29“Distillation不是Teacher越强越好”内，现有共享projector/嵌套mask段后、`2605-17093` binding前。Ch28复制中层成长已承载训练深度变化，不重复该owner；本项差额是成长student与固定teacher层监督的相对位置接口，现有Ch29仅讲固定shape层映射/容量及rollout失配，没有此映射。
- **唯一拟稿，待root必要/actualowner/PRE：**

若student在蒸馏中逐阶段长深，层对应也随拓扑变化，而不只是选哪些固定层加loss。一条分支每阶段复制按当前深度均匀选中的层，并把副本紧插原层之后；teacher中间锚保持固定，student受监督位置则按阶段重新映射，另保最终输出监督。它避免把原晚层整块搬成中层，却不保持原函数，也不由相对位置或表示相似证明层语义相同；复制、映射、projector与阶段预算必须一同保存。

[有限语音蒸馏对照](https://arxiv.org/html/2606.11766v1)支持在所测stacking分支中比较这份映射，不能推成所有任务胜过完整深度训练；部分任务、schedule和中间层监督仍会反退。Teacher forward、多阶段训练、层复制、projector、schedule选择与下游回归全计费，局部训练速度不等推理或全链净加速。层职责、目标支持或质量费用失配时，保留固定深度student、普通输出蒸馏及已验层映射，不从相邻层相似批准任意复制或加深。

## 12280 — Holding the FP8 Quality Ceiling

当前真实结果：root§19实际必要/actual Ch49具体owner复核通过，6分具体已有覆盖生效，无Books写入；下方证据/原proposal保留，不再待独核。

- [exact-v1](https://arxiv.org/html/2606.12280v1)必要§3–7/Table1–3与统计限制。2+2+2=6，标准完成。采用same-seed质量/参考一致性分开、FFN保护的局部消融和无fused INT8 kernel不加速，不采通用consumer优势或“质量等价”。参考FP8而非无公开版BF16；二份独立CFG权重各9.3B、34层/211linears，Qwen3VL encoder/VAE不按本recipe全量化。
- 200非文字prompts与100文字prompts、seed1000、48steps、1024²；bootstrap是在同seed prompts上，不是跨seed等价试验。17层保护cutoff从200评价集中的50子集选，排名虽来自独立8prompt仍有selection/evaluation重叠；四格消融与8→17层膝点仅单次50prompt描述。OCR exact match接近零，NED相对保持不能签文字高质量；CLIP家族judge不代表细字真值。
- 两RTX3090中DiT计算在一卡/VAE另卡，无CPU offload的相应用时；INT8实际约184秒对FP8 172.9，无fused INT8，非算术位宽自动收益；权重18.6GB仍FP8级，FFN保护额外驻留。Q4_K更高Pick/CLIP但像素更偏离reference，Q8_0仅50子集。未核代码/复现。
- **actual Books proposal：具体已有覆盖**，`INFER-TENSORRT-LLM` Ch49“粒度与校准决定谁共享同一份误差预算”已承载校准人口、动态scale和额外热路径；“量化验收不能只看平均分”明确质量/逐例一致性/分布diagnostic各有权限、reference精度和evaluator须绑定；其敏感层局部activation替换/精度保护段已要求实际失败样本与更高位预算分账；“量化为什么不自动带来加速”与Q/DQ/原生kernel段区分低位artifact和真实执行。FFN17层、OCR与FP8参考属本模型recipe/评价反侧，保报告而不再写统一阈值或重复通用门禁。待root实际必要/owner确认NC。

## 11716 — A Fast Locality Simulator for GEMM Design-Space Exploration on Multi-Chiplet GPUs

当前真实结果：root§18必要/actualowner/原两段PRE→作者真实SAVE→root唯一§20实际POST通过，实际I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.11716v1)必要II–IV全核心，2+1+2=5，actualgap深入。functional trace将L2 miss与output write按placement分local/remote；MI300X-like四域、各76CU/8MB16way L2/128Bline、tile128×128×32/BF16，12个Qwen3-30BMoE/Llama3.1-70B FFN fwd/dX/dW。CTA波内K步lockstep，L2可cache remote/local，未建跨interposer之后InfinityCache；因此是跨越量代理，不是DRAM实测或cycle模型。
- 固定4KB RR下，遍历改变privateL2 reuse仍能改变remote bytes；shape有neutral，坏layout/placement可比RR更糟。agent找到的是现成2D swizzle，不采AI发明新kernel能力；CPU9–44秒是模拟器执行，不是GPU GEMM性能。无硬件timing/power验证，lockstep可扰L2命中；不采用90×为推理加速。
- **actual owner**：`INFER-GPU-MEMORY` Ch54“Chiplet Locality需要Layout与Placement共同拥有”。现段写tile连续/placement/CTA affinity，但没有固定placement仍可由CTA traversal改变L2复用与跨片流量，也没有functional模型输出的权限。拟原首段后、原“布局变换减少…”成本段前；不迁移kernel执行owner。
- **唯一拟稿，待root必要/actualowner/PRE：**

即使page placement固定，CTA遍历顺序也可能通过每片私有L2的复用改变跨片流量；只对齐tile与HBM归属，仍不足决定最佳locality。可固定GEMM shape、operand layout、tile与placement，分别比较row/column traversal和二维swizzle，把L2命中、local/remote bytes与最终执行时间分开读出。

[有限functional对照](https://arxiv.org/html/2606.11716v1)显示该旋钮依GEMM而变，部分shape无收益，坏布局还可更差；波内lockstep与cache假设下的流量模型不是实机时延、能耗或全服务加速证明。布局制备、遍历搜索、模拟与真实kernel回归均计费；工作负载、cache或测时不支持时，保留普通统一布局与已验遍历，不用更低remote-byte代理替发布验收。

## 12059 — Attention by Synchronization in Coupled Oscillator Networks

当前真实结果：root§22必要/owner/原两段PRE→作者真实SAVE→root唯一§25实际POST通过，实际I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12059v1)必要§2、§3 Theorem2及直接退化条件、§4.1–4.4/§5。2+1+2=5，actualgap深入；仅固定query物理等衡蓝图。固定训练所得sphere anchors，数字前端从token对产生正couplings；每free oscillator受固定加权anchor sum h驱动，求h/||h||后用shifted-cosine归一读取values，因果分支另限制可见支集。不是普通softmax exact实现，也没有取消数字QK、softplus或全局readout分母；每token对T anchors仍有二次总工作。
- Theorem2仅h≠0且初值非精确反极点；正coupling不能排除相消h=0，small h/近反极初始化会慢。独立uniform anchors的概率命题不等训练后普适保证，本项不采用该概率界。数值RK45 T30/5初值的err<.01比例d2仅84.3%、d32亦98.3%；T5000的98.7%不是all已收敛。物理不同噪声/频率/非理想电路不能从理想ODE直接继承；高维硬件仍open，实际只软件验证，不签能耗/延迟。
- 软件分类仅小模型：KWS d32/2head/1layer，SVA最小容量差额大部分来自softmax1/5训练失败；更大SVA架构都98%。因果LM d128/4head/2layer、WikiText2/TinyStories，d提高仍逊softmax。powerlaw五点拟合非通用budget律，frozenWv/randomphase只支持受测几何分支，不签唯一物理机制。数字前后端、参数制备、等衡时间/读出、训练和回归均付费；未核实现/复现。
- **actual owner**：`MODEL-SELF-ATTENTION` Ch14。现有WTA/spike分支是离散winner、后续signed/solver分支也不承载固定anchor的sphere gradient flow。拟WTA两段及`2604-11321` marker后、原“非负归一化也可以被换成允许相消…”前。不是增加hardware平台owner或写成熟softmax宣传。
- **唯一拟稿，待root必要/actualowner/PRE：**

物理介质若擅长等衡而不擅长指数运算，还可以改变Attention算子本身：把训练所得query anchors固定在球面，由输入相关的正couplings驱动free oscillators，再将它们与anchors的shifted cosine归一成读取权重。训练可直接使用非零加权anchor sum的单位方向，部署蓝图则让理想动力学趋近它；这是另一种受约束的归纳偏置，不是softmax的精确加速。数字匹配、coupling制备与读出归一仍存在，不能把局部无指数改称全链无数字计算。

[有限固定anchor对照](https://arxiv.org/html/2606.12059v1)保留非零驱动力、非反极初值与有限等衡窗口：正coupling也可相消，接近退化位置会变慢。软件验证的语言任务仍逊softmax，高维物理实现、实机能耗和时延尚未成立；小模型与少量seed的取舍不构成通用缩放律。前后端、全部训练、等衡/读出和独立质量回归均计费；数值、物理条件或净预算不合时，保留成熟softmax/数字算子，不由渐近稳定点批准有限时间部署。

## 11864 — CORE-Bench

当前真实结果：root§23必要/owner/原两段PRE→作者真实SAVE→root唯一§25实际POST通过，实际I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.11864v1)必要§3.1–3.3、§4.1–4.7/Tables3/5/6及Limitations，2+1+2=5，为actual长期gap深入。Level2的query匹配pre-PR commit，patch只产生edit qrels不进入检索答案；多快照合并去重corpus在评分时按query commit过滤。Level3从agent browse/relevance ensemble扩支持标签，用edit-only与broader allowlists重跑作utility对照，不使浏览过的内容或模型同意变真值。
- 采用snippet→repo-state下edit/support两种目标与本地distractors的评价人口差，不采新检索架构。Level1/2/3长度、候选库、query与qrel密度不同，下降不能唯一归因跨文件推理或某encoder失效。Qwen3-8B从L1 71.7/96.9到L2 20.3/48.0和L3 34.4/41.5，只是各人口NDCG@10/Recall@100；不能直接算同难度处理效应。rewrite常退、SFT可损L1，popular ecosystem/旧SWE任务人口不代表新仓库freshness。
- labels受agent/三票judge选样和allowlist支持限制，完整软件语义/全部有用context未证；未采用label“准确率”或agent end-to-end成功提升量，不为此展开全附录。query过滤/改写、checkout/AST-chunk/commit过滤、多模型标注与重跑/SFT和回归全计费，在线latency/硬件/precision/SLO Not Disclosed，不外推生产。未核代码/复现。
- **actual owner**：`AGENT-RAG` Ch76“RAG Benchmark的Corpus本身也是实验状态”，当前冻结corpus与变换/标签、下一judged-pool coverage不承载pre-PR query-state过滤及edit/support两种任务。Ch66 APR oracle段诊断builder消费既有证据，不持有检索corpus协议。拟该Ch76首两段及`2605-08838` marker后、原“即使corpus已冻结…”标注池段前。
- **唯一拟稿，待root必要/actualowner/PRE：**

代码检索的评价人口还要从孤立snippet转到请求发生时的仓库。保存query对应的pre-change commit、chunk路径/行span与可见性过滤，分别标记“需要编辑的位置”和“理解改动所需的支持上下文”；两者不是同一相关性。合并多份快照只为节约索引制备时，评分仍须按每个请求的状态过滤，不能让后来的修复或未来文件成为当时可检索答案。

[有限repository检索对照](https://arxiv.org/html/2606.11864v1)显示snippet排名不足以替这两种任务，本地相似distractors与query改写也会改变结果；但跨级长度、语料和标签密度同时变化，不证明某一因素的唯一因果。Agent浏览与模型投票只提议支持标签，allowlist重跑也不证明context完整或真实任务已解决。Checkout、切分/索引、逐query过滤、标注/重跑与独立任务检查全付费；状态、标签或支持覆盖不齐时，保留原仓库回读、lexical/hybrid与Unknown，不由检索均值批准patch正确和生产收益。

## 11673 — Higher-Order Token Interactions via Quantum Attention：中心保证争议

当前真实结果：root唯一§24已独立实际读中心证明与actual owner，原6/中心保证H/Books暂缓安全终态通过；以下原提案保研究依据，不预DAY。

- [exact-v1](https://arxiv.org/html/2606.11673v1)必要§3–5、§5.1 local/all-to-all直接反侧、§7与B.1–B.4。原2+2+2=6不降分，因中心证明问题深入。B.1对象为T^{1,H}_{1,m,1,p}、p-bit、单层、固定k的Match_k存在匹配族，mHp=o(N/loglogN)渐近；不把n12实测parity失败当它的有限尺度推论。B.2所构造却是fixed-support monomial/parity；“Combined with Lemma1”未给从Match_k难到这个monomial族难的桥，故不采用其总表达分离结论。
- B.3把generalization gap上界随norm变大，当作无法泛化的下界；宽松上界不证明失败，更不能由量子表达存在直接推出少量样本学习保证。这是原证明逻辑缺口，不是缺代码或所有量子研究无效。B.2先称RZ angles可载basis bits，与§3的H|0>后RZ等幅态不一致；后文scope承认basis-loading witness与受测reupload encoder不相同，保留这份身份区别而不把gate-set witness当已实现benchmark电路。
- 可保留作者有限parity实验和模型/预算/拓扑反侧：n12、QHA296参数与标准head1922非strict等参数；Table3另tinyMLP302/HOT634/HOFM595等存在不同成功/失败，少参数非总费；经典HOFM/MLP能表示并学习高阶，不是quantum-only能力。local2design/logdepth/1localcost的无barren-plateau定理不授all-to-all RZZ，后者gradient实测指数衰减，ring较稳却丢高阶，butterfly为有限拟合。CPU statevector/shot/depolarizing代价不等量子加速，未核代码/硬件复现；不采用科学应用部分。
- **actual Books proposal：暂缓中心表达/泛化保证，不写通用警告凑I。** Ch15当前direct-sum/算术电路下界已明确计算模型/有限精度/最坏情形与真实学习不同，Ch14已有替代token mixer的独立质量/执行验收；本项新formal separation桥未闭合。报告保有限设计与empirical反侧，未给全局原定理或新可验证长期接口前不进Books。重开条件为同一函数族的明确reduction/反例处理、与宣称电路一致的输入编码及正确的学习下界或收窄定理；只重开这几处，不无限查全部引用。待root实际独立核争议/终态，未预签H或DAY。

## 12109 — InDex

当前真实结果：root§28必要/owner/原两段PRE→作者真实SAVE→root唯一§30实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12109v1)实际必要§3.1–3.4、4.1–4.6/Tables1–4、5限制。2+2+2=6，为actualgap深入。不是摘要所暗示上层只吐scalar：§3.3将terminal projection从1扩为6DoF coarse hand joints，LoRA仅action-expert selfattention、VLM冻结，loss监督arm与coarse q_hand；再用FK thumb-tip到其余指尖centroid的aperture按dmin/dmax压成gamma。stage2冻结VLA，以visual/proprio/gamma训练独立diffusion head，不给γ真实意图或接触充分性。
- robosuite GR1固定底座/FDH6、双视图、20Hz同步示教，四任务各100成功demo/100trials、episode500步；双RTX4090、stage1 BF16/30k steps/r16α32，obs4/pred12/exec8。只受测仿真，真实部署/双手futurework；不采millisecond/hardware-agnostic/消除catastrophic forgetting普遍保证。冻结权重不等全部旧行为已回归，stage1仍改action expert。主Table2与direct-projection Table3/4基线明显不同，不合并为唯一效应；coupled/no-intent/MLP逐项比较支持recipe但未验梯度冲突唯一因果。SR_grasp定义conditional，不把reach/grasp/task三个百分数默当同分母乘积。
- 直接反侧：Nut Assembly仍停滞/hover；gamma压缩可alias不同接触，未做所有手型迁移/真实控制安全。FK标定、全部示教/两阶段训练、VLA特征与DDIM解码/反馈回归全计费；无完整latency/total训练budget，不授净加速。未核实现/复现。
- **actual owner**：`MULTIMODAL-EMBODIED-VLA` Ch26，现有cross-embodiment latent-goal/forward-model段让目标本体规划futurestate；多指contact-retarget段迁移指面接触时序，都非本项粗关节→aperture proxy→另训dex head接口。拟`2605-20811:end`完整binding后、原“视频示教的目标也不必全部恢复…”前。仅作更窄的动作接口分支，不声称标量能代完整接触。
- **唯一拟稿，待root必要/actualowner/PRE：**

从夹爪先验适配多指手时，也可先保留一份较窄的抓握条件，而不让同一大骨干直接承担全部精细关节控制。一条分支先适配action expert输出粗手部关节与arm轨迹，再通过目标手的forward kinematics把thumb与其余指尖间的aperture归一成标量；第二阶段冻结该VLA，用它的视觉特征、当前关节与标量条件训练独立diffusion head。这个量是受本体标定的proxy，不是真实意图或接触充分状态，相同aperture仍可对应不同抓持。

[有限InDex仿真对照](https://arxiv.org/html/2606.12109v1)支持比较这份两阶段接口，却没有证明所有旧能力保留、梯度冲突唯一因果或任意手型可迁移；紧装配仍会停滞，真实部署尚待验证。FK/开合标定、目标本体示教、两阶段训练、特征与动作生成和闭环回归均付费，冻结上层不使下层适配免费。接触、代理或控制时序失配时，保留目标手示教、显式接触/几何与已验controller，不由标量条件或较高仿真成功批准物理执行安全。

## 11585 — Kuramoto Attention: Synchronizing Self-Attention on the Torus

当前真实结果：root§29必要/owner/原两段PRE→作者真实SAVE→root唯一§30实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.11585v1)实际必要§2、§3.1–3.5/Prop1–2/Lemma3、§4/Table1–2、Limitations/AppA。2+1+2=5，actualgap深入。hidden坐标为角、positive cosine gates经causal softmax选邻居；values是raw phases的复phasor，不经denseWv/Wo；weighted circular mean的tangent方向恒等于sum A sin(phase差)，再乘signed value gate/bound，可吸引也可排斥。身份仅未变换phase-values，不能推广普通projectedvalue；仍有softmax和densegates，不是12059固定anchor/无指数物理等衡。
- Lemma3只freeze A时的局部coherence方向，不是整个state-dependent层固定energy下降，更无全局同步/不collapse保证。SwiGLU读取rawangles而非cos/sin，会区分θ与θ+2π，故全block不是严格torus函数；不采用完整geometry-native或拓展任意compactgroup已验。门控局部近似metric不当成全局输入不变真值。
- enwiki8 char90/5/5、seq256、4layer、50epoch、AdamW1e−3/batch64，五seeds，bestval epoch；参数约±3%匹配但width176vs120/400vs276、一个phase用2components，不称同算力。1M均逊、5Mmedian近但mean与方差逊，一seed落后不能丢掉重启；移去FFN/换densevalue/untiegates都退，局部order参数近1非所有token全球collapse。无速度优势/硬件precision总费ND；三角函数、softmax/densegate/FFN、全部训练与回归付费。未核代码/复现。
- **actual owner**：`MODEL-SELF-ATTENTION` Ch14。现有非负/有符号聚合、coherence局部动力学段均未让hidden直接为phase并改变value-path的加法/乘法职责。拟原`2602-05230` signed归一完整段后、原“是否归一为概率…”query幅值段前；与12059另肩部不冲突，不把同Kuramoto名当同机制。
- **唯一拟稿，待root必要/actualowner/PRE：**

另一种算子选择保留softmax，却把hidden坐标变成相位：用门控cosine选择过去tokens，再直接聚合其原始phasors，将圆周均值的切向分量作为相位更新。只有这种identity-value接口，方向才等于所选邻居相位差的正弦耦合；signed gate还可排斥而不总吸引。Dense gates决定每坐标的乘法强度，跨坐标的加法混合交给FFN，不能把去掉Wv/Wo解释为没有跨坐标计算或所有普通Attention已等同同步器。

[有限torus语言模型对照](https://arxiv.org/html/2606.11585v1)仅支持受测小规模字符任务；固定Attention权重时的局部coherence解释不授整个自适应层能量下降，全block的raw-angle FFN也不严格保持相位代表元不变。参数近似匹配不等同算力，较小模型及均值/方差仍逊参考，且无速度优势。三角函数、softmax、dense gates/FFN、训练和回归全计费；周期表示、质量或净预算不合时，保留普通Q/K/V与已验softmax，不由同步几何签发全局收敛、能力或部署优势。

## 12263 — Void

当前真实结果：root§31必要/owner/原稿PRE→作者真实SAVE→root唯一§34实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12263v1)实际必要§3 threat、§4直接反侧、§5.1–5.4/Eq5–9/Algorithm1、§6.1/6.6–6.7/Table10–11、7.2/Ethics、AppC/D。2+2+2=6，安全与actualgap深入。数据owner仅在发布前改像素，不改模型；本地SD1.5 surrogate提高VAE posterior std之和，并压shadow-caption条件/无条件噪声预测差的跨元素std，JND mask与linf限制视觉改动。是两个可优化代理与受限输入防护，不是intrinsic stochasticity不可消除的证明；std(v)=0仍容非零常量向量，故Eq7不独证CFG向量消失/无语义方向。前文Table1 Lipschitz估计与有限相似度不能证明所有mean encoder收缩/语义抹除。
- 同budget8/255/1000steps、保护float32/攻击mixed precision、主RTX4090，单A100作部分cost/holistic adaptive；五datasets/训练与推理mimicry多分支，不把FID/CLIP当身份授权或隐私真值。Table10加GSC对surrogate effectiveness降但transfer/robustness改善，mask再降raw strength换utility，非各模块一概单调提升；超过中度lambda也会抑制效果。JND/PSNR/LPIPS无human-subject试验，不授人类绝对不可见或所有合法用途无损。
- AppD强适应者用protected图重建，fine-tune整个VAE/UNet，t600/15unroll+KL pullposterior：Table11 FID下降/CLIP回升，是明确保护削弱，约79GB/2h是该攻击配置，非成本下界或未来不可突破。Ethics明确非绝对防护/未来adaptive可弱化，不采正文“所有mimicry都会失败”。仅图像LDM，其他模态未验；全surrogate/BLIP/双噪声预测与梯度、mask/候选选择、回归均付费。TPOS文字维护分区optima但伪码仅一个delta*，不照抄literal选择recipe。未核代码/复现、未读图像素，不采用输出可用性独立人审结论。
- **actual owner**：`PLATFORM-SECURITY` Ch72“生命周期威胁”。现有data poisoning与内部安全修复段关注被保护模型/参数；不存在发布图像作为防护artifact、VAE uncertainty/CFG双代理与未来训练/编辑威胁这一边界。拟该H2图示后“单一WAF无法覆盖…”完整通用段后、现训练containment分支前；不把diffusion基础公式迁至此owner。
- **唯一拟稿，待root必要/actualowner/PRE：**

公开图像还可以自身携带一层受限防护，而不要求随后训练或编辑它的人遵守本地API策略。一条分支在本地生成模型上优化微扰：提高VAE后验的预测不确定性，并以代理caption下条件/无条件噪声预测差的离散程度为另一目标，另受像素预算与感知mask约束。防护artifact是发布后的图像及制备版本，不是模型权重或授权令牌；提高variance不证明噪声不可被移除，压低跨元素std也不独证guidance向量为零。

[有限Void攻防对照](https://arxiv.org/html/2606.12263v1)显示局部保护、视觉效用与跨模型适应有取舍，完整管线适应训练也能改善重建指标；FID/相似度与感知代理不能代身份隐私或真人不可见证明。Surrogate、caption、双分支梯度、mask/候选选择及全部适应回归均计费，单次高攻击费用不是安全下界。模型、图像变换、合法效用或适应者越出支持时，收窄保护声明、重新验收或不发布，并保留consent、provenance与平台访问控制，不以输入微扰批准永久防盗用。

## 12236 — DrivingAgent

当前真实结果：root§32必要/owner/原稿PRE→作者真实SAVE→root唯一§35实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12236v1)实际必要§3.1/3.2完整机制、§4.1–4.4/Table1–2/§5，2+2+2=6，长期执行接口gap深入。Design Agent离线提出attachment/cache fields/supervision，过代码检查、轻probe及训练gate后产tool profile；不是代码生成自己认证可用。Profile绑定输入输出、validity、执行模式和latency/checkpoint，运行时LLM只提Reuse/Refresh/Skip计划；逐帧确定路径另验cache/输入/预算，异步refresh仅作用未来frame。关键是sensor timestamp为event-time，不按慢replay墙钟把旧结果洗成新状态；stale/no-pending/background上限约束LLM调用，不逐帧询问。
- GRPO短H-frame rollout以signed quality减zero-shot anchors的上包络参考线，FPS先clip校准区间；FPS是H/预定模块compute latency之和，不是sensor帧率、全链wallclock或harddeadline。可选frozen scorer未用时β0；仅重排schema-valid计划概率，不改变validity规则。A100/float未量化，scheduler Qwen3.5-.8B训练8H100约16h；nuScenes open-loop L2/碰撞与Bench2Drive闭环仿真分别验收，不授实车安全。Table1有adapter L2比baseline更差而碰撞更低，不概括每指标全胜；Table2 dense reward稳定性.168→.172并非单调改善，calculator后.074仍高于deterministic .037/.043。Communication local ports延迟明确未计，data loading亦未入theoretical compute；不可用2/5/8FPS意图宣称满足总SLO。未取图曲线精确数、未核实现/复现。
- **actual owner**：`AGENT-PLATFORM` Ch84“Serving结束不等于Agent任务结束”。现有Nalar future/周期全局policy→事件局部执行持有placement与metadata一致性，但不承载连续sensor event-time、未来帧plan activation与cache freshness；Ch81调度证据顺序是不同问题。拟Nalar完整两段/2601-05109 marker后、client接口段前，不迁Serving scheduler owner。
- **唯一拟稿，待root必要/actualowner/PRE：**

持续消费传感序列时，调度计划还要区分event-time与运行墙钟：慢速回放不应让旧输出重新取得fresh资格。可把模块输入输出、cache有效条件与执行费用写入profile，让模型只提出reuse、refresh或skip，逐帧执行器再核当前输入与预算；异步刷新完成后仅更新合资格的未来帧，不反写已经作出的控制决定。模型计划与确定性准入分开，且刷新缓存不增加真实观察帧率。

[受限DrivingAgent原型](https://arxiv.org/html/2606.12236v1)支持这种多速率接口，LLM调用还受staleness、pending与后台上限限制；其理论compute FPS不包含模块通信等全链费用，也不是实车deadline或安全证明。Profile制备/训练、LLM、cache驻留、刷新与真实反馈回归都付费，dense reward也未令所有稳定性读数单调改善。时间身份、输入有效性或净预算不合时，保留固定频率/已有计划与已验controller，拒绝无效reuse或跳过可选模块，不由平均吞吐批准动作提交。

## 11792 — MultiToP

当前真实结果：root§33必要/owner/原稿PRE→作者真实SAVE→root唯一§35实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.11792v1)实际必要§3.1–3.3/Eq2–18、§4.1–4.5/Table1–6、AppA/直接B1/B2反侧。2+2+2=6，具体接口gap深入。冻结VideoLMM，patcher读取video+question，以局部/全局半hidden预测每视觉token keep/replace；所有被替位置共享同一由视觉均值+context residual生成的patch token，数量/文字保持，不是减少token或恢复丢失证据。训练CE gold answer经STE Gumbel二值前向，另从原backbone gold-answer→visual attention的中层.25–.75、每帧top32均值产生相对rank；这是模型/答案条件代理，不是真实可靠性标签。ρ均方惩罚为软比例目标，不是hard精确上限；部署只用video/question，不读gold answer或teacher图。
- 随机3k LLaVA-Hound、2epochs/AdamW1e-5、batch1×accum4、8A6000 48GB；VideoLLaVA8frames，Qwen训练16frame/推理default不同，512/1024生成上限依benchmark，不拼统一population。ρ/.rank/TopK/.sparse均有过强反退，no-rank56.35仍高于vanilla47.69，不能称全部收益来自rank；AppB2 VideoMMMU comprehension11.67→11.33与Qwen adaptation31→29反退，不采完全保持能力。Table5 Vript平均s/generated-token3.37e-2→3.39e-2、显存15.74→16.52GB，Qwen亦增，非“零开销”或全链request SLO。Qwen DeepStack适配另将lowres mask扩为merge-group highres replacement，再走原vision path，不能假定任何模型只在LLM输入贴token即兼容。未核完整生成例/图像素/代码/复现；多seed/CI未披露。
- **actual owner**：`MULTIMODAL-REPRESENTATION` Ch23。既有DocPrune与recoverable routing持有删选/延后计算，RVE持有head attention重加权，不持有保留位置而以同context全局token替换局部内容、训练期answer-conditioned排序撤除的接口。拟Reroute两段及2606-12412 marker后、恢复grid段前；不将其作为压缩加速或安全过滤器。
- **唯一拟稿，待root必要/actualowner/PRE：**

视觉token也可以保留位置和总数，却替换部分内容，而不永久删除或只延后计算：由视频与当前问题生成keep/replace提案，再让被选位置共享一个“视觉均值加context残差”的全局patch token。可冻结原消费者，以真实训练答案的预测loss适配这层接口；训练时答案到视觉的attention还可提供帧间替换倾向排序，但这种代理不拥有局部证据真值，部署不再读取答案或teacher热图。

[MultiToP的有限对照](https://arxiv.org/html/2606.11792v1)仅支持受测视频/问题人口，软替换比例不是精确硬预算，过强替换/排序约束及部分理解切片仍退步。共享token会丢弃局部区别，保持token数或冻结主干不认证信息无损；不同merger/DeepStack路径还须保持特征兼容。全视觉编码、patcher、teacher取图/训练与新旧任务回归均计费，平均每生成token近似延迟不签完整请求SLO。细节、接口或净质量失配时，缩小替换并回原视频tokens、外部grounding与独立答案核验，不把较低幻觉代理升级为事实或安全保证。

## 12403 — World Pilot

当前真实结果：root§36必要/owner/原稿PRE→作者真实SAVE→root唯一§39实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12403v1)实际必要§3.1–3.4/Eq1–6、§4.1–4.3/Table1–6、§5。2+2+2=6，预测condition消费gap深入。冻结WAM同当前obs/instruction产生future latent与coarse trajectory；latent经投影/未来tag以residual crossattn写入VLM hidden，trajectory resample后压单prefix token供action generator，不替初始flow noise/不逐步锁定轨迹。VLA/VLM/fusion/actionhead均训练，WAM冻结并训练可预计算，但eval每决策仍在线额外forward；这不是完整policy不训练或免费未来。clean-action flow损失按velocity重参数权重，不采用未披露endpoint数值recipe。
- ABotM0/Qwen3VL/DiT与CosmosPolicy5denoise，8RTX PRO6000/prior dropout.3。LIBERO train→LIBEROPlus10030扰动7轴，三seed Total84.7；Robot60.6<ABot67.9、Layout80.5<82.6，原LIBERO98.5<98.6，RoboCasa65.5<Cosmos67.1，不能称每population更强。部分baseline引自论文、部分rerun，非所有同budget；Language列高值偏“不响应instruction扰动”，不直接授更懂语言。真机四任务每100ID demo/10k matchedsteps/每setting20trials，同臂/RGB，个别<10点差不作确定排序；所有OOD仍比ID降10–20。
- 直接消融：LS83.7、AS83.1、两者84.7；CosmosPredict无action后训仍有LS收益，不证明唯一动力学因果。latent1/3/5步84.6/84.5/84.7，decodedfuture83.5；singletrajectory token84.7、perstep83.6、flowinit84.1、raw83，支持受测接口偏置，不授所有latent优于pixel/单token普适最佳。共同错误WAM prior会被policy消费，§5明确WAM覆盖外收益缩小、高频因额外前向受限；future模型输出不是真实观测，未核代码/复现或全图像素。
- **actual owner**：`MULTIMODAL-EMBODIED-VLA` Ch26。现有2605-07931未来单token是joint latent/action flow；几何encoder/FiLM是当前几何条件，不持有冻结WAM的scene-latent residual注入与trajectory prefix两路径，以及guidance vs初始化的分责。拟2605-07931完整段marker后、原“部署几何预测…”前，不新增world-model owner或替基础生成解释。
- **唯一拟稿，待root必要/actualowner/PRE：**

外部world-action model还可以同时提供两类可错prior，而不让生成未来直接取得控制权：将scene-evolution latent投影后以residual cross-attention补入VLM状态，另把粗trajectory压成一个action-generator prefix。后者是整体运动提示，不是每步目标、真实未来或flow初态；训练可以冻结prior生产者，却仍适配VLA与fusion，部署每个决策也继续支付生产prior的前向。

[World Pilot的受限对照](https://arxiv.org/html/2606.12403v1)支持分开比较latent/pixel与trajectory条件形式，但单token、少量去噪步和双路径只在受测人口有优势；部分本体/布局及原任务仍退步，WAM覆盖外两prior会一起失准。Teacher/WAM、在线预测、融合与动作训练、全部真机/新旧任务回归均计费，不由冻结或预计算训练条件报价为免费实时。Prior、场景或control预算失配时，保留原观察/policy、较短chunk重观测和独立controller/停机接管，不把更高OOD均值替代实际环境反馈或物理安全。

## 12372 — UniIntervene

当前真实结果：root§37必要/owner/原稿PRE→作者真实SAVE→root唯一§39实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12372v1)实际必要§3.1–3.4/Eq1–8、§4/Tables1–2、§6，及直接采用所需AppB/C1/D/E/F/G/H。2+2+2=6，恢复接口gap深入。Qwen3VL2B LoRA以当前obs/instruction/action预测VJEPA2 nextlatent，再由twinmin head拟合离线proxy价值；K8趋势shortfall与离成功的距离提供trigger代理。Offline proxy先在成功/失败rollouts训练并freeze，成功轨迹按t/(T−1)标progress、失败全0，不是真实连续物理进展。历史减值项未作正部，可互相抵消；sigmoid(.5)门和额外mined focalhead不是严格统一可执行recipe，本项不采其阈值校准保证。
- Memory从同一proxy高增长片段筛120/240目标，taskrouter再cosine top1；goal是过去高proxy endpoint，不是当前必可达或安全目标。BC/FAST产生H8/7D纠正chunk，不直接重放旧轨迹。Table6 retrieval仅trainingrollout回读、cosine高与proxy value lift非独立正确率。AppF表/图Fold候选3574/3973差异不抹平，不采用精确memory构建计数recipe。
- UR7e/平行夹爪/双校准224RGB/SpaceMouse、五桌面任务，20evalepisodes/task，IR为三trainingruns中人工接管steps/总交互steps，不是次数、人工总时长或无人工。Table1平均SR81→88是7pp/约8.6%relative，IR34.3→14.6约57%relative，不错写8.6pp；比π0.5 pick任务仅tie95非全优。两任务消融中noMemory与完整模型offlineF1均.882而SR95→85，说明trigger分类不能替recovery成功；noFuture SR90、noTVR/NoValue更差，模块收益人口有限。FA-RL触发/恢复backbone不同且其低F1不证所有failure预测不行。人类仍处理罕见unsafe/OOD，camera/hardware相同不保证所有监督/计算等预算；bf16/30epochs/额外proxy和VJEPA训练/rollouts全费，GPU与端到端deadline未在所采用setup披露。未核代码/复现或视频图像素。v1 HTML封面Aug24与页眉Jun10不同，仅原精确版本当前内容，不补历史字节证明或迁归属。
- **actual owner**：`MULTIMODAL-EMBODIED-VLA` Ch26 Fleet循环。现通用部署—干预—再部署与2603-09121最后人工后缀持有人类纠正数据人口；IG-RFT仅阶段探索noise，不持有learned停滞trigger和memory goal→独立recovery proposal。拟Fleet通用图和分责段/`SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL` marker后、原人工后缀段前。不是RAG/Memory数据存储owner。
- **唯一拟稿，待root必要/actualowner/PRE：**

接管触发还可以从“已经失败”移到“持续不再取得进展”，但两者不能混作物理风险。可用当前动作的预测latent估计离线proxy价值，再从短窗价值变化提出是否干预；触发后，从以往恢复片段选择高proxy目标，由goal-conditioned policy重新生成当前状态到目标的纠正chunk，而不直接重放过去动作。价值、目标检索和动作生成是三个可错接口，筛出的高价值endpoint也不证明现在可达。

[UniIntervene的有限真机对照](https://arxiv.org/html/2606.12372v1)中，移除memory目标几乎不改离线trigger F1，却降低在线成功，说明检测好不等恢复好。成功轨迹时间进度、模型价值与training-rollout相似度都不代真实任务或安全标签；人工接管step比例下降也不等无需监护或总人工费用同幅降低。Proxy/未来encoder、memory筛选、恢复训练、全部rollout和回归均计费；价值失准、目标越出支持或净预算不合时，保留原policy、固定检查与人工接管，独立controller和safety monitor继续持有动作veto。

## 12365 — Ambient Diffusion Policy

当前真实结果：root§38必要/owner/原稿PRE→作者真实SAVE→root唯一§39实际POST通过，I生效/窄位释放。

- [exact-v1](https://arxiv.org/html/2606.12365v1)实际必要§3.1–3.3、§4/§5定理假设及采用边界、§6完整sampler、§7.1–7.5/Table1–3、§8/9，AppF setup与直接D PSD说明；不采用全理论式/完整AppA证明、可选VP Ambient loss或未实测rejection variant。2+2+2=6，数据训练接口gap深入。先分target P/suboptimal Q，采uniform diffusion time后只从该time合资格集合抽data；P全time，Q按高噪或低噪区间使用。classifier可定tmin，tmax本文未用classifier自动定，sweep亦是实际付费路线；不是单一全time downweight，也不改推理policy sampler。
- 高噪相近/低噪局部是要检验的具体条件：Gaussian零均值stationary/低频一致与power-tail的定理不授自然机器人全分布；谱拟合还用action归一、10Hz/horizon100及OXE重采样/低频加速，不能由直线图证所有actions天然分层。classifier“分不清”依赖校准/分布/无observation shift，§9明确未解决观察域移。§7.4文字tmin=0与§6 union rule下“只Q低噪”的设定不闭：取0会使(0,T]全合法；仅采局部noise资格设计，不照抄该literal开关或宣称完整recipe无矛盾。
- 四受控人口：maze50P/5000Q、NMP100k/1MQ、push50/2000、sorting50/200反向logic；maze/filter与co-train成功近同但smooth不同，NMP Ambient比filter更不smooth、push加low-noise 92<perpoint93.5、sorting logic98.2<filter98.6，不能称所有指标全优。sim-and-target作sim-real proxy不代全部真实域移；sorting四block/episode的约800块非800独立episodes。OXE table50/150target、tower35target；Q MS++27/COXE48datasets约1.28/1.40M，20trial/policy，table完成rubric与tower高度不同，33%是tower相对高度不是通用success涨幅。target更足时low-noise可无益/有害，unweighted co-train因unsafe未硬件测，不填0或假等budget。
- AppF各baseline扫超参/每run保存5–10checkpoint报best，CP区间为二元trial而非training-seed不确定性；训练GPU/precision与总SLO未在采用setup披露，不采效率量。Classifier未总胜costly sweep；更多Q训练比filter贵，P/Q划分人工决定/非无条件任意source。所有造数/分类与搜索/更大训练/硬件回归计费，未核代码/复现/图像素，不签物理安全。
- **actual owner**：`MULTIMODAL-EMBODIED-VLA` Ch26 action-diffusion。现2606-05737改训练time密度偏噪端以支持一步推理，而本项按time改可用数据人口，不持有同一Q只借local/global之一的接口；次优示教质量段仅权重/过滤/tag粒度。拟2606-05737完整段及marker后、原“减少actiondecoder步数也可以…”前，不将通用diffusion理论迁来或改Ch29。
- **唯一拟稿，待root必要/actualowner/PRE：**

训练time还可以决定“允许学习哪批动作”，而不只决定同一目标被抽多少次。高质量target示教覆盖全部noise levels；另一些轨迹若仅在全局计划或局部运动上与target相合，可只让它们进入对应的高噪或低噪区间，再在当时合资格的数据中采样。这样把全time加权或整条过滤变成time-dependent数据资格，推理仍用原diffusion policy；条件是那部分动作结构确实可以借用，而不是任意次优数据自动有益。

[Ambient的有限动作对照](https://arxiv.org/html/2606.12365v1)显示local motion与task logic可有不同取舍，target数据更足或接触动力学不合时，低噪借用也会无益/反退。Gaussian理论、谱拟合或classifier分不清不证真实条件分布相同，观察域移仍未解决，且公开局部开关记法不作为完整可执行recipe。P/Q划分、分类/阈值搜索、更多数据训练与独立闭环回归都付费；局部性、分类或任务质量失配时，收紧合资格区间并回target-only、常规co-training/finetune与已验controller，不由更大可用数据池批准正确动作或安全。
