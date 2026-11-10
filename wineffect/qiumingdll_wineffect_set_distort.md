# qiumingdll_wineffect_set_distort(intensity)

设置窗口轮廓扭曲强度。窗口左右边缘会按正弦波逐行收缩，形成波浪状轮廓。

## 函数签名

```gml
qiumingdll_wineffect_set_distort(intensity)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| intensity | Real | 是 | 0.0 ~ 1.0；越界自动钳制。0 = 关闭扭曲。1.0 时边缘最大收缩约 48 像素 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：未绑定窗口（需先调用 `qiumingdll_wineffect_init()`） |

## 使用说明

- 前置条件：先调用 `qiumingdll_wineffect_init()`。
- 通过 `SetWindowRgn` 修改**窗口区域**：波浪边缘以外的窗口部分会被裁掉，露出桌面/下层窗口。
- 这是窗口轮廓扭曲，不是画面重采样；窗口内容不会缩放或平移，只会被裁剪。
- 可以与 `set_tear()` 同时开启，两者会合并成同一个窗口区域。
- 窗口最大化时仍然生效。
- 停止时恢复启用时保存的原始窗口区域；若原窗口没有区域则恢复为完整矩形。

## 示例

```gml
/// 故障演出：窗口边缘开始波动
qiumingdll_wineffect_set_distort(0.5);
qiumingdll_wineffect_set_enabled(1);

/// 演出结束
qiumingdll_wineffect_set_distort(0);
```

## 相关函数

- [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md)
- [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md)
- [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md)
