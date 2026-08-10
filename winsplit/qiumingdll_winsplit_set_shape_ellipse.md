# qiumingdll_winsplit_set_shape_ellipse(splitId)

把指定的分裂窗口设置为椭圆形（内切于其客户区的椭圆），窗口四角变透明，适合做成圆形小地图、圆形头像窗等。

## 函数签名

```gml
qiumingdll_winsplit_set_shape_ellipse(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 椭圆形状应用成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 椭圆内切于窗口客户区：宽度为客户区宽、高度为客户区高的完整椭圆（水平方向的椭圆）。窗口必须足够"方"才接近正圆；想获得正圆请先 set_size 把宽高设为相等。
- 椭圆外的区域变为透明，鼠标点击透明区域会穿透到桌面。
- 椭圆大小不会跟随窗口尺寸变化自动更新：如果之后用 set_size 改变窗口大小，需要重新调用本函数刷新形状。
- 该形状会替换之前设置的任何形状；`qiumingdll_winsplit_clear_shape` 可恢复矩形。

## 示例

```gml
// 在控制对象的 Step 事件中：按 M 生成一个 400x400 的圆形小地图分裂窗口
if (keyboard_check_pressed(ord("M")))
{
    // 先创建正方形窗口，再应用椭圆 => 得到正圆
    if (global.split_minimap == 0)
        global.split_minimap = qiumingdll_winsplit_create(0, 0, 500, 500, 30, 30, 400, 400);

    qiumingdll_winsplit_set_shape_ellipse(global.split_minimap);
}
```

## 相关函数

- [qiumingdll_winsplit_set_shape_roundrect](qiumingdll_winsplit_set_shape_roundrect.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)