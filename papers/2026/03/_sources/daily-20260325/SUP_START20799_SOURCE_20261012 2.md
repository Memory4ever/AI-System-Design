# START20799必要Source与中心资格争议提案

次批准入/日期root已核，2+2+3=7保持。作者实际读[exact-v1](https://arxiv.org/html/2603.20799v1) §2.1～2.2/Table1～2、§3.1～3.5、§4.1～4.4/Table3～6及A.1～A.6/B.1～B.4；不是只凭题名判否，未核代码/复现，不扩全部AppendixC。

Cross-Generation让X生成T作为fixedprefix，Y续A；MATHLevel5 200tests/2Ktrain，Alpaca805 LCWin由Llama3-70B evaluator，2～3parse errors被排；ExpertQA90/10split与UltraFeedback2K/200、ArmoRM8B scalar reward。Qwen3 1.7/4/8及DeepSeek1.5/Hunyuan1.8，preset T/p不同、receiver身份变动，可诊断某个prefix对某个receiver的任务效用，不能直接读为CoT因果truth或整个domain不提升。Table2 Hunyuan/DeepSeek thinking仍有局部提升，不能被“RLVR不改善任何thinking”headline覆盖。

START PhaseI只将answer-token loss mask设0，thinking-token梯度仍更新同一theta；A仍来自当前model。§3.2～3.3却将其称stationary/fixed responsehead、物理无法通过answer改进reward，并据此“thinking是sole driver”。共享parameter被thinking梯度改动就会改变条件answer分布；零answer loss不是独立冻结receiver，原式未给单独frozen参数/stopupdate模块。Table5即PhaseI A_post配T_pre也明显改善（Win78.98 vs T_post/A_pre69.11），正是不能声称“只thinking能力变化”的直接反侧，不由术语授实现冻结。PhaseII去mask全token训，仍可作局部recipe结果而不能补PhaseI理论qualification。

1.7B seed、GRPO/DAPO、bf16/batch64/group6/prompt256/response3328/think2047/answer1280；GRPO KL.001、DAPO noKL和filtergroupsfalse/overlong等具体配置在B表，不是完整algorithm-only控制。baseline按convergence终止、START两phase不同训练流程，未证明同token/steps/compute预算；Table3胜率由受测judge/rm，不授独立真值或所有generalQA。硬件/全部epoch/重复seed与生产SLO未披露。mask计算、额外采样、长prefix和receiver续写都计费。

## root 非准备者中心资格裁决（2026-10-12）

实际打开精确 v1 §3.1～3.4 的共享 policy θ、mask 原式与 stationary/fixed-response-head/sole-driver 主张，以及 §4.3/Table5。只令 answer tokens 的 loss 为零，仍由 thinking 梯度更新同一 θ；没有独立 frozen receiver 参数条件。原 Table5 的 T_pre/A_post 同样改善不能支持 answer 行为冻结，不由 mask 名称授这种资格。PhaseII 和局部 recipe 胜率不能补足 PhaseI 这条中心理论链；不是拒绝其所有局部实验。

接纳中心争议终态 Books0，原 7 分候选保留。报告可保留固定 receiver 的 prefix 使用诊断及受限 mask 训练结果，不能采用 stationary-answer/sole-thinking 主链。精确重开条件为独立 frozen receiver 的实现/参数分离，或改写中心资格并在共享 θ 与匹配预算下给出拟采用命题的证据；当前非访问受阻，无 Books 锁，不预 DAY。
