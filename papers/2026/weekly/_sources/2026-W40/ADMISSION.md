# W40 周来源准入与有限停止

窗口：2026-09-27T09:00:00+08:00～2026-10-04T09:00:00+08:00。作者 w40_weekly；2026-10-05恢复。Daily既有结果仅复用，不重新发现。以下是首批准入校准包，尚不代表证据或Books通过。

## 首批拟入选（本次新周来源）

| 身份 / 原入口 | 原约束 → 具体增量 → 重考虑的选择 | 原始时间依据 / 拟评分 / 下一必要阅读 |
| --- | --- | --- |
| PyTorch v2.14.1 / https://github.com/pytorch/pytorch/releases/tag/v2.14.1 | 数据表示与算子配置正确不代表生成二进制正确；本发布修正NVFP4 tensor-wide scale遗漏和嵌套divergence reconvergence；需要把量化numerics验收绑定compiler/library component而非仅模型位宽 | API published_at 2026-09-30T19:14:48Z；3+2+2=7；仅release与CUDA精确纠错、必要MPS反侧，不审普通PR |
| SGLang v0.5.21 / https://github.com/sgl-project/sglang/releases/tag/v0.5.21 | abort不是DMA写完；新默认在PD失败路径暂留decode KV至多rank ACK，另layer-boundary collective及weight-update session改变兼容合同；重新考虑内存回收/数值与更新提交边界 | API 2026-10-02T01:09:04Z；3+2+2=7；只深入这些变化及具名silent-correctness/安全信号，不逐779普通PR |
| FlashInfer v0.7.1rc1/rc2及0.7.0.post1 / https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.1rc1 | 可调优候选不等有效候选；零行fast-math产生INF、MoE replay布局/下界和cuDNN plan元数据寿命改动影响正确性；重考虑winner复用与量化pack绑定 | API rc1 2026-09-30T16:43:06Z、rc2 Oct2 01:50:27Z、post1 Sep29 23:22:24Z；2+2+2=6，纠错须深入；需必要PR core及两compare限定 |
| Transformers v5.18.0 / https://github.com/huggingface/transformers/releases/tag/v5.18.0 | KV等价、停止边界、fractional时间坐标不能靠shape推定；本发布cache recompute断言、assisted eos/max-length及video RoPE/计数纠错提供具体接口验证边界 | API 2026-09-30T16:46:27Z；2+2+2=6，纠错须深入；必要精确PR与CI安全变化反侧 |
| Ray 2.59.0 / https://github.com/ray-project/ray/releases/tag/ray-2.59.0 | 本地cluster默认未认证且环境/数据入口秘密暴露与deserialize风险；新token default、dashboard redaction、Hudi guard及placement/lease tombstone修正边界；重考虑本地与远端默认安全和状态收尾 | API 2026-10-02T07:04:37Z；3+2+2=7；必要安全/取消core及BackpressureConfig核心；不能宣称远端默认认证 |
| Olmo-core 3 / https://allenai.org/blog/olmocore3 | FSDP按microbatch gather全部专家旧成本→resident expert DDP/EP、rowwise GPU routing与sharded optimizer实现改变可行性→重考虑固定active参数扩expert池与内存通信的取舍 | 官方October1仅日期/未显时区，需带时区原字段；拟2+2+2=6；blog core及tech report只读必要设计/对照，不照录2.7x普遍收益 |
| Prime Inference / https://www.primeintellect.ai/blog/prime-inference | DCP通信可能超过sparse读计算；NVFP4 pack/native unpack、block-major减少descriptor、最终tool response验证是不同边界；重考虑容量/执行/传输frontier与schema生效 | 官方article:published_time=2026-10-02未时区；需可完全落周窗范围；拟2+2+2=6；只核该blog关键对照/图/条件 |
| METR per-action blocking monitor / https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/ | judge分数不等运行覆盖/见到所有action/阻断/可信人审；实际漏监、子agent不见与自动按键approve反例改变monitor保障范围 | datePublished=2026-09-27T00:00:00-07:00，保留日精度按PDT整天[Sep27 15BJT,Sep28 15BJT)完全落周窗；3+2+2=7；四合取claim和必要操作/对照/人审反侧，不遍历所有附录 |

