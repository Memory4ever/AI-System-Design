# 2026-04-24：最后六项中心争议的有限非作者复核

复核日：2026-09-29。范围仅为已入工作候选的六项中心命题、印刷式/方法及相应处置；不代替 14 个来源入口、日期归属、反向负例或整日 Gate。均使用链接中的 arXiv exact-v1，未以作者后发修订替换当窗版本。`Disputed` 只隔离具体正面保证，不宣告整篇论文或所有实验无效。

1. [ReCAPA 2604.21232v1](https://arxiv.org/html/2604.21232v1)：§3.5 Eq.6 把 PAC 定为 `−slope(k, log q(k))`；Appendix D.3 则定义 `PAC_k=q(k)/q(1)`，后者 `PAC_k<1` 表示风险衰减，而前者衰减越快数值越大。取 `q(1)=0.5,q(2)=0.25`，两者分别为 `log 2` 与 `0.5`，不是同一测量量。作者的分层预测/对齐与有限成功率实验可分别存在，但 PAC 曲线及“更快恢复”的统一解释待 scorer/定义对应；维持中心评价争议、不写 Books。
2. [DiffMAS 2604.21794v1](https://arxiv.org/html/2604.21794v1)：Figure 1 明写前 `K−1` 个 stage 构造 KV trace 时不更新梯度，只更新末 Agent LoRA；§3.3 又以可微组合宣称 loss 梯度跨所有 stage 与 micro-step。共享 LoRA 在末 stage 更新后改变下一次上游 forward，不等于这次前向图穿过上游 KV 构造；Eq.6 仅给各 trace 子块梯度的上界，不能推出非零或等强。通信接口的 append-only 形式和受限任务结果不因这项歧义消失；但端到端训练的中心实现仍需计算图、detach 和参数共享清单，维持争议、不写 Books。
3. [ERA 2604.20854v1 官方 PDF](https://arxiv.org/pdf/2604.20854v1)：物理第 5 页 Eq.6 指明标签 `y` 是 one-hot，Eq.7 又打印 `tilde α=y(1−y)⊙α`。one-hot 各分量 `y_i(1−y_i)=0`，因此 `Dir(tilde α)` 的全部参数为零，KL 定义不成立；与 HTML 排版无关。不能自行替作者补常见 evidential-loss 公式，也不能由此推论其全部四象限任务经验为假。只隔离印刷 loss 与依赖它的中心可靠性解释；需同版 loss 实现/勘误后再议 Books。
4. [HARBOR 2604.20938v1](https://arxiv.org/html/2604.20938v1)：§VII 宣称 Boolean `{-1,+1}^d` 上 Matérn-5/2 是 Hamming 距离的仿射函数，并称替代的 linear tensor-product kernel 与参考核等价。但在 `d≥2` 时核随欧氏距离 `2√h` 非线性变化，`h=0,1,2` 三点不能共同满足仿射关系。该文还承认实现用 ridge 代替 SAAS/NUTS、不保完整 kernel-scale posterior；故参考设计的机会约束不可自动移交所测 artifact。89 个 Terminal-Bench 任务和 smoke telemetry 的局部经验仍可报告；等价/后验保证维持争议、不写 Books。
5. [PGU 2604.21041v1](https://arxiv.org/html/2604.21041v1)：Algorithm 1 在本次 hardening step 对每层梯度投影，`w'r=wr` 只对固定线性层和 `r∈range(P)` 成立。它不限制未来任意未投影的微调，也不保证全网改变后的激活仍属同一 retain 子空间；因此“所有 retain 输出精确保留”“后续任意形式微调不可复活”均超出已给条件。SD v1.4、两概念及 10 级 curriculum 的受限结果仍保留，不把 CLIP/ViT 阈值当开放世界安全证明。维持强保证争议及 Books 暂缓。
6. [HPO 2604.21045v1](https://arxiv.org/html/2604.21045v1)：§4.2 文本称质量与延迟各自 group-normalize，但 Eq.4 的延迟分母仍为质量 `std(q)`；Eq.7 外乘 importance ratio、Eq.8 的 clipped surrogate 内又含该 ratio。令正 advantage=1、ratio=2、clip 上界=1.2，非 KL 项按印刷式得到 `2×1.2=2.4`，不是单次 clipped surrogate 的 `1.2`。句级对齐与低质量屏蔽延迟奖励的设计分支仍可讨论，但印刷目标不足以确定实际优化；需 loss 实现或勘误，维持中心目标争议、不写 Books。

六项的必要反证、旧方案边界和重开材料与当日 `README.md` §4–5 一致。到此 15/15 项中心争议已有具名有限非作者复核；这是该子集的审阅闭合，**不是**整日候选、来源、日期或独立语义 Gate 通过。
