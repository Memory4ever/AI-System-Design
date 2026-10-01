# 04/20 完整题摘的否定侧：分层抽检入口（作者工作态）

**最新纠偏（非作者，2026-09-28）：**[root 对15376/15945的 exact-v1 逆向审校](./V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)又恢复两项标准、仅报告。当前对账为 `111候选+38具名前关闭+1首公开身份隔离=150完整题摘`；下方 `109/40/1`、净新18及“仍待”字样是此前工作快照，不能作当前日级状态。被恢复项原关闭理由留作错误样本，不在现行关闭分母；其余有限抽样仍不能替代整日 Gate。

本文件为本日已读150个唯一完整题摘中**未进入当前拟冻结候选表**的具名贡献前判断提供有限抽检路由，不把447宽标题库存变候选或全题摘队列。原22项理由分层保留在下表；反向审计先移出39项，作者自纠恢复三项、root [逐项独立重判八项](./V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)与[后续定点纠错三项](./V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)，再经[十一项冲突作者裁决](./V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)七项恢复、四项维持，净新增18项前关闭。原[72个Only反向准入审计](./V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)保留作者当时逐项理由和原证据位置，但被恢复十八项的旧前闭判断已失效。日级非作者 Gate 尚未通过，不能把有限单篇审阅冒充全日准入PASS。

已逐 ID 对账：额外125与旧25不重叠，共150完整题摘；当前作者拟冻结§3为109，未正式41=40具名贡献前关闭+15483首公开隔离。原22前闭精确ID：`15343 15468 15475 15623 15641 15647 15671 15679 15727 15751 15814 15849 15877 15898 15911 15919 15951 16042 16070 16088 16108 16114`；净新18项：`15701 15376 15400 15709 15482 15484 15648 15657 15802 15972 15859 15756 16056 16145 15830 15873 15917 15945`。16171/15609/15809经[作者自纠](./V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)恢复；15351/15451/15614/16076/15705/15706/16079/16135经[root 八项独立重判](./V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)恢复；15675/15583/15771经[root 三项有限纠错](./V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)恢复；15622/15794/15871/15741/15760/15521/15621本次由作者恢复，后七项仍待非作者逆向准入核。剩余现行关闭理由见原审计中未被纠正的逐项行及[四项维持关闭理由](./V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)；原必要方法、反证仍在[恢复笔记](./v3-reopen-notes.md)。`109+40+1=150` 只为当前作者工作态，尚未通过日级独立分母；早期被纠正的16054/15660/16198/15663/15549亦不在关闭集。

| 理由层 | 具名已读条目与本次前关闭的最小依据 | 建议非作者抽检/触发恢复 |
| --- | --- | --- |
| 领域或一般系统应用、缺本项目直接机制 | 15475 多机器人模块编码/Zenoh 不给 foundation/VLA 或新执行反证；15647 civic deliberation CIG 为领域对话测量；15679 FEP successor 是一般脑模型规划；15751 Sybil pointer-chasing 为一般 crypto primitive；15814 hand-eye pose 几何 replay 为普通校准应用；15919 HPC continuous benchmark、16088 HPC congestion trace 均未给大模型特有测量/状态条件。原在本层的15549已经因有向 mixing 联合训练通信成本的直接分支恢复，不再以前闭计。 | 抽 15475（机器人是否漏 VLA）、16088（GPU术语不等LLM负载）；受15549纠错影响，按是否把缺LLM名字/模型规模当硬门槛定点复查本层，不普遍恢复所有机器人/HPC。 |
| 成熟组件迁用或局部 operating point，不见新选择边界 | 15727 algebraic weakest-link/possibilistic rules 未给新 LLM 验证；15849 小 music model 的 encoder/projector 迁用只有任务比率；16070 表格 OCR/Transformer/MTP 组合；16108 语音驱动动画 joint condition。15660 原在本层，但其“DP post-processing 保护发布数据”的关闭理由被反例推翻；16198 的前后两种需求校验与消融、15663 的跨模态代码检索方向/长结构失配均已独立恢复，三项移出前闭。 | 抽 15727（是否真实保证）、其余成熟组合有无新条件；不因局部方法或小模型本身拒绝。 |
| 综述、taxonomy 或个案未解决具体设计分歧 | 15343 autoethnography 将情感个案推成 attention 隔离普遍失效，无受控机制；15468 六 ring taxonomy/三 worked cases 明示 conceptual；15898 symbolic XAI overview；15911 video diffusion 四类加速 taxonomy；15951 graph/LLM/Agent 用途梳理；16042 intrinsic interpretability 五范式综述。 | 抽 15343（安全反证措辞是否误关）、15911（是否有新比较证据）；若综述含独立 synthesis 解决争议才恢复。 |
| 新任务或测量数字但未改变已有模型设计判断 | 原把 16054 以八视觉认知任务/人模分数差与高层错误 taxonomy 前关闭；本次定点抽检发现 §4–5 的 prompt×task 方向分化和分辨率对照，已**撤销**这一项闭合并经非作者有限核入正式5分仅报告，不将本层扩成所有 benchmark 的全文队列。 | 16054 的准入与受限处置由root具名通过；本层其余负侧仍需分层抽检。 |

