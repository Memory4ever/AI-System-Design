# 01472 HOPM：选择版本与修改指令的粒度分离

仅06-03补Jun02；当前合同/ROADMAP与本日停点有效加载，R122–123完整v1题摘与联合Jun02日证直接复用。[当前abs](https://arxiv.org/abs/2606.01472)所见唯一v1，无withdrawn/removed说明。[exact-v1](https://arxiv.org/html/2606.01472v1)实际读§3–8完整核心/主评价/限制及A.1–A.4直接校准边界，没有读所有引用、未取得私有case级数据/代码或运行实验。访问2026-10-25 BJT。

## 必要支持与限定

Typed evidence→family/version bandit选择→生成→guardrail/judge与抽样人审→按CTAM把失败映射到允许修改的指令类别→创建新version并校验→后续路由，分别维护router参数与mutation priorities。请求路径是生成/校验，人工/auto feedback形成off-request更新，不是当次所有反馈立即可得。这里prompt-token指自然语言指令类别/片段，不是模型内部tokenizer或权重更新；deterministic attribution map只定义操作责任，不证明该片段是真实错误根因，也不使事实/权限检查获得确定语义。

表1九类从title/role/evidence/OCR到格式语法，只是本场景mutable surface，不能从taxonomy直接导出跨任务完整策略。算法1给reward加权形式但未给足具体bandit策略/探索参数、lambda、mutation criterion/优先级更新或每variant冻结的prompt/基模/轨迹预算，不能签一个可直接复现的online学习recipe。候选通过schema/policy才有资格探索的caption是作者公开流程，不等已核实现会覆盖所有事实、引用和权限边界。主模型精确身份/revision、hardware/precision、输入输出长度、concurrency/完整SLO与总token/人审费未充分披露，Not Disclosed。

主评价为7×同600case的matched production-evaluation，不是随机线上A/B；固定case ID和amount可配对，但同一case下不同文稿的downstream win怎样获得、时序/评审盲化/在线反馈隔离未有本必要域足以独立核验的原始记录。只保作者描述的同case七配置有限比较，不把“production”改为模拟，也不升级实时流量因果。Static禁routing/mutation/human/autojudge，其他臂按表改变，非完整factorial；若干比较同时改变多个模块/反馈，不能唯一归因某个bandit、CTAM或双loop算法。

T3/4 full在作者四endpoint总体最好，但guardrail pass78.8低于human-only79.0与mutation-only79.7；计数胜率、人审Likert和必须通过的guardrail不是同一质量量。Full-human amount差CI跨0，不照count显著性授金额显著。Wilson/1000bootstrap/McNemar是作者在matched单位上的统计，不代私有数据或未来分布验证。770review的多数分布是318 labeled export投影，reviewer shared IDs不稳定无法恢复text kappa；10case/61rating小重叠Fleiss近零不能由最佳pair覆盖。OCR70case/350rating是另一人口，不能拿OCR agreement替主文稿质量或claim真实性验证。SNAD约753/770使稀有fraud/INR外推受限，constructed example只是可解释schema不是真实raw复现。

同作者01472/01542等共用770review/OCR材料只是一份共享校准证据，不按论文数算独立重复。所需未披露recipe或未来randomized流量证据只影响强因果/复现/生产保证，不阻原公开接口的有限理解；不为此扩同机构全史/私有访问请求。案例制备、bandit探索/弃选、生成校验、反馈人审、mutation及独立回归均计费。

## 拟分与actual owner/具体NC提案

2+1+2=5：D2仅针对family/version选择与失败归因后局部修改两粒度的受限接口；Reach1为prompt配置控制，不借高风险业务、金额或通用治理加跨层分；Durability2为选择/编辑/发布责任可复用。成熟bandit/双反馈名称不额外计分，不因Books覆盖降分。已深入必要命题/直接反侧，未授全部宣传。

唯一`AGENT-PROMPT` Ch74，而非给Ch81/84再复制优化过程。实际完整读“Prompt生命周期”版本/模型/工具/eval/cohort/owner、offline regression/canary/rollback两组；“从固定Prompt Score到Constraint-residual Feedback”完整原反馈链、mutable failure priorities、独立validator权限/经验可行/反馈漂移和回退；又完整读SkillOpt两段：局部patch、合并冲突/edit-budget、selection split严格接纳、rejected buffer、slow/meta保护与部署分责。现有正文已具体承载版本化候选池、按失败条件定位下一轮修改、局部编辑与候选保留/独立最终验收、原提示与人工回退，足承载拟长期选择/编辑责任分离。HOPM的业务CTAM列举与未完整披露的bandit更新未形成需要新owner论证的独立算法；不为新论文名/同类流程再加段。提案具体已有覆盖，不是事件duplicate；私有matched结果与recipe未披露边界留Report，不能借NC略去反侧。

首次必要/正式拟分/actual具体NC待唯一独核，未改Book/Report、不预NC生效/DAY。当前支持足即停止，不索不存在的公开raw或声称实现复现。

## 已采用独核结果

R141首次必要/正式5分/actual Ch74三组具体已有覆盖已通过，root仅行政融本日报103态，不新增Book或末注；不改原准入、Jun02日证或宣称整日完成。
