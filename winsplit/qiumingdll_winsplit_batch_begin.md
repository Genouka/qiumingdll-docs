# qiumingdll_winsplit_batch_begin(splitId)

开始录制指定分裂窗口的批处理动画序列；之后的 batch_add_* 命令将以此为基础按顺序累积。

## 函数签名

```gml
qiumingdll_winsplit_batch_begin(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 录制已开始 |
| 0 | splitId 无效（该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先初始化并创建分裂窗口（qiumingdll_winsplit_init / qiumingdll_winsplit_create）。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 调用后该窗口进入"录制中"状态：清空已有命令（最多 32 条）、停止当前播放中的批处理。
- 录制期间不能调用 batch_play（会返回 0），必须先 batch_end。
- 录制开始时，批处理的初始缓动曲线取该窗口当前的普通动画曲线（默认 ease-in-out），初始源动画模式重置为 0（无）；可通过 batch_set_easing / batch_set_src_anim_mode 在录制中修改。
- 典型的完整流程：batch_begin → batch_add_*（若干条）→ batch_end → batch_play（或 batch_play_frame_sync + 每帧 batch_step）。

## 示例

```gml
// 按键事件：录制一条完整的批处理动画序列
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);               // 1. 开始录制
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 200, 400);  // 移入
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 400);      // 放大
    qiumingdll_winsplit_batch_add_wait(global.splitId, 500);                 // 停留
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 400);  // 移出
    qiumingdll_winsplit_batch_end(global.splitId);                 // 2. 结束录制
    qiumingdll_winsplit_batch_play(global.splitId, 1);             // 3. 播放（打断模式）
}
```

## 相关函数

- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
- [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_clear](qiumingdll_winsplit_batch_clear.md)