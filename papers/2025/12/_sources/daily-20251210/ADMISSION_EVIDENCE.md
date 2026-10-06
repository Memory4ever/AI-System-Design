# 12/10 准入、必要证据与 Books 处置

2026-10-02T19:31:00+08:00局部同步：root已在Ch66 Context→RAG之间实际写入904/906两段，绑定`SF-2025-GOOGLE-FACTS`。作者本轮重读两段及898–918邻接，四来源分账/统一工具部分控制、不同题集非因果增益、成本与固定基线均在实际正文；下文旧“待协调”是写入前记录，不代表当前状态。6分不改，因已确认长期知识缺口深入必要协议/反证及owner比较，审阅深度同步深入完成，不增加榜单/PDF命题。Popper的POST及日级验收以其ROOT_ADMISSION_REVIEW为准，作者不授通过。仅FACTS一项整合，SGLang仍版本背景仅报告。

2026-10-02T18:14:25+08:00，作者Plato；窗口09日09:00～10日09:00北京。

## 拟入选与准入校准请求

1. [FACTS官方博客](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)：旧事实性总分无法区分知识来源/工具条件 → 原文并列参数知识、统一搜索工具、图像与给定文本四分支 → 需要按来源切片而非单一总分验收。请root校准这条评价增量，不以新题库名或排名准入。官方原页HTTP元字段 `article:published_time` 与 BlogPosting `datePublished` 均为 `2025-12-09T11:29:03.922000+00:00`，换算19:29:03.922北京，完全落窗；dateModified为2026/07/07，不用修改时间替代发布。
2. [SGLang14691](https://github.com/sgl-project/sglang/issues/14691)：组件各自有FP8选项不代表组合路径可执行 → 具体NSA/FlashMLA/EAGLE/PD配置在KV写入断言拒绝 → 部署必须核真实mode/backend/layout路径，而非按功能参数名拼接。官方API `created_at=2025-12-09T03:22:07Z`，11:22:07北京，落窗。报告者称bug不是已确认错误，不采用当前closed状态证明修复。

代表性普通负侧：[OpenAI AAIF](https://openai.com/index/agentic-ai-foundation/)完整核心说明是中立治理、捐赠既有AGENTS.md/MCP/goose，没有此次新协议语义或执行机制；贡献前关闭，未授日标签精确归属。课程、人事与商业合作标题明确范围外，不读无关全文。

## FACTS必要阅读与限制

已读官方博客核心四任务定义、统一search工具、public/private与均值解释。拟采用只限评价对象分账及工具条件控制；不采用厂商冠军排名，不从均值认证单一部署可靠性。所链[技术PDF](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)当前18页，首行日期 **2025-12-11**；实际读首题摘、§2、§3方法和validation，是后续技术背景，不能冒充12/09精确稿。尤其不把PDF rubric、F1、threshold和模型表当本窗首发既已披露。若采用这些细节须恢复原始版本及相应事件归属。

博客层的评价模型/私有题与原始调用日志不足以独立复现，各硬件、precision、长度、batch、concurrency、SLO为Not Disclosed（本次不作性能主张）；模型是其API版本，不认为名称锁定backend。标准审阅限定于实际公开协议说明，可信度不由官网声望授予。

## SGLang正确性必要源码

官方GitHub API contents，ref固定`v0.5.6`：
- [memory_pool.py](https://github.com/sgl-project/sglang/blob/v0.5.6/python/sglang/srt/mem_cache/memory_pool.py) 1411–1419：NSA且float8存储需要override layout；1499–1509通用`set_kv_buffer`拒绝NSA+FP8；1520–1526专用`set_mla_kv_buffer`做quantize/存储布局。
- [flashmla_backend.py](https://github.com/sgl-project/sglang/blob/v0.5.6/python/sglang/srt/layers/attention/flashmla_backend.py) 432–443：不同extend mode走不同路径，其中通用cache setter可触达上述guard。报告日志行号410与tag443不完全一致，未取到报告者容器commit，不能保证精确构建相同。

原issue实际完整核心：DeepSeek-V3.2，SGLang0.5.6、H20-3e、CUDA12.9/driver570.133.20、torch2.9.1+cu129；tp/dp/ep16、2节点、EAGLE、decode PD、fp8_e4m3、FlashMLA。max-running/context配置不是实际请求batch、并发、SLO或benchmark结果；这些及质量对照Not Disclosed。未运行复现，无已核修复/无“移除assert即可支持”建议。当前issue正文可编辑，API updated_at2026/02/20不当新事件落窗或原正文冻结证明。

## Books实际对读与提案

FACTS owner `PLATFORM-EVALUATION-SYSTEM`，Ch66 `books/part-06-ai-infrastructure/66-evaluation-system.md`。已读14–47核心、89–105 EvalSpec、199–205 adapter条件、898–900 closed/open/attacked-open正文。已有段落承载条件性分数、切片、knowledge/use/harness分账；后者没有测retrieval/tools，不能说FACTS所有分支已覆盖。相邻Ch65 14–30是资源公平，Ch67 14–18是趋势测量而非质量标准，不转移owner。

局部提案目标Ch66 Context Evaluation段后（约900行），不覆盖既有三条件因果限定：

> 来源维度也可以用并列任务测量：分别冻结给定文本、参数知识、外部搜索和图像条件，保留每一分支的结果，而不让跨任务平均值替代诊断。统一搜索工具可减少各模型自带检索设置的混杂，却仍不能保证message adapter、调用预算和scorer相同；不同题集的分数差也不是同一道题中“检索带来的因果增益”。这种切片增加工具/图像运行、私有题维护与judge核验成本，简单单一用途可以保留原固定基准，跨来源部署则须显式补分支并保留独立holdout。

此为作者整合提案，待root准入/必要源与owner核验及共享owner协调，**未写入Books**；不以PDF后续细节支撑本窗提案。

SGLang owner `INFER-SGLANG` Ch51。实际读207–225 live-schema差集/高风险fail-closed；相邻Ch50 169–175有attention backend/cache layout identity，Ch52 89–92有兼容identity与拒绝复用。一般组合兼容原则已有具体正文；本次仅补版本化报告背景，没有已证实新修复或可推广机制，因此“仅报告”（同时指出原则已有覆盖），不制造书稿变更。目标tag不等报告者commit的缺口隔离，不支持bug定论/production保证。
