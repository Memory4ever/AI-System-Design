# 12541 必要Source有效复用与唯一owner逐字PRE

仅本17补03/16；完整exact-v1题摘潜力已独核，日级字段SUP_DATACITE_BATCH；全2026 Daily精确ID/同题名去重未见有效同事件处理。root非准备者本轮必要原证及actualCh17差额已实读，以下复用，不重复全核心或借旧done。2+1+2=5，局部response-identification明确长期差额加深，未授Ch17锁/未写，reader Source/owner/PRE待核。

[exact-v1](https://arxiv.org/html/2603.12541v1) root实际§2–3/Methods L142–223：固定prompt只把末nonpaddingtoken当状态，余prefix rows固定；逐层Jacobian与concept首方向/Krylov reachability投32维LLV预测layergain。u*=Δy h/||h||²仅surrogate最小sum平方controlnorm，完整非线性模型另幅度bisection校准，不是所有token/全model线性化或精确安全控制。GPT2/medium/large十binarytask、400/200/200split、nominal128operating与3seed有限对照，aggregate相关不授任意层/任务/规模；conceptscore≠正确性，energy≠compute。硬件/precision/SLO Not Disclosed，artifact/实现/复现未核。

作者actualCh17 378–409优化解释→Layer冗余与Ch16/18开篇交接已读；原conditional gradient interpretation不是局部扰动跨层readout响应识别，冗余干预又需另一协议。唯一MODEL-TRANSFORMER-LAYER，不复制Ch20steering实际budget；拟迭代优化节最后、Layer冗余前两段，root提供草案按原证支持范围保存：

优化类比仍不能预测向某层注入一个小扰动后，读出会怎样变化。固定 prompt 时，可以只把最后一个有效 token 的 residual state 作为被干预变量，其余 prefix states 保持不变；围绕原轨迹求逐层 Jacobian，再投影到包含目标概念方向的低维可达子空间。该局部 surrogate 预测的是扰动跨层传播及最终指定 readout 的敏感度，不把整网、全部 token 或任意新上下文改写为线性系统。因果 mask 是固定 prefix 的前提，context、checkpoint、方向与局部尺度改变后必须重新核响应。<!-- source-family:SF-2026-ARXIV-2603-12541 -->

这样的响应模型可替代逐层盲试，为多层注入分配系数；在线性 surrogate 下，给定读出位移的最小平方控制范数有闭式方向，回到完整非线性模型仍须另行校准幅度并验证实际效果。[受限 GPT-2 家族对照](https://arxiv.org/html/2603.12541v1)只支持指定二分类概念与局部干预，不证明概念分数是真值、范数更小等于推理更快，或该模型能保证开放生成的安全。方向拟合、Jacobian/子空间构建及回归测试都有成本；任务或扰动范围失配时，保留实测层扫和不注入的基线。接下来判断哪些层可以删除，仍需要另一份完整干预协议。<!-- source-family:SF-2026-ARXIV-2603-12541 -->
