# qiumingdll_ime_get_candidate_count()

获取当前候选列表中的候选词数量。

## 函数签名

```gml
qiumingdll_ime_get_candidate_count()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| Real | 当前候选词数量；0 表示当前没有候选列表 |

非 Windows 平台始终返回 0。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 0。
- 前置条件：与候选列表相关的读取应在 `qiumingdll_ime_get_state` 状态位含 0x04（候选列表变化）后执行；但本函数在未变化时读取也能返回当前数量。
- 候选列表与当前组合输入相关：组合输入过程中候选变换频繁；组合结束或候选框关闭后数量为 0。
- 底层最多保留 50 个候选词（超出部分被截断），返回值最大为 50。
- 常与 `qiumingdll_ime_get_candidate(index)` 配合遍历绘制候选框。

## 示例

```gml
// 候选变化时打印全部候选词
var state = qiumingdll_ime_get_state();
if (state & 4) {
    var n = qiumingdll_ime_get_candidate_count();
    show_debug_message("候选数量: " + string(n));
    for (var i = 0; i < n; i++) {
        show_debug_message(string(i) + ": " + qiumingdll_ime_get_candidate(i));
    }
}
```

## 相关函数

- [qiumingdll_ime_get_candidate](qiumingdll_ime_get_candidate.md)
- [qiumingdll_ime_get_candidate_selection](qiumingdll_ime_get_candidate_selection.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)