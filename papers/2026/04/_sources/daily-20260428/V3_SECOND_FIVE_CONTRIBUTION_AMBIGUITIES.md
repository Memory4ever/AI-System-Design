# 04/28 第二组五项贡献歧义有界消歧（作者侧）

沿用此前完整题摘记录，再以官方 `abs/...v1` 定点核机制和版本；必要时只读决定准入的 exact-v1 §4 片段。以下仍是**作者侧贡献准入提案**，非日期确认、评分、Books 或独立 Gate。实验可信度/外推留给真正候选的标准或深入审阅，不把“摘要没给等预算对照”误作没有贡献。

| Source Family | 作者侧贡献判断 | 准入因果链与不可采用之处 |
| --- | --- | --- |
| [2604.23853v1](https://arxiv.org/abs/2604.23853v1) | 准入待独立校准；Ch66/84 owner 待定 | Skill distillation 若只按成功率归纳，会保留成功但高成本的步骤，也可能删掉关键步骤；v1 的逐步 cost TraceCard 支持 preserve/prune/repair 三类不同 patch，且跨任务只 prune 可迁、preserve 反而退步。这是规则类型迁移的评价反证，值得核对 30+30 任务、两 seed、cost attribution 和原始执行轨迹；不能把 YAML 摘要当完整因果解释或 production cost 证明。v1 后有 v2，不能沿用后稿实验。 |
| [2604.24005v1](https://arxiv.org/abs/2604.24005v1) | 准入待独立校准；Ch33 | 单轮 on-policy distillation 默认 teacher 可在 student 到达的状态上提供有效监督；v1 提出多轮轨迹越深，错误复合把 student 带离 teacher 的有效 support，KL 增加且成功率下降，按可监督深度从短到长开放轨迹。这改变的是 rollout/teacher support 的训练准入，而不只是新 curriculum 名称。须核四组师生、ALFWorld/WebShop/ScienceWorld 的匹配交互/compute、teacher 在学生状态可用性和各任务反向；18 点上限非通用收益。 |
| [2604.23626v1](https://arxiv.org/abs/2604.23626v1) | 准入待独立校准；Ch81 | 单轮选模型难承载多轮 Agent 的 role/backbone 与历史工作流复用；v1 将 Query/Agent/Response 历史图状态用于每步同时选 role 与 backbone，并有归纳/转导及去历史对照，故需检验它是否改变 workflow routing 的具体 state identity。`GPU cost 186.26→1.04 GiB` 摘要说法与正文按 token×价格的 Cost 定义不一致，不采硬件容量/成本数字；14 任务及受测模型集合不能保证部署场景。 |
| [2604.23584v1](https://arxiv.org/abs/2604.23584v1) | 准入待独立校准；Ch23/76/72 owner 待定 | MRAG 检索的真实人脸同时是身份隐私与下游回答的视觉证据；v1 分离 identity/attribute code、替换 synthetic identity，再生成仍保属性的证据，使“删除整张图/直接模糊”之外出现隐私×groundedness 的受限方案选择。多 face-recognition oracle 与 impostor threshold 只是指定模型下的近似身份差异，不是一般不可识别性；生成图仍须独立验证证据未被修改。 |
| [2604.23238v1](https://arxiv.org/abs/2604.23238v1) | 准入待独立校准；Ch72/66 owner 待定 | 模型发布 reasoning trace 既供正常理解也可被第三方蒸馏；v1 以 teacher 性能与 student 可学性为双目标，把高影响 sentence 作事后黑盒扰动，不要求改 teacher 权重/代理 student 梯度。这可能改变 trace 发布时的效用—能力转移验收，而非一般拒答 guard。Stackelberg 表述本身不是对任意 student/黑盒查询的保证；需在 exact-v1 核 teacher task quality、真实 student 训练成功率、可检测/语义偏移与攻击方适应，且 v2 后发数据不得回填 v1。 |

本组五项仅把五个原“继续核贡献”从作者侧事实歧义移到待独立准入/必要审阅，不改旧 111 的 70 开放/41 拟前关、来源表或冻结分母。与[第一组](./V3_FIVE_CONTRIBUTION_AMBIGUITIES.md)合计十个**不重复**身份；`.24708` 已在[末批 D](./V3_LATE_BATCH_FINITE_TRIAGE_D.md)有独立作者侧消歧，本文件不重算它。若非作者发现真实增量只有已有组合或超出项目主线，仍可具体前关；撤回必须保存原始题摘和反证。
