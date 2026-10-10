# 第二包五项决定准入 core：实际停读与判断

作者mar14_supplement，待root实际独核；不是必要Source/评分/Books完成。只围绕决定准入的增量补读精确v1，不因全部HTML已取得展开全附件。AB均已由root独核。

## 11228 Markovian Generation Chains — 狭窄潜力

实际§3–4/B35–100固定model/prompt/decoding kernel定义与标准Markov界，§5/B101–151（补齐106–122）有限实证/ablation、§6。原先可能把反复模型改写或training-time model collapse混作同一种退化→无参数更新的固定kernel在greedy下exact fixedpoint/shortcycle、sampling较长transient，450seeds/50steps和prompt/粒度改变对照→多步reuse应区分kernel/decoding state、exact surface recurrence与语义保持，而不是把更多不同字符串当信息增长。准入只保留受控迭代评估人口/失败边界，标准有限Markov结论不作为新理论贡献；没有量测真semantic fidelity、一般memory agents或所有temperature都改善。停主文，不读Appendix全证明/全部曲线。

## 11382 UCIP — 贡献前关闭（root 实际独核后收紧）

实际§3/B44–100、§4/B101–119、§5.3–5.10/B141–226和§6.1–6.3。新signal是**自训练QBM** latent density entropy与gate，不是目标LLM hidden state；known-objective gridworld trajectory7D/8latent/classicalmatrix formalism。有限classifier如何从行为推出continuation目标的原有判断→positivegate并不够，mimicry FPR .4–.75/entropy .4、同schema corridor迁移失败、meanfield signal collapse；DistilGPT2冻结meanpool只有探索null、与QBM不matched→目标标签/表示/阈值/对抗与迁移须分开，不能由latentclassifier自行授内在目标或部署安全。这是评价proxy有效性/表示的负侧线索，**不是仅因为quantum术语或Agent标题入选**；同类meanlatent baselines更改统计量/样本亦不能授QBM必要性。其与当前主线的关系需root裁决：没有实际LLM目标检测/控制接口，若不足改变具体评价选择，应贡献前关闭，不借安全标题纳入。已读决定性反侧后停，不扩大数学/全部plots。

## 11495 Tool-DC — 明确机制潜力

实际§3.1–3.3/B23–86。原topK retrieval会漏真正tool且长definition同时干扰→保留topK完整S0、每anchor另配disjoint tail子集并parallellocal inference、schema-valid候选归并再全局retry；TB枚举singleton再GT匹配/模板rationale→新增是retrieved anchors与遗漏tail召回机会并存的接口，以及schema只验格式不证明选择的边界，非简单try/check/retry重命名。必要Source还须验证分组消融/延迟与失败/GT制备费用，不借instruction/benchmark数字确认收益；停method，不深读未决定准入评价。

## 11351 Novelty Adaptation — 明确机制潜力

实际III–V必要B30–39/B67–91/B93–108。已充分operator domain不能处理新增entity→在每BFS状态LLM加missing operator、symbolic lookahead验可plan并以ordered effects作渐次解锁subgoal；LLM并行reward candidates+周期淘汰而非固定单reward→planner域扩充与可执行skill学习的连接/失败界值得核。predicates已足够、物体可识别/真值可观测的假设不等开放世界；symbolic可plan不等真实skill。原被当组合的理由不足，现具体state/interface潜力明确；必要Source应核reward curriculum/淘汰对照与reset/搜索失败，不默认真机安全。只读所需algorithm，不全proof/robot附件。

## 11356 iSWE — 明确机制潜力

实际§3.1定位B89–92、§3.2编辑B125–129和§3 flowB55–58。自由bash编辑靠全程container隔离→只读静态图提取和structured sanitized location handoff，candidate search-replace先在memory copy格式/match→linter→最后才container compiler→改变effect boundary/失败反馈和sandbox开销，而非仅Java移植。编译通过不等issue语义，heuristicrepair/默认可关compiler不授安全；明确twoReAct组合本身不是贡献，typed scope和分段effect承诺才是待核选择。必要Source须核config/组件消融与patch correctness/完整费用；停决定性接口，不读全部代码example。

root 已实际读上述必要原件后确认：synthetic trajectory / QBM 自训练 latent classifier 不检测目标 LLM state/目标，DistilGPT2 为 unmatched exploratory null；mimicry、corridor、meanfield 反侧修正的是该诊断器，未改变当前大模型评价机制或具体设计选择。不能把成熟 proxy validity 经类比包装贡献，故11382贡献前关闭，无评分/Books；不是因为玩具规模、量子术语或审阅费时。保留以上实际反侧，不扩大附件。

以上经 root 实际原件校准为4明确P+1具体EX，具体最小命题再date/Source，不授全篇审阅或DAY。11394另一个决定core尚在下一manifest，未混入本五。
