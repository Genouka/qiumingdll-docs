# qiumingdll_pitch_cleanup()

彻底清理 pitch 模块：停止音高检测、释放麦克风设备与全部内部资源，并把所有状态（含检测结果与阈值参数）清零。

## 函数签名

```gml
qiumingdll_pitch_cleanup()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 清理完成。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：无。未启动检测时调用也是安全的。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0，不产生效果）。
- 与 stop 的区别：stop 只停止检测并保留参数；cleanup 会**连 YIN 阈值一起重置**（恢复默认值 0.15），并把内部数据结构彻底复位。cleanup 之后若需继续使用，必须重新调用 qiumingdll_pitch_start() 并重新设置需要的阈值。
- 建议在游戏完全退出前调用，确保麦克风被释放，避免 DLL 卸载时设备仍被占用导致崩溃或残留。
- 通常扩展的全局清理流程会自动调用本函数；手动调用时注意不要与全局清理重复执行（重复调用安全但多余）。
- 提示：cleanup 只影响 pitch 模块；volume 模块若无单独清理，其录音不会被本函数停止。
- 调试建议：在房间结束事件里调用后，若再回到检测界面，请重新走完整的 start → 设置阈值 流程，避免在"已清理"状态下直接读取 Get 函数（此时会返回未启动形态的值）。

## 示例

```gml
/// 房间结束事件 (obj_voice_pitch)
// 离开检测场景时彻底释放 pitch 模块资源
qiumingdll_pitch_cleanup();
pitchActive = false;

/// 游戏结束事件
// 游戏退出前的最终清理
qiumingdll_pitch_cleanup();

/// 再次启用（例如重新进入调音房间）
// cleanup 之后需要完全重新初始化使用
var err = qiumingdll_pitch_start(48000, 10);
if (err == 0)
{
    qiumingdll_pitch_set_threshold(0.15); // 恢复到需要的阈值
    pitchActive = true;
}
```

## 相关函数

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md)
- [qiumingdll_pitch_set_threshold](qiumingdll_pitch_set_threshold.md)