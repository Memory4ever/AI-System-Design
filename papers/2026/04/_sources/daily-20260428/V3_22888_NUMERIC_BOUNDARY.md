# 2604.22888v1 RouteGuard：中心结果的有界算术复核

本页只复核 [官方 exact-v1 HTML](https://arxiv.org/html/2604.22888v1) §5.2–5.7、Tables 1–5 与 §6 的必要命题，并接续[早批四项消歧](./V3_EARLY_FOUR_EXACT_V1_TRIAGE.md)。这不是整篇复现实验、日期 Gate、正式候选评分或 Books 采用。

论文把 pre-execution `SKILL.md` 风险检测定义为冻结模型在固定 probe continuation 上的内部信号分类；层/窗口 attention 与 hidden alignment 的双 expert 经可靠性 gate 融合。传感对象是**执行前文本所诱发的内部响应**，不是 skill 安装、工具调用或 effect 的行为保证。作者 §6 亦限定为 open-weight Qwen3-32B、Llama3.1-8B 等受测 backbone，部分比较系统为 paper-faithful reproduction，并非原管线精确重跑。

标准二分类 F1 若由同一测试分母上的 precision `P` 与 recall `R` 计算，应为 `2PR/(P+R)`。官方表中的 RouteGuard 行至少有以下硬冲突（只用公开打印的四位小数复算；舍入不可能造成所示差值）：

| 官方表与切片 | P / R | 打印 F1 | 依打印 P/R 复算 F1 |
| --- | ---: | ---: | ---: |
| Table 1 SI | .8019 / .4218 | .7528 | .5528 |
| Table 1 MASB | .6393 / .5750 | .7867 | .6054 |
| Table 1 MASW | .6393 / .5750 | .7427 | .6054 |
| Table 2 SI-BL | .6077 / .7156 | .7945 | .6573 |
| Table 2 SI-CH | .9334 / .6442 | .8834 | .7623 |
| Table 5 BIPIA | .7501 / .9944 | .8537 | .8551 |

Table 3 将 SI/SI-BL/SI-CH 的 full 行再打印为前述冲突 F1；Table 4 又把 MASB 的同一 P/R 与 `.7867` 同列。尤其摘要、正文所强调的 SI-CH `.8834` 不可当由所列 P/R 支撑的已验 performance 数值；即便按复算 `.7623`，也不能仅凭此表确立“所有切片中融合显著优于每个单 expert”，因为 SI-CH attention-only 行 `.9329/.6465` 的 F1 约 `.7637`，与复算 full 几乎相同且略高。原始 confusion matrix、阈值和样本级预测未在该必要段给出，故无法判断究竟 P/R、F1 还是分母/表格拼接有误；不能据此断言 detector 实际无效或所有其余实验不成立。

现有 Ch72 的 Skill artifact 与 effect-time gate 已分开。`instruction-like carrier` 下的白盒预执行探测仍是可研究的局部信号，但上述中心表与核心宣传不自洽，**正面 Books 机制/优势采用暂缓**；建议保留有界安全纠错审阅提案，请非作者复核 exact-v1 数值与 Ch72 的实质差异。必要重开条件是作者提供同分母 P/R/F1、原始 confusion matrix 或勘误；若仅把本稿当受限传感器实例，也不得把 F1 排名或安全防护效果写为已证明。
