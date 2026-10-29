# 12248 EBFT：必要Source、actual目标接口差额与PRE提案

mar14_supplement；03-14补充Mar13 BJT，只本ID精确v1。完整题摘/八署名及可见Comments/后v2已实际核；非准备者窄P准入通过，后v2不预认重要修订，也不混摘要/精确版本。SUP_DATE_NARROW本ID公开日夹证待root独核，不先计正式。本必要原件 https://arxiv.org/html/2603.12248v1 GET200/1083942bytes，2026-10-10T01:46:31.966636Z，SUP_NARROW_EBFT_MANIFEST_RESULT.json与SUP_NECESSARY_12248.raw/txt。

## 实际必要原证与采用界限

本人实际直读§2.1–2.4全部Eq1–11/Alg1（inspect B30–91/111–113）、主Table1全部行B92–110、§3–4/B115–146/§6B152–154，E梯度与特殊RLOO baseline Eq89–94全B423–437，F全部nested-prefix/strided mask B438–446，G完整Tables2–5/B447–496，主结果对应完整Table6各coding/translation行B497–500与H1直接α/γ反侧B502–505。曾rg长行输出截断，不用它当已读全证据，必要区间另恢复；未读D全证明、所有H曲线/例子、图片pixel、源码/复现或全部引用。D只读主文KL解释与D3声明到所需边界，不授其所有证明正确。

FM是固定feature下的条件均值匹配：每context的actor completion平均feature接近data conditional平均feature；单data参考的CFM与FM相差θ无关的参考feature方差，不等一条样本的feature距离就识别完整答案分布。§2.1的strictly-proper/full-distribution保证**要求feature丰富到均值相同能识别分布**，有限冻结网络25/50/75%depth last-token normalized feature仅“hypothesize”接近，不能认证其满足条件。Eq2的Var定义原HTML末范数没有平方，不能逐字认其方差公式已证；采用只限固定feature的均值目标和梯度构造，不照抄该印刷定义或因此宣称全部实验无效。

Eq6–7奖励是2φ(sample)·φ(reference)减2φ(sample)·其他actor samples均值：reference alignment与actor-actor repulsion各有职责，不是复制teacher hidden-state样本或最大化每条自相似。E明确普通“其余reward均值”会借其他reward的pairwise项重新含当前sample，需同时排除被中心化sample的每项贡献；Eq93–94有n−2故此corrected baseline须n>2（实验n4）。Eq94第一行仍写naive表达、后两行写修正版；本次采用独立性条件而非认证逐字各行相等。理想固定φ/i.i.d./无额外变换的score-function估计不授给任意GRPO clip/std、偏置alignment α或batch-dependent whitening实现。

所有实验用rollout second-moment pseudoinverse whitening，并只normalize alignment，diversity unnormalized（Eq8–9）；样本构造几何依赖同batch，不能由固定feature Eq7无偏性签整个Eq9 implementation。α<1进一步改变fidelity/diversity目标、H1γ0时α0/.5可CE变差；CE γ可选，不把“not tokens”讲成无token loss、无reference或无encoder监督。KL coefficient实验0，Eq10理论KL不是实际target/energy head（没有显式学χ），不授实验等价优化所有EBM/χ²/正确性。

F在同一原sequence选stride anchors、每prefix接其独立G-token rollout，mask只见原prefix和自身rollout；G次generation step并行不同anchors，不是G tokens全并行、不能跨anchors看到未来gold。feature forward可批处理并重排，但原nested prefix大多是data给的prefix，on-policy指从各给定prefix后的短rollout，不认证完整部署分布已on-policy。Quiet-STaR的mask继承不算新增执行原理。

MainTable1是best per method而非单个统一matched recipe。Q&A100k/OpenCodeInstruct、rawcode40k/Swallow、translation100kALMA，1kheldout统计CE/CFM，Qwen2.5-1.5B与Llama3.2-1B主实验、scale至7B，coder温度0/0.6、translation best-of-k是参考指标oracle取最大，不是部署selector。T1 EBFT codingpass4 .659<RLVR .660，warm .658<RLVRwarm .662；T6 MultiPL-E EBFTgreedy .524<RLVR.531，WMT22COMET EBFT.740<SFT.747、OpenSubtitles.700<.701，BLEU部分也弱。T1/6 CE数值口径不全一致（如translation SFT1.782/2.692），不拼一起证明每slice更低或联合最佳。局部收益及reference空间改善有效保留，但CFM不证明语义正确/真值或模型全部distribution已校准。

