# Live 2026-10-09：additional 四项非作者必要复核

复核者 supplement_20260311，作者 supplement_20260312。仅本窗 BJT 2026-10-08 已校准准入的 ready 项，不扩发现；日期与准入复用独立有效结果，Source/PRE、实际 POST 和 DAY 分开。本文件不修改作者原证笔记，未完成项仍是普通可执行工作。

## 2610.09876 PaTh — 必要 Source / actual owner / PRE 通过；实际 POST 由 root 完成

实际读取 [exact-v1 HTML](https://arxiv.org/html/2610.09876v1) §3 全部/Eq1、§4.1 Tables1–3及必要文字、§4.2–4.3/§5（127–261）；C方法和 Tables5–6（364–427）；H/Table13（480–490）；K/Table20（561–580）；L/Tables21–22（581–602）；N文字与图注（609–619）。前轮读至199，本轮补全200–261与这些定点附录。未读全部理论证明、其他附录、图像像素、代码或复现，不授普遍生成能力。

独立核对同意作者的窄命题：递归状态 (y,z) 与 noisy sample 分责，仅空间 y 解码后经 ControlNet 进入先训练、后冻结的 Painter；z 本身非图像/真解。基础每步 reset 与 efficient 跨步保留/早期递归/后段复用是不同方案，不照录 sampler “commit”为外部提交。K 标签确是同轨迹终图 classifier 读数而非真实解；局部 probe 波动不证明唯一内部搜索因果。

直接反侧已实际核：Maze Bagel FT pass/coverage高于PaTh，不能以exact优越合并所有指标；CLEVR属性53.8低于DM54.6/56.1/56.3、Recall略退；注入错来自valid solution重加噪，晚段难修且Sudoku70%处DM反超；L无空间对应为0 puzzle/11.1 cell、token81→144无效，对齐也仅部分恢复；无锚关系tokens51.2/7.8，centroid加入后不同；N有限配置不授统一预算最优；H 85h/113h仅该Sudoku配置且两阶段全部费用均算。

Actual owner `MULTIMODAL-GENERATIVE-PARADIGMS`：Ch24 828–875完整 workflow→provisional/committed→持久条件副本→UI/运行交接、145–162 diffusion条件与状态接口；Ch23/25开篇实际读。现“持久条件副本”完整段只有持续覆盖 denoiser 输入，不承载未解码探索状态经空间readout给冻结sampler的独立分支；作者单段放该完整段后/UI段前自然，不覆盖旧定义。

作者 additional-core-review.md 本篇逐字PRE通过，评分2+1+2=5保持；因已确认状态接口差额深入受影响范围，不改分。PRE保留空间对应失败、晚段与质量退步、全部递归/训练/驻留费用、probe非真解及普通生成/独立输出检查退路。后续root非writer实际POST通过并释放锁，本项实际整合完成；本复核者复用有效POST，不重复声称自行读过写后正文，不授DAY。

## 2610.09679 CERO — 必要 Source / actual owner / PRE 通过；实际 POST 由 root 完成

实际 [exact-v1 HTML](https://arxiv.org/html/2610.09679v1) §2–7（110–346）、Eq1–12与Alg1/Tables1–2；B.2全部423–443与B.4全部451–461定点核。初次find大输出截断后单独439窗口补全B.2末/B.4，不将截断当已读；无D/E/F全证明、图像像素、全G实现或复现。

独立同意固定group下有限horizon admission/pacing提案：跨轮携带Beta状态、支持斜率/共享price/remaining预算，正margin排序得virtual allocation后用remaining裁执行，Eq10双变量确消费virtual而非实际预算裁掉的量；执行后真实success/fail更新Beta并让当前policy消费完整组，零allocation不更新policy。条件iid Bernoulli的expected reward variance仅对比度proxy，forgetting不授漂移calibration；凹utility/pathwise固定率与same-path保证不授不同allocation改变policy路径后的能力最优。此处不采用regret数字或完整证明正确声明。

实际关键反侧同意作者：avg@16为逐回答binary mean非pass；三backbone固定256kresponses不等tokens/updates/FLOPs，T2三seed仅1.5B；T1部分MINERVA/Olympiad/AIME反退。Random-matched保pacing/groups只支持该prompt-assignment对照，不能替pacing独有因果。B.2仅32k selectedgroups、.154预测>.119观察，nominalCI未调重复prompt/时间依赖，不推未选人口或learninggain；B.4 E2E含init/validation/checkpoint且core含rollout/reward/logprob/optimizer/selection，CERO488/486/487updates vsGRPO500，单run成本不授普遍效率，4B Knapsack35.85GPUh低于CERO36.31。

Actual owner `TRAIN-GRPO`：Ch33 499–548完整generalistprior→prompt-replay→errorbranch与432–491采样/straggler/cancel/groupgradient上下文、Ch32/34开篇实际读。旧replay已有近期promptsignal/当前重新rollout与uniformfallback，但没有固定G的全horizon remainingbudget和virtual/executed反馈分账；完整21177 marker之后/errorbranch之前单段自然，不覆盖组advantage或旧均匀支出。作者additional-core-review本篇逐字PRE通过，2+2+2=6保持、具体gap受影响深入；不授虚拟配额为真实feedback或整体训练最优，不加伪实现。后续root非writer实际POST通过并释放锁，本项实际整合完成；本复核者复用有效POST，不重复声称自行读过写后正文，不授DAY。

PaTh/CERO后续实际POST同步：root已作为非writer完成两篇新增正文/完整局部邻接/本人注实际核验并释放锁；作者additional-core-review.md已记录真实位置与正式Report同步。本复核者没有重复POST，当前实际整合以root有效POST为准，不授DAY。

## 2610.09493 — 必要 Source / actual owner / PRE 通过；root实际 POST通过

actual [exact-v1 HTML](https://arxiv.org/html/2610.09493v1) §2完整69–104/Eq1–11、§3–4全部105–212方法/人口/T1–6、§6 220–223、A1 268–270、D2完整403–453/T15–18。正文输出首次截断缺69–82后另小段补全；click附录只回顶部未作有效D2已读，实际另open403窗口补足。未读完整其他附录、图像像素、code或复現，未核500-anchor具体transport算法；PRE只采跨模型另需对齐，§3.2与§4.3明确支持。

独立同意受限诊断/干预分责：同一最后shared prompt位置的paired差，中心化train-only PC1、原始差signed projection与L2幅度不同；exposure/context-vs-none与choice/conflict-vs-congruent是不同fitcontrast，不是一根通用来源轴。Control在训练fold定方向sign、median尺度、层块和dose，不读取heldout congruent state或gradient；正负dose改变同一conflict输入，margin变化不等greedy翻转。T1随机/radial/shuffled/equalnorm与D2训练平均candidategradient控制支持这项有限比较，不认证唯一natural mediator。

实际直接反侧与作者一致：Pythia3994 verifiedtargets/checkpoint97k、OLMo1000/100groups并50pairedgroup、AUC.508 [.482,.534]与80%power只至.570，不证曝光不存在；NQSwap120/113/112三个分母、ConflictQA777/617与eligible flips不同不能池化。早层无主控制gate通过，中晚有限对照通过；candidate-gradient能移动margin但T18 congruent91.63/91.57、no-context89.96/89.95低于pointgate，LTS97.8/96.5也不认证全能力或CI下界95。D2明确只排除平均梯度此条解释，不排除所有非线性/item特定控制。Longform197/200 valid、NLI/support非事实；两source本来答案一致时不能恢复原始依赖。多层activation、方向/尺度拟合、重前向、judge/生成、对齐与独立保留评价计费，不采生产provenance/circuit或发布安全。

Actual Ch66 266–297完整adapter/internal sensor→Gemma2两段→crossmodel差异→EvaluationIdentity，Ch65/67开篇已读。原Gemma2分重建/输出扰动/解释预测与任务干预，但未区分状态变化幅度的diagnosis与signed方向selectivecontrol及等范数答案梯度反侧。作者singlePRE在Gemma2第二完整段后/crossmodel之前自然，唯一PLATFORM-EVALUATION-SYSTEM，不再写Ch76第二机制。additional-core-review.md本篇逐字PRE PASS，2+1+2=5不改；具体差额深入，训练冻结接口/关键反侧/全费退路已足够，停止扩附件。root后续授权作者窄写并完成非writer实际POST通过，本项实际整合完成；本复核者复用root有效POST，不重复写后核验，不授DAY。

## 2610.10533 — 复核 ownership 移交

root将本项必要Source/PRE非作者核交review_mar11_continue，本复核者未读其原证、不计通过、不重复处理。
