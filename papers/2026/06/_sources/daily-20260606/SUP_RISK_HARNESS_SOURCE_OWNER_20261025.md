# Risk States / HarnessFix：首次必要与具体已有覆盖提案

作者`supp_jun06_close`，2026-10-25，仅Daily2026-06-06补Jun05。完整AB/current notice/联合Jun05资格复用R31。未核实现、图像素、真实运行或复现；本包是作者提案，不自签独核。

## Risk States 2606.06223v1

[exact-v1](https://arxiv.org/html/2606.06223v1)实际读§3–5、T1–4、A/B/C1–4及T5–9。拟2+1+2=5：从孤立generation activation到环境标签的next-step风险读出需entropy/context校准，原文受限行为反证改变单信号采用；reach1监测组件，durability2为监测人口与行为目标分离，未把通用安全原则作新机制加分。标准完成，直接反侧已足，未扩大所有引用。

token级reward-hack monitor由Control/Hack适配激活的SAE/PCA/线性classifier构成，mixed adapters未用于其训练；本篇不是重验generation detection。每reasoning segment提mean/final/late mean/slope，与entropy、budget、step、上次action、环境/affordance状态组合，logistic regression预测下一action的环境定义label，非监测器自己打真值。episode-grouped cross-validation、numeric preprocessing仅training-fold，避免同episode step泄漏；没有给出跨新环境/未来时间的已校准风险概率。

主要Qwen在GameableALFWorld，Llama次级、Falcon边界；文中未完整统一披露精确checkpoint/monitor层、全部fold/seed/CI、硬件与运行费用，不补生产适用。broad bad_action含invalid/regressive等，不等所有reward-hacking；explicit exploit是easy-grader/fake-completion等人为提供affordance。T1 broad activation gain .020、entropy .102、internal+context .164；explicit exploit却activation+entropy .131高于internal+context .111，不能宣context每目标都优。T2 Qwen Mix50 exploit .450/Hack .019，但rollout步人口609对2709、策略与访问分布同时变；饱和activation与行为不单调是受限反例，不识别唯一因果。

WebShop只有saved activation+entropy配置，无与ALFWorld相同feature ablation；buy与bad_buy标签不同，Falcon badbuy仅5阳性，在表中虽有数值仍不采稳定结论。TTC与时序诊断非单调，不宣激活必在风险前上升。steering只selected Qwen mixed regimes，gated不普胜、T3是selected效应，无完整任务效用/副作用矩阵；probe representation relevance不等完整防御。SAE/特征/熵读取、context标注、predictor/steering、全部rollout与独立outcome核验均计费。

具体Books比较：唯一`PLATFORM-EVALUATION-SYSTEM` Ch66实际完整读“白盒OOD先做LengthDeconfounding”三段/2605.00269边界、uncertainty supervised-ensemble完整段、TRACER actor×step/MAX/tail整段、CounterfactualLocalization完整两段及“FailureCatchability”Observe/Locate/Intervene两段。它们已要求内部activation/entropy仅sensor，按目标任务与deployment slice重校准，绑定actor/model、前后step与heldout人口；内部转折与最终危险结果分开，检测/可拦截与实际挽救另验。Ch72 BackdoorAgent跨step sensor完整段仅作相邻交接，安全/effect authority不归本篇predictor。

本论文把这些已承载的判断落实到rewardhack adapter、entropy/context logistic读出与非单调标签反例；没有足以改写上述长期论证的新因果或统一监测算法。它仍值得本日证据保留、5分标准审阅，不因已有覆盖从候选删除；不为“新增一种feature组合/再补低分不等安全”制造Book段。拟**具体已有覆盖/No Change**，不新I、不写Books，交root一次必要/正式5/actual NC独核。

## HarnessFix 2606.06324v1

[exact-v1](https://arxiv.org/html/2606.06324v1)实际读III-A–E/IV/V/VI及TII–VI、validation式与完整AppWorld例。拟2+2+2=6：trace+code的step evidence→flaw record→允许编辑/禁改域的repair specification→目标flaw与回归双验收，是跨observability/runtime/promotion的具体替代，非ETCLOVG命名加分。标准审阅读足必要mechanism与对照，未核artifact/图像素或复现。

HTIR保存recoverable step、request/response、role/status/effect；三links为temporal、input provenance与controlflow。前者来源span/代码位置解释当前request如何组装，后者解释为何retry/delegate/finalize，不能用时间邻接代因果。LLM从日志/代码推断这些注释，本身并非真实effect或已标定根因oracle。diagnosis先广回溯candidate，再用node-local证据裁决；跨trace按层/相同rootcause合并flaw，主repair operator限定可改文件/配置与required behavior、明确禁benchmark数据/evaluator/test labels/API。AppWorld例中API缺user_email、错误被吞、数据库delta零、complete_task被接受，是具体effect-evidence缺失，不是把ExecutionSuccessful当业务成功。

validation先查diff/syntax/static，再在heldout validation同时查目标flaw occurrence减少与原已解任务的新增失败上限。目标flaw是否同层/rootcause仍靠新trajectory归因，未见独立人工归因准确率或所有阈值统一披露；自己诊断变少不能单独证明真实缺陷消失。patch memory存accepted/rejected适用条件，不能由此授未来自动安全。

GPT5-mini同base，四任务split依次100/50/100、34/17/34、60/30/60、90/45/90，2:1:2 train/validation/test。TIII test counts45→57、6→9、26→37、33→38；15.2–50%是relative improvement非百分点。TIV full高于四ablations，TB2差仅1–3task，未统一披露repeat/CI、全部iteration/model-token预算/hardware/完整成本，不能从相同base认定等总compute或逐层diagnosis唯一因果。all-split分数混入适应数据，不替heldout。trace读取/HTIR与代码分析、诊断/生成全部patch、所有validation失败与回归、部署/维护都计费；不授跨任务平台或production readiness。

actual唯一`AGENT-PLATFORM` Ch84实际完整对读“Skill可更新性”三能力及pipeline/后续风险段L376–391，以及Self-evolution capability revision与PromotionGate完整段组L1156–1168：现有论证已把failed trajectory+responsible component→fault-localized patch→section-level validation/regression→fixed-backbone consumer→admit/reject/rollback串起，明确缺日志/sharedjudge会破坏归因；新目标增益与preservation replay是两份证据，scope不全或回归超阈值保旧snapshot、缩更新范围或回滚。Ch69开篇span/link语义仅作实现交接，不把该章trace所有权挪给Ch84。

HTIR的三类边与operator模板在这里是上述已存在修复/验收链的具体实现，不是本项目新增一条长期harness层级或新的安全充分条件；不为补“LLM归因可能错”另写通用警句。拟**具体已有覆盖/No Change**，保论文的typed实现与benchmark反侧于Report，不新I、不改Book；6分标准完成待root一次必要/actual NC独核。若root判断三edge的可追溯接口确有旧论证无法承载的具体gap，再只定点重开采用命题，不重读AB/date。

## R35既成采用（2026-10-25）

root R35已独核两项必要/反侧及actual Ch66/84完整承载：RiskStates正式5、HarnessFix正式6，具体已有覆盖均通过。不写Books、不新I；Report已同步正式处置，不再普通待独核，不需行政复审或重复原件。
