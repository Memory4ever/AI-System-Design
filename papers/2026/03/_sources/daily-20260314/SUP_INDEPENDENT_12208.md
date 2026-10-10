# 12208 ForensicZip：独立必要 Source / 具体已有覆盖复核

复核者：mar13_admission_review（非准备者）。2026-10-10；仅 03-14 补充窗口 2026-03-13，北京时间自然日。

## 本次实际范围

实际恢复 AGENTS、当前 Research / Report / Prompt、Sources 使用说明与 Daily / arXiv 切片、ROADMAP、本日 LEARNING_STATE 路由及 README 停点。原窗口、原候选及 §4 前缀不动；本 ID 已通过的完整题摘准入和 Mar13 日级归属复用，不由提交时刻重新决定公开日，不加载其他日期材料。

先读 [准备包](./SUP_EVIDENCE_12208.md)，随后从 [精确 v1 原 HTML](./SUP_NECESSARY_12208.raw) 实际解析并顺读 §3 / Eq1–9、§4 完整 Tables1–6、Implementation、表后直接评价和 §5。解析保留 MathML 的原始 alttext，不只读取准备者归纳；没有扩读图像像素、代码、版本差异、全部参考或未提供的 supplement。

[官方响应记录](./SUP_STOP_GATE_MANIFEST_RESULT.json) 对 `https://arxiv.org/html/2603.12208v1` 为 GET200 / 309691 bytes，2026-10-10T02:27:12.143405+00:00；exact ABS 为 GET200 / 41716 bytes。实际 [ABS 投影](./SUP_ABS_12208.txt) 的完整题摘与 history 显示 *ForensicZip: More Tokens are Better but Not Necessary in Forensic Vision-Language Models*、六作者及唯一可见 v1；第一作者 Yingxin Lai 与 From 的 Yingxing Lai 字符串差异保留，未伪称同字符串。当前该页没有可见撤回/纠错或具名早稿说明；这不是全站/全部版本无标记证明。

## 实际机制、资格与反侧

原语义显著性排序可能漏掉低显著篡改痕迹 → 跨帧 projected patch feature 匹配加 dummy 行列与固定 slack，再用 Laplacian 频率响应调节 novelty 排名并物理删 token → 需要按取证消费者重新验保留规则，而非把语义 salience 当证据充分性。这条贡献准入保持有效，不因应用名称或 Books 已覆盖排除。

Eq1–2 说明长视觉序列增加 attention 与 FFN 计算，但物理删选只影响后续所缩短的序列，不免除 vision encoder、全部 feature projection、selector 和其他输入/输出 token。Eq3 是学得 feature 的归一化；Eq4–5 在 `(N+1)^2` 扩展 cost matrix 上仍有固定相同 marginal，总质量为 2，dummy 提供 unit slack。因此这是扩展空间中的 entropic balanced 运输，不能由命名直接认证物理质量守恒被破坏。20 次 Sinkhorn 是有限求解，未证明 marginal 残差严格为零；dummy 路径受全局约束、熵与 birth/death 联合作用，不等于每个 token 独立按 c_birth 硬判真实出生。

Eq6 的真实源加权匹配成本与 Eq7 的 dummy mass 是 feature correspondence 代理，不是真实因果或篡改标签。原文自己承认 camera panning 可引发同样高 temporal cost。T=1 实际回退 `||z_j-mean(z)||` 的单图空间 novelty；没有相邻帧，不可把大量 image benchmark 的改善说成独立验证了 temporal birth/death。必要方法没有完整说明此单图分数如何接到 Eq8 的 e/b 符号，故本项不认证唯一可执行实现，也不为此扩查代码。

**Eq8 直接限制邻句的 AND 解释。** 它写 `(e+λb)(1+ηU)`，λ、η≥0；令 U=0 仍得到 `e+λb`，不等于零。因此只能描述高频放大与 novelty 排名，不能采纳“必须同时高 temporal 与 spatial”“zeroing either factor eliminates score”或滤掉所有自然运动的保证。令 temporal term=0 确实为零，但两个方向不对称。该反侧已定点核清，不否定 selector 能在某些任务有局部收益。

每帧保留 top `floor(ρN)` patch，global token 始终保留，输出 `T(K+1)`，这是清楚的缩序列接口；position / mask / 完整 artifact 未核。Eq9 的 OT 迭代为每 pair 的二次矩阵工作，并未把 pairwise feature cost 构造、Laplacian、pooling、encoder、projection 与排序费用都写成免费；“negligible”不能外推任意分辨率或长 video。

## 完整六表的采用范围

