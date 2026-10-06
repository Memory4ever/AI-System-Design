# Daily Research — 2025-09-13

**规范：** V3
**窗口：** 2025-09-12T09:00:00+08:00 ～ 2025-09-13T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-10-06T13:34:26+08:00

## 1. 结论

本日作者拟入选1个确定落窗家族：OpenAI CAISI/AISI安全更新，传统软件漏洞与Agent hijacking组合使原本看似不可利用的漏洞进入实际权限风险路径。6分，安全相关必要核心已深入；Books建议现有覆盖，尚待root首批/owner独核，不自授采用或DAY。59个arXiv相关潜力日期隔离，未计正式候选；123条只是提交主题查询线索，实际读69完整题摘、10普通关闭建议，其余54明确领域应用标题范围关闭。没有把123或59转成全文队列。

当前Books正文增量0，官方PoC没有公开足以复现的版本、trace、分母或patch，不能授总体安全率/已验证修复。VaultGemma有sequence级DP取舍潜力，但公开时间只相交，仍不采用本日日期。作者研究已交接，root校准与最终DAY未完成。

## 2. 来源覆盖

本日实际独立请求与有限停止见[原始目录](../_sources/daily-20250913/)，`transport.json`和针对性记录保留执行时间/URL/超时18秒/12MB上限；不继承其他日报结论。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS原pubDate本窗Sep12 12:00GMT安全更新；直接正文403后web官方全文真实恢复并保留工具原记录 | 已检查 | 1家族必要核心已读，独立准入/Books待root；RSS不是全站无遗漏 |
| SRC-ANTHROPIC | 本日Research SSR字符串实际解码，publication原日期Sep5→Sep15T09Z/T20:33Z跨窗 | 已检查 | publication目录切片，不遍历库存全文或已删除记录 |
| SRC-GOOGLE-AI | DeepMind page5 Nov2025→Jul2025，相关原文Sep25/22/17；Research月1→2/2共13条Sep30→Sep9，Vault核心本日完整读 | 受阻 | VaultSep12无时区/时刻，尚不支持完全落窗；月目录不授全部pubs覆盖，科学应用暂缓 |
| SRC-META-AI | Blog3主序Oct24→Aug27/14且旧pin分开；错误publications页45 bytes后实际正确results publication page5→6（275489/275691 bytes），末Sep15→首Sep8 | 已检查 | 错误route不是0；有限窗口前缘处理，不授全历史 |
| SRC-QWEN | 新官网research配置57428 bytes，10个9月对象原ISO；Next Sep10T20Z，ASR Sep8T06:38Z，余Sep21/22/24 | 已检查 | 不相交本窗；不以retrieval首页代历史或复制11采用 |
| SRC-DEEPSEEK | 官网+updates，本日实际Sep29/22→Aug21 | 已检查 | 仅官方公开更新切片 |
| SRC-MOONSHOT | 本日完整可见平台Blog Sep16→Sep5→Aug22 | 已检查 | 无具体本窗repo release触发，不扫普通PR |
| SRC-TENCENT-HUNYUAN | 首查Research shell；实际正确host POST pageNum1/pageSize100/renderType0，9=total9 | 受阻 | 全是2026记录，不能授2025历史；需历史全部列表/具体本窗原文 |
| SRC-ZAI | Research与notes Sep30→Aug11；真实page2→3重复18项，2026Aug26→2025Dec7、无更多 | 受阻 | 已执行窄分页仍未跨9月，Research历史不支持0事件 |
| SRC-BYTEDANCE-SEED | 本日type2/year2025/page0/count20/desc 15/49/has_more，非pin Oct22T16Z→Aug20T16Z→Jul；type1 total94无sub_article_list | 受阻 | Blog非pin跨窗实际停止page0，paper响应不完整需历史列表 |
| SRC-BAIDU-ERNIE | Blog实际1→2/2；PLAS原datePublished/Modified Sep12T00Z→08BJT，窗起点前，原正文本日取得 | 已检查 | 不以date-only迁入13或继承前日贡献判断 |
| SRC-XIAOMI-MIMO | 本日8Paper/15Blog标题及home chunk实际读，More仅切初8/余7无新fetch；Paper Sep19→Jun4 | 受阻 | 历史Blog日期/条目未恢复；不是未执行More分页 |
| SRC-MINIMAX | 本日EN12/CN13、英文page2派生文本同首页；Agent techblog及llms.txt实际当前单项2026 | 受阻 | CN Jan15旧锚不证明中间无事件，历史分页/Agent列表仍缺 |
| SRC-ARXIV | 12分类+language model/Transformer/MoE/Agent/Diffusion/GPU/VLM/World Model submitted Sep11 18Z→Sep12 18Z；两个API均123/123；123标题→69完整题摘。advanced实际只恢复表单及announcement年/月说明；未重复全月扫描 | 受阻 | 主题查询真实处理但submitted≠first-public；59潜力精确日期和部分当前v2/v3/v4历史v1未核，不能授完整Coverage/无遗漏 |

