# qiumingdll_webview_set_title(webviewId, title)

设置指定 WebView 窗口标题栏中显示的文本。

## 函数签名

```gml
qiumingdll_webview_set_title(webviewId, title)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| title | String | 是 | 窗口标题文本，支持中文（内部按 UTF-8 转换）；长度以内部 512 宽字符缓冲为准，过长会被截断 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建。不依赖就绪。
- 只影响**独立窗口**（create 创建）的标题栏文字；标题栏还可能被页面自身的 `document.title` 覆盖（页面加载时 Chromium 会改写窗口标题），需要固定标题可在页面加载后用本函数重新设置，或让页面 title 保持为空。
- **子窗口没有标题栏**，调用本函数无实际显示效果（内部仍会执行，返回 1）。
- 空字符串可清除标题。
- 标题仅供显示，用作窗口标识时建议配合自身记录的 webviewId 使用。

## 示例

```gml
/// 创建事件 (obj_webview_news)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 640, 480);
qiumingdll_webview_set_title(webviewId, "新闻资讯");

/// 步进事件
// 页面就绪后重新固定标题（防止被页面 document.title 覆盖）
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !titleFixed)
{
    titleFixed = true;
    qiumingdll_webview_set_title(webviewId, "新闻资讯 - 游戏内置");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)