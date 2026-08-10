# qiumingdll_winsplit_show(splitId)

显示指定的分裂窗口（若之前被隐藏），不激活它、不抢焦点。

## 函数签名

```gml
qiumingdll_winsplit_show(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 显示成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 与 `qiumingdll_winsplit_hide` 成对使用；创建时窗口默认就是显示的，不调用 hide 则无需调用本函数。
- 显示方式不激活窗口（SW_SHOWNA），不会把焦点从游戏窗口夺走，适合多窗口游戏场景。
- 隐藏的分裂窗口不参与画面显示，但内部状态（位置、大小、源区域）均保留，重新显示时恢复原状。

## 示例

```gml
// 在控制对象的 Step 事件中：按 0 键切换 1 号分裂窗口的显示/隐藏
if (keyboard_check_pressed(ord("0")))
{
    global.split_visible = !global.split_visible;
    if (global.split_visible)
        qiumingdll_winsplit_show(global.split_1);
    else
        qiumingdll_winsplit_hide(global.split_1);
}
```

## 相关函数

- [qiumingdll_winsplit_hide](qiumingdll_winsplit_hide.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)