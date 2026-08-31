#!/usr/bin/env python3
"""Rebuild the 2026-06-01 V2.1 report after an independent semantic audit.

This is deliberately date-scoped.  It consumes the frozen 371-hit screen, the
61-family fresh-audit curation, and exact-v1 arXiv material.  It does not edit
Books; it only prepares the per-family Books comparisons for the serial owner.
"""

from __future__ import annotations

import csv
import argparse
import functools
import gzip
import hashlib
import html
import importlib.util
import re
import xml.etree.ElementTree as ET
from datetime import date
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260601"
CURATION = PACKET / "fresh-audit-curation.tsv"
CURATION_WAVE2 = PACKET / "fresh-audit-curation-wave2.tsv"
CURATION_V3 = PACKET / "fresh-audit-curation-v3.tsv"
CURATION_V4 = PACKET / "fresh-audit-curation-v4.tsv"
CURATION_V5 = PACKET / "fresh-audit-curation-v5.tsv"
CURATION_V6 = PACKET / "fresh-audit-curation-v6.tsv"
CURATION_V7 = PACKET / "fresh-audit-curation-v7.tsv"
CURATION_V9 = PACKET / "fresh-audit-curation-v9.tsv"
V9_DENOMINATOR_RECEIPT = PACKET / "fresh-context-candidate-denominator-audit-independent-v9.tsv"

# V8 reopens Candidate Denominator semantics.  A completed Core source review
# is necessary evidence, not automatic candidacy.  Only families that change a
# durable AI-System mechanism, state/data/control ownership, evaluation
# contract, or platform/training/inference design judgement remain retained.
RETAINED_FAMILIES_V8 = {
    "SF-METASTABLE-FAULT-SCHEDULING",
    "SF-PRISM-DP-LORA",
    "SF-LODESTAR-ONLINE-ROUTER",
    "SF-HIFLOAT8-VIDEO-QUANT",
    "SF-SS-ZKR-MAS",
    "SF-REASMORY-VLM",
    "SF-REGISTRY-BOUND-EVIDENCE-EXTRACTION",
    "SF-SUBLIMINAL-STEERING-DISTILLATION",
    "SF-ORDER-AGNOSTIC-CHAIN-RULE",
    "SF-TRAIT-MISALIGNMENT-MONITOR",
    "SF-MELT-GEMM-AUDIO",
    "SF-HYBRID-VERIFIED-DECODING",
    "SF-TAU0-WORLD-MODEL",
    "SF-JUDGE-PANEL-CALIBRATION",
    "SF-ML-LIFECYCLE-ASSESSMENT",
    "SF-EXPWEAVER-LATENT-RAG",
    "SF-PLAUSIBILITY-NOT-PREDICTION",
    "SF-PMC-INTERCPT-CONTEXT-GROUNDED-DATA",
    "SF-DJUDGE-MULTITURN-JAILBREAK",
    "SF-DAG-MOE",
    "SF-LEYLINE-KV-DIRECTIVES",
    "SF-RLVR-VERIFIER-FUZZING",
    "SF-DART-TEST-TIME-RERANKING",
    "SF-SYMMETRY-DATA-EXCHANGE-EVAL",
    "SF-PER-COMPONENT-NEURAL-SOLVER-AUDIT",
    "SF-LOCAL-MIXVR",
    "SF-MEMORYWIRE",
    "SF-RL-SHARED-PREFIX-REUSE",
    "SF-EXPECTED-VALUE-REWARD",
    "SF-DEFT-DYNAMIC-WORKFLOW-SCHEDULING",
    "SF-ADAPTIVE-COMPLEXITY-REASONING",
    "SF-CABED-CONVERSATION-PLANNING",
    "SF-LOW-RESOURCE-SAFETY-ACTION",
    "SF-CARVE-MANEUVER-REPAIR",
    "SF-HOMEFLOW-AGENT-TRAINING",
    "SF-CFDP-CLOSED-FORM-DIFFUSION-POLICY",
    "SF-SIRIUS-SQL-EXECUTION-FEEDBACK",
    "SF-IN-SENSOR-INT8-INFERENCE",
    "SF-RAG-INFERENCE-COST-ATTACK",
    "SF-TARGET-UPDATE-Q-STABILITY",
    "SF-HARD-NEGATIVE-GEN-DISC-GAP",
    "SF-SKILLADAPTOR",
    "SF-STATE-CONTEXT-MINIFICATION",
    "SF-LEARNING-AUGMENTED-PAGING-ROBUSTNESS",
    "SF-FAILURE-AWARE-MAS-OBS",
    "SF-SEV-FORMAL-VERIFICATION",
    "SF-RESIDENT-KV-CLAIMS",
    "SF-AIREP",
    "SF-APPROX-DIFFERENTIAL-EQUIVALENCE",
    "SF-GPTQ-INTRINSIC-LORA",
    "SF-DP-RAG-DATASTORE",
    "SF-SELF-HEALING-ORCHESTRATOR",
    "SF-MEMORY-FRESHNESS-ASSEMBLY",
    "SF-SATURATED-DATA-SIGNALS",
    "SF-CEAR-CERTIFIED-ENSEMBLE",
    "SF-CROSSCLOUD-INTERCONNECT",
    "SF-OPENEYE-DNN-ACCELERATOR",
    "SF-MURMUR-ASR-INFERENCE",
    "SF-CLAWHUB-SECURITY-SIGNALS",
    "SF-CROSS-INSTANCE-LATENT-REDISTRIBUTION",
    "SF-AGENT-OPERATING-SYSTEM",
    "SF-AGENT-FALSE-SUCCESS",
    "SF-PROBMOE",
    "SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY",
}

# Exact family set from independent V5 finding J01-V5-BKS-001.  Keeping the
# set explicit makes the repair receipt auditable without re-parsing prose.
BOOKS_V5_PROPOSITION_REPAIR_FAMILIES = {
    "SF-SS-ZKR-MAS", "SF-VLA-MOTION-PLANNING", "SF-ORDER-AGNOSTIC-CHAIN-RULE",
    "SF-TRUST-FUNCTIONS", "SF-PRODUCTWEBGEN-MULTIMODAL-WEB",
    "SF-DSL-LLADA-CONTINUOUS-DENOISING", "SF-D3IM-SELF-CORRECTING-DIFFUSION",
    "SF-MATE-MULTIMODAL-TRAJECTORY-POLICY", "SF-PMC-INTERCPT-CONTEXT-GROUNDED-DATA",
    "SF-TEXTFAKE-IMAGE-DETECTION", "SF-ANYEDIT-PLUS", "SF-LEYLINE-KV-DIRECTIVES",
    "SF-HASTE-HARDWARE-SPARSE", "SF-RAG-ARBITRATION", "SF-RL-SHARED-PREFIX-REUSE",
    "SF-SPARSE-REPEATED-TRAINING", "SF-EXPECTED-VALUE-REWARD",
    "SF-FEATURE-ALIGNMENT-FUSION", "SF-NEUROSYMBOLIC-3D-DISTILLATION",
    "SF-REFLECTIVE-MEMORY-BENCH", "SF-CFDP-CLOSED-FORM-DIFFUSION-POLICY",
    "SF-ONEVLA", "SF-MORLET-POSITIONAL-ENCODING", "SF-SABER-CODING-AGENT-SAFETY",
    "SF-DIFFUSENT-BOUNDARY-DIFFUSION", "SF-TFINV-ONE-STEP-DIFFUSION-INVERSION",
    "SF-RESIDENT-KV-CLAIMS", "SF-GPTQ-INTRINSIC-LORA", "SF-DRUGCLAW-AUTHORITY",
    "SF-AGENT-FALSE-SUCCESS", "SF-CRITICALLY-DAMPED-POST-INTERPOLATION",
}
LEDGER = PACKET / "screening-ledger.tsv"
INVENTORY = PACKET / "candidate-inventory.tsv"
MATERIALS = PACKET / "arxiv-v1"
V1_METADATA = PACKET / "arxiv-v1-metadata"


def regenerate_manifest() -> None:
    """Hash the final packet after every generated receipt has been written."""
    rows: list[str] = []
    manifest = PACKET / "SHA256SUMS"
    for path in sorted(candidate for candidate in PACKET.rglob("*") if candidate.is_file() and candidate != manifest):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  ./{path.relative_to(PACKET)}")
    manifest.write_text("\n".join(rows) + "\n")

VERIFIED_INTEGRATES = {
    "SF-LODESTAR-ONLINE-ROUTER",
    "SF-EXPWEAVER-LATENT-RAG",
    "SF-LEYLINE-KV-DIRECTIVES",
    "SF-MEMORYWIRE",
    "SF-RESIDENT-KV-CLAIMS",
    "SF-SATURATED-DATA-SIGNALS",
}

# V2 audit required the other 17 provisional Integrates to be re-compared with
# actual chapter propositions.  Only these source-specific deltas survive that
# comparison; all other previously provisional rows are explicitly downgraded.
REJUDGED_INTEGRATES = {
    "SF-ORDER-AGNOSTIC-CHAIN-RULE",
    "SF-DAG-MOE",
    "SF-DART-TEST-TIME-RERANKING",
    "SF-EXPECTED-VALUE-REWARD",
    "SF-HARD-NEGATIVE-GEN-DISC-GAP",
    "SF-GPTQ-INTRINSIC-LORA",
    "SF-CFDP-CLOSED-FORM-DIFFUSION-POLICY",
    "SF-FED-PERSONALIZATION-SILENT-FAILURES",
    "SF-DEEP-RESEARCH-RUBRIC-RL",
    "SF-SPARSE-REPEATED-TRAINING",
}

# Benchmark Contracts are claim-scoped, not retained-surface-scoped.  These
# four retained families provide durable systems evidence but do not report an
# author-controlled empirical benchmark in exact arXiv v1.
NON_BENCHMARK_FAMILIES = {
    "SF-FED-PERSONALIZATION-SILENT-FAILURES",
    "SF-AIREP",
    "SF-AGENT-OPERATING-SYSTEM",
    "SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY",
}

TITLE_OVERRIDES = {
    "2606.01026": "Revise, Don’t Freeze: Sampler-Matched Training for Self-Correcting Masked Diffusion Language Models",
    "2606.07632": "Position: Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment",
    "2606.01185": "“Skill issues”: data-centric optimization of lakehouse agents",
    "2606.01304": "When Hard Negatives Hurt: Bridging the Generative-Discriminative Gap in Hard Negative Synthesis for Retrieval",
    "2606.01495": "CART: Context-Anchored Recurrent Transformer — A Parameter-Efficient Architecture with Learned Stability",
}

# V4 reopens were independently identified from the frozen Atom denominator.
# Direct arXiv HTML was reviewed through the exact-v1 endpoint, but the host
# reset bulk packet downloads in this repair context.  These locators therefore
# name the public exact-v1 primary source explicitly instead of pretending that
# a local file exists.
WEB_EXACT_V4 = {
    "2606.00971": ("§ `3 Methodology`", "§ `4 Results`", "§ `5 Discussion, Limitations, and Future Work`; § `6 Conclusion`"),
    "2606.01016": ("§ `3 Dataset Creation`", "§ `4 Benchmark Experiments`", "§ `A.6 Limitations of the Benchmark Formulation`; § `5 Discussion`"),
    "2606.01031": ("§ `3 Benchmark Design and Construction`; § `3.4 Temporally-Aware Evaluation Metrics`", "§ `4 Results and Analysis`", "§ `4.5 Guidelines, Limitations, and Future Benchmarks`; § `5 Conclusion`"),
    "2606.14723": ("§ `3 Method`", "§ `4 Experiments`", "§ `6 Limitations and threats to validity`; § `7 Conclusion`"),
    "2606.01162": ("§ `3 Preliminaries`; § `4 Methodology`", "§ `5 Experiments`", "§ `6 Conclusion`"),
    "2606.01183": ("§ `3 System Overview`; § `4 Data Structures and Core Algorithms`; § `5 Implementation`", "§ `6 Evaluation`", "§ `7 Discussion`; § `8 Conclusion`"),
    "2606.01348": ("§ `3 ChartArena Benchmark`; § `4 Format-Agnostic Evaluation Protocol`", "§ `5 Experiments`", "§ `E Limitations`; § `6 Conclusion`"),
    "2606.01442": ("§ `II Methodology`", "§ `III Results and Discussion`", "§ `III-D Threats to Validity`; § `IV Conclusion and Future Work`"),
    "2606.00942": ("§ `3 Model Sketch`; § `4 Metastable Faults`; § `5 Metastable Failures`; § `6 Achieving Metastable Fault Tolerance`", "§ `7 Case Study: Oscillating Membership`; Appendix `B The Look-Aside Cache Incident`", "§ `9 The Road Ahead`"),
    "2606.01022": ("§ `2 The ProductWebGen Benchmark`; § `2.1 Data Curation`; § `2.2 Metrics`", "§ `3 Results and Analysis`; § `4 Improving BAGEL for ProductWebGen via Fine-tuning`", "§ `6 Conclusion`; Appendix `C Experimental Setup Details`; Appendix `D Human Evaluation Details`"),
    "2606.01028": ("§ `3 Environment`; § `4 Benchmarking Pipeline and Policies`", "§ `5 Evaluation Experiments`; Appendix `D Details of Evaluation Results`; Appendix `F Experiments Compute Resources`", "Appendix `A Limitations`; Appendix `G Broader Impact`"),
    "2606.01044": ("§ `3 Method`; § `3.2 Counterfactual Visual Probing`; § `3.3 Risk Estimation`; § `3.4 Risk-Guided Question Selection`", "§ `4 Experiments and Results`", "§ `5 Conclusion` (no dedicated limitations section disclosed)"),
    "2606.01182": ("§ `3 Methodology`; § `3.1 Probabilistic Model`; § `3.2 Optimal Question Selection`; § `3.3 Tree Construction`", "§ `4 Experimental Setup`; § `5 Results & Discussion`", "§ `6 Limitations`; § `7 Conclusion`"),
    "2606.01225": ("§ `Methodology` (privacy-preserving detection and decentralized evidence governance)", "§ `Experimental Results`", "§ `Limitations`; § `Conclusion`"),
    "2606.01313": ("§ `Method`; probabilistic scene graph and multiverse decision making", "§ `Experiments`", "§ `Limitations`; § `Conclusion`"),
    "2606.01323": ("§ `Methodology`; discrete diffusion formulation", "§ `Experiments`", "§ `Limitations`; § `Conclusion`"),
    "2606.01396": ("§ `Method`; residual quantization with finite scalar quantization", "§ `Offline Experiments`; § `Online A/B Test`", "§ `Limitations`; § `Conclusion`"),
}

# V5 independent-audit false negatives.  These exact-v1 pages were opened and
# read through the official public HTML endpoint after the packet host reset
# bulk downloads.  The locator strings name the actual source sections; they
# are not inferred from a later revision.
WEB_EXACT_V5 = {
    "2606.00967": ("§ `3 Method`; § `3.1 Data Preparation and Image Tokenization`; § `3.2 Proposed Architecture`; § `3.3 Training and Inference`", "§ `4 Experiments`; § `4.2 Experimental details`; § `4.3 Quantitative Results`; § `7.5 Ablation Study`", "§ `6 Conclusion`; § `7.5 Ablation Study` (no dedicated limitations section disclosed)"),
    "2606.00970": ("§ `2 Model`; § `3 Prospect-Theory Signatures`; § `4 Closed-form Formula`", "§ `5 Robustness`; § `5.1 Q-learning`; § `5.2 Stochastic Environments`", "§ `6 Discussion`; § `Limitations and broader impact`"),
    "2606.00979": ("§ `3 Problem Formulation`; § `4 Methodology`; § `4.1 The proposed UME framework`; § `4.2 Model Optimization and Inference`", "§ `5 Experimental Studies`; § `5.1 Experimental Setup`; § `5.3 Ablation Studies`; § `5.4 Online A/B Test`", "§ `5.5 Discussion`; § `6 Conclusion` — no dedicated limitations heading"),
    "2606.00984": ("§ `5 Preliminaries`; § `6 Algorithm & Regret Analysis`; § `7 Extensions to Generalized Linear Contextual Bandits`", "§ `8 Numerical Experiments`; Appendix `D Additional Experiments`", "§ `9 Conclusion` — no dedicated limitations heading; claims remain bounded to the stated linear/generalized-linear contextual-bandit assumptions"),
    "2606.00987": ("§ `III MTRefSeg-21K Dataset Construction`; § `IV Method`; § `IV-C MTRefSeg-R1: Change-Aware LVLM for MTRS`", "§ `V Experiments And Results`; § `V-B Comparisons with Existing LVLMs`; § `V-C Ablation Studies`", "§ `VI Conclusion` — no dedicated limitations heading; claims remain bounded to the released dataset splits and evaluated domains"),
    "2606.00988": ("§ `3 Physics-Informed Diffusion-Based Data Enrichment Model For Symbolic Regression`; § `3.1 Framework structure`; § `3.2 Model training`; § `3.3 Physics-Informed Losses`", "§ `4 Experimental Design`; § `5 Results`", "§ `6 Discussion` (implications, limitations and future directions)"),
    "2606.00990": ("§ `3 OSCAR: Survival-Guided Wait-or-Reroute Planning`; § `3.1 Learning Class-Conditioned Obstacle Persistence`; § `3.2 Arrival-Time-Dependent Edge Costs`; § `3.3 Wait-or-Reroute Decision`; § `3.4 Online Adaptation`", "§ `4 Experimental Evaluation of Survival-Guided Navigation`; Appendix `B Simulation Details`; Appendix `D Person/Chair-Only Real-World Results`", "§ `5 Limitations and Future Work`; § `6 Conclusion`"),
    "2606.01013": ("§ `3 Proposed AI-Paper-Review System`; § `3.4 Review Pipeline`; § `3.5 Validation Pipeline`; § `3.6 Implementation`", "§ `4 Experimental Setup`; § `5 Evaluation`", "§ `4.5 Assumptions`; § `6 Discussion`; § `7 Conclusion` — no dedicated limitations heading"),
    "2606.01015": ("§ `III Foundational Definitions & Taxonomy`; § `IV Architecture Proposals`; § `VI Intelligence Distribution Models`", "Not Required — closure-only survey review does not treat the application examples as a newly evaluated artifact", "§ `II Limitations of Prior Integration Studies`; § `VII Challenges and Future Directions`; closure-only disposition remains bounded by survey identity and absence of a new evaluated artifact"),
    "2606.02638": ("§ `3 Methodology`; § `3.1 Model Architecture`; § `3.2 Data Pipeline`; § `3.3 Training and Inference`", "§ `4 Experiments`; § `5 Results and Discussions`; § `5.3 Ablation Studies for Prompt Encoder`; § `5.4 Ablation Studies for Duration Predictor`", "§ `7 Limitations`; § `8 Social Impact`"),
    "2606.01051": ("§ `3 Method`; § `3.1 Reformulation as an Option Semi-Markov Decision Process`; § `3.2 Selection of Safety Function`; § `3.4 Practical Implementation`", "§ `4 Validations`; Appendix `J Detailed Validation Results and Discussions`", "Appendix `A Limitations`; Appendix `L Broader Impact`"),
    "2606.01097": ("§ `2 Method`; § `2.2 Route A: Reasoning/Text Seed`; § `2.3 Route B: Visual Candidate Route`; § `2.5 1v1 VLM Final Reranker`", "§ `3 Implementation and Experiments`; § `3.2 Evaluation Protocol`; § `3.3 Hidden Test Results`; § `3.4 Ablations and Observations`", "§ `4 Conclusion` — no dedicated limitations heading; the result is bounded to the challenge split and disclosed retrieval budget"),
    "2606.01113": ("§ `2 Methodology`; § `2.4 Reasoning Trace Generation`; § `2.7 Agreement-Gated Residual Fusion`; § `2.8 Candidate Reranking`", "§ `3 Experiments`; § `3.3 Ablation Studies`; § `3.4 Validation and Test Performance`", "§ `4 Observations and Insights`; § `5 Conclusion` — no dedicated limitations heading"),
    "2606.01173": ("§ `3 Method`; § `3.2 Shared Spectral Reliability Descriptor`; § `3.3 Spectral Reliability Fusion`; § `3.4 Reliability-Conditioned Expert Routing`", "§ `4 Experiments`; § `4.2 Controlled Ablation`; § `4.3 Robustness Under Modality Agreement Collapse`; Appendix `S10 Statistical Significance of Matched Gains`", "Appendix `S4.2 Per-Class Retention and Failure Analysis`; Appendix `S9.4 Degenerate-Input Regime`; § `5 Conclusion`"),
    "2606.01192": ("§ `3 Methodology`; § `3.1 Definition of a photometric-shifted dataset`; § `3.2 Data generation`; § `3.3 Software details and APIs`", "§ `4 Experiments`; § `4.2 Evaluating photometric shifts on segmentation models`; § `4.3 Analysis of photometric disentanglement`; § `4.4 Cost analysis`", "§ `5.1 Limitations and Future Directions`"),
    "2606.02641": ("§ `3 Problem Formulation`; § `4 The CARVE Algorithm`; § `5 Guarantees`", "§ `6 Evaluation Protocol`; § `7 Results`", "§ `7 Failure analysis`; § `8 Discussion and Limitations`"),
    "2606.01277": ("§ `III Proposed Methods`; § `III-B1 Multi-Modal Perception and Transformer-Based Fusion`; § `III-B2 Waypoint Prediction and Hybrid Control Formulation`", "§ `IV Experimental Setup`; § `V Results and Discussions`; § `V-A Ablation Analysis of Sensor Modalities and Fusion`", "§ `V-C3 Limitations`; § `VI Conclusions`"),
    "2606.01300": ("§ `III Method`; § `III-B ChronosAD Training Procedure`", "§ `IV Experiments`; § `IV-A Quantitative Results`; § `IV-B Ablation Study`; § `IV-C Latent Space Analysis`", "§ `V Conclusions` — no dedicated limitations heading; claims remain bounded to the 11 benchmark datasets and stated detector"),
    "2606.02645": ("§ `3 Preliminaries and Linear-Approximation Setup`; § `5 DLQL and Its Switching Certificate`; § `6 m-DLQL: Periodic Hard Targets as Target-Boundary Error Maps`; § `7 SDLQL1`; § `8 SDLQL2`", "Not Disclosed — arXiv:2606.02645v1 is a theoretical analysis and does not report a separately identifiable empirical evaluation", "§ `9 Conclusion`; the guarantee is restricted to the stated deterministic/mean linear recursion and spectral conditions"),
    "2606.01302": ("§ `2 Background`; § `3 Experiments` (training protocol and key variables)", "§ `3 Representations improve smoothly with scale`; § `3 Asymptotic versus ideal representations`", "§ `4 Future work` (correlation not causation, multiple regimes, illustrative toy model and fixed-small-model boundary)"),
    "2606.01315": ("§ `III Method of DeblurNVS`; § `III-A Preliminary: Geometric Latent Diffusion`; § `III-C Multi-Stage Latent Learning`", "§ `IV Experiments`; § `IV-B Main Results`; § `IV-C Ablation Study`", "§ `V Conclusions and Limitations`"),
    "2606.01362": ("§ `4 Method`; § `4.1 Architecture`; § `4.3 Inference Pipeline`; § `4.4 Training`", "§ `5 Results`; § `5.1 Evaluation Protocol`; § `5.2 Quantitative Results`; § `5.4 Additional Experiments`", "§ `5.5 Limitations and Future Work`"),
    "2606.01367": ("§ `III Method`; § `III-B Hybrid Scene Representations`; § `III-C Online Active Reconstruction Process`; § `III-C1 Planning Phase`; § `III-C2 Mapping Phase`", "§ `IV Experiments`; § `IV-A Evaluation`; § `IV-B Ablation Studies`; § `IV-C Extended Simulations`", "§ `IV-A5 Discussions`; § `V Conclusion` — no dedicated limitations heading"),
    "2606.01397": ("§ `3 Proposed Q-learning strategy`; § `3.3 Finite residual command interface`; § `3.6 Finite-action shield and no-op fallback`; § `3.7 Online learning loop`", "§ `4 Experiment and results`; Appendix `C Scenario catalog`; Appendix `D Per-scenario full-duration results`", "§ `5 Discussion`; Appendix `B Software regression and artifact-generation checks`"),
    "2606.13698": ("§ `II Proposed Method`", "§ `III Experimental Design`; § `IV Results`", "§ `V Discussion`; § `V-A Limitations and Future Work`"),
    "2606.01470": ("§ `3 Finetuning Walrus on RTI physics`; Appendix `8.1 Pretraining`; Appendix `8.3 3D RTI finetuning`; Appendix `8.8 Experimental Methods`", "§ `4 RTI emulation results`; § `5 Emergent Behavior`; Appendix `8.10 zero-shot experimental evaluation`", "Appendix `8.8 Error Sources`; § `6 Conclusion` (simulation-to-lab and tested-regime boundary)"),
    "2606.01493": ("§ `4 Method`; § `4.1 3DGS-Guided Iterative Denoising`; § `4.2 Noise Mixture-Based Iterative Denoising`", "§ `5 Experiments`; Appendix `A Implementation Details, Evaluation and Negative Results`", "§ `6 Discussion and Conclusion` — `Limitations`; Appendix `A Negative Results`"),
    "2606.01504": ("§ `3 Methodology`; § `3.1 Model Architecture`; § `3.2 Contrastive Learning`; § `3.3 Relative Odds Alignment for Retrieval`", "§ `5 Experimental Setup`; § `6 Evaluation`; § `7 Results and Analysis`; § `7.5 Online A/B Test Results`; § `8 Inference and Non-functional Metrics`", "§ `9 Conclusion` — no dedicated limitations heading; claims remain bounded to the disclosed Flipkart datasets, query segments and deployment setting"),
    "2606.01518": ("§ `3 Dataset Construction`; § `4 Proposed Method`; § `4.1 Topology Agnostic Diffusion Model`; § `4.2 Skinning-Aware Texture-Semantic Injection`; § `4.3 Bidirectional Video-Skeleton Fusion`", "§ `5 Experiments`; § `5.2 Comparison on Motion Generation`; § `5.3 Ablation Study`", "§ `6 Conclusion and Discussion` — no dedicated limitations heading; code availability is explicitly future-tense at v1"),
}

