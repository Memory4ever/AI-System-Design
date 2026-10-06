# 02/20 第十六有限必要包：15983 / 16106 / 16138 / 16149

四项必要精确v1方法、关键controlled比较/直接反侧与actual owner已root独核；15983/16138/16149三项实际正文/完整邻接/自身末注POST通过，16106标准仅报告通过，锁全释放，非日级验收。位置为 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。完整题摘在15983:156–164、16106:56–62、16138:67–68、16149:139–140；潜力明确，不再初筛或扩附件。

| ID | v1 Submitted UTC | 同ID DOI Registered UTC | 北京公开范围（已核官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 15983 | 2026-02-17T20:20:33Z | 2026-02-19T02:35:27Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:35:28+08:00 |
| 16106 | 2026-02-18T00:34:29Z | 2026-02-19T02:38:22Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:38:23+08:00 |
| 16138 | 2026-02-18T02:06:24Z | 2026-02-19T02:39:09Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:39:10+08:00 |
| 16149 | 2026-02-18T02:47:36Z | 2026-02-19T02:39:24Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:39:25+08:00 |

Registered只作arXiv已公开上界推定、1秒精度，Created/Updated原值不当正文公开。当前官方abs轻核15983 v4/16138 v2/16149 v3与16106 v1，Comments仅项目或发表格式说明，未见明确纠错/撤回说明；不因revision号扩比较，采用精确v1。

## [ReLoop: Structured Modeling and Behavioral Verification for Reliable LLM-Based Optimization](https://arxiv.org/html/2602.15983v1)

2+1+2=5，设计反侧/具体差额深入。§3.1–3.4（270–303、344–379）：solver-feasible不等自然语言formulation正确。L1执行/solver status唯一blocking；L2从问题提取候选constraint/objective参数，极端扰动数据再看objective response，用Warning/Info/Pass分责。LLM仍负责候选提议，solver只给响应，不从机械响应签原语义truth。active/non-negligible条件、参数/代码对应、原objective分母与扰动规模须固定；不把Property1叙述授任意MILP完整性定理。L2 Warning触发repair、Info不修；crash/status/objective大变回退的guard也会拒绝潜在正确的重大修正，不是证明所有repair安全。

§5.1（544–567）五model、三bench、temperature0/pass@1、N3；作者约3×LLM tokens并额外solvercalls，不能把matchingtask或greedy当equalcompute/生产SLO。§5.4/Table7（705–781）局部缺项可受益，但RetailOpt strict accuracy加L2不增，CoT本身会让DeepSeek执行退化；IndustryOR系数细误差/结构误解超N3修复。Limitations（792–797）测试参数数线性费用、候选抽取共享生成盲点、coefficient/equivalence/unrepresented结构不覆盖。硬件/precision/全链SLO采用命题Not Disclosed，未核代码/复现。

actual PLATFORM-EVALUATION-SYSTEM Ch66:1755–1766已有same-verdict语义pair与reference/validator/executor分权，3667–3669已有corpus mutation的metamorphic relation；AGENT-REFLECTION Ch80:58–62已有solver只对收到前提有效。具体未承载的是**没有reference formulation时，保持可执行模型并改变已声明参数，检查应有响应以定位缺项，同时按缺项可检测/可修复人口限制反馈权**，不同于重命名tests/self-refine。拟Ch66 same-verdict gate后仅一段，保原reference/human审查、数据mapping和搜索/修复成本、结构错误通过/停止回退；不复制四阶段成熟组合。

## [Algorithm-Based Pipeline for Reliable and Intent-Preserving Code Translation with LLMs](https://arxiv.org/html/2602.16106v1)

2+1+2=5，标准完成拟仅报告。§3.1/3.3（99–101、111–148）：预处理Avatar/CodeNet Python↔Java、五model，direct也有step-by-step提示；替代路径先生成language-neutral algorithm的IO/types/bounds，再第二call生成代码。只评价finalcompile/runtime/tests，intermediate text未grading；同测试不是等token/call预算。§4.1（391–396）不同model/direction收益不同，Qwen在部分条件下降；§4.3（1034–1038）type/overload错误增加，不能把总均值归因无损intent保持。§6（1049–1052）仅两个language/tasksets、人工taxonomy/κ.893与API随机性；作者说拒绝under-specified algorithm，但未交付完整独立fidelity判定人口与预算，不能据此称架构唯一因果或语义等价保证。硬件/precision/API sampling预算Not Disclosed，未复现。

