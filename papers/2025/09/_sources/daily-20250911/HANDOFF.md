# 2025-09-11 作者交接：首批准入校准

作者：Bacon。当前合同：[Research](../../../../../docs/RESEARCH_CONTRACT.md) §3–6、[Report](../../../../../docs/REPORT_CONTRACTS.md) §3.6。只处理北京时间 2025-09-10 09:00 至 2025-09-11 09:00；不授日级完成，不写共享文件。

## 首批需要 root 校准

下列是完整题摘支持的贡献潜力，不是已经确认落窗的候选。API `published` 与 abs 的 submission history 均是提交字段；本次没有拿它们或 DataCite 注册替代首次公开。精确 v1 abs 原响应已保存；当前官方页未见撤回说明。

| 材料 / 拟审版本 | 原约束 → 实际潜力 → 需要重新考虑的选择 | 日期状态 / 下一证据 |
| --- | --- | --- |
| [Hetis](https://arxiv.org/abs/2509.08309v1) | 异构 GPU 的算力与容量不匹配 → compute-intensive 操作选择性并行、Attention 按 head 交给低端 GPU、在线负载派发 → 模块级分工是否比静态整模型切分更合适 | v1 submitted 2025-09-10T06:06:51Z，非公开证据；需要日级公告或作者首次公开记录。若落窗，拟 2+2+3=7，读模块划分、通信成本和配置对照。 |
| [MoEpic](https://arxiv.org/abs/2509.08342v1) | expert 全量搬运造成低命中与加载停顿 → expert 纵向切为 top/bottom，以 top 热缓存提高覆盖并与下层预取重叠 → 固定 VRAM 下缓存单位不必是整 expert | 日期待核；若落窗拟 2+2+3=7，读切分等价性、prefetch 错误、CPU/GPU/PCIe 与 latency 分母。 |
| [Selective Induction Heads](https://arxiv.org/abs/2509.08184v1) | 固定 lag 的 Markov 任务不能解释上下文中因果结构选择 → interleaved Markov chains 与 3-layer 构造 → induction/copying 机制需要区分选结构与学转移概率 | 日期待核；若落窗拟 2+1+3=6；理论定点深入，不能外推自然语言因果推理。 |
| [Toxic Synthetic Text](https://arxiv.org/abs/2509.08358v1) | 合成数据被当作人类数据替代 → 激活 patch 后生成毒性文本仍存在词汇多样性缺口，下游 detoxification 退化 → 应验证支持集/多样性而不只看生成条数 | 日期待核；局部负面结果值得核，不因任务局部排除。若落窗拟 2+1+3=6。 |
| [AgentGym-RL](https://arxiv.org/abs/2509.08755v1) | 一开始长 interaction horizon 易冗余与坍塌、始终短则探索受限 → ScalingInter-RL 从短交互逐步扩大 → horizon 是训练课程变量，而非固定预算 | submitted 2025-09-10T16:46:11Z，项目页无首发时刻。拟 2+2+3=7；评价只核非 AI-for-Science 子任务及机制消融，不借科学应用重新扩范围。 |
| [SAPO](https://arxiv.org/abs/2509.08721v1) | 异步异构节点无法共享单一同步 policy → 各自持 policy、交换 rollouts → 要区分异步样本复用、异策略修正与网络运行证据 | 日期待核；拟 2+2+3=7。必须核 off-policy 权重/接受条件和受控对照，不把数千节点 demo 当普适收敛保证。 |
| [RewardDance](https://arxiv.org/abs/2509.08826v1) | CLIP/regression RM 的容量与输入限制 → 比较式 yes-token probability 与模型/context scaling → 视觉 RL reward 的参数化、成本及 hacking 诊断 | submitted 2025-09-10T17:59:31Z，非首公开。拟 2+2+3=7；“reward variance 保持”不自动证明 hacking 已解决，需独立 evaluator、人工评价及 mode-collapse 证据。 |

评分是供校准的拟议命题投入，不计入正式当窗候选分母；root 确认准入与日期后才冻结。

## 代表性排除 / 风险项

- `2509.08151` Trust Semantics Distillation：完整摘要讲设备 collaborator 信任评估，未给出可复用的 LLM 训练/执行或 Agent 委派可靠性机制；不是因为名称含 distillation 就收入训练章节。仅此摘要范围判断待 root 抽检。
- `2509.08203` Componentization：提出可编辑语义单元与微服务参考原型、4 人探索观察；没有具体生成机制、状态一致性条件或对照能够支撑新的 Agent 执行选择。排除理由不是“小样本必无价值”，而是本次摘要没有建立机制增量。
- `2509.08489` Prompt-Driven Image Analysis：现有检测、分割、inpainting、描述模块的组合及阈值建议，未指出新增可验证的通用机制或具体替代设计成立条件；不能仅凭 runtime 占比收入推理章。
- `2509.08827` RL survey：摘要给出文献组织与资源目录，没有明确挑战现有判断的评价盲区或新反证；综述身份本身不排除，当前声明不足准入。
- `2509.08646` Secure Plan-then-Execute guide：存在 control-flow integrity / indirect-injection 抵抗的安全声明，不能按“成熟步骤组合”机械关闭；保留潜力和日期缺口，若确认当窗须深入受影响的安全边界。

## 最新：Qwen单项通过及Z.ai窄分页已执行

root已实际独核Qwen完整正文/config精确对象/Ch22完整相关段，准入6分、11日04:00归属、三项机制已有覆盖NoChange通过。已同步正式日报1家族及受影响内容深入完成；其他七潜力日期仍隔离，非整日DAY。Z.ai `https://www.zhipuai.cn/zh/research?page=2`→`?page=3`实际请求均1397454 bytes，解析18可见条目Aug2026→Dec2025且重复，未跨Sep2025；原件/派生 `zai-page2.*`/`zai-page3.*`保留。仅此有限历史部分仍受阻，不再是“尚未执行分页”。本日作者研究再次ready交非作者DAY，仍进行中；不自授通过。

## 窄重开（2026-10-06T12:39:00+08:00，已获单项独核）

旧12:10作者ready停点被Qwen新官网可恢复原材料纠正，不推翻七项有效校准。[QWEN_REOPEN.md](QWEN_REOPEN.md)新增Qwen3-Next，官方date=`2025-09-10T20:00:00.000Z`对应11日04:00；完整核心、三必要原图反侧和Ch22实际机制对照已交接，请root新增首批准入/日期与Books处置独核，然后作DAY。没有把此事件挪入12日或将可执行官方API隔离为永久hold。最新README保持进行中；不自授新增项或DAY通过。

## 作者侧研究交接（2026-10-06T12:10:00+08:00，旧停点）

首批 root 校准已实际落 [INDEPENDENT_CALIBRATION.md](INDEPENDENT_CALIBRATION.md)。作者补完本轮可执行扫描、含糊/相关题摘与必要 v1 反侧，日报 [09/11](../../11/README.md) 已可作 DAY 独核，仍为进行中。不是已通过 Evidence/Books/DAY，也不自授正式当窗候选。

精确证据见 [EVIDENCE.md](EVIDENCE.md)，筛选/潜力日期保留集合见 [SCREEN.md](SCREEN.md)。请特别核：Selective §5.3 一般 Claim 未来工作；AgentGym Fig7无seed/CI且WebArena26 vs22非+10pp；SAPO外部策略likelihood/过滤与异构demo反侧；RewardDance variance不能证无hacking；08646 A.1 single-tool ReAct与§7.1 replanner破坏immutable条件；08151已核实际v1不是参数蒸馏，未发现可改变排除的主线机制。

日期仍未取得官方日级公告/作者首次正文完全落窗证据；七项与其他具体潜力只隔离，不打正式评分、不写Books。机构可恢复路径已实际执行：Anthropic172、Google月1→2/2与DeepMind页3→5、Meta真实Blog及publication页5、SeedBlog真实page0跨窗/论文US-CN缺list、Hunyuan正确host实际9当前条目。有限历史缺口与精确重开位置自包含于日报§2/5，不以尚未尝试的API作hold。

共享Books、月README、LEARNING_STATE untouched；没有stage/commit/push。作者随后独立启动12日，不等待五日全完才交本日。Books无正面拟增量交root，因为日期/必要证据尚不能授权；证据笔记的owner只为后续条件路由，不能当已有覆盖或自然段写入验收。

## 原始停点（保留初次记录）

官方scoped与supplement各146（start0/max200，无尾页），实际交85、并207、各独61；两次请求主题/分类不同，不再称同身份集合。207只为submitted-window discovery，不是首次公开事件/候选/全文队列。偏宽旧query210不继承为分母。Aristotle13:36实际DAY未通过A/B/C，作者13:49有限返修见[差额路由](DAY_DELTA_ROUTES.md)：35最小题摘潜力、EvolKV遗漏、Meta真实5→results6、08120/08318身份、08157风险预算改判已同步。请Aristotle仅核差额与最终六部分；Qwen/必要core不重审、不改Books。作者仍不授通过。

分类月列表仅定点浏览 `2509.08000` 至 `2509.08840` 标题作为查漏，CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA 不做全类逐项审阅。CV、RO 传输部分截断，不能称列表读完。日级 list 两种路径均未恢复有效公告，月列表不提供 day precision。当前作者仍在本日来源与题摘收尾；尚未 ready，root 可先校准上述首批。
