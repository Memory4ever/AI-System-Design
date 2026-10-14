# Video early screening 窄 PRE（未写 Books）

Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。reader实际S3–7 Source `2+1+2=5`，作者实际S5–6接口；[精确原件](SUP_RESUME_CORE_2603-30043v1_20261013.json)，current正常日门[字段](SUP_RESUME_DATE_2603-30043_20261013.json)待root。Ch24 clean-estimate修订与跨尺度preview实际局部已读，Ch25外部环境dynamics不接此采样state。只申请跨尺度preview后、latent-HR mapping前一段及本人注；其余正文保留。

## 完整拟局部

~~~~markdown
跨尺度还有一条不锁定最终像素的preview分支：先用低分辨率状态筛选seed或prompt，选好后重新运行标准高分辨率生成，而非把LR结果上采样后继续当作完整HR轨迹。它要求检查downsampler `D` 与velocity是否近似可交换；不成立时，用短窗口缓存的HR velocity校正LR更新，selector与correction共同决定预览能否保留有用语义。<!-- source-family:SF-2026-ARXIV-2604-09227 -->

这把大量候选的HR成本换成有条件的LR筛选，却增加downsampler选择、早期HR计算和缓存漂移；commutator小是局部近似，不是完整HR等价或任意flow天生scale-compliant。[受限Flux/SD3.5实验](https://arxiv.org/html/2604.09227v1)以A100上的quality、LR/HR相似和实测latency比较，不能把预览速度直接当最终图像交付速度。细节影响选择、近似失效或筛选成本不合算时，直接HR采样仍合理；选择结果也不能跳过最终HR质量验收。

预览也可以保持原分辨率，只提前停止大多数种子的去噪：在固定probe步解码当前clean-state估计，以任务相关轨迹代理排名，仅让少数种子完成原采样，再验终态。它不等于早期画面已经正确，motion-energy一致性也不认证路径顺序；[受限maze对照](https://arxiv.org/html/2603.30043v1)支持早筛与最终检查的分责，却不能由路径长度相关性签唯一失败原因。若单段生成不足，可只把未违规且确有向目标推进的末帧用作下一段条件；没有合法推进就停止，而非把生成画面当真实环境反馈。每个probe的VAE解码、候选判断及每层chain采样都付费，max-three chaining对照的总预算也高于单轮best-of-N，不能把长链7→67当单模块免费增益。早期排名不稳、约束被视觉作弊绕过或链式误差放大时，保留完整种子采样、更短任务与独立终态验证，不由低NFE或稳定计划批准物理动作。<!-- source-family:SF-2026-ARXIV-2603-30043 -->

跨尺度状态也可以由受训的latent映射接入高分辨率生成，而不先解码成像素、插值后再编码。此时latent重建、解码后的像素误差与相邻帧差分是三个不同目标：latent接近不保证没有block artifact，逐帧像素好也不保证时间一致。高分辨率refinement还可分别限定低通分支进入attention的高噪声阶段、高通分支进入FFN的低噪声阶段；频带、算子位置与训练噪声支集需一起绑定，不能将它们统称一个通用课程或认证频率因果。[受限对照](https://arxiv.org/html/2602.11564v1)中更高分辨率的平均质量仍退步，普通LoRA也有较差FID；数据筛选/锐化与接口共同变化，不保证所有质量提高。中间codec往返被省去，最终decode、像素监督训练、latent映射及expert计算仍付费，不能用单模块速度授整条4K实时。跨尺度失真、时序回归或总费不合算时，保留RGB级联、普通latent插值与原HR采样，并验最终输出而非只验latent。<!-- source-family:SF-2026-ARXIV-2602-11564 -->
~~~~

## 当前尾部后仅追加本人注

~~~~markdown
- `SF-2026-ARXIV-2603-30043` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.30043v1)必要§3–7，2+1+2=5；same-denoise probe/top-K完整采样与valid-pivot frame链。保480maze、Wan14B40步/Hunyuan1.5distilled8步、motion-energy无序代理、VAE每probe约1.5FE、max3chain1200-vsBoN400/反退及全费，不采唯一path因果、普遍端到端倍率或物理保证；未核artifact/视频或复现。
~~~~

未获锁/未写；root逐字PRE/当前邻接通过后申请该一段和本人注窄锁，nonwriter实际POST另做。
