# CutBCE / 2610.05559v1 作者必要 Source 与窄拟稿

作者oct07_missing；root已条件准入通用loss执行机制，非推荐应用效果。下述为作者审阅，不是独立Source/PRE/POST。

原证 https://arxiv.org/html/2610.05559v1 ，保存core-05559v1.raw.html。实际读完整题摘、§III–IV（导航25–63）与结论；支持与关键反侧足够，不遍历推荐数据应用附件。BCE恒等式本身非新发明。

机制：独立Bernoulli BCE写为dense background softplus(x)与稀疏正标签修正-yx，每个vocab tile累加后丢弃logits。customVJP只保A/E/sparse IDs，backward重算tile；Pallas在VMEM跨inner N tiles累加dE后DMA，outer N按真实VMEM容量分块。shard_map将weight replication约束提到chunk循环外，绑定vocab_offset/psum轴。不物化onehot或整BNV HBM logits，不等没有输出权重、梯度、通信或重算。

数值/控制：T2单TPUv5e/v6e，D128/L8，synthetic A/E/target，500 JIT后稳态；32×32/V100k相对loss1.1e-7、梯度relL2 7.1e-5，仅受测数值近似，不自签所有dtype/shape精确。v6e32×32/V100k Keras1.43ms→0.93ms，V200k2.86→1.49；128×128/V100k基线OOM不能算有限倍数。论文声称unaligned/pad/duplicateIDs单测，但我未打开代码，不称核验。

关键反侧：count metrics仅训练阶段，ranking评价仍物化全logits且独立物理TPU，不能把局部HBM省量改成全pipeline RAM/硬件预算。T3 8chip v6e2×4，global64/N256 perchip22.37→7.67GiB、6.14→20.01step/s，但Hit@8 .186→.183，不是已证等质量；扩大batch/length同时改工作点且其他基线OOM，不给有限加速比。推荐效果不纳本项目；仅将质量非等价作为通用执行结论的限制。数值precision在所读必要配置Not Disclosed，非动态serving，无token-length/concurrency/SLO主张。

日期原件datacite-05559.raw.json：精确DOI、arxiv.content/findable，uniquev1 submitted2026-10-04T21:47:02Z，registered2026-10-06T05:01:49.000Z。按已核官方历史公告/发号规则最早Oct6 00:00Z，整个possible区间BJT Oct6 08:00–13:01:49；非登记=真实公开时刻。待独立核官方版本页当前修订信号。

拟评分2+2+2=6；generic objective执行/反向状态/collective边界，可复用但非新目标函数。拟唯一owner TRAIN-PRETRAINING/Ch28，一次trainingstep状态流；实际读其251–290完整局部、Ch27/29交接与Ch36已有TurboGR局部，不借推荐场景扩大范围。现有逻辑logits[B,T,V]→CE→backward尚未区分逻辑输出与必须HBM物化，也没有BCE独立标签的稠密/稀疏执行分工。Ch36的jagged/dense布局不是此差额。

## 精确 literal PRE（待独立Source/owner/PRE）

锚点：Ch28 `一次 training step 的状态流` 代码块结束后、`参数更新抽象为：`前，只加以下唯一自然段。

这里的 logits 是逻辑中间量，不要求所有目标函数都把完整 `[B,T,V]` 写入 HBM。若目标是各类独立的多标签 Bernoulli BCE，而非归一化 next-token softmax，一条分支把每类 loss 分为稠密 `softplus(x)` 与稀疏正标签修正 `−y·x`，按词表 tile 累加后丢弃 logits；custom VJP 只保输入表示、输出权重和稀疏标签，反向重算 tile，在片上累加梯度，再按已声明的分片轴归约。这改变的是loss执行与保存/重算边界，不是更换BCE数学定义，也不能直接拿来替换CE目标。Tile、片上容量、padding/重复标签、数值格式和collective必须联合核验；训练count指标可以同路累加，ranking评价仍可能重建全logits。受限TPU算子对照支持这条物化替代，端到端样例存在质量差额、评价另占设备，不能由局部HBM/step改善签发等质量或全pipeline降本。重算、输出权重/梯度、通信及完整训练回归都付费；目标耦合、数值或资源回归不通过时，保留标准loss/autodiff与原物化路径。<!-- source-family:SF-2026-ARXIV-2610-05559 -->

拟本人注：CutBCE `2610.05559v1`，6分，§III/IV/T2–3必要证据；限通用Bernoulli-BCE loss执行机制，不纳推荐效果，不把算子HBM或作者单测当全pipeline预算/复现；Source/PRE/POST待独立实际核验。
