# qiumingdll_ime_poll()

一次性轮询所有 IME 状态，解析为 GML 的 ds_map 并返回。

## 函数签名

```gml
qiumingdll_ime_poll()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 键 | 类型 | 说明 |
|----|------|------|
| "composing" | Real | 是否正在组合输入（0/1） |
| "compText" | String | 当前组合文本 |
| "compCursor" | Real | 组合文本光标位置（字符偏移） |
| "commitText" | String | 提交文本（一次性，读取后清空） |
| "candidates" | ds_list | 候选词列表，元素为 String |
| "candidateSel" | Real | 当前选中候选索引（-1=无选中） |
| "inputMode" | Real | 输入模式：0=英文，1=中文 |
| "stateFlags" | Real | 状态变化标志位掩码 |

- 非 Windows 平台或扩展未初始化时：返回一个空的 ds_map（无任何键）。
- JSON 解析失败时同样返回空的 ds_map。

## 使用说明

- 平台限制：仅 Windows 平台返回完整数据；其他平台返回空 ds_map（可安全 `ds_map_size` 判断为空）。
- **内存管理（重要）**：返回的 ds_map 使用完毕后必须调用 `qiumingdll_ime_poll_destroy(map)` 销毁（该方法会一并销毁内部的 candidates ds_list），否则每帧调用会造成内存泄漏。
- "candidates" 键恒存在：即使没有候选，也会是一个空的 ds_list，可直接使用 `ds_list_size` / `ds_list_find_value` 而不必判空。
- commitText 为一次性数据：本帧读取后即被清空，下一帧不再返回同一段提交文本。
- 与 `qiumingdll_ime_poll_json` 的关系：本函数内部即调用 poll_json 再解析，是更方便的 GML 侧封装。
- ime_input 系列封装内部使用的就是本函数，不需要再手动调用。

## 示例

```gml
// Step 事件：轮询并处理全部状态
var m = qiumingdll_ime_poll();

// 提交文本上屏
var commit = ds_map_find_value(m, "commitText");
if (commit != "") {
    input_text += commit;
}

// 组合状态
if (ds_map_find_value(m, "composing")) {
    var comp = ds_map_find_value(m, "compText");
    var cur  = ds_map_find_value(m, "compCursor");
    // 绘制组合文本与光标 ...
}

// 候选列表
var candList = ds_map_find_value(m, "candidates");
var candCount = ds_list_size(candList);
for (var i = 0; i < candCount; i++) {
    show_debug_message(string(i) + ": " + ds_list_find_value(candList, i));
}

// 使用完毕必须销毁，防止内存泄漏
qiumingdll_ime_poll_destroy(m);
```

## 相关函数

- [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)