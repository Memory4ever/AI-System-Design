# 2601.09382v1 primary core

URL https://arxiv.org/html/2601.09382v1
Exact version core read; normalized HTML original text, not summary.


Long-term Task-oriented Agent: Proactive Long-term Intent Maintenance in Dynamic Environments
Title:
Content selection saved. Describe the issue below:
Description:
arXiv is now an independent nonprofit!
Learn more
×
    License: arXiv.org perpetual non-exclusive license
arXiv:2601.09382v1 [cs.AI] 14 Jan 2026
Long-term Task-oriented Agent: Proactive Long-term Intent Maintenance in Dynamic Environments
Qinglong Shi
Affiliation: 
School of Management, University of Science and Technology of China, Anhui, China
Donghai Wang
Affiliation: 
Meituan, Beijing, Chinaivyinautumn@mail.ustc.edu.cn{xujun58, gaojiuchong}@meituan.com
Hantao Zhou
Affiliation: 
Meituan, Beijing, Chinaivyinautumn@mail.ustc.edu.cn{xujun58, gaojiuchong}@meituan.com
Jiguo Li
Affiliation: 
Meituan, Beijing, Chinaivyinautumn@mail.ustc.edu.cn{xujun58, gaojiuchong}@meituan.com
Jun Xu
Affiliation: 
Meituan, Beijing, Chinaivyinautumn@mail.ustc.edu.cn{xujun58, gaojiuchong}@meituan.com
Jiuchong Gao
Affiliation: 
Meituan, Beijing, Chinaivyinautumn@mail.ustc.edu.cn{xujun58, gaojiuchong}@meituan.com
Jinghua Hao
Affiliation: 
Meituan, Beijing, Chinaivyinautumn@mail.ustc.edu.cn{xujun58, gaojiuchong}@meituan.com
Renqing He
Affiliation: 
Meituan, Beijing, Chinaivyinautumn@mail.ustc.edu.cn{xujun58, gaojiuchong}@meituan.com
Abstract
Current large language model agents predominantly operate under a reactive paradigm, responding only to immediate user queries within short-term sessions. This limitation hinders their ability to maintain long-term user’s intents and dynamically adapt to evolving external environments. In this paper, we propose a novel interaction paradigm for 
proactive Task-oriented Agents
 capable of bridging the gap between relatively static user’s needs and a dynamic environment. We formalize proactivity through two key capabilities, (i) Intent-Conditioned Monitoring: The agent autonomously formulates trigger conditions based on dialog history; (ii) Event-Triggered Follow-up: The agent actively engages the user upon detecting useful environmental updates. We introduce a high-quality data synthesis pipeline to construct complex, multi-turn dialog data in a dynamic environment. Furthermore, we attempt to address the lack of evaluation criteria of task-oriented interaction in a dynamic environment by proposing a new benchmark, namely 
ChronosBench
. We evaluated some leading close-source and open-source models at present and revealed their flaws in long-term task-oriented interaction. Furthermore, our fine-tuned model trained using synthetic data for supervised learning achieves a task completion rate of 85.19% for complex tasks including shifts in user intent, outperforming other models under test. And the result validated the effectiveness of our data-driven strategy.
†
†
footnotetext: 
∗
Work done during internship at Meituan
†
†
footnotetext: 
†
Corresponding authors: Jun Xu, Jiuchong Gao
1 
Introduction
Large Language Models (LLMs) have achieved remarkable success in serving as conversational assistants 
(
Xi et al. 2025
)
, demonstrating exceptional proficiency in instruction following and knowledge retrieval 
(
Sumers et al. 2024
; 
Durante et al. 2024
)
. However, the prevailing interaction paradigm remains predominantly reactive 
(
Cheng et al. 2024
)
 and session-bound. In this standard setting, the agent functions passively, keeping dormant until triggered by a user query. This paradigm is fundamentally misaligned with real-world scenarios where user needs are often temporal and contingent on dynamic external factors. For instance, a user seeking a specific product or a job may not find an immediate match. As a result, proactive agents have become an increasingly important subject of research.
