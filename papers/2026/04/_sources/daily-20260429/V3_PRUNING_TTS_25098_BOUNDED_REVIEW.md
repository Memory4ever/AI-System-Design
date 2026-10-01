# 2604.25098v1 剪枝粒度与 test-time reasoning：受限证据

[官方 exact-v1](https://arxiv.org/html/2604.25098v1) §3–6、Table 1、Appendix C 的必要配置与实际 [Ch28 预训练／模型压缩 baseline](../../../../../books/part-04-training-system/28-pretraining.md)「模型压缩的 Baseline 必须绑定训练预算与可执行粒度」对读。只核决定贡献与反证的主结果，不展开全部例题/引用。题摘初筛链见 [batch2](./V3_REVERSE_TITLE_ABSTRACT_BATCH2.md)。官方 v1 页眉 `28 Apr 2026` 不是独立 first-public 证明；潜在候选待本日公告与早公开例外核。

## 机制与评价

旧反向准入的具体入口成立：先前“删整层会损伤长链推理”不能推广成“任何稀疏化都会损伤”。作者以 ShortGPT 删 1/2 层与 Magnitude/Wanda 10%/20% 非结构化 mask 比较，在 s1.1-7B、Qwen3-8B、四个数学/科学 benchmark 和 512/1024/2048/4096/8192 thinking-token 限额下，每配置三次随机种子。20% global sparsity、8192 tokens 的 Table 1 显示 s1.1-7B 的 Magnitude-Uniform AIME24 `0.1000`、MATH500 `0.6360`，而 Wanda-Uniform 分别 `0.1775`、`0.8107`；将 Magnitude 改 LayerIF 分配后为 `0.1556`、`0.8007`。因此不能把 unstructured、layerwise allocation 和 structured deletion 合成同一种压缩干预；在这个较弱模型上选择 mask criterion/层分配会改变 test-time reasoning 的任务结果。

负面边界同样必要：ShortGPT 与 10/20% mask 的实际删除参数量仅“约相似至多差 7%”，不是同计算图或硬件执行成本；LayerIF 被改为同时作用 attention/MLP 且 Hessian 取 identity，非原版的独立方法对照。Qwen3-8B 各配置更接近，nonuniform 不普遍胜 uniform；Fig 2/Table1 的部分剪枝模型胜 dense 是给定四题库/种子/解码预算的效果，不能称剪枝抑制 overthinking 的因果解释已被测到。论文没有真实 sparse kernel latency、峰值内存或端到端成本的匹配对照，稀疏参数数目≠可兑现吞吐收益；训练后不恢复也是该协议限定。

## 准入与 Books

作者拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，Standard、Report Only。贡献是对“结构性删层损伤 TTS”外推范围的具体负例，保留候选而不因两种 7–8B 模型/局部题库关闭；但 Ch28 已明确按 mask/granularity 比较质量，细粒度稀疏可保质量却须目标 kernel 证明 latency/memory/SLO，结构性剪枝收益和容量损失另算。因此这篇所测结果支持现有责任划分，尚无非同义 Books 机制；Ch28 不改。它也不证明相同 reasoning 能力以更少现实 test-time compute 得到。待非作者有界核、日期/来源/整日 Gate；本项原在 106 潜在中，作者工作账不变。
