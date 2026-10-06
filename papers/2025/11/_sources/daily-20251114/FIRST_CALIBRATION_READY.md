# 11/14 首批具体增量校准 ready

作者Planck；fresh本日BJT [Nov13 09:00,Nov14 09:00)，未加载13候选池。以下官方核心已实际读，先交root准入与代表性排除校准，未授Evidence/Books/日级通过。原入口raw-web-00/01，实际query raw-web-02/04，核心raw-web-03/04/05；不使用搜索转载作机制证据。

2026-10-04校准返回已实际读取[FIRST_INDEPENDENT_REVIEW](./FIRST_INDEPENDENT_REVIEW.md)：四方向准入通过；SIMA2/cyber/sparse的事件日期通过，仅该层权限。两项代表性排除通过。API日期按下面真实RSS字段纠正，不由官网日期授落窗。

## 拟准入

| 原源 / 原字段 | 原有约束或判断 → 实际增量 → 重考选择 | 评分 / 必要反侧 |
| --- | --- | --- |
| [SIMA 2](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)；官方HTML article:published_time及JSON-LD datePublished=`2025-11-13T18:55:00+00:00`，BJT14 02:55落窗。raw-sima2.html与.request.json；dateModified=`2026-07-06T10:48:07.011700+00:00`保留不当首次公开 | human demo驱动跨游戏agent → Gemini给task/reward后由自玩experience bank训练后续代agent，包括生成世界 → 是否把环境生成、teacher评价和policy自改进组成另一训练分支；不仅“加入Gemini变强” | 2+2+2=6，标准。report需核teacher/reward、筛选、代际对照与budget；新评价集合不能与SIMA1旧论文数字拼接，Genie demos不等广泛泛化；short context换低latency、goal verification/精细keyboard action仍困难。当前修改时间不能证明全篇保持原样，必要精确technical report待核 |
| [Anthropic AI-orchestrated cyber campaign](https://www.anthropic.com/news/disrupting-AI-espionage)；官方meta/JSON-LD datePublished=`2025-11-13T16:00:00.000Z`，BJT14 00:00落窗。raw-anthropic-cyber.html与.request.json；dateModified=`2026-09-10T18:24:07.000Z` | 单个看似正当的请求可通过model安全判断 → 官方case描述跨session orchestrator保存状态、拆分任务令子agent缺全局恶意上下文 → 单call过滤是否足以控制多步组合effect；只采用被报告的失效路径，不采用普遍自主能力 | 2+2+2=6；安全/纠错必要深入。80–90%是厂商战术工作估计，非成功率或无人完成比例；仅Claude可见性、虚假credentials/public data反侧。当前网页已记Nov14速度纠错（不是千次/秒），必须采用纠正限制；两官方PDF路径均是带Nov17 attribution changelog的14页新版，不能冒称Nov13原版。归属原事件与后来纠错权限分开；历史原版必要点待有限恢复 |
| [GPT-5.1 for developers](https://openai.com/index/gpt-5-1-for-developers/)；官网Nov13 2025日粒度；本日raw-openai-rss.xml实际pubDate=`Thu, 13 Nov 2025 00:00:00 GMT`，BJT13 08:00窗外。direct GET403，仅记录失败 | 原reasoning effort最小档仍有thinking、prompt cache短保留 → API新增none/default none与可选24h retention、patch/shell output callback接口 → 是否用显式runtime knobs和执行者反馈而非统一推理预算 | 2+2+1=5，局部评分可沿用；准入通过但不正面收入14。RSS字段按其值窗外，午夜是否只是日粒度编码未获官方说明，不称未有时刻，也不虚构归一化/改发时刻。官网日期不能覆盖此限制。all500 SWE-bench同JSON patch harness不证明新freeform工具因果；AIME/Telecom/Retail退步与未披露cache/offload算法保留。 |

## 代表性排除

1. Google Research 2025官方dated目录Nov13《Separating natural forests from other tree cover with AI for deforestation-free supply chains》：标题已明确森林/供应链领域应用；当前只关闭此发现标题的项目范围，未称全文无学术价值，未展开模型全文。无标题所示主线机制/纠错信号；不通过Evaluation/RAG owner重新引入暂缓AI for Science/领域路线。原raw-web-04，日期不是关闭必要事实。
2. 官方ChatGPT release notes Nov13 Group chats核心实际读（raw-web-02官方返回）：共享计划/对话试点与区域上线，当前未披露模型、训练、推理或跨agent状态新机制；仅多人UI场景不足准入，不用平台术语强造合同差额。只关闭公开功能说明，不声称未公开实现不存在新机制。

## 当前待办与停点

上述准入/排除已独立校准，不重复送；继续SIMA技术稿版本与必要机制、cyber纠错采用边界及具体owner。API本日不采用，定点重开只接受官方说明RSS精度/真实首次公开时刻，不扩论坛或以网站日粒度补造本窗归属。校准不是Books配额，不因owner未有产品名申请写书。

继续无关14源分页、窄主题arXiv与官方相关标题有界补检；不为等首批或全日池停工。不扫Weekly，不扩其他月份，Books直接写入0。

证据阶段收窄：首批表中的cyber“跨session orchestrator保存状态”来自当前Nov17修改版PDF，不再作为Nov13精确原件已证命题。官方Blog本身支持的是看似正当子任务隐藏总体恶意目的与返回人工决策点；本日只采用这个更小的失效路径。SIMA当前technical report取得后实际封面/制作日期为Dec5，也不再当Nov13原技术稿。两项的必要限定与owner处置见 [BLOG_EVIDENCE_OWNER_READY](BLOG_EVIDENCE_OWNER_READY.md)。
