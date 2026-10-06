# 独立准入校准：2601.19487v1

原完整题摘记录：AB3.md。仅用于定点准入，不代表日期或必要证据审阅完成。

[2601.19487v1] LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment
 Abstract: Safety-aligned LLMs suffer from two failure modes: jailbreak (answering harmful inputs) and over-refusal (declining benign queries). Existing vector steering methods adjust the magnitude of answer vectors, but this creates a fundamental trade-off -- reducing jailbreak increases over-refusal and vice versa. We identify the root cause: LLMs encode the decision to answer (answer vector $v_a$) and the judgment of input safety (benign vector $v_b$) as nearly orthogonal directions, treating them as independent processes. We propose LLM-VA, which aligns $v_a$ with $v_b$ through closed-form weight updates, making the model&#39;s willingness to answer causally dependent on its safety assessment -- without fine-tuning or architectural changes. Our method identifies vectors at each layer using SVMs, selects safety-relevant layers, and iteratively aligns vectors via minimum-norm weight modifications. Experiments on 12 LLMs demonstrate that LLM-VA achieves 11.45% higher F1 than the best baseline while preserving 95.92% utility, and automatically adapts to each model&#39;s safety bias without manual tuning. Code and models are available at this https URL . 
 Submission history From: Haonan Zhang [ view email ] [v1] Tue, 27 Jan 2026 11:19:19 UTC (789 KB) [v2] Mon, 4 May 2026 07:11:05 UTC (577 KB) 


