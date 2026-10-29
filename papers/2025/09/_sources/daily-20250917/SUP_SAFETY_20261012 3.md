# Sep17 必要安全与设计反侧局部

均精确v1、仅具名受影响位置；不授日级公开、不评分、不声称整篇Evidence/实现/复现。未知公开日的潜力不是窗内候选；安全保证、性能普遍性不进入Books。题摘P保留，与中心保证未证分别维护。独核旧层/本轮层的实际note读后复用，不让消息替代原证。

## 已实际note读取后复用

Anscombe唯一note§7/11作者实际读：CBP12112v1 §2/3/Algo1私有X拼入f(X*)与“不上传”冲突，300API预算；不授双向隐私。FedFD12630v1 §3.2/附录可视化不证DP或泄漏攻击界。MIA2511.14763v1 Main Method/Eq1–6/Algo1/Data为已知5%member、teacher logits、whitebox reference的graybox，不授未知成员黑盒或真实base-rate风险。FedMentor14275v1 §2/3 Eq2/7/9/Algo1经验噪声/utility降sigma、budget减0.1epsilon没有邻接敏感度、裁剪/全轮accounting，DP保证隔离。上述全P必要安全层可复用，未重读全部表/附录。

同note§11：Phi12521v1 §3.1/3.2、§4、§6、E/F白盒跨图非跨模型，MC/Pscore不证人格；preprocessing确有下降，不采所有防御失效。Watermark12574v1 III/IV/V generation要weights/bias，blackbox仅detection；z阈值非来源后验，随机edit不证adaptive防伪。Survival12190v1 §3/4/Table1/§5/B.2/D为数值state转prompt，不证情感；高资源FullModel比prompt-only更多违规，不授普遍优越。CUDA14279v1 §3–6/A.1/D/E softverifier仅筛选，hardware反侧不可省；30/~20kernel是有限分类、H100/shape/eager与compile不同分母，搜索和验证成本保留。

## 作者本轮实际原件窄读

以下SUP_safety-IDv1原件+同名request实际取得，每项停止于拟潜力的必要机制/评价反侧，未全篇/全部图表。

