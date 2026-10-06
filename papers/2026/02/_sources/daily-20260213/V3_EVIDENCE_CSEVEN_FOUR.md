# 02/13 CSEVEN：11114 / 11128 / 11130 / 11133

四家族准入已经root实际校准；均在已核119及新增3逐项日期交集中，只采用exact-v1必要命题。原返回CSEVENINITIAL/CORE0–3/MORE0–3/LAST0–3/FIND2/TAIL/IMPL，原L如下。CURRENT四abs轻量核：11114/11128仅v1，11130/11133当前v2但无具名withdraw/correction，不因版本号读后稿或展开版本史。以下作者必要判断待root独立核，未核代码/复现。

## [Learning to Compose for Cross-domain Agentic Workflow Generation](https://arxiv.org/html/2602.11114v1)

2+1+2=5，标准完成拟仅报告。CORE0 L126–220：workflow池按执行成败给success/failure监督，rank-r LoRA basis由task embedding composer作top-m归一混合，各adaptedlayer共享routing。multi-reference是length-normalized log-likelihood的logsumexp，不直接当真实成功概率。CORE0 L203–220与LAST3 A1.3 L373–411：移除一个basis再renormalize，测同一workflow的似然差、center/clip并按outcome符号形成proxy credit；没有重跑这个counterfactual workflow来测成功差，也不是Shapley或真实单basis因果。额外forward按E步/子样本限制，不能称无训练代价。

MORE0 L229–277：只采用reasoning/code/math，science栏目与unseen科学应用不纳本项目。Llama3.2-3B-Instruct、K8/top3、单A10035epochs/basisLR2e−4/composer3e−4；GPT4o-mini T0执行、5runs，refinement用Claude3.5Sonnet和20validation rounds，故单pass是生成器部署接口而非所有训练/执行预算等价。Table3无adaptive的math77.78高于full77.42，dense math77.58也高；K16/32退步。Table4去CCA局部反退支持训练信号效用，却不证明likelihood proxy就是实际能力贡献。数据生成/验证总token、dtype/并发/SLO、运行CI ND，Table2HumanEval分钟/parameter storage不是全任务端到端成本。

仅报告新增可学习workflow-basis与局部credit recipe：Ch81当前1032–1034已承载离线学习/solver→在线验证/回退的一般分工，不能说本算法已覆盖；这里没有新的稳定执行权限或proxy因果可靠条件，局部训练效果不强造Books gap。保留原准入及有限证据，不按科学转移或promotional“truly drive success”扩大采用。

## [Asymmetric Prompt Weighting for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/html/2602.11128v1)

2+2+2=6，反证与具体clock差额深入；拟PRE TRAIN-GRPO。CORE1 L126–222：binary reward下中心化组gradient可拆positive-negative平均方向与success边际系数，GRPO/RLOO对极低与极高success的effective coefficient偏小；Linear-R等上调低success，而不是证明经验success率准确或全错组产生正确方向。GSM8K还对zero-success先50/100stepswarmup，不能将非零advantage称必非零/正确expectedgradient。

MORE1 §4 L250–276：TinyZero Qwen2.5-3B/M16及三Linear-R runs，GSM8K Llama3.1-8B-base/M16/B128或256；低初始success局部获益。post-SFT MATH初始.38与DAPO math模型则无显著普遍增益，不能把困难题加权当所有阶段更好。IMPL L397–434：zero-success置零/换REINFORCE方向的反侧影响性能；1–2nodes×4H100/总12kH100h，各方法部分调不同LR、TinyZero RLOO2e−6vs他1e−6。正文TinyZeroB512/MATH256与Table2 256/128不一致；Table2部分clip.2与泛on-policy single-update无clipping叙述须分开，隔离统一batch/所有unclipped配置与绝对compute收益，precision/CI/总teacher预算ND。

LAST0 §5 L282–329、IMPL D1 L438–463：理论是binary、population M→∞、直接优化policy分布、KL-proximal及continuous-time、单prompt且success∈(0,1)，不是参数化Adam/clip的保证。常规update时钟与按稀有命中模型1/rho重标的effective clock不同，同积分weight budget下的optimum也不同。原Eq13首行normalizer多一个pi与下一行不一致，下一binary recursion/log-odds可独立核；不为整证明无误或Eq13执行recipe背书，主§5称Sqrt-R而实验解释L254称Linear-R optimal不统一照录。只采用**update-count效率与稀有成功rollout-cost代理是不同比较轴**，不授Sqrt-R现实compute全局最优。

