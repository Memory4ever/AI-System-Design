# 三项完整 Books PRE 提案

仅以下精确新增段、独立marker与本人末注。未写Books；请sole reader以实际当前磁盘完整邻接核整体PRE。无全章锁，不申请root第三技术批准；若精确共享gap冲突再上报。必要证据见REPAIR_EVIDENCE；R7已核三者key，现请求真实owner差额校准。

## B1 15152 / Ch45

位置：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`，Eviction 与 Offload中“少增加未来重算时间”段之后、“比较成本时还要说明重建的起点”之前。已完整读375–415邻接及Ch46开篇。差额是显式TEL阈值下的safe budget，而非已有重算成本加权。

完整新增正文：

若目标是控制慢请求，最小化平均重算时间又未必等于最小化阈值以上的损失。可定义尾部超额 `TEL=sum max(TTFT-xi,0)`，在单层缓存、TTFT近似随未缓存块线性增长的模型内，只保留足以让下一轮落到阈值内的会话前缀，再将其余容量按LRU竞争。[受限T-LRU分支](https://arxiv.org/html/2510.15152v1#S4)以历史长度、下一prompt长度估计与阈值确定预算，不删除逻辑历史，也不改变KV复用身份；下一prompt未知、共享前缀与真实batch干扰都会使模型失配。其最优性另依会话birth/death、Poisson到达与已知长度分布，不能扩成任意trace或percentile最优；阈值过高已有平均时延或较低SLO违规反退。预测、选参、bookkeeping、重算及并发回归均计费；目标与到达规律未校准时，保留普通LRU、成本加权与offload，不由较低TEL批准所有尾分位或生产SLO改善。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15152 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15152` — Daily2025-10-21补Oct20；exact-v1§3–6必要主体，2+2+2=6。只采用TEL阈值预算/trim再LRU、预测与目标错配边界，不采用全部proof、任意trace最优或宣传倍率；单A100/Vicuna7B/TP1/no mixed batching与xi过高反侧限制外推。HTML300964/532385 bytes partial，必要主文已到，不冒完整附录。未核实现/复现。

## B2 15231 / Ch23

位置：`books/part-03-multimodal-world-models/23-multimodal-representation.md`，NAACA段独立marker之后、“选好声学窗口之后”之前。已完整读85–145相关两侧与Ch24开篇；Ch22拥有一般长上下文，不在此复述通用YaRN。

完整新增正文：

保留更长音频还受语言consumer见过的模态位置范围限制，不只取决于声学encoder能处理多少秒。对audio/text共享输入空间的模型，可只在音频区域伸缩RoPE位置、保留文字坐标，并在训练时随机映射虚拟音频长度，使同一真实片段覆盖不同位置跨度。[Partial YaRN/VLAT的受限对照](https://arxiv.org/html/2510.15231v1#S3)没有增加真实声学信息，文字位置不变也不保证跨模态attention或语言能力无损；应先测原模型实际可用时长，再选择伸缩锚点，而不把标称30秒直接当硬边界。Whole与Partial方案在不同模型/长度上互有反退，MCQA也不足以证明开放生成保持；位置增广与真实长内容训练不能混成同预算比较。分块编码、超参搜索、LoRA训练及长音频/原文字任务回归都计费；位置、内容覆盖或质量不合时，保留原短窗口、显式分段和已验证的whole-context路径，不由扩展坐标签发任意长音频理解或净加速。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15231 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15231` — Daily2025-10-21补Oct20；exact-v1§3–7/Limitations，2+1+2=5。只采用audio-only位置映射与虚拟长度增广、实际2min锚点和Whole/Partial并存边界；保MCQA/Gemini制题、视频级split、1epoch与10epoch训练预算分责，不采文字无损或完整runtime加速。原件完整，未核代码/复现。

## B3 15339 / Ch76

位置：`books/part-07-agent/76-rag.md`，Multimodal Memory Graph两段及原独立marker之后、“Checker Reward”标题之前。已读1748–1782完整直接两侧与Ch77开篇。已有builder proposal/structural credit与checker独立性不覆盖carrier/index不同reward目标如何训练constructor。

完整新增正文：

图构建器也可以消费下游效用反馈，而不只优化抽取的局部精度。先冻结retriever与answer generator，再区分图是直接提供事实的knowledge carrier，还是指向原文的knowledge index：前者可按gold answer能否由检索子图推得给奖励，后者按gold supporting passages的检索覆盖给奖励。[AutoGraph-R1的受限分支](https://arxiv.org/html/2510.15339v1#S4)据此训练constructor，而非只训练图上搜索；consumer、gold/干扰文档人口、judge和reward必须绑定构图版本，换retriever不能沿用原效用资格。Judge可推得不等事实真实，召回提高也不等生成正确，局部对照仍有QA与抽取精度反退。标注/奖励调用、RL、重建索引和独立证据回归都计费；来源支持、质量或总预算失配时，保留原抽取器/索引、flat retrieval与原文核验，不让高reward自动授予图节点事实权威。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15339 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15339` — Daily2025-10-21补Oct20；exact-v1§3–5/6–7，2+1+2=5。采用冻结consumer下carrier/index目标分流训练constructor；保两种训练人口不同、Llama1B-ToG NQ和Llama3B-HippoRAG2 Musique反退、DeepseekV3评估非独立真值。twoH100/Qwen与Llama作者实验，不采全局事实无损/普效或SLO；HTML289939/454380 bytes partial，必要主体完整，不冒全附录。未核实现/复现。
