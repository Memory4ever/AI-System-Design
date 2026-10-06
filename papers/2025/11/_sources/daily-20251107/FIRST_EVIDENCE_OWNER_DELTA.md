# Nov07 首批必要证据与 owner 差额

状态：作者必要审阅记录，待 root 独立证据/Books 判断；没有一项已取得足够的本窗首公开证明，不计正式候选分母，不请求现在写 Books。窗口 BJT [2025-11-06T09:00:00+08:00, 2025-11-07T09:00:00+08:00)。准入校准结果见 [FIRST_CALIBRATION.md](FIRST_CALIBRATION.md) 末段，不授予日期或证据完成。

## 优先可核：Shrinking the Variance v1

原源：[2511.03710v1 HTML](https://arxiv.org/html/2511.03710v1)。实际必要阅读：§2、§3.1-3.3、§4.1/4.3-4.5，Appendix A.1、相关实验设置与 B.1-B.3。原始段落见 [机制与评价](nov07-standard-mechanism-eval.txt)、[条件](nov07-standard-conditions.txt)、[估计器核对](nov07-estimator-and-card-check.txt)、[公式核对](nov07-guard-check.txt)。拟评分仍 2+1+2=5，不为 Books 处置改分。

可支持命题：小组 reward mean 噪声大时，可把每条 response 的同 prompt leave-one-out baseline 与排除整个该 prompt 的 batch baseline 混合；混合系数也只由其他 prompt 估计。在论文的条件独立、当前 policy score-function 对象下，这个双层排除使被估计 response 不参与其 baseline/系数。这是 batch 内统计分支，不是 learned critic、历史 prior 或停止控制器。

关键收窄：§3.1 忽略 score-function squared norm，以 baseline MSE 代理 gradient variance；population coefficient 的分析不能直接授予随机 plug-in 系数普适最优性，更不覆盖 clipping、normalization 和旧 policy reuse。B.3 的有限样本推导仍有需复核之处，本次不采用其精确 oracle 系数或普适最优定理。A.1 `v_square_i / (v_square_i + s_square_i)` 没有零分母分支，常数 reward batch 可为 0/0；这是所示参考代码的边界，不声称已运行或作者训练实际触发。

对照：§4.3 GSM8k/Qwen2.5-0.5B-Instruct，500 steps、64 prompts、每题 2/4/8 rollout、5 seeds；Table 1 的 JS 与 RLOO 均值存在局部改善，但表内没有不确定性，不称显著普适胜出。价值真值是另采 32 trajectories 的 MC 估计，20 个 batch 的 MSE 对照不是精确 value oracle。训练输出长度、更新数和采样设置见附录；precision Not Disclosed，不能由少量 baseline 运算推出端到端免费或同 wall-clock 提升。

现有 owner：`TRAIN-GRPO`，[Ch33](../../../../../books/part-04-training-system/33-grpo.md) 的 “Group-relative Gradient 不是独立样本均值” 已解释 LOO score-function 的受限理论对象、组内耦合与预算；后续跨 prompt 在线统计段已解释历史累计均值/方差、当前 batch 并入 prior 的 self-coupling。相邻 [Ch32](../../../../../books/part-04-training-system/32-ppo.md) 的 “Baseline Granularity” 承载 scalar baseline 不提供 token-level attribution。

具体差额与拟位置：若日期和证据独立通过，仅在 Ch33 当前在线历史统计段之后、prompt-level replay 段之前加入一个短的 batch-only double-LOO 分支，明确排除当前 prompt 的系数/全局 baseline、条件独立要求和退化回退；不重写全部 GRPO，不建立新 owner，不把已有 shrinkage 原理当长期缺口。root 也可裁决仅报告；本作者未写共享 Books。

## 三项继续边界

- [Learning Without Critics? v1](https://arxiv.org/html/2511.03527v1)：实际已读 §3、§5-8 的方法/消融/限制；[原始条件](nov07-standard-mechanism-eval.txt)、[边界](nov07-review-boundaries.txt)。主对照同时改变 critic/GAE、gamma 和 rollout horizon：PPO 为 gamma .99、GAE .95、128 steps；critic-free MC 为 gamma 1、整 episode。故不能将差距全部归因于 critic。五个经典控制任务、1M environment steps、10 seeds 的负结果有局部价值，但 grouping 是随机 reset episode，不是同 prompt responses；不得外推为 LLM 上失败。现有 Ch32 “Baseline Granularity” 与 Ch33 同条件组比较已承载 attribution/group condition 警告，倾向已有覆盖该边界、仅报告具体负验证，待 root 裁决，不强造差额。拟 2+1+2=5 不变。
- [SnapStream v1](https://arxiv.org/html/2511.03092v1)：实际已读 §3-5 与有关伪代码，PDF 同版本已打开；[方法/评价](nov07-standard-conditions.txt)、[必要反证](nov07-review-boundaries.txt)、[代码核对](nov07-guard-check.txt)。固定物理结构为 sink、recent ring、prefill-only Top-K，decode 只更新 recent，`valid_topk` 区分容量与有效 token。新差额可定位 `INFER-KV-CACHE` Ch45 的压缩/eviction 交接：静态形状 consumer 必须保留有效性与 slot 生命周期，不能只记录 Top-K 预算。旧文已有 budget/质量/阶段成本原则，不是名称缺口。质量表有 Aggregation、KV retrieval 等退步；吞吐用各自最大 batch，且乘 2.4 假定 MTP 80% acceptance，不称直接实测最终输出吞吐或 SLO goodput。Eq.4 与 Listing 5 索引疑点待 exact PDF 核对，不采用该公式/代码作正确实现。拟 2+2+2=6 不变。
- [Kimi K2 Thinking 历史 card](https://huggingface.co/moonshotai/Kimi-K2-Thinking/blob/f5ed4a8f7f535ecd0625df17878fd6731e5af7ed/README.md)：已实际读该 commit 的 §3 评价脚注、§4 QAT；[原始历史卡](nov07-precise-core-final.txt)、[QAT 与设置](nov07-estimator-and-card-check.txt)。仅可支持 post-training QAT、MoE INT4 weight-only、所报 benchmark 均 INT4 的作者事实。没有 matched BF16/no-QAT 对照、quantizer/训练 recipe 或硬件/batch/SLO，不能认证无损 2x。长程工具有 step/token caps、超过 256k 隐藏既往 tool outputs、定制 harness，heavy 为 8 条 trajectory 汇聚；不以榜首证实 runtime 稳定性。QAT 命题由 training/通用低精度 owner 负责，不能因框架可部署路由 TensorRT。未披露新的 QAT 机制，现阶段倾向仅报告；不以未见模型名提出 Books 整合。

## 最小日期证明缺口与停止条件

上述四项都未取得可完全落窗的公开时刻/上下界。这里不复用常规 schedule 造时刻，也不把所有尚未读材料转为 date hold。

1. 三篇 arXiv 的原字段是提交：Shrinking `2025-11-05T18:43:15Z`；Learning `2025-11-05T15:01:32Z`；SnapStream `2025-11-05T00:38:31Z`。Atom published 仍为提交。Shrinking DataCite Updated/DOI created 只作元数据线索；已取得官方 OAI [GetRecord](arxiv-03710-oai.xml)，v1 date 仍是提交，header datestamp 为最新修订日期。OAI 不提供需要的首次公告，停止向另外两篇复制同一空路径。
2. Kimi 官方 Blog 字段 `2025年11月06日` 时区/精度不足；历史 card commit 日期不等于 repo first public。官方论坛 `created_at=2025-11-07T03:27:30.356Z` 在窗外，指向 [官方 X 公告](https://x.com/Kimi_Moonshot/status/1986449512538513505)，但 X 403、syndication/oEmbed 有限替代未得到公开时刻，不用 Snowflake 计算替代原证据。

最小可接受材料：arXiv 官方历史公开 batch 中该 ID 的实际归属及足够区分两端 09:00 的公开证据，或作者首次公开正文/公告的原始时间上下界；Kimi 上述官方公告可读 timestamp，或官方首公开正文的原始时间。证据须落入 BJT [11/06 09,11/07 09)，若恰 11/07 09 则归下一 Daily。

当前停止盲追：不再重试 HF API、X/syndication 或三篇 OAI；不扩读月表所有题摘。普通可执行下一步为继续已校准必要 PDF 核对、当前 Books 具体论点比较，以及未读相关题摘初筛；日期仅在取得上述确切原始记录时重开对应材料。root 若有本窗公告原件，可立即补入这条最小链路，不需重读已完成的原文部分。此文件不是日期 Gate 通过或 Books POST。

## 普通待办未关闭

窄查询内其余语义相关/含糊题摘已分批实际读取；具体理由正在落盘，不因本批审阅费时删池。潜在机制项的 exact-v1 身份、纠错信号、必要准入补读仍是普通待办；尚未初筛/审阅不是外部受阻。14 个每日入口的动态历史边界仍需逐源有限恢复并如实隔离；SnapStream PDF 会议模板触发 MLSys 定点查证，不从模板认定会议发表。日级独立复核、正式 README 与本日全流程尚未完成，08-12 尚未启动。

## 后续实际核对（2026-10-04）

SnapStream exact-v1 PDF 必要索引核对已执行：[PDF 原始提取](nov07-pdf-reopen.txt)、[Eq.4/Listing 5](nov07-snap-pdf-index.txt)。PDF p6 Eq.4 加 `Lsr`，而 p16 Listing 5 的 ring index 加 `sink_token_length`，且后续 scatter 仍消费 `cache_position` 而不是刚计算的 `ring_buffer_index`。这些原文问题不只来自 HTML 转换；不能直接采用公式/代码或声称实现正确性已核。PDF screenshot 两页均为 cache miss，记录见 [失败原响应](nov07-snap-pdf-screens.txt)；不继续空截图路径。按结构描述能支持的命题保持不变，公式与参考实现单独隔离。

25项选定完整题摘与逐项具体理由已保存 [TOPIC_SCREENING.md](TOPIC_SCREENING.md)，不是全部61+13条逐项关闭。SRC-OPENREVIEW 已实际触发 Common-O/UserAlign 的 NeurIPS 公开身份核对；两个 forum 和对应 API 原响应为 challenge/403，停止同路径，不能从接收标签推出首公开。Z.ai Research 原生 page2 `hasMore=false` 的18条展示 `createAt` 最早为2025/12，`createdAt` 是 CMS 插入字段；当前目录历史截断不能证明11/06没有论文。官方 release notes 可读且9/30与12/08之间无本窗条目，只支持该 release 列表的结果。Hunyuan 本轮浏览器有限恢复依次出现子任务不支持 visibility 参数、去掉该参数后超时/reset；没有取得历史“全部”列表，保留历史目录缺口，不继续重复初始化。

最新交接：[CURRENT_STOP.md](CURRENT_STOP.md)。正式README现已建立、V3格式检查此前通过，但普通工作与§6未终态；上文“README尚未完成”为较早停点，不是当前无文件状态。首批未变证据不重审，日期/Books仍未授通过。