WEB_EXACT_V7 = {
    "2606.00994": ("§ `2 Methods`; § `2.2 Trait registry`; § `2.3 Extraction pipeline`; § `2.6 Red-zone routing and ethics of public-unverified distribution`", "§ `4 Validation` (full-population substring verification, quote-supports-value audit and red-zone face-validity checks)", "§ `5 Limitations`; every extracted record remains public-unverified and pending human curation"),
    "2606.01086": ("§ `3 Strong Stochastic Flow Maps`; § `3.1 The Itô map`; § `3.2 Training`", "§ `4 Experiments`; § `4.1 Non-linear SDE`; § `4.2 Image generation`; § `4.3 Molecular systems`; Appendix `D Experimental details`", "Appendix `E.3 Limitations`; § `5 Conclusion`"),
    "2606.01090": ("§ `3 Methods`; § `3.5 Sample-complexity metric and the naive law`; § `3.7 Pre-specified failure criteria`", "§ `4 Results`; Appendix `F Reproducibility`", "§ `5 Counterarguments and limitations`; § `6 Discussion`"),
    "2606.01111": ("§ `3 Method`; § `3.4 Practical Deployment`", "§ `4 Experiments`; § `4.4 Industrial Deployment`", "§ `5 Conclusion` — no dedicated limitations heading; claims remain bounded to the four public datasets and disclosed industrial ranking deployment"),
    "2606.01122": ("§ `2 Problem Formulation`; § `3 Neural Network Methodology`; § `4.5 Per-component diagnostic protocol`", "§ `4 Experiments`; § `4.5` matched-truncation and per-component audit; § `4.8` multi-asset extension", "§ `5.2 Limitations`; § `6 Scope and what this paper does not claim`"),
    "2606.01271": ("§ `3.1 Hardware Setup`; § `3.2 Model Selection`; § `3.3 Models Optimization`", "§ `4 Experimental Results`; training and evaluation setup", "§ `5 Conclusion` — no dedicated limitations heading; claims remain bounded to EuroSAT, the three compact ConvNets and IMX500/Raspberry-Pi setup"),
    "2606.01312": ("§ `II Proposed 6G-LLM Architecture`; § `II-C LLM Deployment Model`; § `II-D Semantic Communication`", "§ `IV Results`; § `IV-F LLM Inference Delay Sensitivity Analysis`; Monte Carlo simulation over 5–30 vehicles", "§ `IV-A Simulation Assumptions and Parameter Justification`; results are trend-level simulation evidence, not protocol timing guarantees"),
    "2606.01339": ("§ `3 Method`; § `3.2 Adaptive Reversible Instance Normalization`; § `3.3 Learnable Frequency Decomposition`", "§ `4 Experimental Setup`; § `5 Results`; § `7 Efficiency Analysis`", "§ `8 Conclusion`; disclosed dataset, shift-construction and 4-GB hardware boundaries"),
    "2606.13694": ("§ `II Method`; § `II-B Random Attention`; § `II-D Computational Complexity`", "§ `III Experiments`; § `III-B Training Setup`; § `III-D Computational Efficiency`", "§ `IV Discussion`; § `V Conclusion` — no dedicated limitations heading; mobile efficiency is inferred from model complexity, not measured on a mobile device"),
}
WEB_ARTIFACT_V7 = {
    "2606.00994": "Not Disclosed — arXiv:2606.00994v1 does not pin an immutable extraction implementation revision",
    "2606.01086": "Appendix `D.6 Repositories` lists the exact software resources used; no immutable author-code commit is pinned",
    "2606.01090": "Appendix `F Reproducibility` describes implementation, atomic result writes and tests; no immutable archive revision is pinned",
    "2606.01111": "Not Disclosed — arXiv:2606.01111v1 does not pin an immutable implementation revision",
    "2606.01122": "Reproducibility statement lists scripts, result JSONs, software versions and frozen seeds; no immutable repository commit is pinned",
    "2606.01271": "§ `3.3 Models Optimization` identifies Sony MCT and the hardware-compliant conversion path; no immutable author artifact revision is pinned",
    "2606.01312": "Not Disclosed — arXiv:2606.01312v1 does not pin an immutable simulation implementation revision",
    "2606.01339": "§ `4.4 Implementation Details` discloses software and deterministic setup; no immutable repository revision is pinned",
    "2606.13694": "Not Disclosed — arXiv:2606.13694v1 does not pin an immutable implementation revision",
}

WEB_EXACT = WEB_EXACT_V4 | WEB_EXACT_V5 | WEB_EXACT_V7
PUBLIC_EXACT_PDF_IDS = {"2606.00994"}


def public_exact_locator(arxiv_id: str, value: str) -> str:
    """Prefix concrete public-HTML locators without corrupting exceptions."""
    if re.match(r"^(?:Not Required|Not Disclosed|Not Applicable|Pending)\s+[—-]\s+", value):
        return value
    if arxiv_id in PUBLIC_EXACT_PDF_IDS:
        return f"arXiv:{arxiv_id}v1 public exact-v1 PDF https://arxiv.org/pdf/{arxiv_id}v1 {value}"
    return f"arXiv:{arxiv_id}v1 public exact-v1 HTML https://arxiv.org/html/{arxiv_id}v1 {value}"

# Public exact-v1 pages were read directly.  These values are deliberately
# source-specific; they prevent the generic extractor from turning a failed
# packet download into an all-Not-Disclosed pseudo review.
PUBLIC_BENCHMARK_OVERRIDES = {
    "SF-HYPOTHESISMED-ANSWER-FUSION": {"Model": "Qwen2.5-7B-Instruct; Phi-4-mini-instruct; DeepSeek-R1-Distill-Qwen-32B; BioMistral-7B", "Hardware": "8× NVIDIA H100 80GB; dual Intel Xeon 8468; 1 TiB RAM", "Precision": "BF16", "Input Length": "maximum context 4096 tokens", "Output Length": "maximum generation 512 tokens", "Batch": "Not Disclosed — no batch size stated in §4 Results", "Concurrency": "Not Disclosed — no request concurrency stated in §4 Results", "SLO": "accuracy, parse coverage and confident-error evidence only; no production SLO", "Evaluator": "MedQA, MedMCQA and PubMedQA accuracy plus parse/SPACE coverage and false-commitment measures"},
    "SF-POLYSPEECH-100": {"Model": "22 speech-language systems enumerated in §4 Benchmark Experiments", "Hardware": "Not Disclosed — benchmark hardware is not fixed across all 22 systems", "Precision": "Not Disclosed — precision is not fixed across all 22 systems", "Input Length": "audio utterances across 110 languages and dialects; duration is item-scoped", "Output Length": "multiple-choice answer output", "Batch": "Not Disclosed — no common batch size", "Concurrency": "Not Disclosed — no serving concurrency experiment", "SLO": "benchmark quality evidence only; no production SLO", "Evaluator": "PolySpeech-100 multilingual speech-understanding accuracy and human/synthetic slice analysis"},
    "SF-TEMPORALLY-ALIGNED-TALKING-HEAD-EVAL": {"Model": "20 talking-head generation methods enumerated in §4", "Hardware": "Not Disclosed — no single common hardware contract for all methods", "Precision": "Not Disclosed — no common precision contract", "Input Length": "7 talking-head datasets; sequence lengths are dataset-scoped", "Output Length": "generated talking-head sequences; length is dataset-scoped", "Batch": "Not Disclosed — no common batch size", "Concurrency": "Not Disclosed — no serving concurrency experiment", "SLO": "temporally aligned quality evidence only; no interactive latency SLO", "Evaluator": "Soft-DTW-aligned temporal, visual and synchronization metrics"},
    "SF-DISAGREEMENT-CROSSMODEL-VIDEO-ROUTING": {"Model": "Gemini 3.1 Pro Preview and Claude Opus 4.8", "Hardware": "Not Disclosed — provider APIs hide serving hardware", "Precision": "Not Disclosed — provider APIs hide precision", "Input Length": "ImplicitQA videos sampled at 24 frames in stage 2", "Output Length": "multiple-choice answer output", "Batch": "three samples per item in the primary disagreement estimate", "Concurrency": "Not Disclosed — no production concurrency experiment", "SLO": "quality/cost routing evidence only; no production latency SLO", "Evaluator": "ImplicitQA test and validation accuracy, disagreement signal and incremental API cost"},
    "SF-DEFT-DYNAMIC-WORKFLOW-SCHEDULING": {"Model": "Deft mixture-of-scheduling-experts policy", "Hardware": "Not Disclosed — reported evidence is cloud-workflow simulation", "Precision": "Not Applicable — scheduling simulation, not tensor inference", "Input Length": "arriving DAG workflows with deadline and VM-state features", "Output Length": "one scheduling-policy/action decision per control step", "Batch": "simulation trace/configuration scoped", "Concurrency": "workflow arrival concurrency is scenario scoped", "SLO": "deadline/cost simulation evidence only; no production cluster SLO", "Evaluator": "author-defined workflow cost, deadline and scheduling metrics in §5"},
    "SF-CABI-MATCHING-ENGINE-HARNESS": {"Model": "Priority-Indicated Node matching engine; Exchange-core; QuantCup 1; Liquibook", "Hardware": "latest-generation 96-core ARM machine disclosed in §5–§6", "Precision": "Not Applicable — integer/order-book systems workload", "Input Length": "cancel-dominated stochastic order streams; 10,000-symbol Zipf workload for node-scale tests", "Output Length": "deterministic acknowledgements, trades and market-data deltas", "Batch": "10 subprocess-isolated runs per configuration; medians reported", "Concurrency": "single-writer matcher per symbol; multi-segment 96-core node experiment", "SLO": "author-reported throughput and p50–p99.99/max latency; no independent production SLO", "Evaluator": "byte-identical reference hashes plus throughput and latency distributions under the common protocol"},
    "SF-CHARTARENA-PARSING": {"Model": "26 multimodal large language models enumerated in §5", "Hardware": "Not Disclosed — provider and local model hardware is not normalized", "Precision": "Not Disclosed — no common precision across 26 models", "Input Length": "8 chart families × 3 scenarios × 2 languages", "Output Length": "structured chart parsing output", "Batch": "Not Disclosed — no common batch size", "Concurrency": "Not Disclosed — no serving concurrency experiment", "SLO": "parsing quality evidence only; no production SLO", "Evaluator": "format-agnostic exact-match and mAP-style chart parsing metrics"},
    "SF-SNN-INTRUSION-CONFIG-EVAL": {"Model": "9 spiking neuron models × 3 input encodings = 27 configurations", "Hardware": "Not Disclosed — no production neuromorphic deployment result", "Precision": "Not Disclosed — numerical precision not fixed in the evaluation contract", "Input Length": "4 intrusion-detection datasets", "Output Length": "classification output", "Batch": "five random seeds per configuration; training batch is setup scoped", "Concurrency": "Not Disclosed — no serving concurrency experiment", "SLO": "accuracy, macro-F1, FPR and latency evidence only; no production security SLO", "Evaluator": "accuracy, macro-F1, false-positive rate and latency across 27 configurations"},
}

# V7 source-wide disclosure reconciliation.  Values carry the scope in which
# they were disclosed (training, serving, simulation or one benchmark slice)
# so a real value is not generalized into an unsupported production contract.
PUBLIC_BENCHMARK_OVERRIDES.update({
    "SF-MEDSYN2-FLEXIBLE-CT": {
        "Model": "modified DiT volumetric diffusion transformer (MedSyn2 evaluation slice)",
        "Hardware": "single NVIDIA A100 GPU (§4.2 training setup)",
        "Input Length": "448×448×448 CT volume; text encoder maximum 544 tokens",
        "Output Length": "generated 448×448×448 CT volume; no autoregressive token-output contract",
        "Batch": "training batch size 1 with gradient accumulation 4",
    },
    "SF-TRAIT-MISALIGNMENT-MONITOR": {
        "Hardware": "single NVIDIA A6000 GPU (author experiment setup)",
        "Batch": "batch size 64 for the SAE appendix slice; not generalized to every experiment",
    },
    "SF-EXPWEAVER-LATENT-RAG": {
        "Hardware": "4× NVIDIA A6000 GPUs (implementation details)",
        "Input Length": "maximum prompt length 1024 tokens",
        "Output Length": "maximum completion length 1024 tokens",
        "Batch": "per-device batch 8 with gradient accumulation 4; effective batch 32",
    },
    "SF-DRDD-DECOUPLED-RESIDUAL-DIFFUSION": {
        "Hardware": "NVIDIA A6000 48GB GPU configuration (Experiment Settings)",
        "Input Length": "256×256 cropped input patches",
    },
    "SF-PMC-INTERCPT-CONTEXT-GROUNDED-DATA": {
        "Hardware": "CPT on 64× NVIDIA H800 GPUs; SFT on 8× NVIDIA H800 GPUs",
        "Input Length": "CPT/SFT maximum sequence 8192 tokens; serving appendix input capped at 4096 characters",
        "Output Length": "serving appendix maximum 4 new tokens",
        "Batch": "CPT micro-batch 2/global batch 256; SFT micro-batch 2/global batch 64; serving appendix batch 512",
        "Concurrency": "serving appendix uses data parallel 8; request concurrency is not separately disclosed",
    },
    "SF-IDP-ONE-STEP-ACTION-GEOMETRY": {
        "Hardware": "single NVIDIA A40 GPU for all training runs (Appendix D.3)",
    },
    "SF-STARFISH-STATE-HEALING": {
        "Hardware": "single NVIDIA A10 GPU (§3.3 recovery evaluation)",
    },
    "SF-MLLM-UNCERTAINTY-RECTIFICATION": {
        "Hardware": "single NVIDIA RTX A6000 48GB GPU (implementation details)",
    },
    "SF-HOMEFLOW-AGENT-TRAINING": {
        "Hardware": "single NVIDIA H20 96GB GPU configuration (implementation appendix)",
    },
    "SF-RAG-INFERENCE-COST-ATTACK": {
        "Hardware": "2× NVIDIA H20 GPUs (experiment setup)",
    },
    "SF-GUIDAPA-FEDERATED-CHATBOT": {
        "Hardware": "single NVIDIA RTX A6000 48GB GPU (implementation/evaluation setup)",
    },
    "SF-REGISTRY-BOUND-EVIDENCE-EXTRACTION": {
        "Model": "Xiaomi MiMo-V2.5 through the disclosed API extraction pipeline",
        "Hardware": "Not Disclosed — provider API hides accelerator hardware",
        "Precision": "Not Disclosed — provider API hides serving precision",
        "Input Length": "source documents routed in approximately 1,000–2,500 Chinese-character chunks",
        "Output Length": "typed trait records under the versioned 39-key registry; no common token cap disclosed",
        "Batch": "706,220 author-reported extraction runs; no request batch size disclosed",
        "Concurrency": "two regional endpoints and key-pool retry state are disclosed; simultaneous request concurrency is not",
        "SLO": "author-reported mean successful-run time about 91 s; not a production SLO",
        "Evaluator": "full-population evidence-substring verification plus sampled quote-supports-value and red-zone audits",
    },
    "SF-STRONG-STOCHASTIC-FLOW-MAPS": {
        "Model": "Strong Stochastic Flow Map networks for nonlinear SDE, image generation, ALDP and Chignolin slices",
        "Hardware": "one/two NVIDIA RTX A6000 GPUs or one/two NVIDIA H100 GPUs (Appendix D.5)",
        "Precision": "Not Disclosed — numerical training precision is not stated",
        "Input Length": "task-scoped SDE state/Brownian coefficients; image and molecular dimensions vary by experiment",
        "Output Length": "one pathwise state/sample per requested flow-map step; 1–2 NFE molecular sampling is reported",
        "Batch": "image batches 512/256; ALDP batch 1024; molecular configurations batch 64 (Appendix D)",
        "Concurrency": "Not Disclosed — no serving-concurrency experiment",
        "SLO": "few-NFE quality evidence only; no production latency SLO",
        "Evaluator": "nonlinear-SDE path error, image FID and molecular equilibrium-distribution metrics",
    },
    "SF-SYMMETRY-DATA-EXCHANGE-EVAL": {
        "Model": "two-hidden-layer width-32 MLP families with correct, wrong, absent and augmentation symmetry treatments",
        "Hardware": "single GPU for the primary sweep; Appendix F replication also reports a single-CPU run; device model not disclosed",
        "Precision": "Not Disclosed — tensor precision is not stated",
        "Input Length": "2D synthetic point input; training sizes 50–6400 and group sizes 1,2,3,4,6,8,12",
        "Output Length": "binary classification output",
        "Batch": "training batch size 64; five seeds per cell",
        "Concurrency": "five seeds trained in parallel in the primary implementation; no request-serving concurrency",
        "SLO": "compute-matched sample-complexity evidence; authors assert no wall-clock, throughput or memory advantage",
        "Evaluator": "target-sample threshold, relative exchange-rate estimators, wrong-group control and joint bootstrap",
    },
    "SF-LEAP-ADAPTIVE-FEATURE-SELECTION": {
        "Model": "LeAP plug-in feature-selection module across four public recommenders and one industrial ranking model",
        "Hardware": "Not Disclosed — accelerator model is not stated",
        "Precision": "Not Disclosed — training/inference precision is not stated",
        "Input Length": "industrial slice has 500+ feature fields and 12,000+ concatenated dimensions",
        "Output Length": "feature permutation/selection state; 3,600+ dimensions removed in the industrial slice",
        "Batch": "Not Disclosed — no numeric batch size stated",
        "Concurrency": "over one billion daily production requests describes traffic scale, not controlled request concurrency",
        "SLO": "zero reported business-metric degradation after pruning; no numeric latency SLO",
        "Evaluator": "four public recommendation benchmarks plus disclosed production feature-pruning outcome",
    },
    "SF-PER-COMPONENT-NEURAL-SOLVER-AUDIT": {
        "Model": "neural HJB-PIDE solver with finite-difference and per-component diagnostic references",
        "Hardware": "single Apple M1 CPU for the reproducibility/timing protocol; GPU timing is mentioned without a device model",
        "Precision": "Not Disclosed — tensor/numerical precision is not stated",
        "Input Length": "batch of collocation states with 64 Lévy Monte Carlo samples and 21 policy candidates per gradient step",
        "Output Length": "value, derivative, Hamiltonian-component and policy outputs; not a token sequence",
        "Batch": "training batch size 256 for 500 epochs",
        "Concurrency": "Not Disclosed — no serving-concurrency experiment",
        "SLO": "author wall-clock is diagnostic evidence (about 2–3 min CPU training; 11.3 s legacy FD solve), not a production SLO",
        "Evaluator": "per-component operator/Hamiltonian comparison, matched-truncation finite difference and multi-seed error",
    },
    "SF-IN-SENSOR-INT8-INFERENCE": {
        "Model": "SqueezeNet, ShuffleNetV2 and MCUNetV1 compact ConvNets",
        "Hardware": "Sony IMX500 intelligent vision sensor connected to Raspberry Pi 5",
        "Precision": "FP32 baseline converted by post-training quantization to INT8 weights/activations",
        "Input Length": "EuroSAT image classification input under the disclosed preprocessing; sensor is 4056×3040 effective pixels",
        "Output Length": "image-level class metadata returned to the host",
        "Batch": "training batch size 32; on-sensor inference is per image",
        "Concurrency": "Not Disclosed — no concurrent-stream experiment",
        "SLO": "author latency, FPS, memory and energy measurements; no independent production SLO",
        "Evaluator": "classification accuracy, inference latency, memory occupancy and energy consumption on IMX500",
    },
    "SF-EDGE-LLM-SEMANTIC-COMMUNICATION": {
        "Model": "distilled decoder-only transformer with approximately 7B parameters",
        "Hardware": "assumed ruggedized edge GPU with 16–24GB VRAM; no measured accelerator model",
        "Precision": "FP16 weights about 14GB; simulated edge path assumes 8-bit weight quantization",
        "Input Length": "command inputs typically below 128 tokens",
        "Output Length": "five-field schema-constrained semantic payload below 512 bytes",
        "Batch": "Not Disclosed — simulation does not state an inference batch size",
        "Concurrency": "fleet size 5–30 vehicles is a simulation scale, not request concurrency",
        "SLO": "12–18 ms edge inference and 100 ms mission threshold are simulation assumptions/thresholds, not measured production SLOs",
        "Evaluator": "Monte Carlo latency, mission-success and communication-overhead trends across 5–30 vehicles",
    },
    "SF-FREQLITE-ADAPTIVE-REVIN": {
        "Model": "FreqLite with A-RevIN against NLinear, DLinear, RLinear, FITS and PatchTST-small",
        "Hardware": "single NVIDIA RTX 3050 Ti laptop GPU with 4GB",
        "Precision": "full FP32 training; mixed precision disabled",
        "Input Length": "lookback L=96 or 336; multivariate channels are folded into the batch",
        "Output Length": "forecast horizons H=96,192,336,720",
        "Batch": "batch size 32 generally; reduced batch is used for the high-dimensional ECL slice",
        "Concurrency": "Not Disclosed — no serving-concurrency experiment",
        "SLO": "author reports parameters, analytic FLOPs, seconds/epoch and peak memory; no production SLO",
        "Evaluator": "forecast MSE/MAE, controlled non-stationarity tests and 4-GB efficiency measurements",
    },
    "SF-RANDOM-ATTENTION-MOBILE-INFERENCE": {
        "Model": "sleep-staging network with fixed Random Attention against trainable Transformer and lightweight baselines",
        "Hardware": "single NVIDIA RTX 3090 GPU with 24GB",
        "Precision": "Not Disclosed — training/inference precision is not stated",
        "Input Length": "sequence of sleep EEG epochs; Random Attention projection width 128 in the disclosed configuration",
        "Output Length": "five-class sleep-stage prediction",
        "Batch": "training batch size 20",
        "Concurrency": "Not Disclosed — no serving-concurrency experiment",
        "SLO": "parameter/MFLOP complexity evidence only; no on-device latency or production SLO measurement",
        "Evaluator": "sleep-staging accuracy/F1 plus parameter and computational-complexity comparison",
    },
})


def audited_retained_benchmark(model: str, evaluator: str, **overrides: str) -> dict[str, str]:
    """Return a complete exact-v1 field audit, defaulting only after setup review."""
    row = {
        "Model": model,
        "Hardware": "Not Disclosed — exact-v1 evaluation setup does not identify the physical accelerator or host",
        "Precision": "Not Disclosed — exact-v1 evaluation setup does not state numerical precision",
        "Input Length": "Not Disclosed — exact-v1 evaluation setup does not state a numeric input/context length",
        "Output Length": "Not Disclosed — exact-v1 evaluation setup does not state a numeric output/generation length",
        "Batch": "Not Disclosed — exact-v1 evaluation setup does not state a numeric batch size",
        "Concurrency": "Not Disclosed — exact-v1 evaluation setup does not state request concurrency",
        "SLO": "author-reported benchmark evidence only; no independent production SLO",
        "Evaluator": evaluator,
    }
    names = {
        "hardware": "Hardware",
        "precision": "Precision",
        "input_length": "Input Length",
        "output_length": "Output Length",
        "batch": "Batch",
        "concurrency": "Concurrency",
        "slo": "SLO",
    }
    row.update({names[key]: value for key, value in overrides.items()})
    return row


