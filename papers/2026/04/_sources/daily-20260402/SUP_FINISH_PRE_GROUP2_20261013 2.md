# 五个已过必要Source的窄PRE（未写Books）

只本日旧材料，不扩发现。原必要Source及反侧复用STOP §9.15/9.17/9.19；作者actual当前Ch79 70–112、Ch75 555–590、Ch81 1–48、Ch66 267–308、Ch78 233–270完整相邻。每项只一段/本人注，不替换原文；root未授锁，不写共享Books。LTG/Skill/Eco/APR正常paper日门复用§9.29；SemLoc原DATE另须根/reader必要复合门确认，不从PRE授日。仅接口长期差额，不采全部recipe/性能/安全保证。

## LTGDroid 29623 — AGENT-PLANNING / Ch79

在“学习到的Transition”两段及其end marker后、“缩小action分支之前”前。现有parametric估计不是可恢复sandbox真实trial；保持后续partial-action支持论点。

~~~~markdown
若环境能被可靠隔离并恢复，还可先获得真正的局部transition观察，而不只预测它：从当前界面提议有限动作，逐个在沙箱中试执行，保存前后screen与Activity，再恢复同一snapshot，才把这组观察交给有界路径搜索。筛选后的动作不是全部可行支持，LLM生成的变化摘要也不是原画面真值；snapshot恢复更不覆盖外部服务已经发生的副作用。[LTGDroid的受限对照](https://arxiv.org/html/2603.29623v1)支持这种pre-assessment分支，但75reports/45apps排除特殊初始化、filter漏动作与不支持的gesture限制可达性。较高成功率付出更多trial、restore、调用与等待，原无预评路径更快；100动作/60分钟上限是本配置预算，不是开放环境可解保证。恢复不完整、观察/摘要不可信或总费无益时，保留当前真实观察、短horizon/直接执行或人工排障，不从沙箱试成功批准真实effect。<!-- source-family:SF-2026-ARXIV-2603-29623 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29623` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29623v1)IV-A–C/Alg1、V-B/D/E/TIV/VI，2+2+2=6，仅XML/LLM有限候选→真实trial/screen-Activity→snapshotrestore→有界BFS接口。保75reports/45apps、GPT4.1/MacM4/Android9/三run、100action/60min、filter/gesture漏失、7.96min68.44与20.45min87.51及全部试用/恢复费，不授外部副作用回滚、全支持或安全；未核代码/复现。
~~~~

## SkillReducer 29919 — AGENT-CONTEXT / Ch75

在“Context Compression必须保留执行状态”首段后、PABU阶段状态段前。已有同状态续行动验收，但没有shadow routing→实际trigger→恢复/原文fallback双consumer。

~~~~markdown
压缩可发现的skill还须分开路由与功能消费者：先让一个只含描述的shadow skill模拟与原文的竞争，提出更短的触发描述，再用真实router在指定query子集核是否仍会调用；失败时有限恢复原描述或直接回退原文。只有路由资格通过，才分别压正文/引用并验证实际任务。[SkillReducer的受限协议](https://arxiv.org/html/2603.29919v1)把这两个消费者分开，却不证明模拟judge与真实router等价或任意query触发不变；536/536包含39次原文fallback且排除了原失败人口，任务与同预算切片仍有反退。压缩、模拟候选、真实调用、恢复、引用读取和任务验证全部付费，Stage2保留当前best也不能认证无损。Router版本/query支持、正文功能或净预算失配时，恢复原skill和完整引用、保留人工/真实任务回归，不以描述相似或触发一次批准全部能力保留。<!-- source-family:SF-2026-ARXIV-2603-29919 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29919` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29919v1)IV-A/B/Alg1–2、V-A–C/TIII–V，2+1+2=5，仅shadow模拟→real trigger子集/最多三restore/原文fallback与body-ref功能分验。保536含39fallback/排64原fail、Stage2 best<1、14%反退、同50预算.909<.921及全部制备/路由/读取/验证费，不授任意query/完整faithfulness；未核代码/复现。
~~~~

## EcoScratch 29624 — AGENT-WORKFLOW / Ch81

在“长期任务需要event/state persistence”后、“State Machine是基本模型”前。现通用policy/budget/retry责任尚不承载同一probe绑定三个修复预算选择。

~~~~markdown
资源策略还可以先在同一修复轨迹上支付短probe，再冻结一组联合预算：用有gold/test支持的初始尝试估计任务状态，按固定阈值一起选择证据输入、JSON操作上限与便宜precheck或完整verification，而不是让三项各自独立放宽。这份probe产生后续控制提案，不拥有任务真值，操作格式正确也不等修复正确。[EcoScratch的受限对照](https://arxiv.org/html/2603.29624v1)支持此联合接口，单trajectory/缺重复CI、provider漂移和严格验证的质量/费用差额仍须保留；host-only能耗与fallback估计也不包含remote推理。Gold/probe、证据制备、模型、所有precheck/full check和恢复均计费，固定/text-only仍是便宜分支。Probe不完备、阈值漂移或验证不可靠时，回退固定预算、原证据与完整独立验收，不让估计较省或syntactic patch自签成功。<!-- source-family:SF-2026-ARXIV-2603-29624 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29624` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29624v1)S3.1–3.5/Alg1、S4/6，2+2+2=6，仅same-trajectory gold/test probe→evidence/opcap/verification三项绑定。保12API×四mode×100/4800、MacM4/16GB、singletrajectory/noCI、provider漂移、30.3vsstrict8.0与hostenergy非remote全账；制备/调用/恢复全费，不授视觉唯一因果或完整正确/安全；未核代码/复现。
~~~~

## APR Headroom 29067 — PLATFORM-EVALUATION-SYSTEM / Ch66

在“主动获取信息的任务还要把采到什么/怎样解释分开”SF2602-08693完整段后、VAEX构造段前。其通用oracle差额未承载nativewrapper/sharedbuilder×withinpool×tokenmatchedwrongconstraint测量。

~~~~markdown
差额诊断还须固定真正消费证据的builder，而不把更好的输入自动归成模型能力上限。代码修复可先在原native wrapper中替换定位证据，再用共同builder比较生成接口，并仅在固定已生成patch池内检查oracle选择；三项分别测获取、消费和已有候选选择，有限池饱和不等所有搜索的上限。增加证据时，以同token数filler和同仓库wrong-issue条件作配对，才能区分内容冲突与纯长度压力。[受限RAG-APR审计](https://arxiv.org/html/2603.29067v1)仍有oracle替换后退步、union-context与多轮结果union不同预算以及“十次都稳”到“一到九次”的回归；test passing也不是完整语义或生产验收。Oracle、十patch生成/检查、额外证据与builder迁移均付费，wrapper/候选池/任务人口不匹配时保留原native任务结果、固定池界限和独立检查，不以一个oracle数字批准通用recoverable headroom。<!-- source-family:SF-2026-ARXIV-2603-29067 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29067` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29067v1)S4.2–4.5/5.2–5.3/T1–4/5.5.4–5.6/Threats，2+2+2=6，仅nativewrapper/sharedbuilder、K10 fixed-pool与exacttoken wrongconstraint分层headroom。保300SWEbenchLite/oracle losses9/13/24、180vs196/177vs189预算差、稳定反退及全部生成/证据/test费，不授任意search上限或语义生产正确；未核实现/复现。
~~~~

## SemLoc 29109 — AGENT-TOOL-CALLING / Ch78

在Debugger局部条件/回退完整段后、visual-call utility段前。现tool gate只分诊断调用/证据/修复，不承载per-test semantic spectrum与受约束patch实验接口。

~~~~markdown
诊断也可把自由语义假说绑定到程序中可执行的锚点，而不只返回可读解释：将候选性质映成闭合typed schema，在每个test上检查相应constraint，再把违反谱用于定位、生成一行patch并重跑。[SemLoc的受限方法](https://arxiv.org/html/2603.29109v1)增加了可被反驳的中间对象，却不由typed grounding认证root cause；原算法只据已失败test分类，可能忽略原passed的新回归，passing中已违反的条件与primary定义也不一致，因此不能照抄成充分修复recipe。250个单函数/单故障Python与少量可执行真实issue不授任意repo，文字匹配、可执行约束和完整任务成功须分验。假说生成、schema/constraint执行、patch及回归全费；接受修改时应另跑原passed和完整独立suite，这是一项工程验收要求，不冒称作者已经实施。条件、锚点或测试支持不足时，保留原源码/trace、传统谱定位与人工验证，不由更高定位分数批准semantic或production正确性。<!-- source-family:SF-2026-ARXIV-2603-29109 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29109` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29109v1)S3–5，2+1+2=5，仅typed anchor→per-test violation/Ochiai→one-line patch/retest接口。保原Alg1只failed tests/C3 passing冲突/Table5 Acc@3口径、250单函数/68of463 executable/7youtube完成子集和全部制备/调用/回归费；whole-suite验收是工程要求，typed非causal truth，未核代码/复现或任意repo。
~~~~
