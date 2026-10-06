# 第二十一包：AB12 五项必要原源与具体 owner（待非作者 PRE）

只继续已校准的具名潜力；作者实际必要阅读范围如下，不把下载或发现摘要算审阅。本包尚未获 root PRE、Books lease 或 POST，不增加 35 safe。当前无本代理持有的 Books 写锁；拟整合也可经具体 owner 审阅改为 Existing，不因论文名字造缺口。未核 artifact、未复现，不遍历全部 proof 或默认 revision diff。

## 身份和日期

精确 v1 完整题摘及 current Comments 已读，未见影响本包命题的具体撤回/纠错标记。当前后续版本不默认比较。官方公告规则提供本批公开下界；same-ID DataCite registered 秒精度加一秒提供登记身份上界，不能替代技术 primary 或家族早公开检查。以下 UTC 原值均 Submitted 02/26、registered 02/27；来源为 `V3_ABS_2602.<ID>.txt` 与已有身份库存；原下界规则复用本轮已核记录。

| ID | Submitted UTC | registered UTC | arXiv 事件区间 02/27 +08 |
| --- | --- | --- | --- |
| 23229 | 17:08:18 | 03:05:43 | 09:00～11:05:44 |
| 23235 | 17:12:40 | 03:05:52 | 09:00～11:05:53 |
| 23248 | 17:25:22 | 03:06:12 | 09:00～11:06:13 |
| 23259 | 17:32:30 | 03:06:29 | 09:00～11:06:30 |
| 23266 | 17:39:56 | 03:06:39 | 09:00～11:06:40 |

## 23229 Open/Closed ICL classification：拟 2+1+3=6，Ch23 分类消费者一段

