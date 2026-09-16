# Daily Research — 2026-05-16

**规范：** V3

**窗口：** 2026-05-15T09:00:00+08:00 ～ 2026-05-16T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-15T13:43:09+08:00

## 1. 结论

本次不继承旧报告“只检查 arXiv、候选为 0”的 Complete 结论。14 个每日来源均按当前窗口重新检查：arXiv 在本窗没有新公告 identity；13 个机构来源中有 2 个可精确落窗的原始事件。OpenAI 的 Malta 合作公告在题名与正文摘要语义筛选后于 Candidate Denominator 前关闭；ByteDance Seed 于 2026-05-16T00:00:00+08:00 发布的 Charon 进入候选分母。其余机构入口在有界列表中无窗内研究或系统发布。

Charon 的 arXiv v1 提交发生在 2026-05-17T05:28:22+08:00，晚于本日报窗口；这不改变 ByteDance Seed 官方研究目录已经给出的 05-16 首次公开事件，但意味着 exact-v1 全文是后续补强证据，不能冒充本窗 arXiv 命中。该 Source Family 已完成 exact-v1 深入审阅，V2 评分为 3+3+3=9，归属 `PLATFORM-EVALUATION-SYSTEM`。当前 Books 已明确承载“Training 与 Inference Simulator 共享版本化配置身份、分别用真实 trace 校准、发布仍需真实硬件 replay/canary”的机制与边界，因此本次 Books 决定为 No Change — Existing Coverage，不重复追加。

