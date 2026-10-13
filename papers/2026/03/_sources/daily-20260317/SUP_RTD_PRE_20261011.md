# RTD-Guard 必要Source已独核、唯一owner逐字PRE待核

仅本17补03/16；2603.12582v1完整AB准入及官方arxiv.content字段日级夹证已独核，精确日期原值在SUP_DATACITE_OFFICIAL_SUPPLEMENT。原“traditional NLP”拟EX已按§4.2/5实际机制改判，不以模型大小排除；2+1+2=5，具体安全反侧深入。

[原v1](https://arxiv.org/html/2603.12582v1) §4.2/5–10必要方法/评价/消融作者实际读，review_mar17_18亦独读通过：WIR读已被扰动的class会使token定位失真，独立预训练RTD选top-k5 mask，再对固定原predictedclass比较两次squared confidence shift；必须可取victim class confidence，而不是label-only。ELECTRA-large无需对抗finetune不等总费用/免校准，tau .09在validation校准。三BERT/IMDB AGNews Yelp、四TextAttack词替换并非adaptive-aware。RTD概率不是语义或真实攻击标签，mask亦可能损伤合法任务。2444 AGNews/TextFooler、RTX3090局部35.3s对victim8.9s约4倍；模型前向、mask与查询均计费，precision/batch/concurrency/tailSLO Not Disclosed。§10语言匹配限制，生成式LLM应用仅futurework；未核artifact/复现。

Books背景PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE与ROADMAP、最新本月route重读；actual Ch72 905–1019完整CoT→Learned Security Sensor→Hidden-state衔接已读，Ch71/73开篇交接已读。现Ch72 968/970的BOE独立Mamba前端检测污染、972后的白盒选层并未承载“victim当前label不能可靠定位→独立replacement detector挑token→固定原label做mask干预”这条具体分支。唯一owner PLATFORM-SECURITY，拟在BOE成本/回退段后、白盒多层sensor前，两段如下，未写Books/未申请锁：

入口定位也不必读取受保护classifier当前label下的敏感度：若攻击已使label偏移，按这个label挑token可能错过触发变化的位置。一个受限替代分支先用独立预训练replacement-token detector排序，再mask少数位置，固定原输入的predicted class，比较原文与变换文本的confidence变化；token选择信号与victim响应因而分别有身份。它要求可读取class confidence，并不是label-only接口；replacement概率也不认证对抗语义，mask可能同时删去合法任务信息，不能把变换后分数当安全真值。<!-- source-family:SF-2026-ARXIV-2603-12582 -->

[RTD-Guard的有限证据](https://arxiv.org/html/2603.12582v1)只覆盖BERT在三组分类任务、四种非adaptive词替换攻击及验证集校准阈值；不授知道detector的攻击、跨语言或生成式LLM防护。两次victim query仍要另付RTD前向、mask与校准，所披露局部runtime约为victim-only的四倍，而非constant-time免费防线。检测人口、语言、k、阈值和victim revision须共同固定，误拒/任务损伤或接口不匹配时保留原输入与独立有标签检测、拒绝/复审路径，不由无告警批准输入或后续effect安全。<!-- source-family:SF-2026-ARXIV-2603-12582 -->