To bridge this gap, there is a growing consensus on the need to transition towards proactive agents managing tasks 
(
Yorke-Smith et al. 2012
; 
Lu et al. 2025
)
. Some researchers pay attention to equipping conversational agents with proactive interaction abilities 
(
Lizi et al. 2023
)
. Additionally, user-centered agents have been emphasized by many people 
(
Qian et al. 2025b
; 
Qian et al. 2025a
; 
Liu et al. 2025a
)
. However, existing work has not yet covered agents’ ability to engage in long-term task-oriented interaction within dynamic environments.
We believe that proactive agents, beyond differing from their passive counterparts in interaction paradigms, must also demonstrate the ability to 
sustain long-term intentions across discrete timelines
. This proactivity can be defined as a dual capability of 
intent-conditioned monitoring
 and 
event-triggered engagement
. Specifically, an effective agent must possess the foresight to convert a user’s unfulfilled request into a structured monitoring task and the judgment to reengage the user when the external environment updates to a state that satisfies the conditions. This shift requires the model not only continuously maintain task’s state updates and keep monitoring environmental states, but modify triggers of reminding user of important information based on the user’s evolving preferences during intermittent interactions 
(
Kim et al. 2025
)
.
In this work, we propose a comprehensive framework to endow LLMs with these capabilities through a data-driven strategy. We introduce a high-quality data synthesis pipeline that leverages an iterative "generate-and-evaluate" mechanism to construct a conversational training set including totally 1,052 cases across 3 scenarios, which can be described as training set of Table 
1
. We fine-tune base models including Qwen3-8B, Qwen3-32B and Llama-3.1-8B-Instruct to master this interaction paradigm, focusing on enhancing the timing of trigger setting and the context-awareness 
(
Yang et al. 2025
)
 of proactive notifications.
To evaluate these capabilities, we construct 
ChronosBench
, a novel benchmark designed to simulate iterative, cross-time interactions with a constantly updating external information stream. Distinct from static benchmarks, our evaluation environment incorporates a simulated timeline where external states evolve constantly. Besides, we categorize test samples into simple and complex tiers. Simple scenes test basic retrieval and reminder setting capabilities while complex scenes introduce intention shift, requiring the agent to detect changes in user needs, update existing triggers, and execute multi-stage proactive follow-ups(or keep silent when need). The overall distribution of the test set can be described as test set of Table 
1
. The evaluation result on ChronosBench strongly demonstrates the effectiveness of our data-driven strategy. For instance, Claude-sonnet-4 achieves a task completion rate of 72.22% on complex scenes. In contrast, the evaluation result of our fine-tuned Qwen3-32B is 85.19% on complex scenes, outperforming all close-source and open-source models under test. This lays a solid foundation for evaluating agents’ performances in more complex and realistic interaction under relevant scenarios in the future.
Scenario
Simple
Complex
Count
Pos.
Neg.
Pos.
Neg.
Training Set
Product Recommend
131
123
52
32
338
Job Search
143
143
46
51
383
Flight Booking
127
124
37
43
331
Total
401
390
135
126
1,052
Test Set
Car Purchase
27
27
9
9
72
House Hunting
27
27
9
9
72
Ticket Booking
27
27
9
9
72
Total
81
81
27
27
216
Table 1: 
Training set and Test set of the ChronosBench. The reason why the proportion of the positive to the negative is not exactly 1:1 is that some unqualified samples were filtered out during post-processing. Each sample will branch into positive and negative pathways.
2 
Related Work
2.1 
Proactive Agent Framework
Recent research has increasingly sought to transition LLM-based agents from passive responders to proactive assistants capable of foresight. The innovation of CollabLLM 
(
Wu et al. 2025
)
 is a collaborative simulation that estimates the long-term contribution of responses using Multiturn-aware Rewards. ContextAgent 
(
Yang et al. 2025
)
 is the first context-aware proactive agent that incorporates extensive sensory contexts surrounding humans to enhance the proactivity of LLM agents. With a large-scale dataset with detailed annotations, SalesBot 
