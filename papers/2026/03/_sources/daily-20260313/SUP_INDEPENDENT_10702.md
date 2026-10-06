# 10702 UniCom：单篇独立必要 Source / owner / PRE

复核者：mar13_admission_review（非准备者、非 Books writer）。仅 Daily 2026-03-13 的补充窗口 2026-03-12 北京时间自然日。启动及恢复实际重读 AGENTS、当前 Research / Sources 使用说明与 Daily/arXiv 范围 / Report / Prompt、ROADMAP、本日 README 开头及 LEARNING_STATE 本日路由；未加载其他日期候选。原窗口、原候选与 §4 前缀不改变。本 ID 完整题摘准入与 root 日级日期核验有效复用；仅 Mar12 arXiv 事件日，不签家族从未更早公开。

## 实际原证与停止范围

实际读准备包 [SUP_EVIDENCE_10702.md](./SUP_EVIDENCE_10702.md)，但不以其结论替原件。独立实际读取 [官方 exact-v1 原响应](./SUP_CORE_10702.raw) 中 §3.1–3.3 / Eq1–5、§4.1、§4.2 decoder / 完整 Table1、§4.3 全部机制比较 / 完整 Tables4–5、§4.4、AppA1–A3 与 AppG；另读对应精确文本的完整 Table6。直接解析 raw 的数学 alttext 与完整表格，不用摘要或图片解释代替表格。Figure4/6–8 仅 caption/正文描述，不声称像素、曲线或精确视觉结果已核。

[Manifest](./SUP_CORE_10702_MANIFEST_RESULT.json) 实际 ID/最终 URL 为 `https://arxiv.org/html/2603.10702v1`，GET200，452730 bytes，2026-10-10T02:51:10.550283Z。实际题摘身份为 UniCom: Unified Multimodal Modeling via Compressed Continuous Semantic Representations、Yaqi Zhao 等八作者；缓存显示唯一 v1，未显示 Comments、撤回或纠错标记。只核当前材料可见信号，不遍历全版本或全站证明无标记。主生成/编辑 Tables2–3、附录定性样本、代码与旧 codec 不展开；本两段采用不依赖它们。

## 必要 Source 校准

- §3.1/3.2 的表示为 N×d，d≪D；先联合训练压缩模块与重建 diffusion decoder，§3.3 再冻结 compressor 与 decoder、训练 prior。AppA 明确 SigLIP2 视觉 encoder 冻结；decoder 初始化 FLUX.1-dev，codec 训 50K steps/global batch256、33 aspect buckets；prior 的 alignment/PT/CT/SFT 分别 20K/115K/60K/7K。新表示不是零训练或仅廉价投影。
- 固定 N、降低 d 与降低最大空间 token 数是两个操作点。Table4 中 1024×64 MLP 的 .55/22.17/.66、MHA 的 .56/22.61/.69 相比 256×1152 的 .72/20.29/.56 支持作者所测 channel 分支，但 scalar 总数分别 65536 与 294912，未匹配表示 bit/FLOP 预算，不证明等预算轴向优势。MHA 的 rFID .56 还略差于同形 MLP .55；不能写所有重建指标都赢。原 1024×1152 的 .40/23.26/.69 也限制无损主张。降低 d 不等 N 缩短，更不使 N² 注意力项或整个系统计算同比下降。
- §3.3 **Pathway I** 理解直接输入未压缩 Z，编辑输入压缩 latent；文字“reduce context length”与 N×d / 保 N 操作点不能单独建立位置数缩短。本采用不补拼接或隐藏实现。Pathway II 则 frozen MLLM + MetaQueries + trainable connector；Pathway I fully trainable，容量/梯度资格不同。共享 codec 与 §4.4 局部较慢收敛现象不足唯一归因 query 的空间瓶颈，也不授 Transfusion 普遍胜出。
- 完整 Table5 六项 GQA/RWQA/SEED/MMMU/ChartQA/OCR：baseline 65.25/64.31/74.63/44.56/69.04/55.40；MHA 64.01/63.14/71.75/44.11/62.12/36.00，确实全部下降。MHA 相比 MLP 局部全部改善不等相比未压缩无损。Seq concat 为 65.03/64.58/73.62/43.33/69.24/55.50，混合升退，且保留原 feature；不能当纯压缩表示证据。该表使用 LLaVA-Pretrain-557k 与 Cambrian-737k，不改称完整统一模型本身的全任务证书。
- Table1 的 d64 与 d1152 为同 1024 分辨率下 .42/22.28/.61 与 .38/22.60/.61；FLUX-VAE 对照为512，不授跨分辨率质量等价。§4.3.1 正文约5×、Figure6 caption3.8×口径不一致，未读实际曲线，不采用精确倍数或端到端加速。AppG 承认细粒度信息损失与高分辨率/大规模资源压力。t-SNE 不证明表示同一、可逆或通用语义保持。
- 必要位置未建立实际端到端 latency/FLOPs、concurrency、SLO、总GPU小时/功耗及 seed/CI。Codec/decoder、prior 多阶段训练、额外特征/投影与 decode 均须纳入费用；不声称全论文所有配置均不存在，也不强制额外附件才能完成这两段限定采用。

