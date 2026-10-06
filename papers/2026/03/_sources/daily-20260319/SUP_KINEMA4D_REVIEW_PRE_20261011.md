# 03-19 Kinema4D 16669：必要证据与最小 PRE，待非准备者裁决

准备者 resume_review17_18；root 本日具名授权仅准备本 packet，不写 Books、Report、LS，不自行授 Source/PRE PASS、safe、写锁、POST 或 DAY。原准入 2+2+3=7 保持，不因慢、局部反退或已有关联 owner 降分/排除。恢复后实际独立重读 AGENTS、完整研究/Report 合同、统一 prompt、ROADMAP、Sources 使用/每日与 arXiv 主题、LS 路由及本日 README/STOP/独核；Books 背景三文件完整读。只本03-19补03-18自然日，日期夹证有限复用本日已核准入，不以 submitted 时间替首次公开。

## 1. 身份与实际必要范围

[exact-v1 HTML](https://arxiv.org/html/2603.16669v1)；[current official abs](https://arxiv.org/abs/2603.16669)。同六作者、题名和完整AB；当前仅v1，Comments为项目页，实际轻查未见撤回/具体勘误。HTML first 实际读完整题摘、§3.1–3.3/Eqs1–2、§4.1–4.4/Tables1–4、§5限制；为拟采用分工定点补 G.1实现/归一化、G.2 robot extraction/validation、G.3部署及 H 的相关对照/TableVI–VII。没有核全部定性图片点、视频、project/code、其他版本或实验复现；HTML顺带返回references不作证据审阅。

## 2. 支持的接口与不得补造的保证

§3.1：重建robot mesh分段并对齐URDF joint anchors；EE Cartesian pose通过IK且用上一步joint作seed，已有joint angles直接输入，velocities则积分。FK传播各link，再由camera内外参投影为像素对应XYZ robot pointmap。已知mesh/URDF/pose/camera下这是名义运动学几何条件，不包含力、摩擦、碰撞接触或执行误差解算；unknown robot重建/标定错误仍可能污染它。

§3.2：initial RGB沿时间补齐，与robot pointmap沿width拼接，shared VAE编码；input/noisy latents及robot occupancy mask沿channel拼接，shared RoPE与domain embeddings对齐RGB/pointmap，shared decoder输出完整world RGB/XYZ。10%机器人占据区域mask设.5，原文明说让生成器修正robot visual signal。故“environment-only”是设计分工，不是输出robot像素/XYZ永远硬锁或精确执行的证明。G.1又在完整robot trajectory上取min/max归一化，再用训练5000样本的latent统计作constant normalization；不能把生成XYZ直接授为米制物理真值，归一化也不一般证明所有affine变换不变。

§3.3/G.2：201426 episodes混合DROID/Bridge/RT1与LIBERO，真实几何来自ST-v2 pseudo annotations，LIBERO由native depth/camera backprojection。G.2明确真实pseudo geometry不是submillimeter GT。训练robot-only condition由whole trajectory RGB SAM2 mask提取pointmap；训练可用future motion监督，不能把它说成线上未知未来输入。LIBERO加噪6DoF动作、gripper不扰形成position/reaching失败；不授覆盖各种真实接触失败。49frame切片/下采样不自行证明所有视频物理频率相同。

§4.3/G.3：真实YAM6DoF通过手工base↔reconstruction刚体标定、读取实时joint encoders并FK重建轨迹，执行Diffusion Policy之后生成相应反应。此处支持已执行轨迹的回放比较，不独立证明仅部署前command就能得到完全相同的action realization，也不验证模型参与online闭环或counterfactual candidate搜索。完整序列的normalization可来自给定名义候选，未来logged encoder序列则只能用于回放；不能静默混成无泄漏的部署输入。

## 3. 评价支持、直接反侧与预算

Wan2.1/4DNeX14B，LoRA r64，batch32，AdamW peak2e−5、5000iterations/32A100约2天，480×720每modality/67GB每GPU。text encoder condition用robot VAE latents替换，原conditioning仍有initial world RGB，不把去instruction称完全无场景语义。预训练和真实demo成本不消失；“无real fine-tune”限定新YAM/实验室测试，不是没用任何真实数据预训练。

G.2验证集3200（2000DROID/1000Bridge/100RT1/100LIBERO各50success/failure），原声明严格从训练排除可保留为作者协议。主文“2% of201426”与3200并非同数（约1.59%），不照录精确2%也不猜剩余样本或证明全部baseline同预算/无关联轨迹泄漏。不同conditioning/output/backbone及训练人口的外部baseline不是机制唯一归因；内部替换也只支持所测接口对照。

T1 FID本模型25.2差于Ctrl24.9、与IRA25.2相等；T2 temporal CD-L1 .0074差于Tesser .0067，不能称全指标领先。T4 RGB+pm的PSNR22.98高于仅pm22.50，但FID25.7/CD.0495反而差于25.2/.0479；mask50% FID25.0、mask20% CD.0433较default强，softmask不是所有指标唯一最优。扰动条件仍有各指标退步，“robust”不等无误差。single-domain/mixed变动人口/预算，不由单项消融推出所有embodiment泛化因果。

T3两套各3scenario/每项50trials。模拟GT .48/.38/.80→prediction .56/.46/.84；真实GT .34/.46/.78→prediction .60/.76/.90，高估26/30/12百分点。三成功率近似或qualitative near-miss不足验收逐trial failure detection、ranking、calibration或physical safety；未披露配对混淆矩阵/独立成功judge细节/seedCI，不由N50说已统计显著。§5明确没有rigidbody/friction显式约束，可能违反守恒/穿透，必须与几何控制同处保留。

H/TableVI “add env pm” CD .0420较default .0479好，与“没有收益”概述不一致；真实成功prediction .70/.82/.96相对同GT误差36/36/18pp更大，不能由此普遍排除环境geometry。nulltext FID25.6优于该表Ours25.9；Ours FID25.9与T1/T4 25.2不同，不跨表合并。full-scene noise为作者解释不是已识别独因。

H/TableVII单A100：本模型15min/56GB，Ctrl2.5min/15GB，Tesser10min/31GB。不是实时controller，不换算为fresh sensor deadline；表中time具体计量batch/denoise steps、precision/完整runtime、I/O、concurrency/SLO、重复与全部重建/搜索/训练费用未齐。G.1 mesh15sec/A100是作者重建局部，不等全simulator15sec或低端可部署。跨DROID→Bridge结果有受限质量优势，不由此授开放世界动力学正确或全部系统收益。

## 4. actual sole owner 与具体差额

实际读 Ch25完整169–223（action schema→ego/residual→module/encoder drift→SimDist→goal cost）、1170–1198（tactile/transfer→action realization/environment response→知识交接），Ch24/26开头前22行；[sole MULTIMODAL-WORLD-MODELS / Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。现1186/1188已有controller/kinematics→robot renderer→environment response及标定/authority边界，不能宣称它缺少一般分责。尚缺具体robot trajectory pointmap共享codec条件、可修订mask与联合RGB/XYZ输出、sequence-normalization身份及已执行回放/未知候选输入的边界；这改变如何把显式几何condition交给生成器及如何验收，而非新增论文库存。与183通用schema、193 ego-residual或Ch26最终动作authority不重复。拟在现1188后、该family marker2607-22535前加入以下两段；不重排或覆盖原有效正文。已有其他根在同章写入时须以最新actual邻接再定点确认。

## 5. 两段最小逐字 PRE 与静态来源注（均待 root 非准备者核）

动作实现与环境反应的分工，可以通过像素对齐的几何条件落到生成接口：先把给定joint trajectory或可求解的末端姿态经URDF运动学传播到各robot link，再用相机标定投影为逐帧robot pointmap；initial world RGB与它共同编码，生成器联合提出环境的RGB和XYZ序列。这里精确的是给定模型与轨迹下的名义几何，不是接触、摩擦或实际执行结果。机器人占据mask还可保留局部软区，让生成器修正重建噪声，所以最后生成的robot区域也不是永远硬锁的真值；完整轨迹归一化后的XYZ条件不自动带来标定尺度或守恒保证。<!-- source-family:SF-2026-ARXIV-2603-16669 -->

显式几何减少了生成器猜动作的负担，却增加mesh重建、URDF/相机标定、轨迹展开、共享codec与联合去噪费用。已执行轨迹的joint encoder回放应与部署前名义候选分开：未来实测状态不能偷偷成为未知分支的输入。有限真实pick-and-place中，生成结果的成功率仍高估实机；较好的画面或pointmap相似度也不能排除穿透和守恒失效，且所测单卡生成明显慢于比较基线。条件漂移、物理失败诊断或deadline不可验时，保留显式simulator、短horizon真实反馈与可信controller；world model只提交待验证的环境反应，不接管第26章的动作提交和安全权限。<!-- source-family:SF-2026-ARXIV-2603-16669 -->

静态注拟原文：

- Kinema4D：[exact-v1](https://arxiv.org/html/2603.16669v1)，必要§3.1–3.3/Eqs1–2、§4.1–4.4/Tables1–4、§5及G.1–G.3/H TablesVI–VII。URDF/FK robot pointmap条件、软mask和联合RGB/XYZ生成的受限分工；真实成功率高估、sequence normalization/pseudo geometry、已执行轨迹回放与名义候选分验、统计物理失败和非实时/全费用边界保留。未核代码、全部定性附件或复现，不授物理安全/开放世界正确性。

## 6. 待裁与停止范围

root非准备者独核（2026-10-11）：actual exact-v1 §3.1–3.2/共享codec与soft-mask、§4.3/Table3、G.1归一化/训练、G.3已执行编码回放、H/TableVII必要成本及直接反侧已读；actual Ch25 1183–1205动作实现/环境反应和交接已顺读。7分保持，具体接口可与physical certainty/headline隔离，SOURCE/PRE PASS。root仅窄写两段及本人静态源注；为保原2607-22535正文绑定，将新段放在其原marker之后、知识树交接之前（相同论证位置）；中英文空格及静态注“统计物理失败”改为“物理失败”消歧。未授actualPOST/safe/DAY，非writer须读实际完整局部与本人末注。

必要支持与反侧已足以送非准备者裁：拟受限整合，隔离physical certainty、严格米制ground truth、未经实证的counterfactual/closed-loop无泄漏、通用embodiment或zero-shot安全/实时保证，不因这些headline限制EX/假NC。不自行预支Source/PRE通过；root若认为分工受中心输入接口影响须扩大暂缓，应指出具体依赖，保留上述原证与7分。若以后拟采用候选评估/失败校准或性能保证，只一次定点请求部署前condition取得及normalization协议、配对success/failure判断/人口与完整timing budget；无需现在遍代码或所有附图。当前只packet准备，Books未写、无actualPOST、未计safe/DAY。

## 7. root写后非writer实际POST（resume_mar17，2026-10-11）

复用§6有效非准备者Source/PRE批准，并定点实际回对exact-v1 §3.1–3.2的URDF/IK/FK、投影、shared codec、soft mask与联合输出，Table3真实成功高估、§5守恒/穿透限制、G.1序列归一化、G.3标定/joint encoder及H/TableVII成本；未重开全部原证、图像/附件或实现复现。本人实际顺读Ch25 1170–1223动作实现完整前后及知识树/Ch26交接，1745–1756本人静态注与WorldCam、SimDist、DreamPlan相邻注；另实际Ch26 1–29确认action/controller/safety authority。

新1194/1196两段与有效PRE一致（root声明空格规范/静态“物理失败”消歧），原2607-22535 marker及已有绑定正文保持在新增之前，不误将Kinema接口归给原family。给定模型/trajectory的名义几何、软mask可修订robot区域、完整序列归一化非物理尺度真值及已执行回放/未知名义候选分账准确；真实success高估、画面/pointmap非守恒证明、生成慢于基线与全部重建/训练/去噪费用近文，不把提出环境反应升级成动作提交或安全权限。自身源注只保来源/必要范围/未核边界，没有流程身份循环。一次局部actualPOST PASS，可交root接纳并释放本family窄锁；不改Books、Report或LS，不授本日DAY。
