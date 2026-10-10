# Oct02 Google Pubs 窄恢复

作者Helmholtz / Codex；root首校准指定这两个可用入口，2026-10-07实际执行。仅本日补充窗口2025-10-01，旧默认页和原件不覆盖，不重抓其他来源/21 v1，不读234库存，不写Books/Git。

| 入口与原件 | 实际请求UTC / 响应 | 返回、实际读取与停止 | 权限限制 |
| --- | --- | --- | --- |
| [category=2025 & search=language model](https://research.google/pubs/?category=2025&search=language%20model)；[raw](./supplement-20261007/google-pubs-root-delta-language-2025.raw)、[请求](./supplement-20261007/google-pubs-root-delta-language-2025.request.json) | 11:10:07.491734～11:10:11.033567；HTTP200，366460 bytes，final URL同请求 | 服务端1–15 of 37 publications；15唯一title/detail URL已读，均目录年份2025。页面1/3、data-max-pages=3，有下一页2与末页3；**停在第一页，后22条及页2/3未取** | 年份是publication目录口径，不是首次公开日期；年度facet678不是命中数。首15的预览摘要随机械提取显示，部分文字读到，但没有逐项准入裁决/精确版本核验；没有把37或678变本日题摘/全文队列，也未进详情页 |
| [search=2025-10-01](https://research.google/pubs/?search=2025-10-01)；[raw](./supplement-20261007/google-pubs-root-delta-date-20251001.raw)、[请求](./supplement-20261007/google-pubs-root-delta-date-20251001.request.json) | 11:10:11.074748～11:10:13.739789；HTTP200，241637 bytes，final URL同请求 | 服务端0–0 of 0 publications / No Results Found，无row-card，停止该响应，未转Scholar | **这是字符串搜索，不是官方公开日期过滤**。零字符串命中不等10/01零事件，不与默认页空目标共同证明历史覆盖 |

两请求的bytes/SHA256与独占raw已核；无403/404/timeout，不登记访问故障。只追加6份raw/request/txt，原85响应不变，现本轮累计87 HTTP（84个200、2个404、1个403）。本次没有增加确定当窗候选；Google Segmenter仍由另一个实际10/01公告日证据和原有效core支持，不以Pubs字符串搜索授日期。

## 首15目录身份

以下仅是实际返回身份及目录年份，不逐项关闭/评分，不将后续期刊会议收录当首次公开；未打开这些详情或做跨日报扫描。

1. [Toward expert-level medical question answering with large language models](https://research.google/pubs/towards-physician-level-medical-question-answering-with-large-language-models/)
2. [Towards accurate differential diagnosis with large language models](https://research.google/pubs/towards-accurate-differential-diagnosis-with-large-language-models/)
3. [Gemini & Physical World: Large Language Models Can Estimate the Intensity of Earthquake Shaking from Multi-Modal Social Media Posts](https://research.google/pubs/gemini-physical-world-large-language-models-can-estimate-the-intensity-of-earthquake-shaking-from-multi-modal-social-media-posts/)
4. [SSDTrain: Faster Large Language Model Training Using SSD-Based Activation Offloading](https://research.google/pubs/ssdtrain-faster-large-language-model-training-using-ssd-based-activation-offloading/)
5. [A Scalable Framework for Evaluating Health Language Models](https://research.google/pubs/a-scalable-framework-for-evaluating-health-language-models/)
6. [Astute RAG: Overcoming Imperfect Retrieval Augmentation and Knowledge Conflicts for Large Language Models](https://research.google/pubs/astute-rag-overcoming-imperfect-retrieval-augmentation-and-knowledge-conflicts-for-large-language-models/)
7. [Synthetic Text Generation for Training Large Language Models (LLMs) via Gradient Matching](https://research.google/pubs/synthetic-text-generation-for-training-large-language-models-llms-via-gradient-matching/)
8. [A personal health large language model for sleep and fitness coaching](https://research.google/pubs/a-personal-health-large-language-model-for-sleep-and-fitness-coaching/)
9. [Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models](https://research.google/pubs/crosslingual-capabilities-and-knowledge-barriers-in-multilingual-large-language-models/)
10. [Synthesizing and Adapting Error Correction Data for Mobile Large Language Model Applications](https://research.google/pubs/synthesizing-and-adapting-error-correction-data-for-mobile-large-language-model-applications/)
11. [The Role of Outgoing Connection Heterogeneity in Feedforward Layers of Large Language Models](https://research.google/pubs/the-role-of-outgoing-connection-heterogeneity-in-feedforward-layers-of-large-language-models/)
12. [Analyzing Similarity Metrics for Data Selection for Language Model Pretraining](https://research.google/pubs/analyzing-similarity-metrics-for-data-selection-for-language-model-pretraining/)
13. [HEART: Emotionally-driven test-time scaling of Language Models](https://research.google/pubs/heart-emotionally-driven-test-time-scaling-of-language-models/)
14. [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://research.google/pubs/plan-tuning-post-training-language-models-to-learn-step-by-step-planning-for-complex-problem-solving/)
15. [RADAR: Benchmarking Language Models on Imperfect Tabular Data](https://research.google/pubs/radar-benchmarking-language-models-on-imperfect-tabular-data/)

**覆盖修正：** 旧默认页不是目标历史覆盖证据；本次只支持上述两个检索切片实际可用和已读到的范围。剩余页未做是明确有界停止，不伪装外部故障，也不声称穷尽所有2025论文。具体目标公开日/事件到达后定点核身份和首次正文；不为证明无遗漏扩扫年份或其他日期。
