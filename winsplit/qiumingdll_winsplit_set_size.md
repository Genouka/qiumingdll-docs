# qiumingdll_winsplit_set_size(splitId, w, h)

改变指定分裂窗口的显示尺寸：只改变大小，不改变位置、源区域和其他属性。

## 函数签名

```gml
qiumingdll_winsplit_set_size(splitId, w, h)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| w | Real | 是 | 新的客户区宽度，像素，需大于 0；窗口外框总宽会在此基础上加上边框（含标题栏时） |
| h | Real | 是 | 新的客户区高度，像素，需大于 0；窗口外框总高会在此基础上加上边框（含标题栏时） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- w/h 指分裂窗口客户区（画面显示区域）的尺寸；创建时 dstW/dstH 是同样的含义。窗口实际外框因标题栏和边框的存在会比 w/h 略大。
- 改变大小后，源区域内容会被拉伸适配新的客户区尺寸（拉伸模式为默认缩放，窗口内容不裁剪）。
- 位置（左上角）保持不变，即窗口向右下方向扩展/收缩。
- 若该分裂窗口正在播放尺寸动画，直接调用本函数会与动画冲突，建议先停止动画。

## 示例

```gml
// 在控制对象的 Step 事件中：按 = 放大 1 号分裂窗口到 960x540，按 - 缩小回 640x360
if (keyboard_check_pressed(vk_add) || keyboard_check_pressed(vk_equals))
    qiumingdll_winsplit_set_size(global.split_1, 960, 540);

if (keyboard_check_pressed(vk_subtract) || keyboard_check_pressed(vk_minus))
    qiumingdll_winsplit_set_size(global.split_1, 640, 360);
```

## 相关函数

- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)