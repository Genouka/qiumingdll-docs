# qiumingdll_wineffect_set_speed(speed)

设置窗口特效的动画速度倍率。三种效果共用同一个速度。

## 函数签名

```gml
qiumingdll_wineffect_set_speed(speed)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| speed | Real | 是 | 0.0 ~ 8.0；越界自动钳制。默认 1.0；0 = 冻结动画（保持当前姿态） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：未绑定窗口（需先调用 `qiumingdll_wineffect_init()`） |

## 使用说明

- 前置条件：先调用 `qiumingdll_wineffect_init()`。
- speed 影响颤动/扭曲的相位推进速度，也影响撕裂布局的刷新间隔。
- speed = 0 时动画冻结：窗口保持当前位移和当前区域形状，直到重新设置非 0 速度或停止效果。
- 运行中修改速度是平滑的，不会重置当前相位。

## 示例

```gml
// 慢动作故障
qiumingdll_wineffect_set_speed(0.35);
qiumingdll_wineffect_set_enabled(1);

// 恢复正常速度
qiumingdll_wineffect_set_speed(1.0);
```

## 相关函数

- [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md)
- [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md)
- [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md)
