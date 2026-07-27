# 第68章 Security

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** 模型、数据、API、Prompt、工具调用的安全边界。

## 本章要回答的问题

AI Platform 的安全为什么不止 API authentication？数据、训练、artifact、runtime、Prompt 与工具调用形成了哪些新 trust boundaries？如何避免把模型输出当成可信指令？

本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**

## 从资产与信任边界开始

需要保护的资产包括：

- source data、labels 与 user context；
- code、images、dependencies 与 credentials；
- checkpoints、adapters、tokenizers 与 prompts；
- registry metadata、evaluation 与 approvals；
- GPU nodes、runtime memory 与 KV Cache；
- APIs、tools、business systems 与 audit evidence。

主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。

## 生命周期威胁

```text
Data
  poisoning, leakage, license/provenance failure

Training
  untrusted code, secret exposure, compromised dependency

Artifact
  overwrite, substitution, unsafe deserialization, model theft

Serving
  auth bypass, DoS, side channel, data exfiltration

LLM/Agent
  prompt injection, insecure output handling, excessive agency
```

单一 WAF 无法覆盖这条链。每次从一层向下一层传递，都需要验证 identity、integrity 和 authorization。

## Supply-chain Integrity

Artifact contract 应包含：

```text
source revision
builder identity
build parameters
materials/dependencies
artifact digest
signature / attestation
verification policy
```

SLSA 将 provenance 定义为可验证的“何时、何地、如何由谁生产”。平台可以要求 image、runtime engine 与模型 bundle 在 admission/load 前验证 digest 和 attestations。

签名只证明某身份签过，不证明内容安全；仍需 vulnerability scan、policy review、sandbox 和 runtime restrictions。

## 模型文件与训练代码是不可信输入

某些 serialization format 加载时可执行代码；remote code、custom ops 和 notebook image 都可能突破数据边界。平台应：

- 优先使用数据型安全格式；
- 将转换放在隔离 builder；
- 禁止默认执行 remote code；
- 最小化 service account 与 network egress；
- 扫描依赖并固定 digest；
- 对高风险 workload 使用 sandbox/专用节点。

“模型来自内部 bucket”不等于可信，内部 account 也可能被滥用。

## Prompt Injection 与 Tool Boundary

Prompt injection 的根因不是“模型没有听 system prompt”，而是系统把不可信内容与高权限指令放入同一个模型上下文，再把输出当作 action。

安全边界应位于工具执行器：

```text
model proposes action
→ typed schema validation
→ policy and authorization
→ parameter/content validation
→ optional human approval
→ least-privileged execution
→ result filtering and audit
```

第 74 章会展开 Tool Calling 机制；本章只冻结平台控制：模型不能授予自己权限，检索内容不能改变 authorization，敏感操作必须有独立 policy decision。

## Availability 与 Abuse

AI API 的 DoS 不只看 request count。超长 prompt、超大 output limit、expensive tool loops、adapter churn 和 cache-busting 都能放大成本。Gateway 与 runtime 应联合执行：

- body/context/output bounds；
- token/concurrency budgets；
- admission deadlines；
- per-tenant cost limits；
- tool-step limits；
- model/cache identity validation。

拒绝原因与 policy version 必须审计，以便区分攻击、误配置与容量不足。

## 风险管理而不是一次性认证

NIST AI RMF 用 Govern、Map、Measure、Manage 组织持续风险管理。对平台而言：

- Govern：owner、policy、exception、accountability；
- Map：use case、assets、affected parties、threat model；
- Measure：evaluation、red team、monitoring、security tests；
- Manage：mitigation、release gate、incident、rollback。

安全控制会随模型能力、工具权限与业务后果变化，不能在平台上线前一次完成。

## 本章在知识树中的位置

本章横切 Part I～V，并为 Part VI 建立 action boundary。下一章将质量、SLO、成本、tenancy 和 security 收束为 production readiness，而不是把“部署成功”当成终点。

## 自检问题

1. 为什么模型输出不能被视为可信主体？
2. 签名与 provenance 分别证明什么、不证明什么？
3. 模型 artifact 为什么可能执行恶意代码？
4. Prompt injection 的真正权限边界应放在哪里？
5. AI DoS 为什么不能只按 request rate 防护？
6. NIST AI RMF 的持续闭环如何映射到平台？

## 小结

AI security 必须贯穿数据、训练、artifact、serving 与 action。正确设计不依赖模型永远服从，而是让任何不可信输出都经过独立、最小权限、可审计的执行边界。

## Review notes

本章没有提前展开 Part VI 的 Prompt/Tool/Workflow 机制，只冻结平台 security contract。OWASP 列表作为威胁入口，控制设计仍回到资产、主体、trust boundary 与生命周期。

Primary-source 与官方入口：

- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- SLSA specification: https://slsa.dev/spec/v1.2/
- Kubernetes multi-tenancy/security: https://kubernetes.io/docs/concepts/security/
