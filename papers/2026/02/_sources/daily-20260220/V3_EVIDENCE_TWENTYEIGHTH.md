# 02/20 第二十八有限证据包：运动学状态、LDP 后处理与 DP-DRO 定义域

## 2602.16356v1 — Articulated 3D Scene Graphs for Open-World Mobile Manipulation
2+1+2=5，拟 MULTIMODAL-WORLD-MODELS Ch25 persistent-state 后一窄段与自身末注。exact-v1 V3_REVIEW_2602.16356v1.html actual §III:111–161、数据164–173、TableII234–291/讨论296–297、匹配383–389、containment375–384、限制437–440实际读。日期桥09:00下界，sameID Registered02:44:14Z+1秒upper10:44:15+08；官方abs无可见撤回/纠错。不是scene graph名称映射：static persistent address不足表达可动父对象与开合时才可见的child，需要关节模型与当前状态/parent-child运动关系分账。

RGB-D/pose与hand/warp prior分割interaction；3D point tracks拟合twist ξ与观察到的θ，cosine先验加twist regularization分prismatic/revolute，而非语义模型直接授物理参数。点移动10cm gate，1500 queries/stride2、24GB VRAM；公式ω=0归一不可直接原样实现，不采全公式证书。Object masks几何merge/border可靠性，再按joint motion重放点云，binary integer assignment匹配part/articulation；max-open/closed识别containment与STATIC世界固定/ARTICULATED随父运动。姿态/深度和segment模型错误会组合传播，遮挡当前看不到不等永久无child。状态估计通过articulated点云overlap，控制器仍拥有行动/实测刷新。

Arti4D 62 RGBD视频、5scenes、约600human/teleop interactions；主要下游用GTinteraction segments，非完整自主pipeline。Ablation type/axis改善但无需每metric全胜；contained IoU .091/recall .166/relation .592，保组合错误反侧。DROID19demos，HSR/Spot局部操作，不能授任意embodiment/controller/safety；不采用>80%为通用成功率。真实pose/depth依赖、镜面noise、real-time action recognition瓶颈，semi-static rearrangements仍future。precision、pipeline latency/concurrency/tail SLO未披露。

实际Ch25:374–380已有camera-invariant persistent position，382–396 address/content与逐对象write gate，443–476 geometry commit边界，未含kinematic model/current state/containment运动类别分账；Ch26拥有执行反馈/safety，不复制controller。拟 Ch25 persistent-state解释后、Object Address小节前一段：ξ/θ与父子运动/可见性状态分离，model+mask+pose版本和观测刷新是工程要求，有限GTsegmentation/containment反侧及建图/匹配成本，保static map/新观测/受控interaction回退。待rootPRE，未写。

## 2602.16436v1 — Learning with Locally Private Examples by Inverse Weierstrass Private Stochastic Gradient Descent
2+2+2=6，拟 PLATFORM-SECURITY Ch72 one-sanitized-root 后窄差额深入。exact-v1 actual §2:152–177/§3:178–234、Ass4.1 241–243、§4:253–269、§5:274–346/closedform351–382、匹配§6:385–402、necessary D7:1061–1083/E:1159–1163实际读。sameID Registered02:46:08Z+1秒upper10:46:09+08；官方abs无可见撤回/勘误。

一次Gaussian features+RR binary labels发布，εx+εy组合，后续不是再拿raw私有数据查询。Gaussian expectation是Weierstrass smoothing/RR是Bernoulli混合，直接noisy-risk优化会改目标；在Φ函数regularity与σ²<1/(4a)下，逆变换构造loss/gradient期望无偏，不恢复某个用户原记录。二次/指数loss有closedform，两label evaluation与校正项，general loss可能高阶Laplace/truncation；logistic不属函数类，D7明确更大K未必更好，不借有限logloss实验授精确无偏。反侧与代价：variance随privacy/函数增长，有限样本残差、投影域和numerical cost；single-pass theorem每record只使用一次，以独立fresh样本保条件，重复使用同一release的privacy仍postprocessing，但不继承IID无偏SGD收敛。O~1/n需bounded feature/parameter、strong-convex/smooth risk与特定stepsize，非DNN普遍收敛。

有限binary linear exp-loss+L2实验，same release/noisySGD/raw baseline，synthetic n1e6 p2/10，privacy2/5,δ1e-5，100draw；Folktables两任务五大州random80/20，100noise draws。主文features含SEX，附录只列AGEP/SCHL+第三项，不能合成一份精确feature配置；均保有限线性实验，不纳领域效果。batch128/50、γ1e−4/2e−5、L2=5/10，hardware/precision/wallSLO未披露。Average-model risk非一次模型risk；variance residual明确存在。

ActualCh72:455–471 one sanitized root/release cache解决重复发噪与组合，394–443定义unit/accounting+utility独立；不含sanitized root上非线性learning目标偏移/逆算子有条件debias与方差/截断分账。拟在root subsection末注03188后加1段：一次release可privacy复用不保证目标相同；conditioned gradient debias而非记录逆解，loss/噪声参数/截断版本binding工程，成本/非凸及复用收敛边界；不采用全部variance/率公式，保普通LDP统计、task-specific/interactively accounted学习或收窄发布。待rootPRE，未写。

