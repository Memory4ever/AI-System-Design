# 2026-02-07 遗漏来源补查

检查时间：2026-10-08T12:47:05+08:00。只新增检查北京时间 2026-02-06 完整自然日（date-only）；原窗口、41 家族、原日期/评分、连续原 §4 与有效审阅均冻结。运行前正文见 [baseline](baseline-before-supplement-20261008.md)。不使用原候选反推准入；不展开旧 158 ID、整分类或整月队列，不扫描每周组，不写其他日/索引/LEARNING_STATE。

## 有限入口与停止

- SRC-OPENAI：当前 Research 与 RSS；urllib RSS403后，native curl成功，1255项只抽取Feb5/6/9相邻date字段，Feb6仅localization；[native-2](supplement-20261008-native-2.txt)。该core原有效贡献关闭复用，不因补查重审；[必要定位](supplement-20261008-gpu-localization.txt)显示Feb6与政策说明，不认证执行机制。
- SRC-ANTHROPIC：Research当前10条止于9月；Alignment官方目录仅定点Feb月两题名，PSM官方Feb23窗外，HotMess月日期未明确；Opus4.6 Feb6三处命名/脚注有效关闭复用，无本次新增修订线索。见 [first-probe](supplement-20261008-first-probe.txt)、[Alignment及日期](supplement-20261008-gpu-localization.txt)、[HotMess论文身份](supplement-20261008-anthropic-date.txt)。不把月标题作为Feb6日期。
- SRC-GOOGLE-AI：Google Research当前发表列表及DeepMind publications page3；后者本轮30个metadata从Sep16降到Feb12→Feb5→Jan9，夹窗停止，未审全部论文。news历史分页/first-public完整性仍缺。见 [official-tail](supplement-20261008-official-tail.txt)。
- SRC-META-AI：Research正文0行，官方域Feb6/date+主题检索未恢复本窗事件；有限停止，不授零发布。[official-probe](supplement-20261008-official-probe.txt)、相关域查询见 [related-source](supplement-20261008-related-source.txt)。
- SRC-QWEN：官方旧页redirect；native retrieval qwen_ai/en-US 40个日期metadata全部核，Feb3 CoderNext→Feb10 Image2夹窗，无Feb6字段；未审40正文。可复查 [native-0](supplement-20261008-native-0.txt)。早期大响应 [qwen-response](supplement-20261008-qwen-response.txt)被工具截断，仅诊断，不用于覆盖或正文证据。
- SRC-DEEPSEEK：当前官网Research/More只近期型号，历史Feb6模型/训练主题域补检未恢复dated事件；不展开全站。[official-probe](supplement-20261008-official-probe.txt)及 [topic-search](supplement-20261008-topic-search.txt)。
- SRC-MOONSHOT：Platform完整26标题止于2025；原Kimi1.9实际有效审阅保留（其原日期为Feb7，不移动进补充窗），未发现需定点恢复的新机制事件；当前目录非历史全量证据。[official-probe](supplement-20261008-official-probe.txt)。
- SRC-TENCENT-HUNYUAN：web提取0行后，实际使用in-app browser进入research?page=1，已读“全部”11条标题/date：Sep22两条、Aug28、Aug11、Jul21、Jul6、May21、Apr30、Apr23、Feb13、Feb3；Feb13→Feb3夹窗，页尾无下一页。浏览器实际可用，不继承旧不可用状态；仍非不可变历史快照。
- SRC-ZAI：官方Research当前15标题日期，Feb11→Feb2夹窗，未按GLM名称扩扫。[official-probe](supplement-20261008-official-probe.txt)。
- SRC-BYTEDANCE-SEED：实际GET get_article_list_v2，type1/year2026/ascending/count20/token0：returned20/total82/next20/has_more，Feb5→Feb9跨窗即停止；type2同参数returned9/total23/next20/has_more，首Feb12窗后即停止，不续全年。正文只metadata筛日期，不审窗外AB；[corrected papers](supplement-20261008-seed-metadata-corrected.txt)、[corrected blogs](supplement-20261008-seed-blog-corrected.txt)。第一次解析误用articles键产生returned0，原 [seed-metadata](supplement-20261008-seed-metadata.txt)与native-1截断不得作为阴性覆盖；实际数组是sub_article_list，已定点纠正。
- SRC-BAIDU-ERNIE：Blog page1当前10项，Apr15→Feb6 ERNIE5→Jan29夹窗。Feb6官方Blog与更早04705家族同机制的有效去重结果复用，无新增修订信号，不改原日期。[official-probe](supplement-20261008-official-probe.txt)。
- SRC-XIAOMI-MIMO：Paper8项June29→Mar13→Feb3→Jan8，Blog15标题无日期；只核metadata与本窗域搜索，未恢复历史dated Blog。[official-tail](supplement-20261008-official-tail.txt)。
- SRC-MINIMAX：本轮EN目录成功，10项日期在Feb12→Jan27跨窗；CN13项在Feb12→Jan28跨窗，AgentTech原有限有效metadata复用，未产生具体新事件。修复的是本轮EN可访问性，不删旧访问失败事实、不授历史完整性。[official-tail](supplement-20261008-official-tail.txt)。
- SRC-ARXIV：四有限主题（模型/优化、推理/GPU、世界模型/多模态、Agent/记忆）的Feb5/6相关术语检索与相关标题补检；原查询/返回见 [topic-search](supplement-20261008-topic-search.txt)、[related-source](supplement-20261008-related-source.txt)、[first-probe](supplement-20261008-first-probe.txt)。官方day列表 https://arxiv.org/list/cs.CL/2026-02-06?show=2000 与advanced日期主题页web cache miss；native API以Feb4–6 submission缓冲仅发现用途，Rate exceeded；native advanced无可用响应，浏览器advanced实际显示Rate exceeded。未调用catchup、未展开月宽页。不以提交日期或搜索索引替代公开日，不称无遗漏。

