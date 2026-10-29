# 2025-10-28补窗：有限发现、贡献与停止

窗口仅BJT2025-10-27自然日，旧小时窗/旧候选整行/有效连续§4保留。原`SCREENING.md`仍只代表其实际旧窗范围，本记录补差而不覆盖原件；不catchup、不用其他日报池。运行时请求/时区在各request.json，不按运行日移动事件。

## 入口与日期层

1. 七个主题的实际title/description同义查询见`repair_fetch_20261029.py`：language/foundation model，Transformer/attention/MoE/state-space，训练/后训练/RL/蒸馏/量化，GPU kernel/serving/parallel/KV，language/AI agent/tool/RAG，多模态/VLM/worldmodel/VLA，diffusion/flow/AR/video generation。主题命中只作线索，医学/材料/经典推荐/一般控制等不随关键词自动扩Methods。
2. DataCite V2使用独立`client-id=arxiv.content`过滤，registered与created分别查询UTC`2025-10-26T16:00:00Z`到`2025-10-27T15:59:59.999Z`。各实际140（100+40尾）、64、58、1、16、56、31；language沿真实next到第二页末，其余均total==本页且无next即止。两种日期各366条含跨主题重复、各251唯一DOI，身份集合相同，**registered相对created差额0不是零论文**。初次错误`client.client-id`字段返回零保原件但不授发现层；不能拿submitted或created片替注册公开上界。
3. 适用2025发号/公告规则、精确唯一v1、同DOI/arxiv.content/findable/registered共同复算251中233区间完整落BJT Oct27，18跨日。原字段/上下界在`REPAIR_DATE_BOUNDS_20261029.json`，机械脚本不代贡献或globalfirst。18不全量追日期：明确范围/贡献关闭者停止，8有潜力具名恢复见earlier-public记录。CGoT控制最早Oct28，registered亦Oct28，不当补窗候选；不重读其未必必要方法。
4. 原cs.CL月首50只作旧有限标题补检，新`REPAIR_ARXIV_OFFICIAL_NAV`只核官方月目录真实分页（按ID顺序、无日级公告字段），不把它称Oct27批或据ID判断。官方advanced实际声明announcement仅年/月精度，精确日请求返回表单错误非零；不扩大成全月2666篇。七主题窗口查询与实际具体线索在此停止，不追全类/互联网无遗漏。

## 贡献分层与互斥首必要

首五项与代表排除先W3/R4校准；writer必要层见`REPAIR_EVIDENCE`，sole22与20有限线索首必要见R9–12/R18–19。首必要分工互斥，支持/直接反侧足即停，无第二人全附件或全部代码复现。评分是新增命题，不按访问/Books/工时反推。当前已成49整合/19新增已有覆盖及4仅报告的证据层继续复用；后到W26/W27的25+writer21060仍按具体贡献继续，不因这组处理完成声称全日验收。

### 原首批代表关闭

- 2510.21413：AGENTS.md采用/格式描述性统计，无格式到质量因果或新执行机制。
- 2510.21566：ColorEcosystem蓝图/部分实现，未给新执行/信任机制及可比较成立边界。
- 2510.21219：physical/social worldmodel概念倡议，未给改变具体模型选择的可检验机制。
- 2510.21649：Gompertz-CNN局部常规蒸馏损失调权，未给当前基础模型系统的稳定新机制/条件，非因小模型排除。
- 2510.21697：既有visual diffusion用于几何题图像解，题摘未给新通用生成机制或符号替代条件，非数学领域本身排除。

### Reader必要后关闭

21133 CBRN snapshot、21214 EnhancedMLLM attack、21553 category/RLVR forthcoming、21638 DEEDEE的具体安全/含糊必要均已R10–12完成；21356 GazeVLM、21398 RL budgetforcing、21418 DreamerXP已R18完成。分别保快照非新测量机制、既有攻击组合/额外query union、未实现RLVR桥、经典sensor OOD无foundation/VLA直接桥、既有privileged gaze KL+CE、既有GRPO/length/budgetforcing组合、已有rewardhead ensemble+replay启发未识别新通用条件。均不评分、不Books，不以安全/小模型词强收或倒降分；源和直接反侧不删。

### 后到有限标题/完整题摘关闭

以下是本日同251内具体含糊线索的完整题摘实际读取，不是对整类逐项Methods；编号均2510。未列标题明确领域应用只作范围筛，不声称全文排除。三条R32新关闭由sole独占，未在此抢其Methods。

