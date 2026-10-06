# 第十二包：AB7一次准入后的五项必要原源与owner

准入一次决定见V3_DECISIVE_AB7.md；root新准入/本包PRE尚未完成。只对五个已得明确受限增量的原v1补必要方法、控制、直接反侧及实际owner，不追所有proof/code。位置见各V3_BLOCKS_2602.<ID>.md；获取见V3_FETCH_AB7_ONCE.json。未改Books、未计safe。

原abs-v1实际Submitted UTC：22683 02/26 06:55:48、22703 07:28:04、22733 08:15:38、22742 08:29:25、22745 08:34:09，同metadata一致，均晚于前次截点。官方公告下界02/27 09:00+08与same-ID registered UTC02/27 02:52:10、02:52:38、02:53:20、02:53:33、02:53:37的上界（各+1秒后转换+08）形成完全落窗区间；registered只作公开身份上界，不作技术/首公告证据。当前官方轻量状态仅22745 project page，无采用相关撤回信号；看见v2提交不默认重要修订或版本diff。

## 22683 SuperGlasses — 2+1+2=5，AGENT-RAG拟具体Existing

实际31–38/41–55/103–104/118–125/140–146。采用的是Table4 forced multimodal即便保detector/decoupler32.04仍略低direct32.82，adaptive44.10，以及原141–145 modality/tool与对象identity混淆会使查回知识答非所问；不是新RAG/cache组合或smart-glasses声望。Adaptive还加domain/CoT prompting，direct123明确无CoT、简短1–2句，因此direct-vs-full不是纯retrieval因果；sameadaptive的component/forced控制仍支持具体有限判断。Qwen2.5-32B gold-based Boolean judge不等人审真值，1K shortest-edgeresize、双路各5webpages、top10chunks/threshold.6/Q:.6Image:.4绑定实验。评测用对应开源family而非真实镜内未公开模型，不能说已在device部署的performance。Google/Lens、reader、detector、decoupler、reranker、Redis两层均计费，HW/dtype/concurrency/SLO/latency总账Not Disclosed；26models/2422items非生产population。

实际Ch76 71–77承载document/query/answer分别验收、query variant不可由离线排名推出答案效用、visual crop/caption可删关键对象/语义且oracle不在线；153承载**选对对象、handoff、reader回答分别验证**。这些具体正文已覆盖所采用的“retrieval附加收益不能补query identity、不要强制把全部检索当帮助”条件。拟Existing，不为Table4论文名追加正文；若需记录该局部反侧可留Report，不扩大为所有自适应retrieval可靠。

## 22703 GeoDPO — 2+1+2=5，PLATFORM-EVALUATION-SYSTEM拟一段

实际20–81/93–95，只必要score/solver/translator/对应控制。Declarative points/lines/circles/constraints四类multiset，由max-weight assignment与类别F1分别计precision/recall，NL输出经NL2DSL translator后对已知G_true算reward生成pair；明确perception与downstream reasoning两任务、译者syntax与semantic两个误差责任。原生成器solver将几何constraint变loss，优化后以threshold排除unsolved，再render，**求解收敛/DSL来源不自动认证每张可见图语义唯一**；完整“one-to-one canonical”不能据此继承。Point labels须唯一，label identity/multiset及score weights.25共同为EvalSpec，而非任意重命名也同分。

直接子命题争议：95等长约束Eq(d1,d2)第二匹配分支重复F1(d1,hat_d2)，所写formula不对称。取d1={A,B},d2={C,D},hat_d1={E,F},hat_d2={A,B}，原score=1；交换等长两侧d1/d2则score=.5。**隔离此Eq-constraint分支的order-invariant保证**，不替作者修实现、不将整个primitive set assignment/translator机制D。重开需要同predicate精确对称公式/对应实现与test；不遍历其余proof。

