# I13–I20 完整窄稿

只申请以下完整单段、各独立marker与本人末注；完整直接两侧见context3。全部复用本日已通过的受限Evidence，不重新Methods，不预签SAVE/POST。

## I13 MODEL-SAMPLING / Confidence-gated CoT

文件：`books/part-02-model/20-sampling.md`；Test-time Budget节前。

```markdown
预算决策还可以放在长推理之前：先生成直接答案，再由评分器估计当前答案是否需要升级到CoT；这与在一条已开始的轨迹中提前停止不同。[Confidence-gated CoT的受限对照](https://arxiv.org/html/2510.21007v1#S3)把直接答、评分和升级后重答分成三个调用，阈值依验证人口与模型校准，不能把口述confidence当正确概率。局部质量/平均token取舍不保证尾延迟、最坏预算或换域后相同漏放率；不升级的错误也须单独计入。完整账包括首次直接生成、评分、被升级样本的完整推理及独立校准，而非只算最后留下的答案。分数、人口或预算失配时，保固定受控预算、可信verifier或明确拒答，不由较少CoT调用批准答案正确或省掉评分成本。

<!-- source-family:SF-2025-ARXIV-2510-21007 -->
```

```markdown
- `SF-2025-ARXIV-2510-21007`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R14受限Evidence通过。仅前置升级选择与轨迹内停止分责，保校准人口、漏放、三调用全费；未核实现/复现，PRE/SAVE/全自读/solePOST据本日实际层。
```

## I14 MODEL-SAMPLING / Shortest-answer selection

文件：`books/part-02-model/20-sampling.md`；Coverage/Selection完整段后、prefix选择段前。

```markdown
缺少可投票的规范答案时，selector还可用候选长度作廉价代理，而不另训judge。[Shortest-answer selection的受限实验](https://arxiv.org/html/2510.21067v1#S3)在代码等任务比较先生成多答再取最短，支持长度与部分错误模式的局部关联，不证明短答更真或所有任务单调受益；代码仍须执行测试，长度也依tokenizer、格式和截断规则。全部候选已经生成，最终输出短不能抹去其余生成费；只有实际并发、生成速率与终止契约满足时，先完成即可停止其他分支的运行策略才可能减少等待，不能从离线最短选择自动继承。长度/质量关联消失、正确候选被截断或测试不充分时，保原selector、完整候选预算与独立任务verifier，不由低长度代替正确性判断。

<!-- source-family:SF-2025-ARXIV-2510-21067 -->
```

```markdown
- `SF-2025-ARXIV-2510-21067`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R14通过。仅无规范投票答案时的长度代理与全部候选费用，非短即真或实测净延迟；未核实现/复现，完整PRE/SAVE/自读/solePOST按本日实际层。
```

## I15 TRAIN-PRETRAINING / ZO-FC

文件：`books/part-04-training-system/28-pretraining.md`；零阶成本段后、全参数群体扰动前。

```markdown
零阶与一阶也不必按整模型二选一：对冻结主干上的低秩adapter用有限差分，把易保留梯度的分类head交给一阶更新，分别承担低内存适配与分类边界可塑性。[ZO-FC的受限分支](https://arxiv.org/html/2510.21019v1#S3)因此改变的是参数角色和梯度路径，而非证明零阶普遍找到更平坦或更能泛化的解；分类实验也不自动覆盖生成式LLM全参数训练或端侧部署。应绑定两组参数、更新顺序、扰动尺度、forward次数与head激活/梯度状态，不能把无主干backward当整条训练零梯度内存。有限差分噪声、head过拟合或总费用不合时，保原一阶adapter、固定head或纯零阶基线，并在相同数据/预算下验收，而不由两种优化器混用签发普遍优势。

<!-- source-family:SF-2025-ARXIV-2510-21019 -->
```

