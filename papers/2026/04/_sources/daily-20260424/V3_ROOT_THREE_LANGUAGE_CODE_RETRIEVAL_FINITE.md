# 2026-04-24 三项标准仅报告的有限非作者复核

复核者 root，2026-09-29。仅对下面三家族的精确 v1 必要机制、分母、具体 Books owner 与处置复核；不把这一批结果扩成整日 Gate。实验未复现。

## 2604.21593v1 Language as a Latent Variable

[官方 v1](https://arxiv.org/html/2604.21593v1) §4–5 中，每题五条 rollout 的语言约束改变 RL 的探索输入分布，一条不约束、四条从语言集合抽取。训练后无约束 greedy 解码及部分低资源语言上的变化，并不能识别“模型内部语言潜变量”是唯一原因；小模型全约束/全不约束消融还给相反的偏好方向。`TRAIN-RLHF` 的采样身份、有效探索和 format reward 分账已承载长期设计边界；本项语言 prompt 配比是可报告的受限配方，不必把未识别的隐变量命题写成主线。2+1+2=5，标准审阅、仅报告；非作者必要命题复核通过。

## 2604.21598v1 DryRUN

[官方 v1](https://arxiv.org/html/2604.21598v1) §3–5 在没有公共样例测试的输入下，先 refine plan，再用模型自造输入做 mental simulation，最后 polish 代码。旧的公共测试与真实执行具有可复算失败证据，仍是可用基线；自模拟换来测试稀缺时的候选改进，但不是外部执行 oracle。LiveCodeBench 的 80 题、两 API 模型、三次运行和 37 道 hard 子集的消融都只是局部设置；额外约 19 倍 token 是相对 direct 的特定比较，不是全调用 matched 的系统优势。`AGENT-REFLECTION` 和 `AGENT-PLANNING` 已把独立 execution witness 与模型自评分开，本篇没有改变该合同。2+2+2=6，标准审阅、仅报告；非作者必要命题复核通过。

## 2604.20851v1 HAT-VTR

[官方 v1](https://arxiv.org/html/2604.20851v1) §4–5 的 query-gallery 双向归一化、短期 score memory 与 LN 测试时适配，在视频文本检索域偏移下形成特定组合。相对 TCR 的每 query 延迟不是持平：RTX 4090、batch 16 下 32.27 ms 对 26.37 ms，其中 backward 21.2 ms；不能只报抑制 hubness 的收益。低扰动时简单基线仍可成立，检索 Recall 也不是 RAG 最终答案的来源支持。`AGENT-RAG` 已有 hubness、域迁移和证据支持分权；本组合提供受限视频检索操作点，不足以设为一般检索更新规则。2+1+2=5，标准审阅、仅报告；非作者必要命题复核通过。

三项完成不消除本日其余 Only、争议、日期和来源缺口，状态继续 `进行中`。
