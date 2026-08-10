# qiumingdll_volume_is_active()

查询 volume 模块当前是否正在录音，返回 1 表示录音中、0 表示未启动。

## 函数签名

```gml
qiumingdll_volume_is_active()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 正在录音：qiumingdll_volume_start() 已成功且尚未停止 |
| 0 | 未在录音：start 未调用或已失败、已调用 qiumingdll_volume_stop()/qiumingdll_volume_cleanup()。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：无，任何时刻都可安全调用。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 用途：在调用 Get 系列函数前先用它做守卫，避免在未启动时读取无效数据；也可用来做运行时的"麦克风开关"状态显示。
- 行为细节：start 成功返回 0 后，is_active 立即变为 1；stop 或 cleanup 被调用后立即变回 0。重复调用 start 不会影响该状态（始终为 1）。
- 提示：is_active 为 1 只能说明"设备已打开、正在采集"，并不代表一定检测到了声音，声音有无要看 get_rms / get_level。

## 示例

```gml
/// Step 事件 (obj_mic_controller)
// 每帧检查录音状态，意外停止时自动恢复
if (micWanted && qiumingdll_volume_is_active() == 0)
{
    // 录音意外停止（例如被 stop 调用），按需重新开启
    qiumingdll_volume_start(48000, 10);
}

/// Draw GUI 事件
// 显示当前状态文字
if (qiumingdll_volume_is_active() == 1)
{
    draw_text(10, 10, "麦克风状态：录音中");
}
else
{
    draw_text(10, 10, "麦克风状态：未启动");
}
```

## 相关函数

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_stop](qiumingdll_volume_stop.md)
- [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md)