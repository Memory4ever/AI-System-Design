# 2025-09-13 首批准入交接

作者Bacon。独立窗口2025-09-12T09:00:00+08:00～2025-09-13T09:00:00+08:00。启动已完整重读AGENTS、研究/Report合同、Daily/arXiv来源、Prompt、ROADMAP与9月route；没有继承前日筛选。原件`transport.json`记录33次有界请求及真实时间/错误，另有精确targeted记录；Books/共享索引未写。

## 先交一项确切落窗发布

[OpenAI CAISI/AISI安全更新](https://openai.com/index/us-caisi-uk-aisi-ai-update/)由本日官方RSS原`Fri, 12 Sep 2025 12:00:00 GMT`支持Sep12 20BJT。直接HTTP403原失败保留，web工具实际恢复官方全文并保存原工具记录`openai-caisi-web.json`，读Agent安全段及限定测试条件。原先看似不可利用的传统软件漏洞，与Agent hijacking结合形成跨会话权限风险的实际反例，是新增公开证据而非合作机构名；拟2+2+2=6，因安全变化读受影响核心。只采用厂商报告的局部反例，不采用未披露总体成功率/实现已修复保证。

必要反侧：厂商所述约50% PoC没有公开样本/attempt分母、精确漏洞/实现版本、完整攻击或修补trace；不能当总体风险率。其所链接NIST为2025年1月AgentDojo方法与2024年12月o1评估，并非此次July ChatGPT Agent漏洞的独立复现。UK测试部分拥有非公开信息和额外访问；不把特权评估当普通用户风险。上述原文位置web L39–74，安全声明的权限仅厂商公开事实；未运行攻击或复现。

Books建议No Change（须root实际核，不自授）：`PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)1245–1297实际拥有untrusted输入与effect-time executor权限，764–812拥有run/attempt与集成条件不可合并成安全率，2989–3012拥有integration、credential、destination、fixture与effect的case身份。相邻[Ch71](../../../../../books/part-06-ai-infrastructure/71-multi-tenant.md)、[Ch73](../../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)负责租户隔离与release，不让安全probe授release；Ch73实际1–55和Ch78实际167–197已读，Ch71尚待实际相关段。该Blog没有公开具体新防御机制，局部反例由现正文承载，建议不加自然段，只报告版本事实；请root核准入/6分与实际owner覆盖。

## arXiv有限题摘与独立校准范围

本日主题API实际200、total123/123，覆盖12分类+语言模型/Transformer/MoE/Agent/Diffusion/GPU/VLM/World Model，submitted Sep11 18Z→Sep12 18Z只发现线索。实际读全123标题后收窄69可能相关完整题摘，`scoped-abstracts.json`保留API当前精确version，非全部2025v1；不把未回v1的当前摘要冒充历史事件证据。其余54明确医学/农业/科学等领域应用标题不扩为全文队列；没有声称全月或全学科覆盖。advanced恢复表单，官方说明announcement排序只有年/月，仍不能授逐日公开。

首批潜力建议实际核：09782跨query-model attention预测质量/费用、09790 grounded环境反馈在连续复杂动力学退化、09864 latency+token共同选择test-time方法、10140 VQBridge缓解codebook梯度/陈旧更新、10312空间cluster feature-cache、10377 neuron级expert重建、10396 diffusion inpainting引导RL非零组梯度、10439 local SGD outer optimizer理论边界。未评分、未落窗，后续必要v1与方法不能由本日摘要替代。

安全/反证不普通排除：09893 SART precision boundary安全，09942 SmartCoder安全reward，09955 token merge的privacy声明，09970 firmware validation/patch，10018 GAMA匿名边界，10260 reward hacking，10278 VLM伪造检测，10298 Lipschitz/对抗鲁棒，14256隐性广告检测，10594 SME安全，10401 causal归因。均仅潜力/日期保留，未取得精确威胁模型/实现，不授安全或因果保证。代表关闭及其余身份理由在SCREEN；请root首批校准，尤其LoRA+ReFT局部对照、ASR负面、Longformer局部反证、code energy硬件相反结果不因规模或负面性质关闭。

Ch71实际1–75已补读：namespace不等于租户边界，credentials/network/runtime与evidence平面须共同隔离，与Ch72 executor授权相邻。不提新增自然段；单项No Change仍待root独核。13作者本次研究ready，正式发布1家族、arXiv59潜力日期保留、10题摘关闭建议与54标题范围外，均不授DAY。技术上13API恢复已触发12受影响API的窄重开需求，12原错误/有效题摘不推倒、不迁移本日候选。每完成一日交接，不等五日。
