# 04/20 两项印刷保证的有限非作者审阅

复核者：root；日报与原始必要源审阅作者为 apr20_resume。2026-09-28。仅重开中心公式/算法、相邻实验限制与实际 Books owner；不推断作者代码必同错、不否定全部实验，不代签整日 Gate。

## 2604.15750v1 DepCap

[官方 exact-v1](https://arxiv.org/html/2604.15750v1) §4.2–4.4 的 Algorithm 1 第 7 行将所有 `c_i≥τ_high` 的候选**同时**并入 `S`，第 8 行仅从剩余 `C` 删除与 `S` 冲突者；没有检查原 `S` 内部的每一对。按论文自己的式(6)，两位置都预测同一 token、相互概率 .96，`τ_high=.95`、`γ=−16` 时，二者初始同入 `S` 且 `2log(.96)>γ`，算法却原样返回，故“返回 conflict-free subset”不能由印刷步骤无条件保证。跨步 KL/熵的块边界估计是另一条受限启发式；这项反例不证明所有运行路径均违规，也不证明实现未补 guard。

与 [Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md) 的 proposal/target 检查与提交责任及 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 的迭代修正条件对读，不把局部 high-confidence seed 直接升格为已验证接受集合或端到端 SLO。认同 **2+1+3=6，中央 conflict-free 保证窄争议、Books 暂缓**；保留作者有限基准和方法信号。此为单篇具名独立 PASS，重开需同版内部冲突消除步骤/实现证据。

## 2604.15764v1 Early-Exit PAC-Bayes

[官方 exact-v1](https://arxiv.org/html/2604.15764v1) §III-A Steps 3–5 明写均匀 depth prior 下 `KL(Q_D||P_D)=ln K−H(D)`，又为 K 个 depth 用 `δ/K` 作 union allocation；二者的 `ln K` 在所印两步中同为正，不会凭空出现可抵消的 `−ln K` confidence 项。取 K=2、depth 总选一个出口，H=0 而 KL=ln2、分配项也含 ln2，足以反驳“所印证明直接给 H-only”。Corollary 2 去 KL 的确定性路由版本也没有由路由确定性推出 posterior=prior 的证明。§III-G 的 `sqrt(2 ln2)≈1.177` 数值本身正确，不把文本抽取的丢根号当反例。Table II 包含 BERT/GPT-2 小规模出口实验，但它们不能补足理论缺环或认证更大模型的路由泛化。

[Ch42](../../../../../books/part-05-inference-system/42-what-happens-during-inference.md) 的自适应执行与 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的验证/发布证据要求仍成立；真正可用的早退需把路由、质量、计算和独立验证共同绑定，不能由此印刷界单独放行。认同 **2+1+3=6，H-only/无校准保证窄争议、Books 暂缓**；不推断全部经验表无效。此为单篇具名独立 PASS，重开限于符号一致的证明及 router/backbone 条件。