## 题摘贡献与隔离

确定新增候选0；新4个具体潜在贡献保留项不混入原41，不评分、不授Evidence/Books/Coverage。前三项完整exact-v1题摘及第四官方核心说明实际读过；不是论文证据审阅。

1. [CoSA 2602.05148v1](https://arxiv.org/abs/2602.05148v1)：低秩更新在谱较均匀时可能限制表达 → 固定随机投影+compact learnable core的参数化替代 → 若成立须比较低秩结构与可学习子空间/表达预算，而不只按PEFT名称排榜。完整AB与v1 SubmittedFeb5在[first-probe](supplement-20261008-first-probe.txt)。root已实际AB潜在准入通过；谱条件/泛化优势未核。缺首次公开日或dated原公告，本窗不列确定候选，不读正文绕过日期。
2. [Parity, Sensitivity, and Transformers 2602.05896v1](https://arxiv.org/abs/2602.05896v1)：旧PARITY构造依不实用组件 → 标准softmax、长度无关polynomial PE、noLN且可causal构造和1layer1head下界 → 若成立须按模型定义区分可计算性与浅层表达上限。完整AB与v1 SubmittedFeb5在[first-probe](supplement-20261008-first-probe.txt)；作者PDF封面Feb5仅稿日期，不证公开日。root实际AB潜在准入通过。仅缺首次公开日，必要定理未审，不评分/采用。
3. [GPU-to-Grid 2602.05116v1](https://arxiv.org/abs/2602.05116v1)：单独最小GPU能耗忽略电网目标 → inference batchsize+电网/GPU双测量反馈，降低耗能可缓下限但增加耗能可缓上限电压 → 若成立，batch调度需绑定电网约束与latency/throughput而非只最小功耗。完整AB、v1 SubmittedFeb4及v2July22在[gpu-localization](supplement-20261008-gpu-localization.txt)。root实际AB潜在准入通过，不因eess.SY拒绝；仅缺首次公开日，不读控制器/实验、不评分采用。
4. [The Hot Mess of AI](https://alignment.anthropic.com/2026/hot-mess-of-ai/)：总error不能区分系统偏差与采样不一致 → well-defined target下bias/variance的error composition及自然长思考/受控预算区别 → 若成立，评价须分开错误率、错误类型与干预归因。官方核心说明已可读，Blog只有February2026；所链接2601.23045 SubmittedJan30，April10 v2标typos/writing/references。不知Feb6是否新事件；Jan–Feb日报只定点同ID检索无命中，不将无命中变日期。缺Blog精确公开日及首次/修订事件身份绑定，保留而不评分/采用/读论文核心。

恢复材料只需对应首次公开日期的官方公告/列表快照或作者dated原事件；HotMess另需Blog与更早论文的新事件绑定。取得后只重开本日对应AB→日期层；若确属窗外则路由真实归属日，不改原41。

## 具名有限关闭与未检查范围

- OpenAI localization、ERNIE5 Blog、Opus4.6 Feb6三项命名/脚注：原有效贡献前关闭/同family去重判断复用；不新增评分，也不对原有效证据再审。
- PSM：官方页Feb23，窗外，仅读日期即停；不审其整篇或由月目录带入Feb6。
- Parallel Track Transformers2602.07306：相关GPU查询发现，Apple官方只February月，arXiv SubmittedFeb7；明确有机制但不是确定Feb6事件。保留原论文链接以恢复真实日期，不阅读核心，不授本日候选。科学domain热点、非窗口搜索项未展开，不追整个周/月队列。

本次无Books新写，原29/9/2/1有效处置保留。原AutoInject/CORP精确版本异常、TimelyFreeze中心矛盾与必要历史目录仍隔离，不重复追完整版本史。新增4date/event holds及ParallelTrack归属线索不支持无遗漏声明。

## 独立复核停点

作者supplement_20260207已完成有限来源与普通研究处理；root前三AB及HotMess官方核心全文实际潜在准入校准通过，公开日/新事件仍不足，四项继续隔离。MiniMax EN本轮成功，覆盖表不以旧失败宣称当前受阻；arXiv新项必要公开日仍受阻，旧已检查不授新增Coverage。root已实际核完整六部分差额、14入口有界记录、具名关闭、Seed正确数组、Qwen40日期、DeepMind30、MiniMax恢复及原41/窗口/连续§4冻结和122refs；独立DAY语义通过。作者按该实际验收及具名修正写回完成态，普通待办0。不stage/commit/push，不接下一天。

补检原查询：Meta/DeepSeek/Moonshot/MiMo明确官方域+Feb6日期定点搜索原响应见[domain-date-search](supplement-20261008-domain-date-search.txt)，有限无命中不证明0事件。HotMess实际Blog核心原件见[hotmess-blog](supplement-20261008-hotmess-blog.txt)，不是只用abs v2摘要校准。

作者本地核验：V3 single-report通过；原41候选行逐字保留、原窗口字段不变、原§4连续全文为当前正文连续子串；限定本日README/source的unstaged及cached diff-check均通过。来源语义与终态隔离已由root实际DAY通过，不由机器自批；完成态再次运行同一限定核验。
