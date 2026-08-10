# qiumingdll_winsplit_is_animating(splitId)

查询指定分裂窗口当前是否正在播放普通动画（位置/尺寸/区域/路径动画）。

## 函数签名

```gml
qiumingdll_winsplit_is_animating(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 动画正在播放中 |
| 0 | 未在播放动画；或 splitId 无效；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0（与"未在动画"无法区分）。
- 只反映普通动画状态，不反映批处理动画；批处理请用 qiumingdll_winsplit_batch_is_playing。
- 动画在时间到达 totalMs 后自动结束并归零，无需手动复位。
- 常见用法：在 Step 事件中轮询，动画结束后触发后续逻辑（例如播放下一个动作或销毁窗口）。

## 示例

```gml
// 按键事件：触发一个 2 秒的位置动画
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 600, 400, 2000, 16);
}

// Step 事件：动画结束后执行收尾逻辑（只执行一次）
if (global.move_anim_done == false && qiumingdll_winsplit_is_animating(global.splitId) == 0)
{
    global.move_anim_done = true;
    show_debug_message("移动动画已结束");
}
```

## 相关函数

- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)