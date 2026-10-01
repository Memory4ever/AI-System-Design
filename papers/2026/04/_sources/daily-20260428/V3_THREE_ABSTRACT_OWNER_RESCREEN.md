# 04/28 三项完整题摘→实际 owner 有界重筛（作者提案）

此记录只对旧 `retained` 开放线索中的三个身份做贡献准入对照，不冻结当日候选分母、不评分、不改变正式日报处置。分别核了官方 pinned-v1 的完整题摘与目标章节实际正文；提交日或当前 arXiv 摘要版本不当首次公开证据。后续若保留，才做必要方法/实验与当窗日期核。

| 身份 | v1 题摘、当前 owner 与提案 | 尚缺的核验 |
| --- | --- | --- |
| [2604.23455v1 CUJBench](https://arxiv.org/html/2604.23455v1#abstract1) | v1 题摘定义同一诊断任务的 browser-visible symptom 与 backend observability 配对、固定多模态 snapshot/工具接口，并报 browser-only 与 full-toolset 反向。Ch66 当前 EvalSpec、Agent 多轮任务与 trace 结果虽有任务/工具/判据分账，尚未明确“用户可见症状与后台证据能否被同一诊断正确合成”的评价对象。**保留为贡献消歧**，并非仅因新 benchmark 名称准入。 | exact-v1 故障 gold、工具预算是否等量、87 场景五类 fault 的选择偏差；19.7% 不外推一般运维或生产 Agent。 |
| [2604.23466v1 CuTile](https://arxiv.org/html/2604.23466v1#abstract1) | v1 题摘给 H100 NVL/B200/RTX PRO 6000 的同 kernel 跨架构反向：B200 attention 对 FA2 有局部优势而 RTX 约为 FA2 的 53%；也有 GEMM 与端到端 LLM 层。Ch49 当前 Trade-off 已明确写出“可移植语义≠性能等价”、成熟 CUDA fallback、目标硬件 profile 和 standalone kernel≠端到端收益。此研究加强同一命题的具体反例，**作者拟具名前分母关闭**，不是称论文无实验或无价值；需要非作者检验是否还有 Ch49 未承载的决策边界。 | 确认 v1 中 end-to-end 结果没有与现有 kernel→模型验收合同不同的状态/控制责任；不得把 1007 TFLOP/s 或 60 行代码当服务收益。 |
| [2604.24300v1 ReVSI](https://arxiv.org/html/2604.24300v1#abstract1) | v1 题摘明确两个可能不同于现章的评价失效：point-cloud 3D annotation 映射为 video QA gold 时漏标/误标，以及原题在全场景可答、却在 16/32/64 个实际采样帧不可答。Ch66 已要求视频模态必要性消融、causal visible prefix 与原分母，尚未具体承载“gold 生成所见证据与模型实际输入支持集不一致”。**保留为贡献消歧**，不因 381 scenes/5 datasets 自动入选。 | 核 pinned-v1 复标协议、可答性判据/人工一致性与 Ch66 已有 visible-prefix 论证的真实差值；避免把更干净 benchmark 等同 3D 真值或普遍空间能力。 |

对 `.24300` 的进一步必要定位（仍非正式候选审阅）：[v1 §4.1–4.2](https://arxiv.org/html/2604.24300v1#S4) 从原 3D 标注重标对象/几何并重建 QA；[§5.1–5.2](https://arxiv.org/html/2604.24300v1#S5) 按 16/32/64/all 采样重建各自可答题，5% 像素可见性阈值以下交人工判断，16 帧排除通常不可答的 room-size/route-planning，并用移除目标对象帧的 dummy video 检查视觉证据依赖。作者 §7 说明专家复标成本限制扩展；不能把“全帧题库更干净”当同一稀疏输入分母，也不能把 dummy-video 诊断当自然场景 3D 真值。

对 `.23466` 的必要正文反查补充：[official exact-v1 §VII](https://arxiv.org/html/2604.23466v1) **明说 CuTile 尚未集成端到端推理**，Table VI 的四层 LLaMA-7B-like prefill/decode 是现有 PyTorch 后端的上下文参照，不是 CuTile 替换后端的 E2E A/B。§VI 与 §IX 显示同一 attention kernel 在 B200 相对 FA2 强而 RTX PRO 6000 退步，BF16/FP16、单块设备实例、无 Nsight Compute 瓶颈归因，且 H100 不支持 CuTile。故它提供有价值的跨 sm_100/sm_120 反例，但未新增 Ch49 已有“目标设备×实现后端×完整模型”验收合同；作者具名前关闭提案更明确，待非作者准入裁决前不扣工作池。

三项均尚无日级归属或 Books Decision；`.23466` 的拟关闭也未从既有工作上限扣除。

日期优先级仅按已存 receipt 原字段分流：`.23455` v1 `Updated=2026-04-28T00:41:55Z`、`.23466` `00:42:31Z`，可结合公告槽/连续 ID 作有界推断；`.23781` 为 `01:01:10Z`、`.24300` 为 `01:31:31Z`，都在本窗 09:00 北京时间截点后，若贡献保留须先做官方先公告后元数据更新的定点例外核，否则精确 Date Hold。四项的 DOI initial created 均在 03Z 以后，不当首发时刻；后续 v2 可改写当前 OAI datestamp，2026-09-03 的 OAI 日期检索无匹配也不能反推出首次公告日。`submitted` 同样只作 provenance。

补充一项非关闭对照：[2604.23781v1 ClawMark](https://arxiv.org/html/2604.23781v1#abstract1) 的 pinned-v1 摘要与 §3.2/§6 区分五个有状态服务、turn 间外生更新、确定性 post-state checker、weighted progress 和 strict success。Ch66 当前约 820–831 行已实际写出 `pre-turn state → committed effects → exogenous mutation → next-turn observation → post-turn invariant`、living/frozen suite 共存及 checker 不证明 rubric 完整。故旧 `Existing Coverage` 不能仅凭 V2.1 标签继承，却有真实正文承载；作者侧暂保留为有贡献的候选线索、拟 `No Change — Existing Coverage`，待当窗日期和非作者 source→body 定点核后才计正式处置，不把已经写在 Books 的事实倒推为本日首次公开。
