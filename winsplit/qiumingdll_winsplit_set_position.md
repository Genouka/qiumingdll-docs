# qiumingdll_winsplit_set_position(splitId, x, y)

移动指定的分裂窗口到屏幕上的新位置：只改变位置，不改变大小、源区域和其他属性。

## 函数签名

```gml
qiumingdll_winsplit_set_position(splitId, x, y)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| x | Real | 是 | 新的窗口左上角 X，像素，屏幕坐标（主显示器左上角为 0,0）；可为负值或超出屏幕范围 |
| y | Real | 是 | 新的窗口左上角 Y，像素，屏幕坐标；可为负值或超出屏幕范围 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 坐标系：x/y 为屏幕像素坐标（物理显示器坐标），与 GameMaker 的 display 坐标一致；不是游戏窗口客户区坐标。
- 移动的是窗口外框的左上角（含标题栏时包含标题栏），因此画面（客户区）实际位置随之整体平移。
- 移动是立即生效的瞬时操作；若需要平滑移动请看动画相关函数。
- 若该分裂窗口正在播放位置动画，直接调用本函数会与动画冲突，建议先停止动画再移动。

## 示例

```gml
// 在控制对象的 Step 事件中：按 1/2/3 把 1 号分裂窗口移动到屏幕不同的预览位置
if (keyboard_check_pressed(ord("1")))
    qiumingdll_winsplit_set_position(global.split_1, 50, 50);

if (keyboard_check_pressed(ord("2")))
    qiumingdll_winsplit_set_position(global.split_1, 800, 50);

if (keyboard_check_pressed(ord("3")))
    qiumingdll_winsplit_set_position(global.split_1, 800, 500);
```

## 相关函数

- [qiumingdll_winsplit_set_size](qiumingdll_winsplit_set_size.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_set_draggable](qiumingdll_winsplit_set_draggable.md)