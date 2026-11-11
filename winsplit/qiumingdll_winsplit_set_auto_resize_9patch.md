# qiumingdll_winsplit_set_auto_resize_9patch(splitId, mode, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)

为分屏窗口启用 9-Patch 自动跟随：先用两条参考线定义 9-Patch 网格，再用矩形对角线两坐标定义目标。主窗口尺寸变化（及移动）时按规则自动重映射。

## 函数签名

```gml
qiumingdll_winsplit_set_auto_resize_9patch(splitId, mode, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分屏窗口编号，取值范围 1 ~ 16 |
| mode | Real | 是 | 跟随方式：**0 = 窗口缩放**，**1 = 内容缩放**（两种都需要支持，见下文） |
| gridX1 | Real | 是 | 垂直参考线 1（左），设计坐标系 |
| gridY1 | Real | 是 | 水平参考线 1（上），设计坐标系 |
| gridX2 | Real | 是 | 垂直参考线 2（右），设计坐标系 |
| gridY2 | Real | 是 | 水平参考线 2（下），设计坐标系 |
| rectX1 | Real | 是 | 矩形左上角 X（设计坐标系，可越界） |
| rectY1 | Real | 是 | 矩形左上角 Y（设计坐标系，可越界） |
| rectX2 | Real | 是 | 矩形右下角 X（设计坐标系，可越界） |
| rectY2 | Real | 是 | 矩形右下角 Y（设计坐标系，可越界） |

网格与矩形共用同一个**设计坐标系**：即调用本函数那一刻的主窗口客户区大小（作为设计尺寸被记录）。要求 `0 <= gridX1 <= gridX2 <= 设计宽`、`0 <= gridY1 <= gridY2 <= 设计高`；矩形对角线坐标允许任意顺序（内部自动整理）。

## 两种跟随方式（mode）

| mode | 名称 | rect 定义的是什么 | 主窗口缩放时的行为 |
|------|------|-------------------|--------------------|
| 0 | **窗口缩放** | 分屏窗口的目标矩形（主窗口客户区坐标系） | 分屏窗口按 9-Patch 重映射位置与大小（含跟随主窗口移动）；同时源区域按客户区比例等比缩放，使分屏窗口始终显示同一块游戏内容 |
| 1 | **内容缩放** | 源区域（主窗口客户区/backbuffer 坐标系） | 分屏窗口本身**位置与尺寸保持不变**，源区域按 9-Patch 重映射——分屏窗口作为一个固定视口，窗口内显示的内容范围随主窗口缩放而变化 |

两种方式都支持，按需选择。源区域超出捕获缓冲的部分会被自动钳制。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功：已启用自动跟随并立即按定义应用一次布局 |
| 0 | 调用失败：编号无效、winsplit 未初始化、主窗口句柄无效、客户区为 0、mode 非法，或网格参考线越界/倒序 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 9-Patch 映射规则（水平轴为例）：`[0, gridX1]` 与 `[gridX2, 设计宽]` 为固定区（保持到边缘的距离），`[gridX1, gridX2]` 为拉伸区（按占比缩放）；垂直轴同理。
- 主窗口缩小到两侧固定区放不下时，自动退化为整轴等比缩放。
- 调用后会停止该窗口正在播放的普通动画与批处理动画，然后立即按当前主窗口尺寸应用一次布局。
- mode 0 时源区域基准取"启用那一刻"的源区域；主窗口缩放时按比例从基准换算。想更换基准，重新调用本函数。
- 启用后 `set_position` / `set_size` / `set_region` / `set_source_region` 的手动修改会在主窗口下一次变化时被 9-Patch 计算结果覆盖；用 `qiumingdll_winsplit_clear_auto_resize` 可随时解除跟随。
- 主窗口被 `hide_original` 移到屏幕外的兼容场景（Win7 回退路径）下，分屏窗口不会跟着主窗口移动（避免整组窗口被移到屏幕外）；Win8+ 的 DWM Cloak 隐藏不受影响。

## 示例

```gml
/// 创建分屏：显示主窗口客户区左上 1/4 画面，摆放在屏幕 (900, 80)
splitId = qiumingdll_winsplit_create(0, 0, 480, 270, 900, 80, 480, 270);

/// 模式 0（窗口缩放）：设计分辨率 960x540
/// 网格：x 96/(960-96)，y 54/(540-54)；矩形：右下角四分屏面板，随窗口缩放
qiumingdll_winsplit_set_auto_resize_9patch(
    splitId, 0,
    96, 54, 960 - 96, 540 - 54,
    640, 270, 960 - 20, 540 - 20);
```

```gml
/// 模式 1（内容缩放）：窗口固定为 320x180 的"观察窗"，
/// 源区域在主窗口缩放时按 9-Patch 重映射——
/// 四角固定区内容保持不动，中间内容范围随窗口变化
qiumingdll_winsplit_set_auto_resize_9patch(
    splitId, 1,
    120, 80, 960 - 120, 540 - 80,
    100, 80, 420, 260);
```

## 相关函数

- [qiumingdll_winsplit_clear_auto_resize](qiumingdll_winsplit_clear_auto_resize.md)
- [qiumingdll_winsplit_set_source_region](qiumingdll_winsplit_set_source_region.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_webview_set_auto_resize_9patch](../webview/qiumingdll_webview_set_auto_resize_9patch.md)
