# Chapter Writing Guide

## Template Principle

The chapter template is a thinking checklist, not a required final table of
contents.

During Placeholder or early Draft stages, chapters may keep the full scaffold
to avoid missing important reasoning.

During later Draft, Review, or Final stages, restructure the visible headings
so the chapter reads naturally for its topic. A chapter does not need to expose
`Problem`, `Math`, `Engineering`, or `Research Outlook` as literal headings if
that would feel forced.

However, every major chapter should still cover the underlying questions:
why the problem exists, how the design emerged, what alternatives failed, what
mechanism is involved, what engineering constraints matter, what trade-offs
exist, and where the topic sits in the AI System knowledge tree.

Every major chapter should answer five levels of questions.

## Level 1: Problem

What fundamental problem are we solving?

## Level 2: Design Derivation

If we did not know the modern solution, how might we invent it?

Explore naive solutions and why they fail.

## Level 3: Mechanism

Explain the mathematical and algorithmic mechanism.

## Level 4: Engineering

Explain how the idea interacts with:

- GPU
- Memory
- Communication
- Scheduling
- Distributed systems
- Production serving

## Level 5: System Position

Explain how this concept connects to the entire AI System.

For example:

Tokenizer
→ Embedding
→ Attention
→ KV Cache
→ PagedAttention
→ vLLM
→ PD Disaggregation
→ LLM Runtime
