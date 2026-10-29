"""Reconcile new morphology responses against this day's existing identities."""
import hashlib
import importlib.util
import json
import re
import xml.etree.ElementTree as ET

from REPAIR_dates_20261021 import BASE, ROOT, save


DECISIONS = {
    "08832": ("EX", "Economic risk sharing, not model learning or AI system mechanisms."),
    "08835": ("C", "Opacity taxonomy and general privacy justification; no specific new mechanism or bounded failure evidence in the complete abstract."),
    "08839": ("P", "Crisis-response rubric separates empathy from actionable support and continued engagement; investigate evaluator/population validity. Explicit earlier Research Square preprint requires event recovery."),
    "08857": ("C", "Programming-education chatbot mapping catalog; no new execution or learning condition."),
    "08935": ("N", "Reader calibration reopens only SAMONAI single-point to zero-shot 3D prompt propagation: distinguish transferable representation mechanism from familiar domain adaptation. Do not review survival/clinical outcomes."),
    "08940": ("P", "Evolutionary search links inter-generator attribute divergence to prompt concepts; changes how conditional representation differences are tested."),
    "08950": ("C", "Signal-processing education primer and smart textbook; no concrete new system mechanism or causal evaluation boundary."),
    "08960": ("C", "Adds native Portuguese proverb questions; abstract reports no controlled translated/native comparison or new diagnostic result beyond regional-coverage motivation."),
    "08961": ("EX", "ECG disease classification module combination and clinical metrics; deferred scientific application."),
    "09001": ("P", "Approximate nearest-neighbor attention changes asymptotic cost while claiming MPC expressivity and depth simulation; verify exact assumptions."),
    "09043": ("P", "Re-engagement preference differs from abuse classification and depends on framing/transcript format; separate elicited signal from model state or consent."),
    "09103": ("N", "Crop application itself excluded; one necessary gate only for whether claimed DP introduces a transferable privacy mechanism/limitation, not a full application review."),
    "09131": ("C", "Known blockwise encoder and hard negatives adapted to Vietnamese; abstract supplies task gains without a new memory/quality condition or isolated mechanism."),
    "09146": ("EX", "ISP peering prediction application, not model-serving communication or new learning mechanism."),
    "09151": ("C", "Dataset-centric survey organizes established architectures by invariances; no new controlled evidence or specific design boundary established in abstract."),
    "09154": ("C", "Neuroscience analogy and six-module perspective; no implemented new spatial-learning mechanism or concrete failure test."),
    "09161": ("EX", "Astrophysical inference and waveform science; deferred AI for Science."),
    "09170": ("EX", "Economic information/design model for statistical decisions; no model-learning or AI-system relation beyond analogy."),
    "09177": ("P", "Sequence IS clipping scaled with sqrt(length) addresses length-dependent update distortion; verify fairness and directional guarantee."),
    "09190": ("C", "Challenge dataset and participant ranking summary; abstract supplies no controlled new scorer/recognition blind spot beyond added visual-quality tasks."),
    "09208": ("P", "Boundary-aware adaptive penalty modifies constrained policy optimization and asserts an optimality error bound; check assumptions and safety-vs-return tradeoff."),
    "09219": ("P", "Factored state/action message passing shares a policy across varying entity structures; investigate inductive generalization and abstraction limits, not merely RDDL scores."),
    "09229": ("EX", "Resume seniority classification application without a new transferable learning or inference mechanism."),
    "09234": ("C", "Example selection/SQL generation/verification/refinement pipeline and task accuracy; abstract does not identify a new control mechanism or ablation boundary."),
    "09252": ("EX", "Discrepancy and fair allocation mathematics, no AI model/system mechanism."),
    "09291": ("P", "LLM code-to-process translation feeds an independent symbolic verifier; distinguish translation fidelity from formal-model proof coverage."),
    "09307": ("EX", "Materials-characterization scientific benchmark; deferred AI for Science."),
    "09310": ("P", "Inference-time unlabeled adapter aligns heterogeneous collaborators without joint training; changes adaptation/state and full-cost assumptions."),
    "09337": ("P", "Anonymous-walk subgraphs route to structural experts with a claimed SWL expressivity separation; inspect learning/representation guarantee, not name-based MoE mapping."),
    "09360": ("P", "RAG factoid synonym/antonym mutations test evidence consistency and localize spans; mutation validity and context support are distinct from factual truth."),
    "09396": ("P", "Requested minimal counterfactual edits trade off with actual prediction changes; directly challenges self-explanation fidelity."),
    "09441": ("EX", "Traffic mechanism-design simulation; no new learned world model or AI execution mechanism."),
    "09467": ("C", "Legal RAG overview and consultative/human-oversight principles; no specific new retrieval or hallucination test mechanism."),
    "09473": ("EX", "Educational multilingual-content translation deployment, not new model/system mechanism."),
    "09482": ("P", "Database-view determinacy and learnable masks define relational-model explanations; investigate explanation sufficiency/granularity versus predictive fidelity."),
    "09509": ("C", "Open SLAM sensor platform with standard synchronization/calibration and trajectory benchmark; no new learned multimodal identity/consumer contract or controlled boundary."),
    "09560": ("P", "Perception/generation disaggregation and shared context trade pipeline frequency against stale inputs; inspect real consumer versions and end-to-end quality/cost."),
    "09561": ("EX", "Facility-location mechanism design for economic agents, not AI multi-agent execution."),
    "09584": ("N", "One narrow gate: whether event-stream grounding adds a representation/evaluation condition beyond a new dataset and attribute inventory; no automatic Methods queue."),
    "09602": ("EX", "Verbal-autopsy cause-of-death prediction application, deferred scientific use."),
    "09641": ("EX", "Fair allocation approximation for economic agents, not AI system agents."),
    "09658": ("P", "NOTA-aware rejection tests separate recognition from unsupported-choice rejection and prompt caution; verify diagnostic population and response-bias controls."),
}


