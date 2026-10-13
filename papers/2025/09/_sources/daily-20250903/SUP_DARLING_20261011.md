# 2025-09-03 DARLING自然日事件与必要证据交接

## 1. 身份与日期，待root定点裁决

旧02534题摘潜力与旧日期字段不改。新请求[Meta官方出版页](https://ai.meta.com/research/publications/jointly-reinforcing-diversity-and-quality-in-language-model-generations/)实际全题摘/作者/日期为September2,2025；results6具名邻接Sep08→Sep02→Aug22。由本页真实Download the Paper链接取到[官方PDF](supplement-20261011/meta-darling-paper.raw)，29页，物理p1同题同作者、Date September2,2025、官方darling repo，属同02534家族，不另计家族。

官方日级标记可以支持其Sep02论文公布事件；不使用页面抓取日、arXiv submitted或PDF CreationDate倒授首次公开。当前页没有另披露本地时区，不能新增公开时刻；PDF metadata CreationDate是生成时间不是发布。拟按用户新完整自然日门单独追加resolution，不能重算冻结旧行；究竟足以认定本次官方正文公开日由root独核，不先写正式入选。本日原51日期hold仍是历史数量而非此处已解决的现状。

## 2. 实际必要证据与关键反侧

作者完整读物理pp1–10（初次混排截断的p2后来单页完整重读），限§1–6.3与相关Tables1–4，不读其余19页/代码。准入为质量-only RL会压语义多样性→learned equivalence partition与quality相乘进入online GRPO→重新考虑语义/词法diversity、reward尺度与探索；拟2+1+2=5，不能以厂商/排名或已有知识基础加分。

§3.1 Eq4平均pairwise distance，紧接定义classify=1(semantically equivalent)，却写d=classify；Figure2与文字按“不同”的数量给2/3或3/3。距离方向存在原文冲突，不能照录Eq4为可执行reward配方。§3.2乘法并非单独机制因果证明：还改token-level averaging并移去std normalization；§6.3解释dense noisy reward下normalization放大噪声，不授所有binary verifier无噪声。

非verifiable设置Llama3.1-8B/3.3-70B、10k WildChat、Athene-RM-8B、32/64 prompt×8rollout、max1024；quality用GPT4o/Claude3.7 judge，不等真实人类质量。§4.3相近ELO的rubric显示instruction following/world atmosphere弱于originality，不能写全方面最好。Math Qwen3-4B/14B、10k DeepscaleR、Math-Verify、n256估pass@k，pass@k不是语义多样性独立测度或无污染证书。

§6.1 Table2乘法不在全部quality子项胜加法（creative writing68.8 vs69.2、hard prompts31.1 vs32.7）；§6.2 Table3 4gram在部分quality高于partition但semantic Distinct较弱。§6.2 Table4 lexical奖励平均pass@1 22.49低于quality-only23.40，DARLING26.91；作者观察异语或难度反思的reward hack，只支持该设置。未核附录完整配置/多seed/硬件precision/额外classifier训练与全训练费用，均Not Disclosed于当前审阅范围，不授端到端优越、复现或生产能力。

## 3. 当前Books比较与需要root的精确决定

已实际读取TRAIN-GRPO Ch33“Group Size只有在样本身份独立时才代表探索”正文704–738附近：相似度进入reward是改变目标不是恢复有效样本数，embedding/reward尺度/组内比较费用、原correctness/fresh group回退；质量gate后n-gram diversity并非语义真值也已承载。这里能复用相关原则，但没有声称已覆盖DARLING learned partition或乘法recipe。

拟只报告实验边界/原公式冲突，不新增厂商实例；如root认定lexical与semantic reward失效这一局部验证需稳定owner增量，则由root协调唯一Books写入与非writerPOST。当前不授已有覆盖，不以Books已有主题关闭贡献，Eq4方向和未核同预算禁止采用精确实现或普遍quality/diversity因果保证。root可立即裁决日级事件/评分/受限Evidence及Books，不等待其余arXiv题摘；未完成独核是普通工作。

## 4. root纠正处置与具名官方代码恢复

root实际官方页与PDF pp1–10/p3渲染通过Sep02自然日正文公布resolution（同02534家族不双计）、2+1+2=5；中心Eq4方向未定时应审阅争议/Books暂缓，不用仅报告绕过。上述§3是历史提议，被本节覆盖。旧02534日期行/旧51历史分母不改，必要core已读不等完整Evidence。

按用户具体要求，作者没有将未读code伪装外部缺失：PDFp1链接[官方仓库](https://github.com/facebookresearch/darling)，实际仓库metadata/contents、仅reward文件path commit列表均200，保存darling-repo-metadata/contents、darling-reward-contents/commits原件与requests。仓库created_at=2025-09-14T01:10:53Z；reward文件只有1条commit，[c07a3238a8b4a9f07c9272f823b23d5e1c47f99b](https://github.com/facebookresearch/darling/commit/c07a3238a8b4a9f07c9272f823b23d5e1c47f99b)，author日期Sep14 05:24Z/Initial commit，当前该path blob=0812ac794395de702ab93191d514441f6b839f71。没有用main可变HEAD作精确证据，实际下载[固定commit消费函数](https://github.com/facebookresearch/darling/blob/c07a3238a8b4a9f07c9272f823b23d5e1c47f99b/verl/verl/utils/reward_score/partition_reward_vllm_serve.py)，本地[darling-reward-initial.raw](supplement-20261011/darling-reward-initial.raw)。

实际读lines47–184/219–252/350–403：equivalence_check返回similar prob>threshold（短文本unigram shortcut）；same为True时union；partition用(total_for_uid−len(grp))/(total_for_uid−1)，floor0.1；partition_correct只对correct responses取分区外数/正确数−1，≤1 correct回0.1。因此当前官方artifact消费方向是different partition奖励更高，与Fig2/正文相符，不能照录Eq4的d=classify。它还通过transitive closure分组及floor，而非直接逐pair classify，不能只把符号翻转声称完整对应。

这澄清官方实现意图，但目录未给Sep02精确训练recipe/classifier snapshot与此Sep14 commit的对应说明；未运行、未核模型class label/所有训练consumer，未遍历code。交root判断是否足以收窄争议；若仍暂缓，具体重开材料仅作者对Sep02公式方向/实际partition配方与固定实现版本的对应说明，不索要全源码，不以代码后发改变论文Sep02日级归属。

root随后实际独读同固定commit lines47–184/219–252/350–403，认可官方实现意图为分区外奖励，但Sep14 artifact不能证明Sep02配方一一对应。最终单篇处置为同02534家族Sep02 resolution、2+1+2=5、争议/Books暂缓；日期条件已通过，不因代码后发撤回。有限实证观察保留，不称中心配方或因果已证，Eq4不能照录。重开仅需Sep02公式/recipe到固定实现对应澄清，不继续扩大code、全部源码或全文，报告已同步，不自授日级DAY。
