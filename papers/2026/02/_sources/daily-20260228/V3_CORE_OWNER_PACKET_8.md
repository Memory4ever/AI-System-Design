# 第八包：必要经验命题与实际owner差额

五项由root完整发现题摘校准后，只读original v1必要机制、对应控制与直接负侧，非全部proof/artifact。v1 abs/HTML见V3_FETCH_AB5_NECESSARY；当前官方abs轻量状态见V3_FETCH_CURRENT_AB5B，22591评论为SIGIR2026接受、22592为页/图数、22601为CVPR2026接受，未出现撤回/勘误信号，不默认审后版。original v1 Submitted均2026-02-26UTC，晚于公告政策下界2026-02-25T19Z；same-ID registered为22583 02:49:47Z、22591 02:49:58Z、22592 02:50:00Z、22600 02:50:11Z、22601 02:50:12Z（均2026-02-27）。公开范围共同下界2026-02-27T09:00+08，上界各registered加1秒转+08，完全落窗；不把Submitted/接受日期当public。

## 22583 Strategy Selection/SSR — 2+1+2=5，Ch79局部guidance选择

实际blocks32–48/65–82/85–109/213–225已读足。4850数学题的human/model解法提取3–5条短规则，按策略类别建立语义/图/来源特征，以模型自身试用成功次数训练utility估计，检索proposal后rerank guidance。源解法中经常使用某策略，与目标policy看到一段指导后能执行它不同；human/model source的相对优势亦会随模型/任务反转，不能默认human更好。Beta-binomial posterior平滑与logistic/温度校准仅在训练人口和heldout下成立，不是通用成功概率认证；正确答案/GPT5.1解题judge与策略adherence judge仍可能共享盲点，后者相关性不证明策略因果。有限Qwen8/R1Distill7、32K/temp.7/五seeds支持局部选择，graph/语义检索去除均有反退；绝对难题成功率仍低。source抽取、试用rollout、图/估计器训练与校准/judge付费，输出tokens减少不等总成本下降。

Actual Ch79 58–66已承载环境先验估计器与selector分责、绑定模型/分布及真实observation回退；324–328承载求助指导转动作权限。尚缺**源解法中使用频率≠目标模型可执行指导，以目标policy实际试用结果估计hint效用，并允许source排名反转**。拟环境估计器后单段，不重复RAG索引机制，不把beta平滑或adherence作真值；保费用、数据泄漏/漂移与固定提示/无guidance/可验证过程回退。请求Ch79窄lease。

## 22591 Layer-selective ICR — 2+1+3=6，Ch76训练free层读出

2026-10-06 fresh后续复核（`feb28_ch76_ch36_finish`，非本包原作者）：直接读原v1 blocks21–57/60–79/83–97与actualCh76监督head/queryrouter邻接；Table2 Qwen.6负侧、Table3多调用费用及BRIGHT oracle直接核，不继承准备标签。2+1+3=6，Evidence窄命题通过，Books窄I已写Ch76 482（完整邻接466–492），自身末注1278；root 非写入者已实际核正文、完整邻接与自身末注，POST通过，不计日级完成。仅采用固定layerinterval/null/reverse校准、排序截断及其费用/人口边界，无全层答案等价/普遍bellcurve/实现复现。

实际21–57/60–79/83–97（71–79截断已补）足够。BM25 top100/截断300words、query最后，以null N/A校准及反序平均从各层query→document attention读相关性，TREC19/20选峰附近固定window，BEIR9外测；不是累计attention，也不是动态learnedhead router。最深选层后提前终止forward，只保排序读出而非原答案等价。五模型中Qwen.6BEIR all .418>selected .416、peak .373；Llama近乎持平，不能称所有模型中层必然最优。BRIGHT每dataset的最佳层用了测试oracle，只为上界，不是部署zero-shot方法。

主实验A10080/FA2/doc300words；排序接口对照Llama8单L40 48GB/doc128tokens/c3，不能合成一个预算。在后一协议selected single-listwise NDCG .4534<all .4571，而3.501<4.331s；heapsort反复调用可36s，仍慢于生成14s/likelihood8.85s。N/A及反序校准两次额外forward、层搜索/显式attention/materialization与候选成本均留，precision/concurrency/SLO ND。

Actual Ch76 458–469已有受监督head训练+最深层截断与query-conditioned subset router，尚缺**无排序标注训练的固定layer interval选择、null/反序校准，以及layer-only省算能被多次排序调用吞掉**。请求该读出小节一段，仅受测排序任务，不等模型推理可跳所有后层、attention不认证relevance truth；保外测负侧与完整前向/普通rerank回退。

## 22592 pQuant — 2+2+2=6，Ch49 QAT结构性混合精度

