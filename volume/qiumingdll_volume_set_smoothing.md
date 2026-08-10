# qiumingdll_volume_set_smoothing(smoothing)

设置音量平滑系数，控制 get_rms 与 get_peak 的平滑程度。默认值 0.3，系数越大越灵敏、越小越平滑。

## 函数签名

```gml
qiumingdll_volume_set_smoothing(smoothing)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| smoothing | Real | 是 | 平滑系数（无单位）。取值范围 0~1，超出范围会被自动钳制到边界值；默认 0.3。取值越大，新数据权重越高（对声音变化越灵敏、数值跳动越大）；取值越小，历史数据权重越高（数值越平滑圆润、反应越迟钝） |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 设置成功（系数已保存并立即生效）。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：无。可在 start 之前或之后调用，录音进行中修改也会立即生效（从下一次分析更新开始体现）。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0，不产生效果）。
- 生效范围：影响 get_rms() 与 get_peak() 两个返回值的平滑处理，两者共用同一系数；get_db 由平滑后的 RMS 换算，因此也间接受影响；get_level 基于平滑后的 RMS 分段，同样间接受影响。
- 行为细节：系数为 1 时几乎不做平滑（完全跟随瞬时值）；为 0 时数值几乎不再变化（保持初始值），一般不推荐取 0。
- 持久性：该参数在 stop() 后仍然保留，直到再次调用本函数修改，或执行全局清理流程重置为默认值。
- 使用建议：做音量条动画时 0.3 左右较自然；需要快速响应（对嘴形、音频可视化）可调大；需要稳定读数（语音检测逻辑）可调小。
- 与音量的关系：平滑处理是指数式加权（新数据 × 系数 + 旧值 × (1 - 系数)），因此数值总是向当前音量"追"而不是瞬间跳跃，过度响应和过度平滑之间没有绝对正确值，请按玩法手感调整。
- 评估方法：在设置界面提供滑杆并实时调用本函数，边唱边听/看音量条的表现即可快速找到手感。

## 示例

```gml
/// 创建事件 (obj_mic_volume)
qiumingdll_volume_start(48000, 10);

/// Step 事件
// 根据玩家设置动态调整平滑系数（0.1 平滑 ~ 0.9 灵敏）
qiumingdll_volume_set_smoothing(ui_smoothSliderValue); // 假设滑杆值在 0.1~0.9 之间

// 供绘制事件使用的平滑音量
smoothedRms = qiumingdll_volume_get_rms();

/// 绘制事件
// 用平滑系数较小的读数画主音量条，避免疯狂抖动
draw_set_color(c_lime);
draw_rectangle(50, 50, 50 + smoothedRms * 300, 60, false);
```

## 相关函数

- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_get_peak](qiumingdll_volume_get_peak.md)
- [qiumingdll_volume_start](qiumingdll_volume_start.md)