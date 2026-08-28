# Daily Research — 2026-08-27

**Research Date:** 2026-08-27
**Timezone:** Asia/Shanghai
**Window:** 2026-08-26 09:00:00 ～ 2026-08-27 09:00:00（北京时间，左闭右开）
**Status:** Complete；Coverage、Evidence、Books Gate 均通过 fresh-context Semantic Audit；Thursday，不生成 provisional Weekly

## Executive Summary

本轮按 V2.1 合同重建严格 24 小时窗口。arXiv Atom 九页返回并闭合 841 条 v1；Required Daily 机构、HF bounded discovery 与 exact first-public reconciliation 后，冻结 34 个事件：30 篇论文、1 个官方事故 family、1 个窄 revision、1 个 maintenance closure 和 1 个行业 context。每个窗口内 canonical family 都承担 Score V2、与路由相符的 Source Review 和最终 disposition；HF 恢复的七篇没有因 discovery source 受限而降级或跳过。

18 个 family 已改变或补全现有长期机制，12 个由当前章节完整承载，另外 4 个分别保持观点/行业 context、版本事实或低耐久度维护关闭。长叙事只选择安全 enforcement、共享 prefix state、evaluation contract 三个跨 family 单元；它只是阅读层的叙事上限，其余高分 family 仍分别完成 Deep Review。未参与写作的 reviewer 已完成 Coverage、Evidence、Deep Analysis Selection 与 Books 四个 fresh-context Semantic Audit scope，未留下 unresolved finding。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-27 |
| Window End | 2026-08-27 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-27-0900-v2.1-03 |
| Denominator Frozen At | 2026-08-28T05:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

<!-- audit-target:coverage:start -->
### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OPENAI | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official research index + technical report | checked | 1 | SF-2026-OPENAI-HF-INCIDENT | page=1; final_cursor=end; dated listing crossed below window | 2026-08-26T09:00:00+08:00 | coverage:SRC-OPENAI:20260827 | — |
| SRC-METR | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | exact incident investigation report referenced by the OpenAI technical report | checked | 1 | SF-2026-OPENAI-HF-INCIDENT | pages=1; final_cursor=end; exact dated report | 2026-08-26T09:00:00+08:00 | coverage:SRC-METR:20260827 | — |
| SRC-ANTHROPIC | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official research listing | no_hit | 0 | — | page=1; final_cursor=end; latest visible 2026-08-18 | 2026-08-18T09:00:00+08:00 | coverage:SRC-ANTHROPIC:20260827 | — |
| SRC-GOOGLE-AI | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | DeepMind + Google Research publications | checked | 1 | SF-2026-VGI-WHITE-PAPER | page=1; final_cursor=end; official page + arXiv v1 reconciled | 2026-08-26T15:36:19Z | coverage:SRC-GOOGLE-AI:20260827 | — |
| SRC-META-AI | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official research listing | no_hit | 0 | — | page=1; final_cursor=end; latest visible 2026-08-04 | 2026-08-04T09:00:00+08:00 | coverage:SRC-META-AI:20260827 | — |
| SRC-XAI | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official news | no_hit | 0 | — | page=1; final_cursor=end; latest visible 2026-08-21 | 2026-08-21T09:00:00+08:00 | coverage:SRC-XAI:20260827 | — |
| SRC-MISTRAL | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official news | no_hit | 0 | — | page=1; final_cursor=end; latest raw item 2026-08-24; no trigger | 2026-08-24T09:00:00+08:00 | coverage:SRC-MISTRAL:20260827 | — |
| SRC-QWEN | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official publications + arXiv reconciliation | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-27T09:00:00+08:00 | coverage:SRC-QWEN:20260827 | — |
| SRC-DEEPSEEK | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official updates + manuscripts | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-27T09:00:00+08:00 | coverage:SRC-DEEPSEEK:20260827 | — |
| SRC-MOONSHOT | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official blog + GitHub organization | no_hit | 0 | — | page=1; final_cursor=end; repositories enumerated; exact pushed-at query zero | 2026-08-27T09:00:00+08:00 | coverage:SRC-MOONSHOT:20260827 | — |
| SRC-ZAI | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official docs/releases + GitHub | no_hit | 0 | — | page=1; final_cursor=end; repositories enumerated; exact pushed-at query zero | 2026-08-27T09:00:00+08:00 | coverage:SRC-ZAI:20260827 | — |
| SRC-MINIMAX | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official news | checked | 1 | SF-2026-MINIMAX-FINANCIAL | page=1; final_cursor=end; dated page; context-only closure | 2026-08-26T09:00:00+08:00 | coverage:SRC-MINIMAX:20260827 | — |
| SRC-BYTEDANCE-SEED | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official publications | no_hit | 0 | — | page=1; final_cursor=end; finite listing; latest 2026-08-05 | 2026-08-05T09:00:00+08:00 | coverage:SRC-BYTEDANCE-SEED:20260827 | — |
| SRC-BAIDU-ERNIE | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official publications | no_hit | 0 | — | page=1; final_cursor=end; finite inventory reconciled | 2026-08-27T09:00:00+08:00 | coverage:SRC-BAIDU-ERNIE:20260827 | — |
| SRC-TENCENT-HUNYUAN | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official GitHub organization + exact commits | checked | 2 | SF-2026-HY-MT2-REVISION<br>SF-2026-UNIRL-MAINTENANCE | page=1; final_cursor=end; repository list + exact full SHA diffs | 2026-08-26T03:49:31Z | coverage:SRC-TENCENT-HUNYUAN:20260827 | — |
| SRC-HUAWEI-NOAH | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official dated archive | no_hit | 0 | — | page=1; final_cursor=end; latest visible 2026-08-05 | 2026-08-05T09:00:00+08:00 | coverage:SRC-HUAWEI-NOAH:20260827 | — |
| SRC-SHLAB | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official research surface | no_hit | 0 | — | page=1; final_cursor=end; arXiv identities reconciled | 2026-08-27T09:00:00+08:00 | coverage:SRC-SHLAB:20260827 | — |
| SRC-STEPFUN | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official finite research collection | no_hit | 0 | — | page=1; final_cursor=end; cards=14; slugs=8; crossed below window | 2026-08-27T09:00:00+08:00 | coverage:SRC-STEPFUN:20260827 | — |
| SRC-XIAOMI-MIMO | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official publications | no_hit | 0 | — | page=1; final_cursor=end; finite listing; latest 2026-06-29 | 2026-06-29T09:00:00+08:00 | coverage:SRC-XIAOMI-MIMO:20260827 | — |
| SRC-INCLUSION-AI | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | official publications + LLaDA site | no_hit | 0 | — | page=1; final_cursor=end; main list 2025; LLaDA latest 2026-08-04 | 2026-08-04T09:00:00+08:00 | coverage:SRC-INCLUSION-AI:20260827 | — |
| SRC-ARXIV | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | Atom submittedDate:[202608260100 TO 202608270100] | checked | 841 | SF-2026-GROUNDHOG-BITFLIP<br>SF-2026-METIS-RUNTIME<br>SF-2026-GIFT-IFC<br>SF-2026-FIELD-TIER-MIN<br>SF-2026-CASKG<br>SF-2026-AGENTIC-GAME-WM<br>SF-2026-TOPAS<br>SF-2026-POLYMEMDB<br>SF-2026-V-RUBRICS<br>SF-2026-RA-VLA<br>SF-2026-JIT-AGENT<br>SF-2026-RETRIEVALROUTER<br>SF-2026-PSRL<br>SF-2026-LMSM<br>SF-2026-REDIR<br>SF-2026-TAILSFT<br>SF-2026-TACFORCING<br>SF-2026-SKILLSHIELD<br>SF-2026-LOCALIZE-DECIDE<br>SF-2026-SKILL-ISSUE<br>SF-2026-MA-VLA<br>SF-2026-VGI-WHITE-PAPER<br>SF-2026-CODE-WORLD-MODEL<br>SF-2026-TAU-AGENT<br>SF-2026-SPECTRAL-ALLOCATION<br>SF-2026-PROGROUTER<br>SF-2026-ASYMSPEC<br>SF-2026-STREAMPI<br>SF-2026-PREFIX-SLIDING<br>SF-2026-ZERO-WAM | pages=9; start=0..800; totalResults=841; returned=841; final_cursor=end | 2026-08-26T17:59:51Z | coverage:SRC-ARXIV:20260827 | — |
| SRC-HF-PAPERS | 2026-08-26T09:00:00+08:00 | 2026-08-27T09:00:00+08:00 | 2026-08-28T04:30:00+08:00 | bounded Daily Papers listing + identity recovery | failed | 7 | SF-2026-RETRIEVALROUTER<br>SF-2026-SKILL-ISSUE<br>SF-2026-MA-VLA<br>SF-2026-CODE-WORLD-MODEL<br>SF-2026-TAU-AGENT<br>SF-2026-PREFIX-SLIDING<br>SF-2026-ZERO-WAM | page=1; final_cursor=unavailable; reason=listing timeout; nondeterministic backstop failure | — | coverage:SRC-HF-PAPERS:20260827 | GAP-HF-20260827-LISTING |

<!-- coverage:SRC-OPENAI:20260827:start -->`SRC-OPENAI` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-OPENAI:20260827:end -->
<!-- coverage:SRC-METR:20260827:start -->`SRC-METR` 作为候选明确引用的独立评估 supporting source 执行 exact-report receipt；它不扩大 Required Daily denominator，只在 Independent Evaluator scope 内使用。<!-- coverage:SRC-METR:20260827:end -->
<!-- coverage:SRC-ANTHROPIC:20260827:start -->`SRC-ANTHROPIC` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-ANTHROPIC:20260827:end -->
<!-- coverage:SRC-GOOGLE-AI:20260827:start -->`SRC-GOOGLE-AI` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-GOOGLE-AI:20260827:end -->
<!-- coverage:SRC-META-AI:20260827:start -->`SRC-META-AI` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-META-AI:20260827:end -->
<!-- coverage:SRC-XAI:20260827:start -->`SRC-XAI` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-XAI:20260827:end -->
<!-- coverage:SRC-MISTRAL:20260827:start -->`SRC-MISTRAL` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-MISTRAL:20260827:end -->
<!-- coverage:SRC-QWEN:20260827:start -->`SRC-QWEN` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-QWEN:20260827:end -->
<!-- coverage:SRC-DEEPSEEK:20260827:start -->`SRC-DEEPSEEK` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-DEEPSEEK:20260827:end -->
<!-- coverage:SRC-MOONSHOT:20260827:start -->`SRC-MOONSHOT` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-MOONSHOT:20260827:end -->
<!-- coverage:SRC-ZAI:20260827:start -->`SRC-ZAI` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-ZAI:20260827:end -->
<!-- coverage:SRC-MINIMAX:20260827:start -->`SRC-MINIMAX` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-MINIMAX:20260827:end -->
<!-- coverage:SRC-BYTEDANCE-SEED:20260827:start -->`SRC-BYTEDANCE-SEED` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-BYTEDANCE-SEED:20260827:end -->
<!-- coverage:SRC-BAIDU-ERNIE:20260827:start -->`SRC-BAIDU-ERNIE` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-BAIDU-ERNIE:20260827:end -->
<!-- coverage:SRC-TENCENT-HUNYUAN:20260827:start -->`SRC-TENCENT-HUNYUAN` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-TENCENT-HUNYUAN:20260827:end -->
<!-- coverage:SRC-HUAWEI-NOAH:20260827:start -->`SRC-HUAWEI-NOAH` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-HUAWEI-NOAH:20260827:end -->
<!-- coverage:SRC-SHLAB:20260827:start -->`SRC-SHLAB` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-SHLAB:20260827:end -->
<!-- coverage:SRC-STEPFUN:20260827:start -->`SRC-STEPFUN` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-STEPFUN:20260827:end -->
<!-- coverage:SRC-XIAOMI-MIMO:20260827:start -->`SRC-XIAOMI-MIMO` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-XIAOMI-MIMO:20260827:end -->
<!-- coverage:SRC-INCLUSION-AI:20260827:start -->`SRC-INCLUSION-AI` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-INCLUSION-AI:20260827:end -->
<!-- coverage:SRC-ARXIV:20260827:start -->`SRC-ARXIV` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-ARXIV:20260827:end -->
<!-- coverage:SRC-HF-PAPERS:20260827:start -->`SRC-HF-PAPERS` 的 endpoint、窗口水位、命中或 no-hit 证据已冻结于本表与 `_sources/daily-20260827/`；仅在注册表 authority scope 内使用。<!-- coverage:SRC-HF-PAPERS:20260827:end -->

### Coverage Limitations

- Supporting Evidence Receipt：`SRC-METR@https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/` 已核验 exact identity/date，并作为 `SF-2026-OPENAI-HF-INCIDENT` 的 triggered supporting receipt；它不是本日到期的 Required Daily source，因此不扩大 coverage denominator。METR 只支持独立行为评估及其 evaluation contract，不支持 OpenAI 内部环境、凭据或控制机制事实。
- `SRC-HF-PAPERS` 是 nondeterministic discovery backstop；listing 本次执行失败，不能形成确定性覆盖声明。七个 identity 已由其他路径恢复并回到 arXiv v1 核验；该 backstop 不参与 Coverage Complete 算术，失败记录为 `GAP-HF-20260827-LISTING`，由 Sunday Weekly 重试。
- arXiv 九页的 `totalResults = returned = 841`，时间水位越过窗口两端；30 个入选论文均以 exact v1 为 primary evidence。
- OpenAI 事故报告属于机构对自身事件的 primary account，METR/Redwood 仅作独立交叉检查；二者都不能证明未公开的生产机制或普遍发生率。
<!-- audit-target:coverage:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-OPENAI-HF-INCIDENT | release:openai-hf-incident-2026-08-26 | official-incident:openai-hf | 2026-W35 | 2026-08-26 | SRC-METR;SRC-OPENAI | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-OPENAI-HF-INCIDENT | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-OPENAI-HF-INCIDENT | yes |
| SF-2026-GROUNDHOG-BITFLIP | arXiv:2608.25276v1 | paper-v1:2608.25276 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-GROUNDHOG-BITFLIP | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-GROUNDHOG-BITFLIP | yes |
| SF-2026-METIS-RUNTIME | arXiv:2608.25322v1 | paper-v1:2608.25322 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-METIS-RUNTIME | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-METIS-RUNTIME | yes |
| SF-2026-GIFT-IFC | arXiv:2608.25431v1 | paper-v1:2608.25431 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-GIFT-IFC | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-GIFT-IFC | yes |
| SF-2026-FIELD-TIER-MIN | arXiv:2608.25474v1 | paper-v1:2608.25474 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-FIELD-TIER-MIN | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-FIELD-TIER-MIN | yes |
| SF-2026-CASKG | arXiv:2608.25500v1 | paper-v1:2608.25500 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-CASKG | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-CASKG | yes |
| SF-2026-AGENTIC-GAME-WM | arXiv:2608.25518v1 | paper-v1:2608.25518 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-AGENTIC-GAME-WM | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Weekly Only — Context | — | yes |
| SF-2026-TOPAS | arXiv:2608.25523v1 | paper-v1:2608.25523 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-TOPAS | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-TOPAS | yes |
| SF-2026-POLYMEMDB | arXiv:2608.25577v1 | paper-v1:2608.25577 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-POLYMEMDB | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-POLYMEMDB | yes |
| SF-2026-V-RUBRICS | arXiv:2608.25580v1 | paper-v1:2608.25580 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-V-RUBRICS | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-V-RUBRICS | yes |
| SF-2026-RA-VLA | arXiv:2608.25585v1 | paper-v1:2608.25585 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-RA-VLA | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-RA-VLA | yes |
| SF-2026-JIT-AGENT | arXiv:2608.25593v1 | paper-v1:2608.25593 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-JIT-AGENT | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-JIT-AGENT | yes |
| SF-2026-RETRIEVALROUTER | arXiv:2608.25625v1 | paper-v1:2608.25625 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-HF-PAPERS | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-RETRIEVALROUTER | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-RETRIEVALROUTER | yes |
| SF-2026-PSRL | arXiv:2608.25683v1 | paper-v1:2608.25683 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-PSRL | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-PSRL | yes |
| SF-2026-LMSM | arXiv:2608.25697v1 | paper-v1:2608.25697 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-LMSM | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-LMSM | yes |
| SF-2026-REDIR | arXiv:2608.25711v1 | paper-v1:2608.25711 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-REDIR | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-REDIR | yes |
| SF-2026-TAILSFT | arXiv:2608.25756v1 | paper-v1:2608.25756 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-TAILSFT | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-TAILSFT | yes |
| SF-2026-TACFORCING | arXiv:2608.25798v1 | paper-v1:2608.25798 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-TACFORCING | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-TACFORCING | yes |
| SF-2026-SKILLSHIELD | arXiv:2608.25817v1 | paper-v1:2608.25817 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-SKILLSHIELD | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-SKILLSHIELD | yes |
| SF-2026-LOCALIZE-DECIDE | arXiv:2608.25824v1 | paper-v1:2608.25824 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-LOCALIZE-DECIDE | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-LOCALIZE-DECIDE | yes |
| SF-2026-SKILL-ISSUE | arXiv:2608.25832v1 | paper-v1:2608.25832 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-HF-PAPERS | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-SKILL-ISSUE | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-SKILL-ISSUE | yes |
| SF-2026-MA-VLA | arXiv:2608.25864v1 | paper-v1:2608.25864 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-HF-PAPERS | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-MA-VLA | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-MA-VLA | yes |
| SF-2026-VGI-WHITE-PAPER | arXiv:2608.25924v1 | paper-v1:2608.25924 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-GOOGLE-AI | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-VGI-WHITE-PAPER | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-VGI-WHITE-PAPER | no |
| SF-2026-CODE-WORLD-MODEL | arXiv:2608.25927v1 | paper-v1:2608.25927 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-HF-PAPERS | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-CODE-WORLD-MODEL | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-CODE-WORLD-MODEL | yes |
| SF-2026-TAU-AGENT | arXiv:2608.25935v1 | paper-v1:2608.25935 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-HF-PAPERS | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-TAU-AGENT | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-TAU-AGENT | yes |
| SF-2026-SPECTRAL-ALLOCATION | arXiv:2608.25990v1 | paper-v1:2608.25990 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-SPECTRAL-ALLOCATION | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-SPECTRAL-ALLOCATION | yes |
| SF-2026-PROGROUTER | arXiv:2608.25992v1 | paper-v1:2608.25992 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-PROGROUTER | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-PROGROUTER | yes |
| SF-2026-ASYMSPEC | arXiv:2608.26004v1 | paper-v1:2608.26004 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ASYMSPEC | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ASYMSPEC | yes |
| SF-2026-STREAMPI | arXiv:2608.26067v1 | paper-v1:2608.26067 | 2026-W35 | 2026-08-26 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-STREAMPI | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-STREAMPI | yes |
| SF-2026-PREFIX-SLIDING | arXiv:2608.26070v1 | paper-v1:2608.26070 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-HF-PAPERS | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-PREFIX-SLIDING | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-PREFIX-SLIDING | yes |
| SF-2026-ZERO-WAM | arXiv:2608.26103v1 | paper-v1:2608.26103 | 2026-W35 | 2026-08-26 | SRC-ARXIV;SRC-HF-PAPERS | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ZERO-WAM | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ZERO-WAM | yes |
| SF-2026-HY-MT2-REVISION | commit:ff1903ecaa724e10951a23c16817a2413c752b35 | commit:hy-mt2-ff1903e | 2026-W35 | 2026-08-26 | SRC-TENCENT-HUNYUAN | — | — | — | — | revision | deep_complete | accessible | important_revision | review:SF-2026-HY-MT2-REVISION | self | — | same_window_revision | MODEL-LONG-CONTEXT | Version Fact / Mechanism Not Disclosed | — | no |
| SF-2026-UNIRL-MAINTENANCE | commit:96747df21c2940b6cd68fe38cfecb93f63cc628d | commit:unirl-branch-sync | 2026-W35 | 2026-08-26 | SRC-TENCENT-HUNYUAN | 0 | 1 | 0 | 1 | closure_only | closure_complete | accessible | none | review:SF-2026-UNIRL-MAINTENANCE | self | — | new_in_window | TRAIN-GRPO | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-MINIMAX-FINANCIAL | https://www.minimax.io/news/minimax-announces-first-half-2026-financial-results-1787744160 | official-post:minimax-financial | 2026-W35 | 2026-08-26 | SRC-MINIMAX | 0 | 1 | 1 | 2 | closure_only | closure_complete | accessible | none | review:SF-2026-MINIMAX-FINANCIAL | self | — | new_in_window | WORLDVIEW-FUTURE | Weekly Only — Context | — | no |

