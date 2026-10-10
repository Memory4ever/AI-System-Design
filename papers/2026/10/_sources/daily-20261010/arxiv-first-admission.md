# 2026-10-10 arXiv 首批准入校准

窗口：2026-10-09 BJT完整自然日；作者live1010_author。官方recent列表首个日期段12分类题名恢复保留于`arxiv-official-titles.json`，均明确`Fri, 9 Oct 2026`，该段的跨分类条目数不是候选数。API published字段是submitted，不用于归属。本批26完整题摘保留于`arxiv-batch1-abstracts.json`，官方公告交集核实落窗；尚未做先公开/撤回/必要正文门，以下仅贡献初筛。

| ID | 原有约束 → 本篇具体增量 → 需重新考虑的选择 | 初筛/拟评分 |
| --- | --- | --- |
| 2610.12338 VFold | 跨层V融合可能需要改架构 → symmetry-aware V合并且与key pruning/低比特组合 → V共享须处理表示对称性，而非原值相似度 | 准入 2+1+2=5 |
| 2610.12242 TokenRouter | token路由在single-model server错步/准入等待 → request-centric编程/model-centric异步子服务+delayed batching → token路由的跨engine批处理策略 | 准入 2+2+2=6 |
| 2610.12133 Attic-KV | 未知query缓存倾向全文rehearsal → 紧预算全文rehearsal反而遗漏答案；自问引用+content-adaptive anchors → query-agnostic压缩的rehearsal分配 | 准入 2+1+2=5 |
| 2610.12367 SGUID | semantic相关skill bank全量蒸馏 → 有效signal稳定筛选<25%skills并支持第二轮co-evolution → skill检索相关性不等于学习收益 | 准入 2+1+2=5 |
| 2610.12376 LCT | tokenizer压缩指标代表示质量 → MDL/morphotactic结构发现与词频vocab分配解耦，104语言题摘称收益 → 压缩/结构/语言容量分配需要分开评价 | 准入 2+1+2=5 |
| 2610.12161 KL/ZCPO | group reward零差可能仍受ref KL更新 → 七条具体失效路径+conditional-KL校准组内reward → 不能把任何KL简单看成同一稳定器 | 准入 2+1+2=5；触及失效设计需深入相关core |
| 2610.11659 DIAL-OPD | sampled-token log ratio大即高价值 → low-low token大比值却信号差；log mean概率加权筛token → 监督价值不以reward幅度单独排序 | 准入 2+1+2=5 |
| 2610.11291 Semi-OPD | student on-policy总比离线旧rollout好 → 17teacher/student pair中14离线初始rollout更好；overlap条件 → OPD方案需双边teacher/student分布匹配 | 准入 2+1+2=5；具体反证深入 |
| 2610.11854 GRPODropout | 同sampling budget rollout皆应update → 高prob positive-adv部分丢弃并recenter维持entropy → 生成预算与有效update样本分开 | 准入 2+1+2=5 |
| 2610.11247 OPD failures | stronger teacher提升迁移 → learning-signal proxy早衰与残余loss，近teacher local recovery条件而非已证representation因果 → teacher接近度与失败机制需限定 | 准入 2+1+2=5；具体反证深入 |
| 2610.11575 Elastic routing | deterministic top-k零反馈边界 → 对k对称局部随机budget保expected compute且inference固定 → 训练expert exposure可与服务budget分离 | 准入 2+1+2=5 |
| 2610.12445 Caught in Act | 只依赖text monitor/context无法判hidden goal → 跨层/token probe+introspective groundtruth任务 → white-box监管的证据可超可见文本但须groundtruth条件 | 准入 2+2+2=6；security局部深入 |
| 2610.11915 PTP-U | fixed forgetting下collateral drift视作必要 → analytic edit后non-target投影恢复，匹配forgetting比较 → retention/forget约束下的可恢复部分 | 准入 2+1+2=5 |
| 2610.11132 SFT-as-context | SFT专化与parent能力只能权重折中 → parent把SFT response当上下文，19对11bench验证+conditional error guarantee → 能力组合可换为双模型推理且需成本边界 | 准入 2+1+2=5 |
| 2610.12375 OnTrack | posthoc太迟/每步LLM monitor重 → streaming结构aware OT三access regime与失败abort → 轨迹结构监控收益及误abort测量边界 | 准入 2+1+2=5 |
| 2610.11678 TRACE | score变化直接当能力变化 → paired轨迹行为检查+unchanged轨迹重评分，任务重跑15–36%flip与judge procedure/outcome差 → verifier/mutation估计对象分开 | 准入 2+2+2=6；具体反证深入 |
| 2610.12468 DreamTrue | robot成功轨迹/camera calibration使预测偏乐观 → image-space action calibration+counterfactual RL/defect reward → world model反事实缺真未来时采用何种证据 | 准入 2+1+2=5 |
| 2610.12007 REACT | chunk smoothness与reactivity折中 → staggered timestep滚动action buffer+双解耦 → observation新鲜性/action commit边界 | 准入 2+2+2=6 |
| 2610.12307 BudgetPix | uniform pixel tokenization不能调budget → entropy quadtree多尺度token/scale decoder/variable-token schedule → image denoiser的runtime预算改为tokenization合同 | 准入 2+1+2=5 |
| 2610.12407 LeWAM | raw action MPC钻dynamics error → 四mode JEPA joint latent+policy noise-space planning，相同encoder/size policy比较 → 规划优化空间而非世界预测精度单独决定控制质量 | 准入 2+1+2=5 |
| 2610.11716 4Tensor | joint spatial/semantic/temporal attention → ROCStories next-sentence匹配参数one seed证据；video/robot接口未实现；free-running baseline造成训练walltime不可归因 → 局部结构潜力，但题摘尚未明确可保留设计证据是否控制序列执行差异 | 定点准入core，不以小模型/单seed直接EX |
| 2610.11899 Forms survey | 22系统标签/架构四维归纳，无新执行机制/评价盲区证据 → 只是分类共同语言，不改变设计解释 | EX：主题相关不是具体增量 |
| 2610.12064 ILM | KG/RAG+LLM judge应用于教学内容，无模块成立边界/新执行机制 → domain feasibility不足 | EX：已有模块应用 |
| 2610.11787 BehavDep | depression诊断方法/指标；非基础模型或系统机制主线，不能经representation owner绕回 | EX：医学领域应用 |
| 2610.11430 BioBigBird | biomedical sparse context+多任务NER/RE组合，没有新attention/系统约束证据 | EX：医学应用且既有组合 |
| 2610.11451 SAIL | science-aware能力生成/训练loop面向科学工作流与科学评价 | EX：AI for Science暂缓，不经Agent owner绕回 |

本批准入仅表示值得核验，不授Source/Evidence/Books/日级通过。root已实际独立读取全部26完整题摘，20拟留与5EX准入校准通过；4Tensor另在必要core后以2+1+2=5准入，中心证据争议安全隔离，不因one seed排除。各项后续Source与Books见author-source-decisions.md及independent-training-evidence.md。宽列表保持线索身份，没有全量逐项关闭任务；未自授DAY。
