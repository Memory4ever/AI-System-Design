# Daily Research — 2025-10-28

**规范：** V3
**窗口：** 2025-10-27T09:00:00+08:00 ～ 2025-10-28T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T08:03:39+08:00

## 1. 结论

正式候选1家族：OpenAI敏感对话评价补充披露，Peirce FIRST准入2+2+2=6通过；受影响安全评价深入审阅1家族，正式受限Evidence及整日DAY已由Peirce实际独立复核通过。Books历史窄PRE提案1，root与Peirce最终裁定具体已有覆盖 / No Change，最终采用新差额0、实际写入0，无需POST。采用限回溯测量身份、不同评价人口与非单调反侧，不授线上安全率、训练机制归因或医疗保证；披露不等新模型release。

14源均作本日有限检查，历史目录/首公开限制不支持无遗漏。arXiv三个主题提交线索56/16/42、去重99不等99篇当窗候选，相关题摘和必要安全反侧已分层处理，日期隔离不评分。R-CGOT已恢复2510.22235v1的机制潜力，不以办公室应用直接关闭，待首公开证据再定点核CGoT方法/对照。共享书稿仅root写，不强造差异。

## 2. 来源覆盖

各实际URL、请求时间与失败见[原件目录](../_sources/daily-20251028/)，查询/停止与实际已读内容见[SCREENING](../_sources/daily-20251028/SCREENING.md)。原件保存不等已读。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research首查403；官方RSS本窗GMT过滤，10/27 10:00Z两篇敏感对话披露为同家族，12:00Z政策文按标题关闭；原Blog由web恢复，Hub原HTML200 | 已检查 | Research无法提取，RSS不代全站；FIRST与有限DAY实际通过 |
| SRC-ANTHROPIC | Research原页publishedOn定位；introspection10/29 01:20Z在本窗之后，非CMScreatedAt | 已检查 | 未列直发不保证覆盖 |
| SRC-GOOGLE-AI | DeepMind Research与Google pubs首查；原Blog October月页只定位10/27 coach→10/29，coach核心实际读后按应用/既有编排关闭 | 受阻 | pubs/DeepMind当窗历史未恢复，Blog不替pubs |
| SRC-META-AI | 原Research200当前Muse壳，未把当前内容作历史 | 受阻 | 当窗历史列表/事件不可提取 |
| SRC-QWEN | 原旧Blog至09/23迁移，新qwen.ai200仅壳 | 受阻 | 原新入口历史段不可提取 |
| SRC-DEEPSEEK | 官网原首查后/news/实际Research10项，10/21 OCR→11/01 LPLB；动态09/29→12/01，邻接即止 | 已检查 | 查看全部无href，不编分页，不保证未列直发 |
| SRC-MOONSHOT | Platform Blog26项，邻接09/16→11/06；org有限技术定位 | 已检查 | repo更新时间不作发布时刻 |
| SRC-TENCENT-HUNYUAN | 原Research动态壳；有限browser尝试因subagent visibility限制/重试超时未读成功；中文官方publicList page1 size20 renderType0 total11最早2026/02；org/T1定点 | 受阻 | 本日browser非成功核查，接口无2025历史 |
| SRC-ZAI | 原Research及实际page2共18项，末12/07且没有更多；release notes09/30→12/08 | 受阻 | Research10月缺段，release不替原目录 |
| SRC-BYTEDANCE-SEED | 原Research/论文页；误type请求400后更正article_type、US头；type1 token80 total94末页；type2 token20含10/23→11/27、token40末页total45，邻接即止 | 已检查 | PublishDate展示日期不授论文first-public，未逐审全年 |
| SRC-BAIDU-ERNIE | 原Blog页1/2，10/16→11/07邻接；第2页末1/2即止 | 已检查 | Blog不代未列仓库事件 |
| SRC-XIAOMI-MIMO | 当前8Paper定位最近10/21，More没有历史分页依据 | 已检查 | 未证明完整历史 |
| SRC-MINIMAX | 原Blog英文12项、中文13项；M2已定点核其文章事件10/27 08BJT在本窗之前，未重复候选；Agent独立TechBlog及原生md目前2026/05/13 | 已检查 | Agent当窗历史缺段；未把页面更新当新event |
| SRC-ARXIV | 12分类三主线主题提交线索，start0/max100三组56/16/42全小于100即止，去重99；cs.CL月首50只相关标题补检，不展开2666库存 | 受阻 | submitted不是公开；缺历史公告/完全落窗bounds。相关潜力与15项安全/反侧分层检查均隔离，不计候选Evidence |

