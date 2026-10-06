# 2026-02-06 有界标题补检第二批准入校准

范围：仅恢复原 CL250/275/300、AI225、CV400/425、DC25至05017 的月份列表标题切片，不将150+5标题变成全量题摘队列。已有70候选及有效原筛选不重开。标题抽取纠正后选取下列与表示、训练、上下文、生成或Agent具体机制有关且未见有效原判断的12份完整v1题摘；原文见 supplement-related-new-abstracts-20261008.json。全批未获得官方公开日，Submitted不当作公开日期，不记确定本窗候选，不评分定案，不写Books。这里只提交贡献门槛判断，不自授Source/Owner审阅。

| ID | 具体准入或关闭理由 |
| --- | --- |
| 04081 | 已读完整v1题摘（supplement-dates-attempt-20261008.json）。以next-word预测解释中间层脑对齐不足→作者以layerwise intrinsic dimension、pretrain演化和brain-prediction finetune干预支持语义抽象关联→重新考虑中间表示的迁移解释；可能有主线贡献，不能按脑科学词直接关闭。日期hold。 |
| 04466 | 小域DAPT多选问答表现不能证明真实生成可用→原文将eliciting/reasoning/composing拆开，mDAPT补知识提取但未补后两步→重新考虑只改语料预训练能否解决推理与答案构造；局部负面边界值得核验。日期hold。 |
| 04764 | 更多long-context demonstrations不应被当作单调质量提升→原文在1M token/Javanese/Sundanese对比monolingual、instruction和parallel语料，发现饱和、near-window退化及语料类型敏感→重新考虑上下文预算和示例来源选择；不外推所有语言。日期hold。 |
| 04462 | 无监督视觉语义形成不必只靠类别标注→原文time-contrastive SSL用Ego4D模拟gaze crop，central vision与temporal slowness分别改变foreground与更广semantic facets→可修正表征学习的采样／时间不变性解释，局部模型非自动排除。日期hold。 |
| 04349 | 体素局部编辑受resolution及3D mask劳动限制→作者分析VecSet token子集控制几何区域，2D条件mask seeding/attention gating及去噪drift pruning→改变预训练LRM表示的局部控制与噪声边界；具体生成表示机制，不只新编辑场景。日期hold。 |
| 04167 | 精确视频编辑依赖密mask且文本定位不稳→稀疏正负point条件、两阶段视频对及mask-teacher蒸馏→重新考虑低标注交互条件如何继承更可靠dense control，不采用10xheadline。日期hold。 |
| 04439 | 多物体运动令global-reference含糊、local pointmap依pose而漂移→显式camera-coordinate 3D trajectories、双向trajectory/pointmap一致性受控gradient、static track anchors排除dynamic pose gradient及2D伪track自监督→修正动态几何表示的监督／坐标耦合选择，不只是提高reconstruction指标。日期hold。 |
| 04454 | frozen MLLM knowledge不能解释需外部实时知识的分割→interleaved reasoning/search及hierarchical reward在sparse outcome与rigid step supervision间取舍，OK-VOS强制outside knowledge→可改变多模态Agent知识证据与奖励接口解释；不把场景替换本身算贡献。日期hold。 |
| 05048 | 开放计划缺人类目标/对象信息时固定提问浪费→symbolic knowledge-gap tree和neural policy估计outcome uncertainty，经LLM检索总结与self-play选择elicitation，理论承诺限extended MDP假设→可改变主动澄清的状态／提问决策，不授摘要near-expert普遍结论。日期hold。 |
| 04271 | implicit deformation难直接编辑运动→稀疏skeleton rigid/LBS与fine non-rigid hexplane分解→可能改变动态生成表示的可编辑性取舍；尚需校准是否为任务组合而非本项目新的机制边界，不因3D title自动拒绝。日期hold。 |
| 04300 | 通用relighting改整体照明会破坏原背景→物理一致paired rendering与6D lighting token预训练aux planar-light objective再条件化one-step diffusion→可能改变可控生成条件的物理语义/背景保持选择；不采用160K或单步数字充贡献。尚需校准任务具体组合门槛。日期hold。 |
| 04687 | 完整题摘只有SDXL/DALL-E3在新disability群体的representational imbalance、prompt similarity和mitigation观察，未给可迁移新机制、明确旧评价失效条件或被改变的控制选择；新增群体与一般持续evaluation诉求不足，贡献前关闭，不作日期请求。 |
| 04441 | 完整题摘增加合成tracking数据域/对象、多样性及benchmark，泛称generalization改善/现有tracker limitations但未提出具体新失效边界、控制条件或训练机制；数据规模／coverage增加本身不足，贡献前关闭，不作日期请求。 |

以上是作者校准前拟判断，不是最终准入。root第二批实际读全部12份完整题摘后的校准：04466事实提取≠推理/构造、04764上下文示例饱和/语料敏感、04349 VecSet局部区域控制/denoising drift与05048主动澄清决策保留潜在准入；04454只保窄线索，hierarchical reward具体差异未验证；04462只保采样/时间不变性表示解释，不能外推基础模型。04081另经root实际完整题摘校准保留表示形成潜在线索。04167仅特定视频插入的稀疏/密条件及teacher distillation组合，无题摘所支持的新通用条件/蒸馏失效边界；04439仅动态3D重建坐标/轨迹监督，无foundation/world-state新判断；04271特定骨架LBS+hexplane可编辑重建、04300局部人脸补光paired rendering+conditioning+one-step，仅任务实现组合/指标，均贡献前关闭，不按通用state/coupling词重开。04687与04441原拟关闭理由通过。上述六项关闭无需另作日期请求，不称没有学术价值。

本包最终date hold只有04081、04466、04764、04462、04349、04454、05048七项；加首包04742合计八项。日期恢复仅接受各精确ID的官方历史公告/列表公开日或作者可核公开事件；月份列表、Submitted、registered及后期版本不补日期。仅日期hold不是已入选/标准完成或已证实；无必要日期不再深读此批全文，旧有效Source不重审。