未扫描每周组。表外NIST由官方安全候选链接触发必要身份/反侧检查，非全站扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Working with US CAISI and UK AISI to build more secure AI systems](https://openai.com/index/us-caisi-uk-aisi-ai-update/) | 2025-09-12T20:00:00+08:00 | 传统漏洞原看似不可利用→Agent hijacking串联局部反例→安全验收需跨软件/模型控制边界；2+2+2=6 | 深入完成 | 暂缓：建议`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)已有覆盖，root实际owner/准入独核未完成，不自授采用 |

其他59题摘潜力未确定落窗，不计候选或评分；十关闭建议及分层代表见[筛选](../_sources/daily-20250913/SCREEN.md)。

## 4. 证据与知识整合

### [Working with US CAISI and UK AISI to build more secure AI systems](https://openai.com/index/us-caisi-uk-aisi-ai-update/)

采用身份为Sep12官方发布，时间由本日RSS原GMT支持；当前官方完整核心web L39–74真实读到，HTTP403不冒充正文已得，[原工具记录](../_sources/daily-20250913/openai-caisi-web.json)与[交接](../_sources/daily-20250913/HANDOFF.md)保留证据位置。厂商披露传统漏洞与Agent劫持组合的局部失败路径；约50% PoC没有公开attempt/样本分母、精确漏洞、完整trace/实现或修补版本，不作总体率或修复实现审计。关联NIST是Jan2025 AgentDojo及Dec2024 o1评价，不是此次July ChatGPT Agent漏洞的独立复现；特权访问测试与普通用户条件分开。

作者实际读Ch72 1245–1297的untrusted输入/effect-time executor控制，764–812的run/attempt/集成评价条件，2989–3012的connector/credential/destination/fixture/effect身份；Ch71 1–75、Ch73 1–55与Ch78 167–197相关交接已读。建议已有覆盖、无拟增自然段，因为新材料的长期安全边界已由这些实际论点承载，局部厂商事实留在报告。该建议未独核，当前Books暂缓；root核相同源/owner后才可改已有覆盖。不把厂商合作声明当生产保证，未复现或执行攻击。

Vault本日核心支持1024-token packed sequence级DP、Poisson采样与fixed-batch处理，不能授user/doc DP；尚缺本窗公开日期，不采用。arXiv69完整当前题摘不是精确历史v1审阅，已有安全/设计反证潜力不普通排除，日期恢复才定点核相应版本/必要命题。

## 5. 缺口与下一步

作者研究ready；root首批准入、Books实际owner独核与最终DAY仍可执行，保持进行中。

- 本节唯一候选：需要root实际官方原文/日期、6分准入及Ch72/71/73邻接No Change核验；未公开漏洞细节/patch仅约束可采用范围，不请求无关实现或授已修复保证。
- arXiv59潜力：`scoped-abstracts.json`除SCREEN十关闭外的精确身份；需要官方公告/作者首次正文公开支持完全落窗区间，及必要历史v1。submitted与month不授权。当前隔离，不作正面Evidence/Books、零事件或无遗漏；只重开日期成立的身份，不将123全文入队。
- [VaultGemma](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/)缺公开时区/时刻或完全落窗区间，Sep12日期仅相交。原公开元数据/artifact记录回归时重开该家族，不凭DataCite/仓库创建日迁移。
- Hunyuan、Z.ai Research、Seed paper、MiMo dated历史Blog、MiniMax历史Agent/分页：§2已实际有限尝试，原历史列表/具体原文回归后只核本窗主题；当前隔离，不授无遗漏或零事件。

窗外PLAS原ISO在Sep12 08BJT、Qwen Next在11日04BJT，不属于本窗，不扩另日报。

## 6. 复核

复核者：root（待独立检查）；结论：未通过（首批/Books/DAY尚未实际授予）。需核1正式拟入选、安全潜力未普通关闭、10题摘关闭与54题义范围关闭的分层样本，以及真实来源停止和日期隔离；不称全量附件独核。

结构/引用/限定diff检查待执行，不替代语义复核。
