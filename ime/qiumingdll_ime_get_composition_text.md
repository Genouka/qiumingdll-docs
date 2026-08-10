# qiumingdll_ime_get_composition_text()

获取当前输入法的组合文本（拼音/笔画等尚未确认上屏的字符串）。

## 函数签名

```gml
qiumingdll_ime_get_composition_text()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| String | 当前组合文本；未在组合时返回空字符串 "" |

非 Windows 平台始终返回 ""。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 ""。
- 前置条件：先调用 `qiumingdll_ime_get_state` 确认状态位含 0x01（正在组合）时调用才有意义；未组合时返回 ""。
- 组合文本会随用户输入实时变化（每敲一个拼音字母都会更新），需要持续轮询才能获得最新内容。
- 文本为 UTF-8 编码，GML 字符串可直接拼接、比较、绘制，中文无需额外转码。
- 本函数是只读的，不会清空或修改组合状态。
- 组合结束（按下空格/选择候选上屏）后组合文本变为 ""，此时应停止绘制组合文本。
- 若只需要判断"是否在组合"，用 `qiumingdll_ime_is_composing` 更直接（不会扰动状态标志）。

## 示例

```gml
// 每帧检查并绘制组合文本
var state = qiumingdll_ime_get_state();
if (state & 1) { // 正在组合
    var comp = qiumingdll_ime_get_composition_text();
    if (comp != "") {
        draw_set_color(c_blue);
        draw_text(input_x + string_width(input_text), input_y, comp);
    }
}
```

## 相关函数

- [qiumingdll_ime_get_composition_cursor](qiumingdll_ime_get_composition_cursor.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_is_composing](qiumingdll_ime_is_composing.md)