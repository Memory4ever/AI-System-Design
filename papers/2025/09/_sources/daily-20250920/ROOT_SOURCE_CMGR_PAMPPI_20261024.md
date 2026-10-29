# Sep20补Sep19：CMGR与PA-MPPI首次有限必要证据

作者201明确两必要域尚未开始/无CORE与请求在途，root本轮明确接受后唯一capture与首备。AB123/联合日180/各2+1+2=5复用，不改旧候选日期、分数或窗口。准备者到此；Aristotle唯一另一角色回具名必要原域实际采用，Einstein随后只复用已闭角色链，不第三Methods/评价。本包未给Books决定/写授权或DAY。

## 原件和实际读域

- [CMGR exact-v1](https://arxiv.org/html/2509.14958v1)：[raw](ROOT_CORE_CMGR_14958_20261024.raw)/[request](ROOT_CORE_CMGR_14958_20261024.request.json)，GET 2026-10-24T06:24:03.002839Z～06:24:05.820603Z，200/exit0，379847B/SHA256 `a5b45d4d9ac2c1b474b511b087d7a449ab25a79d2236ead10858686120b7b3e5`。实际完整§3/式1–9、§4.1–4.4/整T1–3/F3–6必要文字caption、§5。未核附加supp/图像素、实现或复现；图只采用明确文字，不当三维几何或因果证明。
- [PA-MPPI exact-v1](https://arxiv.org/html/2509.14978v1)：[raw](ROOT_CORE_PAMPPI_14978_20261024.raw)/[request](ROOT_CORE_PAMPPI_14978_20261024.request.json)，GET 2026-10-24T06:24:55.702476Z～06:24:57.536265Z，200/exit0，207466B/SHA256 `2e5051e467466d38a1e433f33e9ee3645c27c121ae189873d172601db518857b`。实际完整III–VII/式1–2、整TI–II及必要F2–9文字caption/实验说明，不冒像素、视频、实际飞行/代码或复现。

## CMGR14958：中层跨模态接口与增量分类分路

### 机制及解释权限

SAGR用point-cloud表示作Q、选层的2D/depth表示作K/V做cross-attention，其余层self-attention；CLIP中层选择Lr={0,4,8}，不是最终text向量单次对齐。训练另将attention矩阵大权重按MR阈值置零，比较masked/unmasked表示的batch内相似度矩阵。Eq3在softmax权重上置零，未写重新归一，不补成pre-softmax hardmask。大attention权重不自动是几何无关项，关系矩阵一致也不认证逐点三维对应、完整partonomy或语义真值。

TAM从point feature产生[0,1]^3颜色，给多view depth图白背景中满足9x9全白邻域的像素填色，再以text特征对齐并加一条CLIP图文logit。它适配CLIP输入分布，不是从投影恢复未观测几何，也不是保自然纹理；学到背景颜色本身可能被读作分类线索。深度/点/中层特征shape、投影及CA对齐映射和视角数未完整闭合，不私补可运行recipe或无损接口。

BND保存base network冻结副本，用每base类别一个exemplar与新类数据另训binary classifier，按h=.1把测试对象路由base/novel网络；原Net继续增量训练。显式保旧资产不同于保证整套系统不遗忘：gate错分、特征漂移、阈值校准与两路logit比较仍影响全类结果，独立训练并不自动免过拟合。Eq9把hat y称logit却直接用于log概率、sigmoid接口未显式；§3.4 task-specific Ct logits与§3.1所有已见类别统一评测的完整交接未披，不补实现。是否完全并行执行两路与先gate再单路不在本文闭合，保两资产和所有可能编码费用，不按“parallel”授吞吐。

### 直接对照和失败边界

Recon point extractor、depth配置沿FILP3D、CLIP ViT-B/32；Adam/weightdecay1e-4、base10epochs/增量20、lr1e-3→1e-4 cosine、BND每阶段另10epochs/lr1e-3、MR.9/Nsa2、单RTX3090/b16。precision、seed/CI、完整冻结/训练参数集、视角数与总训练/搜索/驻留费ND。大多数baseline引用C3PR已报结果，FILP3D另按当前类数复跑；不能称本研究逐方法同预算重训。

S2C base39+novel50、M2O26+11；S2O设置先称44/11，后称15novel/三组5，T1列44→49→54→59即15。明确人口不齐，不私修样本或迁评价。各阶段microaccuracy类集合变化，DeltaA是相邻总体accuracy的绝对相对变化均值，不是固定old-class遗忘率；上涨也计变化，不能据其独自证明没有旧知识遗忘。

T1 S2C final66.3>FILP57.1/AA78.6>70.8，支持有限整套配置收益；但DeltaA3.2劣C3PR2.8，且不同baseline base准确率83.6/91.4已不同，不能唯一归因中层prior。T1 M2O base93.3低FILP93.6。T2 M2M最终65.9低C3PR70.9/Microshape67.1，DeltaA8.7劣6.2/7.9，AA79.8较高不能抹反侧；S2S DeltaA1.2仍劣Joint1.1。不采全场景稳定防遗忘/Joint严格上下界。

T3 baseline AA72.3→full78.6是6.3百分点，完整三组件整体最好，但V1在第三阶段84.8<baseline85.5、TAM单项个别阶段退步，组合优于单项也有V4 39类91.4<V3相同/非严格、V5 44类87.2<部分单项等反侧；不把平均增益写逐任务必胜。几何/文本身份与分类准确率是不同验收，T-SNE/attention着色没有提供真实三维对应或唯一因果。

全部point/depth/CLIP历史预训、多view渲染与颜色网络、中层对齐/masked双路训练、base副本/每阶段BND与exemplar驻留、择层/阈值搜索、旧新类独立回归均付费。§5承认CLIP空间prior可能不足以覆盖强遮挡/可变形体；错误prior、gate失准或质量/预算不合时保独立点模型、原多view/末层融合、base资产与有标注增量回归，不以few-shot或分类均值授开放场景/物理控制安全。原5/候选与所有反侧保持，具体owner另做。

## PA-MPPI14978：目标proposal不等可达动作，感知也进入控制成本

### 感知—地图—rollout—执行路径

模型或用户给goal pose，本方法以已有深度和camera pose构建Octomap，将free/occupied/unknown三状态转定界occupancy grid，再用机体动力学对加噪控制序列做Monte Carlo rollout。cost包含goal/yaw、control大小/变化、进入occupied或unknown的有限惩罚，以及朝向goal/沿ray遇unknown frontier或直接见goal的奖励。探索的是已知free内能扩大视线的位置，不是让机器人直接飞入所有unknown。

MPPI按累计cost的指数权重平均候选control序列，执行首动作，再shift/interpolate warmstart；不是policy gradient/训练大模型，也不是foundation model理解硬件API。输出collective thrust与body rates，lowest-level controller跟踪，motor clipping只管该限制，不给全轨迹或碰撞可行性。动力学、世界/机体/相机坐标、pose、地图分辨率与更新年龄、rollout与实际执行反馈共同决定消费者资格。

两种步长分开：prediction .1s、control .02s，H15即名义1.5s规划、N10000；重复warmstart需要按control时间shift而非每步删整prediction节点。终端hovering只软惩罚，正文无递归可行安全集证明，实测csafe=0；有限collision cost也不是硬禁区证书，nonconvex场景中平均controls不自动保留各候选几何性质。

印式定义d_goal=p_WB−p_goal，却以r(t)=p_WB+t*d_goal称到goal的ray，因此r(1)=2p_WB−p_goal，朝向点积方向也有同一约定冲突。保此未闭接口，不替作者改号或据此宣未核代码一定错误，亦不把它写成可执行导航recipe。zero-distance归一、grid边界/机体体积与误差margin未完整明确；姿态/感知/地图资格要另验。

### 实验究竟排除了什么

核心是**hardware-in-the-loop**：motion capture给真实quadrotor state，Flightmare据对应pose渲染depth，意在排除深度噪声与定位误差。真实机体执行不等所有传感器、障碍或collision都是开放真实环境；NoMaD两个Matterport scene也在该实验框架内，不能授野外depth/SLAM/真实门洞安全。平台JAX/Agilicious、i7-13800H/64GB/A1000 laptop6GB、机体.21kg/臂19.4cm/TWR6.8，不能泛称任意edge机器人。

controller50Hz、depth30Hz、grid10Hz、4x4x2m/voxel.1m三个不同频率；ray tracing仅每第10个预测step以省费。没有完整sensor-to-actuator worst-case/分位数/丢帧deadline验收，50Hz不是所有状态新鲜或无碰撞保证。

baseline不只去perception项，还把goal cost换成4s minimum-jerk直线reference tracking；故PA与tracking总体差额不隔离新增perception term的唯一因果。C-wall每难度5次、hole五位置各两次，样本少，不给种子/CI或大规模成功保证。TII Cwall2m baseline0→PA100与hole1m50→100有局部优势，不能写所有case“提高100%”：4-wall1m baseline成功80/碰撞20，而PA成功40/碰撞60；Cwall3m PA成功60/碰撞40，hole.5m成功80/碰撞20，仍明确失效。

正文已承认PA进入occupied平均4cm、simulation重复不出现提示简化动力学gap；不能把soft罚、thrust clipping或“safe action policy”名称当安全证据。VI明确需要好初始观测，Cwall例先人工转±90°看外侧free，缺该初态不继承成功。改LIDAR仅future建议，不是已测无代价替代；当前只定界局部导航，长horizon/foundation中间waypoint未来验证，两个NoMaD例不证全部目标可达。

全部depth/pose与标定、Octomap累计/转grid、每轮10000x15动力学/代价、DDA ray、warmstart同步、真实控制反馈与人工初始化、所有失败trial和独立安全/质量回归均付费；端到端能耗/完整时延分布/复杂地图扩展/安全SLO ND。地图陈旧、定位失准、无可行候选或预算不够时保可信低层限制、短horizon重观测/停止/人工接管及更明确planner，而不由模型目标或平均成功自签physical commit。原5及全部正反侧保持，具体owner由writer新层判断。

## 交接

本两项首次有限必要首备已完成，无root GET/exec在途。Aristotle只回上述必要原域作一次实际采用后接owner；Einstein只角色复用已闭Source，不第三原域。支持/反侧足够便停，不扩全部supp、视频/飞行/攻击或每图像素配额。当前仍普通研究进行中，非日报验收/最终池。
