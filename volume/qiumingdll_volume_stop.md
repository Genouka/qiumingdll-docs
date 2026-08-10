# qiumingdll_volume_stop()

停止麦克风录音并释放采集设备，同时把音量状态清零，但保留已设置的参数（静音阈值、平滑系数）。

## 函数签名

```gml
qiumingdll_volume_stop()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 已停止录音，设备已释放。**非 Windows 平台**的 GML 包装函数同样直接返回 0 |

## 使用说明

- 前置条件：无需先调用 start；即使当前未在录音，调用也是安全的（无副作用）。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0，不做任何事）。
- 与 cleanup 的区别：stop 只停止录音、释放麦克风并把音量数值清零，**不会**改变通过 qiumingdll_volume_set_silence_threshold() 和 qiumingdll_volume_set_smoothing() 设置的参数。调用 stop 后再次调用 qiumingdll_volume_start() 时，音量会从清零状态重新开始累积。
- 停止后各 Get 函数的状态：get_rms、get_peak 返回 0，get_db 返回 -96，get_level 返回 0，is_active 返回 0。
- 建议在游戏退出、切场景或不再需要麦克风时调用，及时释放设备资源，避免影响系统中其他需要使用麦克风的程序。
- 本模块与 pitch 模块独立；本函数只影响 volume 模块，不影响 pitch 模块的检测。
- 注意：stop 之后 Get 系列函数全部回到"未启动"形态的值（rms/peak/level 为 0、db 为 -96），若界面仍显示音量条，请一并隐藏或清空，避免误导。

## 示例

```gml
/// 键盘事件 (Enter)
// 按回车停止录音，模拟"静音开关"
if (qiumingdll_volume_is_active() == 1)
{
    qiumingdll_volume_stop(); // 停止后麦克风被释放
    micOn = false;
}
else
{
    qiumingdll_volume_start(48000, 10); // 重新开始录音
    micOn = true;
}

/// 房间结束事件
if (qiumingdll_volume_is_active() == 1)
{
    qiumingdll_volume_stop(); // 退出房间前停止录音
}
```

## 相关函数

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_is_active](qiumingdll_volume_is_active.md)
- [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md)