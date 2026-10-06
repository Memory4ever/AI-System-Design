# Exact-v1 decisive primary response — 19747

Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation (https://arxiv.org/html/2601.19747v1)
citeturn28470view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19747v1","lineno":225}); Total lines: 942
L194: For purely combinational obligations, the Boolean Proofer first infers candidate combinational targets from $\widehat{C}$ (where latency $=0$) and filters out sequentially-driven signals via a dependency analysis, avoiding invalid proofs on stateful logic. It then synthesizes a compact reference combinational model from the contract’s functional summary and constructs a standard miter that compares DUT and reference under identical inputs. Writing the miter error as:
L195:  | $$e(\mathbf{x})\;=\;\bigvee_{y\in\mathcal{Y}_{\mathrm{comb}}}\Big(y_{\mathrm{DUT}}(\mathbf{x})\neq y_{\mathrm{spec}}(\mathbf{x})\Big),$$  |  | (4)
L196: 
L197: the goal is to prove $\forall\mathbf{x},\,e(\mathbf{x})=0$ using SymbiYosys. If the proof fails, the resulting counterexample is distilled into a concrete input assignment.
L198: 
L199: The formal hints produced by the branches are injected into the Debugger prompt, separating timing faults from pure Boolean faults and improving repair generalization.
L200: ## 4 The VerilogEval-v2-EXT Benchmark
L201: 
L202: Figure 3: VerilogEval-v2-EXT problem taxonomy.
L203:  |  |
L204: (a) Code Length  | (b) Assign Count  | (c) Sequential Structure
L205:  |  |
L206: (d) Control Branching  | (e) Data Width  | (f) Construct Coverage
L207: Figure 4: Dataset complexity statistics comparing the original one and ours (full extended dataset). (a–e) show distributions over problems for different metrics and (f) reports the Verilog construct coverage.
L208: We introduce VerilogEval-v2-EXT, an expanded benchmark for evaluating LLMs on realistic RTL code generation. It extends VerilogEval-v2 (cite98†Pinckney et al., 2025 ) with 53 new, industrial-grade design tasks, increasing the total from 156 to 209 problems.
L209: All tasks follow the same evaluation protocol as VerilogEval-v2: each problem provides a natural-language specification, a fully specified module interface, and an executable testbench used for functional checking, enabling direct comparison with prior results.
L210: ### 4.1 Industrial-Grade Extension
L211: 
L212: VerilogEval-v2 offers strong coverage of basic digital logic problems, but it under-represents modules that dominate real RTL development (e.g., protocol controllers, buffering, and multi-cycle datapaths). As a result, models may achieve high scores while still failing on engineering-critical behaviors such as latency alignment, corner-case handling, and stateful control logic.
L213: To address these gaps, we curated 53 new problems that reflect common Intellectual Property (IP) blocks and system components, including communication protocols and buffering (e.g., Universal Asynchronous Receiver Transmitter (UART) interfaces and First-In-First-Out (FIFO) queues), control-dominated designs (e.g., nontrivial Finite State Machines (FSMs), and richer datapath modules (e.g., advanced arithmetic and DSP-style kernels).
L214: cite111†Figure 3 summarizes the resulting benchmark composition and details are provided in cite33†Appendix A .
L215: ### 4.2 Difficulty Annotations
L216: To support finer-grained analysis beyond an aggregate pass rate, we stratify the 209 problems into Easy/Medium/Hard using a rule-based complexity score derived from observable structural signals, including lines of code, counts of assign/always/case constructs, and datapath width, supplemented with manual review. Full scoring details and thresholds are provided in cite38†subsection A.3 .
L217: cite112†Figure 4 shows that the extension increases structural complexity, especially within the Hard subset (e.g., longer solutions with more sequential structure and wider datapaths, up to 1024-bit). Together, these additions make VerilogEval-v2-EXT a more discriminative and industry-aligned testbed for evaluating end-to-end RTL code generation and debugging.
L218: ## 5 Experiments
L219: 
L220: ### 5.1 Experimental Setup
L221: 
L222: #### Benchmark
L223: 
L224: We evaluate on our VerilogEval-v2-EXT benchmark and report Pass@1 for syntax and functional correctness. Syntax success means the simulator compiles the generated RTL code without errors. Functional success means the compiled DUT passes the provided testbench.
L225: #### Baselines
L226: We compare Veri-Sure against 15 standalone LLMs^{1}^{1} 1 For better clarity, we cite the models here rather than in the tables: GPT-5.2 (cite113†OpenAI, 2026 ); Claude-4.5-Sonnet (cite114†Anthropic, 2025 ); Gemini-3-Pro (cite115†Google Deepmind, 2025 ); Qwen3-Max, Qwen3-Coder-Plus (cite116†Qwen AI, 2025b ; cite117†Qwen AI, 2025a ; cite118†Yang et al., 2025 ); Mistral-Medium-3.1, Ministral-3-14B, Devstral-2 (cite119†Mistral AI, 2025b ; cite120†Liu et al., 2026 ; cite121†Mistral AI, 2025a ); DeepSeek-3.2 (cite122†DeepSeek-AI et al., 2025 ); LLaMA-4-Maverick (cite123†Meta AI, 2025 ); GLM-4.7 (cite124†Zhipu AI, 2025 ; cite125†Team et al., 2025 ); QiMeng-SALV (cite104†Zhang et al., 2025 ); RTL-Coder (cite89†Liu et al., 2024 ); CodeV-R1 (cite90†Zhu et al., 2025 ); VeriLogos (cite92†Min et al., 2025b )., covering both commercial closed-source and recent open-weight models, that generate the DUT in a single attempt.
L227: We also include single-agent simulator-feedback baselines that wraps most^{2}^{2} 2 Sadly, we cannot afford to run Claude as an agentic system. models with an iterative compile/simulate loop, feeding Verilator logs back for regeneration. Finally, we evaluate representative multi-agent frameworks, MAGE (cite97†Zhao et al., 2025 ) and VerilogCoder (cite96†Ho et al., 2025 ) with the latest backbone model and report all of the comparisons in cite126†Table 1 .
L228: #### Toolchain and Computing
L229: 
L230: All methods use the same testbenches and verification toolchain. We use Verilator for syntax checking and simulation, chosen for its better support of SystemVerilog assertion-style checks used by our Asserter. For Boolean proof, we use SymbiYosys with a Z3 backend. Commercial models are queried via official APIs; open-weight models are run locally on NVIDIA A100 80GB GPUs. Iterative methods are capped at most $K{=}10$ repair iterations.
L231: ### 5.2 Main Results
L232: Table 1: Performance comparison on VerilogEval-v2-EXT (Pass@1, %). Params reports total (active) parameters for MoE models, and total for dense models; “w.” denotes “with” the specified backbone. Background colors indicate rankings in each column: 1st, 2nd, and 3rd denote the Global Performance across all methods. Blue highlights the Group Best performance if they are not in the global top-3. We assign these badges for standalone LLMs:    Best Open-Source: Top performing open-weights model.
L233:    High Potential: Largest relative gain when enhanced by agents.    Efficiency King: Best performance-to-parameter ratio.    Reasoning Expert: Best performance on the “Hard” subset.    Robust Performer: Minimal gap between Syntax and Functional scores.
L234: Method  | Params  | Easy ($n=51$)  | Medium ($n=91$)  | Hard ($n=67$)  | Overall
L235: Syn.  | Func.  | Syn.  | Func.  | Syn.  | Func.  | Syn.  | Func.
L236: Standalone LLMs
L237: ---
L238: GPT-5.2  | -  | 100.00  | 94.12  | 100.00  | 79.12  | 100.00  | 59.70  | 100.00  | 76.56
L239: Claude-4.5-Sonnet  | -  | 100.00  | 90.20  | 100.00  | 74.73  | 97.01  | 53.73  | 99.04  | 71.77
L240: Gemini-3-Pro    | -  | 100.00  | 94.12  | 100.00  | 85.71  | 100.00  | 62.69  | 100.00  | 80.38
L241: Qwen3-Max  | -  | 96.08  | 86.27  | 93.41  | 54.95  | 86.57  | 37.31  | 91.87  | 56.94
L242: Mistral-Medium-3.1  | -  | 100.00  | 78.43  | 87.91  | 52.75  | 77.61  | 19.40  | 87.56  | 48.33
L243: DeepSeek-3.2  | 685B (37B)  | 96.08  | 80.39  | 96.70  | 64.84  | 85.07  | 41.79  | 92.82  | 61.24
L244: Qwen3-Coder-Plus  | 480B (35B)  | 92.16  | 80.39  | 91.21  | 60.44  | 77.61  | 29.85  | 87.08  | 55.50
L245: LLaMA-4-Maverick  | 402B (17B)  | 100.00  | 86.27  | 85.71  | 53.85  | 76.12  | 32.84  | 86.12  | 55.02
L246: GLM-4.7      | 358B (32B)  | 96.08  | 90.20  | 86.81  | 70.33  | 71.64  | 44.78  | 84.21  | 66.99
L247: Devstral-2  | 123B  | 98.04  | 80.39  | 91.21  | 58.24  | 67.16  | 25.37  | 85.17  | 53.11
L248: Ministral-3-14B    | 14B  | 94.12  | 70.59  | 71.43  | 29.67  | 55.22  | 11.94  | 71.77  | 33.97
L249: QiMeng-SALV  | 7B  | 96.08  | 66.67  | 95.60  | 53.85  | 88.06  | 22.39  | 93.30  | 46.89
L250: RTL-Coder  | 6.7B  | 94.12  | 64.71  | 83.52  | 29.67  | 65.67  | 5.97  | 80.38  | 30.62
L251: CodeV-R1    | 7B  | 88.24  | 74.51  | 92.31  | 54.95  | 64.18  | 23.88  | 82.30  | 49.76
L252: VeriLogos  | 7B  | 86.27  | 49.02  | 90.11  | 26.37  | 71.64  | 1.49  | 83.25  | 23.92
L253: Single Agent Systems (w. Simulator Feedback & Iterative Fix)
L254: ---
L255: w. GPT-5.2  | -  | 100.00  | 96.08  | 100.00  | 81.32  | 100.00  | 59.70  | 100.00  | 77.99
L256: w. Gemini-3-Pro  | -  | 100.00  | 96.08  | 100.00  | 86.81  | 100.00  | 70.15  | 100.00  | 83.73
L257: w. Qwen3-Max  | -  | 100.00  | 94.12  | 92.31  | 68.13  | 89.55  | 44.78  | 93.30  | 66.99
L258: w. Mistral-Medium-3.1  | -  | 98.04  | 78.43  | 95.60  | 56.04  | 89.55  | 31.34  | 94.26  | 53.59
L259: w. DeepSeek-3.2  | 685B (37B)  | 100.00  | 84.31  | 97.80  | 67.03  | 94.03  | 44.78  | 97.13  | 64.11
L260: w. Qwen3-Coder-Plus  | 480B (35B)  | 98.04  | 80.39  | 93.41  | 63.74  | 88.06  | 31.34  | 92.82  | 57.42
L261: w. LLaMA-4-Maverick  | 402B (17B)  | 100.00  | 92.16  | 91.21  | 59.34  | 79.10  | 32.84  | 89.47  | 58.85
L262: w. GLM-4.7  | 358B (32B)  | 98.04  | 94.12  | 96.70  | 81.32  | 92.54  | 58.21  | 95.69  | 77.03
L263: w. Devstral-2  | 123B  | 100.00  | 78.43  | 94.51  | 57.14  | 88.06  | 34.33  | 93.78  | 55.02
L264: w. Ministral-3-14B  | 14B  | 94.12  | 76.47  | 79.12  | 48.35  | 55.22  | 19.40  | 75.12  | 45.93
L265: w. QiMeng-SALV  | 7B  | 98.04  | 74.51  | 94.51  | 51.65  | 88.06  | 17.91  | 93.30  | 46.41
L266: w. RTL-Coder  | 6.7B  | 84.31  | 56.86  | 80.22  | 38.46  | 70.15  | 8.96  | 77.99  | 33.49
L267: w. CodeV-R1  | 7B  | 98.04  | 84.31  | 97.80  | 61.54  | 85.07  | 32.84  | 93.78  | 57.89
L268: w. VeriLogos  | 7B  | 96.08  | 56.86  | 86.81  | 24.18  | 82.09  | 4.48  | 87.56  | 25.84
L269: Multi Agents Systems
L270: ---
L271: MAGE (w. GPT-5.2)  | -  | 100.00  | 96.08  | 100.00  | 95.60  | 98.51  | 77.61  | 99.52  | 89.95
L272: VerilogCoder (w. GPT-5.2)  | -  | 100.00  | 94.12  | 100.00  | 90.11  | 100.00  | 68.66  | 100.00  | 84.21
L273: Veri-Sure (w. DS-3.2)  | 685B (37B)  | 100.00  | 90.20  | 98.90  | 73.63  | 97.01  | 53.73  | 98.56  | 71.29
L274: Veri-Sure (w. GPT-5.2)  | -  | 100.00  | 100.00  | 100.00  | 95.60  | 100.00  | 85.07  | 100.00  | 93.30
L275: cite127†Image: Refer to caption Figure 5: Case study: formal-hint-guided debugging in Veri-Sure. Boolean Proofer and Asserter agents help generate correct RTL code.
L276: cite126†Table 1 reports the Pass@1 for syntax and functional correctness on VerilogEval-v2-EXT, further broken down by difficulty. We observe these key things:
L277: Frontier closed models are strong out of the box: Among standalone LLMs, commercial closed-source models deliver consistently high syntax success and strong functional accuracy, especially on Medium and Hard tasks. This suggests that large-scale general pretraining already confers substantial competence in RTL code generation and code-level reasoning, even without hardware-specific fine-tuning.
L278: Specialized small models lag behind general large models: In contrast, smaller models that are fine-tuned for RTL code generation do not necessarily outperform state-of-the-art general-purpose large models. While these models often achieve reasonable syntax rates, their functional pass rates are markedly lower on the harder tasks, indicating that parameter scale and broad pretraining remain critical for multi-step temporal reasoning, corner cases, and control-heavy designs.

