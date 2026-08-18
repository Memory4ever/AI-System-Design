# AI-System Labs：从机制实验到端到端系统

`books/` 回答一个设计为什么出现、怎样演进以及 trade-off 是什么；`labs/` 用可执行实验检验这些判断。
Labs 不按 84 章机械拆分，而是沿一条纵向系统主线推进：每个 Lab 接收上一阶段的明确产物，再暴露下一阶段
必须解决的新约束。

```text
可复现实验
→ 模型学习
→ Transformer
→ 自回归状态
→ 条件计算
→ 多模态与 World Model
→ Training / Distributed Training
→ Inference Runtime
→ AI Platform / Evidence
→ Agent
→ End-to-End AI Lifecycle
```

## 如何使用

1. 先阅读 [Lab Contract](LAB_CONTRACT.md)，明确一次实验的证据标准。
2. 按编号完成 Lab；第一次学习不建议跳过依赖。
3. 每个机制先完成 CPU correctness baseline，再决定是否进入 GPU、分布式或 Kubernetes 扩展。
4. 把实验结果写入 `reports/` 下由 [实验报告模板](_templates/EXPERIMENT_REPORT.md) 生成的文档；实现阶段再创建
   `src/`、`tests/`、`configs/`、`reports/` 和必要的 `manifests/`，本轮大纲不预造空目录。
5. 框架只能作为实现分支。报告必须先说明机制、状态所有权和验证合同，再说明用了哪个框架。

## 依赖路线

```text
00
└── 01 → 02 → 03 → 04
              ├── 05 → 06
              └── 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16
```

Lab 05～06 可以在掌握 Lab 03 后作为多模态分支推进；Capstone 仍要求 00～15 的契约都已理解。Lab 04 的
conditional compute 会在 Lab 09 的通信与 Lab 10 的执行计划中再次出现，不是孤立的模型结构练习。

## Lab 索引

| Lab | 核心问题 | 主要产物 |
| --- | --- | --- |
| [00 Experiment Contract](00-experiment-contract/README.md) | 怎样证明一个实验结论，而不只是让代码运行？ | 可复现实验合同与反例 |
| [01 Learning from Data](01-learning-from-data/README.md) | 参数如何从数据中获得可泛化行为？ | 最小训练循环与 generalization 诊断 |
| [02 Token to Transformer](02-token-to-transformer/README.md) | 一个 token 怎样穿过完整 Decoder？ | 可逐层对齐的最小 Transformer |
| [03 Autoregressive Runtime](03-autoregressive-runtime/README.md) | 自回归生成怎样把计算变成持久状态？ | Decode、KV 与 Sampling 状态机 |
| [04 Conditional Capacity](04-conditional-capacity/README.md) | 怎样增加参数容量而不让每个 token 激活全部参数？ | Dense/MoE 对照与 router/dispatch 证据 |
| [05 Multimodal Representation & Generation](05-multimodal-representation-generation/README.md) | 不同模态怎样进入共享计算并保持生成语义？ | 表示、融合与生成范式对照 |
| [06 World Model & Embodied Loop](06-world-model-embodied-loop/README.md) | 预测怎样进入 action-conditioned 闭环？ | 可回放的环境状态与控制循环 |
| [07 Training Lifecycle](07-training-lifecycle/README.md) | 一次训练怎样成为可恢复、可验证的模型资产？ | 数据到 checkpoint 的 lineage |
| [08 Post-training Branches](08-post-training-branches/README.md) | SFT、LoRA、DPO、PPO、GRPO 为什么是条件分支？ | 监督对象与状态成本对照 |
| [09 Distributed Training](09-distributed-training/README.md) | 模型、梯度与 optimizer state 怎样跨设备分工？ | Collective/TP/PP/ZeRO 状态账本 |
| [10 Inference Serving Engine](10-inference-serving-engine/README.md) | 多请求怎样共享 GPU 而不破坏生成语义？ | Batching、paging、speculative commit engine |
| [11 Distributed Inference](11-distributed-inference/README.md) | 推理状态跨节点后，谁拥有 locality、freshness 与 recovery？ | PD 与 state-aware scheduling control plane |
| [12 AI Platform Control Plane](12-ai-platform-control-plane/README.md) | 怎样把一次成功运行升级成可复用平台能力？ | Asset/workload/service desired-state loop |
| [13 Evidence & Governance](13-evidence-governance/README.md) | 观测怎样变成可审计的发布决策？ | EvalSpec、telemetry 与 release gate |
| [14 Agent Information State](14-agent-information-state/README.md) | Prompt、Context、RAG 与 Memory 的生命周期如何分工？ | 带 provenance 的 working/persisted state |
| [15 Agent Action & Workflow](15-agent-action-workflow/README.md) | 模型建议怎样变成可授权、可恢复的行动？ | Tool proposal、durable workflow 与 delegation |
| [16 End-to-End Capstone](16-capstone-ai-lifecycle/README.md) | 怎样把前述机制组合成闭环而不丢失身份与证据？ | Data→Train→Serve→Agent→Feedback 系统 |

## Books → Labs 反向索引

| Books 区域 | 首选 Lab | 复盘 / 下游 Lab |
| --- | --- | --- |
| Ch3～5 知识树、学习与表示 | 00、01 | 13、16 |
| Ch11～18 Transformer token lifecycle | 02 | 03、05、10 |
| Ch19～22 KV、Sampling、MoE、Long Context | 03、04 | 09、10、11 |
| Ch23～24 多模态表示与生成 | 05 | 06、10 |
| Ch25～26 World Model 与 Embodied | 06 | 14、15、16 |
| Ch27～35 数据、训练与 Post-training | 07、08 | 09、12、13 |
| Ch36～41 Distributed Training | 09 | 11、12、16 |
| Ch42～50 单机推理与 Serving Engine | 03、10 | 11、13、16 |
| Ch51～56 分布式推理、PD 与调度 | 11 | 12、13、16 |
| Ch57～65 AI Platform 控制面 | 12 | 13、16 |
| Ch66～73 Evidence、Observability 与治理 | 00、13 | 14、15、16 |
| Ch74～77 Prompt、Context、RAG、Memory | 14 | 15、16 |
| Ch78～84 Tool、Workflow、Multi-Agent、Platform | 15 | 16 |

精确 owner 以各 Lab 的 `Books / Stable Node Mapping` 为准；章节号只表达当前阅读顺序，Stable Node ID 才是长期
映射键。

## 五条横轴复盘

完成纵向路线后，再用同一批实验材料复盘五条系统原语：

- **Compute**：01 → 02 → 04 → 08 → 09 → 10。
- **Memory**：03 → 06 → 07 → 09 → 10 → 11 → 14。
- **Communication**：04 → 09 → 11 → 15。
- **Scheduling**：07 → 09 → 10 → 11 → 12 → 15。
- **State**：00 → 03 → 06 → 07 → 10 → 12 → 14 → 15 → 16。

横轴之间允许 `Layering / Dependency` 与 `Principle Reuse`，不应把相似状态误写成直接技术继承。

## 完成状态

目录存在不表示 Lab 完成。只有 README 中的 Acceptance Criteria 全部有证据、实验报告写明反例与未证明内容，
并且 Next Lab Handoff 的产物可被下一 Lab 消费时，才把该 Lab 标记为完成。
