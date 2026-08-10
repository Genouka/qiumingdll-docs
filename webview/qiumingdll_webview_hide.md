# qiumingdll_webview_hide(webviewId)

隐藏指定的 WebView 窗口（页面与脚本状态保留）。

## 函数签名

```gml
qiumingdll_webview_hide(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 隐藏成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建（create / create_child）。
- 隐藏只是让窗口不可见：页面内容、JS 状态、浏览历史全部保留，随时可用 show 恢复。
- 隐藏期间页面仍可能在后台运行（如定时器、请求）；如需完全停止请配合 stop 或导航到 about:blank 之类。
- 对独立窗口和子窗口均有效；子窗口隐藏后游戏画面相应区域不再显示页面内容。
- 隐藏不会销毁窗口，`exists(id)` 仍返回 1、`get_count()` 计数不变。

## 示例

```gml
/// 创建事件 (obj_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(50, 50, 500, 300);
isVisible = true;

/// 按键事件（键盘 H）
if (keyboard_check_pressed(ord("H")))
{
    if (isVisible)
    {
        qiumingdll_webview_hide(webviewId);
        isVisible = false;
        show_debug_message("浏览器已隐藏（页面仍保留）");
    }
    else
    {
        qiumingdll_webview_show(webviewId);
        isVisible = true;
    }
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_show](qiumingdll_webview_show.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_set_opacity](qiumingdll_webview_set_opacity.md)