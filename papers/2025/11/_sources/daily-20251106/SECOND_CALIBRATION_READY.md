# 2025-11-06 有界增量校准与日期恢复

作者Carver；06默认BJT `[2025-11-05T09:00:00+08:00,2025-11-06T09:00:00+08:00)`。本次仅扩三个模型/表示/后训练完整题摘及两个具名原公告，非整类题摘/全文队列。FIRST的CudaForge/GRACEs/WhisperLeak/Teen Blueprint未获独立校准，不继承05任何响应/评分/关闭。

## 本日新增实际原文与校准点

| 材料 | 具体潜力/边界，待独立校准 | 日期身份 |
| --- | --- | --- |
| [DS-STAR官方公告](https://research.google/blog/ds-star-a-state-of-the-art-versatile-data-science-agent/) | 本次实际L104–153核心/变更理由/直接消融：异构文件先summary，judge评计划sufficiency，router区分改旧步骤与加新步骤，最多10round；L141无context hard-task跌至26.98%，L142只追加比可纠正计划更差，L143 model/难度收益不同。这是可能修正“执行无错/只追加即可”的直接反侧，不能因成熟Agentloop组合自动关闭；也不因榜首/LLMjudge自动收，不授无GT正确性或预算可比。请核具体准入，公告够支持什么、是否有必要定点论文。 | 原显示Nov6（日精度/时区未核），native HTML fetch failed，仅web core成功；没有真实datePublished，不能默认截止前。非已准入。 |
| [Kimi K2 Thinking发布](https://platform.kimi.com/blog/posts/k2-think) | 原短核心实际读：训练为Thinking Agent，边思考边工具，多benchmark宣传，公众号全文作为“了解更多”原链读取失败。潜在模型/Agent训练机制明确但核心未披露，仅发布名/SOTA不能准入，请核是否需要必要技术说明及兼容性边界；不读全旧K2附件。 | 原dateTime=2025-11-06T00:00:00.000Z、显示11/06，与相邻changelog/price一律UTC午夜；未证实际时刻，不直接当BJT08。旧Kimi-K2 repo创建07/03不证明Thinking已公开，HF模型API native/web均失败，公众号web非retryable。 |
| [VCode 2511.02778v1](https://arxiv.org/abs/2511.02778v1) | exact-v1完整题摘L16–20：以SVG符号保真+rendered-CodeVQA测下游语义，语言代码能力强未保证视觉代码保真，专业知识/3D弱；revision与detector/parser外部cue。潜在评价盲区，不因新benchmark自动收或一般视觉eval原则自动关。12.3points是摘要宣传未核；需判CodeVQA答对是否只局部proxy，human与VLM对SVG退步也须保留。 | Submittedv1=11/04 18:00:18Z；DataCite Updatedv1=11/05 02:00:29Z，created03:00:39/registered03:00:40，Available2025-11。均不等真实首公开。 |
| [Shorter but not Worse 2511.01937v1](https://arxiv.org/abs/2511.01937v1) | exact-v1完整题摘L16–18：通常滤easy问题追求训练效率可能抬高推理长度分布；保留/温和上调moderately easy作为implicit length regularizer，无显式lengthpenalty，Qwen3-4B-Thinking/16kcap/AIME25同pass@1长度约减半。潜在训练数据难度→在线长度选择负侧，不授free成本/普遍无损/全模型等价。 | submitted11/02 17:29:16Z，Updatedv1=11/05 01:01:50Z，created/registered02:40:32Z，Available2025-11；HFNov5推荐不等firstpublic，v2Jan9不代v1。 |
| [Don't Blind Your VLA 2510.25616v1](https://arxiv.org/abs/2510.25616v1) | exact-v1完整题摘L16–18：action SFT损失VL表示、targetedprobe隔离动作fine-tuning引起的VL退化与alignment恢复/OOD收益。潜在能力迁移反证非领域应用；仅作具名旧日期恢复线索，不能从HF推荐Nov5改成06新事件。 | submitted10/29 15:20:10Z；DataCite Available2025-10、Updated10/30 00:55:25Z、created/registered02:01:59Z，原project页本次可读但未见first时间。不把Octsubmitted代public；月精度Available支持October元数据状态，未核原正文首次时刻，不展开本日附件。 |

三篇原题摘与版本轻量标记在[RAW_SECOND_EXACT_V1](RAW_SECOND_EXACT_V1.json)，无所见撤回/纠错声明，不遍历版本史。HF只恢复原身份/作者入口，不采用generatedsummary；其Nov5目录25标题只主线查漏，选以上三题摘回原源，Brain-IT/fMRI、AyurParam/Ayurveda、BRAINS/Alzheimer标题明确领域应用拟范围关闭，不读其methods。

## FIRST三篇日期有限恢复实际结果

| 精确版本 | 原字段与可用原源/实际停止点 | 本窗采用边界 |
| --- | --- | --- |
| CudaForge2511.01884v1 | submitted10/23 22:52Z，Updatedv1=11/05 01:00:39Z，created/registered02:39:17/18Z，Available2025-11；v2submitted11/05 02:10:35Z、Updated11/06 01:15:24Z。官方OptimAI-Lab/CudaForge repo创建10/23 20:56:23Z、当前README无首公开时间，只核同题身份，不全commit或执行其sudo建议；两个同名非论文repo已排除身份误配。 | 普通有限恢复已停，首公开真实announcement/完全落窗上下界仍缺；v2跨06截止且无重要修订证明，不把它补成本日新事件。日期层保留，不贡献关闭。 |
| GRACEs2511.02833v1 | submitted11/04 18:58:47Z，Updatedv1=11/05 02:03:26Z，created/registered03:01:57/58Z，Available2025-11；作者现GRACE repo创建2026/03/01。同题匿名OR XP6IvkhPt4 web验证页、api2 notes403；后来ICLR26 m276fke38H不替2025首次字段。 | 首公开/匿名版本关系未核；不补常规20ET时刻，不读理论附件，取得原OR可公开记录或作者exact-v1真实时间才定点重开。 |
| WhisperLeak2511.03675v1 | submitted11/05 17:47:46Z，Updatedv1=11/06 01:58:37Z，created/registered03:01:58Z，Available2025-11；MicrosoftResearch仅November，安全Blog官方11/07窗外。 | metadata跨截止但不当public；安全Blog不是本窗公告，论文first仍保留，不从转载时间补造。若有真实11/05–06截止前公开原证再精确恢复，不扩全文。 |

各[DataCite原字段](datacite-01884.json)及其余5具名JSON/receipt均本日实际200，10请求09:35:29～43Z、补3请求09:38:23～25Z均结束exit0；成功不是date通过。Available精度、Updated/registration权限分开，不把外部缺原材料写成证据/无遗漏。Kimi/DSSTAR也继续有限date层保留，不成全文队列。

## 分类/范围停点与下一步

CL月skip25/show25实际25标题（00576～01181）和DC月skip0/show25实际25标题（00038～02034），native200，分别停next50/25；1527/338全月总数不成全类题摘/证据队列。早先web cache miss为原失败，native成功不反写它。本次只是相关标题补漏，不宣称目标09时前announcement完整可恢复。旧相关系统title若需跨日去重/日期，只核身份原字段，不继承05候选。

普通下一点：FIRST与本批独立准入校准、必要date重新到达后的局部恢复、本日14有限源自包含及六部分进行中报告、已准入项必要证据/owner对读。日期层有限恢复停止不是普通审阅/独立验收已完成。作者未修改Books、shared state或monthindex，不stage/commit/push。
