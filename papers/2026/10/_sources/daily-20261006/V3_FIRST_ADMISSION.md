# 首批准入校准：2026-10-06

作者 `/root/oct06_daily`；日期含起不含终，UTC窗口2026-10-05T01:00:00Z～2026-10-06T01:00:00Z。

## C01：UniRL本窗公开实现纠错，单家族多个事件

原始事件：[GitHub本窗commit查询](https://api.github.com/repos/Tencent-Hunyuan/UniRL/commits?since=2026-10-05T01%3A00%3A00Z&until=2026-10-06T01%3A00%3A00Z&per_page=100)，实际8项，未分页。正式公开事件时间再以对应PR `merged_at`核，不将author timestamp单独当first-public。

拟准入：训练/rollout可计算并不确保条件分布、reward目标和溢出状态一致 → #547纠正BAGEL图像上下文注入失效造成rollout/replay不同序列，#528明确定义sleep释放GPU与context-overflow训练mask契约，#403取消对旧reward曲线的错归因并改变prompt-video reward/precision → 必须把可运行/可测recipe与正确训练语义分开判断。拟评分2+2+2=6；具体纠错与负侧强制深入受影响内容，不通读全部库。

- [#547 / 0a82feb](https://github.com/Tencent-Hunyuan/UniRL/commit/0a82feb2240f8b3b2964ec95f4e60215f827b3cc)，committer2026-10-05T03:05:03Z。原core：batch被unwrap后`_source_image`仍找batch prompts，返回None；rollout走上游img2img prefill（SigLIP fixed-size/随机VAE/source canvas），trainer replay却用navit transforms，条件序列不一致。
- [#528 / 54cc7b6](https://github.com/Tencent-Hunyuan/UniRL/commit/54cc7b69698332b7c1b167b174263fe02ce81ea7)，03:34:23Z。原core：colocated engine memory_saver+weights_cpu_backup使sleep真实释放；AgenticTrainer fail-fast，AR warning；context_length传server并clamp剩余output预算；overflow状态（首轮前failed、截断末turn overflow）可选mask_overflow_loss；tool observation clipping与non-retryable4xx不重试。
- [#403 / 94e8f26](https://github.com/Tencent-Hunyuan/UniRL/commit/94e8f26b8768a3695b5985c2fa072e07d9dbfa0d)，09:09:19Z。原core逐次修正明确四knob混杂、eta/objective共线、旧reward只有audio-video无prompt term、bf16master→fp32与最终mode=all后旧斜率不再支持现配置；最终采用范围须核实际recipe，不能照录pooled斜率为新recipe收益。
- [#560 / 852c045](https://github.com/Tencent-Hunyuan/UniRL/commit/852c0454a6cb63592b2582358f88623870848df1)，14:55:24Z。core只收敛vLLM版本检查唯一runtime owner；拟作为本家族局部兼容事实，不以version guard再扩独立知识贡献。
- 其余4项：#553仅bump0.2（无release页，版本号不足准入）；#532/#531内部写作/agent规则，项目研究范围之外；#542实际五README/YAML的既有scorer部署校正，GenEval显式detector路径/download需要目录，GenEval2配置dataset缺条目failclosed（允许fallback须明确）与local缺list得0分开；无新API/数据格式。作为家族辅助事实、只报告，不独立新计分；root已读core与维护者纠偏独核通过。

## C02：Qwen Code v0.25.0发布事件

[精确release](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0)；GitHub API `published_at=2026-10-05T09:44:40Z`，落窗。release公开列表页首10tag，API首5tag的其他SDK/desktop为同CLI包装，不再计家族；nightly20261004等不移动至今日。

拟准入命题：remote tool的接受、授权、持久结果与重启恢复不能由UI请求成功推定 → stable0.25交付Workspace/Managed runtime，默认启用durable local-process+trusted-reboot recovery，并有outside Host deny、tenant scope、publication/writer deadline、lost-reply load idempotence等实现约束 → 发布行为与可恢复边界需要定点证据，不以功能条目数量扩池。拟2+2+2=6，权限/可靠性纠错强制深入具体采用内容；拟聚焦默认恢复和所有权拒绝边界，不以单release授完整安全保证。

特别去重：昨日已实际审#13064/#13069 UNKNOWN Broker拒绝，并明确原首公开9/29–30。今日release汇总不重复将其算新研究机制；若需要解释release行为只复用其具体有效结论。D2K-Bench2610.03226已昨日标准完成；repo init2026-10-05T02:45:19Z只同家族artifact，同事件技术内容无新delta，不重新列候选。

## 风险排除校准

Google CAPS官方Blog实际core和两arXiv完整题摘语义记录见[V3_SOURCE_STOPPOINTS](./V3_SOURCE_STOPPOINTS.md)。Google研究agenda按实际core排除已root校准通过（不称报告全文已审），04740科学范围排除，04721局部diagram机制潜力但first-public日期外缺，不误称已排除。

root非作者首批准入通过：C01/C02各2+2+2=6，纠错/具体发布约束深入受影响部分；Google core排除与两arXiv处置通过。C01 #528 createdSep27/#547Oct4，不称10/05首次bug发现；本日事件是main合入。C02默认策略#13211Oct3为release采用背景，不称Oct5新发明；#13406Oct5合入为窗内权限顺序纠错。最终证据/Books判断以正式日报与[V3_CANDIDATE_EVIDENCE](./V3_CANDIDATE_EVIDENCE.md)为准，不以此初步提案冒充最后验收。
