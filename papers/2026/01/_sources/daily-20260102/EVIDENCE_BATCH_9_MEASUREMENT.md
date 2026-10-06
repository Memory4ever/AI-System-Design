# Jan02 multi-turn preference / capability / risks / tool evaluation / steering

终处置增量：本批五项已通过。Capability Ch66 2301/2303与MultiRisk2305/2307（V/loss界修正后），各末注已root实际正文/前后写后核通过，Ch66锁释放。MCP/CREST具体ExistingCoverage也已通过。MUSIC Ch31 146/148及末注1192已root实际必要源与正文/邻接POST通过，5分具体trajectory-pair知识缺口深入；Ch31锁释放。旧待核过程不覆盖这五项通过，不代表日级Gate。

最新：五份完整AB与评分5/7/7/5/5已root实际校准，作者五项必要core全部完成。Capability新multi-step/ICL证据事件及MultiRisk限定必要源/具体owner已root写前核通过，Ch66 2301/2303、2305/2307与末注5258/5260已窄写，实际POST待root。MCP和CREST必要原源及具体ExistingCoverage已root非作者复核通过，不声称完整附件/精确recipe已被正文复述。MUSIC具体Books尚待，不以‘局部’代替判断。日级未验收。

CREST终处置覆盖下方旧拟报告：具体ExistingCoverage已root实际核通过，Ch15 282/284的whitebox head sensor→局部projection proposal/独立end verifier及校准成本、强干预损伤/fallback，Ch66 3780/3989–3991的decodable≠steering正确因果与collateral边界。这里承载的是干预权限与评价对象，非本论文keyword/PCA exact recipe；局部新recipe留报告，不追加重复正文。MCP下方具体coverage也已root实际核必要原源和owner通过。

完整exact-v1题摘：ABSTRACTS_2.json 35–50（24693/24661）、123–130（24587）；ABSTRACTS_3.json 3–18（24574/24565）。准入/暂定评分已送root，非作者本批尚未授完成。各DataCite原字段已保存：created依次03:17:56Z/03:17:11Z/03:15:25Z/03:14:54Z/03:15:07Z，取下一秒upper与holiday/noadvance-ID Jan1T01Z结合落Jan02；prior作者正文信号单核，不当全家族首次。未比较后续v2/v5，无具体revision事件信号不因版本号扩范围。

## [MUSIC: MUlti-Step Instruction Contrast for Multi-Turn Reward Models — 2512.24693v1](https://arxiv.org/html/2512.24693v1)

拟2+1+2=5：final-turn对比不充分→多个turn质量对比的合成样本→核RM选择是否对多轮条件更敏感。必要§3.1–3.4/Alg1、§4.1–4.3/Tab1、§6已实际读：chosen/rejected各自按自己历史生成user utterance，rejected assistant额外contrast；terminalhidden线性标量BT不是step信用归因或工具执行监督。Gemini1.5Pro同为simulator/judge，Gemma2-9B、原73k+31k、2048/2500step/b64/LR2e-6；generation5turn，eval3turn×BoN2/4/8及1000初prompt，order swap只是缓解positionbias。追加数据/两branch用户分叉/共同teacher与judge未完全分离，RewardBenchchat切片微退、无human独立验证/长轨迹证明。hardware/precision/seed及端到端时间未披露，不复现；不授‘robust多轮’或processcredit。具体Books待对读，不凭局部自动onlyreport。

## [Do Large Language Models Know What They Are Capable Of? — 2512.24661v1](https://arxiv.org/html/2512.24661v1)

