# 01/31 首批必要证据与 Books 窄差额（作者判断，待 root PRE）

身份均为精确 arXiv v1，原题摘见 ABSTRACT_FIRST_ADMITTED.jsonl，正文分别 CORE_22156v1.txt、CORE_22101v1.txt、CORE_22158v1.txt。没有使用后续 v2/v3 当历史事实；未核 artifact、未复现。日期尚待独立处理，下面不是落窗确认或日级完成。

## 2601.22156 HALO/HypeNet

拟评分2+2+2=6：低预算hybrid迁移与position分工是新增受限机制，跨checkpoint训练/模型状态接口；不借成熟hybrid、机构、绝对speedup或NIAH大数增分。标准机制与评价已读足；因需要核具体owner差额，直接相关附录补读，不扩全附件。

- §4.1～4.4：Q/K/V/O权重初始化；逐层MSE重构teacher hidden，冻结其他组件；按recall与CSR变化选择难转attention；stage2 KL teacher蒸馏，再stage3长窗adapt。选择探针是受限任务集合，不能证明任意使用场景层重要度。§6.5只替换layer-selection办法，未复跑Jet-Nemotron/KL-LS整套高预算流程，因此不能称全方法公平优胜。
- §5.1/Eq11：RoPE用于RNN、NoPE用于attention，推理attention logits以`log_a(t+a)`随位置缩放。§6.3/F1：500M从零、20B tokens的HyPE对照与constant/no scaling消融支持本架构长度外推；data-independent Lightning decay优于所测data-dependent mixers，但其归因仍是作者解释，不是证明forget-gate的普适方向。
- Table3：2B conversion在128K NIAH为79.9，去RNN RoPE47.9、attention添RoPE19.7、去RNN QKnorm17.3，支持组合里的position/稳定性选择；去GQA→MHA反而83.5，去attention gate80.9。不能把每项改动都写成所有长度单调改善。
- Table4：teacher CSR58.5仍高于HALO55.9，而长NIAH128K38.6→79.9/256K18.4→74.3；短能力代价保留。E2说明Qwen超40960长度用官方YaRN，不把未扩展teacher作为唯一对照。
- E/Table8：320M+1B+1B训练tokens，layer-selection另234M inference tokens；A800 GPU-hours91.1不含selection N/A。B各阶段context4K/8K/32K、AdamW β.9/.95、warmup2%/cosine；2.3B不含所有搜索成本，不等wall-clock同比低预算。GQA→MHA增加参数，HypeNet2/5/9B不是严格同参数的1.7/4/8B。Appendix C Table6把RNN/attention layer counts与§4.3选择比例及Table7不一致，不能照录该表的层数执行配方。
- §6.1/E1/E2：单A800-80GB，BF16，batch1；PyTorch2.9.1/CUDA12.4/FA2 2.8.3/Mamba2 CUDA2.3/FLA0.4.1。NIAH平均Single1/2/3、CSR七任务、LM-eval0.4.10.dev0；concurrency/SLO与runtime tail Not Disclosed。512K宣称3×decode、3.4×prefill只属于上述配置，不认证生产服务。

Books实际读取：Ch22 `从Dense Checkpoint迁移到Hybrid State Model` 855～873已承载layer probe→保留hard attention→distill→long calibration及teacher/layout/gate/position/kernel成本，不是只有HALO引用。Ch13 `局部混合可以产生隐式位置，但读取它仍有条件` 216～223已承载local/recurrent携带position→global NoPE读取及长度/任务条件。作者拟 `已有覆盖`（MODEL-LONG-CONTEXT，Ch22主owner，Ch13只交接）；HyPE的具体log-scaling与该架构局部得分仅报告，不把新配方默认长期缺口。请root核这一判断；没有申请Books写锁。

## 2601.22101 ECO

拟评分2+2+2=6：新增persistent-state分配与量化误差反馈取舍；不为量化/EMA成熟原则增分。§3/Alg1/Theorem与§4各实验/limitations已读。

