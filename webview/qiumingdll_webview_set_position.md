# qiumingdll_webview_set_position(webviewId, x, y)

设置指定 WebView 窗口的位置（不改变大小）。

## 函数签名

```gml
qiumingdll_webview_set_position(webviewId, x, y)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| x | Real | 是 | 目标 X 坐标，单位：像素。**独立窗口**：屏幕坐标系（原点在屏幕左上角）；**子窗口**：相对主窗口客户区（原点在主窗口客户区左上角） |
| y | Real | 是 | 目标 Y 坐标，单位：像素，坐标系同上 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 调用失败：编号无效或该编号没有活动的 WebView |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建。本函数不依赖 WebView 就绪（就绪与否都能移动窗口）。
- 只改位置不改大小；需要同时改位置和大小用 set_region。
- 坐标取整处理（Real 会被截断为整数像素）。
- 独立窗口：坐标是屏幕坐标，可用 `get_info(id, 0/1)` 反向读取当前屏幕位置。
- 子窗口：坐标是相对主窗口客户区的；主窗口移动时子窗口会自动跟随，因此设置后一般无需手动重设。
- 对尚在加载中的页面同样有效，移动不会打断导航。

## 示例

```gml
/// 创建事件 (obj_webview_ui)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(0, 0, 400, 300);
// 登录界面放在客户区右侧
qiumingdll_webview_set_position(webviewId, 400, 100);

/// 步进事件
// 演示：按方向键微调位置
if (keyboard_check(vk_right)) qiumingdll_webview_set_position(webviewId, pos_x + 2, pos_y);
if (keyboard_check(vk_left))  qiumingdll_webview_set_position(webviewId, pos_x - 2, pos_y);

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)