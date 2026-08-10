# qiumingdll_webview_show(webviewId)

显示指定的 WebView 窗口（取消隐藏状态）。

## 函数签名

```gml
qiumingdll_webview_show(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 显示成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建（create / create_child）。
- 与 hide 成对使用：hide 后调用本函数可将窗口重新显示出来，页面内容和 JS 状态**不会丢失**（隐藏只是不可见而已）。
- 新创建的窗口默认就是显示的；仅当之前调用过 hide（或以其他方式隐藏）时才需要用 show 恢复。
- 对独立窗口、子窗口均有效。
- 显示/隐藏只影响可见性，不影响页面加载与脚本执行（隐藏期间页面照常在后台运行，也可被 navigate）。

## 示例

```gml
/// 创建事件 (obj_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(200, 100, 640, 480);
qiumingdll_webview_navigate(webviewId, "https://example.com");
visible = true;

/// 按键事件（键盘 F1）
if (keyboard_check_pressed(vk_f1))
{
    if (visible)
    {
        qiumingdll_webview_hide(webviewId);   // 隐藏浏览器
        visible = false;
    }
    else
    {
        qiumingdll_webview_show(webviewId);   // 再次显示，页面仍在
        visible = true;
    }
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_hide](qiumingdll_webview_hide.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)