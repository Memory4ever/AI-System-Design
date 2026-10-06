# FrameRepeat 16256：必要证据与输入级强化分支

仅03-19补03-18自然日既有有限队列，root准备；2+2+2=6保持。完整题摘准入与日级夹证复用SUP_LATER_ADMISSION及METADATA:929起，arxiv.content findable/created/registered03-18不补造精确公开时刻。当前官方事件页轻量状态核验，不展开版本史。

## 必要 Source

实际[exact-v1 HTML](https://arxiv.org/html/2603.16256v1)完整题摘、§3.1–3.2、§4.1–4.3/Eqs1–13、§5.1–5.4/Tables1–4及A/Table5、B.1–3/Tables6–8支持与直接反侧。只读图2/4文字及caption，不冒称图内所有曲线、定性画面/附件prompt、代码或复现；必要机制和反侧足够，不继续扩读。

训练先固定VLM/CLIP，以原N帧和单帧就地重复的N+1输入分别求gold answer logprob，差额AOI监督3.69M scorer。CLIP逐帧和问题编码，帧PE、crossattention/FFN/score与零中心CLIP prior形成query条件排序；Top16＋Random16混合候选约32次额外打分，标准化差额回归/正负ranking及未打分U负例。U是未经量测的负例假设，单帧marginal gain不保证多帧joint效果或在另model仍保同排序；不能把gold-answer标签写成无答案特权或独立grounding真值。§3 100样本/32逐帧扫描、300样本direct-to-thinking的gold ranking属于离线诊断，不是部署直接读取答案。

部署保留全部均匀采样基帧，在原位置复制TopK；不重新感知、不改backbone、不在每个CoT step再注入，也不等隐藏向量anchor或删帧压缩。诊断attention总和包含original＋copy位置，位置/长度也改变，不能唯一证明视觉遗忘因果或所有hallucination恢复。增confidence只是冻结模型特定答案likelihood，不是正确性校准。

§5/A配置：20K来自LLaVA-Video多选与Video-Holmes训练样本、5次rollout筛掉全对/全错，Qwen2.5-VL7B训练，Qwen3-VL8B Thinking只有限transfer；128帧、1epoch、BF16/ZeRO2、devicebatch1/accum4/effective32、maxcompletion256，训练16generations。没有独立训练seed/CI、实际GPU硬件/全推理tokens、latency、KV/throughput或服务SLO；不推轻量参数等端到端零成本，截图/图像的像素点也未复核。

T1固定Base128对128+8与同总帧CLIP/Random/Bottom支持选择规则的局部差额，不是匹配原128的计算。T4加至16时Qwen2.5各切片低于8、Qwen3多项也退但MLVU更高，不授8普遍最优。B2 no-thinking Video-Holmes41.6→41.5反退；不能声明CoT独有机制或全部任务无损。B1只给top8/16/32/64均比128+8低，也减少大量上下文与预算，不唯一证明未重复帧必须全部保留；B3先TSPO再repeat4优于8，多帧marginal非单调。原TSPO baseline是用于挑复制帧，不是与原论文完整frame-selection能力的等价比赛。attention/probability/quality三项分账。5次过滤、gold-label制造/每帧额外forward、scorer训练/CLIP编码、复制后的prefill/KV/decode和质量校准全部付费。

## actual owner 与 PRE

实际Ch23 592–628固定预算选择与特权标签、1283–1303完整internal late branch→两路logits→fixed hiddenanchor→audio counterfactual交接，Ch22/24入口实际读。现Ch23 hiddenanchor不重新输入图像，固定budget selector删选不同；缺少用gold marginal复制增益训练input scorer、部署保基帧就地增强的接口。sole `MULTIMODAL-REPRESENTATION`，不将controller安全、genericKV/runtime重复写成第二owner。拟静态anchor限制之后、音频counterfactual之前原一段，等非准备者Source/owner/PRE通过才写。

隐藏状态不可改时，还可以只强化输入中的视觉线索，而不是延长推理或删除未选帧。一条[受限视频分支](https://arxiv.org/html/2603.16256v1)在训练侧固定模型，比较原输入与单帧就地重复后正确答案的log-prob差额，以这个有答案标签的局部信号学习问题条件化的帧排序；部署保留基帧，只在原位置复制少量高分帧。重复改变的是输入权重与序列位置，不获得新观测，也不把模型confidence或更高attention当作视觉真值；逐帧增益更不保证多帧组合或跨模型仍有相同收益。有限对照中更多重复与无推理模式均有任务反退，选择、重复数量和完整输入必须一起比较，不能照搬一般删帧selector或宣布固定最优K。标签制造、scorer/视觉编码训练及复制后的prefill、KV和生成均付费；质量、时间关系或总预算回归时，保留均匀原输入、更小重复预算、已验删选路径与外部grounding，不让同一模型的概率自签答案正确。<!-- source-family:SF-2026-ARXIV-2603-16256 -->

静态注：`SF-2026-ARXIV-2603-16256` — [FrameRepeat v1](https://arxiv.org/html/2603.16256v1)§3–5/Eqs1–13/Tables1–4、A/Table5及B1–3/Tables6–8。仅gold marginal重复标签→query scorer→保基帧就地增强的输入分支；注意力/概率非真值、多帧非可加/不保证跨模型、重复与no-think反退及完整标签/模型费用保留，未核全图、代码或复现。

未写未POST不计safe/DAY。非准备者核必要原证/实际owner与逐字PRE即可，不要求无差别全部附件或再次扫描来源。

## 非准备者必要独核（resume_mar17，2026-10-11）

重新加载实际AGENTS与本19适用研究/报告合同、统一prompt、ROADMAP、来源说明及本日路由后，独立实际读取exact-v1 HTML §3–5/Eqs1–13/Tables1–4、A/Table5与B1–3/Tables6–8；实际Ch23 592–628及1280–1305完整相关邻接已顺读，Ch22/24交接复用已核上下文。不要求全图、后续附件、代码或复现。训练用gold answer的单帧log-prob差额制造标签，scorer部署才排序复制；VLM与CLIP冻结，未打分U负例是假设。原帧保留、就地copy改变序列而非新观测；单帧marginal不授组合可加/跨模型同序，attention合并original＋copy不授唯一因果或真值。T4更大重复预算多项退、B2 Video-Holmes 41.6→41.5、B1删选混杂和B3 TSPO复用范围均与原证一致，标签/scorer训练/视觉编码及扩展prefill、KV、decode全费保留。

必要Source与sole Ch23具体差额PASS：已有hiddenanchor不重新输入图像、删选减少原输入，均未承载gold marginal标签→query scorer→保基帧就地增强这一接口。原一段PRE仅需消歧“scorer/视觉编码训练”为“scorer训练与视觉编码”，避免误称冻结视觉encoder被更新；root已接纳这一唯一短语修正，其余逐字PRE与静态源注通过。此结论不授Books实际POST、safe或DAY；写后需非writer实际正文、完整邻接与本人源注回读。

### root写后非writer actualPOST

resume_mar17实际顺读Ch23 1287–1310完整局部（新正文1297）与1712–1718尾部自身静态源注/相邻MOCR、Camera、f-CBM注，回对已独核必要Source及唯一短语纠正后的PRE。新增段逐字准确，费用句现为“scorer训练与视觉编码”，没有误称冻结encoder更新；静态hiddenanchor→输入级就地copy→音频counterfactual交接正确，gold-label/概率非真值、多帧组合/跨模型边界、更多重复/no-think反退与完整费用近文，自身注仅保来源、必要范围与边界，未复制验收过程身份。局部actualPOST PASS，可交root接纳并释放本family窄锁；不授本日DAY，不要求再修改Book源注或重读必要原证。
