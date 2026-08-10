# qiumingdll_winsplit_set_titlebar(splitId, hasTitleBar)

设置指定分裂窗口是否有标题栏（含窗口边框与系统按钮）。切换时窗口客户区尺寸保持不变，外框大小和左上角会相应调整。

## 函数签名

```gml
qiumingdll_winsplit_set_titlebar(splitId, hasTitleBar)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| hasTitleBar | Real/Bool | 是 | 是否有标题栏：非 0（true）= 有标题栏（默认），0（false）= 无边框无标题栏 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 创建时默认 `hasTitleBar = true`（有标题栏）。
- 设置的目标值与当前值相同（如已是无标题栏又设置 false）时直接返回 1，不做任何操作。
- 切换会重建窗口样式：客户区（画面显示区域）尺寸保持不变，因此窗口外框总尺寸相应增减，且为保持客户区左上角对齐，窗口左上角位置会微调（可通过 get_info 0/1 查询新位置）。
- 无标题栏（false）的窗口更干净，适合"纯画面"用途；但无可视关闭按钮，系统菜单关闭入口也消失，若需要保留关闭能力请配合关闭相关行为（closable 仍控制 WM_CLOSE 响应，程序仍可用 destroy 销毁）。
- 有标题栏时配合 `qiumingdll_winsplit_set_title` 可显示自定义标题；配合 `qiumingdll_winsplit_set_closable` 可控制 X 按钮是否可用。

## 示例

```gml
// 在控制对象的 Step 事件中：按 N 切换 1 号分裂窗口的标题栏
if (keyboard_check_pressed(ord("N")))
{
    global.split_has_title = !global.split_has_title;
    qiumingdll_winsplit_set_titlebar(global.split_1, global.split_has_title);

    if (global.split_has_title)
        qiumingdll_winsplit_set_title(global.split_1, "预览窗口");
}
```

## 相关函数

- [qiumingdll_winsplit_set_title](qiumingdll_winsplit_set_title.md)
- [qiumingdll_winsplit_set_closable](qiumingdll_winsplit_set_closable.md)
- [qiumingdll_winsplit_set_draggable](qiumingdll_winsplit_set_draggable.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)