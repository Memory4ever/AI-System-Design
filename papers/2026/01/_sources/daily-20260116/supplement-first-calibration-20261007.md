# 01-16 补查首批准入包

仅补遗漏，新增窗口BJT2026-01-15自然日；旧86候选与日期/评分/证据全部保留。原报告baseline已存。本文是作者拟判，等待root独立准入校准；不是证据/Books验收。完整精确v1题摘存 `supplement-20261007/abs<ID>.txt`；09295的v1正在捕获。Atom `published`只作提交缓冲（并实际验证响应范围），绝不直接当公开日。

## 拟继续（先准入后评分）

1. 2601.08991 ECOpt：参数/FLOPs作为能耗proxy可能误导配置选择 → 把实测inference energy与质量放入双目标优化并披露优化开销，局部Transformer与CNN对照检验proxy → 需重新考虑只按FLOPs/吞吐选配置。局部反证也能准入，尚不采用“跨硬件一致”或生产节能保证。
2. 2601.09215 UserLM-R1：静态profile、易被Agent操纵的模拟用户影响训练环境有效性 → 静态角色与动态goal分离，先goal-driven rationale再response，以多reward训练策略并测adversarial set → 需重新考虑把用户模拟器当固定可泛化environment。未授真实human fidelity。
3. 2601.09250 FairToT：uniform corrective prompting增加成本且可能引入偏差 → entity substitution形成局部/全局敏感度观测，再决定是否执行再评估 → 需重新考虑“何时纠偏”的条件门与整套population/成本，未授普适公平或label truth。
4. 2601.09295 MACRO-LLM：邻居未来动作不确定与空间局部观察相互耦合 → rollout proposal/reward交给mean-field negotiation，再用drift归因修正 → 需核实际共享统计对象是否改变协作协议，而非只是既有步骤新命名；决定性方法若无新接口/失效证据才关闭，不能因为深审费时缩池。只核通用多Agent/物理控制，疫情应用不准入。
5. 2601.09487 SlidesGen-Bench：代码/图像终产物异构令评价不可比 → 统一rendered输入再分别计算content/aesthetic/editability并用human preference对照 → 核实是否发现视觉分数与实际编辑能力的盲区，不因为是新benchmark准入，不照录human correlation headline。
6. 2601.09527 Blackwell：单资源选型/电费账可能掩盖SLO与量化质量 → 同4模型/79配置跨consumer hardware/context/任务实测 → 局部质量/资源边界可能改变配置选择，必要核真实实验条件、反退与全成本；不授“可替代云”或隐私/生产保证。

## 代表性关闭与定点信号

- 2601.09113 AI Hippocampus：完整题摘仅implicit/explicit/agentic taxonomy、architectural advances/开放挑战整理，无新增验证或机制边界，不因能映射Ch77收录。
- 2601.09059 multilingual translation/distillation：已有forward-translation→2.55B distilled generation→back-translation用于health shared task，任务winrate并非新蒸馏机制或可比成本/边界；贡献前关闭，不追其不影响处置的公开日。
- 2601.09771 PCN-Rec：recommendation场景中已有JSON claim→deterministic verifier→greedy repair→reverify流程，98.55%对无验证baseline不能隔离negotiation独有贡献；完整题摘尚无改变基础执行选择的增量，关闭，不冒称全paper已读。
- 2601.09152 PrivacyReasoner：个体privacy concern预测的comment-derived memory/context filter，完整题摘主要humanlike理论包装/LLMjudge得分，无独立新的可靠性/写入接口；拟关闭。若校准认为“task-specific认知模型”的实际边界值得继续，再定点核心。
- 2601.09365 Frame of Reference：建立relational reference任务并比较common-ground表示/合成RL；题摘没有具体新增表示机制或发现何种失效边界，拟关闭；不把generic grounding主题当贡献。
- 2601.09760 Tool-Memory Conflicts：负面结果具潜力，但abs明确R2-FM ICML2025；先定点检查Workshop早正文，不能把Jan14 submitted当first public。
- 2601.09770 GUI-Eyes、2601.09775 tropical theorem、2601.11641 MOD-DiT：潜在机制/理论/成本delta保留，较晚编号需日期元数据，日期不明留具名缺口，不删为zero。只读必要date，不扩大窗。

## 入口边界

四主题API（model/system/multimodal/agent）submittedDate:[20260113 TO 20260115]；分页0/100/200，total分别267/16/85/274，逐entry submitted字段范围均通过。以正常cohort Jan13T19Z～Jan14T19Z作发现routing，104未读标题仅库存线索，不构成104题摘/全文队列。旧119题摘精确身份用于去重，旧审阅不重读。

官方月列表正格式为 `/list/<cat>/2026-01`，原缩写2601返回404已纠正；CL skip750/show250、CV skip600/show250及DC全月列表只浏览目标ID段的相关标题，不宣称公告日证明。日格式2026-01-15返回400，不重复尝试。混元动态IAB首次超时reset，缺目标历史可读目录隔离；不授已浏览或无发布。
