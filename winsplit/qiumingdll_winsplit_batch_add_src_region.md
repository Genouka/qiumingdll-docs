# qiumingdll_winsplit_batch_add_src_region(splitId, srcX, srcY, srcW, srcH, durationMs)

在批处理录制中添加一条"源区域变换"命令：播放时在 durationMs 毫秒内把源区域（主窗口上截取的图像区域）从当前值插值到目标区域。

## 函数签名

```gml
qiumingdll_winsplit_batch_add_src_region(splitId, srcX, srcY, srcW, srcH, durationMs)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16 |
| srcX | Real | 是 | 目标源区域左上角 X 坐标（主窗口客户区坐标系，单位像素） |
| srcY | Real | 是 | 目标源区域左上角 Y 坐标（主窗口客户区坐标系，单位像素） |
| srcW | Real | 是 | 目标源区域宽度（单位像素） |
| srcH | Real | 是 | 目标源区域高度（单位像素） |
| durationMs | Real | 是 | 该段动画时长，单位毫秒；传 0 表示跳过过渡，命令开始时立即到位 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 命令添加成功 |
| 0 | 添加失败：splitId 无效、未在录制中、或命令数已达上限 32 条；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先 qiumingdll_winsplit_batch_begin 进入录制状态，且尚未 qiumingdll_winsplit_batch_end。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 本命令只改变源区域（画面内容"平移/缩放取景"），不改变窗口位置与尺寸，效果类似于在摄像头画面中平移取景框。
- 不使用源动画模式（模式对该命令无效），也不消耗窗口外的其他状态。
- 缓动取添加命令时设定的批处理缓动曲线。
- 命令起始状态取"该命令开始执行时刻"的源区域，命令按顺序首尾相接。

## 示例

```gml
// 按键事件：录制"取景框先右移再回中"的序列
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    // 主窗口客户区为 640x480，先把取景框移到右侧
    qiumingdll_winsplit_batch_add_src_region(global.splitId, 320, 0, 320, 480, 500);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 300);
    // 取景框回中
    qiumingdll_winsplit_batch_add_src_region(global.splitId, 160, 0, 320, 480, 500);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## 相关函数

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_add_wait](qiumingdll_winsplit_batch_add_wait.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)