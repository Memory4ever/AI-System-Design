# Tucker Attention `2603.30033v1` — 标准必要 Source

准入 root 已完整 AB 校准；拟评分 `2+2+2=6` 仅针对 pre/post-softmax 张量多模态 rank 分解和接口取舍。必要精确 [v1](https://arxiv.org/html/2603.30033v1) §2/§4 已读，原件 [核心](SUP_CORE_2603-30033v1_20261013.json)与 §3 兼容性 [原件](SUP_FIRST_PROOF_CORE_20261013.json) 已读；未读无关附录、代码或复现。Source 独核/日门/Books 判断未预支。

## 原约束 → 实际增量 → 选择

MHA 的每头 `WQ_i WK_i^T` 与 `WV_i WO_i` 是低 rank，但没有同时利用 head、query/key、output/value 轴共享的子空间。作者将两类矩阵沿 head 堆成两个三阶张量，以核心＋每轴基矩阵 parametrization，允许连 output/head 轴一起压缩。参数节省的条件是这些 rank 远小于 model width；不是增加 rank 即无损压缩。§2 的 canonical MHA/GQA/MLA 作为指定 rank 形式可表达，讨论的是参数/可表达集合，不是现成模型无需训练即可等价替换。

§3 KV 保存 `XU3` 与 `XU3_tilde`，若共享 down projection，可保存单份 latent；同 rank 下与 MLA cache 相同，不把额外参数减少混为额外 KV 减少。FlashAttention 入口先形成每头 query，与共享 latent KV 以 PyTorch GQA=1 kernel 消费；专用 tensor-core kernel 是 future work，没有验证全部 kernel 自动利用 core 因式分解。

重要反侧：标准 head-dimension RoPE 放在 Q/K 中间，不能直接与 fused tensor 因式分解相容。作者移动旋转到 latent key 维度，保留相对位置性质，但改变频率/算子配置；**不授已有 RoPE checkpoint 权重与输出不变的 drop-in兼容**。§3.2.1 的 MLA latent-RoPE 是替代架构分支，非已证明取消所有现存位置分支的迁移保证。§3.1 Eq9 与 §3.2.1 Eq13 的 core/上投影符号有需区分的记号，当前不照录这些式子为已核完整实现。

## 评价与不能证明

- ViT：从 HuggingFace 预训练权重作 SVD近似，再下游训练；5 runs 均值、作者称标准差<0.1%。这是初始化＋微调，不是完整匹配预训练预算的巨大模型结论。
- GPT2：OpenWebText，从头同hyperparameter、fixed seed，N1024；Shakespeare N256另测。shared-MLA某rank不稳定/发散；不是所有MLA配置必不稳定。参数表只计 attention weights，而非总模型体积。
- Llama3-style1B：OpenWebText2从头、固定non-attn/hyperparameter，每设置一次fixed seed；4×H100分两节点训练，decode单H100、batch1、query1、cachedN4096、BF16编码，10iterations timingmean。Nonoptimized research code虽计完整iteration，不能作production吞吐或tailSLO。
- Table3：baseline GQA8 loss2.61/PPL13.62，Tucker32/64/64 loss2.69/PPL14.76，iteration4.87→4.05ms；decode1.310→1.274ms。更少attention参数和cache仍付质量代价；不是参数省8倍即可推decode省8倍。相比同cache的MQA32/64/64并非全质量胜出。模型rank、task、trainingbudget选择要联合校准。

## 日期与后续

v1 Submitted Mar31T17:30:51Z、2603首次announcement月在 root已校准正常公告下界/月底上界范围内；仍须当前官方页轻量修订/先公开信号检查，不用Submitted或DataCite created单独授窗。若拟补 Books，先与 `MODEL-MULTI-HEAD-ATTENTION`/相邻位置与KV章节实际正文比较，证据支持的差额明确后再PRE申请；本文件不是书稿写入或已有覆盖收据。
