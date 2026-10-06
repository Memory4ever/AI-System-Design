# 11/15 新增具体方向：Language Drift

作者Planck；[exact v1](https://arxiv.org/html/2511.09984v1)。只送新增方向，不重复Echoing/UGCS/TawPipe。[Ohm实际复核](FIRST_INDEPENDENT_REVIEW.md)已通过局部诊断/公式反例与6分，日期改用[保守历史列表区间](DATE_RECOVERY.md)BJT [Nov14 09:00,Nov15 03:05:54)，不再采用被否定的注册上界。不授日级完成。

## 准入命题与拟分

跨语言RAG的表面答案不匹配常被一概当理解/检索失败 → 固定query/prompt/ICL语言，仅切换gold retrieved context语言后发现部分错语言输出仍与reference语义一致，hard vocabulary isolation也可缩短输出、损伤质量 → 需分开语言合规、语义内容与生成成本，不能仅按ROUGE或LC选择隔离策略。拟新增命题2+2+2=6；negative/design边界只深入受影响核心，分数不含“采样改变轨迹”等成熟原则。

完整题摘raw第二批已经读；必要正文实际位置：[raw12](raw-web-12.json) §2.1–2.6/L85–153、[raw13](raw-web-13.json) §3.1–3.3/L197–243、[raw14](raw-web-14.json) §3.4/Table3/L244–268。不是只摘要改写或全文queue。

## 支持与关键反侧

- 三套QA各1000样本、EN/ZH/AR/RU，由GPT-4o翻译后人工核；gold retrieval排除了真实retriever召回链，LLaMA3-8B-Instruct/Qwen2.5-7B-Instruct，固定4-shot/default decoding。§3.2称五独立run平均，但未披露seed/不确定区间；硬件、precision、batch、concurrency/SLO、端到端latency均Not Disclosed，不从training-free授零成本。
- Table1的翻译后ROUGE及GPT-4o semantic match支持**某些漂移输出**不是完全理解失败。只约42～63%semantic match、不排除另外输出的理解失败；GPT judge/翻译同源偏差也不证明decoder因果或pretraining英语token频次。作者把English attractor与内部偏置写得更强，当前不采用该因果归因。
- Table2 ZH-EN HotpotQA LLaMA3：LC68.4→90.6，ROUGE.182→.306是作者局部数值，不外推所有语种/大模型。Table3 PLI/VRD/SCD CoT104.0/38.6/134.9说明各路径输出预算不同；不把较长CoT证明推理更完整，也不将ROUGE改善全部归于“保留跨语提示”。translation-based evaluation得到100%LC是定义结果，不是无成本生成控制基线。
- §3.1实际不是additive penalty：三词组按Unicode/tokenizer heuristics缓存；raw logits target乘alpha=1.1、distractor乘beta=.9、neutral不变，延迟5步启用。这一式不保证“boost/penalty”文字：target=-2,distractor=-1，原target概率.26894，变换后.21417；给两logit共同+3不改原概率，却使变换后target概率.33181。这个两token数学反例已实际计算，**不是**作者实验复现/代码检查；公式的符号与平移依赖须保留，不静默改成常数惩罚来修论文。
- 因而保留局部现象、评价分账与hard-isolation代价；不采用SCD普遍单调控制、所有language/tokenizer可移植或内部因果机制。若长期整合要讲这条算法，必须先得到作者精确实现/勘误说明其logit convention和语言分组；可选代码未审，不把它变成诊断命题的必要条件。

## 实际owner差额，不按名称缺位

本次已实际读取Books context/philosophy/writing/latest checkpoint、Ch20相关正文/Ch19/21开头交接，及Ch76开篇。owner唯一建议`MODEL-SAMPLING`：[Ch20](../../../../../books/part-02-model/20-sampling.md)。已有L141–168负责penalty vs grammar、processor order/version，L452–460负责prompt与decoder分离及格式/内容双验，L502–514负责成本。这些成熟原则可具体已有覆盖，不需重复写入。

**可供root选择的窄差额**是在Ch20“格式损失要先定位在Prompt，还是Decoder”原论证后，增加跨语言输入的受限诊断分支：固定query/instruction、只变retrieved语言，语言合规与跨语言语义相似度分账；硬隔离的短CoT与表面评分不能证明质量/资源优势。原格式/内容论证不覆盖本次具体语言评价混杂，而Ch76开篇已规定retrieval/packing/generation整链但不拥有token控制。不要因“SCD没有名字”强造gap，也不改Ch76/19/21。若root判断现有分账足以承载，已有覆盖/仅报告同样有效；若窄融入，root协调实际写入及非writerPOST，本作者不写共享Book。

请求root独立核：日期组合权限、上述准入/6分、公式反例与实际owner差额，决定可采用的最小诊断命题。所有性能数字/推断边界保留，未复现；其他14个list吻合项不等同本项Evidence通过。

## 校准后作者最终处置（待独立核处置）

只采用Ohm已核的局部跨语言诊断/质量与成本分账，标准审阅完成；**仅报告**。Ch20现有“格式损失要先定位在Prompt还是Decoder”实际正文明确三路径控制、格式合规与内容正确分离，以及第二调用/tokens/延迟成本（本次再次实际读L452–460）；本材料给出gold-context语言切片的新验证，但没有证明需要改变这条现有设计判断。具体跨语言表格保留日报，不为新增案例重复通用论证，也不按SCD名称缺位造缺口。公式控制权限受限，未经勘误不整合算法保证。该选择不是关闭贡献或降低评分；6分局部新验证仍保留，Books实际0，最终处置交非作者核。
