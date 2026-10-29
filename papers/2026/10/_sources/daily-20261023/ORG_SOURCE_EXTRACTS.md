# 必要固定版本原件 / patch 摘存

通过官方GitHub fetch恢复。只保存已读必要文件/patch，不表示全repo或本地测试已核。

## MiMoRetry

---
feature: retry-record-part
status: delivered
updated: 2026-10-22
source: https://github.com/XiaomiMiMo/MiMo-Code/pull/2703
---

# Retry Record Survives Until The Turn Succeeds

## Report

**What was built** — Every retry of an assistant step (request ladder, stream policy, auto-resume after tools) upserts one `retry` part on that assistant message, for the main agent and every subagent. The part carries the attempt count, phase, scope, kind, reason, hostCode and next-attempt time. It survives retry cleanup and empty-turn resets, and a record on a dropped empty step moves to the next step of the same user turn. It is removed only at the run loop's success exits (final answer, structured-output capture) for the user turns the run completed; failed, aborted, interrupted and compaction-stopped turns keep it. It never reaches the model. History indexing and export read the new shape. While a step is failing (a retry was recorded and no attempt has produced output since), a newer input in the actor's inbox lane supersedes the step: the retry wait or the hanging attempt ends, the step keeps only its record, and the run loop claims the input at its next step within the same run.

**Verification** — `bun run typecheck` PASS. `bun test test/session/invalid-output-continuation.test.ts test/session/structured-output-retry.test.ts test/session/message-v2.test.ts` PASS (includes main and subagent mid-turn records, success clearing, cancel and cancel-between-steps keeping, bounded exhaustion keeping, queued-prompt clearing, structured-output clearing, request-phase provider errors recovering with the desktop e2e retry config, model context exclusion, and supersede by a new input during a hanging retried attempt, during a request-phase wait, at the first retry of an input that arrived earlier, and on a subagent lane). The supersede cases run against one-minute retry delays and finish within seconds. `bun test test/inbox test/session test/actor`: 1779 pass; the failures are 5-second timeouts under full-suite load and pass in isolation, except one `prompt-effect` MCP test that passes or fails around its 5-second limit with no retry involved. Three independent review rounds on the record; the last found only MINOR items, all addressed. The retry-safe stream-failure case is covered by an attempt that streams reasoning and then an `upstream_error` frame: the record survives with attempt 2 and the dropped attempt's reasoning does not remain.

**Journey log** —
1. Clearing on every run exit was wrong: an interrupted turn whose last assistant finished with `tool-calls` looks successful by message state alone. Clearing moved to the run loop's explicit success exits.
2. Compaction returns the same `stop` for success and failure, so it is not a success signal.
3. `Log.create` caches by service name, so per-processor tags overwrite each other; processor log lines can carry another session's IDs.
4. Inbox inputs are claimed only at the top of the run loop, and a persistent retry stays inside one step, so a failing step has to give way to an input explicitly (S2.6).
## [S1] Problem

Retries are only visible through `session.status{retry}` and the `session.retry.attempt` bus event. The processor sets status back to `busy` on the retried stream's first `start` frame, before any content arrives, so the reconnect row disappears while the retried request may still produce nothing for many minutes. Status is session-wide and only the main agent writes it, so subagent and `checkpoint-writer` retries are never visible. Nothing is persisted: a refresh, session switch or restart during a retry shows a plain "processing" turn.

`MessageV2.RetryPart` is declared in the part union but no code writes it.

## [S2] Design

### S2.1 Part shape

`RetryPart` becomes the durable retry record of one assistant message:

```ts
{
  type: "retry"
  attempt: number          // latest attempt number for this assistant message
  phase: "request" | "stream"
  scope: "request" | "live-step"
  kind: RetryKind          // network | rate_limit | server | stream | unknown
  message: string          // decision.message, same text as session.status{retry}
  hostCode?: string
  next: number             // epoch ms of the next attempt
  time: { created: number; updated: number }
}
```

The unused `error: APIError` field is removed. The SDK types are regenerated; regeneration also picks up `UserMessage.task_id`, which the committed SDK was missing relative to the current schema. History indexing (`history/projection.ts`, `history/extract.ts`) and export redaction read `message` instead of the old error.

### S2.2 Writing

- Every retry notification for an assistant message upserts one retry part on that message: the processor's stream-phase `SessionRetry.policy` `set` callback, the request-ladder `onRetryStatus` callback, and the auto-resume-after-tools retry in `processor.ts`. One part per message, keyed by a part ID held in the processor context; later retries update `attempt`, `message`, `hostCode`, `next` and `time.updated` in place.
- It is written for every actor (main, subagents, `checkpoint-writer`, compaction). `session.status{retry}` and `Session.Event.RetryAttempt` keep their current behaviour for the main agent; `session.status` keeps its own session-level attempt count, while the part counts attempts of its assistant message.
- Max-mode candidate/judge retries do not write a part (they are not the user-visible step).

### S2.3 Surviving retry cleanup

- The retry part ID is never pushed to `ctx.stepPartIds`, so the `tapError` cleanup of a retry-safe failed attempt keeps it.
- The empty-turn reset (`processor.ts`, empty/think-only branch) removes every part of the message except retry parts.
- When `runLoop.dropEmptyAssistant` deletes a stale empty assistant, its retry part is carried to the next step's assistant of the same run when that assistant answers the same user message, so the count stays visible. If the run ends before such an assistant exists, the carried record is written back onto the newest assistant of that user turn on exit.
- A successful retried attempt does not remove the part; it stays visible above the recovered content until the turn ends.

### S2.4 Clearing

- Clearing happens only at the run loop's two success exits: the existing-assistant `final` classification and the structured-output capture. It runs after the goal gate and subagent wait, so a turn that re-enters keeps its records until it really ends.
- It removes every retry part of the actor whose assistant answers the run's first real user message or a later one (synthetic re-entries and queued prompts admitted into the same run belong to the completed work). The run's first real user message is the newest non-synthetic user message at or before the run's first `lastUser`, so a run resumed on a synthetic re-entry still covers its real turn. Retry parts are selected by one query filtering part type, actor, assistant role and `parentID` in SQL, without loading the slice.
- Failure, abort, interruption (including cancellation between steps, when the last assistant finished with `tool-calls` and no error), compaction stop (compaction reports success and failure with the same `stop`), text-loop give-up and blocked permission exits do not clear, so the turn still shows how often it retried.
- A later successful resume of the same turn clears them by the same rule.
- A step superseded by a newer input (S2.6) holds nothing but its record; clearing removes that empty assistant together with the record.

### S2.6 A newer input supersedes a failing step

Inbox inputs (steers, queued prompts, actor notifications) are claimed only at the top of the run loop. A persistent retry stays inside one step, so without this rule an input waits for the whole retry chain.

