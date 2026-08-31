#!/usr/bin/env python3
"""Resolve the two exact-v1 blockers in the 2026-05-13 Daily.

This script only updates date-local evidence, report, comparison and queue
artifacts.  It never writes shared Books.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
REPORT = REPO / "papers/2026/05/13/README.md"
sys.path.insert(0, str(REPO))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256


F1 = "SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION"
F2 = "SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA"

METHOD_1 = (
    "arXiv:2605.11378v1 HTML — §2 six-stage EvalAgent pipeline and evaluation-skill packages; "
    "Appendix A trace collection, code generation and reporting stages"
)
EVAL_1 = (
    "arXiv:2605.11378v1 — §3.1–§3.3 AgentEvalBench/meta-evaluation contract and human alignment; "
    "§4.1–§4.4 20-agent × two-requirement evaluation, Eval@1, ablations and failure analysis"
)
LIMIT_1 = (
    "arXiv:2605.11378v1 — §6 Limitations: 20-agent coverage, Claude-only backbones, "
    "62.5–65.0% first-run executability and subjective meta-evaluation; §4.4 implementation failures"
)
ART_1 = (
    "arXiv:2605.11378v1 front matter code URL https://github.com/awslabs/Agent-EvalKit; "
    "immutable commit used by the paper is Not Disclosed"
)
METHOD_2 = (
    "arXiv:2605.12129v1 PDF — §3.2–§3.7 three harness conditions, four-stage "
    "plan→execute→verify→recover pipeline, task design, TSR/VTSR/VCR and run protocol"
)
EVAL_2 = (
    "arXiv:2605.12129v1 PDF — §4–§6, Tables III–XIV: three models, 24 tasks, "
    "condition comparison, cross-model analysis and component ablations"
)
LIMIT_2 = (
    "arXiv:2605.12129v1 PDF — §7.4–§7.5: unequal T6 tool access, 24-task scope, one run per task, "
    "non-uniform timeouts, single scorer, cross-session LLaMA comparison, external rate-limit and latency overhead"
)
ART_2 = (
    "arXiv:2605.12129v1 PDF §3.7 says prompts/tasks/results/analysis are version-controlled, "
    "but no public repository, release or immutable commit is disclosed"
)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one occurrence, found {count}: {old[:120]!r}")
    return text.replace(old, new, 1)


def bounded_body(text: str, ref: str) -> str:
    start = f"<!-- {ref}:start -->"
    end = f"<!-- {ref}:end -->"
    return text.split(start, 1)[1].split(end, 1)[0]


def rp(family: str, identifier: str, method: str, evaluation: str, limitations: str, artifact: str, text: str) -> str:
    review_ref = f"review:{family}"
    claim_ref = f"claim:{family}"
    candidate = {
        "Event Identity": f"paper-v1:{identifier.split(':')[-1].removesuffix('v1')}",
        "Primary Identifier": identifier,
        "Supporting Source IDs": "SRC-ARXIV",
        "Review Override": "none",
    }
    return _expected_review_provenance(
        family,
        candidate,
        "deep",
        identifier,
        f"SRC-ARXIV@{identifier}",
        method,
        evaluation,
        limitations,
        artifact,
        claim_ref,
        review_ref,
        _normalized_body_sha256(bounded_body(text, review_ref)),
    )


text = REPORT.read_text()

# Candidate status and disposition.
old_1 = "| SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION | arXiv:2605.11378v1 | paper-v1:2605.11378 | 2026-W20 | 2026-05-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | blocked | blocked | none | review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Blocked / Unverified | — | no |"
new_1 = "| SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION | arXiv:2605.11378v1 | paper-v1:2605.11378 | 2026-W20 | 2026-05-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION | no |"
old_2 = "| SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | arXiv:2605.12129v1 | paper-v1:2605.12129 | 2026-W20 | 2026-05-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | blocked | blocked | none | review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | self | — | new_in_window | AGENT-WORKFLOW | Blocked / Unverified | — | no |"
new_2 = "| SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | arXiv:2605.12129v1 | paper-v1:2605.12129 | 2026-W20 | 2026-05-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | no |"
text = replace_once(text, old_1, new_1)
text = replace_once(text, old_2, new_2)

# Replace blocked Source Reviews with source-specific exact-v1 reviews.
start_1 = "<!-- review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:start -->"
end_1 = "<!-- review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:end -->"
review_1 = f"""{start_1}
#### An Empirical Study of Automating Agent Evaluation

