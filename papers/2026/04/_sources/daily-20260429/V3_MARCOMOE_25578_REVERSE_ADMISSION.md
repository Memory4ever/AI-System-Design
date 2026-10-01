# 2604.25578v1 Marco-MoE：受限模型证据与贡献前关闭提案

本项原在旧 60 的潜在线索内；本次按[官方 exact-v1 HTML](https://arxiv.org/html/2604.25578v1) §1–2.2、§3.3.3–3.3.4/Figures 5/9/Tables 8–9、Appendix C 的必要段落，和实际 [Ch21 MoE](../../../../../books/part-02-model/21-moe.md) 的初始化、router 统计、语言条件更新相邻命题，重新做**贡献**准入，不因小模型、多语或模型报告题名机械拒绝。官方 v1 页眉 `28 Apr 2026` 只是文稿标识；若恢复候选，还须单独核真实首次公开事件及更早官方发布。这里也不宣布本日来源、负侧或独立日 Gate。

原始题摘最强的可能增量是：将同一 Qwen3-0.6B dense FFN 按中间维度切成细专家，在 all-active pseudo-MoE 阶段修正求和与 softmax 权重平均的幅度差，再以已发表 Drop-Upcycling 打破复制对称；随后以语言—专家激活频率的 Pearson correlation 显示相关语言有相似路由，扩展 29→64 种语言后英语均值看似维持。若它有受控证据证明「细粒度切分＋特定初始化」在相同 token/数据/active compute 下改变跨语干扰的边界，便可能修正 Ch21 的 expert 初始化和多语评测选择。

必要原文没有建立这个因果合同。§2.2 自述采用既有 fine-grained MoE 架构及既有 Drop-Upcycling；Figure 5 的 100B-token ablation 比较 upcycling 和 weight scaling 的训练 loss/尖峰，未把多语 transfer 或语言专家分化与粗粒度复制、等量数据和等算力相匹配。§3.3.3/Figure 9/Appendix C 从每语 100 篇 FineWeb-2 文档统计 routed-token frequency，再对矩阵做相关聚类；被 route 到某专家不等于该专家在输出上有因果必要性，也可能反映 script、tokenization、语料或共同训练分布，不能据此给专家贴稳定语言所有权。Ch21 现文已经明确 route frequency 只是处理机会，需输出贡献和干预验收；并已有 dense checkpoint 破对称、语言特异/共享 route 的条件更新与数据/optimizer 身份。

§3.3.4 的 64 语言模型从 Stage-2 分支，新增 **1.4T tokens** 并重调 Stage3/4 数据混合；报告英语平均 `63.7→63.6`、多语改善，但不构成只改 MoE capacity、其它条件固定的测试，更不证明 dense 同预算必然遭干扰。Table 9 也保留重要反例：Marco-Mini-Global 英语 MMLU `72.9` 低于 Qwen3-4B `75.2`，CMMLU `67.9` 低于 `76.6`，C-Eval `66.2` 低于 `76.6`，虽总 FLOPs 和部分多语切片有自身优势。模型参数数、active FLOPs、训练 FLOPs、语言/任务分布不能被压成“普遍性能/成本最好”。

因此作者侧把本项从旧潜在**具名前分母关闭**：当前可定位的是成熟 fine-grained MoE＋已有 Drop-Upcycling＋多语数据/课程的受限新模型 operating point，以及与 Ch21 已有判断一致的路由相关性例证；未隔离会改变本项目长期解释或设计选择的非同义条件。保留上述模型与消融原证，不称论文无价值或所有 fine-grained upcycling 均无新意。若补出固定 base/data/token/active compute 下，细切＋初始化对语言干扰/负载/输出贡献的受控反向结果，或真实 route 因果干预推翻 Ch21 当前边界，再具名重开；不为关闭而遍历完整附件和代码。该改判待**非作者负侧准入抽核**，不能当日级通过。工作账由此前 `106＝70 潜在＋36 前闭` 暂改 `106＝69 潜在＋37 前闭`，不等于正式当窗候选冻结。