- The run loop gives each step's processor an `awaitNewInput` effect that completes once the actor's lane holds an accepted input no run has claimed (`listAccepted` checked on every `observeInput` revision).
- The processor tracks `retrying`: set when a retry part is recorded, cleared by the first `reasoning-start`, `text-start` or `tool-input-start` of an attempt. A step is failing while `retrying` is set. An attempt that produces output is processing again and is not superseded.
- The retried stream races a watcher. Once the input waits, the watcher wins at once if the step is failing, otherwise at the next recorded retry. The win interrupts the request-ladder sleep, the stream-policy backoff or the hanging attempt. The interruption is not a user abort: no `AbortedError` is written and no tool runs, since a failing attempt has produced no tool call.
- The superseded step removes its attempt's parts, keeps the retry part, clears `finish` and `error`, and is stamped `time.completed` so the orphan sweep never aborts it. Main sets `session.status` back to `busy`. `process()` returns `superseded`, and the run loop continues to its next step in the same run, where it claims the input. The record stays visible before the input until the run succeeds or ends without success.
- Compaction creates its processor without `awaitNewInput`, so a compaction step is never superseded. Max-mode candidate and judge retries are not the user-visible step and are not superseded.

### S2.5 Model context

`toModelMessages` never converts retry parts, and an assistant message whose parts are only structural (step markers, retry, empty text/reasoning) is skipped. A test locks this.

## [S3] Out of Scope

- Desktop rendering of the part is a Desktop change (turn-execution RUN-R7).
- `session.status{retry}` semantics, including the `start`-frame reset to `busy`, are unchanged; Desktop renders from the part instead.
- No retry part for max-mode candidate/judge scopes.

## Tasks
- [x] T1: Reshape `RetryPart` and regenerate the SDK — acceptance: typecheck passes with the S2.1 shape and the old `error` field gone (covers: S2.1)
- [x] T2: Write the retry part from stream and request retries for every actor — acceptance: integration test with two empty stops then text shows one retry part with `attempt` 2 and the empty-output message on the main assistant before the turn ends; a subagent run shows the same on its own assistant (covers: S2.2; depends: T1)
- [x] T3: Keep the part across cleanup — acceptance: after the empty-turn reset and a retry-safe stream failure the part still exists and no other residue survives (covers: S2.3; depends: T2)
- [x] T4: Clear on turn success, keep on failure/abort — acceptance: successful turn leaves no retry part; a structured-output turn and a turn whose recovered attempt streamed while a prompt was queued are cleared; cancelled turn keeps it with the last attempt; a turn cancelled between tool steps keeps it; bounded-exhausted turn keeps it next to the terminal error (covers: S2.4; depends: T2)
- [x] T5: Lock model context — acceptance: a request built from a history containing retry parts contains no retry content and no message created only from them (covers: S2.5; depends: T1)
- [x] T6: Verify — acceptance: repo typecheck and affected session/actor/server suites pass, results recorded (covers: S2; depends: T2, T3, T4, T5)
- [x] T7: Supersede a failing step with a newer input — acceptance: with one-minute retry delays, a prompt sent during a hanging retried attempt, during a request-phase wait, or before the first failure runs in the same turn within seconds; the next request carries both prompts; the superseded step shows only its record (completed, no error) until success, then is removed; the same holds on a subagent lane; a prompt queued after the recovered attempt produced text waits for that attempt (covers: S2.6; depends: T2, T4)


## MiMoBoundary

---
feature: lossless-session-db
status: in-progress
updated: 2026-10-21
branch: feat/lossless-session-db
commits: 4e58a80184..e5954afaa8
---

# Lossless Session DB

## Report

**What was built** — No code path rewrites a persisted part to shrink context any more. Turn-end prune and `stripNonEssential` are gone from `session/prune.ts` together with their call in `session/prompt.ts`; the uncalled `SessionCompaction.prune`, the rebuild-time microcompact in `insertRebuildBoundary`, `pressureLevel` / `contextPressureLevel`, `Flag.MIMOCODE_DISABLE_PRUNE` and the `compaction.prune` config key are removed. `fireCheckpoints`, the threshold functions and `resetThresholds` are unchanged.

A config that still contains `compaction.prune` loads normally: `normalizeLoadedConfig` drops the key and logs one warning, the mechanism already used for `auto_worktree`. Legacy rows that carry `time.compacted` keep rendering the cleared marker, and `history get` returns their stored text. The generated SDK type loses `compaction.prune`.

The rebuild boundary is appended after the newest message (S2.6). `insertRebuildBoundary` reads the tail from the database at insert time, digests it up to the last assistant message, copies the unanswered user messages at its end onto the boundary in full, and records undelivered queued inputs as `deferredInputs` instead of digesting them. `collapseCheckpointTail` applies only to legacy boundaries. The checkpoint writer and the runLoop's turn state read the window with the tail restored (`readRebuildTail` / `withRebuildTail`); the runLoop also places deferred inputs that ended undelivered after the boundary (`withEndedInputs`). `recovery` and resume do not treat a rebuild boundary as a turn. The closing reminder is the loop reminder after a tool step and nothing after a finished reply. The generated SDK type gains `CheckpointPart.deferredInputs`.

**Verification** — From `packages/cli`: `bun typecheck` PASS; `packages/sdk` `bun run typecheck` PASS. The rebuild, checkpoint, fork, threshold, writer, reminder, prune, resume, recovery and overflow test files with `server/session-recovery` and the TUI status tests: 51 files, 514 pass / 0 fail after rerunning `plan-reminder-dedup` alone. Every new test for T6–T11 was run on the commit before its change and failed there for the intended reason. Full `bun test` on the final head: 6131 pass / 77 fail / 41 skip; every failing file (MCP, project, worktree, migrate-global, llm-server tokens, tool-fail-cascade, tool-gate-cancel) passes when run alone except one `prompt-effect` MCP reminder test that exceeds its 5 s limit only under load and passes alone in about 2 s — PRE-EXISTING test interference and timing.

**Journey log**
- `compaction.prune` was opt-in on the base commit (unset meant off) and the test preload isolates XDG config, so a regression test for the old prune path must write `compaction.prune: true` into the fixture's `mimocode.json`; the first version of the T1 test omitted it and passed on base.
- Removed config keys are stripped in `normalizeLoadedConfig` because the config schema is strict.
- Proving a test fails on base: copy it into a detached worktree at the base commit with `node_modules` symlinked, run the file, then remove the worktree.
- The full `bun test` run takes about 34 minutes and shows about 79 failures from interference between test files that do not reproduce per file. Under heavy machine load it takes up to 52 minutes and more files fail on 5 s timeouts; rerun each failing file alone.
- Moving the boundary to the end made it the runLoop's newest user message, which also drives turn state, resume and recovery; every reader that inferred the turn from the window needed the restored tail.
- Automatic rebuild sites hold a window read before their current step, so the tail must be read at insert time.
- Inbox receipt state cannot tell an input a rebuild skipped from one that had already ended, so the boundary records the skipped ids, and only the newest boundary's record is read.

## [S1] Problem

References cite symbols in `packages/cli/src`.

The session database (`PartTable`) is the only copy of a conversation, but three code paths rewrite tool output in place:

