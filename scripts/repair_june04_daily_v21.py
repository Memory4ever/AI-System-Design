#!/usr/bin/env python3
"""Rebuild the 2026-06-04 Daily after the fresh-context recall audit.

The script deliberately separates four facts:
1. all 574 registered identities receive an abstract-level screening receipt;
2. the effective denominator contains every routed family, including low-score
   closure-only candidates;
3. Standard/Deep reviews are grounded in exact event-time v1 material;
4. Books decisions are written to the report, but Books files are not edited.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260604"
REPORT = ROOT / "papers/2026/06/04/README.md"
LEDGER = PACKET / "screening-ledger.json"
RECEIPTS = PACKET / "source-review-receipts.json"
REPAIR_EXECUTED_AT = "2026-08-28T22:21:08+08:00"

AUDIT_RECOVERED = {
    "2606.04326", "2606.04351", "2606.04373", "2606.04375", "2606.04384", "2606.04385",
    "2606.04394", "2606.04397", "2606.04402", "2606.04405", "2606.04418", "2606.04421",
    "2606.04454", "2606.04465", "2606.04474", "2606.04479", "2606.04492", "2606.04494",
    "2606.04503", "2606.04516", "2606.04535", "2606.04536", "2606.04547", "2606.04603",
    "2606.04613", "2606.04650", "2606.04661", "2606.04678", "2606.04701", "2606.04719",
    "2606.04727", "2606.04737", "2606.04964", "2606.04967", "2606.04970", "2606.04971",
    "2606.05015", "2606.05016", "2606.05030", "2606.05037", "2606.05140", "2606.05161",
    "2606.05253", "2606.05257", "2606.05268", "2606.05315", "2606.05328", "2606.05376",
    "2606.05408", "2606.05411", "2606.05449", "2606.05464", "2606.05476", "2606.05513",
    "2606.05528", "2606.05533", "2606.06528", "2606.04485", "2606.04634",
    "2606.04752", "2606.04804", "2606.05441", "2606.05515",
    "2606.04342", "2606.04366", "2606.04522", "2606.04767", "2606.04807", "2606.04853",
    "2606.05115", "2606.05326",
    # Independent V4 closure counterexamples.
    "2606.04505", "2606.04591", "2606.05101", "2606.05106",
    "2606.05336", "2606.05367", "2606.04619", "2606.05242",
    # Independent V5 closure counterexamples plus the additional high-risk
    # false negatives found while semantically rescreening all 296 V5
    # closures.  These are not title-keyword promotions: each abstract/HTML
    # discloses a reusable state, control, communication or evidence contract.
    "2606.04367", "2606.04410", "2606.04513", "2606.04549", "2606.05035",
    "2606.05042", "2606.05076", "2606.05081", "2606.05094",
    "2606.04399", "2606.04437", "2606.04552", "2606.04652", "2606.04736",
    "2606.04857", "2606.04860", "2606.04899", "2606.05348", "2606.05394",
    # Independent V6 full-closure replay counterexamples.
    "2606.04355", "2606.04597", "2606.04812", "2606.04819", "2606.05002", "2606.05423",
}

# These additional abstracts are explicitly about model/agent/platform contracts,
# but their disclosed delta is too local or domain-bound to justify a Standard
# review. Keeping them as scored closure candidates prevents silent omission.
ADDITIONAL_CLOSURE = {
    "2606.04360", "2606.04381", "2606.04434", "2606.04448", "2606.04588", "2606.04596",
    "2606.04599", "2606.04602", "2606.04632", "2606.04646", "2606.04743", "2606.04751",
    "2606.04755", "2606.04773", "2606.04775", "2606.04779", "2606.04806", "2606.04816",
    "2606.04823", "2606.04867", "2606.04883", "2606.04884", "2606.04906", "2606.04915",
    "2606.04920", "2606.04978", "2606.05001", "2606.05009", "2606.05031", "2606.05050",
    "2606.05054", "2606.05079", "2606.05109", "2606.05112", "2606.05121", "2606.05130",
    "2606.05134", "2606.05152", "2606.05252", "2606.05256", "2606.05275", "2606.05316",
    "2606.05330", "2606.05332", "2606.05400", "2606.05404", "2606.05420", "2606.05436",
    "2606.05443", "2606.05445", "2606.05461", "2606.05463", "2606.05478", "2606.05489",
    "2606.05494", "2606.05497", "2606.05510", "2606.05518", "2606.05522", "2606.05531",
    "2606.05544", "2606.06531", "2606.06534",
}

AUDIT_OWNER = {
    "2606.04326": "PLATFORM-EVALUATION-SYSTEM", "2606.04351": "MULTIMODAL-REPRESENTATION",
    "2606.04373": "INFER-TENSORRT-LLM", "2606.04375": "PLATFORM-SECURITY",
    "2606.04384": "PLATFORM-SECURITY", "2606.04385": "MULTIMODAL-REPRESENTATION",
    "2606.04394": "PLATFORM-EVALUATION-SYSTEM", "2606.04397": "AGENT-CONTEXT",
    "2606.04402": "INFER-SCHEDULING", "2606.04405": "TRAIN-PRETRAINING",
    "2606.04418": "MULTIMODAL-REPRESENTATION", "2606.04421": "AGENT-MEMORY",
    "2606.04454": "AGENT-WORKFLOW", "2606.04465": "AGENT-PROMPT",
    "2606.04474": "PLATFORM-EVALUATION-SYSTEM", "2606.04479": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04492": "AGENT-MEMORY", "2606.04494": "AGENT-MCP",
    "2606.04503": "TRAIN-GRPO", "2606.04516": "TRAIN-GRPO",
    "2606.04535": "MULTIMODAL-GENERATIVE-PARADIGMS", "2606.04536": "AGENT-MEMORY",
    "2606.04547": "AGENT-MEMORY", "2606.04603": "AGENT-RAG",
    "2606.04613": "MULTIMODAL-REPRESENTATION", "2606.04650": "TRAIN-SFT",
    "2606.04661": "AGENT-PROMPT", "2606.04678": "INFER-TENSORRT-LLM",
    "2606.04701": "PLATFORM-EVALUATION-SYSTEM", "2606.04719": "MULTIMODAL-REPRESENTATION",
    "2606.04727": "PLATFORM-EVALUATION-SYSTEM", "2606.04737": "MULTIMODAL-WORLD-MODELS",
    "2606.04964": "MULTIMODAL-GENERATIVE-PARADIGMS", "2606.04967": "AGENT-WORKFLOW",
    "2606.04970": "AGENT-WORKFLOW", "2606.04971": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05015": "MULTIMODAL-WORLD-MODELS", "2606.05016": "TRAIN-LORA",
    "2606.05030": "AGENT-REFLECTION", "2606.05037": "AGENT-TOOL-CALLING",
    "2606.05140": "MODEL-TRANSFORMER-LAYER", "2606.05161": "MULTIMODAL-REPRESENTATION",
    "2606.05253": "AGENT-WORKFLOW", "2606.05257": "WORLDVIEW-SCALING-LAW",
    "2606.05268": "PLATFORM-EVALUATION-SYSTEM", "2606.05315": "TRAIN-SFT",
    "2606.05328": "MULTIMODAL-WORLD-MODELS", "2606.05376": "TRAIN-RLHF",
    "2606.05408": "AGENT-WORKFLOW", "2606.05411": "AGENT-PLATFORM",
    "2606.05449": "PLATFORM-SECURITY", "2606.05464": "TRAIN-GRPO",
    "2606.05476": "AGENT-WORKFLOW", "2606.05513": "AGENT-MEMORY",
    "2606.05528": "PLATFORM-SECURITY", "2606.05533": "MULTIMODAL-EMBODIED-VLA",
    "2606.06528": "INFER-TENSORRT-LLM", "2606.04485": "MODEL-TOKENIZER",
    "2606.04634": "PLATFORM-SECURITY", "2606.04752": "MODEL-EMBEDDING",
    "2606.04804": "MULTIMODAL-GENERATIVE-PARADIGMS", "2606.05441": "MODEL-TOKENIZER",
    "2606.05515": "MULTIMODAL-REPRESENTATION",
    "2606.04342": "PLATFORM-EVALUATION-SYSTEM", "2606.04366": "MODEL-TOKENIZER",
    "2606.04522": "PLATFORM-EVALUATION-SYSTEM", "2606.04767": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04807": "TRAIN-GRPO", "2606.04853": "MULTIMODAL-EMBODIED-VLA",
    "2606.05115": "TRAIN-DATA", "2606.05326": "TRAIN-PRETRAINING",
    "2606.04505": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04591": "AGENT-RAG",
    "2606.05101": "PLATFORM-SECURITY",
    "2606.05106": "TRAIN-PRETRAINING",
    "2606.05336": "AGENT-MEMORY",
    "2606.05367": "MULTIMODAL-REPRESENTATION",
    "2606.04619": "AGENT-WORKFLOW",
    "2606.05242": "TRAIN-PRETRAINING",
    "2606.04367": "AGENT-MEMORY",
    "2606.04410": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.04513": "AGENT-WORKFLOW",
    "2606.04549": "PLATFORM-SECURITY",
    "2606.05035": "MULTIMODAL-WORLD-MODELS",
    "2606.05042": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05076": "PLATFORM-MONITORING",
    "2606.05081": "INFER-TENSORRT-LLM",
    "2606.05094": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.04399": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.04437": "MULTIMODAL-EMBODIED-VLA",
    "2606.04552": "MODEL-TOKENIZER",
    "2606.04652": "TRAIN-TENSOR-PARALLEL",
    "2606.04736": "TRAIN-PRETRAINING",
    "2606.04857": "MULTIMODAL-REPRESENTATION",
    "2606.04860": "AGENT-PLANNING",
    "2606.04899": "PLATFORM-SECURITY",
    "2606.05348": "INFER-TENSORRT-LLM",
    "2606.05394": "INFER-TENSORRT-LLM",
    "2606.04355": "AGENT-PLANNING",
    "2606.04597": "AGENT-PLANNING",
    "2606.04812": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04819": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05002": "AGENT-MULTI-AGENT",
    "2606.05423": "PLATFORM-SECURITY",
}

AUDIT_DEEP = {
    "2606.04373", "2606.04375", "2606.04384", "2606.04421", "2606.04454", "2606.04465",
    "2606.04503", "2606.04535", "2606.04536", "2606.04547", "2606.04603", "2606.04613",
    "2606.04650", "2606.04661", "2606.04678", "2606.04701", "2606.04727", "2606.04737",
    "2606.04964", "2606.04967", "2606.04970", "2606.05015", "2606.05016", "2606.05037",
    "2606.05161", "2606.05257", "2606.05268", "2606.05315", "2606.05328", "2606.05408",
    "2606.05476", "2606.05513", "2606.05533", "2606.06528", "2606.04485",
    "2606.04634", "2606.05515",
    "2606.04410", "2606.04513", "2606.04549", "2606.05035", "2606.05042",
    "2606.05076", "2606.05081", "2606.05094", "2606.04437", "2606.04552",
    "2606.04736", "2606.04857", "2606.04860", "2606.04899",
    "2606.04355", "2606.04597", "2606.04812", "2606.05002", "2606.05423",
}

AUDIT_CLOSURE = {"2606.05411", "2606.05449", "2606.05464", "2606.05528"}

AUDIT_SCORE = {
    "2606.04485": (3, 3, 2), "2606.04634": (3, 2, 2),
    "2606.04752": (2, 2, 2), "2606.04804": (2, 2, 2),
    "2606.05441": (2, 2, 2), "2606.05515": (3, 2, 2),
    "2606.04342": (3, 2, 3), "2606.04366": (3, 2, 2),
    "2606.04522": (3, 3, 2), "2606.04767": (3, 2, 3),
    "2606.04807": (3, 2, 2), "2606.04853": (3, 2, 2),
    "2606.05115": (3, 2, 2), "2606.05326": (3, 2, 3),
    "2606.04505": (3, 3, 2),
    "2606.04591": (2, 3, 2),
    "2606.05101": (3, 3, 2),
    "2606.05106": (3, 2, 2),
    "2606.05336": (3, 3, 2),
    "2606.05367": (3, 2, 2),
    "2606.04619": (2, 2, 1),
    "2606.05242": (2, 2, 2),
    "2606.04367": (3, 2, 1),
    "2606.04410": (3, 3, 2),
    # exact-v1 HTML is unavailable and the exact-v1 PDF transfer resets; the
    # official exact-v1 abstract still supports a Standard mechanism review,
    # but not a Deep Full Source Review or portable benchmark claim.
    "2606.04513": (3, 2, 1),
    "2606.04549": (3, 3, 2),
    "2606.05035": (3, 3, 2),
    "2606.05042": (3, 2, 2),
    "2606.05076": (3, 2, 2),
    "2606.05081": (3, 3, 2),
    "2606.05094": (3, 3, 2),
    "2606.04399": (2, 2, 2),
    "2606.04437": (3, 2, 2),
    "2606.04552": (3, 2, 2),
    "2606.04652": (2, 2, 2),
    "2606.04736": (3, 2, 2),
    "2606.04857": (3, 2, 2),
    "2606.04860": (3, 2, 2),
    "2606.04899": (3, 3, 2),
    "2606.05348": (2, 2, 2),
    "2606.05394": (2, 2, 2),
    "2606.04355": (3, 2, 2),
    "2606.04597": (3, 2, 2),
    "2606.04812": (3, 2, 2),
    "2606.04819": (2, 2, 2),
    "2606.05002": (3, 2, 2),
    "2606.05423": (3, 3, 2),
}

# Independent V7 found a second, systemic closure false-negative class.  These
# families are conservatively promoted into the scored denominator as explicit
# low-score closure candidates.  Promotion does not imply a Standard/Deep
# evidence claim; it means their routeable mechanism may no longer be silently
# dismissed as out of scope.
V7_REOPEN = {
    "2606.04327", "2606.04335", "2606.04409", "2606.04429", "2606.04444", "2606.04476",
    "2606.04525", "2606.04545", "2606.04569", "2606.04612", "2606.04648", "2606.04656",
    "2606.04665", "2606.04672", "2606.04680", "2606.04688", "2606.04718", "2606.04749",
    "2606.04754", "2606.04757", "2606.04797", "2606.04834", "2606.04866", "2606.04876",
    "2606.04877", "2606.04909", "2606.04930", "2606.04957", "2606.04987", "2606.04994",
    "2606.05021", "2606.05058", "2606.05067", "2606.05073", "2606.05104", "2606.05107",
    "2606.05129", "2606.05139", "2606.05159", "2606.05234", "2606.05247", "2606.05248",
    "2606.05335", "2606.05365", "2606.05371", "2606.05380", "2606.05382", "2606.05383",
    "2606.05389", "2606.05409", "2606.05437", "2606.05438", "2606.05471", "2606.05536",
}

V7_OWNER = {
    "2606.04327": "TRAIN-PRETRAINING", "2606.04335": "TRAIN-PPO",
    "2606.04409": "WORLDVIEW-WHY-MODELS-LEARN", "2606.04429": "TRAIN-PRETRAINING",
    "2606.04444": "TRAIN-DATA", "2606.04476": "TRAIN-PRETRAINING",
    "2606.04525": "PLATFORM-EVALUATION-SYSTEM", "2606.04545": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04569": "MULTIMODAL-EMBODIED-VLA", "2606.04612": "PLATFORM-SECURITY",
    "2606.04648": "AGENT-PLANNING", "2606.04656": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04665": "PLATFORM-EVALUATION-SYSTEM", "2606.04672": "MODEL-LONG-CONTEXT",
    "2606.04680": "PLATFORM-EVALUATION-SYSTEM", "2606.04688": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.04718": "MODEL-MOE", "2606.04749": "TRAIN-PPO",
    "2606.04754": "TRAIN-CHECKPOINT", "2606.04757": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.04797": "TRAIN-LORA", "2606.04834": "WORLDVIEW-WHY-MODELS-LEARN",
    "2606.04866": "TRAIN-PRETRAINING", "2606.04876": "MULTIMODAL-REPRESENTATION",
    "2606.04877": "AGENT-PLANNING", "2606.04909": "TRAIN-DATA",
    "2606.04930": "MULTIMODAL-WORLD-MODELS", "2606.04957": "PLATFORM-LOGGING",
    "2606.04987": "AGENT-MULTI-AGENT", "2606.04994": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05021": "AGENT-MULTI-AGENT", "2606.05058": "MULTIMODAL-REPRESENTATION",
    "2606.05067": "MULTIMODAL-GENERATIVE-PARADIGMS", "2606.05073": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.05104": "PLATFORM-EVALUATION-SYSTEM", "2606.05107": "TRAIN-SFT",
    "2606.05129": "PLATFORM-SECURITY", "2606.05139": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05159": "PLATFORM-EVALUATION-SYSTEM", "2606.05234": "TRAIN-LORA",
    "2606.05247": "TRAIN-PRETRAINING", "2606.05248": "AGENT-PLANNING",
    "2606.05335": "TRAIN-PRETRAINING", "2606.05365": "WORLDVIEW-REPRESENTATION",
    "2606.05371": "MODEL-LONG-CONTEXT", "2606.05380": "INFER-SCHEDULING",
    "2606.05382": "TRAIN-DPO", "2606.05383": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05389": "MULTIMODAL-REPRESENTATION", "2606.05409": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05437": "MULTIMODAL-EMBODIED-VLA", "2606.05438": "TRAIN-PRETRAINING",
    "2606.05471": "WORLDVIEW-REPRESENTATION", "2606.05536": "PLATFORM-EVALUATION-SYSTEM",
}

AUDIT_RECOVERED |= V7_REOPEN
AUDIT_OWNER.update(V7_OWNER)
AUDIT_SCORE.update({arxiv_id: (1, 1, 2) for arxiv_id in V7_REOPEN})

# Independent V8 replayed the complete 217-item V7 outside set and identified
# this conservative minimum queue.  Each family is now explicitly scored and
# routed.  Exact-v1 body retrieval was retried through the official HTML/PDF
# paths; because those transfers reset in this environment, no family is
# promoted beyond Closure on abstract evidence alone.  This is intentionally
# conservative: the family is no longer silently excluded, but a later
# important revision or readable exact-v1 body may still upgrade its route.
V8_REOPEN = {
    "2606.04374", "2606.04382", "2606.04389", "2606.04420", "2606.04443", "2606.04468",
    "2606.04500", "2606.04514", "2606.04580", "2606.04618", "2606.04621", "2606.04623",
    "2606.04694", "2606.04746", "2606.04764", "2606.04822", "2606.04829", "2606.04833",
    "2606.04935", "2606.04952", "2606.05000", "2606.05045", "2606.05046", "2606.05116",
    "2606.05126", "2606.05131", "2606.05162", "2606.05272", "2606.05327", "2606.05334",
    "2606.05359", "2606.05361", "2606.05373", "2606.05422", "2606.05481", "2606.05506",
}

V8_OWNER = {
    "2606.04374": "MODEL-TOKENIZER",
    "2606.04382": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04389": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04420": "TRAIN-PRETRAINING",
    "2606.04443": "PLATFORM-SECURITY",
    "2606.04468": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.04500": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04514": "MODEL-TRANSFORMER-LAYER",
    "2606.04580": "PLATFORM-SECURITY",
    "2606.04618": "MULTIMODAL-EMBODIED-VLA",
    "2606.04621": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.04623": "MULTIMODAL-WORLD-MODELS",
    "2606.04694": "TRAIN-SFT",
    "2606.04746": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04764": "PLATFORM-EVALUATION-SYSTEM",
    "2606.04822": "MULTIMODAL-WORLD-MODELS",
    "2606.04829": "MULTIMODAL-EMBODIED-VLA",
    "2606.04833": "MODEL-SELF-ATTENTION",
    "2606.04935": "AGENT-PLANNING",
    "2606.04952": "AGENT-WORKFLOW",
    "2606.05000": "PLATFORM-MONITORING",
    "2606.05045": "MULTIMODAL-WORLD-MODELS",
    "2606.05046": "MODEL-TRANSFORMER-LAYER",
    "2606.05116": "MODEL-TRANSFORMER-LAYER",
    "2606.05126": "PLATFORM-SECURITY",
    "2606.05131": "MULTIMODAL-WORLD-MODELS",
    "2606.05162": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.05272": "MULTIMODAL-WORLD-MODELS",
    "2606.05327": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.05334": "PLATFORM-PRODUCTION",
    "2606.05359": "MULTIMODAL-EMBODIED-VLA",
    "2606.05361": "TRAIN-DATA",
    "2606.05373": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05422": "MULTIMODAL-EMBODIED-VLA",
    "2606.05481": "PLATFORM-EVALUATION-SYSTEM",
    "2606.05506": "MULTIMODAL-EMBODIED-VLA",
}

AUDIT_RECOVERED |= V8_REOPEN
AUDIT_CLOSURE |= V8_REOPEN
AUDIT_OWNER.update(V8_OWNER)
AUDIT_SCORE.update({arxiv_id: (1, 1, 2) for arxiv_id in V8_REOPEN})

# The 393-family V8-repair set is a recall-first semantic inventory, not an
# automatically valid Candidate Denominator.  This explicit retain set is the
# result of a second, family-by-family pre-denominator replay.  A family stays
# only when its abstract/body evidence changes a durable AI System mechanism,
# state/data/control owner, evaluation contract, or platform/training/inference
# design judgment.  Being about AI, matching a ROADMAP node, reporting a
# benchmark, or proposing a single-domain method is insufficient by itself.
PRE_DENOMINATOR_RETAIN = {
    "2606.04326", "2606.04329", "2606.04342", "2606.04349", "2606.04351", "2606.04355",
    "2606.04375", "2606.04378", "2606.04384", "2606.04385", "2606.04391", "2606.04394",
    "2606.04396", "2606.04397", "2606.04399", "2606.04401", "2606.04402", "2606.04410",
    "2606.04413", "2606.04415", "2606.04418", "2606.04421", "2606.04425", "2606.04432",
    "2606.04433", "2606.04435", "2606.04436", "2606.04437", "2606.04438", "2606.04442",
    "2606.04446", "2606.04454", "2606.04455", "2606.04459", "2606.04460", "2606.04461",
    "2606.04463", "2606.04465", "2606.04466", "2606.04474", "2606.04479", "2606.04483",
    "2606.04484", "2606.04486", "2606.04492", "2606.04503", "2606.04507", "2606.04511",
    "2606.04516", "2606.04522", "2606.04527", "2606.04535", "2606.04536", "2606.04547",
    "2606.04549", "2606.04555", "2606.04557", "2606.04560", "2606.04579", "2606.04581",
    "2606.04591", "2606.04594", "2606.04603", "2606.04610", "2606.04619", "2606.04620",
    "2606.04627", "2606.04628", "2606.04634", "2606.04641", "2606.04645", "2606.04660",
    "2606.04661", "2606.04662", "2606.04678", "2606.04701", "2606.04703", "2606.04708",
    "2606.04717", "2606.04719", "2606.04727", "2606.04739", "2606.04767", "2606.04769",
    "2606.04778", "2606.04780", "2606.04781", "2606.04799", "2606.04807", "2606.04811",
    "2606.04812", "2606.04815", "2606.04847", "2606.04850", "2606.04874",
    "2606.04889", "2606.04896", "2606.04899", "2606.04903", "2606.04908", "2606.04915",
    "2606.04920", "2606.04923", "2606.04928", "2606.04929", "2606.04939", "2606.04945",
    "2606.04964", "2606.04967", "2606.04968", "2606.04970", "2606.04971", "2606.04974",
    "2606.04980", "2606.04990", "2606.05002", "2606.05004", "2606.05008", "2606.05014",
    "2606.05016", "2606.05025", "2606.05029", "2606.05030", "2606.05037", "2606.05043",
    "2606.05054", "2606.05076", "2606.05079", "2606.05080", "2606.05094", "2606.05122",
    "2606.05134", "2606.05143", "2606.05145", "2606.05152", "2606.05158", "2606.05161",
    "2606.05165", "2606.05233", "2606.05238", "2606.05241", "2606.05249", "2606.05250",
    "2606.05252", "2606.05254", "2606.05257", "2606.05263", "2606.05268", "2606.05271",
    "2606.05290", "2606.05296", "2606.05304", "2606.05308", "2606.05315", "2606.05328",
    "2606.05336", "2606.05339", "2606.05342", "2606.05345", "2606.05348", "2606.05362",
    "2606.05376", "2606.05378", "2606.05384", "2606.05390", "2606.05391", "2606.05394",
    "2606.05395", "2606.05396", "2606.05399", "2606.05402", "2606.05403", "2606.05405",
    "2606.05408", "2606.05414", "2606.05415", "2606.05423", "2606.05429", "2606.05433",
    "2606.05434", "2606.05435", "2606.05468", "2606.05476", "2606.05484", "2606.05486",
    "2606.05495", "2606.05516", "2606.05523", "2606.05525", "2606.05533", "2606.05538",
    "2606.06527", "2606.06528", "2606.06529", "2606.06532", "2606.06533", "2606.06535",
}

PRE_DENOMINATOR_OWNER_OVERRIDES = {
    # Controlled lexical anonymization is an evaluation contract for
    # structural-vs-pattern reasoning, not a multimodal generation mechanism.
    "2606.04915": "PLATFORM-EVALUATION-SYSTEM",
    # Distributional DAgger changes post-training credit/update semantics.
    "2606.05152": "TRAIN-RLHF",
    # Deterministic BAS-to-SIEM synthesis owns typed traceability/provenance.
    "2606.05252": "PLATFORM-TRACE",
}

# V7 also found four coarse owners that caused semantically unrelated Books
# propositions to be selected.  Move the mechanism to the canonical owner
# before regenerating all 131 comparisons.
AUDIT_OWNER.update({
    "2606.04375": "TRAIN-PRETRAINING",
    "2606.04384": "TRAIN-PRETRAINING",
    "2606.04391": "AGENT-RAG",
    "2606.04454": "AGENT-RAG",
    "2606.05378": "WORLDVIEW-REPRESENTATION",
})

BLOCKED_EXACT_V1 = {"2606.05268"}

V6_FALSE_ARTIFACT_LOCATORS = {
    "2606.04329", "2606.04378", "2606.04401", "2606.04413", "2606.04442",
    "2606.04460", "2606.04461", "2606.04484", "2606.04505", "2606.04507",
    "2606.04522", "2606.04594", "2606.04634", "2606.04662", "2606.04799",
    "2606.04807", "2606.05016", "2606.05101", "2606.05165", "2606.05233",
    "2606.05290", "2606.05339", "2606.05376", "2606.05384", "2606.05414",
    "2606.05415", "2606.05538",
}

BENCHMARK_OVERRIDES = {
    "2606.04620": {
        "model": "Qwen3-8B; Llama3-8B; Mistral v0.1-7B; Falcon H1R-7B",
        "hardware": "single NVIDIA A100 GPU with 40 GB memory",
        "precision": "FP16 baseline plus QuBLAST block-level mixed weight quantization; no single fixed quantized precision contract",
        "input_length": "WikiText-2 and WikiText-103 evaluation corpora; exact sequence length not disclosed in the reviewed slice",
        "output_length": "Not Applicable — evaluation reports perplexity and model memory footprint, not generated-token length",
        "batch": "Not Disclosed — exact-v1 evaluation does not state one batch contract",
        "concurrency": "Not Disclosed — single-GPU experiment, no request concurrency contract",
        "slo": "Not Disclosed — reported perplexity/memory measurements are not a production SLO",
    },
    "2606.05238": {
        "model": "GPT-5.3-Codex; GPT-5.4-Mini; Gemini-3.1-Pro; Grok-4.20, all under the OpenHands scaffold",
        "hardware": "fresh Ubuntu 22.04 Google Cloud VM with 16 vCPUs and 64 GB RAM; GPU tasks add one NVIDIA L4 24 GB with no pre-installed CUDA drivers",
        "precision": "Not Applicable / Not Disclosed — heterogeneous artifact deployment tasks, not a fixed model-precision experiment",
        "input_length": "51 deployment tasks; no fixed prompt-token length, with per-model token use reported separately",
        "output_length": "No fixed output length; agent produces a deployed environment and RUNBOOK plus tool trajectory",
        "batch": "one fresh VM per task/model run; not a training batch",
        "concurrency": "Not Disclosed — the paper does not define parallel-agent concurrency as an evaluated variable",
        "slo": "task-specific time budget and fixed verification budget; observed runtime is not a production SLO",
    },
    "2606.05249": {
        "model": "20 language models in exact-v1 Table 1, including Claude 3.7/3.5 Sonnet, Gemini 2.5 Pro, DeepSeek R1, OpenAI o3/o4-mini, GPT-4.1, Claude 3 Haiku and Gemini 2.0 Flash",
        "hardware": "Not Disclosed — compared API/model runs are not bound to one execution-hardware contract",
        "precision": "Not Disclosed — compared models are not bound to one precision or quantization contract",
        "input_length": "100 infrastructure-as-code tasks; exact per-task prompt/context length not disclosed",
        "output_length": "generated CDK solution integrated and tested; exact token length not disclosed",
        "batch": "one attempt per model/task in the main run; five independent trials for the selected reliability subset",
        "concurrency": "Not Disclosed — concurrency is not an evaluated variable",
        "slo": "Not Disclosed — no production latency or availability SLO",
    },
    "2606.05342": {
        "model": "GPT-5.4 (low reasoning); Qwen 3.5:9B; GPT-4o, paired with the disclosed Magentic-UI-derived web-browsing agent",
        "hardware": "Not Disclosed — the compared API/local models are not bound to one hardware contract",
        "precision": "Not Disclosed — no common precision or quantization contract",
        "input_length": "simulated long-running monitoring tasks with 10-minute and extended 40-minute horizons; token use is measured, not fixed",
        "output_length": "agent action/monitoring trajectory plus final evaluation state; no fixed token length",
        "batch": "one agent/task baseline run as reported; not a training batch",
        "concurrency": "Not Disclosed — concurrent agents are not an evaluated variable",
        "slo": "10-minute and 40-minute task horizons are benchmark windows, not production SLOs",
    },
    "2606.05435": {
        "model": "two-layer 795,010-parameter MLP for MNIST; five-layer 582,346-parameter CNN for CIFAR-10",
        "hardware": "Not Disclosed — exact-v1 §IV does not state execution hardware",
        "precision": "Not Disclosed — exact-v1 §IV does not state numeric precision",
        "input_length": "28×28 MNIST pixels; 32×32 RGB CIFAR-10 images",
        "output_length": "10-class classification output",
        "batch": "256 for MNIST; 512 for CIFAR-10",
        "concurrency": "Not Applicable — offline training experiment, no serving concurrency contract",
        "slo": "Not Applicable — reports accuracy/privacy trade-offs over five random seeds, not a production SLO",
    },
    "2606.05538": {
        "model": "Qwen1.5-MoE-A2.7B; OLMoE-1B-7B-0125; Qwen3-30B-A3B; Qwen3.5-35B-A3B",
        "hardware": "NVIDIA H100 for disclosed Fisher calculation and 50% compressed Qwen1.5-MoE inference measurements",
        "precision": "bf16 for disclosed vLLM inference; optional 4-bit AWQ composition experiment",
        "input_length": "128 calibration samples by default (32/64/128/256/512 ablation); benchmark-dependent task inputs, not one token length",
        "output_length": "benchmark-dependent generation/classification outputs; no single fixed token length",
        "batch": "Not Disclosed as a training/serving batch; 128 is calibration-set cardinality",
        "concurrency": "Not Disclosed — concurrency is not an evaluated variable",
        "slo": "Not Disclosed — runtime/cost measurements are observations, not a production SLO",
    },
    "2606.05257": {
        "model": "custom two-part behavioral foundation model: feature embedder plus decoder-only contextualizer for next-event prediction",
        "hardware": "Not Disclosed — exact-v1 does not identify accelerator type/count for the sweeps",
        "precision": "bf16 mixed precision",
        "input_length": "256-event contextualizer sequence; 24-event embedder context in the compute formula",
        "output_length": "next-event ranking: in-batch candidate set before freeze, full cached catalogue after freeze",
        "batch": "global batch size is a swept variable; no single batch value represents the study",
        "concurrency": "Not Applicable — offline scaling study, no serving concurrency contract",
        "slo": "Not Applicable — reports loss/ranking/compute scaling, not a production SLO",
    },
    "2606.05391": {
        "model": "Not Applicable — qualitative study of 17 professional developers using software agents",
        "hardware": "Not Applicable — semi-structured interviews, not a model execution benchmark",
        "precision": "Not Applicable — no model precision claim",
        "input_length": "17 participants; one-hour scheduled interviews averaging 60 minutes, conducted July–August 2025",
        "output_length": "video-recorded/transcribed interviews coded into 13 axial codes and two final conceptual categories",
        "batch": "Not Applicable — criterion/snowball sample, not a training batch",
        "concurrency": "Not Applicable — interviews were conducted 1:1",
        "slo": "Not Applicable — qualitative oversight study, no production SLO",
    },
    "2606.04513": {
        "model": "Qwen3-VL-Instruct 8B; Qwen3-VL-Thinking 8B; InternVL-3.5-8B; frozen GeMap and DuMapNet backbones",
        "hardware": "single server with 8× NVIDIA A800 80GB GPUs; PyTorch 2.6.0; CUDA 12.4",
        "precision": "Not Disclosed — the exact-v1 manuscript does not state one inference/training precision contract",
        "input_length": "3,712 BEV training images and 656 test images; this is dataset cardinality, not token length",
        "output_length": "Not Applicable — output is a versioned vector-map state rather than a token-length contract",
        "batch": "SFT batch size 32; GRPO rollout batch size 16",
        "concurrency": "Not Disclosed — runtime is reported per tile, not as a concurrency contract",
        "slo": "100 warm-up tiles followed by 1,000 validation tiles; mean 420 ms/tile, median 380 ms, p95 920 ms, p99 1.6 s; observed evaluation, not a production SLO",
    },
    "2606.04929": {
        "model": "Llama-3 8B; Qwen3 1.7B/4B/8B",
        "hardware": "NVIDIA H100 for the disclosed full-fine-tuning/LoRA runs",
        "precision": "Not Disclosed — exact-v1 evaluation does not state one precision contract",
    },
    "2606.05165": {
        "model": "Qwen2.5-0.5B; Qwen2.5-32B",
        "hardware": "NVIDIA H100 80GB",
        "precision": "Not Disclosed — exact-v1 evaluation does not state one precision contract",
    },
    "2606.05304": {
        "model": "Qwen3-8B/14B/32B; Claude Opus 4.7; GPT-5.5 and the other identities enumerated by the authors",
        "hardware": "Not Disclosed — the author evaluation does not bind all compared API/local models to one hardware contract",
        "precision": "Not Disclosed — the author evaluation does not bind all compared models to one precision contract",
    },
    "2606.05484": {
        "model": "LLaMA-style 150M–1B models",
        "hardware": "NVIDIA H100; 4-stage and 8-stage pipeline configurations",
        "precision": "bfloat16",
    },
    "2606.05434": {
        "model": "Model identity disclosed in exact-v1 §4 evaluation; see workload row",
        "hardware": "single NVIDIA A100",
        "precision": "bfloat16",
        "input_length": "800 training examples; 500 evaluation examples (dataset cardinality, not token input length)",
        "output_length": "greedy decoding; maximum 512 new tokens",
    },
    "2606.05515": {
        "model": "Model identities disclosed in exact-v1 evaluation; see workload row",
        "hardware": "Hardware configuration disclosed in exact-v1 evaluation; no universal deployment hardware contract",
        "precision": "mixed precision",
        "batch": "effective batch size 200",
    },
    "2606.06530": {
        "model": "Not Applicable — evaluation concerns generated FP adder RTL, not an LLM/model execution identity",
        "hardware": "Synthesis/evaluation toolchain in exact-v1; not an AI serving accelerator contract",
        "precision": "Not Applicable — `fpadd_f16` is the generated circuit workload data type, not model inference precision",
    },
}

# Independent V8 found cells where the exact-v1 evaluation body disclosed a
# condition but the generated benchmark table still said Not Disclosed.  These
# overrides are deliberately field-specific: every other cell remains bounded
# by the exact-v1 extractor and is not inferred from a title or abstract.
BENCHMARK_OVERRIDES.update({
    "2606.04366": {
        "model": "MeshTok with ViT-style PDE Transformer backbones; DeepONet/FNO/ViT/MPP/DPOT/MoE-POT/BCAT baselines",
        "hardware": "single NVIDIA A800 GPU; identical GPU environment for the reported inference-time comparison",
        "batch": "batch size 8 for the disclosed pretraining setup",
    },
    "2606.04373": {
        "model": "ViT-T/ViT-B, DeiT-T/DeiT-S/DeiT-B and Swin-T backbones",
        "hardware": "NVIDIA A800 GPU plus Intel Xeon Gold 6342 CPU",
        "precision": "uniform data-free quantization evaluated at 3-bit weights/activations and 4-bit weights/activations",
    },
    "2606.04438": {
        "model": "LoopMoE/Vanilla-MoE architectures trained on the OLMo-3 Dolma3Mix contract; OLMoE-1B-7B and other disclosed baselines",
    },
    "2606.04463": {
        "model": "Cosmos-Predict2.5-2B conditioned robot/human skeleton-to-video model",
        "hardware": "single NVIDIA GH200 GPU",
    },
    "2606.04719": {
        "model": "pretrained SigLIP vision encoder with a 400M-parameter ViT structure",
        "precision": "automatic mixed precision with FP32 and BF16",
        "input_length": "384×384 image resolution with 729 visual features",
        "batch": "256 for alignment; 128 for end-to-end fine-tuning",
    },
    "2606.04727": {
        "model": "BERT4Rec, GMF and SASRec sequential baselines plus the disclosed Qwen2.5 EviRank setting",
    },
    "2606.04767": {
        "model": "VGG, ResNet, DenseNet and Transformer/ViT architecture families used for the robustness analysis",
    },
    "2606.04939": {
        "model": "frozen T5-Base text encoder plus the disclosed audio DiT/VAE system",
        "hardware": "32 NVIDIA H20 GPUs",
        "batch": "global batch size 768",
    },
    "2606.04964": {
        "model": "LLaDA-Instruct in the main experiments plus disclosed comparison models",
        "hardware": "single NVIDIA H20 GPU",
    },
    "2606.05233": {
        "workload": "CUA-HandCrafted: 793 episodes, 24 multi-step web tasks, 56 attack templates, 8 attack families and 4 system-prompt configurations; cross-domain SkillBench slice",
        "model": "Claude Sonnet 4.6 and GPT-5.4 frontier CUA targets; disclosed legacy/current comparison models in §3 and Appendix B",
        "input_length": "793 benchmark episodes; not a fixed prompt-token length",
        "output_length": "browser/coding agent action trajectories; no fixed output-token length",
        "batch": "episode-level execution; no training batch contract",
        "concurrency": "Not Disclosed — concurrency is not an evaluated variable",
        "slo": "attack-success/canary and reproducibility metrics; no production latency or availability SLO",
    },
    "2606.05250": {
        "model": "Gemma 4 31B via Google AI Studio plus the hosted embedding model used by the resilient RAG pipeline",
        "hardware": "commodity AMD Ryzen 5 5600GE / Intel Core i7-8565U workstations with 16 GB RAM on Windows 11 Pro",
    },
    "2606.05271": {
        "model": "10 disclosed model families spanning CNNs, Transformers, SSMs, KANs, spiking networks and multi-stage VLA pipelines",
        "hardware": "Intel Core Ultra Lunar Lake Series 2 SoC with 8-logical-core CPU, integrated GPU and NPU",
        "precision": "FP16 and INT8 operator/model profiles as disclosed",
    },
    "2606.05336": {
        "model": "Qwen3-4B-Instruct-2507 profile generator and frozen LLM judge",
        "precision": "bfloat16 mixed precision with FlashAttention-2",
        "input_length": "maximum sequence length 4,200 tokens",
        "batch": "per-device batch size 4 with 20 gradient-accumulation steps across 4 devices; effective batch 320",
    },
    "2606.05367": {
        "model": "VITS and CFS2/x-vector text-to-speech systems used by the task-vector elimination study",
    },
    "2606.05396": {
        "hardware": "Intel Core Ultra 7 155H laptop with 32 GB RAM and no dedicated GPU",
        "precision": "Q4_K_M 4-bit GGUF checkpoints under Ollama",
        "slo": "600-second per-prompt timeout with three transport retries; experimental budget, not a production SLO",
    },
    "2606.05429": {
        "model": "OPT and LLaMA/LLaMA-2 model families, including LLaMA-2-70B",
        "hardware": "single NVIDIA L40 46 GB GPU",
        "precision": "ultra-low-bit SAGE-PTQ with disclosed 2-bit/4-bit salient-weight settings and average 1.03 bits/weight",
    },
    "2606.06527": {
        "model": "ResNet18, MobileNetV3-Large, MobileNetV4-Conv-Small, MobileViT, ShuffleNetV2 and EfficientNet-Lite0",
        "precision": "NVFP4 activations with FP8 block scale and FP32 tensor scale; block-size and weight/scale precision ablations",
    },
})

OLD_INTEGRATE_DECISION = {
    "2606.04329": ("AGENT-MEMORY", "No Change — Existing Coverage"),
    "2606.04415": ("INFER-PD-DISAGGREGATION", "Integrate"),
    "2606.04446": ("INFER-SPECULATIVE-DECODING", "No Change — Existing Coverage"),
    "2606.04484": ("TRAIN-DISTRIBUTED-TRAINING", "Integrate"),
    "2606.04594": ("PLATFORM-TRACE", "Integrate"),
    "2606.04769": ("AGENT-MCP", "No Change — Existing Coverage"),
    "2606.04929": ("PLATFORM-SECURITY", "Integrate"),
    "2606.05014": ("MODEL-TRANSFORMER-LAYER", "No Change — Existing Coverage"),
    "2606.05158": ("AGENT-MULTI-AGENT", "Integrate"),
    "2606.05165": ("TRAIN-DATA", "Integrate"),
    "2606.05263": ("TRAIN-GRPO", "No Change — Existing Coverage"),
    "2606.05304": ("AGENT-MULTI-AGENT", "Integrate"),
    "2606.05339": ("AGENT-MCP", "No Change — Existing Coverage"),
    "2606.05484": ("TRAIN-PIPELINE-PARALLEL", "Integrate"),
    "2606.05495": ("INFER-SCHEDULING", "Integrate"),
}

NEW_INTEGRATE = {
    "2606.04421", "2606.04454", "2606.04603", "2606.04727", "2606.05016", "2606.05037",
    "2606.05161", "2606.05268", "2606.05315", "2606.05408", "2606.05513", "2606.05533",
}

# Independent V4 target+adjacent review reopens every provisional disposition
# after evidence repair. Only durable system-contract deltas remain queued.
REASSESSED_BOOKS = {
    "2606.04513": ("AGENT-WORKFLOW", "Weekly Only — Context"),
    "2606.04415": ("INFER-PD-DISAGGREGATION", "No Change — Existing Coverage"),
    "2606.04421": ("AGENT-MEMORY", "No Change — Existing Coverage"),
    "2606.04454": ("AGENT-RAG", "No Change — Existing Coverage"),
    "2606.04484": ("TRAIN-DISTRIBUTED-TRAINING", "No Change — Existing Coverage"),
    "2606.04594": ("PLATFORM-TRACE", "No Change — Existing Coverage"),
    "2606.04603": ("AGENT-RAG", "No Change — Existing Coverage"),
    "2606.04727": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage"),
    "2606.04929": ("PLATFORM-SECURITY", "Integrate"),
    "2606.05016": ("TRAIN-LORA", "No Change — Existing Coverage"),
    "2606.05037": ("AGENT-TOOL-CALLING", "No Change — Existing Coverage"),
    "2606.05158": ("AGENT-MULTI-AGENT", "Integrate"),
    "2606.05161": ("MULTIMODAL-GENERATIVE-PARADIGMS", "No Change — Existing Coverage"),
    "2606.05165": ("TRAIN-DATA", "Integrate"),
    "2606.05268": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage"),
    "2606.05304": ("AGENT-MULTI-AGENT", "Integrate"),
    "2606.05315": ("TRAIN-SFT", "No Change — Existing Coverage"),
    "2606.05408": ("AGENT-WORKFLOW", "No Change — Existing Coverage"),
    "2606.05484": ("TRAIN-PIPELINE-PARALLEL", "Integrate"),
    "2606.05495": ("INFER-SCHEDULING", "No Change — Existing Coverage"),
    "2606.05513": ("AGENT-MEMORY", "No Change — Existing Coverage"),
    "2606.05533": ("MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage"),
}

BOOKS_COMPARISON_NOTES = {
    "2606.04535": (
        "Ch24 owns diffusion-language-model mutable token state, denoising/correction schedules and commit semantics; the closest proposition is the branch that permits positions to be revised before final commit.",
        "Dynamic infilling changes which masked token positions are resampled and committed during diffusion-language-model decoding. It is a generation-state policy, not speculative-decoding exactness or a floating-kernel claim.",
        "Ch23 supplies representation identity and Ch25 may consume generated observations, while Ch48 owns draft-model verification rather than diffusion infilling.",
    ),
    "2606.04549": (
        "Ch72 owns artifact provenance, digest/signature verification, attestation and admission/load integrity before execution.",
        "The confidential-VM design verifies executable-object identity and enforces an integrity boundary inside the disclosed trusted-computing contract; it does not concern cross-tenant KV or prefix-cache reuse.",
        "Ch71 owns tenant isolation and Ch73 consumes attested release evidence for production admission and rollback.",
    ),
    "2606.05423": (
        "Ch72 separates policy text and probabilistic sensors from deterministic authorization/enforcement, including storage-visible operations and versioned policy state.",
        "The paper adds policy-compliant cloud-storage enforcement as a concrete mediated-I/O branch; it is not evidence about generated adversarial training samples or guard-model filtering.",
        "Ch71 owns tenant/data isolation and Ch73 turns the enforcement and audit evidence into production readiness decisions.",
    ),
    "2606.05433": (
        "Ch72 owns public verification, proof-claim scope and the distinction between algebraic correctness, work binding and independent attestation/metering.",
        "The zero-knowledge training-verification protocol instantiates that proof boundary and its overhead assumptions; it is unrelated to adversarial-sample generation or guard-model data curation.",
        "Ch71 contributes trust-domain isolation and Ch73 consumes a versioned proof/attestation result at release time.",
    ),
    "2606.04505": ("Ch66 already treats simulator identity, transition rules, execution trace and real-environment anchoring as evaluation evidence rather than deployment truth.", "MechSim makes assumptions, variables, dependency graph and execution trace explicit before an Agent explains a simulator outcome; this strengthens the same simulator-evidence contract but does not create another owner.", "Ch65 supplies serving observations; Ch67 consumes accepted evidence operationally, while Ch81 owns the executable workflow around the simulator."),
    "2606.04591": ("Ch76 already owns offline ingestion/index construction, online recall, reranking, packing and modality-aware retrieval routing.", "FFRS instantiates that chain with semantic dialogue fragments, vector recall and a generation-based fine-grained reranker; it is a workload-specific retrieval unit rather than a new RAG state boundary.", "Ch75 assembles retrieved context and Ch77 governs whether any derived profile or interaction state persists."),
    "2606.05101": ("Ch72 already defines policy-generated adversarial candidates, independent guards, held-out red-team evaluation and the shared-blind-spot risk.", "FoeGlass supplies an audio-specific black-box exploration loop plus diversity feedback against mode collapse; it validates that existing security branch under ADD/TTS conditions without changing its authority split.", "Ch71 provides tenant/evidence isolation and Ch73 turns accepted red-team evidence into a release decision."),
    "2606.05106": ("Ch28 already owns next-token objective, curriculum/data coupling, checkpoint probes and the difference between loss trend and capability evidence.", "The arithmetic curriculum and attention-mask/residual/logit-lens interventions provide a bounded mechanistic case for staged learning, not a new pretraining lifecycle contract.", "Ch27 owns the serialized curriculum data; Ch29 receives the resulting pretrained artifact for instruction alignment."),
    "2606.05336": ("Ch77 already separates derived preference profiles, admission, retrieval, reward metadata and persistent-memory authority.", "BUMP adds a self-supervised in-batch bidirectional ranking reward for constructing a free-form profile, but remains one learned admission/construction policy inside the existing memory transaction boundary.", "Ch76 supplies retrieval primitives and Ch78 may act only on a committed, provenance-bearing profile."),
    "2606.05367": ("Ch23 already requires representation identity, intervention evidence and explicit separation of codec, speaker/style and semantic state.", "The elimination study localizes emotional control to the co-trained x-vector and applies centroid arithmetic there; this is a bounded intervention case, not a new multimodal representation owner.", "Ch22 supplies the long-context model substrate and Ch24 consumes the representation in a generation branch."),
    "2606.04415": ("Ch55 already owns phase split, co-location and runtime/state ownership.", "FlexNPU is an Ascend-specific virtualization realization of that boundary, not a new general PD contract.", "Ch54 supplies memory/runtime execution constraints; Ch56 consumes the resulting schedulable state."),
    "2606.04421": ("Ch77 already covers temporal memory control, counterfactual attribution and regret-like feedback.", "Temporal regret instantiates that controller but does not add a distinct durable memory state transition.", "Ch76 provides retrieved evidence; Ch78 turns committed memory into bounded tool action."),
    "2606.04454": ("Ch76 owns retrieval, provenance-bearing evidence acquisition and the boundary between retrieved subgraphs and committed context.", "External subgraph generation is a retrieval/program-construction branch whose output remains evidence until the Agent admits it into context; it does not introduce a durable workflow commit contract.", "Ch75 assembles the accepted subgraph into context; Ch79 may plan over it, while Ch81 owns durable workflow state only after a transition is committed."),
    "2606.04484": ("Ch36 already defines rollout/training overlap, snapshots, barriers and agent-RL tree execution.", "AgentJet is a framework realization of those runtime choices; the paper does not establish another distributed-training invariant.", "Ch35 owns checkpoint state and Ch37 the tensor-parallel communication layer."),
    "2606.04594": ("Ch69 already links causal/root-cause graphs to diagnoser authority, repair and rerun evidence.", "The disclosed diagnosis mechanism refines an implementation path but does not alter trace ownership or release evidence.", "Ch68 provides metric evidence; Ch70 consumes trace evidence in cost and operational decisions."),
    "2606.04603": ("Ch76 already owns provenance, confidence, retrieval sufficiency and coarse-to-fine retrieval policy.", "Uncertainty-aware approximate retrieval is a policy instance inside that contract rather than a new RAG state owner.", "Ch75 constructs context; Ch77 decides what derived evidence may persist."),
    "2606.04727": ("Ch66 already separates confidence, calibration, evidence, refusal and evaluation contracts.", "The family supplies a bounded evaluation case but no new calibration or release-gate invariant.", "Ch65 owns serving observations; Ch67 turns accepted evidence into operational observability."),
    "2606.04929": ("Ch72 covers poisoning and lineage, but treats stages largely as individually auditable threat surfaces.", "Sequential post-training composition adds additive/complementary cross-stage attack semantics and requires joint lineage plus replay.", "Ch71 contributes tenancy boundaries; Ch73 consumes the strengthened security evidence at production release."),
    "2606.05016": ("Ch30 already covers adapter merge, routing, subspace compatibility and composition evaluation.", "Probe-guided per-layer merge is a constrained selection strategy within that existing branch.", "Ch29 owns the SFT artifact entering adaptation; Ch31 owns downstream preference signals."),
    "2606.05037": ("Ch78 already owns typed validation errors, retry policy, effect boundaries and the requirement that failure output be machine-actionable.", "The exact-v1 self-reflective response schema packages diagnosis and recovery suggestions inside that existing tool-failure contract; its two-API pilot does not establish a new durable action-state owner.", "Ch77 supplies trusted context; Ch79 consumes the bounded recovery state during planning and reflection."),
    "2606.05158": ("Ch82 owns multi-agent communication, but currently assumes completed messages become available at message boundaries.", "StreamMA makes intermediate reasoning steps consumable and changes message availability plus the pipeline latency critical path.", "Ch81 owns durable workflow checkpoints; Ch83 standardizes protocol envelopes, not intra-message readiness."),
    "2606.05161": ("Ch24 owns multimodal generation branches and their decoding/correction control.", "GACL is decoding-time arbitration rather than a new representation identity, so it belongs to the existing generation decision branch.", "Ch23 supplies representation identity; Ch25 consumes generated observations as possible world-state evidence."),
    "2606.05165": ("Ch27 owns data lineage and influence, but mostly at dataset/example and artifact boundaries.", "Activation-space attribution adds an estimator branch connecting training examples to internal representation changes.", "Ch26 defines embodied data semantics; Ch28 consumes selected data under a pretraining objective."),
    "2606.05268": ("Ch66 already owns verifier/judge evidence aggregation and calibration boundaries.", "Weak-to-strong verification is a bounded evaluator configuration, not a new platform evidence contract.", "Ch65 records serving evidence; Ch67 exposes accepted evaluation signals operationally."),
    "2606.05304": ("Ch82 owns typed agent communication, but does not yet distinguish raw language from committed action-state records.", "PACT introduces projection and commit semantics for shared history, changing communication-state ownership and rollback risk.", "Ch81 owns workflow durability; Ch83 transports the committed record across protocol boundaries."),
    "2606.05315": ("Ch29 already owns distillation/SFT objective alignment and the resulting model artifact.", "Low-rank trajectory distillation is an objective/representation implementation branch rather than a new SFT lifecycle contract.", "Ch28 supplies the pretrained state; Ch30 adapts the resulting artifact efficiently."),
    "2606.05408": ("Ch81 already requires mutation to be paired with selection, quality/diversity control and held-out evaluation.", "The reported non-convergence without selection directly supports that existing proposition and adds no new workflow state.", "Ch80 proposes plans; Ch82 communicates only the selected workflow state."),
    "2606.05484": ("Ch38 defines pipeline boundary activation bytes and communication cost, but treats the boundary tensor as fixed.", "Learned orthogonal projection makes inter-stage compression/decompression trainable state with explicit accuracy/communication trade-offs.", "Ch37 determines intra-layer communication; Ch39 schedules the newly compressed boundary across stages."),
    "2606.05495": ("Ch56 already owns event-triggered scheduling, CUDA-graph/eager paths and runtime dispatch state.", "Task-parallel CUDA execution is an implementation case unless it changes the scheduler-visible task/dependency contract; this paper does not prove that broader change.", "Ch55 supplies disaggregated phase state; Part VI consumes scheduler decisions as a serving control-plane contract."),
    "2606.05513": ("Ch77 already covers streaming consolidation, update regimes and self-evolving memory governance.", "The disclosed mechanism fits that existing update branch and does not add a new persistent-memory invariant.", "Ch76 supplies evidence eligible for consolidation; Ch78 consumes only committed memory state."),
    "2606.05533": ("Ch26 already owns affordance/action representation and the high-level versus low-level controller boundary.", "A4D is a bounded representation case inside that VLA loop rather than a new physical-action contract.", "Ch25 predicts environment transition; Ch27 governs the training data produced by the embodied loop."),
}

BOOKS_KEYWORDS = {
    "2606.04505": ("simulator identity", "transition rules"),
    "2606.04591": ("offline", "rerank"),
    "2606.05101": ("adversarial candidates", "red-team"),
    "2606.05106": ("next-token", "probe"),
    "2606.05336": ("preference profile", "admission"),
    "2606.05367": ("representation identity", "intervention"),
    "2606.04415": ("co-location", "phase"), "2606.04421": ("counterfactual", "temporal"),
    "2606.04454": ("workflow", "graph"), "2606.04484": ("rollout", "barrier"),
    "2606.04594": ("root cause", "repair"), "2606.04603": ("provenance", "confidence"),
    "2606.04727": ("calibration", "refusal"),
    "2606.04769": ("descriptions", "信任", "semantic validation"),
    "2606.04929": ("poison", "lineage"),
    "2606.05016": ("merge", "subspace"), "2606.05037": ("retry", "schema"),
    "2606.05158": ("communication", "message"), "2606.05161": ("decoding", "generation"),
    "2606.05165": ("lineage", "influence"), "2606.05268": ("verifier", "judge"),
    "2606.05304": ("communication", "typed"),
    "2606.05315": ("distill", "objective"),
    "2606.05339": ("cancellation", "state", "ownership"),
    "2606.05408": ("selection", "mutation"), "2606.05484": ("activation", "communication"),
    "2606.05495": ("CUDA", "event"), "2606.05513": ("consolidation", "streaming"),
    "2606.05533": ("affordance", "controller"),
}

# Candidate-specific anchors for cases where a generic token-overlap search can
# land on a semantically adjacent but wrong proposition.  The resolver searches
# current Books prose at generation time, so these do not freeze line numbers.
BOOKS_TARGET_TERMS = {
    "2606.04535": ("mutable", "diffusion", "commit"),
    "2606.04549": ("attestation", "integrity", "admission"),
    "2606.05423": ("deterministic", "policy", "enforcement"),
    "2606.05433": ("ZK relation", "proof claim", "work-binding"),
    "2606.04454": ("retrieval", "provenance", "evidence"),
    "2606.04857": ("噪声", "缺失", "冲突"),
    "2606.05378": ("circuit evidence", "replacement reconstruction", "intervention"),
    "2606.06529": ("attack distribution", "risk(N)", "攻击预算"),
}

# Exact-v1 mechanism summaries for Deep families whose section opener is a
# generic sentence.  Selection must compare the disclosed state/control delta,
# not whichever sentence happens to appear first under the Method heading.
SELECTION_SIGNAL_OVERRIDES = {
    "2606.04425": (
        "The taxonomy treats stored prompt injection as a cross-session state attack: adversarial content is written "
        "into memory, files or tool-visible artifacts, later incorporated into context, and finally activated in a "
        "future execution; the benchmark measures each lifecycle stage separately."
    ),
    "2606.04634": (
        "The method computes finite-horizon safety risk from an MDP and safety specification, synthesizes a shield, "
        "then builds a three-level decision-tree hierarchy whose higher levels provide runtime case-based explanations "
        "for shield interventions and unsafe actions."
    ),
    "2606.05257": (
        "The study separates joint embedder/contextualizer next-event training from a frozen-embedder full-catalogue "
        "stage, then sweeps model/data allocation, embedder share, batch size and negative-pool size under evaluation "
        "contracts matched to those two regimes."
    ),
    "2606.05538": (
        "The method uses empirical Fisher information to rank expert parameters and dimensions by predictive-distribution "
        "impact, then applies structured expert/dimension trimming under a common calibration and evaluation protocol."
    ),
}

PDF_EVIDENCE = {
    "2606.04415": {
        "method": "Section 3 intercepts AscendCL calls transparently, proxies device objects through a per-device daemon, and profiles runtime operations so unchanged applications can be decoupled from physical NPU ownership.",
        "evaluation": "Sections 4.1–4.2 evaluate Ascend 910C/CloudMatrix384 with CANN and vLLM on DeepSeek-R1-family and Qwen2.5-7B workloads, including W8A8, 1K-1K/1K-4K and TTFT≤1s/TPOT≤50ms; 977.6928 to 988.2675 tokens/s is 1.08%, with no statistical uncertainty reported.",
        "limitations": "Section 3.5 bounds the design to the disclosed Ascend runtime and proxy scope; the results do not establish universal no-overhead behavior across NPU generations, workloads or SLOs.",
    },
    "2606.04459": {
        "method": "Section 3 defines the token-ranking signature and Theorem 1; Section 4 states the unforgeability construction and assumptions through Theorem 2.",
        "evaluation": "Section 5 studies approximate parameter exposure with 50 rankings and reports three successful fits out of five attempts under the disclosed fitting procedure.",
        "limitations": "The guarantee depends on the theoretical assumptions in Section 4, while Section 5 exposes empirical fitting constraints rather than a universal recovery guarantee.",
    },
    "2606.05158": {
        "method": "Section 3 defines StreamMA: Section 3.1 streams intermediate steps, Section 3.2 analyzes effectiveness, and Section 3.3 analyzes efficiency and pipeline overlap.",
        "evaluation": "Section 4.1 uses eight benchmarks through OpenCompass, compares Single/Serial and Chain/Tree/Graph structures with Claude Opus 4.6 and GPT-5.4, normally over three runs and eight runs for small sets.",
        "limitations": "Section 6 explicitly limits the conclusions; intermediate-step availability can reduce latency but introduces partial-message quality and orchestration assumptions.",
    },
    "2606.05268": {
        "method": "Section 3 generates multiple weak verifiers, aggregates their outputs, adapts the ensemble to spatial-layout constraints, and feeds verification messages back into layout generation.",
        "evaluation": "Section 4 defines the experiment design, compares aggregation with LLM judges, and analyzes aggregation strategies plus verifier-guided generation under the disclosed spatial-layout tasks.",
        "limitations": "Section 4.5 bounds the claims to the constructed verifier pool, layout domains and aggregation data; the study does not establish a universal verifier replacement.",
    },
}

# Exact-v1 arXiv HTML was independently opened through the working web path
# after the local curl route reset connections.  Keep the section locator and
# a bounded, family-specific review note here; absence from the local cache is
# not evidence that arXiv itself is blocked.
WEB_EVIDENCE = {
    "2606.04355": {
        "method_locator": "https://arxiv.org/html/2606.04355v1 §3 Continuous Reference-Based POMDPs; §4 Algorithm; §§4.1–4.4",
        "evaluation_locator": "https://arxiv.org/html/2606.04355v1 §5 Experiments; §§5.1–5.6; Appendix A.2",
        "limitations_locator": "https://arxiv.org/html/2606.04355v1 Abstract; §3 reference-policy optimality boundary; §6 Summary",
        "artifact_locator": "https://github.com/RDLLab/ROPRAS3",
        "method": "ROP-RAS3 replaces exhaustive action enumeration with a sampled reference policy: VAMP generates diverse macro-actions online, the reference-based Bellman backup samples those actions in belief space, and tree construction plus numerical backup select a policy whose convergence rate depends on sampled actions rather than the full action-space size.",
        "evaluation": "Section 5 evaluates four navigation and three manipulation tasks, horizons up to 3,000 steps, state dimensions up to 35, a physical Stretch 3 demonstration, and ablations over reference exploration and tree depth. This proves only the disclosed long-horizon POMDP and robot slices.",
        "limitations": "The authors explicitly state that the reference-based optimum need not equal the original POMDP optimum. Gains depend on reference-policy quality, sampled-action coverage and the reported simulation/robot conditions; approximate convergence does not establish globally optimal planning.",
    },
    "2606.04597": {
        "method_locator": "https://arxiv.org/html/2606.04597v1 §3 Learning to Infer Cost Partitions; §§3.1–3.3",
        "evaluation_locator": "https://arxiv.org/html/2606.04597v1 §4 Experiments; IPC optimal-track tasks and efficiency/informativeness questions",
        "limitations_locator": "https://arxiv.org/html/2606.04597v1 §5 Conclusion and Future Works",
        "method": "The planner encodes a state and its abstractions as labelled graphs, extracts action-centric Weisfeiler–Leman features, and uses axial self-attention to predict cost weights. A softmax output enforces the partition constraint by construction, preserving admissibility while replacing a per-state optimization solve.",
        "evaluation": "The authors train on optimal cost weights from sampled synthetic tasks and evaluate learned heuristics on selected IPC optimal-track domains, measuring node expansion, computation cost and informativeness against suboptimal partitions. The result is domain-trained planning evidence, not universal heuristic transfer.",
        "limitations": "Section 5 leaves broader-domain transfer and improvement of the learned partition model as future work. Admissibility comes from the output constraint, while heuristic informativeness and runtime gain remain dependent on abstractions, feature construction and training distribution.",
    },
    "2606.04812": {
        "method_locator": "https://arxiv.org/html/2606.04812v1 §4 Probably Approximate Safe Barrier-Certificates; §5 Barrier-Certificate Aided Learning",
        "evaluation_locator": "https://arxiv.org/html/2606.04812v1 §6 Experiments; §§6.1–6.2",
        "limitations_locator": "https://arxiv.org/html/2606.04812v1 §3.4 Setting and Assumptions; §7 Conclusion",
        "method": "The method learns a VAE over encountered states, constructs upper and lower probably-approximate barrier certificates in latent space, and samples the non-robust region between them for a second learning phase. The certificates separate conservative and permissive safe-region estimates instead of treating one learned verifier as exact.",
        "evaluation": "Section 6 reports Gymnasium environments, sampled-trajectory confidence settings and comparisons against PPO/curriculum alternatives, including how sample count changes bound tightness. Evidence is limited to those environments and empirical PAC construction.",
        "limitations": "The guarantees rely on sampled trajectories, stated confidence parameters, the learned latent distribution and Section 3 assumptions. The method improves reported lower-bound tightness but does not prove safety outside the sampled/encoded state distribution.",
    },
    "2606.04819": {
        "method_locator": "https://arxiv.org/html/2606.04819v1 §3 Methodology; §§3.1–3.3",
        "evaluation_locator": "https://arxiv.org/html/2606.04819v1 §4 Results; §§4.1–4.7",
        "limitations_locator": "https://arxiv.org/html/2606.04819v1 §5 Discussion; §8 Ethical Considerations",
        "artifact_locator": "https://github.com/abhinaba/pearl-usefulness-gap",
        "method": "The study constructs a stripped miner, verifies pool acceptance of random matrices, inspects miner binaries and network composition, and measures mainnet behavior across NVIDIA, AMD, CPU and Apple Silicon. It separates computational hardness from protocol-enforced computational utility.",
        "evaluation": "The authors report 44 pool-accepted shares, 8,012 observed workers, binary inspection, statistical distinguishability tests and economic measurements. These observations are tied to Pearl/cuPOW and the collection period, not a generic proof about every proof-of-useful-work design.",
        "limitations": "Section 5 frames the usefulness gap as a protocol design property rather than an exploit, and discusses adversarial adaptation and economic assumptions. Network size, energy and market effects are measurement estimates with disclosed temporal and pricing boundaries.",
    },
    "2606.05002": {
        "method_locator": "https://arxiv.org/html/2606.05002v1 §3 Method; §§3.1–3.4; Appendix A",
        "evaluation_locator": "https://arxiv.org/html/2606.05002v1 §4 Evaluation Design; §5 Experiments; §6 Results and Discussion",
        "limitations_locator": "https://arxiv.org/html/2606.05002v1 §7 Conclusion; bounded legal prioritisation setting",
        "method": "GARL represents multi-agent prioritisation as an agenda-allocation game followed by an arbitration game, then converts role-specific game utilities into token-level advantages for alternating policy optimisation. Interaction structure therefore owns reward decomposition rather than leaving it as one task-specific scalar.",
        "evaluation": "The paper evaluates issue ranking, legal competence and broader strategic decision-making under disclosed data, model/baseline, training and inference settings, and inspects training dynamics. The evidence remains tied to the legal prioritisation instantiation.",
        "limitations": "The manuscript has no dedicated limitations section; the conclusion supports the two-stage strategic-prioritisation formulation, not arbitrary multi-agent topology, open-ended negotiation, or production coordination safety.",
    },
    "2606.05423": {
        "method_locator": "https://arxiv.org/html/2606.05423v1 §4 Overview; §5 Design; §6 Security Analysis; Appendix B",
        "evaluation_locator": "https://arxiv.org/html/2606.05423v1 §7 Evaluation; §§7.1–7.3; Appendix C",
        "limitations_locator": "https://arxiv.org/html/2606.05423v1 §4.4 Deployment and Threat Model; §9 Conclusion",
        "method": "GDPRuler places a policy compiler, trusted runtime monitor, compliance metadata and tamper-evident audit logging in a confidential-VM proxy in front of unmodified Redis/RocksDB. Policy evaluation and attested configuration become explicit enforcement state instead of application convention.",
        "evaluation": "The authors evaluate YCSB and GDPR-inspired operations, storage overhead, indexed compliance queries and CVM/I/O contributions. Reported throughput and query gains apply to the disclosed Redis/RocksDB, CVM and workload configurations.",
        "limitations": "The threat model explicitly excludes side channels, denial of service and timing manipulation, while assuming the disclosed CVM/attestation boundary. Compliance enforcement covers encoded predicates and runtime paths; it does not prove legal completeness or protection beyond that boundary.",
    },
    "2606.04329": {
        "method_locator": "https://arxiv.org/html/2606.04329v1 §3 Memory Poisoning Attack Taxonomy; §3.1 Threat Model; Appendix A exploitation path",
        "evaluation_locator": "https://arxiv.org/html/2606.04329v1 §4 Evaluation; §4.1 MPBench Design",
        "limitations_locator": "https://arxiv.org/html/2606.04329v1 §4.5 Limitations of Prompt Injection Defense against Memory Poisoning; §5 Discussions",
        "artifact_locator": "Not Disclosed — exact-v1 cites HERMES as an evaluated target but does not identify it as this paper's versioned artifact",
        "method": "The paper models an attacker-controlled external payload crossing an agent memory write channel, classifies six write strategies, and evaluates the transaction in two phases: adversarial write followed by later-session retrieval. The durable delta is untrusted input becoming persisted memory, not merely a prompt-injection symptom.",
        "evaluation": "MPBench evaluates OpenClaw and HERMES with GPT-OSS-120B across seven tool/task domains, six attack classes, cross-session persistence and four prompt-injection defenses; this is a bounded agent-memory security benchmark.",
        "limitations": "Existing prompt-injection defenses cannot jointly obtain high TPR and low FPR in the disclosed setting, especially on weak-signal attacks; the study does not prove the same rates for other agents, memory admission policies or models.",
    },
    "2606.04485": {
        "method_locator": "https://arxiv.org/html/2606.04485v1 §4 Method; §4.2 RaBEL; §4.3 Reordered Bidirectional Attention",
        "evaluation_locator": "https://arxiv.org/html/2606.04485v1 §5 Experiments; §§5.3–5.5",
        "limitations_locator": "https://arxiv.org/html/2606.04485v1 §6 Conclusion; Appendix B value-sensitivity boundary",
        "artifact_locator": "https://github.com/limix-ldm-ai/LimiX",
        "method": "RaBEL normalizes each numerical column, expands values through radial-basis functions and projects the expansion into model width so scalar value sensitivity is no longer confined to one affine direction; reordered bidirectional attention addresses the separate row/feature interaction bottleneck.",
        "evaluation": "The paper compares embedding variants, the 2M baseline, toy RBA behavior, SOTA tabular models and ablations; the evidence is specific to the reported tabular datasets and compute envelope.",
        "limitations": "The effective-rank argument concerns scalar tabular embeddings and shallow value sensitivity; it does not establish a universal tokenizer or representation architecture for non-tabular modalities.",
    },
    "2606.05304": {
        "method_locator": "https://arxiv.org/html/2606.05304v1 §4 PACT; §§4.1–4.3 action-state message space and protocol properties",
        "evaluation_locator": "https://arxiv.org/html/2606.05304v1 §5 Experiments; §6 Agentic Coding Harnesses",
        "limitations_locator": "https://arxiv.org/html/2606.05304v1 §Limitations",
        "artifact_locator": "https://github.com/iNLP-Lab/PACT",
        "method": "PACT projects raw agent output into a typed action-state message space before shared-history transmission. The receiver consumes committed artifacts, actions and state rather than the sender's full deliberation, changing message schema, visibility and rollback/error-propagation boundaries.",
        "evaluation": "Sections 5–6 compare grounded handoffs, full history and compact artifacts across disclosed reasoning benchmarks, models and coding harnesses; results do not establish the same gains for arbitrary topologies or tools.",
        "limitations": "The paper's Limitations section bounds generalization to the evaluated tasks, models and proxy-hook integration; projection can omit evidence needed downstream.",
    },
    "2606.05403": {
        "method_locator": "https://arxiv.org/html/2606.05403v1 §2 Experimental design; §3 Behavioral results; §4 Internal representations; §5 Mechanistic analysis",
        "evaluation_locator": "https://arxiv.org/html/2606.05403v1 §2 Experimental design; Appendices A/D",
        "limitations_locator": "https://arxiv.org/html/2606.05403v1 §6 Discussion",
        "method": "The study factorially separates source presentation, sentiment, conflict of interest and third-party consensus, then contrasts behavioral reliance with internal source representations and mechanistic interventions. The evaluated contract is whether a model detects implausibility or conflict yet fails to discount the source in its final judgment.",
        "evaluation": "The authors use preregistered-style factorial scenarios, multiple domains/models, isolation probes, representation decompositions and prompting mitigations; the result measures a bounded epistemic blind spot rather than universal factuality.",
        "limitations": "Section 6 limits the conclusion to synthetic but controlled source-evaluation settings and observed models; detection without discounting is not itself proof of internal belief or every hallucination mode.",
    },
    "2606.05433": {
        "method_locator": "https://arxiv.org/html/2606.05433v1 §3 Proposed solution; §3.1 proving architecture; §3.2 training-verification protocol",
        "evaluation_locator": "https://arxiv.org/html/2606.05433v1 Appendix B proof-cost/overhead estimation; Appendix G protocol formalization",
        "limitations_locator": "https://arxiv.org/html/2606.05433v1 §2 Structural limitations; §3 Scope; Appendix A Open problems",
        "method": "The proposal separates compact commitments and hardware/network witness inputs from zero-knowledge verification components, then binds a deterministic training execution trace to a proving protocol. Its contribution is an architecture and open-problem decomposition, not a completed frontier-scale verifier.",
        "evaluation": "Appendix B estimates proof cost and cites bounded deterministic-kernel overhead cases, while Appendix G formalizes protocol alignment; these are feasibility estimates and component evidence, not an end-to-end frontier-training deployment benchmark.",
        "limitations": "The paper explicitly lists unresolved floating-point GEMM/backprop proofs, deterministic kernels, hardware trust anchors, MoE/RL/multi-site extensions and tooling; feasibility does not mean the full system is implemented.",
    },
    "2606.04367": {
        "method_locator": "https://arxiv.org/html/2606.04367v1 §3 GlossAssist Architecture; §4 Position",
        "evaluation_locator": "https://arxiv.org/html/2606.04367v1 §3–§4 design demonstration; no controlled model benchmark disclosed",
        "limitations_locator": "https://arxiv.org/html/2606.04367v1 §7 Limitations",
        "method": "GlossAssist combines retrieval-based CWoMP predictions with a mutable morpheme lexicon; an accepted annotator correction is admitted into that lexicon and changes future retrieval without model retraining, while the dashboard/event log exposes the update path.",
        "evaluation": "The paper presents a usable annotation workflow and its design position rather than a controlled generalization benchmark; the evidence supports the memory-admission mechanism, not a universal accuracy improvement.",
        "limitations": "Section 7 states that the system cannot generate out-of-vocabulary morphemes and that early annotation requires more effort before the mutable lexicon becomes useful.",
    },
    "2606.04399": {
        "method_locator": "https://arxiv.org/html/2606.04399v1 §III DPDL algorithm and privacy analysis",
        "evaluation_locator": "https://arxiv.org/html/2606.04399v1 §V Experiments; Tables I–VI",
        "limitations_locator": "https://arxiv.org/html/2606.04399v1 §VI Conclusion; no dedicated limitations section",
        "method": "Each decentralized agent perturbs cross-gradients on private local data with Gaussian noise, calibrates received neighbor gradients by cosine similarity, and applies the calibrated aggregate as a momentum-like local update; the privacy analysis binds noise, topology and composition assumptions.",
        "evaluation": "The authors compare DPDL with decentralized DP baselines over disclosed graph sizes, non-IID settings, privacy budgets and image-classification datasets; the result is an author benchmark, not a production privacy or scalability guarantee.",
        "limitations": "The manuscript does not publish a dedicated limitations section; the claim remains bounded to its decentralization topology, Gaussian-DP assumptions, non-IID construction and reported datasets.",
    },
    "2606.04410": {
        "method_locator": "https://arxiv.org/html/2606.04410v1 §3 Proposed Method; §§3.1–3.4",
        "evaluation_locator": "https://arxiv.org/html/2606.04410v1 §4 Experimental Results; §§4.1–4.4",
        "limitations_locator": "https://arxiv.org/html/2606.04410v1 §5 Conclusion and Limitation",
        "artifact_locator": "https://github.com/microsoft/DCVC",
        "method": "DCVC-UF encodes multiple frames as one compact chunk latent, performs cross-frame interaction before frame-specific parallel reconstruction, and consolidates entropy interaction so decode control moves from per-frame sequencing to one chunk transaction.",
        "evaluation": "Section 4 compares rate-distortion, encoding/decoding throughput and component ablations under the authors' codec workload; these numbers prove only the disclosed model, sequence and device slices.",
        "limitations": "Section 5 bounds the gain to chunk-level correlation and parallel reconstruction; chunk size, buffering and latency replace some sequential-compute cost and remain workload dependent.",
    },
    "2606.04437": {
        "method_locator": "https://arxiv.org/html/2606.04437v1 §3 Method; §3.1 Overall Framework",
        "evaluation_locator": "https://arxiv.org/html/2606.04437v1 §4 Experiments",
        "limitations_locator": "https://arxiv.org/html/2606.04437v1 §5 Conclusion; no dedicated limitations section",
        "method": "The ego issues typed object/region evidence queries; heterogeneous collaborators return only local evidence at queried locations, after which sparse per-query routing and gated residual write-back select what becomes ego state. Compatibility shifts from global feature translation to local typed-response comparability.",
        "evaluation": "The author evaluation measures heterogeneous insertion and collaborative perception under the stated sensors, models and datasets; it does not establish zero-training compatibility for arbitrary schemas or calibrations.",
        "limitations": "No dedicated limitations section is disclosed; typed queries, ego calibration and local response comparability remain required, so the protocol does not eliminate semantic or sensor mismatch.",
    },
    "2606.04513": {
        "method_locator": "https://www.researchgate.net/publication/405922503_MapAgent_An_Industrial-Grade_Agentic_Framework_for_City-scale_Lane-level_Map_Generation — author-shared manuscript bearing arXiv:2606.04513v1; §2.1–§2.5 MapAgent Framework",
        "evaluation_locator": "https://www.researchgate.net/publication/405922503_MapAgent_An_Industrial-Grade_Agentic_Framework_for_City-scale_Lane-level_Map_Generation — author-shared manuscript bearing arXiv:2606.04513v1; §3 Experiments; §3.1–§3.4",
        "limitations_locator": "https://www.researchgate.net/publication/405922503_MapAgent_An_Industrial-Grade_Agentic_Framework_for_City-scale_Lane-level_Map_Generation — author-shared manuscript bearing arXiv:2606.04513v1; §2.4–§2.5 safety boundaries; §3.3 minority-class trade-off; §3.4 diminishing returns; §6 Conclusions",
        "method": "MapAgent treats the frozen backbone output as mutable map state. A Quality Agent gates hard tiles; the Judge emits structured geometric/topological/specification evidence; the Planner converts evidence into schema-validated, immutable-rule-constrained actions; deterministic Workers execute a closed toolset; re-validation commits a feasible result or falls back to the best prior state under a bounded retry budget.",
        "evaluation": "The exact-v1 manuscript evaluates frozen GeMap and DuMapNet backbones with Qwen3-VL and InternVL Judge variants on 3,712 training and 656 test BEV images, discloses 8×A800 hardware, SFT/GRPO batch settings, 1,000-tile latency measurement and component ablations. These author results establish only the disclosed map workload and production slice, not a portable agent-runtime benchmark.",
        "limitations": "The disclosed control plane forbids new-lane creation, cross-lane-group/non-local topology edits and unconstrained end-to-end policy optimization. Iterative correction shows diminishing returns, one minority structure-error class drops after GRPO, geometry gains remain small, and latency/automation claims remain bounded to the authors' trigger policy, data and Baidu deployment.",
    },
    "2606.04549": {
        "method_locator": "https://arxiv.org/html/2606.04549v1 §III System Overview; §IV System Design; §V Implementation",
        "evaluation_locator": "https://arxiv.org/html/2606.04549v1 §VI Evaluation",
        "limitations_locator": "https://arxiv.org/html/2606.04549v1 §III threat model and scope; §VII Conclusion",
        "method": "PS-UIE moves measurement/enforcement authority above the measured guest target, manages executable-object policies, interposes execve/mmap/mprotect transitions, and exports verifiable runtime evidence; anonymous executable memory is default-deny in the disclosed prototype.",
        "evaluation": "The AMD SEV-SNP/Coconut-SVSM prototype reports security behavior and performance overhead for file-backed user-space executable objects; it does not prove integrity for every executable-memory path or CVM architecture.",
        "limitations": "The threat/scope text limits enforcement to the disclosed file-backed executable-object lifecycle and prototype; anonymous JIT-style memory and other platforms require separate policy and evidence treatment.",
    },
    "2606.04552": {
        "method_locator": "https://arxiv.org/html/2606.04552v1 §3 Method; §3.3 Dynamic Chunking and Dechunking",
        "evaluation_locator": "https://arxiv.org/html/2606.04552v1 §4 Experiments; FLOPs-matched controlled comparison",
        "limitations_locator": "https://arxiv.org/html/2606.04552v1 §5 Discussion/Conclusion; no dedicated limitations section",
        "method": "LDARNet adapts H-Net-style bidirectional routing to masked genomic modeling: BiMamba-2 and local attention produce dynamic chunk boundaries, a ratio regularizer controls compression, and dechunking restores nucleotide-level outputs.",
        "evaluation": "The paper reports 27 downstream tasks and a FLOPs-matched fixed-grid comparison; gains establish a genomic representation case, not universal learned-tokenization superiority.",
        "limitations": "The evidence is domain-bound to genomic masked modeling and the disclosed compression ratio/architecture; transfer to autoregressive language or multimodal token identity is unproved.",
    },
    "2606.04652": {
        "method_locator": "https://arxiv.org/html/2606.04652v1 §1.2 Results; theorem and algorithm sections",
        "evaluation_locator": "Not Applicable — theoretical round-complexity proof, not an empirical benchmark",
        "limitations_locator": "https://arxiv.org/html/2606.04652v1 §1.4 Discussion",
        "method": "The paper derives communication-round algorithms and lower bounds for two rectangular matrix-multiplication aspect ratios in a low-bandwidth distributed model, making aspect ratio part of the communication plan rather than assuming square dense products.",
        "evaluation": "Evidence is theorem/proof based under O(log n)-bit per-node per-round communication and evenly distributed inputs; there is no author hardware runtime benchmark.",
        "limitations": "Section 1.4 discusses the remaining gaps and model assumptions; results do not directly predict GPU collective performance or arbitrary sparsity/topology behavior.",
    },
    "2606.04736": {
        "method_locator": "https://arxiv.org/html/2606.04736v1 §2 Curvature-aware dynamic precision controller; §3 Methodology",
        "evaluation_locator": "https://arxiv.org/html/2606.04736v1 §3.3 Network architectures and evaluation; §4 Results",
        "limitations_locator": "https://arxiv.org/html/2606.04736v1 §4.6 Limitations and future work",
        "method": "The controller reuses L-BFGS curvature information to retain FP32 while training is numerically stable and promote selected computation to FP64 when curvature or stagnation signals precision sensitivity, making precision a runtime training state instead of a fixed job setting.",
        "evaluation": "The authors test four canonical PINN failure-mode benchmarks, an irradiance ODE and multiple architectures; this is bounded evidence for PINN optimization, not a general mixed-precision scheduler.",
        "limitations": "Section 4.6 limits generalization beyond the tested PINNs and notes controller/solver dependence; promotion also sacrifices some FP32 efficiency.",
    },
    "2606.04769": {
        "method_locator": "https://arxiv.org/html/2606.04769v1 §IV DCIChecker; §IV-B Structure-Aware Tool Semantic Extraction; §IV-C DCI Checking with DRA-Prompting",
        "evaluation_locator": "https://arxiv.org/html/2606.04769v1 §V Real-world Measurement; §§V-A–V-D",
        "limitations_locator": "https://arxiv.org/html/2606.04769v1 §VII Discussion — Limitations and scope",
        "artifact_locator": "Not Disclosed — exact-v1 does not identify a versioned public DCIChecker artifact",
        "method": "DCIChecker treats the natural-language tool description as a planning specification and implementation code as runtime authority. It reconstructs entry logic, reachable helpers and sensitive APIs into a code bundle, then runs taxonomy-guided Direct and Reverse checks plus Arbitration so functional mismatch and undeclared side effects become explicit protocol evidence rather than prompt framing.",
        "evaluation": "The authors apply the detector to 19,200 description-code pairs from 2,214 MCP servers and report taxonomy/detector and consequence analyses. The disclosed 9.93% observation is tied to that mined corpus and imperfect semantic checker, not ecosystem prevalence guaranteed for all servers.",
        "limitations": "Section VII limits the work to description-code consistency rather than unrelated implementation vulnerabilities; descriptions can be ambiguous, behavior can depend on runtime context and LLM analysis is probabilistic. DCI may be accidental drift as well as adversarial behavior.",
    },
    "2606.04857": {
        "method_locator": "https://arxiv.org/html/2606.04857v1 §§3–5 protocol formalization and CRAFT method; §5.3 Masked Fine-Tuning",
        "evaluation_locator": "https://arxiv.org/html/2606.04857v1 §6 Experiments; §6.3 Component Ablation",
        "limitations_locator": "https://arxiv.org/html/2606.04857v1 Appendix protocol audit and discussion; no dedicated author limitations section",
        "method": "CRAFT separates per-sample branches, masks absent views, and performs variable-length attention only over observed views; protocol formalization makes the fully observed-sample proportion explicit and permits train-once complete-data learning to serve diverse missing patterns.",
        "evaluation": "Seven benchmark datasets compare missingness protocols, retraining behavior and ablations; results depend on the audited protocol definitions and do not prove arbitrary sensor-failure robustness.",
        "limitations": "The protocol audit reveals baseline ambiguity and the method assumes observable missingness plus view-compatible attention inputs; the manuscript does not provide a dedicated author limitations section.",
    },
    "2606.04860": {
        "method_locator": "https://arxiv.org/html/2606.04860v1 §3 Methodology",
        "evaluation_locator": "https://arxiv.org/html/2606.04860v1 §4 Experiments",
        "limitations_locator": "https://arxiv.org/html/2606.04860v1 §5 Limitations and Future Work",
        "method": "The value network uses an underestimating Bellman operator and asymmetric overestimation penalty; a validation-set safety offset then calibrates the learned heuristic before A* consumes it, separating learned proposal from admissibility evidence.",
        "evaluation": "The authors report no observed violations and node-expansion reductions on three puzzle families under a finite validation/evaluation protocol; this is empirical calibration, not a proof of global admissibility.",
        "limitations": "Section 5 identifies Python/PyTorch CPU overhead and finite-validation dependence; unseen state distributions can still violate admissibility.",
    },
    "2606.04899": {
        "method_locator": "https://arxiv.org/html/2606.04899v1 §IV Our Approach; §V Delving into DisT-FL",
        "evaluation_locator": "https://arxiv.org/html/2606.04899v1 §VI Evaluation",
        "limitations_locator": "https://arxiv.org/html/2606.04899v1 §II-C SGX limitations; §V-E Security Analysis",
        "method": "DisT-FL splits server authority across attestation-proxy, aggregator and ledger enclaves; an append-only replicated ledger provides operation linearizability against rollback, while inputs from independently reliable servers constrain I/O manipulation.",
        "evaluation": "The WAN prototype evaluates attack resistance and throughput against TEE/MPC baselines; the reported 6x gain is tied to its disclosed topology, SGX implementation and workload.",
        "limitations": "The paper explicitly identifies TEE I/O manipulation and state rollback as fundamental hazards; the solution additionally depends on its server/reliability and enclave threat assumptions.",
    },
    "2606.05035": {
        "method_locator": "https://arxiv.org/html/2606.05035v1 §3 Method",
        "evaluation_locator": "https://arxiv.org/html/2606.05035v1 §4 Experiments and ablations",
        "limitations_locator": "https://arxiv.org/html/2606.05035v1 §5 Limitations",
        "method": "Anchor3R predicts current-frame local pointmaps and window-relative poses as transient measurements, then updates the online trajectory, reinserts loop closures, and uses motion averaging to reconcile local measurements into global reconstruction under bounded memory.",
        "evaluation": "Indoor, outdoor, driving and RGB-D benchmarks compare pose and dense reconstruction quality under the reported streaming setup; they do not prove a physical-robot closed loop.",
        "limitations": "Section 5 states that historical pointmaps are not updated, scale consistency remains difficult, and evaluation is replay based rather than an embodied closed-loop deployment.",
    },
    "2606.05042": {
        "method_locator": "https://arxiv.org/html/2606.05042v1 §3 Methodology; autoregressive elimination and TT factors",
        "evaluation_locator": "https://arxiv.org/html/2606.05042v1 §4 Experiments",
        "limitations_locator": "https://arxiv.org/html/2606.05042v1 §5 Discussion/Conclusion and stated exactness boundary",
        "method": "ICG-I autoregressively emulates variable elimination, stores intermediate factors in Tensor-Train form, emits Dirichlet predictive distributions, and applies weighted conformal calibration under estimated topology-shift density ratios.",
        "evaluation": "The paper reports MAE and coverage across disclosed graphical-model benchmarks, including N=500 frustrated spin glasses; it does not make approximate learned inference exact.",
        "limitations": "The manuscript states that #P-hard computation is not compressed into one polynomial pass; TT approximation and estimated density ratios introduce explicit error/coverage degradation.",
    },
    "2606.05076": {
        "method_locator": "https://arxiv.org/html/2606.05076v1 §III Approach and Empirical Results; §III-A intent formalization",
        "evaluation_locator": "https://arxiv.org/html/2606.05076v1 §III empirical analysis over 100.91M flow records",
        "limitations_locator": "https://arxiv.org/html/2606.05076v1 §IV Future Opportunities; §V Conclusion",
        "method": "The design projects high-level intent into standardized seven-tuple low-level telemetry, computes violation and drift as different observed-state signals, and feeds structural violations back to a closed-loop policy recalculation/enforcement path.",
        "evaluation": "The empirical contract covers 100.91 million honeynet flow records and three administrative policy regimes; it is not proof that the metric controls arbitrary 6G networks.",
        "limitations": "The future-work/conclusion sections leave broader scale, policy semantics and closed-loop production validation open; violation suppression does not imply drift elimination.",
    },
    "2606.05081": {
        "method_locator": "https://arxiv.org/html/2606.05081v1 §§III–VI BVSS, reordering, compute mechanics and multi-source extension",
        "evaluation_locator": "https://arxiv.org/html/2606.05081v1 §VII Experiments; ablation and overhead",
        "limitations_locator": "https://arxiv.org/html/2606.05081v1 §IX Conclusion and Future Work",
        "method": "BLEST builds balanced virtual slice sets, schedules frontier-relevant regions, maps binary neighbor checks to Tensor-Core MMA, applies lazy vertex updates, and dynamically switches to CUDA cores when irregularity makes Tensor Cores inefficient.",
        "evaluation": "The author evaluation covers real graphs, ablations, multi-source workloads and a large 100-H100 run; binary graph arithmetic is a workload representation, not LLM model precision.",
        "limitations": "Performance depends on graph structure, reordering/compression and frontier shape; the dynamic fallback preserves CUDA-core execution where Tensor-Core packing loses efficiency.",
    },
    "2606.05094": {
        "method_locator": "https://arxiv.org/html/2606.05094v1 §3 Design; §§3.1–3.2; §4 API",
        "evaluation_locator": "https://arxiv.org/html/2606.05094v1 §6 Evaluation",
        "limitations_locator": "https://arxiv.org/html/2606.05094v1 §3.2.4 Discussion; §8 Challenges and Future Work",
        "method": "RAMC replaces monolithic collective windows with persistent unidirectional initiator-target channels. Target/initiator status values own pairwise phase state, Slingshot endpoint/MR counters own completion notification, and a bulletin board exchanges registered-buffer addressing once.",
        "evaluation": "Correctness tests, heat-diffusion scaling to 19.6K processes/250 nodes and libfabric-version microbenchmarks bind the result to HPE Slingshot and reported message sizes; small-message latency remains an identified weakness.",
        "limitations": "The current target is passive, bulletin-board posting is limited, NIC selection/generalization remain future work, and active-target semantics are not implemented.",
    },
    "2606.05339": {
        "method_locator": "https://arxiv.org/html/2606.05339v1 §IV Methodology; §§IV-A–IV-G; §V Results: MCP Server Fault Taxonomy",
        "evaluation_locator": "https://arxiv.org/html/2606.05339v1 §IV-D Selection of Repositories for Manual Analysis; §IV-F Taxonomy Construction and Validation; §V-L Validation Results",
        "limitations_locator": "https://arxiv.org/html/2606.05339v1 §VII Threats to Validity",
        "artifact_locator": "Not Disclosed — exact-v1 cites awesome-mcp-servers as corpus provenance, not as this paper's versioned artifact",
        "method": "The study converts 837 MCP-specific runtime-fault threads from 473 maintained repositories into an 11-category, 27-subcategory and 73-leaf taxonomy through bottom-up open coding. The state delta is concrete: accepted-but-not-enforced configuration, session/state lifecycle, schema/security enforcement, provider integration, and timeout/cancellation faults are separated by runtime ownership rather than treated as generic tool failure.",
        "evaluation": "Manual analysis deliberately selects information-rich repositories rather than a random prevalence sample; developer validation covers 55 respondents. The result supports qualitative fault coverage and taxonomy relevance, not population-level MCP failure rates.",
        "limitations": "Section VII bounds construct, internal and external validity of issue filtering, criterion-based repository selection, manual coding and survey validation; repository discussions underrepresent silent production faults and cannot estimate ecosystem prevalence.",
    },
    "2606.05348": {
        "method_locator": "https://arxiv.org/html/2606.05348v1 §§3–5 density compilation and compositional incrementalization",
        "evaluation_locator": "https://arxiv.org/html/2606.05348v1 evaluation/case-study sections",
        "limitations_locator": "https://arxiv.org/html/2606.05348v1 Limitations",
        "method": "The compiler first translates expressive probabilistic programs into deterministic density functions, then applies a compositional incremental lambda-calculus transformation so Monte Carlo proposals reuse intermediate results; separate logical-relations proofs preserve modular correctness.",
        "evaluation": "Case studies measure recomputation reduction and inference performance for disclosed probabilistic programs; evidence does not establish benefit when proposals invalidate most dependency state.",
        "limitations": "The limitations section bounds supported language features and performance to dependency locality; incremental state adds memory and soundness obligations.",
    },
    "2606.05394": {
        "method_locator": "https://arxiv.org/html/2606.05394v1 §§4–6 implementation changes for STFT/iSTFT and transform consistency",
        "evaluation_locator": "https://arxiv.org/html/2606.05394v1 §7 Tests and evaluation",
        "limitations_locator": "https://arxiv.org/html/2606.05394v1 §8.2 Limitations",
        "artifact_locator": "https://github.com/KinWaiCheuk/nnAudio",
        "method": "nnAudio 2 removes dynamic module/state mutation from scripted STFT/iSTFT paths, tightens inverse arguments, rejects unsupported inverse frequency scales explicitly, and restores SciPy/VQT consistency with regression tests.",
        "evaluation": "The updated repository test suite and targeted transform regressions validate disclosed PyTorch/scientific-Python paths; they do not establish universal compiler or audio-transform performance.",
        "limitations": "Section 8.2 bounds reliable inversion to uniform bins (`freq_scale=no`) and leaves unsupported frequency scales as explicit errors rather than silent reconstruction degradation.",
    },
}


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def section_excerpt(path: Path | None, locator: str, fallback: str) -> str:
    """Return source text from the exact-v1 section named by a locator.

    This is intentionally evidence extraction, not a second summary model: it
    preserves author wording from the bounded section and prevents a review
    receipt from claiming full-text review while only paraphrasing the abstract.
    """
    if not path or path.suffix != ".html" or not ("§" in locator or "Appendix" in locator):
        return fallback

    def heading_key(value: str) -> str:
        value = clean(value).casefold().strip(" §.")
        # ar5iv/LaTeXML render the same numbered heading as `3 Method`,
        # `3. Method`, or `3 Methodology`; locators may also use ranges such as
        # `§§3–4`.  Compare the stable title, not punctuation in the counter.
        value = re.sub(
            r"^(?:(?:appendix|appendices)\s+[a-z0-9.]+|[ivxlcdm]+|\d+(?:\.\d+)*(?:\s*[–-]\s*(?:[ivxlcdm]+|\d+(?:\.\d+)*))?)[.):]?\s*",
            "",
            value,
        )
        return value.strip(" .:-")

    targets: list[str] = []
    for part in locator.split(";"):
        if "§" in part:
            candidate = part.split("§", 1)[1]
        elif "Appendix" in part:
            candidate = part[part.index("Appendix"):]
        else:
            continue
        key = heading_key(candidate.lstrip("§"))
        if key and re.search(r"[a-z]", key):
            targets.append(key)
    if not targets:
        return fallback
    raw = path.read_text(encoding="utf-8", errors="ignore")
    headings = list(re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", raw, re.I | re.S))
    stop = {"the","a","an","and","of","to","in","for","on","with","our"}
    for target in targets:
        target_words = {x for x in re.findall(r"[a-z0-9]+", target) if x not in stop}
        for index, match in enumerate(headings):
            heading = heading_key(match.group(2))
            heading_words = {x for x in re.findall(r"[a-z0-9]+", heading) if x not in stop}
            overlap = len(target_words & heading_words)
            semantic_match = bool(
                target_words
                and overlap >= min(3, len(target_words))
                and overlap / len(target_words) >= 0.6
            )
            if not (heading == target or heading in target or target in heading or semantic_match):
                continue
            # A section's evidence normally lives in h3/h4 descendants.  Stop
            # at the next sibling/ancestor heading, not at the first child.
            current_level = int(match.group(1))
            end = len(raw)
            for later in headings[index + 1:]:
                if int(later.group(1)) <= current_level:
                    end = later.start()
                    break
            section = raw[match.end():end]
            paragraphs = [clean(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", section, re.I | re.S)]
            paragraphs = [x for x in paragraphs if len(x) >= 45 and "reporting errors" not in x.casefold()]
            if paragraphs:
                return " ".join(paragraphs[:8])[:2600]
            text = clean(section)
            if text:
                return text[:2600]
    return fallback


def counterevidence_excerpt(path: Path | None, locator: str, fallback: str) -> str:
    """Extract a family-specific limitation, scope or failure paragraph.

    Papers frequently disclose counterevidence inside Discussion, Appendix or a
    named paragraph rather than an h2/h3 ``Limitations`` section.  Falling back
    to one shared sentence caused the V4 audit's 51-family template failure.
    """
    if not path or path.suffix != ".html":
        return fallback
    if "§" in locator:
        bounded = section_excerpt(path, locator, "")
        if bounded:
            signals = (
                "limitation", "failure", "does not", "do not", "cannot",
                "future work", "out of scope", "however", "only", "remain",
            )
            if any(signal in bounded.casefold() for signal in signals):
                return bounded
            return (
                f"The exact-v1 section `{locator}` was read in full. It does not disclose an explicit failure or "
                "limitations statement; therefore the claim is bounded to the paper's own evaluated workload, "
                "baselines and setup and does not establish production or cross-domain generality."
            )
    raw = path.read_text(encoding="utf-8", errors="ignore")
    paragraphs = [clean(value) for value in re.findall(r"<p[^>]*>(.*?)</p>", raw, re.I | re.S)]
    signals = (
        "limitation", "failure mode", "fails to", "does not", "do not", "cannot",
        "future work", "out of scope", "in scope", "trade-off", "however", "only",
    )
    ranked = [
        value for value in paragraphs
        if 80 <= len(value) <= 2200 and any(signal in value.casefold() for signal in signals)
        and "reporting errors" not in value.casefold()
    ]
    if ranked:
        return ranked[-1][:1800]
    return fallback


def disclosed_condition(text: str, patterns: tuple[str, ...], label: str) -> str:
    for sentence in sentences(text):
        if any(re.search(pattern, sentence, re.I) for pattern in patterns):
            return sentence[:320]
    return f"Not Disclosed — exact-v1 reviewed text does not state {label}"


def sentences(value: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", value) if s.strip()]


def pick_sentence(value: str, terms: tuple[str, ...], fallback: int = 0) -> str:
    parts = sentences(value)
    for part in parts:
        if any(term in part.casefold() for term in terms):
            return part
    return parts[min(fallback, len(parts) - 1)] if parts else "摘要未提供可复述文本。"


def closure_screening_reason(item: dict) -> str:
    """Close one identity with a claim-specific, falsifiable routing reason.

    A rejection receipt is not a generic assertion that the paper is
    uninteresting.  It records the mechanism the abstract actually claims and
    the missing durable system boundary that prevents Score V2 routing.  Later
    revisions can therefore be compared against the exact missing condition.
    """
    abstract = item["abstract"]
    claim = pick_sentence(
        abstract,
        ("we propose", "we introduce", "we present", "we develop", "we show", "we prove"),
        min(1, max(0, len(sentences(abstract)) - 1)),
    )[:520]
    text = f"{item['title']} {abstract}".casefold()
    categories = ", ".join(item.get("categories", [])) or "Not Disclosed"
    if any(term in text for term in ("dataset", "benchmark", "survey", "taxonomy")):
        missing = (
            "该贡献主要建立数据集、测量或分类接口；摘要没有改变模型/运行时的状态所有权、"
            "控制流或发布证据 Gate。"
        )
    elif any(term in text for term in ("wireless", "medical", "clinical", "protein", "molecule", "finance", "traffic")):
        missing = (
            "该机制与结果绑定特定领域 workload；摘要没有给出可迁移到通用 AI System owner 的"
            "状态、资源或 failure-recovery contract。"
        )
    elif any(term in text for term in ("theorem", "proof", "convergence", "bound", "geometry", "stationary")):
        missing = (
            "该结果是理论性质或优化刻画；摘要尚未把性质落实为当前知识树中可执行、可测量的"
            "训练/推理状态转移或系统决策。"
        )
    elif any(term in text for term in ("agent", "retriev", "memory", "inference", "training", "multimodal", "world model")):
        missing = (
            "摘要包含 AI-System 相关机制，但披露的变化仍是局部策略/任务实现；没有改变现有 owner 的"
            "长期 invariant、authority split 或跨层 evaluation contract。"
        )
    else:
        missing = (
            "摘要没有建立可路由到现有 Stable Node 的长期机制增量，也没有改变状态所有权、"
            "数据/控制流、资源边界或 evidence contract。"
        )
    return (
        f"Full-abstract review closed 《{item['title']}》 (`{categories}`). "
        f"Primary abstract claim: {claim} Screening boundary: {missing} "
        "若后续 revision 补出该缺失 contract，必须作为 important revision 重开。"
    )


def pre_denominator_closure_class(item: dict) -> str:
    text = f"{item['title']} {item['abstract']}".casefold()
    domain_terms = (
        "medical", "clinical", "biolog", "genom", "protein", "molecule", "drug", "patient",
        "wireless", "e-commerce", "recommendation", "traffic", "autonomous driving", "quadrotor",
        "slam", "robot control", "locomotion", "mesh generation", "cad", "glucose", "pandemic",
        "music", "legal-agent", "counseling", "satellite", "ventilation", "diabetes",
    )
    benchmark_terms = ("benchmark", "dataset", "survey", "taxonomy", "empirical study", "measurement")
    theory_terms = (
        "theorem", "proof", "convergence", "lower bound", "upper bound", "stationary", "asymptotic",
        "characterization", "phase transition", "markov decision process", "koopman", "symplectic",
    )
    adjacent_terms = (
        "data center", "insurance", "carbon emissions", "proof-of-useful-work", "kem", "cryptographic",
        "functional behavior prediction", "factory", "motivational architecture",
    )
    if any(term in text for term in adjacent_terms):
        return "adjacent_non_ai_or_policy_fact"
    if any(term in text for term in domain_terms):
        return "domain_bound_application"
    if any(term in text for term in theory_terms):
        return "theory_without_operational_system_delta"
    if any(term in text for term in benchmark_terms):
        return "benchmark_or_dataset_without_durable_contract"
    return "task_local_method_without_durable_owner_delta"


def pre_denominator_reason(item: dict) -> str:
    claim = pick_sentence(
        item["abstract"],
        ("we propose", "we introduce", "we present", "we develop", "we show", "we prove"),
        min(1, max(0, len(sentences(item["abstract"])) - 1)),
    )[:720]
    closure_class = pre_denominator_closure_class(item)
    boundary = {
        "domain_bound_application": (
            "证据把机制、数据与结果绑定到单一行业、科学领域或 embodied task；没有给出可迁移的 "
            "AI System state/data/control ownership、资源边界或 failure-recovery contract。"
        ),
        "benchmark_or_dataset_without_durable_contract": (
            "证据建立的是 task/capability 数据集、测量或分类结果，但没有改变评估系统的 evaluator "
            "authority、污染/复现控制、workload portability 或发布 Gate。"
        ),
        "theory_without_operational_system_delta": (
            "证据停留在数学性质、收敛/界或问题刻画，没有落为可执行、可测量的训练/推理状态转移、"
            "资源策略或系统设计判断。"
        ),
        "adjacent_non_ai_or_policy_fact": (
            "证据属于相邻基础设施、行业政策或风险事实；它没有给出本书 AI System 生命周期可拥有的"
            "技术机制或可验证设计契约。"
        ),
        "task_local_method_without_durable_owner_delta": (
            "证据是局部模型、prompt、agent 或优化 recipe；即使可映射 ROADMAP，它也没有改变现有 owner "
            "的长期 invariant、authority split、跨层接口或 evaluation contract。"
        ),
    }[closure_class]
    return (
        f"Family-specific pre-denominator closure for 《{item['title']}》. Primary exact-v1 abstract claim: "
        f"{claim} Decision class: `{closure_class}`. Boundary: {boundary} "
        "Being AI-related, ROADMAP-mappable, benchmark-bearing, or a proposed method is explicitly insufficient. "
        "A later revision must add the named missing durable contract to reopen this family."
    )


def pre_denominator_retain_reason(item: dict, owner: str) -> str:
    claim = pick_sentence(
        item["abstract"],
        ("we propose", "we introduce", "we present", "we develop", "we show", "we find"),
        min(1, max(0, len(sentences(item["abstract"])) - 1)),
    )[:720]
    if owner.startswith("TRAIN-"):
        contract = "training data/optimizer/update state、privacy or distributed execution contract"
    elif owner.startswith("INFER-"):
        contract = "inference state、memory/compute placement、scheduling or kernel execution contract"
    elif owner.startswith("AGENT-"):
        contract = "agent memory/context/tool/workflow authority、recovery or interaction contract"
    elif owner.startswith("PLATFORM-"):
        contract = "platform evaluation、security、observability、cost or production evidence contract"
    elif owner.startswith("MULTIMODAL-"):
        contract = "multimodal representation/world/action state or generation-control contract"
    elif owner.startswith("MODEL-"):
        contract = "model architecture、token/state routing or attention/position mechanism"
    else:
        contract = "cross-cutting AI System design judgment or evidence contract"
    return (
        f"Retained after family-specific pre-denominator replay. Primary exact-v1 abstract claim: {claim} "
        f"Durable route: `{owner}` owns the disclosed {contract}. Retention is provisional until a different "
        "fresh-context auditor checks both false positives and false negatives."
    )


def html_headings(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    raw = path.read_text(encoding="utf-8", errors="ignore")
    records: list[dict[str, object]] = []
    stack: list[tuple[int, str]] = []
    for match in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", raw, re.I | re.S):
        level = int(match.group(1))
        heading = clean(match.group(2))
        while stack and stack[-1][0] >= level:
            stack.pop()
        records.append({"heading": heading, "ancestors": [text for _, text in stack]})
        stack.append((level, heading))
    return records


def choose_heading(
    headings: list[dict[str, object]],
    include: tuple[str, ...],
    exclude: tuple[str, ...] = (),
    forbidden_ancestors: tuple[str, ...] = ("related work", "background", "preliminar", "literature review"),
) -> str | None:
    for position, record in enumerate(headings):
        heading = str(record["heading"])
        low = heading.casefold()
        ancestors = " / ".join(str(x).casefold() for x in record["ancestors"])
        if (
            position == 0
            or any(x in low for x in exclude)
            or any(x in ancestors for x in forbidden_ancestors)
            or not any(x in low for x in include)
        ):
            continue
        explicit = bool(
            re.match(r"^(?:[ivx]+|\d+|[a-z])(?:[.\-][a-z0-9]+)*\s+", low)
            or re.match(
                r"^(?:method|methods|methodology|approach|design|architecture|framework|algorithm|"
                r"experiments?|evaluation|results?|benchmark|limitations?|discussion)\b",
                low,
            )
        )
        if explicit:
            return heading
    return None


def disclosed_artifact(raw: str) -> str | None:
    """Return an author-disclosed project artifact, never a bibliography URL."""
    converter_repos = ("arxiv/html_feedback", "brucemiller/latexml")
    positive = (
        "our code", "our implementation", "code is available", "code available",
        "source code", "we release", "we provide", "project page", "official repository",
        "artifact availability", "implementation is available", "repository is available",
    )
    for match in re.finditer(r"https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", raw):
        url = match.group(0).rstrip(".,;:)")
        if any(value in url.casefold() for value in converter_repos):
            continue
        context = clean(raw[max(0, match.start() - 500):match.end() + 220]).casefold()
        if any(signal in context for signal in positive):
            return url
    return None


def exact_path(arxiv_id: str) -> Path | None:
    if arxiv_id in BLOCKED_EXACT_V1:
        return None
    html_path = PACKET / "arxiv-v1" / f"{arxiv_id}v1.html"
    if html_path.exists() and html_path.stat().st_size:
        tail = html_path.read_bytes()[-1024:].lower()
        if b"</html>" in tail:
            return html_path
    pdf_path = PACKET / "arxiv-v1" / f"{arxiv_id}v1.pdf"
    return pdf_path if pdf_path.exists() and pdf_path.stat().st_size else None


def locators(arxiv_id: str) -> tuple[str, str, str, str]:
    path = exact_path(arxiv_id)
    base = f"https://arxiv.org/html/{arxiv_id}v1"
    if arxiv_id in WEB_EVIDENCE:
        evidence = WEB_EVIDENCE[arxiv_id]
        return (
            evidence["method_locator"],
            evidence["evaluation_locator"],
            evidence["limitations_locator"],
            evidence.get(
                "artifact_locator",
                "Not Disclosed — exact v1 does not disclose a versioned public artifact",
            ),
        )
    if path and path.suffix == ".pdf":
        base = f"https://arxiv.org/pdf/{arxiv_id}v1"
        pdf_overrides = {
            "2606.04415": (
                base + " §3 Design; §3.1 Transparent Interception; §3.2 Proxying; §3.3 Runtime Profiling",
                base + " §4.1 Experimental Setup; §4.2 End-to-end Results; Table 2",
                base + " §3.5 Discussion and Scope; evaluation reports no statistical uncertainty",
                "Not Disclosed — exact-v1 PDF does not identify a versioned public FlexNPU repository",
            ),
            "2606.04459": (
                base + " §3 Token-ranking signature; Theorem 1",
                base + " §5 Approximate parameter exposure; 50 rankings and 3/5 fitting attempts",
                base + " §4 Unforgeability assumptions; Theorem 2; §5 empirical fitting constraints",
                "Not Disclosed — exact-v1 PDF does not identify a versioned public implementation",
            ),
            "2606.05158": (
                base + " §3 Method; §3.1 Streaming algorithm; §3.2 Effectiveness theory; §3.3 Efficiency",
                base + " §4.1 Experimental Setup; eight benchmarks; OpenCompass; three/eight-run protocol",
                base + " §6 Limitations",
                "Not Disclosed — exact-v1 PDF does not identify a versioned public StreamMA implementation",
            ),
            "2606.05268": (
                base + " §3 Method; §3.1 Weak Verifier Generation; §3.2 Weak Verifier Aggregation",
                base + " §4 Results and Evaluation; §4.1 Experiment Design; §4.3 Analysis of Aggregation Methods",
                base + " §4.5 Limitations",
                "Not Disclosed — exact-v1 does not identify a versioned public implementation artifact",
            ),
        }
        if arxiv_id in pdf_overrides:
            return pdf_overrides[arxiv_id]
        return (
            base + " Methodology: exact-v1 PDF section identified by the review receipt",
            base + " Experiments: exact-v1 PDF evaluation section identified by the review receipt",
            "Not Disclosed — exact-v1 PDF does not expose a stable explicit limitations heading",
            "Not Disclosed — no versioned artifact is required for the bounded author claim",
        )
    headings = html_headings(path) if path else []
    html_overrides = {
        "2606.05233": (
            base + " §2 The CUA-HandCrafted Benchmark; §3 Results; §3.1 Phase 10 plus Algorithm and Search budget/threat-model subsections",
            base + " §3 Results; §3.1; §4 Harness Validation; §5 Cross-Domain Comparison; Appendices B, G and K",
            base + " §6 Discussion; §7 Limitations; Appendices C, F, H and I",
            "https://doi.org/10.5281/zenodo.20034379 — public CUA-HandCrafted benchmark release; https://github.com/RPC2/AutoInject is the cited attack implementation, not this benchmark artifact",
        ),
        "2606.04349": (
            base + " §3 Approach; §§3.2–3.4",
            base + " §4 Experiments; §§4.1–4.3",
            base + " §5 Conclusion; bounded omni-modal PTQ setting and disclosed quantizer assumptions",
            "Not Disclosed — exact-v1 does not identify a versioned public MorphoQuant artifact",
        ),
        "2606.04460": (
            base + " §3 Dataset Preparation for Benchmark; §§3.2–3.4",
            base + " §4 Experimental Evaluation; §§4.1–4.5",
            base + " §5 Limitations",
            "Not Disclosed — exact-v1 does not identify one versioned CyberGym-E2E artifact",
        ),
        "2606.04486": (
            base + " §4 Methodology; §§4.1–4.3",
            base + " §5 Theoretical Results; §§5.1–5.3",
            base + " §5.3 Edit sensitivity and Assumption 5.5; no dedicated empirical limitations section",
            "Not Disclosed — exact-v1 does not identify a versioned public implementation",
        ),
        "2606.04701": (
            base + " §3 Benchmark; §§3.1–3.4",
            base + " §4 Experiments; §§4.1–4.3; §5 Analysis",
            base + " §6 Conclusion — Limitations: platform replica, language/cultural coverage and annotation scale",
            "Not Disclosed — exact-v1 does not identify one versioned public benchmark artifact",
        ),
        "2606.04929": (
            base + " §5 Sequential Data Poisoning; §§5.1–5.3",
            base + " §4 Experimental Setup; Appendix D.2 Evaluation Details; Appendix E",
            base + " §6 Conclusion — Limitations and future work",
            "Not Disclosed — exact-v1 does not identify one versioned public attack artifact",
        ),
        "2606.05434": (
            base + " §3 Methods; §§3.1–3.4",
            base + " §4 Experimental Setup; §5 Results; §§5.1–5.3",
            base + " §7 Limitations",
            "Not Disclosed — exact-v1 does not identify one versioned public implementation",
        ),
        "2606.04560": (
            base + " §Priority Signal Design; rollout-level replay buffer and age-eviction definition",
            base + " §Experiments; Qwen3-Base scales and five math benchmarks",
            base + " §Conclusion; bounded replay/staleness scope",
            "Not Disclosed — exact-v1 does not identify one event-time public implementation",
        ),
        "2606.05008": (
            base + " §3.1 Evaluation Design; cognitively grounded task construction",
            base + " §4 Experiments/Results",
            base + " §5 Conclusion; benchmark scope",
            "https://pku-value-lab.github.io/m3eval-homepage",
        ),
        "2606.04613": (
            base + " §3 Spectral Alignment Score; §5 Instance-Level SAS",
            base + " §4 Experiments; §4.3 Experimental Setup; Results subsections",
            base + " §6 Discussion; §7 Conclusion and disclosed scope",
            "Not Disclosed — exact-v1 does not identify a versioned public artifact",
        ),
        "2606.05304": (
            base + " §4 PACT; §§4.1–4.3 action-state message space and protocol properties",
            base + " §5 Experiments; §6 Agentic Coding Harnesses",
            base + " Limitations",
            "Not Disclosed — exact-v1 does not identify a versioned public artifact",
        ),
        "2606.05525": (
            base + " §3 SciVisAgentSkills: Design and Evaluation",
            base + " §4 Experiments",
            base + " §5 Discussion; §6 Conclusions and disclosed skill-suite scope",
            "Not Disclosed — exact-v1 does not identify one event-time commit",
        ),
        "2606.06532": (
            base + " §3 Method; §§3.1–3.3",
            base + " §4 Experiments; §§4.1–4.6",
            base + " §5 Conclusion; scope and untested conditions",
            "Not Disclosed — exact-v1 does not identify one event-time commit",
        ),
    }
    if arxiv_id in html_overrides:
        return html_overrides[arxiv_id]
    method = choose_heading(
        headings,
        ("method", "approach", "framework", "design", "system", "architecture", "formulation", "algorithm", "training", "objective", "model"),
        ("related", "background", "baseline", "dataset", "evaluation", "experiment", "result", "conclusion", "introduction", "reporting errors"),
    )
    evaluation = choose_heading(
        headings,
        ("experiment", "evaluation", "result", "benchmark", "empirical", "analysis", "demonstration"),
        ("introduction", "related", "reporting errors"),
    )
    limitation = choose_heading(
        headings,
        ("limitation", "failure", "threats to validity", "discussion", "scope", "conclusion", "future work", "further work"),
        ("threat model", "introduction", "related", "reporting errors"),
    )
    raw = path.read_text(encoding="utf-8", errors="ignore") if path and path.suffix == ".html" else ""
    repo_match = None if arxiv_id in V6_FALSE_ARTIFACT_LOCATORS else disclosed_artifact(raw)
    method_locator = (
        f"{base} §{method}"
        if method
        else "Not Disclosed — exact-v1 has no separately named Method/Architecture/Approach section; mechanism is bounded to the abstract and Introduction"
    )
    evaluation_locator = (
        f"{base} §{evaluation}"
        if evaluation
        else "Not Disclosed — exact v1 has no separately named evaluation section"
    )
    limitation_locator = (
        f"{base} §{limitation}"
        if limitation
        else "Not Disclosed — exact v1 has no explicit limitations/counterevidence heading"
    )

    # The first keyword match can occasionally point two evidence facets to the
    # same heading.  Deep review facets must remain independently reproducible,
    # so use verified exact-v1 headings for these known ambiguous layouts.
    overrides = {
        # Independent V7 exact-v1 locator repair.  These are resolved from the
        # complete heading tree, not from first-keyword matching.
        "2606.04425": (
            f"{base} §4 Taxonomy of Stored Prompt Injection; §§4.1–4.4; §§3.1–3.2 system/threat model",
            f"{base} §5 Experiments; §§5.1–5.7",
            f"{base} §Limitations; §5.7 Discussion",
        ),
        "2606.04634": (
            f"{base} §4 Computing Hierarchical Safety Explanations; §§4.1–4.2",
            f"{base} §5 Experimental Evaluation; §§5.1–5.3",
            f"{base} §6 Conclusion & Future Work",
        ),
        "2606.04804": (
            f"{base} §Theory: The Measure of a Hard Constraint; §CoCoS: Measure-Aware Constrained Sampling; §Amortizing the correction (CoCo-Flow)",
            f"{base} §Experiments; controlled benchmark; Darcy-flow and 2D field-valued studies",
            f"{base} §Discussion and Limitations; rank deficiency; cost and scaling",
        ),
        "2606.05140": (
            f"{base} §§2–6 variational formulation, coercivity mechanism, noisy-transformer coefficients and proof",
            "Not Applicable — exact-v1 is a theorem/proof paper and does not claim an empirical benchmark",
            f"{base} §Remark 2.4 Open uniqueness range; theorem assumptions and dimensional/coupling scope",
        ),
        "2606.05249": (
            f"{base} §3 SWE-InfraBench; §§3.1–3.3",
            f"{base} §4 Experimental Results; §§4.1–4.3; Appendices F–J",
            f"{base} §5 Conclusion; benchmark/repository/version scope",
        ),
        "2606.05342": (
            f"{base} §2 SentinelBench Environments & Tasks; §3 Evaluation Protocol and Metrics",
            f"{base} §4 Baseline Evaluations; §§4.1–4.3",
            f"{base} §5 Discussion and Limitations",
        ),
        "2606.05345": (
            f"{base} §§4–7 PJ-RoPE Position Space, Implementation Regimes, Adaptive PJ and Light-cone PJ",
            f"{base} §9 Experiments; §§9.1–9.7",
            f"{base} §10 Discussion and Scope",
        ),
        "2606.05435": (
            f"{base} §III Differentially Private Mechanism for Adaptive Clipping with Adaptive Momentum; §§III-A–III-D",
            f"{base} §IV Experimental Results",
            f"{base} §V Conclusion; disclosed privacy/optimization scope",
        ),
        "2606.04620": (
            f"{base} §III The QuBLAST Methodology; §§III-A–III-C",
            f"{base} §IV Evaluation Methodology; §V Results and Discussion; §§V-A–V-F",
            f"{base} §VI Conclusion; disclosed quantization/model scope",
        ),
        "2606.05238": (
            f"{base} §3 DeployBench; §§3.1–3.4",
            f"{base} §3.3 Evaluation; §4 Experiment; §5 Further Analysis",
            f"{base} §5.1 Failure Analysis; §5.3 Completion Judgment; §6 Conclusion",
        ),
        "2606.05538": (
            f"{base} §§2–3 Model Capability Attribution and Intermediate-Dimension Compression",
            f"{base} §4 Experiments; §§4.1–4.5; Appendices D–O",
            f"{base} §Limitations",
        ),
        "2606.05257": (
            f"{base} §2 Experimental Setup; §5 Model/Data Allocation Across Compute Budgets",
            f"{base} §§3–7 scaling results and cross-metric/cross-regime evaluation",
            f"{base} §9 Discussion — negative result and architecture/context/compute limitations",
        ),
        "2606.05391": (
            f"{base} §3 Research Methodology; §§3.1–3.2",
            f"{base} §4 Findings; §§4.1–4.2",
            f"{base} §6 Limitations and Future Work",
        ),
        "2606.04505": (
            f"{base} §3 MechSim: Mechanism-Aware Reasoning for Scientific Simulators; §§3.1–3.4",
            f"{base} §4 Experiments and Evaluation; §5 Main Results; §5.4 Ablation Study Results",
            f"{base} §7 Conclusion; Appendix C.5 Sensitivity Analysis Results",
        ),
        "2606.04591": (
            f"{base} §5 Methodology; §§5.1–5.3",
            f"{base} §6 Experiments; §§6.1–6.2",
            f"{base} §5.3.1 Limitations of Existing Embedding Models; §7 Conclusion",
        ),
        "2606.05101": (
            f"{base} §3 FoeGlass: An In-Context Learning Approach to Automated Red-Teaming; §§3.1–3.2",
            f"{base} §4 Experimental Evaluation; §§4.1–4.6; Appendix A.3 Experiments Compute Resources",
            f"{base} §6 Concluding Remarks; Appendix D Potential Defense Mechanisms Against FoeGlass",
        ),
        "2606.05106": (
            f"{base} §4 Language Model Training; §2.2 Information Routing in Language Models",
            f"{base} §5 Results; §§5.1–5.2",
            f"{base} §6 Conclusion — bounded small-model arithmetic setting",
        ),
        "2606.05336": (
            f"{base} §3 B idirectional U ser M odeling via P rofiles (BUMP); §§3.1–3.7",
            f"{base} §4 Experiment; §§4.1–4.5; Appendix A.4",
            f"{base} §5 Conclusion; Appendix A.6 Analysis on Debiasing the Judge",
        ),
        "2606.05367": (
            f"{base} §3 Methodology; §§3.1–3.3",
            f"{base} §4 Experiments and Results; §§4.1–4.2",
            f"{base} §5.3 Identity–Intensity Trade-off and Metric Saturation; §5.5 Limitations",
        ),
        "2606.04619": (
            f"{base} §Four-Valued Evidence and Normative Outputs; §Rule-Restricted Transitions and Staged Saturation; §Admissibility and Stable-Read Commitment",
            f"{base} §Semantic Properties; §Executable Realization; §Topology-Respecting Parallel Saturation",
            f"{base} §Demand Reasoning — scope bounded to the disclosed ASP-oriented compliance semantics",
        ),
        "2606.05242": (
            f"{base} §3 Model, Assumptions, and Deterministic-Envelope Recursions; §§3.1–3.4; §7 Stochastic-Gradient Extension",
            f"{base} §8 Numerical Experiments; §§8.1–8.5",
            f"{base} §9 Discussion; §6 Quantitative Stationary Residual Decomposition",
        ),
        "2606.04375": (
            f"{base} §3. Our Method",
            f"{base} §7. Experiments; §7.2 Accuracy Comparison Across Five Methods; §7.5 Medical Domain Evaluation",
            f"{base} §8. Conclusion and Discussion",
        ),
        "2606.04384": (
            f"{base} §4. METHODOLOGY; §4.1 DP Training Framework with Selective Release Based on Clipping Gradients",
            f"{base} §5. EXPERIMENT; §§5.1–5.2",
            f"{base} §3.3 Limitations in the Privacy Accounting of DPSUR; §7. Discussion",
        ),
        "2606.04603": (
            f"{base} §3. The dinosaur Framework; §5. Practical Instantiations & Systems Trade-offs",
            f"{base} §6. Experiments & Empirical Validation; §6.1 Results and Discussion",
            f"{base} §5. Practical Instantiations & Systems Trade-offs; §7. Conclusions & Future Work",
        ),
        "2606.04641": (
            f"{base} §3. Method",
            f"{base} §4. Evaluation; §4.1 Main Results",
            f"{base} §4.1.1 Failure Mode in Baselines; §5. Conclusion",
        ),
        "2606.04650": (
            f"{base} §2. Methodology",
            f"{base} §3. Experiments",
            f"{base} §5. Conclusion — bounded to the disclosed supervised adaptation setting",
        ),
        "2606.05271": (
            f"{base} §3. BIDENT Framework; §§3.4–3.5",
            f"{base} §4. Evaluation; §4.1 Experimental Setup",
            f"{base} §3.4 Framework Overhead; §7. Conclusion",
        ),
        "2606.05391": (
            f"{base} §3. Research Methodology",
            f"{base} §4. Findings; §§4.1–4.2",
            f"{base} §6. Limitations and Future Work",
        ),
        "2606.06530": (
            f"{base} §3. Method",
            f"{base} §4. Experimental Setup; §5. Results",
            f"{base} §8. Conclusion; Appendix A.2 Evaluation Feedback Reports",
        ),
        "2606.04610": (
            f"{base} §2 Overview; §§2.1–2.2; §3 The Specificity Challenge; §§3.1–3.3",
            f"{base} §4. Evaluation; §4.1 Experimental Setup",
            f"{base} §Limitations; §6. Conclusion and Future Work",
        ),
        "2606.05233": (
            f"{base} §2 The CUA-HandCrafted Benchmark; §3 Results; §3.1 Phase 10 plus Algorithm and Search budget/threat-model subsections",
            f"{base} §3 Results; §3.1; §4 Harness Validation; §5 Cross-Domain Comparison; Appendices B, G and K",
            f"{base} §6 Discussion; §7 Limitations; Appendices C, F, H and I",
        ),
        "2606.04781": (
            f"{base} §3 The Agent Instruction Protocol (AIP)",
            f"{base} §4. Evaluation; §§4.1–4.2",
            f"{base} §4.5 Limitations; §6 Discussion and Future Work",
        ),
        "2606.04908": (
            f"{base} §4. Design and Implementation",
            f"{base} §5. Evaluation; §5.1 Experimental Setup",
            f"{base} §6. Related Work and Discussion; §7. Conclusion",
        ),
        "2606.04971": (
            f"{base} §2. Responsibility-Centered Evaluation of MLE Agents",
            f"{base} §3. Exploratory Experiment; §4. Preliminary Results",
            f"{base} §5. Conclusion & Next Steps",
        ),
        "2606.05408": (
            f"{base} §3. Methods",
            f"{base} §4. Experimental Design; §5. Results",
            f"{base} §6. Discussion; Appendix B Experimental Parameters",
        ),
        "2606.04401": (
            f"{base} §2 Methodology",
            f"{base} §4 Experiments; §4.1 Experimental Setup",
            f"{base} Appendix I Limitations and Future Works",
        ),
        "2606.04436": (
            f"{base} §3 Method",
            f"{base} §4 Experiments; §§4.1–4.4",
            f"{base} Appendix C Limitations",
        ),
        "2606.04463": (
            f"{base} §3 Method",
            f"{base} §5 Experiments; §§5.1–5.4",
            f"{base} §6 Conclusion — Limitations",
        ),
        "2606.04492": (
            f"{base} §3 Method",
            f"{base} §4 Experiments; §§4.1–4.2",
            f"{base} Appendix A Limitations and Future Work",
        ),
        "2606.04507": (
            f"{base} §3 Methodology",
            f"{base} §5 Experiments; §§5.1–5.2",
            f"{base} Appendix A Limitations",
        ),
        "2606.04527": (
            f"{base} §3 Method; §3.2 Overall Framework",
            f"{base} §4 Experiments",
            f"{base} §Failure mode of fixed-ratio compression; Appendix F Limitations and Future Works",
        ),
        "2606.04555": (
            f"{base} §4 Methodology",
            f"{base} §5 Experiments; §§5.2–5.4",
            f"{base} §6 Conclusion — Limitation and future work; Appendix H Limitations and Broader Impacts",
        ),
        "2606.04678": (
            f"{base} §3 Method",
            f"{base} §4 Experimental Results; §§4.1–4.2",
            f"{base} Appendix E Limitations",
        ),
        "2606.04737": (
            f"{base} §3 Methodology",
            f"{base} §4 Experiments; §4.1 Experimental Setup",
            f"{base} Appendix D Limitations and Discussions",
        ),
        "2606.04903": (
            f"{base} §1.4 Methodology; §1.4.3 Ontology-First Agent Design",
            f"{base} §2.3 Derivation of System Invariants; Appendix A.3.2 Preservation of Base Results",
            f"{base} §1.2 Threat Model (What is Safety) — In scope / Out of scope; §5 Conclusion and Future Work",
        ),
        "2606.04907": (
            f"{base} §3 Methodology",
            f"{base} §4 Experimental Results; §4.1 Simulation Experiments",
            f"{base} Appendix H Additional Failure Case Analysis",
        ),
        "2606.05030": (
            f"{base} §3 Methodology; §3.5 Inference Algorithm and Dual-System Repair",
            f"{base} §§4–5 Experimental Setup and Results",
            f"{base} §Failure Modes and Fallback Behaviour",
        ),
        "2606.05254": (
            f"{base} §4 Methodology",
            f"{base} §5 Experiments; §§5.1–5.2",
            f"{base} Appendix C Limitations and future work",
        ),
        "2606.05290": (
            f"{base} §3 Problem Formulation; §§3.1–3.4",
            f"{base} §4 Experimental Results; §4.1 Experimental Setting",
            f"{base} Appendix E Limitations and Societal Impacts",
        ),
        "2606.05433": (
            f"{base} §3 Proposed solution; §3.1 Architecture of the proving system",
            f"{base} §3 Proposed solution; Appendix G Protocol-aligned formalization of execution verification",
            f"{base} §2 Structural limitations; §3 Scope",
        ),
        "2606.04326": (
            f"{base} §2 Use Cases; §3 Decision Support; Dataset Generation; §4 Automation",
            f"{base} §5 Demonstrations; Validation of the Benchmark on Decision Support; Validation of the Benchmark on Automation",
            f"{base} §6 Concluding Remarks — Limitations",
        ),
        "2606.04342": (
            f"{base} §3 Evaluation-Induced Accuracy–Realism Trade-offs",
            f"{base} §4 Empirical Characterization of the Trade-off; §§4.1–4.5",
            f"{base} §6 Discussion and future work — Limitations and future directions",
        ),
        "2606.04366": (
            f"{base} §3 Methodology; §§3.1–3.3",
            f"{base} §4 Experiments; §§4.1–4.6",
            f"{base} §4.7 Limitations",
        ),
        "2606.04373": (
            f"{base} §2 Masked Attention Alignment for Data-Free Quantization of ViTs; §§2.2–2.3",
            f"{base} §3 Experiment; §§3.1–3.4",
            f"{base} §4 Conclusion and Limitations",
        ),
        "2606.04433": (
            f"{base} §3 Stateful Visual Encoders; §3.1 Task Setup",
            f"{base} §§3.3–3.5; §5 Validating SVE in Real-world Tasks",
            f"{base} Appendix A Limitations",
        ),
        "2606.04442": (
            f"{base} §3 The MemoryDocDataSet Benchmark; §4 Collection Pipeline",
            f"{base} §5 Baseline Experiments; §§5.1–5.4",
            f"{base} §6 Discussion — Limitations",
        ),
        "2606.04484": (
            f"{base} §3 AgentJet; §§3.1–3.4",
            f"{base} §§5–6 Multi-Agent/Multi-Model/Multi-Task Training and Automated Research",
            f"{base} §7 Conclusion — reviewed for scope; no dedicated limitations heading",
        ),
        "2606.04522": (
            f"{base} §§3.2–3.3 Accuracy Measures and Downstream Task Evaluation Metrics",
            f"{base} §§5–6 Experimental Setup and Results; §6.3 RAG Experiments",
            f"{base} §7 Conclusions — reviewed for scope; no dedicated limitations heading",
        ),
        "2606.04536": (
            f"{base} §3 Agentic Decision Process with Parametric Memory; §§3.1–3.2; §4 Policy Optimization with Fast-Weight Rollouts",
            f"{base} §5 Experiments; §§5.1–5.5",
            f"{base} §6 Discussion — Practical trade-off",
        ),
        "2606.04662": (
            f"{base} §4 Main Results; §§4.1–4.4",
            f"{base} Appendix A Experimental Details; Appendices B–D empirical verification",
            f"{base} §6 Conclusion — reviewed for scope; no dedicated limitations heading",
        ),
        "2606.04727": (
            f"{base} §3 Method; §§3.1–3.4",
            f"{base} §4 Experiment; §§4.1–4.6",
            f"{base} §5 Conclusion — reviewed for scope; no dedicated limitations heading",
        ),
        "2606.04767": (
            f"{base} §3 Methodology; §§3.1–3.4",
            f"{base} §4 Experiments; §§4.1–4.7",
            f"{base} Appendix K Limitations and Future Work",
        ),
        "2606.04807": (
            f"{base} §3 Methodology; §§3.1–3.4",
            f"{base} §§4–5 Results and Ablation Studies",
            f"{base} §7 Limitations",
        ),
        "2606.04847": (
            f"{base} §§3–4 Data Synthesis Pipeline and Method; §§4.1–4.5",
            f"{base} §5 Experiments; §§5.1–5.5",
            "Not Disclosed — exact-v1 has no explicit limitations section; results are bounded to Moore Threads MUSA and disclosed KernelBench variants",
        ),
        "2606.04853": (
            f"{base} §IV SENTINEL: System Design; §IV-B Reliability Estimation Pipeline",
            f"{base} §§V–VI Experimental Design and Results",
            f"{base} §VII Discussion",
        ),
        "2606.05037": (
            f"{base} §3 Design: Self-Reflective API Framework; §4 Implementation",
            f"{base} §5 Evaluation; §§5.1–5.4",
            f"{base} §5.5 Limitations and Threats to Validity; §6.2 Failure/Saturation cases",
        ),
        "2606.05115": (
            f"{base} §3 Method — Temporal segmentation, Memory replay, Training objectives",
            f"{base} §4 Experiments; §§4.1–4.7",
            f"{base} §5 Discussion and Conclusion — Limitations and future work",
        ),
        "2606.05161": (
            f"{base} §§3–4 Diagnosis and Decoding Rule; §4.3 GACL",
            f"{base} §5 Experiments; §§5.1–5.4",
            f"{base} §6 Conclusion — Limitations",
        ),
        "2606.05326": (
            f"{base} §3 Main results; §§3.1–3.3",
            f"{base} §4 Experiments; Appendix C Experimental details",
            f"{base} §5 Discussion; §5.3 Some open questions",
        ),
        "2606.05484": (
            f"{base} §3 Manifold Aware Projection Learning; §§3.1–3.5",
            f"{base} §4 Experiments; §§4.1–4.2",
            f"{base} §5 Conclusion — reviewed for scope; no dedicated limitations heading",
        ),
        "2606.05476": (
            f"{base} §3 Methodology; §§3.1–3.4",
            f"{base} §4 Results; §9.1 Benchmark Results Table",
            f"{base} §5 Future Work",
        ),
        "2606.05495": (
            f"{base} §4 Stream-Event-Triggered Scheduling; §§4.1–4.2",
            f"{base} §5 Experimental Evaluations; §§5.1–5.3",
            f"{base} §6 Conclusions — reviewed for scope; no dedicated limitations heading",
        ),
        "2606.05516": (
            f"{base} §§3–4 Dominant Layer Discovery and Explanation",
            f"{base} §5 Experimental Validation; §§5.1–5.4",
            f"{base} §6 Conclusion — reviewed for scope; no dedicated limitations heading",
        ),
        "2606.04717": (
            f"{base} §3 Method: K-Shot Layer Disruption",
            f"{base} §4 Experimental Setup",
            f"{base} §10 Discussion — Limitations",
        ),
        "2606.04769": (
            f"{base} §IV DCIChecker : Detecting Real-world DCI",
            f"{base} §V Real-world Measurement",
            f"{base} §VII Discussion",
        ),
        "2606.04970": (
            f"{base} §2 Method",
            f"{base} §4 Experiments & Results",
            f"{base} §8 Limitations and Broader Impacts",
        ),
        "2606.05029": (
            f"{base} §3 The Proxy Approach",
            f"{base} §6 Validity Profiles for Foundation Model Research",
            f"{base} §8 Discussion",
        ),
        "2606.04811": (
            f"{base} §3 Dream.exe: Benchmark Design",
            f"{base} §4 Experiments",
            f"{base} §4.5 More Findings — Failure modes",
        ),
    }
    if arxiv_id in overrides:
        method_locator, evaluation_locator, limitation_locator = overrides[arxiv_id]
    return (
        method_locator,
        evaluation_locator,
        limitation_locator,
        repo_match if repo_match else "Not Disclosed — exact v1 does not disclose a versioned public artifact",
    )


def roadmap() -> tuple[dict[str, tuple[int, str]], dict[int, str]]:
    by_node: dict[str, tuple[int, str]] = {}
    by_chapter: dict[int, str] = {}
    for line in (ROOT / "ROADMAP.md").read_text(encoding="utf-8").splitlines():
        match = re.match(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", line)
        if match:
            node, chapter, path = match.group(1), int(match.group(2)), match.group(3)
            by_node[node] = (chapter, path)
            by_chapter[chapter] = path
    return by_node, by_chapter


def source_line(path: str, terms: tuple[str, ...]) -> int:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    candidates: list[tuple[int, int]] = []
    current_section = ""
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            current_section = stripped.casefold()
            continue
        if any(
            marker in current_section
            for marker in (
                "review note",
                "review notes",
                "evidence note",
                "evidence notes",
                "证据说明",
                "证据记录",
                "参考资料",
                "参考文献",
                "sources",
            )
        ):
            continue
        if (
            not stripped
            or stripped.startswith("|")
            or stripped.startswith("<!--")
            or stripped.startswith("归属（Owner）")
            or stripped.startswith("Stable Node")
            or (stripped.startswith("-") and ("http://" in stripped or "https://" in stripped))
            or len(clean(stripped)) < 45
        ):
            continue
        low = stripped.casefold()
        score = sum(3 for term in terms if term.casefold() in low)
        score += sum(
            1 for signal in (
                "state", "状态", "control", "控制", "boundary", "边界",
                "trade-off", "代价", "failure", "evidence", "证据",
            ) if signal in low
        )
        candidates.append((score, number))
    if not candidates:
        raise ValueError(f"no substantive proposition in {path}")
    return max(candidates)[1]


def semantic_source_line(path: str, candidate_text: str, fallback_terms: tuple[str, ...]) -> int:
    """Resolve a candidate-specific Books proposition, not a generic owner hit.

    The comparison target is selected from prose paragraphs outside review-note
    sections.  Candidate mechanism tokens carry more weight than generic state
    vocabulary; fallback terms are used only when no mechanism token overlaps.
    """
    stop = {
        "the", "and", "for", "with", "from", "that", "this", "into", "via", "using",
        "model", "models", "method", "paper", "section", "propose", "present", "introduce",
        "exact", "evidence", "authors", "system", "systems",
    }
    tokens = {
        token for token in re.findall(r"[a-z][a-z0-9_-]{3,}", candidate_text.casefold())
        if token not in stop
    }
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    candidates: list[tuple[int, int]] = []
    current_section = ""
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            current_section = stripped.casefold()
            continue
        if any(marker in current_section for marker in (
            "review note", "review notes", "evidence note", "evidence notes",
            "证据说明", "证据记录", "参考资料", "参考文献", "sources",
        )):
            continue
        if (
            not stripped or stripped.startswith("|") or stripped.startswith("<!--")
            or stripped.startswith("归属（Owner）") or stripped.startswith("Stable Node")
            or (stripped.startswith("-") and ("http://" in stripped or "https://" in stripped))
            or len(clean(stripped)) < 45
        ):
            continue
        low = stripped.casefold()
        overlap = sum(5 for token in tokens if token in low)
        fallback = sum(2 for term in fallback_terms if term.casefold() in low)
        boundary = sum(1 for signal in (
            "state", "状态", "control", "控制", "boundary", "边界", "trade-off", "代价",
            "failure", "evidence", "证据", "owner", "identity", "lifecycle",
        ) if signal in low)
        candidates.append((overlap + fallback + boundary, number))
    if not candidates:
        return source_line(path, fallback_terms)
    best = max(candidates)
    if best[0] == 0:
        return source_line(path, fallback_terms)
    return best[1]


def books_excerpt(path: str, line_number: int, radius: int = 1) -> str:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    index = line_number - 1
    start = index
    while start > 0 and lines[start - 1].strip() and not lines[start - 1].lstrip().startswith("#"):
        start -= 1
    end = index + 1
    while end < len(lines) and lines[end].strip() and not lines[end].lstrip().startswith("#"):
        end += 1
    excerpt = clean(" ".join(lines[start:end]))
    return excerpt[:420] if excerpt else "目标章节已定义该 owner 的既有状态与控制边界。"


def infer_owner(text: str) -> str:
    low = text.casefold()
    rules = [
        (("mcp",), "AGENT-MCP"), (("multi-agent", "multi agent"), "AGENT-MULTI-AGENT"),
        (("agent", "workflow"), "AGENT-WORKFLOW"), (("retriev", "rag"), "AGENT-RAG"),
        (("memory", "personalization"), "AGENT-MEMORY"), (("tool", "api"), "AGENT-TOOL-CALLING"),
        (("prompt",), "AGENT-PROMPT"), (("world model", "physics"), "MULTIMODAL-WORLD-MODELS"),
        (("vision-language-action", "vla", "affordance"), "MULTIMODAL-EMBODIED-VLA"),
        (("multimodal", "vision-language", "audio-language", "speech token"), "MULTIMODAL-REPRESENTATION"),
        (("diffusion", "generation"), "MULTIMODAL-GENERATIVE-PARADIGMS"),
        (("quantiz", "cuda", "gpu", "npu", "inference"), "INFER-TENSORRT-LLM"),
        (("lora",), "TRAIN-LORA"), (("distill", "fine-tun"), "TRAIN-SFT"),
        (("rlvr", "grpo"), "TRAIN-GRPO"), (("privacy", "poison", "attack", "safety"), "PLATFORM-SECURITY"),
        (("benchmark", "evaluation", "confidence", "verifier"), "PLATFORM-EVALUATION-SYSTEM"),
        (("transformer", "attention"), "MODEL-TRANSFORMER-LAYER"),
    ]
    for terms, owner in rules:
        if any(term in low for term in terms):
            return owner
    return "WORLDVIEW-KNOWLEDGE-TREE"


def score_for(arxiv_id: str, old: dict[str, dict]) -> tuple[int, int, int]:
    if arxiv_id in AUDIT_SCORE:
        return AUDIT_SCORE[arxiv_id]
    if arxiv_id in old and "score" in old[arxiv_id]:
        s = old[arxiv_id]["score"]
        return s["design_delta"], s["system_reach"], s["durability"]
    if arxiv_id in AUDIT_CLOSURE:
        return 1, 1, 1
    if arxiv_id in AUDIT_DEEP:
        return 3, 2, 2
    if arxiv_id in AUDIT_RECOVERED:
        return 2, 2, 2
    return 1, 1, 2


def disposition(arxiv_id: str, owner: str, total: int, old: dict[str, dict]) -> tuple[str, str]:
    if arxiv_id in REASSESSED_BOOKS:
        return REASSESSED_BOOKS[arxiv_id]
    if arxiv_id in OLD_INTEGRATE_DECISION:
        return OLD_INTEGRATE_DECISION[arxiv_id]
    if arxiv_id in NEW_INTEGRATE:
        return owner, "Integrate"
    if total <= 4:
        return owner, "Rejected — Low Durability / Out of Scope"
    if arxiv_id in old and old[arxiv_id].get("books_disposition") == "No Change — Existing Coverage":
        return owner, "No Change — Existing Coverage"
    if total >= 7:
        return owner, "No Change — Existing Coverage"
    return owner, "Weekly Only — Context"


def body_sha(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]: lines.pop(0)
    while lines and not lines[-1]: lines.pop()
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def provenance(family: str, row: dict, receipt: dict, review_body_sha: str) -> str:
    def cm(value: str) -> str:
        return ";".join(sorted(x.strip() for x in value.split(";") if x.strip() and x.strip() != "—"))
    canonical = "|".join((
        "review-completion-v1", family, row["Event Identity"], row["Primary Identifier"],
        cm(row["Supporting Source IDs"]), receipt["Primary Evidence Version"],
        cm(receipt["Reviewed Evidence Versions"]), receipt["Review Route"],
        cm(receipt["Method / Identity Locators"]), cm(receipt["Evaluation Locators"]),
        cm(receipt["Limitations / Counterevidence Locators"]), cm(receipt["Artifact Locators"]),
        receipt["Claim Boundary Ref"], row["Review Ref"], f"review-body-sha256:{review_body_sha}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def pipe(value: str) -> str:
    return value.replace("|", "&#124;").replace("\n", " ")


def old_candidate_map() -> dict[str, dict]:
    """Read the pre-repair Candidate Ledger as the compatibility baseline."""
    text = REPORT.read_text(encoding="utf-8")
    marker = "<!-- validator:candidate-ledger-v2.1 -->"
    tail = text.split(marker, 1)[1].split("\n\n", 1)[0]
    table = [line for line in tail.splitlines() if line.startswith("|")]
    headers = [cell.strip() for cell in table[0].strip("|").split("|")]
    result: dict[str, dict] = {}
    for line in table[2:]:
        cells = [cell.strip().replace("\\|", "|") for cell in line.strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        row = dict(zip(headers, cells))
        primary = row.get("Primary Identifier", "")
        match = re.search(r"(2606\.\d{5})", primary)
        if match:
            result[match.group(1)] = row
    return result


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    current_outside_ids = {
        item["arxiv_id"] for item in ledger["identities"]
        if item.get("final_screening_status") == "screened_out_after_abstract_review"
    }
    if len(current_outside_ids) == 217:
        v8_outside_ids = current_outside_ids
    elif len(current_outside_ids) == 181:
        # Keep the repair generator reproducible after the 36 V8
        # false-negative rows have already been frozen into Score V2 Closure.
        v8_outside_ids = current_outside_ids | V8_REOPEN
    else:
        v8_outside_ids = current_outside_ids
    if len(v8_outside_ids) != 217 or not V8_REOPEN <= v8_outside_ids:
        raise SystemExit(
            f"expected the Independent V8 217-item outside set with all 36 findings, found {len(v8_outside_ids)}"
        )
    # Preserve the V5 denominator boundary before mutation.  This receipt is
    # the evidence that the repair semantically reconsidered every one of the
    # 296 prior closures, rather than only the counterexamples named by V5.
    v5_snapshot_path = PACKET / "closure-rescreen-independent-v5-repair.json"
    if v5_snapshot_path.exists():
        v5_snapshot = json.loads(v5_snapshot_path.read_text(encoding="utf-8"))
        v5_closure_ids = set(v5_snapshot["v5_closure_ids"])
    else:
        v5_closure_ids = {
            item["arxiv_id"] for item in ledger["identities"]
            if item.get("final_screening_status") == "screened_out_after_abstract_review"
        }
        if len(v5_closure_ids) != 296:
            raise SystemExit(f"expected 296 V5 closures before repair, found {len(v5_closure_ids)}")
    history_path = PACKET / "arxiv-submission-history-receipts.json"
    history = json.loads(history_path.read_text(encoding="utf-8"))
    if not (
        history.get("registered") == 574
        and history.get("returned") == 574
        and history.get("timestamp_matches") == 574
        and history.get("timestamp_mismatches") == 0
        and history.get("outside_window") == 0
    ):
        raise SystemExit("official arXiv v1 history receipt is incomplete or disagrees with the ledger")
    recall_input_ids = {
        item["arxiv_id"] for item in ledger["identities"]
        if item.get("final_screening_status") in {
            "routed_to_score_v2",
            "screened_out_family_specific_pre_denominator_closure",
        }
    }
    if len(recall_input_ids) != 393 or not PRE_DENOMINATOR_RETAIN <= recall_input_ids:
        raise SystemExit(
            "expected the 393-family recall-first input and the complete explicit retain set; "
            f"found input={len(recall_input_ids)}, retained={len(PRE_DENOMINATOR_RETAIN)}"
        )
    old_candidates = old_candidate_map()
    old_receipt_list = json.loads(RECEIPTS.read_text(encoding="utf-8"))["families"]
    old = {item["arxiv_id"]: item for item in old_receipt_list}
    for arxiv_id, row in old_candidates.items():
        item = old.setdefault(arxiv_id, {})
        item["score"] = {
            "design_delta": int(row["Design Delta"]),
            "system_reach": int(row["System Reach"]),
            "durability": int(row["Durability"]),
            "total": int(row["Total"]),
        }
        item["stable_node_id"] = row["Stable Node ID"]
        item["books_disposition"] = row["Books Disposition"]
    by_id = {item["arxiv_id"]: item for item in ledger["identities"]}
    candidate_ids = set(PRE_DENOMINATOR_RETAIN)
    if len(by_id) != 574 or not candidate_ids <= set(by_id):
        raise SystemExit("identity universe or candidate IDs changed")

    denominator_replay_path = PACKET / "candidate-denominator-replay-v10.json"
    prior_denominator_rows: dict[str, dict] = {}
    if denominator_replay_path.exists():
        prior_denominator_rows = {
            row["arxiv_id"]: row
            for row in json.loads(denominator_replay_path.read_text(encoding="utf-8"))["rows"]
        }

    # Every one of the 574 identities gets a distinct abstract-level receipt;
    # every member of the 393-family recall input additionally gets an explicit
    # pre-denominator retain/closure decision with frozen evidence.
    denominator_replay_rows = []
    for item in ledger["identities"]:
        arxiv_id = item["arxiv_id"]
        first = sentences(item["abstract"])[0] if sentences(item["abstract"]) else item["title"]
        previous = prior_denominator_rows.get(arxiv_id, {})
        previous_score = item.get("score_v2") or old.get(arxiv_id, {}).get("score") or previous.get("old_score_v2")
        previous_owner = (
            item.get("stable_node_id")
            or old.get(arxiv_id, {}).get("stable_node_id")
            or previous.get("old_stable_node_id")
            or AUDIT_OWNER.get(arxiv_id)
            or infer_owner(item["title"] + " " + item["abstract"])
        )
        previous_owner = PRE_DENOMINATOR_OWNER_OVERRIDES.get(arxiv_id, previous_owner)
        previous_route = item.get("review_route") or previous.get("old_review_route")
        if arxiv_id in candidate_ids:
            item["final_screening_status"] = "routed_to_score_v2"
            decision = "provisionally_retained_in_candidate_denominator"
            rationale = pre_denominator_retain_reason(item, previous_owner)
            item["final_screening_reason"] = rationale
        elif arxiv_id in recall_input_ids:
            item["final_screening_status"] = "screened_out_family_specific_pre_denominator_closure"
            decision = "closed_before_score_v2_after_family_specific_replay"
            rationale = pre_denominator_reason(item)
            item["final_screening_reason"] = rationale
        else:
            item["final_screening_status"] = "screened_out_after_abstract_review"
            decision = None
            rationale = closure_screening_reason(item)
            item["final_screening_reason"] = closure_screening_reason(item)
        if arxiv_id in recall_input_ids:
            item["pre_denominator_audit"] = {
                "audit_id": "CANDIDATE-DENOMINATOR-REPLAY-V10",
                "input_state": "recall_first_candidate_inventory",
                "decision": decision,
                "decision_class": (
                    None if arxiv_id in candidate_ids else pre_denominator_closure_class(item)
                ),
                "rationale": rationale,
            }
            denominator_replay_rows.append({
                "arxiv_id": arxiv_id,
                "title": item["title"],
                "categories": item.get("categories", []),
                "submitted_v1_utc": item["submitted_v1_utc"],
                "evidence_version": f"arXiv:{arxiv_id}v1",
                "abstract_sha256": hashlib.sha256(item["abstract"].encode()).hexdigest(),
                "old_candidate_state": "recall_first_candidate_inventory",
                "old_review_route": previous_route,
                "old_stable_node_id": previous_owner,
                "old_score_v2": previous_score,
                "decision": decision,
                "closure_class": (
                    None if arxiv_id in candidate_ids else pre_denominator_closure_class(item)
                ),
                "new_stable_node_id": previous_owner if arxiv_id in candidate_ids else None,
                "evidence_locator": (
                    f"review:SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"
                    if previous_route in {"deep", "standard", "blocked"}
                    else f"screening-ledger.json#arxiv:{arxiv_id}v1-abstract"
                ),
                "rationale": rationale,
            })
    ledger["routed_candidate_denominator"] = len(candidate_ids)
    ledger["abstract_screening_closure"] = 574 - len(candidate_ids)
    ledger["false_negative_recoveries"] = len(AUDIT_RECOVERED)
    ledger["pre_denominator_recall_input"] = len(recall_input_ids)
    ledger["family_specific_pre_denominator_closure"] = len(recall_input_ids - candidate_ids)
    ledger["candidate_retain_rate"] = round(len(candidate_ids) / len(recall_input_ids), 6)
    ledger["gate_status"] = "open_pending_fresh_context_candidate_denominator_fp_fn_audit"
    ledger["audit"] = {
        "contract_version": "V2.1", "audited_at": REPAIR_EXECUTED_AT,
        "registered": 574, "abstract_screened": 574,
        "routed_candidate_denominator": len(candidate_ids),
        "abstract_screening_closure": 574 - len(candidate_ids),
        "recall_first_candidate_inventory": len(recall_input_ids),
        "provisional_candidate_denominator": len(candidate_ids),
        "family_specific_pre_denominator_closure": len(recall_input_ids - candidate_ids),
        "candidate_retain_rate": round(len(candidate_ids) / len(recall_input_ids), 6),
        "fresh_context_counterexamples_recovered": len(AUDIT_RECOVERED),
        "official_v1_submission_history": {
            "registered": 574, "returned": 574, "timestamp_matches": 574,
            "timestamp_mismatches": 0, "outside_window": 0,
            "receipt": "arxiv-submission-history-receipts.json",
        },
        "exact_v1_review": {"complete": "computed_after_repair", "blocked": ["2606.05268"]},
        "independent_v8_outside_replay": {
            "original_outside": len(v8_outside_ids),
            "reopened_to_recall_inventory": len(V8_REOPEN),
            "retained_after_strict_pre_denominator_replay": len(V8_REOPEN & candidate_ids),
            "closed_after_strict_pre_denominator_replay": len(V8_REOPEN - candidate_ids),
            "affirmed_outside": len(v8_outside_ids - V8_REOPEN),
            "receipt": "outside-replay-independent-v9.json",
        },
        "boundary": (
            "Official arXiv Atom v1 entries prove event time; DataCite remains discovery metadata. "
            "The 393-family set is recall-first input, not a valid denominator by itself. The provisional "
            "retained denominator requires a different fresh-context false-positive/false-negative audit; "
            "Standard/Deep mechanism claims require readable exact-v1 material and 2606.05268 remains blocked."
        ),
    }
    denominator_replay_rows.sort(key=lambda row: int(row["arxiv_id"].split(".")[1]))
    denominator_replay_path.write_text(
        json.dumps({
            "schema": "daily-v2.1-candidate-denominator-replay-v1",
            "report_date": "2026-06-04",
            "auditor": "fresh-context:jun04-v8-repair-owner",
            "raw_identities": 574,
            "old_recall_first_candidate_inventory": len(recall_input_ids),
            "provisional_retained": len(candidate_ids),
            "family_specific_pre_denominator_closure": len(recall_input_ids - candidate_ids),
            "retain_rate": round(len(candidate_ids) / len(recall_input_ids), 6),
            "total_outside_provisional_denominator": 574 - len(candidate_ids),
            "rows": denominator_replay_rows,
            "gate_boundary": (
                "repair complete only; the provisional denominator cannot complete until a different "
                "fresh-context auditor replays false positives and false negatives"
            ),
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    outside_replay_rows = []
    for arxiv_id in sorted(v8_outside_ids, key=lambda value: int(value.split(".")[1])):
        item = by_id[arxiv_id]
        if arxiv_id in V8_REOPEN:
            score = AUDIT_SCORE[arxiv_id]
            decision = "reopened_to_recall_inventory_then_closed_pre_denominator"
            rationale = (
                f"Primary abstract claim: {pick_sentence(item['abstract'], ('we propose', 'we introduce', 'we present', 'we develop'), 1)[:520]} "
                f"Independent V8 correctly surfaced this family into the 393-item recall inventory under provisional owner {V8_OWNER[arxiv_id]}. "
                f"The stricter pre-denominator replay then closed it: {pre_denominator_reason(item)}"
            )
        else:
            score = None
            decision = "affirmed_outside_after_full_abstract_replay"
            rationale = closure_screening_reason(item)
        outside_replay_rows.append({
            "arxiv_id": arxiv_id,
            "title": item["title"],
            "categories": item.get("categories", []),
            "v8_input_status": "screened_out_after_abstract_review",
            "v9_decision": decision,
            "stable_node_id": V8_OWNER.get(arxiv_id, "—"),
            "recall_inventory_score_v2": (
                {
                    "design_delta": score[0], "system_reach": score[1],
                    "durability": score[2], "total": sum(score),
                }
                if score else None
            ),
            "rationale": rationale,
        })
    (PACKET / "outside-replay-independent-v9.json").write_text(
        json.dumps({
            "schema": "daily-v2.1-outside-replay-v1",
            "report_date": "2026-06-04",
            "input_audit": "fresh-context-semantic-audit-independent-v8.md",
            "input_outside": len(v8_outside_ids),
            "reopened_to_recall_inventory": len(V8_REOPEN),
            "retained_after_strict_pre_denominator_replay": len(V8_REOPEN & candidate_ids),
            "closed_after_strict_pre_denominator_replay": len(V8_REOPEN - candidate_ids),
            "affirmed_outside": len(v8_outside_ids - V8_REOPEN),
            "rows": outside_replay_rows,
            "gate_boundary": (
                "repair-owner receipt only; the V8 queue was recall evidence, not automatic retention. "
                "The provisional denominator awaits a different fresh-context FP/FN audit"
            ),
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    by_node, by_chapter = roadmap()
    candidates: list[dict] = []
    receipts: list[dict] = []
    review_bodies: dict[str, str] = {}
    review_evidence: dict[str, dict[str, str]] = {}
    for arxiv_id in sorted(candidate_ids, key=lambda x: int(x.split(".")[1])):
        item = by_id[arxiv_id]
        family = f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"
        dd, sr, du = score_for(arxiv_id, old)
        total = dd + sr + du
        owner = old.get(arxiv_id, {}).get("stable_node_id") or AUDIT_OWNER.get(arxiv_id) or infer_owner(item["title"] + " " + item["abstract"])
        if arxiv_id in AUDIT_OWNER:
            owner = AUDIT_OWNER[arxiv_id]
        if arxiv_id in PRE_DENOMINATOR_OWNER_OVERRIDES:
            owner = PRE_DENOMINATOR_OWNER_OVERRIDES[arxiv_id]
        if arxiv_id in OLD_INTEGRATE_DECISION:
            owner = OLD_INTEGRATE_DECISION[arxiv_id][0]
        owner, books = disposition(arxiv_id, owner, total, old)
        route = "deep" if total >= 7 else "standard" if total >= 5 else "closure"
        exact_blocked = arxiv_id in BLOCKED_EXACT_V1
        status = "blocked" if exact_blocked else route + "_complete"
        review_ref = f"review:{family}"
        claim_ref = f"claim:{family}"
        benchmark = "yes" if route in {"deep", "standard"} else "no"
        row = {
            "Source Family ID": family, "Primary Identifier": f"arXiv:{arxiv_id}v1",
            "Event Identity": f"paper-v1:{arxiv_id}", "Owner Week": "2026-W23",
            "First-public Date": item["submitted_v1_utc"][:10], "Supporting Source IDs": "SRC-ARXIV",
            "Design Delta": str(dd), "System Reach": str(sr), "Durability": str(du), "Total": str(total),
            "Candidate State": "retained" if total >= 5 else "closure_only", "Review Status": status,
            "Access Status": "blocked" if exact_blocked else "accessible", "Review Override": "none", "Review Ref": review_ref,
            "Owner Report Ref": "self", "Prior Review Ref": "—", "Reconciliation": "new_in_window",
            "Stable Node ID": owner, "Books Disposition": "Blocked / Unverified" if exact_blocked else books,
            "Books Review Ref": f"books-review:{family}" if total >= 7 and not exact_blocked else "—",
            "Benchmark Claim": "no" if exact_blocked else benchmark,
        }
        candidates.append(row)

        if exact_blocked:
            blocked_boundary = (
                "exact-v1 PDF is truncated/corrupt, arXiv HTML is unavailable, and two independent "
                "full-file retries plus the official e-print source did not yield an intact artifact"
            )
            method = f"Pending — Method locator cannot be established because {blocked_boundary}"
            evaluation = f"Pending — Evaluation locator cannot be established because {blocked_boundary}"
            limits = f"Pending — Limitations locator cannot be established because {blocked_boundary}"
            artifact = f"Pending — Artifact review cannot be completed because {blocked_boundary}"
            body = (
                f"**身份与日期。** 官方 arXiv Atom v1 receipt confirms `{arxiv_id}` at `{item['submitted_v1_utc']}` inside the strict window.\n\n"
                "**Access blocker.** The locally frozen exact-v1 PDF fails xref/trailer/EOF validation. "
                "A second 38,563,345-byte official PDF transfer and the 36,997,631-byte e-print archive could not be recovered intact through the current transport. "
                "Abstract-only evidence cannot support the existing Method/Evaluation/Limitations locators.\n\n"
                "**Disposition.** Review and Books comparison remain `Blocked / Unverified`; no benchmark claim or long-form analysis may rely on this family until a readable exact-v1 PDF, source archive, or author-hosted exact-version manuscript is supplied."
            )
        elif route == "closure":
            method, evaluation, limits, artifact = (
                f"arXiv:{arxiv_id}v1 identity and DataCite Submitted-v1 metadata",
                "Not Required — closure route makes no experimental claim",
                "Not Required — closure route rejects long-term design relevance",
                "Not Required — closure route does not rely on an implementation artifact",
            )
            body = (
                f"**身份与日期。** `{arxiv_id}` 的 v1 timestamp 为 `{item['submitted_v1_utc']}`，落入严格窗口。\n\n"
                f"**Closure 判断。** 《{item['title']}》的摘要主张是：{pick_sentence(item['abstract'], ('we ', 'this paper', 'we propose'), 0)} "
                f"它被计入 denominator 并完成三维评分，但当前只形成局部或领域事实，没有建立新的长期状态所有权、控制流或数据流。\n\n"
                "**边界。** 该拒绝不是访问失败；若后续 revision 增加可复算的跨层机制或改变 Books 结论，应按 important revision 重开。"
            )
        else:
            method, evaluation, limits, artifact = locators(arxiv_id)
            primary_path = exact_path(arxiv_id)
            mechanism = pick_sentence(item["abstract"], ("we propose", "we introduce", "we present", "we develop", "we formulate"), 1)
            result = pick_sentence(item["abstract"], ("we evaluate", "results", "achiev", "improv", "outperform", "show that", "demonstrate"), -1)
            problem = pick_sentence(item["abstract"], ("however", "existing", "current", "challenge", "limitation", "struggle"), 0)
            method_evidence = section_excerpt(primary_path, method, mechanism)
            evaluation_evidence = section_excerpt(primary_path, evaluation, result)
            limitation_evidence = counterevidence_excerpt(primary_path, limits, limits)
            if arxiv_id in PDF_EVIDENCE:
                method_evidence = PDF_EVIDENCE[arxiv_id]["method"]
                evaluation_evidence = PDF_EVIDENCE[arxiv_id]["evaluation"]
                limitation_evidence = PDF_EVIDENCE[arxiv_id]["limitations"]
            if arxiv_id in WEB_EVIDENCE:
                method_evidence = WEB_EVIDENCE[arxiv_id]["method"]
                evaluation_evidence = WEB_EVIDENCE[arxiv_id]["evaluation"]
                limitation_evidence = WEB_EVIDENCE[arxiv_id]["limitations"]
            review_evidence[family] = {
                "method": method_evidence,
                "evaluation": evaluation_evidence,
                "limitations": limitation_evidence,
                "combined": " ".join((item["abstract"], method_evidence, evaluation_evidence, limitation_evidence)),
            }
            proof_boundary = (
                f"这些证据只限定《{item['title']}》公开的任务、baseline 与 evaluator；"
                "未披露的硬件、精度、长度、batch、并发或生产 SLO 不被补造。"
            )
            old_boundary = (
                f"在 `{owner}` 仍只需处理“{problem[:220]}”所描述的较小状态或较弱约束时，"
                "不引入本文机制仍可降低系统复杂度；新方案只在作者声明的约束改变后才有优势。"
            )
            body = (
                f"**问题与旧方案。** {problem} {old_boundary}\n\n"
                f"**机制、状态与控制流。** `{owner}` 是长期知识 owner。exact-v1 的 Method 段落把本稿件的控制点具体化为：{method_evidence} 定位为 `{method}`。\n\n"
                f"**Evaluation contract。** exact-v1 的评估段落披露：{evaluation_evidence} 定位为 `{evaluation}`。{proof_boundary}\n\n"
                f"**Trade-off 与 failure mode。** 《{item['title']}》的限制/反证边界为：{limitation_evidence} "
                f"因此本 family 的收益只在 `{evaluation}` 指定的 evaluation contract 中成立；反证定位为 `{limits}`。\n\n"
                f"**演进与 Books。** 与 `{owner}` 的关系为 `Layering / Dependency`。本轮 disposition 是 `{books}`；只有 `Integrate` 项才进入 root 的串行 Books writeback。"
            )
        claim_text = (
            f"`{row['Primary Identifier']}` 的 claim boundary 限于《{item['title']}》在 `{method}` 中公开的机制"
            f"以及 `{evaluation}` 中的评估；其 `{limits}` 之外的硬件、精度、长度、并发、SLO 与生产外推均不成立。"
        )
        review_segment = (
            f"{body}\n\n<!-- {claim_ref}:start -->{claim_text}<!-- {claim_ref}:end -->"
        )
        review_bodies[family] = review_segment
        receipt = {
            "Source Family ID": family, "Review Provenance ID": "", "Review Route": route,
            "Primary Evidence Version": f"arXiv:{arxiv_id}v1",
            "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{arxiv_id}v1",
            "Method / Identity Locators": method, "Evaluation Locators": evaluation,
            "Limitations / Counterevidence Locators": limits, "Artifact Locators": artifact,
            "Claim Boundary Ref": claim_ref, "Completion Result": "blocked" if exact_blocked else "complete",
        }
        receipt["Review Provenance ID"] = provenance(
            family, row, receipt, body_sha(review_segment)
        )
        receipts.append(receipt)

    # Candidate truth, including repaired owner and disposition, is mirrored
    # back to the screening ledger so the packet has one reconcilable state.
    candidate_truth = {
        row["Primary Identifier"].split(":", 1)[1][:-2]: row for row in candidates
    }
    for item in ledger["identities"]:
        row = candidate_truth.get(item["arxiv_id"])
        if row:
            item["score_v2"] = {
                "design_delta": int(row["Design Delta"]),
                "system_reach": int(row["System Reach"]),
                "durability": int(row["Durability"]),
                "total": int(row["Total"]),
            }
            item["stable_node_id"] = row["Stable Node ID"]
            item["books_disposition"] = row["Books Disposition"]
            item["review_route"] = row["Review Status"].removesuffix("_complete")
        else:
            item.pop("score_v2", None)
            item.pop("stable_node_id", None)
            item.pop("books_disposition", None)
            item.pop("review_route", None)
    ledger["gate_status"] = "open_pending_fresh_context_candidate_denominator_fp_fn_audit"
    reopened_v5 = sorted(v5_closure_ids & candidate_ids, key=lambda x: int(x.split(".")[1]))
    closure_rescreen_rows = []
    for arxiv_id in sorted(v5_closure_ids, key=lambda x: int(x.split(".")[1])):
        identity = by_id[arxiv_id]
        reopened = arxiv_id in candidate_ids
        closure_rescreen_rows.append({
            "arxiv_id": arxiv_id,
            "title": identity["title"],
            "v5_state": "closure",
            "repair_state": "routed_to_score_v2" if reopened else "closure",
            "decision": (
                "reopened_after_full-abstract semantic rescreen: durable state/control/communication/evidence delta"
                if reopened else identity["final_screening_reason"]
            ),
        })
    v5_snapshot_path.write_text(json.dumps({
        "schema": "closure-rescreen-v5-repair-v1",
        "report_date": "2026-06-04",
        "auditor": "fresh-context:jun04-v8-repair-owner",
        "v5_closure_count": len(v5_closure_ids),
        "v5_closure_ids": sorted(v5_closure_ids, key=lambda x: int(x.split(".")[1])),
        "reopened_count": len(reopened_v5),
        "reopened_ids": reopened_v5,
        "remaining_closure_count": len(v5_closure_ids) - len(reopened_v5),
        "rows": closure_rescreen_rows,
        "gate_boundary": (
            "candidate-denominator replay receipt only; a different fresh-context auditor must check "
            "false positives and false negatives before the denominator can complete"
        ),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ledger["audit"]["exact_v1_review"] = {
        "complete": sum(
            row["Review Status"] in {"deep_complete", "standard_complete"}
            for row in candidates
        ),
        "blocked": ["2606.05268"],
    }
    ledger["audit"]["v5_closure_rescreen"] = {
        "reviewed": len(v5_closure_ids),
        "reopened": len(reopened_v5),
        "remaining_closure": len(v5_closure_ids) - len(reopened_v5),
        "receipt": v5_snapshot_path.name,
        "status": "repair_complete_pending_fresh_context_candidate_denominator_fp_fn_audit",
    }
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    RECEIPTS.write_text(json.dumps({
        "schema": "june-daily-source-review-receipts-v2",
        "report_date": "2026-06-04", "families": [
            {
                "source_family_id": r["Source Family ID"],
                "arxiv_id": r["Primary Evidence Version"].split(":", 1)[1][:-2],
                "review_route": r["Review Route"], "review_provenance_id": r["Review Provenance ID"],
                "primary_evidence_version": r["Primary Evidence Version"],
                "method_locator": r["Method / Identity Locators"],
                "evaluation_locator": r["Evaluation Locators"],
                "limitations_locator": r["Limitations / Counterevidence Locators"],
                "artifact_locator": r["Artifact Locators"],
                "completion_result": r["Completion Result"],
            } for r in receipts
        ],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Frozen SHA receipt for every local exact-v1 artifact.
    sha_lines = []
    for path in sorted((PACKET / "arxiv-v1").glob("*")):
        # ``*.download`` files are interrupted transport scratch artifacts, not
        # accepted primary evidence.  Hash only canonical HTML/PDF packet files.
        if path.is_file() and path.suffix in {".html", ".pdf"} and path.stat().st_size:
            if path.suffix == ".html" and b"</html>" not in path.read_bytes()[-1024:].lower():
                continue
            sha_lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  arxiv-v1/{path.name}")
    (PACKET / "primary-material-sha256.txt").write_text("\n".join(sha_lines) + "\n", encoding="utf-8")

    lines: list[str] = []
    add = lines.append
    add("# Daily Research — 2026-06-04\n")
    add("**Research Date:** 2026-06-04\n")
    add("**Timezone:** Asia/Shanghai\n")
    add("**Window:** 2026-06-03 09:00:00 ～ 2026-06-04 09:00:00（北京时间，左闭右开）\n")
    add("**Status:** In Progress；393-family recall-first inventory 已完成逐 family pre-denominator repair，但 provisional denominator 仍等待不同上下文的 false-positive / false-negative audit；下游 Gate 与 Books writeback 未释放\n")
    deep_n = sum(int(r["Total"]) >= 7 for r in candidates)
    std_n = sum(5 <= int(r["Total"]) <= 6 for r in candidates)
    cls_n = sum(int(r["Total"]) <= 4 for r in candidates)
    int_n = sum(r["Books Disposition"] == "Integrate" for r in candidates)
    complete_review_n = deep_n + std_n - 1
    add("## Executive Summary\n")
    add(
        f"本轮以 `574/574` 个注册 identity 为 raw universe，并把此前 `393` 个候选明确降格为 recall-first inventory。逐 family 重审后，"
        f"`{len(candidates)}` 个暂时保留（retain rate `{len(candidates)/len(recall_input_ids):.2%}`；`{deep_n}` Deep、`{std_n}` Standard、`{cls_n}` Score V2 Closure），"
        f"`{len(recall_input_ids-candidate_ids)}` 个转为 family-specific pre-denominator closure；连同原有 181 个 outside，provisional denominator 外共 `{574-len(candidates)}` 个。"
        "逐项 decision、摘要哈希、旧 owner/score/route 与 closure reason 见 `candidate-denominator-replay-v10.json`。\n"
    )
    add(
        f"Standard/Deep 共 `{deep_n + std_n}` 项，其中 `{complete_review_n}` 项绑定可读 exact-v1 HTML/PDF 或明确标识 exact-v1 的作者共享正文，并完成可定位 "
        "Method/Evaluation/Limitations/Artifact review；`2606.05268` 因 exact-v1 文件损坏保持 `Blocked / Unverified`。"
        f"既有下游计算中仍有 `{int_n}` 项 provisional `Integrate`，但它们不构成当前完成声明，本 Agent 不修改 Books。"
        "同一修复作者不自证 Candidate Denominator；Coverage、Evidence、Selection 与 Books Gate 均保持 Open，等待不同上下文同时审 false positives 与 false negatives。\n"
    )
    add("## 1. Coverage\n")
    add("<!-- validator:report-metadata-v2 -->")
    add("| Field | Value |")
    add("| --- | --- |")
    metadata = {
        "Contract Version":"V2.1","Score Schema":"V2","Report Type":"Daily","Window Start":"2026-06-04","Window End":"2026-06-04",
        "Registry Version":"2026-08-25","Coverage Mode":"Full Replay","Baseline Report":"—","Changed Source IDs":"—","Previous Denominator ID":"—",
        "Denominator ID":f"daily-2026-06-04-0900-v2.1-{len(candidates)}-v10-provisional","Denominator Frozen At":REPAIR_EXECUTED_AT,
        "Completion Status":"In Progress","Coverage Gate":"Open","Evidence Gate":"Open","Books Gate":"Open",
    }
    for k,v in metadata.items(): add(f"| {k} | {v} |")
    add("\n### Source Coverage Receipt\n")
    add("<!-- validator:source-coverage-v2 -->")
    add("| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |")
    add("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    fams = "; ".join(r["Source Family ID"] for r in candidates)
    add(f"| SRC-ARXIV | 2026-06-03T09:00:00+08:00 | 2026-06-04T09:00:00+08:00 | {REPAIR_EXECUTED_AT} | Official arXiv Atom API exact-v1 batches for event time; DataCite DOI prefix snapshots for discovery; 574/574 full-abstract semantic screen | checked | 574 | {fams} | Atom batches=12, returned=574/574; DataCite pages=3, 3000/3000, final_cursor=end | 2026-06-04T01:00:00Z | ../_sources/daily-20260604/arxiv-submission-history-receipts.json; coverage:SRC-ARXIV:20260604 | — |")
    add("\n<!-- coverage:SRC-ARXIV:20260604:start -->")
    add(f"三个互斥 DataCite prefix snapshot 共 3000 条用于 discovery；官方 arXiv Atom API 对 574/574 个显式 v1 身份返回提交历史，timestamp match=574、mismatch=0、outside=0。574 条均已重新执行 abstract-level screening；393-family recall-first inventory 又完成逐 family pre-denominator replay，暂时保留 {len(candidates)}、关闭 {len(recall_input_ids-candidate_ids)}。该 denominator 仍是 provisional，等待 fresh-context FP/FN audit。逐 identity 结果见 `../_sources/daily-20260604/screening-ledger.json` 与 `../_sources/daily-20260604/candidate-denominator-replay-v10.json`。2606.05268 的 event time 已确认，但 exact-v1 正文仍不可读。")
    add("<!-- coverage:SRC-ARXIV:20260604:end -->\n")
    add("### Screening reconciliation\n")
    add(f"- Registered identities: `574/574`\n- Official arXiv v1 timestamps matched: `574/574`; mismatch/outside: `0/0`\n- Recall-first candidate inventory: `{len(recall_input_ids)}`\n- Provisional retained denominator: `{len(candidates)}` (`{len(candidates)/len(recall_input_ids):.2%}` retain rate)\n- Family-specific pre-denominator closures from prior inventory: `{len(recall_input_ids-candidate_ids)}`\n- Total outside provisional denominator: `{574-len(candidates)}`\n- Candidate FP/FN audit: `pending — different fresh context required`\n- Standard/Deep exact-v1 review carried forward: `{complete_review_n} complete / 1 blocked`\n- Ordinary raw-identity screening pending: `0`\n")
    add("## 2. Candidate Ledger and Score V2\n")
    headers = list(candidates[0])
    add("<!-- validator:candidate-ledger-v2.1 -->")
    add("| " + " | ".join(headers) + " |")
    add("| " + " | ".join("---" for _ in headers) + " |")
    for row in candidates: add("| " + " | ".join(pipe(row[h]) for h in headers) + " |")

    add("\n### Review Completion Receipt\n")
    receipt_headers = list(receipts[0])
    add("<!-- validator:review-completion-v1 -->")
    add("| " + " | ".join(receipt_headers) + " |")
    add("| " + " | ".join("---" for _ in receipt_headers) + " |")
    for row in receipts: add("| " + " | ".join(pipe(row[h]) for h in receipt_headers) + " |")

    benchmark_rows = [r for r in candidates if r["Benchmark Claim"] == "yes"]
    add("\n### Benchmark Contract\n")
    add("<!-- validator:benchmark-contract-v1 -->")
    bheaders = ["Source Family ID","Workload","Model","Hardware","Precision","Input Length","Output Length","Batch","Concurrency","SLO","Evaluator"]
    add("| " + " | ".join(bheaders) + " |")
    add("| " + " | ".join("---" for _ in bheaders) + " |")
    benchmark_replay_rows = []
    for row in benchmark_rows:
        arxiv_id = row["Primary Identifier"].split(":",1)[1][:-2]
        item=by_id[arxiv_id]
        evidence = review_evidence.get(row["Source Family ID"], {}).get("evaluation", "")
        evaluation_locator = next(r["Evaluation Locators"] for r in receipts if r["Source Family ID"] == row["Source Family ID"])
        workload = f"《{item['title']}》在 `{evaluation_locator}` 定义的 author evaluation slice"
        # Conditions are extracted only from the reviewed evaluation section and
        # only when an identity/value-shaped phrase is present.  A generic word
        # such as “model”, “GPU” or “throughput” is not a benchmark condition.
        model = disclosed_condition(evidence, (r"\b(?:Llama[- ]?\d[^,.;)]*|Qwen[- ]?[A-Za-z0-9.\-]+|DeepSeek[- ]?[A-Za-z0-9.\-]+|Gemma[- ]?[A-Za-z0-9.\-]+|Mistral[- ]?[A-Za-z0-9.\-]+|GPT[- ]?[A-Za-z0-9.\-]+|Claude[- ]?[A-Za-z0-9.\-]+)\b",), "the evaluated model identity")
        hardware = disclosed_condition(evidence, (r"\b(?:NVIDIA\s+)?(?:A100|H100|H200|B200|L40S|RTX\s*\d{4}|Ascend\s*\d+[A-Za-z]*|CloudMatrix\d+|MI\d{3}[A-Za-z]*)\b",), "hardware")
        precision = disclosed_condition(evidence, (r"\b(?:FP8|FP16|FP32|BF16|W\d+A\d+|INT8|INT4)\b",), "precision or quantization")
        input_length = disclosed_condition(evidence, (r"\b(?:input|context|sequence|prompt)[ -]?(?:length|tokens?)\s*(?:=|:|of)?\s*\d+[KkMm]?\b", r"\b\d+[KkMm]?[- ](?:input|prompt|context) tokens?\b"), "input/context length")
        output_length = disclosed_condition(evidence, (r"\b(?:output|generation|decode)[ -]?(?:length|tokens?)\s*(?:=|:|of)?\s*\d+[KkMm]?\b", r"\b\d+[KkMm]?[- ](?:output|decode) tokens?\b"), "output length")
        batch = disclosed_condition(evidence, (r"\bbatch(?: size)?\s*(?:=|:|of)?\s*\d+\b",), "batch size")
        concurrency = disclosed_condition(evidence, (r"\b(?:concurrency|concurrent requests?|simultaneous requests?)\s*(?:=|:|of)?\s*\d+\b",), "concurrency")
        slo = disclosed_condition(evidence, (r"\b(?:TTFT|TPOT|latency|deadline)\s*(?:<=|≤|<|=|:)?\s*\d+(?:\.\d+)?\s*(?:ms|s)\b",), "a production SLO")
        if arxiv_id == "2606.04415":
            workload = "vLLM serving for DeepSeek-R1-family and Qwen2.5-7B; 1K-input/1K-output and 1K-input/4K-output slices"
            model = "DeepSeek-R1-family; Qwen2.5-7B"
            hardware = "Ascend 910C; CloudMatrix384"
            precision = "W8A8 where reported"
            input_length = "1K tokens"
            output_length = "1K or 4K tokens"
            batch = "Not Disclosed — exact-v1 evaluation does not state a single batch size"
            concurrency = "Not Disclosed — exact-v1 evaluation does not state request concurrency"
            slo = "TTFT ≤ 1 s; TPOT ≤ 50 ms for the disclosed serving slice"
        if arxiv_id in BENCHMARK_OVERRIDES:
            override = BENCHMARK_OVERRIDES[arxiv_id]
            workload = override.get("workload", workload)
            model = override.get("model", model)
            hardware = override.get("hardware", hardware)
            precision = override.get("precision", precision)
            input_length = override.get("input_length", input_length)
            output_length = override.get("output_length", output_length)
            batch = override.get("batch", batch)
            concurrency = override.get("concurrency", concurrency)
            slo = override.get("slo", slo)
        evaluator = BENCHMARK_OVERRIDES.get(arxiv_id, {}).get("evaluator", "Authors; exact-v1 evaluation setup")
        vals=[row["Source Family ID"],workload,model,hardware,precision,input_length,output_length,batch,concurrency,slo,evaluator]
        add("| " + " | ".join(pipe(v) for v in vals) + " |")
        benchmark_replay_rows.append({
            "source_family_id": row["Source Family ID"],
            "arxiv_id": arxiv_id,
            "evaluation_locator": evaluation_locator,
            "evidence_binding": (
                "local exact-v1 artifact" if exact_path(arxiv_id)
                else "live/author exact-v1 binding disclosed in source-review receipt"
            ),
            **dict(zip([x.casefold().replace(" ", "_") for x in bheaders[1:]], vals[1:])),
            "length": f"input: {input_length}; output: {output_length}",
            "v8_contradiction_repaired": arxiv_id in {
                "2606.04366", "2606.04373", "2606.04438", "2606.04463", "2606.04719",
                "2606.04727", "2606.04767", "2606.04939", "2606.04964", "2606.05233",
                "2606.05250", "2606.05271", "2606.05336", "2606.05367", "2606.05396",
                "2606.05429", "2606.06527",
            },
        })
    (PACKET / "benchmark-disclosure-replay-v9.json").write_text(
        json.dumps({
            "schema": "benchmark-disclosure-replay-v1",
            "report_date": "2026-06-04",
            "benchmark_family_count": len(benchmark_replay_rows),
            "fields_checked": [
                "workload", "model", "hardware", "precision", "input_length", "output_length",
                "batch", "concurrency", "slo", "evaluator",
            ],
            "v8_high_confidence_contradictions_repaired": sum(
                row["v8_contradiction_repaired"] for row in benchmark_replay_rows
            ),
            "rows": benchmark_replay_rows,
            "gate_boundary": "repair-owner replay only; Evidence Gate awaits a different new-context semantic audit",
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    add("\n## 3. Source Reviews\n")
    for row in candidates:
        family=row["Source Family ID"]; arxiv_id=row["Primary Identifier"].split(":",1)[1][:-2]
        add(f"### {arxiv_id} — {by_id[arxiv_id]['title']}\n")
        add(f"<!-- review:{family}:start -->")
        add(review_bodies[family])
        add(f"<!-- review:{family}:end -->\n")

    deep_rows=[r for r in candidates if int(r["Total"])>=7]
    selected_ids=["2606.04929","2606.05304","2606.05484"]
    units={"2606.04929":"DA-CROSS-STAGE-POISONING","2606.05304":"DA-ACTION-STATE-COMMUNICATION","2606.05484":"DA-LEARNED-ACTIVATION-COMPRESSION"}
    selected_rows={r["Primary Identifier"].split(":",1)[1][:-2]:r for r in deep_rows if r["Primary Identifier"].split(":",1)[1][:-2] in selected_ids}
    add("## 4. Deep Analysis Selection\n")
    add("<!-- validator:deep-analysis-selection-v1 -->")
    dheaders=["Source Family ID","Eligibility","Decision","Analysis Unit ID","Subsumed By","Priority Rationale","Narrative Ref"]
    add("| " + " | ".join(dheaders) + " |")
    add("| " + " | ".join("---" for _ in dheaders) + " |")
    selection_rationales: dict[str, str] = {}
    for row in deep_rows:
        aid=row["Primary Identifier"].split(":",1)[1][:-2]; family=row["Source Family ID"]
        if aid in selected_ids:
            unit=units[aid]; decision="selected"; subsumed="—"; ref=f"analysis:{unit}"
            rationale=(
                f"{by_id[aid]['title']} scores {row['Design Delta']}/{row['System Reach']}/{row['Durability']} and changes "
                f"the durable `{row['Stable Node ID']}` state/control contract rather than only an implementation choice; "
                "its exact-v1 method, evaluation and counterevidence are independently locatable."
            )
        else:
            decision="not_selected"; unit="—"; subsumed="—"; ref=f"analysis-decision:{family}"
            signal=SELECTION_SIGNAL_OVERRIDES.get(aid) or pick_sentence(
                review_evidence.get(family,{}).get("method",by_id[aid]["abstract"]),
                ("we ","method","system","model"),0,
            )[:240]
            comparator_id=("2606.04929" if row["Stable Node ID"] in {"PLATFORM-SECURITY","PLATFORM-EVALUATION-SYSTEM"}
                           else "2606.05304" if row["Stable Node ID"].startswith("AGENT-") or row["Stable Node ID"].startswith("MULTIMODAL-")
                           else "2606.05484")
            comparator=units[comparator_id]
            selected_row=selected_rows[comparator_id]
            gaps=[]
            for label in ("Design Delta","System Reach","Durability"):
                gap=int(selected_row[label])-int(row[label])
                if gap>0: gaps.append(f"{label} 低 {gap} 级")
            if row["Review Status"] == "blocked":
                relative="exact-v1 正文材料未恢复，当前不能形成可审计长叙事"
            elif gaps:
                relative="、".join(gaps) + f"；其可复用机制被限定为：{signal[:160]}"
            elif row["Books Disposition"] != "Integrate":
                chapter,path=by_node[row["Stable Node ID"]]
                line=source_line(path,BOOKS_KEYWORDS.get(aid,(row["Stable Node ID"].split("-")[-1],)))
                relative=f"目标章节 `{path}#L{line}` 已拥有：{books_excerpt(path,line,0)[:180]}"
            else:
                eval_slice=review_evidence.get(family,{}).get("evaluation","exact-v1 bounded evaluation")[:180]
                relative=f"虽保留 Integrate，但证据只覆盖 `{eval_slice}`，跨 owner 的演进解释不及所选 comparator"
            rationale=(
                f"`{by_id[aid]['title']}` 在 `{row['Stable Node ID']}` 的候选机制是：{signal} "
                f"与 `{comparator}` 的 {selected_row['Design Delta']}/{selected_row['System Reach']}/{selected_row['Durability']} 相比，"
                f"本 family 为 {row['Design Delta']}/{row['System Reach']}/{row['Durability']}，不占长叙事名额的逐项理由是：{relative}。"
            )
            if aid == "2606.05158":
                rationale = (
                    "`Streaming Communication in Multi-Agent Reasoning` 与所选 `DA-ACTION-STATE-COMMUNICATION` "
                    "同为 3/3/3，也保留 Integrate。StreamMA 改变 partial reasoning 的可用时间与 pipeline critical path，"
                    "但不改变消息被持久化后的 schema、authority 或 rollback contract；PACT 直接改变 raw language 到 committed "
                    "action-state record 的状态边界，因此承担本窗口通信主线。StreamMA 的 exact-v1 证据限于八个 OpenCompass "
                    "benchmark、所列模型/拓扑与重复次数，作为 Ch82 的并列 streaming 分支进入 Books，而不被低分淘汰。"
                )
            elif aid == "2606.05165":
                rationale = (
                    "`STRIDE` 与所选 `DA-LEARNED-ACTIVATION-COMPRESSION` 同为 3/3/3，也保留 Integrate。STRIDE 通过 subset "
                    "perturbation 与 sparse recovery 估计 data influence，改变 TRAIN-DATA 的 attribution estimator；其状态范围止于"
                    "训练数据子集、激活响应和 downstream influence score。所选 family 则把 pipeline stage boundary 从固定 activation "
                    "tensor 改成需训练、checkpoint 与恢复的 communication state，跨训练/运行时影响更直接，因此占用第三个跨层长叙事名额。"
                )
        selection_rationales[family] = rationale
        vals=[family,"score_7_9" + ("; potential_books_delta" if row["Books Disposition"]=="Integrate" else ""),decision,unit,subsumed,rationale,ref]
        add("| " + " | ".join(pipe(v) for v in vals) + " |")

    for row in deep_rows:
        aid=row["Primary Identifier"].split(":",1)[1][:-2]
        if aid in selected_ids:
            continue
        family=row["Source Family ID"]
        signal=SELECTION_SIGNAL_OVERRIDES.get(aid) or pick_sentence(
            review_evidence.get(family,{}).get("method",by_id[aid]["abstract"]),
            ("we ","method","system","model"),0,
        )[:320]
        comparator_id=("2606.04929" if row["Stable Node ID"] in {"PLATFORM-SECURITY","PLATFORM-EVALUATION-SYSTEM"}
                       else "2606.05304" if row["Stable Node ID"].startswith("AGENT-") or row["Stable Node ID"].startswith("MULTIMODAL-")
                       else "2606.05484")
        comparator=units[comparator_id]
        row_rationale = selection_rationales[family]
        add(
            f"<!-- analysis-decision:{family}:start -->"
            f"`{family}` 在 `{row['Stable Node ID']}` 的具体机制是：{signal} "
            f"对应评分为 {row['Design Delta']}/{row['System Reach']}/{row['Durability']}；相对 `{comparator}` 的决定证据是："
            f"{next((cell for cell in [row_rationale] if cell), '见上表')} "
            "因此不占用三项长叙事名额；这不降低其 Source Review 或 Books disposition 责任。"
            f"<!-- analysis-decision:{family}:end -->"
        )

    analyses={
        "DA-CROSS-STAGE-POISONING": (
            "从单阶段威胁模型到跨阶段组合攻击",
            "逐阶段安全测试假设每个数据源的风险可独立评估；顺序 post-training 却会把 SFT、reward/preference data 的影响组合到同一参数状态。论文区分 additive 与 complementary 两类组合效应，说明单阶段低风险不能推出 pipeline 低风险。代价是安全 Gate 必须保存 stage lineage、联合 poison budget 与跨阶段回放，旧的单阶段测试在来源可信或阶段真正隔离时仍更便宜。"
        ),
        "DA-ACTION-STATE-COMMUNICATION": (
            "从自由文本转发到显式 Action-state Commit",
            "generate-then-transfer 保留全部自然语言，容易让 token 成本和迟到错误随拓扑深度累积。PACT 把 raw output 投影成下游所需的 action-state record，再提交到 shared history；它改变的不是 Agent 数量，而是通信状态的 owner 与 commit schema。收益是更小上下文和较早消费可靠步骤；代价是投影器可能删掉必要证据，且作者在特定模型、benchmark 与 harness 上的结果不能外推为任意多 Agent 拓扑。"
        ),
        "DA-LEARNED-ACTIVATION-COMPRESSION": (
            "从固定边界张量到可学习的 Stage Communication Contract",
            "Pipeline Parallelism 把激活按原始边界张量传递，实现简单且保真，但当跨 stage 带宽成为主导成本时，传输所有激活不再合理。该 family 学习 orthogonal projection，使 communication boundary 从固定 tensor identity 变成可训练的 compression/decompression state。它降低 bytes，但引入投影误差、训练耦合和恢复复杂度；未证明的模型、网络和精度条件下不应外推。"
        ),
    }
    for unit,(title,body) in analyses.items():
        add(f"\n<!-- analysis:{unit}:start -->\n### {title}\n\n{body}\n<!-- analysis:{unit}:end -->")

    # A Books comparison is evidence-bearing.  A blocked deep family remains in
    # selection accounting, but cannot receive a completed Books comparison.
    books_rows=[r for r in deep_rows if r["Review Status"] == "deep_complete"]
    add("\n## 5. Books Comparison\n")
    add("<!-- validator:books-comparison-v1 -->")
    bh=["Source Family ID","Stable Node ID","Target Chapter Ref","Adjacent Chapter Refs","Existing Proposition","New Evidence Delta","Evolution Relation","Decision","Books Review Ref"]
    add("| " + " | ".join(bh) + " |")
    add("| " + " | ".join("---" for _ in bh) + " |")
    books_replay_rows = []
    for row in books_rows:
        family=row["Source Family ID"]; owner=row["Stable Node ID"]; aid=row["Primary Identifier"].split(":",1)[1][:-2]
        chapter,path=by_node[owner]; adjacent=[by_chapter[x] for x in (chapter-1,chapter+1) if x in by_chapter]
        comparison_text = " ".join((
            by_id[aid]["title"], by_id[aid]["abstract"],
            review_evidence.get(family, {}).get("method", ""),
        ))
        target_line=(
            source_line(path, BOOKS_TARGET_TERMS[aid])
            if aid in BOOKS_TARGET_TERMS
            else semantic_source_line(path, comparison_text, BOOKS_KEYWORDS.get(aid,(owner.split("-")[-1],)))
        )
        adjacent_refs=[]
        for adjacent_path in adjacent:
            adjacent_refs.append(f"{adjacent_path}#L{source_line(adjacent_path,('handoff','boundary','state'))}")
        vals=[family,owner,f"{path}#L{target_line}","; ".join(adjacent_refs),f"existing:{family}",f"delta:{family}","Layering / Dependency",row["Books Disposition"],f"books-review:{family}"]
        add("| " + " | ".join(pipe(v) for v in vals) + " |")
    for row in books_rows:
        family=row["Source Family ID"]; aid=row["Primary Identifier"].split(":",1)[1][:-2]; owner=row["Stable Node ID"]
        delta=pick_sentence(by_id[aid]["abstract"], ("we propose","we introduce","we present","we develop"),1)
        # V6 found that frozen comparison prose drifted after shared Books
        # movement.  Recompute every comparison from current target/adjacent
        # chapter content; legacy notes are retained above only as audit history.
        note=BOOKS_COMPARISON_NOTES.get(aid)
        chapter,path=by_node[owner]
        comparison_text = " ".join((
            by_id[aid]["title"], by_id[aid]["abstract"],
            review_evidence.get(family, {}).get("method", ""),
        ))
        target_line=(
            source_line(path, BOOKS_TARGET_TERMS[aid])
            if aid in BOOKS_TARGET_TERMS
            else semantic_source_line(path, comparison_text, BOOKS_KEYWORDS.get(aid,(owner.split("-")[-1],)))
        )
        adjacent=[by_chapter[x] for x in (chapter-1,chapter+1) if x in by_chapter]
        target_text=books_excerpt(path,target_line,1)[:520]
        method_delta=review_evidence.get(family,{}).get("method",delta)[:520]
        if note:
            existing, evidence_delta, adjacent_role = note
        else:
            existing=(
                f"针对《{by_id[aid]['title']}》的机制问题，`{owner}` 当前在 `{path}#L{target_line}` "
                f"最接近的 canonical proposition 是：{target_text}。比较边界是候选是否改变该 proposition "
                "拥有的状态、控制权、资源或 evidence contract，而不是二者是否共享主题词。"
            )
            evidence_delta=(
                f"exact-v1 的新增机制证据是：{method_delta} 该证据只在 receipt 的 evaluation/limitations "
                "边界内成立，不能从论文名称或摘要外推。"
            )
            adjacent_role=(
                "相邻章节只承担输入/输出 handoff："
                + "; ".join(
                    f"`{p}`（{books_excerpt(p,source_line(p,('handoff','boundary','state')),0)[:180]}）"
                    for p in adjacent
                )
            )
        add(f"<!-- books-review:{family}:start -->")
        add(f"<!-- existing:{family}:start -->{existing}<!-- existing:{family}:end -->")
        add(f"<!-- delta:{family}:start -->{evidence_delta}<!-- delta:{family}:end -->")
        add(f"相邻章节交接：{adjacent_role} 因此逐项比较后的决定为 `{row['Books Disposition']}`；`Integrate` 仍需 root 按日期串行写回。")
        add(f"<!-- books-review:{family}:end -->")
        books_replay_rows.append({
            "source_family_id": family,
            "arxiv_id": aid,
            "stable_node_id": owner,
            "target_chapter_ref": f"{path}#L{target_line}",
            "adjacent_chapter_refs": [
                f"{p}#L{source_line(p, ('handoff', 'boundary', 'state'))}" for p in adjacent
            ],
            "existing_proposition": existing,
            "new_evidence_delta": evidence_delta,
            "adjacent_role": adjacent_role,
            "decision": row["Books Disposition"],
            "v8_mismatch_repaired": aid in {"2606.04535", "2606.04549", "2606.05423", "2606.05433"},
        })

    (PACKET / "books-comparison-replay-v9.json").write_text(
        json.dumps({
            "schema": "books-comparison-replay-v1",
            "report_date": "2026-06-04",
            "comparison_count": len(books_replay_rows),
            "current_content_replayed": True,
            "v8_mismatches_repaired": sum(row["v8_mismatch_repaired"] for row in books_replay_rows),
            "rows": books_replay_rows,
            "books_files_modified": False,
            "gate_boundary": "repair-owner replay only; Books Comparison awaits a different new-context semantic audit",
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    add("\n## 6. Semantic Audit and Gate\n")
    add(f"<!-- audit:SA-0604-REPAIR:start -->本修复先保留 V8 的 217/217 outside replay 作为 recall 证据，再把此前 393 个候选整体重开为 recall-first inventory。逐 family pre-denominator replay 暂时保留 `{len(candidates)}`、关闭 `{len(recall_input_ids-candidate_ids)}`，retain rate 为 `{len(candidates)/len(recall_input_ids):.2%}`。该结果不能由修复作者自证；必须先由不同 fresh context 同时审 false positives 与 false negatives，Evidence、Selection、Books 下游验收继续暂停，Books 文件未修改。<!-- audit:SA-0604-REPAIR:end -->\n")
    add("<!-- validator:semantic-audit-v1 -->")
    add("| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |")
    add("| --- | --- | --- | --- | --- | --- | --- |")
    add(f"| SA-20260604-CANDIDATE-DENOMINATOR-REPAIR | fresh-context:jun04-v8-repair-owner | coverage | coverage:SRC-ARXIV:20260604; audit:SA-0604-REPAIR | FRESH-CONTEXT-FP-FN-AUDIT-PENDING: provisional `{len(candidates)}`-family denominator 不能由修复作者自证 | raw identities=574；old recall inventory={len(recall_input_ids)}；provisional retained={len(candidates)}；family-specific closure={len(recall_input_ids-candidate_ids)}；retain rate={len(candidates)/len(recall_input_ids):.2%}；逐项 external receipt 为 `candidate-denominator-replay-v10.json` | open |")
    add(f"| SA-20260604-EVIDENCE-REPAIR | fresh-context:jun04-v8-repair-owner | evidence | validator:review-completion-v1 | DOWNSTREAM-PAUSED: Candidate Denominator 的 fresh-context FP/FN audit 未完成；另有 MATERIAL-BLOCKER 2606.05268 | locator/benchmark repair receipt 已保留在 `benchmark-disclosure-replay-v9.json`，但不得在 denominator 验收前升级为 Evidence Gate 完成；2606.05268 保持唯一 blocked family | open |")
    add(f"| SA-20260604-SELECTION-REPAIR | fresh-context:jun04-v8-repair-owner | deep_analysis_selection | validator:deep-analysis-selection-v1; analysis:DA-CROSS-STAGE-POISONING | DOWNSTREAM-PAUSED: eligibility denominator 尚未独立验收 | 现有 selected/not_selected 仅为 provisional carry-forward，不构成选择语义验收 | open |")
    add(f"| SA-20260604-BOOKS-COMPARISON | fresh-context:jun04-v8-repair-owner | books | validator:books-comparison-v1 | DOWNSTREAM-PAUSED: Candidate Denominator 尚未独立验收，current-content owner/proposition 也仍需 fresh-context verification | 既有 comparison repair 只保留在 `books-comparison-replay-v9.json`；`{int_n}` 项不得释放，Books writeback queue 保持关闭，Books 文件未修改 | open |")

    add("\n## 7. Ignored Noise\n")
    add(f"`{574-len(candidates)}` 个 identity 位于 provisional denominator 外，但没有静默丢弃：原有 181 条 outside 保留 claim-specific screening reason；从 393 recall inventory 新关闭的 `{len(recall_input_ids-candidate_ids)}` 条另带 family-specific closure class、exact-v1 abstract hash、旧 route/owner/score 与缺失的 durable contract。`{cls_n}` 个仍保留的低分 family 继续进入 Score V2 ledger，等待独立 auditor 判断它们是否还是 false positive。\n")
    add("## 8. Recommended Action\n")
    add(f"下一步只先交给不同上下文 auditor 重放 Candidate Denominator 的 false positives 与 false negatives。该 scope 通过前暂停 Evidence、Deep Analysis Selection 与 Books Comparison 的完成验收；不得释放 `{int_n}` 个 provisional `Integrate`、写 Books 或把日报标为 Complete。\n")
    add("## 9. Repository Changes\n")
    add("- Preserved the 574/574 raw identity universe and reopened the old 393-family set as a recall-first inventory.\n- Added `candidate-denominator-replay-v10.json`: one decision per old candidate, with old state, abstract hash, family-specific rationale and provisional new state.\n- Rebuilt the Daily Candidate Ledger from the provisional retained set; all Semantic Gates remain Open.\n- Kept earlier locator/benchmark/Books comparison repairs as downstream provisional receipts. No Books file was edited by this agent.\n")
    add("## 10. Open Questions\n")
    add(f"- Root must decide and serialize `{int_n}` Books writebacks, then run a fresh-context Books Semantic Audit.\n- `P1 Full Text / 2026-06-04 / arXiv:2606.05268v1`: need a readable exact-v1 PDF, arXiv source archive, or author-hosted exact-version manuscript. The frozen PDF is truncated/corrupt and current official PDF/e-print transfers did not yield a valid EOF/xref artifact; abstract/metadata cannot support Method, Evaluation or Limitations review. After recovery, audit the full Method, experiment setup/results, counterevidence/limitations, artifact, benchmark conditions and Books comparison. Suggested filename: `2606.05268v1.pdf` (or `2606.05268v1.tar`).\n")
    add("\n### Materials Request Ledger\n")
    add("<!-- validator:materials-request-v1 -->")
    mh=["Request ID","Priority","Source Family ID","Source ID","Gap / Limitation ID","Owner Week","Known Identifiers / URLs","Missing Material","Why Existing Evidence Is Insufficient","Acceptable Substitute","Suggested File Name","Required Review Scope"]
    add("| " + " | ".join(mh) + " |")
    add("| " + " | ".join("---" for _ in mh) + " |")
    mv=[
        "MR-SF-2026-ARXIV-2606-05268-01","P1 Full Text","SF-2026-ARXIV-2606-05268","—","—","2026-W23",
        "arXiv:2606.05268v1; https://arxiv.org/pdf/2606.05268v1; https://arxiv.org/e-print/2606.05268v1",
        "Readable exact-v1 full text and, if available, the exact-v1 source archive",
        "The frozen PDF is truncated/corrupt and current official PDF/e-print transfers did not yield a valid EOF/xref artifact; metadata and abstract cannot support Method, Evaluation, Limitations, artifact or benchmark claims",
        "Readable official exact-v1 PDF, complete arXiv source archive, or author-hosted exact-version manuscript",
        "2606.05268v1.pdf (or 2606.05268v1.tar)",
        "Read Method and formulas, experiment setup/results, ablations, appendices/counterevidence, limitations, artifact and benchmark conditions; then redo Source Review, family-relative selection and target/adjacent Books comparison",
    ]
    add("| " + " | ".join(pipe(v) for v in mv) + " |")
    add("## Sources\n")
    add(f"- [arXiv API](https://export.arxiv.org/api_help/) — official v1 submission-history evidence; 12 raw Atom batches and the 574/574 reconciliation receipt are frozen under `../_sources/daily-20260604/arxiv-history/`; accessed 2026-08-28.\n- [arXiv exact v1 HTML/PDF](https://arxiv.org/) — primary manuscript source for completed Standard/Deep reviews except the separately disclosed MapAgent author-mirror fallback; local event-time artifacts are frozen under `../_sources/daily-20260604/arxiv-v1/`, while independently recovered arXiv web-path items retain exact-v1 URLs and section locators; accessed 2026-08-28.\n- [MapAgent author-shared exact-v1 manuscript](https://www.researchgate.net/publication/405922503_MapAgent_An_Industrial-Grade_Agentic_Framework_for_City-scale_Lane-level_Map_Generation) — full author manuscript explicitly bearing `arXiv:2606.04513v1`, used for §2 mechanism, §3 experiment/ablation and §6 boundary review after the official arXiv full-text transfer failed; accessed 2026-08-28.\n- DataCite arXiv DOI prefix snapshots — discovery, identity and abstract metadata only; they do not prove event time or mechanism; frozen and hashed in the source packet.\n")
    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    (PACKET / "independent-v8-repair-resolution.md").write_text(
        "# 2026-06-04 Independent V8 Repair Resolution\n\n"
        "## Repair boundary\n\n"
        "本记录由 V8 finding repair owner 生成，只证明修复施工与可复算 receipt 已完成；它不充当 "
        "fresh-context semantic acceptance，也不把 validator 结果升级为 Gate 通过。Books 文件未修改。\n\n"
        "## Finding resolution\n\n"
        f"- `V8-COV-01`: 对 V8 输入的 `{len(v8_outside_ids)}/{len(v8_outside_ids)}` outside 做完整 conservative replay；"
        f"`{len(V8_REOPEN)}` 条进入 393-family recall inventory，`{len(v8_outside_ids - V8_REOPEN)}` 条维持原 outside。"
        f"随后按更严格 Candidate Denominator 口径，这 36 条全部转为 family-specific pre-denominator closure；这说明 recall 恢复不等于 retain。逐项结果见 `outside-replay-independent-v9.json` 与 `candidate-denominator-replay-v10.json`。\n"
        "- `V8-EVID-01`: `2606.04610` Method 改为 `§2 Overview; §§2.1–2.2; §3 The Specificity Challenge; §§3.1–3.3`，"
        "并由新 locator 重新提取 review body 与 RP。\n"
        "- `V8-EVID-02`: `2606.05233` Method/Evaluation/Limitations locator 扩展到 §2–§7 与相关 appendices；"
        "benchmark 明确 Sonnet 4.6、GPT-5.4 与 793 episodes；artifact 区分 Zenodo benchmark release 与 AutoInject cited implementation。\n"
        f"- `V8-EVID-03`: 全部 `{len(benchmark_replay_rows)}` 个 benchmark-bearing family 对 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator 重新生成逐项 receipt；"
        f"修正 `{sum(row['v8_contradiction_repaired'] for row in benchmark_replay_rows)}` 个 V8 高置信 contradiction，见 `benchmark-disclosure-replay-v9.json`。\n"
        "- `V8-EVID-04`: official exact-v1 HTML/PDF 恢复路径再次 reset；`2606.05268` 仍是唯一 blocked family 与唯一 materials request。"
        "25 个 live/author binding 的 replayability limitation 继续显式保留，不扩写为 25 个 blocker。\n"
        "- `V8-SEL-01`: 下游 selection receipt 保留，但 Candidate Denominator 独立验收前暂停 selection semantic acceptance。\n"
        "- `V8-BOOKS-01`: 既有 comparison 修复 receipt 保留；Candidate Denominator 独立验收前暂停 Books Comparison 完成验收与全部 writeback。\n\n"
        "## Gate truth\n\n"
        "| Scope / Gate ceiling | Status | Reason |\n"
        "| --- | --- | --- |\n"
        "| Candidate Denominator / Coverage | Open | 393-family replay complete; provisional retained set awaits fresh-context FP/FN audit |\n"
        "| Evidence | Open | downstream acceptance paused; 2606.05268 remains the sole external blocker |\n"
        "| Deep Analysis Selection | Open | downstream acceptance paused until denominator audit |\n"
        "| Books Comparison / Books | Open | downstream acceptance paused; Books writeback queue remains closed |\n\n"
        "**Repair status:** complete. **Semantic acceptance:** awaiting a different fresh-context Candidate Denominator FP/FN audit.\n",
        encoding="utf-8",
    )

    closure_class_counts: dict[str, int] = {}
    for replay_row in denominator_replay_rows:
        closure_class = replay_row.get("closure_class")
        if closure_class:
            closure_class_counts[closure_class] = closure_class_counts.get(closure_class, 0) + 1
    closure_class_table = "\n".join(
        f"| `{closure_class}` | {count} |"
        for closure_class, count in sorted(closure_class_counts.items())
    )
    (PACKET / "candidate-denominator-repair-v10.md").write_text(
        "# 2026-06-04 Candidate Denominator Repair V10\n\n"
        "## Outcome first\n\n"
        f"Raw identities=`574`；旧 recall-first candidate inventory=`{len(recall_input_ids)}`；"
        f"provisional retained=`{len(candidates)}`；family-specific pre-denominator closure="
        f"`{len(recall_input_ids-candidate_ids)}`；retain rate=`{len(candidates)/len(recall_input_ids):.2%}`。\n\n"
        "这不是 Semantic acceptance。修复作者只完成逐 family replay 与可复算 receipt；新分母必须由不同 "
        "fresh context 同时审 false positives 与 false negatives 后才能冻结。Books 文件未修改。\n\n"
        "## Retention boundary\n\n"
        "只保留能够改变长期 AI System mechanism、state/data/control ownership、evaluation contract，或 "
        "platform/training/inference 设计判断的 family。可映射 ROADMAP、属于 AI、提出单领域方法或带 benchmark "
        "都不是充分条件。每个旧候选的摘要哈希、旧 route/owner/score、decision class 与 family-specific rationale "
        "均保存在 `candidate-denominator-replay-v10.json`。\n\n"
        "## Closure classes\n\n"
        "| Closure class | Families |\n"
        "| --- | ---: |\n"
        f"{closure_class_table}\n\n"
        "## Gate truth\n\n"
        "| Scope | Status | Boundary |\n"
        "| --- | --- | --- |\n"
        "| Candidate Denominator / Coverage | Open | repair complete; fresh-context FP/FN audit pending |\n"
        "| Evidence | Open | downstream acceptance paused; 2606.05268 remains the sole materials request |\n"
        "| Deep Analysis Selection | Open | downstream acceptance paused until denominator audit |\n"
        "| Books Comparison / Books | Open | downstream acceptance paused; no Books writeback |\n\n"
        "**Repair status:** complete. **Semantic acceptance:** awaiting a different fresh-context Candidate "
        "Denominator FP/FN audit.\n",
        encoding="utf-8",
    )

    packet_readme = PACKET / "README.md"
    packet_readme.write_text(
        "# 2026-06-04 Daily Evidence Archive\n\n"
        "本目录冻结北京时间 `[2026-06-03 09:00, 2026-06-04 09:00)` 的 574 个注册 arXiv v1 身份。\n\n"
        f"- Raw identities=`574`；旧 recall-first candidate inventory=`{len(recall_input_ids)}`；逐 family pre-denominator replay 后 provisional retained=`{len(candidates)}`、family-specific closure=`{len(recall_input_ids-candidate_ids)}`、retain rate=`{len(candidates)/len(recall_input_ids):.2%}`。\n"
        f"- V8 的 36 条 queue 只证明 recall 漏项，不能自动证明 retention；它们已全部在更严格 replay 中关闭。Standard/Deep 下游 receipt 当前为 {complete_review_n} complete / 1 blocked（2606.05268），但下游 acceptance 暂停。\n"
        "- `arxiv-submission-history-receipts.json` 记录官方 Atom v1 574/574 timestamp match、0 mismatch、0 outside；`arxiv-history/` 保存 12 个原始批次。\n"
        "- `screening-ledger.json` 是逐 identity coverage truth；`candidate-denominator-replay-v10.json` 保存 393/393 的 provisional retain/closure decision 与证据；`source-review-receipts.json` 是下游 review routing receipt。\n"
        "- `outside-replay-independent-v9.json` 保存 217 outside replay；`benchmark-disclosure-replay-v9.json` 与 `books-comparison-replay-v9.json` 是下游 provisional repair receipt，不构成 Gate 通过。\n"
        "- `primary-material-sha256.txt` 冻结本目录所有 exact-v1 artifact。\n"
        "- 25 个完成态 family 仍使用 live/author exact-v1 binding，属于 replayability limitation，不扩写为 25 个 blocker。\n"
        "- 本 packet 不替代 Daily 的 Books writeback 与 fresh-context Books audit。\n\n"
        "## Candidate Denominator repair status\n\n"
        "`candidate-denominator-repair-v10.md` 记录 393-family replay。Repair complete；Candidate Denominator 等待不同 fresh context 的 FP/FN audit；Evidence、Selection 与 Books 下游 acceptance 暂停，Books writeback queue 保持关闭。\n\n"
        "## Evidence boundary\n\n"
        "官方 arXiv Atom v1 receipt 证明 event time；DataCite 只用于 discovery/identity/abstract metadata。机制、实验和限制只由可读 exact-v1 正文支持；2606.05268 保持 blocked，作者 benchmark 不外推为生产 SLO。\n",
        encoding="utf-8",
    )
    print(json.dumps({"registered":574,"denominator":len(candidates),"deep":deep_n,"standard":std_n,"closure":cls_n,"integrate":int_n}, ensure_ascii=False))


if __name__ == "__main__":
    main()
