# 04/29 两项候选的必要证据与准入边界（作者侧，非日 Gate）

本文件只核第二个有界题摘小批中的 `2604.25012v1` 与首批中的 `2604.25072v1`。二者都在 106 个已完整题摘身份里、原已标潜在；下述审阅不增加工作分母，不代表最终当窗候选/首公开或独立 Books Gate。身份落 04/29 08:00 北京 arXiv 批次的依据和反向例外见 [`V3_REOPEN_NOTES.md`](./V3_REOPEN_NOTES.md) 页首；不把 v1 提交字段单独当首公开。

## 2604.25012v1 SWIFT：结构先验摊销 ≠ 免验收的自动 Workflow

[官方 exact-v1](https://arxiv.org/html/2604.25012v1) §3.1–3.3、§4.1–4.4/Tables 1–5、§5 和实际 [Ch82 的 multi-Agent topology/typed handoff 段](../../../../../books/part-07-agent/82-multi-agent.md)已定点比较。旧路线对每个新任务各自做 MCTS/进化式 workflow search；作者先把其它任务已有的优/劣搜索轨迹提炼成 operator-level 结构启发 `H`，另从“中间得分、最终输出解析失败”的轨迹提炼 node 间 output contract `C`。目标任务做 leave-one-task-out，不把本任务数据/轨迹/已优化 workflow 注入 meta-prompt；在线据 `H+C` 和跨任务 demos 一次生成可执行 graph。这不是只给 prompt 多放几个例子：实验把**跨任务可迁移的拓扑、输出接口、目标任务自己搜索**作为三种不同成本/权限对象。

受限支持与反证：Table 4 移去 `H` 或 `C` 各使四个主测数据的平均分从 `82.04` 降至 `78.27`/`77.94`，随机改 operator 名仍为 `77.09`，仅支持所测 prompt/demo 协议下结构有用，不证明模型已识别唯一抽象 program。§4.2 的每目标任务 synthesis 约 `$0.004` 是**边际**成本；原作者也算若把来源搜索预算约 `$112.50` 计入，约五个下游任务才 break-even，不能把“5000×”当包含全部准备成本的净节省。OOD Table 2 的 BigCodeBench 只 `31.6→34.3`、AIME `8.3→14.6`；Table 5 的 Gemma MATH **反退** `58.23→48.35`。§5 明说静态数学/代码 benchmark 不覆盖有不可逆 effect 的 Agent 环境；§E.4 把 BigCodeBench 大量失败归缺模块，但该归因未凭本论文证明真实工程环境可忽略运行依赖。跨 model transfer 还需冻结 operator library、schema/接口、执行 harness 和目标族相似性，不能承诺一遍生成后无需执行验收。

作者侧拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`、Standard 候选。Ch82 已有“topology proposal ≠ executor/reward authority”和 typed handoff，但没有具体“**来源任务优化轨迹作为带版本的结构先验，可在新任务免逐任务搜索；接口 contract 必须随图编译并由新任务 executor 回归验收**”这一成本/回退判断。可能的唯一 Books owner 是 Ch82，Ch84 只接 workflow registry/version/runtime admission。此是真实窄 gap 提案，不因此直接写共享 Books；需非作者核 exact-v1 成本分母、Gemma/BigCodeBench 反例和 Ch82 相邻文本。若 source/owner 核认为既有段已具体吸收摊销与目标任务验收，应判 Existing 或 Only，而不是因为题名含 Agent 就 Integrate。

## 2604.25072v1 XTC-Bench：同事实双向一致 ≠ 两项单向高分

[官方 exact-v1](https://arxiv.org/html/2604.25072v1) §3.2–3.3、§4.1–4.4/Tables 2–8、§5，与 [Ch23 的统一理解/生成表示](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)及 [Ch66 评价责任](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)定点比较。作者从 COCO/Visual Genome 各 1000 图抽 scene graph，围绕同一对象/属性/关系原子事实造理解 VQA 与生成 prompt，再按生成图和原图做 label-group Hungarian 匹配，以 `G`、`U` 和同事实的 CCTA 量化两方向；AW-CCTA 额外乘两方向平均事实正确度，避免两边**同错**也得高一致。Table 4 的 MMaDA raw CCTA `0.630`、AW-CCTA `0.144` 对应这个明确评价反例；Table 8 的人工切片 raw CCTA 与可靠性 Spearman `0.39`、AW-CCTA `0.86`，只是所选 fact-triplet 协议中的相关，不是生产任务质量保证。

必须分账：Table 2 的 matched-node coverage 在所测模型差异很大，Show-o `14.3%`、MMaDA `39.1%`、BAGEL `79.3%`；Matched Rel 看似都高不能替代对象召回。§3.3 的 CCTA/AW-CCTA 对 `F` 的措辞是生成/理解共享事实，Table 4 却标 all nodes；在缺失节点如何给 `g_f` 赋值、`F` 是否扩成原始全体事实尚未从已读公式单独确定，因此不可把数值当完整场景覆盖率或证明所有未生成对象已有一致性。另一面 §3.2 的 graph matching 不设最大 cost rejection，同 label 耗尽前强制配对，可能把语义不同的同名对象错配；人工子样本报告总体 scene-graph 质量约 94%、judge 相关约 `0.892`，仍不是每模型/每切片的无偏真值。商业 `GPT` 是 `gpt-image-1.5+gpt-5` 组合且仅给两个单向参考列，不能称一个统一模型的 CCTA 对照。§5 明确 black-box protocol 不定位内部 representation/训练目标因果，静态图像不外推视频/音频。

作者侧拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`、Standard 候选。Ch23 具体说共享 backbone 不等于同一证据标准，但尚未指明“**冻结同一 scene/fact identity，分别量理解正确、生成正确、两向 agreement 与同错**”的评价验收。Ch66 是评价 harness/分母的可能唯一 owner，Ch23 是设计动机和相邻交接；在 14 源/日期和贡献分母未冻结前暂不申请 shared Books 锁，先请非作者核论文公式 `F`/Table 4 的覆盖口径和现有 Ch66 实际命题。不能从相关的架构族均值断言 AR 目标在因果上更统一，也不能用单 benchmark 发布全模态表示一致性保证。
