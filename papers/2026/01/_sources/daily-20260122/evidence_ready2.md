# 已准备必要证据（二）

这些条目实际原文段落见[review_core_batch1](./review_core_batch1.txt)及[decisive_core1](./decisive_core1.txt)、[decisive_core2](./decisive_core2.txt)。只采窄命题；尚未处理Books比较或独立复核不写最终完成。

## R²PO — 2601.11960v1

精确v1[原文](https://arxiv.org/html/2601.11960v1) §3、§4及Limitations。共享backbone与LM head，新增两层MLP residual-vocabulary-logit RO head，零初始化。第一阶段冻结backbone，仅更新explorer head；GIF对相同reward数值分箱计数的逆频率再z-score，不能解释为语义新颖奖励。第二阶段冻结RO head、更新backbone及LM head，使用explorer采样轨迹与task correctness/format奖励。固定head不等于固定整个behavior policy，共享backbone变化会改变explorer；公式标准GRPO分母为旧base policy，未在采用段明确对explorer behavior作重要性校正，不采用“无偏offpolicy”或普遍防干扰保证。

Qwen2.5-3B/Qwen3-8B训练GSM8K/MBPP，评MATH500/HumanEval/APPS等；OpenCompass Pass@1与custom MATH格式兼容评分。3B GRPO→R²PO：MATH42.2→45.6而HumanEval68.9同分；8B GSM88.55→88.48略降，MATH54.4→57.2。3B GSM消融GRPO80.74、无RO分阶段82.18、GIF83.17、mainreward83.55：结构分支可提供收益，GIF不是已证必需或最优。新增head约315M参数（3B的10.2%；8B约7.8%），训练成本并非零；推理detach head只支持结构上不增加此head，不等runtime零开销实验。精确training walltime、RL batch、hardware/precision和统计重复在本次必要段Not Disclosed；不采用格式扰动“免疫”的含糊百分比。

2+2+2=6；标准必要段已读。暂拟仅报告：具体reward bins和交替分支配方还不足替代一般探索/优化策略，单轮3/8B局部结果不改长期优化原则；若后续owner具体冲突成立才重开，不为缺论文名称改书。

## Compression-Aware Attack — 2601.12042v1

精确v1[原文](https://arxiv.org/html/2601.12042v1) §3、§4.2、§5.1/5.3及AppF.3，安全影响命题已深入定点。POPE随机子集控制压缩layer2、retention1～.1与ℓ∞噪声16/255、32/255；相同扰动图像改用clean-ranking oracle恢复效果，把ranking instability与纯语义图像破坏分离。Top100 preservation/bottom100 infiltration和rank correlation支持token排序变化。攻击最大化compressed-output偏离并惩罚uncompressed-output偏离，白盒需完整weights/gradients/compressor；黑盒机制与query预算未在采用段核完，不外推。

采用LLaVA/LLaVA-Next/Qwen2.5-VL、POPE/MME/TextVQA等作者配置，FastV layer2/retention.2、eps32/255主控制，retention.1～.5及跨层/retention mismatch实验有边界。无BPR时CAE .6691→.1715、CSG−.4482；least-important-only vs全扰动保留差异，most-important-only可能直接损伤语义，不同攻击机制不能仅按ASR混合。高retention可保clean额外信息稀释攻击；Qwen Hiera/Erasure/Query消融降低CSG。hardware/precision、端到端query成本Not Disclosed，不采用56.6%headline作为所有配置保证。

具体窄命题：干净图像上的token排序可能对小幅扰动不稳定，离散删选会放大该差额；oracle排序控制是重要归因证据。不是全部压缩不安全、黑盒普遍成功或零utility-cost攻击。2+2+2=6且安全命题深入；Books待比较实际owner是否已有排序鲁棒性/不可逆commit的具体论点，不从安全标签自动整合。

## MemoryRewardBench — 2601.11969v1

精确v1[原文](https://arxiv.org/html/2601.11969v1) §4.1、§5.2/5.3、AppC.2。13个LLM proxy reward evaluators，3个官方API（Claude Opus4.5/Gemini3Pro/Qwen3Max）及10个≥128K opens；invalid parse算incorrect，低于50%不直接等于偏好判断反向。关键对照不是“所有memory RM失败”：outcome一对一错与process两答案都正确但过程质量不同分开，chosen/rejected交换输入位置再次判断。process更偏第一位置而outcome相对稳定，支持过程偏好与顺序一致性须分开测。主评价随机化顺序，不构成全局模型失败证明。

上下文8～128K、约束密度扫点，部分64/128K长ctx失败与参数规模不能作直接因果；采用段无精确Fig4点值故不补造百分比。temperature .7、top_p .95、maxgen16384，开源用LOOM-Scope、商业用官方API；hardware/precision/时延Not Disclosed。没有运行或复现。2+2+2=6；标准必要证据已读。暂拟仅报告此受限过程偏好评价协议，Books若已有judge顺序/内容分离原则，需实际指出具体覆盖而非owner名称。

## 四项最小核心决定准入（尚待校准）

- [PPA11908v1](https://arxiv.org/html/2601.11908v1)：§3与§4.3控制更强planner未必更可执行，GPT移除syntactic corrector有效format74.3%，原baseline79.7%，完整93.3%；弱/强模型交互不同。全文实验GPT4o-mini、Llama3.1-8B、Qwen2.5-14B 8bit，QuALITY/ConditionalQA/LongReason/Qasper；表1仅各方法成功交集存在selection bias，表2全测试集另看。计划步数增长同时改变pitfall与reasoning两组件，不能独立归因或匹配预算。建议准入实际repair依赖的局部反侧，不准入negative-constraint名称本身。
- [PICL11979v1](https://arxiv.org/html/2601.11979v1)：§3和Tables1/2、§5.3/5.4；“wait/maybe”interrupt词表是经验代理，不是算法计算entropy阈值。每个interrupt先reflection提confusion，非空才插demo，semantic retrieval后BGEM3按confusion rerank；k1/r1控制。Qwen-R1distill7B、Llama-R1distill8B，4mathbench；Qwen zero77.7/staticBGEM377.6/PICL83，Llama67.8/65.8/72.7。Stage1去除时每次直接插、stage2去除时confused插随机，必要局部控制支持时机和内容共同影响，反侧是static ICL可伤reasoning-distilled模型；额外reflection/rerank成本未匹配，不称同预算胜出。建议准入该具体反侧。
- [DoubleCalibration11956v1](https://arxiv.org/html/2601.11956v1)：§4.1/4.2与§5.4；Beta(.5,.5) posterior mean依均匀grounded answer candidates和gold标签，原文称MAP但公式是mean，不是任意KG边truth校准。SFT path+confidence；RL对gold路径的结构match、goldF1、Bayesian confidence作alignment。SingleCal去confidence保quality，F1差±1而ECE约4→>20，实际新增是confidence provenance可独立于retrieval quality影响校准。尚需表2/设置必要核，不能只说双层confidence。
- [PREGU12040v1](https://arxiv.org/html/2601.12040v1)：§3、§4设置与§5；SoftReasoning优化first token embedding，PREGU在5条prefix路径首次高entropy(top50，τ3bits且minimum length)处重新设latent optimization root，每path最多一次，BO 5samples/project50dim。Llama3-8B/Mistral7B/Qwen2-7B、5runs mean±std，baseline引用既有SoftReasoning论文，未同budget重跑；部分模型数据集回退。具体分支是internal prefix-root latent refine而非只入口softreasoning，不采用节省runtime或entropy=自知困惑保证。奖励函数必要定义仍待定点核。
