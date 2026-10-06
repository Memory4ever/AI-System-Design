# 2025-11-17 非作者独立复核

复核者：Codex 主线程（root）；作者：Carver。实际检查时间：2026-10-04T20:33:51+08:00。

结论：通过本日准入边界、必要反侧、有限来源及六部分；作者仍须同步本结论与完成态并执行最后格式检查。本记录不证明所有历史来源已恢复，也不授65个日期保留项全文、性能或Books采用通过。

## 实际范围

恢复后重新读取AGENTS、研究合同、Report合同、Sources使用说明/每日/按需/arXiv主题、Prompt、ROADMAP及本日[FIRST](FIRST_CALIBRATION_READY.md)、[筛选](SCREENING.md)、[来源](SOURCE_REVIEW.md)、[日期](DATE_REVIEW.md)、[停点](STOP.md)和正式六部分。窗口BJT `[2025-11-16T09:00:00+08:00,2025-11-17T09:00:00+08:00)`；只核本日材料，不从其他日期继承候选或Coverage。

亲读31份exact-v1完整题摘：12638、11505、12309、11831、12414、11445、11922、12693、12614、11885、11810、11111、11628、11719、12712、12497、12487、12381、12149、10899、10909、11601、11733、11313、11520、11993、11334、16688、11510、12635、11612（以上前缀均2511）。不是84份题摘全量独立重读。首5的具体增量和保守边界通过；CALM的半结构additive forward及HEDGE的通用VLM不确定性条件可留潜力，不因临床实验自动排除，也不采临床结论。其余日期保留项没有正面采用，不要求全部methods/owner展开。

## 必要安全与设计反侧

直接读取以下精确v1 HTML的受影响位置；[原文定位](ROOT_CORE_MAP.md)仅辅助定位，不代替本轮亲读。

- [Sure Trap](core-2511.12414v1.html)：§IV-A模型/单judge、§IV-B/C触发与无害续写分离、§VII限制。高Sure率不等高unsafe率；开放模型、GPT-3.5及纯benign分支不能合并为统一阈值。所谓latent gate是行为解释，未识别内部电路、未实现全部防御/认证，不授确定性tool控制。
- [AFM](core-2511.12712v1.html)：§4比较/设置/Table1/消融及§5.4。只一个短和中对话参考run；温度/预算不齐，无正式人评或系统消融。摘要66%与正文CSR的stateless基线不同于naive replay，外部embedding/compression调用也不能说成零额外成本。不采普遍安全或端到端延迟保证。
- [SGuard](core-2511.12497v1.html)：§4评价对象/指标/消融及Limitation。EN/Korean、训练风险taxonomy、8k建议、低资源语言/新攻击误判限制保留，base支持12语言不证明guard十二语言安全。
- [ToxSearch](core-2511.12487v1.html)：§3实验设置/统计与§5限制。固定100题、10run、量化模型和Perspective toxicity proxy约束，转移衰减及refusal成本不能抹掉，不等所有危害类别或线上攻击成功。
- [White Bear](core-2511.12381v1.html)：§2设置/§3结果及A限制。英语single-token模板/logprob不等完整生成行为；GPT-OSS反例不支持单调规模规律。电路段与未来工作措辞存在张力，不能把局部head干预提升为已经可靠的防御。
- [AttackVLA](core-2511.12149v1.html)：§4.1三模型/LIBERO、实体Franka平台、三种ASR与clean performance及§4.4/5对象。静止、任务失败、目标轨迹成功是不同指标；模拟与物理验证不合为通用安全率。
- [TIM](core-2511.10899v1.html)：§4设置、§5手审过滤/§9限制。54.3%来自筛出的高风险top-10/model，不是全部工具请求；Code Interpreter与GPT-4.1缓解范围不外推其他tool。正确答案、工具执行和论证有效性分开。
- [MMA-Sim](core-2511.10909v1.html)：§III-A测试式模型、§V comparative validation、§VI-B/C dynamic range/rounding。bitwise对照实验不是任意输入形式完备证明；CDNA2/3与具体指令差异不授所有跨平台模型不稳定。
- [Mind the Gap](core-2511.11601v1.html)：§IV-A设备/算子/随机模型、§IV-B异常值/undefined与§IV-C/D编译/validity。随机图、单设备及特定runtime条件，不把无定义行为差异全计为错误，也不当分布式LLM端到端质量测量。
- [DSD](core-2511.11733v1.html)：§2.3松验收、§3.1/2四至八A800节点、batch1/top-k1/三seed。task accuracy保留不等exact target distribution；正文对标准speculation的概率相等描述不能当通用算法定义。
- [DocSLM](core-2511.11313v1.html)：§3.2分段预测/entropy/Not Answerable、§5模块取舍及§6。常数显存不证明任意长文联合推理完备或拒答保证，分段校准不等完整历史信息无损。
- [Video Policy Evaluation](core-2511.11520v1.html)：§IV-C Bridge及追加300轨迹、§IV-D物体幻觉/多视图/累积误差/VLM annotation。相关性和policy ranking不替物理验证；65–80%标注准确度不是安全证书。
- [LLM4SCREENLIT](core-2511.12635v1.html)：§2.3不均衡/非独立指标和§3.4/4的convenience sample、单人抽取、FN成本。Lost Evidence与完整confusion应保留；不把WMCC写成无偏性万能保证或全领域定律。
- [HPC scheduling evaluation](core-2511.11612v1.html)：§3.3/4评价、人工最优与调prompt过程。单任务可行mapping不等依赖/时间正确；探索后prompt选择与API结果不证明一般规划能力或失败率。

