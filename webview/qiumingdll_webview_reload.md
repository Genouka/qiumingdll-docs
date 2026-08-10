# qiumingdll_webview_reload(webviewId)

重新加载指定 WebView 当前页面（相当于浏览器的刷新）。

## 函数签名

```gml
qiumingdll_webview_reload(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 刷新请求已提交 |
| 0 | 调用失败：编号无效、WebView 不存在，或**尚未就绪** |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已就绪（create 后先等 `get_is_active(id) == 1`）。
- 刷新当前页面：与浏览器 F5 行为一致，页面会重新加载（HTTP 缓存策略由 Chromium 决定，可能使用缓存）。
- 如果之前用 navigate_to_string 渲染的 HTML 被刷新，会重新渲染同一段 HTML。
- 刷新是异步的，返回 1 只代表请求发出；刷新完成时间取决于网络/页面复杂度。
- 页面加载被 stop 停止后想重新打开页面，用本函数（或重新 navigate）。

## 示例

```gml
/// 创建事件 (obj_webview_news)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 700, 500);

/// 步进事件
// 就绪后载入新闻页面
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/news");
}

// 按 R 刷新 / 按 S 停止加载
if (keyboard_check_pressed(ord("R")))
    qiumingdll_webview_reload(webviewId);

if (keyboard_check_pressed(ord("S")))
    qiumingdll_webview_stop(webviewId);   // 停止当前加载

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_stop](qiumingdll_webview_stop.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md)
- [qiumingdll_webview_go_forward](qiumingdll_webview_go_forward.md)