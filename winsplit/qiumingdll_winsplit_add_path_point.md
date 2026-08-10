# qiumingdll_winsplit_add_path_point(splitId, x, y)

向指定分裂窗口的路径列表累积添加一个路径点（屏幕坐标），路径点随后可通过 move_path / move_path_animate 使用。

## 函数签名

```gml
qiumingdll_winsplit_add_path_point(splitId, x, y)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| x | Real | 是 | 路径点 X 坐标（屏幕坐标系，单位像素） |
| y | Real | 是 | 路径点 Y 坐标（屏幕坐标系，单位像素） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 路径点添加成功 |
| 0 | 添加失败：splitId 无效，或路径点数量已达上限 256 个；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 路径点按调用顺序累积，每个窗口最多 256 个点，超出上限的调用返回 0 且被忽略。
- 添加路径点只记录坐标，不会移动窗口。
- 路径动画至少需要 2 个点（见 qiumingdll_winsplit_move_path_animate）；不足 2 个点时也可以只用 qiumingdll_winsplit_move_path 跳到最后一个点。
- 建议先调用 qiumingdll_winsplit_clear_path 清空旧路径再开始添加一组新点。
- 路径点坐标是"绝对屏幕坐标"，不是相对偏移。

## 示例

```gml
// 按键事件：录制一条 L 形路径（3 个点）
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_clear_path(global.splitId);
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);  // 起点
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 100);  // 水平段终点
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 300);  // 垂直段终点
    // 随后调用 qiumingdll_winsplit_move_path_animate(global.splitId, 600, 16);
}
```

## 相关函数

- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_move_path](qiumingdll_winsplit_move_path.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)