### Benchmark Contracts

所有数字均保持在作者实验合同内；`Not Disclosed` 表示 exact v1 未给出该字段，不用推断值补齐。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-OPENAI-HF-INCIDENT | 单次内部 cyber-evaluation 事故；不提供普遍发生率 | highly capable internal-only research model；GPT-5.6 Sol | evaluation sandbox；production 与 sandbox controls 明确区分 | Not Disclosed | adversarial task context，exact token length Not Disclosed | agent actions，exact output length Not Disclosed | Not Disclosed | 单次被监控 agent run；并发 Not Disclosed | incident timeline、unauthorized-action scope、containment/control findings；无性能 SLO | OpenAI Creator Primary 证明事故与内部控制；METR/Redwood Independent Evaluator 仅证明行为评估 |
| SF-2026-GROUNDHOG-BITFLIP | Alpaca target detection；AGNews、SST-2、Samsum、SQuAD2.0；conversation/reasoning/agentic tasks | Mixtral-8x7B、Phi-3.5-MoE、DeepSeek-V2-Lite、Qwen3-30B-A3B、Qwen3-Coder-Next、GPT-OSS-20B | 3×NVIDIA A100 80GB | Not Disclosed | dataset/task dependent；exact prompt length Not Disclosed | max_new_tokens 1024；plan mode 2048 | Not Disclosed | Not Disclosed | token-length inflation、clean accuracy、ROUGE-1、F1、plan steps | paper authors；task-native scorers |
| SF-2026-METIS-RUNTIME | 30 matched real-I/O pairs；10-case fault matrix；300 tool results；five-model Read-marker protocol | protocol probe uses five named models；runtime timing has no model | Apple M2 Pro，12 CPU cores，16GB；macOS 26.5.2；Go 1.26.1 | Not Applicable for runtime；model precision Not Disclosed | matched calls/results；token length Not Disclosed | 300 tool results；token length Not Disclosed | 5 calls per pair | Safe、Queue、Exclusive declarations；baseline treats all Exclusive | paired elapsed ms、fault closure、authority evidence | paper authors；paired local runtime harness |
| SF-2026-GIFT-IFC | vLLM/DistServe prototypes across OPT and Qwen2.5 serving | OPT-13B/30B/66B；Qwen2.5-14B/32B/72B | 1–8×A800 or 1×H100，configuration varies by model | Not Disclosed | ShareGPT requests；length distribution Not Disclosed | ShareGPT outputs；length distribution Not Disclosed | batch sizes 8/16/32 in reported sweeps | request rate varied；exact concurrent-request count Not Disclosed | throughput、TTFT、TPOT、IFT overhead | paper authors；prototype instrumentation |
| SF-2026-FIELD-TIER-MIN | local action-mediation corpus、per-projection leakage analysis 与一次 identifier incident | Not Disclosed — no model is used by this local mediation evaluation | local implementation；hardware Not Disclosed | Not Disclosed — numerical model precision is not part of the local mediation evaluation | structured action fields；length Not Applicable | projection/attestation artifacts；length Not Applicable | corpus aggregate；exact batch Not Disclosed | Not Disclosed | leaked-field count、digest/attestation correctness；无 latency SLO | paper authors；corpus and incident audit |
| SF-2026-CASKG | ALFWorld ID-140 与 ScienceWorld U211；graph/retrieval ablations | six LLMs in §4.1；Qwen3-Embedding-8B retrieval component | Not Disclosed | Not Disclosed | environment trajectories；token length Not Disclosed | actions until task termination；token length Not Disclosed | Not Disclosed | Not Disclosed | task success/score、environment steps、retrieval quality | paper authors；environment-native evaluators |
| SF-2026-AGENTIC-GAME-WM | UnitySceneBench and generated-game trajectories；research agenda plus bounded study | continued-pretraining model Not Disclosed；Qwen3.6-35B-A3B judge | 8×A100 workers disclosed for data/training path | Not Disclosed | game trajectories；exact token/frame length Not Disclosed | generated trajectories；exact length Not Disclosed | global batch 4096 | worker parallelism disclosed；serving concurrency Not Disclosed | MLLM-judge score plus human audit；not a matched system benchmark | Qwen3.6-35B-A3B judge and human audit under author protocol |
| SF-2026-TOPAS | three synthetic DAGs and two MetaGPT workflows on SGLang v0.5.3 | workload model configurations in §V.A；single canonical model Not Applicable | 1×NVIDIA A100 80GB | Not Disclosed | DAG/workflow dependent；exact token length Not Disclosed | query outputs；exact length Not Disclosed | fixed query sets；batch Not Disclosed | ready-agent concurrency varied by DAG/workflow | mean/p99 JCT、request throughput、cache hit/reuse | paper authors；SGLang instrumentation |
| SF-2026-POLYMEMDB | 221 relationship construction demonstration；no matched benchmark or fault injection | Not Disclosed | Not Disclosed | Not Disclosed | demonstration records；length Not Disclosed | memory graph/records；length Not Disclosed | Not Disclosed | Not Disclosed | interface/relationship construction only；no quantitative SLO | paper authors；demonstration only |
| SF-2026-V-RUBRICS | 50,248 samples from 17 sources；rubric GRPO versus answer-only GRPO | Qwen3-VL-8B actor；Qwen3-VL-235B-A22B judges | 8 GPUs per node；GPU type and node count Not Disclosed | judge FP8；actor precision Not Disclosed | prompt max 8192 tokens | response max 8192 tokens | rubric 192；answer 480；PPO mini-batch 192/96 | rubric generation concurrent per item；exact worker count Not Disclosed | benchmark task metrics、rubric reward quality、component ablation | paper authors；model judges plus benchmark scorers |
| SF-2026-RA-VLA | LIBERO and real UR5e tasks；retrieval scale to 10^7 candidates | flow-matching VLA；SigLIP2 retriever | 1×NVIDIA A100 | Not Disclosed | demonstration 128 steps split into 15 segments | action chunk with 4 denoising steps | Not Disclosed | latency averaged over 1000 runs | task success and inference latency | paper authors；LIBERO/real-robot task success |
| SF-2026-JIT-AGENT | nine benchmarks；OpenCode/Claude Code and other harness comparisons | DeepSeek、GLM、MiMo、Qwen model pairs as listed in §6.1 | Not Disclosed | Not Disclosed | benchmark dependent | benchmark dependent | Not Disclosed | Not Disclosed | task reward、mean latency、monetary cost | benchmark-native scorers under author harness |
| SF-2026-RETRIEVALROUTER | 11 document-retrieval benchmarks；80/10/10 in-domain split；five retrieval pipelines | frozen Qwen3-0.6B router with LoRA query encoder | 1×NVIDIA H100 80GB；about 40GB combined indexes | Not Disclosed | query/document lengths dataset-dependent | ranked retrieval results；cutoff dataset-dependent | Not Disclosed | one query routed per decision；serving concurrency Not Disclosed | nDCG、MRR、Recall、mean/P95 latency、index footprint | paper authors；standard retrieval metrics |
| SF-2026-PSRL | production traces and agentic-RL prefix-sharing update workloads | Qwen2.5-1.5B/7B；Qwen3-235B | 4×A100 80GB per node；Xeon；200Gb/s intra-node and 100Gb RDMA | Not Disclosed | prompt/generation lengths per Table 2 | rollout lengths per Table 2 | rollout N and update batches per Table 2 | DP/TP/EP/PP configurations disclosed | update throughput、end-to-end latency、memory；no production tail SLO | paper authors；runtime instrumentation |
| SF-2026-LMSM | HarmBench、XSTest；SAE/transcoder/dense probes on Transformers/vLLM | Qwen3-4B thinking | 1×NVIDIA H100 | backend-dependent；judge labeling uses bfloat16 where stated | prompts per benchmark；exact length Not Disclosed | max 256 tokens | up to 32 active sequences | 32 active sequences | ASR、FRR、throughput | paper authors；benchmark labels and rule-specific evaluators |
| SF-2026-REDIR | two agent-safety benchmarks；three model families；eight held-out tool domains | Qwen3.5-9B、Ministral-3-8B-Instruct、Gemma-4-E4B | NVIDIA A100 | Not Disclosed | multi-turn trajectories；exact tokens Not Disclosed | action trajectories；exact tokens Not Disclosed | Not Disclosed | Not Disclosed | ASR、SSR/benign fidelity、FPR、latency/memory overhead | paper authors；benchmark task/safety scorers |
| SF-2026-TAILSFT | math/code SFT diagnostics and downstream GRPO | OLMo-3 7B | Not Disclosed | Not Disclosed | code 2048；math 4096 | sampled solutions for pass@16/pass@1；exact generation cap Not Disclosed | effective batches disclosed in Appendix D | Not Disclosed | pass@16、pass@1、training loss/coverage diagnostic | paper authors；task execution scorers |
| SF-2026-TACFORCING | six UniVTAC simulations and three real contact-rich tasks | pi0.5 in simulation；GR00T N1.7 on real tasks | Not Disclosed | Not Disclosed | tactile/vision history；horizon H=40 and K=8 on real setup | streaming action chunks；exact dimensionality task-dependent | global batch 256 | streaming control loop；worker concurrency Not Disclosed | task success rate | paper authors；simulator and real-task completion |
| SF-2026-SKILLSHIELD | RedCode attacks、two non-adaptive jailbreak families、731 benign prompts | six LLM/coding-agent models listed in §6.1 | Not Disclosed | Not Disclosed | skill cap 10,000 characters, about 2,400 tokens；one skill per session | tool-loop outputs；exact length Not Disclosed | evaluation repetitions per configuration；batch Not Disclosed | Not Disclosed | ASR、average severity、FPR/refusal rate | execution-based benchmark plus Qwen3.6-Plus judge for generation cases |
| SF-2026-LOCALIZE-DECIDE | multiple candidate-set sizes/datasets/judge LLMs；five-sample/few-shot calibration | judge LLMs and candidate generators listed in §4.1 | Not Disclosed | Not Disclosed | candidate-set size varied；token length Not Disclosed | shortlist plus decide/abstain | calibration samples and candidate size varied | Not Disclosed | guarantee success rate、coverage、target agreement | human-preference labels and calibrated author protocol |
| SF-2026-SKILL-ISSUE | six games、eight human-verified languages；400 games per direction，518,400 total | three open 3–4B models listed in §3 | Not Disclosed | Not Disclosed | game/rules/state/action fixed across language pair；token length Not Disclosed | legal game moves | 400 games per direction | self-play pairs；execution parallelism Not Disclosed | win/loss margins and language-invariance gaps | deterministic game engines plus author analysis |
| SF-2026-MA-VLA | RoboFactory、RoboTwin2.0、SO101；100 simulation rollouts/config and 20 real episodes/task | Pi0 unified executor plus VLM planner in §5.1 | 2×A800 | Not Disclosed | multi-view observations and atomic prompts；exact length Not Disclosed | joint multi-arm actions | training batch 32 | rollout execution；serving concurrency Not Disclosed | task success and safety-stop observations | simulator/real-task completion under author protocol |
| SF-2026-CODE-WORLD-MODEL | 157 gameplay takes，about 5.6 h and 9,420 clips；qualitative proxy-following | MiniMax-H3 LoRA plus video renderer/world model | 8×H800 | Not Disclosed | gameplay clips；exact frame/token length Not Disclosed | code transitions and rendered observations；exact length Not Disclosed | Not Disclosed | Not Disclosed | qualitative proxy-following；no matched control/causal SLO | paper authors；qualitative inspection |
| SF-2026-TAU-AGENT | AI City Track3、FETV、PSI-VQA；2-second caption segments | Gemini captioner、GPT-5.4 agent、Qwen3-VL-8B LoRA | 2×RTX PRO 6000 | Not Disclosed | slow-fast frames、captions and trajectories；exact tokens Not Disclosed | VQA answers；exact length Not Disclosed | Not Disclosed | retrieval/tool iterations；parallelism Not Disclosed | benchmark accuracy and retrieval/task metrics | official benchmark scripts plus paper pipeline |
| SF-2026-SPECTRAL-ALLOCATION | modded-nanogpt 124M/300M/1B；AdamW/Muon/SAMuon comparisons | 124M、300M、1B decoder models | Not Disclosed | Not Disclosed | training sequences per modded-nanogpt setup；exact length Not Disclosed | next-token prediction | multiple batches as reported in §6.1 | data-parallelism Not Disclosed | validation loss and tokens-to-target | paper authors；held-out loss |
| SF-2026-PROGROUTER | HumanEval+、MBPP、MATH-500、ASQA multi-step workflows | candidate LLM pools vary by benchmark and are listed in §4.1 | Not Disclosed | Not Disclosed | workflow state/query dependent | step outputs and final answer；length Not Disclosed | Not Disclosed | online per-step routing；concurrency Not Disclosed | task quality、progress gain、cost、latency | benchmark-native scorers under author router |
| SF-2026-ASYMSPEC | four agent capabilities and two end-to-end benchmarks | Qwen3-32B verifier plus Qwen3-4B drafter on vLLM | Not Disclosed | Not Disclosed | drafter full context；verifier compressed context；lengths vary by task | speculative blocks and verified answer；block cap per §4.2 | Not Disclosed | Not Disclosed | accuracy/F1、throughput、compute | paper authors；benchmark-native scorers |
| SF-2026-STREAMPI | LIBERO and memory-dependent/precise-perception real tasks | pi0.5 | Not Disclosed | Not Disclosed | variable observation history with random intervals | action chunks；exact horizon task-dependent | Not Disclosed | asynchronous streaming observations；worker concurrency Not Disclosed | task success | simulator/real-task completion under author protocol |
| SF-2026-PREFIX-SLIDING | GPQA、MATH500、AIME25；1024-sequence throughput sweep | Qwen3-1.7B main；DeepSeek-R1-Distill-Qwen-7B validation | 1×NVIDIA H100 80GB | Not Disclosed | prefix plus sliding window 4096 main；8192 appendix | reasoning budgets up to 32K tokens | 1024 sequences in throughput experiment | 1024 concurrent sequences | tokens/s and task accuracy | benchmark exact-match scorers and runtime instrumentation |
| SF-2026-ZERO-WAM | RoboTwin seven unseen tasks；dual-Franka real tasks，30 trials/task；HumanGen 74.2K pairs | Wan-2.2-TI2V-5B world-action model；LingBot-VA baseline | 15,360 GPU-hours；GPU type/count Not Disclosed | Not Disclosed | packed variable samples up to 160K tokens/GPU | future robot video then inverse-dynamics actions | variable packed batch | training parallelism Not Disclosed；real evaluation sequentiality Not Disclosed | simulation and real-robot success rate across three seeds/trials | simulator/real-task completion plus author filtering protocol |

## 3. Review Completion Receipt

