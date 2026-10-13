# TRACEspatial23404 — Source / 两PRE

作者supp_mar26_fresh；6分/date25/read完整v1题摘已reader准入通过，与24586 TRACE不可混身份。实际 https://arxiv.org/html/2603.23404v1 §3.1–3.3、§4.1–4.3/T1–4的必要机制/评价/直接反侧已读，不机械读所有prompt附件。

## 原证和边界

不是新增几何encoder/真实pose：single-turn由MLLM从egovideo生成房间对齐起点/轴、离散8方向camera trajectory和timestamp/实体id/appearance/估计xy米制位置/自然关系registry，再在仍可见原video时回答；坐标是plausible estimate，协议化不把绝对scale/pose变测量真值。它改变空间描述与问答消费接口，非worldmodel dynamics、SLAM或物理commit。

VSI全5130QA/288视频，OST仅可复核random200scenes/1396QA，模型Gemini3Pro/Qwen2.5VL72B/MiMo7B；OST省略Qwen有instruction-following问题，不合并模型人口。MCQ exact/fuzzyparse，numericMRA平均相对误差阈值，不当统一accuracy；数据同/基本scaffold同，但长输出和prompt组件也改变预算。T1/2对direct大量局部反退，OST agentstate可降；静态allocentric描述与rapid egoupdate脱耦是作者承认限制。

T3同source/protocol的one-stage、two-stage、text-only结果不同，不能以此唯一归因『生成过程因果必要』；T3 Qwen基线37.58与T1 36.28不是同一可直接比较人口。T4去trajectory在roomsize/relative-direction更好，估计camera可反而干扰。text-only所需info与原video仍互补，不能『摘要足够替原观测』。Gemini作为theoreticalupper仅参照不是oracle；frameencoder、生成registry/路径、文本读出与必要回归全付费。hardware/precision/batch/concurrency/SLO本采用段未披露，不由tokens少推控制deadline。

## Actual owner差额与交接

Ch23实际几何track/grounded-answer接口L1138–1171：SGCoT是已有trained track后答案loss适配；Loc3R是camera prior+BEV/situation监督hidden。二者没有『单pass从egovideo自生成roomaligned camera+entity文本协议、仍保原video问答』的分支，故不是主题覆盖。Ch22可寻址history不是空间真值；Ch24生成commit及Ch25action-conditioned/dynamics不被该QA静态representation接管。拟插SGCoT受限两段之后、Loc3R之前，两段讲区别不重复camera/token常识。

## 两段逐字PRE（未写）

空间问答的中间接口还可以从 egocentric video 自生成一个房间对齐的文本表示，而不先获得可信 tracker 或 BEV hidden：以观察起点和主要静态结构提出参考轴，记录带时刻与离散朝向的 camera path，再按独立 entity ID 保存外观、估计位置和相邻关系；同一次生成先写这份结构，再让答案同时消费它与原视频。这里改变的是空间描述和问答的条件接口，路径与米制坐标仍是模型估计，不因序列化而变成 calibrated pose、当前事实或物理地图。<!-- source-family:SF-2026-ARXIV-2603-23404 -->

[受限室内空间问答](https://arxiv.org/html/2603.23404v1#S4)中，保留同一 schema 的单阶段、重新输入两阶段与纯文本读出有不同结果，不能只凭这个差异唯一识别内部推理因果；去掉 camera path 还改善部分问题，静态 allocentric 表示亦可能损害动态 agent-state 预测。原视频因此保留可回读权，camera/frame、entity 和生成 schema 要与问题及模型版本一起验收，MCQ 与数值相对误差协议不可合成一个通用空间能力保证。描述生成、视频编码、文本解析和回归都付费；路径、尺度或实体对应不可靠时，回到原视频、可信 tracker/几何与 Unknown，而不让流畅文本或更短输出批准真实定位、长期世界状态或实时控制。

本人静态注拟：`SF-2026-ARXIV-2603-23404 exact-v1 §3–4/T1–4；仅roomaligned camera+entity自生成文本与仍可见video问答接口，非SLAM/BEV真实坐标；保stage/数据人口和metric分责、去trajectory及agentstate反退、估计尺度/误识别和完整费用，不采唯一因果、maptruth/安全或SLO；未核代码/复现。`

本轮必要Source/实际owner差额/两逐字PRE与自身静态注已由supp_mar26_reader实际独核通过。精确锚为Ch23 SGCoT08436完整原段之后、下一“离线多视图重建”17625段之前；SGCoT与Loc3R并非直接邻接，不移动17625/VGGT3或其他原段。Books未写，待root本family窄锁，未授DAY。
