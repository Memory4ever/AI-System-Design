"""One metadata lookup per named potentially relevant v1, not a title-list queue."""
import datetime as dt
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).parent
IDS = ["2511.18906", "2511.18692", "2511.17849", "2511.18890", "2511.17864", "2511.17852",
       "2511.18635", "2511.18423", "2511.18936", "2511.18670", "2511.19269", "2511.19229",
       "2511.17729", "2511.21759", "2511.18661", "2511.19575", "2511.19438", "2511.18674",
       "2511.18291", "2511.18151"]
for pid in IDS:
    url = "https://api.datacite.org/dois/10.48550/arXiv." + pid
    target = ROOT / ("date-" + pid + ".json")
    run = subprocess.run(["curl", "--max-time", "10", "-sS", url, "-o", str(target), "-w", "%{http_code}"],
                         capture_output=True, text=True)
    receipt = {"url": url, "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
               "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
               "bytes": target.stat().st_size if target.exists() else 0,
               "stop": "one exact DOI; metadata creation and Submitted are not public"}
    (ROOT / ("date-" + pid + ".receipt.json")).write_text(json.dumps(receipt, indent=2))
    result = {"id": pid, **receipt}
    if run.returncode == 0 and run.stdout == "200":
        try:
            a = json.loads(target.read_text())["data"]["attributes"]
            result["date_fields"] = {k: a.get(k) for k in ("created", "registered", "published", "dates")}
        except (ValueError, KeyError):
            result["parse"] = "response did not contain expected attributes"
    print(json.dumps(result, ensure_ascii=False), flush=True)
