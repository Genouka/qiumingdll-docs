# qiumingdll_winself_begin_shape()

开始为游戏自身窗口录制自定义多边形形状：清空形状点缓冲，后续用 `qiumingdll_winself_add_shape_point` 依次添加顶点、用 `qiumingdll_winself_end_shape` 生成形状。

## 函数签名

```gml
qiumingdll_winself_begin_shape()
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

无参数。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 开始录制成功 |
| 0 | 失败：窗口句柄无效；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：在 Windows 平台下、游戏窗口已存在时调用。函数内部自动使用 `window_handle()` 作为目标窗口。
- 形状点坐标基于窗口**客户区**（client rect）坐标系，原点为客户区左上角。
- 必须依次调用 begin → add_shape_point（至少 3 个点）→ end，才会真正改变窗口形状。
- 顶点顺序决定多边形缠绕方向，建议按顺时针或逆时针连续添加。
- 多边形之外的区域变为透明，鼠标点击透明区域会穿透到桌面。

## 示例

```gml
// 生成一个三角形的游戏窗口（客户区 0,0 ~ 800,600 内）
qiumingdll_winself_begin_shape();
qiumingdll_winself_add_shape_point(400, 0);
qiumingdll_winself_add_shape_point(800, 600);
qiumingdll_winself_add_shape_point(0, 600);
qiumingdll_winself_end_shape();
```

## 相关函数

- [qiumingdll_winself_add_shape_point](qiumingdll_winself_add_shape_point.md)
- [qiumingdll_winself_end_shape](qiumingdll_winself_end_shape.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
