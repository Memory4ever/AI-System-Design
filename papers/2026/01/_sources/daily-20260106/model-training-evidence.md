# Jan06 模型/训练必要证据（四）

本记录的已读段是精确v1原HTML，不使用后继v2/v3结论。原始选段cache保URL/实际checked/truncated状态；formula plain projection可能丢angle bracket或重复math，不凭projection发数学保证，必要公式回到原HTML。下面是单篇停点，非日级验收。

## [Mixed-Language 2601.00364v1](https://arxiv.org/html/2601.00364v1)

实际完整§3/4/5/7，cache core-2601.00364v1-selected.json。新增为真实web-data from-scratch反证：混语documents类别对翻译与理解/检索任务作用不一致；拟3+1+2=6。FineWeb-Edu/FineWeb2每语言60B、en-de/en-es/en-fr，各四配置12×1.35B、34K steps约143Btokens、batch2048/context2048/128GH200，precision/独立重复seed=Not Disclosed。MonoWeb删除双语，parallel/code-switch只加回一类；同训练step但语料唯一量、分类器召回/domain质量可能不同，不能唯一归因token-level alignment。Llama3.3-70B分类与representation cosine诊断不是行为机制因果证据。

Table5 translation22.3→9.8、parallel20.2，部分方向parallel甚至高于完整；XQuAD平均30.4→27.5而MLQA21.7→23.2，不能笼统说所有QA完全无影响。Latin script主要语言/1.35B，不外推低资源/7B。原Ch27 1195–1201只有lexical replacement/mix与词典revision的局部数据分支，非上述真实web parallel/code-switch任务敏感度。root实际必要源/owner窄差异通过后授锁；实际两段1203/1205+首注1217写后root通过，已同步末注，锁释放。评分固定3+1+2=6。

## [Sigmoid Head 2601.00680v1](https://arxiv.org/html/2601.00680v1)

实际§2–5/Limitations，cache core-2601.00680v1-selected.json。新增拟命题收窄为冻结generator、额外sigmoid unembedding、10负样本并避dominant候选的局部QE配方，1+1+2=4；成熟likelihood≠truth/多参考歧义不计原创。dominant heuristic借DinhNiehues2025，并不证明保留者正确；skipnegative只不施该负信号，不自动赋正标签。Tower7B/OLMo1B及62M Transformer/.83B DeltaLM，最后训练阶段数据，不能授pretraining规模。

EvalSelf MT用XCOMET pseudo-gold，EvalOther部分human；QA用Qwen72B judge，可能共源偏好。相对Boosted不全优：Tower en-es/en-ko、BioMQM en-de/en-it等负侧保留。small模型调best sampler和大模型proxysetting配置不同；sigmoid独立score不是softmax生成分布，也不保证真实校准概率。head少量row训练共享hidden不等完整端到端免费；硬件precision/重复seed未采用为事实。身份日期与仅报告具体理由待归档，不能说标准全benchmark复现。

## [ReDGE 2601.00781v1](https://arxiv.org/html/2601.00781v1)

实际§3.2–3.4/4.1/runtime/5及A1必要假设，cache core-2601.00781v1-selected.json。新增factorized categorical一热Gaussian后验denoiser closed-form，而finite DDIM只是approximate differentiable map；exact posterior不等unbiased gradient。1step回到ST/ReinMax，3–5step引入独立f的additive成本；VAE epoch5.16GS/5.2ST与5.8ReDGE/6.64Max，非免费或普遍更快，hardware/precision未披露于必要段。

小t1时Jacobian a.s.消失依赖A1 alpha/sigma²→infinity、固定后继timegrid和A2轨迹存在且不落decision boundary；不是所有schedule保证。原§4线性schedule写alpha=t,sigma=1−t，与§3 alpha1=0及A1时间方向不一致，实际experiment identity需澄清，不采用该schedule照抄。polynomial相同离散顶点可有不同连续extension，ST在作者线性extension上可unbiased；ReinMax quadratic exact不能外推general f。固定2+1+2=5；原Runtime每次gradient estimate single f evaluation，diffusion steps只加f-independent sampler成本，写前纠正‘每step f调用’错误提案。root实际必要源→Ch28 253–274具体gap通过并授权；实际两段263/265+首注1500的root非作者actual POST已通过，锁释放；未作日级完成。

## [DCR 2601.00747v1](https://arxiv.org/html/2601.00747v1)

实际§3.1–3.4/4.1–4.4/5.3/6.1/6.3–6.4/7.1，cache core-2601.00747v1-selected.json。有限trace-simplex、bounded utility、PSD similarity kernel、interior entropy barrier下的Shahshahani flow，不等神经网络SGD收敛。新命题以R(correct)双侧gate的kernel-energy区分语义冗余与tokenentropy，拟2+1+2=5；熵奖励/偏好collapse本身不是原创分。

toy scalar流不同STaR/GRPO/DPO score假设才给对应drift/equalization，不代表每个现实algorithm/parametric optimizer；作者scope note明确非所有scalar objectives。模型/硬件/precision/benchmark不适用本理论，原§7是testable predictions，没有受控LLM训练实测。O(B²) pair kernel与verifier质量/语义kernel才是资源边界，不能说‘manageable’就是生产成本。parametric realization/实际SGD近似的必要条件尚未核，若拟采用这层保证仍普通工作；现Ch33语义正确解法多样性局部需比较，不从主题对应直接判已有覆盖。

## 最终处置同步（2026-10-02，日级Gate待root）

当前最终处置：MixedLanguage固定3+1+2=6实际Ch27 POST通过；Sigmoid4局部recipe关闭，仅报告身份/date已归档；ReDGE5缺口深入与Ch28 actual POST通过；DCR5有限理论标准仅报告，未采用parametric SGD-realization保证，不要求为该未采用保证继续附件审阅。root必要命题复核通过。
