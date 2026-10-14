# OmniRoam30045 受限 owner PRE（未授锁、未写 Books）

Source5由screen准备、resume reader实际独核；Owner `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24。仅global panorama preview→scale/visibility条件refinement，一段/本人末注；不授world-state、一般camera motion或实时保证。日期独立层待闭；与Video PRE同anchor zone，root若授锁需先决定两个新增段的顺序，作者不自写。

## 当前完整局部与拟段

这把大量候选的HR成本换成有条件的LR筛选，却增加downsampler选择、早期HR计算和缓存漂移；commutator小是局部近似，不是完整HR等价或任意flow天生scale-compliant。[受限Flux/SD3.5实验](https://arxiv.org/html/2604.09227v1)以A100上的quality、LR/HR相似和实测latency比较，不能把预览速度直接当最终图像交付速度。细节影响选择、近似失效或筛选成本不合算时，直接HR采样仍合理；选择结果也不能跳过最终HR质量验收。

还有一条面向全景长视频、而非seed筛选的global-local分支：在近恒速、固定朝向的数据条件下，以位移方向与全局scale先产生较快的全程全景preview，再按scale与稀疏可见条件分段refine，恢复目标速度、时间步与分辨率。Preview提供共同的长程条件，不拥有最终像素或真实环境状态；局部refiner仍须分别验质量、跨段衔接与轨迹控制。[OmniRoam的受限对照](https://arxiv.org/html/2603.30045v1)支持这一路线，却不证明任意旋转运动、metric geometry或场景身份永久一致；首尾CLIP-loop比值也受中途相似度分母影响，不能当闭环世界真值。两阶段训练、preview、各段refinement和最终解码均付费，较短preview与完整长序列的质量不能拼成同一指标。相机条件失配、局部细节影响全局路径或段间漂移时，保留原HR/较短视频、重新观测或重新生成全局条件，不从preview快推出整条实时交付。<!-- source-family:SF-2026-ARXIV-2603-30045 -->

跨尺度状态也可以由受训的latent映射接入高分辨率生成，而不先解码成像素、插值后再编码。此时latent重建、解码后的像素误差与相邻帧差分是三个不同目标：latent接近不保证没有block artifact，逐帧像素好也不保证时间一致。高分辨率refinement还可分别限定低通分支进入attention的高噪声阶段、高通分支进入FFN的低噪声阶段；频带、算子位置与训练噪声支集需一起绑定，不能将它们统称一个通用课程或认证频率因果。[受限对照](https://arxiv.org/html/2602.11564v1)中更高分辨率的平均质量仍退步，普通LoRA也有较差FID；数据筛选/锐化与接口共同变化，不保证所有质量提高。中间codec往返被省去，最终decode、像素监督训练、latent映射及expert计算仍付费，不能用单模块速度授整条4K实时。跨尺度失真、时序回归或总费不合算时，保留RGB级联、普通latent插值与原HR采样，并验最终输出而非只验latent。<!-- source-family:SF-2026-ARXIV-2602-11564 -->

## 拟本人末注（仅在写入时当前末尾追加）

- `SF-2026-ARXIV-2603-30045` — Daily 2026-04-02补04-01自然日；[exact-v1](https://arxiv.org/html/2603.30045v1) §3.1–3.3/4.1–4.4/Tables1–2，2+1+2=5。只采fixed-orientation/near-constant-velocity panorama global-preview→scale/visibility local-refinement。Table1只81frame质量、Table2全641不混；loop=(1−S2)/(1−S1) CLIP proxy非geometry/persistent identity；crossbaseline backbone与帧数不同、两阶段/segments/全费保留，未核artifact/复现或实时扩展。
