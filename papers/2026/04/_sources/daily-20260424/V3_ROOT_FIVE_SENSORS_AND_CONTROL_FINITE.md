# 2026-04-24 五项 sensor 与控制候选的有限非作者核

复核者 root；官方 exact-v1 原文与当前 owner 命题对读。这里仅决定五项受限贡献/Books 状态，不以五项替代全部来源、日期和日级独立 Gate。

## `2604.21057v1` TRACES：可学早停 sensor，不是正确答案 oracle

[官方 §3–6、Appendix D/H](https://arxiv.org/html/2604.21057v1)把 reasoning step 文字分类，再以连续步骤角色比例触发强制答案；其 ideal-stop 对照需要 ground-truth answer，实际控制器并无此输入。作者离线回放和时延回归估计的 token 节省不能直接充当线上 SLO；标签误差与强制读出成本需分账。第66章已有“早停信号与外部正确性分权、总成本验收”的长期论点；维持 2+1+2=5、标准审阅、仅报告，不把角色迁移签发为正确性证明。

## `2604.21083v1` API Gateways：行为指纹不是后台认证

[官方 §3–4、Appendix E](https://arxiv.org/html/2604.21083v1)用多类固定 probes 的回答结构训练 per-model one-vs-rest 分类器；同一 `(model,test_id)` 的重复样本被分进训练/测试，不能外推到新 prompt domain 或未知 backend。多轮回忆失误可能是模型失误或截断，gateway 自报 token/billing 不是独立算力证据。第62章有服务身份与路由合同，第66章有测量校准责任；这项黑盒诊断可保留，却不能取代 artifact attestation。维持 2+2+2=6、深入审阅、仅报告。

## `2604.21098v1` Propensity Inference：随机环境因素不识别模型意图

[官方 §2–4](https://arxiv.org/html/2604.21098v1)随机化环境因素，以 Bayesian logistic GLM 估计所定义行为的条件 effects；模型与环境 intercept 有协议意义。作者自己将 odds ratio 2 宽松说成行为率翻倍，但两者并不相等；“战略因素约半”亦只是该模型比较的预测份额，不是意图的因果分解。第66章已有能力、elicitation、机会和行为观测的分权，维持 2+2+2=6、深入审阅、仅报告。它不能证明特定模型持久不对齐或生产事故概率。

## `2604.21131v1` Cross-Session Threats：更正指标名后仅报告

[官方 §3–6](https://arxiv.org/html/2604.21131v1)提供跨 session 攻击/良性场景和检测协议，但 §4.3 明定 `precision = 1-FPR`，这实际是 specificity，不是 `TP/(TP+FP)`；其所谓 F1 因而不是通常 precision–recall F1。复合指标再加可补偿的 prefix 稳定项，也不能充当“所有安全条件必须通过”的 release gate。第72章已有跨 session 状态与权限边界，第45章拥有 prefix/KV 身份；新数据集可作受限压力测试，指标名与保证不能直接进入长期正文。维持 2+2+2=6、深入审阅、仅报告；不否定可独立复核的局部检测结果。

## `2604.21164v1` MAGIC-TTS：局部时长控制不保证 missing/zero 可辨

[官方 §3–4](https://arxiv.org/html/2604.21164v1)在声学生成条件中加入 token-duration/pause 残差和 availability mask；无控制样本仍可走原分支。但 zero 经中心化可能给零残差，missing 亦由 mask 置零，单凭该支路不保证输出上区分“显式零”与“未指定”。MFA 对齐参与目标和测量，有限编辑示例不证明所有未编辑区域保持。第24章拥有多模态生成的条件/状态链，这一 TTS 具体编码不构成通用控制原理，维持 2+1+2=5、标准审阅、仅报告。

五项未写 Books；全日仍进行中。
