"""Preserve finite same-day metadata queries, without deciding public dates."""
import datetime
import json
import pathlib
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).parent
WINDOW = "[2025-10-24T16:00:00Z TO 2025-10-25T15:59:59Z]"
TOPICS = {
    "MODEL": 'transformer OR "mixture of experts" OR distillation OR pretraining OR "language model training"',
    "AGENT": 'agent OR agentic OR "retrieval augmented" OR "language model memory"',
    "MULTIMODAL": '"world model" OR "vision language" OR diffusion OR autoregressive OR "multimodal foundation"',
    "SYSTEM": '"LLM serving" OR "LLM inference" OR "GPU kernel" OR "distributed training" OR "KV cache" OR "speculative decoding"',
    "EVAL": '"language model evaluation" OR "prompt injection" OR "language model safety" OR "language model benchmark"',
    "POSTTRAIN": '"reinforcement learning" OR GRPO OR RLVR OR "post-training" OR "fine-tuning"',
    "RUNTIME": 'quantization OR offloading OR routing OR prefill OR cache',
}
if "--synonyms" in sys.argv:
    TOPICS = {
        "MODEL": 'transformer OR transformers OR "mixture of experts" OR "mixture-of-experts" OR distillation OR pretraining OR "pre-training" OR "language model training"',
        "AGENT": 'agent OR agents OR agentic OR "retrieval augmented" OR "retrieval-augmented" OR "language model memory"',
        "MULTIMODAL": '"world model" OR "world models" OR "world-model" OR "vision language" OR "vision-language" OR diffusion OR autoregressive OR "auto-regressive" OR "multimodal foundation" OR "multi-modal foundation"',
        "SYSTEM": '"LLM serving" OR "LLM inference" OR "large language model serving" OR "large language model inference" OR "GPU kernel" OR "GPU kernels" OR "distributed training" OR "KV cache" OR "KV-cache" OR "speculative decoding"',
        "EVAL": '"language model evaluation" OR "language models evaluation" OR "prompt injection" OR "prompt-injection" OR "language model safety" OR "language model benchmark" OR "language model benchmarks"',
        "POSTTRAIN": '"reinforcement learning" OR "reinforcement-learning" OR GRPO OR RLVR OR "post-training" OR "post training" OR "fine-tuning" OR "fine tuning" OR finetuning',
        "RUNTIME": 'quantization OR quantisation OR offloading OR "off-loading" OR routing OR prefill OR "pre-fill" OR cache OR caching OR caches',
    }

for field in ("registered", "created"):
    for topic, terms in TOPICS.items():
        query = f"{field}:{WINDOW} AND titles.title:({terms})"
        params = {"client-id": "arxiv.content", "query": query, "page[size]": 100}
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode(params)
        variant = "SYNONYM_" if "--synonyms" in sys.argv else ""
        stem = ROOT / f"REPAIR_{field.upper()}_{variant}{topic}_20261029"
        request = {"url": url, "params": params, "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                raw = response.read()
                request.update(status=response.status, final_url=response.url, bytes=len(raw))
            stem.with_suffix(".raw.json").write_bytes(raw)
            result = json.loads(raw)
            rows = []
            for item in result.get("data", []):
                a = item["attributes"]
                rows.append({"id": item["id"], "title": a.get("titles"), "created": a.get("created"), "registered": a.get("registered"), "state": a.get("state"), "client": item.get("relationships", {}).get("client"), "subjects": a.get("subjects"), "descriptions": a.get("descriptions")})
            request.update(total=result.get("meta", {}).get("total"), returned=len(rows), next=result.get("links", {}).get("next"))
            stem.with_suffix(".projection.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
            print(field, topic, json.dumps(request, ensure_ascii=False), flush=True)
            for row in rows:
                print(json.dumps(row, ensure_ascii=False), flush=True)
        except Exception as error:
            request["error"] = str(error)
            print(field, topic, json.dumps(request), flush=True)
        stem.with_suffix(".request.json").write_text(json.dumps(request, ensure_ascii=False, indent=2) + "\n")
