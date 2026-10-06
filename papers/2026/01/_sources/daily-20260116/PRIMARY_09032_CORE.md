# 2601.09032v1 primary core

URL https://arxiv.org/html/2601.09032v1
Exact version core read; normalized HTML original text, not summary.


The Hierarchy of Agentic Capabilities: Evaluating Frontier Models on Realistic RL Environments
Title:
Content selection saved. Describe the issue below:
Description:
arXiv is now an independent nonprofit!
Learn more
×
    License: CC BY 4.0
arXiv:2601.09032v1 [cs.AI] 13 Jan 2026
The Hierarchy of Agentic Capabilities: 
Evaluating Frontier Models on Realistic RL Environments
Logan Ritchie
Thanks: 
Correspondence to: 
loganritchie@surgehq.ai
Sushant Mehta
Nick Heiner
Mason Yu
Edwin Chen
Affiliation: 
[1ex]
Surge AI
Abstract
The advancement of large language model (LLM) based agents has shifted AI evaluation from single-turn response assessment to multi-step task completion in interactive environments. We present an empirical study evaluating frontier AI models on 150 workplace tasks within a realistic e-commerce RL environment from Surge. Our analysis reveals an empirically-derived 
hierarchy of agentic capabilities
 that models must master for real-world deployment: (1) tool use, (2) planning and goal formation, (3) adaptability, (4) groundedness, and (5) common-sense reasoning. Even the best-performing models fail approximately 40% of the tasks, with failures clustering predictably along this hierarchy. Weaker models struggle with fundamental tool use and planning, whereas stronger models primarily fail on tasks requiring contextual inference beyond explicit instructions. We introduce a task-centric design methodology for RL environments that emphasizes diversity and domain expert contributions, provide detailed failure analysis, and discuss implications for agent development. Our findings suggest that while current frontier models can demonstrate coherent multi-step behavior, substantial capability gaps remain before achieving human-level task completion in realistic workplace settings.
1 
Introduction
The year 2025 has witnessed the transition of AI systems from conversational assistants to more autonomous agents capable of executing actions in real-world environments 
(
Xi et al. 2023
; 
Wang et al. 2024
)
. This evolution raises an important question: 
how much (economically) useful work can AI agents actually perform?
Addressing this question requires evaluation paradigms that go beyond traditional benchmarks. Although assessments such as MMLU 
(
Hendrycks et al. 2021
)
 and HellaSwag 
(
Zellers et al. 2019
)
 measure static knowledge and reasoning, they fail to capture the dynamic, multi-step nature of real-world tasks. Similarly, single-turn instruction-following evaluations 
(
Zhou et al. 2023
)
 cannot measure an agent’s ability to recover from errors, adapt to unexpected situations, or maintain coherent behavior across extended interactions.
This gap has motivated interactive evaluation environments where AI agents act through tool use and are assessed on realistic multi-step tasks 
(
Zhou et al. 2024
; 
Xie et al. 2024
; 
Mialon et al. 2024
; 
Xu et al. 2024
)
. These environments enable evaluations of agentic capabilities that static benchmarks cannot capture. Recent empirical studies of production agents reveal that despite widespread deployment in various industries, reliability remains the primary challenge, with practitioners deliberately constraining agent autonomy to maintain operational stability 
(
Pan et al. 2025
)
.
We present an empirical study of frontier AI models evaluated within an RL environment 
Corecraft
, Inc., simulating an online retailer of high-performance PC components and custom builds. Models assume the role of customer support agents, performing tasks ranging from simple database queries to complex multi-step workflows requiring reasoning about system interactions.
Our contributions are:
1.
Empirical RL environment evaluation
: We evaluated frontier models on 150 workplace tasks, revealing substantial performance gaps even among state-of-the-art models.
2.
Hierarchy of agentic capabilities
: Through systematic failure analysis, we identify five hierarchical capability levels: tool use, planning, adaptability, groundedness, and common-sense reasoning. Model failures cluster predictably along this hierarchy.
3.
Task-centric RL environment design
: We describe a principled approach to environment construction that emphasizes task diversity, contributions from real domain experts, and a modular architecture that supports both training and evaluation.
4.
Detailed failure taxonomy
: We provide concrete examples of failure modes at each hierarchy level, offering useful insights for researchers and model developers.
Our findings reveal that even the best-performing models fail approximately 40% of tasks. More importantly, the 
nature
 of failures differs systematically: weaker models fail at basic tool use and planning, while stronger models struggle primarily with common-sense reasoning requiring contextual inference beyond explicit instructions. These results contextualize some recent findings that production agents typically execute at most ten steps before requiring human intervention 
