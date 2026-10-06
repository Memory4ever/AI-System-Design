# 有限余项第四批决定性Source

仅现有68完整题摘集合，无新发现；下列原文必要方法、评价及直接反侧已实际读到拟采用判断，不授root Source或Books锁。

## 00055 VLLR：拟2+2+2=6

[v1](https://arxiv.org/html/2604.00055v1)III-A～D/IV-A～E/Alg1/TableIII：VLM progress偶发高峰会让running-max后续增量长期归零；离线trajectory的邻窗median排除当点高峰，再转progress增量。此窗含未来observations，仅rollout之后的value初始化，不授因果部署sensor。200K步VLM value warmup后停止查询，PPO改用self-certainty和sparse task成功；self-certainty实际uniform||policy的reverse KL，非成功/世界模型真值。SPOC/CHORES两个384×224相机/20动作，20M/50M训练、α1/β.1/φ10，Fetch Full SEL63.2低于VLM63.8，RoomVisit SEL低FLaRe；certainty过重会forget/collapse，trajectory因果分析未做。新边界是spurious peak如何破坏monotone reward及昂贵sensor只初始化value，不采用通用confidence=correctness。噪声窗/阶段分离消融不充分，保局部归因；无现实控制/端到端VLM费用保证。

## 00421 Self-Routing：拟2+1+2=5

[v1](https://arxiv.org/html/2604.00421v1)§2～4/Table1～2：last N hidden坐标直接作logits，top-k及加权expert保持；backbone仍end-to-end学习，router无参数不等routing不学习。12-layer GPT2小型8expert/top2、OpenWebText/context1024，同骨干/预算且均无aux loss；随机fresh assignment显著差，fixed random projection也有竞争力。Self routing WikiText27.4不及learned26.7；节省.07M/520.81M，不采用巨幅降本。4.43M routed tokens的平均entropy较高仍非每batch容量/通信平衡，early2expert集中；DeiT单设定仅局部。新增content routing不必独立projection这一具体替代，但非所有MoE/部署免load balance；未披露重复run/硬件/完整token-budget，不采用性能普遍保证。

## 00666 TRIMS：拟2+2+2=6

[v1](https://arxiv.org/html/2604.00666v1)§3/Alg1/§4.1～4.4：AR teacher-forcing NLL不是实际DLM trajectory；跨训练token quantile分桶，hard bucket较早，随机threshold让上下文/未来mask概率.05/.95；仅10%数据用此结构，ELBO不变。随机bucket本身也改善，hard-first额外margin有时小，不能只把收益归给difficulty order。s1K、Qwen3-8B教师、LLaDA/Dream、LoRA32、1024seq、30epochs、8A10080GB，TPS是tokens/step非wallclock/SLO。LLaDA HumanEval37.2低原38.3，Dream GSM80.3低原83.9；distillation93K/6epochs vs1K/30非同预算，0.6GPUh只是curation。新选择是以可复用AR顺序代理控制corruption结构而不收集每target采样trajectory；不授真实困难/最优reveal顺序，40例轨迹分析用同teacher，不独立证明因果。

## 00716 CircuitProbe：拟2+1+2=5，中心定位争议应隔离

[v1](https://arxiv.org/html/2604.00716v1)§4～5/8：层变化derivative-stability与绝对anomaly两分数max，10～50calibration examples只排名duplicate块，不证明reasoning定位真值。Tables/正文冲突：Table1 Qwen7B预测[6–11)，§5.3却说top是3–6；Mistral表3–6而验证说2–5；Phi表5–10、groundtruth6–11排名6。不能以top1命中采用定位或architectural invariant。250题评分包含expected-answer substring、GSM数字matching；Qwen3B+4.8而7B−1.6，Mistral7B targeted probe提高但broad−5.6。保局部targeted-vs-broad反证，不把3B阈值普遍化或CPU/GPU异资源比当公平speedup。中心位置矛盾请求作者准确index约定/预测与验证对应表，当前不入Books；如只受限采用额外pass并非免费、能力收益应独立任务测，是边界命题但须root裁决是否仅报告或中心争议。

## root 非作者实际必要原证复核回执

root 实际核 00055 Alg1未来窗口median、value warmup后不再查询VLM；00421 §3 last-N坐标/TopK及Table1 27.4vs26.7与fixed-random反侧；00666 bucket/.05/.95/10%及HumanEval/GSM反退，三项限定Source通过，原6/5/6分可继续唯一owner/PRE。00716原Table1 Qwen[6–11)与§5.3 3–6实际冲突已核，2+1+2=5中心定位争议/noBooks通过；恢复准确索引约定、预测和验证对应表才重开，不以未经验证解释抹除冲突。此回执不授PRE/POST或日级完成。
