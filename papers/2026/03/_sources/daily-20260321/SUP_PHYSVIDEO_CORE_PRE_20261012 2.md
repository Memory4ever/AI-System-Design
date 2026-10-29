# PhysVideo18639：多视前景与单视背景消费的责任边界

resume_mar18 sole准备，仅03-21补BJT03-20自然日；既有有限题摘/root准入独校复用，不扩query。本文是exact-v1 PhysVideo，不拿后来重命名OrthoPhys的方法替换本窗。此packet尚非非准备者Source/PRE通过，无锁未写、不计safe/DAY。

## 身份、日期与具体准入

原件[PhysVideo exact-v1](https://arxiv.org/html/2603.18639v1)，v1完整题摘见原SUP_FINITE_REMAINDER_EXACT_AB_20261011.json。actual v1 HTML题名及八作者与初始稿身份匹配；当前官方abs题名OrthoPhys、v3，仅轻量核header/history，所见无明确撤回/纠错或必要先公开venue信号，不比较窗外修订。officialhistory v1Submitted03-19T09:03:06Z、v2May25、v3June2；真实DataCite10.48550/arxiv.2603.18639为findable，created/registered03-20T02:17:24Z、v1Updated03-20T00:44:43Z、Available仅2026-03，currenttitle/version不是v1精确标题。沿本批BJT03-20日级公告/注册夹证有限归属，不把submitted/月份当精确首次公开，也不证明互联网没有其他先稿。

旧单视生成难把前景运动与丰富背景同时绑定→v1生成带物理属性条件的正交前景，再只取原视角转为光流交背景生成器→多视条件的消费边界必须在压缩接口重新验收，不由前景跨视约束签发完整背景视频的几何/物理证书。拟新增命题2+2+2=6，跨几何条件生成与外观生成的可复用替代分支；不以成熟“视频非真实物理”原则给DD3。

## 必要Source：支持、关键评价与直接反側

实际v1 §3.1–3.4/Eqs1–17（HTML L105–209）、§4.1–4.3/Tables1–4（L210–272）、§5必要应用/§6/Impact、App.A.1–A.3文字与关键Figcaption（L336–348）、C数据构造（L355–358）与E限制（L364–368）。支持和关键反证足够即停；未读全部应用图像像素、附录D完整prompts、code、可选artifact或复现，不授生产/实机执行。

1. 第一阶段由静态前景mask与图像到3D先验准备多视输入，沿时间复制静态前景并向条件分支注入。速度/加速度、密度、弹性与泊松比等属性通过condition tokens进入生成器；camera embedding和预测深度关联的跨视attention bias配合时序attention。属性输入并不保证输出满足参数值或真实动力学，预测depth/3D先验也非观测真值。
2. §3.3明确VideoSyn只抽四视结果V4中的原视角V1，先做帧插值再估光流，由flow-conditioned视频模型生成含背景RGB。最终背景模型不是同时消费四视视频，也不继承完整3D场景或硬物理约束；光流只能保其二维可见运动信息，插值、估流与背景合成都可能失真。这项明确producer→representation→consumer接口可单独核，不把一般“两阶段”术语当贡献。
3. 必要训练分工：Phys4View以10K对象构造40K四视序列/160K视频，TaiChi MPM与3DGS及mask/depth proxy制备；背景VideoSyn另用OpenVid/WISA数据。两个训练人口不同，物理合成训练支持不自动传递到真实背景或域外对象。
4. 两处中心recipe疑点明确不采用。Eq7直接比较不同view的camera-frame三维点，所写表达式没有将二者转到共同外参坐标；pose embedding本身不证明这些距离已物理对齐。Eq16把绝对归一化相关写为depth loss，若以正权重直接最小化则同向/反向相关为1、零相关为0，方向不支持正文一致性解释。只隔离原式、无误差保证及严格几何/物理主张，不自行修公式或暗补实现。交非准备者判上述单视光流消费接口能否独立采用；未通过前不写Books，也不因争议降分/删反证或假NC。
5. 评价是33个合成RGB测试视频/作者属性设定与GPT-4o物理proxy；训练8×A10080GB、推理单A100，720×480。未披露完整精度、batch/concurrency、SLO、重复seed/CI及全部pipeline walltime。Table1的flicker等并非完整分支全指标最优；Table4逐步加模块不是全部变量/预算匹配的factorial因果实验。§4.2 prose物理分数与表中不同数值不强行合并，A.3借用judge提示及旧人类相关声明不认证本33人口新的人审真值。四视/物理条件、cross-view/temporal attention与训练差额不可据均值唯一归因。
6. 原C说明背景无法完整360渲染，所以数据以前景为中心；E明确复杂动态/丰富背景及不可见视角几何仍可失败。它们直接阻止“完整场景几何受控/任意物理视频”的外推。mask/3D先验、sim/depth标签、两个模型训练、多视采样、插值、flow估计和RGB采样全部付费；单A100不签发实时、低费或闭环世界/机器人安全。

## Actual sole owner / 邻接差额

`MULTIMODAL-GENERATIVE-PARADIGMS`/[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。actual完整1588–1638已顺读：相机/时间控制、CameraMotion阶段条件→Motion Forcing预测depth后RGB消费→稀疏运动及对象参考→3DreamBooth→后训练。Ch23/25交接沿本日已实际读且未变化结果复用；本项不把生成条件提升为Ch25 persistent world state或Ch26实体执行。

现1622/1624实际已有depth producer与RGB consumer、训练clean/部署predicted depth和两条loop费用；却未覆盖“多视foreground最终仅取一个view转flow→background”的条件信息压缩与分阶段测量范围。拟在完整Motion Forcing段后/现1626控制信号前one段，不覆盖旧深度分支，不新增完整geometry recipe。

## One literal PRE（待非准备者裁）

中间条件的表示还可以在两阶段之间改变，而不让后续外观分支读取全部几何状态。一条受限路径先在多个正交视角生成带物理属性条件的前景运动，再只抽原视角、做帧插值和光流估计，将二维运动交给另一个视频生成器补背景与RGB外观。这把多视前景与最终场景分责，也在接口处丢掉其他视角的显式信息；速度、材料属性或跨视attention只是前景生成的条件，不能由单视光流批准背景的三维一致或物理参数遵循。[有限生成对照](https://arxiv.org/html/2603.18639v1)仅支持该表示交接，不认证跨视距离公式、深度loss方向或完整场景物理保证。mask/3D先验、模拟标签、两模型训练、多视采样、插值与估流都增加费用，属性、几何和最终视频须分别验收；复杂背景、遮挡/新视角、估流或训练支持失配时，保留直接I2V、明确运动条件或真实多视监督，不把更逼真画面批准为World Model转移或机器人动作。<!-- source-family:SF-2026-ARXIV-2603-18639 -->

拟本人静态章末注：

- `SF-2026-ARXIV-2603-18639` — [PhysVideo exact-v1](https://arxiv.org/html/2603.18639v1)，必要§3.1–3.4/Eqs1–17、§4.1–4.3/T1–4、A.1–A.3/C/E。仅多视前景→单视插值/光流→背景RGB消费及分阶段费用/支持边界；不采用Eq7跨camera距离recipe、Eq16正相关loss方向、严格3D/物理遵循或实时保证。33合成测试/作者GPT-4o proxy非实测参数/新独立人审；复杂背景和不可见视角反側保留。未核代码、图像像素或复现。

交root一次非准备者必要v1/date/actualowner/onePRE/static裁，不要求遍历附件；未获锁前不写，必要审阅完成标签不等于safe/DAY。

## 实际 writer 写后（待非writer POST）

收到root非preparer必要Source/date/actualowner/原literal/static有限PASS及soleCh24窄锁后，原one PRE逐字落实正文1626、本人静态注2479。作者实际完整1614–1637和末八行/本人及邻注顺读：原depth producer→RGB consumer之后接foreground→单视flow→background，随后旧稀疏运动/对象参考分支；保Eq7/Eq16recipe隔离、属性/几何/最终视频分账与费用/回退。与原literal/static逐字一致，限定diffcheck0；不修改其他family或书注人员身份。交root一次nonwriter actualPOST，不先计safe/DAY。

## root 非准备者有限裁（2026-10-12）

实际打开 exact-v1 HTML header/八作者、§3.1–3.4/Eqs1–17、§4/T1–4及A/C/E必要段，并轻量打开当前abs/history；当前七作者的v3不替换八作者v1，也不比较窗外版本。沿用本批已独核日级公开夹证，只确认03-20归属，不由提交时刻伪造首次公开。§3.3的V4→V1→插值→flow→VideoSyn接口可独立限定；Eq7缺共同外参、Eq16相关正loss方向与原支持不一致，均不采用为完整recipe或严格几何证书。T4逐步增模块与33合成/GPT-4o代理不批准因果唯一归因、实测物理参数或生产实时。

实际完整Ch24局部1612–1632及ROADMAP唯一owner，之前Ch23/25未变交接复用；Motion Forcing深度消费与该多视前景经单视flow压缩不是同一条件接口。逐字one PRE/static准确说明丢掉其他视角显式信息、分阶段费用及复杂背景/遮挡反侧；6分必要Source/date/owner/PRE有限通过。作者获sole Ch24本family一段及静态末注窄写，写后交root一次实际完整局部/本人末注POST；尚不计安全处置或DAY。

## root 非writer实际 POST

实际顺读Ch24完整1614–1637及末八行，包括新1626和本人2479/邻注2477。新段及本人静态注逐字回原literal，保留depth→RGB旧分支、多视前景→单视flow→背景新消费分支及后续稀疏条件；其他视角信息损失、复杂背景/遮挡、分阶段费用、Eq7/Eq16强recipe隔离与回退近文清楚。有效原证复用，不改其他family静态注；有限actualPOST PASS，root接纳并释放Ch24，可计实际整合，不授DAY。
