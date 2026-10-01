# 2604.25200v1 贡献准入定点核（04/29 作者工作态）

- 官方精确版：[Making AI-Assisted Grant Evaluation Auditable without Exposing the Model](https://arxiv.org/html/2604.25200v1)，§2.3、§5.2–5.6、§6 T2/T5、§7.1/§8；原页的 `28 Apr 2026` 不当作北京本窗首公开时刻。本项若贡献前闭，不为排除追完整时间链。
- 旧题摘入口：私有模型／rubric 与外部可审计之间的张力；原文件、规范化输入、模型／rubric measurement、输出 hash 和签名 bundle 连结。这个问题在主线范围内，不因“grant”应用标签排除。
- 必要原文：原文件和 canonical 表示的 hash、格式转换／注入筛查在 TEE **外**（§5.2）；TEE 启动 measurement 对 model、rubric、prompt、runtime 和 reference manifest 作比较，内部核 canonical hash 并签输出（§5.3–5.6）。§7 明说 attestation 不证明模型质量、公平或 rubric 合理性，也承认 canonicalization 完整性和 TCB 问题。§8 将 canonicalization formal verification 与多阶段 attestation 列作未来工作；没有把它们作为已证明的实现或受控评价。
- 中央保证边界：§6 T5 把“没有静默删输入”几乎归约到 SHA-3 碰撞或 pre-TEE log compromise，但 §5.2 的解析／可见性决定、sanitization 和 hash 均在 TEE 外；外部 verifier 必须另有可信原始文件及可验证转换才能判定 omission。仅比较两个各自一致的 hash，不能证明原始内容完整进入模型。§6 T2 的静态筛查也不证明语义型 prompt injection 被消除。这里指出**印刷架构的保证不由所给步骤推出**，不推断真实产品或代码已有漏洞。
- 实际 owner 对照：`books/part-06-ai-infrastructure/66-evaluation-system.md` 的 Evidence Chain 已把代码／输入／配置／执行／输出绑定 run identity，且不把签名当实验正确性；`books/part-06-ai-infrastructure/72-security.md` 的 service-integrity 段已把 request digest、model/runtime、policy epoch、attested boundary 和 typed verdict 分开，明言 TEE 不证明 host I/O、side effects 或所有执行。本篇的 secret-rubric grant 场景和五层 bundle 是上述合同的具体部署组合，未给出改变输入可信边界、验证机制或评价判断的新增受控证据。其自认的缺口恰落现有 owner 的回退边界，不因可写成“TEE + 审计”自动产生新 Books 命题。
- **作者侧处置：具名前分母关闭，Books No Change；不评分。** 保留原潜在理由和上述反证，供非作者负侧抽样。若出现实际 canonicalization 验证、TEE 外原文可信绑定或多阶段私有 rubric 的新协议／受控反证，可按该具体事实重开；不是外部材料受阻，也不是日级 Gate。
