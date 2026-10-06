# 2025-10-02 日级独立复核

复核者：root / Codex，非作者Huygens；保持当前模型。
对象：本日README、SCREENING、FIRST_CALIBRATION、CORE_BOUNDARIES、GOOGLE_RECOVERY与SOURCE_REPAIR及实际原件。
窗口：`[2025-10-01T09:00:00+08:00,2025-10-02T09:00:00+08:00)`。

## 结论与适用范围

**研究处置通过；作者尚须同步完成态及明确终态保留措辞，再做写后检查。** 正式候选0不代表零研究；81论文及1个Google公告的公开日界仍不确定，不评分、不作为正面证据、不进入Books，也不授无遗漏或安全保证。没有待作者补读全部85论文/年度库存的要求。

鲜读AGENTS、研究与Report合同、Daily来源使用/十四源/arXiv主题边界、Prompt、ROADMAP及本日停点。只处理本日；01 RSS仅用于七个精确案例的日期纠错，不读01候选池。已通过的首批六项原abs及版本史复用FIRST与ROOT_FIRST_AB1/2，不重复同样附件。

## 准入、日期与范围

实际核题摘的范围为首批6项，加原Atom的Semantic-Driven AI Agent Communications、Agent Fine-tuning in Microdomains、Memory-Augmented Log Analysis三项，合计9项；其中4项明确贡献排除均已独立核验。Cookbook整理既有构造，另三项当前摘要没有给出足以改变模型/通用系统设计的具体增量；不是因理论、微领域、小模型或安全应用名称一概关闭。其余76份题摘没有全量重新核验，不称85项独立全文验收。

首批GUI-KV、PAL-UI、M2PO、Priming、REAL-MT的具体潜力成立；不由主题映射或单数字准入。完整Google原HTML另读Training、Teacher、Distillation、Prompt generation、High quality vs low latency、Image-size mask upsampling：固定图像的重encoder一次、提示依赖轻decoder多次、gesture结束后高分辨率上采样有具体阶段成本边界。7.4ms只指iPhone16 Pro、8bit、GPU decoder，不含首次encoder。弱mask生成提示，teacher在相同提示下在线产训练目标，不能称弱mask直接是高质量标签。October1无时区/时刻，当前没有完全落窗范围；潜力保留、日期隔离通过，不授当窗Evidence或已有覆盖。

初始错误日期查询的72374不是队列；修后200/261仍是submitted-title发现，单独agent/inference/training等词过宽，未继续全量关闭余61或月目录。85题摘是已发生的有限阅读，不是本窗85新论文。后续日期须按来源主题收窄，不能因原件已有而自动扩大工作量。官方CL前100仅标题，其他类恢复失败与公告日界不足明确隔离，不用一般公告排期逐篇赋日期。

## 15项必要安全与设计反侧

本轮不是接受作者“已读”标签：实际解析各`core-<ID>v1.raw`原HTML章节，范围如下；没有运行代码/攻击或复现实验。

