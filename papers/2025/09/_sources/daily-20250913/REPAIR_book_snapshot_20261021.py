"""Capture current authorized preimages; never use them to roll back others."""
from pathlib import Path
import datetime
import hashlib
import json
import sys

base = Path(__file__).parent
root = base.parents[4]
paths = {
    "cde-ch32": "books/part-04-training-system/32-ppo.md",
    "af1-ch17": "books/part-02-model/17-transformer-layer.md",
    "kling-ch24": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "diflow-ch24": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "steer-ch21": "books/part-02-model/21-moe.md",
    "ret2-ch76": "books/part-07-agent/76-rag.md",
    "simple-ch26": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "gadms-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "adaptive-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "termi-ch77": "books/part-07-agent/77-memory.md",
    "progd-ch25": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "opensci-ch7": "books/part-01-worldview/07-scaling-law.md",
    "mruie-ch27": "books/part-04-training-system/27-data.md",
    "sqap-ch26": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "rrbench-ch66": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "echox-ch24": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "bargaining-ch82": "books/part-07-agent/82-multi-agent.md",
    "sbp-ch81": "books/part-07-agent/81-workflow.md",
    "uoisc-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "sensible-ch81": "books/part-07-agent/81-workflow.md",
    "date-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "visualprog-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "dualread-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "sparsepiano-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "spice-ch66": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "auras-ch26": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "omnieva-ch26": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "sce-ch66": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "samonai-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "compcon-ch66": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "phcp-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "vlaadapter-ch26": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "grace-ch66": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "plena-ch54": "books/part-05-inference-system/54-gpu-memory.md",
    "trenv-ch57": "books/part-06-ai-infrastructure/57-what-is-ai-platform.md",
    "fsdiff-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "align4gen-ch24": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "neucodec-ch23": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
}
for name, relative in paths.items():
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue
    data = (root / relative).read_bytes()
    target = base / ("REPAIR_before-" + name + "_20261021.raw")
    with target.open("xb") as stream:
        stream.write(data)
    record = {
        "path": relative,
        "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
        "purpose": "Fresh root-authorized one paragraph, independent marker, Carson note only",
    }
    with target.with_suffix(".request.json").open("x") as stream:
        json.dump(record, stream, indent=2)
        stream.write("\n")
    print(json.dumps(record))
