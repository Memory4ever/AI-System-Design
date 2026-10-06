# 02/20 第二十三有限证据包：Conjugate Learning / Causal Abstraction

只恢复16177/16612，不扩宽库存。完整题摘、exact-v1核心与本次采用所需反侧实际读；本地REVIEW HTML以既有抽取命令定位。官方事件页轻核无可见撤回/勘误，16177有Feb19v2但无具体变化说明，不借后版，16612仅v1。沿既已root独核announcement→同ID DOI桥，lower2026-02-19T09:00:00+08:00；同IDRegistered原值16177 `2026-02-19T02:40:04.000Z`、16612 `2026-02-19T02:50:32.000Z`，+1秒upper10:40:05/10:50:33+08:00。注册不是精确公开时刻。未运行artifact、未复现。

## 2602.16177v1 — Conjugate Learning Theory: Uncovering the Mechanisms of Trainability and Generalization in Deep Neural Networks

**2+1+3=6；理论假设/中心保证深入，拟争议终态隔离，待root独核。** 原potential不是因审阅费时排除；局部诊断保留。

实际§2.2.1:256–259、§3.1:301–314、Defs6–7:459–475、Theorem10:553–590、§4.2:597–628、§6.1/6.2:854–870/949–977。exponential-family/Fenchel–Young条件建模、structure matrix `A_x=Jθf Jθf^T` 与单样本梯度平方平均energy不是一般batch梯度norm；risk界需相应最小特征值正、softmax p_min/损失曲率条件，未否定这些条件公式。中心“仅exponential family practically learnable”从固定维充分统计推到有限参数模型一致估计，正文未建立必需桥：充分统计是无损保留全likelihood信息，比consistent estimator更强；固定已知scale的Cauchy location可由sample median一致估计location，输出一参数，而不是固定维充分统计。若将“无额外结构”解释为不允许已知family，exponential假设本身亦需明确，不能据此排除所有非指数族学习。

另一个可直接反例的中心解释是§4.2:609断言batch=1必与out-of-batch gradient不相关。取两条同输入/标签的线性MSE样本、θ≠target，单样本与余样本梯度相同，非正交或无相关；原框架§3允许非iid。`M=max_k |R_out(θ_{k+1})−R_out(θ_k)|`是沿实际更新的loss变化，依步长/轨迹，不是已先验受控的独立noise常数。Theorem12在全局有限Hessian L与固定α=1/(2L)下只给 `ε²+4L(n−m)M/m` 邻域，m=1为 `ε²+4L(n−1)M`；未保证M=0，因此不由此推出一般global optimum或最小batch必有最紧可部署控制。此反例隔离的是桥接宣传/依赖推断，不声称所有定理错误，也不要求遍历所有generalization证明。

实测MNIST/Fashion/CIFAR10/100以及随机16-item mini数据，LeNet/ResNet18/ViT取消BN/dropout改LN，RTX2080Ti、momentum.9/weightdecay5e−4/cosine；mini60ep/batch2、full20ep/batch32，不是定理的固定步长纯SGD。bound/loss的dynamic Pearson相关接近1是局部共变，不能确证唯一控制机制、一般最优或所有generalization theorem。structure eigenvalue/energy计算和架构/recipe网格有费用，未披露全面wall/并发/SLO/CI，LLM外推不采用。

Actual TRAIN-PRETRAINING Ch28:345–373已把同点diagnostic/实际更新/最终质量分开，risk保证绑定surrogate及真实loss条件，data/normalizer/optimizer联合recipe与heldout/fallback具体在正文。局部conditional bounds只作报告，不借上面的争议新增普遍训练规则，无Books写入。重开仅需practical-learnability定义与必要性证明、batch1相关条件/M控制及相应global-convergence桥接的同版修正/正式解释；无争议的有限建模/局部轨迹仍保留，争议项不得支持正面Evidence/Books/全局保证。

## 2602.16612v1 — Causal and Compositional Abstraction

**2+1+3=6；形式理论的组件/查询层接口差额深入，拟Ch66窄整合，待root必要证据/实际owner PRE。** 不因量子应用或无benchmark否定直接因果模型主线；不引入其量子扩展。

actual核心介绍141–193、§6 Def46/Prop47:3777–3805、Def49/50:4105–4119/4212–4226、Theorem51条件4227–4228及结论4265–4283、Example54/55:4290–4310、结论5970–5976，以及A.1自然性关键依赖6647–6674。本次只采用Def46/Prop47的窄命题：query-level把高层query映到低层并保持语义；component-level进一步给每个高层component一个低层diagram，要求先运行低层再τ映射与先τ后运行高层交换，结构映射还须保query diagram。这种逐component一致性可在所声明组合范畴中延伸到组合，强于只看总input/output或某组干预响应相同。

严格理论权限：epic natural transformation、已给structure/query signatures及语义；不是有限intervention sample证明任意composition。Theorem51额外需高层noninput皆output、低层input有normalized state，partition按Cartesian/Markov/cd分别simple/extra-simple/extra-simple+full；不把这些图论分类搬为所有实际DNN必要条件。Example54共同latent Z复制在Markov结构不能简单合成，但确定结构可接受；Example55 constructive abstraction仍可能非component-level，支持强弱区分，不是所有抽象均失效。论文直接承认实践例子是否普遍满足新强条件是future；无实际trained-model mapping learner、生产采样协议、runtime/benchmark收益可采用。

Actual PLATFORM-EVALUATION-SYSTEM Ch66:2974–2984现有estimand/assumption/evidence降级与跨语言predicate/low-level alignment，尚无**query-response fidelity与component/composition fidelity分开**。拟在该段后仅补一条件段：解释若声称可组合机制，声明高/低层变量、mechanism/diagram映射、query域、representation τ及交换义务；一次总输出/局部干预对齐只能支持该查询域，不自动继承逐机制或组合保证。精确形式条件提供目标契约，有限采样只是诊断不是全域proof；真实因果模型假设和映射仍需独立核。额外机制映射/干预/组合检查成本与缺精确结构时退回query-specific/raw intervention/Unknown近文，不声称paper提供实际验证器或通用方法。求Ch66此单段+own末注窄锁；不要求全A.1/其它量子附件复读。

## 停点

两项仍普通待办，README84/50POST/普通12保持；待root上述必要source/owner处置独核，不授日级。16612拟写尚无锁；无stage/commit/push。

## 独立处置追加（2026-10-05）

16177必要争议采用边界root实际独核通过；16612必要PRE与Ch66 body2984/完整邻接/自身末注实际POST通过，锁释放。原84/12为历史停点，现三批同步不回推日级。
