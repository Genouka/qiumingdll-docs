# qiumingdll_webview_set_auto_resize_9patch(webviewId, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)

让**子窗口** WebView 按 9-Patch 规则自动跟随主窗口缩放：先以两条参考线定义 9-Patch 网格，再用矩形对角线两坐标定义子窗口的位置与大小。主窗口尺寸变化时，矩形按 9-Patch 规则重映射并自动应用。

## 函数签名

```gml
qiumingdll_webview_set_auto_resize_9patch(webviewId, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| webviewId | Real | 是 | WebView 编号（必须是 create_child 创建的子窗口） |
| gridX1 | Real | 是 | 垂直参考线 1（左），设计坐标系；`[0, gridX1]` 为固定区 |
| gridY1 | Real | 是 | 水平参考线 1（上），设计坐标系；`[0, gridY1]` 为固定区 |
| gridX2 | Real | 是 | 垂直参考线 2（右），设计坐标系；`[gridX2, 设计宽]` 为固定区 |
| gridY2 | Real | 是 | 水平参考线 2（下），设计坐标系；`[gridY2, 设计高]` 为固定区 |
| rectX1 | Real | 是 | 窗口矩形左上角 X（设计坐标系，可越界） |
| rectY1 | Real | 是 | 窗口矩形左上角 Y（设计坐标系，可越界） |
| rectX2 | Real | 是 | 窗口矩形右下角 X（设计坐标系，可越界） |
| rectY2 | Real | 是 | 窗口矩形右下角 Y（设计坐标系，可越界） |

网格与矩形共用同一个**设计坐标系**：即调用本函数那一刻的主窗口客户区大小（作为设计尺寸被记录）。要求 `0 <= gridX1 <= gridX2 <= 设计宽`、`0 <= gridY1 <= gridY2 <= 设计高`，矩形对角线坐标允许任意顺序（内部会自动整理）。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功：已启用自动跟随并立即按定义应用一次布局 |
| 0 | 调用失败：编号无效、不是子窗口、主窗口句柄无效、客户区为 0，或网格参考线越界/倒序 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 9-Patch 映射规则（以水平轴为例）：
  - `[0, gridX1]` 与 `[gridX2, 设计宽]` 两段是**固定区**：位于其中的矩形边缘保持到左/右边缘的距离不变；
  - `[gridX1, gridX2]` 是**拉伸区**：其中的矩形边缘按拉伸区占比缩放。
  - 垂直轴同理。
- 典型用法：`grid` 设为"中间大片可拉伸、四周留边固定"，再把 rect 设成"除边距外铺满"即可实现带边距的自适应布局；把 rect 塞进固定区即可做出"固定在角落的小窗"。
- 主窗口缩小到两侧固定区放不下时，自动退化为整轴等比缩放。
- 与 `resize_to_parent` 互斥：调用本函数会先关闭 `resize_to_parent`；调用 `resize_to_parent` 也会关闭本跟随。
- 调用时会立即按当前主窗口尺寸应用一次布局（当前尺寸 == 设计尺寸时即按 rect 原值摆放）。
- 本函数记录的 rect 是布局基准；启用后想改变基准布局，重新调用本函数即可。`set_position` / `set_size` / `set_region` 不会更新基准，主窗口下一次变化时会回到 9-Patch 计算结果；`qiumingdll_webview_resize` 则会取消跟随。
- cleanup / 主窗口销毁时自动解除。

## 示例

```gml
/// 创建事件：初始化并创建子窗口
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(0, 0, 800, 480);

/// 步进事件：就绪后启用 9-Patch 跟随
if (!started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    started = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com");

    // 设计分辨率 800x480（当前客户区）：
    // 网格参考线 x: 64 / (800-64)，y: 48 / (480-48)
    // 矩形：留出 16px 边距铺满（rect 在拉伸区内，随窗口缩放）
    qiumingdll_webview_set_auto_resize_9patch(
        webviewId,
        64, 48, 800 - 64, 480 - 48,
        16, 16, 800 - 16, 480 - 16);
}
```

```gml
/// 固定在左下角的 200x120 小窗：矩形完全落在左侧固定区（x < gridX1），
/// y 方向落在底部固定区（y > gridY2），窗口缩放时它纹丝不动
qiumingdll_webview_set_auto_resize_9patch(
    webviewId,
    300, 200, 800 - 300, 480 - 200,
    10, 480 - 130, 210, 480 - 10);
```

## 相关函数

- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
- [qiumingdll_webview_clear_resize_to_parent](qiumingdll_webview_clear_resize_to_parent.md)
- [qiumingdll_webview_resize](qiumingdll_webview_resize.md)
- [qiumingdll_winsplit_set_auto_resize_9patch](../winsplit/qiumingdll_winsplit_set_auto_resize_9patch.md)