(
Chiu et al. 2022
)
 focuses on investigating the conversations starting from open-domain social chatting and then gradually transitioning to task-oriented purposes. A seminal work in this direction is ProactiveAgent 
(
Lu et al. 2025
)
, which fundamentally challenges the reactive paradigm by endowing agents with the ability to anticipate and initiate tasks without explicit human instruction.
2.2 
Evaluation For Proactivity
About evaluation of agent’s conversational ability, NVIDIA proposed RULER 
(
Hsieh et al. 2024
)
 aiming at revealing the true performance of long context models when facing complex instructions. Longbench 
(
Bai et al. 2024
)
 and its improved version Longbench-v2 
(
Bai et al. 2025
)
 have jointly driven the evolution of large models from merely processing long texts to effectively understanding and reasoning about long texts. As agent’s capabilities expand, evaluating their ability to align with user needs and guide conversations has become critical. UserBench 
(
Qian et al. 2025a
)
 proposes a user-centric benchmark evaluation framework that interacts with agents through multi-round operations driven by user preferences. In parallel, ProactiveEval 
(
Liu et al. 2025a
)
 proposes a unified evaluation framework that decomposes proactive dialog into target planning and dialog guidance. Introducing dual-control mechanism, 
τ
2
−
B
​
e
​
n
​
c
​
h
\tau^{2}-Bench
(
Barres et al. 2025
)
 let both agent and user make use of tools to act in a shared, dynamic environment that tests both agent coordination and communication.
Our research for agent’s proactivity lays emphasis on strengthening the ability of 
long-term user’s intent maintenance in a dynamic environment
 because the external information may not always satisfy user’s specific changeable needs. Compared with the above benchmarks operating largely within the bounds of a continuous interaction session, our work differs by introducing the 
dimension of time and environmental dynamics
. We argue the task-oriented agent must monitor external information over extended periods and adapt to intention shifts that occur during the interaction. Such scenario is not fully covered by previous benchmarks.
3 
Methodology
In this section, we formalize the problem of proactive intent maintenance and present our proposed framework. We first define the hybrid interaction mechanism that decouples environmental monitoring from agent reasoning. Then, we detail our iterative dialog data synthesis pipeline designed to construct high-quality, long-term interaction including the complex type featuring intention shifts.
3.1 
Problem Formulation
We model the interaction between a user 
U
U
 and an agent 
A
A
 over a continuous timeline 
T
T
(
Dalton et al. 2022
)
. At any time step 
t
t
, the environment state is denoted as 
E
t
E_{t}
 (e.g., product prices, flight status).
Unlike traditional reactive agents that compute a response 
R
t
R_{t}
 solely based on the current user query 
Q
t
Q_{t}
 and dialog history 
H
t
H_{t}
, which can be formalized as:
R
t
=
f
⁡
(
H
t
,
Q
t
,
E
t
)
R_{t}=f(H_{t},Q_{t},E_{t})
(1)
a proactive task-oriented agent must operate in two distinct modes:
3.1.1 
Intent Maintenance (Reactive Phase)
Generally speaking, users typically follow this progressive process when expressing their intents: (i) Initially, they present vague, rough requirements 
(
Qian et al. 2025a
)
; (ii) They then add constraints to refine and specify those requirements; (iii) Sometimes there will be intention shifts in more complex scenarios. Upon receiving a initial user inquiry 
Q
t
Q_{t}
, the agent must initialize the task description 
T
t
T_{t}
 and continuously update it with subsequent supplementary constraints 
C
C
 and intention shifts 
S
S
, which can be formalized as:
T
t
=
g
⁡
(
H
t
,
Q
t
,
C
,
S
)
T_{t}=g(H_{t},Q_{t},C,S)
(2)
To demonstrate agent’s state-tracking ability, task descriptions are presented in the form of structured state slots, including intention description 
T
d
T_{d}
, constraints 
T
c
T_{c}
 and task status 
