# 2604.26256v1 DORA：Ch33 rollout 生命周期写前有限采用包

本包只供非作者核长期机制和实际 owner，不代表 Ch33 已写入或本日候选冻结。本家族按本批公告槽、连续 ID 与邻界作 04/30 08:00～09:00 北京有据推断；[exact-v1](https://arxiv.org/html/2604.26256v1) 的 04/29 Submitted 标签本身不证明首次公开。

## 真实差额

Ch33 现有约 1130–1151 行的 `Reserve→Occupy→buffer admission` 已要求完整 reward、版本 lag 和 abort 回收，约 1530 行的 partial rollout 已要求 prefix/version/mask 持久化。因此“支持异步”“有界陈旧”不是新知识。DORA §4.2–4.4 的不同选择是：同一 rollout 池同时保留多个 policy version，每个 DP group 仅载一个版本；完整轨迹先到先供 trainer 集齐 `TBS`，长尾仍在原版本继续；滑窗只有最老版本全部完成并送训才前进；在各版本剩余在途负载变化时重分 DP group，并仅在**同一版本**的实例间迁移 KV，避免因换权重而重新 prefill。算法合同与物理状态迁移因此被同一个 version identity 约束，而非只加一个 lag 数字。

建议唯一 owner 为 Ch33 `### 从“允许异步”到“用算法不变量约束异步”` 中现 lifecycle gate 之后、objective-level actuator 之前，两段自然续写（只拟 literal）：

> 完整轨迹 admission 还留下一个长尾调度问题：若每步强制换成新权重，未完长响应要么阻塞 trainer，要么跨版本续写，破坏单条轨迹的生成策略身份。一条条件路径是在 rollout 池中并存多个 policy version，却令每个 DP group 只运行一个版本。先到的完整轨迹可在集齐训练 batch 后交给 trainer，长尾仍由原版本续写；最老版本的全部在途轨迹完成并送训后才滑动允许版本窗口。这样把 `trajectory_id→generating_version→complete reward→training admission` 接到实际资源分区，但窗口越大越要检查 stale 影响，悬挂轨迹也可能拖住版本推进。
>
> 随旧版本未完请求递减，固定给它的 DP groups 会闲置；调度器可按各版本真实在途量重分资源，并在**相同权重版本**的实例间携带 KV 与请求状态，避免一次完整 re-prefill。KV 等价只成立在模型权重、prefix 与生成状态兼容时，不是跨版本免费迁移；P2P 权重/KV 传输、metadata、并发内存与 orchestration 均要入账。短轨迹、低负载或严格 on-policy 目标下，同步或单版本有界队列仍更易验证；资源利用率改善不能代替收敛与服务故障边界。

## 源证据与反例

- 官方 §4.2 明确 `RBS>TBS`、每 DP group 一个 policy version、long-tail 原版本续写和最老版本收齐再推进；§4.3 用版本剩余请求量重分 DP group；§4.4 才是同版本 KV 等价/迁移，不能把两者拆成独立通用技巧。
- §5 公开试验主要 16×8 H800、Qwen2.5-32B/LongCat-Flash、DAPO-Math-17k 的 64/128 GPU 配置；64 GPU 一组 E2E step 22.91→14.67 min 属该设定，不能作普遍吞吐或收敛保证。千卡级工业结果缺同等公开配置和完整对照，不据摘要倍数写正文。
- 非作者需核当前 Ch33 最新相邻段是否已有“多 policy 版本 DP group + 最老版本滑窗 + 同版本 KV 迁移”的完整三元选择；若有，则 Existing/Report Only，不因上面 literal 已备自动采用。Ch36 只掌资源调度/fabric，不另复制轨迹语义。
