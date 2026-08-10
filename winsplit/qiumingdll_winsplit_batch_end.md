# qiumingdll_winsplit_batch_end(splitId)

结束指定分裂窗口的批处理录制状态，之后才能调用 batch_play / batch_play_frame_sync 播放。

## 函数签名

```gml
qiumingdll_winsplit_batch_end(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 录制已结束 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先调用 qiumingdll_winsplit_batch_begin 开始录制。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 结束录制只是把状态置为"可播放"，不会立即播放；播放需要再调用 batch_play 或 batch_play_frame_sync。
- 录制期间添加的命令全部保留；若想废弃本次录制，可调用 qiumingdll_winsplit_batch_clear 清空，或重新 batch_begin（会自动清空）。
- 即使一条命令都没添加，batch_end 也会返回 1；但后续 batch_play 在命令数为 0 时会返回 0（不会播放）。
- 结束后可以再次 batch_begin 开始录制新序列，旧命令会被清空。

## 示例

```gml
// 按键事件：完整的"录制 → 结束 → 播放"流程
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_region(global.splitId, 300, 200, 480, 360, 500);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 300);
    qiumingdll_winsplit_batch_end(global.splitId);     // 结束录制（关键步骤）
    qiumingdll_winsplit_batch_play(global.splitId, 1); // 开始播放
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_clear](qiumingdll_winsplit_batch_clear.md)