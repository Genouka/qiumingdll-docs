# qiumingdll_winsplit_batch_is_playing(splitId)

查询指定分裂窗口当前是否正在播放批处理动画（定时器模式与帧同步模式均计入）。

## 函数签名

```gml
qiumingdll_winsplit_batch_is_playing(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 批处理正在播放中 |
| 0 | 未在播放批处理；或 splitId 无效；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0（与"未播放"无法区分）。
- 两种启动方式的播放都会置为 1：batch_play（定时器驱动）与 batch_play_frame_sync（帧同步驱动）都反映在此状态中。
- 播放自然结束、被 batch_stop 停止、或被 batch_clear 清空后恢复为 0。
- 只反映批处理状态，不反映普通动画；普通动画请用 qiumingdll_winsplit_is_animating。

## 示例

```gml
// 按键事件：仅在无批处理播放时启动新播放（避免冲突）
if (keyboard_check_pressed(vk_enter))
{
    if (qiumingdll_winsplit_batch_is_playing(global.splitId) == 0)
    {
        qiumingdll_winsplit_batch_begin(global.splitId);
        qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 800);
        qiumingdll_winsplit_batch_end(global.splitId);
        qiumingdll_winsplit_batch_play(global.splitId, 1);
    }
    else
    {
        show_debug_message("批处理正在播放，忽略本次请求");
    }
}
```

## 相关函数

- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)