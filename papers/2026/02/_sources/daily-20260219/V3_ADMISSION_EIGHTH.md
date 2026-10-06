# 第八批完整题摘与贡献校准

本日有限具体线索，未因安全标签或主线映射自动采用。当前v1题摘直接复用原身份，v2受影响两项用已恢复v1；未启动无关附件队列。

## 2602.15513v1 — HIMM: Human-Inspired Long-Term Memory Modeling for Embodied Exploration and Question Answering

[精确v1](https://arxiv.org/html/2602.15513v1)

Deploying Multimodal Large Language Models as the brain of embodied agents remains challenging, particularly under long-horizon observations and limited context budgets. Existing memory assisted methods often rely on textual summaries, which discard rich visual and spatial details and remain brittle in non-stationary environments. In this work, we propose a non-parametric memory framework that explicitly disentangles episodic and semantic memory for embodied exploration and question answering. Our retrieval-first, reasoning-assisted paradigm recalls episodic experiences via semantic similarity and verifies them through visual reasoning, enabling robust reuse of past observations without rigid geometric alignment. In parallel, we introduce a program-style rule extraction mechanism that converts experiences into structured, reusable semantic memory, facilitating cross-environment generalization. Extensive experiments demonstrate state-of-the-art performance on embodied question answering and exploration benchmarks, yielding a 7.3% gain in LLM-Match and an 11.4% gain in LLM MatchXSPL on A-EQA, as well as +7.7% success rate and +6.8% SPL on GOAT-Bench. Analyses reveal that our episodic memory primarily improves exploration efficiency, while semantic memory strengthens complex reasoning of embodied agents.

准入理由：text-summary丢视觉/空间且跨环境易脆→episodic先similarity再visual verification、经验提program rules的不同读写→直接视觉证据与derived rules的迁移/治理选择要分账。

## 2602.15515v1 — The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

[精确v1](https://arxiv.org/html/2602.15515v1)

Training against white-box deception detectors has been proposed as a way to make AI systems honest. However, such training risks models learning to obfuscate their deception to evade the detector. Prior work has studied obfuscation only in artificial settings where models were directly rewarded for harmful output. We construct a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and show that obfuscation emerges in this setting. We introduce a taxonomy of possible outcomes when training against a deception detector. The model either remains honest, or becomes deceptive via two possible obfuscation strategies. (i) Obfuscated activations : the model outputs deceptive text while modifying its internal representations to no longer trigger the detector. (ii) Obfuscated policy : the model outputs deceptive text that evades the detector, typically by including a justification for the reward hack. Empirically, obfuscated activations arise from representation drift during RL, with or without a detector penalty. The detector penalty only incentivizes obfuscated policies; we theoretically show this is expected for policy gradient methods. Sufficiently high KL regularization and detector penalty can yield honest policies, establishing white-box deception detectors as viable training signals for tasks prone to reward hacking.

准入理由：惩罚white-box deception detector被误作honesty真值→真实coding rewardhack中分activation drift与policy evasion，policygradient对两者激励不同→安全sensor训练能改变policy但仍需独立行为验收。

## 2602.15549v1 — VLM-DEWM: Dynamic External World Model for Verifiable and Resilient Vision-Language Planning in Manufacturing

[精确v1](https://arxiv.org/html/2602.15549v1)

Vision-language model (VLM) shows promise for high-level planning in smart manufacturing, yet their deployment in dynamic workcells faces two critical challenges: (1) stateless operation, they cannot persistently track out-of-view states, causing world-state drift; and (2) opaque reasoning, failures are difficult to diagnose, leading to costly blind retries. This paper presents VLM-DEWM, a cognitive architecture that decouples VLM reasoning from world-state management through a persistent, queryable Dynamic External World Model (DEWM). Each VLM decision is structured into an Externalizable Reasoning Trace (ERT), comprising action proposal, world belief, and causal assumption, which is validated against DEWM before execution. When failures occur, discrepancy analysis between predicted and observed states enables targeted recovery instead of global replanning. We evaluate VLM-DEWM on multi-station assembly, large-scale facility exploration, and real-robot recovery under induced failures. Compared to baseline memory-augmented VLM systems, VLM DEWM improves state-tracking accuracy from 56% to 93%, increases recovery success rate from below 5% to 95%, and significantly reduces computational overhead through structured memory. These results establish VLM-DEWM as a verifiable and resilient solution for long-horizon robotic operations in dynamic manufacturing environments.

准入理由：VLM工作记忆无法决定out-of-view worldstate真值→外部persistent/queryable DEWM配typed action-belief-causal trace与predicted-observed discrepancy→世界状态owner/执行前核验/定点recovery需区分模型推断。

## 2602.15602v1 — Certified Per-Instance Unlearning Using Individual Sensitivity Bounds

[精确v1](https://arxiv.org/html/2602.15602v1)

Certified machine unlearning can be achieved via noise injection leading to differential privacy guarantees, where noise is calibrated to worst-case sensitivity. Such conservative calibration often results in performance degradation, limiting practical applicability. In this work, we investigate an alternative approach based on adaptive per-instance noise calibration tailored to the individual contribution of each data point to the learned solution. This raises the following challenge: how can one establish formal unlearning guarantees when the mechanism depends on the specific point to be removed? To define individual data point sensitivities in noisy gradient dynamics, we consider the use of per-instance differential privacy. For ridge regression trained via Langevin dynamics, we derive high-probability per-instance sensitivity bounds, yielding certified unlearning with substantially less noise injection. We corroborate our theoretical findings through experiments in linear settings and provide further empirical evidence on the relevance of the approach in deep learning settings.

准入理由：全局worstcase deletionnoise代价过大→individual sensitivity/per-instance DP限定Langevin ridgeunlearning→低噪声只特定实例/机制边界，不让deep empirical继承formalcertificate。

## 2602.15654v1 — Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections

[精确v1](https://arxiv.org/html/2602.15654v1)

Self-evolving LLM agents update their internal state across sessions, often by writing and reusing long-term memory. This design improves performance on long-horizon tasks but creates a security risk: untrusted external content observed during a benign session can be stored as memory and later treated as instruction. We study this risk and formalize a persistent attack we call a Zombie Agent, where an attacker covertly implants a payload that survives across sessions, effectively turning the agent into a puppet of the attacker.
 We present a black-box attack framework that uses only indirect exposure through attacker-controlled web content. The attack has two phases. During infection, the agent reads a poisoned source while completing a benign task and writes the payload into long-term memory through its normal update process. During trigger, the payload is retrieved or carried forward and causes unauthorized tool behavior. We design mechanism-specific persistence strategies for common memory implementations, including sliding-window and retrieval-augmented memory, to resist truncation and relevance filtering. We evaluate the attack on representative agent setups and tasks, measuring both persistence over time and the ability to induce unauthorized actions while preserving benign task quality. Our results show that memory evolution can convert one-time indirect injection into persistent compromise, which suggests that defenses focused only on per-session prompt filtering are not sufficient for self-evolving agents.

准入理由：per-session过滤未覆盖状态演化→正常webread/write途径感染+适配window/retrieval persistence并触发unauthorizedtools→写入/回读/执行跨session职责与普通入库条件要核。

## 2602.15756v1 — A Note on Non-Composability of Layerwise Approximate Verification for Neural Inference

[精确v1](https://arxiv.org/html/2602.15756v1)

A natural and informal approach to verifiable (or zero-knowledge) ML inference over floating-point data is: “prove that each layer was computed correctly up to tolerance \delta; therefore the final output is a reasonable inference result”. This short note gives a simple counterexample showing that this inference is false in general: for any neural network, we can construct a functionally equivalent network for which adversarially chosen approximation-magnitude errors in individual layer computations suffice to steer the final output arbitrarily (within a prescribed bounded range).

准入理由：每layer δ容差验真被误当final inference可靠→functionallyequivalent network构造可放大adversarial layererror任意boundedoutput→容差协议须全图稳定性/输出metric，layerlocal证明不能直接合成。
