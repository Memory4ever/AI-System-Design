# 03/16 官方公共元数据与有界日期恢复

只保存本日实际返回/读取的目录字段与停止点，不复制任何其他Daily候选或判断。Seed type1/token20跨Feb25→Mar26，18/82，next40/has_moretrue；不遍历后页。后续定点纠正Blog入口为type2，本日实际一次请求返回14/total19、next空/has_morefalse，全部日期投影见[V3_SEED_BLOG_FINITE_FIELDS.json](./V3_SEED_BLOG_FINITE_FIELDS.json)，Feb16→Apr1夹窗，保留差额5项；下方type0旧空返回仅保留原始观察，不再作为Blog故障或覆盖依据。Hunyuan实际POST page1/size20/renderType0的11/11返回已读，不补把display/publishedAt当firstpublic。Qwen实际GET data.articles40/40无paginationkeys；displayextra.date+embeddedarticle:published_time全对读，最近Feb16Qwen3.5→Mar19MaxPreview；其中Feb14/Feb16、TTSJan2026/Mar2025、OmniMar30/Jan7字段冲突仍保留，均不落本窗，不 backfill correction。

## Seed实际返回
```text
{"url": "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=100&order_desc=false", "total": 82, "next": "40", "has_more": true, "rows": [{"id": 1992, "PublishDate": 1772020800000, "title": "veScale-FSDP: Flexible and High-Performance FSDP at Scale", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2602.22437"}]}, {"id": 1412, "PublishDate": 1772121600000, "title": "CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2602.24286"}]}, {"id": 1420, "PublishDate": 1772121600000, "title": "Steerable Instruction Following Coding Data Synthesis with Actor-Parametric Schema Co-Evolution", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2604.16322"}]}, {"id": 1411, "PublishDate": 1772294400000, "title": "How RL Unlocks the Aha Moment in Geometric Interleaved Reasoning", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.01070"}]}, {"id": 1607, "PublishDate": 1772294400000, "title": "Learn Hard Problems During RL with Reference Guided Fine-tuning", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.01223"}]}, {"id": 1644, "PublishDate": 1772380800000, "title": "Anatomy of the Modality Gap: Dissecting the Internal States of End-to-End Speech LLMs", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.01502"}]}, {"id": 1664, "PublishDate": 1772380800000, "title": "On the Residual Scaling of Looped Transformers: Stability and Transferability", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2606.18524"}]}, {"id": 1424, "PublishDate": 1773244800000, "title": "Permutation invariant multi-scale full quantum neural network wavefunction", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.12233"}]}, {"id": 1414, "PublishDate": 1773504000000, "title": "Disentangling Tensor Network States with Deep Neural Network", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.14425"}]}, {"id": 1426, "PublishDate": 1773590400000, "title": "Mixture-of-Depths Attention", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.15619"}]}, {"id": 1661, "PublishDate": 1773936000000, "title": " FlexTrain: Scalable Hybrid-Parallel Training with Elastic Resource Utilization and Consistent Accuracy", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://openreview.net/pdf?id=h2yhNcbwSL"}]}, {"id": 1407, "PublishDate": 1774022400000, "title": "Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.20616"}]}, {"id": 1337, "PublishDate": 1774195200000, "title": "Development and large-scale benchmarks of a protein-ligand absolute binding free energy toolkit", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.22274"}]}, {"id": 1334, "PublishDate": 1774281600000, "title": "SIMART: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.23386"}]}, {"id": 1428, "PublishDate": 1774281600000, "title": "UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.23500"}]}, {"id": 1606, "PublishDate": 1774368000000, "title": "TopoMesh: High-Fidelity Mesh Autoencoding via Topological Unification", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.24278"}]}, {"id": 1335, "PublishDate": 1774454400000, "title": "Towards Generalizable Robotic Data Flywheel: High-Dimensional Factorization and Composition", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.25583"}]}, {"id": 1336, "PublishDate": 1774454400000, "title": "Hessian-informed machine learning interatomic potential towards bridging theory and experiments", "slug": null, "links": [{"ExternalLinkType": 1, "Link": "https://arxiv.org/pdf/2603.25373"}]}]}
{"blog_type0": "https://seed.bytedance.com/api/get_article_list_v2?article_type=0&publish_year=2026&page_token=0&count=20&order_desc=false", "total": 0, "rows": 0, "has_more": false, "next": "", "BaseResp": {"StatusMessage": "success", "StatusCode": 0}}
```

## Hunyuan实际返回
```text
topkeys ['code', 'msg', 'data']
datakeys ['totalNum', 'list']
{"code": 0, "totalNum": 11, "rows": [{"id": 100119, "title": "Hy Image3.5 preview 发布：为专业创作提供高性价比模型", "publishedAt": 1789959110, "displayPublishTime": 1790006400}, {"id": 100116, "title": "当大模型强化学习走向规模化，Batch Size Scaling 有什么不一样？", "publishedAt": 1789749798, "displayPublishTime": 1790006400}, {"id": 100100, "title": "Hy4 preview 发布", "publishedAt": 1787896648, "displayPublishTime": 1787846400}, {"id": 100091, "title": "From LR to ELR: A Better Heuristic for Pretraining Dynamics", "publishedAt": 1786592588, "displayPublishTime": 1786377600}, {"id": 100087, "title": "Hyra: 简单有效的科学发现智能体", "publishedAt": 1784110327, "displayPublishTime": 1784599200}, {"id": 100064, "title": "Hy3 正式发布", "publishedAt": 1782959528, "displayPublishTime": 1783320600}, {"id": 100041, "title": "Hy-MT2：面向实际应用场景的高性能多语言翻译模型", "publishedAt": 1779340747, "displayPublishTime": 1779346800}, {"id": 100039, "title": "Real life is where context gets hard", "publishedAt": 1777228775, "displayPublishTime": 1777532400}, {"id": 100061, "title": "Hy3 preview : 混元大模型重建的第一步", "publishedAt": 1782308557, "displayPublishTime": 1776873600}, {"id": 100015, "title": "Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping", "publishedAt": 1770971794, "displayPublishTime": 1770971794}, {"id": 100025, "title": "Learning from context is harder than we thought", "publishedAt": 1770092288, "displayPublishTime": 1770092288}]}
```

