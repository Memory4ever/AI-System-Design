# Pythia source → Ch56 非作者有限复核

- 判定：允许 **Ch56 最小增量**；不等于 04/29 日级 Gate 通过。核验材料为 [arXiv exact-v1 HTML](https://arxiv.org/html/2604.25899v1) §4.1、§4.2、§5、§7，与 `books/part-05-inference-system/56-inference-scheduling.md` 的 “Infrastructure-aware Multi-Agent Orchestration” 和 “Workflow Critical Path 与 Prefix Residency” 两段。
- 已有正文拥有 `ProgramState`、workflow dependency、真实 KV / queue / scheduler 权限分界，不能再复制一套 workflow 联合调度。真正缺口是**跨应用—Serving 边界的最小身份接口与预测生产者**：orchestration 只传 workflow type、session、agent role；Serving profiler 从历史路径与长度产生同一份可降级 forecast，供缓存、优先级和扩缩容消费，而不是由 Agent 直接给缓存/布局命令。
- 只在 Ch56 基础设施感知段后补短过渡，指向已有后文 critical-path 小节；预测为 advisory，真实 KV 驻留由 cache/runtime 核、容量/公平/SLO 由 scheduler 核。冷启动、路径漂移、不受控分支回退 reactive。不要把经验 99 分位数写成未来尾概率或 distribution-free 硬保证：union bound 仅在边际概率上界已经校准且适用时成立。
- 证据边界：论文使用生产 trace，但 §7 的性能比较是 3B–14B 模型映射到单机 8×A100 80GB 的回放试验，不能表述为生产上线效果；更不能把局部 TTFT 比值当工作流整体加速。书稿无需列倍率。
- Owner：`INFER-SCHEDULING`（Ch56）；Ch45 只保留 KV 实际身份/驻留，Ch63 只保留硬件 placement。完成实际写入后，仍须另一个非作者对改后正文、来源和相邻段做 write-after 复核；04/29 正式 Daily 及其整日 denominator 尚未冻结。
