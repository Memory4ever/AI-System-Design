# Weekly Research — 2026-W39

**规范：** V3
**窗口：** 2026-09-20T09:00:00+08:00 ～ 2026-09-27T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-09-27T10:00:00+08:00

## 1. 结论

本周是周日09:00截点的完整七天窗口，不是自然Monday～Sunday。09/26缺失日报和09/27当日日报已补齐并通过独立语义验收：分别有两项前分母关闭、零确认新事件，均无必要Books改动。它们没有把上一批arXiv或旧机构文章搬到周末。

29个每周来源的新增检查已结束在具名停止位置或隔离限制。有限来源审阅从五个提议收窄为四个贡献候选：verl的IPC释放回执、FlashInfer的调优资产身份、nccl4py的同步会话/调用身份、KServe的独立退出清理；METR评估经原文与具体现有命题对照后在分母前关闭，不因机构或模型名强留。四项必要增量已写进Ch36、Ch49、Ch61的原论证，实际写后验收汇总见§6。它们不是四种取代旧方案的新框架，而是不同边界上的资源复用与控制责任。

**整周尚未闭环。** 七份Daily当前有113个具名候选表行；按arXiv ID或原始URL检查未见键碰撞，但这不是113个最终周候选的证明，不能直接相加后冻结。09/22的来源身份/未决证据仍未恢复完，本轮官方列表对齐又发现09/21～23的arXiv公告日期及覆盖存在实际冲突；具体源级恢复正在进行。保留有效原文与Books机制证据，只重开受影响日期与判断，不重跑全年、不删除已经成立的知识。当前没有完成最终周分母、跨日技术关系与全周独立验收，故不标记完成。

## 2. 来源覆盖

### 每日来源：复用既有结果，具名缺口定点恢复

