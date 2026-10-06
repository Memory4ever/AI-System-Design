# HySparse 必要证据与具体 owner PRE

身份：2602.03560v1，MiMo官方Paper目录Feb3日历落新增自然日。root已实际首批准入/评分2+2+2=6通过；以下仍待非作者Source/Books核实。

实际读v1 §3.1–3.3/Eq3–9/Algo1、§4.1/Tables1–4及§4.4、§5，原件为supplement-hysparsecore/core2/hysparselimit。STOP：机制、关键对照与直接反侧足够，未遍历references或其他版本/代码，未复现实验。

机制：full层对每query输出block max probability（64token块，Top1024token→16block），GQA同组max共享indices；后N层以本层query读取源full-layer KV。SWA=128另保本层局部KV，sigmoid gate融合两支；是需训练的混合架构，oracle仅指源full attention，不是未来信息或真实任务重要性。保full历史仅少数层存，不靠永久删除未选token取得各层状态减少。

关键评价：7B 36层1:3、32Q/8KV、1T@8192再200B@32768、BF16；80B-A3B 49层1:11、64Q/4KV、500B@32768。比较Full、同ratio的HybridSWA与HySparse，MoE full另用gated attention。作者Table3 80B16k整体HySparse90.6<Full93.6，多个切片及Table2任务退步，否定摘要across-all。Table4仅7B，局部SWA加入五项中MMLU57.1→56.1反退；SA-only共享比SA+SWA共享五项改善，支持分权但不证明local/global表征解释唯一因果。硬件、batch/concurrency、serving precision/SLO、TTFT/TPOT和端到端代价Not Disclosed，不将“近10x KV”当部署速度或全系统容量；offloading只§5 future work。未披露重复运行不授统计普遍优势。

Algo1 line16把logit max减rowmax再除normalizer，缺Eq3所需exp，不能当可执行校准probability；该共同单query正仿射仍可保TopK排序，但不采用原式数值作为概率证书，也不声称kernel实现核过。原文没有轻量纠错标记，保此冲突，不改分或撤准入。

Books上下文已读当前ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、相关LS路由、Ch22局部正文完整邻接及开头/末注、Ch21/Ch23交接。拟已有覆盖唯一MODEL-LONG-CONTEXT，books/part-02-model/22-long-context.md“选择器的成本如何摊薄：刷新、复用与地址状态”：当前396第一段明确少数full layers产出block scores/global KV供后续层共享、layer-local sliding-window KV维持局部representation；后面ownership轴和更粗复用导致stale selection/head imbalance/index error，短context/迁移风险仍保dense/full+window。后续HySparse2两段明确训练结构/非checkpoint任意删层与独立window回退。本次采用的源/消费、全局/局部分工已在具体正文，1247源注只身份辅助，不作为No Change依据；无需Books新写。

拟§4只记录这些有限作者证据与Alg1冲突，Books已有覆盖，不在书内追加一份同机制摘要或benchmark清单。请root实际必要源及Ch22具体正文/邻接PRE核查，若认为局部共享反侧未被正文承载，提出窄差额再协调锁，不自行写共享Books。
