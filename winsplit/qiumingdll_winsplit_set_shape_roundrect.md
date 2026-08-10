# qiumingdll_winsplit_set_shape_roundrect(splitId, cornerW, cornerH)

把指定的分裂窗口设置为圆角矩形形状（四个角按指定圆角半径裁掉），是"无边框圆角面板"的常用形状。

## 函数签名

```gml
qiumingdll_winsplit_set_shape_roundrect(splitId, cornerW, cornerH)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| cornerW | Real | 是 | 圆角在水平方向的半径（角宽度），像素，取值 0 ~ 客户区宽；0 表示无圆角 |
| cornerH | Real | 是 | 圆角在垂直方向的半径（角高度），像素，取值 0 ~ 客户区高；0 表示无圆角 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 圆角矩形形状应用成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- cornerW/cornerH 是圆角椭圆的半轴长：例如 (20, 20) 得到 20 像素半径的圆角。两个值都传 0 时等于没有圆角的矩形（此时与矩形窗口无异）。
- 圆角外的四角区域透明、鼠标点击穿透。
- 形状不会随窗口尺寸变化自动更新：之后用 set_size 改变窗口大小，需要重新调用本函数。
- 该形状会替换之前设置的任何形状；`qiumingdll_winsplit_clear_shape` 可恢复矩形。

## 示例

```gml
// 在控制对象的 Step 事件中：按 U 把 1 号分裂窗口变成圆角面板
if (keyboard_check_pressed(ord("U")))
{
    // 20 像素圆角的窗户风格
    qiumingdll_winsplit_set_shape_roundrect(global.split_1, 20, 20);
}

// 按 9 变成"胶囊"型（竖直方向很大圆角），按 0 恢复矩形
if (keyboard_check_pressed(ord("9")))
    qiumingdll_winsplit_set_shape_roundrect(global.split_1, 200, 200);

if (keyboard_check_pressed(ord("0")))
    qiumingdll_winsplit_clear_shape(global.split_1);
```

## 相关函数

- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)