(
Pan et al. 2025
)
, suggesting that current deployment constraints reflect genuine capability limitations.
2 
Related Work
2.1 
Agent Benchmarks and Evaluation
Agent evaluation has evolved substantially from early web interaction benchmarks to comprehensive real-world assessments. MiniWoB++ 
(
Liu et al. 2018
)
 established foundational paradigms for the evaluation of web-based agents with simplified browser tasks. 
WebArena
(
Zhou et al. 2024
)
 introduced self-hosted functional websites that incorporate tasks across e-commerce, social forums, and collaborative software. 
VisualWebArena
(
Koh et al. 2024
)
 extended this to multimodal settings with tasks requiring visual comprehension.
OSWorld
(
Xie et al. 2024
)
 extended evaluation to full operating system interaction across Ubuntu, Windows, and macOS, with tasks that range from office productivity, system utilities, and creative applications. The benchmark identified GUI grounding and operational knowledge as primary failure modes.
The 
GAIA benchmark
(
Mialon et al. 2024
)
 took a different approach, designing questions conceptually simple for humans but challenging for AI, requiring real-world interaction, multi-modal reasoning, and web browsing.
For software engineering, 
SWE-bench
(
Jimenez et al. 2024
)
 evaluates agents on 2,294 real GitHub issues that require bug localization and patch generation. 
Terminal-Bench
(
Terminal-Bench Team 2025
)
 evaluates the capabilities of command-line agents in tasks that span scientific workflows, network configuration, cybersecurity, and data analysis, each running in isolated Docker environments.
τ
\tau
-bench
(
Yao et al. 2024a
)
 uses the pass@k reliability metric that measures the success rate over 
k
k
 independent trials rather than best-of-
k
k
 attempts, with the results surfacing considerable reliability concerns. The follow-up 
τ
2
\tau^{2}
-bench 
(
Barres et al. 2025
)
 extends the evaluation to dual-control environments where both the agent and the user can invoke tools.
Recent surveys 
(
Yehudai et al. 2025
; 
Mohammadi et al. 2025
)
 have proposed taxonomies organizing agent evaluation by objectives (behavior, capabilities, reliability, safety) and process (interaction modes, benchmarks, metrics). Our work complements these taxonomies by providing an empirically-derived capability hierarchy that explains 
why
 agents fail, not just 
whether
 they succeed.
2.2 
Production Agent Deployment
Although academic benchmarks provide controlled evaluation settings, understanding real-world agent deployment is equally important. 
Pan et al. 2025
 present the first large-scale systematic study of AI agents in production, surveying 306 practitioners and conducting 20 in-depth case studies in 26 domains. Their findings reveal that production agents are typically built using simple controllable approaches: 68% execute at most 10 steps before requiring human intervention, 70% rely on prompting off-the-shelf models instead of weight tuning, and 74% depend primarily on human evaluation. In particular, reliability remains the top development challenge, and practitioners deliberately constrain agent autonomy to maintain operational stability.
