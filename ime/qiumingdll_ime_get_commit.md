# qiumingdll_ime_get_commit()

简化版提交文本获取：内部自动检查状态位 0x02，有提交则返回提交文本，否则返回空字符串。

## 函数签名

```gml
qiumingdll_ime_get_commit()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| "" | 当前没有新的提交文本 |
| String | 新的提交文本（UTF-8）；内部调用了 `qiumingdll_ime_get_commit_text`，读取后即清空 |

非 Windows 平台始终返回 ""。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 ""。
- 等价逻辑：`var s = qiumingdll_ime_get_state(); return (s & 2) ? qiumingdll_ime_get_commit_text() : "";`，即在 GML 包装层完成"查状态 → 读文本"两步。
- 与 `qiumingdll_ime_get_commit_text` 的区别：本函数自动判断状态位，调用者无需关心 0x02 标志；两者都是一次性读数语义（读后清空）。
- 注意：本函数内部会调用 `qiumingdll_ime_get_state`，这会消费一次性标志。如果你在同一帧中还需要用状态位判断其他数据（组合、候选、模式），请先调用 `qiumingdll_ime_get_state` 保存结果，再按需读取。
- 适合简单场景：每帧调用一次，返回值非空即上屏，代码最精简。

## 示例

```gml
// Step 事件：最简单的上屏逻辑
var commit = qiumingdll_ime_get_commit();
if (commit != "") {
    chat_text += commit; // 组合确认后自动上屏
}
```

```gml
// 与其他状态判断共存：先取状态，再读提交
var state = qiumingdll_ime_get_state();
if (state & 2) {
    chat_text += qiumingdll_ime_get_commit_text();
}
```

## 相关函数

- [qiumingdll_ime_get_commit_text](qiumingdll_ime_get_commit_text.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)