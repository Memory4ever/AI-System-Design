# 2026-10-10 机构来源检查

窗口：2026-10-09 北京时间完整自然日。执行：2026-10-10；检查者 root。只查每日机构来源的当窗切片，不扫描每周组；首页年份、仓库 updated 和 API submitted 不当作公开日期。以下有限停止点不证明互联网或机构全目录无遗漏。

| Source ID | 实际入口、读取范围与停止位置 | 窗内结果与边界 |
| --- | --- | --- |
| SRC-OPENAI | [Research index](https://openai.com/research/index/) 首屏十张日期卡；最新10-07、随后10-06、09-29，日期降序前缀已越过本窗 | 未确认10-09事件；不向旧页扩扫 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 发布列表，10-09、10-08、10-01日期前缀；进入10-09原文读取完整核心和限制 | 1家族：[非预期行动案例调查](https://www.anthropic.com/research/investigating-unintended-model-actions)。10-08科学条目不扩为本窗或暂停范围 |
| SRC-GOOGLE-AI | [Research blog](https://research.google/blog/) 日期前缀最新10-07、10-06、10-05、10-02；[DeepMind blog](https://deepmind.google/blog/) 月级卡进入首张EmbeddingGemma 2 [原文](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)，核为10-06；[Pubs](https://research.google/pubs/) 首15条只给年份 | 未确认10-09新事件。Pubs 年份排序不能恢复本窗公开段，具体目录缺段隔离；不把年度论文全送审 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 提取为空，转[Blog](https://ai.meta.com/blog/) 与[publication](https://ai.meta.com/results/?content_types%5B0%5D=publication)；读取当前11条日期前缀：10-02、09-24、09-07至07-17，后接旧模板2019即停止 | 未确认10-09事件；不是对全部年份/隐藏分页的无遗漏保证 |
| SRC-QWEN | 旧qwenlm主页转[qwen.ai/research](https://qwen.ai/research)；动态目录仅返回壳。回到[官方GitHub](https://github.com/QwenLM) 首10/59仓库；Qwen-Image-2.1 README News明确10-09 checkpoint/API；进入[官方card](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo/raw/main/README.md) 读取发布核心和sampling兼容性 | 1家族的两个发布事件；8-step为版本接口事实，不能借09-20架构加分。动态研究目录缺段终态隔离，GitHub updated不单独证明新研究 |
| SRC-DEEPSEEK | [官方News](https://www.deepseek.com/news/) 最新09-10、04-24、2025-12-01前缀；研究入口06-24、02-25等旧日期 | 未确认10-09事件；停止旧日期前缀 |
| SRC-MOONSHOT | [Platform blog](https://platform.kimi.com/blog) 26条overview最新2025-11-07；[官方组织](https://github.com/MoonshotAI) 首10/42，旧kimi-cli归档转[kimi-code Releases](https://github.com/MoonshotAI/kimi-code/releases)，最新09-24、09-17的五版本前缀 | 未确认10-09事件；不以updated或归档产生新候选，不审全部42仓库 |
| SRC-TENCENT-HUNYUAN | [Research全部列表](https://hunyuan.tencent.com/research) 正文请求超时、直接提取仅壳，独立浏览器打开也超时；[官方组织](https://github.com/Tencent-Hunyuan) 首10/85中Precise updated10-09，回[README](https://github.com/Tencent-Hunyuan/Precise) 和[5条上限commit查询](https://api.github.com/repos/Tencent-Hunyuan/Precise/commits?per_page=5)，实回3条 | Precise d07fa076为10-09 16:04:42 UTC＝北京时间10-10，且仅NIPS acceptance README；原paper/code为5月，不是本窗新论文。Research目录缺段明确受阻隔离，不报零覆盖或无遗漏 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 最新08-26、08-14、06-16日期前缀；[官方release](https://docs.z.ai/release-notes/new-released) 08-26、08-18、06-16等前缀 | 未确认10-09事件；不把旧记录搬移 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers) 第一页20/242（13页），最新08-18已早于本窗；[Research](https://seed.bytedance.com/en/research) 完整可提取页面，featured SeedRealtime明确08-05，后续07-31、07-20、07-08 | 日期目录第一段未确认10-09；停止旧日期前缀，不遍历13页年度池 |
| SRC-BAIDU-ERNIE | [中文技术博客](https://ernie.baidu.com/blog/zh/) 当前十条日期，最新05-09、04-30、04-15等至2025，分页第二页更旧 | 未确认10-09事件；停止已越窗日期前缀 |
| SRC-XIAOMI-MIMO | [官网Paper/Blog](https://mimo.xiaomi.com/) 论文8条最新06-29、03-13、02-03；Blog目录无日期，进入[Tool-Call Repetition](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition) 核为09-27。arXiv当窗2610.11959由论文来源单独核验，不重复家族 | 旧blog不搬至10-09；无日期剩余Blog项不支持零命中或全覆盖。MiMo当窗研究以必要arXiv原文/公开列表为准 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog) 首页12/13日期卡最新08-13、07-31、06-09；中文镜像同新日期；[Agent techblog](https://agent.minimax.io/docs/techblog) 三条10-08、09-22、09-19 | 未确认10-09事件，停止旧日期前缀；10-08不计本窗新研究 |

## 准入与必要审阅范围

- Anthropic：root实际读原文四类案例、环境修订和限制。候选命题仅为授权不能随工具封装/目标变化丢失、测试fixture失败不得自动提升为真实目标。厂商已知案例复测不等于未知攻击覆盖或基准失败率；安全contract变化需深入相关核心，拟2+2+2=6，独立Source与Books判断由非写入者核验。
- Qwen：同家族checkpoint/API，拟1+1+1=3最低关闭，仅报告。官方card指出默认CFG=1、8步schedule来自checkpoint、Diffusers pipeline-configured sigmas依赖，显式其他sigmas未被评价；不声称复现、普遍质量保持或prefix-cache新理论。报告作者已独立读GitHub日期及card核心并确认这一关闭判断。

## 外部来源保留项

Google Pubs公开日切片、Qwen/Hunyuan动态研究目录及MiMo未标日期Blog尚不能提供本窗确定性覆盖。当前有限可用入口已检查，剩余不是已确认候选或必须全文审阅的年度队列。恢复条件是取得相应官方本窗列表/日期段或可复查单项原始发布；只重开命中家族或目录缺段。它们不进入正面证据、Books，也不支持“无遗漏”。其他具名候选可继续，不等待这些入口恢复。
