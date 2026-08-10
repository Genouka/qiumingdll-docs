# qiumingdll_pitch_start(sampleRate, bufferMs)

打开系统默认麦克风并开始基频检测，返回 0 表示检测已成功开始。

## 函数签名

```gml
qiumingdll_pitch_start(sampleRate, bufferMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| sampleRate | Real | 是 | 采样率（单位 Hz）。取值范围 8000~192000，超出范围会被自动钳制到边界值。推荐使用 48000（CD 音质）；采样率越高，可检测的音高范围与精度越好，但 CPU 消耗越大 |
| bufferMs | Real | 是 | 缓冲时长（单位毫秒）。取值范围 5~100，超出范围会被自动钳制到边界值。缓冲越短检测更新越快（延迟越低），缓冲越长越省资源但音高刷新越迟钝，通常取 10 左右即可 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 成功：麦克风已打开，音高数据开始更新 |
| 1 | 失败：系统检测不到麦克风、设备被其他程序独占，或内部资源分配失败。**非 Windows 平台**的 GML 包装函数也会直接返回 1 |

## 使用说明

- 前置条件：需要先完成扩展的全局初始化流程，使 `global.__qiumingdll_pitch_start` 指向 DLL 函数；否则包装函数直接返回 1。
- 平台限制：仅 Windows 可用。底层以 WAVE_MAPPER 打开系统**默认**麦克风，按单声道、16-bit PCM 格式采集，无法选择指定输入设备。
- 检测原理：使用 YIN 算法对采集到的音频进行基频检测，结果通过 get_frequency / get_note 读取。
- 重复调用：若已在检测中，再次调用会先自动停止上一次会话，再按新参数重新开始。
- 参数关联：sampleRate 与 bufferMs 共同决定每次采集的缓冲大小（约 sampleRate × bufferMs ÷ 1000 个样本，最小 64 个样本）；音高检测的分析窗口约 2048 个样本，采样率越高该窗口覆盖的时间越短，对低频音（如男低音）的检测越不利，追求低音检测时建议降低采样率（如 22050）。
- 本模块与 volume 模块共用系统麦克风；本模块的 Get 系列函数只有在 start 成功之后才能拿到有效数值。
- 典型用途：歌声音高显示、乐器调音器、音游判定。

## 示例

```gml
/// 创建事件 (obj_voice_pitch)
// 以 48kHz 采样率、10ms 缓冲开始音高检测
var err = qiumingdll_pitch_start(48000, 10);
if (err == 0)
{
    pitchActive = true; // 检测成功，可在 Step 中读取音高
}
else
{
    pitchActive = false;
    show_debug_message("音高检测启动失败");
}

/// 房间结束事件
if (pitchActive)
{
    qiumingdll_pitch_stop(); // 停止检测并释放麦克风
}
```

## 相关函数

- [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md)
- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_get_note](qiumingdll_pitch_get_note.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)