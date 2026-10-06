# Five exact date fields under calibrated lifecycle condition

Exact primary: https://api.datacite.org/dois/ ; selected necessary original body excerpts actually read, not full-attachment review.

Each ID queried GET /dois/10.48550/arxiv.<ID>, actual publisher arXiv/state findable. Raw Submitted-v1(s),Updated-v1(u),created(c),registered(r) values retained without substituting one field for another:

```json
[
  {
    "id": "2601.09088",
    "s": "2026-01-14T02:43:17Z",
    "u": "2026-01-15T01:12:38Z",
    "c": "2026-01-15T02:37:51.000Z",
    "r": "2026-01-15T02:37:51.000Z"
  },
  {
    "id": "2601.09258",
    "s": "2026-01-14T07:46:59Z",
    "u": "2026-01-15T01:25:35Z",
    "c": "2026-01-15T02:41:52.000Z",
    "r": "2026-01-15T02:41:52.000Z"
  },
  {
    "id": "2601.09292",
    "s": "2026-01-14T08:53:16Z",
    "u": "2026-01-15T01:28:19Z",
    "c": "2026-01-15T02:42:39.000Z",
    "r": "2026-01-15T02:42:40.000Z"
  },
  {
    "id": "2601.09445",
    "s": "2026-01-14T12:45:52Z",
    "u": "2026-01-15T01:39:01Z",
    "c": "2026-01-15T02:46:12.000Z",
    "r": "2026-01-15T02:46:13.000Z"
  },
  {
    "id": "2601.08951",
    "s": "2026-01-13T19:41:11Z",
    "u": "2026-01-15T01:03:51Z",
    "c": "2026-01-15T02:34:42.000Z",
    "r": "2026-01-15T02:34:43.000Z"
  }
]
```

All five s fields actually lie [Jan13T19Z,Jan14T19Z); each r is completely before Jan16T01Z. Under root-actually-calibrated policy in DATE_PRIMARY_NORMAL_08919.md and absent earlier-public正文 signal, each conditional first-arXiv range is [Jan15T01Z, its own c+1second). Updated alone is not proof; original +.000 precision is conservatively treated as whole seconds. This grants neither exact first-second nor other unknown IDs. Earlier author manuscript/publication or lifecycle exception reopens the affected item. Subsequent v2 Submitted/Updated fields were visible but are different events, not a current-v1 diff task.
