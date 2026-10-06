# 第九包：AB6已校准主线的必要证据及owner差额

仅22603/610/617/623/631/642/647/654/681九项潜力，不重扫AB1–13或228命名目录。original-v1 ABS/HTML见V3_FETCH_AB6_NECESSARY；本文坐标对应V3_BLOCKS_2602.ID.md。全部v1 Submitted在2026-02-26UTC，早于本日公告而晚于前一公告提交截点；官方公告政策公共下界2026-02-27T09:00+08，与same-ID registered上界共同落窗。registered UTC（均02/27）：22603 02:50:15、610 :25、617 :35、623 :44、631 :55、642 02:51:11、647 :18、654 :28、681 02:52:07；上界加1秒后转+08，不将提交当公开。当前官方abs轻量状态另见V3_FETCH_CURRENT_AB6；实际当前comments为617页图数、623页图数、631为55pages、642接受KDD2026、647为KDD2026camera-ready、654接受CVPR2026，其余无comment，未出现必要撤回/勘误词信号。不把这些后续发表事实改归本窗，也不因后版编号比较全部revision。

## 22603 SideQuest — 2+2+3=7，Ch75辅助分支/主轨迹隔离

实际29–61/63–100足够。工具调用/结果以cursor组织，主轨迹每K=4步fork同上下文到专门auxiliary generation，用LoRA学del-cursor；辅助生成的管理文字不进入主回答，主工具边界检查已完成aux结果后再驱逐。未来引用不总等于显式cursor重读，hindsight最后引用标签不证明内容已失效；成功215个FRAMES轨迹构成1274aux训练人口，失败未全覆盖。distill、三个LoRA MoE层、400训练/424评测FRAMES和local BrowseComp500只是作者条件。SGLang单H100/gpt-oss20Medium改变concurrency后峰KV/吞吐改善，不是同batch/质量/SLO的生产保证；aux前向、临时KV、判断与恢复都付费，shared-prefix专用kernel未来建议不授免费分叉。

实际Ch75 385–432、563–569已有working-set驱逐、raw-artifact回源、内容效用和prefix-cache冲突/状态验证，不含**独立生成分支的管理trace隔离与主工具边界应用删除**。拟Context/Cache部分一段，保成功条件训练、future引用风险、保守完整历史/驱逐关闭回退。archive、generation/过期结果检查只可明确作本章工程条件，不归因paper披露协议。请求Ch75单段+ownnote窄lease。

## 22610 DP-aware AdaLN — 2+1+3=6，Ch28前向gain与DP裁剪分开

实际25–75/83–120，71–74截断已恢复；126–130只核界所需bounded inputs/loss/LN/谱范数，不审全部proof。condition先投影到L2球，AdaLN的shift/scale/gate用tanh限幅，再走相同C=1/σ的DP-SGD。Table3裁剪频率.561→.556/.589→.585近似不变，主要是尾部裁剪严重度改善，不授普遍少裁剪。Eq10由两个敏感度上界相除不能证明真实敏感度比率；隔离该比率/更强privacy保证。single PrivatePower/ETT按时间切分、rolling windows不自动满足用户级邻接；ε/accountant/全硬件精度ND，matched Cσ不认证privacy预算。八层TimeDiT/20K/B96/EMA有限控制，单边限幅不如联合、hard-clamp/STE更差；限幅会丢condition信息并需bound搜索，在线private校准只是未来建议。

实际Ch28 476–489已有privatized-gradient之后的filter/Adam noise校正，缺**条件路径在前向限幅以减少全梯度裁剪的collateral，不能代替DP accountant**。拟该段后一段，保上界与实际比率分责/ND、控制负侧与原DP-SGD/重新校准回退。请求Ch28窄lease。

## 22617 Semantic Tube Prediction — 2+1+3=6，Ch28同forward表示prior

