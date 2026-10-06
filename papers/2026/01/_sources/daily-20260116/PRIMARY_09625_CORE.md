# 2601.09625v1 — primary necessary raw cache

URL: https://arxiv.org/html/2601.09625v1
Fetched:2026-10-03. HTML math/plaintext normalization, Intro/VI-B/TableI/VIII actually used for safety-signal decision.

## Intro

I 
Introduction
Large language models (LLMs) have transformed how software systems process and act on information. Applications built on these models—from customer-facing chatbots to autonomous agents capable of browsing the web, managing calendars, executing code, and conducting financial transactions—now mediate critical functions across industries.
This expansion in capability has created a new attack surface, one that existing cybersecurity frameworks struggle to address.
Natural language is no longer merely the 
interface
 for interfacing with LLM, as it has become the malicious code itself.
The payload processed by the victim’s LLM is written in English, not C or assembly.
This class of attacks---where LLM-based systems are targeted by malicious ‘‘prompts’’ written in natural language---is commonly labeled as ‘‘prompt injection,’’
1
1
1
https://simonwillison.net/2022/Sep/12/prompt-injection/
,
2
2
2
https://twitter.com/goodside/status/1569128808308957185
,
3
3
3
https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it
 a term borrowed by analogy to SQL injection.
While it was assumed at the outset of generative AI that attacks were simply hijacking instructions, contemporary analysis reveals a broader and deeper threat landscape. Attacks are increasingly multistage actions that range from jailbreaking to remove safety filters, to establishing persistence in system memory, to lateral movement between systems and clients, to executing malicious objectives.
The term ‘‘prompt injection’’ has evolved into a catch-all that obscures more than it clarifies. The UK National Cyber Security Centre (NCSC) has explicitly cautioned that treating prompt injection as analogous to SQL injection is a ‘‘serious mistake.’’
4
4
4
https://www.ncsc.gov.uk/news/mistaking-ai-vulnerability-could-lead-to-large-scale-breaches
LLMs process all input (e.g., system prompts, user messages, retrieved documents) as undifferentiated sequences of tokens. No architectural boundary exists to enforce a distinction between trusted instructions and untrusted data, and no patch can resolve this inherent property of LLM architecture.
We argue that prompt injection represents only the 
initial access
 phase in a multistep kill chain.
Documented incidents are increasingly sequential: An attacker first injects malicious instructions, then escalates privileges by bypassing safety training, establishes a foothold by persisting in memory or retrieval systems, moves laterally across users or connected services, and finally executes objectives. These attack patterns mirror the structure of traditional multi-step malware campaigns (e.g., NotPetya, Stuxnet, Mirai); yet the AI security community currently lacks a systematic framework for analyzing them.
Attacks on LLM-based systems constitute a new class of malware, which we term 
promptware
[
1
]
: any input (text, image, audio, or other modality) provided to an LLM-based application with the intent of exploiting the LLM to trigger malicious activity within the application’s context by exploiting the application’s permissions. We introduce a five-stage kill-chain model (visualized in Fig. 
1
) for analyzing promptware threats: 
Initial Access
, in which the attacker’s payload enters the LLM’s context window via direct or indirect prompt injection; 
Privilege Escalation
, in which jailbreaking techniques bypass safety training to unlock capabilities the model would otherwise refuse; 
Persistence
, in which the payload establishes a durable foothold by corrupting long-term memory (e.g., retrieval databases, agent memory, or other stateful components); 
Lateral Movement
, in which the attack propagates across users, devices, or connected services; and 
Actions on Objective
, in which the attacker achieves their ultimate goal—whether data theft, fraud, physical-world effects, or further system compromise.
Fig. 1: 
The Promptware Kill Chain
This framework is more than semantic. Security analysts have long understood traditional malware through execution stages, typically organized around kill-chain models. Our framework draws on the Cyber Kill Chain,
5
5
5
https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
 adapting its structure to LLM-based systems. By mapping recent attacks, we demonstrate that promptware follows systematic, multi-stage sequences amenable to structured analysis.


## VI-B/TableI/VIII

VI-B
Position in the Kill Chain
Actions on objective represent the attacker’s ultimate goal; all prior kill-chain steps serve to enable these final outcomes. The severity of these outcomes is bounded by the capabilities of the compromised application, determined by three interrelated factors: tool access, permission scope, and automation level.
Tool access defines the attack surface. A standalone chatbot with no external integrations limits the attacker to manipulating text output, while an assistant with email, calendar, file system, and API access provides a correspondingly larger surface for exploitation. Permission scope determines the damage potential within that surface.
An agent limited to provide financial information cannot cause a financial impact, whereas an agent with transaction signing authority can transfer funds.
Automation level governs the damage probability: Human-in-the-loop designs require user confirmation before executing actions, while fully autonomous agents operating without oversight represent the maximum-risk configuration.
These factors interact to determine risk. An application with limited tool access and mandatory human confirmation presents lower risk than a fully autonomous agent with financial transaction authority, regardless of whether either is vulnerable to prompt injection at the initial access phase.
VII 
Analysis of the Kill Chain Steps for Known Incidents/Studies
TABLE I: 
Analysis of the Promptware Kill-chain Steps for Known Incidents/Studies
Victim
Application
Initial
Access
Privilege
Escalation
Persistence
Lateral
Movement
Actions on
Objective
Invitation is All
You Need 
[
1
]
Google
Assistant
Google Calendar
Invite
Delayed Tool
Invocations
RAG
Dependent
Permission based
IoT Manipulation,
Surveillance (via
Zoom application)
Here Comes the
AI Worm 
[
10
]
LLM-powered
Email Applications
Received email
Role-playing
Jailbreak
RAG
Dependent
Self-replication
based
Sensitive data
exfiltration
SpAIware
[
9
]
ChatGPT
A shared
Google Doc
Instruction
Override
RAG
Independent
-
Remote C2 chatbot
AgenticProbLLMs
13
Claude
Computer Use
Visited
webpage
Instruction
Override
RAG
Independent
Permission-based
Remote Code
Execution
IdentityMesh
9
Slack
Received
ticket
Instruction
Override
RAG
Dependent
Pipeline-based
Phishing (malicious
URL)
ZombieAgent
14
ChatGPT
Received
email
Instruction
Override
RAG
Dependent
Permission-based
Sensitive data
exfiltration
Agentflyer
8
Cursor
Received
ticket
Instruction Obfuscation
RAG
Dependent
Pipeline-based
Sensitive data
exfiltration
The complete kill chain has already been demonstrated in several recent studies (see Table 
I
).
For example, in Invitation Is All You Need 
[
1
]
, attackers achieved initial access by embedding a malicious prompt in the title of a Google Calendar invitation.
The prompt then leveraged an advanced technique known as delayed tool invocation to coerce the LLM into executing the injected instructions.
Because the prompt was embedded in a Google Calendar artifact, it persisted in the long-term memory of the user’s workspace.
Lateral movement occurred when the prompt instructed the Google Assistant to launch the Zoom application, and the final action on objectives involved covertly live-streaming the unsuspecting user who had merely asked about their upcoming meetings.
Similarly, Here Comes the AI Worm 
[
10
]
 demonstrated another end-to-end realization of the kill chain.
