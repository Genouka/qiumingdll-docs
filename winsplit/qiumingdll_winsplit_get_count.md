# qiumingdll_winsplit_get_count()

返回当前存在的分裂窗口总数（0 ~ 16），用于槽位管理、UI 显示等。

## 函数签名

```gml
qiumingdll_winsplit_get_count()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 ~ 16 | 当前活跃（未被销毁）的分裂窗口数量；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用（未初始化时返回 0）。
- 与 get_info/get_count 这一族查询函数类似，本函数是只读查询，不产生副作用。
- 数量上限为 16：当返回值达到 16 时，调用 `qiumingdll_winsplit_create` 必然返回 0（槽位耗尽）。需要先销毁若干窗口才能再创建。
- 隐藏（hide）的窗口仍计入数量；只有销毁（destroy）后才不计入。

## 示例

```gml
// 在控制对象的 Step 事件中：按 C 创建一个小地图分裂窗口，但先检查是否还有槽位
if (keyboard_check_pressed(ord("C")))
{
    if (qiumingdll_winsplit_get_count() < 16)
    {
        global.split_minimap = qiumingdll_winsplit_create(0, 0, 400, 300, 50, 50, 400, 300);
    }
    else
    {
        show_debug_message("分裂窗口数量已达上限（16 个），无法继续创建");
    }
}

// 在 Draw GUI 事件中显示数量
draw_text(10, 10, "分裂窗口数量: " + string(qiumingdll_winsplit_get_count()) + "/16");
```

## 相关函数

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_exists](qiumingdll_winsplit_exists.md)