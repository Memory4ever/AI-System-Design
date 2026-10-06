# 22 日七项风险/反侧必要 core 补读

执行者：James，**本日报告作者**。这是作者侧必要证据补读，不是独立 Evidence/DAY，不能拿作者声明替代 root 复核。root 已核七份精确 v1 完整题摘及三项代表关闭、通过局部 FIRST；本次只补受影响七项，不把172提交库存变成全文队列。

实际请求见 [risk-core-fetch.json](risk-core-fetch.json)：2026-10-06T06:21:40～51Z，七个 `https://arxiv.org/html/<ID>v1` 均200，原响应 `<ID>v1.core.raw` 与标准HTMLParser派生文本 `<ID>v1.core.txt` 保留。HTML 可得，未使用PDF fallback，**没有必要正文外部阻断**。只读下述必要域，没有遍历所有引用、附录、实现或运行实验。首次公开日期缺口仍隔离：不评分、不转正式候选、不写Books、不授正面覆盖或安全保证。

## [Inverting Trojans in LLMs, 2509.16203v1](https://arxiv.org/html/2509.16203v1)

实际读 §3完整算法/损失与超参边界、§4完整设置、§5.1–5.6结果与反侧、§6限制（派生文本71–346）。BABI用负margin与内部激活 cosine penalty 压低本来与目标类语义相关的候选，并逐步扩展有限触发序列；不仅是词表黑名单。其威胁/消费合同是预定义响应类、小干净类集、内部特征与后验可访问；显式黑名单还使用微调前foundation模型，不是通用黑盒生成式后门检测。

验证是FLAN-T5-small、SST-2二分类、5 clean/5 poisoned实例，同一“Tell me seriously”触发、dirty 0.5/0.8/1%与clean 5/7%，IMDB每类50个干净样本，A100，J=3/N=20/L=5。部分触发片段高排名、20个检测配对可分，不等于未知触发/任意模型总体准确率。过强黑名单可移除真触发；J太小只找片段，N提高花更多枚举/前向预算；λ/层选择是超参，外国情感token与分词残片仍逃显式黑名单。非受限多token生成、多类/更大模型在§6仍是未来工作。保留局部检测机制潜力，不授通用防护。

## [Visual sycophancy, 2509.16149v1](https://arxiv.org/html/2509.16149v1)

实际读 §3.1–3.2、§4–5.1、§6.1–6.5（含Tables6–9/推理时延）、§8限制（122–140、257–294、515–653）。SRT训练图像文字化→判断用户意见是否误导/纠正→总结；GPT-4o-mini构造SRT-30K及解释，两个7B微调模型，lr1e-5/batch64/3epochs，4 A100-80G约4h，测试temperature0，MME11子集、二元问题七种注入场景。Flip率本身混合好/坏纠正，必须与conditional correction/sycophancy分开。

关键反侧：图/文对照的文字描述直接含正确属性答案，resolution下降也直接丢失视觉证据；两者不能唯一证明“多模态训练量不足→置信度”因果链。SFT减少迎合却使纠正率跌到6.18%；SRT为28.86%，仍低于未训练34.39%。去reasoning的sycophancy 1.56%优于完整3.47%，但correction 10.22%低于28.86%；不是所有指标支配。单A100/1200项从2m9s到7m39s，是更长CoT的代价，不是生产SLO。局部反证有效，不能用“无损纠正”总结；视频/音频只是未来方向。

## [SABER, 2509.16060v1](https://arxiv.org/html/2509.16060v1)

实际读 §3、§4必要归一化残余与三阶段选择、§5完整评价协议、§6.1/6.3、§7.1–7.3、Table4/§8–10及必要A.4–A.5（86–201、306–311、397–505、1028–1038）。攻击者能改变模型内部执行，早层表示按目标层norm缩放后接入后层，另预填“Sure, here”；这是white-box架构/执行权限风险，不是远端普通prompt权限。验证集41 harmful/41 benign，HarmBench测试159 standard behaviors，另JbBench100/AdvBench520；Llama2-7/13B、Vicuna7B、Mistral7B，greedy输出512/150tokens，HB验证/测试与JB judge不同，不合并成功率协议。KL仅衡量benign提示最后token分布，不能替整体能力保持。

关键反侧：system prompt有/无分别报告，不与不能删system prompt的攻击混为同权限对照；baseline与架构改动权限/搜索预算并非单因素matched。NoENorm使Vicuna/Mistral PPL明显恶化；Table4 Llama2-7B MMLU46.37→32.49、TinyHellaSwag77.55→64.14，反驳无损通用能力保持，TruthfulQA采用ROUGE不是事实安全证书。A.4连续λ有validation过拟合退步，更强残余会伤连贯性；§10连续λ尚待研究的说法与A.4.1已经执行该实验有文本不一致，不能照录。保留内部执行攻击面与有限失败证据，不提供生产攻击复现或防护保证。

## [Randomized Smoothing Meets VLMs, 2509.16088v1](https://arxiv.org/html/2509.16088v1)

实际读 §4算法/Th4.1–4.2及完整短proof、§5.1–5.4假设/近似、§6完整评价与失败、Limitations（109–304）。图像加Gaussian、文本固定；oracle把自由输出归成安全类/离散动作/语义等价类，再为smoothed复合决策作证。不是逐次生成内容或实体行为都安全，也不覆盖文字扰动。缩采样半径结论依赖CLT/概率远离0/1、主要质量集中β≥0.7及阈值平均，是近似不是所有输入精确关系。LLaVA1.6、Gemma2-9B oracle、σ0.5/α.001、vLLM，4 A100-40G；有prompt无法certify。n100约2.8s、n1000约38s只是该批处理负载；多用户抢batch时不继承，GPU翻倍减半仅预测，precision/长度/在线SLO未披露。