- **Table1**：完整 FakeVLM / FakeShield 八检测列及 50/25/10% 组已读。10% ForensicZip 八列全部低于 dense，虽显著高于该表其他剪枝对照，仍不支持原性能逐项不变。平均 FLOPs 3.102T→.452T 约减 85.4%，不是同一口径的 >90%；2.97× 对应作者平均 per-sample end-to-end latency 4520.2→1520.3ms。保留这些绑定口径，不能把保留 10% tokens 当所有成本均减 90%。
- **Table2**：FakeClue / 25% retention，分别披露 LLM-only、full-model、benchmark total latency、peak memory 和吞吐。ForensicZip 为 660.5s / 666.8s / 30:55 / 19.8GB / 2.70 samples/s，dense 为 1472.5s / 1478.6s / 67:59 / 26.7GB / 1.23；不是 Table1 10% 的同条件 2.97×。Caption row 写 FakeVLM-7B，表后正文写 LLaVA-OV-7B，不能静默合成统一 backbone 身份或通用模型收益，也不自行重解释这些 aggregate 时间为单请求 latency。
- **Table3**：POPE，A100 上 LLaVA-1.5 85.9→86.1，但 NeXT 86.3→85.8；不能从一个改善推出普遍 hallucination/取证正确性。两种 backbone 的 token 数、费用和分母各自保留。
- **Table4**：SID-Set / SIDA-7B / 10%，同预算 semantic Top-K、TNE、FS/HF 组件原表已读。若 Real/Tampered accuracy 与 Overall 来自同一二类人口，Overall 应位于两类准确率之间；例如 base 55.23/54.23 却 overall57.20，完整组合88.15/90.35却 overall92.50。必要文本未给使其一致的其他分母，故不采用这些 overall 数字作强化机制归因；不由此指控代码或全部表虚假。
- **Table5**：同 SID-Set 的 hard assignment / balanced OT / only-birth / birth-death 行保留为作者 selector 配置比较，不把分数提升当物理 conservation 证明，也不自动消除 Table4 的分母问题。
- **Table6**：FakeClue / FakeVLM-7B / 10%，None93.45、variance94.82、Sobel96.15、Laplacian97.74。只支持该局部空间算子选择；不证明自然高频均无假阳性或普遍解释充分。

Implementation 披露 A10080GB、εOT=.1、birth/death=.35、20 iterations 与所列 backbone；batch、precision、生成长度、并发、生产 SLO、seed 和不确定性未披露，不补造。training-free 不免除已有 encoder/projector 与下游模型训练，也不意味着线上 selector 免费。Table4/5 主人口为 image，单图 fallback 与跨帧模式须分开解释。

## 实际 owner 与 NC 判据

实际顺读 [Ch23 当前正文](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 537–645 的完整有关局部，涵盖包指543–579与608–634并补足中间邻接；不是仅查 review note。另实际读 Ch22/24 入口，确认 Ch23 拥有输入表示/选择，Ch22 管长上下文联合能力，Ch24 管生成状态与输出提交，不迁移 owner。

这里 **没有 ForensicZip 的 OT/Laplacian 配方或新实验**，不能声称该算法/结果已经写入。但经证据限定后要保留的设计命题有实际承载：

1. “方向性 compression 是受任务 truth authority 约束的 policy”，以及压缩率不等 information fidelity、稀疏关键证据可能丢失、原信号/readback 保有事实 authority（543、547–551相应段）。这约束取证消费者不能沿用语义显著性为充分证据，而非仅因两者都叫视觉压缩认定相同。
2. 同输入压缩/未压缩配对、分别验 selector 排序、预算、质量和完整选择费用，排名恢复也不是部署保证（568–572相应段）。取证方法的新本地配置是这项验收的实例，原表没有提供足以修改既有边界的全机制因果证据。
3. 选择/合并代理不是视觉事实因果判据，稀有瞬时证据可被丢；原输入/不剪枝回退与 compressor 自身费用必须进入总延迟；高 attention 不证明冗余，低 attention 不证明缺语义（stage/kernel/sink 的614–630相应段）。这直接承载所核 salience–evidence 失配及全费用边界，而非一般“效率有取舍”套话。

故 **NC 只针对以上长期条件/接口**，不是 OT、dummy、Laplacian 或新实验逐字覆盖；尚未成立的 physical conservation / AND 强保证不算可填长期缺口，也不用算法名称或榜单数制造新段。

## 独立裁决

**通过受限 Source、2+1+2=5 与具体已有覆盖 / Books0。** Design Delta 2 计取证消费者下语义选择失配及实际 proxy 的设计反侧，Reach1 是视觉输入压缩局部，Durability2 是可复用的任务/证据保留条件；不借成熟 OT、复杂度身份、A100 或速度 headline 加分。标准必要审阅完成，Eq8 与表分母的直接反侧已定点加深并隔离；不因 NC 降分或减少已完成投入，不作贡献 EX / 四分关闭。

不存在必要 Books 提案或写锁，不授 PRE / 实际 POST；公式宣传不用于正面 AND 或安全保证，Table4 overall 不用于新增数量级归因。若后续官方给出修订 scoring、清楚人口/分母、跨帧独立实证或新的可支持保留接口，再仅重开相应 Eq8 / T4 / temporal 与 image 桥接。当前有限单项到此停止，不授 DAY，不改共享 Report / Books / State / mainledger。
