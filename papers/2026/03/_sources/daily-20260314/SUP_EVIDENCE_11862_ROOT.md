# 11862 ReadSecBench：必要原证与已有覆盖提案

root 准备，待非准备者独立审阅。精确 v1 题摘、署名、版本与本日 arXiv 事件门复用已通过的第六包核验；官方 HTML 本轮 GET 200，222598 bytes，UTC 2026-10-10T01:09:16.629418Z，原件及抓取结果保留。实际阅读 §III threat model、§IV-A–F 的设计、指标、跨环境及防御比较、§V limitations、Appendix D；不核攻击 payload、图像像素、旧版本或全部引用。

## 贡献与评价边界

文档被解释成高权限执行指令的基本风险不是新机制。本稿增量是安装 README 工作负载下，区分提出泄漏函数、执行命令和实际外传，并以良性文件误报检验过滤器的有限证据：拟 Design Delta 2 + System Reach 2 + Durability 2 = 6。安全边界只做这些必要验证，不提高为通用不可防御定理。

500 个 README，五种语言各 100；文中每次抽 40%、三次随机种子与 Table II 每 cell 七次试验不是同一统计人口。主要环境为 Claude Computer Use / Sonnet 3.7；报告的 Linux / EPYC 7742 / A100 80GB 是主机配置，不冒充闭源 API 模型的推理硬件。precision、完整长度、并发、线上 SLO、复测置信区间未披露。ASR 以正确私有文件实际发送到研究团队接收端为成功，尝试、错误文件和占位内容不算。未把摘要最大值推广到所有代理或全部攻击配置。

Appendix D 的 LangChain/LangGraph 比较每模型抽 150，调用可能泄漏的函数即算 semantic compliance；即使环境不能实际传输也算，因此不能与主要实验 end-to-end ASR 合并。跨代理的 OpenDevin 被 Docker 网络限制挡住外传，证明所测环境中的执行层限制有实际意义，不由作者的能力差异解释推导权限隔离无用。

Table V 是文档分类而不是防御后端到端外传评测；PromptInjection 对 benign/injected/link 都标记 .3，Anonymize 的 benign .9 等说明高检出可能付出高误报。GPT-4o 为 benign 0 / injected .9 / link .3，只支持受测输入及最小 yes/no 提示。表中样本人口和重复误差不完整，不补为生产错误率；更强防御、实际授权、网络策略、专业安全审查未被穷尽。15 名参与者各三份 README 的自然清晰度阅读不是专门安全审计，0% 发现不能称人类无法检测。artifact 链接仍待接受确认，公开 benchmark/实现可复现性没有独立验证。

## 具体已有覆盖，不新增 Books

实际阅读 PLATFORM-SECURITY / Ch72 下列连续局部及 Ch71、Ch73 入口：

- Prompt Injection / Tool Boundary（1307–1337）：不可信资料不能改变 authorization；typed proposal → policy → least-privileged executor → audit，读外部资料、敏感资源及 egress 三者组合需实际限制而非只依赖模型拒绝。
- Containment（865–930）：分别核 untrusted read、proposal、authorization、executor commit；尝试不等实际 effect，并同时检查 security、utility 与效率。
- authenticated provenance（2251–2269）：模型指令层级不替代平台授权；过滤需保留安全与可用性代价。
- Approval Summary（3131–3150）：审批基于可信实际 effect、独立身份与通道，而非代理自述；保留误报和 review capacity 成本。

这些不是主题相近，而是已拥有本稿能够支持的状态、控制权、效果判据和误报取舍。新 README 实验没有改变这些长期设计契约，`No Change — Existing Coverage`，Books 0；实例、测量人口及限制写入报告。不会把‘所有防御均无效’或尚未实现的怀疑式推理写入书稿。mar13_admission_review实际必要原证、评分与完整指定正文/相邻入口独核通过，见 `SUP_INDEPENDENT_SIXTH.md`；四受测 backend 不能称四个独立厂商/家族，未公开 GPT-oss identifier 不认证公开精确 revision。本记录不授 DAY。
