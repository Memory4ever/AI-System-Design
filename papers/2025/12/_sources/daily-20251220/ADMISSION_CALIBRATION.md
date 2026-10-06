# 12/20 首批准入校准请求

实际2026-10-02T19:51+08；窗口[12/19 09:00,12/20 09:00)+08。作者继续其余扫描，不等待校准。

- [Gemma Scope 2官方release](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/)：官方HTML `article:published_time=2025-12-19T12:00:00+00:00` =>12/19 20:00+08，落窗；modified=2026-07-06不当作不可变2025文本。完整核心已读。原有逐层SAE不容易连成多步计算解释 → Matryoshka多粒度字典、skip/cross-layer transcoders与chat模型工具 → 需要比较表示重建、跨层解释与因果干预的证据边界。拟准入而非只按270M–27B/110PB/1T参数宣传入选；技术报告必要机制/实验尚在读，评分待命题限定。请校准机制增量是否足以归Ch66（不是规模即贡献）。
- [Activation Oracles官方Blog](https://alignment.anthropic.com/2025/activation-oracles/)：完整核心已读；activation作为输入模态注入AO layer1，原模型训练AO后审fine-tuned激活，OOD审计3/4任务；强解释器可能自己推断而非目标表示，且多次forward成本。具体潜力成立但官方只December19日精度，不能授落窗；2512.15674v1已在19题摘读，不作为20新论文。精确Blog事件日期仍外部缺口，不评分/Books。
- [Bloom官方Blog](https://alignment.anthropic.com/2025/bloom-auto-evals/)：已读四阶段核心；相同seed不等同固定prompt，ideation/evaluator改变场景分布和elicitation rate，属于测量条件而非模型风险概率。潜力保留、只Dec19日精度不能落窗；必要评价部分可读，继续定点读完，不据日期缺口豁免。
- 代表性负侧：2512.16334电池寿命foundation model、2512.17152火灾传播物理WorldModel、2512.16424化学合成规划，题名明确暂缓AIforScience，仅应用foundation/world命名不建立本项目机制贡献；不补造公开日期。2512.16236 reranking演进综述题名含糊，仍需完整摘要，不按综述标签直接关闭。

ordinary尚未0；14源邻接、相关题摘、官方列表补检、artifactpatch、Scope必要报告/Books对读继续。
