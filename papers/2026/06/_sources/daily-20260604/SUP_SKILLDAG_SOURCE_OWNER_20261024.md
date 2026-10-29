# SkillDAG — necessary Source / actual owner / PRE

作者supp_20260604_author。准入日期R2已通过；2+2+2=6，受具体memory update gap深入必要域。exact2606.03056v1完整TEXT61325chars已保存（原HTML流剥标签/math重复，不含truncation）；作者已读§3–4.3/Limitations/AppD/F/G/H，支持与反侧足够即停。未核代码或复现。

## 证据范围

§3.3/F search返回独立matches/top5相似、bidirectional BFS depth2的typed neighbors、仅matches一跳conflicts；show再载选定body，可丢整个field或不选graph，不是只换一个scorer。§3.5/G propose先dryrun+pairhistory，edit才reason/taskid/timestamp commit；同agent单execution可作semantic决定，DAG/noncontradiction/appendhistory rollback只结构约束，不独立证明边真。API可delete/retype与conflict，不把所有edit叫add-only。

§4 baseline taskreward引用他作，未本地rerun/非seedpaired；ALFWorld140 validseen/37skills，SkillsBench87容器任务passfraction/200–2000skills，MiniMaxM2.7与GPT5.2codex各n=2 task attempts，30stepALF限。Intrinsic用SkillDAG轨迹自己的queries固定embedding重放，不证明各policy自己query下同优势，10x ranking只matches与GoS HNSW/PPR差异，不隔离typedfields。Train420→test140编辑关闭展示局部transfer，强backbone task优势可消失。316queries65tasks replay+27positive edges，**untruncated matches∪BFS**使该新增positive-edge recalled-set单调；不证明delete/retype/conflict或固定contextbudget无损，也不保证answerquality/production。

D冷启scale1000约200 GPT5nano bucketcalls+每skill两view embedding；查询次数不设硬上限，推理和show都要计费，不以按需body自动净省。H想象needs/self两view只提可能依赖，非实体执行precondition真值。短期single-observation semantic污染/过时关系与错误冲突要可撤回；出处、版本与独立行为check不可由history日志替代。

## actual owner与PRE

三context/ROADMAP已读。唯一AGENT-MEMORY/Ch77；actual“Procedural Memory应保存可展开依赖图”完整原段→12039 marker→GUI routine完整段与marker、Ch76 retrieval身份/Ch78set发现分责均已读。现段讲typedgraph/mutationproposal/controller/执行边界，但未区分向agent暴露三观察通道与固定pipeline消费bundle，也未解释propose/commit仍由同agent语义拍板/结构guard非semanticgate；不是因为主题相同给NC。拟在12039完整marker后/GUI routine完整段前加两段，不另立论文标题，source只支持条件分支。

完整上锚：

独立 skill 条目按语义相似度检索，在数量少时简单有效；长期积累后却无法表达前置依赖、兼容性和 merge/split/retire。typed skill graph 可以把 trajectory evidence 变成 mutation proposal，由 memory controller 管理版本和关系，workflow runtime 仍验证当前状态并提交执行。组合性换来图漂移、循环依赖、错误合并和 RL feedback 固化偏差；证据不足时应回退孤立 versioned skills、人工依赖和只读快照。exact-v1 的环境结果不证明图关系具有因果性、跨 Agent 可移植或在线更新一致。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12039 -->

拟增两段：

关系图也可以被暴露为 Agent 自己查询的记忆接口，而不只由固定 retriever 消费成一个不可分的 bundle：相似匹配、带类型的依赖邻居和不应共同载入的冲突分别返回，需要时才读取 skill body。这样模型能在任务推进中重新查询、按预算放弃某类观察，并留下选择或排除的理由；但搜索结果仍是有来源的关系提案，不是当前环境前置条件或真实兼容性的证明。[受限图接口对照](https://arxiv.org/html/2606.03056v1)中的检索重放使用该 Agent 自己提出的 query，任务基线又并非配对重跑，不能把全部收益唯一归给三通道接口。<!-- source-family:SF-2026-ARXIV-2606-03056 -->

更新前的预览与更新后的记录也不等于独立语义审核：同一个 Agent 可以看过 pair history 后，仅凭一次观察提交关系；无环、禁止相互矛盾的边及可回滚历史，只约束图结构和恢复路径。新增正边在不截断的匹配与邻居并集中不挤出旧成员，并不保证删除、改型、冲突剪枝或固定 Context 预算下仍无损。冷启动分类与双视图编码、反复搜索、body 载入和关系回归都需计费；错误或过期关系应可隔离、撤回并回读原轨迹，回退孤立 versioned skills、人工依赖与当前环境检查，而不以可追溯日志或一次成功自签长期记忆。<!-- source-family:SF-2026-ARXIV-2606-03056 -->

完整下锚：

GUI routine 也可以被编译为可搜索 transition graph，避免每屏从头解释；Q/value 只排序 path proposal，observer 与 runtime 必须验证当前 screen state 和 action precondition。它减少重复推理，却增加状态 alias、图陈旧、搜索成本和错误 routine 复用；不匹配时应回退逐步 observation/planning 与可撤销 checkpoint。exact-v1 只支持 AndroidWorld，不证明真实桌面安全或跨应用迁移。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12294 -->

Review note拟：`SF-2026-ARXIV-2606-03056`：2+2+2=6；exact-v1 §3–4.3/Limitations/D/F/G/H，agent-callable matches/neighbors/conflicts与same-agent semantic commit/结构guard分责；引用非paired taskbaseline、policyquery replay/仅matches排名、untruncated positive-edge recall非全部edit或预算保证，冷启/反复query/回归费用保留。未核实现或复现。待实际写后复核。
