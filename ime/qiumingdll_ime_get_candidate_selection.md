# qiumingdll_ime_get_candidate_selection()

获取当前候选列表中选中的候选索引。

## 函数签名

```gml
qiumingdll_ime_get_candidate_selection()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| Real | 当前选中的候选索引（从 0 开始，与 `qiumingdll_ime_get_candidate` 的索引一致） |
| -1 | 当前没有选中的候选（如候选列表为空、没有候选被选中） |

非 Windows 平台始终返回 -1。

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 -1。
- 前置条件：候选列表有效（状态位 0x04 后读取）时调用有意义；无候选时返回 -1。
- 返回值可能与 `qiumingdll_ime_get_candidate_count` 搭配使用：选中索引恒小于候选数量（无选中时为 -1）。
- 用户按 ←/→ 键或数字键切换候选时，选中索引会同步变化；需要轮询才能反映最新选中项。
- 典型用途：绘制候选框时高亮当前选中项（与 `qiumingdll_ime_get_candidate` 配合），或直接按数字键上屏对应候选。

## 示例

```gml
// 绘制候选框，且高亮选中项
var n = qiumingdll_ime_get_candidate_count();
var sel = qiumingdll_ime_get_candidate_selection();
for (var i = 0; i < n; i++) {
    var label = string(i + 1) + ". " + qiumingdll_ime_get_candidate(i);
    if (i == sel) {
        draw_set_color(c_yellow); // 选中项高亮
    } else {
        draw_set_color(c_white);
    }
    draw_text(cand_x, cand_y + i * 20, label);
}
```

## 相关函数

- [qiumingdll_ime_get_candidate](qiumingdll_ime_get_candidate.md)
- [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)