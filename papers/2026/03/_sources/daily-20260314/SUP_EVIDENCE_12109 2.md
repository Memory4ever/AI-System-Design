# 12109 必要Source与中心理论争议

当前结果：root作为非Source准备者实际必要声明/完整对应证明/有限envelope反例、局部实验/代理与Ch33邻接复核PASS，5分争议/暂缓Books0正式同步。下文待核是原提案时停点；具体复核在 `SUP_INDEPENDENT_REVIEW_20261009.md`，不授DAY或全POMDP反例。

mar14_supplement，Mar13 BJT自然日。实际完整v1题摘、七作者与当前说明 `SUP_ABS_12109.txt`：Deyu Zou/Yongqiang Chen/Fan Feng/Mufei Li/Pan Li/Yu Gong/James Cheng；v2日期May31只是版本信息，未有具名早稿/撤回/纠错提示，不据版本号遍历。精确v1 `https://arxiv.org/html/2603.12109v1`，`SUP_NECESSARY_12109.raw/txt`，GET200/780303B，`SUP_FIFTH_MINIMUM_MANIFEST_RESULT.json`。本窗official owning/findable/registered上下界与v1正常公告批次日级门由root实际核PASS，见 `SUP_DATE_FIFTH.md`；不是Submitted或注册单独决定firstpublic。

## 实际必要范围与有效局部

实际读B25–147（§2–5完整关键方法/Equation2–6/Table1–2/§6）、B192–228假设B1/B4–9、B247–272 B12–14/B17与oracle定义、B390–450 B13末段/B17/B19完整证明及任务入口、B465–491 C3协议/critique/训练配置。C3 prompt超长块仅定位，没有声称全部提示/附录/全部证明审阅；代码/复现未核。必要充分即停。

AS由query决定observation，BT由explicit候选confidence更新；固定query换oracle/rule/human BT与把反馈替为Unknown的受限干预支持两接口可分别诊断，但explicit报告向量不是LLM内部真实belief、cosine/GT margin不是一般信息真值。PE的non-dominated pair为信息代理而非必然information gain；MediQ的模拟患者Qwen14B/四假设不认证临床安全。AReW把正、负critique steps各自平均loglikelihood作gap；两组都存在才更新，否则0；可加λu到PPO/GRPO/GSPO的advantage，正负权重和0不等无偏、原objective不变或共享参数无干扰。需要GT/参考诊断项、额外counterfactual调用，非部署免费oracle。

C3更细限定：MediQ uninformative feedback要求margin不变，informative时比较Unknown反事实更新距离，而非所有BT都直接GT正确标签；FloDial Yes AS+1/No0/Unknown−1，No不是无信息，BT有信息时要求GT confidence提高。PE BT按GT相似改善，只在informative query开启。不同task的critique语义不能合并为通用正确性。8B200单节点/FSDP/BF16/vLLM TP1/temp1，PPO200步对GRPO/GSPO100步、GRPO每prompt3responses；同algorithm内方法对照不授权跨algorithm同预算。全wallclock/critique总成本/concurrency/SLO/多训练seedCI未必要核，Not Disclosed。

Table1 AS+BT不总优于AS-only（Qwen FloDialEasy41<43.67、Llama PE-F D6 54.65<56.91/MediQ70.75<71.75），λ过强会塌缩，Table2噪声行不是逐格严格单调。局部收益仍保留，不据中心理论争议抹掉实验。

## 必要理论核与精确反例

B17 B265–267仅假设ω0在Rδ,ε，声称ANY符合B14 one-step drift bounds的projected evolution在K步前不可离开；K用I0作分母、ε作分子。其完整证明B396把uniform o(η)直接升级O(η²)，B407另引入C_BT0≤I0的初始化条件（命题没有写），B408–412换成u_star≤min(δ,ε)阈值。这些不能静默补进已发布命题。

对它“any consistent envelope evolution”字面量给直接有限反例，不声称构造了全部原POMDP：δ=ε=.1，x0=(I0=.01,C_BT0=.0995)，η=.01，α=βI=βC=1，c0=C=0，m=2。按其Eq24允许的上包络取等号x1=(I+.01*C_BT,C_BT+.01*(I+C_BT))=(.010995,.100595)，第一步已经超过BT ε；其K=floor(50 log10)=115。初始严格在R内，one-step各正增量恰满足该envelope；缺失的C_BT0≤I0正是证明不能应用的点。这里只否决发布的envelope普遍步数命题，不否决所有真实优化动态都会观察到锁定，也不外推原B12/B14全部不成立。

B19/main Prop4.1的“weighted critic accuracy>.5 ⇒ escape改进”不能作实际优化一般保证：B429–431把两个gradient expectation都设在oracle-belief trajectory law，实际方法是模型belief on-policy；B433把inner product of expectations换成同trajectory expectation of inner product，不是一般恒等式；B434又明确for simplicity删除cross-time terms，随后B435–443仅该diagonal近似才出现W(2Acc−1)。shared parameters、跨时项与分布bridge均不能由多数critic正确自动消除。保留作者公式与近似，不把理论证明为真。

## 评分/Books处置提案与owner

拟2+1+2=5：终局奖赏不能区分信息获取/证据吸收的受限干预及step signal重要边界2，训练policy组件1，信息/credit资格稳定2。实际深入受中心理论冲突触发，不用争议减分或排除。当前提案 **争议/暂缓Books0**，不授K步锁定、>50%critic保证、普遍逃逸或临床/生产能力。

实际Ch33 2035–2145完整controller→domain→task mixture→多channel聚合/诊断，另1730–1768 fork belief probe→typed/rubric credit邻接与Ch32/34入口。`TRAIN-GRPO`拥有过程credit和信息采样接口，现正文有per-channel guardrail/额外probe、reward correctness与controller observation/action；尚无AS/BT相互耦合的该具体对照命题，故不是“已有覆盖”关闭。但中心理论冲突未独核前不拟写Books。局部实验与代理接口可继续作为报告证据，不让理论错误否定其存在。

精确重开条件：本B17修正初始化/阈值/余项条件并给有效证明；本B19补实际分布bridge、正确gradient inner-product计算/保留跨时项，或独立支持一个不依赖这些保证的matched-cost AS/BT采用命题（真实proxy、各channel反退/critic费用/heldout）。本次仅请求上述具体缺口，不追全版本/代码。尚待非Source作者实际原证、反例和处置复核，不授formal候选/DAY。
