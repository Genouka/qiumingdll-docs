# qiumingdll_procdetect_streaming()

检测当前系统中是否存在常见直播/录屏软件进程（如 OBS、Streamlabs 等），用于判断游戏是否正在被串流或录制。

## 函数签名

```gml
qiumingdll_procdetect_streaming()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 检测到直播/录屏类软件进程正在运行 |
| 0 | 未检测到，或非 Windows 平台 / 未初始化（此时返回 0） |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows。
- 行为细节：通过预设的常见串流/录制软件进程名列表匹配，可用于在直播期间调整画面内容（如隐藏彩蛋、替换贴图）等场景。
- 注意：该函数只能按已知进程名匹配，无法保证覆盖所有第三方直播工具；检测结果只代表调用时刻的状态。

## 示例

```gml
/// 步进事件
if (qiumingdll_procdetect_streaming())
{
    // 正在直播：隐藏未公开内容
    surprise_content.visible = false;
}
else
{
    surprise_content.visible = true;
}
```

## 相关函数

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)