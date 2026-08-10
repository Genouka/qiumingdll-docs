# qiumingdll_procdetect_streaming()

检测系统进程中是否存在录屏与直播软件，用于保护剧情内容或提示录制状态。

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
| 1 | 检测到至少一个录屏/直播软件进程在运行 |
| 0 | 未检测到任何目标进程，或非 Windows 平台调用 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台固定返回 0。
- 行为细节：内部遍历系统进程快照，按进程名（大小写不敏感，精确匹配 exe 文件名）逐一比对内置名单，命中任何一个即返回 1。内置名单包括：
  - 直播推流软件：OBS Studio（obs64.exe、obs32.exe、obs.exe）、XSplit（xsplit.core.exe、xsplit.gamecaster.exe）、Streamlabs OBS（streamlabs obs.exe、streamlabsobs.exe、sl.exe）、vMix（vmix64.exe、vMix.exe）、Wirecast（wirecast.exe）等；
  - 录屏软件：Bandicam（bandicam.exe）、Fraps（fraps.exe）、Mirillis Action（action.exe、action!.exe、mirillis_action.exe）、ShareX（sharex.exe）、Camtasia（camtasia.exe、camrec.exe）、Dxtory（dxtory.exe）、ocam（ocam.exe、ocam_capture.exe）等；
  - 显卡内录：NVIDIA ShadowPlay / GeForce Experience（shadowplay.exe、nvidia share.exe、gamecapture.exe、nvcontainer.exe）等；
  - 转流连接工具：livestreamer.exe、streamlink.exe、mediasourcehelper.exe 等。
- 检测方式是"按名单比对进程名"，只对名单内软件的**默认可执行文件名**有效；改名后可能检测不到，同时可能误报同名进程。
- 注意：本函数不做任何阻止动作，仅返回检测结果。
- 典型用途：剧情向游戏在检测到录制时暂停播放未公开内容、显示"请勿录制"提示，或按需求调整画面输出。

## 示例

```gml
// 剧情关键片段前检查是否有人在录制
qiumingdll_init();

if (qiumingdll_procdetect_streaming() == 1)
{
    // 有人在录屏/直播：暂停剧情并提示
    show_message("检测到录屏或直播软件，请关闭后再继续观看本段剧情");
    // ...... 挂起剧情逻辑
}
else
{
    // 环境干净，正常播放剧情
}
```

## 相关函数

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_init](qiumingdll_init.md)