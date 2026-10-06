# Daily Research — 2026-02-05

**规范：** V3
**窗口：** 2026-02-04T09:00:00+08:00 ～ 2026-02-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T16:10:44+08:00

## 1. 结论

本日从原始来源独立重建。旧 README 原文仅备份于 [LEGACY_README](../_sources/daily-20260205/LEGACY_README.md)，未用于发现、准入、评分或 Books 判断；该目录原有其他非 feb05_ 前缀材料同属 legacy，不作为本轮证据。

App Server→Ch84、Anthropic zero-days→Ch72、DALI→Ch54、02987→Ch56、MatGPTQ→Ch49、TSS→Ch27、FaithRL/RCGRPO→Ch33、FASA→Ch45、ReMiT→Ch28、CSO→Ch34、TAME→Ch77、MASProVe→Ch82、Self-Verification→Ch80、ATA→Ch75、Semantic Routing→Ch23、World Model/POMDP与LIVE→Ch25十八项已实际整合并获root非作者写后复核通过。GPT-5.3-Codex、TokenSparse、POP、FailurePrediction、A-RAG、Risky、LPS-Bench、Memora、PnP、EB-JEPA、TRT及MAF十二项具体已有覆盖通过；POP只窄修last-input/first-new-token表述。False First一项标准完成、仅报告；ForesightKV与Distillation Resistance两项中心定义争议隔离，不授机制/性能通过。发现与贡献筛选冻结33个家族：3个机构、3个首批arXiv及30份新完整v1题摘中的27项，另外3项贡献前关闭，均已root准入校准。33项均已有安全处置，候选审阅与Books无普通待办；root已实际通读最终六部分并通过独立日级语义Gate，本日完成；机器校验不替代这一验收。四组来源限制及VTok日期未定保留精确终态，不授正面覆盖或无遗漏保证。无性能复现、stage、commit或push。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 原入口及官方 RSS 1243 条元数据；仅取 Feb3～6 边界定位。本窗 App Server Feb4 13:00 GMT、GPT-5.3-Codex release/card Feb5 00:00 GMT；Sora Feb3 00:00 GMT 窗前，Frontier Feb5 06:00 GMT 窗后。三个本窗原页必要核心已读，RSS 是发布方声明时刻，不证明初版逐句措辞。 | 已检查 | 当前网页可更新，不授 immutable 初版文本保证。 |
| SRC-ANTHROPIC | Research 首查 current10；原页面嵌入 publishedOn 的 Jan/Feb 记录定点恢复：zero-days Feb5 00:00Z，前邻 Jan29 AI assistance，后邻 Feb16 Country Briefs。zero-days L17–99 已读；Feb6 作者列表编辑单独保留。 | 已检查 | 当前目录不证明历史删改不存在；原页面 setup 不完整披露所有运行配置。 |
| SRC-GOOGLE-AI | Google pubs全年目录仅定位；Blog February2026相关标题，Feb4 Sequential Attention核心及两关联论文exact-v1题摘/历史已核，分别首次Sep2022/Feb2024，本窗是旧机制说明，LLM pruning为future路线，不准入。DeepMind真正/blog/page/3/与page/4/各24，前者May→Feb、后者Feb→Nov；定点官方NanoBanana2 Feb26、Gemini3.1Pro Feb19、Lyria3 Feb18、DeepThink Feb12均窗后。四主题有界官方域查询未扩年度队列。 | 已检查 | 当前有限历史切片不保证历史删改不存在；page=4未改变返回，使用实际路径分页。 |
| SRC-META-AI | 原 Research 动态0正文；官方域 Feb4 有界主题补检没有可采用原始正文；不将空响应当零发布。 | 受阻 | 可接受替代是本窗官方研究列表/带时间的原始发布；恢复只重开本窗，不全站考古。 |
| SRC-QWEN | GitHub Blog 原入口跳至旧 Qwen3Guard；当前 qwen.ai/blog 动态，从本日JS module44467实际恢复 /api/v2/article/retrieval，type=qwen_ai/language=en-US GET200。40项日期元数据已实际读完，边界前项CoderNext Feb3 04:00+08、后一项Image2 Feb10 13:08+08，没有本窗可见项。 | 已检查 | 当前40项有限停止，不证明历史删改不存在；未读取metadata中的私有git入口。 |
| SRC-DEEPSEEK | 官方 /news 原生 Research10实际日期：Jun24 V4、Feb25 DualPath、Jan28 OCR2、Jan12 Engram、Dec31 mHC；本窗无可见项。 | 已检查 | 当前原始有限列表，不宣称历史不存在其他发布或删改。 |
| SRC-MOONSHOT | Kimi Platform Blog 完整本页26条：Nov7/6 2025最新→May29 2024末；GitHub org updated10仅身份定位，created/updated不作论文公开时间。 | 受阻 | Platform旧列表缺2026覆盖；当前10仓库不证明全部历史发布，无可采用本窗材料。 |
| SRC-TENCENT-HUNYUAN | Research首查动态0正文，浏览器尝试因 subagent IAB visibility 不支持失败；原JS恢复正确 api.hunyuan.tencent.com/api/blog/publicList，page1/pageSize20/renderType0实际9/total9，publicAt最早CL-bench Feb3 18:02:07 BJT、后一项Feb13。 | 已检查 | 当前9项的有限停止，不证明历史删改不存在；wrong-origin404不是当前API不可用。 |
| SRC-ZAI | 官方 Research 当前175行按日期定位：Feb21 GLM5 report→Feb11 release→Feb2 GLM-OCR→Jan19/13；本窗没有可见项。 | 已检查 | 当前有限目录，不授全历史召回或版本不变保证。 |
| SRC-BYTEDANCE-SEED | Research/Blog curated Jan27→Apr11；papers动态分页原JS恢复 get_article_list_v2 article_type1/count20/publish_year2026/order_desc=false：20/total82、has_more、next20。日期由Jan20升序至Feb24，实际停在Feb5的BABE范围外标题，后段日期均窗后；本窗边界VTok单独核完整v1题摘与日期。 | 已检查 | VTok目录日期仅Feb4 date-level，不证明正文落窗；详见§5。不因total82扩大逐项队列。 |
| SRC-BAIDU-ERNIE | 官方中文Blog第一页：Feb6→Jan29→Jan15→Jan8→Nov21；本窗夹在Feb6/Jan29之间，分页2只较旧范围，不追旧内容。 | 已检查 | 当前列表的有限停止，历史删改未知。 |
| SRC-XIAOMI-MIMO | Paper8日期Jun29/March13→Feb3 HySparse→Jan8 Flash→2025；Blog15相关标题多无日期。实际JS index-c5195ace与4752.2908c99e恢复具名Flash发布wrapper/iframe Dec16,2025、关联Safety原页Dec22,2025，均窗前；不扩JS库存或安全case链接。 | 受阻 | 其余无日期Blog的历史公开切片无法确认；需要本窗带原始公开时间的官方Blog列表或具名正文，只重开相应项，不能用Paper零项冒充Blog零发布。 |
| SRC-MINIMAX | EN Blog Jan27→Feb12/14；CN原生目录6条Jan28→Feb12；Agent techblog.md当前May13新团队正文880字符。只定位本窗，不将三入口不一致视为三次发布。 | 已检查 | 当前有限列表及较晚文档不能证明历史缺失页无发布。 |
| SRC-ARXIV | 四主线主题的官方API各start0/max100/Submitted检索区间202602021900～202602031859均429，替代API仍失败。官方Feb月目录仅有界题名查漏：CL skip100/200、AI75/175、CV75/350各25；DC25，相关题名去重后仅具名题摘。30 exact-v1题摘实际读完，三首批system题摘另已读；逐ID DataCite恢复日期，不把宽分类库存作为候选。 | 受阻 | 来源入口的召回限制保留；具名贡献校准与候选必要core/owner处置已收束，Legal撤回负侧已root独立核。catchup失败不造日批次。 |

