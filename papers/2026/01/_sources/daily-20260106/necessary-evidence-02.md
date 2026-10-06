# Jan06 必要证据停点（二）

本记录只保留实际读过的精确v1核心、反证和当前owner局部；不是完整日级验收，也不冻结候选。未读范围仍是普通工作。身份日期仍须从本日原字段与官方公告合取，不把Submitted或registered等同公开。

## [RIMRULE 2601.00086v1](https://arxiv.org/html/2601.00086v1)

实际读§2.1–2.3/3：ground-truth训练失败定位与EBL规则、Domain/Qualifier/Action/Strength/ToolCategory符号检索，先filter可用tools再检索规则、转成advisory，不是执行授权。MDL的二元熵项在全对/全错都为0，不是单调准确率指标；greedy不证明全局压缩最优。Table3跨model/tool基准非统一改善，Llama rules→GPT4o的ToolHop 58.1→57.4负侧保留。

现Ch77 953–977实际已有scoped advisory规则、失败价值/source-version与greedy非最优；拟新增是此受限证据，不授普遍规则迁移。后续已actual补读§4全部与成本/MDL反证，core-2601.00086v1-supplement.json保原段；α是同训练失败集tradeoff，不是heldout可靠性，全错熵0并非无风险。具体已有覆盖已送root，非因主题已有降分。v2实际public事件未定（Submitted Jan5T04:14:46Z，Updated Jan6T01:58Z窗外），不把v1当v2审过。

## [Online DT 2601.00167v1](https://arxiv.org/html/2601.00167v1)

实际读§3.1–3.3/4.1/4.3，ratio核心原段缓存core-2601.00167v1-ratio.txt。行为按g_online采样，事后替换成g_actual再用旧policy(g_actual)作denominator，不是原行为分布；这是有条件反例，不否定所有hindsight方法。sub-trajectory组必须同reset state；L_eval额外环境步骤有成本；不可reset分支训练TD3 Q辅助，所以pure RL不等不加辅助模型。sequence joint likelihood而非geometric mean仍需保条件状态。

D4RL MuJoCo/Adroit/AntMaze、3 runs；outer iteration不是compute或环境步数等预算，作者自身说明ODT+TD3约100倍gradient updates而本文更多环境交互。未复现，不授全任务SOTA。

TRAIN-GRPO：现Ch33 118–152明示ratio分子/分母同x/history，1988–1998明确on-policy action source不保证conditioning state一致及重建equivalence。固定2+2+2=6；root实际原§3.1与该局部正文核通过具体已有覆盖，reset/Q特定配方仅报告，不复制正文。

## [Noise Optimization 2601.00090v1](https://arxiv.org/html/2601.00090v1)

实际读§3/4、A2/B：冻结生成器，batch4初始noise联合优化quality+hinged diversity+prior-radius；pink FFT再归一化不证明Gaussian边际。PixArt/SANA/SDXL Turbo/Flux，GenEval553、T2I50每prompt400样本；选择64取4与100步优化非compute matched，HPS有退步。A2阈值来自baseline seeds，不是可迁移quality约束。单A10080GB、三seed、SDXL/Flux .345/1.092秒每步，不等端到端请求SLO；precision=Not Disclosed。

新增拟采用对象仅该局部quality/diversity noise recipe，1+1+2=4；不把成熟tradeoff算原创。现Ch24 213–215已区分联合batch noise coupling保边际与optimization改边际，但评分不是因为Books已有而降低。关闭身份/日期及仅报告理由尚需归档。

## [JP-TL 2601.00223v1](https://arxiv.org/html/2601.00223v1)

实际读§3.1–3.2/4.1–4.7/5.2–5.3：70 JA/EN候选+20从200冻结anchor；每候选单独与同anchor graph作BT，候选增删不改其他候选fit，但当前candidate加入centering可整体平移；不授temporal endpoint不变。seed42的A/B orientation非双向重复，Gemini2.5Flash temperature0仍不是deterministic证据；约1400judge比较为建模成本，人类agreement总N=Not Disclosed。COMET族/低质量离群及定性模型对照不证明一般人类排名正确。

