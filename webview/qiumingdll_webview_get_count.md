# qiumingdll_webview_get_count()

返回当前同时存在的（尚未销毁的）WebView 窗口数量。

## 函数签名

```gml
qiumingdll_webview_get_count()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 无参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 ~ 16 | 当前活动 WebView 的数量（独立窗口 + 子窗口合计）。销毁一个减少一个，16 是同时存在的上限 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：无需先 init（未初始化时窗口数为 0，本函数依然可安全调用）。
- 用途：判断是否还有窗口需要清理、是否接近 16 个上限（再 create 会返回 0）、调试时统计资源占用。
- 只统计"活动"窗口：销毁（destroy / destroy_all / 主窗口销毁引发的自动销毁）过的不在内。
- 注意：已经 init 但从未创建窗口时返回 0；全部销毁后也返回 0。

## 示例

```gml
/// 创建事件 (obj_webview_debug)
qiumingdll_webview_init();

/// 步进事件
// 每 60 帧刷新一次调试信息
if (frame % 60 == 0)
{
    var n = qiumingdll_webview_get_count();
    show_debug_message("当前 WebView 数量 = " + string(n) + " / 16");
}

// 演示：接近上限时不再创建新窗口
if (keyboard_check_pressed(ord("N")))
{
    if (qiumingdll_webview_get_count() >= 16)
    {
        show_debug_message("已达 16 个上限，创建失败");
    }
    else
    {
        var id = qiumingdll_webview_create(100 + irandom(800), 100 + irandom(400), 320, 240);
        show_debug_message("创建了 id = " + string(id));
    }
}

/// 房间结束事件
qiumingdll_webview_destroy_all();
show_debug_message("销毁后数量 = " + string(qiumingdll_webview_get_count()));
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_exists](qiumingdll_webview_exists.md)
- [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)