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

## Writing a Technical Evolution Route

When a chapter contains more than one generation of a design, do not organize
the section as a list of release dates or as “old versus latest”. Use each
transition as a reasoning unit:

1. **Original problem and constraint**: what workload, hardware, scale, or SLO
   made the earlier design reasonable?
2. **Earlier mechanism and strength**: what did it solve well, and where is it
   still sufficient?
3. **Boundary exposed**: which pressure could it no longer absorb?
4. **Constraint shift**: what changed enough to justify a different design?
5. **New mechanism**: which state, data flow, algorithm, or control decision
   changed?
6. **Benefit and proof boundary**: what improved, under which verified
   conditions?
7. **New debt**: what cost, coupling, correctness requirement, observability
   need, or failure mode was introduced?
8. **Relationship**: is this direct evolution, layering/dependency, principle
   reuse, or only an explanatory analogy?
9. **Coexistence and next pressure**: when should the earlier design remain,
   and what unresolved pressure may cause the next transition?

A compact reusable form is:

```text
A
  solved: ...
  under: ...
  but exposed: ...

constraint shift: ...

B
  changed: ...
  gained: ...
  introduced: ...

relationship: replacement | coexistence | layering | principle reuse
next pressure: ...
```

Do not delete an earlier mechanism merely because a newer paper or framework
exists. Mark it obsolete only when primary evidence shows that its validity
boundary has disappeared or its premise is wrong; otherwise preserve it as a
conditional branch in the design space.
