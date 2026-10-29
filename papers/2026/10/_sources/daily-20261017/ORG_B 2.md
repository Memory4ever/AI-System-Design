# Live Daily 2026-10-17：机构来源 B

- 窗口：北京时间 `2026-10-16 ～ 2026-10-16`。检查截至：`2026-10-17 09:16 +08:00`。
- 本文件只记录本窗有限发现与题摘/官方核心筛选；不代表整日报告、独立复核或 Books 验收。没有继续历史 cursor、扫描其他日期目录、写 Books、stage、commit 或 push。
- 已重新读取当前 AGENTS、研究合同、Report V3、Prompt、来源使用说明/每日组、ROADMAP；最新相关暂停路由只用于确认不恢复历史。
- 六源没有确认落窗且通过项目增量门槛的候选。一个落窗原始命中《稀宇科技诚信自律承诺书》已读官方核心后排除；不是把空页记作零。

## 1. SRC-TENCENT-HUNYUAN

入口：[Research](https://hunyuan.tencent.com/research)。网页正文为动态壳，网页提取超时。按来源要求尝试浏览器：创建标签的调用超时，但库存实际出现 `https://hunyuan.tencent.com/research?page=1`；读取该标签仍超时。未把上述结果算作列表检查。

从当前首页官方脚本恢复实际公共 API：

- [首页脚本](https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-Uh_m57w8.js) 中 `Qi` 将 `hunyuan.tencent.com` 映射到 `https://api.hunyuan.tencent.com`。
- [列表模块](https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-CeX5xNqy.js) 调用 `POST /api/blog/publicList`；列表组件使用 `pageNum/pageSize/renderType`，`renderType:0` 为全部。
- 实际请求 [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)：先 `pageNum:1,pageSize:10,renderType:0`，再 `pageNum:1,pageSize:100,renderType:0`；后者 `code:0,totalNum:11,list.length:11`，全部页已回齐，停止第 1 页，不继续历史分页。直接同站 `/api/blog/publicList` 曾返回404，不算实际 API 结果。

本次实际11条身份（用于证明有限列表范围，不把它们变成全文审阅队列）：`100119,100116,100100,100091,100087,100064,100041,100039,100061,100015,100025`。当前最晚 `publicAt/updatedAt` 为 `100119` 的 `1790053389`（北京时间2026-09-22），最晚展示日期也是09-22；所有11条 `publicAt/updatedAt/publishedAt/displayPublishTime` 均不在10-16。前两条为 [Hy Image3.5 preview](https://hunyuan.tencent.com/research/100119) 和 [Batch Size Scaling](https://hunyuan.tencent.com/research/100116)，均展示09-22，不纳本窗，不评价其窗外贡献。`100087 Hyra` 标题属暂缓科学发现应用，不扩读。

结论：当前官方“全部”11/11公共事件已检查，未见本窗事件；浏览器不可读已由实际公共API恢复，不用构建时间 `2026/10/16 15:32:16` 冒充论文/公告日期。没有为证明全球无遗漏扩扫组织仓库或T1旧报告。

## 2. SRC-ZAI

首查 [中文 Research](https://www.zhipuai.cn/zh/research)：实际“全部”、时间排序首屏15条，自 `2026/08/26 GLM-5.3-Flash` 至 `2025/12/09 GLM-ASR-Nano`，页面有“查看更多”。当前顶端已早于本窗，停止首屏，不点击更旧批次，不把全部历史目录变成待筛队列。

补核 [官方 release notes](https://docs.z.ai/release-notes/new-released)：当前最新日期08-26，后续降序08-18、06-16、04-07、02-12、01-14、2025-12-22、09-30；页面到底，未见10-16事件。Research中的08-14与release notes中08-18是两个来源各自日期，不用于本窗事件归属，也不追查该窗外差异。无本窗候选；不声称GitHub全部release已扫。

## 3. SRC-BYTEDANCE-SEED

首查 [Research](https://seed.bytedance.com/en/research) 及 [Publications](https://seed.bytedance.com/en/public_papers)。论文目录明确 `Newest → oldest`，第1页显示 `1-20 of 246 / Page 1 of 13`，最新 `2026-09-28 Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression`，其后09-01、08-31等，页末05-26。停止第1页（没有请求第2～13页）。

Research首页Blog只是精选，未当完整Blog列表。实际再核5个当前技术分组的最新首段：

| 分组 | 实际入口及停止依据 |
| --- | --- |
| Foundation | [list/foundation](https://seed.bytedance.com/en/blog_list/foundation)，明确时间降序，最新06-23 Seed2.1，首屏12条至2025-05-13；顶端早于窗，停止 |
| Visual | [list/visual](https://seed.bytedance.com/en/blog_list/visual)，时间降序最新07-31 Seedance2.5，首屏12条至2025-04-16；停止 |
| Audio | [list/audio](https://seed.bytedance.com/en/blog_list/audio)，时间降序最新08-05 SeedRealtime，5条至2025-01-20；停止 |
| AI Infra | [list/ai-infra](https://seed.bytedance.com/en/blog_list/ai-infra)，网页工具超时后同一URL普通HTTP恢复；时间降序3条，最新2025-08-14 VeOmni；停止 |
| Frontier | [list/frontier-research](https://seed.bytedance.com/en/blog_list/frontier-research)，网页工具超时后同一URL普通HTTP恢复；时间降序9条，最新2026-07-07 EdgeBench；停止 |

首页置顶未标日期的 [SeedRealtime原文](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction) 已定点打开，原文日期08-05，与Audio组相合，不将置顶等同今日发布。不扩读窗外全文。没有确认落窗事件；论文和Blog发现入口都不只检查首页精选。

## 4. SRC-BAIDU-ERNIE

首查 [中文技术Blog](https://ernie.baidu.com/blog/zh/) 第1页：10篇，最新 `2026年5月9日 文心5.1正式发布`，至 `2025年11月21日`，底部下一页标 `2/2`。按当前时间降序列表顶端早于10-16，停止第1页；不请求更旧第2页。无确认落窗项，不将历史发布数字或排行榜当本日机制贡献。未扩扫Paddle普通PR。

## 5. SRC-XIAOMI-MIMO

首查 [主页 Paper/Blog](https://mimo.xiaomi.com/)：Paper 8条，首条 `MOPD` 日期2026-06-29，末条2025-05-12；Blog首屏15条，自工具复读复盘至人文社科评价，末尾有More。Paper均窗外，不扩读。

Blog首页条目未逐项标日期，因此定点打开最新项及紧随研究/工程项：

- [工具调用复读复盘](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)：官方正文2026-09-27；API更新另写09-25，不是本窗纠错。其重复/洪泛区分、局部惩罚与MOPD修复有潜在机制价值，但属于窗外，不在本次评分、深审或改Books。
- [MiMo-V2.6介绍](https://mimo.xiaomi.com/mimo-v2-6/article)：官方日期2026-09-22。
- [MiMo Code长程任务](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)：2026-06-10。
- [UltraSpeed](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)：2026-06-08。
- [Full-Pipeline Inference](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)：2026-05-30。
- `How Xiaomi MiMo-V2.6-Pro Boosts Productivity in New Materials R&D` 标题和首页完整说明明确是PFAS材料领域应用，按ROADMAP暂缓，不为日期恢复读完整案例。

当前官方路由元数据 [4752.2908c99e.js](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js) 的frontmatter定点确认复盘09-27、长程06-10、UltraSpeed06-08、Inference05-30、人文2025-12-19、安全报告2025-12-18；未取得的其他旧模型介绍日期不补造。实际停止Paper8条/Blog首屏15条，不点击More，不作全历史逐项日期证明。无确认落窗候选；对未带日期条目不声称已经证明10-16绝无发布或修订。

## 6. SRC-MINIMAX

首查 [英文Research Blog](https://www.minimax.io/blog)：首批12条，最新08-13 Music3.0，其后07-31 H3，至2025-10-27；停止首批。中文入口 `https://www.minimaxi.com/blog` 重定向 [minimax.cn/blog](https://www.minimax.cn/blog)，最初一次提取只有导航空壳，未记0；再次请求已恢复13条完整列表，最新同为08-13，末条2025-01-15 MiniMax-01。日期字段按各自原文保留，不追查窗外中英文个别旧文章日期差异。

[Agent Tech Blog](https://agent.minimax.io/docs/techblog)：3条，日期10-08、09-22、09-19，最新为 `I stopped babysitting my coding agents. Here’s the workflow.`；页面到底停止，无10-16条。

限定日期搜索触发一个落窗非技术命中，回到官方页面实际读核心：

- 身份：[稀宇科技诚信自律承诺书](https://www.minimax.cn/news/integrity-self-discipline-pledge)，官方中文IR [最新发布](https://ir.minimax.cn/zh/news-events/new-releases) 首项，`id:news-6ad1efb6a830de04f38c1a08`，`publishDate:1792080000000`，页面展示2026-10-16，标签合规/公告。英文IR相同入口当前返回的首项是10-13日本IP活动，不替代中文证据。
- 官方正文网页工具不可达，普通HTTP200取到正文；全文核心8项为遵法、内容安全治理、数据/个人信息保护与生成内容标识、账号风险、报告、内部培训与监督等企业合规承诺。
- 排除理由：没有新增具体技术执行机制、兼容性/正确性更正、可检验安全保证或模型/系统设计边界；不是一个具备技术证据的安全事件或发布约束变化。不因含“安全”而机械加深；不评分、不列候选、不进Books。

## 补检边界与缺口

实际搜索只用8个有限query：`site:hunyuan.tencent.com "2026-10-16"`、`site:zhipuai.cn "2026" "10" "16" research`、`site:seed.bytedance.com "2026-10-16"`、`site:ernie.baidu.com "2026" "10" "16"`、`site:mimo.xiaomi.com "2026-10-16"`、`site:minimax.io "2026-10-16"`、`site:minimaxi.com "2026-10-16"`、`site:agent.minimax.io/docs/techblog "2026-10-16"`。只读返回的有限结果，不用搜索0命中证明来源0更新。仅MiniMax承诺书触发定点原文恢复；其余返回旧Research页/窗外条目，没有扩为历史池。

本次发现边界已到：6个机构官方研究/技术入口的上述有限列表，不包含组织内全部仓库/所有历史版本。没有必要正文或落窗日期仍待恢复的拟入选项；MiMo旧Blog无日期字段的有限范围保留，不支持“无遗漏”断言。所有窗外项目只是恢复线索，不把本次顺手打开算成已审重复或要求现在恢复历史。未启动下一日。

## S0. 本日具名 arXiv Source 接续边界

root后续分配的8个已具名项不扩发现；`2610.22314 MindEval2`已由其他独立reader R3完成，按root通知复用、不重复打开。本人只处理另7项的精确v1必要Source和actual-owner比较，不写Books/Report。日期使用root已取得的官方CL recent `Fri, 16 Oct 2026`首50条公开列表；HTML页眉`15 Oct`是submitted，不替代公告日，也不追精确时刻。以下建议不是writer POST或日级验收。

## S1. 2610.21436v1 — HyCo

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.21436v1)，本次实际读§1、§3.1–3.5、§4.1–4.6、§5、Limitations；无须PDF恢复。未核公开实现、未复现。
- 准入/建议评分：端云drafter既要减少server work，又受手机NPU串行SLM passes所限 → 原文把target原生MTP head迁到手机提供depth、一次独立SLM pass提供width → 重新考虑“device只能运行完整SLM”的work split。`2+2+2=6`；为这条具体机制差额深入必要部分。
- 机制：server回传末hidden、root embedding及两个verifier layers的window KV；手机MTP串行chain加runner-up siblings，SLM一次在root及所有已植节点下加分支，按proxy剪为ancestor-closed 32 nodes。proxy不是proposal概率；exact分支由target每节点自采样，命中child才继续，否则该sample作为bonus，故可支持其声明的processed target law，不用阈值伪装exact。默认epsilon分支改为接受`p_tilde(child)>=.005`并择最深path，明确有损；support membership和质量区间跨0都不是quality equivalence。
- 评价/直接反侧：Galaxy S26 Ultra/SM8850/Hexagon v81、commercial LTE/5G、单client；Gemma4 26B-A4B/AWQ4bit/单RTX PRO6000，temp1/topk64/topp.95；1K drafter window、86K/262K keep set、MTP4bit QAT与fixed-point activations。SB480含1024 output cap与32K小说50题/1200 output cap。相同epsilon下server GPU ms/token相对Cloud+MTP为-38.6% vs SLM-only -29.6%，三run只覆盖这两组SB；exact HyCo仍-27.7%/-11.9%（SB/32K）。这是server GPU busy-time，不是loaded capacity、能耗或币值节省；Cloud+MTP未stream到手机，不能比其user latency。手机MTP多约20ms/round；5.6KB/round+6.1KB/output-token（8bit），长prompt首次reply可多6.3MB。head迁移对照还同时改变precision/keep/window，不能纯归因placement；更多SLM pass更省server却更慢delivery；TTFT SB846ms/32K4.60s。翻译对SpecEdge-epsilon退2.6分，CI[-5.2,-.2]为exploratory未多重校正；单Cloud+MTP run、question-only judge与summary reference均不授事实保持。head/hidden/KV不可取得、tokenizer不兼容或状态泄漏未防护时不可直接部署。
- actual owner：`INFER-SPECULATIVE-DECODING`，Ch48当前WISV段（约88行）已有端云协议/hidden传输/RTT/有损仲裁，树形预算段269–277已有ancestor-closure、target own-token与proxy/proposal分离，但没有原生MTP-on-device与SLM-width的双drafter职责。故不是仅主题覆盖，建议一个最小PRE，不另写Ch49/54。
- 最小PRE位置：WISV段后、`### 声学草稿让验证分成两级仲裁`前。建议语义：当target已有可迁移native head，端侧可让head供应chain depth、独立SLM单pass补width，server只回head所需state；这以额外device compute/weights、双向传输与中间state暴露换server sequential-head work。exact target-own-token与epsilon有损路径分账；单client GPU-time证据非并发SLO，长输入首包与手机预算可使server-head/普通drafter仍合理。无需在书中搬整张性能表。

## S2. 2610.21463v1 — SpecAgent

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.21463v1)，实际§3/Alg1、§4/T2–3、§5/T4、必要Appendix D adapters/prompts；无须PDF。未核实现/复现。
- 准入/建议评分：强模型逐步生成使decode work高 → weak在真实read observations上继续、只在adapter定义state-changing边界hold，再强模型一次semantic prefix verify并融合一个repair action → 把算力合同从每步强生成改为分块语义检查。`2+2+2=6`；已深入必要机制与反侧。
- 机制：read立即执行，遇write hold；K个纯reads可未经strong复核并入history。verifier输出最长有效prefix j及reason/可选replacement，首错后整个依赖suffix失效；fused replacement过schema/执行校验后直接commit，否则strong单步repair，不二次review。语义有效不要求与strong会写的步骤字面相同，也不是token-level target-law保证。
- 必须近文的反侧：Appendix D明确read撤销只是删除history，service访问日志仍在；真正保证只到“被分类state-changing的动作在review前不执行”，不是一切副作用可回滚。tau2/Vita客户回复虽不可撤销但未hold（只看DB变化），Automation/MCP final answer则hold；不能写成“所有不可逆动作都先核”。错误classification、read的信息泄漏、外部receipt和authorization不由semantic model消除。strong semantic verdict可错，pure-read未核历史可能继续影响后续。本文不授safe execution。
- 评价：弱Qwen3.5-4B/1 H20 SGLang，强397B-A17B/TP16 H20，8 tasks concurrently；tau2 airline50/retail114各3runs、Automation600各1、Vita100各2；temp等细项在附录，未在此推算。tau2 Pass@1 86 vs strong86、87.7 vs88.6，paired CI分别[-5.3,+5.3]与[-4.7,+2.9]不等equivalence。Automation10.5 vs15.2、Vita44.5 vs48仍有质量损失。HBM是按token/architecture估算、MoE route不明给interval，非硬件计数器；FLOPs反增30–87%，small decode batch memory-bound假设和可共享prefix影响收益。MCP101 real servers/local5090+hostedAPI：Qwen59.4 vs72.3、GLM67.3 vs76.2、DS74.3 vs84.2，walltime120/108/215 vs105/110/151，不能泛称更快；API成本不含local GPU。
- actual owner：`AGENT-TOOL-CALLING` Ch78。已实际顺读1–125及相邻Ch81 learned-transition段：现78的typed intent→trusted executor、stream finish admission、MiMo FIFO/read overlap/write barrier已承载通用执行分权/不可回滚；未承载weak多turn draft→强semantic prefix review与fused repair的计算分工。Ch81只是模拟transition不可当事实，不替代这里真实reads。建议在MiMo排序段后、`### 随机策略需要真正的 Sampler State`前一段最小PRE。
- 最小PRE语义：允许低风险真实只读观察驱动weak草拟多步，held mutation之前用strong保最长语义有效前缀并给一个repair；省的是strong decode，不保持strong policy分布。read日志/泄漏及未hold用户回复不能撤回，模型语义核不授authorization或effect安全；分类/证据不足时逐步强生成、完整review与原executor硬门继续成立。必须保FLOPs可增、real MCP延迟反侧；不在Ch48重复。

## S3. 2610.21496v1 — OPRD

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.21496v1)，实际§3.1–3.4/Eq1–10、§4.1–4.3/T1–4、AppB Top-k/refresh、AppC.1构造与trigger核心。未核代码/复现。
- 准入/建议评分：终态binary verifier不足以提供跨turn与当前观察纠错 → teacher独享persistent global和仅next-turn local reminders，在student真实无reminder rollout同prefix提供分布，并按success/failure分CE/反向KL → 改变privileged supervision的作用域和consumer，不是部署再加提示。`2+1+2=5`，此具体scope/loss差额已深入。
- 机制：成功轨迹全部valid assistant tokens做self-imitation CE；失败轨迹不teacher重采样、对全部valid assistant tokens做RKL，teacher每turn见global、只紧接对应observation的那个assistant turn见local，之后移除；scope通过teacher input实现，不等只对被提醒turn做loss。student从未读reminders；test diagnostics可形成global，但不允许revealing reference patch。AppB shared Top100按`max(logp_student,logp_teacher)`选，双方在同index重归一后RKL，非teacher Top100或全词表exact KL；20/40/60/80%刷新teacher后区间固定，无teacher gradient。
- 评价/反侧：Qwen3.5 4B/9B；8k verified code trajectories、2k IF examples、4k task pool在线rollouts；4B训练16H20、131072seq、batch32、3epochs、LR1e-5。ClaudeCode shared harness，200turn cap，temperature1/topp.95、vLLM128seq/262144 max model length；precision未披露。4B base36.6→IF41.6→full47.9平均成功率；9B44.4→50.5→55.9。相同rollout budget、Top100、temperature下all-rollout RKL46.0 vs routed47.9；只支持局部route差额，完整11.3pts不能全归reminder。teacher四刷新最佳、shared参数最差，证明不能把该方法默认为current student自教。200任务诊断446→222是case-level trigger count非独立risk guarantee；IF responsiveness77.1是插reminder介入测量，不等main reminder-free outcome。主表未给多seed或CI，不作普遍可靠内化；训练提醒构造、teacher前向、SFT及刷新全费，外部hard constraints仍需runtime校验。
- actual owner：`TRAIN-SFT` Ch29，实际440–540附近已承载same-model privileged reference、fixed teacher、同visited prefix、部署无特权及feedback critique；新差额是global/local teacher visibility寿命与outcome-routed CE/RKL而非这些旧原则。建议在现`同模型产生target也不必是无外部监督`段后、视觉特权段前最小一段PRE；不在Ch75/79重复训练机制。
- 最小PRE语义：对on-policy失败轨迹将持久任务纠错和仅next-turn观察纠错限定在teacher输入，student同prefix蒸馏且部署移除；成功用verified self-imitation避免对失败行为一概CE。teacher reminder作用域不等lossmask、TopK重归一与checkpoint refresh需版本绑定；test诊断/提醒仍可能错且有训练成本，不认证外部约束已经永久内化。收益不稳时保verified target/原on-policy或runtime显式约束。

## S4. 2610.22131v1 — Intern-Decision

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.22131v1)，实际§3.1–3.5/Eq1–3、§4、§5.1–5.5/T2–7、§6.1–6.4。未核artifact/复现；不将selected demos当controlled tests。
- 准入/建议评分：有限候选的多字段选择不必反复decode整段JSON → 复用causal backbone/native LMhead，在固定masked skeleton的每个decision marker前读取logits、一遍求多个field → 改变typed-decision输入/输出计算接口。`2+1+2=5`，必要机制、对照和直接反侧深入。
- 机制：caller固定ordered schema/options，legal symbols单token映射，62候选symbols与HTTP最多16fields是release界限不是理论能力。输入仅placeholders，不含gold/predicted answers；普通causal shift使marker位置target由前一位置logits监督。training是仅decision位full-vocabulary CE、其他context ignored；inference才在legal candidate logits上temperature归一并由确定serializer写JSON。后field能看前placeholder，不见前答案；因此单pass不等独立/permutation-invariant或joint constrained output，schema合法不保证跨field一致。score expectation、Boolean yes probability、argmax各自不同consumer，softmax vector不自带校准。
- 评价/反侧：0.8/2/4B同17880 samples/23500 decisions（5500图像样本），7suite共12351 decisions，macro average不是pooled；Jevbench公开231题参与development，不是独立heldout。4B macro90.02、Hard82/111；没有matched-data/compute baseline ablation，不能把所有准确率差归singlepass或size。Hard ECE/Brier只111题、baseline temperatures未同等重拟合。96-case exact-distribution pilot来自48 settings×option order，非96独立试验；calibrated4B整体改善但Monty个案未校准更接近真分布，另有category反侧，Jev separate confidence也非同一probability读出。confidence cascade42/111 routed、97正确vsstrong99；hybrid time是estimate，本地总时按固定短请求latency推导，不是per-item trace。
- timing合同：单RTX4090/BF16/SDPA/HF、Transformers5.14.1，289input/3fields，4B mean44.16ms只固定短请求；batch/warmup/repetition/timing boundaries/Jev transport未全披露，不用2.48×或reciprocal FPS认证公平硬件speedup、截图长context或饱和QPS。视觉game/CAPTCHA/browser均selected qualitative，server inference不含planner/network/browser，不授general CUA或安全。
- actual owner：`AGENT-TOOL-CALLING` Ch78，实际前125及相邻Ch77/79。现约98–100行已有compact-code→deterministic JSON decoder与format/route/state分账，但仍是sequence generation，不承载all-placeholder singlepass native-logit读出；confidence cascade属其概率consumer、不需Ch79另写。建议最小PRE在compact serialization两段后、`调用记录完整，还不等于整批提案已经可以执行`前，解释有限decision schema可预置placeholders并在causal前一位读native logits、serializer写结构化结果；合法candidate概率、argmax和跨field一致分账。训练/候选映射、全部input-prefill与校准均付费；无限schema、开放生成或字段强依赖时保原typed generation/逐步反馈，executor原权限和effect Gate不变。

## S5. 2610.21561v1 — DialFork

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.21561v1)，实际§3–6/T1–4、Limitations/Ethics；HTML回收包含核心及部分附录，输出在无关后部截断，不影响上述必要原文。未核代码/复现或全部附件。
- 准入/建议评分：语义相近的对话仍可错误切workflow、跳步骤或改goal → 在同场景conformant trajectory不同位置注入单类偏离，分开测set/dialogue距离与first-deviation localization → 改变procedural fidelity的测试对象与可见信息合同。`2+1+2=5`，评价反证及具体owner差额深入；不是因为36k条数据而加分。
- 机制/标签：只用STAR workflows/role metadata、不重用原对话，Gemma4-31B双角色生成2134 conformant各16fork（4type×4positions）共36278。四type是workflow identity、step-policy、goal replacement、competing constraint；固定seed重放prefix可能有minor wording differences，不证明逐字配对。fork时点是注入construction label而非自然onset真值。30人只评5tasks/428conversations（526judgments），盲conformance顺序tau_b .64；type91%确认、onset±1turn77%/exact67%、pre-fork conformant95%，不能当全库标签100%完美。
- 原文可支持的测量增量：Task1 set distribution rank、Task2 paired dialogue rank、Task3 onset/abstain分开；length controls与shared-prefix control帮助排部分构造cue，非自然样本因果证明。FlowKL对reference聚类bigram及observed transitions likelihood做分布KL，有可读图但不自动验证真实business rule。FlowDTW显式保单调alignment；FlowScore是turn max matching，当前每turn独立embedding，原文明确不捕捉explicit turn order，不能把强rank结果写成检测顺序错误的形式保证。
- 直接反侧：set τ=.882/.913等差异不显著；FlowScore across encoders约.812–.845支持此合成ranking。streaming只past prefix+conformant refs，无future/workflow；best IT+NC MAE4.61turn、hallucinated coverage93.82%、false alarm5.58%，不等即时拦截安全。full-dialogue+workflow privileged Gemma MAE1.09却conformant falsealarm30.65%（其他模型最高82.8%），不能用离线精定位认证在线门禁。单generator/STAR、单type singlefork无compound/cascading，不给真实用户自然偏离率。generation约33GPU-days、reference/embedding/graph/threshold/human calibration另计。
- actual owner：`PLATFORM-EVALUATION-SYSTEM` Ch66，已实际顺读350–418及邻Ch65/67交接。现`Evaluation Identity必须包含Harness与Environment`中的TRACE三实验/同轨迹re-score已明确outcome/procedure区别和judge不等authority，故这些原则具体NC，不重复整节。尚缺有界fork位置作为procedural extent instrument，以及online-prefix versus hindsight/future+workflow的onset可见信息分账。建议只在TRACE第二段后最小一段PRE，保construction标签/人工不完美、独立turn bag不等顺序sensor与漏报误报，不搬taxonomy或排行榜。
- 若root认为该最小instrument差额仍不需正文，可作“仅报告”而非把全文价值否认；不能声称当前TRACE段已具体解释fork-onset protocol。

## S6. 2610.21739v1 — RIKA

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.21739v1)，实际§3.1–3.3/T1–2、§4.1–4.5、§5–6/T3–5、AppA.1–A.4、AppD.1–D.5/Alg1/Table7、AppE.3–E.5及F条件CI说明。未核artifact/复现。
- 准入/建议评分：抽取出plausible claim不等其scope已有反馈支持 → 以原子claim的direct/indirect grounding分别immediate/deferred admission，后续真实task evidence更新状态再渲染 → 改变memory reuse gate而非再增加一种summary格式。`2+2+2=6`；这条revisable admission差额深入。
- 机制：四类hierarchical extractors不看stored claims；atomizer保source spans/parents，router根据feedback是否覆盖claim的**scope**分route，不按factual/conceptual类硬分。direct threshold1、deferred3；same-scope equivalent合并且route冲突回deferred，changed scopes分开。specific→general DAG传support、不反向；contradiction在重叠scope减count；overlap/independent无传播。每batch更新净e后重算admitted，先前admitted可退pending，低门槛连续3batch才删除/重提重建；全文由canonical admitted集合程序渲染，不让反复summary改写当原source。
- 权限边界：LLM还负责route/relation/**evidence counts**，所谓sequential-hypothesis启发不提供独立样本、p-value、形式entailment或真值保证。累积支持不能把correlated/copied observations变独立证据，也不能从version1反馈证明所有schema版本；原scope/observationledger要保留。model-generated count到admitted是原机制，不认证安全权威。pending不进入consumer，但永久forget仍付不可逆丢失成本，应保原episode及可重建来源。
- 评价/直接反侧：6 text tool streams×4 hosted backbones，temp0/max8192/128k context，每题重置再inject完整知识；batch5（Sales4），5run为固定corpus的within-stage permutations，Sales完全同chronology，不是5独立世界。RIKA aggregate最高但只14/24 model-task格最高；Gemini Poker gain -0.688、GPT Cohort -0.013，保无memory/简单curated分支。routing消融DeepSeek DB/Cohort/Codebase：RIKA .281/-.042/.575，all-immediate .225/-.089/.540，all-deferred .265/-.070/.557；hierarchy/route有局部支持，不授全部设计单因果。aux calls不计环境action budget，不能由环境steps推总token/API省。
- Harmful-entry诊断：frozen artifact在后续固定窗口做claim删一项、其他retrieved context冻结，5paired seeds Student-t CI全负才判harm；从未被retrieved的entry不进分母。3 artifacts的rate等权平均，12–33%是条件exposure/冻结artifact比率、非所有memory坏率；DB窗口仅migration之后、code跨Tablib→Tenacity。F中Gain CI条件于shared stateless mean，未包含control估计不确定性；no highstakes/perceptual/physical证明。
- actual owner：`AGENT-MEMORY` Ch77，实际80–180、typed transition与failure-reflection相邻；当前已有accepted/pending/history、source/consent/conflict与失败reflection待核，以及约405行shared-copy独立false-support反证，所以“抽取不等真值”“多次相同说法不独立”均具体NC。差额是按claim作用域分route、后续support/opposition使**既有admitted可回pending**并从当前state重渲染。建议在typed-state-transition/TARL限制段后、poison trust段前一个最小PRE；不要把四类taxonomy或net-count阈值写成生产规范。支持不足、relation/count漂移时原source/人工pending及静态curated memory继续成立。

## S7. 2610.22196v1 — Hy-Memory-30B-A3B

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.22196v1)，实际§3–7/Eq2–7、§8/T6、§9、Limitations，尤其§8.4无消融声明。未核代码/模型card或复现；不因GitHub可用扩全实现。
- 准入/建议评分：long memory writer仅少数terminal QA reward不能定位哪chunk保留了哪些事实 → frozen writer/answerer/judge分责，以chunk-specific probes+traps与gold-fact-attributed outcome组成chunk GRPO signal，并将选中bank跨window续接 → 改变写入训练credit和state continuation接口。`2+2+2=6`，深入具体reward/group边界；不因vendor榜首评分。
- 机制：只有writer训练；answerer只见query+retrieved bank，不见gold/rubric；judge见question/answer/reference/rubric但不见bank。OPD是student生成的多call分段链，frozen Hy3 teacher top50 RKL近似、call边界position重置；不补成全vocab exact KL。RL每window≤5chunks，每chunk约10turn不跨session；8rollouts起于同parent，之后各bank已分岔。正probe只奖current chunk新facts、前两chunk事实仅解指代/novelty；crosschunk ORM按gold-fact chunk id分credit，history-only不奖当前。traps（should-not-store）与token-growth penalty共同防store-everything，PRM这里是per-chunk recall不是reasoning-step model。
- group/状态：每window/harness/sequence/chunk position组内归一，multi-call chunk所有segments同advantage，但只一票进入baseline；后续banks并非相同state，one-vote不证明无state混杂，multi-call仍可获得更多loss mass。gamma0不广播future PRM；gold-fact recovered attribution是evidence-based、**非counterfactual cause**。每window按各chunk score和选一个final bank，整bank续下window、不是拼各chunk局部赢家；跨optimizer继承坏bank无retrospective gradient。平台fault重试/退出分母，policy malformed仍低reward，不能合并为missing。
- 配置/评价：Hy3 30B-A3B，OPD375初始化；RL16×8 H20、64windows×8rollouts、PPO clipped/chunk GRPO、无KL、rollout MoE route replay；precision/完整evaluation API并发未披露。Mem0/MemOS/Hy-Memory chat-working-coding是3family/5configs，不是5独立framework。main矩阵固定20%subsample、4harness×6metrics宏平均55.49 vs base47.66；Opus54.62，有MemOS .01、HyMemory .02微差，不是统计resolved superiority。EverMemOS仅一个heldoutframework，仍可有metric反侧，不能授所有memory transfer。
- 关键反证/采用限度：§8.4明确**没有**chunk-vs-window GRPO、gold-attribution-vs-broadcast、probes/traps、growth penalty、binary/rubric、OPD-vs-generic初始化、single/mixed harness controlled ablation；human-judge agreement、near-duplicate/sequence leakage、judge sensitivity和repeated train seeds也留future。因此7.84pt整体gain不能归因给某模块，更不证明train/eval无漏或reward标注全正确。只采用公开reward/group/state接口与验收分责，不采用原结论中“正确decision boundary已单独证实”。多模型/annotation/retrieval/8rollout/validation与state checkpoint都付费。
- actual owner：`AGENT-MEMORY` Ch77。当前159–183实际已讲memory-local gold answer proxy、counterfactual attribution、entry→step credit及非causal/全费；这些具体NC。缺口是**非counterfactual gold-evidence chunk credit**和多call按chunk一票baseline但不同loss mass、winner-bank续接的边界。建议在entry→step信用段（约177–179）后、task-conditioned adapter前最小一段PRE，作为另一reward接口而非更优算法；现有counterfactual/outcome-only/curated writer仍共存。无需Ch33复制GRPO教科书。

## S8. 本批 Source 收口

本人7项必要精确v1 Source与actual-owner差额已完成；MindEval2遵照root复用其他reader R3。没有新增发现/跨日材料，无待PDF恢复的本批正文；已有原理均明确指出具体承载，不因mapping即称整合。以上均为可供独核的最小PRE语义建议，尚未逐字授位、尚未写Books、无本人writer POST。源层不授准入、Books或DAY最终通过；root按独核结果决定具体NC、仅报告或最小整合。

## S9. 2610.22160v1 — EMO

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.22160v1)，实际§3.1–3.3/Eq1–10/Alg1、§4.1–4.5/T1–4、Limitations与AppB.3配置/成本。HTML必要核心完整，不需PDF/代码；未核复现。首公开归属沿root已核CL recent Fri Oct16首50；submitted Oct15不替代公开日，未追精确时刻。
- 准入/建议评分：逐轮feedback改context未必在decode兑现 → 以相邻两轮context在同prefix的概率位移构成steering，并保存候选由judge选择 → 改变context优化与逐token实现的接口。`2+1+2=5`；不是因EM命名或benchmark数量准入。
- 机制：冻结model，judge给无gold的0–10分与critique，文本Backward/Opt只改question-specific context；禁泄答案及pattern filter不能认证无泄漏。所谓textual gradient不是导数，EM只是结构比喻，不是共同likelihood的坐标最大化。`Popt`来自本轮优化context，`Pbase`来自**上一轮**context而非永远初始context；两KV stream共享同一generated prefix。方向为`delta=J(Popt) log(Popt/Pbase)=Popt(v)[r(v)-E_Popt r]`，正值是above-average log-ratio，不是简单`Popt>Pbase`或plain logit差。mask保`Popt(v)>=alpha max(Popt)`，其余delta置有限-100而非硬零；默认mu2.4/alpha.1，先steer再temperature/truncation。mu0是context-only，非去掉feedback。
- 选择/证明边界：K4产生5候选但9个target-generation equivalents，另有judge/rewrite及长度成本。最终选历史最高judge score（平分取早），feedback却接最近回答，不保证逐轮correctness。定理在full-softmax、有限vocab/horizon下，需TextGrad改善target KL且**实际masked direction**满足target-weighted alignment，才存在足够小mu；不认证默认mu2.4、截断采样、单调accuracy或跨steered-round改进。KL/NLL共目标也不让context更新与参数更新可行集相同。
- 评价/反侧：8个3B–32B Qwen/Llama、6 reasoning benchmarks（AIME25/26合成一task平均），external judge Qwen3.5-122B-A10B FP8/TP4/vLLM；主表greedy。40cells平均比Base+9.10、context-only+1.53，但后者25胜/4平/11负，DR1增量-.64，Qwen32 GPQA62.1低于TextGrad64.6。8B消融external judge增益5.56高于steering1.76，judge同时影响feedback与selection；缺mask-only对照，不能全归contrast。matched-generation实验3seeds/temp.6/topp.95、N=2K+1，排除judge/rewrite与响应长度，不是matched FLOPs/latency；Qwen8B GPQA60.3低于BoN60.4，MATH85低于SC86.1。Llama8 GPQA coverage73.7但selected37.4，候选覆盖不等selector可靠。
- actual owner：`MODEL-SAMPLING` Ch20，已实际读298–326与邻Ch21开头；Ch74相关prompt search段也定点读。当前Ch20约315–321已具体承载同prefix双stream、custom/default logit外推、独立KV成本/回退与mask不授真值，故这些NC。差额是**相邻context位移经概率Jacobian投影**及闭环candidate/selector成本。最小PRE位置：system-prompt双stream两段后、DPS段前。只加该不同方向与scope，保judge错/有限mask/条件定理及完整预算；原fixed-context sampling、context-only或BoN在收益不稳时继续成立。不在Ch74重复整套优化。

## S10. 2610.22294v1 — Multi-Target Few-Shot Prompting with Diffusion Language Models

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.22294v1)，实际§3.1–3.3/Eq1–6/Lemma3.1/Prop3.2、§4.1–4.3、§5与Limitations。HTML可读；未核实现/复现。沿同日CL recent公开归属，不用submitted作公开日。
- 准入/建议评分：自回归few-shot适合一个尾部target，而多离散编辑位点和未知长度需共同分配 → shared canvas保已知左右context、给J个mask sites分配长度再joint infill，并可按demonstration条件比重采样 → 改变多目标条件生成/评分接口。`2+1+2=5`。
- 机制：有限长度向量各`L_j>=1`由oracle或learned allocator在compact canvas上选，展开mask后揭示。**确定性一次一token**的位置选择（fixed ascending或deterministic confidence）可把实际条件概率乘积定义成归一化的induced target law；learned predictor通常order-dependent，恢复真实data conditional另需每步predictor恰为data条件分布。该定理不覆盖parallel revelation；评分target时额外masked demo outputs不填。`P1`是example-output可见、`P0`是其masked时同target概率，保同reveal rule但不同context可以产生不同candidate-specific顺序。`R=log(P1/P0)`测相对example支持，不是真值。
- 重采样边界：`Qbeta ∝ P1 exp(beta R)`是有限正共同support上的KL-regularized reward最优分布，但直接采样难；K次IID `P1`候选再importance resampling只是有限池近似，K趋∞才得该极限，beta0仍有demonstrations。未知长度两侧相同allocator使其因子从ratio消去，不等resample后长度边际不变。
- 评价/直接反侧：3DLM（LLaDA1.5、NemotronLabsDiffusion8B、dQwen3.5-9B），Qwen3-8B AR只single-target；SST2codes/ListFunctions/SALT/MovieDirector，64prompt families，single K64、multi K16，ascending reveal/beta.5，主实验oracle length。16个series随demo数整体改善不授任意task；J1→8 LLaDA per-target73.6→72.3且all-targetsuccess天然不同分母。J8 guidance在ListFunctions无positive CI、SST2部分改善但MovieDirector退步。learned-length有效mass约40–46%高于prior27%，但per-target准确仅oracle的35–48%，少一token便破坏结构。
- Java127tasks/50commits/14repos各D/J配置eligible population不同，Sonnet5.5 judge不编译/执行，不授code correctness或无污染；oracle unguided74.4→guided71.5，predicted15.8→14.5。Checkstyle错误行号/type候选得8.69nats高于正确2.05，一错对七correct占61.8%weight，局部期望success43.8→15.7，直接否定ratio=truth。one-token reveal、K候选、两context评分与allocator/judge全费，不能借DLM名称宣称parallel/SLO收益。
- actual owner：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，已实际读632–708与邻Ch23/25开头。当前mask/reveal顺序、parallel dependency误差与learned predictor不等data law均具体NC。缺口是**多个不连续target的长度allocation和示例输出选择性mask的双条件有限池重采样**。最小PRE位置：known+[MASK] schedule基础段后、multicodebook speech分支前；保exact induced law与真实data law、顺序与parallel、example support与correctness分账，明确length失败与完整成本；fixed-length/普通conditional infill仍保留。不在Ch74另建few-shot论文段。

## S11. 2610.21671v1 — PACE

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.21671v1)，实际§3–4/Eq1–13、§5/T1–2、Limitations、AppB.2/B.4/B.9与2B反侧。未遍历附件/实现或复现。沿root同日公开归属。
- 准入/建议评分：trajectory binary reward不能直接提供token credit，raw teacher likelihood受token先验影响 → correctness-hint对×full/null视觉构成四view，构造sign-conditioned正权并按trajectory confidence调混合 → 改变token credit proxy的比较基线与consumer。`2+1+2=5`。
- 机制：训练才见GT-correct hint与同题去重incorrect siblings；null是视觉embedding置零而非移除image/text。teacher是policy copy每20step硬刷新；negative先平均prob再log（main K1）。`Δfull=l(+V)-l(-V)`，`Δnull=l(+null)-l(-null)`，**`c=1.5Δfull+0.5Δnull`，不是full−null、不是消除语言捷径的difference-in-differences**；不依视觉的correct token仍可得2Δ，只有full差者1.5Δ。pair只消同一visual context内共享additive offset，不消任意teacher漂移，不保证c均值零。
- `S=mean(+V)-mean(other3)`为teacher相对分离，不是视觉必要性/因果grounding；按microbatch有效pair median/MAD、clip±3、sigmoid把混合λ调至.15–.65，缺pair退RLSD λmin，无hint退uniform。token权`exp(sign(A)c/tau)`裁[.8,1.2]、每response均值归一后mix1，detach后`Ahat=A*w`；保持coefficient符号和均值，不保持PPO clipping之后的参数gradient norm/方向、期望return或因果token贡献。4teacher view只训练用，不增加部署推理前向，但训练不是free。
- 配置/评价：RLSD/verl full-param Qwen3VL8B、Qwen2.5VL7B、InternVL3.5-4B；123k MMFineReason final-answer supervision，hard subset按4B thinking 4/4失败选；200steps，batch256×8、Adam1e-6/noKL、BF16teacher、8H200，rollout temp1/max4096。OPSD基线用ms-swift/rank64/forwardKL等不同recipe，不能当严格matched causal对照。5bench mean@8是采样口径，不是train-seed CI；8B均58.47 vsGRPO54.83/RLSD55.38/VPPO57.25，但InternVL GSM15.54低于RLSD15.92，2B不最优且改refresh10/λ.05–.30，不授default跨规模优越。
- 消融/成本反侧：无hint vision gap51.05低于Base52.09，hint branches57.06–57.68；full+null adaptive58.47高于fixed57.23，但full−null fixed57.68反高于adaptive57.34，且range选择影响大于confidence estimator。50step后PACE约350–380s/step vsGRPO250–280、RLSD300–350、VPPO约1000；generation约50s相近，额外成本来自teacher eval。训练四view、batch统计与refresh状态需一起验收。
- actual owner：`TRAIN-GRPO` Ch33，已实际读277–349及邻Ch34。当前trajectory reward到token代理、VLCalibration双视觉hidden uncertainty和正weight不授token真值均具体NC；新差额是correct/incorrect hint×full/null四view的**正null系数**和batch-relative混合。最小PRE在现VLCalibration两段后、PRL分支前，只解释比较基线/符号consumer及teacher全费；不把四view当因果视觉证据，不重讲GRPO。信号不稳/小模型退步时uniform GRPO、固定权/RLSD与原验证器保留。

## S12. 2610.22234v1 — OS-Helix

- 精确原源：[v1 HTML](https://arxiv.org/html/2610.22234v1)，实际§3.1–3.3、§4/T1–5、§5/Ethics、AppC.2–C.3、E.3与F.5必要失败案例。HTML可读，C.2定点第二次取回完整，不需PDF；未核代码/复现或全附件。沿root已核Fri Oct16公开归属。
- 准入/建议评分：GUI动作短、code动作长，按全部token平均sequence log-ratio使代码token长度隐式放大其更新份额 → 先action内平均再action间按权平均，形成step-balanced GSPO surrogate → 改变ratio归一单位，不只是再加一个computer-use接口。`2+1+2=5`。
- 系统/数据边界：一policy共享真实desktop的GUI/native/meta+Python/Bash，code每次fresh process；app–artifact compatibility graph固定version/init真实文件，非破坏exploration建coverage，冻结task后由独立evaluator编CLI/rule/VLM检查并做initial-reward0/quality filters。该分工不等evaluator语义全对；SFT Sonnet4.6 teacher本身也是visual judge，GPT5.5做quality review，31k success-filtered+40k general一epoch（83k attempts/9ktasks），selection不授无bias。RL只dense27B，1000steps live desktop、rule-only reward；Slime async最大1policy lag，frontier EMA采样，8prompts×8rollouts，2steps/update；malformed assistant单独隔离reward0，不把最终task成功反向洗白。
- ratio：每action `delta_bar_k=mean_token log(pi/pi_old)`，`wstep=exp(weighted_mean_k delta_bar_k)`；GUI/code α同1，替换raw-token geometric sample ratio。未clip的标量求导系数每action合计为`-A*wstep*omega_k`，与该action token数无关；但token gradient vectors/相关性、clipping与reward仍在，**不等参数梯度范数/variance相等，更不保证routing正确**。此surrogate不是whole sequence joint IS；step平均与外层sample loss权重亦不同。
- 配置：32H200（16train/16rollout）、Megatron TP4/SGLang、vision冻结、Adam1e-6、clip.2/.28/dualclip3/noKL；temp.5/max10240/50actions，历史截图5–10 retain5，overflow分段旧context loss0，precision未在必要正文核得。成本含SFT合成/筛选、live VMs与eval，不以50action固定证明equal FLOPs。
- 评价/关键反侧：OSWorld verified369去8个GDrive任务为361、Ubuntu/50step/8history截图1504×832；reproduced same-harness base可比较，外部leaderboard不是matched。matched hybrid27B46.50→SFT62.75→RL66.44，35B MoE42.84→57.27（无RL）；35B OS子域-8.7、27B Daily-.5，RL Office/Workflow也低于SFT，不能把全部增益给ratio。controlled同init/data/sampling/reward/budget下standard GSPO60.47/code40% vsstep66.44/code26.1%（SFTcode27.9%），支持局部改进，不证明所有action分工；fixed10k hybridSFT60.61 vsGUI57.56，去code52.13。WAA63.87 vs hybridbase56.41，不是把文中相对GUI40.82的+23.05当相对hybrid增益；WAA经prompt改为Python-only、无Bash，非接口零变化transfer。
- 直接失败：F.5 code转换文件丢row banding，将其误解为currency而非重建格式，显示reward/task理解覆盖不足；另一例GUI第一子任务只在unsaved buffer，code改disk完成第二，随后点Don't Save丢第一。**GUI buffer、磁盘写入与最终persist不是同一commit域**，global terminal reward不自动补足。实验VM隔离host credentials/files、混合code的effect权限仍单独成立，不能授部署安全。
- actual owner：`TRAIN-GRPO` Ch33；已实际读764–792现GSPO/长度重权段，当前明确sequence geometric ratio与外层长度权不同、不是joint IS以及clip/lag重新验收，故这些NC。缺口是**多模态action-token长短不等时，ratio先step内再step间归一**。最小PRE在GSPO段后、`Sequence ratio的长度归一化与loss外层`段前；保unclipped标量份额与full parameter gradient非等价、controlled反侧与成本。GUI/code分权和评价身份由Ch78/66当前原则承载，不另复制pipeline；unsaved-state反例可作为Source中的采用边界，不强制新增第二owner。

## S13. 最终有界 Source 收口

上述S9–S12完成root最后同日4项，无新增发现、无全站/附件遍历，无转下一日。连S1–S7，本人共11项必要v1 Source与actual-owner具体差额完成；S0的MindEval2继续复用R3，不重复阅读。本人只扩写本日ORG_B source，不写Books/Report/LS/index，不stage/commit/push；没有待PDF恢复的必要核心。所有PRE是独核前最小语义建议，不授实际采用、writer POST或DAY验收。

## S14. 同日具名十项补闭合的范围与日期

依root后续明确授权，只补2610.22187、21456、21763、22312、22158、22249、22213、21995、22238、22236，不扩发现池/日期。重读当前AGENTS、研究/Report合同、Prompt、来源使用说明/每日组与ROADMAP；沿此前未变Books上下文。10项官方abs逐一核身份、完整题摘及现有version history，均当前唯一v1，页面未见withdrawal/erratum。21763的abs抽取因错误链接吞尾，改用精确v1 HTML恢复完整题摘；22238一次curl空响应只作失败，第二次取回HTML必要正文，不当0。其他HTML均取得必要范围；不遍历全版本、实现或附件。

八项沿root已核本日Fri Oct16官方CL/LG列表日级依据；22238/22236由root再次确认官方LG recent首16同Fri16分组，联合此处精确身份/唯一v1。各abs的submitted Oct15均仅记提交口径，不冒充公开日。以下评分只对具体拟核增量，不计主题映射、模型规模或声望；无0–4强行配额。RBCD因实际核心证明冲突隔离，不降分假关闭，也不把其理论身份作为排除理由。

## S15. 2610.22187v1 — Rating Scale Sensitivity

- 原源：[abs](https://arxiv.org/abs/2610.22187)、[v1 HTML](https://arxiv.org/html/2610.22187v1)。完整题摘后实际§3–5/Eq1–4、AppC/D/E；未核代码或复现。
- 准入/评分：把scalar judge换刻度后线性归一常被当成同测量 → 2format×4range×2sign最小对照显示normalized值及类别也改变，rubric未缓解 → scalar比较须把数字端点/离散化与任务单极/双极定义作为instrument身份并做配对稳健性。`2+1+2=5`。
- 方法/评价：政治1700、sentiment5000、toxicity5000个英文item，5LLM×zero-shot/rubric×16scale；只分析final score。40minimal pairs仅改一个design element，先线性归一[0,1]，MAE量变化，三等宽bins量switch；后者是此处操作化的semantic sensitivity，不是逐item人类语义真值。1200pair/task/prompt/model cell等权，2000item bootstraps在每task内重采样并保所有模型/条件配对，CI不包含独立服务运行/模型seed漂移。
- 数字/反侧：format/range/sign平均MAE .098/.098/.085、switch19.2/18.2/20.3%；细scale令format MAE下降但switch不降，rubric差异≤.007，higher reasoning仍残留且Qwen range-switch19.1→22.0。toxicity唯一unipolar任务，不能单因果归给单极结构；signed zero被当not-toxic是分布解释而非已控内部机制。没有same-scale重复调用基线，因此总pair差异不全能归scale；开源temp1与API默认/lowest reasoning也不是相同解码recipe。Human labels只是context/有效性线索（政治label为outlet而非句子，toxicity为标注比例而非强度），不能挑最一致scale宣布truth。硬件/precision/完整调用费未披露，不采用服务性能命题。
- actual owner：`PLATFORM-EVALUATION-SYSTEM` Ch66，实际读388–390的预期不变量/重复随机噪声、457–478 scalar/prompt测量身份；后者已具体承载量表、prompt和先验身份以及稳定不等有效，故这些NC。仍缺**线性归一不能修复刻度设计引发的逐item值/类别差，以及rubric不自动解这一问题**。最小PRE可在现同答案多prompt latent-quality段后加一个短限制：冻结端点、连续/ordinal、sign并配对替代scale，另测same-scale噪声；不要用三等宽bins、约20%或unsigned推荐作为通用生产阈值。当前仅建议，不动Ch66。

## S16. 2610.21456v1 — TITAN / Translation Circuit Discovery

- 原源：[abs](https://arxiv.org/abs/2610.21456)、[v1 HTML](https://arxiv.org/html/2610.21456v1)。实际§3–9/Eq1–11/T1–5、AppB训练设置与progressive-knockout必要反侧；未核artifact/复现。
- 准入/评分：按层/低rank选择适配面未检查该任务的干预敏感性 → contrastive translation-intent prompts提出activation差方向，再subspace replacement定位组件并只在其上SFT+DPO → 改变trainable support的证据来源，需比较intervention-derived mask与关联probe。`2+1+2=5`，不因翻译场景本身准入。
- 机制：Gemma2 9B；positive翻译prompt与去target/语义扰动/矛盾descriptor counterfactual，聚合activation差，分解出单translation方向和正交residual。仅该方向换成counterfactual分量，其余保持positive，按translation-logit降幅和P99 noisefloor（操作点约.25%）选attention/MLP组件。SAE只训这些layer的residual，selectivity×positive causal-lift筛feature用于细解释；实际优化是selected components，不是声明仅更新SAE feature。CIRCE为targeted SFT，TITAN再DPO；preferred gold、rejected为SFT生成，word→phrase→sentence curriculum另变数据路径，KL保base。
- 证据：BPCC HiUr60k/HiSd35k，contrastive每对10k来自SFT split，baseline同splits/LoRA rank16/batch8，SFT3epoch+DPO2epoch/A10040GB，SAE latent14336。same3.14%trainable-budget LoRA SFT+DPO26.37 vsTITAN31.82 BLEU支持局部support选择价值，但不等匹配发现/SAE总计算与超参搜索。8选组件在未restrict的generalLoRA模型knockout BLEU25.53→16.54 vs随机25.41，减少targeted优化循环论证；仍不识别唯一/完整translation mechanism。其他语对**各自重新发现circuit再训练**，不是一个mask无更新transfer。
- 反侧：主表TITAN相对GemmaDPO HiUr TER52.30>42.37、UrHi72.10>44.39，不能说全metric优；摘要33.75/45.86%用SFT为分母，不能写超过最强DPO同幅。英语embedding cosine负值不证明完全无English-mediated computation，更不反驳所有语言的pivot；单base/指定contrastive prompts、counterfactual多属性联改限制因果。human样本/多seed及CI未完整披露，专家阈值率不授统一真实翻译可靠性。发现干预和SAE明确昂贵，参数少不等总费少。
- actual owner：`TRAIN-LORA` Ch30，实际110–132现probe-derived rowmask与PreciseShield限制，以及688–706 merge交接；Ch5坐标/feature/causal distinction也实际读。现正文已有“update support与lowrank分责、probe非真值、小参数不免全forward/发现成本”，这些具体NC；新差额是**subspace counterfactual intervention用于选更新组件，而不是仅关联probe**。若采用最小PRE，置当前行为probe更新面段后，只增加该选mask路径及在非targeted模型knockout验证、受限因果/代价，不搬语言榜单或English-pivot断言。需要可信干预/组件mask及独立retain回归，否则回普通LoRA/full update。

## S17. 2610.21763v1 — Audio Bias Mitigation

- 原源：[abs](https://arxiv.org/abs/2610.21763)、[v1 HTML](https://arxiv.org/html/2610.21763v1)。完整HTML摘要、§3–7/T1–4、Limitations及AppB必要配置。未核代码/复现。
- 准入/评分：声学attribute读出降到chance容易被当已移除representation → adversarial encoder在真实AuLLM中可借输出常数/拒答达标，后续mixed-teacher distillation又可能恢复bias → 改变“unlearning通过”和“attribute-sensitive行为消除”的验收。`2+1+2=5`；主要采用负面边界，不照录成功宣传。
- 方法：Qwen2Audio7B、Qwen3Omni30B-A3B、Nemotron3NanoOmni30B-A3B，关闭CoT。仅audioencoder全参更新，meanpool接GRL和binary classifier，genderCE+γLMCE；4000 gender-balanced、filtered SIFT/VCTK，一epoch，48超参×4checkpoint，从direct-prompt genderacc<60%中按MMAU最高选择，移除classifier后评。第二步只decoder attention LoRA，4000原teacher factual+4000GUM ImpGender样本logit KL、按sample长度归一，一epoch，8configs×10checkpoints，筛genderacc≥70%和MMAU≥97%原值再挑最低bias。不是纯encoder零信息证明，也不是deployment runtime去属性。
- 关键反证：Qwen3 GUM acc54.5%但95.5%直接预测F；Nemotron acc50.8%但拒答37.1%，非拒答acc80.8%、另pronoun72%仍正确。chance aggregate不等gender representation已删除，gender知觉/拒答/错误代词/偏见关联须分账。GUM generalMMAU Qwen3 75.0→71.3、Nemotron75.3→73.5，也非无损。distilled Qwen3/Nemotron 86.3%/83.8%checkpoints比原bias更高，挑最优只略降LOR .24→.22/.25→.21；不是全部训练失败也非通用bias消除。biasLOR降低可伴统一选某刻板词，open adjectives减少又混入输出缩短。
- 条件/费用：970录音来自BritishDialects/SpeechArchive；restricted bias23280prompt-recording，generalMMAU908（已过滤gender），ImpGender34prompts×240recordings，单英文/二元speaker标注，非真实genderidentity/所有语言。small curated改进只是future；无real-world语音指令评价。Transformers/AdamW/Accelerate、vLLM，batch8/WD.005、单epoch约2h；A40/L40/H100/RTX6000Pro等48/95GB，模型train95/190GB，precision未披露。全grid、teacher generation/logits、两phase与多consumer评价均付费；不能用一最佳checkpoint当无selectionbias证据。
- actual owner：`MULTIMODAL-REPRESENTATION` Ch23，已实际读53–74音频layer/probe身份与群体读出限制、邻Ch24/Ch5交接。现语音probe差小不授无偏、末层分数不批准所有consumer迁移已具体NC。缺口是**adversarial后direct readout chance可来自常标签或拒答，而非表征删除；attribute知觉、行为关联、pronoun utility要分别验收**。最小PRE可放群体probe段后、speaker-change分支前，不把binary性别任务扩大为fairness证书或推荐固定GRL recipe；信号仍可泄露时保原声/专用接口及明确不确定回答，生产permissions另管。

## S18. 2610.22312v1 — Grid-Bench

- 原源：[abs](https://arxiv.org/abs/2610.22312)、[v1 HTML](https://arxiv.org/html/2610.22312v1)。实际§3–5/Eq1–4/T1–4、AppC.1/C.3/C.4与matched-state/Copy/Zero直接反侧。未跑simulator/artifact。
- 准入/评分：单event精确或长history全错的EM都不足定位state prediction → 同一初态/历史prefix独立请求完整grid，将full-state恢复、错误extent与initial-final更新/保留分区拆开，并比copy/zero → 改变长horizon状态预测的失败测量，而不只加八类任务。`2+1+2=5`。
- 机制/测量：8deterministic transition families、2/3/4D约同252/256cells，core family单一但穿插SET；rules完整已知、全history文本给模型一次响应，无tools，不是在线action选择/learned sim rollout。248独立reference trajectories各6prefix T0/1/8/16/32/64，1488instances×6models，bootstrap2000整trajectory保prefix相关。full-world EM含invalid为0；cellaccuracy只valid，errorquantiles只valid incorrect；changed/unchanged由初/终值定义，unchanged可能中间改后恢复，不能叫从未受影响。Copy/Zero均按各model自己的valid子人口配对，不跨模型直接比较CA均值。
- 实证/反侧：GPT5.6Sol单event95%→T64约13%，单步相似模型在长history分化；但同history后prefix对而前prefix错（独立queries）不证明持续内部state repair或所有轨迹单调累错。同T8共同84个validincorrect Kimi/MiniMax median错14/67，说明EM不辨局部错误程度。T64 ClaudeCA90.5但valid仅58/192，不得对比Sol81.6且191/192宣布Claude更强。Sol比copy约+31pts，MiniMax约+1.5，不能把全部CA当动态推断；late-half-only执行只3/192 EM支持该suffixbaseline不够，不证明模型没走shortcut。维度改变同时改邻域/坐标arity，workload与状态变化量也耦合，非单因果dimension效应。
- 运行边界：固定prompt0.4，onecompletion、128k combined cap、7200s deadline，high reasoning（MiniMax native），温度/top_p/seed省略，NAIRR/Bedrock各route，收集9/16–24UTC。重试仅technical前置，delivered失败保留；无同条件重复generation估计，bootstrap只benchmark人口。hardware/precision实际完整费用ND；生成reference、API长输出、抽取与验证有费。只明确symbolicfullyspecified worlds，不能授真实physical dynamics或planning安全。
- actual owner：`MULTIMODAL-WORLD-MODELS` Ch25，实际949–975及1084–1100，另读Ch23关系serialization交接。现one-step与long-horizon/下游control分账、transition不等planning可用均具体NC。缺口是**完整state EM之外，按有效返回coverage/错误cells与初终更新—保留分区对照Copy/Zero**。最小PRE可在Evaluation首两段后，作为离散可执行oracle下的诊断分支，保invalid分母、paired baselines与final-only不识别内部算法；不复制全部taxonomy，不从此宣布LLM没有worldmodel。

## S19. 2610.22158v1 — PremiseSQL

- 原源：[abs](https://arxiv.org/abs/2610.22158)、[v1 HTML](https://arxiv.org/html/2610.22158v1)。实际§3–5/T3–4，A.2、B.6–B.8，必要judge/human与executed-original对照；未核代码/复现。
- 准入/评分：多拒答可能仅服从“问题有错”提示而非识别错前提 → fixed original/flawed pair在Base/可能错/断言错三prompt下分开测validity自述、grounded critique和SQL行为 → 改变可靠abstention的treatment与反事实负控。`2+1+2=5`。
- 标签/设计：1800原query及taxonomy合成flaw（9类各200），label取query+schema+assumed SQL能力，不随prompt改；Explicit的“肯定有错”在original上故意为false。flawed y1是positive，不要倒置正负；DET/TYPE与ordinal SQL abstention分开，original GEN只是coverage、VAL是is_valid字段不是SQL准确。15192生成候选经过GPT/Gemini与human筛2248pool，E3.2 schema缺失另造；重过滤和synthetic taxonomy限制自然mistake外推。
- 评价/反侧：16models×3600requests×3=172800，temp0/defaultAPI。Base DET .319、originalGEN .988；Explicit DET .931却GEN .523/VAL .321，Qwen397 .998normalizedSQL但originalGEN .004，直接否定高abstention=可靠critique。Base→Implicit同时增加is_valid字段，非纯warning单因素；Implicit→Explicit保持schema但改语义assertion。10kpaired querybootstrap所有32个DET增/GEN降CI不跨0，固定models/judges，不是服务noise或trainingseedCI。actualSQL执行仅1726可验gold originals（74另排），GEN .987/.902/.524对EX .713/.652/.399，conditionalEX .722/.722/.762；高相关不让GEN代替correctness，拒答提升conditionalEX仍可损整体utility。
- judge边界：GPT5.4/Opus4.6同rubric双评，2160 outputs人工抽检κ较高但只有两targetmodels、部分judge-target重合，非全人口truth。8000failure的四行为机制是observable attribution/strict双judge consensus，不是内部cause；不采用机制频率作为未筛自然总体率。构造、人审、172800API、judge与executedgold全费；hardware/precision/max length完整runtimeND，temp0不授endpoint确定性。
- actual owner：`PLATFORM-EVALUATION-SYSTEM` Ch66，实际54–106回答/拒答、输入完整性×output合同及438–440规则/自述/行为分账；这些通用原则均具体NC。缺口是**保持query/schema/reference label不变，交叉真实flaw与prompt“有flaw”断言，识别instruction-driven rejection**。最小PRE可接现输入完整性交叉两段后，保DET≠行为、original false rejection与execution分母，不搬SQLtaxonomy；无法核前提时Unknown/clarify，不用模型is_valid裁决schema真值。当前不写Ch66。

## S20. 2610.22249v1 — Not X, but When

- 原源：[abs](https://arxiv.org/abs/2610.22249)、[v1 HTML](https://arxiv.org/html/2610.22249v1)。实际§3–5、AppA.1/B/C必要annotation、quality-matching与checkpoint反侧；未核artifact/复现。
- 准入/评分：表达出现频率或无事实错误不足衡量是否有用 → 先查defect，再核当前context是否真有待否定alternative及是否推进QUD，对照保rejection的reorder与删rejection两种edit → 改变style/reward偏好的语义验收对象，防把高频即错误或reward偏好即合适。`2+1+2=5`，不采某中文句式频率本身。
- 诊断：完整answer+context上恢复scope/holder/QUD，T/A/P有独立缺陷才defective；否则R/L/U分别看有无可恢复rejection、独立context cue、是否推进未决问题，missing motivation只optional，不自动wrong。annotator盲source/score，事实与confidence另记。A原句、B先Y后拒X、D仅Y；A–B主要order，A–D删语义内容，不是意义完全固定的style干预。judge双order平均ordinal preference不是概率校准；RM按AarmSD归一且winrate排tie。
- 实证/反侧：1061中文prompts/5285APIanswers，307selected occurrences中52.8%optional、1.3%defective，但Claude服务拒1留missing；不是全部answers有52.8%问题。human reference不同prompt、detector也较宽；33humantext功能label由Codex自动，未做model样本同样审核，不能叫33humanannotated gold。100共同case两linguist top77%/κ.577、terminal66%/κ.521，细taxonomy有不确定性。3/5RM optional非tie原order胜68.3–76.8%，InternLM反向；质量匹配仍73.1–78.3%，但HY3 qualityproxy非真gold。Claude/GPT substantive−unlicensed差CI含0，不证明数学意义完全insensitive。
- 归因/成本：12opencheckpoints五family/12518answers，所有SFT与两个DPOstage density上涨、chosen多该式+14.7/+26.5%是观察关联；未控制retraining/data composition/update budgets，不授SFT/DPO固有因果或一刀切禁止句式。humanfrequency不同任务及输出长度/截断、content-filter/overlength exclusion影响分母；singleMandarin construction/无readeruserstudy，不授机器文本鉴别或annoyance结论。配对edit、人审、quality/5RM/2judge及generation成本另计，硬件/precision/完整训练费用ND。
- actual owner：`PLATFORM-EVALUATION-SYSTEM` Ch66，实际451–478 qualitymatched bias/来源与内容/风格proxy，邻Ch31偏好非真理也实读。现“qualityproxy不是gold、改写可能改内容、偏好不等truth”具体NC。新差额是**把事实正确但不必要的context-unlicensed表达与真实defect分开，再测evaluator是否辨其功能**。最小PRE可接qualitymatched bias解释段，保reorder与删content不同treatment、频率不等appropriateness、观察training不授cause；不是在Prompt章禁一句话或宣称已解决写作tic。

## S21. 2610.22213v1 — RBCD Generalization（中心争议隔离）

- 原源：[abs](https://arxiv.org/abs/2610.22213)、[v1 HTML](https://arxiv.org/html/2610.22213v1)。完整题摘后，为决定准入的actual theorem定点读Def1、§3.1–3.3、§4.1/Thm2–3/Eq14–22证明、§4.2/Thm4及§4.3结构假设；没有遍历旧稿/附件。唯一v1未见撤回。
- 原拟增量/评分：仅优化stationarity不等population stationarity → uniform随机block的full-empirical partial gradient用self-bounding和block矩恒等式，声称无需随机partial-gradient额外moment assumption并可early-stop balance → 或可修正block update的优化/泛化边界。`2+1+2=5`，按中心争议深入而非因纯理论排除；目前**不采用其rate/最优停止规则**。
- 明确scope：IID样本、非负loss、全局L-smooth及empirical partial-gradient Lipschitz、uniform blocks、w1=0；每step是全经验风险的一个block gradient，不是minibatch SGD、Adam或选择性adaptive blocks。所谓dimension-independent另限`l(y,<w,phi(x)>)`、bounded features与kernel eigenvalue多项式p>1衰减，不授任意Transformer。population PL用于functional excess risk，不是一般非凸自动有PL。
- 核心矛盾：Thm2 Eq14写`Ση||∇F_S||² ≲ K L ηmax F0 log(1/δ)`，但proof Eq20实际只得`≤4K(F0−F_T+1)+8KLηmaxF0log(1/δ)`；其独立的初始risk-drop项没有理由被`ηmax`吸收。按文中允许常步长η>0、K1、L1、所有样本同`f(w)=1/2(w−1)^2`、w1=0、T≈1/η，左侧精确为`[1−(1−η)^(2T)]/(2−η)`趋正数，右侧固定δ下趋0，违反其universal-constant约定。这是本人按原定义直接代入的反例，不称作者已认错；HTML原公式及proof均有TeX字样，不是仅OCR掉项。
- 处置：依赖Thm2的population bound/iterate norm与更快early-stop结论至少受此冲突影响，不把其余Thm4/6全部宣布已独立证伪，也不继续替作者重证。暂缓/本窗中心争议保留，**不进入Books、不为coverage或泛化保证提供正面证据**。可接受重开是作者正式corrigendum/修正精确bound与假设，或独立可核证明解释为何常步长/反例不在合同内；不等待无限外部回复。
- actual owner：`WORLDVIEW-WHY-MODELS-LEARN` Ch4为优化/泛化合同路由，`TRAIN-PRETRAINING`不接管未经核的理论rate。此处不是已有覆盖结论，也不建议PRE；维持既有train/held-out分责，不因出现一篇rate争议改写一般优化认识。

## S22. 2610.21995v1 — Interfaces and Modules / UWE

- 原源：[abs](https://arxiv.org/abs/2610.21995)、[v1 HTML](https://arxiv.org/html/2610.21995v1)。实际§2–6/Def2.1/Thm2.2/Remark2.3/T1–5、compiler基本constraint scope与resource协议正文；未核compiler实现/完整proof或复现。
- 准入/评分：neuron graph全局attention昂贵，按层手工symmetry又难跨架构 → 以必须共同permutation的coordinate spaces为interfaces、operation occurrences为typed modules，由supported-op constraints编译共享作用，再在invariant interface summaries上global attention → 改变weight-space学习的graph单位与可验证symmetry接口。`2+2+2=6`。
- 机制/保证：residual addition/norm/activation glue坐标，concat/head boundary split，linear不glue in/out；split沿glue传播到fixed point，再按同一permutation equivalence classes立interface，external IO/fixedstate固定，有alias/sharedstorage规则，unsupported即拒。参数reindex可逆、每distinct tensor一次；encoder cell lift仍可能有fixed-width压缩损失。Gamma为compiler constraints的精确解；加受支持head/module exchange，function-preservation是soundness，**不证明所有function-preserving变换完整**，尤其continuous basis/key-bias symmetries不全含。独立q/k共享但v可独立、完整head exchange须连outputblocks一起；不是任意headcoordinate混换。
- Encoder：local cell row/column equivariantupdates、interface coordinate pooling成invariant summary，再globalattention、broadcast；narrow cellfeatures/widerinterfacestates降低memory。全图不等自动语义表示或知识地址，representable symmetry不授actual predictive transfer。compilertrace eval-mode、shape/dtype/operator规则，不看数值weight来决定接口；arbitraryattentionmask/crossattention/RoPE/recurrence/unsupportedsharing明确拒。
- 评价/反侧：1200CIFAR100 ViT、100architectures×12recipes，70/15/15按architecture整组切，common train最大2.12M，beyondtest2.8–9.1M；60clean/blur/noise superclassloss targets，τ先在每架构12network内部排序再均架构，不是跨架构总排名。common UWEτ.7965 vsbestbaseline.5455，beyond.7538vs.5795；singlemetamodelseed，无trainseedvariance，full-cohort同时改train/test人口不隔离adding-large原因。CNNzoo .933低于best.941，removecodes commonMSE .27略优于.28而ranking差。
- resource：common/full A10 training8.9/23h，比NGGNN约3×/1.6×慢；低memory不等更快。H100、75GiB cap、batch1/firstAdamW训练step、1–100M随机targets+syntheticlabels；nativeViT/GPT2到355M可step，不证明真实大模型quality（Table1更大graph数字不是其实际trainingquality）。manysmallkernels、固定cell压缩、只一ViTfamily/task都是反侧；precision等完整runtime未核，不认性能SLO。compiler、参数features、metamodel训练和heldout验证全费。
- actual owner：`WORLDVIEW-REPRESENTATION` Ch5，实际18–54现神经元permutation和“坐标非语义身份”、邻Ch4/6交接可沿未变上下文；该原则具体NC。差额是**若把weights当学习对象，可先由operation constraints恢复必须joint作用的坐标接口，global通信移到invariant摘要**，不是解释activation的普通graph。最小PRE放permutation例后：保supportedconstraints sound-not-complete、IO/position/alias限制和scaling≠quality；不在Ch59把metamodel预测当registrytruth，不借该文提出新增前沿owner。

## S23. 2610.22238v1 — SIRS

- 原源：[abs](https://arxiv.org/abs/2610.22238)、[v1 HTML](https://arxiv.org/html/2610.22238v1)。实际§3–6/Alg1–2/Prop4.1/Thm5.1/5.3/Lemma5.2及直接proof sketch解释。一次HTML空请求后同URL成功，未需PDF或实现。公开日复用root本日LG Fri16首16核验。
- 准入/评分：同轮独立marginals忽略joint依赖，全ratio纠偏要逐token query → 随机single-increment估logratio，再Poissonized Bernoullifactory形成合法accept概率，clipping换误差/查询数，复用单query全部remainingconditionals做RB → 新增与缩小block不同的可分析纠偏选择。`2+1+2=5`，小exact-scoretoy不构成排除理由。
- 机制：block由已revealed状态提出，proposal为各conditional marginals乘积；joint/proposal logratio沿randomorder分tokenincrements。`n*delta`单sample对logratio无偏，但**exp无偏log估计一般不无偏**，故J~Poisson(2B)、独立incrementsclip[-B,B]，以product[(Wclip+B)/(2B)]作随机acceptprob；期望为clipped-mean exponential，保持该修正目标不是无条件原data。B0时J0全接纳退parallel，exactscore且不clip才recoverdata。每query给remaining全部conditionals，先平均再clip的RB改善clipping bound，不是通过“无偏accept更精确”改变未clip输出。
- 理论/代价：expected queries/step≤`(1+2B)exp(2B)`，固定B才与blocksize解耦，不是每step最多一次/constant latency。KL分clipping、proposal misspecification与acceptscoreerror；exactscore后二者0，真实scoreerror带expB系数会放大，大B不保证neterror更小；n也进入scaledincrement/clipping。Thm界要求relative probabilities/相关χ²、logerror条件可定义，未给任意neuralLM已满足认证。RB只更小bound不保证每setting实测KL单调，early-reject优化保同acceptlaw但随机重试tail仍在。
- 评价/反侧：exact conditional Ising L8/16、6couplings与Polya L256/1024/V32/6strengths，randompermutation independenttokens、B1/8…2，以KL与expectedqueries比较小blockparallel/sequential；图64/32permutations×4sequences，near0按2SE放bottom不证明exactzero。weakdependence RB纠大block更合算，strongdependence**小blockparallel更便宜且同budget更好**；无需神经训练的toy支持机制边界但没有LLMaccuracy、walltime/hardware/precision/batch/SLO证明。query是整conditionals oracle计数，缓存、采样/ratio/RB聚合与随机重试全费。
- actual owner：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，实际632–690现entropy-sum与conditional totalcorrelation分解，后者已具体承载perfectpredictor也有parallelfactorization误差及小toy不授SLO；这些NC。新差额是**同一block用随机accept/reject纠偏，而不是只改变揭示顺序/分块**，以及clip/RB/exponentiation边界。最小PRE置现factorization-profile两段后、learnability理论前，只保有界factory与fixedB查询/真实score反侧；不能将SIRS类比第48章而承诺保持真实LM分布。strongdependency/scoreerror不稳时逐token或小块原sampler继续成立。

## S24. 2610.22236v1 — Training-Free On-Policy Distillation

- 原源：[abs](https://arxiv.org/abs/2610.22236)、[v1 HTML](https://arxiv.org/html/2610.22236v1)。实际§3–5/Eq1–4/Prop3.1/T2–3、AppA closedform scope、AppB完整必要protocol/compute与AppC precision/rollout反侧。公开日复用root LG Fri16，未核代码/复现。
- 准入/评分：same-base specialists合并的二阶统计常取fixedcorpus，却可能不代表长reasoning运行输入 → 以各teacher自己的rollout收layer-input uncenteredGram，剔repeatloop避免tokenmass占统计，再闭式RegMean合并 → 改变校准人口及precision验收，而非声称新发明least squares。`2+1+2=5`。
- 机制：固定teacher-layer输入分布，min ΣwE||Wx−Wdx||²，Δ*=ΣΔdGd(ΣGd)^−1；offdiagshrink α.9相当加coordinatepenalty，已不是未regularize原objective。equalG退weightedaverage，不是taskarithmetic；orthogonalrange+pseudoinverse才能各自exactresponse。这里on-policy是teacher-generated（非严格studentonpolicy），全部prompt/answertoken做Gram，按domain totaltokens归一；长loop虽少可主导domain内统计。sharedQKV/gateup共享Gram，FP64solve，nonlinear/norm/embed用taskarithmetic；每层fixedinput最优**不等端到端studentinput漂移后精确distillation**。
- 实验：same Olmo3 7B base及Math/Code RL-zero两个teacher，各256训练题、mathtemp.7/topp.9/31744，codetemp1/p1/32768，vLLM。math19truncated全loop，默认keep175correctfinishedloopfree；code241可stdin题92pass，reference自身只有212/241pass，verifier有qualification。main sevenbench mean61.1高于math59.8/code53.6，但releasedBF16与fusedFP16；fused存FP32（BF16round updatecos约.96），matchedFP16 AIME只是within约1pt/30题×4samples，不认small差resolvedsuperiority。MATH/OlympiadBench/HumanEval/MBPP各sample1，threecompetition各30×4，未披露独立trainseedCI。
- 直接反侧/归因：allrollouts AIME与taskarithmetic相当；只去loop恢复hardmath，进一步仅correct未再改善；verifiedcode也无明确额外益，easierbench final90.8/84.1/67.5低于未correctfilter93.2/87.2/70.1，不能把筛更严自动当质量更好。tokenKL/argmaxagreement高不代表longderivation关键决策可靠；math3:1weight挽math牺牲code，studentrollouts不胜cleanteacher。fewGP hours不含所有eval，48GB单GPU/process，rollouts64题≈1GPUh、statistics2.6M≈40m、solve25m、两teacher约10GPUh，AIMEeval每model另2.5–3h；具体GPU型号ND，不宣称在线SLO或所有distillation免训练。
- actual owner：`TRAIN-LORA` Ch30，实际688–718包含ACT-Mat：samebase/architecture/coordinates、真实uncenteredsecondmoment的layer-output leastsquares、fullnetwork非保真及有数据时核actualinputstatistics均已具体NC；Ch29多teacherOPD只是监督consumer，不能在两章重复closedform。真正差额是**teacher自身长rollout的loop tokenmass使Gram偏向退化方向，以及融合精度需与specialist matched**。最小PRE置ACT-Mat两段后，保持statisticalpopulation/loopfilter/FP32store–FP16eval身份，明确forward+solve仍费、genericOPD/independent specialists继续适用异构/质量不稳。不采题名的“整网精确/普遍不需训练”断言。

## S25. 本轮十项有界闭合

10项完整题摘/轻量当前标记已核，9项必要标准Source/具体owner差额可供独核，RBCD一项中心证明争议安全隔离；未因小模型、负面结果或理论排除，亦未用模型映射/榜单代替贡献。未改Report/README/LS或这十项owner，未stage/commit/push。S15–S24的PRE均为建议，未授实际采用/POST；root独核后决定NC、仅报告或有限写入。停止新增来源/日期；下一步仅执行root已明确另授的原五family/四Books文件窄写，不将本轮十项夹带入书。

## S26. 原五 family / 四 owner 已授权窄写保存（非独立 POST）

root实际独核S1–S12的必要Source与最小PRE语义后，明确授Ch20 EMO、Ch24 MultiTargetDLM、Ch48 HyCo及Ch78 SpecAgent/InternDecision四文件窄写。本人重读Books上下文/实际局部与邻章交接，按五family各两短段及本人Review note保存；没有改Ch29/33/66/77或S15–S24十项owner。已实际顺读新增与完整局部两侧、五本人注，保旧文与其他修改；使用git实际跟踪的小写`books/`路径限定diff，numstat为6/6/6/12 added、0 deleted，diff --check通过（大写Books路径在此mac文件系统可读，但不能拿其空gitpath结果作check证据）。无stage/commit/push、未跑模型/API或复现。作者自读不当独立POST；root另行核实际正文/邻接/注后决定接纳，不预签POST或DAY。后续仅按root指定6项CV必要Source，不扩发现/日期。

## S27. 原五 family POST 既成状态与本轮六项边界

root随后实际读回原五family的新两段、完整局部邻接及本人notes，确认Source/PRE相符并明确POST PASS，授本人仅行政同步五条notes；本条只记录该独立检查已发生，不由作者自行签POST，也不授DAY。原正文不重写。以下仅root指定六项CV：22217、22200、22075、22070、22060、21937；复用REVIEW R8完整题摘/当前唯一v1轻量标记及root官方Fri16 CV列表公开日依据，不把submitted Oct15当公开日。未扩初筛名单。当前精确v1 HTML全部取得，早先未轮询的异步空stdout不当真实空页；未需PDF、未遍历全附件/实现或追时刻。

## S28. 2610.22217v1 — SCOPED

- 原源：[abs](https://arxiv.org/abs/2610.22217)、[v1 HTML](https://arxiv.org/html/2610.22217v1)。实际§3/Eq1–9、§4配置、§5/T1–2、AppA.2/A.5/A.8/A.9及梯度诊断必要段。当前唯一v1/无可见撤回纠错沿R8；未核代码/复现。
- 准入/评分：直接混合能力RL可能损坏已会能力 → 分别训练四个capability experts，再把奖励筛选的成功/失败轨迹反思为teacher-only procedural skill，学生在自己的prefix蒸馏 → 核验由独立专家和特权上下文组合而非混合reward直接更新的取舍。`2+1+2=5`；不把论文所谓reward purity或跨任务无冲突预先当真。
- 核心：四expert同Qwen3VL base，各自RL；按capability label选择teacher，teacher看到当前capability skill，student rollout及推理都不需要skill。成功和失败轨迹共同构造skill，不是逐题gold答案；source train split、去重/子类平衡，不使用eval。按student已访问prefix的token reverse KL传能力，正文公式为full-vocab目标，但配置loss是`k_1`估计，不能声称实现精确全词表KL。相同初始化/route能力标签是条件，不授任意异构teacher可无代价融合。
- 证据/反侧：8B平均73.13，对base67.30/MixRL69.31/无skill72.39；skill自身增量仅.74，不能把全部5.83归skill。CC-OCR88.79低于无skill88.89、PixMo相同79.89，4B MMSI29.4低于base30.2，专家skill也可伤其他能力。梯度cosine是32样本/当前checkpoint的局部方向诊断，不证明全局不可避免冲突；retention在固定base greedy轨迹上量observed-token logprob shift的cosine/投影，既不等下游accuracy，也不由R=1推出全向量相同。trajectory embedding近似可来自模板，attention命中也不证明因果grounding。格式/文本F1等reward仍是proxy，没有专门受控reward-hack反例认证“纯净”。
- 条件/成本：student TP2/teacher TP1，3epochs、batch256、每prompt1response、prompt12288/response8096、lr1e-6、BF16；expert EasyR1 3epochs、batch128/actor64、8responses、8192长度、KL.01。A80080GB，GPU数量/全GPUh Not Disclosed。四专家RL、轨迹合成反思、teacher/student forward、route及retain回归全费，不能只算最终student推理。
- actual owner/具体NC：`TRAIN-SFT` Ch29实际424–462的同prefix多teacher选择与当前OPRD、590–640的Context Distillation已经具体承载**student不见teacher特权instruction，在自己的prefix接同位置分布监督，部署不依赖该instruction；teacher选择/target身份不能合并成真值**。此处expert-derived skill是这一接口的受限验证/构造recipe，未证明全局reward purity或独立新保证，故建议这些核心命题已有覆盖、NC，不为四能力名称新增平行段。方法与能力反退保留报告；不是以已有覆盖撤销候选/降低审阅。

## S29. 2610.22200v1 — OpenGCUA

- 原源：[abs](https://arxiv.org/abs/2610.22200)、[v1 HTML](https://arxiv.org/html/2610.22200v1)。实际§3全部机制、T2–4、§4/T5与AppA evaluation protocol；R8唯一v1/当前标记有效复用。没有trained model release；未核runtime实现/复现/真实设备。
- 准入/评分：固定GUI批次或独立shell调用仍须模型每次协调跨接口条件 → 一个Python program内可联GUI/PyAutoGUI与shell、检查中间stdout/exit/state并分支，另按需投递截图 → 改变proposal粒度、runtime控制流与observation开销边界。`2+2+2=6`。
- 核心分工：程序仍由可信interpreter执行；shell可返回structured state，模型不必为每个内部条件再次生成。GUI baseline本来已能batch，不能把收益全写成首次batch；OSWorld不使用Playwright，真实device可用不同SDK。`screenshot()`控制向模型投递，环境仍每step capture，**没有投递图不等没有采集**。todo的pending/attempted/changed_unverified/claimed_verified是模型自评，不是external successproof；intent annotation也不授权限。harness保rolling screenshot buffer/microcompaction，没有将全部持久上下文搬进模型。
- 评价：OSWorldv2.1 offline82（排26internet任务），8models GUI+batch到full mean45.3→64.9、平均相对steps−53%/tokens−27.2，但GPT token31.9>30.8、Gemini82>80.3；full共同改变多机制，不是program-only因果收益。code-only的三模型对照支持更窄增益，如Qwen57.2→62.4/steps66.1→54.9，不能与full64.0/57.0混列。T4 code Qwen62.4/54.9steps，加截图64.3却63steps，加intent61.5；DeepSeek加intent56.7→53.3。缓存命中上升也不保证质量或步数全优，microcompaction可降cache。AppA每task取latest evaluated attempt，不是bestscore；均值含失败，无独立多run CI披露。
- 成本/边界：cost/resource曲线对完整轨迹按预算阈值置最终score或0，非中途partial-credit或已实现adaptive budget策略。API价格/cachewrite估算，失败尝试仍费；time受API限流、并行VM、provider排队影响未控，不做SLO排名。真实macOS4任务只selected one-run，曾录至3attempt不等3run平均；短案例不授通用环境rank。persistent target handles显式绑定目标而非前台焦点，reset仍会失效；observed element ID不等无staleness。程序、截图capture/delivery、AX查询、interpreter、全部模型/工具等待及policy gates均付费，执行本地代码不授新权限或effect正确。
- actual owner/最小PRE建议：`AGENT-TOOL-CALLING` Ch78已实际读Tool Contract至执行/admission段及新增InternDecision/SpecAgent；现typed proposal、effect-time授权、连续gesture与反馈门不能由代码替代，这些NC。缺口是**同一个受审program可在GUI/shell间消费即时结构反馈分支；capture与delivery是不同观测成本**。可在连续gesture两段后、模型Proposal段前加两短段：程序是更大的proposal，仍经runtime权限、真实反馈与停止/hold；条件中间值缺失或不可信时退回逐步交互，少投图不当成功/安全证据。邻Ch81 portable workflow/authority已读，仍不重复接管执行权限；不写这些新段，待root独核。

## S30. 2610.22075v1 — Recurrent Retrofit

- 原源：[abs](https://arxiv.org/abs/2610.22075)、[v1 HTML](https://arxiv.org/html/2610.22075v1)。实际§3–6/T1–6与AppA.1完整必要配置，R8唯一v1/当前标记复用；未核代码/复现。
- 准入/评分：预训练VLM直接共享/剪层会破坏既有接口，参数变少又容易被当推理状态变少 → 剪中层后插入prelude-state adapter，依次文本恢复、projector对齐、视觉指令恢复，分别核per-pass KV → 改变retrofit恢复路径及权重/运行深度/状态账。`1+2+2=5`，不是新发明recurrence。
- 方法：TinyLLaVA1.4（TinyLlama1.1B22层+CLIPViTL14-336）去4–9六层，4prelude/8recurrent block/4coda；adapter把上一state和prelude concat后线性投影，block循环r6，存16个distinct层但走56层。全VLM1.4101B→1.1542B（−18.1%），LM减23.3%，adapter8.4M。S0只text backbone、冻视觉/projector，S1只projector，S2全VLM；原未剪teacher用于S0/S2 forwardKL+CE，S1无KD。阶段是额外训练，不是训练free置换。
- 条件/评价：main S0 60Btokens/SlimPajama85%+FineWebEdu15%、16GPUs、228874steps/seq2048/batch128；S1 493k/6426steps/batch96，S2 660k/6408steps/batch128/4GPUs、4visual:1text。Muon矩阵/其余AdamW、seed42；GPU型号/precision Not Disclosed于必要配置。7.5B ablation更换数据/预算，不能归单一结构。恢复同数据baseline avg55.80 vsretrofit58.13，GQA59.2<60.4/SQA59.1<60.2；其他converted model历史训练成本不同。移除S0或S1也改变数据/KD投入，不是只顺序因果。
- 直接反侧：固定r6只本深度稳定，r2/4/12/16崩溃/早停，GQA r5为43.1/r6为59.7/r8为50.9；sampled-depth训练r2–16稳定但收益饱和，不证明test-time scaling。default每pass独立KV为56/22=2.55×原模型；循环只保n1副本可到.727×KV却avg52.70<58.13，n3为1.45×/57.38。首次pass复用K/KV改forward并需相应训练，仍有质量退步，不能任意共享同地址cache当exact。参数少、activation/KV少、执行少与latency快四者不互推。
- actual owner/最小PRE：`MODEL-TRANSFORMER-LAYER` Ch17实际566–602“Parameter Depth≠Execution Depth”及650–680受限recurrent span，已经有存参/执行/训练预算外不稳/非免费KV的具体NC。仍可用一个最小段补**预训练retrofit需先恢复text、再重接projector、再恢复crossmodal路径；每pass状态有独立身份，剪权重不自动剪KV**，放现Parameter/Execution Depth后、连续思考分支前。以原同深feedforward或固定受训loop为退路，不推荐默认多loop，不把恢复recipe移交Ch23再复制。当前仅PRE待root。

## S31. 2610.22070v1 — Memory as Weights / MaLoW

- 原源：[abs](https://arxiv.org/abs/2610.22070)、[v1 HTML](https://arxiv.org/html/2610.22070v1)。实际§3/Eq1–10、§4/T1–4、AppA.1–3/A.5理论边界、C.1/C.4/C.5及D.1/T9–10直接消融。R8当前唯一v1有效复用；未核代码/复现。
- 准入/评分：流式历史不能持续塞显式attention，但静态summary不一定适合当前consumer → HyperNetwork将每段视觉历史更新为local recurrent+global状态，再forward写入session-specific低rank模块 → 核验模型状态改写如何代替一部分history token，不需test-time反向。`2+2+2=6`。
- 核心：逐decoder层learned queries汇聚带timestamp视觉特征（4layers/d512），再4层DeltaNet local state与独立global gated accumulation，converter生成rank8 LoRA各模块A/B。base冻结，训练NTP梯度穿过生成权重+γ.01 meanabs正则；inference只forward更新，不跑gradient，也不是永远静态merge。主训练2800steps/batch64/4H200BF16、AdamW8e-5，2秒clip/1fps；**Qwen3VL4B main当前window8秒，其他2秒**，不可统一写2秒输入。381kQA/55,867videos14数据集的LLM构造/验证有共享label bias，不当groundtruth全保。
- 理论限定：线性attention下历史KV和M=ΣvkT经rank投影压入gate/up权重，可对该近似线性history-input transform等价；完整softmax/normalization需feature近似、residual及Lipschitz误差条件。作者明确不证明learned state/MaLoW精确fullhistory attention，固定rank也不保任意历史/查询无损。C.1文字同时以median cosine distance .0542取β.05、却写keep `cos≤β`，Eq6的gated sum与C.1 uniformly averaged也未统一，不能替作者静默修成唯一gate recipe。
- 评价/反侧：Qwen4B StreamBench84.8/OVO69.3，MOSS总74.5>73.8但backward71.7<72.5、ASI62.8<64.5/HLD90.3<92.4；不能说全consumer改善。OVO HLD gold全“Unable to answer”有shortcut，base与新增训练数据未一因子隔离。rank8高于4/16不是容量单调；多module还可回退。history-retrieval877题/237videos、median gap12.1min，总22.8>21.4但部分层级低于VST，windows/fps/pixels不同且未见CI，不授公平同费胜出。100deterministic OVO latency包含本step update/LoRA生成应用/currentprefill和firsttoken，总152.89ms vsbase130.07；不含decode/resize/full answer，previous history已摄入，非全stream walltime/SLO。训练H200不自动证明该profile硬件，未见可复用完整profile配置。
- actual owner/具体NC：`MODEL-LONG-CONTEXT` Ch22实际732–750（尤其742）的**把evicted/history信息聚成request状态，经global query写动态lowrank模块，base不test-time反传；非静态LoRA、非exact档案、session reset/全费/fallback**已具体承载此接口。581固定状态collision及773sessionmutable分支又承载容量/lifetime。MaLoW视频聚合与local/global构造是该机制受限验证，当前gate文本冲突/理论不认证learnedstate exact，建议已有覆盖NC，不另造Agent外部memory或WorldModel owner。保存这些新验证/反侧至报告，不因为NC排除候选。

## S32. 2610.22060v1 — FeaTok

- 原源：[abs](https://arxiv.org/abs/2610.22060)、[v1 HTML](https://arxiv.org/html/2610.22060v1)。实际§2/Eq1–2、§3.1/3.3、§5，AppA tokenizer、C.1–3必要控制、D完整成本协议及G/T16；R8唯一v1/当前标记复用。未核代码、像素图或复现。
- 准入/评分：像素reconstruction逼token保局部细节，未必最易被生成器预测 → token梯度只来自冻结vision teacher的feature重建/约束，pixeldecoder保训练但stop-gradient隔离，另设global离散condition先生成 → 改变token objective与pixel输出consumer分工。`2+2+2=6`。
- 机制：E以同一frozen teacher初始化；patch target取四均布层各LN后平均，global target取末层（不要两者混用）。featuredecoder复原global+patch，L1+L2+cos，末层MSE维持原语义；16bit FSQ/STE。pixeldecoder仍联合训练，pixel/perceptual/Gram/adversarial/alignment loss只训其分支及输出projector，tokens被detach，因此不是取消pixel训练/费用。global也16bit独立code，AR先global再raster patches，pixeldecoder只读patch；global的职责是生成condition而非直接多给pixeldecoder一token。
- 评价/反侧：相同BAR-B/ImageNet256、50k生成、无guidance控制下，四encoder的feature-only patch目标改善3/4，SigLIP2例外；加global后均改善。MAE feature gFID6.40差于pixel5.74；该消融又改regularizer/末层target/globaltemp，不授单因子pretrainingobjective因果。pairedPSNR/SSIM全部下降，DINOv3 PSNR20.61→17.45，DINOv2 rFDr6可1.82→2.06，不能称保真重建无损。six-space gFDr6是各自train/val normalizer ratio均值，不是人类truth；guided RAEv2为2.17优于FeaTok3.08，unguided关系反过来。T2I预训sample数虽同、batch/steps不同不等compute匹配，finetune前GenEval.611<RAE.624/DPG79.8<81.7，不能全归objective。
- 成本协议：tokenizer H200/BF16、40epochs/200ksteps/batch256/AdamW，featureteacher与pixel分支都费；generator与decoder-refinement版本分开。TFLOPs按torch2 MAC=2FLOPs，含全生成loop+一次pixeldecode（.16TFLOPs），guidance复制batch但不复制decode；不是实延迟。L40SBF16/uncompiled端到端含decode，同时报matchedbatch256及各自bestbatch sweep；FeaTokB31.82img/s@1024低于BAR34.32，L15.35@512低于BAR17.02。RAE bestbatch8与此512不授同batch/在线tail-SLO比较。pixeldetail或featuretarget失配时原pixel-supervisedcodec仍合理，不把semantic目标当普适替代。
- actual owner/最小PRE：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24实际50–69已具体解释codec重建与learnability拉扯、RAEAR/REPA；这些NC。新增可两短段接RAEAR后、DiffusionFlow projection前：**feature-only指token梯度隔离，不是废除pixeldecoder；global-code作为AR条件与pixel重建读入分责**，并保重建退步/encoder例外及decoder全费。不要在Ch23再复制codec目标或以一个benchmark证明语义更好。当前仅PRE，未写六项Books。

## S33. 2610.21937v1 — Flow-CLIP

- 原源：[abs](https://arxiv.org/abs/2610.21937)、[v1 HTML](https://arxiv.org/html/2610.21937v1)。实际§3/Eq1–12/Alg1、§4.1–4.6/T1–7及replacement/统计/迁移直接反侧；R8当前唯一v1标记复用。未核artifact/复现、未看像素图；名称不表示Flow Matching或ODE生成。
- 准入/评分：global alignment能高分却不保证词与局部patch绑定 → tokenquery从同图patch支持构造residual，评分只加入修正前后pooled support的有符号增量，并以samecaption跨图的relative margin约束抑制text-only捷径 → 改变局部consumer评分和对照对象。`2+1+2=5`。
- 机制：CLIP冻结；normalized patch/query相似度先减patch mean、positivepart，context为Σep/N而非权重归一。`r=c−(qTc)q`先投切面，随后learnedW可改变方向，故**Wr/最终query不保证仍正交**。归一新query前后对同patchset各作logmeanexp，取signed delta，再对全部valid tokens平均（含function/subword/punctuation），global+αlocal；W0/α0可退global。不是parser识别对象或局部grounding真值。HNB fullcaption hardnegative配imageidentity多正例；CIMR对samecaption的正负margin比较matched与different-identity donor image，排已知positive；能抵消可加text-only/image-only项，不去掉全部非线性先验或构造错误。
- 控制/反侧：COCO113287images/566435records、501921可HN，CC3M97,734train/4096val且显式9image overlap；5epochs、三maps786432参数、AdamW8e-5/batch32+32HN、RTX3090/A800，FP32 score/noautocast/TF32关闭、预存FP16normalizedfeatures。sameglobalbaseline同epoch/data/optimizer的3runs平均11tasks67.73→71.10，七binding58.34→62.64；原CLIP到baseline的大增益不能全算local。image-cluster bootstrap10k只固定checkpoint/运行的数据不确定性，非trainseedCI，部分任务缺group无法该CI。COCOspatial pairedCI−3.20…−.04；加CIMR也非全task改善，ABC78.56→78.34/SwapA78.68→77.93/GQA45.18→44.97。
- 验收/成本：replacement保原gold，shuffle/fixed后的“accuracy”其实原caption偏好保留，不是新image正确率；ARO matched85.75→85.91、shuffle48.75→35.66支持该shortcut诊断，但六task shuffle仍50.38，不授语言bias移除。迁移SigLIP binding68.30→68.03、BLIP ARO91.50→90.85，CIFAR10064.5→58/ImageNetV254.7→47，CC训练COCOI2T50.4→43.1，localconsumer可伤global/classification。smallhead仍有token×patch工作、donor双图训练、backbone features与gallery评分全费，未给完整walltime/latency/SLO，不称免费头。
- actual owner/最小PRE：`MULTIMODAL-REPRESENTATION` Ch23实际151–174包括global≠denseconsumer、SAGA learned anchors与ObjectDINO局部consumer，通用原则具体NC。差额是**局部修正以同patchset前后support增量计分，再用samecaption跨图margin作负控**，可一短段接SAGA后/ObjectDINO前；保切面只在W前成立、旧gold retention不是新图truth和globalconsumer反退，退回原globalscore/明确consumer-specific validation。不挪Ch24按题名讲flow、不交Ch66重复维护表示机制。当前仅PRE待独核。

## S34. 指定六项必要 Source 闭合

六项实际必要method/evaluation/直接反侧充分，准确版本、日期依据层与actual owner已保存；SCOPED和MaLoW建议具体已有覆盖NC，其他四项最小PRE供root独核，不以NC倒改准入。没有外部正文访问阻断，implementation/复现/未披露runtime不冒充已验证；MaLoW gate文字不一致作为不能照抄recipe的限制，不靠猜测修复。未把候选数量/全部图附件当完成门槛。只原五family四文件行政notes同步已发生root POST，其余六项Books均未写；未改Report/README/LS/index、未stage/commit/push。本次指定六项后停止来源与日期扩展，不自行授POST或DAY。

## S35. 三 family 后续授权窄写已保存（actual POST 待 root）

root实际核S15–24后另授Ch30 TITAN/Training-FreeOPD与Ch23 AudioBias最小段及notes。本人重读Books合同、当前实际局部/邻接交接，保旧机制分别在更新支集probe、ACT-Mat实际Gram、语音群体probe后各加一段及章末本人注；完整新增/两侧/本人注已实际读回，限定小写gitpath diff --check通过。采用命题限S16/S24/S17，未夹带其他S15–24、CV6或旧历史。作者不签实际POST/DAY。随后root另授五family Ch23 Gen4P/DKVLM/FlowCLIP、Ch17 Retrofit、Ch78 OpenGCUA窄写；FeaTok交ORG_A唯一写，本人不动Ch24。该五项在本条时尚未保存，不预记完成。

## S36. 后五 family 授权窄写与实际自读

已按root另授范围保存Ch23 Gen4P（perceiver后）/DKVLM（query-view RoPE后）/FlowCLIP（SAGA后）各一短段，Ch17 Retrofit（parameter/executiondepth后）一段、Ch78 OpenGCUA（连续gesture后）两段及五本人notes。Gen4P/DKVLM的有效必要Source与最小稿复用REVIEW R9.1/R9.5，root已独核，不另造新的初审或发现层；本人实读这些记录及实际插点完整局部/邻章交接，采用范围保深度prior/非transition、valid geometry分支/非全局解因果、联合训练/局部反退与全部费用。FlowCLIP/RR/Open沿S33/S30/S29。

本人已实际顺读五项完整新增、两侧与notes；AudioBias首句进一步收窄为“拒答改变计分人口”，不猜测模型具体知道哪些被拒样本。此时Ch17/23/30/78限定小写gitpath diff --check通过，numstat4/16/8/18 added、0 deleted（Ch78包含先前已POST五family中的两项，非本轮净增计数）。未改其他Books、Report/LS/index，未stage/commit/push；全部八family实际POST仍待root，不由本自读授DAY。指定Source任务已闭，无新来源/下一日期扫描。

## S37. 本日最后 DC 指定集合 / 非作者复核边界

root另明确授最后有界集合：22035/21815/20981/21640必要Source与actual owner，另独核ROOT末尾22172/21162/21500/22230四项必要Source/PRE。只这八身份，不把DC全16标题变全文队列；日期复用root已完整核Fri16官方DC分组与精确uniquev1，新增四项本人又读当前完整abs/唯一v1、无可见撤回纠错（20981 submitted Oct14，另三Oct15均不当公开日）。精确v1 HTML八项全部正常取回，不需PDF、不读旧版本；本轮只扩本文件，不写Books、Report、LS或索引。BCL明确补§2/3前部，RemoteKV严格只§4/5.1–3/6.1–3；本文不将局部核验标为全论文/实现复现。

## S38. 2610.22035v1 — ETH / Data-Balanced HPP

- 原源：[abs](https://arxiv.org/abs/2610.22035)、[精确v1](https://arxiv.org/html/2610.22035v1)。实际§3–4全部、§6–8/关键T1–2与AppB convergence；§5搜索仅采用正文已明确四优化身份及§7.6必要反侧，不声称完整搜索证明/实现。
- 准入/评分：仅按stage层数平衡受存储与离散层粒度约束 → 多条不同PP/TP/DP配置的完整replicas分配不同local batch，再按参数坐标重组跨配置gradient blocks → 改变模型切分与数据切分联合搜索及同步对象。`2+2+2=6`。
- 机制：先各pipeline暂按GBS优化stage，再greedy按microbatch粒度分local batch，最后按其local batch再调stage，**三阶段heuristic不保globalopt**。pipeline组无序、stage组有序（1F1B earlystage activation寿命不同）；profiling记录各device/operator/TP/MBS的forward/backward、memory和消息成本。跨replica gradients先按layer/operator/maxTP分partition，较低TP块exchange/combine，再把相同DP成员组的blocks按layer序fusion，避免padding和每tensor单独launch。它不是无坐标的异形tensor直接AllReduce。
- 评价：Megatron改约9kLoC，PP/TP/DP+ZeRO1/2、1F1B；GPT3 350M–175B/Llama2-70B，Atlas910B2/B3/B4与A100/RTX3090，seq2048/GBS1024，100Gbps跨异构节点。报告iteration和search time分开，最高倍数不代表含一次性profile/search的全程time-to-quality。NVIDIA main只350M–13B；type-split同构pipelines在2/5模型已匹配ETH，其他3有1.17–1.36×，不等所有集群必须全搜索。recompute固定其他配置消融仅peakmemory1.8–5.7%，不把全部可运行长度归该项；runtime误差−6.7…6.6%、memory+4.9…7.4%是所测误差，不是全域容量证书。
- 反侧/未闭：α.5更快search却产生更慢配置，pruning不保最优；global batch约束正文是ΣLbs≥GBS而非严格等号，核心blockwise描述未明确unequal replica样本数的gradient normalization/overshoot处理，故不授exact original SGD或拷贝完整recipe。2000step Enwiki loss近似相同/约.1%差异只是短trainloss，不证所有heldout/数值等价，也不据无seed/CI数值签长期收敛。具体运行dtype/完整总GPUh Not Disclosed。更多DP可增通信；CP/EP和非1F1B需新model/同步验证，不能自动支持。所有profile、搜索、额外重算、重组/collective、状态与独立质量回归付费。
- actual owner/最小PRE：`TRAIN-PIPELINE-PARALLEL` Ch38实际246–274已有stage联合计算/容量与异构MoE计划，`TRAIN-MEGATRON` Ch40 149–175还有globalbatch不变量；这些具体NC。新增可在StageBalance的异构分支后加一段：**不同完整pipeline副本分不同local batch，使microbatch数成为比层数更细的平衡旋钮，同步须按真实参数分片对应而非物理buffer形状；样本权重/总batch是另一个必须验的合同**。不推荐原未闭normalization或最优保证；条件不稳保同构子组、统一配置与现1F1B。仅建议，不改Books。

## S39. 2610.21815v1 — Exact Makespan / GPipe Homogeneity Bias

- 原源：[abs](https://arxiv.org/abs/2610.21815)、[v1 HTML](https://arxiv.org/html/2610.21815v1)。实际§2–5三个recurrence/定理与必要proof、§7.1/7.2、§9/10直接生产/适用边界；未核artifact/复现，不采用§8对历史调度论文的泛化优先性声明。
- 准入/评分：同构bubble式被拿来规划异构forward流水 → 固定stage服务时延下区分一次fill/drain与稳态maxstage，通信只在理想不占stage的delay模型中为加项 → 改变低microbatch数的capacity/通信优先级解释。`2+1+2=5`，不是因其重述classical criticalpath而排除精确边界。
- 有效理论：纯forward、固定顺序、无限buffer、每stage τj/每link dj不随microbatch变、只相邻P2P。无通信`T(M)=Στ+(M−1)maxτ`，所以将每stage都设maxτ的同构式偏差`Σ(maxτ−τj)`是一次fill项而非steady斜率。完全async在其recurrence里每条传输无共享link排队/吞吐资源限制，`T=Στ+Σd+(M−1)maxτ`；blocking采用stage有效服务σ=τ+d则换maxσ。**“NCCL另stream”不保证真实通信满足该无带宽瓶颈模型**。boundedbuffer、带宽共享、prefill/decode交错、训练反向、cache/load变化均明确不覆盖。
- 核验/反侧：11constructed configs与20k随机配置×M共160k doubleprecision recurrence点（不是GPU实验/随机独立trial）验证给定公式，不证明模型适合真实runtime。例`[.5,1,1,5]`是normalized假设，不是实测GPUprofile。8571production gateway log只记单请求duration/queue，作者取各model/host最小duration拼“pipeline”；输出长度/模型数据不同，不是按stage分层真实PP makespan观测。`total≥duration`是queue非负，不验证async/blocking sandwich；文中7.2/9也作此限定，不将该日志或“minimum=exclusive”当硬件比率。无真实pipeline SLO/完整precision/多runCI可授。
- 不采用：§5/9对一个overlap fraction线性插值得斜率、两次测量固定ρ与“balance compute always dominates”不作为任意物理系统定律。ρ若由两个完整T定义只是该M下重参数化，未证明随M常数；服务/带宽/backpressure变化可超blocking简式，实际compute与link都须profile。理论求值/校准、buffer与真实测量也有费，非生产更快的新系统。
- actual owner/PRE：`TRAIN-PIPELINE-PARALLEL` Ch38实际67–89已将bubble式限定理想均衡forward、246–274已按maxstage与实际profile分责，故不是现文“错了”。最小可补**异构固定服务纯forward的Στ fill项及maxτ steady项，通信加项只在无独立网络吞吐约束模型成立**，接bubble示例后；不要把训练GPipe或一般NCCL直接替成此公式。新调度无可用profile时保现保守模型/实测，不将理论边界扩成服务保证。

## S40. 2610.20981v1 — Cyclotron

- 原源：[abs](https://arxiv.org/abs/2610.20981)、[v1 HTML](https://arxiv.org/html/2610.20981v1)。实际§3.1必要grammar/空间时间注解、§4全部dependency/communication lowering、§5与§6.1–3/关键T2–3；未核源码、生成程序或复现。
- 准入/评分：传统distributed algebra隐藏通信策略，改broadcast/ring常需改imperative控制 → 在iteration-space value之间显式写recurrence数据移动，另注space/time mapping，再生成配对send/receive/guard → 改变通信算法、物理映射与求值顺序的共同IR。`2+2+2=6`，LLM端到端不是准入唯一门槛，矩阵执行机制直接服务主线。
- 机制：external tensor access与iteration-space tile身份分开，同一坐标差映成跨PE移动或本地temporal carry。mapping后纯time offset标stale、从live ordering graph移除但仍读取旧register；live依赖toposort决定本step statement序，反推receive关系生成matching send/guards。原简单cycle例说明换mapping必须换read-before-clobber顺序；不由该例证明任意recurrence一定live-DAG/无覆盖危害。有限grammar `v/n/v+n`、约束/非recursivefunc、guards及initialconditions仍须合法，未核一般program soundness。block-cyclic虚拟PE再specialize/dedup可复用同tile；不是消去通信或任意collective正确性证明。
- 运行/评价：Python compiler→portableProtobuf，C++CPU/GPU runtime，Rust/DAM simulator默认无payload，仅行为模拟不等数值正确运行。Perlmutter16CPU节点/16A100（每node4、NVLink/Slingshot11），matchedprecision/tile/BLAS/thread/MPI，2warmup+4measured报告best而非均值CI；必要段未指明统一dtype。CPUCholesky部分schedule差于ScaLAPACK，赢家随machine/size/shape换。GPU hoststage对SLATE同transport才支持至1.24×；directGPU+outoforder对SLATE4.57–4.74×同时换transport，不能全归IR，对direct cuSolverMp1.12–1.28×还含scheduling差。T2 pingpongsolve1.72–1.83×是互补wavefront，非任意workload；T3 fused隐藏90%在imbalanced非blockcyclic，balanced只18–23%，不叫solve免费。
- 成本/边界：设计recurrences/mapping、编译/模拟、guards、buffer/register寿命、kernel/vendor调用、MPI、communication和完整验证均费；没有LLM质量/全服务latency或GPU任意拓扑验证。不以无死锁宣传代替执行check，更不将程序同义直接当浮点bitwise。
- actual owner/PRE：`INFER-TENSORRT-LLM` Ch49实际159–187 sequentialspec/schedule与layout分层、2305–2319 distributedtiling/资源坐标已有相邻分工，但**把通信本身写成iteration-space recurrences，mapping改变stale/live与生成配对通信顺序**未具体承载。最小一段置DistributedTiling首两段后，仅保该IR接口与需验证liveDAG/读旧值寿命/同步语义，不授通用安全编译器或端到端提速。通信策略在Ch36不再重复；普通库路径/显式验证P2P仍作退路。当前不写Books。

## S41. 2610.21640v1 — ReFlow

- 原源：[abs](https://arxiv.org/abs/2610.21640)、[v1 HTML](https://arxiv.org/html/2610.21640v1)。实际§4–6全部方法/Eq2–6/Alg1、§7/T1–3与availability；完整题摘/唯一v1轻量复核。未核代码或复现；availability明确代码待内部approval，不能称公开实现已验。
- 准入/评分：只放大异步lag仍受fresh生成速率限制 → batch中replay比例按供需变动但有cap，loss influence另downweight，worker按完整replica保shard布局切换role → 改变样本reuse/更新影响与弹性资源相互配合的控制。`2+2+2=6`。
- 核心：unused可以fresh/stale、replay是已用样本，buffer带policyversion、全局δ admission；σ限制每batch replay fraction，τ乘replay importanceweight，再按validtokenmass归一loss规模，两旋钮不是同义。partial请求在sync时hold后续写，必须沿现trajectory identity核逐段behavior而不能把version近当onpolicy。理论equalimportance-tokenmass、unused gradient无偏、fresh/replay centerederrors不相关、replaybias有界+Lsmooth才得局部errorbound/one-step progress；实际样本反复影响参数又被复用，**不相关不是已经证实的实际RL性质**，不采用普遍方差下降/收敛保证。
- 系统：prewarm hybrid worker兼具trainer/inference contexts，inactive模块CPUoffload/dormant；只按完整trainer/rollout replica组重配且尽可能保shardlayout。增加trainer以同shard rank广播model/optimizer，不任意reshard；新rollout拿最新权重，通常sync边界切换，startup、CPU驻留/复制及状态传输不消失。生成cap用EWMA/AIMD，token预测/当前KV/preempt做admission，siblingprefixaffinity可spill；不是严格未来KV上界。resource scheduler按idle校正producer/consumer速率外推可行离散比例、cooldown，非globalopt/无抖动证明。
- 评价/反侧：VeRL/Ray/vLLM/FSDP2，16nodes128H800、8×400Gbps、CUDA12.6/Torch2.7.1/NCCL2.26.2，Qwen3 4/8/14/32B/DAPO/APPS/ReTool；dtype/完整batch/长度/repeatseed在必要配置Not Disclosed。σ=τ=.5、δ1、Bmax=batch。tokens/s是**trainer本step处理tokens含replay**/step时间，不是unique fresh生成或有效新样本数；5warmup+5steps，coding10+10，非长程SLO。convergence主要training reward/step和walltime，无独立heldout能力/多seedCI，故只支持所测reward进程，不授comparable/better generalmodel。同期多机制baseline不能分摊headline2.06×因果；4GPU单生成scheduler消融+10.4%，32GPU切role5.72/9.20s都非零费。尚无replay-only充分matchedendtoend消融证明每component独立收益。
- actual owner/PRE：`TRAIN-GRPO` Ch33实际1670–1730已有policyidentity、boundedreplay与horizon/reuse/resource三账及相关性限制，2129–2150有partialrollout；这些具体NC。缺口只建议一短段接FIFO/reuse两段后：**batch replay admission fraction和loss influence分开，供需调节不得让replay tokens冒充fresh产量；弹性role改变以完整replica与原shard身份保状态，初始化/CPU驻留仍费**。不另在Ch41复制RL生命周期，不采理想variance保证；统计/身份/质量不稳回fresh-only、窄lag与固定资源。当前不写Books。

## S42. 非作者复核 ROOT 22172 EdgeFlow：限定机制通过，精确cost/approx不采用

- root是Source作者，本人实际独读[2610.22172v1](https://arxiv.org/html/2610.22172v1) §III-A/B全部及§V-A/B配置/主要带宽、长度、异构对照，未核IV全部LP/rounding证明与V-C simulation；沿root已读层不虚记全论文。准入2+2+2=6的混合ACT/directKV机制成立；不认证2approx。
- 验证支持：发送act-layer输入后target以同层权重重构其KV，其余层直接KV；先act可将targetcompute和后续transfer重叠，弱target或低带宽会改变分界。测试Qwen2.5-32B/Llama3.1-70B/fp16、WikiText2、consumerGPUs、100–900Mbps±30%，默认batch32/length32、长度到512；ACT/DKV共用targetselection，greedy另作对照；不是完整serving tail、网络断开后的recovery或续写语义精确实验。
- **新发现的模型边界**：III-A Eq5写lastACT到达Ta加单层recompute再与totaltransfer取max；III-B Eq9却取`max(totalACT+KV transfer,totalACT recompute)`，没有显式startup/drain依赖。P=1/KV层0时，实际至少一份activation先到再算，通常是a+c，而Eq9为max(a,c)。这是本人按其定义的反例，仅反对该式作为精确物理流水公式，不宣布混合接口/原受测结果全失效。均匀层cost及同hidden/数据layout也支撑不了任意heterogeneous层只数比例。故不采用其物理最优、2approx/安全保证，不再追全部证明。
- actual owner：`INFER-PD-DISAGGREGATION` Ch55实际80–126/408–442已有stateidentity/completion/cost及livehandoff，通用原则NC；最小PRE可只补**按层混合source activation→target局部KV重构与直接KV，带宽/目标compute决定候选分界**，并明确所有activation留存、重算、startup/drain、模型/adapter/dtype/position一致性与destinationcommit额外验。不能用原Eq9作recipe；重构身份/预算不稳回全KV/原tokenrecompute。ROOT写“不采用2approx”正确，需再保此Eq5/9矛盾，窄机制证据/PRE通过，不授BooksPOST。

## S43. 非作者复核 ROOT 21162 BCL：必要缺段已补，唯一 owner 选 Ch36

- 本人实际独读[精确v1](https://arxiv.org/html/2610.21162v1) §2/§3全部，§4.1–3必要lowerbounds及§6/9评价/边界；补齐root明确待的costmodel和算法前部。`2+2+2=6`可通过，主题是fixed-count trainer的rank-local grouping，不是纯paddingpacking。
- 确认`c(l)=α min(l,lmax)+β min(l,lmax)^2`是metadata proxy，cap/coeffs预先policy，不由BCL自动发现。每rank stages KB、每record恰一次、每pack恰B，只在窗口重排；LPT给least-loaded nonfull pack，heavy/light exchange仅接受降低maxcost且保持cardinality。无经典LPT approximation继承。lowerbound `max(S/K,max c)`、跨rankwindow总量差不可被localpermutation去掉；CV/η不授memoryfeasibility或近似attainability。重排序改变同一optimizer步的共批人口，非仅执行placement。
- §6复核支持ROOT描述：8H200/Llama3.2-1B/NeMoRL.7/FSDP2/bf16/FA3，3×300除20warmup，samep99cap。K1/K32才同rankreader/collector；pooledMFFD是跨campaign不同loader，不能单独归packing；Alpaca.4±1.4%不说显著，两个OOM对照没同本轮重跑。§9明确没heldoutquality/exactrestart，内部非LLM AUC不迁移。Hostmemory/首包等待/reader、sort/swap、shuffle/restart都费。未跑代码/训练。
- actual owner/PRE：`TRAIN-DISTRIBUTED-TRAINING` Ch36实际681–718的attentionworkloadpool**冻结本step multiset且可跨rank协调**与BCL不同；后者只ranklocal但跨K步重新分组，不能说原stepmembership不变。建议紧接该pool分支一短段，解释无crossrankmetadata的fixedB有界lookahead、不可消的单record/总window下界、合法顺序与checkpoint状态、按完整step而非CV验收。Ch27只交batchdataidentity，不重复算法；ROOT两候选owner由此确定Ch36，最小PRE通过，不授POST。

## S44. 非作者复核 ROOT 21500 Remote KV Tier：仅必要指定域通过

- 本人严格只读[精确v1](https://arxiv.org/html/2610.21500v1) §4、§5.1–3、§6.1–3，未读§5.4 bug实现/§6.4–6/§8，不冒称其三修复或throughput/kernel/总部署已独核。ROOT的7=2+2+3仅针对remotehit反证和collective恢复接口，必要受影响域已核；吞吐14/34%不由本核支撑。
- 正确推断：`Tload=T0+ns/B`对`n/R`，B>sR是必要bandwidth条件；有T0时有限B的真正break-even是`n>RT0/(1−sR/B)`，n>RT0只是其必要下限。singlepoint拟T0=.33s再验证三个非拟合point是局部拟合，非所有prompt/backend常数；16k fastestremote median.40仍慢recompute.31，cache价值可能是腾GPU而非降低median。同步hit-heavy λns/B>1说明该单server模型可失稳，不等任何rate/flow稳态证明。
- protocol：chunk c owner c modW，owner返回首ownedmissing的start，min得到全局连续前缀；无ownedhit也不能返回统一0。每rank先同顺序metadata/fingerprint/failure exchange、共同短前缀，再同顺序ownerbroadcast，避免**已参与且可progress**ranks因localfailure跳collective；不授crashedrank/永久GETstall或任意backend下永不hang，也不由fingerprint等于身份认证。跨engine W/布局/key身份一致仍是条件。
- 对照：GLM5.3FP8/8B300 PCP8/MLA、LMCache/Valkey、256tokenchunk；683request fullstream、450hit-heavy primedL2/L1empty。H2b async只有50.6%tokens远取、49%请求timeout重算，不能和H1b98.5%同hit率归纯async；8instances also改partition/带宽，H5b还加fixes。83.32→.67s是完整组合、私有primedtrace无eviction人口，不是所有requestSLO；同fastestmedian仍不及recompute，p99则更好。GPU7%→22%不是一般capacity收益，全部network、host、exchange、额外replicaservice及失败prefetch/recompute付费。
- actual owner/PRE：`INFER-GPU-MEMORY` Ch54实际288–355/652–660已有tiercapacity/placement和generation-ready，不把命中当免费带宽；但缺**以实际prefill rate为基准的T0+byte带宽门，及chunkowner首miss最小值/一致collective前缀**。可最小两段在层级策略后，保持完整benchmark条件/健康progress前提、慢load异步隔离与回重算，不搬未经本核的bugs/性能模块。Ch55已有handoff不复制。ROOT窄Source/PRE通过，需按这里收窄never-desync语义，不授POST。

## S45. 非作者复核 ROOT 22230 Meta Hardware Diversity：具体 NC

- 本人独读[2610.22230v1](https://arxiv.org/html/2610.22230v1) §III-B全部/Eq1–5（补root前半后的selector）、§V全部、§VI-A/B全部；未核§III其它/§IV/§VI-C后部或实现。2+2+2=6的hardware-parameterized解析selector与HBM影响recipe，作为公开局部证据通过，不照摘要optimal。
- Origami按matrixinstructions、LDS tile、L2/LLC共享与容量估miss/traffic，加入issue-rate、K-loop load/compute max、wave/tail与StreamK/XCDswizzle。它枚举有限合法catalog，hardwareconstant校准是前提；**相对exhaustiveautotune仅93%平均selectionefficiency**，不是零warmup总选最优/不付维护成本。regularGEMM数据搬运predictability不授任意稀疏/动态kernel，同义与实际数值执行仍另验。
- §V GPT1.3B AC内存取舍是直接语言训练案例，但1.35×仍绑定两平台/不同内存recipe；DLRM十模型8–128GPUs matchedbatch geomean101.2%，各model82–130%不是普胜。HBM扩batch另表、可移embedding/HSDP等联合收益不能全归selector。GEMM MI350X慢1.3–1.7×、无nativeTF32三BF16仿真；kernel时长加总忽略multistreamoverlap，不能当整step归因。dtype/shape与平台自定义spec需绑定，benchmark未披露所有step重复/CI/全TCO，功耗/可靠性不由此认证。
- actual owner/具体NC：`INFER-TENSORRT-LLM` Ch49实际662–704已逐项承载**完整operation descriptor/候选catalog、从problem/kernel/hardware常量推wave/tail/cache/occupancy/pipeline物理后果再选择、换GPU/dtype要重校准、actualcoverage与fallback**；其learnedrank实例不排除直接解析取min，因此本次解析实现/93%是该接口的新验证，不必重复追加另一通用costmodel段。HBM下batch/checkpoint/sharding/peak三账在Ch38 246–274/Ch40 batch合同和Ch54容量owner也已有具体承载，不因DLRM规模/声望另写机制。建议已有覆盖NC；ROOT“若现命题足则NC”的路由在actual文中成立，报告保验证和跨平台反退，不改书。

## S46. 最后 DC 有界 Source / 独核交付

新增四项必要Source与actual owner最小PRE已齐（S38–41），ROOT四项非作者必要域已核（S42–45）：BCL必要缺段恢复、Remote严格局部、EdgeFlow精确cost矛盾仅隔离强保证而保混合机制、Meta具体NC。没有访问型普通待办，不追实现/全附件/旧版；源头身份与Fri16公开日层复用root既有独立依据，不新造全分类召回。全部PRE只供root采用决策，**本轮不写任何Books**，不自行授POST/DAY、不扩发现/日期，不stage/commit/push。

本批最终实际读回检查时间：2026-10-17 10:23:22+08（时钟返回02:23:22UTC，仅执行时间，不作论文归属）。完整S37–46已读回，source行尾空白检查无命中；该文件仍untracked，限定git diff --check空输出不冒充已检查untracked全部内容。仅保存本文件，后续只待root必要采用/验收，不开启新池。

## S47. DC 七 family / 八机制段实际非 writer POST 通过

复核者：`live1017_org_b`，本层七项Books均由root写入，本人不是writer。结论：**七family八机制段及七新Review notes实际POST通过**。执行检查时间2026-10-17 10:27:53+08，仅本日10-17/窗口10-16；复用本日有效必要Source/PRE，不复读全附件或其他日期、不重新发现。本人实际顺读下列完整新增、完整直接前后论证及新来源注，逐项回对S38–44的限定采用边界；不是只搜marker判通过。

| 家族 | 实际正文 / 本人核读范围 / 新注 | 实际通过的命题与衔接 |
| --- | --- | --- |
| 21815 Exact Makespan | Ch38新89；完整67–108；注426 | bubble同构小例后、GPipe反向前，Στ fill/maxτ steady只限纯forward固定服务无限buffer；无限并行delay才加fill，NCCL另stream不充要。真实bandwidth/backpressure/反向需实测，gateway log非PP trace；没有采overlap插值或普遍computefirst。 |
| 22035 ETH | Ch38新276；完整246–298；注427 | StageBalance/HAPMoE后增加不同完整replica的localbatch旋钮，按真实参数坐标重组梯度；样本权重/GBS/accumulation另验。三阶段heuristic、normalization/overshoot未闭、trainloss非exactSGD/heldout与全profile/search/recompute费均近文，接不平衡stage例仍自然。 |
| 21162 BCL | Ch36新710；完整681–728；注1926 | nested SP/pool后明确ranklocal KB→K个fixedB packs，保记录但改optimizer共批人口，与前文冻结stepmultiset分清；单record/平均/跨rank总量下界、CV非可行性、same-reader K1/32与跨campaignloader、未验heldout/restart及host/恢复费用完整。 |
| 20981 Cyclotron | Ch49新2313；完整2303–2336；注2520 | distributedtiling总论后/逻辑物理资源坐标前，iteration-space通信递推与space/time mapping、stale旧register/live依赖及匹配send/receive分责；liveDAG/readbeforeclobber等须验证，行为模拟非数值正确、transport混杂/部分更慢与全费保留，不授通用安全或LLM端到端收益。 |
| 21500 Remote KV Tier | Ch54新292/294；完整284–321；注799 | 层级开头后分别解释有限B准确阈值与健康progress rank的连续前缀；B>sR及n>RT0/(1−sR/B)、n>RT0只必要、最快median仍慢重算、H2b人口变化均明确。metadata/同序collectives不授crash/permanentstall或fingerprint认证；后接flash寿命分支没有把慢tier等同容量免费。 |
| 22172 EdgeFlow | Ch55新128；完整112–142；注570 | selective transfer开头先引ACT重构/directKV混合，再接proactive/selective旧分支；startup/drain两成本式不一致、未认证tail/无损续写与approx不作物理保证。模型/adapter/dtype/position及destinationcompletion另验、activation留存/重构全费和全KV/已验重算退路完整。 |
| 21640 ReFlow | Ch33新1713；完整1697–1742；注2820 | priorityreplay之后/AgentRL身份之前，batch reuse fraction与loss influence分旋钮，含replay processedtokens不冒fresh；完整replica/shard角色切换与CPU/初始化/optimizer复制/cooldown成本、理想fresh无偏/误差不相关及短trainingreward非heldout保证都落实。并未替代后接trajectory/environment admission。 |

已实际核六owner的Review notes位置；本批八机制段全在各自唯一`## Review notes`之前，七新注都位于章末notes内，无新机制插到notes之后。相邻旧分支、现有Source markers与后续章节交接保持；没有必须修正文义的问题，不为制造diff重写。六文件限定小写gitpath `git diff --check`无诊断，链接均为上述精确v1；机械检查仅辅助，不能代替本次实际语义读回。本人本层只写ORG_B，未改任何Books/notes、README、LS或index，未stage/commit/push。root可仅行政同步这七注为本既成POST通过；不授整日DAY/FINAL、实现复现或全来源无遗漏。Meta22230沿S45具体NC，无新增Books可验，不计入本七family。