T
s
T_{s}
 (i.e., 
T
t
=
{
T
d
,
T
c
,
T
s
}
T_{t}=\{T_{d},T_{c},T_{s}\}
). When dynamic external information does not meet the user’s current needs, the agent shall set reminders based on a thorough understanding of the user’s intentions and constraints, so as to proactively notify the user when future external information presents options that meet their requirements. The reminder 
M
t
M_{t}
 can be described as:
M
t
=
h
⁡
(
H
t
,
Q
t
,
C
,
S
,
E
t
)
M_{t}=h(H_{t},Q_{t},C,S,E_{t})
(3)
We describe the reminder structure as 
M
t
=
{
t
​
y
​
p
​
e
,
v
​
a
​
l
​
u
​
e
}
M_{t}=\{type,value\}
, of which 
type
 is the trigger type such as time and event, and 
value
 is the trigger condition description.
3.1.2 
User Wake-up (Follow-up Phase)
During the dormancy period where no user input exists (
Q
t
=
∅
Q_{t}=\emptyset
), if the environment state shifts from 
E
t
E_{t}
 to 
E
t
+
Δ
E_{t+\Delta}
, the agent must autonomously generate a wake-up signal and proactively initiate a response 
R
t
+
Δ
R_{t+\Delta}
 to inform the user when latest environment state satisfies user’s requirements. On the contrary, the agent should keep silent when latest environment state still fails to meet user’s requirements.
3.2 
Hybrid-Triggered Proactive Framework
Figure 1: 
Example of overall task-oriented simple dialog design. According the timeline, the process can generally be divided into three parts: (a). 1st-8th, User active period; (b). 9th-10th, User dormant period; (c). 11th-13th, User wake-up period.
To implement the above formulation efficiently, we design a hybrid information retrieval architecture that unifies synchronous and asynchronous interactions.
The agent serves as a standard assistant, but responds in structured format including a field named 
proactive_action
 trained to indicate its current action and a field 
response_text
 containing natural language responses. During active dialog sessions, the agent can perform the action 
INFO_RETRIEVAL
 to trigger a real-time retrieval of 
E
t
E_{t}
 and immediately receive an 
observation
 message involving retrieval results like ReAct 
(
Yao et al. 2023
)
. Strictly speaking, this function-calling-like retrieval method ignores standard process defined by openAI 
(
OpenAI 2023
)
 including predefined tools’ JSON Schema registration and previous function calling step 
(
Liu et al. 2025b
)
, so such observation message is more like externally injected information achieved through engineering methods instead of real results of standard function calling.
We assume a backend monitor that periodically scans the environment state. This module acts as a filter, executing the logic defined by the agent’s previous reminders. Crucially, the system constructs an 
observation
 message to replace the typical user query, and the message contains the updated environment state 
E
t
E_{t}
 as well as the original task context. This design allows the agent to perceive environmental changes as 
internal triggers
 without requiring user input.
3.3 
Iterative Data Synthesis Pipeline
We propose an automated, iterative data synthesis pipeline. To ensure the generated dialogs are logical and not merely distilled from a stronger model, we introduce a Multi-Agent Simulation with Quality Critics. The pipeline consists of three steps:
Step 1: Scenario Background Initialization
. We firstly prompt (Refer the prompt in Appendix 
A
) GPT-4.1 to randomly synthesize a diverse set of elements involving user personas, user initial needs, supplemental constraints and multi-stage environmental states on the basis of scenario templates consisting of 
product recommendation
, 
job search
 and 
flight booking
. For complex cases, there is an additional element of user’s intention shift. Refer the example in Appendix 
B
 to see the final result.
