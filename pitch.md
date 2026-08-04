# pitch 模块

音高检测模块。通过麦克风输入实时检测音频的频率、音量和音符。

## 技术原理

- 使用 Windows MME (`waveIn`) API 采集音频
- 采用 YIN 算法进行基频检测
- 支持 MIDI 音符转换

## API

### qmPitchStart

```c
QM_EXPORT QM_Real qmPitchStart(QM_Real sampleRate, QM_Real bufferMs);
```

**参数：**
- `sampleRate` - 采样率（8000-192000，默认 48000）
- `bufferMs` - 缓冲区大小（5-100ms，默认 10ms）

**返回值：**
- `0` - 成功
- `1` - 失败

**说明：**
- 启动麦克风录音和音高检测线程
- 自动管理音频缓冲区

---

### qmPitchStop

```c
QM_EXPORT QM_Real qmPitchStop();
```

**返回值：** `0`

**说明：** 停止录音和检测

---

### qmPitchGetFrequency

```c
QM_EXPORT QM_Real qmPitchGetFrequency();
```

**返回值：** 当前检测到的频率（Hz），无检测结果时返回 0

---

### qmPitchGetVolume

```c
QM_EXPORT QM_Real qmPitchGetVolume();
```

**返回值：** 当前音量（RMS），范围 0.0-1.0

---

### qmPitchGetNote

```c
QM_EXPORT QM_Real qmPitchGetNote();
```

**返回值：** MIDI 音符编号（0-127），无检测结果时返回 -1

**MIDI 音符对照：**
- 60 = C4 (Middle C)
- 69 = A4 (440Hz)

---

### qmPitchGetIsActive

```c
QM_EXPORT QM_Real qmPitchGetIsActive();
```

**返回值：**
- `1.0` - 正在运行
- `0.0` - 已停止

---

### qmPitchSetThreshold

```c
QM_EXPORT QM_Real qmPitchSetThreshold(QM_Real threshold);
```

**参数：**
- `threshold` - 检测阈值（0.01-0.99，默认 0.15）

**说明：** 值越小越敏感，值越大越严格

---

### qmPitchCleanup

```c
QM_EXPORT QM_Real qmPitchCleanup();
```

**说明：** 清理所有资源

## 使用示例

```c
// 启动检测（48kHz，10ms 缓冲）
qmPitchStart(48000, 10);

// 轮询检测结果
if (qmPitchGetIsActive()) {
    double freq = qmPitchGetFrequency();
    double vol = qmPitchGetVolume();
    int note = qmPitchGetNote();
    
    if (freq > 0) {
        // 处理检测到的音高
    }
}

// 停止检测
qmPitchStop();
```
