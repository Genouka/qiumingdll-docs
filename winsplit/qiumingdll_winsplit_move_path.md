# qiumingdll_winsplit_move_path(splitId)

不带动画，将指定分裂窗口立即移动到当前路径的最后一个路径点，并清空路径点列表。

## 函数签名

```gml
qiumingdll_winsplit_move_path(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 跳转成功，窗口已移动到最后一点 |
| 0 | 跳转失败：splitId 无效，或路径点数量为 0（没有可跳转的点）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create），并至少用 qiumingdll_winsplit_add_path_point 添加 1 个路径点。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 本函数是"瞬移"：立即把窗口移动到路径最后一个点的位置，窗口尺寸保持不变。
- 跳转成功后路径点列表被清空（pathCount 归零）。
- 本函数不停止正在播放的普通动画；若位置动画正在播放，后续动画进度会继续覆盖窗口位置，请先调用 qiumingdll_winsplit_stop_animation 或 qiumingdll_winsplit_clear_path。
- 想要平滑移动请使用 qiumingdll_winsplit_move_path_animate。

## 示例

```gml
// 按键事件：瞬移到路径终点
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_clear_path(global.splitId);
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);
    qiumingdll_winsplit_add_path_point(global.splitId, 800, 500);
    qiumingdll_winsplit_move_path(global.splitId);  // 立即跳到 (800, 500)
}
```

## 相关函数

- [qiumingdll_winsplit_add_path_point](qiumingdll_winsplit_add_path_point.md)
- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)