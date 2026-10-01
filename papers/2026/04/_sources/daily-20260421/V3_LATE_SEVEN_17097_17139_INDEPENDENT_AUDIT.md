# Apr21 晚批七项独立采用复核

复核者：`/root/apr01/apr21_late_adopt`，非作者；实际访问 2026-09-27。只复核已准备必要证据的 17097/17102/17111/17112/17126/17132/17139，不新发现、不扩题摘库存、附件、版本史或年份。窗口沿用 `[2026-04-20T09:00:00+08:00,2026-04-21T09:00:00+08:00)`，**本轮不重新验收日期、分母冻结、来源覆盖或全日 Gate**；Submitted/Updated/OAI 均不在本轮被重命名为 first-public。

当前合同与 ROADMAP 延续同一有界任务中已经亲自完整读取的版本。实际读三份作者必要证据：`V3_BATCH_17097_17108.md`、`V3_BATCH_17111_17132.md`、`V3_BATCH_17139_17145.md`，随后逐项定点重开官方 exact-v1 方法、关键评价与反证；不是凭作者结论签收。未访问未列入本轮的其他候选，未复现实验或代码实现，不声称全理论/附件审查。

| 候选 | 作者处置 | 本轮结论 |
| --- | --- | --- |
| 2604.17097v1 | 5，标准，仅报告 | PASS；另明确 47% 为非加权模型均值 |
| 2604.17102v1 | 5，标准，已有覆盖 | PASS；Existing 仅指配置/预算评估命题 |
| 2604.17111v1 | 5，标准，仅报告 | PASS；API 存活不等 whole-run 恢复 |
| 2604.17112v1 | 6，标准，仅报告 | PASS；相似度估计器不等真实概率分解 |
| 2604.17126v1 | 5，标准，仅报告 | PASS；混合目标不能全当同义不变性 |
| 2604.17132v1 | 6，保护深入，仅报告 | PASS；signed-score 排序不等采样分布/安全保证 |
| 2604.17139v1 | 6，保护深入，仅报告 | PASS；保留 RR 经验，隔离谱隙→真值收缩桥 |

## 17097 — 表示链与幸存分母