## Anthropic Research实际March publishedOn邻接
默认urllib403后curl普通UA成功317670bytes，publishedOn174match；仅提取March fields。Mar13T10:15 diff-tool→Mar23T23:00 science/long-running/vibe，跨本窗，无identified当窗条目；不是全机构历史无遗漏。
```text
bytes 317670 matches 174
nvestigation, code inspection, finding bugs, code examination\",\"name\":\"Object CodeMagnifier\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-31T22:17:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"how-australia-uses-claude\"},\"subjects\":[{\"_key\":\"economic-research\",\"_type\":\"tag\",\"label\":\"Economics\",\"value\":\"economic-researc
g\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":{\"backgroundColor\":null,\"illustration\":null},\"publishedOn\":\"2026-03-24T10:41:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"economic-index-march-2026-report\"},\"subjects\":[{\"_key\":\"economic-research\",\"_type\":\"tag\",\"label\":\"Economics\",\"value\":\"economic-
1000x1000.svg\",\"width\":1000},\"keywords\":\"Head, nodes\",\"name\":\"Node-Head-Constellation\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-23T23:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"introducing-anthropic-science\"},\"subjects\":[{\"_key\":\"science\",\"_type\":\"tag\",\"label\":\"Science\",\"value\":\"science\"}],\"summary\":
361111949b32136a308ef35b6864-1000x1000.svg\",\"width\":1000},\"name\":\"Object Hourglass Cosmic\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-23T23:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"long-running-Claude\"},\"subjects\":[{\"_key\":\"science\",\"_type\":\"tag\",\"label\":\"Science\",\"value\":\"science\"}],\"summary\":\"A practi
th\":1000},\"keywords\":\"Hero illustration: Hand HeadNodeThink\",\"name\":\"Hand HeadNodeThink\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-23T23:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"vibe-physics\"},\"subjects\":[{\"_key\":\"science\",\"_type\":\"tag\",\"label\":\"Science\",\"value\":\"science\"}],\"summary\":\"Can AI do theor
g\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":{\"backgroundColor\":null,\"illustration\":null},\"publishedOn\":\"2026-03-13T10:15:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"diff-tool\"},\"subjects\":[{\"_key\":\"interpretability\",\"_type\":\"tag\",\"label\":\"Interpretability\",\"value\":\"interpretability\"}],\"sum
puting, technology, work computer, office setup, computer interface\",\"name\":\"Object Desktop\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-06T10:30:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"mozilla-firefox-security\"},\"subjects\":[{\"_key\":\"policy\",\"_type\":\"tag\",\"label\":\"Policy\",\"value\":\"policy\"},{\"_key\":\"frontier-
ies\":[{\"_key\":\"research\",\"_type\":\"tag\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":null,\"publishedOn\":\"2026-03-06T00:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"exploit\"},\"subjects\":[{\"_key\":\"frontier-red-team\",\"_type\":\"tag\",\"label\":\"Frontier Red Team\",\"value\":\"frontier-red-team\"}],\"su
g\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":{\"backgroundColor\":null,\"illustration\":null},\"publishedOn\":\"2026-03-05T19:59:21.508Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"labor-market-impacts\"},\"subjects\":[{\"_key\":\"economic-research\",\"_type\":\"tag\",\"label\":\"Economics\",\"value\":\"economic-research\"}]
```

## arXiv实际cs.DC月目录定位
仅定位首8日期恢复，不按346个分类条目审阅。
```text
bytes 578820 headers ['Distributed, Parallel, and Cluster Computing', 'Authors and titles for March 2026 ']
12465 Learning (cs.LG)
         

       
     
     
       [110] 
       
        arXiv:2603.12465
       
      
        [ pdf ,  html , <a href="/format/2603.
13019 g (cs.DC) 
         

       
     
     
       [113] 
       
        arXiv:2603.13019
       
      
        [ pdf ,  html , <a href="/format/2603.
12831 ineering (cs.SE)
         

       
     
     
       [112] 
       
        arXiv:2603.12831
       
      
        [ pdf ,  html , <a href="/format/2603.
12520 not in category
12933 not in category
13110 not in category
12440 g (cs.DC) 
         

       
     
     
       [109] 
       
        arXiv:2603.12440
       
      
        [ pdf ,  html , <a href="/format/2603.
12614 not in category
listlinks ['https://arxiv.org/search/cs?searchtype=author&amp;query=McAllister,+J']
```
月列表只有月份heading，无分日announcement header；4/8身份本分类找到，其他4不在cs.DC。这次有效成功不恢复小时。API Updated(v1)无已证公开语义，DataCite findable upper晚09，不能推nextday；需要真实SundayMar15公告相关段/相同ID早于本窗右端的官方可公开证据。有限恢复到此停止，未扩大全月公告实现考古。