- Turn-end `prune` in `session/prune.ts`: when `compaction.prune` is explicitly `true` (unset means off, although the docs called it "default true"), the prompt cache is cold and context pressure is high, it soft-trims main-agent tool outputs over 4096 chars to head and tail, or sets `state.time.compacted`, and blanks reasoning and media through `stripNonEssential`.
- `SessionCompaction.prune` in `session/compaction.ts` sets `time.compacted`. It has no caller.
- Rebuild-time microcompact in `insertRebuildBoundary` (`session/checkpoint.ts`) sets `time.compacted` on read/bash/grep/edit outputs after the boundary.

A compacted output renders as `[Old tool result content cleared]` in `toModelMessages` (`session/message-v2.ts`), and `history get` (`history/service.ts`) returns the rewritten data. Anything the model or the user later needs to recover from the session (a test log, a grep hit, a reasoning step) may already be gone, so neither `history get` nor a script reading the database can serve as a source of truth.

The rebuild boundary is also placed in the middle of the conversation. `insertRebuildBoundary` gives the boundary message `time.created` = the watermark message's time + 1 ms, so the tail (the messages between the writer's watermark and the newest message at insert time) sorts after the boundary. `filterCompacted` walks from the newest message back to the newest boundary, so the tail stays in every later window, and every request then filters it again with `collapseCheckpointTail` (non-user tail messages dropped, user tail messages kept live) to avoid sending it next to its `# Recent activity` digest. The digest is generated once and stored on the boundary; the per-request filter only exists because of the boundary's position.

## [S2] Design

### S2.1 Invariant

After this change no code path mutates the content of a persisted part to reduce context size. Parts are only appended or updated by their own lifecycle (streaming, tool state transitions). Context size is controlled exclusively by window boundaries (checkpoint rebuild boundaries and compaction boundaries).

### S2.2 Removals

- `session/prune.ts`: the turn-end `prune` effect, `stripNonEssential`, their `Interface` members, and the turn-end `prune.prune` call in `session/prompt.ts` with the variables that only feed it. `fireCheckpoints`, threshold resolution (`defaultThresholdsFor`, `parseThreshold`, `maxAllowedFor`, `resolveThresholds`) and `resetThresholds` stay unchanged.
- `SessionCompaction.prune`, its async wrapper, and the `prune` member of the compaction `Interface`.
- The rebuild-time microcompact block in `insertRebuildBoundary`.
- `Overflow.pressureLevel` and `Overflow.contextPressureLevel`, whose only consumer is turn-end prune.
- Config key `compaction.prune`, `Flag.MIMOCODE_DISABLE_PRUNE` and the config-loading code that writes the key from the flag, plus their documentation (including the bundled `mimocode-docs` config reference). Existing configs containing `compaction.prune` load with one warning; the value is ignored.
- Constants used only by the removed code (`PRUNE_MINIMUM`, `PRUNE_PROTECT`, `PRUNE_PROTECTED_TOOLS`, the soft-trim constants) once unreferenced.

### S2.3 Legacy data

`ToolStateCompleted.time.compacted` stays in the schema as an optional read-only field so existing rows parse. Rows that already carry it keep rendering `[Old tool result content cleared]`; no new row gets it. Consumers that read the field (the TUI check in `cli/cmd/tui/routes/session/index.tsx`, the skip in `session/instruction.ts`, and `collapseCheckpointTail` neighbours) keep working on legacy rows unchanged.

### S2.4 Behavioral consequence

Turn-end prune only ran for users who set `compaction.prune: true`. For them, a main session resumed after its prompt cache expired now keeps its old tool outputs and reasoning verbatim inside the current window until the next boundary, so usage crosses the checkpoint thresholds and `Overflow.usable` sooner and the existing checkpoint writer and rebuild run earlier. With the default configuration nothing changes at turn end. Subagents are unaffected (turn-end prune only read main-agent messages). Removing the rebuild-time microcompact does not change any request: after S2.6 the tail it used to clear is outside every window, and only the checkpoint writer reads it, in full. No trigger, threshold or ratio changes.

### S2.6 Rebuild boundary at the end of the conversation

**Placement.** `insertRebuildBoundary` creates the boundary message after the newest main-agent message of the session: `time.created` is the insert time, or that message's `time.created` when the clock reads earlier, and the id is ascending as before. It reads the tail from the database at insert time, because its callers hold a window read before their current step: the main-agent messages after the writer's watermark, without earlier boundaries and without queued inputs (below). Its inputs are the session, the watermark, agent and model only (`boundaryCreatedAt`, `digestUpTo` and `lastMessageInfo` inputs and the code in `rebuildFromCheckpoint` that computed them are removed). `CheckpointPart` keeps its fields and gains the optional `deferredInputs` (below): `coveredUpTo` = the writer's watermark, and `digestUpTo` = the last tail message before the unanswered user messages at its end, written whenever there is one (not only when the activity digest rendered lines). The closing reminder of the rebuild context is chosen from the last tail message.

**Unanswered and queued input.** User messages at the end of the tail, after its last assistant message, have not been answered yet. They are neither digested nor quoted: their text parts (including the text read from attached files) are copied onto the boundary in full as synthetic text parts with their metadata, and their file parts are copied as they are, after the rebuild context. Inputs the inbox has accepted or claimed but not yet delivered to a model step (no `delivery_message_id`) are not part of the tail at all: they are left out of the digest, the copies and `Recent user input (verbatim)`, the ids of all inputs still undelivered at insert time (including ones an earlier boundary left out) are recorded on the boundary's `CheckpointPart` as `deferredInputs`, and they reach the model as their own user messages through the runLoop's pending-input path, which also records their delivery. A recorded input whose receipt later ends without delivery (cancelled by stop, swept on restart, rejected) is visible again like any such input outside a rebuild: the runLoop places it right after the boundary. An input whose receipt had already ended before the rebuild is part of the tail like any other user message.

**Model view.** `filterCompacted` stops at the boundary, so no tail message enters a later window. The tail is represented only by content stored on the boundary at insert time: the `# Recent activity` digest (`renderTailDigest`, unchanged), the `Recent user input (verbatim)` section, which quotes the newest main-agent user messages from the database except the copied and queued ones, and the copied unanswered user messages. Messages created after the boundary stay live.

**Per-request filter.** For a boundary placed this way, `collapseCheckpointTail` has nothing to remove: its range lies before the boundary, outside the window. It stays for legacy boundaries, whose message sorts before the end of its range, and is applied only to them. Detection uses only stored data: a boundary is legacy when its message's `time.created` is earlier than the `time.created` of the message `digestUpTo`.

**Reminders.** Synthetic reminders persisted once per user message (MCP readiness and repeated-step reminders, marker-deduplicated) and the plan reminders that `insertReminders` adds lived on the newest user message, which was often a tail user message. After S2.6 the newest user message in the window is the boundary, which carries none of those markers, so the existing reminder insertion attaches them to the boundary or a later user message. The memory paths reminder goes on the first own user message of each context window, which after a rebuild is the boundary. The skill catalog is not affected: it is sent in the system prompt, and catalogs persisted on user messages by older versions are skipped when rendering. No new reminder logic is added.

