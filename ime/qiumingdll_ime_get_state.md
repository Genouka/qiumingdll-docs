# qiumingdll_ime_get_state()

返回 IME 状态变化标志（位掩码），用于判断接下来该读取哪些数据。

## 函数签名

```gml
qiumingdll_ime_get_state()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 无任何状态变化 |
| 0x01（1） | 正在组合输入。**持续状态**：组合期间一直置位，读取后不清空，组合结束才消失 |
| 0x02（2） | 有新的提交文本。**一次性标志**：读取后清空 |
| 0x04（4） | 候选列表发生变化。**一次性标志**：读取后清空 |
| 0x08（8） | 输入模式发生变化。**一次性标志**：读取后清空 |
| 其他组合值 | 上述标志的按位或，如 5 = 0x01 \| 0x04，7 = 0x01 \| 0x02 \| 0x04 等 |

非 Windows 平台始终返回 0。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 0。
- 轮询式 API：输入法事件不会主动通知 GML，必须每帧（或高频）调用本函数获取变化。
- 标准读取流程（先看标志、再读数据）：
  - 含 0x01 → 读取组合数据：`qiumingdll_ime_get_composition_text` / `qiumingdll_ime_get_composition_cursor`（或直接查 `qiumingdll_ime_is_composing`）；
  - 含 0x02 → 读取提交文本：`qiumingdll_ime_get_commit_text`（或直接用简化版 `qiumingdll_ime_get_commit`）；
  - 含 0x04 → 读取候选列表：`qiumingdll_ime_get_candidate_count` / `qiumingdll_ime_get_candidate` / `qiumingdll_ime_get_candidate_selection`；
  - 含 0x08 → 输入模式已变化，可用 `qiumingdll_ime_get_mode` 查询新模式（`qiumingdll_ime_poll_json` 的 inputMode 字段亦可）。
- 一次性标志（0x02/0x04/0x08）被读取后立即清空，同一标志不会在下一帧重复出现；持续标志（0x01）不受影响。
- 组合结束（含按下确认键上屏）同样会置位 0x01 供你察觉，此时组合文本为空字符串。
- 若觉得逐项读取繁琐，可改用 `qiumingdll_ime_poll_json` / `qiumingdll_ime_poll` 一次性获取全部状态。

## 示例

```gml
// Step 事件：按状态位读取相应数据
var state = qiumingdll_ime_get_state();

if (state & 2) { // 有新的提交文本
    var commit = qiumingdll_ime_get_commit_text();
    total_text += commit;
}

if (state & 1) { // 正在组合
    var comp = qiumingdll_ime_get_composition_text();
    var cur  = qiumingdll_ime_get_composition_cursor();
    // 绘制组合文本与光标 ...
}

if (state & 4) { // 候选列表变化
    var n = qiumingdll_ime_get_candidate_count();
    for (var i = 0; i < n; i++) {
        show_debug_message("候选" + string(i) + ": " + qiumingdll_ime_get_candidate(i));
    }
}

if (state & 8) { // 输入模式变化
    show_debug_message("输入模式: " + string(qiumingdll_ime_get_mode()));
}
```

## 相关函数

- [qiumingdll_ime_get_commit_text](qiumingdll_ime_get_commit_text.md)
- [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md)
- [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)