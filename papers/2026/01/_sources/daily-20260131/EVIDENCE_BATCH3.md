# 本日第三批必要证据（root 必要原源独立复核通过）

全部精确 v1；只核已校准的具体增量及必要配置/反侧，未复现，不把原文性能提升为部署保证。完整题摘与日期仍在本日既有记录。

root 已实际核全部五项上述必要原源：22136中心性能争议暂缓、另四项仅报告处置通过，不授日级 Gate。下面保留作者原判断与反证，不将只报告的具体算法称为现有书稿已覆盖。

## 2601.22136 — StepShield

2+1+2=5，采用 binary outcome 会遮蔽首次违规前后检测时机这一局部测量差额，不从“更早检测”推出阻止了副作用。§3–5定义 EIR 为检测不晚于首次违规 step；同 step 观察可能已在 effect 之后，不能成为 before-effect 安全授权。9213 trajectories 中1278 train为639违规/639配对clean，7935 test为639违规/639clean/6657 benign，类不平衡必须保留；Appendix A说明 GPT-4/Claude-3 合成、人工标注94%一致，不是真实incident logs。

中心冲突：Table4 Hybrid EIR .41，Appendix F Table14 的95% CI [.60,.66]不包含该点；已实际用公开 exact-v1 PDF p15 核实，非HTML错误。Table5 LLMJudge DEC .79、Hybrid .29，而紧接正文把 Hybrid .79 归为最佳。Table4“accuracy”协议在91.9% benign人口中不清晰；EIR比值不是检测时间倍率，不能照录2.3× faster。检测调用延迟不是端到端风险收益，硬件/precision/concurrency/队列与独立重复条件未披露；§9 KV/O(n²)推断不采用。

拟中心性能争议暂缓，不将排名/经济结论用于正面证据或 Books。保留 EIR 的定义供诊断，不授监控安全保证；重开需作者更正 Table4/5/F、同人口逐步标记和 detection-before-effect 的执行时序。原源在 CORE_STANDARD_22136v1.txt（含 PDF 必要段）。此为受影响结论隔离，不因深审工作量排除贡献。

## 2601.22129 — SWE-Replay

2+1+2=5，采用 archive 中间节点分叉与重放使十次探索不必十次从root开始的局部预算机制。§2–4.1 archive以既有regression通过为过滤，不证明patch任务正确；按file-set抽象状态访问次数倒数探索，repository paragraph count只是目标进度proxy。恢复仅在pattern detector认为无repo外变化时用per-step diff，其他情形重放action，不能当任意副作用sandbox snapshot正确性。

Naive10条从root与archive10条总轨迹对照；Appendix A.2 Pro731仅5条，不能统一成十次。Verified500/Multilingual300；Gemini3Pro Verified75.4→75.6、$2.88→$2.38仅作者API token计价；缓存所有先前context，未计环境/回归测试/重放walltime，不是等端到端预算。Devstral steps128/temp.2，Gemini variants steps250/temp.2或.8，不同模型不合并；无reproduction tests、regression filtering majority vote。50任务顺序module ablation非全factorial；reward judge54% cost1.44+1.87 vsproxy60%1.52，额外critic成本不能删。

拟仅报告：AGENT-PLANNING Ch79实际remaining budget/value分支与AGENT-TOOL-CALLING Ch78 snapshot lineage/cache identity边界不授权repo-diff恢复一般外部状态；本篇提供specific file-set/proxy/archive配方的局部收益，未建立可替代真实snapshot或可靠value的长期资格。不称具体SWE-Replay已被正文覆盖。原源 CORE_STANDARD_22129v1.txt。

## 2601.21961 — Visual Agent Factors

2+1+2=5，采用相同HTML/text/function下视觉因素会改变web-agent选择的局部对照；不把输入语义等价升为观测信息相同：blur改变可读性、布局改变可见范围/target box。§3–6五web snapshots、48CSS variants/8families，target固定第一item；viewport1280×1200、scroll600。UI-TARS7B/GLM4.1v9B/Qwen3VL8B与CUA各variant50次独立采样，temp1/top-p.8，Qwen3-14B相关自动judge。硬件/precision/API版本与完整E2E成本未披露。

