# Jan02 flow / radial generation / group preference / binary envelope / KV packing

最新Dream24766/RadAR24639必要原源/owner及实际正文/前后/末注POST root通过；本批四项actual整合与Phy中心终态，旧待核过程不覆盖此记录。

最新MDBF/PackKV必要原源/owner与actual正文邻接POST root通过，actual Ch49 936/938/末注2605、Ch45 658/660/末注2056已同步；原5/6分具体gap深入未改分。Phy中心终态不变。仅Dream24766/RadAR24639尚待非作者必要源/Books处置，不授全批或日级Gate，旧待核字样由此覆盖。

最新非作者复核：root实际核下方PhyGDPO Eq2–14/default参数，6分中心推导争议安全终态暂缓通过；α正值更正与γ<1/α反例有效，Eq9两行不等。只隔离该group概率/upper-bound训练链，不宣称整个实测无效，也不采LoRA事实替代中心增量。Dream/RadAR/MDBF/PackKV必要证据与具体owner仍待root。

## 原页必要公式缓存（非评价账本）

Source：https://arxiv.org/html/2512.24551v1；web exact-v1实际返回，行号为该工具HTML展开定位，不是PDF页。只存争议所需公式；其他正文仍按各节定位读。

```text
L151: Groupwise Probability. We denote the reward as $r(c,x_{0})$ with the generation $x_{0}$ and condition $c$. Different from the normal DPO, we start from the groupwise Plackett-Luce (PL) probabilistic model, as shown in Fig. cite56†3 (c). We adopt the real video as the winning case $x_{0}^{w}$ because it always follows physical laws and a set of generated videos as the losing cases $\mathcal{G}^{l}(c)=\{x_{0}^{l_{1}},\ldots,x_{0}^{l_{m}}\}$. The preference probability of the PL model is formulated as
L152:  | $$\small p_{\mathrm{PL}}\!\big(x^{w}_{0}\mid\mathcal{G}^{l}(c),c\big)=\frac{\exp\!\big(r(c,x^{w}_{0})\big)}{\sum_{j=1}^{m}\exp\!\big(r(c,x^{l_{j}}_{0})\big)}.$$  |  | (2)
L155:  | $$\normalsize\mathcal{L}_{\mathrm{PL}}(\phi)=-\,\mathbb{E}_{c,\,\mathcal{G}^{l}(c)}\!\Bigg[\log\frac{\exp\!\big(r_{\phi}(c,x^{w}_{0})\big)}{\sum_{j=1}^{m}\exp\!\big(r_{\phi}(c,x^{l_{j}}_{0})\big)}\Bigg].$$  |  | (3)
L159:  | $$\normalsize r(c,x_{0})=\beta\log\frac{p_{\theta}^{*}(x_{0}|c)}{p_{\psi}(x_{0}|c)}+\beta\log Z(c),$$  |  | (4)
L160: where $p_{\theta}$ and $p_{\psi}$ denote the conditional probabilities of trained model $\theta$ and reference model $\psi$. $p_{\theta}^{*}$ and $Z(c)$ are the unique global optimal solution and the partition function. We plug Eq. (cite57†4 ) into Eq. (cite58†2 ) and drop the group-constant term $\beta\log Z(c)$ as it does not affect the optimization direction to obtain the groupwise DPO (GDPO) loss as
L161:  | $\displaystyle\mathcal{L}_{\text{GDPO}}(\theta)$  | $\displaystyle=-\,\mathbb{E}_{c,\,\mathcal{G}^{l}(c)}\Big[\log\frac{\exp\!\big(\beta f_{\theta}(x^{w}_{0},c)\big)}{\sum_{j=1}^{m}\exp\!\big(\beta f_{\theta}(x^{l_{j}}_{0},c)\big)}\Big]$  |  | (5)
L162:  |  | $\displaystyle=\mathbb{E}_{c,\,\mathcal{G}^{l}(c)}\Big[\log\frac{\sum_{j=1}^{m}\exp\!\big(\beta f_{\theta}(x^{l_{j}}_{0},c)\big)}{\exp\!\big(\beta f_{\theta}(x^{w}_{0},c)\big)}\Big]$  |
L163:  |  | $\displaystyle=\mathbb{E}_{c,\,\mathcal{G}^{l}(c)}\Big[\log\!\Big(\sum_{j=1}^{m}\exp\!\big(\beta(f_{\theta}(x^{l_{j}}_{0},c)-f_{\theta}(x^{w}_{0},c))\big)\Big)\Big].$  |
L168:  | $$\normalsize\log\frac{p_{\theta}(x_{0}|c)}{p_{\psi}(x_{0}|c)}=\sum_{k=1}^{T}\log\frac{p_{\theta}(x_{t_{k-1}}\mid x_{t_{k}},c)}{p_{\psi}(x_{t_{k-1}}\mid x_{t_{k}},c)}\;\triangleq\;\sum_{k=1}^{T}\Delta_{k}.$$  |  | (6)
L170:  | $\displaystyle\mathcal{L}_{\text{GDPO}}(\theta)$  | $\displaystyle=\mathbb{E}_{c,\,\mathcal{G}^{l}(c)}\Big[\log\!\Big(\sum_{j=1}^{m}\exp\!\big(\beta T\mathbb{E}_{k}[\Delta_{k}^{l_{j}}-\Delta_{k}^{w}]\big)\Big)\Big]$  |  | (7)
L171:  |  | $\displaystyle\leq\mathbb{E}_{c,\mathcal{G}^{l}(c),k}\Big[\log\!\Big(\sum_{j=1}^{m}\exp\!\big(\beta T[\Delta_{k}^{l_{j}}-\Delta_{k}^{w}]\big)\Big)\Big].$  |
L174:  | $$\normalsize\sum_{j=1}^{m}e^{x_{j}}\leq\prod_{j=1}^{m}\big(1+e^{\alpha_{j}x_{j}}\big)^{\gamma_{j}},~~~0<\alpha_{j}\leq 1,\ \gamma_{j}\geq 1/\alpha_{j}.$$  |  | (8)
L176:  | $\displaystyle\mathcal{L}_{\text{GDPO}}(\theta)$  | $\displaystyle\leq\mathbb{E}_{c,\mathcal{G}^{l}(c),k}\Big[\sum_{j=1}^{m}\gamma_{j}\log\Big(1+\exp\big({-\alpha_{j}\beta T[\Delta_{k}^{w}-\Delta_{k}^{l_{j}}]})\big)\Big]$  |  | (9)
L177:  |  | $\displaystyle=\mathbb{E}_{c,\mathcal{G}^{l}(c),k,j}\Big[-\gamma_{j}\log\sigma\big(-\alpha_{j}\beta T(\Delta_{k}^{w}-\Delta_{k}^{l_{j}})\big)\Big].$  |
L183:  | $\displaystyle v_{j}$  | $\displaystyle=1-\frac{s^{sa}_{j}+s^{pc}_{j}}{2},~~\gamma_{j}=\frac{1+\lambda\cdot\sigma\!\big(\kappa_{\gamma}(v_{j}-b_{\gamma})\big)}{\alpha_{\text{min}}},$  |  | (10)
L184:  | $\displaystyle\alpha_{j}$  | $\displaystyle=\alpha_{\text{min}}+(1-\alpha_{\text{min}})\cdot\tanh\big(\kappa_{\alpha}(v_{j}-b_{\alpha})\big),$  |
L195:  | $\displaystyle\log\frac{p_{\theta}(x_{t-h}\mid x_{t},c)}{p_{\psi}(x_{t-h}\mid x_{t},c)}$  | $\displaystyle\approx-\frac{h}{2\varepsilon}\Big(\ell_{\theta}(x_{t},t)-\ell_{\psi}(x_{t},t)\Big),$  |  | (13)
L200:  | $$\normalsize\mathcal{L}=\mathbb{E}_{c,\mathcal{G}^{l}(c),k,j}\Big[-\gamma_{j}\log\sigma\!\big(-\alpha_{j}\beta T[(\ell_{\theta}^{w}-\ell_{\psi}^{w})-(\ell_{\theta}^{l_{j}}-\ell_{\psi}^{l_{j}})]\big)\Big],\vskip 2.84526pt$$  |  | (14)
L212: To address this issue, we design a LoRA-Switch Reference (LoRA-SR) scheme. As shown in Fig. cite56†3 (b), we freeze the backbone as the reference model $\psi$ and attach trainable LoRA modules to $\psi$ as the trained model $\theta$. Our LoRA-SR enables the reference and trainable models to share the same heavy backbone while flexibly switching the lightweight LoRA parameters for the training and reference modes.
L217: Implementation Details. We implement our PhyGDPO by pytorch cite75†Paszke et al. (2019) based on a foundation T2V model Wan2.1-14B. Our model is finetuned for 10K steps in total at a batch size of 8 on 8 H100 GPUs for 6 days. To save GPU memory, we adopt mixed-precision training cite76†Narang et al. (2018) with BF16 and sublinear memory training cite77†Chen et al. (2016) . We adopt the AdamW optimizer cite78†Loshchilov and Hutter (2019) ($\beta_{1}=0.9$, $\beta_{2}=0.999$) with a weight decay of 0.01.
L218: The learning rate is initially set as 1e^{-5} and decays to 1e^{-6} using cosine annealing cite79†Loshchilov and Hutter (2017) algorithm. The training and inference spatial resolution of the video is 480$\times$832. We set $\tau=3$, $N=100$, $\alpha_{\text{min}}=0.5$, $k_{\gamma}=2.0$, $b_{\gamma}=0.4$, $\lambda=0.6$, $k_{\alpha}=5.0$, $b_{\alpha}=0.5$. The rank of LoRA is set to 48. We follow the same metrics of VideoPhy2 and PhyGenBench to evaluate the T2V generation models.
```