本窗漏斗为：2 个机构原始事件、1 个 pre-denominator closure、1 个候选、1 个深入审阅完成、0 个 withdrawn、0 个 blocked、0 个 Books 待写。非作者 fresh-context 终审已独立复核日期、候选守恒、exact-v1 证据和 Books 语义承载；05-19 的同 family 记录已按后续 arXiv evidence 调和，不再重复拥有、评分或执行 Books Decision。本日报完整闭环。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml)；逐项检查精确 `pubDate`。Malta 合作公告为 2026-05-16T08:00:00+08:00，落窗并在分母前关闭；05-15 的产品、企业合作与 Academy 条目均为 08:00，早于窗口起点 | 已检查 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)；官方页面时间字段由 2026-05-14T17:06:12.172Z 跳至 2026-05-22，窗口内无条目 | 已检查 | 无 |
| SRC-GOOGLE-AI | [Google DeepMind Publications](https://deepmind.google/research/publications/) 与 [Google Research Publications](https://research.google/pubs/)；相邻公开记录分别夹在 05-06/05-28 与 04-25/05-28 | 已检查 | 无 |
| SRC-META-AI | [Meta Research Publications](https://ai.meta.com/research/publications/)；有界目录相邻记录为 05-12 与 05-17/19 | 已检查 | 无 |
| SRC-QWEN | [Qwen 官方站点](https://qwenlm.github.io/) 与 publication/blog index；无窗内条目 | 已检查 | 无 |
| SRC-DEEPSEEK | [DeepSeek 官方研究入口](https://www.deepseek.com/)；模型与研究发布索引无窗内条目 | 已检查 | 无 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [MoonshotAI GitHub](https://github.com/MoonshotAI)；无窗内技术文章、首次公开仓库或 release，`pushed_at` 不作首次公开 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [腾讯混元 Research 全部列表](https://hunyuan.tencent.com/research) 与官方组织；相邻记录为 04-30 与 05-21 | 已检查 | 无 |
| SRC-ZAI | [智谱 Research](https://www.zhipuai.cn/zh/research) 与 release index；目录由 04-29 与 05-20 夹住窗口 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [官方论文目录](https://seed.bytedance.com/en/public_papers)；页面原始 `PublishDate=1778860800000` 对应 2026-05-16T00:00:00+08:00，命中 1 个候选 Charon；上一条 UAM 为 2026-05-15T00:00:00+08:00，早于窗口 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/) 与 release index；无 05-15/16 条目，最近明确技术记录为 05-09 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [MiMo Paper / Blog](https://mimo.xiaomi.com/) 与官方组织；论文索引在 03-13 后跳至 06-29，无窗内发布 | 已检查 | 无 |
| SRC-MINIMAX | [MiniMax Research / Blog](https://www.minimax.io/blog) 与官方组织；相邻研究记录为 03-18 与 05-26/27 | 已检查 | 无 |
| SRC-ARXIV | 只按本窗新增公告 identity 检查，owner-day inventory 为 0。Charon 的 `[v1] Sat, 16 May 2026 21:28:22 UTC` 等于 05-17 05:28:22 北京时间，属于窗外的同 family 后续证据 | 已检查 | 无 |

逐项筛选与日期换算见 [`screening-outcomes-v3.json`](../_sources/daily-20260516/screening-outcomes-v3.json)；机构覆盖依据见 [`non-arxiv-source-coverage-v3.json`](../_sources/daily-20260516/non-arxiv-source-coverage-v3.json)。`no_hit` 只证明注册入口的有界列表在本窗没有相关事件，不声称整个互联网不存在材料。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference](https://arxiv.org/html/2605.17164v1) | 2026-05-16T00:00:00+08:00 | ByteDance Seed 首次公开；arXiv v1 是窗外后续证据。训练与推理性能模拟从分裂工具演进为共享 graph/configuration identity 的 compiler-style pipeline，并把 profile、prediction、analytical backend 的选择与 fallback 显式化；3+3+3=9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference](https://arxiv.org/html/2605.17164v1)

- **身份与版本：** Source Family 为 `SF-2026-ARXIV-2605-17164`。窗口事件由 ByteDance Seed 官方目录的毫秒时间戳拥有；`arXiv:2605.17164v1` 的提交时间是 2026-05-16T21:28:22Z，即本窗结束后的 2026-05-17T05:28:22+08:00。正文审阅采用 exact-v1，不使用 v2 结论覆盖 v1。
- **旧方案与新约束：** 分离的 training/inference simulator 在单一工作负载、固定并行策略下简单且合理；当规划需要跨模型图、并行方案、硬件、网络、precision 和 runtime 比较时，两套输入与校准容易漂移，真机逐点 profiling 的 GPU 成本又随设计空间增长。
- **机制与状态所有权：** §3.1–3.5 将 native PyTorch/Hugging Face/vLLM 模型转为 operator graph，再以 pass 注入 TP/PP/DP/EP/SP、ZeRO、fusion、quantization 与分析；backend 为每个 operator 在 profiling、prediction、analytical engine 之间选择，并在不支持时按优先级 fallback。版本化 graph/configuration 拥有“比较的是哪个系统”的 identity，simulator 只拥有候选配置和预测值，真实 runtime measurement 仍拥有发布判断。
- **Evaluation contract：** §4.1–4.5 覆盖 Qwen3-8B、LLaMA3-8B、Qwen3-30B-A3B，训练侧使用 Megatron/VeOmni，推理侧使用 vLLM，并包含 Ampere/Hopper/Ada GPU 与不同集群规模。内存实验明确绑定 Qwen3-30B-A3B、8 GPU、FSDP=8、batch=2、sequence length=8192；§5 的 inference case 绑定 LLaMA-3 70B、NVIDIA Hopper、固定输出长度与 100ms 端到端 latency SLO。作者报告的 5.35%/3.74% 等误差只属于这些披露设置。
- **证明与未证明：** 论文证明其受测配置中 graph-based、multi-backend simulation 能贴近作者真机测量，并能用于 design-space proposal；没有证明未测 operator、动态 shape/data-dependent kernel、故障恢复、生产 tail、任意网络拓扑或跨版本 calibration 仍保持同样误差。论文没有独立 Limitations 章节；§4.5 已承认 runtime jitter、动态 congestion 与 data-dependent randomness 未被确定性建模。
- **Trade-off、failure 与 fallback：** 统一图提高 training/inference 比较一致性并减少重复建模，却扩大共享错误的传播面，依赖 profiling database、硬件校准和 graph lowering 完整性；stale profile、unsupported operator、overlap 模型失真或 search pruning 误杀会给出错误 Pareto frontier。早期规划可用 analytical/prediction backend 扩池；高价值候选必须回到 profiling，发布仍需真实硬件 replay/canary。小搜索空间、固定栈或缺少可信 calibration 时，分离 simulator 或直接真机 sweep 仍更合理。
- **Artifact 边界：** exact-v1 结论声称代码位于 `https://github.com/ByteDance-Seed/Charon`，本次访问返回 404；论文正文已足以审阅机制和实验，但不能据此声称 artifact 可复现、公开 commit 存在或代码与论文一致。
- **Books 对读：** `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的“Training 与 Inference Simulator 需要共享配置身份”已经逐项承载 shared configuration、真实 trace 校准、误差传播、适用边界与 hardware replay/canary fallback，并具有 `SF-2026-ARXIV-2605-17164` binding。当前正文与 exact-v1 一致，因此决定为 `No Change — Existing Coverage`。

完整作者审阅记录见 [`evidence-review-v3.json`](../_sources/daily-20260516/evidence-review-v3.json)，Books 对读见 [`books-comparison-v3.json`](../_sources/daily-20260516/books-comparison-v3.json)。

## 5. 缺口与下一步

无可执行待办。Charon 在 05-19 出现的是同 family 的后续 arXiv evidence，已完成 owner reconciliation；05-16 继续由 ByteDance Seed 官方首次公开事件拥有。

本窗终态保留项：

- Charon 论文声明的 GitHub repository 当前返回 404。该材料不用于正面证据、不进入 Books，也不支撑无遗漏断言或性能保证。定点重开条件是官方仓库或事件时 immutable commit 可访问；届时只重开 artifact 可复现性，不重做已完成的正文机制审阅。

Books 写回队列为空，见 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260516/root-books-writeback-queue-v3.json)。

## 6. 复核

复核者：`fresh-context:may16-nonauthor-final-20260915`

结论：通过

非作者终审重新打开 OpenAI Malta 官方公告、ByteDance Seed 官方论文目录、arXiv 版本历史与 exact-v1 HTML，确认严格窗口、14 个每日来源终态、2=1+1 守恒、withdrawn 状态、V2 三维评分、Stable Node、目标及相邻章节、Books 语义 binding 与外部 artifact 边界。OpenAI Malta 条目只涉及采用、访问和 literacy，不改变本项目机制，分母前关闭成立；Charon 的 05-16 官方事件与 05-17 arXiv v1 证据日期没有被混同。Ch66 的对应机制正文位于全局 `Review notes` 前，并实质承载 shared configuration identity、分别校准、共享误差风险和真实硬件 replay/canary fallback。完整终审见 [`V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md`](../_sources/daily-20260516/V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md)。