七份固定Daily窗口相接，覆盖本周：
[09/21](../../09/21/README.md)、[09/22](../../09/22/README.md)、[09/23](../../09/23/README.md)、
[09/24](../../09/24/README.md)、[09/25](../../09/25/README.md)、[09/26](../../09/26/README.md)、[09/27](../../09/27/README.md)。
09/20日报不在本周七份之内。复用证据不等于复用旧完成标签；本轮没有重抓整个每日来源组。下表前14行为每日来源复用，后29行为每周来源新增扫描，依据[每周发现记录](../../09/_sources/weekly-2026-W39/weekly-source-discovery.md)。`100+next`表示第一页100项后止于远早于窗口的历史段，不表示读完所有历史页。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 七日官方目录/RSS与报告所列实际停点；周末最新八项核日期 | 已检查 | 09/26业务案例关闭；各日受限声明不外推零遗漏 |
| SRC-ANTHROPIC | 七日Research与具名公告；周末公开字段和Nine Loops原文 | 已检查 | Opus5.5 system card的日级日期可在周窗定点重新判断，不能用METR评价替代厂商机制 |
| SRC-GOOGLE-AI | 复用DeepMind/Research各日查询与原文 | 受阻 | 年级Publications不能证明日级零新增；09/24 private-memory必要白皮书仍不可用 |
| SRC-META-AI | 复用各日目录/替代results与09/25 MaD-RL线索 | 受阻 | MaD-RL仍需可读原文；周末目录不可达不归零 |
| SRC-QWEN | 七日官方目录/artifact及09/27恢复的60/40条列表 | 未完成 | 09/24空壳身份与09/22目录重建尚须定点reconciliation，不能以当前列表抹去旧缺口 |
| SRC-DEEPSEEK | 各日报News、研究索引与周末可见十项 | 受阻 | 查看全部/API Docs入口未恢复范围被隔离 |
| SRC-MOONSHOT | 七日平台博客、明确发布与具名artifact | 已检查 | 仅覆盖记录所列仓库/版本，不外推全部branch |
| SRC-TENCENT-HUNYUAN | 复用publicList、UniRL等具名原始事件 | 已检查 | 显示日、publicAt和更早arXiv需分别理解；迟发博客不重复评分 |
| SRC-ZAI | 复用Research/notes/release；周末15项完整目录 | 已检查 | 既有ZCode日级事件在周窗定点对齐，不重新扫描全站 |
| SRC-BYTEDANCE-SEED | 复用论文/Blog目录，周末官方API返回数量与publish字段 | 已检查 | 只用PublishDate，不用UpdateTime冒充首发 |
| SRC-BAIDU-ERNIE | 复用Blog窗口停止点与明确release | 已检查 | 不扫描普通Paddle活动 |
| SRC-XIAOMI-MIMO | 七日Paper/Blog与contract事件，周末恢复无日期卡片 | 未完成 | 较早日级Date Hold的实际归属及旧window内机制须定点核，不从当前零命中倒推 |
| SRC-MINIMAX | 复用Blog/明确release，Agent壳目录已由llms.txt恢复 | 已检查 | 只恢复实际关联入口，不全面审所有commit |
| SRC-ARXIV | 复用12分类各日列表；09/26～27无常规公告，09/22具名恢复另执行 | 未完成 | 09/21～23列表标签与北京时间对齐、旧身份/排除依据和必要证据尚未闭合，见§5 |
| SRC-MISTRAL | News可见顶部日期段，最新09/16，停于09/10～08 | 已检查 | 未逐按钮遍历87篇历史正文 |
| SRC-AI2 | Papers首页1～10、Latest research及官方域名补检 | 受阻 | 只标年份，Next未执行；需要当窗dated archive或具名论文公开日，不证明零新增 |
| SRC-BLACK-FOREST-LABS | Research三张卡至尾，最新03/03 | 已检查 | 限该公开入口 |
| SRC-PHYSICAL-INTELLIGENCE | 主页/Blog/Research/裸域及官方域名补检 | 受阻 | 403或抓取失败，未恢复可采用本窗原文 |
| SRC-WORLD-LABS | Blog研究与News可见卡至尾，最新09/01 | 已检查 | 旧Atlas不重入选 |
| SRC-SSI | Updates三项至Back，最新07/26 | 已检查 | 主页方向不是公开算法 |
| SRC-REFLECTION-AI | Blog两篇与News十项至尾，最新07/14 | 已检查 | 组织采购/融资不作机制 |
| SRC-AMI-LABS | Updates唯一03/10与主页方向 | 已检查 | 不将成员旧成果冒作机构当窗成果 |
| SRC-THINKING-MACHINES | Connectionism七项至尾，最新07/31 | 已检查 | 产品导航不当研究 |
| SRC-PRIME-INTELLECT | Blog09/23→09/17→08/28段与Sandboxes核心 | 已检查 | 组合成熟隔离/调度原则，前分母关闭 |
| SRC-SAKANA-AI | Blog09/25奖项、09/24advisor至09/18段 | 已检查 | 两组织事件关闭，不读旧论文重计 |
| SRC-RECURSIVE | Recent Stories与具名置顶研究日期06/11 | 已检查 | 窗外研究未全文重审 |
| SRC-MIND-LAB | 重定向后的Publications六项、Updates09/22→09/02与V1.1核心 | 已检查 | 局部产品迭代未分离替代解释，关闭 |
| SRC-SAND-AI | 组织11仓到尾、三相关release/News，MAGI-2核08/05 | 已检查 | 普通push不是新研究 |
| SRC-EVERMIND | EverCore两卡恢复01月/04月论文版本身份 | 已检查 | 未标日期新产品的覆盖限制，不算窗内候选 |
| SRC-METR | Research/Risk Assessment与Opus5.5原文核心 | 已检查 | 具体已有评价合同，无独立长期增量；私有生产率不采用 |
| SRC-PYTORCH | releases69项到尾，最新09/02 | 已检查 | 不扫描普通PR |
| SRC-MEGATRON-LM | releases46项到尾，最新09/18；README顶部News | 已检查 | README月级旧条目不重计 |
| SRC-DEEPSPEED | releases100+next，最新09/16，停2021年历史段 | 已检查 | 未遍历next历史页 |
| SRC-VERL | releases16项到尾，v0.9.1及必要#7873/精确版本代码 | 已检查 | 采用发布中的保护变化，不冒充机制首次披露 |
| SRC-VLLM | releases100+next，v0.30核心与旧PR日期 | 已检查 | 已知FastStart/scale-out首次机制窗前；未审762个普通commit |
| SRC-SGLANG | releases61项到尾，最新09/18 | 已检查 | 不由其他项目引用扩大PR队列 |
| SRC-TRITON-LANGUAGE | releases7项到尾，最新08/28 | 已检查 | kernel language，不是推理服务器 |
| SRC-FLASHINFER | releases100+next，0.7.0/rc4归一；Autotuner v2 §1～5 | 已检查 | 默认/experimental/已知错误均限定，不采用宣传倍数 |
| SRC-NCCL | releases17项到尾，页内nccl4py0.6及pinned调用合同 | 已检查 | 不是新C++ NCCL发布，device API experimental |
| SRC-HF-TRANSFORMERS | releases100+next，最新09/09，停2024年段 | 已检查 | 未遍历next历史页 |
| SRC-KSERVE | releases63项到尾，0.21/rc1归一，必要#6156与版本代码 | 已检查 | user-authored route重渲染反例仍未解决 |
| SRC-RAY | releases100+next，最新08/23，停2020年段 | 已检查 | 未遍历next历史页 |
| SRC-MCP | releases9项到尾，最新07/28 | 已检查 | 未全扫所有议案、SDK与普通PR |

