# 2026-09-11 Deep Books Decisions — Batch A

本文件记录 `DEEP_REVIEW_BATCH_A.md` 中已达到长期机制门槛、并在本批次写入唯一 Books owner 的 source family。
它只记录决策与正文锚点，不替代 exact-v1 Source Review。SearchAtlas 不属于本批次。

## Decisions

| Source Family | Decision | Stable owner | 正文锚点 | 吸收的长期命题 | 证据边界 |
| --- | --- | --- | --- | --- | --- |
| `SF-2026-ARXIV-2609-10812` | Integrate | `INFER-SCHEDULING` / Ch56 | `GPU 调度之前，Host Control Plane 也要有容量合同` 下的 exascale control-plane 段 | data plane 扩容前必须单独验收 replica discovery、streaming endpoint 与 bring-up deadline；HPC launcher 不等于 serving control plane | Aurora、Ray/vLLM fork、Llama-3-8B、PVC、ShareGPT 与披露 SLO；streaming/non-streaming 结果不可外推 |
| `SF-2026-ARXIV-2609-10964` | Integrate | `INFER-SCHEDULING` / Ch56 | `Ready 只表示可释放，不能自动把工作提交给 Engine` | 将 workflow readiness 与 engine release 分离；ready set、release budget 和 outstanding work 属于 workflow scheduler，已提交 turn 属于 engine | vLLM 0.20.2、所列 GPU/模型和 SWE workflow；单 seed，不证明质量、吞吐或生产多租户 SLO |
| `SF-2026-ARXIV-2609-10830` | Integrate | `PLATFORM-SECURITY` / Ch72 | `Membership Signal 必须先通过可识别性审计` | 低 loss 只有在 corpus count、register-matched controls、模型/precision 与 attacker contract 可识别时才是 membership sensor，不能直接产生删除或合规判决 | 六本英文书、OLMo-2/Pythia；样本、量化和退火信息有限，不支持 MIA 普遍无效 |
| `SF-2026-ARXIV-2609-10883` | Integrate | `TRAIN-DATA` / Ch27 | `Synthetic data：从“先生成再打分”到 Specification Compilation` 内的叙事行为段 | 数据内容无害不等于训练效果中性；叙事角色、persona、mixture 与独立 behavioral canary 应进入数据 lineage 和准入 | 合成故事与有限模型/recipe；亲和度对学习率敏感，不证明隐藏表示或普遍生产风险 |
| `SF-2026-ARXIV-2609-10895` | Integrate | `MULTIMODAL-EMBODIED-VLA` / Ch26 | `可执行评测先暴露控制缺口，低延迟生成再缩短缺口` 前半 | physical-action 评测必须执行结构化 action proposal，并以 endpoint、alignment、安全规则和 violation denominator 区分感知与可执行性 | 306 个仿真场景、7 个 MLLM、2,138 次决策；不含模型 latency 与真实机器人安全 |
| `SF-2026-ARXIV-2609-10915` | Integrate | `MULTIMODAL-EMBODIED-VLA` / Ch26 | `可执行评测先暴露控制缺口，低延迟生成再缩短缺口` 后半 | 单步多模态 action head 用训练期多候选换较低 latency；horizon、observation freshness、interrupt 与 controller commit 必须联合验收 | L40S/A6000、LIBERO 和有限 Franka 任务；`11x` 含 horizon multiplier，无开放环境安全证明 |
| `SF-2026-ARXIV-2609-10954` | Integrate | `MULTIMODAL-WORLD-MODELS` / Ch25 | `Prediction Error 不能替代 Update 的反事实效用` | continual world-model update 应建立 update/hold fork，固定 Planner 与环境重放，以 downstream return 决定 promote/hold/rollback | 三个连续控制任务、固定无 rehearsal 合同；存在预注册分析偏离，不证明所有在线更新有害 |
| `SF-2026-ARXIV-2609-10970` | Integrate | `INFER-TENSORRT-LLM` / Ch49 | `Chiplet Pool 与 Execution Plan 必须联合演化` | 长期 chiplet pool 与 per-workload execution plan 分层拥有状态，pipeline bottleneck 连接 architecture、compiler、mapping 与 P&R | Timeloop/Accelergy/CENT/CACTI 模拟与所列 Llama/Qwen workloads；不是已制造 silicon 的绝对性能证明 |

## Post-write checks

`2609.10964` 的机制作用在 workflow readiness 与 engine admission 的交界，但本次长期增量只改变“何时把 ready work 释放给
serving engine”的容量与 tail-SLO 控制；因此 canonical owner 取 `INFER-SCHEDULING`，Agent Workflow 只保留调用方 handoff，
避免在两个章节复制同一 release controller。

- 八个 source-family marker 在 Books 中各出现一次，且均位于目标章节首个 `Review notes` 之前。
- Ch56 将 ExaServe 的 control-plane capacity 与 Agent readiness/release 写在同一调度演进链，但保持两个不同状态 owner。
- Ch26 将可执行 physical-action evaluation 作为 latency 优化的前置 contract，未把仿真安全或 throughput 外推到实机。
- Ch25、Ch27、Ch49、Ch72 均保留旧方案成立条件、约束变化、owner/control flow、收益、代价、failure mode、fallback 与 exact-v1 边界。
- 本批次没有修改 SearchAtlas、Daily README、ROADMAP、Learning State 或其他日期。
