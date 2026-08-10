# qiumingdll_ime_input_create(x, y, w, h, [font])

创建"IME 输入框"一站式解决方案：初始化输入框并创建全部 `ime_` 前缀实例变量。

## 函数签名

```gml
qiumingdll_ime_input_create(x, y, w, h, [font])
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| x | Real | 是 | 输入框左上角 X 坐标 |
| y | Real | 是 | 输入框左上角 Y 坐标 |
| w | Real | 是 | 输入框宽度（像素） |
| h | Real | 是 | 输入框高度（像素） |
| font | Font Asset | 否 | 指定字体资源；不传时使用 -1（默认字体） |

## 返回值

无返回值（本函数不返回任何值）。

## 使用说明

- 在对象的 Create 事件中调用一次。调用后必须配套使用：Step 事件调 `qiumingdll_ime_input_step()`，Draw 事件调 `qiumingdll_ime_input_draw()`（或 draw_text + draw_candidates），清理事件调 `qiumingdll_ime_input_cleanup()`。
- 自动平台检测：Windows 且 DLL 扩展已初始化 → `ime_use_dll = true`，并自动调用 `qiumingdll_ime_fix_conflict()` 修复输入法冲突；其他平台或扩展未初始化 → `ime_use_dll = false`，回退到 `keyboard_string` 方案（无组合文本与候选列表）。
- 调用后实例拥有以下变量（可直接读写定制）：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| ime_x / ime_y / ime_w / ime_h | 传入值 | 输入框位置和大小 |
| ime_text | "" | 已确认的文本 |
| ime_max_length | 0 | 最大字符数，0=不限 |
| ime_focused | true | 是否获得焦点（false 时 step/draw 不工作） |
| ime_composing | false | 是否正在组合输入 |
| ime_comp_text | "" | 当前组合文本 |
| ime_comp_cursor | 0 | 组合文本光标位置 |
| ime_cand_list | ds_list | 候选列表（ds_list，请勿手动销毁） |
| ime_cand_sel | -1 | 当前选中候选索引 |
| ime_input_mode | 0 | 输入模式（0=英文，1=中文） |
| ime_use_dll | 自动 | 是否使用 DLL 方案（平台检测结果） |
| ime_kb_string | "" | 回退模式下 keyboard_string 缓存 |
| ime_cursor_blink | 0 | 光标闪烁计时器（0~59 循环） |
| ime_on_commit | -1 | 提交回调脚本索引（-1=不使用） |
| ime_on_compose_change | -1 | 组合变化回调脚本索引（-1=不使用） |
| ime_on_mode_change | -1 | 输入模式变化回调脚本索引（-1=不使用） |
| ime_color_bg / ime_color_text / ime_color_comp / ime_color_cursor | 白/黑/蓝/红 | 背景、文本、组合文本、光标颜色 |
| ime_color_cand_bg / ime_color_cand_text | 黑/白 | 候选框背景、候选文本颜色 |
| ime_color_cand_sel_bg / ime_color_cand_sel_text | 藏青/黄 | 候选选中项背景、文本颜色 |
| ime_font | -1 | 字体（-1=默认字体） |

- 回调脚本不是脚本资源时也可以是方法变量（内部用 `script_execute` 调用）。
- 建议在创建后立即设置需要的 `ime_*` 变量（如颜色、字体、回调），再开始输入。

## 示例

```gml
// Create 事件：创建输入框并注册回调
qiumingdll_ime_input_create(100, 200, 320, 32);
ime_max_length = 30;                       // 最多 30 字
ime_font = fnt_chat;                       // 自定义字体
ime_color_bg = c_silver;                   // 自定义背景
ime_on_commit = scr_on_ime_commit;         // 注册提交回调
ime_on_compose_change = scr_on_ime_compose;// 注册组合变化回调
ime_on_mode_change = scr_on_ime_mode;      // 注册模式变化回调
```

```gml
// 回调脚本 scr_on_ime_commit(commit_text) —— 提交文本上屏
show_debug_message("提交: " + commit_text);
```

```gml
// 回调脚本 scr_on_ime_compose(composing, comp_text, comp_cursor)
show_debug_message("组合中: " + string(composing) + " " + comp_text + " 光标@" + string(comp_cursor));
```

```gml
// 回调脚本 scr_on_ime_mode(mode) —— 0=英文 1=中文
show_debug_message("输入模式: " + (mode == 1 ? "中文" : "英文"));
```

## 相关函数

- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)
- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_input_cleanup](qiumingdll_ime_input_cleanup.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)