# 11/14 新 arXiv 方向：有限准入校准 ready

作者 Planck。只送三个新增方向与两种代表性排除理由，不重复四项官方 Blog 校准。确定落窗尚未成立，三个方向均不算本日确定候选、不进入 Books；此次可先独立核贡献筛选与日期隔离，不等待剩余标题集合。

## 真实范围与原始题摘

发现查询与起止页保存在 [arxiv_discovery.py](arxiv_discovery.py) 及各 `raw-arxiv-*.xml.request.json`：12个主线分类，submitted 区间 `[20251111190000 TO 20251112185959]`，start0 / max100 / ascending。提交区间仅作发现。原四组返回60/1/16/12，跨组未去重，不称89篇本日论文。model-training 的泛 RL/distillation 已增加 foundation/language/VLM/diffusion 限定，实际 [narrow p0](raw-arxiv-model-training-narrow-p0.xml) 返回36/36，停止start100；没有把60条宽响应逐项题摘或全文关闭。

三个方向完整题摘与原字段在 [exact-v1 XML](raw-arxiv-first-exact-v1.xml)，此次另实际打开三个精确 v1 原页 [raw-web-20](raw-web-20.json) 核身份和当前修订信号。页面没有撤回标记；SAGE/SSR当前分别有2026年v2，只提示晚版存在，不能证明本日有重要修订。本包不使用晚版方法。

## 三个潜在贡献

| 身份 | 原文新增与待核命题 | 评分草案与最低投入 |
| --- | --- | --- |
| [Structured Uncertainty guided Clarification for LLM Agents / SAGE, 2511.08798v1](https://arxiv.org/abs/2511.08798v1) | 模糊指令不只需要多问一次；原文将 tool-argument 联合不确定性、EVPI 选问及问题成本连起来。潜在增量是把澄清选择绑定到参数联合状态与交互代价，而非通用“有疑问就问”。LLM 模拟用户、训练信号与成功口径仍需必要审阅，不把题摘收益当真实人类交互保证。 | 2+2+2=6，若日期通过则标准审阅；owner线索 `AGENT-TOOL-CALLING`，尚未授具体差额。 |
| [Selective Sinkhorn Routing for Improved Sparse Mixture of Experts / SSR, 2511.08972v1](https://arxiv.org/abs/2511.08972v1) | 辅助平衡loss与每步重 OT 都有成本；原文提出从 transport map 取 gating score、仅最小程度使用平衡路由，以减少辅助目标并保留选择灵活性。需要核选择频率、梯度路径、训练/推理分工与相同预算反侧，不凭题摘“更快”授系统收益。 | 2+1+2=5，标准审阅；owner线索 `MODEL-MOE`。 |
| [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models, 2511.09515v1](https://arxiv.org/abs/2511.09515v1) | 真机 RL 样本成本高；原文用像素预测匹配预训练视觉接口，在想象轨迹内做 on-policy GRPO。需要区分 learned dynamics/reward 与真实反馈，也不能把策略更新时少用真机等同整个pipeline零真实交互。作者 [project](https://wm-po.github.io/) 核心与失败切片见 [raw-web-14](raw-web-14.json)：真实数据仍参与，微小接触会预测失真，真实rollout预算不是总计算预算。 | 2+2+2=6，标准审阅；owner线索 `MULTIMODAL-EMBODIED-VLA`，必要交接为 Ch25。 |

以上分数是拟采用命题的校准草案，不已确定落窗评分，也不是 Books 缺口宣告。不因完整摘要没有消融细节关闭它们；日期若补齐，再按校准后的具体命题读必要方法/评价/反侧。

## 有限日期恢复与停止

SAGE v1 `submitted=2025-11-11T21:50:44Z`；SSR `2025-11-12T04:29:05Z`；WMPO `2025-11-12T17:54:09Z`。精确原页仅给提交记录，不给首公开时刻。

SSR [DataCite](raw-ssr-datacite.json) registered `2025-11-13T02:44:25Z`、WMPO [DataCite](raw-wmpo-datacite.json) registered `2025-11-13T02:56:59Z` 可作为注册事实，不能单独给首公开下界。本窗UTC为 `[Nov13 01:00,Nov14 01:00)`；一般 schedule 不能排除提前非标准发布，不能把注册时间直接叫公开时间。

实际官方月列表 [raw](raw-arxiv-cl-month.html) 只有 November 标题，没有 Thu13 公告身份；只在ID08700–09599作56条标题查漏，不作全月题摘队列。一次明确日期路径 `https://arxiv.org/list/cs.CL/251113?skip=0&show=200` 返回400，见 [request](raw-arxiv-cl-dated-list.html.request.json)，不换空路径继续试。三项精确官方日列表搜索（`site:arxiv.org "Thu, 13 Nov 2025"` 分别加08798/09030/09515）返回空，见 [raw-web-21](raw-web-21.json)。此前有限历史公告/SSR日期搜索见 [raw-web-19](raw-web-19.json)，仅有第三方收录，未采用它的首公开或方法结论。

当前停止日列表恢复，不继续扩大候选池。可接受替代为真实历史官方公告/当天公开列表身份，或作者官方原始首次发布的精确时刻/完全落窗范围；取得后只重开对应ID日期，再继续必要审阅。没有这些材料时，隔离为外部日期保留，不拿日期hold回避当前可执行的官方 Blog、owner与来源工作。

## 两种负侧样本

- [Toward Automated Cognitive Assessment in Parkinson's Disease Using Pretrained Language Models, 2511.08806v1](https://arxiv.org/abs/2511.08806v1)：完整题摘实际读于 [narrow raw](raw-arxiv-model-training-narrow-p0.xml)。比较现有 BERT/Llama QLoRA/GPT 方法抽取病人叙述类别；结果限定医学分类，没有新增模型形成/推理系统机制或足以修正主线的失效因子。领域研究本身仍有价值；范围关闭，不因日期含糊追加请求。
- [AI Founding Fathers: A Case Study of GIS Search in Multi-Agent Pipelines, 2511.09005v1](https://arxiv.org/abs/2511.09005v1)：完整题摘实际读于 [agent raw](raw-arxiv-agent-context-p0.xml)。三历史persona回答三政治问题、递归refinement整套pipeline与简单pipeline比较，arbiter与人工评价；题摘主张尚是既有批评/反馈流程组合及9例局部质量差异，没有可识别的新搜索控制、评价反证或可靠性条件。作者先按具体增量不足关闭，**请抽核这一关闭是否过严**；不以“局部/没有额外实验细节”本身作为排除理由，若独立认为其流程比较改变重要判断则只重开此项。

请root核三条增量及草案评分、日期隔离是否足够精确，并抽核两侧理由。未完成日级来源/全部潜力项复核，不授本日完成。