按需会议/协议未触发，不扫描每周来源。OpenAI原链接Hub及arXiv具体v1/PDF为必要材料恢复，未扩站点日常库存。辅助搜索不能补成原pubs或历史公告覆盖。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [GPT-5 system card sensitive conversations](https://openai.com/index/gpt-5-system-card-sensitive-conversations/) | 2025-10-27T18:00:00+08:00 | 旧版安全分数不能代表新指标→新emotional/mental指标回溯重测及不同人口/版本的非单调反证→重新限定历史比较与采用边界；2+2+2=6，Peirce FIRST通过 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) EvalSpec、测量仪器身份与evidence revision；新差额0、写入0，见§4 |

## 4. 证据与知识整合

### [GPT-5 system card sensitive conversations](https://openai.com/index/gpt-5-system-card-sensitive-conversations/)

官方RSS两篇pubDate为`Mon, 27 Oct 2025 10:00:00 GMT`，完全落窗。原Blog说明评价10/03已部署模型，故只计本次披露1家族，不重记release。原Blog及Hub必要正文实际读到本命题，准入包见[FIRST_CALIBRATION](../_sources/daily-20251028/FIRST_CALIBRATION.md)，具体读点及反侧见SCREENING。

Peirce FIRST已核准最小命题与6分，身份/原证未变化，复用已读core，不重跑附件。Hub比较gpt-5-aug-15与gpt-5-oct-3，新emotional/mental指标是事后回溯；extremism not_unsafe .933→.925，SimpleQA accuracy .46→.44、hallucination .49→.52，均保留，不能宣称安全/质量全面单调改善。专家、自动困难集、线上估计分母与scorer不同，不能合并65–80%范围；专家一致率71–77%和taxonomy变动使低prevalence估计保持估算性质。采用只到该披露的测量身份/比较边界；policy not_unsafe不等实际伤害率。训练/路由细节未充分公开，无法归因全部改善于单一机制；model/hardware/precision/batch/concurrency/SLO未披露为`Not Disclosed`，本命题不采用速度性能。无代码复现或医疗安全保证。

实际重新核[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)开篇及“从目标到证据”、enriched gold与predicted-positive人口、“Rare Failure Evaluation需要保留无偏Audit Floor”：困难集不代表总体、人口/scorer/估计目标与审计下限已有具体承载，不提重复整合。变化核查进一步实际读EvalSpec及330–365的evidence revision正文。[Ch65](../../../../books/part-06-ai-infrastructure/65-kai-scheduler.md)末尾确有Scheduler只负责资源admission/placement→Ch66把workload/artifact/环境/scorer/结果绑定的直接交接，纠正旧稿否认该明文的说法；[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md)开头明确observed health不拥有质量定义。

历史[BOOKS_PRE_PROPOSAL](../_sources/daily-20251028/BOOKS_PRE_PROPOSAL.md)提出回溯重测的时间/测量身份不能静默替代旧时刻结果；root已实际比较owner/邻接并裁定已有覆盖，Peirce亦独立比较后确认No Change。Ch66的EvalSpec已绑定population/taxonomy/scorer/比较规则；固定答案仅改judge时，分数变化首先是测量仪器而非模型能力；“数值可复算不等于复现了同一个实验”要求任一身份变化生成新evidence revision、不得沿用旧排名/效果声明，历史调用记录缺失则仅授当前artifact的窄结论。回溯重测另存而不覆盖旧评价是这些机制的具体应用，提案字段细化未构成新的长期差额。最终具体已有覆盖，采用新差额0、实际写入0；历史提案1仅保留决策过程，不是待写任务，不制造POST或书稿diff。Peirce实际DAY已通过，本次仅同步其结论。

## 5. 缺口与下一步

可执行剩余：无。Peirce FINAL §8已实际通过最终已有覆盖/新差额0写入0、MiniMax英12中13、Ch65交接及§5/6范围同步；FIRST、正式OpenAI受限Evidence、十四有限来源、15项必要信号及root最终No Change的有效独核复用，不重跑核心或来源，无待写Books、无需POST。以下仅本窗终态保留项，不是正面证据或无遗漏证明。

本窗终态保留项：arXiv相关ID缺本窗官方历史公告/完全落窗首公开bounds，后续v2/v3不替本事件；Google pubs/DeepMind、Meta、Qwen、Hunyuan、Z.ai及MiniMax Agent缺历史段。普通原入口恢复与有限browser/接口已执行，隔离项不支持确定候选、正面Evidence、Books、无遗漏、性能/安全保证。替代需官方历史公告原件、带时区事件发布或当时RSS/历史导出；仅重开对应ID/源，不扩全月。HTML404的Chimera已由原PDF恢复，不再把可修正文缺口当外部hold。

R-CGOT已改判：[2510.22235v1](https://arxiv.org/abs/2510.22235v1)完整题摘明确Composable Graphs of Thoughts与可携带另一Agent的新推理机制潜力。API published `2025-10-25T09:39:39Z`不是first-public，未授窗内/窗外。仅缺官方历史公告或完全落窗首公开bounds；取得后读CGoT方法/对照决定采用，不把未读方法称无可迁移机制，不扩99条或全部附件。

## 6. 复核

复核者：Peirce（非作者）。

结论：通过

作者Curie不能自审。[FIRST](../_sources/daily-20251028/FIRST_INDEPENDENT_REVIEW.md)已核OpenAI最小准入/日期/6分及披露反侧、四arXiv题摘与Google coach核心抽样；R-CGOT已同步。[DAY复核](../_sources/daily-20251028/FINAL_INDEPENDENT_REVIEW.md)§2–3实际核十四有限来源和15项必要信号，§5通过R-CGOT/正式受限Evidence变化，§6–7核具体已有覆盖及root No Change裁定，§8于2026-10-05T07:56:44+08:00起实际通过07:49稿全部窄修并裁DAY通过；不授全量普通排除、历史全集或安全保证。作者仅同步实际非作者结论，写入0、无需POST。完成态V3与本地引用/限定变更检查另核，机器结构检查不替语义验收。
