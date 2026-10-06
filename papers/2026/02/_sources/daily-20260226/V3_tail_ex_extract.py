import pathlib,json,re,html
ROOT=pathlib.Path(__file__).resolve().parent
known=set()
for name in ['V3_CURRENT_ABSTRACTS.json','V3_LG_NEW_ABSTRACTS.json','V3_AI_NEW_ABSTRACTS.json','V3_CROSS_NEW_ABSTRACTS.json','V3_CROSS_TAIL_ABSTRACTS.json']:
 known.update(x['id'] for x in json.loads((ROOT/name).read_text()))
known.update('2602.'+s for s in ['20303','20324'])
reasons={
 '20165':'心内超声定位心律失常的领域诊断网络，不是多模态基础模型表示机制。',
 '20168':'急诊分诊/病情恶化预测的医学传感与benchmark，不作为模型机制新证据。',
 '20169':'AI财产权/ownership规则讨论，非执行state/permission/runtime ownership机制。',
 '20176':'手性蛋白/肽相互作用设计，暂缓AI for Science领域研究。',
 '20177':'MOSFET冷却速度/PINN物理热设计，非大模型accelerator执行或模型训练机制。',
 '20178':'MIMO无线信号检测网络与其领域泛化，不将通信符号检测当训练通信/runtime机制。',
 '20181':'LLM服务住宅能源改造决策的应用，非模型学习/Agent执行机制。',
 '20187':'病理whole-slide区域异质性的领域实例学习，不是foundation路由机制。',
 '20195':'有机晶体结构生成，暂缓AI for Science领域研究。',
 '20198':'促炎肽feature融合预测，暂缓生命科学领域模型应用。',
 '20199':'区域划分/元启发式ensemble用于imbalanced分类，未以当前foundation训练operator为研究对象。',
 '20206':'新手编程教育中metacognitive scripts干预，非模型本身的学习或系统执行机制。',
 '20209':'肽序列质谱反演与质量约束的科学任务，不据diffusion名词引入生成owner。',
 '20210':'晶体多模态建模，暂缓AI for Science研究路线。',
 '20224':'LLM/主题模型用于抗衰老文献分析，非模型表示/系统机制。',
 '20271':'配送延迟时长的领域多任务预测，非模型runtime/SLO调度。',
 '20289':'MRS/GABA定量sim-real验证，暂缓医学科学任务，不泛化为VLA sim-real机制。',
 '20297':'完整v1 AB拟EX：LSVI-UCB++线性Q探索gapregret/并行探索samplecomplexity，未建立foundationpolicy/神经训练operator/runtime桥；新理论增量非无贡献。',
 '20306':'心脏力学surrogate/生成增广，暂缓AI for Science领域研究。',
 '20316':'太阳观测rare-event探测，暂缓科学观测应用，不将rare-event词挂安全评估。',
 '20317':'核聚变/生物声学时间序列信号提取，非当前foundation表示或执行机制。',
 '20344':'分子fragment self-supervised表示，暂缓科学分子建模。',
 '20361':'OFDM接收器/DMRS检测中的continuallearning，非训练runtime通信或foundation持续学习接口。',
 '20376':'完整v1 AB拟EX：Max3Cut低秩objective候选枚举/exactmaximizer与近似保证，不是模型低秩训练/量化/compiler对象。',
 '20383':'异质处理效应中的groupbias统计，非模型输出群体偏差或基础模型训练机制。',
 '20394':'完整v1 AB潜在IN待独校：learnedMRF→AR order→restrictedconditionalset/modelcomplexity；Ising仅局部实验，不仅科学域标题EX。',
 '20442':'电子病历缺失值插补，暂缓医学领域应用。',
 '20449':'完整v1 AB后once待独校：PLM/NL层头信息差与earlyexit，核是否operator受控新条件而非成熟earlyexit蛋白应用；不采用科学任务结果。',
 '20465':'激励相容探索机制，经典机制设计对象而非foundation/Agent执行模型接口。',
 '20475':'HL-LHC粒子信号物理purification，暂缓科学领域模型。',
 '20486':'LLM对话支持学习者reflection的教学互动设计，非模型自反思训练或执行contract。',
 '20500':'腹腔镜camera控制的领域graph mining，非VLA/基础模型物理行动机制。',
 '20527':'教学策略apprenticeship学习，非当前foundation学习/执行主线对象。',
 '20539':'UAV林业中stereo/SAM组合应用，不是foundation模块的新成立条件。',
 '20541':'maximin share公平分配保证，经典分配理论，非模型MoE/训练资源placement。',
 '20547':'学生使用AI chatbot的technologyacceptance调查，非模型/Agent系统机制。',
 '20611':'actigraph时程数据Bayesianinference应用，非基础模型后验/训练更新机制。',
 '20634':'社交hate-speech分类器/文本变换比较，非基础模型安全counter或训练更新机制。',
 '20636':'手术注意tracking的proposal rerank/motion refinement，非foundationattention机制。',
 '20643':'城市出行轨迹GPT/RL领域生成，非foundationpolicy/runtime的新机制说明。',
 '20658':'VLM估手位置服务人体工效评估，非VLA闭环或新视觉表示机制。',
 '20676':'CTR/relevance推荐框架与encoderdistillation组合，标题未给直接LLM信息损失/训练更新新条件。',
 '20677':'城市时空foundation模型的领域路线，不按foundation/scaling措辞推定通用架构贡献。',
 '20709':'空间相机straylight分割，非大模型端侧推理runtime或生成机制。',
 '20712':'太阳F10.7指数小波/多尺度预测，暂缓科学领域应用。',
 '20744':'Kurdish maqam演唱错误检测，音乐任务应用非通用音频基础表示机制。',
 '20752':'肌骨MRI interpretation的领域模型，暂缓医学科学任务。',
 '20805':'speech spoofing中的speakeridentity评价，非已见foundation训练/推理机制改变。',
 '20857':'完整v1题摘另核：C1时序拟合/JAX与CNNfeature增强，无直接foundation/operator新成立条件；见V3_TAIL_TITLE_REPAIR.md。',
 '20877':'电商multimodalknowledgegraph框架，非LLM-RAG索引/Agent检索机制。',
 '20925':'热成像stereo SLAM的经典几何系统，非foundation persistentstate学习机制。',
 '20946':'AGI经济学分析，非模型能力形成或runtime机制证据。',
 '20958':'EKF/deeplearning用于UAV距离估计/SAR following，非VLA/基础模型控制接口。',
 '20994':'MRI报告监督脑病变分割，暂缓医学领域应用。',
 '21033':'医学图像处理PyTorch框架，暂缓医学应用，不按框架名准入。',
 '21036':'完整v1 AB拟EX：CIT adversarialfeature/response函数与monotonep calibration/FDR，无实际foundation训练/读出桥；非所有因果理论范围外。',
 '21052':'next-item推荐的positionattention，非通用Transformeroperator新条件。',
 '21116':'非地面无线网络SINR估计，非大模型Attention机制或推理通信runtime。',
 '21119':'实体craft robots的团队竞技策略，非VLA/foundation学习接口。',
 '21130':'projectionpursuit treeclassifier/可视化评价，非foundation表示/训练operator。',
 '21136':'半结构访谈HCIinsight工具，非模型/Agent执行机制。',
 '21138':'L1 PageRank经典加速复杂度，非LLM GraphRAG索引/模型operator的新成立条件。',
 '21142':'纵向放射学prognosis/diagnosis模型，暂缓医学科学路线。',
 '21165':'患者声音文本检测领域工具，暂缓医学应用，不作为foundation行为机制。',
 '21174':'多分辨率3Dgrid传统any-angle路径规划，非模型驱动planning/worldmodel/VLA接口。',
 '21178':'LLM辅助脑肿瘤分析，暂缓医学科学应用。',
}
found={}
for name in ['V3_ARXIV_LG_LIST3.raw','V3_ARXIV_CV_LIST2.raw','V3_ARXIV_AI_LIST2.raw','V3_ARXIV_AI_LIST3.raw']:
 raw=(ROOT/name).read_text()
 for m in re.finditer(r'href\s*=\s*[\x27\x22]/abs/(2602\.\d+)[\x27\x22].*?list-title mathjax.*?Title:</span>(.*?)</div>',raw,re.S):
  identity=m[1]
  if '2602.20162'<=identity<='2602.21206' and identity not in known:
   found.setdefault(identity,(html.unescape(re.sub('<[^>]*>','',m[2])).strip(),name,raw.count('\n',0,m.start())+1))
