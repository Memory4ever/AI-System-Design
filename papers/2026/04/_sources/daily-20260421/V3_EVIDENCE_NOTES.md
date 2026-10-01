# 2026-04-21 必要证据审阅

窗口 `2026-04-20T09:00:00+08:00`～`2026-04-21T09:00:00+08:00`。以下是分批作者判断，不是冻结分母或独立日级Gate。日期仍按官方批次组合核验，Submitted/Updated均保留原字段，不独立冒充first-public。

## [BASIS — 2604.16324v1](https://arxiv.org/html/2604.16324v1)

实际读取§2.1–2.4、Algorithm1、§3配置和Table1。线性层保留`dX=dY Wᵀ`的当前精确局部反传，仅用batch轴sketch近似`dW`；activation norm校准可减少幅值漂移，却是依赖样本的缩放，作者亦承认偏差。缓存还包括B长度的hash/sign，不能把rank×feature缓存的阶数当全部训练peak memory。实际实验仅T4、JAX/Flax、2层d64/2head、seq64、batch1、固定SGD与FineWeb样本；R=1的held-out loss劣于dense，未见peak-VRAM/wall-clock测量、seed方差或普遍收敛证明。保留这一受限近似梯度分支，不采用无限Context、训练拓扑不变或理论无损宣传。

§2.2 Eq6以bin-label置换表示balanced hash；任意operand的交叉项权重不相等时，仅平衡bin大小不证明weighted variance全局最小。以B=4,R=2、仅样本1与3的`X/dY=1`非零为例，该Eq6分组使这两样本必碰撞，方差4；另一同样平衡分组可将其分开，方差0。**Algorithm1的RandomPermutation若是B长度assignments置换则不同**，该对碰撞率1/3、期望方差4/3，不能称整个算法固定碰撞。apr02已独立实际核Eq1–7/Alg1并确认此窄争议；仅挑战Eq6与无条件weighted-variance最优表述，不否定未缩放sign sketch无偏性或全部经验。拟5分/理论争议Deep，暂不写Books；重开需要作者明确Eq6/Algorithm1分组定义和加权最优限定，不追加泛benchmark。

## [Training for Compositional Sensitivity Reduces Dense Retrieval Generalization — 2604.16351v1](https://arxiv.org/html/2604.16351v1)

实际读取§2–4、AppendixB/C/D。四个encoder在NQ与结构负例混合的匹配wall-clock对照中，target-domain结构区分改善并不等于zero-shot NanoBEIR保持；MaxSim作为reranker有效，也未可靠区分role/negation near-miss。单向量ANN召回与token-interaction身份验证因此是不同目标。实验使用128token、Top100、L4/A10级、3seed和合成near-miss；固定时间不等训练数据/steps，所谓几何不可能只给informal桥，不能采用普遍所有encoder不可表达组合的结论。

实际Books再比较：root对读当前Ch76 hard-negative目标域收益/原域退化段及query/evidence gate，现文已明确跨域代价和relevance≠support。采用的长期命题已有具体正文，2+2+2=6深入完成、已有覆盖，不再申请新增正文；此前“尚未明确”的缺口判断被本次真实段落比较修正。四backbone/合成5,964对的受控near-miss协议仍保留日报，不冒称书稿已实现整个基准或所有encoder理论。

## 当前写后同步

本轮最新270完整题摘/175必要最小/146正式作者阶段候选。16479/16462/16503已在Ch23原codec/fusion/update-read论证各窄写，apr02实际重开必要原文并顺读真实正文及相邻交接，写后独立通过，见V3_APR02_CH23_THREE_WRITE_AFTER.md；当前真实I10/普通Books23。三项此前未列正式表，实际整合后新增三行。EvoComp仍待独立采用/实际书稿；OrthoReg只隔离未建立独立随机分布桥，不否定有条件lemma。新四项必要裁决保存V3_BATCH_17139_17145.md：17139保护深入Only、17143标准Existing、17145标准Only；17140更早同家族公开日未恢复，日期隔离不评分。以下是历史阶段记录，不继承陈旧待核状态，不冻结分母。 新四项V3_BATCH_17147_17163.md：17147标准Only、17159标准Existing，17153/17163具体前分母关闭，有限非作者待核。 17187/17198新增两个正式终态，17197/17200具体前分母关闭，必要证据见V3_BATCH_17187_17200.md；17207/17211标准Only、17210/17215保护/gap深入Ch72普通提案，见V3_BATCH_17207_17215.md；最后有限五家族已落V3_BATCH_17237_17249.md；原有限信号已收口，普通Books23及必要非作者仍未完成。

新四家族V3_BATCH_17040_17056.md已落必要审阅/身份例外：当前130必要最小/93正式作者终态、270题摘；实际I7/普通Books19。17054不评分，其余3候选终态待有限非作者；未冻结，不以此代全日来源验收。

2026-09-27本轮新增实际写后非作者PASS：16332/16826/16940→Ch30，16395/16583→Ch56。root已实际顺读五处正文及邻接，复用本轮必要原文核验；item分歧×rank、gauge-sensitive B谱、sunk FullFT后压缩、arrival计划/分配与LCP、router/residency反馈均保留受限代价和反例。累计真实I7，普通Books提案19；正式表90，完整题摘270/必要最小126不变。下面2I/24是此前阶段日志，不作当前状态。没有自签整日通过。

16686已在Ch76 prior/context gate后真实写入same-prefix条件token回退、双forward/阈值代价及有益context共存分支；17104已在Ch59逻辑artifact身份之后真实写入sketch→ratio→online base/split物理规划与new-base/I/O边界。root实际必要源与正文/相邻交接写后均PASS，两个6分gap深入变实际Integrate，不是仅source→owner。对应Book Review notes已由root同步，不擅自再改共享章。新七项必要审阅见V3_BATCH_16988_17022.md；累计126必要/最小家族，270完整题摘不变，85正式作者终态，24普通Books待办，分母未冻结。

## [Cross-Family Speculative Decoding on Apple Silicon — 2604.16368v1](https://arxiv.org/html/2604.16368v1)

实际读取§3.1–3.3/Alg1–2、§4–5/Table2–3、§6.2成本式与硬件限制。作者在M2Pro32GB上比较Bielik11B int8与三个int4 drafter，generation128tokens、50prompt/primary条件、k2/4、prefix5；TPS不含prefill，未测并发/SLO。带上下文重tokenization改善acceptance，但额外draft KV重同步和共享带宽成本可吃掉收益；专业drafter也未普遍优于通用draft。Ch48§“Acceptance不是独立常数”与draft/verify/state成本已有同一长期判断，因此拟标准6分、已有覆盖/受限例证，不为设备名新增一段。Alg2未证明跨tokenizer exact distribution；§6的二次overhead拟合只有两个k点，等式简化还省去r/k等项，k6样本数量前后不一，不能采用公式阈值普遍预测。

## [Same Verdict, Different Reasons — 2604.16383v1](https://arxiv.org/html/2604.16383v1)

实际读取§3.1–3.2、Table1、§4.1–4.2及groundtruth脚注。MedExpert是真人遗漏标注；HealthBench此文用GPT4.1按正rubric给ideal-answer重新评分，不能把全部groundtruth写成独立clinician逐回答真值。HealthBench Dynamic-Checklist与这套标签有同源循环，作者已排除相应高AUC；few-shot/F1提高而排序区分不足、90%遗漏recall仍需近全人工，是triage效用的具体反证。解释对齐又由GPT5Mini分类并用20人工例校准，不是无误reasoning oracle。Ch66 expected-fact inventory及AUC/risk–coverage现文已承载遗漏检测与阈值分账，拟标准5分已有覆盖，日报保留这个受限反证；不宣称所有LLM judge无用或医疗正确率。

上述四项未复现实验、未检验artifact执行；必要原文已读与作者判断不等于独立通过。BASIS/检索提案仍需root定点源/owner复核；另外两项也需相应采用范围校准，不预支日级Complete。

## [FlexStructRAG — 2604.16312v1](https://arxiv.org/html/2604.16312v1)：最小贡献消歧后关闭

作者实际读§3.1/§4.3 Table2：document-local抽取、token阈值分块、bounded overlap、source-span引用，随后二元/多元关系与cluster并行组织；组合移除说明互补，却没有抽取缺失/错误的控制试验建立宣传的鲁棒成立条件。新增是这一已有多粒度方案的组合operating point，而非值得改变本项目检索解释的重要机制或反证。**前分母关闭**，不是因为已有owner或材料费时；保留已读证据，不追全部发表史。apr02本轮实际核完整題摘、§3.1/Table2后接受这条具体closure；该局部复核不代替本日来源/日期/Gate。

## [GraphRAG-Router — 2604.16401v1](https://arxiv.org/html/2604.16401v1)：标准审阅拟仅报告

实际读§4.1、§5.1/§5.3–5.5、B.2/B.3。Table3存在one-time、LLM-first、GraphRAG-first的顺序对照，可保留窄路由证据。**这里先选检索框架及预期granularity，再选generator，然后才调用pair；并没有先取得实际检索证据再决定模型**，不能把标签顺序写成已经实现evidence-dependent admission。成本1/2/4是model-scale proxy，不是构图、router、token、API与尾延迟总账；新增pool的HotpotQA也微降。模型3B、固定五GraphRAG/五generator，离线Wikipedia条件；未披露seed uncertainty、各顺序独立matched训练明细或生产SLO。拟2+1+2=5、标准完成/仅报告这个受限order结果，不能抬成普遍最优routing或额外Books正文；待日期与非作者裁决。

## [Functional Similarity Metric for Neural Networks — 2604.16426v1](https://arxiv.org/pdf/2604.16426v1)：窄保证争议

因HTML作者日期异常，作者实际核官方PDF-v1首页April21/页眉提交April4；只读§10.4及§11.2–11.3必要部分，不声称通读92页。PDF同样说fixed hashes可能违反triangle，而定义是同一签名的Hamming均值：每项`1[a≠c]≤1[a≠b]+1[b≠c]`确定成立，均值仍成立。此反证只否定该特定声明，不否定Jaccard无偏估计或全部matching实验。两个32-neuron、16k-sample toy比较未直接检验parameter-perturbation稳定canonical。拟2+1+2=5、保证纠错deep例外/争议暂缓，不能正面采用；作者修正定义/命题与稳定性证据是窄重开条件，日期仍依正式公开组合确认。

