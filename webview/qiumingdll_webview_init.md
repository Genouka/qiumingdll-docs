# qiumingdll_webview_init()

初始化 WebView 模块：注册窗口类、加载 WebView2Loader.dll、初始化 COM 并创建 WebView2 环境，是所有 WebView 功能的第一道前置步骤。

## 函数签名

```gml
qiumingdll_webview_init()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 无 GML 参数。包装层会自动把主游戏窗口句柄 `window_handle()` 传给 DLL，用于后续创建子窗口浏览器和接收父窗口尺寸变化 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 初始化成功，可以开始调用 create / create_child 等函数 |
| 1 | 窗口类注册失败（或传入的窗口句柄无效），无法创建任何浏览器窗口 |
| 2 | 无法加载 WebView2Loader.dll（未随程序分发该 DLL，或加载入口函数失败） |
| 3 | COM 初始化失败 |
| 4 | WebView2 环境创建回调分配内存失败 |
| 5 | WebView2 环境创建失败（未安装 WebView2 Runtime，或系统版本过旧） |
| 1 | **非 Windows 平台**：GML 包装函数直接返回 1 |

## 使用说明

- 前置条件：必须在调用本模块任何其他函数（create、navigate 等）**之前**先调用本函数，且需确认返回值为 0。
- 平台限制：仅 Windows 可用。基于 Microsoft Edge WebView2 运行时，要求系统已安装 WebView2 Runtime（Win10 / Win11 一般自带，若缺失需要安装 Evergreen Standalone 运行时，或把 WebView2Loader.dll 随程序分发到 exe 同目录）。
- 本函数无参数：主窗口句柄由包装层自动获取，不需要也不能手动传入。
- 初始化成功与否决定后续所有函数是否可用；初始化失败时 create 系列函数会返回 0。
- 退出游戏前应调用 qiumingdll_webview_cleanup() 释放环境；cleanup 之后如需再次使用，需要重新调用本函数。
- 用户数据（Cookie、缓存等）保存在游戏 exe 同目录下的 WebView2Data 文件夹中。

## 示例

```gml
/// 创建事件 (obj_webview_manager)
// 游戏启动时初始化 WebView 模块
initResult = qiumingdll_webview_init();
if (initResult != 0)
{
    // 初始化失败，记录错误码并跳过 WebView 功能
    show_debug_message("WebView init failed: " + string(initResult));
    webviewEnabled = false;
}
else
{
    webviewEnabled = true;
}

/// 房间结束事件
qiumingdll_webview_cleanup();  // 游戏退出前释放全部 WebView 资源
```

## 相关函数

- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)