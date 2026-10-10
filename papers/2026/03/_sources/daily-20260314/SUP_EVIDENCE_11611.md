# 11611 Partial RoPE：必要Source、actual Ch13差额与两段PRE提案

mar14_supplement；只03-14补充Mar13 BJT。完整v1题摘、身份/可见说明与贡献准入已由非准备者实际校准，四作者Mohammad Aflah Khan/Krishna P. Gummadi/Manish Gupta/Abhilasha Ravichander，标题Fractional Rotation, Full Potential? Investigating Performance and Convergence of Partial RoPE；v1 abs未见撤回/纠错说明，不遍历完整版本。十项日期包SUP_DATE_NARROW.md的本ID日级夹证仍待root实核，此处不先计正式候选。

## 实际原证与停止

SUP_NARROW_MINIMUM_MANIFEST_RESULT.json官方exact https://arxiv.org/html/2603.11611v1 GET200/240182bytes，2026-10-10T01:44:11.287374Z。本人直读原HTML经inspect_source解析B25–51（§3、全部六RQ、§5 seed/LR/QK-Norm反侧及§6/Limitations）、B101–131（A旋转维数/Table1、B真实训练协议、C cache公式）、B155–225完整Table3与B226–284完整Table4。首输出截断§4/5另恢复；未读所有图pixels、代码、复现、全引用/框架PR和无关D模型目录。本命题由这些原文/关键表足够支持，不继续全附件。

新证据对象不是RoPE本身或QK-Norm成熟原则，而是从头训练中改变旋转维度比例后，少量旋转与NoPE/极少pair呈不同loss/稳定性分支。分别Llama-style顺序1B/8B与Pythia-style平行1B、FineWeb/FineWeb-Edu各100B token subset、Pythia tokenizer；默认2048，1B另1024/4096/8192，8B只2048，不授超8192或原发行checkpoint行为。0/名义10/25/50/75/100%与极少两channel，Table1精确合法偶数是Llama1B 6/64、8B12/128、Pythia26/256，名义10%不是所有架构恰10%。两channel不是全架构相同比例。

§4正文的near loss/comparable是作者曲线判断，不是经过全配置equivalence test；8192时10%与≥25%稍分离、8B更离散。Table3 WSC及其他具体slice没有统一最优；Table4 FineWeb-Edu Standard-PPL名义10%64.50对100%57.82，8B Standard10.08对9.03，不能从整体near-loss抹除质量差异。MCQ多采用byte-length normalized而WinoGrande/PubMedQA/WSC未normalize，括号误差不能自行称独立训练seed CI或证明不劣。§5并行NoPE loss spike的seed/LR补检及8192顺序反侧有用：QK-Norm消spike仍higher-loss，不推真实机制唯一为gradient，也不把stable当全loss/benchmark等价。小LR也higher-loss、大LRearly divergence不是任意调参均可救。

训练B披露4node×8H200、默认DP全局4096seq；1B BF16 forward/backward而FP32累加/reduction，8B BF16累加+FP32reduction、36层而非发行32层；1B平行12–14h/顺序24–27h，8B约120h。不同序列调整microbatch保持steps，不能混每run时长作partial-vs-full净节省。forward/inference batch/concurrency、完整SLO等未披露，不授服务收益。QK-Norm用每head hidden轴而非原框架跨heads规范，此为原文实现条件而非我们核PR/代码。Artifact仅upon acceptance承诺，不认证已释全部checkpoint。

C计算仅precomputed sin/cos raw cache，FP32、headDim256、Lmax×Dhead×bytes（partial换Drot），排除fragmentation；不是KV/模型状态缓存、不是每layer×每head所有激活总量，也未测即时生成kernel或服务显存。作者leave partial/NoPE hybrid与length extrapolation未测，from-scratch训练不允许直接删既有checkpoint的rotary坐标后称等价。

## 评分与具体owner差额（待独核）

提案Design2+Reach1+Durability2=5：新增是partial-rotation比例与NoPE稳定/quality非等价的受限实证，改变全head旋转/完全去位置之间的机制选择；影响首先是位置组件而非独立多系统加速，维度与cache/quality分账有稳定价值。不以10x或训练投入、能映射书章倒推高分。标准必要Source已读够；实际长期接口缺口触发窄深入/PRE，但还未获独核/写许可。

actual owner MODEL-POSITION-ENCODING Ch13已顺读125–218完整ALiBi→RoPE数学/activation低秩/二维小例子→连续位置/设计表→causal mask，以及247–284坐标辨识/频率替换/周期裁剪完整邻接。现159式恒等式与161相对关系后直接163 content-invariant条件分支，没有明确旋转子空间与剩余无旋转content项、合法pair比例/训练稳定性与sin-cos/KV cache分离。后文频段干预与pruning均非partial pretraining；因果mask可给顺序不等NoPE稳定性的区分也未承载。本新证据不能由现有“任意长不保证质量”一句主题覆盖。Ch12 embedding与Ch14 1–75 QKV/position插入点交接已实际读，其他章节不新建owner。

拟在Ch13“点积中的位置影响只与相对偏移…结构。”之后、原“这也给出…content-invariant”之前窄加下面两段；不修改原式/旧分支/其他owner，root独核后root写/作者nonwriter实际POST。

### 逐字两段提案

上面的旋转恒等式并不要求每个 head 的全部坐标都带位置相位。若把 Query/Key 分成旋转子空间 `q_rot/k_rot` 与其余 `q_plain/k_plain`，只对前者使用 RoPE，匹配就分成 `q_rot^T R_(n-m) k_rot + q_plain^T k_plain`；后一项仍可做内容匹配，而不是被删除的容量。选择旋转比例因而是在同一个 head 内分配位置调制与无旋转匹配的坐标，需要按二维 pair 选择合法偶数维度，并绑定训练时使用的频率/维度配置。[partial RoPE 的受限从头预训练对照](https://arxiv.org/html/2603.11611v1)在所测 1B/8B、顺序/平行 block 与有限训练长度中发现，名义约一成的旋转维度常接近全旋转的最终 loss；这不是证明固定一成普遍最优，更不是允许对既有 checkpoint 直接删去旋转而保持行为。<!-- source-family:SF-2026-ARXIV-2603-11611 -->

完全 NoPE、只旋转极少 pair 与适度 partial RoPE 也不是同一个稳定性承诺：受测 NoPE 在平行 block 及长窗顺序训练中可出现 loss spike，QK-Norm 能缓解，但稳定后仍可处于更高 loss 分支；部分任务和较长长度也保留 partial 与 full 的差异。因此选择应同时验收训练轨迹、目标质量与实际旋转维数，而不是只看是否收敛或平均任务分数。这里线性减少的只是按最大长度预计算的 sine/cosine 表存储，不是 Key/Value cache、整机显存或端到端服务时延；长窗外推仍未验证，既有 full RoPE、已校准的 partial 配置和其他位置方案应按原训练/负载条件共存，质量或稳定性失配时不以表缓存节省覆盖回退条件。

未授Source/PRE/Books/DAY通过，待root非准备者必要原证、实际owner差额和逐字两段核验。日期仅需SUP_DATE_NARROW本ID官方字段，不追时分秒/全版本。
