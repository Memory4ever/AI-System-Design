# 2603.10978v1：非准备者最低关闭复核

仅2026-03-13既有日报补充2026-03-12北京时间自然日；复核者 mar13_admission_review，不是准备者或Books writer。恢复时实际重读AGENTS及当前Research/Report/Prompt、Sources使用说明与Daily/arXiv范围、ROADMAP及本日README停点；LEARNING_STATE只作本日路由。既有完整题摘准入与§23日级arXiv事件日期有效复用，不重开日期、不继承异日材料。

## 原件与实际范围

实际读[准备包](./SUP_MINIMUM_10978.md)、[完整v1题摘/history](./SUP_ABS3_10978.txt)、[官方精确v1原件](./SUP_CORE_10978.raw)及[GET结果](./SUP_CORE_10978_MANIFEST_RESULT.json)。身份GroundCount: Grounding Vision-Language Models with Object Detection for Mitigating Counting Hallucinations，五位作者与题摘对应；官方URL `https://arxiv.org/html/2603.10978v1`，GET200、212260 bytes、2026-10-10T03:53:30.161436Z。当前题摘仅显示v1，无可见Comments撤回/纠错或具名先稿信号；不据提交日或无信号推全网从无先稿。

实际原件必要范围为完整§III-A–C、Table I、§IV-A–D、§V-A–E、完整Table II及§VI，图只读正文/caption，不签图4未视觉核的每格数字。实际顺读[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)开头representation identity 16–43、readout/空间细节/grounding 93–119完整相关局部；没有读取无关旧论文/图像像素/实现、全附录或运行复现。

## 逐项裁决

- **实际增量保留**：原计数输出会失败→YOLOv13x类别/实例index/3×3位置/confidence转提示，或local/global CNN特征与ViT patch作FiLM/cross-attention/gate融合，再比较组合→选择须依具体consumer与阈值，而不因融合更复杂或辅助字段更多就默认优于原路径。局部多模型正反结果是真实新增，不改成贡献EX。
- **4=1+1+2通过**：设计是现成检测器、提示与成熟融合算子的计数局部配置；未建立新执行协议、训练目标或跨生命周期状态接口。System Reach只限单任务组件选择，Durability保留阈值/字段与consumer兼容的配置资格。不给成熟grounding/融合原则额外贡献分，也不因工作量、单榜或Books有主题降分。
- **必要正侧具名保留**：Table II Ovis2.5 baseline74.7/10.0s，Plan A81.3/7.8s；B.1=75.2/17.8s、B.2=72.7/14.6s、B.3=71.4/4.3s、B.4=78.0/7.7s、C=78.2/4.8s。训练采用COCO train2017 GT bbox目标文本、最多40k steps、batch1、AdamW2e-5/cosine、best checkpoint；不是未知标签自监督或训练预算匹配的唯一算子因果。
- **直接反侧保留**：§V-B/D confidence移除四模型改善而Ovis下降.7pp；位置移除方向依模型不同；InternVL3.5 full64.0→62.5。阈值.5→.3在所测五模型计数准确率退步；正文所报时间增量以no-augmentation baseline比较，不授任意检测域precision优于recall。Table I能支持计数低准确率，但不能采§III“所有类别中计数上下文退步最陡”的泛称，例如Molmo attribute在icc下降70.1pp、大于counting34.3pp。
- **人口/费用边界通过**：PhD全33688QA/16844图不是本计数子集N；CCS753生成图/1506QA另人口。五≤4B、greedy/float32/1024 budget、A10080GB是所测条件。YOLO-only72.8/.1s不认证独立真值或全部VLM新能力。有限mean时长与输出变短解释不授全费用、唯一幻觉循环因果、并发/SLO、全任务质量保持；训练搜索、预处理/缓存与完整时账不补造。缓存/其他detector/更多预训练仅未来工作。

## Books与停止

**最低关闭/仅报告，Books0通过；不是NC。** Ch23已有专用readout、显式坐标与原输出的任务/费用边界，但本次不说新GroundCount实验已写入，也不以同主题作为覆盖证据。实际新增主要是有限三recipe与字段/阈值比较，尚不改变现有长期机制或提供应纠正现正文的强因果证据，故无需PRE/POST或Books写入。支持与直接反侧已足够最低关闭，不以缺未拟采用的通用证明延长审阅。

本文件只授此ID最低4分关闭的非准备者证据裁决，不授正式日报同步、实际Books验收或DAY；没有stage/commit/push。
