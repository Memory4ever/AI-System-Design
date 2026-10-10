# 10370 GeoSense：按需独立几何通道Source/owner/PRE（待非作者）

仅03-13补Mar12 BJT。有效第三完整v1准入和42日级夹证复用；本次SUP_ABS3_10370.txt题名/七作者/完整abstract/history直接重对，无可见withdraw/纠错说明，只精确v1。SUP_CORE_10370_MANIFEST_RESULT.json官方 https://arxiv.org/html/2603.10370v1 GET200/236940bytes/UTC2026-10-10T01:18:25.884407Z，原raw/txt本日已保存。SubmittedMar11T03:32:12/registeredMar12T01:59:50Z与已核公告下界支持Mar12日级，不以Updated或Submitted单独作公开。未扩别日期、venue库/全版本。

## 真正增量/投入

始终在2D feature上加geometry会同时改变入口且消耗预算→双冻结encoder各自projector、独立geometry token段→先只读2D/text，模型生成<vggt>请求才追加geometry并second re-inference；训练用同题有/无geometry正确性差异决定request/suppress监督。新分支是**额外模态是否进入decoder的显式两次消费协议与其模型特定监督**，不借3D预测、projector、gate/RL、Bayes或“自感知”名字计贡献。

拟Design2+Reach1+Durability2=5：重要的常开fusion替代接口2，单multimodal感知/decoder路径1，请求/附加模态producer/监督与消费revision及预算的接口约束2。不是所有“可映射章节”都加分；具体Ch23现有内层路由不能替此whole-input/second-pass差额，需必要局部深入；强保持2D/严格必要性与费用反侧已读足拟两段。不采用真实空间意识、geometry truth、所有2D能力无损/更省或生产edge保障。Source/PRE待非作者，不formal。

## 实际读到与关键证据

直接精确v1 §3.1–3.3/Eq1–3完整（298–538）、§4全部构造与Table1（540–620）、§5全部setup/Tables2–5/ablation/5.5case文字及§6限制（620–1357）。Table4数据在caption前1113–1193实际已读，不用后正文概述代数值；Fig1/2/3/4/5只正文/caption，未看pixels精点，不认证noise-control曲线、案例真实机制或代码执行；无额外附录/实现或复现。初次owner大输出中无关中段截断不认证全章，目标GPRO与上下两路接口局部另精确读足。

Figure2/§3说明2D/text先“Internal Sense Decision”，<vggt>后串独立geometry tokens second re-inference；§3.2 both encoders extract features的architecture句并未完整说明VGGT是否真的延后算、cached特征/first-pass KV复用或重推范围，**不据较低trigger比例签encoder费用或总时延下降**。Geometry frozenVGGT-1B与2D Qwen2.5VL-3B encoder；各projector+LLM+boundary tokens训练，Eq3 text⊕vision⊕start_g⊕geo⊕end_g。独立段不更改2D embedding加法，但LLM与2D projector已更新，closed-trigger亦未恢复原weights/计算图，所以不签原2D模型bitwise或能力不变。

§3.1用VGLLM在约700k混合题有geometry/zero-padding比较，67%一致、25%均错、5%geometry改善/3%损害为该模型/样本的标签来源，不是所有scene的真实必要性。§4 Table1 55+5+15+3+13+16+10=117k；同样场景可相反trigger target。StrategyA T-F生成两turn：CoT以<vggt>结束、第二turn finalanswer；StrategyB F-T保原答案/抑trigger；这些标签基于指定模型双条件正确性，不识别geometry真实因果/所有新模型的必要性。相同scene两target减少某类shortcut的机会，不足证明已彻底去shortcut/潜意识已真实。

训练Stage1 LLaVAHound64k/Spar234k mixture、1epoch/Adam LR1e-6/warmup.03/batch32，Stage2维持设置/batch96，8A10080GB alignment14h+spatial-aware20h。Frozen前作pretrain/标签700k双条件infer/CoT生成和VGGT runtime额外费用未包括在该34h中。Precision、token长度、resolution/frame输入、推理batch/并发、完整latency/GPU-memory和重复seed/CI Not Disclosed。Table2 FT-Data940k与方法所列alignment+117k的合计不能自动补为940k，保持披露差别，不编造额外配方。零padding是主发现对照，分支结构及新数据训练也变化，不能从双条件正确性唯一识别trigger学习收益。

