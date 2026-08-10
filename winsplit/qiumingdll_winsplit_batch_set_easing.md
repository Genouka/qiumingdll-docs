# qiumingdll_winsplit_batch_set_easing(splitId, easing)

设置指定分裂窗口批处理录制中后续命令（batch_add_*）所使用的缓动曲线。

## 函数签名

```gml
qiumingdll_winsplit_batch_set_easing(splitId, easing)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| easing | Real | 是 | 缓动曲线枚举，取值范围 0~11，与 qiumingdll_winsplit_set_easing_curve 共用同一套枚举（0=linear、1=ease-in、2=ease-out、3=ease-in-out、4=in-cubic、5=out-cubic、6=in-out-cubic、7=in-back、8=out-back、9=in-out-back、10=bounce-out、11=elastic-out） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）；通常在 qiumingdll_winsplit_batch_begin 与 qiumingdll_winsplit_batch_end 之间调用。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 每条 batch_add_* 命令在添加时"快照"当时的缓动曲线，因此可以在同一条录制的不同位置切换不同缓动，实现"前段匀速、后段弹跳"之类的组合效果。
- 不在录制中调用也可以修改当前缓动，但不会影响已添加的命令。
- 录制开始时初始值为该窗口普通动画的当前曲线（默认 ease-in-out），通常无需额外设置。

## 示例

```gml
// 按键事件：录制一条前慢后弹的入场动画序列
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_set_easing(global.splitId, 1);    // ease-in，缓慢起步
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 600);
    qiumingdll_winsplit_batch_set_easing(global.splitId, 10);   // bounce-out，弹跳收尾
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 600);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)