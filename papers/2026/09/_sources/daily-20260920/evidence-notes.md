# Daily 2026-09-20 UniRL evidence notes

## `07ac948` — SGLang dropped rollout arguments

- 精确身份：[commit `07ac948a5d70a1a08777920fd191390fc0556ac2`](https://github.com/Tencent-Hunyuan/UniRL/commit/07ac948a5d70a1a08777920fd191390fc0556ac2)，commit header `Date: Sun, 20 Sep 2026 01:27:56 +0800`，title `fix(sglang): surface dropped rollout arguments (#392)`。
- 核心问题：旧 adapter 按 live `ServerArgs` 过滤 intent，但未知键可被静默丢弃；recipe typo 或 SGLang version skew 因而可能在任务继续启动时被误认为已生效。
- 实现机制：`_unknown_server_arg_keys` 从 intent 中减去 live allowed fields 与 `_UNIRL_ONLY_INTENT_KEYS`；非空差集默认记录 warning，`UNIRL_SGLANG_STRICT_SERVER_ARGS=1` 时抛出 `RuntimeError`。随附文档明确 UniRL-only 键和 Qwen3 colocate/async/LoRA recipe knobs。
- 采用命题：framework→engine 配置边界必须对目标版本 live schema 做全键归类；framework-only 与 engine-recognized keys 之外的差集是兼容性失败，低风险环境可观察告警，影响 correctness/security/topology/resource limit 的参数应 fail closed。
- 证据边界：官方 commit 支持实现存在与行为说明；没有独立生产 incident rate、跨 engine 对照、性能数字或所有 SGLang 版本的 schema coverage。
- 评分：Design Delta 3；System Reach 2；Durability 2；总分 7。纠错与 interface-contract 保护行为变化触发深入审阅。
- Books owner：`INFER-SGLANG`，第 51 章。

## `a77575a` — direct vLLM TP rollout / native IPC weight sync

- 精确身份：[commit `a77575acaaf3ed54386b866747dda2a22d5b6b0c`](https://github.com/Tencent-Hunyuan/UniRL/commit/a77575acaaf3ed54386b866747dda2a22d5b6b0c)，commit header `Date: Sun, 20 Sep 2026 02:03:00 +0800`，title `feat(vLLM): support direct vLLM TP rollout engine and vLLM native IPC weight sync (#480)`；[merged PR #480](https://github.com/Tencent-Hunyuan/UniRL/pull/480)。
- 核心问题：trainer 以 FSDP layout 持有参数，而 rollout runtime 以 vLLM TP layout 与 model-specific fused weights 装载；producer 若预先拥有 receiver layout，会把两端版本和 topology 细节耦合起来。
- 实现机制：trainer lazy 导出 canonical full tensors；vLLM 0.27 native loader 拥有 TP slicing、fusion 与 layerwise load。一次 publication 绑定版本、tensor manifest、物理 CUDA device identity、TP receipts 与 rank consensus；direct CUDA IPC handle 由 receiver 路径消费。
- 失败语义：layerwise in-place load 不是原子事务。任一 rank 或后续 layer 失败后，旧/新参数可能混合；实现选择 poison/fail-stop，而不是回退 legacy ZMQ/CPU 路径继续服务。
- 作者验证：PR 披露 compile/lint/config/protocol checks，以及 Qwen3-30B-A3B、single-node FSDP4、vLLM TP4、BF16、无量化、PP1、EP1、full fine-tuning 的 two-rollout 运行；final post-squash TP4 rerun 尚待 GPU。
- 采用命题：异构 trainer/rollout layout 的发布契约应由 producer 提供 canonical state，由 receiver-native loader 拥有最终 transformation，并以 device/manifest/receipt/version 证明完成；非原子 partial load 失败后必须 poison/rebuild。
- 证据边界：不外推到 multi-node、quantization、PP/EP、LoRA、其他模型/TP degree、其他 vLLM 版本或生产性能；一次受限运行不证明原子 rollback 或普遍稳定性。
- 评分：Design Delta 3；System Reach 3；Durability 3；总分 9，深入审阅。
- Books owner：`TRAIN-DISTRIBUTED-TRAINING`，第 36 章。

## Revision / dedup / withdrawal

两项 commit 是本窗首次处理的独立主干事件，不是同一 Source Family 的 revision，也不与 MiMo family 重复。精确 commit 页面与 merged PR 在复核时可用，所查 main 历史未见直接 revert/withdrawal；后续若出现 revert、兼容性修订或 final validation 结果，应以新事件重开对应 family，而不是静默覆盖本次边界。
