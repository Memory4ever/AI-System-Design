# 2025-11-20 有界标题补检增量

作者Dalton；16份exact-v1完整题摘实际读完，原始 [arxiv_tail_v1.xml](arxiv_tail_v1.xml) 与receipt保留。14潜在方向、2代表性关闭请求，均待root校准，不是确定落窗候选。

## 查询与停止

[learning focus](arxiv_learning_focus.xml)实际7条全部标题，来自LLM与pre-training/optimization stability/generalization bound/RL theory限定；query/start0/max25在receipt原值中。不是翻完先前107或44条。

官方cs.CL月表总1527只为定位有界片段：[初始web](WEB_NARROW_DECISION_AND_LIST.json)确认分页/升序；[skip800/show50](arxiv_cl_anchor.html)定位锚点只读标题，未转其他日期候选；[skip650/show50](arxiv_cl_slice.html)和[skip700/show50](arxiv_cl_target.html)浏览主线相关标题。目标段停止750，没有打开all或把三页150标题转全题摘/全文队列，不用编号当日期。新补选来自学习表示/量化、弱监督、reasoning压缩、置信度/评价冲突、安全训练与embedding信息流；科学推理、医学应用、普通情感分类等标题不送逐项队列。标题含糊的理论15005已只补决定性公式/限制，不用机构或领域名判定。

## 14潜在命题

