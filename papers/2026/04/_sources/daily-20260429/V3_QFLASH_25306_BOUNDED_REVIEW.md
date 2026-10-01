# 2604.25306v1 QFlash：整数 fused attention 的数值身份与执行边界

## 贡献准入与身份

[arXiv 官方 exact-v1](https://arxiv.org/html/2604.25306v1)题名 *QFlash: Bridging Quantization and Memory Efficiency in Vision Transformer Attention*。旧 60 完整题摘提出的可检验增量并非“INT8 比 FP16 快”，而是 tile-wise online softmax 一旦全程整数化，跨 tile 的 row-max 比较须同一单位、重缩放不可让整数累加范围滚雪球、指数近似也不能把整数除法带进 GPU 内环。§3.1–3.3／§4 Algorithm 1／Appendix B 分别把这三项连接到 scale release、固定乘法加 shift 的 ShiftExp2、与共享 scale/per-tensor 量化。原来 floating-point online-softmax 可按各 tile 调整数值范围；此处若选择 integer-only fused path，就须把 scale identity 与 overflow/SQNR 纳入 kernel correctness，而非仅用 attention 权重量化 bitwidth 决定部署。作者侧建议 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9`，标准审阅候选；是否构成 Books 增量见下，需非作者核。

## 必要评价及反证

§5/Table 1–5 只在单张 RTX 5090 上取 ViT/DeiT 的 `N=197,D=64` 与 Swin 的 window `N=49,D=32` 七个 attention shapes，batch 1/8。对 integer-only I-ViT 的最佳 kernel speedup 在 ViT/DeiT batch8 `6.73×`、Swin batch8 `8.69×`，不是对 FP16 FlashAttention-2 的倍率；§5.2 Table 3 对同一 A2 batch8 才有 FP16 FlashAttention-2 `929.6µJ` 与 QFlash `754.6µJ` 的 `18.8%` operator energy 差。其能耗来自 `nvidia-smi` 积分，不能称整机端到端能源或生产 serving。Appendix A 的 V0→V4 `62.4%` 也只在 A2、batch1024 的逐步替换微基准，不把它并入 batch8 headline。

§5.3 Table 4 直接给质量反证：QFlash A2 SQNR `32.50dB`，低于 mixed-precision INT-Flash-Half `38.19dB`；A7 `31.02dB` 低于 `39.07dB`。Table 5 的分类精度是在**只量化 attention、其余层保持 float**下测得：ViT-S `82.24` 相对 FP32 `81.38`，但 Swin-T `80.06` 相对 FP32 `81.35`、I-ViT `80.83`，Swin-S `81.86` 相对 FP32 `83.20`、I-ViT `82.81`。因此“整数内核”不等于整模型整数端到端，也不等于 Top-1 普遍无损；动态 activation scale 的计算成本须和 kernel 内 integer-only 声称分开。Table 5 混合不同方法原始 quantization granularities（per-token/per-head/per-tensor），虽可比较交付工作点，不能隔离所有收益的单一算法因果。

Appendix B.1 Fig 5 的 scale accumulation SQNR 随 tile 数迅速塌陷、scale release 相对稳定，是局部反证而非对任意长度无 overflow 的形式保证。Appendix B.3 Figure 8 称 per-token 对简单 integer fused path 难以直接比较；这不等于数学上无法重标定成统一 scale，只是重标定/转换可能吃掉目标收益。§4.3 的指数仍是分段/线性近似，不是精确 softmax；论文未给通用误差上界或 LLM 长上下文注意力、Prefill/Decode、尾 SLO 的测试。旧 FP16/mixed kernel 在质量敏感或转换成本占优时仍有效。

## 实际 owner、日期与下一步

[Ch49 的 FlashAttention 段](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)约 692–702 行已有 IO-aware tiling、online max/sum 片上通信及硬件适配；约 915–936 行又有量化 output 的数值一致性和 per-tile 精度/转换成本。但现文未把**整数 fused online-softmax 的跨 tile 比较同一 scale、逐步 release 防累加爆炸与整数指数 GPU division 成本**并成一个明确的执行合法性条件。可考虑 Ch49 最小增量：在 FlashAttention 与后续 numeric plan 的交接处说明，integer-only 不是只换 QK/PV GEMM dtype；需联合冻结 Q/K score scale、row-max/denominator 的累计单位、重缩放误差、指数近似和动态 scale 生成成本；若 per-token scale 需要重标定或质量退化，回退 FP16/mixed。只给这条受限合同，不照搬 QFlash 实现、Vision Top-1、单卡最佳倍率。先由非作者读实际 owner 与必要 §3/4/B.1–B.3 核是否真缺口；共享 Ch49 未授锁，当前不写 Books，也不计 Integrate。

arXiv v1 身份落本日官方公告 ID 批链。[作者代码仓库](https://github.com/EfficientCompLab/qflash) GitHub API `created_at=2026-04-23T04:41:04Z`，但[04/23 初始提交](https://github.com/EfficientCompLab/qflash/commit/532a2c8cc935)仅有一行 `# qflash` README，中心数值方法与代码至[05/06 Add QFlash 提交](https://github.com/EfficientCompLab/qflash/commit/46adca5a179f)才出现在可见默认分支历史；仓库早建不等于本项完整机制早公开。此窄链没有找到早于本日 arXiv 公告的实质同家族材料，可按官方公告批链暂定本窗正文；不把 repo 创建或 arXiv submitted 独自当首公开，也不据此宣称所有非默认分支/外部平台绝无早稿。Books 仍待非作者 source→owner 和共享锁。
