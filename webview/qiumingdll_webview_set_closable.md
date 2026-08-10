# qiumingdll_webview_set_closable(webviewId, closable)

控制指定的 WebView 独立窗口是否允许被用户关闭（通过标题栏关闭按钮 / Alt+F4）。

## 函数签名

```gml
qiumingdll_webview_set_closable(webviewId, closable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| closable | Real | 是 | 布尔开关：1（非 0）= 允许用户关闭（默认），0 = 禁止用户关闭 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建，主要作用于独立窗口（create 创建）。
- 关闭的两种途径：
  - 系统菜单/标题栏的 X 按钮：`closable=0` 时会被禁用（系统菜单该项置灰）并拦截 WM_CLOSE；
  - `destroy(id)` / `destroy_all()`：**不受本设置影响**，游戏内总是可以销毁。
- `closable=0` 时 Alt+F4 也无效（防止误关窗口/游戏）。
- 对子窗口无意义：子窗口恒不可由用户关闭，只能由游戏销毁。
- 与 set_close_triggers_main 配合使用：closable=1 时用户关闭窗口是否连带关闭游戏主窗口，由 close_triggers_main 决定。

## 示例

```gml
/// 创建事件 (obj_webview_lock)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(400, 200, 480, 320);
qiumingdll_webview_navigate(webviewId, "https://example.com");

// 默认可关闭；按 L 之后锁死，禁止用户点 X 关闭
locked = false;

/// 步进事件
if (keyboard_check_pressed(ord("L")))
{
    locked = !locked;
    qiumingdll_webview_set_closable(webviewId, locked ? 0 : 1);
    show_debug_message(locked ? "窗口已锁定（不可关闭）" : "窗口已解锁");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_close_triggers_main](qiumingdll_webview_set_close_triggers_main.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md)