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