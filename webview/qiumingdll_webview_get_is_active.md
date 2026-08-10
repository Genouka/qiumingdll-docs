# qiumingdll_webview_get_is_active(webviewId)

查询指定的 WebView 是否已创建并且**内部已就绪**（控制器创建完成，可以执行 navigate / execute_script 等操作）。

## 函数签名

```gml
qiumingdll_webview_get_is_active(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | WebView 存在且已就绪，可以进行导航、执行脚本等操作 |
| 0 | WebView 不存在（编号无效、已销毁或从未创建），或存在但**尚未就绪**（刚 create 完的常见状态） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- **这是判断"可以开始操作"的最重要函数**：create / create_child 返回后 WebView 的内核创建是异步的，只有等本函数返回 1（或 `get_info(id, 4)` 返回 1），navigate、navigate_to_string、execute_script、reload、stop、go_back、go_forward 等依赖就绪的函数才会成功，否则一律返回 0。
- 建议在 GML 步进事件中轮询本函数，就绪后一次性做完初始设置（标题、开关、首次导航）。
- 与 exists 的区别：exists 只判断"窗口是否存在"（create 后立刻为 1），本函数额外判断内核是否就绪。
- 就绪后，运行中不会退回未就绪；销毁后返回 0（与 exists 一致）。

## 示例

```gml
/// 创建事件 (obj_browser_launcher)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(150, 100, 900, 600);
started = false;

/// 步进事件
// 轮询等待就绪，就绪后一次性做完初始化
if (!started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    started = true;
    show_debug_message("WebView 就绪，开始初始化");
    qiumingdll_webview_set_devtools_enabled(webviewId, 1);
    qiumingdll_webview_set_title(webviewId, "主页");
    qiumingdll_webview_navigate(webviewId, "https://example.com");
}

// 等待期间如果页面还没就绪，尝试导航的演示（会失败，仅供教学）
if (!started)
{
    var r = qiumingdll_webview_navigate(webviewId, "https://example.com");
    if (r == 0) show_debug_message("尚未就绪，navigate 失败（预期行为）");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)
- [qiumingdll_webview_exists](qiumingdll_webview_exists.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)