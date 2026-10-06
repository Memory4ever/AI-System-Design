# SynRL17693：程序状态标签与模型解释的监督权限

root唯一准备，2026-10-12，仅03-20补03-19。原准入/date及2+2+2=6有效复用，未写Books，不自授Source/PRE或DAY。交非准备者一次核验。

## 必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17693v1)完整题摘、§2.1–2.3、§3设置/T1–4、§4/T5–7与§6.2/T8–11直接反侧实际读；current abs同十五作者/单v1，无影响本采用的具体撤回说明。第一次评价返回局部截断，必要§6.2与T8–11已定点恢复，不授全部附录/图像像素/代码/复现。

程序生成短期运动与长程隐状态操作，frame-indexed事件/状态日志计算答案，再由VLM读取video/question/gold/全timeline产生CoT，另LLM按答案与事件验证、最多五轮修订，最后polish。SFT只对合成行保CoT，真实LLaVA行只答案；后GRPO消费合成可判答案。状态日志给答案的依据，不给模型生成或润色解释自动真值，也不证明学生仅从video取得同样信息。长程只初/终一端可见、操作序列可见，不意味着任何单帧都不可能提供捷径，需另测。

T1/2主要Qwen3-VL4B/8B局部视频指标；§3.2称Qwen2.5-VL7B/5K+5K，与题摘/§1的6.7K synthetic+1Kreal/7K及Qwen3主表人口不一致，不能合成精确统一recipe。8 H10080GB/global512/8rollouts/temp1、去KL/entropy仅所披露设置；完整precision、teacher/filter/polish与端到端成本/并发/SLO Not Disclosed。T6的VideoR1与本数据内容/模型标注/分布/数量共同变化，不能采21倍完整效率或唯一质量因果。T5收益不是cold-start必要性定理，T11 15K RL-only两类超过7K CoT+RL；T8 mixed的complex38.7低于synthetic39.2，不授全任务mix最优。T9 full若干切片不及单primitive，不采各类全优。§6.2的50例/四人各12例与blind judge只局部解释评价，不是全部训练CoT零误差认证；Pass4至少一次成功也不能推出faithful过程或线上pass1。原文“绝对正确”仅按程序答案有限分采，不能覆盖生成解释或真实迁移。支持与直接反侧足即停，不展开代码/版本diff。

## 实际owner与最小差额

实际Ch27入口、352–385合成/teacher/程序grader邻接、385–445混合/递归，以及77/256/1289附近时序/观测资格具体段已读；Ch26/28入口交接实际读。唯一`TRAIN-DATA`。已有grader、teacher、模态dependence与lineage原则仍成立；缺程序timeline/答案与特权metadata生成CoT、学生video观察的三份权限及real行不沿teacherCoT的具体时序数据分支。不复制GRPO推导，不建立视频应用owner。

拟在图引导合成/teacher监督完整两段之后、跨轨迹工具任务合成之前一段；非准备者可裁具体已有覆盖/收窄，不由主题映射自动整合。

## 待裁一literal PRE

视频监督缺口还可以由程序生成受控事件来补，而不让强模型同时制造场景和答案：以状态转移与逐帧事件日志渲染视频，直接从日志计算目标答案，再用这些特权元数据帮助生成和核对解释。这里必须分开程序答案、模型生成的CoT和学生实际看到的视频；日志可核不意味着润色后的每句话正确，也不保证抽帧输入保留了全部事件。[受限时序合成分支](https://arxiv.org/html/2603.17693v1)对合成行使用CoT、对混入的真实视频只用答案，随后以程序答案作后训练反馈，改变的是监督依据与人口而非物理真值。生成、验证、修订、润色与训练都计费；原数据规模/模型口径不齐，混合、各primitive和cold-start也并非所有切片最优，不能用样本条数比认证完整成本或普遍迁移。程序模型、渲染/抽帧、元数据可见性与标签检查须共同留在lineage，真实分布、观察支持或质量回归时保留真实标注、直接答案训练与独立时序holdout，而不是让流畅解释取得真值权限。<!-- source-family:SF-2026-ARXIV-2603-17693 -->

静态源注：

- `SF-2026-ARXIV-2603-17693` — [SynRL exact-v1](https://arxiv.org/html/2603.17693v1)必要§2–4/T1–7及§6.2/T8–11。仅程序事件/状态答案、特权元数据CoT和真实/合成监督分流的有限接口；保解释非零误差、学生观察支持、人口/模型口径冲突、mix/primitive/冷启动反侧与全费用，不授21倍总效率、绝对正确或普遍真实迁移。未核代码/全部图像或复现。

## Writer 实际写入与读回

2026-10-12 非准备者resume_review17_18主独核§45有限Source/PRE通过后，root sole Ch27写入：图引导teacher两完整段后、跨轮bank前一literal与章末自身静态注。实际完整361–384及末9行顺读，程序答案/特权解释/学生观察资格承接teacher lineage，随后bank转向跨轮覆盖；未改原图引导或视觉self-play论点。正文与静态逐字回PRE，限定diff-check无输出。writer检查不算POST或DAY，交非writer一次真实邻接/自身注复核；先前未匹配短上下文的patch失败无改动，最终用完整原段锚点完成。
