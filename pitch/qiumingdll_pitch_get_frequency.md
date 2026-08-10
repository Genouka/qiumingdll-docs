# qiumingdll_pitch_get_frequency()

返回当前检测到的声音基频（单位 Hz），范围为 20~20000；检测不到有效音高时返回 0。

## 函数签名

```gml
qiumingdll_pitch_get_frequency()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 20 ~ 20000 | 当前检测到的基频（单位 Hz）。人声歌唱通常在 80~1100 Hz 范围内；A4 标准音为 440 Hz，中央 C（C4）约为 261.6 Hz |
| 0 | 未检测到有效音高：没有稳定周期信号（静音、噪声、太轻的声音），或未启动检测时。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：必须先成功调用 qiumingdll_pitch_start()，start 之前调用返回 0。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 检测条件：只有当输入音量（RMS）不低于内部音量门槛时才会进行基频分析；静音或环境噪声下返回 0。可通过 qiumingdll_pitch_set_threshold() 调节 YIN 算法的灵敏度。
- 时效性：仅检测进行中持续刷新，start 后需要约几十毫秒（积累足够分析窗口样本）才产生首个有效结果。
- 与 get_note 的关系：get_frequency 是换算成 MIDI 音符前的原始频率值；两者在同一分析周期内同步更新，应优先用音符编号（get_note）做"准不准确"判定，用频率做音高曲线绘制。
- 典型用途：歌唱音高计、乐器调音器、音高训练游戏。

## 示例

```gml
/// Step 事件 (obj_tuner)
// 读取当前基频，并转换为与目标音高的偏差（音分）
var f = qiumingdll_pitch_get_frequency();
if (f > 0)
{
    // 目标音 A4 = 440Hz，计算偏差音分（cents）
    var cents = 1200 * log2(f / 440.0);
    // 偏差在 ±20 音分内视为"准了"
    inTune = abs(cents) < 20;
}
else
{
    inTune = false; // 没有检测到音
}

/// Draw GUI 事件
if (f > 0 && inTune)
{
    draw_set_color(c_lime);
    draw_text(10, 10, "A4 调准！当前频率：" + string(f) + " Hz");
}
else
{
    draw_set_color(c_white);
    draw_text(10, 10, "请对着麦克风唱 A4 (440Hz)……");
}
```

## 相关函数

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_get_note](qiumingdll_pitch_get_note.md)
- [qiumingdll_pitch_get_volume](qiumingdll_pitch_get_volume.md)