# qiumingdll_cursor_get_invert()

查询当前是否处于"光标与鼠标移动相反"状态。

## 函数签名

```gml
qiumingdll_cursor_get_invert()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 光标反向效果当前处于开启状态 |
| 0 | 未开启（从未开启、已手动关闭，或已被 8 次 F12 安全阀取消） |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows。
- 行为细节：玩家用 F12 安全阀取消效果后，本函数也会返回 0，可用于 UI 提示是否需要重新开启。
- 本函数只是查询，不会改变效果状态。

## 示例

```gml
/// Step 事件：效果生效期间显示提示
if (qiumingdll_cursor_get_invert()) {
    draw_text(8, 8, "鼠标已反向！连按 8 次 F12 解除");
} else {
    draw_text(8, 8, "");
}
```

## 相关函数

- [qiumingdll_cursor_set_invert](qiumingdll_cursor_set_invert.md)
