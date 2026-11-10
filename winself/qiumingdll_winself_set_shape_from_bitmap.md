# qiumingdll_winself_set_shape_from_bitmap(bitmapPath, transColor)

用一张位图（BMP）作为游戏自身窗口的形状模板：图中颜色等于 `transColor` 的像素在窗口上变透明（成洞），其余像素保留显示。可按任意图形（如角色剪影、圆形、星形）精确裁切窗口。

## 函数签名

```gml
qiumingdll_winself_set_shape_from_bitmap(bitmapPath, transColor)
```

> 窗口句柄由函数内部自动取 `window_handle()`，无需显式传入。

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| bitmapPath | String | 是 | BMP 位图文件路径（建议与游戏窗口客户区同尺寸，32bpp 最佳） |
| transColor | Real | 是 | 视作"透明色"的颜色值，BGR 打包成整数（如 0x00BBGGRR），图中等于该色的像素将被挖空 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 位图形状应用成功 |
| 0 | 失败：窗口句柄无效、路径为空或位图加载失败；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：在 Windows 平台下、游戏窗口已存在时调用；BMP 文件需可被进程以 `LR_LOADFROMFILE` 读取（注意工作目录与权限）。
- 位图像素尺寸决定窗口有效显示区域；建议位图与窗口客户区尺寸一致，否则透明区域范围会按位图像素坐标（客户区坐标系）应用。
- 颜色比较基于 24 位颜色（忽略 alpha），`transColor` 用 0x00BBGGRR 形式传入。
- 该形状会替换之前设置的任何形状；`qiumingdll_winself_clear_shape` 可恢复矩形。

## 示例

```gml
// 用 circle_mask.bmp 中颜色为白色(0x00FFFFFF)的像素成洞，其余保留
qiumingdll_winself_set_shape_from_bitmap("circle_mask.bmp", 0x00FFFFFF);
```

## 相关函数

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
