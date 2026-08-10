# qiumingdll_webview_end_shape(webviewId)

结束 WebView 窗口的不规则形状编辑，使之前通过 `qiumingdll_webview_set_region` 设置的形状区域生效。

## 函数签名

```gml
qiumingdll_webview_end_shape(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号（1 ~ 16），由 `qiumingdll_webview_create` / `qiumingdll_webview_create_child` 返回 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 形状区域设置成功并已应用 |
| 0 | 失败。可能原因：webviewId 无效、尚未设置区域、非 Windows 平台或未初始化 |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_webview_init()`；必须先调用 `qiumingdll_webview_set_region(webviewId, ...)` 再调用本函数。
- 平台限制：仅 Windows。
- 行为细节：`set_region` 负责描述形状，本函数结束编辑并提交形状，使窗口按设定的区域显示。
- 注意：结束形状后如需更换形状，重新调用 `set_region` 与 `end_shape` 即可；调用 `hide` / `show` 不会丢失已应用的形状。

## 示例

```gml
// 将浏览器窗口裁剪为不规则形状
qiumingdll_webview_set_region(webviewId, ...);
qiumingdll_webview_end_shape(webviewId);
```

## 相关函数

- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)