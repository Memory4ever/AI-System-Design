# DDSR / MetaKube 决定准入定点

作者supp_mar26_fresh，只处理先前完整题摘决定接口未明的两项，不扩来源查询或附件。精确v1官方HTML实际§3全部方法；MetaKube额外只§4.1 memory/fast-sufficient与§4.3 graph构建，决定后停止，不当必要Source深审。

## DDSR22908v1

https://arxiv.org/html/2603.22908v1 §III-A/B1–4/C/Eq1–16。不是泛泛两teacher组合：source只API预测、target同labelspace，按全target平均entropy和样本量阈值调整双teacher融合，smalltarget分支甚至给较不确定source更高份额；另对同student前γ权重子网作outputJS对齐同时增大gradientdiscrepancy，用subnetentropy调强度，再student反向更新teacherprompt/EMA labels。它提出具体配对和更新目标分责，需要重新考虑“只选低entropyteacher/输出一致即可rectification”的选择，贡献已清楚后进入证据而非初筛全附件。

拟准入2+1+2=5、sole TRAIN-SFT Ch29（监督目标/teacher-student优化分支）；owner请独校，不由分类领域或小模型排除。Entropy/nt规则的因果、gradient向量维度/停止梯度、teacher自确认、预算与反侧仍需必要Source；只是准入无可靠伪标签/梯度配方/免费保证。日期v1下界/上界25此前已独校，v2submitted25T03:47不是该版本当天公开证据，不混v2或v3标题。

## MetaKube23580v1

https://arxiv.org/html/2603.23580v1 §3.1–3.3/Eq1–11与§4.1/Eq12–18、§4.3/Eq20–21。实际是Kubernetes症状RAG+graph辅助诊断组合：similarity/recency/success/context加权confidence选择fast/deep，episodic/pattern聚类、两层TopK与memory-overlap作为graph优先级；BCE标签fast_sufficient是已有gate calibration目标，GraphRAG/GPT清洗构图本身不新增执行或证据权限机制。它把成熟检索/路由/图建组合具体化并换K8s任务，未见与之相区分的新执行机制、旧方案失效条件或归因证据；“memory使causal探索更快”亦未提出新的验证判据。

故拟EX，不因标题domain/组合标签一律排除，而因定点原接口仍止于成熟组件改写；声称fast方案包含于deep、confidence单调/日志复杂度和图内“verified causal”不是条件完整的新可靠性证据，也不将流程命名或数学记号当贡献。现v1真实公开25/26未定，但贡献已可关闭且当前exact事件页未见纠错/撤回说明；按合同不为不影响处置的日期新建请求、不评分/Books。上述含自称可靠性/设计反侧，交非作者必要负侧实际复核，不能以日期不清逃避准入。

两项拟判断待独校；无Book写/Source完成/DAY声称。
