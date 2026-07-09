<p align="center">
  <img src="./assets/logo.png" width="96" alt="AI System icon" />
</p>

<h1 align="center">AI System：从大模型原理到 AI 基建</h1>

<p align="center">
  一套面向 AI Infra 工程师的长期知识树：从第一性原理理解模型、训练、推理、平台与 Agent。
</p>

---

## 这个项目是什么

这不是一组 AI 框架笔记，也不是 API 使用手册。

这个项目要建立一棵稳定的 **AI System Knowledge Tree**，帮助你回答：

> 一个技术为什么出现？它解决了什么系统问题？做出了什么 trade-off？如果约束变化，它还成立吗？

目标不是“会用更多框架”，而是形成能设计 AI 系统的判断力。

## 项目亮点

- **问题优先**：先问 Why，再讲 What，最后讲 How。
- **第一性原理**：从原始约束推导设计，而不是直接背标准答案。
- **系统视角**：把 Tokenizer、Attention、KV Cache、vLLM、KServe、GPU Scheduler、Agent 放回同一棵树。
- **工程取舍**：持续关注 GPU、memory、latency、throughput、cost、observability 和 governance。
- **长期稳定**：框架会变，底层问题长期存在。本项目围绕问题组织知识，而不是围绕框架组织目录。

## 知识树主线

| Part | 主题 | 核心问题 |
| --- | --- | --- |
| I | 世界观 | AI System 为什么会发展成今天这样 |
| II | 模型 | 一个 token 如何变成答案 |
| III | Training System | 模型能力如何产生 |
| IV | Inference System | 为什么推理是 AI Infra 的核心战场 |
| V | AI Infrastructure | 如何从工具走向平台 |
| VI | Agent | 如何从回答问题走向执行任务 |

## 当前状态

- Roadmap：已初始化 80 章知识树，见 [ROADMAP.md](./ROADMAP.md)
- Book：章节内容统一放在 [books/](./books/)
- Current Draft：[第1章 为什么学习 AI System](./books/part-01-worldview/01-why-learn-ai-system.md)
- Writing Rule：模板是 thinking checklist，不是最终目录结构，见 [docs/WRITING_GUIDE.md](./docs/WRITING_GUIDE.md)

## 推荐阅读方式

1. 先看 [ROADMAP.md](./ROADMAP.md)，建立全局地图。
2. 再读 [第1章 为什么学习 AI System](./books/part-01-worldview/01-why-learn-ai-system.md)，理解项目的问题意识。
3. 后续按六大部分推进：世界观 → 模型 → 训练系统 → 推理系统 → AI 平台 → Agent。

## 仓库结构

```text
books/                 # 正式书稿内容
  part-01-worldview/
  part-02-model/
  part-03-training-system/
  part-04-inference-system/
  part-05-ai-infrastructure/
  part-06-agent/

docs/                  # 项目上下文、写作原则、学习状态、决策记录
assets/                # README 和文档使用的图标、图片资源
ROADMAP.md             # AI System knowledge tree single source of truth
```

## 一句话

先建立树，再长叶子。

以后每遇到一个新模型、论文、框架、runtime 或 Agent 技术，先问：**它在 AI System 这棵树上的位置是什么？**
