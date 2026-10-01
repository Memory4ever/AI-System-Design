# Daily Research — 2026-09-20

**规范：** V3
**窗口：** 2026-09-19T09:00:00+08:00 ～ 2026-09-20T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-21T10:18:00+08:00

## 1. 结论

14 个 Daily 来源均按窗口检查。arXiv 的 Friday new/cross 批次在本窗开始前一小时公布，周五、周六不发布新的 announcement batch，因此本窗 arXiv raw identity 为 0。机构官方 GitHub 若已列入来源合同，不能另造“普通仓库活动仅归 Weekly”的边界；仍须逐事件按贡献合同筛选，而不是整库计数。

本窗共确认 5 个 raw identity，分别形成 5 个 Source Family：MiMo-Code 3 个彼此独立的 MCP connection、session orphan reclaim 与 failure persistence 修复均在贡献筛选关闭；UniRL 2 个主干提交通过贡献筛选并完成深入审阅。`07ac948` 将 SGLang `ServerArgs` 未知键从静默丢弃改为默认告警、可选 fail-closed，暴露 recipe typo/version skew；`a77575a` 新增 direct vLLM TP rollout 以及从 FSDP full-weight state 到 vLLM native TP loader 的 IPC 发布协议，并明确部分原地加载失败后的 poison/fail-stop 边界。最终漏斗为：5 个 raw identity → 5 个唯一 family → 保留候选 2、关闭 3、撤回/删除 0、Evidence 完成 2、Books 写回 queue 2。