问题与旧路径：人工为每个 Agent 手写 metric、trace parser 与报告，在 Agent 数量少、行为协议稳定时最可审计；直接让通用 coding assistant 一次生成评估代码则容易出现 metric proliferation、plan-code drift、无效 trace 解析以及“代码运行但指标恒定”的空洞成功。

机制与状态所有权：论文把 source code、user requirements 与执行 trace 编译为 evaluation plan、test cases、instrumentation、trace processing、可执行 metric code 和报告，并用 procedural instructions、可复用 code/template 与动态 API 文档组成 evaluation skills。这里生成器只拥有 evaluator proposal；evaluation owner 必须版本化 plan、code、dependencies、trace schema 与 report，独立 meta-evaluator/human anchor 负责 construct validity，执行 harness 负责首轮可执行且非空洞的 `Eval@1`，release owner 保留最终 authority。

全文定位：`{METHOD_1}`；evaluation=`{EVAL_1}`；limitations/counterevidence=`{LIMIT_1}`；artifact=`{ART_1}`。

收益、代价与 failure：结构化 skills 和 trace 输入可减少无关 metric 与 scope expansion，并观察静态代码看不到的 tool call、error recovery 和 decision sequence；代价是 instrumentation、trace parsing、动态依赖与 meta-evaluation 增加成本。论文自身约三分之一 evaluator 首轮不可执行，trace 虽提高语义质量却降低 executability，model judge 对 plan quality 的一致性也低于 metric relevance。

<!-- claim:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:start -->证据只支持 exact-v1 的 20 个 Agent、两类 requirement、Claude-family evaluator/backbone、预收集 trace 和作者 meta-evaluation contract。它不证明自动生成 evaluator 等同 ground truth、跨 framework 可直接执行或 production release 无需人工/可执行 verifier；低规模稳定评估继续使用人工 EvalSpec 与确定性 harness。Books Decision=`Integrate`，等待 root 串行写回。<!-- claim:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:end -->
{end_1}"""
old_block = start_1 + text.split(start_1, 1)[1].split(end_1, 1)[0] + end_1
text = replace_once(text, old_block, review_1)

start_2 = "<!-- review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:start -->"
end_2 = "<!-- review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:end -->"
review_2 = f"""{start_2}
#### It's Not the Size: Harness Design Determines Operational Stability in Small Language Models

问题与机制：raw prompt 在简单、短任务上成本最低；只增加 wrapper tags 却不增加 verifier 或 recovery，可能新增格式负担而没有新的控制回路。论文比较 model-only、minimal-shell 和 `plan→execute→verify→recover`，把 planning 视为 proactive format scaffold、把 verification/retry 视为 reactive recovery，并用 TSR、VTSR 与 VCR 区分完整成功、有效输出和 verifier 捕获。

全文定位：`{METHOD_2}`；evaluation=`{EVAL_2}`；limitations/counterevidence=`{LIMIT_2}`；artifact=`{ART_2}`。

收益、代价与 failure：四阶段 harness 在作者部分模型/任务中修复 timeout、缺步骤与可检测格式错误，但增加约 2–3 倍 inference latency；字符计数、知识边界、false pass 和外部 API failure 仍可能无法修复。minimal shell 在两个模型中低于 raw prompt，说明 harness complexity 不是单调收益。

