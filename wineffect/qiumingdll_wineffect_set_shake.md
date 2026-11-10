# qiumingdll_wineffect_set_shake(intensity)

设置窗口颤动强度。窗口会以正弦叠加轨迹在屏幕上快速移动。

## 函数签名

```gml
qiumingdll_wineffect_set_shake(intensity)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| intensity | Real | 是 | 0.0 ~ 1.0；越界自动钳制。0 = 关闭颤动。1.0 时最大位移约 24 像素 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：未绑定窗口（需先调用 `qiumingdll_wineffect_init()`） |

## 使用说明

- 前置条件：先调用 `qiumingdll_wineffect_init()`；可在 `set_enabled(1)` 之前或之后设置。
- 作用对象是**真实窗口位置**，不是窗口内容；窗口的非客户区、标题栏、阴影会一起移动。
- 窗口最大化时无法移动，本效果会被跳过；请先还原窗口。
- 特效运行期间游戏自己移动窗口（如拖拽）会被跟随，停止时回到最后一次检测到的基准位置。
- 停止时（`set_enabled(0)` / `stop()` / `cleanup()`）窗口会精确回到基准位置。

## 示例

```gml
/// 受击时抖一下
qiumingdll_wineffect_set_shake(1.0);
qiumingdll_wineffect_set_enabled(1);
alarm[0] = 12;   // 0.2 秒后关闭

/// Alarm 0
qiumingdll_wineffect_set_shake(0);
```

## 相关函数

- [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md)
- [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md)
- [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md)
