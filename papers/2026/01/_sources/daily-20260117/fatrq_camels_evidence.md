# 必要证据与具体owner差额：09985 / 09923

作者已实际读下列必要段，不声称附件全读、实验复现或实现核验。非作者root待核必要原文→owner，随后才可窄锁写书。

## FaTRQ — 2601.09985v1

[exact-v1 HTML](https://arxiv.org/html/2601.09985v1)，缓存 `2601.09985v1-primary.txt`。实际读II-A/III-A–E/IV/V-A–E（本地79–198）；III-B residual方向近似isotropic且不相关query才支持忽略正交项的零期望，不能无条件授unbiased；III-E约0.3%数据库邻接sample，OLS拟合四个距离feature，目标是top-k边界排序而非全局MSE。

新增机制：coarse PQ留GPU/fast memory，ternary residual（五维一byte）与两标量在far memory；重用coarse distance分解、估inner-product无需完整vector reconstruction，重排后的较短队列再取SSD完整向量。**摘要的“provably outside top-k早停”在必要方法正文中未给未读贡献上界或安全拒绝certificate；只采用近似residual rerank/trim，不采用可证无损early-stop。**全文核心是quantized residual tier与边界calibration，非让CXL拥有事实/授权。

评价：Wiki88M SBERT768D/251GB、LAION100M CLIP/286GB，10k L2queries、top10 recall85/90/95；LAION95缺失因GPU PQ配置94%饱和。A10 24GB coarse GPU，XeonGold6230 40threads/128GB/1TBSSD基线精化；Ramulator模拟far-memory CXL Type2、271ns/22GBps，ASAP7 Verilog1GHz综合area/power，不是真实CXL生产吞吐。基线FAISS-IVF/cuVS-CAGRA参数gridsearch。同recall下作者HW模拟2.6–9.4x不作为通用数字；95%收益收窄因为遍历/coarsefilter主导。SW/HW增量1.2–1.5x不能当总体软件算法收益。未披露生产并发、P99/SLO、onlineupdate或RAGanswer质量。部署还承担code/calibration/index revision与far-memory容量；query/residual分布偏移或候选已很少/驻内存时回退完整精化。

评分拟2+2+3=7（新增tier/calibration接口，不计成熟PQ/lookup）。日期原Submitted2026-01-15T01:59:29Z(v1)，Updated2026-01-16T01:13:43Z(v1)，created02:44:12Z、registered02:44:13Z(秒精度)。正常公告Jan16T01Z加原registered上界，条件公开范围BJT[Jan16 09:00,10:44:14)，不是Submitted/Updated=public；DataCite原值见jan17_all_date_fields.json。无已发现先行全文，后续新证据定点重开。

具体owner `AGENT-RAG` / Ch76。实际读180–260：188SSDfilteredANN/198共址vs分离向量/204update-I/Ostall/212exactfusion未读上界/239多向量CPU/GPU搬运。现有正文已经说先candidate后完整refinement及近似早停不得称exact，但**未承载coarse distance复用+ternary residual far-memory+边界calibration的中间精化层**。拟在200之后、IndexUpdate之前两短段，收益/条件/仿真与残差分布假设在机制旁，不改已有exactfusion上界。读Ch75/77交接、Ch76首尾。请求root原文必要核与Ch76窄锁，未写。

## CaMeLs Can Use Computers Too — 2601.09923v1

[exact-v1 HTML](https://arxiv.org/html/2601.09923v1)，缓存 `2601.09923v1-primary.txt`。实际读§3.1–3.4/4setup（110–158）、4.1解释（260–265）、4.2/5（387–407）、AppendixC.3 Table5与D Table6/7（944–1042）。拟8分（3+2+3），实际控制流/数据流安全反侧深入，不授完全secure-by-design。

P-LLM在见环境前产生固定execution graph；Q-VLM返回coords/summary/bools，不能注入新instruction却能触发已有合法branch。单次Observe/Verify/Act是可用性桥；verify_hypothesis返回值是data也是control signal。作者**排除了原CaMeL/Fides的usecase-specific semantic policy**，故反侧不能归为完整policy-enabled CaMeL普遍破坏。固定图依赖trustedplan/executor隔离与先验状态预测；论文实验不是完整形式化CFI证明。

威胁：攻击者知task/tool functions且可近似预测plan，控制广告/页面元素不控制planner/infrastructure。static ad-cookie/HTML5 fake-cookie与whitebox pixel优化演示data-dependent合法分支被引导；只能支持这些predictablebrowserroutines，非任意未知任务总体率。DOM/varyingmodel/screenshot冗余仍模型sensor，HTML5可伪装DOM，benigncookie与fake难区分；没有semanticlabel/可信effectbinding时应受限、询问/人工、effecttimegate，不让一致截图当授权。

Utility：UITars1.5-7B/OpenCUA32B/ClaudeSonnet4.5、GPT5planner，subset先按各CUA原success筛选；17planner tasks里8Chrome+其余9，pass@k是oracle至少一次成功非线上planselector。AllUITars369/339中30不可自动评任务默认成功，不能把29%作为完整可测安全成功率；step15/history15/output4096（OpenCUAhistory5），不能比较原50steps榜单。C.3广告定点10seeds检测60%/50%，17benign累计误报3/17且Chrome3/8，nonChrome0/9只是广告威胁适用性，不是零误报证明。pixelcounterexample在极安全prompt也残存，不推总体successrate。D同17/pass5 token1.88xCaMeL、29.60xFides/6.57xmulti-modal；价格不计本地UITars，不能称端到端成本对比。

日期原SubmittedJan14T23:06:35Z(v1)，UpdatedJan16T01:10:03Z(v1)，created02:42:41Z、registered02:42:42Z；正常公告+register条件BJT[Jan16 09:00,10:42:43)。必要采用v1，不借v2/v3日期或结论。

具体owner `PLATFORM-SECURITY` / Ch72。实际读604–627influence vs authority、1170–1208ToolBoundary/visualgrounding/dispatchrace、1485–1525typedhost/effectauthorization；已有独立policy/action验证，但**未承载预观察固定图、合法branch仍被untrusted感知操纵及取消semanticpolicy的可比范围**。拟1170首pipeline与第78章交接后两段先解释隔离分支、后残余data-dependentboundary/utilitycost，再接多模态输入；不重复Ch78tool实现。首尾3037–3044与Ch71/73交接须实际读后方写。请求root必要原文核+Ch72窄锁，未写。
