# qiumingdll_webview_execute_script(webviewId, script)

在指定 WebView 当前页面中执行一段 JavaScript 代码。

## 函数签名

```gml
qiumingdll_webview_execute_script(webviewId, script)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| script | String | 是 | 要执行的 JavaScript 源代码字符串；支持多语句与中文；注意 GML 字符串里的引号、反斜杠需要转义（内部按 UTF-8 转换后传给 Chromium） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 脚本已提交给页面执行（提交成功不代表脚本执行没有 JS 错误，脚本本身抛错不会反馈） |
| 0 | 调用失败：编号无效、WebView 不存在、尚未就绪，或脚本字符串转换失败 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 必须已创建并就绪，且**页面已加载**（最好在 navigate / navigate_to_string 之后等待片刻）；页面加载中执行脚本通常会失败或作用到半加载的页面上。
- **无返回值**：本函数不返回脚本的执行结果，只返回提交是否成功。需要在页面和游戏之间双向通信时，页面端可把数据写进 DOM（如 input 的 value、某个元素的 textContent），游戏端用 execute_script 写入或读取。
- 依赖 JavaScript 开关：`set_script_enabled(id, 1)` 需保持开启（**默认开启**），关闭后 execute_script 无效。
- 会进入页面当前 document 的全局作用域：可读取/修改全局变量、调用页面函数、触发 DOM 事件。
- 执行是异步的：返回 1 后脚本在页面线程运行，若紧接着立刻查询页面状态可能尚未生效。
- 与 DevTools 联动：开启 DevTools 后可在开发者工具 Console 中直接调试页面脚本（`set_devtools_enabled(id, 1)`，默认关闭）。

## 示例

```gml
/// 创建事件 (obj_webview_hud)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(0, 0, 640, 100);
pageReady = false;

/// 步进事件
// 1) 等待就绪并载入页面
if (!ready_started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    ready_started = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body><div id='hud'>HP: 0/0</div></body></html>");
    loadTick = 0;
}
if (ready_started && !pageReady)
{
    loadTick++;
    if (loadTick > 10)
    {
        pageReady = true;  // 简单延时等待页面渲染
    }
}

// 2) 页面就绪后，把游戏 HUD 数据注入页面
if (pageReady && hp != lastHp)
{
    lastHp = hp;
    var code = "document.getElementById('hud').textContent = 'HP: " +
               string(hp) + "/" + string(hpMax) + "';";
    qiumingdll_webview_execute_script(webviewId, code);
}

// 3) 演示读取页面内容（写入 DOM 后由下次脚本读取，或转为图片再处理）
if (keyboard_check_pressed(vk_f5))
{
    // 让页面把数据写回 DOM 的某个字段，之后可由其他途径获取
    qiumingdll_webview_execute_script(webviewId,
        "localStorage.setItem('last_ts', String(Date.now()));");
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)
- [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)