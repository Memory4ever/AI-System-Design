# 本日贡献筛选与有界来源恢复

## 后到纠正与跨日分层

后到必要原件优先于下方准入时的题摘线索：23594 PRISM-Bench current官方abs已撤回（first-error groundtruth含GPT幻觉），撤回准入、不评分/入书；22276 WAON首版没有题摘声称的native/translated受控对照，具体撤回准入待reader核；22969原“已知平均场界”误排已重开，writer实读新增条件drift/pathKL界后准入6分，详EVIDENCE。初批22084/22085最终分分别2+1+2=5/2+2+2=6，依据精确采用命题而非工作量；旧safeguard分不动。

38跨日的earliest分布Sep18–Oct27，不可概括成统一Oct27。22潜力日期未解：21722、21740、21746、21770、21786、21792、21794、21805、21807、21834、21844、21849、21850、21853、21861、21864、21866、21867、21879、21885、21908、21910。完整题摘已读，仍只是潜力身份，不评分、不先列本窗候选。需精确公告/带时区官方首次正文证据把earliest–registered区间收窄；Updated(v1)、submission、IDmonth、第三方“firstposted”不代日门。

其余16停止日期恢复，原因分别：21723 patterned preference与internalstate的循环解释缺独立状态测量/新机制；21757作物科学；21761 JORA资源/attributeprompt组合未给新模型条件；21791遥感fusion；21793 industrialanomaly的RGB/pointcloud组合；21795 Xihe层次local/global注意力分解和时序任务收益未给新foundation系统约束；21798单18volunteer混合标注workflow速度、缺新的独立truth/误差条件；21812 recommendation INMO/跨域/多模态组合；21820生物医学；21828 relationalimage资源+两阶段训练；21829医疗survival；21835 ecom multitask与预测属性prompt组合，无超越已知hallucination/资源取舍的新一般机制；21847天气；21862 YOLO/Donut工程图接线；21881 geometrydata/rationale常规SFT；21906图优化的VLM+sparsify/layoutensemble任务组合。均不由日期未明倒推排除，已实读完整题摘；科学标题范围足以关闭。

实际日期替代路径：官方CL月表旧短2510路径404后，沿已有实际2025-10/month/show2000形状恢复两页1–2000/2001–2666及末页，但只有月成员没有日分组。只定点浏览本日主题相关标题，不变全部Methods。有限search（本日执行）为精确21722、21740，以及`site:arxiv.org/list/cs.CL "Tue, 28 Oct 2025"`、`"Mon, 27 Oct 2025"`和官方past announcement help；没有恢复官方日档。21740搜索出现作者/镜像的submitted Oct2和SciRate Oct28，均不满足官方公告的权限，故不授日。DataCite原dates仅Available=2025-10、Issued=2025、Updated(v1)Oct28，不能额外收窄。现有缺额仅上述22，不泛化38全H，也不靠HTTP200授Coverage。

本次补窗BJT 2025-10-28。`REPAIR_INVENTORY.json`仅保存六主题原字段及联合界；不是候选表。旧候选和旧证据不变。以下是完整题摘后的具体增量，尚未读core者不记完成。

## 来源停止

DataCite六有限主题与同义表达见 `repair_fetch.py` TOPICS及DC2 request；MODEL为2页128，TRAIN61/INFER17/AGENT36/MULTI73/EVAL28各一页，registered/created双向差额0，各260唯一身份。query内错误client字段首轮不支持零事件，四拆分正控及B0/B1保留。222合法同日界，38跨日。2025官方发号规则、唯一v1、精确DOI的arxiv.content/findable/registered联合复算；不授全球首公开或历史逐字全文。

Google三页有限年/主题卡片本日实际恢复15/15/7，37卡片含同题不同入口，不是当日37家族。静态href为`javascript(0):void`，实际data-page及官方bundle构造page2/3，不能声称本次原件有静态href。浏览器点击还发生search丢失扩到全年680，立即停止该扩展、不取全年；保留有效主题三页的HTTP原件。三页标题/venue未出现具体Oct28日级新线索，不将年度导航变逐条日期请求/Methods配额；日级first目录缺额仍隔离。

