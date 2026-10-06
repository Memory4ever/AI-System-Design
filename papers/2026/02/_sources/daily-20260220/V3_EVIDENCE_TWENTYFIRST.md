# 02/20 第二十一有限证据包：SPARC / Calibrate-Then-Act

仅本日16671/16699，沿首包已独核announcement→same-ID DOI橋接，公开下界2026-02-19T09:00:00+08:00，上界Registered+1秒分别10:52:03、10:52:45。原字段保各DataCite文件。官方v1事件页本轮轻查，无可见撤回/勘误，16671仅v1；16699有Feb19v2/May15v3，版本号本身不证明重要，当前页无具体改变本次claim说明，不借后版内容/不做广泛revision比对。完整题摘已实际读，精确HTML本地与抽取命令沿前包，不运行artifact或复现。

## 2602.16671v1 — SPARC: Scenario Planning and Reasoning for Automated C Unit Test Generation

**准入定界：**一次core原来待具体grounding与反侧；现在actual §3明确保signature、helper描述与独立path atom，而§4.3直接观察repair使assertion适配trivial input、test通过却不覆盖algorithm，支持“修复可执行性与原检验义务分开”的具体反证。不是只TDD/CI改名，拟2+1+2=5，差额深入；尚待root独校/必要源/owner PRE。

实际core109–171、setup472–488、fault616–644、userstudy647–673、cost883–910。原函数/头文件与curated helper pool经cosine检索后，LLM构建operationmap；newhelper code仍生成，复制给各path后独立修复，最后merge。每path最多3repair，compiler和ASan只检测给定program/tests的语法/运行错误；原定义paths可行不保证extractor真穷尽（5.3% dropped是unreachable）。生成的helper名称/arity仍是近2/3 dropped错误，94.3%保留不等原语义或全路径正确。

51algorithm+8Rustine项目，但排I/O、mocking、main/harness并改static；vanillaDS一次prompt无CFG/operationmap/iterativerepair，调用预算并不匹配，KLEE不同执行路径亦不授纯单组件收益。Mull局部mutation score不等真实bug检出/完整oracle；qsort相同coverage的6点反侧支持coverage不充分，不唯一证明scenario因果。10人/150pairedrating独立性受共享rater/item影响，Alpha0.08–0.32，不以显著性认证客观correctness。inputtoken约12,152/test，约22.1%validation，pathcostquadratic仅拟合且不等全wallcost。10project Gemini/GPT平均近DeepSeek不授任意底座无损（Qwen8Bstructured失败），T0也不证明API确定性；hardware/precision/并发/SLO与重复seed/区间不足。

**具体缺口：**AGENT-REFLECTION Ch80:51–64有deterministic反馈、formaltranslation忠实性分责，72–74有反例query而非当前hypothesisconfirmation，仍未明确**同一模型修复自己生成的测试时通过修改inputs/assertions缩小原检验义务**。拟在formalverifier段后补一窄条件分支：生成test是proposal，保目标path/独立预期与helper版本，修复可执行性不能默许改oracle或退化输入；compiler/ASan pass与实际coverage/semanticassertion分账，测试目标独立校核是工程要求不冒称已实现严格gate。额外path检查、sandbox/repair费用、unreachable/不完整oracle与固定人工test fallback近文。无需把全部C框架写书，求Ch80该段/末注锁。

## 2602.16699v1 — Calibrate-Then-Act: Cost-Aware Exploration in LLM Agents

**2+1+2=5；显式校准环境prior接口差额深入，拟窄整合，待root必要源/actual owner PRE。**

实际core89–150、QA/code202–257、setup261–283、matchedresults298–374、AppB909–910和C913–963。成熟POMDP/VOI不算新贡献；具体增量把uncertainty estimation从actionpolicy显式解耦：QA verbalconfidence用validation isotonic校准，retriever-after-answer quality为validation估的全体常数，非query-specific真值；CSV filename→BERTtiny(4.4M)三independentmarginal，oneepoch，67%属性平均accuracy，值传给prompt或RLpolicy。上层仍只是proposal，prior不是当前observation。QA oracle `γ p_ret≥p_da` 在其单一质量/成本抽象下，不授开放多次检索最佳停止。

Qwen3-8B，PopQA1000，γ0.1–0.65；CSV2000/1400train/300validation/300test，由16binary filenamefeature人工induce因子formatdistribution，unit-test直接返回选择属性真值，非真实测试任意代码。相同RLdata但CTA另付prior-estimator训练/校准与promptcontext成本。Pandora100/3box有explicittrueprior，94%match不证明估计器一般校准。QA reward0.293 vs0.283、小模型NT差异不能仅归prior信息因果；代码CTA-prompt accuracy0.945低于base0.958，CTA-RL0.991低于RL0.997，reward0.268高于0.259，是合成discount取舍，不是无损准确率或实测费/时延Pareto。代码testρ1.5与mainaggregate表ρ1.0口径差异保留，不把所有curve权重视同一分母；mean/单实验缺seedCI，不授显著泛化。

**实际owner差额：**AGENT-PLANNING Ch79:52–59已有可查latentstate/observationbudget，未承载**环境prior estimator与action policy分开校准、显式传distribution/成本**；不是只增加更多query。拟在此后加一段：有稳定可核任务分布时先估latent属性或继续获取证据后的成功分布，给selector与行动cost竞争；可通过validation校准而非读verbalconfidence就commit。分布与estimator/model/schema共同绑定，额外标注/训练/calls也算成本；有限synthetic/task evidence不授普遍最优，shift/不可靠估计时取真实observation、固定test-first/检索或人工。sharedbudget/事实提交保持既有owner，不写新结构。

## 当前边界

该两项仍普通待办，不计终态；二十包另待PRE。当前README76 / 45POST与普通20保持，不授整日。Ch80/79拟写都需具体授权锁后才写，无stage/commit/push。

**后续独核结果：** root 两项准入/必要源/actual owner PRE通过并授窄锁；实际 Ch80:64/56–73邻接/自身末注432 与 Ch79:60/48–69邻接/末注544 已 root POST 通过。两锁释放，16671/16699 均5分差额深入整合终态；原义务/先验权限、proxy成本与回退近正文。未运行或复现，不授整日。
