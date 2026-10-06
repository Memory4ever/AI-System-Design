# 2025-10-31 有限筛选与必要 core

作者 Curie。三主题 API：12分类限定模型/训练，LLM inference/cache/kernel/serving，foundation-model Agent/多模态/World/VLA；`submittedDate:[202510291800 TO 202510301800]` 只是发现范围。每主题 start=0/max_results=50，total=26/10/29，无剩余页，去重61。完整精确 v1 题摘44条来自本日 `arxiv-v1-abstracts.raw`，不以当前 v2/v3/v4 摘要回填。常规公告与1–4工作日质量检查说明已读；未取得历史官方公告，不用 submitted、API published 或 DataCite 注册充当 first-public。

## 贡献初筛

下列完整题摘显示具体潜力；均 DATE_HOLD，未评分、不记当窗候选/审阅完成。这里按贡献命题归组，不把全年/整类条目转成逐项队列：

- 架构与学习：25933 scaffold与微调互补（非小模型直接等价 frontier）；25947绝对多语token量与比例的混杂；26027视觉encoder temporal attention；26182 SSM多头专家；26183 SDM校准/拒答；26219 pre-logit importance-sampling control；26441 angular diversity与校准；26446稀疏/低秩统一优化；26622 encoder-decoder scaling与微调前后排序；26692 KDA细粒度gate/混合MLA；26697学习逐token解码参数；26721视觉key-space偏置；26771序列维量化/混合精度；26788训练rollout精度反侧；26792 PRNG curriculum与表示。
- 系统：25860 label-only judge traces的拒绝采样与准则；25977 v1题名 **NeuronMM**，不是当前v4 NeuronMLP；25979 attention-map近似复用只prefill；26136质量/成本frontier；26577 batch/device-aware speculative tree；26730 adaptive专家预测/缓存routing；26835按类别阈值/TTL与miss-cost；26843动态cascade草稿配置；2511.00101共运行LoRA微调/serving。
- Agent/多模态：25863治理控制平面须核安全实现主张；25941反馈式记忆提取与污染反侧；26052 VLM动态负prompt；26167 v1题名 **One Model to Critique Them All**，不以当前ToolRM题名覆盖；26200 diffusion update forgetting；26352 dialogue graph组队；26433联合LAM/World warm-up避免collapse；26457 SecureBLEU评价盲点；26583 DiDA/原生多模态next-state；26585 runtime自适应监督触发；26658 AsyncThink并发思考学习；26702语义task-scope授权反侧；26752 oversight MPG前提；26782几何正则World rollout；26799 masked diffusion视觉学习；26852 v1 CATArena迭代学习评价；27190跨阶段风险观察与概念防线分开。

Mill FIRST指出三项原“组合即无增量”理由误判，作者依据原完整v1题摘窄恢复，不因题摘欠实验细节关闭潜力：

- 2510.26615v1 SlideAgent：query-agnostic全局/页/元素表示预构建，推理时选择agent激活，可能改变query-dependent在线执行成本/依赖；不只三层拆分。
- 2510.26339v1 GLYPH-SR：冻结主SR分支，训练OCR TS-ControlNet并交替文本/场景guidance调度，可能改变生成路径的可读性/感知质量取舍；不是仅领域指标。
- 2510.26144v1 FM Agent：新evolution sampling与分布式异步执行用于GPU kernel/MLE，主线潜力保留；Science数学应用仍暂缓，Ray/专家初始化不单独给分。
- 2510.26104v1 OneTrans：Mill DAY额外实际读完整v1题摘/历史，统一序列与非序列token、共享与token-specific参数、causal attention KV跨请求预计算可能改变表示/在线复用依赖。foundation/LLM适用性未确认，推荐GMV不当LLM效果；此项不是作者旧44题摘已读。

四项均范围/日期潜力，不评分、不计当窗候选/Evidence。submitted/API published只发现；恢复各官方first-public公告或完全落窗bounds后只核对应命题，不默认全附件。

