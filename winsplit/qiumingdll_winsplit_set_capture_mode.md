# qiumingdll_winsplit_set_capture_mode(mode)

设置分裂窗口的捕获方式。**已弃用**：新方案总是从 GPU 直接读取 backbuffer，调用本函数不会产生任何效果（返回值固定为 1）。

## 函数签名

```gml
qiumingdll_winsplit_set_capture_mode(mode)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| mode | Real | 是 | 旧方案下的捕获模式参数（如"屏幕截图 / PrintWindow"）。新方案中该参数被忽略，传任意值均可（建议传 0） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 函数执行成功（固定返回值，不代表有任何效果） |
| 0 | 非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- **已弃用，调用无任何效果**：新的 D3D11 GPU 捕获方案始终从 IDXGISwapChain 的 backbuffer 读取画面，不再存在"截图模式"切换。
- 保留该 API 仅为兼容旧版调用方：即使调用，捕获行为也不会改变。
- 全局设置，无 splitId 参数，作用于所有分裂窗口（实际上不起作用）。
- 新代码不应调用本函数，直接从项目中移除即可。
- 平台限制：仅 Windows；其他平台该 GML 包装返回 0。

## 示例

```gml
// 旧代码迁移示例：以下调用在新方案中无任何效果，可安全删除
if (variable_global_exists("__qiumingdll_winsplit_set_capture_mode"))
{
    qiumingdll_winsplit_set_capture_mode(0);
}
```

## 相关函数

- [qiumingdll_winsplit_set_dwm_thumbnail_mode](qiumingdll_winsplit_set_dwm_thumbnail_mode.md)
- [qiumingdll_winsplit_set_render_interval](qiumingdll_winsplit_set_render_interval.md)
- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)
- [qiumingdll_winsplit_set_render_during_drag](qiumingdll_winsplit_set_render_during_drag.md)