# Required Daily Organization Receipt — 2026-08-28

- Window: `[2026-08-27T09:00:00+08:00, 2026-08-28T09:00:00+08:00)`
- Executed: `2026-08-28T08:55:00+08:00` ～ `2026-08-28T09:25:00+08:00`
- Registry: `docs/RESEARCH_SOURCES.md`, version 2026-08-25
- Result: 19/19 Required Daily organization sources have a dated listing decision; one OpenAI day-precision context event was retained, the remaining organization surfaces yielded no in-window technical Source Family.

The official endpoints were checked in registry order. Where a dynamic surface did not expose a stable timestamped response to the ordinary client, the bounded official-domain search result and the complete arXiv v1 snapshot were used only for discovery/date reconciliation. A search result never supports a mechanism claim.

| Source ID | Listing watermark / exact check | Window decision |
| --- | --- | --- |
| `SRC-OPENAI` | Official page dated `2026-08-27`, “Better answers, broader thinking”; page lines 13–20 and 36–65 expose the experiment summary and linked paper | one day-precision context family retained; no AI-system mechanism claim |
| `SRC-ANTHROPIC` | Official research listing bounded search; latest visible dated item remained below the window | no hit |
| `SRC-GOOGLE-AI` | DeepMind and Google Research endpoints plus exact arXiv identities; Google-linked manuscripts in the OAI snapshot were reconciled by arXiv v1 time | no separate organization-only event |
| `SRC-META-AI` | Official research listing bounded search, then arXiv identity reconciliation | no hit |
| `SRC-XAI` | Official news listing bounded search; no dated technical event in the interval | no hit |
| `SRC-MISTRAL` | Official news listing bounded search; no dated model, report or artifact in the interval | no hit |
| `SRC-QWEN` | Official Qwen listing and linked arXiv identities | no separate organization-only event |
| `SRC-DEEPSEEK` | Official surface and arXiv identity reconciliation | no hit |
| `SRC-MOONSHOT` | Kimi blog and MoonshotAI organization/release surfaces | no hit |
| `SRC-ZAI` | documentation index, release-note route and organization surface | no hit |
| `SRC-MINIMAX` | official listing serialized publication dates | no hit |
| `SRC-BYTEDANCE-SEED` | official publication surface and exact arXiv identity reconciliation | no separate organization-only event |
| `SRC-BAIDU-ERNIE` | official publication card inventory | no hit |
| `SRC-TENCENT-HUNYUAN` | organization repositories/releases; repository update time was not treated as first-public manuscript time | no new release/report family |
| `SRC-HUAWEI-NOAH` | official dated news/research surface | no hit |
| `SRC-SHLAB` | official research/news surface and arXiv identity reconciliation | no separate organization-only event |
| `SRC-STEPFUN` | official research card inventory | no hit |
| `SRC-XIAOMI-MIMO` | official publication listing | no hit |
| `SRC-INCLUSION-AI` | official publication/blog listing | no hit |

## Hugging Face Daily Papers

`SRC-HF-PAPERS` was attempted through the dated Daily Papers route, but the requested dated page did not yield a stable retrievable snapshot during this run. It is a registered non-deterministic discovery backstop, so this limitation is recorded as `LIM-20260828-HF` and does not replace or lower the deterministic arXiv closure. No HF recommendation date was used as first-public evidence.

## Claim Boundary

Organization pages prove only their own publication, release or artifact facts. The arXiv OAI and exact-version manuscript evidence owns paper identity, v1 time, method and author experiments. Day-only publication metadata is preserved as day precision and is never fabricated into a time-of-day.
