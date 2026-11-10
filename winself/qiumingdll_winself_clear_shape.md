# qiumingdll_winself_clear_shape()

清除游戏自身窗口的形状区域，恢复为完整矩形（显示整个客户区画面）。

## 函数签名

```gml
qiumingdll_winself_clear_shape()
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

无参数。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 清除成功（已恢复为完整矩形） |
| 0 | 失败：窗口句柄无效；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：在 Windows 平台下、游戏窗口已存在时调用。函数内部自动使用 `window_handle()` 作为目标窗口。
- 调用后窗口恢复为普通的矩形窗口，之前通过 ellipse / roundrect / 多边形 / 位图设置的任何异型形状都被移除。
- 与透明度接口互不冲突：清除形状不影响已设置的窗口透明度。

## 示例

```gml
// 恢复游戏窗口为矩形
qiumingdll_winself_clear_shape();
```

## 相关函数

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
