# qiumingdll_webview_set_region(webviewId, x, y, w, h)

同时设置指定 WebView 窗口的位置和大小。

## 函数签名

```gml
qiumingdll_webview_set_region(webviewId, x, y, w, h)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| x | Real | 是 | 目标 X 坐标，单位：像素。**独立窗口**为屏幕坐标；**子窗口**为相对主窗口客户区坐标 |
| y | Real | 是 | 目标 Y 坐标，单位：像素，坐标系同 x |
| w | Real | 是 | 客户区宽度，单位：像素 |
| h | Real | 是 | 客户区高度，单位：像素 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 等价于依次调用 set_position(id, x, y) 和 set_size(id, w, h)，且一次调用同时生效（无中间状态）。
- 前置条件：WebView 已创建。不依赖 WebView 就绪。
- 独立窗口的 w / h 指客户区大小，实际外框自动加上标题栏尺寸；子窗口的 w / h 直接就是窗口大小。
- 适合窗口布局的整体调整（如适配分辨率切换、弹出小窗口）。
- 尺寸请传合理正数，否则窗口可能不可见或异常。

## 示例

```gml
/// 创建事件 (obj_webview_popup)
qiumingdll_webview_init();
mainId = qiumingdll_webview_create_child(0, 0, 800, 600);
popupId = qiumingdll_webview_create(500, 300, 300, 200);
popupVisible = true;

/// 步进事件
// 演示：按 P 打开中间有动画的「小窗」，再按 P 收回到右下角
if (keyboard_check_pressed(ord("P")))
{
    if (popupVisible)
    {
        // 收起到屏幕右下角并缩小
        qiumingdll_webview_set_region(popupId, 1200, 700, 300, 200);
    }
    else
    {
        // 移到屏幕中央并放大
        qiumingdll_webview_set_region(popupId, 400, 200, 640, 480);
    }
    popupVisible = !popupVisible;
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)
- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)