明确领域应用标题16项关闭（原17减OneTrans，题名在原API可回查）：2511.05537 EEG depression；25976 fMRI Brain-IT；26838 underwater bioacoustics；26023 vehicle immobilization recovery；26362 multi-arm transformation控制；26568 spine ultrasound；26603 residential energy；25914 FinOps用例；26114 Oracle bone script；26172 social media data；26242 traffic signal；2511.00095 spineCT；2511.00096 urban prediction；26494 social mobilization；26498 clinical triage；26641 object detection survey。Mill分层抽检Brain-IT、bioacoustic与survey完整v1题摘维持关闭，其余未逐项二次核验；不泛扫视觉/领域应用。

## 有界标题补检

官方 `cs.CL/2025-10?skip=2600&show=100` 实际2601–2666，仅浏览66题名，不是66全文队列。选10相关/反侧标题恢复完整v1题摘；其中6是相交/更早提交但首公开未确认的独立日期保留：26037 SIRAJ、26038 KD debias、26241 Arrow-of-Time、26745 geometric memory、26847 Broken-Token、26935 RepV。保留具体增量，继续必要core。

另4条 arXiv v1 **提交下界本身晚于本窗终点 UTC 2025-10-31 01:00**：27258 `2025-10-31T07:54:37Z`；27378 `11:14:39Z`；27484 `14:02:37Z`；27623 `16:50:49Z`。不能属于本窗 arXiv 首公开；这是该发布路径下界，**不是全网首次公开已经判为窗外**。只留真实日期恢复线索，不在31读附件。

## 必要 core 实读与停止

下列均精确v1，日期未通过不授正面 Evidence。数字是本日 `.txt` 原页提取定位行；原件 `.raw` 保存不等于已读全篇。

