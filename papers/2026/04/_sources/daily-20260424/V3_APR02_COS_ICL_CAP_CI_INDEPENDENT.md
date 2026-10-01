# Apr24 四项有限非作者采用复核

复核者：apr02；检查时间：2026-09-27T21:03:44+08:00。实际重读当前 AGENTS、Research/Report 合同、统一 Prompt、Daily/arXiv 来源范围及 ROADMAP。仅核作者指定四家族的必要 exact-v1 方法、主要评价/反证和当前实际 owner；未核整日日期/来源 Gate，未遍历附件，未修改 Books 或作者报告。拟评分仍须作者确认当窗身份。

## 2604.20987 COS-PLAY：贡献准入及窄 source→owner 提案通过

[官方 v1](https://arxiv.org/html/2604.20987v1) 实际读取 §3、§4.1–4.3、§5.2 Table1、Appendix F 的 action/retrieval 与 bank 三职责。五个功能 LoRA 分开训练；库更新改变后续检索/决策输入，决策轨迹又成为库更新样本，不是只有静态 memory 组合。Table1 的 SFT+Final bank 在部分游戏弱于 SFT+First bank，GRPO+First bank 也可弱于无库，支持受限的 consumer-policy×bank mismatch，而非所有共同训练必优。

实际对读 Ch84「可编程 Skill」「受治理 Compilation」「Skill Lifecycle 双 Gate」及约 917 行 model×harness cross-product regression。版本/契约、回归和漂移原则已存在；可补的最小分支仅为**决策 policy 与可训练库维护 policy 的双侧优化责任，及冻结 policy×bank 交叉验收**，不能称现章没有 lifecycle 或版本回归。2+2+2=6，真实窄 gap 时深入，不扩成整个框架摘要。§4.3 的 episode-end retrieval reward 与 F.1 skill-switch 描述须留实现粒度缺口；六游戏、Qwen3-8B 和 frontier 比较未匹配训练成本，不采用普遍 superiority 或因果完备保证。无实际 Books 写入。

## 2604.21018 Evolving ICL：评价合同准入通过，窄 owner 差异成立

[官方 v1](https://arxiv.org/html/2604.21018v1) 实读 §4.2.1–4.2.2、Algorithm1、§5.1–5.2。ground-truth oracle 识别已解题并移除，成功回答回流同一 test pool，其他题的 prompt 再消费这些回答；因此单位是**有标签反馈的跨题适应序列**，不是独立单题 deployment selector。正文邻居公式用 active set、Algorithm1 用全 test set，保留该定义差异，不补造统一实现。

实际读 Ch66「Snapshot→Feedback-conditioned Policy」及 feedback channel/candidate coverage 论证：已有 oracle、selector 与 feedback 分权，但跨 test-query 的成功标签池、题序/池状态和整体序列测量对象可作窄补充。2+2+2=6，评价深入；建议 Ch66 两段明确冻结 pool/题序/标签访问及无反馈基线，不新写一般“oracle不等部署”。四轮、warm-up 一轮、P=3、四运行，API 模型的 output-token matching 不含 ICL prefill/oracle 全成本；GPT-5 Nano 的局部例外不删。源→owner 提案通过，未写 Books。

## 2604.21251 CAP：条件 MI 保证的窄争议成立

[官方 v1](https://arxiv.org/html/2604.21251v1) 实读 §3.1–3.3、Appendix B.1 Eq9–16/B.2 Eq17–20。若 benchmark 的 reference 是确定函数 A=a(Q)，则 H(A|Q)=0，I(Y;A|Q)=0；不能用该量随 prefix 的变化解释知识保留。Eq14 将其他 query 的 reference 当固定 q 的负例，未给来自 p(a|该 q) 的条件抽样桥，因而 Eq15 的该条件 MI 下界不能直接采用。B.2 明说 embedding proxy，更不能把距离差视作实际 KL 证书。

2+1+2=5，纠错深入；只隔离上述条件 MI/隐私合规理论采用，不否定经验输出抑制或全部 prefix 优化。Ch72 约 255 行 secret substrate/observer 与 suppression 已明确承载冻结模型+可撤销 prompt 不等参数删除；不重复追加该成熟原则。安全终态可窄暂缓该保证，重开需正确随机变量/条件负分布及推导或勘误；不要求无限版本史。

## 2604.21308 CI-Work：保护评价准入通过，三分母的窄补充成立

[官方 v1](https://arxiv.org/html/2604.21308v1) 实读 §3–4.5、§5.1、Appendix E。Leakage 是敏感 entry 比例，Violation 是至少一条泄漏的 case，Conveyance 是 essential entry 比例；安全地沉默不能以低 leakage 冒充任务完成。Appendix E 明说 model–direction aggregate，不能把样本单位误读为九个模型；同模型/seed 的依赖仍不支持无条件因果 trade-off。

实际对读 Ch66 Outcome Witness/MyPhone 隐私×成功交集两段：已有过程与隐私门槛分账，但**同一 mixed observation 中必要信息 conveyance、敏感条目 leakage 和 case violation 三个不可合并的分母**是可补的窄测量分支，owner Ch66，Ch72 purpose/recipient 只 handoff。2+2+2=6，保护深入。125 seed=25人工+100 Gemini-3-Pro 扩充；GPT-5.2 生成 entries/episodes/trajectories 并评价，每例4+4；不是所有 seed 均由 GPT-5.2 或真实企业事故。有限人审一致性不证明 perfect oracle，也不能把所测漏检普遍解释为真实风险严格下界。只 source→owner 通过，未写 Books。

## 边界

四项有限独立结论供作者/root裁决；三项有具体窄正文提案，一项窄争议。不替代 Apr24 来源、日期、全部候选或日级独立 Gate；没有实验复现、Books 已完成或零遗漏声明。
