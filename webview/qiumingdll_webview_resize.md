# qiumingdll_webview_resize(webviewId, x, y, w, h)

取消该 WebView 的所有自动跟随（`resize_to_parent` 与 `set_auto_resize_9patch`），并把窗口一次性缩放到自定义矩形。之后主窗口再变化也不会自动调整。

## 函数签名

```gml
qiumingdll_webview_resize(webviewId, x, y, w, h)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| x | Real | 是 | 新位置 X。子窗口为客户区坐标；独立窗口为屏幕坐标 |
| y | Real | 是 | 新位置 Y。子窗口为客户区坐标；独立窗口为屏幕坐标 |
| w | Real | 是 | 新客户区宽度（小于 1 会被钳制为 1） |
| h | Real | 是 | 新客户区高度（小于 1 会被钳制为 1） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功：已取消自动跟随并应用新矩形 |
| 0 | 调用失败：编号无效或 WebView 不存在 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 与 `set_region` 的区别：本函数会**同时取消** `resize_to_parent` / 9-patch 自动跟随，适合"退出全屏嵌入、切换到固定布局"的场景；`set_region` 不取消跟随。
- 独立窗口的 x/y 为屏幕坐标，尺寸按客户区计算（标题栏与边框自动补偿）。

## 示例

```gml
/// 从"全屏嵌入"切换到右下角固定尺寸面板
qiumingdll_webview_resize(webviewId,
    window_get_width() - 420, window_get_height() - 280,
    400, 260);
```

## 相关函数

- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_clear_resize_to_parent](qiumingdll_webview_clear_resize_to_parent.md)
- [qiumingdll_webview_set_auto_resize_9patch](qiumingdll_webview_set_auto_resize_9patch.md)
