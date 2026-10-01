# 04/30 智谱 Scaling Pain → Ch55 非作者实际写后核

复核者 root；书稿作者 apr01。范围仅 [智谱官方《Scaling Pain》](https://www.zhipuai.cn/zh/research/159)（页面标 2026-04-29 16:00 北京时间）§BugFix#1 与 `books/part-05-inference-system/55-pd-disaggregation.md` Handoff 状态机新增两段和 Review note；不验收 04/30 整日报告。

官方正文说明：Decode 超时 Abort 未正确传至 Prefill；旧 Prefill 计算与 RDMA 写继续，将已回收并分配给另一请求的 KV 槽位覆盖。修复为 Prefill 侧确认“相关写尚未开始”或“已提交写全部完成”后，Decode 才回收复用。书稿如实把它接在原有 source-copy/destination-commit 的正向 handoff 后，补反向 `abort → remote-write-retired → slot-reclaim` 次序；没有把作者实例写成所有引擎的普遍异常率，也交代了 ACK 往返、保留容量和失联清理代价。同步 handoff 或没有跨节点在途写时，较轻回收路径仍成立。Ch54 的 tier read-before-ready 只是相邻交接，不在本次重复写；LayerSplit 另待 owner 审阅。

**结论：通过本条 Source Family 的实际正文与相邻交接写后复核。** 作者机制陈述与我们的保守回退推断已分界；这不代表官方实验经独立复现、LayerSplit 已审毕，也不代表 04/30 的来源、日期、候选分母或整日 Gate 通过。`git diff --check` 对本章节改动通过；不 stage、commit 或 push。
