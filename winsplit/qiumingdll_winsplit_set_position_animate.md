# qiumingdll_winsplit_set_position_animate(splitId, x, y, totalMs, intervalMs)

将分裂窗口从当前位置平滑移动到指定屏幕坐标，动画由内部定时器驱动，结束后停留在目标位置。

## 函数签名

```gml
qiumingdll_winsplit_set_position_animate(splitId, x, y, totalMs, intervalMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| x | Real | 是 | 目标 X 坐标（屏幕坐标系，单位像素），即窗口左上角要移动到的屏幕位置 |
| y | Real | 是 | 目标 Y 坐标（屏幕坐标系，单位像素） |
| totalMs | Real | 是 | 动画总时长，单位毫秒；传 0 时动画立即结束并跳到目标位置 |
| intervalMs | Real | 是 | 刷新间隔，单位毫秒；内部会钳制到最小 1ms（传 0 或负数按 1ms 处理） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 动画已启动 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 移动过程使用该窗口当前的缓动曲线（见 qiumingdll_winsplit_set_easing_curve，默认 ease-in-out）。
- 调用本函数会立即停止该窗口正在播放的普通动画（包括路径动画），再从"调用时刻的位置"向目标插值，而不是从目标残差继续。
- 动画期间源区域保持不变（本动画内部强制源动画模式为无）。
- 时间基准为系统时间，不是游戏帧率；intervalMs 越小动画越平滑，建议 16ms 左右。
- 动画结束时窗口停留在目标 (x, y)，可用 qiumingdll_winsplit_is_animating 轮询结束时机。

## 示例

```gml
// Create 事件：初始化并创建分裂窗口
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);

// 按键事件：800ms 内把窗口从当前位置滑到 (400, 300)，每 16ms 刷新一次
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 400, 300, 800, 16);
}
```

## 相关函数

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)