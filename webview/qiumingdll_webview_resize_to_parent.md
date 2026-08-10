# qiumingdll_webview_resize_to_parent(webviewId)

让指定的**子窗口**浏览器自动铺满游戏主窗口的整个客户区，并在主窗口尺寸变化时自动跟随。

## 函数签名

```gml
qiumingdll_webview_resize_to_parent(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16（必须是 create_child 创建的子窗口） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功：子窗口已铺满主窗口客户区，并启用了主窗口尺寸变化时的自动跟随 |
| 0 | 调用失败：编号无效、WebView 不存在、**不是子窗口**（独立窗口调用无效），或主窗口句柄无效 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- **仅子窗口有效**：create_child 创建的窗口才能调用；create 创建的独立窗口调用返回 0。
- 调用后子窗口的位置被重置为 (0, 0)（客户区左上角），宽高铺满整个主窗口客户区。
- **自动跟随**：启用后主窗口被拉伸/缩放时（含用户调整窗口大小、分辨率变化），子窗口会自动重新铺满客户区，无需在 GML 侧处理 resize 事件。
- 这项跟随能力在 cleanup / 主窗口销毁时自动解除，无需手动关闭。
- 适合"全屏嵌入式页面"：游戏画面就是浏览器页面，主窗口大小时窗口自动全屏。
- 若之后又需要手动控制位置大小，请在布局改变前先调用 set_position / set_region / set_size（这些调用不会取消自动跟随，之后主窗口再变化仍会铺满）。

## 示例

```gml
/// 创建事件 (obj_fullscreen_browser)
qiumingdll_webview_init();
if (qiumingdll_webview_create_child(0, 0, 320, 240) > 0)
{
    webviewId = qiumingdll_webview_create_child(0, 0, 320, 240);
    started = false;
}

/// 步进事件
// 就绪后铺满整个游戏窗口并载入页面
if (!started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    started = true;
    qiumingdll_webview_resize_to_parent(webviewId);   // 全屏嵌入，自动跟随窗口缩放
    qiumingdll_webview_navigate(webviewId, "https://example.com");
    // 游戏窗口被玩家拉伸时，页面自动跟着缩放，无需额外代码
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)