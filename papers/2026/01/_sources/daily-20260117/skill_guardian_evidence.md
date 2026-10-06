# SkillScan / AgentGuardian：必要安全证据待 root 核

两项已题摘准入；以下exact-v1实际必要方法/评价/直接反侧，未核实现/复现。2+2+2=6，安全受影响范围深入，不以31k规模/方法pipeline计贡献。

## 10338 SkillScan — 拟具体 Existing

primary actual §3.1 L420–459、§3.3 L500–679、scope1036–1043、§5/Limitations1131–1146、AppendixE1743–1758。SKILL.md+bundledscripts不是单纯描述，static(v1.2)/LLMGuard(.3.14)union→Claude3.5 T0 classification，confidence.6确认/.8覆盖static，危险pattern不等malice/exploitation。taxonomy500/calibration300/validation200 disjoint，后两者source/structure分层；200的63positive，两researcher+第三裁决，kappa.83/.79。IPW source参数只能处理已声明sample设计；aggregate86.7precision/82.5recall，category CI10–14pp不可推类别性能。T0 classifier三运行94.5%、三prompt91%，共识≠truth。

December2025 two-market snapshot42,447→31,132English≥10line，4047353 excluded，survivor/missing-script去重条件影响人口。26.1%是flagged mixedmalice/negligence/ambiguouspattern、不是全pop confirmedattack/vulnerability。categorized1218的38.7%非31k人口，source/structureIPW27.3%不证明detector类别均准。pilot25 highseverity+confidence≥.85+clear credential/egress，Docker+tcpdump/auditd18confirm/4uncertain/3legitredteam，72%不能外推所有flagged、更不能认证intent。FalseFN dynamicURL/自然描述/延时trigger，FP legitsecurity/telemetry/docs examples。各扫描/Claude/annotation/runtime成本未给e2ehardware预算，不声称可部署全popscan安全。

actual `PLATFORM-SECURITY` Ch72 L2239–2241正文具体已承载自然语言+脚本+permission fact/source-sink、examples/templates可被执行、stdout回灌、static审计不授runtimeauthorization/market统一risk，真实effect-time gate/沙箱不可替代。不是同名主题匹配，也不假称已有本论文统计。可采用长期边界已覆盖，新的Dec snapshot与分类测量局限仅报告；拟6安全深入完成Existing请root终裁，毋需新正文。

## 10440 AgentGuardian — 拟Ch72两段 learned-policy差额

primary actual IV105–279（IVB cluster/rules166–250、enforcement277–279）、V280–321、VI332–366/VII367–373。staging假设全benign→按出现的tooloccurrence/transition提CFG、每tool/context分组embed150D文本+normalized numeric→cluster→Sonnet4.5 regex聚合+numericminmax，pertool (allowedpath) AND union cluster(text ANDattr)。具体新增是训练/部署分离的轨迹→scope/规则接口，不授有限trace包含所有合法flow，也不把cluster内语义等于authorization。thought/taskresult与clock仅日志字段，不当不可伪造特征；runtime当前已知input/已完成结果边界须校验，不以未来OUTCOME提前放行。LiteLLM feedback alert/中断/关键terminate说明未核tool前原子interposition源码，不能将反馈当不可绕过effectgate。

每app100benign→60staging/40test+10misleading，两app GPT4.1、policyregexSonnet4.5。aggregate80benign/20bad，18/20捕获(FAR.1)，FRR.1、BEFR.075另人口；paper把benign hallucination failures单列且另建议部分FR移BEFR，不能重标成全部utility通过。10samples regex近乎任意text/60更紧只是所测例，moredata并非自动更安全；time外numeric允许2倍，合法长输入可拒。GPT4omini24/13误流程同时污染trainingpolicy，不能归架构/规模causal。作者不能改T/topp、precision/GPU/e2e与policygeneration/monitoring预算ND；no matched baseline/CI，2apps合成scenario非实际未知生产攻击分母。regex不能可靠分辨恶意自由文本、staging污染/rarevalid缺失正是直接反侧。

actual Ch72 L1190–1194已有independentpolicy/预观测CFI branch与authority边界，L2239–2241有staticfact审计，不含benignstaging→perroletoolcontext derivedCFG/clusterregexnumericpolicy的有限support+更新版本。拟在preexec/CFI分支附近两短段：学习到的是候选policy support非真实权限，trusted staging/版本/人工确认/更新离线，缺失flow不自动恶意，percontext/utility costs与immutable authority/effectcheck退路相邻。请root必要IV/V/VI/limits+当前owner核后授锁，不扩无关relatedwork。

日期原字段另见jan17_all_date_fields.json。两项正常Submitted落cohort+公告条件/register上界完全落窗，写报告时逐项ISO范围，不把Submitted当public。
