# 2603.08999 — completed-trace采样门控必要原证与Ch20两段（Source/PRE/actualPOST通过）

[exact-v1](https://arxiv.org/html/2603.08999v1)标题Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning。第四包完整AB已root独核，作者本轮实际§3–8完整/Eq1–6/Tables1–4必要文字，不读无关relatedwork或全部Appendix，不采用Fig2/3及其他模型曲线精确数。currentv4标题Selective Sampling，AB明确calibration-only transfer、有限均值/不确定性；无已见撤回/纠错comment，版本号/改名不单独重要修订，后版数字不回填v1。

raw SUP_EXACT_BATCH4与freshabs/DOI回读一致：Mar09UTC22:34:06晚于deadline，official noadvance最早Mar11BJT08下界，arxiv.content拥有findable registeredMar11UTC02:03:03已经可发现上界，同BJT03-11夹证，非Submitted/registration单独公开。currentcomment没有accepted先稿信号，无需追全会议/仓库史；日期待root核。

2+1+2=5；采样前activation难度门不等完成轨迹后可采的proxy→completed greedy CoT数值/词汇sequence训练correctness classifier，再决定是否追加multipath→已付首轨迹、判别及目标域校准须同算，不能充在线earlyexit。具体MODEL-SAMPLING gap拟定点深入，成熟GRU/MHSA/SC不独立加分。

## 必要方法、评价与反侧

§3.1 Eq2–4对每sentenceprefix串接各选项，累乘/求和整option token条件概率，再在选项间归一；长度、选项集合与白盒概率接口是条件，不是自然正确率。§3.2完整greedy CoT及answer先全部产生，再32维numeric/linguistic sequence给classifier：featuregating为masked全轨迹mean/MLP、GRU64、4headnoncausalMHSA、末sentence概率；正文列模块次序与表示符号有不一致，不补造已核可执行图。最终p≥tau接受原答案，低分转更贵增强；§8明确不能在线earlyexit，abstract/introduction的ongoing stop文字不采。全轨迹z-score/normalizedposition/fullmean与noncausalattention都不支持因果prefix控制。

§4/6五openLLM/四MCQA（含MathQA/MMLU，不只医疗场景），训练单H10080GB、8500/500/1000train/val/test、10paths/T1；主要GPTOSS20B，其余附录不作为本轮数字证据。§5.3每LLM分别训练MedQAclassifier，跨dataset不重训但§5.1每目标datasetval扫tau，在最高观测valaccuracy的relative .5%退幅内最大tokenreduction；MedQA.65/MathQA.20/MedMCQA.60/MMLU.80不能移用新模型/题型。既非模型无关classifier，也非无监督/无标注zero-shot threshold，目标域答案和校准预算真实存在。

§5.2 pairedbootstrap2000exampleID与图caption的across-run盒图不提供完整run数/seeds/非劣marginCI；n.s.不是等价，relative .5%选点不是分布保证。文本69–79%对SC/CER、27–48%对DV限该生成token协议；不采精确未独核曲线，也不由“最多80%”签墙钟/服务成本。§5.4 Table3MedMCQA单FA/MHSA从.704→.701、MMLUMHSA.900→.898，即小门控模块不保证逐slice提高。Table3fullmean794/Table4full805且MedQA1026/1070等不同，未说明统一同run，不拼一个执行配置。数字+linguistic文本统计含题目/选项overlap，不等额外独立语义校验；高confidence可同样错误。

完整greedy、sentence分割/逐option条件评分、特征抽取、detector训练/前向、val标注/阈值搜索和被触发10path/投票都计费；sentenceprefix/option评分是否另FW/cache复用、推理hardware/precision、prompt、seed/重复次数、完整latency/token分账与SLO Not Disclosed。训练H100不等全部inferencehardware。预算总收益不由仅outputtokens取得，白盒不可得/开放生成/分布或判别信号漂移不采用未经校准gate，保留原greedy/固定SC/verifier。

## 实际owner与逐字PRE

唯一ownerMODEL-SAMPLING，Ch20。作者实际opening、329–361完整Parallel Sampling局部及Ch19/21开篇；353ACT-SC是从同prompt内部activation在大量probe前预测difficulty、351固定N后加裁决、355CoCoA是已生成候选selector，均非“付完整首条greedy→句序列correctnessgate→决定是否追加多路”的接口。拟ACT-SC完整段后/CoCoA前两段，旧策略共存，不写已在生成中停止。

追加多少候选还可以等首条轨迹完成后再决定。先付一次完整 greedy 推理与答案，再从各句的选项条件概率、熵、变化量和词汇统计形成序列，由单独训练的判别器估计这条答案的可靠性；分数越过阈值时保留原答案，否则才追加多路径生成与聚合。[completed-trace 的受限机制](https://arxiv.org/html/2603.08999v1#S3)以每个基座模型自己的判别器支持这一分支。它改变的是后续采样预算，不缩短已经完成的首条轨迹，也不使概率趋势或文字风格成为正确性真值；全轨迹统计与非因果 attention 不能直接充当生成中的提前停止器。
<!-- source-family:SF-2026-ARXIV-2603-08999 -->

不重训判别器也不等于无需目标域校准：[有限迁移对照](https://arxiv.org/html/2603.08999v1#S5)仍用新数据集验证答案选择阈值，较少生成 token 与未显著的准确率差异不证明所有任务非劣或完整推理更快。首条 greedy、每句选项评分、特征抽取与判别、训练/标注/阈值搜索，以及被触发的全部候选和聚合都要计入预算。模型、选项形式、题型或概率接口改变后须重新验收；白盒信号不可得、校准不足或误接受代价过高时，保留原单路、固定 self-consistency 预算和独立 verifier，不由高 confidence 自签答案正确。
<!-- source-family:SF-2026-ARXIV-2603-08999 -->

原拟本人注保留为PRE文字：SF-2026-ARXIV-2603-08999，Daily2026-03-12，v1§3–8/Eq1–6/Tables1–4，2+1+2=5 gap深入；completedgreedy/noncausalfeatures gate只管追加采样，targetval校准/模型特定判别器、有限n.s.非等价及全部费用近文。不采在线earlyexit、currentv4数字、未核图/其他模型附录、实现/复现/完整SLO；root必要Source/date/逐字PRE与actualPOST待核。

实际结果：root必要exact-v1完整§3/5/8及Tables1–4、日期夹证与Ch20具体owner逐字PRE通过，不反称其独读全部§4/6设置。作者按窄锁写新354/357两段与本人685注并实际顺读347–371；root非writer实际顺读347–375完整ACT-SC→两新段→CoCoA/后续selection邻接及本注，回对必要原证，actualPOST通过，Ch20锁释放。完整已付首轨迹、非因果不能在线earlyexit、每targetval校准、n.s.非等价和全部费用/旧策略共存均通过；不授本日DAY。
