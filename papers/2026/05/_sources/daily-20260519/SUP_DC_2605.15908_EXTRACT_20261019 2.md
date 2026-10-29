# 精确DataCite响应摘录（非完整JSON）

2026-10-19实际GET `https://api.datacite.org/dois/10.48550/arxiv.2605.15908`，返回exit0；原字段摘录：

- id/doi: `10.48550/arxiv.2605.15908`
- titles[0].title: `RaPD: Resolution-Agnostic Pixel Diffusion via Semantics-Enriched Implicit Representations`
- dates: `2026-05-15T12:45:17Z` Submitted v1；`2026-05-18T00:49:04Z` Updated v1；`2026-10-16T09:35:08Z` Submitted v2；`2026-10-19T00:51:32Z` Updated v2；Available v1 `2026-05`。
- state: `findable`；version: `2`；url: `https://arxiv.org/abs/2605.15908`
- created: `2026-05-18T02:00:25.000Z`；registered: `2026-05-18T02:00:26.000Z`；updated: `2026-10-19T02:57:01.000Z`
- relationships.client.data.id: `arxiv.content`

登记最晚界只使用registered，不把created或Updated改名为实际公开时间。description为current v2，不回填精确v1。
