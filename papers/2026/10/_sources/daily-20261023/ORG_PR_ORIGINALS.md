# 官方 GitHub PR 核心说明原件摘存

拉取时间：2026-10-23。以下为GitHub API原始title/body（去重复中文details及无关bot footer），非独立实验。

## Tencent-Hunyuan/Hy-Memory PR132

API: https://api.github.com/repos/Tencent-Hunyuan/Hy-Memory/pulls/132

created_at: 2026-10-21T08:59:39Z; merged_at: 2026-10-22T07:24:21Z; merge_commit_sha: 6d1d29e16d9ea9d6172e44a6b768e71f444e7ba9

refactor(memhub): move memory authority to SDK

## Scope

- **MemHub Core:** SDK-owned memory/raw authority, fresh target schema, single-layer durable write queue, verified legacy cutover and physical legacy cleanup
- **MemHub CLI / HTTP:** SDK-native OpenAI messages write API, SDK memory CRUD, write status, and assembled user-profile read
- **MemHub Desktop:** run legacy migration and cleanup in the visible startup loading phase
- **SDK dependency:** pinned development release `hy-memory==2.0.5.dev3`; no stable SDK release

## Result

- fresh installs create only the management-plane target schema
- fresh installs do not create Evidence, Governance, Matter, legacy retrieval/session-shadow, or `memory_tasks` tables
- one `memory_write_jobs` row maps to exactly one SDK `add()`; pending rows have no SDK IDs and successful rows retain only request/raw/memory receipts
- legacy pending jobs freeze their full input before cutover; unstarted legacy tasks migrate into deterministic write jobs
- App startup creates and verifies a full management + SDK bundle, resumes the ledger, reconciles, commits SDK authority, then physically drops old live tables
- Matter was unpublished and is removed rather than migrated
- extraction window desired state now lives in `config.json`
- CLI `write submit` accepts OpenAI text messages; `profile` calls SDK `get_user_profile()`; memory list/show/update/delete use v2 SDK-backed endpoints
- retired upload/processing/extraction and Governance revision/Evidence command surfaces are no longer advertised

## Verification

- Core PR gate: **5047 passed**, 0 failed
- CLI: **576 passed**, 0 failed
- Runtime Control: **849 passed**, 0 failed
- TypeScript typecheck: passed
- Core mypy: **207 source files**, 0 issues
- Ruff / Biome / workspace builds: passed
- full workspace gate: passed

## Migration safety

See `memhub/docs/contracts/sdk-data-plane-migration-v1.md`. The verified bundle is the rollback/audit artifact; legacy plaintext authority is not retained in the live database after cutover.

