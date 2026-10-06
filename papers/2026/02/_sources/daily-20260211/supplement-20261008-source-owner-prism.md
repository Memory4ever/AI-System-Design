# Prism：必要Source与owner差额/PRE请求

2602.08426v1；2+1+2=5（具体长期差额深入）；root完整题摘/Feb10BJT上下界通过。原件 prism-core.json 完整§3/4及必要§8/9，无artifact/复现。

## 实际必要命题与反侧

§3.2在block内pre-RoPE内容近稳定条件下，B个相位均值幅度 λ_j(B)=|sin(Bθ_j/2)/(Bsin(θ_j/2))|，是有限几何和，不证明trained激活都常数，也不是所有高频严格消失。§3.3 RMS能源观察非局部特征重要性的因果证明。

§3.4 first64与last96两band在d128重叠，并非独立正交语义/位置分割；各自blockpool、RMS比温度校准、Top-P mask union，是training-free block-only selector。Eq11–13给approx logit scale，不当全attention分布恢复或校准概率。§4.4高频只取deadzone32时只放大noise且退，不能说已丢信息靠温度精确恢复；transition64必要，阈值/overlap均影响density。

评价Llama3.1-8B/Qwen3-8B（YaRN32→128k）/Qwen3VL8B；B128、dhigh64/dlow96、Top-P .95/.93、customTriton，baseline各recommended参数未匹配同density/quality，所以不认证allpoint优越。LongBench avg41.08<full41.47、39.12<39.49；RULER128k Llama72.75<77.77，Qwen72.65<75.09；LVB64.25<65.00；headlineparity不覆盖所有切片。5.1×是128k attention prefill vsFA2/H100非完整TTFT、decode、servingSLO；20%memory是selector workspace vsFlex非峰值E2E；precision/batch/concurrency/outputlength/repeatsCI未披露。§9 B64更细但128kselector约22ms> B128约9ms，密度-粒度-质量要一起核。

## 实际owner差额

MODEL-LONG-CONTEXT Ch22 205–225访问图/质量分责、348–366完整hierarchypooling miss和学习summary已实际读；现有pooling ancestor miss还没明确RoPE相位下跨token平均会系统压不同频率，或two-band overlap/RMS温度作为保留弱信号的可替换selector。Ch13 133–165含一般RoPE与低秩激活内容条件，不能充当已覆盖pooling校准机制。Ch21/23入口已读；唯一owner Ch22，不复制RoPE原理到Ch13/推理章。

最小一段拟放当前PISA pool-miss段之后、hybrid span-search之前。尚未Source/PRE或写锁，未写Books。

## 最小拟文

Pool 的漏选还可能来自位置编码而不只是摘要容量：block 内内容近稳定时，RoPE 的相位旋转使跨 token 均值按频率衰减，局部位置信号与较慢变化的内容分量不能默认保有相同比例。一条无需重训的选择分支分别对高、低频 band 的 pooled Query/Key 评分，用各 band 相对全向量的 RMS 比例调整温度，再取两张 Top-P mask 的并集；band 可以重叠，温度也只是选择校准，不恢复已经消失的信息或证明 dense 等价。只放大近零高频还会放大噪声，因此 block size、频段、阈值、真实 density 与任务质量要共同验收。有限 long-context 对照仍有检索质量退步，attention prefill 的加速不包含完整 serving；额外评分、mask union、tile overfetch 与校准漂移均付费。内容不满足近稳定条件、关键证据漏选或净延迟不合算时，保留更细粒度、原 selector 或 dense 回退。

拟链接 exact-v1#S3，末注保RULER反侧/H100 attention-only与频段条件。请求root实际必要Source、Ch22邻接/PRE，再协调窄锁。
