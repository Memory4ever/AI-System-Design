# 长编辑循环 / GroupDPO：必要 source→owner 提案

作者 apr20_resume；作者必要原始方法、评价与反证见[v3-reopen-notes 最后四项](./v3-reopen-notes.md)。两项2+2+3=7深入，未独立采用、未写 Books、未计 I；不是日 Gate。

## 15597 DELEGATE-52 → PLATFORM-EVALUATION-SYSTEM / Ch66

[official v1](https://arxiv.org/html/2604.15597v1) actual §2–5/§8、必要 A.1/A.2、B.2/B.3、M.1/M.2。当前Ch66 `从 Final Pass 扩展到 Trajectory、Cycle 与 Checkpoint Decision` 516–525保存整个cycle、handoff与artifact verifier；未解释**可逆编辑重建只测复合保留性，不证明forward任务正确**。拟在Full-cycle段后、Checkpoint decision段前两段：

> 长期委托编辑还需要单独测 artifact 保留性，而不是只看每次任务是否结束。一个可复查分支为编辑定义 forward/inverse instruction，在每步独立 session 中携带文档，连续执行多个 round-trip，再按领域 parser 比较重建内容与原始 artifact。这能暴露多次看似成功编辑后积累的稀疏严重损伤；但高重建分数可能来自 no-op、部分执行或错误抵消，低分也不能分解错误出现在 forward 还是 inverse。必须另验前向编辑确实完成、可逆条件成立，以及 parser 没有漏掉需要保护的语义字段。
>
> 这条测量增加成对执行、checker 和原始 artifact 存储成本，也将可逆任务选择、session边界、distractor 与领域权重写入 EvalSpec。[受限长编辑实验](https://arxiv.org/html/2604.15597v1)中的严重 round-trip score drop不能等同逐token内容丢失率；基础文件工具harness也不代表所有Agent系统。无法构造可信inverse、任务确实有损或checker不足时，应回退逐步diff、不可变before-image、具体编辑的独立测试和人工审阅。完整cycle/verifier仍负责交付判断，round-trip分数只补 artifact-preservation evidence，不拥有任务完成权。

源需保留：52×6/real2–5k种子/8–12k distractor；19models/20 interactions，各步fresh单turn无history。A的93.8% fully/partially是attempt非correct，GPT5.4 judge也是受测model；B明确opacity/error-faithfulness近似条件。工具4GPT与basic5tools/25turn/500ktokens，GPT5.4工具latency×.4而非全慢。采用以上测量边界，不采用全生产文档损失25%/所有委托不可靠或形式禁止工具。

## 15602 GroupDPO → TRAIN-DPO / Ch34

[official v1](https://arxiv.org/html/2604.15602v1) actual §3–5.3/Limitations、必要 A.3/Table6–7。Ch34 `Sequence Log Probability` 128–155冻结response/tokenreduction，`工程数据流`316起保policy/reference/distributed身份；没有**耦合group loss的系数计算与sample backward分离**。拟在工程数据流标题后、分布式身份段前两段：

> 一组response共同进入preference objective时，直接保留整个group的前向图最清楚，却会同时驻留多条长序列activation；把所有正负pair展开再逐pair反传虽省驻留图，又会重复计算同一response。对只通过每条response的score `u_i(θ)` 耦合的可微group loss，可以先在同一参数点无梯度计算全部scores，得到 `c_i=∂L_group/∂u_i`，再固定系数，以 `Σ_i c_i u_i(θ)` 逐sample累积梯度。chain rule使其在该参数点保持一阶梯度，不保持原loss值或Hessian；response、reference、token reduction与参数点必须一致，全部梯度累积完才提交更新。forward随机性或score版本不同也会破坏这份等价，这是将公式落实成执行协议的额外条件，不是论文已验证所有runtime的保证。
>
> [受限GroupDPO实现](https://arxiv.org/html/2604.15602v1)用额外no-grad pass和小系数状态换较低activation驻留，group-level pair interactions仍可为二次规模，并非总计算与group大小无关。其单H10080GB、gradient-checkpointing测量的memory overhead排除了初始化后的参数/optimizer base及optimizer.step临时峰值，不能写成GPU总峰值恒定；step latency反而包含optimizer，额外pass也不能省略。取样/偏好truth仍由数据owner负责，正例NLL是另一项objective选择；系数陈旧、数值不一致、二阶optimizer或额外前向成本不合适时，保留直接group graph、较小group或匹配的pair基线，并共同验收chosen likelihood、KL和任务slices。

只采用式子与执行分离/成本边界。主实验multiplegroup并不全任务胜pair：gemma general37.8与多个group36.x，coding反向；offline β/NLL sweep/最高validationmath vs last取better，online最高checkpoint影响泛化。A.3 offline8/8/32GPU、online8T16R/H100，precision及seedCI未披露，不采无条件质量优势/生产SLO或所有group Hessian等价。

## root 非作者有限 source→owner 复核

实际打开15597官方v1 §2–5、§8、A Instruction Compliance、B.2/B.3与§4.2工具反例：独立session携带artifact的round-trip测复合保留性，高分不保证forward正确，低分不能分错误步；93.8%是尝试/部分执行，不是任务完成。实际Ch66 full-cycle/verifier与checkpoint前后已读，尚未区分可逆重建与单次前向编辑正确。两段literal采用通过：保留no-op/抵消、parser、可逆任务及工具harness局限，不把有限score损伤写成生产内容损失率。必要来源与对照足够，未复现实验或遍历所有52域附件。

实际打开15602官方v1 §3/§4系数和surrogate、§5/§5.3以及A.3；chain rule只在同参数点、同score输入且系数stop-gradient下保持一阶梯度，loss值/Hessian不同，随机forward一致性是明确工程推断。H10080GB测量的额外forward/backward内存排除optimizer.step临时峰值，latency包含optimizer，AllPairs交互仍二次。实际Ch34 logprob及工程流与相邻Ch33/35已读；当前尚缺耦合目标的系数/逐sample反传分离。两段literal采用通过，保留reference/data/参数点身份与质量不普遍胜出；不是全runtime等价或总GPU峰值恒定证明。二者均仅授权本文必要两段及章末notes，真实写入后另核，不据提案计整合或日级完成。

实际写后：root顺读Ch66的full-cycle→新增两段→checkpoint选择，以及Ch34工程流→新增两段→分布式身份，两者与通过literal一致，source-family在具体机制正文而非只在notes。成本、no-op/抵消及forward正确边界、一阶同参数点/随机性/总内存边界均仍在对应机制旁；两个章末notes及scoped diff检查通过。两项真实Books写后PASS，不代表本日其他候选或日级Gate已完成。
