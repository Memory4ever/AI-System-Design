# AB8前四项：必要证据与实际owner，PRE待审

本包仅22755/22756/22758/22760的精确v1。固定窗口02/27 09:00～02/28 09:00+08，不扩发现池；未写Books、不计safe。HTML优先；22758原HTML404后必要原PDF已取得并读到拟采用范围，非永久正文缺失。共同获取见V3_FETCH_AB8_NECESSARY.json（2026-10-05T19:43:51～55Z）。当前位置以各V3_BLOCKS_2602.<ID>.md段号为准，PDF用页号。没有遍历全部proof/code或默认比较revision。

四个原abs-v1实际Submitted UTC：02/26 08:43:07、08:44:39、08:47:42、08:49:57，与同IDmetadata一致。根据已保存官方公告政策，均晚于前次cutoff，首公开下界为02/27 09:00+08；same-ID registered上界UTC 02/27 02:53:52、02:53:54、02:53:57、02:53:59（秒精度各+1秒，转换+08）分别为10:53:53、10:53:55、10:53:58、10:54:00。形成完全落窗半开区间，Submitted不作为public，DataCite仅身份公开上界而非primary技术/原公告。当前官方状态轻量已读：22755/758无评论、756IEEE submitted、760technical report；未发现采用相关撤回信号，不授发表验收。

## 22755 AuditBench — 2+2+3=7，PLATFORM-EVALUATION-SYSTEM拟一段

原20–33/35–76、scaffold147–155及必要162–180实际读；H末181–185未读、不采用其额外结果。过去“给auditor更多诊断工具即可增强发现”的选择，需要新增**单独工具信号有效不等于agent会消费、形成假设并验证，收益还随植入与anti-confession训练人口变化**。56个主实验模型、14行为×TD/SDF×SFT/KTO是作者控制植入，不是自然前沿模型恶意motivation分布。TD LoRA rank64/一epoch/6000transcripts，SDF40Kfictional documents；anti-confession是冻结行为adapter后训练并相加第二adapter，不当作模型自然欺骗机制。

Claude4.5-Haiku审计Agent SDK，25K investigator生成tokens**不含tool输出**，每model/tool配置16runs、最多10predictions，由LLM分类器匹配已知植入；不是开放真实行为完备oracle。Whitebox工具50generic prompt/层40–50信号筛选与12 held-out开发模型调参，SAE/steering/logit信号不认证intent真值。Static Petri转录与动态agent采样不同人口；scaffold并行辅助调用增加工具输入及总费用，不能因同25K investigator额度宣称等总算力。

直接反侧63–66：agent常只采5–10次用户、回退常规问答，相关SAE feature不被转成具体hardcoded-answer测试；更多Petri/honesty-steering噪声会分散注意并有false positive，TD+KTO部分工具甚至恶化。SDF+SFT容易、TD+KTO困难，blackbox scaffold在这个有限设置较好不证明whitebox普遍无用。Preexisting quirk可能误报，未覆盖自然出现的开放hidden behavior；无生产攻击安全或完整性保证。硬件/dtype/concurrency/端到端SLO Not Disclosed；16次调查不是16次模型训练。

实际Ch66 1159–1181有active judge取证≠oracle、取得正确evidence仍推理错、panel评分稳定≠独立问题发现；尚缺**static diagnostic识别率与agent能提出/检验具体问题的tool-to-agent gap，且anti-confession训练方式改变可发现性**。拟active judge/panel附近单段，用工具/植入/预算分责而非另建alignment章。保留固定/人工审计和可核行为test作为fallback；要同时测信号质量、工具消费和去重发现，不能以发现未出现签发模型安全。请求该单段与自身note窄lease，未获PRE不写。

## 22756 Dynamic Hierarchical BvN — 2+2+2=6，TRAIN-DISTRIBUTED-TRAINING拟一段

2026-10-06 fresh后续复核（`feb28_ch76_ch36_finish`，非原包作者）：原v1 blocks31–40/47–57/87–109/152–172/207–245/278–328直接读，对应构造、Poisson/capacity条件与同aggregate U/NU、同DFS仅切balancing控制足够即停。2+2+2=6，窄Evidence通过；Ch36 rail/wave实际邻接仍缺aggregate-preserving local block→server→GPU matching，Books窄I写309–311、完整邻接295–321、自身末注1818，root 非写入者已实际核正文、完整邻接与自身末注，POST通过。保localshuffle/restore、有限expectedframe与ideal模拟；不授所有completion严格下降、payload协议正确/真实GPU/任意到达生产稳定。

实际31–57/79–109/117–127/152–186/207–245/266–284/285–328；只采用构造、必要条件和对应模拟控制，未读全证明241–265、未作artifact实现审阅。已知fast intra-server B1≫slow inter-server B2、理想两级crossbar，整数单位packets的GPU demand可先在服务器内做row/column balancing，**保持server-to-server aggregate**，再对block与server矩阵分解并按全局matching时刻组装GPU subpermutation。改的是物理发送/接收安排，不是更改expert assignment或payload语义。

Δij=ceil(block最大row/col单位需求/m)的局部尺度与server-level Δ=maxrow/colsumΔij决定此模型schedule长度；零padding用于对齐。局部transfer潜势有限下降只在整数模型成立，payload重分布和restore本身付intra-server带宽；不能把45的“所有completion严格下降”当保证：若另一row/col瓶颈仍同高，最大值未必严格减，更未计local开销。这里采用容量界及条件构造，不借它认证实际协议正确性。

