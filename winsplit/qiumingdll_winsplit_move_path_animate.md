# qiumingdll_winsplit_move_path_animate(splitId, totalMs, intervalMs)

让指定分裂窗口沿已录制的路径逐段平滑移动，动画结束后停留在路径的最后一个点。

## 函数签名

```gml
qiumingdll_winsplit_move_path_animate(splitId, totalMs, intervalMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| totalMs | Real | 是 | 沿整条路径移动的总时长，单位毫秒；时长会平均分摊到每一段（每段时长 = totalMs / (点数-1)） |
| intervalMs | Real | 是 | 刷新间隔，单位毫秒；内部会钳制到最小 1ms（传 0 或负数按 1ms 处理） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 路径动画已启动 |
| 0 | 启动失败：splitId 无效，或路径点不足 2 个；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create），并用 qiumingdll_winsplit_add_path_point 至少添加 2 个路径点。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 路径移动时窗口尺寸保持不变，只改变位置。
- 每一段都应用窗口当前的缓动曲线（见 qiumingdll_winsplit_set_easing_curve，默认 ease-in-out）；可把路径想成"多个连续的子动画"。
- 调用本函数会立即停止该窗口正在播放的普通动画，从当前位置（通常是第一个路径点所在屏幕位置）开始移动。
- 动画结束后窗口停在最后一个路径点，但路径点列表保留（需要时用 qiumingdll_winsplit_clear_path 清空）。
- 路径点坐标是绝对屏幕坐标；动画的时间基准是系统时间，不受游戏帧率影响。
- 动画期间可用 qiumingdll_winsplit_is_animating 查询状态，qiumingdll_winsplit_stop_animation 可中途停止。

## 示例

```gml
// 按键事件：录制一条折线路径并沿路径移动
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_clear_path(global.splitId);
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);  // 点 1
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 100);  // 点 2
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 300);  // 点 3
    // 总时长 600ms，2 段，每段 300ms
    qiumingdll_winsplit_move_path_animate(global.splitId, 600, 16);
}

// Step 事件：轮询动画是否结束
if (qiumingdll_winsplit_is_animating(global.splitId) == 0)
{
    show_debug_message("路径动画已结束，窗口停在最后一个点");
}
```

## 相关函数

- [qiumingdll_winsplit_add_path_point](qiumingdll_winsplit_add_path_point.md)
- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_move_path](qiumingdll_winsplit_move_path.md)
- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)