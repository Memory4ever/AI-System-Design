# Jan28 来源遗漏补查 — 进行中

只补充 Jan27 北京时间完整自然日；原窗口、64候选及连续 §4 正文保留，完整基线见 supplement-original-20261008.md。只本日作者 supp_jan28；root 与 jan28_review 独立复核，Books 写入需 root 锁。旧 STOP 的“完成”仅属上一轮，不能替代本轮。

## 实际进度

- 每日14入口已发请求；原始响应见 supplement-native-*、supplement-theme-*。Hunyuan Research 脚本壳，本轮隐藏浏览器首查30秒超时/重置；不能授零命中。OpenAI/Anthropic 403，Meta/Qwen壳、MiMo当前无日期首页、DeepMind当前分页不覆盖历史，必要历史目录仍保留恢复限制。
- Seed API 已确诊 sub_article_list/next_page_token/has_more/total；paper首20从Jan20跨Jan29，只查看窗口相关段，不追全年82库存。Jan27官方题摘19834 Visual Generation、19895 Keel；type2首项Feb12已越窗，止于该日期，不把后续博客变队列。
- 四主线 API 成功；submittedDate Jan26–27仅发现入口，按官方公告/最终ID/已deposit上界决定公开归属。model首150已跨Jan26截止，后页无需扩为Jan28队列；其他返回量与有界停止还须落表。旧377 registration列表只相关标题补检，不逐项筛整类库存。
- 新增68个相关 exact-v1 完整题摘实际已读（supplement-abs-*）；这不是68候选或68证据完成。80身份/日期定点包见 supplement-date-identities-20261008.json。
- root实际独立首批准入：18175、18401、18510、18486、18777、18779、18795；四官方 Kimi K2.5、M2-her、Seed Visual Generation、Keel。peer实际其余46完整题摘及决定准入的有限core已独校，18418 exact-v1 HTML完整AB恢复并实际读完；冻结新增60家族（56 arXiv +4 native），原64不动，共124。68新相关AB中10项贡献关闭、18415 NAACL2025同稿去重、18778 SOAR已有效旧公开去重，不因审阅/Books成本缩池。

## 已实际必要 Source Review（Books判断尚待）

18175v1：§2 fixed Markov π0/fixed P/binary terminal/nonterminal success>0，§3.1两臂0.495/0.505只微弱改进，§4.1–4.5/A.3/A.6 exact π+=π0Q/V、success occupancy加权χ² trust radius=Σd0+I、relative state advantage=χ²=I，true success弱改进。§6.1–6.3/A.9 proxy threshold相关性可为反向；§8 finite data/function approximation/large优化非主定理，无forced exploration。§5 M=sup d0+/dπ+ 与 A.8证明实际 M=sup dπ+/d0+ 方向不一致，隔离一般stochastic finite-fit bound；不削掉有效exact主定理，不采用训练部署保证。

18401v1：§2.1–2.4/3.1–3.4 Mamba累计key→固定stride anchors→top2 contiguous spans→selected-span软门，未选span本步零梯度；candidate span family覆盖是structural non-exclusion，不是每query都读全部token。全KV保留。N=2理想O(L^1.5)，N>2/log搜索future。§4.1/4.2/4.4/4.5/5：Nemotron30B-A3B、B200180GB、batch1、32Kchunk、20decode steps；10M只efficiency feasibility，4K→64K课程训练，NIAH仅至256K且冗余减少不消除失败。§4.5 factor 0.2/2.0内部描述不一致，未采用其精确参数/最高准确率。精度未披露，其他负载/SLO不外推。

18510v1：§3–4.4与Appendix C.1已读，经验(s,a,G)的LLM步奖励→局部kNN V/Q→未见action概率λ乐观α/|N|或0→Ahat→z+βAhat。KL惩罚闭式解仅对给定Ahat，非真实最优保证。C要求值Lipschitz、噪声条件无偏/有限variance、N/k无限增长k/N→0、每action count→∞、邻域policy drift→0；实际固定k及LLM评价不自动满足。§5.1–5.7：Gemini2.5flash training-free、WebArena5次逐任务交互与Jericho3游戏50轮；Table8同memory logitvs prompt Admin52.31vs49.46/Reddit57.64vs53.02，窄归因。跨task disjoint memory另测；Table9 API价格vsH200训练费不是统一端到端成本/算力证据，不授34倍生产降本。

