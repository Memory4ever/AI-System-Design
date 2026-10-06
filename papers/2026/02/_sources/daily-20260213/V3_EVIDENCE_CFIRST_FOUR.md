# C 首组必要证据：10905 / 10908 / 10915 / 10934

四家族完整v1准入已由root独立校准，日期属于已核119排程交集。作者本组已完成必要证据（10915安全受影响深入），root必要源命题/Only/Existing处置已实际复核；Aura/CAT两处实际正文/邻接/末注非作者POST已通过、窄锁释放，不授日级。原缓存CFIRSTCORE0–3/MORE0–3按标题顺序；CFIRSTEVAL混合三篇，source L号按标题分开。FINISH/LAST0–3和AUDIOA/CSHORT是必要补点，不声称全附件、代码或复现。当前abs CHECK1+CFIRSTAUDIOREVISION未见明确withdraw/correction；10915v2 Submitted02/12T10:44:59Z、10934v2 Submitted02/12T04:04:45Z均不等public，没有具体重要修订信号，不扩版本史，采用精确v1。

## [10905 Natural Hypergradient Descent](https://arxiv.org/html/2602.10905v1)

5（2+1+2），标准完成，仅报告通过。§3在inner SGD轨迹上复用随机gradient outer product，维护EFIM逆并与另一device上的inverse/crosspartial更新并行；end-inner crosspartial版本另采M样本，不是任何版本都无额外计算。完整逆矩阵有二次状态，KFAC是额外近似分支。§4.1–4.5及B.2明确strong-convex/smooth/unbiased/bounded noise和每个outer v处正确设定p(theta*)=q，只有该最优点Fisher=Hessian；不采用非凸LLM、任意misspecification或KFAC同保证。B.2消掉密度二阶积分正依赖上述同分布及可交换积分微分条件。

E.1为MNIST线性分类50k、50%噪声、batch1024/inner10/λ1e−4，CG/Neumann受控共享batch/iteration、各方法gridsearch。NHGD实际用平滑rank-one更新而非理论Eq3.2，两张A100-SXM4-80GB做并行；Table2 outerloss .2765明显不优于SOBA .1055等，accuracy .9180是最后50epoch平均，所列±不能直接当独立seed CI。“最快收敛/更好所有目标”不采用。E.2的5/class FashionMNIST披露beta=0而实践inverse式除beta，属于数值配置未解，不能背书该实现或从其结果授普遍生产提速；理论式与实践、用资源换时延分开。PDE应用不纳入AI-for-Science，不展开其附件。precision/精确时延测量边界/并行基线device数与总GPU成本/训练seed ND。仅报告有限同步估计替代与明确假设，不把小线性实验、存在初始化/配置缺口的实现提升为训练owner普遍Fisher优化结论。原CORE0 132–180、MORE0 184–252；FINISH0 530–553；EVAL对应323–351；LAST0 1105–1145。

## [10908 SoftMatcha 2](https://arxiv.org/html/2602.10908v1)

6（2+2+2），标准完成，具体已有原则覆盖/算法仅报告通过。固定最长pattern L=12的disk sorted array配RAM每B=128–256采样索引，先定位小区间再精查；单随机读取说法依赖page-size条件，不是任意长度/所有cache状态保证。semantic token替换加insert/delete相似度，prefix扩展立即检corpus存在性；高频2/3gram RAM和稀有prefix直接枚举后续tokens减少查盘。理论sublinear依赖Hypothesis1及Zipf/固定阈值，动态relax阈值/更宽相似度仍改变搜索量；实测full查存在次数每token增长2.27倍，不是零指数增长证明。

FineWebEdu1.375T与word-level GloVe，AWSi4i.32xlarge128vCPU/1TB/30TB NVMe；EN400（其他100）generated短queries、K20。baseline的Kth阈值预计算不计时、第一条前清CPU cache而条间不清，不能授每query冷盘端到端。median89.59ms与p95278.17ms只该协议；K80/minsim.2 p955697.39ms直接反侧。21.6TB总量含raw，其他9.9TB排raw不直接同口径；53.8h建索引及RAM/SSD成本保留。precision不适用离散索引/embedding查找，embeddingdtype、并发/SLO/多run不确定性ND。

污染例仅7bench共2564题的question-only扫描（10tokenstride、.6相似/.8coverage），exact338之外36flag人工29真/7误报，未建立全未标记集recall，更不建立模型使用该语料/分数由污染造成。Ch27实际717–736已载exact/n-gram/near/semantic分层、宽匹配误报、冻结policy与provenance/clean slice；故该有限semanticoverlap评价边界已有覆盖，不为+36造普遍污染gap。disk-aware pattern工程与限定人口结果仅报告，不称正文已有具体该算法。原CORE1 140–188、MORE1 188–225；EVAL对应234–265；LAST1 617–626/671–690。