Hunyuan本日官网新bundle指向Blog/Research同一组件，`Se=[{renderType:0,labelKey:"blog.allTab"},...]`；实际用中文header、pageNum1/pageSize100/renderType0响应`totalNum11/list11/lang=zh`，比对本日原件而不借他日数。所有11条展示时间在2026，最早2026-02；这只证明当前中文全部响应已取完，**不证明2025零事件**。官方列表历史缺段保持隔离。真实API映射见当前bundle、RESEARCH_CHUNK、API_CHUNK与request。

其他每日源复用本日旧入口/响应/停止，覆盖至Oct28的相邻记录已经存在；不能恢复的历史段沿原隔离，不以当前页面授零。原旧arXiv Oct27 18:00至Oct28 18:00提交片是Oct29公告线索，不把它的66个潜力/七core搬到补窗；本次通过registered发现独立重建。

## 首批准入校准（全部2510前缀）

| ID | 约束→实际新增→改变的选择 | 拟分 | 首必要 |
| --- | --- | --- | --- |
| 21956 | 线性attention理论复杂度不能兑现→前后向重排与CUDA kernel→比较实际端到端收益而非只数FLOPs | 2+2+2=6 | writer |
| 21970 | 4bit通常被当作更快→T4出现dequant负加速且CPU/GPU协议不同→量化选择需绑定硬件/协议 | 2+1+2=5 | writer |
| 21977 | survey模型拟合训练分布→显式学习跨背景分布位移的目标→分布模拟不等单样本标签拟合 | 2+1+2=5 | writer |
| 21978 | task-KL不保任务外能力→RECAP动态重放目标重权→用跨目标测量控制遗忘 | 2+2+2=6 | writer |
| 21986 | DiT均匀丢token伤浅层细节→稠密浅层/稀疏深层残差融合及短全token阶段→按层分配训练计算 | 2+2+2=6 | writer |
| 22009 | 小端侧模型与云成本矛盾→OpenPhone按复杂度升级及历史压缩→评估端云分工而不等同大模型替代 | 2+2+2=6 | reader |
| 22014 | jailbreak跨prompt迁移原因不明→拒绝方向/正交变化统计与干预→以表征几何限定迁移而非语义近似 | 2+1+2=5 | reader |
| 22026 | norm位置只被看作训练技巧→球面token动力学/速度调节→在假设下比较聚类/塌缩 | 2+2+3=7 | writer |
| 22042 | 情绪文本标签不等内部结构→多语多集低维表征与干预→区分可预测/可操纵与情感体验 | 2+1+2=5 | writer |
| 22067 | 按静态visual attention放大可放大sink→GIFT使用query阶段attention正变化并平衡query→视觉选择不直接等同高attention | 2+1+2=5 | writer |
| 22084 | preference排序被误当合取约束学习→六方法受控合取控制反侧→不把局部DPO失效推广为不可能性 | 2+2+2=6 | reader |
| 22085 | 手工攻击模板难规模化→LoRA紧凑narrative attacker与跨模型评估→限定已测攻击面而不授普遍防线 | 2+1+2=5 | reader |
| 22101 | 只压参数不能保证SLO→生产SLM参数/上下文/serving联合优化→分开质量bar与吞吐协议 | 2+2+2=6 | writer |
| 22109 | 长上下文只加内部记忆→输入对数分辨率压缩→保持架构不变但接受信息有损边界 | 2+1+2=5 | writer |

代表排除完整题摘已读：21958作者文风预测；21984群体沟通效应；22034 VC预测中ProbLog/规则挖掘组合；22052愿景；22087领域题库与内存设计任务收益；22095 BCI position。它们分别缺直接模型/系统增量、只有成熟组件组合/场景收益，或没有新增可核条件，不因机构/数字/owner相似准入。科学应用/明确医学天文气象标题按ROADMAP暂缓；范围含糊者读完整摘要后判。

## 后批完整题摘已读（待校准后的必要审阅）

下列是具体新机制/局部有效性条件线索，不因低样本或已有覆盖排除：