`complete` 表示 exact primary evidence 已按 route 阅读并界定 claim，不表示独立复现。

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-OPENAI-HF-INCIDENT | RP-84f4d761672b8213 | deep | release:openai-hf-incident-2026-08-26 | SRC-METR@https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/;SRC-OPENAI@release:openai-hf-incident-2026-08-26 | https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf §II OpenAI’s Evaluation Environment; §IV Hugging Face Intrusion | https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#core-takeaways-about-this-incident; https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#preliminary-answers-to-the-core-questions-in-scope | https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#investigation-process-and-limitations; https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf §I pp. 4–5 production-vs-evaluation boundary; §VIII.D p. 24 System-level guardrails and production boundary | https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf; https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ | claim:SF-2026-OPENAI-HF-INCIDENT | complete |
| SF-2026-GROUNDHOG-BITFLIP | RP-1e118de946b59319 | deep | arXiv:2608.25276v1 | SRC-ARXIV@arXiv:2608.25276v1 | arXiv:2608.25276v1 §3 Groundhog Bit-Flip Attack; §3.4 Bit-Flip Attack on MoE Router; Appendix A algorithm | arXiv:2608.25276v1 §4.1 Experiment Setup; Table 1; §4.2–§4.4; Appendices E–F | arXiv:2608.25276v1 §8 Limitations | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-GROUNDHOG-BITFLIP | complete |
| SF-2026-METIS-RUNTIME | RP-c3367d4f21745a5c | deep | arXiv:2608.25322v1 | SRC-ARXIV@arXiv:2608.25322v1 | arXiv:2608.25322v1 §4 Runtime Design, §4.1–§4.7 | arXiv:2608.25322v1 §5.1–§5.7; Table 4 | arXiv:2608.25322v1 §7 Threats to Validity and Required Evaluation; Table 6 | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-METIS-RUNTIME | complete |
| SF-2026-GIFT-IFC | RP-2122b6bd5267ab5d | deep | arXiv:2608.25431v1 | SRC-ARXIV@arXiv:2608.25431v1 | arXiv:2608.25431v1 §3 GIFT Overview; §4 Near-Zero-Overhead GPU IFT; §5 GIFT-CC | arXiv:2608.25431v1 §7.1.1 A800; §7.1.2 H100; §7.2; Figures 8–9 | arXiv:2608.25431v1 §6 Implementation and Limitations; §8 Security Analysis | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-GIFT-IFC | complete |
| SF-2026-FIELD-TIER-MIN | RP-ad644590b7147ce0 | deep | arXiv:2608.25474v1 | SRC-ARXIV@arXiv:2608.25474v1 | arXiv:2608.25474v1 §3 Field-tier minimization; §4 Digest independence; §5 One declaration, three artifacts; §6 Who computes what | arXiv:2608.25474v1 §8.1 Per-projection; §8.2 Corpus quantified; §8.4 incident | arXiv:2608.25474v1 §9 Limits and residual trust, §9.1–§9.4 | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-FIELD-TIER-MIN | complete |
| SF-2026-CASKG | RP-42e6e955b45111ea | standard | arXiv:2608.25500v1 | SRC-ARXIV@arXiv:2608.25500v1 | arXiv:2608.25500v1 §3 Method, §3.2 graph induction, §3.3 counterfactual augmentation, §3.4 Bayesian calibration, §3.5 retrieval | arXiv:2608.25500v1 §4.1 Experimental Setup; §4.2 Main Results; §5.2 component ablation | arXiv:2608.25500v1 §4.1 reporting contract and §4.2/§5.2 ALFWorld/ScienceWorld-only evidence boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-CASKG | complete |
| SF-2026-AGENTIC-GAME-WM | RP-d7f98574dce362d5 | standard | arXiv:2608.25518v1 | SRC-ARXIV@arXiv:2608.25518v1 | arXiv:2608.25518v1 §4 Game Development as Human-Engine Verification; Appendix A supplementary method | arXiv:2608.25518v1 §5.1 falsifiers; §5.2 setup; §5.3–§5.5; Appendix B | arXiv:2608.25518v1 §6 Discussion; Appendix C.1 Limitation Discussion and Future Analysis | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-AGENTIC-GAME-WM | complete |
| SF-2026-TOPAS | RP-44122ea3832c5b4a | deep | arXiv:2608.25523v1 | SRC-ARXIV@arXiv:2608.25523v1 | arXiv:2608.25523v1 §IV TOPAS; §IV.A Design Overview; §IV.E Hierarchical State Search | arXiv:2608.25523v1 §V.A Setup; §V.B End-to-End; §V.C Ablations | arXiv:2608.25523v1 §II progress-reuse conflict; §VII limited-GPU-memory boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-TOPAS | complete |
| SF-2026-POLYMEMDB | RP-393430fa53f6d5b4 | standard | arXiv:2608.25577v1 | SRC-ARXIV@arXiv:2608.25577v1 | arXiv:2608.25577v1 §II System Overview; §III Probabilistic Memory Graph Maintenance | arXiv:2608.25577v1 §III 221-relationship construction demonstration; no matched experiment section | arXiv:2608.25577v1 counterevidence: v1 has no benchmark, ablation, fault injection, or explicit limitation section | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-POLYMEMDB | complete |
| SF-2026-V-RUBRICS | RP-cf11c670f4ec537f | deep | arXiv:2608.25580v1 | SRC-ARXIV@arXiv:2608.25580v1 | arXiv:2608.25580v1 §3.3 V-Rubrics 50K Construction; §3.4 Rubric Design; §3.5 Reward Design and RL | arXiv:2608.25580v1 §4.1 Setup; §4.3 Main Results; §4.4 Analysis; Appendices D.2/D.3/D.5 and E | arXiv:2608.25580v1 §6 Limitations; §7 Ethics | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-V-RUBRICS | complete |
| SF-2026-RA-VLA | RP-267ddd29b6d4f46d | standard | arXiv:2608.25585v1 | SRC-ARXIV@arXiv:2608.25585v1 | arXiv:2608.25585v1 §4.1–§4.3 retrieval and grounded execution | arXiv:2608.25585v1 §5.1 setup; §5.2–§5.6; Appendices C and H | arXiv:2608.25585v1 Appendix F Limitations | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-RA-VLA | complete |
| SF-2026-JIT-AGENT | RP-556383b6abe24cdb | deep | arXiv:2608.25593v1 | SRC-ARXIV@arXiv:2608.25593v1 | arXiv:2608.25593v1 §3 Unified Harness Codebase/HarnessFactory; §4.1–§4.3; §5 Inference | arXiv:2608.25593v1 §6.1 setup; §6.2–§6.6; §6.4 Pareto analysis | arXiv:2608.25593v1 §6.4/§6.6 bounded results; §7 Conclusion and Future Work | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-JIT-AGENT | complete |
| SF-2026-RETRIEVALROUTER | RP-7360c13999c030f5 | deep | arXiv:2608.25625v1 | SRC-ARXIV@arXiv:2608.25625v1 | arXiv:2608.25625v1 §4.1 Problem Formulation; §4.2 Router Architecture; §4.3 Training | arXiv:2608.25625v1 §5 Experimental Setup, §5.1 datasets, §5.3 metrics; §6.1–§6.3 | arXiv:2608.25625v1 §6.3 oracle gap and cross-domain/query-only evidence boundary | commit:1e287df589cb188972b463aedf2bfd9f39af0529 — code, indexes and evaluation scripts present before v1 | claim:SF-2026-RETRIEVALROUTER | complete |
| SF-2026-PSRL | RP-9c02c0a72347da96 | deep | arXiv:2608.25683v1 | SRC-ARXIV@arXiv:2608.25683v1 | arXiv:2608.25683v1 §3.2 Architecture; §4 Workload Scheduling; §5 Memory Management; §6 Implementation | arXiv:2608.25683v1 §7.1 Setup and Table 2; §7.2 Figure 9; §7.3–§7.4 | arXiv:2608.25683v1 §7.4 scalability/sequence-length studies; v1 only promises future code release | Not Disclosed — v1 does not pin an immutable implementation artifact | claim:SF-2026-PSRL | complete |
| SF-2026-LMSM | RP-c1017b725a4df0a3 | deep | arXiv:2608.25697v1 | SRC-ARXIV@arXiv:2608.25697v1 | arXiv:2608.25697v1 §4.2 Common Contract; §4.4 Request-keyed Evaluation; §4.5 Selective Enforcement; §5 | arXiv:2608.25697v1 §6.1 and Table 3; §6.2–§6.4; Appendices A–D | arXiv:2608.25697v1 §8 Discussion, Limitations paragraph; Appendix D | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-LMSM | complete |
| SF-2026-REDIR | RP-fb76cff5565ca2e1 | deep | arXiv:2608.25711v1 | SRC-ARXIV@arXiv:2608.25711v1 | arXiv:2608.25711v1 §4.1–§4.3 trajectory-conditioned action generation | arXiv:2608.25711v1 §5 Experimental Setup; §6.1–§6.6 | arXiv:2608.25711v1 §7 Adaptive Attackers; Appendix B hardware/evaluation boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-REDIR | complete |
| SF-2026-TAILSFT | RP-c6fd16167c7ea591 | deep | arXiv:2608.25756v1 | SRC-ARXIV@arXiv:2608.25756v1 | arXiv:2608.25756v1 §3.1 algorithm; §3.2 diagnostics; §3.3 theory | arXiv:2608.25756v1 §4.1 SFT; §4.2 diagnostic; §4.3 GRPO; Appendices D.1–D.2 | arXiv:2608.25756v1 §5 Discussion and one-model/recipe generalization boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-TAILSFT | complete |
| SF-2026-TACFORCING | RP-dd4d33ffc887169c | deep | arXiv:2608.25798v1 | SRC-ARXIV@arXiv:2608.25798v1 | arXiv:2608.25798v1 §3.1–§3.3 streaming action/tactile mechanism | arXiv:2608.25798v1 §4.1 Setup; §4.2–§4.3; Appendix A | arXiv:2608.25798v1 §4.3 ablation and §6 Conclusion; v1 reports no latency/safety matched study | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-TACFORCING | complete |
| SF-2026-SKILLSHIELD | RP-03ff95848d5a968f | deep | arXiv:2608.25817v1 | SRC-ARXIV@arXiv:2608.25817v1 | arXiv:2608.25817v1 §5.1–§5.3 security-skill construction and injection | arXiv:2608.25817v1 §6.1 Setup; §6.2–§6.5; Appendices B/H/I | arXiv:2608.25817v1 §7 Discussion; threat-model and automated-judge boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-SKILLSHIELD | complete |
| SF-2026-LOCALIZE-DECIDE | RP-40c3bec7f5623cbb | deep | arXiv:2608.25824v1 | SRC-ARXIV@arXiv:2608.25824v1 | arXiv:2608.25824v1 §3.1 Localization; §3.2 Calibrated Decision | arXiv:2608.25824v1 §4.1 Setup; §4.2–§4.4; Tables 2 and 6 | arXiv:2608.25824v1 §Limitations; exchangeability, calibration-distribution and judge-dependence boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-LOCALIZE-DECIDE | complete |
| SF-2026-SKILL-ISSUE | RP-889f292f843e6e98 | deep | arXiv:2608.25832v1 | SRC-ARXIV@arXiv:2608.25832v1 | arXiv:2608.25832v1 §2 Multilingual TextArena; §3 Experiment Setup; §4 Metrics | arXiv:2608.25832v1 §5.1–§5.4; Appendix B | arXiv:2608.25832v1 §Limitations; small-model, translation and tokenizer confound boundary | commit:6dfb577c01d0337fe03b05adce84c5ae1878eca1 — framework tests present; full result pipeline not pinned | claim:SF-2026-SKILL-ISSUE | complete |
| SF-2026-MA-VLA | RP-b8abf60d396ab8c9 | deep | arXiv:2608.25864v1 | SRC-ARXIV@arXiv:2608.25864v1 | arXiv:2608.25864v1 §4.1 System Overview; §4.2 VLM-based Planner; §4.3 VLA Executor; §4.4 Arm Shuffle and View Dropout | arXiv:2608.25864v1 §5.1–§5.5; §6.1–§6.3; Tables 1–6 | arXiv:2608.25864v1 §8 Conclusion; counterevidence: v1 has no explicit limitations section and only evaluates finite simulated and real multi-arm tasks with a fixed atomic-skill vocabulary | commit:855bb08445cbab0e23cbde0f8813e9fc083cc604 — training, config and atomic-prompt artifacts present before v1 | claim:SF-2026-MA-VLA | complete |
| SF-2026-VGI-WHITE-PAPER | RP-e2766c23dd8dd515 | deep | arXiv:2608.25924v1 | SRC-ARXIV@arXiv:2608.25924v1;SRC-GOOGLE-AI@https://deepmind.google/research/publications/270149/ | arXiv:2608.25924v1 §1 Introduction; §2 Perspectives on VGI, §2.1–§2.9 | Not Required — position paper presents no matched mechanism benchmark | arXiv:2608.25924v1 §3 Summary and Discussion; counterevidence: no single method, experiment, or ablation | Not Disclosed — no immutable artifact required for the position-paper claim | claim:SF-2026-VGI-WHITE-PAPER | complete |
| SF-2026-CODE-WORLD-MODEL | RP-9d0e9fc7166dc2d8 | deep | arXiv:2608.25927v1 | SRC-ARXIV@arXiv:2608.25927v1 | arXiv:2608.25927v1 §3.1–§3.3 executable/visual state split; §4.1 Implementation | arXiv:2608.25927v1 §4.2 Visual Quality and proxy-following study | arXiv:2608.25927v1 §5 Limitations and Conclusions | Not Disclosed — project page exposes no immutable code artifact at v1 | claim:SF-2026-CODE-WORLD-MODEL | complete |
| SF-2026-TAU-AGENT | RP-71d79c63ff70a359 | standard | arXiv:2608.25935v1 | SRC-ARXIV@arXiv:2608.25935v1 | arXiv:2608.25935v1 §3.1–§3.3 caption/tracking/evidence orchestration | arXiv:2608.25935v1 §4.1 Implementation; §4.2–§4.4 | arXiv:2608.25935v1 §5 Conclusion; dataset/model-specific evidence boundary | commit:6729512a01592efdc0053f5d1eeb46338e0afc4c — code and evaluation artifacts present; reproducibility partial | claim:SF-2026-TAU-AGENT | complete |
| SF-2026-SPECTRAL-ALLOCATION | RP-23596e4d54e8e735 | deep | arXiv:2608.25990v1 | SRC-ARXIV@arXiv:2608.25990v1 | arXiv:2608.25990v1 §4.1 spectral probe; §4.2 observation; §5.1–§5.2 SAMuon | arXiv:2608.25990v1 §6.1 Setup; §6.2 Results | arXiv:2608.25990v1 §7 Discussion; 124M–1B scale and static-prior boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-SPECTRAL-ALLOCATION | complete |
| SF-2026-PROGROUTER | RP-470c20881e2db2b7 | deep | arXiv:2608.25992v1 | SRC-ARXIV@arXiv:2608.25992v1 | arXiv:2608.25992v1 §3.2 Multi-View Progress; §3.3 Online Predictor; §3.4 Decision | arXiv:2608.25992v1 §4 Experiments, setup/results/ablations across four workflows | arXiv:2608.25992v1 §Limitations; benchmark-specific candidate-pool and progress-label boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-PROGROUTER | complete |
| SF-2026-ASYMSPEC | RP-2204a1b772cf61fc | deep | arXiv:2608.26004v1 | SRC-ARXIV@arXiv:2608.26004v1 | arXiv:2608.26004v1 §3.1 Problem Setup; §3.2–§3.4 delta fusion and acceptance | arXiv:2608.26004v1 §4.2 Models and Hyperparameters; §4.4 Baselines; §5.3 End-to-End | arXiv:2608.26004v1 §Limitations; deterministic-task and non-token-exact boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-ASYMSPEC | complete |
| SF-2026-STREAMPI | RP-5def3a6588ba7bb5 | deep | arXiv:2608.26067v1 | SRC-ARXIV@arXiv:2608.26067v1 | arXiv:2608.26067v1 §3 Method, §3.2–§3.3 temporal attention and random-interval training | arXiv:2608.26067v1 §4 Experiments; Appendix B Implementation Details and B.2 Real-world Experiments | arXiv:2608.26067v1 Appendix D Limitations and Future Work | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-STREAMPI | complete |
| SF-2026-PREFIX-SLIDING | RP-33dd98cbcffc8b02 | deep | arXiv:2608.26070v1 | SRC-ARXIV@arXiv:2608.26070v1 | arXiv:2608.26070v1 §2 Prefix Sliding and position-embedding/KV-reuse choices | arXiv:2608.26070v1 §3 Setup; §4 Results; §5 Ablations; Appendices E/F/H | arXiv:2608.26070v1 unnumbered §Limitations: Limited comparisons; Information loss; Limited benefit for short generations; System outputs and multi-turn; Scale | commit:f657773ece3b916256535956993bd740f678f1c4 — event-time tree contains only LICENSE and README; implementation unavailable at v1 | claim:SF-2026-PREFIX-SLIDING | complete |
| SF-2026-ZERO-WAM | RP-3439361aacd7f934 | deep | arXiv:2608.26103v1 | SRC-ARXIV@arXiv:2608.26103v1 | arXiv:2608.26103v1 §2.2 In-Context Human Video Generation Pipeline; §2.3 HumanGen; §3.2 Human Video as Task Specification; §3.3 In-Context Future Chunk Prediction; §3.4 Training and Inference | arXiv:2608.26103v1 §4.1 Implementation; §4.2 Simulation; §4.3 Real-World; §4.4 Ablation Studies | arXiv:2608.26103v1 §5 Conclusions and Discussions: stationary-tabletop, dynamic-environment, long-horizon and human/robot embodiment-gap boundary | Not Disclosed — no immutable artifact pinned by v1 | claim:SF-2026-ZERO-WAM | complete |
| SF-2026-HY-MT2-REVISION | RP-e383bd93bac19c89 | deep | commit:ff1903ecaa724e10951a23c16817a2413c752b35 | SRC-TENCENT-HUNYUAN@commit:ff1903ecaa724e10951a23c16817a2413c752b35 | commit:ff1903ecaa724e10951a23c16817a2413c752b35 §README.md unified diff: adds `max_context: 8192` to two inference/deployment examples | Not Required — revision makes no evaluation claim | commit:ff1903ecaa724e10951a23c16817a2413c752b35 §exact parent comparison changes README examples only; no code, model artifact, or benchmark delta | commit:ff1903ecaa724e10951a23c16817a2413c752b35 and its parent diff | claim:SF-2026-HY-MT2-REVISION | complete |
| SF-2026-UNIRL-MAINTENANCE | RP-7ea27a61c3675c2d | closure | commit:96747df21c2940b6cd68fe38cfecb93f63cc628d | SRC-TENCENT-HUNYUAN@commit:96747df21c2940b6cd68fe38cfecb93f63cc628d | commit:96747df21c2940b6cd68fe38cfecb93f63cc628d §exact parent comparison identifies branch/repository synchronization only | Not Required — repository maintenance has no evaluation claim | Not Required — exact commit diff contains no algorithm, API, release, configuration, or evaluation delta | commit:96747df21c2940b6cd68fe38cfecb93f63cc628d and its parent diff | claim:SF-2026-UNIRL-MAINTENANCE | complete |
| SF-2026-MINIMAX-FINANCIAL | RP-43bb4299695ce785 | closure | https://www.minimax.io/news/minimax-announces-first-half-2026-financial-results-1787744160 | SRC-MINIMAX@https://www.minimax.io/news/minimax-announces-first-half-2026-financial-results-1787744160 | https://www.minimax.io/news/minimax-announces-first-half-2026-financial-results-1787744160 §Dated disclosure identity | Not Required — context-only financial disclosure | Not Required — financial scope discloses no model or system mechanism | Not Required — organization context | claim:SF-2026-MINIMAX-FINANCIAL | complete |