def main():
    old = {row["id"] for row in json.loads((BASE / "REPAIR_discovery_20261021.json").read_text())}
    nav = set()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for name in ("arxiv-api.raw", "SUP_exact-v1_20261012.raw"):
        for entry in ET.parse(BASE / name).findall("a:entry", ns):
            nav.add(re.search(r"\d{4}\.\d{4,5}", entry.findtext("a:id", namespaces=ns)).group())
    spec = importlib.util.spec_from_file_location("arxiv_date", ROOT / "scripts/arxiv_publication_date.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = {}
    requests = []
    appearances = 0
    for path in sorted(BASE.glob("REPAIR_FORMS-*-p*_20261021.raw")):
        if "CONTROL" in path.name:
            continue
        body = path.read_bytes()
        record = json.loads(path.with_suffix(".request.json").read_text())
        assert record["status"] == 200 and record["bytes"] == len(body)
        assert record["sha256"] == hashlib.sha256(body).hexdigest()
        payload = json.loads(body)
        assert len(payload["data"]) == payload["meta"]["total"] and not payload["links"].get("next")
        requests.append({"raw": path.name, "returned": len(payload["data"]), "total": payload["meta"]["total"], "next": payload["links"].get("next"), "request": record})
        appearances += len(payload["data"])
        for resource in payload["data"]:
            key = resource["id"].lower().split("arxiv.")[-1]
            if key not in rows:
                rows[key] = {"id": key, "resource": resource, "themes": [], "old107": key in old, "old144": key in nav}
            rows[key]["themes"].append(path.name)
    assert old <= rows.keys()
    fresh = set(rows) - old - nav
    assert fresh == {"2509." + suffix for suffix in DECISIONS}
    counts = {}
    for key in sorted(fresh):
        decision, reason = DECISIONS[key.split(".")[1]]
        rows[key].update(initial_gate=decision, gate_reason=reason, date_result=module.publication_date_envelope(rows[key]["resource"], key))
        counts[decision] = counts.get(decision, 0) + 1
    output = {"scope": "Sep12 BJT registered window; four original themes expanded explicitly; discovery/admission only", "requests": requests, "appearances": appearances, "union": len(rows), "old107": len(old), "old144": len(nav), "delta_vs107": len(set(rows) - old), "already_old_nav_delta": sorted((set(rows) - old) & nav), "genuinely_new": sorted(fresh), "initial_gate_counts": counts, "rows": [rows[key] for key in sorted(rows)]}
    target = BASE / "REPAIR_forms_delta_calibrated_20261021.json"
    encoded = (json.dumps(output, ensure_ascii=False, indent=2) + "\n").encode()
    if target.exists():
        assert target.read_bytes() == encoded
    else:
        save(target, encoded)
    print(json.dumps({key: value for key, value in output.items() if key not in ("requests", "rows", "genuinely_new")}, ensure_ascii=False))
    for key in sorted(fresh):
        row = rows[key]
        print(key, row["initial_gate"], row["date_result"]["bounded_bjt_date"], row["date_result"]["reasons"])


if __name__ == "__main__":
    main()
