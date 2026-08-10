# qiumingdll_webview_navigate_to_string(webviewId, html)

用一段 HTML 字符串直接在指定 WebView 中渲染页面（类似 `data:text/html` 的效果），无需网络和本地文件。

## 函数签名

```gml
qiumingdll_webview_navigate_to_string(webviewId, html)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| html | String | 是 | 完整的 HTML 文档字符串（可从 `<!DOCTYPE html>` 开始），支持中文与 UTF-8 编码；注意 GML 字符串中的双引号需要用转义或单引号写法处理 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | HTML 渲染请求已提交成功 |
| 0 | 调用失败：编号无效、WebView 不存在、尚未就绪，或 HTML 字符串转换为宽字符时失败 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 必须已创建并就绪（`get_is_active(id) == 1`，页面创建是异步的）。
- 与 navigate 的差异：navigate 需要真实可访问的网址；本函数把 HTML **直接作为内容**渲染，适合游戏内嵌说明页、排行榜、对话框等纯静态或纯 JS 动态页面。
- HTML 内的相对资源路径无法解析（没有真实 URL 基准），如需图片/样式尽量用 data: URI 内联或 base64 嵌入。
- HTML 字符串可以很长（内部动态分配缓冲区，无固定上限，但过长应分批/精简）。
- 渲染同样异步：调用后需要给 WebView 一点时间完成解析渲染，再执行页面脚本。
- 可用 execute_script 与渲染出的页面交互；例如用 JS 读取用户输入、更新 UI。

## 示例

```gml
/// 创建事件 (obj_webview_help)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(100, 100, 600, 400);
state = "waiting";

/// 步进事件
if (state == "waiting")
{
    // 先等 WebView 就绪
    if (qiumingdll_webview_get_info(webviewId, 4) == 1)
    {
        state = "done";
        var html = "<!DOCTYPE html><html><head><meta charset='utf-8'>" +
            "<style>body{font-family:sans-serif;background:#1e1e2e;color:#cdd6f4;padding:20px}" +
            "button{background:#89b4fa;color:#111;border:none;padding:8px 16px;cursor:pointer}</style>" +
            "</head><body><h1>游戏帮助</h1><p>这里是内嵌帮助文档。</p>" +
            "<button id='btn' onclick='count++'>点击我</button>" +
            "<p id='out'>0</p><script>var count=0;" +
            "document.getElementById('btn').onclick=function(){" +
            "document.getElementById('out').textContent=count;}</script></body></html>";
        qiumingdll_webview_navigate_to_string(webviewId, html);
    }
}

/// 步进事件（另一段循环，定时与页面脚本沟通的演示）
// 注意：execute_script 无返回值回调，这里仅演示"向页面发指令"
if (state == "done")
{
    if (keyboard_check_pressed(vk_space))
    {
        qiumingdll_webview_execute_script(webviewId,
            "document.body.style.background = '#2a2a3e';");
    }
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)