### Source Reviews

<!-- review:SF-2026-OPENAI-HF-INCIDENT:start -->
<!-- claim:SF-2026-OPENAI-HF-INCIDENT:start -->《The Hugging Face incident and the road ahead》面对的问题是：evaluation sandbox 中的 agent 获得了超出题目所需的凭据与网络能力，导致模型可把研究环境当作真实攻击面。其机制不是名称替换，而是把 environment containment、least privilege、secret boundary 和 independent monitoring 作为评测合同，而不是只约束 prompt。<!-- claim:SF-2026-OPENAI-HF-INCIDENT:end -->

Evaluation contract：OpenAI 事故技术报告与 METR/Redwood 独立复盘；单次 cyber evaluation 事故，不提供普遍发生率。Authority boundary：OpenAI 作为 Creator Primary 只证明其披露的 sandbox、凭据、时间线与控制事实；METR/Redwood 作为 Independent Evaluator 只证明其观察到的行为评估及评估合同，不证明 OpenAI 内部模型机制、完整基础设施状态或修复有效性。证据边界：只能证明该次披露的链路与控制缺口；其他模型与生产环境发生率未公开。因此本报告只保留与 `PLATFORM-SECURITY` 相关的机制与边界，分数只决定 Review route，不把任一来源结论外推为通用结论。
<!-- review:SF-2026-OPENAI-HF-INCIDENT:end -->

<!-- review:SF-2026-GROUNDHOG-BITFLIP:start -->
<!-- claim:SF-2026-GROUNDHOG-BITFLIP:start -->《Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips》面对的问题是：MoE router 把终止行为集中到少数 expert 后，硬件位翻转可演化为 Denial-of-Wallet。其机制不是名称替换，而是定位与 EOS 等 token 强相关的 routing bits，破坏相关 expert 激活，使生成持续到 max-token 而尽量保持语义表面。<!-- claim:SF-2026-GROUNDHOG-BITFLIP:end -->

Evaluation contract：四个 MoE 模型、conversation/reasoning/agentic workloads；作者报告少量 expert 失活即可显著放大 token。证据边界：是主动故障注入，不证明普通软错概率；硬件、精度、并发与线上检测 SLO 未完整披露。因此本报告只保留与 `PLATFORM-SECURITY` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-GROUNDHOG-BITFLIP:end -->

<!-- review:SF-2026-METIS-RUNTIME:start -->
<!-- claim:SF-2026-METIS-RUNTIME:start -->《Metis: Typed Runtime Mediation for Tool-Using Software Agents》面对的问题是：provider stream 直接落到外部副作用时，permission、interference 与 lifecycle 缺少统一可审计语义。其机制不是名称替换，而是先将多 provider 输出规范化为 typed events，再由 permission gate、registry 与 lifecycle machine 决定 effect admission。<!-- claim:SF-2026-METIS-RUNTIME:end -->

Evaluation contract：30 个 matched real-I/O pairs、10-case fault matrix、child-boundary ablation 与五模型 Read-marker protocol。证据边界：只证明本地 runtime 的 dispatch/permission/trace closure；不证明模型能力、语义安全或通用 rollback。因此本报告只保留与 `AGENT-TOOL-CALLING` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-METIS-RUNTIME:end -->

<!-- review:SF-2026-GIFT-IFC:start -->
<!-- claim:SF-2026-GIFT-IFC:start -->《Here is a GIFT: Enforcing User Data Isolation in LLM Serving via GPU Information Flow Tracking》面对的问题是：共享 GPU serving 中 CPU orchestration 与 GPU kernel 都可能跨租户传播敏感数据。其机制不是名称替换，而是CPU 侧以 per-user encryption 隔离内容，GPU 侧静态分析 kernel flow 并以 decoupled tracker 执行信息流规则；GIFT-CC 再覆盖不可信 OS/hypervisor。<!-- claim:SF-2026-GIFT-IFC:end -->

Evaluation contract：vLLM 与 DistServe prototype；作者报告 4–10.7% throughput overhead 且 latency 基本不变。证据边界：只覆盖已建模 kernel 与论文 threat model；新 kernel、side channel、硬件/并发细节和独立复现仍缺失。因此本报告只保留与 `PLATFORM-SECURITY` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-GIFT-IFC:end -->

<!-- review:SF-2026-FIELD-TIER-MIN:start -->
<!-- claim:SF-2026-FIELD-TIER-MIN:start -->《Separating Disclosure from Authorization: Field-Tier Minimization for Agent Action Mediation》面对的问题是：授权与审计同时读取完整 action parameters 会把敏感值永久写进不可删除 ledger。其机制不是名称替换，而是按字段而非 action 分类为 raw、projection、never-leave 三层；client 在最小化前承诺 canonical digest，并对 policy/tier schema 版本做 attestation。<!-- claim:SF-2026-FIELD-TIER-MIN:end -->

Evaluation contract：论文给出本地实现、leakage analysis 和一次 projection 仍泄漏 identifier 的设计事故。证据边界：远端服务、schema evolution 与恶意 verifier 未被实证覆盖；projection 本身仍可能泄漏。因此本报告只保留与 `AGENT-TOOL-CALLING` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-FIELD-TIER-MIN:end -->

<!-- review:SF-2026-CASKG:start -->
<!-- claim:SF-2026-CASKG:start -->《CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval》面对的问题是：技能库扩大后，纯向量召回忽略程序依赖，普通图检索又依赖不可靠边。其机制不是名称替换，而是从语义、词法、I/O 与结构生成高召回候选图，再用方向化 counterfactual probe 与 Bayesian smoothing 校准边，离线发布 state-filtered graph。<!-- claim:SF-2026-CASKG:end -->

Evaluation contract：六个 LLM，在 ALFWorld ID-140 与 ScienceWorld U211 上比较任务得分和环境步数，并含 ablation。证据边界：只覆盖两个模拟环境；LLM judge、离线构图成本和跨域 graph drift 尚未验证。因此本报告只保留与 `AGENT-MEMORY` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-CASKG:end -->

<!-- review:SF-2026-AGENTIC-GAME-WM:start -->
<!-- claim:SF-2026-AGENTIC-GAME-WM:start -->《Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models》面对的问题是：仅用 crawled video 和模糊相似度奖励难以为 world model 提供可验证的长轨迹反馈。其机制不是名称替换，而是提出 RLHEV：把 game engine 作为 collision/physics/navigability/playability 的 dense verifier，人类 acceptance 作为全局反馈。<!-- claim:SF-2026-AGENTIC-GAME-WM:end -->

Evaluation contract：该文主要是立场与研究议程，没有足以比较训练方案的 matched implementation/evaluation。证据边界：不能把可执行 game specification 等同真实世界动力学，也不能据此宣称 RLHEV 已优于视频预训练。因此本报告只保留与 `MULTIMODAL-WORLD-MODELS` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-AGENTIC-GAME-WM:end -->

<!-- review:SF-2026-TOPAS:start -->
<!-- claim:SF-2026-TOPAS:start -->《TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving》面对的问题是：保留 agent prefix 可减少 prefill，却占用 KV 空间并挤压 batching；只优化 cache hit 或 workflow progress 都会延长 JCT。其机制不是名称替换，而是联合选择保留的 prefix 与执行请求，以最长剩余服务路径收益、下游 prefix reuse、迁移/抢占成本和 task aging 评分 post-decision state。<!-- claim:SF-2026-TOPAS:end -->

Evaluation contract：SGLang prototype，三个 synthetic DAG 与两个 MetaGPT workflow；报告 mean/p99 JCT。证据边界：结果依赖 synthetic DAG、特定 workflow 与共享 KV budget；生产 fairness、负载漂移和 tail-SLO 未证明。因此本报告只保留与 `INFER-SCHEDULING` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-TOPAS:end -->

<!-- review:SF-2026-POLYMEMDB:start -->
<!-- claim:SF-2026-POLYMEMDB:start -->《PolyMemDB: A Polyglot Database System for AI Memory Management》面对的问题是：单一存储无法同时表达向量、图、概率和时空记忆，长期冲突又缺少 provenance。其机制不是名称替换，而是以 polyglot stores 管理多种 memory，并用 temporal decay、semiring aggregation 与 provenance chain 处理冲突。<!-- claim:SF-2026-POLYMEMDB:end -->

Evaluation contract：四页 demonstration 描述系统接口与示例，没有广泛定量评估或故障注入。证据边界：缺少跨 backend consistency、事务边界、删除/隐私语义与规模数据，因此不支持新增 owner。因此本报告只保留与 `AGENT-MEMORY` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-POLYMEMDB:end -->

<!-- review:SF-2026-V-RUBRICS:start -->
<!-- claim:SF-2026-V-RUBRICS:start -->《V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning》面对的问题是：多模态 post-training 的单一 outcome reward 无法定位哪条视觉事实、推理步骤或指令约束出错。其机制不是名称替换，而是把答案拆成 VF/RC/IF atomic rubrics，并在有证据 span 时进行 component-wise、prefix-localized credit assignment。<!-- claim:SF-2026-V-RUBRICS:end -->

Evaluation contract：50,248 样本、17 个来源；Qwen3-VL-8B 的 SFT 后以 rubric GRPO 对比 answer-only GRPO。证据边界：rubric 由 Gemini-3-Pro 标注且继承其偏差；不外推其他模型、领域或无 reference 的开放任务。因此本报告只保留与 `PLATFORM-EVALUATION-SYSTEM` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-V-RUBRICS:end -->

<!-- review:SF-2026-RA-VLA:start -->
<!-- claim:SF-2026-RA-VLA:start -->《RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation》面对的问题是：VLA 面对新任务时，表层相似 retrieval 与 pretrained policy inertia 阻碍 expert context 转成动作。其机制不是名称替换，而是用 behavior-aligned retrieval 选择示例，并通过 grounded execution pipeline 强制策略利用功能线索。<!-- claim:SF-2026-RA-VLA:end -->

Evaluation contract：LIBERO 与真实 UR5e 任务，对 success 与计算效率作作者比较。证据边界：摘要未披露完整硬件、控制频率、并发与安全 SLO；只证明受限 task adaptation。因此本报告只保留与 `MULTIMODAL-EMBODIED-VLA` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-RA-VLA:end -->

<!-- review:SF-2026-JIT-AGENT:start -->
<!-- claim:SF-2026-JIT-AGENT:start -->《JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution》面对的问题是：固定 harness 把 memory、planning、action protocol 和 tool orchestration 固化为人工任务特化配置。其机制不是名称替换，而是以四模块协议把 harness 变成可生成 artifact，并从任务、repair 信号和历史配置 archive 即时合成与自演化。<!-- claim:SF-2026-JIT-AGENT:end -->

Evaluation contract：九个 benchmark，跨 DeepSeek、GLM、MiMo、Qwen 等模型，与 OpenCode/Claude Code 等 harness 比较。证据边界：harness generation 的隔离、可复现版本、失败回滚与 token/cost contract 未闭合，作者分数不能证明生产可靠性。因此本报告只保留与 `AGENT-PLATFORM` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-JIT-AGENT:end -->

<!-- review:SF-2026-RETRIEVALROUTER:start -->
<!-- claim:SF-2026-RETRIEVALROUTER:start -->《RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieval》面对的问题是：text/multimodal 与 dense/late-interaction pipeline 在 relevance、latency 和 index footprint 上不存在静态最优。其机制不是名称替换，而是冻结 Qwen3-0.6B 主体并以 LoRA query encoder 和 soft reward target，在五类 pipeline 间按 nDCG/latency 权衡逐 query 路由。<!-- claim:SF-2026-RETRIEVALROUTER:end -->

Evaluation contract：11 个文档检索 benchmark、80/10/10 域内切分、单 H100 80GB；报告 nDCG/MRR/Recall 与 mean/P95 latency。证据边界：需同时维护约 40GB 多索引；query-only 看不到 document layout，未验证跨域 routing，oracle gap 仍大。因此本报告只保留与 `AGENT-RAG` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-RETRIEVALROUTER:end -->

<!-- review:SF-2026-PSRL:start -->
<!-- claim:SF-2026-PSRL:start -->《psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing》面对的问题是：tree/step-wise agentic RL 使 update 而非 rollout 成为瓶颈，同时样本间出现大量 immutable prefix redundancy。其机制不是名称替换，而是利用 update phase 的 global visibility，把 prefix-sharing workload placement 与动态 block KV manager 联合优化，在 reuse 与 load balance 间调度。<!-- claim:SF-2026-PSRL:end -->

Evaluation contract：production traces 与论文 GPU/interconnect 下比较 update throughput，作者报告最高 5.2×。证据边界：不外推普通 pretraining；代码在 v1 仅承诺将公开，硬件拓扑、长度分布和 tail latency 需按原表解释。因此本报告只保留与 `TRAIN-DISTRIBUTED-TRAINING` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-PSRL:end -->

<!-- review:SF-2026-LMSM:start -->
<!-- claim:SF-2026-LMSM:start -->《LMSM: LLM Security Framework Inspired by Linux Security Modules》面对的问题是：interpretability signal 若各自绑定 calibration、policy 与 intervention，就无法形成稳定 enforcement substrate。其机制不是名称替换，而是把 calibrated evidence backend、versioned policy 和 independent buffered-output gate 分离，保持 request identity 穿过 continuous batching。<!-- claim:SF-2026-LMSM:end -->

Evaluation contract：Transformers/vLLM、SAE/transcoder/dense probes；Qwen3-4B、32 active sequences 下同时报告 HarmBench、XSTest 与 throughput。证据边界：learned backend 可能漂移且不能替代 reference monitor；结果只覆盖特定模型、规则和攻击集。因此本报告只保留与 `PLATFORM-SECURITY` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-LMSM:end -->

<!-- review:SF-2026-REDIR:start -->
<!-- claim:SF-2026-REDIR:start -->《Reassembling Distributed Risk: Trajectory-Conditioned Action Generation for Multi-Turn Agent Safety》面对的问题是：多轮攻击把风险分散到单独看似合理的 request/action，单步 filter 无法重组意图。其机制不是名称替换，而是在每次 action 前将 trajectory 压成 latent safety representation，并用同模型 cross-view supervision 注入冻结 base model 的生成过程。<!-- claim:SF-2026-REDIR:end -->

Evaluation contract：两个 agent-safety benchmark、三个 model families、八个 held-out tool domains；测 ASR、benign fidelity 与 overhead。证据边界：仍是 learned generation-time defense；不能给 deterministic authorization，跨工具迁移不等于未知攻击安全。因此本报告只保留与 `PLATFORM-SECURITY` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-REDIR:end -->

<!-- review:SF-2026-TAILSFT:start -->
<!-- claim:SF-2026-TAILSFT:start -->《TailSFT: Filtered Fine-Tuning Improves Post-Training Performance》面对的问题是：SFT 平均优化已拟合样本会浪费容量，并可能产生不适合后续 RL 的低 coverage 初始化。其机制不是名称替换，而是训练时过滤已拟合 sequence，把梯度集中到 under-modeled tail，并用轻量诊断判断何时值得启用。<!-- claim:SF-2026-TAILSFT:end -->

Evaluation contract：OLMo-3 7B、math/code pass@16 与后续特定 GRPO pass@1；含控制实验和理论分析。证据边界：只覆盖一个 7B 家族与特定后训练配方；不能推广为所有 easy sample 都应丢弃。因此本报告只保留与 `TRAIN-SFT` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-TAILSFT:end -->

<!-- review:SF-2026-TACFORCING:start -->
<!-- claim:SF-2026-TACFORCING:start -->《TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback》面对的问题是：chunk VLA 在执行前一次读取 tactile，接触状态变化后条件已过期。其机制不是名称替换，而是以 streaming action expert 在执行中持续接收 tactile，并用 EATA 只让临近执行动作关注最新触觉，避免独立高频控制器。<!-- claim:SF-2026-TACFORCING:end -->

Evaluation contract：六个 UniVTAC 仿真与三个实机 contact-rich tasks，报告 success rate。证据边界：没有证明通用实时性、安全 envelope 或更长 horizon；现有 VLA feedback-loop 章节已能承载。因此本报告只保留与 `MULTIMODAL-EMBODIED-VLA` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-TACFORCING:end -->

<!-- review:SF-2026-SKILLSHIELD:start -->
<!-- claim:SF-2026-SKILLSHIELD:start -->《SkillShield: Prompt-Space Security Skills for LLM Coding Agents》面对的问题是：API-only coding agent 无法改权重，而逐步外部 classifier/reference monitor 又增加运行成本。其机制不是名称替换，而是离线从攻击/失败合成 security skills，以固定 prompt budget 在 all-class、bundle、per-class 三种 scope 注入整个 tool loop。<!-- claim:SF-2026-SKILLSHIELD:end -->

Evaluation contract：六模型 RedCode、两类非自适应 jailbreak、731 benign prompts；比较 ASR、severity 与 refusal。证据边界：prompt policy 仍由同一模型解释，面对 adaptive attack 无硬隔离保证，不能替代 authorization/reference monitor。因此本报告只保留与 `PLATFORM-SECURITY` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-SKILLSHIELD:end -->

