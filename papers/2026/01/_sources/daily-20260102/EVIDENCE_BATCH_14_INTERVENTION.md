# Jan02 有限五项决定性方法

最新SiLRI24288/Duality24271/RAG24268必要原源/owner及actual正文/前后/末注POST root通过。RAG移至完整状态生命周期标题下、Span取证前；SiLRI uniformκ与Dualityfactor权限局部隔离。RSA中心成本符号/温度争议已root原式核终态暂缓；Mirage最后两frame对应注入6分必要原源/评价与Ch24具体owner已root核，863/865两段及末注1722实际正文、邻接及末注经root非作者POST通过。不授整批附件或日级Gate。

仅此前47具名完整AB潜在中的24288/24271/24268/24263/24227；GAP_ABSTRACTS_1完整题摘已实际重读并送root具体命题校准，不是新扫描/自动保留。当前只以下决定性method实际读，必要评价/关键反侧与独立复核仍普通待办，不授Evidence完成或Books写入。所有raw是原工具可复查位置，不是复现/性能认可。

## [SiLRI24288 exact-v1](https://arxiv.org/html/2512.24288v1)

拟2+2+2=6：human干预非总最优，按state行为policy的uncertainty放宽模仿界，而非将全部干预当最优。actual IV-A–B Eq3–8：deterministic actor与Gaussian human policy比较mean deviation，bound随其std，statewise非负lambda；beta只从intervention buffer拟合，policy-only访问state没有真human样本，四网优化不是已求全局saddle。可核增量是行为不确定性参与约束的训练边界，不授human std已校准/所有state可行/真实safe。需要直接消融、支撑域与必要AppendixVIII约束化简假设，不扩无关证明。

```text
L119 Eq3: ||mu(pi(.|s))−mu(beta(.|s))|| ≤ kappa sigma_beta(s), all s.
L128 Eq4: L(pi,lambda)=−J(pi)+lambda^T[D(pi,beta)−kappa Sigma_beta].
L143: beta approximated by multivariate Gaussian fitted on interventions; human distribution unavailable on policy-only states.
```

### SiLRI必要对照/理论收束（作者实际读，root待核）

实际IV-C–E/V-A–F/VII-A–C/VIII/IX必要范围：20 offline demonstrations；两个buffer各128，beta每50 intervention更新，lambda LR3e-6/其余3e-4，actor4090/learnerA6000、precision未披露。实测8任务/two embodiments，三基线同架构超参但ConRFT原JAX/超参不同；success要求无human intervention，ten-episode滑动平滑，扰动每任务15trials；two-operator CI来自两训练过程非多seed保证。固定lambda .5早期同样warmup却后退、扰动knot退化，不能授所有human或全部state安全。

**局部关键反证：VIII Theorem4从Eq20到22不成立的方向。** Eq20可得 state-specific bound；原proof写c(s)≤cmax，因此2ε−c(s)≥2ε−cmax，却将较大上界替成较小上界。例d=1、σπ=1、σβ∈[1,2]、ε=1，cmax=.25−1+ln4≈.6363；σβ=1/Δμ²=1.5时KL=.75≤1，但1.5>κ=1.3637违反Eq22。只隔离uniform κ guarantee，不否定有限经验机制。正文Eq3为norm≤κ std，实际Eq11为squared norm≤6·average std+.1；AppendixEq22为squared norm≤κ variance，三者不是同一约束，不把实现称已证KL等价/已达saddle。

必要原公式定位（actual HTML，公式原值非作者保证）：

```text
IV-C L213 Eq11: L_lambda=E_s[-lambda(s)(D(pi,beta)−kappa sigma_beta−c)].
L214: D=||pi(s)−beta(s)||_2^2; sigma_beta=average std across action dimensions; kappa=6.
VIII L437 Eq18: c(sigma)=d(sigma_pi^2/sigma^2−1+ln(sigma^2/sigma_pi^2)).
L448 Eq20: ||Delta mu||²/sigma_beta² ≤ 2 epsilon−c(sigma_beta).
L451 Eq21: c_max=max_[sigma_lower,sigma_upper] c(sigma).
L455–457 Eq22: ||Delta mu||² ≤ kappa sigma_beta²; kappa=2 epsilon−c_max.
L460 proof: c(sigma_beta)≤c_max => 2epsilon−c(sigma_beta)≥2epsilon−c_max; then says multiplying Eq20 gives Eq22.
```

