# 10340 CGVD：运行时视觉删改与静态补景缓存的必要Source/PRE

仅补充2026-03-12 BJT自然日，第二包精确v1完整题摘/窄准入与arxiv日级夹证复用。官方 https://arxiv.org/html/2603.10340v1，`SUP_CORE_10340.raw/txt`及manifest/result GET200、149012bytes、UTC2026-10-09T15:43:07.884380。作者实际读III-A–G全部方法/Eq1–6、IV-A–E全部关键评价/TablesI–III、V–VI直接限制与结论；图只用正文/caption，不采用未读像素值、attention因果或完整曲线数值。没有核代码、复现、真机或无关引用。

## 新增命题及三维最低投入

预训练VLA可能把语义相近背景当目标，重训或只裁掉视觉tokens各有成本→本文在原policy观测入口先构造safe/distractor分路并交叉校验，再复用一次补景/当前robot像素→需要验收的是**视觉删改的保护集合、生成背景的时效与物理几何/控制责任**，不是SAM3或LaMa模块名称本身。拟`2+1+2=5`：具体输入删改/缓存有效性重要接口2、局部policy视觉frontend1、可复用观测资格2。不借成熟segmentation/inpainting/缓存原则或physical safety概念另抬分。必要方法、关键对照/反侧与actual owner已读，拟两段长期受限接口差额，触发深入；待非作者Source/PRE，不提前计确认候选、整合或POST。

## 实际机制与身份

III-B deterministic解析instruction的target/anchor；safe概念还有robot，distractor是给定可能clutter的semantic categories，没有额外LLM API，不是自主发现全部障碍。III-C SAM3独立channels把目标/anchor与distractor masks分别并集；vision encoder仅initial t=0一次，masks复用全部frames。

III-D Eq3的g为safe confidence减IoU>eta的最大distractor confidence，保留负值；Eq4按`(1+g*)sigma*`选**唯一最高connected component**。作者称正/负值genuine/imposter，只是模型分数规则，不证明真实目标身份，空IoU匹配与阈值具体值未披露。不认证实际实现对全部对象完备/错误无害。

III-E masks阈值.5后二值、膨胀distractor减膨胀safe，rs≥rd提供检测集合上的buffer，**保护的是实际safe mask而不是所有真实目标**。III-F LaMa同时抹掉Minp与初始robot膨胀mask，形成每episode只算一次的背景。III-G subsequent frame以Gaussian-blurred alpha将live图与cache混合，再用当前robot像素覆盖；仿真明确使用SimplerEnv **GT robot mask**，真机“ SAM3 can achieve similar”是推测，不是实际真机评价。

该wrapper只改视觉输入，不改变真实clutter/动力学/碰撞几何。复用初始masks/cache不等跟踪或重观测，误删真实target/anchor、top-component丢目标或inpainting改空间线索都可影响动作；这些是原方法与作者V/Carrot负侧支持的工程推断，不能据此称已发生全部物理碰撞或模型造假。

## 关键评价、代价与直接反侧

IV-A作者比较π0/GR00T，但未给具体checkpoint revision、部署hardware/precision或完整control-stack时序；不自行补N1.5。SimplerEnv单WidowX、fixed third-person camera，Bridge两任务spoon→towel/carrot→plate；RoboCasa/YCB collision-aware grid的semantic/random/attribute distractors。各task/count 10seeds×20episodes=200，baseline/CGVD matched seeds；没有置信区间/原paired结果，不因200就授统计显著。

IV-B/C carrot中moderate clutter本身帮助baseline，CGVD在该情形持续较差，作者明确有用visual anchors被移除与补景破坏几何。TableI attribute低clutter非单调，1个distractor simple78<80、complex69<74；不是所有形态/属性都受益。TableII仅π0/spoon/18semantic clutter：base43/full77.5/mean-color56.5/no two-layer65/no robot protect73。这个有限消融支持对应模块/输入选择，但不能由局部attention图证明全部收益唯一来自“feature dilution”，也不授模型无关全部policy适用或严谨goal preservation。

IV-E TableIII initialization4914ms；执行base317ms/CGVD421ms，增加104ms约32.8%。正文称negligible/nativefrequency，表注moderate；不采用可忽略总费用或原生控制频率保证。若将串行耗时倒数换算只是推断，非实测吞吐/完整闭环Hz，本包不写成测量。初始化segmentation/inpainting、per-frame compositing/robot mask、policy、communication/controller均须计费，未披露硬件/流水重叠/机械时钟不能授SLO。

V static background假设明确，distractor移动使cache desynchronize，real-time mask更新又高频成本过大；carrot形状/空间伪影退步保留。原文把SAM3/LaMa曾在真实图片训练等同sim-to-real风险只剩policy，是未获本研究真机证据的强桥接，本包不采用。结论“efficient prerequisite for deployment”也不授普遍必要条件；无clutter、需要真实context或mask不可靠时原RGB/explicit geometry路径仍合理。