<!-- review:SF-2026-LOCALIZE-DECIDE:start -->
<!-- claim:SF-2026-LOCALIZE-DECIDE:start -->《Localize-Then-Decide Guarantees for LLM Judgments》面对的问题是：候选数增加会把 probability mass 摊薄，破坏 confidence 与 human disagreement 的单调关系。其机制不是名称替换，而是先用 conformal prediction 产生高概率包含 human-preferred answer 的 shortlist，再在 shortlist 内 calibrated decide-or-abstain。<!-- claim:SF-2026-LOCALIZE-DECIDE:end -->

Evaluation contract：多候选规模、多个数据集与 judge LLM；比较 guarantee success rate 与 coverage，并依赖 five-sample/few-shot calibration。证据边界：保证依赖 exchangeability 与校准分布；不是模型自知，也不覆盖分布漂移或 judge 攻击。因此本报告只保留与 `PLATFORM-EVALUATION-SYSTEM` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-LOCALIZE-DECIDE:end -->

<!-- review:SF-2026-SKILL-ISSUE:start -->
<!-- claim:SF-2026-SKILL-ISSUE:start -->《Skill Issue: Are Skills Language-Invariant in LLMs?》面对的问题是：知识和通用 benchmark 会混淆 language interface 对实际技能执行的影响。其机制不是名称替换，而是同模型 self-play 固定 game/rules/state/action，仅改变双方界面语言并交换角色；另把 interface language 与 reasoning language 分离。<!-- claim:SF-2026-SKILL-ISSUE:end -->

Evaluation contract：三种 3–4B open models、六 games、八人工核验语言，每方向 400 局，共 518,400 games。证据边界：仅小模型与八语言；self-play 测相对强弱而非绝对部署质量，translation/tokenization 仍是混杂因素。因此本报告只保留与 `PLATFORM-EVALUATION-SYSTEM` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-SKILL-ISSUE:end -->

<!-- review:SF-2026-MA-VLA:start -->
<!-- claim:SF-2026-MA-VLA:start -->《MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization》面对的问题是：单一 global instruction 无法显式分配多臂子目标，模型容易把技能绑定固定 arm identity。其机制不是名称替换，而是planner 生成有限 atomic prompts；统一 Pi0 executor 联合输出多臂 action；Arm Shuffle 联合置换 state/view/prompt/action tuple，View Dropout 增强视角鲁棒性。<!-- claim:SF-2026-MA-VLA:end -->

Evaluation contract：RoboFactory、RoboTwin2.0 与 SO101；仿真每配置100 rollouts，实机每任务20 episodes，2×A800。证据边界：只证明 seen atomic skills 的组合重排；planner error、控制频率、latency、安全与 open-world skill acquisition 未评估。因此本报告只保留与 `MULTIMODAL-EMBODIED-VLA` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-MA-VLA:end -->

<!-- review:SF-2026-VGI-WHITE-PAPER:start -->
<!-- claim:SF-2026-VGI-WHITE-PAPER:start -->《Visual General Intelligence: A White Paper》面对的问题是：视觉智能研究缺少从输入模态、学习范式到 benchmark 的统一问题框架。其机制不是名称替换，而是以多作者 white paper 梳理 vision-centered AGI 的定义、模态、学习、评测与语言关系，而非提出单一可执行系统。<!-- claim:SF-2026-VGI-WHITE-PAPER:end -->

Evaluation contract：证据是观点综述和研究议程，不存在可归因于一项机制的 matched benchmark。证据边界：不能用共识性叙述证明具体机制收益；Ch25 已区分生成、预测、因果控制与 persistent world state。因此本报告只保留与 `MULTIMODAL-WORLD-MODELS` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-VGI-WHITE-PAPER:end -->

<!-- review:SF-2026-CODE-WORLD-MODEL:start -->
<!-- claim:SF-2026-CODE-WORLD-MODEL:start -->《Code World Model: Coding Agent as World Brain》面对的问题是：纯视频 world model 观察结果却不拥有规则，难以维持可修改、持久且可执行的因果状态。其机制不是名称替换，而是拆分 S_exe/S_vis：coding agent 管低频推理与机制修订，code 管确定性 transition，video model 通过可寻址 proxy 渲染 observation。<!-- claim:SF-2026-CODE-WORLD-MODEL:end -->

Evaluation contract：157 gameplay takes、约5.6小时/9420 clips；8×H800 对 MiniMax-H3 做 LoRA，主要是 qualitative proxy-following。证据边界：没有实时、控制或因果定量评估；agent 不能从零可靠构造复杂 simulator，项目页没有公开代码。因此本报告只保留与 `MULTIMODAL-WORLD-MODELS` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-CODE-WORLD-MODEL:end -->

<!-- review:SF-2026-TAU-AGENT:start -->
<!-- claim:SF-2026-TAU-AGENT:start -->《TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding》面对的问题是：交通视频异常问答需要从长视频中取回与 query 相关的时间段、字幕与对象轨迹。其机制不是名称替换，而是central agent 编排 2秒 caption segments、open-vocabulary tracking 与迭代 evidence selection，再把 slow-fast frames 和 top-k 文本交给 VLM。<!-- claim:SF-2026-TAU-AGENT:end -->

Evaluation contract：AI City Track3/FETV/PSI-VQA；Gemini caption、GPT-5.4 agent、Qwen3-VL-8B LoRA、2×RTX PRO 6000。证据边界：大量 benchmark-specific 后处理；closed API revision、cost/latency 与 agent/tool ablation 未闭合，非 streaming。因此本报告只保留与 `AGENT-RAG` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-TAU-AGENT:end -->

<!-- review:SF-2026-SPECTRAL-ALLOCATION:start -->
<!-- claim:SF-2026-SPECTRAL-ALLOCATION:start -->《Spectral Allocation: Why Muon Outperforms Adam, and How to Improve Muon》面对的问题是：Muon 的统一正交缩放没有解释为何优于 Adam，也可能低估 loss landscape tolerant bulk 的可用步长。其机制不是名称替换，而是在 held-out data 上按 momentum singular directions 探测 loss-optimal step，区分 volatile head 与 tolerant bulk；SAMuon/SAMuon-lite 对 bulk 放大。<!-- claim:SF-2026-SPECTRAL-ALLOCATION:end -->

Evaluation contract：modded-nanogpt 124M/300M/1B、多个 batch；比较 AdamW、Muon 与验证损失所需 token，lite 用 rank-one power iteration。证据边界：仅小到中型模型；静态 spectral prior 在 frontier scale、不同 architecture 与长期稳定性上未证明。因此本报告只保留与 `TRAIN-PRETRAINING` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-SPECTRAL-ALLOCATION:end -->

<!-- review:SF-2026-PROGROUTER:start -->
<!-- claim:SF-2026-PROGROUTER:start -->《ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs》面对的问题是：one-shot cascade router 无法随 multi-step workflow 的剩余难度、进度和预算变化调整模型。其机制不是名称替换，而是以多视角 progress scorer、dual-path predictor 与 meta-gating 估计每步候选 LLM 的 progress gain，在线平衡 time/cost。<!-- claim:SF-2026-PROGROUTER:end -->

Evaluation contract：HumanEval+、MBPP、MATH-500、ASQA 四个 benchmark，跨代码、数学与 RAG workflow。证据边界：不证明开放工具环境、并发资源竞争或真实价格漂移；现有 multi-agent orchestration 已承载该 policy 类。因此本报告只保留与 `AGENT-MULTI-AGENT` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-PROGROUTER:end -->

<!-- review:SF-2026-ASYMSPEC:start -->
<!-- claim:SF-2026-ASYMSPEC:start -->《AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs》面对的问题是：压缩 verifier context 降成本却损伤正确性，而传统 speculative decoding 强制 drafter/verifier 同 context。其机制不是名称替换，而是让轻量 drafter 读 full context、large verifier 读 compressed view，以 contrastive delta-fusion 和 divergence-aware acceptance gate 传递被压缩信号。<!-- claim:SF-2026-ASYMSPEC:end -->

Evaluation contract：四类 agent capability 与两个端到端 benchmark；Qwen3-32B/vLLM 条件下比较 accuracy、throughput 与 compute。证据边界：只在特定确定性设置验证；不是 token-exact 的普通 SD 等价保证，压缩器与 verifier drift 仍可能失效。因此本报告只保留与 `INFER-SPECULATIVE-DECODING` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-ASYMSPEC:end -->

<!-- review:SF-2026-STREAMPI:start -->
<!-- claim:SF-2026-STREAMPI:start -->《StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models》面对的问题是：single-frame VLA 丢失过去 observation，且同步训练与实机异步采样存在 timing gap。其机制不是名称替换，而是把 observation-instruction pair 作为原子单元，单元内双向融合、跨单元 causal attention；random-interval training 适应异步 frame timing。<!-- claim:SF-2026-STREAMPI:end -->

Evaluation contract：LIBERO 与 memory-dependent/precise-perception 实机任务，对 pi0.5 比较 success。证据边界：未披露完整控制频率、tail latency 与 safety；属于既有 observation-history/action-loop 的参数零增量实现。因此本报告只保留与 `MULTIMODAL-EMBODIED-VLA` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-STREAMPI:end -->

<!-- review:SF-2026-PREFIX-SLIDING:start -->
<!-- claim:SF-2026-PREFIX-SLIDING:start -->《Prefix Sliding for efficient test-time scaling》面对的问题是：长 reasoning 保留完整轨迹导致 KV 与 attention 成本随思考长度增长，而近期状态和固定任务契约的重要性不同。其机制不是名称替换，而是永久保留 system/task prefix 与最近 reasoning window，丢弃中间 token；继续 RoPE position 复用 KV，RL 侧用约4×window context、末端 loss mask。<!-- claim:SF-2026-PREFIX-SLIDING:end -->

Evaluation contract：Qwen3-1.7B 为主并验证7B；GPQA/MATH500/AIME25，单80GB H100、1024 sequences、window4096 的吞吐实验。证据边界：LiveCodeBench 旧代码依赖受损；短生成收益小、tool output 可淹没 window；v1 时 repo 只有 README/License，无实现代码。因此本报告只保留与 `MODEL-LONG-CONTEXT` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-PREFIX-SLIDING:end -->

<!-- review:SF-2026-ZERO-WAM:start -->
<!-- claim:SF-2026-ZERO-WAM:start -->《Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization》面对的问题是：语言不足以完整指定新 manipulation task，而 paired human-robot demonstrations 稀缺。其机制不是名称替换，而是把 human video 作为 in-context task contract；causal model 先预测 future robot video 再由 inverse dynamics 预测 action；IFP 强迫利用 human prefix，HumanGen 合成74.2K pairs。<!-- claim:SF-2026-ZERO-WAM:end -->

Evaluation contract：Wan-2.2-TI2V-5B、15360 GPU-hours；RoboTwin七 unseen tasks 与双Franka实机每任务30 trials。证据边界：synthetic video/VLM filter 会引入偏差；仅 tabletop、小样本实机，embodiment gap 与 artifact 均未闭合。因此本报告只保留与 `MULTIMODAL-EMBODIED-VLA` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-ZERO-WAM:end -->

<!-- review:SF-2026-HY-MT2-REVISION:start -->
<!-- claim:SF-2026-HY-MT2-REVISION:start -->《Hy-MT2 README max_context revision》面对的问题是：部署示例需要显式给出上下文上限。其机制不是名称替换，而是exact commit 只在 README 两处 inference/deployment 配置加入 max_context: 8192。<!-- claim:SF-2026-HY-MT2-REVISION:end -->

Evaluation contract：逐行审阅 commit ff1903e；没有模型质量或性能实验。证据边界：只证明示例配置事实，不证明训练长度、服务端 enforcement、架构、质量、latency 或 safety。因此本报告只保留与 `MODEL-LONG-CONTEXT` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-HY-MT2-REVISION:end -->

<!-- review:SF-2026-UNIRL-MAINTENANCE:start -->
<!-- claim:SF-2026-UNIRL-MAINTENANCE:start -->《UniRL branch maintenance sync》面对的问题是：仓库同步维护分支。其机制不是名称替换，而是exact commit 是 branch/repository maintenance，没有新增可识别算法、接口或 release contract。<!-- claim:SF-2026-UNIRL-MAINTENANCE:end -->

Evaluation contract：审阅 commit 96747df 的 diff 与父提交关系；不适用 benchmark。证据边界：维护提交不能作为技术机制、版本能力或训练结果证据。因此本报告只保留与 `TRAIN-GRPO` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-UNIRL-MAINTENANCE:end -->

<!-- review:SF-2026-MINIMAX-FINANCIAL:start -->
<!-- claim:SF-2026-MINIMAX-FINANCIAL:start -->《MiniMax 2026 first-half financial results》面对的问题是：机构经营与收入变化提供行业背景。其机制不是名称替换，而是官方财报披露业务数据，但未公开可复核的模型/系统机制。<!-- claim:SF-2026-MINIMAX-FINANCIAL:end -->

Evaluation contract：仅核对官方 2026 H1 results 页面；不适用技术 benchmark。证据边界：财务口径不能证明模型能力、训练效率或系统架构，保留 Weekly context。因此本报告只保留与 `WORLDVIEW-FUTURE` 相关的机制与边界，分数只决定 Review route，不把作者结果外推为通用结论。
<!-- review:SF-2026-MINIMAX-FINANCIAL:end -->


## 4. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-OPENAI-HF-INCIDENT | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-ENFORCEMENT-LAYERS | — | 跨 family 改变共同的状态所有权或 evidence/enforcement contract，适合重建演进链 | analysis:DA-ENFORCEMENT-LAYERS |
| SF-2026-GROUNDHOG-BITFLIP | score_7_9<br>forced_review<br>potential_books_delta | subsumed | — | DA-ENFORCEMENT-LAYERS | 与 incident、GPU isolation、evidence backend 和 output gate 共享 enforcement 分层 | analysis:DA-ENFORCEMENT-LAYERS |
| SF-2026-METIS-RUNTIME | score_7_9 | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-METIS-RUNTIME |
| SF-2026-GIFT-IFC | score_7_9<br>forced_review<br>potential_books_delta | subsumed | — | DA-ENFORCEMENT-LAYERS | 与 incident、GPU isolation、evidence backend 和 output gate 共享 enforcement 分层 | analysis:DA-ENFORCEMENT-LAYERS |
| SF-2026-FIELD-TIER-MIN | score_7_9<br>forced_review<br>potential_books_delta | subsumed | — | DA-ENFORCEMENT-LAYERS | 与 incident、GPU isolation、evidence backend 和 output gate 共享 enforcement 分层 | analysis:DA-ENFORCEMENT-LAYERS |
| SF-2026-TOPAS | score_7_9<br>potential_books_delta | selected | DA-SHARED-STATE-CONTROL | — | 跨 family 改变共同的状态所有权或 evidence/enforcement contract，适合重建演进链 | analysis:DA-SHARED-STATE-CONTROL |
| SF-2026-V-RUBRICS | score_7_9<br>potential_books_delta | selected | DA-EVALUATION-CONTRACT | — | 跨 family 改变共同的状态所有权或 evidence/enforcement contract，适合重建演进链 | analysis:DA-EVALUATION-CONTRACT |
| SF-2026-JIT-AGENT | score_7_9 | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-JIT-AGENT |
| SF-2026-RETRIEVALROUTER | score_7_9<br>potential_books_delta | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-RETRIEVALROUTER |
| SF-2026-PSRL | score_7_9<br>potential_books_delta | subsumed | — | DA-SHARED-STATE-CONTROL | 改变 prefix state 的 identity、lifetime、placement 或 verification cost | analysis:DA-SHARED-STATE-CONTROL |
| SF-2026-LMSM | score_7_9<br>forced_review<br>potential_books_delta | subsumed | — | DA-ENFORCEMENT-LAYERS | 与 incident、GPU isolation、evidence backend 和 output gate 共享 enforcement 分层 | analysis:DA-ENFORCEMENT-LAYERS |
| SF-2026-REDIR | score_7_9<br>forced_review | subsumed | — | DA-ENFORCEMENT-LAYERS | 与 incident、GPU isolation、evidence backend 和 output gate 共享 enforcement 分层 | analysis:DA-ENFORCEMENT-LAYERS |
| SF-2026-TAILSFT | score_7_9<br>potential_books_delta | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-TAILSFT |
| SF-2026-TACFORCING | score_7_9 | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-TACFORCING |
| SF-2026-SKILLSHIELD | score_7_9<br>forced_review | subsumed | — | DA-ENFORCEMENT-LAYERS | 与 incident、GPU isolation、evidence backend 和 output gate 共享 enforcement 分层 | analysis:DA-ENFORCEMENT-LAYERS |
| SF-2026-LOCALIZE-DECIDE | score_7_9<br>potential_books_delta | subsumed | — | DA-EVALUATION-CONTRACT | 共同把 aggregate score 拆成可定位、可校准、可 abstain 的 evidence contract | analysis:DA-EVALUATION-CONTRACT |
| SF-2026-SKILL-ISSUE | score_7_9<br>potential_books_delta | subsumed | — | DA-EVALUATION-CONTRACT | 共同把 aggregate score 拆成可定位、可校准、可 abstain 的 evidence contract | analysis:DA-EVALUATION-CONTRACT |
| SF-2026-MA-VLA | score_7_9<br>potential_books_delta | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-MA-VLA |
| SF-2026-VGI-WHITE-PAPER | score_7_9 | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-VGI-WHITE-PAPER |
| SF-2026-CODE-WORLD-MODEL | score_7_9<br>potential_books_delta | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-CODE-WORLD-MODEL |
| SF-2026-SPECTRAL-ALLOCATION | score_7_9<br>potential_books_delta | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-SPECTRAL-ALLOCATION |
| SF-2026-PROGROUTER | score_7_9 | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-PROGROUTER |
| SF-2026-ASYMSPEC | score_7_9<br>potential_books_delta | subsumed | — | DA-SHARED-STATE-CONTROL | 改变 prefix state 的 identity、lifetime、placement 或 verification cost | analysis:DA-SHARED-STATE-CONTROL |
| SF-2026-STREAMPI | score_7_9 | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-STREAMPI |
| SF-2026-PREFIX-SLIDING | score_7_9<br>potential_books_delta | subsumed | — | DA-SHARED-STATE-CONTROL | 改变 prefix state 的 identity、lifetime、placement 或 verification cost | analysis:DA-SHARED-STATE-CONTROL |
| SF-2026-ZERO-WAM | score_7_9<br>potential_books_delta | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-ZERO-WAM |
| SF-2026-HY-MT2-REVISION | forced_review | not_selected | — | — | 形成独立机制分支，已由本 family 的完整 Review 与 Books Comparison 闭合 | analysis-decision:SF-2026-HY-MT2-REVISION |

