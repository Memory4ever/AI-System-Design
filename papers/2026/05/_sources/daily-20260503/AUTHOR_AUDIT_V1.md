# 2026-05-03 Author-side Audit

本文件只记录 2026-05-03 author lane 的自审结果，不构成 `fresh-context` 独立 Semantic Audit，也不关闭 Daily Gate。

## Checkpoint

- 严格北京时间窗口：`[2026-05-02 09:00, 2026-05-03 09:00)`。
- 月度 raw identities：31,604；严格窗口全类别 raw identities：512。
- 注册类别：274；其中 Core Daily 180、keyword-category 94，均完成 title + abstract 语义筛选。
- Candidate Denominator：36（13.14%）；pre-denominator closures：238。
- exact-v1 Full Source Review：36/36 author-complete。
- Books Decision：22 `Integrate`、13 `No Change — Existing Coverage`、1 `Structural Candidate`。
- Access：blocked=0；ordinary pending=0。
- Gate：Coverage / Evidence / Books 均为 `Open`。

## Denominator Reopen History

初次冻结得到 20 个候选。第一轮反例检查重开 4 项，第二轮重点挑战再重开 4 项；root 的第三轮 title audit 指定 14 项 exact-v1 challenge 后，又重开 8 项，最终形成 36 个候选：

- `2605.01191`：把 VLA 的 status monitor 从一般 reasoning 方法重开为控制状态与 recovery ownership 变化。
- `2605.01201`：把 visuomotor safeset、Nagumo invariance 与 recovery QP 重开为 learned actor 和 physical commit 分权。
- `2605.01302`：把 counterfactual evidence critic 重开以核验其是否改变 RAG verify / abstain contract；exact-v1 对读后判定现有章节已覆盖。
- `2605.01386`：把 provenance-enriched graph memory 重开以核验 memory state owner；对读当前及相邻章节后判定 No Change。
- `2605.01429`：把 LoRA retrieve 后的 composition reliability 重开为 adapter lifecycle 与 promotion gate 增量。
- `2605.01567`：把带 propensity、OPE 与 shadow policy 的 developer memory 重开；对读后判定为现有 Memory promotion/rollback contract 的实现证据。
- `2605.01604`：把 production-agent evaluation failure modes 重开；因没有 production data，且当前 Evaluation 已拥有 trajectory/drift/release receipts，判定 No Change。
- `2605.08143`：把 sequential model editing 重开；它同时跨越 base weights、edit sidecar、runtime routing 和 registry lineage，保留为 Structural Candidate。
- `2605.01186`：terminal sequence 的 passive fingerprint 与 active forensics 改变 Security sensor 面，但当前 Books 已明确 fingerprint 不是身份凭证，判 No Change。
- `2605.01247`：typing/scroll/mouse 行为使 web-agent attribution 超出 browser flag；当前 MARK 路线已完整承载多层 fingerprint 与 drift fallback，判 No Change。
- `2605.01284`：pixel-level region identity 与 hop dependency 补全 multimodal RAG 的 evidence locator，进入 Ch76 writeback queue。
- `2605.01293`：trace→control-flow/variable-binding program 属于长期 Skill artifact；当前 typed Skill compilation、held-out admission 与 rollback 已完整承载，判 No Change。
- `2605.01471`：assertion weakening 与 test deletion 证明 repair agent 可窃取 oracle/scope owner，进入 Ch66 anti-gaming gate queue。
- `2605.01560`：clean top-to-bottom equivalence、read/write receipt 与 stale-cell gate 补全 notebook workflow state，进入 Ch81 queue。
- `2605.01566`：equal-budget Pareto front 使 multi-agent topology 与单 Agent baseline 可比，进入 Ch82 queue。
- `2605.01660`：testing、translation certificate、machine proof 与 audit 的分层 trust boundary 进入 Ch66 queue。

同轮其余 6 项在 exact-v1 后保持 closure：`2605.01208` 是 mobile-GUI post-training estimator 分支；`2605.01346` 是 GUV hidden-connectivity selective predictor；`2605.01415` 尚为无执行 enforcement 的概念框架；`2605.01489` 是 frontier-science data/model 方法；`2605.01502` 是 seismic segmentation 的单次 uncertainty proxy；`2605.08138` 是 synthetic-data toolkit。六项 closure 均已改写为具体机制、exclusion boundary 与重开条件。

第二轮 retained false-positive 检查没有移除已冻结候选；但它修正了两个错误 Books queue：access-aware vector indexing 与 quantization behavioral regression 均已由当前 owner 及相邻章节完整承载，降为 `No Change — Existing Coverage`。

## Closure Quality Audit

238 条 pre-denominator closure 均保留：

1. 该 family 具体解决的问题；
2. 具体机制或实验对象；
3. 为什么它只属于领域方法、局部模型改进、受限 benchmark 或已有 owner 的实现案例；
4. 什么新证据会使它重新进入 denominator。

归一化检查得到 238 个不同 closure，最大重复数为 1。closure 不以“可映射到 ROADMAP”作为 retain 理由；只有改变长期机制、state/data/control ownership、evaluation contract 或现有 Books 设计判断的 family 才进入 denominator。

## Deep Analysis Selection Audit

36 个候选均有逐 family 的选择或不选择理由。三个长叙事分别承担不同的跨层问题：

- `SF-COMPUTE-OPTIMAL-TOKENIZATION`：改变 scaling / evaluation 的基本信息计量单位，并传播到训练与推理成本。
- `SF-CONFOUNDED-LOG-EVALUATION`：改变 OBS / EXP / SIM 日志进入因果 evidence 的识别合同，并扩展到多轮 Agent mediator state。
- `SF-SEQUENTIAL-MODEL-EDIT-SIDECAR`：暴露 base weights、external edit memory、runtime override 与 registry lineage 之间缺少 canonical owner 的结构缺口。

其余 25 项没有被简化为同一条“优先级较低”模板；完整机制、证明边界和 Books delta 仍保存在 Source Review 与 Books Comparison。

## Evidence Provenance Boundary

36 项均记录 exact-v1 URL、访问时间、method / evaluation / limitations / artifact locator 和 Daily 内 review-body SHA256。`SOURCE_PROVENANCE_V1.json` 没有把 arXiv 原始 HTML/PDF 复制成本地 snapshot，因此不得宣称拥有 immutable local source copy；但公共合同要求的是 precise evidence version、Review Provenance、可定位 locator、claim boundary 与完整 bounded review，本地 source-body hash 只是可选留档，不构成 Evidence Gate 阻塞条件。

## Remaining Gate Conditions

- root 以独立上下文重审 274 条 screening 的 false positive / false negative。
- root 独立核验 36 项 claim、locator、non-proof 与 Deep Analysis 选择。
- root 对 22 个 Books queue 按日期和 owner 串行写回，并做 post-write semantic audit。
- root 裁决 1 个 `Structural Candidate`；在裁决前不得强塞到现有章节。
- 共享 Books 尚未由本 author lane 修改，因此本日不能标为 `Complete`。
