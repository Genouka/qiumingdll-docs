# qiumingdll_winsplit_exists(splitId)

判断指定的分裂窗口 ID 是否有效（是否已创建且尚未销毁）。

## 函数签名

```gml
qiumingdll_winsplit_exists(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 要检查的分裂窗口 ID，取值 1 ~ 16 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | splitId 有效：在 1~16 范围内且该分裂窗口存在（包括被隐藏的窗口） |
| 0 | splitId 无效：不在 1~16 范围，或该槽位当前没有活跃窗口；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：无（未初始化时也安全返回 0）。
- 与 `qiumingdll_winsplit_get_count` 不同，本函数检查的是"某个具体 ID 是否可用"，适合在调用其他函数前做防御性检查。
- 隐藏中的窗口（被 hide）仍返回 1；只有销毁后才返回 0。
- 槽位会被复用：如果 split_1 被销毁后，新建的窗口恰好占用了编号 1 的槽位，则 exists(1) 再次返回 1，但此时它对应的是新窗口。

## 示例

```gml
// 在控制对象的 Step 事件中：对已不存在的分裂窗口执行操作前先检查
if (keyboard_check_pressed(ord("S")))
{
    // 确保窗口还存在再调整它的位置
    if (qiumingdll_winsplit_exists(global.split_1))
    {
        qiumingdll_winsplit_set_position(global.split_1, mouse_x, mouse_y);
    }
    else
    {
        show_debug_message("分裂窗口不存在，请先创建");
    }
}
```

## 相关函数

- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)