本轮apr02有界非作者复核实际读取官方PDF §10定义及§10.4 fixed-hash声明，确认同一hash realization的逐项Hamming三角确定成立；只隔离这一错误陈述，不否定Jaccard unbiased/identity概率或全部matching。同批另核16312 closure、16401必要顺序/成本、16318 closure，共四家族必要内容；未检查Apr21全部候选、日期或日级Gate。

## [Diagnosing LLM-based Rerankers — 2604.16318v1](https://arxiv.org/html/2604.16318v1)：准入信号定点收窄

实际读IV-B/IV-C、V TableII/III、VI-A。论文比较full-catalog baseline与FAISS pool，cross-encoder实际为MS-MARCO MiniLM，非生成LLM；表述的总体胜负不能归因‘LLM reranker能力’。同pool HR .011→.008而nDCG .004→.005，不是所有质量下降；局部诊断没有受控新边界足以超出成熟coverage/任务域错位原则。apr02实际核同段和表后支持**具体前分母关闭**，保留证据与改判原因，不把该局部结果包装成新通用反证。

## 六项有限必要正文（作者裁决，非日级 Gate）

### 16615 / 16657：外部模态条件化的 Bayesian rank latent

来源分别为 [CoCo-LoRA v1](https://arxiv.org/html/2604.16615v1) 与 [CALIBER v1](https://arxiv.org/html/2604.16657v1)，实际读两者 §2.2、§4 的方法与对照。不是同作者就合并家族：前者共享 pooled audio 再逐层映射，后者文本 token query 对 audio frame 做 cross-attention；二者都把随机性放在低秩矩阵 E，保持 A/B 和 backbone 的角色分离。各拟 2+1+2=5、标准审阅后仅报告。临床/情绪任务不是硬排理由；采用窄 PEFT 条件化机制，但 AUC 不证明 posterior variance 被校准为错误概率，也没有直接 noisy-audio reliability 的有效性对照。CoCo-LoRA 为 rank8、两轮、十次 MC；CALIBER 为 rank8、50轮、十次 MC、speaker-separated 五折。不能横比训练预算或称 token-level 必胜；CALIBER Table3 有 global/fusion 反收益。暂不把该实现采为通用不确定性设计；helper 已实际核方法/评价并支持上述窄准入，不代表日级 Gate。

### 16677：ReconVLA 的动作选择不是原边际覆盖保证

[官方 v1](https://arxiv.org/html/2604.16677v1)，实读 IV-B/C、V-C/TableI–II、VI-A/TableIII。对 action+latent 训练 error quantile、holdout offset，再从 K=10 选最小值；另用 nominal-state Mahalanobis score 触发干预。LIBERO 两种 policy、UR5 四任务/100训练轨迹只支撑受限经验结果。作者与 helper 必要消歧后改为具体前分母关闭，不评分：成熟 CQR error-ranking/SMD 组合没有新增有效安全成立条件。Eq6 将 α=.1 下分位当90% upper coverage；共用 offset 不改变 argmin，TableII 未分离rawQR/CQR；原边际覆盖不直接传给 postselection，AUC 也不证明安全。`2|A12−.5|` 不是 Cohen d。保留这些问题及经验，不据缺陷本身新造长期贡献；没有否定全部动作选择收益。

### 16686：连续 logit tilt 与显式 backoff 是不同控制分支

[NWCAD v1](https://arxiv.org/html/2604.16686v1)，实读 §3.2–3.3、§4、§6/Table3、AppB。JS 小且 no-context margin 大则复制 baseline logits；否则选 confident context 或 contrastive fallback。exact 只限当前共同生成历史上的被选 token，全程 backoff 才保证整串 baseline 一致；confidence 不等 correctness。拟 2+2+2=6，Ch76 context/prior gate 当前没有这个 token-level backoff 分支，若独立 owner 复核支持再以知识缺口深入。Llama8B 同受控切片调三个阈值，无单独 heldout dev，复用到70B/Ministral；两条 forward、topK-JS、短 greedy 输出与 no-fallback 接近全方法均保留。不是所有 context 必不退化，尚未写 Books。

### 17121：架构 taxonomy 不自动成为长期增量

[Topological Trouble v1](https://arxiv.org/html/2604.17121v1)，最小读 §3–5。明确区分 token、depth、autoregressive 三维回流，formal bounds 来自引用的既有结果；实现箭头刻意不指定，后段是未来训练/表示议程。作者与 helper 独立必要消歧支持具体前分母关闭：本篇没有新证明、受控证据或综合结果解决一个原有知识分歧，不将递归分类命名当新增 state-tracking 保证；不是因综述标签拒绝。

### 17104：tensor-content 规划与 Registry 身份仍分层

[官方 abs v1](https://arxiv.org/abs/2604.17104v1)、[HTML v1](https://arxiv.org/html/2604.17104v1)、[PDF v1](https://arxiv.org/pdf/2604.17104v1)。库存标题为 TStore，当前三种官方入口同为 TensorHub；实际 PDF 首页及 §4.4、§6/Table3 与必要 HTML 一致，保留标题 alias，不仅凭差异断言错版。TensorSketch 对 raw bits 建低成本指纹，TensorPred 估 delta ratio，FlexSplit 把新增 base 的完整保存成本与旧成员节省联合决策；不是 model-card lineage 相同就配对，ZipLLM 对照也使用 bit distance，不能把旧方案描述成纯 metadata。拟 2+2+2=6、Ch59 当前缺 sketch→ratio预测→online base/split 的具体分支，helper 已核必要源和实际正文并支持窄缺口，待 root 协调实际写入。2,890模型/40.11TB trace、EC2 c6a.48xlarge/96core/384GB，Table3为192线程全内存无I/O；不能当下载SLO、hash认证或全局最优。只有压缩物理规划提案，Registry逻辑身份/digest/授权保持；尚未写 Books。

## 后续六项：必要正文与具体裁决

### 16320：输入邻域与等价程序是不同干预

[官方 v1 HTML](https://arxiv.org/html/2604.16320v1)，实读 §3.1、§4.1–4.2、§5.1。输入 mutation 改的是被执行实例，四种 MPT 才要求语义保持；后者仅在原输入执行核输出相同，不能叫全部程序全域证明。684 程序各十个输入、14 模型/default API，PSR 是全部十次正确；异常 any/strict substring 及 multiple assertions 的 any-correct 有 oracle 宽松性，模型大小/训练机制不能由跨家族排序识别。拟 2+1+2=5、标准完成/仅报告具体 canonical 高分与邻域表现的反证，不据此宣称有/无内部世界模型。Ch66 的关系型回归已要求成对 mutation、独立 gold 与协议边界；此受限代码实例暂不另写通用机制。非作者校准仍待。

### 16322：可行 Witness 与难度 Actor 不应混为一个控制器

HTML 两次不可取后读[官方 PDF v1](https://arxiv.org/pdf/2604.16322v1) §3.2–3.4、§4.1–4.3，首页 April21，提交 Feb27 保留而不直接回拨。parametric schema 提供 AST checker；生成器每加约束同时改 witness，累积 tests/checkers 通过后才看 actor pass rate 决定是否继续加难。该顺序是实际控制分支，不仅论文命名；测试通过的可行性仍相对于有限 checker，不是任意程序正确性证明。27 初始 schema、三代演化、4,241问题；模型/生成器预算和 schema evolution 不全部隔离，Seed-Coder 第二→三代部分指标回退。拟 2+1+2=5、标准完成/仅报告这个条件化 curriculum。Ch27 既有 constraint/spec→独立 verifier 与 current-policy difficulty 分层已承载长期约束；不称其全部算法已有覆盖，也不为名义 SOTA 添加正文。

### 16332：标签分歧可能被 Adapter 更新容量选择性放大

[官方 v1 HTML](https://arxiv.org/html/2604.16332v1)，实读 §3–5、Limitations 及必要梯度/校准解释。ChaosNLI 100标注/样本形成 entropy，五轮39停点 loss/AULC；4 encoder+Qwen1.5/3B、r4/16、同LR/batch、三seed（两条件缺seed）。高分歧训练样本在 LoRA 下 loss 上升，full FT/IA3 对照不同；不能把多数标签 loss 上升当训练功能退化或严格证明 rank 是唯一原因。MNLI相关更弱、最多解释约18%方差，noise injection 小效应、decoder 没 full FT 对照。拟 2+2+2=6、实际知识缺口深入：Ch30 当前 rank/placement/梯度耦合没有 annotation-disagreement×逐样本轨迹的具体分账，Ch66 有 label-distribution authority。可用一段提醒提高rank/改loss是待验proposal，不自动删争议数据；普通 Books 提案，尚未获共享锁/实际写入。

### 16349：实时 Oracle 需要冻结时间锚与修复版本

[官方 v1 HTML](https://arxiv.org/html/2604.16349v1)，实读 §3.1–3.3 与评价限制。相对时间在执行时解析，DOM workflow 生成当前答案；320中文/12域、Claude4.5造流程，文本与截图交叉核加人工初验。Repair 的运行成功不自动证明新DOM语义不变；多hop复用同 L1 workflow 不代表独立答案oracle。拟 2+1+2=5、标准完成/已有覆盖 Ch66 的 run identity、snapshot/replay/真实 outcome witness 与 repaired harness 版本边界；保留受限实时QA案例，不用 lazy-retrieval错误比例证明任意Agent机制。非作者待核实际既有命题。

### 16358：前缀 Worst-turn Reward 与动态对手共演化

[官方 v1 HTML](https://arxiv.org/html/2604.16358v1)，实际 §4.4 Eq17–21、§5/Table3、附录消融。Tutor 同时生成下一攻击和评分；prefix min/mean 再累积为 trajectory return 更新所有 assistant tokens，属于 reward shaping 而非逐turn causal credit。Eq18 s/安全和 Eq17 weighted reward 指代须谨慎，不称硬安全保证；长短trajectory的回报可比性、对手/裁判共享误差与阈值后才计算Table3均是限制。QwenVL3/7B、BF16/8×A800、5rollout、batch64，去TCSR/feedback均有受限消融，但不能从平均 safety/helpfulness推出整体发布安全。2+2+2=6、标准完成/仅报告窄训练分支；非作者必要校准已完成，尚无实际保护行为变化或已确认长期缺口触发深入，不由安全标题强制扩审。

### 16363：生成类别分布只提供受限 Lineage 线索

[官方 PDF v1](https://arxiv.org/pdf/2604.16363v1) 网页工具因24MB上限失败，直接官方PDF恢复成功；实读首页与主文 §3–5.3（前八页），非54页全部附件。42组合prompt×每次30生成→CLIP分类分布→Wasserstein最近六base→Beta count interval；Beta对象是 probe argmin 投票比例，每个base均从Beta(1,1)起算，不是归一化模型身份posterior、合法所有权或部署unknown-lineage错误率。独立prompt/iid是假设，共享类别/属性与CLIP误差可能相关；组合稀有不保证任意FT都保行为。六families/十三variant和UCE局部测试，不能覆盖针对探针的自适应服务/任意merge。非作者已实际读取同版PDF前八页与Ch59。拟 2+2+2=6、标准完成/仅报告该query-only实现；没有发布/保护行为变化，不因lineage标签强制Deep。Ch59一般‘行为指纹不是所有权证书’及querybudget/reference/阈值身份已有，但不冒称整个探针实现已有覆盖。

### 六项写后独立校准同步

`V3_MINIMAL_DISAMBIGUATION_INDEPENDENT.md`第三批已实际完成16320/16322/16332/16349/16358/16363的必要原文和窄owner校准，以上旧‘待非作者’以此为准，不等日级通过。16320两类干预是分开实验；16349 time-anchor对照改变日期，repair只runtime error/null，不检测静默语义漂移。16332只四encoder有FullFT、IA3限RoBERTa/SNLI，两个decoder无FullFT；soft-label仍loss上升，不能当已验证修复。16358保留prefix shaping的标准6分，仅报告，尚没有独立核定发布/保护行为改变触发Deep；不将标题safety自动作为扩审依据。16363已在上段明确Beta投票频率边界。六项没有自动全升Deep，16332因真实Ch30缺口继续必要Books判断。

## 流式 Serving、参数共执行与过滤检索的必要三项

### 16395：输入到达是新的调度事件，而非只增加最终 Prompt 长度

[Stream2LLM 官方 v1](https://arxiv.org/html/2604.16395v1)，实际读取 §4.1–4.4、§6.1–6.4。Phase1只计算优先级和可行性、不分配或修改状态；Phase2才获取块并从未调度请求中选抢占对象，用硬件画像比较swap与recompute。append与update均通过真实token LCP保留前缀、失效后缀，不是任意文档语义相同就复用KV；早位置更新会吞掉收益。拟2+2+2=6标准审阅，随后按真实Books差异判断。

H10080GB/H200141GB、Llama3.1-8B、TP2、80%显存预算、2048–8192 step token budget，crawler4322/ANNS500查询、不同到达轨迹与QPS replay；只测PD prefill instance，TPOT不测，headline TTFT不等全链SLO。Ch56现有request-arrival/preemption与Ch45 causal-prefix身份给一般边界，但尚未见streaming-context-arrival→analysis/allocation两阶段这一具体分支；拟在Ch56 admission/preemption中最小补充，未独立采用或实写。

### 16400：Shadow Adapter 的原子交换不自动给整请求单版本保证

[CoLLM 官方 v1](https://arxiv.org/html/2604.16400v1)，实读§III–V unmerged/Shadow双adapter和§VI实验。Inference读active、optimizer写shadow，训练步后原子换指针并异步回拷；机制避免直接读半写A/B，却没有据此证明整条多token请求、已存在KV和多kernel执行均绑定同一adapter revision，回拷/下一步同步也应实际运行验证。不能照录无条件deterministic、单步传播或所有PEFT通用保证。

两服务器共8 A30 24GB、PyTorch2.5/Transformers4.48、Llama3.1-8B/Qwen3-4B、六instruction数据集和Azure traces；quality用CE，global adapter通信被忽略。Ch56 co-serving已拥有冻结base/adapter commit与资源租约，Ch59/55版本身份仍须保持。拟2+2+2=6标准完成、仅报告双缓冲共执行方案及未证明的request-version条件，不因原子pointer swap采用全请求consistent或3×普遍结论，也不据缺这个证明否定全部goodput经验。

### 16402：Bucket Layout 是执行选择，Remote Edge 不是任意过滤可达性证明

[GRAB-ANNS 官方 v1](https://arxiv.org/html/2604.16402v1)，实读§4.2–4.5/Alg2、§5.1–5.6。Scalar predicate分bucket、物理连续向量、fixed-degree邻接、local/remote边和append-only out-of-order insertion的ID→location映射，是CPU分支图直接移植GPU之外的具体设计分支。Alg2丢弃区间外候选，remote edge存在本身不证明任意诱导过滤子图仍导航；连续存储也不单独保证每个warp邻居读取coalesced。保留布局机制，不正面采用exact nearest-neighbor/任意filter guarantee。

四百万规模数据集、uniform synthetic scalar、随机区间、batch100、Recall@10×QPS Pareto、i9-14900K/RTX3090Ti；CPU与GPU资源不相同，bulk insert不等删除、高churn、任意布尔ACL或concurrent snapshot维护。拟2+2+2=6标准完成/仅报告该scalar-range GPU实现，Ch76 filtered ANN/freshness/mapping框架不冒称已完整覆盖具体算法；长期正文增量仍待非作者source→owner判断，不凭240×追加Books。

本批 apr02 已实际独立核三项必要原文与 Ch56 等具体正文：16395 的输入到达事件与两阶段计划/分配是真实缺口，可按 6 分 gap 例外深入；DefaultStream median 改善而 P99 退步、压力轨迹人为延迟 10×/30×，不能采用一般 SLO 收益。16400 原子 pointer 不保证多 decode 版本 pin，16402 remote edge 不保证任意过滤诱导图可达、连续行不证明 gather coalescing。后两项标准仅报告通过窄命题复核；本批未复现实验，不是日级 Gate。

## 新四项必要正文（作者侧判断，尚非独立日 Gate）

### 16385：Web 扰动轴与真实转移语义分别评价

[StressWeb exact-v1](https://arxiv.org/html/2604.16385v1)，实际读 §3.1–3.3、§4.1–4.4/Table1。十个生成站点、149 任务、七种条件将视觉/DOM 扰动、单击改双击等 interaction semantics、执行失败/弹窗分开；RemapE 的显式提示也不能与隐式条件混合。Playwright screenshot/DOM/history、100 步上限，checkpoint pass 不是整任务成功，额外执行成本和截断仍影响结果。八种 API 模型的 precision/hardware/SLO 未披露。拟 2+1+2=5、标准完成/已有覆盖：Ch66 实际的受控状态/规则配对、失效执行与累计任务复杂度已承担该长期判断，不声称其整个 benchmark 已实现或全部代理失效原因已识别。后续只定点补 §4.5 必要边界，不扩附件。

### 16420：允许无效搜索对象不等于执行无效程序

[AST 两阶段演化 exact-v1](https://arxiv.org/html/2604.16420v1)，实读 §3.1–3.4/Alg1–2/Eq1、§4.1–4.2/Table1–2。删除/交叉 AST 后，原无效对象可留在 population，但 fitness 来自 LLM 修复出的合法子程序；不是运行非法程序，也没有证明合法搜索空间的拓扑不连通。EoH/ReEvo/EoH-S 与对应两阶段变体在披露轮数/population 配置比较，缺单独修复/结构控制与普遍收敛保证。iOBP n1kc200 .0340 对 .0182、TSP c100 8.769 对 8.723 是反收益，不能称所有配置更好。拟 2+1+2=5、标准完成/仅报告具体搜索分支；Ch81 现有 repair/build 与探索节点协议不冒称已有这套算法，当前受限证据也不足以采用一般“跳出合法区”设计保证。

### 16421：几何表征一致性指标的对象必须统一

[GeoRepEval HTML v1](https://arxiv.org/html/2604.16421v1) 与[官方 PDF v1](https://arxiv.org/pdf/2604.16421v1)均实际读取 §3.1–3.3 Eq1–6、§4.2/§5.1–5.4、App B.1/Table7。158 core/474 等价变体、十一 API 模型、temperature0/top-p1、每项单次；人工核题与后续 normalization 不构成公开运行 oracle。Eq2 Invariance 是三种表示均正确，Eq3 Consistency 是三种答案相同，Property3 声称后者不小于前者。若三种正确答案依表示采用不同尺度，必须先在同一规范答案空间比较；原定义未交代这层桥。更直接的同版 Table7：Haiku Invariance .918/Consistency .741、Gemini .948/.812、Qwen .596/.443，均与 Property3 方向矛盾，PDF 第16页同样如此。拟 2+1+2=5、纠错深入/争议暂缓，暂不采用该指标保证或据其推模型能力；不否定受控等价表示评价本身。重开条件是同 family 原始预测、规范化/指标实现与更正定义/Table7，不是再扩 benchmark。需非作者定点核该矛盾。

### 16479：训练期频带压缩与部署后剪掉 Latent 是不同 Codec

[LC-VAE exact-v1](https://arxiv.org/html/2604.16479v1)，实际 §4.1–4.3 Eq3–8、§5.1–5.3/Table1–4/Limitations。3D wavelet 变换后 Eq5 保留 LLL/LLH/LHL/HLL 四组、其他四组置零，再逆变换交 learned decoder；不能按摘要简写成只留 LLL。该 filter 参与完整 encoder/decoder 训练，与同压缩率减少 channels 或 post-training PTLC 不是同一个 codec artifact。VAE 200k steps、8×H200 约五天；Latte-L 100k steps、16 帧、2048 视频 FVD，未给 precision/生产 SLO。重建 PSNR 与生成质量不必同向：WebVid 8/16 的 rFVD 135.99/73.66 对 baseline101.06/68.72 退步，Sky4 生成 FVD240.56 对198.87、UCF16 735.04 对721.43 亦退步。拟 2+2+2=6、Ch23 codec rate/distortion/downstream 现有原则下，具体“训练期固定频带支持→解码器适配”分支待独立实际缺口核验；不是普遍更好或已测端到端加速，不先写 Books。

四项身份已与各自官方 abs/v1/必要正文对读。原始 Updated/OAI 字段分别为：16385 `2026-04-21T00:02:03Z`、16420 `00:02:49Z`、16421 `00:02:50Z`、16479 `00:04:10Z`，OAI datestamp 均 04/21。只结合永久 ID 公告分配、相邻批次与官方公告 slot 作 08:00–09:00 北京时间有界推断，不将 Updated 或提前 Submitted 单证改名首次公开；后续日级日期审查仍需检查具体例外。此小批完成时必要审阅为27个family、正式表17个作者侧终态，均非冻结分母。

## 追加必要小批：16405 / 16410 / 16423 / 16424

### 16405：危险初态、触发与严重后果不是同一评价对象

[ICAT v1](https://arxiv.org/html/2604.16405v1)实际读§2.1–2.3、§3 setup/metrics/Table2–3、Impact/limitations。事故记忆与标准派生pseudo-case有不同provenance；校验初态后仅把动作给video world model，风险解释留给三人评价，best-of3由RCCC选择。909项、六video模型，不是在线风险概率或真机policy安全。拟2+1+2=5、标准完成/仅报告：条件风险链测试有独立诊断价值，但不据其采纳认证门槛。Ch66已有物理可观测量及依赖/critical-outcome一般原则，未声称整个ICAT方法已有完整覆盖；采样oracle/近似severity和coverage限制保留。未披露运行hardware/precision/SLO。

### 16410：方法均值不能把欠优化当作低秩固有劣势

[Matched-LR CLIP v1](https://arxiv.org/html/2604.16410v1)实际读§3.1、§4–6、§7.2必要backbone/regularizer反例与§9。ViT-B/32、四sharedLR、五seed、EuroSAT/Pets；LoRA r8低LR欠拟合而高LR恢复，adapter-active CIFAR100 transfer另测。相同LR不是相同有效步幅或总compute；attention entropy/CKA仅相关诊断，不能当retention因果。拟2+1+2=5、标准完成/仅报告，受控优化点反证值得保留，不从有限grid推全部FT/PEFT排序，不为新paper名重复Ch30的placement/heldout-transfer与Ch66预算原则。

### 16423：训练期防御对象可以改变梯度，而不只是推理时抑制

[PPS/IP v1](https://arxiv.org/html/2604.16423v1)实际读§2–3、§4.1–4.4/Table1、§5–7。Qwen2.5-7B-Instruct、LoRA r64/alpha128、trait vector与训练期prompt移除后再评价。PPS在trait轴可由放大变衰减；IP接近中性，但不能据此完整解释其机制，也不抑制该设置中已学性状。activation-gradient并非parameter-update identity，直接梯度干预有coherence崩溃反例。拟2+2+2=6、真实缺口深入：Ch29噪声/retention/teachertrait现文缺“训练期trait-aligned偏置与解释性prompt拥有不同责任、已有trait与新trait分账”分支。仅提案，待作者外原文→owner及共享锁，不先采用；不把IP explaining-away当已证因果或开放安全保证。

### 16424：平均时变传递函数不能直接承接LTI保证

[HTML v1](https://arxiv.org/html/2604.16424v1)与[PDF v1](https://arxiv.org/pdf/2604.16424v1)实际核§3.2/3.4、§8.1、§9与AppA Table16。LTI H∞界有特定假设；Remark3.2将时间变化transfer先平均再应用该界，缺支撑桥。最小LTV反例：无记忆系统y_t=b_tu_t，b=(1,-1)，平均K=0，但u=(1,-1)产生y=(1,1)；小幅缩放仍是精确一阶系统，不能以平均K给零输出界。只隔离这项extension保证，不否定LTI分支/所有攻击。预训练Mamba谱攻击是pending；4层S4-lite/128hidden/1000合成序列、360测试的greedy位置攻击不证明frequency-concentrated真实模型攻击。拟2+1+2=5、纠错深入/争议暂缓，不写Books；重开需时变系统正式bound及对应真实协议结果，不全版本搜索。

四项原字段：v1 Updated分别`2026-04-21T00:02:31Z`/`00:02:39Z`/`00:02:53Z`/`00:02:55Z`，OAI均04/21；Submitted分别03/31T16:36:33Z、04/01T06:35:09Z、04/03T16:54:25Z、04/04T13:08:38Z。结合公告分配/相邻批次/官方slot作本窗08–09推断，提前提交不被误写first-public。本轮必要/最小审阅31个family，不是31候选或日级终态。

apr02实际独立核16421的Eq1–6/Property3与Table7：规范答案空间下all-correct应为consistent子集；未规范原输出则Property3缺桥，两种解读都不能同时采用保证与表中反向数字。窄Disputed通过，不否定representation测试。16479实际原文→Ch23缺口通过：按Eq5训练mask，不将Appendix阶段缩写当恒定轴次序或C.2不同频带描述当Eq5；质量退步保留，仍待实际Books写入/写后验收。

16385本轮已实际补读§4.5：自报成功与page oracle失配、提前终止/预算混杂均已纳入正式正文；不再有该项普通补读待办。

后续apr02实际独立核16405§2.2–2.3/§3、16410§3–6、16423§2–4.2/Table1与Ch29:975–1008、16424§3.4/Remark3.2及最小LTV反例；四项上述窄处置通过。16423是source→owner已通过而尚未写入的6分gapDeep，不先称Integrate；16424只隔离平均transfer保证，未否定LTI界/全部经验。该复核计入后续日Gate，不无差别重复附件。

## 16391 / 16431 / 16453 / 16456：必要原文收口

四项官方abs/v1均已实际核题摘、版本history及当前说明，没有withdrawal标记，不把页面未提供某类标记称为缺材料。原库存Updated为04/21 UTC00:02:12/00:03:05/00:03:37/00:03:39，OAI均04/21；Submitted分别03/27T17:20:10、04/06T13:43:20、04/07T21:48:04、04/08T00:43:48。结合已保存相邻批次/ID公告分配/官方EDT槽有界推断本窗08–09，不改名Submitted或Updated为公开。四项本来在270完整题摘内，复读不增加初筛数；必要审阅累计35family。

### 16391 DeFI：预训练责任先分开，再作动作适配

[官方HTML v1](https://arxiv.org/html/2604.16391v1)实际读§3.1–3.4/§4.1/4.3–4.5/Table4–9、AppA.3 Alg1、A.5–A.6。Forward以混合视频noise prediction预训练；inverse从current/future DINO特征经VQ latent重建future feature，无action-label。下游不是三模块全部更新：固定forward，一步denoise所得feature经MLP适配给inverse，训练inverse及diffusion action adapter；inverse预训练reconstruction decoder丢弃。Table9 all-train4.40低于inverse+adapter4.51，但该对照不独立证明唯一gradient interference因果；Table5部分逐步数字与平均长度前后不完全一致，不采用它推精确人类数据增益。

CALVIN1000rollouts、Simpler三任务有输于基线slice；Franka8任务1600轨迹，每次最多20连续尝试，不能称单次81.3%或安全。4090五次平均component86.1/42.9/24.3ms，非并发/尾SLO；trainingH100、precision Not Disclosed。Ch26已有未来观测→inverse action和action-facing latent重建陷阱，但缺无动作标签数据分别预训练两职责→固定forward表示→discard pretraining decoder/ground action adapter这一训练分支。拟2+2+2=6 gapDeep提案，条件共存为动作标注充分/执行预算紧仍可直接BC；forward失真和inverse失败分账，不声称量化瓶颈消除了future leakage。需非作者source→owner和文件授权，未写Books。

### 16431 Grokking avalanche：几何诊断不等于泛化门禁

[官方HTML v1](https://arxiv.org/html/2604.16431v1)实际读II Methods、III.1–III.4及IV Discussion。梯度快照进入固定BA图上的阈值扩散，跨width拟合最大avalanche的FSS D；shadow-probe保raw训练梯度，另有未grok及prime47对照。ModAdd59 80/20 split与XOR四样本无train/test split不是同一泛化协议，论文也承认后者是突变学习而非canonical delayed generalization。以观测test>99%的g对齐事后轨迹，不能把100–200epoch差异直接变成未知任务的可部署early-stop规则；D≈1还出现在Gaussian null。

拟2+1+2=5标准完成/仅报告：有具体gradient诊断协议及negativecontrols，但不采普遍critical manifold或stop证书。Ch5已有probe诊断与heldout/干预分权，本文实现未证明足以改变长期设计；不冒称BA probe全部算法已写在书中。硬件/precision Not Disclosed，不报告吞吐。

### 16453 SMC：精确形式目标与实现近似必须分开

[官方HTML v1](https://arxiv.org/html/2604.16453v1)实际读§3.1–3.4 Eq4–17/Alg1、§4.1/4.2/Table1及§5。定义的lookahead full future sum可给精确边际；实际H有限MC、N16/J2/S2与reward-selective duplicate MH不是直接取得该和。Eq17包含proposal importance ratio，**不能误说缺importance correction**。真正需隔离的是SMC TargetI prefix与MH TargetII lookahead切换后没有给整体同target修正，以及独立重估当前/提案L的ratio没有说明extended-state pseudo-marginal保持；无偏L估计也不独立证明这个ratio kernel exact。

最小target区别：两步第一token A/B各.5、A后续确定/B后续均匀、alpha2/reward全1，TargetI第一步边际(.5,.5)，TargetII为(2/3,1/3)。§3.4称两者切换，但未给重权如何匹配该差别；这是实现分布保证未建立，不是否定Eq9定义或全部SMC理论。MH还可能接受较低target-density提案，不能采用‘只接受真正更好trajectory’保证。三7B、3072max、vLLM、reward/verifier额外成本；HumanEval用unit-tests+syntax但未区分search tests与evaluation tests，baseline主要继承priorwork、walltime/hardware/precision未披露，不采用优于GRPO或144Ktoken排除更多计算因果。拟2+2+2=6纠错Deep、中心exact实现声明暂缓，不进Books；可保留有限经验与形式目标说明。恢复需一致target/selection kernel/MC状态证明及复核用test划分，不扩全附件。

### 16456 EchoChain：接纳信息与让出话轮不是一回事

[官方HTML v1](https://arxiv.org/html/2604.16456v1)实际读§1配对控制、§4.1–4.3、§5–7。speech onset固定offset注入相同barge-in、保持context，并按rubric核新信息/旧约束/原目标；48对话×4模型配对的92→55failures不是全部200对话的代表性因果效应。收集先flag失败→human筛有效性→同rubric比较四endpoint，selection与judge false-negative影响分母。全部speech预合成与planner依live history的文字存在执行顺序张力，不能据此声称任意交互完美matched。voice preference不显著也不证明等效。

拟2+2+2=6标准完成/已有覆盖，具体Ch66‘Duplex Agent Evaluation要联合测Timing与Content’已把continue/adapt/yield和uptake evidence分开，§用户途中修订的配对轨迹已要求更新位置与原目标保留。该文是受限独立例证，不为三类新名称重复写书。四closedendpoint/200受控对话只测state-update，未测acoustic latency/prosody和生产并发/SLO；不把MPR<50%推广所有实时模型。

apr02已实际独立核16391§3.1–3.4/Table4/9/AppA.2/A.3与现Ch26具体段，确认6分gapDeep；discard decoder/fixed-forward更新边界与Table5数字不一致的警告通过。16453必要Eq7–17/§3.4/Alg1已非作者核：Eq17含importance ratio，两步TargetI/II边际差反例与无全局重权桥、MC状态缺口支持6分窄争议，只隔离实现exact保证，不否定形式fullsum/全部经验。两项没有Books实写，非日Gate。

随后16431/16456亦完成apr02有限实际原文→owner对读：前者ModAdd/XOR协议、事后g、shadow-probe/null限制支持5分标准仅报告；后者§4–7与Ch66 Duplex三态/uptake及途中修订真实正文支持6分标准已有覆盖，保留48×4选择后子集、执行顺序张力与p=.63非等效。均非整日报独立验收。

## 16462 / 16469 / 16471 / 16475：有限必要证据

四项官方abs/v1均已读题摘、history与可见说明，未见withdrawal。库存v1 Updated分别为`2026-04-21T00:03:49Z`/`00:03:56Z`/`00:03:58Z`/`00:04:06Z`，OAI均04/21；提前Submitted为04/08、04/09、04/10、04/11，仅作提交来源，不改名公开。与既有ID分配/相邻批次/官方槽组合推断本窗08–09，非单证。必要正文累计39家族，完整题摘仍270；以下是作者判断，不是日级Gate。

### 16462 HalfV：冻结视觉更新和删掉视觉读路径不能互换

[官方v1 HTML](https://arxiv.org/html/2604.16462v1)实读§3.1–3.3、Table2/3/6/7、§5.3/7与AppA/B.4–B.5。Gram截断entropy仅为几何proxy，不能证明普遍三阶段或排除视觉前端因果。早层attention anchor+FPS后，深层对LLaVA保留视觉读路径但停更新，对Qwen仍更新少量视觉token；同一冻结策略在Qwen显著失败，删全部视觉token在LLaVA OCR失败。Ch23已有几何稳定≠可删、分层剪枝，但缺这组**更新责任与读路径分开、且选择依backbone**的受限反证。拟2+2+2=6、知识缺口Deep提案，未写Books。

限4B–13B、白盒hidden-state与所测基准；Table6 Qwen POPE质量下降，不称无损。AppB.4的硬件字符串是“RTX4080SUPER(32G)”且runtime组合需恢复确认，不当可信生产配置；不采用4.1×FLOPs为时延，selector开销不可忽略，precision/batch/concurrency/SLO未充分披露。若独立审阅不支持长期缺口，可保留仅报告，不因已读而强写。

### 16469 B-PASTE：分支效用调度是提出的机制，不是已验证干扰隔离

[官方v1 HTML](https://arxiv.org/html/2604.16469v1)实读§3–7/Alg1、§8–9。推测对象从单调用到有状态bounded子图，q乘overlap/unlock/interference效用；先promotion与authoritative资源保护，再按slack admission，stage-write留commit barrier。不同于只按预测概率启动单工具，但COW/staging不能独立证明外部副作用安全。Thor类内部归一化观测没有model/workload/precision/latency-tail等充分配置，完整评价明确仍future work。拟2+2+2=6标准完成/仅报告该分支；Ch78 provisional-call/exact-match/side-effect已给一般边界，不冒称整个branch算法已有覆盖，也不采1.4×通用收益。

### 16471 Semantic Channel：闭包保真不是自然语言消息恢复

[官方v1 HTML](https://arxiv.org/html/2604.16471v1)仅定点实读§III-A、Theorem5.1及其proof、Remark5.15–5.16，未通读其全部理论。有限可判定知识库、固定推导系统与sender剩余完整KB是distortion对象：redundant消息可统一替换某core元素，因其余KB仍保留闭包；不能外推没有完整共享KB的Agent文本通信。

Remark5.16声称weak coverage `a∈Cn(receiver)`即存在一个receiver元素替换a而保sender closure，缺桥。固定规则`b∧c→a`、sender `{a}`、receiver `{b,c}`即可满足weak coverage，但单个b或c均不能替换a保`Cn({a})`。这只反驳该proxy存在性扩展，**不否定强H1的Theorem5.1及全部capacity结果**。拟2+1+2=5纠错Deep/暂缓这条保证，需非作者必要核；重开是proxy输出集合/条件及相应证明，不扩所有附件。Ch82已有通信载荷/先验/重建成本分账，不写普遍semantic-capacity承诺。

### 16475 SDLLM：脉冲重编码的算术能耗模型不等于实测Serving节能

[官方v1 HTML](https://arxiv.org/html/2604.16475v1)实读§4.1–4.4/Eq5–22、§5/Table3–12及AppA.1–A.2能耗定义。γ-SQP→整数count→T×D二元/三元脉冲展开→稀疏列累加，用representation长度和稀疏度换MAC，clipping进一步换质量；Theorem1的κ明确是X平方幅度，不误当量化误差定理。45nm MAC/AC常数给理论算术energy，未证明内存/控制流/实际chip或GPU端到端节能。

Llama2/3及Qwen14B、INT4/INT6局部QA/PPL，Table7复杂语言任务仍有退步；增大D增加质量同时增加展开工作。异步单步需要硬件支持，不等普通GPU自动低时延。拟2+2+2=6标准完成/仅报告这条具体执行表示分支；不采用15×实测power或全部量化baseline排序，未证明Serving latency/concurrency/SLO，Books不强加实现细节。

apr02已实际完成这四项必要源→实际owner/中心反例的有界非作者复核：16462 §3/Table2/AppA Eq8–11与Ch23:310–368支持6分gap提案，冻结视觉更新仍算完整K/V供文本读，Qwen少量继续更新的反向结果不能隐藏；硬件字符串不当已证设备。16469 §4–9/Alg1支持6分标准仅报告，future evaluation不写成已验证COW安全或1.4×性能。16471 Remark5.16/Theorem5.1与规则反例支持5分窄争议，强H1不被否定。16475 Eq6/AppA2支持6分标准仅报告，magnitude proxy与45nm算术常数不当量化误差/芯片实测保证。这不是完整日Gate，没有Books实写。

## 16481 / 16483 / 16484 / 16487：必要消歧后处置

官方abs/v1题摘、history和可见状态均已实际打开，未见withdrawal。库存Updated依次为04/21 UTC `00:04:16/00:04:20/00:04:22/00:04:26`；前三OAI current 04/21、末项04/22，不把current datestamp或提前Submitted当first-public。结合既有永久ID公告分配/相邻处理批次/官方EDT槽推断本窗08–09；必要正文累计43，完整题摘仍270，不冻结候选。

### 16481 ETC：把模块移除变成质量退化，不等于永久删除

[官方v1 HTML](https://arxiv.org/html/2604.16481v1)实际读§3.1–3.4/Eq1–7、§4.1–4.2、D.2、F.4/I。PCA+t-mixture以template embedding描述concept分布，affine transport给映射目标、低密度boundary给preservation anchor，再训练MoEraser；不是统计密度自动证明语义安全。NIR进一步扰动projector，再让模块恢复被扰动的生成路径，使只移除模块而保留corrupted projector的对手付出质量损失。它没有证明持有原始projector的白盒对手无法恢复、继续训练也无法绕过，不能称tamper-proof或concept从参数永久消失。

SD1.4/3.5-L、A6000/AMD7763、2072目标与保留池；CLIP/用户CRS不是语义删除证明，UD攻击ASR有明显残余，额外RARE又增加训练成本。Ch72:408–439已有module-integrity与训练隔离，2075附近已有erasure/refusal分权，但尚无“主动制造基座退化→module修复依赖→原权重恢复威胁”的责任分支。拟2+2+2=6、保护行为/知识缺口Deep，提案两段置Unlearning的旁路/retain-utility论证内：声明对手可恢复哪些artifact，分开模块移除测试与权重恢复测试。未获写锁、未实际Books，待有限非作者源→owner核；不强行写全算法。

### 16483 DSS：闭式校正只对声明的特征目标最优

[官方v1 HTML](https://arxiv.org/html/2604.16483v1)实际读§4.1–4.3/Eq3–15、§5/Table1–4。敏感PCA/KDE找中心及normal anchor，prompt条件融合anchor，再按feature cosine score触发沿normal−sensitive方向的闭式step。Eq13–14在固定方向、非退化条件下可最小化该二次surrogate，不证明最优语义安全；阈值来自正常max/敏感min也不证明两分布分离，benign drift需单独测。并非所有正常输入数学上保持原样。

SD1.4/2.1、50步DPM/CFG7.5、9概念/I2P与受限RAB，FID/AES/CLIP有退步，硬件/precision/并发/SLO未充分披露，不采用普遍91%或在线安全保证。拟2+2+2=6、保护行为定点深入完成/仅报告：保留具体runtime校正分支及有效性边界，现Ch72已有保留utility/域外未判定责任，当前证据不足以改变其长期安全判断，不冒称书中已有该算法。

### 16484 CLWM：真实观测记忆与预测工作记忆分开

[官方v1 HTML](https://arxiv.org/html/2604.16484v1)实际读§3.1–3.3/Eq9–16、§4/§5.2–5.3。TTT长期权重只接真实观测/已执行动作，工作副本接预测latent、ODE期间冻结；动作执行时预denoise，真实观测到达再校正。固定维度state只支持存储量不随episode长度直接增长，不保证无损历史、无限可靠推理或预测path换条件后保持正确。原文flow-time终点与pre-denoising方向表述也不统一；Gaussian history augmentation不构成所有替换条件下的稳定性证明。

64H100/20天、Wan2.2-5B、chunk16、50项模拟与受限真机；没有独立matched预算把各组件收益分离，生成simulation不等真实物理真值。拟2+2+2=6标准完成/仅报告这套条件性职责组合：Ch25:488–510已给可修订权重记忆、真实状态authority和漂移回退，本文未形成足以改变这些长期边界的新证据；不把完整实现称已有覆盖，也不采用效率定律、50%生产收益或无界部署。

### 16487 CLIP local geometry：细粒度重排仍依赖scene annotation

[官方PDF v1](https://arxiv.org/pdf/2604.16487v1)实际核首页与§4.2–4.4/§6.1–6.2、AppD必要负例；HTML同题名/机制可用。按scene annotation拆per-object text embedding，top-k后Hungarian匹配或FGW软transport，结构term并非几何真值：同对象词向量关系不自动代表空间位置。多对象平均steering有显著退步，Hungarian常优于FGW，局部候选扩大也非单调恢复；不能把本文结论里的邻域普遍更优照录。

Synthetic Shapes/Urban1K/CLEVR-HOPE/SugarCrepe、CLIP/SigLIP、200 query VLM nDCG与identity Recall协议不同，per-object annotation不是部署免费的感知；precision/hardware/端到端检索成本未充分披露。拟2+1+2=5标准完成/仅报告局部matching与composition反证，不写结构ranking普遍优于单向量或对原始图像全部成立。Ch76已有表达/打分/支持分权，但未声称完整承载本算法；本轮不为一个annotation条件的实现另造正文。

apr02实际独立核16481 §3.4 Eq6–7/F4/I与Ch72:408–439/Unlearning，确认6分保护行为/gap提案；只移除模块的受限威胁不含原projector恢复，UD/RARE成本保留。16483 Eq8–14/§5支持固定非零方向、合法λ条件下的二次闭式，6DeepOnly裁决通过，不证明所有正常输入不变。16484 §3.2/3.3与Ch25:488–510支持真实/预测TTT分权，但s0终点与0→1说明矛盾且augmentation不证明稳定，6StdOnly通过。16487官方PDF §4.3–4.4/§6.1–6.3/AppD与annotation/负例支持5StdOnly。这是四项有限非作者源→owner检查，不写Books、不验整日日期/Gate。

## 当前六项有限必要审阅：2026-09-27T05:14:22+08:00

完整题摘复读已计入原270，不新增初筛数；本批不是全库存深审。五个未撤回家族的库存v1 Updated依次为16492=00:04:31Z、16499=00:04:40Z、16503=00:04:45Z、16514=00:05:02Z、16519=00:05:10Z；只与永久ID公告分配、OAI/相邻批次及官方20ET槽联合推断，绝不改名为首发。HQA另有更早正式正文线索须单项隔离。

### 2604.16492v1 LayerCache

实际读[官方HTML](https://arxiv.org/html/2604.16492v1) §3.1–3.5、§4.1–4.4/Table1/消融及官方abs，未读全部附录。group hidden-state变化图指导timestep×group×JVP span分配，forward hooks保存group history，预算贪心优先高误差组；是具体刷新粒度/配置分支，不等网络真实velocity各层可独立相加或全局误差有保证。浅/中/深的平均与峰值不同，不能将深层一概写为变化更大；其Related Work本身列token/attention细粒度方法，‘所有旧方法整网单决策’不成立。

Qwen-Image60层、50步、1024²、CFG4、单A10080GB/BF16/CUDA12.2/PyTorch2.x，3prompt profiling、20prompt对uncached图像相似度；没有heldout profile迁移与并发/SLO保证。§4.1说B25，Table1 LayerCache标B30、MeanCache B25且1.37<1.54，故不采用预算匹配/同时更快宣传或全Pareto支配。2+2+2=6标准完成/仅报告受限schedule实现与代价，不冒称Ch24已完整承载该算法，也不凭通用cache命题强行写书。

### 2604.16499v1 HQA-VLAttack：日期/身份有界隔离

实际读[HTML](https://arxiv.org/html/2604.16499v1) §4.1–4.3/§5核心对照、[官方PDFv1](https://arxiv.org/pdf/2604.16499v1) 首页，未读20页全附件。PDF首页明确NeurIPS2025；[正式出版页](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f9bc7653cf176075e88203d1e83e8c65-Abstract-Conference.html)同作者/同题摘并给DOI10.52202/085713-5694、Paper/Supplemental；同家族[OpenReview正文](https://openreview.net/pdf?id=LZ4IKybwWl)亦检索到。当前forum/API两种原始替代均ChallengeRequired/403，未取得首次公开精确日期。不得将April arXiv新ID当同家族首次正文；本窗没有已证重要修订信号，保留更早owner恢复线索，暂不评分/Books。Eq7同号positive/negative cosine与文字相反目标只作待恢复原owner的定点问题，不在日期未闭时新造本窗纠错候选；不扩全年发表史。

### 2604.16502 撤回排除

[当前官方abs](https://arxiv.org/abs/2604.16502)明确withdrawn；v2在2026-06-04标withdrawn，说明未署名复用方法/代码。该日旧潜在准入撤销，只保留原始关闭依据，不评分、不selected、不采用；此前已读方法记录不成为正面证据。未删除其他有效材料。

### 2604.16503v1 Motif-Video：拟窄缺口，尚无写许可

实际读[HTMLv1](https://arxiv.org/html/2604.16503v1) §3.3 Eq2–4/Fig5、§6.2与§7.2。新增cross-attention以post-self-attention视频状态产生新Q，复用同层pre-attention文本K/V投影和已有tensor，Wo零初始化；不等全attention免费。两个零Wo路径初始化函数相同，raw-text直接KV与共享投影KV的后续训练稳定性不同，是‘函数保持不充分保证更新兼容’的受限分支，不采manifold因果定理。当前Ch23 Fusion零门保持段已有前半，却缺该KV兼容责任/训练对照；拟2+2+2=6知识缺口深入，两段嵌此处而非章末摘要，待非作者源→owner及root锁。

当前官方abs正常页可读v1历史（Submitted04/14T15:09:39Z只为投稿），精确abs/v1与PDFv1两次cache miss不冒充成功；HTML页为v1且中心机制无明确版本异常，当前abs不得当精确v1实验。零Wo比较仅定性训练图，组件完整规模消融缺失；§6.2为50步/121帧/1280×736/guidance8且低sigma尾未覆盖，attention余弦不是因果归因。保留训练预算/跨模型比较不能隔离组件、物理/时序失败，不采VBench headline或普遍稳定保证。

### 2604.16514v1 BARD：拟窄缺口，尚无写许可

实际读[HTMLv1](https://arxiv.org/html/2604.16514v1) §3/Alg1、§4目标、§5.3/Table2–5、§7；[官方PDFv1](https://arxiv.org/pdf/2604.16514v1) 首页/Alg1/§3.2/Table4核与HTML中心一致，不将latestv5事实倒灌。先从AR训练B4 diffusion anchor，固定anchor，在4→8→16→32扩块后蒸馏same-position/corrupted-state logits；AR clean-prefix next-token logits不是天然同一监督对象。Ch24现有AR teacher representation alignment与block质量取舍未承载这个logit状态兼容分支，拟2+2+2=6gap深入，嵌AR→diffusion/BlockDiffusion交接，待独立源→owner/root锁。

Qwen3-VL2/4/8B、最多4.4M监督；Table4主要4B三block、同数据/架构/优化配置，未给各法总训练FLOPs等价或生产SLO，不采用3×普遍吞吐。Diffusion teacher并非全部指标改善：ChartQA若干切片退步；progressive增加训练阶段与teacher成本，固定anchor也限制适配。论文单位名称含AIforScience不令通用VLM机制范围外，会议模板占位不当正式发表。

### 2604.16519v1 PODPO：中心解释窄争议，经验保留

实际读[HTMLv1](https://arxiv.org/html/2604.16519v1) III.B–C/Alg1/III.C.5、IV–V与官方abs。positive advantage筛选、每observ生成G=8 action、local attraction/repulsion加critic是明确替代更新分支，不因仅机器人模拟而拒绝；但无clipping保证不成立：其RV定义μ²/E[V²]实际是信号占比，固定均值下噪声减少应使此值增大而非更小；同actions多temperature场相关，Var(sum)缺covariance桥。另Alg1只说stop-gradient V，而target=x+V若x两侧都求导会抵消梯度；III.B全target stopgrad与III.C描述须澄清，不能推断公开实现必然零梯度。

2+2+2=6纠错深入/争议/暂缓，隔离中心推导与实现声明，不否定Genesis GO2/舞蹈经验。4096/16384parallel environments、448步无历史输入、G4崩溃/G16更慢与后期jitter均保留；seed/hardware/precision/匹配总训练成本不足，不照录6.7%普遍收益、proactive prevention或PPO必单模态。重开仅需合法covariance/RV解释与完整target stopgrad实现，不索全部引用。

apr02已实际独立核本组六项：LayerCache §3.4/3.5/4.1/Table1/4.3支持6StdOnly；PODPO III.B–C/RV方向与完整target差别支持窄争议；Motif §3.3/Fig5与Ch23 Fusion支持6gapDeep，但Fig5同时改变Q与KV，不能唯一因果归KV/manifold；BARD Alg1/§3/Table4与Ch24现文支持6gapDeep，ChartQA负例及总预算未matched保留。HQA正式页同family及撤回状态亦实际核；这是有限source→owner，12提案尚无Books实际写入，不是日Gate。

## 16515 / 16521 / 16524 / 16529：必要处理与日期例外

270完整题摘不变，必要/最小正文累计53；只当前四项，不扩附件。16521/16524库存Updated分别04/21T00:05:13Z/00:05:23Z、OAI04/21，与永久ID公告分配/邻批/官方槽组合可推断08–09；Submitted04/16不是公开。16515库存v1 Updated实际07/13T00:22:24Z、无OAI当日；16529为04/22T01:08:07Z、OAI04/22：当前没有支持04/21精确落窗的本家族组合，不据连续ID替它们确定归属。

### 16515 PriceBlind：机制可核，但本窗日期证据未闭

[官方HTMLv1](https://arxiv.org/html/2604.16515v1)实际读§3.2–3.6/§4.1–4.3/4.5–4.7/F、[abs/v1](https://arxiv.org/abs/2604.16515v1)读history与可见状态。商家图像控制之外，优化还需截图/稳定布局/目标坐标，单轮coordinate transfer不是闭环交易；CLIP anchor+action loss的受限攻击可核，cross-attention/CoT均不是内部因果证明。200E-ShopBench、Mobile-Agent-v2/AppAgent及三closedAPI；VtA降低ASR同时降低clean accuracy，precision/runtime/SLO未充分披露。Ch72已有图标内容无害但grounding错误与可信目标独立校验，本文可能提供独立受限反证，但Submitted04/15与July v1 processing不能确定首公开。本窗不评分/不Books，不推断July就是首公开；恢复仅需该family原始公告/首次正文公开区间及v1身份，不展开ACL全届。

### 16521 CAMP：回溯改写未来请求不能清除已发送日志

实际读[PDFv1](https://arxiv.org/pdf/2604.16521v1) III.D–F/IV.B–G/V.C–E/VI，HTML同中心但标题措辞不同，必要采用以PDF为准。CPE按entity-type图加权触发，阈值前消息原样送外部API，之后改写本地历史；威胁主体却能读取所有API request logs。因此已发送前缀没有被远程删除/撤销，不能从后续伪名化推出累计日志real-PII暴露为零。TableIV四scenario CAMP0与该声称的累计对象不相容，若实际只测最后请求，应明确改分母；不是否定未来请求最小披露价值。ClaudeSonnet4.6/Azure、四合成scenario/三阈值/alpha.3，coherent response非独立utility评估，weight未校准成重识别概率。2+2+2=6保护保证纠错Deep暂缓；Ch72 trajectory ledger/sink边界已要求跨释放记账，不能采用CAMP零泄漏。恢复只需逐轮实际payload/log exposure定义及必要删除责任/更正结果，不要求全部代码。未推断全家族虚假或所有utility无效。

### 16524 Anumati：可审计同意链不等实际遵从证明

[官方HTMLv1](https://arxiv.org/html/2604.16524v1)实际读§3.1–3.6、§4.1/4.3–4.4与§6.1–6.2、abs/v1状态。PolicyDocument hash/version→完整ParsedClaim→per-action AdherenceEvent与capability fingerprint失效，callee按disputed/understood阻断skill，具体协议分支可描述；S1–S7是TLC模型内状态property，不证明模型真正理解/行为遵从，调用方fingerprint与reasoning均self-report。§4.3微基准不含network/TLS，JWS验证未实现；两Gemini2.5Flash agents demo非敌对广验证，35tests未由本轮复现。2+2+2=6、保护行为定点Deep仅报告，不采用legal-compliance或开放tamper proof；Ch84 run consent/version与Ch72 policy/effect authority是一般现文，但不冒称全ACAP算法已有。该提案在共享信任组织内可试，当前证据不改变现有独立effect要求，未创建书稿diff。

### 16529 Agentic Coding Scaling：条件摘要复用，不是环境状态复用

实际读[HTMLv1](https://arxiv.org/html/2604.16529v1) §2.1–2.4/§3.1–3.3/§4.1–4.2、[abs/v1](https://arxiv.org/abs/2604.16529v1)history。独立容器rollout→compact summary→小组递归投票→K summaries条件化全新环境，是信息复用而非共享已执行副作用。N16/T2/K4/G2/V8、SWEVerified全测试与Terminal88/89；100task randomK/selectK对照仍受选择质量和额外投票/summary成本，强rollout与后续表现相关不证明唯一因果。文中步骤下降不等总token/cost降低，硬件/precision/API预算/SLO未披露。Ch81恢复联合状态与advisory memory未完整承载本方案，但日期当前只有Apr22处理记录，SubmittedApr16不能倒填Apr21。潜在贡献保留日期隔离，不评分/不写Books；恢复官方首次公开组合即可，不索全引用/旧新版。

## 16535 / 16536 / 16555 / 16557：本轮有限必要判断

实际访问2026-09-27；完整题摘仍270，必要/最小正文增至57，不等57候选。前三正常未撤回条目的库存v1 Updated分别16535=04/21T00:05:42Z、16555=00:06:22Z、16557=00:06:26Z；16535当前OAI04/22、16555为04/21、16557空。与永久ID公告分配、已有相邻批次、官方EDT公告槽共同作08–09有据推断，不把Updated孤证称first-public。16536库存Updated07/14T19:49:17Z/OAI空，不能随连续ID归入本窗；日期隔离。

### 16535 SCATR：轻量排序器成本与全部采样成本分开

[官方HTMLv1](https://arxiv.org/html/2604.16535v1)实读§4.1–4.2/§5.1–5.2/Table1–3/§6；[abs/v1](https://arxiv.org/abs/2604.16535v1)题名/history已核。每model/domain单独训练小MLP，以倒数第二层最后non-padding token状态预测unit-test/answer correctness，然后BoN或weighted voting。它是具体可部署条件的selector operating point，不证明内部知道或错误率在跨域已校准。N16、三calibration重采样、heldoutearlystop、Qwen1.7B/14B/30BA3B、OLMo7B/GPTOSS20B、代码/数学单轮。Table2小Qwen HumanEval准确率反例及更大N在数学可能退化保留。

0.15–0.20ms是scorer局部延迟，不含16次生成、hidden export/storage、标签/校准训练、网络和发布验收；硬件/precision/concurrency/SLO未充分给定，不采用1000×端到端加速。Ch66现accepted-selector×coverage分账与probe不取得correctness authority仍适用，本文不提供改变此设计判断的独立保证；其具体小MLP实现不冒称书稿已全覆盖。2+1+2=5标准完成/仅报告，待有限非作者必要核，不写Books。

### 16536 Unlearning Testing：有条件干预路线，但公告日期未闭

[官方HTMLv1](https://arxiv.org/html/2604.16536v1)实读§3/§4.1/§5，官方abs/v1题摘/history可读。预算化目标/mediator干预→原输入与干预输出对比→path leakage排序；proxy/cancellation/subgroup可造成全局attribution盲点。Oracle依赖DAG和有效干预，成人收入/药物/半合成心脏表格数据、删特征后重训只是unlearning代理，不是LLM删除验证，§5明确foundation-model干预为future。具体机制可能相关，不因表格/小规模关闭，也不宣称因果识别或全面无泄漏。

本家族July processing/OAI空和HTML页眉April16仅投稿信息，未形成本窗官方首次正文公开组合；保留日期终态隔离、不评分、不Books。恢复限该家族官方公告/首次正文可用区间与必要版本身份，不从FSE2026会议月份推首发或展开全届。

### 16555 LLMasTool：粗搜索权与局部语言决策分开

[官方HTMLv1](https://arxiv.org/html/2604.16555v1)实读§3.1–3.3/§4.1/§4.3/Table2–3及AppC.2/Table6、C.3/Table7、C.5/Table9，abs/v1身份/可见状态已核。从nn.Module代码挖tree，再由算法采operation/template/node/module、LLM补残余参数；E(exec,const,intend)判可运行/资源/所请求变换后才训练计分。受限随机粗决策胜LLM主导有独立反例，不能采用‘算法挖掘100%正确’或更大模型必然因memorization更差的因果。

Qwen3-8B、NAS-Bench201/小图像模型≤1.5M、ImageNet100≤2M/0.3GFLOP，100/500架构、主要one-epoch消融；Table6随机选择位置/模块也更好，后100epoch对照另分账。Ch81 canonicalDAG/typedmutation、外部可执行评估与searchholdout已承载长期控制边界；本文具体树搜索实现不等全已有，但局部证据未改变该设计结论。2+1+2=5标准完成/仅报告，不外推大模型NAS或搜索稳定保证。全training/searchwallclock、硬件、precision/SLO未充分披露。待有限非作者。

### 16557 S-GRPO：专家注入不自动成为纯on-policy估计

[官方HTMLv1](https://arxiv.org/html/2604.16557v1)实读§4.1–4.3/Eq4–7、§5/Table1–2、abs/v1身份/history。全失败组替换一条为GT、固定maxreward、混合group归一化，再在成功组取消注入，是可研究的conditional监督分支；Ch33现统计anchors/失败组SFT分流并非此完整算法。Eq7仍把混合组写成由πold生成，专家deterministicreplacement却不服从该律，称pureonpolicy/无偏行为克隆没有相应proposal/权重桥。只隔离该保证，不声称bootstrap梯度必然无效，也不否定全部经验。

Qwen2.5VL7B、Qwen3-4Bsemantic verifier、COCO/Geo/OpenI有限视觉posttraining；§5把人工GT/语义threshold与严格binaryverifier混称，Table2δ=1 general能力退步，Table1若干domain指标不全面最优。seed、总训练/验证预算、硬件precision及SLO未充分给出，不照录SFT一定灾忘或本法保证不忘。2+2+2=6纠错定点深入/暂缓中心采样解释；恢复需真实mixedproposal/目标与conditionalreplacement权重或明确改称混合监督heuristic，不索全部代码/文献。尚待有限非作者，不写Books。

## 16543 / 16565 / 16571 / 16576：2026-09-27T06:02:29+08:00 有限必要审阅

完整题摘仍270，必要/最小原文累计61；本组四项尚待有限非作者，不等日Gate。均实际打开官方abs/v1核标题、history与当前可见说明，没有新增撤回。库存v1 Updated依次00:06:02Z、00:06:37Z、00:06:44Z、00:06:52Z；OAI当前分别04/21、05/28、04/21、04/21。结合已核永久ID公告分配、相邻批次与官方EDT槽推断08–09，不将Updated或Submitted改名首发，也不因OAI后更新强制回拨。16565当前v3不是本次采用版本。

### 16543 Conjunctive Prompt Attacks：组合激活不是实际特权效果

[HTMLv1](https://arxiv.org/html/2604.16543v1)实际核§3.1–3.7、§4、§5、AppC.1–C.2/C.6/C.11–C.12必要定义与反证。用户key与远端template单独不触发、合流触发，四条件clean/key/template/both分开，star/chain/DAG中的routing exposure是具体攻击评价分支。可是§3.5把ASR定义为compromised output出现`__ACTIVATED__`，示例为模拟特权行为，没有独立unauthorized tool-effect。工具allowlist后仍出现marker，不能推出真实工具授权被绕过。

rho是优化中的独立标量；C.2声称对应提示导致的emergent routing bias，但不能仅由调rho证明已能在固定生产router实现相同控制。§4正的lambda3 Ptemplate项本身是惩罚而非单独促进，总目标不能据一句符号直接否定。20 role/50 episodes、小open models与有限closed transfer；precision、端到端成本/SLO未充分披露。2+2+2=6保护边界深入/仅报告，保留组合评价而不采用开放安全失效保证。Ch72已有片段合流后新执行身份及effect authority，本文marker不能改变这条设计判断，不冒称全攻击算法已有。

### 16565 BMC：重构稳定性仍是同源selector signal

[HTMLv1](https://arxiv.org/html/2604.16565v1)实际核§3.1–3.2、§4.1–4.3/Alg1/Eq14、§5.1–5.4/Tables1–3与AppB必要限制。同模型mask→reconstruction的六分数加权形成BMC，阈值接受/否则重采样，失败后返回最大分数；这个conditional self-check有具体分布信号，不是独立truth。RL Eq14明确GT correctness gate，不能把此训练写成完全无监督的自证reward，也不采用稳定高密度必正确或各f-divergence等价普遍保证。

LLaDA8B/Dream7B、四推理集、mask .9/K16、MiniLM语义score、阈值.75/max10；Table2 Dream GPQA guided低于BMC-BoN，Table3部分GPQA低于OutcomeRL。K16是每次重构的16个去噪步骤，不是16条独立重构样本；sample efficiency未把每次检查额外16步重构、encoder打分、最多10次生成重试、训练与wallclock统一计入，不声称免费验证。hardware/precision/concurrency/SLO未充分披露。2+2+2=6标准完成/仅报告受限诊断和selector分支。Ch66实际“低熵与高共识稳定地错”与accepted-selector分账仍成立，不冒称全部BMC算法已覆盖，不写内部知道或普遍幻觉消除。该窄命题及修改已获apr02必要源非作者核，不等日Gate。

### 16571 EquivFusion：跨IR等价只在已建模位宽和展开范围内

[HTMLv1](https://arxiv.org/html/2604.16571v1)实际核§3.1–3.2/§4.1–4.4、§5.1–5.2及AppC/E.2必要适用域。不同前端lower到MLIR/CIRCT common logic、I/O配对构建miter、SMT/BTOR/AIG检查，是具体translation/verification实现分支。UNSAT支持所建模integer/fixed-bitvector、静态affine loop和有限sequential展开，不能无条件承接前端语义正确、任意时间协议或大模型浮点正确性；SoftFloat仍future。

8uint排序、2维8bit PyTorch dot/netlist与输出32bit sign-extension反例；静态数组/限制pointer/control条件明确。硬件/precision以该integer语义解释，Serving length/batch/concurrency/SLO不适用，求解总资源未充分披露；未复现工具。2+2+2=6标准完成/仅报告受限cross-abstraction artifact，不宣称已验证LLM kernel或将所有compiler正确性移交solver。ROADMAP编译/执行owner为Ch49，不是Ch39 ZeRO；本轮不据一个受限tool demonstration强造Books正文。

### 16576 dense retrieval robustness：相关几何不能直接成为训练目标

[HTMLv1](https://arxiv.org/html/2604.16576v1)实际核§3/§5/§6.1–6.2/§7.3/§8.1–8.2及Limitations。九模型/30英语数据的mixed-effects、query扰动与white-box poisoning分轴；不把不同checkpoint/pooling/instruction的比较归因为reasoning训练一项。Synonym规则不自动保语义，ASR@20只是poison被检索不是最终QA攻击。direct-transfer低ASR不涵盖surrogate黑盒。

§8.1对Qwen3-.6B/MSMARCO作angular penalty和bidirectional conversion；几何确变而robustness未一致提高，是有限独立反证，不将几何correlation当因果或普遍否定双向attention。Ch76现domain/relevance与表示成本未声称该具体控制实验已全承载；本篇受限selection证据不足以规定通用encoder目标，因此2+1+2=5标准完成/仅报告。默认exact FAISS非ANN生产，完整硬件/precision/latency/SLO未充分披露；保留English/有限模型/未公开GTE训练及perturbation有效性限制。

## 16583 / 16584 / 16585 / 16587：有限必要方法与真实章节差异

恢复后的有限非作者追加：apr02已实际核16515/16529/16521/16524、16535/16536/16555/16557、16543/16565/16571/16576必要命题/反例。CAMP先前“阈值前消息原样”只适用于非hardblock类别；hardblock从turn0保护不受日志反例否定，已在Report同步。BMC K16已改为去噪步数。其余历史“待非作者”句是当时checkpoint，不表示这十二项仍待审；不由这些单篇通过推日Gate。

2026-09-27T06:11:01+08:00。完整题摘270不变，必要/最小源累计65；新增两项作者证据Only终态，另外两项是普通Books提案待独立source→owner、锁和写后，并非已采用。四family的库存v1 Updated依次04/21T00:07:07Z、00:07:08Z、00:07:10Z、00:07:13Z，当前OAI均04/21；官方abs/v1题名/history/可见状态已实际打开，无新撤回。仅与永久ID公告分配、相邻批次和官方槽组合推断08–09，不将单证改名first-public。

### 16583 POLAR：驻留改变探索代价，路由改变未来反馈

[HTMLv1](https://arxiv.org/html/2604.16583v1)实际读§2、§3/Alg1–2、§4.2 Assumptions1–2/Theorem4.2与§5.1–5.4；不声称逐行全证明复现。快路由从全adapter library取quality/UCB减cold penalty，慢epoch选择resident set；forced exploration提供缓存识别所需反馈，doubling减少反复churn。Ch56实际routing/placement/scale交接与Calibration Routing State已有时标/反馈，但未承载cache placement直接影响探索可见性与router反向影响cache估计这一闭环。拟2+2+2=6知识缺口Deep，在routing交接附近窄补，Ch54只接resident bytes；无锁、不写Books。

15 Qwen2.5-7B adapters加base、r8–64、50–656MB；RTX5080/PEFT20次load仅校准291–1263ms，五benchmark logprob衍生utility结合synthetic power-law request、线性reward、K5/d5/H200/five seeds是模拟，不是完整Serving trace或TTFT/P99/SLO。理论依赖IID/full-rank、可缓存hot set覆盖/margin/separability和exact SolveCache；实际greedy不能直接继承sublinear保证，forced exploration与cold routing也有成本。保持静态已知quality/驻留集合和常规LRU的成立条件，不采用“memory不减慢学习”普遍结论；precision/输入输出长度/concurrency/SLO Not Disclosed。

### 16584 LeetProof：完成形式证明，不等规范已经正确

[HTMLv1](https://arxiv.org/html/2604.16584v1)实际读§2–3、§4.2–4.4、§5.1–5.2、§6.1–6.4/§7。生成spec先过type/LLM/PBT的precondition、postcondition与确定性输出唯一性，再把Velvet/invariant/VC交给不同证明模式；PBT没反例不当最终certificate，Lean机器证明仅对形式spec有效，不能越权证明NL intent。这里multi-modal是证明模式，不是视觉模态。

§5.2 reference defect与§6固定预算提供独立受限实例，但不改变Ch66现reference/oracle完整性、vacuous equivalence与budget分账责任；该具体分阶段工具不冒称现文全实现。2+1+2=5标准完成/仅报告。GPT5.2/Opus4.6、50算法题含15development/35evaluation，$5只code/proof不含spec生成；4题Lean已证明而Velvet只部分，15development选择/额外Aristotle预算/非并发IO程序限制均保留。M4 PBT局部时间不是LLM端到端加速；输入输出长度/precision/concurrency/SLO Not Disclosed，不采用全部开放软件正确性。

### 16585 GNWM：离散锐度保持与转移正确性是两个目标

[HTMLv1](https://arxiv.org/html/2604.16585v1)实际读§3全部公式/Listing1–2、§4、§5/§6.1–6.5及结论。Softmax后L2、batch mean的均匀方向项加WTA项与predictive alignment、固定Gaussian邻域组织；推理argmax grid snapping把连续预测强制投影到onehot，可减少模糊累积，却不证明选中节点或其物理转移正确。单球1200frames、15×15网格/四action随机游走、双球双channel及40词32D合成语法只验证有限设置，未给开放物理因果识别、所有state组合或无限rollout稳定性。

2+1+2=5标准完成/仅报告具体训练/离散rollout分支，不采“任意D唯一全局最小已由训练达到”或“仅噪声/消失实体失败”。§3.2 lower-bound需均匀onehot可行条件，有限Softmax严格正输出与有限batch也限制精确达到；不能以某个p=z子集值直接否定全可行域的global bound。Ch25既有state预测/真实observation authority不等该算法全已有；本文受限锐度示例不足以改为通用物理可靠性结论。hardware/precision/seed/匹配训练成本与SLO Not Disclosed，未复现实验。

### 16587 vStream：把昂贵干预标签摊销成在线排序sensor

[HTMLv1](https://arxiv.org/html/2604.16587v1)实际读§3.1–3.6、§4.1–4.3/Table1–2、B.8–B.9、Alg1–2/E.2与F.3.1/Table8–9必要段。DINOv3/Ward regions→跨layer/head pooled attention→以32随机region-mask造成的logprob变化训练Pearson目标linear estimator→按completed span异步输出。与直接attention当解释不同，它先用干预标签校准映射；Ch66 Interpretability Graph实际只组织patch effect为graph，尚缺“干预模拟器作为amortized sensor”这一分支，拟2+2+2=6知识缺口Deep、在diagnostic authority附近两段，待独立准入/锁/写后，不先采用。

correct-answer训练选择、Pearson与LDS只支持相关排序，不给绝对effect校准或开放reasoning causal faithfulness；mask/region/granularity/teacher-forcing prefix及模型版本必须共同保留。四7–9B VLM/五类别、32mask离线labels、A100局部latency与single-configuration seeds不能变成全生成免费成本。生成attention原本计算不等其全矩阵导出/存储免费；E.2 `output_attentions=True`与F.3.1 SDPA/Flash兼容声明未给真实materialization路径，表中每token attribution时延不充分证明部署backend/总SLO。DINO preprocessing、标签、queue/backpressure、span结束等待与错误答案shift需另验；precision/input-output lengths/batch/concurrency/productionSLO不完整。不采用117×端到端加速、attention天然faithful或绝对因果分数；原始定点干预仍高风险fallback。
