#!/usr/bin/env python3
"""Materialize the independent 2026-04-01..07 access/denominator audit.

This script deliberately does not close Coverage or Evidence.  It separates
recovered official exact-v1 access from a completed full-section Source Review
and records closure families that must be reopened by the final denominator
reconciliation.  It never reads Weekly files and never writes Books.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
MONTH = ROOT / "papers/2026/04"

# Fresh-context title+abstract challenges.  These are not automatically
# accepted into Books.  They invalidate the old "Coverage passed" assertion
# and must enter exact-v1 denominator reconciliation.
FALSE_NEGATIVE_CHALLENGES = {
    1: [
        "2603.29122", "2603.29193", "2604.16401", "2604.16402",
        "2603.29535", "2603.29632", "2603.29741", "2603.29765",
    ],
    2: [
        "2604.00387", "2604.00430", "2604.00451", "2604.00478",
        "2604.00510", "2604.00547", "2604.00594", "2604.09666",
        "2604.00677", "2604.00717",
    ],
    3: [
        "2604.01518", "2604.01532", "2604.01535", "2604.01567",
        "2604.01605", "2604.01608", "2604.01620", "2604.01647",
        "2604.01658", "2604.01664", "2604.01681", "2604.01687",
        "2604.01707", "2604.01733", "2604.01762", "2604.01954",
        "2604.01985", "2604.02006", "2604.02047", "2604.02091",
        "2604.02106", "2604.02145",
    ],
    4: [
        "2604.02617", "2604.02623", "2604.02640", "2604.02651",
        "2604.02666", "2604.02668", "2604.02728", "2604.02734",
        "2604.02816", "2604.02869", "2604.22778", "2604.09681",
        "2604.02954", "2604.02988", "2604.03016", "2604.03035",
        "2604.03098", "2604.03118", "2604.03145", "2604.22783",
        "2604.03208", "2604.03362", "2604.03384", "2604.03414",
        "2604.03430", "2604.03515", "2604.03527",
    ],
    5: [
        "2604.03551", "2604.03591", "2604.03592", "2604.03598",
        "2604.04969", "2604.03626", "2604.03656", "2604.03785",
        "2604.03820", "2604.04979", "2604.03851", "2604.04983",
        "2604.03908",
    ],
    6: [
        "2604.03925", "2604.04987", "2604.04988", "2604.04989",
        "2604.03997", "2604.04990", "2604.04043", "2604.04074",
        "2604.04190", "2604.04202", "2604.04220", "2604.04226",
        "2604.04269", "2604.04274",
    ],
    7: [
        "2604.04347", "2604.04359", "2604.04372", "2604.04373",
        "2604.04426", "2604.04522", "2604.04532", "2604.04651",
        "2604.04664", "2604.04707", "2604.04745", "2604.04749",
        "2604.04759", "2604.06247", "2604.04847", "2604.04872",
        "2604.04876", "2604.04913", "2604.04921", "2604.04929",
        "2604.05096", "2604.05149", "2604.05157", "2604.05172",
        "2604.05225", "2604.05278",
    ],
}

FALSE_POSITIVE_CHALLENGES = {
    1: ["2604.00073"],
    2: ["2604.01193"],
    4: ["2604.02721", "2604.03395", "2604.03512"],
    7: ["2604.04514", "2604.05091", "2604.05134"],
}


def dump(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def raw_recovery(packet: Path) -> tuple[str, list[str], list[str]]:
    parts = []
    ids = []
    files = sorted(packet.glob("exact-v1-web-recovery-raw*.json"))
    for path in files:
        payload = json.loads(path.read_text(encoding="utf-8"))
        parts.append(payload["raw"])
        ids.extend(payload.get("ids", []))
    return "\n".join(parts), [str(path.relative_to(ROOT)) for path in files], list(dict.fromkeys(ids))


def facet(raw: str, aid: str, name: str) -> dict:
    chunks = [c for c in raw.split("--------------------------------------------------------------------------------") if aid in c]
    chunk = next((c for c in chunks if f'pattern":"{name}' in c), "")
    total_match = re.search(r"Total lines:\s*(\d+)", chunk)
    lines = re.findall(r"^(L\d+:.*)$", chunk, re.MULTILINE)
    meaningful = [line.strip() for line in lines if line.strip()]
    return {
        "facet": name,
        "total_lines": int(total_match.group(1)) if total_match else 0,
        "matched_lines": meaningful[:8],
        "matched": bool(meaningful),
        "internal_error": "Internal Error" in chunk,
    }


def locator(aid: str, result: dict) -> str:
    url = f"https://arxiv.org/html/{aid}v1"
    if result["matched_lines"]:
        nums = [int(re.match(r"L(\d+):", line).group(1)) for line in result["matched_lines"]]
        return f"{url} — bounded `{result['facet']}` recovery lines L{min(nums)}-L{max(nums)}"
    return (
        f"{url} — no dedicated `{result['facet']}` match in bounded recovery; "
        "full-section navigation still pending"
    )


def patch_candidate_row(text: str, family: str, access: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {family} |") and "paper-v1:" in line:
            cols = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(cols) >= 22:
                cols[11] = "pending" if access == "accessible" else "blocked"
                cols[12] = access
                cols[19] = "Not Assessed" if access == "accessible" else "Blocked / Unverified"
                lines[i] = "| " + " | ".join(cols) + " |"
            break
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def patch_review_receipt_row(text: str, family: str, aid: str, facets: list[dict], access: str) -> str:
    lines = text.splitlines()
    method, evaluation, limitations = (locator(aid, x) for x in facets)
    reviewed = (
        f"SRC-ARXIV@arXiv:{aid}v1 official HTML bounded recovery"
        if access == "accessible" else f"SRC-ARXIV@arXiv:{aid}v1 identity/abstract only"
    )
    result = "pending" if access == "accessible" else "blocked"
    provenance = "—" if access == "accessible" else {
        "2604.05013": "RP-b55d32dbac29e616",
    }.get(aid, "—")
    claim_ref = (
        "Pending — full-section source-specific review and Books comparison incomplete"
        if access == "accessible" else f"claim:{family}"
    )
    artifact = f"https://arxiv.org/abs/{aid}v1 ; https://arxiv.org/html/{aid}v1"
    for i, line in enumerate(lines):
        if line.startswith(f"| {family} |"):
            cols = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(cols) != 11 or cols[2] not in {"deep", "standard", "closure", "not_required"}:
                continue
            lines[i] = (
                f"| {family} | {provenance} | deep | arXiv:{aid}v1 | {reviewed} | {method} | "
                f"{evaluation} | {limitations} | {artifact} | {claim_ref} | {result} |"
            )
            break
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def patch_review_block(text: str, family: str, aid: str, facets: list[dict], access: str) -> str:
    start = f"<!-- review:{family}:start -->"
    end = f"<!-- review:{family}:end -->"
    a = text.find(start)
    b = text.find(end, a)
    if a < 0 or b < 0:
        return text
    block = text[a:b]
    method, evaluation, limitations = (locator(aid, x) for x in facets)
    block = re.sub(r"Method locator=`[^`]*`；Evaluation locator=`[^`]*`。", f"Method locator=`{method}`；Evaluation locator=`{evaluation}`。", block)
    block = re.sub(r"Trade-off / failure / fallback：`[^`]*`。", f"Trade-off / failure / fallback：`{limitations}`。", block)
    claim_start = f"<!-- claim:{family}:start -->"
    claim_end = f"<!-- claim:{family}:end -->"
    boundary = (
        "official exact-v1 HTML 已恢复访问；当前仅完成 bounded locator recovery，尚未完成逐节 Source Review、"
        "evaluation-contract 与 non-proof boundary 复核，因此不得进入 Books writeback。"
        if access == "accessible" else
        "official exact-v1 HTML 返回内部错误，PDF route 亦未形成可复核正文；仅有 identity/abstract，不能进入 Books writeback。"
    )
    block = re.sub(re.escape(claim_start) + r".*?" + re.escape(claim_end), claim_start + boundary + claim_end, block, flags=re.S)
    block = block.replace("Books Decision=`Blocked / Unverified`", "Books Decision=`Blocked / Unverified`")
    return text[:a] + block + text[b:]


def patch_books_rows_and_blocks(text: str, family: str, access: str) -> str:
    decision = "Not Assessed" if access == "accessible" else "Blocked / Unverified"
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {family} |") and "books-review:" in line and "paper-v1:" not in line:
            cols = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(cols) >= 9:
                cols[7] = decision
                lines[i] = "| " + " | ".join(cols) + " |"
            break
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    start = f"<!-- books-review:{family}:start -->"
    end = f"<!-- books-review:{family}:end -->"
    a = text.find(start)
    b = text.find(end, a)
    if a >= 0 and b >= 0:
        block = text[a:b]
        block = re.sub(r"Decision=`(?:Blocked / Unverified|Not Assessed)`", f"Decision=`{decision}`", block)
        text = text[:a] + block + text[b:]
    return text


def patch_materials_table(text: str, items: list[dict]) -> str:
    marker = "<!-- validator:materials-request-v1 -->"
    start = text.find(marker)
    if start < 0:
        return text
    end = text.find("\n## 13. Final Status", start)
    if end < 0:
        return text
    head = (
        marker + "\n"
        "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
    )
    rows = []
    for item in items:
        rows.append("| " + " | ".join((
            str(item.get("request_id", "—")), str(item.get("priority", "—")),
            str(item.get("source_family_id", "—")), "—", "—",
            str(item.get("owner_week", "—")), str(item.get("known_identifiers_urls", "—")),
            str(item.get("missing_material", "—")), str(item.get("why_existing_evidence_is_insufficient", "—")),
            str(item.get("acceptable_substitute", "—")), str(item.get("suggested_file_name", "—")),
            str(item.get("required_review_scope", "—")),
        )) + " |")
    replacement = head + ("\n".join(rows) + "\n" if rows else "")
    return text[:start] + replacement + text[end:]


def patch_readme_status(text: str, day: int, registered: int, retained: int, closures: int,
                        complete: int, pending: int, blocked: int, queue: int,
                        fn_count: int, fp_count: int) -> str:
    text = re.sub(r"\*\*Status:\*\*.*", "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；fresh-context denominator / exact-v1 reconciliation 尚未完成。", text, count=1)
    text = re.sub(
        r"严格窗口注册并逐项 title\+abstract 语义筛选 .*?。exact-v1 Review complete=.*?；Integrate queue=.*?。",
        f"严格窗口注册并逐项 title+abstract 语义筛选 {registered}/{registered} identity；现有 provisional Candidate Denominator={retained}、closures={closures}。fresh-context audit 已恢复 exact-v1 access：complete={complete}、pending full-section review={pending}、blocked={blocked}；旧 queue={queue}，但 denominator false-negative challenges={fn_count}、false-positive challenges={fp_count}，因此不能视为 final queue。",
        text,
        count=1,
    )
    text = re.sub(r"\| Completion Status \| .*? \|", "| Completion Status | In Progress |", text, count=1)
    text = re.sub(r"\| Coverage Gate \| .*? \|", "| Coverage Gate | Open |", text, count=1)
    text = re.sub(r"\| Evidence Gate \| .*? \|", "| Evidence Gate | Open |", text, count=1)
    text = re.sub(
        rf"<!-- coverage:SRC-ARXIV:202604{day:02d}:start -->.*?<!-- coverage:SRC-ARXIV:202604{day:02d}:end -->",
        f"<!-- coverage:SRC-ARXIV:202604{day:02d}:start -->已重放 {registered}/{registered} identity；fresh-context reviewer 对全部 retained/closure 执行反向挑战，发现 {fn_count} 个明确的系统级 closure 需要重开，并对 {fp_count} 个 retained 提出 false-positive challenge。当前 denominator 仍在 reconciliation，Coverage Gate 保持 Open。<!-- coverage:SRC-ARXIV:202604{day:02d}:end -->",
        text,
        flags=re.S,
    )
    text = re.sub(r"\| SA-\d+-COVERAGE \|.*?\| passed \|", f"| SA-202604{day:02d}-COVERAGE | fresh-context:april01-07-independent-reviewer | coverage | coverage:SRC-ARXIV:202604{day:02d} | {fn_count} false-negative challenges; {fp_count} false-positive challenges | reopen denominator and exact-v1 review | open |", text)
    text = re.sub(r"\| SA-\d+-EVIDENCE \|.*?\| passed \|", f"| SA-202604{day:02d}-EVIDENCE | fresh-context:april01-07-independent-reviewer | evidence | validator:review-completion-v1 | {pending} accessible families still lack complete full-section review; {blocked} exact route blocker | finish source-specific Method/Evaluation/Limitations review | open |", text)
    text = re.sub(r"Completion Status: `[^`]+`", "Completion Status: `In Progress — Denominator / Evidence / Books Pending`", text)
    text = re.sub(r"Coverage: `[^`]+`", "Coverage: `Open`", text)
    text = re.sub(r"Evidence: `[^`]+`", "Evidence: `Open`", text)
    text = re.sub(r"unresolved findings: \d+", f"unresolved findings: {fn_count + fp_count + pending + blocked + 1}", text)
    text = re.sub(
        r"Author packet：raw=.*?不能宣称本日 Complete。",
        f"Fresh-context checkpoint：registered/screened={registered}/{registered}、provisional denominator={retained}、closures={closures}、exact-v1 complete={complete}、pending={pending}、blocked={blocked}、旧 queue={queue}。由于 denominator 与 source-specific Review 均有未解决 finding，不能宣称本日 Complete。",
        text,
        count=1,
    )
    return text


def main() -> None:
    monthly = {"schema": "april-01-07-fresh-context-audit-v1", "weekly_dependency_count": 0, "days": []}
    for day in range(1, 8):
        date = f"2026-04-{day:02d}"
        packet = MONTH / f"_sources/daily-202604{day:02d}"
        readme_path = MONTH / f"{day:02d}/README.md"
        ledger = json.loads((packet / "screening-ledger-final.json").read_text(encoding="utf-8"))
        identities = {row["arxiv_id"]: row for row in ledger["identities"]}
        exact_path = packet / "exact-v1-review-packet.json"
        exact = json.loads(exact_path.read_text(encoding="utf-8"))
        raw, raw_refs, recovery_ids = raw_recovery(packet)
        recovery = []
        old_blocked = [item for item in exact["items"] if item["arxiv_id"] in recovery_ids]
        readme = readme_path.read_text(encoding="utf-8")
        access_receipt = json.loads((packet / "exact-v1-access-receipt.json").read_text(encoding="utf-8"))
        access_by_id = {row["arxiv_id"]: row for row in access_receipt["rows"]}
        still_blocked = []
        pending = []
        for item in old_blocked:
            aid = item["arxiv_id"]
            family = item["source_family_id"]
            facets = [facet(raw, aid, name) for name in ("Method", "Evaluation", "Limitations")]
            accessible = any(x["total_lines"] > 1 and not x["internal_error"] for x in facets)
            access = "accessible" if accessible else "blocked"
            if accessible:
                pending.append(aid)
                item.update({
                    "reviewed_evidence_versions": [f"SRC-ARXIV@arXiv:{aid}v1 official HTML bounded recovery"],
                    "method_identity_locators": locator(aid, facets[0]),
                    "evaluation_locators": locator(aid, facets[1]),
                    "limitations_counterevidence_locators": locator(aid, facets[2]),
                    "artifact_locators": f"https://arxiv.org/abs/{aid}v1 ; https://arxiv.org/html/{aid}v1",
                    "claim_boundary": "Official exact-v1 access recovered, but bounded keyword excerpts do not substitute for a complete source-specific Method/Evaluation/Limitations review; Books remains blocked.",
                    "completion_result": "pending",
                })
                access_by_id[aid] = {
                    "arxiv_id": aid,
                    "identity_url": f"https://arxiv.org/abs/{aid}v1",
                    "identity_path": "—",
                    "identity_sha256": "—",
                    "withdrawn": False,
                    "withdrawal_phrase": "—",
                    "body_route": "official_html_v1_bounded_web_recovery",
                    "body_url": f"https://arxiv.org/html/{aid}v1",
                    "body_path": "—",
                    "body_sha256": "—",
                    "error": "full-section semantic review pending",
                }
            else:
                still_blocked.append(aid)
                access_by_id[aid] = {
                    "arxiv_id": aid,
                    "identity_url": f"https://arxiv.org/abs/{aid}v1",
                    "identity_path": "—",
                    "identity_sha256": "—",
                    "withdrawn": False,
                    "withdrawal_phrase": "—",
                    "body_route": "blocked",
                    "body_url": f"https://arxiv.org/html/{aid}v1",
                    "body_path": "—",
                    "body_sha256": "—",
                    "error": "official HTML returned internal error; PDF route did not yield a reviewable exact-v1 body",
                }
            recovery.append({
                "source_family_id": family,
                "arxiv_id": aid,
                "title": identities[aid]["title"],
                "access_status": access,
                "completion_status": "pending_full_section_review" if accessible else "blocked_exact_v1_route",
                "official_url": f"https://arxiv.org/html/{aid}v1",
                "facets": facets,
            })
            readme = patch_candidate_row(readme, family, access)
            readme = patch_review_receipt_row(readme, family, aid, facets, access)
            readme = patch_review_block(readme, family, aid, facets, access)
            readme = patch_books_rows_and_blocks(readme, family, access)

        access_receipt["rows"] = list(access_by_id.values())
        access_receipt["candidate_count"] = len(access_receipt["rows"])
        access_receipt["accessible_count"] = sum(row["body_route"] != "blocked" for row in access_receipt["rows"])
        access_receipt["blocked_count"] = len(still_blocked)
        dump(packet / "exact-v1-access-receipt.json", access_receipt)
        dump(exact_path, exact)

        mr_path = packet / "materials-request.json"
        mr = json.loads(mr_path.read_text(encoding="utf-8"))
        def mr_arxiv_id(item: dict) -> str:
            family = item.get("source_family_id", "")
            match = re.search(r"ARXIV-(\d{4})-(\d{5})$", family)
            return f"{match.group(1)}.{match.group(2)}" if match else ""
        mr["items"] = [x for x in mr["items"] if mr_arxiv_id(x) in still_blocked]
        dump(mr_path, mr)

        comparison_path = packet / "books-current-content-comparison.json"
        comparison = json.loads(comparison_path.read_text(encoding="utf-8"))
        recovery_access = {item["arxiv_id"]: item["access_status"] for item in recovery}
        for item in comparison["items"]:
            if item["arxiv_id"] in recovery_access:
                item["decision"] = "Not Assessed" if recovery_access[item["arxiv_id"]] == "accessible" else "Blocked / Unverified"
        dump(comparison_path, comparison)
        readme = patch_materials_table(readme, mr["items"])

        retained = ledger["candidate_denominator"]
        registered = ledger["registered_identities"]
        closures = ledger["pre_denominator_closed"]
        complete = sum(item["completion_result"] == "complete" for item in exact["items"])
        queue = len(json.loads((packet / "BOOKS_WRITEBACK_QUEUE.json").read_text(encoding="utf-8"))["items"])
        fn = [aid for aid in FALSE_NEGATIVE_CHALLENGES.get(day, []) if aid in identities and identities[aid].get("candidate_state") != "retained"]
        fp = [aid for aid in FALSE_POSITIVE_CHALLENGES.get(day, []) if aid in identities and identities[aid].get("candidate_state") == "retained"]
        challenge_rows = [{
            "arxiv_id": aid,
            "source_family_id": identities[aid]["source_family_id"],
            "title": identities[aid]["title"],
            "abstract_mechanism": identities[aid]["abstract"][:600],
            "finding": "closure may suppress a durable AI-system mechanism/evaluation/state-control delta; reopen for exact-v1 denominator decision",
        } for aid in fn]
        fp_rows = [{
            "arxiv_id": aid,
            "source_family_id": identities[aid]["source_family_id"],
            "title": identities[aid]["title"],
            "finding": "retention may be domain/benchmark-local or unsupported by current exact-v1 boundary; challenge before final denominator",
        } for aid in fp]
        audit = {
            "schema": "fresh-context-denominator-evidence-audit-v2.1",
            "report_date": date,
            "auditor": "fresh-context:april01-07-independent-reviewer",
            "scope": {
                "registered_identities_replayed": registered,
                "provisional_retained_replayed": retained,
                "closures_replayed": closures,
                "semantic_inputs": ["strict-window raw inventory", "official primary identity/exact-v1", "current Books"],
                "weekly_inputs": [],
            },
            "weekly_dependency_count": 0,
            "exact_v1_access_recovery": {
                "old_blocked": len(old_blocked),
                "access_recovered_pending_review": len(pending),
                "still_blocked": len(still_blocked),
                "still_blocked_ids": still_blocked,
                "raw_receipts": raw_refs,
                "items": recovery,
            },
            "denominator_findings": {
                "false_negative_challenges": challenge_rows,
                "false_positive_challenges": fp_rows,
                "final_denominator_frozen": False,
            },
            "source_review_findings": [
                "Recovered HTML access is not a completed full-section Source Review; bounded keyword excerpts cannot by themselves close Evidence.",
                "Existing complete reviews use repeated fallback prose and require source-specific trade-off/failure/coexistence verification before Evidence can pass.",
                "Books queue is provisional until denominator reconciliation and current owner+adjacent comparison are repeated for every surviving candidate.",
            ],
            "deep_selection_finding": "Deep Analysis cannot be final while denominator and source-specific review remain open.",
            "gate": {"coverage": "Open", "evidence": "Open", "books": "Open"},
        }
        dump(packet / "fresh-context-denominator-evidence-audit.json", audit)

        existing_audit_path = packet / "independent-semantic-audit.json"
        existing_audit = json.loads(existing_audit_path.read_text(encoding="utf-8"))
        existing_audit.update({
            "auditor": "fresh-context:april01-07-independent-reviewer",
            "exact_v1_complete": complete,
            "exact_v1_pending": len(pending),
            "exact_v1_blocked": len(still_blocked),
            "false_negative_challenges": fn,
            "false_positive_challenges": fp,
            "weekly_dependency_count": 0,
            "unresolved_findings": [
                f"{len(fn)} closure families require exact-v1 denominator reconciliation.",
                f"{len(fp)} retained families require false-positive challenge.",
                f"{len(pending)} recovered official exact-v1 routes still require full-section source-specific review.",
                f"{len(still_blocked)} family remains exact-v1 access blocked.",
                "Books queue is provisional and cannot be written before the above findings are reconciled.",
            ],
            "gate": {"coverage": "Open", "evidence": "Open", "books": "Open"},
        })
        dump(existing_audit_path, existing_audit)

        readme = patch_readme_status(readme, day, registered, retained, closures, complete, len(pending), len(still_blocked), queue, len(fn), len(fp))
        readme_path.write_text(readme, encoding="utf-8")
        monthly["days"].append({
            "date": date, "registered": registered, "provisional_retained": retained,
            "closures": closures, "exact_complete": complete, "exact_pending": len(pending),
            "exact_blocked": len(still_blocked), "queue": queue,
            "false_negative_challenges": len(fn), "false_positive_challenges": len(fp),
            "gate": "Open",
        })
    dump(MONTH / "_sources/april-01-07-fresh-context-audit-summary.json", monthly)


if __name__ == "__main__":
    main()
