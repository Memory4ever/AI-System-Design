# TERMINATOR / ReBalance 必要Source有效复用与Books处置

仅本17补03/16自然日；2603.12529v1与2603.12372v1完整AB已独核，首arXiv日字段在SUP_DATACITE_BATCH，当前全年同ID/同题名定点未见有效同事件处理。root本轮非准备者实际必要核心、实际Ch20具体论点审阅，review_mar17_18另独读关键桥梁；以下复用具体原证，不沿旧done标签。本轮Books背景已重读，作者actual Ch20 247–303完整budget→feedback→semantic steering与Ch19/21交接已读。两项原潜力2+2+2=6不因争议改分。

## 12529 TERMINATOR / MODEL-SAMPLING 一段PRE待核

[exact-v1](https://arxiv.org/html/2603.12529v1) root实际§2–5/Table2：离线Extract→Identify→Verify，以原full-CoT最终答案hat a首次逻辑到达构造监督，而不是ground-truth correctness；causal copy最后Transformer block+binary head，近期10多数且p≥.7注</think>，不是无阈值，只不在targetdomain校准阈值。文before0/after1与Eq3 y=1(i<i*)反向；HORL截断后保持同答最早点不等语义首次出现，经验Fig6不证明精确optimal。对应实际标签/训练实现、labeltarget与HORL关系必须同一精确请求，未取到前不认证该recipe/最优保证。

受测Qwen3/Ministral3 8/14B、MATH/AIME25/HumanEval/GPQA；GH200 batch1/no prefixcache只MATH子集，TPOT开销7.5–10.8%不可隐藏在tok减少内。precision/concurrency/tailSLO Not Disclosed；token下降/局部latency不等fleet保证，未核artifact/复现。reader实际§2.1–4.2已核标签/HORL冲突。现Ch20 budget-force/统计误停与双向proxy反馈存在，但没有‘完整轨迹离线答案到达标签→在线因果exit建议，保持原答≠正确’差额。唯一MODEL-SAMPLING，拟统计wellposed误停段后、轨迹内Feedback标题前一段，不认证矛盾精确标签：

另一种early-exit建议可以用完整轨迹构造离线监督，再让因果读出在当前prefix上预测是否已出现原轨迹的最终答案；它预测的是与原full-CoT答案的一致性，不是答案正确性，也不保证截断后一定生成同答。[TERMINATOR的受限证据](https://arxiv.org/html/2603.12529v1)把label生成与在线停止分开，但文字/Eq3标签方向及最早同答与语义首次到达的关系尚未明确，不能把其精确recipe或经验结果称为已证实最优。离线完整生成、标注/verifier、额外读出与阈值/窗口均付费，局部token或batch1延迟下降也不授fleet SLO；labeltarget、模型或任务失配时保留普通EOS、硬budget与独立答案verifier，不以“已到达原答”批准正确提交。<!-- source-family:SF-2026-ARXIV-2603-12529 -->

## 12372 ReBalance / MODEL-SAMPLING 已有覆盖与实现隔离

[exact-v1](https://arxiv.org/html/2603.12372v1) root实际§3/B1–B3/§4/Table1–3/D；reader实际§2.1/3.3–3.4/B3桥梁与Ch20 247–300，限定NC通过。低confidence高variance→O/高confidence低variance→U只是proxy，不是真实正确稳定点。500 MATH离线采样、逐model固定layer/prototypes/vector/controlsurface、每step首token双向注vector，非stop classifier。current completed-step的token几何confidence却作用same-step首token，noextraforward缺在线可用时序桥；Eq11 piecewise与B3两smooth additive gate、fitsigmoid与finalsign-tanh也不合并成一个确定实现。实际causal confidence/注入时刻+实际g同一请求，未取得前具体recipe/noextra费用隔离，不绕争议认证。

实际Ch20 264–288明确request budget→trajectory feedback→bidirectional hidden control、confidence≠correctness、checkpoint/tokenizer/layer/vector/window/threshold/artifact绑定、外层deadline及费用/旧EOS退路，确实承载可支持的限定机制，无新差额须改Books；不因为同owner主题就NC，也不新增重复段。受测主要HF五backbone(1.5/7/14/32B+Pangu)、8RTXPRO6000、temp.7/top-p.95/max16k，不因数学/code/GPQA/StrategyQA评测当Science应用关闭；precision/batch/concurrency/SLO未披露，tok减少不授TPOT/TTFT。Source安全隔离与actualNC已由reviewer独核通过；本轮无写/无需POST，最终Report DAY尚未通过。
