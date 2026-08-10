# qiumingdll_webview_set_draggable(webviewId, draggable)

设置指定的 WebView 窗口是否可以通过按住窗口内容区域拖动窗口。

## 函数签名

```gml
qiumingdll_webview_set_draggable(webviewId, draggable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| draggable | Real | 是 | 布尔开关：1（非 0）= 按住窗口任意位置可拖动窗口，0（默认）= 只能通过标题栏拖动（默认关闭） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建，主要为独立窗口设计。
- 开启后：鼠标按住窗口内**任意位置**（包括页面内容区）即可拖动整个窗口，方便无边框窗口的移动控制。
- 与 set_titlebar(id, 0) 组合：实现"无边框 + 全窗可拖"的自绘窗口体验。
- 注意：开启后页面内需要"按下拖拽"的交互（如画布拖拽、滑块、文本选择）可能与窗口拖动冲突，请按实际需求取舍，或让页面元素拦截（页面内可加 `-webkit-app-region: no-drag` 思路的 CSS 元素）。
- 对子窗口无效（子窗口随主窗口移动，不可单独拖动）。

## 示例

```gml
/// 创建事件 (obj_webview_borderless)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(200, 200, 600, 400);

// 无边框 + 任意位置可拖动
qiumingdll_webview_set_titlebar(webviewId, 0);
qiumingdll_webview_set_draggable(webviewId, 1);

// 就绪后载入自定义界面
/// 步进事件
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='margin:0;background:#20242c;color:#fff;user-select:none'>" +
        "<div style='padding:24px;text-align:center'>按住我拖动窗口</div>" +
        "</body></html>");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md)
- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)