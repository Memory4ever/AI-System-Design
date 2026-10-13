# 13091 VAEX 必要原证与 Ch66 最小差额

resume_mar17，2026-03-17 仅补03/16自然日。完整v1题摘/日级夹证复用 SUP_AB_OFFICIAL_SUPPLEMENT_20261011.jsonl 第18行及匹配DataCite/独核；当前官方abs v1/v2只有project链接说明，未见已给出的撤回/勘误，不因v2存在展开版本diff。2+1+2=5，具体证据构造差额加深，不把一般benchmark原则计增量。

## 必要 Source 实际范围

[exact-v1 HTML](https://arxiv.org/html/2603.13091v1) §3/3.1/Table1、§4.1–4.2/Table2、§5.1–5.3/Table3–4、§6/limits、G.1–G.2、H.1–H.4及I.1–I.2；同[v1 PDF](https://arxiv.org/pdf/2603.13091v1) p26–27/Table7–9定点恢复HTML空prompt。PDF与HTML附录字母不一致，正文共同身份核实，使用表号/p页，不称全附件视觉读过；未核artifact/复现。

真实增量是先定义query/room-object/topology事实，再摆放物体/安排trajectory，让关键证据跨时空分散，再render和human cross-validation；不只增加题量。五extractive与五abstractive只是语义意图配套，question/answer/cue不同，不是唯一因素的严格配对因果。十视频300query（每视频30），平均36.81秒/640×480/原30fps；多个query共享scene，五次独立decode的Accuracy@5是平均而非pass@5，H统计是重复decode稳定性，不是300独立场景或真实世界人口置信保证。10annotators交叉场景核，不误称作者没有人审；infer scene和看scenario一起校对也非模型实际32 sampledframes可答性审计。

32uniform frames但Gemini接口例外，closedAPI/HF4–8 L40S/OpenRouter混合，temp.7/top-p1/top-k40只限可控接口；完整precision、budget、长度/batch/concurrency/SLO与总API/制作费用未齐，不授同compute/生产SLO。Map Scale human60显示难度/度量混杂；GeminiFlash Simulation51.3却extractiveRoute16、Qwen32B42.7vs6.7，不逐task宣称abstractive更难。MCQ去选项改变输出/判分，Table4仅三task且GeminiProMemory无下降；主§5.2文字“四task”与H.3/表“三task”冲突隔离。Memory–Action freeform用Gemini3Flash共源judge；PDFTable8仅targetroom/modelanswer，缺物体/GT显式输入桥，不签精确judge recipe或全部能力差由选项造成。

§5.3错误分类可诊断但不是内部因果：Hop2是在Hop1通过子集上统计，给错误room不可能验证原目标object≠模型真实两个memory组件的定理；counting错也混perception/aggregation。10×10 map mIoU混坐标/尺度/格式，PDFTable9实际JSON而主文10行口径不一；不要称已经独立量到纯空间能力。I合成人审可答性不证明sim-to-real，付费/制作2–3weeks每scene与“每人350/scene”对总3500口径也不拼完整费用。

## actual owner / 逐字 PRE

实际Ch66 20–110与220–269，另234后完整旧MAP acquisition/interpretation→首个不变量邻接及Ch65/67开头已读。既有OAKS phase和主动观测诊断不包含query先行生成evidence、真实场景GT和受测可见性分验的差额；唯一 `PLATFORM-EVALUATION-SYSTEM`，Ch25/26不重复评价构造。不能按“已有benchmark章节”假NC。

拟仅在原234主动获取/MAP段后、`## 第一个不变量：评估声明必须绑定完整对象`前插**一段**，原证有限protocol可支持；争议judge、rank与内部瓶颈不进入正文。尚未独核/授权，未写，未计safe。

逐字 PRE：

固定录像上事后出题是便宜且贴近自然分布的旧路径，却难以保证决定答案的证据真的跨越多个时空位置。需要测试这种整合时，可以先规定问题、场景事实与证据分布，再设计物体布局和摄像轨迹，渲染后由其他标注者核查视频可答性；同一场景保留局部读取与跨房间整合两类题，而不以局部识别高分认证全局地图。[VAEX 的受限构造](https://arxiv.org/html/2603.13091v1)支持这条证据生产分支，不证明两类题是严格同难度的因果对照，也不由失败分类识别内部记忆瓶颈。场景真值、实际帧采样与输出判分须分别冻结：多题共享十个场景，五次生成只测解码变动，不增加环境人口；提供选项或改用自由回答又会改变任务与 scorer。布局、渲染、人审和重复调用均付费；真实迁移、可见性或 judge 资格不足时，保留原录像、局部题和独立人工核验，只报告受控切片，不签通用时空能力或生产安全。<!-- source-family:SF-2026-ARXIV-2603-13091 -->

静态本人注拟写：

[^src-vaex-bench]: [VAEX-Bench](https://arxiv.org/html/2603.13091v1)（2026-03-16，exact-v1）。必要审阅§3–6/Tables1–4、G/H/I与同v1 PDFp26–27/Tables7–9；仅采用query-conditioned证据构造与场景/解码人口分账。有限人工合成场景不认证真实世界迁移、严格配对因果或内部瓶颈；freeform judge/格式口径未闭合部分不采用，未核artifact或复现。

只对受影响freeform数值若未来采用时一次请求：Table8实际judge evidence/GT输入与固定parser、三/四task对应，接受原prompt/最小calltrace/正式勘误；本轮不采用该分支，不以此阻塞可读protocol差额，材料到达只重开本family。

## root 非准备者 Source/PRE（2026-10-11）

root 独立打开同exact-v1，实际读§3/Table1及§4.1–4.2/L129–164、§5主protocol/Table3/L165–202与G.1/G.2/H.1/L307–346；原稿问题先行→场景/轨迹→渲染→非同场景构造者交叉校验，支持这一个证据构造差额。人工验证同时看场景配置，不等32 sampled frames独立可答性；本PRE已保留实际采样分责，不认证相同预算、配对因果或内部瓶颈。300问题共享十场景、Accuracy@5平均定义及合成/费用边界实际核对，未采用受影响freeform judge和排序数字，不额外重读全部附件。实际Ch66 L210–251、完整MAP段→首个不变量已独立顺读，既有主动获取/解释替换不拥有反向设计场景证据的差额。

逐字一段及静态末注通过。授resume_mar17仅Ch66此一段和本人注窄锁；写后root读实际新增及完整局部邻接/注后才能计Books落实，不是日级验收。未复現或认证所有表格。

## actual POST：root 非写入者

实际顺读Ch66 L228–248：joint/conditional→可识别假设→state/dynamics→MAP获取/解释→新增236证据生产→完整subject identity不变量，及章末自身VAEX footnote/相邻GoogleCog来源注。真实正文与PRE一致，仅增加已定义的脚注marker；采样、共享场景、decode人口、输出判分、因果/judge限制和原路径退路均保留，与前后问题衔接自然。根源构造段实际回对v1 §4/G，不将所测分数当内部机制或物理能力；限定diff检查通过。局部Books actualPOST通过，root释放Ch66窄锁；不授本日DAY或其它来源的正面覆盖。
