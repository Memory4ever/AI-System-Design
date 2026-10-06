# QAsk / Omni-MMSI：实际 owner 比对后的单段 PRE

两项root必要Source6分已过，日期原27双向链。当前Books公共上下文、owner局部完整前后及相邻交接已读；各仅一段+本人注申请，不默认所有材料两段。

## 00265 / PLATFORM-EVALUATION-SYSTEM / Ch66

文件 `books/part-06-ai-infrastructure/66-evaluation-system.md`，现Pass@k/Pass^k是isolated resettable同task重复，不覆盖一个interactive trajectory中的连续候选决策及oracle输入资格；不是给Ch26重复导航模型bundle。

完整左锚：

> 降低 temperature 只减少 sampling 随机性，不会消除 environment、instruction、tool 或 evaluator 引起的失败。
> 固定 plan 可降低行为方差，也可能固化错误；clarification 可减少歧义，也可能泄漏 benchmark oracle。Computer
> Use Agent 的重复运行研究只在其 OSWorld、三次重复和指定模型合同下支持该诊断，不证明 `k=3` 满足生产 SLO。
> 高副作用任务还必须定义 reset、retry budget 与 compensation；成本受限的离线回归仍可保留 single-run metric。

右锚 `### Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy`，整activejudge节不改。之间拟一段：

同一交互轨迹的连续决策也不能用平均正确率替整段完成率：一个questioner只看目标描述与当前candidate、oracle独享目标image的受限协议，把每episode正确decision比例与全部decision正确才完成分开。目标被固定放在最后时，始终回答“不是目标”可取得前者的高分，却令完整finish为零；候选顺序、数量、description信息量与oracle权限因此必须进入评价身份。[有限交互/导航对照](https://arxiv.org/html/2604.00265v1)还显示更丰富描述的收益依模型变化，独立问答成功不等到达目标的navigation成功，人类小样本近似也不授通用VLM oracle。问题生成、synthetic edit、oracle回答、训练与导航模拟均计费；顺序shortcut、目标描述或oracle失配时，保留完整decision vector、独立finish条件与匹配信息预算的基线，不由问得少或模型小批准真实行动能力。<!-- source-family:SF-2026-ARXIV-2604-00265 -->

本人末静态注一条：`SF-2026-ARXIV-2604-00265` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00265v1)§3.1–3.3/4/5.1–5.2，2+2+2=6，仅SR decision/FR conjunction与questioner/oracle/navigation人口分责；保target-last shortcut、description与SeenSynonym反侧、人类小样本和全部费用，不授oracle普适/3×70×bundle因果或物理安全，未核实现/复现。

## 00267 / MULTIMODAL-REPRESENTATION / Ch23

文件 `books/part-03-multimodal-world-models/23-multimodal-representation.md`，已读完整DreamID/Identity-as-Presence两版分责和assignment反侧→AnyID primary/aux。现是generation reference绑定和输出评价；差额是从raw audio-video识别这份绑定的enrollment与oracle-cue资格，而非重复边际identity不等joint匹配。

完整左锚：

> 多主体还应把“每张脸和每个音色都出现”与“这个人说了这句台词”分开验收：边际相似度高仍可交换声脸；受限修订用唯一 face/voice assignment、说话时间重叠与 active-face 同步匹配检查后者，但这些都是阈值和模型代理，不是独立身份 oracle。短片、干净参照与筛选人口下的改善没有消除遮挡、交叉说话或稀有口音失败，原评价也有质量反退；参照编码、额外 tokens、融合、配对数据、各阶段训练、生成与匹配全部计费。配对不明、参照污染、代理失准或质量/预算回归时，保留显式单主体配对、既有条件路径与独立内容/同步核验，不让联合生成获得真实身份或执行授权。<!-- source-family:SF-2026-ARXIV-2603-17889 -->

右锚现完整“同一主体的多份 reference 也可能在衣服…”AnyID第一段，保持全部。之间拟一段：

生成条件指定了reference配对，还不能替真实audio-video的主体归属推断。理解任务应分开raw输入、人工登记的face/voice reference与已给oracle身份cue：知道谁说话在哪里和将这份证据绑定到谁，是不同误差源。[有限社交视频对照](https://arxiv.org/html/2604.00267v1)用人工69份profile、ASR/声纹/ReID及VLM消费reference；cue与reference同时改变的消融不能独立证明绑定算法因果，同reference外部模型仍有反胜，三步CoT也可低于两步。reference获得权限、识别器/输出身份、预处理与token接口须共同保存，人工enrollment、多encoder、推理/训练与判断均计费；raw识别或身份映射失配时，保留不确定归属、原始音视频回读和独立核验，不用oracle输入的高分认证自主社会感知或真实个人身份。<!-- source-family:SF-2026-ARXIV-2604-00267 -->

本人末静态注一条：`SF-2026-ARXIV-2604-00267` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00267v1)§3/4.1–4.4/5.2–5.6/Tables3–6，2+2+2=6，仅raw/perceptual attribution与oracle/reference/enrollment分责；保cue/reference共变、同reference反胜与CoT反侧/全部费用，不授identity truth或一般社会智能，未核实现/复现。

两个单段PRE与窄锁尚未授权，不写其它family；actual后分别交root完整邻接/本人注POST，非日级。

root实际两单段PRE与Ch23 400–421/Ch66 1417–1440完整邻接通过并依并发锁释放后分别授窄锁。作者逐字写入实际Omni Ch23 410（400–419）注1988，QAsk Ch66 1432（1414–1452）注6171，完整邻接/注顺读和限定diff通过。root随后实际各正文/完整左右段/本人注POST PASS，oracle/reference共变与同trajectory/isolated Pass^k分责保留，旧文完整；两锁释放，可同步真Integration，不授DAY。旧申请态只履历。