- 精确SGDM master-equivalence需保存前次error并以`e_t/eta-e_(t+1)/(eta*beta)`反馈，增加buffer。实际ECO用相邻误差近似，以`(1/eta)(1-1/beta)e_(t+1)`注入momentum来避免额外persistent error state，非trajectory等价。AdamW按per-parameter effective eta调整；高精度m/v仍保留，不能叫所有训练状态无buffer或无temporary。
- Theorem只在Lsmooth、unbiased/bounded quantization variance、bounded gradient等SGDM假设下得constant neighborhood；噪声floor含`4L² sigma²/(1-beta²)`，decaying eta不消除它。deterministic rounding bound更差，不能把SR定理给RTN或无条件AdamW收敛。
- Table1 C4 30～800M，100N tokens，batch512/seq512，AdamW β.9/.98/eps1e-9/wd.1、clip1、10%warmup+cosine；只block线性量化，不含embedding/head。800M master-RTN val2.5343、ECO-SR2.5399、naive-SR2.9471，ECO-RTN2.6046；master-SR800M N/A原文说数据丢失，不补填。Gemma3 1B40B C4与不同预算不合并为同实验。
- 2.1B SMoE 32experts/4active/24layers/hidden576、只expert线性FP8、LM1B 100×active tokens，checkpoint activations、无gradacc，static/peak权重状态主导时12→9 bytes/param约25%；非所有训练显存25%。DeepSeekMoE16B INT4 weight-only QAT，OAguanaco3epochs，seq2048 micro1/acc16、wd0/warmup3%，不是all-op INT4实测加速。
- Hardware型号、精度以外runtime版本、真实E2E吞吐/并发/SLO Not Disclosed。作者称少量elementwise overhead不等实测negligible；不采用无条件“near lossless”。

Books实际读取：TRAIN-PRETRAINING/Ch28 `低比特Training Graph：无偏不等于免费` 1010～1030已明确删除master引入rounding bias→residual进既有momentum→state/checkpoint身份、finite horizon/optimizer边界及BF16/FP8回退。作者拟 `已有覆盖`；本日新理论与局部Pareto证据收窄该已有机制，不新增checkpoint执行规范或单独噪声floor小节。请root核实际命题覆盖，未写Books。

## 2601.22158 pMF

拟评分2+2+2=6：output/loss-space解耦与高pixel维度成立边界；不借MeanFlow/流形假说本身或2.22宣传分数增分。因发现owner实际没有此接口，定点深入以支持窄Books差额，非为凑7分。

- §3～4/Eq8～12/Alg1：t=1 noise、t=0 data，`x=z_t-t*u_avg`，network直接输出x再变换u；u的JVP经MeanFlow identity变成velocity loss，prediction space不等loss target。一般0<r<t的x不能保证位于data manifold，§4.1明确承认；仅边界/图示支持经验假说，不写流形定理。
- §5 toy为同7层256-width ReLU、2D data嵌入D2/8/16/512；支持高观测维度下target可学性分化，不证明真实image的固有维度。
- Table2固定序列16²、Muon/MSE160epochs/ImageNet FID50k、同backbone且无bottleneck：64px patch4/48dim x3.80 vsu3.82；256px patch16/768dim x9.56 vsu164.89，支持具体高patch-dimensional regime而非所有velocity prediction失败。
- Fig3：Muon vsAdam320epochs11.86→8.71；感知loss baseline9.56→VGG5.62→ConvNeXt3.53。Table3 linear/EDM/sCM preconditioning34.61/14.43/13.81 vsdirect3.53。Table4只r=t194.53、只r=0389.28、两条线106.59 vsfull plane3.53；多个变化分账，不把最终2.22全部归因核心parameterization。
- Appendix A Table8：B/L/H16/32/48depth、hidden768/1024/1280，batch1024、Muonβ.9/.95、constant1e-3、warmup0、160/320/360epochs、r≠t50%、logitnormal(.8,.8)；JAX/TPU，具体TPU型号/数目/precision/真实端到端latency/concurrency/SLO Not Disclosed。FID选择best guidance interval/scale与EMA，不等完全无调优预算。感知loss低噪t≤.8、随机crop224；它增加encoder训练成本，1NFE只统计generator调用。

Books实际读取：Ch24 Flow Matching157～196定义概率路径/velocity、训练vsODE及求值成本；并行少步439～457区分trajectory、MeanFlow head和NFE，却未承载image output/velocity loss分离。相关Ch23 encoder/codec信息损失与Ch25 action/environment交接已读。窄差额只应在Ch24既有Flow Matching段加入两段：①多步/latent合理条件→pixel高维capacity问题→直接输出image-like field但转换到velocity-space监督；②转换与JVP/时间采样/感知loss成本、一般r流形未证明、同预算高维Table2及低维无优势、退回latent或多步。不写新论文小节、不采用宣传终局FID/生产保证。请求root必要原源→owner PRE，并在通过后才协调`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`单文件窄锁。
