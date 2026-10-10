# 01-16 / UserLM-R1 必要原证与拟处置

root独立题摘准入后，exact-v1 §4.1–4.4、§5.1–5.3、§6.1–6.3/Tables1–3、Limits及必要profile/metric appendix读足。不是仅摘要、未核代码/复现实验。HTML/abs/exactDOI同日保存。

root独立实际§4.1–4.3/4.4/6.2–6.3/Limitations，并实际Ch31多轮分支及Ch66 simulator必要原证/OnlyReport处置核通过。保6分/准入，不称同实现已有覆盖或真人胜出，非DAY。

## 实际机制

静态profile role/background/style与scenario动态primary/secondarygoals、trust/emotion/patience/participationstate分离；每轮先goal/rationale五subtasks，再生成response，state抽取进入下轮。SFT→GRPO mixture rewards包含think/answer格式、reasoning-lengthpenalty、缺state字段扣分及目标、persona、thinking-responseagreement/anti-manipulationrubric。可操纵的simulationpolicy需要版本化，但格式/state字段不认证真实人类心理，rationale也不是内部faithfulness。

## 对照及限制

Qwen3-8B/32B，3epochsSFT/8rolloutsRL，GPT4o构造/judge共享，hardware/precision/wallbudget/seeds未披露；1440tasks/120sessions、220adversarial=11traps×20，中文+SOP合成population。32B sessiontotal73.49与DeepSeek73.56相近，8B65.79低；三人工ratersκ .63/.72，32B对DeepSeek sessionwin/tie/loss44/28/48（loss多于win），不能用turnlevel收益掩盖session。Sequentialablations目标、SFT、RL及budget同时变化，不能授dynamicgoal单独causal；§6.3 downstreamAgent训练比较未披露真人结果分布，不授生产环境校准。暂无lifelongepisodicsemanticmemory。Profile生成、rationale/response、state抽取、rollout、rewardjudge与人工校准都有成本；state/goaldrift、共同judge或外部效度不足时保留固定script/真实用户切片及独立outcome核。

## Actual owner comparison

拟2+2+2=6，标准完成（非自动深入，只在若选写gap后扩必要标准），拟仅报告。已读Ch31 L164–183已明确多轮分支user identity/history/simulator/candidate/rubric共同冻结、不同userfollowup非action counterfactual；Ch66 L1268–1285明确不合作persona、realism/diversity/taskoutcome与human–proxycalibration分账。**不称已有UserLM训练实现**，其特定traineduserpolicy的dynamicrationale主要提供局部实现/压力，尚无新的稳定状态commit或真人外部校准机制值得加入这些充分正文。root可独立决定是否存在更窄trainingstategap；不因为“环境模型能映射”强行写。

日期：submittedJan14T06:42:01Z仅发现，官方正常公告Jan15下界+exactDOIregisteredJan15T02:40:50Z公共存在上界，非registered=first-public。没有直接作者project/release链接、无已见早正文信号；不作全网无早稿断言。
