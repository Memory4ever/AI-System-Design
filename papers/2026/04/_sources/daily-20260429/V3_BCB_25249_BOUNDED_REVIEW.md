# 2604.25249v1 Below-Chance Blindness：有界证据与 owner 对读

本项为 04/29 作者侧必要审阅，非独立 Gate。来源为 [官方 exact-v1 HTML](https://arxiv.org/html/2604.25249v1) §1.1–1.2、§2–4；它已在 [第三批准入反查](./V3_REVERSE_TITLE_ABSTRACT_BATCH3.md) 从旧题摘的“小模型／局部 benchmark”误拒恢复为潜在线索，**不再改变**当前 `106＝69 潜在＋37 具名前闭` 工作账。首公开归属仍须与本日 arXiv 官方公告窄批链核实，论文首页的 04/28 日期不是带时区时刻。

## 受支持的负证据

预注册的 H1 是 3 模型×4 MMLU-Pro 领域中至少 3/12 个 cell 在“deliberately underperform”指令下显著低于 10 选项随机率 0.10。§2.1–2.5 固定每领域 500 个题目、同题跨条件、四种 prompt 条件、共 24,000 trials；三模型为 Qwen2.5-7B、Llama3-8B 与实际上 3.8B 的 Phi3.5-mini，均 Q5_K_M、单卡 Vulkan、greedy 解码、只需输出 A–J。§3.1 的 **0/12**（最低 0.156）说明这个明确合作式指令、这些模型和题型中，below-chance gate 未触发；§3.2 B 相对诚实 A 的 cell 平均准确率低 0.062，又说明未触发不等于“没有行为变化”。§3.3 A/D 的零 cell 是预注册 null 检查，不是所有对抗设置的结论。

§3.5 的 C3 “选最不可能正确项”使 Qwen 与 Phi 的部分领域低于随机，例如 Qwen Economics 0.024；这是**探索性**拆分，不是预注册 H1 的成功，也不证明模型主动读取正确答案后有意规避。§3.6–3.7 的 Llama B 答案 E/F 分布为 31.8%/26.1%，标准化 entropy 0.977→0.793；当 Physics 正确答案恰位 E 时表现相对 A 高 32.7 个百分点，位 A 时低 22.7 个百分点。它支持受测响应的选项位置相关性，不能以 fixed option order 识别唯一内部策略。作者 §4.4 明说没有对同一题随机重排选项，无法把位置启发式与数据集 distractor 结构干净分离；还有限于显式合作 prompt、小模型、greedy、探索性分析。论文 §1.1 也承认低于随机可由 instruction anti-correlation、选项结构或 decoding artifact 产生，不能单独等同“模型知道正确答案且故意躲开”。

## 项目判断

准入成立的是受限 **EvalSpec 负证据**：在需要发现隐藏/压低能力时，单一 below-chance 命中是低敏感度传感器，未命中不能证明能力没有被压低；异常准确率又需和选项位置、指令遵从、候选重排及真实输出共同解释。拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5/9`，标准审阅。不能把这篇当成熟 sandbagging 检测器，也不据 24,000 trials 推广 frontier 或自然情境。

真实长期 owner 为 [ROADMAP 的 PLATFORM-EVALUATION-SYSTEM／Ch66](../../../../../ROADMAP.md)：[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 “Observed Capability 与 Elicitation Ceiling 必须分开” 已要求把观察分数、诱发能力与 evaluator 上限分账；“多选评测还会受到候选顺序与推理接口的共同影响”已要求冻结 permutation 并同时报告 accuracy 与 Position Bias。两条具体论点足以承载本篇**有限失败示例**，没有新的 release authority 或可验证检测保证需要 Books 增写。作者侧拟 `已有覆盖`（非完整论文或 C3 算法已存在）；待非作者核必要 §2–4 与上述两处实际命题，再定正式日报。当前不得记日级 Gate Complete。
