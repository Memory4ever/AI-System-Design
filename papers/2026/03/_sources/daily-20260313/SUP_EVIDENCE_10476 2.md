# Learning to Negotiate 10476：评价/credit人口的必要Source与具体NC

仅03-13补Mar12；第三完整v1 AB与决定准入core独核有效复用，不以道德persona/GRPO组合本身准入。root已确认DATE4本项Mar12日级夹证可复用，不用Submitted/Updated作公开日。当前exact-v1 title/四作者/full AB/Comments/history实际重对，无当前可见withdraw/correction；v2 Apr9不是自动重要修订，不读v2。

原件 `SUP_DECIDE_10476.raw/txt` 已是 https://arxiv.org/html/2603.10476v1，首次manifest身份复用，不重fetch有效Source。此次实际读§2.1–2.2、§3.1–3.2.2/Eq1/Alg1完整、§4.1–4.3/Tables1–5、§7–8直接限制、B.1 agreement prompt、B.2.1 CA prompt、B.2.2/Table7、C比较训练与D zero-reward必要范围；A1/2只已读generator规则及persona核心上下文，不认证全部示例表、E全输出/图pixels/代码或复现。

## 具体增量、评分和终态提案

直接训练一个回答不能表达双persona对话的成功/失败→同版policy的两实例、每iteration冻结对手，agreement gate决定能否生成最终completion评分，最终CA reward只回dialogue token；失败仍参与组内比较而评价另生成summary→新增受控协商负载下reward对象、loss支持集与评价人口的配方接口，不把成熟GRPO/terminal credit或CA目标算新贡献。

拟 **Design1+Reach2+Durability2=5**：局部配方/任务实现，涉及rollout interaction、posthoc reward与训练mask/部署评价分责，可复用的信号population资格；不是因为Books覆盖降分或扩大书稿reach。标准门槛，B2.2公开strong claim与实际formula冲突触发定点深入，必要反侧已完成。拟 **深入完成／具体已有覆盖，Books0**，不采用“ordinal足以签相同gradient”或全能力/真人共同价值保证，不称新测量已吸收；待非作者校准Source/actual owner/终态，不自授formal。

## 机制与原文限制

Gemini3Pro生成1100 dilemmas与25对persona，两同模型分别assigned相反目标；Agent1更新、Agent2为当前iteration冻结copy，生成只看最近两turn。GPT4o-mini agreement每turn判方向已定，允许细节讨论，最多7turn；train未达agreement不生成summary/r=0，eval不论agreement都生成completion。summary由Agent1读prompt/双persona/dialogue产生，CA score0–5用于dialogue likelihood而非summary。zero-reward不是删样本，无KLβ0，DAPO total-token归一。

Eq1写全D_i token求和，正文D包含两人的utterances，未精确披露role mask、frozen Agent2哪些token被loss消费及recomputed probability完整persona/context身份。不能补造Agent2参数更新或声称已核完on-policy artifact；固定copy不等无需行为identity。同样B2.1文字说judge读full dialogue，但实际给的User Prompt只有query/两个persona/completion，没有dialogue placeholder；有限评分对象按可见prompt记录，不推实际实现或安全欺诈。final-summary reward未唯一分解中间动作因果，§7直接承认coarse supervision/组件未隔离；agreement只是单model semantic判词，非stakeholder真实接受/执行授权。

## 直接评价与预算反侧

Qwen3-14B-Instruct（正文链接Qwen3-14B/base名字偶称Qwen14B）/4bit QLoRA/no thinking；RTX PRO6000 96GB、约110h到reward convergence、batch16/LR5e-6/G8/β0，dialogue温度.7 top-p.95、summary.1/.95。LoRA rank/完整train token预算/precision（4bit之外）/judge totalfees/base checkpoint revision未披露。单agent baseline C用自reward不externaljudge、β.04/batch32/T1/top-p1、RTX6000Ada48GB/160h、2150step vsmulti1900；不能将joint differences全部归协商或匹配same-cost training。

