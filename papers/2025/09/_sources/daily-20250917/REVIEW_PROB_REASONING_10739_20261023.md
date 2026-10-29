# 10739概率推理：必要首包，拟五分/唯一Ch66具体NC

## 范围与原件

作者95明确未GET/未Methods/无在途单让，本人已明确接持首必要域。唯一[exact-v1 HTML](https://arxiv.org/html/2509.10739v1)正常200/274952B/6.774347s/SHA962de948719c7f82d1d5a9ff1a33e5e31dcdc072da5c31be774fbb1eec8c330d，REVIEW_SOURCE_10739V1_20261023.raw/headers/request已存。L136/95完整精确题摘/current/联合Sep16日门直接复用，无第三GET；v2方法不倒填。

actual完整§3–6/T1–2所有行/Limitations、A全部六prompt的foreignObject真实文字、B全部所列离散分布、C judge完整prompt及资格、D/T3、E/T4–5、F必要文字、G/T6全部行。Figs1–4只原文字/caption，未取所有曲线像素、代码/训练/工具执行或复现，不造图上精确值/全统计日志。附录较短且分别决定oracle/采样独立/计数或推理解释，所以按具体命题读取，不是25页配额。

## 贡献与拟评分

同一概率题答对可能只说明读懂给定频数，不能同时证明条件推断或从相应分布独立生成 → 原文在明示离散联合空间上分mode/MLE/sampling×joint/conditional，并替换标签、raw observations和频数输入 → 可重新选择哪项能力/信息合同支持评价。窄准入延续95，不借first/模型名/60%宣传或通用统计原则加分。拟DesignDelta2+SystemReach1+Durability2=5，只单个行为评价接口；标准必要域完成，采样/判分关键反侧按所需加深。

## 原机制与评价权限

§3明确有限label组合空间，mode取经验频数最大项，MLE估所给样本的经验概率，sampling输出K'项后计算输出经验频数相对输入经验分布的TVD；不是从未知真实人口恢复唯一分布。Conditional需按给定变量值过滤、对其他变量边际化/归一，joint与conditional的候选数/计算步骤不相同，不能直接称同难度因果对照。

主设置|L|=12/27/36/54、K=5|L|；固定频数集换10种outcome对应再各10prompts共100，不是100个独立未知分布，较大空间另选entropy大致相近的频数。标签类别变化可伴tokenization/长度/语义先验，观测只支持表征/格式敏感，不识别训练偏置唯一原因。A的基础prompt明确禁止code/pseudocode/允许reasoning并要求格式；G另开放code interpreter，已改变工具可用性/预算，不是同一裸模型突然获得全部概率推理能力。

模式识别先regex，格式不合才用Llama3.3-70B看question+expected+response判语义正确。C明确judge仅mode，100随机人工核对99一致；不能把它外推MLE/sampling全输出真值。后两任务不合格式/缺答可discard，未披各模型全部丢弃率及有效/全请求分母，不以“typically follow”补零失败。完整精度/temperature/APIrevision、seed/每次独立性及运行硬件/总费未齐，准确率/距离不授部署能力或SLO。比较不同family大小混训练/蒸馏/接口，不能从70B对8B归参数量单独因果。

## 实际正反结果与采样解释

- T1 joint-mode Llama8B在12→54时.59→.21，GPT4.1mini 1→.96；cond-mode GPT4.1四格1.0，但Llama8B cond在12/.83和54/.62反高于joint .59/.21。故不照录“conditional对所有模型更难”。
- T2 explicitfrequency的joint-MLE多接近0TVD，cond更难的局部差额保留：54空间Llama8B .198/DeepSeekR1Distill .100/Llama70 .084/GPT4.1mini .016，joint对应.02/.02/.0004/.0001。不是高分认证一切随机变量或科学数据。
- T6 GPT4.1mini raw samples相对频数的joint-mode从12 .87对1.0，到54 .28对.96；加工具为1/1/.99/.97，对frequency1/1/.99/.96。这支持显式计数/信息表示接口；按F固定|L|12增K仍退步的文字保留，不冒未读图精确数值或把长度当唯一原因。
- K'=7|L|的sampling以Python random有限iid输出的TVD作噪声基线。LLM若人为配平频数，其有限histogram TVD可低于iid随机样本，而过程仍相关；例如p=(.5,.5)固定输出ABAB的TVD0不证明iid。这是解释权限例子，不是论文全部算法反例。D原T3 DW/transition-entropy阈值将六模型标为非独立，且作者举按目标计数列出后无法shuffle的响应；保相关观察，不把未给的类别数值编码/entropyratio定义/阈值校准补成通用独立性检验。低TVD不直接支持原“underlying sampler更接近真实随机分布”。一次长输出与多prompt各出一项也是不同过程，后者偏高频只作者观察，未给完整同预算表。
- E Mushroom例子只三离散features/声称80条的子集，不涉及蘑菇安全判断/医学AIS。T4打印非零13/17/34/2/9合75而标题和正文80，缺失5条或分母说明未闭，不自补。T5 Llama70 joint/condmode都100、jointMLE0/cond.005，jointsampling.111/condsampling.089；R1Distill采样.237/.173也显示conditional未必更差。该aux局部原结果保留，不认证其全部分母，不能由此否定主有限协议或自修原数据。

全prompt/frequency制备、raw计数、生成84至378项及全部失败/格式fallback、100次与judge/人工、代码工具和对照采样费用都存在。主任务无需本轮训练，但原模型训练/蒸馏并非免除；输出histogram/格式通过不授实际iid、通用概率理解或真实决策可靠性。

## 唯一 owner 与具体NC

ROADMAP唯一`PLATFORM-EVALUATION-SYSTEM`/[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。actual20–62的条件证据/完整身份与受控能力、496–526的不同证据对象/原响应与harness/scorer、1028–1068完整分布评价组已读；不改Books。

尤其当前“能描述分布，不等于逐次调用会从该分布采样”完整两段已明确分别保存目标数据、描述分布、逐调用经验分布、samplingconfig和相关性；紧后规则/边缘频率/自身历史条件结构分验完整段又直接承载“边缘频数接近不等条件采样可靠”。此前统计可评估性组另分有限样本分数与任意分布统一保证，开篇/identity组把信息呈现、scorer与工具作为测量条件。这是对本篇安全窄采用命题的具体覆盖，不是仅“概率/评估”主题同名。

拟**标准完成、原5、唯一Ch66具体已有覆盖NC/Book0**；原有限benchmark/正反结果留报告，不替其samplinglaw、全部conditional更难、跨模型因果或Mushroom分母补证。无需PRE/新Book位。只有要采用上述强量时，取得精确分布/全响应与丢弃人口、sampling/统计定义和相合分母/具名修订才单项重开，不默认全曲线/所有代码/所有分布。

交Bernoulli一次不同角色必要采用/原5/owner与具体NC，首准备不selfsign正式第71。当前70=23I26NC21D，10655最小EX等作者一次，10818及作者新题摘/来源尾仍普通，无active Book位，未DAY/FINAL。
