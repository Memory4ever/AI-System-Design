# 三个已过Source的具体owner窄PRE

只本日原精确v1，复用STOP RAAP §9.26、Mover §9.31、Concept §9.56与已闭正常日门。作者actual Ch26 110–127、Ch24 338–380、Ch5 270–315完整局部。root具体窄锁前不写Books；只三个接口，不采全recipe或物理/ontology保证。

## RAAP 29419 — MULTIMODAL-EMBODIED-VLA / Ch26

在SF2602-18374接触proposal/深度与controller完整段之后、「几何表示还要满足」前。

~~~~markdown
检索到的动作参考也须按消费者分工：静态contact可取单个参考的dense correspondence，动态方向则从多个参考提取特征，经action条件和跨图alignment组合为方向提案；两者不是同一top-k接口。[RAAP的受限对照](https://arxiv.org/html/2603.29419v1)支持这种分责，却有增加参考引入noise、单任务退步和静态contact不在动态benchmark人口的问题，不能把整体MAE改善当每类动作都更好。二维contact/方向再由depth、camera intrinsics和IK/controller转换，几何lift成功与真实抓取仍分验。检索/特征与alignment训练、点云/标定、四秒推理和实际反馈全付费，不是控制deadline；参考支持、表面深度或controller不可达时回退已验单参考/原几何候选、重观测与传统控制，不由zero-shot标签或二维正确批准物理执行安全。<!-- source-family:SF-2026-ARXIV-2603-29419 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29419` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29419v1)III-A–D/Eq1–8/IV/TI–III，2+1+2=5，仅top1 staticcontact与Kreference动态direction消费者分责。保K3 MAE32.55对40.45但drawer16.23>15.45、K4noise、三split/4090训练、FrankaFR3/D455或L515/20placements、mug同70/handlefail与4s非deadline；全检索/训练/标定/执行费，未核代码/复现。
~~~~

## TrajectoryMover 29092 — MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

在FlexAM投影歧义/对应身份完整段后、「相机与角色姿态易互相代偿」前；不插断coarse scaffold正文及其成本。

~~~~markdown
有些运动编辑缺的不是更多二维控制点，而是训练pair怎样消除深度歧义：从同一合成场景构造source/target，利用ray与场景surface的交点或无交点的depth prior提出对应位置，再混合hit/no-hit人口生成配对视频。这约束数据制备的几何选择，用户box仍不唯一指定三维运动；无交点prior、physics修正和清理clutter都可能改变原offset或世界。[TrajectoryMover的受限证据](https://arxiv.org/html/2603.29092v1)支持此pair条件分支，不证明真实任意视频、严格内容保持或物理motion正确；box IoU较低，简化primitive的局部SSIM仍更好，多个judge排序也不同。Rays/simulation/render、配对筛选、混合T2V训练和全部编辑采样均计费；scene/depth支持、身份或质量失配时保留原片段、二维scaffold/普通I2V和人工几何核验，不由自产pair或视觉逼真批准真实环境transition。<!-- source-family:SF-2026-ARXIV-2603-29092 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29092` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29092v1)S3–6必要，2+1+2=5，仅paired raydepth/hit-nohit人口的数据几何接口。保21K/20Ktrain1Ktest但eval40/119assets、Wan1.3B/7:3T2V/8H1003200/81frames、IoU.27与primitivesSSIM.93>full.92、250votes/InternVL10runs异排名；全制备/训练/采样费，不授strict preservation/physics，未核代码/复现。
~~~~

## Concept Frustration 29654 — WORLDVIEW-REPRESENTATION / Ch5

在局部响应诊断SF2601-12703完整两段后、「这条证据阶梯也适用于模型自己的解释」前；保原因果证据阶梯，不把负signedtriangle当ontology。

~~~~markdown
方向之间的“冲突”也取决于谁消费这些表示：可由固定task BB classifier对activation的梯度构造平均Fisher几何，再在该metric下比较CBM概念或SAE方向，保留metric、概念标签与任务head三份身份。三个带符号cosine的乘积为负是一项定义统计关系，合法Gram也可出现，不证明自然概念逻辑矛盾或缺失真概念。[Concept Frustration的受限分析](https://arxiv.org/html/2603.29654v1)只在特定线性Gaussian/独立noise/正定block及人为构造下联系Bayes误差；增加第三概念同时改方向/head容量与监督，不是foundation weights改变或唯一修复因果。Metric可能退化、零分母与所选decision window都限制对象，proxy交叉验证也不等独立机制复现。Encoder取特征、task BB/CBM/SAE训练、梯度/metric、dictionary/window选择、标注和评价全部付费；标签、metric或head失配时保留原probe、受控干预与独立行为验收，不以几何可视化批准ontology修复、因果解释或安全。<!-- source-family:SF-2026-ARXIV-2603-29654 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29654` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29654v1)S2.2–2.11/Eq1–12/Defs1–5/Thm1–2/S3/必要S4与method，2+1+2=5，仅taskBB-derived平均Fisher比较CBM/SAE方向与metric-label-head三身份。保合法Gram负乘积/零分母、.2–.8选择window、C3容量+监督混杂、600matched/60×10seed/n8000/75:25与proxyCV、caption/p13口径；全制备/标注/CV费，未核代码/复现。
~~~~
