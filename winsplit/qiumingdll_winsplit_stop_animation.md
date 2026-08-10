# qiumingdll_winsplit_stop_animation(splitId)

中途停止指定分裂窗口正在播放的普通动画（位置/尺寸/区域/路径动画），窗口停留在被停止时的位置。

## 函数签名

```gml
qiumingdll_winsplit_stop_animation(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（无论之前是否有动画在播放） |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 停止后窗口停留在当前插值位置，不会跳到目标值或路径终点。
- 停止的同时路径动画状态被重置（路径点不会清除，但会被 move_path_animate 重启时重新使用）。
- 只作用于普通动画；批处理动画需要用 qiumingdll_winsplit_batch_stop 单独停止。
- 动画未播放时调用也返回 1，可安全重复调用。

## 示例

```gml
// 按键事件：开始一段长移动
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 800, 600, 5000, 16);
}

// 按键事件：中途停下（停在当前中间位置）
if (keyboard_check_pressed(vk_x))
{
    qiumingdll_winsplit_stop_animation(global.splitId);
}

// Step 事件：动画结束后打印状态
if (qiumingdll_winsplit_is_animating(global.splitId) == 0)
{
    show_debug_message("动画已停止或结束");
}
```

## 相关函数

- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)