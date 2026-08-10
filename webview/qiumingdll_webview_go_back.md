# qiumingdll_webview_go_back(webviewId)

让指定 WebView 后退到浏览历史中的上一个页面（相当于浏览器的后退按钮）。

## 函数签名

```gml
qiumingdll_webview_go_back(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 后退请求已提交（注意：不保证确实发生了历史回退） |
| 0 | 调用失败：编号无效、WebView 不存在，或尚未就绪 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已就绪。
- **依赖浏览历史**：只有当前 WebView 内部存在"上一个页面"（例如 navigate 过多次，或页面内点击了链接跳转）时后退才有实际效果；没有历史时调用返回 1 但页面不变。
- 历史是每个 WebView 各自维护的，与游戏其他窗口无关。
- navigate_to_string 渲染的内容也会计入历史。
- 前进/后退与刷新组合使用可实现完整的"工具栏"逻辑（配合 go_forward 一起做）。
- 异步执行：返回 1 只代表请求已发出。

## 示例

```gml
/// 创建事件 (obj_webview_wiki)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);

/// 步进事件
// 就绪后打开第一个页面
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/page1");
}

// 浏览器风格的后退/前进按钮
if (keyboard_check_pressed(vk_left))   // 左箭头 = 后退
    qiumingdll_webview_go_back(webviewId);

if (keyboard_check_pressed(vk_right))  // 右箭头 = 前进
    qiumingdll_webview_go_forward(webviewId);

if (keyboard_check_pressed(vk_f5))     // F5 = 刷新
    qiumingdll_webview_reload(webviewId);

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_go_forward](qiumingdll_webview_go_forward.md)
- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)