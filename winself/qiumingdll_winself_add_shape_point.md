# qiumingdll_winself_add_shape_point(x, y)

在 `qiumingdll_winself_begin_shape` 与 `qiumingdll_winself_end_shape` 之间，向当前正在录制的多边形形状添加一个顶点。

## 函数签名

```gml
qiumingdll_winself_add_shape_point(x, y)
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| x | Real | 是 | 顶点 X 坐标（窗口客户区坐标系） |
| y | Real | 是 | 顶点 Y 坐标（窗口客户区坐标系） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 顶点添加成功 |
| 0 | 失败：窗口句柄无效、尚未 begin_shape、或顶点数已达上限（256）；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：必须已经在游戏窗口上调用过 `qiumingdll_winself_begin_shape`。
- 坐标基于窗口客户区（client rect）坐标系，原点为客户区左上角。
- 至少需要 3 个顶点，调用 `qiumingdll_winself_end_shape` 后多边形才生效。
- 一次录制最多 256 个顶点。

## 示例

```gml
// 在 begin / end 之间添加一个顶点
qiumingdll_winself_add_shape_point(400, 300);
```

## 相关函数

- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
- [qiumingdll_winself_end_shape](qiumingdll_winself_end_shape.md)