原作者[2025-07-13 companion post](https://www.alignmentforum.org/posts/9tHEibBBhQCHEyFsa/do-llms-know-what-they-re-capable-of-why-this-matters-for-ai)已实际日期/AB/Introduction/资源模型核读：single-step BCB和capability/calibration无趋势已公开，明说未来多step及in-context。因此本窗拟重要新证据而非首次，7分对象只取后两实验，待root事件核。

必要v1 §3–6、AppendixA/C.1/D.1/F已实际读：1140BCB单步关闭hiddenCoT；512×9contract设置奖罚±1，以旧model全成功271/全失败193集合挑每序列50%能力人口，GPT5.1/Sonnet4.5后来换部分题，非自然任务base-rate或完全统一跨model样本。成功/失败历史可改善profit且AUROC未同样升，区别概率校准、排序、riskaversion；A财富条件threshold fit同selfreport决策后推出utility，是相容性证据非模型内部rational过程。SWE499task/70toolcall，提前submit末confidence forward-filled到70，lateAUROC非只有仍活跃人口；不把时间改善/退化授内部因果或普遍规模律。commercialAPI、MacM1Pro32GB/EC2t3.2xlarge是client运行环境，不是模型GPU/HW成本；GPU/precision/maxoutput/totaltoken预算未披露，未复现实验。高风险决策与delegation threshold仍需匹配当前任务/人口校准；现owner具体覆盖待核。

## [MultiRisk: Multiple Risk Control via Iterative Score Thresholding — 2512.24587v1](https://arxiv.org/html/2512.24587v1)

更新反证：root独立定点Condition5.7与D.5，作者实际重开同段已核：Condition给Vj∈[Vmin,Vmax]，Eq1乘指示器使未触发Lj=0；D.5 L841–843直接用Lj≥Vmin及δ=(Vmax−Vmin)/(n+1)不能在positive Vmin下直接继承。只隔离该uniform perturbation步骤/具体递归保证，不授全部理论被反证，也不自动用Vmin=0修好后续全部证明。重开需要作者修订或有效零loss下界/补偿与完整递归证明；当前Books只采用first-trigger人口与成本/保证权限分账，不采具体算法安全保证。下方原‘D5有真实上界的均匀扰动’须与本限定共同解释，不能单独作正面保证。

拟2+2+3=7。作者必要§2/Eq1、§4/Alg1–2、§5.1/Lemma5.8–5.9/Theorem5.10、§6、AppendixB/C/D.2–D.6均实际读。不是RL training或直接有害输出概率控制：Lj=Vj×I(前面均pass、首次在j触发)，Vj是该行为的provider成本，各行为互斥。prioritized gate改变后续进入人口；升前阈值增加后续Lj，升本阈值减Lj，不能逐滤器各自独立calibration替代。

base只是empirical DP；Multi用(n+1)分母、Vmax补偿和δ=(Vmax−Vmin)/(n+1)的辅助预算递归。D.3用n+1对称阈值+exchangeability把test loss换全样本均值；D.5有真实a.s.上界的均匀扰动；D.6借对称/可观测threshold夹逼与单调性证明每j的marginal期望约束，不是给定这份calibration的high-probability发布证明，更不是逐请求安全。需要exchangeable观测、有限score、pointwise可行阈值与真实known bounded costs；tightness另需continuity/positivecost/nondegenerate预算，near-optimal另需iid/Lipschitz/reverseHolder等，只记录条件不授普适最优。C的小n/rare hugecost反例说明样本未覆盖尾部时base会任意超预算，不把“n大”当充分保证。

§6是Alpaca7Bgreedy/512token、PKUSafeRLHF30k取cal500/test500、Guard3-8B category scores/perplexity、beaver helpfulness；所有触发固定abstain，成本是abstain的负helpfulness移位，不是残留unsafe行为率。用cal empirical minimum与maximum替代population essential bounds无法继承理论；10randomsplit SE不是训练seedCI。AppB LTT是CLT/Bonferroni high-probability口径再用heuristic预算换marginal，不能据曲线授同保证优势；其σ文字称std但公式是variance、零variance分支末尾重复>符号也有口径问题，不替作者补造实现。hardware/precision/总latency未披露，不复现。作者HTML date August24,2026与arxivv1字段保留身份限制，不假定原因；拟窄整合为优先级gate的scored population/成本口径与保证强度，不采LLM安全曲线保证，具体owner/root待核。

## [MCPAgentBench — 2512.24565v1](https://arxiv.org/html/2512.24565v1)

拟1+2+2=5。作者必要§3–5实际读：从841task/20ktools手工筛180task、按task/tooltags和描述修为unique gold；Autogen stubs由GPT4o mock而非真实副作用。TFS是tool-name/parameter set（忽略order），TEFS要gold serial/parallel顺序，仅非unique时有parameter判别；替代合法plan未测。20candidate tools/mainavg@4、10model措辞与表11行保冲突；distractor数量10/20/30不同不是语义matched困难度。provider/toolinterface/harness未matched消融，不能将parallel工具分数归因纯model planning或生产吞吐。

time efficiency按TEFS/minute，token efficiency式直接除OutputTokens却称per1k，reasoning-token计入范围未明确；平均四次不是seedCI。所有mock无环境身份/auth/realstate；score只支持defined call-format gold判据，不证明effect/timeout/recovery。拟具体ExistingCoverage：Ch66过程指令段现367–380实际要求typed trace/effect receipt、legal transition/scorer acceptance sets与false reject分开；现1252附近mock contract正文明确替换范围、integration/state-transition/failure tests。已实际对读相应正文，不声称书已含TEFS公式；不再追加该任务gold recipe，待root核具体NoChange。

## [Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time — 2512.24574v1](https://arxiv.org/html/2512.24574v1)

拟2+1+2=5。作者必要§3/4、§5.1–5.3、AppendixB/C.2实际读。双换行segment+keyword标签是lexical proxy，不是必要verification/真实认知类别；attention-head endpoint linear MSE probe随机采1000/class、8:1:1 step-features与highestvalcheckpoint，不是明确按问题heldout。random-token probe chance只排一种负对照，不能排lexical cues/同题step leakage。head mean→layer shared PCA→方向投影，PCA variance不证明“真实认知/noisefree”。Eq5 x−(xTv)v保orthogonal需unitv，公开本段未说明norm/near-collinear denominator fallback，不宣称实际bug/verified实现。

初识别7%/方法top10%/最终AIME22–24调38%是不同阶段口径，fixed-permodel不是完全untuned。Calib500MATH500，任务包含MATH500同名测试须绑定训练/评价重叠限制；temp.6/topp.95/max32768，R1-Qwen1.5/7/32、Qwen3/OSS。Tables1/2同1.5B AIME25 baseline20 vs17/CREST30 vs20.3的结果口径不同，不照录普遍收益。Table3 Qwen30B code略增tokens；尾部仍32k repetitivefailure，§5.3.2图说top80%而正文top8%不混成统一tail统计。GPU/precision/多seed/端到端runtime/离线校准成本未披露，不授negligible-overhead、norm-preserve稳定性或普遍可删非线性思考。拟标准仅报告需具体长期门槛/owner对照，待root；非center因果bug证明，不降低分数避争议。
