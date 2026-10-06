# 02/28 首批准入校准

窗口固定02/27 09:00～02/28 09:00 Asia/Shanghai。下列为完整题摘已读后的准入判断；日期随后以同ID原字段核查，尚不授当窗身份。题摘可复查 `inventory.json`（只复用原题摘，不复用旧评分/队列）及本轮 `V3_ABS_<id>.raw`。

| ID | 暂定准入 | 旧约束 → 原增量 → 改变选择 |
| --- | --- | --- |
| 2602.22268 AutoQRA | 技术准入曾为2+2+3=7；本窗日期隔离，不列确定候选 | 固定4bit后选LoRA秩忽略二者耦合 → 同预算层级bit/rank联合搜索 → 不再独立最小化量化误差再定rank。原v1 Submitted 2026-02-25T07:18:08Z早于本窗政策下界所需的02/25T19:00Z；registered 02/27T02:42:28Z仅给上界，不给first-public下界。需同identity原公开公告或本窗实质新增事件；不采用旧V2评分/Books完成态。 |
| 2602.22394 ViT registers | 候选 3+1+3=7 | artifact被归因于缺register → background shortcut与coarse supervision/lazy aggregation路径 → register不是充分纠偏，需核patch/CLS聚合。 |
| 2602.22424 Causality ≠ Invariance | 候选 3+1+3=7 | 能因果操控任务的FV被误作格式不变概念 → FV跨格式近正交，RSA选CV迁移较好 → 干预有效不证明抽象不变。 |
| 2602.22437 veScale-FSDP | 候选 2+2+3=7，root准入校准 | element/row shard与block optimizer冲突 → RaggedShard+结构规划 → partition应保留块语义并核通信零拷贝代价；多组件仍是单训练主线，不按宣传规模授9。 |
| 2602.22505 Masked diffusion rates | 候选 2+1+3=6（理论） | Euler KL界与强score假设限制采样解释 → 直接TV分解及FHS仅score误差 → 区分离散化误差与估计误差；深入核采用定理假设而非全proof。 |
| 2602.22593 Flying Serving | 候选 2+2+3=7，root准入校准 | DP/TP部署时固定、切换移动状态/重启 → weight shard views+KV adapter+communicator pool+safe transition → 可选在线重配置但须核layout/调度约束；多组件仍是单serving主线，不按宣传倍率授9。 |
| 2602.22217 RAGdb | EX：一次决定性正文核后关闭 | §3 hash compare跳过未变文件、TFIDF+substring及SQLite/ONNX是成熟组合；entity Recall和cold-start增量更新差额没有新增可选条件/失效边界，不用airgap和32×包装增量；日期不再追。 |
| 2602.22240 parallel code | 待定点核准入事实 | 正确代码≠可伸缩任务并行 → 三prompt/三runtime正确性与扩展评价 → 若揭示具体错配则改评价设计；不是仅看到LLM+HPC就收。 |
| 2602.22261 model switch | EX：一次决定性正文核后关闭 | 原PDF§3–§5的cache、规则、embedding/ML切换、用户阈值与固定Qwen3-4B最大模型比较仍是成熟组合；150 prompts×3重复、BERTScore以大模型回复为参照、NVML仅GPU能量未建立新的成立条件或失效边界。能量数字不授机制贡献，日期不再追。必要原段见V3_DECISIVE_EX_AND_WEB。 |
| 2602.22213 Taxoria | 排除 | seed taxonomy→LLM生成→validation→provenance/visualization仅成熟流程组合；题摘没有新增选择条件、验证机制或原失效边界，主题映射不足。 |

另明确领域题名筛除示例：22216病理RAG与22251分子材料Foundation均暂缓AI for Science/领域应用，不将通用RAG或多模态词汇当准入。小模型/理论/负结果不据标签排除。
