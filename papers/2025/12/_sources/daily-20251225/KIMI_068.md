# Kimi CLI 0.68：执行位置与授权边界

检查时间：2026-10-02T17:52:58+08:00。作者材料，待非作者校准与证据核验。

## 身份、日期与准入

[官方 release](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.68) GitHub API 实读 `published_at=2025-12-24T12:40:22Z`，即 `2025-12-24T20:40:22+08:00`，落在 12/25 日窗。Tag `0.68` 由官方 git/ref API 解析为 commit `d5ae5b809d19086db2d823ca6f1997bd68c3db2d`。不是把 PR 合并时间当 release 首公开。

原先 CLI 直接使用本地 Shell/MCP 配置 → 本次新增客户端提供 MCP 配置、能力条件下将 Shell 替换成 ACP Terminal，并提供显式 OAuth 认证生命周期 → 执行位置和连接身份必须与模型/Agent 所在进程拆开核验。拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，实际执行与授权约束变化触发深入审阅受影响路径；不声称 RPC/OAuth 原理是本次发明。

## 精确原始证据

以下均通过官方 GitHub contents API `?ref=0.68` 实际 Base64 解码，Tag commit 已定点解析；未用当前 main 代替：

- [acp/tools.py](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/acp/tools.py#L17-L37)：`replace_tools` 仅在当前 kaos 为 local、client `terminal` 能力为真且存在 Shell 工具时替换；新 Terminal 保留原工具 name/description/schema。这说明接口身份相同也可以换执行 backend，但不是任意 remote kaos 都代理。
- 同文件 L61–92：先拒绝空 command，再 `runtime.approval.request`；获准后才经 ACP connection `create_terminal(command,session_id,output_byte_limit)`。不能把“客户端支持终端”当成已有调用授权。
- 同文件 L99–156：streaming terminal handle 通过 tool_call_id 关联；wait_for_exit 受 timeout，timeout 分支显式 kill，然后取 current_output，finally release。输出被 client 截断时加说明。此静态路径不证明任意客户端取消/kill 真的终止进程；普通 cancellation 的 finally 只有 release，不在本材料中外推为 exactly-once、rollback 或通用终止保证。
- [acp/server.py](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/acp/server.py#L64-L87)：new_session 用客户端 mcp_servers 转配置后交 KimiCLI.create，再依据 initialize 保存的 client capabilities 替换工具。L104–137 的 load_session 同样处理。返回 agent MCP capability `http=True,sse=False`，不由 converter 的 SSE 分支推出外部已协商支持 SSE。
- [acp/mcp.py](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/acp/mcp.py#L13-L46)：客户端提供的 HTTP/SSE URL/headers 或 stdio command/args/env 被转换为 FastMCP 配置，模型验证失败转 MCPConfigError。这里是客户端提供配置，连接仍由 CLI 的 FastMCP loader 建立；**不是所有 MCP 调用都在 ACP 客户端执行**。
- [mcp.py](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/mcp.py)：必要增量已从官方 PR479 files patch 读到 `_get_mcp_server(require_remote=True)`、`mcp_auth`、`mcp_reset_auth`、`mcp_test` 与 FileTokenStorage。Auth 明确要求 remote 且配置 auth=oauth；reset 清本地缓存，不证明上游服务撤销授权。
- [soul/toolset.py](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/soul/toolset.py#L245-L309)：精确正文 L210–317 已实读。token 缺失时 status 设为 unauthorized，连接任务仅为 pending 创建；`_connect_server` 自身也拒绝非 pending。OAuth server 不由此路径自动注入 runtime session 的 Mcp-Session-Id。reset 清缓存不等于远端 revoke，仍不赋予业务授权。

证据权限：公开代码支持这些静态分支、注册和调用位置；尚未本地运行 ACP/IDE、OAuth 或 cancellation 测试，不授生产安全/性能保证。本文无 benchmark 数字，hardware/precision/batch/SLO 不适用；客户端 SDK 实际终止行为未验证。

精确版本 tests 目录定点检查：相关文件只有 test_acp_convert.py、test_tool_descriptions.py、test_tool_schemas.py；实际读 test_acp_convert.py，唯一测试验证 diff display 转成 ACP FileEditToolCallContent，不验证 terminal 终止或 OAuth。未因此遍历无关测试，也不将测试存在当运行通过。

## Books 具体比较与局部提案

已实读 owner [AGENT-TOOL-CALLING](../../../../../books/part-07-agent/78-tool-calling.md) 的 `Tool Contract`、`模型输出只是 Proposal`、`同功能 Provider 的选择属于运行时路由，不属于模型授权`；相邻 Ch77 `Context 与 Memory 的状态边界`、Ch79 `Plan 不是解释文本 / 从目标到状态图`。另实读协议邻接 [AGENT-MCP](../../../../../books/part-07-agent/83-mcp.md) `MCP 不等于 Tool Authorization`。

已有实际论点：Ch78 主段“模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation”；同功能 Provider 段限定在已授权等价 Provider 集合内选择执行者、Router 不能扩大权限。Ch83 实际段“Host 负责 principal 与 policy，app/runtime 负责把 approval 放在不可逆 effect 之前”，并写 token storage、business authorization 留给实现。这些已覆盖授权不等于连接，故 OAuth 命令事实无需新增通用机制。

主线程已独立通过本窗日期、准入和 6 分，深入范围限受影响实现。按当前 ROADMAP 修正唯一 owner 为 `AGENT-MCP` / Ch83，Ch78 仅保留 effect 接口关系。重新实际顺读 Ch83 Host/Client/Server、五类契约、共享 adapter、授权段：已有正文具体覆盖 capability/version、transport lifecycle、policy/effect 分责；尚未具体解释客户端提供配置但 Agent 进程建立 MCP 连接，与客户端真正承接 terminal execution 这两种路径不能混为“客户端托管”。因此不提前裁为已有覆盖。

剩余局部差额：同一个 Tool name/schema 保留而 terminal backend 被 client capability 条件替换；连接配置来源、连接执行者与动作执行者可能不同。建议在 Ch83 `协议比较必须拆开五类契约` 的 adapter/runtime/policy 分责段之后插入以下短案例；不在 Ch78 重复新增机制。由主线程协调是否采用，作者不写 Books。

局部插入草案：

> 协议接入还要区分配置来源、连接执行者与动作执行者。客户端提供 MCP URL、headers 或 stdio command，不代表 MCP 调用已移到客户端：Kimi CLI 0.68 将这些配置转换后，仍由 CLI 建立 FastMCP 连接；另一条 ACP terminal 路径才在 local 模式且客户端声明 terminal 能力时，保留 Shell 接口而改变命令执行位置。相同 schema 只保证参数形状，不能证明工作环境和生命周期等价。该实现仍在 create_terminal 前请求原 runtime approval，并分别处理 timeout kill、输出截断与 handle release；跨进程执行增加了客户端终止行为和状态关联依赖，cancel 后 release 也不能自动证明进程停止。连接、能力协商和凭据认证均不得替代原 effect-time authorization，无法确认终止的动作须留给 runtime 的恢复或人工确认。

草案最后一句为基于实际边界的工程推断，不是作者测试结论。未主张新的通用授权机制、终止保证或性能收益。待主线程读取必要代码及局部 owner 差额后决定整合/已有覆盖；尚未声称整合完成。
