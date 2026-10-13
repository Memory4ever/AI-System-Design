# 后三项 Books 逐字 PRE（未授写锁）
三个唯一owner，已有段保留；只是正文草案，Source/差额/逐字PRE通过后向root取锁。候选与必要证据见 SUP_EVIDENCE_SEVEN。

## 14903 MODEL-KV-CACHE / Ch19
位置：Position 与 Cache的一致性，跨请求Prefix段后、Cache没有解决什么前。现有位置身份只给要求，补流式输入追加的可重训分支：
流式输入与输出交替追加时，保持已生成 token 的 position 不变还需要显式分配位置，而不能每来一段输入就把旧输出向后挤。一个可重训的分支预留固定长度的输入 slots，输出从这些 slots 之后开始；slots 用满时，在当前序列末尾分配下一块，训练 Attention mask 同时对齐部署时的 read/write policy，避免旧输出读取当时尚未到达的输入。这样位置与可见性一起构成 cache reuse contract，而不是只改 position id 就让任意已有 hidden state 可复用。[受限流式翻译对照](https://arxiv.org/html/2603.14903v1)支持这种分支，slot 长度与训练/推理 policy 失配会损失质量；算法延迟与 FLOPs 不等端到端吞吐或 SLO。预留空间、专门微调和 mask 管理都付费；不能重训、输入模式不匹配或质量回归时，保留普通因果追加、必要重计算或已验收的 encoder–decoder 分工，不静默改变通用模型的 cache 语义。<!-- source-family:SF-2026-ARXIV-2603-14903 -->

## 15159 TRAIN-SFT / Ch29
位置：已有Tool-use dependency-aware trace解释后，高质量demonstration检查前：
当目标是调用模型不熟悉的库时，检索到正确 API 文档只提供知识暴露，不保证模型会组合出可执行程序。可以从 API 规格生成初始示例，记录样本由哪些规格或既有样本合成的有向无环图，交替组合样本、改写任务，并用语法、执行与语义检查裁剪图，再把保留的调用行为作为 SFT demonstrations；图边记录生成来源，不是程序调用的执行依赖。它补的是调用策略，而不是让文档本身取得答案权威。图生成、执行与 teacher/judge 成本，以及错误过滤造成的选择偏差都应计入训练数据合同。[受限新公开库对照](https://arxiv.org/html/2603.15159v1)支持这条课程分支，却没有证明真实私有库无泄漏、所有 RAG 都被取代或通用代码能力不退化；可执行参考与独立 held-out 任务仍需保留。库状态不稳定、judge 不可靠或通用能力回归时，回退经人审的调用 demonstrations、文档检索与固定测试，而不由训练 pass rate 认证接口掌握。<!-- source-family:SF-2026-ARXIV-2603-15159 -->

## 15417 TRAIN-GRPO / Ch33
位置：Verifier Error组内相关/错误动力学完整段后，Verifier也成为Policy标题前：
没有外部标签的 test-time 更新还会把答案格式当作 reward 的准入门：按最终答案多数一致性给组内奖励，可以提高对共同结尾的偏好，却不核验完整回答的行为。只接收数字答案看似隔离了数学任务，但有害指令与数字子题放在同一 prompt 中时，数值部分仍能通过 parser，其他内容也被同一更新改变。[受限 TTRL 反证](https://arxiv.org/html/2603.15417v1)中，普通混合提示的过滤效果不能迁到这种组合提示，math-only 与不同初始安全状态的结果也并非一律恶化。由此得到的是工程约束而非论文证明的安全算法：格式门、完整 prompt/response 的安全准入和独立行为回归应分别验收，不能让 consensus 自证 correctness 或 safety；额外判分、训练与回归预算仍要支付。安全身份未校准、出现回归或信号失真时，应停止更新、回退原 checkpoint 或使用可信外部 verifier，而不是继续按可解析答案优化。<!-- source-family:SF-2026-ARXIV-2603-15417 -->