实际打开 [官方 HTML/v1](https://arxiv.org/html/2604.17097v1) 的 III-A/B/C、IV-B/C/E、Table I/II、V-A；本次 HTML 定位包含第 100–181、194–215 行。lowering 后 Verilog 修复和 simulation-passing 后 FPGA 评价属于不同对象，不能将 conditional FPGA pass 写成原始任务端到端交付率。三模型、六 IR、202 教学任务、两 Lattice 目标，不支持工业芯片或生产 SLO 外推。

独立核表：HLS 的三模型 ECP5 为 13/20、2/6、3/7；约 47% 是 `(65%+33.33%+42.86%)/3`，合并幸存者是 `18/33≈54.55%`，两者均低于 iCE40 的 33/33。作者约 47% 与官方 IV-B 的模型平均口径相容，但不能冒称 pooled rate。较大目标不必成功、双失败不完备定位源码语义，因 backend/接口同时变化；训练语料解释也不是 corpus 干预结论。

实际对读 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 第 157–180、517–521、586–603 行的完整对象、阶段 receipt 与端到端/孤立能力分账。它覆盖长期原则，不等整套 IR/physical-artifact 实验已实现。PASS Only；不新增 FPGA 指南或 Books 保证。

## 17102 — 配置、选择预算与能力对象

实际打开 [官方 HTML/v1](https://arxiv.org/html/2604.17102v1) 的 III、IV-B/Table I–III、跨基准相关分析；本次定位第 89–109、135–191 行。26 模型基线与 pilot 选出的三模型、四参数 108 配置 sweep 不是同选择预算的因果对照。Global HQI 的 best-of-five 与 Expected HQI 的五次均值、pass@1 与 pass@5 不能互换。

原文 GPT-OSS 的跨基准 Spearman `ρ=.23,p=.016` 是弱且显著的关系，不是完全无预测能力；其他不显著结果也不证明独立。部署吞吐/费用混入 serving infrastructure，不能只归因模型权重。

实际逐项对读 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 第 149–180 行：Observed Capability/Elicitation Ceiling 已要求拆分自然表现、诱发预算与监督上限；完整对象明确列出 runtime/decoding configuration，并单列 protocol adapter 的身份与语义等价责任。第 517–521、586–603 行保留阶段/端到端结果。PASS Existing **仅对这些长期命题**，不声称书稿已有 RTL sweep 全算法、通用最佳温度或全部实验结果。无新增 Books 缺口。

## 17111 — API 协调不是业务恢复

实际打开 [官方 HTML/v1](https://arxiv.org/html/2604.17111v1) 的 3.1–3.7、4.1–4.4、5.1–5.4/Table 5–7、7.2；本次定位第 174–380、433–453 行。condition-counter 缩容只约束后续准入；集中 retry/AIMD/滑窗/熔断协调 API。mock 的首个不可恢复错误即死亡与 retry budget 会影响存活比较；Table 5 replay 18% 失败和 Table 6 Full 0% 不可合并成确定单次因果结果，缺少解释此差异的重复 run/置信证据。

本地两 server 的 direct/proxy 均零失败并未触发云端 stampede。3.7/4.4 已将 SSE chunks 向下游即时发布；即使上游重试成功，仍缺已发布 prefix 撤回、重复计费与外部副作用去重合同，不能由 API 成功推出 exactly-once 或整 run 恢复。7.2 明确文件/工具协调不在范围内。

实际对读 [Ch84](../../../../../books/part-07-agent/84-agent-platform.md) 第 78–90 行：AgentRun 保存 retry/side effect/terminal evidence，Tool/Environment 拥有真实副作用，请求成功不等任务完成。该 owner 已覆盖分权边界，不冒称已有完整 proxy 配方。PASS Only，保留受限消融；不采用通用 OS 类比或生产恢复保证。

## 17112 — cross-model sensor 与真值的距离

实际打开 [官方 HTML/v1](https://arxiv.org/html/2604.17112v1) 的 3/Eq1–4、3.3、4、5.1–5.3、A.7/Table 7、A.8–A.10；必要定位第 109–210、444–477 行。直接代数核得 `AU=1−self`、`EU=self−cross`、`TU=1−cross`。跨厂商/同规模不证明 ensemble 平均等理想分布：全部模型稳定给同一个错误答案且 similarity=1 时，三个量均可为零。这只反驳 truth/calibrated-probability 的无条件解释，不否定异构错误下的经验判别收益。

A.7 确有反向 slice，例如 Mistral Word Sorting 的 AUROC `.529→.429`；主文任务平均改进不能写成每模型每任务改进。5×2 与 1×10 匹配响应数，不等部署资源/加载时间；A.9 顺序 L40S 的 `391.7s` 对 `244.1s` 保留额外 checkpoint 成本。A.10 的 gold-conditioned LLM judge 不升级为独立真值 oracle。

实际对读 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 第 1810–1830、1865–1866 行：同源一致性只是 distribution description，多 scorer 只是需校准 sensor。具体 cross-self 估计器仍可报告，不因此改称全算法 Existing 或严格 AU/EU 概率分解。PASS Only。

## 17126 — 固定 proposal 只隔离接口，不建立质量 oracle

实际打开 [官方 HTML/v1](https://arxiv.org/html/2604.17126v1) 的 2/Algorithm 1、3、4.1–4.4、5.3；必要定位第 58–159 行。固定 DETR proposals、CLIP crop similarity 与 argmax 确可定位选择接口变化；但 woman、boy-with-hat 会改变目标谓词，不能把六提示所有选框差异叫同义 prompt 的不变性失败。263 COCO、DETR-R50/CLIP-ViT-B32、单 L4、冻结权重限定范围。

GT 只策展样本，5.3 将同义/异义拆分与 IoU 评价留作未来；定性 ensemble 例图、PCA lobe 与 `r²≈.34` 没有整体质量 oracle 或受控 selector 替换，不能证明总体质量下降、argmax 唯一因果或任意开放感知失败。

实际对读 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 第 1843–1855 行的 target-changing/target-preserving 两臂及独立样本身份。原则已有，论文具体接口诊断并不等所有算法已覆盖。PASS Only；不新增可移植的 grounding 保证。

## 17132 — 真实保护审查，保留 greedy、隔离概率与安全保证

实际打开 [官方 HTML/v1](https://arxiv.org/html/2604.17132v1) 的 3.2–3.3、4.1–4.4/Table 2、Limitations、Appendix H Algorithm 1；必要定位第 118–190、237–273、471–532 行。extreme/raw 在同前缀做两 forward，contrast 为 softmax(logit 差)，top-1 rank 倒数与 confidence 联合切换加/减；只作用首 k token 后回普通 greedy。

独立逐式核：两基础 softmax 均归一化，因此正文 `P_extreme ± αΔP` 总质量为 `1±α`；α=4.5 时分别 5.5/−3.5，不是合法采样概率。**有限 signed scores 仍可 argmax**，故这个问题不推翻 Algorithm 1 的排序机制或全部实验。原文样本使用 greedy N=512，Qwen thinking 关闭；代码中的 masking/normalization 未在本轮复现，不自补实现。

Table 2 的 Llama 恶意平均拒答率 `99.28→99.10` 反向，不能用跨模型平均作逐模型安全保证；拒答排名更不等内容级危害真值。WildGuard 与 GPT-4 判分、固定参数、无人工验证均保留。实际对读 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 第 29–34 行：decoding constraint 不能覆盖 policy gate，utility/coverage/绕过要重测；[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的完整身份与 sensor 边界亦不可省略。PASS Protection Deep Only，不采用保持安全保证，不以关键词关闭。

## 17139 — 轮转经验与潜势收缩之间仍缺桥

实际打开 [官方 HTML/v1](https://arxiv.org/html/2604.17139v1) 的 3.1–3.3、4/Definition 2–3/Assumption 1–2、5.1–5.2/Table 1、6–7、Appendix B、D.1/Table 3–4、D.2；必要定位第 89–148、158–233、307–320、380–424 行。RR 交接 K-token 共用前缀，RRMaj 再聚合 M 条轨迹。N=5、六推理任务与注入威胁模型支持受限经验，不等真实开放 multi-agent 安全。

独立算出窄反例：`θ=e1, TH=diag(1,.5), h=(a,0)` 有主特征值 1、谱隙 .5，但 `V(h)=log(1+exp(−a))=V(THh)>0`，不满足 `V(THh)≤.5V(h)`。取 a=1，两边为 `.31326` 与 `.15663`。**谱隙本身不足推出该 truth-potential 收缩**；这不是满足完整额外收缩假设后又反驳 Appendix B 的代数。实际 LLM 的 truth direction、算子/扰动界校准仍缺，经验提升不能填此桥。

D.1 强污染 4c1t 的 RRMaj `M1→40:40.3→33.5`，moderate 4c1t `M30→40:83.0→82.7`，足以否定普遍单调扩算收益；Table 1 保留少数污染退步。D.2 Fisher 不显著不证明最后 speaker 独立，`N×L` decode 预算不包含 switching/prefill 的同 wall-clock 证明。

实际对读 [Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 第 443–462 行：相关错误、aggregation/visibility/control authority 与独立 verifier 的风险链已存在，更多讨论不自动修复。RR 并非全部已有实现，也不足新增通用安全首选。PASS Protection Deep Only，保留经验机制、隔离普遍真值保证，不以关键词关闭。

## 有界结束

七项采用结论在上述实际最小范围内 PASS：六 Only、一 Existing，其中两项保护深入。17097 聚合口径只作精度澄清，不抬分、不改判。仅新增本专属审计文件；未修改 Books、正式 README、作者 notes 或共享 checkpoint，无写后 Books 验收或新增 Integration 数。没有全日完成声明、日期 Gate 或库存闭合声明。七项完成即结束，不接下一日或新队列。

落盘检查：新文件空白检查无诊断，本地四个 owner 链接目标存在，owner 所引具体段落已重新核行。新文件仍未 stage/commit；这些检查不替代语义、实验或日级验收。17097 正式正文/作者 notes 的后续同步由作者持有，本轮未签收尚未实际读取的后续修改。
