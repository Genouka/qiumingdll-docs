# qiumingdll_volume_get_peak()

返回当前麦克风音量的峰值（Peak），范围 0~1，数值同样经过平滑处理，适合反映声音的瞬时强度。

## 函数签名

```gml
qiumingdll_volume_get_peak()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 ~ 1 | 平滑后的峰值音量。0 表示无声，1 表示信号达到 16-bit 满幅。击掌声、敲击等短促强音会让峰值明显高于同一时刻的 RMS |
| 0 | 未启动录音时返回 0；**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：必须先成功调用 qiumingdll_volume_start()，start 之前调用永远返回 0。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 平滑行为：返回值同样受 qiumingdll_volume_set_smoothing() 平滑系数影响，且与 RMS 使用同一平滑系数。
- 与 get_rms 的关系：同一段音频里 peak 一般大于等于 rms；峰值能更快反映突发音量，RMS 更能代表持续响度。做"卡拉 OK 条"时常用 peak 表现"闪动"效果。
- 时效性：仅在录音进行中持续刷新，start 后约几十毫秒开始有有效数值。
- 性能提示：本函数只读取一个内部数值，调用开销极小，每帧调用无压力；与 get_rms 一起读取时便于做双条（绿=RMS、黄=Peak）经典电平表。
- 提示：若想显示"瞬时峰值保持"效果，可以自己在 GML 侧记录本帧峰值的历史最大值，并随时间缓慢衰减。

## 示例

```gml
/// Step 事件 (obj_voice_detect)
// 用峰值检测"突然的大声"，触发提示
var peak = qiumingdll_volume_get_peak();
if (peak > 0.8)
{
    // 音量过大提示
    draw_loudWarning = 1;
}

/// 绘制事件
// 峰值条（红色）与 RMS 条（绿色）叠加对比
var p = qiumingdll_volume_get_peak();
var r = qiumingdll_volume_get_rms();
draw_set_color(c_red);
draw_rectangle(50, 100, 50 + p * 200, 110, false);
draw_set_color(c_green);
draw_rectangle(50, 115, 50 + r * 200, 125, false);
```

## 相关函数

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)