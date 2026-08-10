# qiumingdll_winsplit_batch_add_wait(splitId, durationMs)

在批处理录制中添加一条"原地等待"命令：播放时窗口在 durationMs 毫秒内保持当前状态不变，之后继续执行下一条命令。

## 函数签名

```gml
qiumingdll_winsplit_batch_add_wait(splitId, durationMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| durationMs | Real | 是 | 等待时长，单位毫秒；传 0 表示不等待，立即进入下一条命令 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 命令添加成功 |
| 0 | 添加失败：splitId 无效、未在录制中、或命令数已达上限 32 条；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先 qiumingdll_winsplit_batch_begin 进入录制状态，且尚未 qiumingdll_winsplit_batch_end。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 等待期间窗口位置、尺寸、源区域全部保持不变（不做任何插值）。
- 等待命令不改变窗口的结束状态，"结束状态"计算（用于 fastforward 冲突模式）会跳过等待命令。
- 适合在两条动画之间制造停顿，让观众看清中间状态。

## 示例

```gml
// 按键事件：录制"移入 → 等 1 秒 → 移出"的完整序列
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 500);  // 500ms 移入
    qiumingdll_winsplit_batch_add_wait(global.splitId, 1000);               // 原地等待 1 秒
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 500);  // 500ms 移出
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md)
- [qiumingdll_winsplit_batch_add_region](qiumingdll_winsplit_batch_add_region.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)