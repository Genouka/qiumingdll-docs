# qiumingdll_pitch_stop()

停止基频检测并释放采集设备，同时把检测结果清零，但保留已设置的 YIN 阈值参数。

## 函数签名

```gml
qiumingdll_pitch_stop()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 已停止检测，设备已释放。**非 Windows 平台**的 GML 包装函数同样直接返回 0 |

## 使用说明

- 前置条件：无需先调用 start；即使当前未在检测，调用也是安全的（无副作用）。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0，不做任何事）。
- 与 cleanup 的区别：stop 只停止检测、释放麦克风并把检测结果清零，**不会**改变通过 qiumingdll_pitch_set_threshold() 设置的 YIN 阈值。调用 stop 后再次调用 qiumingdll_pitch_start()，阈值会沿用之前的值。
- 停止后的状态：get_frequency 返回 0，get_volume 返回 0，get_note 返回 -1，is_active 返回 0。
- 建议在游戏退出、切场景或不再需要音高检测时调用，及时释放设备资源。
- 本模块与 volume 模块独立；本函数只影响 pitch 模块，不影响 volume 模块的录音。
- 注意：stop 之后 Get 系列函数全部回到"未启动"形态的值（frequency 为 0、volume 为 0、note 为 -1）；若界面上仍在显示音高，请一并清空或隐藏，避免把"停止状态"误当"检测不到音"。

## 示例

```gml
/// 键盘事件 (Space)
// 空格键切换音高检测开关
if (qiumingdll_pitch_is_active() == 1)
{
    qiumingdll_pitch_stop(); // 关闭检测
    detectOn = false;
}
else
{
    qiumingdll_pitch_start(48000, 10); // 重新开启
    detectOn = true;
}

/// 房间结束事件
if (qiumingdll_pitch_is_active() == 1)
{
    qiumingdll_pitch_stop(); // 离开房间前停止检测
}
```

## 相关函数

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_is_active](qiumingdll_pitch_is_active.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)