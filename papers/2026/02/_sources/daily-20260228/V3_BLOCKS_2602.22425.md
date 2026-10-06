[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: ArchAgent: Agentic AI-driven Computer Architecture Discovery Thanks: † \dagger Work done while the author was also affiliated with Google.

[3] h6: Abstract.

[4] p: Agile hardware design flows are a critically needed force multiplier to meet the exploding demand for compute. Recently, agentic generative artificial intelligence (AI) systems have demonstrated significant advances in algorithm design, improving code efficiency, and enabling discovery across scientific domains.

[5] p: Bridging these worlds, we present ArchAgent, an automated computer architecture discovery system built on AlphaEvolve. We show ArchAgent’s ability to automatically design/implement state-of-the-art (SoTA) cache replacement policies (architecting new mechanisms/logic, not only changing parameters), broadly within the confines of an established cache replacement policy design competition.

[6] p: In two days and without human intervention, ArchAgent generated a policy achieving a 5.322 5.322 % IPC speedup improvement over the prior SoTA on public multi-core Google Workload Traces. On the heavily-explored single-core SPEC 2006 workloads, in only 18 days ArchAgent generated a policy showing a 0.907 0.907 % IPC speedup improvement over the existing SoTA (a similar "winning margin" as reported by the existing SoTA). Comparing against the effort involved in developing the prior SoTA policies, ArchAgent achieved these gains 3-5 × \times faster than humans.

[7] p: Agentic flows also create an opportunity once a hardware system is deployed, which we call “post-silicon hyperspecialization”. This means having the agent tune runtime-configurable parameters exposed in hardware policies to further align the policies with a specific workload (mix). Exploiting this, we demonstrate a 2.374 2.374 % IPC speedup improvement over prior SoTA on the SPEC 2006 workloads.

[8] p: Since ArchAgent is a first-of-its-kind architectural discovery system, we also outline lessons learned and broader implications for computer architecture research in the era of agentic AI. For example, we demonstrate the phenomenon of “simulator escapes”, where the agentic AI flow discovered and exploited a loophole in a popular microarchitectural simulator—a consequence of the fact that these research tools were designed for a (now past) world where they were exclusively operated by humans acting in good-faith.

[9] h2: 1. Introduction

[10] figure: Figure 1. High-level system diagram of ArchAgent, our agentic-AI-based computer architecture discovery system. In this example, novel cache replacement policy candidates are automatically designed/implemented by AlphaEvolve in ChampSim, a popular trace-based microarchitectural simulator. ChampSim is then compiled and run with a specified workload suite (e.g., SPEC) to evaluate the new policy on a target metric (e.g., IPC). This process continues iteratively, with ArchAgent continually proposing and evaluating new logic/mechanisms within the policy.

[11] p: The computing industry continues to battle the rift between the exploding demand for compute and the need for human-time-intensive per-domain specialization to make up for the plateau in classical hardware scaling techniques. Continued efforts in agile hardware design, more recently driven by the infusion of machine learning (ML), are welcomed to help bridge this gap. While inroads have been made in applying ML to RTL-to-chip flows, there is less focus on enabling automated “discovery” in earlier stages of the hardware design process, beyond using ML to explore parameterized design spaces. In this paper, we answer the following: Can modern generative AI tools help computer architects in early discovery, ideation, and pathfinding, so that we can more quickly architect a greater number of specialized architectures?

[12] p: Recently, agentic flows based on large language models (LLMs) have emerged as useful tools to automate algorithm design, software systems design, software efficiency, and scientific discovery ( Cheng et al., 2025 ; Novikov et al., 2025 ) . Guided by high-level prompting from a human, such a flow can generate, implement, and evaluate ideas much faster than a human designer. This shifts the designer’s focus to problem formulation, creative ideation, and experimental design.

[13] p: The basic premise of ArchAgent is straightforward: Agentic, evolutionary ML-based tools can automatically and iteratively express and evaluate new concepts as code, so we should have these tools write code to express new architectures in the context of our community standard (micro)architectural simulators. Closing the loop, since our simulators can provide quantitative feedback, these agents can work iteratively to improve their solutions with new mechanisms/logic developed on-the-fly by an LLM. In the rest of this paper, we discuss the benefits and tradeoffs of this approach and express a call-to-action for our community infrastructure to enable us to get the most out of these agentic AI tools.

[14] p: More concretely, we make the following key contributions:

[15] h4: 1.0.1. The ArchAgent system

[16] p: We design and implement ArchAgent, an agentic AI system that automates computer architecture discovery. ArchAgent expresses architectures as C++ models in ChampSim ( Gober et al., 2022 ) and builds on AlphaEvolve ( Novikov et al., 2025 ) , including a highly distributed evaluation setup to discover novel architectures. An outline of ArchAgent is shown in Figure 1 .

[17] h4: 1.0.2. Automatically designing state-of-the-art cache replacement policies

[18] p: We show that ArchAgent can discover state-of-the-art (SoTA) cache replacement policies, broadly adhering to the experimental design of established community cache replacement policy design championships, such as the Cache Replacement Championship ( Gratz et al., 2017 ) , most recently held in early 2017. The discovered policy improves IPC speedup normalized to LRU over the prior SoTA policy (published in followup work ( Shah et al., 2022 ) in 2022) by 0.737 0.737 % on single-core SPEC 2006 ( Henning, 2006 ) in the absence of prefetching, and by 0.907 0.907 % in the presence of prefetching. These gains are similar to prior “winning margins” reported by championship winners/new SoTA work in this domain. Notably, comparing against the effort involved in developing the prior SoTA policies, ArchAgent achieved these gains 3-5 × \times faster than humans.

[19] h4: 1.0.3. Policy deep-dive

[20] p: To demonstrate the kinds of mechanisms/logic that ArchAgent can design, we perform an ablation study on Policy31 , one of the winning replacement policies generated by ArchAgent. We break down the novel policy mechanisms created by ArchAgent qualitatively and quantitatively.

[21] h4: 1.0.4. Designing beyond SPEC

[22] p: In addition to discovering new policies for SPEC workloads, which is known to not be representative of cloud workloads ( Ferdman et al., 2012 ; Su et al., 2025 ; Gan et al., 2019 ) , we use the publicly-available Google Workload Traces ( 19 ) to discover high-performance policies for hyperscale workloads, and we show that ArchAgent can design a policy that produces a 5.322 5.322 % IPC speedup improvement over prior SoTA policies within two days. Previously designing a handcrafted hyperscale-centric policy would require a concerted, human-intensive effort spanning months.

[23] h4: 1.0.5. Post-silicon “hyperspecialization”

[24] p: Design flows like ArchAgent represent a new paradigm in automated discovery. Although we have only explored pre-silicon discovery thus far, we can now ask the question: Could ArchAgent further improve its generated policy post-silicon, by configuring the policy specifically for each workload at runtime? While this process would traditionally be extremely human-intensive, we show that ArchAgent can further improve IPC speedup by 2.374 2.374 % on average (up to 8.1 8.1 % on mcf_46B ) over the prior state-of-the-art by customizing post-silicon runtime-configurable policy parameters on memory-intensive SPEC 2006 workloads. It is important to note that this is the only part of this work where we only tune parameters; all other uses of ArchAgent are for devising new policy logic and mechanisms.

[25] h4: 1.0.6. Strengths, pitfalls, and a call-to-action

[26] p: ArchAgent provides a proof-of-concept that ML-assisted design flows can enable architectural discovery. However, this leaves many open questions still to be answered. We take an experiential and evidence-based deep-dive on the strengths and weaknesses of such systems today, including critical issues around about overfitting versus specialization, extrapolation from representative workloads, and the implications for our community evaluation infrastructure in the era of agentic AI.

[27] h2: 2. Background

[28] p: To set the context, we briefly cover very recent advances in two core areas: (1) agentic LLM-based evolutionary discovery tools and (2) cache replacement policy design and competition-based evaluation. A more substantial discussion of related work can be found in Section 8 .

[29] h3: 2.1. LLM-based Evolutionary Agents

[30] p: Recently, there has been an emergence of coding agents designed for algorithmic and scientific discovery, such as Google DeepMind’s AlphaEvolve. These agents use LLMs in combination with evolutionary search to discover new solutions across varied domains such as their use in mathematical proofs ( Georgiev et al., 2025 ) and software systems research ( Cheng et al., 2025 ) . Such agentic systems allow for the evolution of an entire code file (e.g., hundreds of lines of code) in any programming language through automatic generation and evaluation of code. This is done by a human programmer first providing setup instructions (e.g., task directives, evaluation criteria, and background knowledge) to the system and an initial solution to seed an evolutionary database. Next, the setup instructions and prior code blocks from the evolutionary database are sampled to create prompts, which are fed to LLMs to generate new code blocks. These new code blocks are fed into an evaluator, then ranked and fed into the evolutionary database before continuing on iteratively. Such ranking and evolution is done by way of evolutionary algorithms such as island-based evolution ( Romera-Paredes et al., 2024 ; Tanese, 1989 ) or MAP-Elites evolution ( Mouret and Clune, 2015 ) , which balance genetic diversity based on behaviors (e.g., code size and complexity) as well as performance on a specified metric (i.e., fitness score).

[31] h3: 2.2. Cache Replacement Championships

[32] p: With the goal of incentivizing the community to develop novel cache replacement policies, The 1st Journal of Instruction-Level Parallelism (JILP) Cache Replacement Championship (CRC-1) ( Alameldeen et al., 2010 ) was held in 2010 to compare different last level cache (LLC) cache replacement algorithms in a common evaluation framework. Given a fixed storage budget and predefined single- and multi-core configurations, competitors could submit cache replacement policies that would then be ranked by a common set of workloads. The latest championship, CRC-2 ( Gratz et al., 2017 ) , had four tracks: (1) single-core without prefetching, (2) single core with prefetching, (3) multi-core without prefetching, and (4) multi-core with prefetching. Each track was ranked separately, and the winner was decided based on the aggregate score across all tracks. The single-core track score was determined by the geometric-mean of replacement algorithm speedups across a set of single-threaded workloads, while in the multi-core track, scores were determined by the weighted speedup across a set of multi-program and multi-threaded workloads.

[33] p: Looking across CRC-1, CRC-2, and other non-championship publications in the cache replacement policy domain ( Gao and Wilkerson, 2010 ; Wu et al., 2011a ; Mowry et al., 1992 ; Young et al., 2017 ; Jain and Lin, 2016 ; Shah et al., 2022 ) , margins of instructions-per-cycle (IPC) improvement normalized to LRU compared to prior winners are typically reported to be in the range of 1% to 3%, for single-core ChampSim configurations across various mixes of workloads (including SPEC, GAP ( Beamer et al., 2015 ) , CVP1 ( Perais et al., 2018 ) , and more). For direct comparison, Mockingjay ( Shah et al., 2022 ) , the prior state-of-the-art cache replacement policy, saw a 1.6 1.6 % and 1.2 1.2 % increase in single-core performance normalized to LRU over Hawkeye ( Jain and Lin, 2016 ) across a memory-intensive subset of SPEC 2006 workloads, without prefetching and with prefetching, respectively. We make two observations across the winning policies:

[34] p: The winning margins are typically small and are getting smaller, which attests to the difficulty of the problem domain and the expectation that the headroom is shrinking.

[35] p: Nevertheless, the field of cache replacement has progressed gradually with wins in the 1%-3% range accumulating over time. However, each advance requires a concerted effort, with (usually) multiple researchers studying the problem over a long period of time.

[36] h2: 3. ArchAgent System Design

[37] p: ArchAgent harnesses an agentic generative AI system to automate computer architecture discovery. At its core, we utilize the fact that a common mechanism for expressing new computer architectures is writing code in a software (micro)architectural simulator, which is a good match for an evolutionary large language model-based code-authoring agent such as AlphaEvolve. ArchAgent integrates ChampSim, a widely used trace-based microarchitectural simulator written in C++, with AlphaEvolve and a distributed evaluation backend. AlphaEvolve is capable of rewriting any C++ code file in ChampSim, but for the results presented in this paper, we restrict it to designing last-level cache replacement policies. ArchAgent works iteratively: automatically implementing candidate policies in ChampSim and running large-scale, distributed ChampSim simulations to evaluate quality (primarily on instructions per cycle (IPC) achieved). The candidate policies and evaluation feedback guide an evolutionary search algorithm to propose changes for a new generation of candidates. Figure 1 shows a high-level overview of ArchAgent. In the rest of this section, we show the key components of ArchAgent in the context of using it to design new cache replacement policies.

[38] h3: 3.1. Prompting an LLM to be an Architecture Research Agent

[39] figure: ⬇ Act as an expert software developer and computer architect . The codebase that you are working on is a simulator for an out - of - order superscalar processor running a program trace . Your task is to iteratively improve the indicated section of the codebase , which models a replacement policy for the caches in the simulated processor and win the Cache Replacement Championship . That is , you want to design the best possible cache replacement policy for an out - of - order superscalar processor and implement it in the simulator . The primary goal is to increase the scores on the provided evaluation metrics , where larger values are better . One of these metrics is the number of instructions - per - cycle ( IPC ) that the processor executes . A better processor will achieve a higher IPC . [...] Ensure the code you introduce is realizable in hardware . Ensure you don ’t use more than 48KB state for your replacement policy. This is separate from the size of the cache itself. This is a strict limit and you must adhere to it honestly. Otherwise you will be disqualified. [... context about simulator caveats/APIs, max lines to change, workloads, system configs, prior working programs, and prior literature ...]’ Figure 2. Simplified example of a prompt given to the AlphaEvolve used in ArchAgent including persona, background information, guidance.

[40] p: To automatically generate new policies, we provide AlphaEvolve with an instruction prompt to describe the task and provide relevant background and context. Figure 2 lists a simplified example of a prompt used, that we aimed to be an expert computer architect persona. Combinations of prior policies (such as DRRIP, SHiP, Mockingjay), literature references, expectations of IPC headroom, and simulator interface information were provided to help an ensemble of fast and efficient (Gemini 2.5-Flash) and deep reasoning (Gemini 2.5-Pro) LLMs to generate varied policies. After each run, the prompt is automatically configured to provide solutions and metadata from previous runs to create the next evolution to test. Importantly, optimizations added included prompting the models to have more variation, respect hardware budget constraints (e.g., state size) required by the prior cache replacement championships, and reduce code complexity (e.g., upper bound of 1K lines of code). This included variations of word-play to “entice" the models to generate sufficiently different responses. The prompt described above is templatized, with various components probabilistically sampled and inserted to generate a variety of prompts at runtime to improve the volume of ideas explored.

[41] h3: 3.2. Starter Code

[42] p: We provide ChampSim’s default replacement policy C++ implementation files as starter code for AlphaEvolve to add new policy logic and change/remove ineffective logic. While we experimented with simple policies as starting points (e.g., LRU), we eventually converged on providing the Mockingjay policy source code, for faster progress and convergence due to slow simulation speeds. Similar to detailed documentation in the prompt, the file was also annotated extensively with additional API information, assumptions, and more.

[43] h3: 3.3. Workloads and ChampSim Hardware Configurations

[44] p: The choice of workload that can be fed to ChampSim in ArchAgent is flexible. In this case, we selected both SPEC 2006 and Google Workload Traces Version 2, representing a mix of publicly-available workloads with a variety of memory-traffic characteristics. These SPEC 2006 traces, obtained from CRC-2, use SimPoints ( Perelman et al., 2003 ) on multiple high LLC misses-per-kilo-instruction (MPKI) workloads ( Shah et al., 2022 ) . We use the publicly-available Google Workload Traces Version 2 and convert into a ChampSim-compatible format. For ChampSim microarchitectural configurations, we also used the default CRC-2 single- and multi-core configurations as seen in Table 1 . In Section 3.5 , we describe the process of running ChampSim on our distributed backend to maximize parallelism on long-running evaluations.

[45] h3: 3.4. Evaluation Metrics

[46] p: To match CRC-2, ArchAgent optimizes for the IPC of the cores running the given workloads. For single-core ChampSim configurations, this amounts to the geometric-mean IPC speedup over the baseline ChampSim LRU policy. For multi-core configurations, this is the weighted IPC speedup over the same LRU policy.

[47] p: While the initial LLM prompt was given a hardware budget and tips to improve explainability of generated responses, the underlying LLMs occasionally ignored instructions given. This resulted in combinations of unrealistic hardware implementations, circumventing the championship constraints, and complex and difficult to understand policies.

[48] p: In addition to stronger prompt verbiage (e.g. explicit lines of code wanted), we added the ability to measure the number of lines of code generated and negatively rewarded the system for longer responses. Once a final candidate policy was identified (i.e., after sufficient iterative progress on target metrics), additional manual checking was also done to verify that output policies represented realistic, hardware-implementable designs.

[49] figure: Table 1. Simulated ChampSim memory system configurations obtained from the 2nd Cache Replacement Championship. Parameter Single-Core Config. Multi-Core Config. (4 Cores) Prefetch Prefetch Disabled Enabled Disabled Enabled Cache Sizes L1 Data 48 KiB 48 KiB 48 KiB 48 KiB L1 Instruction 32 KiB 32 KiB 32 KiB 32 KiB L2 (Per Core) 512 KiB 512 KiB 512 KiB 512 KiB LLC (Shared) 2 MiB 2 MiB 8 MiB 8 MiB Prefetchers L1 Data - Next Line - Next Line L2 (Per Core) - PC Stride - PC Stride DRAM Bandwidth 25.6 25.6 GB/s 25.6 25.6 GB/s 25.6 25.6 GB/s 25.6 25.6 GB/s

[50] h3: 3.5. Challenges in Using a Microarchitectural Simulator as an AI Evaluator

[51] p: Evaluation of each policy change takes a significant amount of time because microarchitectural simulations are slow and ChampSim itself is single threaded. For example, the evaluation for single-core SPEC 2006 using ChampSim in the CRC-2 competition framing requires running workload traces for 1B instructions. Depending on the host machine running a simulation, the ChampSim configuration, and the benchmark being simulated, this can result in a single simulation taking over 12 hours on a SoTA server-class CPU. Multi-core evaluations are even slower, often taking 2-4 days for some workload mixes since simulation is single threaded, resulting in at least a proportional increase in runtime relative to the number of cores simulated.

[52] p: To reduce ArchAgent’s overall iteration time and avoid overfitting, we reduced the number of instructions run when evaluating proposed policies in each iteration of the evolutionary discovery process. While this resulted in some generalization issues—where results on shorter runs did not generalize to longer, representative runs—we took a cascaded approach wherein policies were created on shorter runs (i.e., 100M instructions) then later validated on longer runs (e.g., 1B instructions for SPEC results to match competition framing).

[53] p: To maximize iteration speed, we also added the capability to run parallel long-running simulations on a distributed cluster. As we began to run microarchitectural simulations in this fashion, we experienced issues common to building distributed systems, including seeing simulations get canceled due to maintenance operations (e.g., kernel updates) and other hardware instability. Typical scale-out software workloads would avoid this issue by periodically checkpointing intermediate state to persistent storage to restart from. However, the ChampSim simulator does not support this functionality, resulting in failed multi-day simulations (used for validating proposed policies) having to be restarted from scratch. Thus, additional infrastructure was built to automatically restart jobs and a locally managed persistent cluster was set up to handle long running jobs susceptible to interruption. In Section 7.3 we discuss augmenting computer architecture evaluation infrastructure to avoid these issues.

[54] h3: 3.6. Putting Together the Pieces

[55] p: After the above inputs are provided and the environment configured, ArchAgent controls the discovery process, automatically generating novel policies, testing them against the evaluation environment, and continually improving them using evolutionary search guided by quantitative evaluator feedback. Due to prompt randomization, LLM entropy, and evolutionary algorithm sampling, evolution speed varies as the system explores the design space and reaches a state-of-the-art solution.

[56] figure: Table 2. Comparison of Policy Evolution Setups. In Evaluation Metric , geomean is geometric-mean across benchmarks while mean(IPC) refers to the arithmetic mean of IPC across all cores. Policy Workload Simulation Instructions Evaluation Metric Evolution Time Evolution Validation Policy31 19 Memory Intensive SPEC06 Benchmarks max(50M, 100M) within 1 hr 1B g ​ e ​ o ​ m ​ e ​ a ​ n ​ ( IPC policy IPC lru ) geomean\left(\frac{\text{IPC}_{\text{policy}}}{\text{IPC}_{\text{lru}}}\right) 18 days Policy31-Tuned 19 Memory Intensive SPEC06 Benchmarks 1B 1B g ​ e ​ o ​ m ​ e ​ a ​ n ​ ( IPC policy IPC lru ) geomean\left(\frac{\text{IPC}_{\text{policy}}}{\text{IPC}_{\text{lru}}}\right) < 8 days Policy61 11 Google Workload Traces 50M 75M g ​ e ​ o ​ m ​ e ​ a ​ n ​ ( OPEN mean(IPC policy ) OPEN mean(IPC lru ) ) geomean\left(\frac{\text{mean(IPC}_{\text{policy}})}{\text{mean(IPC}_{\text{lru}})}\right) 4 days Policy62 11 Google Workload Traces 20M 75M g ​ e ​ o ​ m ​ e ​ a ​ n ​ ( OPEN mean(IPC policy ) OPEN mean(IPC lru ) ) geomean\left(\frac{\text{mean(IPC}_{\text{policy}})}{\text{mean(IPC}_{\text{lru}})}\right) 2 days

[57] h2: 4. Using ArchAgent to Automatically Design LLC Replacement Policies for Single-Core Systems

[58] p: In this case study, we use ArchAgent to design a last-level cache replacement policy, Policy31 , to compete in the single-core portion of the CRC-2.

[59] h3: 4.1. Methodology

[60] p: Policy31 is constructed by ArchAgent optimizing for SimPoint ( Perelman et al., 2003 ) traces from the SPEC 2006 workload suite on single-core ChampSim system configurations with both prefetching and no prefetching, as shown in Table 1 . To align with recent cache replacement policy evaluations ( Shah et al., 2022 ) , we only use memory-intensive SPEC workloads that have LLC MPKI > 1 with the LRU replacement policy. Workload-level speedup is measured as the IPC ratio of the generated policy over an LRU baseline ( I ​ P ​ C p ​ o ​ l ​ i ​ c ​ y I ​ P ​ C l ​ r ​ u \frac{IPC_{policy}}{IPC_{lru}} ) while suite-level speedup is measured as the geometric-mean of workload-level speedups as seen in Table 2 .

[61] p: For speedy evolution and to prevent overfitting, we provide feedback to ArchAgent by simulating a relatively small number of instructions (i.e., upto 100M instructions for each individual workload trace) to allow the simulations to complete within one hour. However, for validation, we collect final results by executing 1B instructions for each workload trace to comply with the CRC-2 competition framing. Quicker feedback allows ArchAgent to explore more solutions in the given time frame (further discussed in Section 7.3 ).

[62] h3: 4.2. Policy31 Description

[63] figure: ⬇ + // --- HAWKS AND DOVES STATE --- + // A bit-packed 2b sat. ctr per cache line + // Tracks usage intensity and follows state budget + // Each byte holds 4 counters + std::vector<uint8_t> packed_usage_counter; /* find a cache block to evict */ long policy31::find_victim(...) { for (...) { + // Retrieve H&D usage and use for ETR + current.usage = get_usage(set, way); + current . effective_etr = abs ( current . etr_val ) - (current.usage * BONUS_PER_USE); } } /* called on every cache hit and cache refill */ void policy31::update_replacement_state(...) { + if (hit) { + // Inc. usage counter (saturating at 3) + // This makes frequently- used blocks stickier + increment_usage(set, way); + } else { + // Fill on a miss (a new line inserted) + // The new block starts with a usage of 0 + reset_usage(set, way); + } } Figure 3. Example Policy31 modifications in the form of a diff to implement the Hawks and Doves mechanism. The packed_usage_counter and corresponding get -, increment -, and reset_usage setter/getters are used to help determine eviction candidates.

[64] p: Starting from the Mockingjay codebase, ArchAgent experimented for 18 days by adding (or changing/removing) code for new policy logic/mechanisms to create Policy31 .

[65] p: Mockingjay predicts the future reuse distance of each line using a PC-based predictor and then evicts the line whose predicted reuse is furthest in the future. ArchAgent augmented the policy with several new techniques discussed below.

[66] h4: 4.2.1. Insertion Quality

[67] p: Policy31 includes an Insertion Quality Predictor (IQP) to identify PCs that bring in dead blocks (i.e., blocks that are never used), and it penalizes reuse distance prediction for dead blocks by inflating their predicted reuse distance (which makes them more likely to get evicted).

[68] h4: 4.2.2. Hawks and Doves

[69] p: Policy31 tracks the usage intensity of each block with a 2-bit saturating counter. Blocks with a higher usage count are considered more valuable and are less likely to be evicted. Figure 3 shows the logic to adjust ETR (Estimated Time of Reuse) based on usage.

[70] h4: 4.2.3. Prefetch-Aware Retention

[71] p: Policy31 introduces logic to deprioritize easy-to-prefetch sources by giving them a high ETR and prioritize difficult-to-prefetch sources by giving them a low ETR.

[72] h4: 4.2.4. Cache Pressure-Aware Adaptive Throttling (CPAAT)

[73] p: Policy31 introduces a new mechanism to dynamically adjust the bypass aggressiveness based on the overall miss rate (i.e., cache pressure). Under high pressure, it’s more conservative with new insertions, preserving the existing working set.

[74] h3: 4.3. Results

[75] figure: Figure 4. Performance improvement (suite-level geomean IPC speedup normalized to LRU) compared to estimated development time of replacement policies for the single-core prefetch-enabled ChampSim configuration on memory-intensive SPEC06 workloads. Slope (grey, italics) denotes percentage point improvement per day.

[76] p: We compare suite-level IPC speedup improvement normalized to the standard LRU baseline. We find that Policy31 improves IPC speedup normalized to LRU by 12.2 12.2 % and 8.0 8.0 % in the no prefetch and prefetch configurations, respectively (versus 11.4 11.4 % and 7.0 7.0 % for Mockingjay). Figure 6 shows the workload-level improvement across the suite in the prefetch-enabled case, demonstrating overall improvement and no significant outliers.

[77] p: To put these improvements in context, Section 2.2 describes that the historical rate of improvement for cache replacement for single-core ChampSim configurations is reported to be in the 1-3% range per solution. Each improvement in prior work has needed significant effort by multiple researchers over several months, whereas here we have demonstrated that ArchAgent can achieve similar gains in less than 3 weeks.

[78] p: Figure 4 compares the performance improvement achieved by successive SoTA cache replacement policies compared to the estimated time of developing these policies for the single-core prefetch-enabled ChampSim configuration on memory-intensive SPEC06 workloads. The estimated development time was obtained from their creators. These reported times include only time to develop the policies, excluding, for example, paper writing time. When comparing the effort involved in developing Policy31 and the prior SoTA policies, we find that ArchAgent achieved its gains 3-5 × \times faster than humans. Furthermore, replacement policy development for SPEC workloads is well explored as prior work has demonstrated that existing solutions come within 90% of the hit rate optimal solution ( Shah et al., 2022 ) . This points to the increasing difficulty of finding performance improvements for this problem domain.

[79] h3: 4.4. Ablation Study

[80] figure: Figure 5. Ablation study measuring improvement in suite-level geomean IPC speedup with each new technique that composes Policy31 for the single-core prefetch-enabled ChampSim configuration running SPEC06 memory intensive workloads.

[81] figure: Figure 6. Per-workload improvement in policy IPC speedup normalized to LRU for the single-core prefetch-enabled ChampSim configuration running SPEC 2006 memory intensive workloads.

[82] p: To better understand the source of performance improvement for Policy31 , we run an ablation study breaking down the impact of key policy features created by ArchAgent (described in 4.2 ). Figure 5 shows the ablation study results when running on the default single-core prefetch-enabled ChampSim configuration running workloads from SPEC 2006 suite for 1B instructions. Selectively, the study re-enables the various mechanisms that comprise Policy31 one-by-one, until the complete Policy31 is evaluated. As seen in the figure, most of the improvement is coming from CPAAT and Hawks and Doves, providing a 0.818 0.818 % improvement, combined. IQP and prefetch management result in marginal gains and only show benefits when combined with all other mechanisms.

[83] p: This highlights a challenge with machine-generated policies, where manual work is still needed to not only validate the performance improvement but also understand the root cause. To have high confidence in machine-generated policies, the process of ablation and verification will remain a key bottleneck that could also benefit from automation, as discussed further in 7.1 .

[84] h2: 5. Using ArchAgent for Runtime-Configurable, Workload-Specific Hyperoptimization

[85] p: We observe that ArchAgent-generated policies such as Policy31 introduce new microarchitectural techniques that make the policies flexible and amenable to runtime tuning. These runtime parameters are expressions in the policy that do not affect storage size and are instead either constants or simple arithmetic expressions derived from constants. We identify 13 runtime parameters in Policy31 that fall into the following two categories:

[86] p: Constants used in scores such as ETR or bonuses/penalties for particular categories of accesses (e.g., prefetches).

[87] p: Thresholds such as those used to detect long ETR blocks or initiate adaptive decay of cache counters.

[88] h3: 5.1. Methodology

[89] p: Since we are exploring runtime tuning, both evolution and validation are performed on the memory intensive SPEC 2006 workload subset mentioned in Section 4.1 running for 1B instructions (Table 2 ). ArchAgent optimizes each workload individually and we enforce that it only changes runtime parameters instead of the entire replacement policy.

[90] h3: 5.2. Results

[91] p: ArchAgent creates a new runtime parameter-tuned variant of Policy31 , called Policy31-Tuned , tuned for individual SPEC 2006 workloads on the championship single-core ChampSim prefetch-enabled configuration. When comparing suite-level speedups, Policy31-Tuned achieves an additional 1.467 1.467 % overall geometric-mean IPC improvement as compared to Policy31 and 2.336 2.336 % overall improvement compared to Mockingjay, normalized to LRU. When analyzing workload-level speedups, Figure 6 shows that workloads such as gcc_13B and mcf_46B show > 5 5 % gain while others show limited improvement (e.g., calculix_2670B ).

[92] p: To put these results in context, Figure 4 shows that ArchAgent’s rate of improvement with Policy31-Tuned is over 10 × \times faster than prior SoTA policies. Notably, this improvement was achieved in less than eight days.

[93] p: These results highlight the potential of AI-driven runtime specialization of hardware to specific workloads and we envision that such post-silicon hyperoptimizations could be commonplace, similar to automatic profile-guided optimizations prevalent in hyperscalers ( Chen et al., 2016 ; Litz et al., 2022 ; Ayers et al., 2020 ) .

[94] h2: 6. Using ArchAgent to Automatically Design Multi-Core LLC Replacement Policies for Google Workload Traces

[95] p: With Policy31 , we show ArchAgent can win within an established competition environment on SPEC 2006. However, it is widely established that SPEC 2006 is not representative of hyperscale cloud workloads ( Ferdman et al., 2012 ) . For example, SPEC workloads have much smaller instruction footprints and significantly lower instruction cache pressure as compared to hyperscale workloads. While Mockingjay shows clear wins on both single- and multi-core SPEC, Figure 8 shows it performs much worse than even LRU on Google Workload Traces.

[96] p: Thus, in this case study, we use ArchAgent to generate multi-core cache replacement policies, Policy61 and Policy62 , specialized for publicly-available Google Workload Traces Version 2.

[97] h3: 6.1. Methodology

[98] p: Policy61 and Policy62 are generated by running 11 workloads from the Google Workload Traces Version 2 suite across both prefetch and non-prefetch multi-core ChampSim configurations stated in Table 1 . The DynamoRIO trace scheduler ( Bruening et al., 2003 ) , similar to an operating system scheduler, is used to schedule thread-level traces from each workload onto the four cores of the multi-core system.

[99] p: Final validation is done by simulating the two policies for 75M instructions as seen in Table 2 . Here, workload mix speedup is computed as the arithmetic mean of IPC across cores normalized to the arithmetic mean of IPC across cores using the LRU replacement policy. We find this to be a suitable metric because all four cores are executing threads from the same workload. Suite-level speedup is measured as the geometric-mean of workload-level speedups.

[100] p: For speed, we provide evolution feedback by simulating 50M and 20M instructions for Policy61 and Policy62 , respectively. The feedback metric averages suite-level speedup scores for both multi-core configurations.

[101] p: We provide the Mockingjay source code as the starter code for both policies, and we allow ArchAgent to change the entire replacement policy code.

[102] h3: 6.2. Policy Description

[103] p: Two different ArchAgent runs on these traces resulted in two vastly different policies, but both are building on the premise that code characteristics of hyperscale workloads are different, so the use of PC as a feature needs to be revisited.

[104] h5: Policy61

[105] p: Policy61 was generated over the course of four days. It maintains the core algorithm of Mockingjay, but makes one critical change: it enriches the signature used for prediction with information about the path taken to reach the current instruction as seen below.

[106] p: This is expected to help in scenarios where the calling context of a PC is important for its caching behavior. For example, a generic memcpy routine might be called to copy small, frequently-reused data structures in one part of a program, and to perform large, non-temporal streaming copies in another. A predictor that only looks at the PC of the memcpy ’s load/store instructions will conflate these distinct behaviors, leading to an average prediction that is optimal for neither case.

[107] p: Similar ideas have been proposed in the literature before ( Shi et al., 2019 ; Mirbagher-Ajorpaz et al., 2020 ) , but not in the context of Mockingjay.

[108] h5: Policy62

[109] p: Policy62 was generated over the course of two days and uses a completely different approach from Mockingjay. It first removes all the key components of Mockingjay (including reuse prediction and eviction based on estimated time of reuse) and then evolves into something that is very close to SHiP, but is much more adaptive and sensitive to larger code footprints.

[110] p: In particular, two key ideas make Policy62 different:

[111] p: Tagged Predictor Table : PC-based cache predictors usually allow for aliasing, and the tables are simply indexed by a hash without any tag matching. Policy62 explicitly stores a 3-bit tag inside the predictor entry. Predictions are retrieved only if the tags match. If the tags don’t match, it resets the entry. This prevents “destructive aliasing," making the predictor more precise.

[112] p: Learning Signal : SHiP typically trains its predictor at the time of eviction. When a block is kicked out of the cache, SHiP checks whether the block was used. If yes, the counter for the PC that inserted it is incremented. If not, the counter is decremented. By contrast, Policy62 updates the predictor when the line is accessed. If the line hits, the counter for the PC corresponding to the access is incremented. If the line misses, the counter for the PC corresponding to the access is decremented.

[113] p: While subtle, the second difference is significant because it allows Policy62 to learn much quicker than SHiP or Mockingjay. Waiting for cache eviction to learn can prolong learning feedback. The key idea here is that some PCs have a small working set that can be cached, while most others will not see reuse due to the large working set. Thus, PCs that miss frequently (and fetch a lot of data) are penalized and PCs that hit frequently are prioritized for cache residency.

[114] figure: Figure 7. Improvement in geomean IPC speedup normalized to LRU for the multi-core prefetch-disabled ChampSim configuration running Google Workload Traces. Figure 8. Improvement in geomean IPC speedup normalized to LRU for the multi-core prefetch-enabled ChampSim configuration running Google Workload Traces.

[115] figure: Figure 9. Per-workload improvement in policy IPC speedup normalized to LRU for the multi-core prefetch-enabled ChampSim configuration running Google Workload Traces.

[116] h3: 6.3. Results

[117] p: Figures 8 and 8 compare suite-level speedups on multi-core configurations with prefetching disabled and enabled, respectively. We find a major inversion in trends here with Mockingjay performing much worse than even LRU and SHiP emerging as the prior SoTA policy.

[118] p: On the non-prefetch configuration, we find that SHiP, Policy61 , and Policy62 achieve a 3.003 3.003 %, 4.732 4.732 %, and 6.116 6.116 % improvement over LRU, respectively.

[119] p: On the prefetch-enabled configuration, we find that SHiP, Policy61 , and Policy62 achieve a 2.905 2.905 %, 5.444 5.444 %, and 8.227 8.227 % improvement over LRU, respectively.

[120] p: On the prefetching-enabled configuration, Mockingjay, the starter code for ArchAgent policies, shows a slowdown of 9.538 9.538 % over LRU. Thus, ArchAgent recovers a performance deficit of 17.765 17.765 % with a simpler policy.

[121] p: Figure 9 shows workload-level speedups across the Google Workload Traces suite in the prefetch-enabled case with Policy61 and Policy62 showing consistently strong performance compared to prior work.

[122] p: In our understanding, the trend inversion between Mockingjay, SHiP, and LRU, and the strong performance of Policy61 and Policy62 —simpler policies derived from Mockingjay—can be attributed to the unique characteristics of these hyperscale workloads, such as deep call stacks, high degree of multithreading, and high context switch rates.

[123] p: We show that ArchAgent enables designers to rapidly customize replacement policies to previously unexplored workload classes.

[124] h2: 7. Discussion, Future Work, and a Call-to-Action

[125] p: The use of evolutionary coding agents in computer architecture research shows great promise, but will require significant improvements to our community research infrastructure, as well as continued experimentation with AI tools. In this section, we outline some of the key takeaways and potential next steps in this area.

[126] h3: 7.1. LLM Capabilities and Constraints

[127] p: A central finding of this study is the remarkable capability of LLMs to generate new microarchitectural designs, including both microarchitectural technique discovery and parameter optimization. Given a rich context, our evolutionary agent automatically generated novel, complex, and functionally correct hardware policies that improved on the performance achieved by state-of-the-art human-designed policies for both classical workloads (SPEC) and hyperscale workloads (Google Workload Traces).

[128] p: Given the current approach however, confirming the realizability of generated policies remains a human intensive process, due to the lack of ASIC quality-of-result data (e.g., frequency and area) in most microarchitectural simulators. In our case, while we found specialized prompts to be effective at generally guiding the LLMs along these lines, significant human-driven verification was still needed to guarantee compliance. For example, to avoid complex, difficult-to-understand policies with thousands of lines of changes, we combined the use of additional prompting to limit code size (a proxy for code complexity and hardware realizability) as well as a rule-based verifier that calculated the number of total/added lines of code and discarded samples violating constraints. This significantly improved the explainability of solutions found, reducing the time-consuming manual ablation studies needed to understand any improvement and estimate its true hardware overhead. However, writing rule-based verifiers is not feasible for all constraints. As an example, inferring physical storage size from a microarchitectural model is non-trivial and thus we still rely on prompting and manual pruning/assessment for such a constraint. This highlights a critical and interesting avenue for future work: developing principled, automated methods to inject these hard architectural constraints directly into the design process, moving beyond simple prompting or post-generation manual verification.

[129] p: Additionally, despite the high quality of generated solutions evidenced in this work, there remains significant opportunity in pushing the limits of the type of solutions ArchAgent can generate. For one, there is an opportunity to collect a dataset representing a much greater sample of prior art in the cache replacement space, both in terms of implementations (software code, RTL) and descriptions (documentation, academic papers, industrial reports). Adding additional agents in the loop is another opportunity. Each of a group of multiple agents can employ a different persona, e.g., a microarchitect, an SRAM design/process design expert, a physical design expert, and a workload expert, each of which are responsible for providing different (and perhaps competing) feedback on the design, potentially using industry standard EDA tools.

[130] h3: 7.2. Hardware/Software Co-Design For Hyperspecialization

[131] p: The automated nature of evolutionary coding agents will have significant implications for computer architecture and systems research. Historically, the immense human effort and simulation time required to design and validate even a single new heuristic has biased the field toward generalist solutions; policies that perform adequately, but rarely optimally, across all workloads. The sheer productivity of an automated parallelizable agent, which can generate and evaluate thousands of policy variants in a short time, shatters this barrier and makes specialization computationally feasible, especially if deployed systems support experimentation.

[132] p: This capability can usher in a new era of hardware-software co-design, moving beyond the “one-size-fits-all" paradigm. Instead of a static, general-purpose cache policy, a system built with even greater runtime configurability (vs. the simpler runtime parameter tuning we explored in Section 5 ) could deploy purpose-built heuristics per workload. For example, a heuristic evolved specifically for a critical database, a high-priority AI model, or a latency-sensitive video pipeline could yield significant efficiency benefits. This requires the right low-cost flexible hardware-software interfaces that allow an operating system or hypervisor to securely and efficiently specialize hardware components, a promising and critical direction for future systems research.

[133] h3: 7.3. A Call-to-Action: Evaluation Methodology Improvements

[134] p: Evaluation methodology, namely computer architecture simulator performance and quality, needs to be re-evaluated in the new era of (potentially adversarial) AI agent-driven execution.

[135] p: In our early experiments, we found that ArchAgent was “willing” to take any shortcut made available by the simulation environment, unlike a human researcher acting in good faith. We describe one such “simulator escape”—a situation where the agentic AI flow discovered and exploited a loophole in the simulator used for evaluations.

[136] p: The ChampSim simulator does not support write-bypassing in the LLC. Verification that a policy is not performing write-bypassing only takes place in an assertion that is eliminated by the compiler when ChampSim is compiled with optimizations enabled . Given the simulator performance concerns described in Section 3.5 and below, building with these optimizations enabled is crucial. In this case, ArchAgent developed a policy called Policy12 , that appeared to be beating Mockingjay on the SPEC06 workloads in the single-core no-prefetch and prefetch scenarios by 3% and 4%, respectively. However, ArchAgent won by taking advantage of the fact that a bypassed write in the LLC would disappear from the system entirely. This not only avoided evicting a potentially more useful line, but also eliminated the corresponding DRAM write pressure entirely , drastically improving IPC. Since there is no notion of “correct computation” in such a trace-driven simulator, there was no further way to detect this issue.

[137] p: Building simulators that are either better verified or closer to the actual hardware design (e.g., RTL simulation or hardware-accelerated emulation) and thus less susceptible to “abuse” by the AI agents is crucial. Incorporating simulators that are closer to the actual hardware design (e.g., RTL-derived) would also have the added advantage of providing additional feedback to ArchAgent-like tools, including frequency, area, and power data collected from ASIC EDA tools.

[138] p: As discussed briefly in Section 3.5 , simulation speed also limits ArchAgent’s rate of discovery. ArchAgent’s ability to reach creative solutions is inversely proportional to the evaluation latency. This becomes untenable for long, complex simulations which are commonplace in computer architecture. For example, evaluating a single design point for a multi-core system using ChampSim, executing hundreds of millions of instructions, can require a 12- to 24-hour turnaround. An evolutionary search, which needs to evaluate thousands of candidates for enough variation, can be severely limited by the simulation speed, reducing the chances for the tool to try sufficiently interesting and “risky” ideas. Similarly, this simulation speed also hinders evaluation of longer representative workloads (e.g., instead of simulating 1B instructions, simulating hundreds of billions of instructions representative of production programs).

[139] p: As established in this discussion, to truly unleash the power of AI-driven architecture discovery, computer architecture simulators must become both more accurate and orders of magnitude faster, warranting more research into higher fidelity frameworks and simulators. Hardware-accelerated simulators such as FireSim ( Karandikar et al., 2018 ) could provide solutions to this problem.

[140] h2: 8. Related Work

[141] p: There has been decades of research in designing efficient cache replacement policies and applying broader automated techniques for hardware-software discovery.

[142] h3: 8.1. Designing Cache Replacement Policies

[143] p: Prior work on cache replacement policy design can be viewed from the lens of different design methodologies, which can be broadly categorized into three main paradigms: handcrafted heuristics, ML-based policies, and evolutionary parameter tuning.

[144] h4: 8.1.1. Heuristic-based Replacement

[145] p: Over three decades, handcrafted heuristics have changed from simple, static rules to highly sophisticated, adaptive algorithms. Early work proposed static heuristics ( O’Neil et al., 1993 ; Smaragdakis et al., 1999 ; Wong and Baer, 2000 ; Lee et al., 1999 ; Karedla et al., 1994 ; Gao and Wilkerson, 2010 ; Qureshi et al., 2007 ; Seshadri et al., 2012 ; Jaleel et al., 2010b ) to avoid pathologies of LRU and LFU. More recent heuristics take a predictive approach ( Lai et al., 2001 ; Kaxiras et al., 2001 ; Khan et al., 2010 ; Wu et al., 2011a ; Jain and Lin, 2016 ; Teran et al., 2016 ; Jiménez and Teran, 2017 ; Hu et al., 2002 ; Abella et al., 2005 ; Takagi and Hiraki, 2004 ; Keramidas et al., 2007 ; Duong et al., 2012 ; Kharbutli and Solihin, 2005 ; Liu et al., 2008 ; Faldu and Grot, 2017 ) . They leverage past behavior to predict future caching priorities. The Mockingjay policy ( Shah et al., 2022 ) use predicted reuse distances to mimic Belady’s optimal caching solution ( Belady, 1966 ) . More recently, Mostofi et al. use offline profiling to determine Insertion and Promotion Vectors for an unseen trace, however, this solution does not outperform Mockingjay ( Mostofi et al., 2025 ) . We use Mockingjay as the initial code that the AI agent starts from for better performance.

[146] p: Another line of work recognizes that cache replacement policies must operate in the context of the system they are in. For example, prefetch-aware policies ( Wu et al., 2011b ; Jain and Lin, 2018 ; Yuan et al., 2025 ) recognize the distinction between demand and prefetch accesses to make replacement decisions; other policies make a similar distinction for instruction accesses ( Mostofi et al., 2025 ) or TLB accesses. There is also work that recognizes the need for adapting replacement policies to the nature of the cache hierarchy, such as inclusive caches ( Jaleel et al., 2010a ) or sliced caches ( Sweta et al., 2025 ) .

[147] p: From a methodological perspective, all these solutions are based on human intuition and insight. These works do not leverage any automated methods to search the design space of replacement policies.

[148] h4: 8.1.2. ML-based Replacement

[149] p: One branch of research deploys ML models directly in hardware, ranging from lightweight online learning ( Zhou et al., 2022 ) to full deep learning inference ( Liu et al., 2020a ; Vietri et al., 2018 ) . For example, PARROT ( Liu et al., 2020b ) casts cache replacement as an imitation learning problem to approximate the “oracle" decisions of Belady’s optimal policy. These policies result in high implementation complexity and overhead, as they require online neural network inference.

[150] p: Therefore, a second line of research uses powerful, unconstrained ML models in an offline setting to discover features and insights, which are used to design hardware-friendly online policies ( Shi et al., 2019 ; Sethumurugan et al., 2021 ) . For example, the Glider policy ( Shi et al., 2019 ) leveraged a powerful, attention-based Long Short-Term Memory (LSTM) network to discover novel features for a simple online model. In this case, the ML model serves as a “discovery engine," but interpreting the model and designing the final simple policy remains a manual process.

[151] p: Our work is the first to bridge the divide between these two schools. We introduce an evolutionary coding framework that automates the discovery process of the “Offline Insight" school, while explicitly optimizing for the simplicity and hardware-efficiency that is the key bottleneck for the “Online Learning" school.

[152] h4: 8.1.3. Evolutionary Computation for Replacement Policy Tuning

[153] p: Prior work that has used evolutionary computation to discover replacement policies has focused on using genetic algorithms to tune parameters within a predefined policy structure ( Butt and Abhari, 2010 ; Mourad et al., 2020 ; Zadnik and Canini, 2010 ) . While these works established a precedent for using evolutionary search, they were limited to optimizing parameters within a fixed-model, rather than evolving the structure of the algorithm itself. More recently, an evolutionary coding framework was used to build web-based caching policies ( Dwivedula et al., 2025 ) . This work uses an approach that is similar to ours, but applies it to software caches, where the constraints and performance tradeoffs are different.

[154] h3: 8.2. ML For Other Design Tasks

[155] p: Beyond predictive policies like cache replacement or branch prediction, ML has been used across a wide-variety of hardware-software co-design domains.

[156] p: With the growing importance of ML accelerators, multiple prior works have focused on hardware-software co-design of neural network accelerators through various search space optimization techniques ( Sakhuja et al., 2023 ; Murali et al., 2024 ; Xiao et al., 2021 ; Xiao et al., 2025 ; Zhang et al., 2022 ) . These works often formulate the search problem to explore both hardware mixes and software mappings to newly generated hardware, leveraging advanced analytical modeling to quickly iterate through the design space. Our work differs from these by focusing on policies , with a well defined set of championship constraints that resulting policies need to be evaluated with a detailed microarchitectural simulator running a mix of standard and realistic hyperscale CPU workloads.

[157] p: Other techniques focused on optimizing microarchitectures ( Bai et al., 2024 ) , instead focus on other reinforcement learning techniques to explore pre-silicon parameters of microarchitectures or in the case of software, optimizing existing codebases/systems ( Cheng et al., 2025 ; Massalin, 1987 ; Vuduc and Demmel, 2000 ) . Our work is different from these approaches as it tackles the whole-scale design (of a cache replacement policy) rather than parametric optimization of an existing system using LLM-based discovery tooling.

[158] h2: 9. Conclusions

[159] p: In this paper, we have introduced ArchAgent, a first step towards building an agentic artificial intelligence system for automatic novel computer architecture discovery. Using ArchAgent, we automatically designed and implemented four novel cache replacement policy algorithms, Policy31 , Policy31-Tuned , Policy61 , Policy62 , that beat SoTA cache replacement policies tested in various cache replacement championships. On the public multi-core Google Workload Traces, ArchAgent achieved a 5.322 5.322 % better IPC speedup over the prior SoTA within two days, and on the single-core SPEC06 workloads, it achieved a 0.907 0.907 % better IPC speedup over the prior SoTA in 18 days. Comparing against the effort involved in developing the prior SoTA policies, ArchAgent achieved these gains 3-5 × \times faster than humans. We identified that agentic flows such as ArchAgent enable post-silicon hyperspecializtion of hardware systems to a specific workload (mix) demonstrating a 2.374 2.374 % IPC speedup improvement over prior SoTA on single-core SPEC06 workloads. While we highlight that the use of these agentic systems allows for a dramatic increase in computer architecture discovery, further improvements are needed to improve simulator fidelity and speed in the era of agentic-AI-assisted research.

[160] h2: 10. Acknowledgments

[161] p: This paper has used generative AI technologies in the following ways. First, the core work done by this paper uses AI tooling to develop novel cache replacement policies. Minor use of generative AI tooling was used to generate tables, plot graphs, and assist with clarity and flow, limited to phrases and single sentences. The authors have reviewed, verified, and edited all such generated content and take full responsibility for the content of the paper, including any errors or omissions.

[162] h2: References

[163] h2: Instructions for reporting errors

[164] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[165] p: Tip: You can select the relevant text first, to include it in your report.

[166] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[167] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
