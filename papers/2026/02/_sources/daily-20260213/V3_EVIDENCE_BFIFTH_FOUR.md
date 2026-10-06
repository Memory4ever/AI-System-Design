# 本日B必要证据：10635 / 10639 / 10652 / 10657

四家族准入已独立校准；前三中10635为新增3日期包络之一，其余119交集。均exact-v1，未复现/未核实现。当前官方abs轻量核：10635有窗外v2/v3、10639有窗外v2，未见撤回/明确纠错声明，不无差别比较；10652/10657为v1，10657首abs503后exact-v1成功。作者支持/直接反侧足够即止；root已实际独立语义核四项必要证据与Only Report处置通过，包括10657关键Table4及多语言直接反侧，不声称无差别第二次全文附件，日级未授。

## [HARPO](https://arxiv.org/html/2602.10635v1)

5（2+1+2），标准；采用两层relative advantage modulation，不将社会行为应用本身计贡献。§3.2平均abs normalized advantage作sample/task contribution proxy，geometric参考的inverse ratio分别乘回，再EMA proxy/multiplicative inertia。geometricmean(s)=1仅消除所有factor同时同方向缩放，不能证明sum gradient/norm或totalstep不变；proxy没包含score-function梯度方向/幅度，不是真实task contribution或公平保障。

Alg1/L330–397 epsilon只显式在group std，p及geometric ratios可能遇到全同reward/零信号，未披露所有零值/新query inertial初始化边界；不采用通用稳定实现保证。主式KL β有而C1实际omit KL，不以主式担保训练trust region。Qwen2.5Omni7B/HumanBehaviorAtlas约100k/10tasks/13datasets，同base和reward下比较GRPO/RLOO/GPG/RE++，baseline沿各原超参，不是所有优化条件相同。5epochs上限/val每50step/250step无进步earlystop、按bestval选checkpoint，B256/PPOmini128/G5/prompt4096/response2048/AdamW/LR1e−6/βρβs.95，4H200+4RTXPro6000 Blackwell，precision/训练多seed/完整rolloutcompute ND。

§4.5 matched主要component ablate：samplelevel/structured/inertia删除后平均rank1.9→2.6/2.0/2.7，rank不是连续公共效用；samplelevel对EMO/INT/SOC没明显改善，SOC25.40仍低RLOO29.54/GPG27.93；体外逐任务指标与judge不混。医疗状态标签成绩不作医学指导。拟仅报告具体twolevel weighting与受限多任务反侧，缺真实梯度贡献识别/一般zero-signal处理或稳定预算边界，不把几何均值的成熟恒等式升级长期算法保证。原源 INITIAL_0 Source113–199；CORE_0 226–253/463–471；TAIL_0 330–407。不因学术应用范围排除已准入模型优化方法。

## [VideoSTF](https://arxiv.org/html/2602.10639v1)

6（2+2+2）安全/可靠性反侧深入。III-A RR是输出存在重复5gram（maxcount>1），RI/IE按unigram统计；这些是可版本化退化sensor，不等harmfulness、事实错误或真实DoS。10k视频testbed来自4公开instruction数据、最长180s，测试10VideoLLM与8/16/24/32sampledframes，forced sampling修改部分默认行为；greedy do_sampleFalse/T0，不能归因仅温度随机性。exact permodel testK、完整prompt/max-outputlimit、hardware/precision/batch/SLO ND，不用10k testbed规模自动冒充每个对照实际样本数。

III-C/IV-C Add/Delete/Replace1–2帧、Reverse/Shuffle；delete1遍历每帧，其余随机30trial，Reverse单一。Reverse/Shuffle不保持真实时间语义，Add/Replace冗余亦可能改变问题条件，不能统称语义保持的因果干预。IV-D attackset只原本非重复outputs，max30query直到RR触发，AQ只成功subset非全测试平均；表III的98%是受测模型/变换/frames局部RR，不能叫所有系统98%安全失败。初始重复强弱异质、同模型frame数量不单调，未控制训练原因。到tokenlimit不等已测shared service exhaustion/tenant DoS，未做防御可靠性保证。

