# Cognitive Mismatch 2603.18472 v1：必要评价证据与具体NC提案

仅03-21补BJT03-20自然日；作者resume_mar18准备，尚未非准备者Source/date/NC裁决，不计safe/DAY，不写Books。本项已在原65完整题摘独校潜力范围，不扩query/全附件。准入命题为复杂符号任务的终点正确率是否足以认证基础视觉识别，并重新考虑跨任务层级的能力归因；不能因已有覆盖、负面结果或基准而EX。

## 1. 身份与日期

原件：[official v1](https://arxiv.org/abs/2603.18472v1)、[exact-v1 HTML](https://arxiv.org/html/2603.18472v1)。当前官方页v2 Apr9无具体withdraw/correction信号，不据版本号自动扩全revisiondiff；方法和评价采用v1。v1 Submitted 2026-03-19T04:08:20Z；实际DataCite `10.48550/arXiv.2603.18472` created 2026-03-20T02:13:26Z、registered同分钟27秒、state findable；v1 Updated 2026-03-20T00:33:43Z不是首次公开时刻，后v2更新不搬归属。按本批已独校官方availability与同日arXiv DOI事件，BJT03-20仅限定日级归属，不冒精确公告或别处无先稿。

完整题摘及官方header/history实际读回；潜在贡献原校准有效。拟评分2+1+2=5：受限评价盲区而非通用感知架构定律，单评价组件人口分责。NC不会降分，中心争议也不改EX。

## 2. 必要原证与停止

实际exact-v1 HTML Methods §270–365、Table1/Statistics §365–405、Baselines/Metrics §407–488；数学反侧 §162–184、人类与综合分析 §237–269、Discussion §492–497。另外完整题摘/intro与对应任务定义读完。支持与直接反侧已经充分，停止全部领域图/附录prompt/代码/复现/全修订历史，不声称全文或实现核验。

- 13,148样本、五符号领域、三层38子任务；层级样本3388/5848/3912及不同领域人口不是同一图像上的配对感知→推理路径。数据来自Visual C3/eWeBench、MultiMath/MathVista、SMILES渲染和手工专家、物理Olympiad/MMMU-Pro/Gaokao等；LLM分类/再标注后人工验证、重复/缺失/可读性检查后人工statement/label核验。96.7% retention不是独立gold准确率或全部误差覆盖。
- Table1任务同时变化：字符识别/计数、错误纠正、emoji故事/熟语、数学识别/应用、化学/物理关系题；语言F1/计数、纠错ExactMatch/NormEdit、文化BLEU/Chr/GPT-4o相似性、理科Acc等不同量尺。不能把异任务、异metric的总分作同一能力层级下降曲线。计数文字“FP高”与Eq2 recall ratio不完全对齐，本文不采精确计数recipe/绝对跨量尺比较。
- 数学原文明确直接反侧：§L167写L1依赖精确visual localization、pixel-level deviation和极低容错；L169写L2/3可用语言逻辑部分补偿。该解释已显示题目/评分设计混杂，不可用同一批排名倒置排除混杂、再唯一归因视觉encoder。
- 方法开放baseline为DeepSeek-VL2-tiny3B、Qwen2.5-VL7B、Llama3-LLaVA-Next8B、InternVL3-8B；闭源为GPT4o/Sonnet4/Qwen-Max/o3-2025-0416/Gemini2.5-Pro。综合分析L255却写InternVL2.6-8B，不把两个身份合并作精确模型结论。prompt/解码温度、图像分辨率与crop、API revision、无效输出解析、统计CI及全调用费用/设备精度等必要主文未披露，记Not Disclosed，不补造公平全协议。
- 五位bilingual master专业志愿者同prompts的三层下滑，只支持这五人的受测分数趋势，不构成成人population normalization或模型任务难度完全匹配。triangle计数漏composite、化学守恒、文本已给AB=AC/launchheight等qualitative trace可提出shortcut/grounding假设，不能认证内部因果。
- 论文L266–269把Vison Transformer解释为inherent low-pass，并将高层回答归因语言语料记忆/程序模仿；必要原证没有架构替换、同图像等难度任务、blank/mismatched图像、等文本信息/规则/alias等干预。故不采用架构固有低通、语言记忆唯一因果、一般不可扩展或AGI能力上限。Discussion仅提出未来视觉目标设计，不是已实现机制。

## 3. actual唯一owner及具体已有覆盖

sole `PLATFORM-EVALUATION-SYSTEM`，实际[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)完整155–171及337–345已读，Ch65/67开篇交接已读。

- 161–163：input scale/binding arity/operand recognition分三轴；在output format、scorer、预算可比切片交叉改变，明确不能拼不同任务accuracy/substructure/recall成下降曲线，生成器label不是内部容量下界。实际承载本项异任务/异metric不能直接认证认知层级倒置的采用边界。
- 165：decision与witness不同人口不能从准确率差归因能力，欲比较需同实例配对。这是本项终点任务成功与基础子步骤识别未配对的实际验收约束，不声称本书已含本paper数字。
- 339：declared rule/独立perception probe/actual decision分责；probe答对不证明同估计控制终点答案，不能内部“知道却撒谎”的因果外推。
- 341–343：相同pixels、standard/inverse及neutral/semantic alias控制；不是一律将失败归因视觉encoder，同pixels亦不证明每次感知都正确，不識别唯一内部因果。实际承载本项视觉错误与语言prior假设的分辨和必要控制，不把未做控制说成作者已做。

受限采用命题是端点分数不越权认证基础感知、跨任务/metric人口和语义prior分账。上述正文已经承载，不为本benchmark名称新增正文/源注，不虚actualPOST。

## 4. 提案与一次重开

提案：保持5分标准审阅，具体NC；中心架构/记忆因果强claim仅在日报与本packet保留，不能用NC洗白、也不进入正面Evidence/Books/性能或容量保证。若非准备者判断该强claim与本项贡献不可分，则改为5分中心终态隔离、仍保全部证据，不降分/EX/虚NC。请root独立裁这一分采边界，作者不自授safe。

唯一必要重开请求：同图像/信息/难度匹配的识别与终点任务，以及blank/mismatch/equaltext或规则alias干预，报告完全人口、固定模型/解码/scorer与费用；若要采用ViT固有low-pass/语言记忆因果，另须对应架构/训练或表示干预并排除任务设计替代解释。不是请求全作者史或全附件。本次普通未读不存在，不以外部材料缺口无限阻塞其他项。

## root 非准备者必要审阅与具体 NC 裁定

实际 exact-v1 HTML 162–170 的任务设计直接反侧、233–269 的人类/综合归因、270–351 的层级与数据定义、Table1完整人口、406–488 的模型与不同metric，以及489–497结论；原DataCite全部日期字段独立读回。实际 Ch66完整155–171与337–344的难度轴/decision-witness和规则—感知—prior分责，现文直接承载跨任务异metric不可拼为认知曲线、终点成绩不认证独立感知，以及因果归因需配对控制；并非主题相似。

有限 PASS：5分标准审阅与具体 NC成立，不加Books段落或来源注，不虚构actualPOST。只采用有限评价盲区与上述测量权限，架构固有low-pass、内部记忆唯一原因及AGI上限留在报告争议边界，不能由NC表述成这些中心推断已被Books接受；同实例/模型身份/解码及干预缺口不授正面保证。该分采不依赖这些强claim，因而不需把可支持的测量命题整体废弃。root接纳单篇安全处置，日报仍待最终来源归并/DAY。
