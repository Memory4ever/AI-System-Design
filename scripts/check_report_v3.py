"""Read-only structural checks for the single human-readable V3 report.

This module does not fetch sources, rate contributions, or establish independent
semantic acceptance. Registry is a mapping of Source ID to its registry row.
"""
from datetime import date, datetime, time, timedelta, timezone
import re


SECTIONS = ("1. 结论", "2. 来源覆盖", "3. 候选与判断", "4. 证据与知识整合", "5. 缺口与下一步", "6. 复核")
SOURCE_COLUMNS = ("来源", "检查范围与依据", "结果", "缺口")
CANDIDATE_COLUMNS = ("材料", "公开时间", "项目贡献与评分", "审阅结果", "Books决定")
LINK = re.compile(r"\[([^\]\n]+)\]\(([^\s)]+)\)")
BEIJING = timezone(timedelta(hours=8))
ABSENT = {"", "无", "—", "-"}


def _timestamp(value, label, errors):
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})", value):
            raise ValueError
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{label}必须是带时区的 ISO 时间：{value!r}")
        return None


def _table(section, columns, errors):
    lines = [line.strip() for line in section.splitlines() if line.strip().startswith("|")]
    cells = [re.split(r"(?<!\\)\|", line.strip("|")) for line in lines]
    cells = [[cell.strip() for cell in row] for row in cells]
    if len(cells) < 2 or tuple(cells[0]) != columns:
        errors.append(f"表格列必须为 {' | '.join(columns)}")
        return []
    if len(cells[1]) != len(columns) or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells[1]):
        errors.append(f"{columns[0]}表缺少合法分隔行")
    rows = []
    for row in cells[2:]:
        if len(row) != len(columns):
            errors.append(f"{columns[0]}表行的列数应为 {len(columns)}")
        else:
            rows.append(row)
    return rows


