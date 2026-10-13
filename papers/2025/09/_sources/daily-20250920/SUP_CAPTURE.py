import datetime
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent


def capture(name, url, data=None):
    path = ROOT / (name + ".raw")
    meta = ROOT / (name + ".request.json")
    if path.exists() or meta.exists():
        raise RuntimeError("capture already exists: " + name)
    args = ["curl", "-L", "--max-time", "25", "-sS", "-o", str(path),
            "-w", "%{http_code}", url]
    if data is not None:
        args += ["-H", "Content-Type: application/json", "--data", data]
    at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(args, capture_output=True, text=True)
    raw = path.read_bytes() if path.exists() else b""
    if not path.exists():
        path.write_bytes(raw)
    record = dict(at=at, url=url, method="POST" if data else "GET",
                  data=data, status=result.stdout, exit=result.returncode,
                  error=result.stderr, file=path.name, bytes=len(raw),
                  sha256=hashlib.sha256(raw).hexdigest())
    meta.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(record, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("url")
    parser.add_argument("--data")
    args = parser.parse_args()
    capture(args.name, args.url, args.data)
