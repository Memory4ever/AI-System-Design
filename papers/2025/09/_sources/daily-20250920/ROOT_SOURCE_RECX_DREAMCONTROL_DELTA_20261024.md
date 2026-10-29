# RecXplore / DreamControl：决定准入后尚未读的必要差额

作者249确认下列新增域尚未开始，root明确接受后复用已有唯一CORE，没有新GET。原题摘、最小决定N、日期和原5/6分复用，不第三；root只首备新增必要域，Aristotle唯一另一角色回该原域实际采用后，Einstein仅角色复用。owner与README仍归作者，不预Books结果或日级完成。

## RecXplore — 2509.14979v1

[精确版本](https://arxiv.org/html/2509.14979v1)，[既有HTML](REPAIR_20261024_CORE_14979v1.html)/[请求](REPAIR_20261024_CORE_14979v1.html.request.json)：UTC2026-10-24T08:24:28.772548至08:24:32.222811，200/exit0，274101B/SHA256 `e29db1e385c2922c57c1bed03c4cdc42bda0afc63ee2c34eaf22928d6e424c3b`，root实际复算bytes/hash相合。

root新增实际读§3.1/3.2/3.4、§4.1 Dataset/Evaluation、§4.2与§4.4 Setup/Analysis、§5。HTML将已读N的表1–4嵌在Evaluation段、表5–6嵌在Analysis，结构化提取时文本亦完整可见；不把这次附带显示当独立第三审表/重算原N或扩大范围。未代码、实验复现/线上推荐验证，也不重读作者已成的§3.3/3.5及全部后续N组。

**新增机制/评价条件。** 属性可直接拼接，也可交额外LLM提关键词、摘要或扩知识；特征encoder可冻结，或PEFT/LoRA作CPT、SFT、SCFT或CPT+SFT，输出通过mean/max/末token或EOL聚合。适配后交SASRec消费，更多语义处理不自动提供新事实/更好读出。知识扩写可能引入与商品实情不符的先验，不能把自产属性当外部观测。作者§5明确逐模块greedy选优可能错过全局组合，且只研究SASRec，不授跨所有consumer的最优配置或任意representation上MoE总优。

Steam与Amazon Beauty/Fashion/Games四数据集按LLMEmb预处理。评价每个目标只与100个随机未交互items比较，HR/NDCG@5/10不是全目录、曝光/真实用户或业务收益；未交互也不等真实负偏好。作者给seed42/43/44三次均值，并说std≤.002所以省略，不能把未列逐格方差/配对差方差补成CI或全部显著性。所有阶段配置/负样本/划分和搜索权限须固定；本域未明示更细切分与LLM预训重合，不自行补假设，也不无证指控泄漏。

§4.2称复杂增强无益/简单最优是过强概括：已成表中Games关键词优SAC、Fashion摘要也局部优SAC。§4.4称任何FT显著全面优冻结亦须收窄，Fashion SCFT H@10 .5740低冻结.5832；CPT+SFT Beauty N@5 .3633低CPT .3679、Fashion N@5/N@10 .4680/.4887低SCFT .4819/.4980，不授每指标最优或独占domain-first因果。表2/6既有适配器×ID融合反转是本次贡献的直接条件证据，但需要训练容量/不同预处理/选点费用分账；更多模块后较高总分不分摊成独立贡献。

**完整费用与退路。** 作者已成N记录8L20/硬件、base配置和实现可复用，不重读以凑标准必要。额外LLM属性制备、CPT/SFT/SCFT全部试验、全item编码/重编码与缓存、PCA拟合/转换、adapter/SASRec训练、各ID融合与greedy搜索、三个seed/独立真实效果回归均计费。离线编码不等全系统免费或只需在线小网络；本域无完整GPUh、缓存更新/失效费用、precision、在线并发/尾延迟/SLO，不推净吞吐或降本。消费者/数据人口变化时重新校准融合×adapter；保SAC、固定encoder、较简单adapter、原ID路径或不融合等已验证工作点，不把单人口榜单变通用架构结论。

## DreamControl — 2509.14353v1

[精确版本](https://arxiv.org/html/2509.14353v1)，[既有HTML](REPAIR_20261024_CORE_14353v1.html)/[请求](REPAIR_20261024_CORE_14353v1.html.request.json)：UTC2026-10-24T08:31:46.547042至08:31:50.588884，200/exit0，441438B/SHA256 `f1e0e8f4c15f8dd5aee9b736721b8c5130f2910da22552f5f0f3125d05bfe3d1`，root实际复算相合。

root新增实际完整读IV-C/IV-D/表III、V、VIII-B/C/表X与Pick专门修形式、IX-A/B/表XI、IX-D/表XII。原III-A/B、IV-A/B与TI/II属作者已读N，不第三。未动作视频/曲线像素、代码、VIII-D专门部署细节或全部11任务附录，不将未读域或当前演示当实验复现/执行认证。

**从可生成到可跟踪仍有必要筛选。** VIII-B明确生成器不考虑全部场景碰撞，也产生动态不可跟踪轨迹；按躯干角、pelvis高度、全身碰撞作任务特定过滤。表X每100条Pick保67、Punch100、Kick66、Press96；除drawer/door的手臂优化分支外，实际只人工挑一条训练，自动规模化仍未来。过滤通过不是独立动力学可行证明，更多数据可消除过滤只是作者推测。VIII-C补20帧（10静止、10插值）到固定起点、冻结无关手臂；Pick因1.32m机器人与1.74m SMPL的平台高度差，又以关节优化约束手到自由空间，仍可能其它部位碰撞后被删。印式中的约束不是全部关节/接触/动力学安全保证，不补成已核通用solver或无人工流程。

**实机不是原privileged policy直接迁移。** IV-D明确重训：删reference observation/root线速度/质量摩擦等privileged输入，仍在reward使用参考，并加time encoding。同reward不等同一个policy或零额外RL。G1 27DoF（腰只yaw）、两Inspire手各6DoF却只二值开闭，IMU与D435i/OWLv2估目标相对pelvis位置；2D检测+深度+object-specific offsets不是生成轨迹自行对齐真实坐标。因OWLv2延迟，**仅首帧检测后固定估计**，多数交互任务冻结下半身并罚root速度，bimanual例外。不能从selected Pick/Press/Drawer/Punch/Squat展示推动态目标持续重定位、任意物体几何/灵巧手、真实闭环通用能力；视觉policy蒸馏、skill组合/复杂几何仍未来。展示未给足试次/失败分母/真实对照或SLO，保有限作者观察。

**自然与任务成功分别验。** IV-C FID参照由HumanML3D关键词筛任务；Pick FID ours .320差于TaskOnly+ .240，作者用身高/动作域差解释，未独立证明唯一原因。Jerk为1000 trajectories×500steps×41keypoints的平均三阶位移读出，低jerk不签接触正确或安全。40人随机左右视频偏好支持本选择集的主观human-ness，非1000独立人标/一般用户/独立物理成功。表III Pick85%、Press82.75%、Punch92.5%、Kick82.5%、Jump95%是作者有限偏好，不补每人完整票数/CI。TaskOnly+的dense reward本身按趋近参考body位置构造，非完全不给参考的公平空白baseline；reference/任务reward/权限变化需分清，原TI/II反侧保持不重审。

IX-A actor/critic各MLP(512,256,256)、同观察非asymmetric；IX-B摩擦U(.7,1)、各任务质量范围不同，randomization不证明任意真实质量/表面覆盖。所有motion prior预训/采样、retarget、碰撞筛除/人工挑选/修形、scene构造、任务reward/训练和实机特定重训、OWLv2/深度与标定、低层PD/二值手动作、全部硬件/环境、失败尝试/独立几何与任务验收均计费。作者N已成A6000/48GB、每任务2000iter/8192env仅该训练配置，不授真实执行性能；precision、总GPUh/电费/人时、检测延迟数值、端到端分位SLO未披。场景、映射/感知或动态支持不合时，保可信轨迹/传统运动规划、独立控制安全与真实状态反馈；不把未实现的持续视觉/自动筛选/skill组合写作现成退路。

以上新增必要事实已足以限定两项拟采用命题；原分数/日期、现有反侧均保留。无root网络/exec在途；等待唯一另一角色实际采用，不直接标标准Evidence或Books完成。