- 22118 2D primitives替3D伪标签误差链；22127 corruption embedding variance collapse和伪标签方差TTA；22132 entropy驱动thought-vector优化；22170 SJT/MIRT替自陈；22171 token级hidden/output联合uncertainty；22201 action-coherence流采样guidance；22210 LSP符号边界替语义近似检索；22219无真值pairwise error识别假设；22242不透明搜索下证据/指令混杂；22272小语料RAG/CPT及图像/文本对照；22276 native/translated同预算控制；22317 CPU memory-based替代LM；22332 FF原生feature对SAE强基线；22340动态变体与过程错因；22362 activation-space concept walk及干预。
- 22366 tail-truncated noise watermark的robustness/diversity；22371 complexity scaling下LRM骤降；22422 group size非线性/meanfield；22443 goal MCQ/generative差异及模态消融；22455 audio/MIDI感知-推理混杂；22467 approximate backward/error feedback；22475 persona-conditioned协同decoding；22489 task/general校准分区pruning；22535 跨模态unlearning恢复/攻击反例；22543 flawed-positive动态奖励；22556 语义块自适应KV预算；22571 object-state三任务一致性；22593 reciprocal judge重权；22594 pretrain/context KL理论；22603 BOS相关sink及decorrelation；22614 24M交互下Platt不奏效/个性化数据门槛；22620 threat snapshots；22626 complexity profiling反馈；22641 imitation/self-spec VLM。
- 22650 weight-eigenvector编辑；22673 fraction-shift equivariant attention；22689 source-presence规则搜索；22693 variable-time event tree；22694 retrieval necessity/modality门控与noise curriculum；22706 3D-consistent instance contrast；22732 cognitive-map hypothetical rollout；22752 固定token位置/置换语义的temporal retrieval；22758 neutral scripts/controlled voice；22765 personal KV retrieval；22768 raw visual persuasion与function action；22775 execution-free patch reward；22785 semantic/spatial TTA attack条件；22827 abstention-aware视觉judge；22836 recipe放大modality gap；22849 per-instance程序结构反馈；22851 prompt embedding概念擦除及视觉反馈；22852 clean encoder/noise decoder复用；22881 MML preference目标；22922 human verification interface RCT；22926 uniform diffusion只训替换token；22931 domain-shift conformal/rejection；22936 保持多位置的压缩算子；22944 benign prompt normativity攻击面；22954 model内/间同质化与个体偏好校准；22956 longctx tag及tag-only对照；22960 temporal/region fairness attention；22961 frozen speech backbone中间视觉注入；22963 compressor共享预算攻击；22977 reasoning RL迁移tool hallucination；22993 ICL skill composition对齐条件。
- 23006 相同ICL分数不同架构内部；23010 subtree局部重推及memory；23027 router-aware offpolicy IS；23038 tool-integrated RL judge；23052 cross-head feature projection；23070 translation-quality metadata而不改正文；23095 multimodal RoPE position/frequency/text prior控制；23119 human-image→robot-action与force闭环；23145 implicit transferability估计；23167 human-intent reward重权skill discovery；23182 process reasoning与reply质量/CoT反侧；23184 graph→feature-field场景对应迁移；23190 privacy transform改变action cues；23240 AR图像stop/alignment及CFG；23254 mixture-prior任务难度自适应理论；23264 patching mixed precision；23272 interactive aesthetics reward；23285 ODE/SDE误差与learned stochastic coefficient；23324 human/model-led接口双RCT；23334 fixed-budget early-token search；23393 max@k unbiased/offpolicy objective；23397 annotation ambiguity与curriculum mask；23458 multi-turn confidence retry；23473 intrinsic grounding/captioning tool-free视频推理；23479 token mixup及soft-margin偏好；23482 visual thought干预和sufficiency；23487 controller-memory/trace限制；23497 teacher/student coldstart错位；23532 path-only关系基准假设反侧；23558 instruction-style adaptation遗忘；23574 固定生成backbone双任务converter；23576 noisy-route alignment/trajectory；23588 NF+AR exact likelihood及latent partition；23590 preference-only DRO；23594 error-detection与answer decoupling；23595 coevolving proposer/solver/judge；23596 two-turn dimension-focused RM；23601 trajectory→parameterized MCP tool；23606 latent dependency masked diffusion。

