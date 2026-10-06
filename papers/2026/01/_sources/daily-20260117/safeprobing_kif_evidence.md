# SafeProbing / KIF — 必要原源与当前owner待root核

均 exact-v1 官方 HTML；原缓存 `2601.10543v1-primary.txt` / `2601.10566v1-primary.txt`。未核代码、复现或生产实施，正常Submitted/正常公告条件与registered上界见本目录date字段，不能把Submitted作public。

## 10543 SafeProbing — 拟2+2+2=6，安全接口gap必要深入，拟Ch72两短段

实际§3.2–3.4 L90–121：给当前prefix虚拟追加固定disclaimer，只计算core phrase条件NLL；它是suffix likelihood sensor，不证明内在安全意识或有害性因果。训练读完整disclaimer，`2/(1+exp(beta*loss))`对二值完整response标签作MSE（不是BCE），另SFT retention λ=.05；推理读core。Base M生成、LoRA M′判分分责；随机抽20%step，任何sample loss<tau就halt/fixedrefusal。没有披露对已生成prefix的pre-delivery buffer，不授atomic安全gate/撤回已发送内容，随机未抽位置不能视作安全。

实际§4.1 L336–344、Table3 L568–607、Table4 L607–646及§4.4/Limitations L684–699：Qwen2.5-7B/Mistral7Bv.3、AdvBench520/七攻击与HExPHI，LlamaGuard3-8B是grader非真值。Qwen未训tau1/2/2.5的平均DSR69.5/87.4/93.1与overrefusal2/17/51对照揭阈值取舍，trained亦11%overrefusal/非zero失败。Table4 ratio .05部分DSR低于.2；不能用所有checkpoint最小loss的比较掩盖采样数差异。GSM8K/JustEval800局部效用仍退，base generation保持不等于最终return utility保持。

实际A3 L1259–1283训练1000样本（600 SafeRLHF+200 benign+100 harmless refusal+100retention），validation同构；LoRA r8/alpha32/qkvo、B16/2epoch/LR5e−5/len256、RTXA6000；precision/seed/servingbatchconcurrency ND。B4/Table9 L1339–1377：main ratio .2额外2.58s/1.48× slowdown，.05 .64s/1.12×，不是negligible/免费；JustEval/Qwen局部成本不泛化。B3只原VLM disclaimer分布分离，没有训练跨模态迁移或部署gate证明，不拟采用。

当前 `PLATFORM-SECURITY` Ch72 L845–857实际拥有activation risk→semantic judge级联、完整response弱标签≠prefix标签、later flag追回不了已发送prefix与independentoutput/actiongate，但没有reserved suffix conditional likelihood的另一sensor接口、M生成/M′probe和full-disclaimer训练/core推理身份。拟此节两短段仅这些差额，不补内在意识/校准伤害概率、KV复用/zerooverhead/全人口保证；阈值与采样漏检/拒答成本、实际buffer/effectgate与外部固定频率退路近正文。需root必要源/owner核后窄锁。

## 10566 KIF — 拟2+1+2=5，安全/擦除反证必要深入，拟具体已有覆盖

实际§3.1–3.4 L94–132、Eq3–5 L193–202：subject prompts的gate/up/down平均activation对比Gaussian synthetic negatives，标准化/50bootstrap/residualPCA形成direction，再挂rank1 capsule `(I+alpha ddT)h`，alpha初−1；这不认证conceptspecific因果axis或真实offtopic人口。Capsule输出构造拒答y+与base factual y−，composite DPO+factualUL+name-tokenUL+KL+EWC训练globalLoRA，Eq4只压拒答response中subject-name token总概率；不授parameter erasure/一般utility不变。

实际§4.1–4.3 L203–223/305–346：SMR是输出mention%，EL10被定义为early-step target-name probability mass（ratio normalization未明确），并非独立activation可恢复性探针。Qwen8B SMR3.33/EL10 11.03只提供nonmention与所定义输出概率信号分离的局部反侧；不能叫内部知识仍存的因果证明，更不能从低EL10授true erasure。Table4标签与作者threshold自相冲突：NoNT SMR3.33≤5/EL10 .275<1仍TypeIII，NoGenEL10 .098<1却TypeII；不采用regime结论或“架构Ucurve证明”/容量因果。不同model families/config未控制，单run/4bit/≤14B/一A6000，不授普遍reasoning架构规律。

实际A1 L774–814：5824prompts/604triples/11subjects，类别/subject失衡；Lim L346–352明示Gaussian negatives与真实负人口差别、single-run/fullprecision未验、只immediate未测jailbreak/后续finetune恢复，Ethics也承认无不可恢复保证。近oracleTOFU proxy分数不证明重训等价；未采用相关headline/碳排降幅。

当前 `PLATFORM-SECURITY` Ch72实际L2593–2599已承载拒答与表示/行为不可恢复性分账、有限命中/局部certificate不授parameter erasure/完整语义删除、unverified及重训退路。这是本材料可安全采用的长期命题；KIF特定signature/capsule/LoRA配方尚未证明新的概念擦除机制或恢复安全边界，拟5分必要安全深入后Existing，不冒已有本实验/EL10证书。root需实际核上述counter与具体owner终裁；若要求新增知识应先指明未承载的可支持命题，不能借成熟erasure边界给高分。
