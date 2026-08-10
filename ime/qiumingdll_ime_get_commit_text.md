# qiumingdll_ime_get_commit_text()

获取本次输入确认上屏的提交文本，读取后该文本会被清空。

## 函数签名

```gml
qiumingdll_ime_get_commit_text()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| String | 本次要提交上屏的文本（UTF-8）；没有新的提交文本时返回 "" |

非 Windows 平台始终返回 ""。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 ""。
- 前置条件：先调用 `qiumingdll_ime_get_state` 确认状态位含 0x02（有新的提交文本）；否则通常读到 ""（因为上一次读取已把它清空）。
- **一次性语义**：提交文本被读取后立即清空，同一段文本不会被读到第二次。若漏读（如游戏暂停期间），该段提交文本会一直缓存到下一次读取时一并返回。
- 提交文本可能包含多段输入的累积（组合上屏时拼接），一次读取返回全部内容。
- 文本为 UTF-8 编码，可直接追加到 GML 字符串中使用。
- 典型用法：把返回值追加到游戏内文本变量（如聊天输入框已确认文本）。
- 简化替代：`qiumingdll_ime_get_commit` 内部自动判断状态位 0x02，无需手动先查状态。

## 示例

```gml
// Step 事件：检测到提交文本时上屏
var state = qiumingdll_ime_get_state();
if (state & 2) { // 有新的提交文本
    var commit = qiumingdll_ime_get_commit_text();
    if (commit != "") {
        input_text += commit; // 追加到已确认文本
    }
}
```

## 相关函数

- [qiumingdll_ime_get_commit](qiumingdll_ime_get_commit.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)