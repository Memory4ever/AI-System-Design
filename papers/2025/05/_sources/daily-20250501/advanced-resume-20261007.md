# 2025-05-01：Advanced Search 增量发现

作者：root；2026-10-07 恢复批次，首请求响应Date为08:40:49 UTC（16:40:49北京时间），记录整理至17:14。新增材料仍只检查2025-04-30；旧22候选不改日期、评分或有效证据。未调用catchup。

## 查询与实际停止

原件位于 [supplement-20261007](supplement-20261007/)。实际GET `https://arxiv.org/search/advanced`，参数如下；没有指定分类，实际是全分类的具名主题检索，含范围外噪声：

```text
advanced=
terms-0-operator=AND
terms-0-term=language model
terms-0-field=all
terms-1-operator=AND
terms-1-term=inference
terms-1-field=all
classification-include_cross_list=include
date-filter_by=date_range
date-from_date=2025-04
date-to_date=2025-05
date-date_type=announced_date_first
abstracts=show
size=50
order=-announced_date_first
```

`advanced-resume-inference.raw/.headers`实际HTTP200、Showing 1–50 of 446 results，50行完整。作者按10项一批实际读了全部50份完整题摘及可见日期/Comments；不是只下载文件。列表给出originally announced April 2025，不能据此授权Apr30，也不能以当前版本正文回填2025初版。首屏含旧重复WebEvolver的Apr22提交；去掉6旧重复后新44行v1提交从Apr30到Apr23。只作靠近目标日的有界查漏，停止50行，不把其余396项变成逐项队列，不授446项已筛或当日召回。另有四主题邻近提交API与有界分类月表补检，范围见[原记录](supplement-20261007.md#arxiv入口错误及有界恢复)，数量不叠加。

`advanced-resume-april-inference.raw/.headers`改为Apr01～Apr30，HTTP200实际0结果；`advanced-resume-april-cs-inference.raw/.headers`同日范围附加`classification-computer_science_archives=all`仍0。该附加字段并非已核表单的CS勾选`classification-computer_science=y`，未证明分类过滤生效，不能称成功计算机分类检查。与月范围446不一致，只记录日期粒度/入口异常，不把0作为当日或月内无论文证据，不声称已证明网站的日期计算实现。`advanced-resume-form.raw`核实announcement选择只提供年月，Submitted Date与Submission Date (original)另有字段；不能把后者改名公开日。

## 去重与准入待复核

50行中6个身份已经在本日原候选：2504.21668、21463、21318、21303、21036、21024。只复用原有效审阅，不搬日期或重复计分。17:15定点打开[RWKV-X当前官方abs](https://arxiv.org/abs/2504.21463)，实际读题摘、Comments及Submission history：v2为May9，Comments只有“12 pages, typos corrected”，没有说明改变哪个机制、公式或评价。检索页的latest submitted May8与abs不一致，二者都不充当公开日。该标签不能自行证明重要修订，也没有可支持扩大旧采用链的具体变更；不遍历全版本史，不把后版替换旧精确v1证据。若以后出现影响采用命题的具名勘误，只重开该项。

其余44项最初为34潜在/待判、10拟关闭；Archimedes全部题摘校准并定点读9项决定性core后，重开新闻/截图评价反侧两项，关闭一般IFC理论一项，现为35潜在、9关闭。不是44个新当日候选。未确认具体公开日的潜在贡献不评分、不列正式候选、不进入Books。以下采用校准后的最小增量及边界；完整core位置见[非作者记录§8](review-resume-20261007.md#8-决定性定点阅读与负侧改判)，未授全部方法/实验审阅或性能保证。

| 身份 | 保留的具体问题与增量 |
| --- | --- |
| [2504.21831](https://arxiv.org/abs/2504.21831) | DEEVISum的多阶段蒸馏/提前退出改变VLM质量与推理预算取舍；不因小规模实验关闭。 |
| [2504.21659](https://arxiv.org/abs/2504.21659) | Ada-R1按问题选择长短推理风格，组级风格偏好与组内实例偏好分层；不把长CoT恒有益作为先验。 |
| [2504.21553](https://arxiv.org/abs/2504.21553) | 投影层集中activation spike使模型专属混合精度可能优于统一outlier处理。 |
| [2504.21538](https://arxiv.org/abs/2504.21538) | Coyote v2的hls4ml编译后端及host流式模型执行路径已由v1 §2.2/3/9.7确认，直接连接成立；基线数据复制与控制语言不同，不把倍数归shell单因果。 |
| [2504.21380](https://arxiv.org/abs/2504.21380) | Sparse-to-Sparse从头训练稀疏扩散网络，而非仅做推理后处理；保留训练预算/质量边界。 |
| [2504.21330](https://arxiv.org/abs/2504.21330) | 对学生人口属性的可识别性与打分偏差相关的反侧；不因教育场景关闭评价混杂证据。 |
| [2504.21266](https://arxiv.org/abs/2504.21266) | CoCoDiff v1 §IV-A～D明确fine描述逐步去噪、coarse类对比约束，生成GCN特征仅用于训练增强；表示条件分路成立，收益消融未审，不称推理架构优化。 |
| [2504.21239](https://arxiv.org/abs/2504.21239) | 每记忆LoRA与门控路由为连续知识注入提供隔离/复用选择。 |
| [2504.21174](https://arxiv.org/abs/2504.21174) | AMP结合head和MLP结构剪枝；需核非独立组件的质量/计算取舍。 |
| [2504.21043](https://arxiv.org/abs/2504.21043) | CodeBC用安全标签的对比学习减少pair依赖；保留安全机制反侧，不因智能合约场景直接关闭。 |
| [2504.20922](https://arxiv.org/abs/2504.20922) | DYNAMAX的动态退出覆盖Transformer/Mamba，须核停止判据与质量代价。 |
| [2504.20835](https://arxiv.org/abs/2504.20835) | 半隐式跨语言CoT把高资源语言instruction能力向语音非核心语言迁移。 |
| [2504.20752](https://arxiv.org/abs/2504.20752) | Grokking in the Wild用合成事实关联分析多跳推理与记忆，保留学习/泛化边界。 |
| [2504.20493](https://arxiv.org/abs/2504.20493) | 压缩注入导致reasoning停止是安全失效路径；当前官方abs与完整题摘已轻读，尚非攻击机制深审。 |
| [2504.20414](https://arxiv.org/abs/2504.20414) | LLM合成邮件补攻击先验使SSE leakage攻击依赖更少真实语料；安全反侧保留，非仅“AI生成数据”类比。 |
| [2504.20271](https://arxiv.org/abs/2504.20271) | task-specific probe与SAE/zero-shot activation monitor的可比边界及OOD监控。 |
| [2504.20196](https://arxiv.org/abs/2504.20196) | AutoPrompter v2 §6.1～6.3明确识别缺信息并在不确信时请求澄清；33个不满意样例9个改善不是普遍正确率增27%，v2事实不回填2025初版。 |
| [2504.20039](https://arxiv.org/abs/2504.20039) | AutoJudge将损失性speculation与judge结合，区分放宽目标分布的速度/质量取舍和exact验证。 |
| [2504.19898](https://arxiv.org/abs/2504.19898) | GenCLS++分析SFT/RL及显式思考对分类的不利结果，不能只按新任务目录排除。 |
| [2504.19739](https://arxiv.org/abs/2504.19739) | AffectVLM v1式1～2的共享多视角对比/三元组及可学习margin是可核训练目标；未认证“gradient-friendly”、收敛改善或DDP扩展性。 |
| [2504.19724](https://arxiv.org/abs/2504.19724) | RepText把文字渲染与语言理解分开，用glyph复制测试语言无关生成边界。 |
| [2504.19483](https://arxiv.org/abs/2504.19483) | residual control vector干预reasoning表示，须区分正确率与概率估计、相关与因果。 |
| [2504.19457](https://arxiv.org/abs/2504.19457) | 长上下文hallucination数据及BERT分解/聚合架构，改变评估器长输入可行性。 |
| [2504.19449](https://arxiv.org/abs/2504.19449) | R-Sparse组合输入通道与权重奇异值逼近，避免active-channel predictor；质量与kernel成本待审。 |
| [2504.19342](https://arxiv.org/abs/2504.19342) | 动态context、相关偏好样本的regret/估计理论；医疗解剖只是例子，不关闭理论。 |
| [2504.19327](https://arxiv.org/abs/2504.19327) | DeepInsert让多模态token从中层进入，利用跨模态交互发生位置；分子任务切片不采用。 |
| [2504.19146](https://arxiv.org/abs/2504.19146) | Muyan-TTS v1 §3.1/4.2.2～3/6给出整段G2P不支持stream、speaker SFT音色收益伴WER恶化及文本格式依赖；速度表关闭句子并行，预算/开源不单独准入。 |
| [2504.19023](https://arxiv.org/abs/2504.19023) | GLaMoR v2 §III-A/VI-A～C的local/global三axiom cycle对照与复杂量词模式迁移建立感受野/泛化潜力；预测准确率不是sound checker，v2不回填v1。 |
| [2504.18884](https://arxiv.org/abs/2504.18884) | ensemble与单次大模型的稳定性/预算反例，需控制采样次数和成本；不因简单方法关闭。 |
| [2504.18839](https://arxiv.org/abs/2504.18839) | compact monitor→larger-model escalation的校准/成本条件，不把模块组合本身当贡献。 |
| [2504.18715](https://arxiv.org/abs/2504.18715) | 空间语音翻译保留方向/说话人并满足实时边界，属于多模态感知与运行时联合约束。 |
| [2504.18673](https://arxiv.org/abs/2504.18673) | 第三方情绪标签不等于第一方私有状态的反证，影响数据/评价代理。 |
| [2504.18583](https://arxiv.org/abs/2504.18583) | PARD共享draft适配和并行预测，COD依赖prefix KV完整性；当前版本不充作Apr2025初版方法。 |
| [2504.21165](https://arxiv.org/abs/2504.21165) | Manicod v1 §3/7实际承认新闻真值错误、网页证据互相冲突与同URL内容变化；历史搜索日期不冻结历史内容，改判保留RAG评价代理反侧，不认证检测器。 |
| [2504.18912](https://arxiv.org/abs/2504.18912) | Programming screenshots v1 §IV/VI指出截图与原问题可能不对应，图像相关性和原问题匹配测不同目标；改判保留输入欠定/评价混杂，不等同代码修复正确率。 |

| 身份 | 校准后关闭的具体理由，日期不再追查 |
| --- | --- |
| [2504.21522](https://arxiv.org/abs/2504.21522) | 无限逻辑/测度概率公理理论，题摘未提供模型学习、表示或系统机制的直接连接；不是仅因理论而排除。 |
| [2504.21390](https://arxiv.org/abs/2504.21390) | 一般event-log随机过程发现与statistical model checking，未指向模型训练/Agent执行机制。 |
| [2504.21344](https://arxiv.org/abs/2504.21344) | 临床肺结节CLIP特征与恶性预测应用，属于暂缓医疗研究切片。 |
| [2504.20732](https://arxiv.org/abs/2504.20732) | 量子程序Bayesian语义，当前不直接支撑大模型学习/运行机制，量子研究暂不引入。 |
| [2504.20628](https://arxiv.org/abs/2504.20628) | 使用LLM程序表达人的认知地图及心理实验；当前增量为人类认知建模，不是模型形成world model或Agent闭环机制。 |
| [2504.19720](https://arxiv.org/abs/2504.19720) | Taming Titans综述分类实例放置、请求调度、长度预测、存储/PD与cluster负载平衡等Serving优化，完整题摘未指出新失败边界、可比反证或评价混杂；纠正先前“训练/量化”概括。 |
| [2504.19467](https://arxiv.org/abs/2504.19467) | 临床文本benchmark，当前暂缓医疗应用切片，不据模型榜单推一般能力边界。 |
| [2504.19021](https://arxiv.org/abs/2504.19021) | 既有PLM与hard-voting组合改善科学文本分类，没有新模型/系统机制或明确纠错证据。 |
| [2504.20432](https://arxiv.org/abs/2504.20432) | v2 §1～2是Viaduct一般标签推断、非对称delegation与MPC/区块链principal，没有模型/LLM Agent执行直接连接；不是因形式理论排除，日期不再追查。 |

以上校准由Archimedes独立完成，作者据其具体core/反侧落实三项身份改判和理由收窄；原始拟判及证据保留在review，不覆盖原件。作者完整题摘实际读取50、额外官方abs轻量恢复20493/20414/RWKV，非作者另读9项必要core，不宣称全部44方法核验或精确v1重审。可见Comments已读，无撤回标签不能证明版本永远有效。

## 下一步

作者READY（17:44检查）后的写回差额由Archimedes实际核验，已给出[最终日级通过](review-resume-20261007.md#12-1746-authorready-写回验收与-day-最终裁决)；17:50 root同步日报完成态。普通待办无，35日期线索及具名历史缺段保持外部终态隔离，不重审未变23候选或无界月库存。

外部保留：具体公开日需当期官方日公告/目录或作者明确首次公开记录。只接受日历日期，不要求时分秒；月公告字段、提交日及current-version题摘不授权Apr30。新身份未入正式候选、未评分、未进入Books，不支撑无遗漏或性能结论。

17:13左右再作三项有界日期恢复：`"Ada-R1" "April 30" 2025`（github.com/huggingface.co/arxiv.org）、`"Precision Where It Matters" quantization "2025" "April"`（github.com/arxiv.org）、`"MiMo-7B" "2025-04-30"`（mimo.xiaomi.com/github.com/huggingface.co）。未得到作者明确首公开日；MiMo返回lvwerra/yuxiaopeng等第三方日报与后续综述，位于HF/GitHub不等于原作者日期权限。结果不作零论文、不采用其中模型能力宣传、不改变冻结旧日期。停止这些具名一轮补检，保留精确原始发布需求。
