# qiumingdll_winsplit_add_shape_point(splitId, x, y)

在 begin_shape 与 end_shape 之间，向当前正在录制的多边形形状添加一个顶点。

## 函数签名

```gml
qiumingdll_winsplit_add_shape_point(splitId, x, y)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须与本组 begin_shape 的 splitId 一致 |
| x | Real | 是 | 顶点 X，像素，相对分裂窗口客户区左上角（0,0），通常取 0 ~ 客户区宽度 |
| y | Real | 是 | 顶点 Y，像素，相对分裂窗口客户区左上角（0,0），通常取 0 ~ 客户区高度 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 顶点添加成功 |
| 0 | 失败：splitId 无效、本窗口不在形状录制状态（没有 begin_shape）、或顶点数已达上限 256；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：对同一个 splitId 先调用了 `qiumingdll_winsplit_begin_shape`，且尚未调用 `end_shape`。
- 顶点坐标是分裂窗口客户区内的像素坐标，与源区域无关。超出窗口尺寸的坐标仍会被记录，但对应的窗口部分不会显示有效形状。
- 至少需要 3 个顶点（end_shape 才能成功），最多 256 个顶点；超出上限的添加会被拒绝并返回 0。
- 顶点按添加顺序连接成封闭多边形（Windows 多边形区域默认按奇偶（ALTERNATE）填充规则处理自交部分）。
- 添加的是"折线顶点"，引擎会自动首尾相连封闭图形，不需要手动重复第一个点。

## 示例

```gml
// 在控制对象的 Step 事件中：按 F 把 1 号分裂窗口裁成六边形（顶点坐标相对其客户区）
if (keyboard_check_pressed(ord("F")))
{
    var _w = 640; // 假设分裂窗口客户区为 640x360
    var _h = 360;

    qiumingdll_winsplit_begin_shape(global.split_1);

    qiumingdll_winsplit_add_shape_point(global.split_1, _w * 0.5, 0);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w, _h * 0.25);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w, _h * 0.75);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w * 0.5, _h);
    qiumingdll_winsplit_add_shape_point(global.split_1, 0, _h * 0.75);
    qiumingdll_winsplit_add_shape_point(global.split_1, 0, _h * 0.25);

    if (qiumingdll_winsplit_end_shape(global.split_1) == 1)
        show_debug_message("六边形形状已应用");
}
```

## 相关函数

- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_end_shape](qiumingdll_winsplit_end_shape.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)