# 2026-01-13 增量准入独立校准（2026-10-07）

## 范围与实际层级

本轮独立复核者 `jan10_books_audit` 已切换到新的 Jan13 上下文，重读当前 AGENTS、Research/Report 合同、Prompt、Daily 来源说明/组、ROADMAP 与相关停点；不继承 Jan10 原证。为 root 后续指定的首七项 Books 写前 PRE，又完整读取 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE 和各实际 owner 的局部完整邻接。本笔记独占写入，不改报告、Books、README 或 LEARNING_STATE，不 stage/commit/push。

与作者 `supp_jan13` 确认本次完整题摘集合冻结 **46 = batch1 10 + batch2 32 + batch3 4**。实际独读三个 JSON 的全部完整 title/abstract；来源为同目录 [batch1](abstracts-new-batch1-20261007.json)、[batch2](abstracts-new-batch2-20261007.json)、[batch3](abstracts-new-batch3-20261007.json)。46 是具名完整 AB 判断集合，**不是 46 候选、46 Evidence PASS 或整日 coverage**。本日原 50 不动。本补查采用 Jan12 完整自然日窗口，与原报告窗口分账。

作者合并本轮纠偏后的分层为 **25 待必要证据候选 + 5 低分候选 + 9 贡献前关闭 + 2 窗前 + 5 日期 held = 46**。原作者 13 负侧中重开 DTI/DOM 为低分候选，Rotate/TREC 为准入；原四边缘中 MoleSyn 准入，另三低分关闭。这里只确认贡献准入与指定命题的必要原证，未授 DAY、整个来源完整性或 Books POST。

## 原 22 个清晰入口：完整 AB → 可改变的设计选择

以下均通过具体贡献入口校准，不从 title、topic/node 命中或实验宣传反推；除后文首七 PRE 外，不在此表宣称独立必要证据全部完成。规模、局部/理论/负面结果不构成前置排除。

| ID / 家族 | AB 的具体增量 → 设计选择；限制 |
| --- | --- |
| 05684 FLRQ | 固定 SVD/rank 的离线成本 → rank-1 sketch 与层别 rank 停止 → 残差修正分支的预算；amax 不是任务全局最优。 |
| 05607 DHPO | token/sequence ratio 的粒度差异 → 分支各自 clip 后 mix，entropy detach → 选择更新单元与混合；不是创造 token 因果 credit。 |
| 05848 GoalForce | 只给文本目标的弱控制 → force-vector 条件接口 → 显式目标到视频动态；不授物理因果规划。 |
| 05866 FACTUM | 输出 citation 不能揭示内部使用路径 → attention/FFN/update 特征 → 风险 sensor；不是 support truth。 |
| 05688 SketchVL | 全轨统一终局 credit → 居中的 PRM/action-KL step 信号与 signed clipping → 训练 credit 分支；绘图接口本身不能重算为新贡献。 |
| 05588 ARR | NTP 不等 ranking 监督 → item 权重与 trie 未来 ID 质量 → 标识生成的排序覆盖；表达能力定理不授有限模型学会。 |
| 05589 ACR | 无差别保留/压缩历史 → 明确 refactor 算子与干预策略 → 何时重塑上下文，而不是一律加长推理。 |
| 05384 Conformity | 单独近乎正确仍会受 group 条件影响 → unanimity/difficulty 控制 → vote、来源独立性与协作预算；不把受测人群模型当现实风险率。 |
| 05420 NoisyJudge | RG 误分类反演方差 → EIF/PPI++ 条件等价 → calibration estimator 选择；human preference 不是客观正确率。 |
| 05437 Moral | dense/macro 与 sparse/micro 效果不同 → geometry 条件的真实干预 → 按纠缠选择 actuator；不是道德或安全规范证明。 |
| 05693 Circular | 等到重复已输出才处理 → semantic/attention 前兆与 CUSUM → 早期循环诊断；前兆不是唯一因果。 |
| 05776 Romanization | 低资源罗马化经验不能直接泛化 → 从零、mono/multilingual 脚本控制 → 信息损失与共享词表取舍。 |
| 05858 CLewR | 各难度只消费一次 → 每 epoch 重访固定 easy→hard 全数据 → 训练支持反复暴露；不是 optimizer reset 或已证遗忘机制。 |
| 05913 SubDistill | 全教师能力 KD 非必要 → 指定层/类别子空间 → 按目标子任务保留表示；不因非 LLM 域自动关闭。 |
| 05939 CEI | 视觉答案 commitment 深度与上下文使用 → last-input hidden injection → 静态 actuator 与动态风险 sensor 分开；Eq8 原式冲突需隔离。 |
| 05487 EvidFuse | 先写完叙事再补图会冻结 claim → request/suspend/实际 chart-caption/resume → 证据到达与叙事顺序；非事务提交协议。 |
| 05513 LEAPS | 扩 query 增 recall 也增噪声 → 多 query 训练与下游校验 → 检索多样性/过滤预算；应用域不抹除机制。 |
| 05675 CHDP | 混合 discrete/continuous action → 条件双 diffusion 与 Q-guided codebook → 动作因子化训练；不是 Agent 协作机制。 |
| 05882 PreferenceShift | source preference 目标不保证 OOD → objective×adaptation 比较 → 目标选择的分布边界；不可按实验未定关闭。 |
| 05729 TAGRPO | 通用 diffusion GRPO 不能直接给 I2V 对齐 → shared-noise/intermediate latent 高低层目标及 bank → 对齐粒度与复用有效性。 |
| 05810 SceneFoundry | 场景看似合理却不可交互 → object-count/articulation/collision/walkability guidance → 功能几何约束；不收无限世界宣传。 |
| 05966 VideoAR | whole-clip 路径代价与时空依赖 → frame/scale AR、3D tokenizer、RoPE/校正/mask → 时空因子化和状态；非通用真实世界 simulator。 |

