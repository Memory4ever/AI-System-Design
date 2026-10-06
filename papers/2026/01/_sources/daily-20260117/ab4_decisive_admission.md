# AB4 具名含糊项决定性准入校准

完整AB已读，恢复只检查决定准入的方法位置，不称标准证据完成；精确v1，缓存为必要主文提取、未遍历附件。拟判断待root校准，不因Books已有主题、小模型、负面或费时关闭。

| 身份 | 实际决定性增量与选择 | 拟准入 |
| --- | --- | --- |
| [10332 Think-Then-Generate](https://arxiv.org/html/2601.10332v1) | §3.1–3.3：同LLM既rewrite又encode会耦合text生成与DiT条件；J种rewrite各K图，LLM按该rewrite图像semantic均奖，DiT按semantic/aesthetic/physical proxy奖励。改变只按重写文本监督/仅训练DM的选择；不是t-SNE重叠认证接口不变。 | 2+2+2=6，标准必要；specific共同训练与条件漂移反侧待核，不自动Books |
| [10349 SuS](https://arxiv.org/html/2601.10349v1) | §3.2–3.5：trajectory内similar downstream action distributions的contrastive策略表示，worldmodel预测误差乘1-cos(pre,post)，另加cos稳定项。改变仅奖励state novelty/困惑度的选择；明确可预测新策略仍低分，不授天然noisy-TV免疫或无objective distortion。 | 2+1+2=5，标准必要；meta weights与signal具体实现/对照待核 |
| [10355 GEM](https://arxiv.org/html/2601.10355v1) | §3.2 Stage2–4/Validation：从web文本设计schema与workflow，再teacher一次生成整trajectory；tool output是simulated，验证仅schema/类型、参数在dialogue出现及LLM judge。未建立新的真实环境执行/工具返回grounding或可迁移验证条件；source corpus+既有synthesis组合不能因称grounded升级执行证据。 | pre-denominator关闭，保留题摘/定点证据；不是benchmark不高或Agent领域拒绝 |
| [10373 DiffCR](https://arxiv.org/html/2601.10373v1) | Method/FaSE Eq8–13：compressed latent与epsilon prior映到同z0预测target，频率分离attention配time mask，避免直接把denoise fidelity目标用于compressor。改变codec latent reconstruction vsperceptual prior目标/少step重建分支选择；不是仅图像压缩应用。 | 2+1+2=5，标准必要；真实rate-distortion/两phase预算与directcrossattn反侧待核 |
| [10398 LatentRefusal](https://arxiv.org/html/2601.10398v1) | §3.1–3.3：冻结LLM单forward intermediate hidden probe，由calibrated threshold在SQL tokens生成前拒绝，避免输出文本refusal与多SQL执行后uncertainty的代价。新signal/readout位置改变generation-before-execution选择；单新增SwiGLU不单独计增量，answerability非数据库安全权限真值。 | 2+1+2=5，必要安全深入仅影响gate/漏拒条件 |
| [10402 ML-Master2](https://arxiv.org/html/2601.10402v1) | §3.3–3.4：当前parallel phase原日志+全部plan保留，phase边界LLM summary写L2后移除对应raw；task结束再distill L3并similarity prefetch。具体phase-dependent retention与promotion改变近期truncate/把历史全带入的选择，summary仍derived非已认证wisdom。 | 2+1+2=5，标准必要；不是cache比喻即准入，也不因ML任务自动AIforScience拒绝 |
| [10524 Phishing diagnostic](https://arxiv.org/html/2601.10524v1) | §4.1–4.5：领域FT/数据多样性比较、model自己>91%confident flag labels、SHAP与attention minimal-pair。没有独立label audit控制支持18%真实错误率，没有intervention支持heads/architecture因果；少数明显spam示例及域错误指标未形成基础表示/执行选择新边界。 | pre-denominator关闭；保留security/设计反证信号供root必要反侧核，不采用head因果，不因负面/模型大小排除 |
| [10527 Safety report](https://arxiv.org/html/2601.10527v1) | 实际§1.2–1.3/§2.1必要协议：多个成熟suite/attack/regulatory组合，Qwen过滤easy再sample100与Qwen3Guard judge；报告给不同风险/语言下模型排序差异，但不同populations并非paired威胁退化因果。是否有可保留的新盲区/控制目前不明确，不能从radar推出internal alignment archetype。 | 当前仅方法决定性仍含糊，须一处实际attack paired/overrefusal控制后准入或具体关闭；不抓全附件、不先评分 |

10527主文首次提取输出27673tokens截断，未写缓存/未称全文读完。现已实际§2.2必要方法/直接结果：同100harmful queries各30黑盒攻击；attack original judge下worst-all/worst3与Qwen3Guard response-safe/refusal分开，Table3 GPT5.2 refusal80.76%、safe54.26%、worst6%，其余worst0–4%。新的具体现代模型验证说明高refusal/response均分不授同query跨attack安全，改变只看单response平均的选择；不把跨dataset benchmark→attack差值归因alignment，也不采内部archetype、family机制或未经控制的“自然语言梯度”。拟2+1+2=5，安全必要深入仅这套判定/直接反侧，Books可能Existing/Only待标准边界。缓存为§2.2决定性片段而非全报告/附件。
# 独立准入纠正

root实际§3.2 Stage2–4/Validation指出10355的新增是训练数据来源/预定义工具库依赖的替代分支，不是execution grounding。故作者原拟preclose过度以simulation抵销来源增量，现改为5标准准入；保留模拟输出/类型及LLM验证边界，必要对照只核vs预定义工具的泛化/预算与synthesizer代价，不采真实反馈宣称。10524经root实际token softmax同model audit与SHAP/minimal-pair原段核，具体preclose成立。10332(6)/10349(5)/10373(5)/10398(5必要安全)/10402(5)准入均通过；非Evidence/Books终裁。原拟表保留改判轨迹如下。
