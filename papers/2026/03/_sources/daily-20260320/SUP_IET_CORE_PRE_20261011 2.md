# IET17445：合作式文本归因与执行 trace 分责

resume_mar17，2026-10-11，仅03-20补03/19。批5完整题摘/日级夹证/2+2+2=6复用；本packet只准备必要Source/actualowner/PRE，不自授PASS、safe、DAY或Books写权。

## 1. 精确必要源与停止

[v1](https://arxiv.org/html/2603.17445v1)方法/关键评价实际L97–325、§4–7直接限制L324–340；当前明确scope变化触发只读[v5](https://arxiv.org/html/2603.17445v5)AB/§1–2 L87–212、关键§3–4/T1–2 L213–320、C/D必要数据/解码/检测/扰动定义L411–480及F非对抗变换反侧L487–499。未遍全部prompts/references/代码/全部版本差，不假称复现或读取全部图像数字。

v1 Eq6以L_j logits定义statistic与“只finaltext”有文义缺口；v5 Eq6已明确从观察token y_j及其context重算key/permutation取方向值。这是真实受影响修正，不能沿旧公式宣称原v1完整检测recipe。v1“full topology/selfdescribing execution”与v5 honest-but-instrumented、auditor registry（agent-key-tokenizer）/segment scope分层；不把current修正复制成03/19早稿已保证，也不另加家族评分。

## 2. 有限支持与直接反侧

合作agent在生成时对logits施agentkey/contextkey置换、小幅方向扰动再逆置换采样，改变生成分布；不是从未instrument的任意文本自然恢复身份。auditor必须有验证registry并使用一致tokenizer/context规则，窗口评分与competitive margin/CUSUM只估片段身份/边界。v5§2.1/2.4明确相邻片段a→b转移是linearized output诱导图，不是并发/隐藏communication graph，更没有timestamps、tool副作用或原happens-before证书。bitmask累计可表示observededges，但不采v1 μ进入编码的未闭合桥，也不授wholeexecution复原/加密签名或不可伪造。

v5 T1 TokenAcc .818–.867/IoU .814–.843及EdgeSim .912–.949不是完美归因；EdgeSim cosine也不是逐边exactness。signal-aware KGW/Unigram是更可比对照，纯文本LLM与已植入信号pipeline不具有相同信息预算。v1TopoAcc系agentunitlabel口径，不授原fullgraphaccuracy。v1 T2多个clean/boundary项退；v5 T2新评价clean仍退，例如All-at-Once agent54.33→54.16/step12.50→10.47；IDRemove只恢复约21.5–24.5 agentaccuracy，不证明因果责任恢复。currentboundary protocol保持turnorder/metadata skeleton、随机cut/refill，非完整metadata丢失/乱序通信。

current MAMA484样本、Llama3.1-8B、4/5/6agent与chain/star/tree、maxrounds3；Fourier kp1/κ.8/ngram2/window64/step16等已披露。WhoWhen184整体但localpipeline主要126algorithm-generated；100Arithmetic seed42与100GSM8K、3agent2rounds质量对照的CI含零不是等价/所有任务无损证书。F Oracle-IET用goldboundaries的chain4非全部自动分段路径：中文回译与10%无watermark替换会退。不采adversarial forgery/suppression安全，作者明确scope外；PIIplaceholder反侧不是任意semanticrewrite。生成/keyregistry维护/窗口检测/全部候选agent评分/审校与失败归因复跑计全费，hardware/precision/concurrency/SLO及端到端费用Not Disclosed。

一次精确强命题重开条件：需要匹配registry/tokenizer的独立端到端生成—分段trace、保留原通信/副作用happens-before的对照及完整扰动/预算人口；在此之前不采用执行复原、因果责任、抗伪造/隐私或无损保证。受限文本身份接口不等待这些强外推。

## 3. 实际唯一owner差额

sole `PLATFORM-TRACE` / [Ch69](../../../../../books/part-06-ai-infrastructure/69-trace.md)，实际完整1–130：66–70统一schema不保证provider字段穿栈；72运行时hook；76–100显式context/spanlinks与clock/happensbefore；114–116repo标记恢复仅身份线索。它们未承载“生成分布内植入统计身份，finaltext+registry后验恢复segment”的具体替代采集路径。不是因为一般provenance主题就新增。实际Ch68/70入口与Ch82 995–1025failure/replay边界已读：Log事件保存与Cost归因不接管这个trace证据对象，Multi-Agent策略不另复制检测机制。

拟Ch69原72运行时hook完整段之后、74资源normalized-profile前两段，把metadata exposure→运行时观察→artifact内合作式身份恢复→资源测量沿同一证据链推进。旧显式span/context仍主路径，结构不变。

## 4. 两段 literal PRE 与静态注

当运行环境和显式metadata都未随文本保存时，采集路径还可前移到合作模型的生成过程：每个agent以自己的key和token上下文派生置换/扰动，轻量改变logits后采样；离线auditor持有agent-key-tokenizer验证registry，再对最终token序列作窗口评分和变点检测，估计片段来源。这不是任意文本的无条件身份识别，更不是不可伪造签名；key、tokenizer与生成分支未绑定时应保留Unknown，不能由风格相似度补造执行事实。它恢复的是线性文本片段及其相邻转移，隐藏通信、并发happens-before、工具副作用和原wall-clock仍须显式trace承担。<!-- source-family:SF-2026-ARXIV-2603-17445 -->

[合作式文本归因的受限证据](https://arxiv.org/html/2603.17445v5)仍有身份/边界误差，重写或替换生成会侵蚀信号；恢复speaker不等识别失败的因果责任，保留turn骨架的边界扰动也不认证完全metadata丢失。原v1检测式与只观察文本的接口未闭合，当前稿收窄到registry下的token统计与诱导转移图，不能倒写为完整执行拓扑复原。生成质量、片段归因、转移结构与下游失败诊断须各验收，生成扰动、key管理、全候选评分和复跑均计费；抗伪造、任意语义改写和生产SLO未获证明。高风险执行、无法合作instrument或身份不稳定时，保留原显式span/日志与人工审计，不让文本归因替代权限或发布gate。<!-- source-family:SF-2026-ARXIV-2603-17445 -->

静态注：

- `SF-2026-ARXIV-2603-17445` — [IET v1](https://arxiv.org/html/2603.17445v1)必要方法/评价/直接限制；[current v5](https://arxiv.org/html/2603.17445v5)仅受影响registry/观察token/segment与诱导转移、关键评价和非对抗反侧。采用合作式文本来源恢复接口，不采完整execution/通信拓扑、因果责任、抗伪造、无损或生产SLO；保人口/quality回归与全费，未核代码/复现。

## 5. 非准备者裁

待reader必要Source/actualowner/两PRE有限裁，root授权前不写Books；不按忙碌改center/NC/EX。

## 6. 授权后的 writer 实际落实

reader必要Source/actualowner/两literal PRE与静态注有限PASS见本日独核§21；root随后明确授author唯一Ch69窄锁。原两PRE逐字写新74/76与本人静态433，writer实际顺读64–104完整metadata exposure→runtime hook→新合作式文本归因→资源profile→links/clock链，以及427–433静态本人及PASTA/解释器邻注；限定实际diff仅6行增量/check0。未改其他family或验收身份注；registry/segment非隐通信、并发因果/责任/签名与强v1桥不采均近文。交reader一次nonwriter actual POST，不由writer授POST/safe/DAY。
