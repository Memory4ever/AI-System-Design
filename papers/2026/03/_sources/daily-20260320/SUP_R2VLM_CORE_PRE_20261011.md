# R2VLM17312：可修订文字进度状态与奖励消费者

resume_mar17，仅03-20补03/19；恢复已重读AGENTS/完整适用合同、Sources每日主题/prompt/ROADMAP与本日STOP、Books约束。批5题摘/date准入有效复用，原2+1+2=5不变。准备必要Source/actualowner/PRE，未自授PASS、Books锁或safe/DAY。

## 1. 必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17312v1)实际核心§3/Eq1–10 L51–155、关键§4.1–4.4/T1–4 L157–243，必要A1–2/B1–3/C/T7与D1–3 L279–353、E2文字修订例L368–372；不读references/全部案例、F图像prompt、代码或其他版本。当前official abs只v1及CVPR2026说明，未见具名撤回/纠错；录用不改变已核公开自然日。

## 2. 采用接口与直接反侧

每轮只读4均匀帧的短片段（ALFRED4s/Ego4D2s）、任务与上一轮累计CoT，更新任务分解/完成与待做步骤及进度。CoT可拆分/合并/重排，不是immutable计划或全部事实历史。训练标签按已完成步骤比例加当前步骤内时间线性插值；distractor与原任务共享前nr步骤后截住进度，仍是特定构造人口，不是任意失败/绕路的真实完成度。teacher生成CoT能读gold步骤/时间；标签进度、文字推断和环境成功必须分开。分解revision使分母/阶段意义可能变化，不能无条件将同名百分比相减当真实动作效用。

B1 full-parameter SFT/RL各8GPU，LR1e-5/output上限1024/PPO KL0；RL挑>=5轮ALFRED或>10轮Ego4D改变训练人口。B3平均每iteration使长轨迹权重大；binary completion按两类逆比例加权，不是一般任务成功率。单GPUvLLM/16线程计时，GPU型号/precision/生产并发tail和完整标注/teacher/训练/检索/采集费用ND。full-video分支使用ZeRO3 offload、其余ZeRO2，不把Fig4训练效率归因全部排他归递归；fixed4frames不证明端到端常数，累计文字/生成/consumer费用仍在。

T1 ALFRED Zero完成acc .490低于base .494，说明“全部variants全部优”不能采。T2 full bin .917低于去MAE .924/去improvement .920，完整reward不每指标最优。T7 mixed ALFRED MAE3.02高于ALFRED-only2.77且bin .862低于.876，跨域不能授普遍positive transfer。T3文字称validseen goal改善2.2点，表GoalCond10.9−9.4=1.5点，路径加权7.9−5.7=2.2点，不混headline；*旧ALFRED来源对照非当下严格matchedseed。T4五步task .23与pretrain .23持平，不授每长度全面提高。D2真实接口把pre-action图复制两次、post图两次匹配四帧输入，非获取四个独立时刻。

消费者包括离线全trainset进度auxiliary监督、模拟在线IQL的进度差reward、独立LLM将CoT整理成提示。D2以Bellman gamma1解释progress差需要progress确实是相应value等条件，论文标签并不证明该身份；不采完整reward recipe、GRPO普遍不适多轮、推理真值/动作因果效用或现实安全。迟到观察/文字误判/分解变化可造假奖励，真实controller和fresh成功检查不移交给文字。一次强命题重开请求为固定或显式对齐分解revision的reward分母、label/physical success独立盲验及匹配预算/真实闭环trace；有限接口不依赖这些强保证。

## 3. actual唯一owner差额

sole `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际完整604–644：现有trace/subgoalstack、progress-trigger fresh检查、joint progress阈值切policy及Rewind异常退却，未具体承载短视频+可修订累计文字的进度估计器及离线label/在线delta/提示三消费者。不是泛progress主题NC，也不重做Ch22一般压缩或Ch31/32训练算法。Ch25/27入口实际读，前者环境预测、后者数据分布不接管本estimate到动作反馈接口。

拟Rewind完整628后/Policy latent memory标题前两段；保触发/切阶段/退却原分支，并说明第四种估计消费者，不自授动作权限。

## 4. 两段literal PRE与静态注

进度也可以先由独立估计器形成，再供训练或提示使用，而不是与动作联合解码。面对不断增长的视频历史，一条受限分支每轮只读取新短片段、任务及上一轮累计文字，修订步骤分解、完成/待做状态和进度；同一估计可离线标注policy训练集，也可在运行后的新观测上形成进度差奖励或交给另一模型整理阶段提示。这不是保存全部历史，也不是执行事实账本：文字会遗漏或继承错误，步骤拆分、合并和重排会改变进度分母，消费进度差前应先明确比较的任务与分解revision。训练标签中的步骤比例和步内时间插值不取得物理完成真值；奖励proposal、提示和controller的完成验收继续分责。<!-- source-family:SF-2026-ARXIV-2603-17312 -->

[递归进度接口的有限证据](https://arxiv.org/html/2603.17312v1)来自模拟与egocentric视频人口，teacher标签、过滤、长轨迹加权及不同历史输入/训练路径限制归因；关键消融、跨域和五步任务仍有反退或持平，不由较低进度误差授通用成功与安全。在线奖励对照复制动作前后两张图以匹配四帧接口，并不新增独立视觉时刻；固定短视频也不消除累计文字、生成、teacher标注、训练、提示模型及闭环执行的费用。缺独立成功证据、观察迟到或分解/奖励失配时，应重新观察/重置文字状态、保留稀疏完成监督和已验policy/controller，不让估计百分比自行宣布完成、切换或批准恢复。<!-- source-family:SF-2026-ARXIV-2603-17312 -->

静态注：

- `SF-2026-ARXIV-2603-17312` — [R2VLM exact-v1](https://arxiv.org/html/2603.17312v1)§3/Eq1–10、§4/T1–4及必要A/B/C/D。仅短片段+可修订累计文字的progress estimator与离线监督/在线差奖励/提示接口；保标签/物理完成、分解revision、加权人口、反退/配置与全费，不采真实value恒等、因果效用、普遍速度或物理安全；未核代码/复现。

## 5. 唯一窄写与作者实际回读

root授唯一Ch26该family锁后，resume_mar17仅按原两literalPRE写实际630/632及末静态注。作者完整612–655与最后本人/HeiSD/KineVLA/ShiftingUncertainty邻注实际回读，进度trigger/切换/退却→估计器→policy latent交接及限制近文正确；限定diff只本两段与静态注，`git diff --check`退出0。等非writer实际POST，不自授safe/DAY，不复制过程身份到Books注。
