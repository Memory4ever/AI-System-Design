# DAY 复核后的定点恢复

2026-10-07，root要求修正可执行来源范围；没有扩大论文题摘池或全文审阅。

## MiMo

独立提取 `daily-20250701/mimo.raw` 中 `id="paper"` 至 `id="blog"` 原HTML Paper列表，共8条：

| 原始题名 | 原日期字段 |
| --- | --- |
| MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training | June 29, 2026 |
| ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning | March 13, 2026 |
| HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing | February 3, 2026 |
| MiMo-V2-Flash Technical Report | January 8, 2026 |
| Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers | October 21, 2025 |
| MiMo-Audio: Audio Language Models are Few-Shot Learners | September 19, 2025 |
| MiMo-VL Technical Report | June 4, 2025 |
| MiMo: Unlocking the Reasoning Potential of Language Model – From Pretraining to Posttraining | May 12, 2025 |

现存日期有序Paper列表从Sep19跨至June4，不含本窗。前稿误将整页当前介绍当作没有历史Paper，现已修正。这里只检查目录的时间边界，不把窗外题名变成题摘队列。Blog历史payload仍未恢复，不作全站零事件。

## DeepMind

一次使用真实路径 [page5](https://deepmind.google/blog/page/5/)、[page6](https://deepmind.google/blog/page/6/)，均已恢复，见 [原工具文本](./deepmind-pages.txt)。page5自Nov2025到Jul2025，page6自Jul2025到Apr2025，止于本窗下界之后的June条目已越过。

page6相邻July/June边界是 MedGemma 与 Gemma3n developer guide。仅为日期核实打开边界原页：[MedGemma](https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/)显示 July 9, 2025；[Gemma3n](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/)显示 JUNE 26, 2025。因此现存有序Blog目录没有本窗条目，先前失败的 `?page=16` 不代表真路径失败。Google publications目录原请求超时仍隔离，不声称全部Google研究零事件。

## 硬件/编译/runtime

按 cs.AR/cs.PL/cs.OS/cs.PF 分类与 LLM/GPU/kernel/runtime/language/inference/compiler 主题，submitted Jul2～Jul3，start0/max_results20/升序做一次有界标题请求，读操作20秒超时，未取得条目。完整URL与错误保存在 [请求记录](./hardware-title-query.json)。这是已执行但访问受限的补检，不再写为未执行扫描；没有取得标题，也没有零命中结论。重开需要可读的该查询响应或本窗对应历史公开分类列表。

## Hunyuan

root在DAY协调中报告已做浏览器有限恢复、30秒初始化失败。本作者只亲自读取Research skeleton和替代Blog API，不将协调者恢复事实改写为本日浏览器成功核查。Research“全部”论文历史目录依旧隔离。
