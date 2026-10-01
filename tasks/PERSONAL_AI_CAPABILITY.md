# Personal AI Capability：产品命题与验证任务

> Status: Thesis / Discovery  
> Created: 2026-09-20  
> Scope: 长期产品方向，不属于 Books 章节进度，也不直接改变 `progress.yaml`

## 一句话命题

当 Agent、Skill、Tool、MCP 和专业服务大量增长后，用户面对的核心问题将从“信息在哪里”逐渐变成：

> **什么能力最适合在我的环境中完成当前任务，并且如何可信地获得、授权、执行、验证和持续优化它？**

Personal AI Capability 的目标不是再制造一个万能 Agent，而是建设 **Capability Intelligence Layer**：根据个人长期 Context 理解用户的目标、工作方式和能力缺口，在不断增长的 Agent 生态中发现、排序、生成、组合和迁移可执行能力。

## 为什么值得长期关注

传统搜索引擎解决 Information Retrieval：从大量网页中找到与 Query 最相关的信息。Agent 生态需要进一步解决 Capability Retrieval：从大量 Skill、Tool、MCP、Agent 和 Service 中找到能够完成任务的能力。

二者都需要 retrieval 和 ranking，但 Capability 的选择后果更重。网页相关不等于任务完成；一个可执行能力还涉及：

- 是否适配用户的环境、数据和工作流；
- 是否拥有必要权限和凭证；
- 成本、延迟和可靠性是否可以接受；
- 能否与其他能力组合；
- 执行结果是否真正满足目标；
- 失败后能否恢复、审计和撤销。

因此，这个方向更接近以下系统的组合，而不是其中任何一个的简单复制：

```text
Search Engine       找到候选能力
Recommendation      判断什么最适合当前用户
App Store           分发、版本与商业交易
Package Manager     安装、依赖与兼容性处理
Agent Control Plane 权限、执行、状态、验证与审计
```

## 对 Agentic OS 的判断

Agent 很可能走向“操作系统化”，但这不等于所有 App 都会消失，也不等于市场最终只剩一个 Super Agent。

更稳定的判断是：用户交互会从 **App-centric** 逐步向 **Goal-centric** 迁移，过去由人完成的跨应用 orchestration 会越来越多地交给 Agent：

```text
User Goal
→ Task Decomposition
→ Capability Discovery
→ Capability Selection and Composition
→ Permission
→ Execution
→ Verification
→ Result
```

底层终局可能同时存在：

1. **Super Agent**：一个主要入口负责跨领域任务。
2. **App + Embedded Agent**：现有应用保留数据、权限和业务逻辑，Agent 成为新的交互层。
3. **Multi-Agent Federation**：个人 Agent、企业 Agent 和专业 Agent 通过协议协作。
4. **Protocol-centric Agentic Web**：能力通过开放协议被发现和调用，不由单一平台垄断。
5. **Vertical Agent**：医疗、金融、研发等受专业知识、数据和监管约束的领域形成独立体系。
6. **Hybrid**：用户看到少数统一入口，系统内部仍由大量应用、Agent、协议和服务协同。

本项目不押注其中某一种形态独占市场，而押注它们共同产生的需求：

```text
Agent 数量增加
→ 可执行能力数量增加
→ 选择、组合与治理复杂度增加
→ Capability Retrieval and Ranking 成为基础设施
```

## 产品在系统中的位置

```text
┌──────────────────────────────────────────┐
│ User Goal                                │
├──────────────────────────────────────────┤
│ Planner / Orchestrator                   │
├──────────────────────────────────────────┤
│ Personal Capability Intelligence        │
│ - Context Understanding                  │
│ - Capability Gap Detection               │
│ - Retrieval / Ranking                    │
│ - Recommendation / Composition           │
├──────────────────────────────────────────┤
│ Skill / Tool / MCP / Agent / Service     │
├──────────────────────────────────────────┤
│ Identity / Permission / Payment / Audit  │
├──────────────────────────────────────────┤
│ Execution Runtime                        │
├──────────────────────────────────────────┤
│ Existing OS / App / SaaS / Infrastructure│
└──────────────────────────────────────────┘
```

产品不必自己实现整个 Agentic OS。更现实的定位是成为不同 Agent Runtime 都需要的 Capability Layer，并通过开放接口接入它们。

## 核心闭环

```text
Long-term Personal Context
→ Task and Habit Understanding
→ Personal Capability Graph
→ Capability Gap Detection
→ Search and Rank Capabilities
→ Install, Generate or Compose
→ Authorize and Execute
→ Verify Outcome
→ Update Context, Graph and Ranking
```

### 1. Know Me

从设备活动、项目、历史任务、显式目标和用户反馈中理解：