## 2602.16155v1 — Differentially Private Distributionally Robust Optimization with Non-Convex Losses
2+2+2=6，拟中心定义域/目标桥 Disputed（待root独核），不降分或删除反侧。actual §2:138–169、§3:172–237、§4:240–247/378–429、匹配§5:431–466及Tables2/3已实际读。Registered02:39:33Z+1秒upper10:39:34+08，官方abs无可见纠错/撤回。

原增量为primal/dual不同smoothness分别SPIDER refresh/difference+Gaussian，与KL compositional estimator。保这些作者描述，不授完整DP/utility证明。必要直接冲突：
1. Eq2固定λ0的divergence-penalized目标，与Eq5优化λ≥λ0并加λρ的radius-constrained目标不是同一个给定fixed-penalty问题；§4/Theorem4继续用原F记号，需明确目标身份和stationarity转移。简单固定x loss=(0,1)、KL与λ0=1，penalized value log((1+e)/2)=.6201；Eq5取ρ=0及λ→∞极限.5，已经不同。不推翻标准各自的DRO duality。
2. Algorithm3:391 w0=0使当前λ=0，而§4 λ≥λ0>0需exp(loss/λ)；无约束projection。421 st=有限clipped term+Gaussian，σst>0时Pr(st≤0)>0，425直接log(st)，没有positive floor/rejection/domain规则。因此作为随机算法有非零概率无实数输出，不支持“Algorithm3按该描述为(ε,δ)-DP且给stationary utility”的完整可执行桥。补floor属于postprocessing可保已有privacy，但会改变bias/utility，需重新对应证明；不能擅自替作者补齐。
3. Table1 χ²给ψ(t)=.5(t−1)²（t≥0）但ψ*(u)=−1+.25(u+2)²，u=2时Table=3；定义sup_a[2a−.5(a−1)²]在a3为4（完整piecewise为u+.5u²/u≥−1，否则−.5）。这个具体归一/域错误只隔离依赖该表实例，不称全部ψ理论错。Ass3 bounded-domain/nonnegative不显然涵盖Table KL/χ²，不拿“mild”标签外推。

ResNet20/CIFAR10-ST人为imbalanced/MNIST-ST binary/其余Fashion/CelebA、batch128、KLρ.5 λ0=1e−3、δn^−1.1，没披露总epochs/tuning/hardware/precision/运行SLO，不授LLM净加速。Table3局部accuracy与MIA five seeds保报告，MIA低不是DP证书：DS ε.1 AUC .9719 vsRS .8234，不能仅据AUC宣称DP数学失效或更小ε。Ch72:516–535已有mechanism/accountant同构与audit下界边界，Ch28优化界不替general quality。NoBooks；重开精确同版correctedAlgorithm3 domain/λ约束、fixed-penalty vs radius目标证明及χ²实例更正，再只审受影响privacy/utility主张，不要求所有附录或后版本比较。

## 停点
上述三项均普通必要源/owner工作已准备；尚无rootPRE/隔离终态，仍不可记本日完成。没有外部访问缺口，冲突只申请precise中心Disputed采用边界。

## 独立必要处置追加（2026-10-05）

root actual source/owner PRE通过16356、16436；16155目标/算法域/χ²实例中心争议限定隔离通过，保标准DRO duality/局部评价，不据MIA否DP。16356已写Ch25 body382/own1587，16436已写Ch72 body475/own4234，作者完整邻接实际顺读，两文件限定diff-check通过，实际POST待root核。初筛16436/16155为2+1+2潜力；实际准入命题贯穿一次私有release→下游estimator与DRO objective→private estimator/accountant，Reach定为2，当前2+2+2=6；不是因深入耗时、冲突或Books决策加分。仍未日级验收。

最终两写入root非作者actualPOST通过：16356 Ch25正文382/374–392完整邻接/自身末注1587，16436 Ch72正文475/455–479/自身末注4234；机制、成本、反侧与fallback衔接有效，两锁释放。96家族冻结（58实际Integrate+15Disputed+5Existing+18Only），无作者普通待办/未核POST；日级最终六部分仍待root非作者独立验收。原43/93/等数字为历史停点，不覆盖本次。

## 正式日级终态（2026-10-05）

root最终非作者六部分/14每日来源和触发入口有限停止/隔离边界验收通过；全部拟入选及58实际POST复用有效逐项结果，分层负侧完整题摘10具名与Comfy实际precision patch及16608/16241已核，16640“无precision对照”排除理由纠偏但EX/96不变。README已同步完成态96=58Integrate+15Disputed+5Existing+18Only、普通待办0；完成态validator实际通过，本日及所授owner限定cached/unstaged diff-check通过。外部目录/日期/身份/中心争议不授正面Coverage/Evidence、Books或无遗漏。只结束02/20并释放自身日文件及Books ownership，不接他日；未stage、commit、push。
