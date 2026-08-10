# qiumingdll_ime_input_draw_candidates(x, y)

仅绘制候选列表（候选框背景 + 边框 + 候选项 + 选中高亮），可指定绘制位置。

## 函数签名

```gml
qiumingdll_ime_input_draw_candidates(x, y)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| x | Real | 否 | 候选框左上角 X 坐标；不传时使用默认位置（ime_x + 6 + 已确认文本宽度） |
| y | Real | 否 | 候选框左上角 Y 坐标；不传时使用默认位置（ime_y + ime_h + 4） |

## 返回值

无返回值（本函数不返回任何值）。

## 使用说明

- 前置条件：必须先调用 `qiumingdll_ime_input_create` 创建输入框。
- x/y 为可选参数：**不传则使用默认位置**（与 `qiumingdll_ime_input_draw` 内置的候选框位置一致）；传入两个参数则绘制在指定位置。
- 当候选列表为空（`ime_cand_list` 大小为 0）时直接返回，不绘制任何内容。
- 绘制内容：
  1. 背景：半透明（alpha 0.9）实心矩形，颜色 `ime_color_cand_bg`；
  2. 边框：`ime_color_cand_bg` 与白色 3:7 混合色；
  3. 候选项：格式为"序号. 文本"（序号从 1 开始，即 "1. 候选一"），每行高度 = 行高 + 6 像素；颜色 `ime_color_cand_text`；
  4. 选中项（索引等于 `ime_cand_sel`）：以 `ime_color_cand_sel_bg` 高亮背景 + `ime_color_cand_sel_text` 高亮文本色显示。
- 候选框宽度：取所有候选项"序号. 文本"的宽度最大值 + 16，最小 100 像素。
- 通常与 `qiumingdll_ime_input_draw_text` 搭配实现完全自定义的输入框渲染；默认位置即设计为显示在输入框正下方。
- 应放在调用 `qiumingdll_ime_input_step` 之后（保证 `ime_cand_list` 为最新数据）。
- 本函数会修改当前颜色/alpha/字体设置。

## 示例

```gml
// 默认位置绘制候选框（与完整输入框效果一致）
qiumingdll_ime_input_draw_candidates();
```

```gml
// 自定义位置：把候选框跟随鼠标
var endX = qiumingdll_ime_input_draw_text();
qiumingdll_ime_input_draw_candidates(mouse_x, mouse_y);
```

## 相关函数

- [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md)
- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)