| exact-v1身份 | 实际潜在增量与最小核验 |
| --- | --- |
| [2511.15633 HASTEN](https://arxiv.org/abs/2511.15633v1) | 概念层级漂移导致遗忘→hyperbolic hierarchy监督及mapper null-space梯度投影；核两部分作用与旧类/新类tradeoff，不以CLIP应用SOTA准入 |
| [2511.15411 D4C](https://arxiv.org/abs/2511.15411v1) | 单模态DFQ伪图缺语义/内部结构→text-guided及foreground/background synthesis；核CLIP量化校准需要的分布变化，不用bit-width数字直接结论 |
| [2511.14214 Chronology](https://arxiv.org/abs/2511.14214v1) | 局部rank高不等于全序正确、过滤错不能当排序错；reasoning-effort有局部正负证据；金融动机不自动排除通用LM测试，不外推实际回测无泄漏 |
| [2602.00003 v1 Efficient Multilingual Search Relevance Modeling](https://arxiv.org/abs/2602.00003v1) | 异构语言专家互补与routing/embedding fusion的效用及离线batch资源取舍可能有局部增量；核same-active-parameter对照与真正调度变化，不按e-commerce名称或MoE名称自动准入/排除 |
| [2511.14106 Stealth Fine-Tuning](https://arxiv.org/abs/2511.14106v1) | 暴露CoT可自生成有害轨迹并用于低成本适配，alignment可被破坏；仅核威胁模型/训练权限与安全-能力反侧，不提供执行攻击教程，不把表示相似当保留能力证明 |
| [2511.14166 Selective W2SG](https://arxiv.org/abs/2511.14166v1) | 弱label可能有害→P(IK)选择自身/弱标签加graph smoothing；核selector资格和强模型自标错误，不把三个benchmark推成superalignment保证 |
| [2511.14258 Entropy-Guided Reasoning Compression](https://arxiv.org/abs/2511.14258v1) | 长度与准确率目标对逻辑连接token梯度可能相冲→entropy状态导向训练；核真正冲突证据与分阶段控制，不靠短CoT本身准入 |
| [2511.14275 Don't Miss the Forest for the Trees](https://arxiv.org/abs/2511.14275v1) | 单猜测置信度与全answer-space分配概率不同；核distribution verbalization对校准的增量及answer-space unknown条件，不称人类样式reasoning即可靠概率 |
| [2511.14342 ConInstruct](https://arxiv.org/abs/2511.14342v1) | 冲突检测成功不等于主动告知/请求澄清，属于局部评价盲区负证据；核同任务检测与响应人口，不因benchmark无新算法关闭 |
| [2511.14385 Label Length Bias](https://arxiv.org/abs/2511.14385v1) | 长度归一化后仍有full-label偏差→NCC全label normalization/calibration；核与token层校准的区别及多词标签对照，不外推所有校准任务 |
| [2511.14423 Unified Defense](https://arxiv.org/abs/2511.14423v1) | attention realignment、跨层judgment及safe/unsafe routing针对jailbreak/finetune；教育benchmark不自动退出安全机制主线，核误拒与utility反侧，非鲁棒性保证 |
| [2511.14773 Temporal Predictors](https://arxiv.org/abs/2511.14773v1) | 早期hidden-state可预测最终正确性，长CoT难题选择会混入测量；核probe/holdout与selection artifact，不把早预测当模型已因果commit |
| [2511.14776 COMPASS](https://arxiv.org/abs/2511.14776v1) | context reliance probe驱动PID attention steering；核CRS资格、闭环代价与失稳，不把PID类比或注意力=事实直接准入 |
| [2511.14868 HTP](https://arxiv.org/abs/2511.14868v1) | 单summary与末token readout两种压缩→block-level prepending与mean pooling；核信息流/over-squashing理论假设与分离消融，不因组件成熟关闭真正局部证据 |

日期全保留：[v1原字段](arxiv_tail_v1.xml)中14773为`2025-11-03T08:57:18Z`、14776为`2025-11-05T05:30:28Z`；这不是已证明公开上界，不自动称窗外。2602.00003 v1字段是`2025-11-18T07:13:37Z`，不能仅由2602编号判定2026首次公开，也不能把当前v2 anisotropy新标题/机制回填v1。其余Nov18/19字段同样不是公开时间。任何采用都仍需真实首公开证明，未定项不展开全实验/owner。

## 两项代表性关闭

- [2511.14738 LAUD](https://arxiv.org/abs/2511.14738v1)：完整题摘只给zero-shot初始标注接active learning框架、commodity classification优于zero/few-shot结果；未提出改变标注选择/冷启动可靠性条件的实际新机制或局部反证。不是按商品领域一概排除active learning；请root核是否有摘要中的决定性增量被遗漏。日期未核但贡献处置不需另建日期请求。
- [2511.15005 Mathematical Analysis of Hallucination Dynamics](https://arxiv.org/abs/2511.15005v1)：摘要有理论潜力，所以实际读了[核心公式/限制](WEB_HALLUCINATION_THEORY_ADMISSION.json) §2.1/2.3/3.4/4.1/A.5。不是因无实验排除。作者的phase-risk联系仅假设，尚无推出风险的条件；其§4.1相位项仅随位置t、对该步各候选相同，不能改变argmax或归一化概率；A.5的WKW^-1是相似变换，trace和谱不变，所定义von Neumann entropy也不变。以上两条是作者公式条件下的直接数学反侧，不是实验推断。§2.1将概率乘积称delta亦未给正确差分/一阶推导。其余ECE/dropout/KLE/RAG等整合不建立新的已支持边界。因此不采用其可靠性机制；请root必要理论反侧独立核，不泛化成“所有无实验理论不收”。

## current纠错与版本轻量检查

[arxiv_selected_current.xml](arxiv_selected_current.xml)仅对已选30身份实际读current标题/updated/comments，不重读全部current摘要或版本史。没有明示撤回；Chronology明确`Version 2: corrected footnote and added code repository link`，须处理。

[原页身份](WEB_CHRONOLOGY_CORRECTION_IDENTITY.json)、[v2脚注](WEB_CHRONOLOGY_FOOTNOTE_POINT.json)、[v1精确绑定](WEB_CHRONOLOGY_V1_BINDING.json)实际定点核：v1 L103标v1，L112仓库`chronollms`；v2 L103标v2，L112为`chronollm`并增加workshop说明。只证明这个脚注/链接差额，不声明全稿实验无变化；未采用数值也不核全部附件。v2提交17:19Z不是公开时刻，不能自动作为本窗修订。

DataSage/Seer/Hyperion/AsyncVLA及若干新标题的current晚版不回填v1；版本变化本身不构成重要修订。ConInstruct/pi-star等Nov19 updated也不直接当公开。若具名纠错影响拟采用命题，精确重开该命题，不全池深审。

## root请求与普通停点

新增14方向和2排除可现在独立校准，特别是理论反侧、LAUD关闭、金融/教育/商品名称是否误影响主线边界。初筛raw已读，不等于候选Evidence完成。还需来源边界收口和有限日期恢复；不把缺所有owner/未读所有全文统一写普通待办。没有Books写入或名称补录请求。