```markdown
- `SF-2025-ARXIV-2510-21019`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R14通过。仅adapter/head梯度分工，不采用平坦极小值普遍保证、全LLM/端侧结论；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I16 AGENT-RAG / UDCG

文件：`books/part-07-agent/76-rag.md`；逐层归因段后、citation eligibility前。

```markdown
同一passage对检索器相关，不等它对当前reader有正效用：它可能提供答案，也可能以冲突或冗余信息干扰生成。一个[reader-specific context分支](https://arxiv.org/html/2510.21440v1#S4)分别估计正向帮助与负向干扰，再选择context，而不是把IR标签直接当生成收益。其从logit/非拒答估效用依赖“相关context只会答对或abstain”等强假设；非拒答实际可能答错，单段有用也不保证组合后仍有用。Reader版本、问题人口、context顺序/组合及拒答口径须一起绑定，先检索再评分/过滤和最终生成、独立正确性标注均计费。效用代理或组合稳定性未验时，保可信相关性排序、受控context预算、原文回读与独立答案核验，不由更高效用分批准事实正确或检索已无遗漏。

<!-- source-family:SF-2025-ARXIV-2510-21440 -->
```

```markdown
- `SF-2025-ARXIV-2510-21440`：Daily2025-10-28补Oct27；exact-v1必要层、2+2+2=6，R20通过。仅reader效用/干扰与IR相关性分责，保非拒答强假设、组合交互和全费；未核实现/复现，PRE/SAVE/全自读/solePOST据本日实际层。
```

## I17 AGENT-MULTI-AGENT / Co-Sight

文件：`books/part-07-agent/82-multi-agent.md`；DebateQD完整段后、RepPop前。

```markdown
审计预算也可随分歧而分配，而不让第二个Agent无差别重跑整份轨迹：先独立生成并比较，对冲突的局部步骤触发工具核查，再把受限核查结果作为后续共享锚点。[Co-Sight的受限协议](https://arxiv.org/html/2510.21557v1#S3)减少的是后续audit范围，不是免去前置完整生成、工具与比较。相同base的温度差异不提供独立事实，双方一致的共同错误还可能完全不触发审计；协议称为verified anchor也不使工具输出、定位或解释自动为真。须保留冲突定位、原始证据与采用范围，并另抽查一致区及最终任务正确性。全部前置/失败/重审费用纳入相同预算；分歧检测或工具权限失配时，保单Agent可信证据、受控全审或人工核验，不由较少冲突批准整条轨迹可靠。

<!-- source-family:SF-2025-ARXIV-2510-21557 -->
```

```markdown
- `SF-2025-ARXIV-2510-21557`：Daily2025-10-28补Oct27；exact-v1必要层、2+2+2=6，R20通过。仅冲突定点审计/一致区盲点/前置全费，非truth锚点或独立性保证；未核实现/复现，PRE/SAVE/全自读/solePOST据本日实际层。
```

## I18 MULTIMODAL-EMBODIED-VLA / Human-hand pretraining

文件：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`；VITA-VLA完整段后、混合视频目标前。

```markdown
从人类视频取得动作监督时，还要先决定一条训练样本在哪里开始、结束：恢复camera/world中的手部轨迹，按速度低点分成短原子动作，再配轨迹条件的语言描述；固定窗口padding须在loss里保留有效步身份。[人手预训练的受限路径](https://arxiv.org/html/2510.21571v1#S3)把时序切分/坐标与语义标签纳入接口，而不是把人手坐标直接当robot command。三维重建和MLLM描述都可能错，仍需机器人teleop对齐与微调；短动作证据不授权长任务、双手或未见本体。视频重建、分段/标注、全部预训及机器人数据和闭环回归均付费，自动取得标签不等零监督。坐标、有效长度、动作语义或本体映射失配时，保真实机器人示教、明确mask/retargeting与独立controller，不由更多人类视频批准可执行动作或物理安全。

<!-- source-family:SF-2025-ARXIV-2510-21571 -->
```

```markdown
- `SF-2025-ARXIV-2510-21571`：Daily2025-10-28补Oct27；exact-v1必要层、2+2+2=6，R20通过。仅atomic segmentation/轨迹caption/padding/本体映射，保重建误差和teleop微调全费；未核实现/复现，PRE/SAVE/完整自读/solePOST据本日实际层。
```

## I19 TRAIN-GRPO / Chunk-GRPO

文件：`books/part-04-training-system/33-grpo.md`；trajectory-balance段后、连续flow噪声搜索前。

```markdown
去噪轨迹上的更新单位还可从单步换成固定chunk：汇总一组step的log-ratio，以几何平均ratio进入clipping，再共享终局advantage。[Chunk-GRPO的受限分支](https://arxiv.org/html/2510.21583v1#S4)改变的是更新尺度与clipping资格，不是还原每一步的因果贡献，也不是原完整path的importance ratio；边界、无随机末步的处理、step概率与归一必须共同声明。Weighted sampling的部分质量反退也说明更高训练reward不能代替独立生成质量。全部轨迹、概率/参考求值与训练费仍保留，较少计算step loss不等相同比例端到端节省。Chunk边界、方差或质量失配时，保已验step/outcome更新、完整轨迹记录与独立终态评价，不由共享advantage批准无偏credit或普遍稳定训练。

<!-- source-family:SF-2025-ARXIV-2510-21583 -->
```

```markdown
- `SF-2025-ARXIV-2510-21583`：Daily2025-10-28补Oct27；exact-v1 Chunk-GRPO而非current改名，2+2+2=6，R20通过。仅chunk ratio/clipping与terminal credit分责，保weighted sampling反侧/全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I20 MULTIMODAL-REPRESENTATION / Modest-Align

文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`；modality gap段后、表示域尺度段前。

```markdown
配对监督也不必把每个positive都当同样可靠：按当前跨模态相似度识别弱pair，对其表示加扰动并软化目标，而不是只把两群centroid拉近。[Modest-Align的受限组合](https://arxiv.org/html/2510.21606v1#S3)承认pair可靠性与对齐强度不同，却不能由模型自己的低相似度判定标签必错；hard但正确的pair也可能被削弱。Gaussian扰动下的一阶Taylor展开不足直接推出普遍梯度平方正则保证，不把印刷等式当稳定性定理。Frozen encoder的原预训、adapter训练、pair选择/扰动和独立任务评价均付费；弱pair阈值、人口或实际质量失配时，保可信cleanpair、原对比目标与分层回归，不由较软目标签发语义真值或普遍鲁棒对齐。

<!-- source-family:SF-2025-ARXIV-2510-21606 -->
```

```markdown
- `SF-2025-ARXIV-2510-21606`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R20通过。仅弱pair扰动/软标签与真实可靠性分责，不采未闭Taylor等式保证；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## 作者整体自读

八段全文/独立marker/本人注与context3完整直接两侧已逐一自读。各自的实际长期差额不同，不以一般控制/状态语言替代。I1–I12有效POST复用；本批未获PRE不写Books，仍非DAY。
