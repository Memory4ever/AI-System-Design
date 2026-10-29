# 必要固定contract原件摘存

下面为已读原件，provider仅保Checkpoint transfer至Timeout段；gate design含未实现分期，应按§11实际范围限定。

## Hy-Memory migration exact

Source: https://raw.githubusercontent.com/Tencent-Hunyuan/Hy-Memory/26c33ee40fbbfa9ca7b2be09c01356629b2b75de/memhub/docs/contracts/sdk-data-plane-migration-v1.md

# SDK Data Plane Migration v1

Updated: 2026-10-21.

This contract migrates released MemHub installations from the historical
Evidence/Governance authority to the Hy Memory SDK data plane defined by
[`../ARCHITECTURE.md`](../ARCHITECTURE.md).

It is an offline, resumable migration executed inside the App's visible startup
loading phase, before Core accepts product traffic. It is not a permanent
dual-read or dual-write design and is not a separate manual upgrade flow for
ordinary users.

## 1. Authority before and after cutover

Before the cutover marker is committed:

- `evidence*` and `governed_*` remain the product read authority;
- SDK stores are inspected and backfilled, but are not merged into live search;
- new imports, writes, queue drains, corrections, deletes and session delivery
  are paused.

After the cutover marker is committed:

- SDK memory/raw/vector/graph/coding stores are the only memory data authority;
- MemHub stores management state and `memory_id` / raw references only;
- legacy Evidence/Governance/retrieval/session-shadow tables are physically
  dropped before the normal App window is revealed;
- startup must not fall back to legacy authority because an SDK read failed.

The surviving `memory_authority_state` singleton, not legacy table existence,
selects the authority.

### Fresh install

A fresh home does not execute the historical application schema chain. It
bootstraps the latest management-plane schema directly with SDK authority and
never creates Evidence, Governance, legacy retrieval, any Matter, or
session-shadow tables. Historical schema migrations are an input format reader
for old homes only.

## 2. Supported source state

The migration preflight records and validates:

- source MemHub Runtime tag/build and management schema version;
- migration Runtime SDK capabilities and the actual on-disk store shape;
- SDK namespace, vector/graph/cache/history/coding providers and locations;
- embedding model identity and dimensions;
- source grants, model profiles, config, queue leases, and pending operations.

The migration fails closed when the installed SDK lacks:

- complete lifecycle/raw inventory;
- exact raw and exact memory import;
- durable request outcome lookup;
- consistent snapshot/export and restore.

MemHub tags `v1.0.0` through `v1.0.4` all use the `governed-v2` namespace and
the same SDK SQL table families (`memory_operations_v2`, `pipeline_logs_v2`,
`system_metrics`, `episode_state`, `memory_history`, `coding_memory_meta`,
`working_fact`, and `coding_trace`). They therefore use one migration selected
by inspected schema/store capabilities, not one branch per historical SDK pin.
The old SDK version is informational only and is not a migration discriminator.

The migration Runtime itself must expose the required APIs. Its exact SDK
version is defined by the release lockfiles; old data is not rejected merely
because an earlier App wrote it.

## 3. Legacy-state classification

While Core and Runtime writers are stopped, build four inventories:

- `E`: Evidence rows and revisions;
- `G`: current Governance rows, statuses, supersession links, and latest content;
- `M`: task-output mappings from legacy `memory_id` to SDK `hy_memory_id`;
- `S`: complete SDK inventory, including raw and non-active lifecycle records.

Every item must end in exactly one class:

| Class | Meaning | Required action |
| --- | --- | --- |
| matched | Governance/mapping and SDK identity, content, owner and lifecycle agree | verify only |
| mapped mismatch | legacy ID maps to a different existing SDK ID | keep SDK ID; record alias |
| Governance-only | current legacy memory has no SDK entity | exact import without extraction |
| SDK-only | SDK entity has no legacy mirror | retain and adopt |
| divergent | both exist but content, owner or lifecycle differs | reconcile explicit user intent or quarantine |
| raw-only | Evidence has no SDK raw receipt | exact raw import |
| unknown outcome | a task may have reached SDK without a confirmed result | SDK outcome inquiry; never blind retry |

An unclassified item blocks cutover.

## 4. User edits, deletion and supersession

The current product has no MemHub revision history or Undo.

- The latest non-deleted user correction is imported as the current SDK body.
- Historical `governed_memory_versions` remain in the compatibility backup, but
  are not recreated as product-visible SDK versions.
- A legacy user deletion is applied as an SDK physical delete. Deleted
  Governance tombstones are not imported and no deleted-list UI survives.
- SDK supersession remains an SDK lifecycle relationship. Existing SDK chains
  are retained. Governance links are used only to repair a missing SDK chain
  during exact import.
- Pending correction/delete records are settled before ordinary backfill.

`update(memory_id, content)` modifies the same SDK ID. There is no product CAS,
revision number, or restore operation.

## 5. Evidence to SDK raw

Evidence must not be replayed through ordinary `add()`: doing so would extract
and reconcile again, changing semantic memories.

The SDK exact-raw import preserves:

- source, conversation/session, workspace, role and author;
- original event time and stable source ordering;
- verbatim content and source identity;
- a deterministic migration key.

The operation is idempotent and returns an SDK raw ID. Evidence revisions and
repairs are preserved in the migration bundle for audit; only the current
accepted raw record becomes the normal product read.

## 6. Full migration bundle

A successful preflight creates one versioned bundle containing:

- an online backup of `one-memory.sqlite3`;
- an SDK-consistent export/snapshot of raw, vector, graph, cache, history and
  coding stores;
- `config.json` and non-secret configuration needed to locate those stores;
- Runtime, SDK, schema, namespace, backend and embedding fingerprints;
- object/file hashes, row counts, object counts and creation time;
- migration ledger version and bundle ID.

Secrets are not copied into a plaintext manifest. The bundle records only
secret references and the secure-store identity required for restore.

The bundle is published only after an isolated restore verifies hashes, counts
and SDK reads. A remote backend without a supported snapshot/export mechanism
blocks migration; SQLite-only backup is not reported as success.

## 7. Authority state and migration ledger

The MemHub management database owns:

- `memory_authority_state`: the surviving singleton authority and migration ID;
- `sdk_data_plane_migrations`: one run, source/target fingerprints, bundle,
  phase, cutover state and reconciliation digest;
- `sdk_data_plane_migration_items`: source identity/revision/hash, target SDK
  identity/hash, deterministic operation key, state, attempts and error code;
- `memory_id_aliases`: temporary historical ID to canonical SDK ID mapping for
  call-events, write-job receipts, and links;
