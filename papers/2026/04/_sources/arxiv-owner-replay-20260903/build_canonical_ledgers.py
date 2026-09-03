#!/usr/bin/env python3
"""Build date-correct canonical candidate ledgers and reviews for Apr/May."""

from __future__ import annotations

import hashlib
import html
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path("/Users/apple/Documents/Work/PycharmProject/AI-System-Design")

# Fresh-context semantic audit decisions for the families recovered by the
# initial-created owner replay.  Keeping the assessment explicit prevents the
# renderer from silently converting keyword matches into Score V2 judgments.
REVIEW_DECISIONS = {
    "2603.28768": ("MODEL-MOE", (3, 3, 2)), "2603.28769": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 2)),
    "2603.28780": ("TRAIN-DISTRIBUTED-TRAINING", (2, 3, 2)), "2603.28781": ("PLATFORM-MONITORING", (3, 3, 2)),
    "2603.28793": ("INFER-TENSORRT-LLM", (2, 3, 2)), "2603.28795": ("INFER-KV-CACHE", (3, 3, 2)),
    "2603.28815": ("PLATFORM-EVALUATION-SYSTEM", (2, 3, 2)), "2603.28823": ("WORLDVIEW-SCALING-LAW", (2, 3, 2)),
    "2603.28887": ("MULTIMODAL-WORLD-MODELS", (2, 3, 2)), "2603.28963": ("MULTIMODAL-WORLD-MODELS", (2, 3, 2)),
    "2603.28988": ("PLATFORM-SECURITY", (3, 3, 2)), "2603.29002": ("INFER-KV-CACHE", (3, 3, 2)),
    "2603.29010": ("INFER-TENSORRT-LLM", (2, 2, 2)), "2603.29020": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2)),
    "2603.29090": ("MULTIMODAL-WORLD-MODELS", (2, 2, 1)), "2603.29848": ("PLATFORM-MONITORING", (2, 2, 2)),
    "2604.02340": ("MULTIMODAL-GENERATIVE-PARADIGMS", (2, 3, 2)), "2604.02344": ("INFER-TENSORRT-LLM", (2, 2, 2)),
    "2604.02367": ("INFER-SCHEDULING", (2, 2, 2)), "2604.03258": ("INFER-TENSORRT-LLM", (2, 2, 2)),
    "2604.03270": ("INFER-KV-CACHE", (3, 2, 2)), "2604.03295": ("AGENT-MEMORY", (2, 2, 2)),
    "2604.08565": ("TRAIN-PRETRAINING", (2, 2, 2)), "2604.08584": ("MODEL-SELF-ATTENTION", (2, 2, 2)),
    "2604.08585": ("INFER-KV-CACHE", (3, 2, 2)), "2604.09557": ("INFER-SPECULATIVE-DECODING", (2, 2, 2)),
    "2604.09562": ("INFER-SPECULATIVE-DECODING", (3, 3, 2)), "2604.09580": ("MULTIMODAL-WORLD-MODELS", (2, 3, 2)),
    "2604.09587": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2)), "2604.09588": ("AGENT-MEMORY", (2, 2, 1)),
    "2604.09603": ("INFER-SPECULATIVE-DECODING", (3, 2, 2)), "2604.09611": ("PLATFORM-COST", (2, 3, 2)),
    "2604.09651": ("PLATFORM-SECURITY", (3, 2, 2)), "2604.13055": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 1)),
    "2604.13064": ("PLATFORM-SECURITY", (2, 2, 2)), "2604.13072": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2)),
    "2604.14170": ("AGENT-RAG", (2, 2, 2)), "2604.14178": ("AGENT-PLATFORM", (2, 2, 1)),
    "2604.16310": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 1)), "2604.16331": ("AGENT-MEMORY", (2, 2, 2)),
    "2604.16368": ("INFER-SPECULATIVE-DECODING", (2, 2, 1)), "2604.16385": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2)),
    "2604.16395": ("INFER-PREFILL", (3, 2, 2)), "2604.18592": ("INFER-SCHEDULING", (2, 2, 2)),
    "2604.19752": ("PLATFORM-SECURITY", (2, 2, 2)), "2604.19769": ("INFER-KV-CACHE", (3, 2, 2)),
    "2604.19780": ("INFER-SCHEDULING", (2, 2, 2)), "2604.20854": ("AGENT-RAG", (2, 2, 2)),
    "2604.20860": ("INFER-SCHEDULING", (3, 2, 2)),
    "2605.00831": ("INFER-GPU-MEMORY", (3, 2, 2)), "2605.00873": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 1)),
    "2605.02905": ("INFER-KV-CACHE", (2, 2, 2)), "2605.04069": ("INFER-KV-CACHE", (2, 2, 2)),
    "2605.04075": ("INFER-KV-CACHE", (2, 2, 2)), "2605.04084": ("INFER-TENSORRT-LLM", (2, 2, 2)),
    "2605.05219": ("INFER-KV-CACHE", (3, 3, 2)), "2605.05222": ("INFER-SCHEDULING", (2, 2, 2)),
    "2605.05225": ("MODEL-MOE", (2, 2, 2)), "2605.06675": ("INFER-KV-CACHE", (3, 2, 2)),
    "2605.06676": ("INFER-KV-CACHE", (3, 2, 2)), "2605.10312": ("INFER-GPU-MEMORY", (3, 2, 2)),
    "2605.12530": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2)), "2605.13848": ("AGENT-WORKFLOW", (2, 2, 2)),
    "2605.13851": ("PLATFORM-SECURITY", (3, 2, 2)), "2605.15204": ("AGENT-MULTI-AGENT", (3, 2, 2)),
    "2605.16265": ("PLATFORM-SECURITY", (3, 2, 2)), "2605.18755": ("PLATFORM-MONITORING", (3, 2, 2)),
    "2605.18762": ("PLATFORM-SECURITY", (3, 2, 2)), "2605.19755": ("PLATFORM-SECURITY", (3, 3, 2)),
    "2605.20196": ("WORLDVIEW-SCALING-LAW", (2, 2, 2)), "2605.23911": ("INFER-TENSORRT-LLM", (3, 2, 2)),
    "2605.23918": ("PLATFORM-COST", (2, 3, 2)), "2605.23935": ("PLATFORM-SECURITY", (3, 2, 2)),
    "2605.25310": ("AGENT-TOOL-CALLING", (2, 2, 1)), "2605.26118": ("INFER-TENSORRT-LLM", (2, 2, 2)),
    "2605.26120": ("TRAIN-DISTRIBUTED-TRAINING", (2, 2, 2)), "2605.26440": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 1)),
    "2605.26444": ("INFER-SPECULATIVE-DECODING", (3, 2, 2)), "2605.27390": ("INFER-SPECULATIVE-DECODING", (3, 2, 2)),
}

