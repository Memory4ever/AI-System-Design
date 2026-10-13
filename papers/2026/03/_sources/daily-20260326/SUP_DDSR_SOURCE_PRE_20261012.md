# DDSR necessary Source / Ch29 PRE

作者supp_mar26_fresh；2603.22908v1/day25/2+1+2=5已独校，仅精确v1，不借后v2submitted日期。未获写锁。

实际[exact-v1](https://arxiv.org/html/2603.22908v1) III-A/B/C Eq1–16、IV-A–E/T1–V/F3–8caption及V268限制读完。只采用同labelspace黑箱source概率+开放CLIP概率的全target人口entropy/nt分支teacher配权、output一致性与gradient监督分责，不采完整gradient recipe。Eq3大nt时CLIP权1−α/2，小nt时α=Hc/(Hb+Hc)；低entropyCLIP仍可被小人口分支减权，α是全target平均而非逐样本置信。teacher同时低entropy导致分母0无fallback披露；nt阈值不提供正确率校准或classshift支持。teacher outputs在epoch起与student/CLIP prompts/EMA .9同步更新，闭环共偏需独立真实任务核验，不能自签reliable labels。

Eq8输出JS有定义，但Eq9 gfull=∂JS/∂Wfull、gsub=∂JS/∂Wsub，原138按每层firstγweights取子网，未说明不同维向量cosine共同坐标/zero-gradient保护、sharedparameter身份与second-order/create_graph或detach责任；选择γ=.84使dimension问题真实需要实现映射，不能默认同维。只保“输出对齐不等同梯度对齐”的设计分责，隔离完整subnet梯度实现/互补知识保证；source-independent Eq3配权可局部采用，不整体HOLD/EX降分。prototype阶段Eq14使用nc记号但psoft分母/全数据迭代身份及正文q=g而III-A gclassifier/hfeature命名反侧保留，不照录完整伪标签修复recipe。

ResNet50Office31/Home、101VisDA，CLIPViTB32，SGD/momentum.9/weightdecay1e-3，新增层lr1e-2或VisDA1e-3/B64/stage25+10或15+10epoch/3seed/singleNvidiaRTX具体型号及precision未披露，servinglength/concurrency/SLO不适用/未披露。所有baseline取原论文、UDA/SFDA可访问内容不同，不能将crossbudget排行当唯一配权因果；Office31 W→D/BBC部分任务更高，VisDAavg与BBC同90.6且多class反退。TIV nt1000大部分平台区间相同，不证明1000普遍唯一最优；F8 small/large domains同时改变内容/类别不能单凭nt区分因果。F6对average有局部收益，TV loss组件有限两任务留一，不独立验证gradient式或每组件可重现。全target两teacher调用、prompt/EMA、子网额外forward/backward/可能二阶、prototype和第二阶段训练均计费，未报总费净收益。未核实现/复现或后版比较。

## actual owner / gap / 锚

sole TRAIN-SFT Ch29。actual完整824–905蒸馏strategy尾→privacy→safety→commonoutputhead/traitconstraints与Ch28/30开篇已读。已有蒸馏要求teacher/source/logit身份，不承载跨teacher的全targetentropy/nt替代配权及output/gradient目标资格分责。拟在privacy标题之前、前“污染审计和compute accounting”完整段之后两段；不移动旧段，非新增收纳节。待reader实际Source/具体差额/PRE与root锁。

## PRE paragraph 1

只有黑箱 teacher 的类别概率时，蒸馏还须决定多个 teacher 的监督怎样组合，而不能把最自信的一份分布直接当真值。一条受限同标签空间分支让 source teacher 与视觉语言 teacher 先在完整目标人口上分别求平均预测熵，再按目标样本量选择不同混合规则；少样本分支可以降低较低熵 teacher 的份额，较大人口则使用另一配权。这里人口级权重不同于逐样本置信选择，也不是正确率校准；类别接口、目标人口与两份 teacher artifact 一起定义监督身份，平均配权及单teacher蒸馏继续作为对照。<!-- source-family:SF-2026-ARXIV-2603-22908 -->

## PRE paragraph 2

[必要方法与反侧](https://arxiv.org/html/2603.22908v1#S3)还把完整模型与子网的输出 JS 对齐，同其梯度 cosine 的差异目标分开；输出可比不使不同参数集合的梯度自动同维，原文共同坐标、共享参数与高阶反传责任未披露，不照录完整子网 recipe。有限域适配的样本量阈值和融合消融支持局部选择，却未把人口大小同类别/内容变化完全隔离；模型与任务仍有反退，引用别论文的排行也不是总预算匹配。全人口两teacher调用、prompt与伪标签刷新、额外子网求值/梯度及第二阶段训练均付费。零熵分母、监督共偏、类别迁移或净收益无法核验时，保留固定混合、经验证单teacher与真实标注任务检查，不让学生自更新伪标签签发可靠性。

## 自身静态证据注 PRE

SF-2026-ARXIV-2603-22908 — [DDSR exact-v1](https://arxiv.org/html/2603.22908v1)，必要III/IV/T1–V/F3–8及V限制；仅全target entropy/nt双teacher配权及output/gradient资格分责，隔离不同维梯度共同坐标/二阶实现、prototype记号与零熵fallback recipe，保teacher/人口混杂、task反退和全费用；未核实现/复现。