## actual唯一owner与具体差额

唯一 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际完整47–115的frame/calibration→真实观察vsvirtual rerender→canonical body normalization→training-only teacher/runtime geometry交接，536–558的sensor/belief/proposal/controller职责与memory freshness完整局部，以及755–779 sim-to-real/control budget完整局部已读。虚拟view只重采已观测RGBD、canonical分支移除robot以统一embodiment、teacher只训练不是当前**episode初始safe/distractor补景cache+live robot合成**；现文不承载本稿具体输入删改/GT来源与static资格，不能仅主题近似授已有覆盖。Ch25只拥有真实环境transition/world-state，Ch27只接训练数据，运行时视觉删改仍Ch26一个owner。

拟在Ch26现“主动选择视图还要区分真实取证与同一观察表示采样”完整段**之后**、“统一空间frame还不足以统一不同手”段**之前**插两段，不打断原标定/真实观察论证。未请求自己写Books；非作者核过后请求root该两段窄锁/写入，再实际非writer POST。

### 逐字PRE（未写入）

视觉预处理还可以改变 policy 的输入，而不改变真实环境：当语义相近的 clutter 分散目标识别时，一条受限分支从指令得到 target/anchor，将它们与 distractor 分路分割，再用重叠区域的置信差与 connected-component 选择收窄目标 mask；对 distractor mask 减去受保护 mask 的区域补景，并在缓存生成时移除初始 robot 区域。初始场景一次生成并缓存，后续混合当前画面与旧背景，再以当前 robot 像素覆盖，保留视觉本体线索。这不是重新取得环境证据，也不移除物理障碍；保护范围取决于实际分割，模型分数不能认证“真实目标全部保留”。原 RGB policy 与显式几何控制仍是合理基线，输入删改只给 action proposal，不接管 controller 的提交权。

这种缓存把 segmentation/inpainting 成本前移，却把初始 masks、生成背景、指令和当前观察的对应关系变成有效性条件。[CGVD 的有限仿真对照](https://arxiv.org/html/2603.10340v1)在部分语义 clutter 中受益，但 carrot 任务存在退步，作者将丢失有用背景或生成伪影列为可能解释；仿真 robot mask 来自 GT，不能当作真机在线感知已验。4914ms 初始化与317→421ms执行耗时也不支持“可忽略费用”或原生控制频率保证。移动 clutter、相机或目标变化会使缓存失配，补景像素更不提供碰撞几何；系统应保留 raw observation 与删改/cache identity，重新观察、重建或回退原视觉/几何路径，并计入分割、补景、混合、policy 与控制全费用，不能让干净图像或局部成功率签发物理安全。<!-- source-family:SF-2026-ARXIV-2603-10340 -->

## 精确停点

必要Source/actual owner与校正PRE已由mar13_admission_review直接独核通过，root实际按校正两段窄写Ch26。5分必要深入整合的实际POST如下；强target保证、唯一feature-dilution因果、完整真机迁移/原生frequency/部署必要性隔离；如拟采用这些命题，只重开GT→在线mask、动态freshness/碰撞geometry、matched budget与实机反馈原证，不请求无关全附件。

## 本作者非Books writer实际POST

本作者只own本日Report/day_sources，没有写Ch26；root实际写入后直接顺读当前Ch26 65–81完整局部（calibration fallback/activeview→virtual rerender→新73/75→canonical hand与TSDF），不是只看diff/提案字符串；再读当前2119–2125末注、root 10340本人2123记录。当前前后链完整保留：同一观察的虚拟表示与当前输入删改分支相接，不把干净图当新几何/真实障碍消失，也不打断原canonical hand论点。

本次回源定点III-F Eq6/III-G、IV-B Carrot作者解释、IV-E TableIII与V全部直接限制；本turn此前实际III-A–E/Eq1–5及IV-A–D有效复用。新段准确包含distractor减protected与初始robot并集补景、cache后live覆盖，safe只检测集合；Carrot措辞是作者可能解释而非唯一因果、GT/费用/静态cache/真实controller/fallback近文。自身末注尚“POST待审”不自授完成，新段未引入普遍真机/geometry/安全或原生控制频率保证。

**actual非writer POST通过**：两新段、完整前后局部及本人末注对回必要v1一致，root可只同步本人note为此POST并释放该两段锁。作者同步正式结果仍等待root确认末注；不改Books、不授DAY/代码/复现。
## root末注同步与正式状态

root已同步本人Review note为实际非writer POST通过并释放本两段窄锁；作者直接回读当前Ch26对应完整末注确认。Source/校正PRE/actual窄写/非writer POST层均通过，Report正式同步受限整合，不授日报DAY；不重复已核原件，也不写共享Books。