actual Ch26 239–258：旧RL token/reference约束与phase切换不承载“human Gaussian dispersion→state-bound”的接口，拟其受限online-RL段后窄段：beta dispersion作为训练约束proxy非正确性/安全，intervention-only support、critic/label/人工SOP影响、实际约束版本与KL理论分账及原BC/保守controller回退。确认具体gap再深入已读affected条件；暂不写Book/root尚未授。

## [Duality24271 exact-v1](https://arxiv.org/html/2512.24271v1)

拟2+2+2=6：同question在original/edited答案变化，以成对优势尺度控制两人口。actual§3.2/§4.1–4.2：同context blueprint生成edited视频和oraclecaption/QA，由model验证，不能把计划编辑自动视为实际像素事实。SFT等量两域，RL对eachgroup的L1优势proxy按二者mean重权；动态过滤排除全对/全错改变人口。Eq9口径冲突保留：正文S=sum|A|、原式G×sum|A|=2sqrt(p(1-p))；population-std下sum应为2Gsqrt(p(1-p))。相同G时公共因子在两域ratio可能消掉，不能由此宣称整个训练无效；梯度向量/token长度及相关性不同，L1优势相等也不保证实际梯度贡献相等。拟采用只限paired人口/重权对象，中心‘guarantee balanced gradient’不授。尚待必要评价/独立原源核。

```text
L118–120: shared Q with different answers for V_ori vs V_edit; model divergence D(P(a|Q,Vori),P(a|Q,Vedit))≥delta.
L157: S=sum_i |A_i| (prose); L158 Eq9: S=|G|sum_i |A_i|=2sqrt((1−Rbar)Rbar).
L177–178: alpha_*=S_target/S_*, S_target=mean(S_R,S_CF); A_*'=alpha_* A_*.
```

### Duality必要对照/定义收束（作者实际完成，root待核）

实际§5.1–5.3/Tables3–5/A.2与AppendixB：16/64/8帧不同bench合同、≤30s；SFT1epoch/LR1e-6/batch4/7B用8H200，32/72B16H200；RL batch64/G16/7B600、32B60、72B20steps，greedy，precision未披露。Table4从同SFT start比较GRPO/DAPO/DNA，保两域配对数据与额外生成/筛选费用；Table3并非所有general任务paired最好。双答案同时正确才记pair success，600 pair文字与类别计数599原值不补造一致。

AppendixB.15实际为group mean |A|=(1/G)sum|A|=2sqrt(p(1−p))，B.10/Eq9却写G·sum|A|；局部因子口径冲突，固定同G比例可能消去，仍不授代码实现身份。更重要的是Eq6 R=format+correct但B.11仅binary假设，若format奖励不恒定，binary式不自动适用。L1 reweight只改优势proxy，不保token-length/score-gradient向量的实际两域梯度均衡。Ch33 461–469已承载normalization改变统计单位/权重，却未承载paired-domain优势proxy→真实gradient贡献分责；拟其后窄段（不复制dataset生成recipe），必要原源/owner未授，不写共享文件。

```text
B.10 L409: S=G sum|A_i|=2sqrt((1−Rbar)Rbar).
B.11 L413: R_i in {0,1}.
B.15 L431–434: S=(1/G)sum|A_i|=2sqrt(Rbar(1−Rbar)).
§4.2 Eq6 L146: R=r_f+r_c; Eq8 L156 reduces by sum response lengths.
§5.3 T4 DAPO: Event60.6/dual74.8; DNA61.3/76.8 (same SFT start, not universal rates).
```


## [RAGPart & RAGMask24268 exact-v1](https://arxiv.org/html/2512.24268v1)

