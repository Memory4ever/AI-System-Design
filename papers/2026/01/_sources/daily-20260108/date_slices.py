"""Fresh bounded public date metadata; stdout only, no local writes."""
import datetime
import json
import re
import urllib.request
import xml.etree.ElementTree as ET

def fetch(url, body=None, headers=None):
    request = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, headers={"User-Agent": "Mozilla/5.0", **({"Content-Type": "application/json"} if body else {}), **(headers or {})})
    with urllib.request.urlopen(request, timeout=35) as response:
        return response.read().decode("utf-8")

targets = [("openai-rss", "https://openai.com/news/rss.xml"), ("anthropic-dates", "https://www.anthropic.com/research"), ("hunyuan-directory", "https://api.hunyuan.tencent.com/api/blog/publicList"), ("kimi-releases", "https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100&page=1")]
for article_type in [1, 2]:
    for year, descending in [(2026, "false"), (2025, "true")]:
        targets.append((f"seed-{article_type}-{year}", f"https://seed.bytedance.com/api/get_article_list_v2?article_type={article_type}&publish_year={year}&count=20&page_token=0&order_desc={descending}"))
for name, url in targets:
    record = {"name": name, "url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        body = {"pageNum": 1, "pageSize": 1000, "renderType": 0} if name == "hunyuan-directory" else None
        raw = fetch(url, body, {"x-tt-locale": "US"} if name.startswith("seed-") else None)
        if name == "openai-rss":
            items = [{"title": item.findtext("title"), "link": item.findtext("link"), "pubDate": item.findtext("pubDate")} for item in ET.fromstring(raw).findall(".//item")]
            selected = [item for item in items if re.search(r"\b(?:0?[1-9]|1[0-2]) Jan 2026\b", item["pubDate"] or "")]
            record.update(total_metadata=len(items), nearby_date_metadata=selected, boundary="Jan1–12 metadata only; no full article content or historical completeness")
        elif name == "anthropic-dates":
            normalized = raw.replace('\\"', '"')
            matches = list(re.finditer(r'"publishedOn"\s*:\s*"([^"\\]+)', normalized))
            dates = [m.group(1) for m in matches]
            nearby = [m for m in matches if m.group(1).startswith(("2026-01", "2025-12"))]
            record.update(publishedOn_count=len(dates), nearby_fields=[{"publishedOn": m.group(1), "context": normalized[max(0,m.start()-500):m.end()+500]} for m in nearby], boundary="only Dec2025/Jan2026 metadata contexts, not entire institution")
        elif name == "kimi-releases":
            releases = json.loads(raw)
            record.update(total_returned=len(releases), metadata=[{"tag_name": r["tag_name"], "published_at": r["published_at"], "created_at": r["created_at"], "html_url": r["html_url"], **({"body": r["body"]} if "2026-01-07T01" <= r["published_at"] < "2026-01-08T01" else {})} for r in releases if "2026-01-01" <= r["published_at"] < "2026-01-11"], first=releases[0]["published_at"] if releases else None, last=releases[-1]["published_at"] if releases else None, boundary="page1 only; missing Jan slice requires tag/date restoration, no created_at substitution")
        else:
            record["request_body"] = body
            payload = json.loads(raw)
            if name.startswith("seed-"):
                record["raw_metadata_fields"] = {key: value for key, value in payload.items() if key != "sub_article_list"}
                record["metadata"] = [{"ArticleMeta": {key: value for key, value in item.get("ArticleMeta", {}).items() if key in {"ArticleId", "ID", "PublishDate", "UpdateTime", "IsPinned", "ContentType", "StatusEn", "StatusZh"}}, "ArticleSubContentEn": {key: value for key, value in item.get("ArticleSubContentEn", {}).items() if key in {"Title", "TitleKey"}}} for item in payload.get("sub_article_list", [])]
            else:
                def metadata_only(value):
                    if isinstance(value, dict):
                        return {key: metadata_only(item) for key, item in value.items() if not re.search(r"content|abstract|description|cover|thumbnail|image|avatar", key, re.I)}
                    if isinstance(value, list):
                        return [metadata_only(item) for item in value]
                    return value if not isinstance(value, str) or len(value) <= 500 else "[nonmetadata text omitted]"
                record["raw_metadata_fields"] = metadata_only(payload)
            record["boundary"] = "current official metadata slice; pinned and pagination retained, not archive or public first timestamp"
    except Exception as error:
        record["error"] = str(error)
    print(json.dumps(record, ensure_ascii=False), flush=True)
