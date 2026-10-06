# 2025-10-20 本日筛选、查询与必要反侧

窗口为 BJT 10/19 09:00 至 10/20 09:00。只处理本日独立取得的线索，不继承其他 Daily 或 Weekly。

## 实际查询与停止

四组主题和实际 URL、提交检索带、页大小、返回数见 [FOCUS_FETCH](./FOCUS_FETCH.json) 与 [FETCH](./FETCH.json)。收窄三组为 22/44/20 项，系统 19 项；按当前精确 ID 去重 100 家族，完整题摘逐段读过。API 的 published 是提交日期；当前摘要也不代表历史 v1。初始宽组只保留原响应，未转成全文队列。

CL 官方月列表长年份路径恢复后，仅在 `2510.15000～2510.17100` 身份带浏览前 40 标题，止于 2510.15594；身份带用于限定查漏，不推定公开日期。不逐项关闭全月 2666 条，也未翻到第二页。对其中 12 个相关标题请求 [supplement.xml](./supplement.xml) 并实际读取完整题摘：15007、15103、15231、15244、15312、15346、15421、15455、15501、15517、15522、15545。实际请求为 `https://export.arxiv.org/api/query?id_list=2510.15007,2510.15103,2510.15231,2510.15244,2510.15312,2510.15346,2510.15421,2510.15455,2510.15501,2510.15517,2510.15522,2510.15545&max_results=12`。其他标题并未成为题摘/全文待办。

共 112 份当前完整题摘用于初筛，不称当日新论文或历史 v1 审阅。另有原宽查询发现的 MCP 安全论文 2510.16558 和 Google 官方相册文章的定点核心。没有确定落窗候选，不评分。

实际辅助搜索均首屏停止：

- `site:openai.com "October 19, 2025" research`；`site:anthropic.com "Oct 19, 2025" research`；`site:arxiv.org "19 Oct 2025" "language"`。
- `site:arxiv.org/list/cs.CL "Mon, 20 Oct 2025"`；`site:openai.com/index/ "October 19, 2025" -site:community.openai.com`；`site:research.google/pubs "2025" "October 19"`。
- `("2025-10-19" OR "October 19, 2025") (site:deepmind.google OR site:research.google/pubs OR site:ai.meta.com) ("model" OR "training")`。
- `("2025-10-19" OR "2025年10月19日") (site:qwen.ai OR site:deepseek.com OR site:platform.kimi.com) research`。
- `("2025-10-19" OR "2025年10月19日") (site:hunyuan.tencent.com OR site:zhipuai.cn OR site:seed.bytedance.com) model`。
- `("2025-10-19" OR "2025年10月19日") (site:ernie.baidu.com OR site:mimo.xiaomi.com OR site:minimax.io OR site:agent.minimax.io) model`。

无相关搜索命中不等于源内零事件。Google ICCV 会期标签不证明具体论文首次公开；社区帖子、转载和错误域结果不作原始证据。

