# 第一标准包：必要Source已读后的具体Books PRE — 待非作者

使用本日 supplement-reviews 中精确位置和反侧。作者恢复后完整重读Books适用上下文；source STOP不等Books完成。以下四处拟整合均须peer actualPRE和root窄锁；未写。

## 17676 → MULTIMODAL-REPRESENTATION，Ch23

现有L14/18–35/45解释表示身份及tensor≠semantic，L294派生intent≠心理真值；尚未解释同一gaze observation的句选择、词heatmap和window intent classifier如何改变consumer粒度。作者实际读上述局部、Ch22小结/Ch24开篇。拟插在256token思想实验后、派生模态之前，两段：

显式 instruction 的意图由用户提交；把阅读时的 gaze 作为辅助输入，则先增加了一层可错的意图推断。相同 fixation 可以被聚合为高密度句子的文本子集、保留到词位置的视觉 heatmap，或在短时间窗提取统计特征、分类后再汇聚到句子；这三条路径保留的信息和下游接口不同，不能把“都用了 gaze”当成同一条件。应绑定眼动原坐标、文本布局、时间窗、聚合规则与 consumer identity，分开观察在哪里停留和系统认为用户想要什么；派生 intent 只拥有 proposal 权限，不替代用户明确目标。<!-- source-family:SF-2026-ARXIV-2601-17676 -->

