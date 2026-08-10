# qiumingdll_winsplit_batch_step(splitId)

推进指定分裂窗口的"帧同步"批处理动画一帧（仅对 batch_play_frame_sync 启动的播放有效），并返回播放是否仍在进行。

## 函数签名

```gml
qiumingdll_winsplit_batch_step(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 批处理仍在播放中，需要继续在下一帧调用本函数 |
| 0 | 批处理已播放结束；或该窗口当前没有帧同步批处理在播放（包括用 batch_play 启动的定时器模式）；或 splitId 无效；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先用 qiumingdll_winsplit_batch_play_frame_sync 启动帧同步播放。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 每帧调用一次即可；内部按系统时间计算插值进度，调用频率决定平滑度（建议在 Step 事件中每帧调用）。
- 本函数只对 frameSync 模式生效：用 batch_play 启动的定时器播放调用本函数会返回 0。
- 播放结束后返回 0，无需再调用；命令保留，可重新播放。
- 注意：若中途不再调用本函数，批处理会"冻结"在当前进度，不会自行结束。

## 示例

```gml
// Create 事件：初始化并创建分裂窗口
qiumingdll_winsplit_init();
global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);

// 按键事件：录制并用帧同步模式播放
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 800);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 800);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play_frame_sync(global.splitId, 1);
}

// Step 事件：每帧推进帧同步批处理
if (qiumingdll_winsplit_batch_step(global.splitId) == 0)
{
    show_debug_message("帧同步批处理已结束");
}
```

## 相关函数

- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)