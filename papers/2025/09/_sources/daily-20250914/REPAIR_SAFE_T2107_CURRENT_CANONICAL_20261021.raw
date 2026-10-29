# SAF-T2107: AI Model Poisoning via MCP Tool Training Data Contamination

## Overview

- **Tactic**: ATK-TA0042
- **Technique ID**: SAF-T2107
- **Research Packet**: [research/techniques/SAF-T2107](../../research/techniques/SAF-T2107/)
- **Traceability Ledger**: [traceability-ledger.yml](../../research/techniques/SAF-T2107/traceability-ledger.yml)
- **Documentation Status**: Under Review
- **Evidence Status**: Research-Derived
- **Severity**: High
- **Severity Rationale**: An admitted poison can influence a derived model and every deployment of that model, but the adversary must first get MCP-derived records into a training run. <!-- SAF-TRACE: claims=SAF-T2107-C015,SAF-T2107-C006; sources=SRC-wan23b,SRC-anthropic-small-samples -->
- **First Observed**: No direct production incident identified as of 2026-09-02. <!-- SAF-TRACE: claims=SAF-T2107-C010,SAF-T2107-C011; sources=SRC-microsoft-tool-poisoning-2026-06-30,SRC-nvd-cve-2025-61591 -->
- **Last Updated**: 2026-09-02

## Scope

This technique covers adversary-controlled MCP tool results that cross from live tool execution into a corpus used to update model weights, causing the derived model to learn attacker-influenced behavior. <!-- SAF-TRACE: claims=SAF-T2107-C005; sources=SRC-mcp-tools-2025-06-18,SRC-toucan,SRC-wan23b -->

### In Scope

- The adversary controls or compromises an MCP tool result source, and the result is retained as a training example or trajectory. <!-- SAF-TRACE: claims=SAF-T2107-C005,SAF-T2107-C006; sources=SRC-mcp-tools-2025-06-18,SRC-toucan,SRC-wan23b -->
- A pretraining, fine-tuning, continual-learning, or similar weight-update job consumes the contaminated MCP-derived record. <!-- SAF-TRACE: claims=SAF-T2107-C002,SAF-T2107-C006; sources=SRC-toucan,SRC-wan23b -->

### Out of Scope

- A malicious tool result that changes only the current inference session is runtime tool-output prompt injection, not this technique. <!-- SAF-TRACE: claims=SAF-T2107-C001,SAF-T2107-C010; sources=SRC-microsoft-tool-poisoning-2026-06-30,SRC-mcp-tools-2025-06-18 -->
- Poisoning a retrieval index without a model-weight update, or replacing a model artifact directly, crosses different boundaries. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C007; sources=SRC-wan23b,SRC-nist-ai-600-1 -->

### Distinguishing Characteristics

The distinguishing observable is lineage from an MCP tool result into an admitted training sample and then a model-training job. A live response alone, a changed retrieval result, or a tampered checkpoint does not meet the contract. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C009; sources=SRC-toucan,SRC-nist-ai-600-1,SRC-owasp-llm04 -->

## Description

MCP servers expose tools for model invocation, and tool calls can return text, media, embedded resources, or structured content. <!-- SAF-TRACE: claims=SAF-T2107-C001; sources=SRC-mcp-tools-2025-06-18 -->

Published MCP training research has collected real server interactions as trajectories containing planning, calls, tool responses, and final answers, then used those trajectories for fine-tuning. Separately, instruction-tuning and pretraining studies show that attacker-influenced training records can induce trigger-conditioned or otherwise degraded behavior. <!-- SAF-TRACE: claims=SAF-T2107-C002,SAF-T2107-C003,SAF-T2107-C004; sources=SRC-toucan,SRC-wan23b,SRC-anthropic-small-samples -->

The complete MCP-specific technique is therefore an inference across independently supported components. The reviewed record contains neither a direct end-to-end MCP tool-result poisoning experiment nor a qualifying production incident. <!-- SAF-TRACE: claims=SAF-T2107-C005,SAF-T2107-C010; sources=SRC-toucan,SRC-wan23b,SRC-microsoft-tool-poisoning-2026-06-30 -->

## Attack Vectors

