# 2026-10-03 有限来源检查停点

检查：2026-10-03T09:02:40+08:00～2026-10-03T09:10:03+08:00。
窗口：2026-10-02T09:00:00+08:00～2026-10-03T09:00:00+08:00。
作者：daily_oct03；非作者/root已定点核Google传播、Anthropic培训、Meta两题摘及arXiv公告排程。未扫描周级库存或历史池；无stage/commit/push。
本记录的已检查是有限入口/主题/窗口检查，不是全网、全站或全年零遗漏。原始命中不计候选，必要正文/日期缺失不当零命中。

| 来源 | 实际入口/有限停点 | 结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research → Research index，首屏九条显示9/29～9/03，最上GPT6.1 Sol及同日addendum；没有继续Load more | 该有限最新列表未显示窗内研究；未声称完整网站修订监控 |
| SRC-ANTHROPIC | Research初次两次timeout，尾斜线入口恢复原Research；Publications首屏到9/04、最上10/01 Claude-shaped science；News首屏Oct2 Academy、Oct1 Barclays，实际打开Academy核心全文 | 培训公告贡献关闭，Research最上science按ROADMAP暂缓；不以最初timeout为已检查证明 |
| SRC-GOOGLE-AI | DeepMind Research→Blog首屏9月到8月，Google pubs首屏1–15/11573、只年级日期且含2027；Google Research Blog第1/135页Oct2 FL→9/29后旧条目，打开FL与对应2609.31494完整题摘/版本史 | Blog传播关闭；pubs无窗内首公开定位隔离，不把11573条当日新材料或全量队列 |
| SRC-META-AI | Research初始空文本→Blog首屏latest7/27、Publications首屏六条Oct2数学到Sep24 MaD-RL；两相近题目完整题摘已读，其余四明确数学范围标题关闭 | 六条Oct2登记不是模型论文增量；已有限检查，不声称元数据日期即首次公开或全站召回 |
| SRC-QWEN | qwenlm.github.io旧页9/23/2025；官方跳转qwen.ai/research Web返回0lines，浏览器显示研究/研究索引/排序但无材料卡片；补搜索site:qwen.ai限定2026-10-02与October2结果空 | 动态研究索引空壳，当前可用入口未恢复列表，具名隔离；搜索空结果不证明无发布 |
| SRC-DEEPSEEK | 官网研究导航最新V4.1，进入V4.1Flash发布原页日期9/10；首页没有更晚研究事件 | 在此有限入口无确定窗内事件，不把模型banner视为新发布 |
| SRC-MOONSHOT | Kimi Blog overview最新11/07/2025；MoonshotAI组织Research与本页10个更新库，只有kimi-code UpdatedOct2；定点打开kimi-code Releases最新2.1.1 Sep24、2.1.0 Sep23及当前安全/revert说明 | 更新日期不等发布事件；已核窗外release，不展开所有PR/仓库 |
| SRC-TENCENT-HUNYUAN | 首查Research两次web timeout后浏览器成功；/research?page=1“全部”实际读取11条，首条日期2026-09-22，第二条同日，之后Aug28/Aug11、Jul21～Feb03；未证明全站总数 | 本页最新日期2026-09-22，止于该页，无确定window研究；未用featured替代全部 |
| SRC-ZAI | 首查Research时间排序可读，topGLM5.3Flash8/26、GLM5.3 8/14；官方release notes top8/26→8/18，无Oct2 | 有限最新段无窗内新事件，不展开历史报告 |
| SRC-BYTEDANCE-SEED | Research Blog latestSeedRealtime首页无日期，打开原页恢复8/05；Publications Newest→oldest第1/13页20/242，top8/18，止于第一页 | 两入口最新段窗外，未把AIforScience条目经通用Node引入 |
| SRC-BAIDU-ERNIE | ERNIE中文Blog第1/2页最新5/09，其余4月→2025旧条目，停止 | 本页未显示窗内事件，未读取历史全文 |
| SRC-XIAOMI-MIMO | 官网Paper八条最新MOPD6/29；Blog可见最新工具调用重复纠错/模型发布等，无目录日期；浏览器打开第一条工具重复原页9/27，API更新明确9/25 06:00UTC+8 | 该明确纠错窗外；其余无日期目录不授全站零遗漏，恢复日期明确材料后仅定点重开 |
| SRC-MINIMAX | 英文Blog可见首屏最新8/13；中文跳转minimax.cn/blog同为8/13，停止；Agent TechBlog入口仅15lines导航无dated文章 | 双语Blog有限最新段已查；TechBlog动态空目录隔离，不用其空响应证明无新原文 |
| SRC-ARXIV | 四主类cs.CL/cs.LG/cs.DC/cs.AI recent与cs.CV/cs.RO/cs.AR/cs.PL/cs.OS/cs.PF/cs.IR/cs.MA recent首屏日期；cs.CL/new显示Friday2 October，availability排程实际已读；四主题API见下 | 本窗不含常规公告批次；API是submittedDate查漏而非公开判据，一项timeout隔离 |

## arXiv查询原值与停止条件

接口：export.arxiv.org/api/query，start=0，max_results=50，sortBy=submittedDate，descending；submittedDate仅旁证查漏，不用于首次公开归属。
日期代理范围是202610010000～202610022359UTC，**不是报告public-window覆盖**；因为目录/正式排程已经显示本窗无正常announcement，旧代理返回不展开为全文队列。

1. (cat:cs.CL OR cat:cs.LG) AND (all:"large language model" OR all:transformer OR all:"mixture of experts") AND submittedDate:[202610010000 TO 202610022359]
   HTTP200，totalResults87，只有start0第一页50，最新可见字段10/01；未翻第2页，不宣称87项题摘关闭。
2. (cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:"model serving" OR all:"distributed training") AND submittedDate:[202610010000 TO 202610022359]
   HTTP200，totalResults6，第一页已到底；只核这是旧提交字段，未对六项展开贡献判定。
3. (cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:agent OR all:"retrieval augmented" OR all:memory) AND submittedDate:[202610010000 TO 202610022359]
   15秒timeout，HTTP000，不记录为0results，不支持Agent/RAG/Memory主题覆盖。
4. (cat:cs.CV OR cat:cs.RO) AND (all:"foundation model" OR all:"world model" OR all:VLA OR all:multimodal) AND submittedDate:[202610010000 TO 202610022359]
   HTTP200，totalResults46，第一页已到底；只核旧提交字段，不逐篇清退宽命中。

正常公告窗口排除包含new、replacement、cross-list、withdrawal；不能据此保证所有作者原站/异常发布没有事件。没有新增候选触发按需source；不扫描每周组。候选0，不表示互联网发布0。

## 空响应与终态保留项

Qwen无材料卡片、Google publications仅年级/未来发表元数据、MiniMax Agent TechBlog空导航、MiMo其余无日期Blog目录、arXiv Agent主题API timeout均没有转化为正面Coverage/Evidence。已执行本轮有限原入口/重试；恢复条件见README§5。MetaResearch空文本已被官方Blog/Publication有限入口恢复，不再仅靠失败结果判零。
