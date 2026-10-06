"""Finite native-source recovery for this date; generated raw network artifacts."""
import concurrent.futures, datetime, html, json, pathlib, re, sys, urllib.request
base = pathlib.Path(__file__).parent
def fetch(job):
    key, url = job[:2]
    try:
        req = urllib.request.Request(url, data=json.dumps(job[2]).encode() if len(job)>2 else None, headers={"User-Agent":"AI-System-Design historical source review", "Content-Type":"application/json", "Origin":"https://hunyuan.tencent.com"})
        with urllib.request.urlopen(req, timeout=35) as response:
            body = response.read().decode("utf-8", "replace")
            status = response.status
        (base / ("V3_NATIVE_" + key + ".txt")).write_text(body)
        plain = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", body, flags=re.S)
        plain = html.unescape(re.sub(r"<[^>]+>", " ", plain))
        return {"key":key,"url":url,"status":status,"bytes":len(body),"text":re.sub(r"\s+", " ", plain)[:20000]}
    except Exception as error:
        return {"key":key,"url":url,"error":str(error)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, json.loads(sys.argv[1])))
(base / ("V3_NATIVE_" + sys.argv[2] + ".json")).write_text(json.dumps({"executed_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"results":results},ensure_ascii=False,indent=2))
for row in results:
    print(row["key"], row.get("status",row.get("error")), row.get("bytes",0), row.get("text", "")[:180])