拟仅报告：具体temporal输入压力→生成重复的有界失效切片成立，但mechanistic cause/完整服务成本和真实语义鲁棒性未证。Ch66实际219区分退化输出与安全classifier假阳性，3050–3055只授有限audit；不假称其已有VideoSTF精确metric/全部temporal保障，也不以n-gram重合直接授新安全设计。原源 INITIAL_1 Source84–155；CORE_1 268–275/表II-III；TAIL_1 275–286。无需全攻击prompt附件。

## [UMEM](https://arxiv.org/html/2602.10652v1)

5（2+1+2），标准并定点可能memory差额。§4 sourcequery之外BGE-M3 cosine TopN邻居（AlgF明确D除自身），对memory前/后由同frozenexecutor评正确性差，加双方都correct时length ratio效率奖励，再fmt XML/GRPO；训练max组候选reward后提交bank。需要邻居GT/环境正确性反馈及双执行，短输出不是普遍更正确或免费；retrieval相近不等futureutility相同。

MMLU约2k训练、N3/K3、Qwen3-8B executor；1B/4B memorypolicy跨GPT5.1/GeminiFlash有限评价；B128/G8/3epochs/LR1e−6/KL.001/clip.2/trainT1/evalgreedyT0/16A100约11h，precision/总executor评分/online训练额外budget ND。Table2N1/5退步但N5仍在Qwen HLE及ALFprogress略高；去SNM在Qwen ALFsuccess52.99高full50.75，不授N3普遍最优或每组件必要。持续memory实验同有限QA/ALFWorld、10epochs重复不是新任务无限stream与永久记忆质量保证。

AppC actual证明仅normalized embedding的retrieval score Lipschitz bound，L287进一步声称TopK高度重合缺ranking margin；不由它授检索集合/真实reuse/因果保证。MainTables含原方法各任务反退，不称architectureagnostic普遍效果。Ch77实际1391–1393已承载同futuretargets、前后memory效用差/reader成本及不等因果、154–156 localproxy非真值；具体邻居选择recipe是有限proxy近似，不新增普遍memory可靠性条件。因此拟仅报告（不是该公式精确已有覆盖），保留source排除自身与邻域偏差/额外correctness评测成本，不造重复正文。原源 INITIAL_2 Source95–155；CORE_2 173–216/259–285；TAIL_2 Source285–287/310–339。

## [Word overlap](https://arxiv.org/html/2602.10657v1)

5（2+1+2），实际评价反侧深入。§3 simplewhitespace/casesensitive/noNFKC、Laplaceadd-one empiricalwordunigram crossentropy与绝对wordcount分开，crossentropy=benchmarkentropy+KL仅同benchmark下分布差；不采用文中一般higher-order投影误差“dominates”的无条件理论说法。不是检测exact样本污染，也不是词频因果干预。

GPT2tokenizer/Llama400M/1.33B/3.36B nonembedding，8.5/26/60Btokens/FineWebEdu/DCLM/C4/OpenWebText、AdamW(.9/.95)/decay.1/clip1/cosLR/warm350Mtoken，10zero-shot benchmarks，5独立训练子集有限平均std；训练seed与subset抽样未单独分解、HW/precision/batch/context/evaluatorrevision完整成本 ND。Table1–3fixedscale跨corpus相关，corpus同时改变text质量/句法/主题，不能隔离word-marginal因果；8.5→26B同时增加总token与steps，不是只改wordcount。§6.1 benchmarkrareword synthetic/penalty方案是提议未实际实验，不声称已操纵benchmark成功。

直接反侧§5.1 BLiMP排序逆、MathQA与多语言PIQA/LAMBADA不满足proxy趋势；seenwords几乎全覆盖不等任务distribution同。§7.3 crossbenchmark entropy不是difficulty，短bench估计噪声更强，只同bench比较corpora。Ch66实际3846–3866要求干预/clean counter才归因污染、相关construct生态分账已承载不从观测相关得到因果；本篇窄proxy观察没有识别泛化/真正contamination，拟仅报告，不授“benchmark都weak OOD”“无需context推理”或按公开bench词频优化通用数据质量。原源 INITIAL_3 Source91–195；CORE_3 198–233；TAIL_3 234–249。支持与反侧足够，未遍历全部benchmark附件。
