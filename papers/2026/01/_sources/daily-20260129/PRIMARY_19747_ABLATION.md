# Exact-v1 necessary ablation response — 19747

Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation (https://arxiv.org/html/2601.19747v1)
citeturn28469view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19747v1","pattern":"Ablation"}); Total lines: 942
L278: Specialized small models lag behind general large models: In contrast, smaller models that are fine-tuned for RTL code generation do not necessarily outperform state-of-the-art general-purpose large models. While these models often achieve reasonable syntax rates, their functional pass rates are markedly lower on the harder tasks, indicating that parameter scale and broad pretraining remain critical for multi-step temporal reasoning, corner cases, and control-heavy designs.
L279: Practically, this gap is difficult to close by fine-tuning alone because training large backbones is compute intensive.
L280: Feedback improves results, but gains vary by backbone: Simply feeding simulator logs back to the same model, improves syntax and functional accuracy across all tested backbones, but the magnitude is model-dependent. Stronger models tend to benefit modestly, while weaker or less robust models can gain substantially.
L281: Multi-agent approaches are effective; Veri-Sure performs best: Multi-agent frameworks (MAGE and VerilogCoder, controlled to use GPT-5.2) generally outperform both standalone inference and single-agent feedback, highlighting the value of curated tool use and role specialization. Veri-Sure achieves the best overall functional Pass@1 (93.30%) with perfect syntax, and the largest advantage on Hard tasks (85.07% functional).
L282: It also boosts the open-weight MoE backbone DeepSeek-3.2 to 71.29% overall functional Pass@1 (+10.05 pp over standalone; +7.18 pp over single-agent feedback).
L283: ### 5.3 Ablation Results
L284: Table 2: Ablation results of Veri-Sure on VerilogEval-v2-EXT (Func. Pass@1, %). Base model: GPT-5.2. Subscripts denote absolute drop in percentage points vs. the full framework.
L285: Variant  | Hard  | Overall
L286: GPT-5.2 (Standalone)  | 59.70_{↓25.4}  | 76.56_{↓16.7}
L287: + Simulator Feedback & Fix  | 59.70_{↓25.4}  | 77.99_{↓15.3}
L288: Veri-Sure (full)  | 85.07  | 93.30
L289: w/o Contract (Architect Agent)  | 82.09_{↓3.0}  | 90.43_{↓2.9}
L290: w/o Tracing, Slicing & Patching  | 68.66_{↓16.4}  | 82.30_{↓11.0}
L291: w/o Formal Verification  | 73.13_{↓11.9}  | 89.47_{↓3.8}
L292: cite128†Table 2 isolates the contribution of each major Veri-Sure component. Overall, Veri-Sure achieves 93.30% functional pass rate, improving substantially over GPT-5.2 standalone (76.56%) and simulator-feedback loop (77.99%), especially on hard problems (85.07% vs. 59.70%). Results also indicate that feedback alone is insufficient for hard RTL tasks, and that most gains come from structured agentic verification and repair.
L293: Generally, removing any major component of Veri-Sure degrades performance. The most critical part is the Tracing, Slicing & Patching mechanism, disabling it causes the largest drop, showing that precise localization and targeted repairs dominate end-to-end accuracy. For Hard problems, Formal Verification is also important: removing it reduces pass rate from 85.07% to 73.13% (-11.9 pp), indicating that proof-based feedback could help debug deep logical bugs that may not surface under finite simulation.
L294: ### 5.4 Case Study
L295: In cite129†Figure 5 , we illustrate how Veri-Sure converts failing executions into formal-hint-guided repairs. For an 8$\times$8 two’s-complement multiplier (top), the Boolean Proofer derives the contract-level Boolean model and proves inequivalence against the generated RTL via a SymbiYosys miter, pinpointing the missing sign-bit contribution of $b[7]$ and enabling a minimal patch to the partial-product logic.
L296: For a control-heavy history-register block (bottom), the Asserter injects a clock/reset assertion that triggers at the first violating cycle and reports the implicated signals/values, guiding the Debugger to fix the edge/reset handling without regenerating the whole module. More detailed case studies can be found in cite64†Appendix C .
L297: ## 6 Conclusion
L298: In this work, we present Veri-Sure, a contract-aware multi-agent framework that closes the RTL development loop by aligning generation with verification and localized repair. By distilling natural-language intent into a shared design contract, Veri-Sure mitigates semantic drift across agents, while its waveform tracing and static slicing mechanisms enable precise patching that avoids whole-file rewrites and reduces regression risk.
L299: Beyond simulation-centric evaluation, we integrated formal verification to achieve better debugging capability. To measure progress on realistic RTL tasks, we also introduced VerilogEval-v2-EXT, including 53 more industrial-grade problems and difficulty stratification. Experiments show that Veri-Sure achieves state-of-the-art verified-correct performance, reaching 93.30% overall functional pass rate; ablations confirm that the gains come primarily from our debugging pipeline.