- **Primary Vector**: A controlled or compromised MCP server returns crafted content during a data-collection run, and that response is admitted to a training corpus. <!-- SAF-TRACE: claims=SAF-T2107-C005; sources=SRC-mcp-tools-2025-06-18,SRC-toucan,SRC-wan23b -->
- **Secondary Vectors**: <!-- SAF-TRACE: claims=SAF-T2107-C006; sources=SRC-toucan,SRC-wan23b -->
  - A downstream pipeline imports previously captured MCP trajectories from an untrusted contributor. <!-- SAF-TRACE: claims=SAF-T2107-C002,SAF-T2107-C006; sources=SRC-toucan,SRC-wan23b -->
  - A legitimate tool source is altered after approval while provenance checks remain stale or absent. <!-- SAF-TRACE: claims=SAF-T2107-C007; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- **Affected Components**: MCP server, tool, host-side collection pipeline, dataset registry, training job, and derived model. <!-- SAF-TRACE: claims=SAF-T2107-C001,SAF-T2107-C002; sources=SRC-mcp-tools-2025-06-18,SRC-toucan -->
- **Trust Boundary Crossed**: Runtime tool output becomes trusted model-development input. <!-- SAF-TRACE: claims=SAF-T2107-C005; sources=SRC-toucan,SRC-wan23b -->

## Technical Details

### Prerequisites

- The adversary can influence an MCP tool result that a collector records. <!-- SAF-TRACE: claims=SAF-T2107-C001,SAF-T2107-C006; sources=SRC-mcp-tools-2025-06-18,SRC-toucan -->
- The organization admits that record to a weight-update corpus without sufficient origin, integrity, or transformation evidence. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C007; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- The poisoned material has enough effective representation in training to influence learned behavior; a single record is not assumed sufficient. <!-- SAF-TRACE: claims=SAF-T2107-C003,SAF-T2107-C004; sources=SRC-wan23b,SRC-anthropic-small-samples -->

### Attack Flow

1. **Setup**: The adversary prepares a server, tool, or upstream dependency whose response can reach an MCP trajectory collector. <!-- SAF-TRACE: claims=SAF-T2107-C001,SAF-T2107-C005; sources=SRC-mcp-tools-2025-06-18,SRC-toucan -->
2. **Delivery**: The collector invokes the tool and records the returned content with the interaction. <!-- SAF-TRACE: claims=SAF-T2107-C002; sources=SRC-toucan -->
3. **Admission**: A data pipeline accepts the record despite missing, invalid, or mismatched provenance. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
4. **Training**: A weight-update job consumes the contaminated sample or trajectory. <!-- SAF-TRACE: claims=SAF-T2107-C003,SAF-T2107-C006; sources=SRC-wan23b,SRC-toucan -->
5. **Objective**: The resulting model learns attacker-influenced behavior that may remain conditional on a trigger. <!-- SAF-TRACE: claims=SAF-T2107-C003,SAF-T2107-C004; sources=SRC-wan23b,SRC-anthropic-small-samples -->
6. **Follow-On Activity**: The affected model is evaluated, registered, or deployed, propagating the integrity failure to its consumers. <!-- SAF-TRACE: claims=SAF-T2107-C015; sources=SRC-wan23b,SRC-anthropic-small-samples -->

### Example Scenario

An internal team records MCP tool trajectories to adapt a support model. A test server at an inert domain emits a record whose digest does not match the approved source manifest; the pipeline still admits it and the next model version consumes it. This is an illustrative, research-derived scenario rather than a reproduced exploit. <!-- SAF-TRACE: claims=SAF-T2107-C005,SAF-T2107-C009; sources=SRC-toucan,SRC-nist-ai-600-1,SRC-wan23b -->

The inert event below shows the admission observable without supplying poison content. <!-- SAF-TRACE: claims=SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->

```json
{
  "event.action": "training_sample_ingested",
  "sample.origin": "mcp_tool_result",
  "provenance.status": "digest_mismatch",
  "sample.disposition": "admitted",
  "source.server_id": "server.example.invalid",
  "source.tool_name": "catalog_lookup",
  "dataset.version_id": "dataset-demo-17",
  "training.job_id": "job-demo-42"
}
```

## Evidence and Current State

### Evidence Summary

