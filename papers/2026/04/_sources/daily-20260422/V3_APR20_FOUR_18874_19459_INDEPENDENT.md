# 04/22 四项有限非作者 Evidence→实际 owner 核

复核人：`apr20_resume`，非本日作者。仅核 2604.18874/18901/19405/19459 四份官方 exact-v1 的决定性方法、直接反证与当前 Ch66/72 相邻命题；不审全附件、全部候选、日期/来源或日级 Gate，不写共享 Books。作者必要审阅见本日 `V3_EVIDENCE_REVIEW.md` 相应 ID 节。本核确认的是**下列窄命题的具体已有覆盖**，不是四篇完整方法、数据集或结果都已写入书稿。

## 2604.18874v1 — 攻击机会分母不能被无工具接触掩盖：PASS，窄 Existing

[官方 §3.3/§4.2](https://arxiv.org/html/2604.18874v1) 把 retrieval/reference traversal 定为 depth engagement，分别报无条件 trap-entry 与已接触条件下 entry；Llama-3 只有 8/450 runs 满足 engagement，其中 7 次入陷阱，故 5.6% 无条件数不能解释为强防御。§3.1–3.8 中 tool-output 内容/拓扑被攻击者改写，但未开放独立 verification channel；breadth 的 wrong-after-non-abstain 与 depth 的 entry/budget waste 不是同一效果分母，11K 跨 campaign 总数不能并作配对样本。跨维度 AUC 接近 chance 不证明模型内部安全模块正交或生产攻击率。

真实 [Ch66 过程探索与 first causal error](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 约 2119–2139 已规定 opportunity set、已访问证据与 verified bad transition 分账；同章约 2906–2910 更直接要求 task outcome、opportunity exposure、action trace、exploit verdict 同时保存。[Ch72 Security Agent trace](../../../../../books/part-06-ai-infrastructure/72-security.md) 约 603–610 则保 proposal/tool receipt/最终效果归属。该研究给这条现有 EvalSpec 的具体拓扑/接触率反例，但未改变责任链；只判此窄命题 `PLATFORM-EVALUATION-SYSTEM` Existing，不把 fake-citation harness、全部 attack taxonomy 或数值称现文已有。无必要 Books 新增。

## 2604.18901v1 — decodable harm、refusal 与发布授权三分：PASS，窄 Existing

[官方 §3.5–§4.1/§5.3](https://arxiv.org/html/2604.18901v1) 在同一 max-pooled prompt residual 与验证集选定 layer 上比方向；effective AUROC 对反向分数作 `max(AUC,1−AUC)`，TPR@1%FPR 是经验 ROC 插值，不是冻结阈值的生产误报承诺。fit/valid 有限且从 LDA 选层，Soft-AUC warm-start 与几何角度不识别全局唯一方向；base/instruct/abliterated 家族的受限检测稳定性支持“harm 可读出不等 refusal”，不证明因果训练来源、adaptive/多轮/跨语言防御或 effect authorization。正文自己也说明跨方向 2D 组合仍是未来工作。

真实 [Ch72 Learned Security Sensor 与 Reference Monitor](../../../../../books/part-06-ai-infrastructure/72-security.md) 约 666–680 已将 layer/校准/风险建议与外置 monitor 授权分离；约 1966–1970 明确 behavioral refusal、representation probe 和真实 effect boundary 不互授。Ch66 另负担 calibration slice。故所采三分命题已有具体 owner，论文的方向优化和受限指标只是报告证据；不把其特定 probe 算法称全文 Existing，也不据高 AUROC 放行请求。`PLATFORM-SECURITY` 窄 Existing PASS，无 Books diff。

## 2604.19405v1 — 翻译派生评测的 transformation identity：PASS，窄 Existing

[官方 §3/§4.7/Fig.4](https://arxiv.org/html/2604.19405v1) 保同一图像却翻译 query/answer；Qwen3-VL-32B 换三种译器的平均正确率 68.8→64.4→58.1，说明翻译器与接受集合影响绝对分数，即使有限排名趋势仍存在。A.6 的约 200 英语回译抽查与 Bengali 局部 native 检查并非 25 语言逐项等价证明；OpenCQA 的模型 reference、解析和语言标签都不是独立真值，跨 judge 相关不能补此缺口。

真实 [Ch66 跨语言派生 benchmark](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 约 925–933 已明确 source→target transformation lineage、label/parser identity、native review、contamination，以及派生分数不可直接互换。该论文的译器敏感度是此契约的具体受限反证，未新增另一 owner 或缺失控制边界；`PLATFORM-EVALUATION-SYSTEM` 窄 Existing PASS，保 5 分标准，不把完整 M-VL-RewardBench 宣称已在 Books。

## 2604.19459v1 — 后验 stage diff 看不见最初错误规格：PASS，窄 Existing

[官方 §3/§4.2–4.3/Table 6/Case 177](https://arxiv.org/html/2604.19459v1) 的 two-stage 在文字中称 formalization locked，但 Stage 2 仍能生成变更，再以 diff flag；这不是不可变型检查。107 个 GPT-5 fabrication 是 609+300 pooled 三轮记录，过滤后 105 个、88 unique，不可混为独立题目发生率。Case 177 的错误 stage-1 公理与目标自洽，proof 成功而 stage diff 无改变，正好说明 Lean 只证明给定规格；未见 systematic gaming 不证明其不存在。两阶段每阶段最多三次编译修订，与 unified 最多三次总修订不构成同预算性能因果；LLM judge 也有 FP/FN。

真实 [Ch66 形式化规格发布 Gate](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 约 3304–3308 已明确先验收 specification validity、再看 proof/checker result，错误规格会正确地证明错误目标，开放语义时退回 tests/人工/监控；约 1238–1246 又区分 sensor 与 semantic authority。本文正是该既有命题的具体负例，不需新增通用规则。`PLATFORM-EVALUATION-SYSTEM` 窄 Existing PASS，不称全篇 evaluation 或 stage-diff 实现已覆盖，也不采“形式验证因此无用”。

四项均为独立**单篇有限**裁决，待作者据此同步本日正式表与证据；日期归属、来源完整性、其它候选、任何 Books 实写和 04/22 整日 Gate 均未由本文件验收。
