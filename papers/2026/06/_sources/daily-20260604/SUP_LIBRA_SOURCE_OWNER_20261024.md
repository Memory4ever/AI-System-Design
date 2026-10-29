# Libra 03077 必要Source / actual同family比较 / 最小PRE

作者supp_20260604_author；R27准入/Jun03日证直接复用。正式2+2+2=6，对tool-return history消费与迁移guard具体长期gap深入。exact-v1完整流TEXT112026字符保存SUP_CORE_2606.03077v1_TEXT_20261024.txt，无工具截断；必要读§2.2–5/6/7.1–7.4及A.1–A.3。支持与关键反侧足够停止；没有读足以认证zero-gradient恢复的完整AppendixB，因本项不采用其全状态数学等价/无阻塞恢复保证，不补读无关附件。未核实现、figure像素或复现实验。

## 必要Source

§3–4 planner枚举training parallelplan/rollout DP，历史每prompt长度排序且每instance只能contiguoussegment，Costproxy/剪枝，不是任意真实runtime全局最优。globalreplan收益须超过reconfigcost；coretrain组不重建，hybrid完整unshardedweights/optimizer以sidechannel梯度接入。§4.4/6声称恢复期zero梯度等价/加载snapshot后同state，但本稿不证明snapshot推进间隙/active梯度权重与完整恢复安全，不把它写成生产协议已验。fixedpool合理性/版本与objective owner不变。

§5真正差额：以prompt_id加完整已观察tooltype/sizeclass/successfailure序列索引trie，每node存到轨迹结束的**总剩余长度**历史分布，不是下个tool输出增量。首轮全放短bucket；每toolreturn读remaining mean与P90，只有两者落同bucket才迁移，未知child回parent统计、仍不一致保当前bucket。它仍是经验length estimator，不是tool事件识别确定未来长度或已识别因果；不宣称彻底无预测。CPU KVoffload/reshard/targetreload、crossnode transfer-vs-recompute按实际profile选择，必须核同policy/layout/context。原文“offload总被toolIO完全隐藏”不外推任意工具速度/PCIe争用。

A1 coldprofile先对**整个训练corpus**用initialpolicy生成N×K轨迹，校准CE并bootstrap，故“zero online inference cost”不是零采样制备费或对新prompt保证。A2 completedtrace增量更新，默认50steps用recent重建；subsecond树操作不含那些rollout采样。A3 SearchR1初期fallback<6%、后期<4%只已profile人口，不证明全开放任务低fallback/无drift。

§7固定48A800SXM480GB/6nodes×8、NVSwitch600GB/s、200GbRoCE/GDR，Qwen3-14B/30B-A3B，GRPO16samples/prompt max40960，verl/vLLM/Megatron版本、完整precision/各run所有batch/SLO矩阵未披露。三benchSearchR1/R2EGym/DAPOMath；四baseline有AReaL static optimum由同CE选，非其在线调度能力上界。§7.2同heterogeneousbuckets的SearchR1 routing比较OracleGTremaining/embeddingpredictor/MLFQ/loadbalance，T2 CMLFQ91.1%/2848tok/s对embedding65.2/2400，不能当未来结果正确率/任意policy因果。§7.3顺序叠加planner/hetero/CMLFQ/elasticity不是全factorial独立主效应，正文分项423+87+41+115+97合计763相齐，但顺序增量与所报百分比基准不同，不把27%独立百分比拼全收益。完整同budget/seed/uncertainty未充分披露，不使用强统计结论。

§7.4 train→rollout10.8s activate，reverse背景snapshot3.6s+reload4.4s，平均454.16s step下<3.5%为该设置非零；same/crossnode40K KV<330/733ms，选择migration/recompute另有profile成本。全coldprofile/更新、planner、原始rollouts/failedtools、迁移/重算、state与独立trainquality回归都计费。新prompt/稀疏returnhistory/测量漂移或迁移不值时保固定pool/普通queue和现有policyfreshnessgate。

## actualowner：旧NC不足，但不重复建owner/family

R29独核补充的原证内部差额仅行政保留，不采用进Book单段：§7.3各项合763相齐，但763相对423增加约80.4%，不是原述78%；§5 crossnode transfer/recompute约4K交点与§7.4最长序列catchup叙述不齐，不授通用迁移阈值；A1同时写46GPUs及TP8×DP6，配置不相容，不作已验可复现拓扑。以上不影响原稿有限tool-return统计/guard命题，亦不因未采用数字扩读附件。

