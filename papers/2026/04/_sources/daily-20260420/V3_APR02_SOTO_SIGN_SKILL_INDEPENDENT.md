# Apr20 三项有限 source→owner 独立复核

复核者apr02，非Apr20作者、非这三项Books写者。恢复后实际重读当前AGENTS、三合同、统一入口与ROADMAP，并读作者[V3_SOTO_SIGN_SKILL_OWNER_PROPOSALS](./V3_SOTO_SIGN_SKILL_OWNER_PROPOSALS.md)。本批只核必要原文、拟采用范围及当前具体owner/邻接，不核日期全日Gate、不复现实验、不扩附件树、不写Books或作者Report。结论是写前窄提案可采用，不是已经Integrate。

## 2604.15453v1 — SoTo

[官方v1](https://arxiv.org/html/2604.15453v1)实际§3–4、§5.1–5.2、D.2–D.3、E.3–E.4、G。partial reconstruction→verifier→beam与完整BoN不同；matched 2D baseline及uniform verification控制支持表示顺序影响搜索。NFE未计各函数相同实际成本，H100二十图时间分解显示flow detokenization占主导；大搜索可提高内部verifier却损害外部质量，弱prior缺失不由搜索普遍补回。零AR不是零训练tokenizer。

实际Ch24 AR/RAE-AR约35–55是预测性、历史误差；Ch23约123–133提供learned nested ordering，未承载部分prefix可供质量sensor辨识的搜索接口。**2+2+3=7深入，窄gap写前PASS**，唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`；按作者拟位置补两段成立。保beam/lookahead重建和评判成本、grid/BoN回退、verifier适用范围，不采用未审AppendixB全局界，不外推所有模态或wall-clock普遍最优。

## 2604.15416v1 — StoSignSGD

[官方v1](https://arxiv.org/html/2604.15416v1)实际§2.2 Definition1/Proposition1、§2.3–2.4相关假设、§3 Algorithm3与3.1、B.2/Table10–12。`sign(v+G·U[-1,1])`在`|v_i|≤G_i`且正包络时的期望是`v_i/G_i`；不是raw gradient无偏。实践Alg3先EMA momentum、再历史absolute-max包络，含weight decay；不能将理论无momentum/投影过程与实践等同。FP8失败对照保BF16 master/nonlinear，E5M2 gradient/E4M3 state与GPT2固定训练；underflow不证明所有FP8 AdamW失败。

实际Ch28 sign geometry约382–393与state quantization约748–754没有这个“随机sign期望保持预条件更新、尺度状态改变几何”的分支。**2+1+2=5、gap深入写前PASS**，owner `TRAIN-PRETRAINING`。作者窄稿合理；保zero handling、采样方差、historical-max漂移和高精度回退，不将Qwen/数学task及单FP8实验升级大模型普遍收益，不采用未绑定token/总成本的speedup。

## 2604.15415v1 — HarmfulSkillBench

[官方v1](https://arxiv.org/html/2604.15415v1)实际Benchmark Construction/Evaluation、Tables5–7、Related Work与Limitations。200 skills、API六模型、temperature0/minimal reasoning；bare task、主动调用、被动读取后plan是不同处理与分母。明确去除scripts，只测有害规划意愿；HiTL/AID是建议文本而非真实批准/外部告知。原文主动加载公开有害功能与隐藏payload威胁不同，第三方受害者不因用户同意而变成授权用途；分类taxonomy不能当法律裁决。

实际Ch72 Skill Poisoning约1414–1436与description≠code约2571–2575解释隐藏effect，未承载功能透明却违反平台policy的admission层区别。**2+2+3=7安全深入、窄gap写前PASS**，owner `PLATFORM-SECURITY`。两段可嵌现SkillPoisoning入口；保任务/计划/effect分账、policy版本和误拒绝成本，可信低风险分支及真实effect Gate不被此文本benchmark替代。不得据harm score支持生态事故率或实施有效性保证。

## 交付

三项source→实际owner窄采用均通过；未写共享正文，仍需root授锁、作者实际落笔、非作者写后与全日Gate。没有新增材料请求，不把普通Books工作装作external blocked。仅新增本审计文件，保其他dirty/staged修改；本文件Markdown与限定diff检查通过。
