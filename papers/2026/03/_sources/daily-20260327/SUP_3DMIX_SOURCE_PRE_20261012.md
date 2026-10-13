# 3D-Mix24393 必要Source与逐字PRE

root actual nonwriter POST（2026-10-12）：实际顺读 live Ch26 50～83完整标定几何→新69/71→主动view及本人静态注2378，逐字对回本 packet 原两 PRE 与本人注；复用未变的本人必要 exact-v1 Source/PRE，不重复附件或修订比较。geometry hidden/action conditioning gate placement与metric frame分责、ID/OOD反转/零噪声非因果、全费与独立controller退路均在机制附近，原邻接完整保留，新注仅静态证据范围、不含执行收据。实际写后与衔接通过；限定 diff 校验另列，不授 DAY 或实验复现。

root 独立必要Source/PRE：实际核 exact-v1 §3.3–3.4/T1、§4.1–4.4/Eq1–10、§5.1–5.3/T2–3与Fig3必要文字，顺读liveCh26 50–87完整metricframe→主动view/相机适配交接。全sequence meanpool广播semantic+geometry逐token/channel gate，原序列和fused tokens同供actionexpert；final/per-layer分别placement，geometry一次复用不等metrictruth。T1 ID/OOD反转、逐任务反退和零/噪声输入非3D语义因果保留；局部费用/所有runtime未披露不补deadline。具体差额成立，两原拟段/纯注通过，可soleCh26指定锚窄写并做actual非writerPOST，不授DAY。

root官方题摘潜力通过；日级26原字段NEXT_DATACITE。拟2+2+2=6，具体actionconditioning融合差额深入。实际[v1](https://arxiv.org/html/2603.24393v1)§3.1–3.4/T1、§4.1–4.4/Eq1–10、§5.1–5.3/T2–3/Fig3text必要完整读；未核artifact/复现。

9fusion同Qwen3VL4B、frozenVGGT1B/8H100、60ksteps/global128/ZeRO2；BridgeV2→SimplerOOD与LIBEROindomain不同人口。MLLM全部sequence meanpool成globalsemantic，在每geometrytoken上与projectedgeometry concat给sigmoidchannelgate；fusedgeometry仍与原MLLMsequence拼接给actionexpert，不把MLLMhidden直接逐像素配对。GR00Tfinal layer fusion，pi-style每相关层各gate、VGGT只extractonce。hiddengeometry不是显式depthmetric坐标，也不认证counterfactual当前task几何truth。

T1 AEfusion在LIBERO97.4高于base96.5却SIMPLER3.13远低57.81；Visualfusion更低、gate68.23/98.05并非所有task最高。T2/3多个backbonepair有single-task反退，个别增量很小；无逐seed不确定性/完整memorylatency所有runtime对照，不采稳定跨本体/全hardware胜利。Fig3zero/randomgeometry消融损伤说明该representation输入有用，不隔离其「3D语义」而非oodfeature扰动；frozen comparable/better和sparsefusion comparable/lower memory的作者text只支持局部取舍，不授既已量化taildeadline。VGGT常驻、额外token/actionattention、每层gate、训练和校准均费，plug-and-play非零费用或实现已核。

## actual owner差额与PRE

Books公共上下文、Ch25开篇/Ch27交接已核，MULTIMODAL-EMBODIED-VLA Ch26实际50–73完整标定geometry→action+主动view邻接。当前明确metricframe与controller，但没有「hiddengeometry可在semantic/actionexpert交接处按task gate、不等显式metric」；拟标定geometry原完整两段后、主动view前两段，唯一ownerCh26，不在Ch23重复VGGT训练。

已有几何先验还可通过 learned feature 接入动作模型，而不先转成米制 waypoint：让冻结 geometry encoder 读取当前多视角图像，将其 tokens 投影到动作条件维度，再用语言与视觉 hidden states 的全局语义摘要逐位置、逐通道调节融合比例；原语义序列与这些融合 tokens 一起进入 action expert。最终层读取与逐层读取需要不同的 gate placement，几何提取却可以在各层间复用。这个接口适配的是 action conditioning，不提供已标定的实际坐标或物理真值。<!-- source-family:SF-2026-ARXIV-2603-24393 -->

增加 3D features 并不意味着融合越早、越宽或越频繁越好。[相同骨干的受限九接口对照](https://arxiv.org/html/2603.24393v1)中，有的融合提高 in-domain 平均值却明显损伤 real-to-sim，有的任务在总体改善时仍退步；把 features 换成零或噪声也不单独证明收益来自真实三维因果语义。Geometry encoder、额外 tokens、attention/gates 与训练都付费，冻结和稀疏复用只减少其中部分成本。任务条件、表示或资源不可靠时，应保留原语义 policy、已校准的显式几何与短 chunk 重观测；controller 仍独占可执行性、deadline 和安全验收，不让融合 gate 签发物理授权。

拟静态注：

- `SF-2026-ARXIV-2603-24393` — [3D-Mix exact-v1](https://arxiv.org/html/2603.24393v1)§3–5/T1–3/Fig3text。仅geometryhidden/actioncondition gate placement与metricframe分责；保9fusion的ID/OOD反转/任务反退、zero/noise非3D因果和全费，不采稀疏融合精确deadline/physicaltruth/普遍稳定，未核artifact/复现。