These production patterns provide an important context for our evaluation findings. The capability gaps we identify help explain why practitioners adopt bounded autonomy and extensive human oversight: current models have not yet achieved the reliability required for extended autonomous operation.
3 
Environment Design
3.1 
Design Philosophy
Effective evaluation environments for LLM agents should satisfy the following requirements: (1) a coherent world model that defines the setting, organizational relationships, and domain constraints; (2) realistic entities with authentic attributes, relationships, and behaviors; and (3) a functional tool system that allows agents to perceive and act within the environment.
We adopt a 
task-centric design philosophy
: tasks provide a useful training and evaluation signal, while entities and tools exist to support tasks. This principle has important implications for environment construction. Instead of solely maximizing the number of entities or tools, we optimize for realistic and challenging tasks, which in turn requires creating diverse and interconnected entities.
Complex real-world systems are not designed top-down, but evolve organically. We reflect this principle in our construction methodology: within a framework enforcing coherent relationships and properties, domain experts with professional experience populate environments with realistic entities and tasks. This organic growth approach yields data that approximates real-world complexity.
3.2 
Environment Architecture
Our evaluation infrastructure provides six core components:
1.
Sandboxed environment
: An isolated execution context for agent operation with controlled state management.
2.
Data layer
: Rich, interconnected entities representing realistic business operations (customers, products, orders, tickets, employees).
3.
Tool API
: Model Context Protocol (MCP) interface for structured agent-environment interaction.
4.
Task specification
: Prompts with defined success criteria that enable automated and human evaluation.
5.
Task management API
: Mechanisms for task assignment, completion signaling, and reward verification.
6.
Telemetry
: Complete trajectory logging including read/write actions and final outputs.
This architecture supports both training and evaluation, enabling the same environment to serve multiple research purposes.
3.3 
The 
Corecraft
 Environment
Our RL environment simulates 
Corecraft
, Inc., an online retailer of high-performance PC components. The world model encompasses:
•
Customer database
: Profiles including contact information, loyalty tiers (standard, gold, platinum), purchase history, and communication preferences.
•
Employee database
: Profiles including contact information, department, organization structure, and permissions.
•
Product catalog
: PC components with specifications, compatibility constraints, pricing, and inventory status.
•
Order management
: Orders with line items, shipping status, payment information, and fulfillment tracking.
•
Support ticketing
: Tickets with priority levels, categories, and resolution status.
The e-commerce domain was selected for several reasons: it represents economically significant work where agents could be deployed with minimal incremental effort; it spans a range of task difficulties from simple lookups to complex multi-system reasoning; and customer support specifically requires the bedrock capabilities needed for real-world agency regardless of domain specifics. Notably, recent surveys indicate that finance, technology, and corporate services represent the highest-concentration deployment domains for production agents 
(
Pan et al. 2025
)
, with customer support among the most common application areas.
The single world model supports multiple domain-specific task sets. While this study focuses on customer support, the same 
Corecraft
 infrastructure can support recruiting, marketing, and social media management tasks, enabling controlled comparisons across domains.
3.4 
Tool Interface
Agents interact through a tool system that implements the Model Context Protocol (MCP), providing structured access to search, retrieve, create, and update operations. Listing 
1
 presents a representative tool schema.
