# Jan14 动态历史目录补核限制

混元官方 Research 使用说明要求动态目录无法提取时用浏览器核查。本次实际尝试 `cua.createBrowserTab("iab", "https://hunyuan.tencent.com/research", {visible:false})` 返回 `Browser is not available: iab`；替代 Chrome 同官方 URL 返回 `Browser is not available: chrome`。未取得页面状态，不能称浏览器已检查/没有本窗条目。既有官方原生列表仅支持该已返回切片，其最早日期晚于本窗不证明历史零命中。

定点重开：恢复可用浏览器后仅核该 Research 全部列表的本窗历史相邻项，或取得实际含 Jan13 日期邻接的官方列表/存档。不扩大机构整个仓库，当前限制不授正面历史 Coverage 或候选归属。
