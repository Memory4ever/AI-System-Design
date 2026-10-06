# Daily Research — 2026-04-11

**规范：** V3
**窗口：** 2026-04-10T09:00:00+08:00 ～ 2026-04-11T09:00:00+08:00
**窗口说明：** 用户授权冻结原窗口、原候选日期/评分与连续原§4，只补来源遗漏，不迁移旧材料归属。
**补充窗口：** 2026-04-10 ～ 2026-04-10
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-14T11:38:59+08:00

## 1. 结论

原小时窗有效层恢复了14个每日来源，处理Seed Protenix-v2、MiniMax CLI v1.0.6/v1.0.7、Kimi CLI 1.31.0四项；原候选空集与连续原§4冻结。原验收仅针对旧窗，不代替下面完整自然日补查。

本次有界查漏实际读43个唯一arXiv完整题摘（12+17+14），42个精确v1的公开日上下界合证成立，07397仍缺日期下界；4项arXiv按具体增量前分母关闭，Axios另1项，共39个当窗准入家族。最终处置为27整合、6已有覆盖、1仅报告、5中心理论/配方争议隔离；34项必要审阅完成，5项争议已读足关键反側并安全隔离，不授其正面Evidence。27个整合家族在17个唯一owner实际写入并经root非作者逐项POST通过。Anthropic实践说明无独立机制关闭，Seed Nexus缺当日原始公开链上界，不倒填后出论文。来源/筛选/必要审阅/Books普通待办为0，本轮非作者日级DAY通过且三句行政/衔接修正已保存，完成态FINAL已由root实际读回通过；终态保留项不支持全源无遗漏。[补查证据与实际边界](../_sources/daily-20260411/SUP_SOURCES_20261014.md)、[旧窗查询](../_sources/daily-20260411/v3-reopen-notes.md)分层保存，旧完成声明不作本輪验收。

重要的设计差额不是新模块数量：WorldMAP把生成未来改为结构化teacher监督，ASR把encoder更新与consumer适配限定在训练版本边界；HDPO/FGRPO/SPARD分别改变比较人口、反馈尺度和权重状态，均需独立结果与成本验收。Unlearning的retain-only retrain反侧阻止把feature可分冒作样本残留，CIM则将静态权重与动态attention操作数的存储假设分开。正面机制、局部收益和中心争议在下文逐项限定，不把局部报告推成普遍性能或安全保证。

## 2. 来源覆盖

