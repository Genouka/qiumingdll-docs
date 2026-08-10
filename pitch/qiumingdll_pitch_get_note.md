# qiumingdll_pitch_get_note()

返回当前检测到的音高对应的 MIDI 音符编号，60 代表中央 C，69 代表中央 A（440Hz）；检测不到时返回 -1。

## 函数签名

```gml
qiumingdll_pitch_get_note()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 12 ~ 135 | 检测到的 MIDI 音符编号（按 69 + 12 × log2(f / 440) 由基频换算而来）。常用参考：60 = 中央 C（C4，约 261.6Hz）、69 = A4（440Hz）、72 = C5（高音 C）；每增大 1 表示升半音 |
| -1 | 未检测到有效音高（静音、噪声、无稳定周期信号），或未启动检测时。**非 Windows 平台**的 GML 包装函数也直接返回 -1 |
| 其他 | 理论可返回的范围随频率换算约为 12~135，但实际只有检测成功（get_frequency 在 20~20000Hz 之间）时才会产生音符编号 |

## 使用说明

- 前置条件：必须先成功调用 qiumingdll_pitch_start()，start 之前调用返回 -1。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 -1）。
- 用法：用 -1 判断"有没有检测到音"，用编号与目标谱面音符做相等或相近判断，实现音游/卡拉 OK 判定；同一音符的轻微走音不会改变编号，需要精细走音判断时请改用 get_frequency 计算音分偏差。
- 与音符名称的换算：MIDI 编号对 12 取模可得音名（0=C, 1=C#, 2=D, ... 11=B），编号除以 12 减 1 可得八度（如 60 → 音名 C、八度 4，即 C4 中央C）。
- 时效性：与 get_frequency 在同一分析周期内同步更新，检测停止后立即回到 -1。

## 示例

```gml
/// Step 事件 (obj_piano_lesson)
// 读取当前音符编号，并与谱面目标音符比较
var targetNote = 60; // 目标：中央 C
var note = qiumingdll_pitch_get_note();
if (note == -1)
{
    statusText = "等待发声……";
}
else if (note == targetNote)
{
    statusText = "唱对了！中央 C";
    score += 1;
}
else if (note > targetNote)
{
    statusText = "偏高 " + string(note - targetNote) + " 个半音";
}
else
{
    statusText = "偏低 " + string(targetNote - note) + " 个半音";
}

/// Draw GUI 事件
draw_set_color(c_white);
draw_text(10, 10, statusText);
draw_text(10, 30, "音符编号: " + string(note));
```

## 相关函数

- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_is_active](qiumingdll_pitch_is_active.md)