# Apr17 V3：第四组十项有限独立语义复核

## 范围与裁决边界

仅复核 14488、14644、14723、14501、14548、14564、14585、14604、14634、14682。复用作者必要证据定位，独立打开 exact-v1 必要方法、评价与关键反证，并比较实际 owner 正文；不扩展 536 raw / 88 candidates，不遍历附件或版本历史。评分维持作者：四项 `2+2+2=6`，六项 `2+1+2=5`。

PASS 仅表示限定的 source→owner 判断可用。窄 gap 仍是提案，必须实际落 Books、复核衔接后才计 Integration；本文件不证明整日日期、Coverage 或 Complete Gate。first-public availability 由独立日期审计负责。

| ID | 独立裁决 | Score | 实际 owner / 连接 |
| --- | --- | --- | --- |
| 14488 | PASS — Narrow Gap Proposal，隔离必要性定理过述 | 6 | Ch76 `AGENT-RAG` |
| 14644 | PASS — No Change / Existing Coverage | 5 | Ch72 `PLATFORM-SECURITY` |
| 14723 | PASS — No Change / Existing Coverage | 5 | Ch78 `AGENT-TOOL-CALLING` |
| 14501 | PASS — Report Only | 5 | Ch22 `MODEL-LONG-CONTEXT` 为连接 |
| 14548 | PASS — Narrow Gap Proposal，配对不是完美因果分解 | 6 | Ch66 `PLATFORM-EVALUATION-SYSTEM` |
| 14564 | PASS — Narrow Gap Proposal | 6 | Ch33 `TRAIN-GRPO` |
| 14585 | PASS — Report Only，修正实验单元 | 5 | Ch74 `AGENT-PROMPT` 为连接 |
| 14604 | PASS — Narrow Gap Proposal，仅 adaptive detector threat 差异 | 6 | Ch72 `PLATFORM-SECURITY` |
| 14634 | PASS — No Change / Existing Coverage | 5 | Ch66 `PLATFORM-EVALUATION-SYSTEM` |
| 14682 | PASS — Report Only，agreement proxy 不是路径收益 | 5 | Ch48 `INFER-SPECULATIVE-DECODING` 为连接 |

## 1. 14488：语义 Anchor 之后还可能缺权威后继

