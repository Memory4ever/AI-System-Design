# Swarm17803：必要原证/具体差额与有限PRE

仅03-20补03-19自然日，resume_mar17准备，不写Books；root完整exact-v1题摘准入已复用，2+2+2=6保留。日级夹证原值见SUP_FIRST_DATE_FIELDS：18日14:59Z提交/最早公告19日08BJT→registered19日02:40:56Z，均落19自然日；此为primary组合日级推断，未补确时。无当前纠错/撤回说明，v1唯一。Source/PRE未授独核或safe。

## 已实际读必要原证及停止

[exact-v1 HTML](https://arxiv.org/html/2603.17803v1)，§3–8（尤其5.1/Eq2–5/Alg1、5.2/Eq6–7、6/Eq8–9、7、8.1–8.4/T2–5），支持/关键反側够即停，不核repo、全部图拟合或旧版本。

稀疏attention选出的KV会共访，单SSD即使少读bytes仍有I/O带宽瓶颈。作者offline profile pair frequencies→clusters/medoids，多cluster允许KV复制；各cluster成员跨多SSD循环条带，DRAM留medoids+route table/localwindow/hotclusters。runtime query对DRAMmedoid选cluster；取回先union激活clusters，减去DRAM已有entry，再将低replication-degree entry先分配，单副本固定SSD、多副本交给当前最小bucket，批量io_uring到pinnedhost再CUDA copyengine至HBM。它不是多SSD汇pool本身，而是工作负载相关的物理布局→去重复本选择→并行I/O接口。Localwindow用于newKV观察与cluster加入、hotfrequency/minheap更新；下一层embedding预测取回只可视prefetch proposal，不证明候选完整或fullattention等价。

**保留原方程/描述冲突，不照录精确配方：** Eq2分母是所有pair frequency总和，其量不等“given某KV已激活的conditional概率”；Eq3 d=1−P，但相邻prose称d=1总共激活，代数方向相反。Eq9把sum_j f(new,medoid_j)写成W，需要每step恰好计一个medoid或独占计数条件；同时激活多medoids时不自动相等，文中选多个cluster及复本也不能自行补此条件。故不授阈值/概率/最优图聚类正确性、negligible replica开销或无损质量。这些recipe与采用的Eq8集合去重/已有副本路径分权分开；请非preparer判断这种有限接口采用是否足够，不为快速关闭虚NC或删反证。若中心依赖仍不可分，则保持6分中心隔离，需一次精确pair归一化/阈值语义、localwindow计数及实际selection-quality/费用trace请求。

§8配置CPU XeonGold6530(64cores/128threads)、8H20各96GB/1TB DDR5、最多8SSD；PM9A3 6.9GBps/1.1MIOPS与Optane900P 2.5GBps/.55MIOPS，不能把两种介质条件合一。BF16/GQA，T2实际列Qwen3-14B/32B、Llama3.1-70B、GPTOSS120B、Qwen3MoE235B共5项；prose称6 models、intro5，不补第6身份。WikiText/LongBench/MMLU/GSM8K，不足长序列拼接至1M。默认10% sparsity，NoCluster oracle选token但全cache读至DRAM的时间未完全计（原文只报score与selectedtransfer），InfLLM块与PQCache Kmeans选择器不同，不能当相同选择/同质量budget单因果取回优势。§8.2 normalizedaccuracy oracle最高、Swarm接近但不是相同输出或fullKV无损。Offline replication/placement，runtime dedup/balance消融指向该接口，仍与whole-system因果分开。8.4短prefix/低sparsity IOPS-bound，较长才BW-bound；batch1/4/8只局部，1SSD退回baseline。PM9A3 vs900P crossover及8SSD吞吐不同，不授介质通用峰速或生产TTFT/TPOT/SLO。offlineprofile/cluster构建、冗余写入/存储、DRAMindex、hostscoring/pinnedbuffer、sorting、prefetch miss与故障恢复/磨损/能耗全费未闭合；无生产arrival/tenant公平/独立重复CI，不用headline倍率填缺。

## actualowner差额与交接

sole INFER-GPU-MEMORY/Ch54 `books/part-05-inference-system/54-gpu-memory.md`，实际L278–307扩展层级、L310–349 layerahead/prefetch/capacity、L657–681压力与层级/多DRAMSSD pool完整顺读。现有L670–672只承载bandwidth-weighted pool/SPDK绕串行和tier代价；不讲共访cluster条带+selective replica的union去重及取回路径选择。L408 expert coactivation是weights/router identity，不能作KV具体NC。Ch53 actual L1–32部署topology；Ch55 L1–38只管PD break-even/handoff，不移owner。拟最小段置L670/672已有pool论点后，不重复稀疏selection数学或paging语义；前后仍是层级/容量、路径取舍。

## 拟逐字PRE（只候选，非写授权）

带宽池解决了“有多少设备可读”，还不能保证某一步会用到这些设备。稀疏 Attention 的候选 KV 经常共同访问时，一条 workload-aware 分支先按观察到的共访关系组织 clusters，让同簇 entries 跨 SSD 条带放置，并为重叠簇保留有限副本；DRAM 保留代表 entry、位置索引和热簇。取回时先合并已选簇、去除重复及已驻 DRAM 的 entries，再把单副本固定到所属盘、多副本交给当前待取回 entry 数较少的盘，最后并行读入 pinned host buffer 并传到 GPU。这样用离线布局、索引与副本容量换同时读多盘的机会，不是仅增加 SSD，也不让存储取回路径决定 Attention 的正确答案。<!-- source-family:SF-2026-ARXIV-2603-17803 -->

共访图、medoid 候选与下一层预取都可能失配；cluster 变大、重叠副本和小随机读还会放大 bytes、metadata、host 排序及写入成本。[Swarm exact-v1 §5–8](https://arxiv.org/html/2603.17803v1)支持这种布局—去重—副本取回接口，但其 pair-frequency 归一化、距离方向描述与 local-window 计数条件未闭合，本文不将其精确聚类阈值作为可复现配方，也不授最优或无损质量保证。作者 BF16/GQA、H20、两种 SSD 与指定数据的默认10%稀疏评价改变了候选选择方式，oracle 质量更高；吞吐及取回数字因此不是 full KV 等价、全费用或生产 SLO 证据。单盘、短前缀、访问分散、严格 exactness 或画像漂移时，原有连续条带、普通按需加载及更大的驻留集合仍是合理分支。<!-- source-family:SF-2026-ARXIV-2603-17803 -->

静态源注拟：`SF-2026-ARXIV-2603-17803`，Swarm exact-v1 §5–8/Eq8/T2–5，采用coactivation布局→激活cluster union减驻DRAM→低副本度先分配/最小bucket选副本→pinnedhost与GPU取回接口。Eq2/3/9配方与质量等价/最优/完整费用不采用；默认10%/不同selector、oracle反側与1SSD退路保留。未核代码或复现。