| Claim ID | Claim | Evidence Status | Source ID and Source | Limitations |
| --- | --- | --- | --- | --- |
| SAF-T2107-C001 | MCP tools return model-visible content in several content forms. | Demonstrated | SRC-mcp-tools-2025-06-18: MCP Tools specification | The protocol capability does not establish training use. |
| SAF-T2107-C002 | A published corpus used real MCP tool responses in trajectories for fine-tuning. | Demonstrated | SRC-toucan: TOUCAN | It does not study adversarial contamination. |
| SAF-T2107-C003 | Instruction-tuning poisons can induce conditional model behavior. | Demonstrated | SRC-wan23b: Wan et al. | The inputs were not MCP tool results. |
| SAF-T2107-C004 | A controlled pretraining study found a narrow backdoor from 250 poisoned documents. | Demonstrated | SRC-anthropic-small-samples: Souly et al. | Scaling and complex behaviors remain uncertain. |
| SAF-T2107-C005 | Combining the MCP trajectory and poisoning evidence supports this technique. | Research-Derived | SRC-toucan; SRC-wan23b; SRC-mcp-tools-2025-06-18 | No direct end-to-end experiment was identified. |
| SAF-T2107-C006 | Control of content, corpus admission, and training consumption are necessary conditions. | Research-Derived | SRC-toucan; SRC-wan23b | The effective poison dose is environment-dependent. |
| SAF-T2107-C007 | Provenance and transformation records support training-data integrity review. | Research-Derived | SRC-nist-ai-600-1; SRC-owasp-llm04 | Provenance does not establish semantic safety. |
| SAF-T2107-C008 | Filtering, versioning, testing, and rollback reduce exposure but have tradeoffs. | Research-Derived | SRC-wan23b; SRC-owasp-llm04 | No single control guarantees removal. |
| SAF-T2107-C009 | Failed provenance at MCP-sample admission is a detectable risk event. | Research-Derived | SRC-nist-ai-600-1; SRC-owasp-llm04 | It detects unsafe admission, not learned misbehavior. |
| SAF-T2107-C010 | Disclosed MCP tool poisoning is adjacent runtime behavior. | Observed | SRC-microsoft-tool-poisoning-2026-06-30 | The report does not describe model-weight updates. |
| SAF-T2107-C011 | Two disclosed MCP CVEs concern runtime command injection. | Observed | SRC-nvd-cve-2025-61591; SRC-nvd-cve-2025-52573 | Neither record establishes training contamination. |
| SAF-T2107-C012 | ATT&CK stored-data manipulation is an analogy, not a direct mapping. | Research-Derived | SRC-mitre-t1565.001 | ATT&CK does not specify MCP training flows. |
| SAF-T2107-C013 | ATLAS poison-training-data is the closest direct AI-security mapping. | Research-Derived | SRC-mitre-atlas-safeai | The reviewed report predates this MCP-specific composition. |
| SAF-T2107-C014 | Semantic poisoning can evade lineage-only detection. | Research-Derived | SRC-wan23b; SRC-anthropic-small-samples | Evasion depends on data and training design. |
| SAF-T2107-C015 | Successful contamination primarily threatens model integrity and can affect many deployments. | Research-Derived | SRC-wan23b; SRC-anthropic-small-samples | Blast radius depends on promotion and deployment. |

### Current State

- **Affected Environments**: Pipelines that retain MCP interactions and use them for model weight updates. <!-- SAF-TRACE: claims=SAF-T2107-C002,SAF-T2107-C006; sources=SRC-toucan,SRC-wan23b -->
- **Known Exploitation**: No qualifying direct example is recorded in the completed [source coverage assessment](../../research/techniques/SAF-T2107/source-coverage.yml).
- **Available Protections**: Source vetting, provenance tracking, anomaly filtering, dataset versioning, model evaluation, and rollback. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C008; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- **Residual Risk**: Valid-looking lineage cannot by itself reveal semantically malicious content, and filtering may reduce utility. <!-- SAF-TRACE: claims=SAF-T2107-C008,SAF-T2107-C014; sources=SRC-wan23b,SRC-anthropic-small-samples -->

### Known Breaches and Vulnerabilities

No reviewed candidate qualified as a direct incident, vulnerability, or demonstration; the table preserves the nearest adjacent evidence and its boundary. <!-- SAF-TRACE: claims=SAF-T2107-C010,SAF-T2107-C011; sources=SRC-microsoft-tool-poisoning-2026-06-30,SRC-nvd-cve-2025-61591,SRC-nvd-cve-2025-52573 -->

