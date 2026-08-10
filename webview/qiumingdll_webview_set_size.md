# qiumingdll_webview_set_size(webviewId, w, h)

设置指定 WebView 窗口的客户区大小（不改变位置）。

## 函数签名

```gml
qiumingdll_webview_set_size(webviewId, w, h)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| w | Real | 是 | 客户区宽度，单位：像素（内容区域的实际宽度） |
| h | Real | 是 | 客户区高度，单位：像素 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建。不依赖 WebView 就绪。
- 传入的 w / h 指**客户区**（页面内容区）大小；独立窗口还有一个标题栏，因此实际窗口外框会略大（标题栏高度由系统决定，内部自动换算外框尺寸）。
- 子窗口没有标题栏，w / h 直接就是窗口大小。
- 页面内容会随窗口缩放重新布局（相当于浏览器窗口拉伸）。
- 只改大小不改位置：位置保持不变；需要同时设置位置和大小用 set_region。
- 尺寸为 0 或负数会使窗口不可见/异常，请传入合理正数。

## 示例

```gml
/// 创建事件 (obj_video_player)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 640, 360);

/// 步进事件
// 演示：按 1/2/3 切换画面大小
if (keyboard_check_pressed(ord("1")))
    qiumingdll_webview_set_size(webviewId, 640, 360);
else if (keyboard_check_pressed(ord("2")))
    qiumingdll_webview_set_size(webviewId, 1280, 720);
else if (keyboard_check_pressed(ord("3")))
    qiumingdll_webview_set_size(webviewId, 320, 180);

// 读取当前客户区尺寸
if (keyboard_check_pressed(ord("S")))
{
    var w = qiumingdll_webview_get_info(webviewId, 2);  // 客户区宽
    var h = qiumingdll_webview_get_info(webviewId, 3);  // 客户区高
    show_debug_message("当前客户区: " + string(w) + " x " + string(h));
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)