实际23–48/49–64/65–86/88–118/192–196足够。保NTP，在末层同一真实序列随机s<r<t，加1−cos(h_t−h_r,h_r−h_s)，无外部teacher/predictor、推理不换路径。五seeds/成对检验支持有限任务；LLaMA/Qwen等NL-regex/math/SQL/QA，lambda单独搜索并随任务改变，投影predictor反侧较差。n倍少unique样本同时n倍epochs匹配近似steps，不等少tokens/FLOPs或违反Chinchilla。Theorem3.3需局部线性h*与hidden端点对应；BOS/EOS token同名不自动使h=h*，不采通用geodesic/no-collapse保证。regex等价.*类不平衡代理不是开放语义真值，SNR未直接测；训练activation读出/采样/λ与重复runs都计费。

实际Ch28 71–87已有future-token/teacher-hidden/rollout三种额外目标，缺**不增加future标签、只约束同forward三个hidden位置方向的表示prior**。拟这些辅助目标后单段，保局部直线prior可失配/目标竞争、unique-vs-token分账与NTP/关闭正则回退。请求同Ch28第二窄段，不追加理论尾注外置机制。

## 22623 ContextRL — 2+2+3=7，Ch33privileged过程verifier与rollback credit

实际48–83/85–128/163–168，109截断已补。teacher参考带gold/完整解法，过程verifier比单final oracle更严格；整组negative才生成mistake report→带原失败回答和报告二次rollout，过滤standalone表述后回到原x计算offline-positive+online-negative训练credit。standalone文本不使条件生成分布on-policy/unbiased。负例验证率95.8%来自原法拒绝且235B一致的30K中随机1000，是选择条件precision而非所有过程accuracy/recall。QwenVL8/32teacher/~250K筛出16K VQA+14Kmath/16K输出/八H800/oneepoch，SFT五epochs-best vsRL-last预算不全同；γ/λ/selective-KL和额外反馈rollout/teacher均付费。去某组件部分任务反而更好、gold/reference会传播错误，报告新增17%代理不等Shannon information。

实际Ch33 269–314已有reference partial-credit/首错边界及可靠terminal oracle，缺**全negative条件下用privileged错误反馈生成conditional成功，再明确回滚条件输入后的credit支持**。拟首错机制附近一段，只采用可定义训练接口/局部控制，保反馈权限、offline-support与额外费用，不采faithful internal reasoning/无偏保证；回退outcome-only/可靠process verifier。请求Ch33窄lease（与22576/其他本日段同owner分开）。

## 22631 TorchLean — 2+2+3=7，Ch49shared执行/checker IR与数值trust edge

实际19–42/43–63/186–191/206–213（32–35/54–58截断均补）足够。shape-indexed op-tag SSA/DAG在spec/eager/tape与formal-graph编译/checker共用；所谓compiled不是Torch高性能fusion。real-number reverseAD及受限IEEE32核心是不同语义层，Float32/64 opaque runtime与外部Arb/FLINT oracle仍trusted。tanh/exp endpoint不是已证transcendental enclosure；硬件FTZ/FMA/reassociation/并行reduction refinement未来未完成，不授end-to-end GPU证明。IBP/CROWN witness局部检查不检查完整branch-bound内部/全域coverage。小MNIST/ACAS/控制器支持受限可执行接口，Float64demo不等IEEE32proved路径；1212s vsPython .015s体现显式算术成本，PINN只是原例不纳AIforScience。未遍历code/proof。

实际Ch49 81–120拥有lowering/语义回归、顺序spec与parallel annotation边界，缺**同一NN中间表示生成execution和checker，而scalar model、外部numeric oracle与hardware refinement分别作为证据边**。拟顺序spec小节一段，不重复泛proof词或声称完整Lean runtime可信；保限定算子/域/成本与原runtime+差分回归回退。请求Ch49窄lease。

## 22642 CEEH — 2+1+3=6，Ch33历史difficulty/entropy/length目标

