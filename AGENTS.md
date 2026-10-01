# AGENTS.md

## 定位

面向有模型训练与 LLM 推理基础设施经验的工程师，构建连贯、可验证的 AI System 知识体系。

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
2. `docs/RESEARCH_SOURCES.md` 的使用说明与本次频率分组
3. `docs/REPORT_CONTRACTS.md`
4. `CODEX_RESEARCH_PROMPT.md`
5. `ROADMAP.md` 与最新相关 checkpoint

生成和续跑 Report 均按当前合同。**每份 Daily 独立执行**：启动、换日、委派或压缩恢复时重读本文件与上述适用内容，只加载当日窗口、材料和停点。月度 checkpoint 只作路由；跨日仅定点核去重、首公开归属或共享 Books 冲突。不同日期/周按独立文件 ownership 并行，共享 Books/索引文件写入前先协调 ownership。

公共规则按唯一 owner 维护：`docs/RESEARCH_CONTRACT.md` 负责贡献筛选、去重、评分、证据审阅与 Books 判断；
`docs/RESEARCH_SOURCES.md` 负责来源入口；`docs/REPORT_CONTRACTS.md` 负责时间窗口、报告结构、独立复核与完成条件。
Prompt、Heartbeat 与其他说明文件只引用，不复制这些定义。

Research → Books 按研究合同执行；开始改书时再加载上面的 Books 上下文。校验器只检查格式与可判定的一致性，语义验收按 Report 合同执行。

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
