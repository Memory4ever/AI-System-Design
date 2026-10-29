# 2026-02-05 补查：VTok Source / Owner PRE

本日仅补充2026-02-04北京完整自然日，date-only。原33行、原窗口、评分及连续原§4保留；原先VTok因精确时刻不能落原小时窗而保留，现由Seed官方PublishDate=1770134400000对应Feb4独立恢复，不以arXiv Submitted作公开日。root已独立核Seed日期、完整v1题摘、必要§3.1–3.2/§4.1–4.4及代表Google排除，准入2+2+2=6通过。

## 支持与不支持

exact-v1 §3.2 Eq13–15：首帧空间tokens，后续帧共享同一feature encoder，以相对首帧feature差经g_phi投影形成motion token，抽象接口S+T−1。不是读取视频压缩文件的codec motion vectors，也不是相邻帧差，更非像素无损。§4.4/T4局部短视频同框架对照支持空间重复与时间读取的预算分配；T5/§4.4默认6FPS、6frames-per-token及tokens增长方向存在自冲突，不认证可部署采样recipe。§4.1声称冻结CLIP/decoder、只更新MLLM，但g_phi更新和continuous visual latents对unified vocabulary接口未充分说明，不采用实现保证。T3非训练Llava Video-MMMU41.3→41.2反侧保留；额外finetuning、encoder与decoder成本需另计，不由token数量推出端到端速度。原源码/性能未复现。

## 唯一owner比较

Owner MULTIMODAL-REPRESENTATION，Ch23当前Codec-aware tokenization节。实际对读794–842及邻接：803–810明确compressed codec primitives分支；813–817已有scene-invariant/dynamic分解、scene/epoch身份与镜头切换失效；826–829已有token更少不授TTFT/端到端性能。该正文已有抽象分责和失效边界，但没有“在decoded-frame共享feature空间计算对首帧差、单token bottleneck且不同于codec输入”的替代分支，因此仅列已有主题不足以解释VTok设计。

拟窄增量为一段：在codec二分图之后、scene-invariant段之前加入decoded-frame reference-residual分支；明确参考帧S空间tokens、相对参考帧差的motion投影、预算从逐帧空间重复转为时间覆盖。边界依赖场景短期相近；长期/切镜头/细小新内容可能越过单token容量，dense或重新参考仍合理，属于工程选择推断，不称作者已实现自动reset。正文不写T5默认粒度、通用速度/无损、g_phi训练实现或词表机制；末注留来源及冲突。Ch24只拥有后续AR/diffusion采样，不重复推导本表示接口；Ch22的长context状态不拥有视频codec。

请求root独立Owner PRE并确认是否需要该窄段；若同意写入再申请Ch23单owner锁，未获锁前不写Books。当前没有书稿修改。