完整读当前Ch36 1315–1364弹性phase/同group交接，1688–1742 AgentRL dataflow→ProRL→28101长尾trajectory完整组→DARTS完整段，以及2199现SF-LIBRA-AGENTIC-RL同family note。三Bookscontext/ROADMAP及Ch35/37开篇职责已读。注意后面另一个Libra2607.23250是sequencepool/tiles的不同paper，绝不混同。

同family旧note称弹性、toolwait、placement足够ExistingCoverage，正文实际只承载通用资源/训练semantic分权与progressive remainingwork→queueplacement；它没写prompt+return-state trie的条件剩余长度、mean/P90一致才迁移、未知path父统计以及cold全corpusprofile。不能只按主题给NC，也无须复写已有elastic/dataflow。唯一owner仍TRAIN-DISTRIBUTED-TRAINING Ch36，复用SF-LIBRA-AGENTIC-RL身份；只提一段接在28101完整组后/DARTS完整段前。旧note日期/别人的NC不自行改，root协调本轮具体追加与本人note即可。

完整上锚：

Scheduler 只拥有 rollout execution order 与 placement，不能改变 action、reward 或 policy semantics。它可以缩短同步批次被长尾轨迹占据的时间，却增加 prediction drift、context migration、fairness、stale policy 和 tool-result cancellation；短轨迹、工具调用少或严格 FIFO 更重要时，普通 worker queue 仍更清楚。`arXiv:2603.28101v1` 的证据只覆盖 §4、§7.1 与 §8 所披露的 Agentic RL rollout 系统和实验，不证明任意工具分布、集群或训练同步策略都有相同收益。<!-- source-family:SF-2026-ARXIV-2603-28101 -->

拟增一段：

剩余工作也可在工具返回后从历史条件分布读取，而不只按当前 token 长度升级队列：以同一 prompt 的有序工具类型、返回大小类别和成功/失败状态索引 prefix tree，每个节点保存到轨迹结束的总剩余长度；只有其均值与 P90 指向同一 TP bucket 才迁移，未见分支回到父节点统计，不一致则留在当前 bucket。[受限工具返回调度](https://arxiv.org/html/2606.03077v1#S5)据此改变的是何时信任经验估计，并未让返回事件成为未来长度的确定因果证明。它预先对训练 corpus 生成轨迹并持续更新历史，查表便宜不等零制备费或新 prompt 已覆盖；KV offload、CPU reshard、跨节点传输/重算与 profile、计划和质量回归均需计费。历史稀疏、policy/布局漂移或净迁移收益不足时，应保留当前 bucket、固定 pool 与原 queue/freshness gate，不由较高 routing accuracy 签发无偏训练、恢复等价或线上 SLO。<!-- source-family:SF-LIBRA-AGENTIC-RL -->

完整下锚：

长尾也可以从训练组的产生规则处理，而不只移动既定 trajectory 的执行位置：同一 prompt 先生成冗余候选，再选多数短路径和少数有效长路径组成 GRPO 组，用历史长度差异提出各 prompt 的冗余预算；预算饱和时可改成只收最先完成的有效路径并取消剩余候选。[DARTS 的受限分支](https://arxiv.org/html/2605.30859v1)因此改变采样人口与组内 reward baseline，不是保持原分布的纯 runtime 调度。长度 variance 不是校准 uncertainty，保留少量长解也不证明所有必要深度都被保存，固定长度或极稀疏 reward 可能无益。Token streaming 可先做增量 forward，但 reward 与 backward 仍等完整轨迹；冗余/弃选和已取消前缀、profile/历史状态、KV 与完整训练都计费。代理、质量或净预算失配时，保留原采样组、prompt-level 调度与普通 sample streaming，不让较短 rollout 或有限平均准确率批准无偏更新与通用提速。<!-- source-family:SF-2026-ARXIV-2605-30859 -->

本人trueH2注拟：`SF-LIBRA-AGENTIC-RL`：Daily2026-06-04补Jun03；exact-v1 §2.2–5/6/7.1–7.4/A1–3必要域，2+2+2=6；具体增补toolreturn条件remaining distribution/mean-P90 migrationguard，旧同familyNC不作本次充分覆盖。保全corpus coldprofile/稀疏回退、cost与异步语义分责；不采用zero-gradient恢复等价、泛化因果或后版NPU/headline。未核图像/代码/复现。待实际写后复核。
