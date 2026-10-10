# 10747 Pneuma-Seeker：独立必要 Source / 评分 / actual owner / PRE

复核者：mar13_admission_review（非准备者；准备者 mar13_supplement）。仅 2026-03-13 既有 Daily 的 2026-03-12 北京时间自然日补查；不加载其他日期候选。本次只写此文件，不写 Books、Report、State 或共享 ledger，不授实际 POST / DAY。

## 范围、身份与停点

启动恢复实际重读 AGENTS、当前 Research / Report / Sources 使用说明与 Daily、arXiv 范围、统一 Prompt、ROADMAP、本日报开头及 LEARNING_STATE 最新相关路由。日报仍进行中，原窗口、原候选与连续 §4 不搬移。有效本 ID 准入与日级 arXiv 日期夹证复用，不重新追公开时分秒。

实际读准备包 [SUP_EVIDENCE_10747.md](./SUP_EVIDENCE_10747.md)，然后独立回官方精确 v1 原件 [SUP_CORE_10747.raw](./SUP_CORE_10747.raw)：完整 §3–5、完整 §6–7（含两张完整 Table 1 / 2），使用原 HTML 的正文/表格与 math alttext 投影，不照包裁决。读取完整题摘 [SUP_ABS3_10747.txt](./SUP_ABS3_10747.txt) 与原件首页身份。原件 [manifest](./SUP_CORE_10747_MANIFEST_RESULT.json) 指向 https://arxiv.org/html/2603.10747v1，GET 200、342051 bytes、2026-10-10T03:17:30.056885Z，未发生版本替换。

题摘与 HTML 正文题名不同，但同 ID / 四作者 / 完整摘要对应；分别保留题摘的 “A Relational Reification Mechanism to Align AI Agents with Human Work over Relational Data” 与正文的 “Relational Reification of Information Needs for Agentic Data Discovery and Preparation”。可见题摘仅 v1，无 Comments、撤回或纠错说明；正文 PVLDB 14(1)、2020、XXX / doi XX 是未填模板，不授真实早公开日期。未打开旧 Pneuma 全历史、代码、其他版本、图像像素或全引用。Figure 2–6 只读原文解释 / caption，不采用未视觉核验的 bars 或精确 Pareto 坐标。

## 必要支持与直接反侧

- §3 的目标确为 `(𝒯,S)`：`𝒯` 是多个 derived views，而不只是已有 schema；`S` 是其上的 SQL / Python 答案转换。先定义目标、独立物化视图，再执行答案程序。用户可根据 schema、样本、口径与群体差异修订目标；ProvenanceGraph 记录构造操作和来源依赖，拓扑排序后附 `S` 得可运行脚本。这支持目标解释 / 数据构造 / 答案执行的接口分责，不证明目标忠实、原始数据完整或实际执行正确。
- §4.2 / §5.1 的 micro action 是执行查询探测实际值、分布与结构后改变目标。§7.1.2 的 capital 示例从非空筛选改为 `primary`，说明运行成功也可能计算了错误人口；不是用模型自述置信度代替数据。
- §5.1 / 5.2 两 loop 默认各 10 轮。Conductor 选择 user-facing communication 即停，耗尽轮数也强制合成回应，停止不是全部物化或语义验收。Materializer 可以 structured join / union / projection，也可 semantic join（默认 top-1）、LLM 生成 semantic columns、自由 SQL / Python fallback；因此整条语义计算不能继承纯确定性正确性。独立 workspace.db 只支持所述存储设计，不认证 sandbox / tenant isolation / 事务完备。
- §5.3 的原 Retriever、3 queries × top-10、entity regex 内容扫描、表名枚举是具体发现接口；不计成熟检索 / SQL / DAG 为本稿独创，不授全集召回。§7.1.3 在 identity-theft 单例中，显式 `[state, metropolitan_area, num_of_reports]` 目标加 union-all-name cue 使结果从 114392 改为 243377；无目标消融仍能枚举表，差额是给物化传递覆盖意图，不是“只有新系统可枚举”。
- §6 是两个定性案例：41 表 / 15GB procurement 加 7MB FY2025 Oracle 表，作者将原问题当 `I*`，手工造模糊 `I+`。null acknowledgement、hazardous / radioactive 重叠，以及年度字段、金额字段、ID / dedup 差异确实提供可检查修订线索；不等独立用户 study、不认证普遍收敛 / 用户信任 / within-minutes 生产效率。
- Table 1 六域共 88 题（12/4/9/17/28/18），是过滤后的 tabular questions；采用一般接口，不把领域端点引入暂缓的 Science 路线。§7 使用 M4 MacBook Air / 16GB / Python 3.12.12 / o3-2025-04-16 / text-embedding-3-small，仅 local tables；web / crawl / knowledge store 关闭。部分 baseline 限 5 sample rows，Astronomy 的 DS-Guru 连每表 1 行也超过 context 而省略。sets / lists 用 F1，其余用正确比例；94.44% / 9 题不能硬换算成 binary 答对数。
- §7.1.2 只报告 micro action 在 4/5 数据集改善，不能按六域 overall 擅自补人口或宣称每域改善。§7.1.3 移除目标定义和物化两项责任，不是 schema 文本的唯一因果消融。§7.3.1 弱模型 49.95% 只高 smolagents 1.14 pp，无 CI 不能授显著；重复 runs / seed、判分者与独立标注细则、并发 / SLO 等在必要段 Not Disclosed。
- 完整 Table 2 保留负侧：Environment Pneuma 126.08+3.62s，对 smol 73.96+3.96、DS 40.25+5.85；Legal 106+2.92 对 76.48+3.73 / 32.16+0.78；Wildfire 94.41+3.36 对 68.64+4.34 / 27.92+62.10。前者总时均高于这些比较对象。§7.3.2 Legal 内存 116MB 高于 43 / 25，Biomedical 186 高于 smol 135，不授全负载降本。
- §7.2.2 的 1GB 披露分量加和为 Pneuma 59.11s、smol 55.69s、DS 63.44s；正文“DS-Guru overtakes both at 1GB”的精确速度叙述不能由这些数字支持，隔离此句，不否定其他经验结果。1.9GB smol 更省来自 noisy-string 触发更换处理 pipeline，非同流水线规模因果。§7.3.3 还报告 Legal recall 94%，不能从补表单例认证全部来源覆盖。