# Hand-reviewed replacements for cases where generic sentence extraction
# selected navigation text instead of an evidence-bearing paragraph.  These
# remain exact-v1-bounded and are deliberately narrow about generality.
REVIEW_TEXT_OVERRIDES = {
    "2603.28781": {
        "mechanism_and_ownership": (
            "框架联合建模两类信号：GPU 数值遥测中的 utilization-aware thermal drift，以及监控管道的 scrape latency、sample loss、"
            "time-series gap 和 device-metric disappearance。设备/调度状态仍由基础设施持有，检测器只对数值与结构性可观测性退化生成预警。"
        ),
        "evaluation_contract": (
            "作者使用 GWDG 生产遥测切片：7 个节点、每节点 4 张 GPU、约 353 天观测，数值采样中位间隔约 600 秒；"
            "detachment 子集中 7 起事件只有 5 起具有完整 tidy telemetry 并进入处理，并以 Isolation Forest、One-Class SVM 和 joint detector 比较预警行为。"
        ),
        "tradeoffs_and_failure_modes": (
            "结构信号能覆盖数值仍正常但设备已从监控面消失的故障，却依赖 scheduler state、恢复动作和维护事件来区分真实 pre-fault、良性 workload 变化与 post-failure artifact。"
            "joint detector 还可能产生更碎片化的 alert run、提高 triage 成本；当前单站点、少量完整 detachment 事件不能证明跨集群或其他硬件故障的泛化。"
        ),
    },
    "2603.28815": {
        "mechanism_and_ownership": (
            "SkillTester 对同一任务和环境执行 matched no-skill 与 with-skill 两条路径，记录 skill 是否实际被调用，并把成功与效率差异归一化为 utility；"
            "安全性由独立 probe suite 评估，再汇总为 security score 与三级状态。执行 artifact 属于评测 harness，发布层只输出压缩后的可解释结果。"
        ),
        "evaluation_contract": (
            "该 exact-v1 technical report 定义比较设计、utility/security 维度、timeout/failure 记账和初始阈值，但没有披露足以支持跨 skill corpus 的完整独立 benchmark 结果。"
            "因此它证明的是 evaluation contract 与公开工具接口，不是某类 skill 已被普遍验证为安全或有用。"
        ),
        "tradeoffs_and_failure_modes": (
            "成对执行提供反事实基线，但至少翻倍任务运行成本，并受模型随机性、环境漂移和 skill 实际触发率影响；timeout 等未完成尝试按失败计入，会把基础设施故障与 skill 缺陷混在一起。"
            "utility mapping 与 security-status 阈值只是初始 operational defaults，作者明确留待更广 skill corpus、人类判断和长期 regression evidence 校准。"
        ),
    },
    "2604.14170": {
        "old_path_and_changed_constraint": (
            "单轮或多轮但无持久证据状态的 RAG 通常把检索结果作为扁平上下文拼接；当证据噪声高、信息不完整或相互冲突时，"
            "这种路径难以保留证据角色、缺口和反证，也无法让下一轮检索继承可审计的推理状态。"
        ),
        "mechanism_and_ownership": (
            "方案把文档转为包含 relevance、summary、evidence 与 confidence 的 Structured Reasoning Unit，"
            "由持久对比证据池持有支持、背景及无关证据；deficiency analysis 生成缺口、冲突与负约束来驱动后续查询，"
            "并以自适应停止或 abstention 结束迭代。证据状态属于检索编排层，而非模型权重。"
        ),
        "evaluation_contract": (
            "作者在 StrategyQA、ASQA、Natural Questions、2WikiMultiHopQA 与 HotpotQA 上，以 EM、F1 或 ACC 与多种 RAG baseline 比较，"
            "并在 Natural Questions 和 HotpotQA 的 top-5 结果中注入约 30%、50%、70% 随机无关文档进行噪声测试。"
            "实验使用论文披露的 DPR checkpoint；硬件、并发与线上 SLO 未披露。"
        ),
        "tradeoffs_and_failure_modes": (
            "结构化证据池、缺口分析和迭代查询增加 LLM 调用、状态维护与终止判定成本；relevance、confidence 与 sufficiency 仍由同一模型链产生，"
            "不是独立校准的事实概率。论文只验证列出的 QA benchmark 与合成噪声注入，效率、超大语料和真实冲突证据仍是开放问题；"
            "在单跳、低噪声且延迟约束更强时，简单 RAG 仍可能更合适。"
        ),
    },
    "2604.02340": {
        "mechanism_and_ownership": (
            "推理时在同一 masked-diffusion denoising trajectory 上调度分别训练的 heavy 与 light MDLM：早期和晚期 step 可由小模型替换，"
            "中段保留大模型；assignment 是采样 scheduler 的控制状态，不改变底层模型架构，也不依赖 distillation。"
        ),
        "evaluation_contract": (
            "作者在 OpenWebText（并报告 LM1B 扩展）训练的模型上比较 unconditional 与 prefix-conditional generation，"
            "用 generative perplexity、sample diversity、loss/KL step disagreement 及 10 个粗粒度 segment 中选择 4 个的 210 种 schedule 搜索约束结论；"
            "有效 schedule 最高减少约 17% FLOPs，不能等同于所有硬件上的同幅 wall-clock 或能耗下降。"
        ),
        "tradeoffs_and_failure_modes": (
            "收益需要同时保存并调用大小两个 denoiser，增加模型存储、加载和调度复杂度；中段替换会造成更明显质量损失，固定 schedule 也不适配每个样本的难度。"
            "作者指出大规模多尺寸 MDLM family 尚不成熟，结论仍需在更大模型和标准 benchmark 上验证；旧的单模型采样在内存紧张或缺少匹配小模型时仍成立。"
        ),
    },
    "2604.02367": {
        "mechanism_and_ownership": (
            "front-door 方案让单个 1–4B SLM 仅根据原始 prompt、单次前向生成离散 JSON task label，再由外部 routing policy 选择下游模型；"
            "分类模型持有 task signal，部署控制面持有模型候选、成本、延迟、治理约束与最终路由动作，两者不能用分类准确率相互替代。"
        ),
        "evaluation_contract": (
            "Study 1 在相同 Azure T4、vLLM 0.17.1、4-bit NF4 与冻结 60-case corpus 上比较 Phi-3.5-mini、Qwen2.5-1.5B、Qwen2.5-3B；"
            "Study 2 用同一 60 个唯一 case 重复到每 arm 400 次的合成流量，比较无路由、Phi-4-mini、Qwen2.5-3B 与 DeepSeek-V3。"
            "准确率有效样本仍是每 arm 60；没有任何 arm 同时通过预注册 accuracy≥0.85 与 P95≤2000ms viable region。"
        ),
        "tradeoffs_and_failure_modes": (
            "SLM 可降低 front-door 延迟、边际成本与数据外发，但 taxonomy boundary 会成为新的错误面；合成流量、单标注者和重复 deterministic prompt 限制外部有效性。"
            "实验没有执行完整下游路由，因此分类正确不等于输出质量、总成本或业务 SLO 改善；低置信度 fallback 增加第二模型调用与策略复杂度，仍需生产流量验证。"
        ),
    },
    "2604.09611": {
        "mechanism_and_ownership": (
            "研究把多请求应用显式表示为带依赖关系的 workflow，并在统一执行与测量层控制 input/output length、batch size 和 GPU power cap；"
            "应用层持有 request DAG，serving engine 持有 batching/cache/scheduling，Zeus 分别采集 CPU、GPU 与 DRAM 能耗，从而避免把单请求效率直接外推到工作流。"
        ),
        "evaluation_contract": (
            "作者在单张 NVIDIA A100 40GB、CUDA 12.6 的隔离服务器上，以 Llama-2-7B、temperature 0.7、top-p 1.0 运行四类多请求 workload，"
            "每项实验重复十次，并比较 vLLM 与 Parrot；在 document-chain summarization、batch=16 的披露条件下，vLLM 能耗最高低约 28%。"
            "结果不覆盖多 GPU 通信、现代 GQA/MoE/reasoning model 或未测试的 serving stack。"
        ),
        "tradeoffs_and_failure_modes": (
            "更大 batch 和 engine-level utilization 可摊薄能耗，却提高排队与 tail latency；power cap 可节能但牺牲完成时间，workflow-aware scheduling 只有在特定约束下显示相对收益。"
            "单模型单 GPU基线有利于隔离变量，也移除了分布式同步、模型异构与生产流量干扰；Parrot 当时不支持 GQA/MoE，因此框架比较不能视为普遍排名。"
        ),
    },
    "2605.10312": {
        "old_path_and_changed_constraint": (
            "传统 GPU 优化通常在固定依赖图上调整指令顺序或拆分 kernel；当递归计算图的同时存活中间量超过每线程寄存器预算时，"
            "spill 会把原本 compute-bound 的计算推向 HBM memory-bound，单纯调度固定 DAG 已不足以解决问题。"
        ),
        "evaluation_contract": (
            "作者在 NVIDIA A100-80GB、CUDA 12.4 上与 GPU4PySCF 比较：单卡覆盖不同分子规模及 cc-pVDZ/VTZ/VQZ 基组，"
            "报告最高 3.09x、cc-pVQZ 平均 2.4x 的单次 SCF iteration 加速；并在 8 节点 64 张 A100 上对 Ubiquitin/cc-pVTZ "
            "报告 75% parallel efficiency。数字只适用于论文披露的量化化学 workload、baseline 与硬件。"
        ),
        "tradeoffs_and_failure_modes": (
            "方案以专用图生成和两级 kernel 路由换取更低 peak liveness：低阶图尽量保持 register-only，高阶图切换为 shared/global-memory "
            "buffered two-kernel pipeline。后者重新引入 buffer traffic、kernel boundary 与同步成本；路由阈值和收益没有被证明可迁移到其他 GPU、"
            "其他递归图或通用 LLM kernel。"
        ),
    },
    "2605.05222": {
        "old_path_and_changed_constraint": (
            "固定深度 Transformer 为每个 token 执行相同 block 数，控制流规则且便于批处理；但 token 难度不同时，它会在简单 token 上浪费计算，"
            "也无法给困难 token 分配更多深度。"
        ),
        "mechanism_and_ownership": (
            "Token-wise Scaling Architecture 在 block 间学习连续的逐 token residual gate，使每个 token 的残差更新幅度成为可训练状态；"
            "只有稀疏执行实现真正跳过被 gate 抑制的计算，路由决策由模型层产生，runtime 负责兑现 skip。"
        ),
        "evaluation_contract": (
            "实验限于约 5–6M 参数模型、合成任务、Tiny Shakespeare 与 enwik8，并在 Apple M1 Pro 上比较固定深度、early exit、"
            "soft gating 与 sparse-TSA 的质量和吞吐；新增参数约 1.7%，soft gating 开销约 1%。未提供 LLM 规模、GPU 集群或线上 batching/SLO 证据。"
        ),
        "tradeoffs_and_failure_modes": (
            "连续 soft gate 本身不减少 wall-clock FLOPs，必须由稀疏 kernel/runtime 利用 skip 才可能节省计算；逐 token 不规则路径会增加 batching、"
            "load balance 和实现复杂度。规模扩展、训练期内存收益以及 gate 与 token entropy/frequency 的关系仍未解决，因此不能从小模型结果外推到 LLM serving。"
        ),
    },
    "2605.02905": {
        "mechanism_and_ownership": (
            "eOptShrinkQ 先按 token block 对 KV 矩阵执行 optimal singular-value shrinkage，自动识别并单独编码共享的低秩 context 分量；"
            "再用 TurboQuant 逐向量量化保留 token-specific 信息的全秩 residual。若没有 singular value 越过 bulk edge，则跳过 SVD、直接进入 residual quantization。"
        ),
        "evaluation_contract": (
            "作者在 Llama-3.1-8B-Instruct 与 Ministral-8B-Instruct 的各层/attention head 检查谱假设，并用 per-head MSE/inner-product fidelity、LongBench 16 tasks 和 multi-needle retrieval 比较。"
            "在论文配置下约 2.2 bits/entry 的结果优于 3-bit TurboQuant，并接近各自 FP16 baseline；硬件、并发和线上 latency SLO 未形成完整披露合同。"
        ),
        "tradeoffs_and_failure_modes": (
            "低秩分量需要 SVD、额外 factor storage 与独立量化；block 中没有可检测 spike 时只能回退到 TurboQuant，说明收益依赖局部谱结构。"
            "理论保证依赖 spiked random-matrix、thin-shell 与 coordinate-delocalization 假设，LongBench/needle 质量也不能证明生产 decode latency、所有模型或所有 context distribution 上无损。"
        ),
    },
    "2605.12530": {
        "old_path_and_changed_constraint": (
            "标准问答式 fairness benchmark 默认分数稳定反映模型行为，但论文先在 BBQ 与 Difference-Awareness 上观察到：表面 prompt 构造即可显著改变"
            "11 个 3B–70B 开源指令模型的分数与排序，因此静态准确率不足以描述模型在交互中的行为变化。"
        ),
        "mechanism_and_ownership": (
            "MAC-Fairness 把同一底层模型实例化为 identity agent 与 baseline agent，控制 demographic、human/AI 身份和 peer reveal/anonymous 条件；"
            "agent 每轮只看上一轮且不能识别自身先前答案，用 prior disagreement 条件下的 shift rate 区分 position persistence 与 peer receptiveness。"
        ),
        "evaluation_contract": (
            "主实验在 BBQ、Discrim-Eval 与 Difference-Awareness 上评估 8 个模型；另有 3 个模型因无法稳定满足回复格式而从 in-situ 阶段排除。"
            "设计使用同模型双 agent、仅上一轮可见和统计检验来隔离变量；这不是实际用户环境或社会结果评估。"
        ),
        "tradeoffs_and_failure_modes": (
            "该设计把交互行为与静态问答分开，但 shift rate 不是道德或公平性的真值；同模型双 agent、合成交互和有限历史提高可控性，也限制生态有效性。"
            "格式失败导致的模型排除还会改变可比较总体，因此结果不能外推为真实部署中的公平、安全或用户影响。"
        ),
    },
    "2605.19755": {
        "old_path_and_changed_constraint": (
            "传统 SBOM 以静态组件名和版本为主，无法完整绑定模型、数据引用、运行时依赖、配置与生成过程；在 AI artifact 持续演化和环境漂移时，"
            "仅凭名称清单不足以重放、归责或判断漏洞匹配。"
        ),
        "mechanism_and_ownership": (
            "方案扩展 CycloneDX，记录 AI provenance、model lineage、disclosure metadata，并用组件 hash、签名、容器运行态和 agent 生成的环境记录绑定 artifact；"
            "自动化流水线负责环境发现、漏洞富化、schema 校验和 reproducibility audit，材料不全时保留 partial-attestation 状态。"
        ),
        "evaluation_contract": (
            "作者在受控 containerised analytic workflows 中报告 98.7% reproducibility fidelity、96.2% vulnerability-match precision 和 63% manual-oversight reduction。"
            "这些是作者在论文 workload 下的结果；尚无跨组织、长期生产采用或不同 vulnerability database 的独立验证。"
        ),
        "tradeoffs_and_failure_modes": (
            "完整性依赖 runtime discovery、包名归一化、base-image 可见性和漏洞数据库覆盖；hash 改善身份绑定，却不能证明语义等价或实际可利用性。"
            "非确定性执行仍可能阻止 bit-identical replay，持续采集、签名和富化也增加存储与治理成本；无法解析的瞬态依赖必须保持 unverifiable，而非伪造完整性。"
        ),
    },
    "2605.20196": {
        "old_path_and_changed_constraint": (
            "经验 scaling law 描述损失随数据量下降的斜率，却不解释为什么不同语料具有不同指数；token-frequency tail 只度量出现频率，"
            "不能区分某个上下文状态对 next-token prediction 的贡献。"
        ),
        "mechanism_and_ownership": (
            "论文以 suffix-automaton state 构造 predictive-contribution spectrum：每个状态的 global-KL contribution 等于经验状态质量乘以其相对全局 next-token baseline 的 KL 偏离；"
            "再定义有效截断秩 K(N)，令 spectrum residual tail 与模型 excess loss 对齐，用它描述数据量增加时逐步覆盖的预测贡献。"
        ),
        "evaluation_contract": (
            "实验在 12 个真实语料上训练固定的小型 GPT learner，比较 spectrum tail slope 与经验 data-scaling exponent，并报告 log K 对 log N 的 pooled R² 约 0.96（raw）"
            "和 0.90（smoothed）。未验证 frontier model、不同架构或 causal intervention。"
        ),
        "tradeoffs_and_failure_modes": (
            "该解释需要构造语料状态空间，结果依赖 suffix/state 表示与合并策略；论文中的 quotient/merged construction 解释力更弱，说明压缩可能删除有用的细粒度信息。"
            "当前证据是固定小模型上的相关性，不能证明 K(N) 是模型真实学习状态，也不能把相关斜率当作跨架构的因果 scaling law。"
        ),
    },
    "2605.25310": {
        "mechanism_and_ownership": (
            "研究从 agent 每次 assistant decode boundary 的 residual stream 读取表示，用低容量 edge probe 预测先前 tool output 是否为后续 tool call 提供参数，"
            "从而重建调用依赖 DAG 及其 transitive closure；random-label control、positional baseline、value/structure perturbation 与跨层 patching 用于区分记忆、位置和拓扑信号。"
        ),
        "evaluation_contract": (
            "主实验在 Qwen3-32B 与 τ-bench retail 上记录 65 个表示层，并在 TaskBench、BFCL、ComplexFuncBench、ToolHop 检查跨域调制；"
            "部分 activation-patching 表示传播结果在 Llama-3.3-70B 复现。interactive multi-hop 中 residual 带来非位置贡献，而 single-shot 或位置已足够时该贡献衰减。"
        ),
        "tradeoffs_and_failure_modes": (
            "线性可解码证明 residual 中存在相关结构，不证明 agent 使用该结构控制动作；patching 改变后续 probe readout，却没有改变实际 tool call。"
            "高幅 value perturbation、跨域行为充分干预和长时序控制仍未验证，且部分 benchmark 的位置 baseline 已很强；因此不能把 probe AUROC 当成可靠规划或因果控制能力。"
        ),
    },
    "2605.18755": {
        "old_path_and_changed_constraint": (
            "Kubernetes 原生 Pod 状态和 Event 在 kubelet 重启轮转后只保留当前快照；当 LastTerminationState 被新一次终止覆盖、对象又被删除时，"
            "故障因果链跨过 evidence horizon 后无法由 kubectl 恢复。Metrics、logs 与 traces 各自保留观测，但不自动保存同一对象的时点快照与因果边。"
        ),
        "tradeoffs_and_failure_modes": (
            "当前 collector 仅 namespace-scoped；生产化需要 cluster-wide RBAC 或多 namespace 实例，且 ConfigMap watch 涉及敏感配置，"
            "论文默认只保存 metadata 与 content hash。SQLite 只适合单集群，跨集群需要分布式存储与查询联邦。30 次统计实验来自 Apple M-series 上的 "
            "Minikube，AKS 仅单次；NodeMemoryPressure→OOMKill 边未被观察到，因此不能外推到不同 runtime、硬件、kubelet 配置或大规模生产集群。"
        ),
    },
}


