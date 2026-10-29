# 三个已过 Source 的唯一 owner 窄 PRE

root 实际 Source：00161/00209各6、00228为5；日期分别现27/EXTRA3 owned上下界记录。当前Books公共上下文、目标精确锚与完整局部论证、相邻章节交接已读。仅申请下列各两段+本人静态注；未授锁不写，其它同文件family不变。

## 00161：MULTIMODAL-REPRESENTATION / Ch23

文件 `books/part-03-multimodal-world-models/23-multimodal-representation.md`，Shared self-attention开篇之后。现计算图/packing与channel patch mask均有；差额是query-conditioned **辅助grounding读出**在answer前的可用性，不是decoder消费mask的顺序。

完整左锚：

> 所有 tokens 进入同一 self-attention graph。计算接口最统一，但必须明确 attention mask、position system、modality type、packing boundary 和 loss mask。没有这些元数据，同一个 sequence 中的相邻 token 可能只是打包邻居，而非语义邻居。

右锚为现完整“同一个 compact token index 未必还代表同一空间位置…”段，保channel独立mask/assignment全段。之间拟两段：

共享图中的辅助空间监督，还要声明读出时看到了哪些语言状态。若 query-conditioned segmentation head 只读取 image 与问题的 hidden state、排除答案位置，就能在标准 causal AR 结构中于回答前计算mask；这避免用答案状态构造一个部署前不可得的“依据”。但联合mask和next-token loss只是在训练中约束共享表示，mask没有作为decoder的显式输入，因此不能把它描述成每次“先取得mask、再据mask回答”的硬执行链，也不能由可读空间输出认证答案因果使用了它。<!-- source-family:SF-2026-ARXIV-2604-00161 -->

[有限联合grounding对照](https://arxiv.org/html/2604.00161v1)显示同数据/阶段下部分文字图任务提高而OCRBench略退，实例grounding的recall增加也可伴F1下降；区域到文字exact-match与文字到区域IoU匹配仍是不同验收，unsupported计零还包含接口失败。辅助head、标签、共享训练和空间读出都有费用，局部latency比例不授完整SLO。mask不准、共享训练伤原任务或预算失配时，保留原NTP、独立空间读出或显式回读原图的grounding分支；辅助监督不取得证据或action的放行权限。<!-- source-family:SF-2026-ARXIV-2604-00161 -->

本人静态注末一条：`SF-2026-ARXIV-2604-00161` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00161v1)§3.1–3.4/4.1/5.1/5.3，2+2+2=6，仅image/query-only辅助mask与decoder-input分责；保shared训练、OCR/precision-recall反侧、标签/人口/全部费用，不授truth或先mask后answer执行配方，未核实现/复现。

## 00209：PLATFORM-SECURITY / Ch72

文件 `books/part-06-ai-infrastructure/72-security.md`，视觉CI正负配对完整两段之后，Multi-Agent传播防御之前。现规范问答/真实attachment权限已分开；差额是单轴方向组合的局部反退，不能由可读规范表示授实际隐私保护。

完整左锚：

> 配对构造增加场景生成、规范审校和 trace 判断成本，也会继承合成语境、文化假设与 generator/judge 同源偏差。原研究的人审只覆盖50个场景，部分公式分母与正文、表格与叙述存在数值冲突，因此不采用精确总体泄漏率；它仍支持局部反侧：抑制披露的提示可能同时损害合法传输，CI prompt 不是生产保证。真实接收者或用途无法核实、规范判断不稳时，应由独立权限与 attachment gate 控制释放，保留人工审批或不发送路径，而非让模型以流畅解释代替授权。

右锚 `### Multi-Agent 防御要在消息传播前模拟状态偏移`，现整节不改。之间拟两段：

规范表示可读，也不证明按一个“privacy方向”修改hidden就会减少披露。一个受限干预分支分别从信息类型、接收者和传输原则的contrastive样本提取方向，再组合注入指定层；单轴在某些场景反而增加泄漏，三轴组合才改善所测行为，继续扩成五轴又未必更好。因此concept probe、组合方向的行为结果与真正的信息流授权是三种对象，不能用内部方向相加替代recipient/purpose权限检查。<!-- source-family:SF-2026-ARXIV-2604-00209 -->

