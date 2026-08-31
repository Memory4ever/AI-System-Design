# arXiv cutoff listing recovery extract

- Original access time: `2026-08-31T09:07:00+08:00`
- Report window: `[2026-08-30T09:00:00+08:00, 2026-08-31T09:00:00+08:00)`
- Endpoint: `https://arxiv.org/list/cs/new`
- Original first-page snapshot byte size: `319583`
- Recovery source: original Codex execution transcript retained outside the deleted project tree

## Preserved cutoff observations

The original execution recorded these exact listing facts before the page advanced:

```text
Showing new listings for Friday, 28 August 2026
New submissions (showing first 100 of 638 entries)
```

The execution also attempted a submitted-date API query, but the archived request
shows that the end bound was truncated to `2608310100`. Its
`opensearch:totalResults=0` is therefore invalid as strict-window evidence. The
768-byte response is retained as `arxiv-window.invalid-recovery.atom` solely to
make that failure auditable.

## Recovery boundary

The original HTML bytes were lost in the accidental recursive deletion. A live
re-fetch later on 2026-08-31 already exposed a newer listing state, so the two
late pages are preserved with the suffix `.recovery-late.html` and are not used
as evidence for the 09:00 cutoff. The report's cutoff conclusion relies on this
execution-transcript listing extract, not on the later pages or the malformed
Atom response.