| Event or Identifier | Date and Environment | Impact and Remediation | Relationship to This Technique | Evidence Limitation |
| --- | --- | --- | --- | --- |
| Microsoft MCP tool-poisoning observations | 2026-06-30; enterprise agent ecosystems | Runtime manipulation through tool metadata; inspect metadata and correlate behavior | Adjacent incident or vulnerability | No model-training path is described. <!-- SAF-TRACE: claims=SAF-T2107-C010; sources=SRC-microsoft-tool-poisoning-2026-06-30 --> |
| CVE-2025-61591 | 2025; Cursor through 1.7 | MCP command injection with a fixed build identified by NVD | Adjacent incident or vulnerability | NVD records no training contamination. <!-- SAF-TRACE: claims=SAF-T2107-C011; sources=SRC-nvd-cve-2025-61591 --> |
| CVE-2025-52573 | 2025; ios-simulator-mcp before 1.3.3 | Command injection; fixed in 1.3.3 | Adjacent incident or vulnerability | NVD records no training contamination. <!-- SAF-TRACE: claims=SAF-T2107-C011; sources=SRC-nvd-cve-2025-52573 --> |

## Impact Assessment

| Dimension | Rating | Rationale and Conditions |
| --- | --- | --- |
| Confidentiality | Low | Exposure is conditional on later learned behavior and is not established by the current evidence. <!-- SAF-TRACE: claims=SAF-T2107-C015; sources=SRC-wan23b,SRC-anthropic-small-samples --> |
| Integrity | High | An effective poison changes model behavior after a training run consumes the record. <!-- SAF-TRACE: claims=SAF-T2107-C003,SAF-T2107-C015; sources=SRC-wan23b,SRC-anthropic-small-samples --> |
| Availability | Medium | Degenerate or broadly degraded outputs are possible, but the demonstrated effects and doses vary. <!-- SAF-TRACE: claims=SAF-T2107-C003; sources=SRC-wan23b --> |
| Scope | Multi-System | A promoted model can carry the learned behavior into multiple deployments; promotion boundaries limit spread. <!-- SAF-TRACE: claims=SAF-T2107-C015; sources=SRC-wan23b,SRC-anthropic-small-samples --> |

### Severity Conditions

- **Severity increases when**: Untrusted MCP interactions are collected at scale, lineage gates are absent, and one trained artifact is widely promoted. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C015; sources=SRC-toucan,SRC-wan23b -->
- **Severity decreases when**: Collection and training are separated by origin verification, quarantine, versioned admission, adversarial evaluation, and reversible promotion. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C008; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->

## Detection Methods

### Required Telemetry

| Source | Events or Actions | Required Fields | Collection Notes |
| --- | --- | --- | --- |
| Dataset admission log | MCP-derived sample accepted, rejected, or quarantined | timestamp, origin, server, tool, digest, provenance status, disposition, dataset version | Preserve immutable lineage across transformations. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 --> |
| Training orchestrator log | Dataset version consumed by a job | training job, dataset version, model version, time | Correlate admission with the exact training input. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C009; sources=SRC-toucan,SRC-nist-ai-600-1 --> |

### Indicators of Compromise (IoCs)

- No durable content identifier is established; origin and digest mismatches are risk signals rather than proof of compromise. <!-- SAF-TRACE: claims=SAF-T2107-C009,SAF-T2107-C014; sources=SRC-nist-ai-600-1,SRC-wan23b -->

### Behavioral Indicators

- An MCP-origin sample is admitted while its provenance is missing, invalid, or inconsistent with the approved manifest. <!-- SAF-TRACE: claims=SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- The admitted dataset version is subsequently consumed by a weight-update job. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C009; sources=SRC-toucan,SRC-nist-ai-600-1 -->
- Unexpected trigger-conditioned or degenerate behavior after training increases confidence but requires model evaluation. <!-- SAF-TRACE: claims=SAF-T2107-C003,SAF-T2107-C004; sources=SRC-wan23b,SRC-anthropic-small-samples -->

### Detection Analytic

The standalone example analytic is maintained in [detection-rule.yml](detection-rule.yml).