本日只处理14个每日来源及已知候选的必要官方原文，没有扫描Weekly组或新增按需站点发现队列。旧小时窗的有效目录层仅在身份/范围/停止依据不变时复用，受影响的自然日早段、事件和资格单项恢复。表内“受阻”子入口与以下保留项已隔离，不授其Coverage/Evidence或无遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)、[Index](https://openai.com/research/index/)现行首屏9项止08-18/Load more；[News RSS](https://openai.com/news/rss.xml)1230项按Apr09T16Z～Apr10T16Z筛自然日，Axios为Apr10T00Z且实际完整官方正文/FAQ；Research/Publication sitemap只作身份线索，不用lastmod当首发 | 受阻 | 已知Axios完成必要安全深入与Ch72真实POST；Academy教程无机制增量关闭。历史Research分页未恢复，隔离该子入口，不能称全源无更新 |
| SRC-ANTHROPIC | 复用[Research](https://www.anthropic.com/research)170个publishedOn有效身份层；旧窗下界04-09T16:34Z的trustworthy-agents本自然日触及，实际完整[本文](https://www.anthropic.com/research/trustworthy-agents)L16–63；上界04-14T13:01Z | 已检查 | 五旧原则、PlanMode与澄清训练实践重述，无新具体机制或受控边界，前分母关闭；只限此官方目录，不含未列作者稿 |
| SRC-GOOGLE-AI | [April Blog](https://research.google/blog/2026/04/)整月9条，04-13→04-09→04-08；ConvApparel原文/ACL身份已核；[DeepMind selected publications](https://deepmind.google/research/publications/)264项首屏已跨04-22→03-22 | 受阻 | Google Publications只有年级facet，日级历史停点未恢复；ConvApparel日戳无时区，论文为March2026既有身份，不冒充本窗新稿 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)实际返回0可读行，不能恢复历史日期停点 | 受阻 | 缺官方Research/Publications当窗归档；空页面不是零命中 |
| SRC-QWEN | [动态列表](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项与[静态配置](https://qwen.ai/api/page_config?code=research.research-list)60项，动态04-02T04:00+08→04-15T10:00+08，静态全早于2026 | 已检查 | 官网Research合并列表无当窗条目；不证明全体作者稿不存在 |
| SRC-DEEPSEEK | [研究与动态](https://www.deepseek.com/news/)可见研究06-24→02-25、动态04-24→2025-12-01，越过本窗 | 已检查 | 结论限可见官方目录，不扩张为未列作者稿零遗漏 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)所见最新2025-11-07；Kimi-K2.5官方release API空；kimi-cli全release分页超时/截断，但已直接恢复[1.31.0 release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.31.0)，04-10T14:45:26Z在窗内，完整说明和5项贡献消歧PR已读 | 受阻 | 已知release逐项局部关闭，不用分页失败掩盖它；April完整Blog/CLI发布停点仍缺，隔离后不检普通commit |
| SRC-TENCENT-HUNYUAN | [官方Research](https://hunyuan.tencent.com/research)publicList，page1/size100/renderType0，total9/list9；displayPublishTime04-30/04-23→02-13 | 已检查 | “全部”目录无当窗条目，不表示全体作者稿无命中 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)日期04-29→04-07→04-01，之后03月/2025年；已越过日窗 | 已检查 | 04-07未标时区但不与本窗相交；不用CMS createdAt证明首发 |
| SRC-BYTEDANCE-SEED | 复用[Papers](https://seed.bytedance.com/en/public_papers)type1/US locale旧0/20/40下界层，本轮定点API token40取回Nexus ID1657（PublishDate Apr09T16Z）完整题摘/外链及[精确v1 history](https://arxiv.org/abs/2604.09258v1)；[Blog](https://seed.bytedance.com/en/research)type2旧0/20已跨Apr22→Apr08T16Z→Mar31，页20至2025年 | 受阻 | 本自然日Nexus是后建CMS目录项，需Apr10真正原始发布链，不能由PublishDate倒灌后来paper；Protenix仅旧窗关闭、自然日为Apr11，不迁移。未称全242/95逐全文 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)04-15→02-06，之后2025年；[ERNIE releases](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100)1条2025-06-30 | 已检查 | 所查Blog/release无当窗条目，不代替全部百度作者论文 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper06-29→03-13→02-03；MiMo/MiMo-VL/MiMo-V2-Flash官方release API均0 | 受阻 | Paper/release已处理；Blog无可靠历史日期，隔离该子入口 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)05-26→03-18，[中文Blog](https://www.minimaxi.com/blog)跳转官方minimax.cn，04-27→03-18；CLI release26条含当窗v1.0.6/1.0.7已读发布说明及后者2-commit发布差异 | 受阻 | 两个当窗CLI事件已具体关闭；M2/M2.5 release API空；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)与llms.txt只有现行无日戳文档，历史日期缺口隔离 |
| SRC-ARXIV | 自然日包含[常规公告](https://info.arxiv.org/help/availability.html)Apr10BJT槽；model `(CL\|LG)+(transformer\|language)` submittedApr08T16Z～Apr09T16Z API total150仅返回100（不等100全已读），tail start100/max100 Timeout后429；model/system窄query429、multi/agent超时。替代12官方分类April原始页相关title与Apr10 OAI identity交集，只定点43完整题摘，再按贡献处理；41精确v1晚提交公告下界+Apr10 DOI登记上界，07628另核Wed截止后提交的同v1上下界，合42定日；07397保资格缺口 | 受阻 | 辅助query检索受限，07397必要公开日缺下界，安全隔离；不宣称完整150或全学科召回，宽月列表不转全AB/全文队列；不是zero-hit。07397及旧03263精确边界见§5；普通已选材料审阅继续 |

## 3. 候选与判断

原窗口冻结候选为0；以下39个是本自然日新增准入家族，跨来源/章节不重复计数。各I因确认长期知识缺口定点深入其机制、关键评价/直接反侧及owner，不因此遍历全附件；NC/Only为具体标准审阅，D为中心争议安全終态。公开日基于同一精确v1身份、官方常规公告下界与Apr10登记上界/OAI合证，非单字段或精确秒筛选；07628另经Wed deadline后的提交身份恢复上下界，不迁移旧候选日期。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Axios developer-tool compromise](https://openai.com/index/axios-developer-tool-compromise/) | 2026-04-10 | 构建依赖执行权限与签名/notarization资产、迁移撤销分责；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SOLAR 2604.08368v1](https://arxiv.org/abs/2604.08368v1) | 2026-04-10 | base谱basis/seed重构的post-hoc传输表示，区别于再降LoRA rank；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [StableOPD 2604.08527v1](https://arxiv.org/abs/2604.08527v1) | 2026-04-10 | student occupancy重复反馈、额外gold loss与reference约束分工；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [MIG/offloading 2604.08451v1](https://arxiv.org/abs/2604.08451v1) | 2026-04-10 | 固定compute/memory profile容量缺口的C2C host-spill策略边界；2+2+2=6 | 深入完成 | 整合：PLATFORM-GPU-SCHEDULER [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [Sinkhorn rank decay 2604.07925v1](https://arxiv.org/abs/2604.07925v1) | 2026-04-10 | 无skip秩坍缩反侧与局部softmax复合不能替全局Sinkhorn界；2+1+3=6 | 争议 | 暂缓：中心remainder/真实算子证明缺口见§5 |
| [GQA co-localization 2604.07766v1](https://arxiv.org/abs/2604.07766v1) | 2026-04-10 | diagnostic层敏感度与RoPE干预位置不同，但中心recipe对照矛盾；2+1+2=5 | 争议 | 暂缓：精确实现/受控消融缺口见§5 |
| [DoGraph 2604.07963v1](https://arxiv.org/abs/2604.07963v1) | 2026-04-10 | 模型梯度域分区与权重目标接口不闭，限制“最优”配方；2+2+2=6 | 争议 | 暂缓：A.6无w目标与solver缺口见§5 |
| [TSUBASA 2604.07894v1](https://arxiv.org/abs/2604.07894v1) | 2026-04-10 | 有类型时效记忆与teacher特权上下文分责，推理仍需grounding；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)、TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Implicit curriculum 2604.08510v1](https://arxiv.org/abs/2604.08510v1) | 2026-04-10 | 阈值敏感与正确样本FV/LOO曲线预测人口分责；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Tempo 2604.08120v1](https://arxiv.org/abs/2604.08120v1) | 2026-04-10 | query-conditioned局部memory表示与全局decoder预算分责；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Cram Less 2604.08519v1](https://arxiv.org/abs/2604.08519v1) | 2026-04-10 | wholefact/head-flatten与token筛选、准确率/覆盖/预算分责；2+2+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [PPT-Bench 2604.07749v1](https://arxiv.org/abs/2604.07749v1) | 2026-04-10 | baseline stance与hedge、单轮/多轮压力排序测量分责；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SepSeq 2604.07737v1](https://arxiv.org/abs/2604.07737v1) | 2026-04-10 | 值/索引与delimiter格式、token边界及数值handoff分责；2+1+2=5 | 深入完成 | 整合：MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [Frozen LLM graphs 2604.08335v1](https://arxiv.org/abs/2604.08335v1) | 2026-04-10 | 冻结模型间可训latent channel与activation反传/执行费用；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)、TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Atomic long-context 2604.07981v1](https://arxiv.org/abs/2604.07981v1) | 2026-04-10 | NIAH读取、组合/冲突与动态状态能力切片不能相互替代；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [CivBench 2604.07733v1](https://arxiv.org/abs/2604.07733v1) | 2026-04-10 | 进度proxy、held-out校准与终局修正/相对人口分账；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GenCircuit 2604.08192v1](https://arxiv.org/abs/2604.08192v1) | 2026-04-10 | 跨模型DDB与固定模型CSS参考/带gold surrogate校准分责；2+1+2=5 | 深入完成 | 整合：PLATFORM-MONITORING [Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Entropy allocation ASR 2604.08003v1](https://arxiv.org/abs/2604.08003v1) | 2026-04-10 | encoder snapshot更新与consumer适配的训练表示版本边界；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [DiADEM 2604.08425v1](https://arxiv.org/abs/2604.08425v1) | 2026-04-10 | annotator分布/variance训练接口与argmax零梯度中心冲突；2+1+2=5 | 争议 | 暂缓：可微variance估计/实际梯度缺口见§5 |
| [Visual MoE routing 2604.08541v1](https://arxiv.org/abs/2604.08541v1) | 2026-04-10 | domain-reference expert提案、小幅softbias与hard/mismatch回归分责；2+2+2=6 | 深入完成 | 整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md) |
| [HDPO 2604.08545v1](https://arxiv.org/abs/2604.08545v1) | 2026-04-10 | 全组accuracy与correct-qualified工具效率的两adv人口；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [SPARD 2604.07837v1](https://arxiv.org/abs/2604.07837v1) | 2026-04-10 | reward criteria反馈权与data-category loss权两种状态；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [HiExp 2604.08124v1](https://arxiv.org/abs/2604.08124v1) | 2026-04-10 | 经验抽象粒度/initial与runtime消费、条件训练和依赖分责；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [RewardFlow 2604.08536v1](https://arxiv.org/abs/2604.08536v1) | 2026-04-10 | adaptive多reward梯度/clean-latent tether但VQA ascent符号矛盾；2+2+2=6 | 争议 | 暂缓：Eq4正确方向/同配置评估缺口见§5 |
| [Unlearning 2604.08271v1](https://arxiv.org/abs/2604.08271v1) | 2026-04-10 | 输出抑制/feature可分/特定训练样本影响不能互证；2+1+3=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [DMLE 2604.08284v1](https://arxiv.org/abs/2604.08284v1) | 2026-04-10 | 规则formula/description共享层与关联instance另一层组织；2+2+2=6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [PASK 2604.08000v1](https://arxiv.org/abs/2604.08000v1) | 2026-04-10 | silent/fast/full读取预算与深读后最终介入分开；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [AQA 2604.08294v1](https://arxiv.org/abs/2604.08294v1) | 2026-04-10 | 细动作质量需rank/error/contrastive gap与专家参照分账；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TrilinearCIM 2604.07628v1](https://arxiv.org/abs/2604.07628v1) | 2026-04-10 | 静态权重/动态attention操作数的介质与数据路径取舍；2+2+2=6 | 深入完成 | 整合：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [WorldMAP 2604.07957v1](https://arxiv.org/abs/2604.07957v1) | 2026-04-10 | 生成未来→derived semantic map/planner→student伪监督的消费位置；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Entropy-Gradient Grounding 2604.08456v1](https://arxiv.org/abs/2604.08456v1) | 2026-04-10 | first-token gradient读取提案与spatial concentration stop资格；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [FGRPO 2604.08476v1](https://arxiv.org/abs/2604.08476v1) | 2026-04-10 | correct/bbox masks、独立adv尺度与clipped dual反馈分责；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [TTVS 2604.08468v1](https://arxiv.org/abs/2604.08468v1) | 2026-04-10 | original/variant/mixed共识人口与伪label谱系分责；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Goedel agent reactivation 2604.08388v1](https://arxiv.org/abs/2604.08388v1) | 2026-04-10 | 通用agentic prefix+verified专用completion的受限接口再适配；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [NUMINA 2604.08546v1](https://arxiv.org/abs/2604.08546v1) | 2026-04-10 | latent attention→count-layout保守校正→regeneration条件分支；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [MolmoWeb 2604.08516v1](https://arxiv.org/abs/2604.08516v1) | 2026-04-10 | privileged structural teacher到visual action的数据/消费接口；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)、TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)、MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [TrACE 2604.08369v1](https://arxiv.org/abs/2604.08369v1) | 2026-04-10 | inter-rollout agreement只提call-budget，不是step正确校准；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [SAVeR 2604.08401v1](https://arxiv.org/abs/2604.08401v1) | 2026-04-10 | persona候选→LLM audit/repair→score不是独立真值；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)、MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [UniViGU 2604.08121v1](https://arxiv.org/abs/2604.08121v1) | 2026-04-10 | generator-first sharedattention/modalityFFN及连续text噪声身份；1+2+2=5 | 标准完成 | 仅报告：架构事实已核，但完整替代的性能/兼容边界未量化支持 |

以下为原小时窗冻结证据与处置，‘无正式候选’只属于该旧窗口。

## 4. 证据与知识整合

**Seed Protenix-v2**：官方论文目录PublishDate=1775836800000，即2026-04-10T16:00Z（本窗内的目录事件），外链为[生物分子结构预测与设计v1](https://www.biorxiv.org/content/10.64898/2026.04.10.717613v1.full.pdf)。该标题已明确是当前暂缓的AI for Science；不是大模型Training/Inference/平台机制研究，前分母关闭，不评分、不全文深审、不修改Books。目录时刻不当作论文首发证明；范围处置已确定，无需另建日期请求。

**MiniMax CLI v1.0.6**：[正式release](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.6) published_at=2026-04-10T05:15:40Z。发布说明为默认音频输出文件扩展名、SSE流解码成raw audio与EPIPE处理（PR63/60）；是具体客户端correctness修复，不改变模型推理状态、长期流控/协议或平台设计结论，前分母关闭。不能因“stream”关键词而保留或推成新的serving机制。

**MiniMax CLI v1.0.7**：[正式release](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.7) published_at=2026-04-10T08:31:19Z。[发布差异](https://github.com/MiniMax-AI/cli/compare/v1.0.6...v1.0.7)共2提交，只删除重复SKILL.md与package.json版本号更新；无长期机制增量，前分母关闭。没有把缺release正文等同材料受阻，也未扫描全部普通commit。

**Kimi CLI 1.31.0**：[正式release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.31.0) published_at=2026-04-10T14:45:26Z。完整发布说明中的有歧义条目已定点打开原始PR：[todo](https://github.com/MoonshotAI/kimi-cli/pull/1742)将root/subagent计划状态分开持久化、加查询模式与保存时刷新，模型重复调用的背景是空输出和Shell禁用，PR手工无storm验收仍未勾选，不能证明通用Agent控制已解决；[凭证刷新](https://github.com/MoonshotAI/kimi-cli/pull/1822)使用进程内锁→跨进程advisory文件锁→重新读token，锁失败仍无协调刷新，不能升级成可靠性/安全保证；[断流](https://github.com/MoonshotAI/kimi-cli/pull/1800)是特定SDK异常守卫与启发式分类，[think-only](https://github.com/MoonshotAI/kimi-cli/pull/1801)是不把不完整模型输出静默算TurnEnd；[启动升级提示](https://github.com/MoonshotAI/kimi-cli/pull/1826)保留继续/跳过选择，不是后台强制安装。它们分别修复一个客户端的状态存储、token-rotation race、错误分类与交互提示；未给出新的长期机制、受控设计反证或新的发布/安全保证，前分母关闭。持久化事实状态与确定性提交/重试分权在[Ch81](../../../../books/part-07-agent/81-workflow.md)主线已成立；这里不是凭章节相关性自动保留，也不把已有通用原则的局部bug修复全部升为研究候选。

以上是前分母关闭说明，不冒充候选已读全文。没有正式候选，Books判断终态为无必要改动；不调整既有设计结论，不新增知识owner。

本次完整自然日补查：以下为已处置批次，不替代原小时窗的有效证据。

### [Axios developer-tool compromise](https://openai.com/index/axios-developer-tool-compromise/)

官方全文What happened/Investigation/FAQ明确floating Actions tag与未设minimumReleaseAge，使签名workflow运行恶意Axios依赖并可接触签名证书/notarization材料。采用的是依赖身份、构建执行权限、签名资产和客户端迁移四层分责，不将“no evidence”写成未泄漏证明，也未独立读取取证日志。分别阻止旧材料生成新notarization、发行新证书签名版本、迁移窗后撤销旧证书，不伪造执行先后。Ch72在原TanStack案例后新增两段，保留旧训练产物链和后文provenance，root已实际POST验收。

### [SOLAR 2604.08368v1](https://arxiv.org/abs/2604.08368v1)

精确v1 §2–3/Table3–5与A必要假设支持post-hoc basis/索引/系数/seed重构分支，不等低秩截断；least-squares后top-k不是稀疏最优，理论依赖初始化/数据/谱条件。1B MMLU30.1→28.3与模型名矛盾收窄“any adapter/no loss”，不采用记法有疑的逐字实现；SVD与重构费用不从少bytes推推理更快。Ch30原LoRA-Squeeze后新增一段，root实际POST通过。

### [StableOPD 2604.08527v1](https://arxiv.org/abs/2604.08527v1)

精确v1 §3–5/Eq5–6/Table1–3与必要C参数支持student访问重复states的reverse-KL反馈及off-policy gold-loss/reference约束分工，区别于DAgger改变occupancy。忽略clipping不是全局因果证明；tail长度定义冲突、缺mixture-only消融、late mild drift保留；7B仅3.8pp，不能套用1.5B7.2pp。额外teacher/reference/gold费用近文保留。Ch29 DAgger后两段实际写后通过。

### [MIG/offloading 2604.08451v1](https://arxiv.org/abs/2604.08451v1)

精确v1 III/V-B1/VI与受限GH H10096GB、七并行同任务条件显示固定MIG profile显存缺口不必一律提升compute档，可比较host spill；α偏重性能时Llama3 FP16 offload并不优，FAISS短内存突发才更有利，Qiskit原swap也可更优。MIG未隔离power/C2C、20ms GPU NVML非全端到端能耗。Ch63 sharing表/application交接后新增一段，不重复Ch54offload路径，root实际POST通过。

### [Sinkhorn rank decay 2604.07925v1](https://arxiv.org/abs/2604.07925v1)

精确v1 §2–4/C/D的Eq7–8由一阶近似直接推严格界、C/D所算softmax复合局部导数不等真实正矩阵Sinkhorn迭代，缺remainder控制。实验在full Transformer训练后inference禁skip/MLP，AGNews/MNIST与100 sampled paths/random矩阵反侧不能证明任意LLM正面理论。root实际反侧独核通过，中心定理隔离，不写Books正面结论。

### [GQA co-localization 2604.07766v1](https://arxiv.org/abs/2604.07766v1)

精确v1 §3–5/T3–5：15minimal-pair hidden cosine是diagnostic非因果；all32 probe与插值、α与sqrtα/only-K RoPE记法矛盾。四配置不是组件删除消融；own A六项全部低于base，ARC A<B又破统一A优结论。root实际独核，中心最优recipe暂缓，不因负面结果或小理论排除。

### [DoGraph 2604.07963v1](https://arxiv.org/abs/2604.07963v1)

精确v1 §2–3/5/A.6：gradient-kernel MMD不保证真实域可识别，模型当前投影/Kmeans分区不等dataset ground truth；A.6 robust Lopt无w却给softmax optimizer、variance第一项亦无w，目标/solver不闭。LogiQA反退与模型人口记法矛盾限制泛化，root实际核中心公式同意争议隔离。仅分区描述可报告，不将“最优权重”写进Books。

### [TSUBASA 2604.07894v1](https://arxiv.org/abs/2604.07894v1)

精确v1 §4–6/T2–3：typed ADD/UPDATE/RECONCILE/IGNORE、teacher全上下文而student只问题、self-QA/top-d蒸馏仍保推理检索grounding；无检索T2明显退化、动态记忆部分配置低于static、open-domain反退。LoCoMo过滤/last8pairs与PRO配置不同，input tokens非全成本，target-user-only不证隐私。长期typed history/时间非事实身份已在Ch77 90–121/170–175，训练特权与运行时事实分责已在Ch29 contextdistill/DiSC近文覆盖；不声称已实现本论文QA生成或teacher-forced recipe。root对原证及承载正文实际读回确认，无必要Books差额。

### [Implicit curriculum 2604.08510v1](https://arxiv.org/abs/2604.08510v1)

精确v1 §3–5与必要F/G：固定80%与relative-best threshold不同，组合有19weak/3strong反序；正确样本FV、按model选head/hidden及smoothed LOO需要目标表示，不能说完全不知target。Ch28 class/item轨迹后补一段阈值/人口/sensor与费用退路，不批准因果先修课程，root实际POST通过。

### [Tempo 2604.08120v1](https://arxiv.org/abs/2604.08120v1)

精确PDF header DateApr10及§3ATA/Eq3–4/Alg1/P7–8 Tables1–2与HTML core一致；HTML Aug24为转换日期差异，不作版本首发证据。小VLM局部后置memory汇聚，再按同次Yes/No logits分配全局输入；最小总预算与可得token上限须另处理，O(1)只是已有hidden截取。HardTopK/ToMe部分优于ATA、base relevance有更好任务，4K/8K不单调；不从timestamps推因果或免费计算。Ch23原query→eventframe budget后补一段局部latent分支，root实际POST通过。

### [Cram Less 2604.08519v1](https://arxiv.org/abs/2604.08519v1)

精确PDF §3事实/离散W条件、§4 Alg1–2/Wiki评价及D2–3：完整fact answer loss sum的online percentile选head，可选flatten最易重复，Wiki保nonfact并重标答案mask。α.1 NLU退、factaccuracy匹配大模型非全能力，66k backward steps不等candidate forward/grid总FLOPs，不采普遍2bits容量。Ch27 AlignPrune后新增wholefact单位/coverage取舍一段，root实际POST通过。

### [PPT-Bench 2604.07749v1](https://arxiv.org/abs/2604.07749v1)

精确v1 §3–5/Limit：90items、四压力/单轮与多轮三层，stance与hedge复合标签依赖GPT4o单judge及有限人工一致性，单/多轮模型排序不同。Prompt/local-decoding两pipeline和near-zero 24eval小split不拼成防御保证；合法新证据修正应另计。Ch66 SWAY后补一段，区分baseline/hedge/stance/history判分与费用，root实际POST通过。

### [SepSeq 2604.07737v1](https://arxiv.org/abs/2604.07737v1)

精确v1 §3–4/Limit的delimiter替换改变长数值读取，但替换输入会改变全部Q/K，不能由固定QK假设认证严格sink隔离界；0.6B/复杂separator有反退，Table1/2均值记法不一致。16.4%为response长度，不等总token/墙钟，PoT仍可共存。Ch11同string分词接口后补一段值/索引与格式/实际token核验、数值工具handoff，root实际POST通过。

### [Frozen LLM graphs 2604.08335v1](https://arxiv.org/abs/2604.08335v1)

精确v1 §3–5/Limit为3frozen encoding/projection到2frozen residual consumer及learned4choice head。Single-head非matched五model无通信控制，非零gradient不证明独立信息、frozen参数仍有activation反传/执行费。Ch82 317–389已具体承载latent proposal→receiver-native残差/冻结融合，Ch30 138–160已承载冻结参数的activation成本；root实际NC通过，仅这些稳定接口/费用已有覆盖，不声称实现整个五节点图。

### [Atomic long-context 2604.07981v1](https://arxiv.org/abs/2604.07981v1)

精确v1 §2–4.3/结论，五技能anchor构题/相关性与训练有具体潜力，但相关不证正交或因果先修，RL mixture/筛题/YaRN/teacher评分共变，MRCR及加数据反侧保留。Ch22 95–106/125–140实际已有读取非组合、冲突/动态状态与长度/输出/费用分账，root NC通过；不声称完整论文课程配方已实施。

### [CivBench 2604.07733v1](https://arxiv.org/abs/2604.07733v1)

精确v1 §3–6/A2的progress predictor、relative standing、civilization OLS及BT分账，146/551 winner-preserving correction带终局信息，非纯在线进度。Five-fold game/OoF校准、构念验证与实际LLM+setup+opaque tactical executor不是同一测量对象；nonDomination/war temporal和单seed等限制保留。Ch66 forecaster后新396段将三种验收与费用/回退相连，root实际POST通过。

### [GenCircuit 2604.08192v1](https://arxiv.org/abs/2604.08192v1)

精确v1 §3.2–4.3/Limit：mean-ablation KL/EAP-IG circuit proxy、跨模型DDB与固定模型CSS适用对象不同；39个带gold corruption surrogate校准阈值，target无label不等全链label-free。部分τ/ANE反侧和discovery费用限定相关性，不能认证内在truth或因果。Ch67 first-token sensor后新36段实际POST通过。

### [Entropy allocation ASR 2604.08003v1](https://arxiv.org/abs/2604.08003v1)

精确v1 §3.2–4.5/T1–3：phoneme encoder→frozen snapshot的IA-SFT/CKA触发→joint，谱/Gaussian proxy不证信息守恒。去hot-swap同时去async、plateau非equalcompute，Dialect等切片非普胜，hallucination只窄长度/完全无关failure，离线beam3非streaming SLO。Ch23 Training/Serving间新1049段保表示版本/consumer适配分责、全阶段成本与固定encoder退路，root实际POST通过。

### [DiADEM 2604.08425v1](https://arxiv.org/abs/2604.08425v1)

精确v1 §3–6与A1/A6/A7，predicted variance用argmax label却无可微surrogate/straight-through，普通反传为零的中心目标接口未闭；α×W不能单独识别人口因果重要性，VOICED variance与DICES差异不隐藏。root实际独核D通过，隔离正面训练配方，不因未公开实现整篇硬排。

### [Visual MoE routing 2604.08541v1](https://arxiv.org/abs/2604.08541v1)

精确v1 §3–5/Limit，domain-reference vs一般文本frequency提出expert、小幅layer-std softbias；100digit patch/JSD非通用语义或因果身份，hard/Top1与mismatch反退，不修perception缺证。Ch21 Gaussian router后新75段定义固定checkpoint的另一proposal分支、搜索与完整费用/回归，root实际POST通过。

### [HDPO 2604.08545v1](https://arxiv.org/abs/2604.08545v1)

精确v1 §3–4.4/Eq6–11/T3，accuracy全组与正确且至少2样本的tool-eff集合独立adv、两clippedloss仍共享θ；非gradient正交/准确率单调，小α展开条件与w.1/.2反退近文保留。额外filter/rollout/judge/tool与全training非调用数，Ch33分桶后新121段实际POST通过。

### [SPARD 2604.07837v1](https://arxiv.org/abs/2604.07837v1)

精确v1 §3–4.3/Eq5–13/Alg1/T1–3：reward-criteria EMA反馈和category loss权不是sampling。Δ(μ−βσ)也可因σ降为正，MAD可能judge噪声而非utility，不采LCB置信界/全域改进；GPQA去模块与LCB反退保留。Ch33整题权后新259段保两种状态/时钟/费用与静态mixture退路，root实际POST通过。

### [HiExp 2604.08124v1](https://arxiv.org/abs/2604.08124v1)

精确v1 §3–4.5/Limit，同题success/fail提E1case/E2strategy/E3原则，initial抽象层/runtime检索case条件化GRPO；mask经验/文档loss不消forward影响，trainedmodel仍HEK/检索依赖。E2/E3差异、math反退、static HEK不跟policy更新与全费用保，Ch77只读消费训练后新419段实际POST通过，不采已内化/删除bank。

### [RewardFlow 2604.08536v1](https://arxiv.org/abs/2604.08536v1)

精确v1 §3–5/T1–4，SP/reward反馈/step/tether构成具体推理期控制潜力，但Eq2 ascent与Eq4 -mean(logp+margin)在inactive margin时反降正确p，中心方向不闭。Full MSE T3与T1/T4矛盾、Edited去模块反优及全Jacobian/LLM/SAM/VQA费用不隐藏；root实际Eq1–4独核D通过，不替作者改符号，不写正面recipe或普遍Langevin收敛。

### [Unlearning 2604.08271v1](https://arxiv.org/abs/2604.08271v1)

精确v1 §3.1–4.3/T1–3：linear probe用含forget标签的全数据再训，retain-only retrain也高probe，故可分/迁移不证特定样本仍保留或隐私失败。Classifier-only压输出而feature保留支持窄错位观察，CMF绑定又让forget输出回升并有retain代价；不采NC假设为全网络定律。Ch27 EraseClean后新1043段明示counterfactual参考与新监督、全probe/重训费，root实际POST通过。

### [DMLE 2604.08284v1](https://arxiv.org/abs/2604.08284v1)

精确v1 §3–6.4/T2四arm支持formula/description早层joint与instance中层sequential的受限组织，1000 tracing是重复/随机而非独立rule，噪声恢复不认证唯一存储层；ΔW写法不补residual/retain项。模型/造题/grammar检查/DeepSeekjudge人口与Llama可靠性/locality反侧收窄普遍配方。Ch5获得/保留/泛化后新490段保form/instance/layer/顺序与全费用，root实际POST通过。

### [PASK 2604.08000v1](https://arxiv.org/abs/2604.08000v1)

精确v1 §3.1/4.2–4.3/5/6.1/T4/6.5：full检索→MemLoader后仍可abstain，上一workspace/anchor下subtree异步读取不保freshness/完整召回，post-session merging不保生命周期恒定费。100sessions3936turn/3prompt选最好/GPT5.2judge、memory/summary无同配独立消融，平均1.3–1.5s不是全<1s。Ch77主动干预后新265段保三分支/介入/旧state分责和退路，root实际POST通过。

### [AQA 2604.08294v1](https://arxiv.org/abs/2604.08294v1)

精确v1 §2–3.6/T1/4/5/Limit，低relative L2可能均值塌缩而rank差，contrastive质量差与Equal边界剔除改变人口；图像Gemini80%反侧不藏，正反rubric不唯一识别prior因果。不同帧采样/半resolution/120frame上限、ICL长度使比较条件不同；不推全VLM chance或fine-quality truth。Ch66 judge资格后新444段只采测量分账/全费与领域评分回退，root实际POST通过。

### [TrilinearCIM 2604.07628v1](https://arxiv.org/abs/2604.07628v1)

精确v1的Wed deadline后提交与Apr10登记合证恢复资格。§2–6.5/T2–7的DG-FeFET BG第三operand仍依赖conductance band近似、reference subtraction、loop/ADC-DAC及数字非线性。INT8PTQ/7nmCMOS+22nmFeFET模拟BERT/ViT，小seq相对bilinear有能耗/latency收益但面积+37.3%、ViT全退/RTE退；fab/read-disturb与decoder KV未验证。Ch14 IO段后新222段不授无限耐久/通用加速，root实际POST通过。

### [WorldMAP 2604.07957v1](https://arxiv.org/abs/2604.07957v1)

精确v1 III/IV/V及TableI/III：generated多video→depth/pose/semanticmap→target/obstacleBEV→FMM pseudo路径监督student，部署只student。GT+pseudo优于pseudo-only，VLM筛选不是真值，2D projected误差不认证实体navigation/safety；unknown blocked/margin仍是假设。全部视频/重建/grounding/规划/筛选/训练费保。Ch25三种model定义后新36段明确非actionchannel的训练消费分支，root实际POST通过。

### [Entropy-Gradient Grounding 2604.08456v1](https://arxiv.org/abs/2604.08456v1)

精确v1 §3–4.3/T1–7，entropy反传取gradient norm，Gaussian/elbow/components/topK crop+global view，空间面积entropy仅集中度、单component/plateau/iteration cap未闭。GeneralQA反退、Layer20及K4某任务更优不照allbest；T2/T7 latency口径不拼。Forward/backward/重编码全费，Ch23静态attention差crop后新823段不采因果充分证据或hardboundedstop，root实际POST通过。

### [FGRPO 2604.08476v1](https://arxiv.org/abs/2604.08476v1)

精确v1 §3.1–3.3/Eq1–6/4.1–4.5/T1–3，correct-only C/S与bbox人口不同、独立groupnorm后λmix/whiten；constant仍零adv，conditional masks与std改变Eq3原期望目标，有限λ不保hardconstraint。Qwen训练/GPT5.4评价judge分责不证内在faithfulness，MMVP/SATReal退且fixedλ IR1.11低于adaptive1.73。Ch33 HDPO后新125段保空人口/threshold/全费与outcome回退，root实际POST通过。

### [TTVS 2604.08468v1](https://arxiv.org/abs/2604.08468v1)

精确v1 §4–5/Limit/A1/A4/A9，以同model多数答案条件改写、原题agreement比例与变体长度过滤，独立IGE/mixedCGE。Agreement非真accuracy，length非等义，16candidate top-ranked与test adaptation不等greedy/heldout；每step32与相近显存不证全FLOPs相同，throughput更低，open-endedjudge仅未来路径。Ch33 solve/verify后新80段保共错/过滤支持域与全费，root实际POST通过。

### [Goedel agent reactivation 2604.08388v1](https://arxiv.org/abs/2604.08388v1)

精确v1 §3–4.4/5–6按actual lemma/retrieval/depth选择混合轨迹，100数据训练128epochs，非随机少量/低更新费。BFCL89.4→83.8属NonLive，Overall85.66→78.37且irrelevance显著退；ProofNet改善与MiniF2F/原RL模型回归共存。有限输出未生成theorem不证明未编码/先前只是抑制。Ch29轨迹接口后新238段保call/abstain、旧特化能力与全费，root实际POST通过。

### [NUMINA 2604.08546v1](https://arxiv.org/abs/2604.08546v1)

精确v1 §4–5.3/T1–5/Limit，head PCA/contrast等提区域、crossattention noun map/cluster筛count，删最小/复制或circle与overlap/center/前帧cost，再重新生成。Fixedseed/210prompts count1–8/1–3categories、detector同测CountAcc/TC，不认证对象身份/运动；8objects仍20.7%，292s14.3GB→431s16.3GB非免费。Ch24先问题/typedprogram后新1937段再接工具selector，root重排后实际POST通过。

### [MolmoWeb 2604.08516v1](https://arxiv.org/abs/2604.08516v1)

精确v1 §2–4.6/6，AxTree bid→pixel action、student仍URL/title/history，数据mix共变，same-task2.7k对照不保全部人/合成配置普胜。Liveweb站点/100steps/10retries/captcha/judge条件不拼榜，pass4是oracle coverage非部署selector。Ch27 160–177直接承载teacher/student observation/action/browser/verifier lineage，Ch29行动接口示教与Ch20 coverage/selection全费也已有；root实际NC通过，不声称整套Molmo数据recipe已实现。

### [TrACE 2604.08369v1](https://arxiv.org/abs/2604.08369v1)

精确v1 §3–5，2起始agreement逐次加样本到cap的局部sensor；MiniHouse greedy/SC/TrACE皆.367，不能对greedy宣称提升。§5.3标签是step所在最终成功episode，非localstep正确；τ1可两次一致早停不必cap，GSM50/三seed及CPU量化人口有限。Ch20 340–385/480–503已有生成/选择预算、agreement非truth/误停与greedy回退/全费，root NC通过；不声称书实施该τ/cap配方。

### [SAVeR 2604.08401v1](https://arxiv.org/abs/2604.08401v1)

精确v1 §3.5/4.1/T1/3/Limit，DPP/persona、六类LLM critic/repair至10轮与qscore只belief proposal，Γ/Sat形式叙述非已核solver。六QA不是durable行动闭环，去Audit/Repair部分accuracy更高而ownfaithfulness较低，共享审计proxy偏差不消失。Ch81 64–123明确proposer/模型assessment、预算停机非truth与可信activation，Ch20候选选择/全费已有；root NC通过，不声称整套SAVeR recipe或真实action verifier已实施。

### [UniViGU 2604.08121v1](https://arxiv.org/abs/2604.08121v1)

精确v1 §2–4/6，Wan起点/sharedattention和modalityFFN、独立τ与text Gaussian embedding denoise再离散decoder，不等离散状态flow。Promptdropout/128vs256长caption不证视觉依赖，Eq11 loss reduction未闭；仅joint定性，无量化受控理解/生成或ablation，competitive不能采用。Ch24 typed/shared/理解辅助条件链已对读，root具体Only通过：保proposed架构上下文，不硬EX、不写未证性能，也不称整套实现已有。

## 5. 缺口与下一步

来源、筛选、必要审阅与Books普通待办：0。本轮非作者六部分DAY通过；以下是已穷尽当前有限恢复、隔离到本窗终态保留项的外部缺口或中心争议；不支持正面证据、Books、无遗漏断言或性能/安全保证，各项定点重开条件如下。Model tail50同query有限恢复Timeout→429、agent窄query超时只属辅助检索限制，替代相关标题范围不冒充完整150，不把普通未读隔离。

- [Seed Nexus 2604.09258v1](https://arxiv.org/abs/2604.09258v1)：后建CMS PublishDate Apr10BJT与v1 submittedApr10相冲突，缺Apr10实际可读原始发布链上界；需该日官方artifact/独立原始公开链，当前不将后来paper细节倒灌本日，定点恢复此family即可。

- Sinkhorn07925：需真实Sinkhorn算子及全局remainder控制/可复核反证，现不支持正面定理；仅定点重开中心命题。
- GQA07766：需明确probe层人口、精确α/only-K实现、组件删除与untuned/null/repeated对照，现不支持中心最优recipe；仅定点重开该命题。
- DoGraph07963：需含w的实际robust目标/solver、投影维度与匹配compute逐域对照，现不能采用最优权重保证；仅定点重开A.6与配方。
- DiADEM08425：需predicted variance argmax后的可微surrogate/实际梯度与同split反侧，现不采用中心训练目标；仅定点重开该接口。
- RewardFlow08536：需Eq4的VQA gradient-ascent方向、精确实现/可核reward定义及T1/T3/T4同配置指标对齐，现不采用中心recipe或普遍收敛；仅定点重开该命题。
- DataWarmup07397：更早Apr08提交不足以给Apr10首公开下界，Apr10登记独立不足；需官方精确公告或同版本可核public下/上界，现不进入确定候选或Books。TrilinearCIM07628已由Wed deadline后的精确v1身份与Apr10登记合证恢复资格，不再作为日期缺口，必要深入审阅与Ch14实际POST均已完成，无剩余可执行待办。

- OpenAI Research Index：首屏止于08-18，历史Load more未恢复；RSS和sitemap身份不能提供完整Apr日级停点。可接受替代为官方带日期的历史分页/完整本窗Research归档，到达后仅重开该子入口及其family。
- Google Research Publications：只有年级facet，无法证明本次Apr10补充自然日公开目录完整；DeepMind精选不是全作者稿。可接受替代为官方带首发日期的Apr10历史结果/本自然日归档，定点补查。
- Meta Research/Publications：Research正文为空，无历史日期停点；可接受官方可读本窗目录或当窗公告存档，定点重开，不能把无响应记无命中。
- Moonshot：Blog停在2025-11、kimi-cli release分页超时/截断，无April历史停点；官方当窗Blog索引/有效release分页到达才重开，不扩扫普通commit。
- MiMo Blog：现行卡片没有可核历史公开时间；官方单篇日期或April完整历史索引可重开，Paper/空release不足替代。
- MiniMax Agent Tech Blog：现行techblog/llms.txt仅无日戳目录；官方当窗历史归档或精确版本公开日期到达才重开，不从现行网页倒推。
- [LPC-SM 2604.03263v1](https://arxiv.org/abs/2604.03263v1)：官方当前history仅v1，旧OAI有Apr11日戳；DataCite created Apr07T02:37Z、Updated/v1 Apr11T04:37:54Z（在Apr11、位于本次Apr10补充自然日之外）、Available仅2026-04，任一单字段都不证明当窗first-public。其方法已在[Apr07](../07/README.md)日期保留项处理，本日不重复申请或重审；只有官方具体公告或可核更早public上界/重要修订证据到达，才定点恢复真实owner，不机械迁移。
- [ConvApparel](https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/)：Blog仅April9无时区；[ACL身份](https://aclanthology.org/2026.eacl-long.244/)已是March2026论文，本次是宣传线索而非确定当窗新family。若有带时区的当窗公开事件且独立机制增量才定点重开，不仅凭发现日重评分。

## 6. 复核

复核者：root（非本日报作者）
结论：通过

本次root实际分批独核覆盖全部43完整题摘及39准入家族的必要Source/关键反側、42日期资格合证、27个整合家族的逐字PRE/实际正文/完整局部邻接/本人note POST；6项具体NC、1项Only与5项D采用边界也已对读owner后通过。明确EX按来源/主题/理由校准：4个arXiv（Cartesian/MERS/DigitalHumanoid/DP-in-limit）、Anthropic本文、已知CLI实现关闭均实际核；宽月库存/全学科原始标题和未列作者稿不冒全量审阅。root已实际完整六部分DAY；三处行政/衔接窄修已落实，完成态FINAL已由root实际读回通过，分批Source或POST不代替日级验收。下一段仅为原小时窗旧验收说明。

root独立重读14来源行的实际停点与限制、四个关闭理由、八项隔离边界及空Books集合；定点重新取得KimiCLI正式release（04-10T14:45:26Z、17项变更）、原始PR1742/1822，并对读Ch81 activation/持久化/重试实际正文。确认本次关闭基于具体实现和证据边界，不是因“bug fix”标签；advisory锁失败降级与无通用storm/可靠性保证没有被隐藏。来源检查记录的复核不是逐一重新抓取全部机构外部目录，零候选不表示全网零遗漏。旧OAI数量矛盾已纠正为具体身份隔离，未伪造首发时刻、未复现实验。

原小时窗机器与空Books集合曾通过，不作为本轮结论。本轮V3、39唯一行/27整合+6已有覆盖+1Only+5D/17整合owner、14每日源、42本地引用零missing、原窗口/0候选/连续原§4 1748字符保持、限定README/SUP与17Books的cached/unstaged diff-check均实际通过；完整baseline快照cached第74行有new blank line at EOF告警，保留原字节不修改，不称该快照cached检查干净。机器不替代语义DAY/FINAL。既有dirty/staged/untracked均保护，不改State/索引/合同/scripts，未stage、commit或push。
