# Daily 2026-09-20 closure locators

## MiMo MCP connection lifetime

- [`b6dbd25818c168ed152bd4d11e7f1ff0fe40d180`](https://github.com/XiaomiMiMo/MiMo-Code/commit/b6dbd25818c168ed152bd4d11e7f1ff0fe40d180)：Atom `2026-09-19T18:57:29Z`。完整 message/diff 显示 host MCP connection refresh/retirement、snapshot binding、fallback retry 与 OAuth probe close。它实现 owner revision、reference drain 与 stale-attempt isolation，没有新增长期 protocol、替代分支或评价边界。

## MiMo session orphan reclaim

- [`895ae523309d0454e022f01c894c844094bc7cf1`](https://github.com/XiaomiMiMo/MiMo-Code/commit/895ae523309d0454e022f01c894c844094bc7cf1)：Atom `2026-09-19T21:05:24Z`。完整 message/diff 显示 abandon threshold、busy/retry/live-owner guard、directory-scoped transaction 与 race tests。它实现 lease/age gate、scoped re-check 与 idempotent settlement，没有长期机制或评价增量。
- `7b14718946f540c24c754d17d3e4b337714d87fa` 的 stale `Running`/lost-wake 修复为同一 session/actor path 的支持活动，不改变关闭判断。

## MiMo failure persistence

- [`4768aab0d0b5056e51b82801935cfce018be148a`](https://github.com/XiaomiMiMo/MiMo-Code/commit/4768aab0d0b5056e51b82801935cfce018be148a)：Atom `2026-09-20T00:35:18Z`，commit `2026-09-20T08:35:18+08:00`。session prompt 的 MCP SDK exception handling diff 把异常经统一 `errorMessage` 路径规范化并截断，配有长异常 persistence regression。bounded durable error 是既有卫生不变量，没有新边界推导、跨实现协议或评价结果。

三项精确 commit 页面在检查时可用，所查 main 历史未见直接 revert/withdrawal 信号。它们是三个不同的 Source Family：MCP connection、session orphan state 与 failure persistence 没有共同问题或修订链，不能仅凭宽泛 lifecycle/robustness 术语合并。这里完成的是贡献关闭所需的身份、日期、完整题名/核心说明、核心 diff 与状态轻查，不是 Evidence 审阅，不支持 benchmark、生产就绪或普适设计结论。