- **Analytic Goal**: Identify admitted MCP-derived samples whose provenance is missing, invalid, or mismatched. <!-- SAF-TRACE: claims=SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- **Rule Status**: Experimental. <!-- SAF-TRACE: claims=SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- **Detection Logic**: Match an ingestion event with MCP origin and a failed provenance state, excluding quarantined samples. <!-- SAF-TRACE: claims=SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- **Correlation Window**: One dataset-version lifecycle; join to the consuming training job when available. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C009; sources=SRC-toucan,SRC-nist-ai-600-1 -->
- **Known False Positives**: Legacy imports, migration replays, and approved emergency ingestion may lack complete lineage. <!-- SAF-TRACE: claims=SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- **Known Limitations**: The rule does not inspect semantics and misses poison with apparently valid lineage. <!-- SAF-TRACE: claims=SAF-T2107-C014; sources=SRC-wan23b,SRC-anthropic-small-samples -->
- **Tuning Guidance**: Require provenance for external MCP sources and allowlist only documented migration workflows. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->

### Validation

- **Test Data**: [test-logs.json](../../tests/SAF-T2107/test-logs.json)
- **Validation Script**: [test_detection_rule.py](../../tests/SAF-T2107/test_detection_rule.py)
- **Expected Result**: Two positive cases match and four negative or boundary cases do not. See [expected-results.json](../../tests/SAF-T2107/expected-results.json).
- **Last Validated**: 2026-09-02; result recorded in [quality-review.yml](../../research/techniques/SAF-T2107/quality-review.yml).
- **Feasibility Waiver**: None; the analytic has executable representative tests in this bundle. See [quality-review.yml](../../research/techniques/SAF-T2107/quality-review.yml).

## Mitigation Strategies

### Preventive Controls

1. **[SAF-M-33: Training Data Provenance Verification](../../mitigations/SAF-M-33/README.md)**: Require verified origin, content digest, transformation history, and explicit disposition before MCP-derived samples enter a corpus. <!-- SAF-TRACE: claims=SAF-T2107-C007; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
2. **[SAF-M-34: AI Model Integrity Validation](../../mitigations/SAF-M-34/README.md)**: Bind immutable dataset versions to training jobs and reject unexplained changes. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C008; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
3. **Filtering and evaluation**: Apply source vetting, anomaly filtering, and behavior tests, while accounting for accuracy and coverage tradeoffs. <!-- SAF-TRACE: claims=SAF-T2107-C008; sources=SRC-wan23b,SRC-owasp-llm04 -->

### Detective Controls

1. **[SAF-M-33: Training Data Provenance Verification](../../mitigations/SAF-M-33/README.md)**: Alert on failed provenance at admission and retain the decision record. <!-- SAF-TRACE: claims=SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
2. **[SAF-M-36: Model Behavior Monitoring](../../mitigations/SAF-M-36/README.md)**: Compare model behavior before promotion and keep a reversible prior version. <!-- SAF-TRACE: claims=SAF-T2107-C008,SAF-T2107-C014; sources=SRC-wan23b,SRC-owasp-llm04 -->

### Response Procedures

#### Immediate Actions

- Stop promotion of models trained on the suspect dataset version and quarantine the associated MCP-derived records. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C008; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- Preserve server, tool, digest, transformation, dataset, job, and model-version lineage. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C009; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->

#### Investigation Steps

- Reconstruct which MCP records entered each dataset version and which jobs consumed them. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C007; sources=SRC-toucan,SRC-nist-ai-600-1 -->
- Evaluate affected and prior models for the suspected trigger or degradation without assuming lineage proves semantic safety. <!-- SAF-TRACE: claims=SAF-T2107-C008,SAF-T2107-C014; sources=SRC-wan23b,SRC-anthropic-small-samples -->

#### Remediation

- Remove or relabel suspect records, rebuild a versioned corpus, retrain from a trusted checkpoint, and re-run adversarial evaluation. <!-- SAF-TRACE: claims=SAF-T2107-C007,SAF-T2107-C008; sources=SRC-nist-ai-600-1,SRC-owasp-llm04 -->
- Restore the last accepted model when the new artifact cannot be validated. <!-- SAF-TRACE: claims=SAF-T2107-C008; sources=SRC-owasp-llm04,SRC-wan23b -->

## Related Techniques

