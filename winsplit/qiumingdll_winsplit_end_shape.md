# qiumingdll_winsplit_end_shape(splitId)

结束形状录制并把已收集的多边形顶点应用到分裂窗口：窗口立即变为该多边形的形状，多边形之外的区域不再显示。

## 函数签名

```gml
qiumingdll_winsplit_end_shape(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须与本组 begin_shape 的 splitId 一致 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 形状应用成功，分裂窗口已呈现多边形外观 |
| 0 | 失败：splitId 无效、本窗口不在形状录制状态，或顶点数不足 3 个（此时本轮录制的点被丢弃）；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：对同一个 splitId 先调用了 `qiumingdll_winsplit_begin_shape`，并添加了至少 3 个顶点。
- 顶点少于 3 个时不会形成多边形，本函数返回 0 并清空本轮缓冲。
- 应用后窗口的显示区域是源区域内容裁剪到多边形轮廓内的结果，多边形外的部分变成透明"穿透"区域（桌面可见）。
- 形状会覆盖之前设置的任何形状（椭圆、圆角矩形、位图形状等），因为每次应用形状都会替换窗口区域。
- 录制状态在调用 end_shape 后自动结束；之后可以立刻对另一个窗口开始新的形状录制。

## 示例

```gml
// 在控制对象的 Step 事件中：按 D 把 1 号分裂窗口裁成菱形，按 C 恢复成矩形
if (keyboard_check_pressed(ord("D")))
{
    var _w = 640;
    var _h = 360;

    qiumingdll_winsplit_begin_shape(global.split_1);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w / 2, 0);      // 上
    qiumingdll_winsplit_add_shape_point(global.split_1, _w, _h / 2);     // 右
    qiumingdll_winsplit_add_shape_point(global.split_1, _w / 2, _h);     // 下
    qiumingdll_winsplit_add_shape_point(global.split_1, 0, _h / 2);      // 左

    if (qiumingdll_winsplit_end_shape(global.split_1) == 1)
        show_debug_message("菱形形状已应用");
}

if (keyboard_check_pressed(ord("R")))
    qiumingdll_winsplit_clear_shape(global.split_1);
```

## 相关函数

- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_add_shape_point](qiumingdll_winsplit_add_shape_point.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)