- `raw_id_aliases`: legacy Evidence ID/item index to canonical SDK raw ID.
- `sdk_data_plane_cutover`: a temporary detailed cutover receipt containing
  SDK/backend/bundle/reconciliation fingerprints.

Progress is committed only after SDK verification. Retrying an item uses the
same deterministic SDK operation key and must not create another memory.
Before cleanup, every surviving reference is rewritten to its canonical SDK
ID. Alias, item-ledger, and detailed cutover tables are then dropped; the
authority singleton and verified bundle remain.

Backfill never mutates the live SDK root. Startup first copies the complete
local SDK data plane, including SDK-only records, to a same-filesystem staging
home. Exact legacy writes and reconciliation run there. Cutover renames the
live root to a protective path, renames staging into place, and only then
commits SDK authority. A failed commit restores the previous root; restart
recovery resolves any interrupted rename before opening SDK stores.

## 8. Queue and unknown outcomes

Queue rows and leases remain MemHub management state.

- A pending job has not called the SDK and therefore has no SDK raw or memory
  ID yet.
- Its worker calls SDK `add()` once. The SDK owns raw persistence plus
  extraction/reconciliation; a successful job stores only the returned raw ID,
  canonical memory IDs and terminal outcome.
- Legacy raw and semantic backfill is an App-owned privileged offline
  operation while Runtime writers are stopped. It writes SDK stores directly;
  no migration-only import/get/list method is added to public
  `HyMemoryClient`, and this is not the first half of a two-stage normal write
  path.

- `hy_invoked=0` may be safely retried after normal lease recovery.
- `memory_write_jobs.hy_invoked=1`, `state=unknown`, or any non-terminal SDK
  outcome must use `get_write_outcome(request_id)`.
- `running`/`unknown` is not absence and must not be replayed.
- confirmed SDK IDs become write-job outcomes/receipts; Governance publication is not part of
  completion after cutover.

## 9. Call events and session delivery

- Matter was an unpublished placeholder. Its rows are not migrated and every
  `matter*` table is deleted during cleanup.
- Before cleanup, historical IDs resolve through `memory_id_aliases`; surviving
  records are rewritten to canonical SDK IDs before that table is dropped.
- `call_events` remains metadata-only; reference titles/content resolve through
  SDK APIs.
- Evidence-based session inbox/outbox is disabled at cutover unless replaced by
  a management-event or SDK-event contract. It must not send shadow memory
  bodies.

## 10. Cutover

The packaged App owns orchestration. While the startup placeholder is visible,
it starts no product writer, creates or verifies the full bundle, resumes the
durable migration ledger, reconciles SDK state, and only then commits cutover.
The normal App window is revealed after this phase. A retry resumes the same
migration and deterministic operation keys; it does not create a second run.

If migration cannot safely complete, the marker remains absent and startup must
report the durable blocked/deferred reason. It must not silently continue into
an SDK/legacy dual-write mode. A missing model profile may defer migration while
legacy authority is still intact so the user can configure the App; it never
authorizes a partial cutover.

Cutover requires:

- no unclassified or quarantined item;
- complete raw coverage;
- no unsafe unknown task;
- pending corrections and deletions settled;
- call-event references resolvable;
- exact counts and hashes reconciled;
- deterministic full-ID get verification;
- a verified full migration bundle.

The final transaction writes the detailed cutover receipt and changes
`memory_authority_state` to SDK authority. Cleanup may remove the detailed
receipt after bundle verification; the authority singleton remains.

After that transaction, legacy memory/raw writes are rejected.

## 11. Rollback and version skew

Before cutover, a failed run resumes from the ledger or restores the full
bundle.

After cutover but before any SDK-only write, rollback restores the full bundle
and matching old Runtime together.

After an SDK-only write:

- automatic binary-only rollback is forbidden;
- operators either forward-fix, or explicitly restore the pre-cutover bundle
  while acknowledging loss of post-cutover writes;
- an old Runtime must fail closed on the post-cutover marker/schema.

Changing only the Runtime `current` symlink is not data rollback.

## 12. Legacy cleanup

Legacy tables are not a compatibility runtime. After every memory/raw
reference resolves, the verified bundle has passed restore validation, and the
SDK cutover marker is durable, the offline startup transaction drops:

- every `evidence*` and `governed_*` table;
- legacy retrieval/index tables;
- every `matter*` placeholder table;
- legacy deletion/index-sync/task-output and session-shadow tables;
- migration-only aliases and ledgers after their canonical references have
  been materialized into the surviving management tables.

Before that DROP, every surviving `memory_write_jobs` row is made
self-contained by freezing its source records into `payload_json`. Unstarted
legacy `memory_tasks` rows are converted to deterministic
`memory_write_jobs(idempotency_key="legacy-task:<task_id>")`; possibly-sent
task rows remain a cutover blocker until SDK request-ID reconciliation proves
their outcome.

The verified bundle is the audit and rollback artifact; keeping duplicate
plaintext tables in the live database is not. A cleanup failure keeps startup
blocked and never exposes a half-cleaned schema.

## 13. Acceptance matrix

The release gate covers:

- a clean install with no legacy rows;
- a clean install whose schema contains no legacy table names;
- Governance-only, SDK-only, mapped-ID and divergent fixtures;
- Evidence/raw-only content;
- pending correction and physical deletion;
- unknown SDK outcome and crash after SDK commit;
- interruption before/after each ledger transition;
- full bundle restore and hash/count mismatch;
- call-event alias preservation;
- old Runtime against a post-cutover home;
- successful migration followed by physical absence of every legacy table;
- local and supported remote backend snapshot behavior.

No narrow unit test may be used as evidence that the full migration is safe.


## Qwen manual compression exact

Source: https://raw.githubusercontent.com/QwenLM/qwen-code/d03b3116dae52589210a50f84ac099876f75326c/docs/design/2026-10-22-managed-context-compression.md

# Managed manual context compression

[English](2026-10-22-managed-context-compression.md) | [中文](2026-10-22-managed-context-compression.zh-CN.md)

## Problem and boundary

Issue #15080 requests explicit control over when Managed Session history is summarized. This slice provides an idle-only durable Operation and an action in the existing context usage popover. It reuses Core compression without creating a user Turn, changing approval policy, rewriting the audit transcript or changing the Workspace installation revision.

The current Hosted model path rebuilds history from a message-only projection. Compression checkpoints must participate in that model projection, including after reopening or writer takeover. Large snapshots use the existing chunked message-body format rather than exceeding the 64 KiB inline resource limit.

## Admission and API

PUBLIC Sessions bound to a Workspace admit OPERATOR and OWNER callers. Active or queued Turns, approvals, unresolved Hooks, recovery and conflicting mutations return session_context_busy. Ordinary user input is refused during maintenance; autonomous input remains in its existing durable queue and executes afterward.

