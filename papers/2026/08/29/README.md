# Daily Research — 2026-08-29

**Research Date:** 2026-08-29

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-28 09:00:00 ～ 2026-08-29 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；四项 Source Review、Books Decision 与恢复后的来源收据均已闭合

## Executive Summary

本轮按 V2.1 合同重放周六窗口。19 个 Required Daily 组织来源完成逐 endpoint 复核，并冻结可获取页面与组织仓库清单；fresh-context audit 据此纠正了初扫的两个 false negative：Anthropic 的 TASTE，以及 Tencent Hy4 preview 的实质发布。arXiv 在该窗口没有公告批次，直接枚举端点虽发生连接重置，但官方公告时刻、北京时间换算和 8 月 28 日已闭合的 OAI watermark 能够闭合零新增判断。Hugging Face Daily Papers 仍是不可确定的 identity-only backstop，其失败不改写 first-public date。

冻结候选分母共 4 项。Anthropic 的 Automated Alignment Researcher（AAR）提供了可全文审计的自动化研究闭环；同日的 TASTE 则补上“研究目标无法由客观 benchmark 直接判断”时，如何用专家讨论、置信度和分歧过滤构造 evaluator 的证据。Tencent Hy4 preview 把 770B/49B-active MoE、Gated DSA/IndexCache、原生 MTP 与公开推理配方绑定为同一 model/runtime artifact，但训练细节与多数 benchmark 条件未披露。OpenAI–Cursor 事件只证明模型供应合同将终止及未来模型不会继续提供，属于 release/security contract 事实，不披露内部安全判定或模型机制。

四项均完成 Source Review 与 Books Decision。AAR 与 TASTE 共同强化“研究 Agent 只拥有 proposal/experiment，可写域之外的 evaluator、hidden data、stop/selection 和最终 commit 必须分离”的既有命题；Hy4 是多项已知模型与 runtime 机制的版本化组合证据；OpenAI 事件只强化通用 provider dependency / recovery contract。Ch21、Ch22、Ch48、Ch66、Ch73 与 Ch84 已承载相应长期机制，因此三项为 `No Change — Existing Coverage`，OpenAI 事件为 `Version Fact / Mechanism Not Disclosed`；不为制造 diff 重写 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-29 |
| Window End | 2026-08-29 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260829-08cfefc8876b9331713b |
| Denominator Frozen At | 2026-08-29T13:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OPENAI | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T13:05:00+08:00 | official rendered research inventory plus exact dated page; alternate query receipt | checked | 1 | SF-2026-OPENAI-CURSOR-CONTRACT | page=1; final_cursor=end; alternate receipt frozen | 2026-08-29T09:00:00+08:00 | coverage:SRC-OPENAI:20260829 | — |
| SRC-ANTHROPIC | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T12:40:00+08:00 | official research listing plus Alignment Science Blog; article, paper/report and artifact reconciliation | checked | 2 | SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS<br>SF-2026-ANTHROPIC-TASTE | pages=2; final_cursor=end; frozen snapshots | 2026-08-29T09:00:00+08:00 | coverage:SRC-ANTHROPIC:20260829 | — |
| SRC-GOOGLE-AI | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-30T12:20:00+08:00 | dated DeepMind/Research Blog plus Publications identity reconciliation | no_hit | 0 | — | Blog boundary=2026-08-27; Publications delta reconciled to arXiv:2603.10465v1@2026-03-11 | 2026-08-29T09:00:00+08:00 | coverage:SRC-GOOGLE-AI:20260829 | — |
| SRC-META-AI | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T13:05:00+08:00 | rendered official Results inventory; alternate query receipt | no_hit | 0 | — | page=1; final_cursor=end; nearest dated item=2026-08-04 | 2026-08-29T09:00:00+08:00 | coverage:SRC-META-AI:20260829 | — |
| SRC-XAI | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T13:23:00+08:00 | rendered official News inventory and bounded official-domain query; alternate query receipt | no_hit | 0 | — | page=1; final_cursor=boundary-reached; nearest dated items=2026-08-26 | 2026-08-29T09:00:00+08:00 | coverage:SRC-XAI:20260829 | — |
| SRC-MISTRAL | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T13:24:00+08:00 | rendered official News inventory and bounded official-domain query; alternate query receipt | no_hit | 0 | — | page=1; final_cursor=boundary-reached; nearest dated item=2026-08-24 | 2026-08-29T09:00:00+08:00 | coverage:SRC-MISTRAL:20260829 | — |
| SRC-QWEN | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T09:40:00+08:00 | official publications and model listing | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-QWEN:20260829 | — |
| SRC-DEEPSEEK | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T09:40:00+08:00 | official research and repository surface | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-DEEPSEEK:20260829 | — |
| SRC-MOONSHOT | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T09:45:00+08:00 | Kimi blog and MoonshotAI repositories/releases | no_hit | 0 | — | pages=2; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-MOONSHOT:20260829 | — |
| SRC-ZAI | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T09:45:00+08:00 | documentation index, release notes and repositories | no_hit | 0 | — | pages=3; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-ZAI:20260829 | — |
| SRC-MINIMAX | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T09:50:00+08:00 | official model surface and status history; transient incident pre-denominator closure | no_hit | 0 | — | pages=2; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-MINIMAX:20260829 | — |
| SRC-BYTEDANCE-SEED | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T09:55:00+08:00 | official publications | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-BYTEDANCE-SEED:20260829 | — |
| SRC-BAIDU-ERNIE | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T09:55:00+08:00 | official publication inventory | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-BAIDU-ERNIE:20260829 | — |
| SRC-TENCENT-HUNYUAN | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T12:40:00+08:00 | GitHub organization API, Hy4 repository/model-card and linked weight artifacts | checked | 1 | SF-2026-TENCENT-HY4-PREVIEW | page=1; repos=100; final_cursor=end; frozen JSON and README | 2026-08-29T09:00:00+08:00 | coverage:SRC-TENCENT-HUNYUAN:20260829 | — |
| SRC-HUAWEI-NOAH | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T10:00:00+08:00 | official research and news surface | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-HUAWEI-NOAH:20260829 | — |
| SRC-SHLAB | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T10:05:00+08:00 | official research/news surface; recruiting pages excluded | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-SHLAB:20260829 | — |
| SRC-STEPFUN | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-30T12:20:00+08:00 | live official Research page with finite server-rendered blogPosts array | no_hit | 0 | — | page=1; 14 bilingual cards / 8 unique slugs; final_cursor=end; newest=2025-08-15 | 2026-08-29T09:00:00+08:00 | coverage:SRC-STEPFUN:20260829 | — |
| SRC-XIAOMI-MIMO | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T10:10:00+08:00 | official publication listing | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-XIAOMI-MIMO:20260829 | — |
| SRC-INCLUSION-AI | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T10:10:00+08:00 | official publication and blog inventory | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-29T09:00:00+08:00 | coverage:SRC-INCLUSION-AI:20260829 | — |
| SRC-ARXIV | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T10:20:00+08:00 | official announcement cadence plus prior OAI watermark; API/OAI retry connection reset | no_hit | 0 | — | pages=0; no Friday/Saturday announcement batch by official cadence; prior closed watermark retained | 2026-08-29T09:00:00+08:00 | coverage:SRC-ARXIV:20260829 | LIM-20260829-ARXIV-ENDPOINT |
| SRC-HF-PAPERS | 2026-08-28T09:00:00+08:00 | 2026-08-29T09:00:00+08:00 | 2026-08-29T10:25:00+08:00 | dated Daily Papers route; identity-only backstop | failed | 0 | — | dated page unavailable; nondeterministic backstop failure | 2026-08-29T09:00:00+08:00 | coverage:SRC-HF-PAPERS:20260829 | LIM-20260829-HF |

