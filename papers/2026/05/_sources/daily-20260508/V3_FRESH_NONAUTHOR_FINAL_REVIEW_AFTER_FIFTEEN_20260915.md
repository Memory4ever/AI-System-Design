# 2026-05-08：十五项返修后的 fresh non-author 最终复核

## 结论

**FAIL。** 当前 `166` 个候选的机械账、Evidence 状态、十五项限定返修以及十二个新 Books 正文绑定均可通过；但新的有界 closure challenge 在既有 `453` 个 closure 中确认 `18` 个 contribution-gate false negative。因此本日报不能登记 `Complete`，也不能把当前 `619 = 166 + 453` 当作最终冻结分母。

本轮 reviewer 与 05-08 作者、root Books writer 均不同。检查没有扩大日期、来源或 `619` 个 canonical raw identities，也没有编辑 Books。

## 1. 机械账与 Evidence

- `V3_RECERTIFICATION.json` 含 `619` 个唯一 arXiv ID 与 `619` 个唯一 Source Family ID。
- 复算得到 `619 = 166 retained_candidate + 453 pre_denominator_closure`。
- `166/166` 候选为 Evidence complete：`124 deep_complete + 42 standard_complete`，`Review Pending = 0`。
- Score V3 复算无算术错误：`103` 项为 `7～9`，`63` 项为 `5～6`。
- 当前 retained set 中未见 `withdrawn`、`blocked` 或 `disputed` 状态；本轮重新打开十五个 exact-v1 URL，题名均与账本一致，未见 withdrawal banner。

上述检查只证明当前快照内部一致，不证明 closure 没有漏收。

## 2. 十五项返修与 Books 对读

### 三项 No Change

- `2605.05662`：Ch66 主正文已经把总体 jailbreak rate 拆为安全韧性、prompt 难度、语言处理难度与 concept-language slice，并要求保留逐语言 outcome、攻击类型与不确定性；足以承载 country/language aggregate failure 的边界。
- `2605.06201`：Ch66 已明确无 ground truth 的一致性只能作为 measurement sensor，不能取得 truth authority；correctness、consistency、prompt variation 与独立 evidence 仍需分账。
- `2605.05741`：Ch66 已把 processing trajectory 限定为 risk sensor，并要求按目标模型、任务和分布校准；Ch29 同时保存 final answer 改善不代表 reasoning process 改善的边界。

三项 `No Change — Existing Coverage` 均有主正文命题，不依赖 Review notes 或泛化章节名称。

### 十二项 Integrate

十二个 `semantic-body-binding` 均唯一，位于各自文件第一个 `## Review notes` 之前，owner 与 ROADMAP 一致：

| Source Family | Owner | 复核结果 |
| --- | --- | --- |
| `2605.05668` | `MULTIMODAL-REPRESENTATION` | 通过；表示重排/扩展、routing 冗余反证、模型/层/benchmark 边界及回退完整 |
| `2605.05742` | `TRAIN-RLHF` | 通过；capacity mismatch 非必要、线性理论边界及生产 Gate 完整 |
| `2605.06070` | `TRAIN-RLHF` | 通过；二元偏好到 latent gap、分布假设/selection bias 与回退完整 |
| `2605.06170` | `PLATFORM-EVALUATION-SYSTEM` | 通过；动态 benchmark lifecycle、污染/late-entry 状态与冻结基线回退完整 |
| `2605.06509` | `MULTIMODAL-GENERATIVE-PARADIGMS` | 通过；谱集中、global/local 分责、SVD 成本与 backbone 边界完整 |
| `2605.05714` | `MULTIMODAL-EMBODIED-VLA` | 通过；appearance 到 relation action state、误差传播与 controller fallback 完整 |
| `2605.05851` | `WORLDVIEW-LLM-INTELLIGENCE` | 通过；hypothesis generation/evaluation/extrapolation 分权与 number-game 边界完整 |
| `2605.06165` | `MODEL-SAMPLING` | 通过；answer commit/justification continuation 分离、fidelity 风险与 pre-answer fallback 完整 |
| `2605.06183` | `TRAIN-LORA` | 通过；gradient-energy proposal、held-out Gate、模型规模/任务边界与 full-stack fallback 完整 |
| `2605.06324` | `PLATFORM-EVALUATION-SYSTEM` | 通过；metric-as-attack-surface、semantic class/certificate、有限形式模型边界完整 |
| `2605.06342` | `MODEL-SELF-ATTENTION` | 通过；QK rerouting、selective projection、white-box/calibration 依赖与多种 fallback 完整 |
| `2605.06529` | `TRAIN-RLHF` | 通过；outcome-equivalent shortcut、trace prior/KL、POMDP/simulator 边界与 trace-audit fallback 完整 |

Books 本体无需返工。不过 canonical ledger 的十二项 item-level `books_disposition` 仍写着 `Integrate — Pending root writeback`，与 README 和实际正文不一致；下一轮作者同步账本时必须改为 `Integrate — Applied`。

## 3. 有界 false-negative challenge

### 抽样方式

不重扫 `453` 个 closure。固定选取 `28` 项标题显示可能触及 RAG、Agent belief/search、训练目标与安全、模型表示、distributed inference、LLM execution hardware、多模态生成、World Action Model、interpretability evidence 或 security workflow 的高风险 closure；逐项阅读完整摘要。样本跨越模型/训练、推理/硬件、多模态、Evaluation/Security 与 Agent 五类，不把简单关键词命中当作恢复依据。

### 确认的 18 个 false negative