**Turn state.** The runLoop reads the state of the current turn (the resume parent, the last user message whose settings drive the step, the last and last finished assistant messages) from its window, and the `session.userQuery.pre` hook reads that user message's text. When the newest user message in the window is a rebuild boundary, the turn's user message and steps are in the boundary's tail, so the loop reads that state from the window with the tail restored between the boundary and the later messages, the same list the checkpoint writer receives; the tail is read once per boundary, and the model request is still built from the window alone. A rebuild after a finished step therefore ends the turn without another model call, and a rebuild after a tool step or before an unanswered user message continues under the turn's own user message. A loop-streak crop span is stored on that user message when the window holds it, else on the boundary.

**Recovery and resume.** A rebuild boundary is not a resumable user: `recovery` offers the newest user message that is not a rebuild boundary when only rebuild boundaries follow it, so a rebuild after a finished turn offers nothing and an unanswered user message carried by a boundary is offered and resumed as itself. An interrupted assistant message is offered only when nothing follows it, so one inside a rebuild tail is not offered: its context is no longer in the window. The resume admission checks do not count a rebuild boundary after the parent as a later user message, and a resume whose parent is the boundary itself is checked against the window.

**Closing reminder.** A tail that ends in a tool step gets the loop reminder (below). A tail that ends in a finished reply or a user message gets none: the next request is the user's. An empty tail (the watermark is the newest message) takes the reminder from the newest message.

**Checkpoint writer input.** The writer deliberately reads full-fidelity history: `buildLLMRequestPrefix` is called without `collapseCheckpointTail` for fork capture (`llm-request-prefix.ts`). Before this change it got the tail because the tail stayed in the window. `tryStartCheckpointWriter` now builds its message list as: the window up to and including the newest rebuild boundary, then the stored messages between that boundary's watermark and the boundary (the same tail as at insert time, unanswered user messages included) that the window does not already hold, in stream order, then the messages after the boundary. A legacy boundary's tail is already in the window, so nothing is added. Copied unanswered user messages therefore reach the writer twice, on the boundary and in the tail. This reproduces the list the writer saw before (boundary, tail, live messages), so `computeBoundary`, the fork:false delta and `last_checkpoint_message_id` behave as before.

**Mid-loop rebuild.** An automatic rebuild between steps of a tool loop finishes the current step first, so that step is the newest message and the last message of the tail; the digest lists its tool calls and marks tool parts that were still pending or running as interrupted, as today. Its tool outputs reach the model only through the digest, so the closing reminder for a tail that ends in a tool step tells the model that the outputs are not in context and that it can re-run a call.

### S2.5 Testing boundary

- Real sessions on the scripted test provider; no mocked services.
- A main session with the legacy `compaction.prune: true` opt-in, driven past the old prune conditions (cache cold, usage in the former level-2 band, large tool outputs older than two turns), keeps every `PartTable.data` identical to what the tool returned, and reasoning parts unchanged.
- A checkpoint rebuild leaves outputs after the boundary identical in the database.
- `history get` on any tool part returns the full stored output through paging.
- A legacy row with `time.compacted` still renders the cleared marker.
- Existing tests that assert prune or microcompact behavior are deleted together with the code they test; tests of `fireCheckpoints` and thresholds keep passing unchanged.
- After a rebuild in a session with a non-empty tail (assistant text, tool calls with large outputs, and a tail user message), the boundary message sorts after every tail message; the next request contains the boundary and no tail message, carries the tail user text through `Recent user input (verbatim)` and the tail tools through `# Recent activity`; a message sent after the rebuild is live in the following request.
- A legacy boundary fixture (boundary time = watermark + 1 ms) renders the same request as before, with its tail collapsed.
- A checkpoint writer started after such a rebuild receives the tail messages in full (tool outputs intact) between the boundary and the live messages.
- The memory paths reminder of the new context window is persisted on the boundary and appears in the first request after the rebuild.
- An automatic rebuild after a finished high-usage reply digests that reply and ends the turn without another model call.
- An automatic rebuild after a tool step digests that step (`digestUpTo` is the step), the next request contains only the boundary with the step's calls in `# Recent activity` and no tool output, and the reply to it belongs to the turn's user message and ends the turn.
- A rebuild whose tail ends in an unanswered user message (long text over the verbatim cap, an attached text file) and with a queued undelivered input: `digestUpTo` is the last assistant message; the boundary carries the full text and file content of the unanswered message, `Recent user input (verbatim)` does not quote it, and nothing of the queued input; the next request carries the full text in the boundary and the queued input as its own user message.
- A queued input left out of a rebuild and then cancelled appears in the next request after the boundary, and `recovery` offers it. An input cancelled before the rebuild is part of the tail and does not appear after the boundary. An input still queued across two rebuilds and cancelled after the second appears in the next request.
- After a rebuild of a finished turn `recovery` offers nothing; after a rebuild that carries an unanswered user message, `recovery` offers that message and resuming it answers under it.
- A tail that ends in a finished reply gets the same rebuild context as one that ends in a user message.

## [S3] Out of Scope

- Changing checkpoint thresholds, the overflow trigger ratio, or adding new window-switch triggers.
- Changing summary compaction, the checkpoint writer's prompt, or the format of the `# Recent activity` digest.
- Migrating or restoring outputs that were already cleared before this change.
- History index kinds (`history/extract.ts`).

## Tasks

