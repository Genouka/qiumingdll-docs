# qiumingdll_webview_go_forward(webviewId)

让指定 WebView 前进到浏览历史中的下一个页面（相当于浏览器的前进按钮）。

## 函数签名

```gml
qiumingdll_webview_go_forward(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 前进请求已提交（不保证发生了历史前进） |
| 0 | 调用失败：编号无效、WebView 不存在，或尚未就绪 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已就绪。
- **依赖浏览历史**：必须先"后退"过（或存在后续历史记录），前进才有内容可走；从未后退时调用返回 1 但页面不变。
- 典型的"前进"场景：用户后退查看旧页面后，又想回到后退前的页面。
- 历史是每个 WebView 各自维护的。
- 与 go_back / reload 配合实现完整浏览工具栏。
- 异步执行：返回 1 只代表请求已发出。

## 示例

```gml
/// 创建事件 (obj_browser_toolbar)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(200, 150, 800, 600);
loaded = false;

/// 步进事件
// 就绪后演示一段"多页面浏览"流程：
// 页面 A -> 页面 B -> 后退 -> 前进
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/page_a");
    step_phase = 0;
}

switch (step_phase)
{
case 0:  // 60 帧后切到页面 B
    phase_tick++;
    if (phase_tick >= 60)
    {
        qiumingdll_webview_navigate(webviewId, "https://example.com/page_b");
        step_phase = 1;
        phase_tick = 0;
    }
    break;
case 1:  // 再过 60 帧后退
    phase_tick++;
    if (phase_tick >= 60)
    {
        qiumingdll_webview_go_back(webviewId);      // 回到页面 A
        step_phase = 2;
        phase_tick = 0;
    }
    break;
case 2:  // 再过 60 帧前进
    phase_tick++;
    if (phase_tick >= 60)
    {
        qiumingdll_webview_go_forward(webviewId);   // 回到页面 B
        step_phase = 3;
    }
    break;
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md)
- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)