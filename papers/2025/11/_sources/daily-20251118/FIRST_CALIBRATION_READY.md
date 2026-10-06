# Nov18 First Calibration Ready

作者Carver；实际2026-10-04T20:03:50+08:00。本窗BJT `[Nov17 09,Nov18 09)`。本日独立取回并实际读六篇exact-v1完整题摘、各自DataCite原字段；未读方法/实验或作Books判断。请root/Ohm等非作者先核具体准入及代表性关闭，不等日级结束。

## 五项potential（不是已定当窗候选）

| 身份与本日完整题摘 | 原文增量与待独立核验边界 | 原日期：Submitted / Updated / created（UTC） |
| --- | --- | --- |
| [2511.11553v1 Multistability](https://arxiv.org/abs/2511.11553v1)；[本日原页](abs-2511.11553v1.html) | 连续时间single-head attention/Oja模型出现多种稳定吸引状态，非仅principal eigenvector；可能修正attention动力学的单一收敛直觉。仅此模型/假设，不预授一般训练或多头Transformer等价。 | Nov14 18:45:22 / Nov17 02:01:55 / Nov17 02:56:37 |
| [2511.10899v1 Proof and Program](https://arxiv.org/abs/2511.10899v1)；[原页](abs-2511.10899v1.html) | 工具选择与执行正确仍可伴随推理过程退化，TIM/PYMATH给出直接反侧。不能因数学任务误作science应用关闭；摘要中的accuracy、myopia比例尚未经core核验，不外推所有tool agent。 | Nov14 02:21:34 / Nov17 01:12:48 / Nov17 02:41:35 |
| [2511.10753v1 FengHuang](https://arxiv.org/abs/2511.10753v1)；[原页](abs-2511.10753v1.html) | local/central remote memory分层、active paging与near-memory tensor ops提出不同推理内存放置/计算取舍。明确vision与initial simulation，非实机、production能力或通用通信收益。 | Nov13 19:11:39 / Nov17 01:02:54 / Nov17 02:38:18 |
| [2511.13751v1 Inside VOLT](https://arxiv.org/abs/2511.13751v1)；[原页](abs-2511.13751v1.html) | SIMT分析/优化集中在可跨frontend和ISA复用的编译层，案例为ISA扩展及host API；请核是否有足够具体机制增量，不能因非LLM或编译器分层熟悉自动关。非实际成本/性能保证。 | Nov13 23:12:00 / Nov19 01:00:54 / Nov19 02:44:51 |
| [2511.10860v1 HPCAgentTester](https://arxiv.org/abs/2511.10860v1)；[原页](abs-2511.10860v1.html) | OpenMP/MPI并行construct、通信与hierarchy test，经RecipeAgent/TestAgent critique迭代生成；潜在执行约束驱动测试改进，但模块组合/比standalone强本身不足。请校准具体增量门槛，不预授普遍bug检测/可靠性。 | Nov13 23:52:53 / Nov17 01:09:48 / Nov17 02:40:43 |

五项DataCite均Available=`2025-11`、Issued年份；见对应`datacite-<ID>.json`。Submitted不是public；Updated/created不是首公开字段。即使Nov17 Updated/created落窗也不单凭它们授日期；Inside VOLT的Nov19字段尤其不能当Nov18公开。实际原公告或完全落窗首公开上下界仍可解hold，正在有限恢复，不用schedule补造精确时刻。

## 两项代表性拟关闭

- [2511.10788v1 Adaptive Reasoning Survey](https://arxiv.org/abs/2511.10788v1)：[完整题摘](abs-2511.10788v1.html)提出经典reasoning形式化、control-augmented policy目标及training/inference taxonomy；摘要没有新控制机制成立条件或直接反证。拟以具体增量不足关闭，不以“综述”类别自动关；若非作者发现决定准入的新事实，仅定点重开。日期未核，不需为已明确不采用项扩全文/日期队列。
- [OpenAI named Emerging Leader in Generative AI](https://openai.com/index/gartner-2025-emerging-leader)：原RSS `Mon, 17 Nov 2025 10:00:00 GMT`（BJT17日18:00）落窗；Research/core native403后，[本日web实际核心](web-primary-recovery.json)已读。机构认定、客户采用与现有controls宣传，没有新增机制/实现/有效性边界；Gartner免责声明将评价标为opinion且非事实/endorsement。拟关闭；未读Gartner付费报告，不采用其效果或安全保证。

## Root独立复核反馈与作者局部同步

2026-10-04T20:53:35+08:00同步root独立复核反馈，非人类用户证据：root actual35份完整v1AB（10876/10909多段另补全）；11553/10899/10753 potential保留，13751/10860继续由root窄core判断具体增量，作者不重复其审阅。

11472 Conformal原AB的imbalance-bin评价盲区、uniform-mass修正及group-conditional threshold属于学习/不确定性评价机制，旧“ImageNet/未Foundation直接链”范围理由撤销，恢复potential。作者仅做[该ID最小日期恢复](DATE_REVIEW.md#conformal最小日期恢复)：v1 Submitted/Updated/Available、created/registered原值不是firstpublic，具名原公告检索不足，仍hold，不展开全文Evidence/全实验/owner。现26论文+Antigravity=27potential、9AB拟关闭、6标题范围关闭，确定当窗候选0。

MiMo沿本日真实首页脚本定位8557/6159 chunks，actual静态15项、initial8、More仅翻state显示后7项，无分页；[SOURCE](SOURCE_REVIEW.md)及日报§2/5已修正，不盲抓或读15全文。剩余普通为root必要准入core、有限来源/日期处置及日级和作者后续局部反馈，不自授完成。

## Root必要core实际准入及反侧反馈

2026-10-04T20:59:22+08:00同步root独立复核反馈，复用其实际原段，不重复作者整篇读取：

- [11553v1](root-core-2511.11553v1.html)§1/2/Assumption1：固定QKV、unit sphere、time=layer/infinite-depth，V symmetric positive且simple largest；只支持此ODE的多稳态边界，非训练或一般Transformer等价。
- [13751v1 VOLT](root-core-2511.13751v1.html)§4.3：late inversion、predicate reload、divergent select破split/join，用IR planning及last MIR safety net处理，是具体机制potential可留。§5.2 psort instruction增多、ZiCond请求密度变慢条件不可抹，不授普遍/生产性能。
- [10860v1 HPCAgent](root-core-2511.10860v1.html)§4.1.1：HPCBugKG→AST易错parallel-pattern→recipe→execution critique支持具体机制potential。§3.2 Listing3 ASSERT_FALSE/is_consistent与caption自相矛盾，不能授测试oracle可靠/复现；§5.2多模型、5迭代预算，Table3不是同模型公平提升保证。
- [11472v1 Conformal](root-core-2511.11472v1.html)§3及Limitation：恢复potential成立，TSS受base accuracy及ground-truth rank饱和影响，不将新评价指标当无条件更可靠或医学效果。

27potential计数不变，全部日期仍hold；13751/10860必要准入core的旧普通停点已关闭，不授整篇Evidence/全部methods。其余必要反侧、14有限源/日期处置及六部分日级待真实非作者结论。共享Books未改。

## 可执行停点

首批校准普通待办：五项准入边界及两关闭；六篇仅完整题摘，不称Evidence完成。作者继续其他来源有限停止/其余相关题摘和必要首公开恢复，不等待校准。全日六部分/日级尚未完成，共享Books/index/state写入0。