- Taurus12676v1 IV/V段68–96、VI段97–130：128-bit security是所用参数集/工具链前提，不证部署侧信道/端到端保密。48bit固定点只在已测参数集bit correctness；强同步key reuse与分组带宽代价、KS/ACC去重是机制P。性能来自cycle-accurate simulator/TSMCN16综合/DRAMSim3，Concrete-ML1.6.1 commit8681124、Compiler2.7.0 b7793aeb；GPT2为7bit量化/6bitround，CPU48coreEPYC7R13/双A5000对照。并非真实芯片部署或任意LLM usable，串行负载要batch提高利用率；memory-controller/PHY排除的面积比较不能作总芯片比较。
- Content Concretization12937v1 §3/§4/§5段17–81：低tier初稿/高tier细化的有限组合P；350个七类前50prompt，keyword过滤/三judge多数与非拒答后A/B偏好不同分母。N3 SR最高而N4下降，不采单调“越多越好”；20个已过过滤的N4代码/160个LLM生成单测只30%全通过，不证生产攻击或普遍安全失效。三具名人工例是局部，不把邮件文本/包发送当实际伤害。仅一modelpair、自动judge偏差、试错prompt选择/成本与人工改动保留，未采用攻击recipe或执行任何生成物。
- DiffHash12824v1 Method22–28、Experiment52–71：文本对齐/latent生成攻击P；target t-MAP@5000为retrieval排序代理，不是请求攻击成功率/语义不变。三个多label数据、5000对齐图、ResNet50 source与转其他backbone、32bit transfer需分开；SDv2/DDIM/4090D/30iter/16.59GB限定。可视化只支持所示图例，不证imperceptibility保证或一般blackbox；短hash有输给对照切片。未核完整攻击实现。
- Defense2Attack12724v1 §3.1/3.2段19–30及§4段31–48：source weights/gradients白盒、Gemini只是transfer target；GPT4o既reward/judge，ASR不是真实harm。5000PGD+GPT2PPO训练预算与推断one-shot分开，不以one-shot证明端到端便宜；弱防线组合可能失效P，非任意防御无效。open/closedmodel与跨dataset口径保留，局部消融不授所有模型因果。
- ReTrack13007v1 Method32–52/Experiments54–79：理论unbiased全和→top-k近邻截断的实际近似必须分开；正则器缓和overforgettingP，不由理论标签认证实际删除。MNIST10seed/50k生成、CelebA与CIFAR各10图、SD1.4的48pair/每评16sample、SSCD/Frequency/NLL及CLIP-IQA是有限遗忘/质量代理，不是certified removal、MIA消除或法律合规。无需为隔离这些保证扩大全部附件。
- VFM12995v1 §2/3段13–43：frozen CLS+同GenImage linear probe比较，但specialized detector来自原发表不同训练协议。postcutoff WebAIG25只部分模型显著下降，PE95.9/DINOv3 95.0仍高，修正原题摘简写“cutoff后崩”不可泛化全VFM。上传日期/数据域变化与训练曝光混杂未受控；作者“曝光主因confirmed”不是因果证。保整个训练史/基线选择评价P，不证检测生产truth或training无污染。
- MedFact12440v1 §Experiments43–72：VC正确不等EL正确、EL在判错条件人口内；GPT4o judge的10%人审kappa.87不认证全部clinical事实。multiagent recall↑precision↓、延长budget误报反侧保P；RAG直接检索同源6405专家原文本，不能与无知识条件归因纯reasoning。补全ROUGE低不证无训练污染，“correct-for-wrong-reason”不是hidden机制因果。未读全临床/所有supp。
- MORABLES12371v1 §3.3–4/Limitations35–85（截断56–85已另完整补读）：TF20%positive/80%negative、NOTO与TF回答不一致是格式/选择评价P，不证model内信念、sycophancy因果或真实道德。709fables、五研究生审校/两annotation、152修订；Western/English/既有故事memorizaton、自生成distractor的潜在偏好/最好one-shot选择保留。BERTScore弱人评相关与主观方差不合并truth；未遍历所有附录。
- Alignment12936v1 §4–7/Limitations36–89：LLaMA7B同SFT后IF+safety、BoN16、temperature0.1/1与五轴ID/OODP。1920stratified人审一致率不使70Bjudge/合成gold成为truth；summary换HHEM>.5、diversity三proxy均值、proactivity以正确拒答归一、FAR/FRR不同prompt人口，不并成任务成功。SFT仅IF而后alignment增safetydata，不能归因全部差额为algorithm；不普遍排列DPO/PPO/ORPO或证强judge无bias。
- RAGs-to-Riches12168v1 §3.4–6段55–100：IOO/IOR token overlap只是示例利用proxy，不能实际计算的Bayesian假设不被它证明。453interaction/3repeat但固定seed温度.1，CrowdVote “human expert”仍LLM模拟，不是人评；authenticity/角色忠实≠安全。披露prompt/角色失配负侧仍保，未核多模态未来计划为实现。
- R2tA12476v1 §2/3.1段16–36及Metrics/Results47–66：同GPT4o guide/refinement与grader需独立oracle；F1 plateau .05/两iter/max5只停止规则，不自证faithfulCoT或groundtruth。三schema450训练/heldout Hospital150与60studentfeedback、只有三类足够quantitative，不能泛化全部错误类型；SFT/DPO选择P与rawaccuracy分开，不授因果reasoning或generalization保证。未核programmaticchecker/全部supp。

所有项继续保窄潜力；本日未取得可靠日级公开证，不进入正面候选/评分/Books。若取得完全落窗公告，按采用命题恢复标准/深入Evidence与具体owner比较，不把以上必要局部当已完成全深审。撤回12715另保官方v2根本方法错误说明，不入选/评分/Books；两overlap家族另见SUP_SOURCES的具体差额门。