两个 UniRL 候选均已完成长期知识写回：第 51 章吸收 framework→SGLang 的 live-schema 差集与 warn/fail-closed 边界，第 36 章吸收 FSDP→vLLM TP 的 canonical publication、receiver-native load 与部分失败 poison/rebuild。独立复核已核对正文唯一落点、证据边界和相邻衔接，本报告完成。完整记录见 [screening ledger](../_sources/daily-20260920/screening-ledger.md)、[closure locators](../_sources/daily-20260920/closure-locators.md)、[evidence notes](../_sources/daily-20260920/evidence-notes.md) 与 [Books queue](../_sources/daily-20260920/books-queue.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 官方目录按窗口检查；最近相关发布早于窗口 | 已检查 | 无当窗候选 |
| SRC-ANTHROPIC | Research 官方目录按窗口检查；最近可见条目为 09-17 | 已检查 | 无当窗候选 |
| SRC-GOOGLE-AI | Google DeepMind Research 与 Google Research publications 官方目录按窗口检查 | 已检查 | 无当窗候选 |
| SRC-META-AI | Meta AI/FAIR Research 官方目录按窗口检查 | 已检查 | 无当窗候选 |
| SRC-QWEN | Qwen 官方站与合同列明的官方研究/发布入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-DEEPSEEK | 官方 Research/News 入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 官方研究/发布入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-TENCENT-HUNYUAN | Hunyuan Research 与合同列明的 Tencent-Hunyuan GitHub 官方入口；UniRL 2 个主干提交完成筛选与深入审阅 | 已检查 | 无 |
| SRC-ZAI | 官方 Research、release notes 与研究/发布入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-BYTEDANCE-SEED | Seed Research、论文目录与官方发布入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客与官方研究/发布入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-XIAOMI-MIMO | MiMo Paper/Blog 与 MiMo-Code 高信号事件；3 个 identity 分属 3 个 family，完整题名/核心 diff 筛选后全部关闭 | 已检查 | 无 |
| SRC-MINIMAX | 中英文 Research/Blog、Agent Tech Blog 与官方发布入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-ARXIV | 十二目标分类官方 new/cross announcement cadence；09-19 08:00 北京时间的 Friday batch 早于本窗，周五、周六无新 batch | 已检查 | 本窗 raw identity 为 0 |

停止点与 denominator 边界见 [screening ledger](../_sources/daily-20260920/screening-ledger.md)。官方仓库不是按 commit 数量扩池；但合同已列明的官方项目入口中出现 correctness、interface contract 或 runtime architecture 变化时，必须逐事件完成贡献判断，不能整类推迟到 Weekly。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [`fix(sglang): surface dropped rollout arguments (#392)`](https://github.com/Tencent-Hunyuan/UniRL/commit/07ac948a5d70a1a08777920fd191390fc0556ac2) | 2026-09-20T01:27:56+08:00 | framework→engine 配置适配不能静默丢弃目标版本未知键；新增显式差集、默认告警与可选 fail-closed；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-SGLANG` [Ch51](../../../../books/part-05-inference-system/51-sglang.md)（已落实） |
| [`feat(vLLM): support direct vLLM TP rollout engine and vLLM native IPC weight sync (#480)`](https://github.com/Tencent-Hunyuan/UniRL/commit/a77575acaaf3ed54386b866747dda2a22d5b6b0c) | 2026-09-20T02:03:00+08:00 | 在 FSDP producer 与 vLLM TP receiver 布局不兼容时发布 canonical full tensors，由 receiver-native loader 完成 TP slicing/fusion；加入 manifest、receipt、版本与 poison/fail-stop；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)（已落实） |

MiMo-Code 三个关闭 family 不进入候选表、不评分；精确版本、核心说明与语义关闭理由见 [closure locators](../_sources/daily-20260920/closure-locators.md)。

## 4. 证据与知识整合

### [`fix(sglang): surface dropped rollout arguments (#392)`](https://github.com/Tencent-Hunyuan/UniRL/commit/07ac948a5d70a1a08777920fd191390fc0556ac2)

精确 commit 的说明、实现 diff 与文档共同显示：UniRL 先从 runtime 的 live `ServerArgs` 得到允许字段，再把 intent 中既不属于 live schema、也不属于 UniRL 自有 metadata 的键识别为 dropped keys；默认记录 warning，设置 `UNIRL_SGLANG_STRICT_SERVER_ARGS=1` 时启动失败。它修正了 recipe typo 或 SGLang version skew 可被过滤后继续运行、从而让配置“看似生效”的保护行为。长期增量不是某个环境变量，而是跨 framework/engine 配置边界的版本化验证：必须区分 framework-only 键和目标 engine 未识别键，并按风险选择告警或 fail closed。

证据只证明该 commit 的 SGLang adapter 行为与随附 recipe/documentation 变更；没有独立生产事故率、跨 engine 实验或性能 benchmark。第 51 章已吸收这条 interface-contract failure mode，同时保留低风险兼容告警与严格启动拒绝的共存边界。

### [`feat(vLLM): support direct vLLM TP rollout engine and vLLM native IPC weight sync (#480)`](https://github.com/Tencent-Hunyuan/UniRL/commit/a77575acaaf3ed54386b866747dda2a22d5b6b0c)

合并 PR、精确 commit 与核心 diff 显示：producer 以 lazy canonical full-tensor stream 暴露 FSDP state，vLLM 0.27 的 native loader 拥有 TP slicing、模型特定 fusion 与 layerwise load；协议把 publication/version、physical CUDA device identity、manifest、TP receipt 与 rank consensus 绑定到一次发布。由于 receiver 是逐层原地更新，partial failure 后旧/新权重可能混合，runtime 被 poison 并 fail-stop，不回退 legacy transport 继续服务。

作者披露的可运行范围是 Qwen3-30B-A3B、single-node FSDP4 + vLLM TP4、BF16、无量化、PP1/EP1、full fine-tuning；PR 记录 compile/lint/config/protocol checks 与一次 two-rollout FSDP4/TP4 run，但 final post-squash TP4 rerun 仍待 GPU。证据不支持多节点、量化、PP/EP、LoRA、任意 vLLM 版本或原子 rollback。第 36 章已吸收异构布局交接的 owner 划分，以及非原子加载失败后的 fail-stop 边界；不能把一次受限运行写成生产就绪。

更长的实现定位与证据边界见 [evidence notes](../_sources/daily-20260920/evidence-notes.md)。

## 5. 缺口与下一步

本窗没有待补扫来源、待审阅候选或待写回 Books 项。第 51 章已写入基于目标版本 live schema 的 unknown-key 差集、warning 与 strict fail-closed 分支；第 36 章已写入 canonical producer state、receiver-native TP transformation、device/manifest/receipt/version identity，以及 non-atomic partial load 后 poison/rebuild。两处均保留旧方案成立条件、失败边界和安全 fallback。

后续只有出现官方 revert、兼容性修订、final GPU validation 或新的 receiver/backend 证据时，才按新事件定点重开对应 family；不重复扫描本窗。

终态保留项：PR #480 的 final post-squash TP4 GPU rerun 尚未完成，且现有证据不覆盖多节点、量化、PP/EP、LoRA、其他模型/TP degree 或其他 vLLM 版本。该缺口不支持任何正面性能、生产就绪、Books 扩张或“这些环境也无遗漏”的断言；只有官方补充相应 exact-version validation/artifact 时才定点重开这一 Source Family。

## 6. 复核

复核者：Codex fresh non-author reviewer（未参与作者初版或 Books 写回）

结论：通过

独立终审核对了窗口、14 个 Daily 来源、arXiv announcement cadence、raw/family 归并、title + 核心说明语义关闭理由、撤回/修订/去重与原始空候选断言。终审发现并修正两项实质问题：其一，Tencent-Hunyuan GitHub 已在 Daily 来源合同中，不能把 2 个窗口内 UniRL contract-level commit 排除为 Weekly-only；其二，MiMo 的 MCP connection 与 session orphan reclaim 仅共享宽泛 lifecycle 术语，不应合并为一个 Source Family，故 3 个 identity 改为 3 个关闭 family。

两项 UniRL 候选均完成深入证据审阅与实际 Books 写回。write-after audit 核对第 51/36 章正文和 Review notes 的官方链接、唯一 source-family marker、旧方案边界、trade-off 与 fallback；没有把受限运行写成通用性能结论。scoped validator、Markdown、本地链接、marker 唯一性与目标 diff 检查均通过；机器校验只作为独立语义终审的补充。