- [x] T1: Remove turn-end prune, `stripNonEssential`, their interface members and the `prompt.ts` call site — acceptance: a regression test drives a main session whose config carries the legacy `compaction.prune: true` past the former prune conditions, fails on the base commit, and after the change asserts every tool part's stored output and every reasoning part equals what was originally stored and that the session still reaches the existing checkpoint threshold when usage crosses it (covers: S2.1, S2.2, S2.4, S2.5)
- [x] T2: Remove `SessionCompaction.prune`, its wrapper and interface member, and unreferenced prune constants — acceptance: `bun typecheck` passes in `packages/cli` with no remaining reference (covers: S2.2)
- [x] T3: Remove rebuild-time microcompact from `insertRebuildBoundary` — acceptance: a test inserts a rebuild boundary over a session with read/bash outputs after the watermark and asserts those parts are unchanged in the database (covers: S2.1, S2.2, S2.5)
- [x] T4: Remove `pressureLevel`, `contextPressureLevel`, `compaction.prune`, `MIMOCODE_DISABLE_PRUNE` and the flag-to-config code with docs — acceptance: a config containing `compaction.prune` loads with exactly one warning and no error; no reference to the flag or the key remains outside the warning; typecheck passes (covers: S2.2)
- [x] T5: Keep legacy `time.compacted` rows rendering — acceptance: a test with a pre-existing row carrying `time.compacted` still renders `[Old tool result content cleared]`, and `history get` returns the stored text (covers: S2.3, S2.5; depends: T1)
- [x] T6: Capture a golden fixture of the request rendered after a legacy rebuild boundary (boundary time = watermark + 1 ms, collapsed tail) before changing placement — acceptance: a committed test asserts the current rendered model messages for that fixture and passes on the base of this task (covers: S2.6)
- [x] T7: Place the rebuild boundary after the newest message, write `digestUpTo` for every non-empty tail, remove `boundaryCreatedAt`, and apply `collapseCheckpointTail` only to legacy boundaries — acceptance: the S2.5 rebuild test (boundary after every tail message; next request has no tail message, has the tail user text and tool digest; a later message is live) fails before the change and passes after; the T6 fixture still passes; the reminder test passes (covers: S2.4, S2.6; depends: T6)
- [x] T8: Feed the checkpoint writer the boundary's tail from the database — acceptance: a writer started after a T7 rebuild receives, in order, the boundary, every tail message with its full tool output, and the live messages; it fails before the change and passes after; existing writer, fork and threshold tests pass (covers: S2.6; depends: T7)
- [x] T9: Read the tail end from the database at insert time and read turn state through the restored tail — acceptance: the two automatic-rebuild tests of S2.5 (finished reply: three model calls, the reply digested; tool step: `digestUpTo` is the step, the next request is the boundary alone without tool output, the reply's parent is the turn's user message) fail before the change and pass after; the T6 fixture and the T7/T8 tests still pass (covers: S2.5, S2.6; depends: T8)
- [x] T10: Copy unanswered tail users onto the boundary, keep queued inputs out of the tail, treat rebuild boundaries as non-turns in recovery and resume, read turn text and crop anchors through the restored tail, drop the closing reminder after a finished reply — acceptance: the S2.5 tests for unanswered and queued input, for recovery and resume after a rebuild, and for the closing reminder fail before the change and pass after; the T6–T9 tests and the resume tests in `prompt-effect` still pass (covers: S2.5, S2.6; depends: T9)
- [x] T11: Record the queued inputs a rebuild leaves out as `deferredInputs`, place those that ended without delivery after the boundary, and keep interrupted assistants inside a rebuild tail out of `recovery` — acceptance: the S2.5 tests for an input cancelled after one rebuild, after two rebuilds and before the rebuild fail before the change and pass after; the T6–T10 tests still pass (covers: S2.5, S2.6; depends: T10)


## packages/core/src/mods/dispatch.ts

```diff
@@ -123,12 +123,21 @@ export class ModBudget {
   get expired(): boolean {
     return this.remainingMs <= 0;
   }
-  async lend<T>(run: () => Promise<T>): Promise<T> {
+  get lending(): boolean {
+    return this.pauses > 0;
+  }
+  pause(): void {
     if (!this.pauses++) this.left -= performance.now() - this.since;
+  }
+  resume(): void {
+    if (!--this.pauses) this.since = performance.now();
+  }
+  async lend<T>(run: () => Promise<T>): Promise<T> {
+    this.pause();
     try {
       return await run();
     } finally {
-      if (!--this.pauses) this.since = performance.now();
+      this.resume();
     }
   }
 }
```

## packages/core/src/mods/mod-worker.ts

```diff
@@ -21,7 +21,7 @@ import {
   type ModCommand,
   type ModPlugin,
   type ModReply,
-  type ModRequest,
+  type ModWorkerRequest,
 } from './types.js';
 import {
   ModBudget,
@@ -44,6 +44,7 @@ const realms: Realm[] = [];
 const calls = new Map<number, ModInvocation>();
 const commands = new Map<string, ModCommand & { plugin: string }>();
 const notifications = new Set<Promise<unknown>>();
+const guestNotifications = new Set<Promise<unknown>>();
 const hostOperations = new Map<
   number,
   {
@@ -55,17 +56,28 @@ const hostOperations = new Map<
 >();
 let serial = 0;
 let epoch = 0;
-let deadline = Infinity;
+let rootId = 0;
+let rootBudget: ModBudget | undefined;
+let toolRoot = false;
+let native: number | undefined;
+let reportedNative: number | undefined;
+let activityRevision = 0;
+let phase = 0;
+let reportedPhase = 0;
+let checks = 0;
+let lastCheck = 0;
+let executing = 0;
 let starting = false;
 let busy = false;
 let logChars = 0;
 let operations = 0;
 let pumping = false;
 let builtinTool: string | undefined;
 let surface: 'terminal' | null = null;
-const send = (reply: ModReply) => port.postMessage(reply);
+const send = (reply: ModReply, root = rootId) =>
+  port.postMessage({ ...reply, root, phase });
 const abandoned = () =>
-  Atomics.load(cancelled, 0) !== 0 || Date.now() >= deadline;
+  Atomics.load(cancelled, 0) !== 0 || rootBudget?.expired === true;
 const callAbandoned = (call?: ModInvocation): boolean =>
   abandoned() ||
   Boolean(
@@ -79,6 +91,29 @@ const assertLive = (call?: ModInvocation) => {
     throw new Error('Mod dispatch cancelled or timed out.');
 };
 
+function updateActivity(): void {
+  if (!busy || !toolRoot || !rootBudget) return;
+  const lending =
+    native !== undefined &&
+    hostOperations.has(native) &&
+    !abandoned() &&
+    !executing &&
+    !checks &&
+    !guestNotifications.size &&
+    !realms.some((realm) => realm.runtime.hasPendingJob()) &&
+    ![...calls.values()].some((call) => call.live && !call.budget.lending);
+  if (lending !== rootBudget.lending) {
+    if (lending) rootBudget.pause();
+    else rootBudget.resume();
+  }
+  const operation = lending ? native : undefined;
+  if (operation !== reportedNative || phase !== reportedPhase) {
+    reportedNative = operation;
+    reportedPhase = phase;
+    send({ type: 'activity', revision: ++activityRevision, operation });
+  }
+}
+
 class Realm {
   readonly runtime = wasm.newRuntime();
   readonly vm = this.runtime.newContext();
@@ -115,6 +150,7 @@ class Realm {
         hostCall(callId, method, JSON.parse(json)),
       );
       notifications.add(task);
+      if (method !== 'next') guestNotifications.add(task);
       void task
         .then((value) => {
           const json = JSON.stringify({
@@ -135,8 +171,10 @@ class Realm {
         })
         .finally(() => {
           notifications.delete(task);
+          guestNotifications.delete(task);
           deferred.dispose();
           kick();
+          updateActivity();
         });
       return deferred.handle;
     });
@@ -170,12 +208,16 @@ class Realm {
     status.dispose();
   }
   execute<T>(action: () => T): T {
+    executing++;
+    updateActivity();
     this.sliceDeadline =
       performance.now() + (this.notifying ? 25 : MOD_TIMEOUT_MS);
     try {
       return action();
     } finally {
       this.sliceDeadline = Infinity;
+      executing--;
+      updateActivity();
     }
   }
   pump(): void {
@@ -324,6 +366,7 @@ async function bounded(
     clearInterval(timer);
     call.live = false;
     if (call.aborted) realms[call.plugin].notify('abort', call.id);
+    updateActivity();
   }
 }
 
@@ -477,13 +520,22 @@ async function hostCall(
   ];
   const value = payload['value'];
   if (method === 'next') {
-    if (call.recovering && call.last) return call.budget.lend(() => call.last!);
-    validateInput(call.event, value, call.input);
-    const nativeInput = call.toNativeInput(value);
-    const task = call.budget.lend(() => call.next(nativeInput, frames));
-    call.last = task;
+    let task: Promise<unknown>;
+    if (call.recovering && call.last) {
+      task = call.budget.lend(() => call.last!);
+    } else {
+      validateInput(call.event, value, call.input);
+      const nativeInput = call.toNativeInput(value);
+      task = call.budget.lend(() => call.next(nativeInput, frames));
+      call.last = task;
+    }
     void task.catch(() => {});
-    return task;
+    updateActivity();
+    try {
+      return await task;
+    } finally {
+      updateActivity();
+    }
   }
   if (method !== 'command.register' && method !== 'ui.log')
     throw new Error('Mod API not supported: ' + method);
@@ -562,20 +614,42 @@ async function executeHostTool(
   } finally {
     clearInterval(timer);
     hostOperations.delete(id);
+    updateActivity();
   }
 }
 
-port.on('message', async (request: ModRequest) => {
+port.on('message', async (request: ModWorkerRequest) => {
+  if (
+    request.type === 'native' ||
+    request.type === 'host-result' ||
+    request.type === 'tool-check'
+  ) {
+    if (!busy || request.root !== rootId) return;
+    if (request.phase < phase) return;
+    phase = request.phase;
+  }
+  if (request.type === 'native') {
+    if (!hostOperations.has(request.id)) return;
+    native = request.id;
+    updateActivity();
+    return;
+  }
   if (request.type === 'host-result') {
     const operation = hostOperations.get(request.id);
     if (!operation) return;
+    if (native === request.id) native = undefined;
+    updateActivity();
     hostOperations.delete(request.id);
     if (request.error !== undefined) operation.reject(new Error(request.error));
     else operation.resolve(request.result);
     return;
   }
   if (request.type === 'tool-check') {
+    if (request.id <= lastCheck) return;
+    lastCheck = request.id;
     const operation = hostOperations.get(request.operation);
+    checks++;
+    updateActivity();
     try {
       if (!busy || !operation) throw new Error('Mod tool operation has ended.');
       assertLive(operation.parent);
@@ -589,30 +663,50 @@ port.on('message', async (request: ModRequest) => {
         operation.parent,
       )) as ModToolCheckResult;
       assertLive(operation.parent);
-      send({ type: 'check-result', id: request.id, result });
+      send({ type: 'check-result', id: request.id, result }, request.root);
     } catch (error) {
-      send({
-        type: 'check-result',
-        id: request.id,
-        error: String(error).slice(0, 4000),
-      });
+      send(
+        {
+          type: 'check-result',
+          id: request.id,
+          error: String(error).slice(0, 4000),
+        },
+        request.root,
+      );
+    } finally {
+      if (request.root === rootId) {
+        checks--;
+        updateActivity();
+      }
     }
     return;
   }
   if (busy) {
-    send({
-      type: 'error',
-      message: 'Concurrent Mod dispatch is not supported.',
-    });
+    send(
+      {
+        type: 'error',
+        message: 'Concurrent Mod dispatch is not supported.',
+      },
+      request.root,
+    );
     return;
   }
+  if (request.root <= rootId) return;
   busy = true;
+  rootId = request.root;
+  phase = reportedPhase = request.phase;
+  toolRoot = request.type === 'tool';
+  native = reportedNative = undefined;
+  activityRevision = 0;
+  checks = 0;
+  lastCheck = 0;
   builtinTool = request.type === 'tool' ? request.builtinTool : undefined;
   epoch++;
   logChars = 0;
   operations = 0;
-  deadline =
-    Date.now() + (request.type === 'end' ? MOD_END_TIMEOUT_MS : 60_000);
+  rootBudget = new ModBudget(
+    request.type === 'end' ? MOD_END_TIMEOUT_MS : 60_000,
+  );
   try {
     let result: unknown;
     if (request.type === 'load') {
@@ -709,7 +803,9 @@ port.on('message', async (request: ModRequest) => {
     hostOperations.clear();
     starting = false;
     builtinTool = undefined;
-    deadline = Infinity;
+    rootBudget = undefined;
+    native = reportedNative = undefined;
+    toolRoot = false;
     busy = false;
   }
 });
```