原始记录集中在 [daily-20260205 sources](../_sources/daily-20260205/)。本轮 fresh 仅 feb05_ 前缀；保留了真实失败返回和恢复路径，未扫 Weekly 来源。

## 3. 候选与判断

本表为发现与准入收束后的33个唯一候选家族，各项必要审阅及Books处置已落实到安全终态；两项争议隔离不算正面证据通过。arXiv范围为有说明的保守推定：分别核 exact-v1 Submitted、相容 February ID/Available、v1 Updated及 findable DataCite created/registered上界，结合官方 received/accepted announcement排程；不是精确发布日志，注册不等于发布。上界含精度端点以多一秒形成保守半开区间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Unlocking the Codex harness](https://openai.com/index/unlocking-the-codex-harness/) | 2026-02-04T21:00:00+08:00 | 短调用合理边界→typed Thread/Turn/Item与双向暂停/恢复接口→client presentation不能替代runtime/business effect authority；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md)两段 |
| [GPT-5.3-Codex release/card](https://openai.com/index/gpt-5-3-codex-system-card/) | 2026-02-05T08:00:00+08:00 | High预防性分类≠充分能力证据；topical→reasoner与message/actor enforcement不同边界、内部异步monitor不能预防副作用；2+2+2=6，必要安全约束深审 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)542–569；发布与局部评价留报告 |
| [Evaluating and mitigating growing risk of LLM-discovered 0-days](https://www.anthropic.com/research/zero-days) | 2026-02-05T08:00:00+08:00 | line/branch覆盖→LZW clear-token特定序列反证→覆盖率不代替状态序列正确性，crash与humanvalidatedseverity/patch分账；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)735一段 |
| [MatGPTQ exact-v1](https://arxiv.org/abs/2602.03537v1) | 2026-02-04T09:00:00+08:00 ～ 2026-02-04T11:26:35+08:00 | 多checkpoint/QAT成本→单parent多precision PTQ、cross-bit补偿与预算感知perlayer search→bit-slice质量需联合校准；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)987一段 |
| [Large-Scale LLM Inference with Heterogeneous Workloads v1](https://arxiv.org/html/2602.02987v1) | 2026-02-04T09:00:00+08:00 ～ 2026-02-04T11:13:46+08:00 | prefill影响decode服务率→phase收入与完成收入诱导不同拥塞→fluid均值最优不授tail SLO保证；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)189一段 |
| [DALI v1](https://arxiv.org/html/2602.03495v1) | 2026-02-04T09:00:00+08:00 ～ 2026-02-04T11:25:37+08:00 | 静态CPU/GPU expert放置→运行时minmax负载分配、只预取GPU highworkload与workload cache→规划/预测开销需端到端计价；2+2+2=6 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)364一段 |
| [ReMiT v1](https://arxiv.org/html/2602.03075v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:15:50.000+00:00 | RL reference与当前learner的token logprob差→有界软重加权mid-training→阶段反馈不等于全分布模仿；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)167一段 |
| [TRT v1](https://arxiv.org/html/2602.03094v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:16:17.000+00:00 | 失败rollout对照自选成功trace→contrast reflection memory→选择失效与测试/搜索预算需分账；2+1+2=5 | 深入完成 | 已有覆盖：AGENT-REFLECTION [具体正文](../../../../books/part-07-agent/80-reflection.md) |
| [TSS v1](https://arxiv.org/html/2602.03103v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:16:29.000+00:00 | likelihood质量proxy→可混淆替代instruction的contrast specificity+质量项→筛选效用不能由容易负例冒充；2+2+2=6 | 深入完成 | 整合：TRAIN-DATA [具体正文](../../../../books/part-04-training-system/27-data.md) |
| [FASA v1](https://arxiv.org/html/2602.03152v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:17:38.000+00:00 | full-head scan成本→CA校准RoPE frequency子空间先选再全维读取→selector近似与KV residency分账；2+1+2=5 | 深入完成 | 整合：INFER-KV-CACHE [具体正文](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ForesightKV v1](https://arxiv.org/html/2602.03203v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:18:50.000+00:00 | 经验淘汰→future attention监督+post-eviction reward→未来依赖估计与在线状态漂移分账；2+2+2=6 | 争议 | 暂缓：中心 ordering/reward 定义冲突，见§4/5 |
| [Token Sparse Attention v1](https://arxiv.org/html/2602.03216v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:19:08.000+00:00 | 早层永久token淘汰→per-head QKV gather/输出scatter+residual保留→本层跳算不等于删除未来候选；2+2+2=6 | 标准完成 | 已有覆盖：INFER-PREFILL，[Ch43](../../../../books/part-05-inference-system/43-prefill.md)108–132 |
| [ATACompressor v1](https://arxiv.org/html/2602.03226v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:19:22.000+00:00 | 固定压缩预算→query-aware encoder+相关跨度监督AAC→压缩token数与任务证据耦合；2+2+2=6 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md)257一段 |
| [POP v1](https://arxiv.org/html/2602.03295v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:20:59.000+00:00 | 所有层prefill full attention→deep prefill省算而保KV projection/full decode→first-token计算与后续读取分账；2+2+2=6 | 深入完成 | 已有覆盖：INFER-PREFILL，[Ch43](../../../../books/part-05-inference-system/43-prefill.md)65–77；69行窄事实修正 |
| [Failure Prediction v1](https://arxiv.org/html/2602.03338v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:21:59.000+00:00 | 高AUROC→failure critic引导策略仍可能变差→预测质量不证明行动干预收益；2+2+2=6 | 深入完成 | 已有覆盖：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)333–343 |
| [Distillation Resistance v1](https://arxiv.org/html/2602.03396v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:23:19.000+00:00 | 公开teacher输出→conditional-MI约束logit变换→任务效用与防蒸馏保证的条件分离；2+2+2=6 | 争议 | 暂缓：CE 对变换 M 的依赖未明确，见§4/5 |
| [CSO v1](https://arxiv.org/html/2602.03412v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:23:41.000+00:00 | 只奖励最终正确→expert step替换后续outcome flip识别关键step→反事实偏好与终局收益分工；2+2+2=6 | 深入完成 | 整合：TRAIN-DPO [具体正文](../../../../books/part-04-training-system/34-dpo.md) |
| [A-RAG v1](https://arxiv.org/html/2602.03442v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:24:22.000+00:00 | 固定retrieve→keyword/sentence/full-chunk三级工具→搜索分辨率与完整上下文读取成本分工；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-RAG [具体正文](../../../../books/part-07-agent/76-rag.md) |
| [Self-Verification v1](https://arxiv.org/html/2602.03485v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:25:24.000+00:00 | 验证确认多于纠错→历史no-change classifier抑制部分test-time verification→少确认不保证更正确或总成本更低；2+2+2=6 | 深入完成 | 整合：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)201一段 |
| [FaithRL v1](https://arxiv.org/html/2602.03507v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:25:54.000+00:00 | outcome advantage广播→依据正负方向调制step evidence-support权重→外部证据归属不等于内部faithfulness；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [False First v1](https://arxiv.org/html/2602.02991v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:13:52.000+00:00 | 首位数字偏离指令→后续序列/第二轮均值局部修正→可读hidden signal不证明预先规划或Bayesian因果机制；2+1+2=5 | 标准完成 | 仅报告：受限数字任务/in-sample读出，不采用一般planning或Bayesian因果机制 |
| [RCGRPO v1](https://arxiv.org/html/2602.03025v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:14:40.000+00:00 | 全同reward组无relative advantage→quality-token conditioned policy与混合rollout→探索条件不等于任务成功或逐组非零保证；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [MASProVe v1](https://arxiv.org/html/2602.03053v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:15:19.000+00:00 | 多agent多轮推理→agent/iteration verifier配置交叉→judge/RM/PRM噪声与策略收益须隔离；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [具体正文](../../../../books/part-07-agent/82-multi-agent.md) |
| [Risky v1](https://arxiv.org/html/2602.03100v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:16:25.000+00:00 | 仅user prompt防护→多环境surface注入下reasoning局部反转→thinking不普遍降低攻击成功；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [具体正文](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MAF v1](https://arxiv.org/html/2602.03128v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:17:05.000+00:00 | 把流程框架当推理增益→schema/planning反侧→格式失败与任务reasoning失败分离；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [World Model/POMDP v1](https://arxiv.org/html/2602.03146v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:17:30.000+00:00 | 有限goal-conditioned policy query→在communicating CMDP/POMDP条件恢复transition→query可识别不证明现实policy已内部建模；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)68一段 |
| [TAME v1](https://arxiv.org/html/2602.03224v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:19:19.000+00:00 | 只按task utility演化memory→executor/evaluator双bank分别约束任务与trust→效用增益不能认证可信性；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [具体正文](../../../../books/part-07-agent/77-memory.md) |
| [LPS-Bench v1](https://arxiv.org/html/2602.03255v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:20:03.000+00:00 | 显式安全拒绝→benign ambiguity需clarify而非guess→执行边界与拒绝指标分离；2+1+2=5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING [具体正文](../../../../books/part-07-agent/78-tool-calling.md) |
| [Memora v1](https://arxiv.org/html/2602.03315v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:21:27.000+00:00 | 平面retrieval→abstract index/concrete cue/cross-aspect linking→压缩线索与证据回读分工；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MEMORY [具体正文](../../../../books/part-07-agent/77-memory.md) |
| [Semantic Routing v1](https://arxiv.org/html/2602.03510v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:25:58.000+00:00 | 固定text feature→多LLM层按DiT depth/time融合→time-dependent gate不普遍更优且trajectory可能失配；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)282一段 |
| [PnP v1](https://arxiv.org/html/2602.03533v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:26:29.000+00:00 | AR理解与diffusion生成→pretrained prior bridge→目标/表示兼容不由模型组合保证；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [EB-JEPA v1](https://arxiv.org/html/2602.03604v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:28:09.000+00:00 | 双encoder目标→有限计算下ablation/collapse反侧→表示学习条件不等于通用能力；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [具体正文](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [LIVE v1](https://arxiv.org/html/2602.03747v1) | 2026-02-04T01:00:00+00:00 ～ 2026-02-04T03:31:29.000+00:00 | 末端视频误差→forward rollout/reverse initial-cycle+curriculum→cycle一致不证明真实动力学；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)967一段 |

以上27项是逐ID核题摘与日期后的家族，不是月目录库存；每项区间由自身metadata推定，原Submitted/Updated/Available/created/registered在[feb05_dates_native.json](../_sources/daily-20260205/feb05_dates_native.json)。Privasis03183、KTV03615、UnifiedEval03238完整题摘由root实际读后校准贡献前关闭：分别只是synthetic私有属性规模/sanitize组合、聚类importance局部组合无新设计条件、position框架无新控制或反证；不以无benchmark或模型小一律排除。

## 4. 证据与知识整合

### [Unlocking the Codex harness](https://openai.com/index/unlocking-the-codex-harness/)

采用当前官方 §Origin / Inside harness / Conversation primitives / Integrating clients / Choosing protocol 及 footnotes。MCP callable/one-off接口在短任务仍合理；复杂客户端需要typed事件及stable lifecycle，server request可暂停Turn等approval。Thread持久化回读与client断线状态投影并不授权重提原任务，也不保证外部exactly-once。JSON-RPC lite省略2.0 header、hosted stdio可网络tunnel；TUI refactor原文是计划。没有核代码或复现实验，backward-compatible目标也不证明任意版本配对无故障。

[Ch84](../../../../books/part-07-agent/84-agent-platform.md) runtime四类authority后、tracker前新增两段（目前90/92行），末尾source注同步root实际写后通过；root顺读74–107与末注确认presentation、runtime和business-effect边界及Ch83交接。

### [Evaluating and mitigating growing risk of LLM-discovered 0-days](https://www.anthropic.com/research/zero-days)

当前原页L17–99已实际读。VM+standard tools是作者披露setup，不等于所有模型/运行参数均公开。GhostScript同类调用漏检查、OpenSC多前置条件、CGIF按uncompressed输入大小预留compressed编码缓冲的假设遭LZW clear-token序列打破，分别是三例；CGIF L57–87支持line/branch coverage不能穷尽sequence，不能升级为Agent普遍优于fuzzer。L29–31明确crash经critique/de-dup/prioritize后仍由人类安全研究者验证与手写patch；500是作者累计声明而不是对照benchmark。L89–91 activation probes与实时enforcement/合法误拦分责。Feb6编辑注明作者列表，不将之后版本措辞当初版逐句证明。

root已实际核L17–99并通过受限反证准入。[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)现735新增sequence coverage反证一段、末注3998，前后733–739与源注已root实际POST通过；原trace/predicate、跨输入变换invariant及静态tool边界保留，sensor/enforcement已有具体覆盖，不重复写。

### [GPT-5.3-Codex release/card](https://openai.com/index/gpt-5-3-codex-system-card/)

Release/Card为一个家族内两个事件。当前card必要§5.1/5.2.1已读：三canary任务不足以决定High；Range、CVE与harness secret/log leak路径不能拼作典型生产能力。1000turn/100K compaction和abort/resume是受测harness预算，非自主性保证。Topical classifier operatingpoint→SafetyReasoner→routing/actor累计处置要分别保存；专家标签集recall不能证明未知攻击阻断。Redteam较早checkpoint与policy变更不支持简单因果比较。内部longrange异步monitor原文明确不能预防harm；high-cyber与longrange条件不合并为任意High标签。Release研究团队用early模型debug/train/deploy不证明模型闭环自行训练；25%快无完整条件不作系统机制采用。最低0.90是synthetic cyber topical labels的召回，非unsafe召回或防攻击率。root实际核原L335–376/365–423/425–446/456–463/467–478与Ch72 542–569，具体已有sensor→reasoner、message/account、trust非豁免及false-positive/online迁移验收覆盖；不借5.4案例反推5.3初版精确措辞。

### [DALI v1](https://arxiv.org/html/2602.03495v1)

§3–6/A1–3实际必要审阅：目标minmax(CPU,GPU)，calibrated residual vector预测下层highworkload专家，workload sliding-window更新cache。作者16CPUcores/32threads、EPYC7532、RTX3090 24GB/PCIe4x16、三MoE模型，C4速度/Wiki1K校准；prefill64与decode64+64、不同baseline以comparable而非完全相同GPU存储路径约束。随机预取反降速、prefetch gate/stream成本与greedy/Opt求解成本必须计端到端；高hit rate不等于高throughput。Precision/部署SLO完整条件未披露，不采用普遍speedup。

Eq9 GPU memory约束未显式出现在Alg1，Alg2 GPU evict TopK与正文低score叙述冲突；只保留可支持的机制/评价边界，不宣称伪码正确性、近最优保证或跨GH200/server适用性。root必要原源/差异和Ch54实际357–372写后复核通过；新增364一段+905注，保CPU直接执行替代GPU补给及真实overlap条件。

### [Large-Scale LLM Inference with Heterogeneous Workloads v1](https://arxiv.org/html/2602.02987v1)

§2.2–7实际必要审阅：one-prefill/fixed chunk、homogeneous GPUs、class representative P/D、Poisson arrivals、独立exponential service/patience、nonpreemptive FIFO是模型假设，不是任意实际serving。混合与solo iteration-rate不同；bundled收入只算decode完成，separate阶段收入可能鼓励上游拥塞。稳态LP目标与gate policy的渐近结论不提供tail SLO保证。作者四A100校准后事件驱动simulation n5–500、两个类、B16/C256及有限seed支持机制说明，不是production benchmark，消融同时改变多个耦合设计不能授单项因果。Ch56现189一段+1885注已按root授权实写，root实际182–198写后复核通过；不以摘要asymptotic optimal授生产最优。

### [MatGPTQ exact-v1](https://arxiv.org/abs/2602.03537v1)

exact-v1 §3–6/C已实际审阅。单整数parent/scale/zero-point同时优化目标位宽投影；λ参与候选projection objective，而跨bit残差传播取均值，两者不混同。round/clamp整数规则不适用于任意float slice；预算搜索是静态per-layer选择，不授权per-token路由。未优化位宽、Qwen/Phi反侧和较大batch的kernel退步均需单独验收。RTX A6000/单token warmup与median测量不支持production吞吐；§5.7已integration与§6未来integration措辞并存，不授部署完成。Ch49 anchor节987一段及2599末注已root实际974–995写后通过，前后QAT/PTQ/ELMoE交接保留，未核实现或复現。

### [ForesightKV v1](https://arxiv.org/html/2602.03203v1)

§3–5及B.2必要反侧已读，原证据见[feb05_attention_core](../_sources/daily-20260205/feb05_attention_core.json)和[公式/文字冲突](../_sources/daily-20260205/feb05_foresight_conflict.txt)。Eq6 ordering、原cache与eviction后likelihood差的正阈值、B.2最高score淘汰给出不相容的方向定义。root已实际核核心冲突；这阻止采用learned ranking/reward算法与机制归因，不证明所有作者实验无效。6分不降分，中心争议终态隔离，不进入Books；重开条件是勘误或与实测绑定的明确ordering/reward实现与配置。

### [Token Sparse Attention v1](https://arxiv.org/html/2602.03216v1)

§2方法与§3–5对照/限制实际读：per-layer/head QKV gather、zero scatter与residual保留未选hidden，未选token以后可重新参与；不是永久token/KV eviction，也不是dense数值等价。selection/gather/scatter成本与短序列fallback不能从矩阵规模省略。root实际核必要core，并对读Ch43 108–132的active mask、旁路保hidden、reconstruction与selectioncost，具体已有覆盖；曾拟新增两段因新owner证据撤销，无本项净新增，不抄TTFT/速度数字或生产收益。

### [POP v1](https://arxiv.org/html/2602.03295v1)

§3–5的deep-prefill attention省算与完整KV projection/decode分工已读，root实际核§3.3及Ch43 65–77。这里x[N]是最后一个INPUT token作为首个DECODE step处理，预测首个新token x[N+1]，不是把x[N]叫生成token。已有正文69行仅修正这一短语，root写后已核；其余prefill省算与后续读取机制具体已有覆盖。不授权把首次完整图处理省掉、虚构KV删除，或由受限作者速度授生产SLO。

### [Failure Prediction v1](https://arxiv.org/html/2602.03338v1)

必要§3critic/calibration/intervention、§4负侧、§5threshold/feedback/oracle与§6early-step已读，见[feb05_core_stage18_2](../_sources/daily-20260205/feb05_core_stage18_2.json)。预测AUROC高不证明critic引导policy更好：阈值改变被干预群体，feedback/oracle信息改变可恢复性，earlystep覆盖也须与实际行动分开。root必要反证和Ch80 333–343已实际核，现有净干预收益、paired pilot与不确定时关闭已承载采用命题，具体已有覆盖。未独立读取全部中间结果表，不采用数字或所有任务因果保证。

### [Distillation Resistance v1](https://arxiv.org/html/2602.03396v1)

exact-v1 §3–5、Eq9及AppC Alg1必要内容已读；原M变换生成zT′，但CE字面仍按原公式引用，未明确依赖M；CE-only warmup与ablation解释又要求任务项确实优化M。root实际核Alg1 6–9后确认中心定义未决。不能凭联合MI/utility叙述授防蒸馏与任务保持保证，也不宣称全部作者实测无效。6分中心争议安全隔离、不进入Books；只有精确变换CE实现/澄清及对应配置可定点重开。

### [ReMiT v1](https://arxiv.org/html/2602.03075v1)

exact-v1 §3–5已读，原核心在[feb05_core_stage18_1](../_sources/daily-20260205/feb05_core_stage18_1.json)。RL reference与CURRENT learner pθ的observed-token logprob差经sequence centering/sigmoid/clipping变软权重，learner仍优化weighted NTP；不是对冻结base算静态权重、全词表KD或重新执行RL。必要[B.1/F.2原段](../_sources/daily-20260205/feb05_remit_weight_boundary.json)补读：B.1 Eq15–20把Zw/H(qw)视θ独立，与主文wθ含current pθ存在梯度条件未决；未披露detach，不授wt-onlygradient或KL方向保证。F.2是一个frozen RL reference额外forward而不是双teacher；confidence proxy不保证长期最优，两个同OLMo迭代不证明无限self-improvement。三backbone等50B midtrain只作受限对照。唯一owner TRAIN-PRETRAINING：Ch28现feedback target-selection后167行新增一段+末注1682。root实际核B.1/F.2与具体owner、150–174正文顺读/末注，POST通过；θ依赖理论边界局部隔离，不采用KL梯度等价。

### [TSS v1](https://arxiv.org/html/2602.03103v1)

exact-v1 §3–5已读，同一缓存obj2。保持input X和target Y固定，比较p(Y|I,X)与多个alternative instructions Ik下的概率；Ik最初只从X生成，TSS++按固定Y likelihood选hard alternatives再加quality项。不是生成错误answers，恢复提案中这一错误已经撤回。Alternative分布不是精确p(I|X)，CMI解释保近似性质；top比例按examples不自动匹配token/compute，Random/PPL在部分受测数据占优，不能授通用最佳selector。唯一owner TRAIN-DATA：Ch27 Quality filtering原quality/retention段后246行新增一段；末注1433行。root已实际核§3/§5及具体gap、238–258写后正文与衔接，POST通过；不采用counter-answer说法。

### [FASA v1](https://arxiv.org/html/2602.03152v1)

exact-v1 §4.1–4.2、B.4与D.1必要原文已读，见[频率selector原core](../_sources/daily-20260205/feb05_fasa_core_locator.txt)及[变换/边界](../_sources/daily-20260205/feb05_fasa_equivalence.txt)。CA校准RoPE frequency子空间先做近似选择，选中项仍以full-dimensional表示读取；这节省selection work，不把未读KV自动从residency删除。位置变换的代数关系不认证selector recall或任意位置精度。受测decode/kernel、额外校准、短序列/分布漂移回退分别计价，不外推所有KV预算/生产tail SLO。唯一owner INFER-KV-CACHE：Ch45 access-plan段后188行新增一段，末注2050；root已实际核D.1/D.2及owner具体差额、183–195写后与末注，POST通过。

### [ATACompressor v1](https://arxiv.org/html/2602.03226v1)

exact-v1 §3–5已读，见[feb05_six_a](../_sources/daily-20260205/feb05_six_a.json)obj1。query-aware encoder从有gold relevance标签的chunks学选择重建，再QA finetune；probe由末input hidden估相关长度，ratio/max约束soft-slot数量，部署冻结encoder/reader并传KV。不能称无监督codec或任意reader兼容。两7B backbone、两A10040G，主评input<600、LongBench两任务<2048；shortinput过压反例及部分baseline更低memory/更高TP保留，不采用全文‘always better’。root已实际核AAC Eq4–5、§5.2短输入反侧与现Ch75具体gap；唯一AGENT-CONTEXT在break-even后257行一段+727末注已实写，root已实际对读方法/短输入反侧、257行正文与compression/break-even邻接及末注，POST通过。

### [TRT v1](https://arxiv.org/html/2602.03094v1)

exact-v1 §3–5及A.6已读，见[feb05_six_b](../_sources/daily-20260205/feb05_six_b.json)obj2与[必要附录](../_sources/daily-20260205/feb05_necessary_appendices.json)obj3。失败与自选较好trace萃取task-scoped knowledge再rollout，生成tests并执行提供反馈，不能称完全无验证环境。相同trace/rollout数量不匹配额外反思calls、tokens或test execution；selected accuracy、cumulative oracle与pass@k不合并。正确→错误和history dilution保留，不授100%或单调改进。现Ch80 stop/no-change、ECR−EIR与critic allocation及Ch77经验派生/验证关系可承载受限反证，root已实际核§3选择/knowledge、§4.1预算/累计oracle、§5.2/§6损害及reflection成本与Ch80 185–228，具体已有覆盖通过，不新增Books。

### [CSO v1](https://arxiv.org/html/2602.03412v1)

exact-v1 §3–5实际读，见[feb05_core_stage19](../_sources/daily-20260205/feb05_core_stage19.json)obj2。PRM提候选failure state，替换一个expert action，恢复current policy后续执行，经outcome evaluator筛选再冻结step-DPO pair；不是终局成功自动证明某动作在全部状态普遍因果必要。no-PRM/verification反侧和不同pairs数量不提供等总预算归因；gold-based LLM judge、web/network及expert分支成本限制外部效度。唯一TRAIN-DPO：Ch34 sameprefix logprob后148行新增一段+末注471。root已实际核§3.2.2–4/§3.3、§5.1反侧与owner具体gap、143–153写后及末注，POST通过。

### [A-RAG v1](https://arxiv.org/html/2602.03442v1)

exact-v1 §3–5.3已读，同six_b缓存obj3。runtime keyword与sentence embedding先返回snippets/parentchunk IDs，再按需完整chunk及adjacent read；readset仅防重复正文返回，通知/call/model仍付费，原‘zero tokens’不等总零费用。NoChunkRead把完整正文直接送入Context，不是纯工具开关隔离；有限backbone/embedding例外及首300 scaling不授匹配总预算。现Ch76 67–77明确document/query/answer分工、navigation→预算展开/去重、完整上下文成本与chunk fallback，root已实际核必要原文与Ch76 65–80，受限已有覆盖通过，不新增Books。

### [Self-Verification v1](https://arxiv.org/html/2602.03485v1)

exact-v1 §3–5已读，见stage18_2 obj2。这是test-time控制，不是训练confirmation/repair两个policy。历史标签经classifier/BM25 vote预测no-change verification，再closureprompt+cooldown抑制部分确认；确认比例高不证明这些步骤都无用，历史分类准确不认证答案正确。统一屏蔽verification有质量反退，部分model/task平均也混合；主轨迹tokens减少不等端到端latency/calls更低。Ch80 stop/nochange/ECR−EIR和critique allocation已有明确论点，原existing提案经root Ch80 183–230实际比较纠正为具体gap：Runtime持久化后/ECR前201行一段已实写+末注414，historical non-change sensor与correctness分账；root已实际补核§5.1–5.4直接反侧、Ch80 183–220写后及末注，POST通过。

### [FaithRL v1](https://arxiv.org/html/2602.03507v1)

exact-v1 §3–5、A.6/G.1/G.3/K必要内容已读，stage19 obj3及necessary_appendices obj4。Eq10在正advantage偏重supported steps，在负advantage偏重unsupported steps，α给其余项floor；外部70B句级evidence attribution不认证hidden faithfulness或全部logical validity。gold decomposition构造E，Bo32全失败不是不可答证明；数学OOD用GT解题steps仅offline核验，不作为部署oracle。THS面积增加不保证每轴Pareto，y0=0需另处理；A.6 trajectory-level mask推导不直接认证Eq10 tokenwise GRPO一致性。唯一owner TRAIN-GRPO：Ch33 process/credit段后195行新增一段，末注2591。root已实际核§3、Eq10、结果反侧/cost及187–202写后与末注，POST通过；理论保证/通用安全及全面Pareto不采用。

### [False First v1](https://arxiv.org/html/2602.02991v1)

exact-v1 Sx2–5完整必要核心已读，见[feb05_false_first_core](../_sources/daily-20260205/feb05_false_first_core.json)。受测首位数字偏离指令、后续序列和第二轮均值部分修正；LASSO隐藏态读出在全部69轨迹拟合，未披露heldout或因果干预，R²不证明原模型预先计划了未来。Gaussian均值修正非每项均优，未认证完整分布，Bayesian prior只是解释假设；greedy数字任务不能推广自由文本。5分标准完成→仅报告局部观测，不以可读signal补造内部规划/因果机制；root已实际核Experiment1/DataAnalysis全69序列LASSO、GeneralDiscussion与限制，处置通过，不新增Books。

### [RCGRPO v1](https://arxiv.org/html/2602.03025v1)

exact-v1 §3–4实际读，stage18_2 obj3。expert successes/policy failures的逐turn quality token用于SFT conditioning；混合condition改变rollout探索，actual outcome/tool-action reward仍独立决定组advantage。质量token不是成功真值，所有同reward group仍可发生；方差结论只在0<p<1、条件均值不同、G>1等假设下，不保证逐组非零。有限BFCLv4/两模型与conditioning+mixed sampling消融不授所有tool任务最优，Eq7 trajectory ratio也不默认tokenwise vanilla GRPO。唯一TRAIN-GRPO：Ch33 prompt replay后394行新增一段+末注2595。root已实际核§3.1–3.3、§4.3/Q4反侧与具体owner、387–401实际写后及末注，POST通过。

### [MASProVe v1](https://arxiv.org/html/2602.03053v1)

exact-v1 §2–4实际读，见[feb05_core_stage20](../_sources/daily-20260205/feb05_core_stage20.json)obj1。六MAS/固定GPT5mini、三branch候选中，agentcall或iteration判分及judge看step/rawhistory/summary会改变控制机会、信息与成本，未有统一最佳粒度或更多context普胜。N=3搜索与baseline成本不等；posthoc BestConfiguration、CoT0/30或MAS0/3不证明部署默认或问题无解，RM/PRM目标域失配保留。现Ch82 verifier independence尚未明确粒度/view交叉责任，唯一AGENT-MULTI-AGENT：Ch82 verifier条件后118行一段+末注1241。root已实际核§4.2–4.4/具体owner、111–123正文与末注，POST通过；原6分保持。

### [Risky v1](https://arxiv.org/html/2602.03100v1)

exact-v1 §2–3及D.1实际读，six_b obj1与necessary_appendices obj2。三access层、五surface中agentinstruction允许改system/governing prompt，不能与不可信toolfeedback相同威胁模型比较；750三域/七agent、人工校正judge是受测条件。thinking两family方向不统一且未隔离全部模型/配置因果，不授‘推理更不安全’定律。现Ch72 580–601分开retrieval/tool/memory影响、authority registry、step guard和executor实际effect，拟已有覆盖仅采用这份受限分层反证，root已实际核五surface/三access、750/sevenagent配置与Ch72 580–603，具体已有覆盖通过。

### [MAF v1](https://arxiv.org/html/2602.03128v1)

exact-v1 §3、§4.1.1/4.1.3、必要表9–11及memory configuration实际读，six_a obj3。NoPlan/schema-plan/freeform改变接口，formatfailure与reasoning错误应分开；Table10 gptoss20B freeform MATH13%与正文‘all0’冲突不合并。memory provider routing、framework语义、calls/output预算不同，100xheadline不采用。现Ch66 51–58 contract≠quality及187–201 adapter会改变schema/serialization/retry/stop、须验semantic equivalence已具体承载这份设计反证，root已实际核§3.2三planning接口/格式错误、§4.1与Ch66 51–59/187–201，具体已有覆盖通过；headline all0与Table10 13%冲突局部隔离，不授全部topology rewrite等价。

### [World Model/POMDP v1](https://arxiv.org/html/2602.03146v1)

exact-v1 §2定义/§3/§4.1–4.3必要证明已读，见[feb05_core_stage22](../_sources/daily-20260205/feb05_core_stage22.json)obj1。有限stationary communicating CMDP、足够全的构造goal及initial-state policy query、无timepenalty允许无限等待是recover transition结论前提；POMDP需goal能指向hidden state，obs-only goal不据此识别隐藏世界。δ范围、query oracle和统计误差不说明现实单任务policy已内部学得可校准worldmodel。root已实际核§2/§4 stochastic/POMDP/width-two必要命题与channel/support现正文具体gap；唯一MULTIMODAL-WORLD-MODELS在68行一段+1513注已实写。Width-two仅deterministic，不合并stochastic/partial；正文进一步准确限定：只有observation、缺少真实状态表达与该goal-query接口的情形不继承结论，不能排除原POMDP hidden-state theorem。root已实际核68行正文/邻接及末注、该排除边界改后POST通过；不采用开放智能必要性宣传。

### [TAME v1](https://arxiv.org/html/2602.03224v1)

exact-v1 §3–5/A.2必要机制/反侧已读，stage20 obj2与[tame限制](../_sources/daily-20260205/feb05_tame_necessary_prompts.json)。只按任务效用演化memory可能固化坏策略；executor/evaluator两个bank按task与规范分工，但不把另bank或model judge变成authority。没有原方法的‘时衰trust’步骤，该旧提案表述已纠正；Eq3毒性趋1不是通用证明，task/trust各有退步，role/复杂度与judge共同偏差未消除。A.4 HTML仅prompt图标题，未声称已核图中文字/实现；不采规范保证。Ch77 taskutilityproxy≠truth、write gate已有，唯一AGENT-MEMORY：Ch77效用proxy→MemoryRead前164行一段+末注2018，明确evaluator两类bank→utilitydraft→normrefine→executor及双方更新。root已实际核§4.3–4.5/Eqs9–13、§5.3/5.5与160–169实际写后/末注，POST通过。

### [LPS-Bench v1](https://arxiv.org/html/2602.03255v1)

exact-v1 §3–4/A.3–4/C必要内容实际读，six_a obj2及necessary_appendices obj1。mocktoolkit、case-specific criterion与HITL只验证该instrument；wholetrace判safe/unsafe/execution_failed分开，没到风险状态不证明安全。benign ambiguity需pre-effect澄清而不是猜，malicious目标另行拒绝；τ1/p.9/k50/100step使探索路径不同，不授防护有效性因果。现Ch78 proposal→executor与高风险字段typeddefault/clarify已承载采用命题，Ch66未发生effect不记完成保评价限制，root已实际核mocktoolkit/wholetrace/benignclarify-vsrefusal及Ch78 24–65，唯一AGENT-TOOL-CALLING具体已有覆盖通过。

### [Memora v1](https://arxiv.org/html/2602.03315v1)

exact-v1 §3–6实际读，stage20 obj3。canonical abstraction与非独占cue links组织episodes，LLM match/merge/delete不是事实identity证明；bounded refine/expand/stop仍受source provenance与working budget。group reward仅mean-centering，不是scale-invariance；cue ablation的F1/BLEU不全胜，learned controller增加calls/检索成本，有限seed/单reader不授通用迁移。现Ch77 229–248 anchor→bounded expansion→evidence assembly与362–368 raw/fact/profile、可回指projection已承载具体命题，root已实际核§3.4–3.6/§4.1–4.2及现Ch77上述正文，具体已有覆盖通过，不新增Books。

### [Semantic Routing v1](https://arxiv.org/html/2602.03510v1)

exact-v1 §3–5实际读，见[feb05_core_stage21](../_sources/daily-20260205/feb05_core_stage21.json)obj1。多LLM层先normalization再convex fusion，gate可依DiTdepth/time或二者；同prompt的条件信息不是每block/时刻必相同。time-only受测退步、depth-only更稳，layerweight可读不证明因果语义分工。SNR诊断用最终generated latent自参考，heuristic t-shift不识别唯一失配原因；singlebackbone、固定solver、judge/caption及cost条件保留。root已实际核§3.3–3.4/Eq2–10、Table1与§5.2/5.3；具体owner校准为MULTIMODAL-REPRESENTATION，现Ch23 Cross-attention fusion后282行一段+1040末注已实写，layer-LN/convex与DiTdepth-condition身份是该接口增量，不写Ch24生成objective。root已实际对读必要方法/反证与282行正文、fusion邻接及末注，POST通过；表中误把CFG跨参数化作为主增量已纠正。

### [PnP v1](https://arxiv.org/html/2602.03533v1)

exact-v1 §3–4实际读，stage21 obj2。冻结VLM/VAE但DiT仍训练；理解/generation query connectors桥接3Dprior，latent缺color/texture需2Dviews补充，不是任意预训练组件即插即用。64/1024query是局部recipe，CLIP/Qalign/GPTcaption不认证3D拓扑真值；1024→4096 qualitative不证明任意resolution。现Ch23 53–66 encoder/projector瓶颈、可读/可访问/可表达分账及280querycapacity承载有限兼容边界，root已实际核§3.1–3.4及Ch23 53–67/280接口瓶颈，具体已有覆盖通过，不为demo组合强改。

### [EB-JEPA v1](https://arxiv.org/html/2602.03604v1)

exact-v1 §3–6实际读，stage21 obj3。latent energy为prediction error，SIGReg/VICReg等防collapse；action-IDM约束只在动作可恢复/数据支持内成立。TwoRoom/MovingMNIST/CIFAR局部MPPI累计cost与terminal cost反侧、强regularization导致collapse不授真实world识别或普遍单调cost。root已实际核§3/Eq1–8、§4IDM/§5collapse反侧与Ch25 251–255 inverse-action anti-collapse具体条件，已有覆盖通过；不声称全部planner参数已核，也不将随编辑变化的旧307–315称作当前horizon段。不因小模型/库名而排除。

### [LIVE v1](https://arxiv.org/html/2602.03747v1)

exact-v1 §3–5/7.1实际读，stage22 obj2。stop-gradient自产生forward rollout，再以逆序conditions/re-noise监督原prompt重建，渐进horizon；parallel forward可见knownfuture条件是离线训练接口，不冒充online完全等价。re-noise防近邻清帧捷径不认证物理inverse或有界真实误差；不同额外训练预算、realestate/Minecraft反侧与随length退化保留，不授无限时长/实时SLO。原已有覆盖提案经root必要Eq9–14与现owner比较纠正：该机制是GTprompt→stopgrad rollout→reverse/noise→recover GT训练监督，不能由真实action-inverse invariant认证。唯一MULTIMODAL-WORLD-MODELS在inverse verifier前967行一段+1515末注已实写；作者再actual核Table1/2长horizon仍退化及§7.1 extra posttrain预算不等。root已实际对读必要方法/长horizon及预算反侧、967行正文与inverse verifier邻接及末注，POST通过；不授formal误差界或live未来信息。

## 5. 缺口与下一步

本窗普通可执行待办：0。候选审阅、Books处置、必要实际写后及最终独立日级复核均已完成；root已实际核最终六部分一致性、14来源范围/有限停止、日期与具名负侧。以下外部限制与中心争议作为本窗终态保留，不授正面证据或无遗漏保证。

本窗中心争议终态保留：ForesightKV03203与Distillation Resistance03396不采用中心机制/性能，不进入Books；具体冲突与各自唯一精确重开条件见§4对应条目，已获root必要原文校准，不把争议隔离记为正面Evidence通过。

本窗来源外部终态保留：SRC-META-AI缺可恢复的本窗官方正文/日期，SRC-MOONSHOT的Platform本页仅2025/2024且org更新不代表2026研究发布，SRC-XIAOMI-MIMO其余具名无日期Blog缺历史公开切片，SRC-ARXIV四主题API与catchup失败限制召回；各自实际入口/停止及替代请求已在§2逐源记明。需要本窗官方列表或对应具名带时间正文（arXiv可接受官方实际公开主题批次/API恢复）；仅定点重开受影响源/时段，不扩仓库/全年目录。这些项不用于正面Evidence、Books或无遗漏保证。

本窗日期保留：Seed [VTok2602.04202v1](https://arxiv.org/abs/2602.04202v1)目录PublishDate1770134400000仅Feb4 date-level；v1SubmittedFeb4T04:39:46Z、v1UpdatedFeb5T01:26:12Z、DataCitecreated/registeredFeb5T02:53:25/26Z表明arXiv事件窗后。完整题摘的keyframe空间+单residual temporal token是具体潜在，但Seed是否更早公开正文、具体时刻未定，不评分、不进入Books、不授覆盖保证。可接受替代是Seed实际首公开正文的带时区时刻或完全落窗区间；只定点恢复1376，不扩Seed82条库存。

窗外恢复线索（不属于本窗，不阻塞本日）：[vLLM-Omni2602.02204v1](https://arxiv.org/abs/2602.02204v1)DataCiteregisteredFeb3T05:18:34Z公开上界在窗前，已读完整题摘仅留stagegraph/独立AR-diff engine身份，未假称旧日已审；[Salamah2603.04410v1](https://arxiv.org/abs/2603.04410v1)SubmittedFeb3而MarchID/AvailableMarch、v1Updated/registeredMar6，不用提交日当公开日。日期事件与具体归属待定点恢复，均不扩本窗。官方移除版本[Legal01474v1](https://arxiv.org/abs/2602.01474v1)原生withdraw/license removed不入选、不评分或Books；root已直接重开exact-v1官方abs核withdraw/rights administrative removal；负侧通过，仅原始排除，不入评分分母。

## 6. 复核

复核者：root（报告非作者）

结论：通过

已实际通过范围：33家族完整题摘/官方core分批准入校准；18项整合的必要原源、具体owner差异、实际正文/前后衔接及末注POST（Ch84、72、54、56、49、27、33两处、45、28、34、77、82、80、75、23、25两处）。最后四项已核AAC Eq4–5/短输入反侧、Semantic Routing层融合/深度与time/SNR反侧、World Model/POMDP真实state-goal-query与width-two条件、LIVE Eq9–14/长horizon及额外预算；03146原排除表述过宽，已改为只有观测且缺真实state/goal-query接口的情形不继承，并获实际改后POST通过。

12项具体已有覆盖已核：GPT5.3原card L335–478与Ch72 542–569；TokenSparse Ch43 108–132；POP原§3.3与Ch43 65–77、last-input/first-new-token窄修写后；FailurePrediction必要critic/干预反侧与Ch80 333–343；A-RAG hierarchical/read工具与Ch76 65–80；Risky surface/access配置与Ch72 580–603；LPS mock/wholetrace/clarify与Ch78 24–65；Memora §3.4–3.6/§4.1–4.2与Ch77 229–248/362–368；PnP §3.1–3.4与Ch23 53–67/280；EBJEPA §3/Eq1–8/§4IDM/§5反侧与Ch25 251–255；TRT选择/累计oracle/正确被丢及reflection成本与Ch80 185–228；MAF三planning接口/格式错误/§4.1与Ch66 51–59/187–201。行号为实际对读时位置，后续插入可能移动，不以旧行号替代具体正文。

FalseFirst全部69序列LASSO/GeneralDiscussion/限制的仅报告处置已核；Foresight Eq6/reward/B.2、Distill Eq9/Alg1 6–9中心争议隔离已核。普通负侧为Privasis03183、KTV03615、UnifiedEval03238三份完整题摘贡献前关闭；Legal01474 exact-v1原生withdraw/rights行政移除另外直接核，不入候选或评分。14来源行的主题边界、实际入口/停止与失败范围、逐ID日期原字段及公开区间推定/窗外/VTok保留身份已分批核，未把宽分类或年度目录变成队列；四组外部来源限制不授正面覆盖。未变化已通过范围复用；没有独立遍历全部全文/附录，也没有性能复现。root已实际通读最终六部分，结合全部33家族必要原源/owner/实际POST、14来源范围与日期、三项普通负侧及withdraw核验，最终独立日级语义Gate通过；无尚可执行的本窗待办，外部终态保留项不授正面Evidence或无遗漏保证。

机器校验：`python3 scripts/validate_research.py --report papers/2026/02/05/README.md`实际通过（1份V3）；本日README、sources及授权改动章节的限定`git diff --check`实际通过。机器只能确认结构/可判定一致性，不能替代语义Gate；未stage、commit或push。
