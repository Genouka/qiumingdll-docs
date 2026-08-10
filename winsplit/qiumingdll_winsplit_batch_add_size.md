# qiumingdll_winsplit_batch_add_size(splitId, w, h, durationMs)

在批处理录制中添加一条"尺寸缩放"命令：播放时窗口在 durationMs 毫秒内从当前尺寸缩放到目标尺寸 (w, h)（源区域按当时的源动画模式联动）。

## 函数签名

```gml
qiumingdll_winsplit_batch_add_size(splitId, w, h, durationMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| w | Real | 是 | 目标宽度（客户区宽度，单位像素） |
| h | Real | 是 | 目标高度（客户区高度，单位像素） |
| durationMs | Real | 是 | 该段动画时长，单位毫秒；传 0 表示跳过过渡，命令开始时立即到位 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 命令添加成功 |
| 0 | 添加失败：splitId 无效、未在录制中、或命令数已达上限 32 条；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先 qiumingdll_winsplit_batch_begin 进入录制状态，且尚未 qiumingdll_winsplit_batch_end。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 该命令不改变窗口位置，只缩放尺寸。
- 源区域联动由添加命令时设定的源动画模式决定（见 qiumingdll_winsplit_batch_set_src_anim_mode）：0=不动（画面拉伸填满）、1=等比拉伸、2~10=按锚点裁剪。
- 缓动取添加命令时设定的批处理缓动曲线（见 qiumingdll_winsplit_batch_set_easing）。
- 命令起始状态取"该命令开始执行时刻"的窗口状态，命令按顺序首尾相接。

## 示例

```gml
// 按键事件：录制"放大-微等待-复原"的序列（本函数负责两条缩放命令）
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_set_src_anim_mode(global.splitId, 1);  // 源区域随窗口等比拉伸
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 500);   // 500ms 放大到 640x480
    qiumingdll_winsplit_batch_add_wait(global.splitId, 200);             // 停留 200ms
    qiumingdll_winsplit_batch_add_size(global.splitId, 320, 240, 500);   // 500ms 缩回 320x240
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
- [qiumingdll_winsplit_batch_add_region](qiumingdll_winsplit_batch_add_region.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)