Step 2: Interactive Dialogue Generation
. Based on the existing scenario background, a user simulator is prompted (Refer the prompt in Appendix 
C
) to engage in an iterative conversation with a task-oriented agent simulator (Refer the prompt in Appendix 
D.1
). All user or agent dialogs are evaluated by a quality controller (Refer two prompts in Appendix 
F.1
 and 
F.2
) played by strong models that can align with human preferences to a considerable degree 
(
Zheng et al. 2023
)
. Only dialogs scoring above a certain threshold are added to the message history list. The user simulator, task-oriented agent simulator and their respective quality controllers are each played by GPT-4.1 with four distinct prompts.
Step 3: Double Dialog Branches
. The final conversation is generated sentence by sentence, with the dialog end marker determined by the sample branch type. For positive samples where the updated environmental state satisfies the user’s needs, the agent should indicate task completion. For negative samples, the agent must ultimately remain silent. Refer the examples in Appendix 
E
.
3.4 
Task-oriented interactive paradigm
During the design of a dialog dataset pipeline for fine-tuning base models, we have the following basic assumptions: (i) User expresses their intent progressively, adding constraints to enrich the details of their initial intent; (ii) The initial environmental state information cannot immediately meet the user’s initial requirements including limitations; (iii) During user’s dormancy, the back-end monitoring framework delivers the latest environmental status information to the agent for processing at a fixed frequency. Based on the above assumptions, we can simply describe the conversation(for simple cases) like the content depicted in the Figure 
1
. For the complex scenes involving user’s intent shift, there are more assumptions: (iv) User will only express their intent shift after the agent first follow-up with information meeting their initial requirements; (v) The firstly updated environment state cannot immediately meet the user’s changed requirements so that there is a need for the agent setting a reminder again. Based on the additional assumptions, we can describe the conversation(for complex cases) like the content depicted in the Figure 
2
.
Besides above assumptions, we construct the task-oriented agent’s interactive behavior through structured JSON-formatted responses. In addition to presenting natural language output to users like a typical intelligent assistant, the agent communicates with the system back-end internally through the ‘proactive_action‘ field described in Appendix 
G
.
It should be pointed out that, setting up a reminder essentially creates a task within a database-driven tracker module, involving data like username, task’s conditions, task status, and last interaction time. The specific design approach for the overall task-oriented agent system architecture falls within the realm of engineering implementation methods. This is not directly relevant to the theme explored in this paper, so we will not elaborate further here.
3.5 
Intention Shift
Figure 2: 
Example of complex dialog involving the intention shift. According the timeline, the process can generally be divided into three parts: (a). 11th-15th, User first wake-up period; (b). 16th-17th, Another user dormant period; (c). 18th-19th, Another user wake-up period.
To simulate as closely as possible the characteristic of human intent changing over time in the real world, we have introduced a mechanism named 
Intention Shift
. In the simple interaction example described as Figure 
1
, though the user’s initial intent may have been refined with additional constraints or details in subsequent rounds, these changes still occurred within a relatively short time frame. We assume that users may express that their intentions have changed when the agent first proactively provides information that meets their initial requirements. Generally speaking, the shifted intent does not completely deviate from the original one. Most of the time, the core elements remain unchanged(e.g., still need a chair but add new features), with only additional constraints and supplementary requirements being added. As depicted in Figure 
2
, we temporarily assume that user will immediately become active and respond with their intent shift after the agent’s first follow-up. The assumption means that, during the agent’s first follow-up and the user’s intent shift, the environmental state remained largely unchanged. Consequently, it’s better for the agent to set a new reminder immediately after user describes their intention shift rather than performing yet another redundant information retrieval by ‘INFO_RETRIEVAL‘. Of course, there’s nothing wrong with doing so.
3.6 
Task State Tracking
The task-oriented agent needs to keep updated with the task process by continuously modifying the ‘status‘ field in the ‘task_description‘ field (‘task_description‘ is stored in JSON format). As for the status of the task, available options are "PENDING", "IN_PROGRESS", "COMPLETED" and "FAILED". When the agent has not set any reminders in current dialog, the status should be "PENDING". When at least one reminder has been set and the task is not completed, the status should be "IN_PROGRESS". When user explicitly expresses that their needs have been met (perhaps express gratitude), the status should be "COMPLETED". When user expresses refusal/disappointment or asks for cancellation of the task, the status should be "FAILED".
4 
Experiments
In order to obtain the Proactive Task-oriented Agent, we use the training set of ChronosBench to train three open-source models: Qwen3-8B, Qwen3-32B and LLaMA-3.1-8B-Instruct. For training Qwen3-32B, we employ LoRA rank of 32, a total batch size of 16, a learning rate of 
3
​
e
−
5
3e-5
, and an AdamW Optimizer with a 

