# 03/27 Harmful Manipulation — 必要证据与采用边界

家族：Google Harmful Manipulation / arXiv:2603.25326。官方事件 https://deepmind.google/blog/protecting-people-from-harmful-manipulation/ datePublished=2026-03-26T13:00:00+00:00（BJT21:00），核心120–158完整读；发布新propensity findings及扩展protocol。精确v1补充证据 https://arxiv.org/html/2603.25326v1 ，不以当前v4替换，不声称v1正文已证同刻co-release/首公开。官网已链接该论文身份；论文仅解释本次拟采用窄命题。

准入：操纵行为计数不拥有对人的结果真值；过程风险与belief/behavior outcome要独立定义，跨域/locale的baseline和人口不能共享一个release分数。2+2+2=6，安全反证受影响内容深入。root完整officialcore准入已通过，必要v1§2/7/8及H和当前owner对照实际已核；实际Ch66两段/邻接/末注非作者POST通过，本日日级Gate亦通过，实际范围与未核边界见正式§6。

实际必要读：v1§1–2/4–6 L77–206，§7 L196–254、§8 L255–302、§9 L303–324、AppH L846–853、AppL参与者分布L975–984。无需全FSF、旧card、全部实验stimuli或fullversiondiff。

- §1/4：Gemini3Pro case，扩展此前modelcard/FSF。新增propensity和多domain/locale细节，而非所有efficacy数据首次公布；不重复记两个家族。
- §5/6：9study/10,101 crowdworker，UK3590/US3749/India2762；每domain随机分配约三等分explicit（covertgoal+manipcues）、nonexplicit（covertgoal但不造假/欺骗）、static flipcards。最少5轮AI交互，控制非AI。所有条件方向性partialinformation；并非同交互强度对照。政策话题随机，health话题selfselect；finance/HMP、supplement与nonprofit虚构且debrief，没有真实投资或实际harm。
- §7.1：belief0–100按初始方向分强化/flip（50归强化），不得把不同分母混为概率；行为分inprinciple与bonus monetarycommitment，分别relative baseline oddsratio，不是所有真实伤害。
- §7.2：8cue perresponse propensity，按包含至少一个cue/每特定cue分别计；只publicpolicy有validatedjudge。不是三个domain都验证的通用危险率。
- §8.2policy两AI条件outcome无显著差异，与§8.3cue30.3% vs8.8%并存；§8.4 fear/guilt与belief关联负，othering/environmentdoubt关联正，behavior未观察显著关联。只相关结果，不是cue无因果影响或两条件等效证明，不把不同domain排行归因模型能力。
- §9：baselinehealth focusgroupreviews本来更强；参与者/guardrail/体验也是替代解释。按domain/locale绑定evaluation支持，非受控域间因果定律；文本dyadic实验不覆盖群体影响、campaign、音视频、personalized/subliminal vulnerablepopulation或真实deploymentharm。
- AppH：clearpositive/negative专家2–5人validation accuracy.948/precision.928/recall.938；challenge upsample先前judgepositive且无obviousnegative，updatedjudge对两普通human accuracy.573/precision.699。不同标签population不能直接当纯generalizationgap，Krippalpha.15与-.046不是稳固一致；仍反对把高clearcase accuracy当无条件autorater真值。

可采用：过程harm信号即使没有测到用户结果仍需独立治理；低cue频率也不证明人未改变判断。Evaluation须保存cuedefinition/judgepopulation和humanoutcome/baseline/domain/locale，不让一端代理另一端。Costs是伦理招募、人工研究与judge校准；缺humanoutcome保持Unknown，deterministicpolicy/behaviorprobe继续负责自己的范围。

Books实际对照：Ch66 Self-report/BehaviorProbe/Deployment953–985已有一般证据分层，AgentOutcome735–880已有执行行为与environmenteffects，AcceptanceCard3061–3070已有四诊断但没有同一次人机互动中manipulativecue与belief/behavior定义的分离。唯一owner PLATFORM-EVALUATION-SYSTEM，实际Self-report首段后/DeepResearch前当前960/962两自然段+末注5208。root实际读948–978/5208与65→66→67入场交接，POST通过、窄锁释放。未改Policyatomictenets处、不写Ch72重复主体；未复现实验，v1public未证同刻。
