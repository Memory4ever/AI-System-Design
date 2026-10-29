# Nov21 窄主题发现的current／修订层

作者Noether；2026-10-15T18:13:00+08:00。本包是当前官方题摘/原comments/history的实际必要读，不是每个旧版比全文；只因本日有界七主题返回具体修订身份而开，不搬他日池。22份current完整题摘均原站200，`SUP_CURRENT_<ID>_20261015.html`/receipt绑定。提案20P2C；P为该current受限机制潜力，绝非Nov20首次事件、重大修订已成立/评分/Evidence。首公开旧稿与本轮修订资格并存，不能用版本号自动准入，也不把旧稿月份当current修订C。

| 当前精确版本；本轮history UTC | 实际潜在增量或关闭理由 | 提案 |
| --- | --- | --- |
| [2502.04420v5](SUP_CURRENT_2502.04420_20261015.html)；Nov20 15:25:17 | layer attention对KV量化敏感度不同，离线多目标precision pair/pruning/clustering减少online细粒度选择；不采near-lossless/吞吐，v5重要变更未知。`INFER-KV-CACHE` | P |
| [2503.17987v3](SUP_CURRENT_2503.17987_20261015.html)；Nov21 04:55:46 | adversarial prompt生成从handcrafted转posttraining，frame-semantic CoT＋RL多项reward；安全受限机制，不采query效率/transfer或展示操作配方；current晚版不倒填Nov20 | P安全 |
| [2504.01533v2](SUP_CURRENT_2504.01533_20261015.html)；Nov20 02:49:32 | 不加外部guard的logit方向与uncertainty调强度，须区分拒答概率/实际安全与正常效用；不授所有攻击防御 | P安全 |
| [2504.20039v4](SUP_CURRENT_2504.20039_20261015.html)；Nov20 14:38:33 | semi-greedy mismatch搜索产生judge训练标签，放松token分布匹配换task质量，lossless与task保真不同；不采2x/无损，accepted非重要修订 | P |
| [2505.03329v4](SUP_CURRENT_2505.03329_20261015.html)；Nov20 07:42:48 | glyph特征轻注入/区域text perceptual loss与分阶段训练，改变底层生成保留与局部编辑责任；不采97%全预算 | P |
| [2505.12114v2](SUP_CURRENT_2505.12114_20261015.html)；Nov20 23:28:29 | 完整AB是BigFive人格预测/传统affective评估，GAN改人口属性作招聘黑盒fairness audit；未建立foundation/LLM模型/系统新机制，只不能拿该领域结果类比成平台安全。非公平议题一律C，非小样本C，不需不影响关闭日期 | C范围 |
| [2505.23596v3](SUP_CURRENT_2505.23596_20261015.html)；Nov19 16:48:16 | GUI flow状态图/FSM随执行协作建模用于验证/恢复，需真实状态识别和副作用提交边界，不从FSM名称授可靠性。`AGENT-WORKFLOW` | P |
| [2506.06017v2](SUP_CURRENT_2506.06017_20261015.html)；Nov20 15:55:58 | 联合workflow/components层级搜索，coverage+balanced Bayesian生成value监督与uncertainty MCTS；需代理value与真实评估全费，不采8.34% | P |
| [2506.06941v3](SUP_CURRENT_2506.06941_20261015.html)；Nov20 00:19:24 | 同逻辑控complexity与trace预算测reasoning崩溃/三regime；只局部puzzle反侧，不授“不能思考”。comments camera-ready＋additional appendix discussion是必要具体新说明；若采用需该争论域，不读全旧稿 | P设计反侧 |
| [2506.12115v2](SUP_CURRENT_2506.12115_20261015.html)；Nov20 14:43:21 | cognitive operations改由self tool调用序列组织，外部tool与同模型重复调用预算分责；不是人类cognition因果/32→53通用收益 | P |
| [2507.11277v2](SUP_CURRENT_2507.11277_20261015.html)；Nov20 10:41:15 | 完整AB明确vision六阶段observe/metrics/detect/RCA/recommend/automate与四用户role，未给实际新执行、状态/授权机制或有效条件/反证；不能以AgentOps名词或一般“uncertainty”映射owner当贡献。并非vision/无代码自动C | C贡献 |
| [2508.07252v3](SUP_CURRENT_2508.07252_20261015.html)；Nov19 07:54:53 | 3D堆叠热约束下compute/memory异构与跨stack带宽共享是效率条件；不采GPU速度/普遍最优。history仅v2 Aug19 withdrawn、现v3已恢复，不能判current家族撤回 | P |
| [2508.08343v3](SUP_CURRENT_2508.08343_20261015.html)；Nov19 13:36:14 | adapter并发/并行共同决定starvation，digital twin生成配置训练数据；simulation误差/预测最优不等实际SLO，不能从同259KB授v3无变更 | P |
| [2509.13625v4](SUP_CURRENT_2509.13625_20261015.html)；Nov19 16:24:11 | per-private-record token分布DP聚合＋public blend，不重训亦有privacy accountant/查询预算；不采strong privacy口号或完整敏感记录无泄露 | P安全 |
| [2509.24006v2](SUP_CURRENT_2509.24006_20261015.html)；Nov19 14:34:19 | 高权重/高rank与低rank尾拆sparse/linear，critical/marginal/negligible三类同kernel支持fwd/bwd；FT费用与attention/end-to-end不同，不采20x/2.2x | P |
| [2510.22946v4](SUP_CURRENT_2510.22946_20261015.html)；Nov20 18:56:11 | 保留原理解/生成blocks并interleave multimodal attention；底层语义/空间与性能保留未普证，35B非全训费。只有v2 Oct29 withdrawn，v3/v4恢复不当current撤回 | P |
| [2511.06190v2](SUP_CURRENT_2511.06190_20261015.html)；Nov20 02:07:52 | 生成step前读small logits决定large介入，无外部router不等置信度校准/无需extra tokens；不采domain-agnostic/+20% | P |
| [2511.11729v2](SUP_CURRENT_2511.11729_20261015.html)；Nov19 10:34:02 | decode/PEFT共置统一allocator、two-stage predictor、QoS throughput schedule；compute-bound不自动证明无干扰/严格SLO，不能采46.2% | P |
| [2511.12079v2](SUP_CURRENT_2511.12079_20261015.html)；Nov19 07:45:37 | pretrained文本prototype先验/多模态prompt修正codebook，compactness/separation与Gumbel离散化；不把文本语义先验当groundtruth/量化sparsity当速度 | P |
| [2511.13984v2](SUP_CURRENT_2511.13984_20261015.html)；Nov19 20:18:33 | SQL AST gold标签避alias/容器误罚，再schema/node features估错概率；calibrated原claim需验证，不采AUC→真值/执行许可 | P |
| [2511.14214v2](SUP_CURRENT_2511.14214_20261015.html)；Nov19 17:19:20 | ranking/local order/conditional filter差异不能由最终EM合并；current声明v2脚注/仓库修正。仅该身份定点读[此前精确独核](../daily-20251120/DAY_REVIEW.md)中实际v1/v2脚注L103–112的typo/workshop有限层去重，不搬Nov20池，不证明全稿无实质改动；具体已核脚注不重全文 | P机制／已核窄修订去重 |
| [2511.14334v2](SUP_CURRENT_2511.14334_20261015.html)；Nov19 10:26:11 | CP描述结构保持而语境/措辞扰动暴露syntax-valid≠semantics/robustness；不能据qualitative下降证明训练污染因果，保有dataset/test条件 | P设计反侧 |

各旧首稿不当本窗首次；重要修订资格仍需原版本事件说明/官方公开日，accepted/大小变化不自动证明。Reason2Attack/LightFusion等history在补窗后与search Submitted20展示口径并存，不判站点错。除具名2506.06941新增appendix及14214已核窄修外，未无差别双版diff/全文，不把未做比较宣无变更。QMLLM/Feature inversion/poetry/Sleeper等安全必要反侧在其他新包分责，本包不合算式授全pool current。

新发现`2509.10518`当前withdrawn已Ohm9实际核/root可读；仅它当前采用链关闭。Tasa/LightFusion的旧withdrawn版本与有效current严格区分，未采用撤回版本/未在Books写入。未知日期currentP不入正式表，根协调是否需要清理既有采用链，不由writer越权操作共享。
