# qiumingdll_webview_destroy_all()

销毁当前存在的**所有** WebView 窗口实例（包括独立窗口和子窗口），并把全部编号释放。

## 函数签名

```gml
qiumingdll_webview_destroy_all()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 无参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 执行成功（即使当前一个 WebView 都没有也会返回 1） |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 与 cleanup 的区别：**destroy_all 只销毁窗口实例**，WebView2 环境、COM 等底层资源仍然保留，因此销毁后**可以继续**调用 create / create_child 创建新的 WebView，无需重新 init。
- 逐个等价于对每个现存编号调用 destroy。
- 场景：切换关卡 / 切换模式时清空所有浏览器窗口，但保留环境以便快速重建。
- 注意它不会释放 WebView2 环境占用的内存；游戏彻底退出前请用 cleanup 释放全部资源。

## 示例

```gml
/// 创建事件 (obj_webview_manager)
qiumingdll_webview_init();

/// 步进事件
// 演示：按 F2 清空全部浏览器窗口，随后立刻重建一个
if (keyboard_check_pressed(vk_f2))
{
    qiumingdll_webview_destroy_all();
    show_debug_message("销毁后现存 WebView 数量 = " + string(qiumingdll_webview_get_count()));

    // cleanup 不会释放环境，所以可以直接新建
    newId = qiumingdll_webview_create(300, 150, 640, 480);
    show_debug_message("新建 WebView id = " + string(newId));
}

/// 房间结束事件
// 清空所有窗口后再释放环境
qiumingdll_webview_destroy_all();
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)
- [qiumingdll_webview_get_count](qiumingdll_webview_get_count.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)