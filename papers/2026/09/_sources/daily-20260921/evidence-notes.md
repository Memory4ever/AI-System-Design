# Daily 2026-09-21 evidence notes

## Evidence closure matrix

| Source Family | Primary evidence | Method / identity locator | Evaluation locator | Limitation / non-proof | Review |
| --- | --- | --- | --- | --- | --- |
| Qwen-Image-2.1 | [official blog](https://qwen.ai/blog?id=qwen-image-2.1), [official repo](https://github.com/QwenLM/Qwen-Image-2.1) | blog Architecture；repo README Architecture/Model Details；mask/cache implementation | author comparison tables and model examples | no independent reproduction; hardware, batch, concurrency, SLO and uncertainty incomplete | deep complete |
| RecreationWorld | [official repo](https://github.com/QwenLM/RecreationWorld), commit `948e567` | README environment/task construction, explore–implement–verify loop | README frozen reference and programmatic/visual assertions; author report and disclosed scoreboard | no independent reproduction; hidden task bundle, repeat variance and broad cost conditions not disclosed | standard complete |
| MoonEP | [official repo](https://github.com/MoonshotAI/MoonEP), release commit `33327eb` | README dynamic redundant expert planning, fixed `S × K` receive, zero-copy permute, backward ownership | README H20 EP=8 maxvio sweep; release commit kernel/buffer changes | author artifact only; model/precision/multi-node/batch/concurrency/SLO incomplete | deep complete |
| MiMo MCP host state | commits [`e95db7a`](https://github.com/XiaomiMiMo/MiMo-Code/commit/e95db7a80004edfe23617ed2160ff6db8163efef), `db95b68`, `d1a72ba` | full commit explanation and diff: per-name generation, create identity, store/admit/commit/release ordering, progress drain | admission/OAuth/cold-init/stale-status/tool-progress regression suites | repository tests, not production concurrency, server trust or effect correctness | deep complete |
| MiMo session state | commits `05fa8d1`, `30e55a4`, [`1592084`](https://github.com/XiaomiMiMo/MiMo-Code/commit/1592084b2e1fa64dc5a115708d0b5124bb9a3581) | execution-owned orphan sweep, exclusive resume admission, typed error/status preservation and `budgetFor` | session status/resume/retry/containment tests in official diff | default retry budgets are project choices; no live provider, cost, side-effect or long-run acceptance | deep complete |
| MiMo skill roots | [`1a7a747`](https://github.com/XiaomiMiMo/MiMo-Code/commit/1a7a7478f58f8123d5cb5cf5abae688e5599e078) | official commit message, README/spec and discovery implementation | external-root, collision-order and dotted-directory tests | discovery restriction does not prove discovered skill safety/authorization | standard complete |

## Adopted claims and boundaries

### Qwen-Image-2.1

- Adopted: a single-stream DiT can reuse a static condition prefix across denoising steps when mixed-granularity mask and condition identity remain invariant.
- Not adopted: general quality/latency superiority, broad hardware efficiency, or safe reuse across changed prompt/mask/order/resolution/sampler/model revision.
- Failure/fallback: stale or mis-keyed prefix cache corrupts semantics; invalidate and fully recompute condition context per step.

### RecreationWorld

- Adopted: reference-validated executable artifacts plus programmatic/visual assertions provide a reproducible behavior target across multiple computer platforms.
- Not adopted: source similarity as success, universal task completeness, or leaderboard generalization beyond disclosed harness/cost assumptions.
- Failure/fallback: replay the reference and inspect assertion coverage; add human/visual review where post-state is not executable.

### MoonEP

- Adopted: proactive redundant-expert prefetch and fixed receiver shapes form a distinct EP imbalance branch with home-rank parameter/gradient authority.
- Not adopted: universal throughput/OOM improvement or topology-independent scaling.
- Failure/fallback: redundancy budget, prefetch latency, memory or gradient reduce can dominate; use static EP or reactive overflow spill.

### MiMo Code retained families

- MCP host state: asynchronous connect/auth results must revalidate host generation before publish; commit successor before identity-safe release of predecessor; stale attempts fall back disabled/reconnect.
- Session state: retry consumes typed failure identity and bounded phase-specific budget; session owner alone commits resume/idle/terminal; unknown failure exhausts to observable terminal state.
- Skill roots: discovery roots, scan order, collision and private namespace exclusions are admission inputs; opt in a pinned root/digest rather than recursively trusting all brand directories.

## Benchmark contract summary

| Source Family | Workload | Model | Hardware | Precision | Input/output | Batch/concurrency | SLO/evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-Image-2.1 | text-to-image/editing examples and author comparisons | Qwen-Image-2.1 7B component | Not Disclosed for adopted claim | Not Disclosed | image resolution/examples vary | Not Disclosed | author metrics; no independent uncertainty |
| RecreationWorld | 250 held-out recreation tasks across 5 platforms | multiple agents in author scoreboard | Not Disclosed | N/A | task-specific | Not Disclosed | frozen reference + programmatic/visual assertions |
| MoonEP | EP=8 router imbalance/maxvio sweep | Not Disclosed | H20 | Not Disclosed | hidden/token shape partially disclosed | EP=8; broader concurrency Not Disclosed | author communication measurements; no production SLO |
| MiMo retained families | repository contract/regression tests | project runtime | CI environment Not Disclosed | N/A | test fixtures | Not Disclosed | deterministic repo assertions, not workload benchmark |

No benchmark headline is required for any adopted Books claim. `Not Disclosed` fields therefore constrain external validity rather than blocking the narrow mechanism review.

## Deleted / withdrawn exclusion

`SF-2026-09-21-MIMO-PROVIDER-PROMPT` was present in the author-stage raw record, but the fresh review could not resolve `71d0cba`, `0fa4888`, or full SHA `8a0b4398ba1dcc629a5c40159c863aa4ead1bfbd` from the current official main history. The representative official commit URL returns 404 and Git object fetch returns `not our ref`. Under the research contract this family is not an Evidence-complete candidate and supports no adopted claim or Books decision. Reopen only if the official project republishes a resolvable commit/release with the corresponding diff and tests.
