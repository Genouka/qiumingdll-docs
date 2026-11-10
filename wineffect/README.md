# wineffect 模块

窗口级特效：直接改变**游戏窗口本身**的位置和形状，不截屏、不复制窗口内容、不创建覆盖层。适用于剧情演出、故障/horror 桥段、整蛊关卡等场景。

三种效果可以单独或同时开启，强度分别控制（0.0 ~ 1.0），速度倍率统一控制动画快慢。

| 效果 | 作用对象 | 实现方式 |
|------|----------|----------|
| 颤动（shake） | 窗口位置 | `SetWindowPos` 按正弦轨迹移动真实窗口，最大位移约 24px |
| 扭曲（distort） | 窗口轮廓 | `SetWindowRgn` 把左右边缘按正弦波逐行收缩，最大收缩约 48px |
| 撕裂（tear） | 窗口轮廓 + 位置 | `SetWindowRgn` 生成错位横条、缺口、纵向裂缝，并叠加窗口跳动 |

> 扭曲/撕裂改变的是**窗口轮廓和可见区域**，画面随窗口区域被裁剪；本模块不做画面重采样（那属于窗口内容特效）。窗口被裁掉的区域会直接露出桌面/下层窗口。

- 动画在游戏窗口的 UI 线程上通过 16ms `WM_TIMER` + 窗口子类驱动，不创建后台线程。
- 停止/清理时恢复窗口原始位置；启用时（`set_enabled(1)`）窗口已有的 `SetWindowRgn` 区域也会被保存并在停止时还原。
- 窗口最小化、不可见或失去前台时自动暂停并还原，回到前台后继续。
- 最大化窗口无法移动，颤动/撕裂跳动会自动跳过；区域效果仍可用。
- 独占全屏（Exclusive Fullscreen）下效果可能不可见；窗口化 / 无边框全屏正常。
- 不要与 winself 的异形窗口同时使用：两者都会修改窗口区域，后设置的会覆盖前一个。

共 9 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_wineffect_init](qiumingdll_wineffect_init.md) | 绑定游戏窗口（不启动特效）。 |
| [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md) | 总开关：启用 / 停止并还原窗口。 |
| [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md) | 设置窗口颤动强度。 |
| [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md) | 设置窗口轮廓扭曲强度。 |
| [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md) | 设置窗口撕裂强度。 |
| [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md) | 设置动画速度倍率。 |
| [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md) | 立即停止并把三种强度清零。 |
| [qiumingdll_wineffect_get_state](qiumingdll_wineffect_get_state.md) | 查询启用/各效果/是否正在生效。 |
| [qiumingdll_wineffect_cleanup](qiumingdll_wineffect_cleanup.md) | 解除绑定并释放全部资源。 |

[返回文档首页](../README.md)
