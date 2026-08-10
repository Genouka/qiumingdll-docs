# volume 模块

麦克风音量检测：获取峰值（peak）、有效值（RMS）与分贝（dB），可设置静音阈值与平滑系数。

共 10 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md) | 彻底清理 volume 模块：停止录音、释放麦克风设备与全部内部资源，并把所有状态（含音量数值与参数设置）清零。 |
| [qiumingdll_volume_get_db](qiumingdll_volume_get_db.md) | 返回当前音量对应的分贝值（dB），范围约 -96 ~ 0，静音时稳定在 -96，适合直接用于专业的电平表显示。 |
| [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md) | 返回当前音量的离散等级，范围 0~5，按平滑后的 RMS 划分阈值区间，适合驱动简易的"格数"式音量指示器。 |
| [qiumingdll_volume_get_peak](qiumingdll_volume_get_peak.md) | 返回当前麦克风音量的峰值（Peak），范围 0~1，数值同样经过平滑处理，适合反映声音的瞬时强度。 |
| [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md) | 返回当前麦克风音量的均方根值（RMS），范围 0~1，数值已按平滑系数进行平滑处理，适合驱动音量条。 |
| [qiumingdll_volume_is_active](qiumingdll_volume_is_active.md) | 查询 volume 模块当前是否正在录音，返回 1 表示录音中、0 表示未启动。 |
| [qiumingdll_volume_set_silence_threshold](qiumingdll_volume_set_silence_threshold.md) | 设置静音判定阈值：平滑 RMS 低于该值的音频被判定为静音（get_level 返回 0）。默认值 0.01。 |
| [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md) | 设置音量平滑系数，控制 get_rms 与 get_peak 的平滑程度。默认值 0.3，系数越大越灵敏、越小越平滑。 |
| [qiumingdll_volume_start](qiumingdll_volume_start.md) | 打开系统默认麦克风并开始采集音量数据，返回 0 表示录音已成功开始。 |
| [qiumingdll_volume_stop](qiumingdll_volume_stop.md) | 停止麦克风录音并释放采集设备，同时把音量状态清零，但保留已设置的参数（静音阈值、平滑系数）。 |

[返回文档首页](../README.md)