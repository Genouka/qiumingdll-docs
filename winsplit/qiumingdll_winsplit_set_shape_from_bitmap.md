# qiumingdll_winsplit_set_shape_from_bitmap(splitId, bitmapPath, transColor)

用一张位图（BMP）作为分裂窗口的形状模板：图中颜色等于 transColor 的像素在窗口上变透明（成洞），其余像素保留显示。

## 函数签名

```gml
qiumingdll_winsplit_set_shape_from_bitmap(splitId, bitmapPath, transColor)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| bitmapPath | String | 是 | BMP 位图文件路径（磁盘上的真实路径，非资源名），建议用 `working_directory + 文件名` 拼接；中文路径支持 |
| transColor | Real | 是 | 透明色，格式 0xRRGGBB（红绿蓝各 0~255，共 24 位）；与该颜色完全相等的像素将变透明 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 形状应用成功：图片加载、透明色检测、区域生成均完成 |
| 0 | 失败：splitId 无效/不存在、位图文件加载失败（路径错误或非 BMP）等；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 只支持 BMP 文件；加载失败时返回 0 并保留窗口之前的形状不变。
- transColor 中的 alpha 部分被忽略，只比较 RGB（低 24 位）。示例：品红 `0xFF00FF`、黑色 `0x000000`。
- 图片尺寸可以小于、等于或大于窗口；形状按图片像素逐行扫描生成，图片中非透明区域在窗口上呈现为形状区域。
- 形状不随窗口尺寸变化自动更新：之后 set_size 改变窗口大小后，需要重新调用本函数。
- 该形状会替换之前设置的任何形状；`qiumingdll_winsplit_clear_shape` 可恢复矩形。
- 适合做异形窗口（星星、角色剪影、任意图形 UI），美术侧只需准备一张带纯色背景的 BMP。

## 示例

```gml
// 在控制对象的 Step 事件中：按 B 用一张五角星模板图裁剪 1 号分裂窗口
if (keyboard_check_pressed(ord("B")))
{
    // mask.bmp：五角星为白色，背景为品红（#FF00FF），品红部分将透明
    var _bmp = working_directory + "star_mask.bmp";
    if (file_exists(_bmp))
    {
        if (qiumingdll_winsplit_set_shape_from_bitmap(global.split_1, _bmp, 0xFF00FF) == 1)
            show_debug_message("五角星形状已应用，背景品红部分已透明");
        else
            show_debug_message("位图形状应用失败：请检查文件是否为 BMP 且路径正确");
    }
}
```

## 相关函数

- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
- [qiumingdll_winsplit_set_shape_roundrect](qiumingdll_winsplit_set_shape_roundrect.md)
- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)