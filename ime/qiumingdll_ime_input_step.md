# qiumingdll_ime_input_step()

在 Step 事件中轮询 IME 状态并更新输入框内部数据（文本、组合、候选、回调）。

## 函数签名

```gml
qiumingdll_ime_input_step()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

无返回值（本函数不返回任何值）。

## 使用说明

- 前置条件：必须先调用 `qiumingdll_ime_input_create` 创建输入框（本函数依赖其创建的 `ime_*` 变量）。
- 在对象的 Step 事件（或 End Step）中每帧调用一次。
- `ime_focused` 为 false 时本函数直接退出，不做任何处理（顺便说明：`ime_focused` 可用来让输入框失去焦点后停止接收输入）。
- DLL 模式（`ime_use_dll == true`）内部流程：
  1. 更新光标闪烁计时（`ime_cursor_blink`，0~59 循环）；
  2. 每帧自动调用 `qiumingdll_ime_set_inline_position(ime_x + 6 + string_width(ime_text), ime_y + 4)`，让系统组合窗口跟随到文本末尾；
  3. 调用 `qiumingdll_ime_poll` 一次性轮询全部状态；
  4. 处理提交文本：追加到 `ime_text`，受 `ime_max_length` 限制（0=不限）；超限时既不追加也不触发回调；
  5. 更新组合状态：写入 `ime_composing` / `ime_comp_text` / `ime_comp_cursor`；组合状态或文本变化时触发组合变化回调；
  6. 复制候选列表到 `ime_cand_list`（ds_list 拷贝），更新 `ime_cand_sel`；
  7. 输入模式变化时更新 `ime_input_mode` 并触发模式变化回调；
  8. 调用 `qiumingdll_ime_poll_destroy` 销毁轮询返回的 ds_map；
  9. DLL 模式下退格键需要手动处理：组合未进行时按退格删除 `ime_text` 最后一个字符。
- 回退模式（`ime_use_dll == false`，非 Windows）内部流程：
  1. 对比 `keyboard_string` 与缓存 `ime_kb_string`，把新增字符追加到 `ime_text`（同样受最大长度限制），并触发提交回调；
  2. 退格键同步删除文本与 keyboard_string；
  3. 组合与候选相关变量复位（组合文本清空、候选清空）。
- 回调脚本参数（对应 `ime_on_*` 变量，-1 表示不使用）：
  - `ime_on_commit(commit_text)`：每次成功上屏的文本；
  - `ime_on_compose_change(composing, comp_text, comp_cursor)`：组合开始/结束或组合文本变化时；
  - `ime_on_mode_change(mode)`：输入法模式变化（0=英文，1=中文）。
- 回调可传脚本资源索引或方法变量（内部用 `script_execute` 执行）。

## 示例

```gml
// Step 事件
qiumingdll_ime_input_step();
```

```gml
// Create 事件中注册方法变量形式的回调（需要 GameMaker 2022.2+）
qiumingdll_ime_input_create(100, 200, 320, 32);
ime_on_commit = method(self, function(_text) {
    chat_log += _text; // 每段上屏文本都记入聊天记录
});
```

## 相关函数

- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)
- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_poll](qiumingdll_ime_poll.md)
- [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md)