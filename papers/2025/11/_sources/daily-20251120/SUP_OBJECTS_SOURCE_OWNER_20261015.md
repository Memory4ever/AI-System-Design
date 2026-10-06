# Nov20 SAM3D Objects 必要 Source 与 owner 差额

## 1. 事件、精确证据与采用角色

作者Noether；只补Nov19 BJT。原Meta publication Nov19完整AB/事件已有Ohm§3有效核验，复用不重日期。它已披露human/model-in-loop shape/texture/pose标注与合成预训→真实对齐；不是只有产品名称。精确后稿[2511.16624v1](https://arxiv.org/html/2511.16624v1)原头部20Nov2025，只为原披露路线的必要后补证，不声称下面阈值/triage/全部recipe已在Nov19同bytes公开。原Meta PDF一次native GET零字节SSL timeout，未重试、未冒全文；本轮必要HTML由官方web原文恢复并保存在`SUP_WEB_OBJECTS_CORE_20261015.raw`。没有采用Body后Feb2026正文或扩大两个版本比较。

## 2. 实际必要机制

已实际读§3.1–3.2 L225–285、必要A.2–A.4 L544–574与A.6 Algorithm1/解释 L591–652。人难直接造mesh、较容易在候选中择优，因此先用多模型/检索弥补cold start，随训练当前模型成为主要候选源；选择与质量bar是两步，不把best-of-N等于acceptable。普通标注者只能选/接受/拒绝，不能编辑mesh。Stage2输出selected D+、quality r及less-preferred D-；Stage3再对point cloud做位姿/位置/尺度对齐，形状偏好不自动授layout真值。

每轮训练汇聚历史collection，只保当轮quality threshold以上的selected人口，阈值可逐轮升高；与用D+/D-做preference update不是同一数据对象。关键反侧是当所有候选都不合格时，重复生成→人择优不会产生可训练正例，这部分困难人口会被系统性漏掉。原Stage2.5/A.3将其中部分按complex geometry/occlusion/transparency/small size分类、去重并送专业artist直接建mesh，补生成支持之外的数据，而不是单纯让judge更严。专业数据仍是人工假设/偏好，不是不可见背面的测量真值，也不保证全部长尾已覆盖。

## 3. 实际评价与反侧

实际读§4必要L286–347、D.2 L897–922、E.1 L961–972、AppendixF L1055–1060。SA-3DAO是1K artist从自然图建立mesh，原D.1实际段L895–896说明不可见部位依赖recognition/context/symmetry等假设，完成时间从分钟到数小时；不是全场景物理扫描GT。shape评价先各自normalize再ICP，和layout/接触真实性不同。human preference按图/目标mask随机匿名顺序逐对选，测视觉匹配偏好，不授物理可行/控制成功。没有采用5:1/6:1为普遍胜率。

Table4的累加阶段同时改数据/训练，vIoU从Art-SFT的.2337到再DPO的.2311反退；不能把全指标写成严格单调或全部收益归artist。Table7去MITL/Art/DPO的消融支持这些阶段在该配置有局部价值，但不是等计算/等样本下对“盲区补样”单因素的充分因果识别。作者历史Elo还同时scale pre/mid/post，不能当纯迭代飞轮法则。未读全部recipe/超参/texture附件/代码或复现。

AppendixF明确单对象逐个预测，不训练contact/stability/interpenetration/co-alignment，texture也不知道预测pose；分辨率预算使整身手/脸细节失真。故真实图像重建与人工偏好不变成物理世界状态/安全。这是必要采用边界，不以“AI for Science暂缓”关闭正常多模态/训练机制。

## 4. 评分与唯一 owner 实际比较

拟2+2+2=6：把不可大规模直接生产的3D监督转成候选选择/独立质量bar/失败专业构造，并将D+/r/D-与不同训练消费者分开；跨采集、生成候选与posttraining生命周期，但不为“foundation”、规模或runtime数字加分。具体长期缺口要求深入受影响annotation规则/评价反侧，以上已读必要域，不因6分停在摘要。

唯一owner拟`TRAIN-DATA` Ch27。实际已读开篇/生产链1–43、collection55–112（含既有人工+LM分歧仲裁两完整段）、synthetic分支350–379、evidence-first/coverage482–530和verifier-backed750–779。现有内容已讲采集定义q(x)、human裁决不等gold、生成/验证共偏与人工补coverage；不冒称“书里完全没有人工/闭环”。具体尚缺：**只能在已有候选中选/拒的标注协议无法修补全候选失败的支持缺口，质量bar越严可能继续删掉所需正监督，须另设可直接构造标签的分支，并区分shape选择与后续scene alignment的人口。** 这是协议能力差额，不是缺SAM名字或泛人工反馈原则。

拟最小承载处为collection中现人工仲裁两段之后、Agent原生交互段之前；可用一个自然段解释选择权限→全失败盲区→专业构造/质量与偏好分流。已读相邻Ch26完整1587–1602交接（表示/行动语义→数据生产）、Ch28开篇1–38（数据→训练更新），不将静态mesh改为world dynamics或物理控制owner。当前没有本项Books锁，不写书；先交Ohm实际Source/差额判定。

## 5. 全费用与非采用范围

候选模型/检索/多次生成、逐对人审/quality rubric、失败分类/聚类、专业建mesh、point cloud恢复/对齐、各轮SFT/DPO与评估都计费。A.5标注秒数只是作者该流程平均，不合成全费用倍率或硬件SLO；没有硬件/precision/batch/concurrency的部署结论，未作实现/制品验收。可采人口有限或专业预算不允许时，保留可信真实标注/较窄目标域、固定候选+显式Unknown，不能让相对最好自动升为可用监督。

## 6. 即时交接

请root转Ohm核原机构/后稿角色、上述必要Source/6分和当前Ch27具体差额；不是逐字PRE、root许可、真实保存/POST或DAY。SAM3的Ch23唯一窄锁另按其PRE§7真实保存交POST，不挪用给Objects；S2ST全闭合不重。root96/132不含Nov20；没有共享State/index写入、普通消息或stage/commit/push。