这种隐式输入减少显式表达的负担，却新增设备校准、layout drift、mind-wandering 与粒度失配。[有限阅读摘要实验](https://arxiv.org/html/2601.17676v1)中，句级 density 的评价更贴近句子选择，而词级 heatmap 的部分 lexical 指标改善不等于 semantic 指标显著；同一模型的自评也不是独立意图真值。10 人指定主题与静态眼动设备的结果不授开放用户心理识别，显式 prompt 在主观总体偏好仍有优势。表示不稳定、用户需要准确控制或系统无法解释推断时，保留原文、显式 instruction 和澄清路径；新增信号应作为可撤销辅助，而非由传感器直接签发任务目标。

## 18157 → AGENT-RAG，Ch76

现有L321–325双向text/graph deferred state重开、L983–1001事实有效期与authority successor，未写empty-trigger timed/entity SQL条件放松，不能以有Graph主题授Covered。作者实际完整读两局部与Ch75/77开篇和交接。拟在text/graph融合两段后、Retrieval基本度量前，两段：

跨模态长历史不只需要把相关片段排序，还要保持同一实体在不同时间和观察中的可回读关系。一个条件分支先将视觉、音频的实体与关系写入带时间和原片段指针的结构化索引，再由查询明确组合实体、时间、关键词与关系条件；只有严格查询为空时，才按预设顺序逐步放松条件。这把“没有满足原条件的证据”与“条件放宽后的候选”分成两种状态，不能让松弛结果静默继承原 query 的 support authority。图、SQLite 查询、源片段与跨模态工作区应保留共同身份，最终判断仍回读原观察。<!-- source-family:SF-2026-ARXIV-2601-18157 -->

放松条件提高候选可达性，却会引入错时、错实体和上游抽取/diarization 错误；派生关系也不是独立事实。[有限视觉历史对照](https://arxiv.org/html/2601.18157v1)中，GPT4.1 的 LLM-search 提高一组问答分数，同时增加 latency 和 tokens，不能由 reader 上下文缩短推导全链更便宜；subhour 的原生 Gemini 路径仍可能更好。应分别验收严格/松弛命中、回读支持和总费用，记录哪个约束被放宽。时间身份不可信、松弛后仍空或成本不合算时，保留原 BM25/完整模态读取、显式过滤和 Unknown，而非无限放松直到得到答案。

## 18345 → PLATFORM-TRACE，Ch69

现有L68字段missing不能补0、L103–113采样必须保normal baseline、L74成功profile不授capacity风险，但未解释repository evidence channels的selection gate与agent排名。作者实际完整读这些段与Ch68/70开篇。拟Sampling两段后、Metrics/Logs/Traces互补前，两段：

从公开仓库恢复 Agent 轨迹时，采样之前还存在观察资格：配置文件、commit coauthor、branch 名称与 PR label 是不同通道，出现标记不等于已执行，没有标记也不等于未使用。配置可能被忽略，coauthor 取决工具设置，完整交互可能需要认证；共享约定文件更不能唯一识别某个模型。因此 trace population 必须同时保存通道、可见权限、缺失状态和提取规则，区分执行事实与身份推断，不把跨通道缺失补成零活动。<!-- source-family:SF-2026-ARXIV-2601-18345 -->

观察资格改变后，结果排名也可能变化。[一项 coding-trace 方法报告](https://arxiv.org/html/2601.18345v1)引用的 PR 切片在排除 draft 后出现排名逆转，只支持该过滤人口下的证据警示，不能冒充本文重新复现的完整 Agent 能力或人类监督因果。跨通道恢复、权限审计和失败/draft 样本保留都增加采集成本；公开记录不足时应标 Unknown，保留原观测和不同分母，而非用可见成功比例给真实部署签发可靠性。短且显式 instrumentation 完整的流程仍可用普通 trace，仓库标记只作恢复线索。

## 18631 → AGENT-TOOL-CALLING，Ch78

现有L116–123 toolname选择/合法性/参数与outcome，L704–708历史profile schema reward，未解释同功能工具改名/参数ID/paraphrase干预与asymmetric reward。作者实际完整读这两段及Ch77小结/Ch79开篇。拟toolname两段后、compiler反馈之前，两段：

合法名称与正确参数之外，还要区分工具功能是否变化。若底层功能相同，只重命名 tool/argument identifier 或改写 description，系统可能暴露的是接口记忆而非新功能适应；训练可以随机化这些表面身份，并以保留语义的改写扩展支持分布，评价则冻结底层函数，单独测名称、参数和描述扰动。这不是对任意新工具的保证，语义改写本身也需核验；registry revision、真实执行结果与授权 Gate 继续决定调用能否提交。<!-- source-family:SF-2026-ARXIV-2601-18631 -->

工具过程奖励也不能与答案正确性无条件相加。一条受限训练分支以 format 为硬门，提出“正确答案取完整奖励、错误答案仍可取分层 tool-quality 部分奖励”的非对称设计；原文 accuracy 取值与加权式未形成一致数值配方，这里只采用激励分账，不认证每个正确答案实际得到相同总 reward。Name/parameter validity 的过程分数也不自动等于有信息、更不等于安全。[有限视觉工具实验](https://arxiv.org/html/2601.18631v1)中，在推理时引入 A* 对导航有益却伤害 verification，所谓 unseen interface 仍使用原底层功能，部分 task 又在后续训练出现。额外 paraphrase、quality 评价与 rollout 都付费；任务、接口或奖励人口变动时应重新验收，不稳定时保留固定目录、普通 SFT/GRPO 与真实 outcome verifier，而非以过程 reward 取代执行证据。

## 18467 — 拟仅报告（非未读）

已实际Source与Ch31相关online/offline/support责任。新增可核差额是该8B API $350/50steps/rate-limit 与 offline优化阶段无API的资源事实，不是免费数据生成、更优SFT/DPO算法或普遍质量保证。训练样本过滤、top/bottom DPO和online support原则已成熟；此局部费用与特定API/上下文/大小不能成为长期固定配方。保留标准证据与counterconditions于Report，不将局部报价写书。不是以局部实验不重要排除准入。

## 18692 — 拟已有覆盖或仅报告，待peer具体比较

作者实际Ch26 L95–109：training-only 3Dteacher target→student projection/alignment→部署去teacher与metricgeometry/safety分界，已承载本次最低采用的几何辅助原则；LingBot query-to-depthtoken 的L1配方是当前组件实现，未据此授对原原则的新成立条件。Matched-runtime 的expert-shardgroups/Flex/compile报告则是运行配置而非通用优胜机制。拟已有覆盖只限定 Ch26的上述训练/部署权限，不授tokenquery配方已写、生产throughput或quality普遍改进；若peer认为queryconsumer具体差额需保留，另作PRE而不为覆盖方便降分。