旧22项中，15623/15877/15671/16114获apr01具名核，15475/16088/15343/15911/16070/16108获root具名有限核；其余旧12项仍没有逐项非作者PASS。净新18项中，root已定点核15701/15859，并对[15648/16056的 exact-v1 方法、反证与真实 Ch24 owner 作反向准入复核](./V3_ROOT_15648_16056_REVERSE_ADMISSION.md)，四项维持具体前关闭；这些有限结果不外推其余14项。root另抽核保留16027/16146/15958，不等于全候选或日级Gate。15483为具名首公开隔离，不是贡献前关闭。不能从上述样本外推40项全部可靠；root最终正反样本Gate仍待执行。

建议对旧22与净新18按来源、主题、理由层及风险信号抽样，对当前保留52个Only的真实设计增量作对照；此前15557因 Ch31 真缺口由Only转实际整合，不能沿用旧43计数。尤其检查新关闭的局部算法是否隐藏稳定适用条件、以及保留的负面结果是否仅换任务。此表列精确ID和审计位置，不宣称447宽目录零遗漏。

**三项后续纠错的现行状态：**作者原[反向审计](./V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)中 15675/15583/15771 的前关闭理由仍留作历史，不再属于上列净新25；root [定点独立原文核](./V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)确认它们分别在跨语种子选择、同文档多query缓存与失败后恢复动作选择上有受限可报告增量。作者已对照既存必要方法、实验反向与 Ch27/76 具体 owner，将三项按5分标准 Only 写入正式§3/4，保留成本、gold标签、指标差异及不采普遍保证的边界。此处仅撤销这三项贡献前判断，不把同行准入核扩成47项负侧或日期 Gate。

**九项旧同行／作者关闭的冲突已获作者裁决，非作者待核：** `15622` 有[apr02源/处置核](./V3_APR02_FIVE_BOUNDED_DISPOSITIONS.md)，`15657 15794 15802 15871 15972` 有[apr02六项源核](./V3_APR02_LAST_SIX_INDEPENDENT.md)，`15741 15756 15760` 有[root有限命题核](./V3_ROOT_FINITE_INDEPENDENT.md)，早前均被判为受限标准 Only；后来的作者反向审计却把它们前关闭。两层审核事实与判断不同。本次[十一项作者逐项裁决](./V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)中此九项恢复五项、维持四项关闭，不删除旧必要证据或反证；仍需另一人核其贡献准入，不说负侧 Gate 已过。

