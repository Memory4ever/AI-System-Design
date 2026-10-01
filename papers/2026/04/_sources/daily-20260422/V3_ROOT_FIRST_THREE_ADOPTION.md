# Apr22 首三项有限非作者采用核验

复核者：root，非本日报作者。已重读当前合同；本次实际打开下列官方 v1 必要段落，对照当前 Ch49/72/56 的真实论点。只核三项必要采用，不核全日日期、全部附件或来源 Gate，未复现实验。

## 2604.18592 — Two-dimensional early exit

[v1](https://arxiv.org/html/2604.18592v1) §3.1–3.3、§4.3、§6.4 实际已读。句子前缀和可用深度联合展开，旧句子补新层，累计 margin 触发停止；这个执行分支真实，不因分类任务而拒绝。作者用全部测试 embedding 预存后扫描阈值，speedup 是 sentence-layer abstract operations，不是实际 CUDA engine/wall-clock；最后层精度容忍门槛亦不是在线校准保证。复杂任务与微调后的反向切片保留。

`2+1+2=5` 标准仅报告通过：保留算法与实际未实现 runtime 的界线，不声称现章实现这一完整算法，不从 operation count 采用生产加速。不能只因没有通用生成结果而降为范围外。

## 2604.18658 — Owner-Harm

[v1](https://arxiv.org/html/2604.18658v1) §2.4、§4.6、§6.5 实际已读。采用同样内容在不同 owner resource/trust/authorization 下可有不同判定，不采用 Proposition1 必有 false negative 的强句：always-deny 是直接反例，但牺牲 utility。小 pilot 的 goal text 拼接退步，不证明结构化 goal-action 对照已成功；优化后、单标注者 diagnostic 不能冒充独立 validation。

`2+2+2=6` 安全边界深入、已有覆盖通过：实际 Ch72“Goal Alignment 不等于组合后的授权”两段完整承载数据范围×敏感性×目的地、owner authorization、dispatch/effect 分权及误拒绝成本。本结论不是主题匹配，也不声称书里已有作者 Datalog 算法或所有 benchmark 结果。不采用预测 ceiling、一般生产保护率或特定架构唯一因果。

## 2604.18788 — Static NPU MoE

[v1](https://arxiv.org/html/2604.18788v1) §3.1–3.2、§4.1–4.3、§5.1/5.8 实际已读。离线容量 tier 与 expert 热度决定同 tier grouped static graph 和 residency；host dispatch→固定 slice→weighted scatter 真实。编译时冷 graph 的 CPU fallback 与 overflow token 临时 spill 不是一回事，后者明确不能容易进行；saliency pruning 有损。group size/容量同时改变 launch、padding、overflow、超大 graph fallback，latency-best 与 energy-best 配置不同。

`2+2+2=6` 具体 gap 深入、写前通过：当前 Ch49“Routed Activation Materialization→Indexed Execution”实际解释 fixed capacity/padding 和 dropless materialization，但没有静态-only backend 中 tier×group×residency 的联动边界。可在该论证补最小条件分支，保留质量损失、校准漂移、CPU-NPU synchronization 与动态 backend/保守 padding 共存。只采用作者 M2Max/M2Ultra、FP16、prefill 主导、短输出 workload 的受限证据，不采用无损、通用 Decode/并发 SLO 或统一最优。

## 18788 实际写后复核

root 已实际顺读 Ch49 的 Routed Activation Materialization→Indexed Execution 约1055–1070行：原有 fixed-capacity/dropless 成本之后，两段补入静态-only 后端的容量等级、同级专家组与 graph residency，随后自然回到 indexed gather/reduce 分支。预置 CPU graph 不等于 overflow token spill、有损 pruning、校准漂移、图容量回退、latency/energy 不同最优点和质量/SLO边界均就近保留，未改变 routing 语义或将局部结果外推全服务收益。复用上述未变化的必要源证据，实际写后通过；未复现实验。三项单篇待办清除，不替代整日报告完成。
