# 第二批必要源与实际 owner 比较

源方法/评价/直接反侧见 [第二批核心](V3_CORE_NEXT_BATCH.md)，10家族分数不借Books处置改变。以下是实际比较，不是已授写锁；只有root必要source与PRE通过并授具体文件窄锁才写。首批6实际整合已POST通过，与本页待办分开。

## 15166 / 15172 — Ch49，两个具体 mapping 差额

actual正文Ch49 L26/28与30/32、完整邻接19–49及末注2686/2688经过root独立POST。已窄纠正：sum同branch可并存reservations、max跨互斥branch，不是latency；TCM原The Turbo-Charged Mapper，partial relevant rank直接under storage改变linebuffer故保留顺序，不授跨storage node重排。POST通过，窄锁释放。旧建议措辞仅保留演变线索，以实际正文和已纠正CORE为准。

实际读Ch49 L18–43 typed equality/shape/dtype/layout/cost model，旧机制让表达式与schedule共同搜索，尚未承载“哪些partial mappings在未来组合中可安全互换”与“data placement不能由dataflow独占”的两条具体条件。Ch48/50既有交接未变可复用。15166建议typed space后1–2段：compatible tensor tile/dataflow/order/backing memory内才Pareto比较，reservation全lifetime先保留不确定分支再collapse；sum/max按树角色分开，optimal仅model-mapspace，搜索成本与实机不相混。15172建议紧接1–2段：显式storage node确定缓存位置/寿命，loop reorder不越storage node且partial relevance例外；symbolic currying再数值shape减少重复，维度未知/divisibility与解析model条件保留。二者不是同篇、彼此不继承证明；TPUv4-like/NVDLA-like、cached baseline估算/1000倍搜索预算与未测GPU kernel反侧邻近，旧局部autotune/backend照样合理。

## 15143 — Ch72 attribution 段，输出 trace 与学得行为分责

actual Ch72 L183/185与完整邻接175–196、末注4146，root已实际非作者POST通过；输出sensor与学生行为查询、有限proxy/误归因反侧俱在，Ch72窄锁释放。

实际读Ch72 L154–183（watermark confidentiality、soundness/forge/recovery）及Ch71出口/73开头，source形态与密码责任已有，但没有“teacher当前最终答复不变 vs student transfer/学得trigger不同”这条trace-distillation接口。建议在watermark生命周期段后1–2段：输出trace可以保留最终答案却改变学生可学性；若在trace上植trigger，检测对象是学生对查询的行为，非原输出token detector。不得把答对等同trace全部语义保持，有限代理学生/未知蒸馏方法边界、K5/K20和false attribution反侧近正文；这不是15323密码不可伪造，也不授蒸馏权利或防侵权。Rewrite/proxy搜索/query成本与provenance/control旧路径保留。需要root比较是否真缺口，不因两种watermark名字不同就写。

## 15195 — PLATFORM-EVALUATION-SYSTEM / Ch66 已有覆盖建议

root已独立核精确v1五SVD/400bank/49+48测试计数及bank/adaptive反侧，并实际核Ch66 L215–223：已有覆盖通过，无书改。97%与2%FPR按原计数，不采用under2%宣传，未复现。

实际读Ch66 L187–247，其中L215–223已具体解释adapter制造方法和训练/test人口改变谱/方向分类、静态sensor不能占行为验收、cross-method holdout、独立judge/生成与release Gate。15195v1五种SVD统计和有限Llama3.2-3B/rank16/layer21新实例未改变这条现有论点，97%/2%FPR与adaptive energy spread/benign bank drift恰落在其sensor边界。建议已有覆盖引用这一实际段，不追加SVD配方；不存在生产证书，当前v3不采用。Ch65/67开头已实际读交接。

## 15189 — PLATFORM-EVALUATION-SYSTEM / Ch66 已有覆盖建议

root已独立核opt-in/schema-hash、2714eval再生成labels及关键反侧，并实际核Ch66 L49–77五层success/缺truth：已有覆盖通过，无书改。GPT5nano再生成不是人工独立gold，未复现。

实际读Ch66 L49–77五层成功事件及L187–247完整对象。它已明确contract/schema成功不等semantic quality/outcome，ground truth不可即时取得时区分judge/human/provenance；本篇schema keyF1高而value较低与telemetry opt-in/hash降重人口不授工业准确率，支持现有分责。建议已有覆盖指L49–77，不把工业数据新规模/阈值写成长期常数，不追加一套抽取框架。邻Ch65/67开头已读；父审若认为反侧还改变其他具体论点再窄比较。

## 15198 — Ch72 coalition effect 的 reference 分责

actual Ch72 L716/718与完整邻接709–733、末注4148，root已实际非作者POST通过；task-defined utility/reference与overall/coalition impact分账落实，Ch72窄锁释放。