POST /v1/agents/sessions/{sessionId}/compress accepts expected_compaction_revision and Idempotency-Key. The WebShell twin is POST /api/agent/web-shell/v1/sessions/compress with camelCase fields. HTTP 202 returns a context_compression Operation, read through the existing operation queries. States are pending, running, recovery_blocked, completed and failed; a completed outcome is compressed or noop. Read authorization precedes actor-scoped replay, which precedes mutable role, capability, revision and busy checks. Conflicting key reuse is idempotency_conflict.

The latest context.compacted event sequence is compactionRevision, initially zero. It is independent of context_revision. Session summaries publish it and any active compression operation. WebShell's contextCompression capability reflects the caller's grants. Public API capabilities retain their existing deployment/support meaning; the compression POST always rechecks authorization. The private Harness adds context-compression/1 and dedicated submit/status routes; older Harness versions fail closed.

Older Sessions without a compaction projection lazily recover it from the verified committed journal prefix. Unavailable evidence hides the capability and omits the revision. Backfill and new commits advance the projection monotonically and retain any newer main-model usage observation.

## Execution and persistence

The Java ma_operation records CONTEXT_COMPRESSION; the reserved history_maintenance domain records the native execution. Source history cut, model/provider identity and parameters are immutable. PreCompact and PostCompact use separate stable operation-scoped occurrences, originTurnId=null. A candidate containing new history, summary and compression information commits before PostCompact. Hosted compression never reads recent-file bytes from the Harness host.

A narrow authority commit atomically appends context.compacted and the final maintenance outcome. NOOP and known failure also retain outcomes without changing history or revision. SQL projects the compaction and invalidates the previous usage/resource reference in the journal commit transaction. Replaying an outcome cannot clear a newer observation. The complete original transcript remains available.

The initiating actor's execution authority is revalidated before submission and in the final SQL transaction. Revocation after native acceptance retains the candidate and recovery barrier; restoring authority allows the original operation to continue.

Core exposes an awaited compression observer at the existing recording payload boundary, preserving pendingUserMessage, summaryPrefixLength and completedToolCallIds. Automatic and manual compaction share model-history restoration. Prepared model-request recovery keeps its existing precedence.

Tool-result recovery also retains a compaction recorded after the last tool-call message. Its declared pending-response tail is removed from the restored prefix and sent once through the existing resume path. Failed or cancelled user input is excluded, including when embedded in a previous snapshot's raw tail.

## Recovery

Unknown Harness acceptance is reconciled from the original durable evidence, never blindly redelivered. A known admitted operation resumes after fencing its old writer. A terminal outcome replays; a candidate resumes PostCompact and application without model recomputation. Without a candidate, a started pure summary attempt may be abandoned and replaced using the same source snapshot, provider pin and persisted PreCompact output. Model billing can repeat, but history commits once. Unknown Hook executions are reconciled rather than repeated. A delayed old writer cannot save a candidate or proceed to PostCompact after losing its fence.

The browser persists intent before submitting, reuses its key after uncertain responses, polls after refresh and adopts an operation advertised by another tab. Send and conflicting controls stay disabled until settlement. Context occupancy becomes unknown after success until a new committed main-model observation; summary-query usage is never substituted.

## Validation and rollout

Verify continuation, reopen and Harness takeover against compressed model inputs while preserving transcript and tool pairing. Race compression against Turns, wake inputs, approvals, model/CWD changes and close. Inject faults before/after candidate persistence, PostCompact, final commit and response delivery; a late old summary must not apply. Cover NOOP, API/Hook failures, corrupt chunks and snapshots larger than 64 KiB.

Run focused Core, CLI, WebShell, SDK and Java tests, root build/typecheck/bundle, API contract gates, disposable MySQL concurrency checks and relevant Hosted fault tests. Record unavailable checks explicitly. Add an incremental canonical-schema migration; never rewrite the published baseline. Deploy schema and Java/Broker readers before Harness writers and then WebShell. Stop new admission and settle accepted operations before rollback.

## Defaults

No custom compression instructions, busy-session compression, compression queue or new slash-command dispatch in this slice. No pending product decisions remain; validation results are recorded separately.


## OpenAgentCore provider exact

Source: https://raw.githubusercontent.com/MiniMax-AI/OpenAgentCore/01a041c6e68752f39a155af7acb405b441091be6/docs/sandbox-provider.md

### Checkpoint transfer

A checkpoint-capable generation reports `CheckpointCompatibility`: opaque `ArtifactDomain` and `ExecutionClass` tokens. Every verified `SnapshotIdentity` carries the same qualification. Core compares these values without interpreting CPU features, filesystem paths or storage implementations. A restore destination must be online and ready for the allocation's immutable deployment generation, match both tokens, and have active capacity plus a retained slot when moving from another node. The allocation, Device and Session identities remain unchanged. The Session and deployment transaction commits the destination route, placement and exact restore intent before target-side native work. No capacity or compatible destination leaves the retained snapshot owned until its configured deadline. The target must already hold that exact generation; Core does not automatically prepare historical generations on new nodes. A node keeps a superseded generation's provider until its checkpoint retention obligations end.

`Suspend` may report `SourceStopped` only after publishing a verified full checkpoint durably, stopping the exact source compute and settling source-local capture and cleanup obligations. Core persists the snapshot before marking it suspended; native absence alone is insufficient. `Suspend.ObserveOnly` may finish checkpoint publication and source cleanup for an already verified snapshot of the same operation, but cannot capture another snapshot or stop a source that has resumed running. If a previously published checkpoint is missing or damaged, `ObserveOnly` may return its exact durable ownership receipt with `Status: unknown` and `SourceStopped: false` for cleanup; that receipt proves neither current checkpoint usability nor source absence. `Resume` still verifies the checkpoint before execution. After the source-settlement barrier, source-node unavailability does not prevent restoration. Deletion and ordinary expiry can transfer an idle suspended allocation's cleanup route to an online node in the same artifact domain; deletion does not require execution-class compatibility. The cleanup destination must already serve the same immutable generation and have retained capacity. Without such a node, cleanup stays pending and ownership is not released; operators must restore an eligible node or its capacity. An unknown running or restoring writer never moves merely because its node is unreachable.

