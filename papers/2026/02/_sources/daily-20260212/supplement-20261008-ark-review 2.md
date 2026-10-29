# 2602.09839v1 必要审阅（作者准备，Source待独立）

[ARK](https://arxiv.org/html/2602.09839v1)，root完整AB准入/Feb11包络已核，评分2+2+2=6。只采用多模态检索诊断设计，不采用科学域能力结论，AIforScience暂缓不借此引入。

§3.1–3.3 L119–144/193–205：一query一positive、同主题/视觉相似但违背关系的定向hardnegative，把知识域与reasoning需求分开标注；LLM改写移除trivial cues→web mine→人工选择→Seed1.6 top50筛歧义/近重复迭代。改变的是不能把semantic overlap高分当关系满足，非数学orthogonal因素独立/模型内部真实reasoning已验证。没有同query有无hardnegative的受控对照，不能将模型整体低分唯一归因reasoning；同一evaluation模型辅助筛选也不是独立无偏真值。

评价§4 L208–237/Table2–3：1547query/36030gallery总库不是每query全库检索；每subtype专属corpus、macroaverage各子类，库规模从280至7500不同，不能以同rank metric授等难度。知识/推理axis多人为标签，多技能重叠，未测完全析因或因果分离。textonly需Qwen3VL8B caption，丢细粒度/空间线索既是pipeline边界也是非同input对照；模型参数增加未控制训练数据/recipe，不授scale必然失败。spatial/细粒度低分为本fixture作者观察而非普遍感知缺陷。

不采用未读AppD Tab8/9数值或cost来证明queryrewrite/rerank提速/系统ROI。只保留正文明确多GPT5.2 rewrite/Top50pairwise额外推理；runtime/hardware/precision/batch/SLO/重复CI Not Disclosed。top50 screening覆盖不是真实全部gallery多positive已排除，假negative风险边界保留。支持协议盲区的必要核心/评价/反侧足，停止无关图表/全benchmark各科目。

Source后owner拟AGENT-RAG的multimodal检索质量、hardnegative/evidence完整性；同主题不授已有覆盖，尚待actual owner对比。