Table3同data比较fusion vsindependent/adaptive：VSI Avg54.86高fusion52.34/base48.07，但RelDir52.85低fusion61.61，RelDist53.66低fusion54.78；MindCube Rotation31.50低base34.50及fusion34，源码文字承认wide-angle/2–4views VGGT失效。35.68%触发（VSI43.7%、MindCube27.58）、general约3%只是调用人口，未有相同预算固定independent通道/no-gate和gate-only完整factorial；不同input-length/second-pass不能混成公平wallclock。

“严格保留general”关键反侧：Table4 final MMBench75.9<原76.6、MME1922<2104、MMStar51.7<56.2；alignment dip后恢复也没有全部恢复base。Table2相应原MME1526.1/final1473.7，与Table4原2104/final1922协议身份不一致；不擅补解、不合并为一population。相对相同data fine-tuned baseline的general较好是局部结果，不授原模型全能力不变。Table5 overall37.36较同量级比较较好，但D2 35.41低原Qwen2.5VL44.32，动态域仍未稳定；只有benchmark问答不是真实机器人执行/闭环安全。Stageconfidence/noise-image只正文描述，未读curvepixels且不等calibrated geometry correctness，不用概率批准producer或部署。

## actual唯一owner与差额

ROADMAP `MULTIMODAL-REPRESENTATION` Ch23，实际133–138 GPRO完整两段及相邻跨层注入/非对称双encoder分支顺读：已有controller在FFN层选择视觉重读/context变换，producer层与consumer位置、代理归因/全费用资格；150–153modality adapter关闭还需原weights/kernel配置才bitwise保留。它们未承载**先2D请求→整段新geometry tokens→第二次重推、双条件模型表现造request-label**这份输入消费协议，不按同为gate或多encoder泛NC。Ch25只action-conditioned dynamics/transition，与本稿问答geometry不同，不把VGGT当world-model owner；Ch26只物理动作消费，不从Quantiphy评测建立新机器人机制。

拟Ch23 GPRO两段后/现非对称双encoder融合前两段；保原内部路由分支与两方向算子链。root协调窄锁后才写，不由作者直接Books写。

### 逐字PRE

是否读取额外模态，也可以在整份 decoder 输入上作决定，而不只在内部层选择算子。一条受限视觉分支保留2D主流，把几何 encoder 输出经独立 projector 编成带边界的另一段 tokens；模型先只读图像与文字，发出几何请求信号后，再追加该段进行第二次推理。训练标签由同题在有、无几何条件下的答题差异构造，因而请求表示指定模型的监督决策，不是场景真实需要几何的证书；预测几何也仍是估计。Encoder/projector、边界与请求 token、标签来源和两次输入协议须共同版本化，不能把独立通道等同原模型不变。

[GeoSense的有限对照](https://arxiv.org/html/2603.10370v1)支持按需输入分支，但方向、旋转与动态任务仍有反退，部分general指标低于原模型；共享LLM/projector训练后，即使未请求几何，也没有原权重路径的精确保留保证。较低trigger比例不等全费用下降，几何编码、首次判断、第二次推理、双条件标签制备与回归均付费，未披露的特征延后计算和cache复用不能补造。请求失准、几何域失配、能力或总预算回退时，保留原2D模型、已验证的固定几何输入或原内部路由，而不以自感知概率批准新模态与部署。<!-- source-family:SF-2026-ARXIV-2603-10370 -->

## 最小停点

必要精确v1/关键评价与负侧、actual Ch23 gap及两段PRE ready，拟5分局部深入。共享Books未写、未formal，Source/PRE与actualPOST仍待独立核，不授DAY，不将未看pixels/代码伪造blocked。

## 后续实际完成（覆盖上一条准备状态）

root非准备者实际必要原源/完整Ch23局部/PRE通过，实际在GPRO两段后窄写两段及自身末注。本日报作者非Books writer实际顺读当前125–158完整局部、新137/139与root本人1293注并回精确原源，POST通过见 `SUP_POST_10370.md`；root再次回读POST与正文/自身末注，已将本人注同步PASS并释放窄锁。正式5=2+1+2必要局部深入、唯一MULTIMODAL-REPRESENTATION Ch23整合两段；只是这份输入消费接口，不授真实必要性、原能力无损、总费用、实现/复现或DAY。
