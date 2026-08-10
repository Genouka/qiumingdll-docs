# qiumingdll_winsplit_clear_path(splitId)

停止指定分裂窗口正在播放的动画，并清空其所有已添加的路径点。

## 函数签名

```gml
qiumingdll_winsplit_clear_path(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 清理成功 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 本函数会停止该窗口当前正在播放的普通动画（位置/尺寸/区域/路径动画），并且清空路径点列表。
- 窗口停留在动画被停止时的中间位置，不会跳到目标或路径终点。
- 在重新录制一组路径点之前调用本函数，可以避免旧路径点残留。
- 不影响批处理动画的播放状态。

## 示例

```gml
// 按键事件：重置路径并重新录制
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_clear_path(global.splitId);   // 清空旧路径（并停止可能的路径动画）
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 100);
    qiumingdll_winsplit_move_path_animate(global.splitId, 600, 16);
}
```

## 相关函数

- [qiumingdll_winsplit_add_path_point](qiumingdll_winsplit_add_path_point.md)
- [qiumingdll_winsplit_move_path](qiumingdll_winsplit_move_path.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)