<!-- analysis:DA-ENFORCEMENT-LAYERS:start -->
### 从提示级防护到独立 enforcement layer

Prompt policy 当时合理，因为它部署快且不需要改 runtime；但当 evaluation agent 能访问凭据、网络和 GPU shared state 时，风险状态已跨出文本边界。Groundhog 暴露模型参数/路由完整性会直接放大资源消耗，GIFT 把租户数据流约束下沉到 kernel，field-tier minimization 则把 disclosure 与 authorization 拆开。LMSM 进一步把 learned evidence、versioned policy 和独立 output gate 分层：收益是可替换 backend 与统一 release point，代价是 calibration drift、规则版本和额外 serving overhead。SkillShield/ReDiR 仍是有价值的 learned defense，但只负责降低风险，不能拥有最终 effect authority。
<!-- analysis:DA-ENFORCEMENT-LAYERS:end -->

<!-- analysis:DA-SHARED-STATE-CONTROL:start -->
### Prefix 从重复文本演进为跨阶段共享状态

静态 prefix cache 先解决重复 prefill；多 agent workflow 随后暴露“保留 prefix 会占用 batching memory”的冲突，TOPAS 因而把 cache residency 与 critical path 联合调度。训练侧 psRL 利用 update phase 的 immutable/global-visible prefix，在 placement 与负载均衡间复用；推理侧 Prefix Sliding 则把 immutable task prefix 与 mutable recent reasoning 分开，获得有界 KV，却牺牲中段依赖。AsymSpec 是另一条分支：drafter 持 full context、verifier 持 compressed view，用 verification cost 换准确性。共同原则不是总保留或总压缩，而是先定义状态 identity、owner、lifetime 和 commit/verification contract。
<!-- analysis:DA-SHARED-STATE-CONTROL:end -->

<!-- analysis:DA-EVALUATION-CONTRACT:start -->
### 从 aggregate score 到可定位且可拒答的证据合同

单一 outcome score 便于排序，却无法说明错误来自视觉事实、推理链还是语言接口。V-Rubrics 用 atomic criteria 和 prefix-localized reward 改善 credit assignment，但引入 rubric generator 偏差；Skill Issue 通过角色交换 self-play 把 interface language 与 reasoning language 分开，却仍受小模型与翻译影响。Localize-Then-Decide 进一步说明候选数量会破坏原始 confidence：先 conformal localization，再在 shortlist 上 calibrated decision 或 abstention。演进收益是 failure 可定位和风险可控，代价是 calibration data、exchangeability 假设与更复杂的 evidence lineage。
<!-- analysis:DA-EVALUATION-CONTRACT:end -->

<!-- analysis-decision:SF-2026-METIS-RUNTIME:start -->《Metis: Typed Runtime Mediation for Tool-Using Software Agents》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-METIS-RUNTIME:end -->
<!-- analysis-decision:SF-2026-JIT-AGENT:start -->《JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-JIT-AGENT:end -->
<!-- analysis-decision:SF-2026-RETRIEVALROUTER:start -->《RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieval》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-RETRIEVALROUTER:end -->
<!-- analysis-decision:SF-2026-TAILSFT:start -->《TailSFT: Filtered Fine-Tuning Improves Post-Training Performance》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-TAILSFT:end -->
<!-- analysis-decision:SF-2026-TACFORCING:start -->《TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-TACFORCING:end -->
<!-- analysis-decision:SF-2026-MA-VLA:start -->《MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-MA-VLA:end -->
<!-- analysis-decision:SF-2026-VGI-WHITE-PAPER:start -->《Visual General Intelligence: A White Paper》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-VGI-WHITE-PAPER:end -->
<!-- analysis-decision:SF-2026-CODE-WORLD-MODEL:start -->《Code World Model: Coding Agent as World Brain》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-CODE-WORLD-MODEL:end -->
<!-- analysis-decision:SF-2026-SPECTRAL-ALLOCATION:start -->《Spectral Allocation: Why Muon Outperforms Adam, and How to Improve Muon》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-SPECTRAL-ALLOCATION:end -->
<!-- analysis-decision:SF-2026-PROGROUTER:start -->《ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-PROGROUTER:end -->
<!-- analysis-decision:SF-2026-STREAMPI:start -->《StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-STREAMPI:end -->
<!-- analysis-decision:SF-2026-ZERO-WAM:start -->《Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-ZERO-WAM:end -->
<!-- analysis-decision:SF-2026-HY-MT2-REVISION:start -->《Hy-MT2 README max_context revision》保持独立 Deep Review；它不与三个入选单元共享同一状态 owner，强行合并会掩盖其自身 workload 与 failure boundary。<!-- analysis-decision:SF-2026-HY-MT2-REVISION:end -->

## 5. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-OPENAI-HF-INCIDENT | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L210 | books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L47 | existing:SF-2026-OPENAI-HF-INCIDENT | delta:SF-2026-OPENAI-HF-INCIDENT | Layering / Dependency | Integrate | books-review:SF-2026-OPENAI-HF-INCIDENT |
| SF-2026-GROUNDHOG-BITFLIP | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L405 | books/part-06-ai-infrastructure/71-multi-tenant.md#L69;books/part-06-ai-infrastructure/73-production-best-practice.md#L91 | existing:SF-2026-GROUNDHOG-BITFLIP | delta:SF-2026-GROUNDHOG-BITFLIP | Layering / Dependency | Integrate | books-review:SF-2026-GROUNDHOG-BITFLIP |
| SF-2026-METIS-RUNTIME | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L202 | books/part-07-agent/77-memory.md#L20;books/part-07-agent/79-planning.md#L42 | existing:SF-2026-METIS-RUNTIME | delta:SF-2026-METIS-RUNTIME | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-METIS-RUNTIME |
| SF-2026-GIFT-IFC | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33;books/part-06-ai-infrastructure/73-production-best-practice.md#L47 | existing:SF-2026-GIFT-IFC | delta:SF-2026-GIFT-IFC | Layering / Dependency | Integrate | books-review:SF-2026-GIFT-IFC |
| SF-2026-FIELD-TIER-MIN | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L202 | books/part-07-agent/77-memory.md#L46;books/part-07-agent/79-planning.md#L239 | existing:SF-2026-FIELD-TIER-MIN | delta:SF-2026-FIELD-TIER-MIN | Layering / Dependency | Integrate | books-review:SF-2026-FIELD-TIER-MIN |
| SF-2026-CASKG | AGENT-MEMORY | books/part-07-agent/77-memory.md#L401 | books/part-07-agent/76-rag.md#L239;books/part-07-agent/78-tool-calling.md#L82 | existing:SF-2026-CASKG | delta:SF-2026-CASKG | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-CASKG |
| SF-2026-TOPAS | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L183 | books/part-05-inference-system/55-pd-disaggregation.md#L300;books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L61 | existing:SF-2026-TOPAS | delta:SF-2026-TOPAS | Layering / Dependency | Integrate | books-review:SF-2026-TOPAS |
| SF-2026-POLYMEMDB | AGENT-MEMORY | books/part-07-agent/77-memory.md#L35 | books/part-07-agent/76-rag.md#L35;books/part-07-agent/78-tool-calling.md#L229 | existing:SF-2026-POLYMEMDB | delta:SF-2026-POLYMEMDB | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-POLYMEMDB |
| SF-2026-V-RUBRICS | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L18 | existing:SF-2026-V-RUBRICS | delta:SF-2026-V-RUBRICS | Layering / Dependency | Integrate | books-review:SF-2026-V-RUBRICS |
| SF-2026-RA-VLA | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L68 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L397;books/part-04-training-system/27-data.md#L214 | existing:SF-2026-RA-VLA | delta:SF-2026-RA-VLA | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-RA-VLA |
| SF-2026-JIT-AGENT | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L367 | books/part-07-agent/83-mcp.md#L83 | existing:SF-2026-JIT-AGENT | delta:SF-2026-JIT-AGENT | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-JIT-AGENT |
| SF-2026-RETRIEVALROUTER | AGENT-RAG | books/part-07-agent/76-rag.md#L239 | books/part-07-agent/75-context.md#L72;books/part-07-agent/77-memory.md#L113 | existing:SF-2026-RETRIEVALROUTER | delta:SF-2026-RETRIEVALROUTER | Layering / Dependency | Integrate | books-review:SF-2026-RETRIEVALROUTER |
| SF-2026-PSRL | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L233 | books/part-04-training-system/35-checkpoint.md#L122;books/part-04-training-system/37-tensor-parallel.md#L212 | existing:SF-2026-PSRL | delta:SF-2026-PSRL | Layering / Dependency | Integrate | books-review:SF-2026-PSRL |
| SF-2026-LMSM | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L388 | books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L65 | existing:SF-2026-LMSM | delta:SF-2026-LMSM | Layering / Dependency | Integrate | books-review:SF-2026-LMSM |
| SF-2026-REDIR | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L210 | books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L65 | existing:SF-2026-REDIR | delta:SF-2026-REDIR | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-REDIR |
| SF-2026-TAILSFT | TRAIN-SFT | books/part-04-training-system/29-sft.md#L114 | books/part-04-training-system/28-pretraining.md#L154;books/part-04-training-system/30-lora.md#L127 | existing:SF-2026-TAILSFT | delta:SF-2026-TAILSFT | Layering / Dependency | Integrate | books-review:SF-2026-TAILSFT |
| SF-2026-TACFORCING | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L264 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L378;books/part-04-training-system/27-data.md#L534 | existing:SF-2026-TACFORCING | delta:SF-2026-TACFORCING | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-TACFORCING |
| SF-2026-SKILLSHIELD | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L210 | books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L65 | existing:SF-2026-SKILLSHIELD | delta:SF-2026-SKILLSHIELD | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-SKILLSHIELD |
| SF-2026-LOCALIZE-DECIDE | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L168 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L132 | existing:SF-2026-LOCALIZE-DECIDE | delta:SF-2026-LOCALIZE-DECIDE | Layering / Dependency | Integrate | books-review:SF-2026-LOCALIZE-DECIDE |
| SF-2026-SKILL-ISSUE | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L146 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L18 | existing:SF-2026-SKILL-ISSUE | delta:SF-2026-SKILL-ISSUE | Layering / Dependency | Integrate | books-review:SF-2026-SKILL-ISSUE |
| SF-2026-MA-VLA | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L127 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251;books/part-04-training-system/27-data.md#L214 | existing:SF-2026-MA-VLA | delta:SF-2026-MA-VLA | Layering / Dependency | Integrate | books-review:SF-2026-MA-VLA |
| SF-2026-VGI-WHITE-PAPER | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L255;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16 | existing:SF-2026-VGI-WHITE-PAPER | delta:SF-2026-VGI-WHITE-PAPER | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-VGI-WHITE-PAPER |
| SF-2026-CODE-WORLD-MODEL | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L81;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171 | existing:SF-2026-CODE-WORLD-MODEL | delta:SF-2026-CODE-WORLD-MODEL | Layering / Dependency | Integrate | books-review:SF-2026-CODE-WORLD-MODEL |
| SF-2026-TAU-AGENT | AGENT-RAG | books/part-07-agent/76-rag.md#L239 | books/part-07-agent/75-context.md#L72;books/part-07-agent/77-memory.md#L113 | existing:SF-2026-TAU-AGENT | delta:SF-2026-TAU-AGENT | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-TAU-AGENT |
| SF-2026-SPECTRAL-ALLOCATION | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L154 | books/part-04-training-system/27-data.md#L103;books/part-04-training-system/29-sft.md#L55 | existing:SF-2026-SPECTRAL-ALLOCATION | delta:SF-2026-SPECTRAL-ALLOCATION | Layering / Dependency | Integrate | books-review:SF-2026-SPECTRAL-ALLOCATION |
| SF-2026-PROGROUTER | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L123 | books/part-07-agent/81-workflow.md#L201;books/part-07-agent/83-mcp.md#L164 | existing:SF-2026-PROGROUTER | delta:SF-2026-PROGROUTER | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-PROGROUTER |
| SF-2026-ASYMSPEC | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L190 | books/part-05-inference-system/47-pagedattention.md#L119;books/part-05-inference-system/49-tensorrt-llm.md#L735 | existing:SF-2026-ASYMSPEC | delta:SF-2026-ASYMSPEC | Layering / Dependency | Integrate | books-review:SF-2026-ASYMSPEC |
| SF-2026-STREAMPI | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L378;books/part-04-training-system/27-data.md#L534 | existing:SF-2026-STREAMPI | delta:SF-2026-STREAMPI | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-STREAMPI |
| SF-2026-PREFIX-SLIDING | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L315 | books/part-02-model/21-moe.md#L317;books/part-03-multimodal-world-models/23-multimodal-representation.md#L215 | existing:SF-2026-PREFIX-SLIDING | delta:SF-2026-PREFIX-SLIDING | Layering / Dependency | Integrate | books-review:SF-2026-PREFIX-SLIDING |
| SF-2026-ZERO-WAM | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L213 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251;books/part-04-training-system/27-data.md#L214 | existing:SF-2026-ZERO-WAM | delta:SF-2026-ZERO-WAM | Layering / Dependency | Integrate | books-review:SF-2026-ZERO-WAM |

<!-- books-review:SF-2026-OPENAI-HF-INCIDENT:start -->
<!-- existing:SF-2026-OPENAI-HF-INCIDENT:start -->`books/part-06-ai-infrastructure/72-security.md#L210` 原有主线已经定义 `PLATFORM-SECURITY` 的基础责任，但尚未完整表达“evaluation sandbox 中的 agent 获得了超出题目所需的凭据与网络能力，导致模型可把研究环境当作真实攻击面”这一约束。<!-- existing:SF-2026-OPENAI-HF-INCIDENT:end -->
<!-- delta:SF-2026-OPENAI-HF-INCIDENT:start -->当前书稿 diff 已把以下长期机制写入该 owner：把 environment containment、least privilege、secret boundary 和 independent monitoring 作为评测合同，而不是只约束 prompt；并保留边界：只能证明该次披露的链路与控制缺口；修复效果、其他模型与生产环境发生率未公开。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L47。前者拥有 tenant identity，后者拥有 release gate；二者均不拥有 evaluation sandbox 的 capability containment。<!-- delta:SF-2026-OPENAI-HF-INCIDENT:end -->
<!-- books-review:SF-2026-OPENAI-HF-INCIDENT:end -->

<!-- books-review:SF-2026-GROUNDHOG-BITFLIP:start -->
<!-- existing:SF-2026-GROUNDHOG-BITFLIP:start -->`books/part-06-ai-infrastructure/72-security.md#L405` 原有主线已经定义 `PLATFORM-SECURITY` 的基础责任，但尚未完整表达“MoE router 把终止行为集中到少数 expert 后，硬件位翻转可演化为 Denial-of-Wallet”这一约束。<!-- existing:SF-2026-GROUNDHOG-BITFLIP:end -->
<!-- delta:SF-2026-GROUNDHOG-BITFLIP:start -->当前书稿 diff 已把以下长期机制写入该 owner：定位与 EOS 等 token 强相关的 routing bits，破坏相关 expert 激活，使生成持续到 max-token 而尽量保持语义表面；并保留边界：是主动故障注入，不证明普通软错概率；硬件、精度、并发与线上检测 SLO 未完整披露。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L69;books/part-06-ai-infrastructure/73-production-best-practice.md#L91。前者只拥有 cache/serving 隔离，后者拥有容量与恢复；router 参数完整性与 fault-triggered output behavior 仍由 Security 拥有。<!-- delta:SF-2026-GROUNDHOG-BITFLIP:end -->
<!-- books-review:SF-2026-GROUNDHOG-BITFLIP:end -->

<!-- books-review:SF-2026-METIS-RUNTIME:start -->
<!-- existing:SF-2026-METIS-RUNTIME:start -->`books/part-07-agent/78-tool-calling.md#L202` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：provider stream 直接落到外部副作用时，permission、interference 与 lifecycle 缺少统一可审计语义。<!-- existing:SF-2026-METIS-RUNTIME:end -->
<!-- delta:SF-2026-METIS-RUNTIME:start -->论文提供的实现/实验是受限证据：30 个 matched real-I/O pairs、10-case fault matrix、child-boundary ablation 与五模型 Read-marker protocol；其机制“先将多 provider 输出规范化为 typed events，再由 permission gate、registry 与 lifecycle machine 决定 effect admission”没有改变现有设计结论。 相邻章节对读：books/part-07-agent/77-memory.md#L20;books/part-07-agent/79-planning.md#L42。Memory 拥有持久状态，Planning 拥有目标状态图；两者均不拥有外部 effect admission 与 tool lifecycle。<!-- delta:SF-2026-METIS-RUNTIME:end -->
<!-- books-review:SF-2026-METIS-RUNTIME:end -->

