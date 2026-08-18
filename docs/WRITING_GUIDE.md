# 章节写作指南

## 模板原则

章节模板是一份思考检查清单，而不是最终目录必须采用的固定形式。

在 Placeholder 或早期 Draft 阶段，章节可以保留完整脚手架，以免遗漏重要推理。

进入后期 Draft、Review 或 Final 阶段后，应根据主题重组可见标题，让章节自然流畅。若显得生硬，章节不必把 `Problem`、`Math`、`Engineering` 或 `Research Outlook` 原样用作标题。

不过，每个重要章节仍应回答这些底层问题：问题为何存在、设计如何出现、哪些替代方案失败了、涉及什么机制、哪些工程约束重要、存在哪些取舍，以及该主题位于 AI System 知识树的什么位置。

每个重要章节都应回答五个层次的问题。

## 层次一：问题（Problem）

我们要解决的根本问题是什么？

## 层次二：设计推导（Design Derivation）

如果我们还不知道现代方案，会如何自行发明它？

探索朴素方案，以及它们为何失败。

## 层次三：机制（Mechanism）

解释其数学与算法机制。

## 层次四：工程（Engineering）

解释该思想如何与以下因素相互作用：

- GPU
- Memory
- Communication
- Scheduling
- Distributed systems
- Production serving

## 层次五：系统位置（System Position）

解释这一概念如何与整个 AI System 连接。

例如：

```text
Tokenizer
→ Embedding
→ Attention
→ KV Cache
→ PagedAttention
→ vLLM
→ PD Disaggregation
→ LLM Runtime
```

## 如何书写技术演进路线

演进关系及其判断标准只由 [LEARNING_PHILOSOPHY.md](./LEARNING_PHILOSOPHY.md) 定义。本文件只规定如何把那条推理写成可顺读的章节：不要按发布日期罗列，而要让读者看到旧方案成立、约束变化、新机制接手以及新债务出现的连续过程。

可以复用下面这个紧凑结构：

```text
A
  解决了：...
  成立条件：...
  但暴露了：...

约束变化：...

B
  改变了：...
  获得了：...
  引入了：...

证据边界：证明了...；没有证明...
关系：直接演进 | 分层/依赖 | 原理复用 | 类比 | 替代分支
下一重压力：...
```

不要仅仅因为出现了更新的论文或框架，就删除较早的机制。只有 primary evidence 表明其有效边界已经消失或前提本身错误时，才能将其标记为过时；否则，应把它作为设计空间中的条件分支保留下来。
