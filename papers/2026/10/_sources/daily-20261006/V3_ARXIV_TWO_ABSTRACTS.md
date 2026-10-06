# 两个实际完整题摘：仅身份/筛选证据

原API `https://export.arxiv.org/api/query?id_list=2610.04721,2610.04740`；后续定点响应updated2026-10-06T01:23:33Z，2entries，不作为本窗first-public证明。初次观察已01:06:55Z，晚于01:00Z截点。没有扩大230宽线索。

## 2610.04740v1

Toward a Locally Deployable Agentic Co-Scientist: Small-Model Planning for Early-Stage Drug Discovery

Early-stage computational drug discovery requires coordinating heterogeneous scientific tools across multi-step workflows. We present a lightweight, tool-augmented framework in which a locally deployable compact language model plans calls to 18 modular tools. A Unified Molecular Schema maintains shared molecular records, while a plug-in interface supports tool replacement and extension. We construct 1,263 manually refined query-plan pairs through workflow-graph path coverage and apply LoRA fine-tuning to three compact model families. Under the query-level split, all fine-tuned models generate fully parseable and schema-compliant plans on 47 held-out cross-group queries. Llama 3.2-3B achieves a tool-selection F1 of 0.998, sequence exact match of 0.979, and argument F1 of 0.960. Under the stricter workflow-grouped split, which excludes identical ordered tool sequences across partitions, sequence exact match reaches 0.452 to 0.548, highlighting the remaining difficulty for compact models in generating complete workflow paths unseen during training. These results demonstrate the feasibility of compact, locally deployable planning while identifying compositional generalization as an important direction for further improvement.

处置：药物发现工作流暂缓范围，排除，不为不影响结论的公开时间另追。API published字段2026-10-03T20:09:34Z为提交字段，不能借作窗内公开。

## 2610.04721v1

Knossos and Ariadne: Benchmarking and Learning Complete Diagram Topology Extraction with Vision-Language Models

Structural diagrams are widely used to represent complex systems and relational information across scientific, engineering, procedural, and spatial domains. Recent vision-language models (VLMs) have become increasingly capable of recognizing diagram elements and reasoning about their content, while complete diagram topology extraction remains comparatively underexplored. In this paper, we study diagram-to-graph topology extraction: extracting all diagram entities and the complete relations among them. To enable large-scale supervised training and systematic evaluation of this task, we introduce Knossos, a benchmark of 19,200 diagrams across six diverse domains, with 245,179 nodes and 439,740 edges. Its symbolic generation process provides exact alignment between rendered diagrams and annotations of complete topology, relation types, and connector geometry. To address the modeling challenge of complete topology extraction, we also present Ariadne, a structured framework that decomposes the task into node inventory extraction and source-conditioned edge prediction. Extensive experiments show that training on Knossos substantially improves complete topology extraction in smaller open-source VLMs. Ariadne further improves over one-step extraction under matched supervision, demonstrating the additional benefit of structured decomposition. It achieves the highest average Edge F1 among the evaluated methods on Knossos, while both backbone variants also improve over their unadapted counterparts on the real-world external benchmark. Code and benchmark are available at https://github.com/bangwayne/knossos_Ariadne_Public.

处置：matched监督下结构分解是局部潜力，不因benchmark排除。API published2026-10-03T19:20:33Z/native Submitted3Oct不能证明公开上界；保留具体日期身份，未评分/未入正式候选，未授Evidence或Books。
