# 2026-05-14 Round5 Root Books Writeback

**状态：** Applied；等待 fresh non-author final review。

root 已按章节现有演进主线写入以下五个 Source Family，均位于首个 canonical `Review notes` 之前，并使用唯一的 `semantic-body-binding:<Source Family>:start/end`：

- `SF-2026-ARXIV-2605-12879` → `MODEL-SELF-ATTENTION` / Ch14：把 iterative Sinkhorn 的部署成本接到 train-then-compile 分支，明确仍为 dense quadratic attention、校准身份、causal boundary 与 fallback。
- `SF-2026-ARXIV-2605-13316` → `MULTIMODAL-EMBODIED-VLA` / Ch26：把 Action Diffusion 复用接到 freshness gate 主线，明确三轴 cache identity、proposal/commit 分权与 dense refresh。
- `SF-2026-ARXIV-2605-12913` → `TRAIN-SFT` / Ch29：在 offline distillation 与 student-only on-policy 之间补入 mixed-occupancy DAgger，并分开 rollout、teacher label 与 outcome owner。
- `SF-2026-ARXIV-2605-12863` → `PLATFORM-SECURITY` / Ch72：在 typed action/effect-time authorization 之前补入统一 typed-host/effect-system 分支，并保留 runtime check 与传统安全边界。
- `SF-2026-ARXIV-2605-13228` → `AGENT-TOOL-CALLING` / Ch78：在 retry state 后补入 abstract-intent resolver，明确其局部权限、`Finish` 禁止与 executor 的 effect commit。

`SF-2026-ARXIV-2605-13821` 保持 `No Change — Existing Coverage`；Ch84 已经承载 process-level state、meta-edit、evaluator isolation、budget、rollback 与 static fallback，不重复写入。

此文件只记录 root 写回事实，不替代独立语义复核，也不把作者实验外推为通用生产结论。
