# 02/20 第四批有限必要包：16065 / 16066 / 16488 / 16165 / 16198

作者 feb20_v3。只列实际所读的核心、关键比较/反侧与 owner 差额，未核实现或复现；不授日级验收、不冻结候选。这五项拟2+2+2=6，具体理论反证/owner差额按受影响命题深入，不要求无关附件。最新：root已实际核五项必要原源/owner PRE，16065中心争议隔离通过；16066/16488落实Ch29:331/620，16165落实Ch32:103，16198落实Ch24:260，四项正文/完整邻接/末注非作者POST均通过并释放窄锁。下方原计划中的待核文字仅保留写前理由，不覆盖本段实际结果。

## 日期与当前事件

沿已独核的 arXiv 公告/ID/DOI桥接，Submitted给最早announcement下界02/19T09:00+08；同ID arXiv-issued DOI Registered+1秒给公开上界推定，Created/Updated仅原字段。实际各 `V3_DATACITE_2602.<ID>.json` 与 `V3_CURRENT_ABS_2602.<ID>.html` 保留原值。

| ID | v1 Submitted UTC | Registered UTC | 公开范围（含起、不含止，北京时间） |
| --- | --- | --- | --- |
| 16065 | 2026-02-17T22:38:18Z | 2026-02-19T02:37:24Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:37:25+08:00 |
| 16066 | 2026-02-17T22:44:10Z | 2026-02-19T02:37:26Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:37:27+08:00 |
| 16488 | 2026-02-18T14:22:13Z | 2026-02-19T02:47:23Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:47:24+08:00 |
| 16165 | 2026-02-18T03:31:34Z | 2026-02-19T02:39:47Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:39:48+08:00 |
| 16198 | 2026-02-18T05:44:19Z | 2026-02-19T02:40:33Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:40:34+08:00 |

五项当前官方题摘/Comments/history已有说明实际有限读完，未显示撤回/纠错安全标记，不由此证明全历史无修订。16065/16165当前v2，分别定点取 `V3_ABS_2602.<ID>v1.html` 实际读完整精确v1题摘；不凭version号遍历later正文。16065 later题摘的real images/texts不迁回v1；16165 later ICML Comments不作为本窗发表事实。其余当前只有v1。