明确排除（完整题摘）：22126现有LLM调参+自适应controller组合未新增一般执行/控制边界；22142 SFDA多注意力/对比模块收益无foundation机制增量；22192 OR taxonomy/tree prompt应用收益；22204 scene graph+离线LLM规则组合只给landing成功数；22205 construction trajectory；22257 EEG科学支线；22282 城市社会指标预测；22318教育题库；22338设计文档prompt应用；22344 SEA checklist+循环RAG的组合/任务F1，未隔离新增有效性条件；22369常规contrastive/hardnegative+pool/prune语言embedding recipe；22370 BLIP/PPO/PID lane组合；22389医学论文质量评分应用；22395新增科学文本hallucination资源但未发现特定评价混杂；22396代码检索/历史总结/编译反馈组合，未新增执行/验证机制；22407 longitudinal causal-estimation应用不改变主线模型；22439 VAE/flow合成RIR组合；22488 literacy-tracing任务；22514 非LLM/foundation controller理论不以agent词收回；22515/22527科学应用；22531 legal NLP已有LoRA/FT比较未隔离新的设计条件；22547低光增强；22559教育diagnosis/recommendation/feedback组合；22581教学评价survey；22609临床pipeline；22610话轮互动社会学观察未提出新模型/执行机制；22691 class-to-token映射+PEFT单pass分类是已有套路，未给新约束/可比边界；22747 CPT/LoRA方言案例描述corpus-dependent收益，未隔离新训练机制或成立条件；22751多源fact-check组合只headline收益；22763 WMT迭代层prune案例无新importance/稳定边界；22781 learned decision-tree+agent router生产例子未给新增一般执行/训练约束；22787 C4 role-dialogue组合；22798 两阶段SFT/RL+visual prompt用于手写评分，未给独特算法/边界；22823 aligned/commercial与open权重对照混杂，未隔离alignment因果/新机制；22830长文summary评分；22838三个命名模块/contrastive style recipe及单一数据集指标，没有明确不同于成熟disentangle/align/consistency的机制或新条件；22844教学thread标注；22888 recommendation grounding+user反馈组合；22892 LLM+VMC/Lyapunov-RL组合只场景收益；22909 offloading survey；22928 score/noise anomaly detection的应用方法未改变foundation generator/系统，未达主线外突破；22967 debate+weighted factual claims组合；22969 wireless mean-field diffusion planner的资源分配应用及已知平均场界，未呈现可改变主线模型/系统的新条件；23055需求分类评测；23066 OCR/retrieval/compact VLM文档pipeline；23074 vLLM batch+共享中间cache工具接线未新增审计/运行机制；23077现有GRPO推荐任务；23081 midtraining术语survey；23090时序forecast prompt组合；23144交通3D detection；23148 PDiT复现+CLIP loss只局部任务收益；23186 RF合成训练；23245治理reference架构无实际机制证据；23252方言ASR数据及常规dialect训练收益；23271 proprietary closure叙事未披露具体新机制或受控证据；23337 BaZi persona任务；23357服务机器人survey；23410广告bidding专用attention/zero-inflated投影；23421行业风险index；23464金融stance任务；23477 tutoring新任务/rubric及OCR降质未隔离一般评估盲点；23506情绪label-rationale reward组合，无超越标签一致性的新增faithfulness机制；23509逻辑norm+world-state/LLM导航组合，未披露执行soundness新条件；23511 VLA toolbox兼容整合；23536新intent预测目标/selection proxy未给一般评价条件新证；23554 U-Net/OCR/NMT组合；23569大规模ego数据+SFT/RFT常规两阶段未给新增机制/隔离边界；23585 hope speech分类；23587 data-agent taxonomy。明确医学/天文/蛋白/化学/遥感科学应用标题另按暂缓关闭，不逐项Methods。

仍需有界定点准入的含糊项：22235 CGoT、22622 DeepfakeBench-MM（是否有独立stacked-forgery新盲点），只读决定准入的必要段，不自动候选/全篇。
