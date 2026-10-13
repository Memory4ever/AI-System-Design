# Test Evolution necessarySource / sole Ch66 两PRE

2026-10-12，[2603.23443v1](https://arxiv.org/html/2603.23443v1)原2+1+3=6/day25保持，设计反证必要深入actual§3–7/T1–2/Results/F4–9文字。无需全部原程序/figure点值/code复现，支持/直接反側足停止。

## 独立设计命题与限制

生成suite仅从当前implementation，不给原版本context；freshindependentinstance+两shot compile repair在各phase相同。先从CodeNet5723(Java3231/Python2492)可独立compile/run程序中按LOC四quantile抽样，**每model100完全passbaseline/各quartile25**再各14changes(5SAC9SPC)。这是permodel成功条件人口，不是800相同程序或5723全通过；筛到baseline100%不证明complete理解或保证后续所有退步纯mutationcause，randomvariation/selection/confounding未控制。22,374generationtasks/346Mtokens整pipeline不是每model独立replicate，也不是acceptedvariants同基数。

SAC boundary/operator/argument/rebind要求新输出，SPC structural/name/comments理论保留行为；改变平均1.0 vs2.4lines(max7)不相同编辑强度，不由词面差自动证明memorization/内部算法。SPC unusedparameter签名改变甚至可能破坏externalAPI，必须绑定closedselfcontainedinput/call适配；baseline有限tests pass不能证明全semanticequivalence。Threats337“updated对originalbaseline然后100%onoriginal”的文字未给完整equivalenceoracle，不自补。原selfcontainedJava/Python非任意multi-file/真实PR安全。

failureattribution：**只失败在newcode的generatedtests**回跑oldcode，且覆盖mutatedregion仍failnew/passold，则标residualalignment。119163testcase中23977failnew，23737满足原说criteria，“>99%”分母23977失败tests，不是alltests/tasks/model99%盲从旧逻辑。差分执行提供旧行为相容signal，仍不识别pretrainingmemories/causalmechanism，也不授oldbehavior一定应保；应由外部需求选哪版真值。代码新版只是intendednewbehavior的一种输入，tests都pass当前implementation不证明bugfinding/developerintent，§7construct明确。

SACavgpass66.5从100原文33.4pp实际33.5，不擅统一；SPC78.9写21.0实际21.1，保持局部非exact数字保证。SACcoverage79.3→67.4/76.1→60.6，SPC73.7/69.2有限聚合、permodel100成功人口不完全matched。Noindependentrepeatseed/CI/temp/tokenlimits/preciseprompt/version/runtime/parallelSLO披露；L40S本地两open(20B30B) vs六API，不推hardware或modelsizecausal。Table2GPT5 vs§5GPT5Mini身份未闭，不合跨model精确rank。Java/Pythontyping/trainingcorpus解释只有猜测非控制实验。

所谓testmatched由**覆盖相同代码lines**定义，不是同assertion/inputs/oracle或行为真等价；fresh每变体完整再生成、没给oldtests，不能把新/丢match当已维护/删除现有tests或微调“adapt旧suite”性能。Humanindependentdeveloperintent/mutationkill未测；2shot/失败过滤、全部baselineattempt、changes/check、生成/执行/coverage/双版本归因全计费。独立SPEC/diff显式标注/静态分析属于future，不声称已实现修复。

## actual owner 差额 / 锚

actual Ch66完整255–335 subject/harness/freshpaired与TRACE、SpecOps/VeriEnv两完整段、104–120EvalSpec，65/67开篇；现SpecOps绑定setup-prompt-oracle和VeriEnv共同生成偏差没有具体声明**当前code生成tests的执行覆盖≠assertion/需求，失败case旧/新版差分与changedregion归因必须分母条件化**，真实长期gap。sole PLATFORM-EVALUATION-SYSTEM Ch66，不为普通softwaretesting新增项目路线，采用LLM-evidence生产者/验收设计反证。

拟SpecOps10268完整第二段末“不要让测试者自行修复被测结果”边界，精确原句“……不让测试者自行修复被测结果。”之后、下一“真实网站不能安全反复探索……”VeriEnv完整段之前两PRE+本人注。不动oldSpecOps/VeriEnv/原ModelSpec块。未独核/锁/写。

## 两逐字PRE

当 LLM 从当前代码生成测试时，还要分开“执行了哪些路径”和“assertion 对哪版行为成立”。一个受限诊断先在原程序上取得可执行且全部通过的 baseline，再分别施加预期改变行为与预期保持行为的变体；对新版失败的测试，回跑旧版并检查是否实际触及修改区域，才能提出旧行为残留的候选解释。这个分支补充覆盖率，不让 pass-current-code 或更高覆盖自签开发者意图；哪版行为应成立仍须由独立需求或 oracle 决定。<!-- source-family:SF-2026-ARXIV-2603-23443 -->

全通过 baseline 只是筛选后的条件人口，不认证完整理解；旧测试全过也不能证明所有重构语义等价。相同代码行覆盖不等于输入、assertion 和期望结果相同，重新生成的 suite 变化也不是维护原 suite 的效果。有限自包含程序、不同模型各自成功样本和不同编辑强度限制因果外推，双版本恢复比例须只按其失败测试分母解释；制备、失败尝试、两轮生成、执行、覆盖和差分检查均计费。需求、等价性或归因证据不齐时保留原回归、可执行差分与人工审查，不由 mutation 数、总 token 或局部一致性批准任意软件变更。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23443` — [Test Evolution exact-v1](https://arxiv.org/html/2603.23443v1)必要§3–7/T1–2/F4–9文字；仅新旧程序差分/changedregion与生成测试oracle分责。保成功条件人口、SAC/SPC非等编辑/等价未证、>99%失败分母/coverage-match非assertion相同、freshgeneration非维护、文数字/模型身份未闭及全费；不采memorization因果、全bugfinding/真实PR安全，未核全部程序/code/复现。