本批仅为已读141题摘范围的24766/24639/24551/24545/24449，root逐完整AB准入评分7/7/6/5/6。前两深入，其余标准；PhyGDPO核心公式出现具体反证，额外深入受影响推导，不借成熟原则抬分。作者必要原文阅读如下，非作者Evidence、具体owner及终态尚待。未运行代码或复现。

原DataCite created依次Jan1T03:19:39Z/03:16:40Z/03:14:35Z/03:14:27Z/03:12:12Z，registered原值保DATACITE_POTENTIAL。官方holiday+availability noadvanceID限定公开区间Jan1T01Z至各created下一秒，完全落窗；非注册精确公开。已见作者project链接仅日期线索，不倒推无更早发布。

当前官方abs五页已实际轻量核：24766/24639/24545保持v1，24551现v4 ECCV2026、24449现v2；页面无具体withdraw/erratum说明。版本号本身不扩审，采用仍精确v1；Phy中心冲突不因后版存在自行推定已经修复。

## [Dream2Flow — 2512.24766v1](https://arxiv.org/html/2512.24766v1)

2+2+3=7。actual III-A–C/IV-B–F/A/B/C/F/H/J：生成对象运动≠执行动作，RGB-D第一帧scale-shift锚定/已知camera extrinsics后track到robot frame，以object flow为目标，另有动力学、grasp、reachability/controller。真机rigid-grasp与仿真particle/SAC边界不同，门任务reward用simulator joint-angle更新并非全程视觉追踪；particle训练500transitions，不能宣传全链无任务训练。baseline做过适配，不是原实现直接对比。100Push-T、每真任务10和附加5trial仅有限证据。morph/hallucination、visibility、grasp分别失败；single-camera/rigidgrasp与3–11分钟flow前处理排除实时与安全保证，HW/precision未披露。拟Ch26 video→controller具体中间目标/actuator与frame条件，不把对象运动真实性授控制可行性，待owner对读。

