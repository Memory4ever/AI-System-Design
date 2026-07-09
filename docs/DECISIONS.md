# Project Decisions

## ADR-001: Use GitHub as the Single Source of Truth

Decision:

The project will no longer use Word as the primary source.

Reason:

Markdown and Git provide:

- Diff
- History
- Review
- Branching
- Collaboration

Word may be generated as a release artifact.

---

## ADR-002: Organize Around Problems, Not Frameworks

Decision:

Frameworks such as vLLM and KServe will not define the top-level
knowledge architecture.

Reason:

Frameworks change.

Underlying system problems remain.

For example:

Inference Scheduling
    ├── vLLM
    ├── SGLang
    └── future systems

instead of:

vLLM
SGLang
KServe

---

## ADR-003: Store Book Content Under `books/`

Decision:

All generated book content will live under `books/`.

The directory is organized by the six roadmap parts:

- `books/part-01-worldview`
- `books/part-02-model`
- `books/part-03-training-system`
- `books/part-04-inference-system`
- `books/part-05-ai-infrastructure`
- `books/part-06-agent`

Each chapter is stored as an individual Markdown file in its corresponding
part directory.

Reason:

`ROADMAP.md` should remain the single source of truth for the knowledge tree,
chapter ordering, and learning route.

Chapter content needs a separate stable location so the repository can grow
from roadmap to book without mixing planning, state, and long-form writing in
one file.
