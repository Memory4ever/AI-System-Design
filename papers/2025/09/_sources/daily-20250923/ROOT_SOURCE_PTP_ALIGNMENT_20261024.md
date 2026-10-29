# Sep23 补充：PTP 与 Alignment Bottleneck 必要证据

作者 A86 重新确认两域尚未开始/无CORE/N/在途后，root明确接受并首次准备。原A61/R44完整题摘、A62/R45日门与各5分复用，不重做；作者负责唯一非准备者回原件实际采用，再比较Books，reader后续只复用这一角色层。未预Source通过、Books或整日完成。

## 精确原件和实际范围

两独立请求均于2026-10-24 UTC00:48:47～48实际结束，200/exit0，无在途；同base raw/request在本日目录：

- [PTP 2509.15704v1](https://arxiv.org/html/2509.15704v1)，`ROOT_CORE_15704_20261024.raw`，296101 bytes，SHA256 `dcc957c96c1551493f887c70f9488de7213f3dbe721419e63ca38c295572a874`。实际读§3～5/全部公式、Tables1～4、B完整文字/C两表与D限制；B图只caption/作者解释，不称核过walnut像素，A其它可视分析/E未读，不设全附件配额。
- [The Alignment Bottleneck 2509.15932v1](https://arxiv.org/html/2509.15932v1)，`ROOT_CORE_15932_20261024.raw`，437797 bytes，SHA256 `11461d03eaea8b6908e43e1adb91705e2a4c4e5255139b4d61c3fb3072bdaf47`。实际完整读§3～8、B、E、F、H、I、J，核两阶段DPI、Fano/风险桥和KL/residual/概率权限；不称全部C/D/G/K/L、所有参考论文或实现已核。理论研究无新训练benchmark，不硬补hardware/实验曲线。

## PTP：编码、早层看图与后层少读是不同预算

§3把原图动态切成448² tiles并加global thumbnail，**每个tile已独立经完整vision encoder**。region分数来自local/global CLS cosine，再按softmax分预算；token bottom-up分数来自某ViT层CLS→patch attention，top-down来自把projected tokens和问题送入LLM第二block后、各视觉位置收到的query attention最大值。两分数经[0,1]尺度化后按alpha混合选top-k。它不是图像进入encoder前就删块，也不等只用一份廉价图像分数；完整视觉编码、CLS/attention读出、最初LLM层及排序都仍付费。

region“像整体”、CLS attention高或问题某词强关注都是选择代理，不保证小物体/细字无关，global thumbnail更不能补回高res细节。B的跨head mean/max与C的跨query mean/max是两个轴，不能把同一“max”名当同一选择；前者只作者单图描述，后者有表。若实现需要attention显式读回，还应检查fused kernel兼容和实际状态驻留，不用“training-free”免除运行成本。

**原预算/执行recipe未闭，不自行修复。** Eq2以T为全部visual tokens，local预算之和是(1−r)T；§3.4又给global Rg=rT，字面总和仍T，而不是声明的整体删除r比例。Rg还可能超过thumbnail自身token数；整数化、clip、剩余预算再分配、zero-range归一未给。top-down需要先投影并跑LLM第二层，末段又称选后才过projector/LLM，继续当前hidden还是重新prefill及旧KV/位置如何处理未交。可保层级/条件选择提案，不把这些矛盾私补成可执行压缩算法或宣称实代码必错。

§4限定InternVL2-2B（InternViT300M+两层MLP+InternLM2-1.8B）、单L20 48GB、13 benchmarks。Table1原8.42→5.71TFLOPs相差32.2%，是所报计算量，不是实测端到端TTFT/TPOT/并发goodput。Avg99.6是相对各baseline的平均保留率，不是99.6%所有问题答对，也不等真实accuracy只少.4个百分点。TextVQA71.5<72、Chart69.8<71.4等反退与MME/POPE局部更高同时保留；MME量尺与其它accuracy不同，不合拼真实错误率。

Table2层11是当前多任务折中，不是所有任务最优：TextVQA/Chart偏较浅，RWQA较深可更好。Table3 alpha.5的折中也不构成统一最佳，OCR偏.2、RWQA偏.8且GQA/其他指标另有最优；D明确其它架构尚未验证。Table4是删Region后再删b/c的顺序设计，不是完整factorial，不证明三者对所有设置均因果必要；Random/Spatial在部分SEED/GQA可胜FastV，不能由方法名推精细选择总优。

C Table5 max的Recall78.9高mean75.5，但Precision94.6低95.8；Table6 Artwork149.75>148.25，而Celebrity117.65<121.18、Posters128.23<129.59、Scene150.50<151.25，OCR/Code/数值有相同值。采用逐行原值，不能从整体perception/reasoning较高说每项都优；这些小差没有完整seed/CI，不补显著性。

全部tile编码/早层LLM、两种attention读出/归一、分区和全排序、重排/位置/KV、alpha/layer搜索与独立细字/小物体/原正确题回归均计费。precision、输入分辨率/tile人口、完整batch/output长度、测FLOPs范围和时延峰内存/SLO未充分披露，不补真实32.2%时间或内存下降。有限支持为“region预算与task-conditioned token选择是两个控制面，saliency只能提出保留集合，需按真实证据和完整执行验收”；保fulltokens、较轻剪枝、原encoder与更保守固定budget退路，不采模型无关、无损或统一recipe。

## Alignment Bottleneck：反馈带来的信息与训练拟合的复杂度分开

§3以latent目标U、公开context S、人的内部判断H和反馈Y建模条件Markov链U→H→Y|S；每stage在给定source下的可行kernel集合定义互信息上界，取两stage上界最小值。B的DPI证明支持级联信息不超过任一stage；两个独立sup的最优kernel未必兼容，因此这个min只是保守上界，不承诺可达，也不是实测“人类每秒多少bits”。capacity依source/任务/context/kernel集合而变，不能只按模型参数或反馈字数换算。

Fano下界有明确且较窄的对象：选择M个可分辨value/action原型、latent索引J在该codebook上均匀且与S独立，另需对**所有动作**成立的loss→index-error可测partition。只有这些假设下，mix风险受 `(epsilon+Delta)[1−(I(U;Y|S)+log2)/logM]+` 约束，再用同一mixture下的capacity上界替换互信息。原型之间cross-loss分离本身不自动给任意action的partition条件；real-world稀有目标、非均匀prior或混合任务不直接继承这一个难source的Bayes/minimax下界。

它不含训练样本数m，说明固定观察通道/风险对象下有无法突破的下界，**不等实际风险不能因更多样本下降直到该界**。这里的decoder只读一次测试样本的Y/S；反复为同一个latent目标新增独立反馈、多轮adaptive提问、新工具观测或channel memory会改变有效观察与独立假设，不能把单样本capacity当所有交互RLHF的数据无用定理。本文没有实验把真实RLHF的U、capacity或codebook量定下来；sycophancy/rewardhacking是解释性联系，不是其定理独立证明的因果机制。

§5的另一端首先针对可观察loss `tilde ell(Y,S,a)`，i.i.d.样本、data-independent prior Q和数据产生的随机posterior P。低经验loss与KL复杂度界讨论的是generalization，不给优化器找到好posterior的保证。Theorem2精确平方根常数作为作者援引的PAC–Bayes式保留，所读E只展开KL/MI两个lemma而非推导该版所有posterior量词/常数，**本包不将其精确常数标成已独立证明或拿来计算部署证书**；有限采用的是需要明确观测loss、prior/posterior与风险对应的接口，而非新通用常数。

E的分解 `E_D KL(P||Q)=I(D;theta)+KL(p(theta)||Q)` 和i.i.d./memoryless条件下 `I(U^m;theta)≤m(Cbar+I(U;S))` 要分开。控制有用目标信息不自动控制theta记住channel噪声/样本细节，故另假设residual `I(D;theta|U^m)≤rho`。rho大、context本身含大量目标信息或prior错配时capacity不支配上界；确定性早停/加一点噪声也不无条件给出小rho，仍需实际更新/噪声与支持约束，不能把建议当算法保证。

capacity对KL只先得到**对数据集期望**的上界；F用Markov再付1/eta和union failure概率代价，不能直接用期望代每次run的高概率KL。upper中的m*Cbar除m后仍可留下常数级项，不证明m增大会得到非空窄区间。lower针对某个难codebook mixture，upper若来自真实部署另一分布，二者不是同一条risk的上下端。

H明确需latent真loss与observable loss之间的link（含alpha/beta松弛）并且分布匹配，才可转风险。I提出canonical `tilde ell*=E[ell(U,a)|Y,S]` 的tower identity，对fresh同分布评价/给定可观测decoder成立；这个条件期望依赖未知真实posterior，不是工程师已经有可计算的reward、可观测gold或自动校准器。不能因数学定义出一个函数，就声称真实reward误差已解决。

J的data-independent有限K quantizer可令压缩参数residual≤logK，pushforward prior/posterior的KL不增加；但改变decoder后真实risk可恶化，不能签“压缩必改善alignment”或没有效用代价。本文无新对照测得容量、rho、优化成功率或完整工程费用，不能以理论框图替代实验；codebook/label定义、人的判断/表达制备、真实risk审核、capacity估计与压缩/随机化/训练/独立回归都仍有代价。

有限支持为“反馈质量受判断与表达两个有条件接口限制，增加标签量/拟合力度不消除所有不可辨识性；但潜在目标风险、反馈拟合风险和算法残余信息须分别证明对应”。不采所有RLHF统一信息上限、从proxy低loss反推出必然rewardhacking、真实人类capacity常数或无需实证的闭合性能区间。失配时保显式任务/真实结果核验、多来源/澄清与原训练基线，不由理论下界宣布扩数据无效。

两篇各原5分/候选保持；必要支持、直接反侧及采用边界足够即停，不将未核可选附件造外部hold。交作者唯一实际采用及当前owner比较，不预NC/I/DAY。
