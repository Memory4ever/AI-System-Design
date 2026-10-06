# 本日4项必要证据与owner提案（等待独立复核）

原返回 `V3_EVIDENCE_<ID>_INITIAL/EVAL.txt`；以下不授日级完成或代码/生产复现。

## 2602.10390（5）

exact-v1 §3–5，L97–230：在固定task distribution上区分task-agnostic与specific intents，distribution-robust affordance约束partial model/search分支。Theorem1限communicating MDP、deterministic competent planner、深度n任务与regret/failure bound，并且δ<1/2才有衰减；不能从普通LLM提示词直接认定已编码准确worldmodel。Corrected partial model给遗漏intent保留ε非零full-action支持，Theory2在固定长度L、独立uniform-intent sampling和最佳ε比较下计线性overhead，不是任意LLM search最优。

Pybullet 3/5/7 blocks、每次4 MC simulations、depth≤10、true reward、4 seeds。3block partial比full搜索有效，但LLM calls43.25高于full40，oracle15.75；减少搜索步不必减少调用。7block回报不确定性大，worldmodel/affordance都是LLM近似，提示词intent和固定morphology仍是限制。没有硬件/精度/concurrency/SLO保证。Ch25当前affordance packing主要合法动作诊断，不承载fixed task-distribution coverage与遗漏intent的支持保留；提案窄知识差额在AGENT-PLANNING：缩搜索必须保留可能漏掉的动作支持，理论条件与LLM近似分开。若root确认具体长期gap，再只核Theory2必要B2；不全读B1证明与所有prompt。

## 2602.10408（6D）

exact-v1 §3–5/§7，INITIAL L101–220、EVAL L221–303：warmup保持per-token Norm并收EMA，初始化γ加权能量least-squares scalar c，冻结c、共享cosine gate转为sample-independent scaling并fold到下一linear。Output final norm与内部Norm不同：ε=0的0-homogeneous final map使径向梯度为0，正margin下无final anchor的CE可logit chasing；固定目标scale penalty只提供局部径向恢复力，不证明整网稳定。LayerNorm folding要保留mean-centering affine结构，不直接把RMS公式移用。

TinyStories1–30M/8层/512 context/10kvocab、6seeds（9M all-taper删除1 outlier）；loss均有0.7–1.8%退步。H10080GB/bf16/CUDA12.1/PyTorch2.4.1 last-token forward、无KVcache、B1/4、T128/256/512、10warmup50times，是microbench非完整generation。GPT2配OWT/PILE存在局部CE反退，all-taper稳定性较差。Ch17 L319–361已有norm替换与信号传播，没有warmup→固定可折叠scale及独立output anchor边界；提案在MODEL-TRANSFORMER-LAYER窄整合这两份控制合同，不采普遍Norm无用或serving倍数。

## 2602.10410（5）

exact-v1 §2/§4/§5，INITIAL L103–244、EVAL L270–307、必要setup L261–269：RKHS delta-rule导出key-key triangular preconditioner，对V做lower-triangular solve后由普通softmax读取，改变模型语义不是softmax exact kernel。实际RN keys/offset让diag为1；原推导I+stril与exp matrix的记号不可无条件互换。非零query gradient theorem需K与softmax Jacobian的明确非null条件，只证明非零，不给梯度大小/conditioning或任务保证。Matrix inverse后的系数可signed，不是新的probability mass。复杂度仍O(N²d)，双向mask失去triangular特性。

Dolma~6.5B、22层/2048hidden/32Qheads4KVheads，文本给head dimension68与2048/32=64存在配置不一致，保留不采用精确架构推断；11ksteps B256/2k→500steps B16/65k，RoPE base改变。LUCID-PaTH不同于LUCID单项，2WikiMQA .274低于PaTH .283；taskvariance不等多trainseed。32k/B1/100新token的76/77ms未披露实际设备精度/耗时定义/SLO，不作生产延迟。Ch14 L393–433的finite-state diagonal preconditioner不是此O(N²) key-key solve；提案窄替代分支，额外矩阵/solve与非probability系数同处说明，若root认可gap再受影响深入，不抄有歧义的全公式。

## 2602.10418（6D）

exact-v1 §3–5/Appendix B2，INITIAL L100–219、EVAL L220–249及B2 L325–369实际：prefix separator处安全score，以vulnerable/fixed diff与AST合并、未paired时全局label传播训练Qwen2.5Coder7B；这是工具/人工label代理，不是可证明partial-code安全。4*80GB GPUs（A100或H100精确型号不定）、bf16/ZeRO2/3epochs、generation N10/20，额外sampling与PRM成本未完整计时。SVEN安全与CWEval功能+安全协议不同；SR@3收敛、@5 QwenPRM略优，QC7B LCB pass1 41.49低于QwenPRM43.44，反驳无安全utility税的普遍说法。

中心实现说明有必要冲突：主文weight∝exp(−r/τ)，B2改成exp(+r/τ)；主文step search，B2写Best-of-N；Eq3把class weight置log内部只加constant，不等加权CE。不能静默选择有利解释或授精确risk-aggregation算法；partial标签来自diff而非每个prefix实际运行漏洞验证，100% F1不授zero-day保证。提案保留报告的prefix-security评价/utility反侧，不写未确认的聚合算法。具体重开是官方同version实现/勘误解释权重符号、selection与class-weight，而不是缺所有附录；这几个命题争议不让其他证据变成未读或改判贡献关闭。

## 10390 当前正文比较收束（作者）

重读AGENT-PLANNING Ch79 L20–105状态/transition验证/受控horizon，合法候选与实际observation分责已有，但没有action-support剪枝对固定任务人口的覆盖及遗漏intent保留非零支持。拟在transition估计与lookahead交接处两短段，仅采用partial action模型+full-support混合的设计分支，communicating MDP/deterministic planner/δ和fixed-length理论条件明确；不采用一般epsilon最优/任意LLM regret保证，因此不为了强定理展开全B证明。Pybullet调用数反退和支持失准回退full-action同段。待窄锁，不凭可映射owner整合。

最终状态同步（2026-10-04）：本组必要源独立复核完成；10390 Ch79、10408 Ch17、10410 Ch14实际两段/邻接/末注已root非作者POST通过，锁释放。10418中心权重/selection/class-weight争议暂缓，不进入Books；日级另验。