拟2+2+2=6，防御保证变化触发深入受影响内容。actual§3.1–3.2：先独立embed fragment再组合平均，与先concat再embed不同；多组合top-p按出现频率聚合。原DPA多数条件不自动迁移top-p，因为非各组合第一也可高频入选；交集utility下降且空时randomunionfallback另有边界。RAGMask只检查初始top-alpha*p，滑窗mask观察similaritydrop删敏感span再重排，依赖毒点局部敏感性且有额外检索费用；不授generator免疫/自适应毒点保证。尚待具体attack/evaluation及§6必要理论边界，非全文附件。

```text
L126–127: np<(N−1)/2 original DPA condition no longer guarantees majority top-p robustness; p=1 returns original setting at utility cost.
L136: masked_score+delta > original_score => retain tokens; otherwise discard span.
L120: C(N,k)*D embeddings/databases; L136 C_mask≈(li/m)*alpha*p.
```

### RAGPart/Mask必要评价与保证边界（作者实际完成，root待核）

实际§4–7主线/§3.1–3.2：NQ2,681,468/FiQA57,638 corpus，512训练queries/每query随机3文作为attack目标，四retriever与HotFlip/散布HotFlip/query-as-poison/AdvRAGgen；ASR是retrieved any poison，SR是retrieved any golden，均非生成答案安全。硬件/precision/在线并发SLO未披露。§6只在benign各组合top-p一致、保至少p clean且RAGPart单poisoned fragment不污染mix等假设下计数组合；这些假设不是encoder mean天生保证。§6.1多毒文最多每列一个poison等分析前提另限，不授自适应top-p免疫。§7明确语义贴题假事实无法被该retrieval防御固有区分。只收embed-before-mix与top-p aggregation权限、mask sensitivity费用/utility分账，未审全超参附件/未跑实现。

actual Ch76 869–899已有span取证、joint-context poisoning与exposure/selection/use/effect阶段，尚未解释分片前embed对单poison影响及“决策多数→多候选top-p”的保证不迁移；拟取证前窄段，保mask probe不是事实判别、initial candidate support/utility回归和trusted-source/answer gate共存。root必要原源/owner未授，不写Book。

```text
§3.1 L126–127: original n_p<(N−1)/2 condition does not guarantee top-p frequency aggregation; p=1 is narrower setting.
§6 L205: benign top-p consistent up to permutation, n_a≤D−p.
L223–225: assume mix poisoned only with at least two poisoned fragments; x=C(N,k)−C(N−n_p,k)−n_p C(N−n_p,k−1).
§6.2 L337: FLOPs=D N R + D C(N,k) k n_e (offline embedding+averaging, not all serving costs).
§5 L202: RAGMask FLOPs=R(l_i/m)alpha p.
```


## [RSA24263 exact-v1](https://arxiv.org/html/2512.24263v1)

拟2+2+3=7：mean安全不等tail，nested风险以token-prefix递归约束后训练。actual III-B/C与IV-A Eq4–9/PropIV.1：finite states/actions、terminal reward/cost、prefix augmented value将风险Bellman重写；riskoperator类别须核concavity/translation与实际CVaR/ERM方向。Eq8参考policy advantage及KL，Alg1safe-set成本上界，不从标题或理论标签授神经训练单调/任意tail安全。必要正面采用依赖risk递归定义/实际loss、直接相关证明与评价，未读部分不隔离。

```text
L124–126 Eq4: Qc_pi(st,at)=C(st,at)+Phi^mu(V_pi(st+1)); Vc_pi=E_pi Qc_pi; Vc_pi(sT)=C(sT).
L155 Eq8: pibar_t=argmax_phat E_z~phat[Atilde^r_piref(st,z)−beta KL(phat||piref,t)].
L162 PropIV.1 requires E_z~pibar Atilde_pi(st,z)>=0 for every state.
```

### RSA必要机制/直接反证收束（作者实际读，root待核）

actual IV-B/C/D、V-A–C及A-A/A-C、B-A/B-C：risk写Concavity/translation invariance但未给所用CVaR/ERM明确方向/参数公式，不从risk名词授tail guarantee。更决定性的是Eq10成本减项与Eq12正指数不一致，而且Eq11的reward温度β与合并目标的(1+λ)β不同；这直接影响stepwise factorization和继承它的BT/SRR loss权限。只保留该中心推导争议，不宣称全部有限实测无效，也不自行修公式后称原算法成立。