def clean_markup(raw: str) -> str:
    # arXiv HTML places the table of contents and site chrome before the paper
    # body.  Their headings contain words such as "Evaluation" and
    # "Limitations", so leaving them in the text makes a sentence selector
    # mistake navigation for evidence.  Strip non-paper containers first.
    raw = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if len(s.strip()) > 24]


def pick(sents: list[str], patterns: tuple[str, ...], fallback: str) -> str:
    for sentence in sents:
        lowered = sentence.lower()
        if any(pattern in lowered for pattern in patterns):
            return sentence[:900]
    return fallback


def node_for(title: str, abstract: str) -> str:
    text = f"{title} {abstract}".lower()
    if "world model" in text:
        return "MULTIMODAL-WORLD-MODELS"
    if any(x in text for x in ("embodied", "vision-language-action", " vla ")):
        return "MULTIMODAL-EMBODIED-VLA"
    if "diffusion" in text:
        return "MULTIMODAL-GENERATIVE-PARADIGMS"
    if any(x in text for x in ("mixture-of-experts", "moe", "expert replication")):
        return "MODEL-MOE"
    if any(x in text for x in ("kv cache", "prefix cach", "cache eviction", "knowledge packs")):
        return "INFER-KV-CACHE"
    if "speculative decod" in text:
        return "INFER-SPECULATIVE-DECODING"
    if any(x in text for x in ("quantization", "gpu kernel", "triton", "compiler", "webgpu", "instruction set")):
        return "INFER-TENSORRT-LLM"
    if "distributed training" in text:
        return "TRAIN-DISTRIBUTED-TRAINING"
    if any(x in text for x in ("scaling law", "wall-clock constrained training", "data scaling")):
        return "WORLDVIEW-SCALING-LAW"
    if any(x in text for x in ("evaluation", "benchmark", "llm-as-judge", "attesting")):
        return "PLATFORM-EVALUATION-SYSTEM"
    if any(x in text for x in ("observability", "fail quietly", "operational memory")):
        return "PLATFORM-MONITORING"
    if any(x in text for x in ("attack", "security", "safety", "provenance", "governance")):
        return "PLATFORM-SECURITY"
    if any(x in text for x in ("routing", "serving", "inference", "early exit", "computation depth")):
        return "INFER-SCHEDULING"
    if "rag" in text or "retrieval-augmented" in text:
        return "AGENT-RAG"
    if "memory" in text:
        return "AGENT-MEMORY"
    if "multi-agent" in text:
        return "AGENT-MULTI-AGENT"
    if any(x in text for x in ("agent", "workflow", "skill")):
        return "AGENT-PLATFORM"
    return "WORLDVIEW-SYSTEM-EVOLUTION"


