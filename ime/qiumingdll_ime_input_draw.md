# qiumingdll_ime_input_draw()

绘制完整的 IME 输入框：背景 + 边框 + 已确认文本 + 组合文本 + 下划线 + 光标 + 候选框。

## 函数签名

```gml
qiumingdll_ime_input_draw()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

无返回值（本函数不返回任何值）。

## 使用说明

- 前置条件：必须先调用 `qiumingdll_ime_input_create` 创建输入框。
- 在对象的 Draw 事件（或 Draw GUI，取决于你使用的坐标体系）中每帧调用一次，通常在 `qiumingdll_ime_input_step` 之后。
- `ime_focused` 为 false 时本函数直接退出，什么都不绘制。
- 绘制内容（由 `ime_color_*` 与 `ime_font` 变量控制外观）：
  1. 背景：以 `ime_color_bg` 填充的实心矩形（位置 ime_x, ime_y，尺寸 ime_w, ime_h）；
  2. 边框：`ime_color_text` 与灰色 1:1 混合色的矩形边框；
  3. 已确认文本：`ime_color_text` 绘制，起点 ime_x+6，垂直居中；
  4. 组合文本（组合中且非空时）：`ime_color_comp` 紧跟已确认文本之后，下方绘制下划线；
  5. 组合光标：按 `ime_comp_cursor` 在组合文本中画竖线（`ime_color_cursor`）；
  6. 无组合时：绘制闪烁光标（`ime_cursor_blink` 前 30 帧可见，之后隐藏）；
  7. 候选列表（非空时）：在默认位置（ime_x + 6 + 已确认文本宽度，ime_y + ime_h + 4）绘制候选框，序号从 1 开始（"1. 候选一"格式），选中项以高亮背景 + 高亮文本色显示；候选框宽度取所有候选项文本宽度最大值 + 16，最小 100。
- 若想自定义布局（如候选框出现在鼠标旁、文本不垂直居中），建议改用 `qiumingdll_ime_input_draw_text` + `qiumingdll_ime_input_draw_candidates` 组合。
- 本函数会修改当前绘图颜色/字体/alpha 设置，调用后如需恢复请自行保存（`draw_get_color` 等）。

## 示例

```gml
// Draw 事件：直接绘制完整输入框
qiumingdll_ime_input_draw();
```

```gml
// 示例：输入框的完整用法（Create / Step / Draw / Clean Up 四个事件）
// Create:  qiumingdll_ime_input_create(50, 300, 400, 36);
// Step:    qiumingdll_ime_input_step();
// Draw:    qiumingdll_ime_input_draw();
// Clean Up: qiumingdll_ime_input_cleanup();
```

## 相关函数

- [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md)
- [qiumingdll_ime_input_draw_candidates](qiumingdll_ime_input_draw_candidates.md)
- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)