# 02/20 第三批有限必要证据：16008 / 16086 / 16092 / 16093

作者 feb20_v3；本文是实际必要原源与owner差额包，不是日级验收、不冻结候选。各版本优先 exact-v1 HTML；支持命题和关键反侧读够即停止，未运行实现或复现。提取行号由同目录 `V3_extract_html.py | awk 'NF' | nl -ba` 得到，原章节号/公式优先。root已实际核四项原源/关键控制反侧与真实owner PRE：16008/16092/16093分别落实Ch23:111/Ch24:758/Ch29:469，完整邻接与自身末注非作者POST通过；DiSC在471极小回接修已实际再核。16086中心争议暂缓/局部仅报告通过，无Books写入。下方原PRE待核文字是写前计划，以上实际POST为最新状态。

## 日期与当前身份

沿首批已独核的官方公告/ID/DOI桥接：Submitted只给最早announcement下界2026-02-19T09:00:00+08:00，arXiv-issued同ID DOI Registered给公开上界（秒精度再+1s），不是Created定义正文公开。原字段保存在各 `V3_DATACITE_2602.<ID>.json`。

| ID | v1 Submitted原UTC | Registered原UTC | 本窗公开范围（含起、不含止） |
| --- | --- | --- | --- |
| 16008 | 2026-02-17T21:00:51Z | 2026-02-19T02:36:04Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:36:05+08:00 |
| 16086 | 2026-02-17T23:20:26Z | 2026-02-19T02:37:54Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:37:55+08:00 |
| 16092 | 2026-02-17T23:39:39Z | 2026-02-19T02:38:02Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:38:03+08:00 |
| 16093 | 2026-02-17T23:49:47Z | 2026-02-19T02:38:04Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:38:05+08:00 |

必要当前事件说明已有限检查：16008/16092/16093实际current abs均只有v1，Comments无影响采用的纠错或withdrawal说明（DiSC注明preprint under review）；原页为`V3_CURRENT_ABS_2602.<ID>.html`。16086实际v1 abs同时展示当前v4身份与本页history，无withdrawal/correction标记；current-v4与v1题摘不同的实际问题已定点恢复，不拿later评价回填，不仅凭version号遍历全版本。

## [MAEB: Massive Audio Embedding Benchmark — exact-v1](https://arxiv.org/html/2602.16008v1)

拟2+2+2=6；评价反侧/actual owner差额深入。实际§2.2（190–208）分类是8样本/类logistic probe，zero-shot分类是audio embedding与label text，clustering用已知label数k的MiniBatchKMeans/V-measure，retrieval为cosine/CVRecall@5，rerank为MAP@1000。它们不是同一能力分数，也不是ASR/生成评价。§3（210–223）53模型分四训练类型，最多30秒且保更短native limit；16/48/24kHz与pooling按模型原接口，并非完全相同input pipeline。

§4.1（702–724）的直接反侧是同VoxPopuli下CLAP-htsat-unfused gender94.4/lang30.0与Whisper-medium59.2/lang99.4的排序反转，及高平均分模型clustering弱；支持按目标信息/读出选encoder，不证明两种信息数学上不可兼得，也不把相同参数量当因果control。§4.2（725–737）不是30项总榜对audioLM普遍预测：仅4 audioLM的26分类task子集对MMAU，R²=.86、p=.072、n=4，直接保留小样本/统计边缘性。§5（738–748）长音频截断、资源成本、Western music/标准语音与language coverage偏置，不能外推podcast/全语言。

