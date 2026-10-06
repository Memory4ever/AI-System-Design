# 01-30 第三批准入项：必要证据（root必要命题/反侧实际复核通过）

均为链接所示精确 v1；未运行代码、复现实验或验证生产能力。分数只针对新增命题。原文缓存为同目录 `V3_CORE_<ID>.txt`。日期字段与窗口推定另见本日报；以下不授早提交材料日期。

## [Sokoban / 2601.20856](https://arxiv.org/html/2601.20856v1)

2+2+2=6。§3–4：一箱直走廊长度5–100、四旋转共80地图；GPT-5/GPT-oss-120B/DeepSeek-R1，8次重复，最多32768输出token。LLM-Modulo以GPT-5-mini生成PDDL problem，人核domain、FastDownward/PyperPlan、60秒/3次上限，4次重复。必要反侧是§4.2：320个problem只有7个语法错误，但语法通过仍会把地图尺寸/位置写错，solver只能证明它收到的形式状态；换旋转/换行也会改变难度。不能把该局部计数/转译失败变成所有规划的25–30步阈值、指数复杂度定律或端到端可靠性；75分钟是收集总时间，不是请求延时。暂拟仅报告：局部PDDL输入忠实性证据，不由特定走廊阈值改写通用规划机制。

## [Referential games / 2601.20641](https://arxiv.org/html/2601.20641v1)

2+2+2=6，受影响的隐蔽通信主张深入。§3、§5–7：sender见10图及目标，receiver相同图片不同顺序；共享协议与独立创造协议不同，overseer同架构但不知道协议。自然/高效/隐蔽是明确提示条件，不是无提示自发串谋。GPT-4o、Qwen2-VL72B、Pixtral12B、Llama4-MaverickFP8，COCO/CLEVR/真实及合成旗帜，300局；局部std最高.029。15名人类、自然/隐蔽最多5词、高效1词，条件长度不完全匹配。§5人类表中GPT隐蔽成功.53、人类.31，不能外推任意带宽或所有模型协作；独立协议接收者损失约.1–.4也说明共同可解码结构的条件。仅报告：受提示、10目标、英语视觉游戏的局部反侧，不授现实隐蔽串谋或安全保证。

## [DAT / CDAT / 2601.20546](https://arxiv.org/html/2601.20546v1)

2+1+2=5。§3 DAT用首7个合法WordNet名词的SBERT平均距离，500回答，温度.5/1/1.5另单次0，500随机名词/显式作弊对照；随机无关词可取得更高novelty，不能把这个指标称全面创造力。§4 CDAT 539 cue先要求语境关联：对random进行two-sided Welch检验、每温度FDR α=.001，且模型均值高于random；通过后仍以novelty为标量，2D Pareto仅诊断。所有模型通过门槛；99人类样本、70cue、11评者不支持普遍人机排名或温度因果。仅报告：英文词嵌入评价的具体混杂/条件门，不把此阈值作为通用创造力判据。

## [Abstention RL / 2601.20126](https://arxiv.org/html/2601.20126v1)

2+1+2=5。方法/实验/讨论：MedMCQA添加IDK选项与Hendrycks数学开放答案，正确1/错误-1/拒答可调；Granite3.3-2B和Qwen3-4B，GRPO LoRA，TRL，lr2e-5、8样本batch/64积累、group8、最大500步、prompt256/completion1024、bf16 A40/A100。8k训练、约100评测，RL-only/SFT随机30%IDK/R-tuning按base错误IDK；答案准确率与拒答召回分别度量。Qwen拒答reward .3局部拒答41%/错误10.3%，不等真实性或医疗安全。文末直接反侧：SFT或R-tuning的IDK比例可压倒学习，拒答与能力不能同看单一正确率；所谓最优比例尚未系统测量。仅报告：两模型有限奖励/数据条件，不从成熟三元reward推普遍探索定律。

## [Agent PR density / 2601.20109](https://arxiv.org/html/2601.20109v1)

2+1+2=5。方法及§6：AIDev33,596 PR→8,106 fix→1,802 Python→1,210 merged、206 repo，Codex949/Copilot106/Devin100/Cursor40/Claude15。SonarQube同配置比较base/merged，新增issue密度分母为added+deleted LOC。raw count差异大多在按churn归一后不显著，Cursor局部例外；不显著不是质量等价。静态code smell/security hotspot不等确认的运行漏洞，无人类反事实、选择偏差、小agent样本、Community edition限制。仅报告：本语料静态比较中的分母混杂；不授Agent排序、merged即安全或泛化修复能力。

