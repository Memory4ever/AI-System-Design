# FSF 3.0 Books 写后复核

复核者：James，非本次Books写入者；写入者root。仅核 `SF-2025-DEEPMIND-FSF3` 实际正文、原源、完整邻接与末注，不自授22日DAY。没有修改Books。

## 第一次实际 POST

结论：未通过，待一句中的两项限定窄修。

实际原源：本日保存官方 `FSF_3.0.pdf` 精确3.0，重新读取§1.6 p7、§3.1–3.2 pp12–14、§4 p15、§5 p16；不是从root的描述或3.1推定。实际书稿顺读Ch72约2142–2215行，含完整Residual Risk Loop、原Meta v2段、新两段、mitigation三问与条件错误/外部损害边界、后接Instruction Hierarchy；实际Review notes约3348–3370行含Meta v2、FSF3末注与后接条目。Ch71末65行及Ch73开篇至Readiness Gates约1–105行也已读。

发现：Ch72当前2173行的“在ML R&D风险域中，把外部部署和大规模内部部署都纳入safety-case审查”没有原§3.1.2 p12明确的 **model reaching a ML R&D CCL** 条件；邻接正文仅有泛指capability/uplift，不足以把触发阈值补给该政策陈述。该句又说“重要更新重新提交治理审查”，原§3.1.2 p13对象明确为 **material updates to a safety case**，不是任意模型或工作流更新。末注引用§1.6/§3–5不能修补正文范围。建议仅把同句限定为“对风险评估确认已达到ML R&D CCL的模型，将外部与大规模内部部署纳入……；safety case的material update须……”。未要求重写其他正文。

其余实际裁决：

- 外部/大规模内部部署与further development区分原p7支持；当前没有声称所有进一步研发同样审批，也没有将小规模内部使用全部纳入最重审查。
- Misalignment illustrative/exploratory、没有显式risk acceptance criteria，与原p7/p15一致。CoT监测只是一种可能缓解，不能认证不可观察推理或绕过监督；正文没有把它写成许可。
- “治理记录还应”“当监测范围不足……缩小授权/监督/暂缓”承接部署决策者证明责任，属于工程推导；没有冒称DeepMind已执行这些控制或其有效性被实验证实。两段都未量化残余风险或授零风险。
- 原Meta v2→内部部署范围/标准状态→三个mitigation问题的推进自然；成本和旧低风险路径仍在附近，不建立平行政策收纳章。Ch71 identity/tenant不替代安全审批，Ch73 lifecycle Gates继续拥有生产执行门槛，没有侵占owner。
- 实际末注以精确3.0官方PDF、§1.6/§3–5定位并明示政策证据非有效性/统一阈值，与采用权限一致；未使用2026版反推。

待root只改上述限定后，复核者重新实际读该句、完整相邻论证和末注再裁决。22仍进行中；当前不能把FSF Books记为POST通过。Omni owner裁决另待root，本记录不验收它或14源/DAY。
