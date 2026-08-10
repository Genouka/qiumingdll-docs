# qiumingdll_volume_get_db()

返回当前音量对应的分贝值（dB），范围约 -96 ~ 0，静音时稳定在 -96，适合直接用于专业的电平表显示。

## 函数签名

```gml
qiumingdll_volume_get_db()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| -96 ~ 0 | 当前音量的分贝值（单位 dB），由平滑后的 RMS 换算而来（20 × log10(RMS)）。0 dB 为 16-bit 满幅信号 |
| -96 | 静音（RMS 低于阈值）时返回 -96，是分贝换算的下限值；未启动录音时同样返回 -96 |
| 0 | **非 Windows 平台**的 GML 包装函数直接返回 0（注意与静音时的 -96 区分） |

## 使用说明

- 前置条件：必须先成功调用 qiumingdll_volume_start()，start 之前调用返回 -96。
- 平台限制：仅 Windows 有效。
- 与其它 Get 函数的关系：get_db 由 get_rms 的平滑结果换算而来，二者数值完全同步，只是显示单位不同；分贝刻度更符合专业音频设备的习惯（如 -60dB 以下视为静音）。
- 时效性：仅在录音进行中持续刷新，start 后约几十毫秒开始有有效数值。
- 提示：人声交谈通常在 -40 ~ -10 dB 之间；若常常低于 -50 dB，说明麦克风输入太小，需要调大系统输入增益。
- 换算关系：0 dB 对应 RMS=1（16-bit 满幅），-6 dB 对应 RMS≈0.5，-20 dB 对应 RMS≈0.1；分贝值越大声音越大。
- 显示建议：直接在 Draw GUI 事件中读取即可，数值本身已平滑，无需再做插值动画。

## 示例

```gml
/// 绘制事件 (obj_audio_meter)
// 专业风格的分贝表：将 -96~0 dB 映射到 0~300 像素高度
var db = qiumingdll_volume_get_db();
var h = (db + 96) / 96 * 300; // -96dB 对应 0px，0dB 对应 300px
draw_set_color(c_orange);
draw_rectangle(200, 400, 220, 400 - h, false);

// 显示数值，保留 1 位小数
draw_set_color(c_white);
draw_text(230, 380, string_format(db, 1, 1) + " dB");
```

## 相关函数

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md)