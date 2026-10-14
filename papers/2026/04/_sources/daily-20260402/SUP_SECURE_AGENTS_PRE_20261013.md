# SecureAgents30016 受限 proposal PRE（未授锁、未写 Books）

Owner `PLATFORM-SECURITY` / Ch72；现有Prompt Injection的执行器边界段后、Rule of Two前，一段与本人末注。resume reader actualII/III/IV Source5与root normalpaperv1日门通过；作者actual完整III及当前1397–1440邻接。只保指令recognition→是否遵循的显式分责proposal，不将成熟plan/enforcer组合全算新增、不授实证防御。

## 当前完整局部与拟段

第 78 章会展开 Tool Calling 机制；本章只冻结平台控制：模型不能授予自己权限，检索内容不能改变 authorization，敏感操作必须有独立 policy decision。

一条尚未验证的设计proposal，是进一步把“模型认为自己要遵循什么”与“系统准许遵循什么”分开：要求模型显式列出拟遵循指令，由系统回指其来源，再按既有policy阻止不可信来源或请求确认；读取外部内容前也可预声明是否预计该源含有可执行指令。需要语义裁决时，可只向bounded judge提交已维护的instruction state与拟变更diff，避免把raw环境全文交给拥有决策任务的模型。这改变候选指令与授权判断之间的可审计接口，不证明模型自述忠实、provenance完整或typed表示无注入。[Secure Agents的必要proposal](https://arxiv.org/html/2603.30016v1)尚未实现并验证这条路线；漏列、错误来源归属、diff遗漏语义或共同模型偏差仍会使裁决失效。识别/来源核验、结构维护、judge与人工确认都付费；无法可靠回指来源或高风险动作仍有歧义时，保留确定性allowlist、最小权限与明确人工/effect-time授权，而非让自述或一次模型判断替代policy。<!-- source-family:SF-2026-ARXIV-2603-30016 -->

在实现逐次授权之前，还可以先检查会话是否获得了危险的能力组合：A 是处理不可信输入，B 是访问敏感系统或私有数据，C 是改变状态或向外通信。[Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/)提供一条低成本部署分支：同一会话兼具 A、B、C 时，不允许无监督自治；可以关闭敏感访问、限制外发对象，或让可靠监督者核验实际动作与内容。限制功能会降低可用性，监督与来源信任确认也有成本，但这比等模型识别出所有注入再决定执行更直接。

## 拟本人末注

- `SF-2026-ARXIV-2603-30016` — Daily 2026-04-02补04-01自然日；[exact-v1](https://arxiv.org/html/2603.30016v1) II/III/IV，2+1+2=5。只采unimplemented proposal的verbalized intended instruction/provenance与follow-decision分责、预声明期待和只见structured diff的bounded judge。原文benchmark批评不作该proposal实证；typed/self-report不授防注入、100%安全、忠实性或policy authority，成本/退回确定性规则与人工近文，未核实现/复现。