## [10915 Blind Gods and Broken Screens / Aura](https://arxiv.org/html/2602.10915v1)

6（2+2+2），安全变化受影响深入完成，拟Ch78窄PRE。实际攻击条件为视觉clone名称/布局替代provider身份，以及预安装恶意app已有overlay+Accessibility权限时，只在automation virtual display显示假控件；用户defaultdisplay看不到与agent相同观测。不能称无权限远程攻击或所有手机都不检查签名。关键新增是effect executor须把visual display/观测surface与真实package/provider principal分账，视觉名称不能授权，非“typed API更好”成熟组合借分。

§4的AIC/GAR/TEE/sessiontoken、taint、CriticalNode、domainallowlist、validator是架构设计；XMLtag+prompt强化不能证明controlflow绝不改变，authenticated AA不签发semantic truth。乐观operation-type token让后续先执行后审、revocation只阻后续，不能撤已发数据/支付；不采用完全intent一致/非否认/不可泄露通用安全保证。source entry是trusted的标签也不证明原user/内部state确为ground truth。

必要评价§5.1明确Aura是Gemini3Flash SA/AA+structured mock APIs的模拟设备，baseline是真实DoubaoStandard/Pro系统视觉路径，非同model/接口/权限/hardware matched因果。80选取任务35低风险/45高风险；Table2 33/35、2/45、68.54s是该protocol，不能作真实Android端到端生产或归因移除截图的单因素收益。Table3两baseline10个benchmark injection均0/10，aggregate差主要general-safety；Aura还有timeout与judge falsepositive，两项错误未消失。§6.3 implicit slang未解；硬件、precision、重复数/CI、实际kernel mediation/TEE/nonbypassable网络实现ND。拟Ch78在interfacegranularity→browser fallback处补display identity与privilege绑定、真实效果receipt和virtual/default两surface审计；Ch72已有principal/scope/effect与taint论点只引用，不重复写安全体系。root授Ch78窄锁后已写正文181/183及末注753，root实际POST通过。原CORE2 112–160、MORE2 161–210；TAIL0/FINISH2 366–505；LAST2 568–640/659–708/738–757。

## [10934 MOSS-Audio-Tokenizer / CAT](https://arxiv.org/pdf/2602.10934v1)

5（2+1+2），标准完成、具体representation接口差额必要加深，拟Ch23窄PRE。HTML404，PDF仅读必要§3–5、A和C的配置，不称全27页/图形复核。24k raw waveform经240/2/2/2 patchify→12.5Hz、因果Transformer/RVQ32/decoder和0.5B audio-to-text head联合训练，不用外部teacher≠无semantic监督：paired ASR/multispeaker/caption CE仍必要。12.5Hz含frame聚合、10s滑窗与庞大0.8B+0.8B编码解码；不能把causal mask当零buffer latency/实时SLO证明。

§3.4 Progressive Sequence Dropout同时截断temporal输入的RVQ embedding sum及depth loss，infer K也只消费/预测前K；不是只丢loss却继续输入全depth，消除具体train/infer接口差。Fig3 .0/.25/.5/1同50kstep消融只支持所测TTS低bitraterobustness；全bitrate接近、非任意K/任意模态无损。Ch23现186–198已讲progressive缺层/decoder compatibility与teacher assignment，206–220时间/depth分工，但尚无同prefix同时约束输入、loss和部署depth的分支；建议一至两段承接此处，旧teacher/staged路线保留。

codec约3M小时、bf16 AdamW、非对抗520k/B1536后对抗500k/B768，joint≠从开始所有loss同一stage。TTS Qwen3-1.7B temporal+4blockdepth、约200k小时、batch1.35M（speech按frame算而非RVQ全部codes）、AdamW2e−4、ablate50k/final200k。Table2 LibriSpeech/AISHELL2/AudioSet/MUSDB指标/bitrate与不同baseline规模绑定；4000bps audioMel .68不优DAC6000bps .65，不跨码率授全优。§5.2大模型低bitrate仍可能逊小模型高bitrate，§5.3fixedsteps扩大batch同时增加seen data/compute，不是同算力缩放证明。Table3 SeedTTS CAT 1.89WER/1.23CER，非优于所有cascade；ASR附录2.96/3.44亦非全胜。硬件、wallclock/吞吐/并发SLO、图形读数/统计CI ND；不采用作者首个/普遍scaling标语。root授Ch23窄锁后已写正文196/198及末注1024，root实际POST通过。原MORE3 PDF P3–6 L126–324；FINISH3 P7–10 L334–618；AUDIOA P21 L954–986；AUDIOCSHORT P24–25 L1139–1160，附带Table4 L1174–1204仅直接反侧。
