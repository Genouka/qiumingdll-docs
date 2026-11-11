# qiumingdll_winsplit_clear_auto_resize(splitId)

取消分屏窗口的 9-Patch 自动跟随。取消后分屏窗口保持当前位置、尺寸与源区域，主窗口再被缩放/移动时不再自动调整。

## 函数签名

```gml
qiumingdll_winsplit_clear_auto_resize(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分屏窗口编号，取值范围 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（即使该窗口从未启用自动跟随也返回 1，本函数幂等） |
| 0 | 调用失败：编号无效或分屏窗口不存在 |
| 0 | 非 Windows 平台：GML 包装函数直接返回 0 |

## 使用说明

- 不会停止正在播放的动画；动画结束后窗口停留在动画结果上，主窗口缩放不再干预。
- 取消后可随时用 `qiumingdll_winsplit_set_auto_resize_9patch` 重新启用（以调用时刻的客户区作为新的设计尺寸）。
- destroy / cleanup 时跟随状态随窗口一并销毁。

## 示例

```gml
/// 玩家关闭"画面复制"功能
qiumingdll_winsplit_clear_auto_resize(splitId);
qiumingdll_winsplit_set_region(splitId, 100, 100, 400, 225);
```

## 相关函数

- [qiumingdll_winsplit_set_auto_resize_9patch](qiumingdll_winsplit_set_auto_resize_9patch.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
