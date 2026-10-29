# Sep20 最小准入决定：RCS 与 SpatialGen

作者132实际确认14932/14981尚未开始N、无core或在途后明确单让；root随后明确接受，仅首次准备这两个准入决定域。118完整精确v1题摘与reader123歧义决定点复用，不第三AB。日期、评分、标准必要Source补足与Books owner仍由作者负责；本包只交作者唯一另一角色回原件实际采用，再由reader按角色复用，不预正式候选/Source全完成/Books。

## 原件与实际范围

两个GET实际于2026-10-24 UTC02:19:18～19结束，均200/exit0，无在途；本日同base真实request保存执行字段，不把获取时刻当公开日。

- [Robot Control Stack 2509.14932v1](https://arxiv.org/html/2509.14932v1)：`ROOT_NCORE_14932_20261024.raw`，146910 bytes，SHA256 `da14dd65dd1aea4e376f4c59b8e201fd41db2e1929df4ca8be56f9a9f49ff79e`。实际完整读§III架构/硬件抽象/仿真/工具与Agents接口；为区分统一API与跨域资格，另定点读§IV-C3/C4的real-to-sim和混合训练直接观察、Fig6完整caption及§V。未读全部署/动作预测/RL结果、曲线像素、源码或复现，不把单篇工具全功能当准入配额。
- [SpatialGen 2509.14981v1](https://arxiv.org/html/2509.14981v1)：`ROOT_NCORE_14981_20261024.raw`，279601 bytes，SHA256 `b6ba5655b587e1ee3e72eda4e2691a829f1eb4febbeb425e94a7ed1e34dfcf9c`。实际完整读§4.2两个attention轴/SCM-VAE及Eqs3–6、§4.3全部迭代状态与Alg1；未读完整数据/实验/消融、图片像素、源码或复现。这足以决定机制存在，但不等质量/一致性收益已成立。

## RCS：同一函数名之外，完成语义与跨环境判据要一起交接

§III不是只有“接多个机器人”的功能表。每个wrapper让动作沿反向组合映到base robot，观察沿正向组合回到policy；默认同步step等待定义目标状态到达，异步step则立即返回。MuJoCo通过step周围callback，让多个实体的收敛条件和碰撞中断进入同一高层调用。只读wrapper可记录/传输轨迹；Agents将policy与设备软件依赖隔离为两环境，异机TCP/同机shared memory的RPC提供同一接口。原文的“观察pre-aligned/step使sensor同步”是作者接口声明，不证明各设备采样时间、硬件时钟与真实控制deadline已经一致。

同一接口还允许先把候选动作交给数字孪生作碰撞/区域检查，未过不向真实机器人提交。这是一个具体执行consumer与停止位置，而不是由自然语言动作直接取得硬件权限；但仿真漏检、模型/坐标误差与现实动态物体仍可能使该检查不充分。校准例以已知tag-to-base CAD关系和camera-to-tag观测组合变换，不能由一份共同API免除本体标定。

拟准入链为：**训练policy的环境step常隐含动作完成和新观察语义，换真实设备/异步调用后不能只靠同名API保持它 → RCS在wrapper链和sim callback中显式交接动作映射、完成/中断、观察与record/RPC，并给出先模拟后执行的位置 → 应把接口复用与状态新鲜性、控制完成和真实结果资格分开验。** 这是一条可核的有限执行接口提案，不以开源/工具包名、机器人种类或泛“统一平台”本身为贡献；是否已有书文具体承担仍是后续owner判断。

直接跨域段落也保留有限失败边界：作者同checkpoint的20真实/100模拟rollouts只观察到loose correlation和其场景sim较低，不能授一般保守lower-bound证书；混入143真实/500模拟后，该接触模拟需更居中抓取，而现实边缘抓取仍可能成功，说明成功率差会来自任务/接触判据，不是“同API即同MDP”。10真实与100模拟、143真实与500模拟的不同训练人口又不支持免费合成数据或相同总预算。这里未核曲线像素/全表，不预其效果可信或最优比例。

本包建议RCS由决定N转入潜在贡献的日期、评分和必要审阅，保同步/异步可读状态、callback与真实执行边界作为拟核命题；不授middleware普遍更低overhead、任意硬件同步/安全、sim-to-real保证或新算法性能。

## SpatialGen：按view和modality交替耦合，并把生成几何变成下一轮条件

§4.2明确同时生成RGB、pixel-wise semantic map与scene-coordinate map：同模态沿view维聚合，单view内部再沿RGB/语义/几何模态聚合，交替两条attention路径；不是只把多个view一次拼接或用“3D consistency”命名已有单图生成。SCM-VAE保冻结encoder、适配decoder，另输出`c=1+exp(c)`并用几何重建/多尺度梯度约束；因此三模态虽共用生成路径，几何codec与RGB可用格式仍有独立责任。

§4.3因GPU memory限制分批生成视图，维护带颜色的全局点云，将其投到新相机视角作warped condition，再把本轮预测坐标并入点云；它把**先前生成的派生几何**转为后续约束，不能仅凭单轮好看认证长期状态一致。训练warp用ground-truth坐标、推断改用预测坐标，存在明确支持差；误差可能随重投影反复传播。原文称c为positive confidence，又在迭代段写按“uncertainty below threshold”剔点，阈值极性/状态接纳规则不能由本包私补。Alg1虽先构造augmented targets，后模型调用的字面参数又未显列warp/layout；需后续按有限命题核接口，不把文字意图自动当完整可运行recipe。

拟准入链为：**独立或仅按view一致的生成难同时固定几何、语义和外观，全部视图joint生成又受显存限制 → 原文交替view/modal信息路径、几何专用codec与持久点云重投影 → 需要联合评价跨模态/跨view耦合、预测几何回读和训练真值条件到推断派生条件的失配。** 这是具体机制与新状态依赖，不是只增加数据量/地图条件或新室内场景榜。建议转潜在贡献的日期/评分与相应必要审阅；未读实验/消融就不授其各组件必要、全局一致性、正确世界几何或净生成效率。

两项独立判断，未因同为sim/scene就联签。作者实际采用后可复用本包已读决定域补足必要证据，不重复读取来回造收据；仍缺的直接控制、关键反侧和费用属于普通下一步，不冒外部hold。