没有确认需要全站扫描的按需触发；为上述候选打开必要官方代码/原文是证据审阅，不是将该机构整个网站升为每日来源。

## 3. 候选与判断

以下四个**每周来源新增处置家族**已确认贡献与发布事件。rc/正式版本归同家族；PR的更早机制日期保留，精确身份检索未在已有9月报告找到相同采用事件，不把迟到发现写成新算法。Daily候选仍按各自原文记录复用，但受影响日期完成恢复前不冻结整周分母，不将113表格行与四项机械相加为最终候选数。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [verl v0.9.1：final ACK / IPC cleanup](https://github.com/verl-project/verl/releases/tag/v0.9.1) | 2026-09-20T15:24:43+08:00 | 数据处理完成与共享映射释放回执分开，GC延时不是协议正确性。3 + 2 + 2 = 7 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md#数据可用存储可回收与同步会话可复用不是同一种完成) |
| [FlashInfer v0.7.0：Autotuner v2](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.0) | 2026-09-22T09:15:03+08:00 | winner复用绑定测量路径、执行身份与rank一致性。2 + 2 + 3 = 7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md#调优结果也是带执行条件的可复用资产) |
| [nccl4py v0.6.0：session / artifact / event合同](https://github.com/NVIDIA/nccl/releases/tag/nccl4py-v0.6.0) | 2026-09-24T01:51:45+08:00 | 显式全组收尾防静默失同步，成套artifact与有类型event限定复用。2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md#数据可用存储可回收与同步会话可复用不是同一种完成) |
| [KServe v0.21.0：group member cleanup](https://github.com/kserve/kserve/releases/tag/v0.21.0) | 2026-09-26T01:04:20+08:00 | 退出清理不能被无关peer terminal配置错误压掉retry。2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-KSERVE` [Ch61](../../../../books/part-06-ai-infrastructure/61-kserve.md#desiredapplied-与-observed-不能压成一个-ready) |

两个6分家族因真实保护/兼容调用条件变化深入审阅，不为配合写Books抬分。METR、Prime、Mind、Sakana及vLLM已关闭的具名主张不进入此表；理由见发现记录和源级审阅。

## 4. 证据与知识整合

### [verl v0.9.1：final ACK / IPC cleanup](https://github.com/verl-project/verl/releases/tag/v0.9.1)

`SF-2026-VERL-0-9-1-WEIGHT-REFIT`；release commit `1876b06d0a3e4e71e06230be10af14492ca8a75b`与必要[#7873](https://github.com/verl-project/verl/pull/7873)，后者09/15已公开。pinned receiver cleanup先等待最后device引用、删除buffer/共享view，再发最终ACK；早发ACK可能令sender回收时consumer引用仍存活。作者单节点Qwen3-0.6B、VeOmni/FSDP2、vLLM TP2、GSM8K、2048MiB bucket三组allocator对照支持次序解释，不证明端到端吞吐、任意callback、direct大tensor、其他后端或多节点。GPU、precision、长度、并发、SLO为Not Disclosed。Ch36新增的是数据ready/producer-reclaim边界，不改Checkpoint或policy原子commit。具体审阅与对照见[verl/NCCL笔记](../../09/_sources/weekly-2026-W39/verl-nccl-review.md)。

### [FlashInfer v0.7.0：Autotuner v2](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.0)

`SF-2026-FLASHINFER-AUTOTUNER-V2`；§1～3/§5及release commit `4d75a33f19aaf48b44d5b1c5dbca33bc1eca5c58`支持测量路径改变排序、环境/operation identity和共享发布后的rank convergence。Ch49现有真实shape/kernal-vs-layer比较没有说明winner资产的复用条件，因此正文在比较之后补三段。validation hook可选，atomic rename只防半写，barrier/reload依赖同构rank与共享存储；一致性不等于全局最优，默认兼容策略不等于自动启用新策略。未复现、不采用宣传倍率。独立写后审阅纠正了“稳定摊销”不足以证明排序，以及Graph必须测captured replay两句，见[实际写后复核](../../09/_sources/weekly-2026-W39/kserve-metr-review.md#3-flashinfer-ch49-有限写后核查)。

### [nccl4py v0.6.0：session / artifact / event合同](https://github.com/NVIDIA/nccl/releases/tag/nccl4py-v0.6.0)

`SF-2026-NCCL4PY-0-6-0`；release/pinned commit `893470119efc83fb6ecd4f9240efcf60c0aef6a3`的barrier模块说明、communicator字段和matching header/IR合同支持采用。全组uniform teardown缺失可使后续barrier不再同步而不挂起；launch event不能抹去类型/rank/group/lifetime及CUDA版本语义。Ch36在IPC之后自然进入session reuse，保留成熟collective分支，不把API文档当性能实验或生产保证。未执行GPU/JIT，必要上下文及反证见上述verl/NCCL笔记。

### [KServe v0.21.0：group member cleanup](https://github.com/kserve/kserve/releases/tag/v0.21.0)

`SF-2026-KSERVE-V0-21-0`；commit `d1482554fc4f66dd41aee70e01f5174e24f265bd`的Reconcile与group cleanup，以及09/08先公开的[#6156](https://github.com/kserve/kserve/pull/6156)。cleanup先于normal reconcile，日志可合并错误，但返回清理错误保持独立retry classification。Ch61已有desired/applied/observed，没有说明删除等待无关peer配置可造成无限终止依赖，故在该段与发布之间补生命周期分支。只限controller-owned route；user-authored规则可能从spec重加peer，权限拒绝不是资源absence。作者manager/envtest与fault injection未由本任务执行，详见[KServe/METR审阅](../../09/_sources/weekly-2026-W39/kserve-metr-review.md)。

四项的关系是**Principle Reuse / Layering**：先区分通信资源的使用/回收/复用，再把可复用计算选择变成有条件的资产，最后在平台退出时保持清理所有权与错误重试权。不是verl→NCCL→FlashInfer→KServe的取代史。旧串行同步、固定tactic与简单服务拓扑仍在低复用、条件不匹配或协调成本高时成立。全周其他技术演进仍待Daily身份恢复后整合；这里不以四项代表整周全部成果。

## 5. 缺口与下一步

**普通可执行工作，非外部Blocked：**

1. 09/22旧arXiv733身份/68暂列与当前官方批次的实际身份对齐；已有原文及已写Books保留，不靠旧Complete或submitted时间验收。恢复入口为其[筛选记录](../../09/_sources/daily-20260922/screening-ledger.md)、[证据记录](../../09/_sources/daily-20260922/evidence-notes.md)和[Books队列](../../09/_sources/daily-20260922/books-queue.md)。本轮new/recent同组对齐发现09/21～23公告归属冲突，须先保存原字段和集合证据，再只修受影响日期；不能把列表总量扩为全文队列。
2. 09/22剩余必要审阅、具体已有覆盖/正文写后复核；H-Spec官方首发及已验收机制不因arXiv身份清单丢失而全部重做。
3. 跨日/周家族及事件reconciliation：Opus5.5 card、ZCode、MiMo日级Date Hold在完整周窗可以定点恢复；不以METR报告替代system card，不据当前目录反推历史正文。Google private-memory白皮书、MaD-RL原文等按必要材料实际结果隔离或采用。
4. 完成全周候选处置与技术关系，安排未参与作者/写作的最终语义复核，才能标Weekly完成；四项已落实不替代整周验收。

**已隔离的外部保留项：**PI四官方入口失败/403，需要可读当窗官方目录或具名作者原文；Ai2年级/未恢复日期入口需要dated archive或具体公开日；Google年级Publications与未得白皮书、Meta具名原文/日期、DeepSeek未恢复入口需各自必要原始材料。只重开对应来源/家族，不请求整个年度资料、不将这些项支撑Books或无遗漏断言。五个release长列表的有界历史停点保留召回限制，出现具名draft/re-publish/RFC时才定点重开。

2026-09-27用户改定执行优先级：最新09/27 Daily已闭环后继续4月。W39仍为进行中，本轮暂存其恢复队列，不把周报未完成误说成最新日报未完成，也不阻塞用户明确指定的4月任务。09/21恢复入口为[本日恢复笔记](../../09/_sources/daily-20260921/arxiv-recovery-20260927.md)，09/22的旧38证据与三项新增提案见[恢复笔记](../../09/_sources/daily-20260922/arxiv-recovery-20260927.md)，09/23待办见[日期恢复笔记](../../09/_sources/daily-20260923/date-recovery-review.md)。保留全部有效证据、四项实际Books及未写提案；未将本周或三份受影响Daily标完成。

## 6. 复核

复核者：日级 `weekly39_discovery`；源级及Books写后 `apr01`、`apr02` 与root交叉审阅；最终全周非作者待执行。
结论：未通过（全周尚有普通待办）。

09/26～27的独立日级验收通过，零候选/具体关闭及无必要Books修改成立。每周五项原始提议经实际原文与现有命题对照收窄为四项，root另核具名版本代码与日期/采用命题；FlashInfer Ch49、verl/NCCL Ch36、KServe Ch61的实际写后均分别由未参与Books写入的apr01/apr02验收通过，详见对应笔记§3/§5/§6。09/27又确认旧09/22的67个v1实际属09/21、旧09/23的38个身份实际属09/22，受影响两个旧Complete已定点重开，未删除有效机制或冒充全周验收。不据局部结果宣称全部Daily身份或全周已经完成。机器格式、链接和scoped diff检查不替代来源/准入/证据与真实写入的语义复核；未运行GPU、集群或作者实验。