两个100-item任务集，conflict personas重新生成fixed，dilemma仍结构接近multi训练；open-ended接近single训练。GPT5.2 held-out judge同provider family，pair双order只有两序一致才win，inconsistent被排，实际每row有效pair分母没有全披露。T2/3三评run mean±SD，不是三次训练复现或CI；greedy与sampled结果不能同population。multi对single CA conflict49.1/51.4近同，open-ended38.4/40.4均更弱；conflict-quality胜率67.7/72.8是模型judge有限结果，较少round可premature compromise，不等更真/更safe。T4两evalrun GPQA28.6±1.06→26.6±1.77，IFEval/AIME局部改善，不由小四bench推所有语言能力无损。

eval-set1900step curves被展示并与训练convergence关联，不补造sealed heldout/全OOD。D称30,400 training samples约25%uniform-zeroadv、3%failed avgadv−1.69 SD.65、72%成功非零；其“samples/trajectory”与B16/G8的完整rollout分母未统一，记录原数不自行乘8成已核实际量。失败零分在all-fail均0，不保证每个failed必负；移除zero或full-group均值不同都是新人口。

## B2.2数学转接断点（分析，不是复现）

原100 converged eval dialogues按旧score2/3/4/5各2/18/40/40分层。两GPT5.2重复：exact28/27%，±1约82/83%，Pearson.24/.21、weightedκ.17/.15，test-retest91%、r/κ.93；无独立人类gold，且无failed/populationall0/1slice。类别条件均值2.00/3.22/3.42/3.58单调，仅证明这四aggregate mean趋势，不证明每个training G8组内rank或acceptance一致。

原文进一步说“only ordinal signal determines direction and magnitude”与Eq1标准mean/std不一致：用同组r=(0,1,2)，中项A=0；严格递增映射到r'=(0,1,5)，中项低mean2、A'<0。排序仍相同但credit符号及大小变，正affine map忽ε时才保normalized advantage。这个确定性反例只限制原claim，不证明实际每组一定反转/全部policy失败；原conditionalmeans更弱，低r/κ不直接否定所有有限效果。中心cross-judge一致/普遍保能力强结论隔离，具体训练配方仍有效候选，不缩池/EX。

## actual唯一owner与NC依据

ROADMAP `TRAIN-RLHF` [Ch31](../../../../../books/part-04-training-system/31-rlhf.md)。actual871–895完整state-distribution→事后scalar/teacher监督分责、1032–1084完整credit/verifier→交互RL state/judge/horizon、842–852完整zero-reward人口与有限能力回归、1201–1208完整偏好评分位置与loss mask/共享参数/完整能力验收已顺读；`TRAIN-GRPO` Ch33 1–128完整同prompt population/ordinal映射→mean/std公式与三样本例是数学交接，不作为第二owner。

现Ch31已经具体绑定simulator/dialogue/policy/judge身份、terminal reward非因果credit、独立真实release gate、zero仍留组与loss-mask不冻结共享参数；Ch33明确rank与reward-gap不同、center relative sign由mean/std而非排序。上述既有正文实际承载拟长期命题：**协商环境/评分对象/更新支持集/失败人口与独立部署评价分开**。本paper未另给可靠人类接受或目标不变证据；在限制strong gradient、能力与价值外推后，没有未承载的长期接口需窄写，不按“同是RLHF”泛NC，也不把其新negotiation结果说已被Books吸收。

## 精确停点与重开边界

5分必要局部深入及actual Ch31/33比较 ready待非作者。Books0具体NC提案无需PRE/POST，不授全日；不要求额外补所有代码或独立实验才终止。本次隔离strong cross-judge/全能力命题；若以后取得实际role/loss mask、完整conditioned概率/组内两judge数据、独立personas/人类acceptance/匹配预算或重要修订，只定点重开该命题，不扩其他日。未读普通附件不标外部受阻。