Google 后补实际打开 [十月 Blog 月页](https://research.google/blog/2025/10/)：第 1 页相邻日期 10/20 与 10/17，停止页 1，未翻含更早条目的页 2；Google pubs 保持独立历史缺口，不由 Blog 替代。网络下载月页超时，网页工具确实返回正文，未制造成功本地原件。10/20 两条中，恒星识别为 AI for Science 暂缓；[相册原文](https://research.google/blog/a-pictures-worth-a-thousand-private-words-hierarchical-generation-of-coherent-synthetic-photo-albums/)的 How/Why 与 Evaluation 核心已读。双模型先生成相册摘要再生成照片描述，YFCC100M 以同用户同小时成组，并限制每用户每训练集一个样本。它存在具体结构/隐私机制潜力，但仅 Oct20 日期标签，时区/时刻未核实；图中非 DP 演示不能作 DP 证明，文本有损不等于 DP 保证。继续日期隔离。

## 潜力而非确定候选

[首批校准包](./FIRST_CALIBRATION.md)的六项已由 root 非作者完成贡献与精确 v1 校准，见 [FIRST 独立复核](./FIRST_INDEPENDENT_REVIEW.md)，不是 DAY 通过。More with Less 与 VisualAR 均已核 v1，不能继续表述为只有当前 v2；VisualAR 原件为 ROOT-2510.16751v1.html。以下保存定点重开依据，不使用成熟原则凑分，也不授 Books 采用。每个家族只请求一次日期恢复：须取得官方首次公开公告/历史事件列表，或由真实首公开原件限定且完全落窗的 bounds；当前 submission、后来的 ID/注册时间或日名相交均不足够。修订版本还须确认本窗实际变化，不以版本号推定重要修订。

| 家族 | 原文具体潜力与待核选择 |
| --- | --- |
| 17015 Justitia；16996 STARK；16946 host telemetry；16933 CUDA tutoring | 分别是内存成本公平调度、带 profiler 的 kernel 搜索、主机侧 GPU 诊断、优化提示/反馈；须核归因和开销，不借一般调度/观测价值评分 |
| 16606 Celeris；16415 MeCeFO；16418 FourierCompress | 放松 RDMA 重传/顺序、接管时近似更新、按层频谱压缩；分别改变传输、失败恢复和协同推理质量契约 |
| 16883 JAX；15596 PRISM；15652 GOGH；15330 BeLLMan | 线性逻辑下 autodiff、概率运行时模型、相关性分配 GPU、输出长度反馈拥塞；理论/系统贡献保留而非因不是大模型算法排除 |
| 17896 attention benchmark；16809 many-shot translation；15494 real-code optimization | kernel 与分布式上下文并行评价；few/many-shot 失败差别；真实 Java 性能与算法题收益差别。负面/评价证据保留，不先认定全部已有覆盖 |
| 17885 efficiency metrics；15700 ProofOptimizer；2511.07424 incidents；2511.07423 Synera | 匹配准确率的多硬件碳/能耗 Pareto；验证器训练简化证明；实际事故失败模式；端云 speculative serving。后两 ID 为 11 月而提交字段为 10 月，尤其不能自动划入本窗 |
| 17021 backdoor；16968 expert signatures；16716 DistilLock；15731 diffusion sinks | unlearning 攻击的触发位置/值范数、MoE 路由指纹、TEE 保护的排列机制、扩散 sink 动态；安全反侧见下文 |
| 21788 online MoE；16448 input-domain MoE；16411 expert graph；16138 Nash merging | 在线 no-regret 条件、路由与任务目标解耦、专家交互图、合并谈判；须核真实假设，非以“MoE”同主题计贡献 |
| 16552 LANPO；16096 Facts in Stats；15516 KD dataset size；15349 Infinity Parser；16455 RAVEN | 语言探索/数值优化；语境结构/多样性/训练时长；蒸馏与标签平滑的样本规模边界；阅读顺序奖励；粗精标注课程和分层定位奖励。后者不是因广告场景自动排除，也未将在线 A/B 宣称作已验证 |
| 16983 Bregman diffusion；16888 Uniworld；16751 visual AR；16729 residual world model；16617 MoS-VLA | 单步密度比目标、隐式负反馈、搜索早剪枝/复用、残差环境预测、一次技能基组合；核各自控制变量与适用任务后才可采用 |
| 21783 noise MIA；16332 TokenAR；15761 QSilk；15530 VO-DP；15510 ORCA | 小噪声聚合攻击、主体 token 分离、区域分位裁剪、语义几何条件、控制条件失效/适配。QSilk 仅定性也不自动排除，但收益及开销未验证 |
| 15446 VDRive；15392 LILAC；15301 no-VAE diffusion；15264 DriveGen3D；21769 H2OFlow | 奖励 VLA/扩散控制、因果流式 motion、非 VAE latent、前馈驾驶场景、3D affordance；不可由模型名称泛化为已建立闭环 world state |
| 16978 Lark；16907 VAGEN；16872 DeepAnalyze；16786 More with Less；16769 GraphVista | 利益相关者演化、自估状态/转移和 turn GAE、训练课程、按需回合延期、图的模态选择；任务依赖局部证据可有贡献 |
| 18893 CodeCRDT；16635 MA-SAPO；16572 Ripple；16392 RGMem；19838 Branch-and-Browse | 文本收敛不等语义一致、分数反馈优化、协调敏感性、快事实/慢归纳、状态重放与行动记忆；保留负面/代价，不以成熟组件组合解释全部收益 |
| 16276 SpecCache；16156 AsyncVoice；15862 deep research RL；16079 EvolveR；15416 LoRA tools；15414 MARSHAL | 推测网页状态缓存、推理/讲述并行与打断、RLOO/GRPO 对照、经验原则自蒸馏、调用适配器、分回合自博弈优势 |
| 17874 tool repair；15283 exemplar KGQA；15261 AUGUSTUS；15259 SAG | 错误结果之后检索修复、模板及前瞻、用户多模态记忆、战略游戏经验图。必须核实际新增，不把 state/control 术语本身当贡献 |
| 2512.00016 hardware agents；16701 AFL；16645 DiMo；15568 Spark | 层次拆解工程师干预、四角色交叉约束、类型化证据链、角色多样性及 judge 偏差；准入的具体约束机制/评价差额仍有限，不授成熟流程组合新增理论地位 |
| 16381 ATA；16255 auditing；16219 SentinelNet；16558 MCP security | 安全命题的必要核心已定点读；日期不明不掩盖其范围限制，见下文 |
| 补检 15007、15103、15231、15244 | 多标签安全评价；稀疏 memory slot 更新；仅音频位置扩展/VLAT；DDLM 到 ARM latent projector。当前不同版本不能覆盖历史版本 |
| 补检 15312、15346、15421、15455 | NPU graph loading 与 chunked prefill 并行；tokenizer/共识位置选择；主动获取证据与误停；按 XML block 减少上传。收益不是一般并行/隐私原则的分数 |
| 补检 15501、15517、15522、15545 | 诱导欺骗评价；BPE 分层动态 patch；vocab-space latent chain；DTW 跨词表 speculative alignment。后者不因摘要自称 universal 就得到无偏分布保证 |

## 明确排除及抽检分层

已实际读题摘的范围/贡献关闭项：BRAINCELL 17064、ReclAIm 17004、LANO 16816、Class-N-Diff 16887、PET 15556、MRI 15400、PHI 16194、MedBuild 2511.11587、Guide-RAG 15782、MoPHES 16085、BIOGEN 16082、SQuAI 15682、TriAgent 16080、MedGemma 15418：科学/临床领域应用，题摘没有在当前主线新增模型或系统机制；不得借通用 Data/RAG/Evaluation 节点绕过暂缓范围。

TACLA 17913 是教育 TA 训练角色应用；SCALAR 16474 是一般预测表示；Attn-JGNN 15583 是 #SAT 专用 join graph；BPL 16076 是推荐偏差；GraphMoE 15333 是 GNN 对抗防御；LightsOut 15868 是镜头眩光处理。以上题摘未建立当前大模型机制链。

RL survey 16724、Beyond Pipelines 16720、world-model survey 16732：题摘是分类/趋势汇总，未提出新的反证/边界，不能仅靠主题归属准入。RTBR 16206 为人的数字记忆权规范，不是 Agent 记忆更新机制；Multi-dimensional 15258 是商品知识图工作流组合，未有具体设计差额；TDD 15585 明确 position/research framework，尚待实验，不借成熟 test-first 原则收录。

**撤回排除：L-MoE 2510.17898v2。** [当前官方 API](./focus_model_training.xml) comment 指 Sec3.2 可微路由数学公式存在技术错误，撤回以更正公式及重新评价证明。该版本不准入、不评分、不进入 Books。不是访问失败，也不以当前摘要宣称的性能/理论作正面证据。

root 已核撤回 v2 日期为 2026/01/07，不是本日发生的撤回。当前已知撤回阻止采用，不能移动撤回事件归属。

### CodeCRDT 必要反侧补读

作者实际读 [2510.18893v1](./2510.18893v1.html) §4.3、§5.2、§6.2/6.3、§7.2、Appendix B.1 后停止。Yjs 的强最终一致保证相同文本收敛；语义重复声明、类型和引用问题另由 evaluator 处理。语义冲突仅人工检查60/600，正文同时给出约5～10%及简单/复杂任务20%/80%，这些口径不能组成可靠全量冲突率。

六个 TypeScript/React 任务、每模式50次，Claude Sonnet4.5/Bedrock，120s timeout、最多5并行作者；质量为同模型 rubric，无人类验证或 runtime 功能证明。总体端到端慢13.1%，任务由快21.1%到慢39.4%；最长代码膨胀82～189%同时伴随减速。按字符归一化5/6更快不等于固定需求端到端更快，也未因果隔离全部协调开销。超5 agent扩展表为推测，不是测量。该补读不授日期、评分、Evidence 完成或 Books。

作者又实读§5.3/5.4（671～691）及A.5（1169～1217）：response time排除83/600 IQR outlier，仍有网络/生成/协调混杂；没有human baseline，也未比较CRDT与OT/log/locking的优劣。A.5 claim-write后固定50ms wait，再read winner；证明explicit依赖verify时post-convergence。任意延迟/分区下不同replica可能尚未收敛，固定50ms本身不保证单次执行互斥。strong eventual consistency不替代执行权限、安全或语义任务完成；不展开其他附件。

root FINAL原范围通过但要求窄同步后回核，见FINAL_INDEPENDENT_REVIEW。四条后续目录日期仅实际归属待核的路由线索，不称全网first-public确定窗外；FIRST六v1旧停点已同步。

排除共 26 个题摘家族加 1 个撤回家族；余项为日期/版本及准入校准保留，不当确定候选或终审。非作者须全核安全/反侧及撤回，其余按领域应用、专用非主线机制、综述/位置论文三层抽检；首包六样本只是校准样本，不宣称全量验证。

## 必要安全/反侧核心的实际边界

- [ATA v1](./2510.16381v1.html)：已读方法入口及 §4.5 Security/§4.7 Fairness。immutable 人工规则 KB 与形式证明器只隔离规则逻辑；NER/关系抽取仍可受虚假事实输入影响，作者承认事实操纵及抽取偏差未解决。不能把此架构称全链 prompt-injection immunity 或事实真实保证。云 Gemini demo 不证明全程本地隐私。
- [DistilLock v1](./2510.16716v1.html)：已读 threat model 与排列/TEE 入口、Appendix C 配置。TEE 不可攻破是明确前提；外部 GPU 参数可见与小模型蒸馏攻击不代表所有攻击。SGX/A100、Alpaca、三 seed 设置仅核身份，未完成全部攻击/成本对照审阅。
- [Auditing v1](./2510.16255v1.html)：§3 Methods 的 D/S/M/P/B/B* 工具，递归数据检索、baseline/post 模型查询、攻击定点 elicitation；低 FPR 下仍漏检，良性微调的偶然退化可混淆。不能把摘要 detection rate 外推部署保证，未完成全部实验审阅。
- [Unlearning backdoor v1](./2510.17021v1.html)：§3 white-box 训练管线，触发样本被纳入 retain 目标；§4/5 位置与值范数机制；§8 限制是小规模开放权重、固定位置文本触发、MUSE/WMDP。证明局部审计盲区的潜力，不证明任意遗忘方法可被攻破。
- [SentinelNet v1](./2510.16219v1.html)：§3.2 观察所有通信但不能改节点内部状态；§4 对比 credit/bottom-k；§6 模拟攻击、平方级 agent 开销、监督标签依赖、恶意多数超出作者典型假设。作者对自适应攻击的讨论不是已验证通用防御保证。
- [MCP v1](./2510.16558v1.html)：§2.2 host 更新/确认界面，§3.1 假设连接安全，攻击位于 registry 与集成后 server 元数据；§3.2 四 host、三个模型（Claude Desktop 例外）、每对五次；§6.2 列表陈旧与删除账户链。原文以 GitHub API 404 推定可重注册，404 本身不足证明名字可注册，212 不作为实际劫持成功数；未检查/复现第三方服务漏洞。定点原文仅用于保留边界，不扩扫 weekly MCP release。
- [Toxicity v1](./2510.15007v1.html)：§2/3 单标签遗漏多种毒性导致漏报/误罚；val/test 多标签十人多数标注，训练保持部分标签。评价协议差额有潜力；未采用伪标签普遍优越的理论，不能由 PCA 重叠证明全部标签语义。
- [DeceptionBench v1](./2510.15501v1.html)：§2.3/2.4 人工检查的诱导场景、GPT-4o 标记 thought/response，L3 是多轮 prompt 诱导而非训练时 RL；§4 风险结论限这些提示与 evaluator。文字 thought 不等真实内部心理状态，不能把场景 deception rate 变成部署欺骗概率。
- [CORE v1](./2510.15455v1.html)：§2 目标是减少上传 UI 元素并容忍决策偏差，§3 block/local-cloud 分工；cardinality exposure reduction 不是差分隐私或所有敏感元素不上传。未声明本地完全隔离/正式隐私保证。
- [GuessBench v1](./2510.15421v1.html)：§5.1 passive 对照直接给完整 target description，§5.3 通过 QA filter 缩候选池并离线重算 single-candidate 提前停止；改善可能依赖该过滤器和终止协议，不能泛化为随意缩 reasoning budget。主动/被动信息条件差别已保留。

上述十份 v1 只完成影响筛选/保证范围的必要定点阅读，**不是十份标准/深入候选审阅完成**。没有复现实验、核验代码或正面采用。原件存在不证明作者读完所有章节；日期未恢复前不进入 Books。

## 来源定点纠正（2026-10-05T05:08:33+08:00）

Seed 自身 seed-main.js 的参数为 article_type，论文请求加 x-tt-locale: US。此前 type=1/2 是错误请求，不能证明目录故障或有效论文/Blog覆盖。实际正确请求与原响应见 seed_papers_locale_p0.json、seed_blog_p0.json，均 publish_year=2025,count=20,order_desc=true,page_token=0。论文18条（total94,next20,has_more=true），非置顶日期已跨目标时段至10/09；Blog18条（total45,next20,has_more=true），10/23 Seed3D后跨至09/09。只处理该窗口切片，不遍历全部年度库存。量子嵌入是科学应用且当前时间字段在本窗后；Seed3D为本窗后路由，不把simulation-ready资产直接称动态World Model。原错误请求保留，不作日期准入。

Z.ai 自身 zai-research.js 的 LoadMore 通过 URL page 参数导航；实际 zai_page2.raw 累积18条，最早12/07，nextPage=3/hasMore=false。已读末页日期与标题，普通恢复消除，仍有真实历史缺段。DeepSeek实际 deepseek_news.raw 独立研究索引十条，相邻10/21 OCR和05/14，只停止目标切片，不用首页模型导航代替Research。