索引、summary / embeddings、内容 scan、目标协商、两 loop / probes / materialization、模型调用、依赖图 / 持久视图、人审都需核成本；论文 monetary cost 是 token inference 及作者 Feb27 定价口径，不授当前价格或完整总费用。此处成本项的完整核算要求是复核者系统推断，不假称稿内已测。

## 三维评分与 actual owner 差额

`1 + 2 + 2 = 5` 成立。D1 只计目标关系 / 答案程序与物化分责的局部实现，没有把 SQL、关系算子、DAG、动态规划或 macro / micro 标签借来加分。R2 是可由用户改的目标对象→数据发现 / 构造→答案执行的实际跨边界交接，不是可联想到章节数。Durability2 是把目标语义、数据人口与执行独立验收的稳定界限，§6 / §7.1.2–3 的具体混杂与遗漏改变如何解释“查询运行成功”。因已确认现章长期缺口，深入仅受影响命题；必要支持 / 反侧已充分，不自动扩全附件。

实际顺读 [Ch79](../../../../../books/part-07-agent/79-planning.md) 90–190 的完整 Decomposition / dependency / replanning / compiled-domain / predicate-first 局部，以及 342–395 的 Goal / Project2Task / Verification；另顺读 [Ch75](../../../../../books/part-07-agent/75-context.md) 1–148，及 Ch76 / Ch78 本章入口与职责。

唯一 owner `AGENT-PLANNING`。Ch79 177–179 已讲固定 domain artifact 的 schema / 约束解释与可复用 solver 分责；181–183 已讲 predicate / arity 自一致不证明真实语义；355–372 已有 task contracts。这些**没有承载**仍可与用户协商的 derived-relations 集合 `𝒯` 与答案程序 `S` 分离、probe 后修目标、按目标物化、暴露整个构造依赖的具体交接。故不是主题式 NC，也不重写已有编译分支。Ch75 已有 production-code 派生表与 live observation 权威不同，但不拥有这里的目标协商 / materialization planning；Ch76 仍拥有源检索 / 覆盖，Ch78 仍拥有执行权限。无需新章或多 owner。

## PRE 裁决

受限 Source 与 score / owner-gap 通过；两段 PRE 在 compiled-domain 两完整段后、predicate-first 分支前可采用，保留前后原分支。第一段有一个最小准确化：

> “它们证明的是已编码操作怎样产生结果” → “它们展示的是已编码操作怎样产生结果”。

原因：DAG / 可重跑脚本展示可检查构造，不自动提供实际运行正确证据；尤其 semantic column 仍由 LLM 产生。其后的“不证明目标忠实、源完整或语义列真实”应完整保留。

其余原位两段通过：不承诺普遍收敛 / 用户信任、明确消融同时改目标与物化、保留某些总时 / 内存退步及预算耗尽仍可不完整。没有采用精确 1GB 速度、图中 Pareto 或各域消融数值，不受上述局部冲突影响。fallback 回澄清 / 原始数据 / 可检验查询是限定系统建议，不假称论文证明必然正确。

实际复读作者原位修正后的 packet：第一段已是“展示”，1GB 加和冲突亦已近成本说明隔离；其余采用命题未变。本文件局部 diff-check 无空白问题，六个本地引用目标存在，仅此本人独核文件新增，无 stage / commit / push。

结论：限定 Source / 5 分 / actual owner 差额与已修正 PRE 通过。尚未写 Books，不授实际 POST、正式报告同步或 DAY；后续若 root 写入，须真实非 writer 检查实际新增、完整邻接与本人 Review note。本项支持与关键反侧已够，停止扩大研究。
