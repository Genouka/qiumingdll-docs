# qiumingdll_winsplit_set_src_anim_mode(splitId, mode)

设置指定分裂窗口在尺寸/区域动画期间源区域（主窗口上的截图区域）的联动方式：保持不变、等比拉伸或按锚点裁剪。

## 函数签名

```gml
qiumingdll_winsplit_set_src_anim_mode(splitId, mode)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| mode | Real | 是 | 源动画模式枚举，取值范围 0~10，含义见下表 |

源动画模式枚举（与 `qiumingdll_winsplit_batch_set_src_anim_mode` 共用）：

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | 无 | 源区域保持不变（默认值） |
| 1 | 拉伸 stretch | 源区域随窗口等比缩放：源坐标与源尺寸按"目标尺寸 / 当前尺寸"的比例缩放 |
| 2 | 裁剪-左上 TL | 锚点固定在左上角，源区域向右下扩展/收缩 |
| 3 | 裁剪-上中 TC | 锚点固定在上边中点，向左右、向下扩展 |
| 4 | 裁剪-右上 TR | 锚点固定在右上角，向左下扩展/收缩 |
| 5 | 裁剪-左中 ML | 锚点固定在左边中点，向右、上下扩展 |
| 6 | 裁剪-正中 MC | 锚点固定在中心，向四周对称扩展 |
| 7 | 裁剪-右中 MR | 锚点固定在右边中点，向左、上下扩展 |
| 8 | 裁剪-左下 BL | 锚点固定在左下角，向右上扩展/收缩 |
| 9 | 裁剪-下中 BC | 锚点固定在下边中点，向上、左右扩展 |
| 10 | 裁剪-右下 BR | 锚点固定在右下角，向左上扩展/收缩 |

裁剪（crop）模式含义：窗口尺寸变化量记为 dW / dH 时，源区域尺寸同步变化相同量（源宽 = 原源宽 + dW，源高 = 原源高 + dH），锚点决定扩展/收缩的方向。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 只影响"尺寸"类动画：set_size_animate、set_region_animate；对纯位置动画无效（set_position_animate 内部会强制使用模式 0）。
- 默认模式为 0（源区域不动）。
- 该设置是持久状态，动画开始前设置一次即可。
- crop 模式以动画开始时刻的源区域为基准插值，起始源区域请先用 qiumingdll_winsplit_set_source_region 设定。

## 示例

```gml
// Create 事件：创建分裂窗口，并启用"拉伸"源动画模式
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
if (global.splitId > 0)
{
    // 拉伸模式：窗口变大时源区域等比放大，相当于画面同步放大
    qiumingdll_winsplit_set_src_anim_mode(global.splitId, 1);
}

// 按键事件：放大窗口到全屏，源区域同步拉伸放大
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_size_animate(global.splitId, 640, 480, 1000, 16);
}
```

## 相关函数

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)