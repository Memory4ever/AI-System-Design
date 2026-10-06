# EGCA16158：执行参照与局部信用的必要边界

root只own03-19现存有限准入，不扩发现；2+1+2=5，具体执行参照→token信用差额必要深入。采用[精确v1 HTML](https://arxiv.org/html/2603.16158v1)§3.1–3.7/Eq1–10、§4.1–4.5/Tables1–4、§5、A.1–A.6及A.8参数；必要G例只作定点接口说明，不核所有图像/代码或复现。完整题摘/本日公开上下界复用实际日级材料；当前abs轻量说明另核，不把Submitted当公开。

## 实际机制与直接反侧

原unit-test reward乘teacher从(x,canonical reference)抽出的约束门；sampling也加约束suffix，候选/参照AST与normalized CFG相似度过阈值才视comparable。先syntax/runtime diagnostics，后constraint/comparability，后correct/logic；logic只对第一个失败测试输入执行同instrumentation，比较对齐后的state snapshot，debugger LLM提议earliest divergence和token span。Correct/constraint仍Ai/T均匀，syntax/logic只非空span Ai/|span|，其余0，sum token credit=Ai不是无偏policygradient/已识唯一因果。空span、循环控制/多算法状态对齐的完整失败退路未公开，本轮不补造。

Reference不作imitation target，却真实影响抽取约束、sample support、reward gate、trace/credit；‘不用teacher gradient’不能被改成没有teacher知识注入。Eq10 logpi条件省略了采样Eq4的C，完整ratio/KL/clipping在Appendix B才提，不采可直接运行的全recipe或无偏保证。静态同CFG不证明变量/边界状态可语义对齐，首divergence可能是表征差异/后果而非唯一root cause；§5承认正确但不同算法也可能被拒。

DeepSeek-Coder-Instruct6.7B/APPS+，Qwen2.5-Coder7B默认debugger，G16/T.8/p.9/max8192，AdamW5e-7/KL.05/clip.2，8A10080GB/globalbatch64/3epochs/.3epochwarmup/lineardecay；evalT.2/p.95/HumanEval与MBPP pass1。原8A100容量不认证有效数值精度；prompt长度、exactcommit、训练seed/CI、trace阈值/对齐算法与所有teacher/cache费用ND。原预算相同不等全部费用相同：Table5 APPS+约35%logic、+18%wallclock只是该workload比GRPO，非任意Serving并发/SLO。明示baseline未加约束guidance/structure gate，主结果同时变support/reward/credit，不能全归单一定位。

T1 82.1/68.9 vsGRPO79/67.4；T3更强Sonnet83.7但MBPP67.8<默认68.9，1.5B78.9/66.1低于GRPO79/67.4。学生比小debugger独立生成更强不排teacher信息影响（不同policy容量/基线）；teacher-SFT与critiqueRL不足以排除constraint/support贡献。T6 earliest/last/random/uniform是受限定位对照，random MBPP67.1<uniform67.4；没有全threshold/teacher效用识别、confidence/因果定理。仅采用执行参照/诊断信号分责的可训练分支，保留质量/费用/误定位风险。

## actual owner

sole `TRAIN-GRPO`，actualCh33 242–300完整sequence reward→token credit、原259检索signed residual、267树内proxy、285证据span、287局部verifier重采、289–292 recoverability；Ch32/34前置已读。它们未承载“可比较执行参照的first-failing-input trace差异只提议信用span，不能将静态同构/首差当根因”的具体接口。拟sequence-credit简单/粗糙说明后、think/answer分区前一段；不在Evaluation/Agent复制第二owner。不授写锁，等待非preparer Source/actualowner/PRE。

## 逐字 PRE

resume_review17_18 非准备者必要Source/实际owner/PRE通过后，root实际写入Ch33 sequence advantage广播说明后单段及本人章末注，回读240–256完整局部与自身静态注、scoped diff-check通过。非writer resume_review17_18实际复核232–262（新增245）、末注3178–3190（本人3190）并回对有效PRE/Source，确认一段一注与邻接完整，actualPOST通过；root接纳并释放窄锁。只计本家族受限整合安全，不授日级验收。

有可执行参照时，可以先问“这条失败程序在哪里偏离参照”，再决定把原 outcome advantage 分给哪些 tokens，而不是把整段错误均匀罚一遍。一条[受限执行信用分支](https://arxiv.org/html/2603.16158v1)先区分编译/运行失败、约束不符和可比较的逻辑失败；后者在同一失败测试输入、同一 instrumentation 下比较候选与参照 trace，由 localizer 提议首个差异的 span，将局部权重归一以保留原 signed advantage 的总量。Reference 不作模仿目标，也仍参与约束、采样和信用，不能称没有教师信息；AST/CFG 相似不证明状态语义对齐，首个差异也不认证唯一根因或无偏更新。合法的不同算法可能被门控排除，错定位又会集中惩罚有用 tokens；较弱 localizer 和部分任务仍反退，执行、参考制备、teacher 调用与训练费用都要计入。对齐无效、没有可信参照或净质量/费用回归时，退回原 sequence advantage、可靠编译诊断或独立过程 verifier，保留多个有效解，不由测试失败替局部因果性背书。<!-- source-family:SF-2026-ARXIV-2603-16158 -->

静态注：`SF-2026-ARXIV-2603-16158` — [EGCA exact-v1](https://arxiv.org/html/2603.16158v1)§3–5/Eq1–10/Tables1–4及A.1–A.6/A.8必要范围。仅执行参照/局部信用消费者分支；采样/reward/credit共同改变、localizer非因果oracle、错对齐与多算法拒绝、任务反退和全费用近文，不采无教师信息、完整无偏recipe或生产保证；未核代码、所有图像或复现。
