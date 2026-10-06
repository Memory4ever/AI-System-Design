# 2025-10-01 首批独立准入复核

复核者：Codex 独立复核会话（非 root 作者；继承当前模型，未切换模型）。
记录时间：2026-10-05T04:30:22+08:00，本轮实际原文打开与结构化字段复查后记录。
窗口：`[2025-09-30T09:00:00+08:00,2025-10-01T09:00:00+08:00)`。
对象：[FIRST_CALIBRATION.md](FIRST_CALIBRATION.md) 当前首批准入包。

**结论：首批准入校准通过，作者文本两处返修尚未通过；不授 DAY、最终 Evidence 或 Books 验收。**
本轮只写本文件，不修改作者材料、日报、index、state 或 Books。作者的“实际已读”标签不作为独立核验。

## 1. 可执行返修

1. **R1：删除 Russian-speaking 的“离线模型”限定，补齐必要反侧。** 作者文件第25行的“离线模型未执行工具”没有原文支持。[原页](https://openai.com/index/disrupting-malicious-uses-of-ai-russian-speaking-malware-tooling/) Completions L36 只说明模型没有执行攻击者工具/工作流、平台外活动不能独立验证，不说明模型离线部署。改成“本案模型未执行攻击者工具或工作流；平台外活动无法独立验证”。同步保留 Behavior L30 的“可能被组装”、L33 的跨会话持续迭代，以及 Impact L48 的“未发现超出多种公开资源的新能力/方向，直接 exploit/keylogger 请求被拒”。不能写成已验证组装成功、代码正确、攻击成功、净伤害为零或普遍无能力提升。作者尚未补读的 Impact 是可执行待办，不是外部受阻；本轮已实际独立读到 L48，未变化命题可复用本次复核。
2. **R2：修正 Anthropic 数组邻接日期，不扩大零命中断言。** 作者文件第31行的“邻接 Sep25/Oct3”不能由存档 [anthropic.html](anthropic.html) 复现。实际结构化解码可复现174个带 `publishedOn` 对象、按 slug/url/title 去重172项、本窗0项；窗前最近项是 `Anthropic Economic Index report: Uneven geographic and enterprise AI adoption`，原字段 `2025-09-15T20:33:00.000Z`，BJT `2025-09-16T04:33:00+08:00`；窗后最近项是 `Building AI for cyber defenders`，原字段 `2025-10-03T18:31:00.000Z`，BJT `2025-10-04T02:31:00+08:00`。请写明原字段与换算，或删去错误邻接日期；只能称“本次返回 Research 数组无落窗项”，不称全站/全部历史子入口无事件。此次只检查日期元数据，不重开这些窗外文章正文。

另外，作者第13行“旧判断”宜明确是被本案检验的代理指标假设，而非未经定位的 Books 既有错误。具体纠错对象是 OpenAI 自己2024年的 Stop News 分级；本轮没有证明本项目曾采用该分级或“一次拒答即安全”的结论。此限定在最终 Evidence/Books 表述时保持即可，不要求现在改书。

## 2. 实际通过的日期、家族与最小贡献

- **日期通过：** 独立解析 [openai.xml](openai.xml) 的 XML `item` 与 RFC 日期字段，确有1245项；七案例各自原 `pubDate` 都是 `Wed, 01 Oct 2025 00:00:00 GMT`，换算 `2025-10-01T08:00:00+08:00`，在本窗内。七原 HTML 各自页首显示 October 1, 2025。RSS 支持官方发布记录的时刻，不证明互联网上首次公开的无遗漏调查。
- **家族通过：** 七个原 HTML 的开头均明确归属 October 2025 报告，并各自链接相同 PDF URL：`https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf`。本包计1个报告家族，七案例不是七篇新研究，跨章节关联不增加分母。本轮未打开 PDF，不核验作者所记的 PDF 请求字节数/失败经过。
- **Stop News 最小贡献通过：** 原 Impact L49-L50 明确把2024年 Category3 的主要证据追溯至疑似英国网站“信息合作”，后续研究使这些合作不再能支持原判断，当前改评 Category2。可以采用“OpenAI 根据后续证据修正自身影响分级”；不能写成“所有传播均无影响”或把第三方调查真实性称为本轮独立验证。
- **Russian-speaking 最小贡献通过：** 原 Behavior L30-L33 支持直接恶意请求遭拒、仍获得可双用途的构件、同代码跨会话迭代；构件在平台外恶意组装是作者的可能性判断，Completions/Impact 保留执行与新增能力的反侧。它提供本案观测边界，不提供通用检测算法、安全绕过成功率或已验证的攻击能力跃迁。
- **5分与审阅投入通过：** 保留 `Design Delta2 + System Reach1 + Durability2 =5`，对象是本案局部纠错与组合风险观测，不是借用的成熟治理原则。2分对应需要重审的局部评价边界，1分限于具体滥用工作流，2分对应可复用的证据适用约束；不按七案例/机构声誉/能映射多个章节加分，不为达深入档提高总分。按研究合同，实际纠错与安全信号已独立触发受影响核心深入审阅，5分不是只读摘要的理由。
- **Owner 只作路由：** ROADMAP 的 `PLATFORM-EVALUATION-SYSTEM`（Ch66）可承载影响指标有效性，`PLATFORM-SECURITY`（Ch72）可承载组合风险与安全证据边界；没有据此新增 owner、宣告知识差额或通过 Books。“真实触达与组合风险需分别核验”是复核者对案例的系统推断，不冒充原报告的新机制。

## 3. 独立实际打开的 HTML 核心与反侧

以下位置为本轮 web 返回的原 HTML 行号，定位同时绑定小节名；不是作者记录的读取回执。七页均实际打开，未遍历图片、全部附件、政治事件历史或全文 PDF。

| 原始案例 | 本轮实际读到的相关位置 | 通过的限定范围 |
| --- | --- | --- |
| [Stop News](https://openai.com/index/disrupting-malicious-uses-of-ai-stop-news-2025/) | Actor/Behavior L27-L39；Completions L41-L44；Impact L47-L50 | 当前传播指标与分级纠错均有原文；外部视频模型身份未独立确认。改分来自对旧证据的重解释，不等于模型防护导致真实影响下降。 |
| [Russian-speaking](https://openai.com/index/disrupting-malicious-uses-of-ai-russian-speaking-malware-tooling/) | Actor/Behavior L26-L33；Completions L36-L38；Impact L48 | 跨会话构件迭代与直接拒答共存；平台外组装、执行及结果不授验证；未发现新增能力的判断限于本次观测。未采用 ATT&CK 映射表作额外证据。 |
| [Nine-emdash Line](https://openai.com/index/disrupting-malicious-uses-of-ai-nine-emdash-line/) | Actor L26-L28；Behavior L35-L38；Impact L60-L62 | 便利性不等新能力，外观相似无技术关联；多平台生成与低互动共存，部分互动来自网络自身，封禁不等运营终止。 |
| [Scam operations](https://openai.com/index/disrupting-malicious-uses-of-ai-scam-operations/) | 核心 L26-L31、L35-L49、L52-L54 | 既有诈骗流程的扩量/效率和封禁后持续活动可作为背景；反诈骗使用频率估计不证明受害损失净下降，不给总体检测率。 |
| [PRC-linked abuse](https://openai.com/index/disrupting-malicious-uses-of-ai-prc-linked-abuse/) | 范围 L30-L32；工具规划与部署反侧 L34-L39；profiling L42-L44 | 选择性被封禁样本、个体使用与规划请求不等机构部署或实际监控；不把政策态度当模型机制贡献。 |
| [Korean-language](https://openai.com/index/disrupting-malicious-uses-of-ai-korean-language-malware-support/) | Actor L27-L28；Behavior L31-L33；Completions L36-L46；Impact L49 | 窄任务账户/双用途、国家归因不可独立确认、未发现对应恶意二进制由模型生成及超公开资源的新能力，均保留。 |
| [Phishing/scripting](https://openai.com/index/disrupting-malicious-uses-of-ai-phishing-and-scripting-support/) | Actor/Behavior L27-L39；Completions L42-L49；Impact L52-L53 | 本轮补打开后读到末尾反侧；效率/本地化与粗糙实现共存，DeepSeek自动化及最终模型未确认，不采用通用攻击能力提升结论。 |

对安全同家族七案例的上述限定没有发现另一项必须独立计家族/额外评分的明确增量。不据此证明附件无其他贡献。

## 4. 代表性排除、检查数与停止边界

本轮抽查 OpenAI 的4个具名窗外事件记录，另复现 Anthropic 返回数组的日期范围；不是所有来源全部排除项的复核。

| 样本/理由层 | 实际核验 | 处置 |
| --- | --- | --- |
| Sora2、Launching Sora responsibly、Sora2 System Card：日期排除层，3项 | XML 各自原字段 `Tue, 30 Sep 2025 00:00:00 GMT`，均换算 BJT09/30 08:00，比起点早一小时 | 本窗排除成立；没有读 card 或发布正文，没有通过其安全结论，也没有授真实归属日完成。 |
| Samsung/SK Stargate：日期与商业发布层，1项 | XML 原字段 `Wed, 01 Oct 2025 03:00:00 GMT`，BJT10/01 11:00；实际打开 [原 HTML](https://openai.com/index/samsung-and-sk-join-stargate/) L22-L29、L34 | 超出终点两小时；原文是供应、数据中心与部署合作计划，不披露新模型/训练/推理机制、可比质量资源取舍或评价反证。不能因 DRAM/数据中心词自动准入；但不把商业发布一概视为不可能贡献。停止于判断所需核心，不扩扫商业目录。 |
| Anthropic：来源返回范围层 | 解码存档 HTML 的 Next Flight JSON，对 `publishedOn` 做时区感知比较，复现174/172及零落窗；只打印边界项 | 返回数组内零项成立，邻接日期须按 R2 修正。未验证独立历史归档、全部子站或当前页面之外的覆盖。 |

本轮未发现需要把“仅主题相关即准入”或“所有负面结果均排除”作为共同错误重开整池的依据。R1 只影响 Russian 证据措辞及依赖结论；R2 只影响 Anthropic 此返回数组边界记录。若后续发现同类错误再定点扩查，不预先声称全量排除已验证。

## 5. 未授予范围与交接

- 首批报告家族的上述日期/准入与必要原文反侧可复用；R1/R2 作者文本尚未落实，复核者没有代作者修稿，也没有授“问题已解决”。
- 本轮未验证 PDF 全文/截图、第三方 VIGINUM/Trellix 等调查原件、模型实现或攻击代码，未做独立复现。不采用这些未读附件的扩展主张，因而不为当前最小命题追读全部附件。
- 其余每日来源、Google/Meta 故障后的恢复、全部14来源的查询/分页/停止点、arXiv主题检索与题摘筛选仍未交付本轮验收；当前全日候选分母未冻结。NATIVE 下载回执只证明相应请求结果，不授覆盖/零命中。
- 未检查具体 Books 正文与相邻交接，也未检查最终日报六部分、最终机器校验和实际书稿变更。后续由 root 完成修稿与 Evidence/Books/14source 包后，再单独任务复核，不由本包授 DAY。
- 不读其他日期整池，不stage、commit、push，不修复无关既有工作区变化。

## 6. 文件检查

本轮仅新增本复核文件，保持未暂存；本地引用限定 FIRST_CALIBRATION、openai.xml、anthropic.html，3个本地链接均存在。写后实际通读 Markdown 表格/链接；限定 `git diff --check` 无诊断，对未跟踪新文件另以 `git diff --no-index --check` 对空文件检查亦无空白诊断（差异存在返回1，不当测试失败）。未执行尚未交付的日报 V3 校验。这些只验证本文件可读性与变更纪律，不替代上述语义复核或日报验收。