def validate(text, registry, root=None, path=None, stable_node_ids=None):
    """Return format/consistency errors, never semantic approval.

    ``root`` and ``path`` are accepted for caller compatibility; no filesystem
    traversal or local-link existence check is performed.
    """
    errors = []
    title = re.fullmatch(r"# (Daily|Weekly) Research — (\d{4}-\d{2}-\d{2}|\d{4}-W\d{2})", text.splitlines()[0] if text.splitlines() else "")
    expected = None
    weekly = bool(title and title[1] == "Weekly")
    try:
        if not title:
            raise ValueError
        if weekly:
            year, week = title[2].split("-W")
            end = datetime.combine(date.fromisocalendar(int(year), int(week), 7), time(9), BEIJING)
            expected = end - timedelta(days=7), end
        else:
            end = datetime.combine(date.fromisoformat(title[2]), time(9), BEIJING)
            expected = end - timedelta(days=1), end
    except ValueError:
        errors.append("首行必须是有效日期的 Daily Research 或 ISO 周的 Weekly Research 标题")

    headings = list(re.finditer(r"^## (.+)$", text, re.MULTILINE))
    if tuple(match[1] for match in headings) != SECTIONS:
        errors.append("报告必须按顺序包含六个固定二级章节")
    sections = {match[1]: text[match.end():headings[i + 1].start() if i + 1 < len(headings) else len(text)].strip()
                for i, match in enumerate(headings)}
    top = text[:headings[0].start()] if headings else text
    fields = {}
    for key, value in re.findall(r"^\*\*([^*：]+)：\*\*\s*([^\n]*)$", top, re.MULTILINE):
        if key in fields:
            errors.append(f"顶端字段重复：{key}")
        fields[key] = value.strip()
    for key in ("规范", "窗口", "状态", "Books", "检查时间"):
        if not fields.get(key):
            errors.append(f"顶端缺少字段：{key}")
    if fields.get("规范") != "V3":
        errors.append("规范必须是 V3")
    status = fields.get("状态")
    if status not in {"进行中", "完成"}:
        errors.append("状态必须是进行中或完成")
    books_mode = fields.get("Books")
    if books_mode not in {"纳入本次", "本次仅报告"}:
        errors.append("Books 必须声明纳入本次或本次仅报告")
    window = fields.get("窗口", "").split("～")
    start = end = None
    if len(window) != 2:
        errors.append("窗口必须用 ～ 分隔起止时间")
    else:
        start = _timestamp(window[0].strip(), "窗口起点", errors)
        end = _timestamp(window[1].strip(), "窗口终点", errors)
        if start and end:
            if start >= end:
                errors.append("窗口终点必须晚于起点")
            if expected and (start, end) != expected and fields.get("窗口说明", "") in ABSENT:
                errors.append("非默认窗口必须提供用户授权的窗口说明")
    checked = _timestamp(fields.get("检查时间", ""), "检查时间", errors)
    if status == "完成" and checked and end and checked < end:
        errors.append("完成时检查时间不得早于窗口终点")

    required = {key for key, row in registry.items()
                if row.get("Cadence", "").replace(" ", "") in
                ({"RequiredDaily", "RequiredWeekly"} if weekly else {"RequiredDaily"})}
    seen_sources = set()
    pending = blocked = deferred = False
    for source, basis, result, gap in _table(sections.get(SECTIONS[1], ""), SOURCE_COLUMNS, errors):
        extra = re.fullmatch(r"(表外|补检)：(.+)", source)
        extra_link = LINK.fullmatch(extra[2]) if extra else None
        valid_extra = bool(extra_link and re.match(r"https://[^/\s]+", extra_link[2]))
        source_link = LINK.fullmatch(source)
        source_id = source_link[1] if source_link else source.split()[0].strip("` ") if source else ""
        if valid_extra:
            source_id = extra_link[2]
        if source_id not in registry and not valid_extra:
            errors.append(f"未知来源：{source_id}")
        if source_id in seen_sources:
            errors.append(f"来源重复：{source_id}")
        seen_sources.add(source_id)
        if basis in ABSENT:
            errors.append(f"{source_id} 检查范围与依据不得为空")
        if result not in {"已检查", "未完成", "受阻", "未触发", "不适用", "检索受限"}:
            errors.append(f"{source_id} 来源结果无效：{result}")
        if result == "不适用" and re.sub(r"https?://\S+", "", LINK.sub("", basis)).strip() in ABSENT:
            errors.append(f"{source_id} 不适用必须说明原因，不能只有链接")
        if result == "未触发" and source_id in required:
            errors.append(f"固定来源 {source_id} 不得写未触发")
        if result in {"受阻", "检索受限"} and gap in ABSENT:
            errors.append(f"受阻来源 {source_id} 必须说明缺口")
        pending |= result == "未完成"
        optional_discovery = (valid_extra and extra[1] == "补检") or "Backstop" in registry.get(source_id, {}).get("Cadence", "")
        search_limited = optional_discovery and result == "检索受限"
        if result == "检索受限" and not optional_discovery:
            errors.append(f"{source_id} 只有补检搜索可用检索受限，必查来源或必要材料须记录受阻")
        blocked |= result == "受阻" or (gap not in ABSENT and not search_limited)
    for missing in sorted(required - seen_sources):
        errors.append(f"缺少必查来源：{missing}")

    evidence = sections.get(SECTIONS[3], "")
    evidence_headers = list(re.finditer(r"^### (.+)$", evidence, re.MULTILINE))
    bodies = {}
    for i, heading in enumerate(evidence_headers):
        link = LINK.fullmatch(heading[1].strip())
        if link:
            body = evidence[heading.end():evidence_headers[i + 1].start() if i + 1 < len(evidence_headers) else len(evidence)].strip()
            bodies[(link[1], link[2])] = body
    seen_materials = set()
    for material, published, score, review, books in _table(sections.get(SECTIONS[2], ""), CANDIDATE_COLUMNS, errors):
        link = LINK.fullmatch(material)
        if not link or not re.match(r"https?://[^/\s]+", link[2]):
            errors.append(f"材料必须是 primary Markdown 链接：{material}")
        elif link[2] in seen_materials:
            errors.append(f"候选材料 URL 重复：{link[2]}")
        else:
            seen_materials.add(link[2])
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", published):
            try:
                publication = datetime.combine(date.fromisoformat(published), time(), BEIJING)
                if start and end and not (start <= publication and publication + timedelta(days=1) <= end):
                    errors.append(f"材料公开日期不能确定完全落在窗口内；补充有依据的时间范围或保留日期缺口：{material}")
            except ValueError:
                errors.append(f"材料公开日期无效：{published}")
        elif "～" in published:
            bounds = published.split("～")
            if len(bounds) != 2:
                errors.append(f"材料公开时间范围必须包含两个窗口边界：{material}")
            else:
                lower = _timestamp(bounds[0].strip(), "材料公开范围起点", errors)
                upper = _timestamp(bounds[1].strip(), "材料公开范围终点", errors)
                if lower and upper and (lower >= upper or (start and end and not (start <= lower < upper <= end))):
                    errors.append(f"材料公开时间范围必须完全落在窗口内：{material}")
        else:
            publication = _timestamp(published, "材料公开时间", errors)
            if publication and start and end and not start <= publication < end:
                errors.append(f"材料公开时间不在窗口内：{material}")
        repeated = "不重复评分" in score
        important_revision = bool(re.search(r"重要\s*(?:修订|revision)|important[_ ]revision", score, re.IGNORECASE))
        scoring = re.search(r"(?<!\d)(\d+)\s*\+\s*(\d+)\s*\+\s*(\d+)\s*=\s*(\d+)(?!\d)", score)
        total = None
        if scoring:
            d, r, l, total = map(int, scoring.groups())
            if any(value not in range(4) for value in (d, r, l)) or d + r + l != total:
                errors.append(f"候选评分必须三项 0..3 且合计正确：{material}")
        elif not repeated:
            errors.append(f"新候选缺少 d+r+l=total 评分：{material}")
        if repeated and not re.search(r"revision|修订|已处理", score, re.IGNORECASE):
            errors.append(f"不重复评分需明确 revision 或已处理：{material}")
        if review not in {"深入完成", "标准完成", "已关闭", "待审阅", "受阻", "争议"}:
            errors.append(f"候选审阅结果无效：{review}")
        if total is not None and total >= 7 and review in {"标准完成", "已关闭"}:
            errors.append(f"7 分及以上候选不得低于深入完成：{material}")
        if total in {5, 6} and review == "已关闭":
            errors.append(f"5～6 分候选不得低于标准完成：{material}")
        if important_revision and review in {"标准完成", "已关闭"}:
            errors.append(f"重要修订不得低于深入完成：{material}")
        decision = re.split(r"[：:\s]", books, maxsplit=1)[0]
        if decision not in {"整合", "已有覆盖", "仅报告", "结构候选", "暂缓", "未纳入本次"}:
            errors.append(f"Books 决定缺失或无效：{material}")
        if decision == "未纳入本次" and books_mode != "本次仅报告":
            errors.append(f"Books 未纳入本次需要顶端声明本次仅报告：{material}")
        if books_mode == "本次仅报告" and decision in {"整合", "已有覆盖", "结构候选"}:
            errors.append(f"Books 本次仅报告不能声明{decision}：{material}")
        if decision in {"整合", "已有覆盖"}:
            nodes = set(re.findall(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b", LINK.sub("", books)))
            if not nodes or (stable_node_ids is not None and not nodes.intersection(stable_node_ids)):
                errors.append(f"Books {decision}需要有效 Stable Node：{material}")
            if not any(re.search(r"\.md(?:#.*)?$", target) for _, target in LINK.findall(books)):
                errors.append(f"Books {decision}需要章节 Markdown 链接：{material}")
        if decision == "整合" and review != "深入完成":
            errors.append(f"Books 整合需要深入完成：{material}")
        if decision == "已有覆盖" and review in {"受阻", "争议", "待审阅"}:
            errors.append(f"Books 已有覆盖不能由未完成审阅支持：{material}")
        if (not repeated or important_revision) and review in {"深入完成", "标准完成", "已关闭"} and link:
            if bodies.get((link[1], link[2]), "") in ABSENT:
                errors.append(f"已审阅新候选缺少 §4 同标题同 URL 的具体正文：{material}")
        pending |= review == "待审阅"
        blocked |= review in {"受阻", "争议"}
        deferred |= decision == "暂缓"

    gap_text = sections.get(SECTIONS[4], "").strip()
    if not gap_text:
        errors.append("缺口与下一步不得为空；无缺口写无")
    no_open_gap = bool(gap_text and gap_text.splitlines()[0].strip() == "无")
    if (blocked or deferred) and no_open_gap:
        errors.append("受阻、争议或暂缓事项必须在 §5 说明，不能声明本窗缺口为无")
    has_gap = blocked or deferred or not no_open_gap
    terminal_reservation = bool(
        re.search(r"终态保留(?:项)?", gap_text)
        and re.search(r"(?:定点)?重开(?:条件)?", gap_text)
        and re.search(r"不(?:用于|支持).*(?:正面证据|Books|无遗漏断言)", gap_text)
    )
    if status == "完成":
        if pending:
            errors.append("完成报告不得存在未完成或待审阅的可执行工作")
        if has_gap and not terminal_reservation:
            errors.append(
                "完成报告的外部缺口必须在 §5 标为终态保留项，明确不支持正面证据、"
                "Books 或无遗漏断言，并给出定点重开条件"
            )
    if status == "完成":
        review_text = sections.get(SECTIONS[5], "")
        reviewer = re.search(r"^复核者：[ \t]*(.*)$", review_text, re.MULTILINE)
        if not reviewer or reviewer[1].strip() in ABSENT:
            errors.append("完成报告需要非空复核者身份")
        conclusion = re.search(r"^结论：[ \t]*(通过|未通过)[ \t]*$", review_text, re.MULTILINE)
        if not conclusion or (status == "完成" and conclusion[1] != "通过"):
            errors.append("完成报告需要已结束且通过的复核结论")
        elif conclusion[1] == "未通过":
            explanation = re.sub(r"^(?:复核者|结论)：.*$", "", review_text, flags=re.MULTILINE).strip()
            if explanation in ABSENT:
                errors.append("复核未通过必须具体说明外部问题")
    return errors
