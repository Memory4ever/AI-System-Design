"""Bounded source extraction; downloaded responses are provenance, not coverage claims."""
import json, sys, urllib.request, datetime, re, html

url = sys.argv[1]
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=35) as response:
        raw = response.read().decode("utf-8", "replace")
        status = response.status
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', raw, re.S)
    body = html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', raw, flags=re.S)))
    body = re.sub(r'\s+', ' ', body).strip()
    may = [body[max(0,m.start()-180):m.end()+260] for m in re.finditer(r"2026[-/.]0?5[-/.]|May\s+\d{1,2},?\s+2026|2026年5月", body)]
    script_dates = [raw[max(0,m.start()-180):m.end()+240] for m in re.finditer(r'2026-05-\d\d|2026/05/\d\d', raw)]
    data = {"url":url,"checked":datetime.datetime.now(datetime.timezone.utc).isoformat(),"status":status,"characters":len(raw),"text":body[:30000],"may_contexts":may,"script_date_contexts":script_dates,"script_urls":re.findall(r'<script[^>]+src="([^"]+)"',raw)}
    print(json.dumps(data,ensure_ascii=False))
except Exception as exc:
    print(json.dumps({"url":url,"error":str(exc)},ensure_ascii=False))
