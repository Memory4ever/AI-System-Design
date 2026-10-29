# Second batch original retrieval

Execution: `2026-10-21T16:14:51Z` (after all three requests completed).

Requested exact official HTML versions with `curl --location --fail --max-time 60`; all exited 0. Raw responses were saved directly without rewriting:

- https://arxiv.org/html/2610.25048v1 → `paper-2610.25048v1.html`, 306649 bytes.
- https://arxiv.org/html/2610.24598v1 → `paper-2610.24598v1.html`, 390013 bytes.
- https://arxiv.org/html/2610.24816v1 → `paper-2610.24816v1.html`, 555166 bytes.

Each `.text` is a mechanical local text extraction using Python standard-library HTMLParser. The HTML remains the primary original. Exact byte values above were checked using each local file's stat after retrieval. No prior versions or code fetched. The installed default Python lacks BeautifulSoup; that initial extraction failed before writing any text derivative, then the standard-library fallback succeeded.
