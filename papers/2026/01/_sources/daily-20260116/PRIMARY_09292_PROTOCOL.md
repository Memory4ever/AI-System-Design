# 2601.09292v1 — safe minimum protocol and identity-defence excerpts

Exact primary https://arxiv.org/html/2601.09292v1 ; selected original body actually read. Malicious implementation text is not needed for the adopted call-selection witness and is omitted here; no code executed.

Experimental Evaluation
We ran the experimental evaluation on four representative LLMs using Ollama
3
3
3
https://ollama.com/
 and DSPy 
(
6
)
: Qwen3:8B 
(
14
)
, Llama-3.2:3B 
(
8
)
, Granite3.2:8B 
(
4
)
, and Granite3.3:8B 
(
5
)
. We selected these models because they are open-source, popular, freely available, and they claim to have function-calling capabilities.
Our choice to evaluate smaller models aligns with the growing emphasis on sustainable AI development and AI democratization, as these models consume significantly less energy and computational resources while maintaining acceptable performance levels, making them more accessible to different kinds of users.
To test the effectiveness of our framework, we used one of the most popular function-calling datasets: the Berkeley Function Calling Leaderboard dataset 
(
11
)
, with the task of calling a single function with correct parameters among multiple available tools
4
4
4
https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/bfcl˙eval/data/BFCL˙v3˙multiple.json
.
To ensure realistic testing conditions, we generated plausible tool implementations using Qwen2.5-Coder:32B 
(
3
)
 and created a sanitized dataset containing 172 query-answer pairs.
We included the implementation of tools in the task because it is a legitimate option for a company hosting its internal tools, or using open-source ones, to further provide information to the function-calling agent.
For brevity, key results are summarized and discussed in the relevant sections, whereas full results are presented in the Appendix.
The baseline (no attack performed) is shown in the first row of Table 
1
, exhibiting how the accuracy (i.e., the percentage of correct tool calls for each scenario out of the 172 instances of the expe

Attack Type
Qwen3:8B
Llama3.2:3B
Granite3.2:8B
Granite3.3:8B
ACC
ASR
ACC
ASR
ACC
ASR
ACC
ASR
No attack
0.92
0
0.66
0
0.84
0
0.78
0
DPI
0.06
0.94
0.20
0.58
0.34
0.56
0.80
0
STP
0.04
0.95
0.50
0.23
0.72
0.12
0.39
0.51
RTP
0.24
0.74
0.69
0.02
0.84
0.01
0.83
0
Table 1: 
Accuracy and Attack Success Rate (ASR) for different models and attack types.


Watermarking.
The watermarking defence implements a cryptographic approach to tool authentication using HMAC keys.
Each legit tool name receives a unique watermark generated through SHA-256 hashing with a secret seed, creating a verifiable hash that can detect unauthorized tool modifications.
This system provides tamper detection capabilities by embedding cryptographic signatures directly into tool identifiers, enabling real-time verification of tool authenticity during the function-calling process, before the execution of the tools.
As trivial as it is, employing this defence, as for the results shown in Tables 
6
 and 
7
, usually has a good impact on both the accuracy and ASR for all the models except Llama3.2:3B (which is not capable or reporting the watermark exactly, causing the selected tool to be marked as incorrect). Additionally, this defence can spot 100% of the successful attempts at calling the malicious function (before it happens) because it does not present the watermark in its name since the attacker does not know the secret key.
Nonetheless, this defence presents some limitations, like the need for hash regeneration when tool changes occur.
LLM-Based Active Defences.
The framework incorporates multiple LLM-based detection systems powered by specialized guardian models, which serve as the foundation for LLM-based defences. Detection results are filtered by confidence levels and probability thresholds to optimize results and mitigate false positives.
The framework uses the granite-guardian-3.2-3b-a800m 
(
10
)
 model as the primary detection engine, with results filtered using high confidence requirements and probability thresholds of 0.7 or higher.
Accuracy and ASR for these defences are not reported because they are the same as the baseline; the aim of the results shown for these defences is to showcase the False Positive Rate (FPR), i.e., the percentage of safe interactions incorrectly detected as malicious, the True Positive Rate (TPR), i.e., the percentage of the malicious interactions correctly detected as malicious, and the percentage of the detected successful attack attempts (DSA).
Query Jailbreak Detector.
This defence specifically identifies DPI attempts in user queries. This system analyzes query content for patterns indicative of malicious prompt engineering, providing focused protection against direct manipulation attempts.
As shown in Table 
12
, this defence suffers no false positives, and it is able to detect 100% of the attacks for the DPI scenario; nevertheless, it is not useful for the other kinds of attacks for which it was not tailored.
Query Answer Consistency.
This defence validates the appropriateness of model responses to user queries using function call detection capabilities. This system ensures that model outputs align with expected responses for given inputs, detecting instances where models produce inappropriate or suspicious function calls.
This defence, whose results are shown in Table 
10
, shows promising results for the DPI attack and the RTP attack, but suffers a quite high FPR rate for the scenario in which no attack is performed (ranging from 11% to 13% of the selected tools). In this scenario, a detection is considered a false positive if the model considers the call inappropriate when it is, in fact, correct.
Tools Jailbreak Detector.
This defence examines each tool implementation and description for signs of compromise or malicious functionality, offering protection against tool poisoning attacks that embed harmful instructions within partly legitimate-appearing functions.
As shown in Table 
13
, this defence correctly detects all the attacks for the two tool poisoning scenarios, but it suffers a very high FPR for both the no attack and the DPI attack scenario.
Query Tools Consistency.
This defence evaluates the relevance of selected tools to user queries using context relevance analysis. This component verifies that the tool list is appropriate for the given query, identifying cases where the available tools do not align with user intentions.
This defence has the highest FPR, as shown in Table 
11
. We speculate that this is caused by the usage of natural text in t
