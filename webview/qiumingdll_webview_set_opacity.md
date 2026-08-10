# qiumingdll_webview_set_opacity(webviewId, opacity)

设置指定 WebView 窗口的整体透明度。

## 函数签名

```gml
qiumingdll_webview_set_opacity(webviewId, opacity)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| opacity | Real | 是 | 透明度值，取值范围 0 ~ 255：0 = 完全透明（不可见），255 = 完全不透明（默认）。超出范围的值会被自动钳制到 0 ~ 255（小数会被截断为整数） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建。不依赖就绪。
- 透明度作用于**整个窗口**（含标题栏和全部页面内容），动画效果需在 GML 步进事件里逐步修改数值实现。
- 设为 255 时内部会移除分层属性（恢复普通窗口，性能最好）；设为小于 255 时启用分层窗口（WS_EX_LAYERED）。
- 设为 0 时窗口完全透明但**仍然存在**（会拦截鼠标、接收输入），请与 hide 区分：需要彻底不显示且不接收输入时用 hide。
- 半透明窗口在上层页面内仍会正常渲染与交互，适合做"幽灵提示""预览浮层"。

## 示例

```gml
/// 创建事件 (obj_webview_ghost)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(300, 200, 400, 300);
qiumingdll_webview_navigate(webviewId, "https://example.com");
fading = false;
alphaNow = 255;

/// 步进事件
// 按 G 开始淡入淡出循环
if (keyboard_check_pressed(ord("G"))) fading = true;

if (fading)
{
    alphaNow += 3 * choose_alpha_dir;  // 演示简化：直接线性变化
    // 更稳妥的写法：记录方向变量，到达边界反转
    if (alphaNow > 255) { alphaNow = 255; fading = false; }
    qiumingdll_webview_set_opacity(webviewId, alphaNow);
}

// 用 choose_alpha_dir 之前先声明
/// 创建事件补充
choose_alpha_dir = 1;

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_hide](qiumingdll_webview_hide.md)
- [qiumingdll_webview_show](qiumingdll_webview_show.md)
- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)