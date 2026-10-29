# StereoWorld17375：校正双目生成的条件块与受限读取

resume_review17_18，2026-10-11，仅03-20补03/19。root与resume_mar17明确sole准备；原本日批6/独核§17准入与2+2+2=6、自然日夹证有效复用。恢复实际重读AGENTS、适用Research/Report合同、Sources每日/arXiv主题、统一Prompt、ROADMAP及Books约束、本日README/STOP。只准备本packet，不自授Source/PRE/safe/DAY，不写Report/LS/Books，不扩发现。

## 1. 身份、日期与必要原证停止

当前[official abs](https://arxiv.org/abs/2603.17375)完整AB/Comments/history实际读：v1唯一，Submitted03/18，未见具名撤回或纠错。日期复用本日Batch6精确DOI identity、created03/19T02:30:41Z/registered42Z与官方ID可公开下界/公告夹证；03/19北京时间自然日成立，不把Submitted或项目页推荐时间作首公开，不追时分秒。

实际[exact-v1](https://arxiv.org/html/2603.17375v1)必要§3.1–3.3/Eq1–9 L106–171、关键§4.1–4.5/T1–5 L174–247与§5限制、S1.1–1.2 L338–357（数据/注意力计费）、S2.3 L390–404仅长程速度/退化、S3–5 L405–423直接预算/可变baseline/场景一致性反侧。图只读正文/图题，不冒像素结果；未读VR人评全图/案例视频、代码、全references、旧修订。支持和直接反侧足以准备下面有限接口即停。

## 2. 实际接口与不采用的强桥

输入是已rectified的左右RGB及baseline、K/T相机轨迹、文本，Wan视频VAE分别编码左右latent，DiT联合去噪。相机条件不是renderer显式深度目标：保留原视频时空RoPE块，在Q/K新增camera通道，以K与T合成的矩阵作用该块，避免直接重参数化全部原位置通道。Eq8相机矩阵相乘使用transpose，P包含非正交intrinsics；它不是自动相对SE(3)逆变换或任意坐标gauge不变性证明。本文称新子空间orthogonal只可作分块结构，不作统计独立或物理几何保证。Eq7原视频块也有Δ与单token记号混用，不拼精确实现recipe。

新增Qcam/Kcam都zero的bilinear相机项需要解释梯度启动；主文承认训练更难，却不足以凭初态相同认证全网络训练等价。Copy temporal weights支持受限训练起点，不保证无扰动或唯一最优。这里只采旧时空块与新增相机块分责，不采用zero/copy的执行配方、通用稳定或更快收敛定律。

完整左右×时空联合attention昂贵。对已校正双目，分别做每个view内部3D时空attention，再在同一时刻、同一水平行内做跨viewattention，两路结果相加；这是基于水平epipolar prior的读取限制，不是full4D算子的等价分解。未校正、垂直视差、非标准rig或occlusion不能由同一行匹配自动解决。Eq9分支归一化/融合尺度需连同实现验收，不授任意相机通用/对应无损。

双目RGB可先生成再用stereo estimator取disparity，已知focal/baseline时提供度量深度候选；本文没有depth监督不意味着无需metric camera标定，也不意味着生成对本身有真实depth。S4只定性示0.25→0.75m轨迹中约0.42m有效，不能由此宣布任意baseline鲁棒或排除image stretching所有替代原因。S5明确无scene-levelconsistency约束，路牌会凭空出现，训练以静态rendered为主；jointstereo不是persistent真实地图。

## 3. 评价、反侧与完整费用

Wan2.2-TI2V-5B，49帧480×640，20ksteps/batch24/24H20/lr1e-4。T1混合Stereo4D真实动态11718/0.063m、TartanAir6433与Ground58168/0.25m静态render、DynamicReplica1686/VKitti230varying；S1筛掉少motion/jitter并用left captions。主文测试435pairs，S1约280Ground+160图像来源随机轨迹（约440），人口口径分开，不造准确同分母。条件pose与metric训练标定属特权，并非实时自主感知。

T2采用VGGT估pose、GIMmatching等生成代理；作者基线训练数据不同，mono/stereo自有对照S3宣称同parameter/compute，但未给完整逐component计费trace，不据此认证额外view免费或唯一camera块收益。Ours0.49FPS对DeepVerse0.35并非>3×，单个高速基线不能拿摘要倍率概括所有；T3flickering93.63低于Voyager94.55/background92.42低于SEVA93.01，保反退。Stereo生成后disparity质量只定性，DROID只是生成manipulation视频，不是实机policy成功/安全闭环评价。

T4表头CLIP-F↓/TransErr↑与T2方向冲突，不采用精准跨表统一质量recipe。T5两CLIP-V列重复，其中first与T2CLIP-F位置相应，不冒唯一指标mapping；stereo attention较4D的CLIP-T25.43<25.74、两相似列97.05<97.55/96.63<97.50，MatPix4.52/4.51只是代理，保质量取舍。S1理论计算的是attentionhead乘加，约3.115e10→1.561e10，不包括所有QKV扩维/FFN/VAE与sampling；FPS.34→.49也不等全费用减半。主文长视频5.6FPS与S2.3的5FPS不统一，4stepcausal蒸馏改变模型/输出且长程退化，不能合并成同质量、30Hzfreshdeadline。

推理hardware/precision、batch/concurrency、采样步与所有camera/深度估计/解码费用、seeds/CI、tail/SLO Not Disclosed。训练GPU不是推理平台。一次强桥请求：原init与相机块实现、rig/rectification及baseline失败协议、匹配完整预算的各分支质量与端到端时延、场景一致性与真实闭环评价；缺这些不排除有限接口、不授物理真值/安全/严格实时。

## 4. actual sole owner 与 literal PRE（待非准备者）

实际读Ch25开头、完整431–487 camera/worldstate→Verse几何payload→joint/objectidentity→historymemory及698–712 referencepacking交接；Ch23 nativegeometry queryview/标定adapter有限1048–1070与Ch24/26开头相关交接。sole拟 `MULTIMODAL-WORLD-MODELS` Ch25原444 Verse限制完整段后、位置持久化/可开合对象前。现有Verse是显式pointcloud/μΣrenderer条件；Ch23是token几何表示/投影族adapter，均没有预训练视频位置块保留+双目几何条件与横向读取的生成选择。只此生成接口，不在Ch23重复相机表示或Ch24复制denoising算法；不创建benchmarkowner。

几何也可以只约束生成条件，而不先提交一张持久真实地图。对于已校正的双目RGB，保留预训练视频的时空位置块，再给Q/K增加由相机标定与pose条件化的独立通道；左右latent共同去噪，但相机条件一致不认证生成内容是真实几何。跨视图读取可再限制为同一时刻的水平行内attention，与每个view内部的时空attention相加，用已知epipolar prior换取较小的attention集合。这是受限rig上的替代分支，不是full4Dattention的无损分解，也不保证未校正相机或任意baseline成立。<!-- source-family:SF-2026-ARXIV-2603-17375 -->

[双目条件与读取范围的有限对照](https://arxiv.org/html/2603.17375v1)仍有生成质量反退和场景物体凭空出现；由生成对估计的disparity只提出深度候选，不给persistentstate或controller真实状态权。扩展Q/K、双viewlatent、训练、sampling、解码与几何评价均付费，attention乘加减少不等全部生成成本减半，蒸馏后的FPS也不认证新观测deadline。标定、rectification、遮挡或长程一致性失配时，保留显式RGB-D/几何renderer、短段观测条件生成与新观测校正；需要持久对象或物理行动时，仍交给独立state更新与真实闭环验收，而不是让双目自洽替代它们。<!-- source-family:SF-2026-ARXIV-2603-17375 -->

静态注：

- `SF-2026-ARXIV-2603-17375` — [StereoWorld exact-v1](https://arxiv.org/html/2603.17375v1)必要§3/Eq1–9、§4/T1–5/§5、S1及S2.3/S3–5直接预算/长程/场景反侧。仅保留视频位置块的附加相机条件与rectified双目同刻横向读取；保非等价full4D、init/矩阵实现未认证、标定与深度候选、质量反退/无场景约束和全费边界，不授任意rig、物理控制、全费用或实时保证；未核代码/复现。

准备交resume_mar17非准备者独立必要Source/actualowner/原两literal与static，不自己授PASS或先写Books/DAY。

## 5. 非准备者必要 Source/actualowner/PRE

resume_mar17独立实际读exact-v1 §3/Eq1–9 106–171、§4/T1–5 174–247与§5 248–251、S1.1–1.2 338–357、S2.3 390–404/S3–5 405–423；actualCh25 431–487及698–712、Ch23 1048–1070和相关交接。两literal PRE/static逐字有限PASS，原6分/date复用；旧视频位置块保留+附加相机块、rectified同刻水平行与view内attention相加，确有生成选择差额，不同于Verse几何renderer载荷或query-view表示。不授full4D等价、物理真值或任意rig。

独核P含K故transpose不自动等SE3逆；两zero的bilinear项初态梯度启动未认证，原有限PRE不采用init recipe。Table4方向/5重复表头不擅补mapping，CLIP-T/相似列质量反退、head乘加仅局部且row算子细节需实现匹配、0.49 vs0.35非概括全baseline三倍。DROID只生成视频，S5明确无scene-level约束/路牌出现，baseline外推与5/5.6FPS口径分开。S1约440与main435人群分账及全fee边界准确。未读VR全图、人评像素、视频/代码/旧史；支持和关键反侧够本接口即停。交root协调Ch25原Verse限制段后两PRE/static窄锁，未写/POST不计safe或DAY。

## 6. root 窄锁后实际 writer（待作者一次 POST）

root接纳author非preparer§5并明确授reader唯一Ch25本family原Verse限制完整段后两literal+静态注。reader实际现有433–452及末注邻接读后，逐字写446/448与static1761；完整433–465 camera/worldstate→Verse载荷限制→双目条件/受限读取→joint/objectaddress及末1753–1761本人/邻注实际读回。scoped本family diff仅两正文+注，diffcheck无输出。原PRE/static不改命题，无身份流程更新；交resume_mar17一次nonwriter实际POST，不自授POST/safe/DAY。

## 7. 非writer实际POST

resume_mar17实际完整读Ch25 433–465与1753–1761本人/邻注，逐字回有效Source/两literal/static。新446/448接Verse载荷限制后、joint与objectaddress前；原semantic marker与既有几何状态不改。附加camera条件/同刻水平行是生成proposal非persistent真实地图，质量/场景一致性/全费与controller分责近文准确，静态末注1761无过程身份。限定diffcheck0；一次nonwriter有限actualPOST PASS，交root接纳释放Ch25，未授DAY/不重复核心。
