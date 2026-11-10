# qiumingdll_winself_set_shape_ellipse()

把游戏自身窗口设置为椭圆形（内切于其客户区的椭圆），窗口四角变透明，适合做成圆形小地图、圆形头像窗等。

## 函数签名

```gml
qiumingdll_winself_set_shape_ellipse()
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

无参数。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 椭圆形状应用成功 |
| 0 | 失败：窗口句柄无效；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：在 Windows 平台下、游戏窗口已存在时调用。函数内部自动使用 `window_handle()` 作为目标窗口。
- 椭圆内切于窗口客户区：宽度为客户区宽、高度为客户区高的完整椭圆。窗口必须足够"方"才接近正圆；想获得正圆请先调整窗口大小为正方形。
- 椭圆外的区域变为透明，鼠标点击透明区域会穿透到桌面。
- 椭圆大小不会跟随窗口尺寸变化自动更新：如果之后改变窗口大小，需要重新调用本函数刷新形状。
- 该形状会替换之前设置的任何形状；`qiumingdll_winself_clear_shape` 可恢复矩形。

## 示例

```gml
// 把整个游戏窗口裁成椭圆（内切于客户区）
qiumingdll_winself_set_shape_ellipse();
```

## 相关函数

- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_set_shape_from_bitmap](qiumingdll_winself_set_shape_from_bitmap.md)
- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
