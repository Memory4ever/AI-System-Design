# 12/18 首批具体准入与负侧

窗口[12/17 09:00,12/18 09:00)+08；实际读取2026-10-02。作者记录，不是非作者验收。

## 拟准入：Gemini3Flash发布的评价/安全采用边界

[原始Blog](https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/)全文核心已读，JSON-LD原值`datePublished=2025-12-17T16:00:00+00:00`，即12/18 00:00+08落窗；`dateModified=2026-03-19T17:52:33.903201+00:00`，不冒称当前HTML为不可变2025快照。事件是官方release Blog，不授独立card首公开时刻。

[官方model-card目录](https://deepmind.google/models/model-cards/)将Gemini3Flash列为Updated17December2025，链接`/models/model-cards/gemini-3-flash/` HTTP200实际redirect至[原PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Flash-Model-Card.pdf)，380481 bytes、6页，PDF封面PublishedDecember2025。已读核心card及必要安全段：

- p5–6明确automated safety eval不等于human/red-team；评价版本和query sets已改善，不能与旧model cards直接比较。
- p6明示FSF借用Gemini3Pro已测CCL结果，理由是Flash较弱、按risk acceptance criteria判断unlikely达CCL；这是厂商发布风险接受，不是对Flash逐项CCL能力的直接测量，也不是形式安全证明。
- 架构/数据多数回指Pro，thinking levels与更低token/latency只给产品能力，不披露自适应算法；3×和30%不作为配置无关系统收益。

**拟准入链：** 新model release常沿用家族/总能力判断→原始card具体披露evaluator revision不同比、CCL采用借用Pro结果的风险接受路径→发布门禁必须区分测量证据、跨模型推断与组织接受权限。拟2+2+2=6；安全信号深入受影响段，不从厂商声望倒推分数。请root校准：这是否有足够具体发布/评价增量；若入选，采用release事件与当前December2025card披露边界，不能声称拿到不可变上线版。

初步Books对读：Ch66开头约34–47已说明平均指标不抵消高风险失败；Evaluation Identity约218–228已绑定model/harness/environment/scorer，不能把两个不同realized协议的run当comparison。它们确覆盖一般版本/条件原则，但未凭这两处确认“借同家族更强模型CCL作子模型风险接受”的具体边界已覆盖。作者不先判整项已有覆盖或仅报告；待root校准后继续定点相邻和局部提案。

## 代表负侧

[OpenAI Academy for News Organizations](https://openai.com/index/openai-academy-for-news-organizations/)原始标题/核心说明是记者培训与机构合作，不改变模型/训练/Agent执行机制，范围关闭；搜索入口日精度不授落窗，但不影响排除。不把培训合作类比Agent机制。

[Gemini3Flash Blog性能/产品功能部分](https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/)不单独作为新机制准入：高thinking可调/30%少tokens和3×引用第三方比较未解释算法与完整匹配配置。不能由负侧将独立安全card一并排除；上项保留的是具体证据/风险采用边界。

## arXiv首批潜在增量

本日submitted发现缓冲不是public事件池。以下精确v1完整題摘已读，不因日期失败省略贡献；个体first-public仍缺，保留潜力但不列确定本窗候选：

- 2512.14100：reward model稳定性问题→logic-similarity reward+supervised GRPO联合目标→需核formal consistency与偏好/label权限分离，不能从logic词证明human alignment。
- 2512.14118 CogMem：长历史增长→LTM/DA/FoA持久层与每轮context重建→可改变策略记忆与当前证据的分工；保留memory机制潜力，不用认知比喻当新增证明。
- 2512.14142 Astraea：segment局部调度不优化Agent全链JCT→state-aware hierarchical HRRN及I/O wait KV manager→端到端request状态进入scheduling，保留INFER-SCHEDULING潜力。
- 2512.14151 ACPC：prefetch引入cache污染→TCN reuse预测+priority replacement→需要核硬件cache/模型KV不同状态，不照录L2/throughput数字；保留具体memory policy潜力。
- 2512.14220 difficulty：无groundtruth问题难度不可直接正确率定标→pairwise LLM compare+Bradley-Terry→difficulty估计与task正确性分离，相关/噪声注入不证明真OOD无偏；保留评价/curriculum潜力。
- 2512.14233 PentestEval：总end-to-end成功遮蔽阶段失效→六阶段配对评价暴露自主agent近乎全失败而单阶段不同→保留Agent评价反证，不因新增benchmark名称排除。
- 2512.14256 TEMP：WSC memory/mesh拓扑约束→tensor-stream partition、traffic-aware mapping、dual-level solving→高通信带宽换片上memory而受tail/traffic contention约束；保留TRAIN-DISTRIBUTED-TRAINING潜力。
- 2512.14273 Zoom-Zero：temporal localization与answer共享reward混淆→zoom-in reward+token-selective credit→保留多模态grounding/credit allocation机制。
- 2512.14313 Dynamic RAG：固定k+distractor/position压力→query-specific context-size classifier→保留受限query自适应context预算与验证潜力，未把“lost in middle”成熟原则计分。
- 2512.14427 document packing：packing不只吞吐→latent multihop在packing/单文档对照有差异且多付compute→保留训练数据组织增量，准入事实尚需正文明确差异/混杂，不因日期失败自动关闭。

来源查询/分页：ARXIV_LANGUAGE126行、ARXIV_SYSTEM15行、ARXIV_MULTIMODAL7行均实达无Next。宽language列表只查漏线索，不自动全部变候选；相关题名仍继续读完整题摘/必要准入正文。具体链接由本日原始查询保存ID；不存数百篇全文摘要。