以上14项只获得不误用关键反侧的权限，没有因日期hold采用性能、训练或安全结论，没有声称所有方法/附件、代码运行或复现实验完成。

## 分层关闭与唯一局部裁决

完整题摘关闭抽样10项：教育11445、IoT FlashFusion11885、Markov观点11810、Dragonfly surrogate11111、OS scheduler11628、edge分类11719、CV攻击11993、LaoBench11334、prompt values16688、OpenUS11510。分别按实际教育/领域预测或组合增量/概念论证/通用评价条件不足判断，不按小模型、理论、负面结果或综述名称自动关闭。CV攻击的安全信号已核AB，未发现本项目foundation/LLM直接切片，不授该攻击全文结论。原18个AB关闭不是全部由本轮独立全量核验。

[OPFormer](core-2511.12614v1.html)另读§3.1、§3.2.2和Appendix B限制，参照[消歧](OPFORMER_CORE_DISAMBIGUATION.md)：确有NOCS三坐标分块RoPE/跨template机制，不能称没有新模块；但其训练/验证仍为已知几何条件下6D pose correspondence，未给一般模型形成、语言动作或世界预测的新条件。本轮范围关闭通过，不是因frozen backbone或没有owner。漏斗改为65潜力、19关闭（原18加此1），不再请求它的日期。

标题关闭分层抽检原API四项：QPU stencil12617、molecule12770、phishing classifier12085、MoCap radar11462，分别量子、暂缓科学、领域分类和特定雷达合成。只核相关标题，不冒称21全部AB或全学科召回。

## 来源、日期及六部分

实际解析本日原RSS1245条/原pubDate邻接；Anthropic Flight1/0Tframe、172去重dated身份及Nov12→21字段；Google两原News页November邻接、Gemini3原JSON-LDNov18 16Z和SIMA原webNov13、pubs/Meta失败receipt及真实有界query输入；Qwen旧5卡/新壳；DeepSeek真实Research/news10研究及5动态；Kimi原26项；Hunyuan本日browser失败和API9个2026字段；Zai p1/p2真实可见15/18与终页；Seed四JSON全部74题名/PublishDate/pins、原请求/next/has_more；ERNIE真实p2六项/终页；MiMo Paper8/Blog15全已返回且button无日期；MiniMax EN12/CN13及独立Tech原MD/索引；arXiv四窄XML/receipt实际52/16/3/26和model尾2、csDC限定标题定位。没有遗漏每日ID、跳过Tech或扫描Weekly。

辅助query实际输入、首页/有界停止可核；一次错site布尔查询后的官方domains补检，不等原目录已恢复。Hunyuan成功API不代2025UI；MiMo已返回15标题，无需把无日期问题包装成无限More分页待办。七来源历史缺段具名安全隔离，通过的是处理边界，不是受阻Coverage。

本日原availability的Sun20EST是终点Nov17 09BJT，故不在窗内；不补造具体公告或作者首次公开时刻。实际逐项查看潜力DataCite v1日期类型与值（含两retry和January ID），都是Submitted/Updated/Available月/created，不是首公开；跨截止上界不能反过来证明窗外公开。具名有限日期恢复已到原件不足处，65项按ID重开，不枚举社媒/全部作者附件。当前Atom comments轻量查无withdraw/retract/correct/error信号，不认证全网站版本史。

正式六部分通过当前有限采用边界：105发现不是当天论文，84作者题摘不是84本轮独立全文，0确定候选不是零研究；空五列表头、Books纳入本次且写入0、终态限制与普通作者同步分开。没有可以正面采用的当窗证据，因此Books No Change通过，不声称全部owner已有覆盖。作者同步本结论、65/19计数及有限arXiv处置后只核变化，不重做已过原件；最后完成态格式检查尚由作者/root执行。未stage、commit、push，未写共享Books或其他日期。
