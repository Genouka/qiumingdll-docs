# qiumingdll_webview_clear_auto_resize_9patch(webviewId)

取消 `qiumingdll_webview_set_auto_resize_9patch` 设置的 9-Patch 自动跟随。取消后子窗口保持当前位置与尺寸，主窗口再被缩放时不再自动调整。

## 函数签名

```gml
qiumingdll_webview_clear_auto_resize_9patch(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（即使该 WebView 从未启用 9-Patch 跟随，也返回 1，本函数幂等） |
| 0 | 调用失败：编号无效或 WebView 不存在 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 仅清除 9-Patch 跟随标志，不会改变窗口当前的位置与大小。
- 与 `qiumingdll_webview_clear_resize_to_parent` 的区别：后者只取消"铺满客户区"的跟随；本函数只取消 9-Patch 跟随。两者互斥，同一时刻最多只有一个生效。
- 取消后可随时重新调用 `qiumingdll_webview_set_auto_resize_9patch` 建立新的布局基准。
- 若想"取消跟随并立即移动/缩放到指定矩形"，直接用 `qiumingdll_webview_resize`。

## 示例

```gml
/// 退出自适应布局，固定在当前位置
qiumingdll_webview_clear_auto_resize_9patch(webviewId);
```

## 相关函数

- [qiumingdll_webview_set_auto_resize_9patch](qiumingdll_webview_set_auto_resize_9patch.md)
- [qiumingdll_webview_resize](qiumingdll_webview_resize.md)
- [qiumingdll_webview_clear_resize_to_parent](qiumingdll_webview_clear_resize_to_parent.md)
