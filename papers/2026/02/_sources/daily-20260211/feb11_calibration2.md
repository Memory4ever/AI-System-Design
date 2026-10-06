# 第二、三批完整题摘准入校准
精确v1完整AB：feb11_AB2.json / feb11_AB3.json；按ID定位。日期暂为submitted+公告policy，未完成registered包络前不进正式候选。只给贡献链，未把AB宣传性能当事实。

## AB2 拟准入
- 07397 Sketch&Walk：固定稀疏mask/每层重算KV选择昂贵→Hadamard估计+确定walk复用跨层注意力→应重新选prefill/decode预算与selector开销；不是只有6x数字。
- 07398 AgentSys：间接PI经工具返回累积主agent上下文→独立workers/nested workers只返回schema-parsedJSON，边界operation级validator→重新选memory isolation单位而非仅清洗全部context；安全强制深入。
- 07470 CoT perturbation：推理链当稳定可读中间对象→固定时点7种干预显示语义保留改写、early/doubt/noise的质量/长度反侧→重新选trace鲁棒性评价和reasoning-token预算；设计counter深入。
- 07546 LR-DLLM：fixedcanvas不同length置信度不同比→lengthregularized decouple semantic confidence vs length uncertainty→重新选dynamiccanvas expansion/contraction，而非manuallength。
- 07549 EpistemicLedger：多约束search“答案似乎齐全”当完成→bareassert/refutationignore/stagnation/earlyexit诊断及explicitconstraintbelief/evidence干预→完成闸门需要证据更新反驳路径。标准成熟tracking不是增量，增量是这种失败条件和介入对照，需core限定。
- 07562 GaussianMatchCopy：低trainloss推断检索可靠→二阶相关copy构造+maxmargin收敛梯度条件→重新解释关联检索如何与memorization区分。理论不能机械拒。
- 07574 ViCA：视觉tokens完整selfattn+FFN作为默认→bypass视觉块只在稀疏layer跨attn有控制→重新选visualrepresentation是否必须深层贯穿，质量/计算绑定；非pruning分数本身。
- 07594 generation/verification：同任务能力/训练互相转移→作者称generationRL不能verify，reverse更有效+联合objective→重新选验证训练而非默认生成带来verifier。需要错误构造等counter。
- 07596 Astro：推理时rotation/onlineoutlierhandling作为量化前置→训练阶段activation-guidedweightregularization suppressoutlier→新选择是提前训练目标约束 vs inference额外变换，不是单纯GPTQ组装。
- 07616 SERE：batchtokenlocalexperts导致union大且全expert昂贵→secondaryexpert similarity替代/保留criticalprimary、动态batch redundancy→重选batch共享与质量权衡，不是静态merge。
- 07652 AgentFence：modelPI抗性就代表agent安全→heldmodel14boundarytests/8architecture显示错误principal/stategoal failures→必须评价runtime权限/状态边界，不靠单modelrobustness；安全深入。

## AB2 最小core再定
07559 VerifyRL：symboliccalculus-specific shrinking decomposition+formalverifier的任务成绩本身不准入；只有验证目标防止何种非法学习路径且有系统通用边界时可收。先读最小core，不因此全proof。

## AB3 拟准入
- 07672 DebuggingCWMs：长程state tracking失败归因Transformer记忆→groundtruthactions替换反事实与字符串/tokenbudget两负侧→先区分action-generation/state-propagation错误和representation预算；设计counter。
- 07673 SummaryOverlapBias：semanticLLMjudge胜overlapmetric→低human/modelsummaryoverlap下9小模型8模型更偏model文本，与positionbias区分→评价不能把judge提升称人类质量提升；局部负侧可收。
- 07721 ParisKV：固定KVretrieval表征受drift、batch1 selector成本→collisioncandidate+quantizedinnerproduct rerank/UVA按需fetch→重选fullattention可运行区间内外的KVselector/data-placement；不是只百万context倍数。
- 07755 ALMA：手工固定memoryschema/retrieval/update→metaagent直接搜索可执行memorydesigncode→memory设计本身可search，须验证搜索/部署预算和未见domain而非“四benchmark超过”。
- 07775 RollingSink：训练5s自回归videocache用于无限rollout失配→training-free cachemaintenance研究与rolling sink→缓存生命周期/历史锚点选择可突破finite-traininghorizon，core必须是具体sink机制不只30mindemo。
- 07790 MaD-Mix：人工多模态混合配比及missing-modality难对齐→Fencheldual intermodalcoupling closedform alignment/容纳languageonly→重新选配比估计成本vsmixturetraining，非22%steps本身。
- 07794 StructuredICL：latentrepresentation只有关联→causalmediation把跨contextconceptsubspace作为功能中介→改变结构表征解释的证据权限，须读干预selectivity和其他替代解释。
- 07796 mandatorythinking：显式thinking默认帮助agent→7models/3bench/2instantiation显示减少披露伤害交互，披露提示反转→重选user-engagedagentreasoning/outputcommunication；设计counter。
- 07832 rePIRL：PRM需要expertreward或entropycollapse→inverseRLduallearn policy/PRM较弱假设→新选择是无需已知expertreward的processlearning，须原objective/identifiability/ablation。
- 07839 TodoEvolve：fixedplanningtopology→PlanFactory topology/init/adapt/nav+IGPO学习产生code架构→重新选规划器是否runtime/learnedcode而不是固定手写，需core budget/stability负侧。
- 07845 RD-VLA：fixeddepth/显式token迭代memory增长→weighttiedrecurrentactionhead+TBPTT+latentconvergencestop→latentreasoning深度/SLO选择，非tasksuccess0→90数字。
- 07854 ViewRoPE：screen-space embedding跨camera revisits drift→relativecamera-rayattention+geometryframe-sparse→新选择是几何identity/index替代pixel-local历史，而非domainvideo效果。

## 代表关闭
DialogLab官方Feb10 blog完整核心read（feb11_official_event_core.json）：已于UIST2025公布。新blog没有重要revision，仅social/temporaldescriptions+dragdrop/script/improv/livehumancontrol成熟集成与14人Likert界面偏好，不能把agent能力/安全有界机制由这些rating推出，贡献关闭，日期不再无限核。
AIRS-Bench待完整AB（已请求06855v1）：不能因Science名称整体否定其中MLresearchtasks，也不能因新20任务排行榜准入；须指出evaluation盲区/混杂新证据，否则关闭。

