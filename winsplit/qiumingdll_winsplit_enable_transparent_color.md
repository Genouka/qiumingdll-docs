# qiumingdll_winsplit_enable_transparent_color(splitId, enable)

开启或关闭指定分裂窗口的透明色键（color key）功能，而不改变已设置的色键值。需先通过 `qiumingdll_winsplit_set_transparent_color` 设定色键后，本函数才决定该色键是否生效。

## 函数签名

```gml
qiumingdll_winsplit_enable_transparent_color(splitId, enable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| enable | Real | 是 | 是否启用透明色键：非 0 = 开启，0 = 关闭；一般传入 `true` / `false` |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功（状态已切换） |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 本函数只切换"透明色键开关"，不影响 `qiumingdll_winsplit_set_transparent_color` 设定的色键值；关闭后色键缓存仍在，再次开启会沿用上一次设定的颜色。
- 若从未调用过 `set_transparent_color`，窗口内 `useColorKey` 默认为关闭状态，调用本函数开启后才按默认色键（0，即纯黑）生效。
- 透明色键基于分层窗口的 `LWA_COLORKEY`：开启时对应颜色的像素变透明；关闭时恢复为普通不透明渲染（系统自动移除分层窗口样式，性能最佳）。
- 可与整体透明度（`set_opacity`）叠加使用。

## 示例

```gml
// 先设定要抠掉的颜色（例如纯红 COLORREF 0x000000FF），再开启
qiumingdll_winsplit_set_transparent_color(global.split_1, 0x000000FF);
qiumingdll_winsplit_enable_transparent_color(global.split_1, true);

// 游戏中根据开关状态切换
if (global.use_mask)
{
    qiumingdll_winsplit_enable_transparent_color(global.split_1, true);
}
else
{
    qiumingdll_winsplit_enable_transparent_color(global.split_1, false);
}
```

## 相关函数

- [qiumingdll_winsplit_set_transparent_color](qiumingdll_winsplit_set_transparent_color.md)
- [qiumingdll_winsplit_set_opacity](qiumingdll_winsplit_set_opacity.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