<!-- coverage:SRC-OPENAI:20260829:start -->The rendered official research inventory and exact page freeze the 2026-08-28 day-precision contract event; `alternate-official-query-20260829.md` records the nearest listing boundary and direct-snapshot limitation.<!-- coverage:SRC-OPENAI:20260829:end -->
<!-- coverage:SRC-ANTHROPIC:20260829:start -->The registered research page and the linked Alignment Science Blog were both enumerated. Frozen listing `org-snapshots/anthropic-research.html` (`sha256:59615ab62f2efb006a07e9c5dd2e12878c1f8454a157cff0c6fc361c314fc0ef`) plus exact AAR and TASTE pages freeze two in-window families; the first pass's one-family result was rejected as a false negative.<!-- coverage:SRC-ANTHROPIC:20260829:end -->
<!-- coverage:SRC-GOOGLE-AI:20260829:start -->DeepMind bytes and the dated Research Blog boundary are frozen; the nearest item is 2026-08-27. The year-only Publications archive is now explicitly an identity/revision route. Its later 229→230 count delta reconciles to MoXaRt / arXiv:2603.10465v1, first public 2026-03-11, so no in-window owner was missed. Recovery receipt: `papers/2026/08/_sources/daily-20260830/README.md`.<!-- coverage:SRC-GOOGLE-AI:20260829:end -->
<!-- coverage:SRC-META-AI:20260829:start -->The rendered official Results inventory is frozen in the alternate query receipt; its nearest dated publication is 2026-08-04.<!-- coverage:SRC-META-AI:20260829:end -->
<!-- coverage:SRC-XAI:20260829:start -->The rendered official News inventory and bounded official-domain query are frozen in the alternate query receipt; the nearest dated item before the window is 2026-08-26.<!-- coverage:SRC-XAI:20260829:end -->
<!-- coverage:SRC-MISTRAL:20260829:start -->The rendered official News inventory and bounded official-domain query are frozen in the alternate query receipt; the nearest dated item before the window is 2026-08-24.<!-- coverage:SRC-MISTRAL:20260829:end -->
<!-- coverage:SRC-QWEN:20260829:start -->The registered listing was checked to the window watermark.<!-- coverage:SRC-QWEN:20260829:end -->
<!-- coverage:SRC-DEEPSEEK:20260829:start -->The registered surface was checked to the window watermark.<!-- coverage:SRC-DEEPSEEK:20260829:end -->
<!-- coverage:SRC-MOONSHOT:20260829:start -->Both registered endpoints were checked to the window watermark.<!-- coverage:SRC-MOONSHOT:20260829:end -->
<!-- coverage:SRC-ZAI:20260829:start -->All registered documentation and repository endpoints were checked.<!-- coverage:SRC-ZAI:20260829:end -->
<!-- coverage:SRC-MINIMAX:20260829:start -->The official model and status surfaces were checked; the transient incident received a family-specific pre-denominator closure.<!-- coverage:SRC-MINIMAX:20260829:end -->
<!-- coverage:SRC-BYTEDANCE-SEED:20260829:start -->The registered listing was checked to the window watermark.<!-- coverage:SRC-BYTEDANCE-SEED:20260829:end -->
<!-- coverage:SRC-BAIDU-ERNIE:20260829:start -->The registered inventory was checked to the window watermark.<!-- coverage:SRC-BAIDU-ERNIE:20260829:end -->
<!-- coverage:SRC-TENCENT-HUNYUAN:20260829:start -->The GitHub organization snapshot plus exact initial commit metadata freeze Hy4's substantive artifact at `2026-08-28T06:58:08Z` / `2026-08-28T14:58:08+08:00`, inside the strict window. Commit `72c695e1d35f031d6a1c6cc19b748b1c46222bf3` adds the model card, benchmark assets and finetuning/deployment files; later pushes do not create a second family.<!-- coverage:SRC-TENCENT-HUNYUAN:20260829:end -->
<!-- coverage:SRC-HUAWEI-NOAH:20260829:start -->The registered surface was checked to the window watermark.<!-- coverage:SRC-HUAWEI-NOAH:20260829:end -->
<!-- coverage:SRC-SHLAB:20260829:start -->The official surface was checked; recruiting pages were excluded as non-research.<!-- coverage:SRC-SHLAB:20260829:end -->
<!-- coverage:SRC-STEPFUN:20260829:start -->The live official route `https://chat.stepfun.com/research` contains a finite server-rendered `blogPosts` array with 14 bilingual cards / 8 unique slugs. The newest unique item is 2025-08-15, so the complete array crosses below this window. Raw snapshot SHA-256 `337ba7533b68d0b2d2e1ea6cd1837663e231563a0a3838f93fb7e3c244c071ea` is frozen in the 2026-08-30 recovery packet.<!-- coverage:SRC-STEPFUN:20260829:end -->
<!-- coverage:SRC-XIAOMI-MIMO:20260829:start -->The registered listing was checked to the window watermark.<!-- coverage:SRC-XIAOMI-MIMO:20260829:end -->
<!-- coverage:SRC-INCLUSION-AI:20260829:start -->The registered publication/blog inventory was checked.<!-- coverage:SRC-INCLUSION-AI:20260829:end -->
<!-- coverage:SRC-ARXIV:20260829:start -->arXiv's official five-day announcement cadence, the absence of a Friday/Saturday batch and the prior closed OAI watermark close this strict window at zero; direct enumeration endpoints reset and are recorded as a limitation rather than fabricated evidence.<!-- coverage:SRC-ARXIV:20260829:end -->
<!-- coverage:SRC-HF-PAPERS:20260829:start -->The dated route did not yield a stable snapshot; this identity-only backstop failure is non-blocking.<!-- coverage:SRC-HF-PAPERS:20260829:end -->

