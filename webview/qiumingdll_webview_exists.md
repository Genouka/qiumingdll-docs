# qiumingdll_webview_exists(webviewId)

查询指定的 webviewId 当前是否对应一个活动的（尚未销毁的）WebView 窗口。

## 函数签名

```gml
qiumingdll_webview_exists(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 该编号存在活动的 WebView 窗口 |
| 0 | 不存在：编号无效（不在 1~16 范围内）、从未创建、已销毁 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 只判断"窗口是否创建且未销毁"，**不**判断内核是否就绪；判断就绪用 get_is_active 或 get_info(id, 4)。
- create 返回后本函数立即为 1（早于内核就绪）。
- 用途：调用其余函数前校验 id 是否还合法（destroy 后再操作会得到 0 / -1，先 exists 校验更清晰）、管理多窗口列表时排查悬空 id。
- 子窗口随主窗口销毁后，本函数也会返回 0。

## 示例

```gml
/// 创建事件 (obj_webview_keeper)
qiumingdll_webview_init();
idA = qiumingdll_webview_create(100, 100, 400, 300);
idB = qiumingdll_webview_create_child(20, 20, 300, 200);
idC = 99;  // 无效编号示例

/// 步进事件
// 按 D 销毁 idA，然后检查各编号状态
if (keyboard_check_pressed(ord("D")))
{
    qiumingdll_webview_destroy(idA);
    show_debug_message("idA 存在? " + string(qiumingdll_webview_exists(idA)));
    show_debug_message("idB 存在? " + string(qiumingdll_webview_exists(idB)) + " 就绪? " +
                       string(qiumingdll_webview_get_is_active(idB)));
    show_debug_message("idC 存在? " + string(qiumingdll_webview_exists(idC)));
}

// 演示：调用前校验，避免对已销毁的 id 操作
if (keyboard_check_pressed(ord("X")))
{
    if (qiumingdll_webview_exists(idA))
    {
        qiumingdll_webview_hide(idA);
    }
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_get_count](qiumingdll_webview_get_count.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)