## packages/core/src/mods/runtime.ts

```diff
@@ -12,7 +12,7 @@ import { pathToFileURL } from 'node:url';
 import { resolveBundleDir } from '../utils/bundlePaths.js';
 import { ToolNames } from '../tools/tool-names.js';
 import type { AnyDeclarativeTool } from '../tools/tools.js';
-import { record, validateResult } from './dispatch.js';
+import { ModBudget, record, validateResult } from './dispatch.js';
 import type {
   ModToolCallInput,
   ModToolNext,
@@ -27,6 +27,7 @@ import {
   type ModLog,
   type ModReply,
   type ModRequest,
+  type ModWorkerReply,
   type ModSource,
   type ModOptions,
   type ModPlugin,
@@ -57,6 +58,14 @@ export class ModRuntime {
   private commands: Array<ModCommand & { plugin: string }> = [];
   private tools = false;
   private sequence = 0;
+  private root?: {
+    id: number;
+    native?: number;
+    idle?: number;
+    revision: number;
+    phase: number;
+    refresh: () => void;
+  };
   private tool?: {
     next: ModToolNext;
     controller: AbortController;
@@ -84,14 +93,26 @@ export class ModRuntime {
     });
     this.worker.stdout?.resume();
     this.worker.stderr?.resume();
-    this.worker.on('message', (reply: ModReply) => {
+    this.worker.on('message', (reply: ModWorkerReply) => {
+      const root = this.root;
+      if (!root || reply.root !== root.id) return;
       if (reply.type === 'host-call') this.executeHost(reply);
       else if (reply.type === 'host-cancel') {
         for (const id of reply.ids)
           this.tool?.operations.get(id)?.controller.abort();
       } else if (reply.type === 'check-result')
         this.tool?.checks.get(reply.id)?.(reply);
-      else if (reply.type === 'log') {
+      else if (reply.type === 'activity') {
+        if (
+          reply.phase !== root.phase ||
+          reply.revision <= root.revision ||
+          (reply.operation !== undefined && reply.operation !== root.native)
+        )
+          return;
+        root.revision = reply.revision;
+        root.idle = this.tool?.checks.size ? undefined : reply.operation;
+        root.refresh();
+      } else if (reply.type === 'log') {
         if (this.failure) return;
         try {
           this.log({ text: reply.text, to: reply.to }, reply.plugin);
@@ -244,8 +265,10 @@ export class ModRuntime {
 
   private executeHost(reply: Extract<ModReply, { type: 'host-call' }>): void {
     const owner = this.tool;
+    const root = this.root;
     if (
       !owner ||
+      !root ||
       owner.operations.size >= 32 ||
       owner.operations.has(reply.id)
     ) {
@@ -260,6 +283,11 @@ export class ModRuntime {
     const task = owner.tail
       .then(async () => {
         signal.throwIfAborted();
+        root.native = reply.id;
+        root.phase++;
+        root.idle = undefined;
+        root.refresh();
+        this.post({ type: 'native', id: reply.id }, root.id);
         const result = await owner.next(
           reply.input,
           signal,
@@ -288,32 +316,50 @@ export class ModRuntime {
                       }
                     }
                   });
+                  root.idle = undefined;
+                  root.phase++;
+                  root.refresh();
                   active.addEventListener('abort', abort, { once: true });
-                  this.post({
-                    type: 'tool-check',
-                    id,
-                    operation: reply.id,
-                    input,
-                    verdict,
-                  });
+                  this.post(
+                    {
+                      type: 'tool-check',
+                      id,
+                      operation: reply.id,
+                      input,
+                      verdict,
+                    },
+                    root.id,
+                  );
                 },
               );
             } finally {
               active.removeEventListener('abort', abort);
               owner.checks.delete(id);
+              root.refresh();
             }
           },
         );
+        root.native = undefined;
+        root.phase++;
+        root.idle = undefined;
+        root.refresh();
         signal.throwIfAborted();
-        this.post({ type: 'host-result', id: reply.id, result });
+        this.post({ type: 'host-result', id: reply.id, result }, root.id);
       })
       .catch((error: unknown) => {
+        root.native = undefined;
+        root.phase++;
+        root.idle = undefined;
+        root.refresh();
         if (!this.failure)
-          this.post({
-            type: 'host-result',
-            id: reply.id,
-            error: String(error).slice(0, 4000),
-          });
+          this.post(
+            {
+              type: 'host-result',
+              id: reply.id,
+              error: String(error).slice(0, 4000),
+            },
+            root.id,
+          );
       })
       .finally(() => {
         owner.operations.delete(reply.id);
@@ -322,10 +368,11 @@ export class ModRuntime {
     owner.tail = task;
   }
 
-  private post(request: ModRequest): void {
+  private post(request: ModRequest, root: number): void {
+    if (this.root?.id !== root) return;
     if (Buffer.byteLength(JSON.stringify(request)) > MOD_MAX_BYTES + 8192)
       throw new Error('Mod host message is too large.');
-    this.worker.postMessage(request);
+    this.worker.postMessage({ ...request, root, phase: this.root.phase });
   }
 
   async runCommand(
@@ -401,18 +448,51 @@ export class ModRuntime {
     )
       throw new Error('Mod request is too large.');
     let timer: ReturnType<typeof setTimeout> | undefined;
-    const cleanup = new AbortController();
+    let cancelTimer: ReturnType<typeof setTimeout> | undefined;
     let aborted = false;
+    const budget = new ModBudget(timeoutMs + 250);
+    const stop = () => {
+      this.fail(
+        new Error(
+          aborted ? 'Mod dispatch cancelled.' : 'Mod dispatch timed out.',
+        ),
+      );
+      void this.worker.terminate();
+    };
+    const root: NonNullable<ModRuntime['root']> = {
+      id: ++this.sequence,
+      revision: 0,
+      phase: 0,
+      refresh: () => {
+        if (aborted || this.root !== root) return;
+        const lending =
+          request.type === 'tool' &&
+          root.native !== undefined &&
+          root.idle === root.native &&
+          !this.tool?.checks.size &&
+          !budget.expired;
+        if (lending !== budget.lending) {
+          if (lending) budget.pause();
+          else budget.resume();
+        }
+        if (timer) clearTimeout(timer);
+        if (!budget.lending) timer = setTimeout(stop, budget.remainingMs);
+      },
+    };
+    this.root = root;
     const onAbort = () => {
       aborted = true;
       Atomics.store(this.cancelled, 0, 1);
       this.tool?.controller.abort();
+      if (timer) clearTimeout(timer);
+      cancelTimer = setTimeout(stop, 250);
     };
     Atomics.store(this.cancelled, 0, 0);
     try {
       return await new Promise<unknown>((resolve, reject) => {
         this.pending = (reply) => {
-          if (aborted) reject(new Error('Mod dispatch cancelled.'));
+          if (this.failure) reject(this.failure);
+          else if (aborted) reject(new Error('Mod dispatch cancelled.'));
           else if (reply.type === 'error') reject(new Error(reply.message));
           else if (reply.type === 'result') {
             try {
@@ -425,30 +505,17 @@ export class ModRuntime {
           }
         };
         signal.addEventListener('abort', onAbort, { once: true });
-        timer = setTimeout(() => {
-          this.fail(
-            new Error(
-              aborted ? 'Mod dispatch cancelled.' : 'Mod dispatch timed out.',
-            ),
-          );
-          void this.worker.terminate();
-        }, timeoutMs + 250);
-        signal.addEventListener(
-          'abort',
-          () => {
-            if (timer) clearTimeout(timer);
-            timer = setTimeout(() => {
-              this.fail(new Error('Mod dispatch cancelled.'));
-              void this.worker.terminate();
-            }, 250);
-          },
-          { once: true, signal: cleanup.signal },
-        );
-        this.worker.postMessage(request);
+        root.refresh();
+        this.worker.postMessage({
+          ...request,
+          root: root.id,
+          phase: root.phase,
+        });
       });
     } finally {
-      cleanup.abort();
+      this.root = undefined;
       if (timer) clearTimeout(timer);
+      if (cancelTimer) clearTimeout(cancelTimer);
       signal.removeEventListener('abort', onAbort);
       this.pending = undefined;
     }
```

