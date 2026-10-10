# Steer2Edit exact-v1 必要证据（作者审阅，独立 Source 待 root）

身份：2602.09870v1；公开日期 2026-02-11，date-extras 同日包络已由 root 实核。拟贡献：逐 token activation steering 的运行时干预→将同一方向编译为组件 rank-1 权重修改、用输入敏感方向与稀疏预算选择组件→在保留运行图的同时改变干预粒度；2+1+2=5。必要长期差额故定点深入，不加分授正确性。

原件：steercore.json L154–300 §3；steereval.json L301–379 §4；steerapp2.json L480–493 Pearson 证明、L557–609 提取/held-out 两阶段调参、L610–680 直接反侧/关键消融。精确来源 https://arxiv.org/html/2602.09870v1 。停止：不遍历余 F/G 全附件；已足支持拟采用设计与边界。

ΔW=λu kᵀ，u=v/‖v‖只保证这个线性组件输出的 v 正交投影不变，不保证多层模型语义/安全/事实真值不变。k∝Wᵀv 在非零/正方差条件下是 Pearson 最大值的一个解，奇异协方差不授唯一解。g=cos(v,Wμ)可能遗漏相消均值或稀有上下文；λ软阈值需要ρ>0、α<1。均值、steering data与调参并非免费。图不增加算子是结构事实，不是已测端到端 latency/SLO；hardware/precision/batch/concurrency Not Disclosed。

同一 mean-difference 向量用于两种干预，TruthfulQA probing/evaluation split与held-out提取/调参/测试分离有作者说明；QwQ-32B标注不是事实验证。安全向量来自ADVBench拒绝与Alpaca benign helpful差，属性与场景混杂未控制；GCG/ADV-LLM拒绝率和三任务utility不是自适应攻击/overrefusal全面保证。原文D.1承认Mistral弱GCG有稍差tradeoff；T3平均中k_mean safety高而utility降，k_svd某utility更高，稀疏/归一化是这套配置的实验证据，不普遍必要性。推理提取GSM8K最短/最长5%，长度不是wallclock；top-10/最佳配置是经搜索选择，seed/CI未披露。

拟 Books owner 需实际正文比较后定：模型层/表征干预优先；不以安全任务自动塞Ch72。独立 Source/PRE/POST 尚未授。