<!-- claim:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:start -->证据仅覆盖 Windows 11/RTX 4060、Ollama v0.21.2、三款 2–3B 模型、24 个作者任务且每任务一次运行。T6 比较的 tool access 不相等，LLaMA 条件跨 session，timeout 不统一且只有单一人工 scorer，因此不能支持“harness 比模型规模更重要”的一般因果结论。第 81 章已把 harness definition、verify/recover、版本化 state、成本与 fallback 写入 Workflow 演进链；本 family 为 `No Change — Existing Coverage`。<!-- claim:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:end -->
{end_2}"""
old_block = start_2 + text.split(start_2, 1)[1].split(end_2, 1)[0] + end_2
text = replace_once(text, old_block, review_2)

# Insert Books comparisons before the Semantic Audit section.
books_blocks = f"""<!-- books-review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:start -->
<!-- existing:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已定义 EvalSpec、trace、scorer、judge 校准与 release authority，但尚未把“自动生成的 evaluator plan/code/report”作为需要独立 meta-evaluation 和 non-vacuous executability gate 的派生 artifact。Ch65 负责资源调度，Ch67 负责线上 signal，不拥有 evaluator admission。<!-- existing:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:end -->
<!-- delta:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:start -->把 evaluation skills 编译出的 plan、metric code、trace parser、dependency 与 report 绑定为 evaluator artifact；生成器只提交 proposal，evaluation owner 用 `Eval@1`、construct-validity/meta-evaluation 与人工/确定性 anchor 决定 admission。<!-- delta:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:end --> Final prewrite decision=`Integrate`；只进入 date-local queue，等待 root 串行写回。
<!-- books-review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION:end -->
<!-- books-review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:start -->
<!-- existing:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:start -->`books/part-07-agent/81-workflow.md` 已明确区分 raw/static scaffold、versioned harness definition、verify/recover、state owner、执行成本、失败回退与不同 workload 下的共存路径；`books/part-06-ai-infrastructure/66-evaluation-system.md` 也已把 harness/environment 纳入 evaluation identity。<!-- existing:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:end -->
<!-- delta:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:start -->exact-v1 提供小模型、24 个任务上的受限案例，说明 minimal wrapper 可能劣于 raw prompt，而 verify/recover 不能修复所有 constraint/tool failure；其机制与边界未改变现有 owner 判断。<!-- delta:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:end --> Final prewrite decision=`No Change — Existing Coverage`。
<!-- books-review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:end -->

