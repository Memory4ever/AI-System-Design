# 最小贡献核查关闭

- 2602.07543v1 MSP-LLM：首批精确完整AB见feb11_calibration_exact_AB.json。材料合成规划的material class、precursor与operation条件链属于ROADMAP暂缓的AI for Science领域recipe；没有独立foundation/system机制或可核主线新边界，范围/贡献关闭，不能经Data/Agent节点回引；日期未继续核，不评分。
- 2602.08990v1 InternAgent-1.5：同一首批完整AB，算法研究与湿实验不能只按科学名称一刀切；但AB所述generation/verification/evolution、deepresearch/memory组合与GAIA/HLE/发现任务成绩，没有实际新执行机制/对照有效性条件或受限失败路径，领域发现不改变主线具体设计，贡献关闭。不是因为新领域/smallmodel/理论/局部结果而拒，不评分、不读全23MB附件，日期不影响关闭未另审。
- 2602.06855v1 AIRS-Bench：完整官方AB见feb11_prior_identity.json。MLresearch任务仍在主线可能范围，但新增20任务、涵盖数据处理/训练/实验/agent排行榜本身未给出新的评价混杂/失效边界；没有独立改变模型系统设计判断的实际delta，贡献关闭而非按Science名称排除。日期不影响关闭不继续审计，无评分/Books。
- 2602.07374v1 TernaryLM：完整AB后定点§method/evaluation。标准QAT/STE threshold、layer alpha与RMSNorm均为成熟机制；132M/T4/TinyStories60M/15epochs，middle-layer zero割合60–62%不是受控层precision干预，embedding89.54对58.42的已知quant敏感与native bit任务成绩未建立新boundary。root认可贡献关闭；不评分/不进入Books，日期不影响处置未另审。
- 2602.07559v1 VerifyRL：完整AB后§3.1–3.3。固定symbolic AST含sin/cos/exp/log/tan/x^n，chain/product/sum derivative由SymPy/template生成、子表达式严格减小与depth1–5课程是常规symbolic differentiation结构性质。新任务成绩与可构造prerequisite本身不改变一般RL planning/verification选择；未显示超出固定AST规则的新增机制或非平凡反侧。root认可贡献关闭，不评分/不入Books；不为此读全部proof或遍历日期。

- 2602.07187v1 PreFlect：完整AB后定点§3/4.6/4.7。mixed success/failure轨迹→LLM及人工整理三类错误提示、critic修订计划、ReAct发现进展受阻触发replan，属于既有experience-guided critic/在线重规划链。Table4去PE/DRP仍同环境/20 execution steps，但没有等长通用checklist或去distillation critic的可比对照，额外调用/文本量未分离；74.44% risky由自身reflector标记非校验正确率，Wayback成功单例未新增执行可达/不可逆失效边界。定点补读没有把新任务成绩转成满足门槛的新控制/可靠性条件，因此贡献前关闭；不因Books覆盖、deep成本或负面局部而拒绝，不评分/不入Books，日期不影响关闭未继续审计。精确原文见feb11_AB1_minimal_final.json；root最终抽检此理由。

精确v1原段保存在本日conditional_core、AB2_core2和AB1_minimal_final；不是因审阅费时或Books既有覆盖缩池。
