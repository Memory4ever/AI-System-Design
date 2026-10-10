# Jan28 剩余具体 Books 包（待窄锁与 PRE）

## 最新层级（恢复后的实际结果）

新增61已到必要证据/具体Books安全终态：35整合48段16owner、11已有覆盖、9仅报告、6中心争议；全部35实际正文/完整邻接/自身末注 POST与状态轻核已由非作者通过，窄锁释放。下文旧待Source/待Books/待锁/PRE仅拟文为历史阶段；未变有效Source/PRE/POST复用，不代表当前普通队列。原64保护，最终六部分已融入README，V3进行态通过，最终DAY尚待。

只复用本日有效 exact-v1 必要 Source；author 实际 owner 比较，root/audit 非作者 PRE，窄锁后才写。各一段，不重排无关机制。未核 artifact/复现。当前 Source 边界见 supplement-reviews、root-source-resume 与 independent。

## 18533 → TRAIN-RLHF / Ch31

实际 Ch31 257–259 typed matching 与773–823 verifier来源已读：已有代理≠语义，缺 offline LLM编译reference/keywords/style code→runtime只执行的角色分离。拟放basic verifier边界后、18722特权judge前：

规则反馈还可以先由模型离线构造，再在训练 rollout 上仅执行冻结的规则：从 reference answers 提取 keypoints 和有序 keywords，以正则匹配后的 keyword-LCS 测内容覆盖；风格则由另行生成的 Python functions 加权评分。离线模型拥有 reference 与规则提案，运行时执行器只测这份 artifact，不能因为没有在线 LLM judge 就把合成偏差消除。[受限 RLVRR 对照](https://arxiv.org/html/2601.18533v1)中有序匹配比直接词面奖励少一种 verbosity hacking，却不验证事实、否定或等义改写，也不是 token-level 语义监督。Reference、keywords、code、权重及失败口径应共同版本化；离线生成费用与训练 step 费用分账，0.71% 的相对 step 成本不等全链降本。规则过拟合、语义错判或代码不可安全执行时，回人工 rubric、独立 semantic verifier 或已有 outcome reward，不让 compiled proxy 替实际质量签证。<!-- source-family:SF-2026-ARXIV-2601-18533 -->

## 18751 → TRAIN-RLHF / Ch31

实际 Ch31 742–751 rater affine/shrinkage/time identity，和76–115 BT comparison支持已读；未覆盖带正/零/负trust的joint reward方向、整体符号不可识别。拟放Reward Heterogeneity段后：

标注者差异还可能是比较方向的系统性反转，而不只是 offset、尺度或随机噪声。一个受限分支联合学习 reward 与正、零、负 expert trust，让稳定反向的比较贡献反号信号；零信任则不据此提供方向。识别依赖共享且有非零 reward 差的比较支持与连接条件，reward/trust 同时反号仍可产生同样的观察，因此方向锚点不能由 joint fit 自签。[受限控制任务实验](https://arxiv.org/html/2601.18751v1)使用模拟 experts，更多反馈也能恶化结果，单个 global trust 不说明不同 context 的资格。应保留 annotator、比较图、信任版本与外部方向核验，并支付联合拟合和反馈成本；正文与算法的精确权重因子未闭合，不拼成保证。支持不相连、可靠方向未知或真实反馈漂移时，回零权重争议隔离、已校准非负信任与独立人工审核，不把负信任解释为“已恢复真实价值”。<!-- source-family:SF-2026-ARXIV-2601-18751 -->

## 18543 → TRAIN-RLHF / Ch31

实际 Ch31 reflection→curriculum 831–849已读，训练信号可信度已有但终局point与相邻pair改善的权重门差额未有。拟放Reflection基本段与原note后、curriculum前：

对多轮生成工具，最终满足约束的 point reward 与相邻结果被 judge 判为改善的 pair reward，可以提供不同压力：前者测交付候选，后者只鼓励修订方向；最终失败时降低 pair 的权重，避免只有“相对变好”就获得完整成功信号。Pair judge 仍可能共同误判，连续改善不认证每个约束或内部反思忠实；[受限图像工具训练](https://arxiv.org/html/2601.18543v1)还按交互轮数重采样 rollout，必须连同候选人口与工具版本保存，不能把变化全归给奖励形状。配对判断、更多生成和训练期特权参考另付费，局部消融增量与第三轮收益下降不授任意工具或免费质量提升；多义目标会诱发过度反思。缺可靠终局判据、工具能力已达上限或费用不值时，保留固定轮数、普通 outcome reward 与独立交付验收，不由 pair 分数替安全 gate。<!-- source-family:SF-2026-ARXIV-2601-18543 -->

## 18554 → PLATFORM-EVALUATION-SYSTEM / Ch66

实际Ch66 2797–2830 rubric formation/atomic/global ranking及63–93成功交集已读，缺constraint type/count/order/cooccurrence人口与fraction/allpass明确分母。拟放逐criterion/globalranking说明之前：

组合指令的评价人口还必须保留每条 constraint 的类型、数量、出现位置与同现项：某条约束的通过率、它与另一条同时通过、给定位置的通过率，以及每份回答满足约束的平均比例，是四个不同对象。最后一项不能改写成“全部约束同时通过”，位置变化也可能混入约束内容与组合差异。[受限 MOSAIC 对照](https://arxiv.org/html/2601.18554v1)提供这类局部诊断，阈值化 rule/judge 的部分通过和 partial JSON parse 却不认证严格合规，相关的约束失败也不证明架构因果。EvalSpec 应保存原 prompt、逐项 verdict、适用分母、parser/阈值及约束布局，另付组合构造、调用与标注成本；judge未校准或顺序人口不匹配时保留固定布局、分项原始结果与人工核验，关键条件继续独立 hard gate，不由高平均比例放行。<!-- source-family:SF-2026-ARXIV-2601-18554 -->

## 18579 → AGENT-RAG / Ch76

实际Ch76 99–118结构候选/预算导航与494–540rerank完整邻接已读，缺冻结crossencoder preMLP latent邻接聚合→semantic/rank/bridge扩展。拟放Reranking开头后：

Corpus graph 还可以直接进入重排表示，而不只作为候选过滤：先取冻结 cross-encoder 在 scoring head 之前的 query–node latent，在已取子图中按邻接聚合，再交给原 head；随后只对未取邻居按 query similarity 与当前排名/桥接分数扩展，直到节点预算停止。图、encoder/head、聚合系数与扩展策略共同定义检索版本，结构邻近不能认证事实或决定性证据。[受限 FastInsight 实验](https://arxiv.org/html/2601.18579v1)不支持把一般非对称 random-walk 算子解释为已证明的 denoising gradient，孤立节点与断连也须另定失败路径。聚合、图建设/更新与候选前向另付费，retrieval 平均时间不等生成端到端 SLO；结构噪声会把错误邻居传播进排名。图不可信、预算触顶或质量回退时，保留普通 cross-encoder、语义/词法候选与原文 support 核验，不从较高拓扑代理签“真正理解”。<!-- source-family:SF-2026-ARXIV-2601-18579 -->

## 18595 → AGENT-PLANNING / Ch79

实际Ch79 153–199 predicate-first→parser/solver→refinement完整邻接已读，缺已有backbone→LLM新commonsense前提→条件entailment/SCfallback。拟放predicate-first两段后：

形式系统不能推出答案时，还可以把“缺什么前提”交给模型提议，而不是让 solver 扩大自己的事实权限：从已可推出的 backbone literals 取少量 antecedents，生成新 commonsense literal，再用模型的常识性与相关性代理筛选，加入候选前提后重试条件推理。SAT 只证明给定全部前提下的 entailment，单条假设各自相容不保证它们与原前提联合一致，更不验证新常识或翻译真实；应另核 joint consistency、来源与语义，模型自评不能认证它自己补入的事实。[受限 ARGOS 对照](https://arxiv.org/html/2601.18595v1)仍有错误翻转与翻译失败，投票 fallback 必须保留 best guess 身份。Literal生成、评分、CoT、prefill和solver共同计价，平均CoT较少不等完整省算，内文阈值/成本冲突不拼精确配方；缺可信前提或预算耗尽时，回原solver、独立澄清与明确Unknown，不由可满足的假设自签正确结论。<!-- source-family:SF-2026-ARXIV-2601-18595 -->
