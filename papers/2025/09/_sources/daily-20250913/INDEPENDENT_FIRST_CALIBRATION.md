# 13 首批及单项 Books 校准

复核者：root，2026-10-06。启动重读 AGENTS、Prompt、当前研究/Report合同、每日来源说明、ROADMAP及本日停点；这里只校准局部，尚非最终 DAY。

## 正式发布：准入与具体已有覆盖通过

实际读 `openai-caisi-web.json` 原官方正文，尤其L39–74，并解析本日 `openai.raw` RSS：对应标题、link及 `Fri, 12 Sep 2025 12:00:00 GMT`，转换为Sep12 20BJT完全落窗。不是把403响应当正文。

传统漏洞原被认为不可利用，加入Agent hijacking后成为可执行权限风险链，是新公开局部反例；2+2+2=6合理，安全变化使必要受影响核心需深入。本次原文读取支持该局部报告，不支持总体成功率、当前防护率或修补实现已核：约50%缺attempt/样本分母、漏洞细节与完整trace；一工作日修复是厂商声明。UK AISI的非公开工具、monitor CoT与禁用enforcement属于特权测试条件，不外推普通攻击者。

Books上下文已实际读取。Ch72的“Prompt Injection 与 Tool Boundary”承载数据不能升级指令、executor独立授权与effect前再检查；“Safety Evaluation 的单位是 Run”承载完整配置/预算/分母、替代解释和不以单项release；“Integration-aware Campaign”承载connector、credential scope、destination/argument、fixture与effect身份。Ch71开头四隔离平面和共享凭据缺口、Ch73开头PoC证明责任与Production Contract已实际读，控制和release owner未混写。此Blog未披露新增防御机制，上述长期边界已具体覆盖；**已有覆盖，正文增量0**。不得把这一裁决授予其他日期潜力或无关书稿修改。

## 题摘实际范围与修正

从本日 `scoped-abstracts.json` 实际完整读：8首批潜力09782、09790、09864、10140、10312、10377、10396、10439；11具名安全/保证/因果信号09893、09942、09955、09970、10018、10260、10278、10298、14256、10594、10401；5负侧/局部潜力09801、09867、10099、10116、10199；10建议关闭09774、2511.11572、09869、09918、21336、10000、10147、10284、10289、10366。共34唯一完整题摘，不冒称69全部或精确v1全部；例如10439v2、10199v3及多项安全当前v2只能作发现。

8首批及5负侧保留最小潜力：query/model质量成本路由、grounded复杂动力学反馈退化、latency/token联合TTC、VQ更新与codebook梯度、空间缓存、neuron重组、inpainting解决零梯度与Local SGD outer optimizer分别可能改变具体选择。小模型、少epoch或负结果不足以排除；性能归因与理论假设仍未验证。

**09774恢复潜力。** 原文不只是列工具，提出将FFT/matmul/QR分解为共同primitive并逐级控制frequency/resource比较。这可能改变编译/硬件设计的公平评价边界，与本项目计算实现直接相连。不能仅因HPC题名关掉；不因此授具体LLM加速、评分或落窗。其余9关闭在当前读过范围成立：明确旧总结；领域registration/磁体应用尚未建立foundation主线差额；WALL组合；HetaRAG未来构想没有可核的新融合机制；经济/伦理倡议；传统MAPF执行没有建立模型驱动机制关系；image codec KD未指明新的训练或资源边界。以后出现具体增量时定点重开，不把本次摘要关闭解释为学术价值判断。

11风险信号不能因为日期隔离被普通关闭：collision-free须核precision边界；安全reward不等真实漏洞消除；token merge不是隐私保证；firmware修补不授全安全；匿名语义补偿可能重识别；reward hacking、伪造检测与对抗鲁棒需要评价条件；广告检测人口与因果scaffold不足以证明生产或干预忠实。作者需读支持这些处置的必要精确版本方法/限制，10439理论保证同样核原假设；不要求全部59潜力全文。

## 剩余普通工作

作者同步09774及59/10计数、正式候选已有覆盖，完成上述必要反侧；其余有限来源/分层样本及最终六部分仍需DAY。当前没有授整日通过、正面arXiv Evidence、日期Coverage或无遗漏。已有覆盖的单篇不等待其他材料，但未完成的普通工作不能被称终态受阻。
