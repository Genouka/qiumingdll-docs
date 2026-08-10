# qiumingdll_winsplit_set_region(splitId, x, y, w, h)

一次性设置指定分裂窗口的位置和尺寸（合并 set_position 与 set_size 的操作）。

## 函数签名

```gml
qiumingdll_winsplit_set_region(splitId, x, y, w, h)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| x | Real | 是 | 新的窗口左上角 X，像素，屏幕坐标 |
| y | Real | 是 | 新的窗口左上角 Y，像素，屏幕坐标 |
| w | Real | 是 | 新的客户区宽度，像素，需大于 0 |
| h | Real | 是 | 新的客户区高度，像素，需大于 0 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 等价于先 `set_position(splitId, x, y)` 再 `set_size(splitId, w, h)`，且一次完成、无中间状态。
- 坐标系与单位：x/y 为屏幕像素坐标；w/h 为客户区（画面区域）像素尺寸，窗口外框会因标题栏/边框略大。
- 适合在初始化布局、或整套切换窗口摆放方案（如从"2 屏布局"切换到"4 屏布局"）时使用。
- 若该分裂窗口正在播放动画，直接调用本函数会与动画冲突，建议先停止动画。

## 示例

```gml
// 在控制对象的 Create 事件中定义两套布局，Step 事件按 Tab 切换
// 布局 1：分裂窗口占据主窗口右侧一带
if (global.layout_tab == 0)
    qiumingdll_winsplit_set_region(global.split_1, 1280, 100, 400, 300);
else
    // 布局 2：分裂窗口占据主窗口正下方
    qiumingdll_winsplit_set_region(global.split_1, 400, 900, 800, 450);
```

```gml
// 在控制对象的 Step 事件中切换布局
if (keyboard_check_pressed(vk_tab))
    global.layout_tab = !global.layout_tab;
```

## 相关函数

- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_set_size](qiumingdll_winsplit_set_size.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)