actual Ch33 L472–521已讲Dynamic Sampling/全错anchors/成功边际q-loss，但尚未承载**低success regime与评价时钟改变最优weight比较**。拟接成功边际权重两段：binary方向/有效系数与稀有成功预算分轴；population clock只解释候选，低初始success vs post-SFT反侧、finitegroup/zero-success/配置不一致与普通GRPO/可靠SFT回退就近。不复制理论最优公式、全部advantage表或跨算法普遍保证。待root必要Source/current ownerPRE与Ch33窄锁。

## [Meltdown: Circuits and Bifurcations in Point-Cloud-Conditioned 3D Diffusion Transformers](https://arxiv.org/html/2602.11130v1)

2+2+2=6，输入扰动失效与activation干预反证深入；拟仅报告。CORE2 L128–202：同sphere surface/N、fixed initial noise的point-cloud路径可出现mesh connected-components骤增。healthy activation替换到unhealthy运行定位early cross-attention write，是有限controlled修复，不证明一切生成diffusion都有数学bifurcation，也不把discrete component count当连续潜在场普遍定理。MORE2 L208–258：normalized squared singularvalue entropy只proxy；PowerRemap保singularvectors、指数压低小singularvalues，gamma>1的entropy非增不等geometry/语义/安全保证。healthy patch依赖privileged reference，PowerRemap不需healthy activation但仍须选layer/time/gamma。

LAST1 B1/2 L519–563与FIND2 B3 L663–706：CFG1 conditionalstream，同seed/点数/网格与surface投影，先搜最小healthy N和失败epsilon，再只对baseline失败计C恢复为1。GSO1030/SimJEB381是该adversarial search人口，不是自然所有pointcloud风险；Make-a-Shape130/30还逐shape gamma-grid取可恢复值，不能和WaLa固定gamma100同部署协议。C=1不能证明mesh贴合GT，早期100trajectory ensemble平均平滑是直接反侧，不采用单seed所有轨迹必离散分岔。§6 L337–343明确entropy proxy粗、features意义未知、模型最优gamma不同；HW/dtype/batch/concurrency/完整SVD/search成本与CI ND。

仅报告具体3D conditionalstream诊断、受控失败及局部谱干预，不将connectedness自动升格为真实几何质量。Ch24当前138–154已区分conditioning注入、位置与语义验收，但不称已经正文包含PowerRemap；本篇受限sensor/修复还未给可迁移activation效用与真实质量成立条件，不为该局部recipe另造普遍conditioning安全机制或搬用物理bifurcation解释。准入不撤回，所有正面数字绑定失败筛选人口。

## [Just on Time: Token-Level Early Stopping for Diffusion Language Models](https://arxiv.org/html/2602.11133v1)

2+1+2=5，标准完成拟仅报告。CORE3 L147–217：top1/(top2+epsilon)confidence和已resolved邻位几何kernel→局部门槛，达标argmax永久unmask，其余仍normal transfer。未达标回到normal schedule是程序分支，不证明早commit质量/分布不变；proximity只是context-support heuristic，非真实独立性。MORE3 §5 L230–272、LAST2 §6 L353–361：Dream7B/LLaDA8B、zero-shot4tasks，MMLU3/HellaSwag5token与256/512生成不同人口，spatial窗口对短序列等价；Table1 Jot多任务低于full，threshold过激退步，不能授质量无损或reasoningtrajectory相同。

TAIL A1 L395–411：主要speedup=configured/actualsteps，另单A100墙钟有DreamHumanEval12.35×vssteps19.60×，不可混成生产SLO。Table3spatial部分任务退步，gamma/D/threshold按模型任务选择；A3 L433–440 C4 512samples/256token，GPT2-medium PPL5.94高于5.88、MAUVE .831低于.941，人类coherence未核。长窗/translation/creative/缓存组合未来工作，dtype/batch/concurrency/seedCI ND。固定argmax早退出牺牲可修改状态与探索，不推缓存组合免费或任意长窗。

actual Ch24 L300–342已经承载confidence/schedule/permanentcommit、where-to-unmask与positionbeam、entropy自适应及质量/预算回退。新增proximity kernel/threshold的有限配方及独立任务反侧仅报告，不声称此具体算法已经正文覆盖；尚未新增稳定准确性/状态权限条件，重复一般commit分工不能作Books gap。保留标准有限贡献，不照录高平均retention当全任务质量等价。

本批4项必要证据与处置已经root实际独立复核，三项Only通过。11128已实际融Ch33两段正文522/524及末注2798，root顺读连续514–533的正文/邻接与末注，非作者POST通过、窄锁释放。作者累计108/112=102必要审阅+6低分关闭，余4普通（11137/11139/11144/11146）；36实际Books POST，不授日级完成。
