# qiumingdll_winself_end_shape()

结束形状录制并把已收集的多边形顶点应用到游戏自身窗口：窗口立即变为该多边形的形状，多边形之外的区域不再显示。

## 函数签名

```gml
qiumingdll_winself_end_shape()
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

无参数。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 形状应用成功 |
| 0 | 失败：窗口句柄无效、尚未 begin_shape、或顶点不足 3 个；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：已经在游戏窗口上调用过 `qiumingdll_winself_begin_shape` 并添加了至少 3 个顶点。
- 顶点不足 3 个时本次录制被丢弃，不产生任何形状变化。
- 该形状会替换之前设置的任何形状；`qiumingdll_winself_clear_shape` 可恢复完整矩形。
- 窗口形状区域基于窗口客户区坐标，不会随窗口尺寸变化自动更新：若之后改变窗口大小，需要重新调用本函数刷新形状。

## 示例

```gml
// 在 begin + 多个 add_shape_point 之后收尾
qiumingdll_winself_end_shape();
```

## 相关函数

- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
- [qiumingdll_winself_add_shape_point](qiumingdll_winself_add_shape_point.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