- 用户正在做什么；
- 哪些流程重复发生；
- 用户当前掌握和经常使用什么能力；
- 用户的环境、成本、安全与合规约束；
- 用户接下来希望到达什么状态。

原始 Context 应优先 local-first、user-owned。系统不应默认把完整屏幕、文件和对话上传到中心服务。

### 2. Grow Me

根据历史行为和目标发现 Capability Gap：

- 已有能力是否缺失关键步骤；
- 重复人工流程是否值得 Skill 化；
- 现有能力是否错误率高、成本高或长期不用；
- 应该安装成熟能力、组合已有能力，还是生成个人能力。

### 3. Move With Me

能力应尽可能属于用户，而不是被锁定在单一模型或 Agent 平台。系统需要逐步解决：

- Capability 的可移植描述；
- Tool、permission、sandbox 和 authentication 差异；
- 版本、依赖和兼容性；
- 用户授权、商业许可和付费关系；
- 从一个 Agent Runtime 迁移到另一个 Runtime 后的行为验证。

## 真正需要建立的数据资产

产品壁垒不应被定义为模型、Memory 数量或 Skill 数量，而应来自两个持续更新的图和真实结果数据。

### Personal Capability Graph

描述一个用户：

- 会什么、不会什么；
- 正在学习或建设什么；
- 使用什么工具和环境；
- 哪些能力在什么任务中有效；
- 当前目标与能力之间还缺什么。

### Capability Graph

描述一个能力：

- 解决什么任务；
- 需要哪些输入、权限、环境和依赖；
- 能产生什么结果；
- 可以和哪些能力组合；
- 成本、延迟、安全和失败模式；
- 在不同用户与环境中的历史结果。

### Outcome Data

最有价值的反馈不是“被点击或调用”，而是：

```text
什么用户
在什么环境
面对什么任务
选择了什么能力
执行过程发生了什么
最终目标是否真正完成
```

这些数据决定 Personalized Ranking 是否会随着使用持续改进。

## Ranking 的初始问题定义

第一阶段可以将推荐理解成一个受约束的排序问题：

```text
Score(capability | user, task, environment) =
    task_match
  + user_fit
  + environment_fit
  + historical_success
  + trust
  - cost
  - latency
  - security_risk
```

这不是最终数学模型，只用于冻结输入变量。后续需要区分硬约束和软排序：没有权限、平台不兼容或违反安全策略的候选，应在 ranking 前过滤，而不是仅降低分数。

## MVP：Context → Capability Recommendation

第一版不做完整 Agentic OS，也不先建设公共 Marketplace。最小验证闭环是：

> 观察一个开发者的长期工作，在可解释、可授权的前提下发现重复流程和能力缺口，每周推荐少量高价值能力，并支持安装或生成，然后衡量它是否真正改善结果。

### MVP 输入

- 用户主动选择的活动记录；
- 最近 7～30 天的任务、工具和工作流；
- 用户声明的目标、环境和数据边界；
- 已安装的 Skill、Tool、MCP 和 Agent 能力。

### MVP 输出

- 最值得新增、删除或改进的 1～3 个能力；
- 推荐理由及使用到的证据；
- 安装现有能力或生成个人 Skill 的选择；
- 权限、数据访问和风险说明；
- 执行后的结果验证与节省量估算。

### 暂不进入 MVP

- 通用 Agent Runtime；
- 完整 Marketplace 与支付体系；
- 无限制自动安装或自动执行；
- 跨所有 Agent 平台的通用编译器；
- 依靠未经验证的自动生成 Skill 扩充数量。

## 关键假设与反证条件

| 假设 | 最小验证方式 | 反证信号 |
| --- | --- | --- |
| 用户存在足够多的重复数字工作流 | 对 5～10 名开发者进行 2～4 周 workflow audit | 重复模式稀少，或人工整理成本长期高于收益 |
| Context 能可靠推断 Capability Gap | 对比系统推荐与用户/专家判断 | 推荐长期停留在宽泛建议，无法转化为具体能力 |
| 个性化 ranking 比通用热门榜更有效 | A/B 对比 personalized 与 popularity baseline | 接受率、成功率和留存没有显著差异 |
| 用户愿意授予长期 Context 访问 | 测试 local-first、最小权限和可解释授权 | 即使本地处理，目标用户仍普遍拒绝持续观察 |
| 推荐能力能产生可衡量结果 | 记录时间、错误、成功率和重复操作变化 | 用户安装但不使用，或结果无法验证 |
| 能力可以跨 Runtime 迁移 | 选择两个 Agent Runtime 做最小移植 | 适配成本接近重写，通用中间表示不能降低成本 |
| 生态需要独立 Capability Layer | 访谈用户、Agent 开发者和企业平台团队 | Agent 平台自身能力发现已经足够，用户不愿引入中间层 |

