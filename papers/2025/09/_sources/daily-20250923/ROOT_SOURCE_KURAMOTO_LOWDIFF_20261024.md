# Kuramoto 与 LowDiff：两项有限必要 Source 首准备

## 互斥与采用范围

作者A20提出尚未开始的两项必要Source，root明确接受，A23已确认让域。仅此两项首准备归root；日门、评分、owner及Books仍作者，不GET、不覆盖原件、不第三已成题摘/日门。沿原5分，以各自可支持的生成路径/采样消费者为命题；不因理论或加速标签扩成全篇/全表图配额。

实际本地解析原HTML及MathML alttext，不依赖截断摘要：

| 精确v1原件 | 实际字节/SHA256 | 原请求事实 |
| --- | --- | --- |
| `REPAIR_20261024_CORE_KURAMOTO.raw` | 345183 / `5a744515a7af952a67fee31c65b01cf796781a313e4194eb84fdd8a2d44755ef` | `https://arxiv.org/html/2509.15328v1`，2026-10-23T21:12:45.089138–45.902269Z，200/exit0 |
| `REPAIR_20261024_CORE_LOWDIFF.raw` | 220562 / `9b2fbda85690f13316616ac10b2d200220a6b5b5638ee590642cd0bae81f8b00` | `https://arxiv.org/html/2509.15342v1`，2026-10-23T21:12:46.038402–46.982527Z，200/exit0 |

两份同名request的URL/bytes/SHA均已实际逐项复算匹配。这是原始取得时间，不是论文公开时间。未核图像像素、代码/运行或复现；不扩其他科学应用、后续版本和引用论文。

## 15328 Kuramoto：周期状态的结构化前向破坏，不是普遍优于 Gaussian

**拟采用命题**限于：前向过程不必只用线性Gaussian drift；在周期相位状态上，可以用相位间耦合与reference attraction构造结构化破坏，再学习匹配的逆过程。改变prior/状态几何必须同时承担score监督、terminal近似和额外训练费用；偏好适配数据结构，不能从自然/生物类比推正确或更强。

实际完整读§2.1–2.3/式1–12/Algorithm1、§3.1–3.3/Tables1–4及必要caption、§5限制、A.4自然图像反侧、B.1实现/schedule Table5、B.2耦合消融/Table6及CMMD Table7；另单独完整提取Algorithm2。没有读A.1–A.3全部证明或B.3/B.4科学负载，不把这些未读内容列本命题的外部hold。

### 机制与数学权限

- 原图像值从[-1,1]映到[-0.9π,0.9π]，状态每步wrap到[-π,π]；并非先从RGB测出真实方向/物理orientation。Sin/cos输入及双通道读出让网络适配周期表示，不认证物理语义。
- 式3将global相位耦合、固定reference attraction与噪声分开；local版本只读5×5邻域。前向同步破坏细节，逆过程以learned score反同步/加细节，不是简单把forward轨迹精确倒放。
- 非线性drift不再给任意t的现成Gaussian闭式边际。式9的conditional-score期望身份和式10的local DSM允许以已模拟到的前一状态、再采相邻wrapped transition构造监督；wrapped Gaussian无限和截到K=3、每状态M=5是有限近似和额外求值，不等原score已精确可得。训练还需模拟到t−1。
- von Mises terminal来自mean-field/慢变quasi-equilibrium及均相位对齐的近似叙述；local耦合破坏mean-field，原文亦只称terminal可近似。它不是任意有限网络/离散步/有限图像的精确joint terminal或逆采样保证。
- **原recipe有具体不一致，不照录完整可执行系数。** 正文写K_ref>D>K；B.1却写global K_ref>2D>K，而Table5的100步global终值K_ref=.045、2D=.1，既不满足后者，也不满足前者的K_ref>D=.05。local Table5令K_ref=K，不满足正文严格链。Algorithm1 loss行写∇p而式10写∇log p，不能悄悄替作者修成一致实现。Algorithm2从p(θ_T)起步的抽样资格也仍受上述近似限制。

### 直接支持、反侧与费用

§3及B.1：CIFAR10为3×32×32，SOCOFing为1×96×96，Brodatz由少量大图切1×32×32 patches，terrain128×128；SGM VP基线与本法使用同U-Net/三个self-attention层，AdamW1e−4/EMA.995，单A100训练/推理，100/300/1000步。原文称训到FID收敛，不等所有配置相同训练预算；precision、完整训练步数/时间、FID样本数/CI、批量和服务并发/SLO必要主域未披，不造数。

Tables1–3在这些orientation-rich图像上报告较低FID；B.2的reference-only控制在Brodatz100步33.76，对global20.26/local18.47，可支持耦合的有限增量而非生物因果或全部结构必要性。CMMD是另一个特征分布proxy，不是物理/语义真值。**关键反侧不可抹掉**：CIFAR1000步SGM3.17对global11.58/local10.79，300步global25.83也略差于25.76；A.4承认同步偏好可能伤自然图像的全局语义/非重复结构。不能由100步纹理较好签所有图像、更多步必益或无损。

