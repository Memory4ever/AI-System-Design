# 04/20 首批九项独立题摘准入口径校准

非作者apr01于2026-09-27实际完整读取owner-replay库存九项标题/摘要，核当前ROADMAP相关节点与作者 `v3-reopen-notes.md` §第一批额外题摘。本次只判断贡献入口/关闭口径：未核所有exact-v1正文、日期或withdrawal，不评分、不签Evidence/Books/日Gate，不扩447库存。正面准入仅待必要审阅，不等结论采用。

## 拟准入侧

- **15357 FLAME：PASS。** 摘要不是简单频率曲线替换：CPU kernel-launch与GPU执行异步重叠→动态pipeline bubble→layerwise/wholemodel latency估计，context长度使全频率profiling爆炸，稀疏profiling是有约束的新执行模型入口。对应Ch70成本/执行资源，Ch49 host/kernel交接；无需是最大LLM才能有贡献，但摘要的deadline/省能/估计误差不能先当普适SLO，留必要evaluation合同。
- **15368 LogJack：PASS，保护行为需必要深入。** 摘要直接给same payload isolated vs cloud-log嵌入、检测后sanitize-and-execute两种控制边界，而非只新增攻击数量。对应Ch72低信任日志输入→可执行remediation权力，Ch66配对评估；必须核command execution是实际执行还是文本判分，API/model/repeated-trial/guardrail条件，不把RCE文字率先升真实remote effect。
- **15383 TCD：PASS。** 原音频与temporally blurred slow-path重新编码→next-token候选集contrast→uncertainty/audio-reliance gate，是特定模型对输入时间信息的解码干预，超出普通音频任务分数。对应Ch23音频表示/Ch24生成接口及Ch48执行成本；两个view编码、候选限制/门控与backbone反例需必要核，不将语言prior或blur当唯一已识别因果。
- **15439 One-Shot Flows：PASS。** 摘要限定independent endpoints、conditional velocity与straight-line flow，Gaussian构造与充分分离多峰目标不可能形成结构对照；直接影响一步生成/rectification机制可行性，Ch24 owner。不能从此拒绝所有few-step/蒸馏、相关endpoint coupling或非straight flow；定理须按真实假设必要核，不因理论而无差别全证明附件。
- **15461 PersonaLedger：PASS。** 有DP统计输入仍被LLM prior覆写的时间/人口分布漂移，改变“生成器忠实实现给定分布”与下游utility分账；金融仅评价载体，不应按行业标签关闭。对应Ch27合成训练数据与Ch66生成器/分布有效性；不得把DP输入后处理的统计drift自动解释成privacy预算失效，AUC只是utility、非privacy证明，需要必要协议定位。

## 拟关闭侧

- **15343：具体前分母关闭PASS。** 单受试者autoethnographic案例与外部观察支持其个人现象记录，未隔离attention机制或prompt共存与认知变化的技术因果；abstract从单例推prompt-layer isolation结构失效的桥不足。关闭的是本项目可验证系统机制贡献，不是否定当事人经历、安全议题或所有prompt隔离风险。若有真正控制机制/可复算失效接口再定点恢复。
- **15468：具体前分母关闭PASS。** 摘要自行声明conceptual keynote/diagnostic agenda，六ring与三个worked case组织职责词汇，但没有新增可执行接口、状态条件或有据设计反证；不能因能映射Agent词汇进入分母。不是“概念研究必无贡献”，而是本篇未给当前知识链新的机制证据。
- **15475 NeuroMesh：当前关闭PASS，但理由应精确。** 摘要是多机器人C++/Zenoh执行栈、reduction/broadcast与CPU/GPU并行组合，cycle-time与E2E latency区分是有用方向；尚未披露超出现有模块化/通信-计算重叠原则的具体状态协议、压力条件或受控执行反证。不是因为含机器人/没有foundation标签硬拒；若必要公开摘要后有异步旧状态、deadline/admission/一致性等新接口证据才重开，不为验证名称而全文审。
- **15549 SGP broadcast mixing：当前范围关闭PASS，勿写成“非LLM所以无贡献”。** 摘要真实研究非对称mixing matrix与有向wireless DFL graph的收敛/通信联合目标；不否定该数学贡献，但当前项目主线的模型训练平台/collective状态生命周期尚无可迁移设计接口或反证从摘要成立。不能把DFL averaging与同步DP AllReduce等同。存在对大模型状态、通信执行/故障合同的具体压力桥时再定点准入，否则不扩一般网络FL图优化。

## 结论

九项五个准入/四个具体关闭口径通过；唯一建议是将15475/15549的关闭理由写成上述具体证据/当前范围边界，而非用“非foundation”“非大模型实验”作普遍硬门槛。不存在本次已证明共享模板错误需要扩到447的依据，未审的15351等不在此范围。实际全文/Evidence/日期与Books由作者继续，本次记录不代替其日级验收。