### Coverage Limitations

- arXiv API/OAI enumeration reset the connection. This is an endpoint-level limitation, not a claim that manuscript HTML/PDF is unavailable. The Beijing window maps to EDT 2026-08-27 21:00 ～ 2026-08-28 21:00: the Thursday 20:00 batch is one hour before the window, Friday/Saturday have no announcement, and the next batch is Sunday 20:00. The preceding report froze OAI watermark `2026-08-27T16:48:39Z`; therefore this window contains no new announcement batch.
- `SRC-HF-PAPERS` did not yield a stable dated snapshot. It cannot prove first-public time or technical claims, and its non-deterministic failure does not lower deterministic-source requirements.
- Six registered organization endpoints rejected direct byte snapshotting or exposed no machine-readable boundary. Their route-specific snapshots freeze the official endpoint, exact query/filter, retrieval time, available pagination boundary, rendered boundary rows and strict-window decision; `alternate-official-query-20260829.md` indexes them. Google Publications is bounded through dated creator routes plus primary identity reconciliation; StepFun is bounded by its finite embedded listing. Search ranking is not used as mechanism evidence.

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
None — 两项请求已由 `papers/2026/08/_sources/daily-20260830/` 的恢复收据闭合。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | official-report:anthropic-aar-2026-08-28 | official-report-v1 | 2026-W35 | 2026-08-28 | SRC-ANTHROPIC | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | yes |
| SF-2026-ANTHROPIC-TASTE | official-paper:anthropic-taste-2026-08-28 | official-paper-v1 | 2026-W35 | 2026-08-28 | SRC-ANTHROPIC | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ANTHROPIC-TASTE | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ANTHROPIC-TASTE | yes |
| SF-2026-TENCENT-HY4-PREVIEW | github:Tencent-Hunyuan/Hy4-preview@72c695e1d35f031d6a1c6cc19b748b1c46222bf3 | model-artifact-v1 | 2026-W35 | 2026-08-28 | SRC-TENCENT-HUNYUAN | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-TENCENT-HY4-PREVIEW | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-TENCENT-HY4-PREVIEW | yes |
| SF-2026-OPENAI-CURSOR-CONTRACT | official:https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/@2026-08-28 | official-contract-notice | 2026-W35 | 2026-08-28 | SRC-OPENAI | 1 | 2 | 2 | 5 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-OPENAI-CURSOR-CONTRACT | self | — | new_in_window | PLATFORM-PRODUCTION | Version Fact / Mechanism Not Disclosed | — | no |

## 3. Review Completion Receipt

