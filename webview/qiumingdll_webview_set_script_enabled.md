# qiumingdll_webview_set_script_enabled(webviewId, enabled)

开启或关闭指定 WebView 页面中 JavaScript 的执行能力。

## 函数签名

```gml
qiumingdll_webview_set_script_enabled(webviewId, enabled)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| enabled | Real | 是 | 布尔开关：1（非 0）= 允许执行 JavaScript（**默认开启**），0 = 禁止页面执行任何脚本 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效、WebView 不存在，或尚未就绪（本函数依赖就绪） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建并就绪（先等 get_is_active 为 1）。
- **默认开启**，正常情况下无需调用本函数。
- 关闭后：
  - 页面自身的所有 `<script>` / 内联 JS 都不执行；
  - `execute_script(id, ...)` 也无法生效（提交会失败或无效）。
- 用途：加载不受信任的第三方 HTML 内容时，可关闭脚本提高安全性（配合关闭 DevTools 和右键菜单形成"纯展示"模式）。
- 只影响单个 WebView。

## 示例

```gml
/// 创建事件 (obj_webview_unsafe)
qiumingdll_webview_init();

// 用于展示"不可信内容"的窗口：关闭脚本和右键菜单，只允许看
webviewId = qiumingdll_webview_create(200, 150, 800, 600);
hardened = false;

/// 步进事件
if (!hardened && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    hardened = true;
    // 全部关掉：脚本、右键菜单、状态栏、DevTools（DevTools 本来默认关）
    qiumingdll_webview_set_script_enabled(webviewId, 0);
    qiumingdll_webview_set_default_context_menus_enabled(webviewId, 0);
    qiumingdll_webview_set_devtools_enabled(webviewId, 0);
    qiumingdll_webview_navigate(webviewId, "file:///C:/game/readme.html");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md)
- [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md)
- [qiumingdll_webview_set_default_context_menus_enabled](qiumingdll_webview_set_default_context_menus_enabled.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)