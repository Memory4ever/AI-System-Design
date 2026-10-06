# 2025-11-05 两公告必要证据与owner差额

作者Carver；2026-10-04T17:26:19+08:00恢复05时重读AGENTS、三份适用合同/来源使用说明/每日/arXiv、CODEX_RESEARCH_PROMPT、ROADMAP、最新相关checkpoint和05STOP。root独立复核反馈已实际读FIRST原核心，认可Suncatcher基础设施范围及拟2+2+2=6，要求只保留必要物理/实验/估计边界；deprecation窄为真实保存承诺，访谈不授welfare/safety因果。此反馈是智能体复核，不是人类证据；13项题摘/DDCL独立notes仍待到达。本文件不是日级验收或Books POST。

## Suncatcher：必要标准证据与具体拟整合差额

精确材料为[本次官方Research公告](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/)L104–144，与FIRST保存原返回同一内容。重新定点核L117–139和142–144，未见改变判断的纠错标记。公开事件仍是官方公告HTML datePublished=2025-11-04T17:00:00+00:00，不把预印本submitted或论文ID当归属。

- 问题/机制：大型ML负载需要高带宽低时延通信，作者分析目标是tens of Tbps，而非已测结果。DWDM/空间复用需要比常规长距链路高得多的接收功率；原文接收功率随距离平方反比，因此以kilometers or less紧密编队补link budget。L121的800Gbps each-way只来自单transceiver pair bench，不是全编队带宽、collective或训练吞吐。
- 编队：L123–127是解析近似加JAX数值修正，示例81卫星/650km高/1km半径/next-nearest-neighbor约100–200m的一轨道模型；地球非球形引力及可能的drag是扰动。它支持条件性编队分析，不证明真实部署、完整collision avoidance、持续station-keeping或故障恢复。
- 硬件：L135–136为Trillium v6e/67MeV质子束的TID/SEE试验。HBM累计2krad(Si)起irregularities，750rad(Si)五年shielded任务剂量为预估；单芯片15krad(Si)未观察到TID导致hard failure，不等整个运行栈无软错误、寿命/辐射安全或所有TPU可在轨运行。原文未给本文拟采用所需的端到端ML workload、precision、batch/concurrency、SLO、样本重复/统计区间，记Not Disclosed，不从局部试验补造。
- 经济：L138依赖历史/预测launch price及持续learning rate，mid-2030s <$200/kg只是条件估计；对比口径为per-kW/year与所报地面energy cost，不是完整训练TCO、当前成本优势或既成采购价格。没有采用该数值作书稿设计结论。
- 直接反侧：L142热管理、high-bandwidth ground communications和on-orbit reliability仍开放；L143两颗prototype early2027是计划，不是已完成分布式训练。公告足够支持“能源placement替代分支带来新的通信几何和硬件环境约束”的标准边界，不足支持更强轨道训练/全通信/成本主张，故不扩预印本、轨道模型或grader可选实现。

已读取Books上下文PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE/最新checkpoint，实际owner [WORLDVIEW-FUTURE / Ch10](../../../../../books/part-01-worldview/10-future-of-ai.md)正文L1–262、邻接Ch9 L230–261及Ch11 L1–38。Ch10 L47–49“Energy与物理基础设施”承载电力、散热、机房/供应链/区域容量，L36–45承载compute和data movement，L207–221要求可证伪与时敏假设；尚未解释能源收集位置改变后，互连几何和硬件环境也同时改变的具体替代分支。不是因为缺Suncatcher名称而提出diff。

**交root的最小拟采用命题/位置：** 在Ch10“Energy与物理基础设施”现有段后、Latency前，增加一短段：近持续太阳能使空间计算成为条件性placement分支，但高带宽自由空间光链路的距离损耗要求紧密编队，换入轨道保持、辐射/热和地面通信约束；地面机房仍是实际SLO与维护路径可核的基线。局部地面链路/芯片试验和轨道模型不能证明在轨ML或经济优势。不要展开轨道方程、市场年份/价格/剂量/速度或项目名单。

定点读[PLATFORM-COST / Ch70](../../../../../books/part-06-ai-infrastructure/70-cost.md)L1–125、247–298：resource rate含power/cooling/network/operations，installed power→feasible placement与energy geography硬约束已有覆盖。经济估计只留报告，不新写成本owner，也不把Ch10做前沿收纳章。root若认为以上具体约束增量仍无需改变情景主线，明确仅报告也有效。当前作者建议拟整合，Books决定暂缓root裁定；未写书稿、无POST。

## Deprecation：标准证据与拟仅报告

精确[官方公告](https://www.anthropic.com/research/deprecation-commitments)L16–34再次实际读。L24是维护公开推理多模型成本/复杂度roughly linear的厂商变更理由，不是独立容量测量；L25保存所有publicly released及今后significant internal use模型的weights至少公司存续期，保存能力不等weights下载、公开API持续可用或完整execution可重现。

L27–31承诺退役时生成并保存post-deployment report，访谈responses/reflections与作者analysis/interpretation并列；Sonnet3.6 pilot只证明作者称做过该过程。L28明确不承诺根据偏好行动，L32选择性公开retired模型仅exploring。L17–23的shutdown行为与welfare是被引用的假设/背景，不为当前保存/访谈机制提供风险降低、体验真实性或福利因果证据；因此不打开旧system card扩为新安全评估队列。无性能实验，workload/hardware/precision/batch/SLO对此承诺不适用。

实际owner [PLATFORM-MODEL-REGISTRY / Ch59](../../../../../books/part-06-ai-infrastructure/59-model-registry.md)L1–205、280–332，邻接Ch58 L100–137及Ch60 L1–42已读。Ch59 L95–108将catalog-visible、CPU/GPU residency和readiness分开，L133–142分artifact durable bytes/retention与Registry identity/policy/status，L179–192含serving→deprecated状态和删除前deployment references/retention/legal hold/reproducibility检查，L31/55–69还指出完整deployment identity超过weights。这些真实论点承载保存资产不等在线可用或可复现。

**拟Books决定：仅报告，不新增Ch59段落。** 本事件具体增量是该公司的公开保存期限和post-deployment过程承诺，不提供新的保全实现/容量算法/恢复合同，也没有足够证据将模型访谈提升为独立真实性信号。长期分层实际已有，名称/期限缺位不是机制差额。该处置不撤销公告准入或降分；2+1+2=5按发布命题保留。待root独立核必要原文→现有owner→该No Change处置。无共享改动，无需writer POST。

## 当前机器/复核边界

两公告的作者标准必要审阅已完成；非作者必要证据、owner采用及日级六部分尚待实际notes。13日期潜力仍不计当窗候选，root准入校准可复用不重读其附件。报告保持进行中，机器检查只说明格式/引用，不替代上述语义验收。