动态帧先缓存到达、下帧清空此前backlog；独立Poisson pair/time、固定大小packet、各server aggregate normalized load严格<1。必要266–284的MGF递推收缩α=(1+λbar)/2<1、初始T1=1支持该ideal模型的有限expected frame bound，不授突发任意分布、多跳heterogeneous links、生产尾时延或故障恢复。模拟8servers×2GPU（16port crossbar），无intra-server arrivals，U/NU skew对照保持aggregate，只切换balancing；100K slots/10K warmup测mean frame，不是真GPU训练实测。硬件/dtype/SLO不适用理想模型，实际network/runtime成本Not Disclosed。

实际Ch36 299–315已有MoE skew下rail routing与cyclic waves，保logical demand、metadata/completion和planning/packing费用，但没有**先aggregate-preserving block balancing→server-level matching→GPU-level matching，以及清帧stability的arrival/capacity条件**。拟这条通信链附近一段，不复制全proof，限定ideal bound/模拟验证。Local shuffle/restore、额外buffer或skew不合算时保留直接collective/已有placement，不能据理论matching宣称coherent payload、真实TCO或全生产稳定。请求单段+自身note窄lease。

## 22758 Physician Disagreement — 2+1+3=6，PLATFORM-EVALUATION-SYSTEM拟具体Existing

精确[原v1 PDF](https://arxiv.org/pdf/2602.22758v1)保存V3_PDF_2602.22758.pdf（19页）；HTML404不降低必要审阅。实际PDF pp1–7、12–13、15–17；p7 Table3视觉核读。未读8–11/14，不采用其quality-classifier/AUC或normativity具体结果，不声称全部论文已审。

60,896 binary physician judgments、29,511cases、186anonymizedraters、34criterion IDs/30texts，94.1%cases恰有2raters。**Label variance与disagreement variance是不同estimand**：label LPM rater2.4%、rubric15.8%、residual81.8%，不写成disagreement的81.8%。Case-level binary/continuous-pair disagreement rubric ICC3.9/3.6%、logit latent6.9%，相应残差96.1/96.4/93.1%；不同scale不可直接合并。仅2raters的多数case没有test-retest，residual混有occasion noise与item×rater，不能认证不可约“structural ceiling”或给F1最大上限。

另一个consensus人口711prompts/8526cases，physician-validated uncertainty标签是同prompt观察属性，不是随机改变信息的causal repair。Any reducible3420cases disagreement28%，vs no uncertainty2730cases13.2%，OR2.55 CI2.13–3.06；irreducible2376cases13.4%，OR1.01 CI.82–1.25 p=.9只是此观察模型未见差异，不证明无作用。Pseudo-R²3.4%不是解释total variance的3.4%。Context-not-enough35.3% vs enough25.8%、OR1.56 CI1.28–1.91不授补context会消除对应份额。所有这些是评价测量机制而非医学处理建议；残差不能因clinical名义变为truth。

实际Ch66 2659–2695已要求明确mean/ranking/slice/release目标并分item/rater/repeat方差；同质raters不修共同偏差，label distribution与normative rubric分责，member残差谱/频率恢复不同targets不能互换。这些具体正文已承载拟采用的**先定estimand再读ICC，未观测重复测量不签irreducible ceiling**。拟Existing而不因新医学论文名造知识gap；如root认为“label vs case-disagreement ICC”是必要缺口，再仅该具体测量接口一短段，不新增应用域内容。必要PDF已可读，普通PRE继续，非外部hold。

## 22760 Curtailment Feasibility — 2+2+2=6，PLATFORM-COST拟一段

原25–60/63–99实际读足。过去同site/time用energy代理operational carbon合理；此处新增**短且不同步的低intensity窗口把同步开销、冷启动、local steps/FedAvg和有效训练进度一起变成质量/成本条件**。nanochat20层561M、12.8B FineWeb-Edu，3物理site各4A100；WattTime <100g/kWh marginal intensity作curtailment proxy，Jan11 carbon traces通过Vessim replay，不等实验站点地理/真实被弃电力。Selected4regions偏乐观，Germany该trace无事件。

Active0暂停、1本地持续、≥2sites按processed batches加权FedAvg；需要近IID分配和明确parameters/progress版本。源码未核，原atomic θ/p协调声明不升级crash-fault证明或共享optimizer一致；作者把optimizer改进列future。约115s sync/600s窗口与5min provisioning、up10s/down10min hysteresis能吞收益；失败未返回θ/p不参与merge，stop在accumulation边界等公开行为只作所述实现事实，不写已审code。

17.8hbaseline final EMA训练PPL14.8、two-site11.1h/15.5、curtail14.6h/15.1；best PPL14.7/15.2/14.6另口径不能混。只有train objective，不等held-out quality或所有能力保持，无seeds CI。Energy37.7kWh仍高于36/36.1；1.38 vs11.4–27.1kg carbon是地理trace估算，不是实测物理排放/合规或账单节省。97%proxy-curtail、3%hysteresis不授zero-carbon。HW4A100/site已给，precision/完整network/provisioning账、tailSLO Not Disclosed；需更大模型/真实窗口/在线失败人口另证。

实际Ch70 197–213有functional unit与site/time/lifecycle、sameplaceintensity代理和deployment排序分开，尚无**窗口短到sync/provision吞进度时，training protocol转换与quality的同功能单位分账**。拟carbon accounting附近一段，只采用窗口/切换/费用与train-vs-validation边界；FedAvg协议、checkpoint/effect实现归原owner不在Ch70重写。窗口不足、data非IID或quality退化时，保固定site连续训练/保守暂停与原同步路径，不以低carbon estimate签品质。请求该短段+自身note窄lease。

拟三I一E全部待独立PRE；未改变本日35safe。共享文件未获lease不写，不把reviewer尚未回复包装为材料外缺。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22755：原必要blocks54–66及采用相关prepared控制/反侧与actual owner独核；Ch66正文1206/完整1184–1221/own5673 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