TCR是bbox selection而非任务正确率；更大card改变目标面积，TMR是CoT提及不是内部attention。CUA baseline .364/orange .496/sidebar .055是同组局部行为，best/bottom事后选择、multiple comparisons及置信细节未充分披露；不能证明单一人类salience因果机制或所有视觉prompt都脆弱。

拟仅报告：PLATFORM-EVALUATION-SYSTEM 的可见信息、readability配对与task/oracle身份决定采用范围；这组CSS/页面population仍需独立可读性/面积控制，不把本次局部效应升为通用界面salience规则或controller权限。原源 CORE_STANDARD_21961v1.txt。

## 2601.21947 — ToolWeaver

2+1+2=5，采用文档embedding+tool co-use约束共享层级codes，序列长度/vocabulary参数与真实工具决策取舍。§3.2–4.3 RQ-VAE residual quantization、cooccurrence Laplacian项、最终Sinkhorn soft-assignment与trie；soft-balanced assignment不是hard唯一性或新tool语义保证。A.3 mpnet768→MLP64，2×1024新增codes，50epoch/codebook batch5096；LLama3-8B alignment5+trajectory2epochs/context6144，A100/ZeRO3/FA2，precision未披露。工具集合46985 APIs/约16kcollections，original与reimplemented基线分开。

必要反侧：λ10变差、naivehierarchy/semantic-only不自动优于atomic；SoPR I2 ToolGen45.13→ToolWeaver44.03、SoWR I2Cat37.90→35.48反退，retrievalNDCG不等execution正确。通用PPL base6.34→25.36虽比ToolGen104.54好，不是能力不变。B.7单A10080GB ToolGen108.16ms/P95111.98，L2 128.21/132.43，L4 183.14/189.11；toks/s19.54→24.53/28.26并非logical tool选择更快。batch/concurrency/promptlength/precision/SLO未披露；层级first-stage error会阻断后续参数检查，分母不同不能合并。

拟仅报告：生成tool-code是proposal接口，trie只限制词法可达性；新codebook/co-use prior要与训练checkpoint/library绑定，却不能从有限retrieval/SoWR得到普遍tool schema升级兼容性或低延迟结论。长期采用是否有具体owner差额请 root 校准，不因新formula或2048tokens自动改书。原源 CORE_STANDARD_21947v1.txt，只保留A.3/A.4/B.7/B.8必要段，未审其他qualitative附件。

## 2601.21937 — DeR2

2+1+2=5，准入仅document-grounded reasoning的四regime诊断，不进入AIforScience应用链。§2.1–2.3/3.1–3.3隔离Instructions/Concepts oracle/Related/Related+Noise；eligible试题依赖DeepSeekR1/Doubao的三次closed-book失败、concept至少一成一败，不能代表所有评估模型没有参数知识。81位理论题annotators、2023–25原论文与人工QA只是构造身份，不授因果完备。

§3.2输入统一30k字符head/tail截断会删除证据，noise组更长因而不是纯视觉/注意力干扰；temp1/top-p.7、每condition两次平均，API默认与thinking预算并非全部严格匹配。答案/概念提取/错误分类使用Doubao-seed1.6同judge，CoT error每模型/setting取50个答错样本为条件人口。Table2 Average Instruction55.9/Full51.2/Related62.9/Concept75.4；Gemini3Pro64.2→53.7是局部反例，不把RLoss=Concept−Full分解为独立retrieval因果量。正文“Concepts-only从less relevant evidence恢复”与定义冲突，不采用该归因；错因judge亦非internal causal ground truth。

拟仅报告：PLATFORM-EVALUATION-SYSTEM / AGENT-RAG 的oracle与实际retrieval分工不允许四regime差值自动识别内部原因；本篇保留长context给更多知识反退的局部population和protocol反侧，未变成生产通用检索/推理边界。原源 CORE_STANDARD_21937v1.txt 的精确protocol、必要difficulty筛选/3.3/Table2与conditional错误人口；已修复此前过长输出截断，不拿截断输出冒称全部证据完备。