具体增量是candidate-pool coupling与fixed-anchor score contract分开，固定2+2+2=6；原Ch66相对偏好与动态fixture未完整覆盖frozen-anchor逐candidate独立fit。root实际core/Ch66 240–289核通过并授权：anchor参数每fit估计、centering含candidate，不能称锁死全部anchor数值。实际正文261/263+首注4275的root非作者actual POST已通过，锁释放；不称日级完成。当前core-2601.00223v1-selected.json保存未截断必要原段。

## [Mathesis 2601.00125v1](https://arxiv.org/html/2601.00125v1)

实际读§2/3/4/5.2 Algorithm2/5.3/6及A1–A3：zero iff semantic truth的忠实encoder是前提，不是连续优化自己证明；非负smooth不能保证NL formalizer或全局convergence。collinearity/perpendicular残差允许degenerate对象，需类型/非退化约束。Hermann理想成员界是借用成熟原理，不按该原理给原创分。§7只有preliminary miniF2F探索，无数值规模/对照，不授已验证自动证明系统。

ordered hypergraph scope+continuous witness是潜在新增命题，2+1+2=5待具体贡献与owner核；不能用未开源提前排除，也不能把必要faithfulness未证写成正面保证。现formal verifier owner需对照，尚普通工作。

## [GRIT 2601.00231v1](https://arxiv.org/html/2601.00231v1)

实际读§2.1–2.4与§3 Table1必要范围。Kronecker空间协方差/EMA/damping/Cholesky在LoRA factor梯度上可用；原display把r×r矩阵夹在d_out×d_in的deltaW梯度旁有维度不一致，不能按原式授exact natural gradient。PA/PG投影可压抑方向但不自动删除optimizer state，也不证明outer basis可自由转动。NF4/bf16的3B/8B QLoRA各任务，Alpaca/GSM8K/BoolQ有负侧，Dolly/QNLI改善不是普遍结论。

拟新增仅局部factor-space优化配方，1+1+2=4，不把成熟Fisher/有效rank principles算原创；但原exactness相关争议保留，若实际采用此保证必须深审受影响命题。现Ch30 165已有optimizer/rank/谱影响，尚待身份日期及不进一步采用的具体归档；runtime/完整A8未读，不称全面评估。

## [Deep Delta Learning 2601.00417v1](https://arxiv.org/html/2601.00417v1)

实际读§2/3、已补§4.1/4.2：A=I−βkkᵀ/(kᵀk+epsilon)，同β写入kvᵀ；ideal unit k/epsilon0仅一方向eigenvalue1−β，其余1。β=2sigmoid、反射/identity/singular边界是固定输入条件，不是含input-dependent k/β/v的full Jacobian保证。§5是Related Work而非评估，本论文无实验节，不能继承此前错误‘§5评估待读’假设。固定2+1+2=5，具体长期gap深入；root原源与Ch17 405–430 owner核后授权，实际430/432两段+714首注已通过root非作者actual POST，锁释放。Ch16末/Ch18首及depth→rank-one→多流衔接实际已读，未采实测收益。

## 其他实际部分读取（早期停点，以下为后续更正）

后续Spatial4D已补§3建设/evaluator；MetaJuLS已补3.3尾/4，§4.2十语言与4.5混task各自设置明确，撤销English-only中央冲突猜测，root必要source→owner及Ch51 actual POST通过。SphereNN/FromSight已读必要core，FromSight root具体Existing通过。Journey/Wild/MalOpt具体已有覆盖、MAESTRO/M2S/ActErase实际Books POST、RWR/CSS中心争议与TG局部recipe关闭已各获root必要复核；分别见security/evaluation、formal-and-control及本日README。AEGIS00561实际必要3.3/4.5及Ch66 rubric/judge任务/人工agreement已由root核通过5分标准仅报告；这些后续状态不抹去早期未读停点与反证。

## 最终处置同步（2026-10-02，日级Gate待root）

当前最终处置：RIMRULE6具体已有覆盖、OnlineDT6具体已有覆盖；Noise/GRIT4关闭仅报告；JP-TL/DDL实际整合POST通过；Mathesis5蓝图仅报告；AEGIS5标准仅报告。root逐项必要命题/owner或关闭校准通过，不采用RIM熵单调正确、GRIT显示公式exactness、Mathesis未验证faithfulness保证；Sphere另按贡献前关闭处理。未采用的runtime/理论拓展不是本窗待办。