**必要中心争议，作者实际推导：** Th4.1 Eq5从“oracle error rate ε<.5”写出 `q=p(1-ε)+(1-p)ε`，实际要求两类相同的conditional flip probability，而非仅总体error bound；正文未明确这个强化条件或语义聚类的稳定等价关系。若真class概率p=.55、false-positive=.2、false-negative=0，则q=.64、总体error=.09<.5，但q>p；因此Th4.2把q的下界无条件当p下界的推论不从其宽泛表述成立。这是本次作者反例，不冒充作者实验。只对固定复合分类器的通常RS证据与对“真实oracle语义安全”转移分别判断；中心保证隔离为争议，待补两类conditional误差/独立稳定分组条件、有效非对称修正或纠正版proof，日期恢复也不能直接采用宽保证。不机械删除局部算法/成本潜力。

## [Latent learning, 2509.16189v1](https://arxiv.org/html/2509.16189v1)

实际读 §3 formal intuition、§4.1–4.4/§5完整bench与方法、§6全部文字结果/图caption、§7局限，以及必要B.3/C.1–C.3（117–213、492–537）。小型受控decoder12层/1024embedding，codebook held-out-use、reverse/semantic/tree、pixelRL与ASCII-BC gridworld；训练重建信息，不等于能把未cue知识参数化用于新任务。Retrieval保证至少一个relevant经验并混distractors，3–7条，BC仅relevant；监督当前参数重新encode，RL用旧cached states并有漂移。loss-token预算相同，**不等forward/context成本相同**，retrieval长度更长。

小任务4runs CI、RL3runs bootstrap，BC binomial CI；训练ICL去除后oracle检索仍差，semantic关联线索强时baseline也泛化，gridworld检索仍远未ceiling。C.1大batch/C.2无关检索/C.3长度batch控制支持有限关系，但最短base sequence时增长度也有效；没有解决真实检索recall或成本。作者明确这是特定潜在泛化模式，不说参数学习不会泛化；训练augmentation/preplay是共存方案。保留负面generalization与retrieval成立条件，不以“玩具”或Books成熟原则排除。

## [MatchFixAgent, 2509.16187v1](https://arxiv.org/html/2509.16187v1)

实际读 §3.1–3.2 overview、§3.2.3–3.4、§4.1协议、§4.2.1–4.2.3文字失败、§4.4–4.5与§6限制（126–214、300–335、530–557、901–936、1232–1320）。六类semantic analysis→可执行对照测试/修复→verdict，Tree-Sitter提供结构但LLM输出不是程序等价proof；测试范围/可达输入/语言接口各有失败面。Claude3.7/ClaudeCode1.0.51为主，1000s timeout，2219 pairs/24项目/6 PL pairs；avg309s/$1.22，开发“便宜”指LoC，不是总成本低11.6倍。

关键反侧：只对每项目D1/D2各最多5个分歧，145案例、双作者18.6%分歧再协商；过滤mocking不可启用与非1:1 Rust refactor。没有核双方同意的真等价，§6明确没有真实总体accuracy。RustRepoTrans分歧仅12.5%支持本法，失败含hallucination/inadequate tests/infeasible private输入。1091共同同意样本的消融用agreement作accuracy，不是独立真值；一次运行、大样本不消除随机性和selection bias。作者文字示例把Go len泛说成Unicode计数，但实际snippet明确 `len([]rune(s1))`，与Rust string `.len()` 不同：二者直接string len本都计bytes，Go此处先转换rune slice再计元素。因此这是文字限定不足，不据此推翻非ASCII反例；源码/输入/LCS仍未运行核验。该基础语义已定点核[Go规范String/len](https://go.dev/ref/spec#Length_and_capacity)与[Rust str::len](https://doc.rust-lang.org/std/primitive.str.html#method.len)，不以当前库说明反推artifact执行。保留测试/equivalence合同反侧，不能从verdict完成率授形式验证或自动生产迁移。

## [The Alignment Bottleneck, 2509.15932v1](https://arxiv.org/html/2509.15932v1)

实际读 §3–7的必要definitions/assumptions/theorems与短proof，以及F expectation→high-probability、H true/observable loss link、I posterior-loss identity（90–298、必要F/H/I752–794）。有界loss、i.i.d./memoryless U→H→Y、source-conditioned每层capacity min是cascade保守上界，optimizer未必兼容，不是可达到的信息容量。Fano下界要求separable codebook/对所有action的loss–index link、uniform J独立S的mixture/minimax语义；它约束该设定的test decoder，不直接证明所有实际RLHF随更多数据必然无收益。

PAC-Bayes采用data-independent prior、residual ρ界、I(U;S)及marginal prior mismatch；capacity只控制**expected KL**，要高概率仍支付Markov slack η。上下界只有同mixture/source与loss link才是同一个风险区间；canonical loss使用真实latent U的conditional expectation，数学身份不提供可观测估计器或可执行校准。大ρ/context信息可主导，压缩虽能界ρ却不保证保持风险。§7把训练过拟合直接解释为sycophancy/reward hacking是解释性推断，不是模型实验证明；未给有效capacity测量或量化部署风险。保留假设受限理论潜力，不授普适alignment墙、empirical bound或完整所有proof认证。

## 作者侧停点

七项必要core **7/7已补读**；普通未读0。上述实际反侧/中心争议交root独立核，不自授通过；原日期hold、其余有效题摘/贡献判断不动。精确原响应可执行，未称外部阻断。Books POST Omni通过、FSF须窄修后再核；两项未同时通过，22保持进行中，不授DAY。停止条件是七个指定必要命题的method/评价/假设及关键反侧已足够界定，不扩附件或别日。
