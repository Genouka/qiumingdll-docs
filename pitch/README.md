# pitch 模块

麦克风输入音高检测：获取当前频率、音名与音量，可用于唱歌游戏等玩法。

共 8 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md) | 彻底清理 pitch 模块：停止音高检测、释放麦克风设备与全部内部资源，并把所有状态（含检测结果与阈值参数）清零。 |
| [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md) | 返回当前检测到的声音基频（单位 Hz），范围为 20~20000；检测不到有效音高时返回 0。 |
| [qiumingdll_pitch_get_note](qiumingdll_pitch_get_note.md) | 返回当前检测到的音高对应的 MIDI 音符编号，60 代表中央 C，69 代表中央 A（440Hz）；检测不到时返回 -1。 |
| [qiumingdll_pitch_get_volume](qiumingdll_pitch_get_volume.md) | 返回 pitch 模块当前分析窗口内的输入音量（RMS），范围 0~1，用于判断当前是否有足够大的声音在进行音高检测。 |
| [qiumingdll_pitch_is_active](qiumingdll_pitch_is_active.md) | 查询 pitch 模块当前是否正在检测音高，返回 1 表示检测中、0 表示未启动。 |
| [qiumingdll_pitch_set_threshold](qiumingdll_pitch_set_threshold.md) | 设置 YIN 基频检测算法的阈值，控制音高检测的灵敏度。默认值 0.15。 |
| [qiumingdll_pitch_start](qiumingdll_pitch_start.md) | 打开系统默认麦克风并开始基频检测，返回 0 表示检测已成功开始。 |
| [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md) | 停止基频检测并释放采集设备，同时把检测结果清零，但保留已设置的 YIN 阈值参数。 |

[返回文档首页](../README.md)