# 2603.10978v1 GroundCount：最低必要增量与关闭提案

准备者 mar13_supplement；仅03-13既有日报的03-12 BJT自然日补充窗。不是正式候选/独核/DAY通过声明。原准入窄潜力及Mar12日级arxiv夹证有效复用，不重开已通过层；不以Submitted作公开日、不推全网无先稿。

## 身份与原件

[完整exact-v1题摘/history](./SUP_ABS3_10978.txt)：GroundCount: Grounding Vision-Language Models with Object Detection for Mitigating Counting Hallucinations，Boyuan Chen/Minghao Shao/Siddharth Garg/Ramesh Karri/Muhammad Shafique；唯一显示v1、无Comments撤回/纠错/具名先稿信号。DATE3已核created/registered Mar12T02:14:25、arxiv.content/findable与正常公告批次，可复用主独核§23日级，不用Updated身份推日期。

[官方精确v1 HTML原响应](./SUP_CORE_10978.raw)、[请求](./SUP_CORE_10978_MANIFEST.json)和[结果](./SUP_CORE_10978_MANIFEST_RESULT.json)：https://arxiv.org/html/2603.10978v1，GET200，212260 bytes，2026-10-10T03:53:30.161436Z。实际顺读§III-A–C/完整T1、§IV-A–D、§V-A–E/完整T2与§VI，§I/II核实际recipe与已有设计对照。图1–4只读正文/caption，不认证Fig4每格数字；未读取图片像素、运行代码/复现、或扩其他论文。

## 实际增量和最低评分

原视觉表示计数会失败→YOLOv13x检测转类别/index/3×3位置与confidence提示，另用FiLM/cross-attention/gating把局部及global CNN feature融合到ViT patch，及两者组合→需按具体VLM和检测阈值检验这一局部配置，而非默认训练融合更好或更多辅助字段一定有益。准入时的局部正反证据保留，不退为范围EX。

拟 **1+1+2=4**：D1是现成专用检测与提示/常见融合算子的局部实现配置及单任务比较，没有另一个新状态、训练目标或执行协议；不把成熟grounding、FiLM/cross-attention/融合可靠性原则给D2。R1是视觉计数局部负载，未建立索引、release或跨生命周期的新接口。Durability2是输入字段/检测阈值与consumer兼容性必须绑定的可复用配置资格，不因单benchmark或未复现扣为版本价值。实际新多模型切片保留；不能因Books已写主题或工作量降低评分。

## 必要支持与直接反侧

- §III/T1：PhD全benchmark33688 VQA/16844图像，binary yes/no；counting子集本次必要段未给独立数量，不能把全量作本计数人口。五≤4B模型、greedy、float32、1024输出/思考budget；SEC/ICC/CCS分开，CCS753生成图/1506QA不是真实图同人口。更强/更弱按此baseline切片不是已证架构类型定律。
- §IV：YOLOv13x confidence≥.5，bbox中心离散3×3，先水平左到右再垂直下到上；检测类别/index提供显式实例信息，不认证为真值。融合训练使用COCO train2017的GT bbox生成目标文本（非未知标签自监督）；最多40k steps，batch1、AdamW 2e-5/cosine，best checkpoint选择。GT训练和runtime detector误差是不同输入身份。
- 完整T2：Ovis2.5 baseline74.7/10s→PlanA81.3/7.8s；fusion-only75.2/17.8s，B2 72.7/14.6s、B3 71.4/4.3s都退步，B4 78/7.7s，组合C78.2/4.8s。不认证所有fusion更差/更好，也不把不等训练、checkpoint选择与推理输出长度归因于唯一融合算子。正文说减少幻觉循环是解释，示例不隔离所有原因。
- §V-B/D的实际文字：四模型不呈confidence值时改善.1–4.8pp，Ovis反降.7；位置删除在两较强baseline下退步而其余三改善。InternVL3.5 full64→62.5，迭代反思被扰是作者可能解释，不是已证架构因果。LowThreshold .5→.3在此五模型都退步/更慢，不等所有检测域precision必比recall重要。只采用上述正文有限对照，不以未视觉核Fig4授每格结果。
- §V-C：ODM-only72.8/.1s，PlanA81.3不证明所有新能力源于VLM、无信息泄漏或真值独立；检测器和VLM接收同图，但高层binary判断/组合与纯检测baseline接口不同，精确ODM答案读出必要正文未完整规定。没有把82%认证为通用消幻觉。
- A10080GB、float32、局部mean时长披露；YOLO .1s与推理时间账是否完整一致/预处理、缓存、训练搜索、峰值内存、重复seed/CI、并发/SLO与旁侧任务质量在必要段Not Disclosed。论文未来缓存/不同detector/更多预训练不当已实现或阻塞最低关闭。

## Books：仅报告/不进一步采用，0新增

ROADMAP唯一可能owner `MULTIMODAL-REPRESENTATION` [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。实际读16–43 raw/coordinate/source身份、93–119 readout/空间细节/grounding与副作用完整相关局部：现文具体区分专用readout/显式坐标和原输出，按任务、旁侧质量/费用选择；不以热图或detector阴性签真值。本文新计数数据没有被吸收，不签“具体已有覆盖新实验”。这次保留的是局部三recipe/字段消融结果，未构成新的长期机制或需纠正现文的强因果证据，故拟仅报告/不进一步采用，而非强NC、不是因无owner关闭。

最低关闭理由已由身份、日期、原准入与必要core/直接反侧支持；不请求更多图、附件或实现才结束。本项等非准备者独核后才能正式列为已关闭4分/仅报告Books0。将来若要采用通用位置/置信字段选择、全任务收益或架构因果，需相应独立配置/阈值人口与可比总成本，只重开相应命题；目前这些非拟采用事实不造成外部材料终态。
