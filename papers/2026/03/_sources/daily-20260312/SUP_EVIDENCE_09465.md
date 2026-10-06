# 2603.09465 — EvoDriveVLA exact-v1

日期/current完整AB复用本日SUP_EXACT_BATCH3/ADMISSION_BATCH3和独核同2026-03-11夹证；currentv3无本窗纠错/撤回，不以版本升高触发重读或回填。[v1](https://arxiv.org/html/2603.09465v1)实际读§3.2/3.3 Eq2–11、§4/Table1–4、§5。2+2+2=6，teacher权限与具体existing owner对比深入。

copy预训练visual encoder为frozen self-anchor，instruction/ego/GT future轨迹驱动AnchorFormer给视觉tokens的MSE权重，不能当通用视觉能力必保留证明。future-aware oracle另读未来images及ego states，coarse-to-fine候选与hidden-state dropout p=.1/N10扩候选，按GT CE选best后蒸馏hidden与logits；不是部署拥有future，也不是可部署oracle upper bound。Table3从noKD .55到trajKD .54、refine .53、dropout .53、visualKD .52（UniAD平均L2），有限逐项组件收益，未唯一控制全部训练预算；Table1 UniAD collision .12劣于DiMA .07，不能采全维SOTA。Table2NAVSIM PDMS81.9→85.3为作者同3B基准，navtrain1192/navtest136与4秒轨迹；nuScenes ST-P3/UniAD是两协议不能拼。当前student及oracle同Qwen2.5VL3B、teacher frozen。hardware/precision/完整teacher生成、训练steps/seedCI、runtimebatch/concurrency/tailSLO Not Disclosed；teacher/refine/dropout都额外生命周期成本。未核代码或复现，不授collision安全或future causal state。

Books提议已有覆盖（No Change）：唯一owner MULTIMODAL-EMBODIED-VLA，实际Ch26“Training-only Foresight 不是 Persistent World State”419–441已具体承载future teacher只作监督、部署不读真实future、额外teacher计算/bias和direct-policy共存；“Privileged 3D Teacher”93–112承载teacher监督不授runtime观测/真实几何，“Action-facing Representation也是Gradient Authority Boundary”250–284承载窄action loss可干扰general representation与显式适配分责。长期采用命题为这三项权限/代价，不把作者weighted anchor保general能力或最优MC候选升级稳定结论；具体权重/局部nuScenes结果保留报告，不为记录方法名增加章末摘要。不存在Books插入位置或逐字PRE，须独立reviewer实际核这些局部是否足以支持NC。

reviewer本轮实际打开必要exact-v1及三处owner局部，Source/date/6分与具体NoChange通过；仅采用权限/成本边界，不采anchor必保旧能力。正文未写，NoChange无需POST；未核artifact/复现，不自签日级完成。
