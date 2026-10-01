# 04/28 Seed 官方仓库发布：VeOmni v0.1.9a2 有界审阅

- 固定窗口：北京时间 `[2026-04-27 09:00, 2026-04-28 09:00)`，即 UTC `[2026-04-27T01:00Z, 2026-04-28T01:00Z)`。
- 原始入口：[ByteDance-Seed/VeOmni 官方 Releases API](https://api.github.com/repos/ByteDance-Seed/VeOmni/releases?per_page=100)，本次有效 JSON `17` 项；其中 [v0.1.9a2](https://github.com/ByteDance-Seed/VeOmni/releases/tag/v0.1.9a2) `published_at=2026-04-27T08:21:57Z`，明确落窗；邻近 v0.1.9a3 `2026-05-01T21:00:32Z`，不能回填。GitHub release 时间是此**版本事件**日期，不宣称所列 PR 机制均本窗首发。
- 只读该版本的变更表与三个对决定有影响的官方 PR：[kernel registry #678](https://github.com/ByteDance-Seed/VeOmni/pull/678) (`merged_at=04/23T15:17Z`)、[HF/VeOmni 数值对照 #670](https://github.com/ByteDance-Seed/VeOmni/pull/670) (`merged_at=04/17T20:38Z`)及[all-ranks-read 权重加载 #648](https://github.com/ByteDance-Seed/VeOmni/pull/648) (`merged_at=04/16T04:21Z`)。另外 [FSDP2 forward-prefetch #660](https://github.com/ByteDance-Seed/VeOmni/pull/660) 仅五增三删、PR 无非模板的评价，暂不因 feature 名称展开。没有审完整 24 条 release PR 或所有组织仓库。

## 精确事件与贡献判断

`#678` 把原先 monkey-patching 改为 `KERNEL_REGISTRY/KernelSpec→OpSlot`，并把 `moe_implementation=fused` 拆成显式 GPU `fused_triton` 与 NPU `fused_npu`，默认变 `eager`。不支持的 backend×硬件组合在 patch/bind 时抛错，而不是静默自动选 NPU 或退回另一实现。这是 release 的真实 breaking config；但 v5 才使用生成的 per-model `OpSlot`，v4 仍走 `LOSS_MAPPING`、全局或 legacy MoE patch 路径，不能把所有模型视作已统一到单一 registry。PR 披露注册算子的数值参考与 mock hardware-gate 测试，但未给完整模型/任务的收敛、不同后端生产性能或 deployment SLO。

`#670` 以三种随机初始化 toy 模型×两 dtype/attention 组合做 `torch.equal` 对照；测试命令关掉 Liger 与 fused kernels，并禁 TF32 等，故只证明**受测 reference path** 的 bitwise parity，不证明所有注册优化 kernel 或训练轨迹 bitwise 等价。实际修了 bf16 MoE router weights cast 与 expert 累加 dtype 两处数值分歧，属于版本兼容/证据有效性条件；不是另一个本窗论文首发。`#648` 区分每 rank 已完整读权重的 local split 与仅 rank0 读时确需 scatter，修正多余 collective；2×A100 与指定 5 模型的启动和 loss 对照不足以推通用训练吞吐。

现有 Ch49 已要求 backend、shape、dtype、硬件兼容作 feasibility gate，reference/fallback 必须显式；Ch36 对权重分片和 collective 的结果语义也已分离。上述三组没有改变这两章的长期权责，而是提供一个**具体 release migration / rollback 受限实例**：旧 `fused` 配置必须改写，不能在未核硬件/模型版本时默认继续执行。作者侧暂建议在 Daily 记为 `5 标准 / Books Only`，不为 registry 新建正文；因这个判断涉及 current Books 是否已承载 exact breaking condition，仍待非作者有限 source→owner 核。不得把 PR 合并日称为本日报新事件，也不得把 Version Fact 当整套框架性能保证。

已补查的 Qwen `qwen-code` Releases API 单项分页 p335 为 04/28T04:26Z（**本窗后**）、p336 为 04/27T00:25Z（**本窗前**）；Moonshot Kimi CLI 已有 1.39.0 04/24T06:22Z→1.40.0 04/28T13:51Z 相邻 release。PaddlePaddle/ERNIE 当前 Release API 仅一条 2025 项。这些是具名 repo 的**可见 release 层**停点，不证明组织所有分支或无标签提交零更新。
