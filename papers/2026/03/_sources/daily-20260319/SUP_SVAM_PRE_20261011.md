# S-VAM16195：必要 Source / sole owner / 一段 PRE

作者resume_mar18，仅本19补03/18自然日，原2+2+2=6给同生成轨迹的teacher表征→单步future条件消费。实际[exact-v1](https://arxiv.org/html/2603.16195v1)完整題摘、§3.1–3.3/Eq1–9、§4.1–4.5/Tables1–4与§5已读，支持和直接反侧足够；不遍参考文献、全部qualitative图、project/code或复现。currentabs为v2 March18，未见具体纠错/撤回信号，版本号不单独触发整版比较；March v1及本批日级夹证复用，不把Submitted或revision自动当firstpublic。

## 必要机制与关键反侧

SVD首步up-block各层feature插值/concat；两decoupler还分别读当前观察的冻结VFM表示作anchor，经时空层预测几何/semantic futurefeature。Teacher来自同SVD多步生成的视频，经冻结DPAv3/DINOv2提取，以L2训练decoupler；不是把真实future observation当teacher，更不是新增真实metric geometry。Actionexpert还concat原diffusionfeature，QFormer凝聚后与text条件交diffusionactionhead。所谓one-step只是videofeature路径，action仍多步diffusion；不推整系统单forward/controller单步。

§4.1三阶段：先SVD适配（MetaWorld100k/real40k、4H100，CALVIN复用VPP权重），再冻结SVD训练decoupler50k/1H100，最后固定两者训练actionexpert（CALVIN60k/其余40k、4H100）。Teacher多步生成与VFM/当前anchor、额外训练和actiondenoise均计费；未披露整pipeline版本/precision/optimizer、全部batch/search、noise/teacher配对具体实现、actiondenoise次数、simulation repeats/seedCI或全部墙钟。

CALVIN ABC→D与MetaWorld50task每task50demo、monocular第三视图是局部人口；T1第5task68.9低HiF69.4，第1task95.8低CLOVER96；T2easy.793低VPP.818，不采所有切片优于SOTA。T3换GT未来teacher 3.82低同generatedteacher4.16，是target人口与训练条件局部比较，不独立证明唯一trajectorymisalignment因果或真实future更差；attention最大值/PCA及depthprobe不证明action必沿该路径或metric真值。T4dense/global/staticdynamic对照也共同改变teacher权重/表示，不采VGGT‘fundamentallyunsuited’或DINOv2所有几何语义解耦。

RealAgileX双臂/单frontcam四task约50demo/各25trial，透明物16→32%只4→8成功，不能签精确因果/普遍可靠。RTX3090单forward307.6ms（231+40.1+36.5）比VPP265.7ms慢约15.8%；chunk8摊销称25Hz不等每40ms重观测重推理、尾延迟或安全闭环。模型输出仍proposal，控制器/环境反馈拥有真实commit；训练/teacher生成/传感器/I/O/全部状态费用不可省略。

## 实际 sole owner / 差额

本日Books上下文/ROADMAP已actual加载，actual Ch26 366–410完整WAM三路径→latentprefill→Giga→geometrymotion分支→异步/可修订proposal交接及Ch25/27开篇已读。sole `MULTIMODAL-EMBODIED-VLA`：现genericfutureteacher/一次prefill与多模态feature消费未具体承载‘同生成轨迹的多步视频经冻结VFM作teacher，当前VFManchor+one-step学生再与原diffusionfeature共同交actionexpert’的接口。不假NC，不复制Ch25worldstate/Ch29通用蒸馏。拟GigaBrain段后、原‘当 predictive backbone 同时维护 appearance、depth 与 flow 时’前一段；Source/PRE待非preparer/新锁，未写未safe。

## 逐字一段 PRE

若一次视频去噪的内部特征过于混杂，也可把多步视觉生成留在训练侧，学习 action 更容易消费的未来条件。一条[受限表征分支](https://arxiv.org/html/2603.16195v1)先用同一生成器的多步预测视频，经冻结视觉编码器提取几何与语义 teacher target；两个学生模块读取首步内部特征和当前观察的编码锚点，分别逼近这两份未来表征，再与原内部特征一起交给动作 expert。这保持了生成轨迹来源，而不是将预测替换为真实 future observation；同源 teacher 仍会把错误未来带进 action，表征对齐、depth probe 或 attention 图都不拥有物理真值。单步只省去部署的视频迭代，动作头仍可多步去噪，锚点编码、teacher 生成、学生训练与控制等待均付费。有限对照中改用真实未来 target 未更好，并不证明唯一失配成因；部分任务退步、一次 forward 更慢而 chunk 摊销较高，也要求将新观测刷新率与命令频率分开验收。预测失准、几何/观测身份变化或完整 deadline 不成立时，保留原 one-step feature policy、显式短未来或 direct VLA，缩短 chunk 并由独立 controller 决定提交。<!-- source-family:SF-2026-ARXIV-2603-16195 -->

静态注：`SF-2026-ARXIV-2603-16195` — [S-VAM v1](https://arxiv.org/html/2603.16195v1)§3/Eq1–9、§4.1–4.5/Tables1–4及§5。仅同生成轨迹VFM teacher→首步学生表征/当前anchor→动作消费接口；GT target比较非唯一因果、任务反退、同源预测偏差、action多步/全部费用和chunk频率非fresh-control deadline保留，未核全图、代码/复现，不授metric真值/物理安全。

## root 实际非writer POST

root 实际顺读Ch26新增388完整段、378–410的三路径/Giga→本分支→geometry-motion/异步交接及2213–2220本人静态注与邻注，回对原PRE和resume_review17_18已独立通过的必要Source。同轨迹teacher、首步学生/currentanchor和原特征合用、action仍多步、GT比较非唯一因果、反退/成本与chunk非fresh时钟均保留，未升级metric真值或物理授权。原逐字段/静态注一致，实际POST通过、释放Ch26窄锁；只计单项整合，不授DAY、实现核验或复现。
