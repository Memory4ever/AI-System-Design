# 2026-02-12：原 45 候选剩余 17 项必要源独立复核

## 范围与结论

非作者复核，仅检查分派的 17 项精确 v1 机制、评价及直接反侧；没有重读另 28 项，没有扩窗、扩来源队列或检查全部附录。HTML 行号为本次原源读取定位，章节、公式和表格号是稳定回查入口。2602.09849 使用已取得的精确 v1 PDF 文本。

17/17 的必要源独立读取完成。作者当前的**限缩证据命题**可成立，不授论文全部宣传、理论或因果解释通过。下面仍列出必须保留的反侧。2602.09934 原先将联合训练学习率、epoch 记为 ND 的错误已经由作者更正，本复核实际读取当前 `V3_EVIDENCE_AND_BOOKS.md` 第 304 行确认，不再留作未解阻塞。

本文件**不是日级 Gate、身份/落窗复核、评分复核或 Books POST**。所有 17 项的 Books 处置仍需由 root 定点比较 ROADMAP owner 的实际句子后闭合；方法名未出现不自动构成知识缺口，必要源通过也不自动授已有覆盖、整合或仅报告。未修改作者报告、Books、索引、LEARNING_STATE 或公共合同。

## 逐项必要证据

| 精确 v1 | 机制与评价实际定位 | 直接反侧与采用边界 |
| --- | --- | --- |
| [2602.09517](https://arxiv.org/html/2602.09517v1) | §4.2，HTML L211–229：dual-view reverse stack 与 causal mask；§6.1–6.2，L275–303：Repeat/StackOnly 有限消融。 | Table 1 的 Hotpot 4B 中 RAG 48.6 高于 SAKE 47.1。采用读取顺序和显式结构的局部接口，不采用普遍优于 RAG、attention 是唯一原因或免费额外推理。 |
| [2602.09825](https://arxiv.org/html/2602.09825v1) | §3.5，L188–229：KSS 按 token 选择 positive/negative 层并截取 top-20；Table 4，L255–264：组件消融。 | Qwen 去 CHSS 的 Ci 7.0 低于完整 7.6；Intern 去 CTSS 的 Cs 30.2 低于 30.4，组件收益有条件。采用可核的逐 token 层选择，不授稳定度等于真值、每组件每维获益或无成本。 |
| [2602.09849](https://arxiv.org/pdf/2602.09849v1) | PDF p5–7：初始图像 KV 条件与动作生成分离，不是多步动作 KV；p10–11，Table 4：各 10K training steps、图像 50/动作 10 denoise、A800、20 次运行的局部时延。 | p10 planning 质量不等真实 success；p18–19 数据计数存在冲突，不统一为确定训练人口。只采用初始 visual context 复用与局部时延，不授长期闭环成功、真实物理可达性或所有成本下降。 |
| [2602.09856](https://arxiv.org/html/2602.09856v1) | §3.2，L131–157：HTML render 加双 reward；§5.2，L253–259：离线单步与在线 task 分开；Table 3，L269–273。 | visual-only 的视觉项改善而 Sid 79.12→78.85。采用可渲染视觉监督与语义奖励的分账，不将离线单步质量当在线完成率，judge 不是环境 transition oracle。 |
| [2602.09878](https://arxiv.org/html/2602.09878v1) | §4.4，L149–159：固定生成 future→trajectory latent→TCN→residual；L228：100 次 backprop；Table 3，L233–236：相对 Action Head 的局部 .1/.5 改善。 | H/I，L408–415：接触、方向、时延与 calibration 限制。采用动作残差纠正接口，不授逆问题唯一性、实时安全或额外优化免费。 |
| [2602.09883](https://arxiv.org/html/2602.09883v1) | §3.2，L123–136：layer×time 平均 bit 与有限 beam；§3.3，L185–197：weighted Hessian；Table 3，L211–216。 | Color Attribute 的 full .290 低于 Fisher .4191。§4.4 L245–246 的 80%×3+10%×4+10%×8 算术为 3.6，不是 3.1。采用有限搜索的局部量化分配，不授 global optimum、真实预算最优或据错误 bit 平均推导 5.16× 算力收益。 |
| [2602.09902](https://arxiv.org/html/2602.09902v1) | §3，L84–117：模型假设及闭式式子；§6，L254–258：小 P 的 existence 结论。 | 结果限定 stationary、iid、单用户订阅抽象。附录 L431 的 alpha(0) 写成 U(s,1) 有符号问题，不照录整条阈值证明或真实生产 throttling 结论。窄 existence 命题可直接支持，不因未采普遍理论一概关闭。 |
| [2602.09924](https://arxiv.org/html/2602.09924v1) | §3.1–3.3，L131–161：policy 标签与 correctness 分开；Table 2，L195–205：不同 complexity 的 AUROC。 | math low→high 下降但 code 非单调；Table 8，L425–438 的成本与 prose 存冲突。采用 policy sensor 的局部边界，不授校准失败概率、成本节省或 information lost 是唯一原因。 |
| [2602.09934](https://arxiv.org/html/2602.09934v1) | §4.3，L139–143：不同 task 的 gradient 累计后共享更新；§5.1，L179–180：caption alignment 和 joint 两阶段参数；Table 4，L187–192。 | VQA 64.8→66.1，而 dense .541→.557/33.6→32.0。head 独立不隔离共享 backbone 梯度。caption alignment 为 128 H20/batch1024/lr1e-3/1epoch；joint encoder/projector/text decoder lr1e-5、其他 1e-4、再 1epoch；不推定 joint 也用 128 H20。当前作者证据已修正。 |
| [2602.10004](https://arxiv.org/html/2602.10004v1) | §4.2–4.3，L160–192：学习 stop proposal 与 external classifier 分开，gold 仅训练监督；A.1，L345–374：future-tail expectation、local curvature 条件；Table 2，L253–258。 | JAMA 56.1 低于 FT 57.2；AIME 3788 token 高于 Lite 3045。A.5 L481–489 有 quality/coverage 取舍。只采用局部 stop sensor，不授 pathwise、任意 distribution 的质量证书或 universal compute saving。 |
| [2602.10021](https://arxiv.org/html/2602.10021v1) | §3.1，L119–124：bucket 绑定输入 length 上界；§3.2–3.3，L134–168：query latent、冻结 reconstruction decoder、QA 阶段再更新 reasoner。 | bucket 不是已测 query information 的自适应实际预算。Table 2 多项 vanilla 更好；L438–445 的 KL 只是 diagnostic。采用内容选择与输出数量分账，不授真实事实清洗、faithful specialization 或跨 chunk 关系已被联合编码。 |
| [2602.10044](https://arxiv.org/html/2602.10044v1) | §4.2，L174–178：advantage 同时更新 transition logprob 和 entropy，不只 actor；§6，L277–279：tabular 理论与 neural gradient 的差别；Table 1，L242–245。 | 138 对 115 分钟约多 20%，不是无开销；附录 Table 3，L398 的 Freeway mean 6.38，而 IQM/median 为 0。采用明示 model/policy 更新权限，不把 tabular 保证移植到 neural 实验或聚合均值当稳定改善。 |
| [2602.10097](https://arxiv.org/html/2602.10097v1) | §3，L85–174：body-gradient 的 step 分解、总 SDI 与 body TracIn 守恒、TensorSketch；§4，L182–185：135.1M、τ32、seq128、FP32、48GB A6000，batch4→40，m2048；SDI/TracIn 相对误差 .0388/.0220（10 sketch trials）。 | 2.55s/checkpoint 对照为 inference-only forward，不等全部 BPTT/训练额外开销；1,000× sketch 压缩不是整机内存比例。§5 L238–244 明示 adaptive optimizer 的 gradient-similarity、truncated-BPTT graph artifact、reweight/remove 因果及 dense train×test 限制。不授数据删除 authority。 |
| [2602.10098](https://arxiv.org/html/2602.10098v1) | §3.1–3.3，L98–155：初始 view+language→latent，冻结 V-JEPA2 future-state target、teacher-forced WM、action token→FM action head。Table 4，L243–251：future horizon 4/8/16 平均 94.8/96.1/95.5。 | Table 2 L205–206 去 human video 的 Simpler 平均相等且 Google 个别更好；Table 3 noise/camera 低于个别对照；§4.4 L217–223 real OOD 不如 π0.5。采用监督与推理输入、teacher forcing 与 action 消费分界，不授人视频普遍控制知识、唯一防泄露原因或可达性/安全。 |
| [2602.10099](https://arxiv.org/html/2602.10099v1) | §3.2/Algorithms 1–2，L140–236：unit sphere、SLERP、tangent projection、exponential-map sampling 与 output radius；§3.3 L237–244：作者 sinc² weighting；§4.3 L268–270：同 80epoch 路径反侧。 | RFM7.06→RJF6.77 是局部 .29；§5.1–5.3 L276–292：widthscaled 仍有改善，decoder radius27.7 的 FID7.79 差于 radius45 的6.77。不能排除 capacity、称所有语义仅角度或任意切向误差都受单一 Jacobi 标量保证。Alg2 的 time grid/x_in 未闭合，不照录执行 recipe。 |
| [2602.10104](https://arxiv.org/html/2602.10104v1) | §3.1，L124–147：latent 均值经 MLP 与冻结 video feature 差均值 cosine 对齐；后者望远镜为 (sK−s0)/K。§3.2 L150–164：冻 LAM 的条件 WM 与 target adapter/LoRA。 | 不是保留完整动作序列顺序或唯一物理 action。Table 4 L264–268 full 的 3rd→1st .5904 低于 w/o norm .5934。F L463–478 明示 camera/ego/环境混杂、collision hallucination 与 contact-rich physics/planning 的 future 边界。采用共享 effect reference，不授 robot 跨 embodiment 已证。 |
| [2602.10109](https://arxiv.org/html/2602.10109v1) | §2.1，L100–113：空间 read/query/action 梯度回传权；A L318–333：PSS=tr(PsPa)/minrank，仅最后层 q 的2048²矩阵和固定64 batch；C2/Table7 的 mixing-ratio 取舍，C5/Table10 L395–425 的 prompt 对照。 | PSS 对 G→−G 不变，nested 不同 rank 也可1，不能授梯度同向、PSS1 必相同子空间或全 VLM 无冲突。默认 prompt 平均77.9>padding58.5，但 Box 的 Widow75.8>默认73.2；有限组合收益不单归因 .5 gradient factor。E5 L514–518 仍错误 grasp/container，不授 universal optimum 或 formal safety。 |

## Books 交接

上述接口与直接反侧均足够支持**进入具体 owner 比较**，没有发现必须重开全附录、全部代码、旧版本或跨日全文队列的证据需求。代码若只是可选附件，不成为正文必要证据的伪阻塞。

root 对每项应分别记录：目标 Stable Knowledge Node、owner 实际句子、该句已承担的条件与反侧、本项是否新增长期设计约束；新增则定点写入并非作者 POST，已有则明确已有覆盖/仅报告。本文未实际读取这些 owner 句子，故不替 root 预授任何 Books disposition 或整日完成。
