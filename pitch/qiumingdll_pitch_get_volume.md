# qiumingdll_pitch_get_volume()

返回 pitch 模块当前分析窗口内的输入音量（RMS），范围 0~1，用于判断当前是否有足够大的声音在进行音高检测。

## 函数签名

```gml
qiumingdll_pitch_get_volume()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 ~ 1 | 当前分析窗口内的均方根音量（RMS）。1 表示信号达到 16-bit 满幅；正常歌唱通常在 0.05~0.5 之间 |
| 0 | 未启动检测时返回 0；**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：必须先成功调用 qiumingdll_pitch_start()，start 之前调用返回 0。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 与 volume 模块的区别：volume 模块有独立的平滑处理与静音阈值设置，而本函数的音量是 pitch 模块每次检测分析窗口（约 2048 个样本）内直接计算的 RMS，未做平滑，反映的是"检测当下"的输入强度。
- 与检测结果的关联：音量低于内部门槛（约 0.01）时，检测会被跳过，get_frequency 返回 0、get_note 返回 -1；因此可以用本函数判断"返回 0 是因为没声音还是没有音高"。
- 典型用途：判断玩家是否真的在发声（避免安静时误判音高）、控制调音界面的提示闪烁。

## 示例

```gml
/// Step 事件 (obj_singing_game)
// 组合判断：先看音量够不够，再看音高
var vol = qiumingdll_pitch_get_volume();
if (vol < 0.05)
{
    // 音量太低：提示玩家靠近麦克风
    hintText = "太安静了，请大声唱！";
}
else
{
    var f = qiumingdll_pitch_get_frequency();
    if (f > 0)
    {
        hintText = "正在检测音高：" + string(f) + " Hz";
    }
    else
    {
        hintText = "有声音但没有稳定音高（试试长音）";
    }
}
```

## 相关函数

- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_set_threshold](qiumingdll_pitch_set_threshold.md)