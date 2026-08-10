# qiumingdll_winsplit_set_opacity(splitId, opacity)

设置指定分裂窗口的整体透明度（0 = 完全透明，255 = 完全不透明）。越界值会被自动钳制。

## 函数签名

```gml
qiumingdll_winsplit_set_opacity(splitId, opacity)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| opacity | Real | 是 | 不透明度，0 ~ 255 的整数：0 = 完全透明（看不见但仍在响应），255 = 完全不透明；小于 0 按 0 处理，大于 255 按 255 处理 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 透明度是"窗口级"的整体叠加：画面内容、标题栏等全部按同一比例透明。
- opacity = 255 时窗口恢复为普通不透明渲染，系统会自动移除分层窗口样式（性能最佳）。
- 0 < opacity < 255 时窗口进入分层（layered）渲染模式，透明混合会在系统层面完成，注意性能与混合效果因显卡/系统而异；为追求最佳观感可优先考虑 128、192 等常用值。
- 完全透明（0）的窗口依然"存在"，仍会占用槽位、仍响应鼠标等事件，只是看不见。
- 透明度与形状功能互不冲突：可以先裁形状再调透明度。

## 示例

```gml
// 在控制对象的 Step 事件中：按 [ 和 ] 渐隐/渐显 1 号分裂窗口
if (keyboard_check_pressed(vk_lbracket))
{
    global.split_alpha -= 32;   // 变透明一点
    qiumingdll_winsplit_set_opacity(global.split_1, global.split_alpha);
}

if (keyboard_check_pressed(vk_rbracket))
{
    global.split_alpha += 32;   // 变不透明一点
    qiumingdll_winsplit_set_opacity(global.split_1, global.split_alpha);
}
```

```gml
// 用鼠标滚轮实时调整透明度（在 Step 事件中）
var _wheel = mouse_wheel_up() - mouse_wheel_down();
if (_wheel != 0)
{
    global.split_alpha = clamp(global.split_alpha + _wheel * 16, 0, 255);
    qiumingdll_winsplit_set_opacity(global.split_1, global.split_alpha);
}
```

## 相关函数

- [qiumingdll_winsplit_set_topmost](qiumingdll_winsplit_set_topmost.md)
- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)