## [From Sequential to Spatial: Reordering Autoregression for Efficient Visual Generation — 2512.24639v1](https://arxiv.org/html/2512.24639v1)

2+2+3=7。actual §3/Eq1/Alg1/NAM/TPT/§4.1–4.4/Tables1–4：inside-out crop/ring并行，旧区修正与新边生成分角色，可见性mask防新边影响旧区；并非token顺序微调。重叠crop的Eq1不直接证明任意联合token exact likelihood，cache reuse与mutable旧区实现一致性未核，不授精确采样/免费revision。teacherforcing与生成混合/TPT和RDS/RNI同时改变训练，sequential消融不是全factorial；50KImageNet输出和300epochs有限质量证据。吞吐表没给HW/precision/batch，不外推5.6×、SLO或VLM兼容；多尺度zero-shot为可视案例。拟Ch24 AR空间扩展/可修正state与cache边界，待具体owner对读。

## [PhyGDPO — 2512.24551v1](https://arxiv.org/html/2512.24551v1)

2+2+2=6。actual §2.2 Eq2–14/LoRA-SR/§3/Tables1–2：共享冻结base与开关adapter减少第二份base，并用组候选与VLM score调权。8H100/BF16/10Ksteps/batch8/6days/Wan14B、LoRA48；额外生成/筛选费用未完整，104人偏好不证明physics真值。real-video winner标注假设不授永远物理正确；sequential ablation不纯group归因。

