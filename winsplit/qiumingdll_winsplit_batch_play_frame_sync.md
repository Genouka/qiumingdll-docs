# qiumingdll_winsplit_batch_play_frame_sync(splitId, conflictMode)

以"帧同步"方式播放指定分裂窗口的批处理动画：不创建内部定时器，必须由调用方每帧调用 batch_step 推进，进度与游戏帧率完全一致。

## 函数签名

```gml
qiumingdll_winsplit_batch_play_frame_sync(splitId, conflictMode)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| conflictMode | Real | 是 | 与正在播放的批处理发生冲突时的处理方式，取值与 batch_play 相同：0=stack 排队等待、1=interrupt 立即打断、2=rollback 回滚到上次播放前状态、3=fastforward 快进到上次播放结束状态 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 播放已启动 |
| 0 | 播放失败：splitId 无效、命令数为 0、或仍在录制中（未调用 batch_end）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先完成录制流程（batch_begin → batch_add_* → batch_end）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 与 batch_play 的区别：本函数不启动任何定时器。若调用方没有在每一帧调用 qiumingdll_winsplit_batch_step，批处理将停留在第一帧，不会自动推进。
- 推荐用法：在 Step 事件中每帧调用 batch_step，直到其返回 0（播放结束）。
- 命令时长仍以毫秒计，进度按系统时间插值；帧率越高每帧推进的插值量越小。
- 其余行为（冲突模式、命令顺序、源区域联动、结束状态计算）与 batch_play 一致。

## 示例

```gml
// 按键事件：以帧同步模式开始播放
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 600);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 400);
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 600);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play_frame_sync(global.splitId, 1);  // 不启动定时器
}

// Step 事件：每帧推进批处理，返回 0 表示播放结束
if (qiumingdll_winsplit_batch_step(global.splitId) == 0)
{
    // 播放结束（或未在播放），可在此触发后续逻辑
}
```

## 相关函数

- [qiumingdll_winsplit_batch_step](qiumingdll_winsplit_batch_step.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)