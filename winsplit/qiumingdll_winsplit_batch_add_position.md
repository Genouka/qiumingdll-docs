# qiumingdll_winsplit_batch_add_position(splitId, x, y, durationMs)

在批处理录制中添加一条"位置移动"命令：播放时窗口在 durationMs 毫秒内从当前插值移动到目标位置 (x, y)。

## 函数签名

```gml
qiumingdll_winsplit_batch_add_position(splitId, x, y, durationMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| x | Real | 是 | 目标 X 坐标（屏幕坐标系，单位像素），窗口左上角要移动到的位置 |
| y | Real | 是 | 目标 Y 坐标（屏幕坐标系，单位像素） |
| durationMs | Real | 是 | 该段动画时长，单位毫秒；传 0 表示跳过过渡，命令开始时立即到位 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 命令添加成功 |
| 0 | 添加失败：splitId 无效、未在录制中、或命令数已达上限 32 条；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先 qiumingdll_winsplit_batch_begin 进入录制状态，且尚未 qiumingdll_winsplit_batch_end。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 该命令不改变窗口尺寸和源区域，只移动位置。
- 命令起始状态取"该命令开始执行时刻"的窗口状态（即上一条命令的结束状态），因此命令按顺序首尾相接。
- 缓动取添加命令时设定的批处理缓动曲线（见 qiumingdll_winsplit_batch_set_easing）。
- 每条命令快照模式与缓动，录制中途修改不影响已添加的命令。
- 播放时命令按顺序执行，整条录制最多 32 条命令。

## 示例

```gml
// 按键事件：录制"移动-等待-移动"的完整序列（本函数负责两条移动命令）
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 200, 400);  // 400ms 内移到 (400,200)
    qiumingdll_winsplit_batch_add_wait(global.splitId, 300);                // 原地等待 300ms
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 400);  // 400ms 内移到 (100,100)
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_add_wait](qiumingdll_winsplit_batch_add_wait.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)