# 必要证据与 owner 差额：P-ALIGN / M2M

exact-v1 HTML，未运行代码或复现实验；root 已完整题摘准入，必要证据待非作者核。

## P-ALIGN — 2601.10064v1

[原文](https://arxiv.org/html/2601.10064v1)，本目录 primary 实际 §3.1–3.2 L100–147、§4 L271–285、§5.1–5.4/Limitations L459–497、A.2 L797–842。2+2+2=6；长期监督接口 gap 深入，不借 binary search 或普通 SFT 单独升分。

完整 teacher 长轨迹可能超出 student 可用推理容量；原机制以句为单位，student 给 ENOUGH/NOT_ENOUGH 判断并二分找短 prefix，再由同 student 在 prefix 条件下补全，最终答案匹配 gold 才保留 prefix⊕continuation 做 CE。不是仅截断 teacher、不是 loss mask，也不删掉 prefix 条件。答案过滤不验证每步正确，self-judge 不是 sufficiency 真值。二分依赖可用的单调判断；正文未建立所有 prefix 的实际单调性，故不授最短 sufficient prefix 证书。

DeepSeek-R1 teacher/s1K-1.1 1000 条，Qwen2.5-7B/Qwen3-8B student，LoRA 3 epochs/LR5e-5；Math500=500、AIME24/25 各30、AMC=83（正文 AMC12 /表3 AMC23 命名不一致，保留原身份不补造）。Pass1/Pass3 分开。teacher-prefix-only/student-CoT-only 与不同截断对照支持组合接口，fixed-ratio 越长在 AIME 有益、Math500 反退；无 binary search 的准确率相近，搜索时延是 preprocessing 不是最终 serving speed。未采用20x headline，硬件、全部 teacher/judge/search token 与 CI Not Disclosed；训练长度减少不证明总训练费用降低。小 student self-judge 可能失真是作者限制，GLM4.5偏好不是过程真值。准备/筛选成本与已丢弃人口需保存；判断不稳回退完整 verified CoT 或固定可核 prefix。

Ch29 TRAIN-SFT actual234–258现有 density/短 latent supervision/teacher交集与配对协议，不承载 student binary sufficiency→自身 completion→answer filtering 的数据合成接口；130–134 loss-mask 保留全部历史也不等价此构造。拟 distillation 小节在教师配对协议后两短段，不占 Ch30 LoRA objective。首尾及 Ch28/30 交接已读。日期原 Submitted Jan15 04:40:45Z，Updated Jan16 01:20:35Z，created/registered02:46:19Z；正常 cohort 公告/无已知先行全文条件 BJT[Jan16 09:00,10:46:20)。

## M2M — 2601.10096v1

[原文](https://arxiv.org/html/2601.10096v1)，primary 实际 §3–4 L79–114/153–174、§5 setup/results L608–624、§6–7与limits L652–720。2+2+2=6，只计 English-anchor 条件迁移与 retrieval/generation 目标边界，不把成熟线性 map/更广 languages 本身升分。

冻结 English multimodal text/image(or audio) encoders 与 multilingual text encoder，仅用语义接近 downstream 的 English captions 学 F: multilingual embedding→原 English text latent；保持原 image/audio 分支与其既有 alignment。retrieval 使用归一 MSE+batch cosine结构项，generation用未归一 MSE并撤结构项。不同语言的迁移依赖 multilingual encoder 已有语言能力及其与 English 的几何对应；并非未预训练语言零数据学习，不是任意 token-level替换。原§3明确几层 linear、§4最优两层无 skip约1M参数，不能称万能 nonlinear projector。

主要 JinaCLIPv1×M-MPNET，GCC/COCO/VizWiz去重 captions，250K/50epochs/B64/AdamW3e-4，两RTXA5000 24GB，XTD English validation选模。XTD11语、XM3600 36语、Multi30K4语Recall10；XM3600较SOTA gap更大，不泛化唯一retrieval-space原因。audio的33语是机器翻译synthetic测试，英语CLAP仍优于对齐multilingual文本，caption域失配限制。FLUX12B CLS替换保留generic T5prompt，512²/guidance3.5/10step/fixedseed；FID差及缺对象支持sentence-level代替不了token-conditioning，IS较高不认证faithfulness。结构loss对generation退步为直接反侧，不复制 Ch24 flow机制。准备成本、encoder人口/数据身份与人工检查翻译误差仍需要；gap无法接受时回退原 English encoder、translation或真实multilingual-multimodal训练。

Ch23 MULTIMODAL-REPRESENTATION actual50–66 stage2现讲raw-feature→LMprojector瓶颈，native段强调staged共存；未承载只在两套 text latent 用共同 English 锚把已有多语能力转接原冻结modal encoder，以及normalized retrieval与unnormalized generation的不同要求。拟stage2接口段后两短段，不把 Ch24 generative conditioning全写此处。Ch23首尾与22/24交接已读。v1 Submitted Jan15 05:56:37Z/Updated Jan16 01:22:46Z、created02:47:05Z/registered02:47:06Z；条件 BJT[Jan16 09:00,10:47:07)。当前 DataCite v2 Jan20提交/Jan22Updated 不能替代 exact-v1。