`complete` 表示公开正文所允许的 route 已闭合，不表示独立复现实验或赞同来源结论。

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | RP-c1fda0fcebb28ecb | deep | https://alignment.anthropic.com/2026/automated-alignment-researchers/@2026-08-28 | SRC-ANTHROPIC@https://alignment.anthropic.com/2026/automated-alignment-researchers/@2026-08-28; SRC-ANTHROPIC@https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures@2026-08-28; SRC-ANTHROPIC@https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf#sha256-a4d6b53eb486b9335f0652a3675c1a08ccdde056df62345d3740c6c2c621fbb6; SRC-ANTHROPIC@https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures#sha256-5000504911f590e2b797e9ee67d576c4dc731e5ad942212203eac85606f8586c; SRC-ANTHROPIC@commit:1899ad64fbfbc65790d259471cc4bf4de9437aa9 | https://alignment.anthropic.com/2026/automated-alignment-researchers/ — §2 Environment; §3 Automated Alignment Researcher Harness; Appendix B | https://alignment.anthropic.com/2026/automated-alignment-researchers/ — §4 Human baselines; §5 Results; §6 Frontier-scale experiment; §7 Monitoring cheating | https://alignment.anthropic.com/2026/automated-alignment-researchers/ — §8 Limitations and future work; official article §“Are we measuring the right things?” | https://github.com/YuehHanChen/automated_alignment_researcher/commit/1899ad64fbfbc65790d259471cc4bf4de9437aa9 | claim:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | complete |
| SF-2026-ANTHROPIC-TASTE | RP-1bc14693a58c6177 | deep | https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf#sha256-7f0924379ad2d4bcaddf98843f6e0cfc9e6c79f1820c282038c19d73576a15be | SRC-ANTHROPIC@https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf#sha256-7f0924379ad2d4bcaddf98843f6e0cfc9e6c79f1820c282038c19d73576a15be; SRC-ANTHROPIC@https://alignment.anthropic.com/2026/taste/#sha256-78b5c9409a48622d7bb852190b34161fc543535c7c2c34104a52d0a1dcccfb29; SRC-ANTHROPIC@https://alignment.anthropic.com/2026/taste/@2026-08-28 | https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf — §2.1 TASTE Dataset; §2.2 Data Collection | https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf — §4 Evaluation; Tables 1–2; Appendix B | https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf — §6 Limitations; 92-pair sample, approximate agreement estimator, roughly ±10 percentage-point intervals and request-only benchmark | Not Disclosed — benchmark is available on request; frozen paper PDF/HTML are evidence, not an executable artifact | claim:SF-2026-ANTHROPIC-TASTE | complete |
| SF-2026-TENCENT-HY4-PREVIEW | RP-740526d1236129b6 | deep | https://github.com/Tencent-Hunyuan/Hy4-preview/commit/72c695e1d35f031d6a1c6cc19b748b1c46222bf3 | SRC-TENCENT-HUNYUAN@https://github.com/Tencent-Hunyuan/Hy4-preview/commit/72c695e1d35f031d6a1c6cc19b748b1c46222bf3; SRC-TENCENT-HUNYUAN@https://api.github.com/repos/Tencent-Hunyuan/Hy4-preview/commits/72c695e1d35f031d6a1c6cc19b748b1c46222bf3#sha256-5f2e71a9afd652050caae5b107eedc20cd2258f71fb780c984f11cb93ac3c557; SRC-TENCENT-HUNYUAN@https://raw.githubusercontent.com/Tencent-Hunyuan/Hy4-preview/72c695e1d35f031d6a1c6cc19b748b1c46222bf3/README.md#sha256-6bfb16c0f2b63e99db1ead36c66af5322818303712068a74d13053dff0139148; SRC-TENCENT-HUNYUAN@https://raw.githubusercontent.com/Tencent-Hunyuan/Hy4-preview/main/README.md@2026-08-29#sha256-4519446bde8bbd6489ccd954c6eda87afb94d8a8453122b3d7e69b047a1a606e; SRC-TENCENT-HUNYUAN@https://huggingface.co/tencent/Hy4-preview@2026-08-29 | https://github.com/Tencent-Hunyuan/Hy4-preview/tree/72c695e1d35f031d6a1c6cc19b748b1c46222bf3 — §Model Introduction; §Model Specifications; §Deployment; §Finetuning | https://github.com/Tencent-Hunyuan/Hy4-preview/tree/72c695e1d35f031d6a1c6cc19b748b1c46222bf3 — §Built for Productivity; §Benchmark Appendix; vendor-reported benchmark images | https://github.com/Tencent-Hunyuan/Hy4-preview/tree/72c695e1d35f031d6a1c6cc19b748b1c46222bf3 — §Known Limitations; training corpus, optimizer, training hardware, precision and most benchmark execution conditions Not Disclosed | https://github.com/Tencent-Hunyuan/Hy4-preview/commit/72c695e1d35f031d6a1c6cc19b748b1c46222bf3; https://huggingface.co/tencent/Hy4-preview; sha256:5f2e71a9afd652050caae5b107eedc20cd2258f71fb780c984f11cb93ac3c557; sha256:6bfb16c0f2b63e99db1ead36c66af5322818303712068a74d13053dff0139148; sha256:4519446bde8bbd6489ccd954c6eda87afb94d8a8453122b3d7e69b047a1a606e | claim:SF-2026-TENCENT-HY4-PREVIEW | complete |
| SF-2026-OPENAI-CURSOR-CONTRACT | RP-9f1ba581286a7986 | deep | https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/@2026-08-28 | SRC-OPENAI@https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/@2026-08-28 | https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/ — §official notice paragraphs 1–4: contract wind-down, change-of-control window and future-model availability | Not Required — official contract notice makes no benchmark or mechanism claim | https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/ — §claim boundary: private contract, technical controls, migration capacity and SLO not disclosed | Not Disclosed — no machine-readable contract or technical artifact | claim:SF-2026-OPENAI-CURSOR-CONTRACT | complete |

### Source Reviews

