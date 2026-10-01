# 2604.25317v1 FusionCIM：驻留对象改变融合的数据搬运账

## 身份与贡献准入

[arXiv 官方 exact-v1](https://arxiv.org/html/2604.25317v1)题名 *FusionCIM: Accelerating LLM Inference with Fusion-Driven Computing-in-Memory Architecture*，在本日 arXiv 官方公告 ID 窄批链内；本轮定点官方题名检索未见具名更早正式全文，仍不把 arXiv submitted 或第三方索引独证为公开时刻。旧 60 题摘所示设计差异由 §III 支持：传统 CIM 为了复用“静态权重”倾向把 KV tile 驻阵列，长上下文、多 Q tile 反复改写 KV 使 CIM write 与转置路径成为瓶颈；本篇让 Q 留 IP-CIM、O partial sum 留 OP-CIM，K/V bit-serial stream 经 score→FP16 online-softmax→PV 的两级流水。于是驻留对象从“看似应固定的 KV”改为“当前 query 与输出累加”，具体改变 CIM attention 的 on-chip write/transpose 选择，而不是一般 GPU FlashAttention tiling 换名称。作者侧拟 `2+1+2=5/9` 标准候选；仅就 CIM/LLM dataflow 的受限设计，不能因非商品 GPU 或局部硬件自动前闭。

## 必要评价与强反证

§IV/Table I 是 28nm 工艺模型、Cacti SRAM 参数、合成的 control/SFU 与架构模拟；16 Hybrid Engines、1MB Global Buffer、400MHz，非整片流片/端到端实机。Table I 明列 **Softmax SFU 为 FP16**，所以不能把整条 attention 流水误称 INT8-only；IP/OP MAC 是 INT8/bit-serial。§IV-A 的主 workload 为 LLaMA3-8B、最大 8K、GQA，但 Fig6–9 的数据重点是 256–4096 length；“与 GPT-3 可据类似结构推断”是作者外推，不是另做模型实测。

Fig6 同一模型构造下，相对 ordinary DCIM baseline 在 4K 最多 `1.98×` normalized latency 改善；相对“TransCIM-like” KV-stationary baseline 的 `21–40%` 延迟下降更能隔离驻留选择，但这个 baseline 也是作者按 TranCIM 原理重建，非同一商业硅片 A/B。Fig8 off-chip access 对 baseline1 减 `46.2–58.9%`，Fig9 on-chip access 对 baseline2 减 `64.3–71.0%`，是不同分母，不能加总。§III-D/§IV-B4 的 diagonal-first reorder 在 LLaMA3/RoPE 所测 prompts 减少 rescale `58.5–61.4%`，在论文所谓 BERT/ALiBi 为 `98.5–99.1%`；作者仍更新真实 row-max 并积累所有 KV，而不是 block skipping 或证明任意上下文最大值必在对角。score 分布换到 retrieval-heavy/attention sink/不同 RoPE 位置会改变收益，不能把 pattern 当保证。

Table II 更不能按作者“1.26× P3ViT”复述成**系统级公平能效优势**：P3ViT 行是 `23.2 TOPS/W (Macro)`，本篇 `29.4 (Sys.)`，计算层级不同；TranCIM `12.5 (System)` 虽标同级，也有 200/240/400MHz 与精度、Softmax support 差异。§IV-B 能源 `3.85×`／摘要 `3.86×` 为四舍五入/图值口径的最多相对 baseline，不是量产能效或生产 SLO。没有显式模型任务质量、FP16 SFU 近似误差及数值重排各自独立消融，不能从 rescale 次数减少直接推出输出逐 bit 不变；相同 KV 全扫描保语义对象，但 Taylor SFU 与低位 partial sum 仍须质量验收。

## 实际 owner 判断与下一步

[Ch49 FlashAttention 段](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)约 692–702 行已有 IO-aware tiling、tile group/NoC 局部通信/occupancy 与独立 GPU fallback；约 895–902 行已有 **以 score pattern 减 rowmax/rescale** 的受限分支，故本篇 diagonal-first scheduler 不宜单独另写为新定律。现有正文未把 **CIM 阵列 write 比 read 贵** 和 “KV-stationary vs Q/O-stationary 改变多 query tile 时的重载、转置、partial sum” 作为长上下文硬件执行计划条件；这是可能的唯一非同义缺口。若非作者认为项目主线需要涵盖该具体硬件选择，可在 Ch49 FlashAttention/低位 hardware 交接处补一条最窄条件：只在 CIM write 高且 Q/O 可常驻、KV streaming/FP16 SFU/NoC 成本合算时，选择 QO-stationary 两级融合；容量、质量或新 attention pattern 不合时保 KV-stationary/GPU。不要植入论文名字、29.4 TOPS/W 或通用能效结论。若 Ch49 现有 tile-residency/transfer 已实质覆盖这项，改为具体 Existing；共享文件未授锁，不写 Books，不把作者 proposal 算 Integration。
