"""Read-only bounded arXiv discovery; stdout retains raw response and title inventory."""
import datetime
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET

url = sys.argv[1]
result = {"url": url, "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
try:
    req = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design bounded historical discovery"})
    with urllib.request.urlopen(req, timeout=40) as response:
        body = response.read().decode("utf-8")
        result.update(status=response.status, raw=body)
    root = ET.fromstring(body)
    ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
    result["total"] = root.findtext("o:totalResults", namespaces=ns)
    result["entries"] = [{"id": e.findtext("a:id", namespaces=ns),
                          "title": " ".join(e.findtext("a:title", default="", namespaces=ns).split()),
                          "submitted": e.findtext("a:published", namespaces=ns),
                          "updated": e.findtext("a:updated", namespaces=ns)}
                         for e in root.findall("a:entry", ns)]
except Exception as error:
    result["error"] = str(error)
print(json.dumps(result, ensure_ascii=False))
