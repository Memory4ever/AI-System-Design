# 第二十四包：AB13 三项必要命题/反侧（待非作者复核）

没有Books lease，不增加35safe。23336只隔离受影响的几何/0–1保证，局部训练经验另留，等待root决定其最小安全采用范围，不自动全篇D。23342/23351普通必要PRE。

## 23336 Differentiable Zero-One Loss via Hypersimplex Projections：6=2+1+3，中心子命题争议，经验仍待裁决

[exact-v1](https://arxiv.org/html/2602.23336v1)28–33/42–94/95–112实际读。训练对每class跨batch logits投影到box+sum=k的hypersimplex，再用平方loss；k与训练batch正label数量相关，coupling不同样本，非每样本的softmax输出接口。F_tau=projection(x/tau)的Lipschitz/a.e. Jacobian局部论证可成立，active interior A上的Jacobian为I−11^T/|A|；不因hardtopk论证错就断言此连续操作不存在。

关键中心矛盾：Eq5最大化<x,y>−||y||²等价projection(x/2)，不是Eq7 projection(x)。50/53称Euclidean projection等于binarytopk且piecewiseconstant，实际上连续投影通常为分数、piecewiseaffine；原51自己的x=(.1,1.6,1),k1真投影(0,.8,.2)，平方距离1.29，小于hardvertex(0,1,0)的1.37。mass=k也不保证exactly k nonzero。独立计算已复核这两个距离，不做所有定理/proof遍历。温度>0也不保证处处smooth/内部：x=(2,0),tau1,k1,target=(0,1)，投影错误顶点(1,0)，loss1、邻域active A空，所有坐标梯度0；公式的1/|A|必须分支处理。不授误分必有梯度、全smooth或与0–1等价/consistent guarantee；未核代码，不能称实际实现必错。

独立经验：CNN四conv+BN/maxpool/ReLU/两FC，CIFAR10/FashionMNIST、batch128～8192、5seeds改变初始化与split，pairedt alpha.1，共280runs；原报告按maximum test accuracy选数，不是冻结checkpoint的held-out选择。103的13/14显著限定alpha.1及多comparison，未校正多重测试，不授普遍generalization或LLM收益。epoch/optimizer/LR、tau/k具体设定、precision/完整墙钟ND；原v1 block100已披露32-core Threadripper PRO5975WX、503GB RAM、3×RTX6000Ada48GB，原包未注明硬件的事实在此纠正，100随机train/test split与标准split描述未完全一致。MSE/hinge声称作控制，但主Table1只有CE/HS完整值，不把未展示ablation当因果证明。Table1 batch8192的CIFAR.8541→.8648，是可保留作者经验而非几何证明；softprojection数学错误不直接否定作者运行，也不足以认证修正版实现。

actual `TRAIN-PRETRAINING` Ch28 661–682完整batch邻接实际读，已有batch/token/step/噪声分责，无跨样本class-mass loss/Jacobian分支。拟仅在原形式修正并独立确认经验实现身份之后考虑窄整合；当前不写Books。安全暂缓的精确重开条件是原投影/硬topk声明纠正、active-empty分支及采用loss的实现/评价设定。root可裁决保有限经验为独立命题或中心争议终态，不用标题/旧准入直接授理论。

Submitted2026-02-26T18:41:31Z、registered2026-02-27T03:08:22Z；arXiv事件09:00～11:08:23+08，原值与已核公告下界分开。current未来PAKDD2026说明不单独认定已早public。

## 23342 AlayaLaser：拟2+2+2=6，Ch76 SSD索引布局一段

2026-10-06 fresh后续复核（`feb28_ch76_ch36_finish`，非原包作者）：本项原准备确在packet24非23。原v1 blocks48–57/65–75/78–90/104–118直接核SIMD布局、earlydispatch、Table2fixedrecall/R/BW控制与Table4DPR构建慢侧，足够拟采用命题即停。2+2+2=6，窄Evidence通过；actualCh76已有导航/向量分离、page消费，缺页内复制code把compute重变I/O及partialbeamlate候选接口，窄I233–235、完整邻接217–245、末注1281，root 非写入者已实际核正文、完整邻接与自身末注，POST通过。保disk放大/OOD/queryrecall成本，不授exact无损/所有工作点赢家/实现复现。

[v1](https://arxiv.org/html/2602.23342v1)23–75/78–129必要方法/控制已实际读，首次输出33–46截断后单独恢复30–46。DiskANN邻接+原向量disk、内存PQ的旧合理路径在低维I/O主导；高维PQ LUT串行/实际cache改变compute瓶颈。原改进将PCA principal的邻居code按SIMD subcode跨neighbor交错放入disk node，保原principal+residual作最终重排；由缓存全体PQ转为按in-degree缓存node，并以早dispatch在部分beam完成后开下一hop、晚到节点仍异步更新候选。最后一句只是作者近似搜索所述语义，不证明所有顺序exact或召回无损。

核心直接控制58/Table2固定GIST960D、Recall@10=.90、R64/BW8只换layout：compute1846.55→220.833us，却meanI/O77.21→131.109、I/O1254.09→1774.51us，latency3223.66→2036.44us；SIMD收益可重开I/O压力，不能仅用compute降幅验收。122四code变体240B PQ/48B PQ/PCA+PQ/PCA+RaBitQ说明更精细码减少I/O却吞吐不一定最好。布局/table主要控制足以采用这条取舍，不必复核每条曲线/all代码。

XeonGold5318Y24core48thread、DDR4 128GB、3×PM9A3 1.92TB、Ubuntu22.04/kernel5.15，O_DIRECT/libaio；1/10/128GB三个memory预算，R64/constructionL200，PCA256，BW各法8/8/32/16，recall由searchL扫描；所以总体胜出不能只归一个组件。QPS48threads、latency单thread，117并发1～48曲线不是完整productionP99/SLO。Cohere/BigCode/DPR三queryset从data抽样10k，GIST/MSMARCO用原querysets；groundtruthlinear scan，不能外推query分布。33所导3cycle×48thread roof不是独立硬件实测通用峰值，不采用所有高维一定compute-bound。

直接慢侧/费用：104 BigCode低recall<.98慢于内存Vamana/HNSW；Table4 DPR构建1532.4min高于DiskANN1464.5/Starling1420.5/Pipe1472.8，与107“全部更快”不同；Table5 Cohere78vs39GB/BigCode80vs40/DPR771vs386GB，nodecode以disk放大换memory。125单SSD控制不授硬件无关普遍性；53 OOD/modal-gap查询会退化，126沿旧PCA插入10/20%仍较rebuild慢。PCA、cluster、cache、layout/graph版本与重建都付费，原文未给多seed不确定性/生产在线更新协议，不照录“无损/所有场景赢家”。

actual `AGENT-RAG` Ch76 190–237完整SSD导航/向量分离与far-memory精化邻接读，已有近似停止/recall、storage、构建与freshness分账，尚无 **SIMD code页内复制改变compute→I/O瓶颈、part-beam earlydispatch仍留晚候选的条件分支**。拟SSD索引处一段；保OOD、index放大、query/recall和late-arrival边界，失败时回退普通PQ/共址/同步beam及完整向量重排。不把maturecache/cluster单独算新贡献，也不重复先前22805 pagebuffer命题。

Submitted2026-02-26T18:48:29Z、registered2026-02-27T03:08:30Z；arXiv事件09:00～11:08:31+08。current SIGMOD2026 acceptance；同题有限搜索未出现更早实际发布依据，不把accepted认定public或全网无早稿。

## 23351 Scale Can’t Overcome Pragmatics：拟2+2+2=6，Ch27 collection protocol一段

[v1](https://arxiv.org/html/2602.23351v1)19–45/47–57/59–81/83–104/107–122/128–141实际读。旧caption采集/自然alttext可给对象和属性监督，增加规模不必补默认不叙述的空间、时序、否定和count；本稿通过 **同100图改变annotation instructions、50图强制50words、同规模26K计数mix fine-tune** 给具体限定的采集选择，而不只泛称dataquality重要。固定图控制是主增量，语用学框架借已有理论不计新机制。

Corpus keywords+每类100例人工TPR只是这些字面模式的估算；不授所有reasoning实际频率上界/隐含能力不存在。Caption越长不等某类缺失信息补齐：50张同图要求至少50词，10空间/25count/0否定/0时序；按100图指令组，专门要求四类得14/39/52/44%，PixMo21/43/12/1，自己的指令也非每类最佳，领域/参与者人口限制保留。合成GPT4 caption中的错误方位不能由keyword出现认证真监督。

32个OpenCLIP模型、LAION80/400M/2B与3/13/34B data seen显示有限scale趋势，不采用标题的全尺度不可能；122明确scaling hypothesis可在更高规模失效。Multilingual一项负结果不证明所有语言都omit。Closed-data模型性能也不识别data原因。计数训练：LLaVA1.5-13B，9K TallyQA+17138LLaVAIT成约26K/39%count，1epoch、2L40S、batch4、lr1e−6，vs同26K原IT结果50.7→54.4；count均衡/来源/内容同时变化，不把纯比例或自己的100图annotation数据直接当唯一因果。其actual100图annotation未规模化train，是作者99/122的限制，不能写成该协议已完成大规模预训练验证；precision/seedCI/wallND。annotation每估算小时$15+超时bonus、人工truth校验/再训练仍付费。

actual `TRAIN-DATA` Ch27 55–104完整采集论证实际读，已有elicitation决定q(x)、采集protocol非中性；还没有 **固定图、长caption与明确类型提示不同补缺、文字keyword不是图中真监督、按真实可见关系分验**。拟此处窄经验条件段，保photo无法决定before/after的不确定、annotation truth/权限、数据混杂和有限scale，回退专门任务标注/原简洁caption与held-out校准。不是因论文名缺位造gap，若root认为原实际protocol链已充分则Existing有效。

Submitted2026-02-26T18:54:06Z、registered2026-02-27T03:08:43Z，arXiv事件09:00～11:08:44+08。TACL2026信号已定点核[官方ACL同题](https://aclanthology.org/2026.tacl-1.41/)六authors/pp918–935/DOI10.1162/tacl.a.690；publisher登记Crossref published-online2026-06-01、created2026-06-17T13:27:35Z，正式publication晚于本窗，不把搜索“9 months ago”当旧public。原值/检查时间见[V3_FETCH_AB13_23351_FAMILY.json](./V3_FETCH_AB13_23351_FAMILY.json)。目前无具体早公开正文证据；该后来publication不改变arXiv event归属，不沿DOI重新计家族。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）本项落实：23351：2+2+2=6，固定图采集类型与长caption反侧，关键词不授真实监督；必要原v1/直接反侧与actual owner独核，Ch27正文77/自身1570及完整邻接root非写入者actual POST通过。保原有效身份/精确版/采用命题，必要原段见本项；作者已实际顺读，费用、人口、错误子保证和原路径回退近正文，窄锁释放；不授全附件/实现复现或日级。
