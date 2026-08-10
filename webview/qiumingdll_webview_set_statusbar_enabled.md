# qiumingdll_webview_set_statusbar_enabled(webviewId, enabled)

开启或关闭指定 WebView 页面底部的状态栏（显示链接地址、加载进度等）。

## 函数签名

```gml
qiumingdll_webview_set_statusbar_enabled(webviewId, enabled)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| enabled | Real | 是 | 布尔开关：1（非 0）= 显示状态栏，0 = 隐藏状态栏 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效、WebView 不存在，或尚未就绪（本函数依赖就绪） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建并就绪。
- **默认关闭**：create 之后状态栏不显示。
- 开启后浏览器窗口底部会出现状态栏区域（鼠标悬停链接时显示目标地址、页面加载时显示进度等），与普通浏览器体验一致。
- 默认关闭是推荐状态，状态栏会占用页面底部空间并降低"嵌入式应用"观感；如需"浏览器感"（如内置浏览器功能页）再开启。
- 只影响单个 WebView。

## 示例

```gml
/// 创建事件 (obj_webview_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(150, 100, 900, 640);

/// 步进事件
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !configured)
{
    configured = true;
    // 这个窗口对标"内置浏览器"，开启状态栏 + 右键菜单 + DevTools
    qiumingdll_webview_set_statusbar_enabled(webviewId, 1);
    qiumingdll_webview_set_default_context_menus_enabled(webviewId, 1);
    qiumingdll_webview_navigate(webviewId, "https://example.com");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md)
- [qiumingdll_webview_set_default_context_menus_enabled](qiumingdll_webview_set_default_context_menus_enabled.md)
- [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md)