实际21–52/53–64/65–82/83–109/120–124（86–87补）足够。asymEMA per-question success估difficulty，仅hard题增加detached entropy advantage（EA）或多epochs（ME）；仅correct且当前accuracy超过history时，以历史最短correct长度作penalty anchor，mean-only非std GRPO。定义新condition而非泛length组合。必须隔离两保证：Eq11 cos(πt/T)后半负，不是始终非负退火；Eq13correctlong没有硬上界，β=.1且L/Lmin=12时correct总R=-.1<wrong0。只可采用EA/实际定义有限目标，不替作者修code，不授correct always>wrong。R1Distill1.5/7B、5Kmath/B512/G12、LoRAr32/16A100/20,480train/16Ktest作者条件，Avg16/pass@16不是部署oracle；MEAIME25反退、较强length项hurtaccuracy、部分baseline原paper不同预算。历史记忆、rollout、entropy与调参费保留，不把tokens降算墙钟。

实际Ch33 269–279与22556段已有reference tolerance/正确短bonus/length token-SUM，缺**题目成功历史决定是否鼓励entropy，并用历史短correct作长度锚点**。拟现有长度reward段后单段，明确EA与ME分支、经验边界/两个误授隔离，关闭length/entropy或普通outcome-only回退。请求Ch33第二窄段。

## 22647 STATIC — 2+2+2=6，Ch51静态shape约束mask

实际54–88/94–119/137–155/184–193，73–74截断已恢复。semantic-ID trie转CSR row-pointers/token/nextstate，浅层d≤2 dense mask，深层按层最大branch B固定gather再mask padding，维护每beam node并随topbeam更新；stacked(token,nextstate)减少双fetch。XLA静态shape而非CPU动态指针主导选择。Alg2 DynamicSlice与A1 jnp.take(fill)接口不相同，terminal/边界/duplicate scatter正确性需实现条件，故不授所有padding/完整code机械正确。单TPUv6e/3B/8tokenSID/V2048/perchipB2/beam70/20M限制集，100次mean±std与PPV exact对照支持mask kernel延迟；0.033ms是constraint per-step增量，不是fullserve加速千倍。PPVtop50和Bloom含近似/2.1%假阳性不可同exact合并；HBM约1.5–1.8GB/20M、dense |V|^d、branch B过VMEM后线性；GPU portability不是实测CUDA生产。作者YouTube A/B确有应用经验，但不认证任意任务语义/安全/production SLO，precision/SLO未披露。

实际Ch51 117–150已有CPU grammar-state瓶颈、mask合法性/学习propagator与输入span语义，缺**将固定长度可枚举ID约束编译为静态shape CSR/gather并分摊浅/深mask资源**。拟CPU瓶颈后一段，保算法接口边界、受测increment-only预算、HBM/branch/dense费用与CPU trie/普通grammar实现回退。请求Ch51窄lease，不声称SGLang已实现此paper。

## 22654 DPCache — 2+1+3=6，全局最优中心主张需独核

实际23–59/61–81/86–88/112–114读足，非全部Appendix。最后层feature依前两个computed anchors预测，PACT(i,j,k)累计中间L1 proxy，十样本calibration与K/M选择可给经验schedule，但Eq8 D[m,k]仅保存单前驱P[m,k]，一般三点cost不满足该压缩最优子结构。最小非负例T=8/M=3/K=6：固定8,7,6，A=8,7,6,5,3 cost0，B=8,7,6,4,3 cost1；C[5,3,2]=100，C[4,3,2]=0，C[3,2,0]=0，其他未指名合法cost1000（前三固定段不计）。D[5,3]选A而删除B，终值100漏真实最优1。C[7,6,5]=0/C[6,5,3]=0，C[7,6,4]=1/C[6,4,3]=0具体定义两前缀成本。要普遍求此surrogate最优须保前两关键steps，不能本笔记自造修复当paper已实现。

