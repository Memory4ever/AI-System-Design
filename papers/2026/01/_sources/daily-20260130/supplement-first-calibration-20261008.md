# 2026-01-30 首批增量准入校准（待非作者 root）

本轮只补遗漏；原稿63家族、日期、评分、原§4有效审阅均保留。本日原始基线见 supplement-original-20261008.md。新增按2026-01-29北京时间完整自然日，官方只给Jan29的日粒度足够，不再要求时区/小时。旧14源有效有限查询与明确缺段复用；本轮native-0～3为精确Jan29具名补线索，并不将全目录设审阅队列。

## 拟新增3家族（先准入，评分暂定校准）

1. [Qwen3-ASR / Qwen3-ForcedAligner 发布](https://github.com/QwenLM/Qwen3-ASR)：官方News直接2026.1.29。旧小时窗口DATE隔离解除，仅release事件，不借后来的arXiv提交日。完整核心见既有 V3_QWEN_ASR_CORE.txt，新补核 supplement-native-core-20261008.json，GitHub核心行210–248、Streaming/ForcedAligner节。原离线转写正确不保证流式前缀稳定和文本时间定位→该模型公开统一offline/streaming及独立NAR文本—语音aligner、当前streaming与timestamp接口分开→是否将可变前缀立即commit和是否另做forced alignment必须分开判断。暂2+1+2=5，必要审阅拟聚焦当前release能支持的接口边界而非未读论文机制/吞吐宣传。
2. [PaddleOCR-VL-1.5 发布](https://ernie.baidu.com/blog/zh/posts/paddleocr-vl-1.5/)：官方blog2026年1月29日，日粒度有效，旧时区/时刻请求解除，论文后公开不算此release首次公开。完整核心见旧 V3_PADDLEOCR_CORE.txt及新 supplement-native-core-20261008.json。干净平面文档分数不能覆盖倾斜/弯折定位→新增不规则polygon解析与Real5五类物理畸变评价接口→文档表示的geometry和评价slice需同时改变。暂2+2+2=6，重要修订精确读当前release受影响接口/评价；同家族不因论文增加计数。尚未将SOTA/94.5或速度归因于polygon机制。
3. [Inside OpenAI’s in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/)：官方January29。新遗漏具名材料，全文核心已读，保留于 supplement-first-native-primary-20261008.json，行95–137、148–173。schema/查询历史能定位表却缺pipeline实际过滤和粒度语义→从生产代码抽取表定义、daily归一化离线context、runtime stale-context补查及需用户确认的可编辑memory分层→预计算检索语义与live验证/用户纠错的权威和刷新边界须分开。暂2+2+2=6，准入只为原文的可复查工作流实例，不把成熟RAG+memory组合本身当突破；厂商未披露controlled ablation，因此效益归因待收窄。

两条贡献入口同标准；目前无Structural Candidate。通过后读取owner现有论点做Books处置，不预先制造写入。

## 分层关闭样本与原文

- OpenAI [Retiring GPT-4o and other legacy models](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)：官方Jan29节为ChatGPT产品退役、API明确无变化；没有本项目新的机制/兼容性约束变化，贡献前关闭。不是只因为产品发布排除全部release。原文在 supplement-native-0-20261008.json。
- OpenAI [Understanding Animals](https://forum.openai.com/en/public/events/irl-virtual-understanding-animals-ai-helps-scientists-interpret-language-across-species-s3dgmg67a2)：鲸类语言探索/AI for Science域外，标题及说明明确关闭；不读完整活动附件。原文同native-0。
- Anthropic [Claude on Vertex AI workshop](https://www.anthropic.com/webinars/claude-on-vertex-ai)：旧有效关闭复用，教学性memory/reasoning/tool组合没有新增机制或有效条件，不因熟悉Agent术语准入。完整说明V3_RAW_DAILY_FINITE_QUERIES.txt开头。
- 旧15 early arXiv：新补核abs题摘和当前纠错comment均已保存 supplement-ab-199xx-20261008.txt，但Submitted早且Created Jan29只能上界，仍缺具名Jan29first-public证明；这不是贡献前关闭，原准入与反侧保留，有限日期恢复后无新必要公告则终态隔离，不全文重读。19944非LLM原误排除保持撤销；19912/19904有效局部反侧复用。

准入及源审阅待root实际非作者复核，不将本文生成/下载视为已通过。
