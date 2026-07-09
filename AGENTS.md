# AGENTS.md

## Project

This repository is a long-term living book and learning system titled:

《AI System：从第一性原理到 AI 基建》
AI System: From First Principles to AI Infrastructure

It is not a collection of random AI notes.

The goal is to build a coherent knowledge system for understanding and
designing modern AI systems, from model fundamentals to training,
inference, AI infrastructure, and agents.

## Primary Reader

The primary reader is an experienced software and infrastructure engineer
with background in:

- Distributed systems
- Flink and Kafka
- Kubernetes
- Kubeflow
- KServe
- Model training platforms
- LLM inference infrastructure

The reader is currently building an end-to-end AI model lifecycle platform:

Data / Training → Model → Deployment → Serving → Observability.

Do not write for a complete beginner.

## Core Learning Philosophy

Always prioritize:

1. Why the problem exists
2. Why the current design emerged
3. What alternatives were possible
4. Why some alternatives failed
5. The mathematical principle
6. The engineering implementation
7. The system trade-offs
8. How the design fits into the global AI System knowledge tree
9. What may change when future constraints change

Avoid API-first explanations.

Avoid simply listing concepts.

Prefer first-principles derivation and design reasoning.

## Required Reading Before Major Changes

Before changing the roadmap or writing a chapter, read:

1. `ROADMAP.md`
2. `docs/PROJECT_CONTEXT.md`
3. `docs/LEARNING_PHILOSOPHY.md`
4. `docs/WRITING_GUIDE.md`
5. `docs/LEARNING_STATE.md`

Do not update a chapter in isolation without understanding its position
in the global knowledge tree.

## Single Source of Truth

`ROADMAP.md` is the authoritative knowledge tree.

Every major new topic must first be located in the knowledge tree.

Do not create disconnected notes when the topic belongs to an existing
chapter.

## Chapter Design

Unless there is a strong reason otherwise, chapters follow:

1. Chapter Question
2. Problem
3. Thought Experiment
4. History / Evolution
5. First Principles
6. Math
7. Engineering
8. Design Trade-offs
9. Alternatives and Dead Ends
10. Engineering Practice
11. AI System Position
12. Interview Questions
13. Research Outlook
14. Reflection

## Writing Style

Write primarily in Chinese.

Keep technical terms in English when that improves precision.

Use coherent prose rather than fragmented one-line sentences.

Explain from first principles.

Focus on design philosophy and trade-offs.

Never invent implementation details, benchmarks, papers, or framework behavior.

For current frameworks and recent research, verify against primary sources.

## Change Discipline

Before making a substantial change:

1. Identify the target knowledge-tree node.
2. Read adjacent chapters.
3. Preserve terminology consistency.
4. Update `docs/LEARNING_STATE.md` when learning progress changes.
5. Update `docs/DECISIONS.md` for major structural decisions.

The goal is not to maximize the amount of content.

The goal is to build a coherent AI System mental model.