| arXiv | 摘要中已经成立的项目增量 | 建议 owner（待作者对读确认） |
| --- | --- | --- |
| `2605.05245` | 把 multi-hop RAG evidence selection 建模为 token-constrained gap repair，并显式拥有 gap、micro-query、corroboration/redundancy utility | `AGENT-RAG` |
| `2605.05277` | 在同一 encoder forward 中合并 moderation 与 PII detection，给出 latency/throughput/quality 的 always-on guardrail operating point | `PLATFORM-SECURITY`，handoff `INFER-REQUEST-LIFECYCLE` |
| `2605.05386` | 交互 Agent 维护可扩展 latent belief，以 expected mutual information 选择澄清问题，改变 information-state 与 query control | `AGENT-PLANNING` |
| `2605.05415` | 以 f-divergence ambiguity set 和 worst-case reweighting 改变 adversarial post-training objective，而非仅增加攻击样本 | `TRAIN-RLHF` |
| `2605.05438` | 揭示高表面 accuracy 下的 causal-reasoning collapse，并以 graph semantic constraint 与动态权重改变 SFT supervision | `TRAIN-SFT` |
| `2605.05495` | 受控 continual-composition 证据显示 feed-forward shortcut 与 recurrent weight sharing 导致不同 transfer/failure boundary | `MODEL-TRANSFORMER-LAYER` |
| `2605.05503` | Diffusion LM watermark 在多跳无密钥 rewriting 下快速失效，直接改变 watermark robustness/evaluation threat contract | `PLATFORM-SECURITY` |
| `2605.05638` | 59 个 backbone-task pairing 支持 frozen representation geometry 可承担 label-free OOD sensor，并挑战 detector-choice 优先级 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.05718` | 异构 pretrained models 在不共享 raw input、参数或 encoder 时，通过 unlabeled consensus embedding 协作推理；representation alignment 成为瓶颈 | `INFER-DYNAMO`，handoff `PLATFORM-MULTI-TENANT` |
| `2605.05980` | 把 long-horizon Agent 的 overthinking/overacting 定义为 trajectory failure state，并用 residual drift axes 做运行时 intervention | `AGENT-REFLECTION` |
| `2605.06040` | 用 novelty sensor 剪枝 Tree-of-Thought，在增加每节点判断开销的同时减少整体 token/search tree，形成明确 search-budget trade-off | `AGENT-PLANNING` |
| `2605.06052` | 用 datatype-adaptive shared MAC 数据通路支持 LLM mixed precision，给出 DSP sharing、constant latency 与资源/能效边界 | `INFER-TENSORRT-LLM` |
| `2605.06247` | 通过 compressed teacher context、router 与 sparse adapters 在异构 World Action Model 间迁移知识，改变 latent interface/adapter ownership | `MULTIMODAL-WORLD-MODELS`，handoff `TRAIN-LORA` |
| `2605.06376` | 将 few-step distribution matching 从离散锚点改为 continuous-time/off-trajectory state，明确 reverse-KL artifact 与辅助模块取舍 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| `2605.06480` | 把 activation-patching 结果组织为 graph artifact，并用 prompt/raw-tensor controls 收窄 circuit claim 的 evidence contract | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.06583` | 将 flow-model preference alignment 写成 velocity-field optimal control，并以 truncated adjoint 重分配 trajectory compute | `TRAIN-RLHF` |
| `2605.06601` | resumable binary-patch Agent pipeline 将 extraction/ranking/context/export/reasoning/validation failure 分段归因，改变安全 Agent 的 evidence workflow | `AGENT-WORKFLOW`，handoff `PLATFORM-SECURITY` |
| `2605.06667` | camera-consistent pose/depth 条件与两阶段 denoising guidance 改变 joint camera/motion generation 的控制与过约束边界 | `MULTIMODAL-GENERATIVE-PARADIGMS` |

这 18 项并非因“主题相关”恢复；完整摘要已经分别给出可定位的机制、状态/控制变化或 evaluation/security contract delta。它们必须进入 author-side exact-v1、withdrawal、Score V3、相应深度 Evidence、owner/相邻章节对读与 Books Decision。

### 抽样后继续关闭的 10 项

`2605.05584`、`2605.05711`、`2605.05920`、`2605.06077`、`2605.06087`、`2605.06104`、`2605.06187`、`2605.06345`、`2605.06416`、`2605.06664` 继续 closure。它们分别属于无验证的治理议程、交互式 3D 应用、用 LLM 做硬件 DSE、position paper、通用 dynamical-system certification、Decision Transformer 局部 tokenization、通用 black-box optimization、受 judge 约束的科研 ideation、认知类比式 context compressor 与 GUI grounding 局部修复；当前摘要不足以证明本项目长期 owner 或需要改变 Books 既有设计判断。若 exact-v1 后续出现与当前关闭理由相反的证据，只定点重开对应 family。

## 4. 精确返修边界

1. 只重开上表 18 项及共享相同泛化 closure 理由的有限 sibling strata；不得重枚举来源、日期或全部 619 identities。
2. 对 18 项完成 exact-v1、withdrawal、Score V3、Evidence、owner/相邻章节对读与 Books Decision；不能由本次摘要挑战直接写 Books。
3. 把十二项已存在 Books binding 的 item-level disposition 从 `Pending root writeback` 同步为 `Applied`。
4. 重新计算 retained/closure、深度与 Books 分流；必要 Books 写回由 root 串行落实。
5. 完成后交给另一位未参与返修和写回的 non-author reviewer；本文件不能被作者自签覆盖。

## 5. 检查

- 十二个新 marker：唯一、owner 正确、均位于 `Review notes` 前。
- 三个 No Change：主正文命题存在。
- `python3 scripts/validate_research.py --report papers/2026/05/08/README.md`：通过；只证明格式与可判定一致性。
- scoped `git diff --check`：通过。
- 最终 Gate：**FAIL**；`final_independent_signoff = false`。
