# 2604.26365v1 负侧恢复：非作者准入与 Ch24 owner 有界判断

核验 2026-09-29，仅对 [官方 exact-v1 HTML](https://arxiv.org/html/2604.26365v1) 的方法、直接实验/附录与当前 Ch24 机制正文作有限判断。日期先由 04/30 owner 按首发规则另审；[abs-v1](https://arxiv.org/abs/2604.26365v1) 的 04/29 提交时间不是首次公开。

原始贡献不是泛泛“加速图像生成”：§3.2 把 TaylorSeer/FoCa 的 forecast 写成历史 final-layer feature 的固定系数线性组合，§3.3 将系数改成 **按 timestep 学习的 predictor artifact**；50 条完整 50-step 轨迹提供监督，部署时从历史特征预测被跳过步的 final-layer feature。状态所有权因此从只含模型/采样器/固定公式的执行计划，增加了与 backbone、schedule、特征层位和采集分布绑定的离线校准产物。当前 Ch24 已覆盖固定 schedule、trajectory-consistent calibration 与 learned reuse/recompute policy，但没有明确“固定状态外推公式 → learned feature forecast 参数”的分支；这是可写入同一 owner 的窄机制增量，不需要新章。建议 **2+2+2=6、标准审阅并因真实知识缺口深入比较、拟 Integrate**，待日期与全日来源 Gate；不因仅有领域图像结果而拒绝。

证据边界：§4 的 FLUX.1-dev、Qwen Image、HunyuanVideo 表格支持受测模型/步数上的 fidelity-vs-latency operating point；PSNR/SSIM/LPIPS是对完整采样输出的相似度，不是语义质量或生产 SLO。附录 §8 还记录缓存特征内存，50 prompts 的完整轨迹采集和 200 epochs 是额外离线成本，摘要的“约20秒训练”不能替代 end-to-end build/amortization。若 prompt、backbone、sampler 或步表改变，需要重新校准/验收；数据稀少或固定式已过质量门时，旧固定公式与 full recompute 仍成立。未见生产并发、跨硬件可迁移性或形式误差上界。

**2026-09-29 日期复核更正。** 作者 Rui Huang 的 [2026-02-22 公开主页提交](https://github.com/RuiHuangAI/RuiHuangAI.github.io/commit/f110b276ae138d1204e585bf2eb42df18d6aa8d4)及其[父版本原文](https://github.com/RuiHuangAI/RuiHuangAI.github.io/blob/2092f6334fecf7793ebff4fba261176761e788e7/_pages/about.md)已列同题、同九位作者及 L²P、50 样本、20 秒等中心机制。root 通过官方 GitHub commit API 核到该提交的 author/committer 时间，并读取父版本源码相应段落；这至少证明该机制家族在 04/30 前已由作者公开，不能以 04/30 arXiv v1 作为本家族首次公开。更早精确首发日仍可另查，但不影响本窗排除。

因此上段“拟 04/30 Integrate”被日期新证据覆盖：本日应按 earlier-family / Date Hold 从正面候选、评分与 Books 采用移出，只保留机制审阅用于追溯。Ch24 尚未为本家族写入；以后如按真实早期窗口重开须重新完成该窗口的身份和证据判断，不能把此处文字直接当已通过的历史 Books Gate。本记录也不把负侧发现等同完成全文审计。
