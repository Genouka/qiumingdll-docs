# qiumingdll_winsplit_set_render_interval(intervalMs)

设置分裂窗口的渲染刷新间隔。**已弃用**：新方案每帧随游戏 Present 同步渲染，本函数不再限制任何渲染频率（调用无任何效果，返回值固定为 1）。

## 函数签名

```gml
qiumingdll_winsplit_set_render_interval(intervalMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| intervalMs | Real | 是 | 旧方案下的渲染间隔，单位毫秒（如 16 表示约 60fps）。新方案中该参数被忽略，传任意值均可（建议传 16） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 函数执行成功（固定返回值，不代表有任何效果） |
| 0 | 非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- **已弃用，调用无任何效果**：新方案由 Present 钩子驱动渲染，与游戏帧同步，不再使用旧的 1ms 定时器与帧率限制。
- 保留该 API 仅为兼容旧版调用方：即使调用，渲染节奏也不会改变。
- 全局设置，无 splitId 参数，作用于所有分裂窗口（实际上不起作用）。
- 新代码不应调用本函数，直接从项目中移除即可。
- 平台限制：仅 Windows；其他平台该 GML 包装返回 0。

## 示例

```gml
// 旧代码迁移示例：以下调用在新方案中无任何效果，可安全删除
if (variable_global_exists("__qiumingdll_winsplit_set_render_interval"))
{
    qiumingdll_winsplit_set_render_interval(16);
}
```

## 相关函数

- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md)
- [qiumingdll_winsplit_set_dwm_thumbnail_mode](qiumingdll_winsplit_set_dwm_thumbnail_mode.md)
- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)