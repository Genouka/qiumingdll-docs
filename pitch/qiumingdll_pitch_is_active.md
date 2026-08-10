# qiumingdll_pitch_is_active()

查询 pitch 模块当前是否正在检测音高，返回 1 表示检测中、0 表示未启动。

## 函数签名

```gml
qiumingdll_pitch_is_active()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 检测中：qiumingdll_pitch_start() 已成功且尚未停止 |
| 0 | 未在检测：start 未调用或已失败、已调用 qiumingdll_pitch_stop()/qiumingdll_pitch_cleanup()。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：无，任何时刻都可安全调用。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 用途：在读取 get_frequency / get_note 之前用它做守卫，避免把"未启动"与"检测不到音"混淆（未启动时 get_note 同样返回 -1）。
- 行为细节：start 成功返回 0 后，is_active 立即变为 1；stop 或 cleanup 被调用后立即变回 0。重复调用 start 不会影响该状态（始终为 1）。
- 提示：is_active 为 1 只代表"检测流程在运行"，并不代表一定检测到了音高，有没有音要看 get_frequency / get_note 是否返回有效值。

## 示例

```gml
/// Step 事件 (obj_pitch_controller)
// 检测意外停止时自动重启
if (wantDetect && qiumingdll_pitch_is_active() == 0)
{
    qiumingdll_pitch_start(22050, 10); // 恢复检测（低采样率更利于低音）
}

/// 绘制事件
// 显示检测状态与当前音符
if (qiumingdll_pitch_is_active() == 1)
{
    var note = qiumingdll_pitch_get_note();
    if (note == -1)
        draw_text(10, 10, "检测中……（无音高）");
    else
        draw_text(10, 10, "检测中，音符 = " + string(note));
}
else
{
    draw_text(10, 10, "未启动");
}
```

## 相关函数

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)