def score_for(title: str, abstract: str) -> tuple[int, int, int]:
    text = f"{title} {abstract}".lower()
    design = 3 if any(x in text for x in ("introduce", "propose", "architecture", "framework", "mechanism", "system")) else 2
    reach = 3 if any(x in text for x in ("distributed", "serving", "platform", "runtime", "multi-agent", "gpu", "release", "security")) else 2
    durability = 3 if any(x in text for x in ("state", "ownership", "contract", "cache", "routing", "checkpoint", "world model", "evaluation")) else 2
    return design, reach, durability


def exact_source(month_root: Path, aid: str) -> Path | None:
    exact = month_root / "exact-v1"
    for suffix in ("html.html", "pdf"):
        path = exact / f"{aid}v1.{suffix}"
        if path.exists() and path.stat().st_size > 2000:
            return path
    return None


def build_new_review(month_root: Path, row: dict) -> dict:
    aid = row["arxiv_id"]
    source = exact_source(month_root, aid)
    if source is None:
        return {"arxiv_id": aid, "status": "blocked", "reason": "exact-v1 HTML/PDF unavailable"}
    body = source.read_bytes()
    raw_html = body.decode("utf-8", errors="ignore") if source.suffix == ".html" else ""
    # Evidence selectors operate on paper paragraphs, not the flattened page.
    # Flattening headings together with text can manufacture a long pseudo-
    # sentence from the table of contents even after site chrome is removed.
    paragraph_text = " ".join(
        clean_markup(block)
        for block in re.findall(r"<p\b[^>]*>.*?</p>", raw_html, flags=re.I | re.S)
    )
    abstract_sents = sentences(row.get("abstract", ""))
    full_sents = sentences(paragraph_text)
    merged = abstract_sents + full_sents
    problem = (abstract_sents[0] if abstract_sents else row["title"])[:900]
    changed = pick(merged, ("existing", "prior work", "however", "challenge", "bottleneck", "limited"), "The exact-v1 body does not isolate the prior-path boundary in one sentence; no broader claim is inferred.")
    mechanism = pick(merged, ("we propose", "we introduce", "we present", "our method", "our system"), "Mechanism is bounded to the exact-v1 abstract and method sections; no undisclosed implementation is inferred.")
    evaluation = pick(merged, ("we evaluate", "experiments", "benchmark", "evaluation", "we show", "results"), "No complete workload/hardware/SLO contract is disclosed in a single extract; missing fields remain Not Disclosed.")
    limitation = pick(full_sents, ("limitation", "threats to validity", "future work", "overhead", "trade-off", "failure"), "No dedicated limitation statement was found by the bounded full-text pass; absence is not evidence of absence.")
    if aid not in REVIEW_DECISIONS:
        raise RuntimeError(f"missing fresh-context Score V2 / owner decision for {aid}")
    node, (dd, reach, durability) = REVIEW_DECISIONS[aid]
    review_status = "deep_complete" if dd + reach + durability >= 7 else "standard_complete"
    review = {
        "source_family_id": row["source_family_id"],
        "arxiv_id": aid,
        "title": row["title"],
        "status": review_status,
        "access_status": "accessible",
        "exact_v1_path": str(source.relative_to(ROOT)),
        "exact_v1_sha256": hashlib.sha256(body).hexdigest(),
        "stable_node_id": node,
        "score_v2": {"design_delta": dd, "system_reach": reach, "durability": durability, "total": dd + reach + durability},
        "problem": problem,
        "old_path_and_changed_constraint": changed,
        "mechanism_and_ownership": mechanism,
        "evaluation_contract": evaluation,
        "proof_and_nonproof": "Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.",
        "tradeoffs_and_failure_modes": limitation,
        "coexistence_boundary": "The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.",
        "books_disposition": "Not Assessed",
    }
    review.update(REVIEW_TEXT_OVERRIDES.get(aid, {}))
    return review


