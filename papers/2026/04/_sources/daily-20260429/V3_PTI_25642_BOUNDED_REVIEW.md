# 2604.25642v1 PTI：prefill KV 干预的受限证据

状态：04/29 作者侧必要 exact-v1／实际 owner 审阅；贡献上拟 `2+1+2=5` Standard，具体 `No Change — Existing Coverage`。但同家族早于本窗的代码/README 已具名触发 **first-public Unknown 隔离**，不可计 04/29 正式候选；非作者和日期 Gate 未过。

## 机制与可保留结果

- [官方 exact-v1](https://arxiv.org/html/2604.25642v1)《Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language Models》§3.2–3.3、§4.1–4.4、§5.1/5.3、Table 1/2/5/6 与 Appendix B.3/Table 9 的决定性段已读。原第一批题摘从旧泛化前闭恢复为潜在是合理的：作者不只是报一个 VLM 榜单，而在初始 KV cache **一次**介入，分别用 MSCOCO 的 object-vs-background mask 与 caption object-vs-nonobject text 提取方向，视觉 token 全部 K/V 和最后文本 token K/V 用不同位置策略；与逐生成 token 干预形成时点、模态、缓存状态的真实设计分支。
- 同家族日期反证须单独隔离：作者自链的 [官方代码仓库](https://github.com/huaiyi66/PTI) 当前为 public，GitHub 仓库元数据 `created_at=2026-04-26T02:30:23Z`；[04/26T04:37:43Z 的固定 commit README](https://github.com/huaiyi66/PTI/blob/3bb504961f9cf16b112a4da0dbef04aae8be10f8/README.md) 已含同一正式论文题名、prefill 单次 KV、视觉/文本分向、object/background 和 `<1.02× latency` 等核心内容，仓库该 ref 亦含相关脚本与预提取方向。CVPR 官方 [proceedings 页](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Prefill-Time_Intervention_for_Mitigating_Hallucination_in_Large_Vision-Language_Models_CVPR_2026_paper.html)标 June 2026，不证明 04/26 网站可见。**仓库当前 public、创建/commit 早于窗并不能倒证当时已公开**，但也使 arXiv 04/29 公告批无法独证这是同家族首公开。需可核的 04/26–28 历史 public visibility、公开 release/网页归档或作者发布记录；若无法取得，按具名 first-public Unknown 安全隔离，不伪造小时，也不以此否认技术审阅。
- §4.1 在 LLaVA-1.5、Qwen-VL-Chat、DeepSeek-VL-Chat 三模型、greedy/beam/top-p=1.0 三解码设置测；§4.2 用 MSCOCO 100 对抽方向、CHAIR 500 validation images/512 new-token 上限。Table 1 的 LLaVA greedy CHAIR-S/I 从 `47.4/13.7` 到 `15.4/5.4` 是本协议下的受限收益，非开放视觉事实正确率；MMHal 96 项用 GPT-5 辅助评估，不是独立人类真值。Table 6 只对 KV 维度相同的 LLaVA↔Qwen 测 cross-model transfer，增量仅 `+0.13/+1.21` 个 accuracy point，不能称普遍 model-agnostic。

## 直接反证与成本

- §5.1/Table 5 的“视觉全 token”分支把 LLaVA greedy CHAIR-S/I `47.4/13.7→16.8/6.2`，同时对象 F1 `75.3→70.3`；加最后文本 token 的最终 PTI 是 `15.4/5.4`，但 F1 仅回到 `72.7`，仍低于 vanilla `75.3`。作者称文本分支“recovers F1”仅相对视觉单用成立，不能写成恢复原基线或所有质量维度改善。Table 2 的 LLaVA POPE adversarial F1 `78.75` 也低于 PAI `79.13`。这是风险减少与有用对象提及/召回的分账，不把少说或改变 yes/no 分布误当更可靠 grounding。
- Figure 2 的 PSH 定义为 `snowball hallucinations / overall hallucinations`：当干预降低总幻觉数，剩余错误的条件组成会变；PSH 上升本身不能证明**每个原本会出错的样本**更严重或是 decode-time 干预造成。要作反事实因果判断，须固定同一图像、输出长度/样本和首次错误位置，报告绝对 cascades 与条件严重度；作者给 VISTA 等局部现象，不能把“DTI 必然放大残余错误”升级为一般定理。
- Appendix B.3/Table 9 是单 RTX 4090 的 CHAIR token-level latency/throughput：PTI 对三个模型为约 `1.00×/1.01×/1.02×` ms/token，但**没有单列 TTFT、预填阶段 cache 修改、batch/concurrency、完整请求尾延迟或离线方向提取成本**。故“negligible per-token overhead”可保，“production end-to-end near-zero latency overhead”未证。共享方向应用于新模型版本需重提取/再校准，不能假定 KV 层/维度跨模型无条件兼容。

## Books 决策

[ROADMAP](../../../../../ROADMAP.md) 的视觉表示 owner 是 [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，评价 owner 是 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch23:623–625 已分 conflict sensor、head intervention、grounding/abstain 和模型漂移；408–416 已分一次 prefill 路径与后续 decode 视觉需要；822–830 已强调视觉写入 vs 语言读取、同图 paired intervention、CHAIR 改善不能遮住长度/召回下降。Ch66:2979–2981 已把 hallucination 分数与 decoding/output-distribution 替代解释拆开，并要求 paired grounding test。PTI 的对象/背景方向、初始 K/V 分槽和调参是所测模型的具体实现，论文没有证明现有 owner 缺一个长期可迁移 authority、状态或验收分账。因此暂为具体 Existing／不新增 Books；可在 Daily 报告其 prefill-vs-decode 条件和上述反证。非作者若发现有不被这些现文承载的可迁移分支，再定点重开，不因局部算法新意自动整合。
