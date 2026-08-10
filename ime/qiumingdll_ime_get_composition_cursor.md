# qiumingdll_ime_get_composition_cursor()

获取组合文本中光标的位置（字符偏移，从 0 开始）。

## 函数签名

```gml
qiumingdll_ime_get_composition_cursor()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| Real | 组合文本中的光标位置（字符偏移，从 0 开始）；非组合状态通常为 0 |

非 Windows 平台始终返回 0。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 0。
- 前置条件：与组合文本配套使用；先确认 `qiumingdll_ime_get_state` 状态位含 0x01 再调用。
- 数值是**字符偏移**而非字节偏移，例如组合文本 "nihao"，光标在第 3 个字符后即返回 3，可直接用于 `string_copy(comp, 1, cursor)` 截取光标前的部分。
- 组合过程中用户按 ←/→ 移动光标时，该值会同步更新，需持续轮询。
- 典型用途：在组合文本中画出正确的光标竖线位置，以及组合文本下划线的分段。
- 返回值不会超过当前组合文本的字符数。

## 示例

```gml
// 在组合文本中绘制光标竖线
var state = qiumingdll_ime_get_state();
if (state & 1) {
    var comp  = qiumingdll_ime_get_composition_text();
    var cur   = qiumingdll_ime_get_composition_cursor();
    var baseX = input_x + string_width(input_text);
    // 光标前的文本宽度，决定竖线位置
    var curX  = baseX + string_width(string_copy(comp, 1, cur));
    draw_line(curX, input_y, curX, input_y + string_height(comp));
}
```

## 相关函数

- [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md)