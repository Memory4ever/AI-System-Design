# 11514 Overhearing exact-v1 必要首包

准备者：Lovelace。作者118明确单让、本人明确接受后唯一首GET；交Bernoulli一次不同角色必要采用，不selfsign。

## 原件与范围

[exact-v1](https://arxiv.org/html/2509.11514v1)，[raw](./REVIEW_SOURCE_11514V1_20261023.raw)、[headers](./REVIEW_SOURCE_11514V1_20261023.headers)、[request](./REVIEW_SOURCE_11514V1_20261023.request.json)。HTTP200/exit0/332829B/6.621964s，SHA d0ad7ebe5d68f9948beb35894a2af03fe923cb54d63a819ec3775c53e732ba27。实际完整S4–8/Limitations、A corpus、B模型/输入playbook、C全部正文/T4–10全部行、D全部主/跟进prompt（含F10–13内嵌文本）已读。F3/4/7–9只正文/caption，不冒曲线像素/逐图对象、代码、原80对话/800标注或模型复现。145有效AB/current/公告联合日门不第三；未GET currentMethods/项目repo。

## 拟原始评分与安全采用范围

拟2+1+2=5，只同一人类referential对话上的视觉对象绑定/历史消费、分段输入与答案反馈对照。不是因新corpus或LVLM主题自动P，也不把自己的统计批评、旧grounding或所有context原则计Delta。原窄P维持，不因局部控制不足撤P或降分。

10对20人、80对话/27902词，狗/篮子各4round，每轮10target加3distractor；人类互动伙伴同任务均100%。模型旁听者每轮见全transcript与重新编号的13图3x5grid，四种startinground、多轮生成，主实验五种order；开放三模型本地3RTXA6000，闭源四API/精确revision见B1，Gemini仅April2025访问时段。temperature0与greedy不保证服务确定性。训练污染“此前未发表故绝无”只是作者陈述，未独立核训练集/原料公开史；没有具体先稿信号时不另造无限日期hold。

主T1原斜率正负保留：GPT4o dogs R1显著正3.4，Qwen7 baskets R1/R2显著负-2.3/-7.3；不能把不一致改成从不改善。T2 Claude/GPT4o负slope支持一些earlierstart收益，T8相合overlap差额保全部正反，不能说更多history无用。T6 R3两轮自然更容易nondecreasing；严格单调小概率不独立证明没有学习，离散10题accuracy、ceiling和随机ordering均影响该指标。10pair×5order不是50名独立人，重复同原图/对话和跨round相关须分账。

T3 ObjectDesc R1 GPT4o dogs+15.8pp、Qwen32 baskets+17/dogs+13.4pp局部改善，GPT baskets+4.4不显著也保。它是人工找到完整对象谈话边界后逐段多轮交互，每对象一次回答，API约10倍，只测R1；同时改变分段、短程工作集/反馈式输出节奏和任务组织，不能独自排除基本grounding失败或定位唯一内部bottleneck。AllTranscripts把四round/四图合为单次多答案，R2–4下降原值全保，但同时增加输入与输出负载、跨round图像/编号绑定，不是单纯只多给有用未来信息。OnlyTargets10对13也改choice人口，Qwen dogsR1 -1.2、GPT dogsR2 -1.0不抹；FixedOrder有局部下降，+Feedback原有限均值变化不显著并不证明反馈完全无效。Formal/-Interaction由gpt4.1重写且仅作者检查，D2.4又写拼接所有round而S7/F11称逐轮multi-turn，保留协议歧义，不用这些表签“只有交互特征是/不是原因”。

D1/F10–12系统输出模板写num_of_objects13并给13索引example，而实际任务10target、metric亦10；D2.7给10目标correctsequence。未说明parser/多余索引/缺失输出处理，不替其静默改模板或认证所有分母。T8文字每轮50实验却印df=100×overlap−1；T9称paired30run而印df59，不是标准paired df29。T4/5/8/9/10显著性星号、OLS/相关性只保原报告，未取raw重算，不能独立授精确p/CI/全比较控制；T4/5/8caption重复“**”不改原符号。实际观察/局部差额仍有价值，不把这些问题反断所有表均虚构或效果为零。

没有招募同任务humanoverhearer，原100%是能主动协商的人类matcher，非等信息/等权限baseline；可支持本有限模型旁听任务未达互动伙伴，不支持同任务人类旁听者普遍更强/可学而模型不能、闭源规模唯一cause或所有embodiedagent。Human效率wordcount下降与模型matchingaccuracy不是同estimand；原也明确不作直接人类overhearer统计比较。模型看全transcript不等自动成功消费，不能从attention可访问宣已具有全部有效groundtruth。

全部原对话/转录/人工分段、GPT4.1重写、五/三十排列、图像编码、跨轮history/KV和输出、逐对象十倍调用、goldfeedback、判分/失败解析及独立真人参照均计费。没有端到端latency/precision/完整token或SLO，不授分段净省费/主动澄清已实现。

## 唯一owner与拟具体NC

实际当前MULTIMODAL-REPRESENTATION Ch23完整20–58身份/坐标与consumer兼容、1914–1942对象表示/实例与指代链已读。1933完整段明确：对话指代可在视觉grounder之前失败，保原表达/历史/可见对象清单/重写身份，分别验referent-preservation和定位；对象清单是额外输入，不把最终定位率倒签指代正确，歧义回原图/原表达、澄清或Unknown。周边完整part/instance身份、query粒度及原视图/显式候选也已承载本窄新诊断所需接口。这不是只同视觉主题，也不借Ch75的“更多context不保证更好”泛原则替具体owner。

因此拟原5/标准完成/唯一Ch23**具体已有覆盖NC、Book0**：新corpus/局部对照留报告，长期安全判断仍是分开对话referent、当前图像编号和消费/组织条件，不把逐对象优势认证完整视觉能力或原历史可删。现文没有这份新数据不妨碍NC，亦不能用现文修原统计/模板。有限重开仅要采普遍人类旁听差距/唯一机制/精确统计时的等信息humanoverhearer、冻结分段与输出/长度的匹配对照、真实parser/逐项人口与相关性正确统计，或具名修订。非请求全repo/全图/所有人类语言学史；必要层足够后由作者实际采用，未整日DAY。