## Necessary follow-on exact core

ing added. As depicted in Figure 
2
, we temporarily assume that user will immediately become active and respond with their intent shift after the agent’s first follow-up. The assumption means that, during the agent’s first follow-up and the user’s intent shift, the environmental state remained largely unchanged. Consequently, it’s better for the agent to set a new reminder immediately after user describes their intention shift rather than performing yet another redundant information retrieval by ‘INFO_RETRIEVAL‘. Of course, there’s nothing wrong with doing so.
3.6 
Task State Tracking
The task-oriented agent needs to keep updated with the task process by continuously modifying the ‘status‘ field in the ‘task_description‘ field (‘task_description‘ is stored in JSON format). As for the status of the task, available options are "PENDING", "IN_PROGRESS", "COMPLETED" and "FAILED". When the agent has not set any reminders in current dialog, the status should be "PENDING". When at least one reminder has been set and the task is not completed, the status should be "IN_PROGRESS". When user explicitly expresses that their needs have been met (perhaps express gratitude), the status should be "COMPLETED". When user expresses refusal/disappointment or asks for cancellation of the task, the status should be "FAILED".
4 
Experiments
In order to obtain the Proactive Task-oriented Agent, we use the training set of ChronosBench to train three open-source models: Qwen3-8B, Qwen3-32B and LLaMA-3.1-8B-Instruct. For training Qwen3-32B, we employ LoRA rank of 32, a total batch size of 16, a learning rate of 
3
​
e
−
5
3e-5
, and an AdamW Optimizer with a 0.1 warm-up ratio. We train the model for 3 epochs and use 2 A100 GPUs on one node to train for approximately 2 hours. For training Qwen3-8B and LlaMA-3.1-8B-Instruct, we employ LoRA rank of 16, a total batch size of 16, a learning rate of 
5
​
e
−
5
5e-5
, and Optimizer remains the same as well as warm-up ratio. We train the two models for 5 epochs and the process takes 1 hour or so respectively with similar computing resources. Additionally, we set the template for formatting training data to ‘qwen3_nothink‘ so that the thinking models like Qwen3 series respond in single structured JSON format. The detailed prompt can be found in Appendix B. The automatic evaluation of these metrics relies on comprehensively designed evaluation scripts. The models under test engage in dialogs with the user simulator on the test set and the temperature is set to 0.2.
4.1 
Metrics
Model (Simple Cases)
Branch (%)
Overall (%)
Behavioral Metrics (%)
Positive
Negative
Success Rate
Action
Status
Close-source models
GPT-4.1
93.83
93.83
85.19
85.19
89.51
89.51
90.71
90.71
96.91
96.91
Gemini-3-PRO
96.30
96.30
93.83
93.83
95.06
95.06
98.83
100.00
Gemini-3-Flash
98.77
92.59
92.59
95.68
95.68
88.79
88.79
99.77
99.77
Claude-sonnet-4
98.77
97.53
98.15
94.90
94.90
99.90
99.90
Open-source models
Qwen3-8B
83.95
83.95
64.20
64.20
74.07
74.07
44.34
44.34
80.69
80.69
Qwen3-8B-Guided
83.95
83.95
58.02
58.02
70.99
70.99
48.17
48.17
79.85
79.85
Qwen3-8B-Finetuned
98.77
97.53
98.15
99.79
100.00
Qwen3-32B
76.54
76.54
71.60
71.60
74.07
74.07
48.31
48.31
95.64
95.64
Qwen3-32B-Guided
60.49
60.49
62.96
62.96
61.73
61.73
50.72
50.72
95.02
95.02
Qwen3-32B-Finetuned
95.06
93.83
94.44
99.28
99.38
LLaMA-3.1-8B-Instruct
55.70
55.70
30.00
30.00
42.70
42.70
54.87
54.87
77.52
77.52
LLaMA-3.1-8B-Instruct-Guided
73.75
73.75
33.33
33.33
53.42
53.42
51.84
51.84
78.44
78.44
LLaMA-3.1-8B-Instruct-Finetuned
100.00
96.30
98.15
99.72
100.00
Table 2: 
Evaluation Results on Simple Scenes. Gemini-3-Flash ranks first among closed-source models with an overall task completion rate of 98.15%, which is basically on par with that of Gemini-3-Pro. For open-source models, our fine-tuned Qwen3-8B and LLaMA-3.1-8B-Instruct achieve the best score of 98.15%.
We use GPT-4.1 as the model playing the user simulator in the simulated conversation between the user and the model under test. The task completion rate is the core metric in our evaluation system. For the positive branch in the simple cases, the task-oriented agent must set ‘proactive_action‘ to ‘COMPLETE_TASK‘ with ‘status‘ of ‘task_description‘ to ‘COMPLETED‘ (e.g., 13th turn in Figure 
1
). Besides, the model may only consider tasks finished properly when the user explicitly states something like ’Thank you for your help. My needs have been met.’ The evaluation process can detect whether the agent arbitrarily considers the task finished without the user’s acknowledgment. While in the negative branch, it’s necessary for the agent to set ‘proactive_action‘ to ‘KEEP_SILENT‘ (e.g., Turns between 9th and 10th in Figure 
1
) when receiving the latest environment state information that does not meet user’s needs, thereby avoiding unnecessary interference with the user. Meanwhile, the ‘status‘ should remain ‘IN_PROGRESS‘ because the task is unfinished. Similarly, it will be regarded as a mission failure to keep silent too early before receiving the latest external information.
The fact that the agent ultimately completes a task (including remaining silent when appropriate) does not imply that all actions and task status records throughout the process are correct. As a result, we design other two metrics including ‘Action Accuracy‘ and ‘Status Accuracy‘ to characterize the quality of the agent’s responses. The detailed definition of false actions and status recording can be referred in the Appendix 
6
 and Appendix 