def week(day: str) -> str:
    iso = date.fromisoformat(day).isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def main() -> None:
    for month in ("04", "05"):
        month_root = ROOT / f"papers/2026/{month}/_sources/arxiv-owner-replay-20260903"
        summary = json.loads((month_root / "month-reconciliation.json").read_text(encoding="utf-8"))
        blocked: list[dict] = []
        queue: list[dict] = []
        month_counts = {"raw": 0, "retained": 0, "closure": 0, "withdrawn": 0, "new_review": 0}
        for day in summary["days"]:
            receipt = json.loads((ROOT / day["receipt"]).read_text(encoding="utf-8"))
            by_id: dict[str, dict] = {}
            for old in receipt["candidate_reconciliation"]:
                cells = old["candidate_row"]
                source_month = old["source_report_day"][5:7]
                archived_review = (
                    f"papers/2026/{source_month}/_sources/arxiv-owner-replay-20260903/"
                    f"legacy-reports-before-created-owner-reconciliation/{old['source_report_day']}.md#{cells[14]}"
                )
                by_id[old["arxiv_id"]] = {
                    "source_family_id": cells[0], "arxiv_id": old["arxiv_id"], "title": next((x["title"] for x in receipt["identities"] if x["arxiv_id"] == old["arxiv_id"]), old["arxiv_id"]),
                    "primary_identifier": cells[1], "event_identity": cells[2],
                    "owner_week": week(day["report_date"]), "first_public_date": day["report_date"],
                    "design_delta": cells[6], "system_reach": cells[7], "durability": cells[8], "total": cells[9],
                    "candidate_state": cells[10], "review_status": cells[11], "access_status": cells[12], "review_override": cells[13],
                    "review_ref": cells[14], "owner_report_ref": "self", "prior_review_ref": "—",
                    "reconciliation": "new_in_window", "legacy_report_ref": archived_review,
                    "stable_node_id": cells[18], "books_disposition": cells[19], "books_review_ref": cells[20], "benchmark_claim": cells[21],
                }
            reviews = []
            for row in receipt["identities"]:
                month_counts["raw"] += 1
                status = row["screening_status"]
                if status == "withdrawn_pre_denominator":
                    month_counts["withdrawn"] += 1
                elif status == "retained":
                    month_counts["retained"] += 1
                    if row["arxiv_id"] not in by_id:
                        review = build_new_review(month_root, row)
                        reviews.append(review)
                        if review["status"] == "blocked":
                            blocked.append({"report_date": day["report_date"], **review})
                            continue
                        month_counts["new_review"] += 1
                        score = review["score_v2"]
                        by_id[row["arxiv_id"]] = {
                            "source_family_id": row["source_family_id"], "arxiv_id": row["arxiv_id"], "title": row["title"],
                            "primary_identifier": f"arXiv:{row['arxiv_id']}v1", "event_identity": f"paper-v1:{row['arxiv_id']}",
                            "owner_week": week(day["report_date"]), "first_public_date": day["report_date"],
                            "design_delta": score["design_delta"], "system_reach": score["system_reach"], "durability": score["durability"], "total": score["total"],
                            "candidate_state": "retained", "review_status": review["status"], "access_status": "accessible", "review_override": "none",
                            "review_ref": f"review:{row['source_family_id']}", "owner_report_ref": "self", "prior_review_ref": "—",
                            "reconciliation": "new_in_window", "legacy_report_ref": "—", "stable_node_id": review["stable_node_id"],
                            "books_disposition": review["books_disposition"], "books_review_ref": "—", "benchmark_claim": "yes",
                        }
                        queue.append({"report_date": day["report_date"], **review})
                else:
                    month_counts["closure"] += 1
            ledger = {
                "schema": "historical-daily-canonical-owner-ledger-v2.1",
                "report_date": day["report_date"],
                "owner_evidence": str((ROOT / day["receipt"]).relative_to(ROOT)),
                "raw_identity_count": len(receipt["identities"]),
                "candidate_count": len(by_id),
                "candidates": sorted(by_id.values(), key=lambda x: x["source_family_id"]),
                "new_exact_v1_reviews": reviews,
                "pre_denominator_closure_count": len(receipt["identities"]) - len(by_id) - sum(x.get("screening_status", "").startswith("withdrawn") for x in receipt["identities"]),
                "withdrawn_pre_denominator_count": sum(x.get("screening_status", "").startswith("withdrawn") for x in receipt["identities"]),
            }
            day_dir = month_root / day["report_date"].replace("-", "")
            (day_dir / "canonical-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        day_ledgers = [json.loads((month_root / day["report_date"].replace("-", "") / "canonical-ledger.json").read_text()) for day in summary["days"]]
        month_counts = {
            "raw": sum(row["raw_identity_count"] for row in day_ledgers),
            "retained": sum(row["candidate_count"] for row in day_ledgers),
            "closure": sum(row["pre_denominator_closure_count"] for row in day_ledgers),
            "withdrawn": sum(row["withdrawn_pre_denominator_count"] for row in day_ledgers),
            "new_review": len(queue),
        }
        (month_root / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "books-writeback-queue-v2.1", "month": f"2026-{month}", "status": "pending_root_serial_books_comparison", "items": queue}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (month_root / "MATERIALS_REQUEST.json").write_text(json.dumps({"schema": "materials-request-v2.1", "month": f"2026-{month}", "items": blocked}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        summary["canonical_counts"] = month_counts
        summary["canonical_candidate_total"] = month_counts["retained"]
        summary["new_exact_v1_blocked"] = len(blocked)
        summary["books_writeback_queue"] = len(queue)
        summary["status"] = "books_writeback_pending" if queue else ("materials_blocked" if blocked else "complete")
        (month_root / "month-reconciliation.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"month": month, **month_counts, "canonical_candidates": summary["canonical_candidate_total"], "blocked": len(blocked), "books_queue": len(queue)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