| 身份 | 实读位置 | 限定命题与关键反侧 |
| --- | --- | --- |
| 26788 FP16 | §3.4–3.5 178–212；§4/4.1 213–228；§4.4–6 248–277 | DeepSpeed/vLLM等引擎精度匹配有局部反证；主sanity是1.5B/8A100/64题×8rollout、8K、4更新的perfectible MATH训练集，另有Qwen3-30B-A3B MoE、Qwen2.5-Math-1.5B LoRA、Qwen3-14B与OctoThinker-3B子实验，不写仅1.5B。均不等总体能力；FP32 rollout约3倍慢；极大模型FP16溢出仍未知，不能宣称消除所有mismatch。 |
| 26622 RedLLM | §4–5 208–232；§6–7 243–263 | 1.6T总token但encoder-decoder有效目标0.8T；同参数/compute/PPL与下游不可互换。FLAN微调后排序变化；2TPUv5p、batch1 throughput不外推生产SLO。 |
| 26692 Kimi Linear | §3/3.1 160–180；§5.4 451–485；§5.6 702–718 | KDA diagonal gate +3:1 MLA混合不是完全抛弃attention；1.4T matched实验和5.7T发布checkpoint分开；batch1长context峰值不证明一般6倍吞吐；该段hardware/SLO未披露。 |
| 25947 multilingual | §2–3 83–116；§8/limits247–259 | fixed-total100B与fixed-multilingual90B+English到225B不能合并；1.1/3B、tokenizer与规模/后训练限制，不把“无curse”当普遍定律。 |
| 25933 Humains-Junior | §3 241–250；§7.1 1767–1793；§7.3 1886–1908；cost1450–1497 | FACTS first500 vs frontier first100、±5pp等价不等任意GPT4o能力；微调+scaffold潜力保留。费用估算含摊销/电价却声称接近零，所列0.72美元/小时×22.2秒与0.00016/千token不一致（作者回算），不采用成本结论。 |
| 25941 RECAP | §3–4 110–164（窄补129–134）；§5.5–6 264–283 | gold reference辅助反馈不是无参训练集鉴定；35books含5cutoff后对照、40token≤5差、book-bootstrap；半数反馈无增益、<20%继续轮次获益、非训练误提取非零；不读版权全文/攻击附录。 |
| 26457 SecureReviewer | §2.1 80–112；§3.1 213–229；§3.3 234–243；§5.1/5.3 561–594（补574–591） | GPT4o筛样+6–7B LoRA；生成评测排除38无issue样本只262，SecureBLEU相关性不等可利用性验证。pattern/context错误和RAG训练集限制保留。 |
| 25863 AAGATE | II-A/B110–149；III-D–V264–305 | blueprint提出实时kill-switch、链上证明和side-effect可逆，无该core的runtime测量/强保证依据；不把规范组件名视为安全达成。 |
| 26702 task-scope | III89–105；IV107–123（补107–114）；V-C/VI218–232 | trusted proxy/AuthZ保留原intent；GPT4o T0+embeddings，synthetic/Toucan 1–3tools；3tool漏授显著。随机wrong/null非对抗认证或dispatch原子性证明。 |
| 26752 Oversight Game | §4.1 224–245（含证明）；§4.2–5 245–287；§8.2 394–399 | MPG+ask-burden是条件，teamgame共享reward满足它；放宽前提只能有界损失。gridworld、可强制wrapper与安全oracle不是现实自动满足。 |
| 27190 Unvalidated Trust | §4.1–4.7 220–260；§6.1–6.4 319–361 | 原观测纯text、禁tools/execution；multimodal是模拟或conceptual，不当真实exfil/跨组件攻击验证。公开模型ID与评测期相容性还需核，不采用总体安全率。 |
| 26200 TTA | §3–4 184–214；§4.1–4.3 324–346 | pertoken软timestep减弱覆盖，非不可逆freeze；RoBERTalarge330M/C4/64token与classifier-guided toxicity只该条件，不授一般DLM安全。 |
| 26037 SIRAJ | §5.2/5.3 179–193；§6.1 210–237 | 16agent/12toolkits/123tools；1920生成 vs429静态不当相同覆盖分母；ASR@K在初始拒绝子集，ASR-T另分母，K3；等1950SFT/4700RL结构蒸馏不等所有blackbox工具风险。 |
| 26038 KD debias | §3 125–153；§7/limits291–301 | BERT/T5/ResNet/ViT、4数据集、3seeds，ID平均不保证各偏置OOD保存；logitKD/单teacher限制。不是因小模型负面排除。 |
| 26241 Arrow-of-Time | §3.1 100–114；§4 138–149；§6–8 473–491 | 212高共识clips/424方向视频、排除cyclic；F/B偏置/增加reasoning恶化是局部反证，缺乏因果归因解释，不直接证明所有VLM没有物理能力。 |
| 26745 geometric memory | §2.1 197–212；§4 296–318；§6 368–380 | symbolic固定图/GPTmid+Mamba与Node2Vec spectral猜测不同证据层；未正式证明pressure解释，也不外推自然语言全部记忆机制。 |
| 26847 Broken-Token | §3–3.2 271–318；§3.4–3.6 325–355 | English20k×6编码标签、四BPE阈值同批优化不等harmfulness/jailbreak阻断；中文/阿拉伯分离恶化，nonalphanumeric攻击未测；window5tokens可误伤正常内容。 |
| 26935 RepV | §4.2 159–215含Theorem1证明；§7.1 364–382；§7.3 397–408 | calibration假定i.i.d.；式5是距离球条件概率，不等每个新plan/真实effect安全证书。CDF定义文字与公式有差异；4域40plans×5rules与robot演示不验证任意OOD。 |

Google PPI 必要隐私原页及白皮书精确`2510.21684v1` §3–4 94–155已读：TEE KMS、HPKE、device-approved binaries、rollback-state/RAFT key erasure与DP-unit/budget同链；TTL只是best-effort不可验证，侧信道仍未解决，Sybil与DP不同层；Gemma3-4B/AMDSEV-SNP/reset每upload不是无条件隐私。日期保留后不扩其代码/附件。

Google magic cycle 原 Blog119–170必要topic段已读；Science暂停，factuality/效率段只概述既有成果，没有当窗新机制或新比较证据，不扩所有链接。DeepMind Personhood 原210560页完整Abstract177已读，法律人格/权责治理而非本项目模型/执行机制，关闭贡献；不为日名请求精确时刻。

## 本日停止

处理到具体命题即停。必要18份v1+PPI白皮书只所列core，不是19篇完整Evidence完成。原模型card、源码、全附录和被关闭领域应用均不作默认队列。Aardvark官方core44–58/2026更新37–39由Mill实际贡献关闭：已披露流程无新的可核搜索/控制算法、利用条件或受控比较，私有gold92%缺数据/误报分母/预算；拟5分撤回，不是1项完成Evidence/OnlyReport。正式候选0，Books最终差额/提案/写入0；只待Mill核同步变化。