## 代表关闭项

| 材料 | 已读范围 | 具体理由与处理 |
| --- | --- | --- |
| Mistral Hallo, Deutschland! https://mistral.ai/news/hallo-deutschland/ | 官方全文核心：Munich hub、sovereignty、Physics AI、BMW/Siemens/TUM | 组织迁址、未来算力目标和工业合作，无新模型或系统机制；科学应用仍暂缓；日期时分不影响关闭，不另建日期请求 |
| World Labs is Joining AMD https://www.worldlabs.ai/blog/amd-announcement | 公告核心 | 组织并购及研究方向，不公开新Atlas机制；Fei-Fei转述同事件不重复入选 |
| Sakana SAIL https://sakana.ai/sail/ → 2603.08269 | 完整官方短稿及arXiv题摘、版本史 | 首次3月9、最新v2 Sep19；Sep28博客与IROS展示未指出新的机制/重要修订，不能按传播日重新评分；不是宣称原论文已证据审阅 |
| Extropic case study https://www.primeintellect.ai/case-study/extropic | 环境/奖励/heldout/core全文 | 约50 coding tasks上既有GRPO+70%exec/30%rubric，训练配方版本化与组合不新增机制；2.8x是局部应用结果，不将研究Agent称新训练原语；不因hardware主题扩科学应用 |
| AstaBrief https://allenai.org/blog/astabrief | 模型发布core待补读 | 不以scientific report任务或开放8B自身准入；如仅旧检索/引用配方和输出task收益则关闭，必要增量不明确时读core后裁，不能先称无贡献 |
| METR Senate testimony https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/ | 事件setup、与08/26原调查指向及三问题核心 | 旧incident调查转述及政策证词；核有无新的纠错/安全信号后关闭，不因重复机构名跳过 |

原始每周入口Web结果见RAW_WEEK_A～D；release API保100项page1返回数、first/last、next及窗内正文于RAW_RELEASES.json。Next存在且最后项已远早于窗口者不遍历历史尾。

普通未决：上述拟入选非作者FIRST、必要证据及Books差额；剩少量入口恢复；Daily隔离材料按周窗定点重判；10/04待作者终态与周级归并。均非外部受阻。

## 最终处置（覆盖上面首批停点，不覆盖原始筛选事实）

2026-10-05：首批8项已root实际核心校准；Prime因原日期时区未知隔离，不记确定候选。Olmo blog/report首公开日期也仍隔离，但对应官方v3.0.0 release已取得2026-10-01T15:17:49Z精确事件，准入改为release具名EOS/sidecar纠错，3+1+2=6；不以blog系统performance采用训练质量。PR843 API限流/web cache miss，仅以release说明为正面证据，不声称最终代码核验。GLM cyber定点日期恢复，3+2+2=7，root完整96行core/footnote独核通过，仅报告。

AstaBrief必要core已读并关闭：SFT+DPO/citation-density filtering与one-pass配置在有限14问题人评，不支持当前前沿通用增量或faithfulness；不是仅读题名。其他五代表EX核心关闭理由不变。所有7新增周源家族+1日期缺口家族处置见W40正文；10/04已经root完整Gate完成，七日日级结果170行归并169家族，最终177。Ch27/45/49/72六处窄差额实际POST已root通过。2026-10-05T16:22:00+08:00 root实际六部分/有限停止/去重/6负侧及完成态V3最终通过，普通待办0；外部覆盖与CodeJudge争议仍隔离，不授正面Evidence、Books或无遗漏。不保留“待补读”候选或普通release队列。
