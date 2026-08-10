# qiumingdll_webview_create(x, y, w, h)

创建一个独立的浏览器窗口（带系统标题栏，可移动、可关闭），返回该窗口的 webviewId。

## 函数签名

```gml
qiumingdll_webview_create(x, y, w, h)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| x | Real | 是 | 窗口左上角的屏幕坐标 X，单位：像素（屏幕坐标系，原点在屏幕左上角） |
| y | Real | 是 | 窗口左上角的屏幕坐标 Y，单位：像素 |
| w | Real | 是 | 窗口客户区宽度，单位：像素（`w` 和 `h` 指内容区大小，实际窗口会额外包含标题栏区域） |
| h | Real | 是 | 窗口客户区高度，单位：像素 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 ~ 16 | 创建成功，返回该 WebView 的编号（webviewId），从 1 开始分配；全部销毁后编号会被复用 |
| 0 | 创建失败。可能原因：尚未调用 qiumingdll_webview_init()、初始化失败、同时存在的 WebView 已满 16 个、系统资源不足 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：必须先调用 qiumingdll_webview_init() 且返回 0。
- 平台限制：仅 Windows；依赖已安装的 WebView2 Runtime（Win10 / Win11 一般自带）。
- 最多同时存在 **16 个** WebView；超过上限时 create 返回 0。
- 本函数创建的是**独立顶层窗口**，自带标题栏、系统菜单和关闭按钮：
  - 默认可关闭（可用 `set_closable(id, 0)` 禁用关闭）。
  - 默认关闭后动作是关闭自身 **不**影响主游戏窗口，可通过 `set_close_triggers_main(id, 1)` 改为连带关闭主窗口。
  - 默认不可拖动，可通过 `set_draggable(id, 1)` 开启"按住窗口任意位置拖动"。
- **页面加载是异步的**：create 返回后 WebView 内部尚未就绪，此时调用 navigate / execute_script / reload 等会返回 0 失败。请用 `get_is_active(id)`（返回 1 = 已就绪）或 `get_info(id, 4)` 轮询就绪后再操作。
- 新窗口默认显示（CreateWindowEx 自带 WS_VISIBLE），也可配合 show / hide 控制。
- 该函数创建的窗口在游戏中关闭时，wm_close 由 DLL 处理，不需要 GML 侧处理关闭事件。
- 主窗口销毁时**独立**窗口不会自动销毁，请在游戏结束前用 destroy / destroy_all / cleanup 清理。

## 示例

```gml
/// 创建事件 (obj_browser_manager)
if (qiumingdll_webview_init() != 0)
{
    exit;  // 初始化失败，本对象不再运行
}

// 创建 800x600 的独立浏览器窗口，位于屏幕中央偏左
webviewId = qiumingdll_webview_create(200, 100, 800, 600);
if (webviewId == 0)
{
    show_debug_message("创建 WebView 失败");
    exit;
}

// 设置标题并等待就绪后打开网址
qiumingdll_webview_set_title(webviewId, "游戏内置浏览器");
state = "waiting_ready";

/// 步进事件
if (state == "waiting_ready")
{
    if (qiumingdll_webview_get_is_active(webviewId) == 1)
    {
        state = "waiting_ready_done";
        qiumingdll_webview_navigate(webviewId, "https://example.com");
    }
}
else
{
    // 页面加载完成后可以开始执行脚本等操作
    if (qiumingdll_webview_get_info(webviewId, 4) == 1)
    {
        // 例如在页面里修改标题文字
        qiumingdll_webview_execute_script(webviewId, "document.body.style.background='#222'");
    }
}

/// 房间结束事件
qiumingdll_webview_destroy(webviewId);  // 游戏结束前销毁该窗口
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_init](qiumingdll_webview_init.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)