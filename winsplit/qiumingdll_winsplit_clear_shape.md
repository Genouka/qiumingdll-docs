# qiumingdll_winsplit_clear_shape(splitId)

清除指定分裂窗口的形状区域，恢复为完整矩形（显示整个客户区画面）。

## 函数签名

```gml
qiumingdll_winsplit_clear_shape(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 形状清除成功（即使之前没有形状也返回 1） |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 作用是撤销任何形状设置（多边形 begin/end、椭圆、圆角矩形、位图形状），窗口恢复为完整的矩形显示。
- 清除形状不改变窗口位置、尺寸、源区域等任何其他属性。
- 重复调用安全：窗口本来就没有形状时同样是 1，不会报错。
- 已录制的"形状点缓冲"（begin_shape 后未 end 的半成品）与本函数无关，仍会自动被下一次 begin_shape 清除。

## 示例

```gml
// 在控制对象的 Step 事件中：按 X 在"圆形模式"与"矩形模式"之间切换
if (keyboard_check_pressed(ord("X")))
{
    global.round_mode = !global.round_mode;

    if (global.round_mode)
        qiumingdll_winsplit_set_shape_ellipse(global.split_1);
    else
        qiumingdll_winsplit_clear_shape(global.split_1);
}
```

## 相关函数

- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
- [qiumingdll_winsplit_set_shape_roundrect](qiumingdll_winsplit_set_shape_roundrect.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)