# Exact-v1 primary cached excerpts — 2601.19747

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Original response 1: latepoint0

Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation (https://arxiv.org/html/2601.19747v1)
citeturn28181view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19747v1","lineno":null}); Total lines: 942


## Original response 2: latepoint4

Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation (https://arxiv.org/html/2601.19747v1)
citeturn28186view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19747v1","lineno":164}); Total lines: 942
L153: We propose Veri-Sure, a multi-agent framework that brings a real EDA-style closed loop for development and testing to RTL synthesis from natural language. Rather than treating generation as a one-shot translation problem, Veri-Sure tightly couples code synthesis with automated validation and actionable debugging signals.
L154: Unlike prior multi-agent systems that primarily coordinate through natural-language context and thus risk specification drift and coarse, regression-prone rewrites, Veri-Sure uses trace-driven analysis to localize failures to concrete time windows, signals, and violated requirements, enabling targeted fixes and improving robustness on multi-cycle corner cases. It also integrates simulation with formal checks to continuously enforce design requirements and help debugging.
L155: ### 3.1 Overall Architecture
L156: cite108†Figure 1 shows the workflow of Veri-Sure. The process starts with (1) an Architect agent, which distills the user prompt into a structured JSON-format design contract, capturing the Device Under Test (DUT) interface (ports, clock/reset conventions), key parameters, and cycle-accurate behavioral requirements. When a reference testbench is available, the Architect cross-checks interface and timing details to reduce ambiguity.
L157: Based on this specification, (2) a Verifier agent produces a self-checking testbench whose stimuli and checkers are aligned with the specified requirements. In parallel, (3) a Coder agent generates synthesizable RTL code conditioned on the same specification. We then invoke Verilator to compile and simulate the code against testbench; designs are accepted only if all checks pass.
L158: When compilation or simulation fails, Veri-Sure enters an autonomous debugging loop led by (4) a Debugger agent. Rather than relying solely on textual error messages, the Debugger leverages trace-driven temporal diagnosis: it analyzes logs and waveforms via our slicing mechanism to localize failures to concrete time windows and a minimal set of relevant signals.
L159: To further sharpen the feedback signal, (5) an Asserter agent generates targeted temporal assertions to expose sequential/protocol violations, while (6) a Boolean Proofer agent performs a checking of localized combinational constraints to validate candidate fixes and prevent regressions. The Debugger aggregates these signals to apply minimal, localized edits to the RTL code and iterates until all verification checks are satisfied.
L160: ### 3.2 Contract Design
L161: 
L162: Natural-language RTL specifications are often underspecified in details like reset polarity, sampling edge, or cycle latency, which easily leads to inconsistent interpretations across agents. Veri-Sure mitigates this by having the Architect agent compile the prompt into a compact, structured design contract that makes such choices explicit before any code is written.
L163: The resulting contract is intentionally compact yet sufficient to drive the pipeline: it records the chosen source of truth, a typed module interface, clock/reset and sequential semantics, per-output latency, a precise functional summary with corner cases, a directed test plan, and guidance for the verifier, coder, and debugger. When the prompt underspecifies details, the Architect makes assumptions explicit so they become checkable requirements.
L164: A lightweight contract linter then validates the schema and basic consistency, preventing malformed or contradictory contracts from propagating into code generation and verification.
L165: ### 3.3 Tracing, Static Slicing & Patching
L166: 
L167: cite109†Image: Refer to caption Figure 2: The tracing, static slicing and patching mechanism.
L168: When simulation fails, the main challenge is to turn an opaque mismatch count into a minimal, actionable edit without destabilizing unrelated logic. Veri-Sure addresses this with a closed-loop debugging pipeline that couples dynamic evidence (i.e. waveforms) with static structure (i.e. code dependencies), producing a patching task for the Debugger rather than a full-file rewrite, as shown in cite110†Figure 2 .
L169: #### Trace-driven Temporal Analysis
L170: 
L171: From the simulator log we identify the earliest divergence time and the signals responsible. Let $\mathbf{O}_{\mathrm{DUT}}(t)$ and $\mathbf{O}_{\mathrm{exp}}(t)$ denote the observed and expected output vectors at time $t$; we define
L172: 
L173:  | $$t_{f}\;=\;\min\{\,t\mid\mathbf{O}_{\mathrm{DUT}}(t)\neq\mathbf{O}_{\mathrm{exp}}(t)\,\}.$$  |  | (1)
L174: We then extract a short waveform window ending at $t_{f}$ from the Value Change Dump (VCD) file and sample it on the contract-defined clocking scheme. In addition to raw values, the trace reporter runs a lightweight alignment check to detect systematic off-by-one-cycle or wrong-edge bugs by testing small shifts and reporting the best-matching offset as a timing hint. All findings are summarized into a trace report, including failing signals, the failure cycle, and the relevant trace slice.
L175: #### Static Dependency Slicing
L176: 
L177: To avoid unfocused edits, the trace slicer restricts attention to the cone of logic that can influence the failing outputs. We parse the RTL into semantic blocks, for example using continuous assignments and always blocks, and compute per-block read/write sets $R(B)$ and $W(B)$. A dependency edge exists when a block reads what another writes:
L178: 
L179:  | $$B_{j}\leftarrow B_{i}\quad\Leftrightarrow\quad R(B_{j})\cap W(B_{i})\neq\varnothing.$$  |  | (2)
L180: Starting from the failing signals as seeds, we perform a bounded backward traversal to obtain a small suspect set $\mathcal{B}_{\mathrm{sus}}$ with block identifiers and line ranges. This converts “the output mismatched” into “these few blocks are the plausible causes,” dramatically shrinking the search space presented to the Debugger.
L181: #### Localized Patching
L182: The Debugger is only allowed to edit blocks in $\mathcal{B}_{\mathrm{sus}}$ via block-level read/replace operations; the rest of the file is preserved verbatim. Each patch is immediately checked by recompilation and re-simulation, and we apply a simple rollback rule to prevent regressions.
L183: Writing $\sigma(\mathrm{RTL})=(t_{f},m)$ for the first-failure time and total mismatch count, we keep a patch only if it improves the failure signature, which means later first failure, or fewer mismatches at the same $t_{f}$; otherwise we revert. This loop grounds the repair process in concrete traces while maintaining stability across iterations.
L184: ### 3.4 Formal Verification
L185: 
L186: Simulation provides concrete counterexamples but offers limited coverage and often weak diagnostic signal. Veri-Sure therefore augments the debugging loop with a two-branch, contract-driven verification pipeline: an Asserter for sequential/timing obligations and a Boolean Proofer for combinational equivalence. From the design contract $\widehat{C}$, we derive a small set of checkable obligations:
L187:  | $$\Phi\;=\;\mathcal{P}(\widehat{C})\;=\;\Phi_{\mathrm{seq}}\cup\Phi_{\mathrm{comb}},$$  |  | (3)
L188: 
L189: which are then discharged by the two verifiers and translated into structured hints for the Debugger.
L190: #### Asserter for Timing Supervision
L191: 
L192: Using clock/reset semantics and latency annotations in $\widehat{C}$, the Asserter generates a small set of non-intrusive SystemVerilog assertions and attaches them to the DUT via binding. Assertions run under Verilator and report violations with type, implicated signals, and time, effectively diagnosing issues such as wrong-edge sampling, reset mismatches, and off-by-one-cycle latency.
L193: #### Boolean Proofer for Combinational Equivalence
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

