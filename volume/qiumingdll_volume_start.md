# qiumingdll_volume_start(sampleRate, bufferMs)

打开系统默认麦克风并开始采集音量数据，返回 0 表示录音已成功开始。

## 函数签名

```gml
qiumingdll_volume_start(sampleRate, bufferMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| sampleRate | Real | 是 | 采样率（单位 Hz）。取值范围 8000~192000，超出范围会被自动钳制到边界值。推荐使用 48000（CD 音质），采样率越高精度越好，但内存和 CPU 消耗也越大 |
| bufferMs | Real | 是 | 缓冲时长（单位毫秒）。取值范围 5~100，超出范围会被自动钳制到边界值。缓冲越短音量刷新越快（延迟越低），缓冲越长资源占用越低但反应越迟钝，通常取 10 左右即可 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 成功：麦克风已打开，音量数据开始更新 |
| 1 | 失败：系统检测不到麦克风、设备被其他程序独占，或内部资源分配失败。**非 Windows 平台**的 GML 包装函数也会直接返回 1 |

## 使用说明

- 前置条件：需要先完成扩展的全局初始化流程，使 `global.__qiumingdll_volume_start` 指向 DLL 函数；否则包装函数直接返回 1。
- 平台限制：仅 Windows 可用。底层以 WAVE_MAPPER 打开系统**默认**麦克风，按单声道、16-bit PCM 格式采集，无法选择指定输入设备。
- 重复调用：若已在录音中，再次调用会先自动停止上一次会话，再按新参数重新开始，无需先手动调用 stop。
- 参数关联：sampleRate 与 bufferMs 共同决定每次采集的缓冲大小（约 sampleRate × bufferMs ÷ 1000 个样本，最小 64 个样本），两者均应取合理值，避免极端组合。
- 调用成功后，在游戏退出或不再需要麦克风时，务必调用 qiumingdll_volume_stop() 或 qiumingdll_volume_cleanup() 释放设备，否则其他程序将一直无法使用麦克风。
- 本模块与 pitch 模块共用系统麦克风；本模块的 Get 系列函数只有在 start 成功之后才能拿到有效数值。
- 典型用途：麦克风音量表、语音检测、卡拉 OK 音量条。

## 示例

```gml
/// 创建事件 (obj_mic_volume)
// 以 48kHz 采样率、10ms 缓冲打开系统默认麦克风
var err = qiumingdll_volume_start(48000, 10);
if (err == 0)
{
    volumeActive = true;  // 录音成功，可在 Step 事件中读取音量
}
else
{
    volumeActive = false; // 无麦克风或被占用，做降级处理
    show_debug_message("麦克风打开失败");
}

/// 房间结束事件
if (volumeActive)
{
    qiumingdll_volume_stop(); // 停止录音并释放麦克风
}
```

## 相关函数

- [qiumingdll_volume_stop](qiumingdll_volume_stop.md)
- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md)
- [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md)