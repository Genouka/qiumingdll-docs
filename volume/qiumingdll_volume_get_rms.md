# qiumingdll_volume_get_rms()

返回当前麦克风音量的均方根值（RMS），范围 0~1，数值已按平滑系数进行平滑处理，适合驱动音量条。

## 函数签名

```gml
qiumingdll_volume_get_rms()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 ~ 1 | 平滑后的均方根音量。0 表示无声，1 表示满刻度（输入信号达到 16-bit 满幅）。静音环境下数值会随时间回落并稳定在接近 0 的地方 |
| 0 | 未启动录音时返回 0；**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：必须先成功调用 qiumingdll_volume_start()，start 之前调用永远返回 0。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 平滑行为：返回值同时受 qiumingdll_volume_set_smoothing() 设置的平滑系数影响，系数越大对瞬时声音越敏感（数值跳动大），系数越小越平滑。
- 时效性：启动后需要约几十毫秒（几个缓冲周期）才能累积出有效数值；音量数值仅在录音进行中持续刷新。
- 典型用途：直接作为音量条的宽度/高度比例（乘以目标象素即可），或作为语音检测的输入。
- 提示：get_peak() 反映瞬时峰值、get_rms() 反映平均响度；做"语音是否在说话"的判断时通常用 rms 更稳定。
- 性能提示：本函数只读取一个内部数值，调用开销极小，可以在 Step 或 Draw 事件中每帧调用，不影响游戏性能。

## 示例

```gml
/// 绘制事件 (obj_mic_volume)
// 把 RMS 音量画成一条水平音量条
var rms = qiumingdll_volume_get_rms();
var barW = rms * 200; // 0~200 像素
draw_set_color(c_lime);
draw_rectangle(50, 50, 50 + barW, 60, false);

// 顺便输出数字便于调试
draw_set_color(c_white);
draw_text(50, 70, "RMS: " + string(rms));
```

## 相关函数

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_get_peak](qiumingdll_volume_get_peak.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)