[精确 v1](https://arxiv.org/html/2602.23229v1) blocks31–45/53–65/67–71/73–85/151–154 实际读；未称完整读过 giant Table2 全部行。旧 zero-shot encoder 语义可用并不保证新增图文 demonstrations 有益：同一 support 池下，CLIP retrieval 选择近邻给 LMM，并与 kNN majority/Tip-Adapter、zero-shot 对照，闭类与开放类无标签上下文污染有不同退步条件。CIRCLE 是对同一批未标注图像 leave-one-out 生成 pseudo-label 后同步迭代，不是新标签真值来源或可部署的独立认证；naive ICL 能低于 zero-shot，改进只在受测协议成立。

candidate label list 改变 bCS 概念指标的奖励人口，mCS 中位汇总也不是完整 gold faithfulness。固定输出模板会影响 LI；append “one of these...” 是评价接口变化，不能把该收益当纯视觉提升。原“所有指标更好”不采用：已显示 Table2 的 Qwen2.5 very-fine SS 为36.4，zero-shot45.8。CLIP检索、kNN 与生成 consumer 成本和 inductive bias 不匹配，不能据此宣告通用表示优劣；伪标签同源错误可以被反复加强。

greedy/64 max tokens、224²输入，batch32按GPU容量退到8/4/2；A10040/64/80GB至多4卡。streaming随机历史 m16，Food/SUN的大集合处理8～10小时，不授在线 SLO/独立迭代质量保证；encoding、retrieval、额外 generation 与上下文预算计费。

actual `MULTIMODAL-REPRESENTATION` Ch23 59–93完整相关段已读：85–87可读/可访问/可表达，89全局分类≠dense grounding，91已有粗细分类头竞争与目标/非目标分验。本次窄差额是 **不用更新权重的分类 consumer，闭/开放标签域下 support 选择与 pseudo-label 上下文污染须单独验收**，不是重复“模型有信息但答错”。拟分类 readout 附近一段，绑定相同 support/输出解析/标签域，保 zero-shot、专用 head 与真实监督回退；若现有消费者分责足够，则具体 Existing 有效。

### 23229 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks31–45、53–85、151–154：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+1+3=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：永久mixed-granularity/dense head已有，但没有同支持人口CWC和leave-one-out同步OWC派生标签更新的接口，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。label judge模板/集合偏差、random/初始pseudo ICL伤zero-shot及迭代非全胜、检索/编码/轮次预算和真实标注回退近文。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 23235 GUIPruner：拟 2+1+3=6，Ch23 token-pruning 一段

[v1](https://arxiv.org/html/2602.23235v1) blocks19–58/60–95/117–127/165–166 必要机制、Table3/4/训练配置与反侧已读。历史画面先按年龄进行像素 resize，当前画面浅层 token 按 fg/bg 重要性选择并保留 uniform grid residual；两处预算/表示变化不能归成单一 token selector。实际消融比较 uniform/decay 分配和 grid/random residual；新差额是先改 history encoder 输入，再保 current 网格辅助关系恢复的接口，而非“旧画面少留、重要patch多留”成熟原则。

TAR 总历史预算写为 floor(T*Norig*lambda)，仍随 T 增长，不采用历史长度无关 memory 保证；T=1、整数resize与patch取整需要实现规则，未把伪码升级为严格预算证书。mu 选择 fg/bg 的 top fraction，不保所有 salient cue，也非完整二维信息无损。layer1性能崩至12.4且FLOPs3.79高于layer2的65.3/3.39，作者归因冗长生成，不唯一证明早层未编码语义；无剪枝质量多数更高，细粒度/历史稀有证据会丢失。

两任务模型的 LoRA/SFT：r8/alpha16、两epoch、4A10080/ZeRO2/FlashAttention/bf16；分模型学习率3e-5/5e-4/3e-5/3e-4。RTX4090单卡 eval、4帧历史，AITW lambda=.1/mu=.75的 encoder87.9→26.6ms、prefill47.5→24.1ms，不是全服务 decode SLO 或训练seed不确定性。历史resize、selectors、grid恢复、额外微调和输出长度成本都保留。

actual Ch23 476–510和574–594完整邻接已读，已有 oracle/rank、selector成本、深度/网格身份、跨模态预算和3D剪枝风险；未把本分支的 **history pixel-resize与current residual-grid两处预算职责、T增长/浅层失效条件**明确放在同一链。拟该小节一窄段，保dense/uniform高预算与近期完整历史回退；不能写 generic pruning 的又一榜单或“无损压缩”。

### 23235 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks19–95、117–127、165–166：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+1+3=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：层位置/合并/grid恢复与模态预算已有，但没有历史resize和当前前景/背景/残余grid两级分工，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。历史quota随T增长、T=1/rounding、layer1 StepSR12.4 vs layer2 65.3、完整输入反侧和4090编码/prefill非全流程SLO近文。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 23248 DPVG：拟 2+2+2=6，Ch33 verifier-policy 之后一段

[v1](https://arxiv.org/html/2602.23248v1) blocks9–40/42–54/83–89实际必要阅读。固定 solver 的答案生产能力，再训练 faithful/sneaky translator与 verifier，将“修改解题器”和“修改可检查呈现”拆开；sneaky 分支拿到 ground-truth y，原 faithful criterion只检查最终答案一致，不认证推理语义等价。理想 equilibrium 依赖 verifier loss最小当且仅当v=c等假设，本次未核完整proof，不采用有限 RL 已实现普遍 soundness。

RLOO role-conditioned reward 会按固定 solver 正误翻转 normalized verifier logit，错role/低于组均值另扣；score std=0 要数值规则，不据此断言实际artifact有bug。8Ktranslator/8Kverifier样本，每条16个离线solver输出，test1024；faithful99.8%、solver57.0%/translation56.9%仅受测回答一致与结果，不授人类可读性。未测 human legibility，PVG无CoT/不同CE与RLOO等配置、baseline4轮早停 vs8轮不能作为全部等预算机制归因。

solver温度.7/translator1，max2048后强制答案格式再20tokens；LoRAr1、solver8epoch、verifier4epoch、translator每轮最多8epoch×8round，reinitialize base；lambda .005，sample4/batch28/KL .001，硬件/precision/完整墙钟 ND。监督y、固定solver的样本与译者搜索训练均付费。

actual `TRAIN-GRPO` Ch33 672–684完整 verifier-policy/test权限邻接已读，拥有 verifier更新/teacher权限与 collusion，但缺 **冻结答案producer、允许呈现translator改变检查接口，再由有y的false-answer分支压测verifier**。拟一窄段，保answer-only faithfulness、理想条件与有限训练分界、原固定格式/真实外部核验回退；不从翻译正确率授语义证明或human audit成功。

## 23259 RaWMPC：拟 2+1+3=6，Ch25 imagined-risk 一段

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；hazard acquisition、cost蒸馏proposal与运行MPC分责；sim oracle非安全。2+1+3=6，Ch25自身末注1282；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原prepared作者实际必要原证/actual owner PRE：blocks25–65/69–76/102–113/130–149，hazard acquisition、预测cost蒸馏proposal与运行MPC分责；warm-up/horizon反側及sim/replay边界核到。窄整合已融Ch25 imagined rollout，未核实现/复现；作者实际邻接顺读后交非写入者POST，不授日级。

[v1](https://arxiv.org/html/2602.23259v1) blocks25–113/130–149/153–157实际必要阅读。训练期主动覆盖 hazard cohort，为 action-conditioned segmentation/event/ego world model学习预测风险；运行时有限候选MPC，与其蒸馏出的 proposal 两种权限分开。horizon cost折扣保最小1/8，violation weights10/15/30，从10候选取预测最低；不是硬物理约束或真实最优策略。

固定总clips的random/good/bad与warmup控制支持覆盖差额，但offline/online exposure一同变化，不能唯一归因某个数据比率。top/bottom5of50伪标签的cVAE/InfoNCE仍由模型预测cost产生，不是真实危险判定；只正例、去cost selection、去高risk覆盖有反侧，H10较好但H15、warmup30退步。proposal q+与prior各有局部 tradeoff，不能因对比损失签零风险。

CARLA/Bench2Drive220routes、NAVSIM约103Ktrain/12Ktest nonreactive replay，非真实自动驾驶实测。ViT/BEV1024×256、256²、512视觉tokens；4layer8head world model、H10/past5、latent32；4A100、Adam1e-4→1e-5、B16，1Kclips/100Ksamples。碰撞/offroad/stuck100的stop依赖sim oracle，另50×H搜索/训练费；precision/墙钟/SLO ND。

actual `MULTIMODAL-WORLD-MODELS` Ch25 318–339完整相关邻接已读，已承载误差滚动/真实刷新、optimism与latent attractor。本次只补 **hazard覆盖的数据获取、预测cost生成proposal、运行时MPC三者分验**，保sim-only和coverage不足/长horizon回退、真实反馈/外部安全控制。不重复“风险分数≠安全”的空泛陈述。

## 23266 DDTSR：拟 2+2+2=6，Ch23 streaming identity 一段

[v1](https://arxiv.org/html/2602.23266v1) blocks32–108/137–144实际必要阅读。小模型从partial ASR提前发 connective，大模型只消费final transcript再生成实质内容；LLM与TTS并行不让前缀具备尚未听到的语义。first-significance/minimum-commitment为所写模型规则，entropy confidence阈值不是安全或语义认证；“Sure/But”也能提前承诺同意/转折，不能说所有 connective无知识/无语义风险。

latency定义有“normal content-carrying output”与firstaudio口径，必须区分最早填充发声和首实质答案。两轨共享大backbone并不保证答案正确性不变，G-Eval logical/coherence和UTMOS不是真值/人工非劣保证；SpokenNativQA有质量退步。connective比例SD-Eval94% vsSpoken38%，收益受话语类型限制，不外推全部长句。两套cascade control共同变 interleaving/reordering/early emission，非三机制独立因果隔离。

Qwen3-.6B local connective/LoRAr32 alpha64 lr2e-5，curriculum按500ms chunk、epochs5/3/3/2；loss weights1/.5/.1，阈值.45/.15、Hmax2、候选5–10。4090D local ASR Zipformer+sherpa-onnx/TTS CosyVoice2，8B/32B main远端API，远端硬件/precision/并发/完整费用 ND。3558样本8:1:1 split、不同benchmark实际population分开，API timing不授可复用 SLO。

actual Ch23 900–919完整 streaming邻接已读，拥有 prefix到达/attention可见性、training reference、commit/cancel；缺 **提前connective这一独立audible支路也会承诺语义，filler-first与content-first latency须分别计量**。拟在训练时序支持/可见prefix交接处一段，保ASR误修/阈值、质量回退及保守等待/外部turn-taking；不把它写成通用runtime协议或无损低延迟证明。

### 23266 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks32–108、137–144：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+2+2=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：arrived prefix/commit与Hibiki时序支持已有，但没有partial/final ASR双轨及filler/content首音分账，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。94%/38%不同connective机会、Spoken Nativ质量反侧、同backbone非同事实质量与肯定/转折潜在承诺风险；远端主模型硬件未披露，保等待回退。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 尚未纳入本包

23242 AIQI已读所写Th4.6假设、phase-separated return prediction和直接off-policy非self-optimizing定理范围；仅证明条件性理想on-policy分析，reflective-oracle grain-of-truth不等computable finite implementation，后续actual owner判断尚未完成。23280 original-v1与发现摘要标题/机制不同，须仅重开该ID准入；23306旧ICLR同题家族日期未恢复，均不凭发现稿自动采用。23271/23320仍普通必要阅读，非外部缺段终态。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：23248：原必要blocks9–40/47–54与actual owner独核；Ch33正文694/完整680–703/own2966 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
