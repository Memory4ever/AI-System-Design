# 第六包：exact-v1训练与执行边界

本包8项由root发现题摘潜力校准后，只读本轮original v1 HTML必要方法、对应控制与直接反侧。originalabs及same-ID registered结合official announcement下界的全窗范围见DATE_BATCH4；不把Submitted当公开，不将发现abstract当v1证据。各5–6分项因具体owner差额加深到拟采用范围，不读全部proof/artifact。root实际PRE与六处正文/完整邻接/自身note POST通过，两项具体Existing通过；六处自身note已同步并释放lease。Ch31首句仅按反馈改善承接，其余机制不变。全日累计34唯一家族安全处置=25整合+7已有覆盖+2争议隔离，仍有普通待办，非日级Gate。

## 22508 MBT，2+1+3=6，Ch29窄差额

原blocks31–61/63–70/72–89/100–110/114–115已实际读。actual题名Mirroring the Mind，与发现题名不同，身份修复见V3_IDENTITY_CORRECTIONS。五phase为understanding/filter/planning/execute-monitor/selfcorrect/verify；MBT-S让teacher看到gold来合成，MBT-R让teacher看到student trace+gold先独立解题再改写正确/错误trace，并非线上自主纠错。SFT后GRPO使用token F1 outcome，不是process reward。GPT-OSS120B同时teacher与judge，行为评分不认证faithfulness；“over/under”还各以不同correct/incorrect人口为分母。Qwen3 .6/1.7/4B、Hotpot train及MuSiQue/2Wiki OOD，rawteacher/rejection控制采用相同SFT+GRPO，但teacher preparation budget未匹配；部分rawteacher accuracy更高却verbose/degenerate，.6B MBT-S degen6%vsbase0，4B2Wiki EM仍低于GRPO，不授所有zero-degeneration或accuracy普胜。AES相对加权非wallclock/SLO，全部teacher生成/重写/judge/训练费用保留。

Actual Ch29 162–170与182–194承载真实learner失败恢复、错误前缀也是监督目标、推导模式≠答案正确；尚缺**gold-anchored分阶段重写与rawteacher/rejection控制分开验收正确中间被覆写/行为稳定**的局部机制。请求186附近单段＋ownnote，不把phase遵从、自我纠错文字与内部human cognition等同；保source privilege、条件人口、局部负侧与原verified trace回退。

## 22518 重实现评测，2+2+2=6，Ch66具体Existing提案

原24–55/86–95/103–126/173–180已实际读。21repos/8langs，CLI/REST而非GUI/lib，source implementation可见、emptytarget；hidden tests只在evaluation复制、删implementation-specific依赖，不等全部行为oracle。4 agents×21=84run，一次每任务，4hwalltimeout；build和test分别统计。LOC分层91.3/66.9/15.3是任务/语言/语义共变的相关性，不授LOC唯一原因。ClaudeCode/OpenCodeClaude同base比较定位整体harness而非单组件。5轮refinement在较早10repo切片、保同workspace且每轮freshsession；有taskwarrior改善亦有charcoal退步，不能把额外4倍时间授普遍修复。hidden-test完整性和可运行reference均是局部支持，未复现。

Actual Ch66 2910–2927的source repo/tests/blackbox identity、需求访问与执行失败分责、bug-discriminating reference replay，以及3591–3611累积repo health/独立execution effect已实际读。它们具体承载**实现替代验收不能由源码/当前testpass自行证明语义完整、harness状态/成本与失败人口须冻结**；本材料LOC相关与有限refinement反退只增经验，不改变该长期合同。请求Existing实际核，不为论文名制造重写gap；不说有完整实现无关semantic证明。

## 22525 edge failover，2+2+2=6，Ch72具体Existing提案

原34–49/64–90/109–110已实际读。三node MQTT/Tailscale/HomeAssistant（Macmini/NUC/phone）。unsigned envelope命令metadata可伪造/重放且broker允许直接topic；这是受测配置，不授所有MQTT或Agent框架缺陷。109KB overcontext触发Anthropic cloud fallback且无用户通知，tcpdump/DNS证明外部路径，不证明所有上下文字节/secret都已恢复。WiFi blackout→ADB35.7s与MQTT reconnect50trials9.3ms不同event；cloud10calls与edge280ops不同workload，不能等价比较整体时延。论文未实现HMAC/ACL防线，也不由本地模型推出zeroegress。

Actual Ch72 2328–2337明确执行路径可信才有local隐私边界、代码/依赖权限和egress先于data挂载；2507–2520明确signature与目标/scopedgrant、网络代理destinationallowlist仍不完整约束effect与response，fallback成本和拒绝分支已实际读。**local标签不授权外部路径、unsignedmetadata不授身份、network可达不授effect**已被真实正文承载，请求Existing。受控overcontext failure是本报告经验，不制造新的networkallowlist原则。

## 22538 RAIN-Merging，2+1+2=5，Ch30窄差额

原18–57/65–84（75–82补读）/177–185/222–227/233–238/272–273已实际读。共同基座LRM与instruction-model task vector，对各QKVO/FFN更新投影到calibration在`<think></think>`特殊token处的feature nullspace；不保护所有thought内容或开放输入。Stage2用attention alignment/leakage作gradient代理与正diagonal曲率启发式，不是真正loss-Hessian保证；FFN scale取head平均。150cal（math/code/science各50）/150validation/365IF、λgrid/ρ/headα以及FP64merge→BF16storage，新增capture/project/search/验证费用。有限线性layerΦΔ=0不授全网络非线性后行为精确保留。cal增加保reasoning却损IF，λ>1reasoning退，32B Aider低于LRM；formatmissing0仅所测格式非安全/semantic证书。

