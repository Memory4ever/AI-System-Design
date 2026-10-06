# Daily Research — 2025-09-20

**规范：** V3
**窗口：** 2025-09-19T09:00:00+08:00 ～ 2025-09-20T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T20:26:28+08:00

## 1. 结论

本日非作者独立验收通过。实际原53精确v1完整题摘加同段cross-list12题摘，共65＝62机制/替代输出/理论/局部负面潜力、3贡献关闭；另主段5、cross-list5及系统medical1共11标题级范围关闭。具体校准、反侧与查漏见[独立复核](../_sources/daily-20250920/INDEPENDENT_DAY_REVIEW.md)。它们是有界发现，不是本窗新论文数。0已确认落窗正式候选、0证据完成家族、0 Books写入；不解释为零事件或无遗漏。

重要潜力包括异质query缓存、语音层/视觉grounding反证、adaptive MoE pruning、光路collective重配、9600GPU拓扑调度、RL时空流水与训练故障恢复。MiMo-Audio核心也保留具体替代设计，但Sep19整天相交与commit字段不确定首次公开。Google TTD-DR本次Blog拟关闭为July贡献再阐述，非旧论文无价值。没有复现或采用缺日期的正面结论。

## 2. 来源覆盖

实际请求/原字段/停止条件详见[FETCH](../_sources/daily-20250920/FETCH.md)，这里只声明有限切片。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS200原1247项只筛本窗UTC19T01→20T01，0；Research403保留 | 已检查 | RSS有限切片，不授全站修订/删除历史 |
| SRC-ANTHROPIC | Research首次partial后20秒重试200，Next恢复172publication原publishedOn本窗0 | 已检查 | 保留目录切片，不由其他日继承 |
| SRC-GOOGLE-AI | Research九月月路径第1页12条至Sep11；TTD-DR核心/July v1题摘；DeepMind当前目录及严格Sep19域补检 | 受阻 | Blog切片可恢复，Pubs/DeepMind历史目录不完整；搜索空不记0 |
| SRC-META-AI | Research connection reset，官方域Sep19主线补检空 | 受阻 | 无可靠历史目录，不支持无事件 |
| SRC-QWEN | 本日独立page_config HTTP200原60日期配置，只筛本窗0，NextSep10T20Z与TTSSep21T20Z夹窗 | 已检查 | 有限原date切片，不遍历60正文或授全站修订 |
| SRC-DEEPSEEK | 准确API文档updates实际200，Sep29/Sep22/Aug21连续跨下界停止 | 已检查 | 只Change Log，不授所有论文/仓库历史 |
| SRC-MOONSHOT | 官方Blog日期序列Sep16/Sep5低于本窗，组织入口有限 | 已检查 | 保留Blog切片，非仓库全历史 |
| SRC-TENCENT-HUNYUAN | Research壳与正确publicList POST9条，最早displayPublishTime为2026 | 受阻 | 九月历史全部未恢复，非0条 |
| SRC-ZAI | Research实际page2累计18/hasMorefalse，无序minDec7；官方release notesSep30→Aug11夹窗 | 受阻 | Research九月缺段，release notes不补论文目录 |
| SRC-BYTEDANCE-SEED | type2 year2025 token0原15/49、hasMoretrue/next20，非置顶至Aug20T16Z和Jul14T16Z停止；type1实际0/20/40/60/80，80 has_more=false停止，20仅窗外SwiftSpec、0/40/60缺列表 | 受阻 | Blog切片跨窗，论文total94未完整恢复；原分页及停止见差额，不授94已读 |
| SRC-BAIDU-ERNIE | Blog page1/2保留日期至Sep12/Aug14跨下界 | 已检查 | 有限Blog，不授仓库所有修订 |
| SRC-XIAOMI-MIMO | Paper8行Sep19/Jun4；具名GitHub/Demo核心、max20 commits实际5个；本日官方runtime+8557/6159完整Blog15题名/描述，More同数组8+7无后续网络页 | 受阻 | Blog15均无date，历史目录缺口仍在；25Hz/patch设计潜力但原首次公开/时区上界未证，不由commit作public |
| SRC-MINIMAX | US12至Oct27、CN13至Jan15、Agent one2026May，原页独立读取 | 已检查 | CN有限保留日期切片跨下界；非全站历史完整性 |
| SRC-ARXIV | 12分类主题API429；5系统分类主题API200共7、6相关精确v1；CL正确月路径2000/2214仅有限主段52标题、47题摘，再核同ID段cross-list17标题、12精确v1题摘 | 受阻 | submitted不是public；历史new?date返回2026当前页；具名日期补检无首发证明，不扩全月全文 |
| 补检：[HF Papers](https://huggingface.co/papers/date/2025-09-20) | 仅arXiv主题接口429触发本日具名日期一次web及10秒curl | 检索受限 | web失败/curltimeout0，不取消触发也不借他日候选 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

日期未证的62潜力及MiMo不列确定本窗候选、不先评分；详细准入理由见[首批交接](../_sources/daily-20250920/FIRST_BATCH.md)、[必要core差额](../_sources/daily-20250920/NARROW_SOURCE_SAFETY_HANDOFF.md)及[最终独立校准](../_sources/daily-20250920/INDEPENDENT_DAY_REVIEW.md)。这不是零事件或准入失败。

## 4. 证据与知识整合

[TTD-DR官方Blog](https://research.google/blog/leveraging-test-time-compute-to-scale-deep-research/)相关draft/search/revision与judge完整核心、[2507.16075v1](https://arxiv.org/html/2507.16075v1)完整题摘及旧§2–4必要差额实际核对；方法、ADK及结果/消融已在July版本，当前一句availability未新增执行/兼容/安全约束。独立通过只关闭本次再阐述，不授旧论文全篇深审。不同backbone默认系统比较不能归因于单组件；Blog消融口径差异保留，无matched成本不采通用加速。原记录20core0/1及本日INDEPENDENT_TTD_CORE。

[MiMo-Audio官方Demo](https://xiaomimimo.github.io/MiMo-Audio-Demo/)与[GitHub](https://github.com/XiaomiMiMo/MiMo-Audio)本轮核心显示25Hz/8RVQ、patch4降LLM输入至6.25Hz再delay decoder恢复25Hz，属于具体替代设计潜力。Paper的Sep19日期相交本窗，原commit在下界前后都出现不证明首次public；不引December论文为本次版本，不采29倍普遍成本或部署能力。

53题摘中安全/负面潜力已保留：15478文本攻击略强、15476trimodal劣于两模态、15655末层语义下降、15837视觉对speech语义未增强、15701PCC/SCC差异、16107简化削弱澄清。它们不能因为局部任务或小样本关闭；题摘并非深审。系统6项精确v1与最新版分离，特别RLinf v1 1.1–2.13倍不能替换为v2数字。

本轮必要core有界补读15478v1 PDF方法/分模型方向/评分/统计限制与D.1，16107v1分类目标、单次DPO和英文全排列，以及16241v1 Algorithm1/Figure2/人工执行评价。REAMS的oracle失败选择与未统一重试预算构成具体评价边界，撤回旧关闭；另维持15896安全现象归纳的综述关闭，不授所引研究已审。实际证据位置与采用限制在差额，不将日期隔离项计证据完成，不扩53篇全文。

独立核15839v1§2.2/Fig2与§3，撤回物理领域范围关闭：错误推理仍有正确终答是通用模型评价的局部反例，不启用AI for Science；step-judge未人核、ASA/ASC混写与输入图信息差额保留。原53现51潜力/2关闭。相同ID有界cross-list12完整题摘中11保留潜力，16244仅PEFT/QAA综述/方向无具体新增机制或条件对照，贡献关闭。16060 SABER实际白盒forward权限、prompt移除混杂/能力下降，不采全模型51%或无损；16163实际CLIP/PGD与Table1，最佳五层恢复与单层22%成本不同配置，不授adaptive防御或部署性能。新增十二ID逐项边界、两个安全必要原件及标题分层见独立复核；没有扩大全文队列。

Books拟增量与实际写入均0：不是“通用原则没变”排除，而是首次公开未证，不能进入本日采用链；尚未声称实际owner完整对照或已有覆盖。取得日期且root校准后按研究合同§5–6定点读证据与owner，只由root改Books。

## 5. 缺口与下一步

**普通待办：** 无；本日首批校准、同段有界查漏、必要风险和六部分DAY已非作者实际完成。**终态保留项：** 以下真实外部日期/历史目录缺口保留精确重开，不支持正面Evidence、Books采用或无遗漏断言。

- 62潜力精确v1逐ID见首批表、REAMS/15839差额与独立cross-list表，缺真实原首发公告或支持完全落窗的区间。主题API429、系统API只published/submitted、正确月表无日公告、历史new参数被忽略；具名日期搜索只恢复转载/提交。可接受作者原始发布或官方公告/历史public artifact；到达后仅重开对应家族版本/日期与必要证据，不重扫65或2214库存。
- MiMo-Audio缺原公开时区/first-public上下界，commits只证明代码版本时刻，不证明当时public；请求官方Sep19原公告或历史公开artifact证据。到达后仅恢复该家族，本日不采用。
- Google Pubs/DeepMind、Meta、Hunyuan历史全部、Z.ai九月Research、Seed论文缺段：FETCH保留真实原响应/有限停点。可接受目标窗口官方归档或带身份、原公开字段和真实分页边界的API；只窄重开受影响源。当前页数量不证明过去无研究。

## 6. 复核

复核者：sept07_10_author（非本日作者，本日作者Tesla；不写共享Books）。

结论：通过

实际范围：[独立记录](../_sources/daily-20250920/INDEPENDENT_DAY_REVIEW.md)所列14源有限停止、65完整v1题摘准入、3贡献关闭及11标题分层范围关闭；安全/负面均纳入，15478/16107/16241/15896/15839与新增16060/16163仅必要核心，不是全部全文深审。正式候选0、证据完成0、实际Books0；外部终态不支持正面采用或全站无遗漏。格式校验不代替本日语义裁决。

本次V3与限定diff-check通过；机器检查不替代语义。Books、月README、LEARNING_STATE归root，未stage/commit/push。