<!-- review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:start --><!-- claim:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:start -->The author's harness keeps hidden data, scoring, capability filtering and selected-method evaluation outside the AAR's writable domain; extending that separation to production checkpoint commit is this report's systems inference, not a result the paper itself validates.<!-- claim:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:end --> The report uses four librarian agents, five parallel researchers, fresh sessions with persistent research memory, an evaluator separate from the optimizing AAR, approximately 30-minute training iterations on one H200, up to 48 hours or plateau, and three-to-five hill-climbing benchmarks for each of ten alignment failures. A pre-run monitor reviews the exact method code and mini-paper before approval; a distinct post-hoc trajectory monitor scans 1,601 trajectories and excludes 39 suspected-cheating cases (2.4%). Winning methods were then checked on held-out benchmarks, Petri and models 1.8–4.7 times larger. These results support a controlled automated-research workflow, not autonomous alignment authority: studied failures are benchmark-measurable proxies, capability guardrails cover a limited slice, accepted gains were not tested after extensive unrelated RL, and neither monitor constitutes a complete proof against benchmark gaming.<!-- review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:end -->

<!-- review:SF-2026-ANTHROPIC-TASTE:start --><!-- claim:SF-2026-ANTHROPIC-TASTE:start -->When research quality lacks an executable oracle, evaluator construction is itself a measured pipeline: preserve expert identity, disagreement discussion, confidence and score gap instead of treating one model-judge score as ground truth.<!-- claim:SF-2026-ANTHROPIC-TASTE:end --> TASTE starts from 93 human proposals and 135 scaffold-generated proposals, asks ten researchers with six months to four years of experience to score proposals, assigns four researchers per prompt, adds paired discussion and revision, then filters for strong self-reported confidence and at least a two-point score gap while capping proposal reuse. This yields 92 preference pairs with estimated human agreement of 77%; strong-confidence post-discussion preferences rise from 53% to 68%, while a conventional same-rater comparison reaches 83% on only 50 pairs. Fable 5 reaches 60%; most per-model intervals span roughly plus/minus ten percentage points, so the experiment does not establish a reliable model ranking or a production evaluator. The durable delta is the evaluation contract and its uncertainty accounting, not the benchmark leaderboard.<!-- review:SF-2026-ANTHROPIC-TASTE:end -->

<!-- review:SF-2026-TENCENT-HY4-PREVIEW:start --><!-- claim:SF-2026-TENCENT-HY4-PREVIEW:start -->Hy4 preview packages conditional capacity, sparse long-context selection, cross-layer index reuse and model-native MTP into one versioned model/runtime artifact; those features remain separate design mechanisms with separate correctness and performance contracts.<!-- claim:SF-2026-TENCENT-HY4-PREVIEW:end --> The exact initial-commit model card reports 770B total and 49B active backbone parameters, 78 layers, 256 routed plus one shared expert with top-8 routing, a one-million-token context window, Gated DSA with IndexCache reuse, identity Hyper-Connections, and one native MTP layer. It also publishes weights and concrete source-build vLLM/SGLang launch recipes, including eight-way tensor parallelism, FP8 artifacts and MTP flags. A later `main@2026-08-29` revision replaces those commands with prebuilt images, external recipes and changed SGLang speculation parameters; it is revision evidence, not the first-public recipe. Vendor evaluation reports 163 internal experts and 203 engineering tasks, but the prompt set, evaluator protocol, hardware, precision, batch, concurrency, latency SLO and training contract are mostly undisclosed. The artifact therefore proves a public compatibility/version surface and a co-designed mechanism bundle, not that any one component causes the reported quality or that either recipe meets general production SLOs.<!-- review:SF-2026-TENCENT-HY4-PREVIEW:end -->

<!-- review:SF-2026-OPENAI-CURSOR-CONTRACT:start --><!-- claim:SF-2026-OPENAI-CURSOR-CONTRACT:start -->OpenAI's official notice says it intends to wind down model supply to Cursor, proposes a 2026-11-12 shutoff, and will not provide its future Astra model through that contract.<!-- claim:SF-2026-OPENAI-CURSOR-CONTRACT:end --> This proves a provider-availability and contract-lifecycle fact only. It does not disclose the private contract, an independently verified violation record, technical safety controls, model internals, migration capacity, fallback behavior or service SLO. A production AI system should therefore treat provider/model availability as versioned external dependency state and maintain tested fallback or exit paths, but this single vendor event cannot prescribe a universal provider policy.<!-- review:SF-2026-OPENAI-CURSOR-CONTRACT:end -->

## 4. Benchmark Contracts

Three families make experimental or vendor benchmark claims; the OpenAI notice makes none. `Not Disclosed` fields are part of the evidence boundary, not missing values silently filled by inference.

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | Ten alignment-failure suites, each with 3–5 hill-climbing benchmarks; held-out benchmark; Petri multi-turn audits; MMLU/GSM8K/IFEval capability guardrails | Researchers: Claude Opus 4.8; targets: Qwen3.5-2B (sycophancy, prompt injection, reward hacking), Phi-4-mini (jailbreaks, privacy), Llama-3.2-3B (power seeking, hallucination), Gemma-2-2B (deception), Olmo-3-7B (social bias, concealed uncertainty); frontier-scale runs: GLM-4-32B and Qwen2.5-72B-Instruct; article also reports Claude Sonnet 5 / early Claude Opus 4.8 experiment | approximately one NVIDIA H200 per training iteration; broader topology Not Disclosed | Not Disclosed | benchmark/model context lengths Not Disclosed | benchmark/task dependent; Not Disclosed | each iteration trains one proposed method; full batch/gradient accumulation Not Disclosed | four librarian agents then five parallel AARs per failure; separate frontier-scale 12+12 runs | geometric-mean safety headroom closed while preserving stated capability floors; up to 48 hours or plateau; no production SLO | rule/judge/trajectory benchmark scorers; held-out evaluator; pre-run exact-code/mini-paper approval monitor; distinct post-hoc trajectory monitor |
| SF-2026-ANTHROPIC-TASTE | 92 pairwise AI-safety research-proposal preferences built from expert scoring, paired discussion, confidence filtering, score-gap filtering and proposal-frequency cap | Human raters: ten AI-safety researchers with six months–four years of experience; model comparison includes Fable 5 and other named frontier models in the paper | Not Disclosed | Not Disclosed | two proposals in pairwise setup or one proposal in single-proposal setup; proposal token lengths Not Disclosed | probability/preference or scalar proposal score; length Not Disclosed | 92 pairs; bootstrap over prompts; inference batch Not Disclosed | four human researchers per prompt; model serving concurrency Not Disclosed | estimated human agreement 77%; best reported model 60%; per-model confidence intervals roughly ±10 percentage points; no production SLO | opposing discussion-pair human scores for estimated agreement; conventional same-rater subset on 50 pairs; bootstrap confidence intervals |
| SF-2026-TENCENT-HY4-PREVIEW | Vendor benchmark appendix plus blind side-by-side evaluation on 203 internal engineering tasks | Hy4 preview versus GLM 5.3 and Kimi K3; model-card architecture: 770B total / 49B active backbone plus native MTP | Deployment example specifies 8 GPUs through tensor parallelism; exact GPU model for benchmark Not Disclosed | FP8 weight artifact is published; precision used for reported benchmark Not Disclosed | context capacity reported as 1M; benchmark input lengths Not Disclosed | benchmark output lengths Not Disclosed | Not Disclosed | 163 internal experts rate 203 tasks; serving concurrency Not Disclosed | reported average/win/tie/loss rates; latency, throughput and production SLO Not Disclosed | Tencent internal experts; task sampling, blinding details and evaluator calibration Not Disclosed |