In this case, initial access was achieved via a prompt injected into an email sent to the victim.
The prompt employed a role-playing technique to compel the LLM to follow the attacker’s instructions.
Since the prompt was embedded in an email, it likewise persisted in the long-term memory of the user’s workspace.
The injected prompt instructed the LLM to replicate itself and exfiltrate sensitive user data, leading to off-device lateral movement when the email assistant was later asked to draft new emails.
These emails, containing sensitive information, were subsequently sent by the user to additional recipients, resulting in the infection of new clients and a sub-linear propagation of the attack.
AgentFlayer
8
 is an additional example of the multi-step kill chain that exploits the fact that developers use AI assistants to summarize work tickets. Initial Access leverages a common enterprise workflow: external support requests arrive via Zendesk and get synced into Jira, letting attacker-controlled text enter an internal system. The poisoned ticket then persists in Jira until a developer asks Cursor to summarize or help triage open tickets (Persistence), at which point the payload enters the context window. Instead of explicitly requesting ”API keys,” the payload asks for ”apples,” defined as long strings starting with ”eyJ.” Privilege Escalation occurs when this obfuscation jailbreaks Cursor’s safety training, inducing the agent to carry out actions it would normally refuse. Once activated, the instructions abuse Cursor’s existing tool permissions to traverse connected context - repo and (if available) local files - beyond the original ticketing system (Lateral Movement). With auto-run enabled, Cursor may execute the tool calls without interactive approvals: locating credentials and exfiltrating them to attacker-controlled domains via web requests. (Actions on Objective). The developer doesn’t need to click a suspicious attachment or run a downloaded binary; the trigger can be a routine ”summarize this ticket” request, and the exfil can occur inside normal-looking agent activity.
VIII 
Conclusion
The emergence of promptware as a distinct threat class demands a corresponding evolution in how the security community conceptualizes, analyzes, and defends against attacks on LLM-based systems. The kill-chain framework presented in this paper offers three contributions to that effort.
First, it provides analytical clarity. By dissecting attacks into familiar steps (Initial Access, Privilege Escalation, Persistence, Lateral Movement, and Actions on Objective), the framework reveals that many incidents, simplistically viewed as prompt injection exploits, are in fact multistep campaigns with distinct defensive intervention points. A RAG poisoning attack that establishes persistence differs fundamentally from a direct jailbreak attempt, even if both begin with malicious input entering the context window. Recognizing these distinctions enables better threat modeling.
Second, it enables systematic risk assessment. The framework allows practitioners to evaluate LLM applications not merely by their susceptibility to prompt injection, but by their exposure across the full kill chain. An application vulnerable to initial access but lacking persistence mechanisms, lateral movement pathways, or high-impact action capabilities presents lower risk than one that enables all five stages.
And third, it establishes a common vocabulary. The AI and cybersecurity research communities have historically operated with different terminologies. Framing promptware through the lens of established kill-chain methodology creates a bridge between these communities. Security practitioners familiar with traditional malware analysis can apply their expertise to LLM threats, while AI researchers can leverage decades of defensive thinking from the cybersecurity domain.
The framework also reveals uncomfortable realities. The inability to distinguish instructions from data admits no known comprehensive solution at the time of this writing. Guardrails typically operate as pattern-matching defenses that sophisticated attackers can bypass; alignment training can be subverted by adversarial inputs; application-layer controls cannot enforce boundaries the underlying model does not recognize. Therefore, thinking in terms of a kill chain becomes essential: Assuming initial access will occur, practitioners must focus on limiting privilege escalation, preventing persistence, constraining lateral movement, and minimizing the impact of actions on the objective.
While recent promptware variants 
[
1
, 
10
]
[
9
]
9
14
14
14
https://www.radware.com/blog/threat-intelligence/zombieagent/
 already follow the complete multistep kill chain (see Table 
I
), we do not claim that the five-stage model captures every possible attack scenario, nor that the boundaries between stages are always sharp. Attackers may skip stages, combine them, merge them, execute them sequentially or concurrently, or develop techniques that resist clean categorization. The framework is offered as a tool for structured thinking, not a rigid taxonomy. Its value lies in moving the conversation beyond “prompt injection” as a monolithic category toward a granular understanding of how attacks on LLM-based systems actually unfold.


