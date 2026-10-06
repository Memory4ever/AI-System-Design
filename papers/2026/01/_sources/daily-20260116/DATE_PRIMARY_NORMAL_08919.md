# arXiv lifecycle: one normal-ID calibration

Primary policy: https://info.arxiv.org/help/availability.html, actually retrieved 2026-10-03; web lines 172,175–176,183,189,192–193.

Original policy excerpts:

“Submissions are made public as part of the scheduled announcement process.”

“The final arXiv identifier is assigned as part of the automated process when the work is announced.”

“It is not possible to generate or to be provided with the arXiv identifier or DOI in advance.”

“The arXiv identifier cannot be back-dated, so identifiers will be assigned in the month of first announcement.”

Schedule original row (all times Eastern US): Tuesday 14:00 – Wednesday 14:00 | Wednesday 20:00 | Wednesday night / Thursday morning.

2026 holidays adjacent original entries: Thursday 2026-01-01; Monday 2026-01-19. Policy allows deferred mailings for ad hoc reasons; schedule is not an unconditional timestamp guarantee.

Exact DataCite GET: https://api.datacite.org/dois/10.48550/arXiv.2601.08919 ; arXiv-deposited metadata, not an independent first-public witness. Raw relevant attributes:

```json
{
  "created": "2026-01-15T02:33:57.000Z",
  "registered": "2026-01-15T02:33:58.000Z",
  "dates": [
    {
      "date": "2026-01-13T19:01:16Z",
      "dateType": "Submitted",
      "dateInformation": "v1"
    },
    {
      "date": "2026-01-15T01:02:06Z",
      "dateType": "Updated",
      "dateInformation": "v1"
    },
    {
      "date": "2026-04-24T12:16:18Z",
      "dateType": "Submitted",
      "dateInformation": "v2"
    },
    {
      "date": "2026-04-27T00:36:56Z",
      "dateType": "Updated",
      "dateInformation": "v2"
    },
    {
      "date": "2026-01",
      "dateType": "Available",
      "dateInformation": "v1"
    },
    {
      "date": "2026",
      "dateType": "Issued"
    }
  ],
  "url": "https://arxiv.org/abs/2601.08919",
  "state": "findable",
  "publisher": "arXiv",
  "types": {
    "ris": "GEN",
    "bibtex": "misc",
    "citeproc": "article",
    "schemaOrg": "CreativeWork",
    "resourceType": "Article",
    "resourceTypeGeneral": "Preprint"
  }
}
```

Author reasoning (pending root calibration): Submitted Jan13 is not public. Updated-v1 Jan15T01:02:06Z is not by itself first-public. Under the official scheduled/no-advance lifecycle, first arXiv announcement is conditionally no earlier than Jan15T01:00Z (Jan14 Wed20 EST); findable arXiv DOI record created Jan15T02:33:57Z gives a conservative existence upper Jan15T02:33:58Z at whole-second precision. Proposed range [2026-01-15T01:00:00Z,2026-01-15T02:33:58Z) fully lies in the window. This is conditional inference, not a recovered announcement log; no blanket range is granted to other IDs. Earlier author-public正文, lifecycle exception or contradictory historical announcement evidence reopens only the affected ID. The four old-submission IDs stay isolated.
