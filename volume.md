# volume 模块

音量检测模块。通过麦克风输入实时检测音频的 RMS、峰值、分贝和音量等级。

## API

### qmVolumeStart

```c
QM_EXPORT QM_Real qmVolumeStart(QM_Real sampleRate, QM_Real bufferMs);
```

**参数：**
- `sampleRate` - 采样率（8000-192000，默认 48000）
- `bufferMs` - 缓冲区大小（5-100ms，默认 10ms）

**返回值：**
- `0` - 成功
- `1` - 失败

---

### qmVolumeStop

```c
QM_EXPORT QM_Real qmVolumeStop();
```

**返回值：** `0`

---

### qmVolumeGetRMS

```c
QM_EXPORT QM_Real qmVolumeGetRMS();
```

**返回值：** RMS 音量（0.0-1.0），经过平滑处理

---

### qmVolumeGetPeak

```c
QM_EXPORT QM_Real qmVolumeGetPeak();
```

**返回值：** 峰值音量（0.0-1.0），经过平滑处理

---

### qmVolumeGetDB

```c
QM_EXPORT QM_Real qmVolumeGetDB();
```

**返回值：** 分贝值（-96.0 到 0.0）

---

### qmVolumeGetLevel

```c
QM_EXPORT QM_Real qmVolumeGetLevel();
```

**返回值：** 音量等级（0-5）

| 等级 | RMS 范围 | 说明 |
|------|----------|------|
| 0 | < silenceThreshold | 静音 |
| 1 | < 0.05 | 低 |
| 2 | < 0.15 | 中低 |
| 3 | < 0.35 | 中 |
| 4 | < 0.60 | 中高 |
| 5 | >= 0.60 | 高 |

---

### qmVolumeGetIsActive

```c
QM_EXPORT QM_Real qmVolumeGetIsActive();
```

**返回值：**
- `1.0` - 正在运行
- `0.0` - 已停止

---

### qmVolumeSetSilenceThreshold

```c
QM_EXPORT QM_Real qmVolumeSetSilenceThreshold(QM_Real threshold);
```

**参数：**
- `threshold` - 静音阈值（0.0-0.5，默认 0.01）

---

### qmVolumeSetSmoothing

```c
QM_EXPORT QM_Real qmVolumeSetSmoothing(QM_Real smoothing);
```

**参数：**
- `smoothing` - 平滑系数（0.0-1.0，默认 0.3）

**说明：** 值越大响应越快，值越小越平滑

---

### qmVolumeCleanup

```c
QM_EXPORT QM_Real qmVolumeCleanup();
```

## 使用示例

```c
// 启动检测
qmVolumeStart(48000, 10);

// 轮询
if (qmVolumeGetIsActive()) {
    double rms = qmVolumeGetRMS();
    double peak = qmVolumeGetPeak();
    double db = qmVolumeGetDB();
    int level = qmVolumeGetLevel();
    
    // 根据音量等级控制游戏逻辑
    if (level >= 3) {
        // 音量足够大，触发游戏事件
    }
}

// 停止
qmVolumeStop();
```
