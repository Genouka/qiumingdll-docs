# qiumingdll_winsplit_batch_clear(splitId)

停止指定分裂窗口正在播放的批处理，并清空其所有已录制的命令，解除录制状态。

## 函数签名

```gml
qiumingdll_winsplit_batch_clear(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 清理成功 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 效果：若正在播放则立即停止（含内部定时器）；命令数清零；录制状态解除（recording = false）。
- 窗口停留在当前位置/尺寸，不会移动或跳变。
- 与 batch_stop 的区别：stop 只停止播放、保留命令；clear 同时删除所有命令。
- 清空后重新 batch_begin 即可录制新序列。

## 示例

```gml
// 按键事件：清空旧批处理并录制一段全新序列
if (keyboard_check_pressed(vk_r))
{
    qiumingdll_winsplit_batch_clear(global.splitId);  // 停播 + 清空命令
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_region(global.splitId, 200, 150, 640, 480, 600);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 400);
    qiumingdll_winsplit_batch_add_region(global.splitId, 100, 100, 320, 240, 600);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)