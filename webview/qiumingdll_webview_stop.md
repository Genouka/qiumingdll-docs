# qiumingdll_webview_stop(webviewId)

停止指定 WebView 当前正在进行的页面加载。

## 函数签名

```gml
qiumingdll_webview_stop(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 停止请求已提交 |
| 0 | 调用失败：编号无效、WebView 不存在，或尚未就绪 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已就绪。
- 等效于浏览器的"停止加载"（Esc）：中断当前导航请求，页面停留/保持在上一次已加载内容；若首次加载被停止，页面显示空白或错误页。
- 常见用途：用户跳过加载、加载超时保护（配合计时器）、清理网络资源。
- 停止后再启动加载：用 navigate 重新导航（reload 会对当前文档重新加载）。
- 异步执行：返回 1 只代表请求提交。

## 示例

```gml
/// 创建事件 (obj_webview_timeout)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
loadingTicks = 0;
loadStarted = false;

/// 步进事件
// 就绪后开始加载一个测试页面
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loadStarted)
{
    loadStarted = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/slow_page");
}

// 加载超时保护：超过 300 帧（5 秒）仍未确认完成则停止
if (loadStarted && loadingTicks < 900)
{
    loadingTicks++;
    if (loadingTicks == 300)
    {
        qiumingdll_webview_stop(webviewId);
        show_debug_message("加载超时，已停止");
        qiumingdll_webview_navigate_to_string(webviewId,
            "<html><body style='text-align:center;padding-top:40%'>加载超时，请重试</body></html>");
        loadingTicks = 900;  // 不再触发
    }
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md)