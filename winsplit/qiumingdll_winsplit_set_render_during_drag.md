# qiumingdll_winsplit_set_render_during_drag(enable)

设置拖拽分裂窗口的过程中是否持续渲染窗口内容（全局设置，默认开启）。

## 函数签名

```gml
qiumingdll_winsplit_set_render_during_drag(enable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| enable | Real | 是 | 0=拖拽时不渲染，非 0=拖拽时渲染（默认值 1） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：建议在 qiumingdll_winsplit_init 之后调用（全局设置，时刻调用均有效）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 本函数仍然有效（不是弃用 API）：控制用户拖拽分裂窗口（可拖拽窗口，见 qiumingdll_winsplit_set_draggable）期间是否跟随渲染画面。
- 默认值为 1（拖拽时渲染）。传 0 可让拖拽过程更省资源，但画面会以拖拽结束后的帧为准。
- 全局设置，影响所有分裂窗口。
- 该设置属于低优先级调优项：一般不建议修改默认值。

## 示例

```gml
// Create 事件：初始化、开启"拖拽时渲染"并创建分裂窗口
qiumingdll_winsplit_init();
qiumingdll_winsplit_set_render_during_drag(1);  // 拖拽过程中正常渲染

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
qiumingdll_winsplit_set_draggable(global.splitId, 1);  // 允许拖拽
```

## 相关函数

- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)
- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md)（已弃用）
- [qiumingdll_winsplit_set_dwm_thumbnail_mode](qiumingdll_winsplit_set_dwm_thumbnail_mode.md)（已弃用）