| Technique | Relationship | Distinction |
| --- | --- | --- |
| [SAF-T1102: Prompt Injection (Multiple Vectors)](../SAF-T1102/README.md) | Alternative | Changes a live inference path without requiring a model-weight update. <!-- SAF-TRACE: claims=SAF-T2107-C001,SAF-T2107-C010; sources=SRC-microsoft-tool-poisoning-2026-06-30,SRC-mcp-tools-2025-06-18 --> |
| [SAF-T3001: RAG Backdoor Attack](../SAF-T3001/README.md) | Alternative | Alters retrieved context rather than learned model weights. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C007; sources=SRC-wan23b,SRC-nist-ai-600-1 --> |
| [SAF-T1002: Supply Chain Compromise](../SAF-T1002/README.md) | Alternative | Alters a checkpoint or model file directly instead of contaminating MCP-derived training data. <!-- SAF-TRACE: claims=SAF-T2107-C006,SAF-T2107-C007; sources=SRC-wan23b,SRC-nist-ai-600-1 --> |

## MITRE ATT&CK Mapping

| ATT&CK ID | Technique | Mapping Type | Rationale |
| --- | --- | --- | --- |
| [T1565.001](https://attack.mitre.org/techniques/T1565/001/) | Stored Data Manipulation | Analogous | Both manipulate stored data to change downstream outcomes, but ATT&CK does not define the MCP-to-training boundary. <!-- SAF-TRACE: claims=SAF-T2107-C003,SAF-T2107-C012; sources=SRC-mitre-t1565.001,SRC-wan23b --> |

### Additional Framework Mappings

| Framework | ID | Name | Rationale |
| --- | --- | --- | --- |
| MITRE ATLAS | AML.T0020 | Poison Training Data | Direct at the model-training layer; SAF-T2107 adds the MCP tool-result origin and admission boundary. <!-- SAF-TRACE: claims=SAF-T2107-C013; sources=SRC-mitre-atlas-safeai,SRC-toucan --> |
| OWASP GenAI | LLM04:2025 | Data and Model Poisoning | Direct conceptual coverage for poisoned training data and provenance controls, without MCP-specific evidence. <!-- SAF-TRACE: claims=SAF-T2107-C002,SAF-T2107-C007,SAF-T2107-C008; sources=SRC-owasp-llm04,SRC-toucan --> |

## References

1. **SRC-mcp-tools-2025-06-18**: [Model Context Protocol Tools specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) — MCP tool results and security considerations.
2. **SRC-toucan**: [TOUCAN — Xu, Meza Soria, Tan, Roy, Agrawal, Poovendran, and Panda](https://arxiv.org/abs/2510.01179) — real MCP interaction trajectories used for fine-tuning.
3. **SRC-wan23b**: [Poisoning Language Models During Instruction Tuning — Wan, Wallace, Shen, and Klein](https://proceedings.mlr.press/v202/wan23b.html) — empirical poisoning and defense tradeoffs.
4. **SRC-anthropic-small-samples**: [A small number of samples can poison LLMs of any size — Souly et al.](https://www.anthropic.com/research/small-samples-poison) — controlled pretraining study and limitations.
5. **SRC-nist-ai-600-1**: [NIST AI 600-1](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958388) — data provenance, incident disclosure, and plugin-input considerations.
6. **SRC-owasp-llm04**: [OWASP LLM04:2025 Data and Model Poisoning](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/) — poisoning risks and controls.
7. **SRC-microsoft-tool-poisoning-2026-06-30**: [Securing AI agents as AI tools move from reading to acting — Microsoft Defender Experts](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/) — adjacent runtime MCP observations.
8. **SRC-nvd-cve-2025-61591**: [NVD CVE-2025-61591](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-61591) — adjacent MCP command-injection record.
9. **SRC-nvd-cve-2025-52573**: [NVD CVE-2025-52573](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-52573) — adjacent MCP command-injection record.
10. **SRC-mitre-t1565.001**: [MITRE ATT&CK T1565.001 Stored Data Manipulation](https://attack.mitre.org/techniques/T1565/001/) — historical analogy.
11. **SRC-mitre-atlas-safeai**: [MITRE ATLAS SAFE-AI report](https://atlas.mitre.org/pdf-files/SAFEAI_Full_Report.pdf) — AML.T0020 mapping.

## Version History

| Version | Date | Changes | Author |
| --- | --- | --- | --- |
| 0.1 | 2026-09-02 | Independent clean-room draft and tested detection | OpenAI Codex clean-room author |
