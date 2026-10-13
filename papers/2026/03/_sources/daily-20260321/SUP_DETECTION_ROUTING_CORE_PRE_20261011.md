# DetectionRouting18280 exact-v1：必要证据与受限评价 PRE

准备者resume_mar18，只本21补BJT03/20，当前合同与本日停点独立恢复；首批完整v1题摘/date夹证/root准入校准复用，不混文内prompt corpus v1/v3与arXiv revision。3+2+2=7，以拒绝率/探针可分性单轴评价的具体盲区计分，不给三阶段架构宣传或通用对照原则新分。尚未非准备者Source/PRE，无Books锁/写入/safe/DAY。

## 实际必要原证

[exact-v1](https://arxiv.org/html/2603.18280v1)实际§2协议、§3.1–3.7/Tables1–8、§4.1–4.5、§6及Appendix A/B必要干预/泄漏复验；不遍引用附件、全模型card、实现或版本史。九open-model/五lab与46 API model行为是不同人口。方法为hidden-state线性probe、方向消融、refusal harness与Gemini steering/human分类；不是直接观测内部router模块。

- §3.1 high-d/small-n ridge的train-set accuracy：48×4096、λ1、不留出训练准确率。matched topic null与200 shuffled-label训练也可100%，不能以原训练可分性推专门政治概念/circuit。原称6fold true-label CV较shuffle强，可只支持受测label generalization。§3.2 LOCO inventory列Tian4+4/Tibet2+2/Xin2+2/Xi2+2/HK1+1/COVID1+1总24，却称48及40–46训练/2–8测试，未闭合；best layer是CV后验择优，GLM/Phi prose94.8/98.9与Table2 91.7/97.9又不齐，不采精确best分数、全类别清洁泛化或zero-width CI人口保证。
- §2对照/adversarial强度多切片，29/32 discrimination prompts由本地/API多模型筛得，postselection人口不能推全自然分布。Chinese定义16而§3.5 human四model×32=128，不能合并同题数/同分母。human类别可重叠；propaganda/accuracy/evasion不是互斥概率。硬件、serving batch/concurrency、precision、总token/API费、重复seed、judgeprompt完整配置 Not Disclosed，不作生产性能研究。
- §3.3 rank-one α/layer intervention会改输出，Qwen产生非目标事实破坏；pol/safety区别与negative sentiment/formality/random控制只限所测方向。Phi最大control8.3pp与baseline6.3%、D4阈值5.9的反侧保留，不照“所有control无影响”。§3.4 directions对corpus敏感，GLM窄prompt .93换广prompt .16；CI跨零不证明数学正交或完整子空间独立，8pair→120pair口径与bootstrap112pairs不混精确样本。不同architecture/lab/training不是纯posttraining因果对照，transfer不成也不证独立物理router。
- A由每capability8prompt的centroid/PC atoms做ridge residual与额外A(Aᵀv)，只能清所测atoms，不授全部能力保留或精确正交投影（atom没有给出全列正交归一前提）。原只DeepSeek有raw/clean逐层logged相同refusal；不采跨模型无collateral保证。
- **B决定性反证**：初α sweep选题有4/8 overlap；作者重做selection2/eval2/adversarial8，但明确heldout baseline0/2与adversarial baseline0/8已零拒答。干预后0/2或0/8不能证明“消除拒答”或同分布因果收益；L6/L24独立adversarial还1/8拒答。此复验只可作更窄的spillover观察，不能以无overlap替代有效的干预前基线。保留其原声称resolved，不将其作为正面Evidence采用。
- §3.6 low/no refusal与non-refusal outputs的steering标签可共存，是受限refusal-only盲区；raw harness拒答与Gemini含refusal-like判分不同，mean仅nonrefusals条件人口，不是joint率、0–5绝对校准或普遍内容控制程度。§3.7/6 human-AI fine agreement54–57%，coarse87.5–89.6，Gemini43evasive human14，5/5尚未human校准；只按原限定标签/协议提供诊断。128 human interrater各项不同、evasion κ.40；不授judge真值。
- 46 API model only38usable，8error不能消失；n8→32多效应消失，Nova是明示非中国强效应反侧，不能用机构来源外推普遍政策。Qwen generations不同尺寸/训练/版本，不能识别纯时间因果。§4明确描述性三stage、alternative internal explanations；§4.3shared-refusal interpretive、gender8+8/null尚无second-domain复验。拒绝率盲区的受限测量事实可独立于这些中心架构/因果桥采用，是否足够须由非准备者裁，不自己绕过争议。

## Actual sole owner

`PLATFORM-EVALUATION-SYSTEM` Ch66：实际195–228的ObservedCapability/elicitation、unsupervised truth与压力配对，268–291 representation/干预方向counter与crosscoder，3150–3166 attribution identification disclosure；相邻Ch65/67开篇说明调度/监测不接管quality判定。现218–220区分salient特征/真值与未知用途、286明确方向干预/随机对照，3157限制causal identification；但缺**high-d训练分离与label-shuffle的容量反证，以及硬拒答全分母/非拒答内容标签的分责盲区联测**。本项不改Ch17/31，不授物理router或安全。

拟两段接在unsupervised truth受限对照现220之后、同压力monitor配对现222之前；同一评价链由内部线索资格过渡到输出验收，不新增孤立heading。

## 两段逐字 PRE（未授权写）

内部可分性与输出控制也须分开测量。样本远少于 hidden dimension 时，训练集上高准确率可能连随机标签都能拟合；应先固定 probe 容量与语料，保留匹配主题的 null、label-shuffle、未参与选择的类别/样本和层或剂量的选择记录，再问该线索能否在留出人口泛化，以及有无同条件干预前基线和非目标行为对照。无训练—测试重叠并不够：若留出题原本就不拒答，干预后的零拒答不能证明“移除了拒答”；direction 的 cosine 或区间跨零也不认证完整回路独立。<!-- source-family:SF-2026-ARXIV-2603-18280 -->

输出验收随后保留全部请求上的硬拒答、无效与错误，同时另报非拒答回答的事实性、回避或 framing 标签，并显式记录它们的条件分母和可能重叠；“回答了”不等于事实正确或没有内容引导。[受限探针与行为审计](https://arxiv.org/html/2603.18280v1)显示仅看硬拒答会漏掉另一种输出策略，但自动 judge 的细粒度标签与人工又有明显分歧，最高 steering 分并未独立校准，不能把它当绝对风险或普遍对齐证书。多语料/语言、方向提取、干预、模型调用与人工校准都有费用；题目选择、基线或判分身份不齐时，保留直接行为回归与人工核验，将内部 detection–routing–output 只作描述性假说，不由它授权安全编辑、因果架构或生产发布。

## 静态注 PRE

- `SF-2026-ARXIV-2603-18280` — [Detection Is Cheap exact-v1](https://arxiv.org/html/2603.18280v1) §2–4/6、Tables1–8及A/B必要干预边界；3+2+2=7，容量null/label-shuffle、选择与留出基线、refusal与nonrefusal内容的评价分责。LOCO库存/择层数字、方向人口/几何强解释和clean-alpha原已零拒答不采正面因果；judge细粒度分歧与未校准steering、事实破坏/负control、全调用校准费用保留，不授三阶段物理回路、安全编辑或普遍对齐。未核实现/复现。

待root非准备者必要Source/actual owner/PRE裁决；若有限评价事实不足独立分采，保7分与反证作中心暂缓，不假NC/EX、不缩池。

## 非准备者正式 Source/PRE 与窄写

root 实际 exact-v1 §2.3–2.6/3.1–3.4/3.5–3.7/4.1–4.5/A/B必要反侧与actual Ch66 210–226及65/67交接，非准备者 Source/两逐字PRE及静态注正式有限 PASS：shuffle200 null、LOCO库存与择层、CI跨零不等正交、B baseline0/2和0/8不采干预因果、conditioned steering/judge54–57限制均保留。两段评价分账可独立采用；物理router、安全编辑中心桥明确不采用，不用一般原则绕过争议。root授Ch66仅两PRE＋本人静态注窄锁。

resume_mar18 按原逐字两PRE在truth probe受限对照后/同压力配对前实际写入与静态注；写后完整局部/本人注回读和限定检查待记录，仍未非writer POST，不计safe/DAY。

## 一次 nonwriter actual POST（正式有限通过）

writer实际完整210–236/新222、224与末10行/本人5929静态注及邻注回读，限定diffcheck空。root非writer实际完整210–237两新段与全部邻接及最后本人源注逐字回PRE/必要Source，正式有限POST PASS：独立容量null/留出基线、全部请求与条件内容分母、judge分歧/全费用及直接回退准确；不认证物理router、安全编辑或零拒答干预因果。Ch66窄锁释放，可计单项实际I，不预支DAY，不再改静态注身份。
