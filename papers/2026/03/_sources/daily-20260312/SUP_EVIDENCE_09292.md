# 2603.09292 — 必要Source与owner差额

身份：[See, Plan, Rewind exact-v1](https://arxiv.org/html/2603.09292v1)。首8完整v1题摘/当前信号及arxiv03-11BJT公开夹证已由review_mar12独核；当前无取得的更早公开身份信号，原件SUP_EXACT_FIRST.json保留。作者实际读§3方法全、§4关键评价/消融全、AppD.2直接失败全与AppE训练/评价全；不由取回HTML算审阅，不要求无关relatedworks/视频逐项关闭。2+2+2=6；Ch26具体长期缺口使必要差额深入，尚待root非作者Source/PRE。

## 支持的机制，不采用的宽表述

§3.1：AR输出depth、剩余subtask数、semantic+2D坐标subgoals、下一subtask 1–5waypoints、action；所有后流条件于前流。§3.2用示教open/close划分pick/place，其他任务用Gemini-3标段，LIBERO语义由DeepSeek-R1生成；DINOv3/SAM定位与离散0–255、median/outlier修正形成坐标。因而“无auxiliary models/无annotation”只可收窄为不另采recovery demonstrations、部署不另加恢复模型，不能免除标注模型/训练费用。

§3.3：从成功示教第一subgoal到初始姿态构造反向帧、取负end-effector action delta，令模型学“return to initial position”；不是在线机械反放日志，更不是物理世界逆操作。FIFO记录4步预测subtask数及8步预测2D轨迹，两相邻窗口数增加或8条轨迹相同触发anomaly；仅是派生预测异常，不是已证completion/接触安全。替换原instruction执行N步退却后恢复任务，N=3是N=2/3/4局部对照选择，太短空间不足、太长出视野/姿态不可恢复。

## 关键评价与直接反侧

§4.1/4.4 Table4：同作者重训MolmoAct85.6、SeePlan无Rewind89.6、全SPR90.6，独立Rewind差额约1个百分点；Spatial无Rewind92.6反高于全SPR92.4，不将论文总5%归因全部给Rewind。Table2原MolmoAct86.8到分训90.6/联合91.8是不同对照。LIBERO每task50episode×每suite10task；LIBEROPlus每task1episode×每扰动300+tasks，五种扰动。未见跨训练seed/CI证明，Robot条件成功47.7低于所列UniVLA50.3，虽相对drop较小也不授所有OOD领先。

§4.3：真实三任务各配置10trial，MolmoAct50/0/0与SPR70/30/40；小样本不是通用稳健性或安全认证。§4.4延长episode到980允许更多重试，重試次数、执行和时间费用不能被消失；N局部最佳也不是不依硬件/场景的阈值。AppD.2：离散action量化使精细放置失败；物理卡住时退却不能改变状态；退却执行成功后仍会错位/幻觉，甚至2Dplan正确而actions不跟plan，直接反驳“必回recoverable state”的保证。

AppE：MolmoAct7B mid-trained/LoRArank32alpha16；模拟32A100-80G，分训40–80ksteps/batch128且visual+LM可训，联合冻结visual/20k原数据+10kSPR/batch1024/5:5:4:8。真机100pick/200tidy/200Push-T示教、4A100-80G/batch64/5ksteps，chunk训练4仅执行前2；额外train budget不混同。4RTX4090作者报告2.08Hz，同7B配置并非真实robot全链路SLO；precision、并发/排队、完整通信与延迟尾部Not Disclosed。无artifact执行或复现，不采“zero overhead”强断言。

## 具体owner及逐字PRE提案（由root写，作者不写共享Books）

Owner `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)实际530–588与900–940局部顺读、Ch26开头/Ch25 action-authority交接/Ch27表示行动语义交接已读。现有2601.02295段是stop/progress触发fresh完成检查与反向记录delta的backtrack；2601.07060段是连续progress阈值切subpolicy；FARL段是world-model风险gate消费独立recovery。这里窄差额为预测剩余数/轨迹的持续异常→用成功示教合成数据训练的instruction退却policy，不重复这些旧分支，不说已有覆盖，因为构造/consumer并不相同。

拟插入：2601.07060的progress不同consumer段后、Policy内部LatentMemory标题前，仅两段。

进度还有第三种消费者：不宣布完成或切换阶段，而是在预测持续异常时暂时请求退却动作。一个受限分支共同预测剩余子任务数、语义与2D subgoal、到下一目标的轨迹和动作；短历史中剩余数连续回升，或规划轨迹持续相同，只触发 anomaly proposal。退却能力从成功示教的前段构造训练：反转帧序、取负末端运动增量，并用“回到初始位置”指令监督；运行时短暂替换任务指令，随后恢复原任务。这是学得的条件动作分支，不是直接倒放当前日志，也不撤销物体状态。[必要方法](https://arxiv.org/html/2603.09292v1#S3.SS3)的4步计数/8步轨迹与3步退却只属于作者配置；执行仍要经过controller与safety envelope，并依据新观测决定是否继续，而不能由模型自签已回可恢复状态。<!-- source-family:SF-2026-ARXIV-2603-09292 -->

这样把额外恢复示范需求移向成功示教的重标注与联合训练，却保留标段/视觉定位模型、decoder、异常窗口和重试执行成本。有限LIBERO对照中Rewind只在已有See–Plan基础上增加约1个百分点，单个Spatial切片反而稍退；真实三任务每配置10次，也不认证长期恢复或物理安全。原文直接展示机械卡住时退却无效、退却后仍错位，以及plan正确而动作不跟随；更长episode只能多给尝试预算，不能当免费可靠性。预测失配、接触不可逆或退却权限无法确认时，回退fresh完成检查、短horizon reactive policy、verified skills或人工接管，保留原来的进度检查和阶段切换分支。<!-- source-family:SF-2026-ARXIV-2603-09292 -->

实际状态更新：root已实际必要Source/上述逐字PRE通过，授权作者仅两段与本人末注窄写；已落入Ch26新568/570。作者实际正文/完整邻接及自身末注顺读，root非写入者实际568/570、553–600完整局部与自身1512末注回对必要原证POST通过，锁释放。下面原拟末注保留阶段依据，其pending已由本更新覆盖，不授DAY。

原拟末注：

- `SF-2026-ARXIV-2603-09292` — Daily2026-03-12补查；[exact-v1](https://arxiv.org/html/2603.09292v1)§3/4/AppD.2/E，2+2+2=6，预测异常消费者与成功示教构造退却policy具体差额深入。只采用条件分支，不授物理撤销/必可恢复状态；Table4约1pp与Spatial反退、10trial真机、物理卡住/plan-action不一致、标注模型与训练/重试费用近正文。4×RTX4090的2.08Hz非完整robotloop/SLO；precision/排队/尾延迟Not Disclosed，未核artifact或复现。作者必要Source/actual owner与逐字提案已准备，非作者Source/PRE、root实际写入及非写入者POST均待核，不授DAY。
