# 2603.09030 — PlayWorld exact-v1

Daily2026-03-12补充自然日2026-03-11。本日SUP_EXACT_BATCH4/ADMISSION_BATCH4及独核AB/date夹证复用，current无撤回；只采用[exact-v1](https://arxiv.org/html/2603.09030v1)。2+2+2=6；实际读§3机制、§4必要设置/评价/组件、§6限制，非只AB。评分与具体Books判断分开。

§3.2让VLM生成指令扰动、预训练VLA执行play；每关节限制、对象边界reset及人工监看/更换物体仍在，连续8小时采集不等无人安全。§3.3为DROID初始化SVD空间/时间factorized attention、逐帧action条件、三视角；8H200/batch64/2天full训练。Curriculum并非生命周期无标签：少量成功human demos形成CLIP/Kmeans success centroids，play样本按到centroid距离分rank逐渐扩大采样。距离是任务相关proxy，不是标定物理难度或接触真实性，play policy支持仍限制transition人口。

§4比较30h play与6h demos、human play和同DROID初始化，但数据时长/人口不同，不能以更多交互唯一证明自主来源因果。500余clips、20余policies、6类human行为；按GT action回放的LPIPS/SSIM只测视频一致。18项policy的20次real与50次sim trial，Pearson .8766只校准受测policy/object/control mode排序，不授任意新policy。human play更差且模糊，直接反证“多样性越多必好”。DSRL冻结diffusionpolicy只学initialnoise，reward仍需small demos/progressproxy，两个任务的想象RL不认证所有物理或安全。未采未独核图像曲线的65%因果/分母。§6明言冗余、playpolicy能力依赖、open-loop/horizon/controlmode discrepancy、仍hallucination、受控lab外扩展未解决。完整precision/seedsCI/全采集人工与reset费用、端到端tail/concurrency/SLO ND，未运行artifact。

Books具体NoChange提案：owner MULTIMODAL-WORLD-MODELS（Ch25），实际Channel/support36–66，校准/失败动作/三种评价1253–1283；Ch26闭环交接实际读。采用的长期命题仅是action support受采集policy限定、失败/部分动作须作真实transition证据、视觉质量/策略效果/克制需分别验收。前述局部已具体覆盖三项，不能把success-centroid的proxy称无监督物理真值，不把有限Pearson推广为任意policy校准。Curriculum具体配方及30h人口留报告，不为论文名新增段。无PRE/无Books写入，reviewer本轮实际打开必要exact-v1及具体owner局部，Source/date/6分与NoChange通过，不授DAY。
