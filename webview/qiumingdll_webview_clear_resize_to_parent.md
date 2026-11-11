# qiumingdll_webview_clear_resize_to_parent(webviewId)

取消 `qiumingdll_webview_resize_to_parent` 设置的"自动铺满主窗口客户区"效果。取消后子窗口保持当前位置与尺寸，主窗口再被拉伸/缩放时不再自动跟随。

## 函数签名

```gml
qiumingdll_webview_clear_resize_to_parent(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（即使该 WebView 从未启用过自动铺满，也会返回 1，本函数幂等） |
| 0 | 调用失败：编号无效或 WebView 不存在 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 仅影响 `resize_to_parent` 的跟随标志，**不会改变**子窗口当前的位置和大小。
- 若之后想以自定义矩形继续自动跟随，请使用 `qiumingdll_webview_set_auto_resize_9patch`。
- 若想一次性"取消跟随 + 移动到指定矩形"，可直接调用 `qiumingdll_webview_resize`。
- cleanup / 主窗口销毁时跟随能力会被自动解除，无需手动调用本函数。

## 示例

```gml
/// 玩家按 ESC 退出"全屏嵌入"模式，改为固定小窗口
if (fullscreen_mode && keyboard_check_pressed(vk_escape))
{
    qiumingdll_webview_clear_resize_to_parent(webviewId);
    qiumingdll_webview_set_region(webviewId, 40, 40, 480, 320);
    fullscreen_mode = false;
}
```

## 相关函数

- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
- [qiumingdll_webview_resize](qiumingdll_webview_resize.md)
- [qiumingdll_webview_set_auto_resize_9patch](qiumingdll_webview_set_auto_resize_9patch.md)