## [SS-MAE / 2601.20072](https://arxiv.org/html/2601.20072v1)

2+1+2=5。方法/评价：ViT-B16、75%patch mask；弱强增强均>.95信心且标签一致。warmup10epoch，可信验证样本准确率≥70%才启pseudo，连续n个epoch低于阈值禁用（n具体未披露）。CIFAR10/100上采样224、10–40%labels、200 pretrain/100 fine-tune、AdamW lr1e-4 wd.05、labelbatch16/unlabel32。Table3 CIFAR10/20%labels全机制66.40 vs首epoch启pseudo62.37/不设val gate63.49。未提供强FixMatch基线、硬件、重复CI，不授通用SOTA或LLM伪标签条件。仅报告：验证准确率控制伪标签介入时机的局部配方，具体70%并非跨任务稳定常数。

## [AutoOverlap / 2601.20595](https://arxiv.org/html/2601.20595v1)

2+2+2=6。§3/5：logical chunk介于global tensor与compute tile，显式(rank,index)依赖，用户注释tile size/index/scheduler；从partition/loop IR取通信计划，构图插wait，swizzle tile schedule而非搬数据；同一logical plan可lower copy engine、专用/共置SM TMA或load/store，调chunk/SM/tile/通信backend。§6固定高层计划对比Domino/Alpa/Mercury，8×H100 NVLink900GB/s、CUDA12.9/NVSHMEM3.3.9/PyTorch2.7，同栈，多种GEMM/attention算子shape来自Llama3/Qwen；不是完整训练step/服务SLO。人工最优GEMM平均4GPU99.8%、8GPU104%，小7B/8B GEMM-AR仍落后TritonDistributed；图11最佳chunk非单调、过细同步开销、过多SM抢compute。仅报告：特定算子自动lowering接口和实测实现，不把tile/通信共同依赖这个成熟原则作新长期缺口或宣称通用无注释自动编译。

## [StreamFusion / 2601.20273](https://arxiv.org/html/2601.20273v1)

2+2+2=6。§3–4：Ulysses跨机减少volume、Ring机内；Pu=gcd(NM,H)受head divisibility约束，Pu=2是volume例外。Torus利用all-to-all原地head chunk先compute，再Pull Q/Pull KV/Push O流水，partial softmax输出须合并；NVSHMEM put/get与stream内顺序/barrier保持数据一致，仍有层始末跨机同步，不是任意无同步读写。§5四AWS p4de.24xlarge各8×A10040GiB、NVSwitch/EFA400Gbps，CUDA12.8/PyTorch2.8/NCCL2.27.3/NVSHMEM3.4.5，Flux12B 3072/4096图、CogVideoX5B 20/40秒768×1360，评价一次sampling step，不是全视频请求SLO。TAS两机反差于USP；>2机平均1.27×，完整SF比TAS1.35×。AppendixB：Flux短序列NCCL Torus不提速而one-sided有益；video Torus已隐藏通信，one-sided边际小。序列>160k且D32可不胜；不得只说拓扑反转普遍更优。仅报告：该布局/两类DiT负载下backend与序列共同影响机制收益，尚不把此布局统一替代现有混合SP设计。

## [VersaQ-3D / 2601.20317](https://arxiv.org/html/2601.20317v1)

2+2+2=6。II-D/III：VGGT通道是较广分位持续saturation非仅孤立spike，WHT单独仍残variance；离线WHT+LayerNormγ融合+DCT weight，在线IDCT/BF16 RoPE再WHT/INT，持rotated activation减少额外WHT，未校准数据。IV两遍score重算只存softmax统计、INT4/8/BF16重配置；不能把数学未量化的orthogonal等价授低比特数值等价。V官方VGGT1B、Co3Dv2单序列8.9GB/15scene及7-Scenes7scene；W4A8 AUC@30 .9553 vsFP.9719，但AUC@3 .5931 vs.7536；W4A4 AUC@30 .5617仍显著落于FP，不照录‘98–99%所有精度’。III硬件是RTL/synthesis TSMC28nm1GHz、cycle simulator、Ramulator2 LPDDR5-6400 102.4GB/s，Jetson XNX20W/ONX25W实测功耗，不是流片实测。3.88mm²/2.18W和10.8×等为作者模型条件，未运行。仅报告：VGGT量化形态与模拟加速器的局部反侧，不能证明所有多视角transformer校准无效或所有低bit正确性；旋转/精度合同的成熟原则不重复建owner。
