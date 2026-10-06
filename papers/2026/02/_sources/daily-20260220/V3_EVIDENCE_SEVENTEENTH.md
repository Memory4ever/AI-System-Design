# 02/20 第十七有限必要包：16173 / 16179 / 16304；16241撤回排除

只处理本日既有具体潜力的必要源，不扩raw目录。三项必要原源/actual owner及H/Only处置已root实际独核通过，16241撤回排除也已独核，无Books写入/锁；非日级验收。16173/16304位置为 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`；16179用同法的 `V3_CORE_2602.16179v1.html`。

| ID | v1 Submitted UTC | 同ID DOI Registered UTC | 北京公开范围（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16173 | 2026-02-18T04:18:47Z | 2026-02-19T02:39:58Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:39:59+08:00 |
| 16179 | 2026-02-18T04:35:46Z | 2026-02-19T02:40:07Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:40:08+08:00 |
| 16304 | 2026-02-18T09:36:46Z | 2026-02-19T02:43:01Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:43:02+08:00 |

Registered只推arXiv公开上界，加1秒保原精度，不把Created/Updated当正文公开。当前官方ABS 16173v1/16179v5/16304v3已轻核，未见明确withdraw/erratum声明；后两版本号不自行证明重要事件。16173精确HTML header `arXiv:2602.16173v1`，稿内`August 24, 2026`与fresh官方exact-v1完整cmp相同（临时/tmp/feb20-pahf-exact-v1.html）；稿内日期仅raw，不变更公告/DOI日期链或假定later-body alias。

## [Learning Personalized Agents from Human Feedback](https://arxiv.org/html/2602.16173v1)

2+2+2=6，完整AB88–89已实际读；拟中心理论争议暂缓，局部双反馈仅报告/具体已有覆盖。§3.2（117–149）per-user explicit memory先取相关偏好，known ambiguity才clarify，post只有用户认为结果错误时收到correction；LLM salience detector、summary与similarity merge没有独立truth权限。§3.4（194–205）标准SQLite/FAISS notes后端非新架构，retrieval/提取/多步写均调用模型。§4（209–237）40×30与20×45 scenarios每phase，四阶段同用户persona→换persona，test撤反馈；embodied用persona LLM、shopping问答LLM但post deterministic conjunctive acceptance policy，不能混作真实人群或真实物理执行。FF只记一项任务是否至少一次反馈，不是完整问题/LLM/token/latency成本。

§5（240–276）已有note使pre-only不感歧义而少问，drift下局部退步；双反馈/后反馈恢复是这一policy与模拟人口下结果。Table1 embodied Phase4 PAHF68.8、post68.3，并非严格所有slice/统计显著优；叙述246把Phase2的67.9/70.5写成Phase4，不采用这组headline。SE不说明所有观察独立或全预算matched，真实用户、生产SLO/hardware/precision此命题Not Disclosed，未核实现/复现。

中心理论§3.3（153–192）`at most K` switches与`any policy never post`声称Ω(T)，但给定设定包含零实际switch或末轮才switch且初始动作正确的序列，不能直接推出所有这类轨迹线性错误；需要worst-case/分布量词和switch可观测性范围。balanced m-ary问句也未单由balance证明每步wrong-action posterior按1/m收缩，需所问划分与action识别关系。不能把理想oracle/正确feedback immediate update的O(K+γTm^-k)授LLM salience、retrieval和可错反馈执行保证；这里是实际证明缺口，不声称双反馈局部实验全假。

actual AGENT-MEMORY Ch77:935–958已明确pre clarification当前歧义与post correction旧preference失效、scope/time/supersession、用户摩擦成本与PAHF persona/理想regret边界；不因缺SQLite配方造gap，不写Books。中心普遍必要性隔离；定点重开量词/信息状态/有效query与反馈正确性条件的修正版证明，不追全附录。

## [EnterpriseGym Corecraft: Training Generalizable Agents on High-Fidelity RL Environments](https://arxiv.org/html/2602.16179v1)

2+1+2=5，完整AB89已实际读；拟标准完成仅报告。§4.1（207–218）order→product→KB、满页10条仍不paginate、price漏alternative是具体失败实例，非统计因果证明。§5（220–260）GLM4.6、每prompt16rollouts/stateful Docker MCP环境、finalresponse rubric LLM judge按criterion比例reward，all criteria才pass；granular/objective rubrics只是减少模糊的设计，不自动确定性环境真值或可靠judge已证。实体规模/关系/噪声提供任务人口，尚未孤立realism/rubric/complexity效应。

§6.1（280–282）训练时heldout集合不是§4后扩Corecraft-Expanded，不合并frontier与训练分母。§6.3 Table4（321–349）作者一epoch后外部任务有增益，Toolathlon Table4+6.2pp与AB+6.8不能混用；所拟命题不采用其数值。§6.4/7（440–459）Monitoring/Operations/Notion弱侧，单GLM/单epoch，degraded环境/简化rubric/降实体复杂度的归因消融明确future；未披露全部训练/调用预算、hardware/precision/SLO，不授环境质量唯一因果或生产可靠。当前v5 AB改suite/bench命名仍保主要方向，未以名称作为本窗修订事件，未比较全版本。

actual TRAIN-DATA Ch27:488–494已executable state/env/tool/verifier/judge/reward/rollout/finalstate身份、格式与outcome分责、ontology blindspot/真实环境与gold；Ch66:1198–1210已persona合成分布不能代真实人群/任务outcome。该企业任务库和局部transfer值得报告，但未证可长期新增的realism/rubric独立有效性条件，不因成熟workflow配方或2,500实体自动强写缺口。不是说整个benchmark和所有局部结果已有。

## [Mind the Gap: Evaluating LLMs for High-Level Malicious Package Detection vs. Fine-Grained Indicator Identification](https://arxiv.org/html/2602.16304v1)

2+1+2=5，完整AB74已实际读；安全反侧受影响深入完成拟仅报告。§4.1/4.2（111–116）binary package与47细indicator不同任务；原池4070不是每配置实际binary人口。§4.4–4.6（208–231）binary固定103 packages（10malicious/93benign），multilabel每config37且跨config不同sample，open5/proprietary3重复；选best weightedF1后再全370。故同13model与提示组不能授paired同人口纯粒度效应，best配置再全池不是独立heldout。配置call/input长度不同也非iso-budget，未授生产SLO/precision/hardware普遍。

§5.1.5（1648–1660/1757）binary均F1到multi weightedF1是协议间差，不采headline41%或文末21%作统一因果gap/semanticdepth判定；GPT4.1 .99来自103抽样，非4070全量。§5.2.2（1779–1782）标准Windows classifier被误判、只见decoder不查decoded benign内容是具体surface-context失效实例，不证明唯一内部semantic路径。§6（1808–1812）contamination、PyPI范围、10:1vs73:1 prevalence、GT47taxonomy/子样本与非线性关联均直接限制。当前v3 ABS已把分层任务和复杂度方向改写，作为窗外限制线索，不把v1negligiblecorrelation外推零因果；无明确纠错说明，不遍历全version或倒填v1实验。

actual PLATFORM-EVALUATION-SYSTEM Ch66:118–120已whole-result不签segment正确、标签/trajectory粒度和judge代理分责；4394–4408安全attackprofile/population/evaluator域未完不签安全保证。本文具体package→indicator经验不等所有security已覆盖，但上述不匹配采样/权重不足以建立新的普遍机制或纯粒度因果命题；保任务/负例/人口在日报，不新增package detector教程或以低score错误回退EX。

## 原始安全排除：[LLM as Annotation Agents: Exploring Zero-Shot Hate Speech Annotation in Bangla with Large Language Models](https://arxiv.org/abs/2602.16241)

不得评分、入候选或Books。当前官方abs Comments与DataCite `Withdrawn` v3原字段实际声明**complete withdrawal**，原因是significant methodological discrepancies affect validity and reproducibility；官方当前page raw存 `V3_CURRENT_ABS_2602.16241.html`，约136–142 Comments与v3身份，同ID DataCite保2026-03-01T18:48:22Z Withdrawn。这是明确撤回，不把有HTMLv1可访问当有效恢复，不将官方撤回当访问故障。

此前完整AB61–62/§4setup/§6/A1/A8已读证据原文件保留，仅作为原筛选与撤回依赖记录：17model/三student majority labels/55人100item、explanation similarity与classification/不等义identity/promptfewshot条件，不授正面结论。尚未进入本日报候选表或Books，故无需删书/清其他有效引用，97旧potential切片要减此1；来源按此具名排除而非当零命中或NoChange完成家族。恢复只接受作者新的有效重发/撤回解除及methodological差异原说明，届时独立归属事件，不扩本窗或邻日。
