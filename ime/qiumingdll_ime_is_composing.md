# qiumingdll_ime_is_composing()

查询是否正在组合输入。

## 函数签名

```gml
qiumingdll_ime_is_composing()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 正在组合输入（用户正在拼音/笔画输入过程中） |
| 0 | 未在组合输入 |

非 Windows 平台始终返回 0。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 0。
- 与 `qiumingdll_ime_get_state` 状态位 0x01 含义一致，但本函数不消费一次性标志（0x02/0x04/0x08），在只想判断组合状态时更干净。
- 组合期间系统组合窗口处于内联/隐藏状态，组合文本由游戏自行绘制（见 `qiumingdll_ime_get_composition_text`）。
- 组合期与组合结束的判定：组合开始到确认上屏（或取消）之间返回 1；确认上屏（提交）或取消后返回 0。
- 典型用途：组合期间禁止对已确认文本做退格处理（避免误删），组合结束后恢复。

## 示例

```gml
// Step 事件：组合中不响应退格删除已确认文本
if (keyboard_check_pressed(vk_back)) {
    if (!qiumingdll_ime_is_composing()) {
        if (string_length(text) > 0) {
            text = string_copy(text, 1, string_length(text) - 1);
        }
    }
}
```

## 相关函数

- [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)