```text
IV-B L187–188 Eq10:
max_p E_p[A_r−lambda A_c]−(1+lambda)beta KL(p||pref)+lambda zeta.
L195 Eq11: pr*=pref exp(Qr/beta)/Zr.
L219 Eq12: p*=pr* exp(+Qc/betaprime)/Y;
L220: betaprime=(1+lambda)beta/lambda.
L240 proof intermediate: p*=pref exp((Qr−lambda Qc)/((1+lambda)beta))/Zrc.
L244 falsely labels pref exp(Qr/((1+lambda)beta))/Zr as Eq11 pr*;
L245 then multiplies exp(+lambda Qc/((1+lambda)beta)).
L273 Eq13: Qc=beta log(p*/pr*)+beta log Y (not betaprime).
L290–291 Eq15 adds alpha and chosen-side stopgradient to BT/SRR loss.
```

最小代数反例（本次推断，非作者实验）：单state两action、pref=(.5,.5)、Qr=(0,0)、Qc=(0,1)、λ=β=1，Eq10最优p(highcost)=1/(1+exp(.5))≈.37754；Eq11 pr均匀，Eq12正cost指数归一化却给highcost≈.62246。此反例不依赖CVaR方向或神经训练实现，足以暂缓Eq12最优性与派生Eq13–15理论权限；无需扩大所有附录审计。

必要评价边界：PKU27k/3k pair labels、helpfulness129与harmfulness83不同prompt人口，DeepSeek-R1 judge；R-Judge569按风险识别F1/recall/specificity，不等真实攻击执行或罕见灾难概率。SafeRLHF直接用公开Beaver模型，DPO/RaDPO/SACPO/RSA才同轻量LoRA+4bit recipe；2H10080GB、3epoch/max512/devicebatch16/accum2/LR2e-5/BF16原设置实际披露。RSA(P) weight averaging不等输出distribution mixture，tSNE/SVM separation不认证安全manifold。TableI ERM specificity30.84低于CVaR49.07，而ERM recall更高，是受限取舍不普胜。代码未跑；中心推导修订/精确loss与risk符号实现一致后才重开本项正面采用，暂不写Books/不降7分。

## [Mirage24227 exact-v1](https://arxiv.org/html/2512.24227v1)

AB原拟7；actualmethod要求改新增命题而非借通用因果原则，拟2+2+2=6待root校准。§3.2.1–3.3实际说causal3D encoder/decoder skip破坏temporal feature distribution、ghosting，**未证实skip读取未来，撤销此前措辞**。只在最后两upsampling blocks一对一frame时注入2D逐frame feature，再用causalLoRA适配；decoder局部temporal isolation不等整条video generation可在线causal。reconstruction阶段用GT encoded latent替代denoised latent为经验近似，harmonization另训；3D粗注册后跨全video平均2D bbox修正是离线监督，非runtime真实metric地图。尚待stage/接口消融及预算反侧，不采用one-step生产SLO。

```text
L138–140: final two D3D upsampling blocks one-to-one latent slice/output frame; z2D_mid from E2D(xNI), via concat CMFB and causal Reconstruction-LoRA.
L144 Eq2: xRO=D3D[E3D(xGT),z2D_mid].
L173: global affine displacement/scale from bbox differences averaged across entire video.
```

Mirage必要局部评价actual §4.1–4.3/Tables1–4：8H200/batch8、9frame512×768，各stage10ksteps/LR1e-4，precision未披露；GT-flow warp/actor crop与fullframe不同人口，fullframe SSIM仍低于naive、warp/vFID也非每基线普胜。Table2支持3D decoder加2D feature的受限重建增益，但2D skip LPIPS退步；Table4仅H/no3Dskip、H/3Dskip、H+A/no3Dskip三组合，非全factorial，不能独立隔离injection/LoRA每项收益。Table3单换MirageDrive已增益，不能把全部结果归latent injection。原Table1 FPS只有局部生成路径且运行硬件未绑定，不能授one-step全链实时/无额外compute。准入具体对象改为最终逐frame对齐层注入静态detail的接口条件，而非未来泄露修复或整网因果；root准入/core/具体Books处置待核。
