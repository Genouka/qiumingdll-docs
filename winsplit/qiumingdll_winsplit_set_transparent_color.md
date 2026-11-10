# qiumingdll_winsplit_set_transparent_color(splitId, color)

设置指定分裂窗口的透明色键（color key）：窗口画面中颜色等于该值的像素变为完全透明（成洞），其余像素正常显示。支持与整体透明度（`set_opacity`）叠加。

## 函数签名

```gml
qiumingdll_winsplit_set_transparent_color(splitId, color)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| color | Real | 是 | 透明色键的颜色值，按 `0x00BBGGRR` 的 24 位 COLORREF 解析（高位字节被忽略，仅取低 24 位 `0x00FFFFFF`）；可与 `make_color_rgb(r, g, b)` 生成的颜色直接传入（GML 颜色为 `0xRRGGBB`，送入后内部取低 24 位，蓝色与红色分量会被按 COLORREF 顺序解释，详见下方使用说明） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功（已启用透明色键并立即生效） |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 透明色键基于分层窗口（layered window）的 `LWA_COLORKEY` 实现：仅"等于"该颜色的像素透明，不等的不透明；它是像素级的精确抠色，与 `set_opacity` 的整体 alpha 混合是两套互不影响的能力。
- 颜色顺序约定：Windows `COLORREF` 为 `0x00BBGGRR`（蓝、绿、红）。本函数内部取 `color & 0x00FFFFFF` 作为色键。若你在 GML 中用 `make_color_rgb(r, g, b)`（其数值为 `0xRRGGBB`）直接传入，红色与蓝色分量会按 COLORREF 的 `BGR` 顺序被解释——即实际抠掉的色是 `(b, g, r)` 而非 `(r, g, b)`。需要严格匹配某像素颜色时，请按 `0x00BBGGRR` 自行构造（例如想抠掉纯红，应传入 `0x000000FF`）。
- 调用本函数会同时把该窗口的"透明色键开关"置为开启；如需临时关闭而保留色值，可用 `qiumingdll_winsplit_enable_transparent_color(splitId, false)`。
- 透明色键与整体透明度可同时生效：先 `set_transparent_color` 抠掉特定颜色，再 `set_opacity` 做整体半透明，二者叠加。
- 取消透明色键后窗口恢复为普通不透明渲染（系统自动移除分层窗口样式，性能最佳）。

## 示例

```gml
// 把 1 号分裂窗口中"纯黑色"（0x000000FF = COLORREF 的纯红，注意 BGR 顺序）
// 抠成透明，实现"用黑色作遮罩"的异形显示
qiumingdll_winsplit_set_transparent_color(global.split_1, 0x000000FF);
```

```gml
// 构造一个真正的纯蓝（RGB 0,0,255）色键：BGR = 0xFF0000
var _key = 0x00FF0000;  // COLORREF 中 0x00BBGGRR => B=FF,G=00,R=00 => 纯蓝
qiumingdll_winsplit_set_transparent_color(global.split_1, _key);

// 临时关闭透明色键（色值保留，下次可直接再开启）
qiumingdll_winsplit_enable_transparent_color(global.split_1, false);

// 重新开启
qiumingdll_winsplit_enable_transparent_color(global.split_1, true);
```

## 相关函数

- [qiumingdll_winsplit_enable_transparent_color](qiumingdll_winsplit_enable_transparent_color.md)
- [qiumingdll_winsplit_set_opacity](qiumingdll_winsplit_set_opacity.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