实际读Ch72 L63–87 coalition search、L685–718 CoT/communication faithful≠real effect；现有实际承载日志不能自证安全，却没把task-defined nominal objective、no-collusion协议reference与coalition/overall regret分别作为可观测对照。建议CoT monitor段后1–2段：冻结task variables/utility/action log后计算相对reference的整体和coalition影响，明示理想Fstar与实现reference不同，judge识别intent与环境advantage分账。只在目标/约束里编码的privacy等可测，违法nominal objective不获伦理真值；single-backbone synthetic channels、seeds和规模迁移未验，counterfactual/protocol成本近正文，原人工scenario及最小权限保留。安全必要源深入已完成，未授自然串谋率/通用检测器。

## 15206 — TRAIN-RLHF / Ch31 feedback likelihood 差额

actual Ch31 L690/692及邻接676–706、末注1274，root已实际非作者POST通过，释放该段窄锁。

实际读Ch31 L674–716人口/rater/迟到反馈及31后训练交接、相邻Ch30/32开头。现有rater offset/time不同，并未承载把preference/demo/ordinal rating/stopping censor写成共享latent reward的不同观测模型。建议Human feedback后/rater heterogeneity前1–2段：异质type不能直接同尺度加总，分开BT/BoltzQ/ordinal/hazard并条件化latent reward；条件独立及right censor责任明确。合并反馈总量更多、synthetic knownQ/reward与相同likelihood family、CartPole退步、EPIC非cardinal真值、perturbed dynamics重训policy反侧近正文，不外推LLM真实人反馈或迟到queue。错误likelihood/人口相关时回退各type独立校准与可信偏好监督。

## 15260 — TRAIN-RLHF / Ch31 prefix OPD 差额

实际Ch31 L799/801、完整邻接791–813及末注1276，47倍已纠正为compute-to-target GPU FLOPs而非时间，root窄POST通过，锁释放。

实际读Ch31 L787–816 policy-induced state、L900–926 teacher/no truth与loop；原文解释full trajectory on-policy覆盖，却无早停prefix仅监督头部与渐长schedule的容量/尾部损失取舍。建议state distribution后1–2段：student只生成前L后停止，teacher/scoring/backward都只消费前缀，部署解码不cap；sample RKL条件同vocab/base格式，短prefix不保证完整tail。1.7B OOD GPQA/MMLU差于base、AIME24 dev与test复用、SeqKD不同teacher/budget、47倍compute-to-target/FLOPs估算、GPUhours另报及未计SeqKD离线生成近正文，§8安全只是风险推断不当实测。回退full OPD/SFT或逐渐延长，保留tail/refusal/calibration独立回归；不授部署安全。

## 15210 — TRAIN-DATA / Ch27 跨语言 curation 条件

实际Ch27 L1245/1247、完整邻接1233–1255及末注1486，root非作者POST通过，锁释放。

实际读Ch27 L1231–1249词典干预/parallel-code-switch类型、Ch26出口/28开头。既有语料类型与干预，不包含“固定bilingual50:50及budget，提升一侧语料质量可同时惠及另一侧”的具体条件反证；不能由追加非英一律推英语容量损害，也不能从数量gain推无interference。建议该双语段后1–2段：quality和mix ratio分别匹配，固定3B60B的双向transfer12/13及Bengali反侧、语言距离仅相关；translation是否益依赖源quality。未披露完整recipe、所谓uncurated已有上游filter，1T compound curriculum/跨model4–10倍预算不授curation因果；过滤/合成成本和保守mixture、逐语种回归保留。

## 15257 — MODEL-LONG-CONTEXT / Ch22 页标识接口

实际Ch22 L201/203、完整邻接195–211及末注1294，344K窗口/336页和artifact/budget已分清，root非作者POST通过，锁释放。

实际读Ch22 L99–151 effective retrieval/source span与L179–203位置/多模态数据；邻Ch21/23开头。已有标称长度不保证使用和多模态continued training合同，但未解释page IDs只eval添加可能坏、必须train与infer相同页面接口的受限对照。建议multimodal longcontext段后1–2段：页数、视觉resolution、document span分布与page-ID serialization共同identity；只增最大窗口/只推理插标识不等有效context扩展。Table5 eval-only退而train+eval益、short/longstage不匹配resolution/SP/预算，mergedartifact及recursive teacher/CPT跨任务反侧保留。MMLongBenchDoc-C修题251删16改变task/evaluator版本，在本日证据注明而不将旧新分数直接比较；这条版本责任Ch66已有，不重复写第二owner。额外训练与编码成本、回退较短窗口/检索与已有页表示；不授全document正确性/生产成本。
