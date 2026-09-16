# 2026-05-11 fresh non-author screening repair queue

- Gate：Ongoing；本队列只返修 current `official_arxiv_oai_direct` 的已定位 false-negative / retained-regression，不扩窗、不扩源、不重扫 826 identity。
- Books：当前 26 项写回结构与写后语义复核已通过；本队列不得先改 Books。新候选须先完成 exact-v1 Evidence 与 Books Decision。
- 当前投影：`826 = 74 retained + 561 direct closure + 191 owner-day isolation`。该式机械成立，但 `74/561` 因下列误关项不是有效终态。

## A. 18 项确定 false negative：直接重开为 retained

这些题摘均明确新增长期机制、适用边界或评价有效性条件，不能用“未找到机制增量”的 generic closure 关闭。重开后逐项完成 exact-v1 locator、证据边界、评分和 Books Decision；不能预设为 Integrate。

| arXiv ID | 最小贡献理由 | 建议 owner |
| --- | --- | --- |
| `2605.06690` | 用 epistemic state graph 显式化递归推理状态，并以 expand/consolidate order-gap 形成有边界的停止判据。 | `AGENT-REFLECTION` |
| `2605.06908` | 区分 compute need 与 compute suitability，证明同一 gate signal 会跨环境/骨干反向，并用 counterfactual learning 修正 gate direction。 | `INFER-SCHEDULING` |
| `2605.06924` | 长视频生成从 open-loop segment chaining 变为带 multimodal memory、mode switch、hierarchical refine/update 的闭环。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| `2605.06988` | 把通信频率、消息内容与 collective belief state 联结，并指出 consensus metric 看不见 confident-but-wrong herding。 | `AGENT-MULTI-AGENT` |
| `2605.07042` | 以 POMDP belief state 显式拥有 agentic search 状态，并提供 programmatic exhaustion gate。 | `AGENT-CONTEXT` |
| `2605.07073` | 用 OS-enforced role separation 区分团队成功、越权与 verifier false accept，改变 Multi-Agent evaluation contract。 | `AGENT-MULTI-AGENT` |
| `2605.07271` | 以 decision representation transition 解释 layer pruning 的突发 collapse，并区分 Silent/Decisive phase 的结构敏感性。 | `MODEL-TRANSFORMER-LAYER` |
| `2605.07331` | cumulative token IS ratio 修复 prefix state mismatch，并以 position-adaptive clipping 改写 LLM policy optimization 的 bias/variance 取舍。 | `TRAIN-PPO` |
| `2605.07395` | 将 multi-LLM routing 的 unsolvability ceiling 分解为 judge bias、truncation 与 format artifact，并证明这些 artifact 污染 router labels。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.07443` | 非连续复用场景把 prefix cache 扩展为 reusable block、分层存储、locality scheduler 与 selective-attention correction。 | `INFER-KV-CACHE` |
| `2605.07494` | continual VLM adapter 从固定专家池变为可演化 sparse pool，并分离 expert evolution 与 prototype-guided selection。 | `TRAIN-LORA` |
| `2605.07569` | 将 CP/HP 从同构 mesh 扩展到按 compute/memory/network 分配的 fully asymmetric heterogeneous partition。 | `TRAIN-DISTRIBUTED-TRAINING` |
| `2605.07630` | 将 harmless outcome 分解为 safe choice、unsafe choice 与 inability-to-act，修正 phone-use Agent safety 评价的假阳性。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.07776` | 把 reasoning trace 视为 evolving state，用 uncertainty profile 支持 early failure sensing，而不把终局 confidence 当唯一信号。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.07850` | LoRA 单一静态 rank 变为同一 adapter 内的 hierarchical sub-rank，并引入 AURAC 评价动态 rank。 | `TRAIN-LORA` |
| `2605.07924` | 离散 flow distillation 的瓶颈从 student capacity 转向 teacher trajectory quality，以 training-only energy navigation 选择 midpoint。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| `2605.07933` | latent diffusion language model 联合训练 encoder/diffusion/decoder，并给出防止 naive joint-training collapse 的分阶段 recipe。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| `2605.08061` | 将单一/二元 reward 分解为 policy 不可见 grounding 下的 weighted rubric criteria，改变 RL credit 与 judge authority 的接口。 | `TRAIN-GRPO` |

## B. 10 项前版 direct retained regression：逐项恢复或给出命题级改判理由

这些 identity 在前一版日报已是 direct retained，并具有 owner / Evidence disposition；当前仍是 `official_arxiv_oai_direct`，却被同一 generic reason 关闭。它们不自动继承旧结论，但必须逐项对照旧 Evidence 与当前合同，不能继续保留模板式 closure。

| arXiv ID | 前版 owner / disposition |
| --- | --- |
| `2605.07068` | `AGENT-MEMORY` / No Change — Existing Coverage |
| `2605.07079` | `MULTIMODAL-WORLD-MODELS` / No Change — Existing Coverage |
| `2605.07110` | `PLATFORM-SECURITY` / No Change — Existing Coverage |
| `2605.07112` | `AGENT-TOOL-CALLING` / No Change — Existing Coverage |
| `2605.07180` | `AGENT-PLATFORM` / No Change — Existing Coverage |
| `2605.07288` | `MULTIMODAL-WORLD-MODELS` / No Change — Existing Coverage |
| `2605.07442` | `PLATFORM-EVALUATION-SYSTEM` / No Change — Existing Coverage |
| `2605.07451` | `PLATFORM-EVALUATION-SYSTEM` / No Change — Existing Coverage |
| `2605.07514` | `MULTIMODAL-EMBODIED-VLA` / No Change — Existing Coverage |
| `2605.07547` | `INFER-SCHEDULING` / No Change — Existing Coverage |

## C. 明确不重开的 owner-day controls

前版另有 11 个 retained identity 在当前账本转为 `datacite_initial_created_owner_proxy` isolation：`2605.06675`、`2605.06869`、`2605.06890`、`2605.07021`、`2605.07076`、`2605.07111`、`2605.07161`、`2605.07243`、`2605.07594`、`2605.07728`、`2605.07985`。本轮核对其 v1 submission provenance 后接受 owner-day 隔离，不把它们并入 direct screening repair。

## 修复完成条件

1. A 组 18 项全部进入 retained，并完成 exact-v1 Evidence / Books Decision；B 组 10 项逐项恢复 retained，或留下能指出具体已知机制与为什么不构成增量的命题级 closure。
2. 重新计算 retained、direct closure 与 74 条旧 Evidence/Books disposition；不得继续复用 `74 + 561`。
3. 若出现新的 Integrate，只由 root 串行写入 Books，再由新的非作者 reviewer 做正文写后复核；No Change 也必须有当前 Books 命题级比较。
4. 更新 README、screening ledger、Evidence、Books queue/checkpoint 后再运行 validator、JSON、marker uniqueness 与 scoped diff-check。

