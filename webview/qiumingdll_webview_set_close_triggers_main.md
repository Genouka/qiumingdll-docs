# qiumingdll_webview_set_close_triggers_main(webviewId, triggers)

设置当用户关闭该 WebView 独立窗口时，是否连带关闭游戏主窗口。

## 函数签名

```gml
qiumingdll_webview_set_close_triggers_main(webviewId, triggers)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| triggers | Real | 是 | 布尔开关：1（非 0）= 关闭本窗口时连带发送关闭信号给游戏主窗口，0（默认）= 只关闭本窗口 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建，只对独立窗口有意义。
- 默认值：create 创建的独立窗口 **triggers = 0**（关闭浏览器不影响游戏）；设置 1 后，用户点 X 或 Alt+F4 关闭该窗口时，游戏主窗口也会收到关闭请求（相当于退出游戏）。
- 仅在用户主动关闭窗口时触发；游戏内调用 destroy / destroy_all **不会**触发连带关闭。
- 与 set_closable 的关系：closable=0 时窗口无法被用户关闭，因此也不会触发本设置；triggers=1 + closable=1 组合常用于"浏览器即主界面"的全屏窗口游戏。
- 常用于独立游戏窗口（非子窗口）作为主菜单、主界面的场景：关闭浏览器等于退出游戏。
- 对子窗口无效（子窗口不能被用户关闭）。

## 示例

```gml
/// 创建事件 (obj_main_menu_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(0, 0, 1280, 720);
qiumingdll_webview_navigate(webviewId, "file:///C:/game/menu/index.html");

// 主菜单浏览器：关闭它 = 退出游戏
qiumingdll_webview_set_closable(webviewId, 1);               // 允许关闭
qiumingdll_webview_set_close_triggers_main(webviewId, 1);    // 关闭时连带退出主程序

// 其余流程：等待就绪、旋转页面等
/// 步进事件
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !navigated)
{
    navigated = true;
    qiumingdll_webview_execute_script(webviewId, "startMenu();");  // 调用页面内函数
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)