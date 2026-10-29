import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[4]
START = "2025-10-25T16:00:00Z"
END = "2025-10-26T15:59:59.999Z"
THEMES = {
    "model": ['language model', 'language models', 'foundation model', 'foundation models',
              'transformer', 'transformers', 'attention', 'mixture of experts', 'mixture-of-experts',
              'MoE', 'representation learning', 'scaling law', 'scaling laws', 'state space model', 'state-space models'],
    "training": ['pretraining', 'pre-training', 'posttraining', 'post-training', 'fine tuning',
                 'fine-tuning', 'finetuning', 'reinforcement learning', 'preference optimization',
                 'distillation', 'LoRA', 'GRPO', 'RLHF', 'PPO', 'DPO', 'continual learning'],
    "inference": ['inference', 'serving', 'decoding', 'KV cache', 'KV-cache', 'key value cache',
                  'key-value cache', 'quantization', 'speculative decoding', 'batching', 'prefill', 'offloading'],
    "compiler": ['GPU', 'GPUs', 'kernel', 'kernels', 'compiler', 'compilers', 'compilation',
                 'accelerator', 'accelerators', 'collective', 'collectives', 'communication',
                 'tensor parallel', 'pipeline parallel', 'all reduce', 'all-reduce', 'all-to-all', 'distributed training'],
    "multimodal": ['multimodal', 'multi-modal', 'vision language', 'vision-language',
                   'diffusion', 'flow matching', 'flow-matching', 'image generation',
                   'video generation', 'audio generation', 'speech generation', 'masked generation'],
    "world_vla": ['world model', 'world models', 'world-model', 'world-models',
                  'VLA', 'vision language action', 'vision-language-action', 'action model',
                  'action models', 'embodied', 'robot foundation', 'latent dynamics'],
    "agent": ['agent', 'agents', 'agentic', 'tool calling', 'tool-calling', 'tool use', 'tool-use',
              'retrieval augmented', 'retrieval-augmented', 'RAG', 'memory', 'planning',
              'reflection', 'multi agent', 'multi-agent', 'jailbreak', 'jailbreaking',
              'prompt injection', 'prompt-injection', 'alignment', 'unlearning'],
}


def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def fetch(name, url):
    raw = BASE / (name + ".raw")
    meta_path = BASE / (name + ".request.json")
    if raw.exists() and meta_path.exists():
        meta = json.loads(meta_path.read_text())
        if meta.get("status") == 200 and meta.get("url") == url:
            return json.loads(raw.read_bytes())
    meta = {"url": url, "checked_at": dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design historical source audit", "Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=25) as response:
            body = response.read()
            raw.write_bytes(body)
            meta.update(status=response.status, final_url=response.url,
                        content_type=response.headers.get("Content-Type"), bytes=len(body),
                        sha256=hashlib.sha256(body).hexdigest())
        result = json.loads(body)
    except Exception as error:
        meta.update(error=repr(error))
        save_json(meta_path, meta)
        print(name, "ERROR", repr(error), flush=True)
        return None
    save_json(meta_path, meta)
    return result


def expression(terms):
    return "(" + " OR ".join(f'{field}:"{term}"' for field in ["titles.title", "descriptions.description"] for term in terms) + ")"


def query(name, text):
    params = {"client-id": "arxiv.content", "query": text, "page[size]": 100,
              "page[number]": 1, "sort": "name"}
    result = fetch(name, "https://api.datacite.org/dois?" + urllib.parse.urlencode(params))
    if result is None:
        return None
    total = result.get("meta", {}).get("total")
    rows = result.get("data", [])
    print(name, "total", total, "rows", len(rows), "next", result.get("links", {}).get("next"), flush=True)
    if total is None or total > len(rows) or result.get("links", {}).get("next"):
        raise RuntimeError(f"{name}: unfinished pagination, do not claim completion")
    return result


def run():
    snapshot = BASE / "REPAIR_BASELINE_GIT_20261029.json"
    if not snapshot.exists():
        staged = subprocess.check_output(["git", "ls-files", "--stage"], cwd=ROOT)
        status = subprocess.check_output(["git", "status", "--porcelain=v1", "-uno"], cwd=ROOT).decode()
        save_json(snapshot, {"checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                            "branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT).decode().strip(),
                            "staged_listing_sha256": hashlib.sha256(staged).hexdigest(),
                            "tracked_status": status.splitlines(),
                            "report_sha256": hashlib.sha256((BASE / "REPAIR_BASELINE_20261029.md").read_bytes()).hexdigest()})
    summary = {}
    for field in ["registered", "created"]:
        summary[field] = {}
        for theme, terms in THEMES.items():
            name = f"REPAIR_DC_{field.upper()}_{theme.upper()}_20261029"
            text = f'{field}:[{START} TO {END}] AND ' + expression(terms)
            result = query(name, text)
            summary[field][theme] = None if result is None else [row["id"] for row in result["data"]]
            time.sleep(0.2)
    control = fetch("REPAIR_DC_CONTROL_EXACT_20261029", "https://api.datacite.org/dois/10.48550/arxiv.2510.21270")
    if control:
        a = control["data"]["attributes"]
        print("CONTROL", a.get("doi"), a.get("created"), a.get("registered"), a.get("state"), flush=True)
        control_day = a["registered"][:10]
        for field in ["registered", "created"]:
            q = f'doi:"10.48550/arxiv.2510.21270" AND {field}:[{control_day}T00:00:00Z TO {control_day}T23:59:59.999Z] AND ' + expression(THEMES["model"])
            query(f"REPAIR_DC_CONTROL_{field.upper()}_20261029", q)
    save_json(BASE / "REPAIR_DC_SUMMARY_20261029.json", summary)


if __name__ == "__main__":
    run()