18486v1：§3–6/Limitations实际读，U.S.Black/White×binarygender，501基础场景扩增；3models(LLaMA3.1-8B/OLMo2-7B/GPT5.2)，开源3seed，GPT单seed。name/dialect/history/explicit四cue，同cue跨name-list一致≠跨cue可交换；Figure3方向可逆，paired固定场景只支持cue-conditioned response变化。无答案GT，不评价正确性/真实伤害；race inference是行为probe非内部因果，readability与promptfixed-effects回归只部分混杂说明。二元/数字输出、API、国家/任务、race×gender限制，不外推人口级bias定律。

18777v1：Method Eq1–3/Experimental Setup/Analysis/Production/Limitations路线已读。query层P@K与query-doc judge层不同，先在query的topK合成估计，再用同分布gold residual纠偏λ μunlabel+mean(gold−λpredgold)。Eq3用document Bernoulli乘积，但线性P@K期望无需独立；非线性ranking不能直接套。ESCI美国只Exact/Irrelevant，去掉Substitute/Complement及不足K；50重复gold样本n30/100,N60K，production100gold+8400unlabel Body queries。人为gold人口/同分布与query cluster单位是采用边界，不能宣称100对任意judge足够；标注集同时isotonic calibration是否交叉拟合未明确，CI适用需保守。商业A/B数字匿名baseline/未完整运行条件，不作为一般效果。

18779v1：§2–6/§7–8/Appendix C实际读。Qwen3-4B-Instruct2507，128rollout×32K筛nearzero难题；GRPO8×16K,temperature.8；short humanoracleprefix仅condition，1:1 guided+unguided，rollout只续写。§3 entropy/clip/passK/easy混合本样本不能破零信号，§5.2禁止重述/回溯干预guided更好而unguided更差，支持overlap/stitching假说非内部因果证明。§6 table2同oracle-prefix SFT+rejection baselines不如guided；LUFFY没稳定跑成明确未比较。无LLM形式保证/所有hardtask guarantee，prefix成本与硬件端到端未完整披露。

18795v1：已实际读§2–5、B1完整consistency proof、B2算法与realizable finite-Q/NPG/ρ=.5μ+.5π critic、D1–3；peer必要Source已独核。offpolicy correct trace prefix梯度mask，只采conditional on-policy continuation，3prefix:1no-prefix；正确/realizable μ存在只支持global optimum consistency，不是samegradient/每步或实践保证。理论输出mixture、prefix-state coverage与实际REINFORCE/fixed3cuts隔离。Llama先OpenThoughtsV3 distill/Qwen4B；1Khardmath基于Llama512zero，3cuts40–80%；D2 2ND采样+6NDupdate并计rejection只FLOPs估算，非wallclock。related/unrelated及long/crossfamily反侧，Llama→Qwen弱于逆向；keyword行为proxy不授内部因果，Fig10未明suffixinjection实现不采用。

## 已落实并独立POST（非DAY）

首7家族必要Source/日期/具体owner PRE与actualPOST均由jan28_review实际独核。18175→Ch29两段；18401→Ch22两段；18510→Ch77两段；18486与18777→Ch66各两段；18779与18795→Ch33各两段。均root先授窄锁、作者写、非作者完整局部邻接与自身note核验后释放。14段/5owner不是候选最终分母或整日完成。

有限准入澄清已经peer actual核：17676 gaze编码粒度、18157 strict-to-relaxed timed/entity/SQL、18345 draft过滤排名逆转/trace missing，18261 NEW-Fisher mask、18393 privileged字幕蒸馏、18771 typed自然语言控制/write-age均准入。17910中心理论争议反例见supplement-source-adaptive-kd-20261008.md，保留候选，不改判排除。17717缺报矩阵的×含not-applicable，18492已知TFV/MEV+skip没有新可靠性条件，窄关闭；18415 official ACL Apr30,2025相同核心同稿去重。当前carrier成功不表示全体已read。

第二批实际新增POST：17676→Ch23、18157→Ch76、18345→Ch69、18631→Ch78，各两段由peer实际完整邻接与自身note POST通过；18631已纠正为推理时“引入A*”导航↑而verification↓。18681 ART→Ch24两段由root实际Source/PRE/完整212–235与自身1820 POST通过，先平均clock→固化grid→归一增量到T。现新增12整合/24段/10owner，不授DAY。18089 latent expert-coordinate最小命题在Ch21 296–314 actual已有覆盖，由peer实际275–335独核；18692 training-only3Dteacher→projection→deployremove最小命题Ch26 95–109 actual已有覆盖；18467在线/离线API费用配置仅报告，均不forcedBooks。

