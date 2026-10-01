# Apr14 十家族有限非作者机制与 owner 复核

审阅者：apr02；作者：root。2026-09-27 实际重新打开下列官方 v1 必要方法、中心公式、关键实验/反例，并读取对应 Books 实际正文与相邻交接。当前 AGENTS、研究合同及写作/学习方法已亲读；未变化的上下文复用。本文件不是日期/全日 Gate、全附件证明核验、实验复现或 Books 实际写入。家族归属由作者日级联合日期依据验收，不能从 Submitted 推首次公开。

## 总体裁决

| 家族 | 三维评分建议 | 必要审阅与最终采用范围 | Books |
| --- | --- | --- | --- |
| 2604.09942 | 2+1+2=5 | 标准完成，受限视觉机制 | 仅报告 |
| 2604.09970 | 2+2+2=6 | 真实责任差异，缺口深入 | Ch36 窄提案通过，未写 |
| 2604.09975 | 2+2+2=6 | 真实表示/边界成本差异，缺口深入 | Ch49 窄提案通过，未写 |
| 2604.10027 | 2+2+2=6 | 深入完成；单 key 与伪代码形状歧义隔离 | 仅报告，不采用 query-dependent selection |
| 2604.10065 | 2+2+2=6 | 深入完成；raw-logit 二元目标不是概率边缘化 | 仅报告，不采用语义分布保持 |
| 2604.10071 | 2+1+2=5 | 标准完成；内部双 anchor 的受限实现 | 仅报告 |
| 2604.10074 | 2+1+2=5 | 标准完成；MTGM 条件理论 | 仅报告 |
| 2604.10079 | 2+1+2=5 | 标准完成；MC 检测与多原因配方 | 仅报告 |
| 2604.10103 | 2+2+2=6 | 缺口深入，视频生成历史迁移/训练身份 | Ch24 canonical 窄提案通过，Ch25 仅交接，未写 |
| 2604.10152 | 2+2+2=6 | 缺口深入，自借 target experts 与驻留耦合 | Ch48 窄提案通过，未写 |

## 逐项实际依据

### 09942：连续性线索的局部因果证据不是完整 object binding

