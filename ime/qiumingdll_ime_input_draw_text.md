# qiumingdll_ime_input_draw_text()

仅绘制输入框的文本部分（已确认文本 + 组合文本 + 下划线 + 光标），不绘制背景与候选列表，适用于自定义渲染。

## 函数签名

```gml
qiumingdll_ime_input_draw_text()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| Real | 文本末尾的 X 坐标：已确认文本与组合文本绘制完后光标所在位置（未聚焦时返回 `ime_x`），便于在其后继续绘制其他内容 |

## 使用说明

- 前置条件：必须先调用 `qiumingdll_ime_input_create` 创建输入框。
- 绘制起点为 (ime_x, ime_y)（左上角对齐，不做垂直居中，与 `qiumingdll_ime_input_draw` 不同）。
- `ime_focused` 为 false 时直接返回 `ime_x`，不绘制任何内容。
- 绘制内容：
  1. 已确认文本：`ime_color_text`，起点 (ime_x, ime_y)；
  2. 组合文本（组合中且非空时）：`ime_color_comp` 紧跟已确认文本之后，下方画下划线（颜色同组合文本色，基线在 ime_y + 行高处）；
  3. 组合光标：按 `ime_comp_cursor` 画竖线（`ime_color_cursor`）；
  4. 无组合时：绘制闪烁光标（闪烁节奏同 `ime_cursor_blink`）。
- 返回值计算：已确认文本宽度 + 组合文本宽度（即返回 `ime_x + string_width(ime_text)` 或再加上组合文本宽度）。
- 典型用法：自定义输入框背景/位置时，用本函数画文字，把返回的 X 传给其他绘制（如图标、按钮），候选框可以用 `qiumingdll_ime_input_draw_candidates` 单独画。
- 本函数会修改当前字体/颜色设置。

## 示例

```gml
// Draw 事件：自定义渲染 —— 文本 + 末尾图标 + 候选框
var endX = qiumingdll_ime_input_draw_text();
// 在文本末尾绘制一个装饰图标
draw_sprite(spr_input_icon, 0, endX + 6, ime_y);
// 候选框画在图标下方
qiumingdll_ime_input_draw_candidates(endX + 6, ime_y + string_height("A") + 12);
```

## 相关函数

- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_input_draw_candidates](qiumingdll_ime_input_draw_candidates.md)
- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)