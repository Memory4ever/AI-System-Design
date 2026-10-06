import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent


def capture(name, url, data=None, timeout=20):
    raw_path = ROOT / (name + ".raw")
    meta_path = ROOT / (name + ".request.json")
    if raw_path.exists() or meta_path.exists():
        raise RuntimeError("capture already exists: " + name)
    args = ["curl", "-L", "--max-time", str(timeout), "-sS", "-o", str(raw_path),
            "-w", "%{http_code}", url]
    if data is not None:
        args += ["-H", "Content-Type: application/json", "--data", data]
    at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(args, capture_output=True, text=True)
    raw = raw_path.read_bytes() if raw_path.exists() else b""
    if not raw_path.exists():
        raw_path.write_bytes(raw)
    meta = dict(at=at, url=url, method="POST" if data else "GET", data=data,
                status=result.stdout, exit=result.returncode, error=result.stderr,
                file=raw_path.name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(meta, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("url")
    parser.add_argument("--data")
    parser.add_argument("--timeout", type=int, default=20)
    options = parser.parse_args()
    capture(options.name, options.url, options.data, options.timeout)
