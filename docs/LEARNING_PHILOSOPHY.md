# Learning Philosophy

## First Principle

Do not reveal the standard solution too early.

Begin with the original problem.

Let the reader experience why simpler designs fail.

Then derive the modern design.

## Example

Do not begin an Attention chapter with:

Q = XWq
K = XWk
V = XWv

Instead begin with:

Suppose each token must understand itself using the rest of the sequence.

What mechanism would we invent?

Why is an MLP insufficient?

Why did RNNs struggle?

Why do we need content-dependent routing?

Only after deriving the need should Q, K and V appear.

## Preferred Reasoning Pattern

Problem
→ Naive Solution
→ Failure
→ Better Solution
→ New Failure
→ Modern Design

## Evolution Is a Constraint History, Not a Ranking

Do not present technical evolution as:

```text
old technology was wrong
→ new technology replaced it
→ only the latest design matters
```

An earlier design usually optimized for a real constraint and may remain the
better choice inside that boundary. A later design should not silently erase
that context. For every important transition from design `A` to design `B`,
reconstruct:

```text
original constraint
→ why A was reasonable
→ where A reached its boundary
→ what changed in workload / scale / hardware / SLO
→ what mechanism B introduced
→ what B improved
→ what new cost, state, coupling or failure mode B introduced
→ where A and B still coexist
→ what pressure may drive the next design
```

Before drawing an evolution arrow, identify the relationship:

- **Direct Evolution**: `B` inherits, extends, or replaces `A`.
- **Layering / Dependency**: `A` and `B` solve different layers and compose.
- **Principle Reuse**: both respond to similar constraints without direct
  lineage.
- **Explanatory Analogy**: similarity helps learning but is not historical or
  implementation evidence.

“Newer” is metadata, not a design conclusion. The goal is to recover the
reasoning that made each design rational, and the constraint shift that made a
different design necessary.

## Core Focus

Prefer:

- Why
- Trade-offs
- Evolution
- Alternative designs
- Dead ends
- Engineering constraints

Avoid:

- Definition dumping
- API documentation style
- Framework catalogues
- Memorization-oriented writing
