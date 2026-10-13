# SympFormer 2603.16535：必要理论/实施反侧与窄 PRE

作者resume_mar18，只03-19补03/18自然日；2+1+3=6给feature/velocity联合状态与连续几何→离散实现的具体接口，知识差额作必要深入。实际[exact-v1 PDF](https://arxiv.org/pdf/2603.16535v1)封面/§2–6、AppendixA的Propositions4.1/4.3/4.5证明与B必要参数已读；p10 Proposition4.3与p15 Algorithm1已实际渲染视觉回对。HTML封面Aug24不作为本窗版本日期或实现证据，PDF封面March18/v1headerMarch17与本批日级夹证分开；currentabs仅v1、comments24pages/2figures/3tables，未见具体撤回/更正，不遍代码/全部图像点/参考文献或复现。

## 支持和关键反侧

§3 attention-only、共享固定Q/K/V及A=KᵀQ对称条件，把残差层解释为粒子场；不是所有训练Transformer的完整连续极限。§4另需A正定、V对称，bilinear kernel下formal Stein流和quadratic势；§2明确Rᵈ只formal、compact才rigorous，bilinear kernel不因此继承一般strict-PD/integrable kernel完整metric保证。Proposition4.3在给定smooth有限矩椭圆密度、Φ0=0和有效连续解下，线性速度场经线性pushforward保留椭圆族，P/mean/covariance闭合；不授完整学习层、MLP/LN、任意离散步长、所有有限token状态或任意时间全局存在性。ProofA的线性transport和纯quadratic Φ链成立于其限定模型，不把这条性质误写为语言质量保证。

§5 softmax几何需A可逆及B=VA⁻¹对称正定，mobility依赖ρ/normalizer；保守部分Hamiltonian的动能同时依赖X与Y，非普通欧氏Nesterov的separable动能。§4.5/5.2的X/Y粒子耦合、velocity初0与damping提供可实现proposal，但凸优化O(1/k²)引言不等此架构训练保证；§7把收敛/rigor/大规模下游列未来工作。Example5.5中离散力消费的X身份和系数，与§6的实际共同旧状态Euler描述不能自行合成精确可复现公式，本次不复制exact update或授conformally symplectic/普遍能量单调。

§6理论singlehead，而实现将多head score在exp之前平均，非普通独立head softmax后concat；eachlayer自由学习Q/K/V，没有原理论对称/正定约束的已核执行。为避免第二次kernel，§6.1/Alg1实际F/G同时读取旧(X,Y)，然后更新两状态，再将attention momentum给MLP lookahead，经LNY/writeback。不是§2 kick-then-damp后以新momentum求position的conformally-symplectic Euler。learned per-layer hX/hY、r/t+m damping和MLP参数共同变化，late strong-convex是heuristic，不是已证所有训练区域性质。AB2/ETDAB2另存历史函数值，调用数守恒不消状态/算术/内存/优化代价。

TinyStories causal nanoGPT-style 10k optimizersteps，原文仅说over2000shortstories，没有披露精确train/eval切分/重复seed/CI；AdamW不是Yuriiformer的AdamW-Muon原配方，不能把基线方法差完全唯一归因几何。Table1 softmax baseline best2.4473/2409.4s，plainEuler2.3234/5036.1s，PresympEuler2.4592/4979s、AB2 2.6546/5249s反退，ETDAB2 1.8386/5798.2s；同calls不是普遍质量更好或更快。Table2 linear小设置baseline2.9614/486.7s对Presymp2.7314/1172.8s；Table3较大plain2.6567好于Presymp2.6909而时间10806.5/12620s，非所有presymp最好。best-loss停止/选择身份与最终step损失不同，不并成一项服务性能。

B：GPT2 BPE50304、GELU4×/0dropout/nobias、FP16、globalclip1但learnedscalar排除clip；8/8/d64/L512/b6/acc16为T1，4/4/d64/L128/b6/acc12为T2，8/8/d64/L1024/b6/acc12为T3，150warmup/peak3e−4，RTX6000Ada/PyTorch。B开头minLR .1×/scalar5×而各实验minratio .4、T2/3scalar100×，必须区分概述与具体配置，不授统一精确recipe；完整framework版本/卡数、复验/统计及服务I/O/arrival/batch/concurrency/SLO ND，任务本是训练对照不假装生产部署。

## actual唯一 owner与差额

已按AGENTS实际重载Books背景/学习方法/写法/ROADMAP及LS本日路由；actualCh17 485–535完整多流读写→depthmomentum→paralleltracks，Ch16/18首22行交接已读。Ch17 509确有跨层momentum状态/初始化/一般稳定费用，但没有X/Y非separable Hamiltonian消费接口、连续几何假设与为守calls改变离散更新而不继承几何保证的具体边界；不能用momentum主题假NC。soleMODEL-TRANSFORMER-LAYER，理论只用于说明该架构分支的约束，不复制Ch14通用attention或Ch28 optimizer。拟原depthmomentum source-marker之后/ParallelTracks标题前一段。待非preparer必要Source/owner/PRE与root新窄锁，未写不计safe。

### 一段逐字 PRE

跨层动量也可以从 token 分布的惯性流构造，而不只把前层更新作欧氏外推。一条[受限架构分支](https://arxiv.org/pdf/2603.16535v1)让 token 同时携带 feature 与 velocity：softmax 几何中的动能依赖两份状态，位置和速度更新因而共同消费 attention 条件；attention momentum 又作为 MLP 的 lookahead 输入。这增加 velocity、阻尼、步长及可能的历史函数值状态，不能直接继承普通凸优化的 Nesterov 速率。连续推导的投影对称/正定条件与线性流的椭圆分布保持，不自动延伸到自由学习的 Q/K/V、多 head、MLP 或 LayerNorm；实际实现为节省 kernel 调用，让两状态同时读取旧状态再更新，也不因此保有先更新动量的几何积分器保证。同样的 attention/MLP 调用数仍可有更高墙钟成本，部分离散器的验证 loss 还反退，须将状态路径、积分次序、训练配方和达到质量目标的全费用分别验收；几何条件、数值稳定或净收益不成立时，保留普通 residual、较简单 depth-wise momentum 与已验证的固定层栈。<!-- source-family:SF-2026-ARXIV-2603-16535 -->

### 静态来源注

- `SF-2026-ARXIV-2603-16535` — [SympFormer exact-v1 PDF](https://arxiv.org/pdf/2603.16535v1)必要§2–6/Propositions4.1/4.3/4.5/5.1/5.2、Algorithm1/Tables1–3与A相关证明/B。仅feature/velocity联合状态及连续几何、实际离散消费/费用分责；不授一般metric严格性、自由QKV/完整网络椭圆保持、Nesterov收敛或普遍质量/加速保证。有限TinyStories/RTX6000Ada对照和离散器反侧近文，未核代码/复现。