## docs/design/2026-10-22-managed-session-mcp-management.md

```diff
@@ -0,0 +1,68 @@
+# Managed Session MCP management
+
+[English](2026-10-22-managed-session-mcp-management.md) | [简体中文](2026-10-22-managed-session-mcp-management.zh-CN.md)
+
+Status: design and implementation in progress. Completes the runtime-management scope of [#15079](https://github.com/QwenLM/qwen-code/issues/15079), together with [ordinary Workspace tools and MCP](2026-10-21-managed-mcp-management-reuse.md).
+
+## Problem
+
+Managed exposes a committed MCP catalog but no public management commands. Daemon management operates its own ACP process; calling those routes from Managed would change the wrong execution environment. Hosted already persists configuration and operation receipts, reconfigures connections, and drains them on close. Its private configure route is insufficient as a public API: it lacks full idle gating, only authorizes admission-time server identifiers, and does not expose a user-visible settings revision.
+
+## Version and authorization policy
+
+Keep the Session's original AgentDefinition revision and digest immutable, including Skills and approval policy. An explicit MCP command creates a new Session-local settings revision. Two Sessions in one Workspace may therefore have different MCP selections. No command follows a latest AgentDefinition or a latest recipe automatically.
+
+Only an actor with the existing Workspace execution permission may manage a visible, active public Session. Preserve creator execution grants, migration/admission checks, lifecycle exclusion, Plan refusal, snapshot-read-only emptiness and original Runtime ownership. Reading a committed catalog retains its existing read authorization. Management never falls back to a daemon primary or a local Runtime.
+
+Add and edit select an exact published server revision and digest from the selected Runtime's tenant-and-Workspace-scoped private manifest. Return only identifier, revision, digest and transport, never commands, arguments, environment, URLs, headers or credentials. Unpublished executable recipes cannot be submitted through this API. Publishing new private recipes remains deployment administration; it is not implied by Workspace permission. A fresh Session without initial MCP pins may explicitly select published servers when its ordinary shell/1 lifecycle and Harness capabilities support this feature.
+
+## Durable settings and commands
+
+Store a bounded Session-local settings snapshot in the existing registered configuration-installation journal domain. Its envelope supplies revision, operation identity and predecessor reference. The closed MCP content contains exact pins and enabled/removed state; removed entries remain tombstones so restoration can authorize historical configuration records. The bound is 32 distinct historical server identities, including removed entries, and 16 enabled servers. A server identity cannot move to a lower definition revision after removal; deployments publish a new identity when resetting a definition lineage. Admission pins are revision zero. Preserve old logs without a settings snapshot.
+
+Every command carries an actor-scoped stable operation identity and expected settings revision. A retry queries the same original command; different content under the same identity conflicts. Concurrent revisions conflict before execution. Persist requested settings before changing physical connections, then record completion with existing MCP configuration/release receipts. An uncertain original effect blocks new work and is reconciled on its original owner; it is never replayed on another Runtime. Restart recovery retains command identity across interruption between release and configure. Historical drain status examines only configurations that existed before that command's durable intent, so a later enable cannot undo a completed disable receipt. The settings append transaction rechecks Plan, Turn and lifecycle admission under the same Session lock those mutations take.
+
+The public and WebShell APIs expose a management snapshot, available published pins, management commands and command status. The management snapshot distinguishes requested settings, completed physical configuration and stale catalog metadata. It must not pick an older successful catalog's revision as the command concurrency token. Advertise capabilities so an older Harness cannot appear to support commands it does not implement.
+
+Management attaches only to a Session already resident in the current Harness. Reattaching validates its identity and returns the existing reference without cleanup, recovery or wake dispatch. After a Harness restart, continue or recover the Session through its normal execution flow before opening management; otherwise return `hosted_mcp_session_load_required`. A new Session admitted without input may create its first journal through management without submitting a Turn. Creation conflicts and unknown creation outcomes may only reattach to that same resident Session, never implicitly load a cold journal. Command status never creates a Session. A cleanup-only recovery attachment also refuses management attachment, queries and commands until an explicit ordinary execution load upgrades it; management must not initialize extensions or commit settings through that restricted attachment. The control plane caches management-only references separately from ordinary attachments; a management read cannot certify a Turn takeover or cancellation recovery. The first ordinary Turn after management initializes an empty Session performs a normal passive attachment to that resident Session before publishing its ordinary reference. Generation changes and final detach/close evict both kinds of reference.
+
+Ordinary rewind acquires a shared MCP broker through the MCP owner so that its mount bookkeeping and ordered release remain consistent. Historical Hook receipts select the original owner for cleanup, but do not alone prove a current mount hold. Pending MCP directory lookups fence only the matching Runtime Session; Workspace drain inspection retains the aggregate count. Atomic MCP settings refusals remain definite non-commits after a transport retry because the store replays an already committed command before evaluating the admission guards.
+
+## Operations
+
+| Operation | Behavior                                                                                          |
+| --------- | ------------------------------------------------------------------------------------------------- |
+| Add       | Select an exact published pin and connect it without recreating the Session.                      |
+| Edit      | Explicitly replace a selected server's published revision; preserve all unrelated selections.     |
+| Remove    | Drain that server and retain a removed tombstone; leave other servers and ordinary tools running. |
+| Disable   | Drain the server and persist its selected pin as disabled.                                        |
+| Enable    | Reconnect the exact selected pin, preserving the Session and conversation.                        |
+| Reload    | Reconfigure an enabled selected server and publish its current catalog.                           |
+| Restart   | Prove the selected old connection drained before configuring its replacement.                     |
+
+All operations refuse an active Turn, Hook, rewind, lifecycle phase, concurrent MCP command or unsettled original effect. Disabled or removed servers are absent from model declarations and resource/prompt execution. Close drains every retained physical configuration, including configurations superseded by a settings change, then releases the original shared owner once. Ordinary Shell/file history retains the established owner and backup semantics. Do not close or restart a shared worker to restart one server.
+
+## Runtime and UI reuse
+
+Reuse the existing MCP configure/release protocol and operation grants. Add only a bounded, scoped inventory read for published pin metadata. Inventory is not connection health. A successful restart requires an observed release receipt and a subsequent configuration receipt; a catalog refresh alone is insufficient.
+
+Extract small server-card, tool-schema and resource-metadata display components from the daemon manager. The daemon retains its ACP lifecycle, epochs, discovery polling and OAuth controller. A Managed manager uses its own provider commands and Session settings; do not fabricate daemon epochs, connected state or tool validation. Offer published definitions rather than a raw executable-recipe form.
+
+Make the manager accessible from the Managed Session and existing MCP management entry. Key request scopes by provider, client, Workspace and Session. Abort requests and discard late results on a target change; preserve operation identity for a retry on the original target. An explicit retry first queries the original operation, then resubmits the saved original command with the same identity only if it remains pending or requires recovery. Query failures never trigger a mutation, and refresh never resubmits automatically. When the provider has an explicit tenant-and-actor storage namespace, retain only the unconfirmed command's public pin metadata and request identity in tab session storage; clear it after terminal confirmation. Providers without that namespace retain commands only in memory. No executable recipes or credentials enter browser storage. Use shared WebShell primitives and the scoped portal root. Resource bodies and prompt expansion are not part of this management change.
+
+## API ownership
+
+| Surface                        | Owner                                                                      |
+| ------------------------------ | -------------------------------------------------------------------------- |
+| Committed catalog              | Persisted Session and Workspace read grant                                 |
+| Management commands and status | Authorized public Session, its journal writer and original Runtime owner   |
+| Published inventory            | Selected Runtime, exact tenant and Workspace; private recipes remain there |
+| Daemon manager                 | Existing selected ACP Workspace, unchanged                                 |
+
+Advance OpenAPI, regenerate WebShell types, update mapped surfaces and contract gates. No new daemon route or mutable AgentDefinition default is introduced.
+
+## Verification
+
+Dry-run the baseline using global `qwen`; record the absence of management separately from existing composition evidence. Verify the built CLI, Java service and WebShell together using disposable MySQL, two real stdio servers and a deterministic model. Exercise all operations in one Session, stable conversation identity, unchanged original definition pins, no credentials in responses, model declaration changes, disabled-state persistence after a Harness restart and cold load, idempotent retries, stale-revision refusal, isolation between Sessions and final close.
+
+Verify failed and unknown releases cannot claim restart success or start a replacement; active Turns and unauthorized actors cannot mutate. Verify empty and read-only Sessions, unsupported profiles, old logs, provider/Session switches, responsive manager controls and the existing daemon manager. Run affected package tests, root build/typecheck/bundle, Java API/surface gates, Maven verify and applicable MySQL/Hosted profiles. Inspect the complete diff twice and obtain independent review. Local process and browser evidence does not establish Linux cgroup, SSH/CSI, Windows or real upstream-provider qualification.
```
