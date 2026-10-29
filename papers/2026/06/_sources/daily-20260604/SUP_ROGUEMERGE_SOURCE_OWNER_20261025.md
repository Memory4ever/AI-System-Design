# RogueMerge 2606.03344v1：首次必要安全域 / actual Ch72 / 两段PRE提案

R55完整题摘/当前notice/Jun03联合日证已独核通过，复用不第三。只v1，不混current v2 Oct12措辞。作者评分2+2+2=6：重要的合并后行为/不确定组合评价边界，跨component→build artifact→行为审计，可复用；不按安全名词/170模型/投入加分。安全影响与既有长期缺口深入必要域，未获本项Book授权/未写/未PRE独核，不预I/DAY。

## 原件与实际读界

https://arxiv.org/html/2606.03344v1 实际GET exit0，原HTML712006字元/178930原token无truncation，剥标保math annotation得到完整TEXT133527字元，已真实保存`2606.03344v1.fulltext.txt`。实际读III–IV全部必要威胁/目标，V-A数据/merge/metric条件、V-B主结果解释与T3、V-C/T5–6及关键反侧、V-D/T7–8、B-C训练配置/B-D六算法概要/B-E基线比较首段；未读全部T1/T12大矩阵每格、完整A证明、全部图像、C敏感prompt样本、算法实施细节/代码或复现。支持及关键反侧足够即止，不提供攻击实施教程。

## 必要支持与反侧

- III：攻击者控制自有task vector，不控制下游merge，也不知道算法/超参/其他participant数量与向量。local dataset与shadow prior不等知道真实下游；clean utility与攻击目标不同，普通task分达标不是安全证据。原受测六utility任务、四攻击目标不要混称六种攻击。默认四task、JB另加Safety，In/Out不是相同难度排序。
- IV-A/B式3–8：把攻击评价放在缩放合并后的模型而非孤立vector。未知benign update用有效干扰小范数假设近似，再以有界worstcase代期望；系数取样与局部一阶干扰只是模拟，不是获取真实其他向量或证明任意merge等价。cosine均值接近0不证明非线性行为无干扰；“平坦所以超bound仍鲁棒”仅作者解释，本次不采用为通用结论。
- IV-C式9–12：parameter-level的不确定合并与input-level的prompt异质性是两层对象；DRO在连续input embedding而非任意离散文本上扰动，输出标签固定。小rho/nu、loss梯度Hölder条件下的渐近近似界不是所有有限radius/未知prompt保证；本次不采用完整定理或可执行优化recipe，未读A完整证明不冒已验理论。实测敏感性/utility退步近文。
- V-A/B-C：主要Llama3-8B，Qwen2.5-7B消融；20K local任务样本、两A6000、batch16/1250steps、LoRA rank64/alpha128，标准task约2h/两卡；攻击/utility各5K、每set batch4。B-E基线额外训练约3h/run vs Rogue约2h为作者局部描述，不等匹配完整搜索/数据与全部成本。precision/完整decoding并发、独立训练seed/CI未由本必要域披露，不补造。50%任务测试抽样与单A6000四task约50min是B-A预算文字已定位，未据此声称全成本或复现。
- V-A指标：utility ratio按不同task相对base归一后平均，非安全效用标尺；四目标ASR分别为exact目标串、注入任务分、WildGuard judge、system prompt exactmatch，不能跨目标合并比例。baseline LoBAM/MergeHijacking从分类适配、SFT在自身攻击高而merge后失败，支持比较最终artifact而非只测component；不授鲁棒优化唯一因果或所有朴素基线失败。
- V-C/T6：无MUAO/DRO、MUAO-only、两者皆有形成受测分支对照；JB/SPE在Out与In不同分布，不将更大In增益当全分布鲁棒。更多co-merged任务JB下降、DELLA部分攻击退、过大rho伤utility；T5多目标loss合并也损utility，不能由最终平均utility尚可断言所有子task不损。fig仅文字/表caption读界，未核像素不冒曲线精度。
- V-D/T7：更强norm clipping可将受测backdoor ASR降至0，同时utility低于cleanmerged；PI/SPE仍有残余，因此不是“所有防御无效”。T8正文FT/KD精确数与表格人口/数值不齐（FT正文76→45而表69.8→58.3；KD正文98→53而表99.3→59.8），本次不采用这些跨口径精确差额，仅保有限方法/残余与代价。自适应trigger-conditioned分支提示已知probe缺口，不证明所有未知trigger不可检测；防护是工程建议而非作者认证安全控制。

收益采用最小命题：component级clean utility/孤立攻击测试不能替最终merged artifact；unknown merge模拟与prompt变体不是同一种覆盖。代价包含local/shadow准备、vector训练、merge构建矩阵、prompt/配置搜索、独立judge、clean与各安全任务回归；未披露项Not Disclosed，不签端到端性能、安全/生产保证。

