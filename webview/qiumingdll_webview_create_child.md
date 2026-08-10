# qiumingdll_webview_create_child(x, y, w, h)

在游戏主窗口的客户区内创建一个嵌入式的子窗口浏览器（无标题栏），返回该 WebView 的编号。

## 函数签名

```gml
qiumingdll_webview_create_child(x, y, w, h)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| x | Real | 是 | 子窗口左上角相对**主窗口客户区**的 X 坐标（客户区坐标系，原点在主窗口客户区左上角，左上偏移为负值也可），单位：像素 |
| y | Real | 是 | 子窗口左上角相对主窗口客户区的 Y 坐标，单位：像素 |
| w | Real | 是 | 子窗口客户区宽度，单位：像素 |
| h | Real | 是 | 子窗口客户区高度，单位：像素 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 ~ 16 | 创建成功，返回 webviewId（从 1 开始分配，可复用） |
| 0 | 创建失败。可能原因：尚未 init、初始化失败、主窗口句柄无效、WebView 数量已达上限 16 个、系统资源不足 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：必须先调用 qiumingdll_webview_init() 且返回 0；子窗口会嵌入 init 时记录的主游戏窗口客户区内。
- 平台限制：仅 Windows；依赖已安装的 WebView2 Runtime。
- 与 create 的差别：子窗口**没有标题栏**，因此：
  - 不可通过系统菜单关闭（closable 固定为 false），只能由游戏调用 destroy / destroy_all 销毁；
  - 不置顶（topmost 无实际效果）；
  - 不可拖动（draggable 恒为 false，set_draggable 对其无效）；
  - 移动、缩放跟随游戏主窗口：主窗口移动时子窗口自动跟随；主窗口被销毁时子窗口也会自动销毁。
- 坐标始终相对主窗口客户区：create_child / set_position / set_region 传入的 x、y 都是客户区坐标；`get_info(id, 0/1)` 查询到的位置也会换算成客户区坐标。
- 页面加载同样异步：create 后需等待 `get_is_active(id) == 1`（或 `get_info(id, 4) == 1`）再调用 navigate 等函数。
- 想让子窗口自动铺满游戏客户区并随窗口大小变化自动调整，可调用 `resize_to_parent(id)`。

## 示例

```gml
/// 创建事件 (obj_ingame_browser)
qiumingdll_webview_init();  // 假设返回 0

// 在游戏画面内嵌一个浏览器，先占 400x300
webviewId = qiumingdll_webview_create_child(40, 200, 400, 300);
if (webviewId > 0)
{
    qiumingdll_webview_set_title(webviewId, "");  // 子窗口无标题栏，此调用无实际效果
    state = "waiting";
}

/// 步进事件
if (state == "waiting" && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    state = "loaded";
    // 用 HTML 字符串直接渲染一个本地页面
    qiumingdll_webview_navigate_to_string(webviewId, "<h1>你好，WebView</h1><p>这是嵌入游戏窗口内的浏览器。</p>");
    // 铺满整个游戏客户区并随窗口尺寸变化自动调整
    qiumingdll_webview_resize_to_parent(webviewId);
}

/// 按键事件 (键盘 ESC)
if (keyboard_check_pressed(vk_escape))
{
    qiumingdll_webview_hide(webviewId);       // 隐藏浏览器（不销毁，可再次 show）
}

/// 房间结束事件
qiumingdll_webview_destroy_all();   // 主窗口销毁时会自动清理，这里显式销毁更保险
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_init](qiumingdll_webview_init.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)
- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)