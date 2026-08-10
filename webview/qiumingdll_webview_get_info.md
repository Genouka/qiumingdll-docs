# qiumingdll_webview_get_info(webviewId, infoType)

按类型查询指定 WebView 的运行时信息（位置、尺寸、就绪状态、窗口类型）。

## 函数签名

```gml
qiumingdll_webview_get_info(webviewId, infoType)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |
| infoType | Real | 是 | 查询类型：0=窗口 X 坐标；1=窗口 Y 坐标；2=客户区宽；3=客户区高；4=是否就绪(1/0)；5=是否子窗口(1/0)；其他值无效 |

## 返回值

| 值 | 说明 |
|----|------|
| （坐标值） | infoType = 0 或 1 时：返回窗口位置。**子窗口**返回相对主窗口客户区的坐标（自动换算）；**独立窗口**返回屏幕坐标。单位：像素 |
| （尺寸值） | infoType = 2 或 3 时：返回客户区宽度 / 高度，单位：像素 |
| 1 / 0 | infoType = 4 时：1 = 内核已就绪（可 navigate / execute_script），0 = 尚未就绪 |
| 1 / 0 | infoType = 5 时：1 = 子窗口（create_child 创建），0 = 独立窗口（create 创建） |
| -1 | 查询失败：webviewId 无效 / 该编号没有活动的 WebView，或 infoType 不是 0~5 中的值 |
| -1 | 非 Windows 平台：GML 包装函数直接返回 -1 |

## 使用说明

- 前置条件：WebView 已创建（查询位置/尺寸/类型时）；infoType=4 无需就绪即可查询。
- 位置是**实时查询的真实窗口位置**，与 set_position / set_region 设置的目标值可能因系统调整（如拖动后）略有差异。
- 独立窗口的 X/Y 是屏幕坐标；子窗口的 X/Y 已自动转换为相对主窗口客户区的坐标，方便游戏内直接使用。
- infoType = 4 是判断就绪的第二种方式（与 get_is_active 等价）。
- 常用组合：2/3 读出客户区宽高后与窗口尺寸做 UI 布局逻辑；4 用于状态机等待。

## 示例

```gml
/// 创建事件 (obj_webview_layout)
qiumingdll_webview_init();
childId = qiumingdll_webview_create_child(50, 40, 400, 300);
standId = qiumingdll_webview_create(800, 200, 500, 400);

/// 步进事件
if (keyboard_check_pressed(ord("I")))
{
    // 子窗口的位置是客户区坐标
    var cx = qiumingdll_webview_get_info(childId, 0);
    var cy = qiumingdll_webview_get_info(childId, 1);
    var cw = qiumingdll_webview_get_info(childId, 2);
    var ch = qiumingdll_webview_get_info(childId, 3);
    show_debug_message("子窗口: (" + string(cx) + "," + string(cy) + ") " +
                       string(cw) + "x" + string(ch));

    // 独立窗口的是屏幕坐标
    var sx = qiumingdll_webview_get_info(standId, 0);
    show_debug_message("独立窗口屏幕 X = " + string(sx));

    // 就绪状态与类型
    if (qiumingdll_webview_get_info(childId, 4) == 1)
        show_debug_message("子窗口已就绪");
    show_debug_message("childId 是否子窗口 = " + string(qiumingdll_webview_get_info(childId, 5)));
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)
- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)