Source：上述有限机制及直接反侧通过；不包含免费、无损、SOTA、等预算最优、query 唯一因果或普遍部署保证。

## 评分与实际 owner 差额

2+1+2=5 成立。D2 计固定空间序列与 channel 压缩的局部选择、生成目标与理解消费者分流；R1 是表示组件；Durability2 是可重复验收的压缩轴/消费者责任边界。不把 MHA、MLP、Flow Matching、Transfusion 的成熟原理或统一/VAE-free 标签计新贡献。具体 Ch23 知识差额需要受影响内容深入，已读足，不扩大附件。

实际顺读 [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 当前 240–262 完整连续表示前后：pixel-space 分责 → continuous feature → SemanticVocoder → 离散表示及相邻反侧；另完整 330–368 统一视觉责任与 rate/distortion/capacity 上下游。初次较宽输出截断的局部已再次定点读取，不以截断输出签全文。

现文已讲语义锚/条件 decoder、联合 rate/capacity/费用；GAE 还明确 patch-wise 降 channel 保 grid，但拥有的是 compact teacher→pixel bottleneck 监督位置。UniCompress 拥有 sparse/global/local 压缩及连续理解/离散生成/AR 展开接口。**它们未承载本稿统一连续 latent 中保 N 压 d 与减 N 的局部比较，以及 Pathway I 理解 raw bypass、纯压缩理解六项下降这一选择边界。** 新增不是主题关联或把旧通用原则再算贡献；也不称这两段吸收了完整架构/新定理/全实验。

唯一 owner 为 `MULTIMODAL-REPRESENTATION` Ch23。拟在 SemanticVocoder 完整段后、离散标题前放两段，与 continuous / discrete 替代分支衔接自然，不改音频分支。实际读取 [Ch22](../../../../../books/part-02-model/22-long-context.md) 与 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 入口：前者拥有通用序列/容量，后者拥有 factorization/noise/采样；不在它们重复 owner。Ch28/66 仅是训练费用/回归消费者路由，不需额外机制写入。

## 两段逐字 PRE 结论

准备包两段限定事实、收益/费用、反侧、回退均可采用；**一处最小必要修改**：第二段“正文理解路径直接消费原 feature”改为“正文 Pathway I 的理解路径直接消费原 feature”。原因：§3.3 的 raw bypass 仅直接声明于 Pathway I，不能无条件覆盖 frozen-MLLM Pathway II。其余提案可保留；“应携带身份”“所有费用均计费”与质量回归时保留旧分支是工程判断，不冒充作者已实现的治理/自动 fallback。

作者已原位修正；独立实际再次读取当前 packet 第37行确认仅此 Pathway I 限定已落实。限定 Source、实际 owner-gap 与当前 PRE：通过，已通知 root / mar13_supplement。六个本地引用实际存在，scoped diff-check 无警告；只新增本独核文件，不写 Books/Report/State/共享 ledger。未实际写入，不授 POST；普通单篇完成不授 DAY。