§5明确每训练step需要O(T)前向链模拟；预计算所有训练对或逐epoch缓存只是把模拟移到先前，并新增磁盘/读写/刷新，不能按“per-step O(0)”删掉总费用。耦合计算、MC/truncated-transition监督、score训练、全部采样与独立质量回归均计费；没有端到端墙钟或服务SLO证明，少步对照不自动等净加速。

**首准备结论：有限标准必要证据已足。** 采用结构化周期路径及匹配训练/状态边界，并保approximate terminal、schedule/印式冲突、自然图像退步和完整费用；不采用完整执行recipe、一般精确posterior/物理正确/全场景优势。原5分保持，未作owner或Book决定，交作者一次actual采用裁定。

## 15342 LowDiff：统一网络里的多分辨率条件采样，少高分辨率求值不等少总求值

**拟采用命题**限于：先在较低分辨率求出带噪条件，再用同一网络复用的低分辨率子块参与高分辨率去噪；训练条件分布和resolution身份共同匹配。这里改变的是训练/采样分支和每次求值成本，不是任意checkpoint都能直接降分辨率执行。

实际完整读§3.1–3.4/Algorithm1–2、§4.1–4.3/Tables1–9、§5限制、AppendixA训练预算、B effective-NFE定义及C采样/截断反侧和Tables10–12。未读全部Related Work、D全部样本像素或源码，不复现。

### 机制与实际消费者

- 低分辨率最低stage无条件生成；训练高stage时，先将clean图下采样并加独立噪声，再升回当前分辨率，和当前noisy高分辨率输入拼接。推理低stage在非零噪声处截断，把该自产条件交下一stage；最后stage才到clean。Truncation augmentation沿用CDM，不算本稿发明；自产条件不变成真实观察。
- 单U-Net的低分辨率内部blocks既独立服务低stage，也在高stage处理下采样features；各resolution独立I/O conv与learnable resolution embedding区分用途。训练逐resolution形成loss、共享block承受多个消费者更新。不同stage的condition、noise/truncation、active blocks和embedding身份必须相配，不能只在runtime缩图。
- 网络共享与多stage级联是两个选择：它减少独立模型/参数副本，但增添多分辨率前向、阶段条件驻留与切换。Transformer分支也有latent低高stage，不等所有backbone/模态已验证。

### 条件化结果与关键反侧

Pixel采用EDM VP/SongUNet/EDMPrecond及Heun二阶solver，latent采用LightningDiT-B/1及Euler。训练8×A40；CIFAR stages8/16/32，FFHQ8/16/32/64，ImageNet256图像对应latent8/16。§4.1一处写ImageNet256×64而同段又写256×256，不拼成新图像尺寸。采样CIFAR/FFHQ为4090 24GB、ImageNet为A10040GB，每trial batch64、10次均值；precision/生产并发/SLO未披。

Table2 CIFAR总实际NFE为18+13+17=48，不是22；22是AppendixB按低/高每步latency比例折到目标分辨率、再ceiling的effective NFE，硬件/布局改变即应重测，不是普遍网络调用数。FFHQ实际22+23+23+39=107对基线79，同样不能只报高stage39来声称总调用减半。

所报采样batch时间确有下降，但质量不是全胜：CIFAR无条件FID2.11差于EDM2.04，条件1.94差于1.84，IS却略高；FFHQ FID2.43对2.47与ImageNet4.00对4.38只是所测分支。Table6多stage相对two-stage的CIFAR无条件FID2.11对2.10也略退；不能由more-stage标签保证更好。Table8/9同分辨率NFE下shared-vs-separate CDM支持有限共享取舍，不认证全部训练/硬件等成本。

**训练预算未完全同一化**：主文称保留超参，AppendixA明确改变每resolution更新和训练时长，每epoch需多次forward；EDM200M→150M是75%，LightningDiT64→42epoch则为65.625%，不能把二者都写75%或已实测等完整训练费。所有stage训练、分辨率I/O/embedding、条件构造/上采样、全部高低stage采样与codec都付费。

**数字/recipe限定**：Table5 CIFAR latency2.22→1.37的吞吐比例约+62.04%，表throughputs28.8→46.7约+62.15%，不能由这些舍入值复算出印刷+60.5%；采用所报原时间和条件，不修作者百分比。AppendixC Table10中2.65对应两stage都用wide(.002,80)，正文却称both-narrow最差；Table11/12的截断指代也混用，不据此教授统一最优采样阈值。Table11截断过大/小均可退，Table12更多低stage步数有额外延迟而无FID收益。

§5明确尚未应用text-to-image，需要重新设计低分辨率语言条件；512²等更大latent路线为未来，不从现有CIFAR/FFHQ/256²推广任意T2I或服务。条件不足、细节/质量退步或净预算失配时，保原高分辨率采样、独立stage/较少stage及已验原模型。

**首准备结论：有限标准必要证据已足。** 可采用resolution-specific条件/共享块与matched训练、实际NFE和effective-NFE分账这个有限机制；不采用无损、固定宣传倍数、全部预算公平或任意模型即插即用。原5分保持，未作owner/Books决定；作者作为不同角色一次actual采用后复用，不要求Sartre第三原Source。
