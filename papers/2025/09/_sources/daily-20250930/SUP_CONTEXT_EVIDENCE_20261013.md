# Context editing / memory tool：具名日期纠正与有限Source/Books包

## 1. 自然日门与准入

作者实际读回Dalton§8，接受其基于当前合同的日期纠正：旧小时窗无法精确归属的记录保留，但本轮Sep29完整自然日不要求公开时分秒。当前[官方原发布](https://claude.com/resources/articles/context-management)及本日SUP_CONTEXT_20261013.raw（539993bytes，SHA b48f51958bac2a1249623c9e1c2c73c66c8d7500b34c3c2aab85dfa8807e0e20）中article:published_time/BlogPosting datePublished均2025-09-29，页面也明确同日发布。该原公开日门有效，不补造BJT午夜或继续把没有TZ当外部hold。

具体贡献链：长Agent轨迹的工具结果反复占据本次可见窗口，持久经验又需要跨会话保存 → 该发布将stale tool calls/results的context editing与开发者后端的client-side文件memory CRUD分别提供 → attention residency、durable state与真实effect必须分责，不能把清窗口当遗忘/撤回，或把写文件当模型持续学习。窄P主owner AGENT-CONTEXT，跨持久边界引用AGENT-MEMORY而非新建owner或算两家族。

最小2+2+2=6提议：Design Delta2只取公开接口把transient editing与开发者持久后端分离的具体发布条件，不取成熟memory原则或更大窗口本身；System Reach2覆盖模型调用工作集、工具轨迹和跨会话后端，不借平台数量加分；Durability2取可重用的状态/authority/删除边界，不取版本名或性能宣传。潜力/日期及必要原core已由reader§8实际核；评分及最终Books仍需本包变化层实际接纳，不预签DAY。

## 2. 必要Source与反侧

作者已实际web完整读原核心（Current windows/long-running/performance/getting-started），再复用原本日context-management-text.json的有效core与Dalton§8当前原件/同后端段核。公开事实是接近token限制时移出stale tool calls/results并保conversation flow；memory tool能在开发者基础设施内create/read/update/delete文件、跨conversation持久，操作全client-side，开发者选择存储后端。不是全部源证据被删除、环境effect被回滚、外部文件天然可靠、记忆正确或权重学习。

原39%/29%来自internal agentic-search，84%来自100-turn websearch；N/harness、baseline matched budget、variance、长期错误/恢复与stale判定细节未披露，不采通用性能因果或稳定性保证。实际模型/任务与运行合同只按原文已披露角色，不补模型精度/hardware/SLO。公开beta/多平台支持只发布身份，未核docs/实现、运行代码或复现。压缩/文件写入带来的选择错误、原文回读、权限/存储治理与维护成本为工程边界，不冒称厂商已证明全部控制。

## 3. 具体owner已有覆盖 / No Change提议

本轮Books上下文已读ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、最新State；现有目标Ch75及邻接Ch76/77/78的实际论证已定点读，不只按主题名字判覆盖。

- Ch75 L14–60：本次调用visible working set与跨调用Memory分离、token budget只证明可接收非正确使用，tool observations为独立预算项。
- Ch75 L166–181：write/read/delete Context显式working state，runtime校验并保source link，hide不删除原artifact/Memory/audit，derived note不变真值；回读/租期/visibility与durable-delete分责，短任务保原文路径。实际正文已承载本次拟采用的editing发布边界。
- Ch77 L14–27及L70–91：storage/write/read/consolidation/forgetting/authorization持久责任，candidate需来源/同意/冲突/expiry/provenance门，model summary只是derived；client-side文件CRUD不是学习权威，开发者后端选择不免治理。
- Ch77 L510–534：compact working state与versioned full-fidelity archive/exact dereference分层，reference绑定namespace/version/授权/删除/恢复，过早archive遗漏与过晚overflow并列，不能由小context反推持久状态正确。Ch78保存真实tool effect，Ch76拥有检索/语料，不让此家族抢第二owner。

最低长期采用命题已有具体正文承载，建议“已有覆盖：AGENT-CONTEXT / Ch75（持久状态边界由Ch77交接）”，本次No Change；不把provider新接口字段或厂商例子复制成新章节/note，也不称现书稿已经实现Context editing或memory tool。请Dalton只核最小评分/必要Source限制和此最终No Change理由，保存实际接纳后才同步正式第八家族。不再获取原发布/后续文档，不等其他来源整包；无Books新写/锁，root49/132、83未验收不预增。

## 4. 实际§9–10读回与作者采取的5分裁决

作者实际完整读回Dalton§9–10：自然日日门有效、公开局部运行时接口窄准入，必要Source标准审阅与Ch75/77具体覆盖已实际比较。采取1+2+2=5，修正上文作者DD2/6分提议：未披露新学习算法/原子协议，这次只是局部生命周期接口，DD1符合实际新增命题；Reach2/Durability2不变。不因No Change、Review省费、未取原证或访问状态降分，必要已读core/反侧保留，未缩候选。

作者最终Books决定已有覆盖AGENT-CONTEXT/Ch75，持久边界由Ch77现文交接，No Change；已实际将第八正式家族/5分标准Source与具体owner并入README，旧六完整行与连续原§4未改。当前需reader实际核作者采取后的变化层/最终Books与整日报DAY，不能将本节或§9准备建议当已签DAY/FINAL。无需重fetch主体或重Books正文，当前49/132、83未验收不预增。
