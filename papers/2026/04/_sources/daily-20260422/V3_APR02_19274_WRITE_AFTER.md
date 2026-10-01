# 2604.19274v1 HarDBench：非写作者 Books 写后复核

- 复核者：apr02（Ch72 本次段落由 root 写入；本记录不代替 04/22 日级 Gate）。
- 原始证据：[官方 exact-v1](https://arxiv.org/html/2604.19274v1) §3.2–3.3、§5.1–5.3、Tables 1–3；受测同一危险草稿的 CoJP w/o task framing 与 CoJP 配对，八个模型的 harmful-completion ASR 在带任务包装时升高，GPT-4o 为 23.50%→96.75%。作者用 GPT-4o judge 判定 harmfulness；Table 2 标题称 unsafe *response* rate，而正文称 *prompt* 被分类，不能把 85%→22% 当线上前置 guard 漏检率。HQ、CoJP 与训练配方的比较含额外变量，不作单因素或普遍因果保证。
- 实际写入：[Ch72「Guardrail 必须覆盖 Persuasion 与语义改写」](../../../../../books/part-06-ai-infrastructure/72-security.md)中 `SF-2026-ARXIV-2604-19274` 段，位于目标等价的说服/语义改写论点之后、Concept-level Suppression 之前。新段区分裸危险请求、同草稿编辑任务包装、输入拦截、生成后行为和良性编辑效用；把评测矩阵、judge 成本、有限主题/模型、多变量提示与线上外推限制放在同段，保留独立 policy/人工审阅的放行权。章末 Review note 与 exact-v1 身份、受限证据一致。
- 判定：该窄机制与相邻章节论证和原文一致，**实际写后 PASS**；未复现实验、未重新抓取全站来源、未验证本日 first-public 或 14 来源。可在 04/22 作者报告中把 19274 改为真实 Integrate，但本日状态仍为进行中，待其它候选、日期/来源、负侧及独立日级 Gate。

本次只读核了对应新增正文和相邻段落；`git diff --check -- books/part-06-ai-infrastructure/72-security.md` 通过。
