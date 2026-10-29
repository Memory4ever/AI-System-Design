# PRE02：四个必要缺额

writer Popper；只请求以下四份完整正文/独立marker/本人注及指定两侧整体PRE。Source/评分与读取边界见REPAIR_EVIDENCE；真实写入前不计整合。已实际读目标直接两完整侧及相邻章交接。不存在已知同gap冲突，不请求root第三批准。

## I03 / 11031 / TRAIN-DATA Ch27 / 2+1+2=5

文件 `books/part-04-training-system/27-data.md`。插在完整“课程还可由可控生成器和当前通过门共同推进”段（SF-2026-ARXIV-2610-25612）之后、原`### Failure-driven Curriculum`及其原引导段之前。

拟正文全文：

可控生成器还可把逻辑深度与数值运算分成两条难度轴：先构造Facts、Rules、Query并在形式世界中求出答案与推导DAG，再以模板和语言润色形成训练/评价文本。[LogiNumSynth的受限分支](https://arxiv.org/html/2510.11031v1#S2)让相同逻辑结构配不同计算复杂度，而不以更长文本直接冒充更深推理；但形式规则的gold与自然语言转述是两个资产，润色仍需检查是否保义。当前合取/蕴含和有限运算不等一般现实语义，过程评分又借模型抽取结构，答案对而路径分低可能含表达/抽取误差，不能自动归为能力缺失。生成/求解、模板/润色、过程提取、训练与外部回归均付费，小模型SFT迁移不签所有规模或独立净收益。形式支持、转述保义或过程评价失配时，保留原符号题/独立求解器、人工核验及分开报告的终答与过程指标，不由可调难度和形式答案批准自然语言推理全正确。

<!-- source-family:SF-2025-ARXIV-2510-11031 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11031`：Popper，Daily2025-10-15补Oct14，exact-v1 §2/3/4必要域/AppB/F1，2+1+2=5；HTML部分传输但该域完整到达，仅采用形式gold/语言转述与逻辑/数值难度分责。保过程提取误差、有限运算/SFT规模与完整费用，不授一般语义正确/通用迁移；未核全F实现/代码/复现。PRE/SAVE/完整自读/solePOST仅本日canonical真实层。

## I04 / 11062 / TRAIN-GRPO Ch33 / 2+2+2=6

文件 `books/part-04-training-system/33-grpo.md`。完整“多智能体训练还可同时使用两种不同人口的基线”段（SF-2026-ARXIV-2605-04906）之后、完整“比较人口还可以落在同一个 episode 的同角色参与者上”段之前。

拟正文全文：

合作多角色轨迹还可把比较组固定在当前观察，而不把同一问题的整条独立rollout强行合组：每个环境、角色和turn从同一实际history采若干动作，在这份候选内归一advantage、保存全组，再执行最高reward候选以继续主轨迹。[AT-GRPO的受限分支](https://arxiv.org/html/2510.11062v1#S4)由此区分候选更新人口与实际访问的后继状态；仅有相同role/turn标签或hash键，并不证明来自相同prompt/behavior policy。团队与局部reward的相加也不产生独立反事实信用，贪心续接会改变未来观察分布。角色专化在部分任务有益，共享policy在另一些任务仍更好；single-agent与multi-agent的轮次和工具条件不同，不能将全部增益归为协作或同预算训练。所有分支评分/工具执行、未选候选、多模型驻留与训练回归都计费；观察身份、组信号或净质量失配时，保留普通同prompt采样、共享policy和可信outcome，不以更多角色或较高终局分批准无偏更新及执行安全。

<!-- source-family:SF-2025-ARXIV-2510-11062 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11062`：Popper，Daily2025-10-15补Oct14，Stronger Together exact-v1 §4/Alg1/Eq4/§5配置、角色共享反侧/Table3/Limitations，2+2+2=6。仅同观察分支分组/全组更新与greedy后继消费分责；保history/hash身份、不同SA/MA预算和完整费用，不采无偏归因/专化普胜或生产安全。未核代码/复现；整体PRE/真实SAVE/自读/solePOST只本日canonical后到层。

## I05 / 11210 / WORLDVIEW-REPRESENTATION Ch5 / 2+1+2=5

文件 `books/part-01-worldview/05-what-neural-networks-learn.md`。完整“关系表示的干预对象也未必是一条均值方向”段（SF-2026-ARXIV-2605-29634）之后、完整“当不同规则能解释同一输入序列时”段之前。

拟正文全文：

若性质能构造明确的输入对照，还可以固定前文、替换关系连接词及其适配的候选后文，再把clean状态补到corrupt运行中，以输出logit差定位相关计算边。[受限话语circuit研究](https://arxiv.org/html/2510.11210v1#S2)用一阶attribution近似筛边，并比较细关系、合并关系、随机与无关任务circuit；它恢复的是指定对照的logit行为，不是证明整个网络只用这些边理解自然话语。归一分数还依赖完整模型分母，预先任务微调、反事实生成与关系映射共同限制解释；circuit重叠大也不必有更好的域内功能迁移。合成/人工校验、微调、全部patch与跨任务回归均付费，有限英文和GPT2族不授通用压缩或唯一语言算法。对照不保义、分母不稳或迁移失效时，保留原网络、原始行为结果与更窄配对干预，不由少数边恢复高比例分数批准全能力保留和部署剪枝。

<!-- source-family:SF-2025-ARXIV-2510-11210 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11210`：Popper，Daily2025-10-15补Oct14，exact-v1 §2–3/归一metric/随机IOI比较/跨框架及Limitations，2+1+2=5。只关系反事实/局部edge恢复与overlap非迁移能力分责；保微调/映射/抽样与全费，不采唯一circuit/通用语言能力/压缩净速。HTML末附件partial，必要域到达，未核全附件/图像素/代码/复现。PRE/SAVE/自读/solePOST据本日canonical实际层。

## I06 / 11370 / TRAIN-GRPO Ch33 / 2+2+2=6

文件 `books/part-04-training-system/33-grpo.md`。现有`semantic-body-binding:SF-2026-ARXIV-2606-00395:end`独立marker之后、完整“一种收敛优先的方案，是让 rollout graph 成为 training forward graph”原段之前；不改现有route identity两段。

拟正文全文：

固定执行路径还要分清保存什么：一条重放分支只记录rollout的Top-k expert mask，learner在这份mask内重新对当前training logits作softmax，再组合专家输出；离散选择固定，router的连续权重仍可有梯度。[R3的受限方法](https://arxiv.org/html/2510.11370v1#S4)因此减少选路差异，却不使两端gating权重、activation或token概率恒等，也不自动消除陈旧性。多turn复用还须把prefix的mask与KV共同绑定到相同模型、路由约束和实际token历史；这是由消费边界提出的工程要求，不是文本相同即可跨更新复用的证书。与额外importance校正叠加可能退步，各任务取不同best step也非一份同预算最终artifact。路由记录/传输、缓存驻留、复算与未用rollout及完整质量回归均计费；mask缺失、专家/版本不兼容或净质量失配时，重采、退回一致后端或原已验route分支，不让路径一致替分布等价和长期稳定性签字。

<!-- source-family:SF-2025-ARXIV-2510-11370 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11370`：Popper，Daily2025-10-15补Oct14，exact-v1 §3–5/Eq4–9/完整Table1与必要配置，2+2+2=6。仅mask固定/learner连续权重重算及prefix双缓存身份差额；保残余mismatch、TIS叠加反退/最佳step与完整费用，不授数值相等/无偏/生产稳定，未核代码/复现。整体PRE/SAVE/完整自读/solePOST只本日canonical后到真实层。
