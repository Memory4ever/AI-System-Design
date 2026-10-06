# 2025-11-11 有限普通题摘裁决

作者Noether。仅本日窗口`[2025-11-10T09:00:00+08:00,2025-11-11T09:00:00+08:00)`。以下18篇均实际读取原exact-v1完整题摘，未从当前月表标题冒充v1；不是18个已确认当窗事件，未进入Books。原history的submitted保留其性质，不推定public。各潜在项最小日期重开为精确版本官方公告/真实首公开上下界完全落窗；若早公开则需本窗实质修订及原公开证据，不重复展开全部实验。

| 精确原身份 | 实际增量及采用边界 | 日期/处置 | 原raw |
| --- | --- | --- | --- |
| [2511.05534v1 FlowMM](https://arxiv.org/abs/2511.05534v1) | 单模态重要性不能直接处理跨模态attention差异 → 层间跨模态信息流引导KV merge与敏感度自适应匹配 → 可重审多模态压缩的质量/状态成本。作者加速不是生产保证。 | submitted Oct29；潜在，日期隔离。 | [第一组](./nov11-abstracts1.txt) |
| [2511.05541v1 Temporal Sparse Autoencoders](https://arxiv.org/abs/2511.05541v1) | 单token稀疏特征可能混入词法 → 时间邻接对比目标偏向持续语义激活 → 可重审表示诊断；不证明语义特征是因果真值。 | submitted Oct30；潜在，日期隔离。 | 第一组 |
| [2511.05578v1 UTF-8 Plumbing](https://arxiv.org/abs/2511.05578v1) | byte token不保证合法字符 → 非同态解码形式化与流式/约束生成failure → 输出correctness边界。只读affected core，见第二小包。 | submitted Nov5；COLM2025不授首公开。潜在，日期隔离。 | 第一组及[PDF核心](./nov11-critical-stop.txt) |
| [2511.06086v1 MuonAll](https://arxiv.org/abs/2511.06086v1) | Muon/AdamW混合参数处理 → 所有参数reshape2D统一优化 → 小规模fine-tuning可比边界；不外推LLM大规模或吞吐。 | submitted Nov8 17:45:20Z；潜在，日期隔离。 | 第一组 |
| [2511.05743v1 In-Context Learning Without Copying](https://arxiv.org/abs/2511.05743v1) | 抽象ICL依赖copying/induction的假设 → Hapax去除copy-token loss而保留抽象任务能力 → 局部反证，不等于所有ICL无需induction。 | submitted Nov7 22:11:11Z；潜在，日期隔离。 | [第二组](./nov11-abstracts2.txt) |
| [2511.05759v1 Language Generation: Complexity Barriers and Implications for Learning](https://arxiv.org/abs/2511.05759v1) | 理论可学不代表可行样本量 → regular/context-free语言生成复杂度边界 → 需分清形式假设与现代LLM经验；不以无benchmark排除理论。 | submitted Nov7 23:06:48Z；潜在，日期隔离。 | [第二组完整补读](./nov11-abstracts2-details.txt) |
| [2511.05852v1 Quantifying Edits Decay in Fine-tuned LLMs](https://arxiv.org/abs/2511.05852v1) | 独立评价editing与fine-tuning忽略后续编辑存活 → 232配置与选择层更新局部反证。 | v2官方撤回声明已取得，作者顺序/状态/未发表记录错误；本历史v1链不采用、不评分；不外推当前活跃v4通篇无效。 | 第二组完整补读及[精确v2声明](./edit-v2.html) |
| [2511.05993v1 Revisiting Entropy in RL for Large Reasoning Models](https://arxiv.org/abs/2511.05993v1) | entropy随RL变化并非单一质量规律 → off-policy、diversity、clip及正负advantage贡献 → 重审梯度控制边界。 | submitted Nov8 12:50:41Z；潜在，日期隔离。 | 第二组完整补读 |
| [2511.05518v1 Retracing the Past: LLMs Emit Training Data When They Get Lost](https://arxiv.org/abs/2511.05518v1) | 启发式divergence不能稳定测泄露 → 持续高entropy优化+错配SFT增加提取 → white-box/可改权重与模板限定风险。 | submitted Oct27；EMNLP2025不授首公开。潜在，必要反侧已读，日期隔离。 | [第三组](./nov11-abstracts3.txt)、[威胁/评价](./nov11-critical-details.txt) |
| [2511.05784v1 DRAGON](https://arxiv.org/abs/2511.05784v1) | retain data/参数更新受限 → negative检测加动态CoT guard → 可提供推理前行为干预，但不证明参数遗忘。 | submitted Nov8 01:13:28Z；已指向ICML MUGen/NeurIPS，forum挑战/错误分号链接已有限恢复，不授日期。 | 第三组、[原核心](./nov11-critical-identity.txt)、[按需停点](./nov11-trigger-final.txt) |
| [2511.05933v1 Reinforcement Learning Improves Traversal of Hierarchical Knowledge in LLMs](https://arxiv.org/abs/2511.05933v1) | 参数知识存在不等于能取回 → 层级提示缩小SFT/RL模型差距 → 访问路径评价；医疗术语任务不使通用机制出范围，模型对比也不证明RL单因果。 | submitted Nov8 08:56:29Z；潜在，日期隔离。 | 第三组 |
| [2511.06073v1 Stemming Hallucination in Language Models Using a Licensing Oracle](https://arxiv.org/abs/2511.06073v1) | RAG不强制拒答 → 抽取triple、SHACL与graph membership licensing后commit → 可核precision/coverage差额；不能采纳必要充分/全事实正确保证。 | submitted Nov8；潜在局部条件，日期隔离；PDF正文身份已核，web索引错误题名只隔离索引，不否定PDF。 | 第三组、[身份/方法](./nov11-critical-identity.txt)、[限制](./nov11-source-final-details.txt) |
| [2511.05560v1 Sample-Efficient Language Modeling with Linear Attention and Lightweight Enhancements](https://arxiv.org/abs/2511.05560v1) | 小数据约束下mLSTM+局部window、Muon优化可改变质量/收敛取舍；不是只因组合名称准入，也不外推规模。 | submitted Nov4；潜在局部验证，日期隔离。 | [第四组](./nov11-abstracts4.txt) |
| [2511.05650v1 Optimizing Diversity and Quality through Base-Aligned Model Collaboration](https://arxiv.org/abs/2511.05650v1) | alignment损多样性 → 按uncertainty/semantic role token级base/aligned路由 → 单次生成quality/diversity差额，成本不能只按pass数。 | submitted Nov7 19:00:01Z；潜在，日期隔离。 | 第四组 |
| [2511.05722v1 OckBench](https://arxiv.org/abs/2511.05722v1) | 只看accuracy忽略reasoning token成本 → 同准确率token差异与Pareto → 局部评价盲区；token不是硬件无关latency/energy等价。 | submitted Nov7 21:29:41Z；潜在，日期隔离。 | 第四组 |
| [2511.06190v1 Confidence-Guided Stepwise Model Routing for Cost-Efficient Reasoning](https://arxiv.org/abs/2511.06190v1) | query级外部router受domain shift/标签成本限制 → 小模型step前logits置信度路由 → 重审粒度/成本，不能采用domain-agnostic普遍保证。 | submitted Nov9 02:33:08Z；潜在，日期隔离。 | [第五组](./nov11-abstracts5.txt) |
| [2511.06441v1 Towards Resource-Efficient Multimodal Intelligence: Learned Routing among Specialized Expert Models](https://arxiv.org/abs/2511.06441v1) | query分类及二阶段vision组合的局部routing成本/质量条件潜力保留；决定性方法/表已读，成本叙述与Table3/4冲突、similarity不是正确性，不能采用聚合性能保证。 | 小段已处理，submitted Nov9 16:14:56Z未作public；日期隔离，不扩全部实验。 | 第五组及[TAIL具体反侧](TAIL_SCREENING.md) |
| [2511.06516v1 You Had One Job: Per-Task Quantization Using LLMs' Hidden Representations](https://arxiv.org/abs/2511.06516v1) | task-agnostic PTQ忽略层分布 → task-conditioned hidden statistics与direct sensitivity分配bit → 任务专用精度/校准取舍；不将单任务保真当通用保证。 | submitted Nov9 19:58:24Z；潜在，日期隔离。 | 第五组 |

## 普通范围及最新收束

最新：下列20份完整v1题摘均已实际读，另4份定点补漏v1已读；逐项见[TAIL_SCREENING](TAIL_SCREENING.md)，06441决定性小段也已处理。下文保留发现/失败过程，不再作为20项未读队列。只余来源记录/正式报告及CAT原身份去重小段，独立校准另接。

原三窄query无有效Atom，不能授主题覆盖。native `skip325/show50`先项2511.07074 submitted Nov10；`skip250/show50`包含上述18题摘恢复方向，均不证明Sunday公告。为修正发现切片再取`skip200/show50`，仅标题查漏，不转50/1527条题摘队列。由模型形成、运行时与评价主题选出20个含糊相关身份：04654、04688、04689、04694、04700、04703、04715、04754、04800、04869、04875、04919、04952、05018、05064、05085、05162、05184、05408、05516（均2511）。一次明确v1 id_list原API25秒timeout、0bytes，没有落盘XML，未读完者仍普通待办；可逐exact-v1题摘恢复，不自动全文。

机构普通：CATransformers Nov11原完整摘要（[raw](./nov11-trigger-final.txt)）新增operational+embodied carbon联合model/hardware优化方向保留，日期未知时区；Teaching AI Nov11冻结teacher adapter→合成triplet→student全训练机制原核心/限制已读，ERNIE Thinking Nov11 GSPO/IcePop、difficulty sampling与image-tool核心已读（[raw](./nov11-source-final-details.txt)、[raw](./nov11-source-final.txt)），均潜在日期隔离，不用相交日精度先授本窗。Northern Ireland教师pilot是应用/使用反馈、没有新增模型/系统机制，范围关闭而非通用否认其评价价值。