## 第一阶段成功指标

不能只看推荐数量或 Skill 安装量。优先观察：

- Recommendation acceptance rate；
- Capability activation rate；
- 7/30 天重复使用率；
- Task completion rate；
- 经人工确认的时间节省；
- 错误或人工接管次数变化；
- 推荐理由的可理解性；
- 用户撤销权限、停用能力和删除 Context 的比例；
- 相比 popularity baseline 的 ranking uplift。

所有指标都必须绑定具体任务和观察周期，不能用主观“更智能”代替。

## 阶段路线

### Phase 0：问题验证

- [ ] 访谈 10 名高频使用 Agent 的开发者或 AI Infra 工程师。
- [ ] 收集重复工作流、现有能力组合和失败案例。
- [ ] 区分“用户缺知识”和“Agent 缺可执行能力”。
- [ ] 明确哪些 Context 用户愿意提供，哪些必须保持本地。

### Phase 1：个人能力审计

- [ ] 从用户主动选择的数据生成 weekly capability audit。
- [ ] 建立最小 Personal Capability Graph schema。
- [ ] 每周只推荐 1～3 个具有明确证据的能力变化。
- [ ] 保留 `No Recommendation`，不为活跃度强行推荐。

### Phase 2：安装与生成闭环

- [ ] 接入一个现有 Skill/Tool 来源。
- [ ] 支持“安装已有能力”和“生成个人能力”两条路径。
- [ ] 为生成能力增加测试、权限声明和人工确认 Gate。
- [ ] 记录任务结果，而不只记录调用是否成功。

### Phase 3：Capability Intelligence

- [ ] 建立 Capability Graph 和 ranking baseline。
- [ ] 比较 personalized ranking 与 popularity baseline。
- [ ] 引入环境兼容、安全、成本和历史成功率。
- [ ] 支持能力淘汰、合并和版本升级建议。

### Phase 4：跨平台迁移

- [ ] 选择两个 Agent Runtime 定义最小 Capability IR。
- [ ] 分离可移植逻辑与平台特定 adapter。
- [ ] 对权限、凭证、Tool schema 和 sandbox 做迁移验证。
- [ ] 建立迁移前后的行为回归测试。

### Phase 5：生态与商业化

- [ ] 在真实供需形成后再验证 Marketplace。
- [ ] 设计发布、审核、授权、付费、分成和撤销机制。
- [ ] 区分公共能力、企业私有能力和个人能力。
- [ ] 评估网络效应是否来自结果数据，而不是目录规模。

## 决策原则

1. **Outcome over invocation**：调用成功不等于任务成功。
2. **User-owned context**：用户拥有 Context、Capability Graph 和迁移权。
3. **Local-first where possible**：敏感原始数据优先本地处理，只输出必要特征和授权结果。
4. **Recommendation before marketplace**：先证明推荐价值，再扩展供给和交易。
5. **Open interfaces over runtime lock-in**：与多个 Agent Runtime 协作，不把产品价值绑定到单一模型。
6. **Hard constraints before ranking**：权限、兼容性和安全边界先过滤，再做个性化排序。
7. **Verified capability over capability count**：少量经过验证的能力优于大量不可控的 Skill。
8. **Preserve `No Change`**：没有足够证据时不推荐、不安装、不生成。

## 当前最需要回答的问题

1. Personal Capability Graph 的最小 schema 是什么？
2. 如何从活动记录中区分重复任务、偶发行为和长期目标？
3. Capability Gap 如何获得可验证的 ground truth？
4. 什么构成一个可比较、可排序的 Capability unit？
5. 如何在不暴露原始 Context 的情况下完成个性化 ranking？
6. 如何验证一个 Skill 完成了用户目标，而不仅是返回了文本？
7. 哪些部分应该成为开放标准，哪些部分可以形成产品壁垒？
8. 最早愿意付费的用户究竟是个人开发者、团队负责人，还是企业 Agent 平台？

## 当前结论

Personal AI Capability 不应被描述成“另一个 Agent”或“一个更大的 Skill Marketplace”。更准确的长期方向是：

> **建设 Agentic 时代的 Capability Intelligence 基础设施，让每个人拥有可理解、可增长、可迁移、可验证和可治理的 AI 能力组合。**

Agentic OS 是否最终由单一入口、多个 Agent、现有 App 或开放协议主导仍不确定，但 Capability 数量增长带来的发现、排序、组合和治理问题在多种未来中都会存在。这是当前产品命题最重要的抗路径依赖基础。