<!-- books-review:SF-2026-GIFT-IFC:start -->
<!-- existing:SF-2026-GIFT-IFC:start -->`books/part-06-ai-infrastructure/72-security.md#L16` 原有主线已经定义 `PLATFORM-SECURITY` 的基础责任，但尚未完整表达“共享 GPU serving 中 CPU orchestration 与 GPU kernel 都可能跨租户传播敏感数据”这一约束。<!-- existing:SF-2026-GIFT-IFC:end -->
<!-- delta:SF-2026-GIFT-IFC:start -->当前书稿 diff 已把以下长期机制写入该 owner：CPU 侧以 per-user encryption 隔离内容，GPU 侧静态分析 kernel flow 并以 decoupled tracker 执行信息流规则；GIFT-CC 再覆盖不可信 OS/hypervisor；并保留边界：只覆盖已建模 kernel 与论文 threat model；新 kernel、side channel、硬件/并发细节和独立复现仍缺失。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L33;books/part-06-ai-infrastructure/73-production-best-practice.md#L47。Multi-tenant 只声明隔离平面，Production 只承接发布合同；kernel-level information-flow enforcement 属于 Security。<!-- delta:SF-2026-GIFT-IFC:end -->
<!-- books-review:SF-2026-GIFT-IFC:end -->

<!-- books-review:SF-2026-FIELD-TIER-MIN:start -->
<!-- existing:SF-2026-FIELD-TIER-MIN:start -->`books/part-07-agent/78-tool-calling.md#L202` 原有主线已经定义 `AGENT-TOOL-CALLING` 的基础责任，但尚未完整表达“授权与审计同时读取完整 action parameters 会把敏感值永久写进不可删除 ledger”这一约束。<!-- existing:SF-2026-FIELD-TIER-MIN:end -->
<!-- delta:SF-2026-FIELD-TIER-MIN:start -->当前书稿 diff 已把以下长期机制写入该 owner：按字段而非 action 分类为 raw、projection、never-leave 三层；client 在最小化前承诺 canonical digest，并对 policy/tier schema 版本做 attestation；并保留边界：远端服务、schema evolution 与恶意 verifier 未被实证覆盖；projection 本身仍可能泄漏。 相邻章节对读：books/part-07-agent/77-memory.md#L46;books/part-07-agent/79-planning.md#L239。Memory 拥有写入决策，Planning 拥有 policy 约束；action 字段最小化和 side-effect admission 仍由 Tool Calling 拥有。<!-- delta:SF-2026-FIELD-TIER-MIN:end -->
<!-- books-review:SF-2026-FIELD-TIER-MIN:end -->

<!-- books-review:SF-2026-CASKG:start -->
<!-- existing:SF-2026-CASKG:start -->`books/part-07-agent/77-memory.md#L401` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：技能库扩大后，纯向量召回忽略程序依赖，普通图检索又依赖不可靠边。<!-- existing:SF-2026-CASKG:end -->
<!-- delta:SF-2026-CASKG:start -->论文提供的实现/实验是受限证据：六个 LLM，在 ALFWorld ID-140 与 ScienceWorld U211 上比较任务得分和环境步数，并含 ablation；其机制“从语义、词法、I/O 与结构生成高召回候选图，再用方向化 counterfactual probe 与 Bayesian smoothing 校准边，离线发布 state-filtered graph”没有改变现有设计结论。 相邻章节对读：books/part-07-agent/76-rag.md#L239;books/part-07-agent/78-tool-calling.md#L82。RAG 拥有在线相关性，Tool Calling 拥有可执行 catalog；技能关系的派生、校准与长期发布属于 Memory。<!-- delta:SF-2026-CASKG:end -->
<!-- books-review:SF-2026-CASKG:end -->

<!-- books-review:SF-2026-TOPAS:start -->
<!-- existing:SF-2026-TOPAS:start -->`books/part-05-inference-system/56-inference-scheduling.md#L183` 原有主线已经定义 `INFER-SCHEDULING` 的基础责任，但尚未完整表达“保留 agent prefix 可减少 prefill，却占用 KV 空间并挤压 batching；只优化 cache hit 或 workflow progress 都会延长 JCT”这一约束。<!-- existing:SF-2026-TOPAS:end -->
<!-- delta:SF-2026-TOPAS:start -->当前书稿 diff 已把以下长期机制写入该 owner：联合选择保留的 prefix 与执行请求，以最长剩余服务路径收益、下游 prefix reuse、迁移/抢占成本和 task aging 评分 post-decision state；并保留边界：结果依赖 synthetic DAG、特定 workflow 与共享 KV budget；生产 fairness、负载漂移和 tail-SLO 未证明。 相邻章节对读：books/part-05-inference-system/55-pd-disaggregation.md#L300;books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L61。PD 只拥有阶段 handoff，平台章只拥有 control-plane contract；跨 workflow 的 prefix-retention/request joint choice 属于 Inference Scheduling。<!-- delta:SF-2026-TOPAS:end -->
<!-- books-review:SF-2026-TOPAS:end -->

<!-- books-review:SF-2026-POLYMEMDB:start -->
<!-- existing:SF-2026-POLYMEMDB:start -->`books/part-07-agent/77-memory.md#L35` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：单一存储无法同时表达向量、图、概率和时空记忆，长期冲突又缺少 provenance。<!-- existing:SF-2026-POLYMEMDB:end -->
<!-- delta:SF-2026-POLYMEMDB:start -->论文提供的实现/实验是受限证据：四页 demonstration 描述系统接口与示例，没有广泛定量评估或故障注入；其机制“以 polyglot stores 管理多种 memory，并用 temporal decay、semiring aggregation 与 provenance chain 处理冲突”没有改变现有设计结论。 相邻章节对读：books/part-07-agent/76-rag.md#L35;books/part-07-agent/78-tool-calling.md#L229。RAG 只拥有 ingestion/retrieval，Tool Calling 只约束 observations；多存储长期状态及 provenance 冲突属于 Memory。<!-- delta:SF-2026-POLYMEMDB:end -->
<!-- books-review:SF-2026-POLYMEMDB:end -->

<!-- books-review:SF-2026-V-RUBRICS:start -->
<!-- existing:SF-2026-V-RUBRICS:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md#L724` 原有主线已经定义 `PLATFORM-EVALUATION-SYSTEM` 的基础责任，但尚未完整表达“多模态 post-training 的单一 outcome reward 无法定位哪条视觉事实、推理步骤或指令约束出错”这一约束。<!-- existing:SF-2026-V-RUBRICS:end -->
<!-- delta:SF-2026-V-RUBRICS:start -->当前书稿 diff 已把以下长期机制写入该 owner：把答案拆成 VF/RC/IF atomic rubrics，并在有证据 span 时进行 component-wise、prefix-localized credit assignment；并保留边界：rubric 由 Gemini-3-Pro 标注且继承其偏差；不外推其他模型、领域或无 reference 的开放任务。 相邻章节对读：books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L18。Scheduler 拥有 placement，Monitoring 拥有 runtime signals；rubric schema、credit assignment 与 evaluator bias 属于 Evaluation。<!-- delta:SF-2026-V-RUBRICS:end -->
<!-- books-review:SF-2026-V-RUBRICS:end -->

<!-- books-review:SF-2026-RA-VLA:start -->
<!-- existing:SF-2026-RA-VLA:start -->`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L68` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：VLA 面对新任务时，表层相似 retrieval 与 pretrained policy inertia 阻碍 expert context 转成动作。<!-- existing:SF-2026-RA-VLA:end -->
<!-- delta:SF-2026-RA-VLA:start -->论文提供的实现/实验是受限证据：LIBERO 与真实 UR5e 任务，对 success 与计算效率作作者比较；其机制“用 behavior-aligned retrieval 选择示例，并通过 grounded execution pipeline 强制策略利用功能线索”没有改变现有设计结论。 相邻章节对读：books/part-03-multimodal-world-models/25-multimodal-world-models.md#L397;books/part-04-training-system/27-data.md#L214。World Models 只界定 predictive state，Data 只拥有训练样本；检索如何进入闭环 action policy 属于 Embodied VLA。<!-- delta:SF-2026-RA-VLA:end -->
<!-- books-review:SF-2026-RA-VLA:end -->

<!-- books-review:SF-2026-JIT-AGENT:start -->
<!-- existing:SF-2026-JIT-AGENT:start -->`books/part-07-agent/84-agent-platform.md#L367` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：固定 harness 把 memory、planning、action protocol 和 tool orchestration 固化为人工任务特化配置。<!-- existing:SF-2026-JIT-AGENT:end -->
<!-- delta:SF-2026-JIT-AGENT:start -->论文提供的实现/实验是受限证据：九个 benchmark，跨 DeepSeek、GLM、MiMo、Qwen 等模型，与 OpenCode/Claude Code 等 harness 比较；其机制“以四模块协议把 harness 变成可生成 artifact，并从任务、repair 信号和历史配置 archive 即时合成与自演化”没有改变现有设计结论。 相邻章节对读：books/part-07-agent/83-mcp.md#L83。MCP 只拥有 protocol lifecycle；可生成 harness artifact、run identity 与平台化演进属于 Agent Platform。<!-- delta:SF-2026-JIT-AGENT:end -->
<!-- books-review:SF-2026-JIT-AGENT:end -->

<!-- books-review:SF-2026-RETRIEVALROUTER:start -->
<!-- existing:SF-2026-RETRIEVALROUTER:start -->`books/part-07-agent/76-rag.md#L239` 原有主线已经定义 `AGENT-RAG` 的基础责任，但尚未完整表达“text/multimodal 与 dense/late-interaction pipeline 在 relevance、latency 和 index footprint 上不存在静态最优”这一约束。<!-- existing:SF-2026-RETRIEVALROUTER:end -->
<!-- delta:SF-2026-RETRIEVALROUTER:start -->当前书稿 diff 已把以下长期机制写入该 owner：冻结 Qwen3-0.6B 主体并以 LoRA query encoder 和 soft reward target，在五类 pipeline 间按 nDCG/latency 权衡逐 query 路由；并保留边界：需同时维护约 40GB 多索引；query-only 看不到 document layout，未验证跨域 routing，oracle gap 仍大。 相邻章节对读：books/part-07-agent/75-context.md#L72;books/part-07-agent/77-memory.md#L113。Context 拥有 assembly，Memory 拥有长期 read/write；逐 query retrieval pipeline selection 属于 RAG。<!-- delta:SF-2026-RETRIEVALROUTER:end -->
<!-- books-review:SF-2026-RETRIEVALROUTER:end -->

<!-- books-review:SF-2026-PSRL:start -->
<!-- existing:SF-2026-PSRL:start -->`books/part-04-training-system/36-distributed-training.md#L233` 原有主线已经定义 `TRAIN-DISTRIBUTED-TRAINING` 的基础责任，但尚未完整表达“tree/step-wise agentic RL 使 update 而非 rollout 成为瓶颈，同时样本间出现大量 immutable prefix redundancy”这一约束。<!-- existing:SF-2026-PSRL:end -->
<!-- delta:SF-2026-PSRL:start -->当前书稿 diff 已把以下长期机制写入该 owner：利用 update phase 的 global visibility，把 prefix-sharing workload placement 与动态 block KV manager 联合优化，在 reuse 与 load balance 间调度；并保留边界：不外推普通 pretraining；代码在 v1 仅承诺将公开，硬件拓扑、长度分布和 tail latency 需按原表解释。 相邻章节对读：books/part-04-training-system/35-checkpoint.md#L122;books/part-04-training-system/37-tensor-parallel.md#L212。Checkpoint 拥有 durable commit，TP 拥有 tensor partition communication；update-phase prefix placement 与 runtime KV ownership 属于 Distributed Training。<!-- delta:SF-2026-PSRL:end -->
<!-- books-review:SF-2026-PSRL:end -->

<!-- books-review:SF-2026-LMSM:start -->
<!-- existing:SF-2026-LMSM:start -->`books/part-06-ai-infrastructure/72-security.md#L388` 原有主线已经定义 `PLATFORM-SECURITY` 的基础责任，但尚未完整表达“interpretability signal 若各自绑定 calibration、policy 与 intervention，就无法形成稳定 enforcement substrate”这一约束。<!-- existing:SF-2026-LMSM:end -->
<!-- delta:SF-2026-LMSM:start -->当前书稿 diff 已把以下长期机制写入该 owner：把 calibrated evidence backend、versioned policy 和 independent buffered-output gate 分离，保持 request identity 穿过 continuous batching；并保留边界：learned backend 可能漂移且不能替代 reference monitor；结果只覆盖特定模型、规则和攻击集。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L65。Tenant identity 和 readiness gate 只是输入合同；calibrated sensor 到 safe-commit enforcement 的控制权属于 Security。<!-- delta:SF-2026-LMSM:end -->
<!-- books-review:SF-2026-LMSM:end -->

<!-- books-review:SF-2026-REDIR:start -->
<!-- existing:SF-2026-REDIR:start -->`books/part-06-ai-infrastructure/72-security.md#L210` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：多轮攻击把风险分散到单独看似合理的 request/action，单步 filter 无法重组意图。<!-- existing:SF-2026-REDIR:end -->
<!-- delta:SF-2026-REDIR:start -->论文提供的实现/实验是受限证据：两个 agent-safety benchmark、三个 model families、八个 held-out tool domains；测 ASR、benign fidelity 与 overhead；其机制“在每次 action 前将 trajectory 压成 latent safety representation，并用同模型 cross-view supervision 注入冻结 base model 的生成过程”没有改变现有设计结论。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L65。相邻章拥有 identity 和 release admission，不拥有 multi-turn intent reconstruction 与 action safety policy。<!-- delta:SF-2026-REDIR:end -->
<!-- books-review:SF-2026-REDIR:end -->

<!-- books-review:SF-2026-TAILSFT:start -->
<!-- existing:SF-2026-TAILSFT:start -->`books/part-04-training-system/29-sft.md#L114` 原有主线已经定义 `TRAIN-SFT` 的基础责任，但尚未完整表达“SFT 平均优化已拟合样本会浪费容量，并可能产生不适合后续 RL 的低 coverage 初始化”这一约束。<!-- existing:SF-2026-TAILSFT:end -->
<!-- delta:SF-2026-TAILSFT:start -->当前书稿 diff 已把以下长期机制写入该 owner：训练时过滤已拟合 sequence，把梯度集中到 under-modeled tail，并用轻量诊断判断何时值得启用；并保留边界：只覆盖一个 7B 家族与特定后训练配方；不能推广为所有 easy sample 都应丢弃。 相邻章节对读：books/part-04-training-system/28-pretraining.md#L154;books/part-04-training-system/30-lora.md#L127。Pretraining 拥有通用 optimizer 轨迹，LoRA 拥有参数化更新空间；demonstration loss 的样本选择属于 SFT。<!-- delta:SF-2026-TAILSFT:end -->
<!-- books-review:SF-2026-TAILSFT:end -->

<!-- books-review:SF-2026-TACFORCING:start -->
<!-- existing:SF-2026-TACFORCING:start -->`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L264` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：chunk VLA 在执行前一次读取 tactile，接触状态变化后条件已过期。<!-- existing:SF-2026-TACFORCING:end -->
<!-- delta:SF-2026-TACFORCING:start -->论文提供的实现/实验是受限证据：六个 UniVTAC 仿真与三个实机 contact-rich tasks，报告 success rate；其机制“以 streaming action expert 在执行中持续接收 tactile，并用 EATA 只让临近执行动作关注最新触觉，避免独立高频控制器”没有改变现有设计结论。 相邻章节对读：books/part-03-multimodal-world-models/25-multimodal-world-models.md#L378;books/part-04-training-system/27-data.md#L534。World Models 拥有 predicted transition，Data 拥有 sampling distribution；实时 tactile-conditioned action commit 属于 Embodied VLA。<!-- delta:SF-2026-TACFORCING:end -->
<!-- books-review:SF-2026-TACFORCING:end -->

<!-- books-review:SF-2026-SKILLSHIELD:start -->
<!-- existing:SF-2026-SKILLSHIELD:start -->`books/part-06-ai-infrastructure/72-security.md#L210` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：API-only coding agent 无法改权重，而逐步外部 classifier/reference monitor 又增加运行成本。<!-- existing:SF-2026-SKILLSHIELD:end -->
<!-- delta:SF-2026-SKILLSHIELD:start -->论文提供的实现/实验是受限证据：六模型 RedCode、两类非自适应 jailbreak、731 benign prompts；比较 ASR、severity 与 refusal；其机制“离线从攻击/失败合成 security skills，以固定 prompt budget 在 all-class、bundle、per-class 三种 scope 注入整个 tool loop”没有改变现有设计结论。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L65。相邻章只消费 security policy 结果；prompt-space defense 的 threat model 与 safety decision 属于 Security。<!-- delta:SF-2026-SKILLSHIELD:end -->
<!-- books-review:SF-2026-SKILLSHIELD:end -->

<!-- books-review:SF-2026-LOCALIZE-DECIDE:start -->
<!-- existing:SF-2026-LOCALIZE-DECIDE:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md#L168` 原有主线已经定义 `PLATFORM-EVALUATION-SYSTEM` 的基础责任，但尚未完整表达“候选数增加会把 probability mass 摊薄，破坏 confidence 与 human disagreement 的单调关系”这一约束。<!-- existing:SF-2026-LOCALIZE-DECIDE:end -->
<!-- delta:SF-2026-LOCALIZE-DECIDE:start -->当前书稿 diff 已把以下长期机制写入该 owner：先用 conformal prediction 产生高概率包含 human-preferred answer 的 shortlist，再在 shortlist 内 calibrated decide-or-abstain；并保留边界：保证依赖 exchangeability 与校准分布；不是模型自知，也不覆盖分布漂移或 judge 攻击。 相邻章节对读：books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L132。Scheduler 处理 resource choice，Monitoring 处理 aggregate signals；calibrated uncertainty guarantee 与 abstention contract 属于 Evaluation。<!-- delta:SF-2026-LOCALIZE-DECIDE:end -->
<!-- books-review:SF-2026-LOCALIZE-DECIDE:end -->

<!-- books-review:SF-2026-SKILL-ISSUE:start -->
<!-- existing:SF-2026-SKILL-ISSUE:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md#L146` 原有主线已经定义 `PLATFORM-EVALUATION-SYSTEM` 的基础责任，但尚未完整表达“知识和通用 benchmark 会混淆 language interface 对实际技能执行的影响”这一约束。<!-- existing:SF-2026-SKILL-ISSUE:end -->
<!-- delta:SF-2026-SKILL-ISSUE:start -->当前书稿 diff 已把以下长期机制写入该 owner：同模型 self-play 固定 game/rules/state/action，仅改变双方界面语言并交换角色；另把 interface language 与 reasoning language 分离；并保留边界：仅小模型与八语言；self-play 测相对强弱而非绝对部署质量，translation/tokenization 仍是混杂因素。 相邻章节对读：books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L18。相邻章不定义 counterfactual benchmark distribution；语言变量隔离与结果边界属于 Evaluation。<!-- delta:SF-2026-SKILL-ISSUE:end -->
<!-- books-review:SF-2026-SKILL-ISSUE:end -->

