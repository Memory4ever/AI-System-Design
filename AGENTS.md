# AGENTS.md

## 项目

本仓库是一套长期维护、持续演进的书稿与学习系统：

《AI System：从第一性原理到 AI 基建》
AI System: From First Principles to AI Infrastructure

它不是随机 AI 笔记、新闻收藏或框架手册。目标是建立一套连贯的知识系统，用于理解和设计现代 AI 系统，从模型基础、多模态与世界模型延伸到 Training、Inference、AI Infrastructure 与 Agent。

## 主要读者

主要读者是经验丰富的软件与基础设施工程师，熟悉：
- 模型训练平台与 LLM 推理基础设施。

读者正在建设端到端 AI 模型生命周期平台：

```text
Data / Training → Model → Deployment → Serving → Observability
```

不是面向毫无基础的初学者写作。

## 项目级不变量

1. 先解释问题、约束和旧方案为何合理，再解释现代机制。
2. 数学、工程实现、系统取舍和 failure mode 必须回到同一条推理链。
3. 新技术不得静默覆盖旧方案；要保留约束变化、共存边界和下一重压力。
4. 不按框架或论文名称堆砌内容；每个机制必须有唯一知识 owner。
5. 绝不虚构实现、benchmark、论文、版本或实验结论。近期事实必须核验 primary source。

完整学习方法由 `docs/LEARNING_PHILOSOPHY.md` 定义，章节呈现方式由 `docs/WRITING_GUIDE.md` 定义。不要在本文件维护第二份章节模板或演进词汇表。

## 唯一事实来源

`ROADMAP.md` 是知识树、Stable Knowledge Node ID、章节顺序和路径的唯一事实来源。

每个重要主题必须先定位到现有 owner。只有现有结构确实无法承载一条长期知识链时，才提出 `Structural Candidate`；不要创建彼此割裂的笔记或“前沿收纳章”。

## 按任务加载上下文

### 修改 ROADMAP 或 Books

先读取：

1. `ROADMAP.md`
2. `docs/PROJECT_CONTEXT.md`
3. `docs/LEARNING_PHILOSOPHY.md`
4. `docs/WRITING_GUIDE.md`
5. `docs/LEARNING_STATE.md` 中最新相关 checkpoint
6. 目标章节与相邻章节

### 生成 Daily、Weekly 或 Historical Weekly

先读取：

1. `docs/RESEARCH_CONTRACT.md`
2. `docs/RESEARCH_SOURCES.md`
3. `docs/REPORT_CONTRACTS.md`
4. `CODEX_RESEARCH_PROMPT.md`
5. `ROADMAP.md` 与最新相关 checkpoint

生成和继续生成 Report 一律执行当前合同；字段细节在对应步骤需要时加载。历史报告默认只读取去重身份和
未决项索引，命中具体关联再读正文。不同日期/周按独立文件 ownership 并行，共享文件才协调写入。

公共规则按唯一 owner 维护：`docs/RESEARCH_CONTRACT.md` 负责贡献筛选、去重、评分、证据审阅与 Books 判断；
`docs/RESEARCH_SOURCES.md` 负责来源入口；`docs/REPORT_CONTRACTS.md` 负责时间窗口、报告结构、独立复核与完成条件。
Prompt、Heartbeat 与其他说明文件只引用，不复制这些定义。

`scripts/validate_research.py` 只检查格式与可判定的一致性，不能证明来源被正确理解或长期结论成立。
报告完成必须有充分证据、落实必要的 Books 改动，并通过独立语义复核；不能用校验通过或额外收据替代实际研究。

### Research → Books

候选满足 Report 合同的单篇证据与独立复核条件且可能改变长期知识后，再读取目标命题及相邻交接内容，执行
Books Decision；不等待无关候选，但整体报告不能提前 Complete。Weekly 摘要、评分或 `Must Read` 本身不构成 Books Gate。

## 写作风格

- 以中文为主；英文能提高精度时保留技术术语。
- 使用连贯叙述，不堆砌割裂单行句。
- 优先回答 Why、Mechanism、Trade-off、Evolution 与系统位置。
- 项目或论文名称只作为机制证据、替代方案或受限案例；删除名称后，正文仍应成立。

## 修改纪律

进行实质性修改之前：

1. 确定目标知识节点和文件范围；
2. 阅读相邻内容并保留术语一致性；
3. 保护运行前已有及无关修改；
4. 学习进度或稳定认知实际变化时，只增加必要的 `LEARNING_STATE` checkpoint；
5. 重大结构或公共合同取舍尚待选择、验证时写入 `docs/DECISIONS.md`；落实后更新对应权威文件并移除待决记录；
6. 检查 Markdown、链接、`git diff --check`、diff 与工作树范围。

除非用户明确授权，不 stage、commit、push，不执行破坏性 Git 操作。

目标不是让内容数量最大化，而是建立可验证、可维护、连贯的 AI System 心智模型。
