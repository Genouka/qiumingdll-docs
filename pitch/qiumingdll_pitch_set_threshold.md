# qiumingdll_pitch_set_threshold(threshold)

设置 YIN 基频检测算法的阈值，控制音高检测的灵敏度。默认值 0.15。

## 函数签名

```gml
qiumingdll_pitch_set_threshold(threshold)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| threshold | Real | 是 | YIN 检测阈值（无单位）。取值范围 0.01~0.99，超出范围会被自动钳制到边界值；默认 0.15。阈值越小对"非周期信号"越挑剔（更难误判、但弱信号可能检测不到）；阈值越大越容易锁定一个周期（对噪声/含混的信号更容易给出结果，但可能误判音高） |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 设置成功（阈值已保存并立即生效）。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：无。可在 start 之前或之后调用，检测进行中修改也会在下一次分析中生效。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0，不产生效果）。
- 生效范围：仅影响 pitch 模块的 YIN 算法判定；volume 模块不受影响，其静音阈值需通过 qiumingdll_volume_set_silence_threshold() 设置。
- 行为细节：YIN 阈值决定"累积均值归一化差"低于多少才算找到周期。阈值过低时，轻微失真的输入会导致检测失败（get_frequency 返回 0）；阈值过高时，噪声也可能被当作音高。
- 持久性：该参数在 stop() 后仍然保留，直到再次调用本函数修改，或执行全局清理流程重置为默认值 0.15。
- 使用建议：干净的乐器信号可用 0.1~0.15；嘈杂环境或歌唱场景可适当调高（0.2~0.3）；需要严格判定"只有清晰音符才算"时可调低（0.05~0.1）。
- 与输入音量的关系：本阈值只影响"周期是否可信"的判定；不论阈值如何，输入音量过低时检测都会被跳过（get_frequency 返回 0），两者互不替代。
- 调试建议：让玩家对着麦克风唱稳定长音，逐步调大阈值直到偶尔出现错误音高，再回调一点，即为当前环境的合适值。

## 示例

```gml
/// 创建事件 (obj_tuner)
qiumingdll_pitch_start(48000, 10);
qiumingdll_pitch_set_threshold(0.15); // 默认灵敏度

/// Step 事件
// 根据界面滑杆（0~1）实时调节检测灵敏度
// 滑杆 0 → 最严格(0.05)，滑杆 1 → 最宽松(0.3)
var t = lerp(0.05, 0.30, sensitivitySlider);
qiumingdll_pitch_set_threshold(t);

// 灵敏度低时容易"无结果"，给玩家反馈
if (qiumingdll_pitch_get_frequency() == 0 && qiumingdll_pitch_get_volume() > 0.1)
{
    drawHint = "没听清，请更清晰地发声或调高灵敏度";
}
```

## 相关函数

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)