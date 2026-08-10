# qiumingdll_winsplit_set_source_region(splitId, srcX, srcY, srcW, srcH)

修改指定分裂窗口的源区域，即分裂窗口从原游戏窗口客户区中截取的画面范围（"显示哪一块"）。

## 函数签名

```gml
qiumingdll_winsplit_set_source_region(splitId, srcX, srcY, srcW, srcH)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| srcX | Real | 是 | 源区域左上角 X，像素，相对原游戏窗口客户区（客户区左上角为 0,0） |
| srcY | Real | 是 | 源区域左上角 Y，像素，相对原游戏窗口客户区 |
| srcW | Real | 是 | 源区域宽度，像素，需大于 0 |
| srcH | Real | 是 | 源区域高度，像素，需大于 0 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 源区域是"屏幕画面地图"：分裂窗口相当于一台随游戏画面实时刷新的摄像机，本函数就是移动/缩放松动摄像机的取景框。
- 修改源区域不影响分裂窗口的位置和大小（目标区域不变）；取到的画面会被拉伸到分裂窗口客户区尺寸。
- 源区域超出原窗口客户区的部分没有画面内容，显示为空白。
- 配合动画/脚本可以实现"环视"效果：例如连续平移源区域的修改即可让分裂窗口显示游戏画面的不同部分。
- 创建时源区域由 create 的 srcX/srcY/srcW/srcH 决定；本函数可在创建后任意修改。

## 示例

```gml
// 在控制对象的 Step 事件中：用方向键控制 1 号分裂窗口的"取景框"在主窗口内环视
var _cw = window_get_width();
var _ch = window_get_height();
var _sw = 400; // 取景框宽（源区域宽）
var _sh = 225; // 取景框高

global.cam_x = clamp(global.cam_x + keyboard_check(vk_right) * 8 - keyboard_check(vk_left) * 8, 0, _cw - _sw);
global.cam_y = clamp(global.cam_y + keyboard_check(vk_down) * 8 - keyboard_check(vk_up) * 8, 0, _ch - _sh);

// 把取景框位置应用到分裂窗口
qiumingdll_winsplit_set_source_region(global.split_1, global.cam_x, global.cam_y, _sw, _sh);
```

## 相关函数

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)