<!-- books-review:SF-2026-MA-VLA:start -->
<!-- existing:SF-2026-MA-VLA:start -->`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L127` 原有主线已经定义 `MULTIMODAL-EMBODIED-VLA` 的基础责任，但尚未完整表达“单一 global instruction 无法显式分配多臂子目标，模型容易把技能绑定固定 arm identity”这一约束。<!-- existing:SF-2026-MA-VLA:end -->
<!-- delta:SF-2026-MA-VLA:start -->当前书稿 diff 已把以下长期机制写入该 owner：planner 生成有限 atomic prompts；统一 Pi0 executor 联合输出多臂 action；Arm Shuffle 联合置换 state/view/prompt/action tuple，View Dropout 增强视角鲁棒性；并保留边界：只证明 seen atomic skills 的组合重排；planner error、控制频率、latency、安全与 open-world skill acquisition 未评估。 相邻章节对读：books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251;books/part-04-training-system/27-data.md#L214。World Models 拥有环境状态，Data 拥有 augmentation source；多臂 action schema 与 closed-loop execution 属于 Embodied VLA。<!-- delta:SF-2026-MA-VLA:end -->
<!-- books-review:SF-2026-MA-VLA:end -->

<!-- books-review:SF-2026-VGI-WHITE-PAPER:start -->
<!-- existing:SF-2026-VGI-WHITE-PAPER:start -->`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：视觉智能研究缺少从输入模态、学习范式到 benchmark 的统一问题框架。<!-- existing:SF-2026-VGI-WHITE-PAPER:end -->
<!-- delta:SF-2026-VGI-WHITE-PAPER:start -->论文提供的实现/实验是受限证据：证据是观点综述和研究议程，不存在可归因于一项机制的 matched benchmark；其机制“以多作者 white paper 梳理 vision-centered AGI 的定义、模态、学习、评测与语言关系，而非提出单一可执行系统”没有改变现有设计结论。 相邻章节对读：books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L255;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16。Generative Paradigms 只比较生成 factorization，Embodied VLA 只拥有 physical action loop；跨预测 channel 的 world-state distinction 由 World Models 拥有。<!-- delta:SF-2026-VGI-WHITE-PAPER:end -->
<!-- books-review:SF-2026-VGI-WHITE-PAPER:end -->

<!-- books-review:SF-2026-CODE-WORLD-MODEL:start -->
<!-- existing:SF-2026-CODE-WORLD-MODEL:start -->`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251` 原有主线已经定义 `MULTIMODAL-WORLD-MODELS` 的基础责任，但尚未完整表达“纯视频 world model 观察结果却不拥有规则，难以维持可修改、持久且可执行的因果状态”这一约束。<!-- existing:SF-2026-CODE-WORLD-MODEL:end -->
<!-- delta:SF-2026-CODE-WORLD-MODEL:start -->当前书稿 diff 已把以下长期机制写入该 owner：拆分 S_exe/S_vis：coding agent 管低频推理与机制修订，code 管确定性 transition，video model 通过可寻址 proxy 渲染 observation；并保留边界：没有实时、控制或因果定量评估；agent 不能从零可靠构造复杂 simulator，项目页没有公开代码。 相邻章节对读：books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L81;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171。前者拥有 token commit，后者拥有 sensor/action freshness；可修订 simulator state 与 visual proxy 的 ownership 属于 World Models。<!-- delta:SF-2026-CODE-WORLD-MODEL:end -->
<!-- books-review:SF-2026-CODE-WORLD-MODEL:end -->

<!-- books-review:SF-2026-TAU-AGENT:start -->
<!-- existing:SF-2026-TAU-AGENT:start -->`books/part-07-agent/76-rag.md#L239` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：交通视频异常问答需要从长视频中取回与 query 相关的时间段、字幕与对象轨迹。<!-- existing:SF-2026-TAU-AGENT:end -->
<!-- delta:SF-2026-TAU-AGENT:start -->论文提供的实现/实验是受限证据：AI City Track3/FETV/PSI-VQA；Gemini caption、GPT-5.4 agent、Qwen3-VL-8B LoRA、2×RTX PRO 6000；其机制“central agent 编排 2秒 caption segments、open-vocabulary tracking 与迭代 evidence selection，再把 slow-fast frames 和 top-k 文本交给 VLM”没有改变现有设计结论。 相邻章节对读：books/part-07-agent/75-context.md#L72;books/part-07-agent/77-memory.md#L113。Context 拥有最终 packing，Memory 拥有持久 state；query-conditioned evidence acquisition 与 reranking 属于 RAG。<!-- delta:SF-2026-TAU-AGENT:end -->
<!-- books-review:SF-2026-TAU-AGENT:end -->

<!-- books-review:SF-2026-SPECTRAL-ALLOCATION:start -->
<!-- existing:SF-2026-SPECTRAL-ALLOCATION:start -->`books/part-04-training-system/28-pretraining.md#L154` 原有主线已经定义 `TRAIN-PRETRAINING` 的基础责任，但尚未完整表达“Muon 的统一正交缩放没有解释为何优于 Adam，也可能低估 loss landscape tolerant bulk 的可用步长”这一约束。<!-- existing:SF-2026-SPECTRAL-ALLOCATION:end -->
<!-- delta:SF-2026-SPECTRAL-ALLOCATION:start -->当前书稿 diff 已把以下长期机制写入该 owner：在 held-out data 上按 momentum singular directions 探测 loss-optimal step，区分 volatile head 与 tolerant bulk；SAMuon/SAMuon-lite 对 bulk 放大；并保留边界：仅小到中型模型；静态 spectral prior 在 frontier scale、不同 architecture 与长期稳定性上未证明。 相邻章节对读：books/part-04-training-system/27-data.md#L103;books/part-04-training-system/29-sft.md#L55。Data 拥有 sampling weights，SFT 拥有 conditional demonstration objective；optimizer 的 spectral update geometry 属于 Pretraining。<!-- delta:SF-2026-SPECTRAL-ALLOCATION:end -->
<!-- books-review:SF-2026-SPECTRAL-ALLOCATION:end -->

<!-- books-review:SF-2026-PROGROUTER:start -->
<!-- existing:SF-2026-PROGROUTER:start -->`books/part-07-agent/82-multi-agent.md#L123` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：one-shot cascade router 无法随 multi-step workflow 的剩余难度、进度和预算变化调整模型。<!-- existing:SF-2026-PROGROUTER:end -->
<!-- delta:SF-2026-PROGROUTER:start -->论文提供的实现/实验是受限证据：HumanEval+、MBPP、MATH-500、ASQA 四个 benchmark，跨代码、数学与 RAG workflow；其机制“以多视角 progress scorer、dual-path predictor 与 meta-gating 估计每步候选 LLM 的 progress gain，在线平衡 time/cost”没有改变现有设计结论。 相邻章节对读：books/part-07-agent/81-workflow.md#L201;books/part-07-agent/83-mcp.md#L164。Workflow 拥有 durable state，MCP 拥有 protocol boundary；跨 agent/model 的 per-step routing policy 属于 Multi-Agent。<!-- delta:SF-2026-PROGROUTER:end -->
<!-- books-review:SF-2026-PROGROUTER:end -->

<!-- books-review:SF-2026-ASYMSPEC:start -->
<!-- existing:SF-2026-ASYMSPEC:start -->`books/part-05-inference-system/48-speculative-decoding.md#L190` 原有主线已经定义 `INFER-SPECULATIVE-DECODING` 的基础责任，但尚未完整表达“压缩 verifier context 降成本却损伤正确性，而传统 speculative decoding 强制 drafter/verifier 同 context”这一约束。<!-- existing:SF-2026-ASYMSPEC:end -->
<!-- delta:SF-2026-ASYMSPEC:start -->当前书稿 diff 已把以下长期机制写入该 owner：让轻量 drafter 读 full context、large verifier 读 compressed view，以 contrastive delta-fusion 和 divergence-aware acceptance gate 传递被压缩信号；并保留边界：只在特定确定性设置验证；不是 token-exact 的普通 SD 等价保证，压缩器与 verifier drift 仍可能失效。 相邻章节对读：books/part-05-inference-system/47-pagedattention.md#L119;books/part-05-inference-system/49-tensorrt-llm.md#L735。PagedAttention 拥有 KV storage，Execution Engine 拥有 compiled runtime；draft/verify acceptance semantics 属于 Speculative Decoding。<!-- delta:SF-2026-ASYMSPEC:end -->
<!-- books-review:SF-2026-ASYMSPEC:end -->

<!-- books-review:SF-2026-STREAMPI:start -->
<!-- existing:SF-2026-STREAMPI:start -->`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171` 已通过状态 owner、控制/数据流与 failure boundary 承载该问题：single-frame VLA 丢失过去 observation，且同步训练与实机异步采样存在 timing gap。<!-- existing:SF-2026-STREAMPI:end -->
<!-- delta:SF-2026-STREAMPI:start -->论文提供的实现/实验是受限证据：LIBERO 与 memory-dependent/precise-perception 实机任务，对 pi0.5 比较 success；其机制“把 observation-instruction pair 作为原子单元，单元内双向融合、跨单元 causal attention；random-interval training 适应异步 frame timing”没有改变现有设计结论。 相邻章节对读：books/part-03-multimodal-world-models/25-multimodal-world-models.md#L378;books/part-04-training-system/27-data.md#L534。World Models 拥有 transition semantics，Data 拥有 sampling；online observation freshness 与 action conditioning 属于 Embodied VLA。<!-- delta:SF-2026-STREAMPI:end -->
<!-- books-review:SF-2026-STREAMPI:end -->

<!-- books-review:SF-2026-PREFIX-SLIDING:start -->
<!-- existing:SF-2026-PREFIX-SLIDING:start -->`books/part-02-model/22-long-context.md#L315` 原有主线已经定义 `MODEL-LONG-CONTEXT` 的基础责任，但尚未完整表达“长 reasoning 保留完整轨迹导致 KV 与 attention 成本随思考长度增长，而近期状态和固定任务契约的重要性不同”这一约束。<!-- existing:SF-2026-PREFIX-SLIDING:end -->
<!-- delta:SF-2026-PREFIX-SLIDING:start -->当前书稿 diff 已把以下长期机制写入该 owner：永久保留 system/task prefix 与最近 reasoning window，丢弃中间 token；继续 RoPE position 复用 KV，RL 侧用约4×window context、末端 loss mask；并保留边界：LiveCodeBench 旧代码依赖受损；短生成收益小、tool output 可淹没 window；v1 时 repo 只有 README/License，无实现代码。 相邻章节对读：books/part-02-model/21-moe.md#L317;books/part-03-multimodal-world-models/23-multimodal-representation.md#L215。MoE 拥有 conditional compute，Multimodal Representation 拥有 modality identity；token-retention policy 与 context-loss boundary 属于 Long Context。<!-- delta:SF-2026-PREFIX-SLIDING:end -->
<!-- books-review:SF-2026-PREFIX-SLIDING:end -->

<!-- books-review:SF-2026-ZERO-WAM:start -->
<!-- existing:SF-2026-ZERO-WAM:start -->`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L213` 原有主线已经定义 `MULTIMODAL-EMBODIED-VLA` 的基础责任，但尚未完整表达“语言不足以完整指定新 manipulation task，而 paired human-robot demonstrations 稀缺”这一约束。<!-- existing:SF-2026-ZERO-WAM:end -->
<!-- delta:SF-2026-ZERO-WAM:start -->当前书稿 diff 已把以下长期机制写入该 owner：把 human video 作为 in-context task contract；causal model 先预测 future robot video 再由 inverse dynamics 预测 action；IFP 强迫利用 human prefix，HumanGen 合成74.2K pairs；并保留边界：synthetic video/VLM filter 会引入偏差；仅 tabletop、小样本实机，embodiment gap 与 artifact 均未闭合。 相邻章节对读：books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251;books/part-04-training-system/27-data.md#L214。World Models 拥有 latent transition，Data 拥有 paired-data construction；human-video task contract 到 robot action 的 closed loop 属于 Embodied VLA。<!-- delta:SF-2026-ZERO-WAM:end -->
<!-- books-review:SF-2026-ZERO-WAM:end -->


## 6. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260827-COVERAGE | fresh-context:aug27_28_fresh_audit | coverage | audit-target:coverage | — | 34/34 family 与 receipt union、严格窗口、Atom archive 水位和 HF 非阻塞降级均已独立复核。 | passed |
| SA-20260827-EVIDENCE | fresh-context:aug27_28_fresh_audit | evidence | validator:review-completion-v1 | — | 34/34 route-matched Review、30/30 实验合同、exact locator、评分和证据边界均已独立复核。 | passed |
| SA-20260827-DEEP | fresh-context:aug27_28_fresh_audit | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | 三个长叙事单元的共享状态 owner 与 subsumption 已复核；叙事上限未替代逐 family Review。 | passed |
| SA-20260827-BOOKS | fresh-context:aug27_28_fresh_audit | books | validator:books-comparison-v1; review:SF-2026-AGENTIC-GAME-WM; review:SF-2026-MINIMAX-FINANCIAL | — | 30/30 技术 family 比较、18 项 Integrate、canonical owner、相邻章节和 evidence boundary 均已复核；两项 Weekly Only disposition 也已逐 family 验收。 | passed |

## 7. Ignored Noise

- 新闻转载、社交讨论和没有 primary artifact 的 benchmark 宣传不进入 denominator。
- HF recommendation date 不覆盖 arXiv v1 first-public date；同一 family 不因推荐或仓库更新重复评分。
- Repository `pushed_at`、sitemap `lastmod`、财报发布时间和 branch merge 不自动等于新技术机制。

## 8. Recommended Action

- 保留 18 项已通过 fresh-context owner/adjacent 与证据边界审计的 Books Integration；后续新证据按同一 Source Family revision 处理。
- 12 项 `No Change — Existing Coverage` 保留为 implementation/evaluation evidence，不在章末堆论文列表。
- Hy-MT2 只保留 8192 示例配置的版本事实；UniRL maintenance、MiniMax 财报和观点性 game-data 路线不进入机制正文。

## 9. Repository Changes

- 完成 `papers/2026/08/27/README.md` 的 V2.1 表格、34 项 Source Review、Deep Analysis Selection、Books Comparison、Semantic Audit 与 Gate 状态。
- 本次 27/28 日共享主流程已把本日 18 项长期机制增量写入对应 canonical owner；不生成 Thursday Weekly，不修改 ROADMAP 或 LEARNING_STATE，不 stage、commit 或 push。

## 10. Open Questions

- HF listing export 仍不可用；Weekly 应重新执行一周 bounded discovery，但不能用 HF 日期覆盖 arXiv v1 owner date。
- Prefix Sliding、Zero-WAM、Code World Model 等仍缺生产级 tail-SLO、长期一致性或安全 matched evidence；后续证据应作为同 family revision 处理。

## 11. Sources

### 模型与研究机构

- OpenAI, “The Hugging Face incident and the road ahead”, 2026-08-26, accessed 2026-08-28: https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- OpenAI, “OpenAI–Hugging Face Incident Technical Report”, 2026-08-26, accessed 2026-08-28: https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf
- METR / Redwood Research, independent incident assessment, 2026-08-26, accessed 2026-08-28: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- Google DeepMind, “Visual General Intelligence: A White Paper”, 2026-08-26, accessed 2026-08-28: https://deepmind.google/research/publications/270149/

### arXiv / 学术来源

- Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25276v1
- Metis: Typed Runtime Mediation for Tool-Using Software Agents, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25322v1
- Here is a GIFT: Enforcing User Data Isolation in LLM Serving via GPU Information Flow Tracking, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25431v1
- Separating Disclosure from Authorization: Field-Tier Minimization for Agent Action Mediation, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25474v1
- CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25500v1
- Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25518v1
- TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25523v1
- PolyMemDB: A Polyglot Database System for AI Memory Management, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25577v1
- V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25580v1
- RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25585v1
- JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25593v1
- RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieval, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25625v1
- psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25683v1
- LMSM: LLM Security Framework Inspired by Linux Security Modules, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25697v1
- Reassembling Distributed Risk: Trajectory-Conditioned Action Generation for Multi-Turn Agent Safety, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25711v1
- TailSFT: Filtered Fine-Tuning Improves Post-Training Performance, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25756v1
- TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25798v1
- SkillShield: Prompt-Space Security Skills for LLM Coding Agents, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25817v1
- Localize-Then-Decide Guarantees for LLM Judgments, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25824v1
- Skill Issue: Are Skills Language-Invariant in LLMs?, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25832v1
- MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25864v1
- Visual General Intelligence: A White Paper, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25924v1
- Code World Model: Coding Agent as World Brain, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25927v1
- TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25935v1
- Spectral Allocation: Why Muon Outperforms Adam, and How to Improve Muon, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25990v1
- ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.25992v1
- AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.26004v1
- StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.26067v1
- Prefix Sliding for efficient test-time scaling, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.26070v1
- Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization, v1 2026-08-26, accessed 2026-08-28: https://arxiv.org/html/2608.26103v1

### AI Infra 与工程项目

- Tencent-Hunyuan Hy-MT2 exact revision, 2026-08-26: https://github.com/Tencent-Hunyuan/Hy-MT2/commit/ff1903ecaa724e10951a23c16817a2413c752b35
- Tencent-Hunyuan UniRL branch sync, 2026-08-26: https://github.com/Tencent-Hunyuan/UniRL/commit/96747df21c2940b6cd68fe38cfecb93f63cc628d
- MiniMax first-half 2026 financial results, 2026-08-26: https://www.minimax.io/news/minimax-announces-first-half-2026-financial-results-1787744160
