# qiumingdll_winsplit_cleanup()

整体清理窗口分裂模块：销毁所有分裂窗口、恢复原游戏窗口显示、卸载捕获与消息钩子。用于游戏退出或彻底停用分裂功能。

## 函数签名

```gml
qiumingdll_winsplit_cleanup()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 清理成功；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用（未初始化时调用也无害，幂等）。
- 本次清理依次完成：销毁全部分裂窗口 → 若原窗口被隐藏则恢复显示 → 移除画面捕获钩子与消息钩子。
- 清理完成后所有分裂窗口 ID 失效，`get_count` 返回 0；若之后再使用分裂功能，必须重新调用 `qiumingdll_winsplit_init()`。
- 建议在游戏退出事件（如 Game End / Main Loop 结束前）调用，确保原窗口和系统状态被完整还原；不调用也不会崩溃，但可能残留隐藏状态与钩子。
- 对单个分裂窗口的销毁请用 `qiumingdll_winsplit_destroy` 或 `qiumingdll_winsplit_destroy_all`，本函数是"模块级"清理。

## 示例

```gml
// 在控制对象的 Game End 事件（或 Clean Up 事件）中执行模块清理
qiumingdll_winsplit_cleanup();
```

```gml
// 在游戏中提供"停用分裂模式"的开关：先清理，后续需要时再重新 init
// 控制对象 Step 事件
if (keyboard_check_pressed(ord("Q")))
{
    qiumingdll_winsplit_cleanup();
    global.winsplit_ready = false; // 标记模块已停用，下次使用前需重新 init
}
```

## 相关函数

- [qiumingdll_winsplit_init](qiumingdll_winsplit_init.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_show_original](qiumingdll_winsplit_show_original.md)