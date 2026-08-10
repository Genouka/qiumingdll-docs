# qiumingdll_webview_set_zoom_factor(webviewId, zoomFactor)

设置指定 WebView 页面的缩放比例（Zoom）。

## 函数签名

```gml
qiumingdll_webview_set_zoom_factor(webviewId, zoomFactor)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| zoomFactor | Real | 是 | 页面缩放倍数，**1.0 = 100%** 正常大小；0.5 = 缩小到 50%，2.0 = 放大到 200%。建议使用正数（0 或负数页面会不可见）。实际允许范围由 WebView2 决定（约 0.25 ~ 5.0 之间），超出会被系统钳制 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效、WebView 不存在，或控制器尚未创建（请先等就绪） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建且控制器已就绪（等 `get_is_active(id) == 1`）。
- 缩放作用于页面渲染（相当于浏览器 Ctrl+滚轮缩放），不影响窗口尺寸。
- 生效时机：设置后立即对当前页面内容生效，包括缩放后重新加载的页面。
- 布局影响：放大后页面可视范围变小（相当于固定窗口内看到的内容更多/更少），因此常与窗口尺寸配合调整。
- 合法范围：WebView2 支持约 0.25 ~ 5.0 之间的值；建议传 0.5 ~ 2.0 之间的常用档位。

## 示例

```gml
/// 创建事件 (obj_webview_read)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
zoom = 1.0;

/// 步进事件
// 就绪后载入长文档
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='max-width:720px;margin:auto;padding:24px;font-size:16px'>" +
        "<h1>章节一</h1>" + string_repeat("<p>正文段落……</p>", 40) +
        "</body></html>");
}

// 缩放控制：+ / - 调整，R 复位
if (keyboard_check_pressed(vk_add) || keyboard_check_pressed(vk_numpadadd))
{
    zoom = min(2.0, zoom + 0.25);
    qiumingdll_webview_set_zoom_factor(webviewId, zoom);
}
if (keyboard_check_pressed(vk_subtract) || keyboard_check_pressed(vk_numpadsub))
{
    zoom = max(0.5, zoom - 0.25);
    qiumingdll_webview_set_zoom_factor(webviewId, zoom);
}
if (keyboard_check_pressed(ord("R")))
{
    zoom = 1.0;
    qiumingdll_webview_set_zoom_factor(webviewId, 1.0);
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)