§3称twoepochs固定compute，G说明SFT基线fiveepochs/max2048、EBFTsequence1024/G8code/G4translation、n4/temp.6/stride8或2、RLVRgenerate1024/n8/temp1及不同batch，不能用相同epoch或stepexamples签总tokens/FLOPs等价。80GBH100 cluster，Q&A一epoch SFT单H100 .5h、RLVR两H100约28h、EBFT无vLLM under-optimized约36h（EBFT此句未明GPU数），precision/全并发SLO未披露，不补相同hardware数量或速度优越。冻结feature网络/多rollout/whitening/teacherreference及搜索费用都真实存在；§6承认perupdate慢于SFT。不给全修订diff或代码验证要求。

## 三维评分/actual owner（提案待独核）

Design2+Reach1+Durability2=5：新命题为固定feature的sequence-moment监督与sample-coupled reward→corrected baseline接口，改变只teacherforced CE或verifier reward的适配目标；先影响训练目标组件，不因跨章节/自定义mask/EBM名字增加Reach。可复用监督对象/样本依赖分账有稳定价值。standard必要Source已够，具体gap触发窄深入，不按耗时/参数数/Books产出倒推。

actual TRAIN-SFT Ch29 47–114完整 schema→CE数学→ConceptToken/ER-CE→跨语校准→票分布/多语hidden几何→nuisance basis已顺读。现85后“Logits仍…目标…”与既有96“多个正确推导”、104 soft-label distributions只承载token/small-category目标，不承载actor rollout均值与reference moment、actor-actor repulsion或pairwise reward的LOO依赖；292–298已有on-policyteacher/student hidden/KL桥针对逐样本蒸馏，非本目标。Ch33 58–82 reward/θ依赖/latent cluster、483/485 baseline独立及normalization分责有效复用，只作这项监督构造的具体交接，不能因已有独立原则直接NC whole新mean-objective。Ch28/30完整入口已实际读，目标归Ch29不接管通用优化/RL/rollout serving。

拟Ch29 CE数学“Logits仍…更新从checkpoint…”之后、ConceptToken分支之前窄两段（root独核后root写/本人nonwriterPOST）；保留标题“SFT的数学仍是条件最大似然”，明确新路线非CE等价实现。逐字如下：

条件最大似然适合复现经核验的 demonstration，但每步 teacher-forced likelihood 不直接度量模型自己续写后的序列分布。若没有可靠 outcome verifier，可以进入另一条 rollout 辅助适配分支：冻结一份 feature network，把各给定 prefix 下模型续写的平均特征，与参考 completion 的特征矩匹配。相应奖励既拉近 sample 与 reference，也以其他模型 samples 的相似项制约只向一个模式聚拢；这是改变监督对象，不是把 CE 换一种等价计算，更不是让 frozen hidden features 取得正确性权限。[EBFT 的受限目标与对照](https://arxiv.org/html/2603.12248v1)只在足够丰富、均值能识别分布的 feature 条件下连接完整分布校准；实际有限表示、短 rollout 与 reference 人口仍可能漏掉事实或有效模式，CE 和独立任务验收应分别保留。<!-- source-family:SF-2026-ARXIV-2603-12248 -->

这一奖励构造还要求具体采样依赖可见：其他 sample 的 reward 若通过两两相似项含有当前 sample，仅从 reward 均值中去掉当前条目，仍不是与当前样本独立的 leave-one-out baseline；须连其他项内这份贡献也排除，并按剩余样本重新归一；原修正版要求同一 prefix 下条件独立采样数 n>2，再核对实际梯度。该固定 feature 下的估计条件不能自动传给同批 whitening、偏置权重或 clipped/normalized 实现。[第33章](./33-grpo.md)仍拥有通用 policy-gradient 与 baseline 的分责。多个 nested prefixes 可共享原序列计算并批量抽取特征，但各短续写只能看自己的已给 prefix/采样历史；它不使整个部署轨迹变成已匹配人口。冻结网络、rollout、特征与统计求值、参考制备和调参均付费，作者部分任务仍弱于基线且每步比 SFT 慢；特征支持失配、行为回归或总预算不合算时，保留普通 verified CE、可靠 outcome 更新或原 checkpoint，不以更低特征 loss 自签忠实和无损。

待root实际必要原证/actual owner与逐字PRE；尚未授Source/PRE/Books/DAY通过，不写共享书。