assert len(found)==67,len(found)
assert set(reasons)=={i.split('.')[-1] for i in found if i!='2602.20947'}
out=['# 有限tail范围提案：60title EX、4完整AB EX、2potential与1once待校准','',
 '只复用上述四份既有tail原页ID20162–21206。原69减20303/20324既有AI11-title EX为67；20947完整题摘发现potential，另见V3_TAIL_TITLE_REPAIR.md，不放下表。',
 '以下为作者范围提案与来源定位，未宣称root逐项或分层验收。20947完整题摘暴露一般理论题名未声明foundation不足关闭的共同风险；只20297/20376/20394/20449/21036五项定点完整AB重开，具体原证/日期见V3_TAIL_TITLE_REPAIR.md，不读全文，不连带其他清楚应用。标题记录不等已读摘要/正文；没有已见纠错/安全标题标记不等逐站版本史安全证明。','',
 '| ID/原目录标题 | 具体范围理由（非领域价值评价） | 原始位置 |',
 '| --- | --- | --- |']
for identity,(title,name,line) in sorted(found.items()):
 if identity=='2602.20947':continue
 short=identity.split('.')[-1]
 prefix='' if short in {'20297','20376','20394','20449','21036'} else '拟EX：'
 out.append(f'| [{identity} — {title}](https://arxiv.org/abs/{identity}) | {prefix}{reasons[short]} | {name}:{line} |')
(ROOT/'V3_CROSS_TITLE_EX.md').write_text('\n'.join(out)+'\n')
print('tail proposals: 60 title EX / 4 full-AB EX / 2 potential / 1 once; independent calibration pending')
