# qiumingdll_winsplit_set_region_animate(splitId, x, y, w, h, totalMs, intervalMs)

将分裂窗口从当前位置与尺寸平滑移动到目标位置与尺寸（位置+尺寸组合动画），动画结束后停留在目标状态。

## 函数签名

```gml
qiumingdll_winsplit_set_region_animate(splitId, x, y, w, h, totalMs, intervalMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| x | Real | 是 | 目标 X 坐标（屏幕坐标系，单位像素），窗口左上角目标位置 |
| y | Real | 是 | 目标 Y 坐标（屏幕坐标系，单位像素） |
| w | Real | 是 | 目标宽度（客户区宽度，单位像素） |
| h | Real | 是 | 目标高度（客户区高度，单位像素） |
| totalMs | Real | 是 | 动画总时长，单位毫秒；传 0 时动画立即结束并跳到目标区域 |
| intervalMs | Real | 是 | 刷新间隔，单位毫秒；内部会钳制到最小 1ms（传 0 或负数按 1ms 处理） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 动画已启动 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 位置与尺寸在整个动画过程中同步插值，等效于 set_position_animate 与 set_size_animate 的合并，但只占用一个动画状态，不会互相覆盖。
- 源区域联动由窗口当前的源动画模式决定（见 qiumingdll_winsplit_set_src_anim_mode）：模式 1 等比拉伸、模式 2~10 按锚点裁剪。
- 插值使用当前缓动曲线（默认 ease-in-out）。
- 调用本函数会立即停止该窗口正在播放的普通动画，再从调用时刻的状态向目标插值。
- 动画结束时停留在目标 (x, y, w, h)，可用 qiumingdll_winsplit_is_animating 轮询结束时机。

## 示例

```gml
// Create 事件：初始化并创建分裂窗口
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);

// 按键事件：1.2 秒内从 (100,100,320x240) 平滑移动到 (50,50,800x600)
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_region_animate(global.splitId, 50, 50, 800, 600, 1200, 16);
}
```

## 相关函数

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)