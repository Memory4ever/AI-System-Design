# 12826 MCQ / IDC 必要原证与逐字 PRE（待独核，未写）

仅本17补03/16自然日；此前完整AB/日期同日夹证/具名去重准入有效复用。resume_mar17必要原证实际读exact-v1 §3–5、Tables1–7、limitations、A/B/C/D.1/F/G、H.1–H.3（HTML prompt空块以PDFp15–16恢复）、J–Q直接反侧。当前官方abs只有v1，未见给出的纠错/撤回信号；不是全网无勘误证明。2+1+2=5，具体数据输入/目标代理差额深入，不降分，不按医学场景假排除模型训练机制。

## 必要 Source

- [exact-v1 HTML](https://arxiv.org/html/2603.12826v1) §3把输出写c,a且reward只按a=o*；错误推理偶然答对概率的mixture为建模假设，λ/n即使强distractor仍存在，不证明“错误logic必错答”或真正reasoning被核验。§4保持题干/正确选项，随机抽2/4/6/8/10；z按每test-count在五train-count间归一，聚合peak不认证逐格单调。Table7 Qwen6test最高4train58.22、8test最高10train53.50；只采用train/test option结构是有用控制，不写普遍exact-match最优或基本定律。
- §5.1/F强度为K8/T.7完整轨迹中该错误选项的频次/全部错误响应数，Nerr=0则0；不是错误推理标注，也不是无条件难度。Table2自选strong局部好于random，crossDS在两模型都低于random；Table1扩选项的Llama仍低于人类原10选项，不签强teacher必要/任意自生成恢复。
- §5.2/Alg1：固定q/o*，先保s>0池；不足N−1生成填充，满则去weak再生成并在候选option set评估，new强度高于旧则替换；历史先max有效数量再min passrate，末尾不足用original填回。强度依赖整个option population，变集合前后比较不是真值固定hardness排序；有限8采样的0不证明永不误选。算法未清晰显示所有存量强度刷新，故不认证完整数值recipe/单调语义压力。只采用数据构造角色与判分职责。
- H.3 PDFp16要求完全同义且任何scope/specificity差异都NOT_EQUIVALENT，不认证所有不同措辞/不同范围的候选均为错误答案；生成与同义judge可能共错。§5.5语义冲突652/35000（222/5000题）只观察识别项，无独立漏检率。Table6 400/200paired response汇总两model、DSV3.1 judge+humanverification，未给人审人数/一致性/逐model/置信区间，仍有限代理，不称没有人工审核；不以低spuriousrate授全部CoT真值。
- A8H200/GRPO+RLOO/128batch与minibatch/8rollouts/lr1e−6/KL.001+entropy.001/maxprompt/response2048/trainT1/testgreedy。B9417 MMLUPro原10选项随机8004/1413；不能当未见题源/污染已排除。§5.3 MedQA训练，四医疗evaluation只是方法条件不作为Science应用主张；O法学1k/85:5:10三run有限泛化。M三seed mean±std不等正式显著性检验；LlamaPubMedQA Orig77.92±.44>IDC77.58±.48。Kcrossestimator Llamaavg52.14>self51.90，N mixed弱于best单strategy；single-round无estimator且一次改全部，不是单独迭代因果消融。
- Table5全7round1.5h/RL18–20h、8H200/10k样本，source为作者局部wallclock；self配置与主实验Qwen32generator分开，F完整CoT与费用节singlelabel分开，完整训练step/epochs、precision、长度实际分布、并发/SLO及每配置全部费用ND。不把<10%当普遍或无代价，不核artifact/复现。

## Actual owner / 具体差额

actualCh27 310–377尤其327–351完整改写监督→Synthetic generator/judge→Seed2Scale；Ch28/29开篇交接已实际读。Ch31/33精确distractor/选择题/12826搜索未有同机制，现33序列trajectory负例不是输入候选集改写；现27检索假文档/策略多样也不是固定正确答案整形option set。唯一TRAIN-DATA：共享原题/正确答案身份不变，主动更换错误选项以改变当前policy的contrast population；RL objective仍由31/33负责，不复制推导。拟接Synthetic标题首段generator/judge后、Seed2Scale前，仅两段。

## 逐字 PRE（待root与非writer通过，未获锁）

合成器还可以保持题干与正确答案不变，只改写模型面对的错误候选集合：原有人工干扰项在含义可靠、难度合适时仍是直接基线，删除所有选项则可能同时改变任务格式。一条受限分支用目标模型的多次回答估计每个干扰项在错误回答中的相对频次，先填充可被误选的候选，再尝试替换较弱项；历史集合按有效项数量及模型通过率选择，不是按更强生成器的名望选择。这个信号依赖 checkpoint、采样配置和整套选项，零频次不证明永不会误选，换集合前后的分数也不自动具有共同难度标尺。题干、gold、选项身份/顺序、generator、scorer、候选历史与实际保留集应一起留在 lineage；它改变的是训练输入的人口与对比压力，不把答案标签升级为逐步推理验证。<!-- source-family:SF-2026-ARXIV-2603-12826 -->

[有限的选项构造对照](https://arxiv.org/html/2603.12826v1)支持把 train/test 的选项数量和干扰项强度分别验收，却不支持所有配置严格匹配最优、强教师必更好或每类任务都受益。完全同义检查只能提出待拒候选，含义有差别也可能仍是合法答案；降低模型通过率可能来自歧义而非更好的推理压力，必须另验 gold 唯一性、正常效用与未参与构造的任务。生成、强度采样、语义审校、重训与回归都计费，局部七轮耗时不能代替所有配置的总预算；选项格式、评分者或语义门失配时，保留可信原始选项、人工/独立核验以及经过验证的开放回答或混合格式配方。<!-- source-family:SF-2026-ARXIV-2603-12826 -->

本人注拟记录exact-v1上述必要位置、2+1+2=5、代理/语义门/费用和负侧，未获Source/PRE非writer正式PASS不写Books，不计safe/DAY。
