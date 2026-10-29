"""Derive conservative announcement bounds from preserved official metadata."""
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

root = Path(__file__).resolve().parent
rows = json.loads((root / 'REPAIR_DATES_20261029.json').read_text())
et, bjt = ZoneInfo('America/New_York'), ZoneInfo('Asia/Shanghai')
out = ['# 本日精确 DOI 与公告联合界', '',
       '此表为原JSON的可复算推断，不把registered称为实际公开时间。2025官方规则见REPAIR_ARXIV_RULE_2025_20261029.md。',
       '每件核精确DOI、client arxiv.content、state findable、唯一Submitted/v1；本地既有exact-v1原件另作身份对照。',
       '下界按ET截止14:00后的最早可公告20:00，延迟只可能推后；上界为registered。整个区间同BJT日才授该公告日。',
       '本表处理旧49+新9潜力，不增加候选/全文数；没有具体更早正文线索时不无限排除假想渠道。', '',
       '| DOI/原件 | 唯一v1 UTC | 最早公告BJT | registered原值UTC | 结论 |',
       '| --- | --- | --- | --- | --- |']
counts = {}
for row in rows:
    aid = row['doi'].split('arxiv.')[1]
    assert row['client'] == 'arxiv.content' and row['state'] == 'findable'
    v1 = [d['date'] for d in row['dates'] if d.get('dateType') == 'Submitted' and d.get('dateInformation') == 'v1']
    assert len(v1) == 1
    submitted = datetime.fromisoformat(v1[0].replace('Z', '+00:00'))
    registered = datetime.fromisoformat(row['registered'].replace('Z', '+00:00'))
    if submitted.year == 2025:
        day = submitted.astimezone(et).replace(hour=14, minute=0, second=0, microsecond=0)
        for _ in range(10):
            if day.weekday() < 5 and submitted <= day:
                announcement = day.replace(hour=20)
                if day.weekday() == 4:
                    announcement += timedelta(days=2)
                break
            day += timedelta(days=1)
        lower = announcement.astimezone(bjt)
        assert lower <= registered
        assert lower.date().isoformat() > '2025-10-18'
        verdict = lower.date().isoformat() if lower.date() == registered.astimezone(bjt).date() else '明确窗后，区间跨日'
        lower_text = lower.isoformat()
    else:
        verdict = '2026事件，不授2025日；无更早原件线索'
        lower_text = '不套用2025公告日程'
    counts[verdict] = counts.get(verdict, 0) + 1
    out.append(f'| [{aid}](REPAIR_DOI_{aid}_20261029.json) | {v1[0]} | {lower_text} | {row["registered"]} | {verdict} |')
out += ['', '计数：' + json.dumps(counts, ensure_ascii=False), '',
        'Temporal16685官方v1为Oct19，旧Advanced Oct18字段不覆盖唯一v1原件；冲突保留为旧发现元数据差异，不移植v2理论到v1。',
        '不把窗后材料全部搬进本日报；只关闭本日arXiv事件日期待办。旧27必要反证及撤回16309禁界保留。']
(root / 'REPAIR_BOUNDS_20261029.md').write_text('\n'.join(out) + '\n')
print(len(rows), counts)
