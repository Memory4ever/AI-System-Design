# Daily Research — 2026-03-23

**规范：** V3
**窗口：** 2026-03-22T09:00:00+08:00 ～ 2026-03-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T04:15:34+08:00

## 1. 结论

本窗确定候选 **1 个唯一家族**：Sora 既有安全说明的重要修订。其新增上传真人照片的 consent attestation、分层 guardrails 与分享标记条件属于版本相关安全边界，已深入核受影响内容，**仅报告 1、Books 新增 0**，不将产品配置泛化成认证或安全保证。

arXiv 四主题提交区间检索得到 149 个交叉命中、去重 **124 个标题线索**（非124篇本窗新论文）；实际精选 **28 份完整 v1 题摘**，1 个具体贡献前关闭，**27 个日期/准入保留**，不是27确定候选或Evidence通过。普通待办0，root最终非作者日级验收通过；5组外部历史来源限制与27项精确日期/准入请求已到有限终态，不支持正面覆盖或无遗漏。[旧正文仅保留证据](../_sources/daily-20260323/V3_LEGACY_REPORT_RESTORATION.md)，旧513池/15候选/旧分/EffectiveDate及旧Books认证均未沿用。

## 2. 来源覆盖

实际入口、原字段与停止位置详见[本日来源记录](../_sources/daily-20260323/V3_SOURCE_STOP.md)。只每日14源与本窗主题；宽目录只定位，不逐篇审机构历史。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 RSS 实际1242item，按本窗过滤仅Sora修订；当前core28–40与明确previous26–34定点对读 | 已检查 | 无；RSS证明本次修订事件，不证明家族首次公开 |
| SRC-ANTHROPIC | 官方Research嵌入174 publishedOn，9个March原日期/slug完整对读；Science三文Mar23T23Z=24T07 BJT | 已检查 | 可见原日期均窗外，不授机构全历史 |
| SRC-GOOGLE-AI | Research March archive12+2卡、2/2；DeepMind page3完整24卡与邻界三实际日期；Pubs year2026实际322973B但无可核本窗dated slice | 受阻 | H1：Pubs本窗主题历史公开切片 |
| SRC-META-AI | Research HTML实际286765B但无可用本窗日期；Engineering page1/2完整10+12卡、非严格时序，无22/23可见 | 受阻 | H2：Research本窗dated历史切片 |
| SRC-QWEN | 公共API40条metadata全部日期/标题，MaxPreview19→Omni30；无total/paging，当前可见无22/23 | 已检查 | 不认证所有历史或40篇正文 |
| SRC-DEEPSEEK | 本轮官方页+9467B公开脚本；News完整16原日期/Research隐藏数组恢复原值定点复用，六月→二月跨过本窗 | 已检查 | 不再保留假hidden目录故障；有限目录非全机构保证 |
| SRC-MOONSHOT | 新官方Kimi Blog19卡完整可见Jul16→Apr20→Feb09→2025 | 已检查 | 未以旧platform Blog截止2025作Research故障 |
| SRC-TENCENT-HUNYUAN | 实际publicList renderType0/page1/size20完整11/total11，displayFeb→Apr、published不同不互换 | 已检查 | 有限可见目录，无22/23，不授全机构历史 |
| SRC-ZAI | 官方Research完整15卡Aug→Apr01→Mar15→Feb→2025 | 已检查 | 停15可见，无本窗，不扩Github |
| SRC-BYTEDANCE-SEED | type1/token20完整18邻界metadata：1337本窗protein-ligand领域工具title范围关闭；type2/token0完整14/total19，next空/has_morefalse | 受阻 | H3：Blog total差额5的本窗主题metadata |
| SRC-BAIDU-ERNIE | 官方zh Blog实际10 dated卡May→Apr→Feb→Jan→2025，无本窗可见 | 已检查 | 仅可见停止，不继承旧分页完成 |
| SRC-XIAOMI-MIMO | 首页Paper8 dated/Blog15 undated；正确Pro/Omni原页core实际已读、March18明确窗外；TTS只undated标题 | 受阻 | H4：本窗dated Blog历史切片/TTS身份与日期；不猜route、不留已恢复core故障 |
| SRC-MINIMAX | EN12/CN13完整可见卡，March18→Feb及后April无22/23；AgentTech .md实际882B仅May13datedentry | 已检查 | 有限目录，不扩Guide/Github或声称全历史 |
| SRC-ARXIV | 四主题start0/max100/asc返回64/50/31/4，149交叉命中→124标题；28完整v1题摘与current header；合法cs.DC月目录250仅monthheader、一次export cs.CL250失败 | 受阻 | H5：本窗主题announcement/延迟旧Submitted及重要revision历史切片；27具体公开区间未完全落窗 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Creating with Sora safely](https://openai.com/index/creating-with-sora-safely/) | 2026-03-23T08:00:00+08:00 | 新真人照片上传授权声明与内容/分享约束，校正旧可见标记范围；本窗增量 1 + 2 + 1 = 4，不重复计算2025原家族贡献 | 深入完成 | 仅报告：产品版本规则与未披露执行机制，不改长期通用机制；无Books写入 |

## 4. 证据与知识整合

### [Creating with Sora safely](https://openai.com/index/creating-with-sora-safely/)

作者实际读官方当前core28–40、链接[此前版本](https://openai.com/index/launching-sora-responsibly/) core26–34。采用的是安全说明修订，而非新模型训练或控制器论文；官方RSS pubDate原值 Mon, 23 Mar 2026 00:00:00 GMT → BJT08完全落窗。

真人照片上传现在以用户 attestation 为条件，当前31另述人像/年轻人物更严 moderation 与分享标记；它不是身份或真实 consent 已由系统验证的证据。当前29说许多输出有可见动态标记，不沿用旧27“launch all”扩成所有输出当前都带同样可见标记。Characters撤回/草稿可见等与分层prompt/output/frame/audio检查保留共存，但文中没有可归因的新实现、漏检/误检受控评价、训练预算或部署成本；均 Not Disclosed，不授普遍安全性。

root已实际读当前28–40，首批准入与受影响安全边界校准通过。新增事实只限定该产品当时规则，并不建立新认证、watermark完整性或guaranteed control机制，所以仅报告，不虚构已有覆盖认证，也不为制造Books差额写入。April26关闭banner属当前页面后续事实，不回填March。

[完整题摘与筛选状态](../_sources/daily-20260323/V3_SCREENING.md)、[首8日期/header原值](../_sources/daily-20260323/V3_FIRST_DATE_HEADER_PACKET.md)、[尾20日期/header原值](../_sources/daily-20260323/V3_EXTRA_DATE_HEADER_PACKET.md)均保留；题摘与索引不被当作性能、安全或Books证据完成。

## 5. 缺口与下一步

普通待办0，root最终非作者日级验收通过。来源/筛选/候选必要审阅/Books处置已完成到本轮有限停止；不得重复首波或扩窗。

本窗终态保留项，不支持正面证据、Books 或无遗漏断言：

**27具体日期/准入请求（每项仅一次）。** 共同必要材料是各精确v1的官方announcement/发行记录，或具有可核公开语义的timestamp。实际Submitted处于Thu14EDT→Fri14EDT，最早常规公告为Sun20EDT=03/23T00Z=BJT08；arXiv-owned findable DOI registered全部晚于右端03/23T01Z，复合区间跨右端。registered是upper非exact，晚注册也不证明nextday；Updated没有公开语义不作upper。合法月列表与一次mirror补试已有限停止，未取得更精确primary。恢复先日期，只有完整落窗才进入评分/必要证据；下面列出各身份与其定点机制，详细原值与重开条件在上述SCREENING/两日期包，不另扩全稿队列。

- [PowerLens: Taming LLM Agents for Safe and Personalized Mobile Power Management](https://arxiv.org/abs/2603.19584v1)：移动电源动作从prompt转PDL gate+implicitoverride偏好闭环→执行授权/偏好更新条件；绝对安全保证待证；先恢复精确公开区间，再定点核该增量/对照与限制。
- [A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469v1)：上下文授权评价与理想因果oracle；§4.3.3付款例与§4.4谓词冲突，具体见下面；形式保证不采用；先恢复精确公开区间，再定点核该增量/对照与限制。
- [LoopRPT: Reinforcement Pre-Training for Looped Language Models](https://arxiv.org/abs/2603.19714v1)：token末端RL不足latentrecurrent→EMA teacher/noisylatentrollout并优化内循环步骤→latentcredit与训练目标选择；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation](https://arxiv.org/abs/2603.20172v1)：同一行为faithfulness比率随classifier/rank变化→区分词汇提及与epistemic依赖→评价定义影响模型比较；先恢复精确公开区间，再定点核该增量/对照与限制。
- [The Autonomy Tax: Defense Training Breaks LLM Agents](https://arxiv.org/abs/2603.19423v1)：防御训练不只攻击成功率→benign任务先失败/级联→robustness与autonomy共同评价；不直接采用比率或因果；先恢复精确公开区间，再定点核该增量/对照与限制。
- [The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference](https://arxiv.org/abs/2603.19664v1)：KV由residual可重算→提出保留residual而重算层投影→内存/算力与精度选择；bit-identical及规模界限待证；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States](https://arxiv.org/abs/2603.19987v1)：纯trajectory缺显式近Markovstate→重新引入结构状态/状态估计→推理后训练sample-complexity与能力界限；先恢复精确公开区间，再定点核该增量/对照与限制。
- [DataProphet: Demystifying Supervision Data Generalization in Multimodal LLMs](https://arxiv.org/abs/2603.19688v1)：多模态监督迁移并非similarity排序→perplexity/similarity/diversity预测14datasets7tasks→数据选择信号与适用界限；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Evolving Jailbreaks: Automated Multi-Objective Long-Tail Attacks on Large Language Models](https://arxiv.org/abs/2603.20122v1)：long-tailsemantic/encryption representation+effectiveness/perplexity多目标搜索；是否改变过滤边界或只是既有operators组合未明；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Pitfalls in Evaluating Interpretability Agents](https://arxiv.org/abs/2603.20101v1)：interpretability评价可能memorization/informedguessing→functional-interchangeability反证/replication检验→解释agent评估应测内在功能；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Semantic Token Clustering for Efficient Uncertainty Quantification in Large Language Models](https://arxiv.org/abs/2603.20161v1)：反复sampling估uncertainty昂贵→single-generation token语义cluster probabilitymass→一次输出的置信度proxy选择；先恢复精确公开区间，再定点核该增量/对照与限制。
- [The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents](https://arxiv.org/abs/2603.20320v1)：文本compliance不同toolaffordance实际违反→同prompt/policy配对block/permit与attempted/realized双层→安全评价不能只看回复；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Automated Membership Inference Attacks: Discovering MIA Signal Computations using LLM Agents](https://arxiv.org/abs/2603.19375v1)：LLM搜索新MIA信号tailoredmodel/data；题摘未明确相对手工信号新决策机制/泄露失效条件，准入含糊，不因组合自动关；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Adaptive Layerwise Perturbation: Unifying Off-Policy Corrections for LLM RL](https://arxiv.org/abs/2603.19470v1)：更新policy与rollout policy差距→hiddenperturbation进入importance-ratio numerator而inference不改→heavy-tail/KL稳定条件；先恢复精确公开区间，再定点核该增量/对照与限制。
- [An Empirical Study of SFT-DPO Interaction and Parameterization in Small Language Models](https://arxiv.org/abs/2603.20100v1)：GPT2小数据受控matched-depth SFT/DPO/FFT/LoRA→任务依赖边际与实际墙钟非收益→受限优化方案选择，非普遍LoRA结论；先恢复精确公开区间，再定点核该增量/对照与限制。
- [On the Ability of Transformers to Verify Plans](https://arxiv.org/abs/2603.19954v1)：测试时sequence与objectvocab同时长→C*-RASP条件规划verification→长度泛化成立条件而非一般ranking；先恢复精确公开区间，再定点核该增量/对照与限制。
- [PoC: Performance-oriented Context Compression for Large Language Models via Performance Prediction](https://arxiv.org/abs/2603.19733v1)：固定压缩比不能约束性能退步→performancefloor控制压缩强度+inputcompressibility预测→压缩controller选择；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Timestep-Aware Block Masking for Efficient Diffusion Model Inference](https://arxiv.org/abs/2603.19939v1)：diffusion整链mask优化高内存→逐timestep独立mask、敏感期loss与reuse→计算graph/训练代价取舍；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Enhancing Alignment for Unified Multimodal Models via Semantically-Grounded Supervision](https://arxiv.org/abs/2603.19807v1)：统一理解/生成监督granularity与冗余→groundedvisualhints+核心textalignedregion reconstructionloss→监督信号位置选择；先恢复精确公开区间，再定点核该增量/对照与限制。
- [All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution](https://arxiv.org/abs/2603.19595v1)：长期memory总结不可逆丢失→immutableevidence+confidencegatedtopology edits/visibleboundedretrieval/archivehops→成本与证据生命周期；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Unbiased Dynamic Multimodal Fusion](https://arxiv.org/abs/2603.19681v1)：动态modality质量权重双重惩罚难学模态→controlledcorruptionnoiseestimator+dropout依赖bias校正→quality-weight成立条件；先恢复精确公开区间，再定点核该增量/对照与限制。
- [From Plausibility to Verifiability: Risk-Controlled Generative OCR for Vision-Language Models](https://arxiv.org/abs/2603.19790v1)：OCRbenchmark平均精度掩罕见overgeneration→多structuredviews一致/稳定accept-abstain→coverage-risk控制评价；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Agentic Harness for Real-World Compilers](https://arxiv.org/abs/2603.20075v1)：普通软件bugbench可能不覆盖compiler→reproducibleLLVMbugs+specialtools/minimalharness对照→受限评价/工具feedback，不把60%当一般能力；先恢复精确公开区间，再定点核该增量/对照与限制。
- [ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents](https://arxiv.org/abs/2603.20340v1)：隐式skill状态/成功语义难修→explicitpre/post/step/recovery/termination artifact→deterministicverification与局部patch；先恢复精确公开区间，再定点核该增量/对照与限制。
- [WorldAgents: Can Foundation Image Models be Agents for 3D World Models?](https://arxiv.org/abs/2603.19708v1)：2Dfoundation+director/generator/verifier-curation静态3D重建；representation收益和筛选scaffold尚未分离，非actionconditioned dynamics；先恢复精确公开区间，再定点核该增量/对照与限制。
- [Beyond Single Tokens: Distilling Discrete Diffusion Models via Discrete MMD](https://arxiv.org/abs/2603.20155v1)：离散蒸馏collapse→discreteMMD保留quality/diversity但仍需足够steps→distillationsteps/分布损失成立条件，非一两步保证；先恢复精确公开区间，再定点核该增量/对照与限制。
- [GEM: A Native Graph-based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336v1)：single-vectorindex丢多vector semantics/nonmetric→set-levelgraph拆constructionmetric与relevancescore→导航召回/成本选择；先恢复精确公开区间，再定点核该增量/对照与限制。

19469额外中心冲突必须保留：作者窄读官方v1§4.2–4.4/§5起/§6，付款例认为task/action均1仍违反sourceauth；整体predicate却同时Ha=1且sourceauth写auth∨Ha=1，使该行恒真。需作者定义/例子澄清，不采用四性质形式保证；日期恢复不自动解除此证据限制。AutoMIA/WorldAgents/EvoJail准入决定事实含糊，不因模块组合自动排除，也不把27全称贡献通过。

**历史来源5组精确隔离。** H1 Google Pubs本窗foundation/训练/推理/多模态主题dated slice；H2 Meta Research相同窗口dated slice；H3 Seed Blog type2 total19但实际14/next空/has_morefalse缺5元数据；H4 MiMo本窗dated Blog切片及TTS原始身份/日期；H5 arXiv本窗主题announcement及delayed Submitted/重要revision历史切片。当前可见入口已按SOURCE到停止；恢复接受官方公开分页/原始metadata/明确历史日期目录，不以当前首页、空解析、错误route或Submitted库存替代。只重开对应source/身份/时段，不展开全年或全分类。

具名负侧：20313常规query-tool topK/局部ranking未新增召回或授权条件，root完整题摘关闭通过，无另追日期必要；Seed1337当窗蛋白-配体free-energy工具按明确AIforScience标题范围关闭，不声称完整题摘已审。其他标题范围样本与未核96条边界见SCREENING，不说124全贡献审阅。

窗外线索不阻塞本窗：AnthropicScience三文Mar23T23Z已归24窗口（本作者有限非作者core核另交24），MiMoPro/OmniMarch18、GoogleFlashLive/Manipulation26/Lyria25、QwenMaxPreview19/Omni30仅日期定位；不在23重审或重复记候选。

## 6. 复核

复核者：root（非作者）。
结论：通过

root实际完整读正式六部分、核14来源有限停止与原字段（SOURCE主体实际读；未变化尾部原值按已有实际证据复用）。首8完整v1题摘/history与日期原值校准有效；本轮实际当前Sora28–40及明确previous26–34对读，4分Only安全边界通过，19469§4.3.3/4.4付款例与predicate矛盾实际独立核。124标题≠28题摘≠1确定候选/27保留区分通过，five历史限制终态不算正面Coverage/Evidence；具名negative20313及Seed蛋白工具暂停范围、WorldAgents/EvoJail弱侧含糊保留已核，不授其余20题摘全量或27全文Evidence/Books。没有Books写入待POST，普通0。机器校验只认证格式，不代替本段语义验收。