Made with [Cursor](https://cursor.com)


## Tencent-Hunyuan/Hy-Memory PR143

API: https://api.github.com/repos/Tencent-Hunyuan/Hy-Memory/pulls/143

created_at: 2026-10-22T08:43:55Z; merged_at: 2026-10-22T08:51:15Z; merge_commit_sha: de4292ed4e8a139815c4276fa1d3a6c11bafbd91

feat(hermes): add managed native prefetch provider

## Summary

- add the native Python `hy_memory` MemoryProvider from #28 as a MemHub-managed Hermes integration, packaged with Host Bridge and installed by the existing one-click transaction
- route managed recall through the authorized MemHub Broker `/context` path instead of the unauthenticated bare Hy HTTP server
- use Hermes `queue_prefetch/prefetch` lifecycle for automatic recall, consuming the previous turn's warmed result without blocking or requiring identical adjacent queries
- deduplicate opaque `memory_id` values per Hermes session, persist only hashed-session→ID state across restart, and reset the target session on rewind/reset
- prevent memory recursion: managed provider is read-only, automatic capture is disabled, injected blocks use the reserved `memhub_memory_context` boundary, and the Hermes source adapter strips persisted injected blocks
- install `memory.provider: hy_memory` when the user clicks Connect, journal and restore the previous provider on managed disconnect, and fail safely if MemHub is deleted without cleanup

## Contribution integration

Refs #28. This branch directly preserves #28's commit history and its native provider, bounded HTTP transport, TLS/CA handling, response framing tests, and operator-managed direct mode. The maintainer changes add the requested hook-first product behavior, session deduplication, recursion prevention, Broker authorization, and MemHub installation lifecycle.

Co-authored-by: kindong <727777477@qq.com>

## Focused local verification

- Hermes provider suite: 113 passed before the managed integration slice; final hook/Broker/dedupe/capture selections passed
- Host Bridge Hermes/YAML/install/credential/wording selections: 95 passed
- Core Hermes recursion-filter selection: 3 passed
- Host Bridge, Runtime Control, and Desktop typechecks passed
- Ruff, targeted Biome formatting, packaged provider build/cmp, and `git diff --check` passed

The complete clean Linux gate is delegated to GitHub CI.

## Tencent-Hunyuan/Hy-Memory PR146

API: https://api.github.com/repos/Tencent-Hunyuan/Hy-Memory/pulls/146

created_at: 2026-10-22T12:31:45Z; merged_at: 2026-10-22T12:49:24Z; merge_commit_sha: 26c33ee40fbbfa9ca7b2be09c01356629b2b75de

refactor(sdk): internalize legacy data migration

## Scope

- **Hy Memory SDK Client:** remove migration-only and duplicate raw read methods.
- **MemHub App migration:** make stopped-writer startup migration the isolated privileged data-plane access exception.
- **MemHub HTTP raw history:** keep the existing endpoint, backed by unified `list_memories()`.

## Changes

- Remove public `import_raw` / `async_import_raw`.
- Remove public `import_memory_exact` / `async_import_memory_exact`.
- Remove public `get_raw` / `async_get_raw` and `list_raw` / `async_list_raw`.
- Remove `include_raw` from `get()`; exact lookup returns the actual matched layer (`raw_id -> l1_raw`, fact ID -> fact layer).
- Make explicit raw listing use `list_memories(layers=[\"l1_raw\"])`; add generic session/source list filters and include the original source in list/get results. Backend provenance is now `retrieval_source` instead of overwriting `source` with `vdb`/`graph`.
- Move exact legacy writes and raw inventory access into `hy_sdk_migration.py`, which directly accesses SDK stores only while Runtime writers are stopped. Semantic migration writes both vector and graph projections.
- Backfill a complete same-filesystem staging copy, preserving SDK-only records. Cutover atomically swaps SDK roots, rolls back on pre-commit failure, and recovers interrupted swaps on restart.
- Refuse to start Runtime while startup migration is deferred or blocked.
- Keep `get_write_outcome()` public because it is required by the normal durable write queue, not migration.
- Keep private SDK access forbidden everywhere except existing Graph projection and this exact offline migration module.

Historical MemHub versions already wrote to the SDK and stored `hy_memory_id` mappings, so migration still validates existing records internally. This prevents duplicate raw/memory rows without creating public Client APIs.

## Verification

- Focused SDK contracts: 42 passed.
- Core staging/migration/CLI/architecture target: 50 passed.
- Earlier full affected Core target: 230 passed.
- Desktop suite: 473 passed; TypeScript typecheck passed.
- SDK and Core Ruff checks passed.
- Core test index remains current (322 files).

## QwenLM/qwen-code PR15104

API: https://api.github.com/repos/QwenLM/qwen-code/pulls/15104

created_at: 2026-10-21T18:27:02Z; merged_at: 2026-10-22T00:09:13Z; merge_commit_sha: d03b3116dae52589210a50f84ac099876f75326c

feat(managed-agent): Add durable manual context compression

## What this PR does

Adds idle-only manual context compression for Workspace-bound public Managed Sessions through the public API and the existing WebShell context-usage popover. Compression is a durable operation with actor-scoped idempotency, its own compaction revision, native capability negotiation and recovery barriers. It reuses Core compression without creating a user Turn, preserves the audit transcript, and restores the compressed model history for later Turns and reopened Sessions.

The implementation persists chunked candidates before PostCompact, commits the compaction and its terminal maintenance result atomically, fences stale writers, and reconciles uncertain submissions from their original evidence. Automatic compression shares the persisted history restoration path, including pending input and tool-result recovery. The browser resumes the original operation after reload and shows context usage as unknown until the next primary-model observation.

## Why it's needed

Managed Sessions currently provide no manual compression action, and their model-input projection does not apply persisted compression checkpoints. An entry point alone would therefore lose the compression on the next Turn. This change provides the action together with durable model-history restoration and recovery, while keeping approval policies and the Workspace installation revision independent.

## Reviewer Test Plan

### How to verify

1. Open a Workspace-bound public Session as an OPERATOR or OWNER on a compatible Harness. Compress from the context-usage popover while idle; expect HTTP 202 and a queryable context_compression operation, with no new user Turn. Unsupported Harnesses and unauthorized callers must not expose an enabled WebShell action.
2. Race compression with a queued or running Turn, pending approval, unsettled Hook, model/CWD change or close. Expect session_context_busy for conflicts. Retry the original actor/session/key and body to obtain the original operation; changing the body must return idempotency_conflict, and a new request with a stale revision must be refused.
3. Compress a long history, send another Turn, reopen the Session and exercise writer recovery. Confirm that model requests use the compressed history, tool calls and results remain paired, and the original chat records remain readable. Cover snapshots larger than 64 KiB and NOOP outcomes.
4. Reload during compression. Confirm that the original key/operation is resumed without a second POST, conflicting controls stay disabled, the draft survives, and completion enables controls while displaying context usage as unknown until a real primary-model observation.
5. Exercise interruption before and after candidate persistence, PostCompact and final commit. A fenced old summary must not publish a candidate, dispatch a Hook or commit history; uncertain acceptance and unknown Hooks must reconcile existing evidence, and a duplicate terminal receipt must not erase a later usage observation.

Local validation passed root build/typecheck/bundle, focused Core/CLI/WebShell checks, the full Managed Agent Server and Java SDK verification, MySQL concurrency tests and Hosted process-fault regressions. A separate PR comment records counts and validation boundaries.

### Evidence (Before & After)

| Scenario | Before | After / observed evidence |
| --- | --- | --- |
| Managed manual action | No Managed compression endpoint or supported WebShell action. | Public and WebShell compression admission contracts pass; browser smoke exposes the existing popover action at 1280 px and 390 px. |
| Reload during compression | No durable manual operation to resume. | Browser smoke records one compression POST across reload, no Turn submission, a retained draft and enabled controls after settlement. |
| Model history after compression and reopen | The summarizer receives the original history containing RAW_BEFORE_COMPRESSION. | Actual Hosted Config/Core plus loopback OpenAI HTTP integration observes MANUAL_MEMORY_BLUE in the next primary-model request and no RAW_BEFORE_COMPRESSION; both original audit records remain. |
| Usage after completion | Previously observed occupancy describes the old model context. | Browser and persistence checks show unknown occupancy after compaction and preserve later real-model observations across receipt replay. |

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  | ✅ tested |
| 🪟 Windows | ⚠️ not tested |
|  🐧 Linux  | ⚠️ not tested |

### Environment (optional)

macOS arm64, Node.js 24.19.0, JDK 21.0.8, Maven 3.9.14, disposable MySQL 8.4.11 and Chromium. Model-facing verification uses deterministic providers or a loopback OpenAI HTTP fixture with the actual Hosted configuration and Core engine; no paid upstream model was called.

## Risk & Scope

- Main risk or tradeoff: interrupted pure summarization may be attempted again after writer fencing, so model billing may repeat while history commits at most once. Unknown Hook execution remains recovery_blocked until original execution evidence resolves it. Concurrency and durable history recovery are the main review focus.
- Not validated / out of scope: production-model Java HTTP → SDK → Harness deployment acceptance, local Windows/Linux execution, custom compression instructions, busy-session compression, queued compression and new slash-command dispatch. The process-fault profile is regression coverage, not a new live public compression acceptance test.
- Breaking changes / migration notes: additive API contract 1.81.0, context-compression/1 Harness capability and incremental schema V16; published baseline migrations are unchanged. Deploy schema and Java/Broker readers first, then Harness writers, then WebShell. Stop new admission and settle accepted operations before rollback.

The synchronized design documents cover decisions, constraints, acceptance criteria and deployment boundaries: [English design](https://github.com/QwenLM/qwen-code/blob/codex/managed-context-compression-15080/docs/design/2026-10-22-managed-context-compression.md) and [中文设计](https://github.com/QwenLM/qwen-code/blob/codex/managed-context-compression-15080/docs/design/2026-10-22-managed-context-compression.zh-CN.md).

## Linked Issues

Closes #15080



## QwenLM/qwen-code PR15119

API: https://api.github.com/repos/QwenLM/qwen-code/pulls/15119

created_at: 2026-10-21T19:36:49Z; merged_at: 2026-10-22T14:07:47Z; merge_commit_sha: 4ee2bb4e4744c2f688401eb4f00cf5791bd1e9eb

feat(managed-agent): manage MCP servers without recreating sessions

## What this PR does

Let an authorized user add, change, remove, enable, disable, reload and restart published MCP servers in an existing Managed Session while continuing to use its ordinary files and Shell tools. The WebShell manager reuses the daemon's server cards and metadata views, with Managed commands operating on the selected Session's original Runtime owner.

Each explicit change records a Session-local MCP settings revision. The original AgentDefinition revision, Skills and approval policy stay pinned. Add and edit select an exact revision and digest from the Runtime's private published inventory; executable recipes and credentials never enter the public API or browser storage. Unknown effects retain their original operation identity and require confirmation before another change.

## Why it's needed

Managed currently exposes a saved MCP catalog but cannot change a Session's server selection or reconnect a server through the public interface. Using daemon commands would target a different execution environment. This provides the missing management path without replacing the Session or its conversation.

## Reviewer Test Plan

### How to verify

1. Open an ordinary local Managed Session with Workspace execution permission. Before sending its first message, open Manage MCP and add a published server. Confirm that the same Session subsequently exposes files, Shell and that server's tools.
2. Exercise change-definition, disable, enable, reload, restart and remove. Confirm that disabled or removed tools disappear from later model requests, restarting one server leaves the other connection and worker running, and conversation identity stays unchanged.
3. Continue using ordinary tools, backups and rewind. Restart the Harness and confirm that settings survive normal Session continuation. A management query alone must refuse cold recovery rather than start a model request or pay resource-cleanup debt.
4. Confirm stale revisions, an unauthorized actor, Plan mode, unsupported profiles and active work cannot mutate settings. Retrying an unconfirmed command must query and resume the same original operation; switching Session or provider must discard late results.
5. Inspect tool schemas, resource metadata and prompt metadata at desktop and mobile widths. Check that the existing daemon manager still uses its own execution environment.

### Evidence (Before & After)

Before: Managed's catalog is read-only. A global `qwen` 0.25.2 Hosted capability and route probe confirms that the new management surface is absent.

After: local validation uses the built CLI, actual Java control plane and Broker, disposable MySQL, real stdio MCP processes and a controlled model. The separate E2E comment records operation, browser, persistence, recovery and cleanup results, with fixture evidence distinguished from platform acceptance.

### Tested on

| OS | Status |
| :---: | :--- |
| 🍏 macOS | Local process stack, MySQL and Chromium; detailed results in the E2E comment |
| 🪟 Windows | ⚠️ Not tested locally |
| 🐧 Linux | ⚠️ Runtime/cgroup acceptance not tested locally |

### Environment

Node 22, JDK 21, MySQL 8.4 and Chromium at 1280px and 390px, using isolated test resources. Existing preview services are untouched.

## Risk & Scope

- This crosses the Session journal, Java/SDK, Broker, Runtime and WebShell boundaries; deploy matching artifacts and enable the exact supported lifecycle profile and capability together.
- Management reattachment reads an already resident Session without implicitly recovering execution. After a Harness restart, continue or recover the Session through its normal execution flow before managing MCP. A fresh empty Session can initialize through management without submitting a Turn.
- This supports ordinary local `shell/1` and the existing MCP profile. Private recipe publication, resource bodies, prompt expansion, OAuth authoring, SSH, CSI, newer Workspace profiles, real upstream models and the complete cross-platform fault matrix are outside this change or unqualified locally.
- Existing logs without management settings keep their admission pins. Session settings use an already registered journal domain; no definition rewrite or schema migration is introduced. Plan stays unavailable after MCP management history, including after removing every server.

Designs: [ordinary tools and MCP (English)](https://github.com/QwenLM/qwen-code/blob/1ce997a561c540b0623a224725b2c7e4537552cf/docs/design/2026-10-21-managed-mcp-management-reuse.md), [中文](https://github.com/QwenLM/qwen-code/blob/1ce997a561c540b0623a224725b2c7e4537552cf/docs/design/2026-10-21-managed-mcp-management-reuse.zh-CN.md); [Session management (English)](https://github.com/QwenLM/qwen-code/blob/1ce997a561c540b0623a224725b2c7e4537552cf/docs/design/2026-10-22-managed-session-mcp-management.md), [中文](https://github.com/QwenLM/qwen-code/blob/1ce997a561c540b0623a224725b2c7e4537552cf/docs/design/2026-10-22-managed-session-mcp-management.zh-CN.md). Both language pairs are synchronized.

## Linked Issues

Closes #15079



## QwenLM/qwen-code PR14986

API: https://api.github.com/repos/QwenLM/qwen-code/pulls/14986

created_at: 2026-10-21T03:51:34Z; merged_at: 2026-10-22T14:42:11Z; merge_commit_sha: 1477a3f8a2eae18eb156fd5550f99cf2db72a967

fix(mods): exclude native waits from root execution budget

## What this PR does

P02b changes the 60-second Mod tool-root limit to cumulative charged time on both the host and worker. Actual native execution and approval waits are excluded only while the trusted bridge confirms that guest work is idle. Guest checks, continuations, jobs and log observers remain charged; starting another attempt never refreshes the allowance. Root/phase identities reject stale activity, and cancellation retains its independent 250ms worker watchdog.

The required cancellation fixture also exposed an existing Ink result-pairing bug: Esc stopped the native process and recorded cancellation, but the next turn received a missing-result placeholder. A minimal correction now pairs the finalized real responses for ordinary cancelled turns, including mixed success/cancelled batches. Review also identified a completion crossing `/clear` during asynchronous result persistence. Completion now revalidates the original session and chat before bookkeeping/recording, releases stale local Goal state, and skips already-paired responses. The user documentation and existing no-AK E2E matrix describe and exercise the new behavior.

## Why it's needed

Both outer clocks previously counted native waiting as Mod execution. A legitimate long-running tool or an unanswered approval could therefore be cancelled around 60 seconds even when the plugin itself was idle. Pausing only one clock or increasing the limit would leave the underlying accounting and cancellation boundaries incorrect.

## Reviewer Test Plan

### How to verify

- With experimental Mods enabled and a middleware that awaits the native tool, leave an approval open for at least 65 seconds. It should remain actionable without executing anything; approving once should execute once and pair one logical result.
- Run a foreground native tool for at least 66 seconds. At 65 seconds it should still be pending with no completed result; after completion, the next ordinary turn and clean exit should work in Ink and strict OpenTUI. Headless stream-json should preserve the same execution facts.
- Cancel during approval and native execution, then try a late approval or the next turn. Cancellation should prevent further side effects, stop the exact native process, and preserve the real result. An explicit native timeout must still take effect independently of the Mod budget.
- Check that queued work and guest checks/jobs/observers cannot grant free execution, stale phases cannot resume an expired root, and the cancellation watchdog remains active during an excluded wait. Load, command, end, disabled and command-only behavior should retain their existing limits and admission rules.

### Evidence (Before & After)

Before: the installed 0.25.3 CLI cancelled the enabled-Mod native oracle at 60059.7ms; its disabled-Mod control completed at 66001.9ms. A separate frozen-base Ink build lost the approval around 61 seconds and reproduced the cancelled-result placeholder. These are distinct, explicitly recorded baselines.

After: The original budget candidate `efc5928d8b` passed all 41 artifact cases on the first attempt (16 Ink + 9 headless; 16 strict OpenTUI), with zero retries. Approval remained actionable after 65.098s / 65.077s. Foreground native execution completed at 66.011s / 66.007s / 66.028s for Ink / OpenTUI / headless, with no premature result at the 65-second sample. Native timeouts, cancellation, result pairing, NEXT and exit checks passed, and artifact hashes were unchanged.

Repair head `63c4956b2014994050e29883ec04f061f0fd8d50`: Final-head Ink terminal regression passed 16/16 on the first attempt with zero retries: approval remained actionable after 65.063s, foreground native execution lasted 66.029s in the same process, and the 65s sample had no settled/completed/paired result. Native timeout, cancellation, result/record pairing, NEXT and natural exit passed. The independent conforming probe was red on the original hook and green on the final source, with actual 220000-byte persistence in both and no old result in the replacement chat/recorder after repair. Independent final-bundle Ink cancellation also passed; all head/artifact hashes were unchanged.

Validation on the repair head: complete build, typecheck and bundle; 310 stream-hook cases, 29 clear/scheduler boundary cases, and changed-file ESLint/Prettier. The original budget head also passed 130 core cases, 159 CLI boundary cases and one relocated-worker bundle contract case; those unchanged-component results retain their original head identity. The real-worker unit cases verify activity transitions; cumulative expiry uses deterministic ledger/protocol tests, with real long waits checked separately by E2E. A separate test engineer reproduced the original issue and independently verified the long-wait candidate and final Ink cancellation. Final hashes and commands are in the separate E2E report comment. Local validation and source review do not imply hosted CI success or formal PR acceptance.

### Tested on

| OS | Status |
| :-- | :-- |
| 🍏 macOS | ✅ 26.6.2, arm64 |
| 🪟 Windows | ⚠️ Not tested locally |
| 🐧 Linux | ⚠️ Not tested locally |

### Environment (optional)

The Ink/headless matrix used Node 25.9.0; strict OpenTUI used Bun 1.3.13; separate test-engineer checks used Node 24.14.1; packaged CLI with isolated HOME/workspace, fake provider, real native child processes, sandbox disabled. No live model service was used.

## Risk & Scope

- Main risk or tradeoff: host/worker activity accounting and check/result transitions must agree. Identity checks and conservative charging cover unknown or stale states; native process cleanup can take longer than the worker's 250ms cancellation watchdog.
- Not validated / out of scope: local Windows/Linux runtime, live model services, P02c APIs, hosted Mods and wider cancellation/attachment refactors. The experimental feature remains opt-in.
- Breaking changes / migration notes: no public API or configuration change. Tool-native timeouts and permissions still apply; native waits no longer consume the Mod root allowance. Load/command continuous limits, end cleanup and own/catch budgets retain their policies.

## Linked Issues

Related to #13749 (P02b slice; does not close the umbrella issue).



## QwenLM/qwen-code PR15053

API: https://api.github.com/repos/QwenLM/qwen-code/pulls/15053

created_at: 2026-10-21T12:19:25Z; merged_at: 2026-10-22T13:09:35Z; merge_commit_sha: e39319881e7f59c58dd8464be63fadfe3fc16bbf

fix(core): make Anthropic global cache scope opt-in on every base URL

## What this PR does

Makes Anthropic's cross-session ("global") prompt-cache scope opt-in for every base URL, `api.anthropic.com` included. By default a request now carries only the standard per-session cache breakpoints, and prompt caching stays on. `generationConfig.forceGlobalCacheScope: true` still turns the global scope and its matching beta header back on, and `false` or unset now genuinely means off.

## Why it's needed

Against the native Anthropic API, any request carrying two or more tools was rejected on the first prompt of every session with a 400 `invalid_request_error`. Two or more tools is every real session, so this made the Anthropic provider unusable whenever caching was on — and caching is on by default.

The request body places one cache breakpoint on the last tool and one on the static prefix of the system prompt, while deliberately leaving the volatile system suffix and the trailing user message per-session: those change every turn or every session, so a global-scope entry there would churn cache for no hits. The API rejects that mixture in its own words, quoted by the reporter in the linked issue from a live replay against `claude-haiku-5-5`:

> A block with `scope: "global"` was found after content with a narrower cache scope. Note that tool definitions render before `system` blocks, so `scope: "global"` on `system[0]` is not a true prefix when tools are present. Remove `scope: "global"` from the non-prefix block, or ensure all preceding content also uses `scope: "global"`.

Taking the second branch — ensure all preceding content is also global — means giving every tool its own global breakpoint, and a request is capped at four cache breakpoints. The reporter's replay matrix lands on exactly that: global scope on every tool is accepted, and "what it needs is scope global on every tool, which is where the 4-breakpoint cap bites". So global scope is not reachable for a normal agent request, and having it on by default turned that into a hard failure rather than a cache miss. This PR drops the native-base-URL clause from the gate, so the default is the per-session shape everywhere and the requests succeed. `forceGlobalCacheScope` remains as the explicit escape hatch for backends whose validation differs and that forward the beta.

The precise acceptance rule is subtler than a one-line summary, and this PR deliberately does not depend on resolving it. The reporter's matrix contains shapes where an unmarked tool list precedes a global block and is accepted, and shapes where the same list is rejected depending on what follows it. What the fix rests on is the single shape confirmed twice against the live API — session scope everywhere returns `200, cache written` — which is exactly what the default now produces.

Worth flagging for maintainer awareness: this reverses the native default that #4020 introduced. That PR's description said it kept the direct `api.anthropic.com` path on its existing behavior while enabling cross-session caching, and it did the opposite. The cross-session hit-rate gain it cited was never measured and could not have been realized, since native requests carrying tools were failing outright.

## Reviewer Test Plan

### How to verify

The behavior to confirm is the outgoing request body, not any UI surface:

- With an Anthropic-native base URL, caching on (the default) and two or more tools, no cache breakpoint anywhere in the body carries a `scope` field, and the `prompt-caching-scope-2026-01-05` beta header is not sent. The breakpoints themselves are still present with the per-session shape on the last tool, the system prompt, and the trailing user message — so prompt caching keeps working and only cross-session reuse is given up.
- The same request under `generationConfig.forceGlobalCacheScope: true` puts the global scope back on the static system prefix and the last tool, and ships the beta header. That opt-in path is unchanged by this PR.
- A non-Anthropic base URL without the opt-in behaves exactly as before: per-session shape, no beta header.
- The system-prompt split at the recorded static prefix still produces two blocks with one breakpoint each; both are now per-session by default.

**Real-API verification is not included in this PR.** This machine has no Anthropic credential and no route to `api.anthropic.com`, so the wire shape is pinned by unit tests rather than by a replay. The reporter has offered to test a fix against the live endpoint and has been asked in the issue thread; that confirmation is the missing piece of evidence.

### Evidence (Before & After)

N/A — there is no TUI, Web UI or Web Shell surface to this change; it is the shape of an outgoing HTTP request body. The observable evidence is the request body asserted in the unit tests, plus the 400 in the linked issue. Locally:

```
$ npx vitest run src/core/anthropicContentGenerator/
 Test Files  3 passed (3)
      Tests  331 passed (331)
```

The regression test added here pins the reporter's repro shape specifically: two tools on a native base URL, asserting no `scope` field survives anywhere in the assembled body. A single tool was the one shape the API accepted, which is why the test uses two — a one-tool test would have passed both before and after this change and proven nothing. This closes the blind spot raised in the issue thread, where the existing converter coverage marks one tool and is therefore structurally unable to see the ordering violation.

Eleven existing assertions pinned the old native default and were updated. Where a test's real subject was something else (beta-header composition on the streaming path, the hot `enableCacheControl` flip, the cache-scope beta's body-scan gate), the global scope is now enabled through the explicit opt-in so the assertion keeps its original signal instead of being deleted. One of them — "omits the extended-cache-ttl beta when retention is unset" — would have degraded into a vacuous pass once the header disappeared entirely, so it now opts in and asserts the cache-scope beta is present while the TTL beta is absent.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  |   ⚠️   |
| 🪟 Windows |   ⚠️   |
|  🐧 Linux  |   ✅   |

Linux: unit tests and lint. The change has no platform-specific code path.

### Environment

Unit tests only (`npx vitest run` in `packages/core`). No live model calls.

## Risk & Scope

- Main risk or tradeoff: Anthropic-native users give up cross-session cache reuse. That reuse was never being realized — the requests failed — so the practical change is from a guaranteed 400 to working per-session caching. If a future API revision accepts a mixed shape, re-enabling the default is a one-clause change to the gate.
- Not validated / out of scope: replay against a live `api.anthropic.com` endpoint (no credential here), and the behavior of the opt-in path against a real backend. Also out of scope: the "all-or-nothing global" variant discussed in the issue thread (mark every tool global and drop the narrower breakpoints). The reporter's own analysis puts it out of reach of the four-breakpoint cap for a realistic tool list, so it is not attempted here; the opt-in keeps emitting the current mixed shape, which a strict backend may still reject.
- Breaking changes / migration notes: none. The setting keeps its name and its `false` default. Only the generated settings schema description changes, to stop documenting native URLs as implicitly global; the generated file is updated in this PR so the schema-sync check stays green.

## Linked Issues

Fixes #15039

Related, not closed: #6642, #6643 (the opt-in this PR keeps), #4020 (the PR whose native default this reverses).

Coordination: @holny claimed this issue in the thread 18 minutes before this PR was opened, with substantially the same plan, and that claim was missed before pushing. Flagged in the issue thread — review, correction, or taking it over is welcome.



## QwenLM/qwen-code PR15069

API: https://api.github.com/repos/QwenLM/qwen-code/pulls/15069

created_at: 2026-10-21T14:17:49Z; merged_at: 2026-10-22T12:21:11Z; merge_commit_sha: 74c67c9e94f09b80b5f47df8f8ab216c9ebe6a14

feat(core): gate scheduled tasks on a shell command run outside the model

## What this PR does

A scheduled task can now carry a **gate**: a shell command the scheduler runs at each fire, outside the model, before the prompt reaches the session. If the command prints nothing and exits 0, the fire is skipped — no model turn, no queue entry, nothing in the transcript. If it prints output, the fire is delivered with the output appended after the prompt and marked as data produced by the command. A command that fails, cannot start or runs longer than 60 seconds is reported once per streak and then counted silently until it succeeds again; `cron_list` shows the gate and its recent outcomes.

The gate runs inside the scheduler, at the one point every fire kind passes before the consumer callback, so the interactive TUI, ACP sessions, headless runs and daemon-bound sessions share a single path and needed no delivery changes. Each session's scheduler runs its gates with that session's working directory, environment, sandbox policy and permission state through the same shell path the Monitor tool uses. One gate runs at a time per task; a slot that comes due while the previous run is still in flight is consumed and the probe runs again at the next slot. Deleting or disabling a task, or stopping the scheduler, aborts a running gate so a late result delivers nothing.

A gate is approved where it is proposed and checked again where it runs. When the model proposes one through `cron_create`, the confirmation is the exec dialog Monitor shows for the same command, with `Monitor(...)` rules, so "always allow" saves a rule that also covers the scheduler after a restart; the auto-mode classifier sees the command; a bare `cron_create` allow rule saved before this change does not cover a gate on its own. At fire time the gate runs when the session is in auto or yolo mode, when a saved `Monitor(...)`/`Bash(...)` rule or the read-only check allows the command, or when it was confirmed in this process; otherwise the fire reports the rule to add instead of running the command. Gate output is sanitized like Monitor output and its wrapper tags are added to the defanged envelope list.

Durable tasks persist the gate and a status summary. Quiet fires are not booked in the run ring (a one-minute gate would flush it in twenty minutes); delivered and reported fires are. The writer mirrors the gate into the legacy `condition` field as a downgrade fuse: an older binary ignores `gate` and would fire the task unconditionally, but it fails closed on a non-empty `condition`, so it withholds the task with its existing "recreate it" notice. This version treats `condition` as legacy only when no `gate` is present.

One related fix rides along: the TUI now passes an explicit non-shell intent when it drains a cron fire, so a fire that lands while the composer is in `!` mode is never executed as a shell command.

This is step 1 of the event-driven PR watch discussed in #15056: the probes (`qwen autofix-pr snapshot --gate`, continuing #15057, and a repository-level probe for opened and pushed PRs) and the skills come next. The daemon REST routes, the current-session creator, the `scheduledTaskGate` capability and the Web Shell form are a follow-up PR; a gate for managed automations is a separate design (they never touch the scheduler). The bilingual design is in `docs/design/2026-10-21-scheduled-task-gate.md`.

## Why it's needed

Watching a pull request today means `/loop` or a plain scheduled prompt: the model polls on a timer, and every fire is a model turn whether or not anything changed. The default 30-minute cadence is too slow for CI and review traffic; a 5-minute cadence fills the conversation with turns that report nothing. GitHub cannot push to most developer machines and sends no webhook at all for merge-conflict transitions, so polling has to stay — but it has to run outside the model, and the model should only be woken when the check found something. A gate makes a one- or two-minute cadence affordable: a quiet poll costs one process spawn and nothing else.

## Reviewer Test Plan

### How to verify

1. In an interactive session, with a script in the project that prints `event: comment` only when a file `events` exists and then removes it, ask for a task every minute that runs the script as a gate and summarizes the events when it prints. Expect the `cron_create` confirmation to be the exec dialog showing the script with a `Monitor(...)` rule; approve once. With `events` absent for a few minutes, expect no model request, no `Cron:` line and `cron_list` showing the gate with `quiet ×N`.
2. Create `events`. Expect one `Cron:` line within a slot, one model request whose text starts with the task prompt and contains a `<gate-output>` block with `event: comment`, and `cron_list` showing `last delivered`.
3. Make the script exit 1 with something on stderr. Expect one notice that names exit code 1 and the stderr tail, no further notices on the next slots, and `cron_list` counting the consecutive failures; restore the script and expect quiet fires again.
4. Switch the composer to `!` mode across a delivering slot. Expect the fire to reach the model, not run as a shell command.
5. Create the task with `durable: true`, restart the CLI in the same workspace. Expect `cron_list` to show the gate and its status, a delivering slot to wake the session, and the task in `~/.qwen/tmp/<project-hash>/scheduled_tasks.json` to carry `gate`, `gateStatus` and a `condition` equal to the gate. Run an older build in the same workspace and expect it to warn that the task carries a legacy precondition and will not fire.
6. In default mode, add a saved `cron_create` allow rule and ask for a gated task. Expect the tool to refuse with "The gate command was not confirmed" rather than scheduling a command that would run unattended.

### Evidence (Before & After)

Before (global `qwen` 0.25.3): `cron_create` has no `gate` parameter; its schema ends at `sessionMode`, and every fire of a `/loop` or scheduled prompt is a model turn.

After, on this branch:

```
packages/core: tsc --noEmit → ok; packages/cli: tsc --noEmit → exit 0
eslint --max-warnings 0 on every changed file → ok; prettier --check → ok
vitest (core): cron-gate, cronScheduler.gate, cron-create.gate, cronScheduler, cronTasksFile,
  cron-create, cron-list, cron-delete, monitor, monitor.runtime → Test Files 10 passed, Tests 377 passed
vitest (cli): use-llm-stream "recorded shell intent routing" → 4 passed (incl. the new cron case)
npm run build (core) → ok; node import of dist/src/services/cron-gate.js and dist/src/config/config.js → loaded
```

Mutation controls, each run against the real source and restored afterwards:

```
TUI drain without `shellMode: false`   → "routes a cron fire to the model while shell mode is on" fails
delete() no longer aborting the gate   → "delivers nothing when the job is deleted while its gate runs" fails
fuse not written by withTaskGate       → "treats the downgrade fuse as a gate" and "persists a durable gated task with its downgrade fuse" fail
```

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  |   ⚠️   |
| 🪟 Windows |   ⚠️   |
|  🐧 Linux  |   ✅   |

macOS and Windows were not run locally; the gate uses the same shell execution path as the Monitor tool on every platform.

## Risk & Scope

- Main risk or tradeoff: a gate is a shell command that runs unattended, so it is confirmed like a Monitor command when the model proposes it, re-checked against the session's mode and rules at fire time, and blocked rather than run when neither covers it. Gate output is attacker-influenced text placed in the turn; the wrapper marks it as data, tag names are defanged, and the cron path cannot answer a pending permission prompt.
- Not validated / out of scope: the daemon REST routes, the current-session creator (`sessionMode: "current"` with a gate is refused for now), the `scheduledTaskGate` capability and the Web Shell form and "Run now" are a follow-up PR; the probes and skills are steps 2 and 3; managed automations are a separate design. The E2E plan in `.qwen/e2e-tests/2026-10-21-scheduled-task-gate.md` was dry-run against the global CLI for the baseline only.
- Breaking changes / migration notes: none. Tasks without a gate behave as before. A gated durable task read by an older binary is withheld (legacy-precondition notice) rather than run unconditionally.

## Linked Issues

Refs #15056, #15057



## QwenLM/qwen-code PR15131

API: https://api.github.com/repos/QwenLM/qwen-code/pulls/15131

created_at: 2026-10-21T22:08:30Z; merged_at: 2026-10-22T06:06:57Z; merge_commit_sha: 59d21e1c6910221522122699f067f7f7262fb2d3

feat(managed-agent): Safely settle recovery and continue sessions

## What this PR does

Keeps a possibly submitted Managed Workspace Turn under its original recovery/cancellation driver until durable native settlement, continuation readiness and blocking cleanup prove that the same Session can accept another message. Adds a conservative five-state recovery view, read-only queries and original-Turn rechecks, with synchronized public/WebShell contracts and Java SDK support. Retains main's durable manual context compression routes, Session projections and independent send gate; the public API contract is 1.82.0.

WebShell displays the recovery reason and valid actions, gates sending on recovery evidence, preserves the original cancellation key/operation across refreshes, and offers an editable text handoff of at most 32 KiB UTF-8 through the existing new-Session form. Handoff preparation never creates or sends a Session automatically.

## Why it's needed

After some post-admission failures, Java previously marked a Turn terminal when cancellation was only acknowledged, while the Harness input could still be running. The UI then treated the missing active Java Turn as permission to send again. Delayed Session-scoped cancellation could also affect the following Turn. Recovery now retains the original identity, replays the real terminal and confirmed output, and keeps unproven outcomes blocked with a usable fallback.

## Reviewer Test Plan

### How to verify

1. Fail recovery after native admission while the original tool is held. Confirm that cancellation ACK/HTTP 202 does not end the Java recovery driver or enable sending; rechecks retain the original Turn, retry budget and execution identity.
2. Let the original input settle, including a coordinator restart between cancellation admission and terminal delivery. Confirm that real output/terminal are projected, cleanup debt remains visible, the tool executes once and the same Session can complete a later Turn. Replay the original cancellation while that later Turn is active and confirm it still completes.
3. Exercise stale owner/generation, old Harness capabilities, corrupt or unreadable evidence, and cold cleanup after a Harness restart. Confirm conservative blocking, no model/tool resubmission, no ordinary-load fallback and no release of a newer owner's resources. A proven pristine initial state must still permit legitimate first-message admission.
4. Refresh during cancellation and check that the original key/operation remains tracked until terminal confirmation. Open the new-Session fallback and confirm authorized source Workspace/cwd/Agent defaults, editable bounded quoted text, exclusion of partial/tool/approval/execution content and no automatic create/send. Existing Workspace admission must still apply.

### Evidence (Before & After)

Before: four assertions against exact main `21337f0e5131` reproduced premature Java termination after cancellation admission; the baseline UI used Java activity alone and generated a new cancellation key for each action. A real-process negative control also showed an old delayed cancellation stopping the following Turn.

After: three real Chromium cases verify evidence-gated sending, reload-safe original cancellation tracking and editable authorized handoff without automatic execution, using a controlled HTTP adapter. The real Java/Harness/Broker/worker fault test retains the original tool exactly once, projects the original native terminal and completes the same Session's following Turn with `FOLLOW_UP_OK` despite replaying the original cancellation while that Turn is active. Browser evidence establishes UI behavior; deterministic model responses establish the exercised execution protocol, not live-model quality.

Verification of the source snapshot committed as `7da1c812cc77`: The complete default non-clean Maven verify passed: 358 classes / 5,306 tests, zero failures or errors, and 18 conditional skips. The original initial-state class passed all 38 cases with zero skips both individually and again in the full run. Both Checkstyle gates reported zero violations; the newly generated SpotBugs analysis XML recorded zero issues, errors or missing classes. Root build, bundle and typecheck passed. Four complete CI configuration test files passed 194 tests with five conditional skips. A real Linux/Node 22.22.1 experiment using the unchanged Core fixture reproduced the transport defect: its 10,054-byte output fills an 8 KiB private pipe and times out at the original 30-second deadline; draining that same process lets it exit successfully in 0.0067 seconds, while file output completes in 0.571 seconds. The test now receives stdout and merged stderr through a JUnit temporary file, retains the deadline and every recovery assertion, and reaps its child on failure. CI's actual pipe capacity was not captured, so the experiment establishes the backpressure mechanism rather than a measured CI kernel setting. Main's existing no-AK membership repair is included through the rebase; no separate TUI changes or blind CI reruns were made.

Earlier feature verification on `2e6eb32d459b`:  root build/bundle/typecheck passed; the corrected core test file passed all 606 tests; WebShell passed 552 tests and Chromium passed seven cases without skips or retries (three recovery, two context compression and two SSH registration). The complete CLI suite passed all six files / 768 tests without skips. The full Hosted profile verify passed again with the newly built bundle: two methods, all nine actual fault windows, zero failures/errors/skips, and clean Checkstyle/SpotBugs. It confirms one original tool execution, a completed following Turn and an ignored delayed original cancellation. The then-current eight lint-gate commits are incorporated; the freshness helper's nine tests pass. Source-tree and integration ESLint, Prettier and diff whitespace checks passed. The first bare local ESLint invocation encountered only 953 diagnostics in 22 untracked Maven target outputs; that failure is preserved. Its source-only rerun excludes `**/target/**`, which excludes no tracked file, and changes no repository lint configuration.

On `2e6eb32d459b`, prior Java results were reused from `9046a3ac8eec` after independently matching all 1,222 tracked Java/POM inputs, 122 dependency JARs and 2,127 compiled outputs: SDK 406 tests with nine conditional skips; complete unit/H2 5,306 tests with 18 conditional skips and zero failures/errors; complete MySQL 8.4 rerun 54 classes / 1,075 tests without failures, errors or skips; and static `mvn verify -DskipTests` with Checkstyle and SpotBugs clean. These are identical-input results, not a second unit/MySQL run. The initial clean verify remains recorded as failed: a 32 MiB + 1 byte fixture exceeded the task server's 64 MiB packet budget before the assertion, while CI requires 128 MiB. Aligning only that isolated fixture made the original method and complete unchanged MySQL roster pass. The static command did not rerun unit tests, and the direct Failsafe retry makes no new coverage claim. These historical SDK/MySQL results are retained separately; the complete unit/H2 suite is rerun for the current test-only repair as recorded above.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  | ✅ tested |
| 🪟 Windows | ⚠️ not tested |
|  🐧 Linux  | ⚠️ product acceptance not tested; fixture transport verified |

### Environment (optional)

macOS; Node 24.12.0 for the root build and Node 22.22.3 for fresh Java verification; JDK 21.0.8; Maven 3.9.14. Current candidate is `7da1c812cc77`, based on `438bcb2a8f7b`. Compared with the previously validated `2e6eb32d459b`, Core, CLI, Java server production/resources, Java SDK and WebShell source trees are identical; this follow-up changes only the initial-journal test's output transport. The original feature commit was replayed unchanged, and main already contains the duplicate-import repair. The fresh CLI bundle is frozen separately. Earlier MySQL/Hosted evidence used disposable native MySQL 8.4.11, performance_schema, CI's 128 MiB packet budget, an isolated V16 catalog and task-only paths; those tests were not rerun for this test-only repair. The earlier task MySQL and Hosted descendants remain stopped and their reports/data are preserved. The Linux experiment reused an existing VM only for four owned fixture children, all reaped; it changed no global pipe settings or deployment. SDK verification skipped local GPG signing. Live GitHub CI state is reported separately from local results.

## Risk & Scope

- Main risk or tradeoff: false-positive readiness, losing cancellation-only intent across a crash, or stale-identity cancellation/cleanup. Missing proof remains blocked; negotiated original-prompt targeting and cleanup-only loading avoid silently falling back to Session-wide execution.
- Not validated / out of scope: Linux physical-Workspace/cgroup acceptance, Windows, optional remote SSH/Kubernetes rigs, cross-host HA, full history cloning, permanent journal repair, MCP/Hooks automatic continuation and signed release artifacts. macOS results do not establish Linux physical-Workspace/cgroup acceptance.
- Breaking changes / migration notes: no database migration, new recovery operation kind or lifecycle status. Recovery fields are optional; older Harness versions without affirmative proof/capabilities remain conservative.

Complete synchronized designs: [English](https://github.com/QwenLM/qwen-code/blob/7da1c812cc772e105da6baf2639bc8fa9b62f7e9/docs/design/2026-10-22-managed-recovery-continuation.md) and [简体中文](https://github.com/QwenLM/qwen-code/blob/7da1c812cc772e105da6baf2639bc8fa9b62f7e9/docs/design/2026-10-22-managed-recovery-continuation.zh-CN.md). E2E plans: [English](https://github.com/QwenLM/qwen-code/blob/7da1c812cc772e105da6baf2639bc8fa9b62f7e9/docs/plans/2026-10-22-managed-recovery-continuation-e2e.md) and [简体中文](https://github.com/QwenLM/qwen-code/blob/7da1c812cc772e105da6baf2639bc8fa9b62f7e9/docs/plans/2026-10-22-managed-recovery-continuation-e2e.zh-CN.md).

## Linked Issues

N/A



## XiaomiMiMo/MiMo-Code PR2703

API: https://api.github.com/repos/XiaomiMiMo/MiMo-Code/pulls/2703

created_at: 2026-10-22T04:56:06Z; merged_at: 2026-10-22T13:43:54Z; merge_commit_sha: e37f2c2d01460df19b31d67b8116d6c66fe33db8

fix(session): retry empty output persistently and persist retry records until the turn succeeds

## Summary

- **Empty output retries persistently.** `SessionRetry.decide` now classifies `InvalidOutputError` (an empty or think-only step) as `kind: "server"`, so it uses the persistent server budget: no retry count, no wall-clock deadline, backoff capped at 30 s, and only user cancellation ends it. Before this change, the bounded `unknown` budget (15-minute deadline from the first failure) was used up by a single upstream attempt that held the stream open for about 1000 s with no content. The turn then failed with "empty output" after only two attempts.
- **Retry records persist until the turn succeeds.** Every retry of an assistant step writes one `retry` part on that assistant message. This covers the request ladder, the stream policy and auto-resume after tools, for the main agent and for every subagent.
  - The part carries `attempt`, `phase`, `scope`, `kind`, `message`, `hostCode` and `next`.
  - It survives retry-safe failure cleanup and the empty-turn reset.
  - It moves with a dropped empty step to the next step of the same user turn.
  - It is removed only at the run loop's success exits (the final answer and the structured-output capture), for the user turns that run completed. Failed, aborted, interrupted and compaction-stopped turns keep their records.
  - Clients can therefore keep showing "reconnecting, attempt N" after `session.status` flips back to busy, after a reload, and for subagents, which never write session status.
- `RetryPart` is reshaped: the unused `error: APIError` field is replaced by the fields above. The SDK is regenerated, and history indexing and export read the new shape. Retry parts are never sent to the model.
- **A newer input supersedes a failing step.** Inbox inputs are claimed only at the top of the run loop, and a persistent retry stays inside one step, so a steer used to wait behind the whole retry chain and was cancelled as `never_ran` when the run ended.
  - A step counts as failing while a retry has been recorded and no attempt has produced output since (`reasoning-start`, `text-start` or `tool-input-start` clears it).
  - The run loop gives each step an `awaitNewInput` effect that completes once the actor's lane holds an accepted, unclaimed input. The retried stream races it: the request-ladder sleep, the stream-policy backoff or the hanging attempt ends immediately, or at the next retry if the input arrived first.
  - The superseded step keeps only its retry record, is marked completed without an error, and `process()` returns `superseded`; the run loop claims the input at its next step in the same run. When the run succeeds, the record and the empty step are removed.
  - Works on subagent lanes too. Compaction steps and max-mode candidates are never superseded.

Design notes: `docs/compose/spec/empty-output-persistent-retry.md` and `docs/compose/spec/retry-record-part.md`.

## Verification

- `bun run typecheck` (repo root): pass.
- `cd packages/cli && bun test test/session/invalid-output-continuation.test.ts test/session/retry.test.ts test/session/structured-output-retry.test.ts test/session/message-v2.test.ts test/history test/actor/spawn.test.ts test/session/title-first-turn.test.ts`: 330 pass, 0 fail, run after rebasing onto current `main`.
- New tests cover:
  - recovery after more empty stops than the old bounded budget allowed;
  - cancellation ending an endless empty-output retry;
  - main and subagent records during a turn and clearing on success;
  - records kept on cancel, on cancel between tool steps, and on bounded exhaustion;
  - clearing for a turn whose recovered attempt was streaming when a prompt was queued, and for a structured-output turn;
  - records surviving a retry-safe mid-stream failure;
  - request-phase provider errors recovering;
  - retry parts staying out of model context;
  - a new input superseding a hanging retried attempt, a request-phase retry wait, the first retry of a step whose input arrived earlier, and a subagent step. These run with one-minute retry delays and finish within seconds.
- Each clearing test was confirmed to fail against the previous rule it guards against.
- `bun test test/inbox test/session test/actor`: 1779 pass. The failures are 5-second timeouts under full-suite load that pass when run alone, plus one `prompt-effect` MCP test that sits at its 5-second limit and involves no retry.
- A full `bun test test/session test/actor test/history test/server test/cli/cmd test/error` run leaves 2 to 4 failures that vary between runs. Each of them passes when run alone. They are cross-file timeouts, and the same files also fail on `main`.

## Scope

- Not changed: the SSE idle timer in `provider.ts` resets on any received byte, so a stream that only sends keep-alive frames is still cut only by the upstream. With this change such an attempt no longer ends the turn; the turn keeps retrying.
- A request that returns empty output every time is retried until the user cancels, and each attempt resends the full context. This is accepted in exchange for not giving up on transient upstream failures.
- `session.status{retry}` and `Session.Event.RetryAttempt` keep their current behavior.



## XiaomiMiMo/MiMo-Code PR2702

API: https://api.github.com/repos/XiaomiMiMo/MiMo-Code/pulls/2702

created_at: 2026-10-21T15:29:46Z; merged_at: 2026-10-22T01:46:14Z; merge_commit_sha: e0636e7b496e09e99bfb1010c7bcdf49f3e9e009

fix(session): append the rebuild boundary after the newest message

### Issue / context (if applicable)

Follow-up to #2691. A checkpoint rebuild inserted its boundary at the writer's watermark (`time.created` = watermark + 1 ms), so the tail between the watermark and the newest message stayed in every later window and was filtered again on every request by `collapseCheckpointTail`. Spec: `docs/compose/spec/lossless-session-db.md` S2.5, S2.6, tasks T6–T11.

### Type of change

Bug fix

### What does this PR do?

The rebuild boundary is appended after the newest message, so its tail leaves the window by position.

- `insertRebuildBoundary` reads the tail from the database at insert time (automatic rebuild sites hold a window read before their current step), digests it up to the last assistant message, and stamps the boundary no earlier than the tail.
- Unanswered user messages at the end of the tail are copied onto the boundary in full (text with metadata, file parts), instead of being quoted under the 2K-token cap.
- Inputs the inbox has accepted or claimed but not delivered stay out of the tail and are recorded as `CheckpointPart.deferredInputs`; one that later ends undelivered is placed after the boundary. The SDK type gains the field.
- `collapseCheckpointTail` applies only to legacy boundaries (boundary created before its `digestUpTo` message); a golden fixture pins the legacy request.
- The checkpoint writer and the runLoop's turn state (resume parent, last user, last assistant, `session.userQuery.pre` text, loop-streak crop anchor) read the window with the tail restored; the model request is built from the window alone. A rebuild after a finished reply ends the turn without another model call.
- `recovery` and resume do not treat a rebuild boundary as a turn.
- The closing reminder after a finished reply is removed; after a tool step it says the outputs are not in context.

### How did you verify your code works?

From `packages/cli`:

- `bun typecheck` PASS; `packages/sdk` `bun run typecheck` PASS.
- Each new test was run on the commit before its change and failed there for the intended reason: `rebuild-legacy-boundary-golden`, `rebuild-boundary-placement` (7 tests), `checkpoint-writer-rebuild-tail`, `auto-overflow-writer-first` (completed turn: 3 model calls), `checkpoint-rebuild-v3` (closing reminder).
- Rebuild, checkpoint, fork, threshold, writer, reminder, prune, resume, recovery and overflow test files plus `server/session-recovery` and the TUI status tests: every file passes when run alone on this branch.
- Full `bun test` on the pre-rebase head: 6131 pass / 77 fail / 41 skip; every failing file passes when run alone except one `prompt-effect` MCP reminder test that exceeds its 5 s limit only under load. These are pre-existing cross-file interferences.

### Screenshots / recordings

N/A

### Checklist

- [x] I have tested my changes locally
- [x] I have not included unrelated changes in this PR


## MiniMax-AI/OpenAgentCore PR819

API: https://api.github.com/repos/MiniMax-AI/OpenAgentCore/pulls/819

created_at: 2026-10-22T10:58:40Z; merged_at: 2026-10-22T11:04:25Z; merge_commit_sha: 01a041c6e68752f39a155af7acb405b441091be6

Cold-replace a checkpoint that cannot be restored

A microsandbox resume that failed before native restoration (missing or damaged snapshot, failed qualification, or a helper that cannot read the snapshot format) left its durable restore admission open. Every later attempt returned `unconfirmed`, so the allocation stayed in `restoring` until retention expiry, and the Session's pending input waited until its public deadline. Seen on mx on 2026-10-22.

The Core–Sandbox Provider protocol gains the `Resume` outcome `ErrCheckpointUnusable` (node wire code `checkpoint_unusable`): the adapter durably closed the exact attempt before native dispatch, and the snapshot cannot be restored. A later `ObserveOnly` reports it again, and it is never returned once native restoration was dispatched.

- **Core:** on this outcome, Core ends the allocation's retention at once with `ExpireUnusableCheckpoint` (`running`, `restoring`, same `compute_revision`), and the ordinary expiry cleanup runs from there. A qualified Session then continues through the existing cold replacement. Capacity-pressure expiry still applies only to `suspended` allocations.
- **microsandbox helper:**
  - The fresh dispatch that created the admission closes it on any failure before `RestoreSandbox`.
  - Snapshot defects are also recorded as unusable: not found, identity or integrity failure, or a failed resource, workspace or runtime-image qualification.
  - Other failures are only closed, so Core retries with a new operation ID through the existing `RestoreAttemptClosed` path.
- **Docs:** `docs/sandbox-provider.md`, `contracts/agents-api/node-generation-protocol.md` and their Chinese mirrors, and the helper README.

Checks:
- `python3 scripts/build-microsandbox-provider.py test`
- `go test` with `-run` filters on the restore, compute, retention and pressure tests in `internal/execution`, `internal/deployment` and `deploymentpg`, plus `./internal/sandbox/...`
- `go vet`
- `make check-docs`

An independent review found two problems, both fixed: a failed target lookup left the admission open, and the helper README was not updated.



## MiniMax-AI/OpenAgentCore PR816

API: https://api.github.com/repos/MiniMax-AI/OpenAgentCore/pulls/816

created_at: 2026-10-21T20:03:08Z; merged_at: 2026-10-21T21:08:58Z; merge_commit_sha: 5036ed85f29363f6a748be66b6ae7f5df6e8a0c0

Keep microsandbox checkpoints as native snapshots

Stacked on #815.

A microsandbox suspend exported the native snapshot to a zstd archive, fsynced and hashed it, then deleted the native snapshot; every resume hashed and unpacked the archive again. On mx that export was 2.73 s of a 5.85 s suspend and about 0.9 s of each resume.

Now the native snapshot is the checkpoint:

- Suspend creates the full snapshot directly in the private checkpoint root (`SnapshotCreateOptions.DestDir`, group `s-<operation>`). The SDK materializes the checkpoint closure there (hard links on the same filesystem, otherwise a synced copy) and returns it durable. The adapter verifies it once, writes the ownership receipt, stops the source, then reports `SourceStopped`.
- Resume verifies the snapshot once and restores from it directly. A node that mounts the same checkpoint root restores it the same way, so checkpoint transfer keeps working.
- DeleteSnapshot writes the tombstone, then removes everything else in the operation directory without opening the snapshot, so a damaged snapshot or an interrupted capture's staging directory never blocks cleanup.
- Archive export, import, hashing and their receipt fields are deleted.

Cost: a retained checkpoint takes about 0.5 GB instead of about 0.15 GB, and a shared checkpoint root receives a full copy at suspend.

Checks: helper tests with the bundled SDK (`scripts/build-microsandbox-provider.py test`), `go test` for `internal/sandbox/microsandbox`, Core `go vet ./internal/sandbox/...`, translation check. Real-cluster timings on mx are in progress.



## MiniMax-AI/OpenAgentCore PR817

API: https://api.github.com/repos/MiniMax-AI/OpenAgentCore/pulls/817

created_at: 2026-10-22T08:51:53Z; merged_at: 2026-10-22T08:56:44Z; merge_commit_sha: 62b2df6ce8087f635e00804ca64dd79d9e4789c7

Keep Turns running when event text contains NUL

## Problem

PostgreSQL `jsonb` cannot hold `\u0000`. When a Harness emits output with a NUL byte, `InsertTurnEventBatch` rejects the whole batch (SQLSTATE 22P05), and the Turn fails with `event_persistence_failed` after the Harness has already finished. Common commands trigger it, including `grep -a`, `cat` on a binary file, reading `/proc/*/cmdline` and `find -print0`. It reproduces with Codex and Claude Code. Core logged nothing.

## Change

- `sessions.journalPayload` normalizes each journal observation and the execution outcome. It replaces U+0000 with U+FFFD in every string and key, as decoding already does for invalid UTF-8. Payloads without `\u0000` keep the existing single pass.
- `execution.journal.flush` logs a failed journal write with its Session, Turn, first ordinal and event count. It does not log the raw driver error, which can contain submitted values.
- Documentation: the rule is in [Turns and Items](contracts/agents-api/sessions-events.md), and the OpenAI compatibility ledger has a new difference line. Both have English and Chinese versions.

## Checks

- New `TestTurnJournalStoresNULInObservedTextAsReplacementCharacter` (PostgreSQL). It fails on main with `unsupported Unicode escape sequence (SQLSTATE 22P05)` and passes with this change.
- Focused tests pass for `sessions`, `execution` and `sessionpg` (journal and execution), along with `go vet ./...` and `make check-docs`.


