# qiumingdll_winself_set_shape_roundrect(cornerW, cornerH)

把游戏自身窗口设置为圆角矩形形状（四个角按指定圆角半径裁掉），是"无边框圆角面板"的常用形状。

## 函数签名

```gml
qiumingdll_winself_set_shape_roundrect(cornerW, cornerH)
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| cornerW | Real | 是 | 圆角椭圆的宽度（像素），一般取 0 ~ 客户区短边的一半 |
| cornerH | Real | 是 | 圆角椭圆的高度（像素），一般取 0 ~ 客户区短边的一半 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 圆角矩形形状应用成功 |
| 0 | 失败：窗口句柄无效；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：在 Windows 平台下、游戏窗口已存在时调用。函数内部自动使用 `window_handle()` 作为目标窗口。
- 圆角矩形内切于窗口客户区，四角按 (cornerW, cornerH) 指定的椭圆角裁掉。
- cornerW / cornerH 过大（超过短边一半）会被系统按有效范围处理，建议取较小常用值（如 16、32）。
- 形状基于窗口客户区坐标，不会随窗口尺寸变化自动更新：改变窗口大小后需重新调用。
- 该形状会替换之前设置的任何形状；`qiumingdll_winself_clear_shape` 可恢复矩形。

## 示例

```gml
// 给游戏窗口加上 32px 的圆角
qiumingdll_winself_set_shape_roundrect(32, 32);
```

## 相关函数

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_from_bitmap](qiumingdll_winself_set_shape_from_bitmap.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
