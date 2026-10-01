# 2604.25634v1 输出秩频“指纹”反向准入

范围仅限 [官方 exact-v1](https://arxiv.org/html/2604.25634v1) §3.1–3.3、§4.5、§5.1–5.6、§6 与实际 [Ch66 Evaluation](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 Evaluation Identity、EvalSpec 和「从 Raw Score 到可定位、可校准的 Claim Sensor」。这是作者侧具名处置，不是独立复核、首公开日期证明或整日 Gate。

## 原恢复入口与实证

原[题摘反查](./V3_REVERSE_TITLE_ABSTRACT_BATCH2.md)把“模型间 Mandelbrot 参数差异可能提供廉价黑盒替换监测”恢复为潜在候选，待查 prompt、长度、温度和统计阈值。论文确测六模型、五域、每模型约 77k–236k 输出 token；同一批 100 prompts/model 用共同 Llama 3.1 BPE 重分词，36 组拟合中 34 组 log-log `R²>0.94`、35 组 AIC 偏向 Mandelbrot。全域汇总 `q=1.63–3.69`，各模型 bootstrap SD 常为 `0.03–0.10`。这是受限输出分布规律，不应否认。

但同文 §3.2 Fig.1/4 明说**同一模型跨域位移大于固定域跨模型位移**；§3.1 的输出长度差异明显，温度虽定为 0.7，其余 top-p、top-k、seed、重复惩罚仍用 provider default。§6 还明确未测 native-tokenizer 不变性，§4.9 自承完整 fingerprint operating-characteristic study 仍属未来工作。bootstrap SD 是该采样协议下拟合参数不确定性，不是未知流量、不同解码或对抗替换的误报/漏报率。故不能把参数分离写成单回复身份认证、加密 provenance、部署门槛或 vendor 静默替换检测已被验证。

论文称中心**已验证**的其实是 §5 的廉价 scoring primitive：全局 rank 表叠加可选 logprob，在 FRANK、TruthfulQA、HaluEval 对词法/实体异常有有限信号，无法判领域词汇正常的推理和事实错误。FRANK 主协议 span AUC `0.585`，TruthfulQA 多选 `61.4→63.8%`；HaluEval QA 单独由长度即可达到 AUC `0.965`。统一内部 Table 3 不等同主协议：FRANK rank-only `0.559`、HaluEval QA `0.457`，而更具体的 FRANK 实体实验中，最简单的全局稀有度在 relaxed named-entity 标签上 `0.622`、完整 strict 标签上仅约 `0.374`。§5.2.3 的域匹配 `β` 在 FRANK 从 `0.557` **降至** `0.529`。CPU 计时 `0.139ms/pass` 要预供实体，带 NER 为 `10.5ms/pass`；相对采样检测器的约 `100,000×` 来自异硬件/已发表配置估算，非匹配端到端对照。FRANK 10% 路由是单基准初步观察，不是部署风险/质量保证。

## 与实际 owner 的准入判断

Ch66 已将 `request/model/prompt/decoding/evaluator` 绑定为 Evaluation Identity，EvalSpec 保存目标错误、切片、阈值与风险要求；「Claim Sensor」已有 typed span→模型或外部 sensor→部署切片校准→检索/弃答/人工复核的分责，且明确 sensor 不是真值概率。本文所测 rank-only/词法稀有度可作这一既有低成本传感器的一个实现点，贡献在受限 benchmark 的成本—弱效果取舍；没有证明新的身份认证 Gate，也未隔离出需要改变现有 calibration/escalation 合同的边界。论文自己划分的词法异常可观测、普通词汇推理错误不可观测，亦被现有 semantic success 与 evidence authority 分账覆盖。

因此作者侧将原“待证实模型替换监测”从**潜在线索**改为**具名前分母关闭**：不评分、不列 Report candidate、不写 Books；不是以小模型、局部任务或负结果硬拒，而是原拟改变 Ch66 选择的身份机制没有 operating-characteristic 验收，实际受限评分器仍是已有 sensor+calibration 决策的参数化实例。保留上述实证与反证供非作者逆向抽核；如未来在冻结 prompt/domain/decoding/输出长度与 native tokenizer 下给出身份判别 ROC、误报率/漂移阈值及生产替换对照，可重新开准入。

工作账影响：本篇属于新 106 题摘中的非旧 60 项；原 `64 potential + 41 contribution-preclosed + 1 early-public date-isolate`，作者拟更新为 `63 + 42 + 1 = 106`。旧 60 分账不变。因贡献侧明确前闭，按合同不为排除项继续追完整首公开史；来源窗口覆盖独立核，不以此条代签日期或整日 Gate。
