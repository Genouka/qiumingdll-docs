# qiumingdll_winsplit_set_stretch_mode(mode)

设置分裂窗口画面与窗口尺寸不一致时的 GDI 拉伸模式（仅影响缩放渲染时的画质，全局设置）。

## 函数签名

```gml
qiumingdll_winsplit_set_stretch_mode(mode)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| mode | Real | 是 | 拉伸模式，取值范围 0~1，含义见下表 |

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | COLORONCOLOR | 快速拉伸（默认值）。性能更好，但放大时边缘可能产生锯齿 |
| 1 | HALFTONE | 高质量拉伸。画面平滑，但性能开销更高 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：建议在 qiumingdll_winsplit_init 之后、创建分裂窗口之前调用（全局设置，时刻调用均有效）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 本函数仍然有效（不是弃用 API）：当分裂窗口源区域尺寸与窗口客户区尺寸不一致（即发生 StretchBlt 缩放）时，决定缩放使用的 GDI 拉伸算法。
- 全局设置，影响所有分裂窗口。
- 注意：负值会被钳制为 0；除 1 之外的任意值都按 0（COLORONCOLOR）处理。
- 源区域尺寸与窗口尺寸一致时不会发生缩放，本设置不起作用。

## 示例

```gml
// Create 事件：启用高质量拉伸并创建分裂窗口
qiumingdll_winsplit_init();
qiumingdll_winsplit_set_stretch_mode(1);  // HALFTONE 高质量拉伸

// 源区域 320x240，窗口 640x480，画面放大显示时使用平滑拉伸
global.splitId = qiumingdll_winsplit_create(0, 0, 320, 240, 100, 100, 640, 480);
```

## 相关函数

- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md)（已弃用）
- [qiumingdll_winsplit_set_render_during_drag](qiumingdll_winsplit_set_render_during_drag.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)