[四种7B/8B模型的有限对照](https://arxiv.org/html/2604.00209v1)仍有Llama2的CONFAIDE反退；NCR还含拒答/不连贯，不等于一减泄漏率，合成表与正文冲突的精确降幅不用于保证。方向构造、白盒hidden读取、layer/强度搜索与独立输出judge都计费，并需绑定规范标签、模型与人群。域、模型或强度变化后应重验合法效用和不当披露；组合失配时关闭steering，保留最小披露、独立release gate与人工审批，不由模型规范解释认证法定合规或生产隐私。<!-- source-family:SF-2026-ARXIV-2604-00209 -->

本人静态注末一条：`SF-2026-ARXIV-2604-00209` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00209v1)§3.1–3.4/4.2/5.1–5.4及必要E，2+2+2=6，仅单轴/合轴steering与规范读取/行为权限分责；保五轴/Llama2反侧、NCR与冲突数值、标签/observer/完整费用，不授隐私或合规保证，未核实现/复现。

## 00228：PLATFORM-EVALUATION-SYSTEM / Ch66

文件 `books/part-06-ai-infrastructure/66-evaluation-system.md`，“Security Agent 评估是一条 Cost-Success-Refusal Curve”开篇之后、tool-safe分母之前。差额是预测拒答必须锁定真实response label，strict/lenient归并可改ranking；现tool-call安全与provider refusal统计并不覆盖自省标签资格。

完整左锚：

> Security Agent 的一次成功率不能说明部署价值：更强配置可能通过更多尝试、昂贵模型或更宽 tool policy 获得成功，也可能因 provider refusal 无法执行本来具备的能力。EvalRun 因而要把 outcome、attempt/epoch budget、API/tool cost、refusal/abstain、runtime policy 与 task contamination 放在同一 operating curve 上。

右锚现完整“工具安全的分母与时间位置也必须进入这条曲线…”段，保执行前predicate/enforcement/final-text全文。之间拟两段：

若还要让模型事先预测“我会不会拒答”，测量目标必须先定为其真实响应行为，而不是请求是否有害或模型是否符合规范。可先收集拒答预测与verbal confidence，再在fresh context中实际生成回应，按full refusal、partial refusal、full compliance标注；将partial归拒答或归配合会改变二元真值，有限对照中甚至反转模型排名。因此自省sensor、响应标签和安全policy版本必须共同冻结，不能将较高辨别力直接解释为校准或安全authority。<!-- source-family:SF-2026-ARXIV-2604-00228 -->

[有限拒答自省对照](https://arxiv.org/html/2604.00228v1)来自300个base请求的三类变体而非900个独立基础请求，fresh-context也不覆盖已有对话历史；classifier的100个分层spot-check不认证所有partial边界。confidence最高档仍有明显预测错误，strict/lenient定义差异须作为效用/拒答曲线的独立轴。预测调用、真实回应、标签判断和迁移校准都有费用；模型、历史或标签变化时重新验收，误拒/漏拒代价高时保留真实输出检查和确定性权限规则，不以“自称会拒答”批准工具执行或敏感内容释放。<!-- source-family:SF-2026-ARXIV-2604-00228 -->

本人静态注末一条：`SF-2026-ARXIV-2604-00228` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00228v1)§3.1–3.3/4.5–4.6/5，2+1+2=5，仅预测/真实fresh-context行为与strict/lenient标签分责；保300×3相关人口、partial/spotcheck及confidence反侧/全部费用，不授harm真值或安全gate，未核实现/复现。

## 当前状态

三PRE未授权，尚未写入；每项只申请以上两段与本人注，actual后分别交root完整邻接和位置供nonwriterPOST，不授全日。

## 实际授权/POST更新

root实际三逐字PRE与现精确左右锚通过，授各仅两段/本人注。作者按逐字PRE实写并实际顺读完整邻接和本人注、限定diff通过：QMask Ch23 562/564（554–574）注1982，CI Ch72 66/68（60–77）注4569，Refusal Ch66 2338/2340（2334–2353）注6161。root后实际逐处顺读完整左右邻接/本人注，三nonwriter POST全PASS，原正文/读出对象/反侧/全部费用保留，Books未加process收据；各窄锁已释放，真Integration可同步，不授整日。旧申请态只履历。
