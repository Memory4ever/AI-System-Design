# Apr21 九项有限非作者审阅

审阅者：apr02；报告作者：apr01。访问日期：2026-09-27。实际重新读取当前 AGENTS/研究合同，审读作者两份 `V3_BATCH_16659_16684.md`、`V3_BATCH_16706_16725.md`，独立打开以下必要官方原文和具体 owner。只核本组采用命题，不重扫库存、不遍历附件、不复现实验；未写 Books 或作者 README。本文件不替代日级来源/日期 Gate，也不证明全网零遗漏。

## 结论集合

9 项为：1 个 source→owner 真实 gap、5 个受限仅报告、1 个窄争议、1 个日期隔离、1 个前分母关闭。评分沿本次窄命题：16659/16682/16683/16706/16715 为 2+2+2=6；16684/16714 为 2+1+2=5；16678 日期未定、16725 未准入，不评分。KAIROS 只有源/章节差异通过，尚无写锁、实际正文或写后验收；不能计 Integrate。

日期方面复用作者已记录的组合依据供日级验收，没有把 v1 submitted、Updated 或 current OAI 单独证明 first-public。16678 的更早同家族线索单独隔离；本审阅不重新验收其他八项的公告归属。

## 16659 — 保护行为深入、仅报告 PASS

独立读 [official v1](https://arxiv.org/html/2604.16659v1) §3–5.5、Appendix A/I 的必要配置和反证。冻结 audio encoder、LoRA 更新 LLM 后端后，原来 benign 内容筛选不能代表更新后各模态拒答保持；同样本 audio/text 对照有实际测量增量。§5.3 的两模型反向退化不证明 encoder 架构的单独因果；Appendix A 的 Qwen comply 仅 1 个，不能将 refusal-direction probe 当可靠完整机制识别。Table3 远距离筛选仍有 Qwen 退步，system prompt 只测有限英语单轮协议。

实际对读 Ch72 `Preference Data Admission 也必须检查安全能力重分布`（当前 474–480）：已承载 benign 更新身份、OOD slice、发布回归与隔离 adapter 回退；本项报告音频轴与具体反例，不冒称全部方法 Existing，不新增未经开放攻击验证的普遍安全保证。6 分深入仅报告通过。

## 16678 — 日期隔离及窄公式风险 PASS

实际读 [arXiv v1](https://arxiv.org/html/2604.16678v1) Appendix B Eq35–40、B.1 Eq54–56；独立打开 [ICLR 正式页](https://proceedings.iclr.cc/paper_files/paper/2026/hash/892895fdeba45acd837f1a861a4a30aa-Abstract-Conference.html)，确认同题/作者/正式版本，但页面没有首次公开时间。[OpenReview PDF](https://openreview.net/pdf?id=BjL4CSNJug) 本次返回 challenge，不能声称实际读到其 PDF 或 note 时间。恢复须官方公开 note/正文事件及本窗重要 revision 证据，不从 accepted 推日期。

Eq54 使用 normalized cosine，Eq55 改为未归一化线性 trace 的桥仍有具体风险：r=1、正 F1/F2、X=(1,2)、Y=(1,3)、one-to-one、epsilon=nu=1、phi=log、psi=exp、R=0 时，cosine 全为 1，原 loss 局部导数为 0；Eq35 的 S=1/4[[1,-1],[-1,1]] 给出 XSYᵀ=1/2，raw trace 对 F1 的导数 F2/2 非零。此反例只针对该线性设定的桥，不否定 normalized embedding 的链式导数、固定权重 raw surrogate 的解或全部经验。日期隔离项不评分、不支持 Books。

## 16682 — KAIROS source→Ch70 真实 gap PASS，待实际写入

实际读 [official v1](https://arxiv.org/html/2604.16682v1) §3.3–3.4、6.2–6.3、7–8：降频延长 agent 寿命、积累 context、触发 eviction/recompute，进而继续减慢；控制器按 context 量选频、最慢 agent 的累计 progress boost，并用 beta/gamma 两阈值处理 admission。当前 Ch70 `执行中闲置与 Deep Idle 不能合并核算`（177–186）有 residency/activity/power 分账和 DVFS/cooldown 代价，却缺这个正反馈及频率—admission 联动。Ch56 保持请求调度与状态可用性职责，成本 owner 仍为 Ch70。

建议在 DVFS 条件分支补两段，而非框架摘要：频率不能独立于 context 驻留反馈调优；分别验收频率控制、进度 proxy 和 admission/headroom，保留默认频率与保守准入回退。H100 NVL、单实例 H100 80GB、vLLM 0.14、Qwen3-Coder30B FP8/Ministral14B、3 小时录制请求回放限定实证。P5 是最慢 5% agent 的累计 token/s，不是 request-tail、真实重跑 task success 或整机 goal 能量；饱和/PD 未测边界保留。6 分 gap 深入 source→owner 通过；实际正文、独立写后与日级 Gate 尚未发生。

## 16683 — Rewind-IL 保护行为深入、仅报告 PASS

独立读 [official v1](https://arxiv.org/html/2604.16683v1) Alg1/IV-B–D、V-A、VI：TIDE 为相邻 action chunk 的重叠 MSE，offline VLM/KDE template 与 online slot/action snapshot 分开，触发后执行一个旧 action 并清 queue/ensembler，不能把 slot 持续保存称完整 scene snapshot。10 个成功 episode 的相关 frame quantile 不是 time-uniform failure 保证；单次外部扰动、有限任务/机器人设置限定评价。scene-state 验证与 collision-free 恢复仍在 future work，不能从执行旧动作推出物理精确回滚。

Ch26 runtime assurance、critical-phase trigger→proposal→physical commit（599–612）已有通用责任链。本项保留具体 detector/recovery 分工和限制，不将全部 recipe 写 Existing，也不采用安全复位保证。6 分保护深入、仅报告通过。

## 16684 — DARLING 标准仅报告 PASS

实际读 [official v1](https://arxiv.org/html/2604.16684v1) §3/4.1–4.4、Assumptions4.7/4.10、Remark5.1。forced probe 监测 reward 与 successor feature，触发在 episode 末重置 learner/history；rank 不足时存在不可观测的正交变化，reachability 与足够静稳长度是检测/后悔保证前提。Remark5.1 明确实验几乎均违反这些前提，因此经验收益不能被称为该定理保证；也不能将 tabular/linear episodic MDP 结果直接升级开放 Agent/Transformer 的非平稳承诺。5 分标准仅报告通过，无须为本地条件理论扩写所有证明。

## 16706 — AgentProp-Bench 窄争议 PASS

独立读 [official HTML v1](https://arxiv.org/html/2604.16706v1) §4.4–4.6、5.1–5.5、6.3–6.4、Limitations，并以 [official PDF v1](https://arxiv.org/pdf/2604.16706v1) 首页、§6.3/6.4、p14 局限交叉核当前 2,000 core tasks/2,300 traces/9 models，不能沿旧污染库存。100 human 标签主要单作者，第二人重叠仅 7 项；40-row threshold sweep 不是 held-out estimate。

n=9 的 Spearman 不显著不推出独立或提高 rejection 不影响 recovery，原局限自己明确允许未检出的中等相关。两臂同一 heuristic 也不推出 arm-wise bias 相同，干预改变输出/abstention 分布；没有两臂人工标签不能采用无偏净 mitigation 保证。保留 concurrent 600/arm、有限 confusion matrix 和实际经验，不否定全部实验或一般 stage 分账。Ch66 judge calibration/Outcome Witness 的责任不是未成立外推的授权。6 分纠错深入、暂缓该中心外推通过；重开须相应独立性/等效设计或两臂人工及 abstention-adjusted 分母。

## 16714 — Signed estimation 标准仅报告 PASS，两处定点更正

独立读 [official v1](https://arxiv.org/html/2604.16714v1) §2–3.2/Theorem1、§6、Appendix C 的运行身份。负权不是 categorical probability；两组正负 ancestral samples 的期望差不等直接 target sample；近抵消处 weight/variance、support/integrability 条件和 safe additive component 代价应保持。synthetic/BLR 证据不证明 Transformer/Serving 收益。Ch24 生成路线已有 sampler/target/approximation 分账，不因本论文名称另写通用 signed sampler。5 分标准仅报告的窄采用通过。

本次发现需作者同步的局部不一致：HTML Alg2 初始化 M=Z/Z+，而正文 rejection 段和接受式需要 M=Z+/Z；不采用当前伪码作为 exact RS 实现。例 q+=(1/2,1/2)、q-=(1,0)、Z+=1、Z-=1/4，则 target=(1/3,2/3)，伪码 M=3/4 给两接受概率(8/9,16/9)，截断后输出(8/17,9/17)≠target。此为该伪码局部反例，不否定 signed expectation 分解；本次 PDF 访问失败，未核代码，不能声称实现同错。Appendix C 已披露 runtime 单 RTX A6000、BLR A100/RTX3080Ti，不能把 hardware 全写 Not Disclosed；precision/在线 SLO 则仍不补造。

## 16715 — Sparse attention 并行机制标准仅报告 PASS

实际读 [official v1](https://arxiv.org/html/2604.16715v1) §3/Table1、4.3/Alg3、5.1–5.3：node split+AG 的 K/V 复制与 head split+A2A 的全图复制是不同通信/显存选择，Table1 图存储前者(N+E)/p、后者N+E。研究实际 sparse attention 的分布式数据流和 collective 成本，不是仅将 GPU 名称类比大模型；但不可称已实证 dense causal LLM。Ch36 `Context Parallel 的 buffer 也有容量上限`（495–515）的 head/sequence view 与 buffer trade-off 是相关主线，具体 graph recipe 当前仅报告，不冒称全部已有覆盖。

8×A100 和 8×H100 是两台分别测试的服务器，不是单个 16 卡跨节点实验；hidden128/heads8、PyTorch/DGL2.3/cu121、2 warmups+10 runs 限定评价。§5 明确未给 DistDGL/TorchGT 同口径端到端 speedup，profiling 近似不证明任何拓扑最优。6 分标准仅报告通过。

## 16725 — FliX 前分母具体关闭 PASS

实际读 [official v1](https://arxiv.org/html/2604.16725v1) abstract、§1.2、2.1、3 的 bucket-query 分工及5.2负载：GPU 有序 key→rowID map 有真实 bucket-pull、排序批处理与重整/回收增量，不称无算法创新。原始问题/评价是通用数据库索引，未给大模型计算、向量近邻/过滤检索、模型状态或训练/推理执行的新约束/证据；只引用 machine learning 应用和 GPU 并行类比不足以建立本项目主线贡献。范围/贡献具体关闭支持，不评分、不否定其一般数据库价值。

## 交接和校验范围

作者应同步 16714 两个精确修正，其他处置按以上窄边界。KAIROS 待共享 Books 锁与实际写后，不能因为非作者 source→owner 通过而计已整合。作者已有日期组合仍交日级非作者裁决，UniCon 单项隔离不改为零命中。本审阅仅新建此专属 audit，未修改 Books、README、作者材料或全局 checkpoint；结构/行尾检查与 scoped diff check 单独执行，不冒充语义或整日报告 Gate。
