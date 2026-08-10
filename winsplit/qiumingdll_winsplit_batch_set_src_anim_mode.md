# qiumingdll_winsplit_batch_set_src_anim_mode(splitId, mode)

设置指定分裂窗口批处理录制中后续尺寸类命令（batch_add_size / batch_add_region）所使用的源动画模式。

## 函数签名

```gml
qiumingdll_winsplit_batch_set_src_anim_mode(splitId, mode)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| mode | Real | 是 | 源动画模式枚举，取值范围 0~10，与 qiumingdll_winsplit_set_src_anim_mode 共用（0=无、1=拉伸 stretch、2~10=裁剪锚点：2=左上 TL、3=上中 TC、4=右上 TR、5=左中 ML、6=正中 MC、7=右中 MR、8=左下 BL、9=下中 BC、10=右下 BR） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）；通常在 qiumingdll_winsplit_batch_begin 与 qiumingdll_winsplit_batch_end 之间调用。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 只影响后续添加的尺寸类命令：batch_add_size 与 batch_add_region；位置类（batch_add_position）和源区域类（batch_add_src_region）命令不使用该模式。
- 每条命令在添加时"快照"当时的模式，因此可在同一条录制的不同位置切换。
- 录制开始时初始值为 0（无）。
- 拉伸模式：源区域随窗口等比缩放（画面内容放大/缩小）；裁剪模式：源区域按锚点方向随窗口尺寸同步扩展/收缩。

## 示例

```gml
// 按键事件：录制"放大窗口时画面同步放大"的序列
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_set_src_anim_mode(global.splitId, 1);  // 拉伸
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 800);
    qiumingdll_winsplit_batch_set_src_anim_mode(global.splitId, 0);  // 还原为不联动
    qiumingdll_winsplit_batch_add_position(global.splitId, 200, 200, 400);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_add_region](qiumingdll_winsplit_batch_add_region.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)