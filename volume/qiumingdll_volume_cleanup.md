# qiumingdll_volume_cleanup()

彻底清理 volume 模块：停止录音、释放麦克风设备与全部内部资源，并把所有状态（含音量数值与参数设置）清零。

## 函数签名

```gml
qiumingdll_volume_cleanup()
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

- 前置条件：无。未启动录音时调用也是安全的。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0，不产生效果）。
- 与 stop 的区别：stop 只停止录音并保留参数（静音阈值、平滑系数）；cleanup 会**连参数一起清零**，并把内部数据结构彻底复位。cleanup 之后若需继续使用，必须重新调用 qiumingdll_volume_start() 并重新设置需要的参数（阈值、平滑系数恢复默认值 0.01 / 0.3）。
- 建议在游戏完全退出前调用，确保麦克风被释放，避免 DLL 卸载时设备仍被占用导致崩溃或残留。
- 通常扩展的全局清理流程会自动调用本函数；手动调用时注意不要与全局清理重复执行（重复调用安全但多余）。

## 示例

```gml
/// 房间结束事件 (obj_mic_volume)
// 切换场景或关闭游戏时彻底释放 Volume 模块资源
qiumingdll_volume_cleanup();
volumeActive = false;

/// 游戏结束事件
// 游戏退出前的最终清理
qiumingdll_volume_cleanup();

/// 再次启用（例如重新进入录音房间）
// cleanup 之后需要完全重新初始化使用
var err = qiumingdll_volume_start(48000, 10);
if (err == 0)
{
    qiumingdll_volume_set_silence_threshold(0.01); // 恢复到需要的参数
    qiumingdll_volume_set_smoothing(0.3);
    volumeActive = true;
}
```

## 相关函数

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_stop](qiumingdll_volume_stop.md)
- [qiumingdll_volume_set_silence_threshold](qiumingdll_volume_set_silence_threshold.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)