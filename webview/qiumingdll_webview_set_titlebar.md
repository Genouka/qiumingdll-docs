# qiumingdll_webview_set_titlebar(webviewId, hasTitleBar)

切换指定 WebView 窗口是否带有系统标题栏（用于独立窗口的"无边框"模式）。

## 函数签名

```gml
qiumingdll_webview_set_titlebar(webviewId, hasTitleBar)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| hasTitleBar | Real | 是 | 布尔开关：1（非 0）= 显示标题栏，0 = 隐藏标题栏（无边框） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功（如果状态没有变化也返回 1） |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建，主要用于 create 创建的独立窗口。
- 隐藏标题栏后窗口成为无边框"内容窗口"，配合 `set_draggable(id, 1)` 可实现自定义外观的窗口（例如游戏自绘的边框+拖动条）。
- 切换标题栏会**重建窗口样式并调整外框尺寸**：内容区大小保持不变，但窗口外框会变化；窗口位置会保持在客户区左上角对应的屏幕位置（视觉上左上角不动）。
- 无标题栏时系统菜单和关闭按钮消失，如需关闭请通过 `set_closable` + 游戏内按钮/快捷键调用 destroy，或调用 `destroy(id)` 直接销毁。
- 对子窗口无意义（子窗口恒无标题栏），调用返回 1 但无效果。

## 示例

```gml
/// 创建事件 (obj_custom_win)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(300, 150, 500, 400);
borderless = false;

// 先载入一个自绘"边框"的页面
// （就绪后）：
/// 步进事件
if (!borderless && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    borderless = true;
    // 隐藏系统标题栏，变成无边框窗口
    qiumingdll_webview_set_titlebar(webviewId, 0);
    // 允许按住窗口任意位置拖动
    qiumingdll_webview_set_draggable(webviewId, 1);
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='margin:0;background:#2b2b2b'>" +
        "<div id='bar' style='height:32px;background:#444;color:#fff;line-height:32px;text-align:center'>" +
        "自定义窗口</div></body></html>");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_title](qiumingdll_webview_set_title.md)
- [qiumingdll_webview_set_draggable](qiumingdll_webview_set_draggable.md)
- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)