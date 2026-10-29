# Terminal-Lego 03461 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author；R27完整题摘/准入与Jun03联合日证、2+1+2=5复用，不第三AB/date。仅本日必要层。exact-v1 [HTML](https://arxiv.org/html/2606.03461v1) HTMLfirst；当前完整剥标/保mathannotation TEXT88217字符保存为[原件](2606.03461v1.fulltext.txt)，无工具truncation标记。实际必要读§2–5.1/5.3、Limitations、A4–5/B、D1–2/D4；§3及A3.6数据验证核心读，非完整prompts附件逐项审计。支持与直接关键反侧足，止于此，不把未采用的全部附录/代码变为额度；未核图像像素、实现、数据或训练复现。

## 必要证据与反侧

§2固定task substrate/Terminus-2/harness、student backbone、recipe和TB2评价；四teacher交集同8.1K成功任务；Qwen3-8B/32B，TB2三独立trial平均pass rate，不是三trainingseeds/置信区间。T1 Opus standalone69.4/DeepSeek39.3，但student8B5.6/10.5、32B15.5/20.6；只支持此交集和配方下teacher独立排名不替student验收，不等教师完整成功pool效用、全部token/GPU预算已配平、低分teacher普遍更好。

§4.2同1.1K hardtaskpool五rollout选择最长/最短成功轨迹：8B长5.2<短6.0、32B长12.7<短13.9，不能由更长/更多显式error-recovery直接认定更可教。1.7K errorfree四teacher同题筛选仍保DeepSeekstudent较高，只排显式错误消息，不等过程语义无错或隔离全部风格/长度/target混杂。

§4.3/T3 TOR=有path-aligned先前observation的action数/全部action数；align含同path、包含或直接相关，非观察token比例/语义因果/必要充分取证证书。D1–2明确cat读取是observe、重定向写是action；混合turn占48%，命令字符串需语义分类。D4额外commandpair计数用3assistantturnwindow，不擅自把此窗口当Eq1全部TOR的已实现精确定义。Limitations明确未测每observation必要性、充分性或推理逻辑严密性。

§4.3.3 **loss-level而非trajectorydeletion**：8.1K DeepSeek轨迹中仅pureobservationturn监督被mask，原turn与terminalobservation仍serializedcontext可见；pureaction/mixed保留。T4 noMask→mask，8B10.5→3.8、32B20.6→13.8，avg监督turn7.3→4.4；原段误指T5，实际masktable为T4。支持“可见反馈与显式生成观察动作监督是两份不同信号”，不授语义唯一因果/只剩action即完整等budget。生成analysis/plan/commands的整turn mask也不隔离命令token的全部独立因果。

§4.3.2 high/low/random从同1.1K成功任务五rollout池选，每组一份对应同题；32B14.6/11.8/13.8，只相关选择支持。§4.3.4 target50%与等turncountuntargeted/random；**mixedturn中的action亦可能一起mask**，控制turn数不等有效token、梯度尺度或纯observation成分完全相同。T7target17.2而邻文17.6内部不一致，不采精确target差额；其余32Bnone20.6/random19.1/un19.7仅该表条件。§4.3.5同Opus/8.1K改systemprompt鼓励先读再写，TOR2.5→6.6、32B15.4→19.5（与T1原15.5小异）；不能把整prompt改动的收益只归TOR，不采用通用强制多读recipe。

§4.3.1 failed2.5K DeepSeek对照并非matched成功pool，8B3.5远低于成功10.5，32B16.1低于成功20.6；不能把仅其32B超过Opus成功轨迹15.4写成失败数据普遍更好或最终success不重要。采用命题不依赖这组跨人口因果。

§3/A3.6/A4/A5：StackOverflowaccepted/votes→dependent instruction/environment/solution/tests/Docker，独立LLMreview可至3轮但不是人核真值。主文postsolutionreward positive，A4明确reward.txt含1/onlyreward1准入；A5 15389/36846=41.8%，只执行/生成测试通过，不证明完整任务、真实意图或无泄漏。A5 FAIL_TO_PASS8.81/PASS_TO_PASS1.48是原表统计，非每题全部有效证书。B输出10Kbytes截断、接近contextlimit模型自summary、completion双确认、retry3；固定scaffold减少接口混杂，不使teacher过程变为逻辑真值。

§5.1最终15K（12.8K成功+2.5K失败，近似数），Qwen3-8B7epochs/32B3epochs，LR1e-5、40,960maxseq、globalbatch8/micro1perGPU、AdamW(.9,.95)/cosine5%warmup/clip1。该finalrecipe不能补造每ablation完整相同token或cost。precision、GPU型号/总卡与完整训练/teacher制备token/时长、并发、推理SLO/各trialseed Not Disclosed；采样三trial不是retrainuncertainty。§5.3同15K数据数/同DeepSeekteacher比较Nemotron三subset32B19.9/17.2/17.9vs24.3，非等总准备/训练compute。Headline30×按数据条数，不采用端到端省费/SOTA保证。

所有task生成/review/Docker验证、teacherrollout、parsedcommand/targetedclassification、保完整contextforward、student训练和独立行为回归均付费。局部generalization只8B/32B四teacher/terminaltasks，不外推全部agent、安全或生产可靠性。

## actualowner与最小差额

