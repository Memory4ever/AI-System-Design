# 本日第五批核心/决定准入

root已读第五批完整精确题摘并校准15287/15293/15322/15327具体贡献链可以进入必要证据；15286/88仍按决定核心判断，不借命名。以下来源完成与Books实际判断分开。

完整精确v1题摘与准入理由见[V3_ADMISSION_NEXT](V3_ADMISSION_NEXT.md)。以下不是全部库存队列，不因state/公式或既有owner准入。原日期字段各自核，明确EX不追补日期。

## 2602.15286v1 / 2602.15288v1 — 决定核心后排除，root校准通过

root实际原HTML核S3lease/relocation、S4co-reserve/S5人口及Eq16，EX校准通过。无新模型state迁移条件，安全反侧保留；不追全文或额外日期。

分别实际读[15286v1](https://arxiv.org/html/2602.15286v1) §III、V与[15288v1](https://arxiv.org/html/2602.15288v1) §III–V。新增是把既有lease、two-phase co-reservation、make-before-break与QoS绑定套用network-exposed AI service；优化placement不在primitive、client/state-transfer处理out-of-scope或hard open problem，未新增模型状态迁移、inference queue/kernel机制、具体可验证跨域恢复条件。算法明确反复申请lease后install/flip/drain，并非新状态一致性算法；schema/分plane本身不够。拟EX依据为实际增量仍是成熟控制原语的AIaaS应用映射，不是因弱benchmark或主题不在白名单。

安全/guarantee信号没有默漏：15286以simulated time无lease steering rate作正确性，原文保留prototype措辞但未唯一给实际AI model、serving config/hardware/seed数；zero rate只针对该definition/horizon，不授model/context正确迁移或无中断保证。15288 MonteCarlo样本是人为queue/runtime/network三项，endpoint全部requests与AIS仅admitted sessions的opportunity set不同，所报tail/violation不能不计rejects合并；Eq16每请求超过ell99与整窗口p99条件也要分账。上述反侧收窄宣传，不构成论文新发现的LLM评估机制。已读内容保留，若root发现原core有具体差额则定点重开，不由工作量改判。

## 2602.15287v1 — 2+2+2=6，标准必要证据完成

[精确v1](https://arxiv.org/html/2602.15287v1) §III–IV/Eq5–22/TablesI–II实际读。对joint DPP diversity gradient，仅删除与temporal interpolation consistency梯度负对齐分量；保留正对齐和正交分量。公式仅支持一次小步对latent proxy的first-order非降，不保证有限sampler步骤、真实画面一致性或所有prompt。Latent embedding/interpolation小CNN由decoded VideoPrism/CLIP目标训练，免sampler时decoder反传不等总零成本；离线decoder/encoder、100train+20test每prompt和embedding12000steps/interpolator1000epochs仍须摊销。

Wan2.1 t2v1.3B、50flow steps、十个给定prompt，每prompt jointly4×20重复，95%CI。TableI Ours Vendi-v .155 vs DPP .153、Vendi-f .197 < .207；MSE .0019改善DPP .0028但仍差IID .0010，不能“完全preserve”。对照diversity用latentmean而本法learned embeddings，主要表不是只gradient regulation消融。TableII同learned branch去ConsisReg .0021→.0019，但video-level diversity增益同时损consistency；支持有限取舍不普遍支配。Evaluator VideoPrism/CLIP与训练参考相关，temporal metric是EDEN插值MSE/CNI非独立完整quality/safety。分辨率/长度、GPU/precision、端到端耗时/并发SLO与unseenprompt泛化 Not Disclosed，v1仅codewillrelease未核实现。Books待实际owner，独立源待root。

## 2602.15322v1 — 2+2+2=6，标准必要证据完成

[精确v1](https://arxiv.org/html/2602.15322v1) §2–5/Table1、AppendixA.1/B.1/C.3–4实际读。独立Bernoulli block mask加1/p缩放保持给定update条件期望，但二阶Taylor产生(1-p)/(2p)ΔᵀHbbΔ及三阶余项；这只是local curvature项，H不正时不是全局非负regularizer，不能证明实际SGD自动求flatterminima。Magma又将cos(momentum,gradient)/τ经sigmoid/EMA作damping，参数update稀疏、momentum仍dense；与unbiased SkipUpdate不同，damping引入bias，作者unbiased替代不稳定。不能把稀疏更新当optimizer-state内存节省或完整step FLOPs省掉。

Llama2 C4 60M/130M/350M/1B，B512×T256、10k/20k/60k/100ksteps，五LR网格取最终validation最优，10%warmup/cosine；mask仅attention/MLP，p=.5/τ2由局部ablation选择。Table1 RMSProp+Magma1B13.19对Adam16.35及借前作Muon14.52，不能视作同artifact新复现；Adam+Magma Table1 13.71与正文13.81矛盾，保留两值不合成准确数字。NanoMoE中间更慢但最终更好，C4dense/sparsemomentum对照说明auxstate不能随mask冻结；ResNet+CIFAR对照不获益（作者给94.46/93.82顺序表述不清，采用“不获益”限定）。只perplexity/局部任务，未验安全或全部downstream；GPU/precision/重复seeds/端到端开销未披露，no overhead文字不作测量。§5 stationarity以constant SGD和smooth/variance假设分析，不等实际adaptive EMA算法的LLM收敛保证，不采用全局rate；采用local mask/damping取舍及反側足够，无需全proof史。Books待actualowner，未核代码或复现。

## 2602.15293v1 — 3+1+3=7，必要理论深入完成

[精确v1](https://arxiv.org/html/2602.15293v1) §2–5/Theorem3/Eq3.1–3.4/4.1、AppendixA.1–2/B.1–2/C.1–2实际读。Softmax KL是lognormalizer的Bregman divergence，dual coordinate是expected unembedding；给定固定准确linear probe与目标hyperplane、minimizer存在，forwardKL constrained optimum满足phi(hatlambda)-phi0平行probe。只有全hyperplane加初点均concept-factorizable、准确probe使目标概率在hyperplane固定时，A.30分解目标项为常数，才等价最小off-target KL。Minimizer不是无条件off-target完全不变，未证明一般semantic concept会满足这些强假设。

Covariance Hessian可数值rank-deficient、dual坐标需在unembedding convex hull内，regularizedNewton加αI再归一化小步仅近似dual路径；C.1也显示实际dualstep未始终parallel且靠boundary再转离。C.2直接反侧：testprobe可分，但steeringpath相同projection的target logit不同，probe-hyperplane假设实际不严格满足，可能目标不足与off-target tradeoff。§5.3 Euclidean在counterfactual mass稳定时也合理，不静默替代旧branch。

Gemma3-4B/C4、MetaCLIP2/COCO+GPTImage1synthetic，ClaudeAPI整理300+tokenpairs；10000sequences前256tokens、Top3含base/target且cumprob≥.7筛population再train/test。非全自然context；pair构造/多对一aggregate亦evaluator责任。α=.005调参、262K vocab covariance以Top20K近似，每步solve+covariance成本高，rank metric只0.99mass reducedvocab；概率offset改KL、paths达.9999后截断，之后both可能single-token collapse被排除。SEM是context均值，非independent训练runs；未披露GPU/precision/总体latency，不授生产control。

另有具体理论措辞不能采用：§2.2说dual interpolation等于两端**完整分布linear mixture**，但A.1证明仅匹配expected unembedding并最小forwardKL。作者未假设softmax family是完整simplex。一个数学反例（本审阅推导非作者实验）：一维unembeddings{-1,0,1}、端点lambda=±1，dual midpoint期望0对应uniform；完整两分布mixture则为{cosh(1),1,cosh(1)}/(1+2cosh(1))，非uniform。故不采用“OR/full-distribution exact mixture”解释，保留其正确moment/Bregman条件与Theorem3受限结论；反例只影响此命题不推倒全部有效机制。Books实际owner待比较/独立源待root，未核代码或复现。
## 2602.15327v1 — 2+2+2=6，标准必要证据完成

[精确v1](https://arxiv.org/html/2602.15327v1) §2–5、Table2/3、AppendixB.1–3/D.1–2/F实际读。采用的增量是把单model point或条件max改为观测生态内的98% upper-tail quantile，绑定base pretraining compute、post-training人口与评价protocol，再按训练compute bins校准并验证下一时段；并非compute唯一决定能力或真实可达硬上限。Sigmoid单调性β≥0是参数化约束，不是证明全部模型单调；pinball aggregate与signed bin coverage共同读，拟合好不消除未覆盖recipe/family。

四时段≤Jun24、Jul–Sep24、Oct–Dec24、Jan–Mar25，rolling只评train/OOD compute-range overlap，不授计算外推。Table2 Sigmoid ID/OOD pinball .00408/.00493，与I-spline .004/.00492近似而非全项最佳；coverage .0184/.0221 vs .0183/.0241，各有取舍。MATH及较小程度IFEval早期偏差/新recipe提升保留，BBH/GPQA/MMLUPro/MUSR局部较稳定。Base与post差距是观测，不是posttraining单独因果。

§4 balance I-optimal以nominal Jacobian和ridge近似prediction variance再加bin-count log penalty，greedy gain-per-cost仅近似选择，cost取parameter count假设大致线性，不是实测GPU-hours/token-length/SLO。GPQA/MUSR部分protocol α5%接近full fit，其他task20–50%趋稳，不写全任务5%保证或global optimal。拟合、模型估算、evaluation采样也有成本，具体GPU/precision/端到端未披露。

AppendixF newly evaluated Table5总1346，HF likes且lm-eval-harness兼容筛选，另手选end2025厂商模型；不是全部2000模型独立随机sample。老/新base分账，MATH L5高compute outliers直接反侧仍在；附录未给统一重复seed/实机费用。AppendixB.1异常值仅motivate quantile，不证明Benchmaxx实际污染。§5 cross-benchmark AIME2025 release分组仅MATH overlap n90、p=.15，未显著≠无污染，task/recipe/time confound仍在。不采用文中‘best possible’为全生态安全upper bound；只是可更新的预算线索。Books实际owner与独立源待核，未核实现或复现。
