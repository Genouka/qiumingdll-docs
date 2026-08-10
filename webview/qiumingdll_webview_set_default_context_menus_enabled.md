# qiumingdll_webview_set_default_context_menus_enabled(webviewId, enabled)

开启或关闭指定 WebView 页面的默认右键菜单。

## 函数签名

```gml
qiumingdll_webview_set_default_context_menus_enabled(webviewId, enabled)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| enabled | Real | 是 | 布尔开关：1（非 0）= 显示默认右键菜单（**默认开启**），0 = 禁止默认右键菜单 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效、WebView 不存在，或尚未就绪（本函数依赖就绪） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建并就绪。
- **默认开启**。关闭后右键点击页面不再弹出浏览器的"后退/刷新/检查"等菜单。
- 注意：关闭的是**内置**菜单；页面自定义的 contextmenu 事件（页面自己实现的右键菜单）仍然有效。
- 用途：
  - 营造"客户端"感而非"浏览器"感；
  - 阻止玩家通过右键菜单打开 DevTools、查看源代码、另存图片等；
  - 防止误触打断游戏操作。
- 只影响单个 WebView。

## 示例

```gml
/// 创建事件 (obj_webview_app)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
// 禁止默认右键菜单，屏蔽浏览器操作
qiumingdll_webview_set_default_context_menus_enabled(webviewId, 0);

/// 步进事件
// 就绪后载入游戏客户端主界面
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='background:#111;color:#fff;text-align:center;padding-top:40%'>" +
        "右键菜单已被禁用<br>（C 键切换开关）</body></html>");
}

// 按 C 切换右键菜单开关（演示）
if (keyboard_check_pressed(ord("C")))
{
    ctxOn = !ctxOn;
    qiumingdll_webview_set_default_context_menus_enabled(webviewId, ctxOn ? 1 : 0);
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md)
- [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md)
- [qiumingdll_webview_set_statusbar_enabled](qiumingdll_webview_set_statusbar_enabled.md)