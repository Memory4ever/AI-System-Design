# 首批必要证据与 owner 差额（作者判断，待 root 非作者核）

精确版本均为 arXiv v1；日期原字段保留在 `jan17_all_date_fields.json`。初次两种 Python 缺库回执不作为证据，成功原文为 `2601.<id>v1-original.txt`，仅实际读到的必要段落承载下述判断。未复现实验或运行 artifact。

纠偏恢复说明：09833/09883真实采用、反侧、精确v1与root实际POST记录均未变，必要范围已达到对拟采用长期命题的深入判断，README同步实际“深入完成”；不是仅因分数或validator要求扩大阅读/凭空升深度。下列旧“标准”是最初最低路线，不覆盖实际owner差额与采用审阅。09858仍中心争议NoBooks，未授整日Gate。

## 2601.09833 PVNI — 2+1+2=5，标准必要段已读

Primary：https://arxiv.org/html/2601.09833v1 。必要范围 §3.1/3.2，§5.1–5.3，Table1/2 的列定义与均值/std，§7 全部直接限制；缓存行281–420、539–769、3400–3553及4303–4314协议。pos/neg responses 均值隐藏状态差作 persona axis；neutral-minus-negative 投影系数 `〈v_n,v_p〉/〈v_p,v_p〉` 对外部 judge 两个评分锚点插值，不是权重模型合并。三个约7–8B instruct模型，10套questionnaire/roleplay变体，GPT5.2生成探针，GPT4.1mini评分，两GPU小时/模型 RTX4090。方差下降对已测变体成立，不认证内部人格、construct validity或人的人格真值。

直接反侧：外部judge锚点偏好、neutral可能离开线性axis、axis相关、whitebox必要、单轮与有限模型/语言，未给成本–稳定性充分对照。§4理论是stylized近线性表示假设，不采用为实际模型真值证明；5分标准无需无关证明遍历。

Owner `PLATFORM-EVALUATION-SYSTEM`，Ch66已实际读996–1004的self-report / behavior / outcome分账和157–167的input provenance，承载“不应由probe推真值”，但未具体承载contrastive内部坐标可减少prompt敏感性且仍依赖judgeanchor与geometry假设。拟在996首段后融入两小段：问卷在prompt稳定且行为对象明确时仍便宜；变化提示鲁棒性可加内部坐标sensor，却必须把variance、judge calibration、construct/outcome分账；增加whitebox/生成/judge成本，轴曲率/相关或闭源回退行为测量/独立校准。不写分数或人格排行榜。

## 2601.09883 CORAL — 2+2+2=6，标准必要段已读

Primary：https://arxiv.org/html/2601.09883v1 。必要范围 §3整体消息/submit机制，§4.1–4.4，Table2全部配置与Fig3描述，§5适用边界；缓存283–635、638–813。新增对象不是typed state或权限机制：LLM information-flow orchestrator从全局消息history判断询问、继续原worker/refineinstruction、换worker或replan，wait_for_mention/send_messages自然语言通道，submit_answer_tool、30min cutoff。

GAIA165 validation，temperature0，强配置Grok4.1Fast均同64.24%；异构main强、worker GPT4.1Mini时63.64%对OWL55.15%。作者称同角色/模型，但正文明确CORAL排除OWL coordinator，角色/协调提示和runtime并不完全同构。OWL官方实现replan上限2调3；强配置CORAL tokens略高，异构简单题略高、>0.6M困难题tokens较低。没有配对置信区间/独立多seed，也不能把CDF或30min说明当两边强同walltime/费用预算。三个case揭示subtask成功flag掩盖birthdate缺项、1999不满足before1999、pageproxy不等wordcount；是归因线索，不是唯一因果消融。

Owner `AGENT-MULTI-AGENT` Ch82，实际读105–137 supervisor/worker及185–188 boundedtopology、883–889角色正确性。已有监督与局部合同，但未具体连接“worker返回success仍需核全局语义obligation → 只修当前instruction而非自动重跑已成功分支”。拟在Supervisor/Worker瓶颈句后两短段：固定有限状态在任务可枚举时仍可靠；partialsuccess把粗flag变薄，orchestrator可就缺失语义义务继续/refine/替换worker，预算、typedhandoff和independentverifier仍拥有authority；本地异构结果与全强平局、tokens代价及无唯一归因边界。不是所有workflow被替代，不借CORAL给形式化state或安全gate授证。

## 2601.09858 OutlineForge — 2+1+2=5，必要段已读；RL中心声明争议待裁

Primary：https://arxiv.org/html/2601.09858v1 。必要范围 §3.3–3.4、§4 Table1/评价说明、§5；缓存765–1112、1369–1404。具体可见机制是editablehierarchicalsection/subsection/paragraph schema，结构edit确定性执行、semanticedit query委派LM；arXivHTML解析1500稿、随机破坏段落反向state/diff supervision，用MLE或preferencealignment近似editpolicy。摘要说backward+forwardvalueRL，但正文没有对应已实现valuecritic、reward权重或RL优化训练配置；实验只说finetuneGemma2-2B/Qwen3-1.8B/Phi-3.8B，Qwen3-1.8B模型身份亦待具体澄清。不能照录“hierarchical RL已验证”。

200/300steps，surveywriting only；SurveyForge/AutoSurvey是引用reportedone-passperformance而非严格matched重跑。GPT4ojudge每50step评结构/引用/密度，citation饱和后质量升只是关联，不证明learnedvalue机制。人工schema限制、judge偏好、早期错误累积，没有支持通用papergeneration/更广scientific成果。本项是longdocumentplanning/learning mechanism不是AI4Science科学发现，不因应用名排除。

Ch79 actual357现outlineutility增删/重排与budget/verifier已覆盖可编辑outline控制；本次新训练claim必要细节缺失，建议中心RL暂缓隔离（重开确切value/reward/训练配置与模型身份），不凭schema命名整合新Books。可支持的逆向editdata construction仅为公开方法提案/有限survey结果，能否仅报告而非整项争议请root裁。未读附录（该v1没有必要实现材料）；未采用未披露RL或虚拟模型规格。
