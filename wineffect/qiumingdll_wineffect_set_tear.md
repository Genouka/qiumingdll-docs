# qiumingdll_wineffect_set_tear(intensity)

设置窗口撕裂强度。窗口会被切成错位的横条，并随机出现缺口、纵向裂缝和小幅跳动。

## 函数签名

```gml
qiumingdll_wineffect_set_tear(intensity)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| intensity | Real | 是 | 0.0 ~ 1.0；越界自动钳制。0 = 关闭撕裂。1.0 时最大错位约 120 像素 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：未绑定窗口（需先调用 `qiumingdll_wineffect_init()`） |

## 使用说明

- 前置条件：先调用 `qiumingdll_wineffect_init()`。
- 通过 `SetWindowRgn` 生成带缺口/裂缝的窗口区域；被裁掉的部分会露出桌面或下层窗口。
- 撕裂布局每隔约 60~140ms 随机刷新一次，同时叠加小幅窗口位置跳动，形成"窗口被撕开"的感觉。
- 与 `set_distort()` 同时开启时，撕裂的错位会叠加在扭曲轮廓上。
- 强度越高：切片越多、错位越大、缺口/裂缝越明显、跳动越强。
- 停止时恢复原始窗口区域和位置。
- 注意：撕裂期间窗口被裁掉的区域不再参与鼠标命中测试，点击会落到下层窗口；这是异形窗口的正常行为。

## 示例

```gml
/// 强烈故障：撕裂 + 轻微抖动
qiumingdll_wineffect_set_tear(0.8);
qiumingdll_wineffect_set_shake(0.2);
qiumingdll_wineffect_set_enabled(1);

/// 恢复正常
qiumingdll_wineffect_set_tear(0);
qiumingdll_wineffect_set_shake(0);
```

## 相关函数

- [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md)
- [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md)
- [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md)