唯一TRAIN-SFT Ch29。当前ROADMAP/三Bookscontext已完整重读；2026checkpoint仅路由。实际读Ch29开篇/末交接、§lossmask相关184起可见历史与target区分、241–259梯度路由/输入corruptionsupport、260起失败历史与恢复target、324起demonstrationqualification以及388–465“Teacher越强越好”完整相关论证；Ch28/30开篇边界定点读。检索exact03461/TerminalLego在Ch27/29未见旧family，不新建owner。

现Ch29的2604-08880两段已承载teacher交集筛选改变比较对象与“teacher独立分不替student”；2506-23041还讲teacher可教性校准；前lossmask讲保留context不等保留target。**不把这些已有通用结论再算差额**。实际未承载terminal中生成observation动作本身的训练target，在反馈/原turn仍可见时去掉该监督的具体反证，以及pathalignTOR仅提议selector、mixedturnmask不能签纯取证因果。这是同owner的一条具体监督分支，非runtime工具执行策略或Ch27再造数据pipeline。

拟在2604-08880完整两段后/2506-23041完整视觉teacher段前补原两段及trueH2本人注。未新授/未写Books；待首次独立必要Source/actualowner/PRE。

完整上锚（两段）：

比较 teacher 还要先问“蒸馏本身有没有收益”。只比较两个蒸馏后 student，可能把较小退步误当最佳方案；至少要保留同提示与评价协议下未蒸馏 student 的基线，并对齐有效 batch、更新次数与预算。若更大 batch 恰好减少更新次数，改数据策略与少走几步带来的保护不能被混为一个因果结论。<!-- source-family:SF-2026-ARXIV-2604-08880 -->

训练样本的选择也改变比较对象。只保留所有 teacher 都答对的交集，适合隔离同题 rationale 的可教性，却消除了强 teacher 多解出的题目与监督数量优势；分别使用每个 teacher 全部答对样本，更接近单 teacher 的部署效用，但同时改变数据数量、难度与 reasoning quality，不能把收益全归于容量匹配。[受限重评](https://arxiv.org/html/2604.08880v1)中两种协议会改变 teacher 排序，一些任务蒸馏仍不如原 student；没有统一的容量比或数据量阈值可替代任务验收。共同交集并非错误，关键是先声明研究的是机制隔离还是完整训练方案；若蒸馏无稳定净收益，直接保留原 checkpoint 比在退步方案里选赢家更合理。

拟增两段：

终端 Agent 的可教性还要落到学生被监督生成了哪种交互，而不只看教师排名或成功终态。保留“检查当前文件与目录→修改或执行→观察结果”的完整轨迹时，环境输出可以是后续动作的条件，主动请求观察的命令则是另一份行为 target；前者仍可见，不等于学生已学会产生后者。[受限同题终端对照](https://arxiv.org/html/2606.03461v1#S4.SS3)在保留原 turn 与终端输出的条件下，仅屏蔽纯观察 turn 的生成监督，两个学生规模的 held-out 任务分均下降。这支持把取证行为纳入 demonstration 合同，而不是把“已有工具反馈”当作删除观察动作监督的充分理由。

这种监督选择不能由命令数量自签正确性。按先前观察与后续动作的路径关系定义的 TOR，只能提议轨迹选择，不证明观察必要、充分或推理忠实；针对性屏蔽若连带移除 mixed turn 的动作监督，也不能把全部差额归给纯观察。更长、更多错误恢复或更高 TOR 均不是通用质量证书，失败轨迹的价值还依赖学生与任务人口。应绑定任务、harness、teacher/student、可见历史、监督位置与验证器，分别看独立任务收益和有效 token/更新预算；任务合成、教师采样、命令分类、完整上下文训练与回归都计费。代理失准、监督删减或部署行为回归时，保留经核验的完整交互示范、原 student 与独立 outcome 检查，不以较少轨迹条数批准总成本更低或自主执行可靠。<!-- source-family:SF-2026-ARXIV-2606-03461 -->

完整下锚：

若发布teacher对任务很强、固定student却难以消费其输出，还可以先准备另一份专供蒸馏的teacher，而不只更换student目标。一条[受限视觉蒸馏分支](https://arxiv.org/html/2506.23041v1)保留attention路径，降低各层MLP输出相对权重并提高skip权重，再以扰动邻域的训练目标适配teacher，最后让student学习其输出。它允许teacher本身得分下降而student改善，但不由此证明teacher已恢复真实输入信息：像素重建和激活聚类只是所选表示/decoder下的代理，不是精确互信息或因果机制。应保存原teacher、重权/适配版本、搜索与student配对，并在独立任务上同时比较原student、普通teacher蒸馏和新teacher蒸馏；多checkpoint各训student再择优也须计入预算。teacher额外梯度、proxy训练、全部选择和蒸馏全付费，较小目标数据与部分任务仍可反退；净收益不稳时，保留原teacher/普通KD或原student，不把教师独立排名、更低重建误差或局部重权签发普遍可教性。
<!-- source-family:SF-2025-ARXIV-2506-23041 -->

本人trueH2注拟：

- `SF-2026-ARXIV-2606-03461`：Daily2026-06-04补Jun03；exact-v1 §2–5.1/5.3、Limitations、A4–5/B/D1–2/D4与§3/A3.6必要，2+1+2=5因生成观察动作监督与context可见的具体差额深入。只采loss-level去观察监督反证和TOR代理边界；保mixedturn动作连带、teacher交集人口/三trial非retrainseed、失败与长轨反侧、T7数值冲突不采和全费，不授路径对齐真值/30×总降本/自主可靠。未核图像、代码、数据或复现；待首次PRE/新授/唯一实际POST。

