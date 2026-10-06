# 第十二批必要原源与受限采用

## 最后四项：必要证据与Books处置已root独立通过

### 2602.15539 DynamicFusion

精确[v1 §4–5](https://arxiv.org/html/2602.15539v1)，本地V3-exact-v1/2602.15539v1.html。Eq13按输入、layer和step硬择subject/style LoRA，不是连续融合权；KL扰动未定义完整概率归一，不采用严格KL理论，CLIP/DINO采样guidance是成熟组件。SDXL1.0；subject DreamBooth4–5图/style StyleDrop1图，各r64/1000steps/B1/LR5e−5，FLUX公开权重另有人口不合并。30pairs×10生成、消融25pairs；Table3 FLS DINO40.1→43.7但style60.3→59.5，LLR style66.1>joint64，joint DINO43.4<FLS43.7；Table4 dot43.8>KLDINO43.7，Table5更大m可style升而subject降。额外分支feature与采样guidance付费；HW/precision/总runtime/重复seed未披露不补，human/LLM喜好不当truth。2+1+2=5，因具体adapter execution gap定点深入，不扩FLUX附件。

### 2602.15400 GTA

精确[v1 IV–V](https://arxiv.org/html/2602.15400v1)，本地V3-exact-v1/2602.15400v1.html。TSDF metricstate和校准四view/BEV grid，经viewID/normalized coordinates→raycast生成真实waypoint再交localplanner；只采用接口条件，不采semantic reasoning自签物理有效/安全。R2R unseen1839/RxR subset260，消融curated180，SR三米停止与OSR非同量；TableI RxR46.2与文字42.2/curated口径不混。EWR消融未拆view/grid/graph；PB45→47.2局部，三backbone点不证明规模因果。真实50navigation trials，TurtleBot4/D455/Nav2与UAV/D435/外部mocap，远程HTTP计算费用/延迟及碰撞率未披露；40/42%不是安全保证或全robot泛化。2+1+2=5，因坐标接口gap定点深入，保传统已校准geometry/localcontroller。

### 2602.15749 GenAE

精确[v1 §2.1–4.4/Table1](https://arxiv.org/html/2602.15749v1)，本地V3-exact-v1/2602.15749v1.html。encoder把downsample前移residual且可用separable convolution；decoder的同变更触发CUDA slow-GEMM fallback故刻意不采，不能把两侧层同名视为同执行收益。2×60sec stereo44.1k/bf16速度消融HW未披露：ELU4.5%、前移36.1%、separable6.5%，13.9x bundle含aggressive层数变化，不唯一归因。25Kh instrumental/8A100一周，SAO32A10019天非matched；RVQ另4A1004天。13.125Hz GenAEVQ mel.5956弱于DAC.5144，36.75Hz改善但付更高rate；CoDiCodec主观与指标分歧。40GB/bf16/B8/80%activation预算的832s context为下游假设估计，CoDi993s更大，不是实测generation/SLO；M/S格式切换只已训format。2+1+2=5，实际质量/资源选择gap定点深入，不授零训练或总系统加速。

### 2602.15763 GLM-5

精确[v1 §4.1.1–4.1.2](https://arxiv.org/html/2602.15763v1)，本地exact-v1-bodies/2602.15763v1.html。TITO保原sampled ids和metadata、rollout logprob作behavior proxy免旧checkpoint/extra forward；ratio区间外置零不是普通clip，允许off-policy bias。多版本trajectory按最老w0筛staleness，environment失败移除；组有效超过半才复制不足，否则drop，不能声称原组无偏。optimizer每sync重置、K同步、τ/ratio阈值和机制组件controlled ablation未披露；frontier score属model/data/infra bundle，不归因这些组件。2+2+2=6，标准必要块完成，actual已有覆盖比较；不扩架构/全部appendix。早产品release是不同事件：官方README精确Feb11 ref 88e136faee607677c567831f76e6d58e1301e304（GitHub contents API实际恢复）仍声明“technical report is coming soon”，不是正文公开；不借commit单独判first-public，本论文独立DOI/Submitted日程落窗。

处理本日已校准六项及有限最后四项，不扩104宽线索。精确v1；五项HTML缓存为V3-exact-v1/相应ID，15593官方HTML不可用，有限PDF恢复。日期原字段已实际逐family核：Submitted位于官方本批提交区间，DOI同身份原Created/Registered在本窗内；与公告最早Feb18 01Z共同限定，非Created单字段断日。六项准入root校准通过；六项均已root必要源/owner/实际POST或Existing通过，15580仅中心争议隔离；最后四项独立owner处置待核，不授日级Gate。未运行代码或复现。

## 2602.15580 — PID Flow，中心争议终态隔离

[exact-v1](https://arxiv.org/html/2602.15580v1)。实际§3–5、C.1–5、B.2/E/F/G必要块：mean-pool/PCA95%后flow Gaussianization及Gaussian plug-in估计；正确回答子集至少900/任务/模型、六GQA子任务，不等全任务人口。C.4 Eq16定义R=min(I_Q,I_I)，Eq17 U_L=I_Q−R、U_V=I_I−R，每一row至少一unique必须为0；Table3 ChooseAttr两unique14.18/2.01、ChooseCat15.40/5.31，Table8亦同row两正，与同一声明estimand不符，非1e−6数值误差。C.2 joint(source,target)流还未证明保源分账不变性，两个target变换不同。局部Image→Question knockout保留其他通道，不能把重分配PID/82%/低于2%变因果份额或compute cost；Table8某些总量反而下降。

root已实际独核Eq16–17和Tables3/8，中心PID份额终态隔离通过。不写Books，不绕用局部knockout背书中心数字。精确重开需同estimand公式/实现与表一致的纠正原材料；不继续遍历附件。

## 2602.15593 — 共享权重的条件归纳偏置

[官方精确PDF v1](https://arxiv.org/pdf/2602.15593v1)，实际PDF pp3–8 §3.1–3.3/Figs2–5，Fig4/5及Eq8必要页像亦看过；非28页全文队列。scalar输出RNN/DNN、μP先验尺度、MSE、weight decay及独立Gaussian噪声SGLD的平稳Bayesian posterior；不是通常minibatch SGD有限时间动力学。RNN保跨time covariance，DNN为时间对角masked kernel。弱信号时共享可能不形成不同表示，强信号才出现RNN temporal coherence；解析相变限线性最短链，T更长没有同一闭式。顺序监督插值的优势来自teacher/task与weight-sharing匹配；端点监督时两模型预测模式可相同，仅尺度有别。有限N2048与合成任务验证，不授所有trained网络、真实LLM或硬件优势。

拟采用共享权重不是自动优势，而是与监督时序/优化统计共同决定kernel相关结构。理论求解/大宽度及SGLD采样均有成本，脱离posterior/μP条件回退实际held-out时序质量与非共享对照。3+1+3=7，必要深入；实现未核。

## 2602.15671 — 数据来源污染与恶意update筛查分责

[exact-v1](https://arxiv.org/html/2602.15671v1)，实际§3.1–3.5/§4.1–4.4/§5与防御直接反侧。server和clients遵守协议，污染来自上游数据，影响client比例ρ与每client poison rate不同。BSNR由已知affected/clean均值差定方向，不能在未知群组时自动检测；ρ高时clean参考噪声增加可让测量下降，不等真实攻击信号弱。

有限IID十client，Vicuna/Llama2-7B、TriviaQA/SimpleQuestions、LoRA r4、每轮一local epoch/100通信轮。Krum/FreqFed在ρ<.5时ASR可近0，ρ更高才全部失效；MA代价亦保留，不采摘要“根本无效”全称。未披露真实跨组织部署、NonIID/硬件precision/CI等不补造。安全深入拟采benign protocol不证明data benign；上游provenance隔离与update检测不能相互替代，BSNR只属有group truth的研究诊断，不写攻击配方。2+2+2=6。

## 2602.15761 — 测试通过与refactoring语义分账

[exact-v1](https://arxiv.org/html/2602.15761v1)，实际§2.1–2.2/§3 RQ1–2/Tables2–4/threats。六模型、三Python套件、两zero-shot refactor类型；4368输出先移除830 compilation/timeouts→3538可比较，不把19–35%当所有生成分母。GPT4输入约束经此前人工验证，Atheris提议1000program/2000function输入；有效输入出现输出分歧反驳该程序对等价，但未找到分歧不证明等价，也不判断谁正确。

Table3漏检69+42+91=202 / detected nonEq333+194+406=933≈21.65%，不是全部输出21%。仅有限输入约束/套件/任务，种子值、CI、执行开销/HW未披露不补。2+1+3=6，标准必要块完成；拟现owner具体已有覆盖，No Change，不要求伪造新fuzzer机制。

## 2602.15799 — 初始方向不拥有整个优化轨迹的安全证明

[exact-v1](https://arxiv.org/html/2602.15799v1)，实际§3 Assumption1/§5 AIC/§6.1–6.3/§7 Tables及D.2–4。Assumption1 base policy等于developer reference，utility loss才等KL；AIC还需Fisher低rank谱/小tail、初始近正交、非零曲率耦合、C²局部。仅采local gradient-flow Taylor −tg+t²Hg/2的条件分支，不用quartic headline签有限SGD/整轨迹或普遍collapse保证。曲率项未在LLM测到，作者称计算代价高。

4096随机子空间Fisher来自100safe completions；OS使用训练后ΔW而非纯预发布预测器，fullFT相关例外及LoRA无同趋势必须保留。Qwen3-1.7B/Llama3.2-3B、full1epoch与LoRA3epoch，单A10080；HS为Gemini2.5Flash判断AdvBench520，非humantruth。Llama LoRA SamSum/GSM8K HS1.10<base1.11，反驳“所有fine-tune上升”；AlpacaTop100还是攻击性挑选子集。3+1+3=7，安全深入只采初步方向/后续轨迹分责，不替代更新后独立behavior gate。

## 2602.15823 — Bregman保留约束与近似低曲率编辑

[exact-v1](https://arxiv.org/html/2602.15823v1)，实际§3.1–3.3/§4.1–4.2/Table1/Fig4与AppendixE/§6。普通caploss二阶近似依赖converged checkpoint；output Bregman使reference处一阶为0，局部二阶为Gauss–Newton，但不是全更新全能力保证。K-FAC用block Kronecker近似，eigenproduct阈值矩阵free投影；与input-nullspace关系限同edited subset，不跨不同layer方法授全局包含。

Llama3-8B三套3000 edits，五capbenchmark每套200，Wikipedia10k curvature cache，编辑五down层；WILD自由生成与teacher-force分责。Table1 ZsRE ARC58→55、IFEval69.3→67.9，平均近1%不是每项都低于1%；Wiki noQA局部对照UltraEdit可更高，Seq耗时和cap退步另记。Fig4 wallclock执行定义未明示所有offline KFAC/SVD构建均入同口径，不能把4m6对7h19当端到端普遍加速。cache、分解、编辑/再校验都付费；precision/HW/多seed未披露不补。2+2+2=6，因具体长期gap加深方法，仅采近似artifact与独立capability回归分责。