actual AGENT-PLANNING Ch79:173–175已声明signature→形式翻译→parser/solver与translation fidelity分权，169–171已有domain artifact/参数抽取复用；本文neutral algorithm的局部translation配方并非全部已有，但未证新接口正确性或适用条件超出typed specification与finaltests的已有论点。仅保Python/Java经验/错误切片，不因没有该prompt配方制造长期缺口，不退回贡献排除。

## [IRIS: Intent Resolution via Inference-time Saccades for Open-Ended VQA in Large Vision-Language Models](https://arxiv.org/html/2602.16138v1)

2+1+2=5，时间×空间输入接口具体差额深入。§2.1–2.4（93–106）：research EyeLink1000/1000Hz、10participant×50images，spoken question onset用于选择fixations，coordinatewise median附近空间filter，无保留则回退temporal set（10.8%trials）；在原图上overlay markers送VLM，既不是模型内部attention也不是用户授权。采集有forcedfixation/calibration与1.5s silence等待，不能把training-free当无硬件/同步/latency成本。§2.5–2.7（109–121）LOI click用于GT生成/人工选择与作者复核，Gemini accuracyjudge/88%人工一致和embedding similarity各有权限，LOI“upper bound”是协议proxy非数学最优；500pair共享10人/50图，不当独立人群复现。

§3.1–3.3（126–134）近speech-onset窗口/滑窗优于某些allfixations，unambiguous小收益；window在本数据上选择，关联距离≠已证明用户intent causal机制或heldout最优。§3.5（198–213）crop分支较差、可能丢context，textcoords/heatmap另cost和分辨率；不是所有overlay/窗口都安全。Limitations（218–219）大学人群/受控设备，仅proof-of-concept；未核代码/复现，consumer-device/SLO/precision Not Disclosed。

actual MULTIMODAL-REPRESENTATION Ch23:626–645已sensor clocks、timestamp接口与consumer时间head分责；现有Ch23:531原图派生回读和16455marker反馈不承载**用户gaze需绑定question-onset而非全观看平均，表示接口仍须保存原图/时窗/坐标并防crop丢context**。拟时间/provenance段后一个自然段；意图证据不签真值/授权，噪声/设备校准/多调用成本与语言澄清、原图VQA共存，不授普遍用户可用性。

## [Evaluating Demographic Misrepresentation in Image-to-Image Portrait Editing](https://arxiv.org/html/2602.16149v1)

2+1+2=5，设计反侧/条件评价差额深入。§3.2–3.4（185–198、260–262）输出图仍可能silently不执行edit；执行edit也可能改变未要求的skin/race/gender/age。分别ordinal评分edit-compliance与untargetedidentity，不由genericquality或单refusal率认证成功。§4.1–4.3（267–275、325–334）84 FairFace images的7race×2gender×6age，20prompt×3openeditors=5040；paired500 featureprompts只改变prompt、same输入/seed，但外部appearance抽取与采样人口须保留，约束是soft描述不是latent独立control。

§5.2/5.3/§6（379–389、440–442、461–474）source demographic切片下mitigation异质，且VLM/human都发现edit success下降；human30workers/3rater/item，κ.09–.28、α.23–.46低到fair，VLM高估edit成功，不由平均identity改良授全部自然用户有效或内部White/safety因果。仅84受控images/三editor、有限prompt；“structural rather than incidental”是作者解释而非所有生成器保证。只采用定性条件/反侧，不继承headline比率，完整预算/硬件/precision/SLO此命题Not Disclosed、未复现。

actual PLATFORM-EVALUATION-SYSTEM Ch66:745–749已有response-rate/conditional/unconditional quality，428–434的target/untargeted×context语义偏好评价不同于image editing source identity；尚未承载**输出存在、目标edit响应与未目标identity preservation须按source demographic联合切片，soft身份约束可能以edit交付退步换保留**。拟response-quality gate后仅一段，如root确认该差额而非已有条件控制重述；保detector/judge人口与独立人工、原单属性/原prompt路径，不复制人口统计榜单或授公平性保证。
