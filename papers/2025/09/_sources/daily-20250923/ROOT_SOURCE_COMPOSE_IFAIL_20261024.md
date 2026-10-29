# Compose by Focus / I-FailSense：首次有限必要证据

Singer A213确认两项已准入/日门成立，但没有CORE、Methods首读或在途请求；root本轮明确接受后首次捕获并准备必要证据。原5/6分、日期和owner/README仍归Singer。以下不是Books决定或日级完成；交Singer唯一另一角色回实际原域采用后，Sartre仅角色复用，不第三相同Methods/对照。

## Compose by Focus — 2509.16053v1

[精确稿](https://arxiv.org/html/2509.16053v1)、[raw](ROOT_CORE_COMPOSE_16053_20261024.raw)/[请求](ROOT_CORE_COMPOSE_16053_20261024.request.json)：GET UTC2026-10-24T09:20:26.692268至09:20:27.249133，200/exit0，155874B/SHA256 `84a4588f870eca8b2872cb6dda116bf37416a16975360ab8ee0f934ddbe78278`。

root实际完整读III-A–D/式1–2、IV-A–D/整TI/F2–6必要文字caption、V-A/B/整TII–III/F7–8caption与VII。未图/视频像素、代码或复现；核心机制、直接原表示/消融控制、关键反侧与全费足停，不要求外部DP3/GroundedSAM的全部论文或所有demo。

**问题到机制。** 独立atomic技能的示教不包含杂乱组合场景，全图raw RGB/点云可混进无关实体。本文按当前subgoal决定相关物体，用GroundedSAM mask抽RGB-D反投影后的物体点云，FPS/DP3 encoder作node，VLM推grasp/next/inside等relation的边；gripper点云假定可得。两层GAT（第一层4head concat/ELU、第二层1head）后全图mean pooling，与CLIP技能文字和robot pose共同条件化diffusion action chunk。点云encoder/GNN/denoiser共同训练，不是每个atomic独立expert或图本身直接输出可执行控制。

训练只见独立atomic示教，测试高层VLM先分解subgoals，再动态重建各自小图；**假定所有需要的atomic已学过**。新组合不等新skill零样本学会。任务相关选择改变的是policy可读支持与实体关系，不保证被删内容全部无关，障碍可被漏分/漏选，VLM边也非测得真值。GAT印式明确邻接聚合，未详细给语义edge label如何进入数值message，不补成完整可执行symbolic predicate或硬碰撞约束。图、任务描述、mask/相机、pose/动作horizon和policy版本须共同保存，是系统要求，不冒论文已做完整版本治理。

**直接证据与分母。** 五组ManiSkill2任务、13atomic各100motion-planning demonstrations，50随机初始position seed/相同步数限制；这是测试初态重复，不等多训练seed/CI。基线DP/DP3/pi0用同示教，也允许开头高层规划，但额外动态mask/VLM关系输入不完全相同，不能把所有收益唯一归GAT。TI composition平均子技能完成比例从.78至.93局部更高；atomic SceneGraph在stack.94低DP1.0/DP3.96、obstacle.92低三基线1.0。原文“所有都近完美”“baseline要穷举所有组合”不能升级为通用必要性/数据scaling不可能定理。

IV-D只三任务比较：改2D crop+DINO同时改feature/预训/几何；取消图或拼node改变边/顺序/固定长度。文字与caption支持有限设计对照，未看F6像素不补数值/显著性或每条边唯一因果。两个实机任务/六atomic各50SpaceMouse示教，两L515标定为world点云，20trial/同最大总步。TII composition .97/TIII工具.9均**每trial完成子步骤比例的平均**，不是97%/90%全任务无失败试次。例中三菜拾二即.67；不能推full-task概率。VLM还判subtask是否提前完成，预测完成不等真实独立执行验收，正文未给hardstop/失败恢复协议。单菜SceneGraph与pi0同1.0，杂乱/未见砖块示例不认证任意场景或物理安全。

**成本/共存。** 全演示/运动规划、真实示教与相机标定、每帧分割/点云/图、VLM规划/边与完成判定、CLIP/DP3/GNN/diffusion训练和多步action采样、驻留、真实控制/独立目标与碰撞回归均计费。硬件/precision、训练epoch/参数匹配、完整VLM snapshot/调用数、wallclock/峰memory/并发deadline与净费未披；VII明确额外VLM计算和mask错误，不由小图或少示教推净快/通用鲁棒。固定少物体/单skill可保raw RGB/点云policy；选择/关系或新atomic支持不足时保完整观察、可靠skill库与独立完成判据，澄清/停机或人工接管，不把focused graph当现实约束证明。

## I-FailSense — 2509.16072v1

[精确稿](https://arxiv.org/html/2509.16072v1)、[raw](ROOT_CORE_IFAIL_16072_20261024.raw)/[请求](ROOT_CORE_IFAIL_16072_20261024.request.json)：GET UTC2026-10-24T09:20:27.400144至09:20:28.425549，200/exit0，183765B/SHA256 `a0c1bd46034cf701eab64d0d5f286e8d80d1da9b936a56bf56881e3e257f4304`。

root实际完整读III-A/B、IV-A/B/两训练阶段/式1与投票式、V-A/B、VI-A–D/整TI–II/F6文字caption、VII/VIII。未图/视频像素、代码或复现；不将完整轨迹图分类叫作在线prefix monitor/真实恢复控制，也不为全部外部CALVIN/AHA/DROID附件建队列。

**构造人口与训练。** 一般控制故障不一定覆盖“动作合理却不合用户目标”的semantic misalignment。将成功demo与原instruction配positive(y=1)，与**同task类别但不同目标**配negative，形成平衡人口；换instruction不等真实policy实际产生该失败，同类别也不自动保证另一指令必不可同时满足，标签仍依所选目标互斥资格。CALVIN task_D34任务/六类，每task约150demo/11文字变体；训练/测试相同底层轨迹、场景或paraphrase的隔离细节未披，不补默认不重合，也不无证指控泄漏。

把所有时间帧/多视角拼成一张图，冻结SigLIP视觉encoder、训练MLP connector及语言K/Q/V LoRA作success/fail token监督。第二阶段冻结posttrained VLM，只训分布于不同深度的三FS heads，各以MLP/MHA pooling及residual/BN/BCE读内部features，再与VLM二值输出加权投票。三head各1、VLM2，strict大于总权重一半；不是平均已校准概率，也不因不同层认定统计独立/不同因果解释。“double weight break ties”不只处理平票：两FS投success而VLM fail时总2/5仍判fail，三FS success才3/5通过；保实际公式而不替成普通多数。FS所印probability是scalar BCE还是两类向量/argmax未完全闭，不照抄完整部署recipe。

**关键结果/反侧。** TI CALVIN单视LoRA accuracy.8571/F1.8626→加heads .9064/.9132，双视.8227/.8286→.8818/.8909；多视在本条件反而低单视，不以更多观察签更好。该增量比较同时增加heads/训练/投票，缺单层等参数/同预算ensemble对照，不能唯一归多层reasoning或grounding。未披trainingseed/CI，不把表格差视普遍显著。

AHA原数据未公开，作者依其流程另构**400条negative-only**，约85%控制/15%wrong-object；作者报89%是该人口失败检出率，不能同时验false alarms/成功保留或作balanced accuracy，恒判fail也会100%。与原论文打星AHA结果不当然同400样本/协议；不能从此推全域failure detector胜出或已识别内部因果。

DROID由真实demo重配instruction造6Ktrain/276test/平衡人口，仍非机器人部署时自然失败分布。LoRA保持CALVIN训练，分别换FS训练人口：仅CALVIN双视acc.6196/F1.4560；混real .6848/.6201；FS只real .7428/.7300，支持head校准/训练支持很重要，不能说sim-only已解决sim2real。Qwen双视acc.7536更高但F1.7094更低，最佳方法随指标而变。**y=1是成功**，precision/recall测成功类；漏报成功与错判失败不能沿正文部分“detect failures”措辞混读，sim-only precision.8/recall.3188不等失败召回.3188。一次输出/投票不是风险校准、独立任务完成或物理安全证书。

**全部费用与边界。** 全真实/模拟demo、目标重配及互斥标签审定、帧采样/拼图、多视编码、connector/LoRA训练、三head训练/feature读取和所有投票、领域校准及独立成功/失败回归均计费。冻结主体仍付backbone forward与中间features存取；3B标称不包括所有frontends/heads成本。具体training hyperparameters/rank/epoch、硬件/precision、帧数/最终分辨率与sampling、墙钟/显存、online latency/SLO/总能耗未在所读稿披露，不补值。固定完整图观察不能支持已经在未来帧前报警的声称；failure recovery仍future。真实目标、输入支持或误报/漏报失配时，保留真实状态/独立执行判据、域内可信head/人工复核与原控制安全，不由自评通过授权下一危险动作。

两项必要支持/直接控制/关键反侧及费用已足限定本轮拟采用命题；不预owner、NC/I或DAY。当前两原件请求均已结束，待唯一另一角色实际采用。
