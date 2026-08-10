# qiumingdll_winsplit_batch_play(splitId, conflictMode)

播放指定分裂窗口已录制好的批处理动画序列；由内部 16ms 定时器驱动，与游戏帧率无关。

## 函数签名

```gml
qiumingdll_winsplit_batch_play(splitId, conflictMode)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| conflictMode | Real | 是 | 与正在播放的批处理发生冲突时的处理方式，取值范围 0~3，含义见下表 |

冲突模式枚举：

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | stack | 排队等待：不主动停止当前播放的批处理，本次请求紧接着处理 |
| 1 | interrupt | 立即打断：停止当前播放的批处理，从头播放本次序列 |
| 2 | rollback | 回滚重播：先把窗口回滚到"上次播放开始前"的状态，再从头播放本次序列 |
| 3 | fastforward | 快进：先把窗口直接推进到"上次批处理结束"的状态，再从头播放本次序列 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 播放已启动（或已排队/回滚/快进后启动） |
| 0 | 播放失败：splitId 无效、命令数为 0、或仍在录制中（未调用 batch_end）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先完成"录制"流程：batch_begin → batch_add_* → batch_end，且命令数大于 0。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 播放间隔固定为 16ms（约 60fps 节奏），命令时长累计决定总播放时间。
- 播放期间该窗口的普通动画会被忽略（批处理优先）；想中途停止请用 batch_stop。
- 需要与游戏帧率精确同步时，改用 batch_play_frame_sync + 每帧 batch_step 驱动。
- 播放结束后命令保留，可再次播放；用 batch_clear 清空。
- 若希望严格按"排队"语义等待前一批处理播放完，建议先用 batch_is_playing 轮询，播放结束后再调用本函数。

## 示例

```gml
// 按键事件：录制并播放一段"飞入-停留-飞出"序列
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 500);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 500);
    qiumingdll_winsplit_batch_add_position(global.splitId, 800, 600, 500);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);  // interrupt：立即从头播放
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)