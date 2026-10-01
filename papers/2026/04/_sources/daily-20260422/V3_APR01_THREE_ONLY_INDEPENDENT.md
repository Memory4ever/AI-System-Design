# Apr22 三项标准仅报告的有限非作者复核

复核者 apr01；实际重新读取当前 AGENTS、统一入口、研究/Report 合同、Daily 来源与 ROADMAP。仅核 18728/19089/19105 准备采用的机制、关键评价及真实 owner 比较；不验收本日日期、全部来源或日级 Gate，不写 Books，未复现实验。三项均支持 `2+1+2=5 / 标准完成 / 仅报告` 的受限处置，不把局部公式疑点扩成整家族不可用。

## 2604.18728v1 — The Cost of Relaxation

[官方 HTML-v1](https://arxiv.org/html/2604.18728v1)实际读取 §3.2–3.3/Eq4–8、§4.1/Eq14–15、§5.1 与评价配置。可行集过近似会接受原模型不可达输出，但不等于保守的无反例证明失效。§5.1 是30个随机 ReLU 网络；半径 .025 的包络与从 [-1,1] 采样的输入不应称同一域证书。元素绝对值条件不排除抵消，不能采用“所有网络误差必指数增长”。Ryzen5500U/TF2.4.1 仅为本实验配置，非 LLM 性能或安全结论。

实际对读 Ch72「单条 Trace 无法证明跨执行安全性质」中 monitor/reference/mechanical check 分工，以及 Ch66 EvalSpec 的 eligible population/slice/scorer 责任。这里足以承担报告应保留的一般边界，但没有声称已写本论文的整个凸松弛理论。有限测量与方法解释留报告；不据本篇升级正式安全证书或新增普遍增长定理。**窄处置通过。**

## 2604.19089v1 — LightEdit

[官方 HTML-v1](https://arxiv.org/html/2604.19089v1)实际读取 §4.1–4.2/Eq8–10、§5.1 与 Tables3/5/6；冻结模型、外部事实和 NLI selector 后仅首 token 干预，收益不能解释为删除参数知识。印刷 prior 是标量，归一化扣同一常数会抵消。

为该歧义定点实际读取[作者固定 commit 代码](https://github.com/ekgus9/LightEdit/blob/f1031749a727173262ec440b6f934addf3c4bdc9/editors/lightedit/lightedit.py)：`prefill_hook` 对完整词表 log-softmax 向量求平均，processor 只首步逐 token 扣向量，确非共同常数。当前 artifact 可解释执行对象，不证明 April artifact 身份或实验复现。Llama3.1-8B/GPT-J6B、1000 selector 监督样本/A100、k5/α.2 的局部对照保留；Table6 全 token 分支退步，外部检索与维护非免费。

实际读取 Ch20 softmax 段「减同一常数不改变概率」和 Ch29 Context Distillation 的 prompt 可逆、参数迁移及成本交接。该首步配方不是全部已有覆盖，但尚不改变这些长期选择；仅报告算法与公式/实现区别，不采用一般概率保证。**窄处置通过。**

## 2604.19105v1 — EgoMotion

[官方 HTML-v1](https://arxiv.org/html/2604.19105v1)实际读取 III-A/B、IV-B/D、TablesII–III：motion-token 监督适配 VLM，再冻结梯度训练生成器。Joint-Tuning 语义对齐更高、fidelity 更差，是局部取舍，不是独立测得梯度冲突。两阶段总成本与只训生成器不同；140K 五秒片段、23关节/150帧/batch256 的动作序列评价，不是物理 controller 成功或生产 SLO。硬件/精度未披露，不采用全面范式排序。

实际读取 Ch26「Action-facing Representation 也是 Gradient Authority Boundary」及 mediator 的成本/适用条件：现有正文明确 joint action loss 可改写语义表示，以及固定/分阶段接口与 direct fusion 的共存边界。它不承载所有 RVQ 算法，但足以承载本次可长期采用的通用判断；新受限对照保留报告，无须按论文名追加书稿。**窄处置通过。**

三项采用范围外的强理论/安全或部署声明均未被此复核授权；日期、来源和整日报告仍由作者与日级独立复核者收口。