native最终Books由root实际裁决：Keel仅Jan27官方AB高层norm/residual/depth-widthLR联合设计Ch17已有覆盖，不授Jan28公式或1000层稳定实验；Kimi PARL trained-orchestrator/frozenexecutors、boundedfanout/criticalpath预算Ch82已有覆盖，不采auxrecipe/4.5x通用保证。SeedVisual只有Jan27官方AB声明，没有该日必要method/eval，Version Fact/Mechanism Not Disclosed，仅报告。M2her官方selfplay/implicitfeedback/entropyrecipe仅报告，不把自玩errorrate或vendor causal-denoise未披露变真实性能因果。

旧暂停前停点：18261+18255 joint retention两段PRE与18129 InK两段PRE当时仅拟文。用户恢复后已重新取得窄锁、改后字面PRE、实际写入及独立POST；不沿用旧授权。其余有效Source/反侧保留，当前层级见下一步。18699/18702/18753 root actual中心争议保留，不采用Books；需要精确实验/理论恢复材料，不以Only掩争议。

## 下一步

用户已明确恢复。原冻结60安全终态保持；OCR2 Jan27原repo精确首稿、完整题摘与独立准入/必要Source/Ch23 PRE/实际POST均通过，新增61/合计125。新61 Books为35整合家族/48正文段/16实际去重owner，11具体已有覆盖、9仅报告、6中心争议；Source/PRE/POST有效范围复用，不授中心正面Evidence。14source stop/旧10日期有界恢复已独核；Google尾Jan12已返修、OCR2旧hold解除。新增61已融入README原六部分，125行且原64/连续§4保留；进行态V3通过，普通工作只最终独立DAY与完成态校验。

普通待办：最终六部分非作者DAY与完成态V3/引用/原内容保护检查。没有新的Source/Books普通待审；中心争议与旧10日期/历史目录按精确请求隔离，不授正面Evidence/Coverage。已完成有效层级不重审。

## 旧暂停停点 — 2026-10-08（用户已明确恢复，此节仅保留历史）

暂停时作者与独立复核者已中断、所有旧写锁撤销，本轮当时未获DAY；Ch29 retention与Ch33 InK当时仅拟文。恢复后已重读合同并按上述新授权完成这些POST。本节不再代表当前暂停或写入状态，仍未授整日完成。

root追加实际必要Source停点（不授Books/DAY）：

- **18751 TriTrust-PBRL v1**：完整题摘、§3.1–3.3、§4辨识条件/整体符号对称、§5.1/5.2.4/5.3已实际核。joint reward与正/零/负expert trust是可采用的受限分支；理论需有非零reward差的共享edge及两个连接图，不能用disjoint比较实验认证定理。整体符号仍不可辨，可靠多数仅受限模拟；PEBBLE/SAC、MLP、模拟expert与10seed，增加反馈也可恶化。单global trust未分context/query难度；Eq4与Algorithm1权重的K因子不一致，精确recipe隔离，不声称代码已核或tanh永远无饱和。最终具体Books判断尚待。
- **18753 HalluGuard v1**：完整题摘、§3.2–3.3/4.1、Appendix A.1–2/C.1/C.3/C.5已实际核。中心risk guarantee争议隔离：A.2额外Galerkin/coercive前提未包含在A1–3中，尾概率被当误差幅值、K与|L|切换未提供可核导出；synthetic注噪紧性图不是现实风险上界验证。受限ranking proxy与实验recipe可保留描述，但不能当事实置信度、校准风险或统一理论保证；K10生成、projection/clipping/SVD及beam10均需成本，<1ms仅postprocess，不授全链zero overhead。最终处置与Report争议边界尚待写回。
- **18730 / 18731 / 18734（旧定位停点，已恢复）**：暂停时root只定位原件，未审；恢复后作者与audit实际完成必要Source、各1段字面PRE/写入/POST，当前不再是Source待办。保留原界限，不把早期下载逆称为早期审阅。

## 六部分合并后的实际检查

本轮六部分合并后实际机器/保护检查（作者，不代DAY）：125唯一候选行/125同标题证据小标题，分布37整合/16已有覆盖/62仅报告/10争议；新增61的35整合48正文段/16路径owner、11覆盖/9Only/6中心争议。原64行/原窗口/连续原§4逐字保护通过。README本地引用365次/37 unique目标存在；进行态V3与当前工作文件scoped diff-check通过。cached旧已暂存基线仍有EOF空白警告，不stage不改index，不能声称cached clean。最终DAY尚待resume_20260128_audit。
