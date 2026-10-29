# 02060 TELBench / DRIFT：过程标签、支持状态与错误传播

root，仅06-03补Jun02；R62完整题摘/准入/联合日证有效复用，不改旧字段。[当前官方页](https://arxiv.org/abs/2606.02060)所见v2 Jun02，未见撤回/纠错，本次仅[exact-v1](https://arxiv.org/html/2606.02060v1)。实际必要读§3–6、B工具设置、D token表及§3.1完整标注协议；未读全taxonomy/prompt/案例/消融附件、代码或复现，访问2026-10-25 BJT。不为v2号变化额外做旧新全文diff。

## 必要判断

数据先把不同框架的事件折为semantic spans，嵌套subagent依语义执行次序展开、manager消息主要作上下文摘要；这已经是依赖解析的派生视图，不等原始日志逐字完整。边界按目标、候选、时间范围/核验标准变化，正常重试/改写留同span；因此换segmenter就可改变first-error索引和分母。

DRIFT是**读取完整已完成轨迹的离线审计**：先记录claim首次提出、首次被当成决定依据、后续复用与状态；再把支持标direct/weak/missing/conflicting；最后依实际承诺/复用/放弃/定稿是否让风险变得有后果而标error span。仅弱支持或失败search不自动错误。它输出的是标签定位提案，不运行修复、不中断在线action，也不是原文支持/根因的形式化oracle。由未来完整轨迹回溯找早错，不能写成错误发生当时即可检测。

465tasks×三backbone×两框架=2790轨迹，任务复用造成相关，不能当2790独立任务。双不同family LLM提高召回，再由七专家池中两人核完整轨迹/补改/裁决；作者称每人300h以上，不等金标准绝无漏标。1890有error的pool再筛稳定边界/内部可核证据/正常span干扰→1000（600easy/400hard）；它不是自然全成功/失败流量样本，也缺完全无error run的独立误报校准。Span负例并不补出all-clean run特异性；36.9%成功run仍有process error仅对应原人口，非普遍错误率。

主评统一question+ordered spans、三次重复，macroP/R/F1与首错误accuracy是不同目标；更高F1仍伴hard首错定位很低，不能由总体分数认证每个根因正确。模型列表主文Sonnet4.5而主表Sonnet4.6，必要B另说明轨迹生产工具/多模态配置，不能合成所有auditor精确统一版本；此处不采用跨backbone精确排名/倍率。仅统一Serper/Jina，代码/多模态工具保各框架native，剩余wrapper与工具差异不是完全消除。Hardware/precision、全部sampling/revision/输入长度与服务并发/SLO未充分披露，不补。

§6 claim/support/dependency增量消融同时增加推理调用，不证明单模块等预算因果。D token表明确DRIFT相对bare大多多费，Gemini明显更高；“多位于Pareto”是作者局部图与tokenproxy，不等美元、墙钟或生产总体效率。较长span复杂度各法都退步，更多参数不单调提升也不证明结构是唯一原因。三次重复未给全部误差区间，未看图像精确点；不把专家标签、支持status或模型依赖图升级为真实因果/事实认证。标注/segmentation、三阶段审阅、全部trace驻留/调用与独立验证均计费；支持与直接反侧足，停止全附件。

## 正式拟6分与actual Books具体已有覆盖提案

2+2+2=6：有害承诺及传播与普通探索分开的测量/审计接口，跨trace视图、证据与评价；不是按2790/1000规模、Agent框架名或up-to30分加分。潜在贡献资格保留，不因最终NC降分。

原初筛AGENT-REFLECTION只是路由，实际新产物是离线过程诊断而非生成器修订，主owner拟`PLATFORM-EVALUATION-SYSTEM` Ch66。实际完整读Ch66“过程评估还需要区分尚未成功探索与已造成错误动作”三值语义、first causal error→propagation→recovery完整代码与两段：保普通探索/不可观察则不判错、后续重复传播非独立缺陷，以及run级exploration/exploitation的机会集边界；又读“Raw Score→Claim Sensor”完整typed span/原子claim与外部支持分权段。Ch65/67开篇确认调度/monitor不接管标签权限。

actual Ch69“从Linear Trace到Root-cause Graph”的完整dependency view→backward slice/候选责任→复现/abstain流程及两侧限制，和claim-centered evidence graph的observation/变换/policy→action→validation段，已经承载从原始记录派生依赖、追踪claim支持/下游复用与候选归因非真值。Ch80已读原子claim盲再回答、span反馈及“修好不等诊断正确→Ch69受控重放”交接，不能把本离线audit误成已执行Reflection修复；邻Ch79/81职责已读。

因此具体NC提案为：**现有Ch66已定义无害探索/有害承诺、首错与后果的评价义务，Ch69已定义claim支持与复用依赖、不可变trace/派生view和非因果归因边界；DRIFT提供同义务的另一LLM审阅组织实例，受限新标签结果尚未改变既有设计判断。** 不假称现章逐字实现DRIFT算法、不把主题映射或旧trace当同事件重复；精确标注人口、受限比较及未来可核证据保Report。不为三个组件名重复加正文/末注，若独核发现真正未承载命题再具体指出小gap。

当前首次必要/正式六分/actual具体NC待唯一独核，未改Books/Report/State或预NC/DAY。Source支持限于本精确版本，不执行攻击/写代码或扩别日队列。

## 采用独核R151的具体覆盖补正

R151实际在Ch66“Failure Evaluation要从最终错误追到首次有害承诺”下找到同family `SF-DRIFT-TELBENCH`真实两段，已承载span/first harmful commitment/claim lineage与propagation及localizer非因果oracle；不是仅generic span主题。结合原Ch66/69具体组，首次必要/正式6/主owner Evaluation与NC通过。root行政融Report，不新Book/注、事件duplicate或预DAY。
