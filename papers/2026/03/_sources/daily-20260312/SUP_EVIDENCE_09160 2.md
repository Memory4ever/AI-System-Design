# 2603.09160 — 离线逐样本缺口rubric与奖励盲区（必要Source/date/PRE/actualPOST通过）

[RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning exact-v1](https://arxiv.org/html/2603.09160v1)。root已完整AB准入；作者actual完整§3/4、AppendixB/E/F/H，必要Table1/5/6字段。不读全部G/I曲线像素/案例或repo，不授代码/复现。currentv2 Sep26题摘措辞细改、comment空，无已见withdraw/纠错；v1HTML页内Aug24呈现日期与明确v1身份/提交史不同，不能把渲染正文日期冒充公开日期或迁移本窗。只采用确切URL的原机制/协议，不回填v2。

日期原batch2 arxiv.content owning/findable registeredMar11UTC02:06:50为已可发现上界，SubmittedMar10UTC03:51:27配本日official noadvance最终ID/DOI与公告日程最早Mar11BJT08下界，同日夹证03-11BJT；不是Submitted/Updated/注册单独公开。无已见必要更早发表信号，不扫其他会议/项目史。root必要日期实际核通过，与文末Source/PRE/POST结果一致。

拟2+1+2=5标准；具体长期缺口深入必要范围。全局holisticcaption reward易shortcut→离线teacher committee与初始student差额制备逐图binarycriterion，然后训练只用文本LLM逐项验rule→rubric来源/所选缺口和独立图像事实分责。成熟GRPO/多数投票不另加分，唯一TRAIN-RLHF，不绕到caption数据/Agent多owner。

## 机制与受限采用

§3五teacher caption＋Gemini2.5Pro writer读取图像、匿名caption和studentcaption，提取共识→只保留student相对共识未满足的criterion→severity1/2/3→LLM binaryverdict加权归一reward。不是持续onpolicy刷新：B声明committee onceperimage、E stage1遍历制备完成后stage2循环训练消费固定R(x)。student已满足项被排除，R只覆盖当初诊断差额；即使score1也不能保证新出现的错误、原正确项或漏项不被牺牲。该盲区是从明确规则与冻结时序推得，不写成作者已实测完整覆盖失败率。

§3/E阈值至少ceil(K/2)，K5应3；B systemprompt却说>=2，且同时自称majority。原身份不静默改为3，实施须锁定实际准则；此次采用抽象committee条件提案，不认证唯一阈值recipe或多数真值。B judge只收到criterion/description/evalrule及generatedcaption，F明确Qwen2.5-7B-Instruct LLM-only，不见原图；其verdict测“文本是否表达rule”，不能重新确认图像事实。来源writer/committee可能共享错误，匿名身份不能消除内容风格偏差、相关或知识泄漏。

reward G归一权重支持固定同图尺子，但跨图M/权重不同分母、零rubric/zero-groupstd未在必要描述闭合，不能自己补实现。§3GRPO ratio写reference，本文只采reward construction，不把它当已验证oldpolicy/rollout一致目标，不修伪公式执行。候选/初始student/rubric/权重/judge/provider/更新期均需同artifact身份。

## 关键评价、费用及直接反侧

§4两caption数据/50k有限图像训练+500评估；F说50k中hold500，训练分母口径差异保留。Qwen2/2.5 VLM2/3/7B fulltuning，8H100/1epoch/N4/maxcompletion1024/lr1e−5；RLbaselines同trainconfig只reward变，但rubric制备老师/API调用、前置人工/数据、judge身份不同不能授全总预算matched。SFT1epoch并非同rollout/探索预算，CapRL75k与our50k不由少image推降全费。

§4.1 Reference-Likert作者实际描述self-praising shortcut，3B PixMo 7.8%对base/4.0%对humanref的作者文字只支持该baseline/prompt而非所有holisticjudge必失败。RubiCap的CapArena GPT4.1及blindranking是modeljudge偏好，human-expertannotation是被比caption而非同期独立human评审；不同teacher/writer/judge名字不是groundtruth。§4.4 same-rubric SFT学生重写然后imitate vsRL不同训练/rollout，不能独证所有增量归探索机制。wordlimit100–600/CaptionQA Qwen72B为所测文字utilityproxy，非全推理速度/32B完整能力等效。

Table1重caption3.5M/LLaVANeXT/CLIP336+Qwen2-7B的有限pretraining平均41.75→42.99/43.04/43.18，MMMU3B35.22/35.89低于GPT4V36.33，7BMathVistaFormat31.80低于32.70，非所有任务改善。AppH retention3Bbase77.62→76.09/76.03、2B72.16→70.75/70.32，有实质保留任务退步，不能写无遗忘；main十项与AppH九项人口不同，不拼同一均值。未核曲线精数、完整multiseed/CI或teacher独立性，不采用普遍优于人工/闭合verification。

委员会生成、writer图像读取/规则制备、初始student、每rollout逐criterion文本judge与LLM调用、GRPO全训练、heldout/真实图像审核和后续3.5Mcaption全部计费。一次制备是成本前移，后续不调用proprietary不代表全流程无teacher/免费/无需真值；完整precision/endtoendbudget/latency/concurrency/SLO Not Disclosed。不采用额外任务Science应用，只把Table1局部作为跨能力边界。

## 现有owner及逐字PRE

作者actualCh31 145–178（偏好身份/shortcut审计）、245–277（bottleneck→RubricIRT→formatreward→MAESTRO）、275–310（demoderived/consensus gate）、558–578（RewardDAG/自演化）、790–807（compiledreference rules）、1120–1126（policy-relative rubric/holdout）及Ch30/32开篇交接。当前IRT拥有如何把已有criterion pattern测scalar，compiledrules拥有referencekeypoints/regex，但未拥有“teachercommittee与初始student缺口制备逐样本rubric→冻结文本语义judge”的两阶段接口与正确旧项被排除盲区。拟在bottleneck完整费用/回退段后、IRT前两段，不覆盖既有真值/固定聚合与dynamicrule。

拟段1：

聚合之前还要问判据从哪里来。全局质量分在目标稳定、人工尺度已校准时简单，却可能让开放式输出靠自我赞美或表面格式取得高 reward；一个受限分支先为同一输入生成多教师候选，与初始 student 输出比较，只把共识中尚未满足的部分转成带严重度权重的 binary criteria，再冻结为逐样本 rubric。训练 rollout 随后由文本 judge 逐项检查是否表达这些规则，以权重归一的通过率产生 reward；教师与 writer 的大模型调用前移到制备阶段，训练并非每步重新投票或刷新 rubric。这与下文从 verdict pattern 推断质量的测量器不同：这里改变的是评分尺子的来源和覆盖对象，后者消费已经定义的判据。

拟段2：

缺口导向也留下一个新的盲区：初始已经正确的部分被排除，后续补齐全部 criteria 不保证其他事实仍正确，更不保证教师未提到的错误被覆盖。只读规则和 caption 的文本 judge 不能重新看到原图验证事实，共识与匿名教师身份也不认证独立真值；committee、初始 student、criterion、权重和 judge revision 应共同保存，并以独立视觉证据和保留任务验收。原稿的共识阈值与 prompt 口径不同，必须先锁定实际规则，不能自行修成可复现 recipe。[必要方法与直接反侧](https://arxiv.org/html/2603.09160v1)支持有限 caption reward 分支，但模型 judge 偏好和均值提升不授普遍优于人工或无遗忘，部分保留任务仍退步。教师制备、全部逐项评分、rollout/训练与独立审核均计费；规则饱和、遗漏或质量—费用不改善时，保留完整人工 rubric、原 reference/SFT 与独立 outcome gate，再考虑受控更新尺子，不让模型自行宣布 verification 已闭合。<!-- source-family:SF-2026-ARXIV-2603-09160 -->

实际独核：root完整必要§3/4、B/E/F/H及Tables1/5/6、原batch2日期/当前说明与Ch31 242–279、Ch30/32开篇通过。root授Ch31窄锁后作者按上述逐字PRE写257/259两段及1219自身末注，实际顺读245–280完整局部/末注并回对原证。root作为非writer实际同一完整局部、新正文及自身末注POST通过，锁释放。评分2+1+2=5；不授全部曲线、实现/复现或完整SLO/DAY。
