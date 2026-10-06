# 2025-09-20 非作者独立验收

复核者：sept07_10_author（本日作者 Tesla；未写本日作者报告或共享 Books）。窗口 2025-09-19T09:00+08～09-20T09:00+08。本日已独立重读 AGENTS、Prompt、Research/Report 合同、Sources 使用/Daily/arXiv、ROADMAP 与相关 checkpoint 路由，只读取本日材料与停点。旧暂停记录保留为历史，当前根线程恢复后的授权有效。

## FIRST 与必要反侧

实际独立读原53份完整精确v1题摘（15478/15560以同日abs原件补HTML失败），不是53全文深审。系统替代、理论、局部负面及验证不能因为非通用、小模型、单任务或现有Books主题关闭；具体保留异质query缓存15515、光collective15450、localmax15958、阈值卸载15674、Arnold15940、RLinf15965与ByteRobust16293。题摘条件未变不扩实现/附件；RLinf仍只v1 1.1–2.13倍，不采后版数字。所有准入潜力仍缺first-public，不评分/正式采用。

- 15478精确v1 PDF实际读§3–5、§6/8、Appendix D.1及TableD1，本地视觉核页5/Table4与页19/TableD1。四API May–June2025、26人726成对prompt、17评分者2904输出；可重提但次数预算未说明。总体text .35/multimodal .31，Qwen相反；不是模态普遍安全排序。评分者不是独立prompt样本，分模型alpha及ASR口径和评级计数转换边界保留；D.1 Pixtral 4.27与TableD1 4.67不合并或判断失实。没有统计复现、生产安全率或实现验收。
- 16107实际§3.1–3.6、§4.1–4.3、Limitations、AppendixD全排列反侧：52/227样本、8关系、DeepL翻译非英语；clarification默认正确、hedge至少提一实体可正确，answer attempt须全positive；correct不等direct。judge仅一作者500英文对照，DPO1388对单次训练大量迁移为澄清/hedge，不等直接求解。固定次序与全排列差额、单suffix及翻译局限保留。
- 16241实际Algorithm1/Fig2、§4.1–4.5/§7/Table2/§9：人工运行与预先正确答案oracle筛失败题再推理/重生成；Fig2迭代至正确而Algorithm一次额外阶段预算未统一。8bit并不证明总成本小，265混合题整体90.15与Table2 MATH89.96不同分母，硬件/长度/重试统一预算缺失。作者恢复最小oracle/资源评价边界通过，不采无oracle自主解题、解释忠实或形式证明能力。
- 15896实际§5–6：安全反侧归属先前Chiang/Lee、Xu、Wu等研究；本稿心理框架/未来机制建议未给本次可核新机制或条件对照，维持贡献关闭而非否定所引安全现象。15560完整题摘为观点/认知解释，未给新模型机制或条件对照，维持关闭。
- 15839原“物理benchmark范围关闭”撤回。实际§2.2/Fig2与§3为通用多模态模型评价反例：Claude4-Sonnet错误假定加速度/力方向却得到正确终答，终答正确不保证推理步骤正确。只恢复该最小局部潜力，不启用AI for Science。Gemini2.5Flash逐步judge未经人核、ASA/ASC名称混写、公开考试污染/移除图也移除必要信息，不将ASA解释为隐式推理忠实或图片普遍提升。

## 有界 cross-list 查漏

同一CL月表ID15400–16300主段52标题之外，实际检查cross-list同段17标题；12相关/含糊取得并完整读精确v1题摘，原输出在[INDEPENDENT_CROSSLIST_ABSTRACTS.json](./INDEPENDENT_CROSSLIST_ABSTRACTS.json)。不扩2214全文或其他日期。另5明确领域/社会应用标题15473/15957/15986/16224/16295关闭范围，连同原主段5标题与系统medical15844共11个标题级范围关闭，不计完整题摘分母。

| v1 ID | 准入最小潜力或关闭依据 |
| --- | --- |
| 15540 | 双向text/image解码、mixed-scale masked建模处理图文局部/全局计算权衡；不从F1小增量授通用能力 |
| 15561 | deterministic轨迹摘要TCS代原训练trajectory供小LLM，10-trial HPT局部预算比较；GPT4总成本/可靠性仍待核 |
| 15661 | vision teacher audio-focused CoT经audio-grounded过滤，再SFT/GRPO给audio student；teacher预算、过滤漏误与泛化待核 |
| 15676 | query-specific预测error surrogate近似submodular+kernel/optimal-design多样性；线性LLM假设不能外推全部LLM |
| 15692 | 截断语音/部分译文自增广缩小offline到streaming分布差；1%数据不等免费翻译或零延迟 |
| 15969 | 单调phoneme/audio对齐、动态lookahead和分层流式TTS，102ms为局部GPU报告非部署SLO |
| 16060 | 白盒forward跨层残差绕安全变化与能力损失的明确测试机制；见下方必要反侧 |
| 16163 | CLIP表征低秩分解/重建防PGD，rank/残差/层数安全成本取舍；见下方必要反侧 |
| 16189 | oracle retrieval复用经历缓解reversal/navigation及within-example ICL条件；oracle不是现实检索验收 |
| 16197 | shared vision encoder+continuous/discrete双adapter与AR semantics/diffusion pixels兼容理解/生成；需核任务冲突/训练budget |
| 16244 | 完整题摘仅PEFT/QAA综述和比较方向，没有给本稿具体新增机制、实际条件对照或反例；贡献关闭，不以量子领域关闭 |
| 16297 | 十二LLM长提示产生模拟self-preservation的局部行为潜力；哲学类别/架构必然幻觉与真实生存意图均未证明，不采宣传结论 |