实际owner `MULTIMODAL-REPRESENTATION`：[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 18–47已拥有采样率/codec/信息损失identity，107–109有phoneme与连续projector保声学细节的条件；没有把同原语音上的acoustic/linguistic probe排序反转与监督/聚类读出一起用于encoder选择。拟最多一自然段，接现有语音接口论证：统一embedding接口不等同一种信息，按speech-content/speaker/timbre与实际readout验收；probe/预处理/短片段评价额外成本，任务单一时专用encoder仍合理，不采普遍AudioLM预测。邻接Ch22/24开篇已实际读。PRE待独核，未写Books。

## [LGQ: Learning Discretization Geometry for Scalable and Stable Image Tokenization — exact-v1](https://arxiv.org/html/2602.16086v1)

拟2+1+2=5。原inventory题摘是later《LGQ: Learnable Geometric Quantization...》的256²、100% utilization与MaskGIT；已实际取 [v1 abs](https://arxiv.org/abs/2602.16086v1)（`V3_ABS_2602.16086v1.html`）完整题摘，恢复本窗精确标题/贡献，不给later事件当窗权限。

实际§3.1–3.2（120–150）learnable centers、temperature soft assignments、hard argmax forward/soft-average STE backward，token peakedness与batch-average global usage两正则；**公式以未平方Euclidean norm为energy**，不授摘要的isotropic Gaussian posterior身份。§3.3（151–174）定理假设distinct centers却在证明用unique nearest：例如c1=-1,c2=1,z=0始终两者各.5，distinct不够推出one-hot。采用条件可收窄为unique minimizer，不证明原strong theorem完整成立。

§4.1–4.2（231–243）同VQGAN enc/dec、C64、downsample16、K16384、ImageNet128²，局部reconstruction rFID110.64 vs FSQ125.56/SimVQ117.77，FSQ/SimVQ有reconstruction-loss/PSNR优势；LGQ8199 active codes而非约16K。§4.3（330–362）把active-code数近似“rate”，**不是entropy-coded bitstream/实压缩bitrate**；Keff定义为perplexity也不能与active count互换。§6（385–387）没有learned prior/MaskGIT end-to-end，其他模态/分辨率和正式rate-distortion bounds未证。

当前中心probabilistic/convergence/rate强主张争议隔离；算法和有限重建结果可报告，不授collapse-free、49.45%压缩或普遍生成提升。actual Ch23:172–180已经拥有codebook-collapse、encoder STE与code追踪职责/usage非质量；同处还没有这两个正则具体recipe，但不能仅少一个recipe把争议中心升级为gap。拟Books暂缓，不写；重开需修正unique-nearest假设与energy定义、独立bitrate/生成必要证据，或单独获得非作者认可的局部机制采用边界。

## [Why Any-Order Autoregressive Models Need Two-Stream Attention: A Structural-Semantic Tradeoff — exact-v1](https://arxiv.org/html/2602.16092v1)

拟2+1+2=5，设计反侧深入。实际§2–3（63–92）区分original semantic order与generation structural order；semantic-locality/最近structural位置含完整summary是作者hypotheses，不是形式下界。§4.2（106–126）query按要预测的leading semantic position旋转，key按已观测token的lagging位置旋转，不暴露target内容；单流仍同时承担预测/摘要。

关键control §5（129–151）8M transformer/text8 character、128与1024，temperature扫coherence-diversity（有效English≥4字word与unique-word比例），D-RoPE与MDLM短序列近、长序列退化。§6 Limitations（157–158）**没有直接two-stream对照**、小规模字符级、只是consistent-evidence hypothesis；不能由D-RoPE失败唯一识别双流优势原因、宣称two-stream必要定理或大模型普遍结果。不同attention/objective/architecture替代解释仍在，训练成本、attention计算与native cache需另分账。

actual owner `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md):754–756已经具体拥有query/KV共同防clean-label泄漏的strict/content两流与计算代价，不能重复“two-stream防泄漏”。拟窄差额为**避免target泄漏与处理semantic/structural locality张力是两个问题**，接该论证一段保hypothesis/未直接双流比较与短序列旧单流共存，不授论文标题的必要性。Ch23/25正确路径开篇交接已经实际补读，PRE待独核，未写Books。

## [Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities — exact-v1](https://arxiv.org/html/2602.16093v1)

拟2+2+2=6，actualowner接口差额受影响深入。实际§3.2–3.4（115–157）同post-trained初始化：teacher永久冻结、student更新，document按句选k-1随机+最后split，teacher读完整前缀、student只读该真实suffix，**forward KL以同suffix token对齐**，不是student on-policy rollout。teacher一次全document forward、student把suffix拼接且attention分块隔离一次forward，总两次forward，不需要teacher生成transfer set；仍有teacher驻留/logits与训练计算。

§4.3（180–183）FP32单epoch、四模型families/sizes。§5.2（994–1005）CP checkpoint共同按适配score最大且IFEval/Math/HumanEval最多约5点退步选，AppB（1526–1530）batch1、DiSC/FT共同10LR sweep、T2、k5增大仅边缘收益增成本；不是相同LR一概授优或无需调参。KUP合成news知识更新可支持本文主线；BioASQ只作作者另一适配数据条件，不扩Science领域机制。§6.2（1090–1115）n6/model-task下train-domain KL与heldout遗忘相关符号随域变化，反驳通用KL-small即retention的判据，未因果证明所有遗忘由KL或posttraining-reversion造成。hardware/端到端wall-clock与production忘却未披露，不采速度比例。

actual owner `TRAIN-SFT`：[Ch29](../../../../../books/part-04-training-system/29-sft.md):446–488是同student on-policy prefix/privileged behavior context，874–892为new-fact acquisition/retention与生成replay；已有KL/teacher lineage不是完整raw-document split接口。拟一自然段接Context Distillation主线：只读raw文档时可用真实suffix而非生成transfer set作分布蒸馏，原同on-policy路径仍有state-coverage优势；teacher条件更丰富不保证知识truth、suffix监督与能力preserving选点不同角色，budget/old replay/RAG/adapter共存。Ch28/30开篇交接已实际读，PRE待独核，未写Books。
