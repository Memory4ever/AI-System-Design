[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Systems-Level Attack Surface of Edge Agent Deployments on IoT

[3] h6: Abstract.

[4] p: Edge deployment of LLM agents on IoT hardware introduces attack surfaces absent from cloud-hosted orchestration. We present an empirical security analysis of three architectures (cloud-hosted, edge-local swarm, and hybrid) using a multi-device home-automation testbed with local MQTT messaging and an Android smartphone as an edge inference node. We identify five systems-level attack surfaces, including two emergent failures observed during live testbed operation: coordination-state divergence and induced trust erosion. We frame core security properties as measurable systems metrics: data egress volume, failover window exposure, sovereignty boundary integrity, and provenance chain completeness. Our measurements show that edge-local deployments eliminate routine cloud data exposure but silently degrade sovereignty when fallback mechanisms trigger, with boundary crossings invisible at the application layer. Provenance chains remain complete under cooperative operation yet are trivially bypassed without cryptographic enforcement. Failover windows create transient blind spots exploitable for unauthorised actuation. These results demonstrate that deployment architecture, not just model or prompt design, is a primary determinant of security risk in agent-controlled IoT systems.

[5] h6: Keywords:

[6] h2: 1. Introduction

[7] p: LLM-based agents are rapidly moving from cloud APIs to edge hardware controlling physical devices. Commercial deployments now include SwitchBot AI Hub (local agent for smart home, launching Feb 2026) ( SwitchBot, 2026 ) , Home Assistant with MCP integrations enabling agentic automation ( Home Assistant Community, 2025 ) , and distributed frameworks like OpenClaw running on consumer hardware ( OpenClaw Project, 2026 ) . This shift changes the threat model fundamentally: where cloud-hosted agents present a single point of compromise with inherent data exfiltration, edge deployments distribute both capability and attack surface across heterogeneous nodes ( Roman et al., 2018 ) .

[8] p: Recent security incidents highlight the urgency. Over 40,000 exposed OpenClaw gateway instances were discovered in late 2025, with 1,184 malicious packages uploaded to ClawHub (the agent skill repository) ( OpenClaw, 2025 ) . The 7,000-unit DJI Romo vacuum breach (Feb 2026) demonstrated how compromised credentials grant mass control over physically distributed agents ( Hollister, 2026 ) . Yet the systems community has not systematically examined how deployment architecture shapes agent security for IoT.

[9] p: Critically, these agents do not choose their communication infrastructure: they inherit it. MQTT pub/sub is the de facto coordination layer in IoT deployments (AWS IoT Core, Azure IoT Hub, Home Assistant, SwitchBot), handling billions of device messages daily ( Andy et al., 2017 ; Harsha et al., 2018 ) . When LLM agents are deployed on this hardware, MQTT becomes their command-and-control plane by default. Our analysis examines the security consequences of this inheritance: what happens when a protocol designed for telemetry becomes the coordination bus for autonomous agents with physical actuation.

[10] p: Existing agent security research focuses on prompt injection ( Greshake et al., 2023 ; Debenedetti et al., 2024 ) , tool misuse ( Ruan et al., 2023 ) , and model alignment ( Shinn et al., 2023 ; Yao et al., 2022 ) , assuming centralized cloud orchestration ( Zhan et al., 2024 ) . These defenses do not transfer cleanly to edge deployments where: (i) agents run on resource-constrained hardware unable to execute full guardrail stacks locally; (ii) network partitions isolate edge nodes, creating audit gaps; (iii) local data sovereignty eliminates cloud exfiltration risk but enables lateral movement between co-located agents; and (iv) physical actuation latency becomes a security-relevant metric ( Alrawi et al., 2019 ) .

[11] p: We ask: how does deployment architecture change the systems-level attack surface of agent-controlled IoT? Through empirical measurements on our testbed, we make three contributions:

[12] p: Architectural threat characterization. We define three deployment patterns as distinct threat models: cloud-hosted (single point, inherent egress), edge-local swarm (distributed surface, zero egress), and hybrid (inherited risks from both), and enumerate five attack surfaces, including coordination-state divergence and induced trust erosion, two emergent failures observed during testbed operation.

[13] p: Systems metrics as security properties. We measure actuation-to-audit delay, provenance chain completeness, data sovereignty (external egress), and failover vulnerability windows, demonstrating that these systems-level quantities determine the feasibility of real-time safety monitoring, forensic analysis, and attack interception.

[14] p: Empirical findings. Edge-local MQTT pub/sub achieves 23 ms mean actuation-to-audit delay (P95 < < 27 ms), enables complete provenance for cooperative agents but provides zero cryptographic enforcement, eliminates external data egress entirely during normal operation but silently degrades when fallback mechanisms trigger, and exposes vulnerability windows during network failover.

[15] h2: 2. Threat Model and Architecture

[16] h3: 2.1. Deployment Architectures

[17] p: We identify three deployment patterns for LLM agents on IoT, each producing a distinct security posture.

[18] h4: Cloud-Hosted Orchestration.

[19] p: The agent runtime (inference, tool calls, decision loop) executes in cloud infrastructure; IoT devices are controlled via cloud-to-device APIs. All sensor data, commands, and reasoning context transit externally. The architecture provides centralized audit and a single enforcement point, but inherently exfiltrates operational data during WAN partition ( Roman et al., 2018 ) .

[20] h4: Edge-Local Swarm.

[21] p: Multiple agents run on local hardware, coordinating via a local message broker with no cloud dependency for normal operation. Operational data never leaves the local network. The architecture distributes the attack surface across heterogeneous nodes, requires per-node compromise, but lacks centralized enforcement and places resource constraints on local guardrails.

[22] h4: Hybrid (Edge + Cloud).

[23] p: Edge agents handle low-latency actuation; cloud handles heavy inference. Unless carefully partitioned, this pattern inherits the attack surfaces of both: cloud egress for inference traffic plus a distributed local surface for actuation.

[24] h3: 2.2. Testbed

[25] p: We deploy an actively-used edge-local agent swarm with different LLM models utilizing Openclaw ( OpenClaw, 2025 ) to control real IoT hardware (operational daily for home automation and research coordination):

[26] p: Mac mini M4 (16 GB, macOS): orchestrator agent “Rupert” (Claude Opus 4.6), MQTT broker

[27] p: Moto G35 (Android 15, Termux): mobile edge agent “Percy” (Gemini 3.1 Pro)

[28] p: Intel NUC N150 (16 GB, Ubuntu 24.04): Home Assistant bridge and IoT gateway “Jeeves” (GPT-5.2)

[29] p: IoT devices: Philips Hue lights (5), smart switches (3), camera (1), motion sensors (2), speaker (1), microphone(1)

[30] h4: MQTT as coordination backbone.

[31] p: We do not advocate MQTT as an agent communication protocol; rather, our testbed inherits MQTT from the IoT ecosystem it controls. All inter-agent communication uses MQTT pub/sub on the Mac mini broker (port 1883, Tailscale ( Donenfeld, 2017 ) mesh only; no public exposure). Agents publish to topic-structured channels using a JSON envelope carrying sender ID, message type, microsecond timestamp, correlation ID, and payload. The NUC bridges MQTT to Home Assistant’s REST API for IoT device control. Model inference calls traverse WAN to cloud providers; all operational IoT traffic remains mesh-local.

[32] p: This design makes MQTT the sole coordination plane for the swarm: every agent decision, actuation command, status update, and audit record passes through the broker. Consequently, the security properties of the MQTT layer directly determine the security posture of the entire deployment.

[33] figure: Figure 1. Testbed topology. Inter-agent traffic traverses the Tailscale mesh via MQTT pub/sub on the Mac mini. The NUC bridges MQTT to Home Assistant for IoT actuation. WAN links carry only LLM inference and Telegram traffic. Network topology diagram showing three agent nodes connected via Tailscale VPN mesh with MQTT messaging, plus external API connections for inference and messaging.

[34] h3: 2.3. Attack Surfaces

[35] p: We identify five systems-level attack surfaces that are architectural consequences of edge-local deployment, not present (or present differently) in cloud-hosted orchestration. We exclude model-level attacks (prompt injection, jailbreaking) and supply chain attacks. These are orthogonal to deployment architecture and addressed by complementary defenses ( Greshake et al., 2023 ) . We assume three attacker capabilities: (1) remote network access (e.g., compromised credentials, exposed MQTT port); (2) physical access to an edge node (e.g., stolen phone, USB debugging); (3) a rogue agent within the swarm (e.g., compromised skill package installing a malicious MQTT client).

[36] p: Table 1 summarises the five surfaces, their architectural root causes, and the systems metrics that expose them.

[37] figure: Table 1. Attack surfaces of edge-local agent deployments. Each surface is an architectural consequence of the deployment pattern, measurable through systems-level artifacts. Surface Root Cause Attack / Effect Metric § S1a No cryptographic binding in MQTT envelope Agent impersonation; command replay Spoofed msg acceptance rate 3.2 S1b No shared state plane; message-only coordination Silent context drift; persistent corruption Divergent context copies 3.2 S1c No tiered trust in MQTT bus Induced channel distrust; operator lockout Out-of-band recovery required 3.2 S2 Sovereignty boundary is runtime, not architectural Silent data exfiltration via fallback DNS egress; bytes to cloud 3.3 S3 Audit asynchronous; failover creates blind spots Unaudited actuation during blackout Reconnect window (s) 3.4

[38] p: We group S1a–c as a family reflecting their shared root cause (unauthenticated MQTT coordination) while distinguishing their distinct exploitation patterns and operational manifestations.

[39] h4: S1a: Provenance forgery.

[40] p: Provenance in our edge swarm is self-reported metadata in the MQTT JSON envelope with no cryptographic binding ( Mishra and Kertesz, 2020 ; Firdous et al., 2017 ) . Any client with broker credentials can impersonate any agent or publish to safety-critical topics.

[41] h4: S1b: Coordination-state divergence.

[42] p: Without a shared state plane, each agent assembles shared context incrementally from MQTT messages, embedding full copies that drift silently. We observed two failure modes: (i) redundant state duplication (file contents embedded rather than referenced) and (ii) invisible semantic drift (independent modifications with no conflict detection).

[43] h4: S1c: Induced trust erosion.

[44] p: An attacker publishes obviously-forged messages on the MQTT bus. The defending agent, unable to distinguish forged from legitimate traffic, treats the entire channel as compromised and refuses subsequent operator commands. We observed this during testbed operation: recovery required out-of-band confirmation via human admin through Telegram.

[45] h4: S2: Silent sovereignty degradation.

[46] p: Edge-local deployment eliminates external egress by construction. However, when an agent falls back to cloud inference (resource exhaustion, model unavailability), operational data silently transits externally with no notification or audit record. The sovereignty boundary degrades under stress precisely when monitoring is most needed.

[47] h4: S3: Actuation-audit temporal gap.

[48] p: Every command has a delay between physical actuation and the audit record becoming observable. During network failover, we observe multi-second windows where agents actuate with no audit trail, with the network stack as the dominant bottleneck.

[49] figure: Figure 2. MQTT message flow and supervision architecture. Agents communicate via per-agent inbox topics ( agents/inbox/{id} ), with all messages streamed to agents/mirror for real-time human monitoring via Telegram. A rogue client (bottom-left) can publish directly to agent inboxes, bypassing the supervision layer—illustrating the provenance gap measured in Table 4 . MQTT message flow diagram showing three agent nodes communicating via named inbox topics, a broadcast topic for heartbeats, a supervision layer mirroring all messages to Telegram for human oversight, and a rogue client bypassing the mirror with direct publishes to agent inboxes.

[50] h2: 3. Empirical Analysis

[51] h3: 3.1. Actuation-to-Audit Delay

[52] p: For agent-controlled physical systems, unauthorized actions must be detected before physical completion. A door lock command takes ∼ 500 {\sim}500 ms to actuate; if the audit trail records the command within that window, a safety monitor can intercept it.

[53] h4: Metric and method.

[54] p: MQTT round-trip latency: Rupert publishes → \to Percy receives and echoes → \to Rupert records. Three payload sizes (50 B, 1 KB, 10 KB), N = 150 N{=}150 messages per class, microsecond-precision timestamps.

[55] h4: Mac mini → \to Moto G35 (via Tailscale, N = 150 N{=}150 per size).

[56] figure: Table 2. Actuation-to-audit delay: Mac mini → \to Moto G35 via Tailscale ( N = 150 N{=}150 per payload size). Payload Mean Median P95 P99 50 B 23.6 ms 23.4 ms 26.9 ms 33.0 ms 1 KB 22.5 ms 22.4 ms 26.6 ms 30.6 ms 10 KB 34.5 ms 34.2 ms 41.9 ms 44.6 ms

[57] h4: NUC → \to Mac mini (cross-validation, N = 50 N{=}50 per size).

[58] figure: Table 3. Cross-validation latency: NUC → \to Mac mini ( N = 50 N{=}50 per payload size). Payload Mean P95 128 B 64.4 ms 65.0 ms 1 KB 64.3 ms 64.8 ms 8 KB 64.5 ms 65.1 ms

[59] p: The 2.7 × 2.7{\times} latency difference between paths (Tables 2 and 3 ) reflects node heterogeneity: the NUC’s low-power N150 processor (single performance core) versus the Mac mini’s M4 (8 cores, unified memory architecture). Notably, the NUC path shows near-zero variance across payload sizes (64.3–64.5 ms), suggesting a fixed scheduling overhead rather than serialization cost. Both paths remain well within the interception window for physical actuators.

[60] h4: Burst resilience.

[61] p: Under sustained load on the NUC ( N = 100 N{=}100 messages at 128 B, rapid-fire), mean latency is 49.8 ms with 0% degradation. It confirms that the MQTT broker handles burst traffic without queuing delays even from the most constrained node.

[62] h4: Implication.

[63] p: Real-time safety monitors are feasible for edge-local MQTT deployments. A monitor subscribing to the audit topic observes every action within ∼ 23 {\sim}23 ms on the fastest path (64 ms on the NUC path). It is within the actuation window of electromechanical devices such as door locks ( ∼ 500 {\sim}500 ms) and motorized valves ( ∼ 1 {\sim}1 – 2 2 s), though insufficient for solid-state relays ( < 5 {<}5 ms).

[64] h3: 3.2. Provenance Chain Completeness

[65] p: Forensic analysis requires full provenance: which agent issued which command, when, and in response to what event.

[66] h4: Cooperative agents.

[67] p: We audit 100 agent commands across 5 action types. All messages carry complete metadata: sender ID, ISO-8601 timestamp, UUID correlation ID, message type, and action details. Coverage: 100% across all fields.

[68] h4: Adversarial testing.

[69] p: We probe MQTT’s enforcement against malicious clients:

[70] figure: Table 4. Adversarial MQTT provenance testing: all attacks accepted by the broker. Attack Broker Response Impact Missing sender field Accepted Untraceable command Spoofed sender Accepted Rogue agent frames others Replayed message Accepted Command re-executed Direct safety publish Accepted Agent logic bypassed

[71] p: MQTT provides transport-level delivery but no application-level security enforcement (Table 4 ). Provenance therefore depends entirely on agent cooperation. Message signing (HMAC/JWT), nonce-based replay protection, and topic access-control lists (ACLs) are required yet absent from the default deployment. None of the open-source agent frameworks we surveyed implement them either.

[72] h3: 3.3. Data Sovereignty and Egress

[73] p: We capture all network traffic on the NUC during a 10-minute agent task session (50 MQTT publishes, 200 sensor reads, 30 light commands) and compare against equivalent cloud API calls.

[74] figure: Table 5. Data egress comparison: edge-local vs. cloud architecture during a 10-minute operational session. Architecture External IPs Bytes Sent Operations Edge-local MQTT 0 0 B 280 Cloud (OpenAI API) 3 64,981 B 10

[75] p: Edge-local deployments exhibit zero external data egress during normal operation (Table 5 ). All communication remains within the Tailscale mesh. The operation counts differ because our cloud baseline captures only inference API calls, not a full cloud-orchestrated workload performing identical tasks. The comparison demonstrates the structural egress difference rather than a controlled workload-matched measurement. Even so, a minimal cloud workload produces 65 KB of egress, while more edge-local operations produce zero. This eliminates structural data exfiltration as an attack vector: an adversary cannot observe agent context by monitoring cloud API traffic but must compromise a node within the mesh.

[76] h4: Forced fallback: sovereignty under stress.

[77] p: To validate S2, we triggered a sovereignty boundary crossing by sending the mobile agent (Percy) a 109 KB sensor dump exceeding its local model’s context capacity. The agent framework’s fallback chain silently routed inference to a cloud provider (Anthropic API). We captured traffic via tcpdump on the Mac mini, filtering Percy’s Tailscale IP.

[78] figure: Table 6. Sovereignty boundary crossing: baseline vs. forced fallback. Metric Baseline Fallback Packets captured 10,473 14,638 Packets to/from Percy 190 434 DNS queries to api.anthropic.com 0 10 Resolved IP — 160.79.104.10 User notification N/A None MQTT-layer anomaly N/A None

[79] p: The sovereignty violation is invisible at the application layer (Table 6 ): MQTT message patterns are identical before and after fallback, and the agent itself reported only a “brief glitch”. No indication that operational context had transited to external infrastructure. Only DNS-level monitoring (tcpdump) revealed the boundary crossing. The local model returned a CANCELLED error (code 499) confirming resource exhaustion as the trigger. This validates the S2 threat: an adversary can force sovereignty degradation by inducing resource exhaustion, causing the agent framework to silently exfiltrate context via legitimate fallback channels.

[80] h3: 3.4. Failover Vulnerability Windows

[81] p: Mobile edge agents experience network transitions during which they are unreachable and unauditable.

[82] h4: Method.

[83] p: Percy connects via WiFi to the MQTT broker (Tailscale tunnel). We disable WiFi, forcing failover to an ADB/USB bridge path. Keep-alive pings at 500 ms intervals measure the blackout window. We decompose failover into two phases: (a) network stack recovery (WiFi re-association, Tailscale tunnel re-establishment) and (b) MQTT reconnection (client-side reconnect to broker).

[84] h4: End-to-end failover.

[85] p: 35.7 s from WiFi loss to first successful ping via the ADB fallback path—dominated by network stack recovery (33.6 s) and ADB bridge establishment.

[86] h4: MQTT reconnection in isolation ( N = 50 N{=}50 ).

[87] p: To isolate the MQTT layer, we simulate broker disconnection at the application level (firewall block/unblock) across varying block durations:

[88] figure: Table 7. MQTT reconnection latency in isolation ( N = 50 N{=}50 ). Metric Value Mean reconnection time 9.3 ms ( σ = 1.9 \sigma=1.9 ms) P95 14 ms P99 17 ms Block-duration effect None (8.5–10.1 ms)

[89] p: MQTT reconnection is near-instantaneous ( < 20 {<}20 ms, Table 7 ). The 35 s end-to-end failover window is entirely attributable to the network and VPN stack, not the messaging layer. This has design implications: reducing the vulnerability window requires network-level solutions (fast roaming, multi-path transport) rather than application-level optimizations.

[90] h4: Implication.

[91] p: During the 35 s blackout, a mobile agent cannot receive commands, publish audit logs, or be monitored. If the agent executes a safety-critical action immediately before network loss, the action log is delayed by 35+ s. An attacker who can induce network disruption gains a predictable blind spot.

[92] h2: 4. Discussion

[93] h3: 4.1. Architecture IS Security Posture

[94] p: Our measurements support a central claim: for agent-controlled physical systems, deployment architecture determines security posture more than any model-level or prompt-level mitigation. Consider the contrast:

[95] p: A cloud-hosted agent with state-of-the-art prompt guardrails still transmits 65 KB of context per planning cycle to external infrastructure, a structural exfiltration channel that no amount of alignment tuning can close.

[96] p: An edge-local agent with no guardrails produces zero external egress and enables 23 ms actuation-to-audit delay, sufficient for real-time interception of most physical actuators.

[97] p: This is not an argument against model-level safety. It is an argument that the systems community has underweighted architectural decisions. The choice of where to run the agent, how to connect it to devices, and what transport to use for audit logs has measurable, quantifiable security consequences that dominate the threat surface for IoT deployments. An open question is guardrail placement: edge hardware cannot run full guardrail stacks locally, suggesting a tiered model with fast local checks and deferred cloud verification for high-stakes actions. Similarly, the 35 s vulnerability window (§ 3.4 ) implies that safety-critical actions should be deferred when network stability is uncertain. Integrating network health signals into agent planning remains unexplored.

[98] h3: 4.2. The Provenance Gap

[99] p: Our adversarial MQTT testing (§ 3.2 ) reveals a critical gap: no open-source agent framework provides cryptographic provenance enforcement. In a cooperative swarm this is invisible as all messages arrive with correct metadata. But a single compromised node can impersonate any agent, replay commands, and publish directly to safety-critical topics.

[100] p: This gap is architectural, not incidental. MQTT was designed as a lightweight pub/sub transport, not a secure command-and-control protocol. Closing the gap requires: (i) per-agent signing keys with broker-side verification; (ii) nonce-based replay protection; and (iii) topic-level ACLs enforced at the broker. These are well-understood techniques, but their absence from current agent frameworks reflects a community assumption that agents operate in trusted environments, an assumption that IoT deployments invalidate ( OWASP Foundation, 2025 ; Alrawi et al., 2019 ) . Scaling beyond our three-agent testbed to N N agents will require formal trust policies: capability delegation and least-privilege topic access. None of these are provided by MQTT natively.

[101] h3: 4.3. Emergent Coordination Failures

[102] p: Operating the testbed revealed two failure modes not anticipated in our initial threat model, both arising from the absence of coordination-layer security primitives. These are gaps identified as open problems in recent multi-agent LLM surveys ( Guo et al., 2024 ; Talebirad and Nadiri, 2023 ) .

[103] h4: State-plane divergence (S1b).

[104] p: During multi-agent task coordination, agents maintained inconsistent local views of shared context. Without a shared filesystem or state-synchronisation protocol, agents embedded full task specifications in MQTT messages rather than referencing canonical files. It creates divergent copies that drifted within minutes. One agent participated in an experiment via MQTT while its Telegram-facing session remained unaware the experiment had occurred. This is a direct consequence of message-based coordination: MQTT carries messages, not state. We addressed this operationally by layering a git-backed shared state plane over the MQTT bus, providing content-addressed versioning, agent-attributed commits, and explicit conflict detection.

[105] h4: Induced trust erosion (S1c).

[106] p: After a series of provenance-testing messages (S1a adversarial experiments), the orchestrator agent began treating all MQTT traffic as potentially adversarial, refusing legitimate operator commands received on the same channel. Resolution required out-of-band communication via Telegram, a trusted secondary channel. The attack requires no actual compromise: an adversary need only publish forged messages to degrade operator trust in the coordination bus. This is a denial-of-service via induced paranoia , exploiting the absence of tiered trust in MQTT.

[107] h3: 4.4. Silent Sovereignty Degradation

[108] p: Our forced-fallback experiment (§ 3 , Table 6 ) confirms that edge-local data sovereignty is a runtime property, not an architectural guarantee. The boundary crossing was invisible at every layer except DNS: MQTT messages showed no anomaly, the agent reported only a “brief glitch,” and no audit record indicated that operational context had left the local network. Mitigation requires sovereignty-aware fallback policies: either blocking cloud fallback entirely for sensitive contexts, or injecting explicit audit markers when the boundary is crossed.

[109] h3: 4.5. Limitations

[110] p: Our measurements derive from a single three-node testbed with one MQTT broker, one VPN substrate (Tailscale), and one IoT platform (Home Assistant); generalisation to other topologies, brokers, and network substrates remains future work. The cloud egress comparison (Table 5 ) is not workload-matched: the cloud baseline captures only inference API calls, not a full cloud-orchestrated workload performing identical tasks, and serves as a directional baseline demonstrating structural egress differences rather than a controlled experiment. We do not implement or evaluate mitigation prototypes (e.g., HMAC signing, topic ACLs, sovereignty-aware fallback policies); our contribution is identifying and measuring the attack surfaces, not closing them. The three S1-family surfaces (S1a–c) share a common root cause and could be viewed as facets of a single vulnerability rather than independent attack surfaces; we distinguish them because their exploitation patterns and operational manifestations differ significantly. Finally, our failover measurements reflect a specific WiFi → \to ADB bridge path; other failover mechanisms (e.g., WiFi → \to 5G, multi-path TCP) would yield different window durations.

[111] h2: 5. Related Work

[112] h4: LLM agent security.

[113] p: Greshake et al. ( Greshake et al., 2023 ) and Zhan et al. ( Zhan et al., 2024 ) demonstrated prompt injection and surveyed agent attacks, both assuming cloud-hosted architectures. Xi et al. ( Xi et al., 2025 ) proposed guardrail taxonomies without addressing edge deployment constraints. AgentDojo ( Debenedetti et al., 2024 ) and LM-emulated sandboxes ( Ruan et al., 2023 ) evaluate agent vulnerabilities in controlled settings; OWASP ( OWASP Foundation, 2025 ) and PASB ( Wang et al., 2026 ) catalogue and benchmark agentic risks. These works focus on what agents do wrong (tool misuse, prompt compliance); we complement them by examining how the infrastructure agents inherit shapes the attack surface independent of model behaviour.

[114] h4: Edge AI, IoT, and MQTT security.

[115] p: Edge computing security surveys ( Shi et al., 2016 ; Roman et al., 2018 ) identify data sovereignty as a central concern; we measure it empirically and show it degrades silently under resource exhaustion. IoT security work has focused on device-level vulnerabilities ( Meneghello et al., 2019 ; Alrawi et al., 2019 ) and smart-home automation risks ( Surbatovich et al., 2017 ) , but not the LLM agent layer that now mediates between user intent and physical actuation. MQTT-specific analyses ( Andy et al., 2017 ; Harsha et al., 2018 ; Firdous et al., 2017 ; Mishra and Kertesz, 2020 ) document authentication and access control gaps in telemetry contexts; we show these gaps become safety-critical when MQTT carries autonomous agent commands to physical actuators. Our testbed uses WireGuard ( Donenfeld, 2017 ) via Tailscale, but our findings confirm that transport-layer encryption does not address application-layer coordination vulnerabilities (S1a–c).

[116] h4: Multi-agent coordination.

[117] p: Dorri et al. ( Dorri et al., 2017 ) applied blockchain to IoT multi-agent trust, a solution ill-suited to resource-constrained edge nodes where our NUC already exhibits 2.7 × 2.7{\times} latency overhead. Calvaresi et al. ( Calvaresi et al., 2018 ) surveyed negotiation protocols assuming static agent populations; LLM agent swarms add and remove nodes dynamically. LLM-specific multi-agent work ( Talebirad and Nadiri, 2023 ; Guo et al., 2024 ) identifies coordination and trust as open problems but reasons about them abstractly; we ground these concerns in empirical measurements from an operational deployment controlling real IoT hardware.

[118] h2: 6. Conclusion

[119] p: Through empirical measurements on a three-node edge-local agent swarm, we showed that deployment architecture, not model or prompt design, is the primary determinant of security posture for agent-controlled IoT. Edge-local MQTT eliminates structural data exfiltration and enables actuation-to-audit delay, but provides zero cryptographic provenance enforcement, exposes failover blind spots, and silently degrades data sovereignty under stress. Two emergent failures (coordination-state divergence and induced trust erosion) further demonstrate that unauthenticated message buses are insufficient for multi-agent coordination. Closing these gaps requires per-agent signing keys, sovereignty-aware fallback policies, and network-level fast roaming; none are provided by current agent frameworks. The systems community should treat where agents run and how they communicate as first-class security design choices, not implementation details subordinate to model-level alignment.

[120] h2: References

[121] h2: Instructions for reporting errors

[122] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[123] p: Tip: You can select the relevant text first, to include it in your report.

[124] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[125] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
