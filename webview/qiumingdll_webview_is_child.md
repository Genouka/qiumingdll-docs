# qiumingdll_webview_is_child(webviewId)

查询指定的 WebView 是子窗口（create_child 创建）还是独立窗口（create 创建）。

## 函数签名

```gml
qiumingdll_webview_is_child(webviewId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 该编号是子窗口浏览器（create_child 创建，嵌入主窗口客户区） |
| 0 | 该编号是独立窗口（create 创建） |
| 0 | 该编号不存在（无效、未创建或已销毁）——与独立窗口一样返回 0，请配合 exists 区分 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 前置条件：WebView 已创建（未创建时返回 0）。
- 判断"单个窗口"类型的最直接函数；`get_info(id, 5)` 提供同样的信息。
- react 依据：
  - 子窗口：位置坐标是客户区坐标、不可拖动/关闭/置顶、主窗口销毁时自动销毁、可用 resize_to_parent；
  - 独立窗口：屏幕坐标、可拖动/关闭/置顶、需显式销毁。
- 适合在统一管理多窗口的结构化逻辑里区分处理。

## 示例

```gml
/// 创建事件 (obj_webview_manager)
qiumingdll_webview_init();
widgets[0] = qiumingdll_webview_create_child(20, 20, 300, 200);  // 游戏内 UI
widgets[1] = qiumingdll_webview_create(600, 150, 400, 300);      // 独立弹窗

/// 步进事件
// 统一遍历所有窗口，按类型执行不同逻辑
for (var i = 0; i < 2; i++)
{
    var id = widgets[i];
    if (qiumingdll_webview_is_child(id) == 1)
    {
        // 子窗口：检查客户区坐标是否越界
        var x = qiumingdll_webview_get_info(id, 0);
        if (x < 0) qiumingdll_webview_set_position(id, 0, 20);
    }
    else
    {
        // 独立窗口：保证置顶状态符合需求
        qiumingdll_webview_set_topmost(id, 1);
    }
}

/// 房间结束事件
qiumingdll_webview_cleanup();
```

## 相关函数

- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)
- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)