[官方 v1](https://arxiv.org/html/2604.09942v1) §3–7：同像素旋转/位置控制、CSI、七种 ViT、top-five heads mean-ablation 与 random-head 比较实际已读。连续性头能改变作者 synthetic binding probe，早层集中，但其他头/邻近线索仍参与；自然 PartImageNet 仅受限消融，不能推所有物体绑定由这几头负责。Ch23 视觉 writer/read-path 与 full-sequence intervention 两侧正文已经要求匹配控制、分离可读性与行为。具体 Gestalt 发现仍有贡献，不因 ViT 自动排除；无需把受限头定位写成新的普适设计责任，5 分标准仅报告。

### 09970：共识模型估计与 node-local adaptive history 是不同状态

[官方 v1](https://arxiv.org/html/2604.09970v1) Assumptions1–3、Algorithm1、Theorems3.1–3.3、§4.1–4.4 实际已读。节点本地保留 adaptive moments/滞后 preconditioner；通信更新 reconstructed-model estimate 的压缩残差，再对邻居估计做 gossip，并非平均 Adam 状态或原始梯度。Ch36 Local-SGD/error-feedback 与 canonical Adam owner 段尚未明确这个分支。可在 Local-SGD 后补共识对象/本地优化历史/重建估计的 checkpoint 分责。固定 doubly-stochastic 图、contractive compressor、bounded gradients 与 T/K/拓扑条件不能省；所谓 topology-independent 步长只在指定渐近区间。CPU CNN、四 A100 上 10.7M GPT，不推任意生产 Adam/大模型线性 wall-clock 加速。6 分 gap Deep 窄提案通过，旧同步 dense/local bounded 更新保留。

### 09975：encrypted execution 的边界数量不是总边界成本

[官方 v1](https://arxiv.org/html/2604.09975v1) III-C、IV-B、V-A/B、VI–VII 必要段实际已读。packing 链可吸收布局转换，real/imag 边界分成两实数 shares；conversion payload 还取决于 scale、modulus-chain、fixed-point ring。Ch49 previous-backend/state 与 FHE calibration 段已有一般切换原则，但缺这些加密表示责任。可在 FHE/MPC 分支补：不要仅最少转换次数，联合算 payload、数值映射、两侧安全假设和后续乘法所需 level。A100、GPT2/BERT、GLUE，LAN/WAN 数字由局部实测加网络 overlay，非真实端到端网络部署；近似 nonlinear/BatchLN 不是原 Transformer 精确输出。6 分 gap Deep 窄提案通过，MPC/明文受信路径仍是有条件替代。

### 10027：单 pooled key 的 softmax 不产生 query-dependent 内容选择

[官方 v1](https://arxiv.org/html/2604.10027v1) §2.2–2.4、AppendixA AlgorithmS1、B/C 必要段实际已读。Eq4 的 mean-pooled f_info 是一个向量；若 K 只有一项，softmax 权重恒1，query 不决定所读内容。层投影变化仍可能改变 anchor 表示，但不是 query selection。AlgorithmS1 又列 L_info×D 输入，未清楚对齐主文 pooling 形状；不能替作者补实现。Ch22 独立 anchor state/causal self-attention 正文只可保留弱架构命题，不能泛称完整覆盖动态检索。实测 rank/attention/RTX4090 prefill 不是信息完整性证明。6 分深入仅报告，隔离动态选择强解释；不否定全部经验，也不为这处歧义展开版本史。

### 10065：binary timing surrogate 与原 token 分布是不同目标

[官方 v1](https://arxiv.org/html/2604.10065v1) §2 Eq1–3、§3/4 与设置实际已读。Eq1 对 pad/nonpad 各组 raw logits 求和再 binary softmax，非 logsumexp 或原 token probability mass。共同加 c 时原 softmax 不变，binary log-odds 却增加 c(n_nonpad−n_pad)，已足够否定 marginal-preserving 解释。Shared LoRA/embeddings 仍可改变组内语义；binary KL 不能保证组内原分布。Moshi、八 V100、额外三秒 baseline prompt、ASR/judge 与 1s reward 门槛限定结论；语义与 latency 切片并非全胜。Ch23 流式提交/模态消费已有弱分权原则，不补错误投影。6 分深入仅报告经验 timing policy，不采用语义保持保证。

### 10071：双 anchor 是条件化 decoder proposal，不是视觉真值

[官方 v1](https://arxiv.org/html/2604.10071v1) §2/3 Eq1–6、§4.4–4.6、AppendixA.3 必要段实际已读。VAS attention mass 选 Spotlight/早层 Shadow，组合中间 logits 并限制 final-layer plausibility set；相关 attention 不证明纯视觉信号/纯语言噪声，候选概率阈值也非语法真值保证。Ch23 视觉路径、内部 counterfactual decoder 与行为回退已承载拟采用的一般责任；本算法不是完全相同，但不足单独加正文。五种7B模型/RTX5070Ti；作者实测 overhead 1.31–1.35×，不采用≈1×免费，α/β 过强反退保留。5 分标准仅报告，不把所有附件的强保证采入书稿。

### 10074：受控 MTGM 可学性不等于现实 DiT recipe

[官方 v1](https://arxiv.org/html/2604.10074v1) Definition1/2、§2、Theorem1/2、§4.1–4.3 必要公式与解释实际已读。正交 Gaussian patterns、多 token 与单层单头 denoiser、W=0 初始化、population GD 条件下，attention 学同 pattern 聚合。维数/样本 token 数、低概率模式与 SNR、步长/迭代数条件都进入近 Bayes-risk 结论；知道 latent labels 的 oracle 不是部署 oracle。Ch24 当前表达性/有限训练/terminal mismatch 已分账，不把这条特例理论当通用训练 owner。5 分标准仅报告，保留理论贡献，不声称已审所有附录证明或可直接加速现实采样。

### 10079：测到训练样本的 MC 失败，不等于已定位知识不存在

[官方 v1](https://arxiv.org/html/2604.10079v1) §3.1–3.2、§4/主表、§6 必要段实际已读。作者把原 demonstration 变为 MC 再重复检测；其 pass@N 字段实际是成功比例，confidence BoN 也不是 oracle upper bound。格式转换、distractor 与阈值能改变检测，zero-shot 失败不足证明基座不存在知识。CPT 新数据、冲突分桶、重采样/增加 epochs 是不同干预，不能把额外数据/预算收益归于唯一五因分类。Ch29 拟合损失≠真实行为、数据与优化预算主线已覆盖一般采用命题；本受限配方保持可报告，不自动加一套诊断 taxonomy。5 分标准仅报告；模型、训练集/外部领域任务口径分开。

### 10103：canonical 是视频生成的历史迁移，不是环境 state 真值

[官方 v1](https://arxiv.org/html/2604.10103v1) §3.2 Eq3–7、§3.3–3.5、§4.1/主表实际已读。evicted-only 历史先累积 L/H 再释放 KV，近期 top-block attention 独立；dense 1000→hybrid 1000 更新，train/infer capped relative RoPE 与 first-step latent teacher regularization 共同治理迁移。实际对读 Ch24 帧内 exact/跨帧 recurrent 与 block-cache 两段，以及 Ch25 History Bank/self-rollout 交接：前者未承载 eviction 时点与模型迁移时机的具体分支，后者包含 observation reconciliation，不能混成本文证明。canonical Ch24 窄 gap 6 分深入通过；Wan2.1-T2V1.3B、单 H100/no quant、832×480、30s 定量与长视频 qualitative 分开，固定状态不等无损/无限期稳定/物理 dynamics。局部 attention/短历史回退保留。

### 10152：无额外 draft model 不等于无需验证或免费驻留

[官方 v1](https://arxiv.org/html/2604.10152v1) III-B/C、IV、V/VI-B/C 必要段实际已读。target hot experts 子集驻 GPU 自借 draft；offline affinity 缺 expert 替代只产生 proposal，target verification 仍裁决。Ch48 既有 fixed-trained-draft/union-loading 段没有该 no-extra-draft-artifact 与动态热集/affinity 耦合的替代条件，6 分 gap Deep 窄提案通过。作者 Xeon/PCIe5/H100配置、NLLB WMT greedy，Mixtral/Scout CNN temperature1 sampling 是不同 contract；更多 N 的 acceptance 上升不保证 throughput，上未接受 token 仍付 expert-union 搬运，小 batch≤4 可输 caching。只补 residency/hotness/replacement 与 target verification 同时结算，保留 target-only/固定 draft 回退；不从借用同 weights 自动推出任意 sampling exactness。

## 交付边界

四个真实窄 gap（09970/09975/10103/10152）仅通过本轮 source→owner 非作者采用提案，没有改 Books、作者日报或共享状态；写后仍需独立实际正文核验。六个 Only 保留证据与限定，其中 10027/10065 为必要强解释反向消歧，不是把所有实验判 Disputed。未新增题摘/宽库存，不重跑日期、来源或全部附件。root 负责最终表、准确时间归属与日级 Gate。

## 四项实际写后复核（apr02，非正文作者）

本次实际顺读 root 新写的四处正文及各自两侧衔接，复用以上已核、未变化的 exact-v1 必要方法和反证。结果为四项写后通过；没有重审整章、全部附件或复现实验，也不代替 04/14 日期、来源与日级验收。

- **09970 / Ch36，约75–81行**：Local SGD 后明确 local moments、本地参数与压缩模型重建/gossip 的不同对象，保留独立恢复状态及 compressor/mixing revision。连通、有界梯度与特定 adaptive 条件没有扩成全局 Adam 等价，通信减少没有冒充 wall-clock 收益；后续 tensor partition 不能证明优化等价的交接准确。Checkpoint 身份要求属于本项目推断，不是声称作者验证了任意恢复协议。
- **09975 / Ch49，约237–245行**：在 previous-backend state 后补加密表示切换，packing、scale/modulus、fixed-point mapping 与 payload 共同计划，未把最少转换等同最快。安全密钥/暴露责任留给 Security；近似非线性与 LAN/WAN overlay 限制保留，后接 accelerator readiness 自然。没有制造实际 WAN 部署或通用 round-trip 保证。
- **10103 / Ch24，约73–79行**：接帧内 exact/跨帧 recurrent 分支，明确只对待淘汰帧先移交线性统计、再释放 KV，近期窗口独立。dense→hybrid、同 temporal cap 与首步 teacher 目标被限制为受测生成迁移；压缩不等无损或无限稳定，Ch25 action-conditioned transition 仍另验。正文没有把 Wan 视频生成改称环境真值。
- **10152 / Ch48，约716–724行**：接 trained-draft/expert-union 分支，自借 resident target experts 只在 proposal 内替代，target verification 仍裁决，热集更新与 affinity/替换成本完整。greedy 与 sampling 评价分开，小 batch 和更多驻留 expert 的反收益保留；移回的收益引句紧接四条件，衔接成立。没有从共用权重推出任意 sampling exactness。

四处 source-family marker 与对应 Review notes 均实际存在。此记录只证明本轮窄正文与来源边界/相邻逻辑一致，正式日报采用与完整 Gate 仍由 root 协调。
