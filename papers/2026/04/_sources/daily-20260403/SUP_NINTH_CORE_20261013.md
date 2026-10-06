# 第九批有限余项决定性 core

仅既有完整 v1 题摘集合；实际读必要方法、直接对照及反侧，不扩发现或全部附件。拟分数尚待 root Source 独核，日期未由 Submitted 单独授予，Books 未授锁。

## 00799 局部 3D consistency：拟 2+2+2=6

[v1](https://arxiv.org/html/2604.00799v1) §3.2–3.4/4.1–4.3：静态三视图中用真实另一 pose 的物体替换中间视图，cut/paste/inpaint 并恢复遮挡关系；自动超过 10K、人工过滤剩 6151，每场景 1–2 项。1024×768 下候选通常 >1000 pixels、最多 26，目标须保留时可降至 300；强制字母选择不是开放几何重建。局部跨视角几何一致性和 semantic object identity 分开是拟采用差额，不把最佳约 34% 对人类 84.8% 外推所有 3D 能力失败。self-paste/no-change 控制仍约 19.5/20.7%、Qwen8B 21.3/22%，高于 7.9% chance，作者承认 selection bias；更大 inpaint 窗口提高表现，不能声称 artifact 全排除或提升必由 3D 推理产生。未核图像像素或复现。

## 00829 LinguDistill：拟 2+2+2=6

[v1](https://arxiv.org/html/2604.00829v1) §3.1–3.2/4.1–4.3、Tables7–10：冻结同 LM 架构 SmolLM360M teacher，以其 text queries 逐层读取 nanoVLM student 的 multimodal K/V；teacher 权重冻结不等于独立原语言 teacher 输出，因为 memory 来自 student。按来源选择 KD 权重，OCR 9 来源不蒸馏、语言 8 来源蒸馏，是拟采用 signal eligibility 差额。17 来源 <600K，单图 1024、380M tokens/4000 steps、LR1e−4/bf16/冻结 ViT；uniform α.5/T2 和 selective α.7/T4 不匹配，不能只归因选择器。selective OCR .600 仍低原 .760（高 uniform .452），DocVQA .740<.769、ARCchallenge .318<.322；不是所有语言/视觉知识保留。teacher forward 与训练 activation/memory 额外费用不可由部署时无 teacher 消除。

## 00903 IDDM：拟 2+2+2=6，隐私必要反侧深入

[v1](https://arxiv.org/html/2604.00903v1) §3.3/4.1–4.3/5.1–5.3、Tables4/9/10：威胁是获授权个性化、私照及参数不公开，攻击者拿公开生成图作黑盒 FR 关联；非公开输入扰动防恶意训练、非基础模型删除或隐私证明。temporary reference FT→冻结模型 PGD 私照→在优化私照继续 FT；先 denoising consistency，再由 denoised prediction 的多 FR prototype cosine 做 softmax 加权（较高相似度更重）并最小化，随当前个性化模型刷新，不是原始私照独立 adversarial evasion。每身份 4 reference/4 protected/≥4 clean，CelebA-HQ 与 VGGFace2 各 50 身份、SD2.1 DreamBooth、10 outer×8 PGD、4 surrogate FR 与 3 held-out FR；A100 约20min/identity，推理约1min/batch，不作 DP 或生产延迟保证。ρ 在设定正文 .1 与主表 .3 不一致，不挪作统一 default。主 photo 指标 ISM .69→.43、ADA .66→.38，同时 FID 158→213、BRQ10.65→16.81；FSR .57→.65 不能取消 quality 退步。Table9 stage 与 joint 在 photo FSR/ISM 同 .65/.43、FID213.37 vs220.14，portrait FSR .48 vs .38，是局部 trade-off，不证明 joint 普遍巨大崩溃。Table10 VGGFace2 photo held-out top1 仍97.43%、portrait75.43%，不能把少量下降写无法关联；SimAC 无脸样本引起低 attack 指标与 utility 分母另计。

## 00913 IKEA assembly evaluation：拟 2+2+2=6

[v1](https://arxiv.org/html/2604.00913v1) §3.4/4.2–4.3/5.1、Table5：29 产品（排除7）、98 videos/133 diagrams/132 ClaudeOpus descriptions、1623 tasks、17 open models2–38B+2Gemini visual；51 greedy/bf16/1024token runs，解析成功约94.1%，失败计错。V+T 加描述与 TextOnly 替图改变 input，不是同一跨 depiction 信息预算；后者删除23跨步提示，127/132描述人工核过也非完美 truth。V+T T1−3.1pp/T3−3.2、D2+19.5pp；TextOnly D2+23.6、T1−5.1，支持任务/输入资格不能由 aggregate 一个 winner 决定，不外推所有文本增补有害。113 matched mean-pooled ViT CKA 近零不证明信息不可恢复；attention 只 Qwen3VL8B 局部层，相关变化不是 encoder bottleneck 因果。采用跨 depiction 对齐与 input-policy 评价的具体盲点，不按家具应用 EX，也不把视觉 proxy 升为失明证明。

## 当前具体停点

四项必要 core 已到拟采用结论，停止其余附件；独核未通过不写正式候选/Books。后续仅原集合 00923/00938/01151/01152/01161/01170 的必要 core，加 00199 首公开精准日期隔离；不换日。