决定性理论反证：Eq2/3分母不含winner，可给>1的所谓PL概率；Eq9两行log-exp与negative-sigmoid符号不一致，Eq13负denoise比代入与Eq14另有符号承接。Eq10参数αmin=.5/bα=.5/kα=5在v∈[0,1]实际仍α>0；按已披露公式直接算v=0得α≈.00669285、γ≈2.37203、1/α≈149.41316，不满足Eq8要求γ≥1/α。v=0是两个VLM得分均1的可允许端点，并非声称真实样本曾达到；数学保证需覆盖自身定义域。故撤回此前‘可能α≤0’猜测，保正确反证。不能自己加winner或修sign后称作者等价链通过。先拟中心推导暂缓，LoRA事实不替代本次group概率重要增量；重开需exact实现/作者澄清并核合法group目标、权重条件和训练loss一致性。root待实际核。

必要局部条件核到即停；原文提supplement但此HTML目录只有§1–4和references，没有对应证明页，当前公式本身足以定位矛盾，不能因此声称supplement已审。

## [More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization — 2512.24545v1](https://arxiv.org/html/2512.24545v1)

2+1+2=5。actual §3.2/§4.1–4.4/Theorem4.2/§5.1–5.2/Tables1–2/§8：固定sign demodulation使factor magnitude envelope的rank自由度独立于inner rank；fixedmask TSVD最优仅factor Frobenius，adaptive-sign ADMM明言无同一投影/全局收敛。共享binary primitive不等同两次matmul常数成本，Eq12有l²项，未见真实延迟证据。B200、WikiText512calibration/QEP/头尾各4层fullprecision，targetBPW不是整模型residentbit；P变化optimizer次数不同；更大l并非所有model/BPW更优，7B误差改善不必任务改善。作者Ch49 932–943实际对读：已有共享lookup/basis与ternary bitmask成本，但尚未承载binary factor inner rank增加不解除demodulated envelope秩一限制。拟在ternary分支前窄两段，5分因具体表示知识缺口深入固定mask/执行关系，不授性能。root owner/必要源待核。

## [PackKV — 2512.24449v1](https://arxiv.org/html/2512.24449v1)

2+2+2=6。actual III-B–D/IV-A–F：buffer fullblock压缩、quant唯一lossy、pairedKV重排/bitpack与K/V不同dot维度融合解码；joint permutation需mask/position语义已消费且K/V对应，不能任意重排causal原始token。K warp局部dot、V partial FP32 atomic与half2非无数值差异。A10040GB/RTXPro6000所报98GB、sixmodel/sixbench，5%允许退化阈值由同bench sweep/interpolation选择非独立认证。IV-E replay collectedKV+cuBLAS MatVec仅kernel，compression/pre-fill/softmax/servingSLO未纳完整；IV-F单机独立实例不证明TP或跨节点perfectscale。median K压缩有负收益。作者actual Ch45 635–672已有packed frontier/metadata/fused不规则布局与阶段更新，缺lossy quant之后lossless codec和K/V contraction方向为何使layout不能共用。拟在MosaicKV后、mixed sparse前窄两段；6分具体gap深入这些直接机制，root owner/必要源待核。
