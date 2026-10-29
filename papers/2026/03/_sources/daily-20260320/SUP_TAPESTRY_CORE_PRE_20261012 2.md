# TAPESTRY17735：显式几何条件与自遮挡补齐 / 必要准备

resume_mar17，2026-10-12，仅03-20补03-19。原2+2+2=6、22有限尾准入/date独核§30有效复用；不以Submitted单独作公开日。只核几何载荷、生成中间表示和后续消费的具体差额，不扩query、旧版本或附件。本准备未自授Source/PRE PASS、Books写锁、safe或DAY。

## 1. 必要原证与停止

[exact-v1 HTML](https://arxiv.org/html/2603.17735v1)完整题摘、§3 L88–119、§4.1设置与§4.2/T1–3 L123–179、§5直接限制L180–187实际读。current官方abs同题七作者、单v1与轻量说明已实际核，无本采用相关纠错/撤回说明。恢复后只定点再回§3与T2/3/限制，不展开References、supplement视频、demo、代码或复现；支持与直接反侧够即止。

固定外部normalized mesh和环形look-at-origin相机轨迹先渲染aligned normal/position视频；冻结video VAE分别编码几何、已知视频和inpainting mask，channel concat经小geometry fusion，再与noisy latent和时间补齐的初始帧latent共同进入DiT。文本/初始帧embedding另作cross-attention context。该拼接是学习条件，不是逐像素硬约束、从视频发现真实几何或action-conditioned dynamics；“strict/pixel-perfect”作者措辞不作保证。§3称full-finetuning，§4.1实际LoRA rank128 all DiT linear加geometry module，不补成精确统一训练recipe。

生成TTV用ray tracing可见性回投UV，angle/depth加权形成partial texture和confidence map；置信权重不是真值校准。一次轨道因self-occlusion留下孔洞后，§3.2明确旋转物体base、相机轨迹沿用，渲染新几何、已有partial texture与missing mask供条件二次生成，再回投更新纹理；不是独立第二段video，更不是新真实观测。紧接多stage段又称multiple camera trajectory sets，因此不采用完整迭代/视点调度recipe、必收敛或full-coverage保证，只采生成产物成为下轮条件的接口。

## 2. 关键评价、反侧和费用

Wan2.1底座，约30k Objaverse meshes normalized unit sphere，随机半径/高度/FOV/旋转及四env lighting约120k TTV数据；200 GSO/Objaverse test meshes。单DGX Spark训练约10天，61帧/4步视频约30s，T2纹理87s是不同阶段口径，不作端到端SLO。T1与T3有限指标支持geometry-condition局部取舍，但底座/训练与条件不全相同，不证明normal+position唯一因果或普遍必要；user study未披露样本/盲测/重复，不作统计推广。

T2纹理87s慢于HY3D33/TEXGen15/MV-Adapter32，快于Paint3D96；不是全部更快。progressive inpainting vs naive independent TTV仅相关正文/Fig6 caption的定性支持，未像素核或取得覆盖率/收敛定量；3DGS只有正文/Fig7 caption及demo线索，不授真实场景一致、材质或动作效果。§5明确clean mesh/topology前提，appearance含video model lighting而不易relight，不称可控物理材质。输入几何准备、renderer/VAE、采样多pass、ray tracing/fusion、3DGS与训练/调参全部计费；precision、并发/deadline、全部seed/CI和完整总费Not Disclosed。

## 3. actual唯一owner与差额

sole `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。实际完整885–947的evidence ladder、视觉/三维分验与随机rollout邻接，Ch23/24/26入口实际读。现925/927已说明几何评价不能替动作效果，未承载**外部固定mesh的法向/位置载荷→条件appearance video→回投UV/后续3DGS**及**已有partial texture成为遮挡下轮条件**；不是因为主题相近就必写。拟原2605-15185 marker完整后、随机rollout前两短段；非preparer可裁更小PRE或specific NC。几何状态输入资格由Ch25拥有，VAE/DiT一般机制不重复到Ch24，真实行动不交Ch26安全签字。

## 4. 待裁两literal PRE

几何也可以是生成前已给定的载荷，而不是模型从视频发现的世界状态。一条受限分支固定输入 mesh 与相机轨迹，渲染对齐的法向和位置视频，经冻结 video VAE 与小融合模块编码，再和 noisy latent、初始帧及文本共同条件化 appearance video；生成的环绕视频随后回投 UV，或作为神经渲染的训练输入。[显式网格条件](https://arxiv.org/html/2603.17735v1)改变几何进入生成器及下游消费的位置，却不把 latent 拼接变成硬几何约束，也没有得到 action-conditioned dynamics。应分别保存输入 mesh/pose、生成视图与回投结果，独立检查视觉质量、几何偏差和后续用途，不从同一组感知指标签发真实状态或控制可靠性。<!-- source-family:SF-2026-ARXIV-2603-17735 -->

单条环绕轨迹不能看见全部表面时，独立再生成一段视频可能让重叠区域出现不同外观；另一选择是旋转已有的部分纹理网格，重新渲染几何、已有纹理和缺失 mask，把它们作为下一轮生成条件后再回投更新。这是复用生成产物的条件补齐，不是新增真实观测；角度/深度加权的 confidence 也不是正确概率。有限纹理对照有更慢的结果，补齐与3DGS展示未认证所有遮挡、完整覆盖或物理材质；干净拓扑仍是前提，模型带入的照明也限制重打光。几何准备、渲染、VAE、多轮生成、回投与重建均付费。需要可控材质、严格几何或实际环境决策时，保留明确网格、确定性渲染和独立用途验收，不把更完整的appearance当作世界动态或动作安全。<!-- source-family:SF-2026-ARXIV-2603-17735 -->

静态源注：

- `SF-2026-ARXIV-2603-17735` — [TAPESTRY exact-v1](https://arxiv.org/html/2603.17735v1)必要§3、§4.1–4.2/T1–3及§5。仅显式mesh几何条件→appearance视频→UV/神经渲染消费、已有partial texture条件二次补齐；保学习条件非硬约束、自遮挡/拓扑/照明限制、定性展示和速度反侧/全费用，不采精确视点/融合recipe、必覆盖、真实世界动态或控制保证。未核supplement像素、代码或复现。

## 5. 待独立裁与实际写后

交resume_review17_18非preparer必要Source/actualowner/两literal与static。准备者不自验，不在root授窄锁前写Books；写后须一次非writer实际完整邻接和本人静态源注POST，单项通过不授DAY。

## 6. 授权后的实际 writer 回读

root在reader§44必要Source/actualowner/原两literal与static有限PASS后授sole Ch25本family窄锁。作者仅将原两literal写入当前929/931，静态本人注1773；写前完整885–950与末注、写后实际913–955及1766–1773本人/邻注顺读，确认15185完整marker→显式几何/条件补齐→随机rollout与反馈责任衔接。两literal逐字包含检查均true；本family仅六新增行，章numstat62/0→68/0，限定diffcheck0。没有改EVA或其他既有正文/注，也没有授实际POST、safe或DAY；交resume_review17_18一次非writer实际完整局部和自身静态注回读。