Recovery uses `Resume.ObserveOnly` for the persisted target and operation. `RestoreAttemptClosed` is an exact operation ID, not a generic absence flag: the adapter may return it only after durably closing an attempt that never entered native execution and fencing every late request for that ID. An adapter may also close a durably admitted attempt when it can prove that its current invocation failed before dispatching native restoration. The microsandbox adapter does this for the fresh request that created the admission, on any failure before it dispatches native restoration. An expired wire deadline or an unclassified failure closes the attempt, and Core then persists a new operation ID. A snapshot that is missing, fails identity or integrity verification, or fails the adapter's qualification for this generation, such as a resource, workspace or runtime image mismatch, is also closed and reported as `ErrCheckpointUnusable`. That outcome is durable: `Resume.ObserveOnly` for the same operation reports it again, and late requests for the operation ID stay fenced. A Provider never returns it once native restoration was dispatched. On `ErrCheckpointUnusable` Core never restores that snapshot again and [ends its retention at once](#cold-replacement-after-checkpoint-retention). Once native restoration has been dispatched, an unknown outcome retains the same target, ownership and original retention deadline; a missing native listing, helper death or timeout does not authorize replay. Such a restore can remain unavailable until explicit deletion or ordinary retention expiry, and pending inputs can reach their public deadline while waiting. User deletion still requires exact native settlement before resources and ownership can be released.

The microsandbox adapter requires an explicit private `checkpoint_root`, outside every guest-accessible filesystem. Its directory is mode `0700`; a private namespace marker identifies the actual checkpoint store. The default installation creates a node-local private store. Cross-node restoration requires operators to mount the same private store on each participating node; mount paths may differ. Each retained checkpoint is an uncompressed native snapshot of the guest's memory and root-disk layers, so a shared store carries that volume for every suspension and cross-node restore. Runtime state directories and workspace bindings are never used to infer this root. The adapter verifies the checkpoint, external filesystem identity and native execution class again before restoration. Restored RAM and file descriptors do not promise continuity of external TCP connections or replay safety for application side effects.

### Cold replacement after checkpoint retention

Snapshot retention bounds compute resources, not the lifetime of an eligible retained Session. After the deadline, Core can clean up the allocation without terminating the Session only when its independent filesystem object is ready, initialization is complete, the Session and Environment remain nonterminal, and the previous authenticated Runtime has a persisted `retained_native_history` declaration. The capability and native recovery obligations are defined by the [Core–Runtime protocol](runtime-protocol.md). Filesystem retention alone is insufficient.

An unusable checkpoint, reported as `ErrCheckpointUnusable` by a restoring allocation's `Resume`, ends retention at once, exactly as if its deadline had passed. Core deletes the target and snapshot through the ordinary expiry cleanup, and a qualified Session continues as below, while an unqualified one ends as at ordinary expiry.

Capacity pressure ends retention early only for the node's oldest idle suspended allocation that meets these conditions, and only when waiting placement demand is blocked by the node's full retained slots. Core then treats the allocation as expired, one release per blocked demand, and every other suspended allocation keeps its snapshot and retained slot until its configured deadline. A checkpoint whose restore lacks capacity or a compatible node is not cold-replaced for that reason. Pending requests retain their original input deadline. The ordinary expiry cleanup must confirm resource deletion before another allocation can reserve the slot; files and qualified native history remain retained.

Core confirms the original creation is settled and all owned compute and snapshots are cleaned up before releasing allocation and placement ownership. The old device's authority is revoked before replacement admission. Until Create, Kill or DeleteSnapshot has a confirmed outcome, it keeps ownership and admits no replacement writer. A recoverable Session and Environment remain disconnected with the same filesystem object and initialization result. Archive, reset and deletion take precedence and cannot be undone by a wake request.

New input or live Environment file access reserves a new allocation on a compatible node and bootstraps a fresh Runtime device. Preparation reuses the same filesystem and completed initialization rather than replaying initialization. Execution resumes the same native Session from retained history after validating the replacement Runtime's declaration. Missing or invalid native history fails explicitly; Core never substitutes a new native Session or replays completed input. History and published Artifact reads do not reserve compute. This path does not preserve VM memory, background processes or open connections, and it does not qualify an undeclared Runtime, Harness or filesystem combination. It also provides no node-level drain, failover from an unreachable writer, concurrent writers, multi-active Core, autoscaling or snapshot replication.

### Confirmed compute loss

Running compute has no retention deadline, so a host crash or reboot would otherwise leave its allocation owned indefinitely. After the owning node is online again, `GetCompute` returning `ErrNotFound` or a verified `stopped` or `crashed` status for the exact persisted incarnation releases a checkpoint-capable allocation in compute phase `running` only when all of these hold: the original creation is settled, the incarnation has a native ID, no capture, restore or rollback intent is recorded, no authenticated Runtime connection exists for the allocation's device, and the Session meets the conditions for [cold replacement](#cold-replacement-after-checkpoint-retention). Core then calls `KillCompute` for that exact incarnation. Only its confirmed result permits one Session-locked commit that rechecks the compute revision and those conditions, revokes the device and releases the allocation and placement. The Session, Environment, pending input, native Session identity and filesystem remain, and new input or live file access continues as in cold replacement.

Every other observation keeps ownership and its diagnostic: a `paused`, `running` or unknown native status, an identity mismatch, a timeout or transport error, an unknown creation, a recorded restore, a live Runtime connection, owned workspace storage, incomplete initialization, a terminal Session or a missing `retained_native_history` declaration. A failed `KillCompute` changes nothing, and a concurrent archive, deletion or compute transition prevails. Core never acts while the node is offline, because it has no authority to stop compute without the node. Continuation retains the filesystem and uses the recorded native Session ID; a Harness resume error fails execution rather than creating another native Session. Core does not replay interrupted or completed input. [OpenAI compatibility](../contracts/agents-api/index.md) records the qualified continuation cases, including crashes immediately after completion acknowledgement. Completeness of arbitrary crash-damaged native history remains unqualified; identity checks do not detect a truncated but parseable history tail.

## Timeouts and limits

