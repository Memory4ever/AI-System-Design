# 04/24 有界非作者复核 — 21327/21330/21335/21343

复核者：apr02（不是该日报或拟 Books 正文作者）。本次实际重读当前 AGENTS、研究/报告合同与来源范围，读取作者必要记录、literal，以及以下 exact-v1 方法、决定性评价/反证和实际 owner 邻接。仅此四项；不验日期/来源全日、不复现实验、不签日级 Gate，也不将写前采用通过记为实际整合。

## 2604.21327：6 分纠错深入，窄争议处置通过

实际依据：[官方 v1](https://arxiv.org/html/2604.21327v1) §3.1 Eq5–6、§3.2 Eq7、§4.4。K⁺≤K/2 且正负 advantage 为 ±1，所以每个 prompt 的 rollout 等权均值为 (2K⁺−K)/K≤0；正权跨 prompt 聚合仍不可能转正。§4.4 的正均值描述需要另一个日志分母、token 权重或实现差异才能成立。隔离的是该中心解释，不是否定固定幅度去掉 std 放大或全部数学任务实验；伪多数错误、负例分布改动及额外 M128 重采样成本继续保留。明确的日志/代码定义或勘误是定点重开条件。

## 2604.21330：6 分缺口深入，source→owner/literal 窄采用通过，未写

实际依据：[官方 v1](https://arxiv.org/html/2604.21330v1) §3/Eq6–9/Algorithm1、§4.2 Table3、§5.2–5.4 Tables5–7、J.4。冻结的是 dense feature backbone，辅助 teacher router 继续在 load/entropy 下更新；student 接收停止梯度的 assignment KL 目标，teacher 的均衡 proxy 不成为语义 oracle。实际读 Ch21 负载辅助代理及 quality-teacher 未来策略段（约230–245）和离线激活路径 contribution-prior 段；现文未承载外部 dense feature 空间形成联合训练 assignment proxy 这一具体职责分支。作者两段 literal 可嵌当前分权链。

早半程指导的受限 Table5 优势、末层 teacher features 低于基线、只模仿在 Table6 下降均已核，不能解释成通用指导规则。teacher 在线配置是不同 privileged 推理路径而非部署收益；J.4 的 epoch 增量和参数计数排除 teacher 也不能称零资产成本。保留原 Top-k/task 训练、较短指导及已验收负载约束共存；未核 LLM 任意 token 部署吞吐。此 PASS 不是写锁或 I。

## 2604.21335：6 分标准仅报告，受限处置通过

实际依据：[官方 v1](https://arxiv.org/html/2604.21335v1) §3.1–3.3/Eq8–13、A.2、C.6 Table14。保留完整 K，V-group 恢复与 context-token/group Top-M 后未保 V 置零是不同分支；末16 query tokens 完整保留。context split 隐状态只能预测 diagnostic query-attention 目标，不能据名字当作已读取未来 query。TotalKV=(1+ρV)/2 与单 V 保留率不同。实际对读 Ch45 可重建状态与 attention-distortion 责任，通用验收原则存在，但不称本算法全被覆盖；仅报告这一局部 operating point 合理。

单 H100NVL、batch1/~400-token forward 与 warmup 排除限制保留；C.6 32B 的111.4→112.7/114、72B 的233.2→234.5/236.4 说明非所有 latency 配置改善。不推出 packed 动态执行、cache 跨新 query 无条件复用或完整 Serving SLO。

## 2604.21343：6 分缺口深入，source→owner/literal 窄采用通过，未写

实际依据：[官方 v1](https://arxiv.org/html/2604.21343v1) §3.1–3.3/Eq4–12、§4.1–4.6/Table1。实际读 Ch23 完整 patch teacher 监督→latent 检索相邻段（约464–476）。既有分支是在视觉预训练输入被 mask 而对完整 patch support 监督；本项是 projector 后的语言空间腐化，由 LMM 中间层训练期 decoder 在腐化位置恢复 clean teacher features，再作 row-wise 相似结构 KL、同图 patch contrast 与语言 loss。恢复责任跨到语言内部而非重复同一 encoder recipe，最窄两段 literal 有真实增量。

clean teacher 是表示目标不是视觉事实真值；causal mask 不许借未来视觉位置。训练辅助头撤掉仅证明架构推理路径无此头，不使训练成本免费。实际 Table1 MME 的 CLIP 与 Qwen 下降、CLIP SQA 小退步均保留，训练 latent 腐化与测试 pixel 扰动不同；CKA/kNN 不是独立唯一归因。腐化比例、saliency、监督层位与 clean/污染切片分别验收，普通答案监督和已有 patch 对齐仍合理。本 PASS 不代表已写 Books。

## 收束

四项采用/处置必要范围通过；两真实 gap 仍是未授权、未实际写入提案。未复核整日初筛集合、公开日期组合、机构覆盖或全部附件。