| 精确身份 | root实际原文位置 | 核验边界 |
| --- | --- | --- |
| 2510.00490v1 | §3.1～3.2 | 权限/部署假设和物理mapping要求与“无root”表述存在张力，不作任意云租户远程攻击生产证明。 |
| 2510.00494v1 | §4.1、§5 | same-data/latent预算不等参数配平；统一模型缩小差距是局部设计反侧，不推翻所有latent reasoning或脑科学类比。 |
| 2510.00496v1 | §5.1 | 18 GUI模型、grounded/text/structure不同子集，部分原100%成功样本；下降不能直接归因为记忆占比。 |
| 2510.00565v1 | §4.1、§6.1 | 中间态可干预与黑盒会话威胁不同，judge/训练对照受设置限制，不授全部API可达。 |
| 2510.00626v1 | §2.2～2.3 | 6模型与采样方式不完全相同；双向flip率不同于accuracy，静音不是零影响，不把模型规模相关性写为控制因果。 |
| 2510.00628v1 | §3.1 | TTS及长度/四选项过滤、正确选项逐位置重排；限定受控位置偏差，不推广所有口语任务。 |
| 2510.00635v1 | §5.1～5.2 | FLUX.1-dev白盒参数改动、指定擦除与detector任务；不等任意用户prompt可绕过任意服务。 |
| 2510.00761v1 | §3、§7、Limitations | 普通遗忘强度与后续quantization/relearning鲁棒性分开；ZO更弱普通遗忘代价不能删去，未验证一般安全对齐。 |
| 2510.00778v1 | §4.1、§4.4.2 | SD1.4/PIE与输入保护；CLIP辅以结构指标，更多采样步削弱保护，未推无限免疫。 |
| 2510.00829v1 | Experimental Settings的Models/Controlled Noise | 不同模型/token预算及合成idiom噪声，保留retrieval误信反侧，不把注意力相关性或资源差异写为完整因果识别。 |
| 2510.00857v1 | Limitations | 合成多选与人工校准subset、不能提出第三路径、nudge改目标；不能外推真实管理行为概率。 |
| 2510.00938v1 | §4.1 | 错CoT prefill、直接harmful/jailbreak/overrefusal分别评价，judge/reward不同；改善不等adaptive安全保证。 |
| 2510.01070v1 | §6 | 单SFT人工secret、single rollout与多轮行为probe不同；不作自然pretrain/RL秘密可恢复上界。 |
| 2510.01088v1 | §5.1 | unlabeled PKU prompts与20攻击、rule/LLM judge、8A100/verl；内生entropy不是天然安全真值。 |
| 2510.01157v1 | §4.2～4.3、§5.2～5.3 | 训练污染、组件freeze/propagation分开，clean质量与trigger AER分开；不是正常推理可任意植入后门。 |

全部15项保留必要信号，不将安全/负面材料因日期不明当无贡献。只核决定非采用边界所需核心，不授其论文完整正面Evidence、代码核验或所有附录已读。

## 来源及Books

实际读十四行及各首查/修补请求范围；独立定点看DeepSeek原/news/研究10项日期与部署展开机制、Seed US原JSON的0/20/40/60/80与80末页、Zai原page2累计18/没有更多、Google原月页2及Segmenter、Qwen旧原页、Moonshot原Blog邻接日期、ERNIE原终页、Hunyuan原JSON9/9与时间字段、Meta/Anthropic原响应及有限切片、Google pubs/DeepMind及MiniMax三个原入口请求和历史限制。

DeepSeek 10/21→5/14、Seed近窗9/22→10/9、ERNIE9/12→10/16、Moonshot9/16→11/6的当前可见日期边界成立；它们不替代论文first-public，也不证明删除/未收录项不存在。Seed真实返回85身份不等total94，没有因此安排85篇年度全文队列。Zai末12/7及Hunyuan最早2026/02仍缺2025历史段，不用“当前列表结束”证明当时无研究。

MiMo作者壳本身不证明八Paper。root另于2026-10-05约05:20 BJT实际请求官方部署Paper数据URL `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js`，原件[ROOT_mimo_paper_data.js](ROOT_mimo_paper_data.js)，实际返回25477 bytes、curl成功，有限核8个Paper日期，9/19→10/21跨本窗。没有赋这个下载时间为发布日；Blog历史列表未恢复仍隔离。

OpenAI定点原RSS七exact case均GMT10/01 00→BJT08，在起点前1h；作者已实际移出日期hold，单页发布与PDF/主报告事件不混同。只读过两个case核心，不声称七篇在02重审。

十四来源的有限处理/外部隔离可终态，不是全部历史Coverage通过。未逐一复演全部搜索结果或恢复机构全部仓库；每个缺段有原入口、范围和替代材料，不构造互联网绝无遗漏。Books No Change仅因没有可采用的确证当窗命题，不是所有owner已覆盖潜力。没有共享Books实际改动需要写后验收，不要求为了结果造diff。

## 作者同步与剩余

剩余普通窄项仅作者同步：§5明确“本窗外部终态保留项，不用于正面证据、Books或无遗漏断言”及具名重开条件；§6引用本复核的真实范围/通过结论并保持抽检限定；随后运行完成态V3、引用/围栏/空白检查。通过后02可以进入实际日级分母，不能由本文件自动替作者稿写完成。已有来源/core不重复重跑。

未stage、commit或push；唯一新增是root原Paper数据和本复核，保护所有其他任务改动。