单H20/FLUX1024图200prompts、HunyuanVideo640×480×65/VBench4730、DiT256/FID50K作者实验有matched-like latency controls及3D/2D/累计消融，但采样/precision/SLO和重复置信不完整；FID/VBench仍低于baseline、轨迹匹配可继承错误/放大花盆artifact与多样性损失。最后层feature成本proxy不授真质量optimal、十sample好不授content-independent普遍定律。Ch24 1299–1330已actual承载trajectory-conditioned cache-error、prior/schedule identity/quality-fullcompute反側。请root先独核中心最优反例并决定安全D或是否仍有独立窄经验差额，不因原名造gap；目前不写Books。

## 22681 LITE — 2+1+3=6，Ch28按曲率子空间分配update

实际70–133/147–158/162–171/173–186/195–215必要接口、假设、控制足够，不展开J全部proof。Muon用momentum covariance NS-filter估sharp投影，SOAP用自身preconditioner eigenspace softthreshold，complement提高χ/β2；sharp与flat不同coeff而不是统一调大LR。toy block eigenspacealignment是proxy假设，continuous River/smooth/common-eigenbasis/Tmax、正β1理论不自动覆盖离散noisy LLM；真实Muon最优β1=-.25，隔离理论无条件签实际配方。NS近似/阈值反馈不是exact Hessian oracle且有搜索成本。统一β1/2使.25Bterminalloss2.113/2.129比Muon2.110差，L与H单开又不如联合；输出head排除因风险/小收益。C4/Pile130M–1.3B/QwenMoE1B有限训练，250M搜索迁移其他sizes但MoE另搜，不授所有LR迁移。40×/100×/200×tokens loss等价省steps不是总FLOPs；AppendixB1单8A80080/1.3B/seq1024/global8192/micro16吞吐100.4K<101.5K tokens/s约1%费，非全配置零开销。其他训练预算/精度/跨seed不确定性ND。

实际Ch28 327–358已有低秩ZO几何、stabilityindex、decay/recipe，缺**借preconditioner的受限sharp/flat proxy，将稳定coeff与flat drive/damping分开并保projection成本**。拟Optimizer不是独立旋钮小节一段，只采用可定义离散机制/反侧，不采理论为大型训练证书；谱/阈值失配或quality退步时回原Muon/SOAP/tunedAdamW。请求Ch28第三窄段。

2026-10-06 fresh非旧作者22654独核：原v1 blocks38～59/Alg1/Eq6～8及必要经验反侧已实际读，单P丢路径状态中心保证判D/noBooks，不指控未读code或全部经验无效。独立补强到真实1D两cache线性外推cost：h(t0..8)=[0,3,5,−4,5,1,−3,−4,−4]，T8/M3/K6，C[i,j,k]=sum(t=k..j−1)|h[t]−(h[j]+(h[j]−h[i])*(t−j)/(j−i))|。按原Eq8得到path8,7,6,5,4,2,0/cost31；枚举固定8,7,6且相同K的可行paths得8,7,6,5,2,1,0/cost88/3。非仅任意C抽象反例，不称这是真实模型实测。重开只需充分path state的最优性/对应实现和评价身份，现有Ch24已具体承载有限经验缓存误差/质量回退。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22623：原必要blocks48–83/108–111/116–122与actual owner独核；Ch33正文285/完整273–293/own2954 root非写入者actual POST通过；22642：原必要blocks32–64/85–88与actual owner独核；Ch33正文287/完整273–293/own2956 root非写入者actual POST通过；22610：原必要blocks44–60/94–109与actual owner独核；Ch28正文494/完整478–507/own1805 root非写入者actual POST通过；22617：原必要blocks36–47/64–83与actual owner独核；Ch28正文84/完整65–95/own1807 root非写入者actual POST通过；22681：原必要blocks76–113/173–182与actual owner独核；Ch28正文359/完整327–375/own1809 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
