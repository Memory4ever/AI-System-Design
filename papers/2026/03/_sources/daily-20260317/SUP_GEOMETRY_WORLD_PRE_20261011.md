# 两几何世界模型：必要Source有效复用与逐字PRE待独核

仅本17补03/16。两exact-v1完整AB已独核，日级arXiv夹证在SUP_DATACITE_MULTIMODAL；全年ID/完整标题定点无有效同事件dup。root本轮独立实际必要核心、关键评价/直接反侧及Ch25/26差额核验，以下复用其原证而非旧done。作者fresh读Ch25 235–275与557–591、Ch24/26交接。两项原2+2+2=6，具体表示消费差额深入；未授Ch25锁/未写，以下不是PRE PASS。

## 12655 VGGT-World / MULTIMODAL-WORLD-MODELS

[exact-v1](https://arxiv.org/html/2603.12655v1) root实际§3.1–3.3、§4.1–4.3、B.1/B.2及D必要：冻结VGGT L0–4早层state接原5–47及多尺度heads，非任意深embedding；1024D clean-z目标对velocity-collapse的局部同设置观察不授维度唯一因果/ELBO稳定。由GT转partially-denoised rollout混合λ课程；fixedlatest-k/m-chunk与实际stride1另分。Jointdecode observed+predicted/globalattention使当前估计依赖想象future，不是新sensor。City/KITTI/TartanAir、1RTXPro6000 96GB训练batch64/48；Umeyama对齐/20kFPS点云非rawmetric真值。Table3两view列同值待说明，Table4Acc .8672→.8764退步而CD改善、frame7后horizon退步；1.9vs9.5s/frame异horizon归一化，不采用通用公平5×。inference precision/batch/concurrency/SLO Not Disclosed，artifact/复现未核。

actual Ch25 frozenfeature/dynamics段已有泛分责，未解释decoder-compatible早层与imaginedfuture反向影响observed几何。拟现2603.09241段后、重建到表示标题前两段：

冻结视觉encoder并不意味着它的任意深层feature都能直接成为可推进状态。若希望复用原几何decoder，可以选其早期residual tokens作为预测接口，再让预测状态经过原剩余层与heads；接口层位、token布局及decoder版本共同定义兼容性。一个受限分支在该空间预测clean future state，并逐步把训练条件从真实history混到部分去噪的预测history，以暴露rollout分布偏移；clean目标在有限设置下较稳定，不证明高维表示普遍只能采用这一目标。<!-- source-family:SF-2026-ARXIV-2603-12655 -->

[VGGT-World的几何消费边界](https://arxiv.org/html/2603.12655v1)还在联合decode时把observed与predicted tokens一起送入含global attention的剩余网络，因此当前几何估计也可能受想象future影响。应保存raw observation与joint estimate的不同身份，不能把更完整点云当作新观测或物理真值；对齐后的误差和局部horizon收益也不授任意长rollout或公平端到端提速。早层状态、课程训练、多步生成及joint decode均付费；接口、horizon或几何回归失配时，保留原观测独立decode、显式状态监督与真实传感刷新，不让预测历史自行修订已观察事实。<!-- source-family:SF-2026-ARXIV-2603-12655 -->

## 12639 RoboStereo / MULTIMODAL-WORLD-MODELS

[exact-v1](https://arxiv.org/html/2603.12639v1) root实际§3.1–3.3/4.1–4.4/6/8/9.1–9.3/10–11：RGB/XYZ twinDiT相同t独立noise、双向crossattention与FFNfreeze jointfinetune；XYZ由DA3depth+camera inverseprojection估计，非独立物理真值/严格3D证明。TTPA VideoMAE2阈值非safety；IEPL同view LPIPS imaginedexpert/agent，OEPL learnedlaterclipweight。Alg1负平均/折扣与正文Eq12求和recipe不同，Table3 ID6 Average数字非前三avg，97%joint headline隔离。16H200训练、Bridge20k320×256/5FPS/7D；MimicGen三任务OpenVLAOFT300demo+128adapt/eval，Realman30demo/6of20→13of20仅有限总结果。0.7sframe/12frames非controlfrequency；inference precision/batch/concurrency/SLO Not Disclosed。WorldArena physicsQwen3judge/depthscaledteacher/actionfollowingCLIP非physicalcausal。artifact/复现未核。

actual Ch26已有verifier/proposal/commit/realoutcome及费用，三policy接口受限NoChange；唯一新增paired twin-noisy state/teacher geometry由Ch25 projective4D承担，不复制26。拟现RGB/depth/flow生成身份限制后、consumer段前两段：

共享一套state与多个输出heads之外，还可把appearance与估计geometry建成两条共同去噪的状态流：同一diffusion time下分别加入noise，让RGB与XYZ分支通过双向cross-attention交换条件。这样显式保留两种表示及其相互约束，却没有取消几何teacher：若XYZ来自单目depth模型与camera反投影，两个分支的误差可能相关，联合生成不等于独立几何证据或严格物理状态恢复。<!-- source-family:SF-2026-ARXIV-2603-12639 -->

[RoboStereo的受限paired分支](https://arxiv.org/html/2603.12639v1)可以为trajectory筛选或policy adaptation提供预测，但视觉匹配和learned权重只是消费者的proxy，真实结果仍由行动后观测决定。其奖励聚合记号及joint平均表存在待澄清映射，这里不采用精确优化recipe或联合成功率headline；twin状态、teacher预处理、joint训练/生成和policy回归均计费，单frame速度也不等控制频率。geometry、camera或proxy质量失配时保留独立RGB/可信几何分支与已验证controller，不让两流互相支持代替真实证据。<!-- source-family:SF-2026-ARXIV-2603-12639 -->