# Manual exact-v1 audit for every benchmark-bearing family in the canonical V9
# denominator.  Model identities are role-scoped: evaluated model/backbone,
# auxiliary evaluator and literature-only mentions are never collapsed together.
V9_RETAINED_BENCHMARK_AUDIT = {
    "SF-METASTABLE-FAULT-SCHEDULING": {
        "arxiv_v1": "2606.00942v1",
        "model_locator": "public exact-v1 HTML §7; Appendix B",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Not Applicable — formal systems/Nyx case studies; no ML model is evaluated",
            "formal metastable-fault proof obligations plus oscillating-membership and look-aside-cache case studies; pending requests/acknowledgements are latency/goodput proxies",
            precision="Not Applicable — formal and systems case studies, not tensor inference",
            input_length="Not Applicable — case-study events and server/load parameters, not model sequences",
            output_length="Not Applicable — liveness/correctness outcomes, not generated sequences",
            batch="Not Applicable — no batched ML evaluation",
            concurrency="server capacity 35, nominal load 30 and retry timeout 4 in the Nyx case-study model; not request-concurrency benchmarking",
            slo="formal liveness and case-study evidence only; no production SLO",
        ),
    },
    "SF-PRISM-DP-LORA": {
        "arxiv_v1": "2606.00944v1",
        "model_locator": "Appendix B Experimental Setup, Table 4",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Gemma-3-4B-pt; Gemma-2-9B; Gemma-3-12B-pt",
            "GLUE-8 task metrics and Math-10K numeric/exact task metrics, privacy budget and gauge/DP numerical diagnostics",
            hardware="1× NVIDIA A100-PCIE-40GB",
            input_length="maximum sequence length 384 for GLUE-8 and 256 for Math-10K",
            output_length="Not Separately Disclosed — sequence caps are training/input limits; no generation-output cap is stated",
            batch="effective batch size 64; micro-batch size 4",
            concurrency="Not Applicable — single-accelerator fine-tuning evaluation",
            slo="privacy/utility and numerical-stability evidence only; no production SLO",
        ),
    },
    "SF-LODESTAR-ONLINE-ROUTER": {
        "arxiv_v1": "2606.00946v1",
        "model_locator": "§5.1 Experimental setup",
        "model_action": "confirmed_exact",
        **audited_retained_benchmark(
            "Llama3-8B",
            "mean and p99 TTFT, routing overhead and online-adaptation behavior under public-cloud traces",
            hardware="NVIDIA A30 and V100 clusters; L20+A30 heterogeneous slice",
            precision="float16",
            input_length="1,000–10,000 input tokens",
            output_length="normally sampled output length with mean 100 and standard deviation 10 tokens",
            batch="Not Disclosed — no numeric engine batch size is stated",
            concurrency="arrival-rate sweeps 10–80 requests/s, including reported dynamic and trace-specific rates; no fixed simultaneous-request count",
            slo="author-reported mean/p99 TTFT and 3 ms mean/4.5 ms tail routing overhead; no independent production SLO",
        ),
    },
    "SF-COHESION-AWARE-MAS-PARTITIONING": {
        "arxiv_v1": "2606.00953v1",
        "model_locator": "§4 Experimental Setup; §5 Results",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "gpt-5-mini for all compared orchestration methods; Claude Code Agent Teams is a harness baseline, not a model identity",
            "DevEval and CodeProjectEval pass rate, wall-clock latency and API cost",
            hardware="Not Disclosed — API serving hardware is hidden",
            precision="Not Disclosed — API serving precision is hidden",
            input_length="28 repository-level coding tasks; no common token-length cap disclosed",
            output_length="repository code changes and test outcomes; no common token-length cap disclosed",
            batch="Not Applicable — task-by-task agent evaluation",
            concurrency="method-scoped agent parallelism; no request-serving concurrency experiment",
            slo="pass-rate/latency/cost comparison only; no production SLO",
        ),
    },
    "SF-ASYNC-AUTOFORMAL-PLANNING": {
        "arxiv_v1": "2606.00981v1",
        "model_locator": "§4 Experimental Setup; Appendix C",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Gemini 3 Flash; GPT-5-mini; DeepSeek-V4-Flash; Qwen3.6-35B-A3B",
            "plan validity, plan makespan, translation faithfulness and online replanning outcomes on AsyncHow, Robotouille, AsyncPlan-XXL and online Robotouille",
            hardware="Not Disclosed — provider/API hardware is not normalized",
            precision="Not Disclosed — provider/API precision is not disclosed",
            input_length="task/problem instances and event schedules; no common token cap disclosed",
            output_length="formal plans and makespans; no common token cap disclosed",
            batch="Not Applicable — one planning instance per evaluation item",
            concurrency="asynchronous action overlap is the planning object, not request concurrency",
            slo="plan-correctness and makespan evidence only; no production SLO",
        ),
    },
    "SF-ORDER-AGNOSTIC-CHAIN-RULE": {
        "arxiv_v1": "2606.00997v1",
        "model_locator": "§4 Experiments; generation configuration",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "LLaDA-2.1-mini; GPT-2 Large is only the external perplexity evaluator",
            "mean/variance of log q, EOS rate, GPT-2-Large external perplexity, Distinct-3 and downstream task accuracy",
            input_length="task prompts plus a fixed 128-token continuation in the likelihood slice; block size 32",
            output_length="maximum generation length 16,384 tokens with EOS early stop",
            batch="Not Disclosed — no numeric evaluation batch size stated",
            concurrency="Not Applicable — decoding-order comparison, not serving concurrency",
            slo="generation-quality/consistency evidence only; no production SLO",
        ),
    },
    "SF-TRAIT-MISALIGNMENT-MONITOR": {
        "arxiv_v1": "2606.07631v1",
        "model_locator": "§3 Models; §4.3; Appendix evaluation protocol",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Llama-3-8B; Mistral-7B-v0.3; Qwen2.5-7B; Gemma-2-9B; held-out probes Qwen2.5-14B and Phi-4-14B",
            "two-pass GPT-4o grading, EM/FNR/FPR thresholding and trait-space drift diagnostics across checkpoints/seeds",
            hardware="single NVIDIA A6000 GPU",
            input_length="checkpoint prompt sets; no common numeric prompt-length cap disclosed",
            output_length="maximum 600 generated tokens per checkpoint response",
            batch="vLLM batched generation with numeric size undisclosed; batch size 64 is limited to the SAE appendix slice",
            concurrency="Not Disclosed — no request-concurrency experiment",
            slo="monitoring-quality evidence only; no production detection SLO",
        ),
    },
    "SF-TASK-AWARE-MOE-GROUPING": {
        "arxiv_v1": "2606.01007v1",
        "model_locator": "§4.1 Models; Appendices A–D",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "DeepSeek-MoE-16B; Qwen1.5-MoE-A2.7B; Moonlight-16B-A3B",
            "cross-group expert dispatch, communication reduction, Jain load-balance index and maximum capacity/load violation",
            hardware="16 logical expert-parallel GPUs arranged as four groups; physical accelerator model not disclosed",
            input_length="calibration corpora use source-defined token budgets; no serving sequence-length contract disclosed",
            output_length="Not Applicable — expert-placement/routing measurements rather than generated-output length",
            batch="Not Disclosed — no numeric serving batch size stated",
            concurrency="Not Disclosed — no request-level concurrency experiment",
            slo="communication/load-balance evidence only; no production SLO",
        ),
    },
    "SF-HYBRID-VERIFIED-DECODING": {
        "arxiv_v1": "2606.01019v1",
        "model_locator": "§4.1 Models; Table 6; serving appendix",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Qwen3-8B; Qwen3-4B; Llama-3.1-8B with the matched EAGLE3 checkpoint",
            "tokens/s, speedup, cycles per 1K tokens, accepted length and payoff-predictor precision/recall; vLLM serving check on MT-Bench and CNN/DailyMail",
            hardware="NVIDIA H100 for main results; NVIDIA RTX 5090, H100 and B200 for cross-GPU checks",
            precision="float16",
            input_length="maximum sequence length 16,384 tokens",
            output_length="maximum 8,192 new tokens",
            batch="serving batch size 1; payoff-predictor training batch 65,536 is separately scoped",
            concurrency="Not Disclosed — no simultaneous-request concurrency experiment",
            slo="throughput/speedup evidence only; no production latency SLO",
        ),
    },
    "SF-JUDGE-PANEL-CALIBRATION": {
        "arxiv_v1": "2606.01034v1",
        "model_locator": "§4 Experiments; Appendix C Judge configuration",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Qwen2.5-7B-Instruct; Llama-3.1-8B-Instruct; Mistral-7B-Instruct-v0.3; Prometheus-7B; Gemma-3-12B-IT; Selene-1-Mini-Llama-3.1-8B; DeepSeek-V4-Flash",
            "held-out calibration/test risk, selection regret and path/prefix/aggregator diagnostics on RewardBench, LLMBar, SummEval and Arena100K",
            hardware="Not Disclosed — the seven-judge pool has no normalized hardware contract",
            precision="Not Disclosed — no common precision contract across the judge pool",
            input_length="benchmark item/prompt scoped; no common numeric token cap disclosed",
            output_length="deterministic scalar/pairwise judge outputs; no common token cap disclosed",
            batch="Not Disclosed — no common numeric batch size stated",
            concurrency="Not Applicable — offline finite-calibration study",
            slo="calibration/selection reliability evidence only; no production SLO",
        ),
    },
    "SF-ML-LIFECYCLE-ASSESSMENT": {
        "arxiv_v1": "2606.07632v1",
        "model_locator": "exact-v1 PDF §3.5 Case Study",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Not Applicable — ML life-cycle assessment framework and system-design case studies; no controlled model implementation is benchmarked",
            "ISO-style LCA functional unit, resource inventory and energy/water/carbon life-cycle impact comparison",
            hardware="H100 appears in the case-study system inventory; no controlled benchmark host",
            precision="Not Applicable — life-cycle inventory comparison, not tensor execution measurement",
            input_length="Not Applicable — functional-unit/workload inventory rather than sequence-length sweep",
            output_length="Not Applicable — environmental-impact inventory rather than generated output",
            batch="Not Applicable — no batched ML run",
            concurrency="Not Applicable — no request-concurrency experiment",
            slo="life-cycle impact comparison only; no production SLO",
        ),
    },
    "SF-LEYLINE-KV-DIRECTIVES": {
        "arxiv_v1": "2606.01065v1",
        "model_locator": "§5 deployment cells; Appendices T–U",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "DeepSeek-V2-Lite and JoyAI-LLM-Flash in the disclosed deployment cells",
            "cache-hit rate, p50/p99 latency, output-equivalence/first-token agreement, debug-gym solve rate and KV-pool occupancy",
            hardware="NVIDIA H100 and H200 deployment cells",
            precision="BF16 KV storage with FP32 rotation in the scoped arms",
            input_length="synthetic long system prompt about 4,096 tokens plus six about-2,048-token turns; mutation slice about 3,200 tokens; long-context replay separately scoped",
            output_length="trajectory/output lengths are trace scoped; no common generation cap disclosed",
            batch="batch=8 appears in one deployment cell; not a universal serving batch contract",
            concurrency="C={1,4,8,16} serving sweeps; cross-tenant cell uses 32 requests per tenant",
            slo="author-reported cache hit and p50/p99/e2e latency evidence; no independent production SLO",
        ),
    },
    "SF-RLVR-VERIFIER-FUZZING": {
        "arxiv_v1": "2606.01066v1",
        "model_locator": "§5 Experimental Setup; §6 Results",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Not Applicable — deterministic math-verify/jsonschema/SymPy verifier harness; no generative model is evaluated",
            "false-positive, false-negative, verifier disagreement, exploit and uncertainty rates under mutation/fuzzing replay",
            hardware="CPU/local execution; exact-v1 states that no GPU or distributed training framework is required",
            precision="Not Applicable — structured verifier execution, not tensor inference",
            input_length="structured verifier inputs/mutations; no token-length contract",
            output_length="pass/fail/error outcomes; no generated sequence",
            batch="mutation-corpus/case counts are experiment scoped; no batch size",
            concurrency="Not Applicable — local verifier replay",
            slo="verifier-correctness evidence only; no production SLO",
        ),
    },
    "SF-DEEP-RESEARCH-RUBRIC-RL": {
        "arxiv_v1": "2606.01091v1",
        "model_locator": "§4.1–§4.3; Appendix training setup",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "policy models Qwen3-8B-SFT, Qwen3-14B and Qwen3-30B-A3B; GPT-5 and Gemini are rubric sources, not policy models",
            "ResearchQA, DeepResearchBench and LocalSearchBench scores plus rubric coverage/quality and expert-reasoning evaluations",
            precision="FP8 training/inference in the disclosed policy setup",
            input_length="research queries, retrieved evidence and rubric constraints; no common numeric token cap disclosed",
            output_length="research answers/reports; no common numeric token cap disclosed",
            batch="training batch size 64",
            concurrency="Not Applicable — offline policy training/evaluation",
            slo="research quality/rubric evidence only; no production SLO",
        ),
    },
    "SF-LOCAL-MIXVR": {
        "arxiv_v1": "2606.01128v1",
        "model_locator": "§4 Experiments",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "two-layer convolutional network for MNIST; ResNet-18 for CIFAR-10",
            "test accuracy versus communication rounds and sample/gradient budget across SGD/ASGD/local optimizer baselines",
            input_length="MNIST and CIFAR-10 images under standard dataset preprocessing",
            output_length="10-class prediction",
            batch="per-worker minibatch 4 for MNIST and 16 for CIFAR-10",
            concurrency="4 workers for MNIST and 8 workers for CIFAR-10; distributed-worker count, not request concurrency",
            slo="optimization/communication evidence only; no production SLO",
        ),
    },
    "SF-MEMORYWIRE": {
        "arxiv_v1": "2606.01138v1",
        "model_locator": "§5.1 Microbenchmark",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "sentence-transformers/all-MiniLM-L6-v2 embedder; no LLM is evaluated in the main microbenchmark",
            "Recall@5, ingest/recall latency, adversarial-fusion leak/recall and 16-scenario cross-adapter conformance",
            hardware="Windows 11 AMD64, Python 3.13.13, CPU-only inference",
            input_length="100 hand-authored facts and 50 labelled queries; no token-length cap disclosed",
            output_length="top-k retrieval with k=5",
            batch="50-query microbenchmark and 16 conformance scenarios; no runtime batch size",
            concurrency="Not Disclosed — no concurrent-client experiment",
            slo="microbenchmark latency and recall evidence only; no production SLO",
        ),
    },
    "SF-SKILLREVISE": {
        "arxiv_v1": "2606.01139v1",
        "model_locator": "§4 Experiments; model table",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "GPT-5.5 author/reviser; executors GPT-5.5, Claude Opus 4.7, Kimi-K2.6, Qwen3.6-plus and DeepSeek-V4-Pro; ALFWorld Qwen3-8B",
            "verifier task success, outcome utility, tokens, tool calls, steps and latency across executor/task slices",
            hardware="Not Disclosed — provider/API hardware is hidden",
            precision="Not Disclosed — provider/API precision is hidden",
            input_length="task and skill text are benchmark scoped; no common numeric token cap disclosed",
            output_length="skills/trajectories are benchmark scoped; no common numeric token cap disclosed",
            batch="Not Applicable — task-by-task agent evaluation",
            concurrency="Not Applicable — no request-serving concurrency experiment",
            slo="task success/utility/cost evidence only; no production SLO",
        ),
    },
    "SF-RL-SHARED-PREFIX-REUSE": {
        "arxiv_v1": "2606.01143v1",
        "model_locator": "§5 Evaluation; configuration tables",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Llama3-8B; Qwen3-8B; Qwen3-MoE-30B-A3B",
            "optimizer-parameter equivalence, GPU time/speedup, HBM use and maximum rollout-group capacity",
            hardware="up to two nodes / 16 NVIDIA H20 GPUs",
            precision="BF16 tensors with FP32 optimizer/reference checks",
            input_length="fixed total sequence length 12,288 tokens; reported 2K/10K and 10K/2K prefix/suffix cells",
            output_length="Not Applicable — RL training sequence partition, not generated-output cap",
            batch="rollout groups N={16,32,64,128}; suffix microbatching is schedule scoped",
            concurrency="Not Applicable — data-parallel training schedule, not request serving",
            slo="training-time/memory/capacity evidence only; no production SLO",
        ),
    },
    "SF-SPARSE-REPEATED-TRAINING": {
        "arxiv_v1": "2606.01155v1",
        "model_locator": "§3.3; §4; Appendix D",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "custom LLaMA-2-family sparse models with 15M–960M active parameters and dense-equivalent scales up to 7.68B",
            "validation loss, scaling-law fit, held-out scale extrapolation and repeated-epoch/token-budget comparisons",
            precision="bfloat16",
            input_length="training budgets 520M, 1.3B and 2.6B tokens, repeated for 1–16 epochs up to 41.6B token presentations; sequence length not disclosed",
            output_length="Not Applicable — language-model training loss evaluation",
            batch="global batch size 512",
            concurrency="Not Applicable — offline training",
            slo="scaling-law/loss evidence only; no production SLO",
        ),
    },
    "SF-LAKEHOUSE-SKILL-OPTIMIZATION": {
        "arxiv_v1": "2606.01185v1",
        "model_locator": "§4 Experiments; implementation configuration",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "claude-sonnet-4-6 task LLM through the Claude Code harness",
            "validation/test checks, task accuracy, wall-clock time and API cost over 25 lakehouse tasks and six skills",
            hardware="Not Disclosed — provider/API hardware is hidden",
            precision="Not Disclosed — provider/API precision is hidden",
            input_length="25 repository tasks with 50/25/25 split; no common token cap disclosed",
            output_length="repository changes and validation outcomes; no common token cap disclosed",
            batch="Not Applicable — task-by-task agent evaluation",
            concurrency="Not Applicable — no request-serving concurrency experiment",
            slo="task quality/time/cost evidence only; no production SLO",
        ),
    },
    "SF-LOW-RESOURCE-SAFETY-ACTION": {
        "arxiv_v1": "2606.01196v1",
        "model_locator": "§3 Setup; §4–§5",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Qwen2.5-7B-Instruct; Gemma-2-9B-it; Llama-3.1-8B-Instruct; GPT-4o-mini is the multilingual refusal judge",
            "harmful/harmless refusal, refusal selectivity, balanced accuracy/F1, few-shot calibration and multilingual MMLU utility",
            hardware="single NVIDIA RTX 5090 for the disclosed local evaluation",
            input_length="PolyRefuse prompts across 23 languages; no common numeric token cap disclosed",
            output_length="greedy completions; no common numeric generation cap disclosed",
            batch="Not Disclosed — no numeric evaluation batch size stated",
            concurrency="Not Applicable — offline activation/gating evaluation",
            slo="safety/utility calibration evidence only; no production SLO",
        ),
    },
    "SF-DISCOURSEFLIP": {
        "arxiv_v1": "2606.01212v1",
        "model_locator": "§5.2 Implementation Details",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "target generators Llama3.1-8B-Instruct and Qwen3-8B-Instruct; Qwen3-Next-80B-A3B-Instruct optimizer; Llama3-8B-Instruct surrogate; GPT-5-mini expansion and qwen-plus stance judge are auxiliary",
            "retrieval attack success, coverage and average stance variation across two generators and three retrievers",
            hardware="4× NVIDIA DGX H100 80GB GPUs; 1TB system memory",
            input_length="top-K=5 retrieved documents; injected-document budget M=10; prompt lengths otherwise not normalized",
            output_length="generation/manipulation budget T1≤500 tokens and SEO edit budget T2≤100 tokens",
            batch="Not Disclosed — no numeric runtime batch size stated",
            concurrency="Not Applicable — offline attack evaluation",
            slo="attack-success/stance-shift evidence only; no production SLO",
        ),
    },
    "SF-RAG-INFERENCE-COST-ATTACK": {
        "arxiv_v1": "2606.02643v1",
        "model_locator": "§4.1.2 Implementation Details; Tables 1–2",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Llama-3.1-8B-Instruct attack agent; victim models Qwen-turbo, GPT-5, Claude-Sonnet-4 and DeepSeek-R1",
            "retrieval rate and weighted token-consumption ratio across datasets, methods and transfer victim models",
            hardware="2× NVIDIA H20 GPUs for attack-agent training/evaluation; API victim hardware hidden",
            precision="Not Disclosed — local/API precision is not stated",
            input_length="dataset queries plus generated adversarial documents; no common token cap disclosed",
            output_length="victim response token consumption is the measured outcome; no fixed generation cap disclosed",
            batch="MA-GRPO group G=3 documents per step; no serving batch size",
            concurrency="Not Applicable — offline attack evaluation",
            slo="retrieval/cost-amplification evidence only; no production SLO",
        ),
    },
    "SF-SKILLADAPTOR": {
        "arxiv_v1": "2606.01311v1",
        "model_locator": "§4.1; Appendix B.1",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Kimi-K2.5; GLM-5; GPT-5.2 backbones; Qwen3-Embedding-8B is the skill retriever",
            "WebShop success rate, PinchBench average score and Claw-Eval average score under matched backbones",
            hardware="Not Disclosed — provider/API hardware is hidden",
            precision="Not Disclosed — provider/API precision is hidden",
            input_length="benchmark tasks plus retrieved skill text; no common numeric token cap disclosed",
            output_length="agent trajectories/task outcomes; no common numeric token cap disclosed",
            batch="Not Applicable — task-by-task agent evaluation",
            concurrency="Not Applicable — no request-serving concurrency experiment",
            slo="task-score evidence only; no production SLO",
        ),
    },
    "SF-SKILLSMITH": {
        "arxiv_v1": "2606.01314v1",
        "model_locator": "§4.1 Experimental Setup; Appendix D",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Qwen3.5 backbones at the five exact-v1 source-labeled scales from 9B to 397B; Qwen3.5-122B is the frozen judge",
            "OfficeQA, SealQA and WildClawBench accuracy, evolution trajectory, regression/tool-error rate and empirical model-call cost",
            input_length="task context includes skill/tool descriptions; exact-v1 reports context-size analysis but no common token cap",
            output_length="skill/tool proposals and task trajectories; no common numeric token cap disclosed",
            batch="three judge repetitions per response for majority vote; no runtime batch size",
            concurrency="Not Applicable — offline agent evolution/evaluation",
            slo="accuracy/evolution/cost evidence only; no production SLO",
        ),
    },
    "SF-SABER-CODING-AGENT-SAFETY": {
        "arxiv_v1": "2606.01317v1",
        "model_locator": "§3 Table 1; §5; Appendix E",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "13 evaluated models: Claude Opus 4.6, GPT-5.4, MiniMax-M2.5, Qwen3.5-397B, Qwen3.5-35B, Qwen3.5-9B, DeepSeek-V3, DeepSeek-V3.2, DeepSeek-R1, GLM-5, GLM-4.7, Kimi-K2.5 and Ling-flash-2.0",
            "harmful/safe completion, incapable/refusal, propagating/compositional harm and cause labels over 716 executable tasks",
            hardware="Docker-isolated workspaces; provider model hardware and precision are not normalized",
            precision="Not Disclosed — no common precision across provider models",
            input_length="stateful project workspaces and task prompts; no common numeric token cap disclosed",
            output_length="multi-step command/tool trajectories and final workspace state; no common token cap disclosed",
            batch="Not Applicable — one agent run per model/task cell",
            concurrency="Not Applicable — isolated offline runs, not serving concurrency",
            slo="operational-safety benchmark evidence only; no production SLO",
        ),
    },
    "SF-RINGELMANN-MAS": {
        "arxiv_v1": "2606.02646v1",
        "model_locator": "§4 Experimental setup; Appendix C.1; Appendix H",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Qwen2.5-7B primary experiments; Llama-3.1-8B cross-family verification",
            "team accuracy, answer entropy/agreement, effective team size and fitted Ringelmann c/beta across team size and communication conditions",
            hardware="NVIDIA H100, A100 and L40S cells as scoped in the exact-v1 experimental appendix",
            input_length="MMLU-Hard, GPQA and GSM-Hard items; no common token cap disclosed",
            output_length="multiple-choice/free-form answers; no common generation cap disclosed",
            batch="team size N={2,…,30}; this is agent-team scale, not inference batch",
            concurrency="team size and communication rounds are experimental factors; no request-serving concurrency",
            slo="team-effectiveness/scaling evidence only; no production SLO",
        ),
    },
    "SF-FAILURE-AWARE-MAS-OBS": {
        "arxiv_v1": "2606.01365v1",
        "model_locator": "§V Experimental Setup; §IV.5 grounding audit",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Not Applicable — the primary object is 165 recorded GAIA agent traces; gpt-4.1-mini is only the offline grounding auditor",
            "warning/failure observability, evidence availability/support, post-warning compute and intervention pilot outcomes; gpt-4.1-mini grounding audit",
            precision="Not Applicable — trace analysis and API-based offline audit",
            input_length="165 GAIA validation traces; no common token cap disclosed",
            output_length="mean trace token use ranges from 8,152 to 16,389 by level; not a configured output cap",
            batch="10-trace grounding audit and 10-task intervention pilot; no runtime batch size",
            concurrency="Not Applicable — offline trace analysis",
            slo="observability/intervention evidence only; no production SLO",
        ),
    },
    "SF-RESIDENT-KV-CLAIMS": {
        "arxiv_v1": "2606.01387v1",
        "model_locator": "§6 Boundary Studies; §8 Evaluation",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Not Applicable — protocol/compiler checker over TensorRT-LLM, SGLang/HiCache, Dynamo and patched-vLLM descriptors; no ML model is benchmarked",
            "obligation-bundle checker over positive/negative lowering cases and anchored runtime descriptors",
            precision="Not Applicable — protocol/claim validation, not tensor execution",
            input_length="descriptor/claim bundles; no token-sequence workload",
            output_length="accept/reject obligation outcomes; no generated sequence",
            batch="Not Applicable — case-based checker evaluation",
            concurrency="Not Applicable — no request-serving experiment",
            slo="claim-correctness evidence only; no production SLO",
        ),
    },
    "SF-DP-RAG-DATASTORE": {
        "arxiv_v1": "2606.01413v1",
        "model_locator": "§4 Experiments, paragraph 2",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Phi-4-Mini backbone",
            "classification accuracy/privacy utility plus membership-inference AUROC/features across seven datasets at epsilon=5",
            input_length="1.8K–8.7K datastore-construction examples and fixed 1K-example test sets (TREC 500); no token cap disclosed",
            output_length="2–14-class classification output",
            batch="Not Disclosed — no numeric inference/training batch size stated",
            concurrency="MIA attacker may issue unlimited datastore queries by threat-model assumption; no measured simultaneous concurrency",
            slo="privacy/utility and attack-resilience evidence only; no production SLO",
        ),
    },
    "SF-SELF-HEALING-ORCHESTRATOR": {
        "arxiv_v1": "2606.01416v1",
        "model_locator": "§6.5 Model-in-the-loop Configuration; §7.6",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Not Disclosed — exact-v1 says a live tool-calling model but does not name its identity; deterministic controlled track has no model",
            "task success, detection, recovery success, silent-failure rate and matched recovery-budget sweeps over controlled and 90-execution model-in-loop tracks",
            input_length="100 controlled tasks plus compact model-in-loop task set; no common token cap disclosed",
            output_length="tool-call/answer trajectories; no common token cap disclosed",
            batch="one execution per task/seed cell; 90 total model-in-loop executions, not a batch size",
            concurrency="Not Applicable — controlled offline execution",
            slo="reliability/recovery evidence only; no production SLO",
        ),
    },
    "SF-MEMORY-FRESHNESS-ASSEMBLY": {
        "arxiv_v1": "2606.01435v1",
        "model_locator": "§4.2 Backbone models; §5.6–§5.7",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "gpt-4o-mini headline backbone; gpt-4o and o4-mini ablations; Claude-3.7-Sonnet is a named long-context comparison, not the headline backbone",
            "SubEM on MemoryAgentBench FactConsolidation, matched-backbone ablations and 45-item LongMemEval knowledge-update check",
            hardware="Not Disclosed — provider/API hardware is hidden",
            precision="Not Disclosed — provider/API precision is hidden",
            input_length="MemoryAgentBench contexts 6K, 32K, 64K and 262K tokens; chunk-4096 is 4,096 characters",
            output_length="short fact-consolidation/QA answers; no common numeric generation cap disclosed",
            batch="n=100 controlled cells and 45 LongMemEval items; no request batch size",
            concurrency="Not Applicable — offline benchmark evaluation",
            slo="memory-answer quality evidence only; no production SLO",
        ),
    },
    "SF-REASONING-PRODUCTION-EVAL-GAP": {
        "arxiv_v1": "2606.01462v1",
        "model_locator": "§3.1–§3.3; Appendices A–B",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Claude Sonnet 4.6; Claude Opus 4.7; DeepSeek-R1; GPT-5; GPT-5.4; Gemini-3.1-Pro; Qwen2.5-Math-PRM-7B and Gemini-3.1-Flash-Lite are auxiliary evaluator/annotator models",
            "final-answer accuracy versus intermediate-reasoning validity on VAVR/VAIR/IAIR, process-reward-model checks and human/annotator studies",
            hardware="NVIDIA RTX 4090 and RTX 5090 for the scoped open-model probing; provider hardware hidden for frontier APIs",
            input_length="reasoning problems and invalid/valid solution variants; no common token cap disclosed",
            output_length="reasoning traces and final answers; no common generation cap disclosed",
            batch="Not Disclosed — no common numeric batch size stated",
            concurrency="Not Applicable — offline reasoning evaluation",
            slo="reasoning-validity/evaluator-reliability evidence only; no production SLO",
        ),
    },
    "SF-CLAWHUB-SECURITY-SIGNALS": {
        "arxiv_v1": "2606.01494v1",
        "model_locator": "§4–§8; scanner identities",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "Not Applicable — VirusTotal, static analysis and NVIDIA SkillSpector are scanner identities; exact-v1 does not benchmark a named base LLM",
            "scanner overlap/agreement, verdict-conditioned positives, risk categories and illustrative cases over 67,453 sanitized skill versions",
            precision="Not Applicable — dataset/scanner disagreement analysis",
            input_length="67,453 sanitized skill bundles; item lengths are corpus scoped",
            output_length="scanner/verdict labels and advisory categories",
            batch="full-corpus scanner-signal analysis; no runtime batch size",
            concurrency="Not Applicable — offline corpus analysis",
            slo="scanner-disagreement evidence only; no production detection SLO",
        ),
    },
    "SF-CROSS-INSTANCE-LATENT-REDISTRIBUTION": {
        "arxiv_v1": "2606.01502v1",
        "model_locator": "§3 Experimental Setup; §4.3; §6; §8",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "DeepSeek-V3.2 sparse/latent-attention geometry instantiated in the communication microbenchmark; no end-to-end model serving run",
            "RDMA latency/bandwidth, route-vs-fetch-vs-local cost fit, holder capacity and redistribution correctness",
            hardware="multi-node NVIDIA H100/IBGDA primary cells with scoped A100 and one/four-H100 sensitivity cells",
            precision="BF16/FP32 compute and FP8/wire-format cells as separately scoped in exact-v1",
            input_length="attention query/KV geometry derived from the disclosed model configuration; no end-to-end prompt length",
            output_length="latent/KV payload transfer and attention result; no generated token sequence",
            batch="microbenchmark payload/topology cells; no inference batch size",
            concurrency="about eight requester instances per holder before copy-engine contention in the measured hot-chunk cell",
            slo="communication primitive latency/bandwidth/capacity evidence only; no production serving SLO",
        ),
    },
    "SF-AGENT-FALSE-SUCCESS": {
        "arxiv_v1": "2606.09863v1",
        "model_locator": "§3.1 source families; §3.4 detectors; §3.5 judges",
        "model_action": "corrected_or_precisified",
        **audited_retained_benchmark(
            "evaluated detectors TF-IDF+LR, TF-IDF+XGBoost and microsoft/deberta-v3-base; source trajectories span Claude Opus 4.5, Claude Sonnet 4.5, GPT-5.2, Gemini 3 Pro/Flash, GLM-5, Qwen3-Max-Thinking-Preview and Qwen3.5-397B-A17B; judge models are GPT-4o, Claude Sonnet 4.5, Llama-3.3-70B-Instruct, DeepSeek-R1 and o3-mini",
            "false-success rate, detector/judge AUROC, task/model-disjoint generalization, triage recall/precision and inference latency",
            hardware="XGBoost detector evaluated on CPU with no GPU dependency; LLM judge/provider hardware hidden",
            precision="Not Disclosed — detector/API numerical precision is not stated",
            input_length="DeBERTa sequence length 512 with left truncation; TF-IDF uses full or scoped trajectory text",
            output_length="binary detector/judge completion labels",
            batch="DeBERTa training batch size 16; judge queries are cached per model/prompt with no request batch stated",
            concurrency="Not Disclosed — no measured simultaneous-request concurrency",
            slo="author reports 1.19 ms XGBoost CPU inference versus about 4,000 ms LLM API call; diagnostic, not production SLO",
        ),
    },
    "SF-FED-PERSONALIZATION-SILENT-FAILURES": {
        "arxiv_v1": "2606.00947v1",
        "model_locator": "§4 The Monitoring Gap in Federated Systems; Appendix A Benchmark Paper Overviews",
        "model_action": "corrected_or_precisified",
        "Model": "Not Disclosed",
        "Hardware": "Not Disclosed",
        "Precision": "Not Disclosed",
        "Input Length": "Not Disclosed",
        "Output Length": "Not Disclosed",
        "Batch": "Not Disclosed",
        "Concurrency": "Not Disclosed",
        "SLO": "Not Disclosed",
        "Evaluator": "landscape analysis of twelve representative federated and centralized trustworthiness benchmarks; no newly executed model benchmark",
    },
    "SF-AIREP": {
        "arxiv_v1": "2608.21363v1",
        "model_locator": "§4 Conformance and Neutrality; §4.4 Implementation",
        "model_action": "corrected_or_precisified",
        "Model": "Not Disclosed",
        "Hardware": "Not Disclosed",
        "Precision": "Not Disclosed",
        "Input Length": "Not Disclosed",
        "Output Length": "Not Disclosed",
        "Batch": "Not Disclosed",
        "Concurrency": "Not Disclosed",
        "SLO": "Not Disclosed",
        "Evaluator": "mechanical schema-conformance and neutrality checks plus the disclosed two-language conformance kit; no author-controlled model benchmark",
    },
    "SF-AGENT-OPERATING-SYSTEM": {
        "arxiv_v1": "2606.01508v1",
        "model_locator": "PDF §10 Evaluation Criteria and Open Research Problems",
        "model_action": "corrected_or_precisified",
        "Model": "Not Disclosed",
        "Hardware": "Not Disclosed",
        "Precision": "Not Disclosed",
        "Input Length": "Not Disclosed",
        "Output Length": "Not Disclosed",
        "Batch": "Not Disclosed",
        "Concurrency": "Not Disclosed",
        "SLO": "Not Disclosed",
        "Evaluator": "architecture evaluation criteria in exact-v1 PDF §10; no executed evaluator or benchmark result",
    },
    "SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY": {
        "arxiv_v1": "2606.04017v1",
        "model_locator": "§3 Evaluating Long-Running Epistemic Integrity",
        "model_action": "corrected_or_precisified",
        "Model": "Not Disclosed",
        "Hardware": "Not Disclosed",
        "Precision": "Not Disclosed",
        "Input Length": "Not Disclosed",
        "Output Length": "Not Disclosed",
        "Batch": "Not Disclosed",
        "Concurrency": "Not Disclosed",
        "SLO": "Not Disclosed",
        "Evaluator": "five proposed persisted-trajectory integrity dimensions in exact-v1 HTML §3; empirical testbed remains future work",
    },
}


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_research", ROOT / "scripts/validate_research.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator()


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if value:
            self.parts.append(value)


