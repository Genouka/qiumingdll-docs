# qiumingdll_webview_set_devtools_enabled(webviewId, enabled)

开启或关闭指定 WebView 的开发者工具（F12 DevTools）支持。

## 函数签名

```gml
qiumingdll_webview_set_devtools_enabled(webviewId, enabled)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| enabled | Real | 是 | 布尔开关：1（非 0）= 开启 DevTools，0 = 关闭 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效、WebView 不存在，或**尚未就绪**（本函数依赖就绪，请先等 get_is_active 为 1） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建并**就绪**（本开关写入 WebView2 设置项，未就绪时调用返回 0）。
- **默认关闭**：create 创建后 DevTools 处于关闭状态（与脚本、右键菜单的默认开启不同）。
- 调试建议：开发阶段在就绪后立即调用本函数开启；发布版本不要开启，避免玩家打开开发者工具查看/篡改页面内容。
- 开启后，在窗口内按 F12 或右键->检查即可打开 DevTools 面板，可配合 execute_script 生成的动态内容进行调试。
- 只影响本 WebView，不影响其他窗口。

## 示例

```gml
/// 创建事件 (obj_webview_dev)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(200, 150, 800, 600);
devMode = false;   // 例如从 ini 读取: devMode = ini_read_real("config.ini", "Debug", "devtools", 0)

/// 步进事件
// 等就绪后，按配置决定是否开启 DevTools
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !configured)
{
    configured = true;
    if (devMode)
    {
        qiumingdll_webview_set_devtools_enabled(webviewId, 1);
        show_debug_message("开发模式：DevTools 已开启");
    }
    qiumingdll_webview_navigate(webviewId, "https://example.com");
}

// 运行时按 F9 临时切换
if (keyboard_check_pressed(vk_f9))
{
    devMode = !devMode;
    qiumingdll_webview_set_devtools_enabled(webviewId, devMode ? 1 : 0);
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md)
- [qiumingdll_webview_set_statusbar_enabled](qiumingdll_webview_set_statusbar_enabled.md)
- [qiumingdll_webview_set_default_context_menus_enabled](qiumingdll_webview_set_default_context_menus_enabled.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)