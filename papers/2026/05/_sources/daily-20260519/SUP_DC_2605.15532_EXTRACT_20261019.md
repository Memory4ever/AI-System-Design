# 精确DataCite响应摘录（非完整JSON）

2026-10-19实际GET `https://api.datacite.org/dois/10.48550/arxiv.2605.15532`，exit0；原字段摘录：

- id/doi: `10.48550/arxiv.2605.15532`
- titles[0].title: `DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation`
- dates: `2026-05-15T02:04:12Z` Submitted v1；`2026-05-18T00:20:23Z` Updated v1；`2026-05-19T17:39:21Z` Submitted v2；`2026-05-20T01:19:22Z` Updated v2；`2026-08-08T21:33:46Z` Submitted v3；`2026-08-11T00:47:04Z` Updated v3；Available v1 `2026-05`。
- state: `findable`；version: `3`；url: `https://arxiv.org/abs/2605.15532`
- created: `2026-05-18T01:51:32.000Z`；registered: `2026-05-18T01:51:32.000Z`；updated: `2026-08-11T04:21:29.000Z`
- relationships.client.data.id: `arxiv.content`

只用registered联官方发号规则限定v1最晚界，不把current描述或后版事件回填。
