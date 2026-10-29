"""Bounded Sep12 morphology delta; responses never replace earlier discovery."""
import json
import sys
import urllib.parse

from REPAIR_dates_20261021 import BASE, capture


def text(terms):
    return "(titles.title:(" + terms + ") OR descriptions.description:(" + terms + "))"


LANGUAGE = '"language model" OR "language models" OR LLM OR LLMs OR LM OR LMs OR transformer OR transformers OR "foundation model" OR "foundation models" OR "mixture of experts" OR MoE'
THEMES = {
    "MODEL": text(LANGUAGE) + " AND " + text("architecture OR architectures OR attention OR optimizer OR optimizers OR training OR alignment OR quantization OR reinforcement OR confidence OR calibration"),
    "SYSTEM": text(LANGUAGE + " OR GPU OR GPUs") + " AND " + text("inference OR communication OR communications OR kernel OR kernels OR compiler OR compilers OR runtime OR runtimes OR serving OR parallel OR parallelism OR training"),
    "MULTI": text('"foundation model" OR "foundation models" OR "world model" OR "world models" OR "vision language" OR "vision-language" OR "vision-language models" OR "vision-language-action" OR "vision-language-action models" OR multimodal OR VLA OR VLAs OR VLM OR VLMs OR MLLM OR MLLMs') + " AND " + text("representation OR representations OR generation OR diffusion OR flow OR action OR actions OR training OR fusion OR evaluation OR reasoning OR navigation"),
    "AGENT": text(LANGUAGE + " OR agent OR agents OR agentic") + " AND " + text("agent OR agents OR agentic OR retrieval OR memory OR memories OR safety OR jailbreak OR jailbreaks OR planning OR tool OR tools OR tool-calling"),
}
WINDOW = "registered:[2025-09-11T16:00:00Z TO 2025-09-12T15:59:59.999Z]"


def run(name, query):
    params = {"client-id": "arxiv.content", "query": query + " AND " + WINDOW, "page[size]": 100, "sort": "registered"}
    url = "https://api.datacite.org/dois?" + urllib.parse.urlencode(params)
    seen = set()
    for page in range(1, 11):
        assert url not in seen, "repeated page URL"
        seen.add(url)
        body, record = capture("FORMS-" + name + "-p" + str(page), url)
        assert record.get("status") == 200, record
        payload = json.loads(body)
        print(name, page, "returned", len(payload["data"]), "total", payload["meta"]["total"], "next", payload.get("links", {}).get("next"), flush=True)
        url = payload.get("links", {}).get("next")
        if not url:
            return
    raise RuntimeError("bounded 10-page limit reached; coverage remains open")


if __name__ == "__main__":
    if sys.argv[1:2] == ["controls"]:
        controls = [
            ("LANGUAGE-MODELS", "language models", "2509.09215"),
            ("FOUNDATION-MODELS", "foundation models", "2509.09151"),
            ("TRANSFORMERS", "transformers", "2509.08897"),
            ("AGENTS", "agents", "2509.09215"),
            ("AGENTIC", "agentic", "2509.09505"),
            ("TOOLS", "tools", "2509.09286"),
            ("KERNELS", "kernels", "2509.09337"),
            ("COMPILER", "compiler", "2509.09505"),
        ]
        for name, form, identity in controls:
            run("CONTROL-" + name, text('"' + form + '"') + ' AND doi:"10.48550/arxiv.' + identity + '"')
    elif sys.argv[1:2] == ["control"]:
        name, form, identity = sys.argv[2:]
        run("CONTROL-" + name, text('"' + form + '"') + ' AND doi:"10.48550/arxiv.' + identity + '"')
    else:
        for name in sys.argv[1:] or THEMES:
            run(name, THEMES[name])
