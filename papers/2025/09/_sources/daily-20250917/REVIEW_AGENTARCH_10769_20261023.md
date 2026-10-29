# AgentArch10769 首次必要Source准备包

准备者Lovelace，非报告writer Bernoulli。作者77明确未GET/读Methods单让，本人109已接受独占；本包由Bernoulli从保存primary一次非准备者采用，不selfsign正式/Books。

## 原件与实际必要域

https://arxiv.org/html/2509.10769v1 。REVIEW_SOURCE_10769V1_20261023.raw/headers/request正常200/exit0/321874B/8.189620s，SHA3815d49d8ab08a0c5e2c7f6231ede74f5a07f398b093e1ef6e3507e5ab26c06c。106完整exact-v1/current/联合Sep16层直接复用，不第三日期或后版Methods。

actual完整§3–8、浮在§2的T1–3、T4–6/T8全部数值、A.1–4正文与Fig3–6完整文字prompt。T7/T9/T10只指标身份/定位，未所有数值；未Fig1/2架构图像素、数据/代码、API执行或复现。A.1用例与单agent合并instructions/人类标注、A.2 thinking semantics、A.3实际prompt读足，不依摘要“enterprise”下判断。

## 具体增量与拟分数

单部件测量不能决定完整Agent配置→同两个确定mock工作流、六backend上交叉比较orchestration/prompt style/memory/thinking→检验配置偏好是否随模型/任务变化，并区分最终决策与真实调用合同。拟2+1+2=5，仅受限配置比较/测量接口，不借六大模型、enterprise或低总分加分；无新Agent运行算法。

正文称四orchestration却实际列三：single、orchestrator-open、orchestrator-isolated，表亦三。每类ReAct仅complete×thinking开关，function calling才complete/summarized×开关，故每类6/共18，不是3×2×2×2完整24因子；不能把没测的ReAct summarized当已测或分离所有高阶交互。两任务分别60 utterances，TO8tools/3agents，CR31tools/9agents；复杂程度不只一个变量，不能由两任务排序变化唯一识别复杂度因果。

所有tool responses为人工构造deterministic messy JSON/长KB，不是生产执行；工具名、实参、预期顺序与最终决定人标。single拼接所有agents instructions，名义同信息不等相同上下文长度/工具候选/调度次数。complete含原tool/history，summary只前agent finish摘要；摘要可能丢信息，也改变token预算，不能当相同context单因素。ReAct用于orchestrator与worker两级，主文自己承认未分别测试单级，故低分不推所有multi-agent ReAct应禁用。

关键A.2：math与synthesize_collected_information根本**不执行外部计算**，模型文字原样返回并写memory，是额外reasoning token/显式记录接口；不称calculator/tool验证了日期/数学。额外tool动作与记忆/调用预算同时变，不能独归真计算。Prompt bundle也不同：function calling用system instructions+native schema/API，实际ReAct Fig4/5将任务/JSON模板放user；与A.3“all information system”的文字不齐，不替作者改角色/指控代码，只按两种完整接口条件保留。Sonnet4 reasoning disabled/Bedrock，OpenAI和Llama用OpenAI-function调用接口；temperature0不免backend非确定或接口兼容性差额，精确revision/token/step上限与完整时延费用未足披。

## 指标与直接反侧

Acceptable是correct tool choice AND all arguments完全正确 AND final decision正确，默认lenient允许额外read-only而惩罚额外write；strict要求顺序/全精确/无hallucination。人标固定reference也可能拒合法替代路径；最终答对不代表调用/参数/真实effect已对，mock effect不等生产持久化。Hallucination仅不存在的agent/tool名，非事实、参数、越权或所有失败；zero不等安全。

保T2受限pass@1与T5 final-decision分离：GPT4.1 TO single/function/summary/thinking70.8%，关thinking48.5%，complete开68.1%；CR的single结果21.5而multi组合可有97–99% final-decision却仅约15–17% Acceptable。Sonnet CR约33–35% Acceptable与较高final decision不混；精确表最高35.2与文字35.3另保原打印差额，不补rawcounts。o3-mini TO single约55–57但multi ReAct约1–2，CR反有multi function22.2/文字22.3而single约1–2。局部配置/任务交互真实可保，不以全部rank同向或所有model/prompt外推。

T3 CV/SD是**跨18配置**而非同配置跨trial噪声；低CV可表示各配置均差，不能直接签重复可靠性或稳定生产模型。k8尝试/每task应保向量；T8与pool pass@1的八次幂数值几乎相合：本人逐18×12=216cells比较(T2百分比/100)^8×100与T8打印百分比，全部差≤.1pp，最大.058605pp（含输入四舍五入）；70.8333%^8=.0633726。这里只数值观测，不证明未核实现就这么算或所有raw运行不可靠。

若目标为同task连续八次都成功，均值的八次幂不等按task平均的八次联合率。有限算例：两task条件成功率0和1，各次独立条件成立时mean p=.5，真实按task平均all8=.5，而pool .5^8=.00390625；同mean p不能恢复此量。若实际测60task各8次的经验all8比例，未加权计数步长应1/60，T8 6.3%不直接是这一计数；可为另一估计/人口，原应说明，不由reader补统计实现。保pass1有限表，暂不采用“6.34%即真实同任务八次持续成功”的强解释，不拿temperature0或跨配置CV补它。

未给独立tasks/paired uncertainty、选择18配置后最优的holdout、相等总tokens/latency/工具调用预算；各8重复不是8个独立训练seed，也不把60×8冒480独立任务。所有orchestrator/worker调用、finish/summary、echo thinking、长KB和各配置搜索/人标/八次reset均付费，hardware/precision/完整API账单与SLO未足披，不能由小模型peak接近大模型证明净费用相当或生产可靠。

## 唯一owner与建议处置

actual唯一建议PLATFORM-EVALUATION-SYSTEM Ch66。完整520–530已有model×benchmark×harness×environment×scorer、authority/action-space预算及fresh-interaction/trajectory/rescore分责；866–878过程instruction→真实tool trace/实参/effect→outcome，脚本化与合法替代路径边界；1838–1858 Pass@k/Pass^k同task isolated resettable outcome-vector/paired-analysis，2371–2380按题cluster不假独立连乘；822–836重复预算/原轨迹不确定性均完整相合。Ch82 equal-budget Pareto 1019–1024是拓扑消费者，非本篇第二owner。

建议原5/唯一Ch66具体NC、Book0：长期可保的是完整harness条件的模型/任务交互，以及决策、调用/参数合同和重复结果分账，现文已具体拥有；有限排名和echo-tool反侧留报告，不说所有结果已经进书。未采用的新强命题是普遍禁multi-ReAct、thinking真计算因果和pool p^8持续可靠性，这些不能由成熟现文补证。若writer认为本文中心只能用上述未闭强量才能成立，应保原5/具体中心D而非假NC，请据实际选定采用命题决定；不强凑新段或降分EX。

对强可靠性或架构因果的有限重开仅相合task-level outcome vectors/Pass^k定义与reset、实际prompt/API与echo-tool语义、共同预算/逐条件对照或具名修订；当前有限pass1表与NC建议不依可选全日志/全部T7/T9/T10/图像/代码读取。生产mock外推不作已验证事实，未预正式第55/PRE/Book。