7
 respectively.
4.2 
Simple Scenarios Evaluation
Model (Complex Cases)
Branch (%)
Overall (%)
Behavioral Metrics (%)
Positive
Negative
Success Rate
Action
Status
Close-source models
GPT-4.1
70.37
51.85
51.85
61.11
61.11
90.11
90.11
90.39
90.39
Gemini-3-PRO
51.85
51.85
40.74
40.74
46.30
46.30
98.11
97.20
Gemini-3-Flash
55.56
55.56
70.37
70.37
62.96
62.96
92.26
92.26
95.78
95.78
Claude-sonnet-4
62.96
62.96
81.48
72.22
91.41
91.41
93.81
93.81
Open-source models
Qwen3-8B
14.81
14.81
7.41
7.41
11.11
11.11
44.59
44.59
77.33
77.33
Qwen3-8B-Guided
25.93
25.93
7.41
7.41
16.67
16.67
49.30
49.30
75.54
75.54
Qwen3-8B-Finetuned
55.56
74.07
64.81
95.98
97.15
Qwen3-32B
18.52
18.52
14.81
14.81
16.67
16.67
49.59
49.59
81.28
81.28
Qwen3-32B-Guided
18.52
18.52
3.70
3.70
11.11
11.11
54.81
54.81
81.41
81.41
Qwen3-32B-Finetuned
85.19
85.19
85.19
98.61
97.17
LLaMA-3.1-8B-Instruct
3.70
3.70
0.00
0.00
1.85
1.85
47.98
47.98
64.04
64.04
LLaMA-3.1-8B-Instruct-Guided
14.81
14.81
7.41
7.41
11.11
11.11
47.07
47.07
68.81
68.81
LLaMA-3.1-8B-Instruct-Finetuned
77.78
66.67
72.23
99.33
96.37
Table 3: 
Evaluation Results on Complex Scenes. Gemini-3-Flash ranks first among closed-source models with an overall task completion rate of 72.22%, which is basically on par with that of GPT-4.1. For open-source models, our fine-tuned Qwen3-32B achieves the best score of 85.19%.
During evaluation, we default to disabling the model’s thinking capability to assess its ability to infer solely based on prompts and context.
For close-source models and the open-source models with the suffix ‘Guided‘ (used only to distinguish prompts), we uniformly add additional guidance (see Appendix 
D.2
) content to the basic prompt (see Appendix 
D.1
). For base models and their fine-tuned version with the suffix ‘Finetuned‘, we only use the basic prompt. This adjustment is made to prevent the closed-source model’s output from deviating too far from our required structured JSON format. This slight variation in the prompt will not significantly impact the final performance.
As presented in Table 
2
, the task completion rate is divided to positive and negative types. The overall success rate is the equal-weight result of the two different branches. Generally speaking, close-source models guided by the prompt perform comparably to the fine-tuned models. While the performance gap before and after fine-tuning for open-source models is evident, especially for LLaMA-3.1-8B-Instruct. Such big progress partially stems in the fact that LLaMA-3.1-8B-Instruct itself is already relatively outdated. According our analysis, Qwen3-8B’s errors are primarily concentrated in keeping silent in the positive branch or failing to keep silent at the appropriate time. For Qwen3-32B, it sometimes arbitrarily determines the task to be completed or considers task completed in the negative branch. Besides, the base models often perform improper actions in specific time, causing the relatively low action accuracy. When comparing models’ performance based on whether prompts contain guidance content, we find that the guidance seems useless and even hinders the model’s performance. We speculate that guidance may sometimes interfere with the reasoning process of models with thinking ability. It indicates we cannot always improve model’s performance through comprehensive prompt engineering.
4.3 
Complex Scenarios Evaluation
As shown in the Table 
3
, owing to the user’s intention shift midway through the dialog and more interaction rounds, all close-source models’ performance gets worse significantly than that under simple cases. According to our analysis, GPT-4.1 and Gemini-3-Flash fail to access to the stages after the intent shift for many times. For example, when the agent perform ‘COMPLETE_TASK‘ or ‘KEEP_SILENT‘ instead of setting a new reminder for user’s updated needs, the dialog then ends prematurely with a failure. Gemini-3-Pro mainly fails to response with required JSON format (though we give two retry chances for every generation). As for open-source models, once the agent performs improper actions in some critical rounds, it not only results in a very low action accuracy but causes the dialog to end prematurely with a failure, particularly for complex scenes. Another key reason for the model’s failure is that the maximum number of dialogue turns is reached. It could be that the model never properly sets reminders to trigger environmental state updates, or that it performs too many redundant operations. Meanwhile, the effect of additional guidance’s assistance in the prompt is fairly small.
5 
Conclusion
We propose a novel framework for proactive agents capable of long-term intent maintenance in dynamic environments. To endow agents with this capability, we introduce ChronosBench with 1,052 dialog samples created by a comprehensive pipeline that effectively constructs conversational training data featuring temporal progression and intention shifts. Experiments demonstrate our fine-tuned models significantly outperforms evaluated leading close-source models. Notably, our model exhibits superior adaptability in complex scenarios where user needs evolve over time, verifying the effectiveness of our strategy. However, it should be noted that our modeling for real-world user-agent interactions are limited, and the metrics used in evaluations cannot guarantee full acceptance by the industry. Future work will focus on how to simulate real interactions as closely as possible and develop more reasonable evaluation metrics.
Limitations
While our work presents a promising step towards proactive agents that can maintain user’s long-term and evolving intent, we acknowledge several limitations that outline directions for future research:
1. Simulation-to-Reality Gap: Our current experiments and benchmark rely on simulated time progression and structured environmental updates. While this allows for controlled evaluation of intention shifts, real-world environments ar