| 身份 | 实际新增与关闭理由 |
| --- | --- |
| 21031 AgentArcEval | Agent架构scenario catalogue/税务copilot案例，未给新的可检验执行或评价成立条件，不因agent主题强收。 |
| 21114 Controllable-LPMoE | 冻结视觉主干加异构卷积local priors/MoE gating/deformable adapter的segmentation实现，题摘未给超出组合的通用融合条件。 |
| 21148 EGO-Prompt | 专家SCG与textual-gradient的领域任务迭代，未识别真实因果graph或新的通用优化成立条件。 |
| 21207 ADaMoRE | 初始“未写foundation桥”理由不足，sole R40具名重开、R42已读exact-v1决定性结构/理论后关闭：sparse hop backbone+dense residual experts、MAE/loadloss/CKA与cross-filter是既有局部组合；Rademacher upperbound不能推出naive-MoE lowerbound，输入依赖gating非固定convexhull，小target residual也不强制可训练类小norm。未得到可采用的新一般sample-complexity/stability条件，不采该宣传或补loss方向；不把本次核出的数学警告冒充作者新贡献。 |
| 21210 flow interpretability | 将2D Ising equilibrium作为物理生成目标/解释载体，暂缓science应用；无独立于该物理任务的通用新flow机制/保证。 |
| 21244 VoiceAgentEval | outbound业务场景/过程分数与LLM persona模拟，题摘未给一般测量新机制或真实性验证，更多类别不够。 |
| 21254 OOD safety review | 技术综述/生命周期建议，未明确新的可检验OOD机制/安全成立条件；R31独核抽样同意。 |
| 21306 PARL | state/action/reward放prompt的无微调简单RL应用，未给新记忆/交互学习机制，局部与传统agent胜负不足。 |
| 21341 Magellan | MCTS/embedding semantic compass/novelty-coherence打分的科学idea搜索，题摘没有可采用的新latent控制成立条件；不扩science应用。 |
| 21363 FairImagen | 既有FairPCA作用于CLIP prompt再加noise/交叉人群组合，未给新通用保证；保画质/语义取舍，不沿用内容保持/任意公平。 |
| 21372 HalleluBERT | Hebrew RoBERTa训练/语料与语言专用BPE发布，未给新通用表示/训练/系统机制，非因语种小排。 |
| 21406 MUVR | 长视频多层匹配类别及新benchmark，题摘尚未识别影响一般检索/重排选择的新测量成立条件，未把规模/类别数当机制。 |
| 21425 symbolic integration | 已有NeSy/LLM文献taxonomy与roadmap，未给新的具体可验证symbolic执行机制。 |
| 21436 AutoOpt | MER→LaTex→Pyomo→领域优化器pipeline，模型与solver拼接未给当前foundation系统新接口/成立边界。 |
| 21520 brain tuning | 多人fMRI目标调speech模型以改善brain alignment，当前为暂缓神经科学应用，未给独立通用训练机制。 |
| 21561 language genus | 语言亲缘/资源量与model差异的局部相关，未识别训练资源因果或新语言系统条件。 |
| 21604 RETuning | stock任务的组织/反思证据CoT冷启动，题摘未超出既有流程给新通用训练/推理机制，不采用价格预测保证。 |
| 21605 S3OD | 迭代合成难例、DINO/diffusion伪标与多mask decoder的局部saliency组合，未给新的通用歧义/标注成立条件。 |
| 21623 IF-Track | LLM作probabilistic encoder用于统一人类心理推理测量，未建立其entropy为真信息或改变当前model形成的机制，不扩神经科学支线。 |
| 21635 DAP-MAE | point-cloud domain adapter/generator在pretrain适配与finetune融合的任务组合，未给一般迁移条件的新证据。 |
| 21656 CMOMgen | RAG+ICL选择ontology类/示范的生医任务应用，未建立通用semantically-sound guarantee或新机制。 |
| 21659 SRS | complex-STFT/phase-aware loss的紧凑vocal restoration，本件未给当前foundation体系的直接新机制；移动RTF不自动迁LLM。 |
| 21685 StylePitcher | 既有rectified flow加reference style/score/pitch条件的歌声任务应用，未给新通用flow/控制边界。 |
| 21693 TSP SAE | 已有SAE用于pointer TSP的可解释feature应用，未给新字典/因果干预机制或通用solver资格。 |
| 20926 FicSim | 文学12轴语义相似数据集/局部embedding评测，未给超出领域指标的通用测量条件。 |
| 20941 overruling | 法律长文/历史case失败快照，训练时偏差与shallow理解为未识别解释，不当新因果机制或法律保证。 |
| 20985 memory predictor | BiGRU/Transformer预测显存优于树模型，未给tensor生命周期/allocator/目标硬件映射新机制，不以调度应用名强收。 |
| 21192 GenReview | prompt正负/中性评论数据集与检测/评分相关，未给一般审稿/评测新执行边界或能力形成机制。 |
| 21242 BLOGER | 推荐任务的既有bilevel/meta/gradient-surgery组合，未给超出item应用的新tokenizer成立条件。 |
| 21299 generative communication | JSCC低码率表示+文字+SD/ControlNet恢复的局部组合，无新通用channel/生成保证，不把plausible当真实faithfulness。 |