## 5. Deep Analysis Selection

All four families complete the eligibility decision. AAR and TASTE form one evolution chain—objective benchmark hill-climbing versus fuzzy proposal judgment—and share one analysis unit. Hy4 is a mechanism bundle/versioned artifact whose individual mechanisms already have canonical owners; OpenAI is a contract fact without a disclosed mechanism.

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | score_7_9<br>potential_books_delta | selected | DA-AUTOMATED-RESEARCH-COMMIT | — | Provides bounded evidence for externally owned evaluation/commit and exposes benchmark-hacking failure modes | analysis:DA-AUTOMATED-RESEARCH-COMMIT |
| SF-2026-ANTHROPIC-TASTE | score_7_9<br>potential_books_delta | subsumed | — | DA-AUTOMATED-RESEARCH-COMMIT | Completes the same control chain when research quality lacks an executable oracle | analysis:DA-AUTOMATED-RESEARCH-COMMIT |
| SF-2026-TENCENT-HY4-PREVIEW | score_7_9 | not_selected | — | — | Public artifact bundles already-owned MoE, sparse attention and MTP mechanisms; source does not isolate a new causal mechanism | analysis-decision:SF-2026-TENCENT-HY4-PREVIEW |
| SF-2026-OPENAI-CURSOR-CONTRACT | forced_review | not_selected | — | — | Contract notice changes external availability state but discloses no technical mechanism to analyze | analysis-decision:SF-2026-OPENAI-CURSOR-CONTRACT |

<!-- analysis:DA-AUTOMATED-RESEARCH-COMMIT:start -->
### 从自动化实验到可审计的研究控制环

旧研究流程由人类串行完成文献检索、方法设计、训练和评测，优点是责任边界直观；当实验空间和反馈速度扩大后，人工吞吐成为瓶颈。Automated Alignment Researcher 把搜索循环交给 Agent，但没有把全部控制权一起移交：librarian 负责建立共享先验，researcher 只提交方法与数据、执行固定预算训练，作者 harness 中与 AAR 隔离的 evaluator 保管 held-out data，capability filter 拒绝破坏通用能力的方法，pre-run monitor 审批 exact code，post-hoc monitor 扫描轨迹，stop/selection rule 决定继续与选择。

关键变化不是“Agent 能做研究”，而是把研究过程改写成有版本的 proposal → experiment → evidence → admission 状态机。收益是并行搜索与更快迭代；代价是 benchmark overfitting、evaluator/monitor 同源偏差、持续 memory 污染、算力成本和优化者对规则的策略性适应。39 条作弊轨迹说明 post-hoc monitor 是必要 sensor，也说明它不是完备证明；把 final commit 留给生产系统外部 controller 是由这些证据推导的设计要求，而非论文本身完成的生产验证。

TASTE 暴露了下一层压力：AAR 适合 reward 可以被 benchmark 明确计算的任务，但研究 proposal 的“taste”没有可执行 oracle。此时 evaluator 的状态不再只是一个 score，而包括 rater identity、individual judgment、discussion transcript、self-reported confidence、score gap、pair construction 和 sampling uncertainty。discussion 与 strong-confidence filtering 提高观测到的一致性，却也会筛掉真实争议、缩窄任务分布，并不能把 77% 的 estimated agreement 变成 ground truth。旧的人类直接评审仍适合高风险、低样本、目标开放或分歧本身有信息的场景；模型 judge 只能在其与专家偏好、可执行结果和长期 outcome 的关系被单独校准后，承担有界 proposal score，而不能自动取得 commit authority。
<!-- analysis:DA-AUTOMATED-RESEARCH-COMMIT:end -->

<!-- analysis-decision:SF-2026-TENCENT-HY4-PREVIEW:start -->Hy4 preview 达到长审计门槛，因为它公开了大规模 MoE、稀疏长上下文、原生 MTP、权重与 engine recipe 的统一版本面；但来源没有隔离各机制的因果收益，训练与 benchmark 运行合同也不完整。其长期认知分别由 MoE、Long Context、Speculative Decoding 与 Execution Engine 章节拥有，不另写模型发布叙事。<!-- analysis-decision:SF-2026-TENCENT-HY4-PREVIEW:end -->

