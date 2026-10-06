# 独立准入校准：2601.19451v1

原完整题摘记录：AB3.md。仅用于定点准入，不代表日期或必要证据审阅完成。

[2601.19451v1] Dynamic Multi-Expert Projectors with Stabilized Routing for Multilingual Speech Recognition
 Abstract: Recent advances in LLM-based ASR connect frozen speech encoders with Large Language Models (LLMs) via lightweight projectors. While effective in monolingual settings, a single projector struggles to capture the diverse acoustic-to-semantic mappings required for multilingual ASR. To address this, we propose SMEAR-MoE, a stabilized Mixture-of-Experts projector that ensures dense gradient flow to all experts, preventing expert collapse while enabling cross-lingual sharing. We systematically compare monolithic, static multi-projector, and dynamic MoE designs across four Indic languages (Hindi, Marathi, Tamil, Telugu). Our SMEAR-MoE achieves strong performance, delivering upto a 7.6% relative WER reduction over the single-projector baseline, while maintaining comparable runtime efficiency. Analysis of expert routing further shows linguistically meaningful specialization, with related languages sharing experts. These results demonstrate that stable multi-expert projectors are key to scalable and robust multilingual ASR. 
 Submission history From: Isha Pandey [ view email ] [v1] Tue, 27 Jan 2026 10:37:03 UTC (608 KB) 