提取行号均为同目录 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`，章节/公式为主定位。

## [Contaminated Recursive Training exact-v1](https://arxiv.org/html/2602.16065v1)

§3（77–116）A1为凸模型类Q上对iid n样本统一成立的baseline收敛界，A2为凸metric；每轮取得新m1真实样本与新m2前代synthetic，并累计所有旧样本，α=m1/(m1+m2)固定。Th3.4给t^-min(p,α)，p=α还有log t；§4（127–150）偏置真实来源须在同类Q且误差随t^-q衰减，固定偏置不能当真目标恢复。

中心必要反侧在B.1（604–645、684–709）：证明把A1用于累计混合Q_t，直接使用baseline对Q_t的界；但累计样本来自跨轮异质/依赖于前代模型的来源，不由已写的iid统一类假设自动得到这一步。需额外说明适用于该依赖/三角样本人口的统一学习界，不能把条件不闭合写成通用LLM convergence，也不武断称所有局部递推为假。§6（272–293）实际v1是MNIST视觉，300图/轮、三种α、150epoch×300轮、网络不重初始化，无高维W1测量/收敛速率统计；§7（294–303）likelihood/CE/KL不满足所用理论条件，现实筛选/RLHF/curation未覆盖。

actual `TRAIN-DATA` [Ch27](../../../../../books/part-04-training-system/27-data.md):368–399已具体拥有corpus/parameter recursion、fresh与固定anchor、mixture/sample-count条件递推；不以缺新rate公式制造gap。拟中心rate/无分布假设保证争议暂缓，局部框架与MNIST只报告，不写Books。重开只需iid→累计dependent population的必要桥接或修正假设，不请求全部later论文/附件。

## [Interactive In-Context Learning exact-v1](https://arxiv.org/html/2602.16066v1)

§2（132–150）teacher读取GT/unit tests等特权信息，student仅公开对话；verifier失败后反馈再尝试，外环RL更新权重，内环适配只是context而非每题梯度。两者可同模型，关键是information asymmetry，不要求teacher参数更大。§3.1（160–166）四模型/四任务的leak check为string match+LLM judge，约.3% flagged不是严格零泄漏。§3.2（167–181）Gemma3 12B/math训练与500问题heldout，单轮SFT/RL对照单轮表现接近而多轮反馈收益不同；未披露足够训练hyperparameters/完整teacher预算，不能授等compute收益。

新增训练角色在§4（312–323）：让student预测teacher反馈，部署只看自己先前尝试自评再修，不读取GT；不是可信World Model环境动力学。实际读Figure7原SVG（`V3_16066_social_main.svg`、`V3_16066_omni_si.svg`，已render查看）：OMNI Math十轮cumulative accuracy，self-improvement、baseline及didactic水平参照；没有单独控制teacher-feedback prediction这一因素的因果消融，不能把‘key’宣传升级唯一机制证据。§6（334–337）协作固定任务、mixed-motive与sycophancy未解决，短期context适应尚未巩固为永久知识。

actual [Ch33](../../../../../books/part-04-training-system/33-grpo.md):467–469 error-branch已有privileged诊断反馈→新group/verifier与预算；[Ch29](../../../../../books/part-04-training-system/29-sft.md):311–318 self-distill target变化已有，但没有明确把外部反馈turn变成可部署自评target与oracle移除两权限。拟 `TRAIN-SFT` 一窄段把消费反馈与学习生成反馈分开，不采唯一因果/可靠selfjudge/永久知识，PRE待root；若独校认为该局部接口已充分覆盖可仅报告，不靠缺recipe硬写。Ch28/30邻接已读。

## [Social Meta-Learning exact-v1](https://arxiv.org/html/2602.16488v1)

§4.1–4.3（117–141）static goal POMDP，student只公开history、teacher私有GT/测试；成功dialogue的student-turn SFT与online GRPO不同。关键新条件在§4.4（143–147）：SML alone不激励提问，Q-priming以.75^t概率把错误student turn替换为合成问题，生成问题时可用teacher私有GT。不能把训练造题权限当部署问句知道答案。

§5（163–191）math2k/code2k、math heldout500、静态math↔code迁移和Lost-in-Conversation逐步提供shards；GRPO g8、β0、γ.7、训练4轮/评价10轮，三seed/95%CI。单轮g32对照只匹配4×generation steps，不等teacher调用/总tokens/算力。§6.1（195–205）多轮收益不能由单轮预算baseline解释，但不唯一归因Q-priming；§6.4（242–246）Q-priming/SFT→RL有限协议中减少premature guessing、问题约5倍，不是问句校准效用或人类研究。§7（251–252）verifiable数学/代码、稀疏reward/固定目标，不外推动态意图或所有开放任务。

actual `TRAIN-SFT` Ch29:608–619 Demonstration Schedule已有信息等价full/stepped view→defer/clarify，但新差额是incorrect-turn replacement与外部私有GT造question监督；不是通用‘反馈有用’。拟一段接该schedule论证，保训练/部署权限、预算不等与静态任务范围，PRE待root，未写。与16066同部分作者/反馈主题不自动去重，两篇新增训练角色不同。

## [HiPER exact-v1](https://arxiv.org/html/2602.16165v1)

§4.1（140–154）一AR LLM依序SWITCH/KEEP、subgoal、action，KEEP复制旧subgoal，不是独立高低两模型。§4.3（174–227）segment内low GAE，末residual bootstrap到下一boundary的high value；high按duration γ^Δ与macro return估计，switch用(q-β)(Vhigh−Vlow)，一critic backbone两heads。新接口是segment boundary的credit权属，不是仅Plan-Execute prompt。

§4.4（229–242）无偏仅λlow=λhigh=1且critic exact；AppA.3（774–809）比较同Plan-Execute/on-policy的low-level advantage方差，不自动证明score加权的完整policy-gradient方差、λ=.95实训或所有LLM无偏。§5.4（403–405/465–487）同Plan-Execute prompt control GiGPO91.1±3.6、HiPER95.3±1.4，三seed；无RL该prompt8.3→2.9反退。§5.3（392–400）2.8×指到80%成功率的optimizer steps/sample-efficiency，不是wallclock。AppC（887–903）ALFWorld50步/2048prompt/512response、WebShop15步/4096prompt/512response，roll128，trainT1/evalT.4、KL.01、λ.95；两head多.8%memory参照PPO而非critic-free。AppD1（958–963）critic额外显存；AppD2（1006–1023）KEEP penalty从0→.3使76.6→95.3，正则是实质共同因子，不能全归HAE。

actual `TRAIN-PPO` [Ch32](../../../../../books/part-04-training-system/32-ppo.md):75–101普通TD/GAE与token information-time，还有value/credit误差分账，但没有subgoal持续时间与boundary换value head的具体合同。拟一段接GAE基础，保critic训练、switch penalty、有限方差对象和旧flat适用范围；PRE待root，不授标题‘provable gradient variance’。Ch31/33开篇已实际读。

## [DOIT exact-v1](https://arxiv.org/html/2602.16198v1)

§3.2（166–188）target以terminal reward event重加权，h为达高reward终态概率；任意target解释要求q/p有界与support/absolute continuity，不生成base没有的模式。§4（202–247）用terminal weight×Gaussian transition score的MC梯度估计，分母hhat有η floor；reward可不可微，不等score network无需导数。每步M full backward rollouts成本高。

§5（248–281）理论A5.1要求event概率≥ρ和score gradient有界，A5.3统一离散误差；TV bound依base error/ρ、MC M^-1/6与积分误差，低σ敏感，不授有限MC exact或rare-event保证。实际§6.1（283–325）Algorithm2只one-step lookahead，用当前位置score替代lookahead score的Tweedie terminal surrogate，不是fullrollout原理论原样实现；γ/time cutoff也改guidance。§6.2（327–362）实际采用exp(reward/τ)，SD1.5/K32/aesthetic，Table1 surrogate均值6.726±.072 vs full6.714±.055；**runtime排除reward evaluation**，1.712s vs39.584s不能充全pipeline加速。代理reward均值相近也不证明分布TV界。§7（512–516）rare highreward低h直接加大variance/cost。C4（1944–1955、2041–2046）D4RL用作者称ground-truth Q oracle，DDIM15且要求随机transition；M32/候选K/搜索配置不同，不采通用model-free或等compute支配。

actual `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24:258已具体拥有learned terminal-weight h回归、值/导数/正分母与no reward gradient的训练成本。DOIT真正差额是**不训练h estimator而从transition-score MC估计**，再用full→surrogate替代换取score-NFE与reward-query成本/理论权限分离；不是泛Doob或nondifferentiable reward新命名。拟最多一段邻接h接口，保rare-event floor、support、MC/score导数、reward调用与surrogate非exact、base fallback，不搬完整TV公式。PRE待root；若局部机制不足以改变既有设计选项，具体仅报告，不因缺配方强造gap。Ch23/25邻接已读。

## 当前处置与有限复核队列

16065中心争议隔离拟暂缓；其他四项仅提出上述最小owner差额，尚无共享写授权或非作者必要验收。五项正文支持/关键反侧已足够当前采用命题，下一步是root有限PRE，不继续遍历余证明或附录。ordinary未决的其他题摘/证据另按本日真实进度继续，不把这份包或下载数当日级完成。
