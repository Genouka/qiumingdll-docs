# qiumingdll_wineffect_set_enabled(enable)

总开关：启用或停止窗口特效。停止时会立即还原窗口位置和窗口区域。

## 函数签名

```gml
qiumingdll_wineffect_set_enabled(enable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| enable | Real | 是 | 非 0 = 启用；0 = 停止并还原窗口 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 操作成功 |
| 0 | 失败：尚未调用 `qiumingdll_wineffect_init()`，或窗口无效，或子类/定时器安装失败 |

## 使用说明

- 前置条件：必须先调用 `qiumingdll_wineffect_init()`。
- 启用后会安装窗口子类和 16ms 定时器；所有强度为 0 时不会产生视觉效果，但状态位仍显示"已启用"。
- 停止（enable=0）会恢复窗口位置和启用时保存的原始窗口区域；三种强度值会保留，重新启用后继续生效。
- 窗口最小化、不可见或失去前台时，特效会自动暂停并还原；回到前台后自动继续。
- 最大化窗口不能移动：颤动和撕裂跳动会被跳过，扭曲/撕裂的区域效果仍然生效。

## 示例

```gml
/// 进入故障房间时开启
qiumingdll_wineffect_set_shake(0.6);
qiumingdll_wineffect_set_enabled(1);

/// 离开房间时停止并还原
qiumingdll_wineffect_set_enabled(0);
```

## 相关函数

- [qiumingdll_wineffect_init](qiumingdll_wineffect_init.md)
- [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md)
- [qiumingdll_wineffect_get_state](qiumingdll_wineffect_get_state.md)