[exact-v1](https://arxiv.org/html/2604.14488v1) §2.1、Definitions 6–7、§3.2 Theorem 4 及其证明：先找到 entity-scoped semantic anchor，再沿 authority/supersession 关系补齐 closure，最后筛 active frontier。检索过期材料后要求同时看见其 superseder，不等价于单纯按发布时间过滤。理论依赖静态 corpus、已知确定性的 authority partial order、理想 scope/recovery 与 deterministic answer function；真实权威图不完整时不能照搬完整性保证。

Theorem 4 的必要方向把 AnswerCorrect 推到完整 active frontier，却未由 deterministic answer function 推出每个 frontier 元素都不可缺：两个 active documents 独立给出同一答案，只取其一、未取过期文档时，仍可能同时满足 AnswerCorrect 与 NoIgnoredSuperseder。因此不采用普遍 iff 结论；这一局部反例不否定主动补检权威后继的机制。

实际 [Ch76](../../../../../books/part-07-agent/76-rag.md)“Temporal Retrieval 要在 Admission 前验证事实有效期”已覆盖 query fact date / source validity / corpus revision 的 admission，缺的是低语义相似度权威后继可能根本没有进入召回的责任。最窄提案：anchor→entity-scoped authority closure→reader admission；图或 scope 缺失时标 Unknown，给出补检成本、错误 supersession、跨 entity 污染与旧语义召回仍适用的边界。不要把 corpus benchmark 成绩提升为通用正确性或线上 SLO。

## 2. 14644：行为拒答不是参数影响删除

[exact-v1](https://arxiv.org/html/2604.14644v1) §3.2–3.3 与 Appendix G：以 paraphrase 正例和高词汇重叠 hard negatives 训练 sentence embedder；forget DB 追加请求，cosine 阈值决定拒答还是调用权重未变的 LLM。作者明确区分 behavioral suppression 与 parameter deletion。阈值同时改变拒答覆盖与 retained utility，不能由权重不动推断 utility 不受影响。

Appendix G 中 persona/payload 拆分和编码攻击可恢复知识：persona recall 在阈值 .8/.7 为 78%/96%，payload 拆分为 41%/>65%；这些数字仅属于对应攻击与阈值，不是全产品概率。base64 还可能消除 embedder 所依赖的语义线索。不采用“唯一实时”或无完整条件的秒数，也不把安全测试的学科内容当 AI-for-Science 新准入。

实际 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)“Unlearnability 与 Unlearning 不能共用一个浅层遗忘分数”明确分账 prevention、parameter influence、behavioral withholding、relearning resistance，并要求 retained utility、攻击验收与高风险回退。采用命题已经真实存在，Existing，不另写新 unlearning 案例段。

## 3. 14723：授权有效仍可能绑定错实体

[官方 PDF v1](https://arxiv.org/pdf/2604.14723v1) §4–5、§7.12 / Tables 3–5：permission-aware typed manifest 约束模型 proposal，consumer 保有业务逻辑、authorization、persistence 与 side-effect。对照 B 也保留 consumer backend，不能写成直接裸数据库对照。

CRM / GPT-4o-mini / 25 trials 中 C 23/25 成功、0/25 unsafe；B 17/25、2/25 unsafe，其中语法和权限有效但 wrong-entity mutation。ambiguity 子集只有 3/4，不是普遍零失效。手工 81 秒来自 industry benchmark，不是同组实测，不能照录 13–18× 或归因每层独立效果。

实际 [Ch78](../../../../../books/part-07-agent/78-tool-calling.md) Text2Opt binding 段已把结构 proposal 与确定性实体、单位、索引绑定分开；不唯一则拒绝并请求补信息，模型不持有 commit 权。与现有 identity/effect 主线共同承载本文窄命题，Existing。hardware、precision、并发及生产 SLO 不足，不补企业案例摘要。

## 4. 14501：交错计算改变受限模型的信息通路

[exact-v1](https://arxiv.org/html/2604.14501v1) §6 Theorem 4：input-interleaved thought 与 post-input thought 不同；后者不能恢复此前通信瓶颈丢失的信息。generalized finite-precision SSM 的模拟方向构造任意 matrix function，例如把 streaming transition 编入 B(y)，并令 A=0。形式上的固定转移次数没有约束计算 B/F 的代价或保证它是可学习的现实架构。

仿射 map summary 的 d²p 通信量也不是实际递推 state 的 dp bound。只保留受限 formal model 的计算/信息区分，不宣称全部 CoT 无效或提供 Mamba 可执行配方；未审计无关独立下界证明，也没有把理论当 benchmark。

实际 [Ch22](../../../../../books/part-02-model/22-long-context.md)已区分长上下文计算、状态与读取责任。本文具体 formal expressivity 结论具有报告价值，却不足推出通用架构选择，Report Only，不虚称全部理论已在 Books。

## 5. 14548：同音频的感知 Cue 与规范决策分别验收

[exact-v1](https://arxiv.org/html/2604.14548v1) Appendix J / Table 42：保持同音频，把 normative action 问题改为较容易的 cue-recognition probe，并比较 SAR 与 text-explicit-cue reference。cue 可听见、被正确分类、决定正确行动是三件事；识别 probe 高分不是行动正确证书。三个人工标注者验证 audibility，不是所有规范 gold 的真值证书。

例如对应 Qwen3-Omni child-voice probe 90、SAR .5，child-presence 91.5/.5，是指定合成测试结果。不同 prompt 改变任务要求，不能完美隔离内部因果；UnsafeBackground 的 NSFW-presence probe 与“是否适用于教学”的规范标签也不是同一命题，不可把二者机械当严格上下界。22 个英中任务和有限模型不推出全音频安全表现。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已有 perception/reasoning 与 typed predicate，却未明确同音频 cue sensor / normative decision / text-cue reference 的配对接口。最窄增量是把这三轴及提示差异写入 EvalSpec，保留 probe failure 与 decision failure、联合置信区间及来源身份边界；年龄或背景音 cue 绝不能成为权限认证。不是把 22 项 benchmark 清单写进 Books。

## 6. 14564：共享 Credit 参照不等共享 Policy Token 更新

[exact-v1](https://arxiv.org/html/2604.14564v1) §2.1–2.4 / Eqs 3、7–8：节点是完整 candidate solution，以生成/修订扩展搜索树；Thompson sampling 选择 agent/node。节点有自己的 reward/public tests，parent/sibling 构造参照，shaping 为 r+γΔ。各 agent 的 policy loss 只用自己生成的 T_j，树级统计可共享；不能把不同 policy 的 token ratio 混为一池。

主训练使用 7,992 个筛选 DeepCoder prompts。等 per-agent 样本与 update steps 不是等 wall-clock；AReaL-14B 的 pass@8 反例不支持全面支配。单模型 shaping 曲线不证明普遍降低方差，也不证明修改后的目标无偏或完全不变。

实际 [Ch33](../../../../../books/part-04-training-system/33-grpo.md)已有 shared-prefix matched branches、执行树和 prefix/retry 成本，但缺 heterogeneous policies 下共享 credit reference 与各 policy 节点更新 ownership 的明确区分。最窄提案补在 tree credit 交接：共享结构/统计、保留 token producer 与 policy revision，再做分别验收。新增搜索、测试、调度与统计混杂成本；简单独立采样在低协作收益时仍合理。

## 7. 14585：不显著交互不能证明交互不存在

[exact-v1](https://arxiv.org/html/2604.14585v1) §3.1–3.2 / Table 1–2：Study 1 是两个 executor（Haiku 4.5 / Nova Lite）×三个任务（HotpotQA / MBPP / XSum），统一 A→B pipeline。10×10 prompt grid 中每格 n=30 是 benchmark samples/questions，不是 30 次独立生成重试；question blocking 后 F<1 / p>.52 不证明不存在交互或 joint optimization 永远无用。

Study 2 六方法×四任务×三重复共 72 组 Haiku runs，49% 低于 baseline 是此合同下反证，不是普遍 coin-flip 概率。best-of-10–20 在同 20 题选择 headroom 存在选择偏差；instruction tuning 压缩 phrasing 的解释没有独立因果干预。

实际 [Ch74](../../../../../books/part-07-agent/74-prompt.md)“自动 Prompt 优化要先区分设计信号与采样噪声”及 Ch66 已要求重复测量、选择/验收集合分离。报告保留具体负面结果，不把所有 compound-AI 交互理论虚称 Existing；Report Only。API 预算不是跨任务统一总 compute，生产 SLO 未给出。

## 8. 14604：知道 Detector 的攻击者可改变原检测面

[exact-v1](https://arxiv.org/html/2604.14604v1) §III–V、VII–VIII：white-box 参数访问下，audio-only 修改经离散 tokenization 的 gradient approximation、多 context / attention steering 与 reverb 隐藏注入；不适用于任意 black-box 产品。13 LALM / 13,000 普通目标与三 tool models / 四工具实验分开，phrase PISR 与行为 BMSR 分开。

原 attention PCA/SVM precision .98 / recall .93；攻击者知道 detector 后把 steering κ 降至 .01，recall .69 / precision .90，而 BMSR 代价有限。§V Implementation 明确 carrier 15 秒、train/test 各 100 个不重叠 instructions、batch 4、默认 κ=.015，**全实验 bfloat16**；作者“precision ND”须纠正，并发与生产 SLO 仍未披露。

实际 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)已经承载跨模态 source identity 与 task intent / 独立 controller 分权，以及 white-box signal 仅为 sensor 而非 reference monitor；不要再写通用 audio identity 段。真正窄 gap 是同一 model revision 下 detector-aware 攻击主动改变 calibrated surface，需要 adaptive-threat false-negative 验收及互补检查；不能只等模型升级再重校准。保持模型外权限控制为最后边界，不称 detector 完备或泛化攻击成功率。

## 9. 14634：选项密度不是能力真值

[exact-v1](https://arxiv.org/html/2604.14634v1) §3、§6–7 / Table 4：30 个 Korean orthography targets，N=4/10/20/50/100，每 target/N 1,000 trials，五模型 temp0 / exact index match；同 target 不等同选项内容完全不变。八种 padding（前后×四类）、约 2K–5K 长度帮助拆轴，但 semantic neutrality 不完美，HyperCLOVA X / EXAONE 有模型依赖反例。

gold position 用实际响应 CDF 而非假定均匀，N100 共 30K responses；低 N ceiling 不是本体能力、高 N 也不自动更可信。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已有 matched permutation、direct/CoT interface 及 Position–Content–Length factor grid，本文采用边界真实存在。Existing，具体 benchmark 结果留日报，不另增选项百项案例段。hardware、precision、SLO 未完整披露。

## 10. 14682：节点概率平均不是真实 Accepted Path

[exact-v1](https://arxiv.org/html/2604.14682v1) §III–IV：TinyLlama1.1B / Llama2-7B-Chat GPTQ4b、两 Tesla T4，四域各 50 prompts，input≤512 / output≤64，depth3 / max8 nodes / root3 / branch2、temp0 / use_cache=False。对 top-k/greedy 节点记录 min(1,p/q)，没有执行完整随机 accepted path 与 residual correction。

Eq3 使用各深度 mean α 乘积，却未提供独立性或 conditional path weights；一般 E[α1α2]≠E[α1]E[α2]，同一 Bernoulli(.5) 两层就是 .5 对 .25 的反例。99,768 nodes 不是独立 prompts；chat 1.065 是局部 proxy，不含 draft、bonus、full-forward 等执行成本，不能称加速或 RLHF 因果。

实际 [Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md)“Exact Acceptance 机制”与“接受长度小例子”已分目标分布、真实路径、rollback 及 wall-clock。本文有限 agreement 诊断保留报告，不以局部公式问题否定全部测量，也不把 proxy 变成通用 recipe，Report Only。

## 结果与后续

四个窄 gap 提案、三个实际 Existing、三个 Report Only。必要事实修正：14585 是两 executor × 三任务、每格 30 个题目；14604 精度已知为 BF16；14548 paired prompts/labels 不提供完美因果分解。作者实际落 Books 后才可计 Integration。本文件只新增此独占 audit，不改报告、Books、日期 owner 或全局 checkpoint，不替代整日验收。
