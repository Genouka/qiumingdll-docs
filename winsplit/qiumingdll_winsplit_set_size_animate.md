# qiumingdll_winsplit_set_size_animate(splitId, w, h, totalMs, intervalMs)

将分裂窗口从当前尺寸平滑缩放到指定尺寸，源区域可按源动画模式联动，动画结束后停留在目标尺寸。

## 函数签名

```gml
qiumingdll_winsplit_set_size_animate(splitId, w, h, totalMs, intervalMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| w | Real | 是 | 目标宽度（客户区宽度，单位像素） |
| h | Real | 是 | 目标高度（客户区高度，单位像素） |
| totalMs | Real | 是 | 动画总时长，单位毫秒；传 0 时动画立即结束并跳到目标尺寸 |
| intervalMs | Real | 是 | 刷新间隔，单位毫秒；内部会钳制到最小 1ms（传 0 或负数按 1ms 处理） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 动画已启动 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 尺寸指窗口客户区尺寸；缩放时窗口左上角位置不变，若窗口带标题栏，外层窗口矩形会由内部自动换算调整。
- 源区域联动由窗口当前的源动画模式决定（见 qiumingdll_winsplit_set_src_anim_mode）：
  - 模式 0：源区域不动，画面被拉伸或压缩填满；
  - 模式 1（拉伸）：源区域等比缩放，画面内容同步放大/缩小；
  - 模式 2~10（裁剪）：按锚点方向扩展/收缩源区域。
- 缩放过程使用当前缓动曲线（默认 ease-in-out）。
- 调用本函数会立即停止该窗口正在播放的普通动画，再从调用时刻的尺寸向目标插值。
- 窗口位置在本动画中保持不变。
- 动画结束时停留在目标 (w, h)，可用 qiumingdll_winsplit_is_animating 轮询结束时机。

## 示例

```gml
// Create 事件：初始化、创建分裂窗口并配置"拉伸"源动画模式
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
qiumingdll_winsplit_set_src_anim_mode(global.splitId, 1);  // 源区域随窗口等比缩放

// 按键事件：1 秒内放大到 640x480（源区域同步放大）
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_size_animate(global.splitId, 640, 480, 1000, 16);
}
```

## 相关函数

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)