Translator Qwen7B rank4/3epochs B32/lr1e-4、4H800，syntax valid100但复杂circles F1降至65.9；模型NL→DSL可错，不以parse success授oracle。Main和translator各10K separate split；DPO rank8/1epoch B32/lr2e-5额外10samples、delta.3pair选择及译者训练，不称SFT等总预算。Qwen圈F1 GeoDPO48.7<SFT57.56、LLaVA点66.98<SFT69.94等保负侧；OOD100 diagrams/MathVista203只局部。精度/总generation token/延迟SLO ND，未核artifact或原图truth。

实际Ch66 1168–1177已有judge取得evidence不等oracle、formal任务优先deterministic verifier及缺oracle邻题间接score，但缺**保持NL外接口、经有独立误差的translator对接order-invariant集合匹配，并把syntactic validity、primitive perception、downstream reasoning拆分**。拟deterministic-verifier附近单段，采用points/lines/circles及对应primitive接口，明确等长constraint子式暂不采用；不把DPO公式复制到Ch66。请求窄lease。

## 22733 Pixel2Catch — 2+1+2=5，MULTIMODAL-EMBODIED-VLA拟一段

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；image center/scale与proprioception、CTDE权限；tracking/grasp分验。2+1+2=5，Ch26自身末注1462；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：§IV–V、blocks31–70/72–83/93；image center/尺度变化与proprioception接口、CTDE权限；SAM2/sim-to-real费用与几何回退。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

实际21–23/31–70/75–99。视觉vector为cx/cy及相邻frame的delta cx/cy/w/h，两帧context；中心+尺度变化只是方向/接近程度proxy，不重建真实3D。SAM2从RGB取得bbox，5pixel扰动不涵盖所有segmentation错误。Actor不拿object3D，**critic和reward拿sim object3D**，trained不等完全无privileged位姿。CTDE两独立policy/value网络，arm residual joint PD、hand joint-target及各自reward/obs与single PPO shared不同，所以不能把全部收益因果归于agent拆分。两A6000/512envs/3seed sim，实际30throws/object；UR5e、13active Allegro、D435、ROS2/30Hz、120Hzphysics decimation4。

Only-center sim catch81.27/80.72但real13/3/23，full84.13/84.83与real63/43/43；tracking real only-center57/54/54与grasp差距说明tracking不够。Only-WH real0也显示尺度proxy不能单独给方向。MA单policyreal33/20/20是package对照不是冻结reward/网络容量的唯一拆分因果。所谓zero real finetune仍先做真实joint trajectory system identification，再随机动力学/噪声；SAM2、硬件校准/识别、训练和在线分割+control有成本，latency尾/dtype/SLO及精确trial CI ND。仅三对象/单手臂，不授动态抓取通用安全；丢目标/scale不稳就重观测、保留state estimator/controller/停机。

实际Ch26 53–69说明explicit calibrated3D与implicit interface各自条件，固定camera/稳定coverage可留implicit；已有view-policy visibility≠task success，但没有**pixel方向+尺度角色、sim center-only强却real稳定抓取退，以及actor/privileged critic分账**。拟显式geometry后、主动view前单段，保implicit分支而不取代原3D路线。请求窄lease。

## 22742 ProjFlow — 2+1+2=5，MULTIMODAL-GENERATIVE-PARADIGMS拟一段

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；SPD graph metric的clean-endpoint投影；可逆条件、foot/text质量反侧。2+1+2=5，Ch24自身末注1768；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：§3–5、blocks50–70/97–119；SPD图metric的clean-endpoint投影；Gram可逆条件、foot/text质量反侧和非物理保证。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

实际44–71/97–119/212–217/219–223。在已知线性equalities/Gaussian observation noise下，以SPD R为metric作clean endpoint correction；R由骨架graph Laplacian+lambdaI，lambda正负责translation null modes可逆。Hard Σ=0还要求AR^-1A^T可逆（如A独立rows）或另有合法pseudoinverse/consistency处理，原普通inverse不能授任意冗余/矛盾constraint exact。固定clean端点修正后的混noise recomposition与下个velocity求值分开，zero-shot不是不付projection/inverse费用。线性观测等式可精确保留，不认证非线性contact、不等式、物理关节限位或sampler全posterior。

