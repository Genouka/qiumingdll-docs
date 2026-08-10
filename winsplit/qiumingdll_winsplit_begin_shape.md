# qiumingdll_winsplit_begin_shape(splitId)

开始为指定的分裂窗口录制自定义多边形形状：清空该窗口的形状点缓冲，后续用 add_shape_point 依次添点、用 end_shape 生成形状。

## 函数签名

```gml
qiumingdll_winsplit_begin_shape(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 进入形状录制状态成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 必须与 `qiumingdll_winsplit_add_shape_point`、`qiumingdll_winsplit_end_shape` 成组使用，三者的 splitId 必须一致。
- 形状点缓冲是模块级共享的：同一时间只能录制一个窗口的形状。在某个窗口 begin 之后、end 之前，不要再对另一个窗口 begin（会使前者的录制作废）。
- 只是开始录制，并未改变窗口外观；真正的形状要在 `qiumingdll_winsplit_end_shape` 时才生效。
- 若中途放弃，直接不再调用任何形状函数即可（下次 begin 会自动清除旧点缓冲）。

## 示例

```gml
// 在控制对象的 Step 事件中：按 P 开始录制"东西南北四棱形"多边形形状
if (keyboard_check_pressed(ord("P")))
{
    // 开始录制 1 号分裂窗口的形状点
    qiumingdll_winsplit_begin_shape(global.split_1);
    // ……之后按顺序调用 add_shape_point 添加至少 3 个点……
}
```

## 相关函数

- [qiumingdll_winsplit_add_shape_point](qiumingdll_winsplit_add_shape_point.md)
- [qiumingdll_winsplit_end_shape](qiumingdll_winsplit_end_shape.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)
- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)