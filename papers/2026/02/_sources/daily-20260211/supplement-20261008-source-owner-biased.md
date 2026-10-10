# Biased AI Feedback — 单篇 Source→owner PRE 请求

身份：SF-2026-ARXIV-2602-08259；exact-v1 https://arxiv.org/html/2602.08259v1 。公开日上下界 Feb10 BJT 已由 root 实读确认（不以注册时刻作公开时刻）。2+2+2=6，因具体纠偏目标的长期差额深入，未自授 Source/PRE。

## 必要已读与原件

v1 §3 DDPO、§4 DIPO 与 §5 全部核心实验，必要 theory assumptions 对应片段已读；webCore4–10.json、biased-eval.json（完整 S5）。不展开无关证明或全部附录。DDPO 以大量 AI label loss，加上同 pair AI–human loss residual 的 density-ratio 加权校正；DIPO 是当前 policy 采样的 symmetrized residual correction，不能合成同一 offline objective。generator likelihood、reference policy 与 label target 是不同身份。

理论只在覆盖/有界 weight、可实现性与 nuisance estimation 等条件下成立：DDPO BT reward-realizability、finite VC、AI-human agreement；DIPO fixed-policy estimating EIF、weak overlap、clipping 在假设下 inactive、oracle in class、nuisance一致及product小、MC准确等。少量 paired labels 不会自动恢复任意未覆盖偏好，也不是通用真实人类真值或发布安全。

实验：IMDb gpt-neo125M；summary/dialog Qwen2.5-1.5B。40% 随机翻转、20%恢复的模拟并非所有真实偏差；DDPO summary/HH 可复用原人工标签，sentiment 的“human”是 gpt4omini，DIPO 的“human”是 Qwen3-1.7B。真实弱/强 label 条件强模型又作 final judge，不能称完全独立人工验收。DIPO 一epoch online 与 SampledIPO offline 预算不同；Table6 summary DIPO 71.71/60.03 低于 SampledIPO 73.07/61.51，Table7 dialog高温58.75<59.99。hardware/precision、生成/标注/ratio估计的完整成本与生产SLO未披露；不换成总训练更便宜、全任务胜出。

## owner 实际差额

Ch34 §DPO保留了什么难题 277–338 已实读：pair provenance、teacher混杂、offline coverage/on-policy刷新、质量gap筛选和保守ensemble均已有；但没有“同pair的 paired residual + generator density ratio”纠偏目标。拟在第一项数据质量与第二项distribution之间自然补两段：训练target偏差与candidate生成人口错位须分开；paired correction需要独立校准/overlap、ratio估计及成本，普通审校DPO和人工/verifier仍合理。只采用DDPO有条件纠偏分支，DIPO作为不同online分支短区分，不复制完整理论证明、不宣普遍human truth。邻接Ch33/35在实际写前再读。

请求 root 实读必要原证及实际owner PRE；当前未获Ch34写锁，未写Books，单篇准备不等待其余日期或论文。
