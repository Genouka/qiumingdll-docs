# qiumingdll_winsplit_set_dwm_thumbnail_mode(enable)

启用/禁用 DWM 缩略图作为分裂窗口内容来源。**已弃用**：新方案使用 GPU Hook 捕获 backbuffer，调用本函数不会产生任何效果。

## 函数签名

```gml
qiumingdll_winsplit_set_dwm_thumbnail_mode(enable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| enable | Real | 是 | 旧方案下的开关（0=关闭，非 0=开启）。新方案中该参数被忽略，传任意值均可（建议传 0） |

## 返回值

| 值 | 说明 |
|----|------|
| （无） | 本函数的 GML 包装脚本没有 return 语句，返回值为 undefined，不要依赖返回值判断执行结果 |

## 使用说明

- **已弃用，调用无任何效果**：新方案通过 D3D11 Present 钩子直接从 GPU 读取 backbuffer，不再使用 DWM 缩略图。
- **注意事项（与其他包装不同）**：
  - 该包装脚本没有 `variable_global_exists` 检查，若 DLL 未加载（`__qiumingdll_winsplit_set_dwm_thumbnail_mode` 全局不存在），直接调用会报脚本错误，请先自行检查；
  - 包装脚本引用的是变量名 `enable` 而非 `argument0`，并非常规的 argument 传参写法，兼容性有限；
  - 非 Windows 平台同样没有返回值（不返回 0）。
- 全局设置，无 splitId 参数。
- 保留该 API 仅为兼容旧版调用方；新代码不应调用本函数。

## 示例

```gml
// 旧代码迁移示例：调用前检查全局是否存在，避免脚本错误
if (variable_global_exists("__qiumingdll_winsplit_set_dwm_thumbnail_mode"))
{
    qiumingdll_winsplit_set_dwm_thumbnail_mode(0);  // 新方案中无任何效果，可安全删除
}
```

## 相关函数

- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md)
- [qiumingdll_winsplit_set_render_interval](qiumingdll_winsplit_set_render_interval.md)
- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)