# 2026-06-03 V3 Evidence batch 05

本批覆盖恢复候选 33～40，全部使用官方 exact-v1 HTML。对“新 benchmark/新算法”不自动产生 Books 写入；只有当前正文缺可区分长期合同者才执行 owner-level 写回。

## Candidate evidence 与 Books comparison

### 2606.03601v1 — DDOR

- Evidence：Method=`§3.1 fault localization；§3.2 test generation；§3.3 oracle；§3.4 repair`；Evaluation=`§4.1～§4.8`；Limitations=`§5 Conclusion；无 dedicated limitations`。
- 边界：black-box delta debugging 能在所测 model/dataset 生成 minimal refusal-trigger fragment 并提出 prompt repair，但 refusal detector/oracle、语义保持与有限 benchmark 不证明 repair 后安全或无新回归。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。当前正文已要求 overrefusal 与 harmful counterpart 成对、minimal mutation、oracle/meta-evaluation、repair regression 和 release owner 分权。

### 2606.03647v1 — Adaptive LLM Attack Baseline

- Evidence：Method=`§2 attack desiderata；§3.1～§3.2 IHO`；Evaluation=`§4；§5.1～§5.5；Appendix B/F/G`；Limitations=`§7 Conclusion；Appendix J/L`。
- 边界：IHO 与 EVUS 在所测 behavior/model/defense pipeline 上扩展 adaptiveness、transfer 与 severity/sample-efficiency 评价；attacker/judge training 与有限 harm taxonomy 不证明最坏情况完备。
- Books：**Integrated / `PLATFORM-EVALUATION-SYSTEM`**。正文锚点“Attack Success Rate 不能压平 Attack Profile”已写入顶层 Review notes 之前，覆盖 attacker knowledge/access、适用性、自适应性、迁移性、危害、样本效率与指标 non-authority 边界。

### 2606.03648v1 — Capability-Grounded Safety Measurement

- Evidence：Method=`§3.1～§3.4 fine-tuning/evaluation identity`；Evaluation=`§4；§5.1～§5.5`；Limitations=`§6 Limitations`。
- 边界：selected model/data/hyperparameters/safety judges 支持安全结论会随 capability goal、coherence、refusal 与 benchmark 变化；不证明单一 capability score 可统一所有 safety trade-off。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。正文已要求安全与能力目标、artifact/hyperparameter、sampling/judge 与 matched release slices 共同冻结，不能比较不等价 capability operating points。

### 2606.03657v1 — NovelAPIBench

- Evidence：Method=`§3.1～§3.3 discovery、knowledge extraction、task/test generation 与 failure taxonomy`；Evaluation=`§4；Appendix E`；Limitations=`Appendix A`。
- 边界：约 800 APIs、五库域、四 backbone 与多 adaptation paradigm 支持 signature/mechanism/source/example 与 executable use 分离；只测 Python/single-API、有限 compute，不证明 internalization 永久或 RAG 优势普适。
- Books：**Existing / `AGENT-TOOL-CALLING` + `PLATFORM-EVALUATION-SYSTEM`**。当前正文已有 tool/API discovery、schema/version、environment execution、argument/effect verifier 与 failure taxonomy；文档召回不能替代 executable usage。

### 2606.03692v1 — SkillPyramid

- Evidence：Method=`§2.1～§2.4 relation analyzer/builder、atomic extraction、abstract induction 与 evolution`；Evaluation=`§3～§4`；Limitations=`Limitations`。
- 边界：所测 Agent tasks 支持 hierarchy 可减少冗余并促进复用，但 LLM-induced relation/abstraction、有限 benchmark 与 self-evolution 不证明正确依赖、无冲突或安全安装。
- Books：**Existing / `AGENT-PLATFORM`**。正文已要求 skill candidate、typed dependency/conflict、validation、promotion/version/revoke 与 executable-set gate；pyramid 是可选组织形态。

### 2606.03739v1 — Entropy Gate

- Evidence：Method=`§3～§5 energy、quenching、fidelity gate 与 architecture`；Evaluation=`§6～§10`；Limitations=`§8；§11.3～§11.8`。
- 边界：所谓 fidelity bound 约束 embedding similarity 而非 task correctness；标准 benchmark 仅 6/9 compressed questions 保持正确，LaTeX/token boundary 与 pipeline loop 均是明确反例。
- Books：**Only report**。当前 Context/KV compression 已有 role/semantic fidelity、irreversible deletion、task verifier 与 raw/full fallback；本篇的 thermodynamic 命名和极小实验不足以改变 owner 正文。

### 2606.03762v1 — Tool-Aware Agentic RL

- Evidence：Method=`§IV-A trajectory filtering；§IV-B entropy-guided exploration；§IV-C implementation`；Evaluation=`§V-A～§V-D；Appendix D`；Limitations=`§VI Conclusion and Limitation`。
- 边界：tool failure/over-reliance filtering 与 post-tool high-entropy bonus 只在所测 Qwen sizes、benchmarks 和 tool environments 支持稳定性；execute success 不等于 tool result 正确，entropy 不等于 useful exploration。
- Books：**Existing / `TRAIN-GRPO`**。正文已把 tool/environment outcome、trajectory admission、partial verifiability、exploration entropy 与 delayed consequence 分权，并要求 outcome verifier 保持最终 gate。

### 2606.03785v1 — Backdoor Unlearning Generalization

- Evidence：Method=`§3.1 backdoors；§3.2 model diffing/CASD`；Evaluation=`§4～§6；Appendix E～G`；Limitations=`§7 Discussion；Limitations`。
- 边界：六个 models/三 family、八类 injected trigger 支持相近 activation shift 时单-trigger unlearning 可能迁移；CASD 是相关 sensor，不证明未知 trigger 被完整删除或 retained utility/生产攻击安全。
- Books：**Integrated / `PLATFORM-SECURITY`**。正文锚点“Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family”已写入顶层 Review notes 之前，覆盖 held-out trigger family、activation diagnostic 与 behavior/retain release gate。

## Batch result

- Evidence complete：8/8。
- Books：5 `Existing`，2 `Integrated`，1 `Only report`，0 `Deferred`。
- exact-v1 blocker：0。
