# Nov20 SAM3必要Source与owner提案

## 1. 机构事件与精确证据分责

作者Noether；本日补Nov19 BJT。Ohm§3已实际核[Meta publication](https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/)Nov19机构事件与完整AB；root已读回，不重该日门。原AB明确presence head分开recognition/localization，支持此机制已在机构披露，不授论文最早公开。当前原blog同URL已有SAM3.1/2026更新，不采用晚版multiplexing/帧率或未来正文。

原Meta下载PDF链接本轮web cache miss；随后该精确URL一次native有限GET，40秒只得542163/17808650bytes后timeout28，是partial非完整PDF，未把它作完整正文。必要原论文身份经官方arXiv恢复为[2511.16719v1](https://arxiv.org/html/2511.16719v1)，原字段20Nov2025；它是Nov19机构已披露机制的后发精确补证，**不称v1正文在Nov19首次公开、同bytes或全部recipe当日已披露**。如该补证角色不能支持拟采用关系，应只保原机构受限命题，不改原日期。

## 2. 实际必要阅读与拟采用命题

本轮实际读精确v1§3 L200–209：原DETR/PE共同backbone下，全局presence token预测概念在整图存在，object query预测存在条件下的局部匹配，推理分数取两者乘积。不是presence获得事实真值，也不是条件概率已校准的证明。

实际A.1 L436–451及C.2必要L617–620：presence的BCE按PCS存在/不存在训练；逐object分类只在概念存在时监督，负图不再把每个query都当负分类；存在时仍按Hungarian matching给局部监督。总分乘积共同监督是不同配置，不能把“分开训练”当数学必优；Table9(c)cgF1略高于(a)，代价为联合校准较不便于已知存在的condition。作者未读全部训练recipe，不写权重/超参为可复现配方。

拟保留的长期命题：概念存在性与区域条件定位是不同读出/监督人口，不能从一个漂亮mask推出该概念确实存在，也不能由presence高分批准定位准确；训练的监督条件与推理评分合成需分别声明。

## 3. 必要对照与直接反侧

实际§5 L255–269：SA-Co/HQ/SYN/EXT训练来源不同；Gold为三人标注，Silver单人，Bronze/Bio部分由boxes派生mask；Gold ambiguity评价选对预测最有利的标注，不冒独立唯一mask真值。固定confidence>0.5的pmF1只在positive media-phrase上验mask，IL_MCC验image-level存在，cgF1=100*pmF1*IL_MCC是合成量，不是已校准安全概率。

实际Selected Ablations L372–407：presence的短训练消融中cgF1与IL_MCC改善，pmF1由65.4降到63.4；正文明确各表不同训练run、不能跨表直接比较。因此采用存在/定位分验的反侧，不照录“2×”或宣传为每项质量同时更好，不把联合训练差额唯一归因head。A.1四种监督配置进一步限定分数乘积与训练loss的关系。

实际AppendixB L578–586：细粒度OOD/thermal泛化、简单noun phrase长度、按对象masklet增加成本、缺共享对象级上下文，以及concept/instance hard-mode switch均是限制。原mask/PVS仍是合理分支，复杂语言可交外部MLLM，但本项不采用该agent所有实验或其新家族。未核所有实验、图、代码/制品、实现或复现。

## 4. 评分与实际owner差额

拟2+1+2=5：新增具体global presence/conditional localization读出及监督人口，影响限定跨模态概念-区域接口，长期价值是两类错误/评价分责；不为整个SAM能力或机构加分。若真实owner缺口获核，深入受影响A.1/反侧已实际完成，不靠5分免掉。

唯一owner拟`MULTIMODAL-REPRESENTATION` Ch23。已加载Books治理，实际读当前Ch23开篇、对齐完整896–914及950–983局部完整目标/PE-AV/Omni-NegCLIP/InfoNCE邻接。既有Omni-NegCLIP区分present/absent事实前提如何形成图文正负pair，强调遮挡/未标注不等不存在；尚未承载同一个概念提示的global存在读出与逐region条件定位如何分开监督、乘积合成及分类改善定位可反退。不是以缺SAM名字造缺口，也不替换已有否定事实、hard-negative或局部监督分支。

拟最小位置为Omni-NegCLIP两完整段及其原marker之后、现“即使总目标不变，负例之间也在竞争梯度”之前；新增单自然段解释这项表示/读出分责，具体annotation协议仍归Ch27、task级证据规则仍归Ch66，不另建owner。不请求写锁，先供Ohm实际Source/owner核，准备好才另给逐字PRE。

## 5. 费用、采用禁界与退路

训练数据/负图存在标注、额外global head/后训练、逐region读出及标注仲裁均计费，不称低成本/已核硬件收益；GPU/precision/batch/concurrency/SLO对本段机制没有可迁移保证，不采原runtime倍数。图级分类可错，遮挡/OOD/复杂prompt与不同阈值仍需独立验存在/定位；概念条件不稳时保留已知目标的PVS、真实标注与独立存在检查，而非让模型score批准事实或下游行动。模型仍不能从分割自动授主体身份、世界状态或控制安全。

## 6. 交即时必要独核

请root转Ohm核原机构事件/后v1补证权限、必要机制/评价/直接反侧、5分及唯一Ch23具体差额；不等所有Source或新arXiv，不重S2ST。当前仅作者Source/owner提案，未通过本项独核、逐字PRE/root窄锁、真实写入/POST，更未本日日级DAY/FINAL。S2ST本人注行政差额现已root读回闭合，所有本轮锁已释放，95/132不变。原README唯一row/window/连续§4保留。