## Actual owner与差额

已完整读三Book上下文、ROADMAP Ch71/72/73职责及各章开篇交接。实际唯一owner `PLATFORM-SECURITY`：`books/part-06-ai-infrastructure/72-security.md` 真H3 `Model Merge Input 是对权重的 Supply-chain Write Access`，既有`SF-ROGUEMERGE`，不得另建家族/owner或改旧日期。完整两段已承载开放vector的write access、digest/merge identity、隔离组合、merged artifact clean/targeted/adaptive/crossalgorithm gate及有限人口/回退。不能因题名一样NC，也不重复这些门。

具体缺口是：已有一句merge-specific uncertainty没解释局部component与merge后对象的分账，以及bounded-effective-interference与embedding邻域各自的有限覆盖，容易把“未知配置”误读为知道真实他人vector或全分布证书。拟在该H3**原第一完整段后/原第二完整段前**加下面两段，旧两段/inline结构/原marker都不动；不在Ch30重复参数化/训练知识，不改任何共享Book，待reader PRE及root精确新授。

### 完整上锚

第三方 task vector 或 adapter 在受信团队内、用途单一时可以作为低成本能力组合输入；进入开放共享后，它实际拥有修改最终
权重和行为的写权限。Merge gate 应冻结 contributor、base/source digests、vector/adapter digest、merge strategy/order、prompt
assumptions 与构建环境，在隔离环境完成 composition，再对 merged artifact 执行 clean utility、targeted/adaptive behavior 与
跨 merge-algorithm regression。Contributor 只能提交 component，builder 产出候选，独立 security/evaluation gate 决定发布。

### 最小原稿（两完整段）

评估对象还必须区分提交的 component 与最终 merged artifact：一个更新在独立模型上的攻击表现和 clean utility，都不能直接替后者签字。攻击者即使不知道真实共合并向量，也可能在合并后行为目标上，把缩放与未知更新的有效干扰作为模拟条件共同优化；只测孤立 component 或一个固定组合就会漏掉这条适应路径。[受限的合并攻击对照](https://arxiv.org/html/2606.03344v1)支持重新测试最终组合，而不证明攻击者能控制 merge 或任何组合都会失败。构建身份变化后，应分别保留 component、clean merged 与待发布 merged 的任务效用和受测安全行为，不能用平均任务分代替后两者的差异。

未知组合的覆盖仍需分账：参数空间中的有界有效干扰，只是对未知合并影响的近似；输入 embedding 邻域内、固定输出标签的鲁棒目标，则是在处理 prompt 变化。前者不提供真实其他参与者向量，后者不覆盖任意离散文本，两者的局部假设或渐近近似也不能升级为所有配置/提示的安全或攻击证书。更多合并任务、较激进裁剪或更强鲁棒目标都可能改变攻击率与正常效用；受测裁剪能消除某类攻击却损任务分，其他目标仍有残余。配置/提示搜索、组合构建与独立回归全部计费；覆盖不明或任务/安全回归失败时，保持拒绝发布、可信组件与受控组合回退，不由一次 clean gate 或一个防御标签宣称风险消失。

### 完整下锚与原family归属

隔离与多算法回归会增加构建矩阵和误报，且已知 probe 无法证明未知 payload 消失；攻击还可能利用 prompt 或 merge-specific
不确定性绕过。来源不可验证、组合测试失败或行为漂移不可解释时，应拒绝 component，回退受信 source model 或重新训练，
而不是用平均 utility 覆盖供应链风险。exact-v1 的六类任务、六种 merge algorithm 与 170+ merged models 只证明其攻击在
披露设置中的可迁移性，不证明所有 merge 或防御边界。

<!-- semantic-body-binding:SF-ROGUEMERGE -->

### Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family

### 拟本人true-H2 Review notes注

- `SF-ROGUEMERGE` — Daily2026-06-04补Jun03；[exact-v1](https://arxiv.org/html/2606.03344v1) III–IV、V-A/B/C/D与T3/5–8、B-C/D/E必要域，2+2+2=6，安全影响/实际缺口深入。仅component/merged评价对象与参数干扰/input邻域分账；保有界干扰假设、embedding代理非离散覆盖、utility与ASR不同口径、normclipping局部可奏效但有代价及全费，不采超ball鲁棒/完整理论界或T8跨口径差额。当前v2摘要漂移隔离，只v1；未读全矩阵/完整A证明/敏感prompt附录、代码或复现。待首次必要Source/score/actualowner/PRE，尚无本项授权/未写，不预I/DAY。
