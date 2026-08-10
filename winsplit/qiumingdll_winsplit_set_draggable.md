# qiumingdll_winsplit_set_draggable(splitId, draggable)

设置指定分裂窗口是否允许被鼠标拖动移动位置。开启后用户可直接用鼠标拖动窗口。

## 函数签名

```gml
qiumingdll_winsplit_set_draggable(splitId, draggable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| draggable | Real/Bool | 是 | 是否可拖动：非 0（true）= 可拖动，0（false）= 不可拖动 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 创建时默认 `draggable = false`（不可拖动）。
- 有标题栏时，按住标题栏拖动窗口；无标题栏时，按住窗口任意位置拖动。
- 拖动只会移动窗口位置，不影响窗口尺寸、源区域、形状等属性；被拖到的新位置可通过 `qiumingdll_winsplit_get_info(splitId, 0/1)` 查到。
- 重要行为差异：开启可拖动后，分裂窗口内的鼠标事件（点击、移动、滚轮等）不再转发给原游戏窗口。如果分裂窗口承担"游戏交互画面"功能（例如在分裂窗口里点击游戏按钮），请保持不可拖动，游戏才能收到你的点击。
- 与动画位置相比，拖动是用户主动行为，两者互不干扰（动画结束后窗口停在动画终点）。

## 示例

```gml
// 在控制对象的 Step 事件中：按 G 切换 1 号分裂窗口的"可拖动"开关
if (keyboard_check_pressed(ord("G")))
{
    global.split_draggable = !global.split_draggable;
    qiumingdll_winsplit_set_draggable(global.split_1, global.split_draggable);

    if (global.split_draggable)
        show_debug_message("分裂窗口已开启拖动（鼠标事件不再转发给游戏）");
    else
        show_debug_message("分裂窗口已锁定（点击将转发给游戏）");
}
```

## 相关函数

- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)