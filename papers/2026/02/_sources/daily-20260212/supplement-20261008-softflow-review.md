# SOFT-FLOW：必要命题审阅，待实际Source

原件 exact-v1题名Sample-Efficient Real-World Dexterous Policy Fine-Tuning via Action-Chunked Critics and Normalizing Flows，https://arxiv.org/html/2602.09580v1 与官方PDFv1首页一致；SOFT-FLOW为方法名，不用当前DataCite的SERNF题名倒填。root完整AB/日期包络通过。拟2+2+2=6：diffusion action likelihood难直接求/逐step Q与chunk执行错位→invertible NF完整chunk likelihood与chunk-boundary discounted target→重新选保守offpolicy目标与控制粒度。

必要已读III/IV §§A–E/Eq5–8/Algorithm1–3、V–VII/Table1–2、AppA-C2/D1–D2/E。NF动作→Gaussian/inverse采样/RealNVP determinant用于数据NLL与Q+BC正则；不是精确环境分布或安全动作证明。动作normalize加Gaussian再atanh要求合法support，NF exact-density与inference sigma.7改采样律分开。chunk critic为H内折扣reward加gamma^H次boundary value，H10不是逐step bootstrap的静默替换。离线critic warmup→actor Q+imitation→online mixedreplay；candidate bestQ和many-NF-samples都付费，critic误校准仍可被利用。Algo3 actor更新行没显式gradient，与文字maxQ-lambda L_IL不当完整运行recipe，未核代码。

Table2 NF/ACT/FM仅IL的表达力对照与后续RL收益分开，ACT H20 vsNF H10、ACT temporal aggregation、FM8steps不是同executed-contract。成功轨迹IL再加online数据可退步，offline grasp .8但cut0且学counterproductive backward，onlinecut.7而grasp .7；不把exact likelihood归因全部改进。§V文字50 online+121=171，Table2 full181，在线梯度5×500=2500与AppC2 4000亦不一致，故不采用精确总样本/训练recipe保证。剪刀10testconfigs/10runs，无realworld重复seed/CI；cube105min/58trajectory6.25RPM、探索初跌/平均每trajectory仅1.01turn，不授长程不掉落。sim4seed/100rollout与robot10配置不可混。

视觉DINOv2/pretrainedpose与simulationteacher20M更新不算free；单GPU H200/A100训练、RTX4090 inference/distill，另3090Ti .24s/3090 asynchronous系统为各自披露配置，不能合成统一latency SLO。剪刀35hIL+21h offline、cube4day distill+2h offline不等105min onrobot预算；候选数real init64、RL24与硬件费用/precision NotDisclosed分开。人工reward、occlusion/no tactile、unsafe/infeasible终止及掉落反侧保留。原文VLA大规模适配是futurework，不称已证foundation VLA transfer；当前具体现象仍支持chunk控制/likelihood接口主线。Source后核MULTIMODAL-EMBODIED-VLA owner差额，尚无PRE或写锁，未运行代码/复现。