16060实际v1§3–6/§8/10及Table1–4：[原核心](./INDEPENDENT_CROSSLIST_SAFETY_CORE.json)、[结果/限制](./INDEPENDENT_SABER_RESULTS.json)。41 harmful+41 benign验证/159 harmful测试，4个7–13B模型、classifier ASR，修改forward的白盒权限，不是黑盒远程攻击。额外“Sure, here”、是否删除system prompt影响大；51是特定Llama2-7B的百分点差，不是全模型相对提升。HarmBench验证/测试classifier及输出长度不同，Mistral最佳baseline AutoDAN93而GCG88，SABER93.1仅0.1高于真正最佳；KL最后token/随机pair选择不能证明整体能力无损。Table4 MMLU等确有下降（L2-7B 13.88pp），PPL小变化不覆盖reasoning。保留局部威胁机制潜力，不采因果唯一安全层或部署危害率。

16163实际v1§3–5/7：只有CLIP ViT-B/32、COCO/Flickr30K、PGD10步eps8/255；3000pair评价、1000pair参数分析，无adaptive攻击证据或其他VLM验证。Table1单层rank64 TT1.22x与五层TT3.93x不是同配置；最佳19.8/11.9恢复不配“22%成本”概括。rank/alpha局部选择与高频解释非因果机制保证，未核实现/硬件/SLO，日期隔离。

最终完整v1题摘65＝62潜力（原50+15839+cross-list11）+3贡献关闭15560/15896/16244；另MiMo潜力1及11标题范围关闭。正式候选/证据完成/Books写入均0，不是0事件。原53包/49–50计数保留历史，不覆盖反证。

## 官方事件与14源实际停点

Google本日20core1完整Blog核心与July2507.16075v1题摘，本轮再窄核旧v1§2–4/Implementation/results/ablation：[INDEPENDENT_TTD_CORE.json](./INDEPENDENT_TTD_CORE.json)。draft/search/revision/self-evolution、ADK、20steps、74.5及7.7/1.7结果在旧版，Blogavailability一句未披露新的执行/兼容/安全约束；关闭本次再阐述，不否定旧贡献或自授旧论文深审。不同LLM基线不可归因单组件；Blog消融4.4/1.2口径不能替代旧表格。不把日期仅Sep19当精确落窗。

MiMo实际Demo/README25Hz/8RVQ/patch4→LLM6.25Hz→delay25Hz及本日5commit身份，最早00:48:29Z、次01:05:50Z分处下界前后都不是首次public。8557完整Blog15标题/描述无date、6159实际slice8+7同数组无网络More待办，历史缺段仍外部隔离；不带入December研究。

实际检查本日FETCH/原恢复请求及14源关键原字段/停止：RSS1247本窗0；Anthropic重试172 publication、Sep15/5夹下界（唯一日期数166不等publication条数）；Qwen60有限date夹窗；DeepSeek Sep29/22/Aug21；Kimi Sep16/5；ERNIEpage2 Sep12/Aug14；MiniMaxUS12/CN13/Agent2026；Hunyuan9原displayPublishTime最早1770090898为2026；ZAI18无序minDec7/hasMorefalse；Seedtype2有限15/49跨下界（置顶单列），type1真正0/20/40/60/80至has_morefalse，total94列表缺段保留；Google九月页12条至Sep11/DeepMind当前2026、Metareset补检空均不授历史0；MiMo如上；arXiv主题429真实14字节/system7有限发现/月表2000/2214仅当前有界段，new?date实际2026忽略历史参数；HF20实际web失败/curltimeout0、不是继承他日。停止来源普通分页已执行，不把普通未读当外部终态。

## DAY

六部分闭合；普通待办无。终态保留项：62潜力及MiMo缺原first-public或完全落窗区间；Google/Meta/Hunyuan/ZAI/Seed论文/MiMo历史缺段。原作者公告、官方历史公开artifact或真实分页/日期归档到达，仅重开具名家族日期/必要证据或缺段来源，不重扫库存。终态不支持正面Evidence、Books采用或无遗漏断言。没有Books采用因而无owner POST写入义务，不声称既有Books覆盖；正式日期恢复后再走分数、必要证据/owner路线。

结论：通过

验收仅本日有限来源、贡献筛选、必要风险与最终格式语义；未复现统计、GPU、实现或全部全文。同步后实际V3校验及限定本日diff-check均通过，机器检查不替代本结论。
