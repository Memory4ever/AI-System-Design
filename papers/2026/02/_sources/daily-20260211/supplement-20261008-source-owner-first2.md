# 2026-02-11 单篇 Source→owner 预审请求（补查）
作者：supplement_20260211；未自授 Source/PRE/POST/DAY。
日期：六项上下界推断已由 root 实读准许。不是 DataCite registered=公开时刻；最早正常 arXiv 公告由 v1 Feb09 UTC 提交和官方排程界定，最终 ID 公告时才分配，Feb10 注册提供“最晚已经公告”的上界，均落 Feb10 BJT。无已知更早作者正文事件；仅这批定点材料。

## Spherical Steering — 2602.08169v1
- 准入：固定 additive activation edits 同时改变方向/范数 → 原始 activation 空间的 geodesic Slerp 恢复原 norm，并由 antipodal vMF prototype 分数条件触发 → 可把幅度与选择性干预拆开，重新检验 MC 与生成质量，而不先采用 norm=truth 或无损控制。
- 评分：2+1+2=5；因为 WORLDVIEW-REPRESENTATION 的具体长期几何分支缺口深入受影响命题，不因访问或要改书加分。
- 实际已读：v1 §3.1–3.3、§4.1–4.4、§5.1–5.4、AppendixB/C.1/C.2。原件 webCore0/1/2/3/4/5.json。原HTML https://arxiv.org/html/2602.08169v1#S3 与 #S5。
- 可支持：contrast 均值差为目标μ，保留norm的球面路径；vMF±μ 和 κ/β/α 设置改变触发/强度。训练-free只指不学习额外 neural steering model，仍须配对训练样本、prototype、sweep和逐token白盒计算。θ=0已有定义，未核artifact与θ=π数值处置，不能自补部署recipe。
- 评价：Qwen2.5-7B-Instruct / Llama3.1-8B-Instruct；TruthfulQA817题2fold，train/validation4:1，prototype仅train；MC按候选token-logprob，生成由两个TruthfulQA7B judge输出TRUE/INFO及product。相同split且单独hparam sweep，但没有全面独立重复/不确定性、生产hardware/precision/batch/concurrency/SLO（Not Disclosed），非端到端性能。
- 直接反侧：Table1 Llama TRUE轻微下降、Qwen INFO下降；§5.1 ungated高强度退步，Table4在base Llama3.1-8B过强干预INFO大降，保norm不保useful generation；base与Instruct结果不合并。有效rank下降不是完整manifold/唯一因果证明，平均norm近似一致不证明truth只由direction编码，antipodal prototype并非已校准真假概率。
- 当前owner已实读相关正文：Ch5几何/steering §“表示方向…”约242–266、证据阶梯/控制边界至365。已有 output-KL与Euclidean分离、contextidentity、probe≠control；缺 norm-preserving spherical+conditional proxy 分支。
- 拟窄写：保norm球面方向更新是一种替代而非分布无损保证；绑定 μ/model/layer/token population，gate proxy和强度独立校准，joint测MC、TRUE、INFO，费用及失败回退保持。不要写 rotation 首次出现，既有Angular/HPR已存在。由实际写入者再读Ch4/6邻接，root实读SOURCE/PRE后协调Ch5窄锁。

## Adaptive Latent CoT — 2602.08220v1
- 准入：统一latent预算/全past latent依赖阻碍并行与compute分配 → 2D因果mask改变可读取的(t,k)关系+逐token reach/exit阈值剪枝+训练期正确性权重stopgradient → 固定参数/数据时可将依赖图、停止器训练和执行预算分开。
- 评分：2+2+2=6；MODEL-TRANSFORMER-LAYER实际token级依赖/停止分支缺口深入受影响命题。
- 实际已读：v1 §3.1–3.6、§4.1–4.4、§5.1–5.3；webCore0/1/2/4。原HTML https://arxiv.org/html/2602.08220v1#S3 和 #S5。
- 可支持：mask只准 t_j≤t_i且k_j≤k_i，改变旧依赖而非精确保持原fullpast计算；按每latent step并行active positions，O(K)是criticalsteps不是总FLOPs；exit mass混合并把截断剩余分配最后执行态。训练loss用ground-truth token概率与stopgradient罚继续，部署只读router/reachproxy，不是在线知道真实答案。所有latent steps共用tokenposition，不扩positionID。
- 评价：从头Llama410M/1.4B、Pile26B/50k步，同data/opt/schedule主对照；0/5shot9下游与PPL；预算为Kaplan式estimated pretraining FLOPs，410M2.27 vs vanilla1.4B2.18不是完全相等。lmax3 1.4B7.47e20 vs PonderLM2 17.47e20；不换成walltime/GPU吞吐/E2ESLO。hardware/precision/production batch/concurrency/length/SLO未披露；未核代码/复现。
- 直接反侧：平均提高不等所有任务赢；410M zero Lambada/ARC-E/SciQ低于vanilla1.4B，lmax5 PIQA低于PonderLM2；70M ablation router Linear2.670 vs NoAdaptive2.671差极小、MLP2.675更差，无显著性保证；λ增大更多prune却更差CE，β增大更好CE却少prune。难度/targetprob与长度相关不证明在线停点正确，更多latent compute也可伤已高targetprob token。
- 当前owner实读Ch17 §Parameter Depth vs Execution Depth 511–627：已有sameposition/crossposition循环、FROST相对loss stop、不同execution预算和SLO。缺2Dmask下tokenwise parallel frontier/reach-exit mixture/训练truthprivilege与runtimegate区分。
- 拟窄写于该节：将token t与latent k拆开、训练并行active positions但decode仍nexttoken串行；reach/exit mixture是有成本的budget mechanism，训练target-informedstoploss不授权runtime正确性；共同版本化mask/router/τ/λ/β/Kmax/KVread语义，质量与真实运行分账。由实际写入者读Ch16/18邻接，root实读SOURCE/PRE后协调Ch17窄锁。

准备好的单篇不等待其余材料；目前两篇未写Books，未授Source/PRE通过。
