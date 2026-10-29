# PRE08：双轴升级不等自动授权

已读reader R16实际意见，writer重新完整读Ch72 Safe-commit引导/流程及certificate代价退路、紧接白盒guardrail两段、Tool Boundary整段，以及Ch71/73开篇交接。现有all-world safety与independent IAM不承载资源风险/认识不确定分别升级的双轴提案；以下不宣实现或校准，未写Books。

## I25 / 11414 / PLATFORM-SECURITY Ch72 / 2+1+2=5

文件 `books/part-06-ai-infrastructure/72-security.md`，完整“Certificate 不替代 IAM、sandbox、审批或 compensation”三行段后、`<!-- semantic-body-binding:SF-2026-ARXIV-2605-10901:start -->`与完整guardrail区域证书段前。

拟正文全文：

升级审批也可先拆开两个不相互抵销的轴：资源/动作的固有后果决定risk，当前证据不足或模型不知道决定epistemic uncertainty，任一越界都触发人工，而不是把高自信抵扣高风险。[TBAC的未验证提案](https://arxiv.org/html/2510.11414v1#S3)将这份升级判断与执行分开，由可信policy发出范围/期限受限的capability，再由PEP核验后才产生effect；模型只提议和提供风险线索，不自授凭证。双轴/阈值和短凭证是设计接口，不是已校准的安全概率或完整实现，原文将校准、风险与注入测试留待未来，低风险且低uncertainty也不能自动证明应当允许。取证/评分、人工等待、凭证发行撤销和执行核验均费；风险依据、身份/范围或认识资格不足时，保留确定性拒绝、最小权限与独立人工审批，不由置信度、MAC通过或一次概念流程签发真实安全与生产授权。

<!-- source-family:SF-2025-ARXIV-2510-11414 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11414`：Popper，Daily2025-10-15补Oct14；本人首次必要§II–VI及VII/VIII，Epicurus R16定点反侧，2+1+2=5，安全具体gap深入。只risk/epistemic双轴升级与短capability/PEP职责提案；未实现/未校准、注入future及全费明确，不授自动approve可靠性/授权实现/安全保证。未读代码或复现；PRE/SAVE/完整自读/solePOST仅本日canonical实际层。
