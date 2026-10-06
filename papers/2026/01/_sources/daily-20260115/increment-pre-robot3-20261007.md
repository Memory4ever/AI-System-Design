# 本日已校准感知/动作三项必要命题

作者supp_jan15；完整AB已root第二20准入校准。精确v1核心/必要段在increment-j15robot-core0、required1–4、robotrequired5、semfind、semrequired6，事件直链在direct7。日期沿既核arXiv正常公告下界/正式ID存在上界限定Jan14，非Submitted单判。当前未授Books锁；下面待非作者必要原件及actual owner PRE。

## 08665 VLingNav — 2+2+2=6，标准必要完成；Ch26窄差额提案

定频推理与history读写绑死→模型先predict think_on/off，只有on解码reason/summary并更新文字memory，行动仍消费当前视觉与旧memory→读写/推理时钟必须分责。实际§3.3/Alg1、§4.1.2、§5.4、§6.3/6.5/T6–8、§8：annotation用Qwen72B+expert轨迹并过滤，不是独立内部reason truth；128A100/4.5M训练，visual encoder冻但其余更新。T6 adaptive2.1%步有局部质量优势，非总token/latency同幅省；memory T7结合更好但collision1.90(noMem)低于5.51(full)，不得全安全提升。4090 remote+Go2/D457 RGB/1280×800、约300ms+100ms网络=2.5FPS，未证P99/deadline，single-system与FOV限制作者明确。precision/batch/concurrency/seed/完整annotate训练费Not Disclosed。Alg1最后hidden状态变量与§3.3口述不完全一致，不发布recipe；grid stride公式可能0亦不采用。

actual MULTIMODAL-EMBODIED-VLA Ch26:510–540已有derived state/immutable trace/新观察与controller权限、112–146已有时间尺度；没有**每步先门控，关门仍读历史/出动作，而summary更新只在开启推理时发生**这一调度分支。拟state freshness入口短段，summary非新sensor事实、漏更新/过期会反伤、encoder/门控/回放与通信费用、固定频/保守controller回退近文。不把think_off授足够安全。项目直链当前404为可选demo缺口，不阻塞本稿命题，不授实现核验。

## 08246 FSAG — 2+1+2=5，标准必要完成；具体Existing提案

关节模仿跨手失配→预训SD多步hyperfeature/五finger contact目标，depth投影与kinematic QP执行独立→语义接触目标不授物理可达/稳定。实际III-A–C、IV-A–D/TablesI–III、V：130demo/13objects与7unseen，H100/batch2/4k/3seeds；两手20试验/物体，lift>0.1m且hold>3s。SD/DINO替换同labels/schedule局部，但baseline只有3keypoint/固定执行vs五finger+新planner，不授总success单因果；3seed不是每cellCI，TableIII不构成统计等价。III-B全局pool vector又描述dense A_g身份冲突，不采用完整实现；RGB+stereo depth/segmentation非只depth无RGB。固定closure可滑/旋，force/slip反馈仅futurework；precision/多步extract latency/并发/SLO/完整训练执行费Not Disclosed。

actual Ch26:29–37完整已承载source动作不能直接复制、contact/finger目标与target retargeter/controller分责、目标错误或不可达、恢复/离线费及触觉仍待独立验收。采用本稿的contact/kinematic分离不改变这些具体判断，拟NoChange—Existing，不因新SD extractor名称新增段。abs有v2无撤回/勘误提示，不无差别比较未来稿。

## 08355 Semantic Misalignment — 2+1+2=5，标准必要完成；具体Existing提案，因果宣传不采用

HTML两次失败后官方v1 PDF已读§3–6关键文字/Tables4–6及§7–8；web截图失败，但原PDF断点续传已完整成功，本地渲染03–07页并实际逐页核§3–5完整定义/协议及Tables1–6，不是仅抽文本。采用边界：§5.4明确segmentation只作分析，VLM读raw图，不能采用“upstream segmentation失败因果传递”。§4.3把模糊回答计safety失败，Qwen Table6 parse_success .02–.22、SMR≈1，解析/拒答与真实unsafe不能混合；CLIP/SigLIP Top-K与free-form构念不同，安全reference来源/样本量/精确model/visual token budget具体值未披露。图3仅10个aggregate条件，不能证逐例预测/causal；HR/SMR并非全随severity单调。硬件/precision/batch/concurrency/SLO/总调用费/seed不披露，不复现，不授真实行车风险率。abs v2/v3无明确撤回/勘误标记，无更早完整正文链接，不遍历未来稿。

准入链收窄为：pixel aggregate被当语义可靠性proxy→同corruption下不同模型/输出协议的HR/COR/SMR与parse分歧→任务构念/解析覆盖必须分账，而不是修复任何upstream causal path。actual PLATFORM-EVALUATION-SYSTEM Ch66:104–116已定义target/poplulation/failure taxonomy/metric/scorer，216–218完整邻接已明确valid choices/拒答/无效格式另报、joint/conditional分母与grounding不同。本稿局部测量反侧不改变这些具体论点，拟NoChange—Existing；因果传递/物理安全中心宣传不采用。必要文件：[原PDF](./increment-semantic-08355v1.pdf)与render03–07，原摘录semfind/semrequired6供独立核。
