# qiumingdll_volume_get_level()

返回当前音量的离散等级，范围 0~5，按平滑后的 RMS 划分阈值区间，适合驱动简易的"格数"式音量指示器。

## 函数签名

```gml
qiumingdll_volume_get_level()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 静音：平滑 RMS 低于静音阈值（默认 0.01，可通过 qiumingdll_volume_set_silence_threshold 调整） |
| 1 | RMS 不小于静音阈值且小于 0.05，极轻的声音 |
| 2 | RMS 在 0.05 ~ 0.15 之间，轻声说话 |
| 3 | RMS 在 0.15 ~ 0.35 之间，正常说话音量 |
| 4 | RMS 在 0.35 ~ 0.6 之间，比较大声 |
| 5 | RMS 达到 0.6 以上，最大音量档 |
| 0 | 未启动录音时返回 0；**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：必须先成功调用 qiumingdll_volume_start()，start 之前调用返回 0。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 阈值分段：等级划分基于每次分析窗口（约 1024 个样本）内平滑后的 RMS，分段如下——低于静音阈值 = 0；< 0.05 = 1；< 0.15 = 2；< 0.35 = 3；< 0.6 = 4；其余 = 5。
- 与静音阈值联动：通过 qiumingdll_volume_set_silence_threshold() 提高静音阈值后，原本返回 1 的轻音会变成 0（静音）。
- 典型用途：手机通话栏式音量格、卡拉 OK 伴奏跟唱指示、语音活动检测。

## 示例

```gml
/// 绘制事件 (obj_level_meter)
// 用 5 格彩条显示音量等级（0~5）
var lvl = qiumingdll_volume_get_level();
for (var i = 0; i < 5; i++)
{
    // 点亮第 i 格
    if (i < lvl)
    {
        draw_set_color(lvl >= 5 ? c_red : c_yellow);
        draw_rectangle(50 + i * 26, 200, 70 + i * 26, 220, false);
    }
    else
    {
        draw_set_color(c_gray);
        draw_rectangle(50 + i * 26, 200, 70 + i * 26, 220, true);
    }
}

/// Step 事件
// 等级 = 0 且正在录音时认为是"没人在说话"
if (qiumingdll_volume_is_active() == 1 && qiumingdll_volume_get_level() == 0)
{
    silenceFrames += 1;
}
else
{
    silenceFrames = 0;
}
```

## 相关函数

- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_set_silence_threshold](qiumingdll_volume_set_silence_threshold.md)
- [qiumingdll_volume_start](qiumingdll_volume_start.md)