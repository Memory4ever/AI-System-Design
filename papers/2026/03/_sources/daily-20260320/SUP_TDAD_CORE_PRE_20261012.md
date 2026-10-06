# TDAD 2603.17973 — 必要证据与最小 PRE 准备

准备者：resume_review17_18。仅03-20补03-19自然日；原准入/date与2+2+2=6复用[九Agent准入原packet §5](./SUP_AGENT_TAIL_ADMISSION_PREP_20261011.md)，不再发现或改归属。本件是必要Source/actualowner/拟稿准备，**未由准备者自授Source/PRE PASS、safe或DAY**。未改Books/Report/LS/索引、未读代码/实验日志、未复现。

## 1. 实际必要范围与版本边界

恢复时实际重读AGENTS、当前研究合同、Report时间/独立复核/完成条件、Sources使用/每日/arXiv适用部分、Prompt、ROADMAP Ch65–67与Ch78路径、本日README窗口与STOP。只本日既有家族。近期Source为作者论文，不冒独立评估/生产能力。

- [exact-v1 HTML](https://arxiv.org/html/2603.17973v1)：实际§3.1–3.6（HTML L118–170）、§4.1–4.3（172–212）、§5.1–5.5与Tables4–7（213–324）、§6.1–6.4及结论（325–366）。支持拟采用接口、关键评价与直接反侧足即停；不读related work/reference对应论文、代码库/所有历史。
- [current abs/history](https://arxiv.org/abs/2603.17973)：实际标题/作者/完整摘要/comments/history，v1 submitted03/18、v2 submitted03/19；这些不另当首次公开日期。当前无withdrawal标记；Submitted to AIWare2026不是已发表同稿信号。
- [v2必要受影响局部](https://arxiv.org/html/2603.17973v2)：实际§3.4–5.5/Tables4–7（L150–326）、§6.3–7（336–369）。当前摘要省略自动改进10子集数字，但§5.5/T7和结论仍保留12→60/0%；**不是正式撤回，也不是正文纠正**。仅修正拟采用边界，不全版本diff或增加家族分数。

## 2. 必要支持与不采用的反侧

### 机制

v1 §3：Python AST提取File/Function/Class/Test及静态调用、导入/继承等关系；TESTS链接实际来自测试文件命名、逐步prefix匹配、目录邻近规则，不能因命名为TESTS就当真实执行coverage。changed files启动direct/transitive（1–3hop）/file/import四种检索、评分取max并按档位截断（默认至多50）；这些启发式未给完备/概率校准保证。静态test_map.txt源文件→测试文件映射与短SKILL交给Agent，运行时grep并执行相关测试，不是Agent在线查询完整图数据库或测试oracle。

§6直接限制：动态dispatch、monkeypatch、运行时生成代码不在静态索引保证内，仅Python/两个本地较小模型。有限匹配接口可分采；confidence权重、hop数、档位/默认50不授通用精确recipe、无损覆盖或安全性。索引更新/导出/测试执行都付费，GraphDB backend替换不认证部署或pickle安全。

### 评价人口与混杂

- §4：Phase1为SWE-bench Verified前100（Qwen3-Coder30B Q4_K_M、llama.cpp、32K、temp0、每题15min）；Phase2为diversity25（Qwen3.5-35B-A3B 4bit、MLX/Apple Silicon、OpenCode1.2.24）。消费级硬件具体GPU/完整功耗、端到端wallclock、CI/seed及完整索引/执行费用未披露；不能合并两阶段或与外部52/69.2%比同预算。
- Docker harness运行F2P/P2P；**empty patches不参与P2P**。T4 Vanilla→Graph+TDD：generation86→74%、resolution31→29%，P2P tests9245→8536、fail562→155、pooled rate6.08→1.82%；但generated-patch instance regression30.2→33.3%。较低pooled severity不证明每个提交更安全或相同population无回归，不能把少生成patch解释成已核实的合理abstention。
- T5单个astropy案例322→12贡献310/407总体fail下降，测试不是独立等权风险人口。§5.2 verbose prompt/保守性解释缺完整因子控制；§6顺序实验、无正式统计推断/temp0与容器不等所有非确定性冻结。
- T6仍列17/25 generated，却列8/13 resolved-of-generated；13人口未解释，故不采62%数字。总体8/25只承载该25配置表，不授跨模型因果或安全保证，且有基线已解题丢失。
- §5.5/T7自动修改SKILL/索引器与小子集筛选主要按resolution接受/回滚，不见同强度P2P release gate。10-instance caption下28/12等百分比无法按一次10题整数计数闭合；checksum防篡改不证明没有selection/overfit。§6.4明确另有disjoint25，但模型/scaffold/量化框架同时变化，不是同配置独立heldout，不闭合auto-loop因果。v2正文仍如此，不采12→60/0%保证或通用auto-improvement因果。

精确重开需求仅针对上述不采用主张：提供T6的13生成子人口、T7每行实际实例/重复次数/聚合分母与独立heldout；固定同patch/同tests人口下同时给F2P、P2P与生成率、完整搜索和执行成本。有限静态映射接口不等待这些headline闭合。

## 3. actual唯一owner与差额

唯一候选owner：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Agent Regression Testing需要分配EvidenceBudget段。

实际读Ch66 440–500相关完整段（其中475–500恢复定点补读）：现有test revision/requirement/code绑定、breaking/stale/missing、AgentDevel固定case pass→fail、prompt slice不改真实被测source、历史bug/TransFuzz oracle分责、VeriGrey探索及AgentAssay uncertainty-budget与随机audit/固定关键tests。另实际3090–3104的ProdCodeBench reverse diff/F2P/P2P分工。已有论点很强，不重复“不要只看平均”或一般有向图；具体尚无**静态source→test映射传给coding Agent→Agent局部验证→独立完整回归人口**的交接，也没有本证据中empty-patch条件选择/pooled P2P severity与generated-patch风险联合验收的实例。

Actual相邻：ROADMAP Ch65是GPU调度，Ch67是metrics监控，实际章首/问题边界已读；Ch78现有workspace+真实call trace的Rust分支和临时编译反馈，是工具执行/observation接口，不承载最终regression-selection人口。这里的图只作验收候选检索，因此sole Ch66，不复制Ch78的tool executor或新建owner。

拟位置：Ch66 当前AgentAssay两段与`SF-2026-ARXIV-2603-02601`独立marker完整之后（现L497），下一“保留原始trajectory还有一个不同于重复预算的理由”之前。保留原随机audit/critical tests，与后续稀有行为反证/aggregate审计自然交接。只该两段与静态源注，未授锁不写。

## 4. 最小逐字 PRE（待非准备者裁，不是已写）

测试选择还可先服务修复过程，再由独立回归人口验收：对已知代码revision构建静态source→test关系，把changed files检索到的测试映射导出为可grep的文本，交给coding Agent局部执行与修复；图和短操作说明是验证候选的载荷，不是测试充分性证书。[TDAD的受限接口](https://arxiv.org/html/2603.17973v1#S3)采用Python AST与命名、prefix及目录邻近链接，不能把TESTS边当真实执行覆盖。动态dispatch、运行时生成代码和截断掉的测试仍可能漏检；索引revision、导出载荷与实际执行tests须分别保留，局部选择不替代固定关键回归、随机audit和独立验收。小型稳定项目继续运行固定suite更直接，索引和重复执行的费用也不能由静态文件抵消。<!-- source-family:SF-2026-ARXIV-2603-17973 -->

评价这个接口时还须把“生成多少补丁”“解了多少题”“生成补丁中多少发生回归”与按测试数量汇总的失败强度一起报告，保存empty patch排除规则和实际P2P人口。该受限对照中，测试级失败比例下降，同时生成率、解题率下降，而生成补丁的实例级回归比例没有改善；这不能认证每次提交更安全，也不能把少生成补丁解释成已验证的合理弃答。不同模型、scaffold和子集的阶段不合并；作者小子集自动优化仍缺明确分母与同配置独立heldout，checksum不认证抗过拟合。验收人口、关键路径或业务风险权重变化时，回到固定revision与完整测试，分开复查逐补丁风险和失败强度，不让selector或总体均值自行批准发布。<!-- source-family:SF-2026-ARXIV-2603-17973 -->

拟静态源注：TDAD exact-v1 §§3–6/Tables4–7；current/v2仅受影响摘要/§5.5/T7与结论复核。静态启发式source→test载荷与独立回归人口分责；pooled P2P下降不授per-patch安全、跨配置因果或完整覆盖；T6/T7分母和自动优化外推不采。未核可选代码/日志、未复现。来源：https://arxiv.org/html/2603.17973v1 ，https://arxiv.org/html/2603.17973v2 。

等待resume_mar17非准备者必要Source/actualowner/两PRE裁决；准备者不预记整合、已有覆盖或完成。

## 5. 非准备者必要 Source/actualowner/final PRE 审查（2026-10-12）

resume_mar17 实际独读exact-v1 §3.1–3.6/L118–170、§4.1–4.3/L172–212、§5/T4–7与§6直接反侧/L213–366；v2仅受影响§5.5/T7/§6–7及摘要说明，不全版本diff。命名/prefix/目录链接真实静态启发式而非coverage，test_map/SKILL供Agent grep执行接口成立。实际T4生成86→74/解题31→29/P2P pooled下降但实例30.2→33.3；T5 astropy主导、T6 generated17却8/13、T7十题与28/12人口未闭合，均不洗成安全/完整无损或自动改进证明。

actual Ch66完整435–510及3080–3125顺读，Ch65/67入口与Ch78真实workspace/call-trace L125–150已独读；静态source→test候选供开发、独立回归人口验收的具体差额成立，非主题NC或复制执行owner。第2PRE独立heldout已按实际§6.4收窄为‘同配置独立heldout’，承认真实disjoint25但换模型/scaffold/量化框架不闭合auto-loop归因；笔记与完整final句已定点读回，两原literal PRE及静态注有限 PASS。原2+2+2=6保持，未授headline/recipe/发布安全；非准备者未改Books或自授写后POST，root协调窄ownership后再落实。

## 6. root授权后的实际 writer 落实（非独立 POST）

2026-10-12 root确认SGC锁释放并授resume_review17_18 sole Ch66本family两final literal/static窄写。实际写前读AgentAssay完整反侧/02601 marker→稀有审计反证两侧及章末SGC本人邻注；只按§4原两PRE写new499/501（保‘同配置独立heldout’）与static5951。写后实际490–506完整邻接/两正文与章末自身/SGC邻注读回，逐字原PRE保持；scoped diffcheck0，章文件已有38新增行→44新增行，仅本family6新增行。未覆盖任何已有论点，未stage/commit/push。

交resume_mar17一次nonwriter实际正文/完整邻接/静态本人注POST；writer自读不充当独立POST，不提前记safe/整合完成或DAY，不循环修改Books验收身份。

## 7. 非 writer 实际 POST（2026-10-12）

resume_mar17 实际读回 Ch66 完整475–507（含原AgentAssay预算/随机audit与02601 marker、新499/501两段、后续稀有行为反证及完整507段）及5945–5951自身/VeriGrey/SGC邻注。新两正文逐字回对§4最终literal PRE，静态自身源注范围/未复现与原必要证据一致；静态TESTS边不授coverage、empty-patch/pooled与per-patch分母、真实跨配置disjoint25和同配置heldout缺口、费用及固定suite共存界均近文保留。既有随机audit/稀有原轨迹检查衔接未被覆盖，无流程身份改注。限定diffcheck0；本family有限actualPOST PASS，可交root接纳/释放窄锁，不授整日DAY或其余未读候选证据。
