# Apr20 两项有限非作者处置核

复核者apr02，非Apr20作者；本轮实际重读AGENTS/当前研究与Report合同、统一Prompt，复核采用范围而非整日Gate。只读两项必要官方v1与15559对应当前Ch72实际正文/相邻论证，不遍历全附件或重扫日期。

## 2604.15559v1：6分安全深入，窄已有覆盖通过

实际打开[官方v1](https://arxiv.org/html/2604.15559v1) §3.1–3.5、4.1–4.3、Limitations及AppendixA必要超参数。teacher先学删除偏好，student仅用safe-tools轨迹且过滤删除词，仍在20个模糊任务/3seed下改变first substantive action。这是trajectory supervision到行为选择的受限反证，不是实际filesystem effect或全部Agent删除事故率；chmod-first偏好与删除也不是统一harm分母。

Table2 random control的student25/base5，明确不满足§3.4的control≈baseline成功判据；无实际CI/p报告，作者也没有识别隐式特征的机制。因此不能写“随机控制无变化/结构编码已经唯一归因/任意模型迁移”，但不因这条限制否定所有有限行为观察。teacher150样本2epochs、safe400过滤约15%、student4epochs、LoRA/bf16条件有界，不外推线上模型/权限。

实际Ch72“公开的任务无关输出也可能携带后训练行为影子”及两侧保密论证已经明确：无目标文字不是无信息training artifact，词审计之外需要主动查询/同源蒸馏/下游行为transfer测试，且同源、家族、初始化限制保留。**已有覆盖只指该一般保护责任命题**，不称Agent删除/permission协议、具体算法或数值全在书里。原文新增受限证据保留日报；2+2+2=6，必要安全深入采用边界PASS，无新正文。

## 2604.15577v1：5分标准，仅报告通过

实际打开[官方v1](https://arxiv.org/html/2604.15577v1) §3 Eq1–3、§4近似实现、§5必要预算/采样协议及§6限制。精确Q的Bayes展开是有条件的恒等式；Q^γ/logQ需要可定义正值，Jensen必须是非负归一权重。实践有限YS、z-score带负权、训练prior替prefix posterior、.95 nucleus截断，不能无桥地继承精确Q或Jensen的policy improvement保证；这与一般未写证明不是同一问题，原文自己的实现已改变对象。

保留可迁移的AR conditional likelihood-ratio guidance机制及成本/支持集限制，不恢复化学任务为项目贡献。§5的每token条件forward次数、RL16组网格/1000步再2000best与guidanceγ选择预算不同，8H100训练不等线上请求成本；已知目标y*时直接conditioning更好、越界属性与反复蒸馏退步保留。2+1+2=5，标准Only的必要范围与作者边界一致；不说整个算法已Existing，不写Books。

两项只完成具名source/采用边界核验，未核首公开窗口、未复现实验，不替代Apr20来源、候选全体与日级Gate。无本组普通未核事项，作者可同步两项处置。
