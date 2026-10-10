# DeAction08995：必要Source/owner/PRE请求

When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents，2602.08995v1；2+2+2=6，具体动作aligned≠最优/无攻击≠无偏离、检测/归因/纠正人口与叙事上下文的资格差额深入。root完整AB/日期已过，core完整§2–5实际读；deaction-direct.txt必要A2/A4/C/D/E1/E2/E4。当前abs展示v2Jun25不据版本号开启旧revision遍历；本日仅v1，未核artifact/复现。

§2动作需服务userintent、不带unauthorized consequences、合理直接/间接贡献；低效/探索/不成功仍可aligned，不能把每一步非optimal当offtask。三类externalmalicious/internalharmful/internalnonharmfulirrelevant分开。§3 558traj2264steps：1264aligned/1000misaligned，562malicious/210harmful/228irrelevant。成功攻击trace经benchmark evaluator筛后收集；内部failure由13templates独立执行subgoal再插入 benign trace并whole replay，不是自然部署事故人口。三人行动label，kappa.84 majority，先滤wait/emptyclick；A4 annotation GUI可见immediate postaction截图，detector只有pre-exec，因此标签用outcome信息不证明preexec可推全部效应。

§4 cheapfast-check一行rationale筛clearlycanonicalaligned后bypass，其他走Injection/ActionUnderstanding/OutcomePrediction/Misalignment四个组件；每步executed(o,a,o')作natural-language叙事摘要，parallelwithagent只是作者安排、不授所有server无额外latency或没有stale风险。flag后feedback提示revision，再检最多3，不等authoritativepermission或所有corrected有真实task/safety效果。外部新query/低效探路的reasonablycontributing须保留，不能窄intent导致误拒。

§5T3 QwenVL32B F170.7<89.95‘over15 pp’标题普遍叙述，maxbaseline61.6 gap9.1；Claude80.4−66.6=13.8，Instant79.4−65.1=14.3，Thinking82.8−66.9=15.9，只部分>15。T4 F1two79.9<systematic80.1，precision85.4<85.8，latency11.3vs13.1支持有限tradeoff不是sameperformance guarantee。C2 stratifiedtrajectorysource抽566steps(242misaligned/324aligned)，非全2264，step抽样不授wholetrajectory稳定。history比较41summarytokens vs>1k/screenshot，inputstate不等信息量。E1 detection recalls malicious89.86/internalharmful73.81/nonharmful67.70；分类只flagged且excludealigned，一对其余onevsrest，不能当全人口分类可靠。

Online RedTeam50最高历史ASR任务，max50steps；OSWorldmax15且nodefense直接leaderboard不freshreplay，model snapshot/repeats/CI/precision/fullSLO ND。GPT5.1Instant为guardcore，只有OpenCUA72B比较全部defenses，3correctiterations。ASR T5 60→6 exactly90%(不是strict>90)、42→4、32→2；UA原表OpenAI82→84，Claude44→76，OpenCUA48→60<InferAct70。benignClaude42.9→40.7退步，not zero utility harm。7.2s/28.06s mean25.7%启用后运行时间组成不是nodefense因果开销；36.56%adversarial/47.5%benignfastapprove不同人口，78%是flagged后revision alignment sensor not independentactualimpact。主method已有误grounding、错outcome与过窄taskrelevance反侧，足够停止不展开所有附图。

actualCh72 2587–2614预测风险sensor/独立effectcommit段已读，只有worldstate轨迹risk，没保三类offtask且alignment≠optimal与fastbypass/narrative/revision的具体资格分责；DeAction只出现3484来源清单不是actualbody覆盖。Ch78 preventive/evidential、anchor/declaredscope、canonical action与computerstate是执行contract不是本测量人口；actualCh71/73入口核。唯一PLATFORM-SECURITY Ch72，拟紧接predictiverisk段后，避免另写Ch78。

拟正文：动作风险的观测还要区分外部恶意指令、无攻击时的内部有害偏离和不造成直接损害的离题；探索、低效或暂时失败并不自动违反用户意图。一个受限检测分支先让轻量检查筛出明显与任务一致的动作，其他动作再按注入线索、动作语义、预测后果和意图关系分项检查，并用已执行transition的叙事摘要维持历史；发现偏离后给结构化反馈，让新proposal重新过门，而不是以一句blocked结束任务。新增的是这一测量/恢复路径，不是让模型获得effect权限：快速bypass会漏掉伪装为任务建议的注入，摘要与坐标grounding可能失真，过窄意图还会误拒合理的回轨动作。应分别验检测、flagged后的归因、revision一致性和实际任务/安全效果，保合成偏离与真实失败人口、pre-exec观察与事后标注资格。额外摘要、深审与重试都付费；来源或intent不确定、预算耗尽时停止自动修订并交独立policy/人审，不能由低ASR或自我纠正授普遍安全。

请求root实际Source/owner/PRE，必要通过后再协调Ch72窄锁，当前未写。
