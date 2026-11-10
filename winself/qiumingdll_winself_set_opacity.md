# qiumingdll_winself_set_opacity(opacity)

设置游戏自身窗口的整体透明度（0 = 完全透明，255 = 完全不透明）。越界值会被自动钳制。

## 函数签名

```gml
qiumingdll_winself_set_opacity(opacity)
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| opacity | Real | 是 | 不透明度，0 ~ 255 的整数：0 = 完全透明（看不见但仍在响应），255 = 完全不透明；小于 0 按 0 处理，大于 255 按 255 处理 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：窗口句柄无效；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：在 Windows 平台下、游戏窗口已存在时调用。函数内部自动使用 `window_handle()` 作为目标窗口。
- 透明度是"窗口级"的整体叠加：画面内容、标题栏等全部按同一比例透明。
- opacity = 255 时窗口恢复为普通不透明渲染，系统会自动移除分层窗口样式（性能最佳）。
- 0 < opacity < 255 时窗口进入分层（layered）渲染模式，透明混合在系统层面完成；性能与混合效果因显卡/系统而异。
- 完全透明（0）的窗口依然"存在"，仍会响应鼠标等事件，只是看不见。
- 透明度与形状功能互不冲突：可以先裁形状再调透明度。

## 示例

```gml
// 用鼠标滚轮实时调整游戏窗口透明度（在 Step 事件中）
var _wheel = mouse_wheel_up() - mouse_wheel_down();
if (_wheel != 0)
{
    global.game_alpha = clamp(global.game_alpha + _wheel * 16, 0, 255);
    qiumingdll_winself_set_opacity(global.game_alpha);
}
```

```gml
// 按 [ 和 ] 渐隐/渐显整个游戏窗口
if (keyboard_check_pressed(vk_lbracket))
{
    global.game_alpha = max(global.game_alpha - 32, 0);
    qiumingdll_winself_set_opacity(global.game_alpha);
}
if (keyboard_check_pressed(vk_rbracket))
{
    global.game_alpha = min(global.game_alpha + 32, 255);
    qiumingdll_winself_set_opacity(global.game_alpha);
}
```

## 相关函数

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
