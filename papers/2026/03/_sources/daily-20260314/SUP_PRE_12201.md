# IndexCache 非 root 实际必要 Source / 逐字 PRE

mar14_supplement，2026-10-09。root为必要Source/PRE提案者。作者本次实际读精确v1缓存 `SUP_CORE_12201.raw`：§2–4/B42–183、Tables1–4、AppC/B278–303及AppD/B304–305；原件200/274826B与执行时刻在 `SUP_INDEXCACHE_MANIFEST_RESULT.json`。不遍历artifact/PDF/全版本。

与root裁决一致：F是完整indexer而非full attention，S复用最近前方F的topk索引，各层自己的KV不共享/删除；首层F。固定SFT校准batch768/context200K全模型LM-loss greedy只局部，不是全局最优；pipeline-block首层F/顺次commit是额外近似，n²indexer成本未全部变linear。Cross-layer KL平均target梯度命题需要目标固定且只有q含参数，不扩到joint sparse训练全参数/充分每层token。Table2 1/4search GW47.4<49.6、LCB70<71.4；1/8 Long46.1<50.2。Table3目标平均也有GPQA76.7<79.4，缩短训练1K+4K不等full原训练；Table4 GLM5 preliminary也有GW90.3<92.7，不能说全部无损。AppC DP相似度代理50.7→49.8反退，该表原DSA54.0，未将不同人口均值合并；local cosine失效解释只保留author假设、不授已隔离唯一机制。

Serving dp_attention/dp8 H100与single-request/fullKV~800K/GPU不混为同concurrency，输出长度/精度/在线SLO未充分，机制正文不采用速度比。D temperature1/top-p.95/top-k40、200K含32K输出，MRCR/GW只可容纳人口、其余middle truncation分别记；所有model/task/ratio共同质量验收，未核实现/复现。

实际独读Ch45连续175–212（首次输出中间被截后重新完整187–202补齐），Ch44/46入口与Ch14 120–136、Ch22 309–340。现有2602.04541是dense head map/HardKuma teacher/固定role继承；虽已经有索引身份与不删KV，但不等独立DSA indexer的Full/Shared layer plan、LM loss替代cosine refresh定位或shared indexer多服务层目标。root逐字两段的具体差额、代价、身份与回退成立，唯一owner `INFER-KV-CACHE` Ch45，不重复DSA基础。2+2+2=6，实际必要Source与两段PRE通过，root可据proposal窄写；我再真实POST新增/完整邻接/本人末注。未授实际写入或DAY。
