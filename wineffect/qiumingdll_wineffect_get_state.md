# qiumingdll_wineffect_get_state()

查询窗口特效的当前状态，返回位掩码。

## 函数签名

```gml
qiumingdll_wineffect_get_state()
```

## 参数说明

无参数。

## 返回值

| 位 | 值 | 说明 |
|----|----|------|
| 0 | 1 | 已启用（`set_enabled(1)` 成功） |
| 1 | 2 | 颤动强度 > 0 |
| 2 | 4 | 扭曲强度 > 0 |
| 3 | 8 | 撕裂强度 > 0 |
| 4 | 16 | 当前正在生效（已安装定时器，且未因失焦/最小化/不可见而暂停） |

例如返回 `19`（1+2+16）表示已启用、颤动开启、正在绘制。

## 使用说明

- 可以直接用 `&` 判断某一位，例如 `if (state & 16)` 判断特效是否正在显示。
- 未初始化时返回 0。
- 已启用但三种强度都为 0 时，只返回位 0。
- 窗口失焦/最小化时，位 4 会暂时清零，但强度和启用状态保留。

## 示例

```gml
var st = qiumingdll_wineffect_get_state();
if (st & 16) {
    draw_text(8, 8, "窗口特效运行中");
}
if (st & 8) {
    draw_text(8, 24, "撕裂已开启");
}
```

## 相关函数

- [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md)
- [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md)
