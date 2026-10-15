# 2026-10-14 Daily：七个全球官方来源检查

窗口：**2026-10-13 ～ 2026-10-13，北京时间完整自然日**。检查者：`live_oct14_global`；实际检查启动2026-10-14 18:48 BJT。这里只维护来源、题摘准入与必要原证，不是日报/Books/独立验收完成证明。唯一写入owner为本文件；不改Books、Report、State或索引，不stage/commit/push。

启动已完整重读AGENTS、Prompt、研究/Report合同、来源使用说明和每日组、ROADMAP；最新LEARNING_STATE明确两历史cursor暂停，不启动历史补查或Weekly。昨天global-sources仅作入口路由，今天所有列出的来源实际重开；不继承其覆盖。using-agent-skills只用于确认范围纪律，未新增通用代码/产品任务。

## 1. 实际来源与停止

| 来源 | 实际检查入口、范围与停止 | 状态/结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research index](https://openai.com/research/index/)当前9 dated cards；Oct07×2→Oct06×2→Sep29×2→Sep23→Sep22→Sep10，窗前停止，不Load more | 已检查可见当前日期前缀；未确认当窗新事件 | 不授隐藏删除/全历史保证 |
| SRC-ANTHROPIC | [Research Publications](https://www.anthropic.com/research)当前10项：Oct12×2→Oct09→Oct08×2→Oct01等，窗前停止不See more | 已检查当前日期入口；未确认当窗新事件 | Oct12两原件不搬入本窗 |
| SRC-GOOGLE-AI | [DeepMind News](https://deepmind.google/blog/)当前月级Oct五卡：原文核实Argon发布/安全/Robotics=Oct13，新加坡诈骗检测=Oct14窗后，EmbeddingGemma2=Oct06窗前。停止月边界；[Publications](https://deepmind.google/research/publications/)页1日期前缀Sep16→Sep01→Aug26，窗前停。[Research Blog](https://research.google/blog/)最新Oct07；[Pubs](https://research.google/pubs/)页1仅年份/venue，2027/2026非首公开日 | 已检查日期入口；安全同family新事件及ADK具体反证准入已校准，产品/Robotics具体EX；Pubs本窗日级切片与long-decode正文受阻隔离 | Pubs缺官方本窗相关主题首公开日期段，不扩全年目录逐项队列；接受日期目录或具体原件定点重开 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)web0行；替代[Blog](https://ai.meta.com/blog/)/[Publication results](https://ai.meta.com/results/?content_types%5B0%5D=publication)两入口Node fetch均失败；curl各一次25s timeout/0B | 受阻，已穷尽本轮有限当前入口 | 缺当窗相关主题日期列表，0行/0B不作零命中；接受官方日期目录或具体原件定点重开 |
| SRC-QWEN | [Research](https://qwen.ai/research)web0行，实际HTTP200/92469字符仅app壳，无日期条目；IAB一次`ERR_NETWORK_IO_SUSPENDED`止。[组织](https://github.com/QwenLM)首10/59，qwen-code/docs=Oct14、Image2.1=Oct13、其余≤Oct11。有限releases首5与Image commits首5实际200已夹窗；本窗nightly53条changelog完整实读，具体最低门见§4 | Research目录及必要GitHub core受阻隔离；有限官方载体已实际检查，不授完整当窗零研究 | 不以updated作研究日期；具体需要core/merge日期的身份保留，不全组织扫描 |
| SRC-DEEPSEEK | [研究与动态](https://www.deepseek.com/news/)News5最新Sep10/Apr24，Research10最新Jun24/Feb25/Jan28；前缀窗前停，不查看全部 | 已检查当前日期入口；未确认当窗新事件 | 不授隐藏条目/全历史保证 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26项完整可见列表最新2025-11-07；[组织](https://github.com/MoonshotAI)首10/42仅kimi-code updatedOct14，其余≤Oct12。releases首5最新Sep24；commits首20实际200，前4Oct14→6条Oct13→Oct12，已夹窗；六Oct13对应PR完整core/behavior实读 | 已检查这些有限入口；两拟候选、四贡献前EX（§5） | 提交/merge与首次研究公开分开，不扩旧仓库或声称整个组织无其他研究 |

## 2. 首批拟准入校准

### G1. [Developing Gemini 4 Argon responsibly and safely](https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/)

官方原文Oct13，已读全部核心Misuse/Misalignment/Prompt-injection说明，无当前撤回/纠错标记。最初拟 **2+3+3=8** 经去重校准撤销，保留原家族评分不重复计分。Root提示并实读Ch72现1028～1034：`SF-2026-GOOGLE-GEMINI4-ARGON`已有CoT/action监测与训练反馈lineage两段，原链接是[早期Argon发布](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)，与本日`introducing-gemini-4-argon`全球发布及`gemini-4-model-safety-security`路径不同。独核/root确认同family当窗重要安全新事件；只审本次thought-penalty公开反侧，不重复原发布与反馈分工论点。

本次限定命题：可监控CoT不等价于诚实观测，惩罚思考中的shortcut可能降低可见风险而非必然减少行为。作者口径公开讨论shortcut下降61%、silent shortcut份额11.2%→36.4%；只保存公开反侧，不当多seed普遍因果定律。博客另有activation probe/input/实时action+scratchpad监控，不以旧原则加分。[正式Safety and Security Report](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf)web两次Internal Error；HTTP HEAD200/17,293,501B（last-modified Oct14，只证明当前对象更新时间不是实验公开日），GET返回0B/timeout，内存解析因空文件失败。没有读到PDF；样本/model/hardware/budget、penalty精确定义与可比对照未披露，不能采用安全率、强因果、完全反馈隔离或零漏报。Root/独核允许依据实际已读博客完成上述窄声明的深入限定，不把PDF全报告作为该窄命题强制依赖；Ch72现反馈/独立outcome论点可已有覆盖，具体Books由root核。将来要采用实验归因/安全效力时只重开相关PDF人口/协议/限制，不继续重复抓取。

### Google相关具体最低门，不从成熟原理倒推高分

- [Argon全球发布](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)Oct13全部核心已读：新模型/价格/排行榜/行业demo本身贡献前EX。Gemma4 E2B、A100、vLLM 2.85x/token parity的原[PR查询](https://github.com/vllm-project/vllm/pulls?q=is%3Apr+author%3Alucianommartins+%28created%3A%3E2026-10-05+created%3A%3C2026-10-10%29)URL实际从主文href恢复，明确只定位Oct05～10早期PR；本窗厂商合并叙述不作为当窗新实现。Workload/precision/batch/SLO未披露，不据2.85x认定新可比质量/资源边界。AI for Science段范围前排除，不绕Data/Agent纳入。1M unified input-output与continuation是实际潜在接口线索，不与旧发布合并成已证机制；必要[long-decode官方说明](https://aistudio.google.com/docs/long-decode)本日实际web仅1行Google AI Studio壳，无protocol/core，故单列外部保留项不评分、不采用；接受官方公开协议/错误与恢复语义后只重开该接口。
- [Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/)Oct13完整core全部读完，贡献前EX：校准坐标/动作原语/视觉反馈、contact-only sim约束、domain randomization＋VLA微调、dry-run/hardware反馈组成已知技术流程；没有定位新的学习/执行机制或对旧设计的相反成立条件。单桌面77任务与4500+sim episodes、作者real success56→75%/35→24s、SO101三个iteration，不改变其demo证据范围，不从局部效果倒推新通用边界。原文未给对照归因/跨任务失败分布，未观看或复现视频；排除理由是没有具体长期增量而非机器人范围外、仅因sample少或未开源。
- [ADK overnight engineering](https://developers.googleblog.com/optimizing-a-200000-line-python-codebase-overnight-with-gemini-4-argon/)由当窗发布定点触发，官方Oct13；完整core/评价/limitations已读。初筛EX经root/独核纠正为 **2+2+2=6** 标准候选：现有“全测试通过/局部加速”判断→真实open-source pass但25内部mock失败，以及import加速未改变first-request的局部反证→release验收须重新检查population/语义contract与真实端到端成本。不是把成熟holdout原则自身评分。作者instant model/tools隔离framework成本；6～12次median、byte-identical模型请求，import快21%但new-process first request3.07→3.09s未改善；只InMemorySessionService，其他DB deserialize不变。六proposal二落地四拒绝中弱引用地址复用可stale、private tracer属性、synthetic-only收益均保原反侧，不归因于模型一般可靠性或替代完整review。Ch66现Harness/Environment/held-out release具体论点可已有覆盖，需root核实承载位置；无需为制造增量改书。

## 3. 限制与下一步

有限Source任务结束：G1同family窄事件、ADK及Moonshot两候选准入已校准；root继续具体证据/Books判断。PDF、long-decode壳、Qwen/Meta/Google Pubs具体入口缺段隔离，不得作为零命中、Coverage通过或互联网无遗漏。Google产品/Robotics两EX、Moonshot四EX保必要反侧供独核。本轮不再抓取上述失败入口，不扩大机构全年目录、每周源或历史cursor。

## 4. Qwen：载体、窗前去重与原证缺口

[releases首5](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=5)顺序非严格时间排序：preview0 published Oct13T20:01Z、nightly1013 Oct13T21:56Z，均BJT Oct14窗后；唯一本窗载体[nightly1012](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.1-nightly.20261012.18f80f5666)published Oct12T22:25:02Z＝BJT Oct13；v0.25.1与nightly1011分别BJT Oct11/12窗前。载体prerelease=true、draft=false，不能把53条历史changelog都当当窗新增家族。

昨天记录定点去重只对同事件身份使用：13330/13892/13872/13460/13788/13877/13673/13674/13909已保存窗前核心；新API实际核[13276](https://github.com/QwenLM/qwen-code/pull/13276)merged Oct12T00:41Z、[13243](https://github.com/QwenLM/qwen-code/pull/13243)merged Oct12T00:50Z，亦为BJT Oct12，不因新nightly把它们搬入本窗。其余纯UI测试、CI runner、BOM/图标/常规文档标题范围明确，不借managed-agent名称建立准入。

具名必要最低门：PR [13923](https://github.com/QwenLM/qwen-code/pull/13923)shutdown、[13915](https://github.com/QwenLM/qwen-code/pull/13915)middleware recovery、[13894](https://github.com/QwenLM/qwen-code/pull/13894)placement/retention ordering、[13889](https://github.com/QwenLM/qwen-code/pull/13889)Monitor/background gates、[13917](https://github.com/QwenLM/qwen-code/pull/13917)never-started settlement、[13940](https://github.com/QwenLM/qwen-code/pull/13940)Java envelope mirror、[13959](https://github.com/QwenLM/qwen-code/pull/13959)wake drain/gate guard、[13950](https://github.com/QwenLM/qwen-code/pull/13950)tool permission checks、[13654](https://github.com/QwenLM/qwen-code/pull/13654)async publication verification、[13777](https://github.com/QwenLM/qwen-code/pull/13777)parked-turn recovery、[13899](https://github.com/QwenLM/qwen-code/pull/13899)CSI process isolation：本日官方API均403，没有取回core或merge日期；一次原网页批读取fatal connection failed，没有正文。仅release题名含机制/安全信号，不能据title判准入或排除，不评分、不确认为本窗候选；需要这些身份完整core/当前安全修订及官方merge日期，恢复后先准入日期/贡献，再决定必要实现，不遍历全PR史。403不冒已知原因或零事件，不绕权限/新凭据重试。Release中其他具体核心但未展开的13335 config/API hygiene与13077 spawn-error也保持未审，不授整个载体逐项关闭。

[Image2.1 commits首5](https://api.github.com/repos/QwenLM/Qwen-Image-2.1/commits?per_page=5)夹窗：Apple Silicon docs Oct14窗后，唯一[OpenVINO Day-0 docs](https://github.com/QwenLM/Qwen-Image-2.1/commit/bb8e2172e08c6720652a4a23ad1c406e5b6ed1ee)committer Oct13T04:25Z为当窗，仅文档支持公告的题名不能建立新的模型机制/可比资源边界；不宣称读取了其diff，不从支持列表升格为候选。其余Oct12/09窗前。

## 5. Moonshot：六个本窗合并事件core

日期以下均取[官方PR API](https://api.github.com/repos/MoonshotAI/kimi-code/pulls/4179)created/merged字段，不将旧PR创建搬入本窗首次论文；均无所读原件撤回/删除标记。

### M1候选：[fork request prefix parity in prompt cache probe](https://github.com/MoonshotAI/kimi-code/pull/4179)

created Oct12T03:56:47Z，merged Oct13T03:15:42Z（本窗merge事件）。拟 **2+2+2=6**：原fork缓存命中率把不可命中新尾部计入分母，且混淆客户端前缀分叉与server miss；新增同模型父请求基线/工具system identity及消息复制时的prefix revision，改变可比较样本与因果诊断选择。拟`AGENT-CONTEXT`或`PLATFORM-MONITORING`唯一owner由root核；不是遥测字段越多越有贡献。

完整core与反侧：快照在同步复制消息处取revision，异步media/clearContext不能把旧消息绑定新revision；compaction读时revision校验、模型alias跨cache namespace不比，unknown parent usage不报0分母。undo只截尾仍严格前缀不机械丢baseline。tools/system相等不证明完整序列化相等，thinking keep/effort盲区保留；gap从流式结束起不是cache写入年龄，长输出系统性低估。作者范围测试，不是远端缓存复现或端到端性能证明。live_oct14_review已实际核必要patch/测试与精确merge `fed19d24f00203205b1fa4d23e60afce0609cc00`，不采用true=server必miss。root已写入Ch67两窄段；独核实际正文与邻接POST通过，源注补精确merge后仍待最终日报验收。

### M2候选：[remote control device management](https://github.com/MoonshotAI/kimi-code/pull/4169)

created Oct10T09:18:09Z，merged Oct13T09:40:24Z（本窗新merge/接口事件）。**2+2+2=6**：注销并非删credential即结束，仍存relay cookie/in-flight handshake/另一进程machine lock；新增清session、停tunnel、start gate与credential discard的跨边界协调。受控tunnel中的respond-first分支实际只有定时延后，不存在已验证flush与撤权完成收据，这个反侧改变注销完成的验收。安全约束变化已深入受影响实现，唯一`PLATFORM-SECURITY`的撤权/epoch gate/旧请求lease实际论证已承载，因此具体已有覆盖，不另写Books。

完整core：cloud session仅Node内存按generation/origin/OAuth slot隔离，clear abort；401一次exchange/retry、15s timeout；本机device deactivate识别starting/外国process holder，等待lock release。toggle串行，starting可cancel。Kimi logout串行、credential前后clear；非Kimi不动remote。后续必要实现独核纠正早期概括：只有非hosted路径先disable/gate，再改credential；hosted路径调用reply.send后固定250ms，再异步disable、最多三次失败只log。没有真实flush receipt，不保证所有分支cleanup失败均先于credential变更，也不是原子撤权。作者38/25/83定向测试等只支持其声称测试范围，不是我们的多进程公网E2E。具体原证与最终Books比较见本日独核R3及正式报告，不沿用早期广义顺序保证。

### 四项贡献前EX，不评分

- [4188 qualified plugin skill names](https://github.com/MoonshotAI/kimi-code/pull/4188)，created/merged Oct13T04:19/11:41Z：完整core/behavior是v1成熟namespace parity移植，plugin限定名恢复裸名可达/幂等注册，命令优先显式skill escape保留；未新增能力授权模型或相反实验条件，不因compatibility词准入。
- [4190 select_tools failure reasons](https://github.com/MoonshotAI/kimi-code/pull/4190)，created/merged Oct13T07:10/11:39Z：完整core把policy-denied/stale/unknown分桶，3次全失败提醒、per-name计数随policy/registry重置、loadable-only suggestions；恢复既有工具发现与权限分工，未验证新的reliability边界，不把fail提示当强制禁止retry。
- [4192 device deletion](https://github.com/MoonshotAI/kimi-code/pull/4192)，created/merged Oct13T09:53/11:58Z：完整core是沿4169既有exchange/timeout/clear路径增加thin proxy soft-delete，离线设备从列表移除；无新credential/执行授权设计，不拆M2再加家族。
- [4165 skill prompts and steering](https://github.com/MoonshotAI/kimi-code/pull/4165)，created Oct10T07:45Z、merged Oct13T04:17Z：完整core为既有Enter/Ctrl-S/skill路径统一，不新增SDK等待或恢复协议。明确显示输入≠引擎持久化/执行成功；Hook拒绝会暴露既有waiting/running卡住，视频lease误关联未修，作者撤回额外Hook补丁。保存该负面限制，不声称全安全；未建立超越已有提交/显示分离原则的新机制或独立反证，供root复核安全/兼容性信号，不以feat或UI标签泛排。

## 6. 交接与限定检查

实际来源检查18:48～19:15 BJT（全稿读回UTC11:15:49），随后只同步已收到的独核/root校准裁定；七项本任务来源均有本轮有限入口/停止证据，只有有序可见段可以记已检查，受阻切片不继承昨天成功。两Moonshot候选、ADK候选及同Argon家族重要安全事件（不重复计旧分数）、上述身份明确外部保留项交root/reader，必要实现证据、Books与Report由root继续。没有声称整个Daily完成。

本文件实际保存后执行限定`git diff --check`及untracked文件`git diff --no-index --check /dev/null <本文件>`；只检查本文件，既有与并发其他修改未动。不stage/commit/push。

## 7. root定点恢复与最终处置（2026-10-14）

独核发现§4把13335/13077尚未读core混入外部受阻，root纠正这一普通层。实际访问同一官方API，没有更换凭据或绕过权限：两条返回200，完整英文核心可得。因本轮有明确访问恢复信号，再对原11具名hold一次顺序请求，只在落窗时读完整core；没有重扫release/组织或PR史。

| PR | 官方merged_at（UTC） | 北京时间日期 | 本窗处置 |
| --- | --- | --- | --- |
| 13923 | 2026-10-12T03:31:17Z | 2026-10-12 | 窗前，不深审/搬日 |
| 13915 | 2026-10-12T03:49:02Z | 2026-10-12 | 窗前 |
| 13894 | 2026-10-12T04:19:59Z | 2026-10-12 | 窗前 |
| 13889 | 2026-10-12T06:30:06Z | 2026-10-12 | 窗前 |
| 13917 | 2026-10-12T06:38:13Z | 2026-10-12 | 窗前 |
| 13940 | 2026-10-12T08:35:15Z | 2026-10-12 | 窗前 |
| 13959 | 2026-10-12T09:56:08Z | 2026-10-12 | 窗前 |
| 13950 | 2026-10-12T11:16:54Z | 2026-10-12 | 窗前 |
| 13654 | 2026-10-12T13:02:10Z | 2026-10-12 | 窗前 |
| 13777 | 2026-10-12T13:06:11Z | 2026-10-12 | 窗前 |
| 13899 | 2026-10-12T13:06:11Z | 2026-10-12 | 窗前 |
| 13335 | 2026-10-12T07:17:05Z | 2026-10-12 | 窗前；完整core实际读到单位/lease、配置与API差額，但不转成本窗新事件 |
| 13077 | 2026-10-12T16:00:40Z | 2026-10-13 | 具体EX，见下 |

本表身份对应 `https://api.github.com/repos/QwenLM/qwen-code/pulls/<PR>` 的实际merged_at；新请求顺序11项全部200、已到已列集合末项13899，没有本轮后台session留存。原403/网页失败仍是发生过的轨迹，**不再是这13项当前缺口**；不能继承过时受阻标签。载体正式最终口径为53条，先前消息54是中间口误，不加到本日论文数。

[13077](https://github.com/QwenLM/qwen-code/pull/13077)完整core：`spawnSync`启动失败时error但无status/signal，旧launcher静默exit1，新在两处输出command/code/errno/syscall并exit126。PR body仍为旧17条unit/Linux范围；独核在当前原网页轻检发现Oct02 maintainer纠正：head `25bbcd77` 20/20、base失败5/20，并有macOS真实POSIX restart EACCES前后对照，Windows真实路径/Bun仍未覆盖。旧body不代表当前全部测试证据，这一纠正已纳入判断，但不是本项目实际运行。只恢复已有启动失败的诊断/exit合同，没有新的模型、执行恢复、状态控制机制或可比系统边界，贡献前具体关闭，不因fix标签泛排，也不把unit green当运行保证。精确merge `6d79d511fe4755702c9d6136bdb9cff3cceb184a`，不追完整版本史。

最终既有六家族Source层复用：G1/ADK/M2具体已有覆盖；A1/A2/M1由root落实Ch30/83/67窄正文及末注，非writer实际POST通过。G1同家族重要安全披露不重复评分；M2的hosted定时teardown反侧以§5修正文字与独核R3为准。普通源恢复层0，剩正式README独立DAY/完成态FINAL；Google Pubs/Meta/Qwen动态Research、MiMo无日Blog、long-decode与完整Safety实验仍按各自原证范围隔离。
