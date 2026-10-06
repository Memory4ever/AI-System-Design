# 2603.10158v1：跨手型冻结 codec 的必要Source与PRE

仅03-13补充03-12 BJT自然日；准备者mar13_supplement，非Books writer。实际增量准备，不授formal/写后验收/DAY。

## 原件、身份与采用范围

Cross-Hand Latent Representation for Vision-Language-Action Models / XL-VLA；[完整v1题摘](./SUP_ABS3_10158.raw)与当前唯一v1/header无可见撤回纠错，Comments只指project网站、不含具名venue早稿。DATE3 Mar12正常公告批次下界+registered同日/ arxiv.content/findable上界日级夹证与准入§19有效复用，不以Submitted10或Updated定公开日；不授全网没有更早稿。

官方精确[原响应](./SUP_CORE_10158.raw)，URL https://arxiv.org/html/2603.10158v1，GET200/397533 bytes/2026-10-10T04:20:38.664175Z，见[manifest/result](./SUP_CORE_10158_MANIFEST_RESULT.json)。实际必要阅读完整§3.1–3.2.2/Eq1–4、§4.1–4.2完整T2–5及直接§5、Appendix6.2–6.4/完整T6；§1/2只核问题与对照边界。Figure4/5/6/7/17只读必要正文与caption，不认证尚未视觉曲线的每格成功率或动作视频，未读代码/复现/其他手型旧文献。

原约束：不同手指数/自由度下把raw joint token直接拼给共享policy，容易混淆动作接口。新增：用本体关节范围随机姿态训练各手MLP encoder/decoder，以重构、FK拇指–手指pair距离/方向及KL塑形共享latent，再冻结codec交VLA输入/输出。需重新考虑的是先生产什么action接口、部署按哪一手型decoder消费，而不是共享code自动取得物理动作权限。

## 必要方法与实现资格

§3.2随机从硬件joint limits采样，不读teleoperation示教或paired跨手轨迹；一个source latent同时self-decode及cross-decode至目标手，jointly优化所有手头。L1重构原q-pos，L2对FK pinch距离/方向加权，L3为Gaussian posterior到standard-normal KL。手指对应**人工**对齐，四指Paxini省略little-finger pair；无需paired标签不等无需joint-limit/kinematic模型/对应关系。β1e−5、λdis2000、λdir5、weight exponent12及最终latent32为本配方，不据KL同分布认证语义完整无损或物理动作安全。

§3.1 VLA继承π0/PaliGemma；将上一已执行动作chunk经该手encoder形成latent history/state条件，vision+language+action expert预测下一latent、由hand-specific decoder回native joints；fine-tune VLA时所有E_h/D_h冻结，handID只选codec、不显式送backbone。动作chunk64帧/20Hz（3.2s）已披露；§3.1把chunk写为一次编码，而§3.2的MLP按joint-position vector定义，两者time packing/encoder逐帧或整体的精确recipe未明，**不签唯一可执行张量实现**。本次采用生产/消费分责不依赖补造这一细节。

## 关键正反与费用

- 主T2四手×十任务，raw shared π0与XL-VLA同multi-hand数据，Mean row/column实际baseline .32、XL .72；Ability .37→.73、Inspire .27→.68、Paxini .35→.78、XHand .29→.70。Ability PushSugar .30→.30持平，不采“每手每任务严格改善”。§4.1正文说全均值.55→.90实际与T2最后PC列相同、不能替全表mean，不由此否定有限表结果或推造假。
- T4 latent replay两手组 .60/.61→.82/.81对LAD，支持本四手映射的有限动作重放，不证任意hand semantics；“无监督数据”只指codec阶段，本VLA仍2000demonstrations/2M state-action、10task/每手每task50demonstrations。
- Fig4的zero-shot是已训练codec的手×heldout task组合；各手VLA训练剩余任务；π0+RT只XHand全部tasks训练，几何retarget至其他手，人口与训练范畴不同。只保有报告的有限迁移，不认证未训练新手型/任意任务，未核未视觉格数字，不读所有视频来授“never underperforms”。G1只Inspire，T6四task .525→.825另人口，不证所有组合/硬件。
- T5 removing L2两项后reconJoint3.781/Tip2.602较full5.476/3.703更好，却pinch-dir62.733/random-dir71.765明显更差；这是recon不代cross-hand几何的直接反側。latent128某些指标改善，不采“维度增大皆退步”或唯一capacity因果。FK/pinch、continuity noise.05及linear interpolation accel/jerk是几何proxy，不覆盖contact-force/碰撞/可达/全部closed-loop结果。
- App6.2 L515/tabletop vs G1 chest两视角不同，crop960×540→320×240→224×224；App6.3每setting仅10real trials、固定同手初始joints、随机objects；PSR只heldout，部分推进与全成功另计。8H10080/60Ksteps/batch128约10h为policy条件；codec预训练总时账、完整teleop/标定、deploymentprecision/latency/batch/concurrency/SLO均Not Disclosed。几何codec输出仍joint proposal，不授contact-safe或3.2秒无需重新观察。

