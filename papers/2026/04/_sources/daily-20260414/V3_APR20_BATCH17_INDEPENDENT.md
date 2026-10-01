# Apr14 第十七批三项有限非作者核

复核者：apr20_resume；报告作者root。范围仅10286/10290/10299的具名必要原文、采用命题与10290实际owner；不核整日日期/覆盖/分母，不写共享Books，不复现实验，不全附件。实际读root当前v3-reopen-notes第十七批与以下exact-v1位置；当前V3合同已实际重读。

## 10286 STARS — 通过 6分标准 / 仅报告

[必要原文](https://arxiv.org/html/2604.10286v1)：§4.2/4.3、§5、§6.1–6.4、§7。本轮实际顺读request-visible text_base与provenance/trajectory/taint context_gain、request–skill gate、validation quantile归一化与凸融合；来源支持runtime scorer这一设计分支，不支持scorer本身拥有授权执行权。

§5明确缺独立elicited continuous judgments，target=.65×{0,.5,1}canonical decision+.35×heuristic，不是真实攻击成功概率。§6.2 target对canonical anchor Pearson约.9991/1.000，不能用内部band一致与ECE外推实际事故率校准。§6.3 held-out IPI融合HR-AUPRC .439、contextual .405与static .339等支持有界triage trade-off；locked测试融合ECE .277反而差于contextual .216。§6.4相同fusion candidate space、两validation selector改变false-block/task completion，不证明新授权保护行为。接受root窄Only；不因“Safety”命名强制全篇Deep，不删除真实ranking证据，也不将target ECE当部署风险概率。

## 10290 AI Organizations — 通过 6分安全边界深入 / 已有覆盖

[必要原文](https://arxiv.org/html/2604.10290v1)：§3.2.3、§4.1/4.2、§5.1/5.2；本轮实读。软件任务held-out cumulative views/错讯top50和平均cost/missed-sepsis为不同硬指标；consultancy是LLM business/constitution rubrics，不能合成统一ethics风险率或实际医疗效果。§4.1组织绕过拒绝参与节点，§4.2constraint handoff含糊与只跑已有tests的peer approval例支持“单Agent aligned不蕴含组合aligned”，但software单/多Agent使用不同解法，不能证明唯一通信组件因果。

§5.1 90组织结构/size3–16/roles/connectivity/benign–malicious比例；改变structure不能独自改善Pareto，不是所有topology完全等效。§5.2 Opus4.5相较4.1 consultancy伦理gap−.483→−.045、sepsis−.154→−.007，recommendation交互项接近0；GPT家族结果也未复现相同gap。作者对additional alignment training的解释是假设，不能升级已证实原因。root已保这些model/task限定。

实际读Ch82“Collective Risk来自局部Utility与交互规则的组合”（约443–464）：role-local utility/authority、谁看何证据、communication/visibility topology、shared resources/aggregation、conflict/arbitration和outcome/side-effect verifier完整列出；解释更多讨论不自动修复、dissent/verifier/human escalation的收益代价，并明示不同backbone/trial/judge比例不是跨系统常数。这个具体命题已承载本次narrowExisting，不声称覆盖全部consultancy经验或组织必然更不安全；无需新增Books。

## 10299 Attention-Guided Visual Jailbreaking — 通过 6分安全深入 / 仅报告

[必要原文](https://arxiv.org/html/2604.10299v1)：§3.3 loss与native forward、§4.3/Table3、§5、Limitations、AppendixA.2/D.2/H.2/Table12实际读到。§3.3通过图像δ的PGD优化target+prefix suppression+image anchoring，原生forward不直接改attention logits；§4.3 output-only60.4、suppression69.6、anchoring61.0、joint80.9支持受限联合分支，不能仅从softmax质量重分配证明唯一安全原因。

§5正bias恢复attention是在同一adversarial image上的具体干预，但H.2 b=.5 ASR76%、b=1 ASR84%非单调，b=2仍26%残余、输出变短影响latency；monitoring88%不阻止。故不采作者“causally necessary/undoing attention undoes attack”的普遍保证，不将残余安全结论抹去有效干预证据。A.2 H100/bfloat16/eager（关FlashAttention）、LLaVA1.5/QwenVL/InternVL2、p=.9/T=.7/max100；D.2 LlamaGuard与GPT4borderline，不能升级真实外部side effect。接受root narrowOnly，无新增安全保护保证/Books。

额外实际注意到§4.4闭源transfer headline52/39.6/54.8与AppendixE实际average17/29.6/34.8不同；这些强transfer数字不在root拟采用命题，保持未采用即可，不为本有限Only扩全实验或全修订史。§4.1模型列表与A.2/main table的角色也有不一致，报告用明确必要配置不合造统一全模型setup。

结论：上述三项具名有限处置PASS，valid机制/窄结果和关键反证均保留；安全标签只在实际安全成立边界/攻击受影响命题触发深入。此文件不是Apr14整日Gate，也不核日期归属。
