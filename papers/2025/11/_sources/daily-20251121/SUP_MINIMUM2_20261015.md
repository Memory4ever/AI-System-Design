# Nov21 七个相关标题的决定域

作者Noether；仅处理[标题包](SUP_ARXIV_TITLE_20261015.md)七M，不重已过五M或全池Methods。以下是作者实际读原文后的6P1C提案，请root转Ohm核；不预签独核、日期、评分、Evidence或Books。

## 1. 15383 MRO：窄P

[精确v1 HTML](SUP_CORE_2511.15383_20261015.html) §3.1–3.2，投影块42–69实际读。索引只嵌入稳定ATA层级/任务题名、不嵌入变动程序正文；LLM只重排top50索引，程序仍在certified OEM viewer消费并保原ID/preview，JSON无效回退dense。这不是让模型生成维修步骤：内容授权消费与可变派生检索分开，索引稳定性条件改变“把完整手册持续嵌入”的设计选择，足以保留窄P。未证明索引到当前revision的强校验/拒绝，也不把有效JSON当无幻觉/合规证明；10人/200queries等自报比较不采用普遍速度或安全结论。无需全手册/全部实验。

## 2. 15408 NAMeGEn：窄P

[精确v1](SUP_CORE_2511.15408_20261015.html) §III-B/C、Algorithm1/2，实际块50–77及66–76窄回读。隐式目标先accuracy规则，再completeness/clarity聚合；通过IIO才按用户显式目标权重评价，显隐式历史分开；预算内阈值随迭代松弛、最终取历史候选。具体增量是不同目标消费者的先后gate、历史和有限预算停止，而非“LLM命名有反馈”泛循环；故P。不采formal Pareto optimal、用户偏好已准确识别或衰减阈值通用有效；未把warmup边界配方无歧义作为已证明事实，不遍历CBNames全部数据。

## 3. 15424 MemCluster：窄P

[精确v1](SUP_CORE_2511.15424_20261015.html) 方法块57–101实际读：单次LLM输出label/可选merge，runtime更新label集并把历史所有assignment回溯映射；达到Kmax切strict prompt，否则relaxed，Kmin只入context。增量是merge须联动已派生历史状态及提示模式条件，不只是“有memory”；P。提示词不保证K范围，merge一致性不等语义正确；每merge O(i)不能推出总线性，最坏及上下文增长仍在，不采用通用复杂度/正确性保证。

## 4. 15552 Mera：窄P，原响应部分

[精确v1局部HTML](SUP_CORE_2511.15552_20261015.html) receipt HTTP200但curl28、1033529/1260440bytes，**不是全文成功**。已实际读到的§3.3/3.4块172–231足以决定本门：attempted-score A在已尝试任务/模态重归一、coverage C分开，T=A*C，不把未测模态等同低质量；十prompt变体及trained judge是评价消费者而不是真值。MSMIA用原样本与语义扰动邻居、original模型与注入泄漏fine-tuned模型作条件测试，AudioSeal与图像/video可见overlay角色不同。具体评价人口/质量与污染探针条件可以修正只看榜分的解释，故窄P；十八任务或俄语资源本身不足。未授公平排名、membership取证、无泄漏、所有水印不可见/鲁棒或license法律保证，不需补全全部数据集。

## 5. 15976 TOD-ProcBench：窄P

HTML404不冒正文；[PDF](SUP_CORE_2511.15976_20261015.pdf)200/853725bytes，实际通过[原PDF文本调用](SUP_WEB_TOD_20261015.raw)读§3.2–3.5/4.1–4.3必要域（L143–201、209–239、283–380）。三格式在条件/动作结构上变换，测试把instruction retrieval与next action分账；反例将参数或branch动作替换后最小改写响应，再做不蕴含检查与人工筛选。相同工作流动作不代表细条件遵从，且先归因instruction再比对不自动改善判定；这是一条具体评价盲区P，不仅新增TOD任务。人核基底、后续格式/语言LLM judge及生成任务同族judge角色不互相替代；不采所有协议等价、普遍合规能力/结果数字或生产安全。无需全部34页附件。

## 6. 16198 SemanticCite：C贡献

[精确v1](SUP_CORE_2511.16198_20261015.html) 实际读§3.1–3.5、4.1–4.4（块80–128、140–190）。实现为BM25+dense→FlashRank top3、512char/50overlap、LLM四类及结构化理由/证据、Qwen3 QLoRA蒸馏，未见相对现成RAG/分类的新选择或可核有效条件。UNCERTAIN与PARTIAL标签有用但标签本身不构成新机制；把uncertain编码成ordinal0的评价选择及GPT标签不是真值，也不能据此替作者发明新贡献。按实际方法判C，不因citation科研工具误归Science，也不因无大规模实验关闭。无需再追不影响处置的公开日期。

## 7. 15807 TopoReformer：窄P及安全反侧

[精确v1](SUP_CORE_2511.15807_20261015.html) 方法/评价块55–99实际读。TopoAE在input/latent两侧pairing距离约束上保结构；Reformer的reconstruction/classifier/KL与latent辅助支路要避免decoder/下游分类器manifold错配，训练先冻结后放开；这是一条可核的表示/优化条件，不因MNIST/OCR直接范围C。消费者仍是局部图像分类/OCR，word purification失败需拆字符/重组，OCR为效率省去Reformer；不能拿完整图示当所有消费者实际pipeline。BPDA残余ASR81/84%的反侧与EOT条件保留，不授model-agnostic或普遍防御/LLM安全保证，不读取/执行攻击payload。

## 8. 合并权限与已发生复用

首33五M已Ohm12/root实际闭合为32P1C；本七门若通过，标题21为18P3C，新54为50P4C，无minimum待办。这个算式仅题摘/必要贡献门，不是54当窗候选或Methods Evidence。Ohm13已核标题两C/必要安全方向；Ohm14 current22的两C/恢复身份及必要安全分层样本、Ohm15 Illusion v3 A.1五问答实际读，可按该层消费，不再要求其全Methods/双版全文。Illusion长度/采样/人口/算法/工具权限分别记账，v3history不是Nov20公开，亦不声称五回应均为首次新加。CVE Ohm7 OnlyReport与Nano旧有效core均不重。剩余已观察12 current完整题摘/必要日期及six继续，不因本包等待停工。

## 9. 实际Ohm17后的限定同步

Ohm17已真实核本七门6P1C，54题摘50P4C的贡献层可消费，不再挂minimum普通项。NAMeGEn Eq7/8 warmup等号与j_imp/j_exp更新未闭，不授完整动态配方。MERA A/C分账可解释不同缺测/质量原因，但不能把这一点说成总分无需缺测零贡献：Ohm实际读Eq2–4后推得T=(1/M)Σ_m(1/n_m)Σ_attempted score，未尝试项总分仍贡献0；此是reader代数推论而非作者新实验。增加未测任务也会改n_m/模态权重，A并非对任意任务增删不变。保留具体污染探针的受限P，不用该夸大性质加分/保证。此行政与限定同步不重原文或重复请求POST/DAY。