## 三维与actual唯一owner

拟 **2+2+2=6**：D2新action生产接口随机pose/FK跨decode→冻结codec的具体替代设计；Reach2跨codec预训练、VLA监督与部署hand选择的两个消费者阶段；Durability2为可复用的本体schema/producer-consumer边界，**不借Gaussian VAE、通用安全controller或39k/数据规模原则抬分**。已确认具体长期gap触发受影响必要深入；方法/主评价/反側够即停止，不预设所有窄P深审。

唯一owner `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际完整局部25–42接触迁移与latent goal、90–125校准/canonical25维接口→privileged3D、289–299共享手部几何start–goal码本与native-action head，以及ActionChunk/控制提交边界。现canonical25只统一arm/TCP/jaw几何，shared hand skeleton码本依human/robot start–goal transition监督；未有随机joint-pose/FK跨decode的**独立预训练codec**与VLA latent-state条件/next-latent的冻结消费路径。不是只按手型题名映射新owner，也不新增Ch23/Ch27重复推导。已重读PROJECT_CONTEXT/LearningPhilosophy/WritingGuide，现有有效分支保留。

拟在canonical25接口两完整段之后、Privileged3D标题之前窄整合以下两段，待非准备者Source/owner/PRE通过后root窄写；**无自行Books写入/锁占用**。

## 逐字PRE（两段）

不同多指手型还可以共享学习到的动作坐标，而不先复制整条关节轨迹。直接使用原生 joint space 在单一手型中清楚、无需额外 codec；跨手混合训练时，关节数和指长差异则要求先声明生产者与消费者。一个受限分支从各手的 joint limits 内采样姿态，用手型专属 encoder/decoder 重构自己，同时让同一个 latent 经其他手的 decoder 产生姿态，以 forward kinematics 的拇指–手指距离和方向对齐它们；Gaussian regularization 只塑形分布，不认证动作语义相同。这个阶段不需要成对跨手示教，却仍依赖人工手指对应、kinematic model 和本体范围。训练 VLA 时冻结这些 codec，以已执行动作的 latent 作状态条件，预测下一 latent action chunk，再由当前手型的 decoder 返回原生关节命令；hand identity 选择 codec 而非显式送入共享 backbone。<!-- source-family:SF-2026-ARXIV-2603-10158 -->

冻结 codec 能让 policy 复用一致接口，不使未适配的新手型自动可执行。所谓 zero-shot 只限已有 codec 的手型与未训练任务组合；随机姿态重构和 pinch 几何也不是接触力、碰撞或成功的替代真值。必要对照中去掉跨手几何约束可改善自重构却显著恶化跨手方向，因而应分别验 codec 重构、目标手几何和真实闭环任务；有限四手/十任务与少量实机试验不签任意本体、安全或无退步保证。Codec 预训练、kinematic 标定、示教、VLA 训练和部署解码都付费，时序打包与 decoder revision 应和 action schema 一同冻结，完整控制 deadline 不能由局部训练时长推出。目标手无有效 codec、几何失配或反馈不足时，保留原生 action policy、显式 retarget、较短 chunk 重新观测与独立 controller/停机接管，不让共享 latent 授权物理提交。 [必要方法与反侧](https://arxiv.org/html/2603.10158v1)。<!-- source-family:SF-2026-ARXIV-2603-10158 -->

独核若发现具体已有覆盖或评分增量不足，可按真实原件作NC/最低判，不为书稿数量维持提案；当前未自授任何formal/POST/DAY。