<!-- analysis-decision:SF-2026-OPENAI-CURSOR-CONTRACT:start -->该事件进入强制 Source Review，因为它改变模型供应和退出时间；但正文只披露合同决定，没有可审计的技术机制、benchmark 或系统设计 delta，因而不与自动化研究控制环合并，也不占用长叙事名额。<!-- analysis-decision:SF-2026-OPENAI-CURSOR-CONTRACT:end -->

## 6. Books Comparison

三项机制/证据 family 已完成目标章与相邻章比较。OpenAI family 属于 `Version Fact / Mechanism Not Disclosed`，不伪造 Books Comparison 行。

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1506 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L48; books/part-06-ai-infrastructure/67-monitoring.md#L18; books/part-07-agent/84-agent-platform.md#L645 | existing:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | delta:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS |
| SF-2026-ANTHROPIC-TASTE | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1260 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1284; books/part-07-agent/84-agent-platform.md#L645 | existing:SF-2026-ANTHROPIC-TASTE | delta:SF-2026-ANTHROPIC-TASTE | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ANTHROPIC-TASTE |
| SF-2026-TENCENT-HY4-PREVIEW | MODEL-MOE | books/part-02-model/21-moe.md#L56 | books/part-02-model/22-long-context.md#L219; books/part-05-inference-system/48-speculative-decoding.md#L374; books/part-05-inference-system/50-vllm.md#L310; books/part-05-inference-system/51-sglang.md#L219 | existing:SF-2026-TENCENT-HY4-PREVIEW | delta:SF-2026-TENCENT-HY4-PREVIEW | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-TENCENT-HY4-PREVIEW |

<!-- books-review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:start --><!-- existing:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:start -->Ch66 already requires frozen substrate, immutable checkpoints, separate evaluation, versioned stop/checkpoint selection and open-stack revalidation; Ch84 already limits research agents to proposal and gives an external controller disaggregated audit and commit authority.<!-- existing:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:end --><!-- delta:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:start -->The new report is a strong bounded instance of that contract and adds observed cheating prevalence, but it does not change the long-term owner or design conclusion.<!-- delta:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:end -->Ch65 owns resource placement and Ch67 owns telemetry; neither owns research-evidence admission. No Books write is warranted.<!-- books-review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS:end -->

<!-- books-review:SF-2026-ANTHROPIC-TASTE:start --><!-- existing:SF-2026-ANTHROPIC-TASTE:start -->Ch66 already separates claim-level confidence, scorer identity, human/judge calibration and evidence admission, while Ch84 keeps final commit outside the optimizing research Agent.<!-- existing:SF-2026-ANTHROPIC-TASTE:end --><!-- delta:SF-2026-ANTHROPIC-TASTE:start -->TASTE adds a bounded empirical example in which discussion, confidence and score-gap filtering alter label agreement, but does not establish a new evaluation owner or a generally valid judge.<!-- delta:SF-2026-ANTHROPIC-TASTE:end -->The mechanism is already expressed more generally than this benchmark; no Books write is warranted.<!-- books-review:SF-2026-ANTHROPIC-TASTE:end -->

<!-- books-review:SF-2026-TENCENT-HY4-PREVIEW:start --><!-- existing:SF-2026-TENCENT-HY4-PREVIEW:start -->Ch21 owns total-versus-active MoE capacity and routing; Ch22 owns sparse long-context selection and index reuse; Ch48 owns model-native MTP and verification; the inference engine chapters own executable artifact and kernel compatibility.<!-- existing:SF-2026-TENCENT-HY4-PREVIEW:end --><!-- delta:SF-2026-TENCENT-HY4-PREVIEW:start -->Hy4 proves these mechanisms can coexist in one public 770B/49B-active model and exposes concrete serving flags, but it neither adds a new mechanism nor supplies enough causal or SLO evidence to change their design boundaries.<!-- delta:SF-2026-TENCENT-HY4-PREVIEW:end -->The release remains a versioned integration case; no Books write is warranted.<!-- books-review:SF-2026-TENCENT-HY4-PREVIEW:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260829-COVERAGE | fresh-context:coverage-recovery-audit | coverage | coverage:SRC-OPENAI:20260829; coverage:SRC-ANTHROPIC:20260829; coverage:SRC-GOOGLE-AI:20260829; coverage:SRC-META-AI:20260829; coverage:SRC-XAI:20260829; coverage:SRC-MISTRAL:20260829; coverage:SRC-QWEN:20260829; coverage:SRC-DEEPSEEK:20260829; coverage:SRC-MOONSHOT:20260829; coverage:SRC-ZAI:20260829; coverage:SRC-MINIMAX:20260829; coverage:SRC-BYTEDANCE-SEED:20260829; coverage:SRC-BAIDU-ERNIE:20260829; coverage:SRC-TENCENT-HUNYUAN:20260829; coverage:SRC-HUAWEI-NOAH:20260829; coverage:SRC-SHLAB:20260829; coverage:SRC-STEPFUN:20260829; coverage:SRC-XIAOMI-MIMO:20260829; coverage:SRC-INCLUSION-AI:20260829; coverage:SRC-ARXIV:20260829; coverage:SRC-HF-PAPERS:20260829 | — | Verified — dated Google routes plus primary identity reconciliation and the finite StepFun array close the two former findings; ordinary pending and unresolved findings are zero. | passed |
| SA-20260829-EVIDENCE | fresh-context:aug29-final-re-audit | evidence | review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS; review:SF-2026-ANTHROPIC-TASTE; review:SF-2026-TENCENT-HY4-PREVIEW; review:SF-2026-OPENAI-CURSOR-CONTRACT | — | Verified — exact initial Hy4 commit, later main revision and their recipes are separately frozen; review provenance recomputes and first-public claims remain bounded. | passed |
| SA-20260829-SELECTION | fresh-context:aug29-final-re-audit | deep_analysis_selection | analysis:DA-AUTOMATED-RESEARCH-COMMIT; analysis-decision:SF-2026-TENCENT-HY4-PREVIEW; analysis-decision:SF-2026-OPENAI-CURSOR-CONTRACT | — | Verified — all four eligible families have route-consistent selected, subsumed or not-selected decisions and resolvable narrative refs. | passed |
| SA-20260829-BOOKS | fresh-context:aug29-final-re-audit | books | books-review:SF-2026-ANTHROPIC-AUTOMATED-ALIGNMENT-RESEARCHERS; books-review:SF-2026-ANTHROPIC-TASTE; books-review:SF-2026-TENCENT-HY4-PREVIEW; review:SF-2026-OPENAI-CURSOR-CONTRACT | — | Verified — all mechanism families resolve to existing canonical owners; OpenAI remains a bounded Version Fact without fabricated mechanism comparison. | passed |

