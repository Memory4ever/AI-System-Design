# 后续8项有限必要原证＋实际owner（待root）

8项完整exact-v1题摘已root准入校准；以下决定原文与直接反侧已实际读，坐标指`V3_BLOCKS_2602.<ID>.md` block，不是文件行。当前57家族safe/51普通；本包未非作者裁决、不提前计数。中心真实冲突单项隔离，未核代码/复现，不默认展开附件或完整proof。

## 22144 NoLan — 2+1+2=5；拟Ch23窄差额

[v1](https://arxiv.org/html/2602.22144v1)20–54/58–76/106/110/156–158。Same-prefix多模态与text-only两forward得lm/lu，输出softmax((1+α)lm−αlu)；Baseα=1，Plus用两**概率分布**的symmetric-KL γ设置α=.8(tanh(1/γ)+1)。动态幅度改变的是视觉输入相对无图语言路径的对比，而不是把γ直接认证为正确grounding；γ=0精确实现未核，不自造数值契约。幻觉组γ较小是相关诊断，图像描述/CLIP代理亦不识别所有主要原因。

Table8固定强度反侧：IB7B recall79.19→73.60/count75.33→61.67、IB13B color153.33→143.33；Plus β在部分任务也非最优，保原decode/外部grounding回退。TitanRTX24GB/50outputtokens的regular .4579s/token/13.57GB vs Base .6075/13.59、Plus .6277/13.59，不把training-free当免费/通用SLO；VCD对照同时有不同扰动接口。只采用有限改distribution机制，不宣语言prior为唯一原因。

ActualCh23 1054–1072已分visual write/prior read与shared-early-prefix late masked branch；1090–1101已有token不确定局部视觉扰动及layer/JSD selector。差额：**两完整input路径同prefix的概率差动态调contrast幅度**，不是layer selector、稀疏attention或late-branch低cost等价。拟在内部对照段后单窄段，邻近第二forward成本/固定与原路径回退，不新论文小节。若root判已有接口充足则Existing，不强造gap。

## 22145 When AI Writes Whose Voice Remains — 2+1+2=5；拟中心Disputed

[v1](https://arxiv.org/html/2602.22145v1)24–41/44–74。中心实证人口直接冲突：[26]1490texts（601Indian+261Singapore+89Nigerian+539American）“selected only if containing at least one culturally specific linguistic marker”；[27]finalcorpus **624 marker instances/mean.42**，即便American539全排除也还有951texts，不能每条至少一marker却总数624。[34–35]IER仅Moriginal>0定义且baseline texts排除；Table2[45]n1490/model，Table5[58]n7450/condition没有说明真正IER有效分母。[44]22350outputs平均.1026，Table2五同人口baseline均值.122，而Table5baseline.1156；需要明确有效子集/权重而不能照录比较。

Table3[50]624×5=3120/1657erased与macro平均可以分账，**不因53.1%与10.26%不同就另造冲突**；但marker-positive成员与测量分母不能从这些表修复。Table4定性例、preservation提示及embedding SPS有限描述保报告，不自动推RLHF原因/规模无关；seed42/t=.7亦非跨runtime确定性证明。请求修复冻结1490inputs的marker成员、有效IER分母/统计人口与一致表格，才重开中心“semantic高但identity受损”量化；已有generic metric≠identity不能用Existing/Only掩盖这一人口冲突。无Books写。

## 22146 Optimistic Primal–Dual RLHF — 2+2+2=6；拟中心Disputed

[v1](https://arxiv.org/html/2602.22146v1)59/61、78、94–112、121–129及253/378–379。Cor3.10[109–112]在boundedreward/fullsupportref/Θclosedconvex+classfullsupport/Slater/logpolicyLipschitz/inexactNPG条件下授参数化几何last-iterate→最优policy，ε=0时gap=0。Ass3.9[105]ε只与**Eq8/10期望精确NPG步骤**比较，不是与distribution-space全局prox最优比较；Alg3[78]使用F†与parameter projection。

作者条件下的有限反例（我们的推导，不是作者承认）：singleprompt/twoactions，Θ=[−1,1]，pθ(y0)=.2+.1θ²、pθ(y1)=.8−.1θ²，ref=p0，softreward(1,0)，hardreward(−.6,.4)，β=.05，ηθ=ηλ=3，初始θ=0/dual0。Rewards≤1、pmin=.2、logpolicy光滑Lipschitz、Θconvex；hardexpectation=.4−p≥.1始终严格Slater。θ=0时所有scoregradient=0，F=0/F†=0，primalpredict/actual均停0；hardexpectation正故dual投影一直0。期望精确计算→Ass3.9 ε=0。类内目标p−.05KL(p||.2)在p∈[.2,.3]严格递增，optimalpolicy p=.3，而所有iterate p=.2，KL(.3||.2)>0恒定；[253]gap(0,pmin)=0与[378]ρ<1/[379]finiteΦ使Cor3.10 RHS→0，构成中心参数化量词冲突。ΠΘ自身概率区间还是convex，并非仅以非convex可行集拒绝。需要明确能排除此Jacobian退化的额外expressivity/update条件或收窄定理后重开。

仅核采用中心和直接反例，不遍历全部appendix。Tabular理论及有限Alpaca7B/PPO经验可在报告分开保留；实际PPOclip/logdual不等精确Alg3，[124]刻意把PD放unstableregime，[126]proxy reward/safety model非物理安全。成熟optimism/PPO不能作为外围救援强写Books，中心D更准确。

## 22158 LLMTailor — 2+2+2=6；拟Existing Ch35

[v1](https://arxiv.org/html/2602.22158v1)37–77：在训练**之前**把AdamW两个全局decay/nondecay groups重排2L+x，保原hyperparameters与auxgroup，然后存layer权重及对应master/moments；YAML从多checkpoint revisions取层，LR/globalstep等取latest。此为composite训练起点，不因每层带moments就自动同一trajectory/resume；已有checkpoint未预分组不能照该方案任意抽取匹配moments。

Table1parityloss同1.58/1.60，但Table2部分task退步；filterTable4 1.58/1.60→1.60/1.62，[72]称loss decreased错误只隔离解释，不丢全有限工程。Store1799.52→899.76是累计checkpointfiles，不是HBM；checkpoint时间占比4.99→3.03/20.63→12.76也非end-to-end40%speed。Table7Llama8restore16.8s→多源279.2/332.4/1027.5s显著代价；fullfileload、合成reserialize且非lazyoptimizerI/O。8A10080GB/ZeRO3/固定1epochCPT/SFT，filterSFT task质量有负侧，不授trajectoryequivalence/全budget胜出。保coherent全量snapshot回退。

ActualCh35完整顺读后补到“有界近似恢复”正文：已明确按层累计漂移、层权重与对应optimizerstate不可拆、混合不同step并非coherent快照、每层revision/阈值/最大staleness/globaldata-RNG策略、restore重建成本与完整snapshot回退。这比原20–85状态清单/410–428转换邻接更具体，已承载上述跨revision组合边界；预先regroup工具实现本身不构成新的主线机制，故改拟具体Existing，不添重复段。原有限loss解释错误仍隔离、不因此丢弃其他有限工程结果。

## 22175 DySCO — 2+2+2=6；拟Ch22窄差额

[v1](https://arxiv.org/html/2602.22175v1)38–65/67–93/113–126：先partialforward中层QRheads，取meansoftmax并EMAγ=.75，last16tokenswarm，选cumulativemass p=.95/.975/maxK8192。对选tokens的**全部head完整forward logits加logβ**，即unnormalizedweights乘β，不是β倍logits；每decode仍读fullhistory，不减KV或softdense矩阵。QRheads/NQprofiling与MRCRdev model-specific配置是校准依赖，非retrievaltruth。

SameQwen8B16heads动态MRCR24.8→27.3，random26.6/static22.5对照支持有限query相关性；非CoT LongBenchV2有退步，PathQwen32B4K80→79，Qwen8B32K1→2也仍低。UniAttnS预算按长度调参，不说全完全matched；+约60%decodecompute，仅因长prefill稀释估计FLOP2/3.8%，非latency/HBM/SLO或省矩阵。费用/标定漂移时回普通dense/readout或显式retrieval。

ActualCh22 391–408已有retrievalheads刷新**稀疏indices**并复用KV、短contextdensefallback。差额是headscore先作**dense非删除的候选token软提升**、EMA状态随query更新，既不把head检索等于事实也不借sparsekernel收益；拟selector刷新节前后单段分这两接口。不添加新章节；若现段已足够承载则E。

## 22190 GUI-Libra — 2+2+2=6；拟Ch33窄差额

[v1](https://arxiv.org/html/2602.22190v1)76–104/112–144/152–156/186/194/197。Demo-match reward只能partialverify；非demo动作可能合法，offline-fixed-expertstate不等online-policyoccupancy。Eq7bound需online支持包含offline、demo-positive可靠、uniform perstateKL及未知validnondemoηbar/ρmin，不能从practicalmeanKLpenalty直接继承onlineguarantee。Practicalfmt.1+acc.9（valueF1>.5/pointinbbox）亦可能误签，成熟KL不新原则。

具体增量SNGS[123]：仅negativeAdv乘λg=min(λ0+κ·empirical组demo-matchrate,1)，高demo集中组保较强负更新，低match组弱化；matchrate不是validity/truth/ηbar估计，all0组仍zeroadv不救。Table10[194]4Bonline39.1→42.6/Web22.2→24.4，但offlineAClowPass1 87.7→86.4/highPass4 69.9→68.6；Table9[186]KL.001online优却offline某sliceKL0更高，不授每项互补。在线独立20/15/30step+livejudges、改Androidlabels/history与SFTmix预算分开；动作验证/采样/KL/judge/全数据均付费，回普通negativeupdate+独立execution结果，notnolabelgrounding。

ActualCh33 118–141all-zero groups、1566–1584 outcome diversity/ACE逐轨迹negative multiplier已有；Ch66 419–436 step/delayedauthority及已有partial可验证错拒root前核复用。窄差额：**组demo-match率只调负梯度强度，弱化假负例风险但不替verifier、不恢复allzero**，与ACE的reference概率逐轨迹放大方向及责任不同。拟ACE附近单窄段+note，不写GUIbenchmarkrecipe、全boundproof或成熟KL段。

## 22193 Improving Parametric Knowledge Access — 2+1+2=5；拟Existing Ch8

[v1](https://arxiv.org/html/2602.22193v1)21–77/113/115。Sameprompt加thinkcue四模型有限世界知识recall改善；math多数反退但GPT5.2 MATH90.4→91.6，故不授allmath无益。格式/readout与trace改变不能证明新latent事实被写入；EM、ExtractiveRecall、singleanswer extraction各不同。GPT-OSS20BTriviaQA RL LoRAr32/G8/1240ckpt rewardexact1/substring.5/formatpenalty，SFT40kfilteredtraces8epoch与RL不等总compute。HotpotEM7.5→17而ExRecall25.5→27.6、SimpleQA3.5→4.1、StrategyQA用training set非heldout；表73/77 answer更早出现也不证明更长真实reasoning。Cue经RL仍可追加收益，mathnocue83.9/cue80.4反侧及extra tokens/calls需分账。

ActualCh8 105–115明确base/posttraining选择重组潜在能力，systemprompt/context/sampling共同决定可调用行为且可能压制另一些能力；37–60形式/意义接口不能互签，172 capabilityceiling/reliability与采样费也已有。该有限cue/QA-RL证据不改变既有**接口elicitation≠内部因果/各任务独立验收**，具体E，不强添知识RL小节。

## 22208 Solaris — 2+2+2=6；拟Ch25窄差额

[v1](https://arxiv.org/html/2602.22208v1)45–71/73–90。两个players tensorjointattention+player独立位置/actionembedding，coupledviews≠共享真实persistentworld；P=2受限不是任意multi-agent。StagedSP→MP→causal→SelfForcing，checkpointvariant先stopgrad AR rollout/cache，再把全窗口noisy+clean concat以causal teacherforce重新计算，KV来自currentweights可反传；原采样分支仍stopgrad，并非exactfullBPTT。固定representation窗口下O(LtLs)→O(Lt)缓存比较不授总activation/HBM常数或无限world。

Table2jointvsconcat Movement68.2<77.1、Memory37.5相同，ground/build/cons提高；Table3KV-backprop视觉FID好却movement78.6→68.2/ground72.9→62.5/memory49→37.5，building/cons才略高，生成质量和actionfaithfulness分开。3repeatsVLMjudge/std不是3训练seed/真物理测量；v5p128/64、pretrain120k/因果60k/学生teachercritic预算、数据bot/render/vptpriors全付费。长teacher的接口不保证matching totalcompute或所有behavior获益。

ActualCh25 345–350已规定targetindex/context来源/detach路径与planner分账，1001–1011persistentcache+stopgrad逆序recovery也有。窄差额是**stopgrad自回归产轨迹→窗口并行重算带梯度KV→长teacher监督**的两计算图分责，直接视觉质量/动作metrics反转；拟345–350两步训练后单窄段，不单为multiplayer名字、dataset或worldspace加新段，保短teacher/短rollout与真实观测回退。
