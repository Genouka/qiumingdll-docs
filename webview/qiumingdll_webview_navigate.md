# qiumingdll_webview_navigate(webviewId, url)

让指定的 WebView 导航到给定的网址，异步加载网页。

## 函数签名

```gml
qiumingdll_webview_navigate(webviewId, url)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| url | String | 是 | 要打开的网址，**必须带协议前缀**，例如 `"https://example.com"`、`"http://127.0.0.1:8080/page"`、`"file:///C:/..."`；缺少协议（如 `"example.com"`）将无法正确解析 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 导航请求已提交成功（注意：页面是否真的加载完成需另行观察，DLL 不提供加载完成通知） |
| 0 | 调用失败：编号无效、该 WebView 不存在、或 WebView 尚未就绪（create 后立即调用最容易遇到） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：该 WebView 必须已创建并**就绪**。页面创建是异步的，create / create_child 返回后必须等待 `get_is_active(id) == 1`（或 `get_info(id, 4) == 1`）才能成功调用 navigate，否则返回 0。
- URL 长度上限约 2000 字符（内部固定缓冲区）。
- URL 支持中文等非 ASCII 字符（内部按 UTF-8 转换）。
- 导航是异步的：返回 1 只代表请求已发出，网页加载完成与否、成功与否都**没有**回调可以获知；需要时可用脚本轮询页面状态，例如 `execute_script(id, "document.readyState")`（注意不返回结果）或定期用 `get_info(id, 4)` 判断 WebView 就绪。
- 页面加载完成后才能可靠调用 execute_script 操作 DOM；过早执行会因页面尚未加载而失效。
- 反复 navigate 会替换当前页面，并写入新的浏览历史（go_back / go_forward 可用）。

## 示例

```gml
/// 创建事件 (obj_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
state = "waiting";

/// 步进事件
switch (state)
{
case "waiting":
    // 等待 WebView 就绪
    if (qiumingdll_webview_get_is_active(webviewId) == 1)
    {
        state = "navigating";
        var ok = qiumingdll_webview_navigate(webviewId, "https://example.com");
        show_debug_message("navigate 提交结果 = " + string(ok));
        tick = 0;
    }
    break;

case "navigating":
    // 简单起见用时间等待页面加载（真实项目可结合 execute_script 轮询）
    tick++;
    if (tick > 120)
    {
        state = "loaded";
        // 页面加载后执行脚本
        qiumingdll_webview_execute_script(webviewId,
            "document.title = '已加载'; document.body.style.background = '#333';");
    }
    break;
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md)
- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_stop](qiumingdll_webview_stop.md)