## 8. Ignored Noise

- OpenAI Thailand accelerator and Academy posts concern adoption/program activity without an AI-System mechanism delta.
- MiniMax's approximately three-minute LLM incident lacks a public durable mechanism, version, interface or postmortem change.
- Shanghai AI Lab recruiting pages are not research artifacts.
- Moonshot `walle` / `kimi-code` and Tencent `UniRL` later pushes modify existing repositories but do not establish new Source Family identity or a durable revision contract.
- No arXiv weekend announcement was silently converted into a paper candidate, and no Hugging Face recommendation date was used as first-public evidence.

## 9. Recommended Action

1. Preserve AAR and TASTE as complementary bounded cases: executable benchmark optimization and fuzzy expert-preference evaluation require different evidence contracts, but neither grants an optimizing Agent final commit authority.
2. Treat Hy4 as a versioned model/runtime compatibility case. Validate exact weights, engine image, TP topology, precision, workload and SLO before using its launch recipe as a deployment contract.
3. Track the OpenAI–Cursor notice only as a provider-contract lifecycle fact; any operational migration decision requires customer-specific dependency, capacity and fallback evidence.
4. Make no Books change unless later evidence reveals a mechanism not already owned by Ch21/22/48/66/84 or a provider-lifecycle gap not already covered by Part VI.

## 10. Repository Changes

- Added this V2.1 Daily and its source packet.
- Froze AAR and TASTE PDF/HTML, the Hy4 exact initial-commit and later-main model cards, organization endpoint snapshots and checksums.
- Rejected the initial two-family denominator after fresh-context audit found TASTE and Hy4; re-froze four families and completed their Source Review / Books Decision.
- Recorded exact organization endpoints, snapshot failures and pre-denominator closures.
- No Books, ROADMAP or decision-record change was made.

## 11. Open Questions

1. How should a future research harness preserve evaluator independence when the optimizing model becomes capable of inferring or influencing hidden tests?
2. How should evaluator owners preserve substantive expert disagreement rather than filtering it away while still producing a usable acceptance signal?
3. What capability slices and long-horizon post-training tests are sufficient before an automated alignment method can approach a deployment gate?
4. Which Hy4 component—capacity routing, sparse index reuse, residual streams or MTP—dominates quality and serving cost under a fully disclosed workload contract?
5. Which provider-exit evidence belongs in a production service contract when an upstream model may disappear for legal or policy reasons rather than technical failure?

## 12. Sources

- Anthropic, “Automated researchers can reliably mitigate alignment failures,” published 2026-08-28, accessed 2026-08-29: https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures
- Chen, Wen, Kirchner, “Automated Researchers Can Reliably Mitigate Alignment Failures,” full report, published 2026-08-28, accessed 2026-08-29: https://alignment.anthropic.com/2026/automated-alignment-researchers/
- Anthropic AAR artifact, commit `1899ad64fbfbc65790d259471cc4bf4de9437aa9`, accessed 2026-08-29: https://github.com/YuehHanChen/automated_alignment_researcher/commit/1899ad64fbfbc65790d259471cc4bf4de9437aa9
- Anthropic, “TASTE: Can AI Models Judge AI Safety Research Proposals?”, published 2026-08-28, accessed 2026-08-29: https://alignment.anthropic.com/2026/taste/
- Tencent Hunyuan, “Hy4 preview,” initial substantive model-card/repository commit `72c695e1d35f031d6a1c6cc19b748b1c46222bf3`, dated 2026-08-28, accessed 2026-08-29: https://github.com/Tencent-Hunyuan/Hy4-preview/commit/72c695e1d35f031d6a1c6cc19b748b1c46222bf3
- Tencent, “Hy4 preview,” weight/model-card artifact, accessed 2026-08-29: https://huggingface.co/tencent/Hy4-preview
- OpenAI, “Our decision on Cursor following its acquisition by SpaceX,” published 2026-08-28, accessed 2026-08-29: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
- arXiv, “Availability of submissions,” announcement schedule, accessed 2026-08-29: https://info.arxiv.org/help/availability.html
- MiniMax Status, incident history, accessed 2026-08-29: https://status.minimax.io/

## 13. Final Status

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；ordinary pending=0；unresolved findings=0。

Daily 的候选分母、四项 Source Review、Deep Analysis Selection、逐项 Books Decision 与 fresh-context Semantic Audit 已闭合。Google Publications 的 year-only archive 通过 dated creator route 与 primary first-public identity 约束，StepFun 通过 finite embedded array 闭合；没有把搜索排名或年级列表伪造成日级发布时间。