| Value | Applies to | On expiry or excess |
| --- | --- | --- |
| Bounded context | Every Provider call | Ends the caller's wait and proves no rollback, stop, cleanup or absence. The adapter never detaches untracked mutations or replays a timed-out command |
| Idle timeout and snapshot retention | Checkpoint-capable allocations, set by the [suspension policy](../contracts/agents-api/sandbox-deployment.md#suspension-policy) | At the idle timeout Core begins [suspension](#suspension). When retention ends Core cleans up the snapshot and, for a qualified Session, replaces the compute through [cold replacement](#cold-replacement-after-checkpoint-retention) |
| 15 s | Inactivity of an idle node allocation before capacity-pressure suspension | Core can suspend it ahead of the idle timeout when compatible waiting demand exists |
| 2 min | Inactivity of an idle allocation on a node with no free active slot and a free retained slot | Core can suspend it ahead of the idle timeout without waiting demand, so the next Session finds a free slot |
| 50 MiB plus 32 bytes (`MaxCommandInputBytes`) | `Command.Stdin` | The command is invalid |

The online window and the other node timers are in the [sandbox node protocol](../contracts/agents-api/node-generation-protocol.md#timeouts-and-limits).



## Qwen scheduler gate exact

Source: https://raw.githubusercontent.com/QwenLM/qwen-code/74c67c9e94f09b80b5f47df8f8ab216c9ebe6a14/docs/design/2026-10-21-scheduled-task-gate.md

# Scheduled-task gate: a probe decides whether a fire reaches the model

[English](2026-10-21-scheduled-task-gate.md) | [简体中文](2026-10-21-scheduled-task-gate.zh-CN.md)

- **Status**: 2026-10-21. PR 1a (Section 11) is implemented on the PR
  branch; PR 1b, the probes and the skills remain proposals. Step 1 of the
  event-driven PR watch (issue #15056); the probes (step 2, continuing
  PR #15057) and the skills (step 3) build on it.
- **Related**:
  [scheduled-task current-session entrypoints](2026-08-24-scheduled-task-current-session-entrypoints.md),
  [scheduled-task empty-session persistence](2026-08-26-scheduled-task-empty-session-persistence.md),
  [scheduled-task safe delete](2026-10-15-scheduled-task-safe-delete.md),
  [one Autofix skill for local and CI runs](autofix-shared-skill.md).

## 1. Problem

Two workflows need a Qwen Code session to react to GitHub without a person
watching:

- A developer keeps a pull request moving: a check fails, a reviewer comments,
  the base branch moves and the PR conflicts.
- A reviewer runs a review or a verification pass when a PR is opened or
  receives a push.

Today the only way to keep a session on such a watch is `/loop` or
`cron_create`: a prompt fires on a timer and the model polls. Every fire is a
model turn whether or not anything changed. The default 30-minute cadence is
too slow for CI and review traffic; a 5-minute cadence fills the conversation
with turns that report nothing.

Polling itself has to stay. GitHub cannot push to most developer machines (no
public ingress), and it sends no webhook at all for merge-conflict transitions
(`mergeable` is only observable by polling). What has to change is who polls:
the check must run outside the model, and the model must only be woken when
the check found something.

## 2. Current state

Building blocks on `main`:

| Need                       | Existing piece                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recurring trigger          | `cron_create` and `CronScheduler` (`packages/core/src/services/cronScheduler.ts`). One scheduler per session, created by `Config.getCronScheduler()`. The tick is synchronous and every fire kind (tick, catch-up, final, forced) ends in one `onFire(job)` callback.                                                                                                              |
| Fire consumers             | The interactive TUI (`packages/cli/src/ui/hooks/use-llm-stream.ts`, a `kind: 'cron'` entry in the background notification queue), the ACP `Session` (its own cron queue; `per_run` tasks spawn a fresh child session with a `buildScheduledTaskRunPrompt` header) and the headless CLI (`packages/cli/src/nonInteractiveCli.ts`). All three deliver `job.prompt` as the turn text. |
| Durable tasks              | `packages/core/src/services/cronTasksFile.ts`: `~/.qwen/tmp/<project-hash>/scheduled_tasks.json`, atomic writes under a lock, unknown keys accepted and preserved on rewrite, a 20-entry run ring, and fail-closed handling of the removed `condition` field (`taskHasLegacyCondition`).                                                                                           |
| Daemon                     | There is no daemon-level scheduler. Each ACP session runs its own, and `packages/cli/src/serve/scheduled-task-keepalive.ts` keeps every bound session loaded, so a fire never restores a cold session. `packages/cli/src/serve/routes/scheduled-tasks.ts` and the Web Shell dialog create, edit and "run now" tasks.                                                               |
| Unattended shell execution | The `Monitor` tool (`packages/core/src/tools/monitor.ts`): command validation, an `exec` confirmation with `Monitor(...)` permission rules and the read-only AST shortcut, `executeRuntimeShell` with a sanitized environment, and output sanitization that defangs envelope tags.                                                                                                 |

Two earlier attempts do not fit:

- The `condition` precondition on isolated scheduled tasks (#6619) was
  evaluated by the model in the task's own session, so a quiet fire still cost
  a turn. It was removed together with isolated mode in #6676; a task that
  still carries `condition` never fires, on every path.
- `Monitor` streams a script's output as notifications, but it auto-stops after
  at most 10 minutes of silence, and a PR is quiet for hours.

Other harnesses: Claude Code injects GitHub events into a running session
through its own cloud and an outbound bridge connection from the CLI; Codex and
deepseek-harness start a new task or session per event; none of them see
conflict transitions. A local poller that runs outside the model is the only
path that works on an intranet, and it is what this design builds.

## 3. Goals and non-goals

Goals:

- A scheduled task can carry a **gate**: a shell command that runs at fire
  time, outside the model. A silent gate skips the fire with no model turn, no
  queue entry and no transcript record. A gate that prints output delivers the
  fire with that output attached.
- The gate works everywhere a scheduled task fires: TUI, ACP, headless,
  daemon-bound sessions, `per_run` tasks, and durable tasks across restarts.
- A gate is approved like a `Monitor` command, never runs where the user would
  have expected to approve it, and its output reaches the model as data.
- Quiet fires are cheap enough for a one- or two-minute cadence.

Non-goals:

- GitHub-specific logic in core. Probes are ordinary commands
  (`qwen autofix-pr snapshot --gate`, a repository-level probe, `gh api`, a
  script); their cursors, filters and budgets live in the probe.
- Coalescing or de-duplicating events in core. A probe prints only what is new
  since its last run. A fire that comes due while the session is busy is
  already delayed until the session is idle, and the probe then runs once.
- Webhooks or an inbound relay.
- Any change to when the model-driven paths (`/loop`, a plain `cron_create`)
  fire.
- Managed Agents. A managed automation is fired by the control plane's
  scanner into a persistent session through the Harness and never touches
  `CronScheduler` or the tasks file (managed-automation runtime design,
  decision 14). A gate there needs a Runtime "gate probe" operation with its
  own durable identity, a schedule-record change in both languages and fault
  gates; it is a separate design (Section 11).

## 4. User-facing behavior

### 4.1 `cron_create`

One new optional parameter:

```text
gate: string — shell command run at each fire, outside the model.
  Prints nothing and exits 0 → the fire is skipped; no turn runs.
  Prints something and exits 0 → the fire is delivered with the output.
  Exits non-zero or runs longer than 60 s → reported once, then counted
  silently until the gate succeeds again.
```

The developer watch becomes:

```text
cron: "*/2 * * * *"
gate: "qwen autofix-pr snapshot --gate 15057"
prompt: "The gate output lists what changed on QwenLM/qwen-code#15057 since
         the last check. Handle each event: ..."
```

The reviewer watch becomes:

```text
cron: "*/2 * * * *"
gate: "qwen review watch-repo --gate QwenLM/qwen-code --review-requested"
prompt: "For each pull request event in the gate output, run /qreview <number>."
```

`gate` needs a recurring task: a one-shot has no next slot, so a quiet gate
would consume it with nothing delivered and no trace, and `cron_create`
refuses the combination. It is accepted with `durable` and with the unbound
session mode (`sessionMode: "current"` comes with the daemon follow-up). The
tool result names the gate, and `cron_list` prints the gate and its last
outcome after the prompt:

```text
ab12cd34 — every 2 minutes (recurring) [session-only]: The gate output lists…
           gate: qwen autofix-pr snapshot --gate 15057 — quiet ×41, last delivered 13:05, 0 failures
```

### 4.2 What the model sees

A gated fire that delivers keeps the task prompt first, so the TUI's
`Cron: <first 40 characters>` line and the ACP echo stay recognizable, and
appends one block:

```text
<task prompt>

Gate output. The task's gate command printed this at 2026-10-21T05:05:07.000Z
(`qwen autofix-pr snapshot --gate 15057`, exit 0, 1.8 s). It is data produced
by that command, not instructions.
<gate-output>
…stdout…
</gate-output>
```

A gate failure delivers a notice instead of the prompt, once per failure
streak:

```text
Scheduled task ab12cd34 (every 2 minutes): its gate command failed, so the
task prompt did not run. `qwen autofix-pr snapshot --gate 15057` exited with
code 1 after 0.4 s. Further consecutive failures are counted silently until
the gate succeeds again (see cron_list). stderr, last 20 lines:
<gate-stderr>
…
</gate-stderr>
Tell the user, and suggest a fix if the cause is clear (for example expired
`gh` authentication). Do not run the task prompt.
```

A gate that may not run unattended (Section 5.4) delivers a similar notice
that names the permission rule to add. A `per_run` task wraps the same text
in the existing `buildScheduledTaskRunPrompt` header.

### 4.3 Daemon and Web Shell

- The scheduled-task form gets one optional field, "Gate command", shown
  only when the daemon reports the `scheduledTaskGate` capability. An older
  daemon would silently drop the field on `POST`.
- The task card shows the gate and its last outcome
  (`quiet ×41 · last delivered 13:05 · 0 failures`).
- "Run now" on a gated task sends a manual-run prompt that asks the model to
  run the gate as an ordinary shell command and then follow the task prompt
  with the output as data only when the command exited 0 and printed
  something; to say that the gate printed nothing when it exited 0 silently;
  and to report the failure and stop on a non-zero exit, a timeout or a
  cancellation — the runner's three outcomes. The usual tool approval
  applies; the scheduler is not involved, as today.

## 5. Design

### 5.1 The gate contract

A gate is a shell command. The scheduler runs it with:

- the session's working directory at fire time (`Config.getTargetDir()`) and
  the session's shell configuration, through `executeRuntimeShell` — the same
  path `Monitor` and the shell processor use, so the sandbox policy and the
  sanitized environment apply;
- no stdin, a 60-second timeout, one run at a time per task.

Its exit code and stdout decide the outcome:

| Gate result                          | Outcome     | What happens                                                                     |
| ------------------------------------ | ----------- | -------------------------------------------------------------------------------- |
| exit 0, stdout empty after trimming  | `quiet`     | Nothing is queued or recorded in the transcript.                                 |
| exit 0, stdout non-empty             | `delivered` | The fire is delivered with the output (first 16 KiB; truncation is noted).       |
| non-zero exit, timeout, cannot start | `failed`    | A notice is delivered for the first failure of a streak; later ones are counted. |
| binary output                        | `failed`    | The command is stopped; same as any other failure.                               |
| not allowed to run unattended (5.4)  | `blocked`   | Same as `failed`, with the rule to add.                                          |

A probe therefore keeps its own cursor and prints only transitions: a new
comment, a check that just failed on the current head, `mergeable` turning
`CONFLICTING`, a PR opened, a head moved. It must be idempotent, because a
slot that comes due while the previous gate run is still in flight is skipped
and the next slot runs it again.

### 5.2 Where the gate runs

In `CronScheduler`, at the one point every fire kind passes before `onFire`.
The front ends keep delivering `job.prompt`; the scheduler hands them a copy
of the job whose `prompt` is the composed text of Section 4.2. Nothing else
in the TUI, ACP or headless paths changes for delivery.

The runner is injected by `Config.getCronScheduler()`, so each session's
scheduler executes its gates with that session's working directory,
environment and permission state. In the daemon the scheduler lives in the ACP
child, not in the daemon process, which has no session `Config` and would run
the command with the daemon's environment.

Sequence for a slot that matches:

1. Stamp `lastFiredAt`, apply the one-shot and expiry removals exactly as
   today, and mark the job `gateInFlight`. A later slot that matches while the
   flag is set returns `none`.
2. Run the gate asynchronously. When it settles, clear the flag, record the
   outcome and either return (`quiet`, suppressed `failed`/`blocked`) or call
   `onFire` with the composed job. The consumer is the one installed when the
   gate settles, not when it started: ACP re-installs its callback through
   `start()` after every turn while the timer keeps running, and that must
   not drop a gate that was mid-run.
3. A delete, a disable or a removal while the gate runs aborts it, whichever
   path it takes: `delete()`, `stop()`, or a reload of the tasks file that no
   longer lists the job, lists it disabled, or lists it with another gate (the
   paths another session and the daemon's task controls use). The safe-delete
   rule "delete takes effect immediately" covers the running command, not
   only its result. A scheduler without a runner (a `Config` that cannot
   execute shell commands) treats every gated fire as `blocked`.
4. A settlement that delivers nothing is reported to a listener
   (`setGateSkippedListener`). The headless run re-checks its hold-open
   from it: a one-shot or an expiring recurring job leaves the map before
   its gate runs, and `sessionSize` keeps counting that fire until the gate
   settles, so a quiet final gate ends the run instead of pinning it. The
   hold-open also waits for any gate still running (`hasGatesInFlight`),
   durable ones included: durable jobs do not pin a headless run, but a
   catch-up that `start()` flushes is stamped before its gate decides, so
   stopping there would abort the gate and lose the slot. A gate cancelled
   by `delete()` or a disk reload delivers nothing but is still reported
   once its command returns, since it may have been the last thing the run
   waited on; one cancelled by `stop()` is not, as the run is already over.

Missed-task carriers never run a gate: their prompt is a notice, not the
task's command. Catch-up fires, final fires and `forceFireJob` run it, so the
`QWEN_CODE_TEST_CRON_FAST` integration hook exercises the same path. A gated
catch-up persists its `lastFiredAt` stamp at once, so a restart cannot replay
it, and books its run only when the gate delivers, as a `catch-up` run.

### 5.3 Outcome records

The job keeps a `gateStatus` summary: last outcome and time, quiet fires
since the last delivery, consecutive failures, and the last error line. For
durable tasks it is written with the per-fire persist that already stores
`lastFiredAt`, so a one-minute gated task rewrites the file no more often than
a one-minute plain task does today.

Quiet fires do not append to the task's `runs` ring; a one-minute cadence
would flush its 20 entries in 20 minutes. Delivered, failed and blocked fires
append a run with `gate: 'delivered' | 'failed' | 'blocked'`, so the Web Shell
history shows what actually reached a session.

### 5.4 Approval and trust

A gate runs a shell command with no model in the loop, so it is approved where
the command is proposed and checked again where it runs.

- **Proposed by the model (`cron_create` with `gate`).** The tool's default
  permission is `ask`, because the scheduled prompt runs with full tool
  access, so the call reaches the dialog in default mode and the classifier in
  auto mode. With a gate the confirmation is the `exec` dialog with the
  command exactly as it is persisted and run, its root, the `Monitor(...)`
  rules from `extractCommandRules`, and a warning that it runs unattended on
  the schedule. A gate that backgrounds any part of itself with `&`, including
  the `&` that ends a wrapper's script (`bash -c './probe.sh &'`), also behind
  a prefix (`nohup`, `sudo`, `env`), is refused before the dialog: it would
  return at once with nothing on stdout.
  "Always allow" therefore saves a `Monitor(...)` rule, not a `cron_create`
  rule. The classifier input for auto mode includes the gate. A bare
  `cron_create` allow rule saved before this change does not cover a gate.
  Such a rule takes the allow fast path around the dialog in default mode and
  around the classifier in auto mode, so nobody has looked at the command;
  the tool then requires a saved `Monitor(...)`/`Bash(...)` rule or the
  read-only check for the gate and refuses the call otherwise. Yolo mode
  confirms nothing, and the gate runs unattended in yolo mode anyway. Before
  any of this, an explicit deny rule for the gate as a `monitor` command
  refuses the call in every mode, a confirmed dialog included: the runner
  checks that deny first at every fire, so the task could only ever be
  blocked.
- **Written by the user (Web Shell form, a hand-edited tasks file).** Trusted
  like the permission rules themselves: the file lives under the Qwen home
  next to the settings that hold those rules, and a process that can write it
  can already write them.
- **At fire time** the runner evaluates the command as a `monitor` call
  (`PermissionManager.evaluate`). An explicit deny rule blocks it in every
  mode, checked before the mode shortcut the way an ordinary tool call is
  denied before yolo or auto mode approves it, so a persisted gate stops the
  moment the user saves the rule. Otherwise it runs when the session's
  approval mode is `yolo` or `auto`, when a saved `Monitor(...)` or
  `Bash(...)` rule or the read-only check allows the command, or when this
  job was confirmed in this process. Anything else is `blocked`, with one
  notice naming the exact rule to add. Plan mode blocks. The daemon's default
  is auto mode, so a gated task created in a daemon conversation keeps working
  after a restart.
- **Output is data.** Gate output is sanitized like `Monitor` lines (control
  characters stripped, envelope tag names defanged, `gate-output` and
  `gate-stderr` added to that list), wrapped in the text of Section 4.2, and
  delivered on the existing cron path, which cannot answer a pending
  permission prompt and skips the `UserPromptSubmit` hook. One fix rides
  along: the TUI drain passes an explicit non-shell intent for cron fires, so
  a fire that lands while the composer is in `!` mode is never executed as a
  shell command.
- The gate inherits `sanitizeChildEnv`, which strips Qwen credentials but
  leaves tool credentials such as `GH_TOKEN`; a GitHub probe needs them.

### 5.5 Persistence

`DurableCronTask` gains `gate?: string` and `gateStatus?: {...}`;
`durableTaskToJob` and `jobToDurableTask` carry both. The REST `toView` exposes
both; `POST` and `PATCH` accept `gate` as a string, and `PATCH` accepts `null`
to remove it.

Downgrade fuse: an older binary ignores `gate` and would fire the task
unconditionally — the silent degradation #6676 guarded against. The writer
therefore mirrors the gate into the legacy `condition` field, which every
older reader treats as fail-closed, and `taskHasLegacyCondition` returns
`false` when `gate` is present. Removing the gate clears both. An older
version shows such a task as "legacy precondition, will not fire — recreate
it", which is the safe outcome.

### 5.6 Daemon

- Bound sessions are pinned by the keepalive, so a quiet gate costs one
  process spawn in the ACP child and nothing else. No session is created or
  restored for it.
- `per_run` tasks run the gate in the bound session's scheduler before the
  per-run branch; a quiet gate creates no child session.
- `sessionMode: 'current'` threads `gate` through the existing creator chain:
  `getCurrentSessionScheduledTaskCreator` → the
  `qwen/control/scheduled-task/create-current` ext method → the bridge →
  `createScheduledTaskWithExistingSession`.
- The `scheduledTaskGate` capability is added to `packages/cli/src/serve/capabilities.ts`
  and documented in `docs/developers/qwen-serve-protocol.md`; the Web Shell
  shows the field only when it is present.
- The keepalive is unchanged. Running gates from a daemon-level ticker and
  unpinning gated sessions is follow-up work (Section 12).

## 6. Decisions

1. **Field name `gate`.** `condition` is reserved by the fail-closed legacy
   path; `check` collides with GitHub checks in the probes' own vocabulary.
2. **The gate lives in the scheduler, not in the front ends.** One choke point
   covers every fire kind and every consumer. The removed precondition lived on
   the front-end side and needed fail-closed patches in four places when it
   went away.
3. **A shell command, not a model-evaluated condition.** The whole point is a
   quiet fire that costs no turn.
4. **Delivery by prompt substitution, prompt first.** No front-end change is
   needed to deliver; display lines and echoes keep showing the prompt. A
   gated prompt should be instructions ("for each event…"), not a slash
   command, because the TUI runs slash commands found in cron prompts.
5. **No coalescing in core.** Probes print transitions; a delayed fire runs the
   probe once when the session is idle.
6. **Trust model of Section 5.4.** Approve where the model proposes, trust what
   the user writes, re-check at fire time with the session's rules and mode.
7. **Downgrade fuse through `condition`.**
8. **Fixed limits, no new settings**: 60 s timeout, 16 KiB delivered output,
   20 stderr lines, one run at a time per task.

Rejected:

- `Monitor` without the idle cap, with a resident polling script: the process
  dies with the session, cannot be durable, and every line is a notification.
- A `pr_watch` tool with a GitHub poller in core: GitHub-specific code in the
  backbone, and a second implementation of what `snapshot` already does.
- A GitHub webhook route in `qwen serve`: no inbound path on an intranet, and
  no conflict events anyway.
- Running gates in the daemon process or the keepalive: no session `Config`
  there, so the command would run with the daemon's environment.

## 7. Limits

| Limit                    | Value                                            |
| ------------------------ | ------------------------------------------------ |
| Gate timeout             | 60 s; a timeout is a failure                     |
| Delivered output         | first 16 KiB of stdout; truncation is noted      |
| Failure notice           | last 20 lines of stderr, 2 KiB                   |
| Concurrency              | one gate run per task; an overlapping slot skips |
| Failure reporting        | once per streak; counted in `gateStatus`         |
| Catch-up for quiet fires | none; the next slot runs the probe again         |

## 8. Risks

- A probe that prints on every run (no cursor) turns the gate back into a
  model-driven loop. The probe contract and the probes shipped in step 2 keep
  their own cursors; `cron_list` shows the delivered count so the user can see
  it.
- A gate that hangs holds its slot for 60 s and skips the slots in between.
  Probes should finish in seconds; the timeout and the in-flight skip bound
  the damage.
- Gate output is attacker-influenced text (comment bodies, PR titles) placed
  in the turn. The wrapper marks it as data; step 2's probes label third-party
  fields explicitly; the fire cannot approve a pending permission.
- An older binary reading a gated task file: fail-closed through the fuse,
  with a confusing but safe message.

## 9. Validation

Unit tests:

- `cronScheduler.gate.test.ts`: quiet, delivered, failed, blocked and
  no-runner outcomes; composed prompt text; in-flight skip; a job deleted
  while its gate runs; `stop()` aborting a gate; a later `start()` receiving
  the output of a gate that was mid-run; a final fire counted in `sessionSize`
  until its gate settles and the skipped-settlement listener; a reload that
  disables, removes or rewrites the task aborting its gate; a gated catch-up
  stamped at once and booked only on delivery; `gateStatus` and the run ring
  for durable tasks; missed carriers never gated; `forceFireJob` gated.
- `cronTasksFile.test.ts`: `gate` and `gateStatus` round trip; the fuse is
  written and cleared with the gate; `taskHasLegacyCondition` with and without
  `gate`.
- `cron-create.gate.test.ts`: `exec` confirmation details and `Monitor(...)`
  rules; classifier input; a bare `cron_create` rule does not cover a gate in
  default mode nor in auto mode, where it skips the classifier; durable
  creation carries the gate. `cron-list.test.ts`: gate and status line.
- The gate runner (`cron-gate.test.ts`): environment, cwd, timeout, output
  caps cut on a character boundary, binary output failing, sanitization, the `monitor` permission evaluation per approval mode,
  a deny rule blocking in yolo and auto mode.
- `use-llm-stream.test.tsx`: cron fires are never routed to shell mode.
- `nonInteractiveCli.test.ts`: a headless run exits once the final fire of a
  gated job settles quietly, holds open for a durable gated catch-up until
  its gate delivers, and exits when that catch-up's task is deleted or
  disabled on disk while its gate runs.
- `scheduled-task-run.test.ts`, `scheduled-tasks.test.ts` and
  `ScheduledTasksDialog.test.tsx`: a manual run of a gated task asks the model
  to run the gate first, for `per_run` tasks (daemon route) and persistent
  tasks (Web Shell); the task view carries `gate` and `gateStatus`.
- Daemon (PR 1b): REST accept, clear and capability; current-session creator
  threading; Web Shell field and card line.

Integration: `integration-tests/cli/cron-tools.test.ts` with
`QWEN_CODE_TEST_CRON_FAST` and a gate script that prints on its second run.

E2E plan: `.qwen/e2e-tests/2026-10-21-scheduled-task-gate.md` — an
interactive TUI watch on a sandbox repository (quiet polls produce no turn; a
pushed comment wakes the session once) and a `qwen serve` daemon watch with a
Web Shell-created gated task across a daemon restart.

## 10. Acceptance criteria

- A gated task whose gate prints nothing produces no model turn, no queue
  entry and no transcript record, in the TUI, ACP, headless and a daemon-bound
  session.
- A gate that prints output wakes the session exactly once per fire, with the
  output after the prompt and marked as data.
- A failing gate is reported once per streak and never runs the task prompt.
- A gate proposed by the model is confirmed like a `Monitor` command; a gate
  that may not run unattended is blocked with the rule to add, never run.
- A durable gated task survives a restart of the CLI or the daemon with its
  gate and status intact; an older binary never fires it unconditionally.
- Deleting or disabling a task while its gate runs delivers nothing.

## 11. Delivery

1. **PR 1a** (this design): `CronScheduler`, `cronTasksFile`, the gate runner,
   `cron_create` / `cron_list`, the TUI shell-intent fix, the headless
   hold-open, the manual-run prompt for gated tasks (daemon route and Web
   Shell "Run now", since a tool-created durable gated task is already
   visible there), user documentation.
2. **PR 1b**: daemon REST routes, current-session creator threading,
   `scheduledTaskGate` capability, Web Shell form and card.
3. **Step 2**: probes — `qwen autofix-pr snapshot --gate` (continuing
   PR #15057 with a surfaced-event record and check-rollup paging) and a
   repository-level probe for opened and pushed PRs with author, draft, label
   and review-request filters.
4. **Step 3**: skills — `/autofix-pr` (`--once`, then watch mode) and the
   reviewer watch that runs `/qreview` or a verification pass per event.
5. **Separate design — managed automations**: a `gate` on the managed
   schedule record (TypeScript and Java validators, digest, DTOs, OpenAPI,
   contract fixtures, a `ma_schedule` migration), a Runtime "gate probe"
   operation run from `fire_run` before the claim with a derived durable
   identity, `skipped/gate_quiet` and `skipped/gate_failed` occurrences with a
   failure streak, definition-time approval, and FG11-style fault gates for a
   lost reply, a crash and an unknown outcome.

## 12. Open questions

- Auto mode after a restart: the fire-time check allows gates in auto mode
  without the classifier, because the task was either classified at creation
  or written by the user. Should blocked gates in default mode instead ask the
  classifier once per process?
- Daemon economics: with gates, a watched PR's bound session could be unpinned
  and its gate run by a daemon-level ticker that loads the session only to
  deliver. That needs a ticker, a bridge-to-child fire method and an explicit
  environment; it is not needed for correctness.
- Should `/loop <prompt>` offer a gate when the prompt is a check ("check the
  build")? Deferred until the probes exist.

