# qiumingdll_webview_set_topmost(webviewId, topmost)

设置指定 WebView **独立窗口**是否置顶（保持在所有窗口之上）。

## 函数签名

```gml
qiumingdll_webview_set_topmost(webviewId, topmost)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| topmost | Real | 是 | 布尔开关：1（或任意非 0 值）= 置顶，0 = 取消置顶（默认） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建（通常配合 create 创建的独立窗口使用）。
- 置顶后窗口永远显示在其他普通窗口（包括游戏主窗口）之上，适合"公告弹窗""强制提示""录像字幕"等场景。
- 取消置顶用 0 恢复普通层级。
- **对子窗口无效**：子窗口嵌入主窗口客户区，此设置没有实际意义。
- 置顶由系统保证，切换其他应用全屏时可能被系统策略限制，属正常行为。

## 示例

```gml
/// 创建事件 (obj_webview_alert)
qiumingdll_webview_init();
alertId = qiumingdll_webview_create(400, 200, 480, 260);
qiumingdll_webview_navigate_to_string(alertId,
    "<html><body style='padding:40px;text-align:center'>" +
    "<h2>系统公告</h2><p>维护将于 5 分钟后开始</p></body></html>");
isTopmost = false;

/// 步进事件
// 按 T 切换置顶状态
if (keyboard_check_pressed(ord("T")))
{
    isTopmost = !isTopmost;
    qiumingdll_webview_set_topmost(alertId, isTopmost ? 1 : 0);
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_set_draggable](qiumingdll_webview_set_draggable.md)
- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)