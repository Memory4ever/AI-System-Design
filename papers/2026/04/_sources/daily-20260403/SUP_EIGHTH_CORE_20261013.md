# 第八批有限余项决定性core

## root实际必要原证复核回执

ViewScaling00557 III-B/C、TableIII和front-view部署反侧实际已root核，Source6有限通过：trajectory×views分母/camera action校准，top/side反退，不授fresh独立demonstrations/免费校准/PoE精确recipe。OmniVoice00688 2.1.1/2.1.2输入/outputheads及Tables5–8原证实际已核，Source6有限通过：fullCB mask/loss与推理顺序分责、ARinit改双向仍需适配，低ASR不授超真实speech、600语言全测或固定steps全费用。SCT00733实际§3/4.1–4.4/5已核5分纠错深入通过，rank参数化精确gradient/简化70Bshape单step非完整70B LM，PPL/LR不匹配与QR費保留。OptimSyn00536 Alg1/2.3/MedQA test reward/E4原文实际已核，成熟IF×GRPO rubric生成具体EX独核通过；保test-selection污染负侧，不按医疗标签关闭、不外推全实验无效。其它Source/PRE/POST/DAY不由本回执继承。

仅原题摘集合，实际方法/直接评价/负侧已读到采用命题；root准入/Source仍待核，不计候选或Books锁。

## 00536 OptimSyn：拟贡献前EX，另保评价污染负侧

[v1](https://arxiv.org/html/2604.00536v1)§2.2/2.3/3.1/3.3/6原证：实际借用LESS/TracIn Adam-compatible cosine影响分数，把它和format/nontrivial/safety checks作为rubric generator的GRPO reward，经teacher生成QA再给target-gradient反馈。原文适配既有影响估计和RL rubric搜索，没有新优化operator、估计资格或失效条件；embedding近≠训练效用的局部关联是成熟梯度proxy原则的又一实例。HSS 2K/4K随机subset IF与accuracy R².57/.54非独立因果，不能由“verifiable reward”取得truth或真实utility证明。§3.1原文MedQA test用于reward validation且又报MedQA评价，decontam训练字符串不能消除其选择污染；这一重要反侧保留，不为排除而删。拟EX基于成熟组合、未新增准入机制，不以医疗领域/小模型标签关闭或用访问/工作量缩池；若root认为target-conditioned rubric对独立目标的反证确有差额请重开具体命题。主线HSS不被Science暂缓误排。

## 00557 Camera view scaling：拟2+2+2=6

[v1](https://arxiv.org/html/2604.00557v1)III-B～D/IV-A～B/TablesI～IV：同物理trajectory同步多cam构pseudo-demo N×V，不是新增human轨迹；base/EEF动作随view不变，camera动作须extrinsic转Δp/ΔR，camera-space非任意增广标签保持。DiffusionPolicy/DINOv3-base+LoRA、robomimic3tasks与一次waterpour实任务有限；15°邻view有益，top/side或30°更远view在fixedfront测试反退(0.24/.40低.26/.42)，多样性不能替deployment-view匹配，EEF差不证明坐标本质无效。camera校准额外劳动，与“无新增人力”分开；独立示教数/视角样本/训练compute不等。可采用sample分母与view/action合同、coverage反侧；PoE式部署聚合Eq9/Alg1坐标外层v歧义，不采用精确多cam sampler或安全控制，原动作闭环仍外部拥有。

## 00688 OmniVoice：拟2+2+2=6

[v1](https://arxiv.org/html/2604.00688v1)§2.1.1～2.1.2/3/4.1/4.3Tables5～6：独立entry mask所有8acoustic codebooks、同time embedding求和但独立prediction heads，loss对所有masked entries；NAR直接text→acoustic与semantic-cascade不同，但不承诺所有error propagation消失。Qwen3-.6B因果weight→bidirectionalbackbone仍须训练适配；Emilia same300Kupdates对照fullCB mask与single-CB loss、randominit多LR表支持局部稠密监督/初始化，不证明pretrained linguistic knowledge唯一因果。Higgs codec/8H800 BF16/8192pack，32step unmask+lowercodebook penalty/CFG2仍有sampling顺序和费用。600+训练语言但FLEURS只102/24benchmark，ASR各域evaluator不同、生成WER低GT不授优于真实语音。更多每step loss entries不是同compute更快，语音质量/时长/吞吐与promptnoise分开；只采用fullCB训练与推理顺序分责，不把规模/榜位计新机制。

## 00733 SCT：拟2+1+2=5，headline纠错范围深入

[v1](https://arxiv.org/html/2604.00733v1)§3/Alg1/4.1～4.4/5：permanent U diag(s) Vᵀ+AdamW后QR Stiefel重traction只该rank参数化gradient，不是densegradient或梯度消失。实际70B-class **additive attention无softmax/masking**、452M spectralparams只一step可运行，非完整70B语言模型训练；1.7B反侧只MLP转，attention/embeddingsdense。Alpaca2000steps/b4/A10040G，denseLR2e−5 vsSCT5e−4不匹配；PPL65.6～86.9远劣3.6、135M95%energy PPL1.8高1.3，不能将质量差已归因LR无capacity约束（§5承认未conclusive）。QR在shape mock40～50%step，pretrain到收敛尚future。新采用是storage factor model≠dense capacity、shape feasibility/quality/optimizer成本分开，拒绝8GB训70Bheadline，不以scope标签EX；成熟SVD/QR组合自身不另计机制。无代码/复现认证。
