# qiumingdll_ime_get_candidate(index)

获取指定索引的候选词文本。

## 函数签名

```gml
qiumingdll_ime_get_candidate(index)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| index | Real | 是 | 候选索引，从 0 开始；有效范围是 0 ~ `qiumingdll_ime_get_candidate_count()-1` |

## 返回值

| 值 | 说明 |
|----|------|
| String | 对应索引的候选词文本（UTF-8） |
| "" | 索引无效（越界）或当前没有候选列表 |

非 Windows 平台始终返回 ""。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 ""。
- 索引越界不会报错，而是返回空字符串 ""，因此可以安全地按数量遍历而不必担心越界。
- 候选列表内容随组合输入实时变化（状态位 0x04 后读取最新列表）。
- 文本为 UTF-8 编码，可直接绘制或拼接。
- 典型用途：遍历所有候选词绘制候选框，并借助 `qiumingdll_ime_get_candidate_selection` 高亮选中项。

## 示例

```gml
// 遍历并绘制候选词（每行一个）
var n = qiumingdll_ime_get_candidate_count();
for (var i = 0; i < n; i++) {
    var cand = qiumingdll_ime_get_candidate(i);
    if (cand == "") break; // 防御：索引无效时停止
    var label = string(i + 1) + ". " + cand;
    draw_text(cand_x, cand_y + i * 20, label);
}
```

## 相关函数

- [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md)
- [qiumingdll_ime_get_candidate_selection](qiumingdll_ime_get_candidate_selection.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)