18跨日中的20835/20838/20849/20850/20853/20855/20859/20884完整题摘关闭理由见W26；20829物理memristor、20868金融graph预测标题已明确不在本轮主线，无具体安全/纠错新信号，不追日期。剩余8具名潜力不按Submitted/created直接归日；VAP已由官方Oct24 report发布排窗，7精确外部日期保留见`REPAIR_EARLIER_PUBLIC`。

后到25的sole R32/R34已成关闭层整体消费，不第二Methods：21329旅行扰动benchmark、21408人脑关联学习model-organism、21460 NIST目录/未验证risk总分在完整题摘停止；21069 ZING-3D、21107 ESCORT、21427 GSAC、21585 REVE、21401 FLAMES实际必要后关闭。前四分别为未新增冲突/identity维护的VLM+depth图组合、known POMDP手工state粒子、known factorized graph MARL且既有局部Q界、EEG特定Fourier4D/MAE组合，原数学/领域价值不否定，当前主线新机制/直接桥不足。FLAMES的FIM-SFT补require是局部适配，必要安全反侧明确编译/语义等价/功能tests/真实防御不同，强guard可误拒、漏合取可放危险；22/108不授production-ready/无人介入。均不评分/Books，不因后到/工时改判。

21110精确同家族官方OpenReview正文与作者检索Published18Sept2025/ReadersEveryone由sole R35实际恢复，窗外不评分/Books，不启动九月。后到其余11件已R36–38完成必要支持/直接反侧，R39实际Books比较为两具体已有覆盖/九真实gap；不二Methods，完整PRE/SAVE/自读/POST与六节DAY仍普通工作。

后到五具名OR日门20903/20994/21267/21311/21542经R41逐件两代API403/forum challenge及限定primary搜索后，分别收口为外部日期保留项；不是尚未读完的Methods改H，也不是贡献关闭。加七跨日/两原OR共14精确家族，不进确定池/评分/正面Books，不授Coverage或零论文。精确forum和重开条件在earlier-public及R41，21110不混作未知。

分层抽检实际范围由sole R40/R42保存：本表30条按主题/理由抽12完整题摘，21207一项必要后修理由；另21254既成R31复用，合计实际独核13/30、未独核17。原五代表、七项reader必要关闭、安全R31其他两项与后到八关闭各复用已成层；不称全部251题摘/全部排除或附件全量独核。未发现共同错误需扩成全表Methods，具名理论判断修正后停止。

## 机构与停止权限

十四每日行的既成有效入口/原始请求、邻接及失败复用旧SCREENING，不按当前页面静默补历史。只补实际缺层：

- Hunyuan：官网research共Blog路由、bundle请求header zh、renderType0=All；本日中文page1/size100实际code0/total11/list11且全部lang zh。全部条目2026只证当前可见集，不授2025零或用其他日数字/英文9。2025日级缺段保持外部隔离。
- Google：本日2025/language model年度导航15/15/7，静态href为JS占位但data-page/form/max-pages真实为3，第三页next4/last3disabled停止。37是本日本次年/主题线索，不是37当日论文或全Methods。没有具体Oct27新正文线索，日级first缺额隔离，HTTP200不等Coverage通过。
- M2：同Blog Oct27事件与Oct27 GitHub精确README历史commit已到；历史think输入合同有效，不用currentcard倒授。算法后续披露、top_k20/40不同原样保，4分兼容性深入/仅报告。
- OpenAI旧候选/有效连续§4、原其余机构的有限停止、Google coach与Steuerrecht等无通用增量的应用关闭均复用，不再次Methods；旧完成标签不代本轮DAY。
- 按需OpenReview只跟具体同家族早稿/理论信号，CVF/ISCA只跟PLAN/SpecTokenizer，DataCite/官方文档只作发现/日门组合；不扫描会议全集、每周源或其他日期Daily/Weekly/2026。

本记录不授整日完成。后到必要、Books及六节README的实际DAY/SAVE/FINAL须继续，普通工作不能改成外部H；真正日门外部保留项只按具名条件重开，不用它们宣布无遗漏。
