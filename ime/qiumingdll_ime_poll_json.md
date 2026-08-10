# qiumingdll_ime_poll_json()

一次性轮询所有 IME 状态并返回 JSON 字符串。

## 函数签名

```gml
qiumingdll_ime_poll_json()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| String | JSON 字符串，包含全部 IME 状态（键见下表） |

非 Windows 平台始终返回 "{}"。

JSON 各键说明：

| 键 | 类型 | 说明 |
|----|------|------|
| composing | Boolean | 是否正在组合输入 |
| compText | String | 当前组合文本 |
| compCursor | Real | 组合文本中的光标位置（字符偏移） |
| commitText | String | 提交文本（一次性，读取后清空，下次不再出现） |
| candidates | Array | 候选词字符串数组 |
| candidateSel | Real | 当前选中候选索引（-1=无选中） |
| inputMode | Real | 输入模式：0=英文，1=中文 |
| stateFlags | Real | 状态变化标志位掩码（0x01/0x02/0x04/0x08 的按位或） |

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 "{}"。
- 与逐项轮询（`qiumingdll_ime_get_state` + 各 get_* 函数）的区别：一次调用即可拿到全部状态，无需先查标志位；代价是需要解析 JSON。
- 副作用：调用后一次性标志（0x02/0x04/0x08）与提交文本会被清空，`commitText` 只在本帧返回一次。
- 文本均为 UTF-8，可直接解析使用。
- 推荐解析方式：`json_parse` 得到 ds_map + ds_list，或直接用便捷封装 `qiumingdll_ime_poll`（返回 ds_map，内部自动完成解析并保证 candidates 存在）。
- 性能：底层一次字符串构建，每帧调用开销极小，可放心每帧轮询。

## 示例

```gml
// 每帧轮询并解析
var json = qiumingdll_ime_poll_json();
if (json != "{}") {
    var map = json_parse(json);
    if (map != undefined) {
        var commit = ds_map_find_value(map, "commitText");
        if (commit != "") {
            input_text += commit;
        }
        var composing = ds_map_find_value(map, "composing");
        if (composing) {
            var comp = ds_map_find_value(map, "compText");
            // 组合文本由自己绘制
        }
        json_destroy(map); // 释放解析结果
    }
}
```

## 相关函数

- [qiumingdll_ime_poll](qiumingdll_ime_poll.md)
- [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)