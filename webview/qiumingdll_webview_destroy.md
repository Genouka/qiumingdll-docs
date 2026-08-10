# qiumingdll_webview_destroy(webviewId)

销毁指定的 WebView 窗口并释放其内部资源，该编号随即被释放可复用。

## 函数签名

```gml
qiumingdll_webview_destroy(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | 要销毁的 WebView 编号，取值范围 1 ~ 16，必须是 create / create_child 返回的有效编号 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 销毁成功（编号有效且窗口存在） |
| 0 | 销毁失败：编号无效（不在 1~16 范围内）、该编号当前没有活动的 WebView，或调用前未初始化 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：该 WebView 必须由 create / create_child 创建且尚未销毁。
- 只销毁**一个** WebView：destroy 之后该编号立即失效，`exists(id)` 返回 0，`get_is_active(id)` 返回 0；后续创建新窗口可能复用该编号。
- 销毁子窗口与销毁独立窗口行为一致；主窗口销毁时会自动销毁其中的子窗口，无需（也无需担心重复）手动销毁。
- 销毁操作是即时的，不需要等待；销毁后不要再对该编号调用任何其他函数（会一律返回 0 / -1）。
- 游戏结束对所有窗口统一处理时，用 destroy_all 或 cleanup 更方便。

## 示例

```gml
/// 全局的 WebView 管理对象 (obj_webview_manager)

/// 创建事件
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(600, 200, 480, 360);
webviewBusy = true;  // 用于防止重复销毁

/// 步进事件
// 若浏览器被测试模式关闭：Windows 下独立窗口的关闭已被 DLL 接管，
// 这里演示按条件主动销毁
if (keyboard_check_pressed(vk_f1) && webviewBusy)
{
    // 先关掉页面再销毁（destroy 前是否 reload/stop 均可，不影响销毁） 
    var result = qiumingdll_webview_destroy(webviewId);
    webviewBusy = false;
    show_debug_message("destroy result = " + string(result));
    // 确认销毁
    if (qiumingdll_webview_exists(webviewId) == 0)
    {
        show_debug_message("WebView 已销毁，编号已释放");
    }
}

/// 房间结束事件
qiumingdll_webview_cleanup();  // 兜底释放全部资源
```

## 相关函数

- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md)
- [qiumingdll_webview_exists](qiumingdll_webview_exists.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)