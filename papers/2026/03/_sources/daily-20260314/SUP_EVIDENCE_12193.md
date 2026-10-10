# 12193 SaPaVe：必要Source / Ch26具体差额与逐字PRE

mar14_supplement，03-14只补Mar13 BJT。root完整题摘及七日级夹证独核复用；CVPR接受/project link不指具名dated早正文，不继续全会议库。exact-v1 SUP_NECESSARY_12193.raw/txt / SUP_STOP_GATE_MANIFEST_RESULT.json GET200；本人实际§3.1–3.4(B31–46)、§4.1–4.6完整Tables1–5(B48–107)、AppendixA(B188–192)、D/E必要实现(B312–389)、G(B404–414)，题名九作者已核。Intro B23–30第一次输出截断不声称全Intro已读；不读B数据生成全部prompt/C资产任务catalog/F展示/代码或全部图。

准入→实际命题：固定优质view训练/统一camera+body输出容易缺主动取证先验→2DoF相机与26DoF操作decoder分工，先训camera LoRA/head、再冻结adapter混合两类数据joint-train动作头，3D条件另接动作cross-attention→改变取证动作怎样适配而不把相机转动直接混入旧manipulation先验的选择。**拟2+1+2=5标准，具体Ch26知识缺口使受影响机制深入**。2针对实际相机/身体监督与冻结接口而非LoRA、Diffusion/加法融合的发明；Reach1是active manipulation局部policy，Durability2为可复用的取证动作适配边界，不凭31.25数字或机器人关键词加分。

机制必要限定：§3.1 current RGB和可选几何，chunk头pitch/yaw相对变化与26关节变化，不是任意本体统一。§3.2 camera adapter LoRA不改原VLM主权重，两个action decoder；MapAnything spatial tokens投影后与语义tokens相加，送DiT cross-attention，主文称可选几何不认证任意噪声/标定错误都可用。§3.3 Stage1仅camera adapter/head监督；Stage2冻结camera adapter，mixed camera/manipulation监督两个head；E0.1明确共享DiT后两MLP decoder，不是两个完全独立policy或解耦物理动力学。E0.3 Eq3–4为几何/语义相加后作为cross-attn K/V，动作noised token为Q；不把这个conditioning KV叫共享ARcache。E1具体MSE与E0.1 denoising目标各保角色，不补造全部optimizer实现。

评价/反侧：Table2同底层架构固定camera36.17、fixed+wrist52.33、active+wrist73.16、active-only74.83，支持视角可控的受测差额，不支持wrist camera普遍有害。AppendixA明确head数据两stage都有、paired head-wrist只有20k/stage2，额外视角比较兼有数据失配；不唯一归因噪声。Table3真机π0/GR00T fine-tune扩入camera分别45/53.75 vs85平均，模型/数据/结构一起变，不纯归因分头；85−53.75=31.25百分点，非31.25%相对收益。Table5去Stage1/Stage2/分头/adapter/几何均在受测四类退步，分头71.25与全部85只支持所设训练接口，未验证任意camera/body混合或所有因果路径。

Table1测pitch/yaw到标签容差的success，不等manipulation/task安全；不同VLM有point→geometry映射等不同解码协议，84.3−72.7=11.6个百分点，不照搬Intro16。Table4有限对象/灯光/背景、A大视角动作仅45%success，不外推全开放世界。D真机G1/双臂Inspire3/D455/custom双servohead；G固定底座、手臂reach受限，转头找到目标不意味可抓/可全局导航。trial总数/seed/完整硬件训练预算/precision/并发/完整控制尾延迟未披露处保留Not Disclosed，未对实机物理执行复现。geometry encoder、LoRA训练、生成数据/遥操作、视角动作和jointdecoder均计费，不授deadline或碰撞安全。

实际owner/PRE：MULTIMODAL-EMBODIED-VLA / books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md，完整31–73主动视角/坐标局部与Ch25/27开头交接已读。现69段是future point-flow/view-prior guidance，不承载两动作head的监督和adapter冻结次序；71段是virtual re-render≠fresh observation。这是具体可承载缺口，拟在69后/71前两段，不改两既有分支，不写共享Books，待非准备者必要Source/实际owner与逐字PRE独核后由root写。

## 拟逐字两段

主动取证还可以先改变动作的训练接口，而不让相机控制直接占用原 manipulation decoder 的同一输出：共享感知与动作骨干，在末端分别解码相机 pitch/yaw 和身体关节变化。先用 image-language-camera 示教只训练 camera adapter 与相机 head，再固定这份 adapter，把相机与操作数据混合，联合训练两类动作 head；可选几何经投影与语义表示相加，作为动作去噪的 cross-attention 条件。这样保留“往哪里看”的适配接口，再学习“看过以后怎样操作”，不是两个完全独立的闭环，也不由冻结 adapter 证明语义能力或物理动力学必然不受干扰。[受限主动操作对照](https://arxiv.org/html/2603.12193v1#S3)支持这份监督与结构分工。<!-- source-family:SF-2026-ARXIV-2603-12193 -->

分工增加合成相机示教、真实操作数据、geometry encoder 与联合 decoder 的费用；不同动作维度、chunk、观测和标定仍要对齐。额外 wrist views 在受测设置中没有继续改善，作者同时指出两阶段 paired head–wrist 数据较少，不能推断更多真实视角本身有害；固定底座也让相机可以看到但手臂不可达。局部成功率与几何 conditioning 不签发碰撞安全、全局搜索或完整控制 deadline。视角/几何失配、目标不可达或更新费用超预算时，保留固定或已校准视角、目标本体示教、短 chunk 重观测和独立 controller/停机接管；原有 future-view guidance 与简单固定-view policy 继续是各自约束下的合理路径。<!-- source-family:SF-2026-ARXIV-2603-12193 -->

最新落地：root必要Source/owner/逐字PRE实际通过并窄写Ch26两段，mar14_supplement真实非writer POST见SUP_POST_12193.md；root回读实际53–80完整邻接/本人note后同步PASS释放。正式本日已计一整合家族，不授DAY。