## 九项准入歧义：fresh exact-v1 定点原证

只打开影响贡献判断的核心、直接评价/反侧；HTML 优先，Im2Sim HTML 不可用后只恢复 exact-v1 PDF 核心，不遍历附件。以下原文已实际读取，作者可复用同版本同命题层；新的性能/实现 claim 仍需其必要证据。

| 家族 / 处置 | 已读原证位置、窄命题与反侧 |
| --- | --- |
| RotateCharacter05722：新增候选，拟 2/1/2=5 | [v1 §3.2–3.3、§4.4–4.5/Fig7](https://arxiv.org/html/2601.05722v1)。canonical A/T 静态阶段，再 camera encoder 冻结 base/联合训练，再 orbit；Plücker 条件本身复用已有路线。无 stage 划分的 joint 路径忽略 camera 是具体 disentangling 对照，不能因角色生成域前置关。反侧：主要定性 stage 对照，46K proprietary characters/120K videos；不能据 Fig7 证明预算匹配、唯一因果或全部 backbone 泛化。下一必要证据只围绕 stage/control 及成本，不需全附件。 |
| TREC Podcast05603：新增候选，拟 2/1/2=5 | [v1 §3–4/Table1](https://arxiv.org/html/2601.05603v1)。原单 assessor qrel 与 LLM qrel 的 ranking 稳定性按年不同（2021 τ约 .41–.62）；22/826 高分歧样本三名 IR 人员重判倾向 LLM，足以重开 gold-label 权威/排序稳定性负侧，不能仅因重复2002原则关闭。反侧：样本是选择的高分歧子集；原 assessor 可听 audio/相邻上下文而 LLM 读 transcript segment；prompt 用10%调 agreement，量化模型，grade4合并。不能授全人口 LLM胜人工或 gold 客观唯一真值。 |
| MoleSyn06002：新增候选，拟 2/1/2=5 | [v1 §3、§4.2、§5.1、§6/Table2](https://arxiv.org/html/2601.06002v1)。真实估计 teacher behavior marginal/transition graph，在图上 random walk 指定 instruction 模型合成行为序列，改变 synthetic-data 生成而非仅化学比喻；keyword 替换/删除与 random/matched ICL 对照为直接层。反侧：自动行为标签/固定表示/强 teacher 结构依赖；相关/t-SNE不能授真实认知因果或 attention 化学律。Table2 合成不全面胜强 teacher；RL 子命题必要设置定位 §15.2（固定任务/超参，初始化历史不同），若采用精确 sampler 再定点 §15.1，当前不授实现复现。 |
| DTI05713：局部候选，拟 1/1/2=4，低分报告关闭 | [v1 §2.1–2.4、§3–4/Limitations](https://arxiv.org/html/2601.05713v1)。hidden 轴算术均值到 layer×token，再有限差分局部梯度/2×2 second-moment tensor；贡献是新可视化 proxy，不是全部已知可视化重测。反侧：π周期椭圆不含定向流因果，均值压缩会丢表示；四模型单例/有限 pronoun/metaphor，pruning 留未来。BERT bidirectional 场景不能按作者“只前向信息流”字面泛化。低分来自 measurement-interface 局部增量，无已证长期 pruning 选择；不是按规模排除。 |
| DOM05502：局部候选，拟 1/1/2=4，低分报告关闭 | [v1 §3.5、Table3、Finding4、§7](https://arxiv.org/html/2601.05502v1)。DOM 修改的 semantic audit 不退却 CLS/runtime visual stability 回退，提供语义检查之外的局部 runtime 负侧；不能按 Web 应用域关。反侧：15 DOM/9模型、单 trial、chunk/window、Lighthouse proxy，不等真实用户体验或生产总成本。只授多轴回归检查接口的局部经验，不能泛化新优化原理。 |
| TestOracle05542：候选，1/1/2=4，低分报告关闭 | [v1 RQ1/RQ2、§III/TableI–II、§V](https://arxiv.org/html/2601.05542v1)。paired buggy/fixed 下 CUT正确失败70.84%与 fixed通过58.13%不相同；zero-shot可高于CoT/ToT。36 bugs/2模型/5 repeats 的 context×prompt 负侧可保留；不是新 oracle 原理，不能拿 buggy failure 当健全正确性。低分候选不伪装贡献前未读关闭。 |
| STELP05467：候选，拟 1/1/1=3，低分报告关闭 | [v1 ASTProcessor/SafeExecutor 核心](https://arxiv.org/html/2601.05467v1)。restricted AST subset、逐 node 执行、受控 tool proxy/timeout/retry、自然语言反馈是真实局部实现，不能由安全标题自动收。未见改变成熟 restricted-interpreter 边界的新机制/新隔离保证；低分是组合实现增量，不声称证明 sandbox 无逃逸。未补所有 CWE 附件。 |
| Safety40405529：候选，拟 1/1/2=4，低分报告关闭 | [v1 §3.1/Table1、§4.2](https://arxiv.org/html/2601.05529v1)。完整 ASCII 的五有效性判据覆盖 reach/obstacle/grid/4-neighbor/coord alignment，30/model 且按难度/模型不同，GPT5在complete easy/normal/hard均100%；不是“所有模型结构必崩”。masked vision正确选项固定B且输入与complete不同，保留其偏差；不把有限1%错误作iid连续机器人灾难概率。局部空间负侧有贡献但不足长期控制替代设计。 |
| Im2Sim05344：贡献前关闭，纠正原笼统领域理由 | [exact-v1 PDF §1–1.1](https://arxiv.org/pdf/2601.05344v1)。量化“Im2Sim”过程和10-choice结果明确来自旧工作[17]；本稿主要增加物理、植被、城市、文本/纹理的定性示例。已实际核而非由抽象标题排除；新实例未提出新的受控再生成判据或可改变重构/物理区分的接口。原文也承认渲染相似不保证物理正确，保留为边界而不写真实物理恢复。 |

作者已接收上述调整；三新增准入不是 Evidence PASS，也不是强制 Books integration。

## 其余九项负侧与分层样本

完整 AB 已全读，不以“属于领域应用”单独排除。GAMMA05336、ESS05473、MMViR05495 是机制/概念/检索组合三层样本；financial05403、CrisisBench05570、gender05751、news05835 是评价/奖励反侧样本；Pantagruel05911 为编码/语料样本。加已定点的 Im2Sim 为九项贡献前关闭。

- GAMMA：gaze/VLM/现成 skills 的组合未给出新不确定度、状态或控制选择；ESS：概念教育框架未形成可改变模型系统设计的机制/边界；不是因概念或非 LLM 自动排除。
- MMViR：复用作者可核 [v1 §4.2–4.3/Limitations](https://arxiv.org/html/2601.05495v1) 的 CLIP/KTS scene、MLLM三级caption、Contriever/timeline top-k再展开；没有具体新 state-reuse/dependency；summary会漏细视觉。该已有定点记录只支持组合判断，不证明所有分段检索无贡献。
- financial/gender/news：AB 的新人口/分类/输出分布描述本身未提出新的可执行检测、控制、保证或可改变已有 bias/evaluator 选择的受控失效接口；不能把 LLM类别标签、单政治框架judge 当真实人类说服效果/客观意识形态。保留这些 proxy 边界，不为明确范围外命题补全文。
- CrisisBench：reputation/market-style simulation reward 的评测目标不直接验证本项目的 access/effect/agent-state 控制；未在 AB 给出新的跨环境机制或可复用 failure contract。Pantagruel：French text/speech 用现成预训练表示目标与语料建设，未见新训练目标/保证/条件设计；语种不是排除理由。

## 日期反侧和终态隔离

本轮 fresh 打开 [arXiv availability](https://info.arxiv.org/help/availability.html)：final ID/DOI 不在首次公告前提供；normal Thu14→Fri14 EST 的最早公开为 Sunday20EST，即 BJT Jan12。Submitted 落该批次的下界与真实 registered Jan12 的 final-ID 已存在上界须联合；moderation 可延迟，因此仅排程或 registered 都不能独自授日期。早官方完整稿信号仍优先检查；不追秒、不按相邻 ID band定日。

- CuTe05972：fresh [Colfax 原文 Revision History](https://research.colfax-intl.com/categorical-foundations-for-cute-layouts/) 明确2025-09-21 Initial release，09-24 typos/exposition；已有 Tuple/Nest/compatibility/composition理论。其 Jan arXiv 不当新首次，未扫描174页证伪有无所有差额。
- HumDial05564：本轮打开官方 [Track2 results](https://aslp-lab.github.io/HumDial-Challenge/track2/results/) 核同 latency/score；复用作者准确版本 [Dec13 readme](https://github.com/ASLP-lab/Hum-Dial/blob/afd63679cb5ca077e8dba987fcc5daa4835717b9/Full-Duplex_Interaction/evaluation/readme.txt)、API commit Dec13T08:48:06Z 与官方 [description](https://aslp-lab.github.io/HumDial-Challenge/track2/description/) 五 interruption/四 rejection/A6000 证据。同 benchmark/环境/结果已经窗前，不能凭 Jan 新论文再记首次。未授所有论文细节无新修订，只是目前无本日重要修订具体信号。
- 日期 held 五项：SendVAE05823 bsmKEJfaar、GenCtrl05637 HJTFgDYoLO、AGDC05680 3xvyPnKUpv、IIB05870 WICf5wRXJ7 有更早官方匿名全文/论坛信号但精确 release 不可恢复；作者 API1/2/forum403 终态可复用，不再无限探403，保留有效AB/局部方法但不绕日期深审。TIME05300 Submitted Jan8T13:24UTC属于更早批次，registeredJan12最多夹Jan9–12，不足归本窗。需要准确官方首公开历史才重开；held不是日期PASS/零贡献。

## root 指定首七项：独立原证→actual owner 写前 PRE

这里只授下面列明的窄差额；未写 Books，不授写锁、实现、复现或 POST。真实章内邻接已顺读，以下位置为写前坐标，作者实际写后需 root 非作者检查新正文、完整邻接与自己的末注。

| 家族 / owner | 已实际读原证与 owner；允许窄差额、共存/反侧 |
| --- | --- |
| FLRQ05684 / `INFER-TENSORRT-LLM` Ch49 | [v1 Method/R1-FLR/BLC/Alg1–2、Tables8–10](https://arxiv.org/html/2601.05684v1)；actual1330–1445涵盖conditional residual、module/fusion、SVDQuant、静态/动态rank。在SVDQuant残差分支附近补离线随机rank-1 deflation与amax收益/额外bytes、budget/slope停止；不重复 input-runtime router。Table9 fixed64 4.44bit/PPL4.98对21.9rank 4.24bit/PPL4.98；BLC OPT13B W4 10.11→10.13反例、kernel融合额外4–6%latency。Proxy不认证任务最优，固定rank/dense仍可回退。PRE窄通过。 |
| DHPO05607 / `TRAIN-GRPO` Ch33 | [v1 Eq8–11、§4.1/Table1](https://arxiv.org/html/2601.05607v1)；actual564–614 GSPO及outer-length邻接。补token/sequence分别clip再mix、entropy sg/minmax混合；终局A相同，不创造causal token credit。4B averaged55.4>entropy54.3；32H100、训练response4096/eval16K、512×16 rollout计成本。Freshness/ratio identity保持，原token/sequence路径共存。PRE窄通过。 |
| ARR05588 / `AGENT-RAG` Ch76 | [v1 §3容量假设、§4.2–4.3/footnote7、§5/Table2](https://arxiv.org/html/2601.05588v1)；actual105–146 identifier→长度/beam邻接。补item rank权重与trie下后续有效ID质量聚合，区别top1 NTP和完整排序；infinite-capacity/augmented满秩是expressivity，不是有限训练保证。ESCI teacher为Gecko，nDCG97.21>95.23但R@1≈70<95.16，teacher-forcing mismatch；不授全库吞吐或替代DE/CE。PRE窄通过。 |
| Moral05437 / `TRAIN-RLHF` Ch31 | [v1 §3.4/5.3/7、B.3.2](https://arxiv.org/html/2601.05437v1)；actual501–543 actuator→probe/output→ID/OOD→组合邻接。新增根据macro/norm纠缠选择micro；Qwen较可分时macro可更强。两7–8B英语问卷，base/aligned未分；micro MMLU最大4.3/4.9点退，不能无副作用安全。Eq8加向量与§5.3clamp描述不同，不据此授统一可执行剂量配方。PRE窄通过。 |
| EvidFuse05487 / `AGENT-WORKFLOW` Ch81 | [v1 §4.2/5.4、AppA/Table8](https://arxiv.org/html/2601.05487v1)；actual173–216及1040–1062，205 Evidence Seeking分支末最顺，Offline World前。补forthcoming claim request→suspend→实际chart/caption→resume，对照whole narrative先定再render；不要发明dependency/version/transaction或把writer升事实权威。OWID43.2calls/1511.4s对3.4/179.33s，代码失败缺证据；simple staged报告仍合理。PRE窄通过。 |
| FACTUM05866 / `AGENT-RAG` Ch76 | [v1 §3/4.3–4.6、Tables2–3](https://arxiv.org/html/2601.05866v1)；actual861–863、881–925 grounding/citation/typed provenance完整邻接。应在916 entailment之后/typed provenance前补内部attention与FFN风险telemetry，不在357 retrieval数值段插citation。CAS/BAS/PFS/PAS是sensor，support真值仍外部。3B/8B、ARGUE70B标签/100human、report-level10fold；PAS反转只8B LR，EBM/LGB仍正，长度/组件改变不授pure scale causal law。PRE窄通过。 |
| NoisyJudge05420 / `PLATFORM-EVALUATION-SYSTEM` Ch66 | [v1 §2–4/Prop5–7](https://arxiv.org/html/2601.05420v1)；actual2385–2485 raw score→PPI→noisy likelihood→迁移校准。generic residual已覆盖，仅补同人口iid/MCAR、positive finite n/m、binary conditional-mean affine下optimal PPI++/EIF/正确MLE渐近等价及RG方差条件q0+q1−1>0/interior。普通PPI无偏不等efficient，sample-fit λ不无条件finite unbiased；continuous/ordinal nonlinear需相应consistent μ，不搬binary等价。不是逐条truth或发布权。PRE窄通过。 |

CEI05939 作者 fresh Eq8 反侧已收到：`min(alpha_max*cos(...),0)` 与正风险增强叙述冲突，**不修 min→max**；动态每token两forward与诊断定位、static/dynamic收益反例保留。这个受影响公式不妨碍last-input injection具体贡献准入，但不授可执行dynamic recipe。本笔记未做其实际owner PRE。

## 停点

46新AB独立校准、九歧义必要定点和root指定首七PRE完成；25仍不是25完整Evidence/Books通过。本日作者继续所需证据/报告，root负责锁与实际POST。原50、README、LS、Books均未由本复核者修改；不自授整日或其他日期验收，不自接别日。

## 余18必要证据与actual owner PRE（续核，非Books写入）

以下是新的独立写前判断；首七已过项不重做，日期held五项不再访问。坐标是实际顺读时的写前坐标，其他作者随后插入会移动行号。每个Integrate只限其窄命题，不能借此授整篇、实现、复现、POST或整日通过。

| 项目 / 独立处置 | 必要原证、实际差额、采用边界 |
| --- | --- |
| SketchVL05688 / Integrate `TRAIN-GRPO` Ch33 | Fresh [v1 Eq1–8、Table2、§4.1/5](https://arxiv.org/html/2601.05688v1)，actual231–241完整PRPO/tool hint/ROSE邻接：PRPO后补长度加权居中FinePRM与action频率offset，整轨A加step偏差后按A符号clip。只在clip前零和；clip后不授守恒，失败好step不转正、A=0仍零。RoI既有不重复归新。RandomPRM/无actionKL多个项高于full，7B PlotQA55.84<base63.44，FinePRM7B/473K合成、16A80040G/24rollouts付费；不是causal credit或普遍正则收益。 |
| CLewR05858 / Integrate `TRAIN-DATA` Ch27 | Fresh [v1 Algorithm1、§2–4/Table1–2](https://arxiv.org/html/2601.05858v1)，actual142–150 DataReuse及517–545 curriculum/FailureDriven顺读：现521后补固定full pool按BLEU/COMET/METEOR similarity排序，每epoch重复easy→hard支持；restart不是optimizer reset。原结构课程未覆盖跨epoch重访，数据顺序唯一owner Ch27，不另在DPO重复。三/六Romance语言翻译；DPOP及GemmaX2有BLEU/COMET反退，forgetting是解释而非独立retention因果证明。保留random/static order与独立任务回归。 |
| CEI05939 / Integrate `MULTIMODAL-REPRESENTATION` Ch23，dynamic公式隔离 | Fresh [v1 §3.1–3.2/4.1–4.3、Table3、Limitations](https://arxiv.org/html/2601.05939v1)，actual1120–1147完整PIH/read-write/contrast/audio邻接，现1139后补last-input final hidden c静态选层残差混合；不同于两路logit contrast。CTXcos/LogitLens commitment-depth只作关联sensor、不证明视觉因果。Eq8 `min(alpha_max*cos(...),0)`与正注入叙述冲突，不静默改max或授dynamic recipe。Dynamic每token两forward、static额外instance forward、white-box/调参成本；AMBER LLaVA coverage48.1<48.6<50.4，NeXT static CHAIR劣于base、MMHal dynamic非全部模型最低。 |
| SubDistill05913 / Integrate `TRAIN-SFT` Ch29 | Fresh [v1 §3.1–3.2/4/5](https://arxiv.org/html/2601.05913v1)，actual242–273完整distillation邻接，现258前补centered teacher/student，teacher orthogonal U所选子空间与student orthogonal V匹配、Stiefel及projected-energy层权。PRCA top1–runnerup margin响应是teacher代理，β→0 PCA不是真重要性；作者可核Table2 DomesticCat PCA75.1>PRCA73.1。原density/共享projector未覆盖所蒸馏对象选择；完美CKA不授任务保真、视觉分类结果不外推任意LLM。子空间估计/teacher forward/训练成本与output-only/PCA回退保留。 |
| CHDP05675 / Integrate `MULTIMODAL-EMBODIED-VLA` Ch26 | Fresh [v1 §4.1–4.3、§5/Table1–2](https://arxiv.org/html/2601.05675v1)，actual163–187完整VLA/actioncodec邻接，现177附近補连续latent扩散→nearest codeword离散choice→条件连续扩散，先更新discrete、后continuous/codebook，sg阻回流；Q引导codeword非reconstruction codec。K仍对应离散组合，未消除2^n。PAMDP模拟非VLA实机安全；main HardGoal79.5与ablation75.9分开，双采样/critic/codebook成本计入，保留原hybrid/continuous controller。 |
| GoalForce05848 / Integrate `MULTIMODAL-WORLD-MODELS` Ch25 | Fresh [v1 §3.1–3.3/4/5.1–5.3](https://arxiv.org/html/2601.05848v1)，actual53–91 support/goal/真实transition邻接，现66后窄补direct cause、desired effect、optional relative mass三blob渠道与paired cause/effect随机mask；goalforce生成前因不等directforce预测后果。尺度是domain-relative非绝对物理。Wan2.2冻结base/ControlNet3Ksteps/4A10080G、合成数据/采样成本；成功仅过滤后的valid人口，Pool1 12/22不等12/50。没有真实机器人闭环，不让逼真视频签物理或行动安全。 |
| Roman05776 / Integrate `MODEL-TOKENIZER` Ch11 | Fresh [v1 §2–4/6、Table1/Fig1–2](https://arxiv.org/html/2601.05776v1)，actual142–167 normalization及276–297 fertility邻接，现151后补native/roman monolingual隔离信息损失与multilingual共享对照，把fertility、collision、任务粒度分账。相同文档149M ModernBERT从零训练、各自tokenizer；四segmental语言接近，Chinese/Japanese尤其token任务退，UConv部分弥补非全保真。先前tuple碰撞已覆盖不可逆性，但未覆盖mono/multi可区分实验合同；不授decoder热替换或低fertility必然质量更优。重训/转换/回归与native/byte/subword回退保留。 |

上述七项窄PRE已逐批送root与作者，Books写锁和写后POST仍由root协调；本复核者未写书。

| 项目 / 独立处置 | 必要原证、实际差额、采用边界 |
| --- | --- |
| Rotate05722 / Integrate `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 | Fresh/reused [v1 §3.2–3.3/4.5 Fig7](https://arxiv.org/html/2601.05722v1)，actual252–275完整motion/camera邻接，现268前只补随机姿态→static A/T且无camera、stageII camera-only冻结其余后再全体joint、stageIII orbit全训的训练支持分离。一般Plücker encoder/分开训再联合已有GeneratedReality，不重复当新。46K proprietary/120K渲染、1–4refs，staging消融定性且非等总预算，不授唯一阶段因果、真实3D一致或world state。StageII不是始终冻结主干；普通camera/I2V与canonicalization单任务保留。 |
| TREC05603 / Integrate `PLATFORM-EVALUATION-SYSTEM` Ch66 | Fresh/reused [v1 §3–4/Tables1–2](https://arxiv.org/html/2601.05603v1)，actual313–349 ranking/RCP完整邻接，现343后只补qrel人工population也须独立复审：固定query/segment/rubric，分别比较label与run排序，再对高冲突人口抽样复评。τ2020 .79–.85而2021 .41–.62；22/826高冲突条件样本的三人支持LLM不能变成总体LLM优于human。原assessor可听full audio、LLM只见转录切片，prompt挑10%校准/4→3等级合并也改变测量身份；保留原qrel与人工复核，领域结果不单独授真值。 |
| MoleSyn06002 / Integrate `TRAIN-DATA` Ch27 | Reused [v1 §3/5.1/6，fresh§15.1–15.2必要段](https://arxiv.org/html/2601.06002v1)，actual331–348 synthetic/策略覆盖邻接，现349后补teacher轨迹LLM标注四state→empirical transition图→weak instruction generator的数据控制。§15.1 L831–840明确20Kteacher轨迹、从exploration起步采state及reflection/exploration/normal/deep提示；HTML四prompt块为空，不补完整prompt或执行recipe。不是化学本体、词换行为或转移相似认证能力；Llama Instruct QwQMole32.29<teacherDistill35.73，RL38.44<39.72。同条数不等teacher调用/SFT/RL总费用，保留真实teacher/verified轨迹与原采样。 |
| Circular05693 / Integrate `MODEL-SAMPLING` Ch20 | Fresh [v1 §3.1–3.3/4/Table3](https://arxiv.org/html/2601.05693v1)，actual129–160 penalty完整邻接，现147后补sentence-final-hidden均值线性probe→CUSUM正常集校准+persistence的statement-loop预警；不同于重复token penalty。语义/attention关联不授不可逆attractor因果，更非已验loop阻断器。Greedy、每model50normal校准与balanced至少50loop/50normal，low-loop模型被排除；EDR .64–.76伴FPR .24–.34，不能自然prevalence/线上门禁。白盒/probe/校准付费，可靠性不足保留原penalty、预算stop和外部验证。 |
| ACR05589 / Integrate `AGENT-CONTEXT` Ch75 | Fresh [v1 §4.1–4.3/5.1 Table1](https://arxiv.org/html/2601.05589v1)，actual215–258 bookkeeping/compression完整邻接，现257后补external router的none或具名操作→对应LoRA derived view，而非仅按长度压缩；rawH留存，不让in-place事实修正改原source。Teacher执行operator、base solver在raw/edited配对outcome分corrective/compressive/none，成功不证明逐字段事实保真。Qwen2.5-7B/E5/GPT5.2teacher；多项低于SearchR1/RECOMP，不能称普遍优于RL。Router/refactor/teacher调用与训练成本不由token减量代偿；原全文、可回读证据/非干预路径保留。 |
| LEAPS05513 / Integrate `AGENT-RAG` Ch76 | Fresh [v1 §3.2.2–3.3/4 Tables1–2](https://arxiv.org/html/2601.05513v1)，actual69–82完整queryQPP/视觉修复邻接，现75后补黑盒多queryset→对原query后置verifier与reward分母：HR每queryprecision/exclusive harmonic，GR dedup pool **precision非recall**，ER pre-dedup returned数分母。原选一QPP不含set重复压力。Eq4空/零分母未定义，不授完整执行recipe。14B verifier overallF1 85.19非全部>93；1Kquery同源优化指标、800Klabels、inverse/posterior/RL阶段/分页与全部调用成本，190/150ms局部均值非尾SLO/全backend可迁移。属性放松不得改原需求，保留固定query/传统hybrid与独立锚。 |
| Conformity05384 / Integrate `AGENT-MULTI-AGENT` Ch82 | Fresh [v1 §2.2/4.1–4.2及必要结果](https://arxiv.org/html/2601.05384v1)，actual152–185完整Peer/Debate/可见性邻接，现164后補先筛model-alone正确人口，再加模拟错误peer text、authority/unanimity/private-public的条件敏感性审计。非真实同题独立Agent，不能以人数或confidence代替独立证据。100image baseline筛选/64trials与difficulty另500image分母分开，logit非校准概率、p=.46不识别置信因果。当前exactHTML无§4.3或temperature；采样recipe不授，标为未核不编造。配对调用与筛选成本、独立vote/verifier回退保留。 |
| PreferenceShift05882 / Integrate `TRAIN-RLHF` Ch31 | Fresh [v1 §3.1–3.3/4/5/6必要段](https://arxiv.org/html/2601.05882v1)，actual338–377行为/coverage完整邻接，现350后补objective×target适配两轴，teacher生成自动chosen、原reference自动rejected后，offline直接SFT/pair与online先RM再policy不同。§4.5 teacher Llama3.3-70B每prompt3候选T=.7，非greedy；Llama8B/OLMo7B、GPT5nano版本/随机展示与500×16/T1diversity为测量合同。作者可核synthetic SFT高win仍低semantic/syntax diversity，不能授teacher偏好真值、相同目标或任意shift配方。教师生成、RM/rollout/训练费用与真实target标签/原reference回退保留；不搬§3目标概述作实现公式。 |
| TAGRPO05729 / Integrate `TRAIN-GRPO` Ch33 | Fresh [v1 §3.2 Eq12–19/4.1–4.4](https://arxiv.org/html/2601.05729v1)，actual299–318完整typed diffusion credit邻接，现311后补sample-i当前x_t上对best/worst **next latent**计算新旧transition ratio的cross-trajectory clipped surrogate，并与普通GRPO相加/FIFO bank。不是欧氏latent拉近、因果step归因或无偏onpolicy。TAGBench200来自TRAIN非heldout，HPSv3 2fps均值/Qsave不同proxy；high-noise、G8、320p53frames/16steps、bank/采样/reward费用。未披露age correction/硬件/bank长度不补造，非等总成本或稳定性保证，保留ordinaryGRPO/可信credit。 |
| SceneFoundry05810 / Integrate `MULTIMODAL-WORLD-MODELS` Ch25 | Fresh [v1 §3.2–3.6/4 Tables1/3–5/B.1/D.2–3](https://arxiv.org/html/2601.05810v1)，actual121–154完整simulator/geometry/evolution邻接，现130后补floor proposal→unordered object diffusion→nearest real asset、empty-slot count/heuristic articulated bbox与同位置shrink/retrieve后处理分责。Floor减sum footprint只是面积，非连通/robotwidth；maxiter/无replacement可未达标。Eq1训练含constraint gradient，非pure test-only；plus-gradient与BCE/IoU cost方向不抄执行recipe。单3090 24G/i9，原130000epochs不自改steps，1500h训练/300s3room；collision .109非零/FID29.02>25、复杂关节近似与数据域限制。不授真实动力学/navigation安全，保留显式几何检查/原asset scene。 |
| VideoAR05966 / Integrate `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 | Fresh [v1 §4.1–4.2/5/A/C](https://arxiv.org/html/2601.05966v1)，actual1154–1175完整exposure/窗口邻接，现1160后补causal codec、framewise multiscale、pastframe/currentcoarsescale接口，再以time-ramped/inherited bitflip及random causal window调整训练support；不是任意cache等价或只换AR头。Infinity preinit/tokenizer2000epochs/B128及完整ARattention成本；rFVD61>Omni42，randommask quality升/semantic退、384×672/8FPS和highdynamic drift保留。30steps/.86s缺已核硬件/总预算配对，不授SLO或归单机制；20sec定性非长一致性证书。与Sep异作者VideoAR不合家族，保留原full-history/较低corruption与独立rollout回归。 |

### 本次18项停点

18项均找到**上述限定小命题**的实际新差额，窄Integrate PRE完成，逐批已送root/作者；不意味着全部headline成立或全篇Evidence/代码通过。真实冲突/缺失层：CEI dynamic Eq8、Scene guidance符号/训练口径、LEAPS零分母、Conform采样身份、Video硬件/速度因果都按命题隔离，并不静默补公式。作者已纠正LEAPS GR与Preference teacher采样口径。

对拟不采用部分已核实际既有覆盖：Rotate一般camera/分阶段控制在Ch24 GeneratedReality已有；Roman一般碰撞不可逆在Ch11 phonetic tuple已有；Sub普通多层/density/shared-projector KD在Ch29已有；ACR一般compression/raw authority在Ch75已有；Conform一般correlated consensus在Ch82已有。它们只排除重复大命题，不抹掉表内更窄新接口。

首七PRE未重读或自授新POST；25=首七+本次18的窄候选层，原50不动、46AB分层分母不变、dateheld五项未扩查。本复核者仅修改本_sources笔记，未改Books/报告/README/LS、未stage/commit/push、未自授DAY/Coverage PASS；完成Jan13指定复核即止，不自接别日。
