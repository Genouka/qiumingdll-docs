# qiumingdll_volume_set_silence_threshold(threshold)

设置静音判定阈值：平滑 RMS 低于该值的音频被判定为静音（get_level 返回 0）。默认值 0.01。

## 函数签名

```gml
qiumingdll_volume_set_silence_threshold(threshold)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| threshold | Real | 是 | 静音阈值（无单位，对应 0~1 的归一化 RMS 音量）。取值范围 0~0.5，超出范围会被自动钳制到边界值；默认 0.01。值越大越容易判定为静音（对轻微环境噪声越不敏感），值越小越灵敏 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 设置成功（阈值已保存并立即生效）。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：无。可在 start 之前或之后调用，录音进行中修改也会立即生效。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0，不产生效果）。
- 生效范围：仅影响 get_level() 的 0 级判定（RMS 低于阈值 = 等级 0）；get_rms / get_peak / get_db 不受影响。
- 参数关联：若把静音阈值设置得高于 0.05，原本划分为等级 1 的声音都会被归入等级 0（静音）。
- 持久性：该参数在 stop() 后仍然保留，直到再次调用本函数修改，或执行全局清理流程重置为默认值。
- 使用建议：环境噪声较大时适当调高（如 0.02~0.05），需要捕捉很轻的声音时调低（如 0.005）。
- 与 get_level 的联动提醒：本阈值只影响 get_level 的 0 级判定，且若静音阈值被调得大于 0.05，等级 1 将永远不会出现。
- 调试建议：先在 Start 后用 get_rms 观察环境底噪数值，再把阈值设为此数值的 1.5~2 倍，可得到较理想的静音判定。

## 示例

```gml
/// 创建事件 (obj_voice_detect)
// 根据不同环境动态设置静音阈值
qiumingdll_volume_set_silence_threshold(0.01); // 安静环境，默认值
micSensitivity = 0.5; // 0~1 灵敏度滑杆，供玩家调节

/// Step 事件
// 按灵敏度滑杆换算阈值：0 最灵敏(0.0) ~ 1 最迟钝(0.3)
var t = lerp(0.0, 0.3, micSensitivity);
qiumingdll_volume_set_silence_threshold(t);

// 判断是否有人在说话（无视轻微底噪）
var talking = qiumingdll_volume_get_level() > 0;
```

## 相关函数

- [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md)
- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)