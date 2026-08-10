# qiumingdll_winsplit_batch_stop(splitId)

中途停止指定分裂窗口正在播放的批处理动画，窗口停留在被停止时的状态。

## 函数签名

```gml
qiumingdll_winsplit_batch_stop(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（无论之前是否在播放） |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 停止后窗口停留在当前插值位置/尺寸，不会跳到批处理的最终状态。
- 定时器模式的播放（batch_play）会同时停止其内部定时器；帧同步模式的播放（batch_play_frame_sync）停止后，继续调用 batch_step 会返回 0。
- 只作用于批处理动画；普通动画需要用 qiumingdll_winsplit_stop_animation 停止。
- 停止不会清空已录制的命令，之后可再次 batch_play 从头播放。
- 想要彻底丢弃该批处理，请用 qiumingdll_winsplit_batch_clear。

## 示例

```gml
// 按键事件：开始播放一段 10 秒的长序列
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 5000);
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 5000);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}

// 按键事件：中途停止
if (keyboard_check_pressed(vk_x))
{
    qiumingdll_winsplit_batch_stop(global.splitId);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)
- [qiumingdll_winsplit_batch_clear](qiumingdll_winsplit_batch_clear.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)