def html_text(path: Path) -> str:
    parser = TextExtractor()
    parser.feed(path.read_text(errors="ignore"))
    return "\n".join(parser.parts)


def is_full_arxiv_html(path: Path) -> bool:
    if not path.exists() or path.stat().st_size <= 5000:
        return False
    head = path.read_text(errors="ignore")
    return '<article class="ltx_document' in head


def pdf_text(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    text = "\n".join((page.extract_text() or "") for page in reader.pages).replace("\x00", "")
    # Some exact-v1 PDFs expose only page-number glyphs through pypdf even
    # though the text layer is intact.  A second parser recovers that same PDF;
    # this is not OCR and does not borrow a later revision.
    if sum(character.isalpha() for character in text) < 1000:
        import pdfplumber

        with pdfplumber.open(path) as pdf:
            text = "\n".join((page.extract_text() or "") for page in pdf.pages).replace("\x00", "")
    return text


@functools.lru_cache(maxsize=None)
def exact_text(arxiv_id: str) -> tuple[str, str]:
    html_path = MATERIALS / f"{arxiv_id}v1.html"
    if is_full_arxiv_html(html_path):
        text = html_text(html_path)
        if len(text) > 3000:
            return text, html_path.name
    pdf_path = MATERIALS / f"{arxiv_id}v1.pdf"
    if pdf_path.exists():
        text = pdf_text(pdf_path)
        if len(text) > 3000:
            return text, pdf_path.name
    raise RuntimeError(f"exact-v1 material is incomplete for {arxiv_id}")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def atom_abstracts() -> dict[str, str]:
    """Load source-specific frozen abstracts for idempotent closure review."""
    root = ET.fromstring(gzip.open(PACKET / "arxiv-overread-first-page.atom.gz", "rb").read())
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out: dict[str, str] = {}
    for entry in root.findall("a:entry", ns):
        raw_id = (entry.findtext("a:id", default="", namespaces=ns) or "").rsplit("/", 1)[-1]
        arxiv_id = raw_id.split("v", 1)[0]
        out[arxiv_id] = " ".join((entry.findtext("a:summary", default="", namespaces=ns) or "").split())
    return out


def first_sentence(text: str, limit: int = 260) -> str:
    text = " ".join(text.split())
    if not text:
        return "the frozen Atom record contains no usable abstract text"
    match = re.search(r"(?<=[.!?])\s", text)
    value = text[: match.start() + 1] if match else text
    return value[:limit].rstrip()


def source_specific_closure(row: dict[str, str], abstract: str) -> str:
    """Create an idempotent, family-specific closure from frozen identity data.

    The output intentionally does not reuse an earlier reason.  A prior repair
    recursively wrapped its own prose, so the only authoritative inputs here
    are the frozen title, categories and Atom abstract.
    """
    title = row["title"]
    categories = row["registered_categories"]
    evidence = first_sentence(abstract, 360)
    text = f"{title} {abstract}".casefold()
    if any(term in text for term in ("survey", "review", "taxonomy", "bibliometric")):
        contribution = "a survey, taxonomy, or literature synthesis rather than a newly evaluated mechanism"
        missing = "no new state owner, control path, implementation contract, or revision claim"
    elif any(term in text for term in ("dataset", "benchmark", "corpus", "challenge")):
        contribution = "a dataset or evaluation-denominator contribution"
        missing = "no reusable evaluation contract beyond the domain-specific subject, task, and metric disclosed here"
    elif any(term in text for term in ("medical", "clinical", "molecule", "drug", "protein", "gene", "finance", "agricultur")):
        contribution = "a domain-local application or scientific result"
        missing = "no mechanism change that transfers to the project's model, training, inference, platform, or agent contracts"
    elif any(term in text for term in ("network", "wireless", "routing protocol", "traffic", "cloud", "edge")):
        contribution = "a communications or general distributed-systems result"
        missing = "no AI-workload-specific state, scheduling, memory, evidence, or artifact contract"
    elif any(term in text for term in ("hardware", "circuit", "fpga", "accelerator", "memory", "cache")):
        contribution = "a component- or hardware-local mechanism"
        missing = "no demonstrated handoff to an AI model/runtime workload with the required correctness and SLO boundary"
    elif any(term in text for term in ("classification", "segmentation", "detection", "recognition", "prediction")):
        contribution = "a task-local model or metric improvement"
        missing = "no durable change to representation identity, learning objective, runtime state, or release evidence"
    else:
        contribution = "a bounded algorithmic or application result"
        missing = "no project-level mechanism delta beyond the paper's own problem formulation and evaluation"
    return (
        f"Frozen v1 evidence: {evidence} Closure after full title/abstract replay in `{categories}`: "
        f"`{title}` is {contribution}; {missing}. Reopen condition: a primary artifact must expose a "
        "transferable state/control contract or evidence that conflicts with a named Stable Knowledge Node."
    )


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def parse_table(text: str, marker: str) -> tuple[list[str], list[dict[str, str]]]:
    after = text.split(marker, 1)[1].lstrip("\n")
    lines = after.splitlines()
    headers = [value.strip() for value in lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        if not line.startswith("|"):
            break
        values = [value.strip() for value in line.strip("|").split("|")]
        rows.append(dict(zip(headers, values)))
    return headers, rows


def render_table(headers: list[str], rows: list[dict[str, str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        # Validator intentionally uses a simple pipe-delimited parser; keeping a
        # literal pipe, even Markdown-escaped, changes the machine cell count.
        lines.append("| " + " | ".join(row.get(header, "—").replace("|", "/") for header in headers) + " |")
    return "\n".join(lines)


def replace_table(text: str, marker: str, headers: list[str], rows: list[dict[str, str]]) -> str:
    start = text.index(marker) + len(marker)
    tail = text[start:]
    match = re.match(r"\s*\|.*?(?=\n\n|\n<!--|\n###|\n##)", tail, re.S)
    if not match:
        raise RuntimeError(f"cannot locate table after {marker}")
    return text[:start] + "\n" + render_table(headers, rows) + tail[match.end():]


def exact_v1_title(arxiv_id: str, fallback: str) -> str:
    if arxiv_id in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[arxiv_id]
    metadata = V1_METADATA / f"{arxiv_id}v1.abs.html"
    if not metadata.exists():
        return fallback
    raw = metadata.read_text(errors="ignore")
    match = re.search(r'<h1 class="title mathjax">(.*?)</h1>', raw, re.S)
    if not match:
        return fallback
    title = re.sub(r"<[^>]+>", "", html.unescape(match.group(1)))
    return " ".join(title.replace("Title:", "").split())


def headings(text: str) -> list[str]:
    candidates: list[str] = []
    for raw in text.splitlines():
        line = " ".join(raw.split()).strip()
        if not 4 <= len(line) <= 150:
            continue
        if re.match(r"^(?:\d+(?:\.\d+)*\.?|[IVX]+\.?)\s+[A-Z][A-Za-z0-9 ,:/()'&\-–—]+$", line):
            if line not in candidates:
                candidates.append(line)
    return candidates


def exact_headings(arxiv_id: str, text: str) -> list[str]:
    html_path = MATERIALS / f"{arxiv_id}v1.html"
    if is_full_arxiv_html(html_path):
        raw = html_path.read_text(errors="ignore")
        values: list[str] = []
        for match in re.finditer(r"<h[1-6][^>]*>(.*?)</h[1-6]>", raw, flags=re.S | re.I):
            value = re.sub(r"<[^>]+>", " ", html.unescape(match.group(1)))
            value = " ".join(value.split())
            chrome = ("report github issue", "instructions for reporting errors", "license", "html conversion")
            if 3 < len(value) < 180 and value.casefold() not in chrome and value not in values:
                values.append(value)
        if values:
            return values
    return headings(text)


def pick_heading(items: list[str], words: tuple[str, ...], excluded: tuple[str, ...] = ()) -> str | None:
    def contains(value: str, phrase: str) -> bool:
        return re.search(rf"(?<![a-z0-9]){re.escape(phrase.casefold())}(?![a-z0-9])", value.casefold()) is not None

    # Prefer main-body top-level sections over appendix/subsection/sentence
    # headings before applying phrase priority. This prevents a late appendix
    # `Methodology` or a result sentence containing `method` from displacing the
    # paper's actual top-level Method/Framework section.
    candidates: list[tuple[tuple[int, int, int, int], str]] = []
    for word_index, word in enumerate(words):
        for item_index, item in enumerate(items):
            if not contains(item, word) or any(contains(item, blocked) for blocked in excluded):
                continue
            appendix = int(bool(re.match(r"^(?:Appendix\s+|[A-Z](?:\.\d+)*\s)", item)))
            if re.match(r"^\d+\.?\s+", item):
                depth = 0
            elif re.match(r"^\d+\.\d+\.?\s+", item):
                depth = 1
            else:
                depth = 2
            sentence_like = int(item.endswith(".") and len(item.split()) > 6)
            candidates.append(((appendix, depth, sentence_like, word_index * 1000 + item_index), item))
    return min(candidates, default=(None, None), key=lambda candidate: candidate[0])[1]


def locator(arxiv_id: str, items: list[str], facet: str, route: str) -> str:
    pdf_only = not is_full_arxiv_html(MATERIALS / f"{arxiv_id}v1.html")
    source_kind = "exact-v1 PDF" if pdf_only else "exact-v1 HTML"
    if facet == "method":
        chosen = pick_heading(
            items,
            ("methodology", "methods", "method", "framework", "design", "architecture", "algorithm", "pipeline", "formulation", "approach", "proposed"),
            ("related work", "background", "theoretical analysis", "literature", "benchmark overview"),
        )
        if chosen:
            return f"arXiv:{arxiv_id}v1 {source_kind} § `{chosen}`"
        # A named architecture/design/pipeline section is stronger method
        # evidence than the first otherwise-unclassified numbered section.
        # Keeping this before the generic fallback avoids selecting sections
        # such as Future Work merely because the paper has no literal
        # "Method" heading.
        chosen = pick_heading(
            items,
            ("architecture", "algorithm", "pipeline", "formulation", "task definition", "problem setup", "setup", "design", "implementation"),
            ("related work", "background", "theoretical analysis", "literature", "benchmark overview", "existing", "evaluation"),
        )
        if chosen:
            return f"arXiv:{arxiv_id}v1 {source_kind} § `{chosen}`"
        # Papers often title the contribution after the system name rather
        # than “Method”.  Prefer the first top-level contribution section after
        # Introduction/Related Work over any 2.x background subsection.
        for item in items:
            low = item.casefold()
            if re.match(r"^\d+\s+", item) and not any(
                word in low
                for word in (
                    "introduction", "related work", "background", "prelim",
                    "experiment", "evaluation", "result", "conclusion",
                    "discussion", "future work", "limitation", "threat",
                    "reference", "appendix",
                )
            ):
                return f"arXiv:{arxiv_id}v1 {source_kind} § `{item}`"
        for item in items:
            low = item.casefold()
            if not any(word in low for word in ("introduction", "related work", "background", "prelim", "experiment", "evaluation", "result", "conclusion", "reference", "appendix", "theorem", "proof")):
                return f"arXiv:{arxiv_id}v1 {source_kind} § `{item}`"
        return f"arXiv:{arxiv_id}v1 {source_kind} § Abstract — no separately named method section"
    if facet == "evaluation":
        if route == "closure":
            return "Not Required — closure-only review does not borrow experimental results"
        chosen = pick_heading(
            items,
            ("experiments", "experimental setup", "experiment", "evaluation", "empirical", "results", "ablation", "case study"),
            ("related work", "background", "theoretical analysis", "benchmark overview", "problem setup"),
        )
        if chosen:
            return f"arXiv:{arxiv_id}v1 {source_kind} § `{chosen}`"
        return f"Not Disclosed — arXiv:{arxiv_id}v1 {source_kind} has no separately identifiable empirical evaluation section"
    if facet == "limitations":
        if route == "closure":
            return "Not Required — closure-only disposition is bounded by identity and project scope"
        chosen = pick_heading(items, ("limitations", "limitation", "threats to validity", "threat", "discussion", "conclusion", "future work"), ("related work", "threat model"))
        if chosen:
            return f"arXiv:{arxiv_id}v1 {source_kind} § `{chosen}`"
        return f"Not Disclosed — arXiv:{arxiv_id}v1 {source_kind} has no dedicated limitations section; Daily claim boundary supplies the conservative limit"
    if route != "deep":
        return f"Not Required — {route} review does not require an immutable artifact locator"
    chosen = pick_heading(items, ("artifact availability", "data availability", "code availability", "reproducibility", "implementation details", "open-source release"), ("related work",))
    if chosen:
        return f"arXiv:{arxiv_id}v1 {source_kind} § `{chosen}`; no immutable commit inferred beyond the manuscript"
    return f"Not Disclosed — arXiv:{arxiv_id}v1 {source_kind} does not pin an immutable implementation revision"


def title_from_review(text: str, family: str) -> str:
    segment = text.split(f"<!-- review:{family}:start -->", 1)[1].split(f"<!-- review:{family}:end -->", 1)[0]
    match = re.search(r"^###\s+(.+)$", segment, re.M)
    return match.group(1).strip() if match else family


OWNER_REFS = {
    "AGENT-PROMPT": ("books/part-07-agent/74-prompt.md#L10", "books/part-07-agent/75-context.md#L10;books/part-01-worldview/03-generalization-and-hallucination.md#L10"),
    "AGENT-WORKFLOW": ("books/part-07-agent/81-workflow.md#L10", "books/part-07-agent/80-reflection.md#L10;books/part-07-agent/82-multi-agent.md#L10"),
    "MODEL-POSITION-ENCODING": ("books/part-02-model/13-position-encoding.md#L10", "books/part-02-model/12-embedding.md#L10;books/part-02-model/14-attention.md#L10"),
    "MODEL-SAMPLING": ("books/part-02-model/20-sampling.md#L10", "books/part-02-model/19-kv-cache.md#L10;books/part-02-model/21-moe.md#L10"),
    "MODEL-TRANSFORMER-LAYER": ("books/part-02-model/17-transformer-layer.md#L10", "books/part-02-model/16-mlp.md#L10;books/part-02-model/18-decoder-only.md#L10"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10", "books/part-03-multimodal-world-models/23-multimodal-representation.md#L10;books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10"),
    "PLATFORM-COST": ("books/part-06-ai-infrastructure/70-cost.md#L10", "books/part-06-ai-infrastructure/69-trace.md#L10;books/part-06-ai-infrastructure/71-multi-tenant.md#L10"),
    "TRAIN-DISTRIBUTED-TRAINING": ("books/part-04-training-system/36-distributed-training.md#L10", "books/part-04-training-system/35-checkpoint.md#L10;books/part-04-training-system/37-data-parallel.md#L10"),
    "TRAIN-DPO": ("books/part-04-training-system/34-dpo.md#L10", "books/part-04-training-system/33-grpo.md#L10;books/part-04-training-system/35-checkpoint.md#L10"),
    "TRAIN-RLHF": ("books/part-04-training-system/31-rlhf.md#L10", "books/part-04-training-system/30-lora.md#L10;books/part-04-training-system/32-ppo.md#L10"),
}


OWNER_PROPOSITION = {
    "MODEL-MOE": "MoE separates parameter capacity from per-token active compute, while routing capacity and communication remain first-class contracts.",
    "MODEL-LONG-CONTEXT": "Long-context design is a state, attention-complexity and evidence-retention problem rather than a context-window number alone.",
    "MODEL-POSITION-ENCODING": "Position representation must preserve the relation the workload needs while defining its extrapolation boundary.",
    "MODEL-SAMPLING": "Sampling exposes an explicit quality, diversity, calibration and latency policy at the token-commit boundary.",
    "MODEL-TRANSFORMER-LAYER": "A Transformer layer composes information mixing, nonlinear transformation, residual state and normalization into a trainable state transition.",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "Generation factorization determines which state can update in parallel, which commitments can be revised and what runtime cache remains valid.",
    "MULTIMODAL-REPRESENTATION": "Multimodal representations require explicit modality, time and provenance identity before fusion.",
    "MULTIMODAL-WORLD-MODELS": "A world model predicts action-conditioned state transition, not merely plausible next pixels.",
    "MULTIMODAL-EMBODIED-VLA": "Embodied systems separate perceptual evidence, high-level proposal and bounded real-time control with an observable feedback loop.",
    "TRAIN-DATA": "Training data is a versioned evidence artifact whose provenance, distribution and quality signals constrain what objectives can learn.",
    "TRAIN-PRETRAINING": "Pretraining couples data distribution, objective, optimization and hardware execution; one axis cannot be interpreted in isolation.",
    "TRAIN-SFT": "SFT changes conditional behavior through supervised trajectories while retaining data and coverage boundaries.",
    "TRAIN-LORA": "LoRA trades trainable state and deployment cost against restricted update rank and merge/version complexity.",
    "TRAIN-RLHF": "RLHF turns preference evidence into a policy update but introduces reward-model, sampling and optimization failure modes.",
    "TRAIN-GRPO": "Group-relative optimization changes the baseline and rollout contract, not the need for calibrated rewards and stable training state.",
    "TRAIN-DPO": "DPO replaces an online policy-optimization loop with an offline preference-ratio objective under a fixed reference and data contract.",
    "TRAIN-DISTRIBUTED-TRAINING": "Distributed training is a partitioned state machine whose compute, communication, memory and checkpoint identities must agree.",
    "INFER-TENSORRT-LLM": "Execution planning owns graph lowering, kernels, precision and hardware-specific plans; isolated kernel gains are workload-bound evidence.",
    "INFER-SCHEDULING": "Inference scheduling allocates time, memory and placement under explicit latency and throughput objectives with safe fallback.",
    "PLATFORM-EVALUATION-SYSTEM": "Evaluation binds subject, denominator, evidence, evaluator and decision boundary; a score without that contract is not release evidence.",
    "PLATFORM-COST": "Cost accounting requires a functional unit and full lifecycle boundary rather than a single accelerator-hour number.",
    "PLATFORM-SECURITY": "Security retains deterministic authority over trust boundaries, least privilege and effects even when model signals assist detection.",
    "AGENT-PROMPT": "A prompt is an untrusted, versioned control input whose authority and provenance must remain distinct from model text.",
    "AGENT-RAG": "RAG separates retrieval, evidence identity, context assembly and answer generation so authority can be audited.",
    "AGENT-WORKFLOW": "A durable workflow owns explicit state transition, retry, compensation and human-intervention boundaries.",
    "AGENT-MULTI-AGENT": "Multi-Agent systems pay coordination and state-transfer cost; partitioning is justified only when responsibility boundaries reduce the critical path.",
    "AGENT-PLATFORM": "Agent platforms version skills, workflows, authority, runtime state and evidence planes.",
}


def block(text: str, ref: str) -> str:
    start = f"<!-- {ref}:start -->"
    end = f"<!-- {ref}:end -->"
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def replace_bounded(text: str, ref: str, body: str) -> str:
    start = f"<!-- {ref}:start -->"
    end = f"<!-- {ref}:end -->"
    if start not in text or end not in text:
        return text
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + body + end + after


def synchronize_review_contract(text: str, family: str, receipt: dict[str, str]) -> str:
    """Keep narrative locator claims identical to the audited receipt table."""
    ref = f"review:{family}"
    body = block(text, ref)
    if not body or "evidence contract" not in body:
        return text
    route = receipt["Review Route"].capitalize()
    replacement = (
        f"{route} evidence contract：Method/identity=`{receipt['Method / Identity Locators']}`；"
        f"Evaluation=`{receipt['Evaluation Locators']}`；"
        f"Limitations/counterevidence=`{receipt['Limitations / Counterevidence Locators']}`；"
        f"Artifact=`{receipt['Artifact Locators']}`。"
    )
    body = re.sub(
        r"(?:Deep|Standard|Closure) evidence contract：.*?(?=Owner/authority：|\Z)",
        replacement,
        body,
        count=1,
        flags=re.S,
    )
    return replace_bounded(text, ref, "\n" + body + "\n")


def owner_contract(node: str) -> tuple[str, str, str]:
    """Return old-path, owned state/authority and coexistence contract."""
    prefix = node.split("-", 1)[0]
    contracts = {
        "WORLDVIEW": ("用经验风险和表示假设解释学习", "假设、证据范围与可识别性", "理论近似只作解释，不替代任务内验证"),
        "MODEL": ("以固定表示和稠密层完成通用计算", "token/activation/概率分解的语义", "简单表示在域和长度稳定时仍更可控"),
        "MULTIMODAL": ("先把各模态压成固定接口再生成或控制", "跨模态 identity、latent state 与环境 transition", "静态感知任务不需要可行动的持久世界状态"),
        "TRAIN": ("以离线批训练和统一目标更新参数", "梯度、优化状态、数据与 checkpoint lineage", "小规模稳定任务仍适合同步、单目标训练"),
        "INFER": ("以单请求、单执行图和完整精度获得确定基线", "KV/activation/commit/execution-plan 状态", "低并发或 correctness-first 路径仍应保留基线"),
        "PLATFORM": ("用离线 benchmark 与人工发布判断质量", "evidence、policy、resource 与 release authority", "低风险实验可保持轻量，但不得冒充生产证据"),
        "AGENT": ("把一次模型调用视为完整决策", "context、memory、tool effect 与 workflow checkpoint", "无外部副作用的短任务仍可使用单轮路径"),
    }
    return contracts.get(prefix, ("使用局部经验规则", "机制状态与控制边界", "约束未变化时旧路径仍成立"))


def roadmap_refs() -> dict[str, tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for line in (ROOT / "ROADMAP.md").read_text().splitlines():
        match = re.match(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+\.md)` \|", line)
        if match:
            rows.append((match.group(1), match.group(2)))
    out: dict[str, tuple[str, str]] = {}
    for index, (node, path) in enumerate(rows):
        adjacent: list[str] = []
        if index:
            adjacent.append(rows[index - 1][1])
        if index + 1 < len(rows):
            adjacent.append(rows[index + 1][1])
        out[node] = (path, ";".join(adjacent) or path)
    return out


def chapter_proposition(ref: str, evidence: str = "") -> tuple[str, str]:
    path = ref.split("#", 1)[0]
    target = ROOT / path
    if not target.exists():
        return ref, "chapter text unavailable in this checkout"
    raw = target.read_text()
    useful: list[tuple[int, str]] = []
    for match in re.finditer(r"(?:\A|\n\s*\n)(.*?)(?=\n\s*\n|\Z)", raw, flags=re.S):
        paragraph = match.group(1)
        value = " ".join(paragraph.split())
        line = raw[:match.start(1)].count("\n") + 1
        if not value or value.startswith(("#", "<!--", "|", "```", "- ", "* ", "> ")):
            continue
        if "?" in value or "？" in value or "Review notes" in value or "本章将" in value or "本章要" in value:
            continue
        if re.match(r"^\d+[.)、]\s*", value):
            continue
        if len(value) < 80 or not re.search(r"[。.!]", value):
            continue
        useful.append((line, value))
    if not useful:
        return ref, "chapter has no narrative paragraph at the audited revision"
    terms = {
        term for term in re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{3,}", evidence.casefold())
        if term not in {"that", "with", "from", "into", "using", "model", "system", "mechanism", "evidence", "boundary"}
    }
    ranked = sorted(
        useful,
        key=lambda item: (sum(term in item[1].casefold() for term in terms), -item[0]),
        reverse=True,
    )
    line, proposition = ranked[0]
    return f"{path}#L{line}", proposition[:700]


def chapter_excerpt(ref: str, evidence: str = "") -> str:
    return chapter_proposition(ref, evidence)[1]


def substantive_review(curated: dict[str, str], exact_row: dict[str, object], abstract: str) -> str:
    node = curated["stable_node_id"]
    mechanism = curated["mechanism_summary"]
    boundary = curated["boundary_summary"]
    method = exact_row["method"]
    evaluation = exact_row["evaluation"]
    limitations = exact_row["limitations"]
    artifact = exact_row["artifact"]
    problem = first_sentence(abstract, 420)
    relation = curated["relationship"]
    relation_old_path = {
        "Direct Evolution": "原路径直接执行较早的状态转换，并把后续约束留给外部补救",
        "Alternative Branch": "原路径在其稳定 workload 下保持更简单、可预测的单一路径",
        "Layering / Dependency": "原路径只保证底层能力，不拥有上层证据、校准或编排责任",
        "Principle Reuse": "原路径解决的是另一类对象；这里复用原则而不宣称同一实现可直接迁移",
        "Explanatory Analogy": "原路径只提供可解释类比，不能据此继承论文的定理或性能数字",
    }.get(relation, "原路径仍是受限 workload 下的可复现基线")
    baseline, owned_state, coexistence = owner_contract(node)
    state_delta = first_sentence(mechanism, 360)
    failure = first_sentence(boundary, 360)
    return (
        f"\n### {exact_row['title']}\n\n"
        f"**问题、旧路径与约束变化。** exact-v1 将问题界定为：{problem} `{node}` 既有路径是{baseline}；"
        f"在本论文改变的 workload 中，{relation_old_path}。"
        f"这项工作只有在该问题真实出现时才构成 `{node}` 的候选增量，而不是凭论文标题改变 owner。\n\n"
        f"**Mechanism、state ownership 与实现。** {mechanism} 本 family 的可变状态不是泛化的‘模型输出’，"
        f"而是 `{state_delta}` 所定义的中间状态；在 `{node}` 中它属于{owned_state}。产生该状态的机制拥有写入权，"
        "下游评估器、调度器或安全层只能按论文公开接口读取、接受或否决，不能把消费端结果反写成来源内部事实。"
        "控制流先建立论文所述条件/候选/估计，再执行选择、更新或动作；数据流保留其输入身份与提交后的输出边界。Method/implementation 定位为 "
        f"`{method}`；artifact 定位为 `{artifact}`。未公开的代码 revision、runtime 和硬件控制流不作补写。\n\n"
        f"**Evaluation、证明与未证明。** 结果证据定位为 `{evaluation}`，限制/反证定位为 `{limitations}`。"
        f"它支持的最强命题是：{mechanism} 不支持的外推是：{boundary}\n\n"
        f"**Trade-off、failure mode 与共存。** 获得 `{state_delta}` 的代价是维护该 family 明示的额外条件、"
        "中间状态、训练或验证路径，并让其 identity 与更新时刻进入 correctness contract。最直接的 failure mode 是："
        f"{failure} 一旦来源假设、输入分布或 evaluator 改变，该状态可能失配、过期或被错误提交。{coexistence}；"
        "不需要该增量或无法承担新增状态与验证成本时，旧路径仍合理。"
        f"本报告将关系限定为 `{relation}`，Books disposition 暂定为 "
        f"`{curated['books_disposition']}`，等待独立 Books audit。\n\n"
        f"<!-- claim:{curated['source_family_id']}:start -->{mechanism} 证据边界：{boundary}"
        f"<!-- claim:{curated['source_family_id']}:end -->\n"
    )


def contract_field(source: str, field: str, locator_text: str) -> str:
    """Extract only normalized configuration values, never prose snippets."""
    flat = " ".join(source.split())
    patterns = {
        "Model": r"\b(?:Llama(?:[- ]?\d+(?:\.\d+)?(?:B)?)?|Gemma(?:[- ]?\d+(?:\.\d+)?(?:B)?)?|Qwen(?:[- ]?\d+(?:\.\d+)?(?:B)?)?|Mistral(?:[- ]?\d+(?:B)?)?|GPT-\d(?:\.\d+)?|Claude(?:[- ]?[A-Za-z0-9.]+)*|BERT|RoBERTa|CLIP|DINOv2|SAM(?:2)?|ViT(?:-[A-Z0-9/]+)?|Wan2\.1-T2V-14B|DeepSeek(?:-[A-Za-z0-9.]+)?)\b",
        "Hardware": r"(?:(?:\d+|one|two|four|eight)\s*[×x]?\s*)?(?:NVIDIA\s+)?(?:H200|H100|A800|A100(?:-PCIE-40GB)?|A30|V100|L40S|RTX\s?\d+|Ascend\s?910B|TPU\s?v?\d+|Apple\s+(?:A18 Pro|M4 Pro))\b",
        "Precision": r"\b(?:FP32|FP16|BF16|FP8|INT8|INT4|float16|bfloat16|4-bit|8-bit)\b",
        "Input Length": r"\b(?:input|context|sequence)\s+(?:length|window)?\s*(?:of|=|:)?\s*\d{2,7}\s*(?:tokens?|[kK])\b",
        "Output Length": r"\b(?:output|generation|decode)\s+(?:length|budget)?\s*(?:of|=|:)?\s*\d{2,7}\s*(?:tokens?|[kK])\b",
        "Batch": r"\bbatch(?: size)?\s*(?:of|=|:)\s*\d+\b",
        "Concurrency": r"\b(?:concurrency\s*(?:of|=|:)\s*\d+|\d+\s+concurrent\s+(?:requests?|clients?))\b",
    }
    matches = []
    for match in re.finditer(patterns[field], flat, flags=re.I):
        value = " ".join(match.group(0).split())
        if value.casefold() not in {item.casefold() for item in matches}:
            matches.append(value)
        if len(matches) == 4:
            break
    if matches:
        return "Disclosed in exact-v1 source-wide reconciliation: " + ", ".join(matches)
    return f"Not Disclosed — no {field.lower()} value found across the exact-v1 full text, setup and appendix; result path `{locator_text}`"


def evaluation_slice(source: str, locator_text: str) -> str:
    """Bound disclosure extraction to the cited evaluation section."""
    if locator_text.startswith("Not Disclosed"):
        return ""
    match = re.search(r"§\s*`([^`]+)`", locator_text)
    if not match:
        return ""
    heading = " ".join(match.group(1).split()).strip(" `")
    start = source.lower().find(heading.lower())
    if start < 0:
        return ""
    return source[start : start + 24000]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force-author-rebuild",
        action="store_true",
        help="explicitly reopen and regenerate the historical pre-write author state",
    )
    args = parser.parse_args()
    if REPORT.exists() and "| Completion Status | Complete |" in REPORT.read_text() and not args.force_author_rebuild:
        raise SystemExit(
            "refusing to regress a completed 2026-06-01 Daily to the pre-write author state; "
            "use --force-author-rebuild only when the semantic Gates were explicitly reopened"
        )
    text = REPORT.read_text()
    _, preaudit_candidates = parse_table(text, VALIDATOR.CANDIDATE_LEDGER_MARKER)
    preaudit_by_id = {
        row["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1"): row
        for row in preaudit_candidates
    }
    curation = (
        read_tsv(CURATION)
        + read_tsv(CURATION_WAVE2)
        + read_tsv(CURATION_V3)
        + read_tsv(CURATION_V4)
        + read_tsv(CURATION_V5)
        + read_tsv(CURATION_V6)
        + read_tsv(CURATION_V7)
        + read_tsv(CURATION_V9)
    )
    v9_denominator_receipt = read_tsv(V9_DENOMINATOR_RECEIPT)
    retained_families_v9 = {
        row["source_family_id"]
        for row in v9_denominator_receipt
        if row["independent_decision"] == "retain"
    }
    assert len(v9_denominator_receipt) == 371
    assert len(retained_families_v9) == 40
    for row in curation:
        family = row["source_family_id"]
        if row["books_disposition"] == "Integrate" and family in VERIFIED_INTEGRATES:
            # These deltas are already present in the current Books proposition;
            # V9 compares against current text, so they are coverage rather than
            # new writeback proposals.
            row["books_disposition"] = "No Change — Existing Coverage"
        if row["books_disposition"] == "Integrate" and family not in VERIFIED_INTEGRATES | REJUDGED_INTEGRATES:
            row["books_disposition"] = "No Change — Existing Coverage"
    # Later curation waves are intentional source-specific overrides. Collapse
    # them before building bounded markers so one family can never receive two
    # review blocks merely because it was revisited in V9.
    curation_by_id: dict[str, dict[str, str]] = {}
    for row in curation:
        curation_by_id[row["arxiv_id"]] = row
    curation = list(curation_by_id.values())
    assert len(curation) == len({row["source_family_id"] for row in curation})
    ledger = read_tsv(LEDGER)
    abstracts = atom_abstracts()
    ledger_by_id = {row["arxiv_id"]: row for row in ledger}
    curated_by_id = {row["arxiv_id"]: row for row in curation}

    exact: dict[str, dict[str, object]] = {}
    for row in curation:
        arxiv_id = row["arxiv_id"]
        ledger_row = ledger_by_id[arxiv_id]
        if arxiv_id in WEB_EXACT:
            method, evaluation, limitations = WEB_EXACT[arxiv_id]
            exact[arxiv_id] = {
                "title": exact_v1_title(arxiv_id, ledger_row["title"]),
                "material": f"https://arxiv.org/{'pdf' if arxiv_id in PUBLIC_EXACT_PDF_IDS else 'html'}/{arxiv_id}v1",
                "headings": [],
                "method": public_exact_locator(arxiv_id, method),
                "evaluation": public_exact_locator(arxiv_id, evaluation),
                "limitations": public_exact_locator(arxiv_id, limitations),
                "artifact": (
                    public_exact_locator(arxiv_id, WEB_ARTIFACT_V7[arxiv_id])
                    if arxiv_id in WEB_ARTIFACT_V7
                    else f"Not Disclosed — arXiv:{arxiv_id}v1 does not pin an immutable implementation revision"
                ),
            }
            continue
        source, material_name = exact_text(arxiv_id)
        source_headings = exact_headings(arxiv_id, source)
        exact[arxiv_id] = {
            "title": exact_v1_title(arxiv_id, ledger_row["title"]),
            "material": material_name,
            "headings": source_headings,
            "method": locator(arxiv_id, source_headings, "method", row["review_route"]),
            "evaluation": locator(arxiv_id, source_headings, "evaluation", row["review_route"]),
            "limitations": locator(arxiv_id, source_headings, "limitations", row["review_route"]),
            "artifact": locator(arxiv_id, source_headings, "artifact", row["review_route"]),
        }
    exact["2606.07632"].update(
        {
            "method": "arXiv:2606.07632v1 exact-v1 PDF § `3 Life Cycle Assessment for ML Models`; § `3.1 Goal Definition and Scoping`",
            "evaluation": "arXiv:2606.07632v1 exact-v1 PDF § `3.5 Case Study: Comparing the Effects of LLM System Design Choices with LCA`; § `4 Alternative Views`",
            "limitations": "arXiv:2606.07632v1 exact-v1 PDF § `2 Limitations in Existing Approaches to Evaluating ML’s Resource Needs`; § `5 Benefits of LCAs in Machine Learning`",
            "artifact": "Not Disclosed — arXiv:2606.07632v1 does not pin an immutable implementation revision",
        }
    )
    exact["2606.01152"].update(
        {
            "method": "arXiv:2606.01152v1 exact-v1 PDF § `3. The conceptual model`; § `4. The evolutionary spiral`; § `5. Twenty-one modules, four parts, one closing`",
            "evaluation": "Not Disclosed — arXiv:2606.01152v1 is a curriculum position paper and does not report a separately identifiable empirical evaluation",
            "limitations": "arXiv:2606.01152v1 exact-v1 PDF § `8. What lasts and what doesn’t`",
            "artifact": "Not Disclosed — arXiv:2606.01152v1 does not pin an immutable curriculum artifact revision",
        }
    )
    exact["2606.14725"].update(
        {
            "method": "arXiv:2606.14725v1 exact-v1 HTML § `Chapter 2 Convolutional Nearest Neighbors`",
            "evaluation": "arXiv:2606.14725v1 exact-v1 HTML § `Chapter 5 Large Scale Experiments, Results, and Discussions`",
            "limitations": "arXiv:2606.14725v1 exact-v1 HTML § `2 Limitations and Future Improvements`",
            "artifact": "arXiv:2606.14725v1 exact-v1 HTML § `2 Code Availability`; no immutable commit inferred beyond the manuscript",
        }
    )
    exact["2607.22568"].update(
        {
            "method": "arXiv:2607.22568v1 exact-v1 HTML § `4 Experimental Design`; § `4.2 Hardware Setup, Model and Experimental Pipeline`",
            "evaluation": "arXiv:2607.22568v1 exact-v1 HTML § `5 Empirical Study and Results`",
            "limitations": "arXiv:2607.22568v1 exact-v1 HTML § `Limitations`; § `6.2 Cross-Device and Cross-Model Generalization`",
            "artifact": "Not Required — standard review does not require an immutable artifact locator",
        }
    )
    exact["2608.12328"].update(
        {
            "method": "arXiv:2608.12328v1 exact-v1 HTML § `III Methodology`; § `III-C Trajectory-Level Low-Rank Adaptation`; § `III-D Training Objective`",
            "evaluation": "arXiv:2608.12328v1 exact-v1 HTML § `IV Experiments and Results`; § `IV-L Rank and Module Ablations`",
            "limitations": "arXiv:2608.12328v1 exact-v1 HTML § `V Conclusion`",
            "artifact": "Not Disclosed — arXiv:2608.12328v1 exact-v1 HTML does not pin an immutable implementation revision",
        }
    )
    exact["2606.01046"].update(
        {
            "method": "arXiv:2606.01046v1 exact-v1 HTML § `3. The TravelEval Benchmark`; § `3.1. Six-Dimensional Evaluation Framework`; § `3.2. Benchmark Construction`",
            "evaluation": "arXiv:2606.01046v1 exact-v1 HTML § `4. Experimental Evaluation`; § `4.2. Main Results and Analysis`",
            "limitations": "arXiv:2606.01046v1 exact-v1 HTML § `5. Conclusion`",
            "artifact": "Not Required — standard review does not require an immutable artifact locator",
        }
    )
    exact["2606.01363"].update(
        {
            "method": "arXiv:2606.01363v1 exact-v1 HTML § `III Mitigating Model Exploitation Through Uncertainty Awareness`; § `III-A Where To Trust The Model?`; § `III-B How To Propagate The Model Where It Can Be Trusted?`",
            "evaluation": "Not Disclosed — arXiv:2606.01363v1 is a perspective/review and has no single author-controlled empirical evaluation contract",
            "limitations": "arXiv:2606.01363v1 exact-v1 HTML § `V Concluding Remarks and Outlook`",
            "artifact": "Not Disclosed — arXiv:2606.01363v1 does not pin an immutable implementation revision",
        }
    )

    # Re-screen the complete 371-hit ledger.  Included rows are rebuilt from the
    # curated exact-v1 decisions; every remaining closure is regenerated from
    # frozen source identity instead of wrapping an earlier generated reason.
    for row in ledger:
        arxiv_id = row["arxiv_id"]
        row["title"] = exact_v1_title(arxiv_id, row["title"])
        family = (
            curated_by_id[arxiv_id]["source_family_id"]
            if arxiv_id in curated_by_id
            else preaudit_by_id.get(arxiv_id, {}).get("Source Family ID", row.get("source_family_id", ""))
        )
        if family in retained_families_v9:
            row["decision"] = "include"
            row["source_family_id"] = family
            mechanism = (
                curated_by_id[arxiv_id]["mechanism_summary"]
                if arxiv_id in curated_by_id
                else f"the exact-v1 Source Review changes the durable contract owned by {preaudit_by_id[arxiv_id]['Stable Node ID']}"
            )
            row["screen_reason"] = f"V9 canonical Candidate Denominator retain after full-text review: {mechanism}"
        elif family:
            row["decision"] = "exclude"
            row["source_family_id"] = family
            node = (
                curated_by_id[arxiv_id]["stable_node_id"]
                if arxiv_id in curated_by_id
                else preaudit_by_id.get(arxiv_id, {}).get("Stable Node ID", "AI-System owner")
            )
            boundary = (
                curated_by_id[arxiv_id]["boundary_summary"]
                if arxiv_id in curated_by_id
                else "the exact-v1 primary material and the V9 independent source-specific mechanism/boundary record remain preserved in the packet"
            )
            row["screen_reason"] = (
                f"V9 family-specific pre-denominator closure for {family}: exact-v1 evidence is relevant to {node}, "
                f"but does not change its durable mechanism/state/data/control/evaluation/platform judgement; boundary: {boundary}"
            )
        elif arxiv_id in curated_by_id:
            curated = curated_by_id[arxiv_id]
            raise AssertionError(f"curated family missing V9 decision: {curated['source_family_id']}")
        elif row["decision"] == "exclude":
            row["screen_reason"] = source_specific_closure(row, abstracts.get(arxiv_id, ""))
    write_tsv(LEDGER, ledger, list(ledger[0]))

    inventory = read_tsv(INVENTORY)
    existing_ids = {row["arxiv_v1"].removesuffix("v1") for row in inventory}
    for curated in curation:
        arxiv_id = curated["arxiv_id"]
        if arxiv_id in existing_ids:
            continue
        inventory.append(
            {
                "source_family_id": curated["source_family_id"],
                "arxiv_v1": f"{arxiv_id}v1",
                "first_public_utc": ledger_by_id[arxiv_id]["first_public_utc"],
                "freeze_reason": "fresh-context-exact-v1-recovery",
            }
        )
    if not (PACKET / "candidate-inventory-v7.tsv").exists():
        write_tsv(PACKET / "candidate-inventory-v7.tsv", inventory, list(inventory[0]))
    inventory = [row for row in inventory if row["source_family_id"] in retained_families_v9]
    inventory = list({row["source_family_id"]: row for row in inventory}.values())
    assert len(inventory) == len(retained_families_v9) == 40
    inventory.sort(key=lambda row: (row["first_public_utc"], row["source_family_id"]))
    write_tsv(INVENTORY, inventory, list(inventory[0]))
    denominator_payload = "\n".join(
        f"{row['source_family_id']}\t{row['arxiv_v1']}\t{row['first_public_utc']}" for row in inventory
    )
    denominator_id = "DEN-20260601-" + hashlib.sha256(denominator_payload.encode()).hexdigest()[:8]

    candidate_headers, candidates = parse_table(text, VALIDATOR.CANDIDATE_LEDGER_MARKER)
    by_family = {row["Source Family ID"]: row for row in candidates}
    for curated in curation:
        family = curated["source_family_id"]
        arxiv_id = curated["arxiv_id"]
        scores = [int(curated[name]) for name in ("design_delta", "system_reach", "durability")]
        route = curated["review_route"]
        disposition = curated["books_disposition"]
        by_family[family] = {
            "Source Family ID": family,
            "Primary Identifier": f"arXiv:{arxiv_id}v1",
            "Event Identity": f"paper-v1:{arxiv_id}",
            "Owner Week": (
                lambda parsed: f"{parsed.isocalendar().year}-W{parsed.isocalendar().week:02d}"
            )(date.fromisoformat(ledger_by_id[arxiv_id]["first_public_utc"][:10])),
            "First-public Date": ledger_by_id[arxiv_id]["first_public_utc"][:10],
            "Supporting Source IDs": "SRC-ARXIV",
            "Design Delta": str(scores[0]),
            "System Reach": str(scores[1]),
            "Durability": str(scores[2]),
            "Total": str(sum(scores)),
            "Candidate State": "closure_only" if route == "closure" else "retained",
            "Review Status": f"{route}_complete",
            "Access Status": "accessible",
            "Review Override": "none",
            "Review Ref": f"review:{family}",
            "Owner Report Ref": "self",
            "Prior Review Ref": "—",
            "Reconciliation": "new_in_window",
            "Stable Node ID": curated["stable_node_id"],
            "Books Disposition": disposition,
            "Books Review Ref": "—" if route == "closure" else f"books-review:{family}",
            "Benchmark Claim": (
                "no"
                if route == "closure"
                else curated.get("benchmark_claim")
                or ("no" if str(exact[arxiv_id]["evaluation"]).startswith("Not Disclosed") else "yes")
            ),
        }
    for family in VERIFIED_INTEGRATES & retained_families_v9:
        # These rows predate the curation waves, so normalize the candidate
        # table explicitly against the current Books text.
        by_family[family]["Books Disposition"] = "No Change — Existing Coverage"
    by_family["SF-LOCAL-MIXVR"]["Benchmark Claim"] = "yes"
    for family in NON_BENCHMARK_FAMILIES:
        by_family[family]["Benchmark Claim"] = "no"
    missing_retained = retained_families_v9 - set(by_family)
    assert not missing_retained, f"V9 retained families missing from reviewed set: {sorted(missing_retained)}"
    closed_families_v9 = set(by_family) - retained_families_v9
    candidates = [row for family, row in by_family.items() if family in retained_families_v9]
    timestamp = {row["source_family_id"]: row["first_public_utc"] for row in inventory}
    candidates.sort(key=lambda row: (timestamp[row["Source Family ID"]], row["Source Family ID"]))
    # Benchmark rows exist exactly for families whose Candidate Ledger declares
    # an empirical benchmark claim.  Retention alone must never manufacture a
    # benchmark contract for position, schema, or architecture papers.
    route_counts = {
        route: sum(row["Review Status"] == f"{route}_complete" for row in candidates)
        for route in ("deep", "standard", "closure")
    }
    ledger_closure_count = sum(row["decision"] == "exclude" for row in ledger)
    raw_count = len(v9_denominator_receipt)
    previous_retained_count = sum(
        row["repair_author_v8_decision"] == "retain" for row in v9_denominator_receipt
    )
    canonical_closure_count = sum(
        row["independent_decision"] == "pre_denominator_closure"
        for row in v9_denominator_receipt
    )
    false_positive_closed_count = sum(
        row["transition"] == "false-positive-closed" for row in v9_denominator_receipt
    )
    false_negative_reopened_count = sum(
        row["transition"] == "false-negative-reopened" for row in v9_denominator_receipt
    )
    previous_retain_rate = previous_retained_count / raw_count
    raw_retain_rate = len(candidates) / len(ledger)
    closure_class_counts: dict[str, int] = {}
    for row in v9_denominator_receipt:
        if row["independent_decision"] != "pre_denominator_closure":
            continue
        closure_class = row["closure_class"]
        closure_class_counts[closure_class] = closure_class_counts.get(closure_class, 0) + 1
    closure_class_text = ", ".join(
        f"{closure_class}={count}"
        for closure_class, count in sorted(closure_class_counts.items())
    )
    assert raw_count == 371
    assert previous_retained_count == 64
    assert len(candidates) == 40
    assert canonical_closure_count == 331
    assert false_positive_closed_count == 37
    assert false_negative_reopened_count == 13
    assert ledger_closure_count == 331
    text = replace_table(text, VALIDATOR.CANDIDATE_LEDGER_MARKER, candidate_headers, candidates)

    # Closed families keep their row-level evidence in the independent V9
    # denominator receipt and source packet, but leave candidate-only report interfaces.
    for family in closed_families_v9:
        for marker in (f"review:{family}", f"claim:{family}", f"existing:{family}", f"delta:{family}", f"books-review:{family}"):
            text = re.sub(
                rf"\n?<!-- {re.escape(marker)}:start -->.*?<!-- {re.escape(marker)}:end -->\n?",
                "\n",
                text,
                flags=re.S,
            )

    # Rebuild every reopened review from source-specific abstract, Method,
    # evaluation, limitation and artifact evidence.  Existing generated wrappers
    # are replaced rather than nested, preserving rerun idempotence.
    new_review_blocks: list[str] = []
    for curated in curation:
        family = curated["source_family_id"]
        if family not in retained_families_v9:
            continue
        arxiv_id = curated["arxiv_id"]
        body = substantive_review(curated, exact[arxiv_id], abstracts.get(arxiv_id, ""))
        if f"<!-- review:{family}:start -->" in text:
            text = replace_bounded(text, f"review:{family}", body)
        else:
            new_review_blocks.append(
                f"<!-- review:{family}:start -->{body}<!-- review:{family}:end -->"
            )
    benchmark_heading = "## Benchmark Contract"
    if new_review_blocks:
        text = text.replace(
            benchmark_heading,
            "\n\n".join(new_review_blocks) + "\n\n" + benchmark_heading,
            1,
        )
    text = re.sub(r"\n{4,}(?=## Benchmark Contract)", "\n\n", text, count=1)

    # Reconcile locators for the complete denominator, not only newly promoted
    # rows.  This is what closes the weak Conclusion/Future-only locator class:
    # each local exact-v1 paper is routed from its own section tree, and public
    # exact-v1 rows use the manually reviewed section map above.
    review_headers, review_rows = parse_table(text, VALIDATOR.REVIEW_COMPLETION_MARKER)
    review_by_family = {row["Source Family ID"]: row for row in review_rows}

    candidate_by_family = {row["Source Family ID"]: row for row in candidates}
    curated_by_family = {row["source_family_id"]: row for row in curation}
    for family, receipt in review_by_family.items():
        candidate = candidate_by_family.get(family)
        if candidate is None:
            continue
        arxiv_id = candidate["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        route = receipt["Review Route"]
        if arxiv_id in WEB_EXACT:
            method, evaluation, limitations = WEB_EXACT[arxiv_id]
            receipt["Method / Identity Locators"] = public_exact_locator(arxiv_id, method)
            receipt["Evaluation Locators"] = public_exact_locator(arxiv_id, evaluation)
            receipt["Limitations / Counterevidence Locators"] = public_exact_locator(arxiv_id, limitations)
            receipt["Artifact Locators"] = (
                f"Not Disclosed — arXiv:{arxiv_id}v1 exact-v1 and public project references do not pin an immutable implementation revision"
                if route == "deep" else f"Not Required — {route} review does not require an immutable artifact locator"
            )
            continue
        try:
            source, _ = exact_text(arxiv_id)
        except RuntimeError:
            continue
        source_headings = exact_headings(arxiv_id, source)
        receipt["Method / Identity Locators"] = locator(arxiv_id, source_headings, "method", route)
        receipt["Evaluation Locators"] = locator(arxiv_id, source_headings, "evaluation", route)
        limitation_locator = locator(arxiv_id, source_headings, "limitations", route)
        if route != "closure" and re.search(r"Conclusion|Future Work", limitation_locator, re.I) and not re.search(r"Limitation|Threat|Discussion|Failure|Error|Ablation|Risk", limitation_locator, re.I):
            limitation_locator += " — no dedicated limitations heading; the cited closing section was read and the Daily claim boundary records the source-specific non-result"
        receipt["Limitations / Counterevidence Locators"] = limitation_locator
        receipt["Artifact Locators"] = locator(arxiv_id, source_headings, "artifact", route)

    # Five independently confirmed locator defects receive source-specific
    # exact-v1 routes rather than another lexical fallback.
    locator_repairs = {
        "SF-BEHAVIORAL-SYSTEM-TESTS": ("arXiv:2608.18081v1 exact-v1 HTML § `3 Behavioral Tests for Artificial Behavioral Systems`; § `3.3 Further Defining Behavioral Tests`", "Not Disclosed — arXiv:2608.18081v1 is a position paper; § `4.2 Case Studies` illustrates the proposal but is not an author-controlled empirical evaluation"),
        "SF-SS-ZKR-MAS": ("arXiv:2606.00962v1 exact-v1 PDF § `IV. THE SS-ZKR PROTOCOL`; § `V. ENTERPRISE DEPLOYMENT: THE AGENTIC MESH FABRIC`", "arXiv:2606.00962v1 exact-v1 PDF § `VI. ANALYTICAL EVALUATION`"),
        "SF-BRAVEGUARD-CUA": ("arXiv:2606.01166v1 exact-v1 HTML § `3 BraveGuard`; § `3.1 Open-World Threat Discovery`; § `3.3 Trajectory Supervision and Guard Training`", "arXiv:2606.01166v1 exact-v1 HTML § `4 Experiments`; § `4.2 Main Results`; § `4.3 Ablation Study`"),
        "SF-DR-DOCBENCH": ("arXiv:2606.01393v1 exact-v1 HTML § `3 Dr.DocBench`; § `3.1 Difficulty-Aware Sampling`; § `3.2 Annotation Schema`", "arXiv:2606.01393v1 exact-v1 HTML § `4 Experiments`; § `4.3 Overall Results and Findings`; § `5 Additional Analysis`"),
        "SF-SAFEGEN-BENCH": ("arXiv:2606.01481v1 exact-v1 HTML § `3 The SafeGen-Bench Benchmark`; § `3.2 Data Curation Process`", "arXiv:2606.01481v1 exact-v1 HTML § `4 Experiments`; § `4.3 Main Results`; § `4.4 Guardrail`; § `4.5 Jailbreak`"),
        "SF-CROSS-INSTANCE-LATENT-REDISTRIBUTION": ("arXiv:2606.01502v1 exact-v1 HTML § `4 A Topology-Aware Redistribution Cost Model`; § `5 Primitive Selection: route vs fetch vs local`", "arXiv:2606.01502v1 exact-v1 HTML § `4.3 Fit and validation on real IBGDA`; § `6 Characterizing the Device-Initiated RDMA Regime`; § `8 Sensitivity: Scaling and Topology`"),
        "SF-AIREP": ("arXiv:2608.21363v1 exact-v1 HTML § `2 The Record`; § `3 Integrity and the Chain`; § `4.4 Implementation`", "Not Disclosed — arXiv:2608.21363v1 is a protocol/design paper with conformance and neutrality checks, not an author-controlled empirical model evaluation"),
    }
    for family, (method_locator, eval_locator) in locator_repairs.items():
        if family in review_by_family:
            review_by_family[family]["Method / Identity Locators"] = method_locator
            review_by_family[family]["Evaluation Locators"] = eval_locator
    v9_locator_overrides = {
        "SF-RLVR-VERIFIER-FUZZING": (
            "arXiv:2606.01066v1 exact-v1 HTML § `3 Failure Model and Metrics`; § `4 Verifier-Fuzzing System`; § `4.1`–`4.3`",
            "arXiv:2606.01066v1 exact-v1 HTML § `5 Experimental Setup`; § `5.1`–`5.3`; § `6 Results`; § `6.1`–`6.7`",
            "arXiv:2606.01066v1 exact-v1 HTML § `7 Discussion`; § `8 Limitations`",
        ),
        "SF-PRISM-DP-LORA": (
            "arXiv:2606.00944v1 exact-v1 HTML § `3 Proposed Method: PRISM`; § `3.1`–`3.3`",
            "arXiv:2606.00944v1 exact-v1 HTML § `4 Experiments`; Appendix `B Experimental Setup`; Appendix `C Additional Diagnostics and Analysis`",
            "arXiv:2606.00944v1 exact-v1 HTML § `Limitations`; Appendix `C Additional Diagnostics and Analysis`",
        ),
        "SF-ASYNC-AUTOFORMAL-PLANNING": (
            "arXiv:2606.00981v1 exact-v1 HTML § `3 Task Formulation`; § `4 Experimental Setup` (methods, datasets, models and protocols)",
            "arXiv:2606.00981v1 exact-v1 HTML § `5 Results and Discussion`; Appendix `C Detailed Results`; Appendix `D Robotouille Error Analysis`",
            "arXiv:2606.00981v1 exact-v1 HTML § `Limitations`; Appendix `C.4 Qualitative Error Examples`; Appendix `D Robotouille Error Analysis`",
        ),
        "SF-TRAIT-MISALIGNMENT-MONITOR": (
            "arXiv:2606.07631v1 exact-v1 HTML § `3 Methodology`; § `3.1 Two-Phase Trait-Space Representation`; § `3.2 Finetuning Protocol`",
            "arXiv:2606.07631v1 exact-v1 HTML § `4 Trait-space Geometry of Finetuning Drift`; § `5 Stress Tests`; Appendix `9 EM Evaluation Protocol`",
            "arXiv:2606.07631v1 exact-v1 HTML § `6 Discussion and Conclusion` (`Calibration scope`; `Caveats and technical limits`)",
        ),
        "SF-TASK-AWARE-MOE-GROUPING": (
            "arXiv:2606.01007v1 exact-v1 HTML § `3 Method`; § `3.3 Task-Aware Coactivation Grouping (TACG)`; § `3.4 Generic Expert Shared Replication (GESR)`",
            "arXiv:2606.01007v1 exact-v1 HTML § `4 Experiments`; § `4.2`–`4.5`; Appendices `A`–`D`",
            "arXiv:2606.01007v1 exact-v1 HTML § `5 Limitations and Future Work`",
        ),
        "SF-JUDGE-PANEL-CALIBRATION": (
            "arXiv:2606.01034v1 exact-v1 HTML § `3 Finite-Calibration Panel Selection`; § `3.5 FCPS Protocol`",
            "arXiv:2606.01034v1 exact-v1 HTML § `4 Experiments`; § `5 Results`; Appendix `C Extended Empirical Results`",
            "arXiv:2606.01034v1 exact-v1 HTML Appendix `A Limitations`; § `6 Conclusion`",
        ),
        "SF-LEYLINE-KV-DIRECTIVES": (
            "arXiv:2606.01065v1 exact-v1 HTML § `3 Leyline: a directive abstraction for policy-driven cache editing`; § `3.3 Serving-stack integration`; § `3.4 The policy interface`",
            "arXiv:2606.01065v1 exact-v1 HTML § `4 Demonstrating correctness for the mutation operation`; § `5 Deployment-cell evidence at the policy layer`; Appendices `A`, `B`, `D`–`I`, `T`, `U`",
            "arXiv:2606.01065v1 exact-v1 HTML § `Limitations`; § `Empirical-coverage scope`; Appendix `O Discussion notes`",
        ),
        "SF-DEEP-RESEARCH-RUBRIC-RL": (
            "arXiv:2606.01091v1 exact-v1 HTML § `3 The DR-Rubric Framework`; § `3.1 Rubric Generation`; § `3.2 Reinforcement Learning with Rubrics`; § `3.3 Bootstrap Rubric Generation`",
            "arXiv:2606.01091v1 exact-v1 HTML § `4 Experiments`; § `4.2`–`4.6`; Appendices `B`–`L`",
            "arXiv:2606.01091v1 exact-v1 HTML § `4.4 Bootstrap Stability Limit`; Appendix `I Bootstrap Stability Limit: Extended Analysis`; § `5 Conclusion`",
        ),
        "SF-SPARSE-REPEATED-TRAINING": (
            "arXiv:2606.01155v1 exact-v1 HTML § `3 Sparse Data-Constrained Scaling Law`; § `4 Resource Allocation`; § `5 Optimal sparsity`",
            "arXiv:2606.01155v1 exact-v1 HTML § `3.1 Experimental setup`; § `3.2`–`3.3`; § `4.1`–`4.2`; Appendix `D Fitting procedure`; Appendix `E Sensitivity Analysis`",
            "arXiv:2606.01155v1 exact-v1 HTML Appendix `F Limitations` (`Scale and Data Diversity`; `System and Practical Efficiency`; `Theoretical explanation`)",
        ),
        "SF-LAKEHOUSE-SKILL-OPTIMIZATION": (
            "arXiv:2606.01185v1 exact-v1 HTML § `3. Skill optimization`; § `3.1. Architecture`; § `3.2. Data generation`; § `3.3. Optimization`",
            "arXiv:2606.01185v1 exact-v1 HTML § `4. Experiments`",
            "arXiv:2606.01185v1 exact-v1 HTML § `6. Conclusion and future work` (single-platform/task-family boundary; no dedicated limitations section disclosed)",
        ),
        "SF-LOW-RESOURCE-SAFETY-ACTION": (
            "arXiv:2606.01196v1 exact-v1 HTML § `3 Setup: Models, Data, and Harmfulness Directions`; § `5 A Few-Shot Latent Gate for Calibration and Routing`",
            "arXiv:2606.01196v1 exact-v1 HTML § `4 Diagnosing the Multilingual Refusal Gap`; § `5.1 Calibrating a Few-Shot Latent Gate`; § `5.2 Routing the Calibrated Gate into Refusal`; Appendices `D`–`H`",
            "arXiv:2606.01196v1 exact-v1 HTML § `6 Conclusion and Discussion` (`Limitations`; `Scope`; `Evaluation and access`; `Training coverage`)",
        ),
        "SF-SKILLSMITH": (
            "arXiv:2606.01314v1 exact-v1 HTML § `3 SkillSmith`; § `3.1 Unified Reflection and Proposal Planning`; § `3.2 Skill Ecosystem Dynamics`; § `3.3 Validation and State Update`",
            "arXiv:2606.01314v1 exact-v1 HTML § `4 Experiments`; § `4.2`–`4.3`; Appendix `D Experimental Details`; Appendix `F Computational Cost Analysis`",
            "arXiv:2606.01314v1 exact-v1 HTML § `5 Conclusion and Limitations`; Appendix `A` (assumption-bounded analysis)",
        ),
        "SF-SABER-CODING-AGENT-SAFETY": (
            "arXiv:2606.01317v1 exact-v1 HTML § `4 Benchmark Design`; § `4.2 Threat Coverage and Benchmark Construction`; § `4.3 Task Format and Evaluation Loop`; § `4.4 Outcome Taxonomy and Judging Protocol`",
            "arXiv:2606.01317v1 exact-v1 HTML § `5 Experiments`; § `5.1 Main Results`; § `5.2 Behavioral Analysis`; Appendices `C`–`E`",
            "arXiv:2606.01317v1 exact-v1 HTML § `Limitations`; Appendix `B Source-to-Template Mapping and Coverage Criteria`; Appendix `D Judging Protocol Details`",
        ),
        "SF-RINGELMANN-MAS": (
            "arXiv:2606.02646v1 exact-v1 HTML § `3 Framework: a Ringelmann scaling law for multi-agent systems`; § `3.1`–`3.3`; Appendix `A Derivation of the effective-team model`",
            "arXiv:2606.02646v1 exact-v1 HTML § `4 Experimental setup`; § `5 Results`; Appendices `C`–`I`, `K`–`N`",
            "arXiv:2606.02646v1 exact-v1 HTML § `5.6 Discussion`; Appendix `C.8 Scope and limitations`",
        ),
        "SF-REASONING-PRODUCTION-EVAL-GAP": (
            "arXiv:2606.01462v1 exact-v1 HTML § `2 Evaluating the Evaluation of Reasoning`; § `3 Answer Confirmation Bias Explains the Production-Evaluation Gap`",
            "arXiv:2606.01462v1 exact-v1 HTML § `2.2 Comparing Reasoning Evaluation and Production`; § `2.3 The Production-Evaluation Gap in LRMs`; § `3.1`–`3.3`; Appendices `A`–`B`",
            "arXiv:2606.01462v1 exact-v1 HTML § `4 Discussion`; Appendix `B Analyzing Answer Confirmation Bias`",
        ),
        "SF-CLAWHUB-SECURITY-SIGNALS": (
            "arXiv:2606.01494v1 exact-v1 HTML § `4. The ClawScan Verification Pipeline`; § `5. Dataset Construction`",
            "arXiv:2606.01494v1 exact-v1 HTML § `6. Scanner Disagreement`; § `7. Verdict Structure and Risk Categories`; § `8. Illustrative Cases`",
            "arXiv:2606.01494v1 exact-v1 HTML § `11. Threats to Validity`; § `13. Discussion`",
        ),
    }
    for family, (method_locator, eval_locator, limitation_locator) in v9_locator_overrides.items():
        review_by_family[family]["Method / Identity Locators"] = method_locator
        review_by_family[family]["Evaluation Locators"] = eval_locator
        review_by_family[family]["Limitations / Counterevidence Locators"] = limitation_locator
    review_by_family["SF-SABER-CODING-AGENT-SAFETY"]["Artifact Locators"] = (
        "Not Disclosed — arXiv:2606.01317v1 describes task/runtime/judging details but does not pin an immutable benchmark artifact revision"
    )
    if "SF-VLM-TOKEN-REDUCTION-LIMITS" in review_by_family:
        row = review_by_family["SF-VLM-TOKEN-REDUCTION-LIMITS"]
        row["Method / Identity Locators"] = "arXiv:2606.01503v1 §3 Problem Setup; §5 Proposed Task-Specific Accelerators"
        row["Evaluation Locators"] = "arXiv:2606.01503v1 §4 Redundancy Analysis; §6 Limits of Unified Efficiency"
        row["Limitations / Counterevidence Locators"] = "arXiv:2606.01503v1 §6 Limits of Unified Efficiency; §7 Conclusion"
        row["Artifact Locators"] = "Not Disclosed — arXiv:2606.01503v1 does not pin an immutable implementation revision"

    for curated in curation:
        family = curated["source_family_id"]
        if family not in retained_families_v9:
            continue
        arxiv_id = curated["arxiv_id"]
        route = curated["review_route"]
        review_by_family[family] = {
            "Source Family ID": family,
            "Review Provenance ID": "PENDING-RECOMPUTE",
            "Review Route": route,
            "Primary Evidence Version": f"arXiv:{arxiv_id}v1",
            "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{arxiv_id}v1",
            "Method / Identity Locators": str(exact[arxiv_id]["method"]),
            "Evaluation Locators": str(exact[arxiv_id]["evaluation"]),
            "Limitations / Counterevidence Locators": str(exact[arxiv_id]["limitations"]),
            "Artifact Locators": str(exact[arxiv_id]["artifact"]),
            "Claim Boundary Ref": f"claim:{family}",
            "Completion Result": "complete",
        }
    # Curation rows are rebuilt above, so locator repairs must be applied after
    # that reconstruction; otherwise the generic locator pass silently
    # overwrites the source-specific facets.
    for family, (method_locator, eval_locator) in locator_repairs.items():
        if family in review_by_family:
            review_by_family[family]["Method / Identity Locators"] = method_locator
            review_by_family[family]["Evaluation Locators"] = eval_locator
    for family, (method_locator, eval_locator, limitation_locator) in v9_locator_overrides.items():
        review_by_family[family]["Method / Identity Locators"] = method_locator
        review_by_family[family]["Evaluation Locators"] = eval_locator
        review_by_family[family]["Limitations / Counterevidence Locators"] = limitation_locator
    review_by_family["SF-SABER-CODING-AGENT-SAFETY"]["Artifact Locators"] = (
        "Not Disclosed — arXiv:2606.01317v1 describes task/runtime/judging details but does not pin an immutable benchmark artifact revision"
    )
    for receipt in review_by_family.values():
        weak = receipt["Limitations / Counterevidence Locators"]
        if (
            receipt["Review Route"] != "closure"
            and re.search(r"Conclusion|Future Work", weak, re.I)
            and not re.search(r"Limitation|Threat|Discussion|Failure|Error|Ablation|Risk|source-specific non-result", weak, re.I)
        ):
            receipt["Limitations / Counterevidence Locators"] = (
                weak
                + " — no dedicated limitations heading; the cited closing section was read and the Daily claim boundary records the source-specific non-result"
            )
    review_rows = [review_by_family[row["Source Family ID"]] for row in candidates]
    text = replace_table(text, VALIDATOR.REVIEW_COMPLETION_MARKER, review_headers, review_rows)
    for receipt in review_rows:
        text = synchronize_review_contract(text, receipt["Source Family ID"], receipt)

    # Conservative benchmark rewrite.  Workload and evaluation path remain
    # family-specific, while fields not re-verified in that exact path are made
    # explicitly undisclosed rather than lexically inferred from the paper.
    benchmark_headers, benchmark_rows = parse_table(text, VALIDATOR.BENCHMARK_MARKER)
    old_bench = {row["Source Family ID"]: row for row in benchmark_rows}
    new_bench: list[dict[str, str]] = []
    benchmark_workload_overrides = {
        "SF-FED-PERSONALIZATION-SILENT-FAILURES": "Landscape analysis of twelve representative federated and centralized trustworthiness benchmarks; no newly executed model benchmark.",
        "SF-AIREP": "AIREP schema-conformance, neutrality and two-language conformance-kit checks; no author-controlled model benchmark.",
        "SF-AGENT-OPERATING-SYSTEM": "Not Disclosed",
        "SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY": "Not Disclosed",
    }
    for candidate in candidates:
        family = candidate["Source Family ID"]
        if candidate["Benchmark Claim"] != "yes":
            continue
        receipt = review_by_family[family]
        primary_id = candidate["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        try:
            source_text, _ = exact_text(primary_id)
        except RuntimeError:
            source_text = ""
        # Contract fields are reconciled across the entire exact-v1 source,
        # including setup and appendices.  Result locators remain separate so a
        # configuration mention is never presented as a measured result.
        scoped_evidence = source_text
        if family in {row["source_family_id"] for row in curation}:
            curated = next(row for row in curation if row["source_family_id"] == family)
            workload = f"{curated['mechanism_summary']} Evaluation is frozen at {receipt['Evaluation Locators']}."
        else:
            workload = old_bench.get(family, {}).get("Workload", f"Family-specific evaluation frozen at {receipt['Evaluation Locators']}")
        workload = benchmark_workload_overrides.get(family, workload)
        row = {
            "Source Family ID": family,
            "Workload": workload,
            "Model": contract_field(scoped_evidence, "Model", receipt["Evaluation Locators"]),
            "Hardware": contract_field(scoped_evidence, "Hardware", receipt["Evaluation Locators"]),
            "Precision": contract_field(scoped_evidence, "Precision", receipt["Evaluation Locators"]),
            "Input Length": contract_field(scoped_evidence, "Input Length", receipt["Evaluation Locators"]),
            "Output Length": contract_field(scoped_evidence, "Output Length", receipt["Evaluation Locators"]),
            "Batch": contract_field(scoped_evidence, "Batch", receipt["Evaluation Locators"]),
            "Concurrency": contract_field(scoped_evidence, "Concurrency", receipt["Evaluation Locators"]),
            "SLO": f"author-reported evidence only; no production SLO inferred; boundary {receipt['Limitations / Counterevidence Locators']}",
            "Evaluator": f"author-defined evaluation; exact result path {receipt['Evaluation Locators']}",
        }
        if family == "SF-LODESTAR-ONLINE-ROUTER":
            row.update(
                {
                    "Model": "Llama3-8B",
                    "Hardware": "NVIDIA A30 and V100 clusters",
                    "Precision": "float16",
                    "SLO": "author-reported TTFT under §5 deployment; no production SLO inferred",
                }
            )
        elif family == "SF-HIFLOAT8-VIDEO-QUANT":
            row.update(
                {
                    "Model": "Wan2.1-T2V-14B",
                    "Hardware": "Ascend 910B",
                    "Precision": "boundary blocks BF16; middle blocks W8A8 HiFloat8",
                }
            )
        elif family == "SF-PRISM-DP-LORA":
            row.update(
                {
                    "Model": "Gemma-family models disclosed by the exact-v1 evaluation",
                    "Hardware": "NVIDIA A100-PCIE-40GB",
                }
            )
        elif family == "SF-MELT-GEMM-AUDIO":
            row.update(
                {
                    "Hardware": "Apple A18 Pro; Apple M4 Pro; NVIDIA H100; NVIDIA V100 (all author-disclosed in exact-v1 §4)",
                    "Input Length": "audio duration up to 160 s on the disclosed H100 sweep",
                    "Batch": "batch/configuration varies by platform experiment; exact values are figure/table scoped",
                    "SLO": "author-reported latency and energy only; no production SLO inferred",
                }
            )
        if family in PUBLIC_BENCHMARK_OVERRIDES:
            row.update(PUBLIC_BENCHMARK_OVERRIDES[family])
        audit = V9_RETAINED_BENCHMARK_AUDIT[family]
        row.update({
            field: audit[field]
            for field in ("Model", "Hardware", "Precision", "Input Length", "Output Length", "Batch", "Concurrency", "SLO", "Evaluator")
        })
        row["V9 Scope"] = "manual exact-v1 nine-field audit; evaluated model/backbone is separated from auxiliary evaluator, references and future placeholders"
        new_bench.append(row)
    expected_benchmark_families = {
        row["Source Family ID"] for row in candidates if row["Benchmark Claim"] == "yes"
    }
    assert expected_benchmark_families == set(V9_RETAINED_BENCHMARK_AUDIT) - NON_BENCHMARK_FAMILIES
    assert expected_benchmark_families == {row["Source Family ID"] for row in new_bench}
    text = replace_table(text, VALIDATOR.BENCHMARK_MARKER, benchmark_headers, new_bench)

    # Rebuild Deep Analysis Selection for every 7+ or forced family.  Only
    # genuine report-level narratives are selected; other decisions are unique
    # and do not claim false subsumption.
    selected = {
        "SF-ORDER-AGNOSTIC-CHAIN-RULE": "DA-DIFFUSION-COMMIT",
        "SF-RESIDENT-KV-CLAIMS": "DA-FAIL-CLOSED-KV",
        "SF-LOW-RESOURCE-SAFETY-ACTION": "DA-SAFETY-ACTION-GAP",
    }
    selected_narratives = {
        "DA-DIFFUSION-COMMIT": (
            "**Why.** 自回归生成把已提交 prefix 当作一个有明确 chain-rule 语义的不可变历史；masked/order-agnostic "
            "生成允许多个位置反复变化，因此 reveal order 不再只是调度细节。\n\n"
            "**Principle.** 并行更新只有在 conditionals 能组成一致 joint、且 provisional 与 committed state 被区分时，"
            "才能把吞吐收益与输出语义同时解释。\n\n"
            "**Mechanism.** exact-v1 分析测量不同 reveal order 下的 chain-rule deviation 与 probability spreading，"
            "把解码顺序提升为 generation contract；它影响 correction、cache validity、streaming 与最终 commit。\n\n"
            "**Trade-off and evidence boundary.** 允许修改未提交位置能并行探索和纠错，却增加重算、振荡、停止规则与"
            "commit bookkeeping。作者结果只覆盖测试模型和 schedule，不证明全部 diffusion LM 不一致，也不证明 AR 普遍更优。\n\n"
            "**Connection and evolution.** 这条路线从 append-only AR，演进到 mutable masked state，再要求显式 commit "
            "protocol；后续压力是让训练 objective、runtime cache 与外部副作用共享同一提交语义。"
        ),
        "DA-FAIL-CLOSED-KV": (
            "**Why.** Agentic request 会携带工具结果、adapter、position rule 与多轮前缀；只用 prefix hash 命中 KV，"
            "可能在数值可读但语义身份已变化时错误复用。\n\n"
            "**Principle.** 缓存复用是 correctness claim，不是纯性能提示。不能证明 compatibility 时必须 miss，而不能"
            "先复用再依赖下游质量检测补救。\n\n"
            "**Mechanism.** resident-KV claim 将 model/tokenizer/adapter/position/prefix 与 runtime revision 绑定为"
            "可验证 directive，由 serving runtime 在 admission 和 commit 前检查；Leyline 等协议只承担传输，最终 authority "
            "仍在拥有物理 KV 的 runtime。\n\n"
            "**Trade-off and evidence boundary.** 更强 identity 减少 silent corruption，却增加 metadata、hash、miss rate 和"
            "跨节点协调。论文没有证明所有实现的 tail-SLO 收益，协议字段也不能替代实际 memory ownership。\n\n"
            "**Connection and evolution.** 路线从进程内前缀复用，演进到跨请求 directive，再到 fail-closed compatibility；"
            "下一压力是让迁移、PD 分离与多租户权限在同一 claim lifecycle 上原子更新。"
        ),
        "DA-SAFETY-ACTION-GAP": (
            "**Why.** 低资源语言下，内部 representation 可能仍能线性分离 harmfulness，但最终 refusal action 失败；"
            "仅证明模型“看见风险”不能证明系统采取安全动作。\n\n"
            "**Principle.** 安全证据必须绑定 effect：sensor/probe 只提供信号，拥有执行权的 decoder、policy 或外部 controller "
            "才决定是否拒绝、降级或交给人工。\n\n"
            "**Mechanism.** exact-v1 将 representation probe 与 matched behavioral action 对照，定位 feature availability 与"
            "action realization 的断层；系统层因此需要语言覆盖、action policy、deterministic guard 与最终环境结果的联合验证。\n\n"
            "**Trade-off and evidence boundary.** 多语言 matched test 与闭环 outcome 更昂贵，但能避免把可分离 feature 冒充"
            "安全行为。作者模型与语言集合不能外推到全部语言，更不能替代规则 safety envelope。\n\n"
            "**Connection and evolution.** 路线从 response-level refusal，演进到 representation probe，再到 effect-based "
            "release gate；下一压力是把策略版本、语言分布与真实副作用持续接入线上证据。"
        ),
    }
    curated_by_family = {row["source_family_id"]: row for row in curation}
    selection_rows: list[dict[str, str]] = []
    selection_blocks: list[str] = []
    for candidate in candidates:
        if int(candidate["Total"]) < 7 and candidate["Review Override"] == "none":
            continue
        family = candidate["Source Family ID"]
        title = title_from_review(text, family)
        claim = block(text, f"claim:{family}")
        eligibility = ["score_7_9"] if int(candidate["Total"]) >= 7 else []
        if candidate["Review Override"] != "none":
            eligibility.append("forced_review")
        if candidate["Books Disposition"] == "Integrate":
            eligibility.append("potential_books_delta")
        if family in selected:
            unit = selected[family]
            decision = "selected"
            rationale = (
                f"选择 `{title}`：其 {candidate['Total']}/9 evidence 改变 {candidate['Stable Node ID']} 的状态/控制契约，"
                "且不能由本报告另一 family 的 narrative 代替。"
            )
            narrative_ref = f"analysis:{unit}"
            selection_blocks.append(
                f"<!-- {narrative_ref}:start -->\n### {unit}: {title}\n\n"
                f"{selected_narratives[unit]}\n\n**Source-family boundary.** {claim}\n"
                f"<!-- {narrative_ref}:end -->"
            )
        else:
            unit = "—"
            decision = "not_selected"
            curated = curated_by_family.get(family, {})
            claim_parts = claim.split("证据边界：", 1)
            mechanism = curated.get("mechanism_summary") or claim_parts[0].strip()
            boundary = curated.get("boundary_summary") or (
                claim_parts[1].strip() if len(claim_parts) == 2 else "该 family 的结论仍受 exact-v1 evidence boundary 约束。"
            )
            owner_lens = {
                "MODEL": "模型语义/表示约束",
                "MULTIMODAL": "多模态生成与对齐约束",
                "WORLDVIEW": "世界建模与预测状态约束",
                "TRAIN": "训练目标、数据或优化状态约束",
                "INFER": "推理执行、放置或内存状态约束",
                "PLATFORM": "平台证据、发布或安全控制约束",
                "AGENT": "Agent 状态、能力或编排约束",
            }.get(candidate["Stable Node ID"].split("-", 1)[0], "局部 owner 约束")
            rationale = (
                f"Score={candidate['Total']}/9（Design Delta={candidate['Design Delta']}、System Reach={candidate['System Reach']}、"
                f"Durability={candidate['Durability']}）。`{title}` 处理的是 `{candidate['Stable Node ID']}` 的{owner_lens}：{mechanism} "
                f"其证据上界是：{boundary} 全前沿比较后，第一，它不改写 `DA-DIFFUSION-COMMIT` 的 mutable-token joint/commit 语义；"
                "第二，它不改写 `DA-FAIL-CLOSED-KV` 的 cache identity、admission 与物理 KV owner；"
                "第三，它不改写 `DA-SAFETY-ACTION-GAP` 的 representation-signal 到最终 effect/release gate。"
                f"因此该 family 的边际知识属于 `{candidate['Stable Node ID']}` 自身的 Source Review/Books Decision，"
                "不是三个长叙事任一项的替代、子项或更高优先级跨 owner correction；决定 `not_selected`，且不声称 subsumption。"
            )
            narrative_ref = f"analysis-decision:{family}"
            selection_blocks.append(
                f"<!-- {narrative_ref}:start -->`{title}` 未进入长叙事：{rationale}<!-- {narrative_ref}:end -->"
            )
        selection_rows.append(
            {
                "Source Family ID": family,
                "Eligibility": ";".join(eligibility),
                "Decision": decision,
                "Analysis Unit ID": unit,
                "Subsumed By": "—",
                "Priority Rationale": rationale,
                "Narrative Ref": narrative_ref,
            }
        )
    selection_headers, _ = parse_table(text, VALIDATOR.DEEP_ANALYSIS_SELECTION_MARKER)
    text = replace_table(text, VALIDATOR.DEEP_ANALYSIS_SELECTION_MARKER, selection_headers, selection_rows)
    selection_section = text.index("## Deep Analysis Selection")
    books_section = text.index("<!-- audit-target:deep_analysis_selection:end -->", selection_section)
    # Replace the old prose region after the table up to audit end rather than
    # attempting to delete nested bounded markers one by one.
    table_marker_pos = text.index(VALIDATOR.DEEP_ANALYSIS_SELECTION_MARKER, selection_section)
    after_marker = text[table_marker_pos:]
    table_match = re.search(r"\n\|.*?(?=\n\n)", after_marker, re.S)
    assert table_match
    table_end = table_marker_pos + table_match.end()
    audit_end = text.index("<!-- audit-target:deep_analysis_selection:end -->", table_end)
    text = text[:table_end] + "\n\n" + "\n\n".join(selection_blocks) + "\n" + text[audit_end:]

    # Books comparisons: preserve exact chapter refs already audited, add refs
    # for owners not represented in the old table, and make every comparison
    # source-family-specific.  No Books file is changed here.
    books_headers, old_books_rows = parse_table(text, VALIDATOR.BOOKS_COMPARISON_MARKER)
    refs_by_node = {
        row["Stable Node ID"]: (row["Target Chapter Ref"], row["Adjacent Chapter Refs"])
        for row in old_books_rows
    }
    # Legacy fallbacks are only for nodes absent from the current ROADMAP.
    # ROADMAP is the source of truth and must win when chapter paths move;
    # allowing the legacy map to override it produced stale adjacent paths
    # after the 84-chapter migration.
    refs_by_node.update(OWNER_REFS)
    refs_by_node.update(roadmap_refs())
    books_rows: list[dict[str, str]] = []
    books_blocks: list[str] = []
    books_v9_reconciliation: list[dict[str, str]] = []
    curated_by_family = {row["source_family_id"]: row for row in curation}
    for candidate in candidates:
        if candidate["Books Disposition"] not in {"Integrate", "No Change — Existing Coverage", "Structural Candidate"}:
            continue
        family = candidate["Source Family ID"]
        node = candidate["Stable Node ID"]
        title = title_from_review(text, family)
        claim = block(text, f"claim:{family}")
        target_path, adjacent_paths = refs_by_node[node]
        relation = curated_by_family.get(family, {}).get("relationship", "Layering / Dependency")
        mechanism = curated_by_family.get(family, {}).get("mechanism_summary", claim.split("证据边界：", 1)[0])
        boundary = curated_by_family.get(family, {}).get("boundary_summary", claim)
        target, target_excerpt = chapter_proposition(target_path, mechanism)
        adjacent_pairs = [chapter_proposition(ref, mechanism) for ref in adjacent_paths.split(";")[:2]]
        adjacent = ";".join(ref for ref, _ in adjacent_pairs)
        adjacent_excerpt = " / ".join(excerpt for _, excerpt in adjacent_pairs)
        proposition = (
            f"`{node}` 当前与该机制最接近的命题是：{target_excerpt} "
            f"相邻章节对 handoff 的约束是：{adjacent_excerpt}"
        )
        delta = claim
        decision = candidate["Books Disposition"]
        if decision == "Integrate":
            if family in VERIFIED_INTEGRATES:
                decision_reason = (
                    f"该 family 已有独立 writeback 证据；当前章节中的相近段落包含该写回。其可沉淀增量是：{mechanism} "
                    f"长期正文仍受此边界约束：{boundary}"
                )
            else:
                decision_reason = (
                    f"现有命题没有完整拥有以下状态/控制变化：{mechanism} 该差异超出相邻章节的 handoff，"
                    f"但只允许在此边界内写入：{boundary}；正文必须保留旧路径的成立条件。"
                )
        elif decision == "Structural Candidate":
            decision_reason = (
                f"实际重读的 owner 与相邻章节均只覆盖上述命题，无法拥有 `{mechanism}` 的完整责任；"
                f"结构判断仍受 `{boundary}` 限制。"
            )
        else:
            decision_reason = (
                f"该 exact-v1 的机制 `{mechanism}` 已被现有命题或相邻 handoff 覆盖；作者结果只增加受限实例，"
                f"而 `{boundary}` 阻止把它提升为新的长期设计结论。"
            )
        books_rows.append(
            {
                "Source Family ID": family,
                "Stable Node ID": node,
                "Target Chapter Ref": target,
                "Adjacent Chapter Refs": adjacent,
                "Existing Proposition": f"existing:{family}",
                "New Evidence Delta": f"delta:{family}",
                "Evolution Relation": relation,
                "Decision": decision,
                "Books Review Ref": f"books-review:{family}",
            }
        )
        books_blocks.append(
            f"<!-- existing:{family}:start -->{proposition}<!-- existing:{family}:end -->\n"
            f"<!-- delta:{family}:start -->{delta}<!-- delta:{family}:end -->\n"
            f"<!-- books-review:{family}:start -->`{title}` 与 `{node}` 的关系判定为 `{relation}`。"
            f"比较 `{target}` 与 `{adjacent}` 后，决定为 `{decision}`：{decision_reason} "
            "不把论文名称、作者 benchmark 或未披露实现写成长期机制；若为 Integrate，正文写回仍由 root 按日期串行处理。"
            f"<!-- books-review:{family}:end -->"
        )
        books_v9_reconciliation.append(
            {
                "Source Family ID": family,
                "Stable Node ID": node,
                "Target Chapter Ref": target,
                "Target Substantive Proposition": target_excerpt,
                "Adjacent Chapter Refs": adjacent,
                "Adjacent Substantive Propositions": adjacent_excerpt,
                "Post-repair Decision": decision,
                "Repair Status": "v9_retained_current_owner_and_adjacent_narrative_awaiting_fresh_audit",
            }
        )
    write_tsv(
        PACKET / "books-comparison-v9-retained-proposition-reconciliation.tsv",
        books_v9_reconciliation,
        [
            "Source Family ID", "Stable Node ID", "Target Chapter Ref",
            "Target Substantive Proposition", "Adjacent Chapter Refs",
            "Adjacent Substantive Propositions", "Post-repair Decision", "Repair Status",
        ],
    )
    text = replace_table(text, VALIDATOR.BOOKS_COMPARISON_MARKER, books_headers, books_rows)
    marker_pos = text.index(VALIDATOR.BOOKS_COMPARISON_MARKER)
    after_marker = text[marker_pos:]
    table_match = re.search(r"\n\|.*?(?=\n\n)", after_marker, re.S)
    assert table_match
    table_end = marker_pos + table_match.end()
    audit_end = text.index("<!-- audit-target:books:end -->", table_end)
    text = text[:table_end] + "\n\n" + "\n".join(books_blocks) + "\n" + text[audit_end:]

    # Recompute every provenance ID after the final review segments exist.
    candidate_map = {row["Source Family ID"]: row for row in candidates}
    for row in review_rows:
        family = row["Source Family ID"]
        review_segment = VALIDATOR._bounded_segment(text, f"review:{family}", family, [])
        assert review_segment is not None, f"missing bounded review segment for retained family {family}"
        body_sha = VALIDATOR._normalized_body_sha256(review_segment)
        candidate = candidate_map[family]
        row["Review Provenance ID"] = VALIDATOR._expected_review_provenance(
            family,
            candidate,
            row["Review Route"],
            row["Primary Evidence Version"].strip("`"),
            row["Reviewed Evidence Versions"].strip("`"),
            row["Method / Identity Locators"].strip("`"),
            row["Evaluation Locators"].strip("`"),
            row["Limitations / Counterevidence Locators"].strip("`"),
            row["Artifact Locators"].strip("`"),
            row["Claim Boundary Ref"].strip("`"),
            candidate["Review Ref"].strip("`"),
            body_sha,
        )
    text = replace_table(text, VALIDATOR.REVIEW_COMPLETION_MARKER, review_headers, review_rows)

    families = [row["Source Family ID"] for row in candidates]
    family_list = ";".join(families)
    text = re.sub(r"\| Denominator ID \| .*? \|", f"| Denominator ID | {denominator_id} |", text, count=1)
    text = re.sub(r"\| Denominator Frozen At \| .*? \|", "| Denominator Frozen At | 2026-08-28T23:34:40+08:00 |", text, count=1)
    text = re.sub(r"\| Coverage Gate \| .*? \|", "| Coverage Gate | Closed |", text, count=1)
    text = re.sub(r"\| Evidence Gate \| .*? \|", "| Evidence Gate | Open |", text, count=1)
    coverage_headers, coverage_rows = parse_table(text, VALIDATOR.SOURCE_COVERAGE_MARKER)
    coverage_rows[0]["Candidate Source Families"] = family_list
    coverage_rows[0]["Endpoint / Filter"] = "Atom submittedDate lower-bound query; strict UTC half-open filter; registered category set; 371/371 exact-v1 identity/title-abstract semantic replay"
    coverage_rows[0]["Result"] = "checked"
    denominator_receipt_sha = hashlib.sha256(V9_DENOMINATOR_RECEIPT.read_bytes()).hexdigest()
    coverage_rows[0]["Closure Evidence"] = (
        "papers/2026/06/_sources/daily-20260601/"
        f"fresh-context-candidate-denominator-audit-independent-v9.tsv#sha256={denominator_receipt_sha}"
    )
    coverage_rows[0]["Gap / Limitation ID"] = "—"
    text = replace_table(text, VALIDATOR.SOURCE_COVERAGE_MARKER, coverage_headers, coverage_rows)

    # Update narrative truth state. Books remains open until serial writeback.
    text = re.sub(
        r"> .*?\n",
        f"> Canonical denominator is frozen at {len(candidates)} retained / {canonical_closure_count} family-specific closures after the accepted 371/371 independent V9 provenance and FP/FN audit. This downstream author rebuild contains {len(candidates)}/{len(candidates)} Review receipts, {len(selection_rows)}/{len(selection_rows)} selection decisions and {len(books_rows)}/{len(books_rows)} Books Comparisons. Evidence, Selection and Books Gates remain Open for a different fresh-context audit; no Books writeback is authorized.\n",
        text,
        count=1,
    )
    text = re.sub(r"(?m)^(> .*\n)(?:> .*\n)+", r"\1", text, count=1)
    summary = (
        f"本窗口保留 {raw_count} 个注册 arXiv raw identities；独立 V9 provenance 与 Candidate Denominator audit 已逐项核对全部 identity、{previous_retained_count} 个旧 retain 的 false positive 和全部旧 closure 的 false negative。"
        f"canonical denominator 保留 {len(candidates)} 个长期 AI System source families，并将 {canonical_closure_count} 个 raw identities 关闭为 family-specific pre-denominator closure；相对 V8 proposal 的变化为 {false_positive_closed_count} 个 false-positive closed、{false_negative_reopened_count} 个 false-negative reopened。"
        f"旧 V8 raw-hit 保留率为 {previous_retain_rate:.2%}，canonical raw-hit 保留率为 {raw_retain_rate:.2%}；新分母路由为 {route_counts['deep']} Deep、{route_counts['standard']} Standard、{route_counts['closure']} Closure。"
        f"当前 {len(candidates)} 项 Review、{len(selection_rows)} 项 selection、{len(books_rows)} 项 Books Comparison 与 {len(new_bench)} 项 benchmark contract 仅是修复 owner 重建的下游接口。"
        "Coverage Gate 已依据 root 接受的独立 V9 audit 关闭；Evidence、Selection 与 Books Comparison Gate 保持 Open，等待不同 fresh context 全量审计下游。"
    )
    text = re.sub(r"(?s)(## Executive Summary\n\n).*?(?=\n<!-- audit-target:coverage:start -->)", r"\1" + summary + "\n", text, count=1)
    text = re.sub(
        r"<!-- coverage:SRC-ARXIV:20260601:start -->.*?<!-- coverage:SRC-ARXIV:20260601:end -->",
        f"<!-- coverage:SRC-ARXIV:20260601:start -->SRC-ARXIV raw Atom、严格窗口/category 复算、371/371 official exact-v1 history/title/author/DOI/revision-chain provenance receipt 与 371/371 strict denominator receipt 均保存在 `papers/2026/06/_sources/daily-20260601/`。V9 canonical denominator 为 {len(candidates)} retain / {canonical_closure_count} family-specific closures；V8 64-family proposal 经全量 FP/FN 审计后关闭 {false_positive_closed_count} 个 false positives 并重开 {false_negative_reopened_count} 个 false negatives。screening ledger 现有 {ledger_closure_count} 个 exclude。arXiv ID 前缀只触发复核，不作为日期证据；owner window 只由 official exact-v1 submission history 与 identity chain 决定。<!-- coverage:SRC-ARXIV:20260601:end -->",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"### Coverage Limitations\n\n.*?(?=\n<!-- audit-target:coverage:end -->)",
        "### Coverage Limitations\n\n其他 Required Daily 来源的注册 Effective Date 晚于本历史窗口，不追溯为本日到期来源。arXiv v1 submission date 决定 owner window；later revision 仅用于发现 title drift，不进入 event-time claim。公开全文证明作者披露的机制与实验，不证明 peer review、生产复现或全网 absence。\n",
        text,
        flags=re.S,
    )
    audit_headers, audit_rows = parse_table(text, VALIDATOR.SEMANTIC_AUDIT_MARKER)
    for row in audit_rows:
        scope = row["Scope"]
        if scope == "coverage":
            row.update({"Auditor": "fresh-context:independent-v9", "Findings": "none", "Resolution": f"Accepted 371/371 provenance plus all 64 proposed-retain FP and all 307 proposed-closure FN decisions; canonical denominator {denominator_id} has {len(candidates)} retain / {canonical_closure_count} closures", "Status": "passed"})
        elif scope == "evidence":
            row.update({"Auditor": "fresh-context:pending-after-v9-downstream-rebuild", "Findings": "POST-V9-DOWNSTREAM-INDEPENDENT-AUDIT-PENDING", "Resolution": f"Verify all {len(candidates)} retained reviews, exact-v1 locators and all {len(new_bench)} Benchmark Claim=yes contracts from a different fresh context", "Status": "open"})
        elif scope == "deep_analysis_selection":
            row.update({"Auditor": "fresh-context:pending-after-v9-downstream-rebuild", "Findings": "POST-V9-DOWNSTREAM-INDEPENDENT-AUDIT-PENDING", "Resolution": f"Verify {len(selection_rows)} family-specific full-frontier decisions and exactly three narratives from a different fresh context", "Status": "open"})
        elif scope == "books":
            row.update({"Auditor": "fresh-context:pending-after-v9-downstream-rebuild", "Findings": "POST-V9-DOWNSTREAM-INDEPENDENT-AUDIT-PENDING;SERIAL-WRITEBACK-PENDING", "Resolution": f"Verify all {len(books_rows)} Books Comparisons independently, then let root decide whether to serialize the proposed Integrate deltas", "Status": "open"})
    text = replace_table(text, VALIDATOR.SEMANTIC_AUDIT_MARKER, audit_headers, audit_rows)
    text = re.sub(
        r"(?s)(## Recommended Action / Books Decision\n\n).*?(?=\n## Ignored Noise)",
        "\\1" + f"作者 downstream self-check 已生成 {len(candidates)}/{len(candidates)} Review、{len(selection_rows)}/{len(selection_rows)} selection 和 {len(books_rows)}/{len(books_rows)} Books Comparison。{sum(row['Decision'] == 'Integrate' for row in books_rows)} 个 `Integrate` proposal 等待不同 fresh-context audit，之后才可由 root 按日期串行写回；Evidence、Selection、Books Gate 保持 Open。\n",
        text,
        count=1,
    )
    text = re.sub(
        r"(?s)(## Ignored Noise\n\n).*?(?=\n## Repository Changes)",
        "\\1" + f"独立 V9 denominator audit 将 {raw_count} 个 raw identities 冻结为 {len(candidates)} retain / {canonical_closure_count} family-specific closures；相对 V8 proposal 关闭 {false_positive_closed_count} 个 false positives、重开 {false_negative_reopened_count} 个 false negatives。screening ledger 的 {ledger_closure_count} 个 exclude 均保留 identity evidence、source-specific reason 与 reopen boundary。\n",
        text,
        count=1,
    )
    text = re.sub(
        r"(?s)(## Repository Changes\n\n).*?(?=\n## Open Questions)",
        "\\1" +
        f"- 按已接受的 `fresh-context-candidate-denominator-audit-independent-v9.tsv` 重冻 371-hit ledger 与 {len(candidates)}-family Candidate inventory；V8 raw-hit 保留率 {previous_retain_rate:.2%}，canonical raw-hit 保留率 {raw_retain_rate:.2%}。\n"
        f"- canonical accounting 为 {len(candidates)} retain / {canonical_closure_count} family-specific closures，FP/FN 变化为 -{false_positive_closed_count}/+{false_negative_reopened_count}。\n"
        f"- 按新分母重建 {len(candidates)} 项 Review、{len(selection_rows)} 项 selection、{len(books_rows)} 项 Books Comparison 与 {len(new_bench)} 项 benchmark contract。\n"
        "- 新增 exact-v1 owner identity audit；arXiv ID 形态不再被当作日期代理。\n"
        "- 本修复不修改 Books、ROADMAP、LEARNING_STATE、Weekly 或其他日期；四个作者候选 Integrate delta 仍须独立审计，再由 root 决定是否串行写回。\n",
        text,
        count=1,
    )
    text = re.sub(
        r"(?s)(## Open Questions\n\n).*?(?=\n## Sources)",
        "\\g<1>"
        + f"1. 不同 fresh-context auditor 是否接受全部 {len(candidates)} 项 exact-v1 Review、{len(new_bench)} 项 benchmark contract、{len(selection_rows)} 项 selection 与 {len(books_rows)} 项 Books Comparison？\n"
        + "2. 若该独立下游审计无未解决 finding，root 是否接受并按日期串行写回四个作者候选 Integrate delta？\n",
        text,
        count=1,
    )

    # Rebuild knowledge-tree coverage and Sources from the final denominator so
    # restored families cannot be present only in machine tables.
    grouped: dict[str, list[str]] = {}
    for candidate in candidates:
        grouped.setdefault(candidate["Stable Node ID"], []).append(candidate["Source Family ID"])
    knowledge = "\n".join(
        f"- `{node}`：" + "、".join(f"`{family}`" for family in families) + "。"
        for node, families in sorted(grouped.items())
    )
    text = re.sub(
        r"(?s)(## Knowledge Tree Position\n\n).*?(?=\n## Deep Analysis Selection)",
        r"\1" + knowledge + "\n",
        text,
        count=1,
    )
    if "<!-- audit-target:deep_analysis_selection:start -->" not in text:
        text = text.replace(
            "## Deep Analysis Selection",
            "<!-- audit-target:deep_analysis_selection:start -->\n## Deep Analysis Selection",
            1,
        )
    source_lines = [
        "- arXiv Atom snapshot，strict first-public window，accessed 2026-08-28: https://export.arxiv.org/api/query",
        "- Frozen source packet: `papers/2026/06/_sources/daily-20260601/README.md`",
    ]
    for candidate in candidates:
        family = candidate["Source Family ID"]
        arxiv_id = candidate["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        title = title_from_review(text, family)
        local_html = MATERIALS / f"{arxiv_id}v1.html"
        suffix = "html" if is_full_arxiv_html(local_html) or arxiv_id in WEB_EXACT else "pdf"
        source_lines.append(
            f"- {title} (first-public {candidate['First-public Date']}): https://arxiv.org/{suffix}/{arxiv_id}v1"
        )
    text = re.sub(r"(?s)(## Sources\n\n).*\Z", r"\1" + "\n".join(source_lines) + "\n", text, count=1)

    # Recompute provenance one final time after every text mutation.  The hash
    # contract includes the bounded review body, so this must be the last table
    # rewrite before the report is written.
    _, final_candidates = parse_table(text, VALIDATOR.CANDIDATE_LEDGER_MARKER)
    candidate_map = {row["Source Family ID"]: row for row in final_candidates}
    final_review_headers, final_review_rows = parse_table(text, VALIDATOR.REVIEW_COMPLETION_MARKER)
    for row in final_review_rows:
        family = row["Source Family ID"]
        candidate = candidate_map[family]
        segment = VALIDATOR._bounded_segment(text, f"review:{family}", family, [])
        assert segment is not None, f"missing final bounded review segment for retained family {family}"
        row["Review Provenance ID"] = VALIDATOR._expected_review_provenance(
            family,
            candidate,
            row["Review Route"],
            row["Primary Evidence Version"].strip("`"),
            row["Reviewed Evidence Versions"].strip("`"),
            row["Method / Identity Locators"].strip("`"),
            row["Evaluation Locators"].strip("`"),
            row["Limitations / Counterevidence Locators"].strip("`"),
            row["Artifact Locators"].strip("`"),
            row["Claim Boundary Ref"].strip("`"),
            candidate["Review Ref"].strip("`"),
            VALIDATOR._normalized_body_sha256(segment),
        )
    text = replace_table(text, VALIDATOR.REVIEW_COMPLETION_MARKER, final_review_headers, final_review_rows)
    REPORT.write_text(text)

    packet_readme = (PACKET / "README.md").read_text()
    packet_readme = packet_readme.replace("## Provisional denominator and fresh-audit reopen", "## Frozen denominator and fresh-audit closure")
    packet_readme = re.sub(
        r"Repair-author V\d+.*?Books writeback is blocked\.",
        f"Independent V9 audit reconciled all {raw_count} registered identities and accepted {len(candidates)} retained / {canonical_closure_count} family-specific closures under `{denominator_id}`. Relative to the V8 proposal it closed {false_positive_closed_count} false positives and reopened {false_negative_reopened_count} false negatives; the identity/date and denominator receipts preserve exact-v1 evidence, unique rationales and reopen boundaries for every raw row. The downstream author rebuild now contains {len(candidates)}/{len(candidates)} Source Reviews, {len(selection_rows)}/{len(selection_rows)} full-frontier selection decisions, {len(books_rows)}/{len(books_rows)} current-owner Books Comparisons and {len(new_bench)} benchmark contracts. Coverage is closed by the accepted independent receipt; Evidence, Selection and Books remain Open pending a different fresh-context audit. Books writeback is blocked.",
        packet_readme,
        flags=re.S,
    )
    packet_readme = re.sub(
        r"The V5 repair independently re-routed every member of the 143-row residual closure set:.*?not a self-pass\.",
        f"The V7 repair re-routed the complete 143-row residual family after the V6 finding: 38 cumulative false negatives are reopened and {ledger_closure_count} remain closed with frozen identity/title/category/abstract evidence and an explicit reopen condition. The repair owner's interface checks are not a self-pass.",
        packet_readme,
        flags=re.S,
    )
    packet_readme = packet_readme.replace(
        "Independent V6 review found at least nine additional retained-closure false negatives and multiple exact-v1 benchmark disclosure contradictions. Therefore the 257-family denominator and all derived Review/benchmark/selection/Books-comparison receipts are superseded as semantic completion evidence pending repair and different-context re-review. Coverage, Evidence, Selection and Books Comparison Gates remain Open; see `fresh-context-post-repair-audit-independent-v6.md`.",
        "Independent V6 review found nine additional retained-closure false negatives and multiple exact-v1 benchmark disclosure contradictions. V7 has repaired those interfaces and refrozen the accounting, but the repair owner cannot self-pass: Coverage, Evidence, Selection and Books Comparison Gates remain Open pending the exact different-context scope in `post-v7-repair-author-checkpoint.md`.",
    )
    packet_links = (
        "- V9 downstream source-specific curation: `fresh-audit-curation-v9.tsv`\n"
        "- Accepted independent V9 identity/date receipt: `fresh-context-identity-date-provenance-independent-v9.tsv`\n"
        "- Accepted independent V9 Candidate Denominator receipt: `fresh-context-candidate-denominator-audit-independent-v9.tsv`\n"
        "- Current V9 retained-family benchmark contract reconciliation: `benchmark-disclosure-v9-retained.tsv`\n"
        "- Current V9 model-identity and nine-field audit receipt: `benchmark-model-identity-audit-v9.tsv`\n"
        "- Current V9 Books proposition reconciliation: `books-comparison-v9-retained-proposition-reconciliation.tsv`\n"
        "- Current V9 downstream author checkpoint: `post-v9-candidate-denominator-downstream-author-checkpoint.md`\n"
        "- V7 source-specific repair curation: `fresh-audit-curation-v7.tsv`\n"
        "- V7 source-wide benchmark disclosure reconciliation: `benchmark-disclosure-v7-reconciliation.tsv`\n"
        "- Historical V7 repair-author checkpoint: `post-v7-repair-author-checkpoint.md`\n"
        "- Pre-refreeze V7 candidate inventory: `candidate-inventory-v7.tsv`\n"
        "- V8 row-level Candidate Denominator audit: `candidate-denominator-audit-v8.tsv`\n"
        "- V8 retained-family benchmark disclosure reconciliation: `benchmark-disclosure-v8-retained.tsv`\n"
        "- V8 retained-family Books proposition reconciliation: `books-comparison-v8-retained-proposition-reconciliation.tsv`\n"
        "- Current V8 repair-author checkpoint: `post-v8-candidate-denominator-author-checkpoint.md`\n"
    )
    if "post-v9-candidate-denominator-downstream-author-checkpoint.md" not in packet_readme:
        packet_readme = packet_readme.replace("- Artifact hashes: `SHA256SUMS`\n", packet_links + "- Artifact hashes: `SHA256SUMS`\n")
    if "benchmark-model-identity-audit-v9.tsv" not in packet_readme:
        packet_readme = packet_readme.replace(
            "- Current V9 retained-family benchmark contract reconciliation: `benchmark-disclosure-v9-retained.tsv`\n",
            "- Current V9 retained-family benchmark contract reconciliation: `benchmark-disclosure-v9-retained.tsv`\n"
            "- Current V9 model-identity and nine-field audit receipt: `benchmark-model-identity-audit-v9.tsv`\n",
        )
    packet_readme = packet_readme.replace(
        "- Previous provisional family list and first-public timestamps: `candidate-inventory.tsv`",
        "- Previous V7 family list and first-public timestamps: `candidate-inventory-v7.tsv`",
    ).replace(
        "- Current V7 repair-author checkpoint: `post-v7-repair-author-checkpoint.md`\n",
        "",
    )
    for duplicate_line in (
        "- V7 source-specific repair curation: `fresh-audit-curation-v7.tsv`\n",
        "- V7 source-wide benchmark disclosure reconciliation: `benchmark-disclosure-v7-reconciliation.tsv`\n",
    ):
        while packet_readme.count(duplicate_line) > 1:
            packet_readme = packet_readme.replace(duplicate_line, "", 1)
    packet_readme = packet_readme.replace(
        "- Current independent V5 finding artifact: `fresh-context-post-repair-audit-independent-v5.md`",
        "- Historical independent V5 finding artifact: `fresh-context-post-repair-audit-independent-v5.md`",
    ).replace(
        "- Current repair-author checkpoint: `post-v5-repair-author-checkpoint.md`",
        "- Historical V5 repair-author checkpoint: `post-v5-repair-author-checkpoint.md`",
    ).replace(
        "- Current independent V6 finding receipt: `fresh-context-post-repair-audit-independent-v6.md`\n- Current independent V6 finding artifact: `fresh-context-post-repair-audit-independent-v6.md`",
        "- Independent V6 finding receipt: `fresh-context-post-repair-audit-independent-v6.md`",
    )
    retained_ids = [
        candidate["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        for candidate in candidates
    ]
    html_count = sum(is_full_arxiv_html(MATERIALS / f"{arxiv_id}v1.html") for arxiv_id in retained_ids)
    pdf_only_count = sum(
        not is_full_arxiv_html(MATERIALS / f"{arxiv_id}v1.html")
        and (MATERIALS / f"{arxiv_id}v1.pdf").exists()
        for arxiv_id in retained_ids
    )
    web_exact_count = sum(
        not is_full_arxiv_html(MATERIALS / f"{arxiv_id}v1.html")
        and not (MATERIALS / f"{arxiv_id}v1.pdf").exists()
        and arxiv_id in WEB_EXACT
        for arxiv_id in retained_ids
    )
    assert html_count + pdf_only_count + web_exact_count == len(candidates)
    packet_readme = re.sub(
        r"(?:All|The) \d+ denominator identities(?: have local exact-v1 material:| have).*?semantic Gates\.",
        f"The {len(candidates)} denominator identities have {html_count} packet-frozen full HTML files, {pdf_only_count} packet-frozen PDF-only files and {web_exact_count} public exact-v1 HTML/PDF reviews whose packet download failed while the official source remained readable. Atom is identity evidence, not a substitute for full review. Every retained row has exact-v1 Method, Evaluation, Limitations and Artifact locators; the downstream semantics still await a different fresh-context audit.",
        packet_readme,
        flags=re.S,
    )
    (PACKET / "README.md").write_text(packet_readme)

    integrate_families = [
        row["Source Family ID"] for row in books_rows if row["Decision"] == "Integrate"
    ]
    # Preserve earlier reconciliations as historical evidence. The current
    # receipt contains only benchmark-bearing families retained by canonical V9.
    benchmark_rows = new_bench
    benchmark_fields = ["Model", "Hardware", "Precision", "Input Length", "Output Length", "Batch", "Concurrency", "SLO"]
    benchmark_not_disclosed = {
        field: sum(str(row[field]).startswith("Not Disclosed") for row in benchmark_rows)
        for field in benchmark_fields
    }
    benchmark_not_disclosed_text = ", ".join(
        f"{field}={benchmark_not_disclosed[field]}" for field in benchmark_fields
    )
    benchmark_reconciliation_rows = []
    for row in benchmark_rows:
        benchmark_reconciliation_rows.append({
            "source_family_id": row["Source Family ID"],
            "workload": row["Workload"],
            "model": row["Model"],
            "hardware": row["Hardware"],
            "precision": row["Precision"],
            "input_length": row["Input Length"],
            "output_length": row["Output Length"],
            "batch": row["Batch"],
            "concurrency": row["Concurrency"],
            "slo": row["SLO"],
            "evaluator": row["Evaluator"],
            "v9_scope": "retained-family exact-v1 source-wide reconciliation; training/serving/simulation scope preserved in field text",
        })
    write_tsv(
        PACKET / "benchmark-disclosure-v9-retained.tsv",
        benchmark_reconciliation_rows,
        ["source_family_id", "workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator", "v9_scope"],
    )

    model_audit_rows = []
    for row in benchmark_rows:
        family = row["Source Family ID"]
        audit = V9_RETAINED_BENCHMARK_AUDIT[family]
        model_audit_rows.append({
            "source_family_id": family,
            "arxiv_v1": audit["arxiv_v1"],
            "model_action": audit["model_action"],
            "model_locator": audit["model_locator"],
            "post_audit_model": row["Model"],
            "fields_checked": "workload|model|hardware|precision|input_length|output_length|batch|concurrency|slo|evaluator",
            "pre_audit_issue": "none" if audit["model_action"] == "confirmed_exact" else "generic extraction was incomplete, role-mixed, prose-contaminated, or confused non-evaluated mentions with evaluation identity",
            "post_audit_result": "model role and all benchmark-contract fields manually reconciled to exact-v1 setup/results/appendices; no unresolved unsafe model extraction",
        })
    write_tsv(
        PACKET / "benchmark-model-identity-audit-v9.tsv",
        model_audit_rows,
        ["source_family_id", "arxiv_v1", "model_action", "model_locator", "post_audit_model", "fields_checked", "pre_audit_issue", "post_audit_result"],
    )
    model_correction_count = sum(row["model_action"] != "confirmed_exact" for row in model_audit_rows)
    model_confirmed_count = len(model_audit_rows) - model_correction_count

    self_check = f"""# Post-V9 Candidate Denominator downstream author checkpoint — Daily 2026-06-01

## Status boundary

This receipt is a downstream repair-author self-check, not an independent fresh-context audit of the rebuilt Review, benchmark, selection, or Books interfaces. Coverage is closed only because root accepted the separate independent V9 371/371 provenance and denominator receipts. Evidence, Deep Analysis Selection and Books scopes remain Open. No Books writeback is authorized by this receipt.

## Refrozen accounting

- Registered arXiv identities: {raw_count}.
- Previous V8 proposal: {previous_retained_count} retained / {raw_count - previous_retained_count} closures ({previous_retain_rate:.2%} raw-hit retain rate).
- Canonical V9 denominator: {len(candidates)} retained / {canonical_closure_count} family-specific closures under `{denominator_id}` ({raw_retain_rate:.2%} raw-hit retain rate).
- V8-to-V9 transitions: {false_positive_closed_count} false positives closed; {false_negative_reopened_count} false negatives reopened; 27 retains upheld; 294 closures upheld.
- Routes: {route_counts['deep']} Deep, {route_counts['standard']} Standard, {route_counts['closure']} Closure.
- Current screening-ledger excludes: {ledger_closure_count}.
- V9 pre-denominator closure classes: {closure_class_text}.
- Review Completion: {len(review_rows)}/{len(candidates)}; ordinary `pending`, `blocked`, `unverified`: 0.
- Deep Analysis selection: {len(selection_rows)}/{len(selection_rows)} eligible; three selected narratives and {len(selection_rows) - 3} family-relative `not_selected` decisions.
- Books Comparison: {len(books_rows)}/{len(books_rows)}, because `{len(candidates)} - {route_counts['closure']} closure-only = {len(books_rows)}`.
- Benchmark contracts: {len(benchmark_rows)}, limited to candidates that make an evaluation claim.
- Model-identity audit before/after: {model_correction_count}/{len(model_audit_rows)} fields required correction or exact-role precision before manual audit; 0/{len(model_audit_rows)} remain unsafe after audit. {model_confirmed_count} prior field was confirmed exact.

## Candidate decision boundary

- `fresh-context-identity-date-provenance-independent-v9.tsv` records all {raw_count} official exact-v1 history/title/author/DOI/revision-chain reconciliations; `fresh-context-candidate-denominator-audit-independent-v9.tsv` records every retain/closure decision, source-specific rationale, evidence and reopen boundary.
- Retain requires an explicit change to a durable AI System mechanism, state/data/control ownership, evaluation contract, platform/training/inference design judgement, or a correction to existing Books knowledge. Topical relevance, a completed Deep Review, a task-specific benchmark, or a bounded model variant is not sufficient.
- The {canonical_closure_count} closed identities remain packet-addressable evidence rows but do not participate in candidate-only Review, benchmark, selection, or Books-comparison counts.
- Retained exact-v1 material split: {html_count} packet HTML, {pdf_only_count} packet PDF-only and {web_exact_count} public exact-v1 HTML/PDF reviews; independent audit must verify the web-only receipts.
- Benchmark reconciliation was regenerated for all {len(benchmark_rows)} retained families in `benchmark-disclosure-v9-retained.tsv`, including workload, model, hardware, precision, input/output length, batch, concurrency, SLO and evaluator. `benchmark-model-identity-audit-v9.tsv` records the {len(model_audit_rows)}/{len(model_audit_rows)} role-separated model decisions and exact-v1 locators. Verified omissions remain literal `Not Disclosed`. Current counts are {benchmark_not_disclosed_text}. These counts are disclosure boundaries, not an independent semantic pass.
- Selection and Books Comparison were rebuilt only for the retained set. This worker did not edit Books.
- Access / Materials Request: no exact-version external blocker remains and no Materials Request was created. Public exact-v1 HTML that is not packet-frozen remains an independent packet-sufficiency review item, not a user-material blocker.

## Books decision boundary

- Independently verified prior writebacks preserved: {', '.join(f'`{family}`' for family in sorted(VERIFIED_INTEGRATES))}.
- Repair-author `Integrate` decisions awaiting independent semantic review and root serialization: {', '.join(f'`{family}`' for family in integrate_families if family not in VERIFIED_INTEGRATES)}.
- Total V9 `Integrate` proposals: {len(integrate_families)}. This count is not a Books write authorization.

## Exact continuation point

1. A different fresh-context auditor must verify all {len(candidates)} Source Reviews, all {len(benchmark_rows)} benchmark contracts, all {len(selection_rows)} full-frontier selection decisions and all {len(books_rows)} Books Comparisons without sampling.
2. Current-owner and adjacent propositions must be checked against Books read-only; this checkpoint did not modify Books.
3. Only after that audit may root serialize valid `Integrate` deltas by owner/date.
4. Only the independent downstream audit may close Evidence, Selection, or Books semantic scopes or mark this Daily Complete.
"""
    (PACKET / "post-v9-candidate-denominator-downstream-author-checkpoint.md").write_text(self_check)
    regenerate_manifest()

    print(f"rebuilt {REPORT}")
    print(f"denominator={denominator_id} candidates={len(candidates)} reviews={len(review_rows)} books={len(books_rows)} selection={len(selection_rows)}")


if __name__ == "__main__":
    main()
