# 01-16 / SlidesGen-Bench 单篇必要原证与 owner 差额

作者准备包，等待 root 独立准入/原证/实际 owner PRE；没有写 Books，没有把本包当日级验收。

## 当窗与身份

- exact-v1： https://arxiv.org/html/2601.09487v1 ，题摘、HTML及请求保存在 `supplement-20261007/abs09487.*`、`html09487.*`。
- Atom/submitted Jan14T13:50:30Z 仅发现字段。官方 availability 公告规则对正常 cohort 提供 BJT Jan15 下界；exact DOI `10.48550/arXiv.2601.09487` Jan15T02:47:11Z registered 的公开存在记录提供 Jan15 上界；**registered 不是 first-public**。自然日条件归属 Jan15；未要求时刻。月列表只身份覆盖。
- 直接论文链接 GitHub `YunqiaoYang/SlidesGen-Bench` README 轻量读到现版本、2025Nov–Dec commercial access/2026 EMNLP及 arXiv citation，未出现更早论文正文发布声明；商业产品访问日期不是本论文先公开证据。未遍历全 commit/history。

## 三维必要审阅

**方法对象。** §2.2 QuizBank 从输入参考构造带 page/source_quote 的问答，生成 slide 图像先解析成 Markdown，再让 evaluator 回答；测的是可恢复事实代理，不是完整语义质量。§2.4/Appendix I 的 PEI 用格式routing与交互/原生对象检查区分单页像素、可独立编辑组件、native chart/data、master/hierarchy、timeline；不是只从渲染推断编辑性。I.4含实际文字扩展、group移动、master修改传播和chart数据修改检查，不把它写成全部自动parser已实现。图像作为统一内容/视觉观察，native对象作为较深编辑观察，两种输入不能互换。其web输入一律cap L2及PDF不可选的断言过强，不采用为通用格式定理；合法HTML/PDF内部对象可能比作者设定更丰富。

**有效证据。** §3.1/3.3、Tables1/2/5、Figure4：189任务（94 Wikipedia、95六行业场景）、9平台，现成图像/代码方案均可渲染但 PEI 能力分层不同；NotebookLM L0、图像方案 L1、Quark L3。跨平台调用失败/N/A使人口不完全相同，不拿综合排名隔离模型或生成范式因果。§3.2的人审相关 `.71±.16` 低于人际 `.85±.12`，只是有限样本相关，不是 scorer truth。

**反侧与费用。** §3.3 13,023 QuizBank问题中2,499失败，6.6%失败归于 VLM extraction，故 failure 不能全部归责生成系统；missing content主文57.7%与Appendix K Table17的1541/2499=61.7%不一致，不将二者统一，分母均为失败子集而非所有任务。Limits主要英语、静态deck，不认证真实动画/工作流。PEI等级不是任意修改任务必成功。渲染、视觉解析、native structure解析、QuizBank生成/回答、人审校准和无效调用均计费；缺参考或转换损坏时回退人工实改/分项观察，不以渲染成功授可维护交付。该文本/表反侧由root独立PRE指出并定点补核。

## 实际 owner 差额

`PLATFORM-EVALUATION-SYSTEM` / `Books/part-06-ai-infrastructure/66-evaluation-system.md` 当前 EvalSpec L107–130 已实际顺读，GDPval段L119要求保留 input/output artifact+可见渲染、accuracy/aesthetics分账，仍未解释**render-equivalent但native可编辑性不同**及哪个观测有权判后续修改。精准新增并非“再保存artifact”，而是 rendered content/presentation 与 native editability双观察、能力与真实修改结果分责。邻接分析规范搜索、metric条件化不冲突。

建议 gap 深入、2+1+2=5；拟写两段放 GDPval段后。不给作者 PEI普适采用权，不加入平台排名。不修改 Ch84或重复owner。

### 拟写正文（待 root 授窄锁）

同一 deck 能够正常渲染，也不等于它能被后续工作流维护。图像式生成与代码式生成可以用相同 rendered view 比较内容和呈现，却可能留下完全不同的 native 对象：文字与图表是否能独立修改、chart 是否保留数据、主题/层级是否可复用，需要读取原交付 artifact，而不能由截图相似度或整体偏好反推。EvalSpec 应把 rendered-content/presentation 与 native-editability 分成两类观察，再由真实修改任务检查这些能力是否足够；可编辑对象的存在仍不保证任意修改正确完成。[SlidesGen-Bench 的受限对照](https://arxiv.org/html/2601.09487v1)支持这种观察分工，不使某个分层等级成为所有交付物的通用合格证。<!-- source-family:SF-2026-ARXIV-2601-09487 -->

这增加渲染、视觉解析、native structure 检查、参考问答构造与人工校准费用；转换失败或视觉读取错误也应分开归因，不能全部写成生成器遗漏。作者九平台、189任务的主要英语静态 deck 对照中，问答失败包含 VLM extraction error，相关性与各平台缺失人口也不能认证任意用户、动画或后续编辑工作流。只需浏览的交付仍可保留图像式方案；需要维护而原生结构不可取得、scorer 未校准或修改测试失败时，回退人工实改、可核的模板/代码生成与分项验收，不用一个视觉总分批准可维护交付。
