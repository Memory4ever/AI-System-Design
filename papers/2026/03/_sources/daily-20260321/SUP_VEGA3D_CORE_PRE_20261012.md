# VEGA-3D / 2603.19235：必要 Source 与 sole owner PRE

准备者 resume_mar18；只本 Daily2026-03-21 补 BJT2026-03-20。当前为作者准备，不自授非准备者Source/PRE、写锁、实际POST或DAY。原窗口/旧候选/连续§4保持；不扩发现、版本diff、代码或无关图附件。

## 身份、日级归属与增量

[exact-v1](https://arxiv.org/html/2603.19235v1) / [official v1](https://arxiv.org/abs/2603.19235v1)：Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding，八作者Xianjin Wu等，v1 Submitted2026-03-19T17:59:58Z，原comment31pages/12figures。当前officialabs同题/同八作者v3Jul17、v2Jun29、commentAcceptedECCV2026，未见具体撤回/纠错信号；不把后续accepted当更早正文公开，也不扩夏季修订。

本次实际curl官方DataCite DOI10.48550/arXiv.2603.19235：v1 Updated2026-03-20T01:20:33Z，created/registered2026-03-20T02:31:48.000Z，statefindable，Available2026-03；当前version3与v2/v3事件字段分清。结合本批原公告/schedule作BJT03/20日级限定推断，不将submitted当公告时刻、不声称互联网从未先公开。

准入原完整AB已本日65校准：语义encoder单一路径→冻结视频生成器中间特征与逐token融合→需要分别验收预训练目标、noising/取层及同任务读出，而不是只按生成器名称宣布物理知识。拟2+2+2=6标准；actual长期接口缺口触发必要深入。成熟gate/缓存原则本身不另加分。

## 实际必要 Source

已实际读v1 §4.1–4.3/Eqs3–8、§5.1–5.4/Tables1–5、§6；AppendixA/Alg1、B1–2/A1、C1–2/Eqs9–15/A2、D/A3与A5的直接反侧及F。未声称所有31页/全部图、code或实现/复现已核。

- §4.2：真实输入video经VAE得z0，再按flow路径一次构造zk=(1−tk)z0+tkε，空textprompt读取冻结Wan2.1-T2V1.3B中间DiT层。这里是对现有输入的一次特征提取，不是执行完整未来rollout或得到新的独立观察。默认k300/1000、layer20；pool对齐semantictokenization，独立MLP投影到LLM维度，LN后concat输入scalar sigmoidgate，凸混合两支路。Gate可学习不证语义/几何已真分离。
- A/Alg1：generativeencoder冻结可offline特征或onlineCacheOrEncode；semantic/projector/LLM沿启用参数训练。代码式流程仍UnprojectDepthToWorld并给fusedfeatures加3DPosEnc，loss可选groundingloss。§4.1说depth/pose只analysis，不足覆盖Alg1的训练路径；不采用整体“无显式3D信息/监督”。B1scene训练含ScanRefer等五ScanNet下游任务；spatial训练SPAR7M+LLaVAHound，后者存在spatiallyenrichedsupervision；LIBERO是sameOpenVLAOFT下游data，无新增robotdataset不等没有动作监督。
- Table1对Video3DLLM多项局部提高，但Scan2CapCIDEr83.2<83.8；多peer指标并非全SOTA。T2同finetunedQwen2.5VL7B avg48.9→50.5、AbsDist37.0→35.9反退。T3OpenVLAOFTavg97.0→97.3，Spatial97.5→97.4/Goal97.8→97.0反退，模拟人口不授真实机器人稳健/规划保证。三个consumer基线与训练数据各异，不能拼成同一无额外训练端到端收益。
- Table4/A1各producer架构、预训练、参数、输入分辨率/native3600 vs196、hiddenwidth等共同变化；生成器/DiT优越或物理inductivebias不是唯一因果。VAE对照已有多数局部收益，不证明去噪激活唯一原因。T5同训练数据/defaultlayer/k的fusion消融：仅generative全项退步；gated并非全任务最优，AddSQA3D61.8>61.3，完整83.2仍<原83.8CIDEr；参数/activecost未匹配不授gate唯一因果。D/A3/A5挑层/时刻，300/l20只部分任务最优，非普遍recipe。
- §4.1/C：GTdepth/pose投影同voxel跨viewcosproxy。实际先同view同voxel平均归一，再跨viewpair加权；validscene mean/std，非所有token独立样本/重复训练CI。主script不剔除zero-depth，无双viewvoxel为NaN。常数非零特征也可cos1：高correspondence不充分证辨别空间结构/物理律。NOS主文“allmodels”与C各组单独minmax归一口径分清，不能将组间NOS作统一可比能力轴。A2VAE79.69cos/NOS77.29也反对唯一DiT因果。
- §5.1：32frames、Adam/batch128/8H100、LLM1e−5/visual2e−6；本文未给足训练seed/重复运行置信范围、推理precision/concurrency/requestSLO完整配置。Fig7同scene特征cache只摊销重复问题，未实际读图数，不采latency数字。§6/F承认memory/inference增加、人工选layer/timestep、室内多view。生成器VAE+DiT前向、驻留/缓存、双projector/gate/下游重训/配置搜索都付费；scene/frame/noise/producer变化须失效，缓存不是freshscene免费或动态闭环deadline。

## actual sole owner 与具体差额

已actual读ROADMAP、PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及当前本日停点/LS路由；Ch23连续表示263–288、Fusion476–537完整局部与Ch22/24开篇交接。

sole `MULTIMODAL-REPRESENTATION`，[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。旧连续表示处理codec/consumer责任，旧Fusion512–516说明early/lategate与promptdependent特征；同modality生成encoder→noisyinput单次intermediatelayer→semantic双支路的producer身份/consumer读出分支尚未具体承载。Ch24拥有完整生成采样，Ch25拥有action-conditioned rollout，此处均不接管；不是按模块名/owner映射造diff。

拟唯一onePRE插当前Ch23原SF2604.02327的earlygate受限案例完整后/“融合点之外，还要核实际可见的模态集合”前（当前516后）。保护旧段和其他family，仅新增本段/static，待root非preparer裁及新窄锁。

## literal one PRE

融合点固定后，也可改变其中一条视觉支路的预训练来源，而不更换原语义encoder：将现有视频经VAE编码，按指定noise时刻扰动，读取冻结视频生成器的一次中间层特征；空间池化和各自projector对齐后，以逐token学习gate与语义支路混合，再交给语言或动作消费者。这是同一输入的两种读出，不是新的独立观察或一段已执行的未来rollout。生成器、输入帧集、noise realization/时刻、取层、池化与gate须共同标识，重复scene可缓存不授新scene免费。[受限VEGA-3D对照](https://arxiv.org/html/2603.19235v1#S4.SS2)中，纯生成特征显著退步，gate也不在每项任务最优；深度位置编码与空间/动作监督仍在相关下游路径，不能将增益写成完全无三维信息、已学会物理律或gate唯一因果。生成器前向、驻留、双投影、下游训练与取层搜索均付费，局部caption、距离和模拟操纵反退须分别验收。表示失配、质量或完整预算回归时，保留原语义encoder、固定融合与专用空间读出，不从中间特征的一致性proxy批准通用三维或真实控制能力。<!-- source-family:SF-2026-ARXIV-2603-19235 -->

## literal 静态末注

- `SF-2026-ARXIV-2603-19235` — [VEGA-3D exact-v1](https://arxiv.org/html/2603.19235v1)必要§4/Eqs3–8、§5/T1–5/§6及A/Alg1、B/C、D/A3/A5、F；2+2+2=6，同输入冻结生成支路noising/取层→semanticgate的producer/consumer差额。保深度位置与下游监督、constant-feature一致性反例/分组NOS、架构预算混杂、puregen与caption/距离/模拟任务反退、缓存及全费，不授完全无3D监督/物理律或真实控制能力；未核代码/复现。

## root 非准备者有限 Source / PRE

2026-10-12实际打开exact-v1 abs身份/题摘/history和DataCite原v1 Updated/create日期，后续v2/v3不混入March采用；必要HTML §4.1–4.3/Eq4–8、T2/3/5与对应解释、Alg1的UnprojectDepthToWorld/3DPosEnc/optional grounding loss、B1三类监督路径、F费用/人工取层/室内限制；实际Ch23 510–528完整early-gate→缺模态/读取交接与Ch22/24入口。原one PRE/static有限PASS：拟6只同一input的冻结生成特征与semantic消费接口，并非物理律、独立新观察或action transition；T5 puregen反退/gate非逐任务最优、T2距离与T3模拟切片反退，以及Alg1含显式几何输入均真实，已近文保留。不以原“no supervision”headline反推能力，不扩读取无关图片/附件或代码，未复现。实际差额并非旧early/late融合原则，Source/PRE通过不等写入/POST/DAY。

## sole writer 实际落实（待 nonwriter POST）

root 授 Ch23 本 family 唯一窄锁后，resume_mar18 按原 one PRE/static 实际写入正文518与本人静态末注1760。写者完整顺读510–532和最后1754–1760，正文及静态注逐字回对上文通过稿；旧early gate、缺模态读取与其他family保留，限定diff-check无输出。此记录只证明实际落实和写者局部检查，不代替非writer POST，不先计本项safe或DAY，不把验收身份写入Books静态注。

## root 非writer actual POST

2026-10-12，root 实际完整读回 Ch23 508–534 的原融合点原则、early-gate案例、新段、缺模态读取与相邻 ICL 交接，以及最后八行本人静态注。新段及静态注逐字匹配已通过 PRE；同输入 noising/一次中间层与独立观察/未来 rollout 分清，depth/下游监督、puregen/gate 非统一改善、切片反退和缓存/完整成本边界均近文保留。未移动旧段，不接管 Ch24 采样、Ch25 transition 或真实控制；实际 POST 通过，释放本 family Ch23 窄锁。可计本项实际整合，不等于本日 Report、来源收尾和 DAY 已验收。