实际18–57/61–91/95–100（41–57截断已补）足够。从scratch QAT将MHA主要1bit，FFN拆1bit分支+4–5% 8bit分支，feature α/β scaling与learned router选择一个高精度branch；top1规则固定不等router不训练。FP16 master/FP32 gradients及optimizer训练，部署另导packed1bit/8bit与INT8 activation，不能把训练表示当低位执行。Eq2 w²/逆Hessian是在quantized=0的敏感性proxy，不授普遍rounding误差或“参数民主化”因果解释。matched BitNet100Btokens/300M–1.3B控制支持局部结构分配，PTQ180B/3T不同预训不因果合并。feature scaling消融有效、naive8%混位反退、增加两个activebranches收益小；N8多分支的active参数少于BitNet1.3B但physical memory .98GB>.72GB，不能以activated bytes签发总驻留节省。

T-MAC AppleM2 CPU/长度256的7B算子示例不是所有所训模型的端到端服务；headline比例未计全部embedding/branch/metadata与高精度训练状态，不授SLO或TCO。training/导出/router与全部高精度副本付费，完整预算未披露。

Actual Ch49 962–991具体QAT产物形成、同weight预算容量折中与执行成本已有；尚缺**QAT用feature scaling和稀疏高精度branch分配容量，active计算人口与physical常驻容量须分开**这一结构接口。请求QAT容量段附近单段+ownnote，不重复通用quantization说明，保控制负侧与普通4bit/混精、小dense回退。

## 22600 Algorithmic Cores — 2+1+3=6，Ch5局部任务子空间

实际13–28/51–68/94–116（58–60补齐）/120–130/143–158足够，未逐个审所有任务proof。ACE把centered activations H与指定task-output Jacobians J共同构成HJ^T/SVD，映回activation span；实际大矩阵避免路径用H^TH及J^TJ因子分解，仍支付activation/Jacobian与rank搜索。三独立seed单层64d Markov模型中几乎正交原坐标得到对应3d task spectra，keep/remove/flip比几何相似更直接；full48d consensus虽keep好，删除后仍.54，不是同一必要性结论。finite99.9%rank threshold和干预选择只定义受测任务人口的operational core，不授普遍唯一/全域minimality。H用全部测试activations，不冒充独立heldout发现。

GPT2 small/med/large语法控制1200prompts，选层最大flip成功；最后层任务由固定are/were−is/was读出定义，线性梯度可直接形成一维轴，不能据此宣称内部所有语法算法唯一一维。跨规模不是同预训预算实验。生成steer每token三个forward与质量/扰动控制，不是单次免费edit；CCA/spectrum对应不认证外部语义truth，原其他任务结论不连带授全证明。

Actual Ch5 304–318解释faithfulness/干预规格与497–517probe诊断、标签不唯一/局部steering已覆盖，尚缺**以输入激活协方差与目标output sensitivity联合提取任务子空间，并将跨seed不变量同原坐标方向分开**。请求faithfulness段附近一段，保测试人口/线性readout条件、keep/remove/flip与完整模型回退。与22581两段拥有不同推理角色，不合成一种“真实circuit”担保。

## 22601 phi-DPO — 2+1+3=6，Ch34 focal pair目标，理论子命题隔离

实际26–78/80–101足够。reference取前stage policy、gold作chosen、LLM看到gold合成负例再人工复核；negative是模拟hallucination，不是真实遗忘response人口。CE+focal DPO `(1-p)^gamma * -log p`改同pair目标，finite gamma衰减容易pair，不是新增真实组公平标签。LLaVA1.5/Vicuna7/CLIP、LoRAr32/16A10040、oneepoch/B64/lr2e-5作者条件；beta↑有BWT好但quality降，gamma5反退、MRLoRA部分BWT优于本文，不授全指标支配。全部gold/负例生成、人工与训练成本保留。

明确不采理论：Eq15写alpha=(1-p)^(gamma-1)[(1-p)+gamma*p*logp]，直接微分Eq14应为减号；p=.9/gamma2时原alpha≈−.008965而实际≈+.028965。组内E(alpha*gradient)不默认等于E(alpha)*E(gradient)，缺协方差条件；gamma→∞两人口更新都vanish，即使差趋0也不证明有用均衡学习。DPO pair loss亦不能据一般性文字签发保留全部旧知识/KL保证，仅保公式14/17可定义目标与局部经验，不无差别审全部附录，也不自造paper实现。

Actual Ch34 152–160已解释objective/reduction改变、374–381有sequential目标关系/固定参照与失败人口，不含**在逐stage前policy reference上叠focal confidence因子与CE、并把难度筛选同组人口纠偏分开**。请求sequential DPO小节一段+ownnote；保finite gamma负侧、synthetic负例权限、理论隔离与vanilla/reference replay、显式组采样回退，请root actual确认可采用窄经验分支而非整项D。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）本项落实：22600：2+1+3=6，active×task-Jacobian子空间与任务/发现人口限定；必要原v1/直接反侧与actual owner独核，Ch5正文324/自身636及完整邻接root非写入者actual POST通过。保原有效身份/精确版/采用命题，必要原段见本项；作者已实际顺读，费用、人口、错误子保证和原路径回退近正文，窄锁释放；不授全附件/实现复现或日级。
