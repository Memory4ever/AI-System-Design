# ATTUNE v2：实际 owner 与 Books 判断

日期：2026-10-24；窗口：2026-10-23 BJT。作者：oct24_arxiv。仅本文件；未修改 Books、Report、State 或 index。

## 1. 身份、事件与去重

材料为 [ATTUNE: Agentic Throughput Tuning for LLM Training](https://arxiv.org/abs/2610.17528)，精确事件 `2610.17528v2`，不是 ATTUNER（`2609.36722v1`，query-side KV adaptation）。先对全 Books 精确检索 `2610[.-]17528|ATTUNE|attune`：只见 Ch45 的 ATTUNER 名称近似命中，没有 ATTUNE 同家族正文或 Review note。不能将其误作已有同论文采用。

官方 cs.DC 当前 `new` 页的 2026-10-23 replacement 区明确列出 v2；abs 保留 v1 `2026-10-13 00:49:11 UTC`、v2 `2026-10-22 17:55:03 UTC` 提交记录。公开日使用官方日公告与公告日程对应 BJT Oct23，不以提交时刻替代公开日。官方 comments 明确 v2 增加 AutoModel benchmark、production deployment、OpenRecipes，故是具名重要修订，不因只有版本号准入。

定点旧家族去重：先查 10-14/10-15 两份 Daily 及其 `_sources`，再按唯一精确 ID/全词 ATTUNE 搜索 `papers/2026/10/**/*.md`；只有本日 ARXIV 有命中，无旧同家族已审事件或评分可复用。不把这解释为 v1 无全球公开，也不恢复旧日报补审 v1。本窗只计一个 ATTUNE 家族的重要修订事件，**不重复家族评分**。

## 2. 必要证据复用及本窗增量

直接复用本日 [ARXIV.md 开头 ATTUNE Source-ready](./ARXIV.md)已实际读过的 current-v2 §2.2.4、§3.1–3.2/3.5、§4、§6.1–6.3；未重读旧版或全篇、未做新旧全文比较。

本窗新增评价不能合成统一实验：AutoModel 四项是原厂框架/H100重现后单 campaign、Opus5.5/web enabled、不同预算、没有 final remeasurement，部分模型曾用于开发；ported 四项则使用另一代理版本和隔离协议、共同 GPU-hour 预算、三 campaigns/final interleaved remeasurement。对本地复现 baseline 的增益与对其他机器/软件 published throughput 的增益分开。生产采用率与平均提速属于作者运营观察，OpenRecipes 是作者目录，不是本次独立部署或全训练验证。

可采用的长期命题：自动调参扩大 proposal 空间，不能把“跑得快/能启动/首步 loss 对齐”变成训练目标或完整轨迹保持的证书。v2 gate 已将 resolved configuration 分 known-invalid/known-valid/unknown，再做 first-step loss parity；该门会漏 optimizer-update-only faults 与 shifted mask，unknown 改动仍待审、生产仍需 full training 验证。数字证明受测配置的可行性，不建立通用无人值守生产正确性。

## 3. 实际 owner 比较：不由论文名称或框架反推

已读项目方法/指南和本日 checkpoint；实际比较 Ch36、Ch40、Ch41 的目标段与直接前后段，另看 Ch35/37 与 Ch42 交接。结果如下。

- **Ch36 `TRAIN-DISTRIBUTED-TRAINING`** 拥有通用组合计划、训练语义不变量、规划器/执行器/验证者分工。实际正文“从手写 Plan 到可校准的并行规划器”（当前约1299–1323）冻结 model/workload/hardware/parallel/kernel/profile，再经真实运行检查 throughput 与 convergence-equivalent work，强调 search 只提案、runtime 验证与静态回退；不是只存在标题。
- 同章“Generated Training Engine 必须沿 Evidence Ladder 晋级”（当前约1959–1963）明确优化 Agent 不能兼 correctness oracle，冻结 reference/harness、分开 bit-for-bit、trajectory parity 与 downstream parity，保留失败探索/硬件/数据顺序，说明长程检查费用、quality parity 不等数值等价及回退。这已经承载 ATTUNE 可保留的自动优化/外置正确性门主张。
- 同章“Silent Corruption 需要按 Forward、Backward 与 Update 分开防护”（当前约607–623）区分 forward/residual、backward/gradient、optimizer commit 检查与权限，明确 detector coverage 不完备。因而 ATTUNE 首步 loss 漏 optimizer-update faults 是对已写覆盖分层的具名反例，不是需要新 owner 的原则缺口；这里不把 bit-flip 与配置 bug 说成同一因果机制，只复用检查覆盖随执行相位变化的边界。
- **Ch40 `TRAIN-MEGATRON`** 的“Kernel Optimization 与并行策略相互约束”（约249–263）已有 local shape/kernel/communication-overlap 耦合，但此文不是 Megatron API 或专属并行算法新增，不能只因 ported recipes 用 Megatron 就落这里。
- **Ch41 `TRAIN-DEEPSPEED`** 的“配置可以运行，但语义仍然错误”（约192–205）及配置审查表（约207–221）已有 global batch/loss reduction、precision、ownership、offload 与实际证据要求；可消费通用训练合同，不应为一份跨 AutoModel/slime/Megatron 的 tuner 复制第二份机制 owner。

唯一最终 owner 仍选 **`TRAIN-DISTRIBUTED-TRAINING` / Ch36**，这是全文实际比较后的结论，不沿用 Source 中暂拟 owner 自动批准。

## 4. Books：具体已有覆盖（NC提案）

**结论：已有覆盖，不增正文、不加本家族末注。** 不是说同家族已经收录；是采用命题已由现有完整论证承载。本窗增量为更多 stack/生产/目录的评价证据，以及首步 gate 的具体漏检实例；它们没有改变现有“性能候选→独立执行证据→预声明训练质量/轨迹门→发布/回退”的设计选择。将 resolved-flag registry、first-step gate 或本次吞吐数字固化为全书默认实现，反而会缩窄或弱化既有 evidence ladder。

独立复核的精确 NC 验收对象是 Ch36 上述三处实际段落及前后交接，而非只验标题匹配：

1. planner/search 只提出性能候选；
2. 优化 Agent 不拥有 correctness oracle，验证层级与比较身份须声明；
3. 一项 detector 不能覆盖 forward/backward/update 全路径，短测量不替完整训练质量；
4. profile/stack 漂移或证据不足时保留成熟已验路径。

报告保留 v2 新评价协议差异、生产观察权限与 gate 漏检，不能因 NC 删候选、降分、跳过当前修订审阅，亦不把 NC 写成“该稿无贡献”。本文件只完成作者 Books 判断，待 oct24_reader 独立复核；不授实际写后或整日完成。
