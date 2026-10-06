# Nov07 后续局部准入校准请求

状态：待 root 非作者准入校准；没有日期或候选分母认证。仅25项窄主题选择性完整题摘中的受影响材料，非宽月表全量审阅。首次公开最小证明缺口仍在，不继续盲追失败日期路径。

## 两个清晰方向

- [Evaluating Control Protocols for Untrusted AI Agents 2511.02997v1](https://arxiv.org/abs/2511.02997v1)：exact-v1完整题摘已实际核对，安全/设计反证需要保留。原有固定攻击下resampling较强 -> 暴露monitor/resampling内部affordance给adaptive attacker后局部安全结果反转 -> 应改变控制协议评价时的attacker information contract，不是借用“最小权限”原则。候选仍须读真实attack预算、usefulness/安全定义、critical-action deferral控制；没有以摘要缺实验细节排除。拟在Agent安全/评价机制owner核，不从Anthropic作者身份赋予权威保证。
- [Whisper Leak 2511.03675v1](https://arxiv.org/abs/2511.03675v1)：Atom当前即v1完整题摘已读，streaming加密流量的包大小/时序泄露topic，padding/batching/injection均未完全消除是局部安全反证，值得继续必要证据。Microsoft原研究记录仅November2025，后续官方Blog原日期11/07；不得回填以后缓解策略或用后续Blog决定v1首次公开。拟主owner为平台安全/执行流量边界而非通用网络应用。

## 含糊点已做最小原文补读，需校准而非强行关闭

原始关键方法见 [最小核心](nov07-admission-ambiguous-core.txt)、[决定点](nov07-admission-key-points.txt)、[受限条件](nov07-ambiguous-decision-evidence.txt)。没有为了医疗任务指标扩读医学资料。

- [SRFT-GaLore 2511.03163v1](https://arxiv.org/html/2511.03163v1) §3.2/4.2/Table3：medical segmentation应用本身按暂缓范围，但替代SVD的结构化随机梯度投影是独立基础优化方向，不能整体范围排除。实际rank128、50步refresh、A6000、batch4、32-bit GaLore-AdamW，Table3显示GaLore与SRFT的受限epoch时间对照；不把领域质量改善采用为通用模型结论。中央公式从左侧sketch `Y=Pi G` 的QR取Q，再写 `P^T G`，没有足够显式的Pi/Y/Q/P尺寸以确认一致，不能直接采用正确实现或高概率top singular方向保证。请root校准“局部optimizer替代方案可以准入、中央公式争议隔离”是否合理；不以争议删掉已读机制，也不先给Books整合。
- [SCALE-VLP 2511.02996v1](https://arxiv.org/html/2511.02996v1) §3.2 Eq1-5：不仅标题医学，原文确实改了pairwise contrastive objective/weight，可能对应基础跨模态监督。需要校准独立一般机制是否达到项目门槛，而不是仅medical spatial/ontology应用。原文off-diagonal target仍是0、weight越大negative BCE罚越大，作者“partial positive/continuous alignment”的语义不能由该式直接推出；Eq2还含batch row-normalization，不采用“完全不需collective”的保证。root可裁决范围外应用，或保留一般损失命题争议审阅；不能凭应用名或成熟contrastive原则关闭。
- [Curved Spacetime 2511.03060v1](https://arxiv.org/html/2511.03060v1) §4.2-4.3：相对论类比不构成证据，但原文有固定step length随机方向null、100个词轨迹及50组with/without/base sentence edits。可核的是层间representation reorientation的局部观测与probe，不是Einstein方程、内禀曲率、attention唯一因果归因或新架构保证。若root认定该probe增量可改变表示解释，可进入受限标准审阅；不新建“spacetime”知识链。
- [ScalingEval 2511.03051v1](https://arxiv.org/html/2511.03051v1) §2.2/AppendixA-B：原文以top25模型60%投票构造ground truth，再评价模型agreement/precision；类别差异是与自身consensus的分歧，没有独立truth anchor或共享bias校验。这不是对真实correctness的验证。请root裁决是否只属推荐应用中的模型比较/已有步骤组合，应关闭贡献；或类别依赖的局部judge反证仍可准入。作者不把自己的“consensus不等于truth”成熟提醒冒充论文新贡献，也不单凭质量问题删候选。

## 事件身份有限恢复

- Diffusion Super Data Learners 2511.03276v1 本身有matched budget crossover与CE/downstream反证方向；[作者仓库](https://github.com/JinjieNi/dlms-are-super-data-learners)明确full paper 10/03、code/logs10/27，作者[Notion](https://jinjieni.notion.site/Diffusion-Language-Models-are-Super-Data-Learners-239d8f03a866800ab196e49928c019ac)写Released on Aug09，实际原件见 [恢复](nov07-narrow-tail-core.txt)。当前没有本窗实质差额披露；拟同家族事件去重，日期不确定不是唯一依据，不扩扫更早月份。
- Common-O 2511.03768v1 的single-image与cross-scene失败对照有明确局部评价贡献；UserAlign有具体fixed response pool/一致无噪声比较条件。两者NeurIPS2025标记触发OpenReview，forum/API实际challenge/403，原PDF可以读取但不提供首公开时刻；停止同路径，不由accepted或submitted认定归属。
- OpenAI 11/06 Enterprise原release中的action controls有真实能力/审批变化：new actions默认disabled，modified actions沿用prior state，refresh需要admin作为user连接。原release足以支持这项披露，不支持当前Help中所有后续frozen snapshot/兼容性语义。请保留具体安全约束变更的准入判断，不因“权限成熟”关闭；原日期粒度尚不能授本窗。

后续普通待办仍逐项保留在 [TOPIC_SCREENING.md](TOPIC_SCREENING.md) 与 [日报§5](../../07/README.md)。没有冻结新分母，没有Books写入或日级独立复核。

## 交接增量

最新五项exact-v1恢复、OpenHands未来v2证据撤出及SCALE-Route误标纠正，连同逐ID普通下一步集中在 [CURRENT_STOP.md](CURRENT_STOP.md)。不重复已校准摘要/未变必要证据；此补充不授日期或证据完成。
