# qiumingdll_webview_cleanup()

销毁所有 WebView 窗口并**释放整个 WebView 环境**（包括 WebView2 Environment、加载的 DLL、COM 等全部底层资源）。

## 函数签名

```gml
qiumingdll_webview_cleanup()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 无参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 清理执行成功 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 在游戏退出（房间结束 / 游戏结束 / 关闭主窗口）前调用，避免残留浏览器进程占用资源。
- **清理后模块回到未初始化状态**：如果想再次使用 WebView 功能，必须重新调用 qiumingdll_webview_init()。
- 与 destroy_all 的对比：
  - destroy_all：只销毁窗口实例，环境保留，可继续直接创建新窗口；
  - cleanup：销毁窗口 **并释放环境**，之后必须重新 init 才能再用。
- 内部流程：先销毁全部窗口 → 解除对主窗口消息的接管 → 释放 WebView2 环境 → 卸载 DLL → 反初始化 COM。
- 重复调用 cleanup 是安全的（后续调用相当于空操作）。
- 子窗口无需单独销毁：主窗口销毁时会自动销毁。

## 示例

```gml
/// 创建事件 (obj_webview_manager)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 640, 480);

/// 房间结束事件（游戏即将退出）
if (qiumingdll_webview_cleanup() == 1)
{
    show_debug_message("WebView 环境已全部释放");
}

/// 游戏结束事件（兜底，防止异常退出路径漏掉）
qiumingdll_webview_cleanup();  // 重复调用安全
```

## 相关函数

- [qiumingdll_webview_init](qiumingdll_webview_init.md)
- [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)