Actual Ch30 607–627为adapter组合后重新eval、activation-conditioned row merge、ACT-Mat层输出保持、Jacobian Gram regularizer与线性化条件。具体新差额是**special-token局部结构anchor投影＋模块缩放proxy**，请求输出保持段附近单段+ownnote，保有限cal/nullspace局部性、上游变化/非线性、代理不是真曲率与原独立adapter/静态merge回退。

## 22543 Ruyi2 Technical Report共享family，2+2+2=6，Ch28窄差额

原12–15/23–28/43–69（48–60补读）/70–93已实际读。Qwen3-14B40层形成共享prefix的3层/22层分支与原40层，联合branchCE与时变λ处理梯度冲突；static shared family不等learnedexit，runtime adaptive routing为未来。800BCPT/4MjointSFT，pretraining总数另有[NUM]placeholder不补造。DaE冻结旧backbone，仅新增3blocks+head，以Wo/Wdown=0提供identityinit，内部Gaussian对clone控制支持局部inertia，不认证训练后旧功能无损；600B增训含10%replay、4M SFT3epoch，新增train/分支/head/共享部署状态全部付费，3Dparallel倍率细节不充分不采。SVD-whitening借已知SVDLLM方法不是新准入主张。Table2 1.7B avg41.10<Qwen57.40，8B/14B亦单项退；不采总体能力压缩均更优。

Actual Ch28 173–194已有learnedexit/recurrentblock与成长复制untied-layer区别、trainFLOPs/部署深度/参数分账，缺**shared-prefix多个固定depth任务loss共训与zero-output新增layer identityinit**这一family合同。请求AdaptiveDepth邻接单段+ownnote，明确static family不是tokenstop policy、冻结weights不是冻结function、局部counter和全部CPT/branch成本，与原独立固定depth/已校准exit共存。

## 22546 Human-in-the-loop具身求助，2+2+2=6，Ch79窄差额

原34–58（49–58补）/60–69/80–85已实际读。when帮助是timeout/failure count nmax3的固定规则，不是learned trigger；只学howquery。HFM GRPO以MuSiQue train的search替作humanresponse训练，不是Minecraft交互RL；Guidance Planner把回复变systemprompt或预定义escape动作，不能授任意humaninfo可执行。15tasks/10experiencedhuman，log-only vsHFM7/32B的受控局部结果；threshold2部分hardtask反而失败、variance随阈值涨，帮助时间50–60splateau非免费。人类分配/重复与信息量预算未充分隔离，不从全部任务需要求助推定agent理论不可解；额外Q&A/教师GRPO/中断与executor验证成本保留。

Actual Ch79 314–328 PlanPool承载已识别ambiguity的asked/drop ledger与预算；58–74估计器/selector以及385PbD承载planner消费者。具体差额是**固定失败触发与学得求助表达、返回guidance如何改规划/动作分责**，请求PlanPool附近单段+ownnote，不把humananswer真值或escape动作当全安全；保threshold负侧、MuSiQue训练迁移边界与原log-only/固定人工milestone回退。

## 22554 跨语安全weight edit，2+1+2=5，Ch31窄差额

原32–48/51–92/95–123已实际必要读。sparse safetyneurons是assumption；activation divergence/Cohen选择只是probe，Englishset Jaccard不是因果universal安全basis。低资源activations向Englishanchor的线性拟合+γ||XsafeΔ||²软utility penalty+λregularizer，以Q-Cholesky白化top-r SVD再反白化解rank-constrained quadratic，只授线性subproblem，postσ target vs preactivation proxy未给σ'不授exact nonlinear。8langs×313translated prompts/HunyuanMT与Qwen3GuardGen8B共同限制真值；1–7B Llama/Qwen，多种criterion可有效不授唯一提取。Table1 Hebrew Llama1/3B unsafe+6/+7直接反侧；Qwen .5B MGSM7.75→5.27、其他utility也退，不授无损。utilityanchoralone ablation还恶化ASR、regularizer alone与combined权衡。capture/SVD/merge/校准有费，hwprecisionND。

Actual Ch31 493–535已有weight更新vsruntime actuator、feature可读≠可干预、ID控制≠OOD控制、共同feature组合非线性副作用。缺**跨语目标anchor权重低秩编辑的utility软penalty与有限线性闭式解**，请求持久weights到activationintervention交接附近单段+ownnote；不写“training-free=未改weights”或“nullspace=hardutility保证”，保译者/judge与语言反退、原safetytraining/小幅steer/独立安全Gate回退。

## 22556 DuoThink，2+1+2=5，Ch33窄差额

原31–63/66–77/82–89/97–98已实际读。HFT think/nonthink分别DeepSeekR1/V3，RLCPAS仅r∈{0,1}且正确短样本加δ，原正确longadv在binaryGRPO本已非负，不说其修复所有“正确长负A”。LAGR以L^-β归一权重乘token-SUM；β0是uniformcoef不是每sample总gradient均权，sharednormalizer改变update scale。控制token bonusλ10本地好但过大激进，β.4局部tune。24K/G8/B128micro64/16H100、MathVerify、HFT3epochs16K；allteacher/rollout/训练费用，tokens/NoThinkratio不等wallclock/SLO。GPQA局部收益伴更长output，非数学语言/generalpolicy未证。

Actual Ch33 256–279 outcome-qualified相对quality信号、压缩process权限、双pass/CRTreference guard；response/token normalization原169已读，缺**仅正确短rollout加bonus＋inverse-length权重作用于tokenSUM而非sampleMEAN**的目标分支。请求CRT附近单段+ownnote，保正确人口/normalizer、双teacher/controltoken迁移与局部length/accuracy折中，原outcome-only/无长度项回退；不授correctness逐题保持或整体免费。