**同理由层再定点的两项（作者已恢复，非作者待核）：**作者重开[15521 FreqFlow exact-v1](https://arxiv.org/html/2604.15521v1) §3–4/Table6–8，原前闭理由中“未分离哪个条件”过强：低/高频有分支消融（FID 3.86→3.55/3.12→both2.95），merge add 2.95 对 cross-attention3.95/concat3.46，另有freq-branch loss 4.67→2.95；这些只识别本模型组件贡献，不匹配额外模型容量、训练总算量或跨模态，不自动改写 Ch24 的生成范式合同。作者亦重开[15621 AdaRankLLM exact-v1](https://arxiv.org/html/2604.15621v1) §III-B/V/TableII：允许有序子集为空的 `[0]`，所测较弱模型的固定大k更易噪声反退，强Qwen3 Thinking 在Vanilla10的Overall34.18/EM54.85反优于Ada32.75/51；“强模型只省上下文”又未算selector全成本。强弱模型对同一自适应策略的排序反转可能比“已有 top-k 深度控制”更具体，但 oracle k与成本分母不能上线。两项按[逐项裁决](./V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)恢复受限标准候选，仍不冒称日级独立准入。

### 16198 定点重开（作者必要原文与非作者有限核通过）

原题摘表把 REA-Coder 简化为成熟“需求重述/自检循环”，并以未给独立 spec authority 前关闭。必要[官方 exact-v1](https://arxiv.org/html/2604.16198v1) §3.1/3.3、Tables 1–3 表明：生成前的 question/reference-answer 检查将“需求理解错误”与代码生成分开；生成失败后又把需求关键片段遮蔽，用已有代码反推并更新检查清单。WO-QA/WO-MASK 的有限消融与首轮结果给这一分工受限支持，但引用答案/判定均由模型生成、public tests 不是用户语义 oracle，成本大幅上升，也不能因无 authority 就否认局部验证选择的可能增量。作者暂移入潜在 `5` 分标准/Only 审阅，完整反证与实际 Ch79 比较见[提案](./V3_16198_REOPEN_AUTHOR.md)；非作者准入、评分与正式处置未过，未记入正式 §3 或Books。

后续[root有界非作者核](./V3_ROOT_16198_FINITE_INDEPENDENT.md)已确认 `2+1+2=5` 标准/Only、Ch79既有最终验收责任无需新增 Books；具名 first-public 联合链另见[日期记录](./V3_DATE_RECONCILIATION.md)，正式 §3/4 已同步。上一段保留作者起始工作态，不再作为当前 pending 声明。

### 15663 定点重开（作者必要原文与非作者有限核通过）

原题摘表把 CodeMMR 作为成熟 shared embedding/RAG 迁往五视觉代码域前关闭；[官方 exact-v1](https://arxiv.org/html/2604.15663v1) §4.2/Tables 2–3、§6–7 却给出 query/return 模态方向、长 SVG 结构和未见任务分层的局部反证。单一平均 nDCG 掩盖 WebUI/UML 与 SVG image→code、草图的显著不同，两个下游 image→code RAG 对照只支持局部生成收益。实际 Ch76 的 typed operator 与检索/reader分账已经拥有长期责任，不能因有章节就抹掉可报告的特定失配；也不能把新benchmark平均提升写成全任务/生产收益。作者拟 `2+1+2=5` 标准/Only，完整限定见[提案](./V3_15663_REOPEN_AUTHOR.md)；[root有限核](./V3_ROOT_15663_FINITE_INDEPENDENT.md)确认准入与实际 Ch76 对照，具名[日期链](./V3_DATE_RECONCILIATION.md)已核，正式 §3–4 已同步，不代表日级 Gate。

同一成熟迁用层的**作者分层抽样，不是非作者全量 PASS**：15727 已定点看原规则与测试对象，property fuzz 验的是符号规则而非 LLM 行为；[15849 官方完整题摘](https://arxiv.org/abs/2604.15849)只是现成 MATPAC++ audio encoder、linear projector、MusicSkills-3.5M 与 MuChoMusic 82%/35×，没有把 music-specific QA 成绩拆成新对齐条件或系统选择；[16070 官方完整题摘](https://arxiv.org/abs/2604.16070)将 OCR/表结构/坐标序列合并并以 MTP 提局部延迟，未给超出现有序列接口的跨任务成立边界；[16108 官方完整题摘](https://arxiv.org/abs/2604.16108)以 transcript 与参考脸部 style 联合条件改善 SDFA，但只在动画任务给结果，未显示模型主线的新条件控制。后三项继续具体前闭，不是因为模型小、无 LLM 关键词或结果局部；若独立抽样发现任何一项的必要原文反证，才扩查其共享理由。15663/16198/15660 的纠正表明本层不能简单用“成熟组件”一句统关。

15727 的上述判断另经[官方 exact-v1](https://arxiv.org/html/2604.15727v1) §2、§6.1–6.3、§7.1–7.2 定点复查：`R_eff` 的 min/ceiling、scope lattice 与 phase FSM 是外部符号系统自定规则；100 个 property 与 16 个 fuzz 类检验其实现遵守这些规则，并没有对 LLM 判断可靠度的校准实验。§7.1 明说 weakest-link 直接沿用 possibilistic logic，§7.2 的 GPT-4o/AIRS-Bench 只是未披露可审数字的 preliminary，受控 logical-reasoning 实验仍在进行；故不把“规则内一致”升级为“LLM 推理正确性保证”，目前维持具体前闭。F0/F1/F2/F3 的百分比是协议给定 ceiling，也非经标定的真实正确率。此处为作者必要抽样，不冒充非作者复核。

范围外／一般系统应用层的作者题摘抽样亦定点核了[15475 NeuroMesh 官方完整题摘](https://arxiv.org/abs/2604.15475v1)、[16088 HPC 网络官方完整题摘](https://arxiv.org/abs/2604.16088v1)与[15549 SGP 官方完整题摘](https://arxiv.org/abs/2604.15549)。15475 确有分散多机器人 observation 编码、message aggregation、Zenoh 与 GPU/CPU 执行栈，并报告异构空地机器人任务，但没有 foundation/VLA 学习或本书 embodied action–environment 反馈的新受控边界；不能仅因“多机器人神经推理框架”就占 Ch26/82。16088 明确研究 NEST、GROMACS、LAMMPS、PATMOS 的 VEF trace、网络拥塞建模及 HPC collective 情况，摘要提到 deep learning training 只是动机，并未以 LLM 训练 topology、模型状态或故障语义作为测试负载。15549 的真实增量是无线 DFL 下 SGP 非对称 mixing matrix 允许有向通信图，并在作者受限数据/图条件下降低收敛时间；早期题摘判断把缺大模型负载桥当作前闭理由，后续必要原文与独立核已纠正，见下段。15475/16088 仍具体前闭，不是因为机器人或 collective 关键词一律范围外；发现共享反例时只扩受影响层。

**15549 后续纠错已生效：**[必要原文与 Ch36 对读](./V3_15549_SCOPE_REOPEN_AUTHOR.md)显示“无大模型／模型状态”不足以独立支持前闭：原文的有向 mixing 与通信成本—收敛联合选择确实触及 Ch36 去中心化训练。root 有界独立核准 `2+1+2=5` 标准仅报告；作者复核 §2/4/6 和[日期联合链](./V3_DATE_RECONCILIATION.md)后已正式入表。半双工无线冲突时隙和小型分类器实验不桥接常规 GPU fabric、任意 LLM 集群或端到端 SLO；否定侧受影响的“模型规模硬门槛”理由须收回，不以本例普遍恢复所有机器人/HPC 条目。

综述／个案层的作者题摘抽样定点核了[15343 exact-v1 官方完整题摘](https://arxiv.org/abs/2604.15343v1)和[15911 exact-v1 官方完整题摘](https://arxiv.org/abs/2604.15911v1)。15343 的单人自我民族志记录与两位观察者并不隔离具体 prompt、用户状态及物理中断的因果；“attention window 内隔离指令与情绪材料共存，因此逻辑隔离必然结构无效”是作者由个案推得的强机制宣称，不能当已证所有 in-context 防护必败。此项不是因安全题材被忽略，而是缺改变 Ch72 具体隔离责任的可检查设计反证。15911 把既有视频扩散加速分为步数蒸馏、attention、压缩、cache/trajectory 并讨论 NFE 与单步开销；完整题摘没有新增配对比较、失败边界或解决某项已知取舍的独立综合证据，未来议程也不等贡献。两项暂维持具名前闭，但安全个案与综述的非作者负侧抽样仍待执行；不从此次两份题摘推断其所有引文或后续版本。

后续[root 独立六项分层抽核](./V3_ROOT_NEGATIVE_SIDE_FINITE.md)已实际重读 15475/16088/15343/15911/16070/16108 官方完整题摘，逐项维持上述具体前分母关闭；与 apr01 对 15623/15877/15671/16114 的具名核互补。该六项核没有覆盖 15549、15849 或全部 22 前闭；15549 另经 root 有界复核恢复。上述单篇核均不代替最后来源/日期/候选分母 Gate；负侧如再见同理由反例仍要只扩受影响层。

另一次**作者侧、未独立签署**的综述/安全边界抽样复核了五项原始完整题摘，并只对确有歧义的必要正文定点读：[15468](https://arxiv.org/abs/2604.15468v1) 自称 conceptual keynote companion，其六环 semi-executable stack 和三 worked cases 是诊断/议程框架，未给新的 Agent 执行约束或受控验证；[15641](https://arxiv.org/abs/2604.15641v1) 把隐私相似性 blocklist 与已通过检查的 cookie 分开以避 TOCTOU，但研究对象是通用恶意软件/加密核验，完整题摘没有把模型、工具授权或生成状态作为受测对象，仅能作 Agent 安全类比；[15898](https://arxiv.org/html/2604.15898v1) §1/§5–7 明确重述作者既有 SHAP 反例、nuSHAP 修正与先前实验，当前稿没有新的 LLM 评价控制或解决本书现有解释争议的独立综合证据；[15951](https://arxiv.org/html/2604.15951v1) 将 graph×LLM 按任务/图模态/融合方式列目录，跨域 best-fit 仍是归纳而非受控任务条件；[16042](https://arxiv.org/html/2604.16042v1) 的五种 intrinsic-interpretability 范式和成本/性能概览未提供新消融或可复算跨范式选择规则。五项暂维持各自具体前分母关闭，不因综述名称一概排除，更不把上述类比宣称为原文 AI-System 贡献；若非作者发现单项新主张，只重开受影响项。15641 的 HTML 本轮不可取，所用是本地保存的官方 arXiv 完整题摘，不冒充已读正文；其前关闭不要求为不影响贡献判断的正文追索。

作者在相同“领域或一般系统应用”层另核[15814 exact-v1 官方完整题摘](https://arxiv.org/abs/2604.15814v1)与[15919 exact-v1 官方完整题摘](https://arxiv.org/abs/2604.15919v1)。15814 确有几何均匀 replay buffer 与 coarse-layout/fine-pose 双蒸馏的连续校准机制，但实际问题是机器人 hand-eye localization 随场景变化的遗忘，题摘没有将其连接到 foundation/VLA 的动作—环境反馈或本书模型训练状态；不因它有 replay/蒸馏术语自动占 Ch26/29。15919 把 CI 式持续基准流水线用于 HPC／科研软件并加入用户无关操作，摘要说大型模型但具体新贡献仍是一般协作 benchmark workflow，未给 LLM evaluation 构念、模型发布 Gate 或训练 runtime 的新可检查边界；还不能仅凭“AI”与 Ch66 对应而准入。两项目前只属作者具名抽样、维持具体前闭，未被 root 六项独立核覆盖；若后续必要原文证明有主线直接机制则定点重开，不凭摘要断言全部结果无价值。

15549 纠错后作者只复查同层受影响的三份[15647](https://arxiv.org/abs/2604.15647)、[15679](https://arxiv.org/abs/2604.15679)、[15751](https://arxiv.org/abs/2604.15751)官方完整题摘，不遍历宽目录：15647 的80段公共审议标注与novelty/relevance/scope语义记忆衡量的是 deliberation 信息进展，尚无 Agent 执行事实/评价构念的独立反证；15679 把 successor representations 放进 FEP 脑功能框架，在 FourRooms/钥匙导航/MountainCar/PointMaze 展示层级状态动作学习，但题摘未给 foundation/world-model 或模型生命周期的新条件；15751 的mutable-arena指针追逐、因果hash和时延资源证明是通用 Sybil/延迟原语，17 CPU/4 GPU 比较不是 AI 系统的授权、训练或推理约束。三项有具体方法，不以小模型、一般RL或加密名称排除；当前缺少改变本书目标选择的直接桥，故暂维持前闭。15647现abs有04/20后修v2，未见决定当前题摘处置的修订说明；不把Submitted/Updated当first-public，也不为前闭开启无问题的全版diff。此为作者有界负侧复查，非 root 全量核。

### 15660 定点误拒修复（作者必要原文与非作者有限核通过）

[官方 exact-v1](https://arxiv.org/html/2604.15660v1) Algorithm 2 第4–10步把原始私有属性矩阵 `X` 逐列置换为 `X̃` 后连同 DP 模型生成的标签发布；§3.3 却把模型训练的 `(ε,δ)`-DP 延伸为**整个发布数据集**的保证。单记录替换邻接 `x=0` 对 `x=1` 时置换恒等，事件“公开属性含 0”在两输入的概率分别为 1 与 0，任何 `δ<1` 均不能满足 DP。多记录逐列置换也保留各列多重集合；这条直接来自原始 `X` 的发布通道不是 DP 模型输出的后处理。原“隐私来自既有 post-processing，故无新边界”理由失效。只隔离印刷 Algorithm 2/§3.3 的完整保证，不推断代码实现或真实部署泄漏；四个表格任务的 utility 观察仍可保留。作者证据与精确重开条件在[提案](./V3_15660_REOPEN_AUTHOR.md)，[root有限非作者核](./V3_ROOT_15660_FINITE_INDEPENDENT.md)已支持具名窄争议及 Ch72 已有覆盖，正式候选/正文已同步；具名日期链见[日期复查](./V3_DATE_RECONCILIATION.md)。整日来源、日期及候选集 Gate 尚未签署。

### 16054 定点误拒修复（作者必要原文、root有限核已过）

[官方 exact-v1](https://arxiv.org/html/2604.16054v1) §3–5/Fig8–9、Appendix A/B.8：Mind's Eye 的八个视觉抽象/关系/变换任务不只是新分数。相同 benchmark 中，meta-task/step-by-step 对规则归纳若干切片有正向，对 mental composition/transformation 的替代提示多为负向；100→300 DPI 对照在单 Qwen-2.5-VL-7B 上未解释主要缺口。这至少提出 **Evaluation 不能把统一 prompt 提升当作通用视觉推理改进，须按能力操作/提示臂与视觉质量分账** 的潜在边界，直接触及 Ch66 的多模态 EvalSpec；与 Ch66 已有视觉规则/alias 成对实验相邻但并非同一任务条件。原表述“没有具体控制发现新条件”不成立，故撤回前关闭，暂拟 `2+1+2=5` 标准审阅/Only，Books 尚待实际 owner 与独立核，非自动 Integrate。

证据只允许局部描述：作者 Fig9 的提示差通常约 0.4–1.8 点，未给跨模型配对置信区间，不能把它当强因果或一般 prompt 规则；DPI 消融只在一个模型两档，不证明视觉分辨率普遍无关。Appendix B.8 对**模型** MT/PF distractor 的 χ² `p=.44/.52` 未拒绝均匀，但**人类** PF 给 `p=.014`，后文却称“两者均高于 .05”，故不能照录“人类与模型均无 distractor bias”；attention map/单 head knockout也不识别唯一内部机制。root已在[V3_ROOT_16054_FINITE_INDEPENDENT](./V3_ROOT_16054_FINITE_INDEPENDENT.md)核准5分标准Only；未签整日Gate，不因这一例把全部负侧升级全文队列。