Listing 1: 
Representative MCP tool schema for customer search.
⬇
{
"
name
":
"
searchCustomers
",
"
description
":
"
Search
for
customers
matching
criteria
",
"
parameters
":
{
"
type
":
"
object
",
"
properties
":
{
"
name
":
{"
type
":
"
string
"},
"
email
":
{"
type
":
"
string
"},
"
loyaltyTier
":
{
"
type
":
"
array
",
"
items
":
{"
enum
":
["
standard
",
"
gold
",
"
platinum
"]}
},
"
limit
":
{"
type
":
"
integer
",
"
default
":
10}
}
}
}
3.5 
Task Design
Tasks span a range of complexity and interaction modes. Task difficulty derives from multiple sources: multi-hop reasoning requiring information synthesis across entities, domain-specific reasoning about product compatibility or policy application, and tool selection requiring judgment about which capabilities to invoke.
Corecraft now includes both 
copilot tasks
, where a human performs the task but requests agent assistance with specific subtasks, and 
fully autonomous tasks
, where the agent handles the workflow end-to-end. For the purposes of this evaluation, fully autonomous tasks were used.
Simple tasks require single-step operations:
“How many refunds were there in July 2025?”
Complex tasks require multi-step reasoning and cross-system coordination:
“A customer placed an order for a gaming build but I’m getting compatibility warnings. They ordered a ZentriCore Storm 6600X CPU with a SkyForge B550M Micro motherboard, plus 32GB of HyperVolt DDR5-5600. Can you help me figure out what’s wrong and suggest the cheapest fix?”
The tasks were designed by domain experts with customer support experience, ensuring realistic complexity and authentic edge cases that reflect actual workplace challenges.
4 
Experimental Setup
4.1 
Models Evaluated
We evaluated frontier and legacy AI models from the major AI laboratories. Our initial evaluation (November 2025) included nine models, and we subsequently evaluated newly released models in December 2025. The complete set includes the following.
•
OpenAI
: GPT-5.2 (high reasoning), GPT-5, GPT-4o
•
Anthropic
: Claude Opus 4.5, Claude Sonnet 4.5
•
Google
: Gemini 3 Pro, Gemini 2.5 Pro
•
Amazon
: Nova 2 Pro, Nova 1 Pro
•
Moonshot AI
: Kimi K2 Turbo
•
Alibaba
: Qwen3-Max
•
Mistral AI
: Mistral Medium 3.1
All models were accessed through their respective APIs with default parameters. Each received identical system prompts describing the environment, available tools, and task objectives.
4.2 
Evaluation Protocol
For each task, the models received: (1) a system prompt that establishes the role of the agent and the environment context, (2) available MCP tools with complete schemas, and (3) the description of the task as a user message. Models could execute unlimited tool calls until producing a final response. Complete trajectories were recorded.
4.3 
Evaluation Criteria
Successful completion of the task required: correct final answer or completion of the action, evaluated with an LLM judge using detailed human written rubrics. The failed trajectories were categorized by failure mode for capability analysis.
5 
Results
5.1 
Overall Performance
Figure 
1
 presents the primary results of our evaluation in December 2025, incorporating newly released models alongside previously evaluated ones. The following findings are immediately apparent:
0
10
20
30
40
50
60
70
Pass Rate (%)
GPT-5.2
GPT-5
Claude Opus 4.5
Claude Sonnet 4.5
Gemini 3 Pro
Nova 2 Pro
Kimi K2 Turbo
Qwen3-Max
Gemini 2.5 Pro
Mistral Medium
GPT-4o
Nova 1 Pro
Figure 1
: 
Task completion rates across frontier models on 150 workplace tasks (December 2025 Update). GPT-5.2 and Claude Opus 4.5 maintain the lead, while mid-tier models like Gemini 3 Pro and Nova 2 Pro demonstrate significant progress over previous generations.
Finding 1
: GPT-5.2 achieves the best performance, followed by Claude Opus 4.5 and Gemini 3 Pro. These three models substantially outperform others, with a gap exceeding 10 percentage points to the next tier.
Finding 2
: Even the best model (GPT-5.2) fails approximately 40% of tasks. At current capability levels, autonomous agents operating without human oversight carry a fairly significant risk of error.
5.2 
The Hierarchy of Agentic Capabilities
Analysis of failure trajectories revealed systematic patterns rather than random errors. Model failures clustered around specific capability levels, which we formalize as a 
hierarchy of agentic capabilities
 (Figure 
2
).
Level 1: Tool Use
Level 2: Planning & Goal Formation
Level 3: Adaptability
Level 4: Groundedness
Level 5: Common-Sense Reasoning
Chatbot with tool access
Weak agent
Weak agent
Strong agent
Human-level
Increasing Capability
Figure 2
: 
The hierarchy of agentic capabilities. Weaker models fail at basic tool use and planning; stronger models reach common-sense reasoning as their limiting factor.
The five levels are:
1.
Level 1: Tool Use
. Correct invocation of tools with appropriate arguments, parsing responses, and incorporating results into reasoning.
2.
Level 2: Planning and Goal Formation
. Decomposing complex tasks into subtasks, forming intermediate goals, and executing multi-step plans.
3.
Level 3: Adaptability
. Recognizing when initial approaches fail and dynamically adjusting strategies based on environmental feedback.
4.
Level 4: Groundedness
. Remaining anchored to the current context without hallucinating information or losing track of state across extended interactions.
5.
Level 5: Common-Sense Reasoning
. Making contextually appropriate inferences beyond explicit instructions and applying world knowledge to ambiguous situations.
This hierarchy is derived empirically, and in practice, model development is not strictly linear: these capabilities can overlap, reinforce each other, and evolve in parallel. Achieving high proficiency at a given level does not imply perfection; even frontier models can occasionally make errors in the use of basic tools. The hierarchy is best understood as a diagnostic framework for identifying where progress is solid and where foundational work remains.
5.3 
Qualitative Observations on Failure Patterns
Weaker models failed predominantly at Levels 1–2, struggling with tool use and planning. These models rarely encountered tasks where common-sense reasoning represented the primary bottleneck, because they failed earlier in the hierarchy.
Stronger models demonstrated robust performance at lower levels, with failures concentrating at Levels 4–5. These models have largely mastered basic tool use and planning, making contextual inference the main remaining challenge.
The mid-tier models exhibited distributed failure patterns. Substantial improvements in Nova 2 Pro over its predecessor suggests that targeted training can effectively address lower-level capability gaps.
6 
Qualitative Analysis
We present illustrative examples of failures at each capability level.
6.1 
Level 1: Tool Use Failures
The most fundamental capability is reliable tool invocation. Weaker models frequently failed to map the prompt information to the tool arguments correctly.
Task
: 
Find customers in the gold or platinum loyalty tiers who have outstanding high priority support tickets.
Nova 1 Pro invoked 
searchTickets
 with the customer ID set to “gold” rather than using the 
loyaltyTier
 parameter on 
searchCustomers
. This represents a fundamental failure to map task requirements to correct tool arguments.
GPT-4o correctly searched for customers in the gold and platinum tiers but made a basic mistake when searching for tickets: it passed “high” to the “status” argument rather than the explicitly available “priority” argument.
6.2 
Level 2: Planning Failures
Task
: 
There has been a product recall with the SkyForge X670E Pro. Please give me a bulleted list of customers who ordered this product in August 2025 with status fulfilled, paid, or pending.
The correct workflow requires: (1) using 
searchProducts
 to identify the product ID, (2) using 
searchOrders
 to find relevant orders, and (3) returning customer names.
Both Nova 1 Pro and Mistral Medium jumped directly to 
searchOrders
, passing the product name to “product_id”. They selected the single tool they believed would produce the final answer, then forced available data into whatever argument seemed plausible. They needed to consider all tools, determine which arguments matched the available information, and plan how to combine them.
6.3 
Level 3: Adaptability Failures
Adaptability sharply distinguished model performance tiers.
Task
: 
Hi, this is Penny Whitcomb, I am looking to upgrade my graphics card and usually go with Vortex Labs, Could you check whether the RX820L or RX780 would be compatible with parts from my last order and let me know my pricing for each?
Gemini 2.5 Flash, Gemini 2.5 Pro, and Qwen3-Max all made the correct sequence of tool calls. However, when searching for graphics cards, they encountered a problem: they searched with 
brand: "Vortex Labs"
 (with space), while the database stored it as 
"VortexLabs"
 (without space). When searches returned empty results, they took this at face value and reported that those graphics cards were not carried.
Claude Sonnet 4.5’s approach: Upon receiving empty results, Claude explicitly reasoned about the unexpected outcome and attempted alternative strategies, searching by product name patterns instead of relying solely on the brand filter. This adaptive behavior was consistently present in stronger models and absent in weaker ones.
Mid-tier models often executed a strict sequence of tool calls, but failed to adjust their p

## Necessary follow-on exact core

 with status fulfilled, paid, or pending.
The correct workflow requires: (1) using 
searchProducts
 to identify the product ID, (2) using 
searchOrders
 to find relevant orders, and (3) returning customer names.
Both Nova 1 Pro and Mistral Medium jumped directly to 
searchOrders
, passing the product name to “product_id”. They selected the single tool they believed would produce the final answer, then forced available data into whatever argument seemed plausible. They needed to consider all tools, determine which arguments matched the available information, and plan how to combine them.
6.3 
Level 3: Adaptability Failures
Adaptability sharply distinguished model performance tiers.
Task
: 
Hi, this is Penny Whitcomb, I am looking to upgrade my graphics card and usually go with Vortex Labs, Could you check whether the RX820L or RX780 would be compatible with parts from my last order and let me know my pricing for each?
Gemini 2.5 Flash, Gemini 2.5 Pro, and Qwen3-Max all made the correct sequence of tool calls. However, when searching for graphics cards, they encountered a problem: they searched with 
brand: "Vortex Labs"
 (with space), while the database stored it as 
"VortexLabs"
 (without space). When searches returned empty results, they took this at face value and reported that those graphics cards were not carried.
Claude Sonnet 4.5’s approach: Upon receiving empty results, Claude explicitly reasoned about the unexpected outcome and attempted alternative strategies, searching by product name patterns instead of relying solely on the brand filter. This adaptive behavior was consistently present in stronger models and absent in weaker ones.
Mid-tier models often executed a strict sequence of tool calls, but failed to adjust their plans on-the-fly when encountering unexpected results. Stronger models are capable of crafting and following multi-step plans, but also adjusting those plans mid-workflow to adapt to new information
6.4 
Level 4: Groundedness Failures
Groundedness refers to maintaining accurate state tracking and avoiding hallucination.
System prompt
: 
“The current date is September 15, 2025.”
Task
: 
Find orders from August 25–31, 2025.
Despite the explicit system prompt, Kimi K2 Turbo searched for orders from August 25–31, 
2024
. When providing the final response, the year was specified as 2025. This temporal confusion represents a failure of groundedness.
Claude Sonnet 4.5 also exhibited groundedness issues. In one instance, after finding a relevant order, Claude attempted to search for customer details using a fabricated email address. When this failed, Claude self-corrected using alternative parameters, demonstrating that adaptability can partially compensate for groundedness lapses.
In another example, Claude was asked to find support tickets and report priority levels. After correctly querying for “normal” priority tickets, Claude’s response incorrectly listed some as “high priority” while including them in the “normal” section. The response was inconsistent with the context retrieved and internally incoherent.
6.5 
Level 5: Common-Sense Reasoning Failures
Common-sense reasoning represents the main bottleneck for frontier models.
Task
: 
Identify which support tickets currently categorized as “other” should be reclassified as “returns.”
GPT-5 correctly retrieved all relevant tickets, including one stating:
“Hi, I’m really sorry but I’m going to need a refund. My son took my card without permission and made this purchase. I didn’t realize until the package showed up a few hours ago. I need the money ASAP.”
GPT-5 did 
not
 flag this for reclassification. The reasoning required: the customer requests a refund (could be return or cancelation), but “the package showed up”, which indicates that they received the item, making it unambiguously a return. GPT-5 gathered the right information, but did not connect the dots.
Another example
: A customer message stated:
“I’ve been getting frame drops when gaming so I want to upgrade my GPU. What’s the highest-end GPU I can get for under $900? Provide the price and all specifications. My name under my account should be set to Sarah Kim.”
GPT-5 interpreted this as an instruction to 
change
 the account name rather than recognizing it as an identification. A human would immediately infer that the customer is Sarah Kim, providing their name for lookup purposes. The model’s literal interpretation led to attempting an unnecessary account modification.
In a task that requires the identification of “gamer” customers based on purchasing patterns, GPT-5 searched through all August orders one day at a time and then individually queried the product details. A more sensible strategy would first identify categories related to gaming and then search for orders containing those products. Claude used the same inefficient approach. This represents a strategic common-sense failure rather than execution failure.
7 
Discussion
7.1 
The Capability Hierarchy as a Diagnostic Framework
Our hierarchy provides a diagnostic framework for understanding agent limitations. Rather than treating failure as monolithic, decomposition by capability level reveals actionable insights.
Development priorities
: A model failing primarily in tool use requires different interventions than