"""
text = replace_once(text, "## 7. Semantic Audit", books_blocks + "## 7. Semantic Audit")

# Remove resolved Materials Requests.
text = "\n".join(
    line for line in text.splitlines()
    if not line.startswith("| MR-20260513-2605.11378 |")
    and not line.startswith("| MR-20260513-2605.12129 |")
) + "\n"

# Recompute provenance after the bounded review bodies are final.
rp1 = rp(F1, "arXiv:2605.11378v1", METHOD_1, EVAL_1, LIMIT_1, ART_1, text)
rp2 = rp(F2, "arXiv:2605.12129v1", METHOD_2, EVAL_2, LIMIT_2, ART_2, text)

old_receipt_1 = "| SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION | RP-40846ab1a258445c | deep | arXiv:2605.11378v1 | SRC-ARXIV@arXiv:2605.11378v1 | arXiv:2605.11378v1 HTML — Pending — exact-v1 paper body not retrievable; abstract identifies EvalAgent skills and trace pipeline | arXiv:2605.11378v1 — Pending — AgentEvalBench, Eval@1 and ablations require exact-v1 tables/protocol | Pending — exact-v1 limitations and artifact revision | arXiv:2605.11378v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION | blocked |"
new_receipt_1 = f"| {F1} | {rp1} | deep | arXiv:2605.11378v1 | SRC-ARXIV@arXiv:2605.11378v1 | {METHOD_1} | {EVAL_1} | {LIMIT_1} | {ART_1} | claim:{F1} | complete |"
old_receipt_2 = "| SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | RP-ae2502b3bfe78c42 | deep | arXiv:2605.12129v1 | SRC-ARXIV@arXiv:2605.12129v1 | arXiv:2605.12129v1 HTML — Pending — exact-v1 paper body not retrievable; abstract identifies model-only/minimal-shell/four-stage harnesses | arXiv:2605.12129v1 — Pending — 3 models × 24 tasks, ablations and VCR protocol require exact-v1 tables | Pending — exact-v1 limitations, task definitions and artifact revision | arXiv:2605.12129v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | blocked |"
new_receipt_2 = f"| {F2} | {rp2} | deep | arXiv:2605.12129v1 | SRC-ARXIV@arXiv:2605.12129v1 | {METHOD_2} | {EVAL_2} | {LIMIT_2} | {ART_2} | claim:{F2} | complete |"
text = replace_once(text, old_receipt_1, new_receipt_1)
text = replace_once(text, old_receipt_2, new_receipt_2)

# Project truthful Gate and reader-facing summary state.
text = replace_once(
    text,
    "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass。独立审计恢复 27 个 false negative；12 项 Books 写回已通过未参与写入者的逐项语义验收，仍有两项 exact-v1 外部材料未取得。",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。75/75 项 exact-v1 Review 已完成；原 12 项 Books 写回已通过独立验收，新恢复的 1 项 Integrate 正等待 root 串行写回与不同 reviewer 的 post-write audit。",
)
text = replace_once(
    text,
    "73/75 项完成 exact-v1 Review；两项论文正文无法取得，已形成精确 Materials Request。内容比较把 author 的 22 项 provisional Integrate 收紧并与新恢复项合并为 12 项最终写回；这些机制均已进入对应 owner 章节，并由另一 reviewer 逐项核验正文语义、相邻 owner、唯一 binding 与 `## Review notes` 前的位置。",
    "75/75 项完成 exact-v1 Review，原两项 Materials Request 已由 official exact-v1 HTML/PDF 恢复。current-Books challenge 将 2605.11378 路由为新的 `PLATFORM-EVALUATION-SYSTEM` Integrate，将 2605.12129 判为 `No Change — Existing Coverage`。原 12 项写回已通过独立验收；新增 1 项只进入 queue，尚未写共享 Books。",
)
text = text.replace("| Completion Status | Conditional |", "| Completion Status | In Progress |", 1)
text = text.replace("| Evidence Gate | Conditional Pass |", "| Evidence Gate | Passed |", 1)
text = text.replace("| Books Gate | Conditional Pass |", "| Books Gate | Open |", 1)
text = replace_once(
    text,
    "| SA-20260513-EVIDENCE | fresh-context:may2026_day02 | evidence | review:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P | none | 修正 2605.11537 locator；其余可达项完整 review，两项 external blocker 进入唯一 Materials Request | passed |",
    "| SA-20260513-EVIDENCE | fresh-context:may2026_day02 + exact-v1-recovery:may2026_day01 | evidence | review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION; review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | none | official exact-v1 HTML/PDF 恢复两项 blocker；75/75 deep Review、claim boundary 与 artifact boundary 完整 | passed |",
)
text = replace_once(
    text,
    "| SA-20260513-BOOKS | fresh-context:may2026_day03 | books | books-review:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P | none | may2026_day02 的 prewrite 比较形成 12 项最终 queue；未参与写入的本 reviewer 随后确认 12/12 机制正文、旧条件、约束变化、state/control owner、trade-off、failure、fallback、evidence boundary、唯一 binding、相邻章节 handoff 与严格二级 Review-notes 前位置均通过，详见 books-post-write-semantic-audit.json | passed |",
    "| SA-20260513-BOOKS | fresh-context:may2026_day03 + recovery-challenge:may2026_day01 | books | books-review:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION; books-review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA | FIND-20260513-RECOVERY-WRITEBACK-1 | 原 12/12 已通过 post-write audit；恢复项中 2605.11378 形成 1 项新 queue，2605.12129 为 No Change。等待 root 串行写回与不同 reviewer 验收 | open |",
)
text = replace_once(
    text,
    "12 项 Books 写回与独立 post-write semantic audit 已闭合。后续只需在取得两项 exact-v1 正文后重开对应 family 的 Evidence Review 与 Books Decision；它们不反向阻塞其余 73 个已审计 family。",
    "两项 exact-v1 blocker 已恢复并完成 Books challenge。2605.12129 无需改书；root 仅需串行写入 2605.11378 的 evaluator-artifact admission contract，并由不同 reviewer 做 owner+adjacent post-write semantic audit。",
)
text = replace_once(
    text,
    "- 更新 canonical Daily 的 counts、locators、Gate 与 Materials Request。",
    "- 恢复两项 official exact-v1，更新 canonical Daily 的 locators、provenance、Gate、Materials Request 与 Books queue。",
)
text = replace_once(
    text,
    "- 两项 exact-v1 正文能否由用户提供 bit-identical PDF/HTML/TXT？\n- 取得正文后，两项 blocker 的 exact-v1 机制、实验条件与局限是否会改变当前 `Blocked / Unverified` disposition？",
    "- 2605.11378 写入 Ch66 后，独立 reviewer 是否确认 evaluator-artifact admission 处于正确演进位置且没有与 Ch65/Ch67 争夺 owner？",
)
text = text.replace("[An Empirical Study of Automating Agent Evaluation](https://arxiv.org/abs/2605.11378v1)", "[An Empirical Study of Automating Agent Evaluation](https://arxiv.org/html/2605.11378v1)", 1)
text = text.replace("[It's Not the Size: Harness Design Determines Operational Stability in Small Language Models](https://arxiv.org/abs/2605.12129v1)", "[It's Not the Size: Harness Design Determines Operational Stability in Small Language Models](https://arxiv.org/pdf/2605.12129v1)", 1)
text = replace_once(text, "Completion Status: `Conditional`", "Completion Status: `In Progress`")
text = replace_once(text, "Evidence: `Conditional Pass`", "Evidence: `Passed`")
text = replace_once(text, "Books: `Conditional Pass`", "Books: `Open`")
text = replace_once(text, "unresolved findings: 2", "unresolved findings: 1")
text = replace_once(
    text,
    "确定性 Coverage 已闭合；12 项 Books 写回已通过独立 post-write semantic audit。两项 exact-v1 external blocker 已精确请求材料，因此 Evidence 与 Books 保持 Conditional Pass，日报 Completion 为 Conditional，而非普通工作仍未完成的 In Progress。",
    "Coverage 与 75/75 exact-v1 Evidence 已闭合；原 12 项 Books 写回已通过独立 post-write audit。恢复后的 2605.11378 是唯一普通 pending：root 尚需串行写回并由不同 reviewer 验收，因此 Books 保持 Open、Completion 为 In Progress。",
)
REPORT.write_text(text)

# Canonical ledger truth.
ledger_path = HERE / "screening-ledger-independent-final.json"
ledger = json.loads(ledger_path.read_text())
for row in ledger["identities"]:
    if row["arxiv_id"] == "2605.11378":
        row.update(review_status="deep_complete", access_status="accessible", integration_disposition="Integrate", independent_audit="exact_v1_recovered_and_books_challenged")
    elif row["arxiv_id"] == "2605.12129":
        row.update(review_status="deep_complete", access_status="accessible", integration_disposition="No Change — Existing Coverage", independent_audit="exact_v1_recovered_and_books_challenged")
ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

# Current-content comparison now covers 75/75 retained families.
comparison_path = HERE / "books-current-content-comparison.json"
comparisons = json.loads(comparison_path.read_text())
comparisons.extend([
    {
        "arxiv_id": "2605.11378",
        "source_family_id": F1,
        "owner_node": "PLATFORM-EVALUATION-SYSTEM",
        "owner_path": "books/part-06-ai-infrastructure/66-evaluation-system.md",
        "adjacent_paths": ["books/part-06-ai-infrastructure/65-kai-scheduler.md", "books/part-06-ai-infrastructure/67-monitoring.md"],
        "existing_proposition": "Ch66 已拥有 EvalSpec、trace、scorer、judge calibration 与 release authority，但未把 generated evaluator plan/code/report 作为需要 non-vacuous execution 与 meta-evaluation admission 的派生 artifact。",
        "new_evidence_delta": "Evaluation skills compile source, requirements and traces into a versioned evaluator artifact; a separate harness and meta-evaluator must validate first-run executability, non-vacuousness and construct validity before release use.",
        "decision": "Integrate",
        "reviewer": "exact-v1-recovery:/root/may2026_day01",
    },
    {
        "arxiv_id": "2605.12129",
        "source_family_id": F2,
        "owner_node": "AGENT-WORKFLOW",
        "owner_path": "books/part-07-agent/81-workflow.md",
        "adjacent_paths": ["books/part-07-agent/80-reflection.md", "books/part-07-agent/82-multi-agent.md"],
        "existing_proposition": "Ch81 已拥有 versioned harness definition、verify/recover、execution state、cost/failure/fallback 和 static/dynamic coexistence；Ch66 已把 harness 纳入 evaluation identity。",
        "new_evidence_delta": "A single-run 24-task case shows minimal wrapper tags may underperform raw prompts and verify/recover does not fix every constraint/tool failure, without changing the existing workflow contract.",
        "decision": "No Change — Existing Coverage",
        "reviewer": "exact-v1-recovery:/root/may2026_day01",
    },
])
comparisons.sort(key=lambda item: item["arxiv_id"])
comparison_path.write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")

# Preserve the 12 already accepted writes and append only the recovered gap.
queue_path = HERE / "books-writeback-queue-final.json"
queue = json.loads(queue_path.read_text())
queue["status"] = "awaiting_root_serial_writeback_and_post_write_audit_for_recovered_family"
queue["items"].append({
    "report_date": "2026-05-13",
    "arxiv_id": "2605.11378",
    "source_family_id": F1,
    "stable_node_id": "PLATFORM-EVALUATION-SYSTEM",
    "owner_path": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "adjacent_paths": ["books/part-06-ai-infrastructure/65-kai-scheduler.md", "books/part-06-ai-infrastructure/67-monitoring.md"],
    "evidence_delta": "Treat generated evaluation plans, metric code, trace parsers, dependencies and reports as a versioned evaluator artifact; require independent executability/non-vacuity and construct-validity/meta-evaluation admission.",
    "writeback_requirement": "merge into the existing evaluation-artifact/evidence spine before Review notes; preserve manual baseline, generator/evaluation/release owners, trace cost, execution/meta-evaluation failures, manual/verifier fallback and exact-v1 claim boundary",
    "required_post_write_audit": "different reviewer reads Ch66 plus Ch65/Ch67; trace marker alone is insufficient",
    "status": "waiting_for_root_serial_writeback",
})
queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

# Reconcile the independent audit without pretending that recovered Books are written.
audit_path = HERE / "semantic-independent-audit.json"
audit = json.loads(audit_path.read_text())
audit["evidence"].update(deep_complete=75, blocked=[], status="passed")
audit["books"].update(final_integrates=13, current_content_comparison=75, status="open_one_recovered_family_waiting_root_writeback")
audit["remaining_findings"] = [
    "root serial Books writeback and different-reviewer post-write semantic audit for SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION"
]
audit["exact_v1_recovery"] = {
    "auditor": "exact-v1-recovery:/root/may2026_day01",
    "recovered": ["arXiv:2605.11378v1", "arXiv:2605.12129v1"],
    "ordinary_pending": 0,
    "books_decisions": {"2605.11378": "Integrate", "2605.12129": "No Change — Existing Coverage"},
}
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

# Recovery receipt keeps route, exact version and immutable body digest reproducible.
receipt = {
    "schema": "exact-v1-blocker-recovery-receipt-v1",
    "report_date": "2026-05-13",
    "recovered_at": "2026-09-01T14:48:36+08:00",
    "ordinary_pending": 0,
    "items": [
        {
            "arxiv_id": "2605.11378",
            "exact_version": "arXiv:2605.11378v1",
            "route": "official HTML",
            "url": "https://arxiv.org/html/2605.11378v1",
            "bytes": 873493,
            "sha256": "55dd8827f3330370f50c13814dab0c14ef13a7988bd7825bd58745bd6d12705e",
            "review_provenance_id": rp1,
            "access_status": "accessible",
            "books_disposition": "Integrate",
        },
        {
            "arxiv_id": "2605.12129",
            "exact_version": "arXiv:2605.12129v1",
            "route": "official PDF",
            "url": "https://arxiv.org/pdf/2605.12129v1",
            "bytes": 581423,
            "pages": 10,
            "sha256": "ddbfdccced9e1cd3b5de27d4b0a98ceb986f3fc8d47da127a55cb4e16f019cca",
            "review_provenance_id": rp2,
            "access_status": "accessible",
            "books_disposition": "No Change — Existing Coverage",
        },
    ],
}
(HERE / "exact-v1-blocker-recovery-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

for path in (ledger_path, comparison_path, queue_path, audit_path, HERE / "exact-v1-blocker-recovery-receipt.json"):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix(path.suffix + ".sha256").write_text(f"{digest}  {path.name}\n")

print(json.dumps({"rp1": rp1, "rp2": rp2, "comparisons": len(comparisons), "queue": len(queue["items"]), "ordinary_pending": 0}, ensure_ascii=False))