HumanML3D/ACMDM-S-PS22、control1/2/5/49/196keyframes均值、known orthographic camera pitch/yaw/scale，100ODEsteps、R weights10/ridge1、dynamicmask10→3、soft interpolated pseudo observations与hard originals分账。Table3 exact errors都0而EuclidFID1.152/no-noise3.429/plainmask.880/full.097，是核心质量条件。Table2 full footskating .146/.139坏于Sketch.103/.102且text Rprec.748/.764低.802/.796，2D reprojection0不等3D真值或更自然everymetric。singleA100/196frames1.84s平均，ControlNet同100steps但others1000/10+optimization不同预算；dtype/batch/tailSLO ND，不认证通用最快或real actuator readiness。

实际Ch24 151–157已有proxy barrier/QP、可行tube、Taylor残差和latent→pixel constraint不自动精确，尚无**清洁端点linear observation投影的metric会在同exact误差下改变realism，topology耦合不认证真实动力学**。拟该采样约束链一段，给已知可逆线性合同；失败回原sampler/显式condition及独立validator，不重复Ch26执行安全。请求窄lease。

## 22745 SpatialAlign — 2+1+2=5，TRAIN-DPO拟一段

实际26–96，仅参考噪声正则/对照与reward直接反侧，不读A4全理论。GroundedSAM bbox中心方向/归一distance→SSR，起止均值加transition gap→DSR proxy；filter只有one animal+one object且>=20frames可检出，invalid不进pair。500prompts每10seed产生训练样本、test120每5fixedseed；pair label只看threshold.7，不直接用score continuous值。Wan2.1-1.3B、text-projection/cross-attention KV LoRA rank16、81frames480×832、B48/lr1e-4/2400steps/4RTX4090、beta1/refnoise lambda.25，参考forward、视频生成/追踪与valid过滤成本全需计。

所写Eq3不能仅由SSR∈[-1,1]授DSR∈[0,1]：LEFT→RIGHT、start LEFT1/RIGHT-1、end LEFT-1/RIGHT1、起止窗均值分别1，两个gap2，.125×6+.5=1.25。**隔离0–1归一化/概率解读**，不替作者修score或据此宣布作者code错误。有限threshold指标仍只是作者所定义proxy，不授真实physical truth。Blur/复杂scene detector错/漏，only三关系与两实体，不能generalize任意DSR。

PureDPO可同时恶化winner/losernoise-fit只保相对margin；SFT noise-target anchor更稳却饱和，reference-noise一致性anchor对w/l各付两项正则，非硬KL或完全function preservation。Table3 800steps/500train/30test中SFT-anchor correct.333高于reference.307，但CLIP-IQA .6549低.8594、identity .7317高.6754，不能全指标胜出；主Table2 identity/CLIP-IQA/IQ均略退baseline。VLM reward .147低同subset baseline .180，为直接反馈失配反侧；几何reward .307也与自己的proxy evaluator共享盲区。阈值.8更correct却更差natural/identity，回退校准reward/原reference与可信训练目标。

实际Ch34 171–175有raw preference margin不能被relative loss遮蔽、reference标签/forward/caches边界；244–253有diffusion proxy labels、consistency residual surrogate但无**geometry-label生成的pair中reference noise-output anchor与SFT实际noise target的不同，以及proxy正确提升和视觉/identity反退并存**。拟253后DPO系统复杂度前单段，以这一训练objective差额为唯一owner；不在Ch24再重复同段，不采错误score范围或“avoids reward hacking”保证。请求窄lease。

五项拟四个I+一个具体E，均待root必要源/owner PRE；六项once里的22698 EX同样待独校。不因局部式错误自动整篇D，不把这些准备材料算日级完成。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22703：原必要blocks32–45/48–60/93–95及采用相关prepared控制/反侧与actual owner独核；Ch66正文1198/完整1184–1221/own5669 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
